"""Screener shape, list chunk, token-bucket, and cache tests."""

import asyncio
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest

from cobalt.archiver.collector import FetchMetrics
from cobalt.radar import collector as module
from cobalt.radar.collector import FinvizScreenerCollector, SourceFailure, TokenBucket, parse_screener_csv
from cobalt.radar.config import load_config
from cobalt.radar.models import ListBlock, ScreenBlock


def test_recorded_csv_parses_by_header_name():
    header, rows = parse_screener_csv(
        b"Ticker,Volume,Relative Volume,Asset Type\nAAA,10,2,Stock\n",
        source="screen-synthetic", required_headers=["Ticker", "Volume"], content_type="text/csv",
    )
    assert header[0] == "Ticker" and rows[0]["Ticker"] == "AAA"


@pytest.mark.parametrize(
    "payload,content_type,match",
    [(b"<html>no</html>", "text/html", "non-CSV"), (b"Ticker\nAAA\n", "text/csv", "missing")],
)
def test_bad_shapes_fail_loud(payload, content_type, match):
    with pytest.raises(SourceFailure, match=match):
        parse_screener_csv(payload, source="screen-synthetic", required_headers=["Ticker", "Volume"], content_type=content_type)


def test_token_bucket_fake_clock_waits_for_second_token():
    clock = [0.0]
    waits = []

    async def sleep(delay):
        waits.append(delay)
        clock[0] += delay

    bucket = TokenBucket(60, monotonic=lambda: clock[0], sleep=sleep)

    async def run():
        await bucket.acquire()
        await bucket.acquire()

    asyncio.run(run())
    assert waits == [1.0]


def test_a_50_request_burst_is_held_to_37_in_one_minute():
    """f4-strike-reserve R1: capacity 1 makes `TokenBucket(37)` a true
    per-minute cap — 37 grants in [0, 60), the 38th at 60, and no half-open
    60 s window over the grant times holds more than 37."""
    clock = [0.0]
    grants = []

    async def sleep(delay):
        # + 1 ns: a fake clock that adds exactly the bucket's deficit can leave
        # its token at 0.9999… forever (float); real time always moves on.
        clock[0] += delay + 1e-9

    bucket = TokenBucket(37, monotonic=lambda: clock[0], sleep=sleep)

    async def one():
        await bucket.acquire()
        grants.append(clock[0])

    async def run():
        await asyncio.gather(*(one() for _ in range(50)))

    asyncio.run(run())
    assert len(grants) == 50
    assert sum(1 for t in grants if t < 60.0) == 37
    assert sorted(grants)[37] >= 60.0
    assert max(sum(1 for t in grants if start <= t < start + 60.0) for start in grants) <= 37


def test_the_radar_bucket_rpm_is_radar_finviz_rpm():
    from cobalt.radar.collector import radar_bucket_rpm

    assert radar_bucket_rpm() == 37


def _by_key(rpm=..., ceiling=50):
    rows = {"radar.finviz_max_rpm": SimpleNamespace(value=ceiling)}
    if rpm is not ...:
        rows["radar.finviz_rpm"] = SimpleNamespace(value=rpm)
    return rows


@pytest.mark.parametrize("rpm", [..., None, 0, -1, 51, "37", True])
def test_radar_finviz_rpm_out_of_bounds_is_refused(rpm):
    from cobalt.radar.collector import radar_bucket_rpm

    with pytest.raises(SourceFailure, match="radar.finviz_rpm"):
        radar_bucket_rpm(_by_key(rpm))
    assert radar_bucket_rpm(_by_key(50)) == 50


def test_a_default_collector_takes_the_37_bucket(monkeypatch, tmp_path):
    from cobalt.radar.collector import FinvizDailyBarsCollector

    monkeypatch.setattr(module, "_BUCKET", None)
    monkeypatch.setattr(module, "_BUCKET_RPM", None)
    screener = FinvizScreenerCollector("synthetic", config=load_config(), cache_root=tmp_path)
    daily = FinvizDailyBarsCollector("synthetic", config=load_config(), cache_root=tmp_path)
    assert screener.bucket.rate == 37 / 60
    assert daily.bucket is screener.bucket


def test_cache_root_is_gitignored():
    import subprocess
    result = subprocess.run(["git", "check-ignore", "data/radar-cache/probe.csv"], capture_output=True, text=True)
    assert result.returncode == 0


class ImmediateBucket:
    async def acquire(self):
        return None


def test_list_requests_are_chunked_with_t_parameter(monkeypatch, tmp_path):
    calls = []

    async def get(_path, params, _token, *, on_metrics):
        calls.append(params)
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=55, content_type="text/csv"))
        names = params["t"].split(",")
        # R16 "C": an ordinary stock's `Asset Type` cell is BLANK (a
        # non-blank one is a fund) and both columns are required headers.
        body = ("Ticker,Volume,Relative Volume,Asset Type,Industry,Price\n"
                + "".join(f"{name},1,1,,Capital Markets,10.00\n" for name in names))
        return SimpleNamespace(content=body.encode())

    monkeypatch.setattr(module, "finviz_get", get)
    cfg = load_config().model_copy(update={"list_chunk_size": 2})
    collector = FinvizScreenerCollector("synthetic", config=cfg, bucket=ImmediateBucket(), cache_root=tmp_path)
    block = ListBlock(list="synthetic", description="fixture", tickers=["AAA", "BBB", "CCC"], radar=True,
        archive=[], backfill_default=True, enabled=True)
    snapshots = asyncio.run(collector.listed(block, datetime.now(timezone.utc)))
    assert [call["t"] for call in calls] == ["AAA,BBB", "CCC"]
    assert len(snapshots) == 2


def test_redirect_metric_degrades_source(monkeypatch, tmp_path):
    async def get(_path, _params, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=200, redirect_statuses=(302,), elapsed_ms=1, bytes=1, content_type="text/csv"))
        return SimpleNamespace(content=b"Ticker,Volume,Relative Volume,Asset Type\n")

    monkeypatch.setattr(module, "finviz_get", get)
    collector = FinvizScreenerCollector("synthetic", config=load_config(), bucket=ImmediateBucket(), cache_root=tmp_path)
    block = ScreenBlock(screen="synthetic", f="exch_nasd", sort="-volume", columns=[0], active_from="10:00", active_to="16:00", enabled=True)
    with pytest.raises(SourceFailure, match="redirect statuses"):
        asyncio.run(collector.screen(block, datetime.now(timezone.utc)))
