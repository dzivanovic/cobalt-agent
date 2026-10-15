"""R5 — the trial runner. `--dry-run` sends nothing; `--run` over a fake
transport only (a CONSTRUCTED fake key; no socket).

The fake transport answers every System One request from the request
itself: the envelope (`id`, `model`, `provider`, `usage`) is the
published-schema fixture's; each asked question gets a schema-valid
answer of its own type. No live call exists in this build.
"""

from __future__ import annotations

import json
import shutil
import threading
from pathlib import Path

import pytest

from cobalt.classify import collector as col
from cobalt.classify import trial as tr
from cobalt.classify.collector import KEY_NAME, ClassifyError, OpenRouterClassifier
from cobalt.classify.config import load_trial_config
from cobalt.classify.models import CallRecord
from cobalt.redact.secrets import LiteralGuard

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "classify"
ENTRY = FIXTURES / "openrouter-model-entry.real-shape.json"
ENVELOPE = json.loads((FIXTURES / "openrouter-systemone-response.openapi-example.json").read_text())
FAKE_KEY = "sk-or-v1-TESTONLY-" + "0123456789abcdef" * 2


def _answer(q: dict) -> dict:
    if q["type"] == "choice":
        return {"type": "choice", "choice": next(iter(q["criteria"]))}
    if q["type"] == "score":
        return {"type": "score", "score": 0}
    return {"type": "noul", "noul": 0.5}


class EchoTransport:
    """A schema-valid answer to whatever was asked; records every call."""

    def __init__(self):
        self.calls: list[dict] = []
        self._lock = threading.Lock()

    def __call__(self, method, url, headers, body, timeout):
        req = json.loads(body)
        with self._lock:
            self.calls.append({"url": url, "headers": dict(headers), "body": req})
        resp = {**ENVELOPE, "answers": {k: _answer(q) for k, q in req["questions"].items()}}
        return 200, json.dumps(resp).encode()


class NoTransport:
    def __call__(self, *a, **k):
        raise AssertionError("a dry-run touched the transport")


@pytest.fixture
def fake_vault(monkeypatch):
    monkeypatch.setattr("cobalt.redact.secrets.read_secret",
                        lambda name: FAKE_KEY if name == KEY_NAME else None)
    monkeypatch.setattr("cobalt.redact.guard.load_literals",
                        lambda *a, **k: LiteralGuard({KEY_NAME: FAKE_KEY}, available=True))


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    from cobalt.classify import config as cfg_mod

    real_reports = sorted((cfg_mod.REPO_ROOT / "docs" / "40 - DevDocs" / "reports").glob("day-open-*.md"))[:2]
    monkeypatch.setattr(cfg_mod, "REPO_ROOT", tmp_path)
    c = load_trial_config()
    c = c.model_copy(update={"spend_ledger": str(tmp_path / "scratch" / "classify-spend.jsonl"), "carried_spend": []})
    dest = tmp_path / c.entry_record
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ENTRY, dest)
    reports = tmp_path / "docs" / "40 - DevDocs" / "reports"
    reports.mkdir(parents=True)
    for p in real_reports:
        shutil.copyfile(p, reports / p.name)
    return c


def _clf(cfg, transport):
    return OpenRouterClassifier(cfg, transport=transport)


# -- the plan ------------------------------------------------------------------

@pytest.mark.parametrize("name", ["FLOOR", "S1", "S2", "S3", "T9", "L20"])
@pytest.mark.parametrize("mode", ["single", "parallel", "sequential"])
def test_the_dry_run_sends_nothing_and_counts_every_call(cfg, name, mode):
    clf = _clf(cfg, NoTransport())
    plan = tr.plan(cfg, clf, name, reps=2, mode=mode)
    qset, items = cfg.resolve(name)
    per_item = 1 if mode == "single" else len(qset.questions)
    assert plan.calls == len(plan.items) * 2 * per_item
    assert len(plan.items) + len(plan.skipped) == len(items)
    summary = tr.dry_run(plan, clf)
    assert f"calls={plan.calls} " in summary
    assert not clf.ledger.path.exists()                  # a dry-run never creates the ledger


def test_gated_is_l20_in_its_four_levels(cfg):
    clf = _clf(cfg, NoTransport())
    plan = tr.plan(cfg, clf, "L20", reps=1, mode="gated")
    assert plan.calls == len(plan.items) * 4
    levels = [list(s.questions) for s in plan.shapes]
    assert [len(x) for x in levels] == [4, 3, 3, 10]
    assert sum(levels, []) == list(cfg.resolve("L20")[0].questions)


def test_gated_on_a_set_without_levels_is_refused(cfg):
    with pytest.raises(ClassifyError, match="level"):
        tr.plan(cfg, _clf(cfg, NoTransport()), "S1", reps=1, mode="gated")


