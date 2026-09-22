"""S2-P2 STEP-3 — anatomy detectors: pure functions over bars (R2/R4/R5).

Real-shape inputs where the real artifact exists (L45): the hub-cut i1
bars (`bars-rubberband.real-shape.json`) exercise working-TF completeness
exactly as production bars arrive — thin names, missing minutes. The
math conventions (Astra R1-9: ATR smoothing/seed/warm-up, volume band
sample/σ, Leg doji treatment, HTF day-count continuity) are specified by
boundary vectors, long/short mirrored, with an independent recompute of
every intermediate.
"""

from __future__ import annotations

import csv
import json
import math
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.radar.anatomy.bars import IncompleteBucket, WorkingBar, rth_only, working_bars
from cobalt.radar.anatomy.daily import (
    DailyBar,
    DailySeries,
    NoDailyBars,
    daily_atr,
    htf_level_proximity,
    htf_range_break,
    parse_daily_csv,
    prior_session,
)
from cobalt.radar.anatomy.extension import ExtensionParams, detect_extension
from cobalt.radar.anatomy.indicators import InsufficientBars, true_ranges, volume_band, wilder_atr
from cobalt.radar.anatomy.leg import legs
from cobalt.radar.anatomy.registry import evaluability
from cobalt.radar.formation.atoms import ATOMS as SUPPORTED_ATOMS  # FINAL §2.5: the table formation dispatches through
from cobalt.radar.anatomy.structure import bar_break_trigger, structural_stop, tracked_extreme
from cobalt.session.clock import session_clock
from cobalt.taxonomy.loader import load_tunables
from cobalt.taxonomy.trade_def import TradeDef

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "radar"
ET_OPEN_UTC = datetime(2026, 1, 6, 14, 30, tzinfo=timezone.utc)  # 09:30 ET, EST


def _fixture_bars(ticker: str) -> list[Bar]:
    rows = json.loads((FIXTURES / "bars-rubberband.real-shape.json").read_text())
    return [
        Bar(
            ticker=r["ticker"], interval=Interval(r["interval"]),
            ts=datetime.fromisoformat(r["ts"]),
            open=Decimal(r["open"]), high=Decimal(r["high"]), low=Decimal(r["low"]),
            close=Decimal(r["close"]), volume=int(r["volume"]),
        )
        for r in rows if r["ticker"] == ticker
    ]


def _i1(ts: datetime, o, h, l, c, v=100, ticker="SYN") -> Bar:
    return Bar(ticker=ticker, interval=Interval.I1, ts=ts, open=Decimal(str(o)),
               high=Decimal(str(h)), low=Decimal(str(l)), close=Decimal(str(c)), volume=v)


def _wb(i: int, o, h, l, c, v=100, *, minutes=2, complete=True) -> WorkingBar:
    return WorkingBar(
        ts=ET_OPEN_UTC + timedelta(minutes=minutes * i), minutes=minutes,
        open=Decimal(str(o)), high=Decimal(str(h)), low=Decimal(str(l)), close=Decimal(str(c)),
        volume=v, complete=complete, minutes_present=minutes if complete else minutes - 1,
    )


# ---------------------------------------------------------------------
# Working-TF completeness (Astra R1-8)
# ---------------------------------------------------------------------


def test_first_minute_of_a_bucket_is_never_a_closed_working_bar():
    t = ET_OPEN_UTC
    series = working_bars([_i1(t, 10, 10.1, 9.9, 10)], 2, as_of=t + timedelta(minutes=1))
    assert series.bars == ()
    assert series.unclosed_bucket == t


def test_a_missing_second_minute_is_flagged_incomplete():
    t = ET_OPEN_UTC
    series = working_bars([_i1(t, 10, 10.1, 9.9, 10)], 2, as_of=t + timedelta(minutes=2))
    (bar,) = series.bars
    assert not bar.complete and bar.minutes_present == 1
    assert bar.missing_minutes == (t + timedelta(minutes=1),)


