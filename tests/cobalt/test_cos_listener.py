"""F20 C3d — the listener and the resident loop (FINAL §2 `cos/listener.py`, §5, F-20, F-31; L2, L18).

A real-shape, redacted, constructed Mattermost posts response (L45, L32):
`fixtures/cos/dm-posts.redacted.json`. The session, the turn store and the
kill switch are faked; nothing reaches Mattermost, the SDK or a database.
"""

from __future__ import annotations

import json
import threading
import time
from pathlib import Path
from types import SimpleNamespace

import pytest

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "cos" / "dm-posts.redacted.json"
HUMAN = "cnstrctdhuman0000000000000"
BOT = "cnstrctdbot000000000000000"


class FakeTurns:
    def __init__(self):
        self.events: list[tuple] = []
        self.rows: dict[int, dict] = {}
        self.refs: set[str] = set()

    def insert_turn(self, message_ref):
        if message_ref in self.refs:
            import psycopg

            raise psycopg.errors.UniqueViolation("constructed duplicate")
        self.refs.add(message_ref)
        turn = len(self.rows) + 1
        self.rows[turn] = {"state": "pending", "message_ref": message_ref}
        self.events.append(("insert", message_ref))
        return turn

    def set_turn(self, turn, state, **fields):
        self.rows[turn].update(state=state, **fields)
        self.events.append(("set", turn, state))


def _post(message, *, post_id="cnstrctdpost00000000000009", user=HUMAN):
    from cobalt.cos.listener import Post

    return Post(id=post_id, user_id=user, message=message, create_at=1756908009000)


@pytest.fixture
def rig(monkeypatch):
    from cobalt.cos import listener as listener_mod

    turns = FakeTurns()
    ran: list[str] = []
    engaged: list[str] = []
    replies: list[str] = []

    def run_turn(text):
        turns.events.append(("session", text))
        ran.append(text)
        return SimpleNamespace(ok=True, reply="constructed reply", error=None, num_turns=1,
                               result_subtype="success", is_error=False, terminal_reason="completed")

    payload = json.loads(FIXTURE.read_text())
    listener = listener_mod.Listener(
        fetch=lambda since: (payload, BOT), store=turns, run_turn=run_turn, reply=replies.append,
        engage=lambda phrase: engaged.append(phrase),
    )
    return listener, turns, ran, engaged, replies


def test_kill_phrase_is_intercepted_before_the_session(rig):
    listener, turns, ran, engaged, _ = rig
    assert listener.handle(_post("  cobalt stop ")) == "killed"
    assert engaged and ran == [] and turns.events == [], "no turn row, no session"


def test_resume_phrase_is_a_plain_turn_and_no_listener_resumes(rig):
    listener, _turns, ran, engaged, _ = rig
    assert listener.handle(_post("COBALT RESUME")) == "done"
    assert ran == ["COBALT RESUME"] and engaged == []
    src = Path(__file__).resolve().parents[2] / "src" / "cobalt" / "cos"
    for path in src.glob("*.py"):
        text = path.read_text()
        assert "matches_resume_phrase" not in text and "killswitch.clear" not in text, path.name


def test_approve_text_changes_no_hitl_row(rig, monkeypatch):
    from cobalt.hitl import store as hitl_store

    def refuse(*a, **k):
        raise AssertionError("the listener touched the HITL store")

    monkeypatch.setattr(hitl_store, "HitlStore", refuse)
    listener, _turns, ran, _engaged, replies = rig
    out = listener.poll()
    assert out == ["done", "own", "done"], "the bot's own card post is skipped"
    assert ran == ["what is on the radar", "approve a1b2c3d4"], "an approve text is a turn"
    assert replies == ["constructed reply", "constructed reply"]


def test_one_pending_row_per_post_before_the_session(rig):
    listener, turns, _ran, _engaged, _ = rig
    listener.handle(_post("constructed question"))
    assert turns.events[:2] == [("insert", "cnstrctdpost00000000000009"), ("set", 1, "running")]
    assert turns.events[2] == ("session", "constructed question")
    assert turns.events[3] == ("set", 1, "done")
    assert listener.handle(_post("constructed question")) == "duplicate"
    assert len(turns.rows) == 1


def test_hung_poll_stops_the_beat():
    from cobalt.cos.run import Loop

    beats: list[float] = []
    release = threading.Event()
    stop = threading.Event()
    store = SimpleNamespace(beat=lambda label: beats.append(time.monotonic()))
    calls = {"n": 0}

    def poll():
        calls["n"] += 1
        if calls["n"] == 2:
            release.wait(5)

    loop = Loop(store=store, poll=poll, steps=[], keep_running=lambda: not stop.is_set(),
                poll_interval_s=0.01)
    thread = threading.Thread(target=loop.run, daemon=True)
    thread.start()
    time.sleep(0.3)
    assert len(beats) == 2, "one beat per iteration; the blocked iteration stamps nothing more"
    release.set()
    stop.set()
    thread.join(2)
    assert not thread.is_alive()


