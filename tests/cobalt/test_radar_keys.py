"""S2-P2 STEP-6 — the ladder keys, snap DOWN only (R8), through the one
`aset/engine.py` path.

Dollars and enabled grades come from the hub-cut real-shape settings
fixture (`tests/fixtures/radar/card-settings.real-shape.json`, the live
`trader_settings` rows with nothing invented): full B 60 / A 135, half
B 30 / A 70, account and reduced ladders [A, B, C], today's rung
`reduced` (= the half sheet).
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.aset.engine import (
    KeyRefused,
    SizingError,
    key_ladder,
    size_at_key,
    snap_down,
    stop_distance,
)
from cobalt.aset.models import Direction, Grade
from cobalt.settings.models import TraderSettings

FIXTURE = Path("tests/fixtures/radar/card-settings.real-shape.json")


@pytest.fixture(scope="module")
def settings() -> TraderSettings:
    rows = {row["key"]: row["value"] for row in json.loads(FIXTURE.read_text())}
    return TraderSettings._build(rows, where="card-settings fixture")


def _today(settings: TraderSettings):
    mode = settings.daymode.lowest_enabled
    return mode, settings.daymode.sheet_for(mode), settings.daymode.enabled_grades_for(mode)


def test_keys_fixed_dollars_per_sheet_disabled_greyed_with_would_be_dollars(settings):
    enabled = settings.daymode.enabled_grades_for("reduced")
    full = {k.grade: k for k in key_ladder(settings.sheet_modes, "full", enabled)}
    half = {k.grade: k for k in key_ladder(settings.sheet_modes, "half", enabled)}
    assert [k.grade for k in key_ladder(settings.sheet_modes, "half", enabled)] == [
        Grade.A_PLUS, Grade.A, Grade.B, Grade.C,
    ]
    assert full[Grade.B].dollars == Decimal("60") and full[Grade.A].dollars == Decimal("135")
    assert half[Grade.B].dollars == Decimal("30") and half[Grade.A].dollars == Decimal("70")
    # A+ is not enabled: greyed, but still carries the dollars it WOULD size.
    assert half[Grade.A_PLUS].enabled is False
    assert half[Grade.A_PLUS].dollars == Decimal("170")
    assert full[Grade.A_PLUS].dollars == Decimal("345")
    assert all(half[g].enabled for g in (Grade.A, Grade.B, Grade.C))


def test_a_plus_tap_on_half_day_records_a_plus_and_sizes_at_a_70_with_notice(settings):
    mode, sheet, enabled = _today(settings)
    assert sheet == "half"
    sized = size_at_key(
        Grade.A_PLUS, ticker="FTFT", entry=Decimal("2.50"), stop=Decimal("2.60"),
        direction=Direction.SHORT, sheet_modes=settings.sheet_modes, sheet=sheet,
        enabled=enabled, max_stop_distance_pct=Decimal("10"),
    )
    assert sized.tapped_grade is Grade.A_PLUS
    assert sized.sized_grade is Grade.A
    assert sized.result.risk_budget == Decimal("70.00")
    assert sized.result.input.grade is Grade.A
    assert sized.result.shares == 700
    assert sized.snap_notice and "A+" in sized.snap_notice and "A" in sized.snap_notice
    assert "70" in sized.snap_notice


def test_tap_snaps_down_only_refuses_when_nothing_enabled_below(settings):
    enabled = [Grade.A, Grade.B]
    assert snap_down(Grade.B, enabled) == (Grade.B, None)
    sized, notice = snap_down(Grade.A_PLUS, enabled)
    assert sized is Grade.A and notice
    # Never UP: C with only A/B enabled has nothing below it.
    sized, notice = snap_down(Grade.C, enabled)
    assert sized is None and "nothing enabled below" in notice
    with pytest.raises(KeyRefused, match="nothing enabled below"):
        size_at_key(
            Grade.C, ticker="FTFT", entry=Decimal("2.50"), stop=Decimal("2.40"),
            direction=Direction.LONG, sheet_modes=settings.sheet_modes, sheet="half",
            enabled=enabled, max_stop_distance_pct=Decimal("10"),
        )


def test_snap_down_skips_a_disabled_middle_key_and_never_lands_on_d():
    sized, notice = snap_down(Grade.A_PLUS, [Grade.B, Grade.D_SAW])
    assert sized is Grade.B and "B" in notice
    sized, _ = snap_down(Grade.C, [Grade.D_SAW])
    assert sized is None


def test_a_key_that_is_not_a_ladder_key_is_refused():
    with pytest.raises(KeyRefused, match="not a ladder key"):
        snap_down(Grade.D_SAW, [Grade.D_SAW])


def test_stop_distance_keeps_the_side_check_and_needs_no_budget():
    assert stop_distance(entry=Decimal("2.50"), stop=Decimal("2.60"), direction=Direction.SHORT) == Decimal("0.10")
    with pytest.raises(SizingError, match="Short stop"):
        stop_distance(entry=Decimal("2.50"), stop=Decimal("2.40"), direction=Direction.SHORT)
    with pytest.raises(SizingError, match="Long stop"):
        stop_distance(entry=Decimal("2.50"), stop=Decimal("2.60"), direction=Direction.LONG)
