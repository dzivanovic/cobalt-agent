"""Slope, normalised slope and flatness of an indicator series (FINAL §3 D1:
`EMA9.slope`, `slope_norm(x)` `A-11`, `flat(x, window)` `A-09` / `A-10`;
setups one build STEP-3).

Pure: a series of values (oldest first, one per closed working bar) in,
typed observation out.

* `slope(series, n) = (x_t − x_{t−n}) / n` — price per working bar.
* `slope_norm(series, n, atr) = (x_t − x_{t−n}) / (n · atr)` — ATR-normalised
  per bar; `atr` is the frame's `ATR(working_tf)` (seeded, [F-10]). A zero
  ATR is unknown (`insufficient_bars`), never inf (FINAL §4).
* `n` is the tunable `slope_norm.bars` (a global engine row, `A-11`); a null
  row reads `slope_norm.bars_unset`; an absent row is a config error.
* `flat(norm_slopes, threshold)`: every normalised slope in the window has
  `|s| <= threshold`; an empty window is unknown. The threshold is the
  `per_indicator` row `flat_threshold.<indicator>` (`A-09`, `A-10`) — F1 is
  not widened, so a null row stays null (`flat_threshold.<ind>_unset`).
  The `flat(...)` ATOM and its window argument are interpreted at STEP-5
  with `between`; this module is the detector it will call.

A slope flips sign with the mirror; the frame marks the atoms accordingly.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from decimal import Decimal, localcontext
from typing import Literal

from pydantic import BaseModel, ConfigDict

from cobalt.taxonomy.tunables import TunableRow

from .indicators import PRECISION

TUNABLE_KEYS = ("slope_norm.bars",)
FLAT_KEYS = {"EMA9": "flat_threshold.ema9", "VWAP": "flat_threshold.vwap"}


class SlopeObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    value: Decimal | None
    n: int
    unavailable: Literal["insufficient_bars"] | None = None


def slope_bars(rows: Mapping[str, TunableRow]) -> int | None:
    """`slope_norm.bars`, or None when its row is null (`_unset`)."""
    row = rows["slope_norm.bars"]
    return None if row.value is None else int(row.value)


def flat_threshold(rows: Mapping[str, TunableRow], indicator: str) -> Decimal | None:
    row = rows[FLAT_KEYS[indicator]]
    return None if row.value is None else Decimal(str(row.value))


def slope(series: Sequence[Decimal], n: int) -> SlopeObservation:
    if n <= 0:
        raise ValueError(f"slope window must be positive, got {n}")
    if len(series) < n + 1:
        return SlopeObservation(value=None, n=n, unavailable="insufficient_bars")
    with localcontext() as ctx:
        ctx.prec = PRECISION
        return SlopeObservation(value=(series[-1] - series[-1 - n]) / n, n=n)


def slope_norm(series: Sequence[Decimal], n: int, *, atr: Decimal | None) -> SlopeObservation:
    raw = slope(series, n)
    if raw.value is None or atr is None or atr == 0:
        return SlopeObservation(value=None, n=n, unavailable="insufficient_bars")
    with localcontext() as ctx:
        ctx.prec = PRECISION
        return SlopeObservation(value=(series[-1] - series[-1 - n]) / (n * atr), n=n)


def flat(norm_slopes: Sequence[Decimal], threshold: Decimal) -> bool | None:
    if not norm_slopes:
        return None
    return all(abs(s) <= threshold for s in norm_slopes)


__all__ = [
    "FLAT_KEYS", "SlopeObservation", "TUNABLE_KEYS", "flat", "flat_threshold", "slope", "slope_bars", "slope_norm",
]
