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


def test_l3_an_accented_tag_is_refused_under_a_utf8_locale(tmp_path):
    """Card 03 L3: `[!A-Za-z0-9._-]` admits `é` under en_US.UTF-8 unless the script runs LC_ALL=C."""
    desk = Desk(tmp_path)
    desk.card.write_text(desk.card.read_text().replace("TAG: x-tag", "TAG: x-tagé"))
    desk.env = dict(desk.env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    done = desk.run(GATE_CLEAN, desk.card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: TAG 'x-tagé' is not a plain tag name" in done.stderr
    assert desk.gate_stands()


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


def test_l3_an_accented_job_worktree_is_refused_under_a_utf8_locale(tmp_path):
    """Card 03 L3, job-clean.sh: `[!A-Za-z0-9._-]` admits `é` under en_US.UTF-8 unless LC_ALL=C."""
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    desk.job_card.write_text(desk.job_card.read_text().replace("WORKTREE: x-job", "WORKTREE: x-jobé"))
    desk.env = dict(desk.env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    done = desk.run(JOB_CLEAN, desk.job_card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: worktree 'x-jobé' is outside the approved pattern" in done.stderr
    assert desk.job_stands()


def test_a_symlinked_job_worktree_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    (desk.wt / "link-job").symlink_to(desk.job_wt)
    desk.job_card.write_text(desk.job_card.read_text().replace("WORKTREE: x-job", "WORKTREE: link-job"))
    _job_refused(desk)


# ---- job-clean.sh salvage ----------------------------------------------------------------


GIT_OPERATIONS = ["rebase-merge", "rebase-apply", "MERGE_HEAD", "CHERRY_PICK_HEAD", "REVERT_HEAD", "BISECT_LOG"]
FORCE_FORMS = ["--force", "branch -D", "worktree remove -f", "reset --hard", "clean -"]


def _salvage(desk: Desk, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(JOB_CLEAN), *args], env=desk.env, capture_output=True, text=True, timeout=120
    )


def _today() -> str:
    return subprocess.run(["date", "+%Y%m%d"], capture_output=True, text=True, check=True).stdout.strip()


def _wip_branches(desk: Desk) -> list[str]:
    out = git(desk.repo, "branch", "--list", "wip/*", "--format=%(refname:short)")
    return out.splitlines() if out else []


def _the_wip(desk: Desk, before: str, after: str, name: str = "x-job") -> str:
    wips = _wip_branches(desk)
    assert len(wips) == 1, wips
    assert wips[0] in {f"wip/{name}-salvage-{before}", f"wip/{name}-salvage-{after}"}, wips
    return wips[0]


def _short(desk: Desk, rev: str) -> str:
    return git(desk.repo, "rev-parse", rev)[:8]


def _merge_job(desk: Desk) -> None:
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")


def _salvage_refused_early(desk: Desk, name: str) -> subprocess.CompletedProcess:
    """W1: a refusal before the report prints nothing on stdout and changes nothing."""
    done = _salvage(desk, "salvage", name)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED" in done.stderr
    assert done.stdout == ""
    assert desk.job_stands()
    assert _wip_branches(desk) == []
    return done


def _salvage_refused_after_report(desk: Desk, name: str = "x-job") -> subprocess.CompletedProcess:
    """W3: refused after the report, with nothing changed (no switch, nothing staged)."""
    tree = desk.wt / name
    status = git(tree, "status", "--porcelain")
    head = git(tree, "rev-parse", "--abbrev-ref", "HEAD")
    done = _salvage(desk, "salvage", name)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED" in done.stderr
    assert done.stdout.startswith(f"INSPECT: worktree {tree}\n")
    assert "RUN:" not in done.stdout
    assert tree.is_dir()
    assert git(tree, "status", "--porcelain") == status
    assert git(tree, "rev-parse", "--abbrev-ref", "HEAD") == head
    assert desk.gate_stands()
    return done


def test_salvage_usage_names_the_salvage_form(tmp_path):
    """W1 red: three arguments, or none, are refused with the two-form usage line."""
    desk = Desk(tmp_path)
    for args in (("salvage", "x-job", "x"), ()):
        done = _salvage(desk, *args)
        assert done.returncode == 1
        assert done.stdout == ""
        assert (
            'REFUSED: usage: job-clean.sh "<job card>" | job-clean.sh salvage <worktree-name>' in done.stderr
        ), done.stderr
    assert desk.job_stands()


@pytest.mark.parametrize("bad", ["../x-job", "/abs/x-job", "a/b", ".hidden", "agy-trial", ""])
def test_salvage_a_name_outside_the_pattern_is_refused(tmp_path, bad):
    desk = Desk(tmp_path)
    _salvage_refused_early(desk, bad)


def test_salvage_a_symlinked_name_is_refused(tmp_path):
    desk = Desk(tmp_path)
    (desk.wt / "link-job").symlink_to(desk.job_wt)
    _salvage_refused_early(desk, "link-job")
    assert (desk.wt / "link-job").is_symlink()


def test_salvage_a_directory_git_does_not_know_is_refused(tmp_path):
    desk = Desk(tmp_path)
    (desk.wt / "loose").mkdir()
    (desk.wt / "loose" / "f.txt").write_text("loose\n")
    _salvage_refused_early(desk, "loose")
    assert (desk.wt / "loose" / "f.txt").read_text() == "loose\n"


def test_salvage_a_prefix_of_a_registered_worktree_is_refused(tmp_path):
    """X3: `worktree <path>` is matched whole; `x-jo` is not `x-job`'s stanza."""
    desk = Desk(tmp_path)
    (desk.wt / "x-jo").mkdir()
    done = _salvage_refused_early(desk, "x-jo")
    assert "is not a registered worktree of" in done.stderr


def test_salvage_an_accented_name_is_refused_under_a_utf8_locale(tmp_path):
    desk = Desk(tmp_path)
    desk.env = dict(desk.env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    _salvage_refused_early(desk, "x-jobé")


def test_salvage_a_tree_on_main_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "switch", "-q", "-c", "other")
    git(desk.repo, "worktree", "add", "-q", str(desk.wt / "x-main"), "main")
    done = _salvage(desk, "salvage", "x-main")
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED" in done.stderr
    assert done.stdout == ""
    assert (desk.wt / "x-main").is_dir()
    assert has_branch(desk.repo, "main")


def _report(desk: Desk, *, merged: str, ahead: list[str], status: list[str] | None = None,
            ignored: int = 0, branch: str = "branch ops/x-job") -> list[str]:
    status = status or []
    return [
        f"INSPECT: worktree {desk.job_wt}",
        f"INSPECT: {branch}",
        f"INSPECT: merged into main: {merged}",
        f"INSPECT: ahead of main: {len(ahead)}",
        *[f"INSPECT:   {line}" for line in ahead],
        f"INSPECT: status: {len(status)} lines",
        *[f"INSPECT:   {line}" for line in status],
        "INSPECT: .env: no",
        "INSPECT: locked: no",
        "INSPECT: git operation in progress: none",
        f"INSPECT: ignored: {ignored} paths, never saved",
    ]


def test_salvage_a_clean_merged_tree_reports_and_is_removed(tmp_path):
    """W2 + W5 CLEAN MERGED: the report, then the plain removal; nothing salvaged."""
    desk = Desk(tmp_path)
    _merge_job(desk)
    done = _salvage(desk, "salvage", "x-job")
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines() == _report(desk, merged="yes", ahead=[]) + [
        f"RUN: git -C {desk.repo} worktree remove {desk.job_wt}",
        f"RUN: git -C {desk.repo} branch -d ops/x-job",
        f"job-clean salvage: removed {desk.job_wt}; deleted ops/x-job; kept none",
    ]
    assert not desk.job_wt.exists()
    assert not has_branch(desk.repo, "ops/x-job")
    assert _wip_branches(desk) == []
    assert desk.gate_stands()


def test_salvage_a_clean_unmerged_tree_keeps_its_branch(tmp_path):
    """W2 unmerged + W4 CLEAN UNMERGED + W5: no wip branch, its own branch kept and named."""
    desk = Desk(tmp_path)
    tip = _short(desk, "ops/x-job")
    done = _salvage(desk, "salvage", "x-job")
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[:10] == _report(desk, merged="no", ahead=[f"{tip} job"])
    assert "SALVAGED: ops/x-job 0 files 1 commits ahead" in lines
    assert "kept: ops/x-job (not merged)" in lines
    assert not any("branch -d" in line for line in lines)
    assert lines[-1] == f"job-clean salvage: removed {desk.job_wt}; deleted none; kept ops/x-job"
    assert not desk.job_wt.exists()
    assert has_branch(desk.repo, "ops/x-job")
    assert git(desk.repo, "rev-parse", "ops/x-job")[:8] == tip
    assert _wip_branches(desk) == []


def test_salvage_a_clean_unmerged_tree_keeps_its_branch_negative_control(tmp_path):
    """W5 NEGATIVE CONTROL: green on BASE (refused) and after (kept)."""
    desk = Desk(tmp_path)
    _salvage(desk, "salvage", "x-job")
    assert has_branch(desk.repo, "ops/x-job")


def _dirty(desk: Desk) -> None:
    (desk.job_wt / "job.txt").write_text("edited\n")
    (desk.job_wt / "new.txt").write_text("new\n")
    exclude = desk.repo / ".git" / "info" / "exclude"
    exclude.write_text(exclude.read_text() + ".venv-x\n")
    (desk.job_wt / ".venv-x").write_text("ignored\n")


def test_salvage_a_dirty_unmerged_tree_commits_to_a_wip_branch(tmp_path):
    """W4 DIRTY UNMERGED + W5: tracked edit and untracked file saved, ignored file not."""
    desk = Desk(tmp_path)
    _dirty(desk)
    tip = git(desk.repo, "rev-parse", "ops/x-job")
    before = _today()
    done = _salvage(desk, "salvage", "x-job")
    after = _today()
    assert done.returncode == 0, done.stdout + done.stderr
    wip = _the_wip(desk, before, after)
    lines = done.stdout.splitlines()
    assert lines[:12] == _report(
        desk, merged="no", ahead=[f"{tip[:8]} job"], status=[" M job.txt", "?? new.txt"], ignored=1
    )
    assert f"RUN: git -C {desk.job_wt} switch -c {wip}" in lines
    assert f"RUN: git -C {desk.job_wt} add -A" in lines
    assert any(line.startswith(f"RUN: git -C {desk.job_wt} commit -q -m ") for line in lines)
    assert f"SALVAGED: {wip} 2 files 1 commits ahead" in lines
    assert git(desk.repo, "show", f"{wip}:job.txt") + "\n" == "edited\n"
    assert git(desk.repo, "show", f"{wip}:new.txt") + "\n" == "new\n"
    with pytest.raises(subprocess.CalledProcessError):
        git(desk.repo, "show", f"{wip}:.venv-x")
    assert git(desk.repo, "rev-parse", f"{wip}^") == tip
    assert git(desk.repo, "log", "-1", "--format=%s", wip).startswith("wip: salvage x-job ")
    assert f"kept: {wip} (salvage)" in lines
    assert "kept: ops/x-job (not merged)" in lines
    assert lines[-1] == f"job-clean salvage: removed {desk.job_wt}; deleted none; kept ops/x-job {wip}"
    assert not desk.job_wt.exists()
    assert git(desk.repo, "rev-parse", "ops/x-job") == tip


def test_salvage_a_dirty_merged_tree_deletes_its_branch_and_keeps_the_wip(tmp_path):
    """W5 DIRTY MERGED: the merged branch is deleted, the wip branch is kept."""
    desk = Desk(tmp_path)
    _merge_job(desk)
    (desk.job_wt / "job.txt").write_text("edited\n")
    before = _today()
    done = _salvage(desk, "salvage", "x-job")
    after = _today()
    assert done.returncode == 0, done.stdout + done.stderr
    wip = _the_wip(desk, before, after)
    lines = done.stdout.splitlines()
    assert f"SALVAGED: {wip} 1 files 0 commits ahead" in lines
    assert f"RUN: git -C {desk.repo} branch -d ops/x-job" in lines
    assert lines[-1] == f"job-clean salvage: removed {desk.job_wt}; deleted ops/x-job; kept {wip}"
    assert not has_branch(desk.repo, "ops/x-job")
    assert git(desk.repo, "show", f"{wip}:job.txt") + "\n" == "edited\n"
    assert not desk.job_wt.exists()


def test_salvage_a_detached_unmerged_head_is_kept_on_a_wip_branch(tmp_path):
    """W4 DETACHED, CLEAN: `switch -c` alone; the wip tip is the detached commit."""
    desk = Desk(tmp_path)
    git(desk.job_wt, "switch", "-q", "--detach")
    (desk.job_wt / "detached.txt").write_text("detached\n")
    git(desk.job_wt, "add", "-A")
    git(desk.job_wt, "commit", "-q", "-m", "detached")
    head = git(desk.job_wt, "rev-parse", "HEAD")
    before = _today()
    done = _salvage(desk, "salvage", "x-job")
    after = _today()
    assert done.returncode == 0, done.stdout + done.stderr
    wip = _the_wip(desk, before, after)
    lines = done.stdout.splitlines()
    assert lines[1] == f"INSPECT: branch (detached at {head[:8]})"
    assert "INSPECT: ahead of main: 2" in lines
    assert not any(" add -A" in line or " commit " in line for line in lines)
    assert f"SALVAGED: {wip} 0 files 2 commits ahead" in lines
    assert git(desk.repo, "rev-parse", wip) == head
    assert lines[-1] == f"job-clean salvage: removed {desk.job_wt}; deleted none; kept {wip}"
    assert not desk.job_wt.exists()
    assert has_branch(desk.repo, "ops/x-job")


def test_salvage_a_detached_merged_clean_head_is_removed_without_a_wip(tmp_path):
    """W4: a detached HEAD already on main holds no work; no wip branch, no SALVAGED line."""
    desk = Desk(tmp_path)
    _merge_job(desk)
    git(desk.job_wt, "switch", "-q", "--detach")
    done = _salvage(desk, "salvage", "x-job")
    assert done.returncode == 0, done.stdout + done.stderr
    assert not any(line.startswith("SALVAGED:") for line in done.stdout.splitlines())
    assert _wip_branches(desk) == []
    assert done.stdout.splitlines()[-1] == f"job-clean salvage: removed {desk.job_wt}; deleted none; kept none"
    assert not desk.job_wt.exists()


def test_salvage_an_env_in_the_tree_is_refused_negative_control(tmp_path):
    """W3 NEGATIVE CONTROL: green on BASE and after."""
    desk = Desk(tmp_path)
    (desk.job_wt / ".env").write_text(CONSTRUCTED_ENV)
    done = _salvage(desk, "salvage", "x-job")
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert desk.job_stands()
    assert (desk.job_wt / ".env").read_text() == CONSTRUCTED_ENV


def test_salvage_an_env_in_the_tree_is_refused_after_the_report(tmp_path):
    desk = Desk(tmp_path)
    (desk.job_wt / "job.txt").write_text("edited\n")
    (desk.job_wt / ".env").write_text(CONSTRUCTED_ENV)
    done = _salvage_refused_after_report(desk)
    assert "INSPECT: .env: yes" in done.stdout.splitlines()
    assert "the job holds the cobalt_dev lock (L76)" in done.stderr
    assert (desk.job_wt / ".env").read_text() == CONSTRUCTED_ENV
    assert (desk.job_wt / "job.txt").read_text() == "edited\n"
    assert desk.job_stands()
    assert _wip_branches(desk) == []


@pytest.mark.parametrize("reason", [None, "held by a test"])
def test_salvage_a_locked_tree_is_refused_after_the_report(tmp_path, reason):
    desk = Desk(tmp_path)
    (desk.job_wt / "job.txt").write_text("edited\n")
    git(desk.repo, "worktree", "lock", *(["--reason", reason] if reason else []), str(desk.job_wt))
    done = _salvage_refused_after_report(desk)
    assert "INSPECT: locked: yes" in done.stdout.splitlines()
    assert desk.job_stands()
    assert _wip_branches(desk) == []


@pytest.mark.parametrize("marker", GIT_OPERATIONS)
def test_salvage_a_git_operation_in_progress_is_refused_after_the_report(tmp_path, marker):
    desk = Desk(tmp_path)
    (desk.job_wt / "job.txt").write_text("edited\n")
    at = Path(git(desk.job_wt, "rev-parse", "--git-path", marker))
    at = at if at.is_absolute() else desk.job_wt / at
    if marker.startswith("rebase-"):
        at.mkdir()
    else:
        at.write_text(git(desk.job_wt, "rev-parse", "HEAD") + "\n")
    done = _salvage_refused_after_report(desk)
    assert f"INSPECT: git operation in progress: {marker}" in done.stdout.splitlines()
    assert desk.job_stands()
    assert _wip_branches(desk) == []
    assert (desk.job_wt / "job.txt").read_text() == "edited\n"


def test_salvage_an_existing_wip_branch_is_refused_after_the_report(tmp_path):
    desk = Desk(tmp_path)
    (desk.job_wt / "job.txt").write_text("edited\n")
    premade = f"wip/x-job-salvage-{_today()}"
    git(desk.repo, "branch", premade, "main")
    done = _salvage_refused_after_report(desk)
    assert f"REFUSED: {premade} already exists" in done.stderr
    assert _wip_branches(desk) == [premade]
    assert git(desk.repo, "rev-parse", premade) == desk.main
    assert (desk.job_wt / "job.txt").read_text() == "edited\n"
    assert desk.job_stands()


def test_salvage_a_wip_name_git_refuses_is_refused_after_the_report(tmp_path):
    """W3: `wip/a..b-salvage-<D>` fails `git check-ref-format --branch`."""
    desk = Desk(tmp_path)
    tree = desk.wt / "a..b"
    git(desk.repo, "worktree", "add", "-q", "-b", "ops/ab", str(tree), "main")
    (tree / "a.txt").write_text("edited\n")
    done = _salvage_refused_after_report(desk, "a..b")
    assert "is not a valid branch name" in done.stderr
    assert _wip_branches(desk) == []
    assert (tree / "a.txt").read_text() == "edited\n"
    assert has_branch(desk.repo, "ops/ab")


def test_job_clean_is_never_forced():
    """W7: no force form anywhere in the file, comments included."""
    text = JOB_CLEAN.read_text()
    assert [form for form in FORCE_FORMS if form in text] == []


def test_salvage_saves_an_untracked_file_when_status_hides_untracked(tmp_path):
    """X1: an untracked file is saved even when the repo config hides untracked files."""
    desk = Desk(tmp_path)
    git(desk.repo, "config", "status.showUntrackedFiles", "no")
    (desk.job_wt / "new.txt").write_text("new\n")
    done = _salvage(desk, "salvage", "x-job")
    saved = [b for b in _wip_branches(desk) if git(desk.repo, "ls-tree", "--name-only", b, "new.txt")]
    assert (desk.job_wt / "new.txt").exists() or saved, done.stdout + done.stderr


def test_salvage_saves_an_edit_hidden_by_skip_worktree(tmp_path):
    """X1: an edit to a skip-worktree file is not lost by the removal."""
    desk = Desk(tmp_path)
    git(desk.job_wt, "update-index", "--skip-worktree", "job.txt")
    (desk.job_wt / "job.txt").write_text("edited\n")
    done = _salvage(desk, "salvage", "x-job")
    saved = [b for b in _wip_branches(desk) if git(desk.repo, "show", f"{b}:job.txt") == "edited"]
    assert (desk.job_wt / "job.txt").exists() or saved, done.stdout + done.stderr


def test_salvage_a_branch_delete_failure_reports_the_original_branch_kept(tmp_path):
    desk = Desk(tmp_path)
    _merge_job(desk)
    lock = desk.repo / ".git" / "refs" / "heads" / "ops" / "x-job.lock"
    lock.write_text("blocked\n")

    done = _salvage(desk, "salvage", "x-job")

    assert done.returncode == 1, done.stdout + done.stderr
    assert not desk.job_wt.exists()
    assert has_branch(desk.repo, "ops/x-job")
    assert done.stdout.splitlines()[-1] == (
        f"job-clean salvage: removed {desk.job_wt}; deleted none; kept ops/x-job"
    )


def test_salvage_prints_the_exact_switch_command_it_runs(tmp_path):
    import shlex
    import shutil

    desk = Desk(tmp_path)
    _dirty(desk)
    calls = tmp_path / "git-calls"
    real_git = shutil.which("git", path=os.environ["PATH"])
    assert real_git is not None
    stub_dir = Path(desk.env["PATH"].split(os.pathsep)[0])
    git_stub = stub_dir / "git"
    git_stub.write_text(
        "#!/bin/sh\n"
        f"printf '%s\\n' \"$*\" >> {shlex.quote(str(calls))}\n"
        f"exec {shlex.quote(real_git)} \"$@\"\n"
    )
    git_stub.chmod(0o755)

    done = _salvage(desk, "salvage", "x-job")

    assert done.returncode == 0, done.stdout + done.stderr
    reported = next(
        line.removeprefix("RUN: git ")
        for line in done.stdout.splitlines()
        if " switch " in line
    )
    actual = next(line for line in calls.read_text().splitlines() if " switch " in line)
    assert actual == reported
