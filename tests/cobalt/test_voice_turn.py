"""C11 — THE turn function `run_turn` (FINAL [F-01]): one function, three
callers (the route, the CLI, these tests). Every dependency is injected;
here they are constructed fakes, an in-memory store with the same
single-flight contract, and synthesized bytes (never a recording).

Also the C4 lifecycle cases the prompt names through the real turn: the
scratch file is unlinked on success, on a transcribe failure, on a Plan
failure and on an exception in between, and the row's `audio_deleted_at`
is set.
"""

from __future__ import annotations

import threading
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from typing import Any

import pytest

from cobalt.modelaccess.models import ModelResult, Usage
from cobalt.voice import agent as ag
from cobalt.voice import tools as tl
from cobalt.voice import turn as tn
from cobalt.voice.models import Plan, TurnState
from cobalt.voice.registry import load_agent
from cobalt.voice.transcribe import SttDown, Transcript

NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
AGENT = load_agent()
CARDS = [
    {"id": 11, "ticker": "XYZ", "direction": "long", "state": "WATCH", "entry": Decimal("4.6000"),
     "stop": Decimal("4.4000"), "shares": 250, "grade": "B"},
    {"id": 12, "ticker": "QRS", "direction": "short", "state": "FILLED", "entry": Decimal("12.2000"),
     "stop": Decimal("12.6000"), "shares": 100, "grade": "A"},
]


class MemStore:
    def __init__(self):
        self.rows: dict[str, dict[str, Any]] = {}
        self.order: list[str] = []
        self.lock = threading.Lock()
        self.reaped = 0

    def create(self, *, turn_id, session_id, source, input_kind, at, confirm_of=None):
        self.rows[turn_id] = {"turn_id": turn_id, "session_id": session_id, "source": source,
                              "input_kind": input_kind, "state": "received", "confirm_of": confirm_of,
                              "received_at": at}
        self.order.append(turn_id)

    def update(self, turn_id, **fields):
        self.rows[turn_id].update(fields)

    def transition(self, turn_id, expected, new, *, at, **fields):
        with self.lock:
            row = self.rows.get(turn_id)
            if row is None or row["state"] not in {s.value for s in expected}:
                return False
            row.update(fields, state=new.value)
            row[f"{new.value}_at"] = at
            return True

    def get(self, turn_id):
        return self.rows.get(turn_id)

    def pending_for_session(self, session_id):
        live = [self.rows[t] for t in self.order
                if self.rows[t]["session_id"] == session_id and self.rows[t]["state"] == "awaiting_confirm"]
        return live[-1] if live else None

    def history(self, session_id, limit):
        done = [(r["transcript"], r["reply"]) for r in (self.rows[t] for t in self.order)
                if r["session_id"] == session_id and r.get("transcript") and r.get("reply")]
        return done[-limit:] if limit else []

    def reap(self, *, now, limits):
        self.reaped += 1
        return []

    def expire_pending(self, *, now):
        return []


def _result(content: str) -> ModelResult:
    return ModelResult(route="local.plan", caller="voice.plan", request_id="t", lane="local",
                       kind="openai_compatible", model_returned="m-returned", content=content,
                       think_block="absent", finish_reason="stop", usage=Usage(input_tokens=5, output_tokens=6),
                       latency_ms=7, at=NOW)


class FakePlanner:
    """Maps a transcript to a constructed Plan; records every call."""

    def __init__(self, plans: dict[str, Plan] | None = None, fail: str | None = None):
        self.plans = plans or {}
        self.fail = fail
        self.calls: list[Any] = []

    def __call__(self, inputs, *, agent, turn_id):
        self.calls.append(inputs)
        if self.fail:
            raise ag.PlanFailed(self.fail, "constructed failure")
        plan = self.plans.get(inputs.transcript)
        if plan is None:
            plan = Plan(kind="unsupported")
        return ag.PlanOutcome(plan=plan, result=_result(plan.model_dump_json()))


