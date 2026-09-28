"""X5b (v2 §7, before S1): a member whose stored bars are ALL from the prior
session — is `last_bar` None (settles the word "today")? Either answer, C
still nulls: None → X5a's path; not None → the old close, stale."""

from __future__ import annotations

from datetime import date, datetime, timezone

import radar_p2_support as sup
from cobalt.radar.anatomy.freshness import RvolObservation
from cobalt.radar.evaluate import MemberInput

from stale_support import evaluate

UTC = timezone.utc
#: The next trading day after the fixture's session (a construction).
NEXT_DAY = date(2026, 1, 7)
NEXT_AS_OF = datetime(2026, 1, 7, 14, 40, tzinfo=UTC)


def test_x5b_prior_session_bars_leave_no_last_bar_today():
    bars = tuple(sup.fixture_bars("FTFT"))
    m = MemberInput(
        membership_id=100, ticker="FTFT", trade_date=NEXT_DAY, as_of=NEXT_AS_OF, bars=bars,
        daily=sup.fixture_daily("FTFT", NEXT_AS_OF), daily_status="cache-hit",
        rvol=RvolObservation(ticker="FTFT", value=4.2, observed_at=NEXT_AS_OF, source="screen:s",
                             candidates=("screen:s",)),
    )
    ev = evaluate(m)
    prior = sum(1 for b in bars if b.ts.date() < NEXT_DAY)
    print(f"X5b: bars={len(bars)} prior_session_bars={prior} last_price={ev.last_price} "
          f"last_bar_ts={ev.last_bar_ts} consumed={len(ev.consumed_bars)} evaluation={ev.evaluation}")
    assert prior == len(bars)
    assert ev.last_price is None and ev.last_bar_ts is None and ev.evaluation == "input_stale"
