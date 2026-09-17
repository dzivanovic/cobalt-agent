"""S2-P4 STEP-5 — F12: the day's unfilled cards replayed over i1 bars.

Charter F12: "nightly report lists misses with the gate/variable that
excluded them". The real-shape fixtures are hub-cut (tests/fixtures/replay/,
L45): one real trading day shifted to 2026-02-10. KNOWN GAP (hub report
§STEP-1): the anchor day was an EDT day and only its DATE was shifted, so
the fixture's UTC offsets are EDT offsets. Tests that use it pass the
anchor's real close — 20:00 UTC — explicitly rather than asking the
calendar for a February close (21:00 UTC), which would call every card
stale. No PASSED-state card exists in the read window, so `passed` is
proved on a hand-built transition list, never on an invented fixture.

The one-bar vectors below are formula arithmetic, not parser fixtures.
"""

from __future__ import annotations

import json
import os
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.cards.models import CardState
from cobalt.replay import cards as cards_mod
from cobalt.replay.cards import (
    STATE_GATE,
    MissedStore,
    coverage,
    replay_card,
    replay_from_receipt,
    session_close_for,
    state_at,
)
from cobalt.replay.models import (
    CardCandidate,
    MissRow,
    PositionSpan,
    ReplayInputError,
    StopEdit,
    TransitionRow,
    WindowResolution,
)

FIX = Path(__file__).resolve().parents[1] / "fixtures" / "replay"
DAY = date(2026, 2, 10)
#: The anchor day's real 16:00 EDT close, carried by the shifted fixture.
CLOSE = datetime(2026, 2, 10, 20, 0, tzinfo=timezone.utc)
AT_CLOSE = WindowResolution(resolved_end=CLOSE, source="session_close", detail="no preferred_windows_ref")

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)


# ---------------------------------------------------------------------------
# fixture loading (read-only)
# ---------------------------------------------------------------------------


def _ts(raw: str) -> datetime:
    return datetime.fromisoformat(raw)


@pytest.fixture(scope="module")
def cards_day():
    return json.loads((FIX / "cards-day.real-shape.json").read_text())


@pytest.fixture(scope="module")
def bars_day():
    return [
        Bar(ticker=b["ticker"], interval=Interval.I1, ts=_ts(b["ts"]), open=Decimal(b["open"]),
            high=Decimal(b["high"]), low=Decimal(b["low"]), close=Decimal(b["close"]),
            volume=b["volume"])
        for b in json.loads((FIX / "bars-day.real-shape.json").read_text())
    ]


def _transitions(cards_day, card_id=None):
    return [
        TransitionRow(card_id=t["card_id"], from_state=t["from_state"], to_state=t["to_state"], at=_ts(t["at"]))
        for t in cards_day["transitions"] if card_id is None or t["card_id"] == card_id
    ]


def _positions(cards_day):
    trs = _transitions(cards_day)
    spans = []
    for cid in sorted({t.card_id for t in trs}):
        filled = [t.at for t in trs if t.card_id == cid and t.to_state == "FILLED"]
        closed = [t.at for t in trs if t.card_id == cid and t.to_state == "CLOSED"]
        if filled:
            spans.append(PositionSpan(card_id=cid, filled_at=min(filled), closed_at=min(closed) if closed else None))
    return spans


def _candidate(cards_day, card_id):
    s = next(c for c in cards_day["sizings"] if c["id"] == card_id)
    return CardCandidate(
        id=s["id"], ticker=s["ticker"], direction=s["direction"], entry=Decimal(s["entry"]),
        stop=Decimal(s["stop"]), created_at=_ts(s["created_at"]),
        transitions=tuple(_transitions(cards_day, card_id)),
    )


def _replay_fixture(cards_day, bars_day, card_id, **kw):
    card = _candidate(cards_day, card_id)
    return replay_card(
        card, [b for b in bars_day if b.ticker == card.ticker], trade_date=DAY,
        window=kw.pop("window", AT_CLOSE), session_close=kw.pop("session_close", CLOSE),
        positions=kw.pop("positions", _positions(cards_day)), **kw,
    )


