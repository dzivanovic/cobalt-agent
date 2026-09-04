"""Integration test: real INSERT/SELECT against cobalt_dev.

Runs only when Postgres env settings are present (conftest loads .env).
Never touches cobalt_brain — the connection factory refuses it.

CLEANUP (added 2026-09-03): these tests write REAL rows into the same
`aset_sizings` the production ASET sheet writes to (configs/dev/aset.yaml
sets `db_name: cobalt_dev` for both). Every run used to leave its
TEST/FORDATE rows behind, and 27 of them accumulated on 2026-09-03 —
15 of which are the rows the incident report found polluting
DRC-2026-09-03.md's "17 cards" when only 2 were real. Each test now
deletes exactly the ids it created.
"""

import os
from decimal import Decimal

import pytest

from cobalt import db
from cobalt.aset.engine import compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
from cobalt.aset.store import AsetStore

pytestmark = pytest.mark.integration

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _delete_rows(store: AsetStore, ids: list[int]) -> None:
    """Remove exactly the rows this test created — never a range, never a
    ticker match. cobalt_dev is the SAME database production ASET writes
    to, so test rows left behind become real pollution in the DRC's
    counts (2026-09-03: 15 stray TEST/FORDATE rows did exactly that)."""
    with store._connect() as conn:
        conn.execute("DELETE FROM aset_sizings WHERE id = ANY(%s)", (ids,))


def test_factory_refuses_prod_db():
    with pytest.raises(db.DbConfigError):
        db.connect("cobalt_brain")


@requires_db
def test_save_and_read_back_roundtrip():
    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="TEST",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
            last_price=Decimal("10.01"),
            price_source="integration-test",
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    row_id = store.save(result)
    try:
        assert row_id > 0

        rows = store.recent(limit=5)
        match = [r for r in rows if r["id"] == row_id]
        assert match, "saved row not found in recent()"
        row = match[0]
        assert row["ticker"] == "TEST"
        assert row["grade"] == "B"
        assert row["sheet_mode"] == "full"
        assert row["shares"] == 120  # 60 / 0.50 = 120
        assert row["used_risk"] == Decimal("60.00")
        assert row["status"] == "CARD"  # migration 0003: lifecycle status
    finally:
        _delete_rows(store, [row_id])


@requires_db
def test_for_date_returns_todays_cards_oldest_first():
    from datetime import datetime, timezone

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="FORDATE",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    id1 = store.save(result)
    id2 = store.save(result)

    try:
        today_et = datetime.now(timezone.utc).astimezone().date()
        rows = store.for_date(today_et)
        ids = [r["id"] for r in rows]
        assert id1 in ids and id2 in ids
        assert ids.index(id1) < ids.index(id2)  # oldest first
        assert all(r["ticker"] != "" for r in rows)

        # migration 0003: cards written vs trades taken are two numbers
        written, taken = store.counts_for_date(today_et)
        assert written >= 2
        assert taken == sum(1 for r in rows if r["status"] == "FILLED")
    finally:
        _delete_rows(store, [id1, id2])


@requires_db
def test_mark_filled_updates_the_card_row():
    """The fill recompute used to persist NOTHING — the 09-03 TSLA FILL
    UPDATE (10:02:36) had no DB row at all. It is an UPDATE to the card
    row now: status FILLED plus the actual-fill figures."""
    from cobalt.aset.engine import compute_fill_recompute

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="TEST",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    row_id = store.save(result)
    try:
        fill = compute_fill_recompute(result, Decimal("10.10"), Decimal("5"))
        store.mark_filled(row_id, fill)
        row = [r for r in store.recent(limit=10) if r["id"] == row_id][0]
        assert row["status"] == "FILLED"

        with store._connect() as conn:
            actual, shares = conn.execute(
                "SELECT actual_fill, recomputed_shares FROM aset_sizings WHERE id = %s",
                (row_id,),
            ).fetchone()
        assert actual == Decimal("10.1000")
        assert shares == fill.recomputed_shares

        with pytest.raises(RuntimeError, match="expected exactly 1"):
            store.mark_filled(-1, fill)
    finally:
        _delete_rows(store, [row_id])
