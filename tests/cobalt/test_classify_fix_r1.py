"""JEV fix round 1 (L75) — one test group per FIX row, each RED on the
unfixed code before its fix (report `jev-fix-r1-build-2026-09-23.md`).

ALL OFFLINE: a CONSTRUCTED fake key, a recording transport, and — for F2
only — two LOOPBACK servers on 127.0.0.1 (the `test_sheet_daymode_probe.py`
shape). Every assertion about the key asserts it is ABSENT from the named
place. The shapes (`fake_vault`, `cfg`, `RecordingTransport`) are copied
from `test_classify_keys.py` / `test_classify_door.py`, never imported.
"""

from __future__ import annotations

import json
import shutil
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest
from loguru import logger

from cobalt.classify import collector as col
from cobalt.classify.collector import (
    KEY_NAME,
    ClassifyError,
    OpenRouterClassifier,
)
from cobalt.classify.config import load_trial_config
from cobalt.redact.secrets import LiteralGuard

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "classify"
ENTRY = FIXTURES / "openrouter-model-entry.real-shape.json"
RESPONSE = FIXTURES / "openrouter-systemone-response.openapi-example.json"

FAKE_KEY = "sk-or-v1-TESTONLY-" + "0123456789abcdef" * 2
PRICING = json.loads(ENTRY.read_text())["data"]["endpoints"][0]["pricing"]


class RecordingTransport:
    """Records (method, url, headers, body); answers with a canned reply."""

    def __init__(self, status: int = 200, body: bytes = b"{}"):
        self.calls: list[dict] = []
        self.status, self.body = status, body

    def __call__(self, method, url, headers, body, timeout):
        self.calls.append({"method": method, "url": url, "headers": dict(headers), "body": body})
        return self.status, self.body


@pytest.fixture
def fake_vault(monkeypatch):
    """The vault holds the fake key; the literal guard is ACTIVE with it."""
    monkeypatch.setattr(
        "cobalt.redact.secrets.read_secret",
        lambda name: FAKE_KEY if name == KEY_NAME else None,
    )
    monkeypatch.setattr(
        "cobalt.redact.guard.load_literals",
        lambda *a, **k: LiteralGuard({KEY_NAME: FAKE_KEY}, available=True),
    )
    return FAKE_KEY


@pytest.fixture
def log_capture():
    lines: list[str] = []
    sink = logger.add(lambda m: lines.append(str(m)), level="DEBUG")
    yield lines
    logger.remove(sink)


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    from cobalt.classify import config as cfg_mod

    monkeypatch.setattr(cfg_mod, "REPO_ROOT", tmp_path)
    c = load_trial_config()
    c = c.model_copy(update={"spend_ledger": str(tmp_path / "scratch" / "classify-spend.jsonl"), "carried_spend": []})
    dest = tmp_path / c.entry_record
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, dest)
    return c


def _floor(cfg):
    qset, items = cfg.resolve("FLOOR")
    return qset, items[0]


def _clf(cfg, transport, **kw):
    return OpenRouterClassifier(cfg, transport=transport, pricing=PRICING, **kw)


# -- F1: the raw body of a non-200 is guarded WHOLE before it is returned -------

TAIL_BODY = b"x" * 2100 + f" Bearer {FAKE_KEY}".encode()


def test_f1_a_non_json_500_with_the_key_past_byte_2000_is_refused(cfg, fake_vault):
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(500, TAIL_BODY))
    with pytest.raises(ClassifyError, match="not written") as excinfo:
        clf._classify(qset, item)
    assert FAKE_KEY not in str(excinfo.value)


def test_f1_a_502_json_with_the_key_in_an_earlier_duplicate_is_refused(cfg, fake_vault):
    qset, item = _floor(cfg)
    body = b'{"error": "echo ' + FAKE_KEY.encode() + b'", "error": "x"}'
    clf = _clf(cfg, RecordingTransport(502, body))
    with pytest.raises(ClassifyError, match="not written") as excinfo:
        clf._classify(qset, item)
    assert FAKE_KEY not in str(excinfo.value)


