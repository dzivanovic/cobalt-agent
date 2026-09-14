"""Pure text parsers over the real log/report shapes C3, C5 and C6 read.

Every regex here is matched against the ACTUAL production files (L45):
`logs/heartbeat.log`'s plain console block (one `HEARTBEAT GREEN|RED —
... (TIMESTAMP TZ)` header line and one `OK|RED  radar  <detail>` probe
line per beat), `logs/heartbeat.err`'s loguru lines, and
`docs/30 - Design/archiver-runs.md`'s markdown table. None of this reads
the markdown-table-diff rendering of the SAME beat that also lands in
heartbeat.log (the vault daily-note's before/after diff, `| emoji |
radar | ... |` with unified-diff `+`/`-` prefixes) — that is the same
information in a second format, and parsing the plain block is enough
and unambiguous.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

_RADAR_PROBE_RE = re.compile(r"^(OK|RED)\s+radar\s+(.*)$")
_BEAT_HEADER_RE = re.compile(
    r"^HEARTBEAT\s+(GREEN|RED)\s+—.*\((\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (EDT|EST)\)$"
)
#: loguru's default line prefix: "2026-09-14 12:24:06.712 | ERROR    | ..."
_LOG_LINE_TS_RE = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\.\d+\s*\|")
_TABLE_SEPARATOR_RE = re.compile(r"^\|[\s\-:|]+\|$")


@dataclass(frozen=True)
class RadarProbeLine:
    state: str  # "OK" | "RED"
    detail: str
    raw: str

    @property
    def is_red(self) -> bool:
        return self.state == "RED"


@dataclass(frozen=True)
class BeatHeader:
    state: str  # "GREEN" | "RED"
    at: datetime  # tz-aware, America/New_York
    raw: str


def newest_radar_probe_line(lines: list[str]) -> RadarProbeLine | None:
    """The most recent `OK|RED  radar  ...` console line, scanning from
    the end. `None` if heartbeat has never logged one (a real finding,
    not a parse failure — the caller renders it as ERROR)."""
    for line in reversed(lines):
        match = _RADAR_PROBE_RE.match(line.rstrip("\n"))
        if match:
            return RadarProbeLine(state=match.group(1), detail=match.group(2), raw=line.rstrip("\n"))
    return None


def newest_beat_header(lines: list[str]) -> BeatHeader | None:
    """The most recent `HEARTBEAT GREEN|RED — ... (TIMESTAMP TZ)` line."""
    for line in reversed(lines):
        match = _BEAT_HEADER_RE.match(line.rstrip("\n"))
        if match:
            state, ts_raw, _tz = match.groups()
            at = datetime.strptime(ts_raw, "%Y-%m-%d %H:%M:%S").replace(tzinfo=ET)
            return BeatHeader(state=state, at=at, raw=line.rstrip("\n"))
    return None


def all_beat_headers(lines: list[str]) -> list[BeatHeader]:
    """Every beat header in file order (oldest first)."""
    out: list[BeatHeader] = []
    for line in lines:
        match = _BEAT_HEADER_RE.match(line.rstrip("\n"))
        if match:
            state, ts_raw, _tz = match.groups()
            at = datetime.strptime(ts_raw, "%Y-%m-%d %H:%M:%S").replace(tzinfo=ET)
            out.append(BeatHeader(state=state, at=at, raw=line.rstrip("\n")))
    return out


def failed_lines(lines: list[str]) -> list[tuple[datetime, str]]:
    """Every loguru line containing the literal substring "FAILED", with
    its ET timestamp (the file's own wall-clock prefix — the host runs
    on ET, same convention as `logs/heartbeat.log`'s beat headers).

    Deliberately a SUBSTRING match, not a level filter: `job_run`'s wrapper
    logs a genuine crash as `... FAILED — <Exception>: ...` at ERROR
    level, but so does a normal RED beat's own `heartbeat: RED — N
    job(s)` line — and that one does NOT contain "FAILED", so the two
    stay distinguishable without parsing the loguru level column.
    """
    out: list[tuple[datetime, str]] = []
    for line in lines:
        if "FAILED" not in line:
            continue
        match = _LOG_LINE_TS_RE.match(line)
        if not match:
            continue
        at = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S").replace(tzinfo=ET)
        out.append((at, line.rstrip("\n")))
    return out


def last_markdown_table_row(text: str) -> tuple[list[str], list[str]] | None:
    """`(header_cells, last_row_cells)` of the LAST `|`-delimited table in
    `text` (a markdown file may carry more than one table; day-open wants
    the newest, which is always the last one in an append-only report).
    `None` if there is no table at all."""
    lines = text.splitlines()
    separator_idx = None
    for i, line in enumerate(lines):
        if _TABLE_SEPARATOR_RE.match(line.strip()):
            separator_idx = i
    if separator_idx is None or separator_idx == 0:
        return None

    def _cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    header = _cells(lines[separator_idx - 1])
    data_lines = []
    for line in lines[separator_idx + 1:]:
        if not line.strip().startswith("|"):
            break
        data_lines.append(line)
    if not data_lines:
        return None
    return header, _cells(data_lines[-1])


__all__ = [
    "ET",
    "BeatHeader",
    "RadarProbeLine",
    "all_beat_headers",
    "failed_lines",
    "last_markdown_table_row",
    "newest_beat_header",
    "newest_radar_probe_line",
]
