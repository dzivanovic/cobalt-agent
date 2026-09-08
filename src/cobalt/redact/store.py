"""F19's counter — what the F18 heartbeat reports.

One row per redaction event, carrying the CHANNEL and the pattern NAME
and nothing else. There is no column that could hold a secret, which is
deliberate: the table is queried by whoever is debugging an alert, and a
schema with nowhere to put a value cannot leak one by accident.

The table is `cobalt_redactions`, prefixed for the reason recorded in
`jobs/migrations/0001_cobalt_jobs.sql`: `cobalt_brain` shares its
database with Mattermost's tables until 2026-09-04, when Mattermost
moved to its own `mattermost` database (ADR-0006). The prefix stays: it
is what made the collision impossible in the first place, and the
one-path rule says a name earns its prefix once.

Database from `COBALT_ENV` via `env.resolve_db_name()` (RULING 7/9).
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import clock as clock_mod

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class RedactionStore:
    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    #: Counts by pattern NAME. The schema deliberately has nowhere to put
    #: a secret or a value, so there is nothing user-side about it.
    SIDE = Side.SYSTEM

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

    def record(self, *, channel: str, hits: dict[str, int]) -> None:
        self.ensure_schema()
        rows = [(channel, name, int(n)) for name, n in sorted(hits.items())]
        with self._connect() as conn:
            with conn.cursor() as cur:
                cur.executemany(
                    "INSERT INTO cobalt_redactions (channel, pattern, hits) VALUES (%s, %s, %s)",
                    rows,
                )

    def count_since(self, since: datetime) -> int:
        """Total redacted secrets since `since` — the heartbeat's number."""
        with self._connect() as conn:
            row = conn.execute(
                "SELECT coalesce(sum(hits), 0) FROM cobalt_redactions WHERE ts >= %s", (since,)
            ).fetchone()
        return int(row[0]) if row else 0

    def by_pattern_since(self, since: datetime) -> list[tuple[str, str, int]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT channel, pattern, sum(hits) FROM cobalt_redactions WHERE ts >= %s "
                "GROUP BY 1, 2 ORDER BY 3 DESC",
                (since,),
            )
            return [(r[0], r[1], int(r[2])) for r in cur.fetchall()]

    def recent(self, limit: int = 20) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, ts, channel, pattern, hits FROM cobalt_redactions "
                "ORDER BY id DESC LIMIT %s",
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    def count_over_minutes(self, minutes: int, now: Optional[datetime] = None) -> int:
        return self.count_since((now or clock_mod.now_utc()) - timedelta(minutes=minutes))


__all__ = ["RedactionStore"]
