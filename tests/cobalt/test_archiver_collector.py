"""Collector tests: datetime parsing quirks + CSV shape validation.

Pure-function tests, no network — `parse_csv_response` and
`_parse_finviz_datetime` are exercised directly against known-good and
known-bad response shapes drawn from DATA-SOURCE-MEMO.md's fetched
samples.

ADR-0007: Finviz writes a bare ET wall clock. Every expectation here is
the tz-aware UTC instant that wall clock denotes, and the DST regime is
picked from the DATE — which is the whole point, and why the fixed rows
below straddle both sides of both 2026 transitions.
"""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import pytest

from cobalt.archiver.collector import (
    CollectorError,
    _parse_finviz_datetime,
    _parse_finviz_wall_clock,
    parse_csv_response,
)
from cobalt.archiver.models import Interval

ET = ZoneInfo("America/New_York")


def utc(y, m, d, hh, mm):
    return datetime(y, m, d, hh, mm, tzinfo=timezone.utc)

GOOD_HEADER = "Date,Open,High,Low,Close,Volume"


def test_parses_clean_12hour_format():
    # e.g. i1/i2/i5's observed shape. EDT (UTC-4) in August.
    assert _parse_finviz_datetime("08/13/2026 04:00 AM") == utc(2026, 8, 13, 8, 0)
    assert _parse_finviz_datetime("08/27/2026 06:52 AM") == utc(2026, 8, 27, 10, 52)


def test_parses_24hour_plus_bolted_on_meridiem_quirk():
    # e.g. i15/i30's observed quirk: "15:45 PM" (24h hour + stray suffix)
    assert _parse_finviz_datetime("08/26/2026 15:45 PM") == utc(2026, 8, 26, 19, 45)
    # 11/07/2025 is EST (UTC-5) — after the 2025 fall-back.
    assert _parse_finviz_datetime("11/07/2025 09:30 AM") == utc(2025, 11, 7, 14, 30)


def test_wall_clock_helper_returns_the_naive_et_digits():
    # The format layer stays naive on purpose; the tz is applied above it.
    assert _parse_finviz_wall_clock("09/03/2026 09:30 AM") == datetime(2026, 9, 3, 9, 30)
    assert _parse_finviz_wall_clock("09/03/2026 09:30 AM").tzinfo is None


def test_every_parsed_timestamp_is_tz_aware_utc():
    """ADR-0007's root cause: a naive value reaching a `timestamptz`
    column takes the session TimeZone silently. Never naive again."""
    ts = _parse_finviz_datetime("09/03/2026 09:30 AM")
    assert ts.tzinfo is not None
    assert ts.utcoffset() == timezone.utc.utcoffset(None)


def test_dst_is_resolved_from_the_bar_date_not_from_today():
    """The SAME wall clock is a different instant in the two regimes."""
    edt = _parse_finviz_datetime("09/03/2026 09:30 AM")  # EDT, UTC-4
    est = _parse_finviz_datetime("01/15/2026 09:30 AM")  # EST, UTC-5
    assert edt == utc(2026, 9, 3, 13, 30)
    assert est == utc(2026, 1, 15, 14, 30)
    # ...and both still read back as 09:30 on the ET clock.
    assert edt.astimezone(ET).strftime("%H:%M") == "09:30"
    assert est.astimezone(ET).strftime("%H:%M") == "09:30"


@pytest.mark.parametrize(
    "raw,expected",
    [
        # 2026 spring-forward is 03/08; 2025 fall-back is 11/02.
        ("03/06/2026 09:30 AM", utc(2026, 3, 6, 14, 30)),  # EST, -5
        ("03/09/2026 09:30 AM", utc(2026, 3, 9, 13, 30)),  # EDT, -4
        ("10/31/2025 09:30 AM", utc(2025, 10, 31, 13, 30)),  # EDT, -4
        ("11/03/2025 09:30 AM", utc(2025, 11, 3, 14, 30)),  # EST, -5
    ],
)
def test_both_2026_dst_transitions_are_crossed_correctly(raw, expected):
    assert _parse_finviz_datetime(raw) == expected


