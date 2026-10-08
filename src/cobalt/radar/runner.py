"""Resident radar cycle: S1 membership, S2 pool, S3 mirror, S4 bars."""

from __future__ import annotations

import asyncio
import json
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, time as wall_time, timedelta, timezone
from decimal import Decimal, InvalidOperation
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
from .config import RadarConfig, is_not_equity, load_config
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
        evaluator=None,
        ceiling_rpm: int | None = None,
        card_store=None,
    ):
        # S5 (S2-P2 R1). `build_runner` always wires the stage; `None` is
        # the S1-S4-only shape the pre-S5 tests and the membership replay
        # tool construct, stated at their call sites.
        self.evaluator = evaluator
        if evaluator is not None and ceiling_rpm is None:
            raise ValueError("S5 needs radar.finviz_max_rpm to bound lifecycle polling (L53)")
        self.ceiling_rpm = ceiling_rpm
        self.config = config
        self.sources_loader = sources_loader
        self.collector = collector
        self.radar_store = radar_store
        self.settings_store = settings_store
        self.poller = poller
        self.clock = clock or session_clock()
        self.now = now
        # A reset crossing cannot be written durably at the instant it is
        # detected: the defining invariant is that nothing commits during
        # market_reset.  Keep the failure on the resident runner until the
        # next active cycle can put it on radar_pool.
        self._pending_drop: tuple[str, str] | None = None
        # R692 F3: `build_runner` hands the S5 stage's CardStore here; `None`
        # (the replay tool, the pre-floor tests) reads and moves no card.
        self.card_store = card_store
        # R692 F1: the last `_collect`'s floored tickers and their lowest
        # readable price, read by `cycle()` for the WATCH expiry.
        self._floored: dict[str, Decimal] = {}
        # (ET day, ticker) already logged with no readable price.
        self._price_unknown: set[tuple[date, str]] = set()

    def _dropped(self, scan_id: int, decision: Decision, stage: str, error: StageDropped) -> CycleResult:
        detail = scrub(str(error))
        self._pending_drop = (stage, detail)
        logger.error("radar cycle dropped at {}: {}", stage, detail)
        return CycleResult(scan_id, "dropped", decision, stage, detail)

    async def _collect(
        self, parsed: ParsedSources, instant: datetime, open_rows: list[dict]
    ) -> tuple[list[Candidate], list[SourceSet]]:
        source_sets: list[SourceSet] = []
        candidates: dict[str, list[str]] = defaultdict(list)
        excluded: set[str] = set()
        prices: dict[str, Decimal] = {}
        blocks = parsed.screens.blocks + parsed.lists.blocks
        et_now = self.clock.to_et(instant)
        local_hhmm = instant.astimezone(et_now.tzinfo).strftime("%H:%M")
        price_header = self.config.export.metric_headers.price
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
                source_prices: dict[str, Decimal] = {}
                for snapshot in snapshots:
                    for row in snapshot.rows:
                        ticker = row["Ticker"].strip().upper()
                        tickers.append(ticker)
                        metrics[ticker] = {
                            "volume": _number(row.get(self.config.export.metric_headers.volume)),
                            "rvol": _number(row.get(self.config.export.metric_headers.rvol)),
                            # Float handicap H1 (v3 §6 replay): stored inputs
                            # of the group verdict, in every receipt's pool_unit.
                            "float_m": _number(row.get(self.config.export.handicap_headers.float)),
                            "market_cap_m": _number(row.get(self.config.export.handicap_headers.market_cap)),
                            "price": _number(row.get(price_header)),
                        }
                        price = _price(row.get(price_header))
                        if price is None:
                            self._flag_price_unknown(et_now.date(), ticker, source_id)
                        elif ticker not in source_prices or price < source_prices[ticker]:
                            source_prices[ticker] = price
                        candidates[ticker].append(source_id)
                        if is_not_equity(row, self.config.not_equity):
                            excluded.add(ticker)
                source_sets.append(
                    SourceSet(source=source_id, kind=kind, tickers=list(dict.fromkeys(tickers)), metrics=metrics, note_order=order)
                )
                for ticker, price in source_prices.items():
                    if ticker not in prices or price < prices[ticker]:
                        prices[ticker] = price
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

        # R692 F1: the price floor, ONCE, after every source is gathered.
        # A ticker with any readable price at or below the floor in this
        # scan leaves every SourceSet (healthy and degraded `held` alike),
        # so `decide()` sees it in no list. F2: an ADMITTED member stays a
        # candidate carrying `price_floor`, so `decide()` emits its LEAVE
        # now; any other floored ticker is dropped.
        floor = self.config.price_floor
        floored = {ticker: price for ticker, price in prices.items() if price <= floor}
        if floored:
            for item in source_sets:
                removed = [ticker for ticker in item.tickers if ticker in floored]
                if not removed:
                    continue
                item.tickers = [ticker for ticker in item.tickers if ticker not in floored]
                item.metrics = {ticker: m for ticker, m in item.metrics.items() if ticker not in floored}
                logger.info("radar price floor {}: {} removed {} ({})", floor, item.source, len(removed), ", ".join(removed))
        admitted = {row["ticker"] for row in open_rows if row.get("entered_at") is not None}
        self._floored = floored

        def reason(ticker: str) -> ExcludedBy | None:
            if ticker in floored:
                return ExcludedBy.PRICE_FLOOR
            return ExcludedBy.NOT_EQUITY if ticker in excluded else None

        return [
            Candidate(ticker=ticker, sources=ids, excluded_by=reason(ticker))
            for ticker, ids in candidates.items()
            if ticker not in floored or ticker in admitted
        ], source_sets

    def _flag_price_unknown(self, day: date, ticker: str, source_id: str | None) -> None:
        """A row with no readable price is kept (unknown is not below the
        floor) and logged once per ticker per ET day."""
        if any(seen != day for seen, _ticker in self._price_unknown):
            self._price_unknown = {item for item in self._price_unknown if item[0] == day}
        if (day, ticker) in self._price_unknown:
            return
        self._price_unknown.add((day, ticker))
        logger.warning("radar price unknown: {} ({}) — kept", ticker, source_id)

    def _expire_floored(self, floored: dict[str, Decimal], scan_id: int) -> None:
        """R692 F3: WATCH -> EXPIRED for a radar card on a floored ticker.
        `open_radar_cards` reads `origin = 'radar'` only; ARMED, TRIGGERED
        and FILLED cards are never passed to `transition`."""
        from cobalt.cards.models import Actor, CardState, IllegalTransition

        for card in self.card_store.open_radar_cards():
            if card.state != "WATCH" or card.ticker not in floored:
                continue
            try:
                self.card_store.transition(
                    card.card_id, CardState.EXPIRED, actor=Actor.COBALT,
                    evidence={"via": "radar.price_floor", "price": str(floored[card.ticker]),
                              "floor": str(self.config.price_floor), "scan_id": scan_id},
                    reason="price floor",
                    before_commit=gate("price_floor:card", clock=self.clock, now=self.now),
                )
            except IllegalTransition as e:
                logger.warning("radar price floor expiry of card {} not applied: {}", card.card_id, e)

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
        floored = self._floored
        decision = decide(
            candidates, opens,
            [item.block for item in parsed.screens.blocks + parsed.lists.blocks] if not parsed.frozen else None,
            source_sets, instant, handicap_headers=self.config.export.handicap_headers,
        )
        elapsed_started = time.monotonic()
        pending_drop = self._pending_drop

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
            return self._dropped(scan_id, decision, "membership", e)
        except Exception as e:
            detail = scrub(str(e))
            row = self._pool_row(parsed, decision, scan_id, instant, session, elapsed_started, open_rows, existing_pool)
            row.update(failed_stage="membership", failed_detail=detail, degraded=True)
            self.radar_store.put_pool(row, now=instant, before_commit=gate("pool_row", clock=self.clock, now=self.now))
            return CycleResult(scan_id, "failed", decision, "membership", detail)

        # R692 F3: a radar WATCH card on a floored ticker expires; nothing
        # else moves. A failure is stamped and the cycle goes on.
        expiry_failed: str | None = None
        if self.card_store is not None and floored:
            try:
                self._expire_floored(floored, scan_id)
            except StageDropped as e:
                return self._dropped(scan_id, decision, "membership", e)
            except Exception as e:
                expiry_failed = scrub(f"price floor expiry failed: {type(e).__name__}: {e}")
                logger.error("radar {}", expiry_failed)

        # S2.
        row = self._pool_row(parsed, decision, scan_id, instant, session, elapsed_started, open_rows, existing_pool)
        if pending_drop is not None:
            row.update(failed_stage=pending_drop[0], failed_detail=pending_drop[1])
        elif expiry_failed is not None:
            row.update(failed_stage="evaluate", failed_detail=expiry_failed)
        try:
            self.radar_store.put_pool(row, now=instant, before_commit=gate("pool_row", clock=self.clock, now=self.now))
        except StageDropped as e:
            return self._dropped(scan_id, decision, "pool_row", e)
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
            return self._dropped(scan_id, decision, "mirror", e)
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
        # Departed members with an open radar card keep being polled so the
        # card keeps its price/health/expiry coverage (Astra R1-15) — but
        # only inside the total Finviz demand ceiling (L53, R5).
        lifecycle_refusal: str | None = None
        if self.evaluator is not None:
            try:
                extra = self.evaluator.lifecycle_tickers([item.ticker for item in admitted])
            except Exception as e:
                extra = []
                lifecycle_refusal = f"lifecycle card read failed: {scrub(str(e))}"
            if extra:
                from .notes import lifecycle_poll_demand

                demand = lifecycle_poll_demand(
                    parsed.planned_rpm, len(extra),
                    scan_interval=int(load_tunables().by_key["radar.scan_interval"].value),
                    ceiling_rpm=int(self.ceiling_rpm),
                )
                if demand.refusal is None:
                    admitted = [*admitted, *(PollMember(ticker, 10**9) for ticker in extra)]
                else:
                    lifecycle_refusal = f"lifecycle polling refused for {extra}: {demand.refusal}"
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
            stamp_kwargs = {
                "polled_at": instant,
                "poll_failures": [
                    {"ticker": item.ticker, "reason": item.reason, "since": item.since.isoformat()}
                    for item in poll.failures
                ],
                "before_commit": gate("bars:status", clock=self.clock, now=self.now),
            }
            if pending_drop is not None:
                stamp_kwargs["preserve_failure"] = True
            self.radar_store.stamp_poll(self.config.pool_key, **stamp_kwargs)
        except StageDropped as e:
            return self._dropped(scan_id, decision, "bars", e)
        self._pending_drop = None
        failed_stage = (
            "mirror" if mirror_failed else pending_drop[0] if pending_drop else "evaluate" if expiry_failed else None
        )
        detail = mirror_failed if mirror_failed else pending_drop[1] if pending_drop else expiry_failed
        if lifecycle_refusal is not None:
            try:
                self.radar_store.stamp_failure(
                    self.config.pool_key, failed_stage="bars", failed_detail=lifecycle_refusal,
                    now=instant, before_commit=gate("bars:lifecycle", clock=self.clock, now=self.now),
                )
            except StageDropped as e:
                return self._dropped(scan_id, decision, "bars", e)
            logger.error("radar lifecycle polling: {}", lifecycle_refusal)
            failed_stage, detail = "bars", lifecycle_refusal

        # S5 evaluate, behind the same commit gate. A failure stamps
        # failed_stage='evaluate'; S1-S4 results stand.
        if self.evaluator is not None:
            from .anatomy.freshness import rvol_observations
            from .evaluate import EvaluateError

            pool_unit = {
                "pool_block": parsed.pool.model_dump(mode="json") if parsed.pool else None,
                "frozen": parsed.frozen,
                "source_sets": [item.model_dump(mode="json") for item in source_sets],
            }
            try:
                outcome = await self.evaluator.run(
                    pool_key=self.config.pool_key, scan_id=scan_id, session=session.value, instant=instant,
                    rvol=rvol_observations(source_sets, observed_at=instant), pool_unit=pool_unit,
                    gate=lambda label: gate(label, clock=self.clock, now=self.now),
                )
            except StageDropped as e:
                return self._dropped(scan_id, decision, "evaluate", e)
            except Exception as e:
                evaluate_detail = scrub(str(e)) if isinstance(e, EvaluateError) else scrub(f"{type(e).__name__}: {e}")
                logger.error("radar S5 evaluate FAILED: {}", evaluate_detail)
                try:
                    self.radar_store.stamp_failure(
                        self.config.pool_key, failed_stage="evaluate", failed_detail=evaluate_detail,
                        now=instant, before_commit=gate("evaluate:status", clock=self.clock, now=self.now),
                    )
                except StageDropped as dropped:
                    return self._dropped(scan_id, decision, "evaluate", dropped)
                return CycleResult(scan_id, "scanning", decision, "evaluate", evaluate_detail)
            if outcome.refusals:
                refusal = scrub("; ".join(outcome.refusals))[:500]
                logger.error("radar S5 card refusals: {}", refusal)
                try:
                    self.radar_store.stamp_failure(
                        self.config.pool_key, failed_stage="evaluate", failed_detail=refusal,
                        now=instant, before_commit=gate("evaluate:status", clock=self.clock, now=self.now),
                    )
                except StageDropped as e:
                    return self._dropped(scan_id, decision, "evaluate", e)
                return CycleResult(scan_id, "scanning", decision, "evaluate", refusal)
        return CycleResult(scan_id, "scanning", decision, failed_stage, detail)

    def _pool_row(self, parsed, decision, scan_id, instant, session, started, open_rows, existing_pool=None):
        # S2 carries S4's last outcome forward. Writing the row clean here and
        # re-stamping it at S4 ~70 s later made the heartbeat radar probe flap
        # on whichever side of that gap a beat sampled (cto-2026-09-15 §1.2).
        # Same strings as RadarStore.stamp_poll; later stages still override.
        carried = list((existing_pool or {}).get("poll_failures") or [])
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
                {"source": source, "reason": decision.reasons.get(source, "source failure"), "since": instant.isoformat()}
                for source in decision.degraded_sources
            ] + ([{"source": "pool_block", "reason": parsed.pool_error, "since": instant.isoformat()}] if parsed.pool_error else []),
            "failed_stage": "bars" if carried else None,
            "failed_detail": f"poll failures: {len(carried)}" if carried else None,
            "sources": [source for source in decision.degraded_sources],
            "session": session.value,
            "cap": parsed.pool.cap if parsed.pool else None,
            "members": admitted,
            "last_scan_id": scan_id,
            "last_scan_at": instant,
            "last_scan_ms": int((time.monotonic() - started) * 1000),
            "last_poll_at": None,
            "poll_failures": carried,
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


