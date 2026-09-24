"""RangeBreak(level) — the break lifecycle of a level, its retest, and the
break → retest → turn sequence (taxonomy v0.7 §3.4 :104, §10.2; FINAL §3 D6;
setups one build STEP-8).

Taxonomy: "Lifecycle `forming → break_attempt → accepted | failed_trap`;
`retest` event; promotion default `close_through`; `failed_trap` = close back
inside within `cfg(range_break.failed_trap_bars)`."

THE CONSTRUCTION, in the frame's coordinates (the long-side text breaks UP
through a level L; the mirrored frame gives the other side). Pure.

* A level is broken inside the session only: the run's first bar must open at
  or under L (a gap above it is not a break).
* `forming`: no bar has traded above L; `break_attempt`: a bar traded above it,
  none closed above it; `accepted`: a bar CLOSED above it (the promotion,
  `close_through`); `failed_trap`: after that close, a close back under L
  within `failed_trap_bars` bars (`A-19`).
* `event(retest)`: after the accepting close, the first bar whose low comes
  back within `retest_tolerance_atr` × ATR of L (`A-20`) and closes above L.
* The sequence (the break-retest-turn trigger steps): the break (the accepting
  close), the retest, then the TURN — the first bar after the retest that
  closes above the prior bar's high. The turn bar is the trigger bar; its low
  is the `turn_candle` ref (`A-23`).
* `Range(prior)` (`A-21`): from the session's lowest low before the break up
  to L — "price inside Range(prior)" = back under the broken level.
* `event(stop_hit)` (`A-22`): computed from bars, never read from the card
  ledger — a completed sequence whose stop (the turn candle's low less the
  buffer) a LATER bar's low touched.

The level set is the frame's (`A-17`: PMH, PDH). `choose` picks the level
whose break is the latest; with none broken, the nearest level above.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict

from cobalt.taxonomy.tunables import TunableRow

from .bars import WorkingBar

TUNABLE_KEYS = ("range_break.failed_trap_bars", "range_break.retest_tolerance_atr")
PRIOR_RANGE_CONVENTION = "range_prior.rule"
STOP_HIT_CONVENTION = "event.stop_hit.source"
TURN_CANDLE_CONVENTION = "turn_candle.rule"

State = Literal["forming", "break_attempt", "accepted", "failed_trap"]


class RangeBreakParams(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    failed_trap_bars: int
    retest_tolerance_atr: Decimal


def range_break_params(rows: Mapping[str, TunableRow]) -> tuple[RangeBreakParams | None, str | None]:
    for key in TUNABLE_KEYS:
        if rows[key].value is None:
            return None, f"{key}_unset"
    return RangeBreakParams(failed_trap_bars=int(rows["range_break.failed_trap_bars"].value),
                            retest_tolerance_atr=Decimal(str(rows["range_break.retest_tolerance_atr"].value))), None


class RangeBreakObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    level: Decimal
    state: State
    attempt_index: int | None = None
    accept_index: int | None = None
    trap_index: int | None = None
    retest_index: int | None = None
    turn_index: int | None = None
    #: `Range(prior)`'s floor: the lowest low before the accepting close.
    prior_low: Decimal | None = None


def range_break(run: Sequence[WorkingBar], level: Decimal, params: RangeBreakParams, *,
                atr: Decimal) -> RangeBreakObservation:
    attempt = next((i for i, b in enumerate(run) if b.high > level), None)
    accept = next((i for i, b in enumerate(run) if b.close > level), None)
    if accept is None:
        return RangeBreakObservation(level=level, state="break_attempt" if attempt is not None else "forming",
                                     attempt_index=attempt)
    prior_low = min(b.low for b in run[:accept]) if accept > 0 else run[0].low
    window = run[accept + 1:accept + 1 + params.failed_trap_bars]
    trap = next((accept + 1 + k for k, b in enumerate(window) if b.close < level), None)
    tol = params.retest_tolerance_atr * atr
    retest = next((i for i in range(accept + 1, len(run))
                   if run[i].low <= level + tol and run[i].close > level), None)
    turn = None
    if retest is not None:
        turn = next((i for i in range(retest + 1, len(run)) if run[i].close > run[i - 1].high), None)
    return RangeBreakObservation(level=level, state="failed_trap" if trap is not None else "accepted",
                                 attempt_index=attempt, accept_index=accept, trap_index=trap,
                                 retest_index=retest, turn_index=turn, prior_low=prior_low)


def choose(run: Sequence[WorkingBar], levels: Sequence[Decimal], params: RangeBreakParams, *,
           atr: Decimal) -> RangeBreakObservation | None:
    """The RangeBreak of the level set: the level broken latest; none broken →
    the nearest level above the run's open."""
    if not run:
        return None
    eligible = [lv for lv in levels if run[0].open <= lv]
    if not eligible:
        return None
    observed = [range_break(run, lv, params, atr=atr) for lv in eligible]
    broken = [o for o in observed if o.accept_index is not None or o.attempt_index is not None]
    if broken:
        return max(broken, key=lambda o: (o.accept_index if o.accept_index is not None else -1,
                                          o.attempt_index if o.attempt_index is not None else -1))
    return min(observed, key=lambda o: o.level)


__all__ = [
    "PRIOR_RANGE_CONVENTION", "RangeBreakObservation", "RangeBreakParams", "STOP_HIT_CONVENTION",
    "TUNABLE_KEYS", "TURN_CANDLE_CONVENTION", "choose", "range_break", "range_break_params",
]
