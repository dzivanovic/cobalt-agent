"""Seam S1 §2.2 / §2.4 / §4 — `call()` / `call_sync()` over a FAKE server.

The fake is a real HTTP server on 127.0.0.1 (an ephemeral port) that
answers `/v1/chat/completions` with a constructed reply, so the REAL
adapter code path runs end to end with no live model (no live call in
C1 — the live proof is X-E4). Every reply here is constructed (L32).
"""

from __future__ import annotations

import asyncio
import json
import socket
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest
from loguru import logger

from cobalt.modelaccess import (
    ModelCallError,
    ModelMessage,
    ModelRequest,
    call,
    call_sync,
)
from cobalt.modelaccess import client as client_mod
from cobalt.modelaccess.config import ModelAccessConfig, Route


class FakeServer:
    """One configurable reply; records every request body it receives."""

    def __init__(self):
        self.status = 200
        self.body: bytes | None = None
        self.delay = 0.0
        self.requests: list[dict] = []
        outer = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):  # quiet
                pass

            def do_POST(self):
                n = int(self.headers.get("content-length") or 0)
                raw = self.rfile.read(n)
                try:
                    outer.requests.append(json.loads(raw))
                except ValueError:
                    outer.requests.append({"raw": raw.decode(errors="replace")})
                if outer.delay:
                    time.sleep(outer.delay)
                body = outer.body if outer.body is not None else b"{}"
                self.send_response(outer.status)
                self.send_header("content-type", "application/json")
                self.send_header("content-length", str(len(body)))
                self.end_headers()
                try:
                    self.wfile.write(body)
                except OSError:
                    pass

        self.httpd = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.port = self.httpd.server_address[1]
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def reply(self, content, *, model="fake-model-returned", finish="stop", usage=(11, 7), reasoning=None):
        msg = {"role": "assistant", "content": content}
        if reasoning is not None:
            msg["reasoning_content"] = reasoning
        self.body = json.dumps({
            "id": "chatcmpl-constructed", "object": "chat.completion", "created": 1, "model": model,
            "choices": [{"index": 0, "message": msg, "finish_reason": finish}],
            "usage": {"prompt_tokens": usage[0], "completion_tokens": usage[1],
                      "total_tokens": usage[0] + usage[1]},
        }).encode()

    def close(self):
        self.httpd.shutdown()
        self.httpd.server_close()


@pytest.fixture
def server():
    s = FakeServer()
    yield s
    s.close()


def _cfg(port: int, **over) -> ModelAccessConfig:
    r = dict(lane="local", kind="openai_compatible", api_base=f"http://127.0.0.1:{port}/v1",
             model="mainframe", no_think=True, think_policy="forbid_nonempty", timeout_s=5,
             max_output_tokens=64, response_format="json_schema", key_name=None)
    r.update(over)
    return ModelAccessConfig(routes={"local.plan": Route(**r)})


def _req(text="what are my open cards", **over) -> ModelRequest:
    d = dict(route="local.plan", caller="voice.plan", request_id="turn-constructed-1",
             messages=[ModelMessage(role="system", content="constructed system text"),
                       ModelMessage(role="user", content=text)])
    d.update(over)
    return ModelRequest(**d)


# --- happy path ------------------------------------------------------


def test_a_reply_becomes_a_model_result_with_model_as_returned(server):
    server.reply('{"kind":"answer"}')
    r = call_sync(_req(), config=_cfg(server.port))
    assert r.content == '{"kind":"answer"}'
    assert r.model_returned == "fake-model-returned"  # AS RETURNED, never the alias
    assert (r.route, r.caller, r.request_id, r.lane, r.kind) == (
        "local.plan", "voice.plan", "turn-constructed-1", "local", "openai_compatible")
    assert r.think_block == "absent"
    assert r.finish_reason == "stop"
    assert (r.usage.input_tokens, r.usage.output_tokens) == (11, 7)
    assert r.latency_ms >= 0 and r.at.tzinfo is not None


