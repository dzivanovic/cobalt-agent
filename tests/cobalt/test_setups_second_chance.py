"""STEP-8 of the setups one build (FINAL C7) — D6 RangeBreak lifecycle,
`event(retest)`, `event(stop_hit)`, `Range(prior)`, the anaphora `that
RangeBreak`, `close_through` / `close_above(prior_bar)` inside `sequence`
steps, the `sequence` trigger and the `turn_candle` stop — the break-retest-
turn setup (second-chance).

- `RangeBreak(level).state ∈ {forming, break_attempt, accepted, failed_trap}`
  (taxonomy §3.4 :104; `failed_trap` within `cfg(range_break.failed_trap_bars)`,
  `A-19`, a GLOBAL hole, fillable); `event(retest)` (`A-20`,
  `range_break.retest_tolerance_atr`); `event(stop_hit)` (`A-22`, computed from
  bars, never the card ledger); `Range(prior)` (`A-21`); `turn_candle` (`A-23`).
- The anaphora binds to the RangeBreak the previous precondition evaluated
  True; with no antecedent it is unknown, never "any".

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


def break_retest_turn(*, trap: bool = False) -> list[Bar]:
    """A day written from the definition: a premarket whose high is 10.05 (the
    level); an RTH climb under it; a bucket that closes THROUGH it (the break);
    two buckets holding above it (accepted); a pullback bucket whose low comes
    back to the level and closes above it (the retest); a bucket that closes
    above the prior bucket's high (the turn). `trap` instead closes the second
    bucket after the break back below the level (a failed trap)."""
    out, t = [], _et(8, 0)
    while t < _et(9, 30):
        high = "10.05" if t == _et(9, 0) else "10.01"
        out += _bucket(t, 10, high, "9.99", 10)
        t += timedelta(minutes=2)
    legs = [("10.00", "10.02", "9.90", "9.92"), ("9.92", "9.98", "9.88", "9.96"), ("9.96", "10.03", "9.94", "10.01"),
            ("10.01", "10.14", "10.00", "10.12"),  # the break: closes through 10.05
            ("10.12", "10.20", "10.10", "10.18")]
    legs += [("10.18", "10.19", "10.00", "10.02")] if trap else [("10.18", "10.26", "10.15", "10.24")]
    legs += [("10.24", "10.25", "10.06", "10.10"),  # the retest: back to the level, closes above it
             ("10.10", "10.30", "10.09", "10.28")]  # the turn: closes above the prior bucket's high
    for o, h, lo, c in legs:
        out += _bucket(t, o, h, lo, c)
        t += timedelta(minutes=2)
    return out


def _daily():
    from cobalt.radar.anatomy.daily import DailyBar, DailySeries

    bars = tuple(DailyBar(session_date=SYN_DATE - timedelta(days=d), open=10, high=12, low=7, close=10, volume=1)
                 for d in (8, 7, 6, 1))
    return DailySeries(ticker="SYN", bars=bars, fetched_at=_et(9, 0))


def _member(bars, at):
    from cobalt.radar.evaluate import MemberInput

    return MemberInput(membership_id=17, ticker="SYN", trade_date=SYN_DATE, as_of=at, bars=tuple(bars),
                       daily=_daily(), daily_status="cache-hit")


def _scan_after(bars):
    return bars[-1].ts + timedelta(minutes=1)


def _frame(bars):
    from cobalt.radar.evaluate import member_frames

    ld = shapes.load_shape_fresh("second-chance")
    return member_frames(_member(bars, _scan_after(bars)), tunables=shapes.tunables_for(ld), defaults=sup.defaults(),
                         clock=session_clock())["long"]


# =====================================================================
# The bricks
# =====================================================================


def test_the_rows():
    from cobalt.radar.evaluate import CONVENTION_LABELS

    rows = sup.engine_tunables()
    row = rows["range_break.retest_tolerance_atr"]
    assert (row.value, row.unit.value, row.scope, row.status.value) == (None, "atr", "global", "proposed")
    for key in ("range_prior.rule", "event.stop_hit.source", "turn_candle.rule"):
        row = rows[key]
        assert (row.value, row.unit.value, row.scope, row.status.value) == (None, "label", "global", "proposed"), key
        assert key in CONVENTION_LABELS
    assert rows["range_break.failed_trap_bars"].value is None  # A-19: a global hole, fillable


def test_the_range_break_lifecycle_on_the_definition_written_day():
    bars = break_retest_turn()
    fr = _frame(bars[:2 * (45 + 3)])  # before the break
    assert fr.atoms["RangeBreak(level).state"].symbol == "forming"
    fr = _frame(bars[:2 * (45 + 4)])  # the break bucket closed through the level
    assert fr.atoms["RangeBreak(level).state"].symbol == "accepted"
    fr = _frame(bars)
    assert fr.atoms["RangeBreak(level).state"].symbol == "accepted"
    assert fr.atoms["event(retest)"].boolean is True


def test_a_close_back_inside_within_the_window_is_a_failed_trap():
    fr = _frame(break_retest_turn(trap=True))
    assert fr.atoms["RangeBreak(level).state"].symbol == "failed_trap"


def test_the_domain_and_the_events_are_served():
    from cobalt.radar.anatomy.registry import evaluability
    from cobalt.radar.formation.atoms import ATOMS

    assert ATOMS["RangeBreak(level).state"].domain == frozenset({"forming", "break_attempt", "accepted",
                                                                  "failed_trap"})
    td = sup.anatomy_def(preconditions=[{"expr": "RangeBreak(level).state == accepted"},
                                        {"expr": "event(retest) on that RangeBreak"}],
                         avoid=[{"expr": "RangeBreak.state == failed_trap after event(retest)"},
                                {"expr": "event(stop_hit) AND price inside Range(prior)"}])
    assert evaluability(td).evaluable, evaluability(td).missing_atoms


def test_the_anaphora_with_no_antecedent_is_unknown_never_any():
    from cobalt.radar.evaluate import evaluate_node
    from cobalt.taxonomy.predicate import parse_predicate

    bars = break_retest_turn()
    fr = _frame(bars)
    unknowns: set[str] = set()
    ctx = {"frame": fr, "tunables": shapes.tunables_for(shapes.load_shape_fresh("second-chance")),
           "trigger": None, "minutes": 2}
    got = evaluate_node(parse_predicate("event(retest) on that RangeBreak"), fr.atoms, lambda k: None, set(),
                        unknowns, context=ctx)
    assert got is None and unknowns == {"no_antecedent"}


def test_the_sequence_trigger_and_the_turn_candle_stop_are_served():
    from cobalt.radar.formation.stops import STRUCTURAL_REFS
    from cobalt.radar.formation.triggers import trigger_resolver
    from cobalt.taxonomy.trade_def import StructuralRef

    td = shapes.load_shape_fresh("second-chance").definition
    assert trigger_resolver(td.trigger) is not None
    assert StructuralRef.TURN_CANDLE in STRUCTURAL_REFS


# =====================================================================
# THE PER-SETUP ACCEPTANCE — the break-retest-turn shape
# =====================================================================


def test_second_chance_shape_is_evaluable():
    from cobalt.radar.anatomy.registry import evaluability

    result = evaluability(shapes.load_shape_fresh("second-chance").definition)
    assert result.evaluable, result.missing_atoms


def test_second_chance_path_forms_long_on_the_definition_written_day():
    from cobalt.radar.anatomy.structure import structural_stop
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("second-chance")
    bars = break_retest_turn()
    ev = evaluate_member(ld, _member(bars, _scan_after(bars)), tunables=shapes.tunables_for(ld),
                         defaults=sup.defaults(), scan_interval=100, clock=session_clock())
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.missing, ev.note,
                                                                  ev.by_side["long"].note)
    f = ev.formation
    assert f.trigger_outcome.kind == "sequence" and f.trigger.price == Decimal("10.28")  # the turn bucket's close
    assert f.stop.price == structural_stop(Decimal("10.09"), "long", Decimal("0.02")).price  # the turn candle's low
    assert f.stop_ref == "turn_candle" and f.anchor.object == "RangeBreak(level)"


# --- FINAL §9 point (1): the four values, from the DEFINITION on the stored bars ---
# (with this build's constructed `A-19` / `A-20` — L69)
# engine at STEP-8; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_SECOND_CHANCE_SIDE = "long"
# engine at STEP-8; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_SECOND_CHANCE_FORMED_BAR = "2026-01-06T16:22:00+00:00"
# engine at STEP-8; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_SECOND_CHANCE_TRIGGER = "5.3000"
# engine at STEP-8; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_SECOND_CHANCE_STOP = "5.21"


def test_second_chance_forms_on_the_committed_day():
    ld = shapes.load_shape_fresh("second-chance")
    formed = [(at, ev) for ticker in ("FTFT", "BGFI") for at, ev in shapes.every_scan(ld, ticker)
              if ev.evaluation == "formed"]
    assert formed
    _at, ev = formed[0]
    f = ev.formation
    got = (ev.direction, f.formed_bar_ts.isoformat(), str(f.trigger.price), str(f.stop.price))
    print(f"second-chance on the committed day: formed_scans={len(formed)} ticker={ev.ticker} first={got}")
    assert got == (DEF_WRITTEN_SECOND_CHANCE_SIDE, DEF_WRITTEN_SECOND_CHANCE_FORMED_BAR,
                   DEF_WRITTEN_SECOND_CHANCE_TRIGGER, DEF_WRITTEN_SECOND_CHANCE_STOP)
    if f.trade_direction == "long":
        assert f.stop.price < min(f.trigger.price, ev.last_price)
    else:
        assert f.stop.price > max(f.trigger.price, ev.last_price)


def test_second_chance_path_a_failed_trap_does_not_form():
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("second-chance")
    bars = break_retest_turn(trap=True)
    ev = evaluate_member(ld, _member(bars, _scan_after(bars)), tunables=shapes.tunables_for(ld),
                         defaults=sup.defaults(), scan_interval=100, clock=session_clock())
    assert ev.evaluation != "formed"


def test_x7_second_chance_both_frames_on_the_committed_day():
    ld = shapes.load_shape_fresh("second-chance")
    rows = [ev for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(ld, ticker)]
    both = sum(ev.by_side["long"].evaluation == ev.by_side["short"].evaluation == "formed" for ev in rows)
    print(f"X7 second-chance: scans={len(rows)} formed={sum(ev.evaluation == 'formed' for ev in rows)} "
          f"both_sides={both}")
    assert both == 0


def test_x11_every_atom_the_second_chance_shape_consults():
    from cobalt.radar.formation.atoms import ATOMS
    from cobalt.radar.seam import AtomOutcome

    td = shapes.load_shape_fresh("second-chance").definition
    consulted = {a for p in [*td.preconditions, *td.avoid] for a in p.required_atoms if a in ATOMS}
    failures = []
    for name in sorted(consulted):
        for reason in ATOMS[name].reasons:
            try:
                AtomOutcome(atom=name, value_kind="unavailable", unavailable=reason)
            except ValueError:
                failures.append((name, reason))
    print(f"X11 second-chance: atoms={len(consulted)} failures={failures}")
    assert failures == []
