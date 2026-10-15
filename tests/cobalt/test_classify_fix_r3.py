"""JEV fix round 3 (L75; his R86 / R89) — one test group per row, each
RED on the unfixed code before its fix (report
`jev-fix-r3-build-2026-09-23.md`).

F9  a returned cost is never dropped because the tokens beside it are
    malformed (check A r3's F7-COST, C3 HOLDS).
P1  the probe can ask a choice and a score (`--set S1`).
P2  the S1 probe's live body parses, its probabilities / confidence as
    returned.

ALL OFFLINE: a CONSTRUCTED fake key and a recording transport. The shapes
(`fake_vault`, `log_capture`, `cfg`, `RecordingTransport`, `_floor`,
`_clf`, `_example`, `PRICING`, `_classify_counted`) are copied from
`test_classify_fix_r2.py`, never imported. No test writes under the
worktree's `scratch/` or touches the real ledger: `cfg` roots every path
in `tmp_path`.
"""

from __future__ import annotations

import json
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


# -- F9: a returned cost is never dropped for the tokens beside it ----------------
#
# A finite `usage.cost` >= 0 the server returned is what the ledger books,
# whatever the token counts beside it; the call stays `invalid` when those
# counts are malformed. Only a missing or unusable returned cost falls back
# to the computed cost or the projection.

def test_f9_a_the_c3_input_books_the_returned_cost_and_the_overrun_stop_fires(cfg, fake_vault):
    fx = _example()
    fx["usage"] = {"input_tokens": -1, "output_tokens": 0, "cost": 4.9}
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    assert clf.ledger.cap_usd == 5
    with pytest.raises(ClassifyError, match="10x|overrun|its projection"):
        clf.classify(qset, item)
    assert clf.ledger.calls() == 1
    (line,) = clf.ledger.entries()
    assert line["cost_source"] == "returned"
    assert line["cost_usd"] == 4.9
    assert clf.ledger.spent() == 4.9


def test_f9_c_the_cap_sees_a_server_stated_cost_beside_malformed_tokens(cfg, fake_vault, tmp_path):
    fx = _example()
    fx["usage"] = {"input_tokens": -1, "output_tokens": 0, "cost": 5.0}
    led = Ledger(tmp_path / "cap" / "classify-spend.jsonl", cap_usd=5, call_ceiling=10)
    t = RecordingTransport(200, json.dumps(fx).encode())
    clf = OpenRouterClassifier(cfg, transport=t, ledger=led, pricing=PRICING)
    qset, item = _floor(cfg)
    with pytest.raises(ClassifyError, match="10x"):
        clf.classify(qset, item)
    assert led.spent() == 5.0
    t.body = json.dumps(_example()).encode()
    with pytest.raises(ClassifyError, match="spend cap"):
        clf.classify(qset, item)
    assert len(t.calls) == 1


@pytest.mark.parametrize(
    "cost",
    [-0.5, float("nan"), "0.00002", None],
    ids=["negative", "nan", "string", "absent"],
)
def test_f9_d_an_unusable_returned_cost_beside_malformed_tokens_is_unchanged(cfg, fake_vault, cost):
    # A GUARD, not a red-first test: green before F9 and after it.
    fx = _example()
    fx["usage"] = {"input_tokens": -1, "output_tokens": 0}
    if cost is not None:
        fx["usage"]["cost"] = cost
    qset, item = _floor(cfg)
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    rec = _classify_counted(clf, qset, item)
    assert rec.status == "invalid"
    assert rec.cost_usd is None and rec.cost_source is None
    assert clf.ledger.calls() == 1
    (line,) = clf.ledger.entries()
    assert line["cost_source"] == "projected"
    assert line["cost_usd"] == rec.projected_usd


# -- P1: the probe can ask a choice and a score (his R89) -------------------------
#
# FLOOR's one Noul cannot carry probabilities / confidence by the schema
# (`DecisionsNoulAnswer` holds `noul` only). `--set S1` asks a choice and a
# score. One probe per set per branch.

EXAMPLE = json.loads((FIXTURES / "systemone-openapi-example.json").read_text())


def _s1_body(cfg) -> dict:
    """The OpenAPI example's answers RE-KEYED onto S1's question ids —
    constructed values, the example's real shape (L45)."""
    qset, _ = cfg.resolve("S1")
    ex = EXAMPLE["response"]
    team, urg, bug = ex["answers"]["team"], ex["answers"]["urgency"], ex["answers"]["is_bug"]
    options = list(qset.questions["relevance"].options)
    team_probs = list(team["probabilities"].values())
    rel_probs = {k: (team_probs[i] if i < len(team_probs) else 0) for i, k in enumerate(options)}
    levels = qset.questions["urgency"].levels
    return {
        "answers": {
            "relevance": {"type": "choice", "choice": max(rel_probs, key=rel_probs.get),
                          "confidence": team["confidence"], "probabilities": rel_probs},
            "urgency": {"type": "score", "score": urg["score"], "confidence": urg["confidence"],
                        "legend": {str(i): lv for i, lv in enumerate(levels)},
                        "probabilities": {str(i): urg["probabilities"].get(str(i), 0)
                                          for i in range(len(levels))}},
            "duplicate": dict(bug),
            "argues_for_label": dict(bug),
        },
        "id": ex["id"], "model": ex["model"], "provider": ex["provider"], "usage": dict(ex["usage"]),
    }


