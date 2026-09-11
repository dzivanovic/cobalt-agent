"""Radar store transaction-hook behavior with injected connections."""

from datetime import datetime, timezone

import pytest

from cobalt.radar.store import RadarStore


class Conn:
    def __init__(self, events):
        self.events = events
        self.autocommit = True

    def execute(self, *_args, **_kwargs):
        self.events.append("execute")

    def commit(self):
        self.events.append("commit")

    def rollback(self):
        self.events.append("rollback")

    def close(self):
        self.events.append("close")


def _row(now):
    return {"pool_key": "primary", "state": "scanning", "degraded": False,
        "degraded_sources": [], "failed_stage": None, "failed_detail": None,
        "sources": [], "session": "rth", "cap": 1, "members": 0,
        "last_scan_id": 1, "last_scan_at": now, "last_scan_ms": 1,
        "last_poll_at": None, "poll_failures": [], "budget": None, "updated_at": now}


def test_before_commit_runs_last_and_exception_rolls_back():
    events = []
    store = RadarStore(connect=lambda: Conn(events))
    now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)

    def gate():
        events.append("gate")
        raise RuntimeError("crossed")

    with pytest.raises(RuntimeError, match="crossed"):
        store.put_pool(_row(now), now=now, before_commit=gate)
    assert events == ["execute", "gate", "rollback", "close"]

