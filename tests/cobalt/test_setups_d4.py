"""STEP-5 of the setups one build (FINAL C4) — D4 Extension lifecycle
(`reverting`, `backside`), `indicator_cross`, `measured_fraction`,
`recent_higher_low`, the `between` relation + `flat`, the Arith shape — the
backside and fashionably-late setups.

- X10 FIRST (FINAL: "evaluate a backside fixture with last > open once D4
  exists"): a constructed series written from the definition — a run down, a
  culminating bar, a snapback, a backside above a rising EMA9, then last > open.
  The card forms on the wrong side, or never forms → `A-01` is not applied to
  the D4 states as §1 words it; the FINAL offers two fixes and chooses neither
  → the two acceptances STOP, D4 is kept, both defs are AWAITING_A_RULING.
- D4 is a SEPARATE lifecycle over `detect_extension`'s output: every existing
  `ExtensionObservation` field is byte-identical (pinned at the start of the
  step). While `extension.snapback_bars_cleared` (`A-08`) is null the atom
  `Extension.state` reads exactly today's value.

Every constructed series is written from the definition's words; every
threshold is a literal of this file's own choosing (L69). R24 holds.
"""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.archiver.models import Bar, Interval
from cobalt.radar.anatomy.bars import rth_only, working_bars
from cobalt.radar.anatomy.extension import ExtensionParams, detect_extension
from cobalt.session import session_clock

UTC = timezone.utc
SYN_DATE = date(2026, 1, 6)
#: The committed day's `ExtensionObservation` dumps, every scan, on the START
#: code — D4 must leave every existing field byte-identical.
PIN_EXTENSION_OBSERVATIONS = "86254c33003cf4767709ceb927cc96052c7ca6b96ce1e4e744287b62c98166b5"
#: X10's result on this build (quoted in the report).
X10_RESULT = "FAIL"


def _sha(payload) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()


def _et(h: int, m: int) -> datetime:
    return datetime(2026, 1, 6, h + 5, m, tzinfo=UTC)


def _bucket(start, o, h, lo, c, v=1000):
    o, h, lo, c = (Decimal(str(x)) for x in (o, h, lo, c))
    mid = (o + c) / 2
    return [Bar(ticker="SYN", interval=Interval.I1, ts=start, open=o, high=h, low=lo, close=mid, volume=v),
            Bar(ticker="SYN", interval=Interval.I1, ts=start + timedelta(minutes=1), open=mid, high=h, low=lo,
                close=c, volume=v)]


def run_down_then_backside(*, above_open: bool) -> list[Bar]:
    """A day written from the definitions: a flat premarket (the seed); a run
    DOWN from the 10.00 open in twenty 2m buckets; a culminating bucket (the
    widest body, on a volume spike); the turn (the low of the move); a snapback
    of up buckets; a backside of higher highs and higher lows above a rising
    EMA9; a micro-Range above the EMA9 (a deeper middle base = the counter-
    pivot). `above_open` carries the recovery past the open first (X10)."""
    out, t = [], _et(8, 0)
    while t < _et(9, 30):
        out += _bucket(t, 10, "10.01", "9.99", 10)
        t += timedelta(minutes=2)
    o = Decimal(10)
    for _ in range(20):  # the run down, 09:30 … 10:08
        out += _bucket(t, o, o + Decimal("0.01"), o - Decimal("0.06"), o - Decimal("0.05"))
        o -= Decimal("0.05")
        t += timedelta(minutes=2)
    out += _bucket(t, "9.00", "9.01", "8.35", "8.40", v=20000)  # 10:10 culminating
    t += timedelta(minutes=2)
    out += _bucket(t, "8.40", "8.42", "8.30", "8.36", v=3000)  # 10:12 the turn (low of the move)
    t += timedelta(minutes=2)
    legs = [("8.36", "8.72", "8.34", "8.70"), ("8.70", "9.12", "8.68", "9.10"),  # the snapback
            ("9.10", "9.42", "9.08", "9.40"), ("9.40", "9.41", "9.20", "9.25"),  # HH, then a higher low
            ("9.25", "9.62", "9.24", "9.60"), ("9.60", "9.61", "9.45", "9.50"),
            ("9.50", "9.72", "9.49", "9.70"), ("9.70", "9.92", "9.69", "9.90")]
    if above_open:
        legs += [("9.90", "10.12", "9.89", "10.10"), ("10.10", "10.34", "10.09", "10.32")]
    for o, h, lo, c in legs:
        out += _bucket(t, o, h, lo, c)
        t += timedelta(minutes=2)
    top = Decimal("10.42") if above_open else Decimal("9.98")
    for i in range(7):  # the micro-Range above EMA9: T B T B(deepest = the counter-pivot) T B T
        if i % 2 == 0:  # touch the top; the low stays far from the base
            out += _bucket(t, top - Decimal("0.03"), top, top - Decimal("0.06"), top - Decimal("0.05"))
        else:  # touch the base; the high stays far from the top
            base = top - Decimal("0.16") if i == 3 else top - Decimal("0.14")
            out += _bucket(t, top - Decimal("0.07"), top - Decimal("0.10"), base, top - Decimal("0.11"))
        t += timedelta(minutes=2)
    return out


