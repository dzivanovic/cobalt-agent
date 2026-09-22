"""Setups fix round 3 (prompt `33-setups-fix-r3.md`) — his rulings R47, R48,
R49, R50, R51 and R61 (`cto-2026-09-22.md` §4), one section per row.

Every constructed series is written from the definitions' words; every
threshold and every filled hole is a literal of this file's own choosing
(L69) — never a value of his, of a cheat sheet, or of the assumed-values
companion (L32). R24 holds: no day is chosen because he traded it.
"""

from __future__ import annotations

from datetime import timedelta
from decimal import Decimal

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
import test_setups_d4 as d4
from cobalt.session import session_clock


def _evaluate(ld, bars, at, rows=None):
    from cobalt.radar.evaluate import evaluate_member

    return evaluate_member(ld, d4._member(bars, at), tunables=rows if rows is not None else shapes.tunables_for(ld),
                           defaults=sup.defaults(), scan_interval=100, clock=session_clock())


# =====================================================================
# F1 — R47: `backside` / `fashionably-late` bind side through the mirrored
# frame on their own long-side text (Grok's fix), never through a direction
# recomputed from last close − session open.
# =====================================================================


def test_f1_the_backside_shape_forms_long_on_a_day_that_recovers_past_the_open():
    """X10's own case: a run down, its culmination, the turn, a snapback and a
    backside, then a recovery PAST the session open. The long-side text's
    Extension is the down one the long trade opposes; the long frame binds it."""
    ld = shapes.load_shape_fresh("backside")
    bars = d4.run_down_then_backside(above_open=True)
    at = d4._scan_after(bars)
    assert bars[-1].close > Decimal(10)  # last > the 10.00 session open
    ev = _evaluate(ld, bars, at)
    print(f"F1 backside past the open: evaluation={ev.evaluation} direction={ev.direction} "
          f"long={ev.by_side['long'].evaluation}/{ev.by_side['long'].note} "
          f"short={ev.by_side['short'].evaluation}/{ev.by_side['short'].note}")
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.note, ev.by_side)
    f = ev.formation
    assert f.anchor.object == "Extension" and f.anchor.direction == "down" and f.stop_ref == "recent_higher_low"
    assert f.formed_bar_ts == d4._et(10, 10)  # the down run's culminating bucket, held past the open
    assert f.stop.price < min(f.trigger.price, ev.last_price)


def test_f1_the_backside_shape_on_the_mirrored_day_forms_short():
    """The mirrored frame gives the other side: the same construction with
    every price reflected forms SHORT — the side comes from the frame."""
    from cobalt.archiver.models import Bar

    ld = shapes.load_shape_fresh("backside")
    flip = lambda b: b.model_copy(update={"open": 20 - b.open, "high": 20 - b.low, "low": 20 - b.high,  # noqa: E731
                                          "close": 20 - b.close})
    bars = [flip(b) for b in d4.run_down_then_backside(above_open=True)]
    assert all(isinstance(b, Bar) for b in bars)
    ev = _evaluate(ld, bars, d4._scan_after(bars))
    print(f"F1 backside mirrored: evaluation={ev.evaluation} direction={ev.direction}")
    assert ev.evaluation == "formed" and ev.direction == "short", (ev.evaluation, ev.note, ev.by_side)


#: The scan of the fashionably-late case past the open: the recovery bucket that
#: closes above the 10.00 open is the 10:30 one, closed at 10:32.
LATE_PAST_OPEN_SCAN = d4._et(10, 34)


