"""S4-P2 S1 + S2 (offline): the strike stream and the pinned tab.

A fake row source stands in for `StrikeAlertStore`; time is a fake
monotonic clock advanced by a fake sleep, so every keepalive is counted,
never waited for. Tickers, prices and dates are constructed (L32).
"""

from __future__ import annotations

import asyncio
import json
import re
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from fastapi.testclient import TestClient

UTC = timezone.utc
AT = datetime(2001, 1, 2, 15, 0, 5, tzinfo=UTC)


def _row(tid, *, card_id=7, via="strike.detector", actor="cobalt", to_state="TRIGGERED", ticker="ZZST",
         direction="long", grade="B", shares=120, stop=Decimal("4.80"), mode="half", at=AT):
    from cobalt.aset.strike import SeamRow

    evidence = {"via": via, "policy": "close_through", "entry": "5.10", "cross_price": "5.12",
                "bar_ts": "2001-01-02T14:59:00+00:00", "bar_close_at": "2001-01-02T15:00:00+00:00",
                "seen_at": "2001-01-02T15:00:03+00:00", "cadence_s": 2, "def_md5": "a" * 32,
                "card_def_md5": "a" * 32}
    return SeamRow(transition_id=tid, card_id=card_id, to_state=to_state, actor=actor, at=at, evidence=evidence,
                   ticker=ticker, direction=direction, sized_grade=grade, shares=shares, stop=stop,
                   sheet_mode=mode)


class FakeStore:
    """`seam_rows(after_id, day)`: rows with id > after_id, or every row of the day."""

    def __init__(self, rows):
        self.rows = list(rows)
        self.reads: list = []
        self.pushed: list = []

    def seam_rows(self, after_id, day):
        from cobalt.session.clock import ET

        self.reads.append((after_id, day))
        if after_id is None:
            # As `StrikeAlertStore.seam_rows`: a fresh connect reads the rows of ET `day` only.
            return [r for r in self.rows if r.at.astimezone(ET).date() == day]
        return [r for r in self.rows if r.transition_id > after_id]

    def upsert(self, transition_id, *, seam_at, pushed_at=None, shown_at=None):
        self.pushed.append((transition_id, seam_at, pushed_at, shown_at))
        return {"transition_id": transition_id}


class FakeTime:
    def __init__(self):
        self.t = 0.0

    def monotonic(self):
        return self.t

    async def sleep(self, seconds):
        self.t += seconds


def _deps(store, *, keepalive_s=15, polls=1):
    from cobalt.aset.strike import StreamDeps
    from cobalt.strike.delivery_config import DeliverySettings

    clock = FakeTime()
    count = {"n": 0}

    def stop():
        count["n"] += 1
        return count["n"] > polls

    deps = StreamDeps(store=store, settings=DeliverySettings(keepalive_s=keepalive_s), now=lambda: AT,
                      monotonic=clock.monotonic, sleep=clock.sleep, stop=stop)
    return deps, clock


def _collect(deps, *, last_event_id=None):
    from cobalt.aset.strike import event_stream

    async def run():
        async def stop():
            return deps.stop()

        return [chunk async for chunk in event_stream(deps, last_event_id=last_event_id, stop=stop)]

    return asyncio.run(run())


def _data(chunk):
    return json.loads(re.search(r"^data: (.*)$", chunk, re.M).group(1))


# ---------------------------------------------------------------------
# S1 — the stream
# ---------------------------------------------------------------------


def test_the_seam_via_values_are_p1s_own():
    from cobalt.aset import strike
    from cobalt.strike import detector

    assert strike.VIA_TRIGGERED == detector.VIA_TRIGGERED
    assert strike.VIA_MISSED == detector.VIA_MISSED


def test_two_seam_rows_are_two_events_with_exact_ids_and_json():
    store = FakeStore([_row(11), _row(12, card_id=8, via="strike.missed", to_state="MISSED", ticker="ZZSU",
                                      direction="short", grade=None, shares=None, stop=None, mode=None)])
    deps, _ = _deps(store)
    chunks = _collect(deps)
    assert len(chunks) == 2
    assert chunks[0].startswith("id: 11\nevent: trigger\ndata: ") and chunks[0].endswith("\n\n")
    assert chunks[1].startswith("id: 12\nevent: missed\ndata: ")
    assert _data(chunks[0]) == {
        "transition_id": 11, "card_id": 7, "ticker": "ZZST", "direction": "long", "key": "B", "shares": 120,
        "stop": "4.80", "hotkey": "HALF-B-LONG", "entry": "5.10", "bar_close_at": "2001-01-02T15:00:00+00:00",
        "seen_at": "2001-01-02T15:00:03+00:00", "at": "2001-01-02T15:00:05+00:00",
    }
    assert _data(chunks[1])["hotkey"] == "n/a — unsized"
    assert [p[0] for p in store.pushed] == [11, 12], "each send upserts its S3 row"
    assert all(p[1] == AT and p[2] == AT for p in store.pushed), "seam_at = the row's at, pushed_at = now"


