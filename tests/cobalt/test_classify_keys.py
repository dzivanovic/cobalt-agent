"""R2 — the key, the guards, the ledger. ALL CONSTRUCTED; no network.

The key here is a CONSTRUCTED fake (`sk-or-v1-TESTONLY-<32 hex>`), handed
to the collector by monkeypatching `read_secret` — the one vault reader
(L3). The literal half of F19 is made ACTIVE with that same fake value,
which is what the real vault gives a keyed run. The transport records
every request it is handed and never touches a socket.
"""

from __future__ import annotations

import json
import traceback

import pytest
from loguru import logger

from cobalt.classify import collector as col
from cobalt.classify.collector import KEY_NAME, ClassifyError, OpenRouterClassifier
from cobalt.classify.config import load_trial_config
from cobalt.classify.ledger import Ledger
from cobalt.redact.secrets import LiteralGuard, VaultAccessError

FAKE_KEY = "sk-or-v1-TESTONLY-" + "0123456789abcdef" * 2


class RecordingTransport:
    """Records (method, url, headers, body); answers with a canned reply."""

    def __init__(self, status: int = 200, body: bytes = b"{}"):
        self.calls: list[dict] = []
        self.status = status
        self.body = body

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
    return load_trial_config().model_copy(update={"spend_ledger": str(tmp_path / "scratch" / "classify-spend.jsonl"), "carried_spend": []})


def _clf(cfg, transport):
    return OpenRouterClassifier(cfg, transport=transport)


PAYLOAD = {"model": "typesafe/jev-1.13", "messages": [{"role": "user", "content": "trend is up"}]}


class TestTheKeyLivesOnlyInTheHeader:
    def test_the_key_is_in_authorization_and_nowhere_else(self, cfg, fake_vault, log_capture):
        t = RecordingTransport(200, b'{"ok": true}')
        clf = _clf(cfg, t)
        status, raw, http_ms = clf._send(PAYLOAD, projected_usd=0.0)
        assert status == 200 and http_ms >= 0
        (call,) = t.calls
        assert call["headers"]["Authorization"] == f"Bearer {FAKE_KEY}"
        others = {k: v for k, v in call["headers"].items() if k != "Authorization"}
        assert FAKE_KEY not in json.dumps(others)
        assert FAKE_KEY.encode() not in call["body"]
        assert FAKE_KEY not in "".join(log_capture)
        assert FAKE_KEY not in json.dumps(vars(clf), default=str)   # never cached

    def test_a_401_that_echoes_the_key_raises_without_it(self, cfg, fake_vault, log_capture):
        echo = json.dumps({"error": {"message": f"bad key {FAKE_KEY}"}}).encode()
        clf = _clf(cfg, RecordingTransport(401, echo))
        with pytest.raises(ClassifyError) as ei:
            clf._send(PAYLOAD, projected_usd=0.0)
        assert "401" in str(ei.value)
        assert FAKE_KEY not in str(ei.value)
        assert ei.value.__cause__ is None and ei.value.__suppress_context__
        assert FAKE_KEY not in "".join(log_capture)

    def test_a_transport_exception_that_echoes_the_key_raises_without_it(self, cfg, fake_vault):
        def boom(*a, **k):
            raise OSError(f"connection reset while sending Bearer {FAKE_KEY}")

        with pytest.raises(ClassifyError) as ei:
            _clf(cfg, boom)._send(PAYLOAD, projected_usd=0.0)
        assert FAKE_KEY not in str(ei.value)
        assert ei.value.__cause__ is None and ei.value.__suppress_context__
        assert FAKE_KEY not in "".join(traceback.format_exception(ei.value))

    def test_a_missing_key_names_the_key_not_a_value_and_sends_nothing(self, cfg, fake_vault, monkeypatch):
        monkeypatch.setattr("cobalt.redact.secrets.read_secret", lambda name: None)
        t = RecordingTransport()
        with pytest.raises(ClassifyError, match=KEY_NAME):
            _clf(cfg, t)._send(PAYLOAD, projected_usd=0.0)
        assert t.calls == []

    def test_a_locked_vault_names_the_key_and_sends_nothing(self, cfg, fake_vault, monkeypatch):
        def locked(name):
            raise VaultAccessError("COBALT_MASTER_KEY is not set on this process")

        monkeypatch.setattr("cobalt.redact.secrets.read_secret", locked)
        t = RecordingTransport()
        with pytest.raises(ClassifyError, match=KEY_NAME):
            _clf(cfg, t)._send(PAYLOAD, projected_usd=0.0)
        assert t.calls == []


