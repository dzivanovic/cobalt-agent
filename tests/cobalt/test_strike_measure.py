"""S4-P1 M1: `cobalt strike measure`, the live-feed re-measure (offline).

Every run here uses a fake fetch and a fake clock: no Finviz call, no
database, no vault write. Tickers, prices and dates are constructed (L32);
2026-01-06 is an EST day, so 15:00 UTC is 10:00 ET (RTH), 13:00 UTC is
08:00 ET (PREMARKET) and 07:00 UTC is 02:00 ET (OVERNIGHT).
"""

from __future__ import annotations

import asyncio
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.archiver.collector import CollectorError, FetchMetrics
from cobalt.archiver.models import Bar, Interval
from cobalt.session.models import Session
from cobalt.strike import measure
from cobalt.strike.measure import LagRow, MeasureRefused, PollRecord, lag_rows, run_measure, verdict

UTC = timezone.utc
RTH_AT = datetime(2026, 1, 6, 15, 0, tzinfo=UTC)
OVERNIGHT_AT = datetime(2026, 1, 6, 7, 0, tzinfo=UTC)


class FakeClock:
    def __init__(self, start: datetime):
        self.start = start
        self.t = 0.0

    def now(self) -> datetime:
        return self.start + timedelta(seconds=self.t)

    def monotonic(self) -> float:
        return self.t

    async def sleep(self, seconds: float) -> None:
        self.t += max(0.0, seconds)


class FakeFetch:
    """One i1 bar per call, stamped at the minute the fake clock is in."""

    def __init__(self, clock: FakeClock, *, fail_on: int | None = None, status: int = 429):
        self.clock = clock
        self.calls: list[str] = []
        self.fail_on = fail_on
        self.status = status

    async def __call__(self, ticker, interval, token, *, on_metrics=None):
        assert interval is Interval.I1 and token == "constructed-token"
        self.calls.append(ticker)
        if self.fail_on is not None and len(self.calls) == self.fail_on:
            if on_metrics:
                on_metrics(FetchMetrics(status=self.status, elapsed_ms=12.0))
            raise CollectorError(f"Finviz HTTP failed: {self.status}")
        if on_metrics:
            on_metrics(FetchMetrics(status=200, elapsed_ms=10.0, bytes=100))
        now = self.clock.now()
        ts = now.replace(second=0, microsecond=0)
        return [Bar(ticker=ticker, interval=Interval.I1, ts=ts, open=Decimal("10"), high=Decimal("10.1"),
                    low=Decimal("9.9"), close=Decimal("10"), volume=100)]


async def _token():
    return "constructed-token"


def _run(clock, fetch, *, names, cadence, minutes, out, planned=lambda: 0.0, session_of=None):
    return asyncio.run(run_measure(
        names, cadence, minutes, out, fetch=fetch, token_source=_token, now=clock.now,
        monotonic=clock.monotonic, sleep=clock.sleep, planned_rpm=planned,
        session_of=session_of or (lambda _now: Session.RTH),
    ))


# -- (a) the lag rows -----------------------------------------------------------


def test_lag_rows_equal_hand_computed_values():
    def poll(sec: int, newest_min: int) -> PollRecord:
        return PollRecord(at=RTH_AT + timedelta(seconds=sec), ticker="ZZMA", status=200, fetch_ms=10.0,
                          newest_ts=RTH_AT + timedelta(minutes=newest_min), session="rth", error=None)

    polls = [poll(2, -1), poll(5, -1), poll(8, 0), poll(11, 0), poll(63, 1), poll(66, 1), poll(121, 1),
             poll(124, 2)]
    rows = lag_rows(polls)
    assert [(r.bar_ts, r.lag_s) for r in rows] == [
        (RTH_AT, 8.0),
        (RTH_AT + timedelta(minutes=1), 3.0),
        (RTH_AT + timedelta(minutes=2), 4.0),
    ]
    assert all(r.session == "rth" and r.ticker == "ZZMA" for r in rows)


# -- (b) the first non-200 stops the run ------------------------------------------


def test_a_429_stops_at_the_first_failure_and_writes_the_summary(tmp_path):
    clock = FakeClock(RTH_AT)
    fetch = FakeFetch(clock, fail_on=7)
    result = _run(clock, fetch, names=["ZZMA", "ZZMB"], cadence=3, minutes=10, out=tmp_path)
    assert result.exit_code == 1
    assert len(fetch.calls) == 7  # no 8th GET
    assert result.verdict.startswith("THROTTLED at 3 s")
    assert result.md_path.exists() and result.jsonl_path.exists()
    assert result.md_path.read_text().rstrip().splitlines()[-1] == result.verdict
    assert len(result.jsonl_path.read_text().splitlines()) == 7


# -- (c) the refusals, all before the first GET ---------------------------------------


@pytest.mark.parametrize("names,cadence,planned,match", [
    (["A", "B", "C", "D", "E", "F"], 3, 0.0, "6 names"),
    (["A"], 1, 0.0, "cadence 1 s"),
    (["A", "B", "C", "D", "E"], 3, 0.0, "minimum cadence 6 s"),
    (["A", "B", "C", "D", "E"], 6, 30.0, "minimum cadence 15 s"),
])
def test_refused_before_any_get(tmp_path, names, cadence, planned, match):
    clock = FakeClock(RTH_AT)
    fetch = FakeFetch(clock)
    with pytest.raises(MeasureRefused, match=match):
        _run(clock, fetch, names=names, cadence=cadence, minutes=1, out=tmp_path, planned=lambda: planned)
    assert fetch.calls == []
    assert list(tmp_path.iterdir()) == []


