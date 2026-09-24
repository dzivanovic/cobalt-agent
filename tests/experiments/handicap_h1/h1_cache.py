"""The ONE cache reader (L3) the float-handicap H1 experiments and the
`handicap-dry-run` share.

It reads the retained screener exports `FinvizScreenerCollector._cache`
writes — `<cache.dir>/<UTC date>/<source>-<UTC HHMMSS>.csv`, where
`<source>` is `screen-<key>` or `list-<key>-<chunk>` — and groups them
into SCANS: every file of one cycle carries that cycle's instant, so one
scan is one `HHMMSS` of one day folder. Directories (`daily/`) are not
exports and are skipped; the nightly replay's mover exports, which
`replay/movers.py` writes into the same folder under its own name
(`movers-<side>-HHMMSS.csv`, matched by that module's `_CACHE_NAME`), are
counted apart and are not scans; any other FILE that fits no scan is a
loud `CacheGroupingError`, never a silently dropped export.

It never parses a cell itself. Each scan's `SourceSet` list is built by
`RadarRunner._collect` — the resident radar's own method, run over a
collector that serves the cached exports — so `_number`,
`is_not_equity` and the header config are the SAME calls production
makes (no second parser). A source the note names but the scan's cache
lacks raises `SourceFailure` inside `_collect`, exactly as a failed
fetch does (a failed fetch writes no cache file), and so degrades.

The replay carries open episodes forward from its own transitions, the
way `RadarStore.apply_membership` would record them; the first scan of
a replayed day starts empty.
"""

from __future__ import annotations

import asyncio
import re
from dataclasses import dataclass, field
from datetime import date, datetime, time, timezone
from pathlib import Path

from cobalt.radar.collector import ScreenerSnapshot, SourceFailure, parse_screener_csv
from cobalt.radar.config import RadarConfig
from cobalt.radar.models import Candidate, ListBlock, OpenMember, ScreenBlock, SourceSet
from cobalt.radar.notes import ParsedSources
from cobalt.radar.pool import Action, Transition

SCREEN_FILE = re.compile(r"^screen-(?P<key>[a-z0-9_]+)-(?P<at>\d{6})\.csv$")
LIST_FILE = re.compile(r"^list-(?P<key>[a-z0-9_]+)-(?P<chunk>[1-9]\d*)-(?P<at>\d{6})\.csv$")


class CacheGroupingError(RuntimeError):
    """A retained file fits no scan, or two files claim one source in one scan."""


@dataclass(frozen=True)
class CachedScan:
    """One radar cycle's retained exports: `files` maps `screen-<key>` /
    `list-<key>-<chunk>` to its CSV."""

    instant: datetime
    files: dict[str, Path] = field(default_factory=dict)


def mover_exports(day_dir: Path) -> list[Path]:
    """The replay's mover exports in one day folder — not radar scans."""
    from cobalt.replay.movers import _CACHE_NAME

    return [p for p in sorted(day_dir.iterdir()) if p.is_file() and _CACHE_NAME.match(p.name)]


def group_scans(day_dir: Path) -> list[CachedScan]:
    """Every retained radar export of one day folder, in exactly one scan."""
    day = date.fromisoformat(day_dir.name)
    movers = set(mover_exports(day_dir))
    by_at: dict[str, dict[str, Path]] = {}
    unmatched: list[str] = []
    for path in sorted(day_dir.iterdir()):
        if path.is_dir() or path in movers:
            continue
        matched = SCREEN_FILE.match(path.name) or LIST_FILE.match(path.name)
        if matched is None:
            unmatched.append(path.name)
            continue
        at = matched.group("at")
        source = path.name[: -len(f"-{at}.csv")]
        scan = by_at.setdefault(at, {})
        if source in scan:
            raise CacheGroupingError(f"{day_dir.name}: two files for {source} at {at}")
        scan[source] = path
    if unmatched:
        raise CacheGroupingError(
            f"{day_dir.name}: {len(unmatched)} file(s) fit no scan, first {unmatched[0]!r}"
        )
    return [
        CachedScan(
            datetime.combine(day, time(int(at[:2]), int(at[2:4]), int(at[4:])), tzinfo=timezone.utc),
            files,
        )
        for at, files in sorted(by_at.items())
    ]


