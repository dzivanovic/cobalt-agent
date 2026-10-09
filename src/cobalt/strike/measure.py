"""`cobalt strike measure` — the F9 live-feed re-measure (S4-P1 M1).

MEASUREMENT ONLY, the spike's pattern (`docs/30 - Design/LIVE-FEED-SPIKE.md`)
committed so it can run unattended. Each cycle makes one i1 `fetch`
per name (default `archiver.collector.fetch_bars`, injected as
`radar/poller.py` injects it), paced by its own
`TokenBucket` at its counted share (names × 60 / cadence rpm).

LAG, the spike's own definition: for each bar start T, the first wall-clock
poll whose newest bar has ts = T, minus T. A ticker's first poll sets its
baseline and is not a transition.

THE VERDICT, the last line of the summary (Charter F9): `CRITERION ≤<c> s
HOLDS at <cadence> s` when every GET was 200 and lag p95 ≤ `strike.
alert_criterion_s` in each window run; `THROTTLED at <cadence> s — …` on a
403, a 429 or a transport failure; `NOT MET — …` otherwise. The verdict is
a printed fact; the criterion is the desk's to fix (DECISION D1).

UNATTENDED-SAFE. Refused before the first GET: more than `strike.max_armed`
names, a cadence below `strike.poll_interval_min`, an unreadable radar plan,
and any cadence whose demand added to the radar's planned rpm puts the
combined peak over `radar.finviz_max_rpm` (`notes.check_scheduled_demand`;
the refusal names the minimum cadence, DECISION D2). Stops at the FIRST
non-200 or `CollectorError` (summary written, exit 1) and at the GET cap
names × ⌈minutes × 60 / cadence⌉. Polls only in PREMARKET or RTH. Opens no
database connection, writes no vault file; writes only
`<out>/strike-measure-<date>.jsonl` and `.md`. Touches no trading platform.
"""

from __future__ import annotations

import asyncio
import json
import math
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Awaitable, Callable, Optional

from cobalt.archiver.collector import fetch_bars, resolve_token, scrub
from cobalt.archiver.models import Interval
from cobalt.session import clock as clock_mod
from cobalt.session.clock import ET
from cobalt.session.models import Session

from .config import StrikeSettings, check

ACTIVE = (Session.PREMARKET, Session.RTH)
THROTTLE_STATUSES = (403, 429)


class MeasureRefused(RuntimeError):
    """Refused before the first GET."""


@dataclass(frozen=True)
class PollRecord:
    at: datetime  # the wall clock when the poll's answer arrived
    ticker: str
    status: Optional[int]
    fetch_ms: float
    newest_ts: Optional[datetime]
    session: str
    error: Optional[str]

    def as_json(self) -> dict:
        row = asdict(self)
        row["at"] = self.at.isoformat()
        row["newest_ts"] = self.newest_ts.isoformat() if self.newest_ts else None
        return row


@dataclass(frozen=True)
class LagRow:
    ticker: str
    bar_ts: datetime
    seen_at: datetime
    lag_s: float
    session: str


@dataclass(frozen=True)
class MeasureResult:
    exit_code: int
    verdict: str
    gets: int
    jsonl_path: Path
    md_path: Path


def lag_rows(polls: list[PollRecord]) -> list[LagRow]:
    rows: list[LagRow] = []
    for ticker in dict.fromkeys(p.ticker for p in polls):
        previous: Optional[datetime] = None
        seen: set[datetime] = set()
        for p in polls:
            if p.ticker != ticker or p.newest_ts is None:
                continue
            if previous is not None and p.newest_ts != previous and p.newest_ts not in seen:
                rows.append(LagRow(ticker, p.newest_ts, p.at, (p.at - p.newest_ts).total_seconds(), p.session))
            seen.add(p.newest_ts)
            previous = p.newest_ts
    return rows


def percentile(values: list[float], q: float) -> float:
    """Nearest rank."""
    ordered = sorted(values)
    return ordered[max(0, math.ceil(q / 100 * len(ordered)) - 1)]


