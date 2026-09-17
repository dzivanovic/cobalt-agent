"""S2-P4 STEP-3 — F3 picks: a card reaching FILLED records his pick against
Cobalt's rank, inside the fill's own transaction, under SAVEPOINT pick.

Charter F3: "DRC shows his pick and Cobalt's rank for every card". The row
exists now; DRC rendering lands in S3.

Offline tests cover the typed result, the rank/tie arithmetic, the report
and exit code, and the transaction shape of `fill()` on fakes. The
`requires_db` tests run in the suite's rolled-back `cobalt_dev` transaction
and need 0008/0009 applied there (`cobalt db migrate`, hub).
"""

from __future__ import annotations

import argparse
import os
from datetime import date, datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from cobalt.aset.engine import compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
from cobalt.aset.store import AsetStore
from cobalt.cards import picks as picks_mod
from cobalt.cards import store as store_mod
from cobalt.cards.models import Actor, CardState, FillResult, Origin
from cobalt.cards.picks import (
    COHORT_STATES,
    TIE_POLICY,
    CohortEntry,
    PickReportRow,
    rank_in_cohort,
    render_picks_report,
)
from cobalt.cards.store import CardStore

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)

RTH = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)   # the suite's frozen clock
TEST_POOL = "p4_pick_test"


# =====================================================================
# Offline
# =====================================================================


def test_fill_result_is_typed_and_a_recorded_pick_carries_its_id():
    ok = FillResult(transition_ids=[1, 2, 3], pick_recorded=True, pick_id=9)
    assert ok.pick_error is None
    gap = FillResult(transition_ids=[4], pick_recorded=False, pick_id=None,
                     pick_error="UndefinedTable: relation picks does not exist")
    assert not gap.pick_recorded
    with pytest.raises(ValidationError):
        FillResult(transition_ids=[1], pick_recorded=True, pick_id=None)
    with pytest.raises(ValidationError):
        FillResult(transition_ids=[1], pick_recorded=False, pick_id=None)   # no named error
    with pytest.raises(ValidationError):
        FillResult(transition_ids=[], pick_recorded=True, pick_id=1)


def test_card_score_rank_ties_share_a_rank_and_the_cohort_includes_the_picked_card():
    cohort = [
        CohortEntry(card_id=11, card_score=80, state="ARMED"),
        CohortEntry(card_id=12, card_score=70, state="WATCH"),
        CohortEntry(card_id=13, card_score=70, state="FILLED"),   # the pick itself
        CohortEntry(card_id=14, card_score=50, state="TRIGGERED"),
    ]
    assert rank_in_cohort(13, cohort) == 2
    assert rank_in_cohort(12, cohort) == 2
    assert rank_in_cohort(14, cohort) == 4
    assert rank_in_cohort(11, cohort) == 1
    with pytest.raises(picks_mod.PickError, match="not in its own cohort"):
        rank_in_cohort(99, cohort)
    assert "ties share" in TIE_POLICY
    assert COHORT_STATES == ("WATCH", "ARMED", "TRIGGERED")


def _report_row(**overrides):
    base = dict(
        transition_id=100, card_id=7, filled_at=RTH, ticker="AAA", state="FILLED", origin="manual",
        pick_id=1, not_in_pool=False, pool_basis="pool", pool_rank=3, pool_size=50,
        rank_metric="volume", rank_value=Decimal("1234567.000000"), card_score=None,
        card_score_rank=None, focus_top4=None, score_basis="unavailable: S2-P2 not merged",
    )
    base.update(overrides)
    return PickReportRow(**base)


