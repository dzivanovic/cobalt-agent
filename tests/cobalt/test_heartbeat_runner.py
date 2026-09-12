"""Regression tests for heartbeat staging and daily-note absence."""

from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

import pytest

from cobalt.heartbeat import runner
from cobalt.heartbeat.probes import Probe
from cobalt.heartbeat.render import Beat
from cobalt.session.clock import ET
from cobalt.vaultwrite import VaultWriteError


# Reduced from the actual 2026-09-11 daily note: the production marker shape
# and stable unit id are preserved; journal/probe content is incidental here.
REAL_HEARTBEAT_NOTE = """# Daily note

<!-- cobalt:section heartbeat -->
<!-- cobalt:unit status -->
🟢 **HEARTBEAT GREEN** · prior beat
<!-- /cobalt:unit status -->
<!-- /cobalt:section heartbeat -->
"""


def et(day: int, hour: int, minute: int) -> datetime:
    return datetime(2026, 9, day, hour, minute, tzinfo=ET)


class FakeStore:
    def __init__(self, *, fail_finalize: bool = False, kill_active: bool = False):
        self.calls = []
        self.row = {"last_result": {"green_summary_date": "2026-09-02"}}
        self.fail_finalize = fail_finalize
        self.kill_active = kill_active
        self.persist_count = 0

    def kill_switch(self):
        return {
            "active": self.kill_active,
            "phrase": "COBALT STOP" if self.kill_active else None,
            "set_by": "test" if self.kill_active else None,
            "set_at": None,
        }

    def get(self, _label):
        return self.row

    def ensure_schema(self):
        self.calls.append("ensure_schema")

    def register(self, _spec):
        self.calls.append("register")

    def record_heartbeat_result(
        self, _label, *, result, vault_outcome, vault_reason
    ):
        self.persist_count += 1
        self.calls.append("finalize" if self.persist_count == 2 else "persist")
        if self.fail_finalize and self.persist_count == 2:
            raise RuntimeError("final database update unavailable")
        self.row["last_result"].update(result)
        self.row["vault_outcome"] = vault_outcome
        self.row["vault_reason"] = vault_reason


def install_healthy_stages(monkeypatch, store, *, alerts, writes, patch_write=True):
    monkeypatch.setattr(runner, "JobStore", lambda: store)
    monkeypatch.setattr(
        runner,
        "take_beat",
        lambda *, now, probe: Beat(
            at=now.astimezone(ET), probes=[Probe("test", True, "healthy")]
        ),
    )
    monkeypatch.setattr(runner, "should_send_green", lambda beat, store: True)
    monkeypatch.setattr(
        runner,
        "send_dm",
        lambda beat: alerts.append(("dm", beat.dm_body())) or "DM sent",
    )
    monkeypatch.setattr(
        runner,
        "out_of_band",
        lambda beat: alerts.append(("out_of_band", beat.dm_body())) or "email sent",
    )

    def write(*_args, **_kwargs):
        writes.append("attempt")
        return SimpleNamespace(write_id=42, report=lambda: "write_id=42")

    if patch_write:
        monkeypatch.setattr(runner, "write_note_block", write)


def install_note_target(monkeypatch, path: Path, *, result=None, error=None, calls=None):
    """Resolve one temporary note and replace only DB-backed writer plumbing."""
    calls = calls if calls is not None else []
    monkeypatch.setattr("cobalt.daymode.note.daily_note_path", lambda _day: path)

    class Store:
        def __init__(self):
            calls.append("store")

        def ensure_schema(self):
            calls.append("schema")

    class Writer:
        def __init__(self, *_args, **_kwargs):
            calls.append("writer")

        def upsert_unit(self, target, section, unit, body):
            calls.append((target, section, unit, body))
            if error is not None:
                raise error
            return result

    monkeypatch.setattr("cobalt.vaultwrite.VaultWriteStore", Store)
    monkeypatch.setattr("cobalt.vaultwrite.VaultWriter", Writer)
    return calls


def test_market_reset_alerts_persists_and_never_attempts_a_vault_write(monkeypatch):
    store, alerts, writes, session_blocks = FakeStore(), [], [], []
    install_healthy_stages(monkeypatch, store, alerts=alerts, writes=writes)

    def forbidden_write(*_args, **_kwargs):
        writes.append("attempt")
        session_blocks.append("vaultwrite:heartbeat:upsert_unit")
        pytest.fail("market_reset must defer before constructing the vault writer")

    monkeypatch.setattr(runner, "write_note_block", forbidden_write)

    beat = runner.run_beat(now=et(3, 20, 0))

    assert [name for name, _body in alerts] == ["dm"]
    assert writes == []
    assert session_blocks == [], "no vault writer means no vaultwrite:heartbeat:* refusal"
    assert store.row["vault_outcome"] == runner.VAULT_DEFERRED
    assert beat.vault_outcome == runner.VAULT_DEFERRED
    assert beat.green


