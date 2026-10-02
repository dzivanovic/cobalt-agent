"""ops/desk/desk-row.sh and ops/desk/desk-commit.sh (card 17 A4).

Every run points COBALT_REPO_ROOT at a tmp git repo holding a constructed desk
report for today; the real desk report and the real repo are never touched.
"""

from __future__ import annotations

import datetime
import os
import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
ROW = REPO / "ops" / "desk" / "desk-row.sh"
COMMIT = REPO / "ops" / "desk" / "desk-commit.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

HEAD = "# CTO desk — x\n\n## §0 Headline\nOpened.\n\n## §4 Rulings x\n| R | time | ruling / record | status |\n|---|---|---|---|\n"
ROWS = (
    "| R1 | 01:00 ET | RECORD: one. | RECORD |\n"
    "| R3 | 01:02 ET | RECORD: three. | RECORD |\n"
    "| R2 | 01:01 ET | RECORD: two. | RECORD |\n"
)
TAIL = (
    "\n## §5 CURRENT\n| session | id |\n|---|---|\n| desk | `x` |\n\n"
    "## §5 HISTORY\n| R | x |\n\nHANDOVER: a → b at 01:00 ET\n"
)


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout


@pytest.fixture
def desk(tmp_path):
    repo = tmp_path / "repo"
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    reports.mkdir(parents=True)
    today = reports / f"cto-{datetime.date.today().isoformat()}.md"
    today.write_text(HEAD + ROWS + TAIL)
    (repo / "src").mkdir()
    (repo / "src" / "x.py").write_text("x = 1\n")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    env = dict(os.environ, COBALT_REPO_ROOT=str(repo), **GIT_ENV)
    return repo, today, env


def run(script: Path, *args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(script), *args], env=env, capture_output=True, text=True, timeout=60
    )


def clock() -> str:
    return subprocess.run(["date", "+%H:%M"], capture_output=True, text=True).stdout.strip()


# ---- desk-row.sh --------------------------------------------------------------------------


def test_the_new_row_is_the_highest_plus_one_after_the_last_row_before_section_5(desk):
    repo, today, env = desk
    before = clock()
    done = run(ROW, "RECORD", "RECORD: four.", env=env)
    after = clock()
    assert done.returncode == 0, done.stderr
    text = today.read_text()
    row = done.stdout.strip()
    m = re.fullmatch(r"\| R4 \| (\d\d:\d\d) ET \| RECORD: four\. \| RECORD \|", row)
    assert m, row
    assert m.group(1) in (before, after)
    assert text == HEAD + ROWS + row + "\n" + TAIL


