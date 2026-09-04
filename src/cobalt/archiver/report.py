"""Run-report writer — one appended line per Bar Archiver run.

Fail-loud alerting can come later (per the task); this is the minimum
visible record: a human-readable, append-only markdown table.
"""

from datetime import datetime, timezone
from pathlib import Path

from cobalt import env

from .config import REPO_ROOT

REPORT_PATH = REPO_ROOT / "docs" / "30 - Design" / "archiver-runs.md"

# RULING 9 (2026-09-04) added the Database column. Every run now says on
# the record which database it wrote to, because the failure this ruling
# repaired — the archiver writing production bars into `cobalt_dev` for
# three weeks — was invisible in this log precisely because the log did
# not name a database. This string is the schema marker: its absence
# from an existing file is what triggers the one-time break below.
COLUMNS = "| Date (UTC) | Mode | Database | Tickers | Requests | Rows Written | Failures | Duration |"
_RULE = "|---|---|---|---|---|---|---|---|"

HEADER = f"""# Bar Archiver — Run Log

Append-only. One row per run (nightly full run, or a manual
`--backfill TICKER`). Written by `cobalt.archiver.report`.

{COLUMNS}
{_RULE}
"""

# Appended ONCE to a pre-RULING-9 file: a markdown table cannot change
# its column count in place, so the log gets a second table rather than
# rows that silently misalign against the old header.
SCHEMA_BREAK = f"""
## Database column added — RULING 9, 2026-09-04

Rows above this line predate the column and were **all written to
`cobalt_dev`**: the archiver named its own database (`db_name=
"cobalt_dev"`) instead of asking `COBALT_ENV`, so every nightly run
above archived production bars into the dev database. RULING 9 migrated
`bars` to `cobalt_brain` (4,563,539 rows, md5-verified) and deleted the
override. Rows below name their target.

{COLUMNS}
{_RULE}
"""


class RunSummary:
    def __init__(self, mode: str, db_name: str | None = None):
        self.mode = mode
        # Resolved once, at the start of the run, from the same source
        # the store uses — so the log cannot disagree with where the
        # rows actually went.
        self.db_name = db_name or env.resolve_db_name()
        self.started_at = datetime.now(timezone.utc)
        self.tickers: set[str] = set()
        self.requests = 0
        self.rows_written = 0
        self.failures: list[str] = []

    def record_success(self, ticker: str, rows: int) -> None:
        self.tickers.add(ticker)
        self.requests += 1
        self.rows_written += rows

    def record_failure(self, ticker: str, interval: str, error: str) -> None:
        self.tickers.add(ticker)
        self.requests += 1
        self.failures.append(f"{ticker}/{interval}: {error}")

    def duration_str(self) -> str:
        elapsed = (datetime.now(timezone.utc) - self.started_at).total_seconds()
        m, s = divmod(int(elapsed), 60)
        return f"{m}m{s:02d}s"


def append_run_report(summary: RunSummary) -> Path:
    """Append one table row. Kept strictly tabular (no interleaved
    content) so the table renders correctly across every future append —
    the Failures column is a count; full per-ticker error text goes to
    stdout/loguru (the launchd job's own log file), not this file."""
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    is_new = not REPORT_PATH.exists()
    needs_break = not is_new and COLUMNS not in REPORT_PATH.read_text(encoding="utf-8")
    date_str = summary.started_at.strftime("%Y-%m-%dT%H:%M:%SZ")
    row = (
        f"| {date_str} | {summary.mode} | {summary.db_name} | "
        f"{len(summary.tickers)} | {summary.requests} | {summary.rows_written} | "
        f"{len(summary.failures)} | {summary.duration_str()} |\n"
    )
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        if is_new:
            f.write(HEADER)
        elif needs_break:
            f.write(SCHEMA_BREAK)
        f.write(row)
    return REPORT_PATH
