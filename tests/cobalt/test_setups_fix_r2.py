"""The setups fix, round 2 (prompt `15-setups-fix.md`) — the FIX rows' tests.

- F1: a def whose preconditions name no anchor object is NOT evaluable,
  named `anchor:none` (the registry reads `ANCHORS`, the table formation
  dispatches through — L3).
- F2: a `sequence` walks its steps as predicates, in bar order, through the
  one interpreter's dispatch; an unserved step names its own gap.
- F3: a key the trigger resolver reads joins the def's declared closure, so
  an assumed fill of it reaches `assumed_keys` and the card's dot.
- P1 (coverage): a single-sentence relation used outside its served sentence
  is reported not evaluable, named `Unsupported(<word>:…)`, never silent.

Neutral defs of this file's own words and literals (L32 / L69), written into
a `tmp_path` vault and loaded through the real `load_vault_trade_defs`
(`setups_shapes.load_note`). Bars, daily bars and settings are the committed
real-shape radar fixtures (L45).
"""

from __future__ import annotations

from datetime import timedelta

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.radar.anatomy.registry import evaluability

# =====================================================================
# F1 — anchors: `evaluability` names `anchor:none`
# =====================================================================


def _indicator_stop(indicator: str) -> dict:
    return {"type": "indicator", "indicator": indicator,
            "buffer": {"type": "fixed", "cents": {"value": "cfg(stop.buffer)", "dynamic": False}},
            "snapshot": "at_entry"}


def no_anchor_mapping() -> dict:
    """Existing bricks only, and no anchor object among them: the pool
    admission, price above the VWAP and above the EMA21; a 4-bar `bar_break`;
    the VWAP stop at entry."""
    mapping = shapes.example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"}],
        preconditions=[{"expr": "InPlay.state == active"}, {"expr": "price > VWAP"}, {"expr": "price > EMA21"}],
        avoid=[{"text": "a human read, this file's words"}],
        trigger={"type": "bar_break", "params": {"bars_cleared": 4, "direction": "any"},
                 "confirmation_policy": {"type": "intrabar"}},
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning"],
        preferred_windows_ref="anatomy: above both lines",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"] = _indicator_stop("VWAP")
    return mapping


@pytest.fixture(scope="module")
def no_anchor(tmp_path_factory):
    return shapes.load_note(tmp_path_factory.mktemp("no-anchor"), "example-fix-no-anchor", no_anchor_mapping())


def test_f1_a_def_with_no_anchor_object_is_not_evaluable_named_anchor_none(no_anchor):
    result = evaluability(no_anchor.definition)
    assert result.evaluable is False
    assert result.missing_atoms == ("anchor:none",)


def test_f1_evaluate_member_reports_not_evaluable_naming_anchor_none_on_the_committed_day(no_anchor):
    for m in range(0, 391, 30):
        ev = shapes.evaluate(no_anchor, "FTFT", shapes.DAY_START + timedelta(minutes=m))
        assert ev.evaluation == "not_evaluable" and "anchor:none" in ev.missing, (m, ev.evaluation, ev.note)


# =====================================================================
# F2 — `sequence` evaluates its steps through the one interpreter
# =====================================================================


def break_then_turn_mapping(steps: list[dict]) -> dict:
    """A RangeBreak-anchored def (the level break accepted, a retest on that
    RangeBreak) whose trigger is a `sequence` of `steps`; the VWAP stop at
    entry. This file's words."""
    mapping = shapes.example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"}],
        preconditions=[{"expr": "RangeBreak(level).state == accepted"},
                       {"expr": "event(retest) on that RangeBreak"}],
        avoid=[{"text": "a human read of the break, this file's words"}],
        trigger={"type": "sequence", "steps": steps},
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning"],
        preferred_windows_ref="anatomy: after the break",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"] = _indicator_stop("VWAP")
    return mapping


TWO_STEPS = [
    {"name": "through", "predicate": {"expr": "price close_through Level_ref"},
     "confirmation_policy": {"type": "close_through"}},
    {"name": "higher", "predicate": {"expr": "close_above(prior_bar)"},
     "confirmation_policy": {"type": "close_through"}},
]


@pytest.fixture(scope="module")
def two_step(tmp_path_factory):
    return shapes.load_note(tmp_path_factory.mktemp("two-step"), "example-fix-two-step",
                            break_then_turn_mapping(TWO_STEPS), engine=shapes.D6_CONSTRUCTED)


