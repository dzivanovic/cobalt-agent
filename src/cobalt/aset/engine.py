"""Deterministic ASET sizing math. Pure functions — no I/O, no LLMs.

Math source of truth: docs/references/aset_daily_position_sizer.html
(riskBudget = dailyStop × pct/100; shares = floor(riskBudget/distance))
and docs/references/Daily_Stop_Model_Card.pdf (daily stop = account ÷ 50;
A+ 80 / A 30 / B 15 / C 5 / D-SAW 0).
"""

from decimal import Decimal

from .models import GRADE_RISK_PCT, Direction, Grade, SizingInput, SizingResult

CENTS = Decimal("0.01")
DAILY_STOP_DIVISOR = Decimal("50")


class SizingError(ValueError):
    """Invalid sizing input — fail loud, never guess."""


def daily_stop_from_account(account_size: Decimal) -> Decimal:
    if account_size <= 0:
        raise SizingError("account_size must be positive")
    return (account_size / DAILY_STOP_DIVISOR).quantize(CENTS)


def compute_sizing(inp: SizingInput) -> SizingResult:
    distance = abs(inp.entry - inp.stop)
    if distance == 0:
        raise SizingError("Entry and stop cannot be the same price.")

    risk_pct = GRADE_RISK_PCT[inp.grade]
    risk_budget = inp.daily_stop * risk_pct / Decimal("100")
    shares = int(risk_budget / distance)
    used_risk = distance * shares

    is_long = inp.direction is Direction.LONG
    target_1r = inp.entry + distance if is_long else inp.entry - distance
    target_2r = inp.entry + distance * 2 if is_long else inp.entry - distance * 2

    warnings: list[str] = []
    if inp.grade is Grade.D_SAW:
        warnings.append("D/SAW grade = NO TRADE. Allocation is 0%.")
    if is_long and inp.stop >= inp.entry:
        warnings.append(
            "For a long trade the stop is normally below entry. Check the ASET plan."
        )
    if not is_long and inp.stop <= inp.entry:
        warnings.append(
            "For a short trade the stop is normally above entry. Check the ASET plan."
        )
    if shares < 1 and risk_budget > 0:
        warnings.append(
            "Position size rounds to zero: risk per share exceeds the allocated risk budget."
        )

    return SizingResult(
        input=inp,
        risk_pct=risk_pct,
        risk_budget=risk_budget.quantize(CENTS),
        per_share_risk=distance,
        shares=shares,
        used_risk=used_risk.quantize(CENTS),
        target_1r=target_1r.quantize(CENTS),
        target_2r=target_2r.quantize(CENTS),
        warnings=warnings,
    )
