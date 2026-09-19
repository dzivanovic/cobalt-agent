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

# The append-only redesign (2026-09-19) gives an `append` night six more
# numbers, and a markdown table cannot change its column count in place —
# the same problem RULING 9 hit, answered the same way. These appear ONLY
# in `append` mode: §5's mode isolation says an `upsert` night writes the
# row it has always written, byte for byte, and a test asserts the append
# header never appears on an upsert night.
APPEND_COLUMNS = (
    "| Date (UTC) | Mode | Database | Tickers | Requests | Rows Written | Failures | "
    "Duration | Inserted | Withheld | Gaps | Restated | Degraded | Bootstraps |"
)
_APPEND_RULE = "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"

_APPEND_NOTE = """## Append mode — write_mode: append

Rows below were written by the APPEND path: only bars that did not exist
were inserted, and no stored row was rewritten. `Rows Written` is
`inserted` — the count the SERVER reported, not the count submitted, so
a bar the radar poller committed in between is a conflict rather than a
write. `Withheld` counts keys an `restated` target refused to insert;
`Gaps`, `Restated` and `Degraded` count targets, not keys.
"""

APPEND_HEADER = f"""# Bar Archiver — Run Log

Append-only. One row per run (nightly full run, or a manual
`--backfill TICKER`). Written by `cobalt.archiver.report`.

{_APPEND_NOTE}
{APPEND_COLUMNS}
{_APPEND_RULE}
"""

APPEND_SCHEMA_BREAK = f"""
{_APPEND_NOTE}
{APPEND_COLUMNS}
{_APPEND_RULE}
"""

# The way back. `write_mode` is a config row and a rollback to `upsert`
# is one reviewed commit, so the log has to survive the round trip
# without writing 8-column rows under a 14-column header.
UPSERT_RETURN_BREAK = f"""
## Back to upsert mode — write_mode: upsert

Rows below were written by the nightly overlay again: the whole export
through `ON CONFLICT … DO UPDATE`, and `Rows Written` is rows SUBMITTED.

{COLUMNS}
{_RULE}
"""


class RunSummary:
    def __init__(self, mode: str, db_name: str | None = None, write_mode: str = "upsert"):
        self.mode = mode
        #: The WRITE mode — a different name from `mode`, which is and
        #: stays the REPORT SCOPE ("full" / "backfill:<T>"). §5 is
        #: explicit about keeping the two names apart.
        self.write_mode = write_mode
        # Resolved once, at the start of the run, from the same source
        # the store uses — so the log cannot disagree with where the
        # rows actually went.
        self.db_name = db_name or env.resolve_db_name()
        self.started_at = datetime.now(timezone.utc)
        self.tickers: set[str] = set()
        self.requests = 0
        self.rows_written = 0
        self.failures: list[str] = []
        #: §9: `system.cobalt_jobs` has ONE row per label and no per-run
        #: id, so the run report and the progress/incident rows share
        #: this TEXT rather than growing a new run table.
        self.run_id = f"{mode}@{self.started_at.isoformat()}"
        # --- append-mode counters (all 0 on an upsert night) ----------
        self.withheld = 0
        self.gap_targets = 0
        self.restated_targets = 0
        self.degraded_targets = 0
        self.bootstraps = 0
        self.counts: list = []
        # --- the shadow compare (upsert mode only, §5) ----------------
        self.shadow_records: list = []
        self.shadow_errors = 0
        self.shadow: dict | None = None

    def record_success(self, ticker: str, rows: int) -> None:
        self.tickers.add(ticker)
        self.requests += 1
        self.rows_written += rows

    def record_failure(self, ticker: str, interval: str, error: str) -> None:
        self.tickers.add(ticker)
        self.requests += 1
        self.failures.append(f"{ticker}/{interval}: {error}")

    def record_append(self, ticker: str, plan, counts) -> None:
        """One ACCEPTED append target. `Rows Written` = `inserted` (§7)."""
        self.record_success(ticker, counts.inserted)
        self.counts.append(counts)
        if plan.bootstrap:
            self.bootstraps += 1
        kinds = {incident.kind.value for incident in plan.incidents}
        if "gap" in kinds:
            self.gap_targets += 1
        if plan.status.value == "degraded":
            self.degraded_targets += 1

    def record_append_failure(self, ticker: str, interval: str, plan) -> None:
        """One REFUSED append target: withheld, regressed or empty."""
        self.record_failure(ticker, interval, plan.reason)
        self.withheld += plan.withheld
        kinds = {incident.kind.value for incident in plan.incidents}
        if "restated" in kinds:
            self.restated_targets += 1
        if "gap" in kinds:
            self.gap_targets += 1

    @property
    def healthy(self) -> bool:
        """V2-9: any FAILED or DEGRADED target makes the night not healthy.

        `degraded_targets` is 0 by construction on an `upsert` night —
        that mode has no such verdict and must not invent one.
        """
        return not self.failures and self.degraded_targets == 0

    def job_result(self) -> dict:
        """What `_archive_nightly` puts on the `cobalt_jobs` row.

        The five keys below are today's, unchanged. `shadow` is added
        only when the shadow ran, and `append` only in append mode —
        §5's complete list of `upsert`-mode additions is those keys plus
        the lock and the artifact, and a test fails if a fourth appears.
        """
        result = {
            "rows_written": self.rows_written,
            "tickers": len(self.tickers),
            "requests": self.requests,
            "failures": len(self.failures),
            "duration": self.duration_str(),
        }
        if self.shadow is not None:
            result["shadow"] = self.shadow
        if self.write_mode == "append":
            result["append"] = {
                "inserted": self.rows_written,
                "withheld": self.withheld,
                "gap_targets": self.gap_targets,
                "restated_targets": self.restated_targets,
                "degraded_targets": self.degraded_targets,
                "bootstraps": self.bootstraps,
                "healthy": self.healthy,
            }
        return result

    def duration_str(self) -> str:
        elapsed = (datetime.now(timezone.utc) - self.started_at).total_seconds()
        m, s = divmod(int(elapsed), 60)
        return f"{m}m{s:02d}s"


