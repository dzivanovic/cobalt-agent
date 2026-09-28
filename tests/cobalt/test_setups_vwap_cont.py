"""STEP-7 of the setups one build (FINAL C6) — D5 trendline + `dist`, the level
set and `rejected` — the pullback-to-VWAP continuation setup
(vwap-continuation).

- `Level_ref(trendline, anchor_leg)` through the anchor leg's pivots (≥
  `cfg(trendline.min_pivots)`); the flat case is the micro-Range far bound
  (`TAXONOMY-DRAFT-v0_7.md:114`) — `trendline_break`.
- `dist(a, b)` against `cfg(dist.k.vwap)` × ATR (`A-16`, a `per_indicator` hole,
  F1 — never widened: at production defaults the shape cannot form).
- The level set (`A-17`, `levels.set`) and `Level_ref(resistance).rejected`
  (`A-18`, `level.rejected.rule`). The note-versus-sheet divergence the
  companion reports for this avoid is REPORTED, never fixed — the NOTE is
  followed (L32 / L65).

Constructed series are written from the definition's words; thresholds are
this file's literals (L69). R24 holds.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.archiver.models import Bar, Interval
from cobalt.session import session_clock

UTC = timezone.utc
SYN_DATE = date(2026, 1, 6)


def _et(h: int, m: int) -> datetime:
    return datetime(2026, 1, 6, h + 5, m, tzinfo=UTC)


def _bucket(start, o, h, lo, c, v=1000):
    o, h, lo, c = (Decimal(str(x)) for x in (o, h, lo, c))
    mid = (o + c) / 2
    return [Bar(ticker="SYN", interval=Interval.I1, ts=start, open=o, high=h, low=lo, close=mid, volume=v),
            Bar(ticker="SYN", interval=Interval.I1, ts=start + timedelta(minutes=1), open=mid, high=h, low=lo,
                close=c, volume=v)]


def drive_pullback_to_vwap(*, reject_pmh: bool = False) -> list[Bar]:
    """A day written from the definition: a flat premarket (PMH 10.01); a
    strong drive UP from the 10.00 open; a pullback of down buckets toward the
    VWAP; the pullback consolidating into a flat micro-Range near the VWAP (the
    trendline's flat case). `reject_pmh` makes the drive's first bucket wick
    through the PMH and close back below it."""
    out, t = [], _et(8, 0)
    while t < _et(9, 30):
        out += _bucket(t, 10, "10.01", "9.99", 10)
        t += timedelta(minutes=2)
    o = Decimal(10)
    if reject_pmh:
        out += _bucket(t, "10.00", "10.04", "9.95", "9.97")  # wicks through the PMH, closes back below
        t += timedelta(minutes=2)
        o = Decimal("9.97")
    for _ in range(12):  # the drive
        out += _bucket(t, o, o + Decimal("0.10"), o - Decimal("0.02"), o + Decimal("0.10"))
        o += Decimal("0.10")
        t += timedelta(minutes=2)
    for c in ("11.00", "10.85", "10.72"):  # the pullback
        out += _bucket(t, o, o + Decimal("0.01"), Decimal(c) - Decimal("0.03"), c)
        o = Decimal(c)
        t += timedelta(minutes=2)
    top = Decimal("10.78")
    for i in range(7):  # the flat micro-Range near VWAP: T B T B(deepest) T B T
        if i % 2 == 0:
            out += _bucket(t, top - Decimal("0.03"), top, top - Decimal("0.06"), top - Decimal("0.05"))
        else:
            base = top - Decimal("0.16") if i == 3 else top - Decimal("0.14")
            out += _bucket(t, top - Decimal("0.07"), top - Decimal("0.10"), base, top - Decimal("0.11"))
        t += timedelta(minutes=2)
    return out


def _daily():
    from cobalt.radar.anatomy.daily import DailyBar, DailySeries

    bars = tuple(DailyBar(session_date=SYN_DATE - timedelta(days=d), open=10, high=12, low=7, close=10, volume=1)
                 for d in (8, 7, 6, 1))  # PDH 12: never reached
    return DailySeries(ticker="SYN", bars=bars, fetched_at=_et(9, 0))


def _member(bars, at):
    from cobalt.radar.evaluate import MemberInput

    return MemberInput(membership_id=13, ticker="SYN", trade_date=SYN_DATE, as_of=at, bars=tuple(bars),
                       daily=_daily(), daily_status="cache-hit")


def _scan_after(bars):
    return bars[-1].ts + timedelta(minutes=1)


# =====================================================================
# The bricks
# =====================================================================


def test_the_convention_rows_and_the_f1_hole():
    from cobalt.radar.evaluate import CONVENTION_LABELS

    rows = sup.engine_tunables()
    for key in ("levels.set", "level.rejected.rule"):
        row = rows[key]
        assert (row.value, row.unit.value, row.scope, row.status.value) == (None, "label", "global", "proposed"), key
        assert key in CONVENTION_LABELS
    assert rows["dist.k.vwap"].value is None and rows["dist.k.vwap"].scope.startswith("per_indicator")  # F1


def test_dist_is_the_absolute_distance_and_is_served():
    from cobalt.radar.anatomy.registry import evaluability
    from cobalt.radar.evaluate import evaluate_node
    from cobalt.radar.formation.atoms import AtomValue
    from cobalt.taxonomy.predicate import parse_predicate

    atoms = {"Leg(pullback).end": AtomValue(kind="number", number=Decimal("10.40")),
             "VWAP": AtomValue(kind="number", number=Decimal("10.50")),
             "ATR(working_tf)": AtomValue(kind="number", number=Decimal("0.2"))}
    node = parse_predicate("dist(Leg(pullback).end, VWAP) <= cfg(k) * ATR(working_tf)")
    assert evaluate_node(node, atoms, lambda k: Decimal("0.4"), set(), set()) is False  # 0.10 > 0.4 × 0.2
    assert evaluate_node(node, atoms, lambda k: Decimal("0.6"), set(), set()) is True  # 0.10 ≤ 0.12
    td = sup.anatomy_def(preconditions=[{"expr": "Extension.state == culminating"},
                                        {"expr": "dist(Leg(pullback).end, VWAP) <= cfg(dist.k.vwap) * ATR(working_tf)"}])
    assert evaluability(td).evaluable, evaluability(td).missing_atoms


def test_trendline_break_serves_its_shape():
    from cobalt.radar.formation.triggers import TRIGGERS
    from cobalt.taxonomy.trade_def import TriggerType

    tb = TRIGGERS[TriggerType.TRENDLINE_BREAK]
    assert tb.serves({"ref": "Level_ref(trendline)", "anchor_leg": "Leg(pullback)",
                      "pivots": "cfg(trendline.min_pivots)"})
    assert not tb.serves({"ref": "Level_ref(trendline)", "anchor_leg": "Leg(opening_drive)"})


def test_rejected_reads_the_level_set():
    from cobalt.radar.evaluate import member_frames

    ld = shapes.load_shape_fresh("vwap-continuation")
    for reject in (False, True):
        bars = drive_pullback_to_vwap(reject_pmh=reject)
        fr = member_frames(_member(bars, _scan_after(bars)), tunables=shapes.tunables_for(ld),
                           defaults=sup.defaults(), clock=session_clock())["long"]
        atom = fr.atoms["Level_ref(resistance).rejected"]
        # a rejection counts only while the last close is still below the level: the drive left
        # the PMH behind (and never reached the PDH), so both full days read False
        assert (atom.kind, atom.boolean) == ("boolean", False), (reject, atom)


def test_rejected_is_true_while_price_is_still_below_the_rejected_level():
    from cobalt.radar.evaluate import member_frames

    ld = shapes.load_shape_fresh("vwap-continuation")
    bars = drive_pullback_to_vwap(reject_pmh=True)[:2 * 46]  # the premarket + the rejection bucket only
    fr = member_frames(_member(bars, _scan_after(bars)), tunables=shapes.tunables_for(ld), defaults=sup.defaults(),
                       clock=session_clock())["long"]
    assert fr.atoms["Level_ref(resistance).rejected"].boolean is True


# =====================================================================
# THE PER-SETUP ACCEPTANCE — the pullback-to-VWAP continuation shape
# =====================================================================


def test_vwap_continuation_shape_is_evaluable():
    from cobalt.radar.anatomy.registry import evaluability

    result = evaluability(shapes.load_shape_fresh("vwap-continuation").definition)
    assert result.evaluable, result.missing_atoms
    assert result.human_predicates == 1  # the text avoid stays human (L11)


def test_vwap_continuation_path_forms_long_on_the_definition_written_day():
    """[F-21] with this file's constructed `dist.k.vwap` (the F1 hole)."""
    from cobalt.radar.anatomy.structure import structural_stop
    from cobalt.radar.evaluate import evaluate_member, member_frames

    ld = shapes.load_shape_fresh("vwap-continuation")
    bars = drive_pullback_to_vwap()
    at = _scan_after(bars)
    rows = shapes.tunables_for(ld)
    ev = evaluate_member(ld, _member(bars, at), tunables=rows, defaults=sup.defaults(), scan_interval=100,
                         clock=session_clock())
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.missing, ev.note,
                                                                  ev.by_side["long"].note)
    f = ev.formation
    assert f.trigger_outcome.kind == "trendline_break" and f.trigger.price == Decimal("10.78")  # the flat case: top
    fr = member_frames(_member(bars, at), tunables=rows, defaults=sup.defaults(), clock=session_clock())["long"]
    idx = [i for i, b in enumerate(fr.run) if b.ts == f.trigger_outcome.ref_bar_ts][-1]
    vwap_at_entry = fr.objects["series"]("VWAP")[idx]
    assert f.stop.price == structural_stop(vwap_at_entry, "long", Decimal("0.02")).price
    assert f.stop.price < min(f.trigger.price, ev.last_price)


