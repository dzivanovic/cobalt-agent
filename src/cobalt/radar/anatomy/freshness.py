"""RVOL as a replayable observation, and staleness by dependency type
(S2-P2 STEP-3, Astra R1-12).

RVOL. The screener snapshot carries each name's vendor RVOL, but the pool
row keeps only rank and membership, so a bars-only replay could never
reproduce it. `rvol_observations` turns the scan's own source sets into
one timestamped `RvolObservation` per ticker for the S5 stage to store in
the run receipt (L57). PRECEDENCE when more than one source carries a
ticker, fixed and stated on every observation:

  1. a screen before a list (the pool's own D3 grouping);
  2. lower note order first;
  3. lexically lower source id (deterministic tie-break).

Only healthy, active sources count — a degraded source's held tickers
carry no fresh metric. A carried ticker with no RVOL cell is kept with
`value=None`; it is never dropped and never zero.

STALENESS BY DEPENDENCY TYPE. The 09-14 "older than 2 × radar.scan_interval
→ input_stale" rule is right for intraday data and wrong for everything
else, so each dependency type has its own rule:

* intraday bars and RVOL → `intraday_2x_scan_interval`: stale when the age
  exceeds 2 × scan_interval (equal is fresh);
* daily bars → `daily_last_completed_session`: fresh only when the series
  holds the last trading day before the trade date. A wall-clock age is
  meaningless here — a Friday bar is current all Monday morning;
* policy, tunable and settings inputs → `versioned_never_wall_clock`: they
  are replaced by a new version (a new hash), never aged out.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from datetime import date, datetime, timedelta
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from cobalt.radar.models import SourceHealth, SourceSet

from .daily import DailySeries

PRECEDENCE = "screen_before_list_then_note_order_then_source_id"

#: Far enough back to cross any exchange closure; a longer run of
#: non-trading days is a broken calendar, not a gap to walk through.
MAX_CALENDAR_WALK_DAYS = 14


class RvolObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    ticker: str = Field(min_length=1)
    value: float | None
    observed_at: AwareDatetime
    source: str
    #: Every source that carried the ticker, winner first.
    candidates: tuple[str, ...]
    precedence: Literal["screen_before_list_then_note_order_then_source_id"] = PRECEDENCE


def _precedence_key(source: SourceSet) -> tuple[int, int, str]:
    return (0 if source.kind == "screen" else 1, source.note_order, source.source)


def rvol_observations(
    source_sets: Sequence[SourceSet], *, observed_at: datetime
) -> dict[str, RvolObservation]:
    """One RVOL observation per ticker from this scan's source sets."""
    if observed_at.tzinfo is None:
        raise ValueError("observed_at must be tz-aware (ADR-0007)")
    usable = sorted(
        (s for s in source_sets if s.active and s.health is SourceHealth.HEALTHY),
        key=_precedence_key,
    )
    carriers: dict[str, list[SourceSet]] = {}
    for source in usable:
        for ticker in source.metrics:
            carriers.setdefault(ticker.strip().upper(), []).append(source)
    out: dict[str, RvolObservation] = {}
    for ticker, sources in carriers.items():
        winner = sources[0]
        metrics = next(v for k, v in winner.metrics.items() if k.strip().upper() == ticker)
        out[ticker] = RvolObservation(
            ticker=ticker,
            value=metrics.get("rvol"),
            observed_at=observed_at,
            source=winner.source,
            candidates=tuple(s.source for s in sources),
        )
    return out


class IntradayStaleness(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    rule: Literal["intraday_2x_scan_interval"] = "intraday_2x_scan_interval"
    observed_at: AwareDatetime
    as_of: AwareDatetime
    age_seconds: float
    ttl_seconds: int
    stale: bool


def intraday_staleness(
    *, observed_at: datetime, as_of: datetime, scan_interval: int
) -> IntradayStaleness:
    if scan_interval <= 0:
        raise ValueError(f"scan_interval must be positive, got {scan_interval}")
    if observed_at > as_of:
        raise ValueError(
            f"observation at {observed_at.isoformat()} is after as_of {as_of.isoformat()} — "
            "a replay never reads the future"
        )
    age = (as_of - observed_at).total_seconds()
    ttl = 2 * scan_interval
    return IntradayStaleness(
        observed_at=observed_at, as_of=as_of, age_seconds=age, ttl_seconds=ttl, stale=age > ttl
    )


def previous_trading_day(day: date, is_trading_day: Callable[[date], bool]) -> date:
    """The last trading day strictly before `day`."""
    probe = day
    for _ in range(MAX_CALENDAR_WALK_DAYS):
        probe -= timedelta(days=1)
        if is_trading_day(probe):
            return probe
    raise ValueError(f"no trading day in the {MAX_CALENDAR_WALK_DAYS} days before {day}")


class DailyStaleness(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    rule: Literal["daily_last_completed_session"] = "daily_last_completed_session"
    trade_date: date
    expected_session: date
    latest_session: date | None
    stale: bool


def daily_staleness(
    series: DailySeries, *, trade_date: date, is_trading_day: Callable[[date], bool]
) -> DailyStaleness:
    expected = previous_trading_day(trade_date, is_trading_day)
    prior = series.before(trade_date)
    latest = prior[-1].session_date if prior else None
    return DailyStaleness(
        trade_date=trade_date, expected_session=expected, latest_session=latest,
        stale=latest != expected,
    )


class PolicyStaleness(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    rule: Literal["versioned_never_wall_clock"] = "versioned_never_wall_clock"
    version_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    stale: Literal[False] = False


def policy_staleness(*, version_sha256: str) -> PolicyStaleness:
    return PolicyStaleness(version_sha256=version_sha256)


__all__ = [
    "DailyStaleness", "IntradayStaleness", "PRECEDENCE", "PolicyStaleness",
    "RvolObservation", "daily_staleness", "intraday_staleness", "policy_staleness",
    "previous_trading_day", "rvol_observations",
]
