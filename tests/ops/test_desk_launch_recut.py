"""desk-launch.sh recut "<deploy card>" (card 2026-10-03/03 adoption-scripts, row L5).

A deploy whose gate FAILED is recut in ONE call: gate-clean.sh on the failed gate; new BRANCH,
WORKTREE, TAG (`-attempt<n>`, n = the highest attempt present + 1) and REPORT
(`deploy-<…>-attempt<n>.md`) on the card; the card committed by desk-commit.sh; the desk row
by desk-row.sh; then the `deploy` kind's launch on the recut card. DESK_LAUNCH_DRY=1 makes
that last launch dry, as it does for every kind.

A tmp repo stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) with the three hub files, a
job branch whose check report is committed and clean, a deploy card, its failed gate
(a real worktree holding one merge) and a FAILED deploy report; a tmp directory stands in
for /Users/cobalt/cobalt-wt (COBALT_WT_ROOT); a stub `claude` on PATH records its cwd.
"""

from __future__ import annotations

import datetime
import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
FAILED_LINE = "FAILED: gate — G (c) — tests/cobalt/test_x.py::test_y · rollback: not used"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def has_ref(repo: Path, ref: str) -> bool:
    return subprocess.run(
        ["git", "-C", str(repo), "show-ref", "--verify", "--quiet", ref], capture_output=True,
    ).returncode == 0


class Desk:
    def __init__(self, tmp_path: Path):
        root = tmp_path.resolve()
        self.wt = root / "wt"
        self.repo = root / "repo"
        self.wt.mkdir()
        self.repo.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        for hub in ("BUILD-HUB.md", "CHECK-HUB.md", "DEPLOY-HUB.md"):
            shutil.copy(HUBS / hub, self.prompts / hub)
        # today's desk report, where desk-row.sh appends (constructed rows only)
        self.today = self.reports / f"cto-{datetime.date.today():%Y-%m-%d}.md"
        self.today.write_text(
            "# cto (constructed)\n\n| # | time | row | status |\n|---|---|---|---|\n"
            "| R1 | 07:00 ET | a constructed row. | RECORD |\n\n## §5 CURRENT\n"
        )
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")

        # the job: a code commit (the tip), its build report (a docs-only head), its clean check
        self.job_wt = self.wt / "x-job"
        git(self.repo, "worktree", "add", "-q", "-b", "ops/x-job", str(self.job_wt), "main")
        (self.job_wt / "src").mkdir()
        (self.job_wt / "src" / "x.py").write_text("X = 1\n")
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", "code")
        self.tip = git(self.job_wt, "rev-parse", "--short=8", "HEAD")
        (self.job_wt / "docs" / "x-build.md").write_text("BUILT\n")
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", "report")
        self.head = git(self.job_wt, "rev-parse", "--short=8", "HEAD")
        self.check = self.reports / "x-job-check.md"
        self.check.write_text(
            f"# check\n\nCHECK DONE · job: x-job · pass: 1 · tip: {self.tip} · held unfixed: 0 · "
            "open: 0 · ready: YES · decisions: 0 · for Dejan: 0\n"
        )

        self.report = self.reports / "deploy-2026-01-02-1.md"
        self.card = self.prompts / "2026-01-02" / "02-x-deploy-card.md"
        self.card.write_text(
            "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
            f"BASE: main\nTIP: {self.head}\nREPORT: {self.report}\nRULINGS: none\n"
            "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n\n"
            "| # | branch | code tip | branch head | check report | its stop line must carry |\n"
            "|---|---|---|---|---|---|\n"
            f"| 1 | `ops/x-job` | `{self.tip}` | `{self.head}` | `{self.check}` | `held unfixed: 0` and `ready: YES` |\n\n"
            "## MARKERS\n## SMOKE READS\n"
        )
        self.commit("cards and checks")

        # the failed attempt: its gate holds one merge of the job; its report ends FAILED
        self.gate = self.wt / "x-gate"
        git(self.repo, "worktree", "add", "-q", "-b", "deploy/x-deploy", str(self.gate), "main")
        git(self.gate, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
        self.write_report(FAILED_LINE)

        stub = root / "bin"
        stub.mkdir()
        self.calls = root / "claude-calls"
        (stub / "claude").write_text(
            '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
            f'printf "%s\\n" "$PWD" >> "{self.calls}"\n'
        )
        (stub / "claude").chmod(0o755)
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{stub}:{os.environ['PATH']}", DESK_LAUNCH_DRY="1", **GIT_ENV,
        )

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def write_report(self, last: str) -> None:
        self.report.write_text(f"# deploy (constructed)\n\n## RECORDS\n- constructed\n\n{last}\n\n")
        self.commit("deploy report")

    def recut(self, *extra: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["sh", str(LAUNCH), "recut", str(self.card), *extra], env=self.env,
            capture_output=True, text=True, timeout=120,
        )

    def header(self) -> dict[str, str]:
        out = {}
        for line in self.card.read_text().splitlines():
            if not line.strip():
                break
            key, _, value = line.partition(": ")
            out[key] = value
        return out

    def called(self) -> list[str]:
        return self.calls.read_text().splitlines() if self.calls.exists() else []


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def index_of(lines: list[str], pattern: str) -> int:
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            return i
    raise AssertionError(f"no line matches {pattern!r}:\n" + "\n".join(lines))


