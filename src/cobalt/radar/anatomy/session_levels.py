"""Session levels — DayRange, VWAP, PMH/PML, PDH/PDL (FINAL §3 D1; setups
one build STEP-3).

Pure: bars in, typed observation out. Prices are in whatever coordinates the
bars are in — the Frame hands the short side mirrored bars, so the same code
yields the short side's levels (FINAL §2.1 [F-04]).

* `DayRange` (convention `dayrange.session`, `A-06`): the RTH run's high and
  low, 09:30 to the last closed working bar; premarket excluded.
  `upper_third = low + 2/3 · (high − low)` — the top third's floor.
* `VWAP` (convention `vwap.anchor`, `A-12`): RTH-anchored from the 09:30 bar;
  Σ(typical · volume) / Σ volume over the closed RTH i1 bars, typical =
  (high + low + close) / 3. No volume → `insufficient_bars` (never a divide
  by zero).
* `PMH` / `PML`: the premarket i1 high / low. No premarket print → none
  (the frame serves `null`, `not_instantiated`).
* `PDH` / `PDL`: the prior session's daily high / low (`daily.prior_session`,
  the one path); no prior daily bar → `NoDailyBars`.

No detector here reads a tunable: `TUNABLE_KEYS = ()`. The two conventions
are rows (`tunables.yaml`, unit `label`); the frame's resolvers declare them.
"""

from __future__ import annotations

from collections.abc import Sequence
from datetime import date
from decimal import Decimal, localcontext
from typing import Literal

from pydantic import BaseModel, ConfigDict

from .daily import DailySeries, prior_session
from .indicators import OHLCV, PRECISION

TUNABLE_KEYS: tuple[str, ...] = ()
DAYRANGE_CONVENTION = "dayrange.session"
VWAP_CONVENTION = "vwap.anchor"


class DayRange(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    high: Decimal
    low: Decimal
    upper_third: Decimal


class VwapObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    value: Decimal | None
    bars_used: int
    volume: int
    unavailable: Literal["insufficient_bars"] | None = None


class Levels(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    high: Decimal
    low: Decimal
    session_date: date | None = None


def day_range(run: Sequence[OHLCV]) -> DayRange | None:
    if not run:
        return None
    high, low = max(b.high for b in run), min(b.low for b in run)
    with localcontext() as ctx:
        ctx.prec = PRECISION
        upper_third = low + Decimal(2) / 3 * (high - low)
    return DayRange(high=high, low=low, upper_third=upper_third)


def vwap(rth_i1: Sequence[OHLCV]) -> VwapObservation:
    volume = sum(b.volume for b in rth_i1)
    if not rth_i1 or volume == 0:
        return VwapObservation(value=None, bars_used=len(rth_i1), volume=volume, unavailable="insufficient_bars")
    with localcontext() as ctx:
        ctx.prec = PRECISION
        weighted = sum(((b.high + b.low + b.close) / 3 * b.volume for b in rth_i1), Decimal(0))
        value = weighted / volume
    return VwapObservation(value=value, bars_used=len(rth_i1), volume=volume)


def premarket_levels(premarket_i1: Sequence[OHLCV]) -> Levels | None:
    if not premarket_i1:
        return None
    return Levels(high=max(b.high for b in premarket_i1), low=min(b.low for b in premarket_i1))


def prior_day_levels(daily: DailySeries, trade_date: date) -> Levels:
    prior = prior_session(daily, trade_date)
    return Levels(high=prior.high, low=prior.low, session_date=prior.session_date)


__all__ = [
    "DAYRANGE_CONVENTION", "DayRange", "Levels", "TUNABLE_KEYS", "VWAP_CONVENTION", "VwapObservation",
    "day_range", "premarket_levels", "prior_day_levels", "vwap",
]
