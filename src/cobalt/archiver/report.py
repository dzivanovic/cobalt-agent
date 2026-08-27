"""Run-report writer — one appended line per Bar Archiver run.

Fail-loud alerting can come later (per the task); this is the minimum
visible record: a human-readable, append-only markdown table.
"""

from datetime import datetime, timezone
from pathlib import Path

from .config import REPO_ROOT

REPORT_PATH = REPO_ROOT / "docs" / "30 - Design" / "archiver-runs.md"

HEADER = """# Bar Archiver — Run Log

Append-only. One row per run (nightly full run, or a manual
`--backfill TICKER`). Written by `cobalt.archiver.report`.

| Date (UTC) | Mode | Tickers | Requests | Rows Written | Failures | Duration |
|---|---|---|---|---|---|---|
"""


class RunSummary:
    def __init__(self, mode: str):
        self.mode = mode
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
    date_str = summary.started_at.strftime("%Y-%m-%dT%H:%M:%SZ")
    row = (
        f"| {date_str} | {summary.mode} | {len(summary.tickers)} | "
        f"{summary.requests} | {summary.rows_written} | "
        f"{len(summary.failures)} | {summary.duration_str()} |\n"
    )
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        if is_new:
            f.write(HEADER)
        f.write(row)
    return REPORT_PATH