def test_picks_cli_lists_pick_and_rank_for_every_filled_card_and_exits_1_on_missing():
    rows = [
        _report_row(),
        # CLOSED later: still a FILLED transition that day, still a pick.
        _report_row(transition_id=101, card_id=8, ticker="BBB", state="CLOSED", pool_rank=None,
                    not_in_pool=True, rank_metric=None, rank_value=None),
        _report_row(transition_id=102, card_id=9, ticker="CCC", pick_id=None, not_in_pool=None,
                    pool_basis=None, pool_rank=None, pool_size=None, rank_metric=None,
                    rank_value=None, score_basis=None),
    ]
    text, missing = render_picks_report(rows, day=date(2026, 9, 3), cutoff=None)
    assert missing == 1
    lines = text.splitlines()
    aaa = next(line for line in lines if " AAA " in line)
    assert "#3/50" in aaa and "volume 1234567" in aaa and "unavailable: S2-P2 not merged" in aaa
    bbb = next(line for line in lines if " BBB " in line)
    assert "not in pool" in bbb and "CLOSED" in bbb
    ccc = next(line for line in lines if " CCC " in line)
    assert "MISSING" in ccc
    assert "1 MISSING" in lines[-1]


def test_picks_cli_cutoff_keeps_pre_deploy_missing_visible_without_counting_it():
    """R1-7 / K6: only FILLED transitions at/after the P4 deploy cutoff count."""
    cutoff = datetime(2026, 9, 3, 15, 0, tzinfo=timezone.utc)
    rows = [
        _report_row(transition_id=1, card_id=1, ticker="OLD", pick_id=None, filled_at=RTH,
                    not_in_pool=None, pool_basis=None, score_basis=None, pool_rank=None,
                    pool_size=None, rank_metric=None, rank_value=None),
        _report_row(transition_id=2, card_id=2, ticker="NEW", filled_at=cutoff),
    ]
    text, missing = render_picks_report(rows, day=date(2026, 9, 3), cutoff=cutoff)
    assert missing == 0
    assert "MISSING (before cutoff)" in next(line for line in text.splitlines() if " OLD " in line)


def test_picks_cli_command_exit_codes(monkeypatch, capsys):
    from cobalt.cards import cli

    class Store:
        def __init__(self, rows):
            self.rows = rows

        def filled_with_picks(self, day):
            self.day = day
            return self.rows

    missing = [_report_row(pick_id=None, not_in_pool=None, pool_basis=None, score_basis=None,
                           pool_rank=None, pool_size=None, rank_metric=None, rank_value=None).model_dump()]
    monkeypatch.setattr(cli, "_store", lambda: Store(missing))
    with pytest.raises(SystemExit) as exc:
        cli.cmd_picks(argparse.Namespace(date="2026-09-03", cutoff=None))
    assert exc.value.code == 1

    monkeypatch.setattr(cli, "_store", lambda: Store([]))
    cli.cmd_picks(argparse.Namespace(date="2026-09-03", cutoff=None))
    assert "no FILLED transitions on 2026-09-03" in capsys.readouterr().out

    with pytest.raises(SystemExit, match="timezone"):
        cli.cmd_picks(argparse.Namespace(date="2026-09-03", cutoff="2026-09-03T15:00:00"))


class _FakeConn:
    """Records statements; `fail_on` makes one statement raise."""

    def __init__(self, fail_on: str | None = None, fail_commit: bool = False):
        self.statements: list[str] = []
        self.fail_on = fail_on
        self.fail_commit = fail_commit
        self.autocommit = True
        self.committed = self.rolled_back = self.closed = False

    def execute(self, sql, params=None):
        self.statements.append(sql)
        if self.fail_on and self.fail_on in sql:
            raise RuntimeError(f"injected failure on {self.fail_on}")

    def commit(self):
        if self.fail_commit:
            raise RuntimeError("injected commit failure")
        self.committed = True

    def rollback(self):
        self.rolled_back = True

    def close(self):
        self.closed = True