# ---------------------------------------------------------------------------
# hand vectors: one ticker, one minute per bar
# ---------------------------------------------------------------------------

T0 = datetime(2026, 9, 3, 13, 30, tzinfo=timezone.utc)   # 09:30 EDT
SYN_DAY = date(2026, 9, 3)
SYN_CLOSE = datetime(2026, 9, 3, 20, 0, tzinfo=timezone.utc)


def bar(minute: int, o, h, l, c, ticker="SYN") -> Bar:
    return Bar(ticker=ticker, interval=Interval.I1, ts=T0 + timedelta(minutes=minute),
               open=Decimal(str(o)), high=Decimal(str(h)), low=Decimal(str(l)),
               close=Decimal(str(c)), volume=100)


def full_day(overrides: dict[int, Bar], *, flat=100, last_minute=389) -> list[Bar]:
    """A covered session: a pre-creation bar at minute -1, a flat tape, and
    the 15:59 bar — with `overrides` placed at their minutes."""
    out = {m: bar(m, flat, flat, flat, flat) for m in range(-1, last_minute + 1)}
    out.update(overrides)
    return [out[m] for m in sorted(out)]


def card(direction="long", entry="101", stop="99", created=0, transitions=None, edits=()):
    created_at = T0 + timedelta(minutes=created)
    trs = transitions or (TransitionRow(id=1, card_id=7, from_state=None, to_state="WATCH", at=created_at),)
    return CardCandidate(id=7, ticker="SYN", direction=direction, entry=Decimal(entry), stop=Decimal(stop),
                         created_at=created_at, transitions=tuple(trs), stop_edits=tuple(edits))


def run(c, bars, *, window_end=SYN_CLOSE, close=SYN_CLOSE, positions=()):
    return replay_card(c, bars, trade_date=SYN_DAY,
                       window=WindowResolution(resolved_end=window_end, source="trade_def", detail="t"),
                       session_close=close, positions=list(positions))


# =====================================================================
# §4 F12 — acceptance sentences
# =====================================================================


def test_trigger_on_unarmed_card_is_missed_row_unarmed(cards_day, bars_day):
    # Real CRWD card 302: WATCH -> EXPIRED at 20:05, never armed; its short
    # entry traded through at 13:30 before either fill opened a position.
    result = _replay_fixture(cards_day, bars_day, 302)
    assert result.status == "miss"
    miss = result.miss
    assert miss.excluded_by == "unarmed"
    assert miss.trigger_ts == datetime(2026, 2, 10, 13, 30, tzinfo=timezone.utc)
    assert miss.gate_detail["state"]["state"] == "WATCH"
    assert miss.gate_detail["rule_10"]["open_card_ids"] == []


def test_gate_order_rule_10_then_window_then_state(cards_day, bars_day):
    # Real MU card 308 is WATCH at its 13:57 trigger (state -> unarmed), but
    # cards 306 and 307 were FILLED and open: rule_10 is first and wins.
    real = _replay_fixture(cards_day, bars_day, 308)
    assert real.miss.excluded_by == "rule_10"
    assert real.miss.gate_detail["rule_10"]["open_card_ids"] == [306, 307]
    assert real.miss.gate_detail["state"]["maps_to"] == "unarmed"
    assert real.miss.gate_detail["order"] == ["rule_10", "window", "state"]

    # window before state: a WATCH card triggering after its window closes.
    bars = full_day({30: bar(30, 100, 102, 100, 101)})
    late = run(card(), bars, window_end=T0 + timedelta(minutes=10))
    assert late.miss.excluded_by == "window"
    assert late.miss.gate_detail["state"]["maps_to"] == "unarmed"

    # rule_10 before window: the same late trigger with two open positions.
    both = run(card(), bars, window_end=T0 + timedelta(minutes=10), positions=[
        PositionSpan(card_id=1, filled_at=T0), PositionSpan(card_id=2, filled_at=T0)])
    assert both.miss.excluded_by == "rule_10"
    assert both.miss.gate_detail["window"]["fired"] is True


