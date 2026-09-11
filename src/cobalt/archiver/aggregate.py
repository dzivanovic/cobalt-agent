"""Pure OHLCV aggregation from minute bars on ET wall-clock buckets."""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

from .models import Bar, Interval

ET = ZoneInfo("America/New_York")


def aggregate(bars: list[Bar], minutes: int) -> list[Bar]:
    if minutes <= 0:
        raise ValueError(f"aggregate minutes must be positive, got {minutes}")
    try:
        interval = Interval(f"i{minutes}")
    except ValueError as e:
        raise ValueError(f"no stored Interval exists for {minutes}-minute bars") from e
    buckets: dict[tuple[str, datetime], list[Bar]] = defaultdict(list)
    for bar in sorted(bars, key=lambda item: (item.ticker, item.ts)):
        local = bar.ts.astimezone(ET)
        bucket = local.replace(
            minute=(local.minute // minutes) * minutes,
            second=0,
            microsecond=0,
        )
        buckets[(bar.ticker, bucket)].append(bar)
    output: list[Bar] = []
    for (ticker, bucket), rows in sorted(buckets.items(), key=lambda item: item[0]):
        rows.sort(key=lambda item: item.ts)
        output.append(
            Bar(
                ticker=ticker,
                interval=interval,
                ts=bucket,
                open=rows[0].open,
                high=max(row.high for row in rows),
                low=min(row.low for row in rows),
                close=rows[-1].close,
                volume=sum(row.volume for row in rows),
            )
        )
    return output


__all__ = ["aggregate"]
