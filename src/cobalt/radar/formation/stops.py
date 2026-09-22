"""STOPS and STRUCTURAL_REFS (FINAL §2.3; setups one build STEP-2).

`STOPS`: `stop.placement.type` -> resolver; `STRUCTURAL_REFS`: the §3.6
structural reference -> the resolver of its extreme. Resolved on a FRAME,
in the frame's coordinates, for the def's long-side text; the stage
un-mirrors (`StopOutcome.unmirrored`). The buffer and the stop-nudge law
are `structure.structural_stop`, unchanged. The geometry guard (FINAL §9
point (5)) is written ONCE, in the formation stage (`evaluate.py`
`stop_on_protective_side`), so every placement here inherits it.

`structural_extreme` on `snapback_candle` / `turn_low` is today's tracked
extreme (`structure.tracked_extreme`), re-registered with byte-identical
output.
"""

from __future__ import annotations

from decimal import ROUND_FLOOR, Decimal, localcontext
from typing import Any, Callable, Literal, Protocol

from pydantic import BaseModel, ConfigDict, Field

from cobalt.taxonomy.trade_def import StructuralRef

from ..anatomy.indicators import PRECISION, InsufficientBars
from ..anatomy.pivots import pivot_n, pivots
from ..anatomy.structure import CENT, StructuralStop, TrackedExtreme, structural_stop, tracked_extreme


