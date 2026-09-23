"""`"user".voice_turns` — the voice module's ONE table (L40: its own rows).

THE ROW IS THE TASK ROW (L18). Every state change is ONE single-flight
statement, `UPDATE … WHERE turn_id = %s AND state = ANY(<expected>)
RETURNING`: the first confirm or cancel commits, a second in-flight request
finds no pending action (FINAL [F-08]). Every state stamps its own
`<state>_at` from the caller's clock. The REAPER moves a row stuck in
`received` / `transcribing` / `planned` / `executing` past its limit to
`failed: reaped_<state>`; a reaped `executing` row is NEVER retried (the
reaper marks, it never executes). `awaiting_confirm` ends only by confirm,
cancel or TTL (`expire_pending`).

NOT SESSION-GATED (FINAL [F-16], the `jobs/store.py` precedent): a turn row
is the voice module's own state, not trading record; inside `market_reset`
a read turn is answered and every ACT is refused by its owning expert's own
gate.

NO BYTES (R18 (b)): the updatable columns are a CLOSED list with no
audio column; the clip's sha256, length and duration are metadata.

Database from `COBALT_ENV` (`env.resolve_db_name()`); `connect` is the
test / tooling seam (two REAL connections for the single-flight proof).
"""

from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Callable, Iterable, Optional

from psycopg import sql
from psycopg.types.json import Jsonb

from cobalt import db, env
from cobalt.db import Side

from .models import TurnState

#: The columns a caller may set (besides `state` and its stamp).
UPDATABLE = frozenset({
    "transcript", "stt_engine", "stt_model", "stt_revision", "stt_ms",
    "audio_sha256", "audio_bytes", "audio_duration_ms", "audio_deleted_at",
    "plan", "plan_route", "model_returned", "plan_latency_ms", "plan_usage",
    "resolution", "reply", "pending_action", "confirm_of", "expert_write_kind", "expert_write_id",
    "failure_class", "failure_detail",
})
_JSON = frozenset({"plan", "plan_usage", "resolution", "pending_action"})

TRANSITION_SQL_TEMPLATE = (
    "UPDATE voice_turns SET state = %s, {stamp} = %s, updated_at = %s{sets} "
    "WHERE turn_id = %s AND state = ANY(%s) RETURNING turn_id"
)

#: Reaper margin on top of the engine budgets (seconds).
REAP_MARGIN_S = 30


def reap_limits(*, stt_timeout_s: float, plan_timeout_s: float) -> dict[TurnState, float]:
    """How long a row may sit in a working state before the reaper fails it.
    A text turn waits in `received` through its Plan call; an audio turn
    sits in `transcribing` through speech-to-text AND its Plan call."""
    return {
        TurnState.RECEIVED: plan_timeout_s + REAP_MARGIN_S,
        TurnState.TRANSCRIBING: stt_timeout_s + plan_timeout_s + REAP_MARGIN_S,
        TurnState.PLANNED: REAP_MARGIN_S * 2,
        TurnState.EXECUTING: REAP_MARGIN_S * 2,
    }


def _set_clause(fields: dict[str, Any]) -> tuple[str, list[Any]]:
    unknown = sorted(set(fields) - UPDATABLE)
    if unknown:
        raise ValueError(f"voice_turns has no updatable column(s) {unknown}")
    parts, params = [], []
    for k in sorted(fields):
        v = fields[k]
        parts.append(f", {k} = %s")
        params.append(Jsonb(v) if (k in _JSON and v is not None) else v)
    return "".join(parts), params


