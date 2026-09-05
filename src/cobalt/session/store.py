"""Persistence for market_reset refusals (the heartbeat-visible counter).

Same shape as every other new-core store: the database is NOT named
here, `COBALT_ENV` chooses it through `cobalt.env.resolve_db_name()`
(RULING 7/9), and `db_name` survives only as the test/tooling seam.

DEGRADATION RULE. Recording a refusal must never be able to turn a
refusal into a pass. `record()` therefore returns None and logs at ERROR
if the database is unreachable — the block already happened by the time
it is called. Loud, and non-blocking, in that order.
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional

from loguru import logger

from cobalt import db, env
from cobalt.session import clock as session_clock_mod

MIGRATIONS_DIR = Path(__file__).parent / "migrations"

#: F16: the heartbeat's lookback window is a tunables row, not a
#: `timedelta(hours=24)` in a method body.
HEARTBEAT_WINDOW_KEY = "session.blocks.heartbeat_window"


class SessionBlockStore:
    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

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

    REFUSED = "refused"
    UNGATED_RUN = "ungated_run"

    def record(
        self, *, session: str, actor: str, target: Optional[str], reason: str,
        kind: str = REFUSED,
    ) -> Optional[int]:
        """Append one refusal. Returns its id, or None if it could not be
        persisted (which is logged at ERROR and never raised — see the
        degradation rule in this module's docstring)."""
        try:
            self.ensure_schema()
            with self._connect() as conn:
                row = conn.execute(
                    "INSERT INTO session_blocks (session, actor, target, reason, kind) "
                    "VALUES (%s, %s, %s, %s, %s) RETURNING id",
                    (session, actor, target, reason, kind),
                ).fetchone()
            return int(row[0]) if row else None
        except Exception as e:
            logger.error(
                "session_blocks: could not persist a {} refusal by {} "
                "({}: {}) — the refusal STANDS; only its counter row is missing.",
                session,
                actor,
                type(e).__name__,
                e,
            )
            return None

    def count_since(self, since: datetime) -> int:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT count(*) FROM session_blocks WHERE ts >= %s", (since,)
            ).fetchone()
        return int(row[0]) if row else 0

    def count_over_window(self, now: Optional[datetime] = None) -> int:
        """The heartbeat's number (F18, S1-P3): refusals over the window
        named by the `session.blocks.heartbeat_window` tunable."""
        from cobalt.taxonomy.loader import load_tunables

        row = load_tunables().by_key.get(HEARTBEAT_WINDOW_KEY)
        if row is None:
            raise RuntimeError(
                f"tunable {HEARTBEAT_WINDOW_KEY!r} is missing from tunables.yaml — "
                "the heartbeat window is config, not a literal (F16)"
            )
        return self.count_since(
            (now or session_clock_mod.now_utc()) - timedelta(minutes=int(row.value))
        )

    def counts_over_window(self, now: Optional[datetime] = None) -> dict[str, int]:
        """The heartbeat's number, SPLIT BY KIND (S1-P3 ruling).

        A refusal and an ungated repair run are both "a write met the
        market_reset window tonight", which is why they share a counter —
        but they are not the same event, and F18 shows both numbers so
        nobody reads five repair runs as five refusals.
        """
        from cobalt.taxonomy.loader import load_tunables

        row = load_tunables().by_key.get(HEARTBEAT_WINDOW_KEY)
        if row is None:
            raise RuntimeError(
                f"tunable {HEARTBEAT_WINDOW_KEY!r} is missing from tunables.yaml — "
                "the heartbeat window is config, not a literal (F16)"
            )
        since = (now or session_clock_mod.now_utc()) - timedelta(minutes=int(row.value))
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT kind, count(*) FROM session_blocks WHERE ts >= %s GROUP BY 1",
                (since,),
            )
            return {r[0]: int(r[1]) for r in cur.fetchall()}

    def recent(self, limit: int = 20) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, ts, session, actor, target, reason, kind "
                "FROM session_blocks ORDER BY id DESC LIMIT %s",
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]
