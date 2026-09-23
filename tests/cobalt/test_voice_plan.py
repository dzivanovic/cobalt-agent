"""C3 — the Plan (FINAL §2.4) and the whitelisted prompt builder.

A Plan that does not parse, names a tool outside the allowlist, carries
a span that is not a VERBATIM substring of the transcript, or a
candidate id outside the closed list FAILS the turn loud (`voice_plan`
class) — checked by code, never trusted. The prompt builder takes only
whitelisted fields; a constructed secret-shaped value fed through any
input is refused by the S1 guard before any byte leaves.
"""

from __future__ import annotations

import json
import os
import socket
from pathlib import Path

import pytest
import yaml

from cobalt.modelaccess import ModelResult
from cobalt.modelaccess.config import ModelAccessConfig, Route
from cobalt.voice import agent as ag
from cobalt.voice.models import CardCandidate, HistoryTurn, Plan, PromptInputs
from cobalt.voice.registry import load_agent

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "voice" / "plan-replies.constructed.yaml"
CASES = yaml.safe_load(FIXTURE.read_text())["cases"]
AGENT = load_agent()
SECRET = "sk-" + "Z" * 32  # constructed, secret-shaped (redact.yaml openai_style_key)


def _cand(i: int, ticker="XYZ", direction="long", state="WATCH") -> CardCandidate:
    return CardCandidate(id=f"card-{i}", card_id=i, ticker=ticker, direction=direction, state=state,
                         label=f"{ticker} {direction} {state} (card {i})")


def _inputs(transcript="what are my open cards", **over) -> PromptInputs:
    d = dict(transcript=transcript, history=[], clock="2026-09-03 10:00 ET (Thursday)",
             candidates=[_cand(1)])
    d.update(over)
    return PromptInputs(**d)


@pytest.mark.parametrize("case", CASES, ids=[c["name"] for c in CASES])
def test_plan_validation_over_constructed_replies(case):
    if case["expect"] == "ok":
        plan = ag.validate_plan(case["reply"], case["transcript"], AGENT, set(case["candidates"]))
        assert isinstance(plan, Plan) and plan.kind == case["kind"]
    else:
        with pytest.raises(ag.PlanFailed) as e:
            ag.validate_plan(case["reply"], case["transcript"], AGENT, set(case["candidates"]))
        assert e.value.kind == case["expect"], e.value
        assert e.value.failure_class == "voice_plan"


def test_the_fixture_declares_its_shape():
    assert FIXTURE.read_text().startswith("# SHAPE: constructed")


# --- the prompt builder ----------------------------------------------------


def test_the_prompt_carries_the_whitelisted_fields():
    msgs = ag.build_messages(_inputs(history=[HistoryTurn(transcript="h-said", reply="h-reply")]), AGENT)
    assert [m.role for m in msgs] == ["system", "user"]
    body = json.loads(msgs[1].content)
    assert set(body) == {"clock", "candidates", "history", "transcript"}
    assert body["transcript"] == "what are my open cards"
    assert body["history"] == [{"said": "h-said", "reply": "h-reply"}]
    assert body["candidates"] == [{"id": "card-1", "label": "XYZ long WATCH (card 1)"}]
    sys = msgs[0].content
    for tool in AGENT.tools:
        assert tool in sys
    assert AGENT.charter.strip().splitlines()[0] in sys


def test_no_env_value_path_or_key_name_reaches_the_prompt(monkeypatch, tmp_path):
    marker = "constructed-env-value-7f3a9c"
    monkeypatch.setenv("COBALT_TEST_CONSTRUCTED_SECRET", marker)
    msgs = ag.build_messages(_inputs(), AGENT)
    text = "\n".join(m.content for m in msgs)
    assert marker not in text
    for v in os.environ.values():
        if len(v) >= 12 and "/" in v:
            assert v not in text, "an environment path reached the prompt"
    for forbidden in ("COBALT_", "/Users/", "voice-scratch", "voice-models", ".env", "api_base", "127.0.0.1"):
        assert forbidden not in text, forbidden


