"""Collector tests: datetime parsing quirks + CSV shape validation.

Pure-function tests, no network — `parse_csv_response` and
`_parse_finviz_datetime` are exercised directly against known-good and
known-bad response shapes drawn from DATA-SOURCE-MEMO.md's fetched
samples.
"""

from datetime import datetime

import pytest

from cobalt.archiver.collector import (
    CollectorError,
    _parse_finviz_datetime,
    parse_csv_response,
)
from cobalt.archiver.models import Interval

GOOD_HEADER = "Date,Open,High,Low,Close,Volume"


def test_parses_clean_12hour_format():
    # e.g. i1/i2/i5's observed shape
    assert _parse_finviz_datetime("08/13/2026 04:00 AM") == datetime(2026, 8, 13, 4, 0)
    assert _parse_finviz_datetime("08/27/2026 06:52 AM") == datetime(2026, 8, 27, 6, 52)


def test_parses_24hour_plus_bolted_on_meridiem_quirk():
    # e.g. i15/i30's observed quirk: "15:45 PM" (24h hour + stray suffix)
    assert _parse_finviz_datetime("08/26/2026 15:45 PM") == datetime(2026, 8, 26, 15, 45)
    assert _parse_finviz_datetime("11/07/2025 09:30 AM") == datetime(2025, 11, 7, 9, 30)


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
