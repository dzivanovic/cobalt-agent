"""STEP-2 of the setups one build (FINAL C2) — the formation registries,
the mirrored frame, the ONE published row (R2-4 = B, per the launch row
R50), and the assumed-key closure (R2-2.2 B).

- §2.2–2.5: `TRIGGERS`, `STOPS`, `STRUCTURAL_REFS`, `ATOMS`, `RELATIONS`;
  `registry.evaluability` reads those tables (its own constants deleted)
  and names a symbol compared outside an atom's producible domain (E8).
- §2.1 [F-04]: the frame property — `negate_prices(eval_as_long(mirror(bars)))
  == eval_as_short(bars)` and `pred_as_long(mirror(bars)) == pred_as_short(bars)`;
  [R2F-12] the daily series is mirrored with the bars; X4, X6.
- R2-4.1 B: `by_side`; one frame formed → that frame; both → `not_formed`
  note `both_sides` + the long detail; neither → the LONG frame always; the
  stage's per-card reads use the card's OWN side (`evaluate.py` open-card
  lookup / the avoid that expires a card).
- R2-4.2 B: factor and seam observations once on the real bars.
- R2-2.2 B: the static closure; a convention row per convention.
- Lego (ii) at this step: the rubberband shapes and the shipped example are
  BYTE-IDENTICAL through the registries — pins captured on the STEP-1 code,
  excluding only the fields this step adds (named below).

R24 / L69: no value of the trader's anywhere; constructed configs only.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.radar.anatomy.bars import rth_only, working_bars
from cobalt.radar.anatomy.extension import TUNABLE_KEYS, ExtensionParams, detect_extension
from cobalt.radar.anatomy.structure import bar_break_trigger, structural_stop, tracked_extreme
from cobalt.radar.evaluate import working_minutes
from cobalt.session import session_clock
from cobalt.taxonomy.loader import load_tunables
from cobalt.taxonomy.trade_def import TradeDef
from test_radar_evaluate import World

UTC = timezone.utc
SCAN0 = shapes.SCAN0
CONVENTION_KEY = "anatomy.orientation.extension"  # A-01


def _sha(payload) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()


@pytest.fixture(scope="module")
def defs(tmp_path_factory) -> dict[str, sup.LoadedDef]:
    out = {}
    for name, valid_setups, htf in (
        ("mixed", shapes.MIXED, False), ("countertrend", shapes.COUNTERTREND_ONLY, False),
        ("full", shapes.MIXED, True),
    ):
        out[name] = shapes.load_note(tmp_path_factory.mktemp(name), f"shape-{name}-registries",
                                     shapes.rubberband_mapping(valid_setups, htf_avoid=htf))
    out["shipped"] = sup.loaded(TradeDef.from_unit(shapes.example_mapping(), slug="example-range-break",
                                                   name="Example Range Break"),
                                md5="fedcba9876543210fedcba9876543210")
    return out


def _run(at: datetime, ticker: str = "FTFT"):
    closed = [b for b in shapes.bars(ticker) if b.ts + timedelta(minutes=1) <= at]
    return tuple(rth_only(working_bars(closed, working_minutes(sup.defaults()), as_of=at), session_clock()))


# =====================================================================
# Lego (ii) — byte identity through the registries (pins on STEP-1 code)
# =====================================================================

#: Fields STEP-2 ADDS by design, excluded from the pins (every other field
#: must be byte-identical): on `MemberEvaluation` — `by_side`; on
#: `Formation` — `side_frame`, `anchor`, `trigger_outcome`, `stop_outcome`.
EVALUATION_ADDED = {"by_side"}
FORMATION_ADDED = {"side_frame", "anchor", "trigger_outcome", "stop_outcome"}
#: On the card spec: `formula_sha256` (the formula files are new bytes by
#: construction) and the `assumed_formation` dot's `engine_inputs` /
#: `engine_why` (the closure replaces STEP-1's unconditional constant, so
#: the dot names the convention ROW key). `tunables_sha256` moves because
#: committed `tunables.yaml` gains the convention row (R2-2.2 B): it is
#: asserted to be exactly the snapshot WITH that row, and mapped back to the
#: same snapshot WITHOUT it — the start-of-step digest.
CARD_EXCLUDED = {"formula_sha256"}


#: STEP-3 (FINAL C3a) moves three more things by design; the pins normalise
#: them exactly ([F-10], [F-11]): `MemberEvaluation.ema9` (seeded — the
#: health input), the new seam observation `atr_seeded`, the D1 atoms a
#: not-evaluable def no longer lists as missing, and the four rows committed
#: `tunables.yaml` gains (their keys excluded from the start digest).
STEP3_KEYS = ("dayrange.session", "frame.warmup_source", "slope_norm.bars", "vwap.anchor",
              # + STEP-4's three rows (D2 / D3 detector keys)
              "leg.consolidation_max_retrace", "range.micro.bound_flat_slope_atr", "range.micro.touch_tolerance_atr",
              # + STEP-5's `A-08` row, STEP-6's three convention rows
              "extension.snapback_bars_cleared", "catalyst_ref.resolver", "leg.pre_test", "extension.on_leg.form",
              # + STEP-7's two convention rows, STEP-8's four rows
              "levels.set", "level.rejected.rule", "range_break.retest_tolerance_atr", "range_prior.rule",
              "event.stop_hit.source", "turn_candle.rule",
              # + fix r3 F3's `A-24` row (R49)
              "leg.min_size_atr")


def _tunables_digests() -> tuple[str, str]:
    from cobalt.radar.evaluate import canonical_sha256

    rows = {k: row.model_dump(mode="json") for k, row in sorted(sup.engine_tunables().items())}
    defaults = sup.defaults().model_dump(mode="json")
    new = canonical_sha256({"rows": rows, "defaults": defaults})
    old = canonical_sha256({"rows": {k: v for k, v in rows.items() if k not in {CONVENTION_KEY, *STEP3_KEYS}},
                            "defaults": defaults})
    return new, old
PIN_EVALUATIONS = {
    "countertrend": "fd2f49725ecd80817bfacd857fc349817b7c75a462992c1a0c567e3932b78ad8",
    "full": "7d868974df741d145c01ced9ce498532b2545f7d061ad4ed7a1c33a5cdd2a44f",
    "mixed": "a8b8f0989a987cab67f30d2754d323e23d982f6e845876269df029831471d024",
    "shipped": "da0f0ef1aa0179ea2b07adf9f6ac4d64eec24dd705152b7e8eee4a2326877be7",
}
PIN_CARDS = {
    "countertrend": "7a0e5796e33ebbd01e68c6b7c66c6946c0a0419258f6adc3bf81f8811573450a",
    "mixed": "5c4dcce2c86b4ffb5526c25274b26578dcf24509c8ce119d0c8dde0629d9a3a7",
}


#: The ONE by-design value change inside a kept field: `Formation.assumed_keys`
#: names the convention's ROW key from STEP-2 (R2-2.2 B's closure replaces
#: STEP-1's constant `A-01`). Mapped back to the start-of-step spelling so the
#: pins still prove every other byte is unchanged.
RENAMED_KEYS = {"anatomy.orientation.extension": "A-01"}


def without_e9_shapes(dump: dict) -> dict:
    """E9 (FINAL §2.5) names every AST shape the interpreter cannot evaluate:
    a def that was already `not_evaluable` gains `Unsupported(<kind>)` in
    `missing` (and the seam's content-free `unspecified_atom`). Stripped
    here so the pin proves nothing ELSE changed."""
    from cobalt.radar.evaluate import seam_safe_missing_atoms

    if not any(m.startswith("Unsupported(") for m in dump["missing"]):
        return dump
    kept = [m for m in dump["missing"] if not m.startswith("Unsupported(")]
    return {**dump, "missing": kept,
            "detail": {**dump["detail"], "missing_atoms": list(seam_safe_missing_atoms(kept))}}


def _rth_only_ema9(ev) -> str | None:
    """The start-of-step `ema9`: EMA(ma.fast) of the RTH run alone, as dumped."""
    from cobalt.radar.anatomy.indicators import InsufficientBars, ema

    try:
        value = ema(ev.working, sup.defaults().ma.fast).value if ev.working else None
    except InsufficientBars:
        value = None
    return None if value is None else str(value)


def _evaluation_dump(ev, ld=None) -> dict:
    from test_setups_d1 import _unmoved

    step2 = _unmoved(ev, ld)  # STEP-3's exact normalisation (ema9, atr_seeded, served atoms)
    step2["ema9"] = _rth_only_ema9(ev)
    dump = without_e9_shapes({k: v for k, v in step2.items() if k not in EVALUATION_ADDED})
    if dump.get("formation"):
        dump["formation"] = {k: v for k, v in dump["formation"].items() if k not in FORMATION_ADDED}
        dump["formation"]["assumed_keys"] = [RENAMED_KEYS.get(k, k) for k in dump["formation"]["assumed_keys"]]
    return dump


def _card_dump(card: dict) -> dict:
    out = {k: v for k, v in card.items() if k not in CARD_EXCLUDED | {"dots"}}
    new, old = _tunables_digests()
    assert out["tunables_sha256"] in (new, old)
    out["tunables_sha256"] = old
    out["dots"] = [{k: v for k, v in d.model_dump(mode="json").items()
                    if not (d.factor == "assumed_formation" and k in {"engine_inputs", "engine_why"})}
                   for d in card["dots"]]
    return out


@pytest.mark.parametrize("name", sorted(PIN_EVALUATIONS))
def test_lego_ii_every_evaluation_is_byte_identical_through_the_registries(defs, name):
    dumps = [_evaluation_dump(ev, defs[name]) for ticker in ("FTFT", "BGFI")
             for _, ev in shapes.every_scan(defs[name], ticker)]
    assert _sha(dumps) == PIN_EVALUATIONS[name]


@pytest.mark.parametrize("name", sorted(PIN_CARDS))
def test_lego_ii_every_card_spec_is_byte_identical_through_the_registries(defs, name):
    world = World(defs=[defs[name]])
    made = []
    for at, ev in shapes.every_scan(defs[name], "FTFT"):
        if ev.evaluation == "formed":
            made += world.scan(at).created
    assert made
    assert _sha([_card_dump(world.cards.cards[c]) for c in made]) == PIN_CARDS[name]


# =====================================================================
# §2.2–2.5 — the registries and the ONE path for "what is served"
# =====================================================================


def test_the_five_tables_exist_and_serve_the_rubberband_bricks():
    from cobalt.radar.formation.atoms import ATOMS, RELATIONS
    from cobalt.radar.formation.stops import STOPS, STRUCTURAL_REFS
    from cobalt.radar.formation.triggers import TRIGGERS
    from cobalt.taxonomy.trade_def import StructuralRef, TriggerType

    assert TRIGGERS[TriggerType.BAR_BREAK].serves({"bars_cleared": 2})
    assert not TRIGGERS[TriggerType.BAR_BREAK].serves({})
    assert "structural_extreme" in STOPS
    assert {StructuralRef.SNAPBACK_CANDLE, StructuralRef.TURN_LOW} <= set(STRUCTURAL_REFS)
    assert {"Extension.state", "Extension.instantiated", "Extension.leg_count",
            "RangeBreak(HTF).day_count"} <= set(ATOMS)
    # STEP-5 (FINAL §3 D4): the lifecycle grows the producible domain.
    assert ATOMS["Extension.state"].domain == frozenset({"culminating", "reverting", "backside", "none"})
    assert isinstance(RELATIONS, dict)


def test_the_registry_keeps_no_constants_of_its_own():
    from cobalt.radar.anatomy import registry

    for name in ("SUPPORTED_ATOMS", "SUPPORTED_TRIGGERS", "SUPPORTED_STOP_REFS"):
        assert not hasattr(registry, name), name


def test_e8_a_symbol_outside_the_atoms_domain_is_not_evaluable():
    from cobalt.radar.anatomy.registry import evaluability

    # STEP-5 re-point (FINAL §3 D4): `reverting` / `backside` are produced now;
    # `building` / `resuming` have no rule, so they are the out-of-domain case.
    td = sup.anatomy_def(preconditions=[{"expr": "Extension.state IN {building, resuming}"}])
    result = evaluability(td)
    assert not result.evaluable
    assert {"Extension.state∌building", "Extension.state∌resuming"} <= set(result.missing_atoms)
    assert evaluability(sup.anatomy_def(preconditions=[{"expr": "Extension.state == culminating"}])).evaluable
    assert evaluability(sup.anatomy_def(preconditions=[{"expr": "Extension.state IN {reverting, backside}"}])).evaluable


def test_e9_every_unsupported_shape_is_named_and_the_registry_agrees_with_the_interpreter(defs):
    """The property: registry evaluable ⇔ the interpreter raises no
    `Unsupported` on the def; when not evaluable, the interpreter reports the
    registry's missing set."""
    from cobalt.radar.anatomy.registry import evaluability

    cases = [*defs.values(),
             sup.loaded(sup.anatomy_def(preconditions=[{"expr": "Leg(pullback) touched VWAP"}]),
                        md5="00000000000000000000000000000001"),
             sup.loaded(sup.anatomy_def(preconditions=[{"expr": "Extension.state IN {reverting}"}]),
                        md5="00000000000000000000000000000002"),
             sup.loaded(sup.anatomy_def(preconditions=[{"expr": "Extension.leg_count * 2 >= 4"}]),
                        md5="00000000000000000000000000000003")]
    for ld in cases:
        reg = evaluability(ld.definition)
        ev = shapes.evaluate(ld, "FTFT", SCAN0)
        if reg.evaluable:
            assert not (ev.evaluation == "not_evaluable" and ev.detail.extension_path != "B_only"), (ld.slug, ev.missing)
        else:
            assert ev.evaluation == "not_evaluable" and set(ev.missing) == set(reg.missing_atoms), ld.slug


# =====================================================================
# §2.1 [F-04] — the frame property, X4, X6
# =====================================================================


def test_f04_the_frame_property_on_every_scan_of_the_committed_day():
    from cobalt.radar.anatomy.frame import mirror_bars

    params = ExtensionParams.from_tunables(sup.engine_tunables())
    buffer = Decimal(str(sup.engine_tunables()["stop.buffer"].value))
    checked = 0
    for m in range(40, 391, 2):
        run = _run(shapes.DAY_START + timedelta(minutes=m))
        if len(run) < 21:
            continue
        mirrored = mirror_bars(run)
        real, mirr = detect_extension(run, params), detect_extension(mirrored, params)
        # predicates: pred_as_long(mirror(bars)) == pred_as_short(bars)
        assert (mirr.state, mirr.instantiated, mirr.leg_count, mirr.path) == (
            real.state, real.instantiated, real.leg_count, real.path)
        # price outputs: negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)
        if real.session_open is None:
            assert mirr.session_open is None and mirr.last_close is None
        else:
            assert (-mirr.session_open, -mirr.last_close) == (real.session_open, real.last_close)
        if real.direction is not None:
            assert {real.direction, mirr.direction} == {"up", "down"}
            assert -tracked_extreme(mirrored, mirr.direction).price == tracked_extreme(run, real.direction).price
        if all(b.complete for b in run[-2:]):
            assert -bar_break_trigger(mirrored, 2, "long").price == bar_break_trigger(run, 2, "short").price
            assert -bar_break_trigger(mirrored, 2, "short").price == bar_break_trigger(run, 2, "long").price
        extreme = max(b.high for b in run)
        assert -structural_stop(-extreme, "long", buffer).price == structural_stop(extreme, "short", buffer).price
        checked += 1
    assert checked > 100


def test_r2f12_the_daily_series_is_mirrored_with_the_bars():
    from cobalt.radar.anatomy.daily import htf_range_break
    from cobalt.radar.anatomy.frame import mirror_bars, mirror_daily

    daily = sup.fixture_daily("FTFT", SCAN0)
    run = _run(SCAN0)
    real = htf_range_break(daily, sup.TRADE_DATE, session_high=max(b.high for b in run),
                           session_low=min(b.low for b in run))
    mirrored_run = mirror_bars(run)
    mirr = htf_range_break(mirror_daily(daily), sup.TRADE_DATE, session_high=max(b.high for b in mirrored_run),
                           session_low=min(b.low for b in mirrored_run))
    assert mirr.day_count == real.day_count
    assert {real.direction, mirr.direction} in ({"up", "down"}, {None})


def test_x4_the_ten_cent_grid_and_the_stop_sweep_on_negated_extremes():
    from cobalt.radar.anatomy.structure import _on_ten_cent_grid

    assert _on_ten_cent_grid(Decimal("-10.00")) and not _on_ten_cent_grid(Decimal("-10.04"))
    unequal = []
    for cents in range(480, 621):
        for sub in ("", "5"):
            extreme = Decimal(f"{cents / 100:.2f}{sub}")
            for buffer in (Decimal("0.01"), Decimal("0.02"), Decimal("0.05")):
                for side, other in (("short", "long"), ("long", "short")):
                    real = structural_stop(extreme, side, buffer)
                    mirr = structural_stop(-extreme, other, buffer)
                    if -mirr.price != real.price or mirr.nudged != real.nudged:
                        unequal.append((extreme, buffer, side))
    assert unequal == []


def test_x6_the_frame_wraps_working_bars_and_never_round_trips_through_the_archiver_bar():
    from cobalt.archiver.models import Bar, Interval
    from cobalt.radar.anatomy.bars import WorkingBar
    from cobalt.radar.anatomy.frame import mirror_bars

    try:
        Bar(ticker="FTFT", interval=Interval.I1, ts=SCAN0, open=Decimal("-5"), high=Decimal("-4.9"),
            low=Decimal("-5.1"), close=Decimal("-5"), volume=1)
        outcome = "constructs"
    except Exception as e:  # noqa: BLE001 — the experiment records what happens
        outcome = f"refused: {type(e).__name__}"
    print(f"X6: a negative-price archiver Bar {outcome}")
    assert all(isinstance(b, WorkingBar) for b in mirror_bars(_run(SCAN0)))


# =====================================================================
# R2-4 = B — the ONE published row, and the stage's per-card reads
# =====================================================================


def test_b_the_mirrored_frame_forms_and_is_the_published_row(defs):
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    assert ev.by_side["short"].evaluation == "formed" and ev.by_side["long"].evaluation == "not_formed"
    assert ev.evaluation == "formed" and ev.direction == "short"
    assert ev.formation.side_frame == "mirrored"
    assert ev.formation.stop.price > ev.formation.trigger.price > 0  # real-world coordinates


def test_b_publication_rule_both_neither_and_one(defs):
    from cobalt.radar.evaluate import publish_frames

    formed = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    long_formed = formed.model_copy(update={"direction": "long"})
    quiet = shapes.evaluate(defs["mixed"], "FTFT", datetime(2026, 1, 6, 15, 0, tzinfo=UTC))
    assert quiet.evaluation != "formed"
    both = publish_frames(long=long_formed, short=formed)
    assert (both.evaluation, both.note, both.formation, both.direction) == ("not_formed", "both_sides", None, None)
    assert both.detail == long_formed.detail
    assert publish_frames(long=quiet, short=quiet.model_copy(update={"note": "short"})) .note == quiet.note
    assert publish_frames(long=quiet, short=formed).evaluation == "formed"
    assert publish_frames(long=formed.model_copy(update={"direction": "long"}), short=quiet).direction == "long"
    # X21: deterministic — the same pair selects the same row
    assert publish_frames(long=quiet, short=formed) == publish_frames(long=quiet, short=formed)


def test_b_an_open_short_card_is_not_expired_by_the_long_frames_avoid(defs, monkeypatch):
    """The stage's open-card lookup and the avoid that expires a card read the
    CARD'S OWN side (`by_side[card.direction]`), never the published row."""
    from cobalt.radar import evaluate as evaluate_mod

    world = World(defs=[defs["mixed"]])
    assert world.scan(SCAN0).created == [1]
    real = evaluate_mod.evaluate_member

    def long_side_avoided(*args, **kwargs):
        ev = real(*args, **kwargs)
        avoided = ev.by_side["long"].model_copy(update={"evaluation": "avoided"})
        not_formed = ev.by_side["short"].model_copy(update={"evaluation": "not_formed", "formation": None})
        return ev.model_copy(update={"evaluation": "avoided", "formation": None, "direction": None,
                                     "by_side": {"long": avoided, "short": not_formed}})

    monkeypatch.setattr(evaluate_mod, "evaluate_member", long_side_avoided)
    outcome = world.scan(SCAN0 + timedelta(seconds=100))
    assert outcome.refreshed == [1] and outcome.expired == []
    assert world.cards.cards[1]["state"] == "WATCH"


def test_x21_both_frames_round_trip_through_the_receipt(defs):
    from cobalt.radar.evaluate import replay_receipt

    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    evaluations, _cards = replay_receipt(list(world.cards.receipts), clock=session_clock())
    live = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    assert evaluations[0].by_side == live.by_side


def test_x25_every_reader_of_the_published_direction_reads_the_short_side(defs, tmp_path):
    from cobalt.radar.evaluate_cli import replay_formations
    from test_radar_evaluate_cli import ReadOnlyRadar, _daily

    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    board = world.radar.board("pool")
    assert board[0]["direction"] == "short" and board[0]["evaluation"] == "formed"
    radar = ReadOnlyRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    report = replay_formations(sup.TRADE_DATE, pool_key="pool", slug_filter=None, radar_store=radar,
                               defs_source=lambda: ([defs["mixed"]], {}), daily_source=_daily,
                               tunables=sup.engine_tunables(), defaults=sup.defaults(), clock=session_clock(),
                               out=lambda _l: None)
    assert report.formations and {f.direction for f in report.formations} == {"short"}


def test_x18_factor_observations_on_the_real_and_the_mirrored_bars(defs):
    """X18: `atrs_from_open`, `Extension.leg_count`, `htf_level_proximity` on
    the real bars and on the mirrored frame, every scan of the committed day
    (offline half; the stored-day half runs at the deploy)."""
    from cobalt.radar.anatomy.daily import htf_level_proximity
    from cobalt.radar.anatomy.frame import mirror_bars, mirror_daily

    params = ExtensionParams.from_tunables(sup.engine_tunables())
    daily = sup.fixture_daily("FTFT", SCAN0)
    differs = {"atrs_from_open": 0, "Extension.leg_count": 0, "htf_level_proximity": 0}
    scans = 0
    for m in range(40, 391, 2):
        run = _run(shapes.DAY_START + timedelta(minutes=m))
        if len(run) < 21:
            continue
        real, mirr = detect_extension(run, params), detect_extension(mirror_bars(run), params)
        differs["atrs_from_open"] += real.distance_from_open_atr != mirr.distance_from_open_atr
        differs["Extension.leg_count"] += real.leg_count != mirr.leg_count
        last = run[-1].close
        a = htf_level_proximity(daily, sup.TRADE_DATE, last)
        b = htf_level_proximity(mirror_daily(daily), sup.TRADE_DATE, -last)
        differs["htf_level_proximity"] += a.value != b.value
        scans += 1
    print(f"X18: scans={scans} differences={differs}")
    assert differs == {"atrs_from_open": 0, "Extension.leg_count": 0, "htf_level_proximity": 0}


def test_x12_a_mirrored_frame_card_carries_no_negative_price_and_no_long_side_label(defs):
    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    card = world.cards.cards[1]
    ev = card["evidence"]
    assert card["direction"] == "short"
    for price in (card["trigger_price"], card["structural_stop"], Decimal(ev["trigger"]["price"]),
                  Decimal(ev["stop"]["price"]), Decimal(ev["stop"]["raw"]), Decimal(ev["stop"]["rounded"]),
                  Decimal(ev["stop"]["extreme"]), Decimal(ev["extreme"]["price"])):
        assert price > 0
    assert ev["trigger"]["trade_direction"] == "short" and ev["stop"]["trade_direction"] == "short"
    assert ev["extreme"]["side"] == "high"
    assert "short" in card["why"] and "long" not in card["why"]
    for atom in ev["atoms"]:
        assert atom.get("number") is None or Decimal(atom["number"]) >= 0


# =====================================================================
# R2-2.2 B — the static closure and the convention rows
# =====================================================================


def test_the_a01_convention_has_an_engine_row_null_and_proposed():
    row = load_tunables().by_key[CONVENTION_KEY]
    assert (row.value, row.unit.value, row.status.value, row.scope, row.dynamic) == (
        None, "label", "proposed", "global", False)


def test_a_null_convention_row_counts_as_assumed_and_names_the_row_key(defs):
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0)
    assert ev.formation.assumed_keys == (CONVENTION_KEY,)
    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    dot = [d for d in world.cards.cards[1]["dots"] if d.factor == "assumed_formation"][0]
    assert dot.engine_inputs == {"assumed_keys": [CONVENTION_KEY]} and CONVENTION_KEY in dot.engine_why


