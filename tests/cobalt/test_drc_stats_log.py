"""DRC D1-4 — the stats-log parser and the trade match, against the
D1-0 fixtures. Column names come from `stats_log`'s constants or the
fixture header; the vendor-named column is never typed (L31).
"""

from __future__ import annotations

import csv
import io
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from cobalt.drc import stats_log
from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Direction, Outcome
from cobalt.drc.pairing import build_day
from cobalt.drc.stats_log import StatsLogSource, split_playbooks
from cobalt.drc.trading_log import TradingLogSource

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures" / "drc"
STATS = FIXTURES / "stats_log_e1.csv"
TRADES = FIXTURES / "trading_log_e1.csv"
DAY = date(2001, 1, 2)
ET = ZoneInfo("America/New_York")


def _records(data: bytes) -> list[list[str]]:
    return list(csv.reader(io.StringIO(data.decode(), newline="")))


def _bytes(records: list[list[str]]) -> bytes:
    """Re-quote exactly where E1 quotes: a cell with a comma, or empty
    where the fixture had `""`, is written back as the fixture wrote it."""
    out = io.StringIO()
    csv.writer(out, lineterminator="\n", quoting=csv.QUOTE_MINIMAL).writerows(records)
    return out.getvalue().encode()


def _parse(data: bytes, name: str = "s.md"):
    return StatsLogSource().parse(data, detect_kind(name, data))


def _set_cell(data: bytes, line: int, column: str, value: str) -> bytes:
    records = _records(data)
    records[line - 1][records[0].index(column)] = value
    return _bytes(records)


def _drop_column(data: bytes, column: str) -> bytes:
    records = _records(data)
    i = records[0].index(column)
    return _bytes([r[:i] + r[i + 1:] for r in records])


def _day(stats_data: bytes = None, trades_data: bytes = None):
    t = trades_data or TRADES.read_bytes()
    s = stats_data or STATS.read_bytes()
    trading = TradingLogSource().parse(t, DAY, detect_kind("t.md", t))
    return build_day(trading, _parse(s))


def test_e1s_cut_parses_four_rows_and_flags_the_unread_vendor_column():
    p = _parse(STATS.read_bytes())
    assert p.result.outcome is Outcome.PARSED, p.result.reason
    assert len(p.rows) == 4 and [r.line for r in p.rows] == [2, 3, 4, 5]
    assert p.result.degraded == "stats_log_shape"
    assert p.result.extras == [_records(STATS.read_bytes())[0][-1]]


def test_a_row_carries_entry_target_rr_mae_mfe_and_best_exit_by_header_name():
    row = _parse(STATS.read_bytes()).rows[1]
    assert (row.symbol, row.side) == ("AAA", Direction.LONG)
    assert row.open_time == datetime(2001, 1, 2, 10, 15, 20, tzinfo=ET)
    assert row.close_time == datetime(2001, 1, 2, 11, 10, 40, tzinfo=ET)
    assert row.entry == Decimal("50.18") and row.exit == Decimal("50.6")
    assert row.target == Decimal("51.4")
    assert row.assumed_rr == Decimal("1.98765432") and row.realized_rr == Decimal("0.79381818")
    assert (row.price_mae, row.price_mfe) == (Decimal("50.1"), Decimal("51.02"))
    assert (row.position_mae, row.position_mfe) == (Decimal("1.2"), Decimal("71.5"))
    assert row.best_exit == Decimal("7.1")
    assert row.best_exit_price is None and row.best_exit_time is None  # empty cells
    assert (row.gross_pnl, row.net_pnl) == (Decimal("44.86"), Decimal("43.66"))
    assert (row.commission, row.fee) == (Decimal("0.8"), Decimal("0.4"))
    assert row.quantity == Decimal("100.0") and row.executions == 7


def test_the_best_exit_time_is_read_as_utc():
    row = _parse(STATS.read_bytes()).rows[0]
    assert row.best_exit_time.utcoffset().total_seconds() == 0
    assert row.best_exit_time.hour == 14


# --- STOP: R17 (4) ----------------------------------------------------


def test_the_stop_is_none_on_every_e1_row_never_computed():
    """E1's header has no stop column. Every row HAS `Trade Risk`, entry,
    target, R:R and a quantity set — and the stop is still None."""
    rows = _parse(STATS.read_bytes()).rows
    records = _records(STATS.read_bytes())
    risk = records[0].index("Trade Risk")
    assert all(r[risk] != "" for r in records[1:])
    assert all(row.stop is None for row in rows)
    assert all(row.entry is not None and row.quantity is not None for row in rows)


def test_no_stop_column_name_is_ruled_so_none_is_read():
    assert stats_log.STOP_COLUMN is None


# --- PLAYBOOKS: R114 --------------------------------------------------


def test_the_multi_playbook_row_keeps_both_names_in_order():
    rows = _parse(STATS.read_bytes()).rows
    assert rows[1].playbooks == ["Alpha Setup Long", "Beta Setup Long"]
    assert rows[0].playbooks == ["Gamma Setup Long"]
    assert rows[3].playbooks == ["Omega Setup"]


@pytest.mark.parametrize(
    "cell,names",
    [
        ("", []),
        ("A, B", ["A", "B"]),
        ("B, A", ["B", "A"]),
        ("A, A", ["A", "A"]),
        ("  A ,B,, C  ,", ["A", "B", "C"]),
        ("Solo Name Short", ["Solo Name Short"]),
    ],
)
def test_the_playbook_cell_is_split_on_the_comma_order_kept_never_deduplicated(cell, names):
    assert split_playbooks(cell) == names


