"""Finviz screener collection, strict CSV parsing, caching, and rate limiting."""

from __future__ import annotations

import asyncio
import csv
import io
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Awaitable, Callable, Protocol

from cobalt.archiver.collector import FetchMetrics, finviz_get, scrub

from .config import RadarConfig, load_config
from .models import ListBlock, ScreenBlock


class SourceFailure(RuntimeError):
    """A source response was unsafe or unusable; degrade it, never guess."""


@dataclass(frozen=True)
class ScreenerSnapshot:
    source: str
    at: datetime
    rows: tuple[dict[str, str], ...]
    header: tuple[str, ...]
    cache_path: Path | None = None


class ScreenerCollector(Protocol):
    async def screen(self, block: ScreenBlock, now: datetime) -> ScreenerSnapshot: ...
    async def listed(self, block: ListBlock, now: datetime) -> list[ScreenerSnapshot]: ...


class TokenBucket:
    """Async token bucket; a fake monotonic clock/sleep makes it deterministic."""

    def __init__(
        self,
        rpm: int,
        *,
        monotonic: Callable[[], float] = time.monotonic,
        sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    ):
        if rpm <= 0:
            raise ValueError(f"finviz rpm must be positive, got {rpm}")
        self.rate = rpm / 60
        self.capacity = 1.0
        self.tokens = 1.0
        self.updated = monotonic()
        self._clock = monotonic
        self._sleep = sleep
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        async with self._lock:
            while True:
                now = self._clock()
                self.tokens = min(self.capacity, self.tokens + (now - self.updated) * self.rate)
                self.updated = now
                if self.tokens >= 1:
                    self.tokens -= 1
                    return
                await self._sleep((1 - self.tokens) / self.rate)


_BUCKET: TokenBucket | None = None
_BUCKET_RPM: int | None = None


def process_bucket(rpm: int) -> TokenBucket:
    global _BUCKET, _BUCKET_RPM
    if _BUCKET is None or _BUCKET_RPM != rpm:
        _BUCKET, _BUCKET_RPM = TokenBucket(rpm), rpm
    return _BUCKET


def parse_screener_csv(
    payload: bytes,
    *,
    source: str,
    required_headers: list[str],
    content_type: str | None,
) -> tuple[tuple[str, ...], tuple[dict[str, str], ...]]:
    lowered = (content_type or "").lower()
    if "html" in lowered or (payload.lstrip().startswith(b"<") and b"html" in payload[:100].lower()):
        raise SourceFailure(f"{source}: non-CSV body ({content_type or 'content type missing'})")
    try:
        text = payload.decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text))
        header = tuple(reader.fieldnames or ())
        rows = tuple(dict(row) for row in reader)
    except (UnicodeDecodeError, csv.Error) as e:
        raise SourceFailure(f"{source}: non-CSV body: {scrub(str(e))}") from e
    if not header:
        raise SourceFailure(f"{source}: empty CSV header")
    missing = [name for name in required_headers if name not in header]
    if missing:
        raise SourceFailure(f"{source}: header mismatch; missing {missing}")
    return header, rows


class FinvizScreenerCollector:
    def __init__(
        self,
        token: str,
        *,
        config: RadarConfig | None = None,
        bucket: TokenBucket | None = None,
        cache_root: Path | None = None,
    ):
        self.config = config or load_config()
        self.token = token
        if bucket is None:
            from cobalt.taxonomy.loader import load_tunables

            raw = load_tunables().by_key["radar.finviz_max_rpm"].value
            if raw is None:
                raise SourceFailure("radar.finviz_max_rpm is unmeasured")
            bucket = process_bucket(int(raw))
        self.bucket = bucket
        self.cache_root = cache_root or Path(self.config.cache.dir)

    def _params(self) -> dict[str, object]:
        return {
            "v": self.config.export.v,
            "c": ",".join(str(value) for value in range(151)),
        }

    def _cache(self, source: str, now: datetime, payload: bytes) -> Path:
        target = self.cache_root / now.date().isoformat()
        target.mkdir(parents=True, exist_ok=True)
        path = target / f"{source}-{now.strftime('%H%M%S')}.csv"
        path.write_bytes(payload)
        cutoff = now.date() - timedelta(days=self.config.cache.retention_days)
        for directory in self.cache_root.iterdir():
            if directory.is_dir():
                try:
                    day = date.fromisoformat(directory.name)
                except ValueError:
                    continue
                if day < cutoff:
                    for item in directory.iterdir():
                        if item.is_file():
                            item.unlink()
                    directory.rmdir()
        return path

    async def _request(self, source: str, params: dict[str, object], now: datetime) -> ScreenerSnapshot:
        metrics: list[FetchMetrics] = []
        await self.bucket.acquire()
        try:
            response = await finviz_get(
                "/export/screener", params, self.token, on_metrics=metrics.append
            )
        except Exception as e:
            raise SourceFailure(f"{source}: {scrub(str(e))}") from e
        metric = metrics[-1]
        if metric.redirect_statuses:
            raise SourceFailure(f"{source}: redirect statuses {list(metric.redirect_statuses)}")
        header, rows = parse_screener_csv(
            response.content,
            source=source,
            required_headers=self.config.export.required_headers,
            content_type=metric.content_type,
        )
        path = self._cache(source, now, response.content)
        return ScreenerSnapshot(source, now, rows, header, path)

    async def screen(self, block: ScreenBlock, now: datetime) -> ScreenerSnapshot:
        params = {**self._params(), "f": block.f, "o": block.sort}
        if block.ft is not None:
            params["ft"] = block.ft
        return await self._request(f"screen-{block.screen}", params, now)

    async def listed(self, block: ListBlock, now: datetime) -> list[ScreenerSnapshot]:
        snapshots: list[ScreenerSnapshot] = []
        size = self.config.list_chunk_size
        for index in range(0, len(block.tickers), size):
            chunk = block.tickers[index:index + size]
            params = {**self._params(), "t": ",".join(chunk)}
            snapshots.append(
                await self._request(f"list-{block.list}-{index // size + 1}", params, now)
            )
        return snapshots


__all__ = [
    "FinvizScreenerCollector", "ScreenerCollector", "ScreenerSnapshot",
    "SourceFailure", "TokenBucket", "parse_screener_csv", "process_bucket",
]