class StopOutcome(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    price: Decimal
    placement: str
    ref: str | None = None
    inputs: dict[str, Any] = Field(default_factory=dict)
    why: str
    #: The buffered, cent-rounded, nudged stop (§0 B1 A.17).
    structural: StructuralStop
    #: The structure the stop protects against, when it is an extreme.
    extreme: TrackedExtreme | None = None

    def unmirrored(self, direction: Literal["long", "short"]) -> StopOutcome:
        if direction == "long":
            return self
        s = self.structural
        structural = s.model_copy(update={
            "trade_direction": "short", "extreme": -s.extreme, "raw": -s.raw, "rounded": -s.rounded,
            "price": -s.price,
        })
        extreme = None if self.extreme is None else self.extreme.model_copy(update={
            "side": "high" if self.extreme.side == "low" else "low", "price": -self.extreme.price,
        })
        return self.model_copy(update={"price": -self.price, "structural": structural, "extreme": extreme})


def _tracked(frame) -> TrackedExtreme:
    """The current tracked extreme of the move the trade opposes: in the
    frame's coordinates a long-side def opposes a DOWN run, so its low."""
    return tracked_extreme(frame.run, frame.extension.direction)


def _range_base(frame) -> TrackedExtreme:
    """`consolidation_low` / `range_base` (= `Range.base`, taxonomy §3.6): the
    live micro-Range's base, at the latest bar holding it (STEP-4)."""
    obs = frame.objects["Range(micro)"]
    r = None if isinstance(obs, str) else obs.range
    if r is None:
        raise InsufficientBars("consolidation_low (no instantiated micro-Range)", 1, 0)
    return TrackedExtreme(side="low", price=r.base, bar_ts=r.base_bar_ts)


def _recent_higher_low(frame) -> TrackedExtreme:
    """`recent_higher_low` (taxonomy §3.6, A.7; STEP-5): the micro-Range's
    latest counter-pivot on the trade-opposite side — for the long-side text,
    the latest pivot low (`cfg(pivot.n)`) inside the live micro-Range."""
    obs = frame.objects["Range(micro)"]
    r = None if isinstance(obs, str) else obs.range
    if r is None:
        raise InsufficientBars("recent_higher_low (no instantiated micro-Range)", 1, 0)
    n = pivot_n(frame.objects["tunables"])
    if n is None:
        raise InsufficientBars("recent_higher_low (pivot.n unset)", 1, 0)
    window = [b for b in frame.run if b.ts >= r.start_ts]
    lows = pivots(window, n).lows
    if not lows:
        raise InsufficientBars("recent_higher_low (no pivot low inside the micro-Range)", 1, 0)
    return TrackedExtreme(side="low", price=lows[-1].price, bar_ts=lows[-1].ts)


#: §3.6 refs -> the resolver of the extreme they name.
STRUCTURAL_REFS: dict[StructuralRef, Callable[[Any], TrackedExtreme]] = {
    StructuralRef.SNAPBACK_CANDLE: _tracked,
    StructuralRef.TURN_LOW: _tracked,
    StructuralRef.CONSOLIDATION_LOW: _range_base,
    StructuralRef.RANGE_BASE: _range_base,
    StructuralRef.RECENT_HIGHER_LOW: _recent_higher_low,
}


class StopResolver(Protocol):
    kind: str

    def serves(self, placement) -> bool: ...

    def resolve(self, frame, placement, value: Callable[[Any], Any], **context) -> StopOutcome: ...


class StructuralExtreme:
    kind = "structural_extreme"

    def serves(self, placement) -> bool:
        return getattr(placement, "ref", None) in STRUCTURAL_REFS

    def resolve(self, frame, placement, value: Callable[[Any], Any], **_context) -> StopOutcome:
        extreme = STRUCTURAL_REFS[placement.ref](frame)
        buffer = Decimal(str(value(placement.buffer.cents.value)))
        stop = structural_stop(extreme.price, "long", buffer)
        return StopOutcome(
            price=stop.price, placement=self.kind, ref=placement.ref.value,
            inputs={"buffer": str(buffer)}, why=f"beyond the {placement.ref.value} extreme",
            structural=stop, extreme=extreme,
        )


def measured_fraction_price(anchor_a: Decimal, anchor_b: Decimal, fraction: Decimal) -> Decimal:
    """`anchor_a − fraction × (anchor_a − anchor_b)`, at the indicator module's
    precision, floored to the cent (away from price for the long-side text)."""
    with localcontext() as ctx:
        ctx.prec = PRECISION
        raw = anchor_a - fraction * (anchor_a - anchor_b)
    return raw.quantize(CENT, rounding=ROUND_FLOOR)


class MeasuredFraction:
    """`measured_fraction {anchor_a, anchor_b, fraction}` (FINAL §2.3; STEP-5):
    `anchor_a − fraction × (anchor_a − anchor_b)`; the anchors resolve through
    `STRUCTURAL_REFS`, and `entry` is the trigger's price. No buffer and no
    ten-cent nudge: the nudge law moves a stop off a round price TOWARD a
    structure, and a measured stop has none (§0 B1 A.17 is written for
    structural extremes)."""

    kind = "measured_fraction"

    @staticmethod
    def _anchor(name: str):
        if name == "entry":
            return "entry"
        try:
            ref = StructuralRef(name)
        except ValueError:
            return None
        return ref if ref in STRUCTURAL_REFS else None

    def serves(self, placement) -> bool:
        return all(self._anchor(getattr(placement, a, "")) is not None for a in ("anchor_a", "anchor_b"))

    def _price(self, frame, name: str, trigger) -> tuple[Decimal, TrackedExtreme | None]:
        anchor = self._anchor(name)
        if anchor == "entry":
            if trigger is None:
                raise InsufficientBars("measured_fraction (no entry: the trigger has no price)", 1, 0)
            return trigger.price, None
        extreme = STRUCTURAL_REFS[anchor](frame)
        return extreme.price, extreme

    def resolve(self, frame, placement, value: Callable[[Any], Any], *, trigger=None, **_context) -> StopOutcome:
        a, ext_a = self._price(frame, placement.anchor_a, trigger)
        b, ext_b = self._price(frame, placement.anchor_b, trigger)
        fraction = Decimal(str(placement.fraction))
        price = measured_fraction_price(a, b, fraction)
        with localcontext() as ctx:
            ctx.prec = PRECISION
            raw = a - fraction * (a - b)
        stop = StructuralStop(trade_direction="long", extreme=b, buffer=Decimal(0), raw=raw, rounded=price,
                              price=price, nudged="none")
        return StopOutcome(
            price=price, placement=self.kind, ref=placement.anchor_b,
            inputs={"anchor_a": placement.anchor_a, "anchor_b": placement.anchor_b, "fraction": str(fraction),
                    "a": str(a), "b": str(b)},
            why=f"{fraction} of the way from {placement.anchor_a} to {placement.anchor_b}",
            structural=stop, extreme=ext_b or ext_a,
        )


class IndicatorStop:
    """`indicator {indicator, buffer, snapshot}` (taxonomy A.2; STEP-6): the
    indicator's value at the ENTRY bar (`snapshot: at_entry`, the ruled
    default), less the buffer, under `structure.structural_stop`'s rounding and
    nudge (the indicator is the structure). `live` is not served (named)."""

    kind = "indicator"
    INDICATORS = frozenset({"EMA9", "EMA21", "VWAP"})

    def serves(self, placement) -> bool:
        indicator = getattr(placement, "indicator", None)
        snapshot = getattr(placement, "snapshot", None)
        return (getattr(indicator, "value", None) in self.INDICATORS
                and getattr(snapshot, "value", None) == "at_entry")

    def resolve(self, frame, placement, value: Callable[[Any], Any], *, trigger=None, **_context) -> StopOutcome:
        name = placement.indicator.value
        if trigger is None or trigger.ref_bar_ts is None:
            raise InsufficientBars(f"indicator stop ({name}: no entry bar)", 1, 0)
        at = [i for i, b in enumerate(frame.run) if b.ts == trigger.ref_bar_ts]
        values = frame.objects["series"](name)
        if not at or values[at[-1]] is None:
            raise InsufficientBars(f"indicator stop ({name} has no value at entry)", 1, 0)
        level = values[at[-1]]
        buffer = Decimal(str(value(placement.buffer.cents.value)))
        stop = structural_stop(level, "long", buffer)
        extreme = TrackedExtreme(side="low", price=level, bar_ts=trigger.ref_bar_ts)
        return StopOutcome(
            price=stop.price, placement=self.kind, ref=name, inputs={"buffer": str(buffer), "snapshot": "at_entry"},
            why=f"beyond the {name} at entry", structural=stop, extreme=extreme,
        )


STOPS: dict[str, StopResolver] = {
    "structural_extreme": StructuralExtreme(),
    "measured_fraction": MeasuredFraction(),
    "indicator": IndicatorStop(),
}


def stop_resolver(placement) -> StopResolver | None:
    resolver = STOPS.get(placement.type)
    if resolver is None or not resolver.serves(placement):
        return None
    return resolver


__all__ = [
    "MeasuredFraction", "STOPS", "STRUCTURAL_REFS", "StopOutcome", "StopResolver", "StructuralExtreme",
    "measured_fraction_price", "stop_resolver",
]