def _fake_store(monkeypatch, conn, *, state=CardState.TRIGGERED, origin=Origin.MANUAL, pick=None):
    store = CardStore("cobalt_dev")
    calls = []
    monkeypatch.setattr(store, "_connect", lambda **_k: conn)
    monkeypatch.setattr(store, "state_of", lambda _id: state)
    monkeypatch.setattr(store, "origin_of", lambda _id: origin)

    def transition(card_id, to_state, *, conn=None, **_kwargs):
        calls.append((to_state, conn))
        return 100 + len(calls)

    monkeypatch.setattr(store, "transition", transition)
    monkeypatch.setattr(picks_mod, "record_pick", pick or (lambda c, card_id, tid, now: 555))
    return store, calls


@pytest.mark.parametrize(
    ("state", "origin", "hops"),
    [
        (CardState.WATCH, Origin.MANUAL, 3),       # the one-click shortcut
        (CardState.ARMED, Origin.MANUAL, 2),
        (CardState.TRIGGERED, Origin.MANUAL, 1),   # strict manual route
        (CardState.TRIGGERED, Origin.RADAR, 1),    # strict radar route
    ],
)
def test_every_fill_route_runs_in_one_transaction_with_the_pick_savepoint(monkeypatch, state, origin, hops):
    conn = _FakeConn()
    store, calls = _fake_store(monkeypatch, conn, state=state, origin=origin)
    result = store.fill(7, actor=Actor.YOU, now=RTH)
    assert len(calls) == hops and all(c is conn for _, c in calls), "every hop on the fill's conn"
    assert result == FillResult(transition_ids=[101 + i for i in range(hops)], pick_recorded=True, pick_id=555)
    assert conn.statements == ["SAVEPOINT pick", "RELEASE SAVEPOINT pick"]
    assert conn.committed and conn.closed and not conn.rolled_back


@pytest.mark.parametrize("state", [CardState.WATCH, CardState.TRIGGERED])
def test_pick_insert_failure_rolls_back_savepoint_only_and_logs_card_and_error_class(monkeypatch, state):
    from loguru import logger

    conn = _FakeConn()

    def failing_pick(c, card_id, tid, now):
        c.execute("INSERT INTO picks -- injected")
        raise KeyError("synthetic pick failure")

    conn.fail_on = None
    store, _ = _fake_store(monkeypatch, conn, state=state, pick=failing_pick)
    messages: list[str] = []
    sink = logger.add(lambda message: messages.append(str(message)), level="ERROR")
    try:
        result = store.fill(7, actor=Actor.YOU, now=RTH)
    finally:
        logger.remove(sink)
    assert result.pick_recorded is False and result.pick_id is None
    assert result.pick_error.startswith("KeyError")
    assert conn.statements[-1] == "ROLLBACK TO SAVEPOINT pick"
    assert conn.committed and not conn.rolled_back, "the fill commits"
    assert any("card 7" in m and "KeyError" in m for m in messages)


def test_a_fill_transaction_failure_never_reports_success(monkeypatch):
    conn = _FakeConn(fail_commit=True)
    store, _ = _fake_store(monkeypatch, conn)
    with pytest.raises(RuntimeError, match="injected commit failure"):
        store.fill(7, actor=Actor.YOU, now=RTH)
    assert conn.rolled_back and conn.closed


def test_a_savepoint_rollback_that_fails_fails_the_fill(monkeypatch):
    conn = _FakeConn(fail_on="ROLLBACK TO SAVEPOINT")

    def failing_pick(c, card_id, tid, now):
        raise RuntimeError("pick broke")

    store, _ = _fake_store(monkeypatch, conn, pick=failing_pick)
    with pytest.raises(RuntimeError, match="ROLLBACK TO SAVEPOINT"):
        store.fill(7, actor=Actor.YOU, now=RTH)
    assert conn.rolled_back and not conn.committed


def test_record_pick_reads_system_tables_qualified_on_the_passed_connection():
    """R1-6: one USER connection, cross-schema reads qualified, no second
    connection or role switch."""
    import inspect

    source = inspect.getsource(picks_mod)
    assert "system.radar_membership" in source and "system.radar_pool" in source
    assert "db.connect" not in source and "SET ROLE" not in source
    assert "commit(" not in source