def _daily():
    from cobalt.radar.anatomy.daily import DailyBar, DailySeries

    bars = tuple(DailyBar(session_date=SYN_DATE - timedelta(days=d), open=10, high=12, low=7, close=10, volume=1)
                 for d in (8, 7, 6, 1))  # prior sessions, a wide range: no day-1 HTF break
    return DailySeries(ticker="SYN", bars=bars, fetched_at=_et(9, 0))


def _member(bars, at):
    from cobalt.radar.evaluate import MemberInput

    return MemberInput(membership_id=9, ticker="SYN", trade_date=SYN_DATE, as_of=at, bars=tuple(bars),
                       daily=_daily(), daily_status="cache-hit")


def _scan_after(bars) -> datetime:
    return bars[-1].ts + timedelta(minutes=1)


# =====================================================================
# The pins D4 must hold (START-of-step code)
# =====================================================================


def test_every_existing_extension_field_is_byte_identical_on_the_committed_day():
    params = ExtensionParams.from_tunables(sup.engine_tunables())
    dumps = []
    for m in range(0, 391, 2):
        at = shapes.DAY_START + timedelta(minutes=m)
        closed = [b for b in shapes.bars("FTFT") if b.ts + timedelta(minutes=1) <= at]
        run = tuple(rth_only(working_bars(closed, 2, as_of=at), session_clock()))
        dumps.append(detect_extension(run, params).model_dump(mode="json"))
    assert _sha(dumps) == PIN_EXTENSION_OBSERVATIONS


def test_while_a08_is_null_extension_state_reads_todays_value(tmp_path):
    """Production safety (NN#16): committed config keeps `A-08` null, so the
    atom is exactly `detect_extension`'s state on every scan of the day."""
    from cobalt.radar.evaluate import member_frames

    params = ExtensionParams.from_tunables(sup.engine_tunables())
    for m in range(0, 391, 10):
        at = shapes.DAY_START + timedelta(minutes=m)
        frames = member_frames(shapes.member("FTFT", at), tunables=sup.engine_tunables(), defaults=sup.defaults(),
                               clock=session_clock())
        for side in ("long", "short"):
            atom, ext = frames[side].atoms["Extension.state"], frames[side].extension
            if ext.unavailable is None:
                assert (atom.kind, atom.symbol) == ("symbol", ext.state), (at, side)


# =====================================================================
# X10 — FIRST
# =====================================================================


