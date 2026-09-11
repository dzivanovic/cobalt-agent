"""Stop-first throttle probe tests with no network or credentials."""

import asyncio
from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from cobalt.archiver.collector import FetchMetrics
from cobalt.radar import throttle
from cobalt.radar.throttle import ProbeError, finviz_max_rpm, refusal_reason

ET = ZoneInfo("America/New_York")


def test_refuses_trading_window_and_market_reset():
    assert "09:00-16:00" in refusal_reason(datetime(2026, 9, 10, 12, 0, tzinfo=ET))
    assert refusal_reason(datetime(2026, 9, 10, 20, 30, tzinfo=ET)) == "market_reset"


def test_rpm_math_uses_highest_achieved_clean_stage():
    assert finviz_max_rpm([
        {"clean": True, "achieved_rpm": 41.9},
        {"clean": False, "achieved_rpm": 99},
        {"clean": True, "achieved_rpm": 20},
    ]) == 20


def test_followed_redirect_stops_first_stage(monkeypatch):
    async def bars(_ticker, _interval, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=200, redirect_statuses=(302,), elapsed_ms=1, bytes=2, content_type="text/csv"))
        return []

    monkeypatch.setattr(throttle, "fetch_bars", bars)
    stages, limit = asyncio.run(throttle.run_probe(
        names=1, grids=[60, 30], cycles=1,
        now=datetime(2026, 9, 12, 12, 0, tzinfo=ET), token="synthetic-token",
    ))
    assert len(stages) == 1 and not stages[0]["clean"]
    assert "redirect statuses" in stages[0]["stop_reason"]
    assert limit is None


def test_naive_refusal_clock_fails_loud():
    with pytest.raises(ProbeError, match="timezone-aware"):
        refusal_reason(datetime(2026, 9, 12, 12, 0))


@pytest.mark.parametrize("status", [429, 500])
def test_non_200_status_stops(monkeypatch, status):
    async def bars(_ticker, _interval, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=status, elapsed_ms=1, bytes=1, content_type="text/csv"))
        raise RuntimeError(f"HTTP {status}")

    monkeypatch.setattr(throttle, "fetch_bars", bars)
    stages, _ = asyncio.run(throttle.run_probe(names=1, grids=[60], cycles=1,
        now=datetime(2026, 9, 12, 12, 0, tzinfo=ET), token="synthetic-token"))
    assert not stages[0]["clean"] and str(status) in stages[0]["stop_reason"]


def test_html_screener_body_stops(monkeypatch):
    async def bars(_ticker, _interval, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=1, content_type="text/csv"))
        return []

    async def screen(_path, _params, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=20, content_type="text/html"))
        return type("Response", (), {"text": "<html>failure</html>"})()

    monkeypatch.setattr(throttle, "fetch_bars", bars)
    monkeypatch.setattr(throttle, "finviz_get", screen)
    stages, _ = asyncio.run(throttle.run_probe(names=1, grids=[60], cycles=1,
        now=datetime(2026, 9, 12, 12, 0, tzinfo=ET), token="synthetic-token"))
    assert not stages[0]["clean"] and "non-CSV" in stages[0]["stop_reason"]


def test_header_change_stops(monkeypatch):
    calls = ["Ticker,Volume\nAAA,1\n", "Ticker,Other\nAAA,1\n"]

    async def bars(_ticker, _interval, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=1, content_type="text/csv"))
        return []

    async def screen(_path, _params, _token, *, on_metrics):
        body = calls.pop(0)
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=len(body), content_type="text/csv"))
        return type("Response", (), {"text": body})()

    monkeypatch.setattr(throttle, "fetch_bars", bars)
    monkeypatch.setattr(throttle, "finviz_get", screen)
    stages, _ = asyncio.run(throttle.run_probe(names=1, grids=[60], cycles=2,
        now=datetime(2026, 9, 12, 12, 0, tzinfo=ET), token="synthetic-token"))
    assert not stages[0]["clean"] and "header mismatch" in stages[0]["stop_reason"]
