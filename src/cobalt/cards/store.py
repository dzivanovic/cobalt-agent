"""F7 persistence: the card's state and the ledger behind it.

Same shape as every other new-core store — the database is NOT named
here, `COBALT_ENV` chooses it via `cobalt.env.resolve_db_name()`
(RULING 7/9), and `db_name` survives only as the test/tooling seam.

THE ONE INVARIANT THIS MODULE EXISTS TO HOLD. `aset_sizings.state` and
`card_transitions` are written in ONE database transaction or neither is
written. A card whose column says ARMED with no ARMED row in the ledger
is a card whose DRC count is a guess, and F7's acceptance test is that
those counts match Postgres. So `transition()` opens an explicit
transaction, re-reads the current state INSIDE it (`FOR UPDATE`), checks
the edge against that re-read value, and commits both writes together.

WHY `FOR UPDATE` AND NOT A READ-THEN-WRITE. The sheet and the expiry job
can touch the same card in the same second — the 16:05 job expiring a
WATCH card while he taps ARM. Without the row lock both would read
WATCH, both would find their edge legal, and the ledger would record two
different next states for one card. With it, the second one re-reads
ARMED and is refused by name, which is the correct answer.

ORDER OF GATES, and it is deliberate:

    1. F1 session guard   (market_reset -> refused, nothing else runs)
    2. edge legality      (illegal -> refused, named)
    3. reason requirement (MISSED and disarm need one)
    4. the two writes, atomically

The F1 gate is FIRST because a refused write must leave no trace of
having been attempted — that is what S1-P1 built the guard for, and the
S1-P2 test "a card in market_reset refused by F1 before any state logic
runs" is asserting exactly this ordering.
"""

from __future__ import annotations

import json
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any, Optional

from loguru import logger

from cobalt import db, env
from cobalt.db import Side
from cobalt.aset.store import MIGRATIONS_DIR as ASET_MIGRATIONS
from cobalt.session import assert_writable, session_clock
from cobalt.session import clock as clock_mod

from . import picks
from .models import (
    ALLOWED,
    FILL_TARGET,
    STOP_EDITABLE,
    TERMINAL,
    Actor,
    CardState,
    FillResult,
    IllegalTransition,
    Origin,
    assert_edge,
    fill_path,
)

#: The evidence a row Cobalt inserted on his behalf carries. Queryable:
#: `evidence->>'auto' = 'manual_fill'` separates the transitions he made
#: from the ones the shortcut made FOR him — Charter §1's "his taps are
#: the calibration set" only survives if the two are never summed.
AUTO_FILL_EVIDENCE = {"auto": "manual_fill"}

MIGRATIONS_DIR = Path(__file__).parent / "migrations"

#: The evidence marker every backfilled genesis row carries, so a row
#: Cobalt classified retrospectively is never mistaken for one it watched
#: happen. Queryable: `evidence->>'backfill' = 'S1-P2'`.
BACKFILL_MARKER = "S1-P2"


class CardStateError(RuntimeError):
    """A state operation was refused for a reason other than the edge."""


def _exec_file(conn, path: Path) -> None:
    lines = path.read_text().splitlines()
    sql = "\n".join(line for line in lines if not line.strip().startswith("--"))
    for statement in sql.split(";"):
        statement = statement.strip()
        if statement:
            conn.execute(statement)


