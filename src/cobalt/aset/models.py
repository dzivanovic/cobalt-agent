"""Pydantic models for the ASET sizer."""

from __future__ import annotations

from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Grade(str, Enum):
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"
    # Daily-Stop Model card: "Too risky to feel like a C? It's not a C —
    # it's a SAW trade. Zero size."
    D_SAW = "D"


GRADE_RISK_PCT: dict[Grade, Decimal] = {
    Grade.A_PLUS: Decimal("80"),
    Grade.A: Decimal("30"),
    Grade.B: Decimal("15"),
    Grade.C: Decimal("5"),
    Grade.D_SAW: Decimal("0"),
}


class Direction(str, Enum):
    LONG = "long"
    SHORT = "short"


class SizingInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ticker: str = Field(min_length=1, max_length=12)
    grade: Grade
    direction: Direction
    daily_stop: Decimal = Field(
        gt=0, description="Max $ loss for the entire day (account ÷ 100 prefill for now, TEMP override)"
    )
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
    risk_pct: Decimal
    risk_budget: Decimal
    per_share_risk: Decimal
    shares: int
    used_risk: Decimal
    target_1r: Decimal
    target_2r: Decimal
    warnings: list[str]
