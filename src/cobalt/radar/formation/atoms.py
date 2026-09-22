"""ATOMS and RELATIONS — what the frame can measure, and the ONE walk of a
predicate's shape (FINAL §2.5, §4; setups one build STEP-2).

An atom resolver declares the atom's value kind, its PRODUCIBLE VALUE DOMAIN
(for a symbol), whether its number is a PRICE (negated back on the mirrored
frame, X12), the `TUNABLE_KEYS` of the detector that serves it and the
conventions it implements (R2-2.2 B terms (2) and (3)). The atom VALUES are
computed by the Frame (`anatomy/frame.py`); this table is what is served.

`predicate_gaps` walks a predicate through the SAME shapes the interpreter
(`radar/evaluate.py` `evaluate_node`) evaluates, so the registry and the
interpreter agree by construction (E9): an atom no resolver serves is named
verbatim, a relation word no resolver serves is named (it is also in
`required_atoms`), a shape the interpreter cannot evaluate is
`Unsupported(<kind>)`, and a symbol compared to a literal outside its
atom's domain is `<atom>∌<value>` (E8) — never served-but-never-true.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Callable, Literal

from pydantic import BaseModel, ConfigDict

from cobalt.taxonomy.predicate import (
    And,
    Arith,
    Between,
    Cfg,
    Compare,
    InTest,
    Node,
    Not,
    Null,
    Number,
    Or,
    Qualified,
    Quantity,
    Ref,
    Relation,
    SetLiteral,
    Symbol,
    render,
)

from ..anatomy import extension as _extension
from ..anatomy import in_play as _in_play
from ..anatomy import indicators as _indicators
from ..anatomy import leg_roles as _leg_roles
from ..anatomy import micro_range as _micro_range
from ..anatomy import session_levels as _levels
from ..anatomy import slope as _slope


class AtomValue(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    kind: Literal["boolean", "number", "symbol", "null", "unavailable"]
    boolean: bool | None = None
    number: Decimal | None = None
    symbol: str | None = None
    #: `null` = definitely no value (`not_instantiated`); `unavailable` = unknown.
    reason: str | None = None


@dataclass(frozen=True)
class AtomResolver:
    name: str
    value_kind: Literal["boolean", "number", "symbol"]
    #: A symbol atom's producible values (E8); None for boolean/number atoms.
    domain: frozenset[str] | None = None
    #: The number flips sign with the mirror (a price, or a price slope):
    #: negated back before it is published (X12).
    price: bool = False
    #: R2-2.2 term (2): the serving detector's own `TUNABLE_KEYS`.
    tunable_keys: tuple[str, ...] = ()
    #: R2-2.2 term (3): conventions this atom's resolver implements.
    conventions: tuple[str, ...] = ()
    #: Every reason the frame can give for no value (X11); a `null` value
    #: reaches the seam as `not_instantiated`.
    reasons: tuple[str, ...] = ()
    #: The number's unit when a predicate compares it to a `Quantity` band
    #: (`IN cfg(band) min`, FINAL §4 row 1); None = unitless.
    unit: str | None = None


def _serves(*resolvers: AtomResolver) -> dict[str, AtomResolver]:
    return {r.name: r for r in resolvers}


_EXT_REASONS = ("insufficient_bars", "incomplete_bucket", "catalyst_ref_unknown")
_WARM = _indicators.WARMUP_CONVENTION
_SLOPE_REASONS = ("insufficient_seed", "insufficient_bars", "slope_norm.bars_unset")
_DIRECTIONS = frozenset({"up", "down"})
_ROLE_REASONS = ("insufficient_bars", "not_instantiated")
#: `A-13`'s convention row (FINAL §6).
CATALYST_CONVENTION = "catalyst_ref.resolver"
#: `A-15`: `<Extension atom> on Leg(x)` reads the Extension detector over that leg's bars.
ON_LEG_CONVENTION = "extension.on_leg.form"
#: `A-17`: which levels count (the set); `A-18`: what "rejected" means.
LEVELS_CONVENTION = "levels.set"
REJECTED_CONVENTION = "level.rejected.rule"
_RANGE_KEYS = _micro_range.TUNABLE_KEYS
_RANGE_REASONS = ("insufficient_seed", "insufficient_bars", "incomplete_bucket",
                  *(f"{key}_unset" for key in _micro_range.TUNABLE_KEYS))

ATOMS: dict[str, AtomResolver] = _serves(
    # D4 (STEP-5): the lifecycle grows the producible domain (`reverting`,
    # `backside`); `building` / `extending` / `resuming` have no rule → E8.
    AtomResolver("Extension.state", "symbol", domain=frozenset({"culminating", "reverting", "backside", "none"}),
                 tunable_keys=(*_extension.TUNABLE_KEYS, *_extension.LIFECYCLE_KEYS, *_slope.TUNABLE_KEYS),
                 reasons=(*_EXT_REASONS, "slope_norm.bars_unset", "insufficient_seed")),
    AtomResolver("Extension.instantiated", "boolean", tunable_keys=_extension.TUNABLE_KEYS, reasons=_EXT_REASONS),
    AtomResolver("Extension.leg_count", "number", tunable_keys=_extension.TUNABLE_KEYS,
                 reasons=(*_EXT_REASONS, "not_instantiated")),
    AtomResolver("RangeBreak(HTF).day_count", "number",
                 reasons=("no_daily_bars", "insufficient_bars", "not_instantiated")),
    # --- D1 (STEP-3): shared indicators + session levels -------------------
    AtomResolver("price", "number", price=True, reasons=("insufficient_bars",)),
    AtomResolver("EMA9", "number", price=True, conventions=(_WARM,), reasons=("insufficient_seed",)),
    AtomResolver("EMA21", "number", price=True, conventions=(_WARM,), reasons=("insufficient_seed",)),
    AtomResolver("ATR(working_tf)", "number", conventions=(_WARM,), reasons=("insufficient_seed",)),
    AtomResolver("EMA9.slope", "number", price=True, tunable_keys=_slope.TUNABLE_KEYS, conventions=(_WARM,),
                 reasons=_SLOPE_REASONS),
    AtomResolver("slope_norm(EMA9)", "number", price=True, tunable_keys=_slope.TUNABLE_KEYS,
                 conventions=(_WARM,), reasons=_SLOPE_REASONS),
    AtomResolver("slope_norm(VWAP)", "number", price=True, tunable_keys=_slope.TUNABLE_KEYS,
                 conventions=(_levels.VWAP_CONVENTION, _WARM), reasons=_SLOPE_REASONS),
    AtomResolver("VWAP", "number", price=True, conventions=(_levels.VWAP_CONVENTION,),
                 reasons=("insufficient_bars",)),
    *(AtomResolver(f"DayRange.{part}", "number", price=True, conventions=(_levels.DAYRANGE_CONVENTION,),
                   reasons=("insufficient_bars",)) for part in ("high", "low", "upper_third")),
    *(AtomResolver(name, "number", price=True, reasons=("not_instantiated",)) for name in ("PMH", "PML")),
    *(AtomResolver(name, "number", price=True, reasons=("no_daily_bars",)) for name in ("PDH", "PDL")),
    AtomResolver("InPlay.state", "symbol", domain=_in_play.DOMAIN, tunable_keys=_in_play.TUNABLE_KEYS),
    # --- D2 (STEP-4): Range(micro) ------------------------------------------
    AtomResolver("Range(micro).instantiated", "boolean", tunable_keys=_RANGE_KEYS, conventions=(_WARM,),
                 reasons=_RANGE_REASONS),
    AtomResolver("Range(micro).duration", "number", tunable_keys=_RANGE_KEYS, conventions=(_WARM,),
                 reasons=(*_RANGE_REASONS, "not_instantiated"), unit="min"),
    *(AtomResolver(f"Range(micro).{part}", "number", price=True, tunable_keys=_RANGE_KEYS, conventions=(_WARM,),
                   reasons=(*_RANGE_REASONS, "not_instantiated")) for part in ("low", "top", "base", "bound")),
    AtomResolver("Range(micro).height", "number", tunable_keys=_RANGE_KEYS, conventions=(_WARM,),
                 reasons=(*_RANGE_REASONS, "not_instantiated")),
    AtomResolver("Range(micro).wick_ratio", "number", tunable_keys=_RANGE_KEYS, conventions=(_WARM,),
                 reasons=(*_RANGE_REASONS, "not_instantiated")),
    # --- D3 (STEP-4): the opening drive's role -----------------------------
    AtomResolver("Leg(opening_drive).direction", "symbol", domain=frozenset({"up", "down"}),
                 reasons=("insufficient_bars", "not_instantiated")),
    AtomResolver("Leg(opening_drive).terminated_by", "symbol", domain=frozenset({"pullback", "consolidation"}),
                 tunable_keys=(*_RANGE_KEYS, *_leg_roles.TUNABLE_KEYS), conventions=(_WARM,),
                 reasons=(*_RANGE_REASONS, "leg.consolidation_max_retrace_unset", "not_instantiated")),
    # --- D3 (STEP-6): pullback / impulse roles ------------------------------
    AtomResolver("Leg(pullback).direction", "symbol", domain=_DIRECTIONS, reasons=_ROLE_REASONS),
    AtomResolver("Leg(pullback).end", "number", price=True, reasons=_ROLE_REASONS),
    AtomResolver("Leg(pullback).index", "number", reasons=_ROLE_REASONS),
    AtomResolver("Leg(impulse).direction", "symbol", domain=_DIRECTIONS, reasons=_ROLE_REASONS),
    AtomResolver("Leg(opening_drive OR impulse).direction", "symbol", domain=_DIRECTIONS, reasons=_ROLE_REASONS),
    # --- THE ONE NAMED SPECIAL CASE (FINAL §6, R2-2.4 B): `A-13` -------------
    # The catalyst resolver stands in for data the radar does not have: the
    # def's "or setup" branch is read as met by the pool admission. Its
    # ASSUMED_CONVENTIONS are its row key; the mark reaches the card through
    # the `assumed_formation` dot, never a field on the atom.
    AtomResolver("catalyst_ref", "boolean", conventions=(CATALYST_CONVENTION,), reasons=("not_instantiated",)),
    # --- D5 / D6 part (STEP-7): the level set and `rejected` ------------------
    AtomResolver("Level_ref(resistance).rejected", "boolean", conventions=(LEVELS_CONVENTION, REJECTED_CONVENTION),
                 reasons=("insufficient_bars", "no_daily_bars")),
)


@dataclass(frozen=True)
class RelationResolver:
    """A relation / qualifier word over the operands' typed objects,
    three-valued (FINAL §4). None registered yet: an unserved word is named."""

    word: str
    resolve: Callable = field(repr=False, default=lambda *_a, **_k: None)
    #: R2-2.2 term (3): the conventions this relation's resolver implements.
    conventions: tuple[str, ...] = ()


def flat_between(norm: list[Decimal | None], *, start: int, end: int, window: int, threshold: Decimal) -> bool | None:
    """`flat(x, window) between start and end` (FINAL §4; STEP-5): some run of
    `window` consecutive bars inside [start, end] where every normalised slope
    has |s| ≤ threshold. No span (end < start) is unknown; a span shorter than
    the window is False; a window with a missing value is skipped."""
    if end < start:
        return None
    for i in range(start, end - window + 2):
        chunk = norm[i:i + window]
        if len(chunk) == window and None not in chunk and all(abs(s) <= threshold for s in chunk):
            return True
    return False


#: The event refs `between` spans: `turn` = the tracked extreme's bar (the
#: move's turn), `cross` = the def's own `indicator_cross` bar.
BETWEEN_EVENTS = frozenset({"turn", "cross"})


def _flat_subject(node: Node) -> tuple[str, Node] | None:
    """`flat(<indicator>, window: <w>)` → (indicator, window node), else None."""
    if not isinstance(node, Ref) or len(node.segments) != 1 or node.segments[0].name != "flat":
        return None
    args = node.segments[0].args or ()
    if len(args) != 2 or args[0].name is not None or args[1].name != "window":
        return None
    indicator = render(args[0].value) if isinstance(args[0].value, Ref) else None
    if indicator not in _slope.FLAT_KEYS:
        return None
    return indicator, args[1].value


def window_bars(node: Node, working_minutes: int) -> int | None:
    """A window in working bars: `<n> min / working_tf` (ceil — the window must
    cover the minutes) or `<n> bars`; any other shape is None (unsupported)."""
    from math import ceil

    if isinstance(node, Arith) and node.op == "/" and isinstance(node.left, Quantity) \
            and node.left.unit == "min" and isinstance(node.left.value, Number) \
            and isinstance(node.right, Ref) and render(node.right) == "working_tf":
        return max(1, ceil(node.left.value.value / working_minutes))
    if isinstance(node, Quantity) and node.unit == "bars" and isinstance(node.value, Number):
        return int(node.value.value)
    return None


def _between_gaps(node: Between) -> set[str]:
    subject = _flat_subject(node.subject)
    gaps = set()
    if subject is None or window_bars(subject[1], 1) is None:
        gaps.add(f"Unsupported(between:{render(node.subject)})")
    for edge in (node.start, node.end):
        if not (isinstance(edge, Ref) and render(edge) in BETWEEN_EVENTS):
            gaps.add(f"Unsupported(between:{render(edge)})")
    return gaps


#: STEP-6: the leg roles a relation may name, and the indicators `touched` reads.
TOUCH_LEGS = frozenset({"Leg(pullback)", "Leg(impulse)"})
TOUCH_INDICATORS = frozenset({"EMA9", "EMA21", "VWAP"})
ON_LEGS = frozenset({"Leg(pre_test)"})
ON_SUBJECTS = frozenset({"Extension.instantiated"})


def _touched_gaps(node: Relation) -> set[str]:
    gaps = set()
    if render(node.left) not in TOUCH_LEGS:
        gaps.add(f"Unsupported(touched:{render(node.left)})")
    if render(node.right) not in TOUCH_INDICATORS:
        gaps.add(f"Unsupported(touched:{render(node.right)})")
    return gaps


def _on_gaps(node: Qualified) -> set[str]:
    gaps = set()
    if render(node.subject) not in ON_SUBJECTS:
        gaps.add(f"Unsupported(on:{render(node.subject)})")
    if render(node.anchor) not in ON_LEGS:
        gaps.add(f"Unsupported(on:{render(node.anchor)})")
    return gaps


def relation_operand_names(node: Node) -> set[str]:
    """The `required_atoms` names a SERVED relation consumes (its subject and
    event operands) — the registry does not count them as unserved atoms."""
    if isinstance(node, Between) and "between" in RELATIONS and not _between_gaps(node):
        return {render(node.subject), render(node.start), render(node.end)}
    if isinstance(node, Relation) and node.op == "touched" and not _touched_gaps(node):
        return {render(node.left), render(node.right)}
    if isinstance(node, Qualified) and node.op == "on" and not _on_gaps(node):
        return {render(node.subject), render(node.anchor)}
    if isinstance(node, Compare):  # a bound direction form / a served `dist` is a value, not an atom
        return {render(s) for s in (node.left, node.right) if isinstance(s, Ref) and (
            bound_direction(s) is not None or (dist_operands(s) is not None and not _operand_gaps(s)))}
    out: set[str] = set()
    for op in getattr(node, "operands", ()) or ():
        out |= relation_operand_names(op)
    if isinstance(node, Not):
        out |= relation_operand_names(node.operand)
    return out


RELATIONS: dict[str, RelationResolver] = {
    "between": RelationResolver("between"),
    # STEP-6: `touched(Leg, indicator)` = the leg's extreme reached the
    # indicator (contact, not proximity, taxonomy §3.1); `<Extension atom> on
    # Leg(x)` = that atom of the Extension detector run over the leg's bars.
    "touched": RelationResolver("touched"),
    "on": RelationResolver("on", conventions=(_leg_roles.PRE_TEST_CONVENTION, ON_LEG_CONVENTION)),
}

#: Symbols bound from the frame (FINAL §4): in a frame, the long-side text's
#: trade direction is `up`; `opposite(x)` / `against(x)` flip a direction.
BOUND_SYMBOLS = {"trade_direction": "up"}
DIRECTION_FUNCTIONS = frozenset({"opposite", "against"})


def dist_operands(node: Node) -> tuple[Node, Node] | None:
    """`dist(a, b)` (FINAL §3 D5; STEP-7) → its two operands, else None. Its
    value is |a − b| in price; a def compares it to `cfg(k) × ATR(working_tf)`."""
    if isinstance(node, Ref) and len(node.segments) == 1 and node.segments[0].name == "dist":
        args = node.segments[0].args or ()
        if len(args) == 2 and all(a.name is None for a in args):
            return args[0].value, args[1].value
    return None


def bound_direction(node: Node) -> str | None:
    """`trade_direction`, `opposite(…)`, `against(…)` → the frame's direction
    value, else None (not a bound form)."""
    if isinstance(node, Symbol) and node.name in BOUND_SYMBOLS:
        return BOUND_SYMBOLS[node.name]
    if isinstance(node, Ref) and len(node.segments) == 1 and node.segments[0].name in DIRECTION_FUNCTIONS:
        args = node.segments[0].args or ()
        if len(args) == 1 and args[0].name is None:
            inner = args[0].value
            inner_symbol = Symbol(kind="symbol", name=render(inner)) if isinstance(inner, Ref) else inner
            value = bound_direction(inner_symbol)
            if value is not None:
                return "down" if value == "up" else "up"
    return None


# ---------------------------------------------------------------------
# The one shape walk
# ---------------------------------------------------------------------


def _operand_gaps(node: Node) -> set[str]:
    if isinstance(node, (Number, Symbol, Cfg, Null)):
        return set()
    if isinstance(node, Ref) and dist_operands(node) is not None:
        a, b = dist_operands(node)
        return _operand_gaps(a) | _operand_gaps(b)
    if isinstance(node, Ref):
        text = render(node)
        return set() if text in ATOMS or bound_direction(node) is not None else {text}
    if isinstance(node, Arith) and node.op in ("*", "/"):
        return _operand_gaps(node.left) | _operand_gaps(node.right)  # FINAL §4 row 2 (STEP-5)
    return {f"Unsupported({node.kind})"}


def _domain_gaps(atom_node: Node, values) -> set[str]:
    if not isinstance(atom_node, Ref):
        return set()
    resolver = ATOMS.get(render(atom_node))
    if resolver is None or resolver.domain is None:
        return set()
    return {f"{resolver.name}∌{v.name}" for v in values
            if isinstance(v, Symbol) and v.name not in resolver.domain and v.name not in BOUND_SYMBOLS}


def unit_mismatch(quantity_unit: str, other: str | None) -> str | None:
    """The named `Unsupported` of a band whose unit is not the other side's."""
    if other == quantity_unit:
        return None
    return f"Unsupported(unit:{quantity_unit})" if other is None else f"Unsupported(unit:{quantity_unit}≠{other})"


