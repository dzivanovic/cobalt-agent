"""STEP-6 of the setups one build (FINAL C5) — D3's pullback / impulse /
pre_test roles, `touched`, `indicator_rejection`, the `indicator` stop,
`Extension … on Leg(x)`, the bound symbols, and the catalyst resolver `A-13`
(THE ONE NAMED SPECIAL CASE, FINAL §6) — the pullback-to-EMA9 setup
(nine-ema-scalp).

- X26 FIRST (hub: "construct `AtomOutcome(atom=…, value_kind="boolean",
  boolean=True, assumed="A-13")` … and follow the `detail()` caller").
- `A-13` serves `catalyst_ref` ONLY as a precondition atom; Extension path B
  keeps `catalyst_ref_unknown`, untouched. `AtomOutcome` gains no field: the
  resolver declares `A-13` (row key `catalyst_ref.resolver`) in the def's
  closure and the mark reaches the card through the `assumed_formation` dot.

Every constructed series is written from the definition's words; every
threshold is this file's literal (L69). R24 holds.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pydantic
import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.archiver.models import Bar, Interval
from cobalt.session import session_clock

UTC = timezone.utc
SYN_DATE = date(2026, 1, 6)
CATALYST_KEY = "catalyst_ref.resolver"  # A-13's convention row


def _et(h: int, m: int) -> datetime:
    return datetime(2026, 1, 6, h + 5, m, tzinfo=UTC)


def _bucket(start, o, h, lo, c, v=1000):
    o, h, lo, c = (Decimal(str(x)) for x in (o, h, lo, c))
    mid = (o + c) / 2
    return [Bar(ticker="SYN", interval=Interval.I1, ts=start, open=o, high=h, low=lo, close=mid, volume=v),
            Bar(ticker="SYN", interval=Interval.I1, ts=start + timedelta(minutes=1), open=mid, high=h, low=lo,
                close=c, volume=v)]


def impulse_pullback_rejection() -> list[Bar]:
    """A day written from the definition: a flat premarket (the seed); an
    impulse UP from the 10.00 open in wide, slowly rising buckets (no Extension:
    the move is small against its own ATR); a pullback of down buckets whose low
    reaches the EMA9 while price stays above the EMA21; then ONE bucket that
    touches the EMA9 and closes above it (the rejection)."""
    out, t = [], _et(8, 0)
    while t < _et(9, 30):
        out += _bucket(t, 10, "10.01", "9.99", 10)
        t += timedelta(minutes=2)
    o = Decimal(10)
    for _ in range(24):  # the impulse, 09:30 … 10:16 (long enough for the Extension detector to judge)
        out += _bucket(t, o, o + Decimal("0.18"), o - Decimal("0.12"), o + Decimal("0.01"))
        o += Decimal("0.01")
        t += timedelta(minutes=2)
    for c in ("10.20", "10.17"):  # the pullback
        out += _bucket(t, o, o + Decimal("0.02"), Decimal(c) - Decimal("0.06"), c)
        o = Decimal(c)
        t += timedelta(minutes=2)
    out += _bucket(t, o, "10.30", "10.10", "10.28")  # the rejection bar
    return out


def _member(bars, at, *, departed=False):
    from cobalt.radar.evaluate import MemberInput

    return MemberInput(membership_id=11, ticker="SYN", trade_date=SYN_DATE, as_of=at, bars=tuple(bars),
                       daily=None, daily_status="absent", departed=departed)


def _scan_after(bars):
    return bars[-1].ts + timedelta(minutes=1)


# =====================================================================
# X26 — FIRST
# =====================================================================


def test_x26_an_assumed_argument_on_the_atom_is_a_validation_error_and_detail_passes_none():
    """X26: the closed model refuses the mark (extra="forbid"), and the
    stage's `detail()` builds every `AtomOutcome` from the frame's value alone
    (it never passes `assumed`) — R2-2.4's premise holds."""
    import inspect

    from cobalt.radar import evaluate
    from cobalt.radar.seam import AtomOutcome

    with pytest.raises(pydantic.ValidationError) as caught:
        AtomOutcome(atom="catalyst_ref", value_kind="boolean", boolean=True, assumed="A-13")
    print(f"X26: {type(caught.value).__name__}: {str(caught.value).splitlines()[0]} | "
          f"{str(caught.value).splitlines()[1]}")
    assert "assumed" not in inspect.getsource(evaluate.evaluate_member).split("def detail(")[1].split("\n\n")[0]


# =====================================================================
# The bricks
# =====================================================================


