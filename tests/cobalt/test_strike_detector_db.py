"""S4-P1 C2/C3 on cobalt_dev (`requires_db`, hub-run).

The card is made the one way a radar card is made — the S5 stage's
`create_radar_card` (the `test_radar_cards_db.world` fixture, which applies
`0022` inside the suite's rollback, L76) — then sized and armed through
`CardStore`, and one detector tick runs against the REAL store with a fake
fetch. Everything rolls back with the suite transaction. Ticker, prices and
dates are constructed (L32); SCAN0 is 11:30 ET, RTH.
"""

from __future__ import annotations

import asyncio
import os
from datetime import timedelta
from decimal import Decimal

import pytest

import radar_p2_support as sup
from test_radar_cards_db import SCAN0, TICKER, world  # noqa: F401 — the fixture

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]

MD5 = "0123456789abcdef0123456789abcdef"


def _bar(minute: int, *, high: Decimal, low: Decimal):
    from cobalt.archiver.models import Bar, Interval

    return Bar(ticker=TICKER, interval=Interval.I1, ts=SCAN0 + timedelta(minutes=minute), open=Decimal("5.40"),
               high=high, low=low, close=Decimal("5.40"), volume=100)


def _detector(cards, *, fetched=(), stored=(), at):
    from cobalt.radar.collector import TokenBucket
    from cobalt.session.models import Session
    from cobalt.strike.config import StrikeSettings
    from cobalt.strike.detector import DemandPlan, StrikeDetector

    async def fetch(ticker, interval, token):
        return list(fetched)

    async def no_wait(_s):
        return None

    return StrikeDetector(
        store=cards, fetch=fetch, token="constructed-token",
        defs=lambda slug: (MD5, sup.anatomy_def()), stored_bars=lambda ticker, start, end: list(stored),
        settings=StrikeSettings(poll_interval_min=2, max_armed=5, alert_criterion_s=5, missed_sweep_interval=100),
        plan=lambda: DemandPlan(planned_rpm=0.0, headroom_rpm=50.0), session_of=lambda _now: Session.RTH,
        now=lambda: at, bucket_factory=lambda rpm: TokenBucket(rpm, sleep=no_wait),
    )


def _crossing(direction: str, entry: Decimal):
    if direction == "long":
        return _bar(5, high=entry + Decimal("0.05"), low=entry - Decimal("0.10"))
    return _bar(5, high=entry + Decimal("0.10"), low=entry - Decimal("0.05"))


def _last_row(cards, card_id):
    with cards._connect() as conn:
        return conn.execute(
            "SELECT to_state, actor, evidence, reason FROM card_transitions WHERE card_id = %s ORDER BY id DESC "
            "LIMIT 1", (card_id,),
        ).fetchone()


def test_an_armed_radar_card_is_triggered_by_one_tick(world):  # noqa: F811
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.cards import Actor, CardState
    from cobalt.settings.models import TraderSettings
    from cobalt.strike.detector import CONTRACT_KEYS

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    record = cards.radar_card(card_id)
    trader = TraderSettings.from_db(world["settings"])
    sizing = size_at_key(
        Grade.A_PLUS, ticker=TICKER, entry=record["entry"], stop=record["stop"],
        direction=Direction(record["direction"]), sheet_modes=trader.sheet_modes, sheet="half",
        enabled=trader.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("10"),
    )
    cards.tap_key(card_id, sizing)
    cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, now=SCAN0 + timedelta(minutes=1))

    [strike_card] = [c for c in cards.strike_cards() if c.card_id == card_id]
    assert strike_card.state == "ARMED" and strike_card.armed_at == SCAN0 + timedelta(minutes=1)

    at = SCAN0 + timedelta(minutes=6, seconds=4)
    entry = Decimal(record["entry"])
    report = asyncio.run(_detector(cards, fetched=[_crossing(record["direction"], entry)], at=at).tick())
    assert report.triggered == [card_id]
    to_state, actor, evidence, reason = _last_row(cards, card_id)
    assert (to_state, actor) == ("TRIGGERED", "cobalt")
    assert tuple(evidence) == CONTRACT_KEYS or set(evidence) == set(CONTRACT_KEYS)
    assert evidence["via"] == "strike.detector"
    assert cards.state_of(card_id) is CardState.TRIGGERED


def test_a_watch_radar_card_whose_bars_cross_is_missed(world):  # noqa: F811
    from cobalt.cards import CardState
    from cobalt.strike.detector import CONTRACT_KEYS

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    record = cards.radar_card(card_id)
    # `created_at` is the column default (the suite transaction's own clock);
    # the constructed bars live on SCAN0's day, so the row is put there.
    with cards._connect() as conn:
        conn.execute("UPDATE aset_sizings SET created_at = %s WHERE id = %s", (SCAN0, card_id))
    [strike_card] = [c for c in cards.strike_cards() if c.card_id == card_id]
    assert strike_card.state == "WATCH" and strike_card.armed_at is None
    assert strike_card.created_at == SCAN0

    at = SCAN0 + timedelta(minutes=8)
    report = asyncio.run(_detector(cards, stored=[_crossing(record["direction"], Decimal(record["entry"]))],
                                   at=at).tick())
    assert report.missed == [card_id]
    to_state, actor, evidence, reason = _last_row(cards, card_id)
    assert (to_state, actor) == ("MISSED", "cobalt")
    assert reason and reason.strip()
    assert set(evidence) == set(CONTRACT_KEYS) and evidence["via"] == "strike.missed"
    assert cards.state_of(card_id) is CardState.MISSED
