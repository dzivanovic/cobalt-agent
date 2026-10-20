"""F20 C4b — the `cos` and `hitl` heartbeat probes (FINAL §2 probes row, F-27; X9).

RED is `Probe(ok=False)`; there is no AMBER. While the registry row is disabled or OWED,
both report unknown and are never red. Stores faked.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace

import pytest

from hitl_support import FakeHitlStore

NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def _jobs(heartbeat_at):
    return SimpleNamespace(get=lambda label: {"label": label, "state": "running",
                                              "heartbeat_at": heartbeat_at})


def _turns(state):
    return SimpleNamespace(last_turn=lambda: {"state": state, "error": "constructed"} if state else None)


def _owed(labels):
    return lambda: frozenset(labels)


def test_dead_session_is_red(monkeypatch):
    from cobalt.heartbeat import probes
    from cobalt.jobs import watchdog

    monkeypatch.setattr(watchdog, "bootstrap_owed", _owed(()))
    fresh = probes.cos(NOW, enabled=True, job_store=_jobs(NOW), cos_store=_turns("done"))
    assert fresh.ok and fresh.name == "cos"
    stale = probes.cos(NOW, enabled=True, job_store=_jobs(NOW - timedelta(hours=2)), cos_store=_turns("done"))
    assert not stale.ok and "heartbeat" in stale.detail
    failed = probes.cos(NOW, enabled=True, job_store=_jobs(NOW), cos_store=_turns("failed"))
    assert not failed.ok and "failed" in failed.detail


def test_disabled_row_is_unknown():
    from cobalt.heartbeat import probes
    from cobalt.jobs.config import load_job_registry

    for probe in (probes.cos(NOW, enabled=False), probes.hitl(NOW, enabled=False)):
        assert probe.ok is True
        assert "unknown" in probe.detail and "enabled: false" in probe.detail
    if load_job_registry().spec(probes.COS_LABEL).enabled is False:
        for probe in (probes.cos(NOW),):
            assert probe.ok is True
            assert "unknown" in probe.detail and "enabled: false" in probe.detail


def test_pending_past_ttl_and_failed_execution_are_red(monkeypatch):
    from cobalt.heartbeat import probes
    from cobalt.jobs import watchdog

    monkeypatch.setattr(watchdog, "bootstrap_owed", _owed(()))
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


def _never_stamped():
    return SimpleNamespace(get=lambda label: None)


def _counts_raise():
    raise RuntimeError("constructed: hitl tables are not created")


def test_cos_probe_is_unknown_green_while_owed(monkeypatch):
    from cobalt.heartbeat import probes
    from cobalt.jobs import watchdog

    job_store = _never_stamped()
    cos_store = SimpleNamespace(last_turn=lambda: None)
    store = SimpleNamespace(probe_counts=_counts_raise)
    # CONTROL: nothing owed. cos is red (no heartbeat); hitl still raises.
    monkeypatch.setattr(watchdog, "bootstrap_owed", _owed(()))
    red = probes.cos(NOW, enabled=True, job_store=job_store, cos_store=cos_store)
    assert red.ok is False and "no heartbeat" in red.detail
    with pytest.raises(RuntimeError):
        probes.hitl(NOW, enabled=True, store=store)
    monkeypatch.setattr(watchdog, "bootstrap_owed", _owed((probes.COS_LABEL,)))
    owed = probes.cos(NOW, enabled=True, job_store=job_store, cos_store=cos_store)
    assert owed.ok is True and "OWED" in owed.detail
    hitl = probes.hitl(NOW, enabled=True, store=store)
    assert hitl.ok is True and "OWED" in hitl.detail
