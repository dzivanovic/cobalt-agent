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

from collections.abc import Mapping
from decimal import Decimal
from enum import Enum
from typing import Any, Optional

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


#: Every card-row column `SizingResult.from_card` reads. None may be NULL:
#: a default for any of them would be a second sizing (S3 exits v3 §2).
FROM_CARD_COLUMNS = (
    "ticker", "grade", "direction", "sheet_mode", "risk_budget",
    "entry", "stop", "per_share_risk", "shares", "used_risk", "warnings",
)


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

    @classmethod
    def from_card(cls, row: Mapping[str, Any]) -> "SizingResult":
        """THE ONLY REBUILD of a sizing from a persisted card row (S3 exits
        v3 §2 [F-22]; L3).

        Copies `entry`, `stop`, `per_share_risk`, `shares`, `risk_budget`
        and `direction` — and the rest of the sizing's own columns — off
        the row as stored. Nothing is recomputed and nothing is defaulted:
        a NULL (an unsized radar card, a legacy row) raises naming the
        column, because a default here would be a second sizing and would
        move `distance_change_pct` and the drift warning with it. The
        targets are the stored entry ± the stored per-share risk, the
        expression `compute_sizing` uses (X10 is the parity proof).
        """
        missing = [c for c in FROM_CARD_COLUMNS if c not in row or row[c] is None]
        if missing:
            raise ValueError(
                f"card {row.get('id', '?')}: cannot rebuild its sizing — "
                f"{', '.join(missing)} {'is' if len(missing) == 1 else 'are'} NULL on the "
                "card row. No default is taken: a default is a second sizing."
            )
        inp = SizingInput(
            ticker=row["ticker"],
            grade=row["grade"],
            direction=row["direction"],
            sheet_mode=row["sheet_mode"],
            risk_dollars=row["risk_budget"],
            entry=row["entry"],
            stop=row["stop"],
            last_price=row.get("last_price"),
            price_source=row.get("price_source"),
        )
        entry, distance = Decimal(row["entry"]), Decimal(row["per_share_risk"])
        sign = Decimal(1) if inp.direction is Direction.LONG else Decimal(-1)
        cents = Decimal("0.01")
        return cls(
            input=inp,
            risk_budget=Decimal(row["risk_budget"]),
            per_share_risk=distance,
            shares=int(row["shares"]),
            used_risk=Decimal(row["used_risk"]),
            target_1r=(entry + sign * distance).quantize(cents),
            target_2r=(entry + sign * distance * 2).quantize(cents),
            warnings=list(row["warnings"]),
        )


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
    #: S3 C1 (v3 §4): the drift P in force at the fill — his
    #: `fills.drift_warning_pct` — and whether `distance_change_pct > P`.
    #: Both None = the warning was NOT evaluated (P missing, L1: bannered).
    drift_warning_pct: Optional[Decimal] = None
    drift_warned: Optional[bool] = None