def test_trade_count_band_unset_recorded_in_gate_detail_never_excluded_by(cards_day, bars_day):
    for card_id in (302, 303, 304, 305, 308):
        miss = _replay_fixture(cards_day, bars_day, card_id).miss
        assert miss.gate_detail["trade_count_band"] == "unset"
        assert miss.excluded_by != "trade_count_band"


def test_uncrossed_card_writes_no_row(cards_day, bars_day):
    # Real MU card 309 (short 905.475, created 13:59): the day's range
    # crossed that price, but never after the card existed.
    result = _replay_fixture(cards_day, bars_day, 309)
    assert result.status == "no_trigger"
    assert result.miss is None


def test_cf_r_stop_touched_first_is_minus_one(cards_day, bars_day):
    # Real CRWD card 304: short 219.75 / stop 220.55, filled at the planned
    # entry, stop touched on the trigger bar -> exactly -1R.
    miss = _replay_fixture(cards_day, bars_day, 304).miss
    assert (miss.fill_price, miss.exit_price, miss.exit_reason) == (Decimal("219.7500"), Decimal("220.5500"), "stop")
    assert miss.cf_r == Decimal("-1.0000")
    # hand vector: long 101/99 fills at entry, stop two bars later
    bars = full_day({1: bar(1, 100, 101.5, 100, 101), 3: bar(3, 101, 101, 98.5, 99)})
    hand = run(card(), bars).miss
    assert (hand.fill_price, hand.exit_ts, hand.cf_r) == (Decimal("101"), T0 + timedelta(minutes=3), Decimal("-1.0000"))


def test_cf_r_same_bar_stop_and_trigger_stop_wins():
    bars = full_day({2: bar(2, 100, 101.5, 98.5, 101.2)})
    miss = run(card(), bars).miss
    assert miss.trigger_ts == miss.exit_ts == T0 + timedelta(minutes=2)
    assert miss.exit_reason == "stop"
    assert miss.cf_r == Decimal("-1.0000")


def test_cf_r_gap_through_fills_at_bar_open(cards_day, bars_day):
    # R1-9's own vector: long entry 100 / stop 99, the bar opens at 102 and
    # the stop is hit -> fill 102, exit 99, -3R (planned risk 1).
    bars = full_day({5: bar(5, 102, 102.5, 98.9, 99)}, flat=99.5)
    miss = run(card(entry="100", stop="99"), bars).miss
    assert miss.fill_price == Decimal("102")
    assert miss.cf_r == Decimal("-3.0000")
    # Real CRWD card 303: short 220.495, the bar opened at 218.355 (beyond
    # the entry for a short) -> filled at that open, stopped at 220.55.
    real = _replay_fixture(cards_day, bars_day, 303).miss
    assert real.fill_price == Decimal("218.3550")
    assert real.cf_r == Decimal("-39.9091")


def test_cf_r_horizon_end_close_window_or_1600():
    rising = {m: bar(m, 101 + m / 100, 101.5 + m / 100, 101 + m / 100, 101.2 + m / 100) for m in range(1, 390)}
    bars = full_day(rising)
    # window end inside the session -> the close of the last bar whose
    # minute has ended by the window end
    w = T0 + timedelta(minutes=60)
    inside = run(card(), bars, window_end=w).miss
    assert inside.exit_reason == "horizon_end"
    assert inside.horizon_end == w
    assert inside.exit_ts == w - timedelta(minutes=1)
    # no window -> the session close (16:00 on a full day)
    at_close = run(card(), bars).miss
    assert at_close.horizon_end == SYN_CLOSE
    assert at_close.exit_ts == SYN_CLOSE - timedelta(minutes=1)


