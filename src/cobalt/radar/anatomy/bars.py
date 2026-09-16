"""Working-timeframe buckets that say whether they are whole (Astra R1-8).

`archiver.aggregate(bars, 2)` is the one aggregation path and it stays
that way — but it emits a bucket holding only its first minute as if it
were a closed 2m bar, and accepts a missing intra-bucket minute in
silence. The anatomy cannot: a volume climax or a trigger read off half a
bar is a fabricated number. So this module wraps the aggregate:

* only i1 bars that CLOSED by `as_of` are used (`ts + 1 min <= as_of`) —
  replay never reads the future;
* a bucket that has not closed by `as_of` is excluded and named
  (`unclosed_bucket`), never emitted;
* a closed bucket missing any minute is emitted FLAGGED
  (`complete=False`, the missing minute timestamps listed). A minute with
  no print and a minute that was never fetched look identical in
  `system.bars`, so the flag is honest about both; detectors refuse
  incomplete buckets rather than guess (`IncompleteBucket`).
"""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_validator

from cobalt.archiver.aggregate import aggregate
from cobalt.archiver.models import Bar, Interval
from cobalt.session.models import Session


class IncompleteBucket(ValueError):
    """A detector was handed a working bar with a missing minute."""


class WorkingBar(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    #: Bucket start, UTC.
    ts: AwareDatetime
    minutes: int = Field(gt=0)
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int = Field(ge=0)
    complete: bool
    minutes_present: int = Field(ge=0)
    missing_minutes: tuple[AwareDatetime, ...] = ()

    @property
    def end(self) -> datetime:
        return self.ts + timedelta(minutes=self.minutes)

    @property
    def body(self) -> Decimal:
        return abs(self.close - self.open)

    @property
    def direction(self) -> Literal["up", "down", "flat"]:
        if self.close > self.open:
            return "up"
        if self.close < self.open:
            return "down"
        return "flat"


class WorkingSeries(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    ticker: str
    minutes: int
    as_of: AwareDatetime
    bars: tuple[WorkingBar, ...]
    unclosed_bucket: AwareDatetime | None = None

    @field_validator("bars")
    @classmethod
    def _ordered(cls, v: tuple[WorkingBar, ...]) -> tuple[WorkingBar, ...]:
        if any(a.ts >= b.ts for a, b in zip(v, v[1:])):
            raise ValueError("working bars must be strictly ordered by ts")
        return v


def working_bars(i1: Sequence[Bar], minutes: int, *, as_of: datetime) -> WorkingSeries:
    """Closed working-TF buckets from i1 bars, completeness-flagged."""
    if as_of.tzinfo is None:
        raise ValueError("as_of must be tz-aware (ADR-0007)")
    tickers = {bar.ticker for bar in i1}
    if len(tickers) > 1:
        raise ValueError(f"working_bars takes one ticker at a time, got {sorted(tickers)}")
    if any(bar.interval is not Interval.I1 for bar in i1):
        raise ValueError("working_bars aggregates i1 bars only")
    one = timedelta(minutes=1)
    closed = [bar for bar in i1 if bar.ts + one <= as_of]
    ticker = next(iter(tickers)) if tickers else ""
    if not closed:
        return WorkingSeries(ticker=ticker, minutes=minutes, as_of=as_of, bars=())

    present: dict[datetime, set[datetime]] = {}
    width = timedelta(minutes=minutes)
    out: list[WorkingBar] = []
    unclosed: datetime | None = None
    aggregated = aggregate(closed, minutes)
    for bar in closed:
        # Same bucket as the aggregate's ET wall-clock floor: every stored
        # interval divides the hour and ET offsets are whole hours.
        start = bar.ts.replace(
            minute=(bar.ts.minute // minutes) * minutes, second=0, microsecond=0
        )
        present.setdefault(start, set()).add(bar.ts)
    for agg in aggregated:
        if agg.ts + width > as_of:
            unclosed = agg.ts
            continue
        minutes_seen = present[agg.ts]
        expected = {agg.ts + timedelta(minutes=m) for m in range(minutes)}
        missing = tuple(sorted(expected - minutes_seen))
        out.append(
            WorkingBar(
                ts=agg.ts, minutes=minutes, open=agg.open, high=agg.high, low=agg.low,
                close=agg.close, volume=agg.volume, complete=not missing,
                minutes_present=len(minutes_seen), missing_minutes=missing,
            )
        )
    return WorkingSeries(
        ticker=ticker, minutes=minutes, as_of=as_of, bars=tuple(out), unclosed_bucket=unclosed
    )


def rth_only(series: WorkingSeries, clock) -> tuple[WorkingBar, ...]:
    """Buckets that open AND close inside RTH on the session clock."""
    return tuple(
        bar for bar in series.bars
        if clock.session(bar.ts) is Session.RTH
        and clock.session(bar.end - timedelta(seconds=1)) is Session.RTH
    )


def require_complete(bars: Sequence[WorkingBar]) -> None:
    for bar in bars:
        if not bar.complete:
            raise IncompleteBucket(
                f"working bar {bar.ts.isoformat()} has {bar.minutes_present}/{bar.minutes} "
                "minutes — refusing to read a partial bucket"
            )


__all__ = [
    "IncompleteBucket", "WorkingBar", "WorkingSeries", "require_complete",
    "rth_only", "working_bars",
]