def _with_convention(value, source):
    from cobalt.taxonomy.tunables import TunableSource

    tunables = dict(sup.engine_tunables())
    tunables[CONVENTION_KEY] = tunables[CONVENTION_KEY].model_copy(
        update={"value": value, "source": TunableSource(source)})
    return tunables


def test_a_ruled_convention_leaves_the_closure_and_an_assumed_one_stays(defs):
    from cobalt.radar.evaluate import CONVENTION_LABELS

    label = CONVENTION_LABELS[CONVENTION_KEY]
    ruled = shapes.evaluate(defs["mixed"], "FTFT", SCAN0, tunables=_with_convention(label, "ruling"))
    assert ruled.evaluation == "formed" and ruled.formation.assumed_keys == ()
    assumed = shapes.evaluate(defs["mixed"], "FTFT", SCAN0, tunables=_with_convention(label, "assumed"))
    assert assumed.formation.assumed_keys == (CONVENTION_KEY,)


def test_a_label_the_code_does_not_implement_is_not_evaluable_named(defs):
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0, tunables=_with_convention("some_other_rule", "ruling"))
    assert ev.evaluation == "not_evaluable"
    assert f"{CONVENTION_KEY}=some_other_rule" in ev.missing


def test_the_closure_holds_a_cfg_key_the_def_names_when_its_row_is_assumed(defs):
    from cobalt.taxonomy.tunables import TunableSource

    tunables = dict(sup.engine_tunables())
    tunables["stop.buffer"] = tunables["stop.buffer"].model_copy(update={"source": TunableSource.ASSUMED})
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0, tunables=tunables)
    assert set(ev.formation.assumed_keys) == {CONVENTION_KEY, "stop.buffer"}


