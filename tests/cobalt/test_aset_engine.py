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
MAX_STOP_DISTANCE_PCT = Decimal("10")
MAX_FILL_DISTANCE_PCT = Decimal("5")


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


def size(enabled_grades=ENABLED_GRADES, max_stop_distance_pct=MAX_STOP_DISTANCE_PCT, **overrides):
    return compute_sizing(make_input(**overrides), enabled_grades, max_stop_distance_pct)


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
    # entry == stop is a wrong-side stop for both directions (SHORT here
    # requires stop > entry strictly) — refused at model construction,
    # not a SizingError from the engine.
    with pytest.raises(ValueError, match="Short stop"):
        size(stop=Decimal("49"))


def test_long_targets_project_upward():
    r = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
    assert r.target_1r == Decimal("101.00")
    assert r.target_2r == Decimal("102.00")
    assert r.warnings == []


def test_long_with_stop_above_entry_is_refused():
    # Slice 2.1a: this used to be a warning (r.warnings), now a hard
    # reject at construction — fail-loud, not warn-and-write.
    with pytest.raises(ValueError, match="Long stop"):
        make_input(direction=Direction.LONG)  # stop 50.09 > entry 49


def test_short_with_stop_below_entry_is_refused():
    with pytest.raises(ValueError, match="Short stop"):
        make_input(stop=Decimal("48"))