class CacheCollector:
    """`FinvizScreenerCollector`'s two calls, served from one cached scan."""

    def __init__(self, scan: CachedScan, config: RadarConfig):
        self.scan = scan
        self.config = config
        self.read: set[str] = set()

    def _snapshot(self, source: str) -> ScreenerSnapshot:
        path = self.scan.files.get(source)
        if path is None:
            raise SourceFailure(f"{source}: no retained export in this scan")
        header, rows = parse_screener_csv(
            path.read_bytes(),
            source=source,
            required_headers=self.config.export.required_headers,
            content_type="text/csv",
        )
        self.read.add(source)
        return ScreenerSnapshot(source, self.scan.instant, rows, header, path)

    async def screen(self, block: ScreenBlock, now: datetime) -> ScreenerSnapshot:
        return self._snapshot(f"screen-{block.screen}")

    async def listed(self, block: ListBlock, now: datetime) -> list[ScreenerSnapshot]:
        size = self.config.list_chunk_size
        return [
            self._snapshot(f"list-{block.list}-{index // size + 1}")
            for index in range(0, len(block.tickers), size)
        ]


def collect_scan(
    scan: CachedScan,
    parsed: ParsedSources,
    config: RadarConfig,
    open_rows: list[dict],
) -> tuple[list[Candidate], list[SourceSet], CacheCollector]:
    """`RadarRunner._collect` over one cached scan — the production call."""
    from cobalt.radar.runner import RadarRunner

    collector = CacheCollector(scan, config)
    runner = RadarRunner(
        config=config,
        sources_loader=lambda: parsed,
        collector=collector,
        radar_store=None,
        settings_store=None,
        poller=None,
        evaluator=None,
    )
    candidates, source_sets = asyncio.run(runner._collect(parsed, scan.instant, open_rows))
    return candidates, source_sets, collector


def carry(
    opens: dict[str, OpenMember],
    transitions: list[Transition],
    *,
    now: datetime,
    trade_date: date,
) -> dict[str, OpenMember]:
    """The open episodes after one scan, as `apply_membership` records them."""
    out = dict(opens)
    for item in transitions:
        prior = out.get(item.ticker)
        if item.action is Action.LEAVE:
            out.pop(item.ticker, None)
        elif item.action is Action.ADMIT:
            out[item.ticker] = OpenMember(
                ticker=item.ticker, sources=item.sources, entered_at=now,
                below_cap_streak=item.below_cap_streak, last_rank=item.rank,
                trade_date=trade_date, rank_metric=item.rank_metric, rank_value=item.rank_value,
            )
        elif item.action is Action.RETAIN and prior is not None:
            out[item.ticker] = prior.model_copy(update={
                "sources": item.sources, "last_rank": item.rank,
                "below_cap_streak": item.below_cap_streak,
                "rank_metric": item.rank_metric, "rank_value": item.rank_value,
            })
        elif item.action is Action.HOLD and prior is not None:
            update = {
                "sources": item.sources, "last_rank": item.rank,
                "below_cap_streak": item.below_cap_streak,
            }
            if item.rank_metric is not None:
                update.update(rank_metric=item.rank_metric, rank_value=item.rank_value)
            out[item.ticker] = prior.model_copy(update=update)
        elif item.action is Action.EXCLUDE:
            if prior is not None and prior.entered_at is None:
                out[item.ticker] = prior.model_copy(update={
                    "sources": item.sources, "last_rank": item.rank,
                    "rank_metric": item.rank_metric, "rank_value": item.rank_value,
                })
            elif prior is None:
                out[item.ticker] = OpenMember(
                    ticker=item.ticker, sources=item.sources, entered_at=None,
                    below_cap_streak=item.below_cap_streak, last_rank=item.rank,
                    trade_date=trade_date, rank_metric=item.rank_metric, rank_value=item.rank_value,
                )
    return out


def open_rows(opens: dict[str, OpenMember]) -> list[dict]:
    """The rows `RadarStore.open_members` would return for these episodes."""
    return [member.model_dump() for member in opens.values()]
