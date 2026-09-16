"""S2-P2 STEP-5 — dots and the one ranking authority (R6, R7, §L52-b).

    card_score = round(conviction × proximity × 100)
    conviction = mean(tapped trader grades) ÷ 10, null with no taps
    proximity  = clamp(1 − |last − trigger| ÷ (3 × |trigger − stop|), 0, 1)

Computed dots are SHADOW: graded through `card.curves`, stored with WHY,
never in conviction (R6). Judgment dots are hollow until tapped — no
neutral 5.
"""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from cobalt.aset.models import Grade
from cobalt.cards import scoring
from cobalt.cards.scoring import (
    DESK_FACTORS,
    Dot,
    FactorObservation,
    card_score,
    compute_dots,
    conviction,
    dot_colour,
    grade_from_curve,
    proposed_key,
    proximity,
    refresh_dots,
    score_card,
    suppression,
)
from cobalt.settings.card import Curve, ProposedKeyBands
from cobalt.taxonomy.trade_def import QualityFactor

AT = datetime(2026, 1, 6, 16, 30, tzinfo=timezone.utc)
LATER = datetime(2026, 1, 6, 16, 45, tzinfo=timezone.utc)

FACTORS = [
    QualityFactor(name="rvol", source="cobalt", tier="deterministic", why_template="RVOL {value} → {grade}"),
    QualityFactor(name="atrs_from_open", source="cobalt", tier="deterministic"),
    QualityFactor(name="trail_fit", source="cobalt", tier="deterministic"),
    QualityFactor.model_validate("tape_read"),
    QualityFactor.model_validate("setup_relation"),
    QualityFactor.model_validate("market_alignment"),
    QualityFactor.model_validate("sector_alignment"),
]

CURVES = {
    "rvol": Curve.model_validate([[1, 1], [3, 6], [10, 10]]),
    "atrs_from_open": Curve.model_validate([[0.5, 2], [2.5, 9]]),
}


def _obs(**kw):
    return {
        "rvol": FactorObservation(value=Decimal("4.4"), inputs={"rvol": "4.4"}, formula="rvol@screen"),
        "atrs_from_open": FactorObservation(value=Decimal("1.5"), inputs={"atr": "0.1"}, formula="|last-open|/atr14"),
        **kw,
    }


def _dots(observations=None, curves=CURVES):
    return compute_dots(FACTORS, observations or _obs(), curves, at=AT)


def _by(dots):
    return {d.factor: d for d in dots}


def test_computable_dots_scored_1_to_10_with_why_held_in_shadow():
    dots = _by(_dots())
    rvol = dots["rvol"]
    assert rvol.role == "shadow" and rvol.source == "cobalt" and rvol.tier == "deterministic"
    # 4.4 between (3,6) and (10,10): 6 + 1.4 × 4/7 = 6.8 → 7 (half-up once)
    assert rvol.engine_value == Decimal("4.4") and rvol.engine_grade == 7
    assert rvol.engine_why == "RVOL 4.4 → 7"
    # the grade replays from the row: measured inputs + the curve + the unrounded grade (L57)
    assert rvol.engine_inputs == {
        "rvol": "4.4", "curve": [["1", "1"], ["3", "6"], ["10", "10"]], "unrounded_grade": "6.8",
    }
    assert rvol.engine_formula == "rvol@screen"
    atr = dots["atrs_from_open"]
    assert 1 <= atr.engine_grade <= 10 and atr.engine_why
    assert [d.position for d in _dots()] == list(range(len(FACTORS)))
    # shadow grades never reach conviction
    assert conviction(_dots()) is None


def test_curve_math_clips_and_rounds_half_up_once():
    curve = Curve.model_validate([[0, 1], [10, 10]])
    assert grade_from_curve(Decimal("-5"), curve) == (Decimal("1"), 1)
    assert grade_from_curve(Decimal("50"), curve) == (Decimal("10"), 10)
    unrounded, grade = grade_from_curve(Decimal("5"), curve)
    assert unrounded == Decimal("5.5") and grade == 6
    assert grade_from_curve(Decimal("4.5"), curve)[1] == 5  # 5.05 → 5