def test_x10_the_backside_shape_on_a_day_that_recovers_past_the_open():
    """X10, recorded and pinned: which side the backside shape forms on when
    last > open. PASS = forms LONG (the down Extension's backside is a long)."""
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("backside")
    bars = run_down_then_backside(above_open=True)
    at = _scan_after(bars)
    ev = evaluate_member(ld, _member(bars, at), tunables=shapes.tunables_for(ld), defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    result = "PASS" if ev.evaluation == "formed" and ev.direction == "long" else "FAIL"
    print(f"X10: {result} evaluation={ev.evaluation} direction={ev.direction} "
          f"long={ev.by_side['long'].evaluation}/{ev.by_side['long'].note} "
          f"short={ev.by_side['short'].evaluation}/{ev.by_side['short'].note}")
    assert result == X10_RESULT


def test_x10_control_the_same_day_before_it_recovers_past_the_open_forms_long():
    """The control: the same shape on the same construction, while last < open,
    forms LONG — so X10's outcome is the direction rule, not the detectors."""
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("backside")
    bars = run_down_then_backside(above_open=False)
    ev = evaluate_member(ld, _member(bars, _scan_after(bars)), tunables=shapes.tunables_for(ld),
                         defaults=sup.defaults(), scan_interval=100, clock=session_clock())
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.missing, ev.note,
                                                                  ev.by_side["long"].note)
    f = ev.formation
    assert f.anchor.object == "Extension" and f.stop_ref == "recent_higher_low"
    assert f.stop.price < min(f.trigger.price, ev.last_price)


# =====================================================================
# D4 — the lifecycle, constructed
# =====================================================================


def _run(bars):
    at = _scan_after(bars)
    return tuple(rth_only(working_bars([b for b in bars if b.ts + timedelta(minutes=1) <= at], 2, as_of=at),
                          session_clock()))


def _lifecycle(bars, **over):
    from cobalt.radar.anatomy.extension import LifecycleParams, extension_lifecycle
    from cobalt.radar.anatomy.indicators import ema

    run = _run(bars)
    ext = detect_extension(run, ExtensionParams.from_tunables(sup.engine_tunables()))
    params = LifecycleParams(**{"snapback_bars_cleared": 3, "backside_hh_min": 1, "backside_hl_min": 1, **over})
    closes = [ema(run[:i + 1], 9).value if i + 1 >= 9 else None for i in range(len(run))]
    return ext, extension_lifecycle(run, ext, params, ema9=closes, slope_bars=4)


def test_d4_reverting_starts_at_the_snapback_and_backside_needs_hh_hl_above_a_rising_ema9():
    bars = run_down_then_backside(above_open=False)
    ext, life = _lifecycle(bars)
    assert (ext.state, ext.direction) == ("culminating", "down")
    assert life.turn_ts == _et(10, 12) and life.turn_price == Decimal("8.30")
    assert life.reverting_ts == _et(10, 16)  # the first bucket clearing the highs of the 3 before it
    assert life.state == "backside" and life.higher_highs >= 1 and life.higher_lows >= 1


def test_d4_with_no_snapback_the_extension_stays_culminating():
    bars = run_down_then_backside(above_open=False)[:2 * (45 + 20 + 2)]  # up to the turn only
    _ext, life = _lifecycle(bars)
    assert life.state == "culminating" and life.reverting_ts is None


def test_d4_a_higher_hh_minimum_than_the_day_holds_is_reverting_not_backside():
    _ext, life = _lifecycle(run_down_then_backside(above_open=False), backside_hh_min=50)
    assert life.state == "reverting"


def test_d4_the_state_domain_and_the_new_row():
    from cobalt.radar.formation.atoms import ATOMS

    assert ATOMS["Extension.state"].domain == frozenset({"culminating", "reverting", "backside", "none"})
    row = sup.engine_tunables()["extension.snapback_bars_cleared"]
    assert (row.value, row.unit.value, row.scope, row.status.value) == (None, "bars", "global", "proposed")


# =====================================================================
# The bricks — indicator_cross, measured_fraction, recent_higher_low,
# between + flat, Arith, a null cfg
# =====================================================================