def test_no_think_is_appended_to_the_last_user_message_only(server):
    server.reply("{}")
    call_sync(_req(), config=_cfg(server.port))
    sent = server.requests[-1]["messages"]
    assert sent[-1]["content"].endswith("/no_think")
    assert not sent[0]["content"].endswith("/no_think")
    assert server.requests[-1]["model"] == "mainframe"


def test_no_think_false_sends_the_text_unchanged(server):
    server.reply("{}")
    call_sync(_req(), config=_cfg(server.port, no_think=False))
    assert server.requests[-1]["messages"][-1]["content"] == "what are my open cards"


def test_the_route_budget_is_sent_and_a_caller_may_only_lower_it(server):
    server.reply("{}")
    call_sync(_req(max_output_tokens=10), config=_cfg(server.port))
    assert server.requests[-1]["max_tokens"] == 10
    with pytest.raises(ValueError):
        call_sync(_req(max_output_tokens=1000), config=_cfg(server.port))
    with pytest.raises(ValueError):
        call_sync(_req(timeout_s=999), config=_cfg(server.port))


def test_a_response_schema_rides_as_response_format_when_the_route_says_so(server):
    server.reply("{}")
    schema = {"type": "object", "properties": {"kind": {"type": "string"}}, "required": ["kind"]}
    call_sync(_req(response_schema=schema), config=_cfg(server.port))
    rf = server.requests[-1].get("response_format")
    assert rf and rf["type"] == "json_schema" and rf["json_schema"]["schema"] == schema


def test_a_response_schema_rides_in_the_system_message_otherwise(server):
    server.reply("{}")
    schema = {"type": "object", "properties": {"kind": {"type": "string"}}}
    call_sync(_req(response_schema=schema), config=_cfg(server.port, response_format="in_prompt"))
    body = server.requests[-1]
    assert "response_format" not in body
    assert json.dumps(schema) in body["messages"][0]["content"]


# --- guard (L4 / L41) --------------------------------------------------


SECRET = "sk-" + "Q" * 32  # constructed secret-shaped value (redact.yaml openai_style_key)


def test_a_secret_shaped_message_is_refused_with_zero_calls(server):
    server.reply("{}")
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(text=f"note {SECRET} here"), config=_cfg(server.port))
    assert e.value.kind == "prompt_refused"
    assert SECRET not in str(e.value) and SECRET not in e.value.detail
    assert server.requests == []


def test_a_secret_in_the_system_message_is_refused_too(server):
    server.reply("{}")
    req = _req()
    req.messages[0] = ModelMessage(role="system", content=f"COBALT_DB_PASSWORD={SECRET}")
    with pytest.raises(ModelCallError) as e:
        call_sync(req, config=_cfg(server.port))
    assert e.value.kind == "prompt_refused" and server.requests == []


# --- think policy -------------------------------------------------------


def test_an_empty_think_block_is_removed_and_recorded(server):
    server.reply('<think>\n\n</think>\n{"kind":"answer"}')
    r = call_sync(_req(), config=_cfg(server.port))
    assert r.content == '{"kind":"answer"}' and r.think_block == "empty_removed"


def test_a_nonempty_think_block_is_a_think_leak(server):
    server.reply('<think>x</think>{"kind":"act"}')
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(server.port))
    assert e.value.kind == "think_leak"


def test_an_unclosed_think_block_is_a_think_leak(server):
    server.reply('<think>reasoning that never closes {"kind":"act"}')
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(server.port))
    assert e.value.kind == "think_leak"


def test_nonempty_reasoning_content_is_a_think_leak(server):
    server.reply('{"kind":"act"}', reasoning="constructed hidden reasoning")
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(server.port))
    assert e.value.kind == "think_leak"


# --- every error kind --------------------------------------------------


def test_unknown_route(server):
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(route="cloud.plan"), config=_cfg(server.port))
    assert e.value.kind == "route_unknown" and server.requests == []


def test_unreachable():
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]  # bound, never listening, then closed → refused
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(port))
    assert e.value.kind == "unreachable"


def test_timeout(server):
    server.reply("{}")
    server.delay = 2.0
    t = time.perf_counter()
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(timeout_s=0.5), config=_cfg(server.port))
    assert e.value.kind == "timeout"
    assert time.perf_counter() - t < 1.9, "a timeout must not be retried"
    assert len(server.requests) == 1, "never a retry"


