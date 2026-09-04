"""Integration test: real upsert/idempotency round trip against cobalt_dev.

Runs only when Postgres env settings are present (conftest loads .env).

RULING 9 (2026-09-04): `BarStore()` takes no database argument any
more — `conftest.dev_env` pins `COBALT_ENV=dev`, so the resolver hands
it `cobalt_dev`, and `conftest.dev_db_tx` runs the whole test inside a
transaction that is rolled back. Nothing this file writes survives the
run, which is what lets `bars` live in `cobalt_brain` (RULING 9) while
the suite still exercises the real upsert. `cobalt_brain` is
unreachable twice over: the fixture raises on any database but
`cobalt_dev`, and the connection factory refuses production to a
process that has not declared it.
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
    store = BarStore()
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
    store = BarStore()
    store.ensure_schema()
    assert store.upsert_bars([]) == 0
