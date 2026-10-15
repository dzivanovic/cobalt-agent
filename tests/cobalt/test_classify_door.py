"""R4 — the door (`POST /api/v1/systemone`), the parse, the probe subcommand.

ALL OFFLINE: a fake transport, a CONSTRUCTED fake key, no socket.

THE DOOR is OpenRouter's System One route (desk R47), built field for
field from its published OpenAPI schema (`DecisionsRequest` /
`DecisionsResponse`, saved in the worktree's scratch/docs-openrouter/).
The response fixtures are built from that schema's own documented
example — `SHAPE: OpenRouter OpenAPI example, not yet a live capture`.
The parse tests are PARAMETRIZED over every
`tests/fixtures/classify/openrouter-*response*.json`: the probe (`31`)
adds its live capture beside the example and the SAME tests run on it.
Expected values are read FROM each fixture, never restated as constants.
"""

from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

import pytest
from loguru import logger

from cobalt.classify import collector as col
from cobalt.classify.collector import (
    KEY_NAME,
    ClassifyAuthError,
    ClassifyError,
    OpenRouterClassifier,
    parse_answers,
)
from cobalt.classify.config import load_trial_config
from cobalt.classify.models import CallRecord, Choice, Noul, QuestionSet, Score, TrialItem
from cobalt.redact.secrets import LiteralGuard

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "classify"
ENTRY = FIXTURES / "openrouter-model-entry.real-shape.json"
EXAMPLE = json.loads((FIXTURES / "systemone-openapi-example.json").read_text())
RESPONSES = sorted(FIXTURES.glob("openrouter-*response*.json"))
WRAPPER = Path(__file__).resolve().parents[2] / "ops" / "run_classify_trial.sh"

FAKE_KEY = "sk-or-v1-TESTONLY-" + "0123456789abcdef" * 2
PRICING = json.loads(ENTRY.read_text())["data"]["endpoints"][0]["pricing"]


class RecordingTransport:
    def __init__(self, status: int = 200, body: bytes = b"{}"):
        self.calls: list[dict] = []
        self.status, self.body = status, body

    def __call__(self, method, url, headers, body, timeout):
        self.calls.append({"method": method, "url": url, "headers": dict(headers), "body": body})
        return self.status, self.body


class NoTransport:
    calls: list = []

    def __call__(self, *a, **k):
        raise AssertionError("the transport was called")


@pytest.fixture
def fake_vault(monkeypatch):
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


def _clf(cfg, transport, pricing=PRICING):
    return OpenRouterClassifier(cfg, transport=transport, pricing=pricing)


def _example_qset() -> QuestionSet:
    """The OpenAPI example request's questions, in Cobalt's neutral schema
    (`unsure` added to the Choice: Cobalt's Choice always carries it)."""
    q = EXAMPLE["request"]["questions"]
    return QuestionSet(id="openapi-example", version=1, questions={
        "is_bug": Noul(instructions=q["is_bug"]["instructions"],
                       true=q["is_bug"]["criteria"]["true"], false=q["is_bug"]["criteria"]["false"]),
        "team": Choice(instructions=q["team"]["instructions"],
                       options={**q["team"]["criteria"], "unsure": "cannot tell"}),
        "urgency": Score(instructions=q["urgency"]["instructions"], levels=q["urgency"]["criteria"]),
    })


# -- the config ---------------------------------------------------------------

def test_the_committed_door_is_systemone_on_openrouter():
    c = load_trial_config()
    assert c.door == "systemone"
    assert c.door_url == "https://openrouter.ai/api/v1/systemone"


# -- rendering: field for field from DecisionsRequest ---------------------------

def test_the_floor_request_carries_only_the_schemas_fields(cfg):
    qset, item = _floor(cfg)
    body = _clf(cfg, NoTransport()).render(qset, item)
    assert set(body) == {"model", "state", "questions"} <= set(EXAMPLE["request"])
    assert body["model"] == cfg.model_id
    assert body["state"] == item.state
    assert list(body["questions"]) == list(qset.questions)
    (qid, q), = qset.questions.items()
    assert body["questions"][qid] == {
        "type": "noul", "instructions": q.instructions,
        "criteria": {"true": q.true, "false": q.false},
    }


