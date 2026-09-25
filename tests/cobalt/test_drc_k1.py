"""DRC K1 — book records, OFFLINE half (v3 §6 K1, R51, R52).

The pairing version, the book hash, B8 replaced (a first import without a
stated book does not pair), a stated position with and without a cost,
the `SeedBook` / exit-leg validators and the `cobalt drc state-book`
parser. Every K1 symbol is imported inside the test that needs it.
Constructed symbols and dates only (L32 / L45); nothing here is a value
of his.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Direction, TradeStatus
from cobalt.drc.pairing import pair_day
from cobalt.drc.stats_log import StatsLogSource
from cobalt.drc.trading_log import TradingLogSource

from test_drc_pairing import CARRIED_SHORT_DAY2, DAY1, STATS, _header

D = date(2001, 1, 2)
D_NEXT = date(2001, 1, 3)
ET = timezone(timedelta(hours=-5))

CARRIED_COST_NOT_STATED = "not computed — carried cost not stated"
OPENING_NOT_STATED = "not computed — opening book not stated"

PARTIAL_COVER = _header(DAY1) + b"09:40:00,GGG,B,19.5,10,ROUTE1,BRK1,ACCT1,Margin,H0000000000303,\n"
NEW_LONG = _header(DAY1) + b"09:45:00,HHH,B,11.0,10,ROUTE1,BRK1,ACCT1,Margin,H0000000000304,\n"


def _parsed(data: bytes, day: date = D_NEXT):
    return TradingLogSource().parse(data, day, detect_kind("t.md", data))


def _encode(rows: list[dict]) -> bytes:
    return json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _stated(*rows, day: date = D_NEXT):
    from cobalt.drc.models import StatedPosition
    from cobalt.drc.pairing import stated_open_positions

    return stated_open_positions(day, [StatedPosition(**r) for r in rows])


GGG_SHORT = {"symbol": "GGG", "direction": "short", "shares": 40, "avg_cost": None}


# ---------------------------------------------------------------------
# C2 — the version and the book hash
# ---------------------------------------------------------------------


def test_the_pairing_version_is_2():
    from cobalt.drc.pairing import FN_VERSION

    assert FN_VERSION == "drc.pairing/3"


def test_an_empty_book_hashes_the_empty_json_array():
    from cobalt.drc.pairing import book_sha256

    assert book_sha256([]) == hashlib.sha256(b"[]").hexdigest()


def test_the_book_hash_is_the_pinned_encoding_sorted_by_trade_id_in_any_input_order():
    from cobalt.drc.pairing import book_sha256

    positions = _stated(GGG_SHORT, {"symbol": "HHH", "direction": "long", "shares": 10, "avg_cost": "11.0"})
    assert len(positions) == 2
    rows = [p.model_dump(mode="json") for p in sorted(positions, key=lambda p: p.trade_id)]
    assert book_sha256(positions) == hashlib.sha256(_encode(rows)).hexdigest()
    assert book_sha256(list(reversed(positions))) == book_sha256(positions)


# ---------------------------------------------------------------------
# C2 — THE B8 REPLACEMENT
# ---------------------------------------------------------------------


def test_a_first_import_without_a_stated_book_does_not_pair():
    """Replaces `test_a_first_import_reads_a_leading_buy_as_a_long_until_he_rules`
    (R22 "A for now" + v3 `:118`: "B8's pin test changes from "a leading
    buy is a long" to "a first import without a stated book does not
    pair"")."""
    from cobalt.drc.pairing import build_day

    day = build_day(_parsed(CARRIED_SHORT_DAY2))
    assert day.not_computed["pairing"] == OPENING_NOT_STATED
    assert day.trades == []
    assert day.open_positions == []


def test_an_unstated_book_leaves_every_stats_row_unmatched_and_says_why():
    """The `build_day` not-computed shape (`pairing.py:327-336`)."""
    from cobalt.drc.pairing import build_day

    stats_bytes = STATS.read_bytes()
    stats = StatsLogSource().parse(stats_bytes, detect_kind("s.md", stats_bytes))
    day = build_day(_parsed(CARRIED_SHORT_DAY2), stats, seed=None)
    assert day.not_computed["pairing"] == OPENING_NOT_STATED
    assert day.not_computed["match"] == "not computed — pairing did not run"
    assert day.unmatched and all(u.reason == "unmatched — no trades were paired" for u in day.unmatched)


def test_an_empty_stated_book_is_a_book_and_pairs():
    from cobalt.drc.pairing import build_day

    day = build_day(_parsed(CARRIED_SHORT_DAY2), seed=[])
    assert "pairing" not in day.not_computed
    (ggg,) = day.trades
    assert ggg.status is TradeStatus.OPEN and ggg.direction is Direction.LONG


# ---------------------------------------------------------------------
# C1 / C2 — a stated position, with and without a cost
# ---------------------------------------------------------------------


def test_a_stated_position_is_one_lot_with_no_time_and_a_stable_id():
    """H1 (`drc-k1-check-2026-09-24.md:149`; K1 fix r1, prompt `48`): a
    stated position's open day is NOT STATED (`None`) — never the stated
    day, a date known false for a swing opened before it (L1; v3 `:134`
    names no open day). The one assertion reversed here."""
    (pos,) = _stated(GGG_SHORT)
    assert pos.trade_id == "GGG-short-stated-2001-01-03"
    assert pos.opened_on is None and pos.day == D_NEXT
    assert pos.entry_time is None and pos.held_shares == 40
    assert [(lot.time, lot.price, lot.shares) for lot in pos.lots] == [(None, None, 40)]


def test_a_stated_position_with_a_cost_closes_with_a_numeric_realized_figure():
    seed = _stated({**GGG_SHORT, "avg_cost": "20.0"})
    day = pair_day(_parsed(CARRIED_SHORT_DAY2).executions, D_NEXT, seed)
    (ggg,) = day.trades
    assert ggg.status is TradeStatus.CLOSED and ggg.direction is Direction.SHORT
    assert ggg.gross_pnl == Decimal("20.0")
    assert ggg.avg_entry == Decimal("20.0")


def test_a_stated_position_without_a_cost_partially_covered_carries_the_literal_and_its_remainder():
    seed = _stated(GGG_SHORT)
    day = pair_day(_parsed(PARTIAL_COVER).executions, D_NEXT, seed)
    (ggg,) = day.trades
    assert ggg.status is TradeStatus.OPEN and ggg.held_shares == 30
    assert ggg.gross_pnl == CARRIED_COST_NOT_STATED
    (pos,) = day.open_positions
    assert pos.trade_id == seed[0].trade_id and pos.held_shares == 30
    assert [(lot.price, lot.shares) for lot in pos.lots] == [(None, 30)]


def test_a_stated_position_with_no_time_sorts_first_deterministically():
    seed = _stated(GGG_SHORT)
    day = pair_day(_parsed(NEW_LONG).executions, D_NEXT, seed)
    assert [t.symbol for t in day.trades] == ["GGG", "HHH"]


def test_a_stated_positions_open_day_stays_not_stated_through_the_carry():
    """H1 (`drc-k1-check-2026-09-24.md:149`; v3 `:134`): a stated position
    untouched by the day's file keeps `opened_on is None` — on the stated
    day and on the next day it is carried to — and its trade names no
    `carried_from`. Control: the long the file opens keeps its day."""
    day = pair_day(_parsed(NEW_LONG).executions, D_NEXT, _stated(GGG_SHORT))
    by_symbol = {p.symbol: p for p in day.open_positions}
    assert by_symbol["GGG"].opened_on is None
    (ggg,) = [t for t in day.trades if t.symbol == "GGG"]
    assert ggg.carried_from is None
    assert by_symbol["HHH"].opened_on == D_NEXT

    after_day = date(2001, 1, 4)
    after = pair_day(_parsed(_header(DAY1), after_day).executions, after_day, day.open_positions)
    carried = {p.symbol: p for p in after.open_positions}
    assert carried["GGG"].opened_on is None
    assert carried["HHH"].opened_on == D_NEXT


def test_a_carried_positions_open_day_is_kept():
    """H1 pin, GREEN-as-pin (`drc-k1-check-2026-09-24.md:149`): a seed
    position with a real open day, carried untouched, keeps it (the D1
    behaviour, pinned beside the not-stated one)."""
    from cobalt.drc.models import Lot, OpenPosition
    from cobalt.drc.pairing import trade_id

    t0 = datetime(2001, 1, 2, 10, 0, tzinfo=ET)
    seed = OpenPosition(
        trade_id=trade_id("GGG", Direction.SHORT, t0),
        symbol="GGG",
        direction=Direction.SHORT,
        held_shares=40,
        lots=[Lot(time=t0, price=Decimal("20.0"), shares=40)],
        entry_time=t0,
        opened_on=D,
        day=D,
    )
    day = pair_day(_parsed(NEW_LONG).executions, D_NEXT, [seed])
    (ggg,) = [p for p in day.open_positions if p.symbol == "GGG"]
    assert ggg.opened_on == D and ggg.day == D_NEXT


# ---------------------------------------------------------------------
# C1 — the validators
# ---------------------------------------------------------------------


def test_the_seed_book_validator_ties_source_to_its_link():
    from cobalt.drc.models import SeedBook

    h = hashlib.sha256(b"[]").hexdigest()
    SeedBook(source="carried", positions=[], from_day=D, from_book_sha256=h)
    SeedBook(source="stated", positions=[], stated_book_id=1, from_book_sha256=h)
    with pytest.raises(ValidationError):
        SeedBook(source="carried", positions=[], from_book_sha256=h)
    with pytest.raises(ValidationError):
        SeedBook(source="stated", positions=[], from_book_sha256=h)
    with pytest.raises(ValidationError):
        SeedBook(source="carried", positions=[], from_day=D, stated_book_id=1, from_book_sha256=h)
    with pytest.raises(ValidationError):
        SeedBook(source="carried", positions=[], from_day=D, from_book_sha256="not-a-hash")


def test_an_exit_leg_refuses_a_missing_price_or_time_and_an_entry_leg_allows_them():
    from cobalt.drc.models import Leg

    t0 = datetime(2001, 1, 3, 9, 40, tzinfo=ET)
    Leg(kind="entry", time=None, price=None, shares=40, carried=True)
    with pytest.raises(ValidationError):
        Leg(kind="exit", time=None, price=Decimal("19.5"), shares=40, line=2)
    with pytest.raises(ValidationError):
        Leg(kind="exit", time=t0, price=None, shares=40, line=2)


def test_a_trades_realized_figure_is_a_decimal_or_exactly_the_literal():
    from test_drc_pairing import _trade

    assert _trade(gross_pnl=CARRIED_COST_NOT_STATED).gross_pnl == CARRIED_COST_NOT_STATED
    with pytest.raises(ValidationError):
        _trade(gross_pnl="not computed")
    with pytest.raises(ValidationError):
        _trade(gross_pnl=None)


# ---------------------------------------------------------------------
# C7 — the `cobalt drc state-book` parser (no store)
# ---------------------------------------------------------------------


def _request(*argv: str):
    import argparse

    from cobalt.drc import cli as drc_cli

    parser = argparse.ArgumentParser(prog="cobalt")
    sub = parser.add_subparsers(dest="group", required=True)
    drc_cli.add_parser(sub)
    return drc_cli.request_from_args(parser.parse_args(["drc", "state-book", *argv]))


def _refused(*argv: str) -> None:
    with pytest.raises(SystemExit) as e:
        _request(*argv)
    assert e.value.code == 2


def test_the_cli_takes_exactly_one_kind():
    _refused("--opening", "2001-01-02", "--flat", "--no-trade", "2001-01-02")
    _refused("--flat")
    r = _request("--no-trade", "2001-01-02")
    assert (r.day, r.kind, r.positions) == (D, "no_trade", [])


def test_the_opening_needs_flat_xor_position():
    _refused("--opening", "2001-01-02")
    _refused("--opening", "2001-01-02", "--flat", "--position", "GGG", "short", "40")
    assert _request("--opening", "2001-01-02", "--flat").positions == []
    r = _request("--opening", "2001-01-02", "--position", "GGG", "short", "40",
                 "--position", "HHH", "long", "10", "11.0")
    assert r.kind == "opening"
    assert r.positions == [
        {"symbol": "GGG", "direction": "short", "shares": "40", "avg_cost": None},
        {"symbol": "HHH", "direction": "long", "shares": "10", "avg_cost": "11.0"},
    ]


def test_a_position_takes_three_or_four_values():
    _refused("--opening", "2001-01-02", "--position", "GGG", "short")
    _refused("--opening", "2001-01-02", "--position", "GGG", "short", "40", "20.0", "x")


def test_apply_without_a_hash_is_refused():
    _refused("--opening", "2001-01-02", "--flat", "--apply")
    r = _request("--opening", "2001-01-02", "--flat", "--apply", "--sha256", "ab" * 32)
    assert r.apply and r.sha256 == "ab" * 32


def test_a_resolve_names_one_trade_and_refuses_a_naive_exit_time():
    _refused("--resolve", "2001-01-03", "GGG-short-stated-2001-01-02", "--exit-time", "2001-01-03T15:00:00")
    r = _request("--resolve", "2001-01-03", "GGG-short-stated-2001-01-02",
                 "--exit-price", "19.5", "--exit-time", "2001-01-03T15:00:00-05:00")
    assert r.kind == "resolve" and r.day == D_NEXT
    (row,) = r.positions
    assert row["trade_id"] == "GGG-short-stated-2001-01-02"
    assert row["exit_price"] == "19.5"
    assert row["exit_time"] == datetime(2001, 1, 3, 15, 0, tzinfo=ET)
    bare = _request("--resolve", "2001-01-03", "GGG-short-stated-2001-01-02")
    assert bare.positions == [{"trade_id": "GGG-short-stated-2001-01-02", "exit_price": None, "exit_time": None}]


def test_exit_fields_and_positions_belong_to_their_own_kind():
    _refused("--opening", "2001-01-02", "--flat", "--exit-price", "19.5")
    _refused("--no-trade", "2001-01-02", "--flat")
    _refused("--resolve", "2001-01-03", "T", "--position", "GGG", "short", "40")


def test_supersedes_is_carried_on_every_kind():
    assert _request("--no-trade", "2001-01-02", "--supersedes", "7").supersedes == 7
    assert _request("--opening", "2001-01-02", "--flat").supersedes is None
