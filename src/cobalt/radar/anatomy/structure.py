"""Structural references, the bar_break trigger and the structural stop.

TRACKED EXTREME (`snapback_candle` / `turn_low`, TAXONOMY v0.7 §3.6): the
current tracked extreme of the move — the run's highest high for an up
extension, lowest low for a down one; on a tie the LATEST bar holding it
(the most recent test of the extreme is the one a snapback reverses from).

BAR_BREAK TRIGGER (§10.2, `{bars_cleared: n, both_must_be_cleared}`):
the price that clears ALL of the last `n` completed working bars — the
max high for a long, the min low for a short. Every one of the `n` bars
must be complete.

STRUCTURAL STOP (§10.2 `structural_extreme` + stop-nudge law, §0 B1 A.17):
  1. raw = extreme + buffer (short, stop above) / extreme − buffer (long);
     buffer = `cfg(stop.buffer)` (0.02);
  2. rounded to the cent AWAY from price (ceil for a short, floor for a
     long) so a sub-cent extreme never yields a stop inside the buffer;
  3. check-and-move, not additive: if the cent lands on x.x0 (a round
     dollar included) it moves 1¢ back TOWARD the structure, keeping the
     stop 1–2¢ beyond it; if that would reach the extreme itself, it
     moves 1¢ further away instead.
The observation keeps every intermediate so the stop replays (L57).
"""

from __future__ import annotations

from collections.abc import Sequence
from decimal import ROUND_CEILING, ROUND_FLOOR, Decimal
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict

from .bars import WorkingBar, require_complete
from .indicators import InsufficientBars

CENT = Decimal("0.01")

TradeDirection = Literal["long", "short"]


class TrackedExtreme(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    side: Literal["high", "low"]
    price: Decimal
    bar_ts: AwareDatetime


class TriggerLevel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    trade_direction: TradeDirection
    price: Decimal
    bars_cleared: int
    bar_ts: tuple[AwareDatetime, ...]


class StructuralStop(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    trade_direction: TradeDirection
    extreme: Decimal
    buffer: Decimal
    raw: Decimal
    rounded: Decimal
    price: Decimal
    nudged: Literal["none", "toward_structure", "away_from_structure"]


def tracked_extreme(run: Sequence[WorkingBar], extension_direction: Literal["up", "down"]) -> TrackedExtreme:
    if not run:
        raise InsufficientBars("tracked extreme", 1, 0)
    if extension_direction == "up":
        price = max(bar.high for bar in run)
        bar = [b for b in run if b.high == price][-1]
        return TrackedExtreme(side="high", price=price, bar_ts=bar.ts)
    price = min(bar.low for bar in run)
    bar = [b for b in run if b.low == price][-1]
    return TrackedExtreme(side="low", price=price, bar_ts=bar.ts)


def bar_break_trigger(bars: Sequence[WorkingBar], bars_cleared: int, trade_direction: TradeDirection) -> TriggerLevel:
    if bars_cleared <= 0:
        raise ValueError(f"bars_cleared must be positive, got {bars_cleared}")
    if len(bars) < bars_cleared:
        raise InsufficientBars("bar_break trigger", bars_cleared, len(bars))
    window = list(bars)[-bars_cleared:]
    require_complete(window)
    price = max(b.high for b in window) if trade_direction == "long" else min(b.low for b in window)
    return TriggerLevel(
        trade_direction=trade_direction, price=price, bars_cleared=bars_cleared,
        bar_ts=tuple(b.ts for b in window),
    )


def _on_ten_cent_grid(price: Decimal) -> bool:
    return (price / CENT) % 10 == 0


def structural_stop(extreme: Decimal, trade_direction: TradeDirection, buffer: Decimal) -> StructuralStop:
    if buffer <= 0:
        raise ValueError(f"stop buffer must be positive, got {buffer}")
    away = Decimal(1) if trade_direction == "short" else Decimal(-1)
    raw = extreme + away * buffer
    rounded = raw.quantize(CENT, rounding=ROUND_CEILING if trade_direction == "short" else ROUND_FLOOR)
    price, nudged = rounded, "none"
    if _on_ten_cent_grid(rounded):
        toward = rounded - away * CENT
        if (toward - extreme) * away > 0:
            price, nudged = toward, "toward_structure"
        else:
            price, nudged = rounded + away * CENT, "away_from_structure"
    return StructuralStop(
        trade_direction=trade_direction, extreme=extreme, buffer=buffer,
        raw=raw, rounded=rounded, price=price, nudged=nudged,
    )


__all__ = [
    "StructuralStop", "TrackedExtreme", "TradeDirection", "TriggerLevel",
    "bar_break_trigger", "structural_stop", "tracked_extreme",
]