def _unit_gaps(atom_node: Node, quantity_unit: str) -> set[str]:
    """FINAL §4 row 1: `IN cfg(band) <unit>` needs an atom measured in that
    unit (the row's own unit is checked when the band resolves)."""
    resolver = ATOMS.get(render(atom_node)) if isinstance(atom_node, Ref) else None
    if resolver is None:
        return set()
    gap = unit_mismatch(quantity_unit, resolver.unit)
    return set() if gap is None else {gap}


def predicate_gaps(node: Node) -> set[str]:
    """Everything that keeps the interpreter from evaluating `node`."""
    if isinstance(node, Not):
        return predicate_gaps(node.operand)
    if isinstance(node, (And, Or)):
        return set().union(*(predicate_gaps(op) for op in node.operands))
    if isinstance(node, Ref):
        text = render(node)
        resolver = ATOMS.get(text)
        if resolver is None:
            return {text}
        return set() if resolver.value_kind == "boolean" else {f"Unsupported({text} is not boolean)"}
    if isinstance(node, Compare):
        gaps = _operand_gaps(node.left) | _operand_gaps(node.right)
        if node.op in ("==", "!="):
            gaps |= _domain_gaps(node.left, [node.right]) | _domain_gaps(node.right, [node.left])
        return gaps
    if isinstance(node, InTest):
        if isinstance(node.right, Quantity) and isinstance(node.right.value, Cfg):
            return _operand_gaps(node.left) | _unit_gaps(node.left, node.right.unit)
        if not isinstance(node.right, SetLiteral):
            return _operand_gaps(node.left) | {f"Unsupported({node.kind})"}
        gaps = _operand_gaps(node.left)
        for item in node.right.items:
            gaps |= _operand_gaps(item)
        return gaps | _domain_gaps(node.left, node.right.items)
    if isinstance(node, Relation):
        if node.op == "touched" and node.op in RELATIONS:
            return _touched_gaps(node)
        return set() if node.op in RELATIONS else {node.op}
    if isinstance(node, Qualified):
        if node.op == "on" and node.op in RELATIONS:
            return _on_gaps(node)
        return set() if node.op in RELATIONS else {node.op}
    if isinstance(node, Between):
        return _between_gaps(node) if "between" in RELATIONS else {"between"}
    return {f"Unsupported({node.kind})"}


__all__ = [
    "ATOMS", "AtomResolver", "AtomValue", "BETWEEN_EVENTS", "BOUND_SYMBOLS", "CATALYST_CONVENTION",
    "LEVELS_CONVENTION", "ON_LEG_CONVENTION", "REJECTED_CONVENTION", "RELATIONS", "RelationResolver",
    "bound_direction", "dist_operands", "flat_between", "predicate_gaps",
    "relation_operand_names", "unit_mismatch", "window_bars",
]