def _price(raw: str | None) -> Decimal | None:
    """The export's `Price` cell as the floor compares it (R692): `,` cut;
    None for blank, `-`, absent or unparseable — unknown, never below."""
    if raw is None:
        return None
    text = str(raw).replace(",", "").strip()
    if not text or text == "-":
        return None
    try:
        value = Decimal(text)
    except InvalidOperation:
        return None
    return value if value.is_finite() else None


async def build_runner() -> RadarRunner:
    config = load_config()
    tunables = load_tunables().by_key
    rpm = tunables["radar.finviz_max_rpm"].value
    if rpm is None:
        raise RuntimeError("radar.finviz_max_rpm is unmeasured; run throttle-probe")
    token = await resolve_token()
    bucket = process_bucket(int(rpm))
    from cobalt.cards.store import CardStore
    from cobalt.taxonomy.loader import load_defaults
    from cobalt.taxonomy.store import TradeDefStore

    from .collector import FinvizDailyBarsCollector
    from .evaluate import EvaluateStage

    settings_store = TraderSettingsStore()
    # ONE CardStore: S5 evaluates the cards, the price floor stage (R692 F3)
    # expires a floored ticker's WATCH card.
    card_store = CardStore()

    def rung(instant, daymode_cfg):
        from cobalt.daymode import DayModeStore, decided_or_stage1

        row = DayModeStore().for_date(session_clock().to_et(instant).date())
        return decided_or_stage1(row, daymode_cfg, now=instant)

    evaluator = EvaluateStage(
        rung_source=rung,
        radar_store=RadarStore(),
        card_store=card_store,
        defs_source=TradeDefStore().loaded_for_evaluation,
        settings_values=settings_store.values,  # re-read every cycle (plan §5)
        daily_source=FinvizDailyBarsCollector(token, config=config, bucket=bucket).daily,
        tunables_loader=lambda: load_tunables().by_key,
        defaults_loader=load_defaults,
        clock=session_clock(),
        now=clock_mod.now_utc,
    )
    return RadarRunner(
        evaluator=evaluator,
        card_store=card_store,
        ceiling_rpm=int(rpm),
        config=config,
        sources_loader=configured_sources,
        collector=FinvizScreenerCollector(token, config=config, bucket=bucket),
        radar_store=RadarStore(),
        settings_store=settings_store,
        poller=BarPoller(
            token,
            bucket=bucket,
            overlap_bars=int(tunables["radar.poll_overlap_bars"].value),
            max_age_s=int(tunables["radar.poll_bar_max_age_s"].value),
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
        # The S1-S4 membership replay tool: no S5. Evaluation replays with
        # `cobalt radar evaluate --replay` (writes nothing).
        evaluator=None,
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
    # v3 §3: replay-from-bars has no float or cap — it reports so and does not guess (R54's missing-header case stores factor 1).
    print(
        f"replay {trade_day}: cycles={counts['cycles']} "
        f"admit={counts['admit']} leave={counts['leave']} · handicap: not replayable from bars"
    )


__all__ = ["CycleResult", "RadarRunner", "StageDropped", "gate"]
