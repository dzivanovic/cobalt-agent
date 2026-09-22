"""STEP-1 of the setups one build (FINAL C1) — the Extension-reversal shape
can form, and a card formed on an assumed convention carries the untappable
`assumed_formation` dot (R2-2 = B, his R40).

The defect this closes is the proof's (`rubberband-card-proof-2026-09-21.md`,
test A): a def whose `valid_setups[]` mixes `countertrend` and `with_trend`
was returned `not_evaluable: Setup(relation)` on every scan. The helpers are
adapted from the proof's test file (`tests/cobalt/test_rubberband_card_proof.py`
on the unmerged proof branch) into `setups_shapes.py`; this file is not the
proof's.

R24 BINDS EVERY TEST: no expected value here comes from a day the trader
traded or tagged. Every `DEF_WRITTEN_*` constant is the value the ENGINE
computes from the definition's shape on the committed real-shape bars — a
checker house re-derives each one blind (prompt `66`, FINAL [F-16] (1)).
L69: every settings value is a constructed config (`ENABLED_CARD`).
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.radar.anatomy.bars import rth_only, working_bars
from cobalt.radar.anatomy.extension import ExtensionParams, detect_extension
from cobalt.radar.anatomy.structure import bar_break_trigger, structural_stop, tracked_extreme
from cobalt.radar.evaluate import (
    EVALUATOR_VERSION,
    TIE_POLICY,
    ReplayError,
    card_why,
    refresh_card,
    replay_receipt,
    working_minutes,
)
from cobalt.session import session_clock
from test_radar_evaluate import ENABLED_CARD, World

UTC = timezone.utc
SCAN0 = shapes.SCAN0
FORMED_BAR = datetime(2026, 1, 6, 16, 22, tzinfo=UTC)

#: The single-relation control forms on this many two-minute scans of the
#: committed FTFT day on the START-of-step code (the proof's denominator).
CONTROL_FORMED_SCANS = 71

# --- FINAL §9 point (1): the four values, from the DEFINITION on the bars ---
# engine at STEP-1; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_FORMED_BAR = datetime(2026, 1, 6, 16, 22, tzinfo=UTC)
# engine at STEP-1; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_SIDE = "short"
# engine at STEP-1; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_TRIGGER = "5.5000"
# engine at STEP-1; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_STOP = "5.81"
# engine at STEP-1; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_RUBBERBAND_LAST = "5.5750"


def _sha(payload) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()


@pytest.fixture(scope="module")
def defs(tmp_path_factory) -> dict[str, sup.LoadedDef]:
    out = {}
    for name, valid_setups, htf in (
        ("mixed", shapes.MIXED, False), ("countertrend", shapes.COUNTERTREND_ONLY, False),
        ("with_trend", shapes.WITH_TREND_ONLY, False), ("full", shapes.MIXED, True),
    ):
        out[name] = shapes.load_note(tmp_path_factory.mktemp(name), f"shape-{name.replace('_', '-')}-reversal",
                                     shapes.rubberband_mapping(valid_setups, htf_avoid=htf))
    return out


def _formed(rows):
    return [(at, ev) for at, ev in rows if ev.evaluation == "formed"]


# =====================================================================
# T1 — THE DEFECT, REPRODUCED (the test asserts the FIXED behaviour)
# =====================================================================


def test_t1_the_mixed_shape_forms_on_the_culminating_bar(defs):
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    assert ev.evaluation == "formed", (ev.evaluation, ev.missing, ev.note)
    assert ev.direction == "short" and ev.formation.trade_direction == "short"
    assert ev.formation.formed_bar_ts == FORMED_BAR
    assert ev.formation.setup_ref == "unclassified"


def test_t1_over_the_day_the_mixed_shape_forms_wherever_the_control_forms(defs):
    control = _formed(shapes.every_scan(defs["countertrend"], "FTFT"))
    assert len(control) == CONTROL_FORMED_SCANS
    mixed = dict(shapes.every_scan(defs["mixed"], "FTFT"))
    refused = []
    for at, c in control:
        m = mixed[at]
        if m.evaluation == "not_formed" and m.note == "stop_wrong_side":
            refused.append(at)
            continue
        assert m.evaluation == "formed", (at, m.evaluation, m.missing, m.note)
        assert (m.direction, m.formation.trigger, m.formation.stop, m.formation.formed_bar_ts) == (
            c.direction, c.formation.trigger, c.formation.stop, c.formation.formed_bar_ts), at
    assert refused == []  # the geometry guard refuses none of the control's formed scans (X17)
    control_at = {at for at, _ in control}
    assert {at for at, ev in mixed.items() if ev.evaluation == "formed"} == control_at


# =====================================================================
# T2 — FINAL §9 GATES 1-5 FOR THE SHAPE
# =====================================================================


def test_t2_point_1_the_control_carries_the_definition_written_values(defs):
    ev = shapes.evaluate(defs["countertrend"], "FTFT", SCAN0)
    assert ev.evaluation == "formed"
    assert ev.formation.formed_bar_ts == DEF_WRITTEN_RUBBERBAND_FORMED_BAR
    assert ev.formation.trade_direction == DEF_WRITTEN_RUBBERBAND_SIDE
    assert (str(ev.formation.trigger.price), str(ev.formation.stop.price), str(ev.last_price)) == (
        DEF_WRITTEN_RUBBERBAND_TRIGGER, DEF_WRITTEN_RUBBERBAND_STOP, DEF_WRITTEN_RUBBERBAND_LAST)


def test_t2_point_1_the_mixed_shape_carries_the_definition_written_values(defs):
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    assert ev.evaluation == "formed", (ev.evaluation, ev.missing, ev.note)
    assert ev.formation.formed_bar_ts == DEF_WRITTEN_RUBBERBAND_FORMED_BAR
    assert ev.formation.trade_direction == DEF_WRITTEN_RUBBERBAND_SIDE
    assert (str(ev.formation.trigger.price), str(ev.formation.stop.price), str(ev.last_price)) == (
        DEF_WRITTEN_RUBBERBAND_TRIGGER, DEF_WRITTEN_RUBBERBAND_STOP, DEF_WRITTEN_RUBBERBAND_LAST)


def test_t2_the_full_shape_is_avoided_exactly_where_the_control_forms(defs):
    """The full shape (4+1 + the day-1 HTF avoid): the avoid is True on the
    committed day, so it is `avoided` on exactly the control's formed scans
    (proof ESCALATE 2) and never `not_evaluable: Setup(relation)`. Its other
    `not_evaluable` scans are Extension path B only (catalyst unknown, R4),
    unchanged by this build."""
    control_at = [at for at, _ in _formed(shapes.every_scan(defs["countertrend"], "FTFT"))]
    rows = shapes.every_scan(defs["full"], "FTFT")
    assert _formed(rows) == []
    assert [at for at, ev in rows if ev.evaluation == "avoided"] == control_at
    for _at, ev in rows:
        assert "Setup(relation)" not in ev.missing and "Setup(relation)" not in ev.detail.missing_atoms
        if ev.evaluation == "not_evaluable":
            assert ev.detail.extension_path == "B_only", ev.note


def test_t2_point_4_the_full_shape_is_evaluable(defs):
    from cobalt.radar.anatomy.registry import evaluability

    assert evaluability(defs["full"].definition).evaluable


def test_t2_gate_4_expect_formed_exits_non_zero_on_zero_formations(defs):
    from cobalt.radar.evaluate_cli import expect_formed_gate, replay_formations
    from test_radar_evaluate_cli import ReadOnlyRadar, _daily

    radar = ReadOnlyRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    common = dict(pool_key="pool", radar_store=radar, daily_source=_daily, tunables=sup.engine_tunables(),
                  defaults=sup.defaults(), clock=session_clock(), out=lambda _line: None)
    zero = replay_formations(sup.TRADE_DATE, slug_filter=defs["full"].slug,
                             defs_source=lambda: ([defs["full"]], {}), **common)
    with pytest.raises(SystemExit, match="expect-formed"):
        expect_formed_gate(zero, defs["full"].slug)
    report = expect_formed_gate(replay_formations(sup.TRADE_DATE, slug_filter=defs["mixed"].slug,
                                                  defs_source=lambda: ([defs["mixed"]], {}), **common),
                                defs["mixed"].slug)
    assert report.formations and report.formations[0].direction == "short"


def test_t2_gate_4_expect_formed_without_a_trade_def_is_refused():
    import argparse

    from cobalt.radar import cli as radar_cli

    parser = argparse.ArgumentParser()
    radar_cli.add_parser(parser.add_subparsers(dest="group"))
    args = parser.parse_args(["radar", "evaluate", "--replay", "2026-01-06", "--expect-formed"])
    with pytest.raises(SystemExit, match="--expect-formed needs --trade-def"):
        args.func(args)


def test_t2_gate_5_replay_refuses_a_receipt_of_another_evaluator_version():
    world = World()
    world.scan(SCAN0)
    receipts = list(world.cards.receipts)
    receipts[-1]["observations"]["evaluator_version"] = "not-this-version"
    with pytest.raises(ReplayError, match="not-this-version") as caught:
        replay_receipt(receipts, clock=session_clock())
    assert EVALUATOR_VERSION in str(caught.value)


def test_t2_the_nightly_binding_supports_the_bumped_version_and_refuses_an_unknown_one():
    from cobalt.replay.formations import SUPPORTED_EVALUATORS, formation_candidates
    from cobalt.replay.models import ReplayError as BindingError

    assert EVALUATOR_VERSION != "s2p2.1"
    assert EVALUATOR_VERSION in SUPPORTED_EVALUATORS
    with pytest.raises(BindingError, match="not-this-version"):
        formation_candidates(type("R", (), {"formations": []})(), evaluator_version="not-this-version")


# =====================================================================
# T3 — THE GEOMETRY GUARD; X17 first
# =====================================================================


def protective(direction: str, trigger: Decimal, stop: Decimal, last: Decimal) -> bool:
    """FINAL §9 point (5), as the test's own predicate."""
    if direction == "long":
        return stop < min(trigger, last)
    return stop > max(trigger, last)


