"""S2-P2 STEP-3, Astra R1-12 — RVOL replays, and staleness is per dependency.

RVOL is read from the same screener snapshot the pool is built from; the
scan keeps it as a timestamped observation (source precedence stated for
a ticker carried by more than one source) so a bars-only replay is not
left without it. The "older than 2 x radar.scan_interval -> stale" rule
applies by dependency type: intraday bars and RVOL use it, daily bars use
a session boundary, versioned policy/tunable inputs never go stale on a
wall clock.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone

import pytest

from cobalt.radar.anatomy.daily import DailyBar, DailySeries
from cobalt.radar.anatomy.freshness import (
    RvolObservation,
    daily_staleness,
    intraday_staleness,
    policy_staleness,
    previous_trading_day,
    rvol_observations,
)
from cobalt.radar.models import SourceSet
from cobalt.session.clock import session_clock

AT = datetime(2026, 1, 6, 15, 0, tzinfo=timezone.utc)


def _set(source, kind, order, metrics, health="healthy"):
    return SourceSet(source=source, kind=kind, note_order=order, metrics=metrics,
                     tickers=list(metrics), health=health)


def test_rvol_observation_is_timestamped_with_its_source():
    obs = rvol_observations([_set("screen:a@1", "screen", 0, {"FTFT": {"volume": 10.0, "rvol": 3.5}})], observed_at=AT)
    assert obs["FTFT"] == RvolObservation(
        ticker="FTFT", value=3.5, observed_at=AT, source="screen:a@1",
        candidates=("screen:a@1",), precedence="screen_before_list_then_note_order_then_source_id",
    )


def test_duplicate_ticker_precedence_is_screen_then_note_order_then_source_id():
    sets = [
        _set("list:watch@9", "list", 0, {"FTFT": {"rvol": 9.0}}),
        _set("screen:late@2", "screen", 5, {"FTFT": {"rvol": 2.0}}),
        _set("screen:early@1", "screen", 1, {"FTFT": {"rvol": 1.0}}),
        _set("screen:b@3", "screen", 1, {"FTFT": {"rvol": 4.0}}),
    ]
    obs = rvol_observations(sets, observed_at=AT)["FTFT"]
    assert obs.source == "screen:b@3" and obs.value == 4.0
    assert obs.candidates == ("screen:b@3", "screen:early@1", "screen:late@2", "list:watch@9")
    # Input order never changes the winner.
    assert rvol_observations(list(reversed(sets)), observed_at=AT)["FTFT"] == obs


def test_missing_rvol_is_kept_as_an_explicit_none_never_dropped_or_zeroed():
    obs = rvol_observations([_set("screen:a@1", "screen", 0, {"BGFI": {"volume": 5.0, "rvol": None}})], observed_at=AT)
    assert obs["BGFI"].value is None


def test_degraded_and_inactive_sources_carry_no_rvol():
    sets = [
        _set("screen:a@1", "screen", 0, {"FTFT": {"rvol": 3.0}}, health="degraded"),
        SourceSet(source="screen:b@2", kind="screen", active=False, metrics={"FTFT": {"rvol": 5.0}}),
    ]
    assert rvol_observations(sets, observed_at=AT) == {}


def test_rvol_observed_at_must_be_aware():
    with pytest.raises(ValueError, match="tz-aware"):
        rvol_observations([], observed_at=datetime(2026, 1, 6, 15, 0))


def test_intraday_ttl_is_two_scan_intervals():
    fresh = intraday_staleness(observed_at=AT, as_of=AT + timedelta(seconds=200), scan_interval=100)
    assert not fresh.stale and fresh.ttl_seconds == 200 and fresh.rule == "intraday_2x_scan_interval"
    stale = intraday_staleness(observed_at=AT, as_of=AT + timedelta(seconds=201), scan_interval=100)
    assert stale.stale and stale.age_seconds == 201


def test_intraday_observation_from_the_future_is_refused():
    with pytest.raises(ValueError, match="after as_of"):
        intraday_staleness(observed_at=AT + timedelta(seconds=1), as_of=AT, scan_interval=100)


def _series(*days: date) -> DailySeries:
    one = dict(open=1, high=2, low=1, close=2, volume=1)
    return DailySeries(ticker="FTFT", bars=tuple(DailyBar(session_date=d, **one) for d in days))


def test_previous_trading_day_skips_weekends_and_holidays():
    calendar = session_clock().calendar
    assert previous_trading_day(date(2026, 1, 6), calendar.is_trading_day) == date(2026, 1, 5)
    assert previous_trading_day(date(2026, 1, 5), calendar.is_trading_day) == date(2026, 1, 2)
    # 2026-01-01 is a holiday: the session before 01-02 is 12-31.
    assert previous_trading_day(date(2026, 1, 2), calendar.is_trading_day) == date(2025, 12, 31)


def test_daily_ttl_is_the_session_boundary_not_a_wall_clock():
    is_trading_day = session_clock().calendar.is_trading_day
    fresh = daily_staleness(_series(date(2026, 1, 2), date(2026, 1, 5)), trade_date=date(2026, 1, 6),
                            is_trading_day=is_trading_day)
    assert not fresh.stale and fresh.rule == "daily_last_completed_session"
    assert fresh.expected_session == date(2026, 1, 5) and fresh.latest_session == date(2026, 1, 5)

    # Today's partial row does not count as the last completed session.
    lagging = daily_staleness(_series(date(2026, 1, 2), date(2026, 1, 6)), trade_date=date(2026, 1, 6),
                              is_trading_day=is_trading_day)
    assert lagging.stale and lagging.latest_session == date(2026, 1, 2)

    empty = daily_staleness(_series(date(2026, 1, 6)), trade_date=date(2026, 1, 6), is_trading_day=is_trading_day)
    assert empty.stale and empty.latest_session is None


def test_policy_and_tunable_inputs_never_go_stale_on_a_wall_clock():
    verdict = policy_staleness(version_sha256="a" * 64)
    assert not verdict.stale and verdict.rule == "versioned_never_wall_clock"