def test_a_failed_deploy_is_recut_and_its_launch_printed_in_order(desk):
    old_card = desk.card.read_text()
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    out = done.stdout.splitlines()
    new_report = desk.reports / "deploy-2026-01-02-1-attempt2.md"

    # the failed gate is cleaned first (gate-clean.sh's own lines)
    i_clean = out.index(f"gate-clean: {desk.gate} and deploy/x-deploy removed")
    assert not desk.gate.exists() and not has_ref(desk.repo, "refs/heads/deploy/x-deploy")

    # the new values, the commit, the row, the launch line — in that order
    i_values = out.index("RECUT: x-deploy attempt 2")
    assert out[i_values + 1:i_values + 5] == [
        "BRANCH: deploy/x-deploy -> deploy/x-deploy-attempt2",
        "WORKTREE: x-gate -> x-gate-attempt2",
        "TAG: x-tag -> x-tag-attempt2",
        f"REPORT: {desk.report} -> {new_report}",
    ]
    i_commit = index_of(out, r"docs\(desk\): RECUT x-deploy attempt 2")
    i_row = index_of(out, r"^\| R2 \| \d\d:\d\d ET \| RECUT x-deploy attempt 2 — "
                     + re.escape(FAILED_LINE) + r" \| RECORD \|$")
    i_launch = out.index(f"git -C {desk.repo} worktree add -b deploy/x-deploy-attempt2 {desk.wt}/x-gate-attempt2 main")
    assert i_clean < i_values < i_commit < i_row < i_launch
    assert out[i_launch + 1] == f"cd {desk.repo}"
    assert out[i_launch + 2].startswith("claude --bg ")
    assert done.stderr.splitlines()[-1] == f'WATCH: sh {LAUNCH.parent}/desk-watch.sh deploy "{desk.card}"'

    # the card: four values changed, nothing else; committed by desk-commit.sh
    header = desk.header()
    assert (header["BRANCH"], header["WORKTREE"], header["TAG"], header["REPORT"]) == (
        "deploy/x-deploy-attempt2", "x-gate-attempt2", "x-tag-attempt2", str(new_report))
    assert desk.card.read_text() == (
        old_card.replace("BRANCH: deploy/x-deploy\n", "BRANCH: deploy/x-deploy-attempt2\n")
        .replace("WORKTREE: x-gate\n", "WORKTREE: x-gate-attempt2\n")
        .replace("TAG: x-tag\n", "TAG: x-tag-attempt2\n")
        .replace(f"REPORT: {desk.report}\n", f"REPORT: {new_report}\n"))
    assert git(desk.repo, "log", "-1", "--format=%s", "--", str(desk.card)) == "docs(desk): RECUT x-deploy attempt 2"
    assert git(desk.repo, "status", "--porcelain", "--", str(desk.card)) == ""
    # the desk row, in today's desk report
    assert f"| RECUT x-deploy attempt 2 — {FAILED_LINE} | RECORD |" in desk.today.read_text()
    # a dry launch: no session, no new gate
    assert desk.called() == []
    assert not (desk.wt / "x-gate-attempt2").exists()


