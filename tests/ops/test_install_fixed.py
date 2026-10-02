"""ops/desk/install-fixed.sh, a fixed file installed on a committed approved row
(card 17 A6). Every run points COBALT_REPO_ROOT at a tmp git repo; no real fixed
file or desk report is read or written.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
INSTALL = REPO / "ops" / "desk" / "install-fixed.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
DESK = (
    "# CTO desk — 2026-01-02\n\n## §4 Rulings 2026-01-02\n| R | time | ruling / record | status |\n"
    "|---|---|---|---|\n"
    "| R1 | 01:00 ET | HIS RULING: approves X-HUB.md. | HIS RULING · APPROVED |\n"
    "| R2 | 01:01 ET | HIS RULING: holds Y. | HIS RULING · HELD |\n"
    "| R12 | 01:02 ET | RECORD: x. | RECORD |\n\n## §5 CURRENT\n"
)
TITLE = "# X-HUB — the fixed x file (DRAFT 3 · «INSTALL on his approval» · R9)"
BODY = "\nline two\n\nMODEL: x «not a token»\n"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout


@pytest.fixture
def desk(tmp_path):
    repo = tmp_path / "repo"
    prompts = repo / "docs" / "40 - DevDocs" / "prompts"
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    prompts.mkdir(parents=True)
    reports.mkdir(parents=True)
    (reports / "cto-2026-01-02.md").write_text(DESK)
    fixed = prompts / "X-HUB.md"
    fixed.write_text(TITLE + BODY)
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    env = dict(os.environ, COBALT_REPO_ROOT=str(repo), **GIT_ENV)
    return repo, fixed, reports / "cto-2026-01-02.md", env


def install(*args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(INSTALL), *args], env=env, capture_output=True, text=True, timeout=60
    )


NEW = "# X-HUB — the fixed x file (DRAFT 3 · INSTALL: 2026-01-02 R1 of his approval of STANDING-LIST.md · R9)"


@pytest.mark.parametrize("r", ["R1", "1"])
def test_line_1_is_installed_and_every_other_byte_is_equal(desk, r):
    repo, fixed, day, env = desk
    done = install(str(fixed), "2026-01-02", r, env=env)
    assert done.returncode == 0, done.stderr
    assert fixed.read_text() == NEW + BODY
    assert fixed.read_text().count("«INSTALL") == 0
    assert TITLE in done.stdout and NEW in done.stdout
    # it commits nothing: the change sits unstaged in the work tree
    assert "X-HUB.md" in git(repo, "diff", "--name-only")
    assert git(repo, "diff", "--cached", "--name-only") == ""
    assert git(repo, "log", "--format=%s").split("\n")[0] == "base"


def refused(done: subprocess.CompletedProcess, fixed: Path, before: bytes) -> None:
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert fixed.read_bytes() == before


def test_a_row_without_approved_is_refused(desk):
    repo, fixed, day, env = desk
    before = fixed.read_bytes()
    done = install(str(fixed), "2026-01-02", "R2", env=env)
    refused(done, fixed, before)
    assert "no approved, committed row" in done.stderr


def test_a_missing_row_is_refused_and_r1_does_not_match_r12(desk):
    repo, fixed, day, env = desk
    before = fixed.read_bytes()
    refused(install(str(fixed), "2026-01-02", "R5", env=env), fixed, before)
    day.write_text(DESK.replace("| R1 | 01:00 ET |", "| R11 | 01:00 ET |"))
    git(repo, "commit", "-q", "-am", "r11")
    refused(install(str(fixed), "2026-01-02", "R1", env=env), fixed, before)


def test_an_uncommitted_row_is_refused(desk):
    repo, fixed, day, env = desk
    day.write_text(DESK + "| R7 | 02:00 ET | HIS RULING: approves. | HIS RULING · APPROVED |\n")
    before = fixed.read_bytes()
    done = install(str(fixed), "2026-01-02", "R7", env=env)
    refused(done, fixed, before)
    assert "no approved, committed row" in done.stderr
    # negative control: the same row once committed installs
    git(repo, "commit", "-q", "-am", "r7")
    assert install(str(fixed), "2026-01-02", "R7", env=env).returncode == 0


def test_two_rows_with_one_number_are_refused(desk):
    repo, fixed, day, env = desk
    day.write_text(DESK + "| R1 | 02:00 ET | HIS RULING: again. | HIS RULING · APPROVED |\n")
    git(repo, "commit", "-q", "-am", "dup")
    before = fixed.read_bytes()
    refused(install(str(fixed), "2026-01-02", "R1", env=env), fixed, before)


def test_a_missing_day_file_is_refused(desk):
    repo, fixed, day, env = desk
    before = fixed.read_bytes()
    refused(install(str(fixed), "2026-01-03", "R1", env=env), fixed, before)


def test_a_file_with_no_token_on_line_1_is_refused(desk):
    repo, fixed, day, env = desk
    fixed.write_text("# X-HUB (INSTALLED)\nbody «INSTALL here»\n")
    before = fixed.read_bytes()
    refused(install(str(fixed), "2026-01-02", "R1", env=env), fixed, before)


def test_a_token_left_elsewhere_in_the_file_is_refused(desk):
    repo, fixed, day, env = desk
    fixed.write_text(TITLE + "\nbody «INSTALL again»\n")
    before = fixed.read_bytes()
    refused(install(str(fixed), "2026-01-02", "R1", env=env), fixed, before)


def test_an_unclosed_token_is_refused(desk):
    repo, fixed, day, env = desk
    fixed.write_text("# X-HUB («INSTALL on his approval)\nbody\n")
    before = fixed.read_bytes()
    refused(install(str(fixed), "2026-01-02", "R1", env=env), fixed, before)


@pytest.mark.parametrize("where", ["sub", "reports", "outside"])
def test_a_file_outside_the_prompts_folder_is_refused(desk, tmp_path, where):
    repo, fixed, day, env = desk
    prompts = fixed.parent
    target = {
        "sub": prompts / "2026-01-02" / "X-HUB.md",
        "reports": day.parent / "X-HUB.md",
        "outside": tmp_path / "X-HUB.md",
    }[where]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(TITLE + BODY)
    before = target.read_bytes()
    refused(install(str(target), "2026-01-02", "R1", env=env), target, before)


@pytest.mark.parametrize("args", [("2026-1-2", "R1"), ("2026-01-02", "Rx"), ("2026-01-02",)])
def test_a_bad_date_or_row_is_refused(desk, args):
    repo, fixed, day, env = desk
    before = fixed.read_bytes()
    refused(install(str(fixed), *args, env=env), fixed, before)
