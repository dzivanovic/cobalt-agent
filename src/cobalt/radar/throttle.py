"""Observable, stop-first Finviz throttle probe."""

from __future__ import annotations

import asyncio
import csv
import io
import json
import math
import statistics
import time
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, time as wall_time, timezone
from pathlib import Path
from typing import Awaitable, Callable
from zoneinfo import ZoneInfo

import yaml

from cobalt.archiver.collector import (
    FetchMetrics,
    fetch_bars,
    finviz_get,
    resolve_token,
    scrub,
)
from cobalt.archiver.models import Interval
from cobalt.session import session_clock
from cobalt.session.models import Session

ET = ZoneInfo("America/New_York")
REPO_ROOT = Path(__file__).resolve().parents[3]
LISTS_FIXTURE = REPO_ROOT / "tests/fixtures/radar/radar-lists.example.md"
SCREENS_FIXTURE = REPO_ROOT / "tests/fixtures/radar/radar-screens.example.md"


class ProbeError(RuntimeError):
    """Probe cannot safely continue; the first failing request ends its stage."""


@dataclass
class Stage:
    target_rpm: int
    metrics: list[FetchMetrics] = field(default_factory=list)
    clean: bool = True
    stop_reason: str | None = None
    elapsed_s: float = 0.0

    def result(self) -> dict[str, object]:
        elapsed = max(self.elapsed_s, 1e-9)
        values = sorted(m.elapsed_ms for m in self.metrics)
        percentile = lambda p: values[min(len(values) - 1, math.ceil(p * len(values)) - 1)] if values else 0
        return {
            "target_rpm": self.target_rpm,
            "requests": len(self.metrics),
            "achieved_rpm": len(self.metrics) * 60 / elapsed,
            "statuses": dict(sorted(Counter(str(m.status or m.error) for m in self.metrics).items())),
            "p50_ms": statistics.median(values) if values else 0,
            "p95_ms": percentile(0.95),
            "bytes": sum(m.bytes for m in self.metrics),
            "clean": self.clean,
            "stop_reason": self.stop_reason,
        }


def _yaml_fences(path: Path) -> list[dict]:
    text = path.read_text(encoding="utf-8")
    blocks: list[dict] = []
    pieces = text.split("```yaml")
    for piece in pieces[1:]:
        body, marker, _ = piece.partition("```")
        if not marker:
            raise ProbeError(f"{path}: unterminated yaml fence")
        value = yaml.safe_load(body)
        if not isinstance(value, dict):
            raise ProbeError(f"{path}: fenced YAML block is not a mapping")
        blocks.append(value)
    return blocks


def fixture_inputs(names: int) -> tuple[list[str], dict[str, object]]:
    lists = [b for b in _yaml_fences(LISTS_FIXTURE) if "list" in b and b.get("enabled")]
    tickers = [ticker for block in lists for ticker in block.get("tickers", [])]
    if len(tickers) < names:
        raise ProbeError(f"{LISTS_FIXTURE}: needs {names} enabled fixture tickers, found {len(tickers)}")
    screens = [b for b in _yaml_fences(SCREENS_FIXTURE) if "screen" in b]
    if len(screens) != 1:
        raise ProbeError(f"{SCREENS_FIXTURE}: expected exactly one synthetic screen")
    return tickers[:names], screens[0]


def refusal_reason(now: datetime) -> str | None:
    if now.tzinfo is None:
        raise ProbeError("throttle probe clock must be timezone-aware")
    session = session_clock().session(now)
    et = now.astimezone(ET)
    if session is Session.MARKET_RESET:
        return "market_reset"
    if session_clock().calendar.is_trading_day(et.date()) and wall_time(9) <= et.time() < wall_time(16):
        return "09:00-16:00 ET on a trading day"
    return None


def finviz_max_rpm(stages: list[dict[str, object]]) -> int | None:
    clean = [float(s["achieved_rpm"]) for s in stages if s["clean"]]
    return math.floor(0.5 * max(clean)) if clean else None


def _validate_metric(metric: FetchMetrics) -> None:
    if metric.error:
        raise ProbeError(f"transport error: {metric.error}")
    if metric.redirect_statuses:
        raise ProbeError(f"redirect statuses: {list(metric.redirect_statuses)}")
    if metric.status != 200:
        raise ProbeError(f"HTTP status: {metric.status}")