def test_at_the_named_minimum_it_runs_to_the_get_cap(tmp_path):
    clock = FakeClock(RTH_AT)
    fetch = FakeFetch(clock)
    result = _run(clock, fetch, names=["A", "B", "C", "D", "E"], cadence=15, minutes=1, out=tmp_path,
                  planned=lambda: 30.0)
    assert result.exit_code == 0
    assert len(fetch.calls) == 5 * 4  # names x ceil(minutes x 60 / cadence)


@pytest.mark.parametrize("planned", [lambda: None, lambda: (_ for _ in ()).throw(RuntimeError("no notes"))])
def test_an_unreadable_radar_plan_is_refused(tmp_path, planned):
    clock = FakeClock(RTH_AT)
    fetch = FakeFetch(clock)
    with pytest.raises(MeasureRefused, match="planned rpm"):
        _run(clock, fetch, names=["A"], cadence=3, minutes=1, out=tmp_path, planned=planned)
    assert fetch.calls == []


# -- (d) no database ------------------------------------------------------------------


def test_the_run_opens_no_database_connection(tmp_path, monkeypatch):
    import psycopg

    def _refuse(*_a, **_k):
        raise AssertionError("strike measure opened a database connection")

    monkeypatch.setattr(psycopg, "connect", _refuse)
    monkeypatch.setattr(psycopg.AsyncConnection, "connect", _refuse)
    clock = FakeClock(RTH_AT)
    fetch = FakeFetch(clock)
    result = asyncio.run(run_measure(
        ["ZZMA"], 3, 1, tmp_path, fetch=fetch, token_source=_token, now=clock.now,
        monotonic=clock.monotonic, sleep=clock.sleep, planned_rpm=lambda: 0.0,
    ))  # the REAL session clock
    assert result.exit_code == 0 and len(fetch.calls) == 20
    assert sorted(p.name for p in tmp_path.iterdir()) == ["strike-measure-2026-01-06.jsonl",
                                                         "strike-measure-2026-01-06.md"]


# -- (e) outside PREMARKET / RTH: no GET ------------------------------------------------


def test_overnight_makes_no_get(tmp_path):
    clock = FakeClock(OVERNIGHT_AT)
    fetch = FakeFetch(clock)
    result = asyncio.run(run_measure(
        ["ZZMA"], 3, 1, tmp_path, fetch=fetch, token_source=_token, now=clock.now,
        monotonic=clock.monotonic, sleep=clock.sleep, planned_rpm=lambda: 0.0,
    ))
    assert fetch.calls == []
    assert result.exit_code == 0
    assert result.verdict.startswith("NOT MET")


# -- (f) the real token path is DB-free ----------------------------------------------------


@pytest.mark.skipif(not Path("data/.cobalt_vault").exists(),
                    reason="no Finviz vault on this host — real token path not proven DB-free here")
def test_the_real_token_path_opens_no_database(monkeypatch):
    import psycopg

    from cobalt.archiver.collector import resolve_token

    called: list[str] = []

    def _refuse(*_a, **_k):
        called.append("connect")
        raise AssertionError("token resolution opened a database connection")

    monkeypatch.setattr(psycopg, "connect", _refuse)
    monkeypatch.setattr(psycopg.AsyncConnection, "connect", _refuse)
    token = asyncio.run(resolve_token())
    assert token
    assert called == []


# -- the verdict, the Charter's rule ----------------------------------------------------------


def _lags(session: str, value: float, n: int = 20) -> list[LagRow]:
    return [LagRow(ticker="ZZMA", bar_ts=RTH_AT + timedelta(minutes=i), seen_at=RTH_AT, lag_s=value,
                   session=session) for i in range(n)]


def test_negative_control_all_200_p95_4s_holds():
    got = verdict(cadence=3, criterion_s=5, failure=None, lags=_lags("premarket", 4.0) + _lags("rth", 4.0),
                  windows_run=["premarket", "rth"])
    assert got == "CRITERION ≤5 s HOLDS at 3 s"


def test_p95_over_the_criterion_is_not_met_naming_the_window():
    got = verdict(cadence=3, criterion_s=5, failure=None, lags=_lags("premarket", 4.0) + _lags("rth", 7.0),
                  windows_run=["premarket", "rth"])
    assert got == "NOT MET — RTH p95 7.0 s"


def test_a_transport_failure_is_throttled():
    failure = PollRecord(at=RTH_AT, ticker="ZZMA", status=None, fetch_ms=30000.0, newest_ts=None,
                         session="rth", error="ConnectTimeout")
    got = verdict(cadence=3, criterion_s=5, failure=failure, lags=[], windows_run=["rth"])
    assert got == "THROTTLED at 3 s — Charter re-rule: 10 s cadence (~8 s)"


def test_the_verb_is_registered(monkeypatch):
    import sys

    from cobalt import cli

    seen = []
    monkeypatch.setattr(measure, "command", lambda args: seen.append(args))
    monkeypatch.setattr(sys, "argv", ["cobalt", "strike", "measure", "--names", "ZZMA,ZZMB", "--cadence", "3",
                                      "--minutes", "20", "--out", "/nonexistent-dir"])
    cli.main()
    assert seen and seen[0].names == "ZZMA,ZZMB" and seen[0].cadence == 3 and seen[0].minutes == 20
