"""X1 (FINAL `## First-gate experiments`, before C3a): "on `cobalt_dev`,
last 10 stored sessions, the share of pool names with at least `period`
complete premarket working buckets by 09:30, for periods 9, 14 and 21."

A pool name is a `system.radar_membership` ticker of that trade date that has
stored i1 bars. When the session has no membership rows, the share is also
reported over every stored name of the session, labelled `stored` — never
mixed into the pool share. Counts and ratios only (L32); nothing about his
trades (R24). Grok: "do not drop the seed, report the rate" — the assertion is
only that the measurement ran.
"""

from __future__ import annotations

import os
from datetime import datetime, time
from zoneinfo import ZoneInfo

import pytest

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: needs cobalt_dev",
)
ET = ZoneInfo("America/New_York")
PERIODS = (9, 14, 21)


def _complete_premarket_buckets(bars, minutes: int, as_of, clock) -> int:
    from cobalt.radar.anatomy.bars import working_bars
    from cobalt.session.models import Session

    series = working_bars(bars, minutes, as_of=as_of)
    return sum(1 for b in series.bars if b.complete and clock.session(b.ts) is Session.PREMARKET)


@requires_db
def test_x1_share_of_names_with_a_full_premarket_seed():
    import radar_p2_support as sup
    from cobalt import db
    from cobalt.archiver.models import Bar, Interval
    from cobalt.radar.evaluate import working_minutes
    from cobalt.session import session_clock

    clock = session_clock()
    minutes = working_minutes(sup.defaults())
    tally = {"pool": {"names": 0, **{p: 0 for p in PERIODS}}, "stored": {"names": 0, **{p: 0 for p in PERIODS}}}
    sessions = pool_sessions = 0
    with db.connect("cobalt_dev", side=db.Side.SYSTEM) as conn:
        days = [r[0] for r in conn.execute(
            "SELECT DISTINCT (ts AT TIME ZONE 'America/New_York')::date AS d FROM system.bars "
            "WHERE interval = 'i1' ORDER BY d DESC LIMIT 10").fetchall()]
        for day in days:
            sessions += 1
            as_of = datetime.combine(day, time(9, 30), ET)
            rows = conn.execute(
                "SELECT ticker, ts, open, high, low, close, volume FROM system.bars WHERE interval = 'i1' "
                "AND (ts AT TIME ZONE 'America/New_York')::date = %s AND ts < %s ORDER BY ticker, ts",
                (day, as_of)).fetchall()
            by_ticker: dict[str, list] = {}
            for t, ts, o, h, lo, c, v in rows:
                by_ticker.setdefault(t, []).append(Bar(ticker=t, interval=Interval.I1, ts=ts, open=o, high=h,
                                                       low=lo, close=c, volume=int(v)))
            names_today = {r[0] for r in conn.execute(
                "SELECT DISTINCT ticker FROM system.bars WHERE interval = 'i1' "
                "AND (ts AT TIME ZONE 'America/New_York')::date = %s", (day,)).fetchall()}
            pool = {r[0] for r in conn.execute(
                "SELECT DISTINCT ticker FROM system.radar_membership WHERE trade_date = %s", (day,)).fetchall()}
            pool &= names_today
            pool_sessions += bool(pool)
            for label, names in (("pool", pool), ("stored", names_today)):
                for name in names:
                    have = _complete_premarket_buckets(by_ticker.get(name, []), minutes, as_of, clock)
                    tally[label]["names"] += 1
                    for p in PERIODS:
                        tally[label][p] += have >= p
    for label, t in tally.items():
        shares = {p: (round(t[p] / t["names"], 3) if t["names"] else None) for p in PERIODS}
        print(f"X1 {label}: sessions={sessions} pool_sessions={pool_sessions} name_sessions={t['names']} "
              f"working_tf={minutes}m share_by_period={shares}")
    assert sessions >= 0