def test_mfe_r_stored_as_observation():
    bars = full_day({1: bar(1, 100, 101, 100, 101), 2: bar(2, 101, 104, 100.5, 103), 3: bar(3, 103, 103, 98, 99)})
    miss = run(card(), bars).miss
    assert miss.cf_r == Decimal("-1.0000")          # the one R
    assert miss.mfe_r == Decimal("1.5000")          # (104 - 101) / 2, an observation
    assert miss.receipt["outputs"]["mfe_r"] == "1.5000"
    assert "cf_r" in miss.receipt["outputs"] and "mfe_r" in miss.receipt["outputs"]


def test_every_missed_number_replays_from_stored_inputs(cards_day, bars_day):
    for card_id in (302, 303, 304, 305, 308):
        miss = _replay_fixture(cards_day, bars_day, card_id).miss
        again = replay_from_receipt(json.loads(json.dumps(miss.receipt))).miss
        assert again == miss
        assert again.inputs_sha256 == miss.inputs_sha256
    # the receipt holds VALUES, not just a hash: the bars it consumed
    miss = _replay_fixture(cards_day, bars_day, 302).miss
    assert miss.receipt["inputs"]["bars"][0]["close"]
    assert miss.receipt["inputs"]["positions"]


def test_stale_bars_write_no_row_and_count_input_stale(cards_day, bars_day):
    # bars that stop at 12:00 ET cannot cover a 16:00 close
    partial = [b for b in bars_day if b.ticker == "CRWD" and b.ts < datetime(2026, 2, 10, 16, 0, tzinfo=timezone.utc)]
    card302 = _candidate(cards_day, 302)
    result = replay_card(card302, partial, trade_date=DAY, window=AT_CLOSE, session_close=CLOSE, positions=[])
    assert result.status == "input_stale"
    assert result.miss is None
    assert "before" in result.reason


# =====================================================================
# Amendments
# =====================================================================


def test_r1_10_explicit_time_window_on_an_early_close_day_never_runs_past_the_close():
    early_close = T0 + timedelta(minutes=210)          # 13:00 ET
    rising = {m: bar(m, 101, 101.5, 101, 101.2) for m in range(1, 390)}
    bars = full_day(rising)
    miss = run(card(), bars, window_end=SYN_CLOSE, close=early_close).miss   # "16:00" resolved literally
    assert miss.horizon_end == early_close
    assert miss.exit_ts == early_close - timedelta(minutes=1)
    assert all(datetime.fromisoformat(ts) + timedelta(minutes=1) <= early_close
               for ts in miss.receipt["outputs"]["eligible_bar_ts"])


def test_r1_10_a_stop_only_in_the_bar_starting_at_h_is_excluded():
    w = T0 + timedelta(minutes=30)
    bars = full_day({1: bar(1, 100, 101.2, 100, 101.1), 30: bar(30, 101, 101, 90, 95)})
    miss = run(card(), bars, window_end=w).miss
    assert miss.exit_reason == "horizon_end"
    assert miss.exit_ts == w - timedelta(minutes=1)


def test_r1_10_trigger_at_exactly_h_writes_no_row_input_stale():
    w = T0 + timedelta(minutes=30)
    bars = full_day({30: bar(30, 100, 101.5, 100, 101)})
    result = run(card(), bars, window_end=w)
    assert result.status == "input_stale"
    assert "no completed bar" in result.reason


def test_r1_10_after_window_trigger_gets_the_session_close_horizon():
    w = T0 + timedelta(minutes=30)
    bars = full_day({45: bar(45, 100, 101.5, 100, 101)})
    miss = run(card(), bars, window_end=w).miss
    assert miss.excluded_by == "window"
    assert miss.horizon_end == SYN_CLOSE


def test_r1_10_ambiguous_prose_takes_the_resolver_fallback():
    window = cards_mod.resolve_window("Power hour 3 PM-close", SYN_DAY)
    assert window.source == "session_close"
    assert window.resolved_end == session_close_for(SYN_DAY)


