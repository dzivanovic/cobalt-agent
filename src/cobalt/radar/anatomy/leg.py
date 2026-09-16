"""Leg = wave (TAXONOMY v0.7 §3.1): one directional move, terminated by
the first opposing bar.

Conventions (Astra R1-9), fixed here so a recompute cannot drift:

* bar direction: close > open = up, close < open = down, equal = flat;
* a flat (doji) bar never starts or ends a leg — it extends the current
  leg, and leading flats join the first directional leg;
* ONE opposing bar terminates the current leg (`terminated=True`) and
  starts the next; the last leg is open (`terminated=False`);
* the leg base is the first bar handed in. The evaluator hands in RTH
  bars from the session open (`extension.leg_base: session_open`,
  replay_pending) — this module does not pick the base.

Consolidation-terminated legs (micro-Range) are an S3 detector; S2 needs
only the Extension `leg_count`.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict
from decimal import Decimal

from .bars import WorkingBar


class LegObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    direction: Literal["up", "down"]
    start_ts: AwareDatetime
    end_ts: AwareDatetime
    bar_count: int
    terminated: bool
    high: Decimal
    low: Decimal


def legs(bars: Sequence[WorkingBar]) -> tuple[LegObservation, ...]:
    out: list[LegObservation] = []
    current: list[WorkingBar] = []
    direction: str | None = None

    def close(terminated: bool) -> None:
        out.append(
            LegObservation(
                direction=direction, start_ts=current[0].ts, end_ts=current[-1].ts,
                bar_count=len(current), terminated=terminated,
                high=max(b.high for b in current), low=min(b.low for b in current),
            )
        )

    for bar in bars:
        bar_dir = bar.direction
        if bar_dir == "flat" or direction is None or bar_dir == direction:
            current.append(bar)
            if direction is None and bar_dir != "flat":
                direction = bar_dir
            continue
        close(terminated=True)
        current, direction = [bar], bar_dir
    if current and direction is not None:
        close(terminated=False)
    return tuple(out)


__all__ = ["LegObservation", "legs"]
