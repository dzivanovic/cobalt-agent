"""S2-P2 STEP-2 — the §10.5 predicate grammar (R3, Astra R1-4).

WHERE THE FORMS COME FROM. The grammar inventory was taken over every
`expr:` position of the 13 defined trade_defs as they last existed in
this repository's history (commit 96c9159^, before ADR-0008 moved them to
the vault), plus the forms the plan names as live (`IN cfg(...) min`,
function calls, named arguments, `/`, `touched`, `on`/`after`/`inside`,
nested calls, `!=`). The live notes themselves are user data and are
never copied here (L32): per-trade `cfg()` keys below are re-keyed to the
synthetic example's `example_range_break.*`. The one real artifact this
file does read is the shipped synthetic note, and the `requires_vault`
test reads the live notes in place (run by the hub).
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from cobalt.taxonomy.predicate import (
    And,
    Between,
    Cfg,
    Compare,
    InTest,
    Not,
    Or,
    PredicateSyntaxError,
    Qualified,
    Ref,
    Relation,
    Symbol,
    parse_predicate,
    render,
    required_atoms,
)
from cobalt.taxonomy.trade_def import Predicate, TradeDef
from cobalt.taxonomy.vault_loader import VaultTaxonomyError, load_vault_trade_defs
from taxonomy_example import EXAMPLE_NAME, EXAMPLE_SLUG, example_note_text

#: Every expression form in the inventory. Anatomy terms verbatim;
#: per-trade cfg keys re-keyed to the synthetic example.
INVENTORY_FORMS = [
    "InPlay.state == active",
    "Gap.instantiated",
    "Catalyst.grade >= 8",
    "Catalyst.grade <= 8",
    "Leg(opening_drive).direction == opposite(Gap.direction)",
    "Regime.label IN {range_bound, fading}",
    "Extension.state == backside",
    "Range(micro).instantiated AND Range(micro).low > EMA9 AND EMA9.slope > 0",
    "RangeBreak(HTF).day_count == 1",
    "Leg(opening_drive).direction == opposite(trade_direction)",
    "RangeBreak(Level_ref(HTF)).state == accepted AND against(trade_direction)",
    "RangeBreak(Level_ref(HTF)).state == accepted against trade_direction",
    "Range(micro) near turn_low AND Range.duration > cfg(example_range_break.near_low_duration_max)",
    "Catalyst.polarity == against(trade_direction)",
    "Leg(impulse).terminated_by == consolidation",
    "Range(micro).duration >= cfg(example_range_break.range_duration_band) min",
    "volatility_state == contraction",
    "Range(micro).height <= 0.5 * DayRange",
    "Range(micro).top < Level_ref(HTF resistance)",
    "Range(micro).instantiated AND Range(micro).bound_type == converging",
    "Range(micro).counter_pivot_count >= cfg(range.counter_pivot_min)",
    "Extension.instantiated on Leg(opening_drive)",
    "catalyst_ref != null",
    "Leg(opening_drive OR impulse).direction == trade_direction",
    "Leg(pullback) touched EMA9 AND price > EMA21",
    "touched(Leg(pullback), VWAP)",
    "Extension.instantiated on Leg(pre_test)",
    "Extension.state IN {reverting, backside}",
    "slope_norm(EMA9) > cfg(flat_threshold.ema9) AND slope_norm(VWAP) <= cfg(flat_threshold.vwap)",
    "flat(EMA9, window: 15 min / working_tf) between turn and cross",
    "Leg(pullback).index == 1",
    "Leg(pullback) touched VWAP",
    "close_through(Leg(pullback).low < VWAP)",
    "close_through(Leg(pullback).low < Level_ref(PMH))",
    "Range(micro).low > Level_ref(support)",
    "Range(micro).height <= 0.5 * Leg(opening_drive).range",
    "gap_retrace_pct > cfg(gap_retrace_pct_max)",
    "Range(micro).duration IN cfg(example_range_break.range_duration_band) min",
    "Range(micro).low >= DayRange.upper_third",
    "Leg(opening_drive).terminated_by == pullback",
    "Range(micro).wick_ratio > cfg(range.wick_ratio_max)",
    "Extension.state == culminating",
    "NOT Extension.instantiated",
    "RangeBreak(level).state == accepted",
    "event(retest) on that RangeBreak",
    "price close_through Level_ref",
    "event(retest)",
    "close_above(prior_bar)",
    "RangeBreak.state == failed_trap after event(retest)",
    "event(stop_hit) AND price inside Range(prior)",
    "Leg(pullback).direction == opposite(trade_direction) AND dist(Leg(pullback).end, VWAP) <= cfg(dist.k.vwap) * ATR(working_tf)",
    "Level_ref(resistance).rejected",
    "Range(micro).duration IN cfg(example_range_break.range_duration_band)",
    "Range(micro).duration <= min(cfg(example_range_break.range_duration_band), 20 min)",
    "event(exit_leg, 1)",
    "(Gap.instantiated OR InPlay.state == active) AND NOT Extension.instantiated",
]


@pytest.mark.parametrize("expr", INVENTORY_FORMS)
def test_every_inventory_form_parses_and_renders_stably(expr):
    ast = parse_predicate(expr)
    assert parse_predicate(render(ast)) == ast


def test_ast_is_frozen_pydantic():
    ast = parse_predicate("Extension.state == culminating")
    assert isinstance(ast, Compare)
    with pytest.raises(Exception):
        ast.op = "!="  # type: ignore[misc]


def test_precedence_not_binds_tighter_than_and_binds_tighter_than_or():
    ast = parse_predicate("NOT Gap.instantiated AND InPlay.state == active OR Extension.instantiated")
    assert isinstance(ast, Or)
    left = ast.operands[0]
    assert isinstance(left, And) and isinstance(left.operands[0], Not)


def test_comparison_right_hand_bare_word_is_a_symbol_not_an_atom():
    ast = parse_predicate("Extension.state == culminating")
    assert isinstance(ast.right, Symbol) and ast.right.name == "culminating"
    assert required_atoms(ast) == frozenset({"Extension.state"})


def test_in_takes_a_set_or_a_cfg_with_unit():
    as_set = parse_predicate("Extension.state IN {reverting, backside}")
    assert isinstance(as_set, InTest)
    as_cfg = parse_predicate("Range(micro).duration IN cfg(example_range_break.range_duration_band) min")
    assert isinstance(as_cfg, InTest)
    assert as_cfg.right.unit == "min" and isinstance(as_cfg.right.value, Cfg)


def test_relations_and_qualifiers_have_their_own_nodes():
    assert isinstance(parse_predicate("Leg(pullback) touched VWAP"), Relation)
    assert isinstance(parse_predicate("price inside Range(prior)"), Relation)
    assert isinstance(parse_predicate("Extension.instantiated on Leg(opening_drive)"), Qualified)
    assert isinstance(parse_predicate("RangeBreak.state == failed_trap after event(retest)"), Qualified)
    assert isinstance(parse_predicate("flat(EMA9, window: 15 min / working_tf) between turn and cross"), Between)


def test_a_relation_word_followed_by_a_paren_is_a_call():
    ast = parse_predicate("touched(Leg(pullback), VWAP)")
    assert isinstance(ast, Ref) and ast.segments[0].name == "touched"


def test_named_argument_and_division():
    ast = parse_predicate("flat(EMA9, window: 15 min / working_tf) between turn and cross")
    call = ast.subject
    assert call.segments[0].args[1].name == "window"


def test_required_atoms_for_the_extension_reversal_predicates():
    assert required_atoms(parse_predicate("NOT Extension.instantiated")) == frozenset({"Extension.instantiated"})
    assert required_atoms(parse_predicate("RangeBreak(HTF).day_count == 1")) == frozenset(
        {"RangeBreak(HTF).day_count"}
    )


def test_required_atoms_names_calls_whole_and_skips_cfg_numbers_symbols():
    atoms = required_atoms(parse_predicate(
        "Leg(pullback).direction == opposite(trade_direction) AND "
        "dist(Leg(pullback).end, VWAP) <= cfg(dist.k.vwap) * ATR(working_tf)"
    ))
    assert atoms == frozenset({
        "Leg(pullback).direction", "opposite(trade_direction)",
        "dist(Leg(pullback).end, VWAP)", "ATR(working_tf)",
    })


@pytest.mark.parametrize(
    "expr,fragment",
    [
        ("Extension.state ==", "expected an operand"),
        ("Extension.state == culminating AND", "expected an operand"),
        ("Range(micro.low > 1", "expected ')'"),
        ("Extension.state = culminating", "unexpected character '='"),
        ("Regime.label IN {range_bound, fading", "expected '}'"),
        ("event(teleport)", "unknown event 'teleport'"),
        ("cfg(Bad-Key)", "cfg key"),
        ("Extension.state == culminating culminating", "unexpected token"),
        ("", "empty"),
    ],
)
def test_bad_expression_fails_loud_with_position_and_text(expr, fragment):
    with pytest.raises(PredicateSyntaxError) as info:
        parse_predicate(expr)
    message = str(info.value)
    assert fragment in message
    assert repr(expr) in message
    assert "column" in message


def test_predicate_model_parses_expr_at_validation():
    pred = Predicate(expr="Extension.state == culminating")
    assert isinstance(pred.ast, Compare)
    assert pred.required_atoms == frozenset({"Extension.state"})
    with pytest.raises(ValueError, match="predicate syntax error"):
        Predicate(expr="Extension.state ==")
    text_pred = Predicate(text="fresh negative news against")
    assert text_pred.ast is None and text_pred.required_atoms == frozenset()


def test_ast_does_not_leak_into_the_stored_def_json(base_trade_def_dict):
    td = TradeDef.from_unit(base_trade_def_dict, slug=EXAMPLE_SLUG, name=EXAMPLE_NAME)
    dumped = td.model_dump(mode="json", by_alias=True)
    assert "ast" not in str(dumped.get("preconditions"))


def test_shipped_synthetic_note_parses(example_vault):
    loaded = load_vault_trade_defs(vault_root=example_vault)
    (td,) = loaded.defs
    for pred in [*td.definition.preconditions, *td.definition.avoid, *td.definition.radar_watch]:
        if pred.expr is not None:
            assert pred.ast is not None


def test_a_syntax_error_in_a_note_names_note_path_line_slug_and_expression(make_vault):
    bad = "Range(micro).low >= DayRange.upper_third AND"
    text = example_note_text().replace(
        '"Range(micro).low >= DayRange.upper_third"', f'"{bad}"'
    )
    vault = make_vault({EXAMPLE_NAME: text})
    expected_line = next(
        i for i, line in enumerate(text.splitlines(), 1) if bad in line
    )
    with pytest.raises(VaultTaxonomyError) as info:
        load_vault_trade_defs(vault_root=vault)
    message = str(info.value)
    assert f"{EXAMPLE_NAME}.md:{expected_line}" in message
    assert f"trade_def:{EXAMPLE_SLUG}" in message
    assert repr(bad) in message
    assert "predicate syntax error" in message


def test_an_unknown_cfg_inside_an_expression_fails_loud(make_vault):
    text = example_note_text().replace(
        "cfg(range.wick_ratio_max)", "cfg(range.no_such_key)"
    )
    vault = make_vault({EXAMPLE_NAME: text})
    with pytest.raises(VaultTaxonomyError, match="range.no_such_key"):
        load_vault_trade_defs(vault_root=vault)


# ---------------------------------------------------------------------
# requires_vault — the live notes, read in place, run by the hub
# ---------------------------------------------------------------------

LIVE_VAULT_ENV = "COBALT_LIVE_VAULT_ROOT"

requires_vault = pytest.mark.skipif(
    not os.getenv(LIVE_VAULT_ENV),
    reason=f"{LIVE_VAULT_ENV} not set — the hub runs the live-note grammar proof",
)


@requires_vault
def test_all_live_defined_notes_parse_and_report_missing_atoms(capsys):
    from cobalt.radar.anatomy.registry import evaluability

    root = Path(os.environ[LIVE_VAULT_ENV])
    loaded = load_vault_trade_defs(vault_root=root)
    assert len(loaded.defs) >= 13, [d.slug for d in loaded.defs]
    report = {d.slug: evaluability(d.definition) for d in loaded.defs}
    with capsys.disabled():
        for slug, result in sorted(report.items()):
            print(f"{slug}: evaluable={result.evaluable} missing={list(result.missing_atoms)}")
    rubberband = report.pop("rubberband")
    assert rubberband.evaluable, rubberband.missing_atoms
    # R2: Rubberband is the only def evaluable end-to-end in S2; every
    # other def names exactly what it is missing, never a fake card.
    for slug, result in report.items():
        assert not result.evaluable and result.missing_atoms, slug
