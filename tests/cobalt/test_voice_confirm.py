"""C10 — confirm (FINAL [F-08] word for word, [F-09], L37).

While a row is `awaiting_confirm` and younger than `confirm_ttl_s` the turn
makes NO model call. The whole normalized transcript must EQUAL `yes`
(or he taps Confirm); `no` cancels; ANY other transcript, or the TTL, ends
the pending action with nothing executed, and that transcript is not
planned. One single-flight token. Execution RE-COMPUTES the dry run and
requires the same hashes; a mismatch is REFUSED with the new read-back.

Normalization, stated: NFKC, Unicode casefold, strip whitespace, then
strip leading / trailing `. , ! ?` — the engine writes a spoken yes as
"Yes." (X-X1 and X-E2 counted with this same rule: 0 false confirms of 70,
12 of 12 confirm words right). Nothing inside the word is touched.
"""

from __future__ import annotations

import os
import threading
import uuid
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.voice import confirm as cf
from cobalt.voice import tools as tl
from cobalt.voice.models import TurnState
from cobalt.voice.registry import load_agent

RAW_CONNECT = db.connect
AGENT = load_agent()
NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
CARD = {"id": 11, "ticker": "XYZ", "direction": "long", "state": "WATCH", "stop": Decimal("4.4000")}

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


# --- the word match ------------------------------------------------------------------


@pytest.mark.parametrize("text", ["yes", "Yes.", " YES ", "yes!", "Yes?", "ｙｅｓ"])
def test_confirm_words(text):
    assert cf.classify(text, AGENT) == "confirm"


@pytest.mark.parametrize("text", ["no", "No.", "NO!"])
def test_cancel_words(text):
    assert cf.classify(text, AGENT) == "cancel"


@pytest.mark.parametrize("text", ["yes please", "yeah", "yes, move it", "move the stop on XYZ to 4.50 yes",
                                  "you", "", "y e s", "yes no", "sure", "okay"])
def test_anything_else_is_other(text):
    assert cf.classify(text, AGENT) == "other"


# --- the pending action against an in-memory single-flight store ---------------------------


class MemStore:
    """The store contract (single-flight transitions) without Postgres."""

    def __init__(self):
        self.rows = {}
        self.lock = threading.Lock()

    def put(self, turn_id, state, **fields):
        self.rows[turn_id] = {"turn_id": turn_id, "state": state.value, **fields}

    def transition(self, turn_id, expected, new, *, at, **fields):
        with self.lock:
            row = self.rows.get(turn_id)
            if row is None or row["state"] not in {s.value for s in expected}:
                return False
            row.update(fields, state=new.value)
            return True

    def get(self, turn_id):
        return self.rows.get(turn_id)


def _pending_row(store, ttl=60, now=NOW):
    p = tl.stop_dry_run(CARD, Decimal("4.50"), ttl_s=ttl, now=now)
    store.put("t-pending", TurnState.AWAITING_CONFIRM, pending_action=p.model_dump(mode="json"))
    return store.get("t-pending")


def test_confirm_executes_once_and_records_the_experts_write():
    s, calls = MemStore(), []

    def execute(p):
        calls.append(p.card_id)
        return type("E", (), {"stop_edit_id": 501})()

    out = cf.confirm_pending(s, _pending_row(s), now=NOW, execute=execute)
    assert out.kind == "done" and calls == [11]
    row = s.get("t-pending")
    assert row["state"] == "done" and row["expert_write_kind"] == "card_stop_edits" and row["expert_write_id"] == 501


def test_a_second_confirm_finds_no_pending_action():
    s, calls = MemStore(), []
    row = _pending_row(s)
    execute = lambda p: calls.append(1) or type("E", (), {"stop_edit_id": 1})()  # noqa: E731
    assert cf.confirm_pending(s, row, now=NOW, execute=execute).kind == "done"
    assert cf.confirm_pending(s, row, now=NOW, execute=execute).kind == "no_pending"
    assert calls == [1]


def test_an_expired_pending_action_executes_nothing():
    s, calls = MemStore(), []
    row = _pending_row(s, ttl=60, now=NOW - timedelta(seconds=61))
    out = cf.confirm_pending(s, row, now=NOW, execute=lambda p: calls.append(1))
    assert out.kind == "expired" and calls == [] and s.get("t-pending")["state"] == "expired"


def test_cancel_and_other_end_the_action_with_nothing_executed():
    s = MemStore()
    assert cf.cancel_pending(s, _pending_row(s), now=NOW, reason="no").kind == "cancelled"
    assert s.get("t-pending")["state"] == "cancelled"
    s2 = MemStore()
    assert cf.cancel_pending(s2, _pending_row(s2), now=NOW, reason="other").kind == "cancelled"


