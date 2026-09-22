"""The closed payloads of the system-side scoring seam (S2-P2, Astra R1-1).

`system.radar_score` sits on the SYSTEM side (0006), and system never holds
user data (L32, ADR-0008). A free JSONB bag would let a trade's authored
predicate text, its resolved per-trade thresholds, a WHY sentence or a
trader setting leak across by accident. So `detail` and `desk_shadow` are
written ONLY through these models:

* every model forbids unknown keys;
* an atom is a bare anatomy reference that re-parses through the §10.5
  grammar to exactly itself, with no `cfg()`, no quoted string and no
  free words inside it — `Extension.state`, `RangeBreak(HTF).day_count`;
* a symbol is one lowercase identifier (`culminating`);
* observations are named numbers with their bar timestamp;
* desk shadow grades are integers 1–10 or a closed N/A reason, with a
  WHY *code*, never WHY prose.

Trade-specific WHY text, thresholds and the settings snapshot live on the
user side (`"user".card_dots`, `"user".radar_score_receipt`). A valid
payload therefore cannot express trade_def content — the property
`test_radar_score_carries_no_trade_def_content` asserts.
"""

from __future__ import annotations

from decimal import Decimal
from typing import Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, field_validator, model_validator

from cobalt.taxonomy.predicate import (
    QUALIFIER_WORDS,
    RELATION_WORDS,
    Cfg,
    EventAtom,
    PredicateSyntaxError,
    Ref,
    String,
    Words,
    parse_predicate,
    render,
)

IDENTIFIER = r"^[a-z][a-z0-9_]*$"
VERSION = r"^[a-z0-9][a-z0-9_.-]*$"

#: Why an atom has no value this run. Closed on purpose. X11 (setups one
#: build STEP-3) added the two a D1 atom can give: `insufficient_seed`
#: (FINAL §5 [F-14]) and `slope_norm.bars_unset` (a null `A-11` row).
UnavailableReason = Literal[
    "catalyst_ref_unknown",
    "insufficient_bars",
    "incomplete_bucket",
    "no_daily_bars",
    "not_instantiated",
    "detector_missing",
    "insufficient_seed",
    "slope_norm.bars_unset",
    # X11, STEP-4: the null engine keys of the D2 / D3 detectors.
    "range.micro.touches_per_side_unset",
    "range.micro.touch_tolerance_atr_unset",
    "range.micro.bound_flat_slope_atr_unset",
    "leg.consolidation_max_retrace_unset",
]


def _walk_forbidden(node) -> bool:
    """True if any Cfg / String / Words node sits anywhere under `node`."""
    if isinstance(node, (Cfg, String, Words)):
        return True
    if isinstance(node, Ref):
        return any(
            _walk_forbidden(arg.value)
            for seg in node.segments
            for arg in (seg.args or ())
        )
    if isinstance(node, EventAtom):
        return any(_walk_forbidden(arg.value) for arg in node.args)
    for name in type(node).model_fields:
        value = getattr(node, name)
        children = value if isinstance(value, tuple) else (value,)
        for child in children:
            if isinstance(child, BaseModel) and _walk_forbidden(child):
                return True
    return False


def validate_atom(atom: str) -> str:
    """A generic anatomy atom, or a relation/qualifier word. Else raise."""
    if atom in RELATION_WORDS | QUALIFIER_WORDS | {"between"}:
        return atom
    try:
        node = parse_predicate(atom)
    except PredicateSyntaxError as e:
        raise ValueError(f"not an atom: {e}") from None
    if not isinstance(node, (Ref, EventAtom)) or render(node) != atom:
        raise ValueError(f"not a bare atom reference: {atom!r}")
    if isinstance(node, Ref) and node.demonstrative:
        raise ValueError(f"not a bare atom reference: {atom!r}")
    if _walk_forbidden(node):
        raise ValueError(
            f"atom {atom!r} carries a cfg() key, a quoted string or free words — "
            "trade-specific content never crosses to the system side (L32)"
        )
    return atom


class _Closed(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class SeamObservation(_Closed):
    """One named measurement the evaluation consumed, with its bar."""

    name: str = Field(pattern=IDENTIFIER)
    value: Decimal | None
    bar_ts: AwareDatetime | None = None


class AtomOutcome(_Closed):
    atom: str
    value_kind: Literal["boolean", "number", "symbol", "unavailable"]
    boolean: bool | None = None
    number: Decimal | None = None
    symbol: str | None = Field(default=None, pattern=IDENTIFIER)
    unavailable: UnavailableReason | None = None

    @field_validator("atom")
    @classmethod
    def _atom(cls, v: str) -> str:
        return validate_atom(v)

    @model_validator(mode="after")
    def _one_value(self) -> AtomOutcome:
        slots = {
            "boolean": self.boolean,
            "number": self.number,
            "symbol": self.symbol,
            "unavailable": self.unavailable,
        }
        set_slots = [k for k, v in slots.items() if v is not None]
        if set_slots != [self.value_kind]:
            raise ValueError(
                f"{self.atom}: value_kind={self.value_kind!r} must set exactly that slot, "
                f"found {set_slots}"
            )
        return self


class RadarScoreDetail(_Closed):
    """`system.radar_score.detail`."""

    atoms: tuple[AtomOutcome, ...]
    missing_atoms: tuple[str, ...]
    observations: tuple[SeamObservation, ...]
    #: Extension path that formed: A lands cards; B-only is logged, never
    #: a card (R4 — catalyst unknown in S2).
    extension_path: Literal["A", "B_only"] | None = None
    formed_bar_ts: AwareDatetime | None = None

    @field_validator("missing_atoms")
    @classmethod
    def _missing(cls, v: tuple[str, ...]) -> tuple[str, ...]:
        return tuple(validate_atom(a) for a in v)


class DeskShadowEntry(_Closed):
    grade: int | None = Field(default=None, ge=1, le=10)
    na_reason: Literal["DESK_NA", "CHECKPOINT_MISSING", "DEFAULT_UNRULED"] | None = None
    why_code: str = Field(pattern=IDENTIFIER)
    observations: tuple[SeamObservation, ...] = ()
    formula_version: str = Field(pattern=VERSION)

    @model_validator(mode="after")
    def _grade_xor_na(self) -> DeskShadowEntry:
        if (self.grade is None) == (self.na_reason is None):
            raise ValueError("a desk shadow entry carries a grade or an N/A reason, exactly one")
        return self


class DeskShadow(_Closed):
    """`system.radar_score.desk_shadow` — the three desk dots."""

    catalyst: DeskShadowEntry
    market_alignment: DeskShadowEntry
    sector_alignment: DeskShadowEntry


__all__ = [
    "AtomOutcome",
    "DeskShadow",
    "DeskShadowEntry",
    "RadarScoreDetail",
    "SeamObservation",
    "UnavailableReason",
    "validate_atom",
]
