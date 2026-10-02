"""gate-clean.sh and job-clean.sh (card 18 desk-tools-b, row B2).

Every run points the scripts at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT) and a tmp directory standing in for /Users/cobalt/cobalt-wt
(COBALT_WT_ROOT). The gate is a real git worktree of the tmp repo holding one
merge of a job branch; `.env` files are constructed. `claude` is a stub on PATH.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
GATE_CLEAN = REPO / "ops" / "desk" / "gate-clean.sh"
JOB_CLEAN = REPO / "ops" / "desk" / "job-clean.sh"
LOCK_NAME = ".cobalt_dev.lock"
CONSTRUCTED_ENV = "COBALT_TEST_CONSTRUCTED=1\n"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def has_branch(repo: Path, name: str) -> bool:
    return bool(git(repo, "branch", "--list", name))


class Desk:
    def __init__(self, tmp_path: Path, *, merge_in_gate: bool = True) -> None:
        root = tmp_path.resolve()
        self.repo = root / "repo"
        self.wt = root / "wt"
        self.repo.mkdir()
        self.wt.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts" / "2026-01-02"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        self.prompts.mkdir(parents=True)
        self.reports.mkdir(parents=True)
        (self.repo / "a.txt").write_text("a\n")
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "base")

        # a job branch in its own worktree, one commit
        self.job_wt = self.wt / "x-job"
        git(self.repo, "worktree", "add", "-q", "-b", "ops/x-job", str(self.job_wt), "main")
        (self.job_wt / "job.txt").write_text("job\n")
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", "job")

        # the gate: cut from main, holding one merge of the job
        self.gate = self.wt / "x-gate"
        git(self.repo, "worktree", "add", "-q", "-b", "deploy/x-set", str(self.gate), "main")
        if merge_in_gate:
            git(self.gate, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")

        self.report = self.reports / "deploy-x-set.md"
        self.report.write_text("# deploy\n\n(run in progress)\nFAILED: gate — x\n\n")
        self.card = self.prompts / "02-deploy-x-set-card.md"
        self.card.write_text(
            "JOB: x-set\nLADDER: OFF-LADDER\nBRANCH: deploy/x-set\nWORKTREE: x-gate\nBASE: main\n"
            "TIP: 00000000\n"
            f"REPORT: {self.report}\nRULINGS: none\nTAG: x-tag\nMIGRATIONS: none\nSET: xset\n\n"
            "## SHIPS\n## MARKERS\n## SMOKE READS\n"
        )
        self.job_card = self.prompts / "01-x-job-card.md"
        self.job_card.write_text(
            "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\nBASE: 00000000\n"
            "TIP:\nREPORT: x\nCHECK REPORT:\nHOUSE B:\nTREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n"
            "## ROWS\n"
        )
        self.main = git(self.repo, "rev-parse", "main")

        stub = root / "bin"
        stub.mkdir()
        (stub / "claude").write_text(f'#!/bin/sh\nprintf "%s\\n" "$*" >> "{root / "claude-calls"}"\n')
        (stub / "claude").chmod(0o755)
        self.env = dict(
            os.environ, COBALT_REPO_ROOT=str(self.repo), COBALT_WT_ROOT=str(self.wt),
            PATH=f"{stub}{os.pathsep}{os.environ['PATH']}", **GIT_ENV,
        )

    def run(self, script: Path, card: Path) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["sh", str(script), str(card)], env=self.env, capture_output=True, text=True, timeout=120
        )

    def gate_stands(self) -> bool:
        return self.gate.is_dir() and has_branch(self.repo, "deploy/x-set")

    def job_stands(self) -> bool:
        return self.job_wt.is_dir() and has_branch(self.repo, "ops/x-job")


# ---- gate-clean.sh --------------------------------------------------------------------


def test_a_failed_gate_is_removed_and_main_is_untouched(tmp_path):
    desk = Desk(tmp_path)
    done = desk.run(GATE_CLEAN, desk.card)
    assert done.returncode == 0, done.stderr
    lines = done.stdout.strip().splitlines()
    assert lines[-1] == f"gate-clean: {desk.gate} and deploy/x-set removed"
    assert any("worktree remove --force" in line and str(desk.gate) in line for line in lines[:-1])
    assert any("branch -D deploy/x-set" in line for line in lines[:-1])
    assert not desk.gate.exists()
    assert not has_branch(desk.repo, "deploy/x-set")
    assert git(desk.repo, "rev-parse", "main") == desk.main
    # the job's own worktree and branch are not the gate's
    assert desk.job_stands()


def test_a_gate_with_no_merge_yet_is_removed(tmp_path):
    """The gate's head is main's own commit (on main's first-parent line): nothing landed."""
    desk = Desk(tmp_path, merge_in_gate=False)
    done = desk.run(GATE_CLEAN, desk.card)
    assert done.returncode == 0, done.stderr
    assert not desk.gate.exists()
    assert not has_branch(desk.repo, "deploy/x-set")


def _gate_refused(desk: Desk) -> None:
    done = desk.run(GATE_CLEAN, desk.card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED" in done.stderr
    assert "worktree remove" not in done.stdout
    assert desk.gate_stands()
    assert git(desk.repo, "rev-parse", "main") == desk.main


def test_a_deployed_report_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.report.write_text("# deploy\nDEPLOYED · x\n")
    _gate_refused(desk)


def test_an_in_progress_report_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.report.write_text("# deploy\nFAILED: earlier\n(run in progress — next step under ## CONTINUE)\n")
    _gate_refused(desk)


def test_a_missing_report_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.report.unlink()
    _gate_refused(desk)


def test_the_deploy_tag_existing_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "tag", "x-tag", "main")
    _gate_refused(desk)


def test_the_pre_tag_existing_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "tag", "pre-x-set", "main")
    _gate_refused(desk)


