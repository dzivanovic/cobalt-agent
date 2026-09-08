"""Persistence for the trader's settings (ADR-0008 D3.4).

Same shape as every other new-core store: the database is NOT named here
(`COBALT_ENV` chooses it), `db_name` is the test/tooling seam, the DDL
lives in `migrations/` and is executed rather than re-typed.

USER SIDE, and the clearest case of it in the whole data model. How much
a trader risks on a B, which grades he takes, what makes today a smaller
day — none of that is engine, all of it is one person's ruling, and none
of it may ever be visible to another Cobalt user (L32).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from cobalt import db, env
from cobalt.db import Side

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class TraderSettingsStore:
    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    #: A sheet dollar is one trader's number. There is no engine reading
    #: of "how much he risks", so there is no system-side copy.
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def ensure_schema(self) -> None:
        with self._connect() as conn:
            db.assert_schemas_exist(conn)
            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
                conn.execute(migration.read_text())

    # -- reads --------------------------------------------------------

    def rows(self) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT key, value, source, updated_at FROM trader_settings "
                "ORDER BY key"
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    def values(self) -> dict[str, Any]:
        """`{key: value}` — what `TraderSettings.from_db` builds from."""
        return {row["key"]: row["value"] for row in self.rows()}

    # -- the one write path -------------------------------------------

    def put(self, rows: dict[str, Any], *, source: str) -> dict[str, str]:
        """Upsert every setting in `rows`. Returns `{key: created|updated
        |unchanged}` so the caller can report what actually moved.

        One transaction: a half-applied settings load is a config that
        validates nowhere, which is the failure the per-top-level-setting
        row layout was chosen to avoid in the first place.
        """
        before = self.values()
        outcome: dict[str, str] = {}
        conn = self._connect()
        conn.autocommit = False
        try:
            with conn.cursor() as cur:
                for key, value in rows.items():
                    if key in before and before[key] == value:
                        outcome[key] = "unchanged"
                        continue
                    outcome[key] = "updated" if key in before else "created"
                    cur.execute(
                        """
                        INSERT INTO trader_settings (key, value, source, updated_at)
                        VALUES (%s, %s::jsonb, %s, now())
                        ON CONFLICT (user_id, key) DO UPDATE SET
                            value = EXCLUDED.value,
                            source = EXCLUDED.source,
                            updated_at = EXCLUDED.updated_at
                        """,
                        (key, json.dumps(value), source),
                    )
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return outcome


__all__ = ["MIGRATIONS_DIR", "TraderSettingsStore"]