def _rebuilt_with_trend(ld: sup.LoadedDef, at: datetime):
    """The WITH_TREND_ONLY control's start-of-step formation, rebuilt from the
    same anatomy functions the start-of-step evaluator called (a long on the
    up-run: `bar_break_trigger(run, n, "long")`, the stop from the run's own
    tracked extreme)."""
    closed = [b for b in shapes.bars("FTFT") if b.ts + timedelta(minutes=1) <= at]
    run = tuple(rth_only(working_bars(closed, working_minutes(sup.defaults()), as_of=at), session_clock()))
    ext = detect_extension(run, ExtensionParams.from_tunables(sup.engine_tunables()))
    trigger = bar_break_trigger(run, 2, "long")
    stop = structural_stop(tracked_extreme(run, ext.direction).price, "long",
                           Decimal(str(sup.engine_tunables()["stop.buffer"].value)))
    return "long", trigger.price, stop.price, closed[-1].close


def test_x17_point_5_against_the_proofs_two_controls(defs):
    """X17 (FINAL: "run §9 point (5) against the proof's two controls"). The
    countertrend tuples come from the evaluator; the with-trend tuples are
    rebuilt from the anatomy on the same scans (the start-of-step with-trend
    control formed on exactly these — `test_x17_start_of_step_equivalence`)."""
    control = _formed(shapes.every_scan(defs["countertrend"], "FTFT"))
    ct = [(ev.direction, ev.formation.trigger.price, ev.formation.stop.price, ev.last_price) for _, ev in control]
    wt = [_rebuilt_with_trend(defs["with_trend"], at) for at, _ in control]
    refused_ct = sum(not protective(*t) for t in ct)
    refused_wt = sum(not protective(*t) for t in wt)
    assert (len(ct), refused_ct, len(wt), refused_wt) == (CONTROL_FORMED_SCANS, 0, CONTROL_FORMED_SCANS,
                                                          CONTROL_FORMED_SCANS)


