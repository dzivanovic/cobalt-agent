"""S4-P1 C2/C3: the strike detector's tick and the MISSED sweep (offline).

A fake store and a fake fetch; the trade_def is the repo's synthetic
anatomy def (`radar_p2_support.anatomy_def`, an `intrabar` bar_break).
Tickers, prices and dates are constructed (L32); 2026-01-06 is an EST day,
so 15:00 UTC is 10:00 ET (RTH).
"""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

import radar_p2_support as sup
from cobalt.archiver.models import Bar, Interval
from cobalt.cards.models import Actor, CardState, IllegalTransition
from cobalt.radar.collector import TokenBucket
from cobalt.radar.notes import TotalDemandExceeded
from cobalt.session.models import Session
from cobalt.strike import detector as det
from cobalt.strike.config import StrikeSettings
from cobalt.strike.detector import (
    CONTRACT_KEYS,
    DemandPlan,
    IntervalRefused,
    StrikeCard,
    StrikeDetector,
    check_strike_demand,
    poll_interval,
)

UTC = timezone.utc
T0 = datetime(2026, 1, 6, 15, 0, tzinfo=UTC)
MIN = timedelta(minutes=1)
MD5 = "0123456789abcdef0123456789abcdef"
OLD_MD5 = "fedcba9876543210fedcba9876543210"
SLUG = sup.anatomy_def().id
SETTINGS = StrikeSettings(poll_interval_min=2, max_armed=5, alert_criterion_s=5, missed_sweep_interval=100)


def card(card_id: int, *, state="ARMED", direction="long", entry="10.00", armed_minute=0, md5=MD5,
         ticker=None) -> StrikeCard:
    return StrikeCard(
        card_id=card_id, ticker=ticker or f"ZZD{card_id}", direction=direction, state=state, trade_def_slug=SLUG,
        trade_def_md5=md5, entry=Decimal(entry), created_at=T0 - 30 * MIN,
        armed_at=(T0 + armed_minute * MIN) if state == "ARMED" else None,
    )


def bar(ticker: str, minute: int, *, high="9.90", low="9.80", close="9.85") -> Bar:
    return Bar(ticker=ticker, interval=Interval.I1, ts=T0 + minute * MIN, open=Decimal("9.85"),
               high=Decimal(high), low=Decimal(low), close=Decimal(close), volume=100)


class FakeStore:
    def __init__(self, cards, *, refuse=()):
        self.cards = list(cards)
        self.refuse = set(refuse)
        self.calls: list[dict] = []

    def strike_cards(self):
        return list(self.cards)

    def transition(self, card_id, to_state, *, actor, evidence=None, reason=None, now=None):
        if card_id in self.refuse:
            raise IllegalTransition(CardState.TRIGGERED, to_state, card_id=card_id)
        self.calls.append({"card_id": card_id, "to": to_state, "actor": actor, "evidence": evidence,
                           "reason": reason, "now": now})
        return len(self.calls)


class FakeFetch:
    def __init__(self, bars_by_ticker=None, *, fail=()):
        self.bars = bars_by_ticker or {}
        self.fail = set(fail)
        self.calls: list[str] = []

    async def __call__(self, ticker, interval, token):
        assert interval is Interval.I1
        self.calls.append(ticker)
        if ticker in self.fail:
            raise RuntimeError("Fetch failed: https://x/export?auth=SECRET&t=" + ticker)
        return self.bars.get(ticker, [bar(ticker, 1)])


class Clock:
    def __init__(self, at: datetime):
        self.at = at
        self.t = 0.0

    def now(self):
        return self.at

    def monotonic(self):
        return self.t

    async def sleep(self, seconds):
        self.t += seconds


def detector(store, fetch, *, clock=None, session=Session.RTH, plan=None, stored=None, defs=None):
    clock = clock or Clock(T0 + 5 * MIN)
    stored_calls: list[str] = []

    def stored_bars(ticker, start, end):
        stored_calls.append(ticker)
        return (stored or {}).get(ticker, [])

    d = StrikeDetector(
        store=store, fetch=fetch, token="constructed-token",
        defs=defs or (lambda slug: (MD5, sup.anatomy_def()) if slug == SLUG else None),
        stored_bars=stored_bars, settings=SETTINGS,
        plan=lambda: plan or DemandPlan(planned_rpm=0.0, headroom_rpm=50.0),
        session_of=lambda _now: session, now=clock.now,
        bucket_factory=lambda rpm: TokenBucket(rpm, monotonic=clock.monotonic, sleep=clock.sleep),
    )
    d.stored_calls = stored_calls
    return d


# -- the interval and the gate (D2) ----------------------------------------------


