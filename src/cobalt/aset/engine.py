"""Deterministic ASET sizing math. Pure functions — no I/O, no LLMs.

Math source of truth: docs/90 - References/aset_daily_position_sizer.html
(riskBudget = dailyStop × pct/100; shares = floor(riskBudget/distance))
and docs/90 - References/Daily_Stop_Model_Card.pdf (daily stop = account ÷ 50;
A+ 80 / A 30 / B 15 / C 5 / D-SAW 0).
"""

from decimal import Decimal

from .models import GRADE_RISK_PCT, Direction, Grade, SizingInput, SizingResult

CENTS = Decimal("0.01")
DAILY_STOP_DIVISOR = Decimal("50")


class SizingError(ValueError):
    """Invalid sizing input — fail loud, never guess."""


def enforce_broker_cap(daily_stop: Decimal, cap: Decimal) -> list[str]:
    """Broker hard cap: refuse above, warn at the cap exactly.

    Returns warnings to attach to the result; raises SizingError when the
    requested daily stop exceeds the cap (UI clamps, server refuses).
    """
    if daily_stop > cap:
        raise SizingError(
            f"Daily stop ${daily_stop} exceeds the broker hard cap ${cap} — refused."
        )
    if daily_stop == cap:
        return [f"Daily stop is AT the broker hard cap (${cap})."]
    return []


def daily_stop_from_account(account_size: Decimal) -> Decimal:
    """The ruled Daily-Stop Model law: account ÷ 50. Do not change this
    divisor — it's the TRIAGE/Daily-Stop-Model-card spec and is tested
    against the reference sizer's worked example."""
    if account_size <= 0:
        raise SizingError("account_size must be positive")
    return (account_size / DAILY_STOP_DIVISOR).quantize(CENTS)


# TEMPORARY OVERRIDE (Dejan, 2026-08-25, "for now"): when no
# daily_stop_default is configured, the sheet's prefill uses account ÷
# 100 instead of the ruled account ÷ 50. This does NOT change the ruled
# Daily-Stop Model law above — only the sheet's auto-fallback value when
# the morning stop hasn't been set explicitly. Revert to
# daily_stop_from_account (or remove this function) when the override
# is no longer wanted.
TEMP_PREFILL_DIVISOR = Decimal("100")


def temp_prefill_daily_stop(account_size: Decimal) -> Decimal:
    if account_size <= 0:
        raise SizingError("account_size must be positive")
    return (account_size / TEMP_PREFILL_DIVISOR).quantize(CENTS)


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