def test_missing_anchors_are_curve_unset_and_a_manual_factor_is_na():
    dots = _by(_dots(curves={}))
    assert dots["rvol"].na_reason == "curve_unset" and dots["rvol"].engine_grade is None
    assert dots["rvol"].engine_value == Decimal("4.4")
    assert dots["trail_fit"].na_reason == "MANUAL" and dots["trail_fit"].engine_value is None
    assert _by(_dots(curves=None))["rvol"].na_reason == "curve_unset"


def test_judgment_dots_hollow_until_tapped_no_neutral_5():
    dots = _by(_dots())
    for name in ("tape_read", "setup_relation"):
        dot = dots[name]
        assert dot.role == "human" and dot.source == "human"
        assert dot.engine_grade is None and dot.trader_grade is None and dot.engine_value is None
        assert dot.na_reason is None


def test_desk_dots_are_shadow_na_until_ruled():
    dots = _by(compute_dots(
        [*FACTORS, QualityFactor.model_validate("catalyst")], _obs(), CURVES, at=AT,
    ))
    assert DESK_FACTORS == frozenset({"catalyst", "market_alignment", "sector_alignment"})
    assert dots["catalyst"].na_reason == "DESK_NA"
    assert dots["market_alignment"].na_reason == "DEFAULT_UNRULED"
    assert dots["sector_alignment"].na_reason == "DEFAULT_UNRULED"
    for name in DESK_FACTORS:
        assert dots[name].role == "shadow" and dots[name].source == "cobalt-degraded"
        assert dots[name].engine_grade is None
        assert dots[name].engine_why.startswith("desk shadow: n/a")


def test_empty_tapped_set_conviction_null_never_zero():
    dots = _dots()
    assert conviction(dots) is None
    tapped = [d.model_copy(update={"trader_grade": 8, "tapped_at": AT}) if d.factor == "tape_read" else d for d in dots]
    assert conviction(tapped) == Decimal("0.8")
    both = [d.model_copy(update={"trader_grade": 5, "tapped_at": AT}) if d.factor == "rvol" else d for d in tapped]
    assert conviction(both) == Decimal("0.65")


def test_missing_required_computed_dot_suppresses_card_score_until_tapped():
    dots = _dots()
    reason = suppression(dots)
    assert reason and "trail_fit" in reason and "MANUAL" in reason
    tapped = [
        d.model_copy(update={"trader_grade": 6, "tapped_at": AT}) if d.factor in {"trail_fit", "tape_read"} else d
        for d in dots
    ]
    assert suppression(tapped) is None
    score = score_card(tapped, last=Decimal("2.35"), trigger=Decimal("2.50"), stop=Decimal("2.60"),
                       bands=None, enabled=[Grade.A, Grade.B])
    assert score.score_suppressed is None and score.card_score == 30  # 0.6 × 0.5 × 100
    untapped = score_card(dots, last=Decimal("2.55"), trigger=Decimal("2.50"), stop=Decimal("2.60"),
                          bands=None, enabled=[Grade.A])
    assert untapped.card_score is None and untapped.score_suppressed


