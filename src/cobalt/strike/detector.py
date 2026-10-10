"""The strike detector — one tick (S4-P1 C2) and the MISSED sweep (C3).

ONE SEAM: every move is `CardStore.transition()` — ARMED → TRIGGERED on a
cross of an ARMED radar card, WATCH → MISSED (`models.MISSED_EDGE`, with a
reason) on a cross of a WATCH radar card — `actor=cobalt`, the CONTRACT
below as evidence. No other edge, no other write path.

A TICK, only in PREMARKET or RTH:
1. read the WATCH and ARMED radar cards (`CardStore.strike_cards`; manual
   cards are not watched, DECISION D6);
2. every `strike.missed_sweep_interval`: the MISSED sweep over the WATCH
   cards, on the i1 bars the radar poller already stored (no GET), from the
   card's `created_at`; then the radar's plan is read again;
3. keep the first `strike.max_armed` ARMED cards by the `at` of their latest
   ARMED transition (DECISION D4); every card left out is logged by name;
4. THE INTERVAL (DECISION D2): `poll_interval(names, headroom_rpm, floor_s)
   = max(floor_s, ⌈names × 60 / headroom_rpm⌉)`, the headroom being
   `radar.finviz_max_rpm` less the radar's planned rpm; the strike demand,
   names × 60 / interval rpm, is counted as one more consumer by
   `check_scheduled_demand("strike", …)`. A refusal, an unreadable plan or
   no headroom → logged loud, no GET this tick;
5. one fetch per kept card through this thread's own `TokenBucket` at its
   counted share (DECISION D8), `crossed(policy, …, since = armed at)`; a
   cross → TRIGGERED. A refused move (`IllegalTransition`, `CardStateError`,
   the F1 `SessionBlocked`) is logged and skipped, never retried in the tick;
   a fetch failure is logged scrubbed and the card is fetched again next tick.

The card's def is the def NOW loaded for its slug: when its md5 differs from
the card's `trade_def_md5` the current policy is used and both md5s are in
the evidence. A sequence trigger or no policy → `unwatchable`, logged once
per card (DECISION D5).

CONTRACT (the seam S4-P2 reads; `docs/40 - DevDocs/cobalt/strike/detector.md`
`## CONTRACT`): the evidence keys, in this order, `CONTRACT_KEYS`.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from typing import Any, Awaitable, Callable, Optional

from loguru import logger

from cobalt.archiver.collector import scrub
from cobalt.archiver.models import Interval
from cobalt.cards.models import Actor, CardState, IllegalTransition
from cobalt.radar.collector import TokenBucket
from cobalt.radar.notes import RadarNoteError, TotalDemand
from cobalt.session.models import Session

from .config import StrikeSettings
from .policy import Cross, Unwatchable, crossed, policy_of

ACTIVE = (Session.PREMARKET, Session.RTH)
VIA_TRIGGERED = "strike.detector"
VIA_MISSED = "strike.missed"
CONTRACT_KEYS = (
    "via", "policy", "entry", "cross_price", "bar_ts", "bar_close_at", "seen_at", "cadence_s", "def_md5",
    "card_def_md5",
)


@dataclass(frozen=True)
class StrikeCard:
    card_id: int
    ticker: str
    direction: str
    state: str
    trade_def_slug: Optional[str]
    trade_def_md5: Optional[str]
    entry: Optional[Decimal]
    created_at: datetime
    armed_at: Optional[datetime]


@dataclass(frozen=True)
class DemandPlan:
    """The radar's planned steady rpm and the headroom it leaves under
    `radar.finviz_max_rpm`; None = unreadable."""

    planned_rpm: Optional[float]
    headroom_rpm: Optional[float]


@dataclass
class TickReport:
    state: str
    interval_s: Optional[int] = None
    fetched: list[str] = field(default_factory=list)
    triggered: list[int] = field(default_factory=list)
    missed: list[int] = field(default_factory=list)
    left_out: list[int] = field(default_factory=list)
    refused: Optional[str] = None


class IntervalRefused(RuntimeError):
    """No interval exists: the radar leaves no headroom, or it is unreadable."""


def poll_interval(names: int, headroom_rpm: Optional[float], floor_s: int) -> int:
    if headroom_rpm is None or headroom_rpm <= 0:
        raise IntervalRefused(f"no Finviz headroom for the strike loop (headroom_rpm={headroom_rpm})")
    if names <= 0:
        return floor_s
    return max(floor_s, math.ceil(names * 60 / headroom_rpm))


def check_strike_demand(names: int, interval_s: int, planned_rpm: Optional[float]) -> TotalDemand:
    """The strike loop as one more consumer of the ONE shared ceiling (L53)."""
    from cobalt.radar.notes import DemandConsumer, check_scheduled_demand, radar_window

    consumer = DemandConsumer(name="strike", rpm=names * 60 / interval_s, window=radar_window(),
                              basis=f"{names} ARMED names x 60 / {interval_s} s")
    return check_scheduled_demand("strike", radar_rpm=planned_rpm, extra=[consumer])


def contract(*, via: str, cross: Cross, entry: Decimal, seen_at: datetime, cadence_s: int, def_md5: Optional[str],
             card_def_md5: Optional[str]) -> dict[str, Any]:
    values = {
        "via": via, "policy": cross.policy, "entry": str(entry), "cross_price": str(cross.cross_price),
        "bar_ts": cross.bar_ts.isoformat(), "bar_close_at": cross.bar_close_at.isoformat(),
        "seen_at": seen_at.isoformat(), "cadence_s": int(cadence_s), "def_md5": def_md5,
        "card_def_md5": card_def_md5,
    }
    return {key: values[key] for key in CONTRACT_KEYS}


class StrikeDetector:
    def __init__(
        self,
        *,
        store,
        fetch: Callable[..., Awaitable[list]],
        token: str,
        defs: Callable[[str], Optional[tuple[str, Any]]],
        stored_bars: Callable[[str, datetime, datetime], list],
        settings: StrikeSettings,
        plan: Callable[[], DemandPlan],
        session_of: Callable[[datetime], Session],
        now: Callable[[], datetime],
        bucket_factory: Callable[[float], TokenBucket] = TokenBucket,
    ):
        self.store = store
        self.fetch = fetch
        self.token = token
        self.defs = defs
        self.stored_bars = stored_bars
        self.settings = settings
        self.plan = plan
        self.session_of = session_of
        self.now = now
        self.bucket_factory = bucket_factory
        self._plan: Optional[DemandPlan] = None
        self._last_sweep: Optional[datetime] = None
        self._interval = settings.poll_interval_min
        self._bucket: Optional[TokenBucket] = None
        self._bucket_rpm: Optional[float] = None
        self._unwatchable: set[int] = set()

    def interval_s(self) -> int:
        """The last derived interval; the floor until one is derived."""
        return self._interval

    def _read_plan(self) -> DemandPlan:
        try:
            return self.plan()
        except Exception as e:
            logger.error("strike: the radar's plan is unreadable — no GET until it reads: {}", scrub(str(e)))
            return DemandPlan(planned_rpm=None, headroom_rpm=None)

    def _unwatchable_once(self, card: StrikeCard, reason: str) -> None:
        if card.card_id not in self._unwatchable:
            self._unwatchable.add(card.card_id)
            logger.warning("strike: unwatchable: card {} ({}) — {}", card.card_id, card.ticker, reason)

    def _resolve(self, card: StrikeCard):
        """(policy, def md5) for the def now loaded for the card's slug, or None (logged once)."""
        if card.entry is None:
            self._unwatchable_once(card, "no entry")
            return None
        if not card.trade_def_slug:
            self._unwatchable_once(card, "no trade_def slug")
            return None
        loaded = self.defs(card.trade_def_slug)
        if loaded is None:
            self._unwatchable_once(card, f"trade_def {card.trade_def_slug!r} is not loaded")
            return None
        md5, definition = loaded
        policy = policy_of(definition.trigger)
        if isinstance(policy, Unwatchable):
            self._unwatchable_once(card, policy.reason)
            return None
        return policy, md5

    def _move(self, card: StrikeCard, to: CardState, *, evidence, reason, now) -> bool:
        try:
            self.store.transition(card.card_id, to, actor=Actor.COBALT, evidence=evidence, reason=reason, now=now)
        except Exception as e:
            from cobalt.cards.store import CardStateError
            from cobalt.session import SessionBlocked

            if not isinstance(e, (IllegalTransition, CardStateError, SessionBlocked)):
                raise
            logger.warning("strike: {} refused for card {} ({}) — skipped: {}", to.value, card.card_id, card.ticker, e)
            return False
        return True

    def _sweep(self, watch: list[StrikeCard], now: datetime, report: TickReport) -> None:
        """C3: WATCH → MISSED on the radar's stored bars, from `created_at`."""
        for card in watch:
            resolved = self._resolve(card)
            if resolved is None:
                continue
            policy, md5 = resolved
            try:
                bars = self.stored_bars(card.ticker, card.created_at, now)
            except Exception as e:
                logger.warning("strike: stored bars unreadable for card {} ({}): {}", card.card_id, card.ticker,
                               scrub(str(e)))
                continue
            hit = crossed(policy, card.direction, card.entry, bars, since=card.created_at, now=now)
            if isinstance(hit, Unwatchable):
                self._unwatchable_once(card, hit.reason)
                continue
            if hit is None:
                continue
            evidence = contract(via=VIA_MISSED, cross=hit, entry=card.entry, seen_at=now,
                                cadence_s=self.settings.missed_sweep_interval, def_md5=md5,
                                card_def_md5=card.trade_def_md5)
            reason = f"trigger crossed while WATCH ({hit.policy}, bar {hit.bar_ts.isoformat()})"
            if self._move(card, CardState.MISSED, evidence=evidence, reason=reason, now=now):
                logger.info("strike: card {} ({}) MISSED — {}", card.card_id, card.ticker, reason)
                report.missed.append(card.card_id)

    async def tick(self) -> TickReport:
        now = self.now()
        session = self.session_of(now)
        if session not in ACTIVE:
            return TickReport(state=f"idle:{session.value}")
        report = TickReport(state="active")
        if self._plan is None:
            self._plan = self._read_plan()
        cards = self.store.strike_cards()

        due = self._last_sweep is None or (now - self._last_sweep).total_seconds() >= self.settings.missed_sweep_interval
        if due:
            self._sweep([c for c in cards if c.state == CardState.WATCH.value], now, report)
            self._last_sweep = now
            self._plan = self._read_plan()

        armed = sorted((c for c in cards if c.state == CardState.ARMED.value),
                       key=lambda c: (c.armed_at or c.created_at, c.card_id))
        kept, left = armed[: self.settings.max_armed], armed[self.settings.max_armed:]
        for card in left:
            logger.warning("strike: card {} ({}) left out — more than {} ARMED; armed at {}", card.card_id,
                           card.ticker, self.settings.max_armed, card.armed_at)
        report.left_out = [c.card_id for c in left]

        watched = []
        for card in kept:
            if card.armed_at is None:
                self._unwatchable_once(card, "ARMED with no ARMED transition")
                continue
            resolved = self._resolve(card)
            if resolved is not None:
                watched.append((card, *resolved))
        if not watched:
            return report

        try:
            interval = poll_interval(len(watched), self._plan.headroom_rpm, self.settings.poll_interval_min)
            check_strike_demand(len(watched), interval, self._plan.planned_rpm)
        except (IntervalRefused, RadarNoteError) as e:
            report.refused = str(e)
            logger.error("strike: no GET this tick — {}", e)
            return report
        self._interval = interval
        report.interval_s = interval
        rpm = len(watched) * 60 / interval
        if self._bucket is None or self._bucket_rpm != rpm:
            self._bucket, self._bucket_rpm = self.bucket_factory(rpm), rpm

        for card, policy, md5 in watched:
            await self._bucket.acquire()
            try:
                bars = await self.fetch(card.ticker, Interval.I1, self.token)
            except Exception as e:
                logger.warning("strike: fetch failed for card {} ({}) — fetched again next tick: {}", card.card_id,
                               card.ticker, scrub(str(e)))
                continue
            report.fetched.append(card.ticker)
            # `seen_at` is THIS poll's wall clock (the CONTRACT), not the tick's
            # start: the bucket wait and the fetch lie between them.
            seen = self.now()
            hit = crossed(policy, card.direction, card.entry, bars, since=card.armed_at, now=seen)
            if isinstance(hit, Unwatchable):
                self._unwatchable_once(card, hit.reason)
                continue
            if hit is None:
                continue
            evidence = contract(via=VIA_TRIGGERED, cross=hit, entry=card.entry, seen_at=seen, cadence_s=interval,
                                def_md5=md5, card_def_md5=card.trade_def_md5)
            if self._move(card, CardState.TRIGGERED, evidence=evidence, reason=None, now=seen):
                logger.info("strike: card {} ({}) TRIGGERED — {} bar {}", card.card_id, card.ticker, hit.policy,
                            hit.bar_ts.isoformat())
                report.triggered.append(card.card_id)
        return report