def test_f2_a_sequence_other_than_the_three_step_one_is_evaluable(two_step):
    result = evaluability(two_step.definition)
    assert result.evaluable, result.missing_atoms


def _evaluate_series(ld, bars):
    import test_setups_second_chance as sc
    from cobalt.radar.evaluate import evaluate_member
    from cobalt.session import session_clock

    return evaluate_member(ld, sc._member(bars, sc._scan_after(bars)), tunables=shapes.tunables_for(ld),
                           defaults=sup.defaults(), scan_interval=100, clock=session_clock())


def test_f2_the_two_step_sequence_forms_on_the_first_bar_after_the_break_that_closes_above_the_prior_bar(two_step):
    """The break-retest-turn day of `test_setups_second_chance.py` (read, not
    edited): the break bucket (09:36 ET, high 10.14) closes through the 10.05
    level; the NEXT bucket (09:38 ET) closes 10.18 above that high — step 2's
    bar, the trigger bar; its close the trigger price."""
    from decimal import Decimal

    import test_setups_second_chance as sc

    ev = _evaluate_series(two_step, sc.break_retest_turn())
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.missing, ev.note,
                                                                  ev.by_side["long"].note)
    f = ev.formation
    assert f.trigger_outcome.kind == "sequence"
    assert f.trigger.price == Decimal("10.18") and f.trigger_outcome.ref_bar_ts == sc._et(9, 38)
    assert f.trigger.bar_ts == (sc._et(9, 36), sc._et(9, 38))  # one bar per step, in order
    assert f.anchor.object == "RangeBreak(level)" and f.anchor.bar_ts == sc._et(9, 36)


def never_higher() -> list:
    """The same premarket (level 10.05) and break; afterwards every bucket
    comes back to the level (a retest) and closes AT OR UNDER the prior
    bucket's high — the last step never holds."""
    import test_setups_second_chance as sc

    out, t = [], sc._et(8, 0)
    while t < sc._et(9, 30):
        out += sc._bucket(t, 10, "10.05" if t == sc._et(9, 0) else "10.01", "9.99", 10)
        t += timedelta(minutes=2)
    legs = [("10.00", "10.02", "9.90", "9.92"), ("9.92", "9.98", "9.88", "9.96"), ("9.96", "10.03", "9.94", "10.01"),
            ("10.01", "10.14", "10.00", "10.12"),  # the break: closes through 10.05
            ("10.12", "10.13", "10.05", "10.10"), ("10.10", "10.12", "10.05", "10.09"),
            ("10.09", "10.11", "10.05", "10.08")]
    for o, h, lo, c in legs:
        out += sc._bucket(t, o, h, lo, c)
        t += timedelta(minutes=2)
    return out


def test_f2_the_two_step_sequence_does_not_form_when_its_last_step_never_holds(two_step):
    ev = _evaluate_series(two_step, never_higher())
    assert ev.evaluation == "not_formed", (ev.evaluation, ev.note)
    assert "sequence" in ev.by_side["long"].note, ev.by_side["long"].note


def test_f2_an_unserved_step_names_its_own_gap_never_trigger_sequence(tmp_path):
    steps = [{"name": "through", "predicate": {"expr": "price close_through Level_ref"},
              "confirmation_policy": {"type": "close_through"}},
             {"name": "sized", "predicate": {"expr": "Gap.size > 0"}}]
    ld = shapes.load_note(tmp_path, "example-fix-unserved-step", break_then_turn_mapping(steps),
                          engine=shapes.D6_CONSTRUCTED)
    result = evaluability(ld.definition)
    assert result.evaluable is False
    assert "Gap.size" in result.missing_atoms and "trigger:sequence" not in result.missing_atoms, \
        result.missing_atoms


# =====================================================================
# F3 — the trigger resolver's reads join the declared closure
# =====================================================================

#: The two `range.micro.*` engine holes the `trendline_break` trigger reads
#: through the micro-Range observation, filled as `source: assumed` with the
#: build's OWN constructed literals (`setups_shapes.D2_CONSTRUCTED`, L69).
ASSUMED_FILLS = ("range.micro.touch_tolerance_atr", "range.micro.bound_flat_slope_atr")