def test_the_closure_holds_a_detectors_tunable_keys_when_its_row_is_assumed(defs):
    from cobalt.taxonomy.tunables import TunableSource

    tunables = dict(sup.engine_tunables())
    tunables["extension.path_b_atr"] = tunables["extension.path_b_atr"].model_copy(
        update={"source": TunableSource.ASSUMED})
    ev = shapes.evaluate(defs["mixed"], "FTFT", SCAN0, tunables=tunables)
    assert set(ev.formation.assumed_keys) == {CONVENTION_KEY, "extension.path_b_atr"}


def test_a_detector_reads_only_its_own_tunable_keys():
    rows = sup.engine_tunables()
    assert ExtensionParams.from_tunables({k: rows[k] for k in TUNABLE_KEYS}) == ExtensionParams.from_tunables(rows)


class _RecordingRows(dict):
    """X22's test-only instrumentation: every tunable key a resolver reads."""

    def __init__(self, rows):
        super().__init__(rows)
        self.read: set[str] = set()

    def __getitem__(self, key):
        self.read.add(key)
        return super().__getitem__(key)

    def get(self, key, default=None):
        self.read.add(key)
        return super().get(key, default)

    def __contains__(self, key):
        self.read.add(key)
        return super().__contains__(key)


def test_x22_the_declared_closure_covers_every_instrumented_read(defs):
    """X22 (FINAL: "Compare declared closures against instrumented reads in
    fixtures covering cfg, trigger, stop, detector and convention paths") —
    a verification tool, not a production recorder. Every formed and
    non-formed scan of the committed day, both frames."""
    from cobalt.radar.evaluate import closure_keys

    for name in ("mixed", "countertrend", "full"):
        ld = defs[name]
        rows = _RecordingRows(sup.engine_tunables())
        for m in range(0, 391, 10):
            shapes.evaluate(ld, "FTFT", shapes.DAY_START + timedelta(minutes=m), tunables=rows)
        declared = closure_keys(ld.definition)
        print(f"X22 {name}: reads={sorted(rows.read)} declared={sorted(declared)}")
        assert rows.read <= declared, sorted(rows.read - declared)


