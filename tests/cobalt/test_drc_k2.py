"""DRC K2 — OFFLINE half (v3 §6 K2, R51; the build prompt's K2 CONTRACT
C1–C2 and C3's compare key).

The pairing version, `SeedBook`'s three source arms, the resolved trade
(`[F-06]`, X11), resolves inside `build_day`, and R51's stated-vs-close
comparison as a pure helper. Every K2 symbol is imported inside the test
that needs it, so each test is its own red until K2 exists. Constructed
symbols and dates only (L32 / L45).
"""

from __future__ import annotations

import hashlib
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Direction, PairingError, StatedPosition, TradeStatus
from cobalt.drc.pairing import pair_day, stated_open_positions
from cobalt.drc.trading_log import TradingLogSource

from test_drc_pairing import DAY1, _header

D = date(2001, 1, 2)
D_NEXT = date(2001, 1, 3)
ET = timezone(timedelta(hours=-5))
H = hashlib.sha256(b"[]").hexdigest()

CARRIED_COST_NOT_STATED = "not computed — carried cost not stated"
EXIT_NOT_IN_ANY_EXPORT = "not computed — exit not in any export"

HEADER = _header(DAY1)
DDD_COVER = HEADER + b"09:35:00,DDD,S,30.8,30,ROUTE1,BRK1,ACCT1,Margin,H0000000000401,\n"
EEE_ROUND = HEADER + (
    b"09:50:30,EEE,S,40.25,15,ROUTE1,BRK1,ACCT1,Margin,H0000000000406,\n"
    b"09:45:00,EEE,B,40.0,15,ROUTE2,BRK2,ACCT1,Margin,H0000000000405,\n"
)


def _parsed(data: bytes, day: date = D_NEXT):
    return TradingLogSource().parse(data, day, detect_kind("t.md", data))


def _ddd():
    """Day 1's carried `DDD` long: 30 shares, one lot at 30.1."""
    parsed = TradingLogSource().parse(DAY1.read_bytes(), D, detect_kind(DAY1.name, DAY1.read_bytes()))
    (pos,) = pair_day(parsed.executions, D).open_positions
    return pos


def _ggg_stated():
    (pos,) = stated_open_positions(
        D_NEXT, [StatedPosition(symbol="GGG", direction="short", shares=40, avg_cost=None)]
    )
    return pos


def _resolve(trade_id: str, **kw):
    from cobalt.drc.models import StatedResolve

    return StatedResolve(trade_id=trade_id, **kw)


# ---------------------------------------------------------------------
# C2 — the version
# ---------------------------------------------------------------------


def test_the_pairing_version_is_3():
    from cobalt.drc.pairing import FN_VERSION

    assert FN_VERSION == "drc.pairing/3"


# ---------------------------------------------------------------------
# C1 — SeedBook's arms
# ---------------------------------------------------------------------


def test_a_no_trade_carry_book_names_its_no_trade_row():
    from cobalt.drc.models import SeedBook

    SeedBook(source="no_trade_carry", positions=[], from_day=D, no_trade_id=3, from_book_sha256=H)
    with pytest.raises(ValidationError):
        SeedBook(source="no_trade_carry", positions=[], from_day=D, from_book_sha256=H)
    with pytest.raises(ValidationError):
        SeedBook(source="no_trade_carry", positions=[], no_trade_id=3, from_book_sha256=H)
    with pytest.raises(ValidationError):
        SeedBook(source="no_trade_carry", positions=[], from_day=D, no_trade_id=3, stated_book_id=1,
                 from_book_sha256=H)


def test_a_carried_book_may_keep_his_statement_as_history():
    """R51: the close wins; the statement for that day is kept by id."""
    from cobalt.drc.models import SeedBook

    book = SeedBook(source="carried", positions=[], from_day=D, stated_book_id=1,
                    stated_differs=["GGG-short-stated-2001-01-03"], from_book_sha256=H)
    assert book.stated_book_id == 1 and book.stated_differs == ["GGG-short-stated-2001-01-03"]
    with pytest.raises(ValidationError):
        SeedBook(source="carried", positions=[], from_day=D, no_trade_id=3, from_book_sha256=H)


