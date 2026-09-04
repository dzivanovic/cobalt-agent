"""Postgres audit trail for the ONE vault write path (LAW L28.3).

Every write persists the touched section's before/after plus the FULL
FILE hashes, and every human override gets its own non-expiring row.
The writer purges `vault_writes` rows older than 30 days itself — no
external cron, no forgotten retention job.

Transaction shape (`pending_write`): the audit row is INSERTed first,
the caller writes the file inside the context, and the transaction only
commits if that file write succeeded. A failed/refused write therefore
leaves no phantom audit row, and a committed row always corresponds to
bytes that reached disk.

DDL lives in migrations/ — one path; this module executes those files
and carries no second copy of the schema (same pattern as
aset/store.py).
"""

import hashlib
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Optional

from cobalt import db

MIGRATIONS_DIR = Path(__file__).parent / "migrations"
RETENTION_DAYS = 30


def sha256_text(text: Optional[str]) -> Optional[str]:
    if text is None:
        return None
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


class VaultWriteStore:
    def __init__(self, db_name: str = "cobalt_dev"):
        self.db_name = db_name

    def _connect(self):
        return db.connect(self.db_name)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
                lines = migration.read_text().splitlines()
                sql = "\n".join(line for line in lines if not line.strip().startswith("--"))
                for statement in sql.split(";"):
                    statement = statement.strip()
                    if statement:
                        conn.execute(statement)

    # -- baselines ---------------------------------------------------

    def last_after(self, note: str, section: str, unit: str) -> Optional[str]:
        """The BODY Cobalt last wrote into this unit — the `base` leg of
        the three-way merge. Deliberately `unit_after`, not `after`:
        `after` is the whole section, markers and any human lines
        between units included, and merging a unit body against that
        would treat every marker as human text. None means no baseline
        is on record (never written, or purged past retention);
        writer.py surfaces that as `baseline_missing`, never a guess."""
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT unit_after FROM vault_writes
                WHERE note = %s AND section = %s AND unit = %s
                  AND unit_after IS NOT NULL
                ORDER BY id DESC LIMIT 1
                """,
                (note, section, unit),
            ).fetchone()
        return None if row is None else row[0]

    def get_write(self, write_id: int) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, ts, note, section, unit, before, after,
                       unit_before, unit_after, hash_before, hash_after,
                       writer, run_id
                FROM vault_writes WHERE id = %s
                """,
                (write_id,),
            )
            row = cur.fetchone()
            if row is None:
                return None
            return dict(zip([d.name for d in cur.description], row))

    def recent(self, limit: int = 20) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, ts, note, section, unit, hash_before, hash_after, writer, run_id
                FROM vault_writes ORDER BY id DESC LIMIT %s
                """,
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    # -- writes ------------------------------------------------------

    @contextmanager
    def pending_write(
        self,
        *,
        note: str,
        section: Optional[str],
        unit: Optional[str],
        before: Optional[str],
        after: Optional[str],
        hash_before: Optional[str],
        hash_after: str,
        writer: str,
        run_id: str,
        unit_before: Optional[str] = None,
        unit_after: Optional[str] = None,
        overrides: Optional[list[dict[str, Any]]] = None,
    ) -> Iterator[int]:
        """INSERT the audit row (+ any override rows), yield its id for
        the caller's file write, commit only if that write succeeded."""
        with self._connect() as conn:
            conn.autocommit = False
            try:
                row = conn.execute(
                    """
                    INSERT INTO vault_writes (
                        note, section, unit, before, after,
                        unit_before, unit_after,
                        hash_before, hash_after, writer, run_id
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (note, section, unit, before, after, unit_before, unit_after,
                     hash_before, hash_after, writer, run_id),
                ).fetchone()
                if row is None:
                    raise RuntimeError("vault_writes INSERT returned no id — audit trail failed.")
                write_id = int(row[0])
                for ov in overrides or []:
                    conn.execute(
                        """
                        INSERT INTO vault_overrides (
                            note, section, unit, write_id, cobalt_text, human_text,
                            attempted_text, conflict, writer, run_id
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            note, section, unit, write_id,
                            ov["cobalt_text"], ov["human_text"], ov["attempted_text"],
                            ov["conflict"], writer, run_id,
                        ),
                    )
                yield write_id
            except BaseException:
                conn.rollback()
                raise
            else:
                conn.commit()

    def overrides_for(self, note: str) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, ts, note, section, unit, write_id, cobalt_text,
                       human_text, attempted_text, conflict, run_id
                FROM vault_overrides WHERE note = %s ORDER BY id
                """,
                (note,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    # -- retention ---------------------------------------------------

    def purge_expired(self, days: int = RETENTION_DAYS) -> int:
        """Drop vault_writes rows past retention. vault_overrides is
        never touched (L28.3: overrides live in their own non-expiring
        table)."""
        with self._connect() as conn:
            cur = conn.execute(
                "DELETE FROM vault_writes WHERE ts < now() - make_interval(days => %s)",
                (days,),
            )
            return cur.rowcount if cur.rowcount and cur.rowcount > 0 else 0