def test_a_changed_target_is_refused_with_the_new_readback():
    s = MemStore()
    new = tl.stop_dry_run({**CARD, "stop": Decimal("4.42")}, Decimal("4.50"), ttl_s=60, now=NOW)

    def execute(p):
        raise tl.TargetChanged(new)

    out = cf.confirm_pending(s, _pending_row(s), now=NOW, execute=execute)
    assert out.kind == "target_changed" and out.new_pending == new
    row = s.get("t-pending")
    assert row["state"] == "failed" and row["failure_class"] == "target_changed"


def test_an_expert_refusal_fails_the_act_loud_and_names_it():
    s = MemStore()

    def execute(p):
        from cobalt.cards import CardStateError

        raise CardStateError("REFUSED: constructed — the stop is not editable in ARMED")

    out = cf.confirm_pending(s, _pending_row(s), now=NOW, execute=execute)
    assert out.kind == "refused" and "not editable" in out.reply
    assert s.get("t-pending")["state"] == "failed" and s.get("t-pending")["failure_class"] == "expert_refused"


class ReapedWhileExecuting(MemStore):
    """The reaper failed the row (`reaped_executing`) while the expert wrote:
    the `EXECUTING → DONE` step finds no `executing` row and returns False."""

    def transition(self, turn_id, expected, new, *, at, **fields):
        if new is TurnState.DONE:
            self.rows[turn_id].update(state="failed", failure_class="reaped_executing")
            return False
        return super().transition(turn_id, expected, new, at=at, **fields)


def test_a_reaped_row_never_reports_done():
    """A5 (voice-v1-check-a-2026-09-24.md FOR THE CLASSIFIER 3; FINAL :170
    [F-15], L1): the stop WAS written, the turn row was reaped mid-way —
    never "Done.", the write named, a RED log line naming the turn."""
    from loguru import logger

    s = ReapedWhileExecuting()
    lines: list[str] = []
    sink = logger.add(lambda m: lines.append(str(m)), level="ERROR")
    try:
        out = cf.confirm_pending(s, _pending_row(s), now=NOW,
                                 execute=lambda p: type("E", (), {"stop_edit_id": 501})())
    finally:
        logger.remove(sink)
    assert out.kind != "done" and out.kind == "failed"
    assert not out.reply.startswith("Done") and "501" in out.reply
    assert "nothing is assumed done" not in out.reply
    assert out.stop_edit_id == 501
    assert any("t-pending" in l and "501" in l for l in lines), lines


def test_x13_confirm_and_cancel_race_in_memory():
    """X-X13 in memory: tap Confirm and a transcript `no` in flight together."""
    for _ in range(50):
        s, calls = MemStore(), []
        row = _pending_row(s)
        barrier = threading.Barrier(2)
        res = {}

        def a():
            barrier.wait()
            res["c"] = cf.confirm_pending(s, row, now=NOW, execute=lambda p: calls.append(1) or type("E", (), {"stop_edit_id": 1})())

        def b():
            barrier.wait()
            res["n"] = cf.cancel_pending(s, row, now=NOW, reason="no")

        ta, tb = threading.Thread(target=a), threading.Thread(target=b)
        ta.start(); tb.start(); ta.join(); tb.join()
        assert len(calls) <= 1
        final = s.get("t-pending")["state"]
        assert final in ("done", "cancelled")
        assert (final == "done") == (len(calls) == 1)
        assert sorted([res["c"].kind, res["n"].kind]) in (["cancelled", "no_pending"], ["done", "no_pending"])


# --- X-X13, WITH-DB: the same race through the REAL store and two connections ------------


@requires_db
def test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both():
    from cobalt.voice.store import VoiceTurnStore

    real = VoiceTurnStore(connect=lambda: RAW_CONNECT(env.DEV_DB_NAME, side=Side.USER))
    sess = f"sess-x13-{uuid.uuid4().hex[:8]}"
    try:
        for n in range(10):
            tid = f"t-{uuid.uuid4().hex[:12]}"
            real.create(turn_id=tid, session_id=sess, source="test", input_kind="text", at=NOW)
            real.transition(tid, {TurnState.RECEIVED}, TurnState.PLANNED, at=NOW)
            p = tl.stop_dry_run(CARD, Decimal("4.50"), ttl_s=3600, now=NOW)
            real.transition(tid, {TurnState.PLANNED}, TurnState.AWAITING_CONFIRM, at=NOW,
                            pending_action=p.model_dump(mode="json"))
            row = real.get(tid)
            calls, res = [], {}
            barrier = threading.Barrier(2)

            def tap():
                barrier.wait()
                res["tap"] = cf.confirm_pending(real, row, now=NOW, execute=lambda p: calls.append(1)
                                                or type("E", (), {"stop_edit_id": 1})())

            def no():
                barrier.wait()
                res["no"] = cf.cancel_pending(real, row, now=NOW, reason="no")

            a, b = threading.Thread(target=tap), threading.Thread(target=no)
            a.start(); b.start(); a.join(); b.join()
            state = real.get(tid)["state"]
            assert len(calls) <= 1, "the stop changed more than once"
            assert state in ("done", "cancelled"), state
            assert (state == "done") == (len(calls) == 1)
    finally:
        real.delete_test_rows(sess)
