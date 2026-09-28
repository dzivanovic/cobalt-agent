"""X13 and X15 (FINAL `## First-gate experiments`, before C3b), run on the
STEP-4 pure detectors BEFORE they are wired into the stage.

- X13: "on stored sessions, the ratio `atr_seeded` / RTH-only ATR at 09:40,
  09:50 and 10:00, and the count of Range(micro) instantiations inside the
  `open_drive` sub-window (taxonomy `:79`) under each." ATR(14) on the RTH run
  alone has NO value before ~09:58 (E7), so beside the ratio to it (counted
  where it exists) the ratio to the RTH-only mean true range of the bars there
  are is reported, labelled `rth_tr_mean` — the RTH-weighted quantity the
  experiment's fail line names.
- X15: "evaluate hitchhiker on stored drive-then-range days under both
  readings" — at the DETECTOR level (the stage cannot read these atoms yet):
  the drive-then-range preconditions (opening drive ended by consolidation,
  instantiated micro-Range, duration in a band, low in the day's upper third)
  on a 10-minute grid 09:40–11:30, under `A-07` and under the literal reading.
  Pool admission is not read (`cobalt_dev` has no membership rows, X1).

Constructed params only (`setups_shapes.D2_CONSTRUCTED`, the band 5–30 min —
L69). Counts and ratios only (L32); nothing about his trades (R24).
"""

from __future__ import annotations

import os
import statistics
from datetime import datetime, time, timedelta
from decimal import Decimal
from zoneinfo import ZoneInfo

import pytest

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: needs cobalt_dev",
)
ET = ZoneInfo("America/New_York")
BAND = (Decimal(5), Decimal(30))


def _sessions(conn, limit=10):
    from cobalt.archiver.models import Bar, Interval

    days = [r[0] for r in conn.execute(
        "SELECT DISTINCT (ts AT TIME ZONE 'America/New_York')::date AS d FROM system.bars "
        "WHERE interval = 'i1' ORDER BY d DESC LIMIT %s", (limit,)).fetchall()]
    for day in days:
        rows = conn.execute(
            "SELECT ticker, ts, open, high, low, close, volume FROM system.bars WHERE interval = 'i1' "
            "AND (ts AT TIME ZONE 'America/New_York')::date = %s ORDER BY ticker, ts", (day,)).fetchall()
        by_ticker: dict[str, list] = {}
        for t, ts, o, h, lo, c, v in rows:
            by_ticker.setdefault(t, []).append(Bar(ticker=t, interval=Interval.I1, ts=ts, open=o, high=h, low=lo,
                                                   close=c, volume=int(v)))
        yield day, by_ticker


def _series(bars, at, clock):
    from cobalt.radar.anatomy.bars import rth_only, working_bars
    from cobalt.radar.anatomy.frame import premarket_buckets

    closed = [b for b in bars if b.ts + timedelta(minutes=1) <= at]
    series = working_bars(closed, 2, as_of=at)
    return premarket_buckets(series.bars, clock), tuple(rth_only(series, clock))


def _params():
    import setups_shapes as shapes
    from cobalt.radar.anatomy.micro_range import MicroRangeParams

    c = shapes.D2_CONSTRUCTED
    return MicroRangeParams(touches_per_side=2, touch_tolerance_atr=Decimal(c["range.micro.touch_tolerance_atr"][1]),
                            bound_flat_slope_atr=Decimal(c["range.micro.bound_flat_slope_atr"][1]))


