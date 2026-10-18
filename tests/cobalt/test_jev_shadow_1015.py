"""Card 591 (jev-shadow-1015) — the JEV shadow router and routing ledger,
one spend ledger for every keyed run, and the two old-tree paths to the
OpenRouter key closed. One test group per row: D2, F13, F2, F3, J1, F4,
F5, F6, J2, F7, F8, F9, F10, F11, F1, F12.

ALL OFFLINE: a stub transport that counts its calls, a CONSTRUCTED fake
key, a stub `read_secret` and the F19 literal guard stubbed active (the
trial tests' `fake_vault` shape). Every ledger, vault, config and git
repo lives under `tmp_path`; no test writes the host ledgers. Each test
imports `cobalt.classify.route` INSIDE its body, never at module level, so
a red names its own reason and never fails the collection.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[2]
TRIAL_YAML = REPO / "configs" / "cobalt" / "classify" / "trial.yaml"
ROUTE_YAML = REPO / "configs" / "cobalt" / "classify" / "route.yaml"
OLD_CONFIG_YAML = REPO / "configs" / "config.yaml"
CLASSIFY_SRC = REPO / "src" / "cobalt" / "classify"
SHADOW_HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "SHADOW-HUB.md"
DESIGN = REPO / "docs" / "30 - Design" / "jev-shadow-design-2026-10-14.md"
PLIST_CHECK = REPO / "docs" / "40 - DevDocs" / "reports" / "plist-step-c-check-2026-10-13.md"
FIXTURES = REPO / "tests" / "fixtures" / "classify"
ENTRY = FIXTURES / "openrouter-model-entry.real-shape.json"
FLOOR_RESPONSE = FIXTURES / "openrouter-probe-response.real-shape.json"
PRICING = json.loads(ENTRY.read_text())["data"]["endpoints"][0]["pricing"]

KEY_NAME = "OPENROUTER_API_KEY"
FAKE_KEY = "sk-or-v1-TESTONLY-" + "zq" * 16
OPUS = "claude-opus-5-5"

#: A constructed commit time for every tmp repo (never a date of his).
STAMP = "2026-01-05T12:00:00+00:00"
DAY = "2026-01-05"
PROMPTS = "docs/40 - DevDocs/prompts/2026-01-05"
REPORTS = "docs/40 - DevDocs/reports"


# -- shared shapes ------------------------------------------------------------------

class Stub:
    """A transport that answers from a script, in order (the last answer
    repeats), and counts every call. An exception in the script is raised."""

    def __init__(self, *answers):
        self.answers = list(answers)
        self.calls: list[dict] = []

    def __call__(self, method, url, headers, body, timeout):
        self.calls.append({"method": method, "url": url, "body": body})
        a = self.answers.pop(0) if len(self.answers) > 1 else self.answers[0]
        if isinstance(a, BaseException):
            raise a
        return a


@pytest.fixture
def fake_vault(monkeypatch):
    from cobalt.redact.secrets import LiteralGuard

    monkeypatch.setattr(
        "cobalt.redact.secrets.read_secret",
        lambda name: FAKE_KEY if name == KEY_NAME else None,
    )
    monkeypatch.setattr(
        "cobalt.redact.guard.load_literals",
        lambda *a, **k: LiteralGuard({KEY_NAME: FAKE_KEY}, available=True),
    )
    return FAKE_KEY


def _trial_cfg(tmp_path, monkeypatch):
    """The committed trial.yaml with REPO_ROOT at tmp; the spend ledger
    moved under tmp AFTER the load (it never reaches the host file)."""
    from cobalt.classify import config as cfg_mod

    monkeypatch.setattr(cfg_mod, "REPO_ROOT", tmp_path)
    c = cfg_mod.load_trial_config()
    return c.model_copy(update={"spend_ledger": str(tmp_path / "host" / "classify-spend.jsonl")})


def _route_cfg(tmp_path, **update):
    """The committed route.yaml, both ledgers moved under tmp after the load."""
    from cobalt.classify import route

    cfg = route.load_route_config()
    return cfg.model_copy(update={
        "spend_ledger": str(tmp_path / "host" / "classify-spend.jsonl"),
        "routing_ledger": str(tmp_path / "host" / "routing-ledger.jsonl"),
        **update,
    })


def _git(repo: Path, *args: str, when: str = STAMP) -> str:
    env = {
        **os.environ,
        "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when,
        "GIT_AUTHOR_NAME": "test", "GIT_AUTHOR_EMAIL": "test@example.invalid",
        "GIT_COMMITTER_NAME": "test", "GIT_COMMITTER_EMAIL": "test@example.invalid",
    }
    r = subprocess.run(["git", "-c", "commit.gpgsign=false", "-C", str(repo), *args],
                       env=env, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    return r.stdout


def _repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    _git(repo, "init", "-q")
    return repo


def _commit(repo: Path, files: dict[str, str], when: str = STAMP) -> str:
    for rel, text in files.items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", "constructed", when=when)
    return _git(repo, "rev-parse", "HEAD").strip()


def _card(job: str = "t1", *, band: str = "MID", tip: str = "", restarts: str = "none",
          check_report: str = "", extra: str = "") -> str:
    return "\n".join([
        f"JOB: {job}",
        f"BAND: {band}",
        "MODEL: x-model",
        f"TIP: {tip}".rstrip(),
        "REPORT: r.md",
        f"CHECK REPORT: {check_report}".rstrip(),
        f"RESTARTS: {restarts}",
        "",
        "## ROWS",
        "",
        "| row | what | red first | files |",
        "|---|---|---|---|",
        "| A1 | the BAND word sits in this row's text | a test | a file |",
        "| A2 | a second constructed row | a test | a file |",
        "",
        "## NOT IN THIS JOB",
        "- nothing constructed here",
        extra,
    ]) + "\n"


def _answers(band: str = "mid", conf: float = 0.8, **gates: float) -> dict:
    """A System One body for the five ROUTE questions (the OpenAPI shape)."""
    g = {"write_path": 0.1, "migration": 0.1, "money": 0.1, "new_horizon": 0.1, **gates}
    ans: dict = {"band": {
        "type": "choice", "choice": band, "confidence": conf,
        "probabilities": {"low": 0.25, "mid": 0.25, "high": 0.25, "unsure": 0.25},
    }}
    for qid, p in g.items():
        ans[qid] = {"type": "noul", "noul": p}
    return {"id": "gen-constructed", "model": "typesafe/jev-constructed", "provider": "TypeSafe",
            "answers": ans, "usage": {"input_tokens": 10, "output_tokens": 2, "cost": 1e-09}}


def _one_card(tmp_path: Path, **card_kw) -> tuple[Path, str]:
    repo = _repo(tmp_path)
    path = f"{PROMPTS}/01-t1-card.md"
    _commit(repo, {path: _card(**card_kw)})
    return repo, path


def _decide(tmp_path, body: dict, **card_kw):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    repo, path = _one_card(tmp_path, **card_kw)
    card = route.load_card(repo, path)
    stub = Stub((200, json.dumps(body).encode()))
    row = route.Router(cfg, transport=stub, pricing=PRICING).route(card)
    return row, stub, cfg, card


def _lines(p) -> list[str]:
    p = Path(p)
    return p.read_text().splitlines() if p.exists() else []


def _classify_parser():
    from cobalt.classify import cli as ccli

    parser = argparse.ArgumentParser(prog="cobalt")
    sub = parser.add_subparsers(dest="group", required=True)
    ccli.add_parser(sub)
    return parser


# -- D2: a 400-digit cost never raises OverflowError --------------------------------

def test_d2_a_400_digit_cost_never_raises_overflow(tmp_path, monkeypatch, fake_vault):
    from cobalt.classify.collector import ClassifyError, OpenRouterClassifier

    cfg = _trial_cfg(tmp_path, monkeypatch)
    body = json.loads(FLOOR_RESPONSE.read_text())
    body["usage"]["cost"] = 10 ** 400
    clf = OpenRouterClassifier(cfg, transport=Stub((200, json.dumps(body).encode())),
                               pricing=PRICING)
    qset, items = cfg.resolve("FLOOR")
    try:
        rec = clf.classify(qset, items[0])
    except ClassifyError:
        return                                     # refused: a loud ClassifyError
    assert rec.cost_usd is None or rec.cost_usd < 10 ** 400   # booked, never the 400 digits


# -- F13: both old-tree paths to the OpenRouter key are closed ----------------------

@pytest.fixture
def old_tree(tmp_path, monkeypatch):
    """A tmp cwd, a generated Fernet key as COBALT_MASTER_KEY, no
    OPENROUTER_API_KEY in the environment, and a tmp `configs/config.yaml`
    holding the real file's `keys:` block, its two `env_key_ref: openrouter`
    models and its `active_profile:` block, copied by content."""
    from cryptography.fernet import Fernet

    monkeypatch.chdir(tmp_path)
    key = Fernet.generate_key().decode()
    monkeypatch.setenv("COBALT_MASTER_KEY", key)
    monkeypatch.delenv(KEY_NAME, raising=False)
    real = yaml.safe_load(OLD_CONFIG_YAML.read_text())
    models = {k: v for k, v in real["models"].items() if v.get("env_key_ref") == "openrouter"}
    assert len(models) == 2
    conf = tmp_path / "configs"
    conf.mkdir()
    (conf / "config.yaml").write_text(yaml.safe_dump({
        "keys": real["keys"], "models": models, "active_profile": real["active_profile"],
    }))
    return key, conf


def _vault(path: Path, key: str, secrets: dict[str, str]):
    from cobalt_agent.security.vault import VaultManager

    vm = VaultManager(str(path))
    assert vm.unlock(key)
    for name, value in secrets.items():
        assert vm.set_secret(key, name, value)
    return vm


def _inject(monkeypatch, vm):
    from cobalt_agent.config import CobaltSettings, Config

    monkeypatch.setattr(Config, "_vault_manager", vm)
    return object.__new__(Config).inject_secrets(CobaltSettings())


def test_f13_lower_case_entry_is_not_injected(old_tree, tmp_path, monkeypatch):
    key, _ = old_tree
    vm = _vault(tmp_path / "lower.vault", key, {"openrouter_api_key": "dummy-or-lower"})
    out = _inject(monkeypatch, vm)
    assert out.llm.api_key != "dummy-or-lower"


def test_f13_upper_case_entry_never_reaches_keys(old_tree, tmp_path):
    from cobalt_agent.config import _load_config

    key, conf = old_tree
    _vault(tmp_path / "data" / ".cobalt_vault", key, {KEY_NAME: "dummy-or-upper"})
    settings = _load_config(conf)
    assert KEY_NAME not in settings.keys
    assert "dummy-or-upper" not in settings.keys.values()


def test_f13_an_openrouter_model_resolves_no_key(old_tree, tmp_path, monkeypatch):
    from cobalt_agent.config import _load_config
    from cobalt_agent.llm import LLM

    key, conf = old_tree
    _vault(tmp_path / "data" / ".cobalt_vault", key, {KEY_NAME: "dummy-or-upper"})
    settings = _load_config(conf)
    settings.keys[KEY_NAME] = "dummy-or-upper"            # placed by hand
    settings.active_profile = {"default": "cloud_claude_4_6_opus"}
    monkeypatch.setenv(KEY_NAME, "dummy-or-env")
    monkeypatch.setattr("cobalt_agent.config.get_config", lambda: settings)

    seen: dict = {}

    class _Reply:
        class _Choice:
            class message:  # noqa: N801 - the LiteLLM response shape
                content = "ok"
        choices = [_Choice()]

    def fake_completion(**kwargs):
        seen.update(kwargs)
        return _Reply()

    monkeypatch.setattr("litellm.completion", fake_completion)
    llm = LLM(role="default")
    assert llm.model_name == "openrouter/anthropic/claude-4.6-opus"
    llm._call_provider([{"role": "user", "content": "hi"}])
    assert seen, "completion was not called"
    assert seen.get("api_key") not in ("dummy-or-upper", "dummy-or-env")


def test_f13_classify_never_imports_cobalt_agent():
    hits = []
    for py in sorted(CLASSIFY_SRC.rglob("*.py")):
        for node in ast.walk(ast.parse(py.read_text())):
            if isinstance(node, ast.Import):
                hits += [f"{py.name}: import {a.name}" for a in node.names
                         if a.name.split(".")[0] == "cobalt_agent"]
            elif isinstance(node, ast.ImportFrom) and (node.module or "").split(".")[0] == "cobalt_agent":
                hits.append(f"{py.name}: from {node.module}")
    assert hits == []


def test_f13_control_gemini_entry_still_injected_and_loaded(old_tree, tmp_path, monkeypatch):
    from cobalt_agent.config import _load_config

    key, conf = old_tree
    vm = _vault(tmp_path / "lower.vault", key, {"gemini_api_key": "dummy-gemini"})
    assert _inject(monkeypatch, vm).llm.api_key == "dummy-gemini"
    _vault(tmp_path / "data" / ".cobalt_vault", key, {"GEMINI_API_KEY": "dummy-gemini-upper"})
    assert _load_config(conf).keys["GEMINI_API_KEY"] == "dummy-gemini-upper"


# -- F2: one host-wide spend ledger, the two paid lines carried ---------------------

def test_f2_two_checkouts_share_one_ledger(tmp_path, monkeypatch):
    from cobalt.classify import config as cfg_mod
    from cobalt.classify.collector import OpenRouterClassifier

    shared = str(tmp_path / "host" / "classify-spend.jsonl")
    clfs = []
    for name in ("checkout-a", "checkout-b"):
        root = tmp_path / name
        root.mkdir()
        monkeypatch.setattr(cfg_mod, "REPO_ROOT", root)
        c = cfg_mod.load_trial_config().model_copy(update={"spend_ledger": shared})
        clfs.append(OpenRouterClassifier(c, pricing=PRICING))
    first, second = clfs
    before = second.ledger.spent()
    first.ledger.record("local-a", 0.001, "returned")
    assert second.ledger.spent() == pytest.approx(before + 0.001)


def test_f2_carried_lines_count_before_any_file(tmp_path, monkeypatch):
    from cobalt.classify.collector import OpenRouterClassifier

    cfg = _trial_cfg(tmp_path, monkeypatch)
    clf = OpenRouterClassifier(cfg, pricing=PRICING)
    assert clf.ledger.spent() == pytest.approx(3.402e-05)
    assert clf.ledger.calls() == 2
    assert not clf.ledger.path.exists()


def test_f2_a_ledger_inside_a_checkout_is_refused(tmp_path, monkeypatch):
    from cobalt.classify import config as cfg_mod

    checkout, wt = tmp_path / "checkout", tmp_path / "wt"
    checkout.mkdir()
    monkeypatch.setattr(cfg_mod, "REPO_ROOT", checkout)
    monkeypatch.setattr(cfg_mod, "WORKTREES_ROOT", wt, raising=False)
    raw = yaml.safe_load(TRIAL_YAML.read_text())
    for value in ("scratch/classify-spend.jsonl",
                  str(checkout / "scratch" / "classify-spend.jsonl"),
                  str(wt / "other" / "classify-spend.jsonl")):
        raw["classify"]["spend_ledger"] = value
        p = tmp_path / "trial.yaml"
        p.write_text(yaml.safe_dump(raw, sort_keys=False))
        with pytest.raises(cfg_mod.ClassifyConfigError, match="outside every checkout"):
            cfg_mod.load_trial_config(p)


def test_f2_control_a_check_never_creates_the_file(tmp_path):
    from cobalt.classify.ledger import Ledger

    led = Ledger(tmp_path / "absent" / "classify-spend.jsonl", cap_usd=5, call_ceiling=10)
    led.check(0.0, calls=1)
    led.stop_if()
    assert not led.path.exists()


# -- F3: the cap is checked on the call's ceiling cost, before the call -------------

def _spend_file(tmp_path: Path, cost: float) -> Path:
    p = tmp_path / "cap" / "classify-spend.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"call_id": "local-x", "cost_usd": cost,
                             "cost_source": "returned", "at": STAMP}) + "\n")
    return p


def _send_with_ledger_at(tmp_path, monkeypatch, cost: float):
    from cobalt.classify.collector import OpenRouterClassifier
    from cobalt.classify.ledger import Ledger

    cfg = _trial_cfg(tmp_path, monkeypatch)
    path = _spend_file(tmp_path, cost)
    stub = Stub((200, b"{}"))
    clf = OpenRouterClassifier(cfg, transport=stub, pricing=PRICING,
                               ledger=Ledger(path, cap_usd=5, call_ceiling=10))
    qset, items = cfg.resolve("FLOOR")
    return clf, stub, path, clf.render(qset, items[0])


def test_f3_a_call_whose_ceiling_cost_passes_the_cap_is_not_sent(tmp_path, monkeypatch, fake_vault):
    from cobalt.classify.collector import ClassifyError

    clf, stub, path, payload = _send_with_ledger_at(tmp_path, monkeypatch, 4.9999)
    before = path.read_text()
    with pytest.raises(ClassifyError, match="spend cap"):
        clf._send(payload, projected_usd=0.00002)
    assert stub.calls == []
    assert path.read_text() == before


def test_f3_control_a_call_well_under_the_cap_is_sent(tmp_path, monkeypatch, fake_vault):
    clf, stub, _, payload = _send_with_ledger_at(tmp_path, monkeypatch, 1.0)
    clf._send(payload, projected_usd=0.00002)
    assert len(stub.calls) == 1


# -- J1: the ROUTE set, its config and the dry run -----------------------------------

def test_j1_route_yaml_loads_with_route_v1_and_its_sha():
    from cobalt.classify import route

    cfg = route.load_route_config()
    qset = cfg.question_set()
    assert qset.id == "ROUTE" and qset.version == 1
    assert list(qset.questions) == ["band", "write_path", "migration", "money", "new_horizon"]
    assert set(qset.questions["band"].options) == {"low", "mid", "high", "unsure"}
    assert re.fullmatch(r"[0-9a-f]{64}", qset.sha256)


def test_j1_dry_run_sends_nothing(tmp_path, monkeypatch, capsys):
    from cobalt.classify import collector as col
    from cobalt.classify import config as cfg_mod

    repo, path = _one_card(tmp_path)
    monkeypatch.setattr(cfg_mod, "REPO_ROOT", repo)

    def no_network(*a, **k):
        raise AssertionError("the transport was called")

    monkeypatch.setattr(col, "urllib_transport", no_network)
    args = _classify_parser().parse_args(["classify", "route", "--card", path, "--dry-run"])
    assert not args.func(args)
    out = capsys.readouterr().out.splitlines()
    assert sum(ln.startswith("ROUTE DRY card=") for ln in out) == 1
    assert sum("cards=1 calls=1" in ln for ln in out) == 1


def test_j1_control_trial_sets_unchanged():
    from cobalt.classify.config import SET_NAMES, load_trial_config

    cfg = load_trial_config()
    assert set(cfg.sets) == set(SET_NAMES)
    assert "ROUTE" not in cfg.sets


# -- F4: the card as launched, answer-bearing header lines removed ------------------

def test_f4_answer_bearing_header_lines_are_never_sent(tmp_path):
    from cobalt.classify import route

    repo = _repo(tmp_path)
    path = f"{PROMPTS}/01-t1-card.md"
    sha = _commit(repo, {path: _card(band="LOW", tip="abcd1234", check_report="c")})
    card = route.load_card(repo, path, launch=sha)
    lines = card.state.splitlines()
    for head in ("TIP:", "REPORT:", "CHECK REPORT:", "BAND:", "MODEL:"):
        assert not any(ln.startswith(head) for ln in lines), head
    assert "JOB: t1" in lines
    assert any("the BAND word" in ln for ln in lines)
    assert card.card_band == "LOW"


def test_f4_a_body_the_guard_would_change_is_refused_with_zero_calls(tmp_path, fake_vault):
    row, stub, cfg, _ = _decide(tmp_path, _answers(), extra=f"- a pasted value {FAKE_KEY}")
    assert row.status == "refused"
    assert stub.calls == []
    assert _lines(cfg.spend_ledger) == []


def test_f4_control_trial_render_keeps_its_state(tmp_path, monkeypatch):
    from cobalt.classify.collector import render_systemone

    cfg = _trial_cfg(tmp_path, monkeypatch)
    qset, items = cfg.resolve("FLOOR")
    assert render_systemone(cfg.model_id, qset, items[0])["state"] == items[0].state


# -- F5: band -> model by the R1532 table only ----------------------------------------

def test_f5_a_low_band_with_high_gates_names_grok(tmp_path, fake_vault):
    row, *_ = _decide(tmp_path, _answers("low", 0.9, write_path=0.9, migration=0.9))
    assert row.status == "ok"
    assert row.model == "grok-4.7" and row.backup == "gpt-5.6-terra"
    assert row.rule_path == "table"
    assert row.gates["write_path"] == 0.9 and row.gates["migration"] == 0.9


def test_f5_unsure_takes_the_higher_band(tmp_path, fake_vault):
    row, *_ = _decide(tmp_path, _answers("unsure"))
    assert row.model == OPUS and row.rule_path == "unsure-higher"


def test_f5_high_names_opus_only(tmp_path, fake_vault):
    row, *_ = _decide(tmp_path, _answers("high"))
    assert row.model == OPUS and row.backup is None


def test_f5_no_threshold_in_route_yaml():
    from cobalt.classify import route

    route.load_route_config()
    text = ROUTE_YAML.read_text()
    assert "min_confidence" not in text
    assert "0.5" not in text


def test_f5_control_trial_yaml_holds_no_routing():
    text = TRIAL_YAML.read_text()
    assert "routing_table" not in text
    assert "grok" not in text


# -- F6: the table's ids are checked at load ------------------------------------------

def _hub(tmp_path: Path, ids: tuple[str, ...]) -> Path:
    rows = "\n".join(f"| `{i}` | `{i.split('-')[0]}` | allow | command | sign |" for i in ids)
    p = tmp_path / "SHADOW-HUB.md"
    p.write_text(f"# hub\n\n## BUILDERS\n\n| id | slug | builder allow | builder command | SIGN |\n"
                 f"|---|---|---|---|---|\n{rows}\n\n## RULES OF THE SEAT\n")
    return p


def test_f6_the_ruled_table_loads_opus_included(tmp_path):
    from cobalt.classify import route

    hub = _hub(tmp_path, ("grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra"))
    cfg = route.load_route_config(shadow_hub=hub)
    assert cfg.routing_table.high.builder == OPUS


def test_f6_sonnet_or_an_unknown_id_refuses_the_load(tmp_path):
    from cobalt.classify import route
    from cobalt.classify.config import ClassifyConfigError

    hub = _hub(tmp_path, ("grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra"))
    for bad in ("claude-sonnet-5-5", "x-model"):
        raw = yaml.safe_load(ROUTE_YAML.read_text())
        raw["route"]["routing_table"]["low"]["builder"] = bad
        p = tmp_path / "route.yaml"
        p.write_text(yaml.safe_dump(raw, sort_keys=False))
        with pytest.raises(ClassifyConfigError, match=bad):
            route.load_route_config(p, shadow_hub=hub)


def test_f6_control_shadow_hub_has_no_opus_builder_row():
    text = SHADOW_HUB.read_text()
    section = text.split("\n## BUILDERS", 1)[1].split("\n## ", 1)[0]
    assert not any(ln.startswith("| `claude-opus-5-5`") for ln in section.splitlines())


# -- J2: one keyed call, one decision row, no card text -----------------------------

DECISION_KEYS = {
    "card_path", "card_blob_sha", "launch_sha", "set_id", "set_sha256", "jev_model_returned",
    "band", "band_probabilities", "band_confidence", "gates", "card_band", "model", "backup",
    "rule_path", "table_sha256", "score_band", "score_components", "rows_band", "latency_ms",
    "cost_usd", "cost_source", "status", "at",
}


def test_j2_one_call_one_decision_row_no_card_text(tmp_path, fake_vault):
    row, stub, cfg, card = _decide(tmp_path, _answers("mid"), restarts="com.x.one com.x.two")
    assert len(stub.calls) == 1
    assert len(_lines(cfg.spend_ledger)) == 1
    rows = _lines(cfg.routing_ledger)
    assert len(rows) == 1
    stored = json.loads(rows[0])
    assert DECISION_KEYS <= set(stored)
    assert stored["status"] == "ok" and stored["card_band"] == "MID"
    assert stored["rows_band"] == 2
    assert stored["score_components"]["S"] == 2 and stored["score_band"] == "UNKNOWN"
    card_lines = [ln.strip() for ln in card.state.splitlines() if len(ln.strip()) >= 6]
    flat = json.dumps(stored)
    assert not [ln for ln in card_lines if ln in flat]


def test_j2_control_classify_path_unchanged(tmp_path, monkeypatch, fake_vault):
    from cobalt.classify.collector import OpenRouterClassifier

    cfg = _trial_cfg(tmp_path, monkeypatch)
    clf = OpenRouterClassifier(cfg, transport=Stub((200, FLOOR_RESPONSE.read_bytes())),
                               pricing=PRICING)
    qset, items = cfg.resolve("FLOOR")
    rec = clf.classify(qset, items[0])
    assert rec.status == "ok"
    assert len(_lines(clf.ledger.path)) == 1


# -- F7: outcome rows from the CHECK DONE line ---------------------------------------

CHECK_DONE = ("CHECK DONE · job: t1 · pass: 2 · tip: t1-tip · house A: none · findings: 5 · "
              "dropped: 0 · held: 3 · fixed: 2 · held unfixed: 1 · open: 4 · house B: none · "
              "ready: YES · decisions: 0 · for Dejan: 0 · tokens: 1234")


def _closed_card(repo: Path, n: int, *, closed: bool = True, when: str = STAMP) -> str:
    path = f"{PROMPTS}/0{n}-c{n}-card.md"
    report = f"{REPORTS}/c{n}-check.md"
    last = CHECK_DONE.replace("job: t1", f"job: c{n}") if closed else "still open, no verdict"
    _commit(repo, {path: _card(f"c{n}", check_report=report),
                   report: f"# check c{n}\n\n| O1 | a finding | HELD |\n\n{last}\n"}, when=when)
    return path


def test_f7_outcome_row_reads_the_check_done_line(tmp_path):
    from cobalt.classify import route

    repo = _repo(tmp_path)
    path = _closed_card(repo, 1)
    ledger = tmp_path / "routing-ledger.jsonl"
    first = json.dumps({"kind": "decision", "card_path": path,
                        "launch_sha": route.launch_sha(repo, path), "band": "mid"})
    ledger.write_text(first + "\n")
    out = route.write_outcome(repo, path, ledger)
    assert out is not None
    rows = _lines(ledger)
    assert rows[0] == first and len(rows) == 2
    o = json.loads(rows[1])
    assert (o["held"], o["fixed"], o["held_unfixed"], o["ready"], o["tokens"]) == (3, 2, 1, "YES", 1234)
    assert {"fix_rounds", "re_passes", "deploy_attempts"} <= set(o)
    assert o["card_path"] == path and o["launch_sha"] == route.launch_sha(repo, path)


def test_f7_no_outcome_before_the_check_closes(tmp_path):
    from cobalt.classify import route

    repo = _repo(tmp_path)
    path = _closed_card(repo, 1, closed=False)
    ledger = tmp_path / "routing-ledger.jsonl"
    ledger.write_text('{"kind": "decision"}\n')
    assert route.write_outcome(repo, path, ledger) is None
    assert _lines(ledger) == ['{"kind": "decision"}']


def test_f7_control_check_done_shape():
    last = [ln for ln in PLIST_CHECK.read_text().splitlines() if ln.strip()][-1]
    assert last.startswith("CHECK DONE")
    for key in ("held:", "held unfixed:", "ready:", "tokens:"):
        assert key in last


# -- F8: the routing ledger outside every checkout; aggregates only in reports -----

def test_f8_a_routing_ledger_inside_a_checkout_is_refused(tmp_path, monkeypatch):
    from cobalt.classify import config as cfg_mod
    from cobalt.classify import route

    checkout, wt = tmp_path / "checkout", tmp_path / "wt"
    checkout.mkdir()
    monkeypatch.setattr(cfg_mod, "REPO_ROOT", checkout)
    monkeypatch.setattr(cfg_mod, "WORKTREES_ROOT", wt)
    raw = yaml.safe_load(ROUTE_YAML.read_text())
    for value in ("scratch/routing-ledger.jsonl",
                  str(checkout / "routing-ledger.jsonl"),
                  str(wt / "other" / "routing-ledger.jsonl")):
        raw["route"]["routing_ledger"] = value
        p = tmp_path / "route.yaml"
        p.write_text(yaml.safe_dump(raw, sort_keys=False))
        with pytest.raises(cfg_mod.ClassifyConfigError, match="outside every checkout"):
            route.load_route_config(p)


def _dec(card: str, *, band: str, card_band: str, model: str, set_sha: str,
         at: datetime, cost: float = 1e-06) -> dict:
    return {"kind": "decision", "card_path": card, "launch_sha": f"launch-{card}",
            "set_sha256": set_sha, "band": band, "card_band": card_band, "model": model,
            "score_band": "UNKNOWN", "rows_band": 4, "status": "ok", "cost_usd": cost,
            "at": at.isoformat()}


def _out(card: str, *, builder: str, held: int) -> dict:
    return {"kind": "outcome", "card_path": card, "launch_sha": f"launch-{card}",
            "stage": "check", "builder": builder, "opus_own_held": held, "fix_rounds": 1,
            "re_passes": None, "tokens": 100}


def test_f8_the_weekly_read_writes_aggregates_only(tmp_path):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    sha = cfg.question_set().sha256
    at = datetime(2026, 1, 5, 12, tzinfo=timezone.utc)
    rows = [_dec("docs/x/c1-card.md", band="low", card_band="LOW", model="grok-4.7", set_sha=sha, at=at),
            _dec("docs/x/c2-card.md", band="high", card_band="HIGH", model=OPUS, set_sha=sha, at=at),
            _out("docs/x/c1-card.md", builder="grok-4.7", held=1)]
    out = route.write_read(route.weekly_read(rows, cfg, week=date(2026, 1, 5)), tmp_path / "reports",
                           date(2026, 1, 5))
    text = out.read_text()
    for value in ("docs/x/c1-card.md", "docs/x/c2-card.md", "launch-docs/x/c1-card.md"):
        assert value not in text


def test_f8_committed_route_yaml_points_outside_the_repo():
    raw = yaml.safe_load(ROUTE_YAML.read_text())["route"]
    for key in ("spend_ledger", "routing_ledger"):
        p = Path(raw[key])
        assert p.is_absolute()
        assert REPO.resolve() not in p.resolve().parents


def test_f8_control_no_routing_ledger_in_the_repo():
    assert not list(REPO.rglob("routing-ledger.jsonl"))


# -- F9: the batch — every failure a status row, exit 0 -------------------------------

def _batch(tmp_path, monkeypatch, repo: Path, stub, **update) -> tuple[list[dict], object]:
    from cobalt.classify import collector as col
    from cobalt.classify import config as cfg_mod
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path, **update)
    monkeypatch.setattr(cfg_mod, "REPO_ROOT", repo)
    monkeypatch.setattr(route, "load_route_config", lambda *a, **k: cfg)
    monkeypatch.setattr(col, "urllib_transport", stub)
    args = _classify_parser().parse_args(["classify", "route", "--day", DAY, "--run"])
    rc = args.func(args)
    assert not rc
    return [json.loads(ln) for ln in _lines(cfg.routing_ledger)], cfg


def test_f9_every_failure_is_a_status_row_and_exit_zero(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    for n in (1, 2, 3, 4):
        _closed_card(repo, n)
    ok = (200, json.dumps(_answers()).encode())
    stub = Stub(ok, OSError("constructed socket failure"), (401, b'{"error":{"message":"no"}}'), ok)
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub)
    assert [r["status"] for r in rows] == ["ok", "transport_error", "auth_error", "auth_error"]
    assert len(stub.calls) == 3


def test_f9_a_cap_refusal_is_a_row(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    _closed_card(repo, 1)
    spend = _spend_file(tmp_path, 4.99999)
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub, spend_ledger=str(spend))
    assert [r["status"] for r in rows] == ["cap_refused"]
    assert stub.calls == []


def test_f9_the_wall_clock_bound_writes_timeout_rows(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    _closed_card(repo, 1)
    _closed_card(repo, 2)
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub, batch_wall_clock_s=0)
    assert [r["status"] for r in rows] == ["timeout", "timeout"]
    assert stub.calls == []


def test_f9_a_card_whose_check_is_open_is_skipped(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    closed = _closed_card(repo, 1)
    still_open = _closed_card(repo, 2, closed=False)
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub, batch_wall_clock_s=0)
    assert [r["card_path"] for r in rows] == [closed]
    assert still_open not in json.dumps(rows)


def test_f9_control_the_trial_run_still_stops_on_a_cap_error(tmp_path, monkeypatch):
    from cobalt.classify import trial
    from cobalt.classify.collector import ClassifyError, OpenRouterClassifier

    cfg = _trial_cfg(tmp_path, monkeypatch)
    clf = OpenRouterClassifier(cfg, pricing=PRICING)
    p = trial.plan(cfg, clf, "FLOOR")

    def capped(*a, **k):
        raise ClassifyError("spend cap: constructed")

    monkeypatch.setattr(clf, "classify", capped)
    with pytest.raises(ClassifyError, match="spend cap"):
        trial.run(p, clf, tag="t")


# -- F10: the retire block is declared before any outcome is read --------------------

def test_f10_route_yaml_without_retire_is_refused(tmp_path):
    from cobalt.classify import route
    from cobalt.classify.config import ClassifyConfigError

    raw = yaml.safe_load(ROUTE_YAML.read_text())
    del raw["route"]["retire"]
    p = tmp_path / "route.yaml"
    p.write_text(yaml.safe_dump(raw, sort_keys=False))
    with pytest.raises(ClassifyConfigError, match="retire"):
        route.load_route_config(p)


def test_f10_rows_before_the_declaration_are_not_compared(tmp_path):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    sha = cfg.question_set().sha256
    before = datetime.combine(cfg.retire.declared - timedelta(days=10), datetime.min.time(),
                              tzinfo=timezone.utc)
    rows = []
    for i in range(3):
        card = f"docs/x/r{i}-card.md"
        rows += [_dec(card, band="low", card_band="LOW", model="grok-4.7", set_sha=sha, at=before),
                 _out(card, builder="grok-4.7", held=i)]
    text = route.weekly_read(rows, cfg, week=None)
    cells = [ln for ln in text.splitlines() if ln.startswith("retire comparison")]
    assert cells
    assert all("n=0 insufficient data" in ln for ln in cells)


def test_f10_control_no_retire_command():
    parser = _classify_parser()
    group = parser._subparsers._group_actions[0].choices["classify"]
    names = [n for a in group._actions if isinstance(a, argparse._SubParsersAction) for n in a.choices]
    assert names and not [n for n in names if "retire" in n]


# -- F11: the weekly read -----------------------------------------------------------------

def test_f11_g7_and_g5_are_printed(tmp_path):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    sha = cfg.question_set().sha256
    at = datetime(2026, 1, 5, 12, tzinfo=timezone.utc)
    rows = [_dec("c1", band="low", card_band="LOW", model="grok-4.7", set_sha=sha, at=at),
            _dec("c2", band="low", card_band="MID", model="grok-4.7", set_sha=sha, at=at),
            _dec("c3", band="high", card_band="HIGH", model=OPUS, set_sha=sha, at=at)]
    lines = route.weekly_read(rows, cfg, week=date(2026, 1, 5)).splitlines()
    g7 = [ln for ln in lines if ln.startswith("G7 ")]
    g5 = [ln for ln in lines if ln.startswith("G5 ")]
    assert len(g7) == 1 and "2 of 3" in g7[0] and "n=3" in g7[0]
    assert len(g5) == 1 and "2 of 3" in g5[0]


def test_f11_a_cell_under_30_prints_no_mean(tmp_path):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    sha = cfg.question_set().sha256
    at = datetime(2026, 1, 5, 12, tzinfo=timezone.utc)
    rows = []
    for i in range(29):
        card = f"c{i}"
        rows += [_dec(card, band="low", card_band="LOW", model="grok-4.7", set_sha=sha, at=at),
                 _out(card, builder="grok-4.7", held=i % 3)]
    text = route.weekly_read(rows, cfg, week=date(2026, 1, 5))
    assert "n=29 insufficient data" in text
    assert "mean" not in text


def test_f11_control_design_keeps_g1_to_g6():
    lines = DESIGN.read_text().splitlines()
    for g in ("G1", "G2", "G3", "G4", "G5", "G6"):
        assert sum(ln.startswith(f"| {g} |") for ln in lines) == 1, g


# -- F1: the call ceiling covers the refresh --------------------------------------------

def test_f1_route_ceiling_covers_the_refresh():
    raw = yaml.safe_load(ROUTE_YAML.read_text())["route"]
    cards = int(re.search(r"(\d+) cards", raw["call_ceiling_source"]).group(1))
    assert raw["call_ceiling_source"].startswith("engine:")
    assert raw["call_ceiling"] >= 2 + 11 + 100 + cards


def test_f1_control_trial_ceiling_unchanged():
    raw = yaml.safe_load(TRIAL_YAML.read_text())["classify"]
    assert raw["call_ceiling"] >= 1014


# -- F12: the fence — no route wrapper under ops/ ----------------------------------------

def test_f12_no_route_wrapper_in_ops():
    hits = []
    for p in sorted((REPO / "ops").rglob("*")):
        if p.is_file():
            try:
                if "classify route" in p.read_text():
                    hits.append(p.name)
            except UnicodeDecodeError:
                continue
    # his 2026-10-18 R1830 (F12): the one keyed wrapper, card 715 W1; no other under ops/
    assert hits == ["jev-route.sh"]


# -- the check of jev-shadow-1015 (CHECK-HUB ## 4): held findings -------------------------

def test_o1_a_closed_card_with_no_launch_commit_is_a_status_row_not_a_crash(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    good = _closed_card(repo, 1)
    path = f"{PROMPTS}/02-c2-card.md"
    report = f"{REPORTS}/c2-check.md"
    _commit(repo, {path: _card("c2", tip="t2-tip", check_report=report),
                   report: f"# check c2\n\n{CHECK_DONE}\n"})
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub)
    # FR-O2 (card 622): a card with no launch commit is not a build card — no row, no crash
    assert [r["card_path"] for r in rows] == [good]


def test_o3_a_check_and_a_deploy_outcome_of_one_card_count_once(tmp_path):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    sha = cfg.question_set().sha256
    at = datetime(2026, 1, 5, 12, tzinfo=timezone.utc)
    rows = []
    for i in range(15):
        card = f"c{i}"
        rows.append(_dec(card, band="low", card_band="LOW", model="grok-4.7", set_sha=sha, at=at))
        for stage in ("check", "deploy"):
            rows.append({**_out(card, builder="grok-4.7", held=i % 3), "stage": stage})
    text = route.weekly_read(rows, cfg, week=date(2026, 1, 5))
    assert "n=15 insufficient data" in text
    assert "mean" not in text


def test_o4_an_openrouter_model_never_reaches_litellm_with_the_environment_key(old_tree, tmp_path, monkeypatch):
    import litellm.main as lm
    from cobalt_agent.config import _load_config
    from cobalt_agent.llm import LLM

    key, conf = old_tree
    _vault(tmp_path / "data" / ".cobalt_vault", key, {})
    settings = _load_config(conf)
    settings.active_profile = {"default": "cloud_claude_4_6_opus"}
    monkeypatch.setenv(KEY_NAME, "dummy-or-env")
    monkeypatch.setattr("cobalt_agent.config.get_config", lambda: settings)
    seen: dict = {}

    def fake_http(**kwargs):
        seen["api_key"] = kwargs.get("api_key")
        raise RuntimeError("constructed stop")

    monkeypatch.setattr(lm.base_llm_http_handler, "completion", fake_http)
    llm = LLM(role="default")
    with pytest.raises(Exception):
        llm._call_provider([{"role": "user", "content": "hi"}])
    assert seen.get("api_key") != "dummy-or-env"


def test_o5_a_spend_ledger_inside_the_main_checkout_is_refused(tmp_path):
    from cobalt.classify import config as cfg_mod

    raw = yaml.safe_load(TRIAL_YAML.read_text())
    raw["classify"]["spend_ledger"] = "/Users/cobalt/cobalt/scratch/classify-spend.jsonl"
    p = tmp_path / "trial.yaml"
    p.write_text(yaml.safe_dump(raw, sort_keys=False))
    with pytest.raises(cfg_mod.ClassifyConfigError, match="outside every checkout"):
        cfg_mod.load_trial_config(p)


def test_o6_a_shadow_check_done_line_gives_its_held_count(tmp_path):
    from cobalt.classify import route

    repo = _repo(tmp_path)
    path = f"{PROMPTS}/01-c1-card.md"
    report = f"{REPORTS}/c1-check.md"
    line = CHECK_DONE.replace("held: 3 ·", "held: 3 (opus-own 2 · house 1) ·")
    _commit(repo, {path: _card("c1", check_report=report), report: f"# check c1\n\n{line}\n"})
    out = route.write_outcome(repo, path, tmp_path / "routing-ledger.jsonl")
    assert out is not None and out["held"] == 3


def test_f9_the_wall_clock_bound_is_reached_at_equality(tmp_path, fake_vault):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    repo, path = _one_card(tmp_path)
    card = route.load_card(repo, path)
    stub = Stub((200, json.dumps(_answers()).encode()))
    ticks = iter([0.0, 5.0])
    rows = route.run_batch(route.Router(cfg, transport=stub, pricing=PRICING), [card],
                           wall_clock_s=5.0, clock=lambda: next(ticks))
    assert [r.status for r in rows] == ["timeout"]
    assert stub.calls == []


def test_f11_the_under_30_read_prints_no_median(tmp_path):
    from cobalt.classify import route

    cfg = _route_cfg(tmp_path)
    sha = cfg.question_set().sha256
    at = datetime(2026, 1, 5, 12, tzinfo=timezone.utc)
    rows = []
    for i in range(29):
        card = f"c{i}"
        rows += [_dec(card, band="low", card_band="LOW", model="grok-4.7", set_sha=sha, at=at),
                 _out(card, builder="grok-4.7", held=i % 3)]
    text = route.weekly_read(rows, cfg, week=date(2026, 1, 5))
    assert "median" not in text


# -- fix round FR-O2 (card 622): the day batch routes BUILD cards only ---------------------

def _check_card(repo: Path, n: int, *, when: str = STAMP) -> str:
    """A separate CHECK card of build card c<n>: the same `CHECK REPORT:`,
    its `TIP:` filled from its first commit (the shape of cards 593, 603, 616)."""
    path = f"{PROMPTS}/0{n}-c{n}-check-card.md"
    _commit(repo, {path: _card(f"c{n}", tip=f"c{n}-tip", check_report=f"{REPORTS}/c{n}-check.md")},
            when=when)
    return path


def test_fr_o2_a_build_and_its_check_card_route_once(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    build = _closed_card(repo, 1)
    check = _check_card(repo, 1)
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub)
    assert [r["card_path"] for r in rows] == [build]
    assert check not in json.dumps(rows)
    assert len(stub.calls) == 1


def test_fr_o2_a_build_launched_on_another_day_is_not_routed(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    path = f"{PROMPTS}/01-c1-card.md"
    report = f"{REPORTS}/c1-check.md"
    _commit(repo, {path: _card("c1")}, when="2026-01-04T12:00:00+00:00")
    _commit(repo, {path: _card("c1", tip="c1-tip", check_report=report),
                   report: f"# check c1\n\n{CHECK_DONE}\n"})
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub)
    assert rows == []
    assert stub.calls == []


def test_fr_o2_deploy_devfix_and_prompt_cards_are_not_routed(tmp_path, monkeypatch, fake_vault):
    repo = _repo(tmp_path)
    report = f"{REPORTS}/c1-check.md"
    base = _card("c1", check_report=report)
    deploy = f"{PROMPTS}/02-deploy-c1-card.md"
    devfix = f"{PROMPTS}/03-c1-devfix-card.md"
    prompt = f"{PROMPTS}/04-c1-prompt-card.md"
    _commit(repo, {
        deploy: base.replace("RESTARTS: none\n", "RESTARTS: none\nTAG: deploy-c1\n"),
        devfix: base.replace("\nTIP:\n", "\nTABLE: system.t1\n"),
        prompt: f"JOB: c1\nTIP:\nCHECK REPORT: {report}\n\n## TASK\n- read only, constructed\n",
        report: f"# check c1\n\n{CHECK_DONE}\n",
    })
    stub = Stub((200, json.dumps(_answers()).encode()))
    rows, _ = _batch(tmp_path, monkeypatch, repo, stub)
    assert rows == []
    assert stub.calls == []


def test_fr_o2_control_the_build_card_still_gets_its_outcome_row(tmp_path):
    from cobalt.classify import route

    repo = _repo(tmp_path)
    build = _closed_card(repo, 1)
    _check_card(repo, 1)
    out = route.write_outcome(repo, build, tmp_path / "routing-ledger.jsonl")
    assert out is not None and out["held"] == 3 and out["card_path"] == build