def test_x17_start_of_step_equivalence(defs):
    """On the START-of-step code the with-trend control's formations equalled
    the rebuilt long tuples scan for scan (GREEN, quoted in the report). From
    STEP-1 `relation` is never read (A-01, FINAL §1): the with-trend-only def
    forms exactly the countertrend control's formations."""
    rows = _formed(shapes.every_scan(defs["with_trend"], "FTFT"))
    got = [(at, ev.direction, ev.formation.trigger.price, ev.formation.stop.price, ev.last_price) for at, ev in rows]
    control = _formed(shapes.every_scan(defs["countertrend"], "FTFT"))
    assert got == [(at, ev.direction, ev.formation.trigger.price, ev.formation.stop.price, ev.last_price)
                   for at, ev in control]


def test_t3_a_stop_on_the_wrong_side_is_not_formed_and_makes_no_card(defs, monkeypatch):
    from cobalt.radar.formation import stops as stops_mod

    real = stops_mod.structural_stop

    def below_the_trigger(price, direction, buffer):
        # STEP-2: the stop resolves in the frame's coordinates (the short trade
        # is the long side of the mirrored frame), so +1.00 there puts the real
        # short stop 1.00 BELOW its extreme — under the trigger.
        return real(price + Decimal("1.00"), direction, buffer)

    monkeypatch.setattr(stops_mod, "structural_stop", below_the_trigger)
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    # STEP-2 (R2-4.1 B): the short frame is refused by the guard; with
    # neither frame formed the published row is the LONG frame's.
    assert ev.by_side["short"].evaluation == "not_formed" and ev.by_side["short"].note == "stop_wrong_side"
    assert ev.evaluation == "not_formed" and ev.formation is None
    world = World(defs=[defs["mixed"]])
    outcome = world.scan(SCAN0)
    assert outcome.created == [] and world.cards.cards == {}