# --- FINAL §9 point (1): the four values, from the DEFINITION on the stored bars ---
# (with this build's constructed `dist.k.vwap`, the F1 hole — L69)
# engine at STEP-7; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_VWAP_CONTINUATION_SIDE = "long"
# engine at STEP-7; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_VWAP_CONTINUATION_FORMED_BAR = "2026-01-06T20:04:00+00:00"
# engine at STEP-7; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_VWAP_CONTINUATION_TRIGGER = "24.8120"
# engine at STEP-7; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_VWAP_CONTINUATION_STOP = "24.75"


def test_vwap_continuation_forms_on_the_committed_day():
    ld = shapes.load_shape_fresh("vwap-continuation")
    formed = [(at, ev) for ticker in ("FTFT", "BGFI") for at, ev in shapes.every_scan(ld, ticker)
              if ev.evaluation == "formed"]
    assert formed
    _at, ev = formed[0]
    f = ev.formation
    got = (ev.direction, f.formed_bar_ts.isoformat(), str(f.trigger.price), str(f.stop.price))
    print(f"vwap-continuation on the committed day: formed_scans={len(formed)} ticker={ev.ticker} first={got}")
    assert got == (DEF_WRITTEN_VWAP_CONTINUATION_SIDE, DEF_WRITTEN_VWAP_CONTINUATION_FORMED_BAR,
                   DEF_WRITTEN_VWAP_CONTINUATION_TRIGGER, DEF_WRITTEN_VWAP_CONTINUATION_STOP)
    if f.trade_direction == "long":
        assert f.stop.price < min(f.trigger.price, ev.last_price)
    else:
        assert f.stop.price > max(f.trigger.price, ev.last_price)