def test_f3_an_assumed_fill_the_trigger_reads_reaches_assumed_keys_and_the_card_dot(tmp_path):
    from cobalt.radar.evaluate import assumed_keys_of, card_dots
    from cobalt.settings.card import CardSettings
    from cobalt.taxonomy.cli import assumed_note_text
    from cobalt.taxonomy.loader import merge_tunables
    from cobalt.taxonomy.vault_loader import load_vault_trade_defs
    from test_radar_evaluate import ENABLED_CARD  # a constructed config (L69)

    rows = [{"key": key, "value": float(shapes.D2_CONSTRUCTED[key][1]), "unit": "atr", "scope": "global",
             "dynamic": True, "status": "proposed", "source": "assumed", "consumers": ["a detector"]}
            for key in ASSUMED_FILLS]
    (tmp_path / "1 - Trading").mkdir(parents=True, exist_ok=True)
    (tmp_path / "1 - Trading" / "Assumed Defaults.md").write_text(assumed_note_text(rows))
    engine_fills = {k: v for k, v in shapes.D5_CONSTRUCTED.items() if k not in ASSUMED_FILLS}
    ld = shapes.load_note(tmp_path, "example-fix-assumed-trigger", shapes.pullback_to_vwap_mapping(),
                          engine=engine_fills)
    assumed = {t.key: t.row for t in load_vault_trade_defs(vault_root=tmp_path).user_tunables if t.slug is None}
    assert set(assumed) == set(ASSUMED_FILLS)
    tunables = merge_tunables(shapes.tunables_for(ld), assumed)

    settings = CardSettings.from_rows(sup.fixture_settings_rows(**ENABLED_CARD))
    formed = [(at, ev) for ticker in ("FTFT", "BGFI") for m in range(0, 391, 2)
              for at in [shapes.DAY_START + timedelta(minutes=m)]
              for ev in [shapes.evaluate(ld, ticker, at, tunables=tunables)] if ev.evaluation == "formed"]
    print(f"F3: formed scans={len(formed)}")
    assert formed
    for at, ev in formed:
        assert set(ASSUMED_FILLS) <= set(ev.formation.assumed_keys), (at, ev.formation.assumed_keys)
        dots = card_dots(ld, ev, settings, at, ev.formation.assumed_keys)
        assert set(ASSUMED_FILLS) <= set(assumed_keys_of(dots)), (at, assumed_keys_of(dots))


# =====================================================================
# P1 — a relation word outside its served sentence is reported, never silent
# =====================================================================

#: One precondition per relation word, each OUTSIDE the one sentence the word
#: serves (FINAL §4 "only what the seven need"). This file's sentences.
OUTSIDE_SENTENCES = {
    "after": "RangeBreak(level).state == accepted after event(stop_hit)",
    "inside": "EMA9 inside Range(prior)",
    "on": "Extension.instantiated on Leg(pullback)",
    "between": "flat(EMA9, window: 15 min / working_tf) between turn and entry",
}


def outside_mapping(sentence: str) -> dict:
    mapping = shapes.example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"}],
        preconditions=[{"expr": "Range(micro).instantiated"}, {"expr": sentence}],
        avoid=[{"text": "a human read, this file's words"}],
        trigger={"type": "bar_break", "params": {"bars_cleared": 4, "direction": "any"},
                 "confirmation_policy": {"type": "intrabar"}},
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning"],
        preferred_windows_ref="anatomy: a probe",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"]["ref"] = "range_base"
    return mapping


#: The `Unsupported(<word>:…)` entry each sentence is named by — pasted from
#: this test's own run (`P1 <word>: <missing_atoms>`), never guessed. A relation
#: whose resolver silently accepted a sentence outside its served one — or that
#: named it something other than `Unsupported(<word>:…)` — turns this red.
NAMED = {
    "after": "Unsupported(after:RangeBreak(level).state == accepted after event(stop_hit))",
    "between": "Unsupported(between:entry)",
    "inside": "Unsupported(inside:EMA9 inside Range(prior))",
    "on": "Unsupported(on:Leg(pullback))",
}


@pytest.mark.parametrize("word", sorted(OUTSIDE_SENTENCES))
def test_p1_a_relation_word_outside_its_served_sentence_is_not_evaluable_named(tmp_path, word):
    ld = shapes.load_note(tmp_path, f"example-fix-outside-{word}", outside_mapping(OUTSIDE_SENTENCES[word]))
    result = evaluability(ld.definition)
    print(f"P1 {word}: {result.missing_atoms}")
    assert result.evaluable is False
    assert NAMED[word] in result.missing_atoms, result.missing_atoms
