"""Persistence for the vault's trade_defs — the loaded copy (ADR-0008 D3).

Same shape as every other new-core store: the database is NOT named here
(`COBALT_ENV` chooses it via `cobalt.env.resolve_db_name()`, RULING 7),
`db_name` survives only as the test/tooling seam, and the DDL lives in
`migrations/` and is executed, never re-typed (one-path rule).

USER SIDE, and not a close call. A trade_def is the trader's own
strategy: everything named after a trade, everything SMB- or
cheat-sheet-derived, every setting that is one trader's choice is user
data and is never shipped to another Cobalt user (L32). Same for the
per-trade tunable rows.

THE VAULT IS THE TRUTH AND THIS TABLE IS A CACHE, so `sync()` is a
REPLACE, not a merge: every def in the read is upserted, and every slug
in the table that the read did not produce is DELETED. A def a trader
removed from their note is a def that stops existing — a row that
outlived its note would be a strategy the radar still fires on and the
vault no longer documents, which is the exact disagreement the one-path
rule exists to prevent. Both counts are returned and printed, because a
delete nobody was told about is the failure mode of a replace.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

from pydantic import BaseModel, ConfigDict

from cobalt import db, env
from cobalt.db import Side

from .vault_loader import VaultTradeDefs

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class SyncCounts(BaseModel):
    """What one `sync()` changed. Printed by `cobalt taxonomy load`."""

    model_config = ConfigDict(extra="forbid")

    defs_upserted: int = 0
    defs_deleted: int = 0
    tunables_upserted: int = 0
    tunables_deleted: int = 0
    #: Named, not just counted: "2 defs deleted" is a number, "these two
    #: slugs are gone from the vault" is a fact someone can check.
    deleted_slugs: list[str] = []
    deleted_tunable_keys: list[str] = []

    def report(self) -> str:
        lines = [
            f"trade_defs : {self.defs_upserted} upserted, {self.defs_deleted} deleted",
            f"tunables   : {self.tunables_upserted} upserted, "
            f"{self.tunables_deleted} deleted",
        ]
        if self.deleted_slugs:
            lines.append(f"  slugs no longer in the vault: {self.deleted_slugs}")
        if self.deleted_tunable_keys:
            lines.append(f"  tunable keys removed: {self.deleted_tunable_keys}")
        return "\n".join(lines)


class TradeDefStore:
    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    #: A trade_def is the trader's own strategy and its per-trade tunable
    #: rows are their own numbers. User data outright (L32).
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

    def slugs(self) -> list[str]:
        with self._connect() as conn:
            return [r[0] for r in conn.execute("SELECT slug FROM trade_defs ORDER BY slug")]

    def get(self, slug: str) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT slug, name, def, md5, note_path, loaded_at, user_id "
                "FROM trade_defs WHERE slug = %s",
                (slug,),
            )
            row = cur.fetchone()
            if row is None:
                return None
            return dict(zip([d.name for d in cur.description], row))

    def matrix(self) -> list[tuple[str, str, str]]:
        """`setup_trade_matrix` rows — the artifact S2's radar reads."""
        with self._connect() as conn:
            return [
                (r[0], r[1], r[2])
                for r in conn.execute(
                    "SELECT trade_def, setup_ref, relation FROM setup_trade_matrix "
                    "ORDER BY trade_def, setup_ref, relation"
                )
            ]

    def tunable_keys(self) -> list[str]:
        with self._connect() as conn:
            return [r[0] for r in conn.execute("SELECT key FROM tunables ORDER BY key")]

    # -- the one write path -------------------------------------------

    def sync(self, result: VaultTradeDefs) -> SyncCounts:
        """Make the tables equal the vault read. One transaction.

        Defs and tunables move together: a per-trade row references its
        def, and committing the two separately would leave a window in
        which a key resolves against a def that is not there.
        """
        counts = SyncCounts()
        conn = self._connect()
        conn.autocommit = False
        try:
            with conn.cursor() as cur:
                for loaded in result.defs:
                    cur.execute(
                        """
                        INSERT INTO trade_defs (slug, name, def, md5, note_path, loaded_at)
                        VALUES (%s, %s, %s::jsonb, %s, %s, now())
                        ON CONFLICT (slug) DO UPDATE SET
                            name = EXCLUDED.name,
                            def = EXCLUDED.def,
                            md5 = EXCLUDED.md5,
                            note_path = EXCLUDED.note_path,
                            loaded_at = EXCLUDED.loaded_at
                        """,
                        (
                            loaded.slug,
                            loaded.name,
                            loaded.definition.model_dump_json(),
                            loaded.md5,
                            loaded.note_path,
                        ),
                    )
                    counts.defs_upserted += 1

                live_slugs = [d.slug for d in result.defs]
                cur.execute(
                    "DELETE FROM trade_defs WHERE NOT (slug = ANY(%s)) RETURNING slug",
                    (live_slugs,),
                )
                counts.deleted_slugs = sorted(r[0] for r in cur.fetchall())
                counts.defs_deleted = len(counts.deleted_slugs)

                for tunable in result.user_tunables:
                    cur.execute(
                        """
                        INSERT INTO tunables (key, row, slug, loaded_at)
                        VALUES (%s, %s::jsonb, %s, now())
                        ON CONFLICT (key) DO UPDATE SET
                            row = EXCLUDED.row,
                            slug = EXCLUDED.slug,
                            loaded_at = EXCLUDED.loaded_at
                        """,
                        (
                            tunable.key,
                            json.dumps(tunable.row.model_dump(mode="json")),
                            tunable.slug,
                        ),
                    )
                    counts.tunables_upserted += 1

                live_keys = [t.key for t in result.user_tunables]
                cur.execute(
                    "DELETE FROM tunables WHERE NOT (key = ANY(%s)) RETURNING key",
                    (live_keys,),
                )
                counts.deleted_tunable_keys = sorted(r[0] for r in cur.fetchall())
                counts.tunables_deleted = len(counts.deleted_tunable_keys)
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return counts


__all__ = ["MIGRATIONS_DIR", "SyncCounts", "TradeDefStore"]