def test_vwap_continuation_at_production_defaults_reads_its_f1_hole():
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("vwap-continuation")
    bars = drive_pullback_to_vwap()
    rows = {**sup.engine_tunables(), **{k: v for k, v in shapes.tunables_for(ld).items() if k != "dist.k.vwap"}}
    ev = evaluate_member(ld, _member(bars, _scan_after(bars)), tunables=rows, defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    assert ev.evaluation == "not_formed" and "dist.k.vwap_unset" in (ev.by_side["long"].note or "")


def test_x7_vwap_continuation_both_frames_on_the_committed_day():
    ld = shapes.load_shape_fresh("vwap-continuation")
    rows = [ev for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(ld, ticker)]
    both = sum(ev.by_side["long"].evaluation == ev.by_side["short"].evaluation == "formed" for ev in rows)
    print(f"X7 vwap-continuation: scans={len(rows)} formed={sum(ev.evaluation == 'formed' for ev in rows)} "
          f"both_sides={both}")
    assert both == 0


def test_x11_every_atom_the_vwap_continuation_shape_consults():
    from cobalt.radar.formation.atoms import ATOMS
    from cobalt.radar.seam import AtomOutcome

    td = shapes.load_shape_fresh("vwap-continuation").definition
    consulted = {a for p in [*td.preconditions, *td.avoid] for a in p.required_atoms if a in ATOMS}
    failures = []
    for name in sorted(consulted):
        for reason in ATOMS[name].reasons:
            try:
                AtomOutcome(atom=name, value_kind="unavailable", unavailable=reason)
            except ValueError:
                failures.append((name, reason))
    print(f"X11 vwap-continuation: atoms={len(consulted)} failures={failures}")
    assert failures == []
