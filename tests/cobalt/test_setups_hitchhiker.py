"""STEP-4 of the setups one build (FINAL C3b) — D2 Range(micro) + pivots, D3
opening-drive roles, `range_break`, `consolidation_low` — unlocks the
drive-then-range setup (hitchhiker).

- D2 (FINAL §3): `Range(micro).{instantiated, duration, low, top, base, bound,
  height, wick_ratio}`, `bound_type` (diverging = no Range), pivots
  `cfg(pivot.n)`; keys `A-02` (`range.wick_ratio_max`, the def's), `A-03`
  (`range.micro.touch_tolerance_atr`), `A-04` (`range.micro.bound_flat_slope_atr`).
- D3: leg ROLES are a separate function over `leg.legs()`'s output plus the
  Range(micro) observation; `leg.py` is byte-identical (X16).
  `Leg(opening_drive).terminated_by` carries the `A-07` rule in Gemini's
  wording [F-12]: "When a micro-Range instantiates from the drive's extreme
  within a bounded retrace, the termination is consolidation."
- §2.2 `range_break {ref: Range(micro).bound | .top}` (intrabar, the trade-side
  bound); §2.3 `consolidation_low` (= `Range.base`); §4 row 1 `IN cfg(band) min`.
- THE PER-SETUP ACCEPTANCE for the drive-then-range shape.

Every constructed series below is written FROM THE DEFINITION's words (a drive
from the open, then a sideways micro-Range at the drive's extreme in the day's
upper third); every threshold is a literal of this file's own choosing (L69).
R24: no expected value comes from a day the trader traded or tagged.
"""

from __future__ import annotations

import hashlib
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.archiver.models import Bar, Interval
from cobalt.radar.anatomy.bars import WorkingBar
from cobalt.session import session_clock
from cobalt.taxonomy.tunables import TunableRow

UTC = timezone.utc
SYN_DATE = date(2026, 1, 6)
LEG_PY = Path(__file__).resolve().parents[2] / "src" / "cobalt" / "radar" / "anatomy" / "leg.py"
#: X16 — `leg.py`'s bytes on the START-of-step code.
PIN_LEG_PY_SHA256 = "2f3b3abc2b9e9b634d4a5d050c352ade8853f5a9221be7cee5f4df43cb7782c8"
STEP4_KEYS = ("leg.consolidation_max_retrace", "range.micro.bound_flat_slope_atr", "range.micro.touch_tolerance_atr")


def _row(key: str, value, *, unit: str, scope: str = "global") -> TunableRow:
    return TunableRow(key=key, value=value, unit=unit, scope=scope, dynamic=True, status="proposed",
                      source="dwv", consumers=["test"])


def _et(h: int, m: int) -> datetime:
    """An ET wall-clock minute on the constructed day, as UTC (EST = UTC-5)."""
    return datetime(2026, 1, 6, h + 5, m, tzinfo=UTC)


def _bucket(start: datetime, o, h, lo, c, v=1000) -> list[Bar]:
    """One 2m working bucket as two i1 bars whose aggregate is (o, h, lo, c)."""
    o, h, lo, c = (Decimal(str(x)) for x in (o, h, lo, c))
    mid = (o + c) / 2
    return [
        Bar(ticker="SYN", interval=Interval.I1, ts=start, open=o, high=h, low=lo, close=mid, volume=v),
        Bar(ticker="SYN", interval=Interval.I1, ts=start + timedelta(minutes=1), open=mid, high=h, low=lo,
            close=c, volume=v),
    ]


def drive_then_range(*, pullback: bool = False) -> list[Bar]:
    """A day written from the definition: a flat premarket (the seed); an
    opening drive UP from 10.00 to 11.00 in five 2m buckets; then — optionally
    one opposing pullback bucket first — a sideways micro-Range 10.85–11.00
    that touches each bound five times, alternating, 09:40–09:58 ET."""
    out: list[Bar] = []
    t = _et(8, 0)
    while t < _et(9, 30):
        out += _bucket(t, 10, "10.01", "9.99", 10)
        t += timedelta(minutes=2)
    o = Decimal(10)
    for _ in range(5):  # 09:30 … 09:38: up, high = close (the drive's extreme is 11.00)
        out += _bucket(t, o, o + Decimal("0.2"), o - Decimal("0.01"), o + Decimal("0.2"))
        o += Decimal("0.2")
        t += timedelta(minutes=2)
    if pullback:  # one opposing bucket that ends the drive BEFORE the range (its low is outside the base)
        out += _bucket(t, "11.00", "11.00", "10.80", "10.82")
        t += timedelta(minutes=2)
    for i in range(10):
        if i % 2 == 0:  # touch the top
            out += _bucket(t, "10.95", "11.00", "10.92", "10.93")
        else:  # touch the base
            out += _bucket(t, "10.93", "10.96", "10.85", "10.90")
        t += timedelta(minutes=2)
    return out