def test_f1_the_fashionably_late_shape_forms_long_after_the_day_recovers_past_the_open():
    """The same construction read by the late-cross shape at a scan where last >
    open; its two flat thresholds are this file's constructed fills
    (`setups_shapes.D4_CONSTRUCTED`, L69 — committed config keeps them null)."""
    ld = shapes.load_shape_fresh("fashionably-late")
    bars = [b for b in d4.run_down_then_backside(above_open=True) if b.ts + timedelta(minutes=1) <= LATE_PAST_OPEN_SCAN]
    assert bars[-1].close > Decimal(10)
    ev = _evaluate(ld, bars, LATE_PAST_OPEN_SCAN)
    print(f"F1 fashionably-late past the open: evaluation={ev.evaluation} direction={ev.direction} "
          f"long={ev.by_side['long'].evaluation}/{ev.by_side['long'].note} "
          f"short={ev.by_side['short'].evaluation}/{ev.by_side['short'].note}")
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.note, ev.by_side)
    assert ev.formation.trigger_outcome.kind == "indicator_cross" and ev.formation.anchor.direction == "down"


def test_f1_only_a_def_naming_a_state_past_the_culmination_binds_side_by_the_frame():
    """FINAL fact 3 stands for rubberband (`:64`): only a def whose text names
    a state past the culmination binds side through the frame; the reversal
    shape and the four with-trend shapes keep the detector's own direction
    (their pins in their own modules are the behavioural guard)."""
    from cobalt.radar.anatomy.frame import binds_side_by_frame

    assert not binds_side_by_frame(shapes.load_shape_fresh("rubberband").definition)
    assert binds_side_by_frame(shapes.load_shape_fresh("backside").definition)
    assert binds_side_by_frame(shapes.load_shape_fresh("fashionably-late").definition)
    for key in ("hitchhiker", "nine-ema-scalp", "vwap-continuation", "second-chance"):
        assert not binds_side_by_frame(shapes.load_shape_fresh(key).definition), key


# =====================================================================
# F2 — R48: the assumed-rows reader accepts a `per_indicator` HOLE
# =====================================================================

#: This file's own literal for the EMA9 flat threshold (L69; the build's
#: constructed fill, `setups_shapes.D4_CONSTRUCTED` — not a companion value).
EMA9_FLAT_LITERAL = shapes.D4_CONSTRUCTED["flat_threshold.ema9"][1]


def _assumed_row(key, value, unit, scope, source="assumed"):
    return {"key": key, "value": value, "unit": unit, "scope": scope, "dynamic": True, "status": "proposed",
            "source": source, "consumers": ["a detector"]}


def _write_assumed(root, rows):
    from cobalt.taxonomy.cli import assumed_note_text

    (root / "1 - Trading").mkdir(parents=True, exist_ok=True)
    (root / "1 - Trading" / "Assumed Defaults.md").write_text(assumed_note_text(rows))


def test_f2_a_per_indicator_hole_takes_an_assumed_row_and_marks_the_card(tmp_path):
    from cobalt.radar.evaluate import assumed_keys_of, card_dots
    from cobalt.settings.card import CardSettings
    from cobalt.taxonomy.loader import merge_tunables
    from cobalt.taxonomy.tunables import TunableSource
    from cobalt.taxonomy.vault_loader import load_vault_trade_defs
    from test_radar_evaluate import ENABLED_CARD  # a constructed config (L69)

    assert sup.engine_tunables()["flat_threshold.ema9"].value is None  # committed config: a hole
    _write_assumed(tmp_path, [_assumed_row("flat_threshold.ema9", float(EMA9_FLAT_LITERAL), "ratio",
                                           "per_indicator(ema9)")])
    engine_fills = {k: v for k, v in shapes.D4_CONSTRUCTED.items() if k != "flat_threshold.ema9"}
    ld = shapes.load_note(tmp_path, "example-fix-late-assumed", shapes.late_mapping(), engine=engine_fills)
    assumed = {t.key: t.row for t in load_vault_trade_defs(vault_root=tmp_path).user_tunables if t.slug is None}
    assert set(assumed) == {"flat_threshold.ema9"}
    tunables = merge_tunables(shapes.tunables_for(ld), assumed)
    row = tunables["flat_threshold.ema9"]
    assert (row.scope, row.source, row.value) == ("per_indicator(ema9)", TunableSource.ASSUMED,
                                                  float(EMA9_FLAT_LITERAL))

    bars = [b for b in d4.run_down_then_backside(above_open=True) if b.ts + timedelta(minutes=1) <= LATE_PAST_OPEN_SCAN]
    ev = _evaluate(ld, bars, LATE_PAST_OPEN_SCAN, rows=tunables)
    assert ev.evaluation == "formed", (ev.evaluation, ev.note, ev.by_side)
    print(f"F2: assumed_keys={ev.formation.assumed_keys}")
    assert "flat_threshold.ema9" in ev.formation.assumed_keys
    settings = CardSettings.from_rows(sup.fixture_settings_rows(**ENABLED_CARD))
    dots = card_dots(ld, ev, settings, LATE_PAST_OPEN_SCAN, ev.formation.assumed_keys)
    assert "flat_threshold.ema9" in assumed_keys_of(dots)


