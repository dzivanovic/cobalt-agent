"""STEP-3 of the setups one build (FINAL C3a) — D1 shared indicators,
session levels and the premarket warm-up (FINAL §3 D1, §5; [F-10], [F-11],
[F-14 · X11]).

- [F-10], as tests: "The Extension's RTH-run ATR KEEPS the name
  `atr_working` … The premarket-seeded ATR is a new quantity named
  `atr_seeded`. Both are `wilder_atr` over different series: one function,
  two named inputs. EMA9 and EMA21 have ONE definition each — seeded,
  falling back to RTH-only when the seed is short — and
  `MemberEvaluation.ema9` takes that value."
- [F-11], as tests: "the Extension, `atrs_from_open`, `leg_count`, the dots
  and `card_score` do not move; the card's `health` moves (its EMA9 becomes
  seeded); the seam observation `atr_working` keeps its name and meaning" —
  golden pins captured on the START-of-step code (`c74436c`) on every one
  of those except `health`.
- X14 (hub: "C3 build + replay of a FILLED card" — "A number other than
  `health` moves → C3a's deploy note (F-10) is wrong"), offline over the
  committed day and a FILLED card built here.
- X11 (Fable: "for every atom the newly unlocked def consults, construct
  its `AtomOutcome` through `seam.validate_atom` with every declared
  reason") over every atom this step serves.
- Each detector on constructed series and on the committed day.

R24 / L69: no value of the trader's anywhere; every threshold here is a
constructed literal of this test.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.radar.anatomy.bars import WorkingBar, rth_only, working_bars
from cobalt.radar.anatomy.extension import ExtensionParams, detect_extension
from cobalt.radar.evaluate import working_minutes
from cobalt.session import session_clock
from cobalt.taxonomy.trade_def import TradeDef
from cobalt.taxonomy.tunables import TunableRow
from test_radar_evaluate import ENABLED_CARD, World

UTC = timezone.utc
SCAN0 = shapes.SCAN0
#: The keys committed `tunables.yaml` gains at this step (their rows move
#: `tunables_sha256` by construction; the pins map the digest back).
STEP3_KEYS = ("dayrange.session", "frame.warmup_source", "slope_norm.bars", "vwap.anchor")
#: + the rows later steps add (each moves the digest by construction).
ADDED_KEYS = (*STEP3_KEYS, "leg.consolidation_max_retrace", "range.micro.bound_flat_slope_atr",
              "range.micro.touch_tolerance_atr", "extension.snapback_bars_cleared",
              "catalyst_ref.resolver", "leg.pre_test", "extension.on_leg.form",
              "levels.set", "level.rejected.rule",
              "range_break.retest_tolerance_atr", "range_prior.rule", "event.stop_hit.source", "turn_candle.rule",
              "leg.min_size_atr")  # + fix r3 F3's `A-24` row (R49)
STEP3_CONVENTIONS = ("dayrange.session", "frame.warmup_source", "vwap.anchor")


def _sha(payload) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()


@pytest.fixture(scope="module")
def defs(tmp_path_factory) -> dict[str, sup.LoadedDef]:
    out = {}
    for name, valid_setups, htf in (
        ("mixed", shapes.MIXED, False), ("countertrend", shapes.COUNTERTREND_ONLY, False),
        ("full", shapes.MIXED, True),
    ):
        out[name] = shapes.load_note(tmp_path_factory.mktemp(name), f"shape-{name}-d1",
                                     shapes.rubberband_mapping(valid_setups, htf_avoid=htf))
    out["shipped"] = sup.loaded(TradeDef.from_unit(shapes.example_mapping(), slug="example-range-break",
                                                   name="Example Range Break"),
                                md5="fedcba9876543210fedcba9876543210")
    return out


def _closed(at: datetime, ticker: str = "FTFT"):
    return [b for b in shapes.bars(ticker) if b.ts + timedelta(minutes=1) <= at]


def _series(at: datetime, ticker: str = "FTFT"):
    return working_bars(_closed(at, ticker), working_minutes(sup.defaults()), as_of=at)


def _run(at: datetime, ticker: str = "FTFT"):
    return tuple(rth_only(_series(at, ticker), session_clock()))


def _row(key: str, value, *, unit: str = "bars", scope: str = "global") -> TunableRow:
    return TunableRow(key=key, value=value, unit=unit, scope=scope, dynamic=True, status="proposed",
                      source="dwv", consumers=["test"])


def _wb(ts: datetime, o, h, lo, c, v=1000, minutes=2, complete=True) -> WorkingBar:
    return WorkingBar(ts=ts, minutes=minutes, open=Decimal(str(o)), high=Decimal(str(h)), low=Decimal(str(lo)),
                      close=Decimal(str(c)), volume=v, complete=complete, minutes_present=minutes if complete else 1)


# =====================================================================
# [F-11] — the golden pins (captured on the START-of-step code)
# =====================================================================

#: What [F-11] lets move, excluded from the pins: `MemberEvaluation.ema9`
#: (the health input — seeded from this step) and the NEW seam observation
#: `atr_seeded` ([F-10], published beside `atr_working`). Everything else of
#: every evaluation — the Extension atoms and seam observations, the factor
#: observations `atrs_from_open` / `Extension.leg_count`, the formation, both
#: frames — must be byte-identical.
F11_MOVES = {"ema9"}
NEW_OBSERVATIONS = {"atr_seeded"}


#: The atoms this step SERVES (the registry's by-design change): a def that
#: stays `not_evaluable` for OTHER atoms no longer lists these as missing —
#: the shipped example names `DayRange.upper_third`. Re-added so the pin
#: proves nothing else moved.
SERVED_AT_STEP3 = {
    "price", "EMA9", "EMA21", "EMA9.slope", "slope_norm(EMA9)", "slope_norm(VWAP)", "VWAP", "ATR(working_tf)",
    "DayRange.high", "DayRange.low", "DayRange.upper_third", "PMH", "PML", "PDH", "PDL", "InPlay.state",
}


#: STEP-4 serves more (the registry's by-design change again): the D2 / D3
#: atoms, `range_break`, the `range_base` / `consolidation_low` stop and the
#: `IN cfg(band) <unit>` shape (its E9 name `Unsupported(in)`).
SERVED_AT_STEP4 = {
    "Range(micro).instantiated", "Range(micro).duration", "Range(micro).low", "Range(micro).top",
    "Range(micro).base", "Range(micro).bound", "Range(micro).height", "Range(micro).wick_ratio",
    "Leg(opening_drive).direction", "Leg(opening_drive).terminated_by",
}
SERVED_TRIGGERS_AT_STEP4 = {"range_break"}
SERVED_STOP_REFS_AT_STEP4 = {"range_base", "consolidation_low"}


def _served_later(ld) -> set[str]:
    """The names a not-evaluable def listed as missing at the START of STEP-3
    that a later step now serves — derived from the def itself."""
    from cobalt.taxonomy.predicate import InTest, Quantity

    td = ld.definition
    named = {a for p in [*td.preconditions, *td.avoid] for a in p.required_atoms}
    out = named & (SERVED_AT_STEP3 | SERVED_AT_STEP4)
    if td.trigger.type in SERVED_TRIGGERS_AT_STEP4:
        out.add(f"trigger:{td.trigger.type}")
    ref = getattr(td.stop.placement, "ref", None)
    if ref is not None and ref.value in SERVED_STOP_REFS_AT_STEP4:
        out.add(f"stop:{td.stop.placement.type}:{ref.value}")
    if any(isinstance(p.ast, InTest) and isinstance(p.ast.right, Quantity) for p in td.preconditions if p.expr):
        out.add("Unsupported(in)")
    return out


def _unmoved(ev, ld=None) -> dict:
    from cobalt.radar.evaluate import seam_safe_missing_atoms

    dump = {k: v for k, v in ev.model_dump(mode="json").items() if k not in F11_MOVES}
    dump["detail"] = {**dump["detail"], "observations": [
        o for o in dump["detail"]["observations"] if o["name"] not in NEW_OBSERVATIONS]}
    if ld is not None and dump["evaluation"] == "not_evaluable" and dump["missing"]:
        dump["missing"] = sorted(set(dump["missing"]) | _served_later(ld))
        dump["detail"]["missing_atoms"] = list(seam_safe_missing_atoms(dump["missing"]))
    return dump


def _tunables_digests() -> tuple[str, str]:
    from cobalt.radar.evaluate import canonical_sha256

    rows = {k: row.model_dump(mode="json") for k, row in sorted(sup.engine_tunables().items())}
    defaults = sup.defaults().model_dump(mode="json")
    new = canonical_sha256({"rows": rows, "defaults": defaults})
    start = {k: v for k, v in rows.items() if k not in ADDED_KEYS}
    start["stop.buffer"] = {**start["stop.buffer"], "unit": "cents"}  # fix r3 F5 (R51): the label only, mapped back
    old = canonical_sha256({"rows": start, "defaults": defaults})
    return new, old


def _card_unmoved(card: dict) -> dict:
    out = {k: v for k, v in card.items() if k not in {"formula_sha256", "dots"}}
    new, old = _tunables_digests()
    assert out["tunables_sha256"] in (new, old)
    out["tunables_sha256"] = old
    out["dots"] = [d.model_dump(mode="json") for d in card["dots"]]
    return out


PIN_F11_EVALUATIONS = {
    "countertrend": "29d45b870be35083576c5edf029ba540f65cddc84e1f41fdc361ad0342fc9d34",
    "full": "fedf05ca2d82db4681e38dcd7c67c026bd1d475fd55fd612412a28338b3aec7b",
    "mixed": "5a9fdfe497f8f8f96a2595f2450108b6a0a574995eeeb22b341d52641a2bcff4",
    "shipped": "54c841b587eaab8184b0785b83669d885eff4efc0a41b8fecda1e717dd871ee0",
}
#: The cards the stage makes AND refreshes over the day (dots, card_score).
PIN_F11_CARDS = {
    "countertrend": "77c3ce1fc3d350a12a3b520e660cc018bdc86af55d86507d04e38b8acde6a03c",
    "mixed": "4e17a9fecfba006b1baa7e5e88224836d1c87aa9a0685e88c3e469a9f749dd94",
}


@pytest.mark.parametrize("name", sorted(PIN_F11_EVALUATIONS))
def test_f11_nothing_but_health_moves_in_any_evaluation(defs, name):
    ld = defs[name]
    dumps = [_unmoved(ev, ld) for ticker in ("FTFT", "BGFI") for _, ev in shapes.every_scan(ld, ticker)]
    assert _sha(dumps) == PIN_F11_EVALUATIONS[name]


@pytest.mark.parametrize("name", sorted(PIN_F11_CARDS))
def test_f11_the_dots_and_card_score_do_not_move(defs, name):
    world = World(defs=[defs[name]])
    for at, _ in shapes.every_scan(defs[name], "FTFT"):
        world.scan(at)
    assert world.cards.cards
    assert _sha([_card_unmoved(world.cards.cards[c]) for c in sorted(world.cards.cards)]) == PIN_F11_CARDS[name]


# ---------------------------------------------------------------------
# X14 — a FILLED card replayed across the day: only `health` may move
# ---------------------------------------------------------------------

#: Constructed thresholds (L69) — any values make the pills computable.
X14_THRESHOLDS = dict(participation_warn=Decimal("0.5"), participation_bad=Decimal("0.25"),
                      cost_warn=Decimal("0.5"), cost_bad=Decimal("1"), dot_warn_drop=2, dot_bad_max=3,
                      structural_warn="touched", structural_bad="lost_on_close")
PIN_X14_NOT_HEALTH = "9317848c7f1d48089b181ac7bcd50c5364cd5f8f72d072b0cf3217daefb61d90"
#: The START-of-step `health` digest — [F-11] says it moves.
PIN_X14_HEALTH_START = "584e0c7441d259814028d973c31bdc26b7e68d59a7c0f7b19cb093183e5331ba"


def _x14_updates(ld) -> tuple[list[dict], list]:
    from cobalt.cards.health import HealthThresholds
    from cobalt.radar.evaluate import OpenRadarCard, refresh_card
    from cobalt.settings.card import CardSettings

    settings = CardSettings.from_rows(sup.fixture_settings_rows(**ENABLED_CARD))
    thresholds = HealthThresholds(**X14_THRESHOLDS)
    rows = shapes.every_scan(ld, "FTFT")
    formed_at, formed = next((at, ev) for at, ev in rows if ev.evaluation == "formed")
    f = formed.formation
    card = OpenRadarCard(
        card_id=1, pool_member_id=100, ticker="FTFT", direction=f.trade_direction, state="FILLED",
        trade_def_slug=ld.slug, trade_def_md5=ld.md5, trigger_price=f.trigger.price, structural_stop=f.stop.price,
        entry=f.trigger.price, stop=f.stop.price, formed_at=f.formed_bar_ts, expires_at=formed_at + timedelta(hours=8),
    )
    others, healths = [], []
    for at, ev in rows:
        if at <= formed_at:
            continue
        update = refresh_card(card, ev, ld, settings, [], at=at, thresholds=thresholds)
        card = card.model_copy(update={"health": update.health, "dots": update.dots})
        dump = update.model_dump(mode="json")
        healths.append(dump.pop("health"))
        others.append(dump)
    return others, healths


def test_x14_a_filled_card_replayed_over_the_day_moves_only_health(defs):
    others, healths = _x14_updates(defs["countertrend"])
    assert len(others) > 50
    moved = _sha(healths) != PIN_X14_HEALTH_START
    print(f"X14: filled-card refreshes={len(others)} non-health numbers moved="
          f"{_sha(others) != PIN_X14_NOT_HEALTH} health moved={moved}")
    assert _sha(others) == PIN_X14_NOT_HEALTH


# =====================================================================
# [F-10] — `atr_working` unchanged, `atr_seeded` new, EMAs seeded
# =====================================================================


def _obs(ev, name):
    return next((o for o in ev.detail.observations if o.name == name), None)


def test_f10_atr_working_keeps_its_name_and_meaning(defs):
    params = ExtensionParams.from_tunables(sup.engine_tunables())
    checked = 0
    for at, ev in shapes.every_scan(defs["countertrend"], "FTFT"):
        ext = detect_extension(_run(at), params)
        assert _obs(ev, "atr_working").value == (ext.atr.value if ext.atr else None), at
        checked += ext.atr is not None
    assert checked > 100  # 107 scans of the day carry an RTH-run ATR


def test_f10_atr_seeded_is_wilder_atr_over_the_warm_series(defs):
    from cobalt.radar.anatomy.frame import premarket_buckets
    from cobalt.radar.anatomy.indicators import ATR_PERIOD, wilder_atr

    seeded_from_premarket = 0
    for at, ev in shapes.every_scan(defs["countertrend"], "FTFT"):
        pre, run = premarket_buckets(_series(at).bars, session_clock()), _run(at)
        got = _obs(ev, "atr_seeded").value
        if len(pre) >= ATR_PERIOD:
            assert got == wilder_atr([*pre, *run]).value, at
            seeded_from_premarket += 1
        elif len(run) >= ATR_PERIOD:
            assert got == wilder_atr(run).value, at
        else:
            assert got is None, at
    assert seeded_from_premarket > 150


def test_f10_one_function_two_named_inputs():
    from cobalt.radar.anatomy import indicators
    from cobalt.radar.anatomy.indicators import ATR_PERIOD, seeded, wilder_atr

    assert {n for n in indicators.__all__ if "atr" in n.lower()} == {"ATR_PERIOD", "AtrObservation", "wilder_atr"}
    run = _run(SCAN0)
    assert seeded(wilder_atr, (), run, ATR_PERIOD).value == wilder_atr(run).value  # the RTH-only fallback
    assert seeded(wilder_atr, (), run, ATR_PERIOD).source == "rth_only"


def test_f10_member_evaluation_ema9_takes_the_seeded_value(defs):
    from cobalt.radar.anatomy.frame import premarket_buckets
    from cobalt.radar.anatomy.indicators import ema, seeded

    fast = sup.defaults().ma.fast
    differs = 0
    for at, ev in shapes.every_scan(defs["countertrend"], "FTFT"):
        pre, run = premarket_buckets(_series(at).bars, session_clock()), _run(at)
        assert ev.ema9 == seeded(ema, pre, run, fast).value, at
        if len(run) >= fast and ev.ema9 != ema(run, fast).value:
            differs += 1
    assert differs > 0  # the health input moved — [F-11]


def test_f10_the_seed_uses_complete_premarket_buckets_only_and_falls_back_when_short():
    from cobalt.radar.anatomy.frame import premarket_buckets
    from cobalt.radar.anatomy.indicators import ema, seeded

    clock = session_clock()
    t0 = datetime(2026, 1, 6, 13, 0, tzinfo=UTC)  # 08:00 ET, premarket
    pre = [_wb(t0 + timedelta(minutes=2 * i), 5, 5.1, 4.9, 5 + i / 100) for i in range(12)]
    pre[3] = pre[3].model_copy(update={"complete": False, "minutes_present": 1})
    rth0 = datetime(2026, 1, 6, 14, 30, tzinfo=UTC)
    run = [_wb(rth0 + timedelta(minutes=2 * i), 6, 6.1, 5.9, 6 + i / 100) for i in range(5)]
    kept = premarket_buckets([*pre, *run], clock)
    assert len(kept) == 11 and all(b.complete for b in kept)  # the incomplete bucket is dropped, RTH excluded
    s9 = seeded(ema, kept, run, 9)
    assert (s9.source, s9.premarket_buckets, s9.bars_used) == ("premarket", 11, 16)
    assert s9.value == ema([*kept, *run], 9).value
    s21 = seeded(ema, kept, run, 21)  # seed short and RTH short → unavailable, never guessed
    assert (s21.value, s21.unavailable) == (None, "insufficient_seed")
    long_run = [_wb(rth0 + timedelta(minutes=2 * i), 6, 6.1, 5.9, 6) for i in range(21)]
    s21b = seeded(ema, kept, long_run, 21)  # the RTH-only warm-up, later
    assert (s21b.source, s21b.value) == ("rth_only", ema(long_run, 21).value)


# =====================================================================
# The detectors — constructed series
# =====================================================================


def test_day_range_and_its_upper_third():
    from cobalt.radar.anatomy.session_levels import day_range

    t = datetime(2026, 1, 6, 14, 30, tzinfo=UTC)
    run = [_wb(t, 10, 11, 9.5, 10.5), _wb(t + timedelta(minutes=2), 10.5, 12, 10, 11)]
    dr = day_range(run)
    assert (dr.high, dr.low, dr.upper_third) == (Decimal(12), Decimal("9.5"), Decimal("9.5") + Decimal(2) / 3 * Decimal("2.5"))
    assert day_range([]) is None


def test_vwap_is_rth_anchored_typical_price_on_i1():
    from cobalt.radar.anatomy.session_levels import vwap

    t = datetime(2026, 1, 6, 14, 30, tzinfo=UTC)
    i1 = [_wb(t, 10, 11, 9, 10, v=100, minutes=1), _wb(t + timedelta(minutes=1), 10, 12, 10, 11, v=300, minutes=1)]
    obs = vwap(i1)
    expected = (Decimal(30) / 3 * 100 + Decimal(33) / 3 * 300) / 400
    assert obs.value == expected and obs.bars_used == 2 and obs.unavailable is None
    assert vwap([]).unavailable == "insufficient_bars"
    assert vwap([i1[0].model_copy(update={"volume": 0})]).unavailable == "insufficient_bars"  # no volume, no divide


def test_premarket_and_prior_day_levels():
    from cobalt.radar.anatomy.daily import DailyBar, DailySeries, NoDailyBars
    from cobalt.radar.anatomy.session_levels import premarket_levels, prior_day_levels

    t = datetime(2026, 1, 6, 12, 0, tzinfo=UTC)
    pm = premarket_levels([_wb(t, 5, 5.5, 4.8, 5.2, minutes=1), _wb(t + timedelta(minutes=1), 5.2, 5.9, 5.1, 5.3, minutes=1)])
    assert (pm.high, pm.low) == (Decimal("5.9"), Decimal("4.8"))
    assert premarket_levels([]) is None
    series = DailySeries(ticker="X", bars=(
        DailyBar(session_date=sup.TRADE_DATE - timedelta(days=1), open=1, high=2, low=Decimal("0.5"), close=1, volume=1),
    ))
    pd = prior_day_levels(series, sup.TRADE_DATE)
    assert (pd.high, pd.low) == (Decimal(2), Decimal("0.5"))
    with pytest.raises(NoDailyBars):
        prior_day_levels(DailySeries(ticker="X", bars=()), sup.TRADE_DATE)


def test_slope_slope_norm_and_a_null_window_key():
    from cobalt.radar.anatomy.slope import TUNABLE_KEYS, slope, slope_bars, slope_norm

    assert TUNABLE_KEYS == ("slope_norm.bars",)
    series = [Decimal(v) for v in ("1.0", "1.2", "1.5", "1.9")]
    s = slope(series, 3)
    assert s.value == (Decimal("1.9") - Decimal("1.0")) / 3 and s.unavailable is None
    assert slope(series, 4).unavailable == "insufficient_bars"
    n = slope_norm(series, 3, atr=Decimal("0.3"))
    assert n.value == (Decimal("1.9") - Decimal("1.0")) / (3 * Decimal("0.3"))
    assert slope_norm(series, 3, atr=Decimal(0)).unavailable == "insufficient_bars"  # never inf
    assert slope_bars({"slope_norm.bars": _row("slope_norm.bars", None)}) is None  # → `slope_norm.bars_unset`
    assert slope_bars({"slope_norm.bars": _row("slope_norm.bars", 5)}) == 5
    with pytest.raises(KeyError):
        slope_bars({})  # a missing row is a config error, loud


def test_flat_over_a_window():
    from cobalt.radar.anatomy.slope import FLAT_KEYS, flat, flat_threshold

    assert FLAT_KEYS == {"EMA9": "flat_threshold.ema9", "VWAP": "flat_threshold.vwap"}
    th = Decimal("0.1")
    assert flat([Decimal("0.05"), Decimal("-0.1"), Decimal("0")], th) is True
    assert flat([Decimal("0.05"), Decimal("0.11")], th) is False
    assert flat([], th) is None
    rows = {"flat_threshold.ema9": _row("flat_threshold.ema9", None, unit="ratio", scope="per_indicator(ema9)")}
    assert flat_threshold(rows, "EMA9") is None  # F1 not widened: the per_indicator hole stays null


def test_in_play_state_reads_pool_admission():
    from cobalt.radar.anatomy.in_play import DOMAIN, in_play_state

    assert DOMAIN == frozenset({"active", "departed"})
    assert in_play_state(departed=False) == "active" and in_play_state(departed=True) == "departed"


# =====================================================================
# The atoms — served, in both frames, on the committed day
# =====================================================================

D1_ATOMS = SERVED_AT_STEP3


def test_the_d1_atoms_are_served_with_their_domain_keys_and_conventions():
    from cobalt.radar.anatomy import slope
    from cobalt.radar.formation.atoms import ATOMS

    assert D1_ATOMS <= set(ATOMS)
    assert ATOMS["InPlay.state"].domain == frozenset({"active", "departed"})
    for name in ("slope_norm(EMA9)", "slope_norm(VWAP)", "EMA9.slope"):
        assert ATOMS[name].tunable_keys == slope.TUNABLE_KEYS
    for name in ("EMA9", "EMA21", "ATR(working_tf)", "EMA9.slope", "slope_norm(EMA9)", "slope_norm(VWAP)"):
        assert "frame.warmup_source" in ATOMS[name].conventions, name
    for name in ("DayRange.high", "DayRange.low", "DayRange.upper_third"):
        assert ATOMS[name].conventions == ("dayrange.session",)
    assert "vwap.anchor" in ATOMS["VWAP"].conventions and "vwap.anchor" in ATOMS["slope_norm(VWAP)"].conventions
    assert ATOMS["ATR(working_tf)"].price is False and ATOMS["VWAP"].price is True


def test_the_new_rows_are_engine_rows_null_and_proposed():
    from cobalt.radar.evaluate import CONVENTION_LABELS

    rows = sup.engine_tunables()
    row = rows["slope_norm.bars"]
    assert (row.value, row.unit.value, row.scope, row.status.value) == (None, "bars", "global", "proposed")
    for key in STEP3_CONVENTIONS:
        row = rows[key]
        assert (row.value, row.unit.value, row.scope, row.status.value) == (None, "label", "global", "proposed"), key
        assert key in CONVENTION_LABELS


def _frames(at: datetime = SCAN0, *, tunables=None, departed=False):
    """Both frames of the committed FTFT day at `at`, through the stage's own builder."""
    from cobalt.radar.evaluate import MemberInput, member_frames

    m = shapes.member("FTFT", at)
    if departed:
        m = m.model_copy(update={"departed": True})
    assert isinstance(m, MemberInput)
    return member_frames(m, tunables=tunables or sup.engine_tunables(), defaults=sup.defaults(), clock=session_clock())