def test_beat_reports_an_active_kill_switch(monkeypatch):
    store, alerts, writes = FakeStore(kill_active=True), [], []
    install_healthy_stages(monkeypatch, store, alerts=alerts, writes=writes)

    beat = runner.run_beat(now=et(3, 20, 0))

    assert "KILL SWITCH ACTIVE" in beat.kill_switch
    assert "Heartbeat exemption active" in beat.kill_switch
    assert "KILL SWITCH ACTIVE" in store.row["last_result"]["kill_switch"]


@pytest.mark.parametrize("writer_result", [None, RuntimeError("vault exploded")])
def test_unexpected_none_or_exception_is_failed_red_persisted_and_corrected(
    monkeypatch, writer_result
):
    store, alerts, writes = FakeStore(), [], []
    install_healthy_stages(monkeypatch, store, alerts=alerts, writes=writes)

    def write(*_args, **_kwargs):
        writes.append("attempt")
        if isinstance(writer_result, BaseException):
            raise writer_result
        return writer_result

    monkeypatch.setattr(runner, "write_note_block", write)
    beat = runner.run_beat(now=et(3, 19, 59))

    assert writes == ["attempt"]
    assert beat.vault_outcome == runner.VAULT_FAILED
    assert not beat.green
    assert store.row["vault_outcome"] == runner.VAULT_FAILED
    corrective = [body for name, body in alerts if name == "out_of_band"]
    assert len(corrective) == 1
    assert beat.vault_reason in corrective[0]
    assert "RED" in corrective[0]


@pytest.mark.parametrize(
    "at",
    [
        et(11, 0, 13),
        et(11, 5, 14),
        et(12, 4, 0),
        et(12, 20, 30),
        et(7, 20, 30),  # Labor Day is overnight, not market_reset.
    ],
)
def test_absent_daily_note_defers_unconditionally_without_constructing_a_writer(
    monkeypatch, tmp_path, at
):
    note = (tmp_path / f"{at:%Y-%m-%d}.md").resolve()
    store, alerts, writes = FakeStore(), [], []
    install_healthy_stages(
        monkeypatch, store, alerts=alerts, writes=writes, patch_write=False
    )
    monkeypatch.setattr("cobalt.daymode.note.daily_note_path", lambda _day: note)

    def forbidden(*_args, **_kwargs):
        pytest.fail("an absent note must defer before store/writer construction")

    monkeypatch.setattr("cobalt.vaultwrite.VaultWriteStore", forbidden)
    monkeypatch.setattr("cobalt.vaultwrite.VaultWriter", forbidden)

    beat = runner.run_beat(now=at)

    expected_reason = (
        f"daily note absent at {note}; heartbeat status write deferred; "
        "com.cobalt.prefill-daily owns note creation; heartbeat never creates notes (L28.1)"
    )
    assert not note.exists()
    assert beat.vault_outcome == runner.VAULT_DEFERRED_NOTE_ABSENT
    assert beat.vault_reason == expected_reason
    assert beat.green
    assert beat.stage_failures == []
    assert store.row["vault_outcome"] == runner.VAULT_DEFERRED_NOTE_ABSENT
    assert store.row["vault_reason"] == expected_reason
    assert [name for name, _body in alerts if name == "out_of_band"] == []
    assert "deferred_note_absent" in beat.note_body()
    assert expected_reason in beat.dm_body()
    assert expected_reason in beat.console()


def test_0529_prefilled_real_marker_shape_reaches_writer_and_records_written(
    monkeypatch, tmp_path
):
    at = et(11, 5, 29)
    note = (tmp_path / "2026-09-11.md").resolve()
    note.write_text(REAL_HEARTBEAT_NOTE)
    before = note.read_bytes()
    result = SimpleNamespace(
        path=note, action="updated", write_id=42, report=lambda: "write_id=42"
    )
    calls = install_note_target(monkeypatch, note, result=result)
    store, alerts, writes = FakeStore(), [], []
    install_healthy_stages(
        monkeypatch, store, alerts=alerts, writes=writes, patch_write=False
    )

    beat = runner.run_beat(now=at)

    assert beat.vault_outcome == runner.VAULT_WRITTEN
    assert store.row["vault_outcome"] == runner.VAULT_WRITTEN
    assert any(isinstance(call, tuple) and call[:3] == (note, "heartbeat", "status") for call in calls)
    assert note.read_bytes() == before, "the fake DB-backed writer must not alter the fixture"