def test_a_difference_needs_the_statement_it_differs_from():
    from cobalt.drc.models import SeedBook

    equal = SeedBook(source="carried", positions=[], from_day=D, stated_book_id=1, stated_differs=[],
                     from_book_sha256=H)
    assert equal.stated_differs == []
    with pytest.raises(ValidationError, match="stated_differs"):
        SeedBook(source="carried", positions=[], from_day=D, stated_differs=["x"], from_book_sha256=H)


def test_a_stated_book_carries_no_difference():
    from cobalt.drc.models import SeedBook

    assert SeedBook(source="stated", positions=[], stated_book_id=1, from_book_sha256=H).stated_differs == []
    with pytest.raises(ValidationError):
        SeedBook(source="stated", positions=[], stated_book_id=1, stated_differs=["x"], from_book_sha256=H)


def test_a_trades_realized_figure_takes_the_exit_literal():
    from test_drc_pairing import _trade

    assert _trade(gross_pnl=EXIT_NOT_IN_ANY_EXPORT).gross_pnl == EXIT_NOT_IN_ANY_EXPORT
    from cobalt.drc.models import EXIT_NOT_IN_ANY_EXPORT as constant

    assert constant == EXIT_NOT_IN_ANY_EXPORT


# ---------------------------------------------------------------------
# C2 — the resolved trade (`[F-06]`, X11)
# ---------------------------------------------------------------------


def test_a_resolve_with_no_exit_price_closes_with_the_literal_and_no_leg():
    from cobalt.drc.pairing import resolved_trade

    pos = _ddd()
    t = resolved_trade(pos, _resolve(pos.trade_id))
    assert t.status is TradeStatus.CLOSED and t.trade_id == pos.trade_id
    assert t.gross_pnl == EXIT_NOT_IN_ANY_EXPORT and t.legs == []
    assert t.held_shares == 0 and t.exit_time is None and t.hold_seconds is None
    assert [leg.carried for leg in t.entries] == [True]
    assert t.carried_from == pos.opened_on == D


def test_a_resolve_with_price_and_time_is_one_exit_leg_and_the_fifo_figure():
    from cobalt.drc.pairing import resolved_trade

    pos = _ddd()
    at = datetime(2001, 1, 3, 15, 0, tzinfo=ET)
    t = resolved_trade(pos, _resolve(pos.trade_id, exit_price=Decimal("31.1"), exit_time=at))
    assert t.gross_pnl == Decimal("30.0")  # (31.1 − 30.1) × 30, a long
    (leg,) = t.legs
    assert (leg.kind, leg.time, leg.price, leg.shares, leg.line) == ("exit", at, Decimal("31.1"), 30, None)
    assert t.exit_time == at and t.avg_exit == Decimal("31.1")


def test_a_resolve_with_a_price_and_no_time_is_numeric_with_no_leg():
    from cobalt.drc.pairing import resolved_trade

    pos = _ddd()
    t = resolved_trade(pos, _resolve(pos.trade_id, exit_price=Decimal("29.1")))
    assert t.gross_pnl == Decimal("-30.0") and t.legs == [] and t.exit_time is None


def test_a_resolve_of_a_stated_short_without_cost_is_the_cost_literal():
    from cobalt.drc.pairing import resolved_trade

    pos = _ggg_stated()
    t = resolved_trade(pos, _resolve(pos.trade_id, exit_price=Decimal("19.5")))
    assert t.gross_pnl == CARRIED_COST_NOT_STATED
    assert t.carried_from is None and t.direction is Direction.SHORT


def test_a_resolve_of_a_costed_short_is_signed_for_the_short():
    from cobalt.drc.pairing import resolved_trade

    (pos,) = stated_open_positions(
        D_NEXT, [StatedPosition(symbol="GGG", direction="short", shares=40, avg_cost=Decimal("20.0"))]
    )
    t = resolved_trade(pos, _resolve(pos.trade_id, exit_price=Decimal("19.5")))
    assert t.gross_pnl == Decimal("20.0")  # (20.0 − 19.5) × 40, a short


# ---------------------------------------------------------------------
# C2 — resolves inside build_day
# ---------------------------------------------------------------------