@pytest.mark.parametrize("status", [400, 404, 500, 503])
def test_http_status(server, status):
    server.status = status
    server.body = json.dumps({"error": {"message": f"constructed {status}"}}).encode()
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(server.port))
    assert e.value.kind == "http_status"
    assert str(status) in e.value.detail
    assert len(server.requests) == 1, "never a retry"


def test_bad_response(server):
    server.body = b"this is not json"
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(server.port))
    assert e.value.kind == "bad_response"


@pytest.mark.parametrize("content", ["", "   ", None])
def test_empty(server, content):
    server.reply(content)
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(server.port))
    assert e.value.kind == "empty"


def test_no_choices_is_empty(server):
    """B2 (voice-v1-check-b-2026-09-24.md FOR THE CLASSIFIER 2): seam §2.4 (6)
    "no choices / no content → `empty`" — exactly `empty`."""
    server.body = json.dumps({"id": "x", "object": "chat.completion", "created": 1,
                              "model": "m", "choices": []}).encode()
    with pytest.raises(ModelCallError) as e:
        call_sync(_req(), config=_cfg(server.port))
    assert e.value.kind == "empty"


def test_the_error_kinds_are_exactly_the_seams():
    assert client_mod.ERROR_KINDS == frozenset({
        "route_unknown", "prompt_refused", "unreachable", "timeout", "http_status",
        "bad_response", "empty", "think_leak", "schema_refused"})


# --- the call record (L57) ----------------------------------------------


def test_one_log_line_per_call_carries_no_message_content(server):
    lines: list[str] = []
    sink = logger.add(lambda m: lines.append(str(m)), level="DEBUG")
    try:
        server.reply('{"kind":"answer","say":"constructed reply words"}')
        call_sync(_req(text="constructed utterance words"), config=_cfg(server.port))
        server.status = 500
        server.body = b'{"error":{"message":"x"}}'
        with pytest.raises(ModelCallError):
            call_sync(_req(text="constructed utterance words"), config=_cfg(server.port))
    finally:
        logger.remove(sink)
    records = [l for l in lines if "modelaccess call" in l]
    assert len(records) == 2, lines
    for l in records:
        assert "constructed utterance words" not in l and "constructed reply words" not in l
        assert "route=local.plan" in l and "caller=voice.plan" in l and "request_id=turn-constructed-1" in l
    assert "error=http_status" in records[1]


# --- off the loop (FINAL [F-04]) ----------------------------------------


def test_call_never_blocks_the_event_loop(server):
    server.reply("{}")
    server.delay = 0.6

    async def main():
        ticks = 0

        async def ticker():
            nonlocal ticks
            while True:
                await asyncio.sleep(0.05)
                ticks += 1

        t = asyncio.create_task(ticker())
        r = await call(_req(), config=_cfg(server.port))
        t.cancel()
        return r, ticks

    r, ticks = asyncio.run(main())
    assert r.content == "{}"
    assert ticks >= 6, f"the loop ticked only {ticks} times during a 0.6 s call"


# --- no non-loopback socket during a call --------------------------------


def test_a_call_opens_no_non_loopback_socket(server, monkeypatch):
    attempts = []
    real_connect = socket.socket.connect
    real_gai = socket.getaddrinfo

    def connect(self, addr):
        host = addr[0] if isinstance(addr, tuple) else str(addr)
        if self.family in (socket.AF_INET, socket.AF_INET6) and host not in ("127.0.0.1", "::1", "localhost"):
            attempts.append(host)
            raise OSError("blocked")
        return real_connect(self, addr)

    def gai(host, *a, **k):
        if host not in ("127.0.0.1", "::1", "localhost", None):
            attempts.append(str(host))
            raise socket.gaierror("blocked")
        return real_gai(host, *a, **k)

    monkeypatch.setattr(socket.socket, "connect", connect)
    monkeypatch.setattr(socket, "getaddrinfo", gai)
    server.reply('{"kind":"answer"}')
    call_sync(_req(), config=_cfg(server.port))
    assert attempts == []