# =====================================================================
# cobalt_dev (hub): the fill -> pick path end to end
# =====================================================================


def _make_card(ticker: str) -> int:
    result = compute_sizing(
        SizingInput(ticker=ticker, grade=Grade.B, direction=Direction.LONG, sheet_mode=SheetMode.FULL,
                    risk_dollars=Decimal("60"), entry=Decimal("10.00"), stop=Decimal("9.50"),
                    last_price=Decimal("10.01"), price_source="p4-test"),
        [Grade.A, Grade.B],
        Decimal("10"),
    )
    return AsetStore("cobalt_dev").save(result)


def _seed_pool(*, members, degraded=False, failed_stage=None):
    """System rows through the SYSTEM-side store (the suite's shared session)."""
    from cobalt.radar.pool import Action, Transition
    from cobalt.radar.store import RadarStore

    store = RadarStore("cobalt_dev")
    transitions = [
        Transition(ticker=ticker, action=Action.ADMIT, sources=["test"], source="test", rank=rank,
                   rank_metric="volume", rank_value=value)
        for ticker, rank, value in members
    ]
    earlier = datetime(2026, 9, 3, 13, 45, tzinfo=timezone.utc)
    store.apply_membership(pool_key=TEST_POOL, transitions=transitions, scan_id=9910001, now=earlier, session="rth")
    store.put_pool(
        {"pool_key": TEST_POOL, "state": "scanning", "degraded": degraded,
         "degraded_sources": ["list:test"] if degraded else [], "failed_stage": failed_stage,
         "failed_detail": "synthetic" if failed_stage else None, "sources": [], "session": "rth",
         "cap": 50, "members": len(members), "last_scan_id": 9910001, "last_scan_at": earlier,
         "last_scan_ms": 1, "last_poll_at": None, "poll_failures": [], "budget": None, "updated_at": earlier},
        now=earlier,
    )


def _pick_row(card_id):
    with CardStore("cobalt_dev")._connect() as conn:
        cur = conn.execute("SELECT * FROM picks WHERE card_id = %s", (card_id,))
        rows = cur.fetchall()
        columns = [d.name for d in cur.description]
    return [dict(zip(columns, row)) for row in rows]


@pytest.fixture
def pick_pool(monkeypatch):
    monkeypatch.setattr(picks_mod, "configured_pool_key", lambda: TEST_POOL)


