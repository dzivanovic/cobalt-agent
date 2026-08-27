"""Deterministic ASET sizing math. Pure functions — no I/O, no LLMs.

Iteration 4 (ruled by Dejan, 2026-08-28): sizing is fixed-dollar-per-
grade, mirroring Dejan's DAS Trader Pro hotkey files exactly (sheet mode
full/half — see configs/cobalt/aset.yaml). The earlier daily-stop ×
grade-percentage model (docs/90 - References/aset_daily_position_sizer.html,
docs/90 - References/Daily_Stop_Model_Card.pdf) and its TEMP account÷100
prefill override are retired — one-path rule. Historical reference only;
no longer the math this module implements.
"""

from decimal import Decimal

from .models import Direction, FillRecompute, Grade, SizingInput, SizingResult, TRADEABLE_GRADES

CENTS = Decimal("0.01")

# ≥25% distance change between the planned and actual-fill entry means
# the stop was likely picked against a different price than what was
# actually paid — flag it as possibly no longer structural rather than
# silently recomputing and moving on.
FILL_DISTANCE_WARNING_PCT = Decimal("25")


class SizingError(ValueError):
    """Invalid sizing input — fail loud, never guess."""


def compute_sizing(inp: SizingInput) -> SizingResult:
    if inp.grade not in TRADEABLE_GRADES:
        raise SizingError(
            f"Grade {inp.grade.value} is not tradeable in sheet mode — no trade (SAW)."
        )

    distance = abs(inp.entry - inp.stop)
    if distance == 0:
        raise SizingError("Entry and stop cannot be the same price.")

    risk_budget = inp.risk_dollars
    shares = int(risk_budget / distance)
    used_risk = distance * shares

    is_long = inp.direction is Direction.LONG
    target_1r = inp.entry + distance if is_long else inp.entry - distance
    target_2r = inp.entry + distance * 2 if is_long else inp.entry - distance * 2

    warnings: list[str] = []
    if is_long and inp.stop >= inp.entry:
        warnings.append(
            "For a long trade the stop is normally below entry. Check the ASET plan."
        )
    if not is_long and inp.stop <= inp.entry:
        warnings.append(
            "For a short trade the stop is normally above entry. Check the ASET plan."
        )
    if shares < 1:
        warnings.append(
            "Position size rounds to zero: risk per share exceeds the allocated risk budget."
        )

    return SizingResult(
        input=inp,
        risk_budget=risk_budget.quantize(CENTS),
        per_share_risk=distance,
        shares=shares,
        used_risk=used_risk.quantize(CENTS),
        target_1r=target_1r.quantize(CENTS),
        target_2r=target_2r.quantize(CENTS),
        warnings=warnings,
    )


def compute_fill_recompute(original: SizingResult, actual_fill: Decimal) -> FillRecompute:
    """Recompute shares at the actual fill price, same grade dollars and
    same stop. Note-only — never persisted to Postgres as a new row."""
    if actual_fill <= 0:
        raise SizingError("actual_fill must be positive")

    inp = original.input
    new_distance = abs(actual_fill - inp.stop)
    if new_distance == 0:
        raise SizingError("Actual fill and stop cannot be the same price.")

    risk_budget = inp.risk_dollars
    recomputed_shares = int(risk_budget / new_distance)
    recomputed_used_risk = (new_distance * recomputed_shares).quantize(CENTS)

    planned_distance = original.per_share_risk
    distance_change_pct = (
        abs(new_distance - planned_distance) / planned_distance * Decimal("100")
    ).quantize(CENTS)

    structural_warning = None
    if distance_change_pct >= FILL_DISTANCE_WARNING_PCT:
        structural_warning = "stop may no longer be structural — re-read the level."

    return FillRecompute(
        original=original,
        actual_fill=actual_fill,
        recomputed_shares=recomputed_shares,
        recomputed_used_risk=recomputed_used_risk,
        share_delta=recomputed_shares - original.shares,
        distance_change_pct=distance_change_pct,
        structural_warning=structural_warning,
    )