def test_poll_interval_is_derived_from_the_headroom():
    assert poll_interval(5, 50, 2) == 6
    assert poll_interval(5, 20, 2) == 15
    assert poll_interval(1, 50, 2) == 2
    with pytest.raises(IntervalRefused):
        poll_interval(5, 0, 2)


def test_the_strike_demand_is_counted_through_the_shared_gate():
    demand = check_strike_demand(5, 15, 30.0)
    assert demand.peak_rpm == pytest.approx(50.0)
    assert "strike" in demand.counted and "radar" in demand.counted
    with pytest.raises(TotalDemandExceeded):
        check_strike_demand(5, 3, 0.0)


def test_with_the_radar_at_30_rpm_five_names_poll_every_15_s():
    store = FakeStore([card(i, armed_minute=i) for i in range(1, 6)])
    fetch = FakeFetch()
    d = detector(store, fetch, plan=DemandPlan(planned_rpm=30.0, headroom_rpm=20.0))
    report = asyncio.run(d.tick())
    assert report.interval_s == 15 and d.interval_s() == 15
    assert len(fetch.calls) == 5


def test_a_tick_over_the_ceiling_makes_no_fetch(monkeypatch):
    monkeypatch.setattr(det, "poll_interval", lambda names, headroom, floor: 3)
    store = FakeStore([card(i, armed_minute=i) for i in range(1, 6)])
    fetch = FakeFetch()
    report = asyncio.run(detector(store, fetch).tick())
    assert fetch.calls == []
    assert report.refused and "REFUSED" in report.refused


@pytest.mark.parametrize("plan", [DemandPlan(planned_rpm=None, headroom_rpm=None),
                                  DemandPlan(planned_rpm=50.0, headroom_rpm=0.0)])
def test_an_unreadable_plan_or_no_headroom_makes_no_fetch(plan):
    store = FakeStore([card(1)])
    fetch = FakeFetch()
    report = asyncio.run(detector(store, fetch, plan=plan).tick())
    assert fetch.calls == [] and report.refused


# -- TRIGGERED ---------------------------------------------------------------------------


def test_an_armed_long_crossing_entry_is_triggered_with_the_contract():
    store = FakeStore([card(1)])
    fetch = FakeFetch({"ZZD1": [bar("ZZD1", 0), bar("ZZD1", 1, high="10.01")]})
    clock = Clock(T0 + 2 * MIN + timedelta(seconds=3))
    report = asyncio.run(detector(store, fetch, clock=clock).tick())
    assert report.triggered == [1]
    assert len(store.calls) == 1
    call = store.calls[0]
    assert call["to"] is CardState.TRIGGERED and call["actor"] is Actor.COBALT
    assert tuple(call["evidence"]) == CONTRACT_KEYS
    assert set(call["evidence"]) == {"via", "policy", "entry", "cross_price", "bar_ts", "bar_close_at", "seen_at",
                                     "cadence_s", "def_md5", "card_def_md5"}
    ev = call["evidence"]
    assert ev["via"] == "strike.detector" and ev["policy"] == "intrabar"
    assert ev["entry"] == "10.00" and ev["cross_price"] == "10.01"
    assert ev["bar_ts"] == (T0 + MIN).isoformat() and ev["bar_close_at"] == (T0 + 2 * MIN).isoformat()
    assert ev["seen_at"] == clock.at.isoformat() and ev["cadence_s"] == 2
    assert ev["def_md5"] == MD5 and ev["card_def_md5"] == MD5
    assert call["now"] == clock.at


def test_a_bar_before_the_arm_never_triggers():
    store = FakeStore([card(1, armed_minute=1)])
    fetch = FakeFetch({"ZZD1": [bar("ZZD1", 0, high="10.50"), bar("ZZD1", 1)]})
    asyncio.run(detector(store, fetch).tick())
    assert store.calls == []


def test_a_changed_def_uses_the_current_policy_and_records_both_md5s():
    store = FakeStore([card(1, md5=OLD_MD5)])
    fetch = FakeFetch({"ZZD1": [bar("ZZD1", 1, high="10.05")]})
    asyncio.run(detector(store, fetch).tick())
    ev = store.calls[0]["evidence"]
    assert ev["def_md5"] == MD5 and ev["card_def_md5"] == OLD_MD5


def test_negative_controls_no_cross_no_call():
    store = FakeStore([card(1), card(2, direction="short", entry="10.00")])
    fetch = FakeFetch({"ZZD1": [bar("ZZD1", 1, high="9.99")],
                       "ZZD2": [bar("ZZD2", 1, high="10.40", low="10.01")]})
    asyncio.run(detector(store, fetch).tick())
    assert store.calls == []
    assert fetch.calls == ["ZZD1", "ZZD2"]