def test_each_type_renders_as_the_documented_example_does(cfg):
    body = _clf(cfg, NoTransport()).render(
        _example_qset(), TrialItem(id="x", state=EXAMPLE["request"]["state"], provenance="constructed"))
    doc = EXAMPLE["request"]["questions"]
    for qid in doc:
        assert set(body["questions"][qid]) == set(doc[qid])
        assert body["questions"][qid]["type"] == doc[qid]["type"]
    assert body["questions"]["is_bug"]["criteria"] == doc["is_bug"]["criteria"]
    assert body["questions"]["urgency"]["criteria"] == doc["urgency"]["criteria"]
    assert body["questions"]["team"]["criteria"] == {**doc["team"]["criteria"], "unsure": "cannot tell"}
    assert body["state"] == EXAMPLE["request"]["state"]


def test_a_noul_without_descriptions_sends_no_criteria(cfg):
    qs = QuestionSet(id="n", version=1, questions={"q": Noul(instructions="the state is quiet")})
    body = _clf(cfg, NoTransport()).render(qs, TrialItem(id="i", state="quiet", provenance="constructed"))
    assert body["questions"]["q"] == {"type": "noul", "instructions": "the state is quiet"}


def test_a_noul_with_one_side_only_is_refused_never_filled(cfg):
    # DecisionsNoulQuestion.criteria requires BOTH 'true' and 'false'.
    qs = QuestionSet(id="n", version=1, questions={"q": Noul(instructions="i", true="yes side")})
    with pytest.raises(ClassifyError, match="both"):
        _clf(cfg, NoTransport()).render(qs, TrialItem(id="i", state="s", provenance="constructed"))


# -- parsing: PARAMETRIZED over every response fixture -------------------------

def test_there_is_at_least_one_response_fixture():
    assert RESPONSES, "no tests/fixtures/classify/openrouter-*response*.json — L1: never a skip"


@pytest.fixture(params=RESPONSES or [None], ids=lambda p: p.name if p else "NONE")
def response(request):
    assert request.param is not None, "no response fixture (L1)"
    return request.param.read_bytes()


def _call(cfg, raw: bytes, fake_vault=None, status: int = 200):
    t = RecordingTransport(status, raw)
    qset, item = _floor(cfg)
    rec = _clf(cfg, t).classify(qset, item)
    return rec, t


def test_parse_takes_every_field_as_returned(cfg, fake_vault, response):
    fx = json.loads(response)
    rec, _ = _call(cfg, response)
    assert rec.status == "ok"
    assert rec.model_returned == fx["model"]
    assert rec.provider_returned == fx.get("provider")
    assert rec.usage.input_tokens == fx["usage"]["input_tokens"]
    assert rec.usage.output_tokens == fx["usage"]["output_tokens"]
    assert rec.cost_usd == fx["usage"]["cost"] and rec.cost_source == "returned"
    assert rec.raw_response == fx
    for a in rec.answers:
        got = fx["answers"][a.question_id]
        assert a.probabilities == got.get("probabilities")
        assert a.confidence == got.get("confidence")
        present = "probabilities" in got or "confidence" in got
        assert a.source == ("returned" if present else "absent")
    CallRecord.model_validate_json(rec.model_dump_json())


def test_an_answer_removed_is_invalid_and_loud(cfg, fake_vault, response, log_capture):
    fx = json.loads(response)
    fx["answers"] = {}
    rec, _ = _call(cfg, json.dumps(fx).encode())
    assert rec.status == "invalid" and rec.answers == []
    assert "invalid" in "".join(log_capture).lower()


