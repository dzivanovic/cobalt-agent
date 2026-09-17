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

from cobalt import db, env
from cobalt.db import Side
from cobalt.aset.store import MIGRATIONS_DIR as ASET_MIGRATIONS
from cobalt.session import assert_writable, session_clock
from cobalt.session import clock as clock_mod

from .models import (
    ALLOWED,
    FILL_TARGET,
    STOP_EDITABLE,
    Actor,
    CardState,
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
                    "SELECT state FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,)
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
    ) -> list[int]:
        """Fill a card. THE entry point for reaching FILLED.

        Returns the `card_transitions` row ids written, in order — so a
        one-click fill from WATCH returns three and a fill of an already
        TRIGGERED card returns one.

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
        if origin is not Origin.MANUAL or len(route) <= 1:
            # Strict path: radar cards, and manual cards already sitting
            # one legal edge away. `transition()` raises by name if the
            # single edge is not legal (a terminal card, say).
            return [
                self.transition(
                    card_id, FILL_TARGET, actor=actor, evidence=evidence,
                    reason=reason, now=ts, allow_prod=allow_prod,
                )
            ]

        if not route:
            raise IllegalTransition(state, FILL_TARGET, card_id)

        # EVERY HOP IN ONE TRANSACTION. A shortcut that crashed between
        # ARMED and TRIGGERED would leave a card armed that nobody armed
        # — a state with a ledger row behind it and no decision behind
        # the row. All of it lands, or none of it does.
        ids: list[int] = []
        conn = self._connect(allow_prod=allow_prod)
        conn.autocommit = False
        try:
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
            conn.commit()
        except BaseException:
            conn.rollback()
            raise
        finally:
            conn.close()
        return ids

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
        from cobalt.aset.engine import recompute_for_stop
        from cobalt.aset.models import Direction

        with self._connect() as conn:
            card = conn.execute(
                "SELECT entry, direction, risk_budget, shares FROM aset_sizings "
                "WHERE id = %s",
                (card_id,),
            ).fetchone()
            if card is None:
                raise CardStateError(f"no aset_sizings row with id {card_id}")
            entry, direction, risk_budget, shares = card

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


__all__ = ["BACKFILL_MARKER", "CardStateError", "CardStore", "IllegalTransition"]