def test_x7_scans_where_both_frames_satisfy_the_def_on_the_committed_day(defs):
    """X7 (FINAL, per unlocked def: the count of scans where BOTH frames
    satisfy the def). Offline half, the committed day; a `both_sides` scan
    where either frame alone would have formed is a FAIL."""
    for name in ("mixed", "countertrend", "full"):
        rows = [ev for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(defs[name], ticker)]
        both = sum(ev.by_side["long"].evaluation == ev.by_side["short"].evaluation == "formed" for ev in rows)
        print(f"X7 {name}: scans={len(rows)} both_sides={both}")
        assert both == 0


def test_x8_source_half_an_open_card_keeps_its_dot_after_the_row_is_ruled(defs):
    """X8's `source` half (Fable R2 (c)): the open card keeps the dot, the
    null score and the suppression after its convention row reads `ruling`;
    a NEW formation after the flip carries no dot for that key."""
    from cobalt.radar.evaluate import CONVENTION_LABELS

    world = World(defs=[defs["mixed"]])
    world.scan(SCAN0)
    ruled = _with_convention(CONVENTION_LABELS[CONVENTION_KEY], "ruling")
    world.stage.tunables_loader = lambda: ruled
    world.scan(SCAN0 + timedelta(seconds=100))
    card = world.cards.cards[1]
    assert [d.factor for d in card["dots"]][-1] == "assumed_formation"
    assert card["card_score"] is None and "assumed_formation" in card["score_suppressed"]
    fresh = shapes.evaluate(defs["mixed"], "FTFT", SCAN0, tunables=ruled)
    assert fresh.formation.assumed_keys == ()