def _input(resolve_id: int, trade_id: str):
    from cobalt.drc.models import ResolveInput

    return ResolveInput(id=resolve_id, resolve=_resolve(trade_id))


def test_a_resolve_is_applied_when_the_file_does_not_touch_its_symbol():
    from cobalt.drc.pairing import build_day

    pos = _ddd()
    day = build_day(_parsed(EEE_ROUND), seed=[pos], resolves=[_input(5, pos.trade_id)])
    assert day.open_positions == []
    (ddd,) = [t for t in day.trades if t.symbol == "DDD"]
    assert ddd.status is TradeStatus.CLOSED and ddd.gross_pnl == EXIT_NOT_IN_ANY_EXPORT
    (outcome,) = day.resolves
    assert (outcome.resolve_id, outcome.trade_id, outcome.status) == (5, pos.trade_id, "applied")


def test_a_resolve_is_superseded_when_the_export_touches_its_symbol():
    """`[F-06]`: "A later export that contains the closing execution
    supersedes the resolve and re-pairs from the export (R67)"."""
    from cobalt.drc.pairing import build_day

    pos = _ddd()
    day = build_day(_parsed(DDD_COVER), seed=[pos], resolves=[_input(5, pos.trade_id)])
    (ddd,) = day.trades
    assert ddd.status is TradeStatus.CLOSED and ddd.gross_pnl == Decimal("21.0")
    assert [leg.line for leg in ddd.legs] == [2]
    (outcome,) = day.resolves
    assert outcome.status == "superseded"
    assert outcome.reason == "superseded — 2001-01-03's export touches DDD (R67: the export is the truth)"


def test_a_resolve_naming_no_seed_position_fails():
    from cobalt.drc.pairing import build_day

    with pytest.raises(PairingError, match="no-such-trade"):
        build_day(_parsed(EEE_ROUND), seed=[_ddd()], resolves=[_input(5, "no-such-trade")])


def test_a_not_computed_day_applies_no_resolve():
    from cobalt.drc.pairing import build_day

    pos = _ddd()
    day = build_day(_parsed(EEE_ROUND), seed=None, resolves=[_input(5, pos.trade_id)])
    assert "pairing" in day.not_computed and day.resolves == [] and day.trades == []


# ---------------------------------------------------------------------
# C3's compare key — R51's stated book vs the recorded close
# ---------------------------------------------------------------------


def _stated(*rows, day: date = D_NEXT):
    return stated_open_positions(day, [StatedPosition(**r) for r in rows])


def test_equal_books_differ_in_nothing():
    from cobalt.drc.pairing import stated_differs

    pos = _ddd()
    stated = _stated({"symbol": "DDD", "direction": "long", "shares": 30, "avg_cost": "99.0"})
    assert stated_differs(stated, [pos]) == []
    assert stated_differs([], []) == []


def test_a_different_share_count_names_both_ids():
    from cobalt.drc.pairing import stated_differs

    pos = _ddd()
    stated = _stated({"symbol": "DDD", "direction": "long", "shares": 20})
    assert stated_differs(stated, [pos]) == sorted([pos.trade_id, "DDD-long-stated-2001-01-03"])


def test_a_missing_and_an_extra_symbol_are_named():
    from cobalt.drc.pairing import stated_differs

    pos = _ddd()
    assert stated_differs([], [pos]) == [pos.trade_id]
    extra = _stated({"symbol": "DDD", "direction": "long", "shares": 30},
                    {"symbol": "HHH", "direction": "short", "shares": 10})
    assert stated_differs(extra, [pos]) == ["HHH-short-stated-2001-01-03"]


def test_a_different_direction_differs():
    from cobalt.drc.pairing import stated_differs

    pos = _ddd()
    stated = _stated({"symbol": "DDD", "direction": "short", "shares": 30})
    assert stated_differs(stated, [pos]) == sorted([pos.trade_id, "DDD-short-stated-2001-01-03"])


def test_the_open_day_is_never_compared():
    """`48` `## FOR K2`: symbol / direction / shares, never `opened_on`."""
    from cobalt.drc.pairing import stated_differs

    pos = _ddd()
    other_day = pos.model_copy(update={"opened_on": None, "trade_id": "DDD-long-other"})
    assert stated_differs([other_day], [pos]) == []
