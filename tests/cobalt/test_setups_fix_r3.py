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
