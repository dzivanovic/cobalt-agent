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

from decimal import Decimal
from typing import Any, Callable, Literal, Protocol

from pydantic import BaseModel, ConfigDict, Field

from cobalt.taxonomy.trade_def import StructuralRef

from ..anatomy.structure import StructuralStop, TrackedExtreme, structural_stop, tracked_extreme


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


#: §3.6 refs -> the resolver of the extreme they name.
STRUCTURAL_REFS: dict[StructuralRef, Callable[[Any], TrackedExtreme]] = {
    StructuralRef.SNAPBACK_CANDLE: _tracked,
    StructuralRef.TURN_LOW: _tracked,
}


class StopResolver(Protocol):
    kind: str

    def serves(self, placement) -> bool: ...

    def resolve(self, frame, placement, value: Callable[[Any], Any]) -> StopOutcome: ...


class StructuralExtreme:
    kind = "structural_extreme"

    def serves(self, placement) -> bool:
        return getattr(placement, "ref", None) in STRUCTURAL_REFS

    def resolve(self, frame, placement, value: Callable[[Any], Any]) -> StopOutcome:
        extreme = STRUCTURAL_REFS[placement.ref](frame)
        buffer = Decimal(str(value(placement.buffer.cents.value)))
        stop = structural_stop(extreme.price, "long", buffer)
        return StopOutcome(
            price=stop.price, placement=self.kind, ref=placement.ref.value,
            inputs={"buffer": str(buffer)}, why=f"beyond the {placement.ref.value} extreme",
            structural=stop, extreme=extreme,
        )


STOPS: dict[str, StopResolver] = {
    "structural_extreme": StructuralExtreme(),
}


def stop_resolver(placement) -> StopResolver | None:
    resolver = STOPS.get(placement.type)
    if resolver is None or not resolver.serves(placement):
        return None
    return resolver


__all__ = ["STOPS", "STRUCTURAL_REFS", "StopOutcome", "StopResolver", "StructuralExtreme", "stop_resolver"]
