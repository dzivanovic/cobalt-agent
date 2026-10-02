"""X5 — a tap that commits while `refresh_radar_card` waits on the card's
row lock is never overwritten (card 22, `f15-p1-decisions-2026-09-30.md`
DECISION 4; the F15 P1 build's X5 RUN row, `f15-p1-build-2026-09-30.md:352`).

Two REAL sessions on the real `db.connect`, outside the suite's rolled-back
transaction (the `tests/experiments/f15_p1/test_x5_tap_vs_refresh_db.py`
pattern): session A holds the card's row lock, session B starts
`refresh_radar_card` with `tap_version=0`. B's wait is PROVEN, never slept
on: a third connection polls `pg_stat_activity` for B's backend until its
`wait_event_type` is `Lock`, and only then is A released to commit.

`cobalt.cards.predictions.write_record` is replaced by a capture that binds
its arguments against the real signature and writes nothing: a committed
record is immutable and pins its card (`0022_prediction_records.sql:14-21`),
so the card could never be deleted. The record path itself stays pinned by
`test_f15_p1_records_db.py`.

Needs `0022` (both UPDATEs write `last_price_bar_ts`): pass 1 deselects
this file, pass 2 runs it. Every row is deleted by id in `finally` and
counted zero. Constructed values only (L32): ticker `ZZX5R`, pool `x5_fix`.
"""

from __future__ import annotations

import inspect
import os
import threading
import time
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt import db as _db
from cobalt import env

#: The UNPATCHED factory, bound at import (`dev_db_tx` patches per test).
REAL_CONNECT = _db.connect
UTC = timezone.utc
TICKER, POOL = "ZZX5R", "x5_fix"
NOW = datetime(2026, 9, 3, 14, 0, tzinfo=UTC)  # the suite's frozen instant, mid-RTH
WAIT_S = 10

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]


def _real(side):
    return REAL_CONNECT(env.DEV_DB_NAME, side=side)


def _settings():
    from cobalt.settings.card import CardSettings
    from test_radar_cards_db import ENABLED

    return CardSettings.from_rows(ENABLED)


def _enabled():
    from cobalt.aset.models import Grade

    return [Grade.A, Grade.B, Grade.C]


def _capture_records(monkeypatch) -> list[dict]:
    """Replace the one record writer with a capture: the arguments are bound
    against the real signature (a changed parameter fails here) and kept;
    nothing is written."""
    from cobalt.cards import predictions

    signature = inspect.signature(predictions.write_record)
    captured: list[dict] = []

    def capture(conn, **kwargs):
        signature.bind(conn, **kwargs)
        captured.append(kwargs)
        return 0

    monkeypatch.setattr(predictions, "write_record", capture)
    return captured


