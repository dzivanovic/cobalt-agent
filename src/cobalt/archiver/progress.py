"""`system.archive_progress` — reading and writing the archiver's OWN
watermark, on the target's connection.

Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §4
and §11. Table: `db_migrations/0010_archive_progress.sql`.

THE WRITER REFUSES A TARGET THAT WAS NOT ACCEPTED. §4 says progress
never moves on a failed, withheld, empty or regressed target, and the
cheapest way to keep that true is to make it impossible to ask for:
`upsert_progress` raises when the plan it is handed has no
`archived_through_after`. The rule lives with the write, not in the
caller's discipline (L1).

MONOTONIC BY `GREATEST`, IN SQL. Two runs of the same night, a retry
after a crash, or a repair racing the nightly run must never move the
watermark backwards, and the only place that can be guaranteed is the
statement itself — a read-then-compare in Python is a race.

NO ROW IS EVER DELETED HERE. A ticker leaving the trader's Lists note
keeps its row, which is what makes the dropped-and-re-added sequence
open a `gap` incident rather than silently skipping the missing days
(round-2 sequence #8). This module contains no `DELETE`, and a test
says so.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict

from .models import Interval
from .reconcile import TargetPlan

TABLE = "archive_progress"


class ProgressRow(BaseModel):
    """One target's row, as the `progress` command renders it."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    ticker: str
    interval: str
    archived_through: datetime
    export_oldest: datetime
    export_newest: datetime
    raw_export_newest: datetime | None
    fetch_started_at: datetime
    bootstrap_at: datetime
    run_id: str
    updated_at: datetime


_COLUMNS = (
    "ticker, interval, archived_through, export_oldest, export_newest, "
    "raw_export_newest, fetch_started_at, bootstrap_at, run_id, updated_at"
)


def read_archived_through(conn, ticker: str, interval: Interval) -> datetime | None:
    """This target's watermark, or `None` — which means BOOTSTRAP.

    `None` is not a default standing in for a missing row: §4 says a
    target with no progress row reconciles its whole available export
    once, and the report says `bootstrap` and names the bounds.
    """
    row = conn.execute(
        f"SELECT archived_through FROM {TABLE} WHERE ticker = %s AND interval = %s",
        (ticker, _interval(interval)),
    ).fetchone()
    return row[0] if row else None


def read_row(conn, ticker: str, interval: Interval) -> ProgressRow | None:
    row = conn.execute(
        f"SELECT {_COLUMNS} FROM {TABLE} WHERE ticker = %s AND interval = %s",
        (ticker, _interval(interval)),
    ).fetchone()
    return _row(row) if row else None


def all_rows(conn) -> list[ProgressRow]:
    """Every target's progress, oldest watermark first — what
    `cobalt archiver progress` prints. Read-only."""
    cursor = conn.execute(
        f"SELECT {_COLUMNS} FROM {TABLE} ORDER BY archived_through, ticker, interval"
    )
    return [_row(row) for row in cursor.fetchall()]


def upsert_progress(conn, *, plan: TargetPlan, run_id: str, now: datetime) -> None:
    """Record an ACCEPTED target's new watermark, on `conn`.

    `archived_through` is a BAR timestamp — the `ts` of the newest
    complete bar of this accepted export — never a clock time, never a
    bar-close time, never `fetch_started_at` (§4). `now` is only
    `updated_at`, and `bootstrap_at` is set once and kept.
    """
    if plan.archived_through_after is None:
        raise RuntimeError(
            f"{plan.ticker}/{plan.interval.value} was not accepted "
            f"({plan.status.value}: {plan.reason}) — progress does not move on a "
            "failed, withheld, empty or regressed target (spec §4)."
        )
    conn.execute(
        f"""
        INSERT INTO {TABLE} ({_COLUMNS})
        VALUES (%(ticker)s, %(interval)s, %(archived_through)s, %(export_oldest)s,
                %(export_newest)s, %(raw_export_newest)s, %(fetch_started_at)s,
                %(bootstrap_at)s, %(run_id)s, %(updated_at)s)
        ON CONFLICT (ticker, interval) DO UPDATE SET
            archived_through = GREATEST({TABLE}.archived_through,
                                        EXCLUDED.archived_through),
            export_oldest = EXCLUDED.export_oldest,
            export_newest = EXCLUDED.export_newest,
            raw_export_newest = EXCLUDED.raw_export_newest,
            fetch_started_at = EXCLUDED.fetch_started_at,
            run_id = EXCLUDED.run_id,
            updated_at = EXCLUDED.updated_at
        """,
        {
            "ticker": plan.ticker,
            "interval": plan.interval.value,
            "archived_through": plan.archived_through_after,
            "export_oldest": plan.export_oldest,
            "export_newest": plan.export_newest,
            "raw_export_newest": plan.raw_export_newest,
            "fetch_started_at": plan.fetch_started_at,
            "bootstrap_at": now,
            "run_id": run_id,
            "updated_at": now,
        },
    )


def _interval(interval) -> str:
    return interval.value if isinstance(interval, Interval) else str(interval)


def _row(row) -> ProgressRow:
    return ProgressRow(
        ticker=row[0], interval=row[1], archived_through=row[2], export_oldest=row[3],
        export_newest=row[4], raw_export_newest=row[5], fetch_started_at=row[6],
        bootstrap_at=row[7], run_id=row[8], updated_at=row[9],
    )


__all__ = [
    "ProgressRow",
    "TABLE",
    "all_rows",
    "read_archived_through",
    "read_row",
    "upsert_progress",
]
