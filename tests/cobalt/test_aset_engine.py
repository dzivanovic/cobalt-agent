"""Deterministic ASET engine tests.

Iteration 4 (ruled by Dejan, 2026-08-28): sheet-mode fixed-dollar risk
per grade, mirroring Dejan's DAS hotkey files (configs/cobalt/aset.yaml
full/half: A 135/70, B 60/30). Worked examples below use full-mode B
($60) unless noted, built from scratch rather than the retired
daily-stop x percentage reference sizer's worked example.

Config-completion follow-up (2026-08-28): `compute_sizing` takes
`enabled_grades` as an explicit argument rather than reading a
hardcoded constant — `ENABLED_GRADES` here mirrors the real config's
`enabled_grades: [A, B]` for every test except
`test_enabled_grades_is_config_driven`, which proves the claim that
enabling a grade is a config change, not a code change, by passing a
different set and watching the previously-tradeable grade B refuse
while the previously-disabled grade C computes.
"""

from decimal import Decimal

import pytest

from cobalt.aset.engine import (
    FILL_DISTANCE_WARNING_PCT,
    SizingError,
    compute_fill_recompute,
    compute_sizing,
)
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput

ENABLED_GRADES = (Grade.A, Grade.B)


def make_input(**overrides):
    base = dict(
        ticker="NVDA",
        grade=Grade.B,
        direction=Direction.SHORT,
        sheet_mode=SheetMode.FULL,
        risk_dollars=Decimal("60"),
        entry=Decimal("49"),
        stop=Decimal("50.09"),
    )
    base.update(overrides)
    return SizingInput(**base)


def size(enabled_grades=ENABLED_GRADES, **overrides):
    return compute_sizing(make_input(**overrides), enabled_grades)


def test_full_mode_b_worked_example():
    # distance 1.09, budget 60 -> 55 shares (60/1.09 floored), used 59.95
    r = size()
    assert r.risk_budget == Decimal("60.00")
    assert r.per_share_risk == Decimal("1.09")
    assert r.shares == 55
    assert r.used_risk == Decimal("59.95")
    assert r.target_1r == Decimal("47.91")
    assert r.target_2r == Decimal("46.82")
    assert r.warnings == []


@pytest.mark.parametrize(
    "grade,dollars,shares",
    [
        (Grade.A, "135", 123),  # 135 / 1.09 floored
        (Grade.B, "60", 55),  # 60 / 1.09 floored
    ],
)
def test_grade_dollar_map_full_mode(grade, dollars, shares):
    r = size(grade=grade, risk_dollars=Decimal(dollars))
    assert r.risk_budget == Decimal(dollars).quantize(Decimal("0.01"))
    assert r.shares == shares


@pytest.mark.parametrize("grade", [Grade.C, Grade.D_SAW])
def test_non_enabled_grades_refuse_to_compute(grade):
    with pytest.raises(SizingError, match="not enabled"):
        size(grade=grade, risk_dollars=Decimal("1"))


def test_a_plus_is_reserved_and_not_enabled():
    with pytest.raises(SizingError, match="not enabled"):
        size(grade=Grade.A_PLUS, risk_dollars=Decimal("1"))


def test_d_saw_risk_dollars_is_always_zero_and_still_refuses():
    # D's real configured dollar figure is 0 (SAW principle) — refusal
    # is about enabled_grades, not about risk_dollars being non-positive.
    with pytest.raises(SizingError, match="not enabled"):
        size(grade=Grade.D_SAW, risk_dollars=Decimal("0"))


def test_enabled_grades_is_config_driven_not_hardcoded():
    # Prove enabling/disabling a grade is purely a matter of what's
    # passed in — no code path treats A/B as structurally special.
    with pytest.raises(SizingError, match="not enabled"):
        size(enabled_grades=(Grade.C,), grade=Grade.B, risk_dollars=Decimal("60"))
    r = size(enabled_grades=(Grade.C,), grade=Grade.C, risk_dollars=Decimal("21"))
    assert r.risk_budget == Decimal("21.00")


def test_equal_entry_and_stop_fails_loud():
    with pytest.raises(SizingError):
        size(stop=Decimal("49"))


def test_long_targets_project_upward():
    r = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
    assert r.target_1r == Decimal("101.00")
    assert r.target_2r == Decimal("102.00")
    assert r.warnings == []


def test_long_with_stop_above_entry_warns():
    r = size(direction=Direction.LONG)  # stop 50.09 > entry 49
    assert any("long" in w.lower() for w in r.warnings)


def test_short_with_stop_below_entry_warns():
    r = size(stop=Decimal("48"))
    assert any("short" in w.lower() for w in r.warnings)


def test_size_rounding_to_zero_warns():
    r = size(
        grade=Grade.B,
        risk_dollars=Decimal("5"),
        direction=Direction.LONG,
        entry=Decimal("50"),
        stop=Decimal("40"),
    )  # budget 5.00, distance 10 -> 0 shares
    assert r.shares == 0
    assert any("rounds to zero" in w for w in r.warnings)


def test_ticker_normalized_and_blank_rejected():
    assert make_input(ticker=" nvda ").ticker == "NVDA"
    with pytest.raises(ValueError):
        make_input(ticker="   ")


def test_half_mode_dollars_differ_from_full():
    full = size(sheet_mode=SheetMode.FULL, risk_dollars=Decimal("60"))
    half = size(sheet_mode=SheetMode.HALF, risk_dollars=Decimal("30"))
    assert full.risk_budget == Decimal("60.00")
    assert half.risk_budget == Decimal("30.00")
    assert half.shares < full.shares


class TestFillRecompute:
    def test_recompute_at_actual_fill(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        fill = compute_fill_recompute(original, actual_fill=Decimal("100.20"))
        # new distance 1.20 vs planned 1.00 -> 60 shares (60/1.20 floored)
        assert fill.recomputed_shares == 50
        assert fill.recomputed_used_risk == Decimal("60.00")
        assert fill.share_delta == fill.recomputed_shares - original.shares

    def test_small_distance_change_no_warning(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        fill = compute_fill_recompute(original, actual_fill=Decimal("100.05"))
        assert fill.distance_change_pct < FILL_DISTANCE_WARNING_PCT
        assert fill.structural_warning is None

    def test_large_distance_change_warns_not_structural(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        fill = compute_fill_recompute(original, actual_fill=Decimal("101.50"))  # distance 2.50 vs 1.00 = 150%
        assert fill.distance_change_pct >= FILL_DISTANCE_WARNING_PCT
        assert fill.structural_warning == "stop may no longer be structural — re-read the level."

    def test_actual_fill_must_be_positive(self):
        original = size()
        with pytest.raises(SizingError):
            compute_fill_recompute(original, actual_fill=Decimal("0"))

    def test_actual_fill_equal_to_stop_fails_loud(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        with pytest.raises(SizingError):
            compute_fill_recompute(original, actual_fill=Decimal("99"))