def _num(frame, name):
    atom = frame.atoms[name]
    assert atom.kind == "number", (name, atom)
    return atom.number


def test_the_committed_day_every_d1_atom_has_a_value_with_a_constructed_window():
    from cobalt.radar.anatomy.session_levels import vwap as _vwap
    from cobalt.session.models import Session

    tunables = {**sup.engine_tunables(), "slope_norm.bars": _row("slope_norm.bars", 4)}
    frames = _frames(tunables=tunables)
    long = frames["long"]
    for name in D1_ATOMS - {"InPlay.state"}:
        _num(long, name)
    assert long.atoms["InPlay.state"].symbol == "active"
    clock = session_clock()
    closed = _closed(SCAN0)
    rth = [b for b in closed if clock.session(b.ts) is Session.RTH]
    pre = [b for b in closed if clock.session(b.ts) is Session.PREMARKET]
    run = _run(SCAN0)
    assert _num(long, "DayRange.high") == max(b.high for b in run)
    assert _num(long, "DayRange.low") == min(b.low for b in run)
    assert _num(long, "PMH") == max(b.high for b in pre) and _num(long, "PML") == min(b.low for b in pre)
    assert _num(long, "price") == closed[-1].close
    flt = sum(float((b.high + b.low + b.close) / 3) * b.volume for b in rth) / sum(b.volume for b in rth)
    assert abs(float(_num(long, "VWAP")) - flt) < 1e-6  # an independent float recompute
    assert _vwap([]).value is None