class FakeTranscriber:
    def __init__(self, text="what are my open cards", fail: str | None = None):
        self.text, self.fail, self.paths = text, fail, []

    def transcribe(self, path: Path) -> Transcript:
        self.paths.append(path)
        assert path.exists(), "the file must exist while it is transcribed"
        if self.fail:
            raise SttDown(self.fail)
        return Transcript(text=self.text, language="en", duration_s=1.2, no_speech_prob=[0.01],
                          avg_logprob=[-0.2], engine="faster-whisper", model="tiny.en", revision="0" * 40,
                          stt_ms=12)


@pytest.fixture
def deps(tmp_path, monkeypatch):
    from cobalt.voice import config as vc

    monkeypatch.setenv(vc.SCRATCH_ENV, str(tmp_path / "scratch"))
    monkeypatch.setenv(vc.MODEL_ENV, str(tmp_path / "models"))
    cfg = vc.load_voice_config()
    executed = []

    def execute(p):
        executed.append(p)
        return type("E", (), {"stop_edit_id": 777})()

    d = tn.TurnDeps(cfg=cfg, agent=AGENT, store=MemStore(), transcriber=FakeTranscriber(),
                    plan=FakePlanner(), read_cards=lambda: list(CARDS),
                    read_pool=lambda: {"pool": {"current": [{"ticker": "XYZ", "position": 1}], "stale": False}},
                    execute=execute, now=lambda: NOW, plan_timeout_s=15, probe_duration=lambda p: 1.2)
    d.executed = executed
    return d


def _text(text, session="sess-a", **kw):
    return tn.TurnInput(session_id=session, source="test", text=text, **kw)


def _audio(session="sess-a", data=b"\x1aE\xdf\xa3synthesized-webm-bytes", **kw):
    return tn.TurnInput(session_id=session, source="test", audio=data, content_type="audio/webm;codecs=opus", **kw)


def _scratch_files(d):
    return [p for p in Path(d.cfg.scratch_dir).glob("*") if p.name != ".lock"] if Path(d.cfg.scratch_dir).exists() else []


READ_OPEN = Plan(kind="answer", tool="cards.open")
STOP_ACT = Plan(kind="act", tool="cards.set_stop",
                args={"card": {"span": "XYZ"}, "stop": {"span": "4.50"}})


# --- reads ---------------------------------------------------------------------------


def test_a_text_read_is_answered_by_the_template(deps):
    deps.plan = FakePlanner({"what are my open cards": READ_OPEN})
    out = tn.run_turn(_text("what are my open cards"), deps)
    assert out.state is TurnState.DONE
    assert out.reply.startswith("You have 2 open cards: XYZ long, WATCH, stop 4.40")
    row = deps.store.get(out.turn_id)
    assert row["transcript"] == "what are my open cards" and row["plan"]["tool"] == "cards.open"
    assert row["model_returned"] == "m-returned" and row["plan_route"] == "local.plan"
    assert len(deps.plan.calls) == 1 and deps.store.reaped == 1


def test_history_comes_from_this_sessions_rows(deps):
    deps.plan = FakePlanner({"what are my open cards": READ_OPEN})
    tn.run_turn(_text("what are my open cards"), deps)
    tn.run_turn(_text("what are my open cards"), deps)
    tn.run_turn(_text("what are my open cards", session="sess-b"), deps)
    assert [h.transcript for h in deps.plan.calls[1].history] == ["what are my open cards"]
    assert deps.plan.calls[2].history == []


def test_radar_pool_read(deps):
    deps.plan = FakePlanner({"what is on radar": Plan(kind="answer", tool="radar.pool")})
    assert tn.run_turn(_text("what is on radar"), deps).reply == "Radar pool: 1 name — XYZ."


def test_card_numbers_read_needs_one_card(deps):
    deps.plan = FakePlanner({"numbers on QRS": Plan(kind="answer", tool="cards.numbers", args={"card": {"span": "QRS"}})})
    out = tn.run_turn(_text("numbers on QRS"), deps)
    assert out.reply.startswith("QRS short, card 12, FILLED")