def test_the_catalyst_resolver_is_an_atom_with_its_convention_row():
    from cobalt.radar.evaluate import CONVENTION_LABELS
    from cobalt.radar.formation.atoms import ATOMS

    assert ATOMS["catalyst_ref"].conventions == (CATALYST_KEY,)
    assert CATALYST_KEY in CONVENTION_LABELS
    for key in (CATALYST_KEY, "leg.pre_test", "extension.on_leg.form"):
        row = sup.engine_tunables()[key]
        assert (row.value, row.unit.value, row.scope, row.status.value) == (None, "label", "global", "proposed"), key


def test_extension_path_b_keeps_catalyst_ref_unknown():
    """FINAL §6: `A-13` never touches Extension path B."""
    import inspect

    from cobalt.radar.anatomy import extension

    assert 'unavailable="catalyst_ref_unknown"' in inspect.getsource(extension.detect_extension)


def test_null_comparisons_are_three_valued():
    from cobalt.radar.evaluate import evaluate_node
    from cobalt.radar.formation.atoms import AtomValue
    from cobalt.taxonomy.predicate import parse_predicate

    have = {"catalyst_ref": AtomValue(kind="boolean", boolean=True)}
    none = {"catalyst_ref": AtomValue(kind="null", reason="not_instantiated")}
    expr = parse_predicate("catalyst_ref != null")
    assert evaluate_node(expr, have, lambda k: None, set(), set()) is True
    assert evaluate_node(expr, none, lambda k: None, set(), set()) is False


def test_trade_direction_and_opposite_are_bound_from_the_frame():
    from cobalt.radar.anatomy.registry import evaluability

    td = sup.anatomy_def(preconditions=[{"expr": "Extension.state == culminating"},
                                        {"expr": "Leg(pullback).direction == opposite(trade_direction)"},
                                        {"expr": "Leg(opening_drive OR impulse).direction == trade_direction"}])
    assert evaluability(td).evaluable, evaluability(td).missing_atoms


def test_touched_and_on_are_served_relations():
    from cobalt.radar.anatomy.registry import evaluability
    from cobalt.radar.formation.atoms import RELATIONS

    assert {"touched", "on"} <= set(RELATIONS)
    ok = sup.anatomy_def(preconditions=[{"expr": "Extension.state == culminating"},
                                        {"expr": "Leg(pullback) touched EMA9"}],
                         avoid=[{"expr": "Extension.instantiated on Leg(pre_test)"}])
    assert evaluability(ok).evaluable, evaluability(ok).missing_atoms
    bad = sup.anatomy_def(preconditions=[{"expr": "Leg(pullback) touched RSI"}])
    assert not evaluability(bad).evaluable


def test_indicator_rejection_and_the_indicator_stop_are_served():
    from cobalt.radar.formation.stops import STOPS
    from cobalt.radar.formation.triggers import TRIGGERS
    from cobalt.taxonomy.trade_def import TriggerType

    ir = TRIGGERS[TriggerType.INDICATOR_REJECTION]
    assert ir.serves({"indicator": "EMA9", "contact": ["touch", "penetrate"]})
    assert not ir.serves({"indicator": "RSI", "contact": ["touch"]})
    assert "indicator" in STOPS


def test_the_roles_on_the_definition_written_day():
    from cobalt.radar.evaluate import member_frames

    bars = impulse_pullback_rejection()
    at = _scan_after(bars)
    fr = member_frames(_member(bars, at), tunables=shapes.tunables_for(shapes.load_shape_fresh("nine-ema-scalp")),
                       defaults=sup.defaults(), clock=session_clock())["long"]
    assert fr.atoms["Leg(pullback).direction"].symbol == "down"
    assert fr.atoms["Leg(opening_drive OR impulse).direction"].symbol == "up"
    assert fr.atoms["Leg(pullback).index"].number >= 1


# =====================================================================
# THE PER-SETUP ACCEPTANCE — the pullback-to-EMA9 shape
# =====================================================================


def test_nine_ema_scalp_shape_is_evaluable():
    from cobalt.radar.anatomy.registry import evaluability

    result = evaluability(shapes.load_shape_fresh("nine-ema-scalp").definition)
    assert result.evaluable, result.missing_atoms
    assert result.human_predicates == 1  # the tape read stays human (L11)