def test_r1_11_state_mapping_is_exhaustive_over_card_states():
    assert set(STATE_GATE) == {s.value for s in CardState}


@pytest.mark.parametrize("terminal,expected", [("MISSED", "unarmed"), ("EXPIRED", "window"), ("PASSED", "passed")])
def test_r1_11_terminal_states_map_with_their_reason(terminal, expected):
    trs = (TransitionRow(id=1, card_id=7, to_state="WATCH", at=T0),
           TransitionRow(id=2, card_id=7, from_state="WATCH", to_state=terminal, at=T0 + timedelta(minutes=2)))
    bars = full_day({3: bar(3, 100, 101.5, 100, 101)})
    assert run(card(transitions=trs), bars).miss.excluded_by == expected


def test_r1_11_simultaneous_transitions_order_by_id_and_refuse_without_one():
    same = T0 + timedelta(minutes=1)
    trs = [TransitionRow(id=11, card_id=7, from_state="WATCH", to_state="ARMED", at=same),
           TransitionRow(id=10, card_id=7, to_state="WATCH", at=same)]
    assert state_at(trs, same).to_state == "ARMED"
    no_ids = [t.model_copy(update={"id": None}) for t in trs]
    with pytest.raises(ReplayInputError, match="unknowable"):
        state_at(no_ids, same)


def test_r1_11_historically_edited_stop_is_read_as_of_the_trigger():
    edit = StopEdit(id=1, at=T0 + timedelta(minutes=20), from_stop=Decimal("99"), to_stop=Decimal("100.5"))
    bars = full_day({2: bar(2, 100, 101.5, 100, 101), 4: bar(4, 101, 101, 98.5, 99)})
    miss = run(card(stop="100.5", edits=(edit,)), bars).miss       # current stop 100.5, 99 at the trigger
    assert miss.stop == Decimal("99")
    assert miss.cf_r == Decimal("-1.0000")


def test_r1_11_position_closed_at_the_trigger_instant_is_not_open():
    trigger = T0 + timedelta(minutes=2)
    bars = full_day({2: bar(2, 100, 101.5, 100, 101)})
    positions = [PositionSpan(card_id=1, filled_at=T0), PositionSpan(card_id=2, filled_at=T0, closed_at=trigger)]
    miss = run(card(), bars, positions=positions).miss
    assert miss.excluded_by == "unarmed"
    assert miss.gate_detail["rule_10"]["open_card_ids"] == [1]
    assert miss.gate_detail["rule_10"]["uncomputed"] == {"stop_at_card_level_exemption": "unavailable"}


def test_r1_12_partial_day_wrong_day_and_no_bars_are_input_stale_and_a_full_quiet_day_is_no_trigger():
    c = card()
    assert run(c, full_day({}, last_minute=200)).status == "input_stale"          # partial day
    wrong = [b.model_copy(update={"ts": b.ts - timedelta(days=1)}) for b in full_day({})]
    assert run(c, wrong).status == "input_stale"                                  # wrong-day export
    assert run(c, []).status == "input_stale"                                     # no archived bars
    assert run(c, full_day({})).status == "no_trigger"                            # complete, no trigger


def test_coverage_records_gaps_without_gating_on_them():
    bars = [b for b in full_day({}) if b.ts.minute % 7]            # every 7th minute has no trade
    cov = coverage(bars, start=T0, end=SYN_CLOSE)
    assert cov["covered"] is True
    assert cov["max_gap_min"] == 2


def test_rerun_is_idempotent(cards_day, bars_day):
    first = [_replay_fixture(cards_day, bars_day, i).miss for i in (302, 303, 304, 305, 308)]
    second = [_replay_fixture(cards_day, bars_day, i).miss for i in (302, 303, 304, 305, 308)]
    assert [m.inputs_sha256 for m in first] == [m.inputs_sha256 for m in second]
    assert first == second


# =====================================================================
# The versioned corpus (requires_db, hub on cobalt_dev with 0008/0009)
# =====================================================================


