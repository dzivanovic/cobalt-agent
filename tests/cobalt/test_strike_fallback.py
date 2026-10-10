"""S4-P2 S4 (offline): the phone fallback is the sheet's OWN tail.

No stream generator is ever started in this file: the fallback reads the
seam rows itself, creates the S3 row, and DMs a trigger nobody was shown
once `dm_after_s` has passed since the seam row's `at`. A fake row source
and record store (the real one's semantics: one upsert that fills only a
NULL column; a claim on `dm_at IS NULL AND shown_at IS NULL`), a fake
`send_dm` and a fake clock. Constructed values only (L32).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

UTC = timezone.utc
T0 = datetime(2001, 1, 2, 15, 0, 5, tzinfo=UTC)
TEXT = "ZZFB LONG · key B · 120 sh · stop 4.80 · HALF-B-LONG"


def _row(tid, *, via="strike.detector", to_state="TRIGGERED", at=T0):
    from cobalt.aset.strike import SeamRow

    return SeamRow(transition_id=tid, card_id=9, to_state=to_state, actor="cobalt", at=at,
                   evidence={"via": via, "policy": "close_through", "entry": "5.10",
                             "bar_close_at": "2001-01-02T15:00:00+00:00", "seen_at": "2001-01-02T15:00:03+00:00"},
                   ticker="ZZFB", direction="long", sized_grade="B", shares=120, stop=Decimal("4.80"),
                   sheet_mode="half")


class FakeStore:
    def __init__(self, rows):
        self.rows = list(rows)
        self.records: dict[int, dict] = {}

    def seam_rows(self, after_id, day):
        return [r for r in self.rows if after_id is None or r.transition_id > after_id]

    def upsert(self, transition_id, *, seam_at, pushed_at=None, shown_at=None):
        rec = self.records.setdefault(transition_id, {"seam_at": None, "pushed_at": None, "shown_at": None,
                                                      "dm_at": None, "dm_result": None})
        for key, value in (("seam_at", seam_at), ("pushed_at", pushed_at), ("shown_at", shown_at)):
            if rec[key] is None:
                rec[key] = value
        return dict(rec)

    def claim_dm(self, transition_id, now):
        rec = self.records.get(transition_id)
        if rec is None or rec["dm_at"] is not None or rec["shown_at"] is not None:
            return False
        rec["dm_at"] = now
        return True

    def record_dm_result(self, transition_id, result):
        self.records[transition_id]["dm_result"] = result


class Sender:
    def __init__(self, fail=None):
        self.calls: list[str] = []
        self.fail = fail

    def __call__(self, text):
        from cobalt.notify.result import SendResult

        self.calls.append(text)
        if self.fail:
            raise self.fail
        return SendResult(True, "post constructed-id to @constructed", ref="constructed-id")


def _tail(store, send, clock):
    from cobalt.aset.strike import FallbackTail
    from cobalt.strike.delivery_config import DeliverySettings

    return FallbackTail(store=store, send=send, settings=DeliverySettings(dm_after_s=10), now=lambda: clock[0])


def test_no_stream_ever_connected_the_tail_dms_at_dm_after_s_and_not_a_second_before():
    store, send, clock = FakeStore([_row(5)]), Sender(), [T0]
    tail = _tail(store, send, clock)
    tail.pass_once()
    assert store.records[5]["seam_at"] == T0, "the tail itself creates the S3 row"
    clock[0] = T0 + timedelta(seconds=9)
    tail.pass_once()
    assert send.calls == []
    clock[0] = T0 + timedelta(seconds=10)
    tail.pass_once()
    assert send.calls == [TEXT]
    assert store.records[5]["dm_at"] == clock[0]
    assert store.records[5]["dm_result"] == "DM sent — post constructed-id to @constructed"
    assert store.records[5]["pushed_at"] is None


def test_an_ack_before_dm_after_s_sends_nothing():
    store, send, clock = FakeStore([_row(5)]), Sender(), [T0]
    tail = _tail(store, send, clock)
    tail.pass_once()
    store.upsert(5, seam_at=T0, shown_at=T0 + timedelta(seconds=2))
    clock[0] = T0 + timedelta(seconds=30)
    tail.pass_once()
    assert send.calls == []


def test_two_passes_and_a_restarted_tail_still_send_one_dm():
    store, send, clock = FakeStore([_row(5)]), Sender(), [T0 + timedelta(seconds=11)]
    _tail(store, send, clock).pass_once()
    tail = _tail(store, send, clock)
    tail.pass_once()
    tail.pass_once()
    assert send.calls == [TEXT]


def test_a_send_that_raises_is_recorded_and_never_raised():
    store, clock = FakeStore([_row(5)]), [T0 + timedelta(seconds=10)]
    send = Sender(fail=RuntimeError("mattermost unreachable"))
    _tail(store, send, clock).pass_once()
    assert store.records[5]["dm_result"] == "DM FAILED — RuntimeError: mattermost unreachable"
    assert store.records[5]["dm_at"] is not None


def test_a_disabled_channel_is_recorded_as_its_result():
    from cobalt.notify.result import SendResult

    store, clock = FakeStore([_row(5)]), [T0 + timedelta(seconds=10)]
    _tail(store, lambda text: SendResult(False, "channel disabled in configs/cobalt/notify.yaml"), clock).pass_once()
    assert store.records[5]["dm_result"] == "DM NOT sent — channel disabled in configs/cobalt/notify.yaml"


def test_a_missed_row_never_dms():
    store, send, clock = FakeStore([_row(6, via="strike.missed", to_state="MISSED")]), Sender(), [T0]
    tail = _tail(store, send, clock)
    clock[0] = T0 + timedelta(hours=1)
    tail.pass_once()
    assert send.calls == []


def test_a_failed_upsert_is_read_again_next_pass():
    class Flaky(FakeStore):
        broken = True

        def upsert(self, transition_id, **kw):
            if self.broken:
                raise RuntimeError("database down")
            return super().upsert(transition_id, **kw)

    store, send, clock = Flaky([_row(5)]), Sender(), [T0 + timedelta(seconds=10)]
    tail = _tail(store, send, clock)
    with pytest.raises(RuntimeError):
        tail.pass_once()
    store.broken = False
    tail.pass_once()
    assert send.calls == [TEXT]


def test_check_o2_a_seam_row_committed_after_a_higher_id_is_still_dmd():
    """X1: the tail's cursor must not skip a lower id that becomes visible late."""

    class LateCommit(FakeStore):
        reads = 0

        def seam_rows(self, after_id, day):
            self.reads += 1
            visible = [_row(52, via="panel.triggered")]
            if self.reads > 1:
                visible = [_row(51)] + visible
            return [r for r in visible if after_id is None or r.transition_id > after_id]

    store, send, clock = LateCommit([]), Sender(), [T0 + timedelta(seconds=10)]
    tail = _tail(store, send, clock)
    tail.pass_once()
    tail.pass_once()
    assert send.calls == [TEXT]


def test_a_transient_result_write_failure_is_retried_without_sending_twice():
    class FlakyResultStore(FakeStore):
        result_writes = 0

        def record_dm_result(self, transition_id, result):
            self.result_writes += 1
            if self.result_writes == 1:
                raise RuntimeError("database down")
            super().record_dm_result(transition_id, result)

    store = FlakyResultStore([_row(5)])
    send = Sender()
    clock = [T0 + timedelta(seconds=10)]
    tail = _tail(store, send, clock)

    with pytest.raises(RuntimeError, match="database down"):
        tail.pass_once()
    tail.pass_once()

    assert send.calls == [TEXT]
    assert store.records[5]["dm_result"] == "DM sent — post constructed-id to @constructed"


def test_the_thread_logs_a_failed_pass_and_goes_on():
    from cobalt.aset.strike import FallbackThread

    class Tail:
        def __init__(self):
            self.n = 0

        def pass_once(self):
            self.n += 1
            if self.n == 1:
                raise RuntimeError("one bad pass")
            if self.n >= 3:
                thread.stop()

    tail = Tail()
    thread = FallbackThread(tail, interval_s=0.001)
    thread.start()
    thread.join(timeout=5)
    assert not thread.is_alive() and tail.n >= 3
    assert thread.daemon
