"""S2-P2 STEP-3 / R5 / L53 — the daily-bars collector and total Finviz demand.

R5: daily bars are fetched behind the collector interface, ONE request per
name per ET day, cached, and counted against the Finviz ceiling with a
total-demand computation across every consumer. Astra R1-13: the proof
includes a cold-cache burst on top of a near-full pool scan, recurring
context-ticker demand and retries, and describes actual pacing (the shared
TokenBucket waits, it does not refuse); the cache's nested `daily/`
directory is covered by retention cleanup; restart cache hits and ET-day
rollover are tested.
"""

from __future__ import annotations

import asyncio
import csv
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from types import SimpleNamespace
from zoneinfo import ZoneInfo

import pytest

from cobalt.archiver.collector import FetchMetrics
from cobalt.radar import collector as module
from cobalt.radar.collector import (
    DAILY_RETRIES_PER_REQUEST,
    DailyBarsSource,
    FinvizDailyBarsCollector,
    FinvizScreenerCollector,
    SourceFailure,
    prune_cache,
)
from cobalt.radar.config import load_config
from cobalt.radar.models import PoolBlock
from cobalt.radar.notes import load_sources, plan_transport_demand

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "radar"
ET = ZoneInfo("America/New_York")


def _export_body(ticker: str) -> bytes:
    """The daily export shape rebuilt from the hub-cut real-shape rows
    (the cut documents the raw columns and MM/DD/YYYY dates)."""
    with (FIXTURES / "daily-bars.real-shape.csv").open() as f:
        rows = [r for r in csv.DictReader(f) if r["Ticker"] == ticker]
    lines = ["Date,Open,High,Low,Close,Volume"] + [
        f"{date.fromisoformat(r['Date']):%m/%d/%Y},{r['Open']},{r['High']},{r['Low']},{r['Close']},{r['Volume']}"
        for r in rows
    ]
    return ("\n".join(lines) + "\n").encode()


class CountingBucket:
    def __init__(self):
        self.acquired = 0

    async def acquire(self):
        self.acquired += 1


def _fake_get(calls, body_for=_export_body, status_meta=None):
    async def get(path, params, _token, *, on_metrics):
        calls.append((path, dict(params)))
        on_metrics(status_meta or FetchMetrics(status=200, elapsed_ms=1, bytes=10, content_type="text/csv"))
        return SimpleNamespace(content=body_for(params["t"]), text=body_for(params["t"]).decode())

    return get


def _collector(tmp_path, bucket=None):
    return FinvizDailyBarsCollector(
        "synthetic", config=load_config(), bucket=bucket or CountingBucket(), cache_root=tmp_path
    )


def test_daily_collector_satisfies_the_collector_interface(tmp_path):
    assert isinstance(_collector(tmp_path), DailyBarsSource)


def test_daily_fetch_once_per_name_per_day_cached(tmp_path, monkeypatch):
    calls: list = []
    monkeypatch.setattr(module, "finviz_get", _fake_get(calls))
    bucket = CountingBucket()
    collector = _collector(tmp_path, bucket)
    now = datetime(2026, 1, 6, 15, 0, tzinfo=timezone.utc)

    first = asyncio.run(collector.daily("FTFT", now))
    second = asyncio.run(collector.daily("FTFT", now + timedelta(hours=3)))
    assert first.bars == second.bars and first.bars
    assert calls == [("/export/stock", {"t": "FTFT", "p": "d"})]
    assert bucket.acquired == 1
    cached = tmp_path / "2026-01-06" / "daily" / "FTFT.csv"
    assert cached.exists()
    assert first.source == "cache-miss" and second.source == "cache-hit"

    # A restart is a new collector over the same cache: still no request.
    restarted = _collector(tmp_path, bucket)
    third = asyncio.run(restarted.daily("FTFT", now + timedelta(hours=4)))
    assert third.bars == first.bars and len(calls) == 1 and bucket.acquired == 1

    asyncio.run(collector.daily("BGFI", now))
    assert [c[1]["t"] for c in calls] == ["FTFT", "BGFI"]