@pytest.mark.parametrize("row, named", [
    # a per_indicator row for a key whose engine row is not a null hole
    (_assumed_row("stop.buffer", 0.03, "cents", "per_indicator(ema9)"), "stop.buffer"),
    # a per_indicator(<ind>) whose <ind> differs from the engine row's
    (_assumed_row("flat_threshold.ema9", 0.07, "ratio", "per_indicator(vwap)"), "flat_threshold.ema9"),
    # a per_indicator row for a key with no engine row at all
    (_assumed_row("flat_threshold.rsi", 0.07, "ratio", "per_indicator(rsi)"), "flat_threshold.rsi"),
])
def test_f2_any_other_per_indicator_row_is_refused_loudly(tmp_path, row, named):
    from cobalt.taxonomy.vault_loader import VaultTaxonomyError, load_assumed_tunables

    _write_assumed(tmp_path, [row])
    with pytest.raises(VaultTaxonomyError) as e:
        load_assumed_tunables(tmp_path, loaded_slugs=set())
    print(f"F2 refusal: {e.value}")
    assert named in str(e.value) and "per_indicator" in str(e.value)


def test_f2_a_sheet_sourced_per_indicator_row_is_still_refused(tmp_path):
    from cobalt.taxonomy.vault_loader import VaultTaxonomyError, load_assumed_tunables

    _write_assumed(tmp_path, [_assumed_row("flat_threshold.ema9", 0.07, "ratio", "per_indicator(ema9)",
                                           source="sheet")])
    with pytest.raises(VaultTaxonomyError, match="source 'sheet'"):
        load_assumed_tunables(tmp_path, loaded_slugs=set())


# =====================================================================
# F3 — R49: the minimum-size rule for `impulse` / `pullback` legs
# (`A-24`, `leg.min_size_atr`, `value: null` in committed config)
# =====================================================================

MIN_SIZE_KEY = "leg.min_size_atr"
#: This file's own literals (L69): a working-TF ATR and a minimum between the
#: small and the large legs below (in ATR).
ATR, MIN_LITERAL = Decimal("0.2"), Decimal("1.5")


def _leg(direction, t, low, high):
    from datetime import datetime, timezone

    from cobalt.radar.anatomy.leg import LegObservation

    ts = datetime(2026, 1, 6, 15, t, tzinfo=timezone.utc)
    return LegObservation(direction=direction, start_ts=ts, end_ts=ts, bar_count=1, terminated=True,
                          high=Decimal(high), low=Decimal(low))


#: up drive · LARGE pullback (0.60 = 3 ATR) · up impulse · SMALL pullback (0.05 = ¼ ATR)
SMALL_LAST = [_leg("up", 0, "10.00", "11.00"), _leg("down", 2, "10.40", "11.00"),
              _leg("up", 4, "10.40", "11.20"), _leg("down", 6, "11.15", "11.20")]
