"""F20 C4b — the `cos` and `hitl` heartbeat probes (FINAL §2 probes row, F-27; X9).

RED is `Probe(ok=False)`; there is no AMBER. While the registry row ships
`enabled: false`, both report unknown and are never red. Stores faked.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

from hitl_support import FakeHitlStore

NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def _jobs(heartbeat_at):
    return SimpleNamespace(get=lambda label: {"label": label, "state": "running",
                                              "heartbeat_at": heartbeat_at})


def _turns(state):
    return SimpleNamespace(last_turn=lambda: {"state": state, "error": "constructed"} if state else None)


def test_dead_session_is_red():
    from cobalt.heartbeat import probes

    fresh = probes.cos(NOW, enabled=True, job_store=_jobs(NOW), cos_store=_turns("done"))
    assert fresh.ok and fresh.name == "cos"
    stale = probes.cos(NOW, enabled=True, job_store=_jobs(NOW - timedelta(hours=2)), cos_store=_turns("done"))
    assert not stale.ok and "heartbeat" in stale.detail
    failed = probes.cos(NOW, enabled=True, job_store=_jobs(NOW), cos_store=_turns("failed"))
    assert not failed.ok and "failed" in failed.detail


def test_disabled_row_is_unknown():
    from cobalt.heartbeat import probes

    for probe in (probes.cos(NOW), probes.hitl(NOW)):
        assert probe.ok is True, "never red while the row is enabled: false"
        assert "unknown" in probe.detail and "enabled: false" in probe.detail


def test_pending_past_ttl_and_failed_execution_are_red():
    from cobalt.heartbeat import probes

    store = FakeHitlStore(now=NOW)
    assert probes.hitl(NOW, enabled=True, store=store).ok
    late, _ = store.add(expires_at=NOW - timedelta(minutes=1))
    red = probes.hitl(NOW, enabled=True, store=store)
    assert not red.ok and "past" in red.detail
    store.rows[late]["status"] = "expired"
    store.add(status="failed")
    red = probes.hitl(NOW, enabled=True, store=store)
    assert not red.ok and "failed" in red.detail


def test_the_runner_calls_both(monkeypatch):
    from cobalt.heartbeat import probes, runner

    called: list[str] = []
    for name in ("database", "sheet_http", "sheet_daymode", "obsidian", "mainframe", "herdr",
                 "archiver_freshness", "seat_usage", "backup_freshness", "vaultwrite_blocks",
                 "redactions", "radar", "cos", "hitl"):
        monkeypatch.setattr(probes, name,
                            lambda *a, _n=name, **k: called.append(_n) or probes.Probe(_n, True, "faked"))
    monkeypatch.setattr(runner, "sweep", lambda **k: [])
    beat = runner.take_beat(now=NOW, probe=False)
    names = [p.name for p in beat.probes]
    assert names[-3:] == ["radar", "cos", "hitl"]
