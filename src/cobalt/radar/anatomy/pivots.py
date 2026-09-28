"""Swing pivots (TAXONOMY v0.7 §3.3; FINAL §3 D2; setups one build STEP-4).

A pivot high is a bar whose high is STRICTLY above the highs of the `n` bars
on each side; a pivot low, a low strictly below the lows of the `n` bars on
each side. The last `n` bars cannot be pivots yet (their right side has not
printed). `n` is `cfg(pivot.n)`. Pivots serve structure (the micro-Range's
counter-pivots, `recent_higher_low`, trendlines), never triggers. Pure.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from decimal import Decimal
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict

from cobalt.taxonomy.tunables import TunableRow

from .bars import WorkingBar

TUNABLE_KEYS = ("pivot.n",)


class Pivot(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    side: Literal["high", "low"]
    index: int
    ts: AwareDatetime
    price: Decimal


class PivotObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    n: int
    highs: tuple[Pivot, ...]
    lows: tuple[Pivot, ...]


def pivot_n(rows: Mapping[str, TunableRow]) -> int | None:
    row = rows["pivot.n"]
    return None if row.value is None else int(row.value)


def pivots(bars: Sequence[WorkingBar], n: int) -> PivotObservation:
    if n <= 0:
        raise ValueError(f"pivot n must be positive, got {n}")
    highs, lows = [], []
    for i in range(n, len(bars) - n):
        around = [*bars[i - n:i], *bars[i + 1:i + 1 + n]]
        if all(bars[i].high > b.high for b in around):
            highs.append(Pivot(side="high", index=i, ts=bars[i].ts, price=bars[i].high))
        if all(bars[i].low < b.low for b in around):
            lows.append(Pivot(side="low", index=i, ts=bars[i].ts, price=bars[i].low))
    return PivotObservation(n=n, highs=tuple(highs), lows=tuple(lows))


__all__ = ["Pivot", "PivotObservation", "TUNABLE_KEYS", "pivot_n", "pivots"]