def test_market_reset_precedes_even_absence_lookup(monkeypatch, tmp_path):
    note = (tmp_path / "2026-09-11.md").resolve()

    def forbidden_resolver(_day):
        pytest.fail("market_reset must return before daily-note resolution")

    monkeypatch.setattr("cobalt.daymode.note.daily_note_path", forbidden_resolver)
    beat = Beat(at=et(11, 20, 0))

    outcome, reason = runner._run_vault_stage(beat, now=beat.at, dry_run=False)

    assert outcome == runner.VAULT_DEFERRED
    assert reason == "session clock resolved market_reset; no vault write was attempted"
    assert not note.exists()


def test_deferred_absence_does_not_mask_an_unrelated_red_probe(monkeypatch, tmp_path):
    at = et(11, 5, 14)
    note = (tmp_path / "2026-09-11.md").resolve()
    store, alerts = FakeStore(), []
    monkeypatch.setattr(runner, "JobStore", lambda: store)
    monkeypatch.setattr(
        runner,
        "take_beat",
        lambda *, now, probe: Beat(
            at=now.astimezone(ET), probes=[Probe("database", False, "down")]
        ),
    )
    monkeypatch.setattr(runner, "should_send_green", lambda *_a: False)
    monkeypatch.setattr(
        runner,
        "send_dm",
        lambda beat: alerts.append(("dm", beat.dm_body())) or "DM sent",
    )
    monkeypatch.setattr(
        runner,
        "out_of_band",
        lambda beat: alerts.append(("out_of_band", beat.dm_body())) or "email sent",
    )
    monkeypatch.setattr("cobalt.daymode.note.daily_note_path", lambda _day: note)
    monkeypatch.setattr(
        "cobalt.vaultwrite.VaultWriteStore",
        lambda: pytest.fail("absent note constructed a store"),
    )

    beat = runner.run_beat(now=at)

    assert beat.vault_outcome == runner.VAULT_DEFERRED_NOTE_ABSENT
    assert not beat.green
    assert beat.red_probes[0].name == "database"
    assert store.row["last_result"]["green"] is False
    assert [name for name, _body in alerts] == ["out_of_band", "dm"]


def test_daily_note_target_errors_and_contract_failure_name_the_resolved_path(
    monkeypatch, tmp_path
):
    note = (tmp_path / "2026-09-11.md").resolve()
    note.write_text(REAL_HEARTBEAT_NOTE)
    install_note_target(monkeypatch, note, result=None)
    beat = Beat(at=et(11, 5, 29))

    with pytest.raises(VaultWriteError, match="writer returned no result") as caught:
        runner.write_note_block(beat, now=beat.at)

    assert str(note) in str(caught.value)


@pytest.mark.parametrize(
    ("action", "dry_run"), [("updated", False), ("unchanged", False), ("updated", True)]
)
def test_idless_result_remains_failed_and_names_its_path(
    monkeypatch, tmp_path, action, dry_run
):
    note = (tmp_path / "2026-09-11.md").resolve()
    result = SimpleNamespace(
        path=note, action=action, write_id=None, report=lambda: f"{action} without id"
    )
    monkeypatch.setattr(runner, "write_note_block", lambda *_a, **_k: result)
    beat = Beat(at=et(11, 5, 29))

    outcome, reason = runner._run_vault_stage(beat, now=beat.at, dry_run=dry_run)

    assert outcome == runner.VAULT_FAILED
    assert reason == (
        f"daily-note target {note}: writer returned action={action} without a write id"
    )


def test_directory_target_is_a_named_failure(monkeypatch, tmp_path):
    note = (tmp_path / "2026-09-11.md").resolve()
    note.mkdir()
    install_note_target(monkeypatch, note)

    with pytest.raises(VaultWriteError, match="not a regular file") as caught:
        runner.write_note_block(Beat(at=et(11, 5, 29)))

    assert str(note) in str(caught.value)


def test_stat_io_error_is_a_named_failure_not_absence(monkeypatch, tmp_path):
    note = (tmp_path / "2026-09-11.md").resolve()
    original_stat = Path.stat
    monkeypatch.setattr("cobalt.daymode.note.daily_note_path", lambda _day: note)

    def broken_stat(path, *args, **kwargs):
        if path == note:
            raise PermissionError("permission denied")
        return original_stat(path, *args, **kwargs)

    monkeypatch.setattr(Path, "stat", broken_stat)

    with pytest.raises(VaultWriteError, match="permission denied") as caught:
        runner.write_note_block(Beat(at=et(11, 5, 29)))

    assert str(note) in str(caught.value)