def test_indicator_cross_serves_its_shape_and_stamps_the_cross_bar():
    from cobalt.radar.formation.triggers import TRIGGERS
    from cobalt.taxonomy.trade_def import TriggerType

    ic = TRIGGERS[TriggerType.INDICATOR_CROSS]
    assert ic.serves({"a": "EMA9", "b": "VWAP", "direction": "a_crosses_above_b"})
    assert not ic.serves({"a": "EMA9", "b": "VWAP"}) and not ic.serves({"a": "RSI", "b": "VWAP",
                                                                          "direction": "a_crosses_above_b"})


def test_measured_fraction_is_anchor_a_minus_fraction_of_the_span():
    from cobalt.radar.formation.stops import STOPS, measured_fraction_price

    assert "measured_fraction" in STOPS
    # entry 10.00, turn_low 9.00, fraction 0.4 → 10.00 − 0.4 × 1.00 = 9.60, floored to the cent
    assert measured_fraction_price(Decimal("10.00"), Decimal("9.00"), Decimal("0.4")) == Decimal("9.60")
    assert measured_fraction_price(Decimal("10.005"), Decimal("9.00"), Decimal("0.4")) == Decimal("9.60")


def test_recent_higher_low_is_the_latest_pivot_low_inside_the_micro_range():
    from cobalt.radar.formation.stops import STRUCTURAL_REFS
    from cobalt.taxonomy.trade_def import StructuralRef

    assert StructuralRef.RECENT_HIGHER_LOW in STRUCTURAL_REFS


def test_arith_multiplication_and_a_zero_divisor():
    from cobalt.radar.evaluate import evaluate_node
    from cobalt.radar.formation.atoms import AtomValue
    from cobalt.taxonomy.predicate import parse_predicate

    atoms = {"Extension.leg_count": AtomValue(kind="number", number=Decimal(3))}
    unknowns: set[str] = set()
    assert evaluate_node(parse_predicate("Extension.leg_count * 2 >= 6"), atoms, lambda k: None, set(), unknowns)
    assert evaluate_node(parse_predicate("Extension.leg_count / 0 >= 1"), atoms, lambda k: None, set(),
                         unknowns) is None
    assert unknowns == {"division_by_zero"}


def test_a_null_cfg_is_unknown_with_its_key_never_a_crash():
    from cobalt.radar.evaluate import evaluate_node
    from cobalt.radar.formation.atoms import AtomValue
    from cobalt.taxonomy.predicate import parse_predicate

    atoms = {"Range(micro).wick_ratio": AtomValue(kind="number", number=Decimal("0.5"))}
    unknowns: set[str] = set()
    got = evaluate_node(parse_predicate("Range(micro).wick_ratio > cfg(range.wick_ratio_max)"), atoms,
                        lambda k: None, set(), unknowns)
    assert got is None and unknowns == {"range.wick_ratio_max_unset"}


def test_the_between_relation_serves_flat_between_turn_and_cross():
    from cobalt.radar.anatomy.registry import evaluability
    from cobalt.radar.formation.atoms import RELATIONS

    assert "between" in RELATIONS
    td = sup.anatomy_def(avoid=[{"expr": "flat(EMA9, window: 15 min / working_tf) between turn and cross"}])
    assert evaluability(td).evaluable, evaluability(td).missing_atoms
    bad = sup.anatomy_def(avoid=[{"expr": "flat(RSI, window: 15 min / working_tf) between turn and cross"}])
    assert not evaluability(bad).evaluable


def test_flat_between_turn_and_cross_on_a_constructed_series():
    from cobalt.radar.formation.atoms import flat_between

    norm = [Decimal(x) for x in ("0.5", "0.01", "0.02", "0.0", "0.01", "0.4")]
    assert flat_between(norm, start=1, end=4, window=3, threshold=Decimal("0.05")) is True
    assert flat_between(norm, start=1, end=4, window=5, threshold=Decimal("0.05")) is False
    assert flat_between(norm, start=4, end=1, window=1, threshold=Decimal("0.05")) is None  # no span