# --- audio lifecycle through the real turn -----------------------------------------------


def test_an_audio_turn_unlinks_its_file_and_records_only_metadata(deps):
    deps.plan = FakePlanner({"what are my open cards": READ_OPEN})
    out = tn.run_turn(_audio(), deps)
    assert out.state is TurnState.DONE and out.transcript == "what are my open cards"
    assert _scratch_files(deps) == []
    row = deps.store.get(out.turn_id)
    assert row["audio_deleted_at"] is not None and row["audio_bytes"] == len(b"\x1aE\xdf\xa3synthesized-webm-bytes")
    assert len(row["audio_sha256"]) == 64 and row["audio_duration_ms"] == 1200
    assert row["stt_engine"] == "faster-whisper" and row["stt_ms"] == 12
    assert not any(isinstance(v, (bytes, bytearray)) for v in row.values())


def test_a_transcribe_failure_unlinks_and_fails_loud(deps):
    deps.transcriber = FakeTranscriber(fail="model_missing")
    out = tn.run_turn(_audio(), deps)
    assert out.state is TurnState.FAILED and out.reply == "speech-to-text down (model missing)"
    assert any(l.level == "red" for l in out.degraded)
    assert _scratch_files(deps) == [] and deps.plan.calls == []
    row = deps.store.get(out.turn_id)
    assert row["failure_class"] == "voice_stt" and row["audio_deleted_at"] is not None


def test_a_plan_failure_unlinks_and_fails_loud(deps):
    deps.plan = FakePlanner(fail="unreachable")
    out = tn.run_turn(_audio(), deps)
    assert out.state is TurnState.FAILED and "Cobalt can't think right now (unreachable)" in out.reply
    assert _scratch_files(deps) == []
    assert deps.store.get(out.turn_id)["failure_class"] == "voice_plan"


def test_an_exception_in_between_unlinks_and_fails_loud(deps):
    def boom():
        raise RuntimeError("constructed failure")

    deps.read_cards = boom
    out = tn.run_turn(_audio(), deps)
    assert out.state is TurnState.FAILED and _scratch_files(deps) == []
    assert deps.store.get(out.turn_id)["failure_class"] in ("turn_error", "tool_read")


def test_an_empty_transcript_is_i_heard_nothing(deps):
    deps.transcriber = FakeTranscriber(text="   ")
    out = tn.run_turn(_audio(), deps)
    assert out.state is TurnState.FAILED and out.reply == "I heard nothing."
    assert deps.plan.calls == [] and deps.store.get(out.turn_id)["failure_class"] == "empty_transcript"


def test_a_clip_too_long_is_refused_before_decode(deps):
    deps.probe_duration = lambda p: 45.0
    out = tn.run_turn(_audio(), deps)
    assert out.state is TurnState.FAILED and "too long" in out.reply
    assert deps.transcriber.paths == [] and _scratch_files(deps) == []


# --- the act and its confirmation --------------------------------------------------------


def _pending_act(deps, session="sess-a"):
    deps.plan = FakePlanner({"move the stop on XYZ to 4.50": STOP_ACT})
    out = tn.run_turn(_text("move the stop on XYZ to 4.50", session=session), deps)
    assert out.state is TurnState.AWAITING_CONFIRM and out.pending_turn_id == out.turn_id
    assert out.readback == "Stop on XYZ long, card 11: from 4.40 to 4.50. Say yes, or tap Confirm."
    assert deps.executed == []
    return out


def test_an_act_reads_back_and_waits(deps):
    _pending_act(deps)


def test_yes_confirms_with_no_model_call_and_executes_once(deps):
    act = _pending_act(deps)
    calls = len(deps.plan.calls)
    out = tn.run_turn(_text("Yes."), deps)
    assert len(deps.plan.calls) == calls, "a confirm turn makes NO model call"
    assert out.state is TurnState.DONE and out.reply.startswith("Done.")
    assert len(deps.executed) == 1
    pend = deps.store.get(act.turn_id)
    assert pend["state"] == "done" and pend["expert_write_id"] == 777
    assert deps.store.get(out.turn_id)["confirm_of"] == act.turn_id