def test_f04_the_short_frame_reads_the_mirrored_levels():
    tunables = {**sup.engine_tunables(), "slope_norm.bars": _row("slope_norm.bars", 4)}
    frames = _frames(tunables=tunables)
    long, short = frames["long"], frames["short"]
    for name in ("price", "EMA9", "EMA21", "VWAP"):
        assert short.real(_num(short, name)) == _num(long, name), name
    for name in ("EMA9.slope", "slope_norm(EMA9)", "slope_norm(VWAP)"):
        assert _num(short, name) == -_num(long, name), name  # a slope flips with the mirror
    assert _num(short, "ATR(working_tf)") == _num(long, "ATR(working_tf)")
    assert short.real(_num(short, "DayRange.high")) == _num(long, "DayRange.low")
    assert short.real(_num(short, "PMH")) == _num(long, "PML")
    assert short.real(_num(short, "PDH")) == _num(long, "PDL")
    hi, lo = _num(long, "DayRange.high"), _num(long, "DayRange.low")
    assert short.real(_num(short, "DayRange.upper_third")) == hi - Decimal(2) / 3 * (hi - lo)  # the short side's third


def test_at_committed_defaults_a_slope_atom_reads_its_unset_key(defs):
    frames = _frames()
    for name in ("EMA9.slope", "slope_norm(EMA9)", "slope_norm(VWAP)"):
        atom = frames["long"].atoms[name]
        assert (atom.kind, atom.reason) == ("unavailable", "slope_norm.bars_unset"), name


