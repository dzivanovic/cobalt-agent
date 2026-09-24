"""X7 and X18, their stored-session halves (FINAL `## First-gate experiments`).

- X7: "count of scans where BOTH frames satisfy the newly unlocked def, on
  the last 10 stored sessions" — per corpus shape. A `both_sides` scan
  where either frame alone would have formed is a FAIL.
- X18: `atrs_from_open` and `Extension.leg_count` on the real bars and on
  the mirrored frame. `htf_level_proximity` needs the daily series, which
  this worktree does not have (`configs/cobalt/radar.yaml` `cache.dir` is
  cwd-relative) → that leg is UNPROVEN here and runs at the deploy.

Counts and ratios only — no ticker, no date (L32); nothing about his trades
(R24). A 30-minute scan grid over RTH keeps the run bounded; the grid is
printed.
"""

from __future__ import annotations

import os
from datetime import datetime, time, timedelta
from zoneinfo import ZoneInfo

import pytest

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: needs cobalt_dev",
)
ET = ZoneInfo("America/New_York")
GRID_MIN = 30


def _sessions_and_bars(conn, limit=10):
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


@requires_db
def test_x7_and_x18_on_the_stored_sessions(tmp_path):
    import radar_p2_support as sup
    import setups_shapes as shapes
    from cobalt import db
    from cobalt.radar.anatomy.bars import rth_only, working_bars
    from cobalt.radar.anatomy.extension import ExtensionParams, detect_extension
    from cobalt.radar.anatomy.frame import mirror_bars
    from cobalt.radar.evaluate import MemberInput, evaluate_member, working_minutes
    from cobalt.session import session_clock

    clock = session_clock()
    params = ExtensionParams.from_tunables(sup.engine_tunables())
    defs = {key: shapes.load_shape(tmp_path / key, shape) for key, shape in {**shapes.SHAPES, **shapes.VARIANTS}.items()}
    tunables = {key: shapes.tunables_for(ld) for key, ld in defs.items()}
    x7 = {key: {"scans": 0, "both_sides": 0, "formed": 0} for key in defs}
    x18 = {"scans": 0, "atrs_from_open_diff": 0, "leg_count_diff": 0}
    sessions = 0
    with db.connect("cobalt_dev", side=db.Side.SYSTEM) as conn:
        for day, by_ticker in _sessions_and_bars(conn):
            sessions += 1
            for ticker, bars in by_ticker.items():
                t = datetime.combine(day, time(10, 0), ET)
                while t.time() <= time(15, 30):
                    at = t.astimezone(ZoneInfo("UTC"))
                    member = MemberInput(membership_id=1, ticker=ticker, trade_date=day, as_of=at, bars=tuple(bars),
                                         daily=None, daily_status="absent")
                    for key, ld in defs.items():
                        # STEP-4: each shape with its own merged rows (the constructed
                        # fills + its note's per-trade rows); rubberband's are the engine's.
                        ev = evaluate_member(ld, member, tunables=tunables[key], defaults=sup.defaults(),
                                             scan_interval=100, clock=clock)
                        x7[key]["scans"] += 1
                        x7[key]["formed"] += ev.evaluation == "formed"
                        x7[key]["both_sides"] += (ev.by_side["long"].evaluation == ev.by_side["short"].evaluation
                                                  == "formed")
                    closed = [b for b in bars if b.ts + timedelta(minutes=1) <= at]
                    run = tuple(rth_only(working_bars(closed, working_minutes(sup.defaults()), as_of=at), clock))
                    real, mirr = detect_extension(run, params), detect_extension(mirror_bars(run), params)
                    x18["scans"] += 1
                    x18["atrs_from_open_diff"] += real.distance_from_open_atr != mirr.distance_from_open_atr
                    x18["leg_count_diff"] += real.leg_count != mirr.leg_count
                    t += timedelta(minutes=GRID_MIN)
    print(f"X7 stored: sessions={sessions} grid={GRID_MIN}min {x7}")
    print(f"X18 stored: sessions={sessions} {x18} htf_level_proximity=UNPROVEN (daily leg)")
    assert all(v["both_sides"] == 0 for v in x7.values())
    assert x18["atrs_from_open_diff"] == 0 and x18["leg_count_diff"] == 0