#: up drive · LARGE pullback · a SMALL up leg (0.05) · LARGE pullback — the only "impulse" is small
SMALL_IMPULSE = [_leg("up", 0, "10.00", "11.00"), _leg("down", 2, "10.40", "11.00"),
                 _leg("up", 4, "10.40", "10.45"), _leg("down", 6, "9.80", "10.45")]


def test_f3_a_leg_below_the_minimum_is_not_a_pullback_the_large_one_is():
    from cobalt.radar.anatomy.leg_roles import pullback_roles

    today = pullback_roles(SMALL_LAST)
    assert today.pullback == SMALL_LAST[3]  # null key: the latest down leg, whatever its size
    sized = pullback_roles(SMALL_LAST, min_size=MIN_LITERAL, atr=ATR)
    assert sized.pullback == SMALL_LAST[1] and sized.index == 1
    assert (sized.before, sized.before_role) == (SMALL_LAST[0], "opening_drive")


def test_f3_an_impulse_below_the_minimum_is_not_an_impulse():
    from cobalt.radar.anatomy.leg_roles import pullback_roles

    today = pullback_roles(SMALL_IMPULSE)
    assert (today.before_role, today.before.direction) == ("impulse", "up")  # holds today
    sized = pullback_roles(SMALL_IMPULSE, min_size=MIN_LITERAL, atr=ATR)
    assert sized.pullback == SMALL_IMPULSE[3] and sized.index == 2
    assert (sized.before, sized.before_role) == (None, None)  # `Leg(opening_drive OR impulse)` no longer holds


def _nine_ema_rows(value):
    rows = shapes.tunables_for(shapes.load_shape_fresh("nine-ema-scalp"))
    if value is not None:
        rows[MIN_SIZE_KEY] = rows[MIN_SIZE_KEY].model_copy(update={"value": value})
    return rows


def test_f3_on_the_definition_written_day_the_minimum_reaches_the_frame_and_the_formation():
    """The nine-ema day (`test_setups_nine_ema.impulse_pullback_rejection`): its
    pullback is about half a working-TF ATR. Key null → today's roles and the
    formation; this file's literal above that pullback → no pullback, no formation."""
    import test_setups_nine_ema as ne
    from cobalt.radar.evaluate import evaluate_member, member_frames

    bars = ne.impulse_pullback_rejection()
    at = ne._scan_after(bars)
    ld = shapes.load_shape_fresh("nine-ema-scalp")
    for value, pulls, forms in ((None, True, True), (MIN_LITERAL, False, False)):
        rows = _nine_ema_rows(value)
        fr = member_frames(ne._member(bars, at), tunables=rows, defaults=sup.defaults(), clock=session_clock())["long"]
        atom = fr.atoms["Leg(pullback).direction"]
        ev = evaluate_member(ld, ne._member(bars, at), tunables=rows, defaults=sup.defaults(), scan_interval=100,
                             clock=session_clock())
        print(f"F3 nine-ema day, {MIN_SIZE_KEY}={value}: pullback atom={atom.kind}/{atom.symbol} "
              f"evaluation={ev.evaluation}")
        assert (atom.kind == "symbol") is pulls
        assert (ev.evaluation == "formed") is forms


#: The pullback / impulse roles of every leg, both frames, FTFT and BGFI, every
#: 10 minutes of the committed day — computed on the code BEFORE F3 (`leg_roles.py`
#: byte-identical to `65c08a0`), copied verbatim from that run's failure output.
PIN_ROLES_COMMITTED_DAY = "0922dadc29013941a7a2512e038ba9310e4fb791bc3a5e53bdd17a4bf5dd6323"


