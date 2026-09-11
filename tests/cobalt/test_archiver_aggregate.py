"""Pure ET-floor OHLCV aggregation tests."""

from datetime import datetime, timezone
from decimal import Decimal

from cobalt.archiver.aggregate import aggregate
from cobalt.archiver.models import Bar, Interval


def _bar(ts, o, h, l, c, v):
    return Bar(ticker="AAA", interval=Interval.I1, ts=ts, open=Decimal(o), high=Decimal(h), low=Decimal(l), close=Decimal(c), volume=v)


def test_ohlcv_missing_minute_and_et_bucket():
    bars = [
        _bar(datetime(2026, 9, 3, 13, 30, tzinfo=timezone.utc), "1", "3", "1", "2", 10),
        _bar(datetime(2026, 9, 3, 13, 32, tzinfo=timezone.utc), "2", "4", "0", "3", 20),
    ]
    rows = aggregate(bars, 2)
    assert len(rows) == 2
    assert (rows[0].open, rows[0].high, rows[0].low, rows[0].close, rows[0].volume) == (Decimal("1"), Decimal("3"), Decimal("1"), Decimal("2"), 10)


def test_dst_dates_keep_0930_et_in_distinct_utc_offsets():
    winter = _bar(datetime(2026, 1, 15, 14, 30, tzinfo=timezone.utc), "1", "1", "1", "1", 1)
    summer = _bar(datetime(2026, 9, 3, 13, 30, tzinfo=timezone.utc), "1", "1", "1", "1", 1)
    out = aggregate([winter, summer], 2)
    assert [x.ts.hour for x in out] == [14, 13]

