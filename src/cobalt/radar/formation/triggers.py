"""TRIGGERS — `trigger.type` -> resolver (FINAL §2.2; setups one build STEP-2).

Each resolver declares `serves(params)` (the parameter shape it reads) and
resolves on a FRAME, in the frame's coordinates, for the def's long-side
text: on the mirrored frame "long" IS the short side (FINAL §2.1 [F-04]).
The stage un-mirrors the outcome before it reaches `Formation`
(`TriggerOutcome.unmirrored`).

`bar_break {bars_cleared}` is today's `structure.bar_break_trigger`,
re-registered with byte-identical output.
"""

from __future__ import annotations

from decimal import Decimal
from typing import Any, Callable, Literal, Protocol

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from cobalt.taxonomy.trade_def import TriggerType

from ..anatomy.structure import TriggerLevel, bar_break_trigger


class TriggerOutcome(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    state: Literal["armed", "fired", "unavailable"]
    price: Decimal | None
    ref_bar_ts: AwareDatetime | None
    kind: str
    inputs: dict[str, Any] = Field(default_factory=dict)
    why: str
    #: The bar-break level itself (the card's `trigger` evidence).
    level: TriggerLevel | None = None

    def unmirrored(self, direction: Literal["long", "short"]) -> TriggerOutcome:
        """This outcome in real-world coordinates for a formation on `direction`."""
        if direction == "long":
            return self
        level = None if self.level is None else self.level.model_copy(
            update={"trade_direction": "short", "price": -self.level.price})
        return self.model_copy(update={"price": None if self.price is None else -self.price, "level": level})


class TriggerResolver(Protocol):
    kind: str

    def serves(self, params: dict[str, Any]) -> bool: ...

    def resolve(self, frame, trigger_def, value: Callable[[Any], Any]) -> TriggerOutcome: ...


class BarBreak:
    """`bar_break {bars_cleared}`: the price that clears ALL of the last n
    completed working bars (`structure.bar_break_trigger`)."""

    kind = "bar_break"

    def serves(self, params: dict[str, Any]) -> bool:
        return "bars_cleared" in params

    def resolve(self, frame, trigger_def, value: Callable[[Any], Any]) -> TriggerOutcome:
        n = int(value(trigger_def.params["bars_cleared"]))
        level = bar_break_trigger(frame.run, n, "long")
        return TriggerOutcome(
            state="armed", price=level.price, ref_bar_ts=level.bar_ts[-1], kind=self.kind,
            inputs={"bars_cleared": n}, why=f"{n}-bar break", level=level,
        )


TRIGGERS: dict[TriggerType, TriggerResolver] = {
    TriggerType.BAR_BREAK: BarBreak(),
}


def trigger_resolver(trigger_def) -> TriggerResolver | None:
    """The resolver that serves this trigger, or None (named missing)."""
    try:
        resolver = TRIGGERS.get(TriggerType(trigger_def.type))
    except ValueError:
        return None
    if resolver is None or not resolver.serves(getattr(trigger_def, "params", {}) or {}):
        return None
    return resolver


__all__ = ["BarBreak", "TRIGGERS", "TriggerOutcome", "TriggerResolver", "trigger_resolver"]
