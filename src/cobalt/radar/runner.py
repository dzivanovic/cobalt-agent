"""Resident radar cycle: S1 membership, S2 pool, S3 mirror, S4 bars."""

from __future__ import annotations

import asyncio
import json
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, time as wall_time, timedelta, timezone
from pathlib import Path
from typing import Callable
from zoneinfo import ZoneInfo

from loguru import logger

from cobalt.archiver.collector import resolve_token, scrub
from cobalt.jobs.wrapper import job_run, should_keep_running
from cobalt.session import clock as clock_mod
from cobalt.session import session_clock
from cobalt.session.models import Session
from cobalt.settings.store import TraderSettingsStore
from cobalt.taxonomy.loader import load_tunables

from .collector import FinvizScreenerCollector, SourceFailure, process_bucket
from .config import RadarConfig, load_config
from .models import Candidate, ListBlock, OpenMember, ScreenBlock, SourceHealth, SourceSet
from .notes import ParsedSources, configured_sources, mirror_sources
from .poller import BarPoller, PollFailure, PollMember, PollResult
from .pool import Action, Decision, decide
from .store import RadarStore

JOB_LABEL = "com.cobalt.radar"
SCANNED = {Session.PREMARKET, Session.RTH, Session.AFTERMARKET}
ET = ZoneInfo("America/New_York")


class StageDropped(RuntimeError):
    """The clock crossed into market_reset before this transaction committed."""


def gate(stage: str, *, clock=None, now: Callable[[], datetime] = clock_mod.now_utc):
    resolved = clock or session_clock()

    def before_commit() -> None:
        if resolved.session(now()) is Session.MARKET_RESET:
            raise StageDropped(f"dropped at {stage}")

    return before_commit


@dataclass
class CycleResult:
    scan_id: int | None
    state: str
    decision: Decision | None = None
    failed_stage: str | None = None
    detail: str | None = None