def test_no_time_component_is_the_daily_fallback_failure():
    with pytest.raises(CollectorError, match="no time-of-day component"):
        _parse_finviz_datetime("08/27/2026")


def test_unparseable_datetime_fails_loud():
    with pytest.raises(CollectorError, match="Unparseable"):
        _parse_finviz_datetime("not-a-date whatsoever")


def test_valid_intraday_response_parses():
    text = (
        f"{GOOD_HEADER}\r\n"
        "08/13/2026 04:00 AM,489.649,490.717,489.2,490,7159\r\n"
        "08/13/2026 04:01 AM,490.0,490.2,489.9,490.1,320\r\n"
    )
    bars = parse_csv_response(text, "MSFT", Interval.I1)
    assert len(bars) == 2
    assert bars[0].ticker == "MSFT"
    assert bars[0].interval is Interval.I1
    assert bars[0].volume == 7159
    assert str(bars[0].close) == "490"
    # ADR-0007: the Bar that reaches the store is UTC, 04:00 ET -> 08:00Z
    assert bars[0].ts == utc(2026, 8, 13, 8, 0)
    assert bars[1].ts == utc(2026, 8, 13, 8, 1)


def test_fixed_finviz_row_lands_utc_end_to_end():
    """The 2e proof, as a test: one fixed Finviz row (the 2026-09-03 RTH
    open that ADR-0007's defect proof used) through the real parse path."""
    text = f"{GOOD_HEADER}\r\n09/03/2026 09:30 AM,324.87,327.50,324.25,325.62,569244\r\n"
    (bar,) = parse_csv_response(text, "AAPL", Interval.I5)
    assert bar.ts == utc(2026, 9, 3, 13, 30)
    assert bar.ts.astimezone(ET).strftime("%Y-%m-%d %H:%M") == "2026-09-03 09:30"
    assert bar.volume == 569244


def test_daily_fallback_shape_rejected_never_stored():
    # This is exactly what a bare/unrecognized p= silently returns
    # (DATA-SOURCE-MEMO.md: identical to p=d, 10 years of plain dates).
    text = (
        f"{GOOD_HEADER}\r\n"
        "08/16/2016,57.61,57.62,57.27,57.44,20523492\r\n"
        "08/27/2026,492.262,492.975,490.13,491.163,127123\r\n"
    )
    with pytest.raises(CollectorError, match="no time-of-day component"):
        parse_csv_response(text, "MSFT", Interval.I1)


def test_unexpected_columns_rejected():
    text = "Date,Open,High,Low,Close\r\n08/13/2026 04:00 AM,1,2,3,4\r\n"
    with pytest.raises(CollectorError, match="Unexpected columns"):
        parse_csv_response(text, "MSFT", Interval.I5)


def test_empty_response_rejected():
    with pytest.raises(CollectorError, match="Empty response"):
        parse_csv_response("", "MSFT", Interval.I5)


def test_header_only_no_data_rows_rejected():
    with pytest.raises(CollectorError, match="No data rows"):
        parse_csv_response(f"{GOOD_HEADER}\r\n", "MSFT", Interval.I5)


def test_malformed_row_length_rejected():
    text = f"{GOOD_HEADER}\r\n08/13/2026 04:00 AM,1,2,3\r\n"
    with pytest.raises(CollectorError, match="Malformed row"):
        parse_csv_response(text, "MSFT", Interval.I5)


def test_unparseable_price_rejected():
    text = f"{GOOD_HEADER}\r\n08/13/2026 04:00 AM,NOT_A_NUMBER,2,3,4,100\r\n"
    with pytest.raises(CollectorError, match="Unparseable row"):
        parse_csv_response(text, "MSFT", Interval.I5)
