"""F6 persistence: one `day_modes` row per trading day.

Database from `COBALT_ENV` via `env.resolve_db_name()` (RULING 7/9);
`db_name` is the test/tooling seam only.

WHAT IS AND IS NOT PERSISTED. Stage 1 has NO ROW: "the lowest enabled
mode" is a system rule computed from config, and storing a constant
invites someone to edit the stored copy instead of the config. A row
appears when the 09:00 job proposes, and `decided` stays NULL until he
answers — which is exactly the state the sheet reads as "still on the
stage-1 mode".
"""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any, Optional

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import assert_writable
from cobalt.session import clock as clock_mod

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class DayModeError(RuntimeError):
    """A day-mode write was refused."""


class DayModeStore:
    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    #: Which sheet he is trading today, and what he decided when Cobalt
    #: proposed otherwise. His day, his call.
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self, *, allow_prod: bool = False):
        return db.connect(self.db_name, side=self.SIDE, allow_prod=allow_prod)

    def ensure_schema(self, *, allow_prod: bool = False) -> None:
        with self._connect(allow_prod=allow_prod) as conn:
            db.assert_schemas_exist(conn)
            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
                lines = migration.read_text().splitlines()
                sql = "\n".join(l for l in lines if not l.strip().startswith("--"))
                for statement in sql.split(";"):
                    statement = statement.strip()
                    if statement:
                        conn.execute(statement)

    def for_date(self, day: date) -> Optional[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute("SELECT * FROM day_modes WHERE trade_date = %s", (day,))
            row = cur.fetchone()
            if row is None:
                return None
            return dict(zip([d.name for d in cur.description], row))

    def upsert_proposal(
        self,
        day: date,
        *,
        proposed: str,
        reason: str,
        now: Optional[datetime] = None,
    ) -> None:
        """Write (or refresh) the 09:00 proposal. Idempotent per day.

        A re-run REPLACES the proposal and clears nothing he decided:
        `decided` and its reason are left alone, because a second job run
        must never silently un-answer a question he already answered.
        """
        ts = now or clock_mod.now_utc()
        session = assert_writable("daymode.propose", target=day.isoformat(), now=ts)
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO day_modes (trade_date, stage, proposed, reason, session, created_at) "
                "VALUES (%s, 'stage2', %s, %s, %s, %s) "
                "ON CONFLICT (trade_date) DO UPDATE SET "
                "proposed = EXCLUDED.proposed, reason = EXCLUDED.reason",
                (day, proposed, reason, session.value, ts),
            )

    def decide(
        self,
        day: date,
        *,
        decided: str,
        decided_by: str,
        overrule_reason: Optional[str] = None,
        now: Optional[datetime] = None,
    ) -> dict[str, Any]:
        """Persist APPROVE or OVERRULE. An overrule carries its reason.

        The rule is checked against what was actually PROPOSED, read back
        here rather than trusted from the caller — the sheet's hidden
        field is not the authority on what Cobalt said.
        """
        ts = now or clock_mod.now_utc()
        assert_writable("daymode.decide", target=day.isoformat(), now=ts)
        row = self.for_date(day)
        if row is None:
            raise DayModeError(
                f"no day_modes row for {day} — there is nothing to decide yet. "
                f"The 09:00 proposal has not run, or {day} is not a trading day."
            )
        if not row["proposed"]:
            raise DayModeError(
                f"the {day} row exists but carries no proposal — it was created by an "
                "early `.htk` attestation, while stage 1 was still in force. There is "
                "nothing to approve or overrule until the 09:00 job has run."
            )
        if decided != row["proposed"] and not (overrule_reason or "").strip():
            raise DayModeError(
                f"REFUSED: overruling the proposal ({row['proposed']} -> {decided}) "
                "requires a reason. Charter §3 F6 — 'his approve/overrule WITH REASON "
                "persists'. The reason is the calibration data; a bare override is a "
                "decision nobody can learn from later."
            )
        with self._connect() as conn:
            conn.execute(
                "UPDATE day_modes SET decided = %s, decided_by = %s, decided_at = %s, "
                "overrule_reason = %s WHERE trade_date = %s",
                (decided, decided_by, ts, overrule_reason, day),
            )
        return self.for_date(day)

    def attest_sheet(
        self,
        day: date,
        *,
        filename: str,
        account_mode: Optional[str] = None,
        now: Optional[datetime] = None,
    ) -> None:
        """Record which `.htk` he states he has loaded (F6 match check).

        ATTESTED, NEVER READ — see match.py. Upserts a row if none
        exists so he can attest before 09:00, while stage 1 is still in
        force and no proposal has been made.
        """
        if account_mode is not None and account_mode not in {"live", "sim"}:
            raise DayModeError(
                f"REFUSED: account_mode must be live or sim, got {account_mode!r}"
            )
        ts = now or clock_mod.now_utc()
        session = assert_writable("daymode.attest", target=day.isoformat(), now=ts)
        with self._connect() as conn:
            conn.execute(
                "INSERT INTO day_modes (trade_date, stage, proposed, reason, session, "
                "attested_sheet, attested_at, account_mode) "
                "VALUES (%s, 'stage1', %s, %s, %s, %s, %s, %s) "
                "ON CONFLICT (trade_date) DO UPDATE SET "
                "attested_sheet = EXCLUDED.attested_sheet, attested_at = EXCLUDED.attested_at, "
                "account_mode = COALESCE(EXCLUDED.account_mode, day_modes.account_mode)",
                (
                    day,
                    "",
                    "attested before any proposal — stage 1 in force",
                    session.value,
                    filename,
                    ts,
                    account_mode,
                ),
            )

    def recent(self, limit: int = 20) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT trade_date, stage, proposed, decided, decided_by, "
                "attested_sheet, reason FROM day_modes ORDER BY trade_date DESC LIMIT %s",
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]


__all__ = ["DayModeError", "DayModeStore"]