class RadarRunner:
    def __init__(
        self,
        *,
        config: RadarConfig,
        sources_loader: Callable[[], ParsedSources],
        collector,
        radar_store: RadarStore,
        settings_store: TraderSettingsStore,
        poller: BarPoller,
        clock=None,
        now: Callable[[], datetime] = clock_mod.now_utc,
    ):
        self.config = config
        self.sources_loader = sources_loader
        self.collector = collector
        self.radar_store = radar_store
        self.settings_store = settings_store
        self.poller = poller
        self.clock = clock or session_clock()
        self.now = now

    async def _collect(
        self, parsed: ParsedSources, instant: datetime, open_rows: list[dict]
    ) -> tuple[list[Candidate], list[SourceSet]]:
        source_sets: list[SourceSet] = []
        candidates: dict[str, list[str]] = defaultdict(list)
        excluded: set[str] = set()
        blocks = parsed.screens.blocks + parsed.lists.blocks
        local_hhmm = instant.astimezone(self.clock.to_et(instant).tzinfo).strftime("%H:%M")
        for order, item in enumerate(blocks):
            block = item.block
            source_id: str | None = None
            snapshots = []
            try:
                if isinstance(block, ScreenBlock):
                    source_id = f"screen:{block.screen}@{item.sha256[:12]}"
                    active = block.enabled and block.active_from <= local_hhmm < block.active_to
                    if not active:
                        source_sets.append(SourceSet(source=source_id, kind="screen", active=False, note_order=order))
                        continue
                    snapshots = [await self.collector.screen(block, instant)]
                    kind = "screen"
                elif isinstance(block, ListBlock) and block.radar:
                    source_id = f"list:{block.list}@{item.sha256[:12]}"
                    if not block.enabled:
                        source_sets.append(SourceSet(source=source_id, kind="list", active=False, note_order=order))
                        continue
                    snapshots = await self.collector.listed(block, instant)
                    kind = "list"
                else:
                    continue
                tickers: list[str] = []
                metrics = {}
                for snapshot in snapshots:
                    for row in snapshot.rows:
                        ticker = row["Ticker"].strip().upper()
                        tickers.append(ticker)
                        metrics[ticker] = {
                            "volume": _number(row.get(self.config.export.metric_headers.volume)),
                            "rvol": _number(row.get(self.config.export.metric_headers.rvol)),
                        }
                        candidates[ticker].append(source_id)
                        if row.get(self.config.not_equity.header) in self.config.not_equity.values:
                            excluded.add(ticker)
                source_sets.append(
                    SourceSet(source=source_id, kind=kind, tickers=list(dict.fromkeys(tickers)), metrics=metrics, note_order=order)
                )
            except Exception as e:
                logger.error("radar source {} failed: {}", source_id, scrub(str(e)))
                held = [
                    row["ticker"] for row in open_rows
                    if source_id and any(str(value).startswith(source_id.split("@", 1)[0]) for value in row.get("sources", []))
                ]
                if source_id:
                    source_sets.append(
                        SourceSet(source=source_id, kind="screen" if source_id.startswith("screen:") else "list", health=SourceHealth.DEGRADED, tickers=held, note_order=order)
                    )
        from .models import ExcludedBy

        return [
            Candidate(
                ticker=ticker,
                sources=ids,
                excluded_by=ExcludedBy.NOT_EQUITY if ticker in excluded else None,
            )
            for ticker, ids in candidates.items()
        ], source_sets

    async def cycle(self) -> CycleResult:
        instant = self.now()
        session = self.clock.session(instant)
        if session is Session.MARKET_RESET:
            return CycleResult(None, "paused_market_reset")
        if session not in SCANNED:
            return CycleResult(None, f"idle:{session.value}")

        parsed = self.sources_loader()
        existing_pool = self.radar_store.pool_row(self.config.pool_key)
        epoch_ms = int(instant.timestamp() * 1000)
        last = int(existing_pool.get("last_scan_id") or 0) if existing_pool else 0
        scan_id = max(epoch_ms, last + 1)
        open_rows = self.radar_store.open_members(self.config.pool_key)
        opens = [OpenMember(**row) for row in open_rows]
        candidates, source_sets = await self._collect(parsed, instant, open_rows)
        decision = decide(candidates, opens, [item.block for item in parsed.screens.blocks + parsed.lists.blocks] if not parsed.frozen else None, source_sets, instant)
        elapsed_started = time.monotonic()

        # S1. Failure is named by S2, then the cycle stops.
        try:
            self.radar_store.apply_membership(
                pool_key=self.config.pool_key,
                transitions=decision.transitions,
                scan_id=scan_id,
                now=instant,
                session=session.value,
                before_commit=gate("membership", clock=self.clock, now=self.now),
            )
        except StageDropped as e:
            return CycleResult(scan_id, "dropped", decision, "membership", str(e))
        except Exception as e:
            detail = scrub(str(e))
            row = self._pool_row(parsed, decision, scan_id, instant, session, elapsed_started, open_rows)
            row.update(failed_stage="membership", failed_detail=detail, degraded=True)
            self.radar_store.put_pool(row, now=instant, before_commit=gate("pool_row", clock=self.clock, now=self.now))
            return CycleResult(scan_id, "failed", decision, "membership", detail)

        # S2.
        row = self._pool_row(parsed, decision, scan_id, instant, session, elapsed_started, open_rows)
        try:
            self.radar_store.put_pool(row, now=instant, before_commit=gate("pool_row", clock=self.clock, now=self.now))
        except Exception as e:
            return CycleResult(scan_id, "failed", decision, "pool_row", scrub(str(e)))

        # S3 failure is stamped and S4 still proceeds.
        mirror_failed = None
        try:
            mirror_sources(
                parsed,
                store=self.settings_store,
                before_commit=gate("mirror", clock=self.clock, now=self.now),
                now=instant,
            )
        except StageDropped as e:
            return CycleResult(scan_id, "dropped", decision, "mirror", str(e))
        except Exception as e:
            mirror_failed = scrub(str(e))
            self.radar_store.stamp_failure(
                self.config.pool_key, failed_stage="mirror", failed_detail=mirror_failed,
                now=instant, before_commit=gate("pool_row", clock=self.clock, now=self.now),
            )

        # S4: one transaction per admitted ticker; the poller keeps onset state.
        admitted = [
            PollMember(item.ticker, item.rank or 10**9)
            for item in decision.transitions if item.action in {Action.ADMIT, Action.RETAIN, Action.HOLD}
        ]
        if decision.frozen:
            admitted = [
                PollMember(row["ticker"], row.get("last_rank") or 10**9)
                for row in open_rows if row.get("entered_at") is not None
            ]
        existing_failures = [
            PollFailure(
                item["ticker"],
                item["reason"],
                item["since"] if isinstance(item["since"], datetime) else datetime.fromisoformat(item["since"]),
            )
            for item in (existing_pool or {}).get("poll_failures", [])
        ]
        try:
            poll = await self.poller.poll(
                admitted,
                now=instant,
                session=session,
                existing_failures=existing_failures,
                before_commit=lambda ticker: gate(f"bars:{ticker}", clock=self.clock, now=self.now),
            )
            self.radar_store.stamp_poll(
                self.config.pool_key,
                polled_at=instant,
                poll_failures=[
                    {"ticker": item.ticker, "reason": item.reason, "since": item.since.isoformat()}
                    for item in poll.failures
                ],
                before_commit=gate("bars:status", clock=self.clock, now=self.now),
            )
        except StageDropped as e:
            return CycleResult(scan_id, "dropped", decision, "bars", str(e))
        return CycleResult(scan_id, "scanning", decision, "mirror" if mirror_failed else None, mirror_failed)

    def _pool_row(self, parsed, decision, scan_id, instant, session, started, open_rows):
        admitted = (
            sum(row.get("entered_at") is not None for row in open_rows)
            if decision.frozen
            else sum(item.action in {Action.ADMIT, Action.RETAIN, Action.HOLD} for item in decision.transitions)
        )
        return {
            "pool_key": self.config.pool_key,
            "state": "scanning",
            "degraded": decision.degraded or parsed.frozen,
            "degraded_sources": [
                {"source": source, "reason": "source failure", "since": instant.isoformat()}
                for source in decision.degraded_sources
            ] + ([{"source": "pool_block", "reason": parsed.pool_error, "since": instant.isoformat()}] if parsed.pool_error else []),
            "failed_stage": None,
            "failed_detail": None,
            "sources": [source for source in decision.degraded_sources],
            "session": session.value,
            "cap": parsed.pool.cap if parsed.pool else None,
            "members": admitted,
            "last_scan_id": scan_id,
            "last_scan_at": instant,
            "last_scan_ms": int((time.monotonic() - started) * 1000),
            "last_poll_at": None,
            "poll_failures": [],
            "budget": {"planned_rpm": parsed.planned_rpm},
            "updated_at": instant,
        }


