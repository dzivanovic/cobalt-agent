# `src/cobalt/radar/anatomy/structure.py`

## What it does
Structural references for a formed card: the tracked extreme, the `bar_break` trigger price and the structural stop. Every intermediate is kept so the numbers replay (L57).

## Key functions/classes
- `tracked_extreme(run, direction) -> TrackedExtreme` is the run's highest high (up) or lowest low (down). On a tie it takes the LATEST bar holding it. This serves `snapback_candle` / `turn_low`.
- `bar_break_trigger(bars, bars_cleared, trade_direction) -> TriggerLevel` is the price that clears ALL of the last `n` completed bars: the max high for a long, the min low for a short. Every bar in that window must be complete.
- `structural_stop(extreme, trade_direction, buffer) -> StructuralStop` works in three steps. (1) raw = extreme ± buffer, beyond the structure. (2) Round to the cent AWAY from price. (3) Stop-nudge check-and-move (§0 A.17): a stop landing on x.x0 moves 1¢ toward the structure, or 1¢ further away if that would reach the extreme. `nudged` records which happened.

## Gotchas
`buffer` is `cfg(stop.buffer)`, resolved by the caller and never a literal here. The nudge is a move, never an extra cent added on top.
