"""Pydantic models for the ASET sizer.

Iteration 4 (ruled by Dejan, 2026-08-28): sizing switched from the
daily-stop-percentage model to a fixed-dollar-per-grade model mirroring
Dejan's DAS hotkey files exactly (SheetMode). The old percentage model
(GRADE_RISK_PCT, daily_stop) is retired, not layered underneath — see
`engine.py` and `configs/cobalt/aset.yaml`.
"""

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Grade(str, Enum):
    A_PLUS = "A+"  # reserved, hidden from the sheet for now
    A = "A"
    B = "B"
    C = "C"
    # Daily-Stop Model card framing carries over conceptually: "too
    # risky to feel like a C? It's not a C — it's a SAW trade." Neither
    # C nor D_SAW has a fixed-dollar figure in the sheet-mode model —
    # both render as "no trade (SAW)" and refuse to compute.
    D_SAW = "D"


# The only grades with a defined fixed-dollar risk right now. Selecting
# any other grade is a fail-loud SizingError in engine.compute_sizing,
# not a silent zero or a guess.
TRADEABLE_GRADES = (Grade.A, Grade.B)


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
    risk_dollars: Decimal = Field(gt=0)
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
