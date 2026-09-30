"""DRC D1-2 — the trading-log parser, against the D1-0 fixtures.

Mutations are one-line edits of the fixture's own bytes; column names
come from `trading_log`'s constants or the fixture header, never retyped
as a header of his.
"""

from __future__ import annotations

import csv
import io
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.drc import trading_log
from cobalt.drc.detect import detect_kind
from cobalt.drc.models import ExecSide, Kind, Outcome
from cobalt.drc.trading_log import TradingLogSource, chronological

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures" / "drc"
E1 = FIXTURES / "trading_log_e1.csv"
DAY = date(2001, 1, 2)


def _records(data: bytes) -> list[list[str]]:
    return list(csv.reader(io.StringIO(data.decode(), newline="")))


def _bytes(records: list[list[str]]) -> bytes:
    return "".join(",".join(r) + "\n" for r in records).encode()


def _parse(data: bytes, day: date = DAY, name: str = "t.md"):
    return TradingLogSource().parse(data, day, detect_kind(name, data))


def _set_cell(data: bytes, line: int, column: str, value: str) -> bytes:
    records = _records(data)
    records[line - 1][records[0].index(column)] = value
    return _bytes(records)


def _drop_column(data: bytes, column: str) -> bytes:
    records = _records(data)
    i = records[0].index(column)
    return _bytes([r[:i] + r[i + 1:] for r in records])


def test_the_fixture_round_trips_through_the_mutation_helpers_byte_for_byte():
    assert _bytes(_records(E1.read_bytes())) == E1.read_bytes()


def test_e1s_cut_parses_every_row():
    p = _parse(E1.read_bytes())
    assert p.result.outcome is Outcome.PARSED, p.result.reason
    assert p.result.kind is Kind.TRADING_LOG
    assert len(p.executions) == 14
    first = p.executions[0]
    assert first.line == 2 and first.symbol == "AAA" and first.side is ExecSide.SELL
    assert first.price == Decimal("50.6") and first.qty == 50
    assert first.account == "ACCT1" and first.order_id and first.route and first.broker
    assert first.order_type == "Margin"


def test_the_date_is_the_import_date_never_read_from_the_file():
    """R17 (3): the same bytes under two import dates."""
    data = E1.read_bytes()
    for day in (date(2001, 1, 2), date(2001, 7, 3)):
        p = _parse(data, day)
        assert {e.time.date() for e in p.executions} == {day}


def test_the_clock_time_is_read_as_et_with_its_own_offset():
    winter = _parse(E1.read_bytes(), date(2001, 1, 2)).executions[-1]
    summer = _parse(E1.read_bytes(), date(2001, 7, 3)).executions[-1]
    assert winter.time.utcoffset() == timedelta(hours=-5)
    assert summer.time.utcoffset() == timedelta(hours=-4)
    assert (winter.time.hour, winter.time.minute, winter.time.second) == (9, 40, 0)


def test_columns_are_read_by_name_so_a_reorder_changes_nothing():
    records = _records(E1.read_bytes())
    order = list(reversed(range(len(records[0]) - 1))) + [len(records[0]) - 1]
    shuffled = _bytes([[r[i] for i in order] for r in records])
    a, b = _parse(E1.read_bytes()), _parse(shuffled)
    assert b.result.outcome is Outcome.PARSED
    assert a.executions == b.executions


def test_an_extra_column_parses_and_sets_the_shape_flag():
    records = _records(E1.read_bytes())
    widened = _bytes([r[:-1] + (["Added"] if i == 0 else ["x"]) + [""] for i, r in enumerate(records)])
    p = _parse(widened)
    assert p.result.outcome is Outcome.PARSED
    assert p.result.degraded == "trading_log_shape" and p.result.extras == ["Added"]
    assert p.executions == _parse(E1.read_bytes()).executions


@pytest.mark.parametrize("column", trading_log.PAIRING_INPUTS)
def test_a_pairing_input_column_removed_is_partial_rows_parsed_pairing_not_computed(column):
    p = _parse(_drop_column(E1.read_bytes(), column))
    assert p.result.outcome is Outcome.PARTIAL
    assert p.result.missing == [column]
    assert p.result.partial_flag == f"PARTIAL — missing: {column}"
    assert len(p.executions) == 14
    field = {"Time": "time", "Symbol": "symbol", "Side": "side", "Price": "price", "Qty": "qty"}[column]
    assert all(getattr(e, field) is None for e in p.executions)
    assert p.result.not_computed == {"pairing": f"not computed — missing: {column}"}