def _validate_csv(response_text: str, expected_header: list[str] | None = None) -> list[str]:
    rows = list(csv.reader(io.StringIO(response_text)))
    if not rows or len(rows[0]) < 2:
        raise ProbeError("non-CSV body")
    header = rows[0]
    if expected_header is not None and header != expected_header:
        raise ProbeError(f"header mismatch: {header}")
    return header


async def run_probe(
    *,
    names: int,
    grids: list[int],
    cycles: int,
    now: datetime | None = None,
    token: str | None = None,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    monotonic: Callable[[], float] = time.monotonic,
) -> tuple[list[dict[str, object]], int | None]:
    instant = now or datetime.now(timezone.utc)
    refused = refusal_reason(instant)
    if refused:
        raise ProbeError(f"throttle probe refused during {refused}")
    tickers, screen = fixture_inputs(names)
    credential = token or await resolve_token()
    results: list[dict[str, object]] = []
    expected_screen_header: list[str] | None = None

    for rpm in grids:
        if rpm <= 0:
            raise ProbeError(f"grid rpm must be positive, got {rpm}")
        stage = Stage(rpm)
        started = monotonic()
        next_at = started

        def observe(metric: FetchMetrics) -> None:
            stage.metrics.append(metric)

        for _ in range(cycles):
            for ticker in tickers:
                delay = next_at - monotonic()
                if delay > 0:
                    await sleep(delay)
                try:
                    await fetch_bars(ticker, Interval.I1, credential, on_metrics=observe)
                    _validate_metric(stage.metrics[-1])
                except Exception as e:
                    stage.clean = False
                    stage.stop_reason = scrub(str(e))
                    break
                next_at = max(next_at + 60 / rpm, monotonic())
            if not stage.clean:
                break
            delay = next_at - monotonic()
            if delay > 0:
                await sleep(delay)
            params: dict[str, object] = {
                "v": 152,
                "f": screen["f"],
                "o": screen["sort"],
                "c": ",".join(str(v) for v in range(151)),
            }
            if screen.get("ft") is not None:
                params["ft"] = screen["ft"]
            try:
                response = await finviz_get(
                    "/export/screener", params, credential, on_metrics=observe
                )
                _validate_metric(stage.metrics[-1])
                expected_screen_header = _validate_csv(response.text, expected_screen_header)
            except Exception as e:
                stage.clean = False
                stage.stop_reason = scrub(str(e))
                break
            next_at = max(next_at + 60 / rpm, monotonic())
        stage.elapsed_s = monotonic() - started
        results.append(stage.result())
        if not stage.clean:
            break
    return results, finviz_max_rpm(results)


def write_result(stages: list[dict[str, object]], limit: int | None) -> Path:
    target_dir = REPO_ROOT / "data"
    target_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = target_dir / f"radar-throttle-{stamp}.json"
    path.write_text(
        json.dumps({"finviz_max_rpm": limit, "stages": stages}, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def print_table(stages: list[dict[str, object]], limit: int | None) -> None:
    print("target  requests  achieved_rpm  status  p50_ms  p95_ms  bytes  result")
    for row in stages:
        outcome = "clean" if row["clean"] else f"STOP: {row['stop_reason']}"
        print(
            f"{row['target_rpm']:>6}  {row['requests']:>8}  {row['achieved_rpm']:>12.2f}  "
            f"{str(row['statuses']):<12}  {row['p50_ms']:>6.1f}  {row['p95_ms']:>6.1f}  "
            f"{row['bytes']:>5}  {outcome}"
        )
    print(f"radar.finviz_max_rpm = {limit if limit is not None else 'NOT RUN'}")
    if stages and all(bool(s["clean"]) for s in stages):
        print(f"no throttle observed up to {max(float(s['achieved_rpm']) for s in stages):.2f} req/min")


def command(args) -> None:
    grids = [int(value.strip()) for value in args.grids.split(",") if value.strip()]
    stages, limit = asyncio.run(run_probe(names=args.names, grids=grids, cycles=args.cycles))
    path = write_result(stages, limit)
    print_table(stages, limit)
    print(path.relative_to(REPO_ROOT))


__all__ = ["ProbeError", "finviz_max_rpm", "refusal_reason", "run_probe"]