def _syn_member(bars, at: datetime, *, departed: bool = False):
    from cobalt.radar.evaluate import MemberInput

    return MemberInput(membership_id=7, ticker="SYN", trade_date=SYN_DATE, as_of=at, bars=tuple(bars),
                       daily=None, daily_status="absent", departed=departed)


def constructed_tunables(**over) -> dict[str, TunableRow]:
    """Committed engine rows with this build's constructed values in the step's
    null holes (`setups_shapes.D2_CONSTRUCTED`, L69)."""
    rows = dict(sup.engine_tunables())
    for key, (unit, value) in {**shapes.D2_CONSTRUCTED, **over}.items():
        rows[key] = rows[key].model_copy(update={"value": None if value is None else Decimal(value)}) \
            if key in rows else _row(key, None if value is None else Decimal(value), unit=unit)
    return rows


SYN_SCAN = _et(10, 0)


# =====================================================================
# X16 — leg.py byte-identical; roles are a separate function
# =====================================================================


def test_x16_leg_py_is_byte_identical():
    digest = hashlib.sha256(LEG_PY.read_bytes()).hexdigest()
    print(f"X16: leg.py sha256={digest}")
    assert digest == PIN_LEG_PY_SHA256


# =====================================================================
# D2 — pivots and Range(micro), constructed series
# =====================================================================


def _working(bars, at=SYN_SCAN):
    from cobalt.radar.anatomy.bars import rth_only, working_bars

    return tuple(rth_only(working_bars(bars, 2, as_of=at), session_clock()))


def _wb(ts, o, h, lo, c, complete=True):
    return WorkingBar(ts=ts, minutes=2, open=Decimal(str(o)), high=Decimal(str(h)), low=Decimal(str(lo)),
                      close=Decimal(str(c)), volume=1000, complete=complete, minutes_present=2 if complete else 1)


def test_pivots_need_n_bars_each_side():
    from cobalt.radar.anatomy.pivots import TUNABLE_KEYS, pivots

    assert TUNABLE_KEYS == ("pivot.n",)
    t = _et(9, 30)
    highs = [1, 2, 5, 2, 1, 3, 1]
    bars = [_wb(t + timedelta(minutes=2 * i), h - 0.5, h, h - 1, h - 0.4) for i, h in enumerate(highs)]
    p = pivots(bars, 2)
    assert [x.price for x in p.highs] == [Decimal(5)]  # index 5 (3) has only one bar after it
    assert [x.price for x in p.lows] == []  # no low beats 2 bars each side strictly
    assert pivots(bars, 1).highs[-1].price == Decimal(3)


def _params(**over):
    from cobalt.radar.anatomy.micro_range import range_params

    params, reason = range_params(constructed_tunables(**over))
    return params, reason


def test_range_micro_instantiates_on_two_touches_per_side_at_the_drives_extreme():
    from cobalt.radar.anatomy.micro_range import detect_micro_range

    run = _working(drive_then_range())
    params, reason = _params()
    assert reason is None
    obs = detect_micro_range(run, params, atr=Decimal("0.05"))
    r = obs.range
    assert obs.unavailable is None and r.instantiated
    assert (r.top, r.base, r.bound_type) == (Decimal("11.00"), Decimal("10.85"), "flat")
    assert r.start_ts == _et(9, 40)  # the drive's last bucket (low 10.79) is outside the base tolerance
    assert r.instantiated_ts == _et(9, 46)  # T 09:40, B 09:42, T 09:44, B 09:46 → two touches each
    assert r.duration_min == Decimal(20)  # 09:40 → 10:00
    assert r.height == Decimal("0.15")
    # wick ratio: T buckets span 0.08 with body 0.02, B buckets 0.11 with body 0.03 (five of each)
    assert r.wick_ratio == (5 * Decimal("0.06") + 5 * Decimal("0.08")) / (5 * Decimal("0.08") + 5 * Decimal("0.11"))
    assert (r.touches_top, r.touches_base) == (5, 5)