def _radar_card(monkeypatch, made: dict) -> None:
    """One committed radar card on cobalt_dev through the ONE creation path,
    with the system rows its provenance needs. Every id lands in `made` as
    soon as it exists, so `_cleanup(made)` deletes whatever was written."""
    from cobalt.cards.radar import RadarCardSpec
    from cobalt.cards.scoring import Dot
    from cobalt.cards.store import CardStore

    assert _db.connect is not REAL_CONNECT, "the suite patches db.connect; this test undoes it"
    monkeypatch.setattr(_db, "connect", REAL_CONNECT)
    system = _real(_db.Side.SYSTEM)
    try:
        system.execute("INSERT INTO radar_pool (pool_key, state, session, members) VALUES (%s, 'scanning', 'rth', 1)",
                       (POOL,))
        made["member_id"] = system.execute(
            "INSERT INTO radar_membership (pool_key, ticker, trade_date, first_seen_at, entered_at, source, sources, "
            "rank_at_entry, last_rank, session, opened_scan_id, last_scan_id) VALUES "
            "(%s, %s, %s, %s, %s, 'screen', '[]', 1, 1, 'rth', -77, -77) RETURNING id",
            (POOL, TICKER, NOW.date(), NOW - timedelta(hours=1), NOW - timedelta(hours=1)),
        ).fetchone()[0]
        made["run_id"] = system.execute(
            "INSERT INTO radar_score_run (pool_key, scan_id, session, started_at, status, cards_enabled, "
            "evaluator_version, formula_sha256, tunables_sha256, settings_sha256, cohort_sha256) VALUES "
            "(%s, -77, 'RTH', %s, 'complete', true, 'x', %s, %s, %s, %s) RETURNING id",
            (POOL, NOW, "a" * 64, "b" * 64, "c" * 64, "d" * 64),
        ).fetchone()[0]
        made["score_id"] = system.execute(
            "INSERT INTO radar_score (run_id, membership_id, ticker, trade_def_md5, direction, evaluation, detail, "
            "desk_shadow, inputs_sha256) VALUES (%s, %s, %s, %s, 'short', 'formed', '{}', '{}', %s) RETURNING id",
            (made["run_id"], made["member_id"], TICKER, "0" * 32, "e" * 64),
        ).fetchone()[0]
        system.commit()
    finally:
        system.close()
    spec = RadarCardSpec(
        ticker=TICKER, direction="short", session="RTH", pool_member_id=made["member_id"],
        trade_def_slug="x5-fix", trade_def_md5="0" * 32, setup_ref="overextension", trigger_type="bar_break",
        trigger_price=Decimal("5.50"), stop_ref="snapback_candle", structural_stop=Decimal("5.81"),
        formed_at=NOW - timedelta(minutes=5), expires_at=NOW + timedelta(hours=1), why="x5 fix",
        radar_score_id=made["score_id"], scan_id=-77, formula_sha256="a" * 64, tunables_sha256="b" * 64,
        settings_sha256="c" * 64, proximity=Decimal("0.5"),
        dots=[Dot(factor="setup_relation", position=0, source="human", tier="judgment", role="human")],
        evidence={"run_id": made["run_id"]},
    )
    made["card_id"] = CardStore(env.DEV_DB_NAME).create_radar_card(spec, proposed_key_reason=None, now=NOW)
    assert made["card_id"] is not None


def _cleanup(made: dict) -> dict:
    """Delete every row `_radar_card` wrote, by id; return the counts left."""
    card_id = made.get("card_id")
    user = _real(_db.Side.USER)
    try:
        if card_id is not None:
            user.execute("DELETE FROM aset_sizings WHERE id = %s", (card_id,))
        user.commit()
    finally:
        user.close()
    system = _real(_db.Side.SYSTEM)
    try:
        if made.get("run_id") is not None:
            system.execute("DELETE FROM radar_score_run WHERE id = %s", (made["run_id"],))
        if made.get("member_id") is not None:
            system.execute("DELETE FROM radar_membership WHERE id = %s", (made["member_id"],))
        system.execute("DELETE FROM radar_pool WHERE pool_key = %s", (POOL,))
        system.commit()
        left = {
            "radar_pool": system.execute("SELECT count(*) FROM radar_pool WHERE pool_key = %s", (POOL,)).fetchone()[0],
            "radar_membership": system.execute("SELECT count(*) FROM radar_membership WHERE ticker = %s",
                                               (TICKER,)).fetchone()[0],
            "radar_score": system.execute("SELECT count(*) FROM radar_score WHERE ticker = %s", (TICKER,)).fetchone()[0],
        }
    finally:
        system.close()
    user = _real(_db.Side.USER)
    try:
        left["aset_sizings"] = user.execute("SELECT count(*) FROM aset_sizings WHERE ticker = %s",
                                            (TICKER,)).fetchone()[0]
        for table in ("card_dots", "card_dot_taps", "card_transitions", "prediction_records"):
            left[table] = user.execute(f"SELECT count(*) FROM {table} WHERE card_id = %s", (card_id,)).fetchone()[0]
    finally:
        user.close()
    return left