# =====================================================================
# T4 — THE `unclassified` TOKEN [F-07]
# =====================================================================


def test_t4_unclassified_is_a_module_constant_outside_setupref():
    from cobalt.radar.evaluate import UNCLASSIFIED_SETUP
    from cobalt.taxonomy.trade_def import SetupRef, TradeDef

    assert UNCLASSIFIED_SETUP == "unclassified"
    assert UNCLASSIFIED_SETUP not in {m.value for m in SetupRef}
    mapping = shapes.rubberband_mapping([{"setup_ref": "unclassified", "relation": "countertrend"}], htf_avoid=False)
    with pytest.raises(ValueError):
        TradeDef.from_unit(mapping, slug="shape-unclassified", name="Shape Unclassified")


def test_t4_every_formation_carries_the_token_and_the_why_starts_with_it(defs):
    for name in ("mixed", "countertrend", "with_trend"):
        ev = shapes.evaluate(defs[name], "FTFT", SCAN0)
        assert ev.evaluation == "formed" and ev.formation.setup_ref == "unclassified", name
        assert card_why(defs[name].definition, ev.formation).startswith("unclassified · "), name


def test_t4_the_label_no_longer_depends_on_list_order(defs, tmp_path):
    reversed_def = shapes.load_note(tmp_path, "shape-mixed-reversed",
                                    shapes.rubberband_mapping(list(reversed(shapes.MIXED)), htf_avoid=False))
    one = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    two = shapes.evaluate(reversed_def, "FTFT", SCAN0)
    assert one.evaluation == two.evaluation == "formed"
    assert one.formation.model_dump() == two.formation.model_dump()


# =====================================================================
# T5 — THE UNTAPPABLE DOT (R40 / B) — the offline legs
# =====================================================================


def _assumed(dots):
    return [d for d in dots if d.factor == "assumed_formation"]


def test_t5a_create_appends_exactly_one_untappable_assumed_dot(defs):
    world = World(defs=[defs["mixed"]])
    assert world.scan(SCAN0).created == [1]
    card = world.cards.cards[1]
    factors = [q.name for q in defs["mixed"].definition.quality_factors]
    assert [d.factor for d in card["dots"]] == [*factors, "assumed_formation"]
    (dot,) = _assumed(card["dots"])
    assert dot.position == len(factors)
    assert (dot.source, dot.tier, dot.role, dot.na_reason) == ("cobalt-degraded", "deterministic", "shadow", "ASSUMED")
    # STEP-2 (R2-2.2 B): the closure names A-01 by its convention ROW key
    assert dot.engine_inputs == {"assumed_keys": ["anatomy.orientation.extension"]}
    assert "anatomy.orientation.extension" in dot.engine_why and dot.trader_grade is None
    assert card["card_score"] is None and "assumed_formation" in card["score_suppressed"]
    assert card["proximity"] is not None and card["conviction"] is None and card["proposed_key"] is None
    relation = next(d for d in card["dots"] if d.factor == "setup_relation")
    assert relation.role == "human" and relation.source == "human"  # L11: stays YOURS


def test_t5c2_refresh_keeps_the_dot_and_the_null_score_after_every_other_dot_is_tapped(defs):
    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    for position, q in enumerate(defs["mixed"].definition.quality_factors):
        world.cards.tap(1, q.name, 5 + position % 5)
    world.scan(SCAN0 + timedelta(seconds=100))
    card = world.cards.cards[1]
    assert len(_assumed(card["dots"])) == 1
    assert card["conviction"] is not None
    assert card["card_score"] is None and "assumed_formation" in card["score_suppressed"]
    assert "(tap to grade)" not in card["score_suppressed"]  # every blocker is ASSUMED


