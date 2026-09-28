"""THE ONE WRITER of `"user".legs` (S3 exits v3 §3; L3, L40).

Every leg row — the entry at the fill, the exits, the corrections, his
held-count statement, the trading-log reconcile — is written here and
nowhere else. S3 C1 builds the entry leg only; C2 adds the exits, the
running-share function and the correction writer to THIS module.

THE CONNECTION RULE. A leg is never a transaction of its own: the entry
leg lands with the FILLED transition, the pick and the fill cache, or
none of them lands (`AsetStore.mark_filled`). So every function here
takes the caller's connection, runs inside the transaction the caller
holds, and never opens, commits, rolls back or closes one. A connection
still in autocommit (`db.connect` opens one that way, `db.py`) is refused
before anything runs: on it each INSERT would commit on its own.

The table is append-only (`refuse_row_update()`); there is no update
function, by design.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Optional

#: seq 0 is the entry leg; exits are 1..n (0021).
ENTRY_SEQ = 0


def _assert_in_transaction(conn) -> None:
    if getattr(conn, "autocommit", False):
        raise RuntimeError(
            "legs: refused on an autocommit connection — a leg is written only inside "
            "the transaction its caller holds (conn.autocommit = False), never on its own"
        )


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
    _assert_in_transaction(conn)
    row = conn.execute(
        """
        INSERT INTO legs (
            card_id, seq, kind, shares, price, at, flag, price_source, price_asof,
            preset, running_before, stop_in_force, source, source_import_id,
            held_stated, corrects, session, account_mode, day_mode_id,
            attested_sheet, sheet_mismatch
        ) VALUES (
            %s, %s, 'entry', %s, %s, %s, %s, %s, %s,
            NULL, 0, %s, %s, NULL,
            NULL, NULL, %s, %s, %s,
            %s, %s
        )
        RETURNING id
        """,
        (
            card_id, ENTRY_SEQ, shares, price, at, flag, price_source, price_asof,
            stop_in_force, source, session, account_mode, day_mode_id,
            attested_sheet, sheet_mismatch,
        ),
    ).fetchone()
    if row is None:
        raise RuntimeError(f"legs: the entry-leg INSERT for card {card_id} returned no id")
    return int(row[0])


__all__ = ["ENTRY_SEQ", "insert_entry_leg"]