def test_f3_with_the_key_null_every_role_on_the_committed_day_is_the_bases():
    import hashlib
    import json

    from cobalt.radar.evaluate import member_frames

    rows = sup.engine_tunables()
    assert rows.get(MIN_SIZE_KEY) is None or rows[MIN_SIZE_KEY].value is None  # committed config: null
    dumps = []
    for ticker in ("FTFT", "BGFI"):
        for m in range(0, 391, 10):
            at = shapes.DAY_START + timedelta(minutes=m)
            frames = member_frames(shapes.member(ticker, at), tunables=rows, defaults=sup.defaults(),
                                   clock=session_clock())
            for side in ("long", "short"):
                r = frames[side].objects["pullback_roles"]
                dumps.append(r.model_dump(mode="json", include={"pullback", "index", "before", "before_role"}))
    sha = hashlib.sha256(json.dumps(dumps, sort_keys=True, default=str).encode()).hexdigest()
    print(f"F3 roles on the committed day: {len(dumps)} observations sha={sha}")
    assert sha == PIN_ROLES_COMMITTED_DAY


def test_f3_the_key_is_a_null_engine_row_in_the_closure_of_every_def_naming_the_roles():
    from cobalt.radar.evaluate import assumed_closure, closure_keys
    from cobalt.taxonomy.tunables import TunableSource

    row = sup.engine_tunables()[MIN_SIZE_KEY]
    assert (row.value, row.unit.value, row.scope) == (None, "atr", "global")
    naming = {key for key, shape in shapes.SHAPES.items()
              if any(a.startswith(("Leg(pullback)", "Leg(impulse)", "Leg(opening_drive OR impulse)"))
                     for p in shapes.load_shape_fresh(key).definition.preconditions for a in p.required_atoms)}
    print(f"F3 defs naming Leg(impulse) / Leg(pullback): {sorted(naming)}")
    assert naming == {"nine-ema-scalp", "vwap-continuation"}
    for key in shapes.SHAPES:
        td = shapes.load_shape_fresh(key).definition
        assert (MIN_SIZE_KEY in closure_keys(td)) is (key in naming), key
    td = shapes.load_shape_fresh("nine-ema-scalp").definition
    rows = _nine_ema_rows(float(MIN_LITERAL))
    rows[MIN_SIZE_KEY] = rows[MIN_SIZE_KEY].model_copy(update={"source": TunableSource.ASSUMED})
    assert MIN_SIZE_KEY in assumed_closure(td, rows)  # a card formed on it is marked ASSUMED


# =====================================================================
# F4 — R50: a FILLED card's health pills skip `assumed_formation`
# =====================================================================


def _thresholds():
    from cobalt.cards.health import HealthThresholds

    return HealthThresholds(participation_warn=Decimal("0.7"), participation_bad=Decimal("0.4"),
                            cost_warn=Decimal("1.5"), cost_bad=Decimal("2.5"), dot_warn_drop=2, dot_bad_max=3,
                            structural_warn="touched", structural_bad="lost_on_close")  # this file's literals


def _graded(factor, position, grade):
    from cobalt.cards.scoring import Dot

    return Dot(factor=factor, position=position, source="cobalt", tier="deterministic", role="shadow",
               engine_grade=grade)


def _assumed_dot(position):
    from cobalt.cards.scoring import ASSUMED_FORMATION, Dot

    return Dot(factor=ASSUMED_FORMATION, position=position, source="cobalt-degraded", tier="deterministic",
               role="shadow", na_reason="ASSUMED", engine_inputs={"assumed_keys": ["a.key"]},
               engine_why="formed on assumed defaults: a.key")


def test_f4_a_filled_cards_dot_pills_skip_assumed_formation():
    from cobalt.cards.health import dot_pills

    dots = [_graded("factor_a", 0, 7), _graded("factor_b", 1, 6), _assumed_dot(2)]
    pills = dot_pills(entry_grades={"factor_a": 8, "factor_b": 6}, dots=dots, t=_thresholds())
    print(f"F4 pills: {[(p.label, p.status) for p in pills]}")
    assert [p.label for p in pills] == ["factor_a", "factor_b"]
    assert not any("assumed_formation has no graded value" in p.note for p in pills)