def test_complete_bucket_matches_the_archiver_aggregate_and_future_bars_are_ignored():
    t = ET_OPEN_UTC
    bars = [_i1(t, 10, 10.2, 9.9, 10.1, 5), _i1(t + timedelta(minutes=1), 10.1, 10.3, 10, 10.25, 7),
            _i1(t + timedelta(minutes=2), 10.25, 11, 10.2, 10.9, 9)]
    series = working_bars(bars, 2, as_of=t + timedelta(minutes=2, seconds=30))
    (bar,) = series.bars
    assert bar.complete and bar.volume == 12
    assert (bar.open, bar.high, bar.low, bar.close) == (Decimal("10"), Decimal("10.3"), Decimal("9.9"), Decimal("10.25"))
    assert series.unclosed_bucket is None  # the 3rd minute has not closed at as_of


def test_odd_scan_time_closes_only_whole_buckets():
    t = ET_OPEN_UTC
    bars = [_i1(t + timedelta(minutes=m), 10, 10, 10, 10) for m in range(5)]
    series = working_bars(bars, 2, as_of=t + timedelta(minutes=5, seconds=10))
    assert [b.ts for b in series.bars] == [t, t + timedelta(minutes=2)]
    assert all(b.complete for b in series.bars)
    assert series.unclosed_bucket == t + timedelta(minutes=4)


def test_rth_only_drops_premarket_buckets_at_the_session_boundary():
    clock = session_clock()
    t = ET_OPEN_UTC - timedelta(minutes=2)
    bars = [_i1(t + timedelta(minutes=m), 10, 10, 10, 10) for m in range(4)]
    series = working_bars(bars, 2, as_of=t + timedelta(minutes=4))
    assert [b.ts for b in rth_only(series, clock)] == [ET_OPEN_UTC]


@pytest.mark.parametrize("ticker", ["BGFI", "FTFT"])
def test_real_shape_buckets_flag_completeness_by_minutes_present(ticker):
    bars = _fixture_bars(ticker)
    as_of = max(b.ts for b in bars) + timedelta(minutes=1)
    series = working_bars(bars, 2, as_of=as_of)
    assert series.bars, "fixture produced no buckets"
    by_bucket: dict[datetime, set[datetime]] = {}
    for bar in bars:
        start = bar.ts - timedelta(minutes=bar.ts.minute % 2, seconds=bar.ts.second)
        by_bucket.setdefault(start, set()).add(bar.ts)
    for wb in series.bars:
        assert wb.minutes_present == len(by_bucket[wb.ts])
        assert wb.complete == (wb.minutes_present == 2)
        assert wb.ts + timedelta(minutes=2) <= as_of
    assert any(not wb.complete for wb in series.bars), "a thin real name has gaps"


