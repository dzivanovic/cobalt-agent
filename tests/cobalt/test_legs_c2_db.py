"""S3 exits C2 as built — exit legs, running shares, corrections, the held
count, CLOSED, the FILLED stop edit (v3 §2–§3, §5; R67, R38).

With-DB, inside the suite's rollback transaction with M1 applied there
(`legs_db_support.apply_0021`), EXCEPT X7: two concurrent ½ taps on REAL
connections (the X1 real-factory pattern), which runs only at the real
`0021` and deletes what it wrote by card id in `finally`.

Every value is constructed (L32): ticker `TEST` / `X7CT`, the sheet
tests' planned 10.0000 / 9.9000, the drift P on a constructed store (L69).
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from cobalt import db as _db
from legs_db_support import apply_0021, card_row, fill_kwargs, legs_of, manual_card, patch_daymode, sizing

REAL_CONNECT = _db.connect
X7CT = "X7CT"

#: 20:30 ET on 2026-09-02 — inside market_reset (the C1 test's instant).
RESET = datetime(2026, 9, 3, 0, 30, tzinfo=timezone.utc)
#: The next trading day after the suite's frozen instant, 10:00 ET.
NEXT_DAY = datetime(2026, 9, 4, 14, 0, tzinfo=timezone.utc)

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


@pytest.fixture
def aset(monkeypatch):
    from cobalt.aset.store import AsetStore

    patch_daymode(monkeypatch)
    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    apply_0021(store)
    return store


def _now():
    from cobalt.session import clock

    return clock.now_utc()


def filled(aset, shares: int = 100, *, price: str = "10.10") -> int:
    """A manual TEST card (planned 10.0000 / 9.9000) filled through THE
    fill for `shares` at `price`."""
    card_id = manual_card(aset)
    aset.mark_filled(card_id, **fill_kwargs(price=price, shares=shares, p=20))
    return card_id


def tap(card_id, preset, running_before, *, shares=None, price="10.20", flag="estimated",
        price_source="last_poll", source="panel", now=None, **kw):
    from cobalt.cards import legs

    ts = now or _now()
    return legs.record_exit(
        card_id, preset=preset, shares=shares, price=Decimal(price), price_source=price_source,
        price_asof=ts if price_source == "last_poll" else None, flag=flag, source=source,
        running_before=running_before, now=ts, **kw,
    )


def running(aset, card_id):
    from cobalt.cards import legs

    with aset._connect() as conn:
        return legs.running_shares(conn, card_id)


def current(aset, card_id):
    with aset._connect() as conn:
        cur = conn.execute("SELECT * FROM legs_current_v WHERE card_id = %s ORDER BY seq", (card_id,))
        return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]


def history(aset, card_id):
    from cobalt.cards.store import CardStore

    return CardStore(aset.db_name).history(card_id)


def entry_leg(aset, card_id):
    return next(l for l in current(aset, card_id) if l["kind"] == "entry")


# ---------------------------------------------------------------------
# C2-1 / C2-2 — the exit leg and the one running read
# ---------------------------------------------------------------------


def test_a_half_on_100_writes_an_estimated_exit_of_50_and_running_is_50(aset):
    card = filled(aset, 100)
    out = tap(card, "half", 100)
    leg = [l for l in current(aset, card) if l["kind"] == "exit"]
    assert len(leg) == 1
    leg = leg[0]
    assert (leg["seq"], leg["shares"], leg["flag"], leg["preset"]) == (1, 50, "estimated", "half")
    assert leg["running_before"] == 100 and leg["id"] == out.leg_id
    assert leg["stop_in_force"] == card_row(aset, card)["stop"]
    assert leg["sheet_mismatch"] is None and leg["corrects"] is None
    r = running(aset, card)
    assert (r.shares, r.basis) == (50, "legs")
    assert out.running_after == 50 and out.closed is False
    assert card_row(aset, card)["state"] == "FILLED"


def test_a_stale_or_duplicate_tap_is_refused_naming_both_counts(aset):
    from cobalt.cards.legs import LegRefused

    card = filled(aset, 100)
    tap(card, "half", 100)
    with pytest.raises(LegRefused, match="REFUSED: screen said 100, now 50 — tap again"):
        tap(card, "half", 100)
    assert running(aset, card).shares == 50
    assert len([l for l in legs_of(aset, card) if l["kind"] == "exit"]) == 1


def test_a_third_on_one_share_is_refused(aset):
    from cobalt.cards.legs import LegRefused

    card = filled(aset, 1)
    with pytest.raises(LegRefused, match="⅓ of 1 is 0 — use flat or type"):
        tap(card, "third", 1)
    assert [l["kind"] for l in legs_of(aset, card)] == ["entry"]


def test_flat_with_a_typed_price_is_confirmed_and_closes_in_the_same_transaction(aset):
    card = filled(aset, 100)
    out = tap(card, "flat", 100, price="10.30", flag="confirmed", price_source="typed")
    assert out.closed is True and out.running_after == 0
    assert card_row(aset, card)["state"] == "CLOSED"
    last = history(aset, card)[-1]
    assert last["to_state"] == "CLOSED" and last["evidence"]["leg_id"] == out.leg_id
    assert last["id"] == out.transition_id
    (leg,) = [l for l in current(aset, card) if l["kind"] == "exit"]
    assert (leg["flag"], leg["shares"], leg["price_source"]) == ("confirmed", 100, "typed")


def test_a_failing_close_rolls_the_leg_back_with_it(aset, monkeypatch):
    from cobalt.cards.store import CardStore

    card = filled(aset, 100)
    real_transition = CardStore.transition

    def broken(self, *a, **k):
        raise RuntimeError("transition broke")

    # Restore ONLY this patch: `monkeypatch.undo()` would also undo the
    # suite's `db.connect` patch and send the reads below to a real
    # session, which blocks behind this transaction's `apply_0021` locks.
    monkeypatch.setattr(CardStore, "transition", broken)
    with pytest.raises(RuntimeError, match="transition broke"):
        tap(card, "flat", 100)
    monkeypatch.setattr(CardStore, "transition", real_transition)
    assert [l["kind"] for l in legs_of(aset, card)] == ["entry"], "the leg rolled back with the close"
    assert card_row(aset, card)["state"] == "FILLED"


def test_a_leg_on_a_card_that_is_not_filled_is_refused(aset):
    from cobalt.cards.legs import LegRefused

    card = manual_card(aset)  # TRIGGERED
    with pytest.raises(LegRefused, match="TRIGGERED"):
        tap(card, "half", 0)
    assert legs_of(aset, card) == []


def test_typed_shares_above_running_are_refused_naming_both(aset):
    from cobalt.cards.legs import LegRefused

    card = filled(aset, 100)
    with pytest.raises(LegRefused, match=r"101.*100"):
        tap(card, "typed", 100, shares=101, flag="confirmed", price_source="typed")
    assert running(aset, card).shares == 100


def test_a_trading_log_exit_needs_its_import_id(aset):
    from cobalt.cards.legs import LegRefused

    card = filled(aset, 100)
    with pytest.raises(LegRefused, match="source_import_id"):
        tap(card, "typed", 100, shares=10, flag="confirmed", price_source="trading_log", source="trading_log")
    out = tap(card, "typed", 100, shares=10, flag="confirmed", price_source="trading_log",
              source="trading_log", source_import_id=7)
    (leg,) = [l for l in current(aset, card) if l["kind"] == "exit"]
    assert leg["id"] == out.leg_id and leg["source_import_id"] == 7


def test_a_card_filled_before_c1_reads_recomputed_shares_else_shares(aset):
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore

    card = manual_card(aset)
    CardStore(aset.db_name).transition(card, CardState.FILLED, actor=Actor.YOU)  # no entry leg
    r = running(aset, card)
    assert (r.shares, r.basis) == (card_row(aset, card)["shares"], "shares")
    with aset._connect() as conn:
        conn.execute("UPDATE aset_sizings SET recomputed_shares = 450 WHERE id = %s", (card,))
    r = running(aset, card)
    assert (r.shares, r.basis) == (450, "recomputed_shares")


# ---------------------------------------------------------------------
# C2-3 — corrections
# ---------------------------------------------------------------------


def test_a_correction_of_a_row_that_is_not_current_is_refused_naming_the_current_id(aset):
    from cobalt.cards.legs import LegRefused, record_correction

    card = filled(aset, 100)
    out = tap(card, "half", 100)
    first = record_correction(out.leg_id, price=Decimal("10.25"), price_source="typed", source="panel", now=_now())
    with pytest.raises(LegRefused, match=f"current row is {first.leg_id}"):
        record_correction(out.leg_id, price=Decimal("10.26"), price_source="typed", source="panel", now=_now())
    (leg,) = [l for l in current(aset, card) if l["kind"] == "exit"]
    assert leg["id"] == first.leg_id and leg["price"] == Decimal("10.25") and leg["flag"] == "confirmed"
    assert leg["corrects"] == out.leg_id and (leg["seq"], leg["kind"]) == (1, "exit")


def test_a_correction_that_moves_a_closed_card_off_zero_is_refused(aset):
    from cobalt.cards.legs import LegRefused, record_correction

    card = filled(aset, 100)
    out = tap(card, "flat", 100, flag="confirmed", price_source="typed")
    before = legs_of(aset, card)
    with pytest.raises(LegRefused, match="CLOSED"):
        record_correction(out.leg_id, shares=60, source="panel", now=_now())
    assert legs_of(aset, card) == before
    assert card_row(aset, card)["state"] == "CLOSED"


def test_a_correction_that_takes_exits_past_the_entry_is_refused(aset):
    from cobalt.cards.legs import LegRefused, record_correction

    card = filled(aset, 100)
    out = tap(card, "half", 100)
    with pytest.raises(LegRefused, match=r"101.*100"):
        record_correction(out.leg_id, shares=101, source="panel", now=_now())


def test_a_correction_that_brings_running_to_zero_closes_the_card(aset):
    from cobalt.cards.legs import record_correction

    card = filled(aset, 100)
    out = tap(card, "half", 100)
    fix = record_correction(out.leg_id, shares=100, source="panel", now=_now())
    assert fix.closed is True and fix.running_after == 0
    assert card_row(aset, card)["state"] == "CLOSED"
    last = history(aset, card)[-1]
    assert last["to_state"] == "CLOSED" and last["evidence"]["leg_id"] == fix.leg_id


def test_an_entry_price_correction_rewrites_the_cache_and_keeps_the_fill_evidence(aset):
    from cobalt.cards.legs import record_correction

    card = filled(aset, 100, price="10.10")
    fill_row = next(h for h in history(aset, card) if h["to_state"] == "FILLED")
    entry = entry_leg(aset, card)
    fix = record_correction(entry["id"], price=Decimal("10.0270"), price_source="typed", source="sheet", now=_now())
    row = card_row(aset, card)
    assert row["actual_fill"] == Decimal("10.0270")
    assert row["distance_change_pct"] == Decimal("27.00")
    assert row["recomputed_shares"] == 472 and row["recomputed_used_risk"] == Decimal("59.94")
    assert row["share_delta"] == 472 - row["shares"]
    assert row["drift_warning_pct"] == Decimal("20.00") and row["drift_warned"] is True
    again = next(h for h in history(aset, card) if h["to_state"] == "FILLED")
    assert again["evidence"] == fill_row["evidence"], "the fill transition keeps the fill-time figures"
    assert again["evidence"]["actual_fill"] == "10.10"
    now_entry = entry_leg(aset, card)
    assert now_entry["id"] == fix.leg_id and now_entry["price"] == Decimal("10.0270")
    assert now_entry["corrects"] == entry["id"] and now_entry["shares"] == entry["shares"]


def test_a_trading_log_correction_needs_its_import_id_and_leaves_his_rows_untouched(aset):
    from cobalt.cards.legs import LegRefused, record_correction

    card = filled(aset, 100)
    out = tap(card, "half", 100)
    his = legs_of(aset, card)
    with pytest.raises(LegRefused, match="source_import_id"):
        record_correction(out.leg_id, price=Decimal("10.22"), price_source="trading_log",
                          source="trading_log", now=_now())
    fix = record_correction(out.leg_id, price=Decimal("10.22"), price_source="trading_log",
                            source="trading_log", now=_now(), source_import_id=7)
    after = legs_of(aset, card)
    assert after[: len(his)] == his, "append-only: his rows are untouched"
    new = after[-1]
    assert new["id"] == fix.leg_id and new["source"] == "trading_log" and new["source_import_id"] == 7
    assert new["corrects"] == out.leg_id


# ---------------------------------------------------------------------
# C2-4 — the held count (S-HELD)
# ---------------------------------------------------------------------


def test_the_held_count_corrects_the_entry_leg_and_wins(aset):
    from cobalt.cards.legs import LegRefused, record_held

    card = filled(aset, 100)
    tap(card, "typed", 100, shares=34, flag="confirmed", price_source="typed")
    assert running(aset, card).shares == 66
    original = entry_leg(aset, card)

    held = record_held(card, 50, source="panel", now=_now())
    entry = entry_leg(aset, card)
    assert entry["id"] == held.leg_id and entry["corrects"] == original["id"]
    assert (entry["held_stated"], entry["shares"], entry["flag"]) == (50, 84, "confirmed")
    assert (entry["price"], entry["price_source"], entry["price_asof"]) == (
        original["price"], original["price_source"], original["price_asof"])
    assert running(aset, card).shares == 50 and card_row(aset, card)["state"] == "FILLED"

    zero = record_held(card, 0, source="panel", now=_now())
    assert zero.closed is True and card_row(aset, card)["state"] == "CLOSED"
    assert entry_leg(aset, card)["shares"] == 34 and running(aset, card).shares == 0

    with pytest.raises(LegRefused, match="CLOSED has no way back — correct the exit instead"):
        record_held(card, 10, source="panel", now=_now())


# ---------------------------------------------------------------------
# C2-6 — the FILLED stop edit, the reset, the owner
# ---------------------------------------------------------------------


def test_a_filled_stop_edit_prices_open_risk_on_the_held_shares_from_the_fill(aset):
    from cobalt.cards.store import CardStore

    card = filled(aset, 100, price="10.10")
    tap(card, "half", 100)
    CardStore(aset.db_name).record_stop_edit(card, from_stop=Decimal("9.90"), to_stop=Decimal("9.95"))
    row = card_row(aset, card)
    assert row["per_share_risk"] == Decimal("0.1500"), "|10.10 fill - 9.95|"
    assert row["used_risk"] == Decimal("7.50"), "0.15 x 50 still held"
    assert row["shares"] == 600, "the planned count is never rewritten"


def test_a_reset_to_the_structural_stop_is_kind_reset_and_the_owner_goes_back_to_cobalt(aset):
    from cobalt.cards.store import CardStore

    card = filled(aset, 100)
    with aset._connect() as conn:
        conn.execute("UPDATE aset_sizings SET structural_stop = 9.8000 WHERE id = %s", (card,))
    cards = CardStore(aset.db_name)
    assert cards.stop_owner(card) == "cobalt"
    cards.record_stop_edit(card, from_stop=Decimal("9.90"), to_stop=Decimal("9.85"))
    assert cards.stop_owner(card) == "yours"
    cards.record_stop_edit(card, from_stop=Decimal("9.85"), to_stop=Decimal("9.80"), kind="reset")
    with aset._connect() as conn:
        kind = conn.execute(
            "SELECT kind FROM card_stop_edits WHERE card_id = %s ORDER BY id DESC LIMIT 1", (card,)
        ).fetchone()[0]
    assert kind == "reset" and cards.stop_owner(card) == "cobalt"
    # a TYPED stop that equals the structural stop stays an edit, and his
    cards.record_stop_edit(card, from_stop=Decimal("9.80"), to_stop=Decimal("9.80"))
    assert cards.stop_owner(card) == "yours"


def test_a_reset_off_the_structural_stop_or_on_a_manual_card_is_refused(aset):
    from cobalt.cards.store import CardStateError, CardStore

    card = filled(aset, 100)
    cards = CardStore(aset.db_name)
    with pytest.raises(CardStateError, match="no Cobalt stop"):
        cards.record_stop_edit(card, from_stop=Decimal("9.90"), to_stop=Decimal("9.80"), kind="reset")
    with aset._connect() as conn:
        conn.execute("UPDATE aset_sizings SET structural_stop = 9.8000 WHERE id = %s", (card,))
    with pytest.raises(CardStateError, match="9.8000"):
        cards.record_stop_edit(card, from_stop=Decimal("9.90"), to_stop=Decimal("9.85"), kind="reset")
    assert card_row(aset, card)["stop"] == Decimal("9.9000")


# ---------------------------------------------------------------------
# market_reset refuses every writer; X-OPEN takes a leg the next day
# ---------------------------------------------------------------------


def test_market_reset_refuses_every_writer_and_writes_nothing(aset):
    from cobalt.cards.legs import record_correction, record_held
    from cobalt.cards.store import CardStore
    from cobalt.session import SessionBlocked

    card = filled(aset, 100)
    out = tap(card, "half", 100)
    before = (legs_of(aset, card), card_row(aset, card)["stop"])
    with pytest.raises(SessionBlocked):
        tap(card, "half", 50, now=RESET)
    with pytest.raises(SessionBlocked):
        record_correction(out.leg_id, price=Decimal("10.25"), price_source="typed", source="panel", now=RESET)
    with pytest.raises(SessionBlocked):
        record_held(card, 20, source="panel", now=RESET)
    with pytest.raises(SessionBlocked):
        CardStore(aset.db_name).record_stop_edit(
            card, from_stop=Decimal("9.90"), to_stop=Decimal("9.95"), now=RESET)
    assert (legs_of(aset, card), card_row(aset, card)["stop"]) == before


def test_x_open_a_filled_card_takes_a_leg_the_next_day(aset):
    from cobalt.cards.expire import expire_due
    from cobalt.cards.store import CardStore

    card = filled(aset, 66)
    expire_due(CardStore(aset.db_name), now=NEXT_DAY)
    assert card_row(aset, card)["state"] == "FILLED"
    out = tap(card, "half", 66, now=NEXT_DAY)
    assert out.running_after == 33 and card_row(aset, card)["state"] == "FILLED"


# ---------------------------------------------------------------------
# C2-7 — `cobalt cards legs <id>`, read only
# ---------------------------------------------------------------------


def test_cards_legs_prints_the_legs_running_realized_r_and_the_owner(aset, capsys):
    import argparse

    from cobalt.cards.cli import cmd_legs

    card = filled(aset, 100)
    tap(card, "half", 100)
    before = legs_of(aset, card)
    cmd_legs(argparse.Namespace(card_id=card))
    out = capsys.readouterr().out
    assert "running: 50 (basis: legs)" in out
    assert "realized R: " in out and "provisional" in out and "realized_r.1" in out
    assert "stop owner: cobalt" in out
    assert legs_of(aset, card) == before, "read only"


# ---------------------------------------------------------------------
# X7 — two concurrent ½ taps on REAL connections (pass 2, real 0021)
# ---------------------------------------------------------------------


class _PausedAfterLock:
    def __init__(self, inner, on_lock):
        object.__setattr__(self, "_inner", inner)
        object.__setattr__(self, "_on_lock", on_lock)
        object.__setattr__(self, "_fired", False)

    def __getattr__(self, item):
        return getattr(self._inner, item)

    def __setattr__(self, key, value):
        setattr(self._inner, key, value)

    def __enter__(self):
        self._inner.__enter__()
        return self

    def __exit__(self, *exc):
        return self._inner.__exit__(*exc)

    def execute(self, query, params=None, *args, **kwargs):
        result = self._inner.execute(query, params, *args, **kwargs)
        if "FOR UPDATE" in str(query) and not self._fired:
            object.__setattr__(self, "_fired", True)
            self._on_lock()
        return result


def _real_read(sql, params):
    from cobalt import env

    conn = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
    try:
        return conn.execute(sql, params).fetchall()
    finally:
        conn.close()


def test_x7_two_concurrent_half_taps_one_writes_the_other_is_refused(monkeypatch):
    import itertools
    import threading
    import time

    from cobalt import env
    from cobalt.aset.engine import compute_sizing
    from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
    from cobalt.aset.store import AsetStore
    from cobalt.cards.legs import ExitResult, LegRefused
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore

    assert _db.connect is not REAL_CONNECT, "the suite patches db.connect; this test undoes it"
    monkeypatch.setattr(_db, "connect", REAL_CONNECT)
    patch_daymode(monkeypatch)
    aset = AsetStore(env.DEV_DB_NAME)
    written: list[int] = []
    results: dict[str, object] = {}
    b_pid: list[int] = []
    waited: list[bool] = []

    def do_tap(name):
        try:
            results[name] = tap(card, "half", 100)
        except Exception as exc:  # the refusal is the expected outcome for one tap
            results[name] = exc

    b_thread = threading.Thread(target=do_tap, args=("B",))

    def on_lock():
        b_thread.start()
        probe = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
        try:
            deadline = time.monotonic() + 15
            while time.monotonic() < deadline:
                if b_pid and probe.execute(
                    "SELECT count(*) FROM pg_catalog.pg_locks WHERE pid = %s AND NOT granted", (b_pid[0],)
                ).fetchone()[0]:
                    waited.append(True)
                    return
                time.sleep(0.05)
        finally:
            probe.close()

    try:
        card = aset.save(compute_sizing(
            SizingInput(ticker=X7CT, grade=Grade.B, direction=Direction.LONG, sheet_mode=SheetMode.FULL,
                        risk_dollars=Decimal("10"), entry=Decimal("10.00"), stop=Decimal("9.90")),
            (Grade.A, Grade.B),
            Decimal("10"),
        ))
        written.append(card)
        cards = CardStore(aset.db_name)
        cards.transition(card, CardState.ARMED, actor=Actor.YOU)
        cards.transition(card, CardState.TRIGGERED, actor=Actor.YOU)
        aset.mark_filled(card, **fill_kwargs(price="10.05", shares=100, p=20))

        calls = itertools.count()

        def factory(dbname, *, side, allow_prod=False):
            conn = REAL_CONNECT(dbname, side=side, allow_prod=allow_prod)
            n = next(calls)
            if n == 0:
                return _PausedAfterLock(conn, on_lock)
            b_pid.append(conn.info.backend_pid)
            return conn

        monkeypatch.setattr(_db, "connect", factory)
        do_tap("A")
        b_thread.join(timeout=30)
        monkeypatch.setattr(_db, "connect", REAL_CONNECT)

        assert waited == [True], "tap B never waited on tap A's card lock"
        wrote = [r for r in results.values() if isinstance(r, ExitResult)]
        refused = [r for r in results.values() if isinstance(r, LegRefused)]
        assert len(wrote) == 1 and len(refused) == 1, results
        assert "screen said 100, now 50" in str(refused[0])
        exits = _real_read(
            "SELECT shares FROM legs_current_v WHERE card_id = %s AND kind = 'exit'", (card,))
        assert exits == [(50,)], "exactly one exit of 50"
    finally:
        cleanup = REAL_CONNECT(env.DEV_DB_NAME, side=_db.Side.USER)
        try:
            for table in ("legs", "picks"):
                cleanup.execute(f"DELETE FROM {table} WHERE card_id = ANY(%s)", (written,))
            cleanup.execute("DELETE FROM aset_sizings WHERE id = ANY(%s)", (written,))
        finally:
            cleanup.close()
        assert _real_read("SELECT count(*) FROM aset_sizings WHERE ticker = %s", (X7CT,))[0][0] == 0