def test_expired_required_input_suppresses_fresh_grade_history_labelled():
    first = _dots()
    tapped = [d.model_copy(update={"trader_grade": 7, "tapped_at": AT}) if d.factor in {"trail_fit", "tape_read"} else d
              for d in first]
    stale = compute_dots(
        FACTORS,
        _obs(rvol=FactorObservation(value=Decimal("5"), stale=True, inputs={"rvol": "5"}, formula="rvol@screen")),
        CURVES, at=LATER,
    )
    merged = _by(refresh_dots(tapped, stale, at=LATER))
    rvol = merged["rvol"]
    assert rvol.engine_grade is None and rvol.na_reason == "input_stale"
    assert rvol.history[-1] == {
        "label": "input_stale", "at": LATER.isoformat(), "engine_value": "4.4", "engine_grade": 7,
    }
    assert suppression(list(merged.values())) and "rvol" in suppression(list(merged.values()))
    # taps survive a refresh
    assert merged["tape_read"].trader_grade == 7
    # a fresh read after the stale one clears the suppression, history kept
    fresh = _by(refresh_dots(list(merged.values()), _dots(), at=LATER))
    assert fresh["rvol"].engine_grade == 7 and fresh["rvol"].history == rvol.history


def test_card_score_is_round_conviction_times_proximity_times_100():
    assert proximity(last=Decimal("2.50"), trigger=Decimal("2.50"), stop=Decimal("2.60")) == Decimal("1")
    assert proximity(last=Decimal("2.65"), trigger=Decimal("2.50"), stop=Decimal("2.60")) == Decimal("0.5")
    assert proximity(last=Decimal("3.50"), trigger=Decimal("2.50"), stop=Decimal("2.60")) == Decimal("0")
    assert proximity(last=Decimal("2.51"), trigger=Decimal("2.50"), stop=Decimal("2.60")) == Decimal("0.966667")
    assert card_score(Decimal("0.75"), Decimal("0.5"), None) == 38  # 37.5 half-up
    assert card_score(Decimal("0.7"), Decimal("0.966667"), None) == 68
    assert card_score(None, Decimal("1"), None) is None
    assert card_score(Decimal("0.9"), Decimal("1"), "trail_fit: MANUAL") is None
    with pytest.raises(ValueError, match="trigger"):
        proximity(last=Decimal("1"), trigger=Decimal("2"), stop=Decimal("2"))


BANDS = ProposedKeyBands(a_plus_min=Decimal("0.9"), a_min=Decimal("0.8"), b_min=Decimal("0.6"), c_min=Decimal("0.4"))


def test_proposed_key_none_without_conviction_and_only_enabled_grades():
    enabled = [Grade.A, Grade.B, Grade.C]
    assert proposed_key(None, BANDS, enabled) == (None, "no conviction — tap to propose")
    assert proposed_key(Decimal("0.95"), None, enabled) == (None, "card.proposed_key bands unset")
    assert proposed_key(Decimal("0.95"), BANDS, enabled)[0] is Grade.A  # A+ met, not enabled → A
    assert proposed_key(Decimal("0.85"), BANDS, enabled)[0] is Grade.A
    assert proposed_key(Decimal("0.6"), BANDS, enabled)[0] is Grade.B
    assert proposed_key(Decimal("0.3"), BANDS, enabled) == (None, "below every band")
    key, reason = proposed_key(Decimal("0.7"), BANDS, [Grade.A])
    assert key is None and "nothing enabled" in reason


def test_dot_colours_from_the_tunable_thresholds():
    assert [dot_colour(g, red_max=3, amber_max=6) for g in (1, 3, 4, 6, 7, 10)] == [0, 0, 1, 1, 2, 2]
    assert dot_colour(None, red_max=3, amber_max=6) is None


def test_the_colour_thresholds_are_tunables_rows_with_consumers():
    from cobalt.taxonomy.loader import load_tunables

    rows = load_tunables().by_key
    assert rows["card.dot.red_max"].value == 3 and rows["card.dot.amber_max"].value == 6
    assert scoring.colour_thresholds(rows) == (3, 6)
    for key in ("card.dot.red_max", "card.dot.amber_max"):
        assert rows[key].consumers


def test_dot_rows_refuse_a_grade_outside_1_to_10_and_a_bad_role():
    with pytest.raises(ValueError):
        Dot(factor="x", position=0, source="human", tier="judgment", role="human", trader_grade=11)
    with pytest.raises(ValueError):
        Dot(factor="x", position=0, source="human", tier="judgment", role="neutral")
