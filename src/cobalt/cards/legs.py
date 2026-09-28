"""THE ONE WRITER of `"user".legs` (S3 exits v3 §3; L3, L40).

Every leg row — the entry at the fill, the exits, the corrections, his
held-count statement, the trading-log reconcile — is written here and
nowhere else. S3 C1 built the entry leg; C2 (R67 = the Fable seat's N)
adds the exits, THE running-share read, the correction writer and the
held-count writer, and the one realized-R function.

THE CONNECTION RULE, two shapes:

* `insert_entry_leg` and `running_shares` run on the CALLER's open
  transaction and never open, commit, roll back or close one — the entry
  leg lands with the FILLED transition, the pick and the fill cache, or
  none of them lands (`AsetStore.mark_filled`).
* `record_exit`, `record_correction` and `record_held` are top-level
  writes: each opens ONE connection, switches off autocommit (`db.connect`
  opens autocommit), takes the card row lock (`SELECT … FROM aset_sizings
  WHERE id = %s FOR UPDATE`, the lock `transition()` takes), and writes its
  leg and — when running reaches 0 — the FILLED -> CLOSED transition in
  that one transaction: one commit, any exception rolls all of it back.

A connection still in autocommit is refused before anything runs: on it
each INSERT would commit on its own.

RUNNING IS DERIVED, NEVER STORED: entry-leg shares − Σ current exit-leg
shares, read by `running_shares` and by nothing else (L3). Every exit tap
posts the `running_before` its screen computed from; a stale or duplicate
tap is refused, never re-applied to the smaller count (R67).

S-C2 (the DRC lane's D5 calls these writers, no other): `record_exit` and
`record_correction` take `source = 'trading_log'` with a REQUIRED
`source_import_id`. Such a row is appended like any other — it never
deletes or updates his rows. The CLOSED check runs only when running
reaches 0. A refusal is raised by name (`LegRefused`, its `code` stable)
for the caller to show verbatim; nothing is ever forced.

The table is append-only (`refuse_row_update()`); there is no update
function, by design.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any, Mapping, NamedTuple, Optional, Sequence

from .store import CardStateError

#: seq 0 is the entry leg; exits are 1..n (0021).
ENTRY_SEQ = 0

#: The exit presets (O14 A) and their share rule (O1 A: round DOWN).
PRESETS = ("half", "third", "flat", "typed")
_PRESET_SIGN = {"half": "½", "third": "⅓"}

#: `running_shares`' `basis`: where the held count's base came from.
BASIS_LEGS = "legs"                            # the current entry leg
BASIS_RECOMPUTED = "recomputed_shares"         # filled before C1, fill recompute cached
BASIS_SHARES = "shares"                        # filled before C1, the planned count

#: The trading-log source, whose rows name the import they came from.
TRADING_LOG = "trading_log"

#: `realized_r`'s id (v3 §3 [F-01]).
REALIZED_R_ID = "realized_r.1"


class LegRefused(CardStateError):
    """A leg write refused by name. The message is shown verbatim (C3,
    the DRC lane's D5); `code` is the stable key a caller may branch on.
    Nothing was written."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


class Running(NamedTuple):
    """THE held count of one card, derived under the card lock."""

    shares: int                    # base − Σ current exit shares
    basis: str                     # BASIS_LEGS / BASIS_RECOMPUTED / BASIS_SHARES
    base_shares: int               # the current entry leg's shares, or the pre-C1 count
    exit_shares: int               # Σ current exit-leg shares
    entry_leg_id: Optional[int]    # the current entry row (None: filled before C1)
    entry_price: Optional[Decimal]  # its price (None: filled before C1)
    state: str                     # the card's state, read under the lock


class ExitResult(NamedTuple):
    leg_id: int
    shares: int
    running_before: int
    running_after: int
    closed: bool
    transition_id: Optional[int]   # the FILLED -> CLOSED row when `closed`


class CorrectionResult(NamedTuple):
    leg_id: int                    # the new (now current) row
    corrects: int                  # the row it corrects
    running_after: int
    closed: bool
    transition_id: Optional[int]


class RealizedR(NamedTuple):
    function_id: str
    value: Optional[Decimal]       # None = not computed (`reason` says why)
    provisional: bool              # any current leg `estimated`
    r_unit: Optional[Decimal]
    reason: Optional[str]


class Position(NamedTuple):
    """What `cobalt cards legs <id>` shows — a read, nothing written."""

    card: dict[str, Any]
    legs: list[dict[str, Any]]     # `legs_current_v`, by seq
    running: Running
    realized: RealizedR


# ---------------------------------------------------------------------
# plumbing
# ---------------------------------------------------------------------


def _assert_in_transaction(conn) -> None:
    if getattr(conn, "autocommit", False):
        raise RuntimeError(
            "legs: refused on an autocommit connection — a leg is written only inside "
            "the transaction its caller holds (conn.autocommit = False), never on its own"
        )


def _connect():
    from cobalt import db, env

    conn = db.connect(env.resolve_db_name(), side=db.Side.USER)
    conn.autocommit = False
    return conn


def _row(conn, sql: str, params) -> Optional[dict[str, Any]]:
    cur = conn.execute(sql, params)
    found = cur.fetchone()
    if found is None:
        return None
    return dict(zip([d.name for d in cur.description], found))


def _lock_card(conn, card_id: int) -> dict[str, Any]:
    card = _row(conn, "SELECT * FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,))
    if card is None:
        raise CardStateError(f"no aset_sizings row with id {card_id}")
    return card


def _check_source(source: str, source_import_id: Optional[int]) -> None:
    if source == TRADING_LOG and source_import_id is None:
        raise LegRefused(
            "import_id",
            "REFUSED: a trading-log row names the import it came from — source_import_id is "
            "required with source = 'trading_log'. Nothing written.",
        )
    if source != TRADING_LOG and source_import_id is not None:
        raise LegRefused(
            "import_id",
            f"REFUSED: source_import_id is carried only by a trading-log row, not by source "
            f"{source!r}. Nothing written.",
        )


def _insert_leg(
    conn,
    card_id: int,
    *,
    seq: int,
    kind: str,
    shares: int,
    price: Decimal,
    at: datetime,
    flag: str,
    price_source: str,
    price_asof: Optional[datetime],
    preset: Optional[str],
    running_before: int,
    stop_in_force: Decimal,
    source: str,
    source_import_id: Optional[int],
    held_stated: Optional[int],
    corrects: Optional[int],
    session: str,
    account_mode: str,
    day_mode_id: Optional[date],
    attested_sheet: Optional[str],
    sheet_mismatch: Optional[bool],
) -> int:
    _assert_in_transaction(conn)
    row = conn.execute(
        """
        INSERT INTO legs (
            card_id, seq, kind, shares, price, at, flag, price_source, price_asof,
            preset, running_before, stop_in_force, source, source_import_id,
            held_stated, corrects, session, account_mode, day_mode_id,
            attested_sheet, sheet_mismatch
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s
        )
        RETURNING id
        """,
        (
            card_id, seq, kind, shares, price, at, flag, price_source, price_asof,
            preset, running_before, stop_in_force, source, source_import_id,
            held_stated, corrects, session, account_mode, day_mode_id,
            attested_sheet, sheet_mismatch,
        ),
    ).fetchone()
    if row is None:
        raise RuntimeError(f"legs: the {kind}-leg INSERT for card {card_id} returned no id")
    return int(row[0])


def _close_if_zero(conn, card_id: int, running_after: int, leg_id: int, ts: datetime) -> Optional[int]:
    """FILLED -> CLOSED through `transition()` on THIS transaction when the
    leg brought running to 0 (v3 §2; L18). Evidence names the leg."""
    if running_after != 0:
        return None
    from .models import Actor, CardState
    from .store import CardStore

    return CardStore().transition(
        card_id, CardState.CLOSED, actor=Actor.YOU, evidence={"leg_id": leg_id}, now=ts, conn=conn,
    )


# ---------------------------------------------------------------------
# C1 — the entry leg (THE fill's)
# ---------------------------------------------------------------------


def insert_entry_leg(
    conn,
    card_id: int,
    *,
    shares: int,
    price: Decimal,
    at: datetime,
    flag: str,
    price_source: str,
    price_asof: Optional[datetime],
    source: str,
    stop_in_force: Decimal,
    session: str,
    account_mode: str,
    day_mode_id: Optional[date],
    attested_sheet: Optional[str],
    sheet_mismatch: bool,
) -> int:
    """Insert the ORIGINAL entry leg (seq 0) of `card_id`. Returns its id.

    `running_before` is 0 on an entry row (nothing was held before it);
    `preset`, `corrects`, `held_stated` and `source_import_id` are NULL.
    A second original entry for the card is refused by the partial unique
    index, never checked here first.
    """
    return _insert_leg(
        conn, card_id, seq=ENTRY_SEQ, kind="entry", shares=shares, price=price, at=at, flag=flag,
        price_source=price_source, price_asof=price_asof, preset=None, running_before=0,
        stop_in_force=stop_in_force, source=source, source_import_id=None, held_stated=None,
        corrects=None, session=session, account_mode=account_mode, day_mode_id=day_mode_id,
        attested_sheet=attested_sheet, sheet_mismatch=sheet_mismatch,
    )


# ---------------------------------------------------------------------
# C2-1 — THE running read
# ---------------------------------------------------------------------


def running_shares(conn, card_id: int) -> Running:
    """THE ONLY running read (L3): the current entry leg's shares − Σ the
    current exit legs' shares, from `legs_current_v`.

    Runs on the caller's transaction and takes the card row lock itself
    (`FOR UPDATE` — re-entrant for a caller that already holds it), so the
    count it returns cannot move before that transaction ends.

    A FILLED card with NO entry leg was filled before C1 (O21 A): its base
    is `recomputed_shares`, else `shares`, and `basis` names which. A card
    with no entry leg in any other state holds no position — refused.
    """
    from .models import CardState

    _assert_in_transaction(conn)
    card = _row(
        conn,
        "SELECT state, shares, recomputed_shares FROM aset_sizings WHERE id = %s FOR UPDATE",
        (card_id,),
    )
    if card is None:
        raise CardStateError(f"no aset_sizings row with id {card_id}")
    entry = _row(
        conn,
        "SELECT id, shares, price FROM legs_current_v WHERE card_id = %s AND kind = 'entry'",
        (card_id,),
    )
    exits = int(conn.execute(
        "SELECT COALESCE(sum(shares), 0) FROM legs_current_v WHERE card_id = %s AND kind = 'exit'",
        (card_id,),
    ).fetchone()[0])

    if entry is not None:
        base, basis = int(entry["shares"]), BASIS_LEGS
    elif card["state"] == CardState.FILLED.value and card["recomputed_shares"] is not None:
        base, basis = int(card["recomputed_shares"]), BASIS_RECOMPUTED
    elif card["state"] == CardState.FILLED.value and card["shares"] is not None:
        base, basis = int(card["shares"]), BASIS_SHARES
    else:
        raise LegRefused(
            "no_position",
            f"card {card_id} is {card['state']} with no entry leg — it holds no position.",
        )
    return Running(
        shares=base - exits,
        basis=basis,
        base_shares=base,
        exit_shares=exits,
        entry_leg_id=None if entry is None else int(entry["id"]),
        entry_price=None if entry is None else Decimal(entry["price"]),
        state=card["state"],
    )


# ---------------------------------------------------------------------
# C2-2 — the exit leg
# ---------------------------------------------------------------------


def _preset_shares(card_id: int, preset: str, typed: Optional[int], running: int) -> int:
    if preset == "typed":
        if typed is None or int(typed) <= 0:
            raise LegRefused(
                "typed_shares",
                f"REFUSED card {card_id}: a typed exit names its share count (> 0), got {typed!r}. "
                "Nothing written.",
            )
        shares = int(typed)
    else:
        if typed is not None:
            raise LegRefused(
                "typed_shares",
                f"REFUSED card {card_id}: the {preset} preset computes its own shares — "
                f"{typed!r} typed with it. Use typed. Nothing written.",
            )
        shares = {"half": running // 2, "third": running // 3, "flat": running}[preset]
        if shares == 0:
            sign = _PRESET_SIGN.get(preset, preset)
            raise LegRefused(
                "zero_preset", f"REFUSED card {card_id}: {sign} of {running} is 0 — use flat or type",
            )
    if shares > running:
        raise LegRefused(
            "over_running",
            f"REFUSED card {card_id}: an exit of {shares} shares is more than the {running} still "
            "held. Nothing written.",
        )
    return shares


def record_exit(
    card_id: int,
    *,
    preset: str,
    shares: Optional[int] = None,
    price: Decimal,
    price_source: str,
    price_asof: Optional[datetime],
    flag: str,
    source: str,
    running_before: int,
    now: datetime,
    source_import_id: Optional[int] = None,
) -> ExitResult:
    """One exit leg (v3 §2 FILLED (leg); R67). ½ = ⌊running/2⌋, ⅓ =
    ⌊running/3⌋, flat = running, typed = `shares` ≤ running (O1 A, O14 A).

    Refused, nothing written: in `market_reset` (the session gate, FIRST);
    a card not FILLED; a posted `running_before` ≠ the running computed
    under the lock (`REFUSED: screen said <posted>, now <computed> — tap
    again`); a preset of 0 shares; shares > running; a trading-log row with
    no import id. The leg that brings running to 0 writes FILLED -> CLOSED
    in the same transaction.
    """
    from cobalt.session import assert_writable

    from .models import CardState

    session = assert_writable("cards.leg.exit", target=str(card_id), now=now)
    _check_source(source, source_import_id)
    if preset not in PRESETS:
        raise LegRefused("preset", f"REFUSED card {card_id}: preset {preset!r} is not one of {PRESETS}.")

    conn = _connect()
    try:
        card = _lock_card(conn, card_id)
        if card["state"] != CardState.FILLED.value:
            raise LegRefused(
                "not_filled",
                f"REFUSED card {card_id}: an exit leg needs a FILLED card — it is {card['state']}. "
                "Nothing written.",
            )
        run = running_shares(conn, card_id)
        if int(running_before) != run.shares:
            raise LegRefused("stale", f"REFUSED: screen said {running_before}, now {run.shares} — tap again")
        n = _preset_shares(card_id, preset, shares, run.shares)
        seq = int(conn.execute(
            "SELECT COALESCE(max(seq), 0) + 1 FROM legs_current_v WHERE card_id = %s", (card_id,)
        ).fetchone()[0])
        leg_id = _insert_leg(
            conn, card_id, seq=seq, kind="exit", shares=n, price=price, at=now, flag=flag,
            price_source=price_source, price_asof=price_asof, preset=preset,
            running_before=run.shares, stop_in_force=card["stop"], source=source,
            source_import_id=source_import_id, held_stated=None, corrects=None,
            session=session.value, account_mode=card["account_mode"], day_mode_id=None,
            attested_sheet=None, sheet_mismatch=None,
        )
        after = run.shares - n
        transition_id = _close_if_zero(conn, card_id, after, leg_id, now)
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()
    return ExitResult(leg_id, n, run.shares, after, transition_id is not None, transition_id)


# ---------------------------------------------------------------------
# C2-3 — corrections
# ---------------------------------------------------------------------


def _rewrite_fill_cache(conn, card: Mapping[str, Any], entry: Mapping[str, Any], price: Decimal) -> None:
    """An ENTRY-price correction rewrites the `aset_sizings` fill cache
    (`actual_fill` and the `compute_fill_recompute` figures) on the
    correction's transaction (v3 §3 N). The plan it recomputes against is
    the plan AT THE FILL: the card row rebuilt by `SizingResult.from_card`
    (the one rebuild) with the stop in force at the fill — the entry leg's
    `stop_in_force` — since a FILLED stop edit has moved the card's stop
    since. The P is the one stored at the fill (`drift_warning_pct`; NULL
    stays not evaluated). `filled_at` and `drift_warning_pct` are not
    touched; the fill transition's evidence keeps the fill-time figures."""
    from cobalt.aset import config as aset_config
    from cobalt.aset.engine import compute_fill_recompute
    from cobalt.aset.models import SizingResult

    stop_at_fill = Decimal(entry["stop_in_force"])
    plan = {**card, "stop": stop_at_fill, "per_share_risk": abs(Decimal(card["entry"]) - stop_at_fill)}
    guard = aset_config.load_config().validation.max_fill_distance_pct
    fill = compute_fill_recompute(
        SizingResult.from_card(plan), price, guard, drift_warning_pct=card["drift_warning_pct"],
    )
    cur = conn.execute(
        """
        UPDATE aset_sizings SET
            actual_fill = %s,
            recomputed_shares = %s,
            recomputed_used_risk = %s,
            share_delta = %s,
            distance_change_pct = %s,
            drift_warned = %s
        WHERE id = %s
        """,
        (fill.actual_fill, fill.recomputed_shares, fill.recomputed_used_risk, fill.share_delta,
         fill.distance_change_pct, fill.drift_warned, card["id"]),
    )
    if cur.rowcount != 1:
        raise RuntimeError(f"legs: the fill-cache rewrite matched {cur.rowcount} rows for card {card['id']}")


def record_correction(
    leg_id: int,
    *,
    price: Optional[Decimal] = None,
    at: Optional[datetime] = None,
    flag: Optional[str] = None,
    price_source: Optional[str] = None,
    shares: Optional[int] = None,
    source: str,
    now: datetime,
    source_import_id: Optional[int] = None,
) -> CorrectionResult:
    """A correction is a NEW row naming the CURRENT row of its seq (R67);
    the old row is never touched. `seq`, `kind`, `preset`,
    `running_before`, `stop_in_force` and the stamps are copied; what is
    given replaces. A changed price names its source (L57) and is
    `confirmed` unless `flag` says otherwise.

    Refused, nothing written: `market_reset`; `leg_id` not the current row
    (naming the current id); Σ current exits past the entry shares; a
    change that moves a CLOSED card's running off 0; a trading-log row
    with no import id. A correction that brings a FILLED card's running to
    0 writes FILLED -> CLOSED in the same transaction (O22 A). An ENTRY
    price correction rewrites the fill cache in the same transaction.
    """
    from cobalt.session import assert_writable

    from .models import CardState

    assert_writable("cards.leg.correction", target=str(leg_id), now=now)
    _check_source(source, source_import_id)
    if price is None and at is None and flag is None and price_source is None and shares is None:
        raise LegRefused("no_change", f"REFUSED: the correction of leg {leg_id} changes nothing. Nothing written.")
    if price is not None and price_source is None:
        raise LegRefused(
            "price_source",
            f"REFUSED: the corrected price of leg {leg_id} names its source (price_source) — "
            "every price stores where it came from (L57). Nothing written.",
        )
    if shares is not None and int(shares) <= 0:
        raise LegRefused("shares", f"REFUSED: a leg holds shares > 0, got {shares!r}. Nothing written.")

    conn = _connect()
    try:
        found = conn.execute("SELECT card_id FROM legs WHERE id = %s", (leg_id,)).fetchone()
        if found is None:
            raise LegRefused("no_leg", f"REFUSED: no leg with id {leg_id}. Nothing written.")
        card_id = int(found[0])
        card = _lock_card(conn, card_id)
        if card["state"] not in (CardState.FILLED.value, CardState.CLOSED.value):
            raise LegRefused(
                "not_filled",
                f"REFUSED card {card_id}: a correction needs a FILLED or CLOSED card — it is "
                f"{card['state']}. Nothing written.",
            )
        old = _row(conn, "SELECT * FROM legs WHERE id = %s", (leg_id,))
        current_id = int(conn.execute(
            "SELECT id FROM legs_current_v WHERE card_id = %s AND seq = %s", (card_id, old["seq"])
        ).fetchone()[0])
        if current_id != leg_id:
            raise LegRefused(
                "not_current",
                f"REFUSED: leg {leg_id} is not the current row of seq {old['seq']} on card {card_id} — "
                f"the current row is {current_id}. Correct that one. Nothing written.",
            )

        run = running_shares(conn, card_id)
        new_shares = int(old["shares"]) if shares is None else int(shares)
        if old["kind"] == "entry":
            entry_after, exits_after = new_shares, run.exit_shares
        else:
            entry_after = run.base_shares
            exits_after = run.exit_shares - int(old["shares"]) + new_shares
        if exits_after > entry_after:
            raise LegRefused(
                "over_entry",
                f"REFUSED card {card_id}: the exits would total {exits_after} shares against an entry "
                f"of {entry_after}. Nothing written.",
            )
        after = entry_after - exits_after
        if card["state"] == CardState.CLOSED.value and after != 0:
            raise LegRefused(
                "closed_off_zero",
                f"REFUSED card {card_id}: CLOSED has no way back — this correction would leave {after} "
                "shares running. Nothing written.",
            )

        new_source = price_source or old["price_source"]
        keep_asof = price is None and new_source == old["price_source"]
        new_id = _insert_leg(
            conn, card_id, seq=old["seq"], kind=old["kind"], shares=new_shares,
            price=old["price"] if price is None else price,
            at=old["at"] if at is None else at,
            flag=flag or ("confirmed" if price is not None else old["flag"]),
            price_source=new_source,
            price_asof=old["price_asof"] if keep_asof else None,
            preset=old["preset"], running_before=old["running_before"],
            stop_in_force=old["stop_in_force"], source=source, source_import_id=source_import_id,
            held_stated=None, corrects=leg_id, session=old["session"],
            account_mode=old["account_mode"], day_mode_id=old["day_mode_id"],
            attested_sheet=old["attested_sheet"], sheet_mismatch=None,
        )
        if old["kind"] == "entry" and price is not None and Decimal(price) != Decimal(old["price"]):
            _rewrite_fill_cache(conn, card, old, Decimal(price))
        transition_id = None
        if card["state"] == CardState.FILLED.value:
            transition_id = _close_if_zero(conn, card_id, after, new_id, now)
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()
    return CorrectionResult(new_id, leg_id, after, transition_id is not None, transition_id)


# ---------------------------------------------------------------------
# C2-4 — the held count (S-HELD)
# ---------------------------------------------------------------------


def record_held(card_id: int, held: int, *, source: str, now: datetime) -> CorrectionResult:
    """His "I'm holding X" mid-trade (R67 (1), S-HELD): a correction row
    of the current entry leg with `held_stated = X`, `shares = X + Σ
    current exit shares` (under the card lock), `price` / `price_source` /
    `price_asof` copied, `flag = 'confirmed'`. It wins over the recomputed
    count. `held = 0` closes the card in the same transaction.

    Refused, nothing written: `market_reset`; a CLOSED card (`CLOSED has no
    way back — correct the exit instead`); any other non-FILLED card; a
    card filled before C1 (no entry leg to correct); "holding 0" with no
    exit recorded (a leg holds > 0 shares — record the exit instead).
    """
    from cobalt.session import assert_writable

    from .models import CardState

    assert_writable("cards.leg.held", target=str(card_id), now=now)
    if source == TRADING_LOG:
        raise LegRefused(
            "import_id",
            "REFUSED: a held count is his statement — the trading log reconciles through "
            "record_correction with its source_import_id. Nothing written.",
        )
    if int(held) < 0:
        raise LegRefused("held", f"REFUSED card {card_id}: a held count is >= 0, got {held!r}. Nothing written.")

    conn = _connect()
    try:
        card = _lock_card(conn, card_id)
        if card["state"] == CardState.CLOSED.value:
            raise LegRefused("closed_held", "CLOSED has no way back — correct the exit instead")
        if card["state"] != CardState.FILLED.value:
            raise LegRefused(
                "not_filled",
                f"REFUSED card {card_id}: a held count needs a FILLED card — it is {card['state']}. "
                "Nothing written.",
            )
        run = running_shares(conn, card_id)
        if run.entry_leg_id is None:
            raise LegRefused(
                "no_entry_leg",
                f"REFUSED card {card_id}: filled before C1, it has no entry leg for the held count to "
                f"correct (running is read from {run.basis}). Nothing written.",
            )
        entry_shares = int(held) + run.exit_shares
        if entry_shares == 0:
            raise LegRefused(
                "held_zero_no_exit",
                f"REFUSED card {card_id}: holding 0 with no exit recorded — record the exit (flat) "
                "instead. Nothing written.",
            )
        old = _row(conn, "SELECT * FROM legs WHERE id = %s", (run.entry_leg_id,))
        new_id = _insert_leg(
            conn, card_id, seq=ENTRY_SEQ, kind="entry", shares=entry_shares, price=old["price"],
            at=old["at"], flag="confirmed", price_source=old["price_source"],
            price_asof=old["price_asof"], preset=None, running_before=old["running_before"],
            stop_in_force=old["stop_in_force"], source=source, source_import_id=None,
            held_stated=int(held), corrects=int(old["id"]), session=old["session"],
            account_mode=old["account_mode"], day_mode_id=old["day_mode_id"],
            attested_sheet=old["attested_sheet"], sheet_mismatch=None,
        )
        transition_id = _close_if_zero(conn, card_id, int(held), new_id, now)
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()
    return CorrectionResult(new_id, int(old["id"]), int(held), transition_id is not None, transition_id)


# ---------------------------------------------------------------------
# C2-5 — realized R (pure, never stored)
# ---------------------------------------------------------------------


def realized_r(card_row: Mapping[str, Any], current_legs: Sequence[Mapping[str, Any]]) -> RealizedR:
    """`realized_r.1` (v3 §3 [F-01]; O15 A — the ACTUAL unit only).

    R_unit = |entry.price − entry.stop_in_force| (his fill, his stop at
    the fill); `sign` from the card's `direction`; Σ over the current exits
    of `sign × (exit.price − entry.price) × exit.shares ÷ (entry.shares ×
    R_unit)`. `provisional` while any current leg is `estimated`. A zero
    unit is `not computed — zero risk unit`, never a division. Pure: the
    caller passes the CURRENT legs (`legs_current_v`); nothing is stored.
    """
    from cobalt.aset.models import Direction

    provisional = any(leg["flag"] == "estimated" for leg in current_legs)
    entries = [leg for leg in current_legs if leg["kind"] == "entry"]
    if not entries:
        return RealizedR(REALIZED_R_ID, None, provisional, None, "not computed — no entry leg")
    entry = entries[0]
    entry_price = Decimal(entry["price"])
    r_unit = abs(entry_price - Decimal(entry["stop_in_force"]))
    if r_unit == 0:
        return RealizedR(REALIZED_R_ID, None, provisional, r_unit, "not computed — zero risk unit")
    sign = Decimal(1) if Direction(card_row["direction"]) is Direction.LONG else Decimal(-1)
    denominator = Decimal(int(entry["shares"])) * r_unit
    value = sum(
        (sign * (Decimal(leg["price"]) - entry_price) * int(leg["shares"]) / denominator
         for leg in current_legs if leg["kind"] == "exit"),
        Decimal(0),
    )
    return RealizedR(REALIZED_R_ID, value, provisional, r_unit, None)


# ---------------------------------------------------------------------
# C2-7's read
# ---------------------------------------------------------------------


def read_position(card_id: int) -> Position:
    """The card's current legs, THE running read, realized R — on one
    transaction that writes nothing and is rolled back (the running read
    takes the card lock, so it cannot run READ ONLY)."""
    conn = _connect()
    try:
        run = running_shares(conn, card_id)
        card = _row(
            conn,
            "SELECT id, ticker, direction, state, stop, structural_stop FROM aset_sizings WHERE id = %s",
            (card_id,),
        )
        cur = conn.execute("SELECT * FROM legs_current_v WHERE card_id = %s ORDER BY seq", (card_id,))
        legs = [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]
        return Position(card, legs, run, realized_r(card, legs))
    finally:
        conn.rollback()
        conn.close()


__all__ = [
    "BASIS_LEGS",
    "BASIS_RECOMPUTED",
    "BASIS_SHARES",
    "ENTRY_SEQ",
    "PRESETS",
    "REALIZED_R_ID",
    "CorrectionResult",
    "ExitResult",
    "LegRefused",
    "Position",
    "RealizedR",
    "Running",
    "insert_entry_leg",
    "read_position",
    "realized_r",
    "record_correction",
    "record_exit",
    "record_held",
    "running_shares",
]