def test_no_cancels(deps):
    act = _pending_act(deps)
    out = tn.run_turn(_text("no"), deps)
    assert out.reply == "Cancelled. Nothing was changed." and deps.executed == []
    assert deps.store.get(act.turn_id)["state"] == "cancelled"


def test_any_other_transcript_ends_the_pending_action_and_is_not_planned(deps):
    act = _pending_act(deps)
    calls = len(deps.plan.calls)
    out = tn.run_turn(_text("what are my open cards"), deps)
    assert len(deps.plan.calls) == calls and deps.executed == []
    assert deps.store.get(act.turn_id)["state"] == "cancelled"
    assert "nothing was changed" in out.reply


def test_a_confirm_word_inside_the_request_does_not_execute(deps):
    text = "yes move the stop on XYZ to 4.50"
    deps.plan = FakePlanner({text: Plan(kind="act", tool="cards.set_stop",
                                        args={"card": {"span": "XYZ"}, "stop": {"span": "4.50"}})})
    out = tn.run_turn(_text(text), deps)
    assert out.state is TurnState.AWAITING_CONFIRM and deps.executed == []


def test_a_tap_confirms(deps):
    act = _pending_act(deps)
    out = tn.run_turn(tn.TurnInput(session_id="sess-a", source="test", tap="confirm", pending_turn_id=act.turn_id), deps)
    assert out.state is TurnState.DONE and len(deps.executed) == 1


def test_a_tap_from_another_session_is_refused(deps):
    act = _pending_act(deps)
    out = tn.run_turn(tn.TurnInput(session_id="sess-z", source="test", tap="confirm", pending_turn_id=act.turn_id), deps)
    assert deps.executed == [] and "no pending" in out.reply.lower()


def test_a_pending_action_past_its_ttl_executes_nothing(deps):
    act = _pending_act(deps)
    later = NOW + timedelta(seconds=deps.cfg.confirm_ttl_s + 1)
    deps.now = lambda: later
    calls = len(deps.plan.calls)
    out = tn.run_turn(_text("yes"), deps)
    assert deps.executed == [] and len(deps.plan.calls) == calls
    assert deps.store.get(act.turn_id)["state"] == "expired" and "expired" in out.reply


def test_a_changed_target_reads_the_new_change_back_for_reconfirmation(deps):
    act = _pending_act(deps)
    new = tl.stop_dry_run({**CARDS[0], "stop": Decimal("4.42")}, Decimal("4.50"), ttl_s=60, now=NOW)

    def execute(p):
        raise tl.TargetChanged(new)

    deps.execute = execute
    out = tn.run_turn(_text("yes"), deps)
    assert out.state is TurnState.AWAITING_CONFIRM and "from 4.42 to 4.50" in out.reply
    assert deps.store.get(act.turn_id)["failure_class"] == "target_changed"
    assert out.pending_turn_id == out.turn_id


def test_x5_guard_and_unparseable_values_clarify(deps):
    for text, span in (("move the stop on XYZ to 450", "450"), ("move the stop on XYZ to four fifty", "four fifty")):
        deps.plan = FakePlanner({text: Plan(kind="act", tool="cards.set_stop",
                                            args={"card": {"span": "XYZ"}, "stop": {"span": span}})})
        out = tn.run_turn(_text(text, session=f"sess-{span[:3]}"), deps)
        assert out.state is TurnState.DONE and out.pending_turn_id is None and deps.executed == []


