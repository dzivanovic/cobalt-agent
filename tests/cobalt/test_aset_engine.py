"""Deterministic ASET engine tests.

Worked example values come from the reference implementation defaults in
docs/references/aset_daily_position_sizer.html (daily stop 1000, grade A
30%, short, entry 49, stop 50.09 → 275 shares, used risk 299.75).
"""

from decimal import Decimal

import pytest

from cobalt.aset.engine import (
    SizingError,
    compute_sizing,
    daily_stop_from_account,
    temp_prefill_daily_stop,
)
from cobalt.aset.models import Direction, Grade, SizingInput


def make_input(**overrides):
    base = dict(
        ticker="NVDA",
        grade=Grade.A,
        direction=Direction.SHORT,
        daily_stop=Decimal("1000"),
        entry=Decimal("49"),
        stop=Decimal("50.09"),
    )
    base.update(overrides)
    return SizingInput(**base)


def test_daily_stop_is_account_over_50():
    assert daily_stop_from_account(Decimal("10000")) == Decimal("200.00")
    assert daily_stop_from_account(Decimal("25000")) == Decimal("500.00")


def test_daily_stop_rejects_non_positive_account():
    with pytest.raises(SizingError):
        daily_stop_from_account(Decimal("0"))


def test_temp_prefill_is_account_over_100():
    # TEMP override (2026-08-25, "for now"): sheet fallback only,
    # separate from the ruled account/50 law tested above.
    assert temp_prefill_daily_stop(Decimal("10000")) == Decimal("100.00")
    assert temp_prefill_daily_stop(Decimal("43000")) == Decimal("430.00")


def test_temp_prefill_rejects_non_positive_account():
    with pytest.raises(SizingError):
        temp_prefill_daily_stop(Decimal("0"))


def test_reference_worked_example_short_grade_a():
    r = compute_sizing(make_input())
    assert r.risk_pct == Decimal("30")
    assert r.risk_budget == Decimal("300.00")
    assert r.per_share_risk == Decimal("1.09")
    assert r.shares == 275
    assert r.used_risk == Decimal("299.75")
    assert r.target_1r == Decimal("47.91")
    assert r.target_2r == Decimal("46.82")
    assert r.warnings == []


@pytest.mark.parametrize(
    "grade,pct,shares",
    [
        (Grade.A_PLUS, "80", 733),  # 800 / 1.09 floored
        (Grade.A, "30", 275),
        (Grade.B, "15", 137),  # 150 / 1.09 floored
        (Grade.C, "5", 45),  # 50 / 1.09 floored
        (Grade.D_SAW, "0", 0),
    ],
)
def test_grade_risk_map(grade, pct, shares):
    r = compute_sizing(make_input(grade=grade))
    assert r.risk_pct == Decimal(pct)
    assert r.shares == shares


def test_d_saw_grade_is_no_trade_with_warning():
    r = compute_sizing(make_input(grade=Grade.D_SAW))
    assert r.shares == 0
    assert r.used_risk == Decimal("0.00")
    assert any("NO TRADE" in w for w in r.warnings)


def test_equal_entry_and_stop_fails_loud():
    with pytest.raises(SizingError):
        compute_sizing(make_input(stop=Decimal("49")))


def test_long_targets_project_upward():
    r = compute_sizing(
        make_input(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
    )
    assert r.target_1r == Decimal("101.00")
    assert r.target_2r == Decimal("102.00")
    assert r.warnings == []


def test_long_with_stop_above_entry_warns():
    r = compute_sizing(make_input(direction=Direction.LONG))  # stop 50.09 > entry 49
    assert any("long" in w.lower() for w in r.warnings)


def test_short_with_stop_below_entry_warns():
    r = compute_sizing(make_input(stop=Decimal("48")))
    assert any("short" in w.lower() for w in r.warnings)


def test_size_rounding_to_zero_warns():
    r = compute_sizing(
        make_input(
            grade=Grade.C,
            daily_stop=Decimal("100"),
            direction=Direction.LONG,
            entry=Decimal("50"),
            stop=Decimal("40"),
        )
    )  # budget 5.00, distance 10 → 0 shares
    assert r.shares == 0
    assert any("rounds to zero" in w for w in r.warnings)


def test_broker_cap_refuses_above():
    from cobalt.aset.engine import enforce_broker_cap

    with pytest.raises(SizingError, match="broker hard cap"):
        enforce_broker_cap(Decimal("450"), Decimal("430"))


def test_broker_cap_warns_at_cap_and_silent_below():
    from cobalt.aset.engine import enforce_broker_cap

    assert enforce_broker_cap(Decimal("430"), Decimal("430")) == [
        "Daily stop is AT the broker hard cap ($430)."
    ]
    assert enforce_broker_cap(Decimal("200"), Decimal("430")) == []


def test_ticker_normalized_and_blank_rejected():
    assert make_input(ticker=" nvda ").ticker == "NVDA"
    with pytest.raises(ValueError):
        make_input(ticker="   ")