@requires_db
def test_x13_seeded_atr_ratio_and_open_drive_ranges():
    from cobalt import db
    from cobalt.radar.anatomy.indicators import ATR_PERIOD, seeded, true_ranges, wilder_atr
    from cobalt.radar.anatomy.micro_range import detect_micro_range
    from cobalt.session import session_clock

    clock, params = session_clock(), _params()
    ratio_atr14 = {t: [] for t in ("09:40", "09:50", "10:00")}
    ratio_trmean = {t: [] for t in ratio_atr14}
    ranges = {"seeded": 0, "rth_tr_mean": 0}
    names = 0
    with db.connect("cobalt_dev", side=db.Side.SYSTEM) as conn:
        for day, by_ticker in _sessions(conn):
            for bars in by_ticker.values():
                names += 1
                for label in ratio_atr14:
                    h, m = map(int, label.split(":"))
                    at = datetime.combine(day, time(h, m), ET)
                    pre, run = _series(bars, at, clock)
                    s = seeded(wilder_atr, pre, run, ATR_PERIOD).value
                    if s is None or not run:
                        continue
                    if len(run) >= ATR_PERIOD:
                        ratio_atr14[label].append(float(s / wilder_atr(run).value))
                    trs = true_ranges(run)
                    mean = sum(trs, Decimal(0)) / len(trs)
                    if mean > 0:
                        ratio_trmean[label].append(float(s / mean))
                    if label == "10:00":
                        for kind, atr in (("seeded", s), ("rth_tr_mean", mean if mean > 0 else None)):
                            r = detect_micro_range(run, params, atr=atr).range
                            ranges[kind] += r is not None and r.instantiated_ts < at
    med = {k: (round(statistics.median(v), 3) if v else None, len(v)) for k, v in ratio_trmean.items()}
    med14 = {k: (round(statistics.median(v), 3) if v else None, len(v)) for k, v in ratio_atr14.items()}
    print(f"X13: name_sessions={names} median(atr_seeded/rth_tr_mean, n)={med} "
          f"median(atr_seeded/rth_atr14, n)={med14} open_drive_ranges_by_10:00={ranges}")
    assert names >= 0


@requires_db
def test_x15_drive_then_range_under_both_readings():
    from cobalt import db
    from cobalt.radar.anatomy.indicators import ATR_PERIOD, seeded, wilder_atr
    from cobalt.radar.anatomy.frame import mirror_bars
    from cobalt.radar.anatomy.leg import legs
    from cobalt.radar.anatomy.leg_roles import opening_drive, opening_drive_literal
    from cobalt.radar.anatomy.micro_range import detect_micro_range
    from cobalt.radar.anatomy.session_levels import day_range
    import setups_shapes as shapes

    clock, params = session_clock_(), _params()
    retrace = Decimal(shapes.D2_CONSTRUCTED["leg.consolidation_max_retrace"][1])
    counts = {"name_sessions": 0, "drive_then_range": 0, "forms_a07": 0, "forms_literal": 0}
    with db.connect("cobalt_dev", side=db.Side.SYSTEM) as conn:
        for day, by_ticker in _sessions(conn):
            for bars in by_ticker.values():
                counts["name_sessions"] += 1
                seen = {"drive_then_range": False, "forms_a07": False, "forms_literal": False}
                at = datetime.combine(day, time(9, 40), ET)
                while at.time() <= time(11, 30):
                    pre, real = _series(bars, at, clock)
                    atr = seeded(wilder_atr, pre, real, ATR_PERIOD).value
                    for run in (real, mirror_bars(real)):  # both frames (F-04)
                        r = detect_micro_range(run, params, atr=atr).range if run else None
                        if r is None:
                            continue
                        lg = legs(run)
                        a07 = opening_drive(run, lg, r, max_retrace=retrace).terminated_by
                        lit = opening_drive_literal(run, lg, r).terminated_by
                        seen["drive_then_range"] |= a07 == "consolidation" or lit == "consolidation"
                        dr = day_range(run)
                        shape_ok = BAND[0] <= r.duration_min <= BAND[1] and r.base >= dr.upper_third
                        seen["forms_a07"] |= shape_ok and a07 == "consolidation"
                        seen["forms_literal"] |= shape_ok and lit == "consolidation"
                    at += timedelta(minutes=10)
                for k, v in seen.items():
                    counts[k] += v
    print(f"X15 (detector level, both frames): {counts}")
    assert counts["name_sessions"] >= 0


def session_clock_():
    from cobalt.session import session_clock

    return session_clock()