@requires_db
@pytest.mark.integration
@pytest.mark.usefixtures("dev_db_tx", "pick_pool")
class TestFillWritesPick:
    def test_fill_writes_exactly_one_pick_row_in_the_fill_transaction(self):
        _seed_pool(members=[("P4PICK", 3, Decimal("1234567"))])
        card_id = _make_card("P4PICK")
        result = CardStore("cobalt_dev").fill(card_id, actor=Actor.YOU, now=RTH)
        assert result.pick_recorded and len(result.transition_ids) == 3
        (row,) = _pick_row(card_id)
        assert row["id"] == result.pick_id
        assert row["transition_id"] == result.transition_ids[-1]
        assert row["picked_at"] == RTH and row["session"] == "rth" and row["origin"] == "manual"

    def test_pick_row_snapshots_pool_rank_metric_and_value_at_pick_time(self):
        _seed_pool(members=[("P4SNAP", 2, Decimal("987.5")), ("P4OTHER", 1, Decimal("2000"))])
        card_id = _make_card("P4SNAP")
        CardStore("cobalt_dev").fill(card_id, actor=Actor.YOU, now=RTH)
        (row,) = _pick_row(card_id)
        assert (row["not_in_pool"], row["pool_basis"], row["pool_rank"], row["pool_size"]) == (False, "pool", 2, 2)
        assert (row["rank_metric"], row["rank_value"]) == ("volume", Decimal("987.500000"))
        assert row["pool_member_id"] is not None and row["pool_scan_id"] == 9910001

    def test_pick_for_ticker_not_in_pool_records_not_in_pool_and_fill_succeeds(self):
        _seed_pool(members=[("P4OTHER", 1, Decimal("2000"))])
        card_id = _make_card("P4NOPOOL")
        result = CardStore("cobalt_dev").fill(card_id, actor=Actor.YOU, now=RTH)
        assert result.pick_recorded
        (row,) = _pick_row(card_id)
        assert (row["not_in_pool"], row["pool_member_id"], row["pool_rank"], row["pool_basis"]) == (True, None, None, "pool")
        assert row["pool_size"] == 1

    @pytest.mark.parametrize("pool", ["missing", "degraded", "failed"])
    def test_degraded_or_missing_pool_row_writes_named_nulls_never_refuses_fill(self, pool):
        if pool == "degraded":
            _seed_pool(members=[("P4DEG", 1, Decimal("5"))], degraded=True)
        elif pool == "failed":
            _seed_pool(members=[("P4DEG", 1, Decimal("5"))], failed_stage="bars")
        card_id = _make_card("P4DEG")
        result = CardStore("cobalt_dev").fill(card_id, actor=Actor.YOU, now=RTH)
        assert result.pick_recorded
        (row,) = _pick_row(card_id)
        assert row["pool_rank"] is None and row["rank_value"] is None and row["not_in_pool"] is True
        assert row["pool_basis"].startswith("unavailable: ")
        assert {"missing": "pool row missing", "degraded": "degraded", "failed": "failed_stage=bars"}[pool] in row["pool_basis"]

    def test_card_score_rank_unavailable_before_p2_named_in_score_basis(self):
        card_id = _make_card("P4NOP2")
        CardStore("cobalt_dev").fill(card_id, actor=Actor.YOU, now=RTH)
        (row,) = _pick_row(card_id)
        with CardStore("cobalt_dev")._connect() as conn:
            p2 = conn.execute(
                "SELECT count(*) FROM information_schema.columns WHERE table_schema = 'user' "
                "AND table_name = 'aset_sizings' AND column_name = 'card_score'"
            ).fetchone()[0]
        if p2:
            pytest.skip("S2-P2's card_score column is present on cobalt_dev")
        assert row["score_basis"] == "unavailable: S2-P2 not merged"
        assert row["card_score"] is None and row["card_score_rank"] is None and row["focus_top4"] is None
        assert row["score_inputs"]["reason"] == "unavailable: S2-P2 not merged"

    def test_score_basis_flips_to_card_score_when_the_p2_columns_are_present(self):
        """§7: when P2 merges after P4, `record_pick` picks the columns up
        with no code change. Simulated inside the rolled-back transaction."""
        cards = CardStore("cobalt_dev")
        with cards._connect() as conn:
            if conn.execute(
                "SELECT 1 FROM pg_constraint WHERE conname = 'aset_sizings_radar_provenance'"
            ).fetchone():
                pytest.skip("real S2-P2 0007 applied: radar cards need provenance; "
                            "the P2 suite owns this path once merged")
            conn.execute("ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS card_score INTEGER, "
                         "ADD COLUMN IF NOT EXISTS conviction NUMERIC(8,6)")
        picked, rival, tied = _make_card("P4SCORE"), _make_card("P4RIVAL"), _make_card("P4TIED")
        with cards._connect() as conn:
            conn.execute("UPDATE aset_sizings SET card_score = 70, conviction = 0.5 WHERE id = %s", (picked,))
            conn.execute("UPDATE aset_sizings SET card_score = 90, conviction = 0.5, origin = 'radar' WHERE id = %s", (rival,))
            conn.execute("UPDATE aset_sizings SET card_score = 70, conviction = 0.5, origin = 'radar' WHERE id = %s", (tied,))
        cards.fill(picked, actor=Actor.YOU, now=RTH)
        (row,) = _pick_row(picked)
        assert (row["score_basis"], row["card_score"], row["card_score_rank"], row["focus_top4"]) == ("card_score", 70, 2, True)
        cohort = row["score_inputs"]["cohort"]
        assert {entry["card_id"] for entry in cohort} >= {picked, rival, tied}
        assert row["score_inputs"]["tie_policy"] == TIE_POLICY

    def test_no_taps_names_the_score_basis(self):
        cards = CardStore("cobalt_dev")
        with cards._connect() as conn:
            conn.execute("ALTER TABLE aset_sizings ADD COLUMN IF NOT EXISTS card_score INTEGER, "
                         "ADD COLUMN IF NOT EXISTS conviction NUMERIC(8,6)")
        card_id = _make_card("P4NOTAP")
        cards.fill(card_id, actor=Actor.YOU, now=RTH)
        (row,) = _pick_row(card_id)
        assert row["score_basis"] == "unavailable: no taps" and row["card_score_rank"] is None

    def test_pick_insert_failure_rolls_back_savepoint_only_fill_commits_banner_and_log(self, monkeypatch):
        real = picks_mod.record_pick

        def broken(conn, card_id, transition_id, now):
            real(conn, card_id, transition_id, now)            # the row is written...
            conn.execute("SELECT 1/0")                           # ...then the savepoint fails
        monkeypatch.setattr(picks_mod, "record_pick", broken)
        card_id = _make_card("P4FAIL")
        cards = CardStore("cobalt_dev")
        result = cards.fill(card_id, actor=Actor.YOU, now=RTH)
        assert not result.pick_recorded and "DivisionByZero" in result.pick_error
        assert cards.state_of(card_id) is CardState.FILLED
        assert _pick_row(card_id) == [], "only the savepoint rolled back"

    def test_picks_cli_reports_savepoint_gap_as_missing(self, monkeypatch):
        monkeypatch.setattr(picks_mod, "record_pick", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("gap")))
        card_id = _make_card("P4GAP")
        cards = CardStore("cobalt_dev")
        cards.fill(card_id, actor=Actor.YOU, now=RTH)
        rows = [PickReportRow(**row) for row in cards.filled_with_picks(date(2026, 9, 3))]
        mine = [row for row in rows if row.card_id == card_id]
        assert len(mine) == 1 and mine[0].pick_id is None
        text, missing = render_picks_report(rows, day=date(2026, 9, 3), cutoff=None)
        assert missing >= 1 and "MISSING" in next(line for line in text.splitlines() if " P4GAP " in line)

    def test_mark_filled_figures_persist_after_a_pick_failure(self, monkeypatch):
        from cobalt.aset.engine import compute_fill_recompute

        monkeypatch.setattr(picks_mod, "record_pick", lambda *a, **k: (_ for _ in ()).throw(RuntimeError("gap")))
        aset = AsetStore("cobalt_dev")
        result = compute_sizing(
            SizingInput(ticker="P4FIG", grade=Grade.B, direction=Direction.LONG, sheet_mode=SheetMode.FULL,
                        risk_dollars=Decimal("60"), entry=Decimal("10.00"), stop=Decimal("9.50")),
            [Grade.A, Grade.B], Decimal("10"),
        )
        card_id = aset.save(result)
        filled = aset.mark_filled(card_id, compute_fill_recompute(result, Decimal("10.10"), Decimal("5")))
        assert isinstance(filled, FillResult) and not filled.pick_recorded
        with aset._connect() as conn:
            actual = conn.execute("SELECT actual_fill FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()[0]
        assert actual == Decimal("10.1000")


@requires_db
def test_user_side_reads_qualified_radar_tables(real_connect):
    """ADR-0008: the USER role reads system.radar_* qualified (read-only)."""
    from cobalt.db import Side

    conn = real_connect(side=Side.USER)
    assert conn.execute("SELECT count(*) FROM system.radar_membership").fetchone()[0] >= 0
    assert conn.execute("SELECT count(*) FROM system.radar_pool").fetchone()[0] >= 0