def test_t5c3_x27_an_appended_dot_survives_refresh_card(defs):
    """X27 (FINAL: "with an evaluator-appended dot outside `quality_factors`,
    run `refresh_card` then read the returned dots and `score_suppressed`").
    The stored card carries a hand-appended `assumed_formation` dot; the
    refresh returns it (re-appended from the card's OWN stored keys)."""
    from cobalt.cards.scoring import Dot, compute_dots
    from cobalt.radar.evaluate import OpenRadarCard
    from cobalt.settings.card import CardSettings

    ld = defs["countertrend"]
    ev = shapes.evaluate(ld, "FTFT", SCAN0)
    settings = CardSettings.from_rows(sup.fixture_settings_rows(**ENABLED_CARD))
    stored = compute_dots(ld.definition.quality_factors, ev.observations, settings.curves, at=SCAN0)
    hand = Dot(factor="assumed_formation", position=len(stored), source="cobalt-degraded", tier="deterministic",
               role="shadow", na_reason="MANUAL", engine_inputs={"assumed_keys": ["A-01"]},
               engine_why="formed on assumed defaults: A-01")
    card = OpenRadarCard(
        card_id=1, pool_member_id=100, ticker="FTFT", direction="short", state="WATCH", trade_def_slug=ld.slug,
        trade_def_md5=ld.md5, trigger_price=ev.formation.trigger.price, structural_stop=ev.formation.stop.price,
        entry=ev.formation.trigger.price, stop=ev.formation.stop.price, formed_at=ev.formation.formed_bar_ts,
        expires_at=SCAN0 + timedelta(hours=2), dots=[*stored, hand],
    )
    update = refresh_card(card, ev, ld, settings, [], at=SCAN0, thresholds=None)
    (dot,) = _assumed(update.dots)
    assert dot.engine_inputs == {"assumed_keys": ["A-01"]} and dot.na_reason == "ASSUMED"
    assert update.card_score is None and "assumed_formation" in update.score_suppressed


def test_t5e_the_keys_come_from_the_stored_dot_never_from_a_live_source(defs):
    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    card = world.cards.cards[1]
    card["dots"] = [d.model_copy(update={"engine_inputs": {"assumed_keys": ["A-99"]}})
                    if d.factor == "assumed_formation" else d for d in card["dots"]]
    engine = sup.engine_tunables()
    world.stage.tunables_loader = lambda: {**engine}  # a reloaded live table changes nothing
    world.scan(SCAN0 + timedelta(seconds=100))
    (dot,) = _assumed(world.cards.cards[1]["dots"])
    assert dot.engine_inputs == {"assumed_keys": ["A-99"]}
    # a card with NO stored dot gets none at refresh: no dot -> no keys
    card = world.cards.cards[1]
    card["dots"] = [d for d in card["dots"] if d.factor != "assumed_formation"]
    world.scan(SCAN0 + timedelta(seconds=200))
    assert _assumed(world.cards.cards[1]["dots"]) == []


def test_t5c4_the_audit_export_shows_no_score_the_card_does_not_have(defs, tmp_path):
    from cobalt.radar import audit_export as ax
    from test_radar_evaluate_cli import ReadOnlyRadar, _daily

    radar = ReadOnlyRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    ax.export_replay(
        sup.TRADE_DATE, pool_key="pool", slug_filter=None, radar_store=radar,
        defs_source=lambda: ([defs["mixed"]], {}), daily_source=_daily, tunables=sup.engine_tunables(),
        defaults=sup.defaults(), settings_values=sup.fixture_settings_rows(**ENABLED_CARD), clock=session_clock(),
        out=tmp_path / "bundle", generated_at=datetime(2026, 9, 21, 22, 0, tzinfo=UTC),
    )
    cards = json.loads((tmp_path / "bundle" / "cards.json").read_text())["cards"]
    assert cards
    for card in cards:
        dots = [d for d in card["candidate"]["dots"] if d["factor"] == "assumed_formation"]
        assert len(dots) == 1 and dots[0]["na_reason"] == "ASSUMED"
        assert card["candidate"]["card_score"] is None
        assert "assumed_formation" in card["candidate"]["score_suppressed"]


def test_t5c5_replay_recomputes_the_created_and_the_refreshed_card(defs):
    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    world.cards.tap(1, "trail_fit", 7)
    world.scan(SCAN0 + timedelta(seconds=100))
    first, second = world.cards.receipts
    assert first["tap_versions"]["cards"][0]["assumed_keys"] == ["anatomy.orientation.extension"]
    assert second["tap_versions"]["cards"][0]["assumed_keys"] == ["anatomy.orientation.extension"]
    for chain in ([first], [first, second]):
        _evs, cards = replay_receipt(chain, clock=session_clock())
        assert [c.recomputed for c in cards] == [c.published for c in cards] and cards
        published = cards[0].published
        assert published["card_score"] is None and "assumed_formation" in published["score_suppressed"]
        assert [d["factor"] for d in published["dots"]][-1] == "assumed_formation"


def test_t5e_prime_order_by_is_unchanged_three_suppressed_cards_tie_to_the_policy():
    from cobalt.cards.models import CardState
    from cobalt.cards.radar import LadderEntry, ladder_order

    assert TIE_POLICY == (
        "pinned(ARMED,TRIGGERED,FILLED) by pool_position nulls last, score desc nulls last, ticker, card_id; "
        "WATCH by card_score desc nulls last, pool_position nulls last, ticker, card_id; "
        "one promoted WATCH card to #2 or below pinned, never demoted"
    )
    at = SCAN0
    entries = [
        LadderEntry(card_id=3, state=CardState.WATCH, card_score=None, pool_position=2, ticker="BBB", state_at=at),
        LadderEntry(card_id=2, state=CardState.WATCH, card_score=None, pool_position=1, ticker="CCC", state_at=at),
        LadderEntry(card_id=1, state=CardState.WATCH, card_score=None, pool_position=2, ticker="AAA", state_at=at),
    ]
    assert [p.card_id for p in ladder_order(entries).active] == [2, 1, 3]