def test_a_row_over_300_characters_is_refused(desk):
    repo, today, env = desk
    before = today.read_bytes()
    # "| R4 | HH:MM ET | " is 18, " | RECORD |" is 11: 271 characters of text make 300
    done = run(ROW, "RECORD", "x" * 271, env=env)
    assert done.returncode == 0, done.stderr
    assert len(done.stdout.rstrip("\n")) == 300
    today.write_bytes(before)
    done = run(ROW, "RECORD", "x" * 272, env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert today.read_bytes() == before


def test_a_launched_row_is_counted_without_its_backticked_spans(desk):
    repo, today, env = desk
    before = today.read_bytes()
    text = "LAUNCHED build `" + "y" * 100 + "` " + "x" * 160
    done = run(ROW, "LAUNCHED", text, env=env)
    assert done.returncode == 0, done.stderr
    today.write_bytes(before)
    # negative control: the same length under another status is refused
    done = run(ROW, "RECORD", text, env=env)
    assert done.returncode == 1
    assert today.read_bytes() == before


@pytest.mark.parametrize(
    "status,text",
    [("RECORD", "a | b"), ("RECORD", "a\nb"), ("REC|ORD", "a"), ("RECORD", ""), ("", "a")],
)
def test_a_bar_a_newline_or_an_empty_cell_is_refused(desk, status, text):
    repo, today, env = desk
    before = today.read_bytes()
    done = run(ROW, status, text, env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert today.read_bytes() == before


def test_a_missing_day_file_is_refused(desk):
    repo, today, env = desk
    today.unlink()
    done = run(ROW, "RECORD", "RECORD: x.", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert not today.exists()


def test_a_day_file_with_no_section_5_is_refused(desk):
    repo, today, env = desk
    today.write_text(HEAD + ROWS)
    before = today.read_bytes()
    done = run(ROW, "RECORD", "RECORD: x.", env=env)
    assert done.returncode == 1
    assert today.read_bytes() == before


# ---- desk-commit.sh -----------------------------------------------------------------------


def staged(repo: Path) -> list[str]:
    return git(repo, "diff", "--cached", "--name-only").split()


def test_commit_takes_exactly_the_named_path(desk):
    repo, today, env = desk
    other = repo / "docs" / "40 - DevDocs" / "reports" / "other.md"
    other.write_text("other\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "other")
    today.write_text(today.read_text() + "x\n")
    other.write_text("changed\n")
    done = run(COMMIT, "docs(desk): x", str(today), env=env)
    assert done.returncode == 0, done.stderr
    assert git(repo, "log", "-1", "--format=%s").strip() == "docs(desk): x"
    shown = git(repo, "show", "--name-only", "--format=", "HEAD").split("\n")
    assert [line for line in shown if line] == [str(today.relative_to(repo))]
    assert staged(repo) == []
    assert "other.md" in git(repo, "status", "--short")


def test_a_relative_path_is_taken_from_the_repo_root(desk):
    repo, today, env = desk
    today.write_text(today.read_text() + "x\n")
    done = run(COMMIT, "docs(desk): rel", str(today.relative_to(repo)), env=env)
    assert done.returncode == 0, done.stderr
    assert git(repo, "log", "-1", "--format=%s").strip() == "docs(desk): rel"


@pytest.mark.parametrize(
    "path",
    ["src/x.py", "SRC", "configs/a.yaml", "ops/desk/x.sh", "tests/x.py", "OUTSIDE", "docs/../src/x.py"],
)
def test_a_code_path_or_a_path_outside_the_repo_is_refused_and_nothing_is_staged(
    desk, path, tmp_path
):
    repo, today, env = desk
    (repo / "src" / "x.py").write_text("x = 2\n")
    today.write_text(today.read_text() + "x\n")
    outside = tmp_path / "outside.md"
    outside.write_text("o\n")
    arg = {"SRC": str(repo / "src" / "x.py"), "OUTSIDE": str(outside)}.get(path, path)
    head = git(repo, "rev-parse", "HEAD")
    done = run(COMMIT, "docs(desk): x", str(today), arg, env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert staged(repo) == []
    assert git(repo, "rev-parse", "HEAD") == head


def test_check_o3_a_code_path_in_another_letter_case_is_refused_and_nothing_is_staged(desk):
    repo, today, env = desk
    (repo / "src" / "x.py").write_text("x = 2\n")
    head = git(repo, "rev-parse", "HEAD")
    done = run(COMMIT, "docs(desk): x", "SRC/x.py", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert staged(repo) == []
    assert git(repo, "rev-parse", "HEAD") == head


def test_commit_with_no_path_is_refused(desk):
    repo, today, env = desk
    done = run(COMMIT, "docs(desk): x", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr


def test_the_commit_status_is_passed_through(desk):
    repo, today, env = desk
    hooks = repo / ".git" / "hooks"
    (hooks / "pre-commit").write_text("#!/bin/sh\necho hook-says-no >&2\nexit 1\n")
    (hooks / "pre-commit").chmod(0o755)
    today.write_text(today.read_text() + "x\n")
    head = git(repo, "rev-parse", "HEAD")
    done = run(COMMIT, "docs(desk): x", str(today), env=env)
    assert done.returncode == 1
    assert "hook-says-no" in done.stderr
    assert git(repo, "rev-parse", "HEAD") == head