def test_a_missing_cost_is_computed_from_the_entry_pricing(cfg, fake_vault, response):
    fx = json.loads(response)
    del fx["usage"]["cost"]
    rec, _ = _call(cfg, json.dumps(fx).encode())
    u = fx["usage"]
    expected = u["input_tokens"] * float(PRICING["prompt"]) + u["output_tokens"] * float(PRICING["completion"])
    assert rec.cost_source == "computed"
    assert rec.cost_usd == pytest.approx(expected)


def test_the_openapi_example_pair_parses_with_probabilities(cfg):
    answers = {a.question_id: a for a in parse_answers(_example_qset(), EXAMPLE["response"])}
    doc = EXAMPLE["response"]["answers"]
    assert answers["team"].value == doc["team"]["choice"]
    assert answers["team"].probabilities == doc["team"]["probabilities"]
    assert answers["team"].confidence == doc["team"]["confidence"]
    assert answers["team"].source == "returned"
    assert answers["urgency"].value == doc["urgency"]["score"]
    assert answers["urgency"].probabilities == doc["urgency"]["probabilities"]
    assert answers["is_bug"].value == doc["is_bug"]["noul"]
    assert answers["is_bug"].probabilities is None and answers["is_bug"].source == "absent"


@pytest.mark.parametrize("mutate", [
    lambda a: a["team"].update(choice="not-an-option"),
    lambda a: a["team"].update(type="score"),
    lambda a: a["urgency"].update(score=7.5),
    lambda a: a["is_bug"].update(noul=1.5),
    lambda a: a["is_bug"].pop("noul"),
    lambda a: a.update(extra={"type": "noul", "noul": 0.5}),
], ids=["choice-not-an-option", "wrong-type", "score-out-of-range", "noul-out-of-range",
        "noul-missing", "an-unasked-answer"])
def test_a_schema_invalid_answer_is_refused_never_defaulted(mutate):
    resp = copy.deepcopy(EXAMPLE["response"])
    mutate(resp["answers"])
    with pytest.raises(ValueError):
        parse_answers(_example_qset(), resp)


def test_a_response_missing_a_required_field_is_invalid(cfg, fake_vault):
    fx = json.loads(RESPONSES[0].read_bytes())
    del fx["model"]
    rec, _ = _call(cfg, json.dumps(fx).encode())
    assert rec.status == "invalid" and rec.model_returned is None


# -- the send ------------------------------------------------------------------

def test_the_request_goes_to_the_door_with_the_key_only_in_authorization(cfg, fake_vault, log_capture):
    rec, t = _call(cfg, RESPONSES[0].read_bytes())
    (call,) = t.calls
    assert call["method"] == "POST" and call["url"] == cfg.door_url
    assert call["headers"]["Authorization"] == f"Bearer {FAKE_KEY}"
    assert FAKE_KEY not in json.dumps({k: v for k, v in call["headers"].items() if k != "Authorization"})
    assert FAKE_KEY.encode() not in call["body"]
    assert json.loads(call["body"]) == rec.request
    assert FAKE_KEY not in rec.model_dump_json()
    assert FAKE_KEY not in "".join(log_capture)


def test_a_429_is_recorded_and_not_retried(cfg, fake_vault):
    rec, t = _call(cfg, b'{"error":{"code":429,"message":"Rate limit exceeded"}}', status=429)
    assert len(t.calls) == 1
    assert rec.status == "http_error" and rec.http_status == 429


def test_a_401_stops_the_run(cfg, fake_vault):
    with pytest.raises(ClassifyAuthError, match="401"):
        _call(cfg, json.dumps({"error": {"message": f"bad {FAKE_KEY}"}}).encode(), status=401)


def test_no_pricing_means_no_call(cfg, fake_vault):
    qset, item = _floor(cfg)
    t = RecordingTransport(200, RESPONSES[0].read_bytes())
    with pytest.raises(ClassifyError, match="pricing"):
        OpenRouterClassifier(cfg, transport=t, pricing={}).classify(qset, item)
    assert t.calls == []