# =====================================================================
# T6 — NOTHING OUTSIDE THE SHAPE'S FORMATION CHANGES (golden pins)
# =====================================================================

#: sha256 over every NON-formed evaluation's `model_dump(mode="json")` on the
#: committed day (FTFT + BGFI, two-minute scans), pinned on the START-of-step
#: code. `MemberEvaluation` carries no `evaluator_version` and no formula
#: digest, so NOTHING is excluded.
PIN_NON_FORMED_SHIPPED_EXAMPLE = "da0f0ef1aa0179ea2b07adf9f6ac4d64eec24dd705152b7e8eee4a2326877be7"
PIN_NON_FORMED_FULL_SHAPE = "e5e7a8799e7e83b62be9d552eca1d74cd2348da0f451813107f580874d80c831"
#: The formed synthetic single-relation def (`radar_p2_support.anatomy_def`)
#: at SCAN0, with ONLY the FINAL's named changes removed: the Formation minus
#: `setup_ref` (→ `unclassified`) and `assumed_keys` (new); the card spec
#: minus `setup_ref`, `why` (it starts with the setup token), `card_score`,
#: `score_suppressed`, `dots` (the dot + null score) and `formula_sha256`
#: (the formula files' bytes change by construction).
PIN_FORMED_FORMATION = "7c3eaba38d569fe3fc0371c0a9062eb9a70a421be6285a8b7078cbe3b54c04bd"
PIN_FORMED_CARD = "0724a61afb0b222b7d9a359d7e9ab17f2c771acb5a46f384f9da74f840ba8224"
PIN_FORMED_CARD_DOTS = "01a579e77814bfa92aa50d204a39b0a839e80496718914eafb649180bfec6e00"
#: + STEP-2's added fields (`side_frame`, `anchor`, `trigger_outcome`, `stop_outcome`).
FORMATION_EXCLUDED = {"setup_ref", "assumed_keys", "side_frame", "anchor", "trigger_outcome", "stop_outcome"}
CARD_EXCLUDED = {"setup_ref", "why", "card_score", "score_suppressed", "dots", "formula_sha256"}


def _non_formed(ld) -> list:
    """STEP-2 re-point: minus `by_side` (added) and E9's `Unsupported(<kind>)`
    names (`test_setups_registries.without_e9_shapes`)."""
    from test_setups_registries import without_e9_shapes

    return [without_e9_shapes({k: v for k, v in ev.model_dump(mode="json").items() if k != "by_side"})
            for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(ld, ticker) if ev.evaluation != "formed"]


def test_t6_non_formed_evaluations_are_byte_identical(defs):
    from cobalt.taxonomy.trade_def import TradeDef

    shipped = TradeDef.from_unit(shapes.example_mapping(), slug="example-range-break", name="Example Range Break")
    assert _sha(_non_formed(sup.loaded(shipped, md5="fedcba9876543210fedcba9876543210"))) == \
        PIN_NON_FORMED_SHIPPED_EXAMPLE
    assert _sha(_non_formed(defs["full"])) == PIN_NON_FORMED_FULL_SHAPE


def test_t6_a_def_that_formed_before_changes_only_in_the_finals_named_ways():
    ev = shapes.evaluate(sup.loaded(), "FTFT", SCAN0)
    assert ev.evaluation == "formed"
    formation = {k: v for k, v in ev.formation.model_dump(mode="json").items() if k not in FORMATION_EXCLUDED}
    assert _sha(formation) == PIN_FORMED_FORMATION
    world = World()
    world.scan(SCAN0)
    card = world.cards.cards[1]
    kept = {k: v for k, v in card.items() if k not in CARD_EXCLUDED}
    # STEP-2: committed tunables.yaml gains the convention row (R2-2.2 B) —
    # the digest is the snapshot WITH it, mapped back to the one WITHOUT it.
    from test_setups_registries import _tunables_digests

    new, old = _tunables_digests()
    assert kept["tunables_sha256"] in (new, old)
    kept["tunables_sha256"] = old
    assert _sha(kept) == PIN_FORMED_CARD
    dots = [d.model_dump(mode="json") for d in card["dots"] if d.factor != "assumed_formation"]
    assert _sha(dots) == PIN_FORMED_CARD_DOTS