def test_a_fresh_connect_reads_todays_rows_and_last_event_id_resumes_after_it():
    store = FakeStore([_row(11), _row(12)])
    deps, _ = _deps(store)
    chunks = _collect(deps, last_event_id=11)
    assert [c.split("\n")[0] for c in chunks] == ["id: 12"]
    assert store.reads[0][0] == 11

    fresh = FakeStore([_row(10, at=AT - timedelta(days=1)), _row(11)])
    deps, _ = _deps(fresh)
    chunks = _collect(deps)
    assert fresh.reads[0] == (None, AT.date()), "a fresh connect starts at today's ET date"
    assert [c.split("\n")[0] for c in chunks] == ["id: 11"], "yesterday's row is not sent on a fresh connect"


def test_his_own_tap_and_any_other_actor_send_no_event():
    store = FakeStore([
        _row(21, via="panel.triggered", actor="you"),
        _row(22, via="strike.detector", actor="you"),
        _row(23, via="strike.detector", to_state="FILLED"),
        _row(24),
    ])
    deps, _ = _deps(store)
    chunks = _collect(deps)
    assert [c.split("\n")[0] for c in chunks] == ["id: 24"]


def test_check_o1_a_seam_row_committed_after_a_higher_id_still_reaches_the_stream():
    """X1: a lower id that becomes visible after a higher one was read (two writers, one sequence)."""

    class LateCommit(FakeStore):
        def seam_rows(self, after_id, day):
            self.reads.append((after_id, day))
            visible = [_row(52, via="panel.triggered", actor="you")]
            if len(self.reads) > 1:
                visible = [_row(51)] + visible
            return [r for r in visible if after_id is None or r.transition_id > after_id]

    deps, _ = _deps(LateCommit([]), polls=2)
    chunks = _collect(deps)
    assert any(c.startswith("id: 51\n") for c in chunks), chunks


def test_a_keepalive_is_sent_after_keepalive_s_with_no_rows():
    deps, clock = _deps(FakeStore([]), keepalive_s=15, polls=40)
    chunks = _collect(deps)
    beats = [c for c in chunks if c.startswith(":")]
    assert len(beats) == 1, chunks
    assert beats[0].startswith(": keepalive ") and "\nevent: keepalive\n" in beats[0]
    # stream_tail_ms 500: 30 polls of silence reach 15 s, not one fewer.
    deps, _ = _deps(FakeStore([]), keepalive_s=15, polls=30)
    assert not _collect(deps)


def test_a_failed_read_sends_no_keepalive_so_the_tab_goes_loud():
    class Broken(FakeStore):
        def seam_rows(self, after_id, day):
            raise RuntimeError("database down")

    deps, _ = _deps(Broken([]), keepalive_s=15, polls=40)
    assert _collect(deps) == []


def test_the_route_streams_text_event_stream():
    from cobalt.aset import strike, web

    deps, _ = _deps(FakeStore([_row(31)]))
    web.app.dependency_overrides[strike.get_stream_deps] = lambda: deps
    try:
        response = TestClient(web.app).get("/strike/stream")
    finally:
        web.app.dependency_overrides.clear()
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/event-stream")
    assert response.text.startswith("id: 31\nevent: trigger\n")


def test_a_malformed_last_event_id_is_refused():
    from cobalt.aset import strike, web

    deps, _ = _deps(FakeStore([]))
    web.app.dependency_overrides[strike.get_stream_deps] = lambda: deps
    try:
        response = TestClient(web.app).get("/strike/stream", headers={"Last-Event-ID": "x1"})
    finally:
        web.app.dependency_overrides.clear()
    assert response.status_code == 400


# ---------------------------------------------------------------------
# S2 — the pinned tab
# ---------------------------------------------------------------------


def _page():
    from cobalt.aset.strike import render_strike_page
    from cobalt.strike.delivery_config import DeliverySettings

    return render_strike_page(DeliverySettings())


def test_the_offline_row_source_drops_a_row_from_another_day():
    from datetime import date

    store = FakeStore([_row(11)])
    assert store.seam_rows(None, date(2001, 1, 3)) == []


def test_the_page_is_served_apart_from_radar():
    from cobalt.aset import web

    response = TestClient(web.app).get("/strike")
    assert response.status_code == 200
    assert "new EventSource('/strike/stream')" in response.text


def test_the_page_holds_the_stream_the_permission_the_sound_and_the_loud_states():
    page = _page()
    for needle in ("new EventSource('/strike/stream')", "Notification.requestPermission", "isSecureContext",
                   "AudioContext", "STREAM DOWN · since ", "NOTIFICATIONS OFF — ", "SOUND LOCKED — press ARM",
                   "/strike/ack", 'id="arm"'):
        assert needle in page, needle
    assert "setInterval(refreshLadder" not in page and "/radar" not in page.replace('href="/radar"', "")


def test_a_sample_alert_holds_exactly_the_four_labelled_values_and_its_title():
    from cobalt.aset.strike import alert_html, alert_values, event_payload
    from cobalt.strike.delivery_config import DeliverySettings

    alert = alert_html(alert_values(event_payload(_row(41), DeliverySettings())))
    assert re.findall(r"<dt>([^<]*)</dt>", alert) == ["key", "shares", "stop", "hotkey"]
    assert re.findall(r"<dd[^>]*>([^<]*)</dd>", alert) == ["B", "120", "4.80", "HALF-B-LONG"]
    assert ">ZZST LONG<" in alert
    for word in ("entry", "target", "why", "5.10"):
        assert word not in alert.lower(), word
