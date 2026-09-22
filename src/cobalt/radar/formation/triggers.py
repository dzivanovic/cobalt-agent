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


class IndicatorRejection:
    """`indicator_rejection {indicator, contact: touch | penetrate}` (taxonomy
    §10.2 A.4; STEP-6): "the bar that touches/penetrates the indicator and
    closes on the trade side IS trigger and entry" — `close_through` by
    definition. In the frame's coordinates: the LAST closed working bar whose
    low reached the indicator (`touch`: low ≤ it; `penetrate`: low < it) and
    whose close is above it. Its close is the entry. The last bar is not a
    rejection → `InsufficientBars` (`not_formed`); next-bar continuation is the
    human read (L11)."""

    kind = "indicator_rejection"
    INDICATORS = frozenset({"EMA9", "EMA21", "VWAP"})
    CONTACTS = frozenset({"touch", "penetrate"})

    def serves(self, params: dict[str, Any]) -> bool:
        contact = params.get("contact")
        contacts = set(contact) if isinstance(contact, (list, tuple)) else {contact}
        return params.get("indicator") in self.INDICATORS and bool(contacts) and contacts <= self.CONTACTS

    def resolve(self, frame, trigger_def, value: Callable[[Any], Any]) -> TriggerOutcome:
        p = trigger_def.params
        contact = p["contact"]
        contacts = set(contact) if isinstance(contact, (list, tuple)) else {contact}
        values = frame.objects["series"](p["indicator"])
        if not frame.run or values[-1] is None:
            raise InsufficientBars(f"indicator_rejection ({p['indicator']} has no value)", 1, 0)
        bar, level_now = frame.run[-1], values[-1]
        reached = ("touch" in contacts and bar.low <= level_now) or ("penetrate" in contacts and bar.low < level_now)
        if not (reached and bar.close > level_now):
            raise InsufficientBars(f"indicator_rejection (the last bar is no {p['indicator']} rejection)", 1, 0)
        level = TriggerLevel(trade_direction="long", price=bar.close, bars_cleared=0, bar_ts=(bar.ts,))
        return TriggerOutcome(
            state="armed", price=bar.close, ref_bar_ts=bar.ts, kind=self.kind,
            inputs={"indicator": p["indicator"], "contact": sorted(contacts), "indicator_at_bar": str(level_now)},
            why=f"{p['indicator']} rejection", level=level,
        )


class TrendlineBreak:
    """`trendline_break {ref: Level_ref(trendline), anchor_leg, pivots}` (FINAL
    §2.2, taxonomy §3.7; STEP-7), intrabar, in the frame's coordinates:

    * the FLAT case (taxonomy `:114`: "the pullback consolidated into a
      micro-Range is the same object with slope 0 — the break must be through
      the far bound"): a micro-Range instantiated after the anchor leg began →
      the trigger is its top;
    * otherwise the line through the pivot highs (`cfg(pivot.n)`) from the
      anchor leg's first bar to now — at least `pivots` of them, descending —
      its value extended to the last bar is the trigger.
    Neither → `InsufficientBars` (`not_formed`)."""

    kind = "trendline_break"
    ANCHORS = frozenset({"Leg(pullback)"})

    def serves(self, params: dict[str, Any]) -> bool:
        return params.get("ref") == "Level_ref(trendline)" and params.get("anchor_leg") in self.ANCHORS \
            and "pivots" in params

    def resolve(self, frame, trigger_def, value: Callable[[Any], Any]) -> TriggerOutcome:
        from ..anatomy.pivots import pivot_n, pivots

        p = trigger_def.params
        leg = frame.objects["pullback_roles"].pullback
        if leg is None:
            raise InsufficientBars("trendline_break (no pullback leg)", 1, 0)
        start = frame.objects["pullback_roles"].before.start_ts if frame.objects["pullback_roles"].before \
            else leg.start_ts
        obs = frame.objects["Range(micro)"]
        r = None if isinstance(obs, str) else obs.range
        if r is not None and r.start_ts >= leg.start_ts:
            level = TriggerLevel(trade_direction="long", price=r.top, bars_cleared=0, bar_ts=r.top_touch_ts)
            return TriggerOutcome(state="armed", price=r.top, ref_bar_ts=r.top_touch_ts[-1], kind=self.kind,
                                  inputs={"case": "flat", "range_start": r.start_ts.isoformat()},
                                  why="break of the pullback's flat trendline (the micro-Range top)", level=level)
        need = int(value(p["pivots"]))
        n = pivot_n(frame.objects["tunables"])
        window = [b for b in frame.run if b.ts >= start]
        highs = pivots(window, n).highs if n is not None else ()
        if len(highs) < need or not highs[-1].price < highs[0].price:
            raise InsufficientBars(f"trendline_break (fewer than {need} descending pivot highs)", need, len(highs))
        first, last = highs[0], highs[-1]
        slope = (last.price - first.price) / (last.index - first.index)
        price = (last.price + slope * (len(window) - 1 - last.index)).quantize(Decimal("0.0001"))
        level = TriggerLevel(trade_direction="long", price=price, bars_cleared=0, bar_ts=tuple(h.ts for h in highs))
        return TriggerOutcome(state="armed", price=price, ref_bar_ts=window[-1].ts, kind=self.kind,
                              inputs={"case": "sloped", "pivots": len(highs)},
                              why="break of the pullback's trendline", level=level)