@pytest.mark.parametrize("transcript,span,stop", [
    ("Move the stock to 450.", "450", "4.40"),
    ("Move the stop to 1225.", "1225", "12.30"),
    ("Move the stop to 975.", "975", "9.80"),
])
def test_x5_measured_wrong_value_shapes_clarify(deps, transcript, span, stop):
    """X5 (desk R41; build report `### X-X5`; FINAL :88 §2.6 read-back + §7
    "unparseable value → clarify"; L45 real SHAPE): X-X5's three wrong-value
    transcript shapes as the engine returned them (synthetic TTS of
    constructed sentences) against a constructed card → clarify naming what
    was heard; no pending action, nothing executed."""
    deps.read_cards = lambda: [{**CARDS[0], "stop": Decimal(stop)}]
    deps.plan = FakePlanner({transcript: Plan(kind="act", tool="cards.set_stop",
                                              args={"card": {"span": "XYZ"}, "stop": {"span": span}})})
    out = tn.run_turn(_text(transcript), deps)
    assert out.state is TurnState.DONE and out.pending_turn_id is None and deps.executed == []
    assert span in out.reply and "point" in out.reply
    row = deps.store.get(out.turn_id)
    assert row["resolution"]["clarify"] == "value_guard" and row["resolution"]["heard"] == span


def test_an_ambiguous_card_clarifies(deps):
    deps.read_cards = lambda: [CARDS[0], {**CARDS[0], "id": 13, "direction": "short"}]
    deps.plan = FakePlanner({"move the stop on XYZ to 4.50": STOP_ACT})
    out = tn.run_turn(_text("move the stop on XYZ to 4.50"), deps)
    assert out.pending_turn_id is None and "Which XYZ card?" in out.reply


# --- refusals --------------------------------------------------------------------------


def test_an_order_is_refused_whatever_the_plan(deps):
    deps.plan = FakePlanner({"buy 100 XYZ": STOP_ACT})
    out = tn.run_turn(_text("buy 100 XYZ"), deps)
    assert out.reply == tl.REFUSE_SENTENCE and deps.executed == [] and out.pending_turn_id is None


def test_trading_logic_is_unsupported_and_the_row_says_so(deps):
    out = tn.run_turn(_text("set my max risk to 200"), deps)
    assert out.state is TurnState.UNSUPPORTED and "cobalt settings load" in out.reply
    assert deps.store.get(out.turn_id)["state"] == "unsupported"


def test_anything_else_is_unsupported(deps):
    out = tn.run_turn(_text("write me a poem"), deps)
    assert out.state is TurnState.UNSUPPORTED and out.reply == tl.UNSUPPORTED_SENTENCE


# --- dry run -----------------------------------------------------------------------------


def test_dry_run_prints_the_change_and_writes_nothing(deps):
    deps.plan = FakePlanner({"move the stop on XYZ to 4.50": STOP_ACT})
    out = tn.run_turn(_text("move the stop on XYZ to 4.50", dry_run=True), deps)
    assert deps.store.rows == {} and deps.executed == []
    assert out.dry_run["plan"]["tool"] == "cards.set_stop"
    assert out.dry_run["resolution"]["card_id"] == 11
    assert out.dry_run["change"]["from_stop"] == "4.40" and out.dry_run["change"]["to_stop"] == "4.50"


def test_run_turn_is_the_one_turn_function(deps, monkeypatch):
    """D10 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 10): behavioural —
    the `run_turn` name the web route uses is called once, with the widget's
    source, for a text turn POSTed from loopback."""
    import inspect

    from fastapi.testclient import TestClient

    from cobalt.aset import web as aset_web
    from cobalt.voice import web

    assert "run_turn" in inspect.getsource(web)  # the CLI caller is pinned in C13's tests
    calls = []

    def recording(inp, d):
        calls.append(inp)
        return tn.run_turn(inp, deps)

    monkeypatch.setattr(web, "run_turn", recording)
    monkeypatch.setattr(web, "get_config", lambda: deps.cfg)
    monkeypatch.setattr(web, "get_deps", lambda: deps)
    deps.plan = FakePlanner({"what are my open cards": READ_OPEN})
    r = TestClient(aset_web.app, client=("127.0.0.1", 51000)).post(
        "/voice/turn", data={"session": "sess-web10", "text": "what are my open cards"})
    assert r.status_code == 200, r.text
    assert len(calls) == 1 and calls[0].source == "widget"
