"""What the radar can evaluate — and, for everything else, exactly what is missing.

ONE PATH (FINAL §2.5, L3; setups one build STEP-2). This module keeps no
constants of its own. It reads the tables formation dispatches through —
`TRIGGERS`, `STOPS` / `STRUCTURAL_REFS`, `ATOMS`, `RELATIONS` and `ANCHORS`
(`cobalt.radar.formation`) — and walks every predicate through the same
shapes the interpreter evaluates (`formation.atoms.predicate_gaps`). So a
def the registry calls evaluable is one the interpreter can evaluate (E9),
and a symbol compared to a value its atom can never produce is named
`<atom>∌<value>` (E8), never served-but-never-true. No trade name appears
here (L31/L32): the rule is data-driven, never slug-driven.

`text` predicates are human (L11) and never block evaluability; they are
counted so the dry-run can say how many human reads the card carries.
`radar_watch[]` is a watch-state list, not a card gate, and is out of the
evaluation's scope.

Missing entries are named so the dry-run line reads on its own: atoms
verbatim (`Leg(pullback)`), relation words (`touched`), shapes the
interpreter cannot evaluate (`Unsupported(arith)`), out-of-domain symbols
(`Extension.state∌reverting`), triggers as `trigger:<type>`, stops as
`stop:<type>[:<ref>]`, a def whose preconditions name no anchor object as
`anchor:none` (fix round 2 F1: formation has nothing to hang on, so the def
could never form) — "this needs a build: a feature for later".
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from cobalt.taxonomy.trade_def import TradeDef

from ..formation.anchors import anchor_for
from ..formation.atoms import ATOMS, RELATIONS, predicate_gaps, relation_operand_names
from ..formation.stops import stop_resolver
from ..formation.triggers import trigger_resolver


class Evaluability(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    evaluable: bool
    missing_atoms: tuple[str, ...]
    human_predicates: int


def evaluability(td: TradeDef) -> Evaluability:
    missing: set[str] = set()
    human = 0
    for predicate in [*td.preconditions, *td.avoid]:
        if predicate.expr is None:
            human += 1
            continue
        consumed = relation_operand_names(predicate.ast)  # a served relation's own operands
        missing |= {a for a in predicate.required_atoms if a not in ATOMS and a not in RELATIONS and a not in consumed}
        missing |= predicate_gaps(predicate.ast)

    if anchor_for(td) is None:
        missing.add("anchor:none")

    if trigger_resolver(td.trigger) is None:
        missing.add(f"trigger:{td.trigger.type}")

    placement = td.stop.placement
    if stop_resolver(placement) is None:
        ref = getattr(placement, "ref", None)
        suffix = f":{ref.value}" if ref is not None else ""
        missing.add(f"stop:{placement.type}{suffix}")

    return Evaluability(
        evaluable=not missing, missing_atoms=tuple(sorted(missing)), human_predicates=human
    )


__all__ = ["Evaluability", "evaluability"]