def test_an_empty_playbook_cell_is_an_empty_list():
    data = _set_cell(STATS.read_bytes(), 2, stats_log.PLAYBOOK, "")
    assert _parse(data).rows[0].playbooks == []


def test_the_setups_column_is_never_read_as_a_playbook():
    data = _set_cell(STATS.read_bytes(), 2, "Setups", "Zeta Other")
    assert _parse(data).rows[0].playbooks == ["Gamma Setup Long"]


# --- partial / degraded / failed --------------------------------------


def test_a_non_match_column_absent_is_partial_and_that_field_not_given():
    p = _parse(_drop_column(STATS.read_bytes(), stats_log.PRICE_MAE))
    assert p.result.outcome is Outcome.PARTIAL and p.result.missing == [stats_log.PRICE_MAE]
    assert p.result.partial_flag == f"PARTIAL — missing: {stats_log.PRICE_MAE}"
    assert len(p.rows) == 4 and all(r.price_mae is None for r in p.rows)
    assert all(r.price_mfe is not None for r in p.rows)


@pytest.mark.parametrize("column", stats_log.MATCH_INPUTS)
def test_a_match_input_absent_leaves_every_row_unmatched_naming_it(column):
    day = _day(stats_data=_drop_column(STATS.read_bytes(), column))
    assert len(day.unmatched) == 4
    assert {u.reason for u in day.unmatched} == {f"unmatched — missing: {column}"}
    assert day.not_computed["match"] == f"not computed — missing: {column}"
    assert all(t.stats is None and t.playbooks == [] for t in day.trades)


def test_an_added_column_parses_with_the_shape_flag():
    records = _records(STATS.read_bytes())
    widened = _bytes([r + (["Added"] if i == 0 else ["1"]) for i, r in enumerate(records)])
    p = _parse(widened)
    assert p.result.outcome is Outcome.PARSED and "Added" in p.result.extras
    assert p.result.degraded == "stats_log_shape"


@pytest.mark.parametrize(
    "column,value",
    [
        (stats_log.SIDE, "sideways"),
        (stats_log.OPEN_TIME, "10:15:20 PST"),
        (stats_log.OPEN_TIME, "10:15 EDT"),
        (stats_log.OPEN_DATE, "2001/01/02"),
        (stats_log.ENTRY, "abc"),
        (stats_log.EXECUTIONS, "2.5"),
        (stats_log.BEST_EXIT_TIME, "2001-01-02 14:52:00 PST"),
    ],
)
def test_one_bad_cell_fails_the_whole_stats_file_naming_the_line(column, value):
    p = _parse(_set_cell(STATS.read_bytes(), 3, column, value))
    assert p.result.outcome is Outcome.FAILED
    assert p.result.line == 3 and "line 3" in p.result.reason
    assert p.rows == []


def test_a_row_with_the_wrong_cell_count_fails_the_stats_file():
    lines = STATS.read_bytes().split(b"\n")
    lines[2] = lines[2] + b",extra"
    p = _parse(b"\n".join(lines))
    assert p.result.outcome is Outcome.FAILED and p.result.line == 3


def test_the_parser_is_reached_only_through_a_stats_log_detection():
    data = TRADES.read_bytes()
    with pytest.raises(ValueError, match="only through detect_kind"):
        StatsLogSource().parse(data, detect_kind("t.md", data))


# --- the match --------------------------------------------------------


def test_every_e1_stats_row_matches_exactly_one_trade():
    day = _day()
    assert day.unmatched == []
    assert all(t.stats is not None for t in day.trades)


def test_the_matched_multi_playbook_trade_carries_both_names_in_order():
    day = _day()
    (aaa,) = [t for t in day.trades if t.symbol == "AAA"]
    assert aaa.playbooks == ["Alpha Setup Long", "Beta Setup Long"]
    assert aaa.stats.target == Decimal("51.4") and aaa.stats.stop is None
    assert aaa.net_pnl == Decimal("43.66")


def test_a_stats_row_one_second_off_is_unmatched_shown_not_dropped():
    data = _set_cell(STATS.read_bytes(), 2, stats_log.OPEN_TIME, "09:40:01 EDT")
    day = _day(stats_data=data)
    (u,) = day.unmatched
    assert u.row.line == 2 and u.reason == "unmatched — 0 trades match"
    (ccc,) = [t for t in day.trades if t.symbol == "CCC"]
    assert ccc.stats is None and ccc.playbooks == []


def test_an_empty_match_cell_leaves_that_row_unmatched():
    day = _day(stats_data=_set_cell(STATS.read_bytes(), 4, stats_log.SYMBOL, ""))
    (u,) = day.unmatched
    assert u.row.line == 4 and "empty" in u.reason and stats_log.SYMBOL in u.reason


def test_two_stats_rows_claiming_one_trade_are_both_unmatched():
    records = _records(STATS.read_bytes())
    records.append(list(records[1]))
    day = _day(stats_data=_bytes(records))
    assert sorted(u.row.line for u in day.unmatched) == [2, 6]
    assert {u.reason for u in day.unmatched} == {"unmatched — 2 stats rows claim one trade"}