def test_diverging_bounds_are_no_range():
    from cobalt.radar.anatomy.micro_range import detect_micro_range

    t = _et(9, 30)
    bars = []
    for i in range(8):  # a megaphone: alternate bars reach a higher top / a lower base
        step = Decimal("0.3") * (i // 2)
        high, low = (Decimal(11) + step, Decimal("10.5")) if i % 2 == 0 else (Decimal("10.5"), Decimal("9.9") - step)
        bars.append(_wb(t + timedelta(minutes=2 * i), "10.5", high, low, "10.5"))
    params, _ = _params()
    # tol = 0.3 × 1 → two touches per side (bars 4, 6 at the top; 5, 7 at the base);
    # slopes +0.15 / −0.15 per bar: apart by 0.3 > flat 0.2 × 1 → diverging → no Range
    assert detect_micro_range(bars, params, atr=Decimal(1)).range is None
    wide, _ = _params(**{"range.micro.bound_flat_slope_atr": ("atr", "0.5")})
    assert detect_micro_range(bars, wide, atr=Decimal(1)).range is not None  # it IS the divergence rule


def test_range_reads_its_unset_keys_the_seed_and_incomplete_buckets():
    from cobalt.radar.anatomy.micro_range import TUNABLE_KEYS, detect_micro_range

    assert TUNABLE_KEYS == ("range.micro.touches_per_side", "range.micro.touch_tolerance_atr",
                            "range.micro.bound_flat_slope_atr")
    params, reason = _params(**{"range.micro.touch_tolerance_atr": ("atr", None)})
    assert (params, reason) == (None, "range.micro.touch_tolerance_atr_unset")
    params, _ = _params()
    run = _working(drive_then_range())
    assert detect_micro_range(run, params, atr=None).unavailable == "insufficient_seed"
    broken = (*run[:-1], run[-1].model_copy(update={"complete": False, "minutes_present": 1}))
    assert detect_micro_range(broken, params, atr=Decimal("0.05")).unavailable == "incomplete_bucket"


# =====================================================================
# D3 — the opening drive's role and termination (A-07, [F-12])
# =====================================================================


def test_a07_a_range_from_the_drives_extreme_within_the_retrace_is_consolidation():
    from cobalt.radar.anatomy.leg import legs
    from cobalt.radar.anatomy.leg_roles import TUNABLE_KEYS, opening_drive
    from cobalt.radar.anatomy.micro_range import detect_micro_range

    assert TUNABLE_KEYS == ("leg.consolidation_max_retrace",)
    run = _working(drive_then_range())
    params, _ = _params()
    r = detect_micro_range(run, params, atr=Decimal("0.05")).range
    od = opening_drive(run, legs(run), r, max_retrace=Decimal("0.6"))
    assert (od.direction, od.terminated_by) == ("up", "consolidation")
    assert od.retrace == Decimal("0.15")  # (11.00 − 10.85) / (11.00 − 10.00)
    # a retrace bound tighter than the range's depth → the drive ended in a pullback
    assert opening_drive(run, legs(run), r, max_retrace=Decimal("0.1")).terminated_by == "pullback"


def test_the_literal_reading_calls_a_pullback_first_a_pullback():
    """X15's two readings on one constructed day: an opposing bucket ends the
    drive before the range starts. The literal reading ("terminated by the first
    pullback (≥1 opposing bar)") says pullback; A-07 says consolidation, because
    the range still instantiates from the drive's extreme within the retrace."""
    from cobalt.radar.anatomy.leg import legs
    from cobalt.radar.anatomy.leg_roles import opening_drive, opening_drive_literal
    from cobalt.radar.anatomy.micro_range import detect_micro_range

    run = _working(drive_then_range(pullback=True), at=SYN_SCAN + timedelta(minutes=2))
    params, _ = _params()
    r = detect_micro_range(run, params, atr=Decimal("0.05")).range
    assert r is not None and r.start_ts == _et(9, 42)
    assert opening_drive_literal(run, legs(run), r).terminated_by == "pullback"
    assert opening_drive(run, legs(run), r, max_retrace=Decimal("0.6")).terminated_by == "consolidation"


def test_a_drive_still_running_has_no_termination():
    from cobalt.radar.anatomy.leg import legs
    from cobalt.radar.anatomy.leg_roles import opening_drive

    run = _working(drive_then_range(), at=_et(9, 40))  # only the drive's buckets are closed
    od = opening_drive(run, legs(run), None, max_retrace=Decimal("0.6"))
    assert (od.direction, od.terminated_by) == ("up", None)


# =====================================================================
# The atoms, the trigger, the stop, the interpreter shape
# =====================================================================

D2_D3_ATOMS = {
    "Range(micro).instantiated", "Range(micro).duration", "Range(micro).low", "Range(micro).top",
    "Range(micro).base", "Range(micro).bound", "Range(micro).height", "Range(micro).wick_ratio",
    "Leg(opening_drive).direction", "Leg(opening_drive).terminated_by",
}


def test_the_d2_d3_atoms_are_served_with_domains_keys_and_units():
    from cobalt.radar.anatomy import leg_roles, micro_range
    from cobalt.radar.formation.atoms import ATOMS

    assert D2_D3_ATOMS <= set(ATOMS)
    assert ATOMS["Leg(opening_drive).terminated_by"].domain == frozenset({"pullback", "consolidation"})
    assert ATOMS["Leg(opening_drive).direction"].domain == frozenset({"up", "down"})
    assert ATOMS["Range(micro).duration"].unit == "min"
    for name in D2_D3_ATOMS - {"Leg(opening_drive).direction"}:
        assert set(micro_range.TUNABLE_KEYS) <= set(ATOMS[name].tunable_keys), name
    assert set(leg_roles.TUNABLE_KEYS) <= set(ATOMS["Leg(opening_drive).terminated_by"].tunable_keys)
    for name in ("Range(micro).low", "Range(micro).top", "Range(micro).base", "Range(micro).bound"):
        assert ATOMS[name].price, name
    assert not ATOMS["Range(micro).height"].price and not ATOMS["Range(micro).duration"].price


def test_the_new_rows_are_engine_rows_null_and_proposed():
    rows = sup.engine_tunables()
    for key, unit in (("range.micro.touch_tolerance_atr", "atr"), ("range.micro.bound_flat_slope_atr", "atr"),
                      ("leg.consolidation_max_retrace", "ratio")):
        row = rows[key]
        assert (row.value, row.unit.value, row.scope, row.status.value) == (None, unit, "global", "proposed"), key


def test_range_break_serves_the_bound_and_the_top_and_the_stop_serves_the_base():
    from cobalt.radar.formation.stops import STRUCTURAL_REFS
    from cobalt.radar.formation.triggers import TRIGGERS
    from cobalt.taxonomy.trade_def import StructuralRef, TriggerType

    rb = TRIGGERS[TriggerType.RANGE_BREAK]
    assert rb.serves({"ref": "Range(micro).bound"}) and rb.serves({"ref": "Range(micro).top"})
    assert not rb.serves({"ref": "Range(prior).top"}) and not rb.serves({})
    assert {StructuralRef.CONSOLIDATION_LOW, StructuralRef.RANGE_BASE} <= set(STRUCTURAL_REFS)


def _band_def(unit_of_row: str):
    td = sup.anatomy_def(preconditions=[{"expr": "Range(micro).duration IN cfg(example_band) min"}])
    rows = {**constructed_tunables(), "example_band": _row("example_band", [5, 30], unit=unit_of_row)}
    return td, rows


def test_the_in_band_quantity_shape_is_evaluable_and_a_unit_mismatch_is_named():
    from cobalt.radar.anatomy.registry import evaluability
    from cobalt.radar.evaluate import evaluate_member

    td, rows = _band_def("min")
    assert evaluability(td).evaluable
    ld = sup.loaded(td, md5="000000000000000000000000000004a1")
    ev = evaluate_member(ld, _syn_member(drive_then_range(), SYN_SCAN), tunables=rows, defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    assert "Range(micro).duration" in {a.atom for a in ev.detail.atoms}
    td, rows = _band_def("bars")
    ev = evaluate_member(sup.loaded(td, md5="000000000000000000000000000004a2"),
                         _syn_member(drive_then_range(), SYN_SCAN), tunables=rows, defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    assert ev.evaluation == "not_evaluable" and ev.missing == ("Unsupported(unit:min≠bars)",)


def test_a_duration_compared_to_a_band_without_a_unit_is_unsupported():
    from cobalt.radar.anatomy.registry import evaluability

    td = sup.anatomy_def(preconditions=[{"expr": "Range(micro).height IN cfg(example_band) min"}])
    assert not evaluability(td).evaluable  # a height has no minutes
    assert "Unsupported(unit:min)" in evaluability(td).missing_atoms


# =====================================================================
# THE PER-SETUP ACCEPTANCE — the drive-then-range shape
# =====================================================================


def test_hitchhiker_shape_is_evaluable():
    from cobalt.radar.anatomy.registry import evaluability

    ld = shapes.load_shape_fresh("hitchhiker")
    result = evaluability(ld.definition)
    assert result.evaluable, result.missing_atoms
    assert result.human_predicates == 1  # the text avoid stays human (L11)


def test_hitchhiker_path_forms_long_on_the_definition_written_day():
    """[F-21]: every precondition, the trigger and the stop resolve on a
    constructed series written from the definition's words."""
    from cobalt.radar.anatomy.structure import structural_stop
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("hitchhiker")
    ev = evaluate_member(ld, _syn_member(drive_then_range(), SYN_SCAN), tunables=shapes.tunables_for(ld),
                         defaults=sup.defaults(), scan_interval=100, clock=session_clock())
    assert ev.evaluation == "formed", (ev.evaluation, ev.missing, ev.note)
    f = ev.formation
    assert (ev.direction, f.trade_direction, f.side_frame) == ("long", "long", "long")
    assert f.formed_bar_ts == _et(9, 46)  # the bucket whose touch instantiated the range
    assert f.trigger.price == Decimal("11.00")  # the trade-side bound (the top, for a long)
    assert f.stop.price == structural_stop(Decimal("10.85"), "long", Decimal("0.02")).price  # the base − buffer
    assert f.anchor.object == "Range(micro)" and f.stop_ref == "consolidation_low"
    assert f.stop.price < min(f.trigger.price, ev.last_price)  # the geometry guard (§9 point (5))
    assert ev.by_side["short"].evaluation != "formed"
    assert ev.detail.extension_path is None  # not an Extension formation


def test_hitchhiker_path_a_departed_member_does_not_form():
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("hitchhiker")
    ev = evaluate_member(ld, _syn_member(drive_then_range(), SYN_SCAN, departed=True),
                         tunables=shapes.tunables_for(ld), defaults=sup.defaults(), scan_interval=100,
                         clock=session_clock())
    assert ev.evaluation == "not_formed"


def test_hitchhiker_path_the_mirrored_day_forms_short():
    """The same shape on the price-mirrored day forms on the SHORT frame
    (F-04): the drive runs down, the range sits in the day's lower third."""
    from cobalt.radar.evaluate import evaluate_member

    mirrored = [b.model_copy(update={"open": 20 - b.open, "high": 20 - b.low, "low": 20 - b.high,
                                     "close": 20 - b.close}) for b in drive_then_range()]
    ld = shapes.load_shape_fresh("hitchhiker")
    ev = evaluate_member(ld, _syn_member(mirrored, SYN_SCAN), tunables=shapes.tunables_for(ld),
                         defaults=sup.defaults(), scan_interval=100, clock=session_clock())
    assert ev.evaluation == "formed" and ev.direction == "short", (ev.evaluation, ev.note)
    assert ev.formation.trigger.price == Decimal("9.00")  # 20 − 11.00: the range base is the short's bound
    assert ev.formation.side_frame == "mirrored"


def test_hitchhiker_path_at_committed_defaults_the_nulls_keep_it_unknown():
    """The step's holes are null in committed config: no formation, and the
    reason is the key's `_unset`, never a guess."""
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("hitchhiker")
    rows = {**sup.engine_tunables(), **shapes.user_rows(ld)}
    ev = evaluate_member(ld, _syn_member(drive_then_range(), SYN_SCAN), tunables=rows, defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    assert ev.evaluation == "not_formed"
    assert "_unset" in (ev.note or "")


def test_x7_hitchhiker_both_frames_on_the_committed_day():
    ld = shapes.load_shape_fresh("hitchhiker")
    rows = [ev for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(ld, ticker)]
    both = sum(ev.by_side["long"].evaluation == ev.by_side["short"].evaluation == "formed" for ev in rows)
    formed = sum(ev.evaluation == "formed" for ev in rows)
    print(f"X7 hitchhiker: scans={len(rows)} formed={formed} both_sides={both}")
    assert both == 0


def test_the_geometry_guard_holds_for_every_hitchhiker_formation_of_the_committed_day():
    ld = shapes.load_shape_fresh("hitchhiker")
    for ticker in ("FTFT", "BGFI"):
        for _, ev in shapes.every_scan(ld, ticker):
            if ev.evaluation == "formed":
                f = ev.formation
                if f.trade_direction == "long":
                    assert f.stop.price < min(f.trigger.price, ev.last_price)
                else:
                    assert f.stop.price > max(f.trigger.price, ev.last_price)


def test_x11_every_atom_the_drive_then_range_shape_consults():
    from cobalt.radar.formation.atoms import ATOMS
    from cobalt.radar.seam import AtomOutcome

    ld = shapes.load_shape_fresh("hitchhiker")
    consulted = {a for p in [*ld.definition.preconditions, *ld.definition.avoid] for a in p.required_atoms}
    failures = []
    for name in sorted(consulted):
        for reason in ATOMS[name].reasons:
            try:
                AtomOutcome(atom=name, value_kind="unavailable", unavailable=reason)
            except ValueError:
                failures.append((name, reason))
    print(f"X11 hitchhiker: atoms={len(consulted)} failures={failures}")
    assert failures == []