def _number(raw: str | None) -> float | None:
    if raw is None or not str(raw).strip() or str(raw).strip() == "-":
        return None
    text = str(raw).replace(",", "").replace("%", "").strip()
    try:
        return float(text)
    except ValueError:
        return None


async def build_runner() -> RadarRunner:
    config = load_config()
    tunables = load_tunables().by_key
    rpm = tunables["radar.finviz_max_rpm"].value
    if rpm is None:
        raise RuntimeError("radar.finviz_max_rpm is unmeasured; run throttle-probe")
    token = await resolve_token()
    bucket = process_bucket(int(rpm))
    return RadarRunner(
        config=config,
        sources_loader=configured_sources,
        collector=FinvizScreenerCollector(token, config=config, bucket=bucket),
        radar_store=RadarStore(),
        settings_store=TraderSettingsStore(),
        poller=BarPoller(
            token,
            bucket=bucket,
            overlap_bars=int(tunables["radar.poll_overlap_bars"].value),
            max_age_s=int(tunables["heartbeat.radar_max_age_s"].value),
        ),
    )


def run_command(_args) -> None:
    async def resident() -> None:
        runner = await build_runner()
        interval = int(load_tunables().by_key["radar.scan_interval"].value)
        while should_keep_running(JOB_LABEL):
            result = await runner.cycle()
            logger.info("radar cycle: {} scan_id={}", result.state, result.scan_id)
            await asyncio.sleep(interval)

    with job_run(JOB_LABEL) as run:
        asyncio.run(resident())
        run.result = {"stopped": True}