def _row(ticker="SYN", card_id=None, sha="a", excluded_by="not_in_any_source", **kw) -> MissRow:
    return MissRow(trade_date=SYN_DAY, kind="card" if card_id else "mover", ticker=ticker, card_id=card_id,
                   excluded_by=excluded_by, gate_detail={}, receipt={"inputs": {}},
                   inputs_sha256=sha * 64, **kw)


@requires_db
def test_reconcile_insert_supersede_retire_and_identical_rerun_against_the_live_index(dev_db_tx):
    from cobalt import db

    store = MissedStore()
    with db.connect(store.db_name, side=db.Side.SYSTEM) as conn:
        mover_id = conn.execute(
            "INSERT INTO movers_daily (trade_date, side, rank, ticker, change_pct, export_sha256, "
            "fetched_at, replay_run_id) VALUES (%s, 'gainers', 1, 'SYN', 12.5, %s, now(), 'r0') RETURNING id",
            (SYN_DAY, "e" * 64),
        ).fetchone()[0]
    a = _row(mover_id=mover_id)
    first = store.reconcile(run_id="r1", trade_date=SYN_DAY, kind="mover", rows=[a])
    assert (first.inserted, first.unchanged) == (1, 0)
    again = store.reconcile(run_id="r2", trade_date=SYN_DAY, kind="mover", rows=[a])
    assert (again.inserted, again.superseded, again.unchanged) == (0, 0, 1)

    stages = []
    changed = _row(mover_id=mover_id, sha="b", excluded_by="config_cap")
    third = store.reconcile(run_id="r3", trade_date=SYN_DAY, kind="mover", rows=[changed], before_commit=stages.append)
    assert third.superseded == 1 and stages == ["retired", "inserted", "linked"]
    current = store.current(SYN_DAY, "mover")
    assert [(r["excluded_by"], r["run_seq"]) for r in current] == [("config_cap", 2)]

    # a mover rising out of the benchmark set: retired, no successor
    gone = store.reconcile(run_id="r4", trade_date=SYN_DAY, kind="mover", rows=[])
    assert gone.retired == 1
    assert store.current(SYN_DAY, "mover") == []
    with db.connect(store.db_name, side=db.Side.USER) as conn:
        rows = conn.execute(
            "SELECT run_seq, is_current, superseded_by IS NOT NULL, retired_by_run_id FROM missed "
            "WHERE trade_date = %s AND kind = 'mover' ORDER BY id", (SYN_DAY,)).fetchall()
    assert rows == [(1, False, True, "r3"), (2, False, False, "r4")]


@requires_db
def test_reconcile_failure_between_retire_and_insert_rolls_the_whole_run_back(dev_db_tx):
    from cobalt import db

    store = MissedStore()
    with db.connect(store.db_name, side=db.Side.SYSTEM) as conn:
        mover_id = conn.execute(
            "INSERT INTO movers_daily (trade_date, side, rank, ticker, change_pct, export_sha256, "
            "fetched_at, replay_run_id) VALUES (%s, 'losers', 1, 'SYN', -12.5, %s, now(), 'r0') RETURNING id",
            (SYN_DAY, "e" * 64),
        ).fetchone()[0]
    store.reconcile(run_id="r1", trade_date=SYN_DAY, kind="mover", rows=[_row(mover_id=mover_id)])

    def crash(stage):
        if stage == "retired":
            raise RuntimeError("killed between (1) and (2)")

    with pytest.raises(RuntimeError, match="between"):
        store.reconcile(run_id="r2", trade_date=SYN_DAY, kind="mover",
                        rows=[_row(mover_id=mover_id, sha="c")], before_commit=crash)
    assert [r["replay_run_id"] for r in store.current(SYN_DAY, "mover")] == ["r1"]
    resumed = store.reconcile(run_id="r3", trade_date=SYN_DAY, kind="mover", rows=[_row(mover_id=mover_id, sha="c")])
    assert resumed.superseded == 1
