"""Daily bars and the higher-timeframe references (R5).

The daily series comes from the daily-bars collector
(`radar.collector.FinvizDailyBarsCollector`, one fetch per name per ET
day). Everything here reads only sessions STRICTLY BEFORE the trade date:
a daily export fetched mid-session may carry today's partial row, and a
prior-session reference computed from it would be a future read.

Conventions (Astra R1-9):

* prior session = the latest daily bar with `session_date < trade_date`;
* daily ATR = Wilder ATR(14) over every prior session in the series
  (`indicators.wilder_atr`, same seed/warm-up rules as intraday);
* `htf_level_proximity` = min(|last − prior high|, |last − prior low|) ÷
  daily ATR — units `daily_atr`, reference = whichever prior level is
  nearer, `prior_high` on an exact tie. HTF range = prior-session H/L
  (`range_break.htf_range: prior_session_high_low`, replay_pending);
* `RangeBreak(HTF).day_count`: today breaks UP when the session high so
  far exceeds the prior high, DOWN when the session low undercuts the
  prior low. Both at once = an outside day: no direction, no count
  (reported, never guessed). The count is 1 + the number of consecutive
  prior sessions, walking back, whose high exceeded the session before
  them (up) / whose low undercut it (down). Neither break → no count.
"""

from __future__ import annotations

import csv
import io
from datetime import date, datetime
from decimal import Decimal, InvalidOperation, localcontext
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_validator

from .indicators import ATR_PERIOD, PRECISION, AtrObservation, InsufficientBars, wilder_atr

EXPECTED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]


class NoDailyBars(ValueError):
    """No prior session exists in the series for the trade date."""


class DailyBar(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    session_date: date
    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal
    volume: int = Field(ge=0)


class DailySeries(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    ticker: str = Field(min_length=1)
    bars: tuple[DailyBar, ...]
    fetched_at: AwareDatetime | None = None
    source: str | None = None

    @field_validator("bars")
    @classmethod
    def _ordered(cls, v: tuple[DailyBar, ...]) -> tuple[DailyBar, ...]:
        if any(a.session_date >= b.session_date for a, b in zip(v, v[1:])):
            raise ValueError("daily bars must be strictly increasing by session_date")
        return v

    def before(self, trade_date: date) -> tuple[DailyBar, ...]:
        return tuple(bar for bar in self.bars if bar.session_date < trade_date)


def parse_daily_csv(text: str, ticker: str) -> tuple[DailyBar, ...]:
    """The daily export shape: exactly Date,Open,High,Low,Close,Volume with
    MM/DD/YYYY dates. A date carrying a time is an intraday body and is
    refused; so is any other column set, an empty body or a bad cell."""
    rows = list(csv.reader(io.StringIO(text)))
    if not rows or rows[0] != EXPECTED_COLUMNS:
        raise ValueError(
            f"{ticker}: daily export columns {rows[0] if rows else []} != {EXPECTED_COLUMNS}"
        )
    if len(rows) == 1:
        raise ValueError(f"{ticker}: daily export has no data rows")
    bars: list[DailyBar] = []
    for row in rows[1:]:
        if len(row) != len(EXPECTED_COLUMNS):
            raise ValueError(f"{ticker}: malformed daily row {row!r}")
        raw_date = row[0].strip()
        if " " in raw_date:
            raise ValueError(f"{ticker}: daily date {raw_date!r} has a time-of-day component")
        try:
            session_date = datetime.strptime(raw_date, "%m/%d/%Y").date()
            bars.append(DailyBar(
                session_date=session_date, open=Decimal(row[1]), high=Decimal(row[2]),
                low=Decimal(row[3]), close=Decimal(row[4]), volume=int(Decimal(row[5])),
            ))
        except (ValueError, InvalidOperation) as e:
            raise ValueError(f"{ticker}: unparseable daily row {row!r} ({e})") from e
    bars.sort(key=lambda bar: bar.session_date)
    return DailySeries(ticker=ticker, bars=tuple(bars)).bars


class PriorSession(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    session_date: date
    high: Decimal
    low: Decimal
    close: Decimal


def prior_session(series: DailySeries, trade_date: date) -> PriorSession:
    prior = series.before(trade_date)
    if not prior:
        raise NoDailyBars(f"{series.ticker}: no daily bar before {trade_date}")
    bar = prior[-1]
    return PriorSession(session_date=bar.session_date, high=bar.high, low=bar.low, close=bar.close)


def daily_atr(series: DailySeries, trade_date: date, period: int = ATR_PERIOD) -> AtrObservation:
    prior = series.before(trade_date)
    if not prior:
        raise NoDailyBars(f"{series.ticker}: no daily bar before {trade_date}")
    return wilder_atr(prior, period)


class HtfProximity(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    value: Decimal
    units: Literal["daily_atr"] = "daily_atr"
    reference: Literal["prior_high", "prior_low"]
    level: Decimal
    last_price: Decimal
    prior: PriorSession
    atr: AtrObservation


def htf_level_proximity(series: DailySeries, trade_date: date, last_price: Decimal) -> HtfProximity:
    prior = prior_session(series, trade_date)
    atr = daily_atr(series, trade_date)
    if atr.value <= 0:
        raise InsufficientBars("daily ATR is zero — proximity undefined", ATR_PERIOD, 0)
    to_high, to_low = abs(last_price - prior.high), abs(last_price - prior.low)
    reference, level, distance = (
        ("prior_high", prior.high, to_high) if to_high <= to_low else ("prior_low", prior.low, to_low)
    )
    with localcontext() as ctx:
        ctx.prec = PRECISION
        value = distance / atr.value
    return HtfProximity(
        value=value, reference=reference, level=level, last_price=last_price, prior=prior, atr=atr
    )


class HtfRangeBreak(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    direction: Literal["up", "down"] | None
    day_count: int | None
    outside_day: bool = False
    range_high: Decimal
    range_low: Decimal
    session_high: Decimal
    session_low: Decimal
    prior_session_date: date


def htf_range_break(
    series: DailySeries, trade_date: date, *, session_high: Decimal, session_low: Decimal
) -> HtfRangeBreak:
    prior = series.before(trade_date)
    if not prior:
        raise NoDailyBars(f"{series.ticker}: no daily bar before {trade_date}")
    last = prior[-1]
    base = dict(
        range_high=last.high, range_low=last.low, session_high=session_high,
        session_low=session_low, prior_session_date=last.session_date,
    )
    up, down = session_high > last.high, session_low < last.low
    if up and down:
        return HtfRangeBreak(direction=None, day_count=None, outside_day=True, **base)
    if not (up or down):
        return HtfRangeBreak(direction=None, day_count=None, **base)
    direction: Literal["up", "down"] = "up" if up else "down"
    count = 1
    for j in range(len(prior) - 1, 0, -1):
        current, before = prior[j], prior[j - 1]
        broke = current.high > before.high if direction == "up" else current.low < before.low
        if not broke:
            break
        count += 1
    return HtfRangeBreak(direction=direction, day_count=count, **base)


__all__ = [
    "DailyBar", "DailySeries", "EXPECTED_COLUMNS", "HtfProximity", "HtfRangeBreak",
    "NoDailyBars", "PriorSession", "daily_atr", "htf_level_proximity",
    "htf_range_break", "parse_daily_csv", "prior_session",
]