def test_refuses_while_agent_pidfile_alive(tmp_path):
    import os

    from cobalt.cos.run import CosRefused, refuse_if_agent_alive
    from cobalt.jobs.config import load_job_registry

    spec = load_job_registry().spec("com.cobalt.agent")
    live = tmp_path / "live.pid"
    live.write_text(f"{os.getpid()}\n")
    with pytest.raises(CosRefused, match="com.cobalt.agent"):
        refuse_if_agent_alive(spec.model_copy(update={"pidfile": str(live)}))
    stale = tmp_path / "stale.pid"
    stale.write_text("999999\n")
    refuse_if_agent_alive(spec.model_copy(update={"pidfile": str(stale)}))
    refuse_if_agent_alive(spec.model_copy(update={"pidfile": str(tmp_path / "absent.pid")}))


# ---------------------------------------------------------------------
# check (CHECK-HUB ## 4) — findings run as written
# ---------------------------------------------------------------------


def test_check_o2_a_failed_turn_posts_its_partial_reply():
    from cobalt.cos.listener import Listener

    turns, replies = FakeTurns(), []
    out = SimpleNamespace(ok=False, reply="constructed partial", error="turn stopped at max turns (2)",
                          num_turns=None, result_subtype=None, is_error=None, terminal_reason=None)
    listener = Listener(fetch=lambda since: ({}, BOT), store=turns, run_turn=lambda text: out,
                        reply=replies.append, engage=lambda phrase: None, is_kill=lambda text: False)
    assert listener.handle(_post("constructed question")) == "failed"
    assert replies == ["constructed partial"]


def test_check_o3_no_session_after_the_kill_phrase_in_the_same_poll():
    from cobalt.cos.listener import Listener

    turns, ran, engaged = FakeTurns(), [], []
    payload = {"order": ["cnstrctdpost00000000000k01", "cnstrctdpost00000000000k02"], "posts": {
        "cnstrctdpost00000000000k01": {"id": "cnstrctdpost00000000000k01", "user_id": HUMAN,
                                       "message": "cobalt stop", "create_at": 1756908001000},
        "cnstrctdpost00000000000k02": {"id": "cnstrctdpost00000000000k02", "user_id": HUMAN,
                                       "message": "constructed question", "create_at": 1756908002000}}}
    done = SimpleNamespace(ok=True, reply="", error=None, num_turns=1, result_subtype="success",
                           is_error=False, terminal_reason="completed")
    listener = Listener(fetch=lambda since: (payload, BOT), store=turns,
                        run_turn=lambda text: ran.append(text) or done, reply=lambda t: None,
                        engage=engaged.append)
    listener.poll()
    assert engaged and ran == [], "no session opens after the kill phrase"


def test_check_o4_a_turn_that_raises_is_marked_failed():
    from cobalt.cos.listener import Listener

    turns = FakeTurns()

    def boom(text):
        raise RuntimeError("constructed")

    listener = Listener(fetch=lambda since: ({}, BOT), store=turns, run_turn=boom,
                        reply=lambda t: None, engage=lambda p: None, is_kill=lambda t: False)
    try:
        listener.handle(_post("constructed question"))
    except RuntimeError:
        pass
    assert turns.rows[1]["state"] == "failed"


def test_a_raising_session_marks_the_turn_failed():
    from cobalt.cos.listener import Listener

    turns = FakeTurns()

    def run_turn(_text):
        raise RuntimeError("constructed session died")

    listener = Listener(
        fetch=lambda since: ({}, BOT), store=turns, run_turn=run_turn,
        reply=lambda _t: None, engage=lambda _p: None,
    )
    with pytest.raises(RuntimeError, match="constructed session died"):
        listener.handle(_post("constructed question"))
    assert turns.rows[1]["state"] == "failed"


def test_the_scratch_dir_is_empty_when_the_session_opens(tmp_path, monkeypatch):
    from cobalt.cos import run as run_mod

    scratch = tmp_path / "scratch"
    scratch.mkdir()
    (scratch / "planted.txt").write_text("constructed")
    monkeypatch.setattr(run_mod, "SCRATCH_DIR", scratch)
    monkeypatch.setattr("cobalt.cos.session.tunable_int", lambda key: 30)

    def stop():
        raise RuntimeError("stop after mkdir")

    monkeypatch.setattr("cobalt.cos.store.CosStore", stop)
    with pytest.raises(RuntimeError, match="stop after mkdir"):
        run_mod._build(object())
    assert list(scratch.iterdir()) == []