class VoiceTurnStore:
    #: ADR-0008 D2: one trader's words and the commands they ran.
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None, *, connect: Optional[Callable] = None):
        self.db_name = db_name or env.resolve_db_name()
        self._connect_override = connect

    def _connect(self):
        if self._connect_override is not None:
            return self._connect_override()
        return db.connect(self.db_name, side=self.SIDE)

    # -- writes ---------------------------------------------------------------

    def create(self, *, turn_id: str, session_id: str, source: str, input_kind: str, at: datetime,
               confirm_of: Optional[str] = None) -> None:
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO voice_turns (turn_id, session_id, source, state, input_kind, confirm_of, "
                "received_at, updated_at) VALUES (%s, %s, %s, 'received', %s, %s, %s, %s)",
                (turn_id, session_id, source, input_kind, confirm_of, at, at),
            )
            conn.commit()

    def update(self, turn_id: str, **fields: Any) -> None:
        """Non-state fields on the row as it stands (e.g. the transcript)."""
        if not fields:
            return
        sets, params = _set_clause(fields)
        with self._connect() as conn:
            conn.execute(f"UPDATE voice_turns SET updated_at = updated_at{sets} WHERE turn_id = %s",
                         (*params, turn_id))
            conn.commit()

    def transition(self, turn_id: str, expected: Iterable[TurnState], new: TurnState, *, at: datetime,
                   **fields: Any) -> bool:
        """Single-flight: True iff THIS call moved the row."""
        sets, params = _set_clause(fields)
        stamp = f"{new.value}_at"
        q = TRANSITION_SQL_TEMPLATE.format(stamp=stamp, sets=sets)
        with self._connect() as conn:
            row = conn.execute(q, (new.value, at, at, *params, turn_id,
                                   [s.value for s in expected])).fetchone()
            conn.commit()
        return row is not None

    def expire_pending(self, *, now: datetime) -> list[str]:
        """`awaiting_confirm` past its pending action's `expires_at` → expired."""
        with self._connect() as conn:
            rows = conn.execute(
                "UPDATE voice_turns SET state = 'expired', expired_at = %s, updated_at = %s "
                "WHERE state = 'awaiting_confirm' AND (pending_action->>'expires_at')::timestamptz <= %s "
                "RETURNING turn_id",
                (now, now, now),
            ).fetchall()
            conn.commit()
        return [r[0] for r in rows]

    def reap(self, *, now: datetime, limits: dict[TurnState, float]) -> list[tuple[str, str]]:
        """Stuck working rows → `failed: reaped_<state>`. Marks only."""
        out: list[tuple[str, str]] = []
        with self._connect() as conn:
            for state, secs in limits.items():
                stamp = sql.Identifier(f"{state.value}_at")
                q = sql.SQL(
                    "UPDATE voice_turns SET state = 'failed', failed_at = %s, updated_at = %s, "
                    "failure_class = %s, failure_detail = %s "
                    "WHERE state = %s AND {stamp} < %s RETURNING turn_id"
                ).format(stamp=stamp)
                rows = conn.execute(q, (now, now, f"reaped_{state.value}",
                                        f"no progress in {state.value} for more than {int(secs)} s",
                                        state.value, now - timedelta(seconds=secs))).fetchall()
                out.extend((r[0], state.value) for r in rows)
            conn.commit()
        return out

    # -- reads ----------------------------------------------------------------

    def get(self, turn_id: str) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM voice_turns WHERE turn_id = %s", (turn_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return dict(zip([d.name for d in cur.description], row))

    def pending_for_session(self, session_id: str) -> Optional[dict[str, Any]]:
        """The newest `awaiting_confirm` row of THIS widget session."""
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT * FROM voice_turns WHERE session_id = %s AND state = 'awaiting_confirm' "
                "ORDER BY received_at DESC, id DESC LIMIT 1", (session_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return dict(zip([d.name for d in cur.description], row))

    def history(self, session_id: str, limit: int) -> list[tuple[str, str]]:
        """The last `limit` finished turns of THIS session (transcript, reply),
        oldest first — the agent is stateless and reads its history here (L2)."""
        if limit <= 0:
            return []
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT transcript, reply FROM voice_turns WHERE session_id = %s "
                "AND transcript IS NOT NULL AND reply IS NOT NULL "
                "ORDER BY received_at DESC, id DESC LIMIT %s", (session_id, limit)).fetchall()
        return [(t, r) for t, r in reversed(rows)]

    def delete_test_rows(self, session_id: str) -> int:
        """Test seam only: remove rows a with-DB test committed for real."""
        if not session_id.startswith("sess-"):
            raise ValueError("delete_test_rows is for constructed test sessions only")
        with self._connect() as conn:
            n = conn.execute("DELETE FROM voice_turns WHERE session_id = %s", (session_id,)).rowcount
            conn.commit()
        return n


__all__ = ["REAP_MARGIN_S", "TRANSITION_SQL_TEMPLATE", "UPDATABLE", "VoiceTurnStore", "reap_limits"]