class Sequence:
    """`sequence {steps[]}` (taxonomy §10.2; FINAL §4; STEP-8): the steps in
    order, the last step's bar is the trigger bar. Served for exactly the step
    shapes the frame's RangeBreak observation resolves, in this order:
    `price close_through Level_ref` (the break of the RangeBreak's level, its
    accepting close), `event(retest)` (its retest), `close_above(prior_bar)` (the
    turn: a close above the prior bar's high). The trigger is the turn bar's
    close; any other step list is not served (named `trigger:sequence`)."""

    kind = "sequence"
    STEPS = ("price close_through Level_ref", "event(retest)", "close_above(prior_bar)")

    def serves(self, params: dict[str, Any]) -> bool:
        return False  # a sequence has no params: `serves_def` reads its steps

    def serves_def(self, trigger_def) -> bool:
        steps = getattr(trigger_def, "steps", None) or ()
        return tuple(getattr(s.predicate, "expr", None) for s in steps) == self.STEPS

    def resolve(self, frame, trigger_def, value: Callable[[Any], Any]) -> TriggerOutcome:
        obs = frame.objects["range_break"]
        if isinstance(obs, str) or obs is None or obs.turn_index is None:
            raise InsufficientBars("sequence (break → retest → turn not complete)", 1, 0)
        bar = frame.run[obs.turn_index]
        level = TriggerLevel(trade_direction="long", price=bar.close, bars_cleared=0,
                             bar_ts=tuple(frame.run[i].ts for i in (obs.accept_index, obs.retest_index,
                                                                   obs.turn_index)))
        return TriggerOutcome(
            state="armed", price=bar.close, ref_bar_ts=bar.ts, kind=self.kind,
            inputs={"level": str(obs.level), "steps": list(self.STEPS)},
            why="break → retest → turn of the level", level=level,
        )


TRIGGERS: dict[TriggerType, TriggerResolver] = {
    TriggerType.BAR_BREAK: BarBreak(),
    TriggerType.RANGE_BREAK: RangeBreak(),
    TriggerType.INDICATOR_CROSS: IndicatorCross(),
    TriggerType.INDICATOR_REJECTION: IndicatorRejection(),
    TriggerType.TRENDLINE_BREAK: TrendlineBreak(),
    TriggerType.SEQUENCE: Sequence(),
}


def trigger_resolver(trigger_def) -> TriggerResolver | None:
    """The resolver that serves this trigger, or None (named missing)."""
    try:
        resolver = TRIGGERS.get(TriggerType(trigger_def.type))
    except ValueError:
        return None
    if resolver is None:
        return None
    if hasattr(resolver, "serves_def"):  # a resolver that reads the whole trigger (`sequence`)
        return resolver if resolver.serves_def(trigger_def) else None
    if not resolver.serves(getattr(trigger_def, "params", {}) or {}):
        return None
    return resolver


__all__ = ["BarBreak", "IndicatorCross", "RangeBreak", "TRIGGERS", "TriggerOutcome", "TriggerResolver",
           "trigger_resolver"]