# ---------------------------------------------------------------------
# fix round W (card 730 row W) — G7
# ---------------------------------------------------------------------


class RecordingJobStore:
    """The store calls `job_run` makes, recorded; `kill_switch` is the is_active read."""

    def __init__(self, *, killed=False):
        self.calls: list[tuple] = []
        self.killed = killed

    def _rec(self, name, args, kwargs):
        self.calls.append((name, args, dict(kwargs)))

    def ensure_schema(self, *a, **k):
        self._rec("ensure_schema", a, k)

    def register(self, *a, **k):
        self._rec("register", a, k)

    def mark_running(self, *a, **k):
        self._rec("mark_running", a, k)

    def mark_finished(self, *a, **k):
        self._rec("mark_finished", a, k)

    def mark_wrapper_finished(self, *a, **k):
        self._rec("mark_wrapper_finished", a, k)

    def beat(self, *a, **k):
        self._rec("beat", a, k)

    def kill_switch(self, *a, **k):
        self._rec("kill_switch", a, k)
        return {"active": self.killed, "phrase": "constructed" if self.killed else None,
                "set_by": "constructed" if self.killed else None, "set_at": None}


def _fields(calls, *, defaults=None):
    """Each call by field: method, label, every keyword; `error` by its first
    line, `result` present-or-None only. `defaults` fills a keyword the call
    left to its default (`job_run`'s `allow_prod=False`)."""
    rows = []
    for name, args, kwargs in calls:
        kwargs = {**(defaults or {}).get(name, {}), **kwargs}
        first = args[0] if args else None
        row = {"method": name, "label": getattr(first, "label", first)}
        for key, value in kwargs.items():
            if key == "error":
                value = value.splitlines()[0] if value else value
            elif key == "result":
                value = "present-or-None"
            row[key] = value
        rows.append(row)
    return rows


def _run_both(monkeypatch, *, killed=False, body_error=None):
    from cobalt.cos import run as run_mod
    from cobalt.jobs import store as store_mod
    from cobalt.jobs import wrapper

    # job_run first, with the real _Beater: the reference.
    ref = RecordingJobStore(killed=killed)
    ref_exc = None
    try:
        with wrapper.job_run("com.cobalt.cos", store=ref):
            if body_error is not None:
                raise body_error
    except BaseException as e:  # noqa: BLE001
        ref_exc = e

    class NoBeater:
        def __init__(self, *a, **k):
            raise AssertionError("main created a _Beater")

    monkeypatch.setattr(wrapper, "_Beater", NoBeater)
    got = RecordingJobStore(killed=killed)
    monkeypatch.setattr(store_mod, "JobStore", lambda: got)
    monkeypatch.setattr(run_mod, "refuse_if_agent_alive", lambda *a, **k: None)
    monkeypatch.setattr(run_mod, "_build", lambda job_store: (SimpleNamespace(poll=lambda: None), [], 1))

    def loop_run(self):
        if body_error is not None:
            raise body_error

    monkeypatch.setattr(run_mod.Loop, "run", loop_run)
    got_exc = None
    try:
        run_mod.main([])
    except BaseException as e:  # noqa: BLE001
        got_exc = e
    return ref, ref_exc, got, got_exc


#: `job_run`'s default the `main` side is read with (`job_run(allow_prod=False)`).
_JOB_RUN_DEFAULTS = {"ensure_schema": {"allow_prod": False}, "register": {"allow_prod": False}}


@pytest.mark.parametrize("case", ["clean", "raising", "killed"])
def test_cos_run_writes_the_wrappers_start_and_finish_rows_and_no_beater(monkeypatch, case):
    from cobalt.jobs.wrapper import JobStopped

    body_error = RuntimeError("constructed body failure") if case == "raising" else None
    ref, ref_exc, got, got_exc = _run_both(monkeypatch, killed=case == "killed", body_error=body_error)
    assert _fields(got.calls, defaults=_JOB_RUN_DEFAULTS) == _fields(ref.calls), (ref.calls, got.calls)
    if case == "clean":
        assert ref_exc is None and got_exc is None
    elif case == "raising":
        assert ref_exc is body_error and got_exc is body_error
    else:
        assert isinstance(ref_exc, JobStopped) and isinstance(got_exc, JobStopped)
        assert "mark_running" not in [c[0] for c in got.calls + ref.calls]