def _update(made: dict, *, conviction, card_score, proposed_key):
    from cobalt.cards.scoring import Dot
    from cobalt.radar.evaluate import CardUpdate

    return CardUpdate(
        card_id=made["card_id"], proximity=Decimal("0.6"), conviction=conviction, card_score=card_score,
        score_suppressed=None, proposed_key=proposed_key,
        dots=[Dot(factor="setup_relation", position=0, source="human", tier="judgment", role="human")],
        health=None, radar_score_id=made["score_id"], tap_version=0, last_price=Decimal("5.40"),
        last_price_bar_ts=NOW - timedelta(minutes=1),
    )


def _row(card_id: int) -> dict:
    user = _real(_db.Side.USER)
    try:
        cur = user.execute("SELECT proximity, conviction, card_score, score_suppressed, proposed_key "
                           "FROM aset_sizings WHERE id = %s", (card_id,))
        return dict(zip([d.name for d in cur.description], cur.fetchone()))
    finally:
        user.close()


class _PausedAfterLock:
    """A real connection that runs `on_lock()` right after its first
    `… FOR UPDATE` — session A paused while it holds the card lock."""

    def __init__(self, inner, on_lock):
        object.__setattr__(self, "_inner", inner)
        object.__setattr__(self, "_on_lock", on_lock)
        object.__setattr__(self, "_fired", False)

    def __getattr__(self, item):
        return getattr(self._inner, item)

    def __setattr__(self, key, value):
        setattr(self._inner, key, value)

    def execute(self, query, params=None, *args, **kwargs):
        result = self._inner.execute(query, params, *args, **kwargs)
        if "FOR UPDATE" in str(query) and not self._fired:
            object.__setattr__(self, "_fired", True)
            self._on_lock()
        return result


def _route(monkeypatch, b_thread, b_pid: list, pause=None) -> None:
    """The real factory for every caller; B's connection records its
    backend pid, and (with `pause`) the main thread's first connection —
    the tap's — is paused right after its lock."""
    paused: list = []

    def factory(dbname, *, side, allow_prod=False):
        conn = REAL_CONNECT(dbname, side=side, allow_prod=allow_prod)
        if threading.current_thread() is b_thread:
            b_pid.append(conn.info.backend_pid)
            return conn
        if pause is not None and not paused:
            paused.append(conn)
            return _PausedAfterLock(conn, pause)
        return conn

    monkeypatch.setattr(_db, "connect", factory)


def _b_waits_on_a_lock(b_pid: list) -> bool:
    """Poll `pg_stat_activity` until B's backend waits on a lock; False
    after `WAIT_S`. The probe runs as the login role (`RESET ROLE`): a
    backend's wait is shown only to its own role, and B's session role is
    the login. Autocommit, so every poll reads a fresh activity snapshot."""
    probe = _real(_db.Side.USER)
    try:
        probe.execute("RESET ROLE")
        probe.commit()
        probe.autocommit = True
        deadline = time.monotonic() + WAIT_S
        while time.monotonic() < deadline:
            if b_pid:
                row = probe.execute("SELECT wait_event_type FROM pg_catalog.pg_stat_activity WHERE pid = %s",
                                    (b_pid[0],)).fetchone()
                if row is not None and row[0] == "Lock":
                    return True
            time.sleep(0.05)
        return False
    finally:
        probe.close()


def _refresh_in(out: dict, update, run_id: int):
    from cobalt.cards.store import CardStore

    def session_b():
        try:
            out["b_wrote_all"] = CardStore(env.DEV_DB_NAME).refresh_radar_card(
                update, run_id=run_id, now=NOW + timedelta(seconds=2))
        except Exception as e:  # noqa: BLE001 — asserted absent below, with its text
            out["b_error"] = f"{type(e).__name__}: {e}"

    return threading.Thread(target=session_b, daemon=True)