class TestTheOutboundGuard:
    def test_a_body_carrying_the_key_is_refused_not_redacted(self, cfg, fake_vault):
        t = RecordingTransport()
        bad = {**PAYLOAD, "messages": [{"role": "user", "content": f"echo {FAKE_KEY}"}]}
        with pytest.raises(ClassifyError, match="refused, not sent") as ei:
            _clf(cfg, t)._send(bad, projected_usd=0.0)
        assert FAKE_KEY not in str(ei.value)
        assert t.calls == []

    def test_a_body_carrying_any_sk_or_string_is_refused(self, cfg, fake_vault):
        t = RecordingTransport()
        other = "sk-or-v1-" + "f" * 40          # not the vault's key: the PATTERN catches it
        bad = {**PAYLOAD, "messages": [{"role": "user", "content": other}]}
        with pytest.raises(ClassifyError, match="refused, not sent"):
            _clf(cfg, t)._send(bad, projected_usd=0.0)
        assert t.calls == []

    def test_an_inactive_literal_guard_refuses_a_keyed_call(self, cfg, fake_vault, monkeypatch):
        monkeypatch.setattr(
            "cobalt.redact.guard.load_literals",
            lambda *a, **k: LiteralGuard({}, available=False, reason="locked"),
        )
        t = RecordingTransport()
        with pytest.raises(ClassifyError, match="INACTIVE"):
            _clf(cfg, t)._send(PAYLOAD, projected_usd=0.0)
        assert t.calls == []

    def test_the_stored_guard_refuses_an_object_carrying_the_key(self, cfg, fake_vault):
        clf = _clf(cfg, RecordingTransport())
        with pytest.raises(ClassifyError, match="not written") as ei:
            clf._guard_stored({"raw": {"echo": FAKE_KEY}})
        assert FAKE_KEY not in str(ei.value)
        clf._guard_stored({"raw": {"echo": "nothing secret here"}})   # passes


class TestTheLedger:
    def test_a_read_never_creates_the_file(self, tmp_path):
        led = Ledger(tmp_path / "scratch" / "classify-spend.jsonl", cap_usd=5, call_ceiling=10)
        assert led.spent() == 0 and led.calls() == 0
        led.check(1.0, calls=1)
        assert not led.path.exists()

    def test_record_creates_it_and_spent_sums_it(self, tmp_path):
        led = Ledger(tmp_path / "scratch" / "classify-spend.jsonl", cap_usd=5, call_ceiling=10)
        led.record("c1", 0.5, "returned")
        led.record("c2", 0.25, "computed")
        assert led.spent() == pytest.approx(0.75) and led.calls() == 2
        line = json.loads(led.path.read_text().splitlines()[0])
        assert set(line) == {"call_id", "cost_usd", "cost_source", "at"}

    def test_a_projection_crossing_the_cap_is_refused_with_zero_calls(self, cfg, fake_vault):
        t = RecordingTransport()
        with pytest.raises(ClassifyError, match="cap"):
            _clf(cfg, t)._send(PAYLOAD, projected_usd=cfg.spend_cap_usd + 0.01)
        assert t.calls == []

    def test_total_demand_two_runs_under_the_cap_together_over_it(self, tmp_path):
        led = Ledger(tmp_path / "l.jsonl", cap_usd=5, call_ceiling=100)
        led.check(3.0, calls=1)                       # run 1 alone: fine
        led.record("run1", 3.0, "returned")
        with pytest.raises(ClassifyError, match="cap"):
            led.check(3.0, calls=1)                   # run 2 alone would pass; the total does not

    def test_the_call_ceiling_is_total_demand_too(self, tmp_path):
        led = Ledger(tmp_path / "l.jsonl", cap_usd=5, call_ceiling=2)
        led.record("a", 0.0, "returned")
        with pytest.raises(ClassifyError, match="ceiling"):
            led.check(0.0, calls=2)

    def test_the_running_total_reaching_the_cap_stops(self, tmp_path):
        led = Ledger(tmp_path / "l.jsonl", cap_usd=1, call_ceiling=100)
        led.record("a", 0.6, "returned")
        led.stop_if()
        led.record("b", 0.4, "returned")
        with pytest.raises(ClassifyError, match="cap"):
            led.stop_if()

    def test_a_cost_ten_times_its_projection_stops(self, tmp_path):
        led = Ledger(tmp_path / "l.jsonl", cap_usd=5, call_ceiling=100)
        led.check_cost(returned=0.001, projected=0.001)
        with pytest.raises(ClassifyError, match="10"):
            led.check_cost(returned=0.0101, projected=0.001)
        with pytest.raises(ClassifyError):
            led.check_cost(returned=0.001, projected=0.0)   # a free projection that was not free


def test_the_module_imports_no_old_tree_and_no_sdk():
    src = open(col.__file__).read()
    for banned in ("cobalt_agent", "litellm", "import requests", "import httpx", "typesafe_sdk"):
        assert banned not in src