def verdict(*, cadence: int, criterion_s: int, failure: Optional[PollRecord], lags: list[LagRow],
            windows_run: list[str]) -> str:
    if failure is not None:
        if failure.status is None or failure.status in THROTTLE_STATUSES:
            return f"THROTTLED at {cadence} s — Charter re-rule: 10 s cadence (~8 s)"
        return f"NOT MET — {failure.session.upper()} GET failed ({failure.status}: {failure.error})"
    run = [s.value for s in ACTIVE if s.value in windows_run]
    if not run:
        return "NOT MET — no PREMARKET or RTH poll"
    for window in run:
        values = [row.lag_s for row in lags if row.session == window]
        if not values:
            return f"NOT MET — {window.upper()} p95 none (no bar transitions)"
        p95 = percentile(values, 95)
        if p95 > criterion_s:
            return f"NOT MET — {window.upper()} p95 {p95:.1f} s"
    return f"CRITERION ≤{criterion_s} s HOLDS at {cadence} s"


def radar_planned_rpm() -> Optional[float]:
    """The radar's planned steady rpm from its notes (read, never written)."""
    from cobalt.radar.notes import configured_sources

    return configured_sources().planned_rpm


def _ceiling() -> Optional[int]:
    from cobalt.taxonomy.loader import load_tunables

    raw = load_tunables().by_key["radar.finviz_max_rpm"].value
    return None if raw is None else int(raw)


def minimum_cadence(names: int, planned_rpm: float, ceiling: int, floor_s: int) -> Optional[int]:
    headroom = ceiling - planned_rpm
    if headroom <= 0:
        return None
    return max(floor_s, math.ceil(names * 60 / headroom))


def preflight(names: list[str], cadence: int, *, settings: StrikeSettings,
              planned_rpm: Callable[[], Optional[float]]) -> float:
    """Every refusal, before the first GET. Returns the run's rpm."""
    from cobalt.radar.notes import DemandConsumer, TotalDemandExceeded, check_scheduled_demand, radar_window

    if not names:
        raise MeasureRefused("no names given")
    if len(names) > settings.max_armed:
        raise MeasureRefused(f"{len(names)} names: at most {settings.max_armed} (strike.max_armed)")
    if cadence < settings.poll_interval_min:
        raise MeasureRefused(f"cadence {cadence} s is below strike.poll_interval_min {settings.poll_interval_min} s")
    try:
        planned = planned_rpm()
    except Exception as e:
        raise MeasureRefused(f"the radar's planned rpm is unreadable: {scrub(str(e))}") from e
    if planned is None:
        raise MeasureRefused("the radar's planned rpm is unreadable (its sources are not planned)")
    rpm = len(names) * 60 / cadence
    consumer = DemandConsumer(name="strike-measure", rpm=rpm, window=radar_window(),
                              basis=f"{len(names)} names x 60 / {cadence} s")
    try:
        check_scheduled_demand("strike-measure", radar_rpm=planned, extra=[consumer])
    except TotalDemandExceeded as e:
        ceiling = _ceiling()
        least = None if ceiling is None else minimum_cadence(len(names), planned, ceiling, settings.poll_interval_min)
        named = (f"minimum cadence {least} s for {len(names)} names" if least is not None
                 else "no cadence fits: the radar leaves no headroom")
        raise MeasureRefused(f"{e}; {named}") from e
    return rpm


