"""What S2 can evaluate — and, for everything else, exactly what is missing (R2).

R2: Rubberband is evaluable end-to-end; the other defs parse and report
"not evaluable: missing atoms […]", never a card. The rule is data-driven
rather than slug-driven — no trade name appears here (L31/L32): a def is
evaluable when every atom its preconditions and avoids require
(`Predicate.required_atoms`), its trigger type and its stop placement are
all served by an S2 detector.

`text` predicates are human (L11) and never block evaluability; they are
counted so the dry-run can say how many human reads the card carries.
`radar_watch[]` is a watch-state list, not a card gate, and is out of S2's
evaluation scope.

Missing entries are named so the dry-run line reads on its own:
atoms verbatim (`Leg(pullback)`), relation words (`touched`), triggers as
`trigger:<type>`, stops as `stop:<type>[:<ref>]`.
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from cobalt.taxonomy.trade_def import StructuralExtremePlacement, TradeDef

#: Atoms served by `extension.py` and `daily.py`.
SUPPORTED_ATOMS: frozenset[str] = frozenset({
    "Extension.state",
    "Extension.instantiated",
    "Extension.leg_count",
    "RangeBreak(HTF).day_count",
})

#: bar_break with `bars_cleared` (structure.bar_break_trigger).
SUPPORTED_TRIGGERS: frozenset[str] = frozenset({"bar_break"})

#: structural_extreme on the tracked extreme (structure.tracked_extreme).
SUPPORTED_STOP_REFS: frozenset[str] = frozenset({"snapback_candle", "turn_low"})


class Evaluability(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    evaluable: bool
    missing_atoms: tuple[str, ...]
    human_predicates: int


def evaluability(td: TradeDef) -> Evaluability:
    required: set[str] = set()
    human = 0
    for predicate in [*td.preconditions, *td.avoid]:
        if predicate.expr is None:
            human += 1
        required |= predicate.required_atoms
    missing = set(required - SUPPORTED_ATOMS)

    trigger_type = td.trigger.type
    if trigger_type not in SUPPORTED_TRIGGERS or "bars_cleared" not in getattr(td.trigger, "params", {}):
        missing.add(f"trigger:{trigger_type}")

    placement = td.stop.placement
    if not (
        isinstance(placement, StructuralExtremePlacement)
        and placement.ref.value in SUPPORTED_STOP_REFS
    ):
        ref = getattr(placement, "ref", None)
        suffix = f":{ref.value}" if ref is not None else ""
        missing.add(f"stop:{placement.type}{suffix}")

    return Evaluability(
        evaluable=not missing, missing_atoms=tuple(sorted(missing)), human_predicates=human
    )


__all__ = [
    "Evaluability", "SUPPORTED_ATOMS", "SUPPORTED_STOP_REFS", "SUPPORTED_TRIGGERS",
    "evaluability",
]