def read_plan() -> DemandPlan:
    """The radar's planned rpm and headroom, from its notes (read only)."""
    from cobalt.radar.notes import configured_sources

    parsed = configured_sources()
    demand = parsed.demand
    return DemandPlan(planned_rpm=parsed.planned_rpm, headroom_rpm=demand.headroom_rpm if demand else None)


async def build_detector() -> StrikeDetector:
    """The resident's detector: the real store, defs, bars, transport and clock."""
    from cobalt.archiver.collector import fetch_bars, resolve_token
    from cobalt.archiver.store import BarStore
    from cobalt.cards.store import CardStore
    from cobalt.session import clock as clock_mod
    from cobalt.session import session_clock
    from cobalt.taxonomy.store import TradeDefStore
    from cobalt.taxonomy.trade_def import TradeDef

    from .config import check

    settings = check()
    token = await resolve_token()
    defs_store, bar_store = TradeDefStore(), BarStore()

    def defs(slug: str):
        row = defs_store.get(slug)
        if row is None:
            return None
        return row["md5"], TradeDef.model_validate(row["def"])

    def stored_bars(ticker: str, start: datetime, end: datetime):
        return bar_store.bars_in_range(None, ticker, Interval.I1, start, end, as_bars=True)

    return StrikeDetector(
        store=CardStore(), fetch=fetch_bars, token=token, defs=defs, stored_bars=stored_bars, settings=settings,
        plan=read_plan, session_of=session_clock().session, now=clock_mod.now_utc,
    )


__all__ = [
    "CONTRACT_KEYS", "DemandPlan", "IntervalRefused", "StrikeCard", "StrikeDetector", "TickReport", "VIA_MISSED",
    "VIA_TRIGGERED", "build_detector", "check_strike_demand", "contract", "poll_interval", "read_plan",
]
