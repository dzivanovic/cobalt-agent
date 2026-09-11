"""Rank-ordered radar member polling with overlap and freshness state."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Awaitable, Callable

from cobalt.archiver.collector import fetch_bars, scrub
from cobalt.archiver.models import Bar, Interval
from cobalt.archiver.store import BarStore
from cobalt.session.models import Session

from .collector import TokenBucket


@dataclass(frozen=True)
class PollMember:
    ticker: str
    rank: int


@dataclass(frozen=True)
class PollFailure:
    ticker: str
    reason: str
    since: datetime


@dataclass
class PollResult:
    failures: list[PollFailure]
    written: dict[str, int]
    stopped_at: str | None = None


class BarPoller:
    def __init__(
        self,
        token: str,
        *,
        store: BarStore | None = None,
        bucket: TokenBucket,
        overlap_bars: int,
        max_age_s: int,
        fetch: Callable[..., Awaitable[list[Bar]]] = fetch_bars,
    ):
        self.token = token
        self.store = store or BarStore()
        self.bucket = bucket
        self.overlap_bars = overlap_bars
        self.max_age_s = max_age_s
        self.fetch = fetch

    async def poll(
        self,
        members: list[PollMember],
        *,
        now: datetime,
        session: Session,
        existing_failures: list[PollFailure] | None = None,
        before_commit: Callable[[str], Callable[[], None] | None] | None = None,
    ) -> PollResult:
        failures = {(item.ticker, item.reason): item for item in existing_failures or []}
        written: dict[str, int] = {}
        stopped_at: str | None = None
        for member in sorted(members, key=lambda item: (item.rank, item.ticker)):
            ticker = member.ticker
            try:
                await self.bucket.acquire()
                bars = await self.fetch(ticker, Interval.I1, self.token)
            except Exception as e:
                # Details are logged by the runner after collector.scrub; the row
                # intentionally carries only the ruled reason and onset.
                scrub(str(e))
                failures.setdefault((ticker, "error"), PollFailure(ticker, "error", now))
                stopped_at = ticker
                continue
            watermark = self.store.watermark(ticker, Interval.I1.value)
            threshold = watermark - timedelta(minutes=self.overlap_bars) if watermark else None
            closed = [
                bar for bar in bars
                if bar.ts + timedelta(minutes=1) <= now
                and (threshold is None or bar.ts > threshold)
            ]
            hook = before_commit(ticker) if before_commit else None
            try:
                written[ticker] = self.store.upsert_bars(closed, before_commit=hook)
            except BaseException as e:
                # A session-gate exception is a transaction boundary, not a
                # member failure.  It must reach the runner so every remaining
                # ticker and later stage is skipped.
                if type(e).__name__ == "StageDropped":
                    raise
                scrub(str(e))
                failures.setdefault((ticker, "error"), PollFailure(ticker, "error", now))
                stopped_at = ticker
                continue
            failures.pop((ticker, "error"), None)
            newest = max(
                [bar.ts for bar in closed] + ([watermark] if watermark else []),
                default=None,
            )
            if session is Session.RTH and (newest is None or now - newest > timedelta(seconds=self.max_age_s)):
                failures.setdefault((ticker, "stale"), PollFailure(ticker, "stale", now))
            else:
                failures.pop((ticker, "stale"), None)
        return PollResult(
            failures=sorted(failures.values(), key=lambda item: (item.ticker, item.reason)),
            written=written,
            stopped_at=stopped_at,
        )


__all__ = ["BarPoller", "PollFailure", "PollMember", "PollResult"]
