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

from ..anatomy.indicators import InsufficientBars
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


class RangeBreak:
    """`range_break {ref: Range(micro).bound | .top}` (FINAL §2.2; STEP-4): the
    trade-side bound of the live micro-Range, intrabar. In the frame's
    coordinates the long-side text's trade-side bound is the `top` (`bound`
    = long → `top`, taxonomy §3.0); on the mirrored frame that is the real
    base. The level carries the top's touch bars; `bars_cleared` is 0 — the
    trigger is a level, not a count of bars cleared."""

    kind = "range_break"
    REFS = frozenset({"Range(micro).bound", "Range(micro).top"})

    def serves(self, params: dict[str, Any]) -> bool:
        return params.get("ref") in self.REFS

    def resolve(self, frame, trigger_def, value: Callable[[Any], Any]) -> TriggerOutcome:
        obs = frame.objects["Range(micro)"]
        r = None if isinstance(obs, str) else obs.range
        if r is None:
            raise InsufficientBars("range_break trigger (no instantiated micro-Range)", 1, 0)
        level = TriggerLevel(trade_direction="long", price=r.top, bars_cleared=0, bar_ts=r.top_touch_ts)
        return TriggerOutcome(
            state="armed", price=r.top, ref_bar_ts=r.top_touch_ts[-1], kind=self.kind,
            inputs={"ref": trigger_def.params["ref"], "range_start": r.start_ts.isoformat()},
            why="break of the micro-Range bound", level=level,
        )


class IndicatorCross:
    """`indicator_cross {a, b, direction}` (FINAL §2.2; STEP-5): the latest
    closed working bar where indicator `a` crossed `b` in `direction`, in the
    frame's coordinates (the long-side text's `a_crosses_above_b` on the
    mirrored frame is the real cross below). It stamps `cross_point`: the cross
    bar and its close, which is the entry the card arms at. No cross yet →
    `InsufficientBars` (the stage reports `not_formed`)."""

    kind = "indicator_cross"
    INDICATORS = frozenset({"EMA9", "EMA21", "VWAP"})
    DIRECTIONS = frozenset({"a_crosses_above_b", "a_crosses_below_b"})

    def serves(self, params: dict[str, Any]) -> bool:
        return (params.get("a") in self.INDICATORS and params.get("b") in self.INDICATORS
                and params.get("a") != params.get("b") and params.get("direction") in self.DIRECTIONS)

    def resolve(self, frame, trigger_def, value: Callable[[Any], Any]) -> TriggerOutcome:
        p = trigger_def.params
        i = frame.objects["cross_index"](p["a"], p["b"], p["direction"])
        if i is None:
            raise InsufficientBars(f"indicator_cross ({p['a']} has not crossed {p['b']})", 1, 0)
        bar = frame.run[i]
        level = TriggerLevel(trade_direction="long", price=bar.close, bars_cleared=0, bar_ts=(bar.ts,))
        return TriggerOutcome(
            state="armed", price=bar.close, ref_bar_ts=bar.ts, kind=self.kind,
            inputs={"a": p["a"], "b": p["b"], "direction": p["direction"], "cross_point": bar.ts.isoformat()},
            why=f"{p['a']} cross of {p['b']}", level=level,
        )


TRIGGERS: dict[TriggerType, TriggerResolver] = {
    TriggerType.BAR_BREAK: BarBreak(),
    TriggerType.RANGE_BREAK: RangeBreak(),
    TriggerType.INDICATOR_CROSS: IndicatorCross(),
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


__all__ = ["BarBreak", "IndicatorCross", "RangeBreak", "TRIGGERS", "TriggerOutcome", "TriggerResolver",
           "trigger_resolver"]
