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
from decimal import Decimal
from pathlib import Path
from typing import TYPE_CHECKING, Any, NamedTuple, Optional
from loguru import logger

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import clock as session_clock_mod
from cobalt.session import session_clock
from .models import FillRecompute, SizingResult

if TYPE_CHECKING:  # `cobalt.cards` imports this module (the import cycle)
    from cobalt.cards.models import FillResult

MIGRATIONS_DIR = Path(__file__).parent / "migrations"


class FillOutcome(NamedTuple):
    """What THE fill (`AsetStore.mark_filled`) committed, in one transaction."""

    result: "FillResult"        # the FILLED transition ids + the pick outcome
    recompute: FillRecompute    # the cache figures, the P in force, whether it warned
    leg_id: int                 # the entry leg (`"user".legs`, seq 0)
    sheet_mismatch: bool        # recorded on the leg, never a refusal


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
        from cobalt.aset.account_mode import AccountModeUnresolved, resolve

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
            try:
                account_mode = resolve(conn, self._connect_day(ts))
            except AccountModeUnresolved as e:
                logger.error("aset.card REFUSED: {}", e)
                raise
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO aset_sizings (
                        ticker, grade, direction, sheet_mode,
                        risk_budget, entry, stop, per_share_risk, shares,
                        used_risk, last_price, price_source, warnings, session,
                        state, state_at, origin, account_mode
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
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
                        account_mode,
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

    @staticmethod
    def _connect_day(ts: datetime) -> date:
        """The card's ET trading date, using the shared session clock."""
        return session_clock().to_et(ts).date()

    def mark_filled(
        self,
        row_id: int,
        *,
        price: Optional[Decimal],
        shares: Optional[int],
        flag: str,
        price_source: str,
        price_asof: Optional[datetime],
        source: str,
        now: Optional[datetime] = None,
        drift_settings=None,
    ) -> FillOutcome:
        """THE FILL (S3 exits v3 §2 [F-22]; L3). `/fill`, the panel (C3)
        and every later caller fill a card through this and nothing else.

        ONE CONNECTION, ONE TRANSACTION (`[R2F-03]`: `db.connect` opens
        autocommit, so it is switched off here, as `transition()` does):

          1. the card row, `SELECT … FOR UPDATE` — the lock `transition()`
             takes; everything below reads the card as locked;
          2. `SizingResult.from_card(row)` — the only rebuild — and
             `compute_fill_recompute` at `price`, with the drift P in force
             (`cobalt.settings.fills`; None = not evaluated, bannered);
          3. `CardStore.fill(conn=…)` — the FILLED transition(s) and the
             pick, on this transaction;
          4. `legs.insert_entry_leg` — his shares at his price, the stop in
             force (the card's stop read under the lock), today's day-mode
             attestation and whether it matched (O18 default: against
             today's day mode, never refusing);
          5. the fill cache UPDATE (the F6 columns + the P and whether it
             warned);
        then ONE commit. Any exception rolls all of it back and re-raises:
        the card stays where it was, with no transition, no leg, no pick,
        no cache (X1).

        Refused BEFORE any connection: a fill with no price, or no shares.
        The typo guard and the session gate (`market_reset`) refuse inside
        the transaction, which rolls back whole. The day-mode ladder is
        read (its own read) before the transaction opens; it is config.

        `drift_settings` is the settings source for the P — None reads
        `trader_settings` on this transaction; a test passes a constructed
        store (L69).
        """
        from cobalt.aset import config as aset_config
        from cobalt.cards import legs
        from cobalt.cards.models import Actor
        from cobalt.cards.store import CardStateError, CardStore
        from cobalt.daymode import config as daymode_config
        from cobalt.settings.fills import drift_warning_pct

        from .engine import SizingError, compute_fill_recompute

        if price is None:
            raise SizingError(
                f"REFUSED card {row_id}: a fill with no price. Type the price the broker "
                "filled you at — a FILLED with no price is a trade whose R cannot be read. "
                "Nothing written."
            )
        if shares is None or int(shares) <= 0:
            raise SizingError(
                f"REFUSED card {row_id}: a fill with no share count ({shares!r}). Type the "
                "shares the broker filled. Nothing written."
            )
        ts = now or session_clock_mod.now_utc()
        guard = aset_config.load_config().validation.max_fill_distance_pct
        ladder = daymode_config.load_daymode_config()

        conn = self._connect()
        conn.autocommit = False
        try:
            cur = conn.execute(
                "SELECT * FROM aset_sizings WHERE id = %s FOR UPDATE", (row_id,)
            )
            found = cur.fetchone()
            if found is None:
                raise CardStateError(f"no aset_sizings row with id {row_id}")
            card = dict(zip([d.name for d in cur.description], found))
            if card["account_mode"] not in {"live", "sim"}:
                raise CardStateError(
                    f"card {row_id} has no valid account_mode stamp "
                    f"({card['account_mode']!r}) — its entry leg cannot be stamped"
                )

            original = SizingResult.from_card(card)
            pct = drift_warning_pct(conn if drift_settings is None else drift_settings)
            recompute = compute_fill_recompute(original, price, guard, drift_warning_pct=pct)

            filled = CardStore(self.db_name).fill(
                row_id,
                actor=Actor.YOU,
                evidence={
                    "actual_fill": str(recompute.actual_fill),
                    "shares": int(shares),
                    "recomputed_shares": recompute.recomputed_shares,
                    "share_delta": recompute.share_delta,
                    "distance_change_pct": str(recompute.distance_change_pct),
                    "drift_warning_pct": None if pct is None else str(pct),
                    "drift_warned": recompute.drift_warned,
                    "structural_warning": recompute.structural_warning,
                    "price_source": price_source,
                    "source": source,
                },
                reason=f"filled at {recompute.actual_fill}",
                now=ts,
                conn=conn,
            )

            day_mode_id, attested, mismatch = self._attestation(conn, ts, ladder)
            leg_id = legs.insert_entry_leg(
                conn,
                row_id,
                shares=int(shares),
                price=price,
                at=ts,
                flag=flag,
                price_source=price_source,
                price_asof=price_asof,
                source=source,
                stop_in_force=card["stop"],
                session=session_clock().session(ts).value,
                account_mode=card["account_mode"],
                day_mode_id=day_mode_id,
                attested_sheet=attested,
                sheet_mismatch=mismatch,
            )
            self._update_fill_cache(conn, row_id, recompute)
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return FillOutcome(result=filled, recompute=recompute, leg_id=leg_id, sheet_mismatch=mismatch)

    @staticmethod
    def _attestation(conn, ts: datetime, ladder) -> tuple[Optional[date], Optional[str], bool]:
        """(day_modes key, attested file, sheet_mismatch) for the fill's ET
        day, on the fill's transaction. Mismatch when nothing is attested,
        when the attested file is not a declared one, or when its sheet is
        not the sheet of the day mode in force (S3 exits v3 §8; O18
        default). Recorded, never refused."""
        from cobalt.daymode import decided_or_stage1
        from cobalt.daymode.config import ConfigError

        day = session_clock().to_et(ts).date()
        cur = conn.execute("SELECT * FROM day_modes WHERE trade_date = %s", (day,))
        found = cur.fetchone()
        if found is None:
            return None, None, True
        row = dict(zip([d.name for d in cur.description], found))
        attested = row.get("attested_sheet")
        if not attested:
            return row["trade_date"], None, True
        try:
            attested_sheet = ladder.sheet_for_hotkey_file(attested)
        except ConfigError:
            return row["trade_date"], attested, True
        in_force = ladder.sheet_for(decided_or_stage1(row, ladder, ts))
        return row["trade_date"], attested, attested_sheet != in_force

    def _update_fill_cache(self, conn, row_id: int, fill: FillRecompute) -> None:
        """The F6 fill columns — a cache of the entry leg + the recompute,
        written only by `mark_filled`, on its transaction (v3 Q4)."""
        cur = conn.execute(
            """
            UPDATE aset_sizings SET
                filled_at = now(),
                actual_fill = %s,
                recomputed_shares = %s,
                recomputed_used_risk = %s,
                share_delta = %s,
                distance_change_pct = %s,
                drift_warning_pct = %s,
                drift_warned = %s
            WHERE id = %s
            """,
            (
                fill.actual_fill,
                fill.recomputed_shares,
                fill.recomputed_used_risk,
                fill.share_delta,
                fill.distance_change_pct,
                fill.drift_warning_pct,
                fill.drift_warned,
                row_id,
            ),
        )
        if cur.rowcount != 1:
            raise RuntimeError(
                f"FILL UPDATE matched {cur.rowcount} rows for aset_sizings id "
                f"{row_id} (expected exactly 1) — refusing to report a fill "
                "that was not persisted."
            )

    def account_mode_for(self, row_id: int) -> str:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT account_mode FROM aset_sizings WHERE id = %s", (row_id,)
            ).fetchone()
        if row is None or row[0] not in {"live", "sim"}:
            raise RuntimeError(f"card {row_id} has no valid account_mode stamp")
        return str(row[0])

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
                SELECT id, created_at, session, account_mode, ticker, grade, direction, sheet_mode,
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
                SELECT id, created_at, session, account_mode, ticker, grade, direction, sheet_mode,
                       risk_budget, entry, stop, shares, used_risk, state, status
                FROM aset_sizings ORDER BY id DESC LIMIT %s
                """,
                (limit,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]