def test_questions_n_takes_the_first_n(cfg):
    plan = tr.plan(cfg, _clf(cfg, NoTransport()), "L20", reps=1, mode="single", questions=5)
    assert list(plan.shapes[0].questions) == list(cfg.resolve("L20")[0].questions)[:5]


def test_reverse_reverses_the_question_order_and_nothing_else(cfg):
    clf = _clf(cfg, NoTransport())
    fwd = tr.plan(cfg, clf, "L20", reps=1, mode="single")
    rev = tr.plan(cfg, clf, "L20", reps=1, mode="single", reverse=True)
    a = clf.render(fwd.shapes[0], fwd.items[0])
    b = clf.render(rev.shapes[0], rev.items[0])
    assert list(b["questions"]) == list(reversed(list(a["questions"])))
    assert b["questions"] == a["questions"] and b["state"] == a["state"] and b["model"] == a["model"]


def test_a_t9_file_carrying_the_key_is_skipped_and_counted(cfg, tmp_path):
    reports = tmp_path / "docs" / "40 - DevDocs" / "reports"
    (reports / "day-open-2099-01-01.md").write_text(f"verdict green; stray {FAKE_KEY} pasted here\n")
    clf = _clf(cfg, NoTransport())
    plan = tr.plan(cfg, clf, "T9", reps=1, mode="single")
    assert [s.id for s in plan.skipped] == ["day-open-2099-01-01"]
    assert "day-open-2099-01-01" not in [i.id for i in plan.items]
    assert FAKE_KEY not in tr.dry_run(plan, clf)


# -- the run (fake transport) ------------------------------------------------------

def test_run_floor_three_reps_writes_three_valid_lines_in_scratch(cfg, fake_vault, tmp_path):
    t = EchoTransport()
    clf = _clf(cfg, t)
    plan = tr.plan(cfg, clf, "FLOOR", reps=3, mode="single")
    plan.items = plan.items[:1]
    out, summary = tr.run(plan, clf, tag="t1")
    lines = out.read_text().splitlines()
    assert len(lines) == 3 == len(t.calls)
    for ln in lines:
        CallRecord.model_validate_json(ln)
        assert FAKE_KEY not in ln
    assert (tmp_path / "scratch").resolve() in out.resolve().parents
    assert out.name.startswith("classify-results-FLOOR-t1-")
    assert "calls=3 ok=3 invalid=0 http_error=0" in summary and "p50=" in summary


def test_a_run_whose_projection_crosses_the_cap_calls_nothing_writes_nothing(cfg, fake_vault, tmp_path):
    t = EchoTransport()
    tiny = cfg.model_copy(update={"spend_cap_usd": 1e-12})
    clf = _clf(tiny, t)
    plan = tr.plan(tiny, clf, "FLOOR", reps=1, mode="single")
    with pytest.raises(ClassifyError, match="cap"):
        tr.run(plan, clf, tag="over")
    assert t.calls == []
    assert not list((tmp_path / "scratch").glob("classify-results-*"))


def test_a_run_over_the_call_ceiling_calls_nothing(cfg, fake_vault):
    t = EchoTransport()
    low = cfg.model_copy(update={"call_ceiling": 2})
    clf = _clf(low, t)
    plan = tr.plan(low, clf, "FLOOR", reps=1, mode="single")
    with pytest.raises(ClassifyError, match="ceiling"):
        tr.run(plan, clf, tag="ceil")
    assert t.calls == []


def test_parallel_over_thirteen_questions_issues_thirteen_calls(cfg, fake_vault):
    t = EchoTransport()
    clf = _clf(cfg, t)
    plan = tr.plan(cfg, clf, "L20", reps=1, mode="parallel", questions=13)
    plan.items = plan.items[:1]
    _, summary = tr.run(plan, clf, tag="par")
    assert len(t.calls) == 13
    assert sorted(next(iter(c["body"]["questions"])) for c in t.calls) == sorted(plan.shapes_ids())
    assert "wall_ms" in summary


def test_percentiles_are_nearest_rank():
    xs = [float(i) for i in range(1, 101)]
    assert tr.percentile(xs, 50) == 50.0
    assert tr.percentile(xs, 95) == 95.0
    assert tr.percentile(xs, 99) == 99.0
    assert tr.percentile([7.0], 99) == 7.0


# -- the CLI ------------------------------------------------------------------------

def test_the_cli_dry_run_prints_one_line_and_calls_nothing(cfg, monkeypatch, capsys):
    from cobalt.classify import cli as ccli

    monkeypatch.setattr(ccli, "load_trial_config", lambda: cfg)
    monkeypatch.setattr(col, "urllib_transport", NoTransport())

    class A:
        set, reps, mode, questions, reverse, dry_run, run, tag = "S3", 1, "single", None, False, True, False, None

    ccli.cmd_trial(A())
    out = capsys.readouterr().out.strip().splitlines()
    assert len(out) == 1 and out[0].startswith("DRY set=S3 ")