def test_size_rounding_to_zero_warns():
    r = size(
        grade=Grade.B,
        risk_dollars=Decimal("5"),
        direction=Direction.LONG,
        entry=Decimal("50"),
        stop=Decimal("40"),
        # distance 10/50 = 20% would trip the stop-distance typo guard at
        # the default 10% — widen it here since this test is about the
        # unrelated shares-rounds-to-zero warning.
        max_stop_distance_pct=Decimal("50"),
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
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("100.20"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
        )
        # new distance 1.20 vs planned 1.00 -> 60 shares (60/1.20 floored)
        assert fill.recomputed_shares == 50
        assert fill.recomputed_used_risk == Decimal("60.00")
        assert fill.share_delta == fill.recomputed_shares - original.shares

    def test_small_distance_change_no_warning(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("100.05"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
        )
        assert fill.distance_change_pct < FILL_DISTANCE_WARNING_PCT
        assert fill.structural_warning is None

    def test_large_distance_change_warns_not_structural(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("101.50"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
        )  # distance 2.50 vs 1.00 = 150% (fill is only 1.5% from entry — passes the hard floor)
        assert fill.distance_change_pct >= FILL_DISTANCE_WARNING_PCT
        assert fill.structural_warning == "stop may no longer be structural — re-read the level."

    def test_actual_fill_must_be_positive(self):
        original = size()
        with pytest.raises(SizingError):
            compute_fill_recompute(
                original, actual_fill=Decimal("0"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
            )

    def test_actual_fill_equal_to_stop_fails_loud(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        with pytest.raises(SizingError):
            compute_fill_recompute(
                original, actual_fill=Decimal("99"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
            )


class TestStopDistanceTypoGuard:
    """D3 (2026-08-31): PCG SHORT entry 13.379, stop 17.72 — a 32% stop
    distance (near-certainly a 13.72 typo) went unflagged. Correct side
    (short: stop above entry), just absurdly far — the side check alone
    doesn't catch this."""

    def test_stop_within_default_band_computes(self):
        r = size(entry=Decimal("49"), stop=Decimal("50.09"))  # 2.22%
        assert r.shares > 0

    def test_stop_beyond_default_band_refused(self):
        with pytest.raises(SizingError, match="typo guard"):
            size(entry=Decimal("49"), stop=Decimal("60"))  # 22.4% > 10% default

    def test_threshold_is_config_driven_not_hardcoded(self):
        # Same distance refused at the tight default, accepted once the
        # caller-supplied threshold (standing in for configs/dev/aset.yaml
        # validation.max_stop_distance_pct) is widened — proves the guard
        # takes its ceiling from the caller, not a baked-in constant.
        with pytest.raises(SizingError, match="typo guard"):
            size(entry=Decimal("49"), stop=Decimal("60"), max_stop_distance_pct=Decimal("10"))
        r = size(entry=Decimal("49"), stop=Decimal("60"), max_stop_distance_pct=Decimal("30"))
        assert r.shares > 0

    def test_pcg_09_40_06_fixture_refused(self):
        # Real 2026-08-31 defect: SHORT, entry 13.379, stop 17.72 (~32.4%
        # from entry) — correct side, absurd distance. Must refuse.
        with pytest.raises(SizingError, match="typo guard"):
            size(
                ticker="PCG",
                direction=Direction.SHORT,
                entry=Decimal("13.379"),
                stop=Decimal("17.72"),
            )


class TestFillDistanceTypoGuard:
    """D2 (2026-08-31): a 2518.91 fill entered against an NVDA card with
    entry 218.595 computed distance_change_pct 330980.58 and recomputed
    shares to 0 — and was PERSISTED, twice, before the real fill (218.91)
    came in. This is a hard floor beneath the existing >=25%
    distance_change_pct WARNING, not a replacement for it."""

    def test_fill_within_default_band_recomputes(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("102"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
        )  # 2% from entry
        assert fill.recomputed_shares >= 0

    def test_fill_beyond_default_band_refused(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        with pytest.raises(SizingError, match="typo guard"):
            compute_fill_recompute(
                original, actual_fill=Decimal("110"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
            )  # 10% from entry > 5% default

    def test_threshold_is_config_driven_not_hardcoded(self):
        original = size(direction=Direction.LONG, entry=Decimal("100"), stop=Decimal("99"))
        with pytest.raises(SizingError, match="typo guard"):
            compute_fill_recompute(original, actual_fill=Decimal("110"), max_fill_distance_pct=Decimal("5"))
        fill = compute_fill_recompute(original, actual_fill=Decimal("110"), max_fill_distance_pct=Decimal("15"))
        assert fill.recomputed_shares >= 0

    def test_nvda_absurd_fill_fixture_refused(self):
        # Real 2026-08-31 defect: NVDA card entry 218.595, fat-fingered
        # fill 2518.91 (an extra digit) — must refuse before anything is
        # recomputed or written.
        original = size(
            ticker="NVDA",
            direction=Direction.LONG,
            entry=Decimal("218.595"),
            stop=Decimal("217.90"),
        )
        with pytest.raises(SizingError, match="typo guard"):
            compute_fill_recompute(
                original, actual_fill=Decimal("2518.91"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
            )

    def test_nvda_corrected_fill_fixture_accepted(self):
        # The correct fill (218.91) that followed, same card — must pass.
        original = size(
            ticker="NVDA",
            direction=Direction.LONG,
            entry=Decimal("218.595"),
            stop=Decimal("217.90"),
        )
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("218.91"), max_fill_distance_pct=MAX_FILL_DISTANCE_PCT
        )
        assert fill.recomputed_shares >= 0


class TestDefect4NoCrossCardStateBleed:
    """Defect 4 (2026-09-01): card 2 (same ticker, different entry/stop/
    risk than card 1) showed a stop-validity warning despite computing
    the correct share size for its own risk. Confirmed root cause: not
    a validator reading stale state (compute_sizing/SizingInput are
    pure functions of their own arguments — nothing here is
    module-level or cached), but Defect 3's web-layer bug leaving card
    1's stale ENTRY in the form while Dejan typed card 2's new STOP, so
    the (mismatched) entry/stop pair the server actually received
    legitimately tripped the check. Defect 3's fix (full field reset on
    ticker blur) removes the vector entirely. This test proves the
    engine layer itself was never the culprit: two consecutive computes
    on the same ticker with unrelated inputs are fully independent."""

    def test_second_card_unaffected_by_first_cards_inputs(self):
        # Card 1: a stop that would fail the typo guard / structural
        # checks if it ever leaked into another computation.
        card1 = size(
            ticker="TSLA",
            direction=Direction.LONG,
            entry=Decimal("358.97"),
            stop=Decimal("356.00"),
        )
        assert card1.warnings == []

        # Card 2: same ticker, deliberately different entry/stop/risk —
        # clean inputs that must produce zero warnings on their own,
        # regardless of card 1 having just run.
        card2 = size(
            ticker="TSLA",
            direction=Direction.SHORT,
            entry=Decimal("358.55"),
            stop=Decimal("359.75"),
            risk_dollars=Decimal("30"),
        )
        assert card2.warnings == []
        assert card2.shares > 0

    def test_many_sequential_computes_never_accumulate_warnings(self):
        # Guards against any future module-level/cached state creeping
        # in: run a long sequence of clean same-ticker cards and assert
        # none of them ever pick up a warning from a neighbor.
        for i in range(20):
            entry = Decimal("100") + i
            stop = entry - Decimal("1")
            result = size(ticker="TSLA", direction=Direction.LONG, entry=entry, stop=stop)
            assert result.warnings == []