@pytest.fixture
def probe_env(cfg, tmp_path, monkeypatch):
    from cobalt.classify import cli as ccli

    monkeypatch.setattr(ccli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(ccli, "load_trial_config", lambda: cfg)

    def install(transport):
        monkeypatch.setattr(col, "urllib_transport", transport)
        return transport

    class A:
        out = "scratch/probe-20260923T120000.json"

    return ccli, A, install, tmp_path


def test_f1_the_probe_writes_neither_file_for_a_500_holding_the_key(probe_env, fake_vault):
    ccli, A, install, root = probe_env
    install(RecordingTransport(500, TAIL_BODY))
    with pytest.raises(ClassifyError, match="not written") as excinfo:
        ccli.cmd_probe(A())
    assert FAKE_KEY not in str(excinfo.value)
    assert not (root / "scratch" / "probe-20260923T120000.json").exists()
    assert not (root / "scratch" / "probe-20260923T120000.raw.json").exists()


# -- F2: the transport never follows a redirect --------------------------------
#
# Two LOOPBACK servers (the `test_sheet_daymode_probe.py` shape): A answers
# every request with a 3xx pointing at B; B records whatever reaches it.


def _serve(handler_cls):
    server = HTTPServer(("127.0.0.1", 0), handler_cls)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server


@pytest.fixture
def redirect_pair():
    """`start(code)` -> (A url base, B's recorded requests); torn down after."""
    servers: list[HTTPServer] = []

    def start(code: int):
        landed: list[dict] = []

        class B(BaseHTTPRequestHandler):
            def _record(self):
                n = int(self.headers.get("Content-Length") or 0)
                if n:
                    self.rfile.read(n)
                landed.append({"method": self.command, "path": self.path,
                               "headers": dict(self.headers.items())})
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", "2")
                self.end_headers()
                self.wfile.write(b"{}")

            do_GET = do_POST = do_HEAD = _record  # noqa: N815

            def log_message(self, *a):
                pass

        b = _serve(B)
        servers.append(b)
        location = f"http://127.0.0.1:{b.server_port}/landed"

        class A(BaseHTTPRequestHandler):
            def _redirect(self):
                n = int(self.headers.get("Content-Length") or 0)
                if n:
                    self.rfile.read(n)
                self.send_response(code)
                self.send_header("Location", location)
                self.send_header("Content-Length", "0")
                self.end_headers()

            do_GET = do_POST = do_HEAD = _redirect  # noqa: N815

            def log_message(self, *a):
                pass

        a = _serve(A)
        servers.append(a)
        return f"http://127.0.0.1:{a.server_port}", landed

    yield start
    for s in servers:
        s.shutdown()
        s.server_close()


@pytest.mark.parametrize("code", [301, 302, 303, 307, 308])
def test_f2_a_keyed_post_redirect_is_not_followed(redirect_pair, code):
    base, landed = redirect_pair(code)
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {FAKE_KEY}"}
    status, _ = col.urllib_transport("POST", f"{base}/api/v1/systemone", headers, b"{}", 5.0)
    assert landed == [], f"HTTP {code}: the redirect reached server B: {landed}"
    assert status == code


def test_f2_a_keyless_get_is_not_followed_either(redirect_pair):
    base, landed = redirect_pair(302)
    status, _ = col.urllib_transport("GET", f"{base}/api/v1/models",
                                     {"Accept": "application/json"}, None, 5.0)
    assert landed == []
    assert status == 302


# -- F3: the response `id` never reaches the ledger unguarded ----------------------

def _example() -> dict:
    """The committed response fixture, read fresh (never edited on disk)."""
    return json.loads(RESPONSE.read_text())


def test_f3_a_response_id_holding_the_key_never_reaches_the_ledger(cfg, fake_vault):
    fx = _example()
    fx["id"] = "gen-" + FAKE_KEY
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    with pytest.raises(ClassifyError, match="not written") as excinfo:
        clf._classify(qset, item)
    assert FAKE_KEY not in str(excinfo.value)
    assert clf.ledger.path.exists()
    assert clf.ledger.calls() == 1                      # the paid call is still counted
    assert FAKE_KEY not in clf.ledger.path.read_text()


# -- F4: every POST that came back is one ledger line -------------------------------
#
# A call that came back with no cost is booked at its OWN projection, marked
# `projected` — never 0 (L1), never a guessed bill.

def test_f4_a_429_is_one_projected_ledger_line(cfg, fake_vault):
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(429, b'{"error":{"code":429}}'))
    rec = clf.classify(qset, item)
    assert rec.status == "http_error"
    assert clf.ledger.calls() == 1
    (line,) = clf.ledger.entries()
    assert line["cost_source"] == "projected"
    assert line["cost_usd"] == rec.projected_usd
    assert line["cost_usd"] > 0