def test_f4_card_health_carries_no_assumed_formation_pill_and_the_dot_stays_on_the_card():
    from datetime import datetime, timezone

    from cobalt.cards.health import EntrySnapshot, card_health
    from cobalt.radar.evaluate import assumed_keys_of

    dots = [_graded("factor_a", 0, 7), _assumed_dot(1)]
    snap = EntrySnapshot(captured_at=datetime(2026, 1, 6, 15, tzinfo=timezone.utc), rvol=None, spread=None,
                         dot_grades={"factor_a": 7})
    pills = card_health(snapshot=snap, current_rvol=None, current_spread=None, dots=dots, stop=Decimal("9.50"),
                        direction="long", intrabar=[], closed=[], ema9=None, t=_thresholds())
    assert [p.label for p in pills if p.klass == "dot"] == ["factor_a"]
    assert assumed_keys_of(dots) == ("a.key",)  # the dot itself is untouched; the card's ASSUMED mark carries it


# =====================================================================
# F5 — R51: `stop.buffer`'s unit label `cents` → `dollars` (the value is
# unchanged; the engine already applies it as a price delta)
# =====================================================================


def test_f5_stop_buffer_is_labelled_dollars_with_the_committed_value():
    import yaml

    from cobalt.taxonomy.loader import TUNABLES_PATH, load_tunables
    from cobalt.taxonomy.tunables import TunableUnit

    committed = next(r for r in yaml.safe_load(TUNABLES_PATH.read_text())["tunables"] if r["key"] == "stop.buffer")
    row = load_tunables().by_key["stop.buffer"]
    assert row.unit == TunableUnit.DOLLARS
    assert row.value == committed["value"]  # read from the file, never typed (L69)


# =====================================================================
# F6 — R61: the dials per setup, and one per-trade override proven to
# reach the evaluator (no source change)
# =====================================================================


def _per_trade_accepted(root, slug, mapping, own_rows, key, unit) -> bool:
    """Is a `tunables:<slug>` row for `key` accepted by the loader for this def?"""
    import yaml

    from cobalt.taxonomy.slug import per_trade_scope
    from cobalt.taxonomy.vault_loader import STRATEGIES_DIR, VaultTaxonomyError, load_vault_trade_defs

    if key in {r["key"] for r in own_rows}:
        return True  # the note already carries it (its own `cfg(<trade key>.…)` dial)
    row = {"key": key, "value": 1, "unit": unit, "scope": per_trade_scope(slug), "dynamic": True,
           "status": "proposed", "source": "ruling", "consumers": ["a probe"]}
    directory = root / STRATEGIES_DIR
    directory.mkdir(parents=True, exist_ok=True)
    body = yaml.safe_dump({"trade_def": mapping}, sort_keys=False).rstrip("\n")
    unit_text = shapes.TUNABLES_UNIT.format(
        slug=slug, body=yaml.safe_dump({"tunables": [*own_rows, row]}, sort_keys=False).rstrip("\n"))
    (directory / f"{slug}.md").write_text(shapes.NOTE.format(slug=slug, name="Probe", body=body, tunables=unit_text))
    try:
        load_vault_trade_defs(vault_root=root)
    except VaultTaxonomyError:
        return False
    return True


