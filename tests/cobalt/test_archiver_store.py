"""Integration test: real upsert/idempotency round trip against cobalt_dev.

Runs only when Postgres env settings are present (conftest loads .env).
Never touches cobalt_brain — the shared connection factory refuses it
(already proven by test_aset_store.py; not re-tested here).
"""

import os
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.archiver.store import BarStore

pytestmark = pytest.mark.integration

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def make_bar(ts, close="100.00"):
    return Bar(
        ticker="TESTARCH",
        interval=Interval.I5,
        ts=ts,
        open=Decimal("99.00"),
        high=Decimal("101.00"),
        low=Decimal("98.50"),
        close=Decimal(close),
        volume=1234,
    )


@requires_db
def test_upsert_is_idempotent_and_refreshes_on_conflict():
    store = BarStore("cobalt_dev")
    store.ensure_schema()
    ts = datetime(2026, 8, 28, 9, 30, tzinfo=timezone.utc)

    n1 = store.upsert_bars([make_bar(ts, close="100.00")])
    assert n1 == 1

    before = store.count_rows()
    # Re-run with the SAME (ticker, interval, ts) but a different close —
    # must refresh in place (PK conflict), never duplicate.
    n2 = store.upsert_bars([make_bar(ts, close="105.00")])
    assert n2 == 1
    after = store.count_rows()
    assert after == before  # no new row — same PK, updated in place

    # Verify the value actually refreshed.
    with store._connect() as conn:
        row = conn.execute(
            "SELECT close FROM bars WHERE ticker=%s AND interval=%s AND ts=%s",
            ("TESTARCH", "i5", ts),
        ).fetchone()
    assert str(row[0]) == "105.0000"


@requires_db
def test_upsert_empty_list_is_a_noop():
    store = BarStore("cobalt_dev")
    store.ensure_schema()
    assert store.upsert_bars([]) == 0
