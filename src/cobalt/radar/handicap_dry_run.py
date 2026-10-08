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

THE DRY-RUN (FLOAT-HANDICAP-v3 §7 (1), [F-16], X12) — below the reader:
`cobalt radar handicap-dry-run --day <d>` replays `decide()` scan by scan
over one retained day, the `h = 1` pass (block absent) and, when his note
carries a block, the handicap pass; prints the per-scan lines [F-16]
names; and compares the `h = 1` pass with STORED membership, read only.
It writes nothing.
"""

from __future__ import annotations

import asyncio
import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import date, datetime, time, timezone
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

from cobalt.radar.collector import ScreenerSnapshot, SourceFailure, parse_screener_csv
from cobalt.radar.config import RadarConfig
from cobalt.radar.models import (
    Candidate, ExcludedBy, HandicapBlock, ListBlock, OpenMember, PoolBlock, ScreenBlock, SourceSet,
)
from cobalt.radar.notes import ParsedSources
from cobalt.radar.pool import Action, Decision, Transition, decide

SCREEN_FILE = re.compile(r"^screen-(?P<key>[a-z0-9_]+)-(?P<at>\d{6})\.csv$")
LIST_FILE = re.compile(r"^list-(?P<key>[a-z0-9_]+)-(?P<chunk>[1-9]\d*)-(?P<at>\d{6})\.csv$")
_ET = ZoneInfo("America/New_York")


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


# ---------------------------------------------------------------------
# The dry-run (FLOAT-HANDICAP-v3 §7 (1), [F-16], X12)
# ---------------------------------------------------------------------

#: Every field a `Transition` carried before H1 — the `h = 1` identity
#: compares exactly these (`raw_rank` is H1's and must equal `rank`).
CORE_FIELDS = (
    "ticker", "action", "sources", "source", "rank", "below_cap_streak",
    "excluded_by", "rollover", "left_at", "rank_metric", "rank_value",
)
TIERS = ("held", "stickiness", "priority", "first_from", "position")
ADMITTED = {Action.ADMIT, Action.RETAIN, Action.HOLD}


class DryRunError(RuntimeError):
    """A day not in the cache, a malformed day, or no pool block: loud (L1)."""


@dataclass
class ReplayedScan:
    scan: CachedScan
    source_sets: list[SourceSet]
    decision: Decision


def replay_day(day_dir: Path, parsed: ParsedSources, config: RadarConfig, pool: PoolBlock) -> list[ReplayedScan]:
    """`decide()` scan by scan over one retained day with `pool` in place of
    the note's pool block; opens carried forward from the replay's own
    transitions; the first scan starts empty."""
    blocks = [
        pool if item.block is parsed.pool else item.block
        for item in parsed.screens.blocks + parsed.lists.blocks
    ]
    opens: dict[str, OpenMember] = {}
    replayed: list[ReplayedScan] = []
    for scan in group_scans(day_dir):
        candidates, source_sets, _collector = collect_scan(scan, parsed, config, open_rows(opens))
        decision = decide(
            candidates, list(opens.values()), blocks, source_sets, scan.instant,
            handicap_headers=config.export.handicap_headers,
        )
        replayed.append(ReplayedScan(scan, source_sets, decision))
        opens = carry(opens, decision.transitions, now=scan.instant,
                      trade_date=scan.instant.astimezone(_ET).date())
    return replayed


def core(transition: Transition) -> tuple:
    return tuple(getattr(transition, name) for name in CORE_FIELDS)


def identity_mismatches(
    day_dir: Path, parsed: ParsedSources, config: RadarConfig, block: HandicapBlock
) -> tuple[int, list[str]]:
    """X12 for one day: the pool block with the handicap ABSENT against the
    same block with `block` at factor 1 — every pre-H1 field of every
    transition and their order identical, `raw_rank == rank` on every
    ranked row. Returns (scans, mismatch lines)."""
    if parsed.pool is None:
        raise DryRunError("the screens note has no pool block")
    absent = parsed.pool.model_copy(update={"handicap": None})
    unit = parsed.pool.model_copy(update={"handicap": block.model_copy(update={"factor": Decimal(1)})})
    a = replay_day(day_dir, parsed, config, absent)
    b = replay_day(day_dir, parsed, config, unit)
    mismatches: list[str] = []
    if len(a) != len(b):
        mismatches.append(f"{day_dir.name} scan count {len(a)} vs {len(b)}")
    for index, (x, y) in enumerate(zip(a, b)):
        left = [core(t) for t in x.decision.transitions]
        right = [core(t) for t in y.decision.transitions]
        if len(left) != len(right):
            mismatches.append(f"{day_dir.name} scan {index} transition count")
        for l_row, r_row in zip(left, right):
            if l_row != r_row:
                field_name = next(CORE_FIELDS[k] for k in range(len(CORE_FIELDS)) if l_row[k] != r_row[k])
                mismatches.append(f"{day_dir.name} scan {index} field {field_name}")
                break
        for t in (*x.decision.transitions, *y.decision.transitions):
            if t.raw_rank is not None and t.raw_rank != t.rank:
                mismatches.append(f"{day_dir.name} scan {index} field raw_rank")
                break
    return len(a), mismatches


@dataclass
class ScanLine:
    """One scan of the dry-run ([F-16]). `kept` / `lost` / `took` are the
    WOULD-BE seats — `effective_position ≤ seats` (= cap − held), before
    stickiness — beside the admission that actually happened."""

    at: str
    members_in: int
    members_out: int
    kept: list[str]
    lost: list[str]
    took: list[str]
    cuts: Counter
    inoperative: str | None


@dataclass
class DryRun:
    day: str
    scans: int
    lines: list[ScanLine]
    headers: tuple[str, str]
    raw_cells: list[str]
    configured: bool
    admitted: list[set[str]] = field(default_factory=list)
    instants: list[datetime] = field(default_factory=list)


def _group(transition: Transition) -> str:
    return "screens" if (transition.source or "").startswith("screen:") else "lists"


def _cut_tier(cut: Transition, last: Transition | None, *, seats: int, held: int, pool: PoolBlock,
              now: datetime) -> str:
    """The tier that decided one cut ([F-16], X12: the tier of every cut; NOT X2's per-scan marginal-seat tally, which ranks held first and stops at one tier per scan — test_h1_x2_marginal_seat.py _tier): a name
    inside the seats that still left was displaced by `stickiness`; a name
    that fits the cap but not the seats lost to `held` members; otherwise the
    first key component where it loses to the last admitted name —
    `priority` (group), `first_from`, else `position`."""
    if cut.rank <= seats:
        return "stickiness"
    if held and cut.rank <= pool.cap:
        return "held"
    if last is None or _group(last) != _group(cut):
        return "priority"

    def first(transition: Transition) -> bool:
        if _group(transition) != "screens":
            return False
        key = (transition.source or "").split(":", 1)[-1].split("@", 1)[0]
        override = pool.overrides.get(key)
        first_from = getattr(override, "first_from", None)
        return bool(first_from and now.astimezone(_ET).strftime("%H:%M") >= first_from)

    return "first_from" if first(last) != first(cut) else "position"


def scan_line(previous: set[str], replayed: ReplayedScan, pool: PoolBlock) -> tuple[ScanLine, set[str]]:
    transitions = replayed.decision.transitions
    admitted = {t.ticker for t in transitions if t.action in ADMITTED}
    held = sum(t.action is Action.HOLD for t in transitions)
    seats = max(0, pool.cap - held)
    shadowed = [t for t in transitions if t.raw_rank is not None and t.handicap is not None]

    def label(t: Transition) -> str:
        return f"{t.ticker} {t.handicap.position}→{t.handicap.effective_position}"

    handicapped = [t for t in shadowed if t.handicap_factor < 1]
    kept = [label(t) for t in handicapped if t.raw_rank <= seats and t.handicap.effective_position <= seats]
    lost = [label(t) for t in handicapped if t.raw_rank <= seats and t.handicap.effective_position > seats]
    took = [label(t) for t in shadowed
            if t.handicap_factor == 1 and t.raw_rank > seats and t.handicap.effective_position <= seats]
    ranked_in = [t for t in transitions if t.action in {Action.ADMIT, Action.RETAIN} and t.rank is not None]
    last = max(ranked_in, key=lambda t: t.rank) if ranked_in else None
    cuts = Counter(
        _cut_tier(t, last, seats=seats, held=held, pool=pool, now=replayed.scan.instant)
        for t in transitions
        if t.action in {Action.EXCLUDE, Action.LEAVE} and t.excluded_by is ExcludedBy.CONFIG_CAP
        and t.rank is not None
    )
    reason = replayed.decision.reasons.get("handicap")
    line = ScanLine(
        at=replayed.scan.instant.astimezone(_ET).strftime("%H:%M:%S"),
        members_in=len(admitted - previous), members_out=len(previous - admitted),
        kept=kept, lost=lost, took=took, cuts=cuts,
        inoperative=reason if reason and reason.startswith("handicap inoperative") else None,
    )
    return line, admitted


def _raw_cells(day_dir: Path, config: RadarConfig) -> list[str]:
    """Five raw float cells as the export wrote them ([F-10]): the format
    the thresholds are compared in."""
    header = config.export.handicap_headers.float
    for scan in group_scans(day_dir):
        for source, path in sorted(scan.files.items()):
            _header, rows = parse_screener_csv(
                path.read_bytes(), source=source,
                required_headers=config.export.required_headers, content_type="text/csv",
            )
            cells = [row.get(header) or "" for row in rows if (row.get(header) or "").strip()]
            if len(cells) >= 5:
                return cells[:5]
    return []


def dry_run(day_dir: Path, parsed: ParsedSources, config: RadarConfig, block: HandicapBlock | None) -> DryRun:
    """The `h = 1` pass (block absent) and, when a block is given, the
    handicap pass — scan by scan over one retained day."""
    if parsed.pool is None:
        raise DryRunError("the screens note has no pool block")
    unit = replay_day(day_dir, parsed, config, parsed.pool.model_copy(update={"handicap": None}))
    passes = (
        replay_day(day_dir, parsed, config, parsed.pool.model_copy(update={"handicap": block}))
        if block is not None else unit
    )
    lines: list[ScanLine] = []
    previous: set[str] = set()
    for replayed in passes:
        line, previous = scan_line(previous, replayed, parsed.pool)
        lines.append(line)
    return DryRun(
        day=day_dir.name, scans=len(unit), lines=lines,
        headers=(config.export.handicap_headers.float, config.export.handicap_headers.market_cap),
        raw_cells=_raw_cells(day_dir, config), configured=block is not None,
        admitted=[{t.ticker for t in r.decision.transitions if t.action in ADMITTED} for r in unit],
        instants=[r.scan.instant for r in unit],
    )


def stored_mismatches(
    unit: list[set[str]], instants: list[datetime], stored_rows: list[dict]
) -> tuple[int, int, list[str]]:
    """[F-16]: the `h = 1` pass against STORED membership, scan by scan. A
    stored scan is matched to a cached one by its second (`scan_id` is the
    cycle's epoch milliseconds; the cache names the second). Returns
    (matched scans, unmatched scans, mismatch lines). Read only."""
    scan_ids = {
        int(row[key]) for row in stored_rows for key in ("opened_scan_id", "last_scan_id", "closed_scan_id")
        if row.get(key) is not None
    }
    by_second = {scan_id // 1000: scan_id for scan_id in scan_ids}
    matched = unmatched = 0
    mismatches: list[str] = []
    for index, (admitted, instant) in enumerate(zip(unit, instants)):
        scan_id = by_second.get(int(instant.timestamp()))
        if scan_id is None:
            unmatched += 1
            continue
        matched += 1
        stored = {
            row["ticker"] for row in stored_rows
            if row.get("entered_at") is not None and int(row["opened_scan_id"]) <= scan_id
            and (row.get("closed_scan_id") is None or int(row["closed_scan_id"]) > scan_id)
        }
        if stored != admitted:
            mismatches.append(
                f"scan {index}: stored-only {len(stored - admitted)} · replay-only {len(admitted - stored)}"
            )
    return matched, unmatched, mismatches


def render(report: DryRun) -> list[str]:
    """The dry-run's text: counts, tiers and would-be ranks — never a value
    of his (the block is his note's; nothing of it is printed)."""
    tally: Counter = Counter()
    for line in report.lines:
        tally.update(line.cuts)
    out = [
        f"handicap-dry-run {report.day} · n: 1 day, {report.scans} scans (L8: descriptive)",
        f"handicap: {'configured' if report.configured else 'not configured — h = 1 pass only'}",
        f"headers read: {report.headers[0]} / {report.headers[1]} · five raw cells: {report.raw_cells}",
    ]
    for line in report.lines:
        out.append(
            f"{line.at} · in {line.members_in} · out {line.members_out} · kept {line.kept} · "
            f"lost {line.lost} · took {line.took} · cut tiers {dict(sorted(line.cuts.items()))}"
            + (f" · INOPERATIVE: {line.inoperative}" if line.inoperative else "")
        )
    inoperative = sum(1 for line in report.lines if line.inoperative)
    out.append(f"scans with the handicap INOPERATIVE (R54): {inoperative} of {report.scans}")
    # X2 (grok, the per-scan marginal-seat experiment): 40 of 118 marginal seats on the retained RTH day were decided by stickiness or priority, so the "keeps its seat iff p ≤ h × c" sentence is never printed. The tally below is _cut_tier's per-cut rule ([F-16], X12), not X2's.
    out.append("cut tiers, the day: " + (", ".join(f"{k} {tally[k]}" for k in TIERS if tally[k]) or "none"))
    return out


def command(args) -> None:
    """`cobalt radar handicap-dry-run --day <d>` — writes nothing."""
    from cobalt.radar.config import load_config
    from cobalt.radar.notes import configured_sources
    from cobalt.radar.store import RadarStore

    try:
        day = date.fromisoformat(args.day)
    except ValueError as error:
        raise DryRunError(f"--day must be YYYY-MM-DD, got {args.day!r}") from error
    config = load_config()
    day_dir = Path(config.cache.dir) / day.isoformat()
    if not day_dir.is_dir():
        raise DryRunError(f"{day.isoformat()} is not in the cache {config.cache.dir}")
    parsed = configured_sources(config)
    block = parsed.pool.handicap if parsed.pool is not None else None
    report = dry_run(day_dir, parsed, config, block)
    for line in render(report):
        print(line)
    if block is not None:
        scans, found = identity_mismatches(day_dir, parsed, config, block)
        print(f"h = 1 identity: scans {scans} · mismatches {len(found)}")
    rows = RadarStore().members_for_day(config.pool_key, day, price_floor_rows=True)
    matched, unmatched, mismatches = stored_mismatches(report.admitted, report.instants, rows)
    print(f"stored membership: matched {matched} scans · unmatched {unmatched} · mismatches {len(mismatches)}")
    for line in mismatches[:20]:
        print(f"stored membership mismatch: {line}")
