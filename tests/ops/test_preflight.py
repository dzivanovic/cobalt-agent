"""ops/desk/preflight.sh — the mechanical PREFLIGHT rows of a build or a check (card 19 worker-steps S2).

A tmp repo stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) and a tmp directory for
/Users/cobalt/cobalt-wt (COBALT_WT_ROOT); the job worktree is a real `git worktree add` of
the tmp repo at BASE. Nothing outside tmp_path is read or written.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
PREFLIGHT = REPO / "ops" / "desk" / "preflight.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
REPORT_REL = "docs/40 - DevDocs/reports/x-job-build.md"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def commit(cwd: Path, msg: str) -> str:
    git(cwd, "add", "-A")
    git(cwd, "commit", "-q", "-m", msg)
    return git(cwd, "rev-parse", "--short=8", "HEAD")


@pytest.fixture
def job(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    (repo / "src").mkdir(parents=True)
    (repo / "docs").mkdir()
    (wt / "beta").mkdir(parents=True)
    (repo / "src" / "a.py").write_text("A = 1\n")
    (repo / "docs" / "x.md").write_text("doc\n")
    (repo / ".gitignore").write_text(".env\n")
    git(repo, "init", "-q", "-b", "main")
    base = commit(repo, "base")
    job_wt = wt / "x-job"
    git(repo, "worktree", "add", "-q", "-b", "ops/x-job", str(job_wt), base)
    prompts = repo / "docs" / "40 - DevDocs" / "prompts" / "2026-01-02"
    prompts.mkdir(parents=True)
    card = prompts / "01-x-job-card.md"
    env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo), **GIT_ENV)
    return wt, repo, job_wt, base, card, env


def write_card(card: Path, job_wt: Path, base: str, tip: str = "") -> None:
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {base}\nTIP: {tip}\nREPORT: {job_wt / REPORT_REL}\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
    )


def built(job_wt: Path, last: str) -> str:
    """A src commit (the tip), then the build report as a docs-only commit above it."""
    (job_wt / "src" / "a.py").write_text("A = 2\n")
    tip = commit(job_wt, "fix(x-job): a")
    report = job_wt / REPORT_REL
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(f"# report\n\n{last.format(tip=tip)}\n\n")
    commit(job_wt, "docs(x-job): build report")
    return tip


GOOD_LAST = "BUILT · job: x-job · tip: {tip} | on base | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0"


def preflight(env: dict, kind: str, card: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(PREFLIGHT), kind, str(card)], env=env, capture_output=True, text=True, timeout=120
    )


def last_line(done: subprocess.CompletedProcess) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.strip()][-1]


def rules(done: subprocess.CompletedProcess) -> list[str]:
    return [ln.split(" · ")[0] for ln in done.stdout.splitlines() if " · " in ln and not ln.startswith(" ")]


def test_a_build_at_base_passes_with_every_row(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    done = preflight(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    assert rules(done) == ["clock", "status", "head", "diff", "main repo", "env here", "env anywhere"]
    assert "## ops/x-job" in done.stdout


def test_a_build_on_its_own_wip_commit_passes(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / "tests").mkdir()
    (job_wt / "tests" / "test_a.py").write_text("def test_a():\n    assert False\n")
    commit(job_wt, "wip(x-job): red")
    done = preflight(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"


def test_a_worktree_on_another_branch_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    git(job_wt, "checkout", "-q", "-b", "other")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: status"


def test_an_uncommitted_file_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / "src" / "b.py").write_text("B = 1\n")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: status"


def test_a_build_on_a_foreign_commit_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / "src" / "a.py").write_text("A = 3\n")
    commit(job_wt, "feat(x-job): not a wip")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"


def test_an_env_in_this_worktree_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / ".env").write_text("COBALT_TEST_CONSTRUCTED=1\n")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: env here"


def test_an_env_in_a_sibling_worktree_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (wt / "beta" / ".env").write_text("COBALT_TEST_CONSTRUCTED=1\n")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: env anywhere"


def test_a_check_on_a_built_branch_passes_with_a_docs_only_commit_above_tip(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    assert rules(done) == ["clock", "status", "head", "env here", "env anywhere", "report", "range"]
    assert "fix(x-job): a" in done.stdout  # the range, quoted


def test_a_check_whose_report_ends_failed_fails(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, "FAILED: W — x")
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: report"


def test_a_check_whose_report_is_short_of_three_self_checks_fails(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST.replace("self-check: 3 of 3", "self-check: 2 of 3"))
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: report"


def test_a_check_with_a_src_commit_above_tip_fails(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    write_card(card, job_wt, base, tip)
    (job_wt / "src" / "a.py").write_text("A = 4\n")
    commit(job_wt, "fix(x-job): after the tip")
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"


@pytest.mark.parametrize("args", [[], ["build"], ["deploy", "x"], ["build", "/no/such/card.md"]])
def test_a_bad_call_is_refused(job, args):
    wt, repo, job_wt, base, card, env = job
    done = subprocess.run(
        ["sh", str(PREFLIGHT), *args], env=env, capture_output=True, text=True, timeout=60
    )
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
