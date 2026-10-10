"""S4-P2 S3 + S4 on cobalt_dev (`requires_db`, hub-run): the ack, its record
(`"user".strike_alerts`, DECISION E4) and one phone-fallback pass.

`0024_strike_alerts` is applied inside the suite's rolled-back transaction
only (L76); the gate runs this file in PASS 2 (`ops/desk/gate-lists.md`).
The ack goes through the real route (`TestClient(web.app)`), whose clock is
the suite's frozen `now_utc` — the SERVER's clock, never the page's.
Ticker, prices and dates are constructed (L32).
"""

from __future__ import annotations

import os
from datetime import timedelta

import pytest
from fastapi.testclient import TestClient

from test_radar_cards_db import TICKER, world  # noqa: F401 — the fixture
from test_strike_stream_db import apply_0024, triggered_card

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]


def _store():
    from cobalt.aset.strike import StrikeAlertStore

    store = StrikeAlertStore("cobalt_dev")
    apply_0024(store)
    return store


def _record(store, tid):
    with store._connect() as conn:
        cur = conn.execute("SELECT * FROM strike_alerts WHERE transition_id = %s", (tid,))
        rows = cur.fetchall()
        names = [d.name for d in cur.description]
    return [dict(zip(names, r)) for r in rows]


def _ack(tid):
    from cobalt.aset import web

    return TestClient(web.app).post("/strike/ack", json={"transition_id": tid})


def test_push_then_ack_is_one_row_with_pushed_at_before_shown_at(world):  # noqa: F811
    from cobalt.session import clock

    store = _store()
    _card, tid, at = triggered_card(world)
    seam = store.transition(tid)
    pushed = clock.now_utc() - timedelta(seconds=2)
    store.upsert(tid, seam_at=seam.at, pushed_at=pushed)
    response = _ack(tid)
    assert response.status_code == 200, response.text
    [row] = _record(store, tid)
    assert row["seam_at"] == at and row["pushed_at"] == pushed
    assert row["shown_at"] == clock.now_utc() and row["pushed_at"] <= row["shown_at"]

    again = _ack(tid)
    assert again.status_code == 200
    assert _record(store, tid) == [row], "a second ack changes nothing"


def test_an_ack_for_an_id_that_is_not_a_seam_row_is_404_and_writes_nothing(world):  # noqa: F811
    store = _store()
    card_id, tid, _at = triggered_card(world)
    with store._connect() as conn:
        armed = conn.execute("SELECT id FROM card_transitions WHERE card_id = %s AND to_state = 'ARMED'",
                             (card_id,)).fetchone()[0]
    for unknown in (armed, tid + 1_000_000):
        response = _ack(unknown)
        assert response.status_code == 404, response.text
        assert _record(store, unknown) == []


def test_an_ack_with_no_prior_push_creates_the_row(world):  # noqa: F811
    store = _store()
    _card, tid, at = triggered_card(world)
    assert _ack(tid).status_code == 200
    [row] = _record(store, tid)
    assert row["pushed_at"] is None and row["shown_at"] is not None and row["seam_at"] == at


def test_one_fallback_pass_with_no_stream_records_the_dm(world):  # noqa: F811
    from cobalt.aset.strike import FallbackTail
    from cobalt.notify.result import SendResult
    from cobalt.strike.delivery_config import DeliverySettings

    store = _store()
    _card, tid, at = triggered_card(world)
    sent = []

    def fake_send(text):
        sent.append(text)
        return SendResult(True, "post constructed-id to @constructed", ref="constructed-id")

    later = at + timedelta(seconds=DeliverySettings().dm_after_s)
    tail = FallbackTail(store=store, send=fake_send, settings=DeliverySettings(), now=lambda: later)
    tail.pass_once()
    tail.pass_once()
    assert len([text for text in sent if text.startswith(f"{TICKER} ")]) == 1
    [row] = _record(store, tid)
    assert row["pushed_at"] is None and row["shown_at"] is None
    assert row["dm_at"] == later and row["dm_result"].startswith("DM sent")


def test_the_table_is_user_side_with_the_tenant_default():
    from cobalt.db import Side
    from cobalt.db_migrations.placement import CREATED_TABLES

    store = _store()
    assert CREATED_TABLES["strike_alerts"] is Side.USER
    with store._connect() as conn:
        nullable, default = conn.execute(
            "SELECT is_nullable, column_default FROM information_schema.columns "
            "WHERE table_schema = 'user' AND table_name = 'strike_alerts' AND column_name = 'user_id'").fetchone()
    assert nullable == "NO" and "current_setting" in default and "cobalt.trader_id" in default


def test_the_migration_goes_up_back_and_up_again():
    from cobalt.db_migrations import MIGRATIONS_DIR

    store = _store()

    def exists():
        with store._connect() as conn:
            return conn.execute("""SELECT to_regclass('"user".strike_alerts')""").fetchone()[0] is not None

    assert exists()
    with store._connect() as conn:
        conn.execute((MIGRATIONS_DIR / "0024_strike_alerts.rollback.sql").read_text())
    assert not exists()
    apply_0024(store)
    apply_0024(store)
    assert exists()