@pytest.fixture
def probe_env(cfg, tmp_path, monkeypatch):
    from cobalt.classify import cli as ccli
    from cobalt.classify import collector as col

    monkeypatch.setattr(ccli, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(ccli, "load_trial_config", lambda: cfg)

    def install(transport):
        monkeypatch.setattr(col, "urllib_transport", transport)
        return transport

    return ccli, install, tmp_path


def _args(out: str, set_name: str | None = None):
    from types import SimpleNamespace

    return SimpleNamespace(out=out) if set_name is None else SimpleNamespace(out=out, set=set_name)


S1_OUT = "scratch/probe-s1-20260923T120000.json"


def test_p1_a_the_s1_probe_asks_a_choice_and_a_score_and_reads_their_probabilities(
        cfg, probe_env, fake_vault, capsys):
    from cobalt.classify.models import CallRecord

    ccli, install, root = probe_env
    body = _s1_body(cfg)
    t = install(RecordingTransport(200, json.dumps(body).encode()))
    ccli.cmd_probe(_args(S1_OUT, "S1"))
    assert len(t.calls) == 1
    sent = json.loads(t.calls[0]["body"])["questions"]
    assert sent["relevance"]["type"] == "choice"
    assert sent["urgency"]["type"] == "score"
    rec = CallRecord.model_validate_json((root / S1_OUT).read_text())
    assert rec.item_id == "s1-01" and rec.set_id == "S1"
    got = {a.question_id: a for a in rec.answers}
    for qid in ("relevance", "urgency"):
        assert got[qid].probabilities == body["answers"][qid]["probabilities"]
        assert got[qid].confidence == body["answers"][qid]["confidence"]
    assert (root / "scratch" / "probe-s1-20260923T120000.raw.json").read_bytes() == t.body
    (line,) = capsys.readouterr().out.strip().splitlines()
    assert line.startswith("PROBE status=200 ")
    assert "probabilities=present confidence=present" in line


def test_p1_b_a_floor_probe_file_does_not_refuse_the_s1_probe_but_an_s1_file_does(
        cfg, probe_env, fake_vault):
    ccli, install, root = probe_env
    (root / "scratch").mkdir(parents=True, exist_ok=True)
    (root / "scratch" / "probe-20260922T000000.json").write_text("{}")
    t = install(RecordingTransport(200, json.dumps(_s1_body(cfg)).encode()))
    ccli.cmd_probe(_args(S1_OUT, "S1"))
    assert len(t.calls) == 1

    (root / S1_OUT).unlink()
    (root / "scratch" / "probe-s1-20260922T000000.json").write_text("{}")
    t2 = install(RecordingTransport(200, json.dumps(_s1_body(cfg)).encode()))
    with pytest.raises(ClassifyError, match="probe-s1-"):
        ccli.cmd_probe(_args(S1_OUT, "S1"))
    assert t2.calls == []


@pytest.mark.parametrize("out", ["scratch/probe-20260923T120000.json", "scratch/probe-s1-x.txt"],
                         ids=["floor-name", "not-json"])
def test_p1_c_an_s1_probe_needs_a_probe_s1_out(cfg, probe_env, fake_vault, out):
    ccli, install, _ = probe_env
    t = install(RecordingTransport(200, json.dumps(_s1_body(cfg)).encode()))
    with pytest.raises(ClassifyError, match="probe-s1-"):
        ccli.cmd_probe(_args(out, "S1"))
    assert t.calls == []


def test_p1_c_no_set_but_floor_and_s1_can_be_probed(cfg, probe_env, fake_vault):
    import argparse

    ccli, install, _ = probe_env
    t = install(RecordingTransport(200, json.dumps(_s1_body(cfg)).encode()))
    with pytest.raises(ClassifyError, match="FLOOR.*S1"):
        ccli.cmd_probe(_args("scratch/probe-s2-20260923T120000.json", "S2"))
    parser = argparse.ArgumentParser()
    ccli.add_parser(parser.add_subparsers(dest="cmd"))
    with pytest.raises(SystemExit):
        parser.parse_args(["classify", "probe", "--set", "S2", "--out", "scratch/probe-x.json"])
    assert parser.parse_args(["classify", "probe", "--out", "scratch/probe-x.json"]).set == "FLOOR"
    assert t.calls == []


def test_p1_d_an_s1_probe_file_refuses_a_floor_probe(cfg, probe_env, fake_vault):
    ccli, install, root = probe_env
    (root / "scratch").mkdir(parents=True, exist_ok=True)
    (root / "scratch" / "probe-s1-20260922T000000.json").write_text("{}")
    t = install(RecordingTransport(200, RESPONSE.read_bytes()))
    with pytest.raises(ClassifyError, match="probe-s1-20260922T000000.json"):
        ccli.cmd_probe(_args("scratch/probe-20260923T120000.json"))
    assert t.calls == []


# -- P2: the S1 probe's live body (his R89; L45) -----------------------------------

S1_LIVE = FIXTURES / "openrouter-probe-s1.real-shape.json"


def test_p2_the_live_s1_body_parses_with_every_answer_as_returned(cfg):
    from cobalt.classify.collector import parse_answers

    body = json.loads(S1_LIVE.read_bytes())
    qset, _ = cfg.resolve("S1")
    answers = {a.question_id: a for a in parse_answers(qset, body)}
    assert set(answers) == set(qset.questions)
    for qid, a in answers.items():
        got = body["answers"][qid]
        assert a.probabilities == got.get("probabilities")
        assert a.confidence == got.get("confidence")