def test_generic_writer_exception_is_a_named_failure(monkeypatch, tmp_path):
    note = (tmp_path / "2026-09-11.md").resolve()
    note.write_text(REAL_HEARTBEAT_NOTE)
    install_note_target(monkeypatch, note, error=RuntimeError("writer exploded"))

    with pytest.raises(VaultWriteError, match="writer exploded") as caught:
        runner.write_note_block(Beat(at=et(11, 5, 29)))

    assert str(caught.value).startswith(f"daily-note target {note}:")


def test_resolver_failure_names_the_et_date_without_fabricating_a_path(monkeypatch):
    def broken(_day):
        raise RuntimeError("resolver unavailable")

    monkeypatch.setattr("cobalt.daymode.note.daily_note_path", broken)

    with pytest.raises(VaultWriteError) as caught:
        runner.write_note_block(Beat(at=et(11, 5, 29)))

    assert str(caught.value) == (
        "daily-note target unresolved for 2026-09-11: resolver unavailable"
    )


def test_corrective_alert_survives_a_finalize_database_failure(monkeypatch):
    store, alerts, writes = FakeStore(fail_finalize=True), [], []
    install_healthy_stages(monkeypatch, store, alerts=alerts, writes=writes)
    monkeypatch.setattr(runner, "write_note_block", lambda *_a, **_k: None)

    beat = runner.run_beat(now=et(3, 19, 59))

    assert any(name == "out_of_band" for name, _body in alerts)
    assert any("FINALIZE/persist" in failure for failure in beat.stage_failures)


@pytest.mark.parametrize(
    "broken", ["probes", "compose", "alerts", "persist", "vault", "finalize"]
)
def test_a_stage_exception_never_suppresses_later_stages(monkeypatch, broken):
    calls = []
    beat = Beat(at=et(3, 19, 59))
    store = FakeStore()
    monkeypatch.setattr(runner, "JobStore", lambda: store)

    def stage(name, result=None):
        def run(*_args, **_kwargs):
            calls.append(name)
            if name == broken:
                raise RuntimeError(f"{name} broke")
            return result

        return run

    monkeypatch.setattr(runner, "take_beat", stage("probes", beat))
    monkeypatch.setattr(runner, "_compose_beat", stage("compose"))
    monkeypatch.setattr(runner, "_run_alerts", stage("alerts", False))
    monkeypatch.setattr(runner, "_persist_beat", stage("persist"))
    monkeypatch.setattr(
        runner, "_run_vault_stage", stage("vault", (runner.VAULT_DEFERRED, "deferred"))
    )
    monkeypatch.setattr(runner, "_finalize", stage("finalize"))

    result = runner.run_beat(now=et(3, 19, 59))

    assert calls == ["probes", "compose", "alerts", "persist", "vault", "finalize"]
    assert any(broken in failure for failure in result.stage_failures)


@pytest.mark.parametrize(
    ("at", "expected", "attempts"),
    [
        (et(3, 19, 59), runner.VAULT_WRITTEN, 1),
        (et(3, 20, 0), runner.VAULT_DEFERRED, 0),
        (et(3, 20, 59), runner.VAULT_DEFERRED, 0),
        (et(3, 21, 0), runner.VAULT_WRITTEN, 1),
        (et(7, 20, 30), runner.VAULT_WRITTEN, 1),  # Labor Day: overnight
    ],
)
def test_vault_session_boundaries_and_holiday(monkeypatch, at, expected, attempts):
    writes = []

    def write(*_args, **_kwargs):
        writes.append("attempt")
        return SimpleNamespace(write_id=7, report=lambda: "write_id=7")

    monkeypatch.setattr(runner, "write_note_block", write)
    beat = Beat(at=at)

    outcome, _reason = runner._run_vault_stage(beat, now=at, dry_run=False)

    assert outcome == expected
    assert len(writes) == attempts


def test_deferred_never_masks_an_unrelated_red_and_failed_is_red():
    unrelated = Beat(
        at=et(3, 20, 30),
        probes=[Probe("database", False, "down")],
        vault_outcome=runner.VAULT_DEFERRED,
    )
    failed = Beat(
        at=et(3, 19, 59),
        vault_outcome=runner.VAULT_FAILED,
        vault_reason="writer returned no result",
    )

    assert not unrelated.green and "database" in unrelated.dm_body()
    assert not failed.green and "vault write" in failed.headline
    assert "writer returned no result" in failed.dm_body()
