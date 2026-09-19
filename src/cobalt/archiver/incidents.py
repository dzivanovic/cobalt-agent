"""`system.archive_incidents` — what a night REFUSED to do, and why.

Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §6,
§7 and §11. Table: `db_migrations/0011_archive_incidents.sql`. The five
kinds are `reconcile.IncidentKind` — defined beside the decisions that
raise them, imported here, never re-spelled (L3).

OPEN OR REFRESH, NEVER DUPLICATE. `ON CONFLICT` on the partial unique
index (`(kind, ticker, interval, range_start) WHERE resolved_at IS
NULL`): a condition that recurs every night for a fortnight is ONE row
whose `last_seen_at` moves, not fourteen. `first_seen_at` is written
once and never touched again — it is how long a target has been
withheld, which is the number an operator actually needs.

EVERY WRITE TAKES THE TARGET'S CONNECTION (§4). One exception matters
and belongs to the RUNNER, not here: a failed or withheld target's
transaction is rolled back, so its incident is persisted afterwards in
a SECOND small transaction (Astra, V3-2 — "persist failure evidence
separately after rollback"). This module is indifferent to which
transaction it is called in; the runner decides.

RESOLUTION IS EXPLICIT AND AUDITED. Nothing here resolves itself, no
run closes a row, and `resolve` refuses an empty `by`: the heartbeat is
not green while a row is unresolved (§11), and a self-closing incident
would be a dashboard that goes green on its own.
"""

from __future__ import annotations

from datetime import datetime
from typing import Iterable

from psycopg.types.json import Jsonb
from pydantic import BaseModel, ConfigDict

from .reconcile import IncidentDraft, IncidentKind

TABLE = "archive_incidents"

_COLUMNS = (
    "id, kind, ticker, interval, range_start, range_end, first_seen_at, "
    "last_seen_at, detail, resolved_at, resolved_by, run_id"
)


class IncidentRow(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    id: int
    kind: str
    ticker: str
    interval: str
    range_start: datetime | None
    range_end: datetime | None
    first_seen_at: datetime
    last_seen_at: datetime
    detail: dict
    resolved_at: datetime | None
    resolved_by: str | None
    run_id: str


def open_or_refresh(conn, draft: IncidentDraft, *, run_id: str, now: datetime) -> int:
    """Open this condition's row, or refresh the open one. Returns its id.

    The `WHERE resolved_at IS NULL` on the conflict target is what names
    the PARTIAL index: a resolved row is history and must not block the
    same condition opening again later.
    """
    row = conn.execute(
        f"""
        INSERT INTO {TABLE} (kind, ticker, interval, range_start, range_end,
                             first_seen_at, last_seen_at, detail, run_id)
        VALUES (%(kind)s, %(ticker)s, %(interval)s, %(range_start)s, %(range_end)s,
                %(now)s, %(now)s, %(detail)s, %(run_id)s)
        ON CONFLICT (kind, ticker, interval, range_start) WHERE resolved_at IS NULL
        DO UPDATE SET
            last_seen_at = EXCLUDED.last_seen_at,
            range_end = EXCLUDED.range_end,
            detail = EXCLUDED.detail,
            run_id = EXCLUDED.run_id
        RETURNING id
        """,
        {
            "kind": draft.kind.value if isinstance(draft.kind, IncidentKind) else str(draft.kind),
            "ticker": draft.ticker,
            "interval": draft.interval,
            "range_start": draft.range_start,
            "range_end": draft.range_end,
            "now": now,
            "detail": Jsonb(draft.detail),
            "run_id": run_id,
        },
    ).fetchone()
    return int(row[0])


def unresolved(conn, *, ticker: str | None = None) -> list[IncidentRow]:
    """Every open incident, oldest first. READ-ONLY.

    This is what `cobalt archiver incidents` prints and what the
    heartbeat's archiver probe counts (§11, O-7).
    """
    if ticker:
        cursor = conn.execute(
            f"SELECT {_COLUMNS} FROM {TABLE} WHERE resolved_at IS NULL AND ticker = %s "
            "ORDER BY first_seen_at, id",
            (ticker,),
        )
    else:
        cursor = conn.execute(
            f"SELECT {_COLUMNS} FROM {TABLE} WHERE resolved_at IS NULL "
            "ORDER BY first_seen_at, id"
        )
    return [_row(row) for row in cursor.fetchall()]


def resolve(conn, incident_id: int, *, by: str, note: str, now: datetime) -> None:
    """Close one incident, on the record.

    `by` and `note` are mandatory and land on the row: spec O-4 makes
    this the audit trail for a repair that has no other home — a
    `restate --apply` in `upsert` mode, or one on a target with no open
    incident, opens and resolves a `restated` row carrying the
    operator's `--reason`.
    """
    if not by or not by.strip():
        raise ValueError(
            "resolving an incident needs --by <who>: the heartbeat goes green "
            "again on this, and 'somebody' is not an audit trail."
        )
    conn.execute(
        f"""
        UPDATE {TABLE}
           SET resolved_at = %(now)s,
               resolved_by = %(resolved_by)s,
               detail = detail || %(note)s
         WHERE id = %(id)s AND resolved_at IS NULL
        """,
        {
            "now": now,
            "resolved_by": by.strip(),
            "note": Jsonb({"resolution_note": note, "resolved_at": now.isoformat()}),
            "id": incident_id,
        },
    )


def counts_by_kind(rows: Iterable[IncidentRow]) -> dict[str, int]:
    """Pure: the heartbeat's detail line, built from rows it already has."""
    counts: dict[str, int] = {}
    for row in rows:
        counts[row.kind] = counts.get(row.kind, 0) + 1
    return counts


def _row(row) -> IncidentRow:
    return IncidentRow(
        id=row[0], kind=row[1], ticker=row[2], interval=row[3], range_start=row[4],
        range_end=row[5], first_seen_at=row[6], last_seen_at=row[7],
        detail=row[8] or {}, resolved_at=row[9], resolved_by=row[10], run_id=row[11],
    )


__all__ = [
    "IncidentRow",
    "TABLE",
    "counts_by_kind",
    "open_or_refresh",
    "resolve",
    "unresolved",
]