class CardStore:
    #: ADR-0008 D2 — the side is chosen PER STORE, never per process.
    #: The card ledger is the card's own history, so it sits where the
    #: card sits. `card_stop_edits` likewise.
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self, *, allow_prod: bool = False):
        return db.connect(self.db_name, side=self.SIDE, allow_prod=allow_prod)

    # -- schema -------------------------------------------------------

    #: Migrations that can only be applied once the data is in shape.
    #: Named by suffix rather than by number so adding another one needs
    #: no edit here.
    NOT_NULL_SUFFIX = "_not_null.sql"

    def ensure_schema(
        self, *, allow_prod: bool = False, include_not_null: bool = True
    ) -> None:
        """Card DDL, in dependency order.

        `card_transitions` carries a foreign key to `aset_sizings`, and
        `aset_sizings.state` is added by that table's OWN migration
        (aset/0006) — this store executes the aset module's files rather
        than carrying a second copy of the DDL (one-path rule). It does
        NOT reimplement AsetStore.ensure_schema(): it calls the same
        files in the same order.

        `include_not_null=False` skips the constraint migrations
        (`*_not_null.sql`) so the BACKFILL can create the column it is
        about to populate. Applying `state SET NOT NULL` to a table that
        still has un-backfilled rows fails — correctly, since the
        alternative is a DEFAULT that invents a state for a card nobody
        classified — but it must not fail *before the backfill has had a
        chance to run*. `cobalt cards backfill` calls this with False,
        then calls it again with the default True once the data is in
        shape. Same two-step `cobalt session backfill` uses.
        """
        with self._connect(allow_prod=allow_prod) as conn:
            db.assert_schemas_exist(conn)
            for directory in (ASET_MIGRATIONS, MIGRATIONS_DIR):
                for migration in sorted(directory.glob("*.sql")):
                    if not include_not_null and migration.name.endswith(
                        self.NOT_NULL_SUFFIX
                    ):
                        continue
                    _exec_file(conn, migration)

    # -- reads --------------------------------------------------------

    def state_of(self, card_id: int) -> CardState:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT state FROM aset_sizings WHERE id = %s", (card_id,)
            ).fetchone()
        if row is None:
            raise CardStateError(f"no aset_sizings row with id {card_id}")
        if row[0] is None:
            raise CardStateError(
                f"card {card_id} has NO STATE. Every card has one (F7) — this row "
                "predates the state column and was not backfilled. Run "
                "`cobalt cards backfill`."
            )
        return CardState(row[0])

    def history(self, card_id: int) -> list[dict[str, Any]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, card_id, from_state, to_state, at, session, actor, "
                "evidence, reason FROM card_transitions WHERE card_id = %s "
                "ORDER BY id",
                (card_id,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    def state_distribution(self) -> list[tuple[str, int]]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT coalesce(state, '(null)'), count(*) FROM aset_sizings "
                "GROUP BY 1 ORDER BY 2 DESC, 1"
            )
            return [(r[0], int(r[1])) for r in cur.fetchall()]

    def transition_count(self) -> int:
        with self._connect() as conn:
            row = conn.execute("SELECT count(*) FROM card_transitions").fetchone()
        return int(row[0]) if row else 0

    def origin_of(self, card_id: int) -> Origin:
        with self._connect() as conn:
            row = conn.execute(
                "SELECT origin FROM aset_sizings WHERE id = %s", (card_id,)
            ).fetchone()
        if row is None:
            raise CardStateError(f"no aset_sizings row with id {card_id}")
        return Origin(row[0])

    def filled_with_picks(self, day: date) -> list[dict[str, Any]]:
        """Every FILLED transition on ET `day`, left-joined to its pick.

        Driven by `card_transitions`, not by current `state`, card creation
        date or `filled_at` (S2-P4, Astra R1-7): a card that later CLOSED
        still carries its pick, and the direct-button route never sets
        `filled_at`. A FILLED transition with no pick row is a gap —
        `cobalt cards picks` prints it MISSING.
        """
        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT t.id AS transition_id, t.card_id, t.at AS filled_at, s.ticker,
                       s.state, s.origin, p.id AS pick_id, p.not_in_pool, p.pool_basis,
                       p.pool_rank, p.pool_size, p.rank_metric, p.rank_value, p.card_score,
                       p.card_score_rank, p.focus_top4, p.score_basis
                FROM card_transitions t
                JOIN aset_sizings s ON s.id = t.card_id
                LEFT JOIN picks p ON p.transition_id = t.id
                WHERE t.to_state = 'FILLED'
                  AND (t.at AT TIME ZONE 'America/New_York')::date = %s
                ORDER BY t.at, t.id
                """,
                (day,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    def open_cards(self) -> list[dict[str, Any]]:
        """Cards not in a terminal state — what the expiry job considers
        and what the sheet lists. Derived from ALLOWED, so adding a
        non-terminal state does not need an edit here."""
        live = sorted(s.value for s in CardState if ALLOWED[s])
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, created_at, ticker, grade, direction, sheet_mode, "
                "entry, stop, shares, state, state_at, session, origin, account_mode "
                "FROM aset_sizings WHERE state = ANY(%s) ORDER BY id",
                (live,),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    # -- the one write path -------------------------------------------

    def transition(
        self,
        card_id: int,
        to_state: CardState,
        *,
        actor: Actor,
        evidence: Optional[dict[str, Any]] = None,
        reason: Optional[str] = None,
        now: Optional[datetime] = None,
        allow_prod: bool = False,
        conn=None,
        before_commit=None,
    ) -> int:
        """Move a card. Returns the `card_transitions` row id.

        Refuses in `market_reset` (F1), refuses an illegal edge by name
        (F7), and refuses a MISSED or a disarm with no reason. Writes the
        ledger row and the card's cached state in one transaction.

        `conn` lets a caller pass an OPEN transaction so several hops
        commit together — `fill()`'s one-click walk is the only caller
        that does, and it does so because a shortcut that crashed halfway
        would leave a card ARMED that nobody armed. Same seam, same
        reasoning, as `create_state(conn=...)`.
        """
        # GATE 1 — F1, before anything else. A refused write must leave
        # no trace of having been attempted.
        ts = now or clock_mod.now_utc()
        session = assert_writable(f"cards.transition.{to_state.value}", target=str(card_id), now=ts)

        owned = conn is None
        if owned:
            conn = self._connect(allow_prod=allow_prod)
            conn.autocommit = False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT state, grade, risk_budget, shares, used_risk FROM aset_sizings "
                    "WHERE id = %s FOR UPDATE",
                    (card_id,),
                )
                row = cur.fetchone()
                if row is None:
                    raise CardStateError(f"no aset_sizings row with id {card_id}")
                if row[0] is None:
                    raise CardStateError(
                        f"card {card_id} has NO STATE — run `cobalt cards backfill` "
                        "before moving it (F7: no card exists without a state)."
                    )
                from_state = CardState(row[0])

                # GATE 2 — the edge, against the value re-read under the
                # lock, not against whatever the caller last saw.
                assert_edge(from_state, to_state, card_id=card_id)

                # GATE 2b — THE SIZED-CARD ARM INVARIANT (S2-P2, Astra R1-6).
                # A radar card is born unsized. ARM is a risk commitment, so
                # it is refused here, under the row lock, for EVERY caller —
                # the sheet button, the radar tap route, anything later —
                # unless the four sizing columns are filled.
                if to_state is CardState.ARMED:
                    unsized = [
                        name for name, value in zip(("grade", "risk_budget", "shares", "used_risk"), row[1:])
                        if value is None
                    ]
                    if unsized:
                        raise CardStateError(
                            f"REFUSED card {card_id}: {from_state.value} -> ARMED on an UNSIZED card "
                            f"({', '.join(unsized)} empty). Tap a key first — ARM commits risk, and a "
                            "card with no size has none to commit."
                        )

                # GATE 3 — the reasons that are not optional.
                self._assert_reason(from_state, to_state, reason)

                # Decision 11: fold every stop edit made since the last
                # transition into THIS row's evidence.
                payload = dict(evidence or {})
                pending_ids, pending = self._pending_stop_edits(cur, card_id)
                if pending:
                    payload["stop_edits"] = pending

                cur.execute(
                    "INSERT INTO card_transitions "
                    "(card_id, from_state, to_state, at, session, actor, evidence, reason) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id",
                    (
                        card_id,
                        from_state.value,
                        to_state.value,
                        ts,
                        session.value,
                        actor.value,
                        json.dumps(payload, default=str),
                        reason,
                    ),
                )
                transition_id = int(cur.fetchone()[0])

                cur.execute(
                    "UPDATE aset_sizings SET state = %s, state_at = %s WHERE id = %s",
                    (to_state.value, ts, card_id),
                )
                if cur.rowcount != 1:
                    raise CardStateError(
                        f"state UPDATE matched {cur.rowcount} rows for card {card_id} "
                        "(expected exactly 1) — refusing to report a transition that "
                        "was not persisted."
                    )
                if pending_ids:
                    # Marked BY ID, not by "everything still unfolded for
                    # this card". `record_stop_edit` does not take the
                    # card lock, so an edit inserted between the SELECT
                    # above and this UPDATE would otherwise be marked
                    # folded into a transition whose evidence never
                    # carried it — silently losing the one record of a
                    # moved stop, which is the 09-03 lesson exactly.
                    cur.execute(
                        "UPDATE card_stop_edits SET folded_into = %s WHERE id = ANY(%s)",
                        (transition_id, pending_ids),
                    )
            if before_commit is not None:
                before_commit()
            if owned:
                conn.commit()
            return transition_id
        except BaseException:
            if owned:
                conn.rollback()
            raise
        finally:
            if owned:
                conn.close()

    @staticmethod
    def _assert_reason(
        from_state: CardState, to_state: CardState, reason: Optional[str]
    ) -> None:
        """MISSED and disarm carry a reason or they do not happen.

        MISSED because Charter §3 F7 says it is "counted, not hidden" —
        a count with no explanation is the hiding. Disarm because
        ARMED -> WATCH is the one backwards edge, and an unexplained
        un-commitment is the thing the DRC most needs to read back.
        """
        needs = {
            (CardState.WATCH, CardState.MISSED): (
                "MISSED means the trigger fired while the card was unarmed. It is "
                "counted, not hidden (Charter §3 F7), and a count with no reason is "
                "the hiding — say what happened."
            ),
            (CardState.ARMED, CardState.WATCH): (
                "DISARM walks the card backwards out of a risk commitment. Give the "
                "reason now, while it is true — the DRC asks for it later."
            ),
        }
        message = needs.get((from_state, to_state))
        if message and not (reason or "").strip():
            raise CardStateError(
                f"REFUSED {from_state.value} -> {to_state.value}: a reason is "
                f"required. {message}"
            )

    @staticmethod
    def _pending_stop_edits(cur, card_id: int) -> tuple[list[int], list[dict[str, Any]]]:
        """(ids, rendered) for the stop edits not yet folded into a
        transition. The ids come back so the caller marks exactly the
        rows it rendered — see the note at the UPDATE."""
        cur.execute(
            "SELECT id, at, in_state, from_stop, to_stop, actor FROM card_stop_edits "
            "WHERE card_id = %s AND folded_into IS NULL ORDER BY id",
            (card_id,),
        )
        rows = cur.fetchall()
        return (
            [r[0] for r in rows],
            [
                {
                    "at": at.isoformat(),
                    "in_state": in_state,
                    "from_stop": str(from_stop),
                    "to_stop": str(to_stop),
                    "actor": actor,
                }
                for _, at, in_state, from_stop, to_stop, actor in rows
            ],
        )

    # -- the one fill path (F7 one-click fill) ------------------------

    def fill(
        self,
        card_id: int,
        *,
        actor: Actor = Actor.YOU,
        evidence: Optional[dict[str, Any]] = None,
        reason: Optional[str] = None,
        now: Optional[datetime] = None,
        allow_prod: bool = False,
    ) -> FillResult:
        """Fill a card. THE entry point for reaching FILLED.

        Returns a `FillResult`: the `card_transitions` row ids written, in
        order — three on a one-click fill from WATCH, one on a fill of an
        already TRIGGERED card — and whether the F3 pick row was recorded.

        ONE TRANSACTION ON EVERY ROUTE (S2-P4, Astra R1-4). The fill opens
        one USER transaction and passes it to every `transition()` hop,
        the strict single-hop route included. After the FILLED hop, still
        inside it, `picks.record_pick` runs under `SAVEPOINT pick`. Any
        exception there rolls back to the savepoint ONLY: the fill commits,
        `pick_recorded` is False with the error named, and one ERROR line
        (card id + error class) goes to the process log — for the sheet,
        `com.cobalt.aset`'s stderr, `~/cobalt/logs/aset.err`. A failure of
        the fill itself (a hop, the savepoint rollback, the commit) rolls
        everything back and raises; it never returns a result.

        ONE CLICK ON A MANUAL CARD (CTO review of S1-P2, 2026-09-04).
        A card whose `origin` is `manual` may be filled from WATCH or
        ARMED: Cobalt inserts the ARMED and/or TRIGGERED rows it is
        missing, itself, with `actor=cobalt` and evidence
        `{"auto": "manual_fill"}`, at the SAME timestamp as the fill.

        THE EDGE TABLE IS UNCHANGED. The route comes from `fill_path()`,
        which is a breadth-first walk of `ALLOWED` — every inserted row
        is an edge the table already permits, written through the same
        `transition()` every button uses, with the same gates. This is a
        convenience OVER the table, not a new edge in it, and the
        evidence marker means the ledger never claims he tapped ARM.

        A `radar` card gets no shortcut. The S2 detector's entire claim
        is that it watched the arm and the trigger happen; a fill that
        skipped them is a hole in that record, so it is refused by name
        (`IllegalTransition`) exactly as it was before this method
        existed.
        """
        ts = now or clock_mod.now_utc()
        state = self.state_of(card_id)
        origin = self.origin_of(card_id)

        if state is FILL_TARGET:
            raise IllegalTransition(state, FILL_TARGET, card_id)

        route = fill_path(state)
        # Strict path: radar cards, and manual cards already sitting one
        # legal edge away. `transition()` raises by name if the single
        # edge is not legal (a terminal card, say).
        strict = origin is not Origin.MANUAL or len(route) <= 1

        # EVERY HOP IN ONE TRANSACTION. A shortcut that crashed between
        # ARMED and TRIGGERED would leave a card armed that nobody armed
        # — a state with a ledger row behind it and no decision behind
        # the row. All of it lands, or none of it does.
        ids: list[int] = []
        conn = self._connect(allow_prod=allow_prod)
        conn.autocommit = False
        try:
            if not strict:
                for hop in route[:-1]:
                    ids.append(
                        self.transition(
                            card_id, hop,
                            actor=Actor.COBALT,
                            evidence=dict(AUTO_FILL_EVIDENCE),
                            reason=(
                                f"inserted by the one-click fill: a manual card cannot reach "
                                f"{FILL_TARGET.value} without passing through {hop.value}, and "
                                "the trader filled it. Not his tap — actor is cobalt."
                            ),
                            now=ts,
                            conn=conn,
                        )
                    )
            ids.append(
                self.transition(
                    card_id, FILL_TARGET, actor=actor, evidence=evidence,
                    reason=reason, now=ts, conn=conn,
                )
            )
            pick_id, pick_error = self._record_pick(conn, card_id, ids[-1], ts)
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return FillResult(
            transition_ids=ids,
            pick_recorded=pick_id is not None,
            pick_id=pick_id,
            pick_error=pick_error,
        )

    @staticmethod
    def _record_pick(
        conn, card_id: int, transition_id: int, ts: datetime
    ) -> tuple[Optional[int], Optional[str]]:
        """F3 pick under `SAVEPOINT pick` (S2-P4 R2). Returns (pick id,
        None) or (None, "<ErrorClass>: <message>").

        Only `Exception` is caught: an interrupt still aborts the fill. If
        the ROLLBACK TO SAVEPOINT itself fails the connection is unusable
        and that error propagates — the fill rolls back and raises.
        """
        conn.execute(f"SAVEPOINT {picks.PICK_SAVEPOINT}")
        try:
            pick_id = picks.record_pick(conn, card_id, transition_id, ts)
        except Exception as exc:
            conn.execute(f"ROLLBACK TO SAVEPOINT {picks.PICK_SAVEPOINT}")
            logger.error(
                "card {}: pick NOT recorded ({}) — the fill commits; "
                "`cobalt cards picks` reports it MISSING",
                card_id,
                type(exc).__name__,
            )
            return None, f"{type(exc).__name__}: {exc}"
        conn.execute(f"RELEASE SAVEPOINT {picks.PICK_SAVEPOINT}")
        return pick_id, None

    # -- genesis ------------------------------------------------------

    def create_state(
        self,
        card_id: int,
        state: CardState = CardState.WATCH,
        *,
        actor: Actor = Actor.COBALT,
        evidence: Optional[dict[str, Any]] = None,
        reason: Optional[str] = None,
        now: Optional[datetime] = None,
        conn=None,
    ) -> int:
        """Give a brand-new card its first state + genesis transition.

        `from_state` is NULL on this row and on no other (enforced by a
        partial unique index) — that is "no card exists without a state"
        written as a constraint rather than a habit.

        `conn` lets the caller pass an OPEN transaction so the card row
        and its genesis row commit together; the ASET sheet does this, so
        a crash between the two cannot leave a state-less card.

        NOT SESSION-GATED, unlike `transition()`, and deliberately. This
        is never the outermost write. Its two callers are:

        * `AsetStore.save()`, whose caller (`aset/web.py` POST /size)
          already ran `assert_writable("aset.card")` — gating again here
          would refuse identically and write a SECOND `session_blocks`
          row for one refused card, inflating the heartbeat's counter.
        * `backfill()`, which is migration tooling. Same carve-out as
          `cobalt session backfill` (S1-P1) and `VaultWriter.restore`:
          locking a migration out for an hour would mean the one hour you
          most need to repair state is the hour you cannot. It is run
          deliberately, by a human, and it says which database it wrote.

        Card CREATION inside `market_reset` is still refused — at the
        sheet, before any of this runs, and `test_cards.py` asserts the
        ordering.
        """
        ts = now or clock_mod.now_utc()
        session = session_clock().session(ts)
        owned = conn is None
        if owned:
            conn = self._connect()
            conn.autocommit = False
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO card_transitions "
                    "(card_id, from_state, to_state, at, session, actor, evidence, reason) "
                    "VALUES (%s, NULL, %s, %s, %s, %s, %s, %s) RETURNING id",
                    (
                        card_id,
                        state.value,
                        ts,
                        session.value,
                        actor.value,
                        json.dumps(evidence or {}, default=str),
                        reason,
                    ),
                )
                transition_id = int(cur.fetchone()[0])
                cur.execute(
                    "UPDATE aset_sizings SET state = %s, state_at = %s WHERE id = %s",
                    (state.value, ts, card_id),
                )
                if cur.rowcount != 1:
                    raise CardStateError(
                        f"genesis UPDATE matched {cur.rowcount} rows for card "
                        f"{card_id} (expected exactly 1)."
                    )
            if owned:
                conn.commit()
            return transition_id
        except BaseException:
            if owned:
                conn.rollback()
            raise
        finally:
            if owned:
                conn.close()

    # -- stop edits (decision 11) -------------------------------------

    def record_stop_edit(
        self,
        card_id: int,
        *,
        from_stop,
        to_stop,
        actor: Actor = Actor.YOU,
        now: Optional[datetime] = None,
    ) -> int:
        """Log a stop move. NOT a state change — no transition row.

        Refused unless the card is in a state where the stop is his to
        move (decision 11: WATCH and IN-TRADE/FILLED). In ARMED the whole
        summary strip is locked; in a terminal state the card is done.
        """
        ts = now or clock_mod.now_utc()
        session = assert_writable("cards.stop_edit", target=str(card_id), now=ts)
        state = self.state_of(card_id)
        if state not in STOP_EDITABLE:
            raise CardStateError(
                f"REFUSED: the stop is not editable in {state.value}. Decision 11 — "
                "the stop moves with structure in WATCH and in-trade (FILLED); from "
                "ARMED onward the summary strip is locked, because the key is a risk "
                f"commitment. Editable states: {', '.join(sorted(s.value for s in STOP_EDITABLE))}."
            )
        # Decision 11: "stop edits recompute shares/risk/targets/room
        # live". Updating `stop` alone would leave `shares` and
        # `used_risk` describing the OLD stop — a card that lies about
        # the position it is asking for. The recompute runs through
        # `engine.recompute_for_stop`, the same arithmetic
        # `compute_sizing` uses, so the two can never disagree.
        from cobalt.aset.engine import recompute_for_stop, stop_distance
        from cobalt.aset.models import Direction

        with self._connect() as conn:
            card = conn.execute(
                "SELECT entry, direction, risk_budget, shares, state FROM aset_sizings "
                "WHERE id = %s FOR UPDATE",
                (card_id,),
            ).fetchone()
            if card is None:
                raise CardStateError(f"no aset_sizings row with id {card_id}")
            entry, direction, risk_budget, shares, locked_state = card

            if risk_budget is None:
                # AN UNSIZED RADAR CARD (S2-P2, Astra R1-6). No key tapped,
                # so there is no budget to divide by — the old path raised a
                # first-use TypeError here. The stop still moves (side-checked
                # through the one distance path) and the live per-share risk
                # still updates, so proximity and a later key tap read the
                # stop he chose; the sizing columns stay NULL.
                if CardState(locked_state) is not CardState.WATCH:
                    raise CardStateError(
                        f"card {card_id} is unsized in {locked_state} — only a WATCH card may be unsized"
                    )
                distance = stop_distance(
                    entry=entry, stop=Decimal(str(to_stop)), direction=Direction(direction)
                )
                row = conn.execute(
                    "INSERT INTO card_stop_edits "
                    "(card_id, at, session, in_state, from_stop, to_stop, actor) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id",
                    (card_id, ts, session.value, state.value, from_stop, to_stop, actor.value),
                ).fetchone()
                conn.execute(
                    "UPDATE aset_sizings SET stop = %s, per_share_risk = %s WHERE id = %s",
                    (to_stop, distance, card_id),
                )
                return int(row[0])

            recomputed = recompute_for_stop(
                entry=entry,
                stop=Decimal(str(to_stop)),
                direction=Direction(direction),
                risk_budget=risk_budget,
                # In-trade the shares are already bought; a wider stop
                # cannot un-buy them, so it changes OPEN RISK, not size.
                in_trade_shares=shares if state is CardState.FILLED else None,
            )

            row = conn.execute(
                "INSERT INTO card_stop_edits "
                "(card_id, at, session, in_state, from_stop, to_stop, actor) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id",
                (card_id, ts, session.value, state.value, from_stop, to_stop, actor.value),
            ).fetchone()
            conn.execute(
                "UPDATE aset_sizings SET stop = %s, per_share_risk = %s, shares = %s, "
                "used_risk = %s WHERE id = %s",
                (
                    to_stop,
                    recomputed.per_share_risk,
                    recomputed.shares,
                    recomputed.used_risk,
                    card_id,
                ),
            )
        return int(row[0])

    # -- backfill -----------------------------------------------------

    def backfill(
        self, *, today: date, dry_run: bool = False, allow_prod: bool = False
    ) -> dict[str, int]:
        """Classify every state-less card, with a genesis row each.

        The rule (S1-P2): `status = 'FILLED'` -> FILLED; otherwise a
        trade date BEFORE `today` -> EXPIRED (the day is over and the
        card was never resolved), and `today` -> WATCH (still live).

        WHY NOT IN SQL. The trade date is the ET calendar date of
        `created_at`, and each row needs its OWN genesis transition
        stamped with the SESSION it was created in — which depends on the
        NYSE calendar. Same reasoning as the F1 `session` backfill: it is
        computed here, through the same resolver every write uses.

        A FILLED row is NOT given a synthetic WATCH -> ... -> FILLED
        history. Inventing four transitions that never happened would put
        fabricated rows in the ledger the DRC counts. It gets ONE genesis
        row landing directly on FILLED, marked as a backfill, which is
        the honest shape: Cobalt knows where the card ended and does not
        know how it got there.
        """
        clock = session_clock()
        # RULING 2026-09-04 (S1-P3, decided-with-veto): this runs inside
        # market_reset if that is when it is needed — but never quietly.
        # One loud line, and the same counter F18 shows.
        from cobalt.session import note_ungated

        note_ungated(
            "cards.backfill",
            target=self.db_name,
            why="classifying state-less cards is repair tooling; refusing it inside "
                "the block would lock recovery out of the hour it is most needed",
        )
        # The column must exist before it can be populated, and the
        # NOT NULL must NOT be applied yet — see ensure_schema's note.
        self.ensure_schema(allow_prod=allow_prod, include_not_null=False)
        conn = self._connect(allow_prod=allow_prod)
        conn.autocommit = False
        counts = {s.value: 0 for s in CardState}
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, created_at, status FROM aset_sizings "
                    "WHERE state IS NULL ORDER BY id"
                )
                rows = cur.fetchall()
                for card_id, created_at, status in rows:
                    trade_day = clock.to_et(created_at).date()
                    if status == "FILLED":
                        state = CardState.FILLED
                    elif trade_day < today:
                        state = CardState.EXPIRED
                    else:
                        state = CardState.WATCH
                    counts[state.value] += 1
                    self.create_state(
                        card_id,
                        state,
                        actor=Actor.COBALT,
                        evidence={
                            "backfill": BACKFILL_MARKER,
                            "from_status": status,
                            "trade_date": trade_day.isoformat(),
                            "rule": (
                                "status=FILLED -> FILLED"
                                if status == "FILLED"
                                else f"trade date {'<' if trade_day < today else '=='} "
                                f"{today.isoformat()} -> {state.value}"
                            ),
                        },
                        reason="S1-P2 backfill: no state existed before the F7 machine.",
                        now=created_at,
                        conn=conn,
                    )
                cur.execute("SELECT count(*) FROM aset_sizings WHERE state IS NULL")
                left = int(cur.fetchone()[0])
                if left:
                    raise CardStateError(
                        f"ABORT: {left} card(s) still have no state after backfill"
                    )
            if dry_run:
                conn.rollback()
            else:
                conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        counts["_total"] = sum(v for k, v in counts.items() if not k.startswith("_"))
        return counts


    # -- radar cards (S2-P2 STEP-4/6) ----------------------------------
    #
    # ONE CREATION PATH for an unsized radar card (Astra R1-7): the row,
    # its genesis transition and its dots in one transaction, through
    # `create_state` — the same genesis every card gets. Taps, key taps
    # and promotes take the card's row lock (R1-14). Nothing here decides
    # a number: the pure modules (`cards.scoring`, `aset.engine`) do, and
    # the store writes what they return.

    RADAR_OPEN_STATES = ("WATCH", "ARMED", "TRIGGERED", "FILLED")

    def _write_tx(self, label: str, target: str, now: Optional[datetime], work, before_commit=None):
        ts = now or clock_mod.now_utc()
        assert_writable(label, target=target, now=ts)
        conn = self._connect()
        conn.autocommit = False
        try:
            result = work(conn, ts)
            if before_commit is not None:
                before_commit()
            conn.commit()
            return result
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()

    @staticmethod
    def _dot_params(card_id: int, dot) -> tuple:
        return (
            card_id, dot.factor, dot.position, dot.source, dot.tier, dot.role, dot.engine_value,
            dot.engine_grade, dot.engine_why,
            json.dumps(dot.engine_inputs, default=str) if dot.engine_inputs is not None else None,
            dot.engine_formula, dot.na_reason, json.dumps(dot.history, default=str),
            dot.trader_grade, dot.tapped_at,
        )

    def _dots_for(self, conn, card_ids: list[int]) -> dict[int, list]:
        from .scoring import Dot

        out: dict[int, list] = {card_id: [] for card_id in card_ids}
        if not card_ids:
            return out
        cur = conn.execute(
            "SELECT card_id, factor, position, source, tier, role, engine_value, engine_grade, engine_why, "
            "engine_inputs, engine_formula, na_reason, history, trader_grade, tapped_at FROM card_dots "
            "WHERE card_id = ANY(%s) ORDER BY card_id, position",
            (card_ids,),
        )
        for r in cur.fetchall():
            out[r[0]].append(Dot(
                factor=r[1], position=r[2], source=r[3], tier=r[4], role=r[5], engine_value=r[6],
                engine_grade=r[7], engine_why=r[8], engine_inputs=r[9], engine_formula=r[10],
                na_reason=r[11], history=r[12] or [], trader_grade=r[13], tapped_at=r[14],
            ))
        return out

    def open_radar_cards(self) -> list:
        from cobalt.radar.evaluate import OpenRadarCard

        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, pool_member_id, ticker, direction, state, trade_def_slug, trade_def_md5, "
                "trigger_price, structural_stop, entry, stop, formed_at, expires_at, promoted_at, health "
                "FROM aset_sizings WHERE origin = 'radar' AND state = ANY(%s) ORDER BY id",
                (list(self.RADAR_OPEN_STATES),),
            )
            rows = cur.fetchall()
            ids = [r[0] for r in rows]
            dots = self._dots_for(conn, ids)
            taps: dict[int, list] = {card_id: [] for card_id in ids}
            if ids:
                for tap_id, card_id, factor, grade in conn.execute(
                    "SELECT id, card_id, factor, grade FROM card_dot_taps WHERE card_id = ANY(%s) ORDER BY id",
                    (ids,),
                ).fetchall():
                    taps[card_id].append({"id": tap_id, "factor": factor, "grade": grade})
        return [
            OpenRadarCard(
                card_id=r[0], pool_member_id=r[1], ticker=r[2], direction=r[3], state=r[4],
                trade_def_slug=r[5], trade_def_md5=r[6], trigger_price=r[7], structural_stop=r[8],
                entry=r[9], stop=r[10], formed_at=r[11], expires_at=r[12], promoted_at=r[13], health=r[14],
                dots=dots[r[0]], taps=taps[r[0]],
            )
            for r in rows
        ]

    def radar_board_cards(self, trade_date: date) -> list[dict[str, Any]]:
        """The `/radar` ladder's read (STEP-8): every `"user".radar_cards_v`
        row that is open, plus the terminal ones whose last transition
        landed on `trade_date` (ET), each with its dots. Read-only — no
        schema init, no attestation, no write."""
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT * FROM radar_cards_v WHERE state = ANY(%s) "
                "OR (state_at AT TIME ZONE 'America/New_York')::date = %s ORDER BY card_id",
                (list(self.RADAR_OPEN_STATES), trade_date),
            )
            columns = [d.name for d in cur.description]
            rows = [dict(zip(columns, r)) for r in cur.fetchall()]
            dots = self._dots_for(conn, [row["card_id"] for row in rows])
        return [{**row, "dots": dots[row["card_id"]]} for row in rows]

    def shadow_agreement(self, since: Optional[date]) -> list[dict[str, Any]]:
        """`"user".shadow_agreement_v` rows (STEP-10), oldest day first. Read-only."""
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT user_id, factor, trade_date, pairs, median_abs_delta, within2_share, deltas "
                "FROM shadow_agreement_v WHERE %s::date IS NULL OR trade_date >= %s::date "
                "ORDER BY factor, trade_date",
                (since, since),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, r)) for r in cur.fetchall()]

    def formation_consumed(self, ticker: str, slug: str, direction: str, formed_at: datetime) -> bool:
        """Any radar card, in ANY state, already made from this formation
        (R1-16: a passed or expired formation never mints a second WATCH)."""
        with self._connect() as conn:
            row = conn.execute(
                "SELECT 1 FROM aset_sizings WHERE origin = 'radar' AND ticker = %s AND trade_def_slug = %s "
                "AND direction = %s AND formed_at = %s LIMIT 1",
                (ticker, slug, direction, formed_at),
            ).fetchone()
        return row is not None

    def create_radar_card(self, spec, *, now: Optional[datetime] = None, before_commit=None) -> Optional[int]:
        """Create an unsized WATCH radar card. Returns its id, or None when
        the database already holds an OPEN card for (member, def, direction)
        — the partial unique index decides, not a check-then-insert."""
        from cobalt.aset.account_mode import resolve

        def work(conn, ts):
            session = session_clock().session(ts)
            account_mode = resolve(conn, session_clock().to_et(ts).date())
            row = conn.execute(
                """
                INSERT INTO aset_sizings (
                    ticker, grade, direction, sheet_mode, risk_budget, entry, stop, per_share_risk,
                    shares, used_risk, last_price, price_source, warnings, session, state, state_at,
                    origin, account_mode, pool_member_id, trade_def_slug, trade_def_md5, setup_ref,
                    trigger_type, trigger_price, stop_ref, structural_stop, formed_at, expires_at, why,
                    proposed_key, conviction, proximity, card_score, score_suppressed, radar_score_id,
                    scan_id, formula_sha256, tunables_sha256, settings_sha256
                ) VALUES (
                    %s, NULL, %s, NULL, NULL, %s, %s, %s, NULL, NULL, NULL, 'radar', '{}', %s, 'WATCH', %s,
                    'radar', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
                ON CONFLICT (pool_member_id, trade_def_slug, direction)
                    WHERE origin = 'radar' AND state IN ('WATCH', 'ARMED', 'TRIGGERED', 'FILLED')
                DO NOTHING
                RETURNING id
                """,
                (
                    spec.ticker, spec.direction, spec.entry, spec.stop, spec.per_share_risk, session.value, ts,
                    account_mode, spec.pool_member_id, spec.trade_def_slug, spec.trade_def_md5, spec.setup_ref,
                    spec.trigger_type, spec.trigger_price, spec.stop_ref, spec.structural_stop, spec.formed_at,
                    spec.expires_at, spec.why, spec.proposed_key, spec.conviction, spec.proximity,
                    spec.card_score, spec.score_suppressed, spec.radar_score_id, spec.scan_id,
                    spec.formula_sha256, spec.tunables_sha256, spec.settings_sha256,
                ),
            ).fetchone()
            if row is None:
                return None
            card_id = int(row[0])
            self.create_state(
                card_id, CardState.WATCH, actor=Actor.COBALT, evidence=spec.evidence,
                reason="radar formation", now=ts, conn=conn,
            )
            with conn.cursor() as cur:
                for dot in spec.dots:
                    cur.execute(_DOT_INSERT, self._dot_params(card_id, dot))
            return card_id

        return self._write_tx("radar.card", spec.ticker, now, work, before_commit)

    def refresh_radar_card(self, update, *, now: Optional[datetime] = None, before_commit=None) -> bool:
        """This scan's numbers on an open card, under its row lock. Taps
        are never overwritten: a tap that landed after the stage read the
        card leaves conviction/score/key to the tap route's own recompute
        (the next scan reconciles), and only engine fields move."""
        def work(conn, ts):
            locked = conn.execute(
                "SELECT state, (SELECT coalesce(max(id), 0) FROM card_dot_taps WHERE card_id = %s) "
                "FROM aset_sizings WHERE id = %s AND origin = 'radar' FOR UPDATE",
                (update.card_id, update.card_id),
            ).fetchone()
            if locked is None:
                raise CardStateError(f"no radar card with id {update.card_id}")
            taps_moved = int(locked[1]) != update.tap_version
            if taps_moved:
                conn.execute(
                    "UPDATE aset_sizings SET proximity = %s, last_price = COALESCE(%s, last_price), "
                    "health = %s::jsonb, radar_score_id = %s WHERE id = %s",
                    (update.proximity, update.last_price,
                     json.dumps(update.health, default=str) if update.health else None,
                     update.radar_score_id, update.card_id),
                )
            else:
                conn.execute(
                    "UPDATE aset_sizings SET proximity = %s, last_price = COALESCE(%s, last_price), "
                    "conviction = %s, card_score = %s, score_suppressed = %s, proposed_key = %s, "
                    "health = %s::jsonb, radar_score_id = %s WHERE id = %s",
                    (update.proximity, update.last_price, update.conviction, update.card_score,
                     update.score_suppressed, update.proposed_key,
                     json.dumps(update.health, default=str) if update.health else None,
                     update.radar_score_id, update.card_id),
                )
            with conn.cursor() as cur:
                for dot in update.dots:
                    cur.execute(_DOT_UPSERT_ENGINE, self._dot_params(update.card_id, dot))
            return not taps_moved

        return self._write_tx("radar.card", str(update.card_id), now, work, before_commit)

    def expire_radar_card(self, card_id: int, expiry, *, run_id: int, now: Optional[datetime] = None,
                          before_commit=None) -> bool:
        """EXPIRED through the one transition path. A card that moved under
        us to a state EXPIRED is not legal from (FILLED, say) is not
        expired — the refusal is the right answer, logged, not raised."""
        from loguru import logger

        try:
            self.transition(
                card_id, CardState.EXPIRED, actor=Actor.COBALT,
                evidence={**expiry.evidence, "run_id": run_id, "job": "radar S5 evaluate"},
                reason=expiry.reason, now=now, before_commit=before_commit,
            )
        except IllegalTransition as e:
            logger.warning("radar expiry of card {} not applied: {}", card_id, e)
            return False
        return True

    def write_receipt(self, row: dict, *, before_commit=None) -> int:
        def work(conn, ts):
            result = conn.execute(
                "INSERT INTO radar_score_receipt (run_id, pool_key, scan_id, evaluated_at, ordered_cohort, "
                "tie_policy, pool_unit, pool_unit_sha256, tunables_snapshot, settings_snapshot, "
                "definitions_snapshot, tap_versions, observations) VALUES (%s, %s, %s, %s, %s::jsonb, %s, "
                "%s::jsonb, %s, %s::jsonb, %s::jsonb, %s::jsonb, %s::jsonb, %s::jsonb) RETURNING id",
                (
                    row["run_id"], row["pool_key"], row["scan_id"], row["evaluated_at"],
                    json.dumps(row["ordered_cohort"], default=str), row["tie_policy"],
                    json.dumps(row["pool_unit"], default=str), row["pool_unit_sha256"],
                    json.dumps(row["tunables_snapshot"], default=str),
                    json.dumps(row["settings_snapshot"], default=str),
                    json.dumps(row["definitions_snapshot"], default=str),
                    json.dumps(row["tap_versions"], default=str),
                    json.dumps(row["observations"], default=str),
                ),
            ).fetchone()
            return int(result[0])

        return self._write_tx("radar.receipt", row["pool_key"], row["evaluated_at"], work, before_commit)

    def receipts_for_day(self, pool_key: str, trade_date: date) -> list[dict]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT * FROM radar_score_receipt WHERE pool_key = %s "
                "AND observations->>'trade_date' = %s ORDER BY id",
                (pool_key, trade_date.isoformat()),
            )
            columns = [d.name for d in cur.description]
            return [dict(zip(columns, row)) for row in cur.fetchall()]

    def receipt_for_run(self, run_id: int) -> Optional[int]:
        """The receipt id of one run (one receipt per run), or None."""
        with self._connect() as conn:
            rows = conn.execute("SELECT id FROM radar_score_receipt WHERE run_id = %s", (run_id,)).fetchall()
        if len(rows) > 1:
            raise CardStateError(f"radar_score_run {run_id} has {len(rows)} receipts — expected exactly one")
        return int(rows[0][0]) if rows else None

    def receipts_chain(self, receipt_id: int) -> list[dict]:
        """The receipt and every base it references, oldest first."""
        chain: list[dict] = []
        with self._connect() as conn:
            current: Optional[int] = receipt_id
            while current is not None:
                cur = conn.execute("SELECT * FROM radar_score_receipt WHERE id = %s", (current,))
                row = cur.fetchone()
                if row is None:
                    raise CardStateError(f"radar_score_receipt {current} is missing from the chain")
                record = dict(zip([d.name for d in cur.description], row))
                chain.append(record)
                current = record["observations"].get("base_receipt_id")
        return list(reversed(chain))

    # -- taps (STEP-6) ----------------------------------------------------

    def radar_card(self, card_id: int) -> dict[str, Any]:
        with self._connect() as conn:
            cur = conn.execute(
                "SELECT id, ticker, direction, state, origin, entry, stop, proximity, formed_at, created_at, "
                "tapped_grade, sized_grade, promoted_at FROM aset_sizings WHERE id = %s",
                (card_id,),
            )
            row = cur.fetchone()
            if row is None:
                raise CardStateError(f"no aset_sizings row with id {card_id}")
            record = dict(zip([d.name for d in cur.description], row))
        if record["origin"] != "radar":
            raise CardStateError(f"card {card_id} is not a radar card")
        return record

    def tap_key(self, card_id: int, sizing, *, now: Optional[datetime] = None) -> dict[str, Any]:
        """Record the tapped key and size the card at the snapped key — one
        transaction under the row lock. WATCH only (KEY_EDITABLE); the entry
        and stop the size was computed on must still be the card's."""
        from .models import KEY_EDITABLE

        def work(conn, ts):
            locked = conn.execute(
                "SELECT state, origin, entry, stop FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,)
            ).fetchone()
            if locked is None or locked[1] != "radar":
                raise CardStateError(f"no radar card with id {card_id}")
            if CardState(locked[0]) not in KEY_EDITABLE:
                raise CardStateError(
                    f"REFUSED card {card_id}: the key is frozen in {locked[0]} — keys are tapped in WATCH only "
                    "(decision 11: from ARMED onward the key is a risk commitment)"
                )
            inp = sizing.result.input
            if Decimal(locked[2]) != inp.entry or Decimal(locked[3]) != inp.stop:
                raise CardStateError(
                    f"REFUSED card {card_id}: entry/stop moved to {locked[2]}/{locked[3]} while the key was "
                    f"sized on {inp.entry}/{inp.stop} — tap again"
                )
            conn.execute(
                "UPDATE aset_sizings SET tapped_grade = %s, sized_grade = %s, grade = %s, sheet_mode = %s, "
                "risk_budget = %s, per_share_risk = %s, shares = %s, used_risk = %s, snap_notice = %s "
                "WHERE id = %s",
                (sizing.tapped_grade.value, sizing.sized_grade.value, sizing.sized_grade.value,
                 inp.sheet_mode.value, sizing.result.risk_budget, sizing.result.per_share_risk,
                 sizing.result.shares, sizing.result.used_risk, sizing.snap_notice, card_id),
            )
            return {"card_id": card_id, "tapped_grade": sizing.tapped_grade.value,
                    "sized_grade": sizing.sized_grade.value, "shares": sizing.result.shares,
                    "risk_budget": str(sizing.result.risk_budget), "snap_notice": sizing.snap_notice}

        return self._write_tx("radar.card.key", str(card_id), now, work)

    def tap_dot(self, card_id: int, factor: str, grade: int, *, bands, enabled,
                now: Optional[datetime] = None) -> dict[str, Any]:
        """Append the tap, set the dot's trader grade and recompute
        conviction / card_score / proposed key from the locked dots and the
        card's stored proximity — one transaction under the row lock."""
        from .scoring import ASSUMED_FORMATION, card_score, conviction, proposed_key, suppression

        if not 1 <= int(grade) <= 10:
            raise CardStateError(f"a dot grade is 1-10, got {grade}")

        def work(conn, ts):
            locked = conn.execute(
                "SELECT state, origin, proximity FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,)
            ).fetchone()
            if locked is None or locked[1] != "radar":
                raise CardStateError(f"no radar card with id {card_id}")
            if CardState(locked[0]) in TERMINAL:
                raise CardStateError(f"REFUSED card {card_id}: {locked[0]} is terminal — nothing to grade")
            dot = conn.execute(
                "SELECT engine_grade FROM card_dots WHERE card_id = %s AND factor = %s", (card_id, factor)
            ).fetchone()
            if dot is None:
                raise CardStateError(f"card {card_id} has no dot {factor!r}")
            if factor == ASSUMED_FORMATION:
                raise CardStateError(
                    f"REFUSED card {card_id}: assumed_formation is not graded on a card — "
                    "an assumed default is ruled on the settings surface"
                )
            session = session_clock().session(ts)
            conn.execute(
                "INSERT INTO card_dot_taps (card_id, factor, grade, engine_grade_at_tap, at, session) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (card_id, factor, int(grade), dot[0], ts, session.value),
            )
            conn.execute(
                "UPDATE card_dots SET trader_grade = %s, tapped_at = %s WHERE card_id = %s AND factor = %s",
                (int(grade), ts, card_id, factor),
            )
            dots = self._dots_for(conn, [card_id])[card_id]
            conv = conviction(dots)
            prox = Decimal(locked[2]) if locked[2] is not None else None
            suppressed = suppression(dots)
            score = card_score(conv, prox, suppressed)
            key, key_reason = proposed_key(conv, bands, enabled)
            conn.execute(
                "UPDATE aset_sizings SET conviction = %s, card_score = %s, score_suppressed = %s, "
                "proposed_key = %s WHERE id = %s",
                (conv, score, suppressed, key.value if key else None, card_id),
            )
            return {"card_id": card_id, "factor": factor, "grade": int(grade),
                    "conviction": None if conv is None else str(conv), "card_score": score,
                    "score_suppressed": suppressed, "proposed_key": key.value if key else None,
                    "proposed_key_reason": key_reason}

        return self._write_tx("radar.card.dot", str(card_id), now, work)

    def set_promoted(self, card_id: int, promoted: bool, *, now: Optional[datetime] = None) -> dict[str, Any]:
        """Promote pins one WATCH card to #2 (at most one per trader —
        the partial unique index backs it); release restores the order."""
        def work(conn, ts):
            locked = conn.execute(
                "SELECT state, origin FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,)
            ).fetchone()
            if locked is None or locked[1] != "radar":
                raise CardStateError(f"no radar card with id {card_id}")
            if promoted:
                if CardState(locked[0]) is not CardState.WATCH:
                    raise CardStateError(f"REFUSED card {card_id}: only a WATCH card can be promoted ({locked[0]})")
                conn.execute(
                    "UPDATE aset_sizings SET promoted_at = NULL WHERE origin = 'radar' "
                    "AND promoted_at IS NOT NULL AND id <> %s",
                    (card_id,),
                )
                conn.execute("UPDATE aset_sizings SET promoted_at = %s WHERE id = %s", (ts, card_id))
            else:
                conn.execute("UPDATE aset_sizings SET promoted_at = NULL WHERE id = %s", (card_id,))
            return {"card_id": card_id, "promoted": promoted}

        return self._write_tx("radar.card.promote", str(card_id), now, work)


_DOT_COLUMNS = (
    "card_id, factor, position, source, tier, role, engine_value, engine_grade, engine_why, engine_inputs, "
    "engine_formula, na_reason, history, trader_grade, tapped_at"
)
_DOT_INSERT = (
    f"INSERT INTO card_dots ({_DOT_COLUMNS}) VALUES "
    "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s, %s, %s::jsonb, %s, %s)"
)
#: Engine fields and history only — trader_grade/tapped_at belong to taps.
_DOT_UPSERT_ENGINE = (
    _DOT_INSERT + " ON CONFLICT (card_id, factor) DO UPDATE SET position = EXCLUDED.position, "
    "source = EXCLUDED.source, tier = EXCLUDED.tier, role = EXCLUDED.role, engine_value = EXCLUDED.engine_value, "
    "engine_grade = EXCLUDED.engine_grade, engine_why = EXCLUDED.engine_why, "
    "engine_inputs = EXCLUDED.engine_inputs, engine_formula = EXCLUDED.engine_formula, "
    "na_reason = EXCLUDED.na_reason, history = EXCLUDED.history"
)


__all__ = ["BACKFILL_MARKER", "CardStateError", "CardStore", "FillResult", "IllegalTransition"]
