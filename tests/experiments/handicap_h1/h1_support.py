"""Experiment-only helpers: where the retained cache and his notes live
(both READ-ONLY), and the scan-by-scan replay the experiments share.

Nothing here prints; each experiment prints its own counts.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Iterator
from zoneinfo import ZoneInfo

from h1_cache import CachedScan, carry, collect_scan, group_scans, open_rows

from cobalt.radar.config import RadarConfig, load_config
from cobalt.radar.models import Candidate, ExcludedBy, OpenMember, SourceHealth, SourceSet
from cobalt.radar.notes import ParsedSources, parse_note
from cobalt.radar.pool import Decision, decide

ET = ZoneInfo("America/New_York")
#: His live vault and production's retained cache — both read, never written.
VAULT = Path("/Users/cobalt/Vault/Think")
CACHE = Path("/Users/cobalt/cobalt/data/radar-cache")


def config() -> RadarConfig:
    return load_config()


def his_sources(cfg: RadarConfig) -> ParsedSources:
    """His two notes through the existing reader (L28: read only)."""
    screens = parse_note(VAULT / cfg.notes.screens, "screens")
    lists = parse_note(VAULT / cfg.notes.lists, "lists")
    pool = next((item.block for item in screens.blocks if item.key == "pool"), None)
    return ParsedSources(screens=screens, lists=lists, pool=pool)


def retained_days() -> list[Path]:
    days = []
    for path in sorted(CACHE.iterdir()):
        try:
            date.fromisoformat(path.name)
        except ValueError:
            continue
        if path.is_dir():
            days.append(path)
    return days


def blocks_of(parsed: ParsedSources, pool=None) -> list[object]:
    """The block list `runner.cycle` hands `decide()`, with `pool` swapped in
    when a pass needs a different pool block."""
    blocks = [item.block for item in parsed.screens.blocks + parsed.lists.blocks]
    if pool is None:
        return blocks
    return [pool if item is parsed.pool else item for item in blocks]


@dataclass
class ReplayedScan:
    scan: CachedScan
    candidates: list[Candidate]
    source_sets: list[SourceSet]
    decision: Decision
    opens_before: dict[str, OpenMember]

    def equity(self, source: SourceSet) -> list[str]:
        not_equity = {c.ticker for c in self.candidates if c.excluded_by is ExcludedBy.NOT_EQUITY}
        return [t for t in source.tickers if t not in not_equity]

    def live_screens(self) -> list[SourceSet]:
        return [
            s for s in self.source_sets
            if s.kind == "screen" and s.active and s.health is SourceHealth.HEALTHY
        ]


def replay(day_dir: Path, parsed: ParsedSources, cfg: RadarConfig, pool=None) -> Iterator[ReplayedScan]:
    """`decide()` scan by scan over one retained day, opens carried forward
    from the replay's own transitions; the first scan starts empty."""
    blocks = blocks_of(parsed, pool)
    opens: dict[str, OpenMember] = {}
    for scan in group_scans(day_dir):
        candidates, source_sets, _collector = collect_scan(scan, parsed, cfg, open_rows(opens))
        decision = decide(candidates, list(opens.values()), blocks, source_sets, scan.instant)
        yield ReplayedScan(scan, candidates, source_sets, decision, opens)
        opens = carry(
            opens, decision.transitions, now=scan.instant, trade_date=scan.instant.astimezone(ET).date()
        )


def et_hhmm(instant: datetime) -> str:
    return instant.astimezone(ET).strftime("%H:%M")


#: The two export headers v3 F5 names (engine config from STEP-2 on:
#: `export.handicap_headers`); the experiments of STEP-1 run before it.
FLOAT_HEADER = "Shares Float"
CAP_HEADER = "Market Cap"


def source_key(source: str) -> str:
    """`screen-<key>` / `list-<key>` — a list's chunks are one source."""
    if source.startswith("list-"):
        return source.rsplit("-", 1)[0]
    return source


def exports(day_dir: Path, cfg: RadarConfig):
    """Every retained export of one day, scan by scan, through production's
    own CSV reader: `(scan, source, header, rows)`."""
    from cobalt.radar.collector import parse_screener_csv

    for scan in group_scans(day_dir):
        for source, path in sorted(scan.files.items()):
            header, rows = parse_screener_csv(
                path.read_bytes(), source=source,
                required_headers=cfg.export.required_headers, content_type="text/csv",
            )
            yield scan, source, header, rows


def constructed_block(**overrides):
    """A handicap block of THIS BUILD's literals — none of them his (L32,
    L69): thresholds 20 / 300, factor 0.8, combinator any, missing apply,
    mode shadow. Callers name any key they change."""
    values = {
        "float_below_m": Decimal("20"),
        "market_cap_below_m": Decimal("300"),
        "factor": Decimal("0.8"),
        "missing": "apply",
        "mode": "shadow",
        "combinator": "any",
    }
    values.update(overrides)
    return values
