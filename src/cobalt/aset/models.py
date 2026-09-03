"""Pydantic models for the ASET sizer.

Iteration 4 (ruled by Dejan, 2026-08-28): sizing switched from the
daily-stop-percentage model to a fixed-dollar-per-grade model mirroring
Dejan's DAS hotkey files exactly (SheetMode). The old percentage model
(GRADE_RISK_PCT, daily_stop) is retired, not layered underneath — see
`engine.py` and `configs/cobalt/aset.yaml`.

Config-completion follow-up (Dejan, 2026-08-28): the grade ladder in
`configs/cobalt/aset.yaml` now carries the FULL truth (A+/A/B/C/D, every
grade has a real dollar figure, D always 0 — SAW principle) with UI/
compute availability tracked as a *separate* config field
(`enabled_grades`). There is no longer a hardcoded "tradeable grades"
constant here — `engine.compute_sizing` takes `enabled_grades` as an
explicit argument (resolved by the caller from
`SheetModesConfig.enabled_grades`), so enabling a grade later is a
config edit only, never a code change.
"""

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class Grade(str, Enum):
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"
    # Daily-Stop Model card framing carries over conceptually: "too
    # risky to feel like a C? It's not a C — it's a SAW trade." D always
    # carries a $0 risk figure in configs/cobalt/aset.yaml — the SAW
    # principle, enforced there, not here.
    D_SAW = "D"


class SheetMode(str, Enum):
    FULL = "full"
    HALF = "half"


class Direction(str, Enum):
    LONG = "long"
    SHORT = "short"


class SizingInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ticker: str = Field(min_length=1, max_length=12)
    grade: Grade
    direction: Direction
    sheet_mode: SheetMode
    # Resolved by the caller from configs/cobalt/aset.yaml (sheet_mode,
    # grade) — engine.py stays config-agnostic, same pattern as before.
    # ge=0, not gt=0: D's dollar figure is always exactly 0 (SAW
    # principle) and is still a legitimate value to carry through here —
    # whether D is allowed to *compute* is enabled_grades' job, not this
    # field's.
    risk_dollars: Decimal = Field(ge=0)
    entry: Decimal = Field(gt=0)
    stop: Decimal = Field(gt=0)
    last_price: Optional[Decimal] = Field(default=None, gt=0)
    price_source: Optional[str] = None

    @field_validator("ticker")
    @classmethod
    def _normalize_ticker(cls, v: str) -> str:
        v = v.strip().upper()
        if not v:
            raise ValueError("ticker must not be blank")
        return v

    @model_validator(mode="after")
    def _stop_on_correct_side_of_entry(self) -> "SizingInput":
        # Slice 2.1a (2026-08-31 defect D3, a 32% PCG stop typo that
        # nothing flagged): this used to be an engine.py WARNING, not a
        # rejection. Fail-loud means a structurally wrong stop refuses
        # the card, it does not warn-and-persist it. The threshold-based
        # typo guard (stop too FAR from entry) is config-driven and lives
        # in engine.compute_sizing instead — this check has no config
        # dependency, so it belongs on the model itself.
        if self.direction is Direction.LONG and self.stop >= self.entry:
            raise ValueError(
                f"Long stop ({self.stop}) must be below entry ({self.entry}) — "
                "refusing, not warning."
            )
        if self.direction is Direction.SHORT and self.stop <= self.entry:
            raise ValueError(
                f"Short stop ({self.stop}) must be above entry ({self.entry}) — "
                "refusing, not warning."
            )
        return self


class SizingResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    input: SizingInput
    risk_budget: Decimal
    per_share_risk: Decimal
    shares: int
    used_risk: Decimal
    target_1r: Decimal
    target_2r: Decimal
    warnings: list[str]


class FillRecompute(BaseModel):
    """Actual-fill recompute: same grade dollars, same stop, entry
    replaced by the real fill price. Not persisted to Postgres — an
    audit-trail note-only action (daily_note's FILL UPDATE block)."""

    model_config = ConfigDict(extra="forbid")

    original: SizingResult
    actual_fill: Decimal
    recomputed_shares: int
    recomputed_used_risk: Decimal
    share_delta: int
    distance_change_pct: Decimal
    structural_warning: Optional[str] = None
