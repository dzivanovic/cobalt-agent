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
