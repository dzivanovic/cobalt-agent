"""X12 (iii) — card 61 RUN row, FINAL row X12 (R2-1 (c) B's precondition).

Does `card_transitions.id` rise in COMMIT order for one card when two
sessions contend on its row lock? Run at BASE, on the REAL `db.connect`
(two real sessions, the `test_s3_c2_experiments.py` X21 pattern), with ONE
constructed radar card. Asserts nothing about the answer (L70): it prints
both ids and the commit order.

The card needs its system rows (a pool, a membership, a run and a score
row: `aset_sizings_radar_provenance` requires `radar_score_id`); every row
this module writes is deleted by id in `finally` — the card first
(`card_transitions`, `card_dots`, `card_dot_taps` cascade), then the run
(its score cascades), the membership and the pool — and proven gone.
Constructed values only (L32): tickers `X12TR` / `X5TR`, pools `f15_x12` /
`f15_x5`.
"""

from __future__ import annotations

import os
import threading
import time
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt import db as _db

#: The UNPATCHED factory, bound at import (`dev_db_tx` patches per test).
REAL_CONNECT = _db.connect
UTC = timezone.utc

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _real(side):
    from cobalt import env

    return REAL_CONNECT(env.DEV_DB_NAME, side=side)


def real_radar_card(monkeypatch, made: dict, dot_factor: str = "setup_relation") -> dict:
    """One committed radar card on cobalt_dev through the ONE creation path
    (`create_radar_card`), with the system rows its provenance needs. Every
    id lands in `made` as soon as it exists, so `cleanup(made)` in the
    caller's `finally` deletes whatever was written."""
    from cobalt.cards.radar import RadarCardSpec
    from cobalt.cards.scoring import Dot
    from cobalt.cards.store import CardStore

    assert _db.connect is not REAL_CONNECT, "the suite patches db.connect; this experiment undoes it"
    monkeypatch.setattr(_db, "connect", REAL_CONNECT)
    now = datetime(2026, 9, 3, 14, 0, tzinfo=UTC)  # the suite's frozen instant
    pool, ticker = made["pool"], made["ticker"]
    system = _real(_db.Side.SYSTEM)
    try:
        system.execute("INSERT INTO radar_pool (pool_key, state, session, members) VALUES (%s, 'scanning', 'rth', 1)",
                       (pool,))
        made["member_id"] = system.execute(
            "INSERT INTO radar_membership (pool_key, ticker, trade_date, first_seen_at, entered_at, source, sources, "
            "rank_at_entry, last_rank, session, opened_scan_id, last_scan_id) VALUES "
            "(%s, %s, %s, %s, %s, 'screen', '[]', 1, 1, 'rth', -77, -77) RETURNING id",
            (pool, ticker, now.date(), now - timedelta(hours=1), now - timedelta(hours=1)),
        ).fetchone()[0]
        made["run_id"] = system.execute(
            "INSERT INTO radar_score_run (pool_key, scan_id, session, started_at, status, cards_enabled, "
            "evaluator_version, formula_sha256, tunables_sha256, settings_sha256, cohort_sha256) VALUES "
            "(%s, -77, 'RTH', %s, 'complete', true, 'x', %s, %s, %s, %s) RETURNING id",
            (pool, now, "a" * 64, "b" * 64, "c" * 64, "d" * 64),
        ).fetchone()[0]
        made["score_id"] = system.execute(
            "INSERT INTO radar_score (run_id, membership_id, ticker, trade_def_md5, direction, evaluation, detail, "
            "desk_shadow, inputs_sha256) VALUES (%s, %s, %s, %s, 'short', 'formed', '{}', '{}', %s) RETURNING id",
            (made["run_id"], made["member_id"], ticker, "0" * 32, "e" * 64),
        ).fetchone()[0]
        system.commit()
    finally:
        system.close()
    spec = RadarCardSpec(
        ticker=ticker, direction="short", session="RTH", pool_member_id=made["member_id"],
        trade_def_slug="f15-experiment", trade_def_md5="0" * 32, setup_ref="overextension", trigger_type="bar_break",
        trigger_price=Decimal("5.50"), stop_ref="snapback_candle", structural_stop=Decimal("5.81"),
        formed_at=now - timedelta(minutes=5), expires_at=now + timedelta(hours=1), why="f15 experiment",
        radar_score_id=made["score_id"], scan_id=-77, formula_sha256="a" * 64, tunables_sha256="b" * 64,
        settings_sha256="c" * 64, proximity=Decimal("0.5"),
        dots=[Dot(factor=dot_factor, position=0, source="human", tier="judgment", role="human")],
        evidence={"run_id": made["run_id"]},
    )
    made["card_id"] = CardStore("cobalt_dev").create_radar_card(spec, now=now)
    return made


