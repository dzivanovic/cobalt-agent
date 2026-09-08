"""Persistence for ASET sizings.

The database is NOT named here: `COBALT_ENV` chooses it via
`cobalt.env.resolve_db_name()` (RULING 7) — production writes
`cobalt_brain`, dev and the test suite write `cobalt_dev`.

DDL lives under migrations/ (one path — the store executes those files,
it does not carry a second copy of the schema). ensure_schema() runs
every *.sql file in filename order, strips full-line '--' comments
(a semicolon inside a comment must not be mistaken for a statement
terminator), splits what's left on ';', and executes non-empty
statements individually — psycopg's execute() runs one statement at a
time, so a multi-ALTER migration (0002) can't be handed over as a
single execute() call the way 0001's single CREATE TABLE could. Only
full-line comments are stripped — a migration must not put a trailing
comment after SQL on the same line. The table may be reshaped again by
the data-model ADR; see the note in 0001.
"""

from datetime import date, datetime
from pathlib import Path
from typing import Any, Optional

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import clock as session_clock_mod
from cobalt.session import session_clock
from .models import FillRecompute, SizingResult

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class AsetStore:
    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    #: A card is a written plan of HIS — ticker, grade, sheet dollars,
    #: entry and stop. Every column is one trader's own decision (L32).
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        """`db_name` is a TEST/TOOLING seam only. Production and dev both
        leave it None and take the database from `COBALT_ENV` via
        `env.resolve_db_name()` — RULING 7 removed the per-component
        `db_name` config that used to route production writes into
        `cobalt_dev`."""
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def ensure_schema(self) -> None:
        """Every table `save()` writes to — which since S1-P2 includes
        `card_transitions`.

        `save()` creates a card AND its genesis transition in one
        transaction (F7: no card exists without a state), so a schema
        call that set up only `aset_sizings` would leave the write path
        one table short. The cards migrations are EXECUTED from their own
        directory, not copied here (one-path rule); the local import
        avoids the import cycle, since `cards.store` imports this module
        for the reverse direction.
        """
        from cobalt.cards.store import MIGRATIONS_DIR as CARD_MIGRATIONS

        with self._connect() as conn:
            db.assert_schemas_exist(conn)
            for directory in (MIGRATIONS_DIR, CARD_MIGRATIONS):
                for migration in sorted(directory.glob("*.sql")):
                    lines = migration.read_text().splitlines()
                    sql = "\n".join(line for line in lines if not line.strip().startswith("--"))
                    for statement in sql.split(";"):
                        statement = statement.strip()
                        if statement:
                            conn.execute(statement)

    def save(self, result: SizingResult, *, now: Optional[datetime] = None) -> int:
        """Persist a card, stamped with the session it was created in.

        F1 (Charter §3): "every card, alert and note carries the session."
        The session is resolved HERE, in Python, and not derived in SQL
        from `created_at` — the answer depends on the NYSE calendar, and
        the calendar is config. `now` is the test seam; production passes
        nothing. `created_at` keeps its server-side `now()` default: both
        clocks are on this one host, and the alternative (a client
        timestamp) trades a nonexistent skew for a real one.
        """
        # Local import: cobalt.cards.store imports THIS module (for the
        # migration directory), so a module-level import here would be a
        # cycle. The dependency runs one way at import time and both ways
        # at call time, which is the ordinary shape for two tables that
        # are written together.
        from cobalt.cards.models import Actor, CardState, Origin
        from cobalt.cards.store import CardStore

        inp = result.input
        ts = now or session_clock_mod.now_utc()
        session = session_clock().session(ts)

        # ONE TRANSACTION FOR THE CARD AND ITS FIRST STATE (F7).
        # "No card exists without a state" is not a habit the callers
        # keep — it is this `with` block. A crash between the INSERT and
        # the genesis transition rolls both back, so there is no window
        # in which a state-less card is reachable.
        conn = self._connect()
        conn.autocommit = False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO aset_sizings (
                        ticker, grade, direction, sheet_mode,
                        risk_budget, entry, stop, per_share_risk, shares,
                        used_risk, last_price, price_source, warnings, session,
                        state, state_at, origin
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (
                        inp.ticker,
                        inp.grade.value,
                        inp.direction.value,
                        inp.sheet_mode.value,
                        result.risk_budget,
                        inp.entry,
                        inp.stop,
                        result.per_share_risk,
                        result.shares,
                        result.used_risk,
                        inp.last_price,
                        inp.price_source,
                        result.warnings,
                        session.value,
                        # The state is set IN THE INSERT, not by a follow-up
                        # UPDATE. `state` is NOT NULL (migration 0007), so a
                        # card literally cannot exist without one — not even
                        # for the few microseconds between two statements
                        # inside this transaction. The genesis LEDGER row is
                        # written next, in the same transaction; that is what
                        # `create_state(conn=...)` adds.
                        CardState.WATCH.value,
                        ts,
                        # A card written on this sheet is HIS. The column
                        # has a DEFAULT, but the sheet states it anyway:
                        # the one-click fill turns on this value, and a
                        # write path that relied on a default would be a
                        # write path that could silently change meaning
                        # if the default ever moved (S1-P3).
                        Origin.MANUAL.value,
                    ),
                )
                row = cur.fetchone()
                if row is None:
                    raise RuntimeError("INSERT returned no id — persistence failed loudly.")
                row_id = int(row[0])

            CardStore(self.db_name).create_state(
                row_id,
                CardState.WATCH,
                actor=Actor.COBALT,
                evidence={"created_by": "aset.sheet", "ticker": inp.ticker},
                reason="card written",
                now=ts,
                conn=conn,
            )
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return row_id

    def mark_filled(
        self, row_id: int, fill: "FillRecompute", *, now: Optional[datetime] = None
    ) -> None:
        """Fill-recompute persists as an UPDATE to the card row it
        belongs to (2026-09-03, LAW L28 step 3).

        Before this, the recompute wrote a note block and NOTHING to
        Postgres — the 09-03 forensics found the 10:02:36 TSLA FILL
        UPDATE had no DB row at all, which is why the DB could not be
        used to rebuild a note and could not answer "how many cards
        became trades". Fail-loud: a row id that matches nothing raises
        rather than silently updating zero rows."""
        # F7 (S1-P2): a fill is a STATE TRANSITION and it goes through
        # the state machine like every other move — gates, ledger row,
        # evidence, session stamp. `status` is NO LONGER WRITTEN here
        # (the column stays readable; see migrations/0006). The figures
        # below are the fill's own numbers, which belong on the card row,
        # not in the transition.
        #
        # S1-P3: it calls `CardStore.fill()`, not `transition()`, so the
        # actual-fill form and the FILLED button on the open-cards list
        # take the SAME path — including the one-click completion on a
        # manual card. Two ways to fill a card that disagreed about what
        # a fill requires would be exactly the second write path the
        # one-path rule forbids.
        from cobalt.cards.models import Actor
        from cobalt.cards.store import CardStore

        CardStore(self.db_name).fill(
            row_id,
            actor=Actor.YOU,
            evidence={
                "actual_fill": str(fill.actual_fill),
                "recomputed_shares": fill.recomputed_shares,
                "share_delta": fill.share_delta,
                "distance_change_pct": str(fill.distance_change_pct),
                "structural_warning": fill.structural_warning,
            },
            reason=f"filled at {fill.actual_fill}",
            now=now,
        )
        with self._connect() as conn:
            cur = conn.execute(
                """
                UPDATE aset_sizings SET
                    filled_at = now(),
                    actual_fill = %s,
                    recomputed_shares = %s,
                    recomputed_used_risk = %s,
                    share_delta = %s,
                    distance_change_pct = %s
                WHERE id = %s
                """,
                (
                    fill.actual_fill,
                    fill.recomputed_shares,
                    fill.recomputed_used_risk,
                    fill.share_delta,
                    fill.distance_change_pct,
                    row_id,
                ),
            )
            if cur.rowcount != 1:
                raise RuntimeError(
                    f"FILL UPDATE matched {cur.rowcount} rows for aset_sizings id "
                    f"{row_id} (expected exactly 1) — refusing to report a fill "
                    "that was not persisted."
                )

    def counts_for_date(self, day: date) -> tuple[int, int]:
        """(cards written, trades taken) for `day`. A card is a written
        plan, not a trade (DRC ruling, 2026-08-31; L28 step 3 makes it
        countable).

        COUNTS `state`, NOT `status` (S1-P2). `status` stopped being
        written when the F7 machine landed, so a count keyed off it would
        have quietly reported 0 trades taken from that day forward —
        which is precisely the class of silent-miscount the state machine
        exists to end. A card that FILLED and then CLOSED is still a
        trade taken, so both count.
        """
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT count(*),
                       count(*) FILTER (WHERE state IN ('FILLED', 'CLOSED'))
                FROM aset_sizings
                WHERE (created_at AT TIME ZONE 'America/New_York')::date = %s
                """,
                (day,),
            ).fetchone()
        return (int(row[0]), int(row[1])) if row else (0, 0)

    def for_date(self, day: date) -> list[dict[str, Any]]:
        """Every card whose created_at falls on `day` in America/New_York
        (Dejan's trading-day boundary, not the DB session's UTC default),
        oldest first — the DRC prefill's re-entry numbering depends on
        chronological order within a ticker.

        Ordered by `(created_at, id)`, not `created_at` alone. `created_at`
        defaults to `now()`, which in Postgres is the TRANSACTION
        timestamp: two cards written inside one transaction carry the
        SAME created_at and the sort between them was arbitrary — so the
        DRC's re-entry numbering could silently invert. Surfaced by the
        RULING 7.1d transaction fixture (2026-09-04), but it was always
        reachable in production by two saves inside one transaction.
        `id` is an identity column, so it is insertion order by
        construction and the correct tiebreak."""
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, created_at, session, ticker, grade, direction, sheet_mode,
                       risk_budget, entry, stop, per_share_risk, shares, used_risk,
                       state, state_at, status, filled_at, actual_fill, recomputed_shares,
                       recomputed_used_risk, share_delta, distance_change_pct
                FROM aset_sizings
                WHERE (created_at AT TIME ZONE 'America/New_York')::date = %s
                ORDER BY created_at ASC, id ASC
                """,
                (day,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    def recent(self, limit: int = 10) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id, created_at, session, ticker, grade, direction, sheet_mode,
                       risk_budget, entry, stop, shares, used_risk, state, status
                FROM aset_sizings ORDER BY id DESC LIMIT %s
                """,
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]
