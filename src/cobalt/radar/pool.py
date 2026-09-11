"""Pure ranking and sticky hard-cap membership decision."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from enum import Enum
from typing import Iterable, Sequence
from zoneinfo import ZoneInfo

from pydantic import BaseModel, ConfigDict

from cobalt.session import session_clock

from .models import (
    Candidate,
    ExcludeBlock,
    ExcludedBy,
    OpenMember,
    PoolBlock,
    ScreenBlock,
    SourceHealth,
    SourceSet,
)

ET = ZoneInfo("America/New_York")


class Action(str, Enum):
    ADMIT = "admit"
    RETAIN = "retain"
    HOLD = "hold"
    LEAVE = "leave"
    EXCLUDE = "exclude"


class Transition(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ticker: str
    action: Action
    sources: list[str]
    source: str | None = None
    rank: int | None = None
    below_cap_streak: int = 0
    excluded_by: ExcludedBy | None = None
    rollover: bool = False
    left_at: datetime | None = None


class Decision(BaseModel):
    model_config = ConfigDict(extra="forbid")
    transitions: list[Transition]
    degraded: bool = False
    degraded_sources: list[str] = []
    frozen: bool = False


def _source_key(source: SourceSet) -> str:
    prefix = "screen:" if source.kind == "screen" else "list:"
    value = source.source
    if value.startswith(prefix):
        value = value[len(prefix):]
    return value.split("@", 1)[0]


def _blocks(
    blocks: PoolBlock | Sequence[object] | None,
) -> tuple[PoolBlock | None, dict[str, ScreenBlock], set[str]]:
    if isinstance(blocks, PoolBlock):
        return blocks, {}, set()
    items = list(blocks or [])
    pool = next((item for item in items if isinstance(item, PoolBlock)), None)
    screens = {item.screen: item for item in items if isinstance(item, ScreenBlock)}
    excluded = {
        ticker for item in items if isinstance(item, ExcludeBlock) for ticker in item.tickers
    }
    return pool, screens, excluded


def _metric_position(source: SourceSet, metric: str, ticker: str) -> int:
    values = source.metrics
    if values:
        ordered = sorted(
            source.tickers,
            key=lambda name: (
                values.get(name, {}).get(metric) is None,
                -(values.get(name, {}).get(metric) or 0),
                name,
            ),
        )
        return ordered.index(ticker) + 1 if ticker in ordered else 10**9
    return source.ranks.get(ticker, source.tickers.index(ticker) + 1 if ticker in source.tickers else 10**9)


def _ranked(
    candidates: dict[str, Candidate],
    pool: PoolBlock,
    sources: list[SourceSet],
    now: datetime,
) -> tuple[list[str], dict[str, int], dict[str, str]]:
    session = session_clock().session(now).value
    session_metric = getattr(pool.rank_metric, session)
    priority = {name: index for index, name in enumerate(pool.priority)}
    source_for: dict[str, str] = {}

    def key(ticker: str):
        carrying = [
            source for source in sources
            if source.active and source.health is SourceHealth.HEALTHY and ticker in source.tickers
        ]
        screen_sources = [source for source in carrying if source.kind == "screen"]
        group = "screens" if screen_sources else "lists"
        if screen_sources:
            positions = []
            for source in screen_sources:
                source_key = _source_key(source)
                override = pool.overrides.get(source_key)
                # ``model_copy(update=...)`` deliberately does not validate its
                # update payload, so callers constructing test/replay variants
                # can leave a JSON-shaped override here.  Keep the decision
                # boundary tolerant of either representation while the parsed
                # note path remains strictly validated by ``PoolBlock``.
                override_metric = (
                    override.get("rank_metric")
                    if isinstance(override, dict)
                    else getattr(override, "rank_metric", None)
                )
                first_from = (
                    override.get("first_from")
                    if isinstance(override, dict)
                    else getattr(override, "first_from", None)
                )
                metric = override_metric or session_metric
                first = 0 if first_from and now.astimezone(ET).strftime("%H:%M") >= first_from else 1
                positions.append(
                    (first, _metric_position(source, metric, ticker), source.note_order, source.source)
                )
            first, position, order, best_source = min(positions)
        else:
            first = 1
            list_sources = [source for source in carrying if source.kind == "list"]
            best_source = min((source.source for source in list_sources), default=candidates[ticker].sources[0] if candidates[ticker].sources else "")
            values = [source.metrics.get(ticker, {}).get(session_metric) for source in list_sources]
            value = max((v for v in values if v is not None), default=None)
            union = sorted(
                candidates,
                key=lambda name: (
                    max(
                        (
                            source.metrics.get(name, {}).get(session_metric)
                            for source in sources if source.kind == "list" and name in source.tickers
                        ),
                        default=None,
                    ) is None,
                    -(
                        max(
                            (
                                source.metrics.get(name, {}).get(session_metric)
                                for source in sources if source.kind == "list" and name in source.tickers
                                and source.metrics.get(name, {}).get(session_metric) is not None
                            ),
                            default=0,
                        )
                    ),
                    name,
                ),
            )
            position = union.index(ticker) + 1
            order = min((source.note_order for source in list_sources), default=10**9)
        source_for[ticker] = best_source
        return (priority[group], first if group == "screens" else 0, position, order, ticker)

    ordered = sorted(candidates, key=key)
    return ordered, {ticker: index + 1 for index, ticker in enumerate(ordered)}, source_for


def decide(
    candidates: Iterable[Candidate],
    open_members: Iterable[OpenMember],
    blocks: PoolBlock | Sequence[object] | None,
    sources: Iterable[SourceSet],
    now: datetime,
) -> Decision:
    """Implement D3's precedence table with provisional winners kept separate."""
    pool, screen_blocks, excluded = _blocks(blocks)
    source_rows = list(sources)
    episodes = {item.ticker: item for item in open_members}
    # Stickiness applies only to admitted episodes.  A never-admitted
    # episode is a record of a cap/filter exclusion, not a pool member.
    opens = {ticker: item for ticker, item in episodes.items() if item.entered_at is not None}
    never_admitted = {
        ticker: item for ticker, item in episodes.items() if item.entered_at is None
    }
    candidate_map = {item.ticker: item for item in candidates}
    degraded = [source.source for source in source_rows if source.health is SourceHealth.DEGRADED]
    if pool is None:
        return Decision(
            transitions=[],
            degraded=True,
            degraded_sources=["pool_block"],
            frozen=True,
        )

    transitions: list[Transition] = []
    today = now.astimezone(ET).date().isoformat()
    rollover = [item for item in episodes.values() if item.trade_date and str(item.trade_date) != today]
    for item in rollover:
        trade_day = item.trade_date if isinstance(item.trade_date, date) else date.fromisoformat(str(item.trade_date))
        close_at = datetime.combine(trade_day, time(20), tzinfo=ET)
        transitions.append(
            Transition(ticker=item.ticker, action=Action.LEAVE, sources=item.sources, rollover=True, left_at=close_at)
        )
        opens.pop(item.ticker, None)
        never_admitted.pop(item.ticker, None)
        candidate_map.pop(item.ticker, None)

    # Never-admitted episodes close as soon as the name stops being a
    # candidate.  If it is still excluded this scan, EXCLUDE below updates
    # that same episode; if it wins a seat, ADMIT closes it and opens an
    # admitted episode in the store.
    for ticker, item in list(never_admitted.items()):
        if ticker not in candidate_map:
            transitions.append(
                Transition(ticker=ticker, action=Action.LEAVE, sources=item.sources)
            )
            never_admitted.pop(ticker)

    active_sources = [s for s in source_rows if s.active and s.health is SourceHealth.HEALTHY]
    held: dict[str, OpenMember] = {}
    removed: set[str] = set()
    for ticker, member in list(opens.items()):
        if ticker in excluded:
            transitions.append(
                Transition(ticker=ticker, action=Action.LEAVE, sources=member.sources, excluded_by=ExcludedBy.MANUAL)
            )
            removed.add(ticker)
            continue
        source_refs = [s for s in source_rows if s.source in member.sources or ticker in s.tickers]
        if source_refs and all(not s.active for s in source_refs) and not any(ticker in s.tickers for s in active_sources):
            transitions.append(
                Transition(ticker=ticker, action=Action.LEAVE, sources=member.sources, excluded_by=ExcludedBy.SCREEN_INACTIVE)
            )
            removed.add(ticker)
            continue
        healthy_lists = any(ticker in s.tickers for s in active_sources)
        degraded_lists = any(ticker in s.tickers and s.health is SourceHealth.DEGRADED for s in source_rows)
        if not healthy_lists and degraded_lists:
            held[ticker] = member
            continue
    for ticker in removed:
        opens.pop(ticker, None)
        candidate_map.pop(ticker, None)

    for ticker in excluded:
        if ticker in candidate_map and ticker not in opens:
            item = candidate_map.pop(ticker)
            transitions.append(
                Transition(ticker=ticker, action=Action.EXCLUDE, sources=item.sources, excluded_by=ExcludedBy.MANUAL)
            )
    for ticker, item in list(candidate_map.items()):
        if item.excluded_by is not None:
            if ticker in opens:
                transitions.append(
                    Transition(ticker=ticker, action=Action.LEAVE, sources=opens[ticker].sources, excluded_by=item.excluded_by)
                )
                opens.pop(ticker)
            else:
                transitions.append(
                    Transition(ticker=ticker, action=Action.EXCLUDE, sources=item.sources, excluded_by=item.excluded_by)
                )
            candidate_map.pop(ticker)

    # If a lowered cap cannot fit held members, evict the worst prior ranks.
    if len(held) > pool.cap:
        worst = sorted(
            held.values(), key=lambda item: (item.last_rank is None, item.last_rank or 10**9, item.ticker), reverse=True
        )
        for member in worst[:len(held) - pool.cap]:
            held.pop(member.ticker)
            opens.pop(member.ticker, None)
            transitions.append(
                Transition(ticker=member.ticker, action=Action.LEAVE, sources=member.sources, excluded_by=ExcludedBy.CONFIG_CAP)
            )

    ranked_candidates = {
        ticker: item for ticker, item in candidate_map.items() if ticker not in held
    }
    ordered, ranks, source_for = _ranked(ranked_candidates, pool, source_rows, now)
    seats = max(0, pool.cap - len(held))
    winners = ordered[:seats]
    provisional = list(winners)

    retained_below: list[tuple[OpenMember, int, int | None]] = []
    for ticker, member in opens.items():
        if ticker in held:
            continue
        if ticker in provisional:
            transitions.append(
                Transition(
                    ticker=ticker, action=Action.RETAIN,
                    sources=candidate_map[ticker].sources, source=source_for.get(ticker),
                    rank=ranks[ticker], below_cap_streak=0,
                )
            )
            continue
        streak = member.below_cap_streak + 1
        if streak > pool.stickiness_scans:
            reason = ExcludedBy.CONFIG_CAP if ticker in candidate_map else None
            transitions.append(
                Transition(ticker=ticker, action=Action.LEAVE, sources=member.sources, rank=ranks.get(ticker), below_cap_streak=streak, excluded_by=reason)
            )
        else:
            retained_below.append((member, streak, ranks.get(ticker)))

    retained_below.sort(
        key=lambda item: (
            item[2] is None,
            item[2] if item[2] is not None else item[0].last_rank or 10**9,
            item[0].ticker,
        )
    )
    newcomers = {ticker for ticker in provisional if ticker not in opens}
    for member, streak, rank in retained_below:
        available = [ticker for ticker in provisional if ticker in newcomers]
        if not available:
            transitions.append(
                Transition(ticker=member.ticker, action=Action.LEAVE, sources=member.sources, rank=rank, below_cap_streak=streak, excluded_by=ExcludedBy.CONFIG_CAP if rank else None)
            )
            continue
        loser = max(available, key=lambda ticker: ranks[ticker])
        provisional[provisional.index(loser)] = member.ticker
        newcomers.remove(loser)
        transitions.append(
            Transition(ticker=member.ticker, action=Action.RETAIN, sources=candidate_map.get(member.ticker, Candidate(ticker=member.ticker, sources=member.sources)).sources, source=source_for.get(member.ticker), rank=rank, below_cap_streak=streak)
        )

    admitted = {t.ticker for t in transitions if t.action in {Action.RETAIN, Action.HOLD}}
    for ticker, member in held.items():
        transitions.append(
            Transition(ticker=ticker, action=Action.HOLD, sources=member.sources, rank=member.last_rank, below_cap_streak=member.below_cap_streak)
        )
        admitted.add(ticker)
    for ticker in provisional:
        if ticker not in opens:
            item = candidate_map[ticker]
            transitions.append(
                Transition(ticker=ticker, action=Action.ADMIT, sources=item.sources, source=source_for.get(ticker), rank=ranks[ticker])
            )
            admitted.add(ticker)
    for ticker in ordered:
        if ticker not in opens and ticker not in provisional:
            item = candidate_map[ticker]
            transitions.append(
                Transition(ticker=ticker, action=Action.EXCLUDE, sources=item.sources, source=source_for.get(ticker), rank=ranks[ticker], excluded_by=ExcludedBy.CONFIG_CAP)
            )

    if len(admitted) > pool.cap:
        raise AssertionError(f"pool cap violated: {len(admitted)} > {pool.cap}")
    return Decision(transitions=transitions, degraded=bool(degraded), degraded_sources=degraded)


__all__ = ["Action", "Decision", "Transition", "decide"]
