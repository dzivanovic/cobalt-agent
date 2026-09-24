"""DRC D1 — the typed records (D1-1) and FIFO pairing + carry (D1-3).

Every input is a D1-0 fixture or a constructed literal (L69); nothing
here is a value of his.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from cobalt.drc.models import (
    Detection,
    Direction,
    ExecSide,
    Execution,
    ImportResult,
    Kind,
    Leg,
    Outcome,
    StatsRow,
    Trade,
    TradeStatus,
)

ET = timezone(timedelta(hours=-5))
T0 = datetime(2001, 1, 2, 9, 40, tzinfo=ET)


# ---------------------------------------------------------------------
# D1-1 — models
# ---------------------------------------------------------------------


def test_the_side_enum_is_exactly_the_three_codes_e1_shows():
    assert {s.value for s in ExecSide} == {"B", "S", "SS"}


def test_an_execution_refuses_a_naive_time_an_unknown_side_and_a_zero_qty():
    with pytest.raises(ValidationError):
        Execution(line=2, time=datetime(2001, 1, 2, 9, 40))
    with pytest.raises(ValidationError):
        Execution(line=2, time=T0, side="X")
    with pytest.raises(ValidationError):
        Execution(line=2, time=T0, qty=0)


def test_an_execution_of_a_partial_file_carries_none_for_an_absent_column():
    e = Execution(line=2, time=T0, symbol="AAA", side="B", qty=10)
    assert e.price is None and e.account is None


def test_a_stats_row_is_all_optional_and_its_stop_defaults_to_none():
    row = StatsRow(line=2)
    assert row.stop is None and row.entry is None and row.playbooks == []


def _trade(**over):
    fields = dict(
        trade_id="AAA-long-x",
        symbol="AAA",
        direction=Direction.LONG,
        status=TradeStatus.CLOSED,
        entry_time=T0,
        avg_entry=Decimal("10"),
        shares=10,
        held_shares=0,
        gross_pnl=Decimal("1"),
        entries=[Leg(kind="entry", time=T0, price=Decimal("10"), shares=10, line=3)],
        legs=[Leg(kind="exit", time=T0, price=Decimal("10.1"), shares=10, line=2)],
    )
    fields.update(over)
    return Trade(**fields)


def test_a_trade_keeps_every_playbook_in_order_and_defaults_to_none():
    assert _trade().playbooks == []
    t = _trade(playbooks=["Beta", "Alpha", "Beta"])
    assert t.playbooks == ["Beta", "Alpha", "Beta"]


def test_net_and_commissions_are_the_stats_logs_own_never_computed():
    assert _trade().net_pnl is None and _trade().commissions is None
    row = StatsRow(line=2, net_pnl=Decimal("0.5"), commission=Decimal("0.1"))
    assert _trade(stats=row).net_pnl == Decimal("0.5")
    assert _trade(stats=row).commissions == Decimal("0.1")


def test_an_open_trades_unrealized_is_not_computed():
    assert _trade(status=TradeStatus.OPEN, held_shares=5).unrealized == "not computed"


def test_the_partial_flag_names_the_missing_columns_loudly():
    d = Detection(name="x", kind=Kind.STATS_LOG, outcome=Outcome.PARTIAL, reason="r",
                  missing=["A", "B"])
    assert d.partial_flag == "PARTIAL — missing: A, B"
    r = ImportResult(name="x", kind=Kind.TRADING_LOG, outcome=Outcome.PARTIAL,
                     missing=["C"])
    assert r.partial_flag == "PARTIAL — missing: C"


def test_an_extra_column_is_the_kinds_shape_flag():
    r = ImportResult(name="x", kind=Kind.TRADING_LOG, outcome=Outcome.PARSED, extras=["New"])
    assert r.degraded == "trading_log_shape"
    d = Detection(name="x", kind=Kind.STATS_LOG, outcome=Outcome.PARSED, reason="r",
                  extras=["New"])
    assert d.degraded == "stats_log_shape"
    assert ImportResult(name="x", kind=Kind.STATS_LOG, outcome=Outcome.PARSED).degraded is None


def test_the_outcome_domain_is_parsed_partial_failed_ignored():
    assert {o.value for o in Outcome} == {"parsed", "partial", "failed", "ignored"}


def test_records_are_frozen_and_refuse_unknown_fields():
    with pytest.raises(ValidationError):
        StatsRow(line=2, invented=1)
    row = StatsRow(line=2)
    with pytest.raises(ValidationError):
        row.stop = Decimal("1")


# ---------------------------------------------------------------------
# D1-3 — FIFO pairing and carried positions
# ---------------------------------------------------------------------

import csv  # noqa: E402
import io  # noqa: E402
from pathlib import Path  # noqa: E402

from cobalt.drc import stats_log, trading_log  # noqa: E402
from cobalt.drc.detect import detect_kind  # noqa: E402
from cobalt.drc.models import PairingError  # noqa: E402
from cobalt.drc.pairing import build_day, check_contiguity, pair_day, trade_id  # noqa: E402
from cobalt.drc.stats_log import StatsLogSource  # noqa: E402
from cobalt.drc.trading_log import TradingLogSource  # noqa: E402

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures" / "drc"
E1 = FIXTURES / "trading_log_e1.csv"
STATS = FIXTURES / "stats_log_e1.csv"
DAY1 = FIXTURES / "trading_log_carry_day1.csv"
SEED = FIXTURES / "trading_log_carry_seed.csv"
D = date(2001, 1, 2)
D_NEXT = date(2001, 1, 3)


def _parsed(data: bytes, day: date = D):
    return TradingLogSource().parse(data, day, detect_kind("t.md", data))


def _pair(data: bytes, day: date = D, seed=()):
    p = _parsed(data, day)
    assert p.result.outcome.value in ("parsed", "partial"), p.result.reason
    return pair_day(p.executions, day, seed)


def _set_cell(data: bytes, line: int, column: str, value: str) -> bytes:
    records = list(csv.reader(io.StringIO(data.decode(), newline="")))
    records[line - 1][records[0].index(column)] = value
    return "".join(",".join(r) + "\n" for r in records).encode()


def _by_symbol(pairing, symbol):
    return [t for t in pairing.trades if t.symbol == symbol]


def test_e1s_cut_pairs_into_four_closed_trades():
    p = _pair(E1.read_bytes())
    assert [(t.symbol, t.direction.value, t.status.value) for t in p.trades] == [
        ("CCC", "long", "closed"),
        ("BBB", "short", "closed"),
        ("BBB", "short", "closed"),
        ("AAA", "long", "closed"),
    ]
    assert p.open_positions == []


def test_the_scale_in_and_partial_exits_are_one_trade_with_n_legs():
    (aaa,) = _by_symbol(_pair(E1.read_bytes()), "AAA")
    assert aaa.shares == 100 and aaa.held_shares == 0
    # Within one `Time`, reverse file order (the rule D1-2 pins).
    assert [leg.shares for leg in aaa.entries] == [18, 12, 30, 40]
    assert aaa.entries[0].price == Decimal("50.18")
    assert [leg.shares for leg in aaa.legs] == [25, 25, 50]
    assert aaa.avg_entry == Decimal("50.3014") and aaa.avg_exit == Decimal("50.75")
    assert aaa.gross_pnl == Decimal("44.86")
    assert aaa.hold_seconds == 3320


def test_a_short_is_opened_with_ss_and_covered_with_b_over_two_exits():
    first, second = _by_symbol(_pair(E1.read_bytes()), "BBB")
    assert first.gross_pnl == Decimal("-6.0") and len(first.legs) == 1
    assert second.gross_pnl == Decimal("16.0") and len(second.legs) == 2
    assert second.direction is Direction.SHORT


def test_the_trade_id_is_symbol_direction_and_entry_time():
    (ccc,) = _by_symbol(_pair(E1.read_bytes()), "CCC")
    assert ccc.trade_id == trade_id("CCC", Direction.LONG, ccc.entry_time)
    assert ccc.trade_id == "CCC-long-2001-01-02T09:40:00-05:00"


def test_two_accounts_pair_exactly_as_one_bucket():
    """R94: the account never splits a position."""
    data = _set_cell(_set_cell(E1.read_bytes(), 3, trading_log.ACCOUNT, "ACCT2"),
                     8, trading_log.ACCOUNT, "ACCT2")
    assert _pair(data).trades == _pair(E1.read_bytes()).trades


def test_a_position_open_at_file_end_is_an_open_trade_not_a_failure():
    p = _pair(DAY1.read_bytes())
    (ddd,) = _by_symbol(p, "DDD")
    assert ddd.status is TradeStatus.OPEN and ddd.held_shares == 30
    assert ddd.unrealized == "not computed" and ddd.exit_time is None
    assert ddd.gross_pnl == Decimal("8.0")  # the one partial exit, realized
    (eee,) = _by_symbol(p, "EEE")
    assert eee.status is TradeStatus.CLOSED and eee.gross_pnl == Decimal("3.75")
    (pos,) = p.open_positions
    assert (pos.symbol, pos.held_shares, pos.opened_on, pos.day) == ("DDD", 30, D, D)
    assert pos.trade_id == ddd.trade_id
    assert sum(lot.shares for lot in pos.lots) == 30


def test_the_seed_round_trips_across_the_two_fixture_days():
    day1 = _pair(DAY1.read_bytes())
    day2 = _pair(SEED.read_bytes(), D_NEXT, seed=day1.open_positions)
    (ddd,) = _by_symbol(day2, "DDD")
    assert ddd.status is TradeStatus.CLOSED
    assert ddd.trade_id == day1.open_positions[0].trade_id, "one trade_id across days"
    assert ddd.carried_from == D
    assert ddd.gross_pnl == Decimal("21.0")  # 30 carried shares at the lot price
    assert all(leg.carried for leg in ddd.entries) and ddd.legs[0].line == 4
    (fff,) = _by_symbol(day2, "FFF")
    assert fff.direction is Direction.SHORT and fff.gross_pnl == Decimal("20.0")
    assert day2.open_positions == []


def _header(path: Path) -> bytes:
    return path.read_bytes().split(b"\n", 1)[0] + b"\n"


CARRIED_SHORT_DAY1 = _header(DAY1) + b"10:00:00,GGG,SS,20.0,40,ROUTE1,BRK1,ACCT1,Short,H0000000000301,\n"
CARRIED_SHORT_DAY2 = _header(DAY1) + b"09:40:00,GGG,B,19.5,40,ROUTE1,BRK1,ACCT1,Margin,H0000000000302,\n"


def test_a_carried_short_closes_on_the_next_days_buy_with_its_seed():
    """`54` rows 1 / 11: a short held overnight, covered by the next day's
    `B` (E1: a cover is `B`), closes as ONE short trade with its seed.
    GREEN-as-pin: no src change backs it."""
    day1 = _pair(CARRIED_SHORT_DAY1)
    (pos,) = day1.open_positions
    assert pos.symbol == "GGG" and pos.direction is Direction.SHORT and pos.held_shares == 40
    day2 = _pair(CARRIED_SHORT_DAY2, D_NEXT, seed=day1.open_positions)
    (ggg,) = _by_symbol(day2, "GGG")
    assert ggg.status is TradeStatus.CLOSED and ggg.direction is Direction.SHORT
    assert ggg.trade_id == pos.trade_id
    assert ggg.carried_from == D
    assert ggg.gross_pnl == Decimal("20.0")
    assert day2.open_positions == []


def _set_stats_cell(data: bytes, line: int, column: str, value: str) -> bytes:
    """A one-cell mutation of a stats log, quoted where a cell needs it."""
    records = list(csv.reader(io.StringIO(data.decode(), newline="")))
    records[line - 1][records[0].index(column)] = value
    out = io.StringIO()
    csv.writer(out, lineterminator="\n", quoting=csv.QUOTE_MINIMAL).writerows(records)
    return out.getvalue().encode()


def test_an_empty_open_date_cell_is_never_reported_as_an_empty_open_time():
    """`54` row 5: `StatsRow` carries only the combined entry time, so the
    reason names the pair jointly — never `Open Time` alone as if proven
    empty."""
    stats = _set_stats_cell(STATS.read_bytes(), 2, stats_log.OPEN_DATE, "")
    day = build_day(_parsed(E1.read_bytes()), StatsLogSource().parse(stats, detect_kind("s.md", stats)), seed=())
    (u,) = day.unmatched
    assert u.row.line == 2
    assert u.reason == "unmatched — empty: Open Date or Open Time"


def test_a_carried_symbol_with_no_prior_row_fails_naming_it():
    with pytest.raises(PairingError, match="carried symbol with no prior row \\(DDD\\)"):
        _pair(SEED.read_bytes(), D_NEXT)


def test_a_file_contradicting_the_seed_fails():
    seed = _pair(DAY1.read_bytes()).open_positions
    data = _set_cell(SEED.read_bytes(), 4, trading_log.SIDE, "SS")
    with pytest.raises(PairingError, match="contradicts the seed"):
        _pair(data, D_NEXT, seed=seed)
    data = _set_cell(SEED.read_bytes(), 4, trading_log.QTY, "40")
    with pytest.raises(PairingError, match="through 0.*contradicts the seed"):
        _pair(data, D_NEXT, seed=seed)


def test_a_position_through_0_in_one_execution_fails_the_file():
    data = _set_cell(E1.read_bytes(), 2, trading_log.QTY, "60")
    with pytest.raises(PairingError, match="line 2 \\(AAA S 60\\).*through 0"):
        _pair(data)


def test_a_short_sale_while_long_fails_the_file():
    data = _set_cell(E1.read_bytes(), 14, trading_log.SIDE, "SS")
    with pytest.raises(PairingError, match="SS while 10 shares long"):
        _pair(data)


def test_a_seed_whose_lots_disagree_with_its_held_shares_fails():
    seed = _pair(DAY1.read_bytes()).open_positions[0]
    broken = seed.model_copy(update={"held_shares": 31})
    with pytest.raises(PairingError, match="lots hold 30"):
        _pair(SEED.read_bytes(), D_NEXT, seed=[broken])


@pytest.mark.parametrize("column", trading_log.PAIRING_INPUTS)
def test_a_partial_file_missing_a_pairing_input_is_not_paired_and_says_so(column):
    records = list(csv.reader(io.StringIO(E1.read_text(), newline="")))
    i = records[0].index(column)
    data = "".join(",".join(r[:i] + r[i + 1:]) + "\n" for r in records).encode()
    day = build_day(_parsed(data), seed=())
    assert day.trades == []
    assert day.not_computed == {"pairing": f"not computed — missing: {column}"}


def test_contiguity_passes_the_first_import_and_a_contiguous_chain():
    check_contiguity(D_NEXT, D, [])
    check_contiguity(D_NEXT, D, [D])
    check_contiguity(D_NEXT, D, [date(2000, 12, 29), D])


def test_contiguity_fails_loud_when_the_prior_trading_day_is_missing():
    with pytest.raises(PairingError, match="prior trading day 2001-01-02 has no import"):
        check_contiguity(D_NEXT, D, [date(2000, 12, 29)])


def test_a_later_recorded_day_is_not_history():
    check_contiguity(D, date(2000, 12, 29), [D_NEXT])