def cleanup(made: dict) -> dict:
    """Delete every row `real_radar_card` wrote, by id; return the counts left."""
    user = _real(_db.Side.USER)
    try:
        if made.get("card_id") is not None:
            user.execute("DELETE FROM aset_sizings WHERE id = %s", (made["card_id"],))
        user.commit()
    finally:
        user.close()
    system = _real(_db.Side.SYSTEM)
    try:
        if made.get("run_id") is not None:
            system.execute("DELETE FROM radar_score_run WHERE id = %s", (made["run_id"],))
        if made.get("member_id") is not None:
            system.execute("DELETE FROM radar_membership WHERE id = %s", (made["member_id"],))
        system.execute("DELETE FROM radar_pool WHERE pool_key = %s", (made["pool"],))
        system.commit()
        left = {
            "radar_pool": system.execute("SELECT count(*) FROM radar_pool WHERE pool_key = %s",
                                         (made["pool"],)).fetchone()[0],
            "radar_membership": system.execute("SELECT count(*) FROM radar_membership WHERE ticker = %s",
                                               (made["ticker"],)).fetchone()[0],
            "radar_score": system.execute("SELECT count(*) FROM radar_score WHERE ticker = %s",
                                          (made["ticker"],)).fetchone()[0],
        }
    finally:
        system.close()
    user = _real(_db.Side.USER)
    try:
        left["aset_sizings"] = user.execute("SELECT count(*) FROM aset_sizings WHERE ticker = %s",
                                            (made["ticker"],)).fetchone()[0]
    finally:
        user.close()
    return left


@requires_db
def test_x12_iii_transition_ids_rise_in_commit_order_under_the_row_lock(monkeypatch):
    from cobalt.cards import Actor, CardState
    from cobalt.cards.store import CardStore

    made: dict = {"pool": "f15_x12", "ticker": "X12TR"}
    order: list[str] = []
    ids: dict[str, int] = {}
    try:
        real_radar_card(monkeypatch, made)
        card_id = made["card_id"]
        sizer = _real(_db.Side.USER)
        try:  # ARM needs a sized card (the sized-card invariant): four constructed sizing values
            sizer.execute("UPDATE aset_sizings SET grade = 'B', risk_budget = 60, shares = 193, used_risk = 59.83 "
                          "WHERE id = %s", (card_id,))
            sizer.commit()
        finally:
            sizer.close()
        cards = CardStore("cobalt_dev")
        a = _real(_db.Side.USER)
        a.autocommit = False
        a.execute("SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,))
        ids["A"] = cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, conn=a)

        def session_b():
            ids["B"] = cards.transition(card_id, CardState.WATCH, actor=Actor.YOU, reason="x12 disarm")
            order.append("B committed")

        b = threading.Thread(target=session_b)
        b.start()
        time.sleep(1.0)
        b_waiting = b.is_alive()
        a.commit()
        order.append("A committed")
        a.close()
        b.join(timeout=30)
        with _real(_db.Side.USER) as reader:
            rows = reader.execute("SELECT id, from_state, to_state FROM card_transitions WHERE card_id = %s "
                                  "ORDER BY id", (card_id,)).fetchall()
        print(f"X12 (iii): B waited on A's lock: {b_waiting}")
        print(f"X12 (iii): A (WATCH->ARMED) transition id {ids['A']}; B (ARMED->WATCH) transition id {ids.get('B')}")
        print(f"X12 (iii): commit order {order}; ids rise in commit order: {ids.get('B', 0) > ids['A']}")
        print(f"X12 (iii): the card's ledger {rows}")
    finally:
        left = cleanup(made)
        print(f"X12 (iii): rows left after cleanup {left}")
