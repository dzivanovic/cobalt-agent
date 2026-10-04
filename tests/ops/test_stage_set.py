"""ops/desk/stage-set.sh — a check's whole reading set staged for a house in one call (card 19 worker-steps S4).

A tmp repo stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) and a tmp directory for
/Users/cobalt/cobalt-wt (COBALT_WT_ROOT), with its own agy-trial/scratch/. The job worktree
is a real `git worktree add`; its working copy is dirtied before staging, so every byte
staged is proved to come from git at TIP, never from the working files.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
STAGE = REPO / "ops" / "desk" / "stage-set.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
REPORT_REL = "docs/40 - DevDocs/reports/x-job-build.md"
SPACED = "src/a dir/with space.py"


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


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


@pytest.fixture
def job(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    (wt / "agy-trial" / "scratch").mkdir(parents=True)
    write(repo / "src" / "m.py", "X = 1\n")
    write(repo / "docs" / "page.md", "page\n")
    write(repo / ".gitignore", ".env\n")
    write(repo / "docs" / "40 - DevDocs" / "reports" / "cto-2026-01-02.md",
          "| row |\n| R1 | 09:00 ET | HIS RULING: the job. | APPROVED |\n")
    git(repo, "init", "-q", "-b", "main")
    base = commit(repo, "base")
    job_wt = wt / "x-job"
    git(repo, "worktree", "add", "-q", "-b", "ops/x-job", str(job_wt), base)
    write(job_wt / "tests" / "test_m.py", "def test_m():\n    assert False\n")
    commit(job_wt, "wip(x-job): red")
    write(job_wt / "src" / "m.py", "X = 2\n")
    write(job_wt / "tests" / "test_m.py", "def test_m():\n    assert True\n")
    write(job_wt / "docs" / "page.md", "page, changed\n")
    write(job_wt / SPACED, "S = 1\n")
    tip = commit(job_wt, "fix(x-job): m")
    write(job_wt / REPORT_REL, "# report\n\nBUILT · job: x-job\n")
    commit(job_wt, "docs(x-job): build report")
    card = repo / "docs" / "40 - DevDocs" / "prompts" / "2026-01-02" / "01-x-job-card.md"
    write(card, (
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {base}\nTIP: {tip}\nREPORT: {job_wt / REPORT_REL}\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
    ))
    commit(repo, "card")
    # the working copy differs from TIP: git, not the files, is the source
    write(job_wt / "src" / "m.py", "X = 'dirty'\n")
    write(job_wt / SPACED, "S = 'dirty'\n")
    env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo), **GIT_ENV)
    dest = wt / "agy-trial" / "scratch" / "tribunal-bars-0920" / "x-job-check"
    return wt, repo, job_wt, base, tip, card, env, dest


def stage(env: dict, card: Path, dest: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(STAGE), str(card), str(dest)], env=env, capture_output=True, text=True, timeout=120
    )


def blob(job_wt: Path, rev: str) -> bytes:
    return subprocess.run(["git", "cat-file", "blob", rev], cwd=job_wt, capture_output=True, check=True).stdout


def test_the_whole_set_is_staged_byte_equal_to_git_at_tip(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    done = stage(env, card, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    for path in ("src/m.py", "tests/test_m.py", "docs/page.md", SPACED):
        staged = dest / "files" / "wt" / path
        assert staged.read_bytes() == blob(job_wt, f"{tip}:{path}"), path
    assert (dest / "files" / "wt" / "src" / "m.py").read_text() == "X = 2\n"
    assert (dest / "files" / card.name).read_bytes() == card.read_bytes()
    assert (dest / "files" / "x-job-build.md").read_text() == "# report\n\nBUILT · job: x-job\n"
    diff = (dest / "diff.md").read_text()
    assert diff.splitlines()[0] == f'=== git log -p {base}..{tip} -- . ":(exclude)docs" (in {job_wt}) ==='
    assert sum(1 for ln in diff.splitlines() if ln.startswith("commit ")) == 2
    assert "page, changed" not in diff and "docs/page.md" not in diff
    rulings = (dest / "rulings.md").read_text()
    assert f'grep -n "^| R1 " "{repo}/docs/40 - DevDocs/reports/cto-2026-01-02.md"' in rulings
    assert "2:| R1 | 09:00 ET | HIS RULING: the job. | APPROVED |" in rulings
    lines = done.stdout.splitlines()
    files = sorted(p for p in dest.rglob("*") if p.is_file())
    assert lines[-1].startswith(f"STAGED {len(files)} files · ")
    assert lines[-1].endswith(" · commits 2")
    total = sum(p.stat().st_size for p in files)
    assert f" · {total} " in lines[-1]
    for p in files:
        assert f"{p.stat().st_size} {p}" in lines, p
    assert not any(p.name == ".env" for p in dest.rglob("*"))


def test_a_dest_outside_the_scratch_folder_is_refused(job, tmp_path):
    wt, repo, job_wt, base, tip, card, env, dest = job
    outside = wt / "agy-trial" / "elsewhere"
    done = stage(env, card, outside)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert not outside.exists()


def test_a_dest_with_dotdot_is_refused(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    sneaky = wt / "agy-trial" / "scratch" / ".." / "out"
    done = stage(env, card, sneaky)
    assert done.returncode == 1
    assert not (wt / "agy-trial" / "out").exists()


def test_a_non_empty_dest_is_refused_and_left_as_it_was(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    dest.mkdir(parents=True)
    (dest / "house-a.md").write_text("FINDINGS: 0\n")
    done = stage(env, card, dest)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert sorted(p.name for p in dest.iterdir()) == ["house-a.md"]


def test_an_env_path_in_the_diff_is_refused_with_the_dest_left_empty(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    git(job_wt, "checkout", "-q", "--", ".")
    write(job_wt / "configs" / ".env", "COBALT_TEST_CONSTRUCTED=1\n")
    git(job_wt, "add", "-f", "configs/.env")
    git(job_wt, "commit", "-q", "-m", "an env in the diff")
    new_tip = git(job_wt, "rev-parse", "--short=8", "HEAD")
    card.write_text(card.read_text().replace(f"TIP: {tip}", f"TIP: {new_tip}"))
    commit(repo, "card at the new tip")
    done = stage(env, card, dest)
    assert done.returncode == 1
    assert not dest.exists() or list(dest.iterdir()) == []


def test_l3_an_accented_worktree_is_refused_under_a_utf8_locale(job):
    """Card 03 L3: `[!A-Za-z0-9._-]` admits `é` under en_US.UTF-8 unless the script runs LC_ALL=C."""
    wt, repo, job_wt, base, tip, card, env, dest = job
    card.write_text(card.read_text().replace("WORKTREE: x-job", "WORKTREE: x-jobé"))
    commit(repo, "card with an accented worktree")
    env = dict(env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    done = stage(env, card, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: WORKTREE 'x-jobé' is not one directory name" in done.stderr
    assert not dest.exists() or list(dest.iterdir()) == []


@pytest.mark.parametrize("args", [[], ["one"], ["/no/such/card.md", "/tmp/x"]])
def test_a_bad_call_is_refused(job, args):
    wt, repo, job_wt, base, tip, card, env, dest = job
    done = subprocess.run(["sh", str(STAGE), *args], env=env, capture_output=True, text=True, timeout=60)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