async def run_measure(
    names: list[str],
    cadence: int,
    minutes: int,
    out: Path,
    *,
    fetch: Callable[..., Awaitable[list]] = fetch_bars,
    token_source: Callable[[], Awaitable[str]] = resolve_token,
    now: Callable[[], datetime] = clock_mod.now_utc,
    monotonic: Callable[[], float] = time.monotonic,
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep,
    planned_rpm: Callable[[], Optional[float]] = radar_planned_rpm,
    session_of: Optional[Callable[[datetime], Session]] = None,
    settings: Optional[StrikeSettings] = None,
) -> MeasureResult:
    from cobalt.radar.collector import TokenBucket

    settings = settings or check()
    names = [n.strip().upper() for n in names if n.strip()]
    rpm = preflight(names, cadence, settings=settings, planned_rpm=planned_rpm)
    if session_of is None:
        from cobalt.session import session_clock

        session_of = session_clock().session
    cap = len(names) * math.ceil(minutes * 60 / cadence)
    token = await token_source()
    bucket = TokenBucket(rpm, monotonic=monotonic, sleep=sleep)

    started_at = now()
    day = started_at.astimezone(ET).date().isoformat()
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    jsonl_path = out / f"strike-measure-{day}.jsonl"
    md_path = out / f"strike-measure-{day}.md"
    deadline = monotonic() + minutes * 60
    polls: list[PollRecord] = []
    failure: Optional[PollRecord] = None
    with jsonl_path.open("a", encoding="utf-8") as sink:
        while len(polls) < cap and monotonic() < deadline and failure is None:
            cycle_started = monotonic()
            session = session_of(now())
            if session not in ACTIVE:
                await sleep(cadence)
                continue
            for ticker in names:
                if len(polls) >= cap:
                    break
                await bucket.acquire()
                metrics: list = []
                t0 = monotonic()
                bars, error = None, None
                try:
                    bars = await fetch(ticker, Interval.I1, token, on_metrics=metrics.append)
                except Exception as e:
                    error = scrub(str(e))
                status = metrics[-1].status if metrics else None
                record = PollRecord(
                    at=now(), ticker=ticker, status=status,
                    fetch_ms=metrics[-1].elapsed_ms if metrics else (monotonic() - t0) * 1000,
                    newest_ts=max((b.ts for b in bars), default=None) if bars else None,
                    session=session.value, error=error,
                )
                polls.append(record)
                sink.write(json.dumps(record.as_json()) + "\n")
                if error is not None or status != 200:
                    failure = record
                    break
            if failure is None:
                await sleep(max(0.0, cadence - (monotonic() - cycle_started)))

    lags = lag_rows(polls)
    windows_run = sorted({p.session for p in polls})
    line = verdict(cadence=cadence, criterion_s=settings.alert_criterion_s, failure=failure, lags=lags,
                   windows_run=windows_run)
    md_path.write_text(_summary(names, cadence, minutes, started_at, polls, lags, failure, line), encoding="utf-8")
    return MeasureResult(exit_code=1 if failure else 0, verdict=line, gets=len(polls),
                         jsonl_path=jsonl_path, md_path=md_path)


def _stats(values: list[float]) -> str:
    if not values:
        return "n 0"
    return (f"n {len(values)} · p50 {percentile(values, 50):.1f} · p95 {percentile(values, 95):.1f} · "
            f"max {max(values):.1f}")


def _summary(names, cadence, minutes, started_at, polls, lags, failure, line) -> str:
    out = [
        f"# strike measure — {started_at.astimezone(ET):%Y-%m-%d %H:%M:%S} ET",
        "",
        f"names {','.join(names)} · cadence {cadence} s · minutes {minutes} · GETs {len(polls)}",
        "",
    ]
    for window in (s.value for s in ACTIVE):
        rows = [p for p in polls if p.session == window]
        if not rows:
            continue
        statuses: dict[str, int] = {}
        for p in rows:
            key = str(p.status) if p.status is not None else f"none ({p.error})"
            statuses[key] = statuses.get(key, 0) + 1
        out += [
            f"## {window.upper()}",
            f"- GETs {len(rows)} · HTTP {', '.join(f'{k}×{v}' for k, v in sorted(statuses.items()))}",
            f"- fetch ms {_stats([p.fetch_ms for p in rows])}",
            f"- lag s {_stats([r.lag_s for r in lags if r.session == window])}",
            "",
        ]
    if failure is not None:
        out += [f"stopped at the first failure: {failure.ticker} {failure.status} {failure.error}", ""]
    out.append(line)
    return "\n".join(out) + "\n"


def command(args) -> None:
    names = [n for n in str(args.names).split(",") if n.strip()]
    try:
        result = asyncio.run(run_measure(names, int(args.cadence), int(args.minutes), Path(args.out)))
    except MeasureRefused as e:
        print(f"REFUSED: {e}")
        sys.exit(2)
    print(f"GETs {result.gets} · {result.jsonl_path} · {result.md_path}")
    print(result.verdict)
    if result.exit_code:
        sys.exit(result.exit_code)


__all__ = ["LagRow", "MeasureRefused", "MeasureResult", "PollRecord", "command", "lag_rows", "minimum_cadence",
           "percentile", "preflight", "run_measure", "verdict"]
