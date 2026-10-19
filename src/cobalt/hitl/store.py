"""Persistence for HITL requests: `cobalt_hitl_requests` (F20 C2a).

The `jobs/store.py` shape: the database is NOT named here (`COBALT_ENV`
chooses it), `db_name` is the test/tooling seam, the DDL lives in
`migrations/` and is executed rather than re-typed.

NO APPROVE METHOD. The `pending` -> `approved` / `denied` statements are
written in the two `/hitl` routes of `aset/web.py` and run through
`update_returning` (L37, T3); this store owns the request, the claim, the
sweep and the reads.
"""

from __future__ import annotations

import json
import secrets
from pathlib import Path
from typing import Any, Callable, Optional

from cobalt import db, env
from cobalt.db import Side

from .models import REPORTED

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


def _row(cur, row) -> Optional[dict[str, Any]]:
    if row is None:
        return None
    out = dict(zip([d.name for d in cur.description], row))
    for key in ("rendered", "before_bytes"):
        if isinstance(out.get(key), memoryview):
            out[key] = out[key].tobytes()
    return out


class HitlStore:
    #: ADR-0008 D2 — his approvals are one trader's record (card DECISION 4).
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            db.assert_schemas_exist(conn)
            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
                lines = migration.read_text().splitlines()
                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
                for statement in sql.split(";"):
                    statement = statement.strip()
                    if statement:
                        conn.execute(statement)

    # -- the request ----------------------------------------------------

    def insert(
        self, *, agent_id: str, action: str, payload: dict, sha256: str, rendered: bytes,
        before_sha256: Optional[str], before_bytes: Optional[bytes], reason: str,
        ttl_min: int, approve_key_sha256: str,
    ) -> tuple[int, str]:
        """One `pending` row; `expires_at` = the database's now() + the TTL,
        the same clock the approve statement compares against."""
        short_id = secrets.token_hex(4)
        with self._connect() as conn:
            cur = conn.execute(
                "INSERT INTO cobalt_hitl_requests (short_id, agent_id, action, payload, sha256, "
                "rendered, before_sha256, before_bytes, reason, expires_at, approve_key_sha256) "
                "VALUES (%s, %s, %s, %s::jsonb, %s, %s, %s, %s, %s, "
                "now() + make_interval(mins => %s), %s) RETURNING id, short_id",
                (short_id, agent_id, action, json.dumps(payload, sort_keys=True), sha256,
                 rendered, before_sha256, before_bytes, reason, int(ttl_min), approve_key_sha256),
            )
            row_id, short = cur.fetchone()
        return int(row_id), short

    # -- reads ----------------------------------------------------------

    def get(self, row_id: int) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM cobalt_hitl_requests WHERE id = %s", (int(row_id),))
            return _row(cur, cur.fetchone())

    def recent(self, limit: int = 50) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT * FROM cobalt_hitl_requests ORDER BY (status = 'pending') DESC, id DESC "
                "LIMIT %s", (int(limit),))
            return [_row(cur, r) for r in cur.fetchall()]

    def backs_sha256(self, sha256: str) -> bool:
        """The `generated` commit path's one question (F-07): does an
        `executed` row carry this sha256?"""
        with self._connect() as conn:
            row = conn.execute(
                "SELECT 1 FROM cobalt_hitl_requests WHERE status = 'executed' AND sha256 = %s LIMIT 1",
                (sha256,),
            ).fetchone()
        return row is not None

    def probe_counts(self) -> dict[str, int]:
        with self._connect() as conn:
            pending, failed = conn.execute(
                "SELECT count(*) FILTER (WHERE status = 'pending' AND expires_at < now()), "
                "count(*) FILTER (WHERE status = 'failed') FROM cobalt_hitl_requests"
            ).fetchone()
        return {"pending_past_ttl": int(pending), "failed": int(failed)}

    # -- the route statements (aset/web.py writes the SQL) --------------

    def update_returning(self, sql: str, params: tuple) -> list[tuple]:
        """Run ONE statement with RETURNING and give back its rows. The two
        `/hitl` routes pass their own single statement (L37)."""
        with self._connect() as conn:
            return list(conn.execute(sql, params).fetchall())

    # -- the executor's claim, the sweeper, the report ------------------

    def claim_next(
        self, handler: Callable[[dict[str, Any]], tuple[str, Optional[dict], Optional[str]]]
    ) -> Optional[tuple[dict[str, Any], str]]:
        """Claim one `approved` row, hand it to `handler`, record its outcome
        (`executed` | `failed`) — one transaction. An exception from the
        handler rolls the claim back and leaves the row `approved`."""
        with self._connect() as conn:
            with conn.transaction():
                cur = conn.execute(
                    "SELECT * FROM cobalt_hitl_requests WHERE status = 'approved' "
                    "ORDER BY id FOR UPDATE SKIP LOCKED LIMIT 1"
                )
                row = _row(cur, cur.fetchone())
                if row is None:
                    return None
                status, result, error = handler(row)
                if status not in ("executed", "failed"):
                    raise ValueError(f"an executor outcome is executed or failed, got {status!r}")
                conn.execute(
                    "UPDATE cobalt_hitl_requests SET status = %s, result = %s::jsonb, error = %s "
                    "WHERE id = %s AND status = 'approved'",
                    (status, json.dumps(result) if result is not None else None, error, row["id"]),
                )
        row.update(status=status, result=result, error=error)
        return row, status

    def expire_pending(self) -> list[dict[str, Any]]:
        """`pending` past `expires_at` -> `expired`. An `approved` row is never
        expired out from under a tap (F-15)."""
        with self._connect() as conn:
            cur = conn.execute(
                "UPDATE cobalt_hitl_requests SET status = 'expired' "
                "WHERE status = 'pending' AND expires_at < now() RETURNING *"
            )
            return [_row(cur, r) for r in cur.fetchall()]

    def unreported(self) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT * FROM cobalt_hitl_requests WHERE status = ANY(%s) AND reported_at IS NULL "
                "ORDER BY id", (list(REPORTED),))
            return [_row(cur, r) for r in cur.fetchall()]

    def mark_reported(self, row_id: int) -> None:
        with self._connect() as conn:
            conn.execute("UPDATE cobalt_hitl_requests SET reported_at = now() WHERE id = %s",
                         (int(row_id),))


__all__ = ["HitlStore", "MIGRATIONS_DIR"]