# =====================================================================
# T5 — the with-DB legs (cobalt_dev, inside the suite's rollback tx)
# =====================================================================

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

from test_radar_cards_db import ENABLED as DB_ENABLED  # noqa: E402
from test_radar_cards_db import SCAN0 as DB_SCAN0  # noqa: E402
from test_radar_cards_db import world  # noqa: E402,F401 — the with-DB fixture


def _db_row(cards, card_id):
    with cards._connect() as conn:
        taps = conn.execute("SELECT count(*) FROM card_dot_taps WHERE card_id = %s", (card_id,)).fetchone()[0]
        dot = conn.execute(
            "SELECT trader_grade, na_reason, engine_inputs FROM card_dots WHERE card_id = %s AND factor = %s",
            (card_id, "assumed_formation"),
        ).fetchone()
        sizing = conn.execute(
            "SELECT conviction, card_score, score_suppressed, proposed_key FROM aset_sizings WHERE id = %s",
            (card_id,),
        ).fetchone()
    return taps, dot, sizing


def _bands():
    from cobalt.settings.card import CardSettings

    return CardSettings.from_rows(DB_ENABLED).proposed_key


@requires_db
@pytest.mark.integration
def test_t5a_db_the_created_card_carries_the_dot_and_no_score(world):
    card_id = world["scan"](DB_SCAN0).created[0]
    _taps, dot, sizing = _db_row(world["cards"], card_id)
    assert dot is not None and dot[0] is None and dot[1] == "ASSUMED"
    assert dot[2] == {"assumed_keys": ["anatomy.orientation.extension"]}
    assert sizing[1] is None and "assumed_formation" in sizing[2]


@requires_db
@pytest.mark.integration
def test_t5b_db_a_tap_on_the_assumed_dot_is_refused_and_the_row_is_unchanged(world):
    from cobalt.aset.models import Grade
    from cobalt.cards import CardStateError

    card_id = world["scan"](DB_SCAN0).created[0]
    cards = world["cards"]
    before = _db_row(cards, card_id)
    with pytest.raises(CardStateError, match="assumed_formation is not graded on a card"):
        cards.tap_dot(card_id, "assumed_formation", 7, bands=_bands(), enabled=[Grade.A, Grade.B, Grade.C])
    assert _db_row(cards, card_id) == before


@requires_db
@pytest.mark.integration
def test_t5c1_x8_db_a_tap_on_every_other_dot_leaves_the_score_null(world):
    from cobalt.aset.models import Grade

    card_id = world["scan"](DB_SCAN0).created[0]
    cards = world["cards"]
    result = None
    for name in [q.name for q in sup.loaded().definition.quality_factors]:
        result = cards.tap_dot(card_id, name, 8, bands=_bands(), enabled=[Grade.A, Grade.B, Grade.C])
    assert result["conviction"] == "0.8"
    assert result["card_score"] is None and "assumed_formation" in result["score_suppressed"]
    _taps, dot, sizing = _db_row(cards, card_id)
    assert dot[0] is None and sizing[1] is None and "assumed_formation" in sizing[2]


@requires_db
@pytest.mark.integration
def test_t5d_x8_db_a_scan_after_a_tap_keeps_the_dot_and_the_null_score(world):
    from cobalt.aset.models import Grade

    card_id = world["scan"](DB_SCAN0).created[0]
    cards = world["cards"]
    cards.tap_dot(card_id, "trail_fit", 8, bands=_bands(), enabled=[Grade.A, Grade.B, Grade.C])
    second = world["scan"](DB_SCAN0 + timedelta(seconds=100))
    assert second.refreshed == [card_id]
    _taps, dot, sizing = _db_row(cards, card_id)
    assert dot is not None and dot[1] == "ASSUMED" and dot[0] is None
    assert sizing[1] is None and "assumed_formation" in sizing[2]


@requires_db
@pytest.mark.integration
def test_t5d_prime_x24_the_shadow_report_and_the_panel_over_a_card_carrying_the_dot(world):
    from cobalt.aset import radar_panel as panel
    from cobalt.aset.models import Grade
    from cobalt.cards import shadow_report as sr
    from cobalt.settings.card import CardSettings

    card_id = world["scan"](DB_SCAN0).created[0]
    cards = world["cards"]
    with cards._connect() as conn:
        engine = conn.execute(
            "SELECT engine_grade FROM card_dots WHERE card_id = %s AND factor = 'rvol'", (card_id,)
        ).fetchone()[0]
    cards.tap_dot(card_id, "rvol", engine, bands=_bands(), enabled=[Grade.A, Grade.B, Grade.C], now=DB_SCAN0)
    rows = cards.shadow_agreement(None)
    assert "assumed_formation" not in {r["factor"] for r in rows}
    report = sr.shadow_report(rows, bar=CardSettings.from_rows(
        {"radar.cards_enabled": False,
         "card.shadow_promotion_bar": {"sessions": 10, "pairs": 30, "median_max": 1, "within2_min": 0.9}},
    ).shadow_promotion_bar, since=None)
    assert "assumed_formation" not in sr.render_report(report)
    view = panel.build_ladder_view(
        card_store=cards, settings_store=world["settings"], clock=session_clock(),
        now=DB_SCAN0 + timedelta(seconds=60), rung_source=lambda _at, _cfg: "reduced",
    )
    card = next(c for c in view.active if c.id == card_id)
    assert any(d.factor == "assumed_formation" for d in card.dots)
    assert "n/a ASSUMED" in panel.render_ladder(view)