def test_nine_ema_scalp_path_forms_long_on_the_definition_written_day():
    from cobalt.radar.anatomy.structure import structural_stop
    from cobalt.radar.evaluate import evaluate_member, member_frames

    ld = shapes.load_shape_fresh("nine-ema-scalp")
    bars = impulse_pullback_rejection()
    at = _scan_after(bars)
    rows = shapes.tunables_for(ld)
    ev = evaluate_member(ld, _member(bars, at), tunables=rows, defaults=sup.defaults(), scan_interval=100,
                         clock=session_clock())
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.missing, ev.note,
                                                                  ev.by_side["long"].note)
    f = ev.formation
    assert f.trigger_outcome.kind == "indicator_rejection" and f.trigger.price == Decimal("10.28")  # its close
    fr = member_frames(_member(bars, at), tunables=rows, defaults=sup.defaults(), clock=session_clock())["long"]
    ema21_at_entry = fr.number("EMA21")
    assert f.stop.price == structural_stop(ema21_at_entry, "long", Decimal("0.02")).price  # at_entry snapshot
    assert f.stop.price < min(f.trigger.price, ev.last_price)
    assert CATALYST_KEY in f.assumed_keys  # A-13 marks the formation (FINAL §6)


# --- FINAL §9 point (1): the four values, from the DEFINITION on the stored bars ---
# engine at STEP-6; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_NINE_EMA_SCALP_SIDE = "long"
# engine at STEP-6; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_NINE_EMA_SCALP_FORMED_BAR = "2026-01-06T15:36:00+00:00"
# engine at STEP-6; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_NINE_EMA_SCALP_TRIGGER = "4.7930"
# engine at STEP-6; a checker house re-derives it blind (66, [F-16] (1))
DEF_WRITTEN_NINE_EMA_SCALP_STOP = "4.64"


def test_nine_ema_scalp_forms_on_the_committed_day():
    """[F-16] (1): the neutral shape FORMS on the committed real-shape day —
    `formed` + side + formed bar + trigger + stop, from the definition."""
    ld = shapes.load_shape_fresh("nine-ema-scalp")
    formed = [(at, ev) for ticker in ("FTFT", "BGFI") for at, ev in shapes.every_scan(ld, ticker)
              if ev.evaluation == "formed"]
    assert formed
    _at, ev = formed[0]
    f = ev.formation
    got = (ev.direction, f.formed_bar_ts.isoformat(), str(f.trigger.price), str(f.stop.price))
    print(f"nine-ema-scalp on the committed day: formed_scans={len(formed)} first={got}")
    assert got == (DEF_WRITTEN_NINE_EMA_SCALP_SIDE, DEF_WRITTEN_NINE_EMA_SCALP_FORMED_BAR,
                   DEF_WRITTEN_NINE_EMA_SCALP_TRIGGER, DEF_WRITTEN_NINE_EMA_SCALP_STOP)
    assert f.stop.price < min(f.trigger.price, ev.last_price) if f.trade_direction == "long" \
        else f.stop.price > max(f.trigger.price, ev.last_price)  # the geometry guard (§9 point (5))


def test_nine_ema_scalp_path_a_departed_member_has_no_catalyst():
    from cobalt.radar.evaluate import evaluate_member

    ld = shapes.load_shape_fresh("nine-ema-scalp")
    bars = impulse_pullback_rejection()
    ev = evaluate_member(ld, _member(bars, _scan_after(bars), departed=True), tunables=shapes.tunables_for(ld),
                         defaults=sup.defaults(), scan_interval=100, clock=session_clock())
    assert ev.evaluation == "not_formed"


def test_x7_nine_ema_scalp_both_frames_on_the_committed_day():
    ld = shapes.load_shape_fresh("nine-ema-scalp")
    rows = [ev for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(ld, ticker)]
    both = sum(ev.by_side["long"].evaluation == ev.by_side["short"].evaluation == "formed" for ev in rows)
    print(f"X7 nine-ema-scalp: scans={len(rows)} formed={sum(ev.evaluation == 'formed' for ev in rows)} "
          f"both_sides={both}")
    assert both == 0


def test_x11_every_atom_the_nine_ema_shape_consults():
    from cobalt.radar.formation.atoms import ATOMS
    from cobalt.radar.seam import AtomOutcome

    td = shapes.load_shape_fresh("nine-ema-scalp").definition
    consulted = {a for p in [*td.preconditions, *td.avoid] for a in p.required_atoms if a in ATOMS}
    failures = []
    for name in sorted(consulted):
        for reason in ATOMS[name].reasons:
            try:
                AtomOutcome(atom=name, value_kind="unavailable", unavailable=reason)
            except ValueError:
                failures.append((name, reason))
    print(f"X11 nine-ema-scalp: atoms={len(consulted)} failures={failures}")
    assert failures == []