def scan_command(_args) -> None:
    if _args.replay:
        asyncio.run(_scan_replay(_args))
        return

    async def once():
        runner = await build_runner()
        return await runner.cycle()

    result = asyncio.run(once())
    print(f"{result.state} scan_id={result.scan_id}")


class _ReplayPoller:
    """Replay reads bars already in system.bars; it never calls Finviz."""

    async def poll(self, members, **_kwargs):
        return PollResult(failures=[], written={item.ticker: 0 for item in members})


def _parse_hhmm(raw: str, field: str) -> wall_time:
    try:
        return wall_time.fromisoformat(raw)
    except (TypeError, ValueError) as e:
        raise ValueError(f"replay {field} must be HH:MM, got {raw!r}") from e


async def _scan_replay(args) -> None:
    from .collector import ScreenerSnapshot
    from .replay import ReplayCollector

    if not args.from_time or not args.to_time:
        raise ValueError("replay scan requires --from HH:MM and --to HH:MM")
    trade_day = date.fromisoformat(args.replay)
    start = datetime.combine(trade_day, _parse_hhmm(args.from_time, "--from"), ET)
    stop = datetime.combine(trade_day, _parse_hhmm(args.to_time, "--to"), ET)
    if stop < start:
        raise ValueError("replay --to must not precede --from")
    path = Path("data/radar-replay") / f"{trade_day.isoformat()}.json"
    if not path.exists():
        raise ValueError(f"replay snapshot missing: {path}; run cobalt radar replay-build {trade_day}")
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
        snapshots = [
            ScreenerSnapshot(
                source="screen-replay",
                at=datetime.fromisoformat(item["at"]),
                rows=tuple(item["rows"]),
                header=("Ticker", "Volume", "Relative Volume"),
            )
            for item in raw
        ]
    except (OSError, ValueError, KeyError, TypeError) as e:
        raise ValueError(f"invalid replay snapshot {path}: {e}") from e
    virtual = [start.astimezone(timezone.utc)]
    runner = RadarRunner(
        config=load_config(),
        sources_loader=configured_sources,
        collector=ReplayCollector(snapshots),
        radar_store=RadarStore(),
        settings_store=TraderSettingsStore(),
        poller=_ReplayPoller(),
        now=lambda: virtual[0],
    )
    interval = int(load_tunables().by_key["radar.scan_interval"].value)
    counts = {"cycles": 0, "admit": 0, "leave": 0}
    while virtual[0] <= stop.astimezone(timezone.utc):
        result = await runner.cycle()
        counts["cycles"] += 1
        if result.decision:
            counts["admit"] += sum(item.action is Action.ADMIT for item in result.decision.transitions)
            counts["leave"] += sum(item.action is Action.LEAVE for item in result.decision.transitions)
        virtual[0] += timedelta(seconds=interval)
    print(
        f"replay {trade_day}: cycles={counts['cycles']} "
        f"admit={counts['admit']} leave={counts['leave']}"
    )


__all__ = ["CycleResult", "RadarRunner", "StageDropped", "gate"]
