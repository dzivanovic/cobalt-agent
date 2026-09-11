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
        body = "Ticker,Volume,Relative Volume,Asset Type\n" + "".join(f"{name},1,1,Stock\n" for name in names)
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
