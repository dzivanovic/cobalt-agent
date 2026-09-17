"""Radar store transaction-hook behavior with injected connections."""

import os
from datetime import datetime, timezone
from decimal import Decimal
from types import SimpleNamespace

import pytest

from cobalt.radar.models import ExcludedBy, OpenMember
from cobalt.radar.pool import Action, Transition
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


# ---------------------------------------------------------------------
# S2-P4 STEP-2 (R1): rank_metric / rank_value persistence
# ---------------------------------------------------------------------


class RecordingConn:
    """Records every statement; cursors report rowcount 0 so EXCLUDE falls
    through to its INSERT exactly as a first sighting does."""

    def __init__(self):
        self.statements = []
        self.autocommit = True

    def cursor(self):
        conn = self

        class Cursor:
            rowcount = 0

            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

            def execute(self, sql, params=None):
                conn.statements.append((" ".join(sql.split()), params))

        return Cursor()

    def execute(self, sql, params=None):
        self.statements.append((" ".join(sql.split()), params))
        return SimpleNamespace(description=[], fetchall=lambda: [])

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def commit(self):
        pass

    def rollback(self):
        pass

    def close(self):
        pass


RTH = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def _apply(transitions):
    conn = RecordingConn()
    RadarStore(connect=lambda: conn).apply_membership(
        pool_key="primary", transitions=transitions, scan_id=7, now=RTH, session="rth"
    )
    return conn.statements


def _writes(statements, ticker):
    return [
        (sql, params) for sql, params in statements
        if params and ticker in params and "rank_" in sql
    ]


def test_rank_value_written_on_retain_exclude_insert_with_ranking_metric():
    statements = _apply([
        Transition(ticker="RET", action=Action.RETAIN, sources=["s"], rank=1,
                   rank_metric="rvol", rank_value=Decimal("7.5")),
        Transition(ticker="EXC", action=Action.EXCLUDE, sources=["s"], rank=3,
                   rank_metric="rvol", rank_value=None, excluded_by=ExcludedBy.CONFIG_CAP),
        Transition(ticker="ADM", action=Action.ADMIT, sources=["s"], rank=2,
                   rank_metric="volume", rank_value=Decimal("99")),
    ])
    (retain_sql, retain_params), = _writes(statements, "RET")
    assert "rank_metric=%s, rank_value=%s" in retain_sql
    assert "COALESCE" not in retain_sql
    assert "rvol" in retain_params and Decimal("7.5") in retain_params
    exclude = _writes(statements, "EXC")
    # The in-place UPDATE of a never-admitted episode, then the INSERT it
    # falls through to: both carry the pair.
    assert len(exclude) == 2 and all("rvol" in params for _, params in exclude)
    (insert_sql, insert_params), = [w for w in _writes(statements, "ADM") if w[0].startswith("INSERT")]
    assert "rank_metric,rank_value" in insert_sql
    assert "volume" in insert_params and Decimal("99") in insert_params


def test_hold_update_keeps_the_prior_pair_when_the_transition_carries_none():
    (sql, params), = _writes(
        _apply([Transition(ticker="HLD", action=Action.HOLD, sources=["s"], rank=4)]), "HLD"
    )
    assert "rank_metric=COALESCE(%s::text, rank_metric)" in sql
    assert "rank_value=CASE WHEN %s::text IS NULL THEN rank_value ELSE %s::numeric END" in sql


def test_leave_does_not_touch_the_last_values():
    statements = _apply([Transition(ticker="LVE", action=Action.LEAVE, sources=["s"])])
    assert statements and all("rank_" not in sql for sql, _ in statements)


requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)


@requires_db
@pytest.mark.usefixtures("dev_db_tx")
def test_membership_values_round_trip_retain_and_hold_on_cobalt_dev():
    """0008 applied on cobalt_dev (hub): ADMIT writes the pair, RETAIN
    replaces it, HOLD with no pair keeps it, and the open row validates
    as an OpenMember — the resident scan's own conversion."""
    store = RadarStore("cobalt_dev")
    key = "p4_value_test"

    def apply(scan_id, transition):
        store.apply_membership(pool_key=key, transitions=[transition], scan_id=scan_id, now=RTH, session="rth")

    apply(9900001, Transition(ticker="P4VAL", action=Action.ADMIT, sources=["test"], source="test",
                              rank=1, rank_metric="volume", rank_value=Decimal("1234.5")))
    apply(9900002, Transition(ticker="P4VAL", action=Action.RETAIN, sources=["test"], source="test",
                              rank=1, rank_metric="rvol", rank_value=Decimal("3.25")))
    apply(9900003, Transition(ticker="P4VAL", action=Action.HOLD, sources=["test"], rank=1))
    (row,) = store.members_for_day(key, RTH.date())
    assert (row["rank_metric"], row["rank_value"]) == ("rvol", Decimal("3.250000"))
    (member,) = [OpenMember(**item) for item in store.open_members(key)]
    assert (member.rank_metric, member.rank_value) == ("rvol", Decimal("3.250000"))


def test_open_members_and_members_for_day_select_both_columns():
    conn = RecordingConn()
    store = RadarStore(connect=lambda: conn)
    store.open_members("primary")
    store.members_for_day("primary", RTH.date())
    assert len(conn.statements) == 2
    for sql, _ in conn.statements:
        assert "rank_metric" in sql and "rank_value" in sql

