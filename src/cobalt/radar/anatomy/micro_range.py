"""Range(micro) — the intraday consolidation (TAXONOMY v0.7 §2.3, §3.0; FINAL
§3 D2; setups one build STEP-4).

Taxonomy: "Intraday consolidation = a Range instance at micro scale —
instantiation 2 touches per side (`cfg(range.micro.touches_per_side)`). No bar
count." Fields `duration`, `bound_type: flat | converging | channel` —
"diverging bounds = no Range" — `top` / `base` (`base` alias `range_base` /
`consolidation_low`), `bound` (the trade-side bound: long → `top`),
`wick_ratio`, `height`.

THE CONSTRUCTION (fixed here so a recompute cannot drift):

* candidates are the windows of the run that END at the last closed working
  bar; every bar of a window must be complete (a window never spans an
  incomplete bucket, and an incomplete LAST bar → `incomplete_bucket`);
* a window's `top` / `base` are its highest high / lowest low;
* a bar TOUCHES the top when its high is within `tol` of it, the base when its
  low is within `tol` — `tol = cfg(range.micro.touch_tolerance_atr) × ATR`
  (`A-03`; the ATR is the frame's `ATR(working_tf)`, seeded, [F-10]);
* a TOUCH is a maximal run of consecutive touching bars (two adjacent bars at
  the top are one touch);
* bound lines: the slope, per bar, from the first to the last touch of each
  bound; with `flat = cfg(range.micro.bound_flat_slope_atr) × ATR` (`A-04`):
  both |slopes| ≤ flat → `flat`; top slope − base slope > flat → `diverging`
  (no Range); base slope − top slope > flat → `converging`; else `channel`;
* the Range(micro) is the LONGEST candidate window with ≥ `touches_per_side`
  touches on each bound whose bounds are not diverging;
* `instantiated_ts` = the bar at which, reading the window forward, both
  bounds first reached `touches_per_side` touches (the formation's bar);
* `duration` = minutes from the window's first bar to the end of its last;
  `height = top − base`; `wick_ratio = Σ(range − |body|) / Σ range` over the
  window's bars (a zero sum → None).

Pure; prices are in the frame's coordinates (the mirrored frame gives the
short side's Range). A null key reads `<key>_unset`; no ATR reads
`insufficient_seed`.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from decimal import Decimal, localcontext
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from cobalt.taxonomy.tunables import TunableRow

from .bars import WorkingBar
from .indicators import PRECISION

TUNABLE_KEYS = (
    "range.micro.touches_per_side",
    "range.micro.touch_tolerance_atr",
    "range.micro.bound_flat_slope_atr",
)


class MicroRangeParams(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    touches_per_side: int = Field(gt=0)
    touch_tolerance_atr: Decimal = Field(ge=0)
    bound_flat_slope_atr: Decimal = Field(ge=0)


def range_params(rows: Mapping[str, TunableRow]) -> tuple[MicroRangeParams | None, str | None]:
    """The detector's params, or the first null key as `<key>_unset`. An
    absent row is a config error (KeyError, loud)."""
    for key in TUNABLE_KEYS:
        if rows[key].value is None:
            return None, f"{key}_unset"
    return MicroRangeParams(
        touches_per_side=int(rows["range.micro.touches_per_side"].value),
        touch_tolerance_atr=Decimal(str(rows["range.micro.touch_tolerance_atr"].value)),
        bound_flat_slope_atr=Decimal(str(rows["range.micro.bound_flat_slope_atr"].value)),
    ), None


class MicroRange(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    instantiated: bool
    start_ts: AwareDatetime
    instantiated_ts: AwareDatetime
    end_ts: AwareDatetime
    top: Decimal
    base: Decimal
    height: Decimal
    bound_type: Literal["flat", "converging", "channel"]
    duration_min: Decimal
    wick_ratio: Decimal | None
    touches_top: int
    touches_base: int
    top_touch_ts: tuple[AwareDatetime, ...]
    base_touch_ts: tuple[AwareDatetime, ...]
    #: The latest bar holding the base (the stop's structure).
    base_bar_ts: AwareDatetime


class MicroRangeObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    range: MicroRange | None = None
    unavailable: Literal["insufficient_seed", "insufficient_bars", "incomplete_bucket"] | None = None


def _touch_runs(flags: Sequence[bool]) -> list[int]:
    """The index of the first bar of each maximal run of True."""
    return [i for i, f in enumerate(flags) if f and (i == 0 or not flags[i - 1])]


def _slope(points: list[tuple[int, Decimal]]) -> Decimal:
    (i0, p0), (i1, p1) = points[0], points[-1]
    return Decimal(0) if i1 == i0 else (p1 - p0) / (i1 - i0)


def _window(bars: Sequence[WorkingBar], params: MicroRangeParams, atr: Decimal) -> MicroRange | None:
    with localcontext() as ctx:
        ctx.prec = PRECISION
        top, base = max(b.high for b in bars), min(b.low for b in bars)
        tol = params.touch_tolerance_atr * atr
        at_top = [top - b.high <= tol for b in bars]
        at_base = [b.low - base <= tol for b in bars]
        top_runs, base_runs = _touch_runs(at_top), _touch_runs(at_base)
        k = params.touches_per_side
        if len(top_runs) < k or len(base_runs) < k:
            return None
        flat = params.bound_flat_slope_atr * atr
        top_slope = _slope([(i, bars[i].high) for i, f in enumerate(at_top) if f])
        base_slope = _slope([(i, bars[i].low) for i, f in enumerate(at_base) if f])
        if top_slope - base_slope > flat:
            return None  # diverging bounds = no Range
        if abs(top_slope) <= flat and abs(base_slope) <= flat:
            bound_type = "flat"
        elif base_slope - top_slope > flat:
            bound_type = "converging"
        else:
            bound_type = "channel"
        spans = sum((b.high - b.low for b in bars), Decimal(0))
        wicks = sum((b.high - b.low - b.body for b in bars), Decimal(0))
        wick_ratio = wicks / spans if spans > 0 else None
        instantiated_at = max(top_runs[k - 1], base_runs[k - 1])
        duration = Decimal((bars[-1].end - bars[0].ts).total_seconds()) / 60
    return MicroRange(
        instantiated=True, start_ts=bars[0].ts, instantiated_ts=bars[instantiated_at].ts, end_ts=bars[-1].end,
        top=top, base=base, height=top - base, bound_type=bound_type, duration_min=duration,
        wick_ratio=wick_ratio, touches_top=len(top_runs), touches_base=len(base_runs),
        top_touch_ts=tuple(bars[i].ts for i in top_runs), base_touch_ts=tuple(bars[i].ts for i in base_runs),
        base_bar_ts=[b for b in bars if b.low == base][-1].ts,
    )


def detect_micro_range(
    run: Sequence[WorkingBar], params: MicroRangeParams, *, atr: Decimal | None
) -> MicroRangeObservation:
    if atr is None:
        return MicroRangeObservation(unavailable="insufficient_seed")
    if not run:
        return MicroRangeObservation(unavailable="insufficient_bars")
    if not run[-1].complete:
        return MicroRangeObservation(unavailable="incomplete_bucket")
    first = max((i + 1 for i, b in enumerate(run) if not b.complete), default=0)
    for start in range(first, len(run)):
        found = _window(run[start:], params, atr)
        if found is not None:
            return MicroRangeObservation(range=found)
    return MicroRangeObservation(range=None)


__all__ = [
    "MicroRange", "MicroRangeObservation", "MicroRangeParams", "TUNABLE_KEYS", "detect_micro_range",
    "range_params",
]
