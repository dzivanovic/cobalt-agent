# source: reports/f21-x8-probe-2026-10-18.md (X8 unloaded: 200, JIT load, no error body)
"""F21 chunk 2 (card 469 V2; FINAL F-01, F-14): `embed_sync()` over a FAKE server.

The fake is a real HTTP server on 127.0.0.1 (an ephemeral port) answering
`/v1/embeddings` with a constructed body, so the REAL adapter path runs end
to end with no live model. A failure raises `ModelCallError` and returns
nothing: no zero vector, no `None`, no `[]` (F-14, D5). There is no
not-loaded cell: a never-loaded model JIT-loads and answers 200 (the source
line above), so the not-loaded exit is the timeout and the non-2xx tests.
Every vector and model name here is constructed (L32).
"""

from __future__ import annotations

import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

from cobalt.modelaccess import ModelCallError, embed_sync
from cobalt.modelaccess.config import EmbedRoute, ModelAccessConfig, Route

MODEL = "constructed-embed-model"
DIM = 8


class FakeServer:
    """One configurable reply; records every request body it receives."""

    def __init__(self):
        self.status = 200
        self.body: bytes | None = None
        self.delay = 0.0
        self.requests: list[tuple[str, dict]] = []
        outer = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):  # quiet
                pass

            def do_POST(self):
                n = int(self.headers.get("content-length") or 0)
                raw = self.rfile.read(n)
                try:
                    outer.requests.append((self.path, json.loads(raw)))
                except ValueError:
                    outer.requests.append((self.path, {"raw": raw.decode(errors="replace")}))
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

    def vector(self, vec, *, model=MODEL):
        self.body = json.dumps({
            "object": "list", "model": model,
            "data": [{"object": "embedding", "index": 0, "embedding": vec}],
            "usage": {"prompt_tokens": 5, "total_tokens": 5},
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
    e = dict(lane="local", kind="openai_embeddings", api_base=f"http://127.0.0.1:{port}/v1",
             model=MODEL, timeout_s=5, dim=DIM, key_name=None)
    e.update(over)
    plan = Route(lane="local", kind="openai_compatible", api_base=f"http://127.0.0.1:{port}/v1",
                 model="mainframe", no_think=True, think_policy="forbid_nonempty", timeout_s=5,
                 max_output_tokens=64, response_format="json_schema", key_name=None)
    return ModelAccessConfig(routes={"local.plan": plan, "local.embed": EmbedRoute(**e)})


GOOD = [0.125, -0.25, 0.5, 0.0, 1.0, -1.0, 0.0625, 0.75]


def test_a_good_vector_returns_model_returned_and_dim(server):
    server.vector(GOOD)
    r = embed_sync("local.embed", "a synthetic paragraph", caller="genesis.embed", config=_cfg(server.port))
    assert r.vector == GOOD and r.dim == DIM == len(r.vector)
    assert (r.route, r.model_returned) == ("local.embed", MODEL)
    assert r.latency_ms >= 0 and r.request_id
    path, sent = server.requests[-1]
    assert path == "/v1/embeddings"
    assert (sent["model"], sent["input"]) == (MODEL, "a synthetic paragraph")


@pytest.mark.parametrize("vec", [GOOD[:-1], GOOD + [0.5], [], [0.0] * DIM],
                         ids=["short", "long", "empty", "zero"])
def test_a_wrong_length_vector_raises(server, vec):
    server.vector(vec)
    with pytest.raises(ModelCallError) as e:
        embed_sync("local.embed", "a synthetic paragraph", caller="genesis.embed", config=_cfg(server.port))
    assert e.value.kind == "bad_response"


def test_a_timeout_raises(server):
    server.vector(GOOD)
    server.delay = 2.0
    with pytest.raises(ModelCallError) as e:
        embed_sync("local.embed", "a synthetic paragraph", caller="genesis.embed",
                   config=_cfg(server.port, timeout_s=0.3))
    assert e.value.kind == "timeout"


@pytest.mark.parametrize("status,body", [
    (500, b'{"error": "constructed"}'),
    (404, b'{"error": {"message": "model not loaded"}}'),
    (503, b"not json at all"),
    (400, b""),
])
def test_a_non_2xx_any_body_raises(server, status, body):
    server.status, server.body = status, body
    with pytest.raises(ModelCallError) as e:
        embed_sync("local.embed", "a synthetic paragraph", caller="genesis.embed", config=_cfg(server.port))
    assert e.value.kind == "http_status"


def test_a_model_returned_other_than_the_route_model_raises(server):
    # X8: an unknown alias answered 200 with ANOTHER model's vector.
    server.vector(GOOD, model="some-other-model")
    with pytest.raises(ModelCallError) as e:
        embed_sync("local.embed", "a synthetic paragraph", caller="genesis.embed", config=_cfg(server.port))
    assert e.value.kind == "bad_response" and "some-other-model" in str(e.value)


def test_a_chat_route_is_not_an_embed_route_and_the_reverse(server):
    server.vector(GOOD)
    cfg = _cfg(server.port)
    with pytest.raises(ModelCallError) as e:
        embed_sync("local.plan", "a synthetic paragraph", caller="genesis.embed", config=cfg)
    assert e.value.kind == "route_unknown"
    from cobalt.modelaccess import ModelMessage, ModelRequest, call_sync

    req = ModelRequest(route="local.embed", caller="voice.plan", request_id="turn-constructed-1",
                       messages=[ModelMessage(role="user", content="constructed")])
    with pytest.raises(ModelCallError) as e:
        call_sync(req, config=cfg)
    assert e.value.kind == "route_unknown"
    assert server.requests == []