def test_f6_a_the_dials_of_every_setup_and_where_each_is_tuned(tmp_path_factory):
    """GREEN-as-pin, a report generator: per setup of the corpus (+ the eighth),
    every key its formation reads (the declared closure + the note's own rows),
    and whether a `tunables:<slug>` row reaches it. KEYS ONLY — no value."""
    import test_setups_lego as lego
    from cobalt.radar.evaluate import closure_keys

    corpus = {key: (shape.note_slug, shape.mapping, shape.rows, shape.engine) for key, shape in shapes.SHAPES.items()}
    corpus["example-lego-eighth"] = ("example-lego-eighth", lego.eighth_mapping, lambda: [], shapes.D2_CONSTRUCTED)
    engine = sup.engine_tunables()
    table = []
    for setup, (slug, mapping, rows, fills) in corpus.items():
        ld = shapes.load_note(tmp_path_factory.mktemp(f"dials-{setup}"), slug, mapping(), rows=rows(),
                              engine=fills)
        keys = sorted(closure_keys(ld.definition) | set(shapes.user_rows(ld)))
        for key in keys:
            unit = engine[key].unit.value if key in engine else shapes.user_rows(ld)[key].unit.value
            reached = _per_trade_accepted(tmp_path_factory.mktemp(f"probe-{setup}"), slug, mapping(), rows(), key,
                                          unit)
            where = "per_trade" if reached else (
                f"assumed / engine only ({engine[key].scope})" if key in engine else "UNPROVEN")
            table.append((setup, key, where))
    print("DIALS setup | key | reachable")
    for setup, key, where in table:
        print(f"DIALS {setup} | {key} | {where}")
    assert not [row for row in table if row[2] == "UNPROVEN"], [row for row in table if row[2] == "UNPROVEN"]
    # a per-trade dial exists only where the note's own text names `cfg(<trade key>.…)`
    assert {(s, k) for s, k, w in table if w == "per_trade"} == {
        ("hitchhiker", "example_drive_then_range.range_duration_band")}


#: This file's own literals (L69): the reversal shape's per-trade trigger dial,
#: the value the neutral shape writes as a literal, and an override of it.
TUNED_SLUG, TUNED_KEY = "example-tuned-reversal", "example_tuned_reversal.bars_cleared"
WIDE_SLUG, WIDE_KEY = "example-tuned-reversal-wide", "example_tuned_reversal_wide.bars_cleared"
AS_WRITTEN, OVERRIDE = 2, 5


def _tuned(root, slug, key, value):
    mapping = shapes.rubberband_mapping(shapes.MIXED, htf_avoid=False)
    mapping["trigger"]["params"]["bars_cleared"] = f"cfg({key})"
    row = {"key": key, "value": value, "unit": "bars", "scope": f"per_trade({key.split('.')[0]})",
           "dynamic": True, "status": "proposed", "source": "ruling", "consumers": ["trigger: bars_cleared"]}
    return shapes.load_note(root, slug, mapping, rows=[row])


def _formed(ld):
    out = []
    for m in range(0, 391, 2):
        at = shapes.DAY_START + timedelta(minutes=m)
        ev = shapes.evaluate(ld, "FTFT", at)
        if ev.evaluation == "formed":
            f = ev.formation
            out.append((at.isoformat(), f.trade_direction, str(f.trigger.price), f.trigger.bars_cleared))
    return out


def test_f6_b_a_per_trade_override_in_the_notes_unit_reaches_the_evaluator(tmp_path_factory):
    """GREEN-as-pin (a PROOF of the tuning path R61 relies on): the reversal
    shape with its trigger's `bars_cleared` as a per-trade dial — at the value
    the neutral shape writes, the formations equal the literal note's; overridden
    in the note's `tunables:<slug>` unit, they change."""
    literal = _formed(shapes.load_shape_fresh("rubberband-without-htf-avoid"))
    as_written = _formed(_tuned(tmp_path_factory.mktemp("tuned"), TUNED_SLUG, TUNED_KEY, AS_WRITTEN))
    overridden = _formed(_tuned(tmp_path_factory.mktemp("wide"), WIDE_SLUG, WIDE_KEY, OVERRIDE))
    print(f"F6 (b) literal note: formed_scans={len(literal)} first={literal[:1]}")
    print(f"F6 (b) per-trade dial at {AS_WRITTEN}: formed_scans={len(as_written)} first={as_written[:1]}")
    print(f"F6 (b) per-trade dial overridden to {OVERRIDE}: formed_scans={len(overridden)} first={overridden[:1]}")
    assert literal and as_written == literal
    assert overridden != literal
