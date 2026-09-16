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


def detect_extension(run: Sequence[WorkingBar], params: ExtensionParams) -> ExtensionObservation:
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
        direction: Literal["up", "down"] | None = "up"
    elif last_close < session_open:
        direction = "down"
    else:
        direction = None

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
    if distance is not None and distance >= params.path_b_atr:
        return ExtensionObservation(
            instantiated=None, state=None, path="B_only",
            unavailable="catalyst_ref_unknown", **base,
        )
    return ExtensionObservation(instantiated=False, state="none", **base)


__all__ = ["ExtensionObservation", "ExtensionParams", "TUNABLE_KEYS", "detect_extension"]
