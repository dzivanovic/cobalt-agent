"""JEV fix round 2 (L75) — one test group per FIX row, each RED on the
unfixed code before its fix (report `jev-fix-r2-build-2026-09-23.md`).

The invariant these rows finish (round 1's F4): every POST that came back
is exactly one ledger line whose cost is finite and >= 0.

ALL OFFLINE: a CONSTRUCTED fake key and a recording transport. The shapes
(`fake_vault`, `log_capture`, `cfg`, `RecordingTransport`, `_floor`,
`_clf`, `_example`, `PRICING`) are copied from `test_classify_fix_r1.py`,
never imported.
"""

from __future__ import annotations

import json
import math
import shutil
from pathlib import Path

import pytest
from loguru import logger

from cobalt.classify.collector import (
    KEY_NAME,
    ClassifyError,
    OpenRouterClassifier,
)
from cobalt.classify.config import load_trial_config
from cobalt.classify.ledger import Ledger
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


def _example() -> dict:
    """The committed response fixture, read fresh (never edited on disk)."""
    return json.loads(RESPONSE.read_text())


def _classify_counted(clf, qset, item):
    """`clf.classify`, but an escaped raise names the ledger's line count,
    so the RED run shows whether the call that came back was booked."""
    try:
        return clf.classify(qset, item)
    except Exception as e:  # noqa: BLE001
        first = (str(e).splitlines() or [""])[0]
        raise AssertionError(
            f"classify raised {type(e).__name__} with ledger calls() == "
            f"{clf.ledger.calls()}: {first}"
        ) from e


# -- F7: a 200 whose usage tokens are negative is one ledger line ----------------
#
# A usage that is not two non-negative ints is no usage: the call is
# `invalid` and booked at its own projection (round 1's F4 path). Its
# `cost`, if any, is not taken on its own.

def _assert_one_projected_line(clf, rec):
    assert rec.status == "invalid"
    assert clf.ledger.calls() == 1
    (line,) = clf.ledger.entries()
    assert line["cost_source"] == "projected"
    assert line["cost_usd"] == rec.projected_usd
    assert line["cost_usd"] > 0


def test_f7_a_negative_input_token_count_is_one_projected_line(cfg, fake_vault):
    fx = _example()
    fx["usage"] = {"input_tokens": -4000, "output_tokens": 0}
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    rec = _classify_counted(clf, qset, item)
    _assert_one_projected_line(clf, rec)


def test_f7_a_returned_cost_beside_a_negative_token_count_is_booked_as_returned(cfg, fake_vault):
    # replaced by JEV fix r3 F9 (his R86): the returned cost is booked, never dropped
    fx = _example()
    fx["usage"]["cost"] = 0.00002
    fx["usage"]["output_tokens"] = -1
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    rec = _classify_counted(clf, qset, item)
    assert rec.status == "invalid"
    assert rec.usage is None
    assert rec.cost_usd == 0.00002
    assert rec.cost_source == "returned"
    assert clf.ledger.calls() == 1
    (line,) = clf.ledger.entries()
    assert line["cost_source"] == "returned"
    assert line["cost_usd"] == 0.00002


def test_f7_the_call_ceiling_sees_a_200_with_negative_tokens(cfg, fake_vault, tmp_path):
    fx = _example()
    fx["usage"] = {"input_tokens": -4000, "output_tokens": 0}
    led = Ledger(tmp_path / "ceiling" / "classify-spend.jsonl", cap_usd=5, call_ceiling=1)
    t = RecordingTransport(200, json.dumps(fx).encode())
    clf = OpenRouterClassifier(cfg, transport=t, ledger=led, pricing=PRICING)
    qset, item = _floor(cfg)
    _classify_counted(clf, qset, item)
    with pytest.raises(ClassifyError, match="ceiling"):
        clf.classify(qset, item)
    assert len(t.calls) == 1


# -- F8: no call that came back hands the ledger a cost it refuses ----------------
#
# A listed price that is negative or not finite refuses the call before it
# is made (L1: no cost, no call). A computed cost that is not finite is
# never recorded: the call is booked at its projection, with one error line.

def _example_without_cost() -> dict:
    fx = _example()
    del fx["usage"]["cost"]
    return fx


@pytest.mark.parametrize(
    "pricing",
    [
        {"prompt": "-0.000000042", "completion": "0"},
        {"prompt": PRICING["prompt"], "completion": "-1"},
        {"prompt": "nan", "completion": "0"},
    ],
    ids=["negative-prompt", "negative-completion", "nan-prompt"],
)
def test_f8_a_negative_or_non_finite_price_refuses_before_any_call(cfg, fake_vault, pricing):
    t = RecordingTransport(200, json.dumps(_example_without_cost()).encode())
    clf = OpenRouterClassifier(cfg, transport=t, pricing=pricing)
    qset, item = _floor(cfg)
    with pytest.raises(ClassifyError, match="pric"):
        clf.classify(qset, item)
    assert len(t.calls) == 0
    assert not clf.ledger.path.exists()


def test_f8_a_computed_cost_that_overflows_is_booked_at_its_projection(cfg, fake_vault, log_capture):
    fx = _example_without_cost()
    fx["usage"]["output_tokens"] = 10**9
    t = RecordingTransport(200, json.dumps(fx).encode())
    clf = OpenRouterClassifier(cfg, transport=t,
                               pricing={"prompt": PRICING["prompt"], "completion": "1e300"})
    qset, item = _floor(cfg)
    rec = _classify_counted(clf, qset, item)
    assert clf.ledger.calls() == 1
    (line,) = clf.ledger.entries()
    assert line["cost_source"] == "projected"
    assert line["cost_usd"] == rec.projected_usd
    assert math.isfinite(clf.ledger.spent())
    assert rec.cost_usd is None
    assert rec.status == "invalid"  # an ok record carries a cost (CallRecord, L1)
    not_finite = [ln for ln in log_capture if "ERROR" in ln and "not finite" in ln]
    assert len(not_finite) == 1