@requires_db
@pytest.mark.integration
def test_x8_source_half_db_the_open_card_keeps_its_dot_after_the_convention_is_ruled(world):
    """X8's `source` half on cobalt_dev (STEP-2; Fable R2 (c): "change the
    row's `source` to `ruling` and load"): the OPEN card keeps its dot, a
    null score and the suppression; a NEW formation after the flip carries
    no dot for that key."""
    import asyncio

    from cobalt.radar.anatomy.freshness import RvolObservation
    from cobalt.radar.evaluate import CONVENTION_LABELS, EvaluateStage
    from cobalt.taxonomy.tunables import TunableSource
    from test_radar_cards_db import POOL, TICKER

    key = "anatomy.orientation.extension"
    rows = [dict(sup.engine_tunables())]

    async def daily(ticker, now):
        return sup.fixture_daily("FTFT", now).model_copy(update={"ticker": ticker})

    radar = world["radar"]
    stage = EvaluateStage(
        radar_store=radar, card_store=world["cards"], defs_source=lambda: ([sup.loaded()], {}),
        settings_values=world["settings"].values, daily_source=daily, tunables_loader=lambda: rows[0],
        defaults_loader=sup.defaults, clock=session_clock(), now=lambda: DB_SCAN0,
        members_at=lambda _pool, _at: radar.admitted_members(POOL),
    )

    def scan(at):
        stage.now = lambda: at
        return asyncio.run(stage.run(
            pool_key=POOL, scan_id=int(at.timestamp() * 1000), session="RTH", instant=at,
            rvol={TICKER: RvolObservation(ticker=TICKER, value=4.2, observed_at=at, source="screen:s",
                                          candidates=("screen:s",))},
            pool_unit={"pool_block": None}, gate=lambda _label: (lambda: None),
        ))

    card_id = scan(DB_SCAN0).created[0]
    ruled = dict(rows[0])
    ruled[key] = ruled[key].model_copy(update={"value": CONVENTION_LABELS[key], "source": TunableSource.RULING})
    rows[0] = ruled
    assert scan(DB_SCAN0 + timedelta(seconds=100)).refreshed == [card_id]
    _taps, dot, sizing = _db_row(world["cards"], card_id)
    assert dot is not None and dot[1] == "ASSUMED" and dot[2] == {"assumed_keys": [key]}
    assert sizing[1] is None and "assumed_formation" in sizing[2]
    fresh = shapes.evaluate(sup.loaded(), "FTFT", DB_SCAN0, tunables=ruled)
    assert fresh.evaluation == "formed" and fresh.formation.assumed_keys == ()


def test_t5b_route_a_refused_tap_reaches_the_page_as_409_with_its_message(monkeypatch):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from cobalt.cards import CardStateError
    from test_radar_card_routes import FakeCards, _card_settings, SETTINGS

    text = ("REFUSED card 1: assumed_formation is not graded on a card — "
            "an assumed default is ruled on the settings surface")

    class Refusing(FakeCards):
        def tap_dot(self, card_id, factor, grade, *, bands, enabled, now=None):
            raise CardStateError(text)

    fake = Refusing()
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    monkeypatch.setattr(web_module, "CardStore", lambda: fake)
    monkeypatch.setattr(web_module, "load_sheet_modes_config", lambda: SETTINGS.sheet_modes)
    monkeypatch.setattr(web_module, "_daymode_state", lambda: {
        "cfg": SETTINGS.daymode, "mode": "reduced", "row": {"attested_sheet": "half.htk"}, "error": None,
    })
    monkeypatch.setattr(web_module, "CardSettingsReader",
                        lambda: type("R", (), {"current": lambda self: _card_settings()})())
    response = TestClient(web_module.app).post("/radar/card/1/dot/assumed_formation", data={"grade": "7"})
    assert response.status_code == 409 and response.json()["reason"] == text