def test_f4_a_200_without_usage_is_one_projected_ledger_line(cfg, fake_vault):
    fx = _example()
    del fx["usage"]
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    rec = clf.classify(qset, item)
    assert rec.status == "invalid"
    assert clf.ledger.calls() == 1
    (line,) = clf.ledger.entries()
    assert line["cost_source"] == "projected"
    assert line["cost_usd"] == rec.projected_usd


def test_f4_a_401_is_one_projected_ledger_line_without_the_key(cfg, fake_vault):
    from cobalt.classify.collector import ClassifyAuthError

    echo = json.dumps({"error": {"message": f"bad key {FAKE_KEY}"}}).encode()
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(401, echo))
    with pytest.raises(ClassifyAuthError):
        clf.classify(qset, item)
    assert clf.ledger.calls() == 1
    assert clf.ledger.entries()[0]["cost_source"] == "projected"
    assert FAKE_KEY not in clf.ledger.path.read_text()


def test_f4_the_call_ceiling_sees_a_call_that_came_back_with_no_cost(cfg, fake_vault, tmp_path):
    from cobalt.classify.ledger import Ledger

    led = Ledger(tmp_path / "ceiling" / "classify-spend.jsonl", cap_usd=5, call_ceiling=1)
    t = RecordingTransport(429, b'{"error":{"code":429}}')
    clf = OpenRouterClassifier(cfg, transport=t, ledger=led, pricing=PRICING)
    qset, item = _floor(cfg)
    clf.classify(qset, item)
    with pytest.raises(ClassifyError, match="ceiling"):
        clf.classify(qset, item)
    assert len(t.calls) == 1


# -- F5: a negative cost never lowers the total ------------------------------------

def test_f5_a_negative_returned_cost_is_computed_from_tokens_instead(cfg, fake_vault, log_capture):
    fx = _example()
    fx["usage"]["cost"] = -1.0
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    rec = clf.classify(qset, item)
    u = fx["usage"]
    expected = u["input_tokens"] * float(PRICING["prompt"]) + u["output_tokens"] * float(PRICING["completion"])
    assert rec.cost_source == "computed"
    assert rec.cost_usd == pytest.approx(expected)
    assert clf.ledger.spent() >= 0
    negatives = [ln for ln in log_capture if "ERROR" in ln and "negative" in ln]
    assert len(negatives) == 1


@pytest.mark.parametrize("bad", [-0.5, float("nan")], ids=["negative", "nan"])
def test_f5_the_ledger_refuses_a_negative_or_non_finite_cost(tmp_path, bad):
    from cobalt.classify.ledger import Ledger

    led = Ledger(tmp_path / "scratch" / "classify-spend.jsonl", cap_usd=5, call_ceiling=10)
    with pytest.raises(ClassifyError):
        led.record("x", bad, "returned")
    assert not led.path.exists()