def test_an_env_in_the_gate_is_refused(tmp_path):
    desk = Desk(tmp_path)
    (desk.gate / ".env").write_text(CONSTRUCTED_ENV)
    _gate_refused(desk)
    assert (desk.gate / ".env").read_text() == CONSTRUCTED_ENV


def test_a_lock_directory_owned_by_the_gate_is_refused(tmp_path):
    desk = Desk(tmp_path)
    (desk.wt / LOCK_NAME).mkdir()
    (desk.wt / LOCK_NAME / "owner").write_text("x-gate\n")
    _gate_refused(desk)


def test_main_holding_the_gate_merge_is_refused(tmp_path):
    """The gate's merge landed on main: its commits are main's now, never the gate's to drop."""
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "deploy/x-set")
    desk.main = git(desk.repo, "rev-parse", "main")
    _gate_refused(desk)


@pytest.mark.parametrize("bad", ["../x-gate", "/abs/x-gate", "a/b", ".hidden", "agy-trial", ""])
def test_a_worktree_outside_the_pattern_is_refused(tmp_path, bad):
    desk = Desk(tmp_path)
    desk.card.write_text(desk.card.read_text().replace("WORKTREE: x-gate", f"WORKTREE: {bad}"))
    _gate_refused(desk)


def test_a_symlinked_worktree_name_is_refused(tmp_path):
    desk = Desk(tmp_path)
    (desk.wt / "link-gate").symlink_to(desk.gate)
    desk.card.write_text(desk.card.read_text().replace("WORKTREE: x-gate", "WORKTREE: link-gate"))
    _gate_refused(desk)
    assert (desk.wt / "link-gate").is_symlink()


def test_a_worktree_on_another_branch_is_refused(tmp_path):
    """The card's BRANCH must be the branch checked out in its WORKTREE."""
    desk = Desk(tmp_path)
    desk.card.write_text(desk.card.read_text().replace("WORKTREE: x-gate", "WORKTREE: x-job"))
    _gate_refused(desk)
    assert desk.job_stands()


def test_a_non_deploy_branch_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.card.write_text(
        desk.card.read_text().replace("BRANCH: deploy/x-set", "BRANCH: ops/x-job").replace(
            "WORKTREE: x-gate", "WORKTREE: x-job"
        )
    )
    done = desk.run(GATE_CLEAN, desk.card)
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert desk.job_stands()


# ---- job-clean.sh ---------------------------------------------------------------------


def test_a_merged_clean_job_is_removed(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    done = desk.run(JOB_CLEAN, desk.job_card)
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip().splitlines()[-1] == f"job-clean: {desk.job_wt} and ops/x-job removed"
    assert not desk.job_wt.exists()
    assert not has_branch(desk.repo, "ops/x-job")
    assert desk.gate_stands()


def _job_refused(desk: Desk) -> None:
    done = desk.run(JOB_CLEAN, desk.job_card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED" in done.stderr
    assert desk.job_stands()


def test_an_unmerged_job_is_refused(tmp_path):
    desk = Desk(tmp_path)
    _job_refused(desk)


def test_a_dirty_job_worktree_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    (desk.job_wt / "job.txt").write_text("edited\n")
    _job_refused(desk)
    assert (desk.job_wt / "job.txt").read_text() == "edited\n"


def test_an_env_in_the_job_worktree_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    (desk.job_wt / ".env").write_text(CONSTRUCTED_ENV)
    _job_refused(desk)
    assert (desk.job_wt / ".env").read_text() == CONSTRUCTED_ENV


@pytest.mark.parametrize("bad", ["../x-job", "/abs/x-job", "a/b", ".hidden", "agy-trial", ""])
def test_a_job_worktree_outside_the_pattern_is_refused(tmp_path, bad):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    desk.job_card.write_text(desk.job_card.read_text().replace("WORKTREE: x-job", f"WORKTREE: {bad}"))
    _job_refused(desk)


def test_a_symlinked_job_worktree_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    (desk.wt / "link-job").symlink_to(desk.job_wt)
    desk.job_card.write_text(desk.job_card.read_text().replace("WORKTREE: x-job", "WORKTREE: link-job"))
    _job_refused(desk)
