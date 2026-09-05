"""F17 persistence: the `jobs` row, and the kill switch behind it.

Database from `COBALT_ENV` via `env.resolve_db_name()` (RULING 7/9);
`db_name` is the test/tooling seam only.

NOT SESSION-GATED, and this one is deliberate. `cobalt.session`'s
market_reset hard block exists to stop Cobalt WRITING TRADING RECORD in
the 20:00-21:00 window. A job's own state is not trading record — and the
archiver, the one job that runs squarely inside that window by design
(20:30, its own carve-out in L28), is exactly the job whose failure the
heartbeat most needs to see. A `jobs` table that went blind for an hour
every evening would go blind for the hour it matters most.
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Optional

from cobalt import db, env
from cobalt.session import clock as clock_mod

from .config import JobSpec
from .models import JobState, Supervisor

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class JobStoreError(RuntimeError):
    """A job operation was refused."""


class JobStore:
    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self, *, allow_prod: bool = False):
        return db.connect(self.db_name, allow_prod=allow_prod)

    def ensure_schema(self, *, allow_prod: bool = False) -> None:
        with self._connect(allow_prod=allow_prod) as conn:
            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
                lines = migration.read_text().splitlines()
                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
                for statement in sql.split(";"):
                    statement = statement.strip()
                    if statement:
                        conn.execute(statement)

    # -- registration -------------------------------------------------

    def register(self, spec: JobSpec, *, allow_prod: bool = False) -> None:
        """Upsert one row from its config spec. IDEMPOTENT, and it does
        NOT touch runtime columns: re-registering after a config edit
        must never erase the last run's exit code, which is the one thing
        an operator looks at first."""
        with self._connect(allow_prod=allow_prod) as conn:
            conn.execute(
                "INSERT INTO jobs (label, kind, expected_cadence, timeout_s, "
                "heartbeat_source) VALUES (%s, %s, %s, %s, %s) "
                "ON CONFLICT (label) DO UPDATE SET kind = EXCLUDED.kind, "
                "expected_cadence = EXCLUDED.expected_cadence, "
                "timeout_s = EXCLUDED.timeout_s, "
                "heartbeat_source = EXCLUDED.heartbeat_source, updated_at = now()",
                (
                    spec.label,
                    spec.kind.value,
                    spec.cadence,
                    spec.timeout_s,
                    spec.supervisor.value,
                ),
            )

    def register_all(self, registry, *, allow_prod: bool = False) -> list[str]:
        self.ensure_schema(allow_prod=allow_prod)
        for spec in registry.jobs:
            self.register(spec, allow_prod=allow_prod)
        return [s.label for s in registry.jobs]

    # -- reads --------------------------------------------------------

    def get(self, label: str) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM jobs WHERE label = %s", (label,))
            row = cur.fetchone()
            if row is None:
                return None
            return dict(zip([d.name for d in cur.description], row))

    def all(self) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM jobs ORDER BY kind DESC, label")
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    # -- the run lifecycle (the wrapper's three calls) -----------------

    def mark_running(self, label: str, *, now: Optional[datetime] = None) -> None:
        ts = now or clock_mod.now_utc()
        with self._connect() as conn:
            cur = conn.execute(
                "UPDATE jobs SET state = %s, started_at = %s, heartbeat_at = %s, "
                "finished_at = NULL, exit_code = NULL, last_error = NULL, "
                "updated_at = now() WHERE label = %s",
                (JobState.RUNNING.value, ts, ts, label),
            )
            if cur.rowcount != 1:
                raise JobStoreError(
                    f"no jobs row for {label!r} — register it first "
                    "(`cobalt jobs register`). F17 refuses to run a job it cannot "
                    "report on: an unregistered job that hangs is invisible."
                )

    def beat(self, label: str, *, now: Optional[datetime] = None) -> None:
        """Stamp `heartbeat_at`. The only thing separating a long job
        from a hung one."""
        with self._connect() as conn:
            conn.execute(
                "UPDATE jobs SET heartbeat_at = %s, updated_at = now() WHERE label = %s",
                (now or clock_mod.now_utc(), label),
            )

    def mark_finished(
        self,
        label: str,
        *,
        exit_code: int,
        error: Optional[str] = None,
        result: Optional[dict[str, Any]] = None,
        now: Optional[datetime] = None,
    ) -> None:
        """`done` on 0, `failed` on anything else. Failed is LOUD: F18
        turns red on this column, and the error text goes with it."""
        ts = now or clock_mod.now_utc()
        state = JobState.DONE if exit_code == 0 else JobState.FAILED
        # F19: a job's own error text is outbound the moment F18 puts it
        # in a DM. Redacting at the point of STORAGE means a traceback
        # carrying a DSN never becomes a row that later leaks.
        safe_error = None
        if error:
            from cobalt.redact import redact

            safe_error = redact(error, channel="jobs.last_error").text
        with self._connect() as conn:
            conn.execute(
                "UPDATE jobs SET state = %s, finished_at = %s, heartbeat_at = %s, "
                "exit_code = %s, last_error = %s, last_result = %s, updated_at = now() "
                "WHERE label = %s",
                (
                    state.value,
                    ts,
                    ts,
                    exit_code,
                    safe_error,
                    json.dumps(result, default=str) if result is not None else None,
                    label,
                ),
            )

    def mark_zombie(self, label: str, *, reason: str) -> None:
        """The watchdog's conclusion. Nothing else may write this state."""
        from cobalt.redact import redact

        with self._connect() as conn:
            conn.execute(
                "UPDATE jobs SET state = %s, last_error = %s, updated_at = now() "
                "WHERE label = %s",
                (JobState.ZOMBIE.value, redact(reason, channel="jobs.last_error").text, label),
            )

    def mark_probe(
        self,
        label: str,
        *,
        alive: bool,
        detail: str,
        now: Optional[datetime] = None,
    ) -> None:
        """Stamp a resident whose heartbeat comes from a PROBE, not from
        itself (`supervisor: launchd | pidfile`).

        A probe says "the process exists". That is a weaker claim than a
        wrapper's "I am running and past my gates", which is why
        `heartbeat_source` is a column: the two must never be read as the
        same evidence.
        """
        from cobalt.redact import redact

        ts = now or clock_mod.now_utc()
        safe = redact(detail, channel="jobs.last_error").text
        with self._connect() as conn:
            if alive:
                conn.execute(
                    "UPDATE jobs SET state = %s, heartbeat_at = %s, last_error = NULL, "
                    "updated_at = now() WHERE label = %s",
                    (JobState.RUNNING.value, ts, label),
                )
            else:
                conn.execute(
                    "UPDATE jobs SET state = %s, last_error = %s, updated_at = now() "
                    "WHERE label = %s",
                    (JobState.FAILED.value, safe, label),
                )

    # -- the kill switch (F17d) ---------------------------------------

    def kill_switch(self) -> dict[str, Any]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM kill_switch WHERE id = TRUE")
            row = cur.fetchone()
            if row is None:
                return {"active": False}
            return dict(zip([d.name for d in cur.description], row))

    def set_kill_switch(
        self, *, active: bool, phrase: Optional[str], by: str,
        now: Optional[datetime] = None,
    ) -> dict[str, Any]:
        ts = now or clock_mod.now_utc()
        with self._connect() as conn:
            if active:
                conn.execute(
                    "UPDATE kill_switch SET active = TRUE, phrase = %s, set_by = %s, "
                    "set_at = %s, cleared_by = NULL, cleared_at = NULL WHERE id = TRUE",
                    (phrase, by, ts),
                )
            else:
                conn.execute(
                    "UPDATE kill_switch SET active = FALSE, cleared_by = %s, "
                    "cleared_at = %s WHERE id = TRUE",
                    (by, ts),
                )
        return self.kill_switch()

    # -- what F18 reads -----------------------------------------------

    def counts_by_state(self) -> dict[str, int]:
        with self._connect() as conn:
            cur = conn.execute("SELECT state, count(*) FROM jobs GROUP BY 1")
            return {r[0]: int(r[1]) for r in cur.fetchall()}

    def last_result(self, label: str) -> Optional[dict[str, Any]]:
        row = self.get(label)
        return (row or {}).get("last_result")


__all__ = ["JobStore", "JobStoreError"]
