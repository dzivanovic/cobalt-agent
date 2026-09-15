"""Regression tests for heartbeat staging and daily-note absence."""

import re
from datetime import datetime, time, timedelta
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
    monkeypatch.setattr(
        runner,
        "send_summary",
        lambda beat: alerts.append(("summary", beat.summary_body())) or "DM sent",
    )
    monkeypatch.setattr(
        runner,
        "send_dm",
        lambda beat: alerts.append(("dm", beat.dm_body())) or "DM sent",
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

    # All green and nothing changed: no alert, only the 16:30 slot's summary.
    assert [name for name, _body in alerts] == ["summary"]
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
    corrective = [body for name, body in alerts if name == "dm"]
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
    assert [name for name, _body in alerts if name == "dm"] == []
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
    monkeypatch.setattr(runner, "send_summary", lambda *_a: pytest.fail("05:14 is before every slot"))
    monkeypatch.setattr(
        runner,
        "send_dm",
        lambda beat: alerts.append(("dm", beat.dm_body())) or "DM sent",
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
    assert [name for name, _body in alerts] == ["dm"]


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

    assert any(name == "dm" for name, _body in alerts)
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


# ---------------------------------------------------------------------
# 09-14 ruling (option B): transition-only alerting
# ---------------------------------------------------------------------


def _sequenced_beats(monkeypatch, store, sequence, alerts):
    """Drive run_beat once per state; `sequence` is "RED"/"GREEN" per beat."""
    monkeypatch.setattr(runner, "JobStore", lambda: store)
    states = iter(sequence)

    def beat(*, now, probe):
        ok = next(states) == "GREEN"
        return Beat(at=now.astimezone(ET), probes=[Probe("database", ok, "state")])

    monkeypatch.setattr(runner, "take_beat", beat)
    monkeypatch.setattr(
        runner, "send_dm", lambda b: alerts.append(("dm", b.dm_body())) or "DM sent"
    )
    monkeypatch.setattr(
        runner,
        "send_summary",
        lambda b: alerts.append(("summary", b.summary_body())) or "DM sent",
    )
    monkeypatch.setattr(
        runner,
        "write_note_block",
        lambda *_a, **_k: SimpleNamespace(write_id=1, report=lambda: "write_id=1"),
    )


def test_transition_oracle_red_red_red_green_green_alerts_exactly_twice(monkeypatch):
    store, alerts = FakeStore(), []
    # 10:xx ET is past the 07:00 slot; mark it sent so only transitions count.
    store.row["last_result"]["summary_sent"] = {"07:00": "2026-09-15"}
    sequence = ["RED", "RED", "RED", "GREEN", "GREEN"]
    _sequenced_beats(monkeypatch, store, sequence, alerts)

    for i in range(len(sequence)):
        runner.run_beat(now=et(15, 10 + i, 0))

    assert [name for name, _ in alerts].count("dm") == 2
    bodies = [body for name, body in alerts if name == "dm"]
    assert "ENTERED RED: database" in bodies[0]
    assert "RECOVERED: database" in bodies[1]


def test_known_idle_radar_weekend_without_pool_row_is_green():
    from cobalt.heartbeat.probes import radar

    class Pool:
        def pool_row(self, _name):
            return None

    class Settings:
        def values(self):
            return {}

    saturday = et(12, 10, 0)  # 2026-09-12 is a Saturday
    result = radar(saturday, enabled=True, pool_store=Pool(), settings_store=Settings())
    assert result.ok, result.detail
    assert "idle" in result.detail


class _Pool:
    def __init__(self, row):
        self.row = row

    def pool_row(self, _name):
        return self.row


class _Settings:
    def values(self):
        return {}


def _scanning_row(last_scan_at):
    return {"last_scan_at": last_scan_at, "degraded": False, "degraded_sources": [],
            "failed_stage": None, "failed_detail": None, "poll_failures": [], "members": 50}


def test_182s_scan_gap_is_green_at_the_ruled_320s_threshold():
    from cobalt.heartbeat.probes import radar

    beat_at = datetime(2026, 9, 14, 7, 22, 27, tzinfo=ET)  # the 09-14 named event
    green = radar(beat_at, enabled=True, pool_store=_Pool(_scanning_row(beat_at - timedelta(seconds=182))),
                  settings_store=_Settings())
    stale = radar(beat_at, enabled=True, pool_store=_Pool(_scanning_row(beat_at - timedelta(seconds=321))),
                  settings_store=_Settings())
    assert green.ok, green.detail
    assert not stale.ok and "last_scan_at stale" in stale.detail


def test_summary_fires_at_the_ruled_slots_and_only_then():
    assert runner.summary_at() == [time(7, 0), time(16, 30)]
    sent, fired = {}, []
    start = datetime(2026, 9, 14, 0, 0, tzinfo=ET)
    for i in range(2 * 96):  # two days of 15-minute beats
        at = start + timedelta(minutes=15 * i)
        slot = runner.summary_due(at, sent, runner.summary_at())
        if slot:
            fired.append(at)
            sent = {**sent, slot: at.date().isoformat()}
    assert [f"{at:%m-%d %H:%M}" for at in fired] == [
        "09-14 07:00", "09-14 16:30", "09-15 07:00", "09-15 16:30",
    ]


def test_summary_goes_out_on_a_standing_red_without_a_transition_alert(monkeypatch):
    store, alerts = FakeStore(), []
    store.row["last_result"].update(red_probes=["database"], summary_sent={"07:00": "2026-09-14"})
    _sequenced_beats(monkeypatch, store, ["RED"], alerts)

    runner.run_beat(now=et(14, 16, 30))

    assert [name for name, _ in alerts] == ["summary"]
    assert "RED:" in alerts[0][1] and "database" in alerts[0][1]
    assert store.row["last_result"]["summary_sent"] == {"07:00": "2026-09-14", "16:30": "2026-09-14"}


def test_herdr_launchd_probe_is_amber_never_red_and_process_probe_is_untouched():
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.watchdog import supervised_finding

    spec = load_job_registry().spec("com.cobalt.herdr")
    assert spec.launchd_unmanaged
    down = supervised_finding(spec, False, "loaded, not running (last exit 0)")
    up = supervised_finding(spec, True, "loaded, pid 1")
    assert down.ok and down.amber and "launchd unmanaged" in down.detail
    assert up.ok and not up.amber
    beat = Beat(at=et(14, 8, 0), jobs=[down])
    assert beat.green and beat.red_jobs == [] and beat.amber_jobs == [down]
    assert "AMBER:" in beat.summary_body() and "com.cobalt.herdr" in beat.summary_body()


def test_launchd_unmanaged_is_refused_off_a_launchd_resident():
    from pydantic import ValidationError

    from cobalt.jobs.config import JobSpec

    with pytest.raises(ValidationError, match="launchd_unmanaged"):
        JobSpec(label="x", kind="resident", supervisor="self", timeout_s=1, what="x",
                launchd_unmanaged=True)


# --- (e) REPLAY ORACLE over the real production log -------------------
# Read-only. The window is pinned to the triage's own (alerts-triage-
# 2026-09-14.md §3/§4): 48 h ending 2026-09-14 08:00 ET, which holds the
# whole 09-12 08:00–12:16 vault episode. Pinned, so the log growing does
# not move the numbers; skipped where the log is absent (a fresh clone).

HEARTBEAT_LOG = Path.home() / "cobalt" / "logs" / "heartbeat.log"
REPLAY_END = datetime(2026, 9, 14, 8, 0, tzinfo=ET)
REPLAY_START = REPLAY_END - timedelta(hours=48)
_HEADER = re.compile(r"^HEARTBEAT .+  \((\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) E[DS]T\)$")
_SEND = ("Email sent", "DM sent", "email channel DOWN", "email channel OFF", "Mattermost DM FAILED")


def _parse_log(text):
    beats, cur = [], None
    for line in text.splitlines():
        header = _HEADER.match(line)
        if header:
            at = datetime.strptime(header.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=ET)
            cur = {"at": at, "jobs": [], "probes": [], "sends": 0}
            beats.append(cur)
        elif cur is None:
            continue
        elif line.startswith(("RED  ", "??   ")):
            body = line[5:]
            if body.startswith("com.cobalt."):
                cur["jobs"].append((body[:28].strip(), body[29:38].strip(), body[39:]))
            else:
                cur["probes"].append((body[:24].strip(), body[25:]))
        elif line.startswith(_SEND):
            cur["sends"] += 1
    return beats


def _rerate(beat):
    """One logged beat under TODAY's code: (red keys, vault failed)."""
    from cobalt.heartbeat.probes import radar
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.watchdog import supervised_finding

    registry, keys, vault_failed = load_job_registry(), set(), False
    for label, state, detail in beat["jobs"]:
        if state == "failed" and detail.endswith(" [launchd probe]"):
            core = detail.removesuffix(" [launchd probe]")
            if supervised_finding(registry.spec(label), False, core).ok:
                continue
        keys.add(label)
    for name, detail in beat["probes"]:
        if name == "vault unit":
            vault_failed = True
            continue
        if name == "heartbeat stage":
            key = runner._stage_key(detail)
            if key:
                keys.add(key)
            continue
        if name == "radar":
            stale = re.fullmatch(r"last_scan_at stale \((.+)\)", detail)
            if detail == "no radar_pool row for primary":
                row = None
            elif stale and stale.group(1) != "None":
                row = _scanning_row(datetime.fromisoformat(stale.group(1)))
            else:
                keys.add(name)
                continue
            if radar(beat["at"], enabled=True, pool_store=_Pool(row), settings_store=_Settings()).ok:
                continue
        keys.add(name)
    return keys, vault_failed


def replay(beats, start=REPLAY_START, end=REPLAY_END):
    """Feed logged beats through the runner's decision functions."""
    inside = [b for b in beats if start <= b["at"] < end]
    before = [b for b in beats if b["at"] < start]
    prior_keys, prior_vault = _rerate(before[-1]) if before else (set(), False)
    slots, sent = runner.summary_at(), {}
    # Prime the summary dedup from the start day's earlier beats, as the job
    # row would have been — otherwise a cold replay "sends" 07:00 at 08:00.
    for beat in before:
        if beat["at"].date() == start.date():
            slot = runner.summary_due(beat["at"], sent, slots)
            if slot:
                sent = {**sent, slot: beat["at"].date().isoformat()}
    events = []
    for beat in inside:
        keys, vault_failed = _rerate(beat)
        entered, recovered = runner.transitions(prior_keys, keys)
        if entered or recovered:
            events.append((beat["at"], runner.transition_note(entered, recovered)))
        if vault_failed != prior_vault:
            events.append((beat["at"], runner.transition_note(
                {runner.VAULT_KEY} if vault_failed else set(),
                set() if vault_failed else {runner.VAULT_KEY})))
        slot = runner.summary_due(beat["at"], sent, slots)
        if slot:
            sent = {**sent, slot: beat["at"].date().isoformat()}
            events.append((beat["at"], f"SUMMARY {slot}"))
        prior_keys, prior_vault = keys, vault_failed
    return inside, events


@pytest.mark.skipif(not HEARTBEAT_LOG.exists(), reason="production heartbeat.log not on this host")
def test_replay_oracle_collapses_the_last_48h_of_real_beats():
    beats = _parse_log(HEARTBEAT_LOG.read_text(errors="replace"))
    if not beats or beats[0]["at"] >= REPLAY_START:
        pytest.skip("heartbeat.log no longer covers the pinned replay window")
    inside, events = replay(beats)
    day = REPLAY_END - timedelta(hours=24)
    last_24h = [b for b in inside if b["at"] >= day]

    def messages(since):  # a transition = one DM (second channel retired 09-14); a summary = one DM
        return sum(1 for at, _note in events if at >= since)

    # BEFORE (as logged): every beat red; both channels on every beat, plus
    # the vault's corrective email on each failed beat.
    assert len(inside) == 192 and all(b["jobs"] or b["probes"] for b in inside)
    assert sum(b["sends"] for b in last_24h) == 192
    assert sum(b["sends"] for b in inside) == 402

    # AFTER: herdr and radar never transition; the window holds the vault
    # episode's recovery, and otherwise only the two ruled summaries a day.
    alerts = [(f"{at:%m-%d %H:%M}", note) for at, note in events if not note.startswith("SUMMARY")]
    summaries = [(f"{at:%m-%d %H:%M}", note) for at, note in events if note.startswith("SUMMARY")]
    assert alerts == [("09-12 12:24", "RECOVERED: vault unit")]
    assert summaries == [
        ("09-12 16:40", "SUMMARY 16:30"), ("09-13 07:14", "SUMMARY 07:00"),
        ("09-13 16:32", "SUMMARY 16:30"), ("09-14 07:07", "SUMMARY 07:00"),
    ]
    assert messages(REPLAY_START) == 5
    assert messages(day) == 2

    # The whole 09-12 vault episode began before the window (00:12, not the
    # 08:00 the triage saw from its window edge): exactly two transitions.
    _, episode = replay(beats, datetime(2026, 9, 12, 0, 0, tzinfo=ET),
                        datetime(2026, 9, 12, 13, 0, tzinfo=ET))
    assert [(f"{at:%H:%M}", note) for at, note in episode if not note.startswith("SUMMARY")] == [
        ("00:12", "ENTERED RED: vault unit"), ("12:24", "RECOVERED: vault unit"),
    ]


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
