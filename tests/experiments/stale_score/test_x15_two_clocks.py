"""X15 (v2 §7, before S1; R39 TWO CLOCKS): a pure clock fixture, not a
product change. The R36 stamp (the poller's `poll_failures`, bar OPEN vs
`max_age_s`, RTH only) and the score's clock (`intraday_staleness`, bar
CLOSE vs 2 × scan_interval, every session) disagree in both directions, as
R39 accepts. Both limits are this module's constructions (L32, L69)."""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone

from cobalt.radar.anatomy.freshness import intraday_staleness
from cobalt.radar.poller import BarPoller, PollMember
from cobalt.session.models import Session

SCAN = 100          # this module's scan interval, seconds
MAX_AGE = 180       # this module's poller max age, seconds (a construction)
NOW = datetime(2026, 1, 6, 16, 0, tzinfo=timezone.utc)


class _Bucket:
    async def acquire(self):
        return None


class _Store:
    def __init__(self, mark):
        self.mark = mark

    def watermark(self, ticker, interval):
        return self.mark

    def upsert_bars(self, bars, *, before_commit=None):
        return len(bars)


def _stamp(open_ts: datetime, session: Session) -> bool:
    async def fetch(*_a):
        return []
    poller = BarPoller("synthetic", store=_Store(open_ts), bucket=_Bucket(), overlap_bars=0, max_age_s=MAX_AGE,
                       fetch=fetch)
    result = asyncio.run(poller.poll([PollMember("AAA", 1)], now=NOW, session=session))
    return any(f.reason == "stale" for f in result.failures)


def _score_stale(open_ts: datetime) -> bool:
    return intraday_staleness(observed_at=open_ts + timedelta(minutes=1), as_of=NOW, scan_interval=SCAN).stale


def test_x15_the_two_clocks_disagree_both_ways():
    # (1) RTH, open-age just past the poller's limit, close-age inside 2 × SCAN
    open1 = NOW - timedelta(seconds=MAX_AGE + 30)
    # (2) not RTH, close-age past 2 × SCAN
    open2 = NOW - timedelta(minutes=1) - timedelta(seconds=2 * SCAN + 1)
    rth = (_stamp(open1, Session.RTH), _score_stale(open1))
    pre = (_stamp(open2, Session.PREMARKET), _score_stale(open2))
    print(f"X15: scan={SCAN} max_age={MAX_AGE} rth_open_age={MAX_AGE + 30} rth(stamp,score_stale)={rth} "
          f"premarket_close_age={2 * SCAN + 1} premarket(stamp,score_stale)={pre}")
    assert rth == (True, False) and pre == (False, True)