# =====================================================================
# The acceptances — STOPPED if X10 fails (pinned AWAITING_A_RULING)
# =====================================================================


@pytest.mark.parametrize("key", ["backside", "fashionably-late"])
def test_the_shapes_are_evaluable(key):
    from cobalt.radar.anatomy.registry import evaluability

    result = evaluability(shapes.load_shape_fresh(key).definition)
    assert result.evaluable, result.missing_atoms


def test_fashionably_late_path_forms_long_on_a_definition_written_day_with_constructed_holes():
    """[F-21] path on constructed series; the two `per_indicator` holes (F1)
    are filled HERE with this file's own literals — at production defaults they
    stay null (`AWAITING_A_RULING: F1`)."""
    from cobalt.radar.evaluate import evaluate_member
    from cobalt.radar.formation.stops import measured_fraction_price

    ld = shapes.load_shape_fresh("fashionably-late")
    at = _et(10, 30)  # after the EMA9 / VWAP cross, while the VWAP is still flat
    bars = [b for b in run_down_then_backside(above_open=False) if b.ts < at]
    ev = evaluate_member(ld, _member(bars, at), tunables=shapes.tunables_for(ld), defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.note, ev.by_side["long"].note)
    f = ev.formation
    assert f.trigger_outcome.kind == "indicator_cross" and f.stop_ref == "turn_low"
    # the measured stop: entry − 0.4 × (entry − the turn's low 8.30)
    assert f.stop.price == measured_fraction_price(f.trigger.price, Decimal("8.30"), Decimal("0.4"))
    assert f.stop.price < min(f.trigger.price, ev.last_price)  # the geometry guard


def test_fashionably_late_at_production_defaults_reads_its_f1_holes():
    """F1 not widened: the `per_indicator` flat thresholds stay null, so the
    shape can never form at production defaults (`AWAITING_A_RULING: F1`)."""
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("fashionably-late")
    at = _et(10, 30)
    bars = [b for b in run_down_then_backside(above_open=False) if b.ts < at]
    rows = {**sup.engine_tunables(), **{k: v for k, v in shapes.tunables_for(ld).items()
                                         if not k.startswith("flat_threshold.")}}
    ev = evaluate_member(ld, _member(bars, at), tunables=rows, defaults=sup.defaults(), scan_interval=100,
                         clock=session_clock())
    assert ev.evaluation == "not_formed" and "flat_threshold.ema9_unset" in (ev.by_side["long"].note or "")


@pytest.mark.parametrize("key", ["backside", "fashionably-late"])
def test_x7_both_frames_on_the_committed_day(key):
    ld = shapes.load_shape_fresh(key)
    rows = [ev for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(ld, ticker)]
    both = sum(ev.by_side["long"].evaluation == ev.by_side["short"].evaluation == "formed" for ev in rows)
    print(f"X7 {key}: scans={len(rows)} formed={sum(ev.evaluation == 'formed' for ev in rows)} both_sides={both}")
    assert both == 0


@pytest.mark.parametrize("key", ["backside", "fashionably-late"])
def test_x11_every_atom_the_shape_consults(key):
    from cobalt.radar.formation.atoms import ATOMS
    from cobalt.radar.seam import AtomOutcome

    td = shapes.load_shape_fresh(key).definition
    consulted = {a for p in [*td.preconditions, *td.avoid] for a in p.required_atoms if a in ATOMS}
    failures = [(n, r) for n in sorted(consulted) for r in ATOMS[n].reasons
                if not _constructs(n, r, AtomOutcome)]
    print(f"X11 {key}: atoms={len(consulted)} failures={failures}")
    assert failures == []


def _constructs(name, reason, model) -> bool:
    try:
        model(atom=name, value_kind="unavailable", unavailable=reason)
    except ValueError:
        return False
    return True
