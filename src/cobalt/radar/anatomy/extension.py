"""Extension — intraday instantiation (TAXONOMY v0.7 §3.2; R4).

Two paths are ruled. S2 lands cards on path A only:

(A) culminating bar character — a working bar whose volume is at least
    the volume band threshold (mean + k·sigma of the `n` bars before it,
    `indicators.volume_band`) AND whose body is strictly wider than every
    earlier body of the run, moving in the run's direction.
(B) distance — |last close − session open| ≥ `path_b_atr` × ATR(working
    TF, 14) with `catalyst_ref: null`. The catalyst is unknown in S2
    (R4), so a B-only formation is reported `B_only` with
    `unavailable="catalyst_ref_unknown"`: logged by the dry-run, never a
    card, never "not instantiated" either.

THE RUN is the bars handed in, from the leg base (session open) to the
last closed working bar; its direction is the sign of last close − open.
The latest qualifying path-A bar is the culmination. `leg_count` = legs
in the run direction (`leg.legs`). Every bar in the run must be complete
(`bars.require_complete`); a gap anywhere makes the observation
unavailable, never partially computed.

Thresholds are tunables, not literals (L52-a): `extension.path_a_volume_ma_bars`
(n), `extension.path_a_volume_sigma` (k), `extension.path_b_atr`.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from decimal import Decimal, localcontext
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from cobalt.taxonomy.tunables import TunableRow

from .bars import IncompleteBucket, WorkingBar, require_complete
from .indicators import ATR_PERIOD, PRECISION, AtrObservation, VolumeBand, volume_band, wilder_atr
from .leg import legs
from .structure import tracked_extreme

TUNABLE_KEYS = (
    "extension.path_a_volume_ma_bars",
    "extension.path_a_volume_sigma",
    "extension.path_b_atr",
)


class ExtensionParams(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    volume_ma_bars: int = Field(gt=0)
    volume_sigma: Decimal = Field(gt=0)
    path_b_atr: Decimal = Field(gt=0)

    @classmethod
    def from_tunables(cls, rows: Mapping[str, TunableRow]) -> ExtensionParams:
        missing = [key for key in TUNABLE_KEYS if key not in rows or rows[key].value is None]
        if missing:
            raise KeyError(f"extension tunables missing or unmeasured: {missing}")
        return cls(
            volume_ma_bars=int(rows["extension.path_a_volume_ma_bars"].value),
            volume_sigma=Decimal(str(rows["extension.path_a_volume_sigma"].value)),
            path_b_atr=Decimal(str(rows["extension.path_b_atr"].value)),
        )


class ExtensionObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    instantiated: bool | None
    state: Literal["culminating", "none"] | None
    path: Literal["A", "B_only"] | None = None
    direction: Literal["up", "down"] | None = None
    leg_count: int | None = None
    session_open: Decimal | None = None
    last_close: Decimal | None = None
    culminating_bar_ts: AwareDatetime | None = None
    culminating_volume: int | None = None
    culminating_body: Decimal | None = None
    widest_prior_body: Decimal | None = None
    band: VolumeBand | None = None
    atr: AtrObservation | None = None
    distance_from_open_atr: Decimal | None = None
    params: ExtensionParams
    unavailable: Literal["insufficient_bars", "incomplete_bucket", "catalyst_ref_unknown"] | None = None


def detect_extension(
    run: Sequence[WorkingBar], params: ExtensionParams, *, direction: Literal["up", "down"] | None = None,
) -> ExtensionObservation:
    """`direction` None = the run's sign (last close − session open), today's
    rule. A given `direction` (fix r3 F1, R47) is the frame's side binding:
    the Extension of that direction is read whatever the run's sign, and
    path B counts only a distance moved in that direction."""
    base = dict(params=params)
    if not run:
        return ExtensionObservation(instantiated=None, state=None, unavailable="insufficient_bars", **base)
    try:
        require_complete(run)
    except IncompleteBucket:
        return ExtensionObservation(instantiated=None, state=None, unavailable="incomplete_bucket", **base)

    session_open, last_close = run[0].open, run[-1].close
    base.update(session_open=session_open, last_close=last_close)
    if last_close > session_open:
        run_sign: Literal["up", "down"] | None = "up"
    elif last_close < session_open:
        run_sign = "down"
    else:
        run_sign = None
    if direction is None:
        direction = run_sign

    n = params.volume_ma_bars
    if len(run) < max(n + 1, ATR_PERIOD):
        return ExtensionObservation(
            instantiated=None, state=None, direction=direction,
            unavailable="insufficient_bars", **base,
        )

    atr = wilder_atr(run, ATR_PERIOD)
    with localcontext() as ctx:
        ctx.prec = PRECISION
        distance = abs(last_close - session_open) / atr.value if atr.value > 0 else None
    base.update(atr=atr, distance_from_open_atr=distance, direction=direction)

    if direction is None:
        return ExtensionObservation(instantiated=False, state="none", leg_count=0, **base)
    leg_count = sum(1 for leg in legs(run) if leg.direction == direction)
    base.update(leg_count=leg_count)

    culmination: tuple[WorkingBar, VolumeBand, Decimal] | None = None
    for i in range(n, len(run)):
        bar = run[i]
        if bar.direction != direction:
            continue
        band = volume_band(run[i - n:i], n, params.volume_sigma)
        widest_prior = max(prior.body for prior in run[:i])
        if bar.volume >= band.threshold and bar.body > widest_prior:
            culmination = (bar, band, widest_prior)

    if culmination is not None:
        bar, band, widest_prior = culmination
        return ExtensionObservation(
            instantiated=True, state="culminating", path="A",
            culminating_bar_ts=bar.ts, culminating_volume=bar.volume,
            culminating_body=bar.body, widest_prior_body=widest_prior, band=band, **base,
        )
    if distance is not None and distance >= params.path_b_atr and direction == run_sign:
        return ExtensionObservation(
            instantiated=None, state=None, path="B_only",
            unavailable="catalyst_ref_unknown", **base,
        )
    return ExtensionObservation(instantiated=False, state="none", **base)


# ---------------------------------------------------------------------
# D4 — the lifecycle past the culmination (setups one build STEP-5)
# ---------------------------------------------------------------------
#
# FINAL §3 D4: the state domain grows past `culminating | none` —
# `reverting` from the snapback rule `A-08`, `backside` from ≥
# `cfg(extension.backside_hh_min)` HH and ≥ `cfg(extension.backside_hl_min)` HL
# above a rising EMA9 (taxonomy v0.7 §3.2). `building`, `extending`,
# `resuming` (v0.4 :32) have no rule in the FINAL and are NOT produced (E8
# names them). A SEPARATE function over `detect_extension`'s output:
# `ExtensionObservation` and its path A / B stay byte-identical.
#
# THE CONSTRUCTION, in the frame's coordinates for a run in direction d:
# * the TURN = the run's tracked extreme in d (`structure.tracked_extreme`:
#   the latest bar holding the lowest low of a down run) — `turn_low` / `turn`;
# * REVERTING starts at the first bar after the turn that moves against d and
#   clears the n preceding bars' extremes on its side (a down run: its high
#   above the highs of the n bars before it), n = `A-08`;
# * BACKSIDE, once reverting: ≥ hh_min higher highs (bars after the turn making
#   a new high since the turn) and ≥ hl_min higher lows (bars moving with d
#   whose low is above the previous swing low, the turn's low first), with the
#   last close above EMA9 and EMA9 rising (its slope over `slope_norm.bars`).
#   A down run's backside is an up recovery; the mirrored frame gives the other.

LIFECYCLE_KEYS = ("extension.snapback_bars_cleared", "extension.backside_hh_min", "extension.backside_hl_min")


class LifecycleParams(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    snapback_bars_cleared: int = Field(gt=0)
    backside_hh_min: int = Field(ge=0)
    backside_hl_min: int = Field(ge=0)


def lifecycle_params(rows: Mapping[str, TunableRow]) -> tuple[LifecycleParams | None, str | None]:
    for key in LIFECYCLE_KEYS:
        if rows[key].value is None:
            return None, f"{key}_unset"
    return LifecycleParams(
        snapback_bars_cleared=int(rows["extension.snapback_bars_cleared"].value),
        backside_hh_min=int(rows["extension.backside_hh_min"].value),
        backside_hl_min=int(rows["extension.backside_hl_min"].value),
    ), None


class LifecycleObservation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    state: Literal["culminating", "reverting", "backside", "none"] | None
    turn_ts: AwareDatetime | None = None
    turn_price: Decimal | None = None
    turn_index: int | None = None
    reverting_ts: AwareDatetime | None = None
    higher_highs: int = 0
    higher_lows: int = 0
    #: Why the state past `reverting` cannot be read (the EMA9 or its slope).
    unavailable: str | None = None


def extension_lifecycle(
    run: Sequence[WorkingBar], ext: ExtensionObservation, params: LifecycleParams, *,
    ema9: Sequence[Decimal | None], slope_bars: int | None,
) -> LifecycleObservation:
    """The lifecycle state of a culminated Extension (else `ext.state`).
    `ema9[i]` is the EMA9 at run bar i (None before it has a value)."""
    if ext.state != "culminating" or ext.direction is None:
        return LifecycleObservation(state=ext.state)
    down = ext.direction == "down"
    turn = tracked_extreme(run, ext.direction)
    t = max(i for i, b in enumerate(run) if b.ts == turn.bar_ts)
    base = dict(turn_ts=turn.bar_ts, turn_price=turn.price, turn_index=t)
    n = params.snapback_bars_cleared
    reverting_at = None
    for j in range(max(t + 1, n), len(run)):
        prior = run[j - n:j]
        bar = run[j]
        if down and bar.direction == "up" and bar.high > max(b.high for b in prior):
            reverting_at = j
            break
        if not down and bar.direction == "down" and bar.low < min(b.low for b in prior):
            reverting_at = j
            break
    if reverting_at is None:
        return LifecycleObservation(state="culminating", **base)
    base["reverting_ts"] = run[reverting_at].ts
    after = run[t + 1:]
    hh = hl = 0
    best = run[t].high if down else run[t].low
    swing = run[t].low if down else run[t].high
    for b in after:
        if (b.high > best) if down else (b.low < best):
            hh += 1
            best = b.high if down else b.low
        moving_with_run = b.direction == ("down" if down else "up")
        if moving_with_run:
            if (b.low > swing) if down else (b.high < swing):
                hl += 1
            swing = b.low if down else b.high
    base.update(higher_highs=hh, higher_lows=hl)
    if hh < params.backside_hh_min or hl < params.backside_hl_min:
        return LifecycleObservation(state="reverting", **base)
    if slope_bars is None:
        return LifecycleObservation(state=None, unavailable="slope_norm.bars_unset", **base)
    now = ema9[-1] if ema9 else None
    then = ema9[-1 - slope_bars] if len(ema9) > slope_bars else None
    if now is None or then is None:
        return LifecycleObservation(state=None, unavailable="insufficient_seed", **base)
    rising = now > then if down else now < then
    above = run[-1].close > now if down else run[-1].close < now
    return LifecycleObservation(state="backside" if rising and above else "reverting", **base)


__all__ = [
    "ExtensionObservation", "ExtensionParams", "LIFECYCLE_KEYS", "LifecycleObservation", "LifecycleParams",
    "TUNABLE_KEYS", "detect_extension", "extension_lifecycle", "lifecycle_params",
]