def test_a_non_pairing_column_removed_is_partial_and_pairing_still_runs():
    p = _parse(_drop_column(E1.read_bytes(), trading_log.ACCOUNT))
    assert p.result.outcome is Outcome.PARTIAL and p.result.missing == [trading_log.ACCOUNT]
    assert all(e.account is None for e in p.executions)
    assert p.result.not_computed == {}


@pytest.mark.parametrize(
    "column,value",
    [
        (trading_log.PRICE, "abc"),
        (trading_log.PRICE, "-1.5"),
        (trading_log.PRICE, "0"),
        (trading_log.SIDE, "X"),
        (trading_log.TIME, "9:40:00"),
        (trading_log.TIME, "25:00:00"),
        (trading_log.QTY, "0"),
        (trading_log.QTY, "1.5"),
        (trading_log.SYMBOL, ""),
        (trading_log.ACCOUNT, ""),
    ],
)
def test_one_bad_cell_fails_the_whole_file_naming_the_line_and_keeps_no_rows(column, value):
    p = _parse(_set_cell(E1.read_bytes(), 7, column, value))
    assert p.result.outcome is Outcome.FAILED
    assert p.result.line == 7 and "line 7" in p.result.reason and "t.md" in p.result.reason
    assert p.executions == []


def test_a_row_with_the_wrong_cell_count_fails_the_file():
    lines = E1.read_bytes().split(b"\n")
    lines[4] = lines[4] + b"extra,"
    p = _parse(b"\n".join(lines))
    assert p.result.outcome is Outcome.FAILED and p.result.line == 5


def test_a_value_under_the_unnamed_trailing_column_fails_the_file():
    lines = E1.read_bytes().split(b"\n")
    lines[2] = lines[2] + b"oops"
    p = _parse(b"\n".join(lines))
    assert p.result.outcome is Outcome.FAILED and p.result.line == 3


def test_a_blank_line_inside_the_file_fails_it_but_trailing_blank_lines_do_not():
    data = E1.read_bytes()
    assert _parse(data + b"\n\n").result.outcome is Outcome.PARSED
    lines = data.split(b"\n")
    lines.insert(3, b"")
    p = _parse(b"\n".join(lines))
    assert p.result.outcome is Outcome.FAILED and p.result.line == 4


def test_undecodable_bytes_after_the_header_fail_the_file():
    """`54` rows 3 / 10: the failure names the line the bad byte sits on —
    the line after the fixture's last."""
    p = _parse(E1.read_bytes() + b"\xff\xfe,,\n")
    assert p.result.outcome is Outcome.FAILED
    assert p.result.line == E1.read_bytes().count(b"\n") + 1


def test_two_accounts_are_one_bucket_read_and_stored_never_a_gate():
    """R94. E1 shows one account; the second is a constructed literal."""
    data = _set_cell(_set_cell(E1.read_bytes(), 3, trading_log.ACCOUNT, "ACCT2"),
                     9, trading_log.ACCOUNT, "ACCT2")
    p = _parse(data)
    assert p.result.outcome is Outcome.PARSED
    assert {e.account for e in p.executions} == {"ACCT1", "ACCT2"}


def test_rows_sharing_one_time_are_taken_in_reverse_file_order():
    """E1 is newest-first: the later line of two fills sharing one `Time`
    is the earlier fill (E1's scale-in evidence, build report `## E1`)."""
    ordered = chronological(_parse(E1.read_bytes()).executions)
    same = [e for e in ordered if e.symbol == "AAA" and e.time.hour == 10 and e.time.minute == 15]
    assert [e.line for e in same] == [9, 8]
    assert [e.price for e in same] == [Decimal("50.18"), Decimal("50.2")]
    times = [e.time for e in ordered]
    assert times == sorted(times) and ordered[0].line == 15


def test_the_parser_is_reached_only_through_a_trading_log_detection():
    data = (FIXTURES / "stats_log_e1.csv").read_bytes()
    with pytest.raises(ValueError, match="only through detect_kind"):
        TradingLogSource().parse(data, DAY, detect_kind("s.md", data))
