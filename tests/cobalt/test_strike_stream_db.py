"""S4-P2 S1 on cobalt_dev (`requires_db`, hub-run): P1's own detector moves
an ARMED radar card, and the stream sends that one transition.

The world is built as `test_strike_detector_db` builds it (the S5 stage's
`create_radar_card`, sized and armed through `CardStore`, one REAL
`StrikeDetector.tick()` with a fake fetch); `0024_strike_alerts` is applied
inside the suite's rolled-back transaction only (L76), so the file needs a
level above 0013 and the gate runs it in PASS 2 (`ops/desk/gate-lists.md`).
Ticker, prices and dates are constructed (L32).
"""

from __future__ import annotations

import asyncio
import json
import os
from datetime import timedelta
from decimal import Decimal

import pytest

from test_radar_cards_db import SCAN0, TICKER, world  # noqa: F401 — the fixture
from test_strike_detector_db import _crossing, _detector

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]


def apply_0024(store) -> None:
    from cobalt.db_migrations import MIGRATIONS_DIR

    with store._connect() as conn:
        conn.execute((MIGRATIONS_DIR / "0024_strike_alerts.sql").read_text())


def triggered_card(world):  # noqa: F811
    """(card_id, transition_id, at): an ARMED radar card TRIGGERED by P1's tick."""
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.cards import Actor, CardState
    from cobalt.settings.models import TraderSettings

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    record = cards.radar_card(card_id)
    trader = TraderSettings.from_db(world["settings"])
    sizing = size_at_key(
        Grade.B, ticker=TICKER, entry=record["entry"], stop=record["stop"],
        direction=Direction(record["direction"]), sheet_modes=trader.sheet_modes, sheet="half",
        enabled=trader.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("10"),
    )
    cards.tap_key(card_id, sizing)
    cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, now=SCAN0 + timedelta(minutes=1))
    at = SCAN0 + timedelta(minutes=6, seconds=4)
    report = asyncio.run(_detector(cards, fetched=[_crossing(record["direction"], Decimal(record["entry"]))],
                                   at=at).tick())
    assert report.triggered == [card_id]
    with cards._connect() as conn:
        tid = conn.execute("SELECT max(id) FROM card_transitions WHERE card_id = %s", (card_id,)).fetchone()[0]
    return card_id, tid, at


def test_p1s_trigger_reaches_the_stream_with_the_cards_shares_and_stop(world):  # noqa: F811
    from cobalt.aset.strike import StrikeAlertStore, StreamDeps, event_stream
    from cobalt.strike.delivery_config import DeliverySettings

    store = StrikeAlertStore("cobalt_dev")
    apply_0024(store)
    card_id, tid, at = triggered_card(world)
    with world["cards"]._connect() as conn:
        shares, stop, grade = conn.execute(
            "SELECT shares, stop, sized_grade FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()

    polls = {"n": 0}

    async def stop_after_one():
        polls["n"] += 1
        return polls["n"] > 1

    async def no_wait(_s):
        return None

    deps = StreamDeps(store=store, settings=DeliverySettings(), now=lambda: at, sleep=no_wait)

    async def run():
        # A fresh connect: the rows of `at`'s ET date, this transition among them.
        return [c async for c in event_stream(deps, last_event_id=None, stop=stop_after_one)]

    chunks = [c for c in asyncio.run(run()) if c.startswith(f"id: {tid}\n")]
    assert len(chunks) == 1 and chunks[0].startswith(f"id: {tid}\nevent: trigger\n")
    data = json.loads(chunks[0].split("data: ", 1)[1])
    assert data["card_id"] == card_id and data["ticker"] == TICKER
    assert data["shares"] == shares and data["stop"] == str(stop) and data["key"] == grade
    assert data["hotkey"] == f"HALF-{grade}-{data['direction'].upper()}"
    with store._connect() as conn:
        row = conn.execute("SELECT seam_at, pushed_at, shown_at FROM strike_alerts WHERE transition_id = %s",
                           (tid,)).fetchone()
    assert row[1] == at and row[2] is None, "the send stamped pushed_at, nothing else"