def test_cache_day_is_the_et_day_and_rolls_over_at_et_midnight(tmp_path, monkeypatch):
    calls: list = []
    monkeypatch.setattr(module, "finviz_get", _fake_get(calls))
    collector = _collector(tmp_path)
    late_et = datetime(2026, 1, 6, 23, 59, tzinfo=ET)  # 04:59 UTC on the 7th
    asyncio.run(collector.daily("FTFT", late_et))
    assert (tmp_path / "2026-01-06" / "daily" / "FTFT.csv").exists()
    asyncio.run(collector.daily("FTFT", late_et + timedelta(minutes=2)))
    assert (tmp_path / "2026-01-07" / "daily" / "FTFT.csv").exists()
    assert len(calls) == 2


def test_bad_daily_body_is_a_source_failure_and_nothing_is_cached(tmp_path, monkeypatch):
    calls: list = []
    monkeypatch.setattr(module, "finviz_get", _fake_get(calls, body_for=lambda _t: b"<html>login</html>"))
    collector = _collector(tmp_path)
    now = datetime(2026, 1, 6, 15, 0, tzinfo=timezone.utc)
    with pytest.raises(SourceFailure, match="FTFT"):
        asyncio.run(collector.daily("FTFT", now))
    assert not (tmp_path / "2026-01-06" / "daily" / "FTFT.csv").exists()


def test_redirected_daily_fetch_degrades(tmp_path, monkeypatch):
    calls: list = []
    meta = FetchMetrics(status=200, redirect_statuses=(302,), elapsed_ms=1, bytes=1, content_type="text/csv")
    monkeypatch.setattr(module, "finviz_get", _fake_get(calls, status_meta=meta))
    with pytest.raises(SourceFailure, match="redirect"):
        asyncio.run(_collector(tmp_path).daily("FTFT", datetime(2026, 1, 6, 15, tzinfo=timezone.utc)))


def test_retention_prunes_date_directories_with_a_nested_daily_dir(tmp_path):
    old = tmp_path / "2025-12-01"
    (old / "daily").mkdir(parents=True)
    (old / "daily" / "FTFT.csv").write_text("x")
    (old / "screen-a-100000.csv").write_text("x")
    keep = tmp_path / "2026-01-05" / "daily"
    keep.mkdir(parents=True)
    (keep / "FTFT.csv").write_text("x")
    (tmp_path / "not-a-date").mkdir()
    prune_cache(tmp_path, today=date(2026, 1, 6), retention_days=7)
    assert not old.exists()
    assert (keep / "FTFT.csv").exists()
    assert (tmp_path / "not-a-date").exists()


def test_screener_cache_write_survives_an_old_day_with_nested_daily(tmp_path, monkeypatch):
    old = tmp_path / "2025-12-01" / "daily"
    old.mkdir(parents=True)
    (old / "FTFT.csv").write_text("x")

    async def get(_path, _params, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=10, content_type="text/csv"))
        return SimpleNamespace(content=b"Ticker,Volume,Relative Volume,Asset Type\nAAA,1,1,Stock\n")

    monkeypatch.setattr(module, "finviz_get", get)
    screener = FinvizScreenerCollector("synthetic", config=load_config(), bucket=CountingBucket(), cache_root=tmp_path)
    from cobalt.radar.models import ScreenBlock

    block = ScreenBlock(screen="synthetic", f="exch_nasd", sort="-volume", columns=[0],
                        active_from="10:00", active_to="16:00", enabled=True)
    asyncio.run(screener.screen(block, datetime(2026, 1, 6, 15, tzinfo=timezone.utc)))
    assert not (tmp_path / "2025-12-01").exists()


# ---------------------------------------------------------------------
# L53 — total demand across every consumer of the shared transport
# ---------------------------------------------------------------------


def _pool(cap: int) -> PoolBlock:
    text = (FIXTURES / "radar-screens.example.md").read_text()
    from cobalt.radar.notes import parse_note_bytes

    parsed = parse_note_bytes(Path("screens.md"), "screens", text.replace("cap: 5", f"cap: {cap}").encode())
    return next(item.block for item in parsed.blocks if item.key == "pool")