def refused(desk: Desk, done: subprocess.CompletedProcess, text: str, old_card: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert "WATCH:" not in done.stdout + done.stderr
    assert desk.called() == []
    assert desk.card.read_text() == old_card
    assert git(desk.repo, "status", "--porcelain", "--", str(desk.card)) == ""
    assert "RECUT" not in desk.today.read_text()


def test_a_deploy_that_did_not_fail_is_refused(desk):
    desk.write_report("DEPLOYED · job: x-deploy · tag: x-tag")
    old = desk.card.read_text()
    refused(desk, desk.recut(), "recut: the deploy report does not end FAILED", old)
    assert desk.gate.is_dir()


def test_a_deploy_whose_rollback_ran_is_refused(desk):
    desk.write_report("FAILED: 4.3 — merge — x · rollback: used — migrations applied: none — aset: UP — radar: UP")
    old = desk.card.read_text()
    refused(desk, desk.recut(), "recut: the failed deploy names 'rollback: used'", old)
    assert desk.gate.is_dir()


def test_main_holding_the_gate_branch_is_refused_by_gate_clean(desk):
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "deploy/x-deploy")
    old = desk.card.read_text()
    refused(desk, desk.recut(), "main contains the gate's head", old)
    assert desk.gate.is_dir()


def test_an_attempt_name_already_present_is_never_reused(desk):
    """X5: a branch deploy/x-deploy-attempt2 already stands: the recut is attempt 3."""
    git(desk.repo, "branch", "deploy/x-deploy-attempt2", "main")
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    assert "RECUT: x-deploy attempt 3" in done.stdout.splitlines()
    header = desk.header()
    assert header["BRANCH"] == "deploy/x-deploy-attempt3"
    assert header["REPORT"] == str(desk.reports / "deploy-2026-01-02-1-attempt3.md")


def test_a_recut_of_a_recut_counts_from_the_cards_own_attempt(desk):
    """The card already carries attempt 2: the next is attempt 3, the suffix never doubled."""
    desk.card.write_text(desk.card.read_text()
                         .replace("BRANCH: deploy/x-deploy\n", "BRANCH: deploy/x-deploy-attempt2\n")
                         .replace("WORKTREE: x-gate\n", "WORKTREE: x-gate-attempt2\n")
                         .replace("TAG: x-tag\n", "TAG: x-tag-attempt2\n"))
    desk.commit("the card at attempt 2")
    git(desk.repo, "worktree", "move", str(desk.gate), str(desk.wt / "x-gate-attempt2"))
    git(desk.repo, "branch", "-m", "deploy/x-deploy", "deploy/x-deploy-attempt2")
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    header = desk.header()
    assert (header["BRANCH"], header["WORKTREE"], header["TAG"]) == (
        "deploy/x-deploy-attempt3", "x-gate-attempt3", "x-tag-attempt3")
    assert header["REPORT"] == str(desk.reports / "deploy-2026-01-02-1-attempt3.md")


@pytest.mark.parametrize("extra", [("E3",), ("PASS-2",), ("E3", "PASS-2")])
def test_card03_l5_a_third_argument_is_refused_before_anything_runs(desk, extra):
    """AMENDED 10-03 (judge, ASK DESK 13): an ignored argument is a guess (L1)."""
    old = desk.card.read_text()
    done = desk.recut(*extra)
    refused(desk, done, "recut takes one argument, the card", old)
    # before anything: not even the desk-size guard's line
    assert (done.stdout, done.stderr) == ("", "REFUSED: recut takes one argument, the card\n")
    assert desk.gate.is_dir() and has_ref(desk.repo, "refs/heads/deploy/x-deploy")


def test_the_header_names_the_recut_kind():
    text = LAUNCH.read_text()
    assert 'desk-launch.sh recut "<absolute deploy card path>"' in text
