"""The email channel's own memory — one row per send attempt.

Read by the F18 `email` probe, which has to answer "and did the last one
actually go?" across process boundaries. Written by every caller that
sends, success or failure.

THE RECORDING NEVER BREAKS THE SEND. Same rule, and the same reason, as
`redact.guard._record`: by the time this runs the mail has already left
(or already failed), and a dead Postgres must not turn a delivered alert
into a raised exception. Loud, and non-blocking, in that order — which
is also the property that keeps `send_email`'s dependency chain free of
Postgres.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Optional

from loguru import logger

from cobalt import db, env

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class EmailSendStore:
    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
                lines = migration.read_text().splitlines()
                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
                for statement in sql.split(";"):
                    statement = statement.strip()
                    if statement:
                        conn.execute(statement)

    def record(self, *, ok: bool, caller: str, detail: str, message_id: Optional[str] = None) -> None:
        self.ensure_schema()
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO cobalt_email_sends (ok, caller, message_id, detail) "
                "VALUES (%s, %s, %s, %s)",
                (ok, caller, message_id, detail),
            )

    def last(self) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, ts, ok, caller, message_id, detail FROM cobalt_email_sends "
                "ORDER BY id DESC LIMIT 1"
            )
            row = cur.fetchone()
            if row is None:
                return None
            return dict(zip([d.name for d in cur.description], row))

    def recent(self, limit: int = 20) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, ts, ok, caller, message_id, detail FROM cobalt_email_sends "
                "ORDER BY id DESC LIMIT %s",
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]


def record_attempt(*, ok: bool, caller: str, detail: str, message_id: Optional[str] = None) -> None:
    """Record, and NEVER raise. The one entry point every sender uses."""
    try:
        EmailSendStore().record(ok=ok, caller=caller, detail=detail, message_id=message_id)
    except Exception as e:  # noqa: BLE001
        logger.error(
            "email send by {} was NOT recorded ({}: {}) — the SEND STANDS; only the "
            "F18 probe's history is missing.",
            caller, type(e).__name__, e,
        )


__all__ = ["EmailSendStore", "record_attempt"]