def _closed_port_cfg() -> ModelAccessConfig:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    return ModelAccessConfig(routes={"local.plan": Route(
        lane="local", kind="openai_compatible", api_base=f"http://127.0.0.1:{port}/v1", model="m",
        no_think=True, think_policy="forbid_nonempty", timeout_s=2, max_output_tokens=64,
        response_format="json_schema", key_name=None)})


@pytest.mark.parametrize("where", ["transcript", "history_said", "history_reply", "candidate_label", "clock"])
def test_a_secret_through_any_input_is_refused_by_the_s1_guard(where):
    inp = _inputs()
    if where == "transcript":
        inp = _inputs(transcript=f"move the stop {SECRET}")
    elif where == "history_said":
        inp = _inputs(history=[HistoryTurn(transcript=f"said {SECRET}", reply="ok")])
    elif where == "history_reply":
        inp = _inputs(history=[HistoryTurn(transcript="said", reply=f"reply {SECRET}")])
    elif where == "candidate_label":
        c = _cand(1)
        c.label = f"XYZ {SECRET}"
        inp = _inputs(candidates=[c])
    elif where == "clock":
        inp = _inputs(clock=f"now {SECRET}")
    with pytest.raises(ag.PlanFailed) as e:
        ag.plan_turn(inp, agent=AGENT, turn_id="t-constructed", config=_closed_port_cfg())
    assert e.value.kind == "prompt_refused"
    assert SECRET not in str(e.value)


# --- ONE call per turn, through the module ---------------------------------


def _result(content: str) -> ModelResult:
    from datetime import datetime, timezone

    from cobalt.modelaccess.models import Usage

    return ModelResult(route="local.plan", caller="voice.plan", request_id="t", lane="local",
                       kind="openai_compatible", model_returned="m-returned", content=content,
                       think_block="absent", finish_reason="stop", usage=Usage(input_tokens=1, output_tokens=1),
                       latency_ms=5, at=datetime.now(timezone.utc))


def test_plan_turn_makes_exactly_one_call_on_the_registry_route(monkeypatch):
    calls = []

    def fake(req, config=None):
        calls.append(req)
        return _result('{"kind": "answer", "tool": "cards.open", "args": {}, "say": null}')

    monkeypatch.setattr(ag, "call_sync", fake)
    out = ag.plan_turn(_inputs(), agent=AGENT, turn_id="t-1")
    assert len(calls) == 1
    assert calls[0].route == AGENT.route and calls[0].caller == "voice.plan" and calls[0].request_id == "t-1"
    assert calls[0].response_schema == ag.PLAN_SCHEMA
    assert out.plan.kind == "answer" and out.result.model_returned == "m-returned"


def test_a_bad_reply_fails_after_one_call_never_a_retry(monkeypatch):
    calls = []

    def fake(req, config=None):
        calls.append(req)
        return _result("not json")

    monkeypatch.setattr(ag, "call_sync", fake)
    with pytest.raises(ag.PlanFailed) as e:
        ag.plan_turn(_inputs(), agent=AGENT, turn_id="t-2")
    assert e.value.kind == "plan_parse" and len(calls) == 1
    assert e.value.result is not None  # the raw call is kept as a stored input


def test_a_model_call_error_becomes_a_voice_plan_failure(monkeypatch):
    from cobalt.modelaccess import ModelCallError

    def fake(req, config=None):
        raise ModelCallError("unreachable", route="local.plan", caller="voice.plan", request_id="t", detail="x")

    monkeypatch.setattr(ag, "call_sync", fake)
    with pytest.raises(ag.PlanFailed) as e:
        ag.plan_turn(_inputs(), agent=AGENT, turn_id="t-3")
    assert e.value.kind == "unreachable" and e.value.failure_class == "voice_plan"


def test_the_plan_schema_names_every_allowlisted_tool():
    tools = ag.PLAN_SCHEMA["properties"]["tool"]["enum"]
    assert set(t for t in tools if t) == set(AGENT.tools)
