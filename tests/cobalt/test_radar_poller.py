"""Poll overlap, closed-bar, freshness, and gate propagation tests."""

import asyncio
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.radar.poller import BarPoller, PollFailure, PollMember
from cobalt.radar.runner import StageDropped
from cobalt.session.models import Session

NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def _bar(minutes):
    return Bar(ticker="AAA", interval=Interval.I1, ts=NOW + timedelta(minutes=minutes), open=Decimal(1), high=Decimal(1), low=Decimal(1), close=Decimal(1), volume=1)


class Bucket:
    async def acquire(self):
        return None


class Store:
    def __init__(self, watermark=None):
        self.mark = watermark
        self.seen = []

    def watermark(self, ticker, interval):
        assert (ticker, interval) == ("AAA", "i1")
        return self.mark

    def upsert_bars(self, bars, *, before_commit=None):
        self.seen = bars
        if before_commit:
            before_commit()
        return len(bars)


def _poller(store, bars):
    async def fetch(*_args):
        return bars
    return BarPoller("synthetic", store=store, bucket=Bucket(), overlap_bars=2, max_age_s=180, fetch=fetch)


def test_overlap_reupserts_closed_bars_and_excludes_open_bar():
    store = Store(NOW - timedelta(minutes=1))
    result = asyncio.run(_poller(store, [_bar(-4), _bar(-2), _bar(-1), _bar(0)]).poll([PollMember("AAA", 1)], now=NOW, session=Session.RTH))
    assert [x.ts for x in store.seen] == [NOW - timedelta(minutes=2), NOW - timedelta(minutes=1)]
    assert result.written == {"AAA": 2}


def test_stale_onset_recovery_and_no_stale_outside_rth():
    old = NOW - timedelta(minutes=10)
    store = Store(old)
    first = asyncio.run(_poller(store, []).poll([PollMember("AAA", 1)], now=NOW, session=Session.RTH))
    assert first.failures[0].reason == "stale"
    store.mark = NOW - timedelta(minutes=1)
    recovered = asyncio.run(_poller(store, []).poll([PollMember("AAA", 1)], now=NOW, session=Session.RTH, existing_failures=first.failures))
    assert recovered.failures == []
    outside = asyncio.run(_poller(Store(old), []).poll([PollMember("AAA", 1)], now=NOW, session=Session.PREMARKET))
    assert outside.failures == []


SINCE = datetime(2026, 9, 14, 13, 38, 7, 287155, tzinfo=timezone.utc)


def test_carried_record_for_a_non_member_is_dropped_and_logged_once():
    # cto-2026-09-15 §1.2: IMCC left the pool on 09-14 and its stale record
    # was carried forever, because only a fetch of IMCC could pop it.
    from loguru import logger

    lines = []
    sink = logger.add(lambda message: lines.append(message.record["message"]), level="INFO")
    try:
        result = asyncio.run(_poller(Store(NOW - timedelta(minutes=1)), []).poll(
            [PollMember("AAA", 1)], now=NOW, session=Session.PREMARKET,
            existing_failures=[PollFailure("IMCC", "stale", SINCE)]))
    finally:
        logger.remove(sink)
    assert result.failures == []
    dropped = [line for line in lines if "IMCC" in line]
    assert len(dropped) == 1
    assert SINCE.isoformat() in dropped[0]


def test_carried_record_for_a_member_is_kept_until_its_fetch_clears_it():
    store = Store(NOW - timedelta(minutes=10))
    carried = [PollFailure("AAA", "stale", SINCE)]
    still = asyncio.run(_poller(store, []).poll(
        [PollMember("AAA", 1)], now=NOW, session=Session.RTH, existing_failures=carried))
    assert still.failures == carried
    store.mark = NOW - timedelta(minutes=1)
    cleared = asyncio.run(_poller(store, []).poll(
        [PollMember("AAA", 1)], now=NOW, session=Session.RTH, existing_failures=still.failures))
    assert cleared.failures == []


def test_commit_gate_exception_propagates_and_stops_remaining_tickers():
    store = Store()
    poller = _poller(store, [_bar(-1)])
    with pytest.raises(StageDropped):
        asyncio.run(poller.poll([PollMember("AAA", 1)], now=NOW, session=Session.RTH,
            before_commit=lambda _ticker: lambda: (_ for _ in ()).throw(StageDropped("boundary"))))

