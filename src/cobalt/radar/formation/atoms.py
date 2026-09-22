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
    Between,
    Cfg,
    Compare,
    InTest,
    Node,
    Not,
    Number,
    Or,
    Qualified,
    Ref,
    Relation,
    SetLiteral,
    Symbol,
    render,
)

from ..anatomy import extension as _extension
from ..anatomy import in_play as _in_play
from ..anatomy import indicators as _indicators
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


def _serves(*resolvers: AtomResolver) -> dict[str, AtomResolver]:
    return {r.name: r for r in resolvers}


_EXT_REASONS = ("insufficient_bars", "incomplete_bucket", "catalyst_ref_unknown")
_WARM = _indicators.WARMUP_CONVENTION
_SLOPE_REASONS = ("insufficient_seed", "insufficient_bars", "slope_norm.bars_unset")

ATOMS: dict[str, AtomResolver] = _serves(
    AtomResolver("Extension.state", "symbol", domain=frozenset({"culminating", "none"}),
                 tunable_keys=_extension.TUNABLE_KEYS, reasons=_EXT_REASONS),
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
)


@dataclass(frozen=True)
class RelationResolver:
    """A relation / qualifier word over the operands' typed objects,
    three-valued (FINAL §4). None registered yet: an unserved word is named."""

    word: str
    resolve: Callable = field(repr=False, default=lambda *_a, **_k: None)


RELATIONS: dict[str, RelationResolver] = {}


# ---------------------------------------------------------------------
# The one shape walk
# ---------------------------------------------------------------------


def _operand_gaps(node: Node) -> set[str]:
    if isinstance(node, (Number, Symbol, Cfg)):
        return set()
    if isinstance(node, Ref):
        text = render(node)
        return set() if text in ATOMS else {text}
    return {f"Unsupported({node.kind})"}


def _domain_gaps(atom_node: Node, values) -> set[str]:
    if not isinstance(atom_node, Ref):
        return set()
    resolver = ATOMS.get(render(atom_node))
    if resolver is None or resolver.domain is None:
        return set()
    return {f"{resolver.name}∌{v.name}" for v in values if isinstance(v, Symbol) and v.name not in resolver.domain}


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
        if not isinstance(node.right, SetLiteral):
            return _operand_gaps(node.left) | {f"Unsupported({node.kind})"}
        gaps = _operand_gaps(node.left)
        for item in node.right.items:
            gaps |= _operand_gaps(item)
        return gaps | _domain_gaps(node.left, node.right.items)
    if isinstance(node, Relation):
        return set() if node.op in RELATIONS else {node.op}
    if isinstance(node, Qualified):
        return set() if node.op in RELATIONS else {node.op}
    if isinstance(node, Between):
        return set() if "between" in RELATIONS else {"between"}
    return {f"Unsupported({node.kind})"}


__all__ = ["ATOMS", "AtomResolver", "AtomValue", "RELATIONS", "RelationResolver", "predicate_gaps"]