def test_in_play_state_is_departed_for_a_departed_member():
    assert _frames(departed=True)["long"].atoms["InPlay.state"].symbol == "departed"


def test_a_def_on_d1_atoms_is_evaluable_and_consults_only_what_it_names():
    from cobalt.radar.anatomy.registry import evaluability

    td = sup.anatomy_def(preconditions=[{"expr": "Extension.state == culminating"}, {"expr": "price > VWAP"},
                                        {"expr": "InPlay.state == active"}])
    assert evaluability(td).evaluable
    assert not evaluability(sup.anatomy_def(preconditions=[{"expr": "InPlay.state == halted"}])).evaluable  # E8
    ev = shapes.evaluate(sup.loaded(td, md5="00000000000000000000000000000d01"), "FTFT", SCAN0)
    assert {a.atom for a in ev.detail.atoms} >= {"price", "VWAP", "InPlay.state"}


def test_the_closure_of_a_d1_def_carries_its_keys_and_conventions():
    from cobalt.radar.evaluate import assumed_closure, closure_keys

    td = sup.anatomy_def(preconditions=[{"expr": "Extension.state == culminating"},
                                        {"expr": "slope_norm(EMA9) > 0"}, {"expr": "DayRange.upper_third < price"}])
    keys = closure_keys(td)
    assert {"slope_norm.bars", "frame.warmup_source", "dayrange.session"} <= keys
    assert {"frame.warmup_source", "dayrange.session"} <= set(assumed_closure(td, sup.engine_tunables()))


