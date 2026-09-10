"""Regression tests for the 2026-09-10 heartbeat blackout fix."""

from datetime import datetime
from types import SimpleNamespace

import pytest

from cobalt.heartbeat import runner
from cobalt.heartbeat.probes import Probe
from cobalt.heartbeat.render import Beat
from cobalt.session.clock import ET


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


def install_healthy_stages(monkeypatch, store, *, alerts, writes):
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

    monkeypatch.setattr(runner, "write_note_block", write)


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
def test_none_or_exception_is_failed_red_persisted_and_corrected(
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
