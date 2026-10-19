"""Persistence for the chief of staff: sessions and turns (F20 C3a; L18).

The `jobs/store.py` shape: the database is NOT named here (`COBALT_ENV`
chooses it), `db_name` is the test/tooling seam, the DDL lives in
`migrations/` and is executed rather than re-typed.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

from cobalt import db, env
from cobalt.db import Side

MIGRATIONS_DIR = Path(__file__).parent / "migrations"
TURN_STATES = ("pending", "running", "done", "failed")
#: The columns a finished turn may carry (the turn row of FINAL §2).
TURN_FIELDS = ("num_turns", "result_subtype", "is_error", "terminal_reason", "error")


class CosStore:
    #: ADR-0008 D2 — his conversation is one trader's record (card DECISION 4).
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

    # -- turns ----------------------------------------------------------

    def insert_turn(self, message_ref: str) -> int:
        """The `pending` row, before the session is called. A second insert of
        one ref raises `UniqueViolation` (T11)."""
        with self._connect() as conn:
            (turn,) = conn.execute(
                "INSERT INTO cobalt_cos_turns (message_ref) VALUES (%s) RETURNING id", (message_ref,)
            ).fetchone()
        return int(turn)

    def set_turn(self, turn_id: int, state: str, **fields: Any) -> None:
        if state not in TURN_STATES:
            raise ValueError(f"turn state {state!r} is not one of {TURN_STATES}")
        unknown = sorted(set(fields) - set(TURN_FIELDS))
        if unknown:
            raise ValueError(f"unknown turn field(s) {unknown}")
        sets = ["state = %s"]
        params: list[Any] = [state]
        if state == "running":
            sets.append("started_at = now()")
        if state in ("done", "failed"):
            sets.append("finished_at = now()")
        for name in TURN_FIELDS:
            if name in fields:
                sets.append(f"{name} = %s")
                params.append(fields[name])
        params.append(int(turn_id))
        with self._connect() as conn:
            conn.execute(f"UPDATE cobalt_cos_turns SET {', '.join(sets)} WHERE id = %s", tuple(params))

    def turn(self, turn_id: int) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM cobalt_cos_turns WHERE id = %s", (int(turn_id),))
            row = cur.fetchone()
            return dict(zip([d.name for d in cur.description], row)) if row else None

    def last_turn(self) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM cobalt_cos_turns ORDER BY id DESC LIMIT 1")
            row = cur.fetchone()
            return dict(zip([d.name for d in cur.description], row)) if row else None

    # -- sessions -------------------------------------------------------

    def session(self, channel: str, agent_id: str) -> Optional[dict[str, Any]]:
        """The current (`active`) session for a channel and agent."""
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT * FROM cobalt_cos_sessions WHERE channel = %s AND agent_id = %s "
                "AND state = 'active' ORDER BY id DESC LIMIT 1", (channel, agent_id))
            row = cur.fetchone()
            return dict(zip([d.name for d in cur.description], row)) if row else None

    def save_session(self, channel: str, agent_id: str, session_id: str, state: str = "active") -> None:
        """Store the session id to resume by. A new id rotates the old row."""
        with self._connect() as conn:
            with conn.transaction():
                conn.execute(
                    "UPDATE cobalt_cos_sessions SET state = 'rotated', rotated_at = now() "
                    "WHERE channel = %s AND agent_id = %s AND state = 'active' AND session_id <> %s",
                    (channel, agent_id, session_id))
                same = conn.execute(
                    "SELECT 1 FROM cobalt_cos_sessions WHERE channel = %s AND agent_id = %s "
                    "AND state = 'active' AND session_id = %s", (channel, agent_id, session_id),
                ).fetchone()
                if same is None or state != "active":
                    conn.execute(
                        "INSERT INTO cobalt_cos_sessions (channel, agent_id, session_id, state) "
                        "VALUES (%s, %s, %s, %s)", (channel, agent_id, session_id, state))


__all__ = ["CosStore", "MIGRATIONS_DIR", "TURN_FIELDS", "TURN_STATES"]