def test_total_finviz_demand_refuses_when_sum_exceeds_ceiling_while_each_consumer_alone_passes():
    pool = _pool(50)
    kwargs = dict(screen_count=1, list_blocks=[], list_chunk_size=50, scan_interval=100,
                  retries_per_request=0, ceiling_rpm=40)
    pool_alone = plan_transport_demand(pool, context_tickers=0, daily_names=0, **{**kwargs, "screen_count": 0})
    assert pool_alone.refusal is None and pool_alone.steady_rpm == pytest.approx(30.0)
    context_alone = plan_transport_demand(_pool(1), context_tickers=12, daily_names=0, **{**kwargs, "screen_count": 0})
    assert context_alone.refusal is None and context_alone.context_rpm == pytest.approx(7.2)

    together = plan_transport_demand(pool, context_tickers=20, daily_names=0, **kwargs)
    assert together.steady_rpm == pytest.approx(30 + 0.6 + 12)
    assert together.refusal and "exceeds" in together.refusal

    # Daily alone has the whole ceiling to drain into; beside a steady load
    # that exactly fills the ceiling it never completes, so it is refused.
    at60 = dict(list_blocks=[], list_chunk_size=50, scan_interval=60, retries_per_request=0, ceiling_rpm=40)
    steady_full = plan_transport_demand(_pool(39), screen_count=1, context_tickers=0, daily_names=0, **at60)
    assert steady_full.refusal is None and steady_full.headroom_rpm == pytest.approx(0)
    daily_alone = plan_transport_demand(_pool(1), screen_count=0, context_tickers=0, daily_names=39, **at60)
    assert daily_alone.refusal is None
    starved = plan_transport_demand(_pool(39), screen_count=1, context_tickers=0, daily_names=39, **at60)
    assert starved.refusal and "no headroom" in starved.refusal


def test_cold_cache_burst_on_a_near_full_scan_describes_actual_pacing():
    pool = _pool(50)
    plan = plan_transport_demand(pool, screen_count=1, list_blocks=[], list_chunk_size=50,
                              scan_interval=100, context_tickers=3, daily_names=50,
                              retries_per_request=1, ceiling_rpm=40)
    # retries double every request's worst case
    assert plan.steady_rpm == pytest.approx((30 + 0.6 + 1.8) * 2)
    assert plan.refusal  # 64.8 steady > 40 with one retry each
    plan = plan_transport_demand(pool, screen_count=1, list_blocks=[], list_chunk_size=50,
                              scan_interval=100, context_tickers=3, daily_names=50,
                              retries_per_request=0, ceiling_rpm=40)
    assert plan.refusal is None
    assert plan.headroom_rpm == pytest.approx(40 - 32.4)
    assert plan.cold_drain_minutes == pytest.approx(50 / (40 - 32.4))
    # The bucket paces the first cycle to the ceiling: 54 steady requests
    # plus 50 cold daily requests at 40/min.
    assert plan.cycle_requests == 54 and plan.cold_cycle_seconds == pytest.approx((54 + 50) * 60 / 40)
    assert plan.cold_cycle_overruns_scan_interval is True
    assert plan.pacing == "token_bucket_waits"


def test_collector_retry_constant_is_what_the_demand_check_uses():
    assert DAILY_RETRIES_PER_REQUEST == 0


def test_load_sources_counts_daily_and_context_in_the_ceiling():
    text = (FIXTURES / "radar-screens.example.md").read_text().replace("cap: 5", "cap: 50")
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory:
        candidate = Path(directory) / "screens.md"
        candidate.write_text(text)
        ok = load_sources(candidate, FIXTURES / "radar-lists.example.md", scan_interval=100,
                          poll_interval=100, finviz_max_rpm=40, list_chunk_size=50, context_tickers=0)
        assert ok.pool_error is None and ok.demand is not None and ok.demand.daily_names == 50
        starved = load_sources(candidate, FIXTURES / "radar-lists.example.md", scan_interval=100,
                               poll_interval=100, finviz_max_rpm=40, list_chunk_size=50, context_tickers=14)
    # pool 30 + screens 0.6 + lists 1.2 + context 8.4 = 40.2 > 40
    assert starved.frozen and "pool budget exceeded" in starved.pool_error
    assert "context=8.40" in starved.pool_error


def test_radar_config_declares_context_tickers():
    cfg = load_config()
    assert isinstance(cfg.context.tickers, list)