def _current_header(text: str) -> str | None:
    """Which table the file is currently appending to, or None.

    WHOLE LINES, scanned backwards. A substring search cannot answer
    this: `COLUMNS` is a PREFIX of `APPEND_COLUMNS` (the append table
    adds six columns after `Duration`), so `find` reports both at the
    same offset and a file in append mode reads as an upsert file —
    which put a fresh schema break above every single row.
    """
    for line in reversed(text.splitlines()):
        if line == APPEND_COLUMNS:
            return APPEND_COLUMNS
        if line == COLUMNS:
            return COLUMNS
    return None


def append_run_report(summary: RunSummary) -> Path:
    """Append one table row. Kept strictly tabular (no interleaved
    content) so the table renders correctly across every future append —
    the Failures column is a count; full per-ticker error text goes to
    stdout/loguru (the launchd job's own log file), not this file.

    A WRITE-MODE CHANGE OPENS A NEW TABLE, ONCE, in either direction. A
    markdown table cannot change its column count in place, so an
    `append` night after `upsert` nights gets the 14-column table and a
    rollback to `upsert` gets its 8-column one back — never rows
    misaligned under the wrong header. This is RULING 9's device,
    reused rather than reinvented (L3).
    """
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    append_mode = summary.write_mode == "append"
    want = APPEND_COLUMNS if append_mode else COLUMNS
    is_new = not REPORT_PATH.exists()
    text = "" if is_new else REPORT_PATH.read_text(encoding="utf-8")
    current = _current_header(text)

    if is_new:
        prefix = APPEND_HEADER if append_mode else HEADER
    elif current == want:
        prefix = ""
    elif append_mode:
        prefix = APPEND_SCHEMA_BREAK
    elif current is None:
        # A pre-RULING-9 file: no Database column anywhere.
        prefix = SCHEMA_BREAK
    else:
        prefix = UPSERT_RETURN_BREAK

    date_str = summary.started_at.strftime("%Y-%m-%dT%H:%M:%SZ")
    cells = [
        date_str, summary.mode, summary.db_name, str(len(summary.tickers)),
        str(summary.requests), str(summary.rows_written), str(len(summary.failures)),
        summary.duration_str(),
    ]
    if append_mode:
        cells += [
            str(summary.rows_written), str(summary.withheld), str(summary.gap_targets),
            str(summary.restated_targets), str(summary.degraded_targets),
            str(summary.bootstraps),
        ]
    row = "| " + " | ".join(cells) + " |\n"
    with open(REPORT_PATH, "a", encoding="utf-8") as f:
        if prefix:
            f.write(prefix)
        f.write(row)
    return REPORT_PATH