def test_real_shape_replay_never_reads_a_bar_after_as_of():
    bars = _fixture_bars("FTFT")
    cut = sorted(b.ts for b in bars)[len(bars) // 2]
    series = working_bars(bars, 2, as_of=cut)
    assert all(b.ts + timedelta(minutes=2) <= cut for b in series.bars)
    assert sum(b.minutes_present for b in series.bars) <= sum(1 for b in bars if b.ts + timedelta(minutes=1) <= cut)


def test_mixed_tickers_or_non_i1_input_is_refused():
    t = ET_OPEN_UTC
    with pytest.raises(ValueError, match="one ticker"):
        working_bars([_i1(t, 1, 1, 1, 1), _i1(t, 1, 1, 1, 1, ticker="OTH")], 2, as_of=t + timedelta(hours=1))


# ---------------------------------------------------------------------
# ATR and volume band conventions (Astra R1-9)
# ---------------------------------------------------------------------


def _independent_wilder(bars, period):
    trs, prev = [], None
    for b in bars:
        h, l, c = float(b.high), float(b.low), float(b.close)
        trs.append(h - l if prev is None else max(h - l, abs(h - prev), abs(l - prev)))
        prev = c
    atr = sum(trs[:period]) / period
    for tr in trs[period:]:
        atr = (atr * (period - 1) + tr) / period
    return atr, trs


def test_wilder_atr_seed_warmup_and_independent_recompute():
    bars = [_wb(i, 10 + i * 0.1, 10.5 + i * 0.13, 9.8 + i * 0.07, 10.2 + i * 0.11) for i in range(30)]
    obs = wilder_atr(bars, 14)
    expected, trs = _independent_wilder(bars, 14)
    assert abs(float(obs.value) - expected) <= 1e-6
    assert [float(t) for t in true_ranges(bars)] == pytest.approx(trs, abs=1e-9)
    assert obs.method == "wilder" and obs.seed == "sma_first_period" and obs.bars_used == 30
    with pytest.raises(InsufficientBars):
        wilder_atr(bars[:13], 14)
    assert wilder_atr(bars[:14], 14).value == sum(true_ranges(bars[:14])) / 14


def test_volume_band_uses_prior_n_population_sigma():
    prior = [_wb(i, 10, 10, 10, 10, v) for i, v in enumerate([100, 120, 80, 100, 100])]
    band = volume_band(prior, 5, Decimal("2"))
    mean = sum([100, 120, 80, 100, 100]) / 5
    sigma = math.sqrt(sum((v - mean) ** 2 for v in [100, 120, 80, 100, 100]) / 5)
    assert float(band.mean) == pytest.approx(mean)
    assert float(band.sigma) == pytest.approx(sigma, abs=1e-9)
    assert float(band.threshold) == pytest.approx(mean + 2 * sigma, abs=1e-9)
    assert band.sigma_convention == "population" and band.n == 5
    with pytest.raises(InsufficientBars):
        volume_band(prior[:4], 5, Decimal("2"))


# ---------------------------------------------------------------------
# Leg (terminated by >=1 opposing bar; doji continues)
# ---------------------------------------------------------------------


def test_legs_terminate_on_one_opposing_bar_and_dojis_continue():
    bars = [_wb(0, 10, 10.2, 10, 10.1), _wb(1, 10.1, 10.1, 10.1, 10.1), _wb(2, 10.1, 10.4, 10.1, 10.3),
            _wb(3, 10.3, 10.3, 10.0, 10.05), _wb(4, 10.05, 10.5, 10.05, 10.4)]
    out = legs(bars)
    assert [(l.direction, l.bar_count, l.terminated) for l in out] == [
        ("up", 3, True), ("down", 1, True), ("up", 1, False),
    ]


def test_legs_mirror_for_a_down_run():
    up = [_wb(0, 10, 10.2, 10, 10.1), _wb(1, 10.1, 10.1, 9.9, 9.95), _wb(2, 9.95, 10.2, 9.95, 10.1)]
    down = [_wb(i, -b.open, -b.low, -b.high, -b.close) for i, b in enumerate(up)]
    flip = {"up": "down", "down": "up"}
    assert [(flip[l.direction], l.bar_count, l.terminated) for l in legs(down)] == [
        (l.direction, l.bar_count, l.terminated) for l in legs(up)
    ]


# ---------------------------------------------------------------------
# Extension — path A lands, path B-only is not evaluable (R4)
# ---------------------------------------------------------------------

PARAMS = ExtensionParams(volume_ma_bars=5, volume_sigma=Decimal("2"), path_b_atr=Decimal("1.25"))


TICK = Decimal("0.01")


def _step(i, o: Decimal, c: Decimal, v: int) -> WorkingBar:
    return _wb(i, o, max(o, c) + TICK, min(o, c) - TICK, c, v)


def _run(direction: str, climax: bool, *, n=20):
    sign = 1 if direction == "up" else -1
    bars = []
    price = Decimal("10")
    for i in range(n):
        c = price + sign * Decimal("0.05")
        bars.append(_step(i, price, c, 100 + (i % 3)))
        price = c
    if climax:
        bars.append(_step(n, price, price + sign * Decimal("0.60"), 5000))
    return bars


def _quiet(n=20):
    bars = []
    price = Decimal("10")
    for i in range(n):
        c = price + (Decimal("0.05") if i % 2 == 0 else Decimal("-0.05"))
        bars.append(_step(i, price, c, 100 + (i % 3)))
        price = c
    return bars


@pytest.mark.parametrize("direction", ["up", "down"])
def test_path_a_climax_bar_is_culminating_in_both_directions(direction):
    obs = detect_extension(_run(direction, True), PARAMS)
    assert obs.instantiated is True and obs.state == "culminating" and obs.path == "A"
    assert obs.direction == direction
    assert obs.culminating_bar_ts == ET_OPEN_UTC + timedelta(minutes=40)
    assert obs.band is not None and obs.culminating_volume >= obs.band.threshold
    assert obs.leg_count == 1


def test_high_volume_but_not_the_widest_body_is_not_path_a():
    bars = _run("up", False)
    bars[3] = _wb(3, bars[3].open, bars[3].open + Decimal("0.9"), bars[3].open, bars[3].open + Decimal("0.8"), 100)
    last = bars[-1]
    bars.append(_wb(20, last.close, last.close + Decimal("0.3"), last.close, last.close + Decimal("0.2"), 9000))
    obs = detect_extension(bars, PARAMS)
    assert obs.path != "A"


def test_path_b_only_formation_is_not_evaluable():
    bars = []
    price = Decimal("10")
    for i in range(20):
        bars.append(_step(i, price, price + Decimal("0.29"), 100))
        price += Decimal("0.29")
    obs = detect_extension(bars, PARAMS)
    assert obs.path == "B_only"
    assert obs.instantiated is None and obs.state is None
    assert obs.unavailable == "catalyst_ref_unknown"
    assert obs.distance_from_open_atr >= PARAMS.path_b_atr


def test_quiet_run_is_not_instantiated():
    obs = detect_extension(_quiet(), PARAMS)
    assert obs.instantiated is False and obs.state == "none" and obs.unavailable is None
    assert obs.distance_from_open_atr < PARAMS.path_b_atr


def test_warm_up_and_incomplete_buckets_make_extension_unavailable():
    assert detect_extension(_run("up", False, n=4), PARAMS).unavailable == "insufficient_bars"
    bars = _run("up", True)
    bars[2] = bars[2].model_copy(update={"complete": False, "minutes_present": 1})
    assert detect_extension(bars, PARAMS).unavailable == "incomplete_bucket"


def test_extension_params_come_from_tunables_rows():
    params = ExtensionParams.from_tunables(load_tunables().by_key)
    assert params.path_b_atr == Decimal("1.25")
    assert params.volume_ma_bars == 20 and params.volume_sigma == Decimal("2")


def test_new_definition_tunables_are_replay_pending_dwv():
    rows = load_tunables().by_key
    for key in ("extension.path_a_volume_ma_bars", "extension.leg_base", "range_break.htf_range"):
        assert rows[key].status.value == "replay_pending", key
        assert rows[key].source.value == "dwv", key
    assert rows["extension.leg_base"].value == "session_open"
    assert rows["range_break.htf_range"].value == "prior_session_high_low"


# ---------------------------------------------------------------------
# Structure: tracked extreme, bar_break trigger, structural stop + nudge
# ---------------------------------------------------------------------


def test_tracked_extreme_is_the_run_high_for_up_and_low_for_down():
    up = _run("up", True)
    ext = tracked_extreme(up, "up")
    assert ext.side == "high" and ext.price == max(b.high for b in up)
    down = _run("down", True)
    assert tracked_extreme(down, "down").price == min(b.low for b in down)


def test_bar_break_trigger_clears_both_of_the_last_n_completed_bars():
    bars = [_wb(0, 10, 10.5, 9.8, 10.2), _wb(1, 10.2, 10.4, 9.9, 10.0), _wb(2, 10.0, 10.3, 9.7, 9.9)]
    short = bar_break_trigger(bars, 2, "short")
    assert short.price == Decimal("9.7") and short.bar_ts == (bars[1].ts, bars[2].ts)
    long = bar_break_trigger(bars, 2, "long")
    assert long.price == Decimal("10.4")
    with pytest.raises(InsufficientBars):
        bar_break_trigger(bars[:1], 2, "long")
    bars[2] = bars[2].model_copy(update={"complete": False, "minutes_present": 1})
    with pytest.raises(IncompleteBucket):
        bar_break_trigger(bars, 2, "short")


@pytest.mark.parametrize(
    "extreme,direction,expected",
    [
        ("10.13", "short", "10.15"),   # 10.15 is not x.x0
        ("10.18", "short", "10.19"),   # 10.20 is x.x0 -> check-and-move 1c toward structure
        ("10.13", "long", "10.11"),
        ("10.02", "long", "10.01"),    # 10.00 round dollar -> 10.01
        ("3.9381", "short", "3.96"),   # sub-cent extreme: ceil to cent beyond, then check
        ("3.9381", "long", "3.91"),
    ],
)
def test_structural_stop_buffer_and_nudge(extreme, direction, expected):
    stop = structural_stop(Decimal(extreme), direction, Decimal("0.02"))
    assert stop.price == Decimal(expected)
    beyond = stop.price - Decimal(extreme) if direction == "short" else Decimal(extreme) - stop.price
    assert Decimal("0.01") <= beyond <= Decimal("0.03")
    assert stop.price * 100 % 10 != 0


# ---------------------------------------------------------------------
# Daily refs: prior session, daily ATR, htf_level_proximity, day_count
# ---------------------------------------------------------------------


def _fixture_daily(ticker: str) -> DailySeries:
    with (FIXTURES / "daily-bars.real-shape.csv").open() as f:
        rows = [r for r in csv.DictReader(f) if r["Ticker"] == ticker]
    return DailySeries(
        ticker=ticker,
        bars=tuple(
            DailyBar(session_date=date.fromisoformat(r["Date"]), open=Decimal(r["Open"]),
                     high=Decimal(r["High"]), low=Decimal(r["Low"]), close=Decimal(r["Close"]),
                     volume=int(Decimal(r["Volume"])))
            for r in rows
        ),
    )


def test_parse_daily_export_shape_and_refusals():
    series = _fixture_daily("FTFT")
    text = "Date,Open,High,Low,Close,Volume\n" + "".join(
        f"{b.session_date:%m/%d/%Y},{b.open},{b.high},{b.low},{b.close},{b.volume}\n" for b in series.bars
    )
    parsed = parse_daily_csv(text, "FTFT")
    assert parsed == series.bars
    with pytest.raises(ValueError, match="columns"):
        parse_daily_csv("Date,Open\n01/02/2026,1\n", "FTFT")
    with pytest.raises(ValueError, match="time-of-day"):
        parse_daily_csv("Date,Open,High,Low,Close,Volume\n01/02/2026 09:30 AM,1,1,1,1,1\n", "FTFT")
    with pytest.raises(ValueError, match="no data rows"):
        parse_daily_csv("Date,Open,High,Low,Close,Volume\n", "FTFT")


def test_prior_session_never_reads_trade_date_or_later():
    series = _fixture_daily("BGFI")
    last = series.bars[-1].session_date
    prior = prior_session(series, last)
    assert prior.session_date < last
    assert prior.session_date == series.bars[-2].session_date
    with pytest.raises(NoDailyBars):
        prior_session(series, series.bars[0].session_date)


def test_daily_atr_on_real_shape_rows_matches_independent_recompute():
    series = _fixture_daily("FTFT")
    trade_date = series.bars[-1].session_date
    obs = daily_atr(series, trade_date)
    expected, _ = _independent_wilder(list(series.bars[:-1]), 14)
    assert abs(float(obs.value) - expected) <= 1e-6
    assert obs.last_bar_ts is None and obs.last_session_date == series.bars[-2].session_date


def test_htf_level_proximity_nearest_prior_level_in_daily_atr_units_symmetric():
    series = _fixture_daily("FTFT")
    trade_date = series.bars[-1].session_date
    prior = prior_session(series, trade_date)
    atr = daily_atr(series, trade_date).value
    near_high = htf_level_proximity(series, trade_date, prior.high + atr / 4)
    assert near_high.reference == "prior_high"
    assert abs(near_high.value - Decimal("0.25")) <= Decimal("1e-6")
    near_low = htf_level_proximity(series, trade_date, prior.low - atr / 4)
    assert near_low.reference == "prior_low"
    assert abs(near_low.value - Decimal("0.25")) <= Decimal("1e-6")
    assert near_high.units == "daily_atr"


def _days(highs_lows):
    start = date(2026, 1, 5)
    return DailySeries(ticker="SYN", bars=tuple(
        DailyBar(session_date=start + timedelta(days=i), open=Decimal("10"), high=Decimal(str(h)),
                 low=Decimal(str(l)), close=Decimal("10"), volume=1)
        for i, (h, l) in enumerate(highs_lows)
    ))


def test_htf_day_count_continuity_up_and_down():
    series = _days([(10, 9), (11, 9.5), (12, 10)])
    trade_date = date(2026, 1, 8)
    up = htf_range_break(series, trade_date, session_high=Decimal("12.5"), session_low=Decimal("11"))
    assert up.direction == "up" and up.day_count == 3
    first = htf_range_break(_days([(10, 9), (10.5, 9.1), (10, 9.5)]), trade_date,
                            session_high=Decimal("10.2"), session_low=Decimal("9.6"))
    assert first.direction == "up" and first.day_count == 1
    down = htf_range_break(_days([(10, 9), (9.5, 8), (9, 7)]), trade_date,
                           session_high=Decimal("8"), session_low=Decimal("6.5"))
    assert down.direction == "down" and down.day_count == 3
    inside = htf_range_break(series, trade_date, session_high=Decimal("11.5"), session_low=Decimal("10.5"))
    assert inside.direction is None and inside.day_count is None and not inside.outside_day
    outside = htf_range_break(series, trade_date, session_high=Decimal("13"), session_low=Decimal("9"))
    assert outside.outside_day and outside.day_count is None


# ---------------------------------------------------------------------
# Registry: which defs are evaluable (R2)
# ---------------------------------------------------------------------


def _def_with(preconditions, avoid, trigger, stop_ref="snapback_candle"):
    from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH  # noqa: F401 — shape reference only
    import yaml

    text = EXAMPLE_NOTE_PATH.read_text()
    fence = text.split("```yaml\n", 1)[1].split("\n```", 1)[0]
    mapping = yaml.safe_load(fence)["trade_def"]
    mapping["preconditions"] = preconditions
    mapping["avoid"] = avoid
    mapping["trigger"] = trigger
    mapping["stop"]["placement"]["ref"] = stop_ref
    return TradeDef.from_unit(mapping, slug="anatomy-probe", name="Anatomy Probe")


BAR_BREAK = {"type": "bar_break", "params": {"bars_cleared": 2, "direction": "any"},
             "confirmation_policy": {"type": "intrabar"}}


def test_extension_reversal_shape_is_evaluable():
    td = _def_with(
        [{"expr": "Extension.state == culminating"}],
        [{"expr": "NOT Extension.instantiated"}, {"expr": "RangeBreak(HTF).day_count == 1"},
         {"text": "human-only context read"}],
        BAR_BREAK,
    )
    result = evaluability(td)
    assert result.evaluable and result.missing_atoms == ()
    assert result.human_predicates == 1


def test_unsupported_atoms_trigger_and_stop_are_named_missing():
    td = _def_with(
        [{"expr": "Range(micro).instantiated"}, {"expr": "Leg(pullback) touched VWAP"}],
        [],
        {"type": "range_break", "params": {"ref": "Range(micro).bound"}, "confirmation_policy": {"type": "intrabar"}},
        stop_ref="range_base",
    )
    result = evaluability(td)
    # `VWAP` is served from STEP-3 of the setups one build (FINAL §3 D1);
    # `Range(micro).instantiated`, `range_break` and `range_base` from STEP-4
    # (§3 D2, §2.2, §2.3); `Leg(pullback)` / `touched` from STEP-6 (§3 D3).
    assert result.evaluable and result.missing_atoms == ()
    # The naming itself, on an object the FINAL does not build (§3 "Not built: Gap"):
    gap = _def_with([{"expr": "Range(micro).instantiated"}, {"expr": "Gap.size > 0"}], [],
                    {"type": "sequence", "steps": [{"name": "break", "predicate": {"expr": "Gap.size > 0"},
                                                    "confirmation_policy": {"type": "intrabar"}}]},
                    stop_ref="turn_candle")
    assert set(evaluability(gap).missing_atoms) == {"Gap.size", "trigger:sequence",
                                                    "stop:structural_extreme:turn_candle"}


def test_sequence_trigger_is_named_missing_not_a_crash():
    step = {"name": "break", "predicate": {"expr": "Extension.state == culminating"},
            "confirmation_policy": {"type": "intrabar"}}
    td = _def_with([{"expr": "Extension.state == culminating"}], [],
                   {"type": "sequence", "steps": [step]})
    result = evaluability(td)
    assert not result.evaluable and result.missing_atoms == ("trigger:sequence",)


def test_shipped_synthetic_def_reports_not_evaluable_with_its_missing_atoms():
    from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH
    import yaml

    text = EXAMPLE_NOTE_PATH.read_text()
    mapping = yaml.safe_load(text.split("```yaml\n", 1)[1].split("\n```", 1)[0])["trade_def"]
    result = evaluability(TradeDef.from_unit(mapping, slug="shipped-example", name="Shipped Example"))
    assert not result.evaluable
    assert result.missing_atoms and all(a not in SUPPORTED_ATOMS for a in result.missing_atoms)


def test_supported_atoms_are_exactly_the_s2_detectors():
    # + the D1 atoms of the setups one build STEP-3 (FINAL §3 D1)
    assert frozenset(SUPPORTED_ATOMS) == frozenset(
        {"Extension.state", "Extension.instantiated", "Extension.leg_count", "RangeBreak(HTF).day_count",
         "price", "EMA9", "EMA21", "EMA9.slope", "slope_norm(EMA9)", "slope_norm(VWAP)", "VWAP",
         "ATR(working_tf)", "DayRange.high", "DayRange.low", "DayRange.upper_third", "PMH", "PML", "PDH", "PDL",
         "InPlay.state",
         # + the D2 / D3 atoms of STEP-4 (FINAL §3 D2, D3)
         "Range(micro).instantiated", "Range(micro).duration", "Range(micro).low", "Range(micro).top",
         "Range(micro).base", "Range(micro).bound", "Range(micro).height", "Range(micro).wick_ratio",
         "Leg(opening_drive).direction", "Leg(opening_drive).terminated_by",
         # + STEP-6's roles and the A-13 catalyst resolver (FINAL §3 D3, §6)
         "Leg(pullback).direction", "Leg(pullback).end", "Leg(pullback).index", "Leg(impulse).direction",
         "Leg(opening_drive OR impulse).direction", "catalyst_ref",
         # + STEP-7's rejected-resistance atom (FINAL §3 D5/D6)
         "Level_ref(resistance).rejected"}
    )