def test_x22_a_rubberband_def_reads_no_d1_key(defs):
    """The frame serves the D1 atoms lazily: a def that names none of them
    reads none of their keys (X22's property holds at this step)."""
    import test_setups_registries as reg

    from cobalt.radar.evaluate import closure_keys

    rows = reg._RecordingRows(sup.engine_tunables())
    for m in range(0, 391, 30):
        shapes.evaluate(defs["mixed"], "FTFT", shapes.DAY_START + timedelta(minutes=m), tunables=rows)
    # STEP-5 re-point (FINAL §3 D4): `Extension.state`'s resolver now declares
    # `slope_norm.bars` (the lifecycle's rising-EMA9 test), so it is in the
    # def's closure by design; no OTHER D1 key is read, and every read is declared.
    declared = closure_keys(defs["mixed"].definition)
    d1 = {"slope_norm.bars", *STEP3_CONVENTIONS, "flat_threshold.ema9", "flat_threshold.vwap"}
    assert not rows.read & (d1 - declared)
    assert rows.read <= declared


# =====================================================================
# X11 — every declared reason of every atom through the closed seam
# =====================================================================


def test_x11_every_atom_and_every_declared_reason_constructs_an_atom_outcome():
    from cobalt.radar.formation.atoms import ATOMS
    from cobalt.radar.seam import AtomOutcome, validate_atom

    failures = []
    for name, resolver in sorted(ATOMS.items()):
        assert validate_atom(name) == name
        # every atom but the pool admission (always known) can lack a value
        assert resolver.reasons or name == "InPlay.state", f"{name} declares no reason"
        for reason in resolver.reasons:
            try:
                AtomOutcome(atom=name, value_kind="unavailable", unavailable=reason)
            except ValueError as e:
                failures.append((name, reason, type(e).__name__))
    print(f"X11: atoms={len(ATOMS)} failures={failures}")
    assert failures == []