def _no_rows_left(made: dict) -> None:
    left = _cleanup(made)
    assert set(left.values()) == {0}, f"rows left after cleanup: {left}"


def test_x5_a_tap_committed_while_the_refresh_waits_keeps_its_numbers(monkeypatch):
    from cobalt.cards.scoring import card_score
    from cobalt.cards.store import CardStore

    made: dict = {}
    out: dict = {}
    b_pid: list = []
    try:
        records = _capture_records(monkeypatch)
        _radar_card(monkeypatch, made)
        card_id = made["card_id"]
        update = _update(made, conviction=None, card_score=None, proposed_key=None)
        b_thread = _refresh_in(out, update, made["run_id"])

        def on_lock():  # A holds the card lock: start B, prove it waits, then let A commit
            b_thread.start()
            out["b_waited"] = _b_waits_on_a_lock(b_pid)

        _route(monkeypatch, b_thread, b_pid, pause=on_lock)
        a = CardStore(env.DEV_DB_NAME).tap_dot(card_id, "setup_relation", 7, settings=_settings(),
                                               enabled=_enabled(), now=NOW + timedelta(seconds=1))
        b_thread.join(timeout=30)
        monkeypatch.setattr(_db, "connect", REAL_CONNECT)

        assert out.get("b_waited") is True, "B never waited"
        assert "b_error" not in out, out.get("b_error")
        assert a["conviction"] is not None and a["proposed_key"] is not None, \
            "the tap must move conviction and key for this test to discriminate"
        assert out["b_wrote_all"] is False, "the refresh did not see the tap that committed while it waited"
        row = _row(card_id)
        assert row["conviction"] == Decimal(a["conviction"])
        assert row["proposed_key"] == a["proposed_key"]
        assert row["card_score"] == card_score(Decimal(a["conviction"]), update.proximity, a["score_suppressed"])
        refresh = [r for r in records if r["kind"] == "refresh"]
        assert len(refresh) == 1
        assert refresh[0]["inputs"]["taps_moved"] is True
        assert Decimal(str(refresh[0]["inputs"]["locked"]["conviction"])) == Decimal(a["conviction"])
    finally:
        monkeypatch.setattr(_db, "connect", REAL_CONNECT)
        _no_rows_left(made)


def test_x5n_a_refresh_that_waits_on_a_lock_with_no_tap_writes_the_stage_numbers(monkeypatch):
    made: dict = {}
    out: dict = {}
    b_pid: list = []
    try:
        records = _capture_records(monkeypatch)
        _radar_card(monkeypatch, made)
        card_id = made["card_id"]
        update = _update(made, conviction=Decimal("0.55"), card_score=33, proposed_key="C")
        b_thread = _refresh_in(out, update, made["run_id"])
        _route(monkeypatch, b_thread, b_pid)
        holder = _real(_db.Side.USER)  # session A: the lock, no tap
        try:
            holder.commit()
            holder.autocommit = False  # the factory's connection autocommits: the lock would end with the SELECT
            holder.execute("SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE", (card_id,))
            b_thread.start()
            out["b_waited"] = _b_waits_on_a_lock(b_pid)
            holder.commit()
        finally:
            holder.close()
        b_thread.join(timeout=30)
        monkeypatch.setattr(_db, "connect", REAL_CONNECT)

        assert out.get("b_waited") is True, "B never waited"
        assert "b_error" not in out, out.get("b_error")
        assert out["b_wrote_all"] is True
        row = _row(card_id)
        assert (row["proximity"], row["conviction"], row["card_score"], row["proposed_key"]) == (
            Decimal("0.6"), Decimal("0.55"), 33, "C")
        refresh = [r for r in records if r["kind"] == "refresh"]
        assert len(refresh) == 1
        assert refresh[0]["inputs"] == {"taps_moved": False, "locked": None}
    finally:
        monkeypatch.setattr(_db, "connect", REAL_CONNECT)
        _no_rows_left(made)