def test_six_armed_five_fetched_the_latest_armed_left_out():
    store = FakeStore([card(i, armed_minute=i) for i in range(6, 0, -1)])
    fetch = FakeFetch()
    report = asyncio.run(detector(store, fetch).tick())
    assert sorted(fetch.calls) == [f"ZZD{i}" for i in range(1, 6)]
    assert report.left_out == [6]


def test_a_refused_move_is_logged_and_the_next_card_still_served():
    store = FakeStore([card(1), card(2, armed_minute=1)], refuse={1})
    fetch = FakeFetch({"ZZD1": [bar("ZZD1", 1, high="10.20")], "ZZD2": [bar("ZZD2", 2, high="10.20")]})
    report = asyncio.run(detector(store, fetch).tick())
    assert report.triggered == [2]
    assert [c["card_id"] for c in store.calls] == [2]


def test_a_fetch_failure_is_logged_scrubbed_and_the_card_retried_next_tick():
    from loguru import logger

    lines: list[str] = []
    sink = logger.add(lambda m: lines.append(str(m)), level="WARNING")
    try:
        store = FakeStore([card(1), card(2, armed_minute=1)])
        fetch = FakeFetch(fail={"ZZD1"})
        d = detector(store, fetch)
        asyncio.run(d.tick())
        fetch.fail.clear()
        asyncio.run(d.tick())
    finally:
        logger.remove(sink)
    assert fetch.calls == ["ZZD1", "ZZD2", "ZZD1", "ZZD2"]
    assert any("ZZD1" in line for line in lines)
    assert not any("SECRET" in line for line in lines)


def test_overnight_no_fetch_no_read():
    store = FakeStore([card(1)])
    fetch = FakeFetch()
    d = detector(store, fetch, session=Session.OVERNIGHT)
    report = asyncio.run(d.tick())
    assert fetch.calls == [] and store.calls == [] and d.stored_calls == []
    assert report.state == "idle:overnight"


def test_unwatchable_defs_are_skipped_and_logged_once():
    from loguru import logger

    seq = sup.anatomy_def(trigger={"type": "sequence", "steps": [{"name": "s", "predicate": {"text": "x"}}]})
    lines: list[str] = []
    sink = logger.add(lambda m: lines.append(str(m)), level="WARNING")
    try:
        store = FakeStore([card(1)])
        fetch = FakeFetch()
        d = detector(store, fetch, defs=lambda slug: (MD5, seq))
        asyncio.run(d.tick())
        asyncio.run(d.tick())
    finally:
        logger.remove(sink)
    assert fetch.calls == [] and store.calls == []
    assert sum("unwatchable" in line for line in lines) == 1


# -- MISSED (C3) ------------------------------------------------------------------------------


def test_a_watch_card_whose_stored_bars_cross_is_missed():
    store = FakeStore([card(7, state="WATCH")])
    fetch = FakeFetch()
    d = detector(store, fetch, stored={"ZZD7": [bar("ZZD7", -20), bar("ZZD7", -10, high="10.30")]})
    report = asyncio.run(d.tick())
    assert report.missed == [7]
    assert fetch.calls == []  # the stored bars, no GET
    call = store.calls[0]
    assert call["to"] is CardState.MISSED and call["actor"] is Actor.COBALT
    assert call["reason"] and "intrabar" in call["reason"] and (T0 - 10 * MIN).isoformat() in call["reason"]
    assert call["evidence"]["via"] == "strike.missed"
    assert tuple(call["evidence"]) == CONTRACT_KEYS
    assert call["evidence"]["cadence_s"] == 100


def test_the_sweep_runs_once_per_interval_not_per_tick():
    store = FakeStore([card(7, state="WATCH")])
    clock = Clock(T0)
    d = detector(store, FakeFetch(), clock=clock)
    asyncio.run(d.tick())
    clock.at = T0 + timedelta(seconds=6)
    asyncio.run(d.tick())
    assert d.stored_calls == ["ZZD7"]
    clock.at = T0 + timedelta(seconds=100)
    asyncio.run(d.tick())
    assert d.stored_calls == ["ZZD7", "ZZD7"]


def test_negative_controls_short_of_entry_and_armed_never_missed():
    store = FakeStore([card(7, state="WATCH"), card(8)])
    fetch = FakeFetch({"ZZD8": [bar("ZZD8", 1, high="9.95")]})
    d = detector(store, fetch, stored={"ZZD7": [bar("ZZD7", -10, high="9.99")],
                                       "ZZD8": [bar("ZZD8", -10, high="10.50")]})
    asyncio.run(d.tick())
    assert store.calls == []
    assert d.stored_calls == ["ZZD7"]
