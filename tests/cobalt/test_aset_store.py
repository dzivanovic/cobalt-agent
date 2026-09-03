"""Integration test: real INSERT/SELECT against cobalt_dev.

Runs only when Postgres env settings are present (conftest loads .env).
Never touches cobalt_brain — the connection factory refuses it.
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

    today_et = datetime.now(timezone.utc).astimezone().date()
    rows = store.for_date(today_et)
    ids = [r["id"] for r in rows]
    assert id1 in ids and id2 in ids
    assert ids.index(id1) < ids.index(id2)  # oldest first
    assert all(r["ticker"] != "" for r in rows)
