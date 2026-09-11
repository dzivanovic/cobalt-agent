"""Deterministic replay snapshots synthesized from archived bars."""

from __future__ import annotations

import json
from collections import defaultdict
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo

from cobalt.archiver.models import Bar

from .collector import ScreenerSnapshot
from .models import ListBlock, ScreenBlock

ET = ZoneInfo("America/New_York")
SUPPORTED_FILTERS = frozenset({"exch_nasd", "sh_avgvol_o500"})


def snapshots_from_bars(
    bars: Iterable[Bar],
    screen: ScreenBlock,
    prior_sessions: int,
) -> list[ScreenerSnapshot]:
    """Build minute snapshots with a named replay-only RVOL proxy."""
    codes = set(screen.f.split(","))
    unknown = sorted(codes - SUPPORTED_FILTERS)
    if unknown:
        raise ValueError(f"replay does not implement fixture filter code(s) {unknown}")
    if prior_sessions < 1:
        raise ValueError("prior_sessions must be at least 1")

    grouped: dict[tuple[str, date], list[Bar]] = defaultdict(list)
    for bar in bars:
        grouped[(bar.ticker, bar.ts.astimezone(ET).date())].append(bar)
    days = sorted({day for _, day in grouped})
    if len(days) <= prior_sessions:
        raise ValueError(
            f"replay needs a target day after {prior_sessions} prior sessions; found {len(days)} days"
        )
    target = days[-1]
    histories = days[-prior_sessions - 1:-1]
    target_by_ticker = {
        ticker: sorted(values, key=lambda bar: bar.ts)
        for (ticker, day), values in grouped.items() if day == target
    }
    cumulative_history: dict[tuple[str, time], list[int]] = defaultdict(list)
    for ticker in target_by_ticker:
        for day in histories:
            total = 0
            for bar in sorted(grouped.get((ticker, day), []), key=lambda item: item.ts):
                total += bar.volume
                cumulative_history[(ticker, bar.ts.astimezone(ET).time().replace(tzinfo=None))].append(total)

    instants = sorted({bar.ts for values in target_by_ticker.values() for bar in values})
    running = defaultdict(int)
    output: list[ScreenerSnapshot] = []
    for instant in instants:
        rows: list[dict[str, str]] = []
        for ticker, ticker_bars in target_by_ticker.items():
            at_minute = [bar for bar in ticker_bars if bar.ts == instant]
            if at_minute:
                running[ticker] += at_minute[0].volume
            if not running[ticker]:
                continue
            wall = instant.astimezone(ET).time().replace(tzinfo=None)
            priors = cumulative_history.get((ticker, wall), [])
            mean = sum(priors) / len(priors) if priors else 0
            rvol = running[ticker] / mean if mean else 0
            rows.append(
                {"Ticker": ticker, "Volume": str(running[ticker]), "Relative Volume": f"{rvol:.6f}"}
            )
        rows.sort(key=lambda row: (-int(row["Volume"]), row["Ticker"]))
        output.append(
            ScreenerSnapshot(
                source=f"screen-{screen.screen}",
                at=instant,
                rows=tuple(rows),
                header=("Ticker", "Volume", "Relative Volume"),
            )
        )
    return output


class ReplayCollector:
    def __init__(self, snapshots: list[ScreenerSnapshot]):
        self.snapshots = sorted(snapshots, key=lambda item: item.at)

    async def screen(self, block: ScreenBlock, now: datetime) -> ScreenerSnapshot:
        eligible = [item for item in self.snapshots if item.at <= now]
        if not eligible:
            raise ValueError(f"no replay snapshot at or before {now.isoformat()}")
        return eligible[-1]

    async def listed(self, block: ListBlock, now: datetime) -> list[ScreenerSnapshot]:
        snapshot = await self.screen(
            ScreenBlock(
                screen=f"replay_list_{block.list}",
                f="exch_nasd",
                sort="-volume",
                columns=[0],
                active_from="00:00",
                active_to="23:59",
                enabled=True,
            ),
            now,
        )
        wanted = set(block.tickers)
        return [
            ScreenerSnapshot(
                source=f"list-{block.list}",
                at=snapshot.at,
                rows=tuple(row for row in snapshot.rows if row.get("Ticker") in wanted),
                header=snapshot.header,
            )
        ]


def replay_build_command(args) -> None:
    """Hub-only DB reader: store synthesized snapshots under gitignored data/."""
    from cobalt import db, env
    from cobalt.archiver.models import Interval
    from cobalt.db import Side
    from cobalt.radar.notes import configured_sources

    day = date.fromisoformat(args.day)
    sources = configured_sources()
    screen = next(
        item.block for item in sources.screens.blocks if item.key.startswith("screen.")
    )
    conn = db.connect(env.resolve_db_name(), side=Side.SYSTEM)
    try:
        rows = conn.execute(
            "SELECT ticker, interval, ts, open, high, low, close, volume "
            "FROM system.bars WHERE interval = 'i1' AND ts >= %s AND ts < %s ORDER BY ts",
            (day - timedelta(days=14), day + timedelta(days=1)),
        ).fetchall()
    finally:
        conn.close()
    bars = [
        Bar(ticker=r[0], interval=Interval(r[1]), ts=r[2], open=r[3], high=r[4], low=r[5], close=r[6], volume=r[7])
        for r in rows
    ]
    snapshots = snapshots_from_bars(bars, screen, prior_sessions=5)
    target = Path("data/radar-replay") / f"{day.isoformat()}.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(
            [{"at": s.at.isoformat(), "rows": list(s.rows)} for s in snapshots],
            sort_keys=True,
        ) + "\n",
        encoding="utf-8",
    )
    print(target)


__all__ = ["ReplayCollector", "snapshots_from_bars"]