def test_the_ledger_records_the_call_and_a_tenfold_overrun_stops(cfg, fake_vault):
    fx = json.loads(RESPONSES[0].read_bytes())
    clf = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    qset, item = _floor(cfg)
    clf.classify(qset, item)
    assert clf.ledger.calls() == 1 and clf.ledger.spent() == pytest.approx(fx["usage"]["cost"])
    fx["usage"]["cost"] = 1.0                           # far above ÷4 × the listed price
    clf2 = _clf(cfg, RecordingTransport(200, json.dumps(fx).encode()))
    with pytest.raises(ClassifyError, match="10x"):
        clf2.classify(qset, item)
    assert clf2.ledger.calls() == 2                     # the money was spent; it is counted


# -- the probe subcommand --------------------------------------------------------

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


def test_probe_writes_both_files_and_prints_one_line(probe_env, fake_vault, capsys):
    ccli, A, install, root = probe_env
    raw = RESPONSES[0].read_bytes()
    t = install(RecordingTransport(200, raw))
    ccli.cmd_probe(A())
    assert len(t.calls) == 1
    out = root / A.out
    rec = CallRecord.model_validate_json(out.read_text())
    assert (root / "scratch" / "probe-20260923T120000.raw.json").read_bytes() == raw
    lines = capsys.readouterr().out.strip().splitlines()
    assert len(lines) == 1
    line = lines[0]
    assert line.startswith("PROBE status=200 ")
    assert f"model={rec.model_returned} " in line
    assert f"provider={rec.provider_returned or 'none'} " in line
    assert f"cost_usd={rec.cost_usd} cost_source={rec.cost_source} " in line
    probs = "present" if any(a.probabilities is not None for a in rec.answers) else "absent"
    assert f"probabilities={probs} " in line
    assert "guard_literals=active" in line and "cap_usd=5" in line
    ledger = root / "scratch" / "classify-spend.jsonl"
    assert json.loads(ledger.read_text().splitlines()[0])["cost_usd"] == rec.cost_usd
    assert FAKE_KEY not in out.read_text() and FAKE_KEY not in line


def test_probe_with_no_key_names_it_and_sends_nothing(probe_env, fake_vault, monkeypatch):
    ccli, A, install, _ = probe_env
    monkeypatch.setattr("cobalt.redact.secrets.read_secret", lambda name: None)
    t = install(RecordingTransport(200, RESPONSES[0].read_bytes()))
    with pytest.raises(ClassifyError, match=KEY_NAME):
        ccli.cmd_probe(A())
    assert t.calls == []


def test_probe_refuses_when_a_probe_file_exists(probe_env, fake_vault):
    ccli, A, install, root = probe_env
    (root / "scratch").mkdir(parents=True, exist_ok=True)
    (root / "scratch" / "probe-20260922T000000.json").write_text("{}")
    t = install(RecordingTransport(200, RESPONSES[0].read_bytes()))
    with pytest.raises(ClassifyError, match="probe-20260922T000000.json"):
        ccli.cmd_probe(A())
    assert t.calls == []


def test_probe_refuses_an_out_not_named_probe(probe_env, fake_vault):
    ccli, A, install, _ = probe_env
    t = install(RecordingTransport(200, RESPONSES[0].read_bytes()))
    A.out = "scratch/other.json"
    with pytest.raises(ClassifyError, match="probe-"):
        ccli.cmd_probe(A())
    assert t.calls == []


def test_a_stored_guard_refusal_writes_nothing(probe_env, fake_vault):
    ccli, A, install, root = probe_env
    fx = json.loads(RESPONSES[0].read_bytes())
    fx["provider"] = f"echo {FAKE_KEY}"
    install(RecordingTransport(200, json.dumps(fx).encode()))
    with pytest.raises(ClassifyError, match="not written") as ei:
        ccli.cmd_probe(A())
    assert FAKE_KEY not in str(ei.value)
    assert not (root / A.out).exists()
    assert not (root / "scratch" / "probe-20260923T120000.raw.json").exists()
