"""order-open.sh prints the facts before an order's first launch (card 18 desk-tools-b, row B3).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT) and a tmp directory standing in for /Users/cobalt/cobalt-wt
(COBALT_WT_ROOT). `claude` is a stub on PATH answering two live sessions and one
dead row. The clock is overridden by ORDER_OPEN_NOW for the window cases.
"""

from __future__ import annotations

import hashlib
import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "order-open.sh"
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

SESSIONS = """[
 {"id": "aaaa1111", "name": "cto-desk", "cwd": "/x/desk", "status": "running", "state": "working", "pid": 101, "sessionId": "s1"},
 {"id": "bbbb2222", "name": "alpha-build", "cwd": "/x/wt/alpha", "status": "running", "state": "idle", "pid": 102, "sessionId": "s2"},
 {"id": "cccc3333", "name": "gone-check", "cwd": "/x/wt/gone", "status": "stopped", "state": "done", "sessionId": "s3"}
]
"""


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def tree_hash(*roots: Path) -> str:
    h = hashlib.sha256()
    for root in roots:
        for p in sorted(root.rglob("*")):
            h.update(str(p).encode())
            if p.is_symlink():
                h.update(os.readlink(p).encode())
            elif p.is_file():
                h.update(p.read_bytes())
    return h.hexdigest()


@pytest.fixture
def desk(tmp_path):
    root = tmp_path.resolve()
    repo, wt = root / "repo", root / "wt"
    repo.mkdir()
    wt.mkdir()
    (repo / "a.txt").write_text("a\n")
    (repo / "b.txt").write_text("b\n")
    (repo / ".gitignore").write_text(".env\n")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    git(repo, "update-ref", "refs/remotes/origin/main", "HEAD")

    git(repo, "worktree", "add", "-q", "-b", "ops/merged-job", str(wt / "merged-wt"), "main")
    (wt / "merged-wt" / "m.txt").write_text("m\n")
    git(wt / "merged-wt", "add", "-A")
    git(wt / "merged-wt", "commit", "-q", "-m", "merged job")
    git(repo, "merge", "-q", "--no-ff", "--no-edit", "ops/merged-job")

    git(repo, "worktree", "add", "-q", "-b", "ops/open-job", str(wt / "open-wt"), "main")
    (wt / "open-wt" / "o.txt").write_text("o\n")
    git(wt / "open-wt", "add", "-A")
    git(wt / "open-wt", "commit", "-q", "-m", "open job")

    # one held lock: the open job's .env and the lock directory naming it
    (wt / "open-wt" / ".env").write_text(CONSTRUCTED_ENV)
    (wt / LOCK_NAME).mkdir()
    (wt / LOCK_NAME / "owner").write_text("open-wt\n")
    # a tracked change on main's tree
    (repo / "a.txt").write_text("a edited\n")
    # b.txt unchanged but stat-stale: a `git status` free to take its optional lock would
    # refresh and rewrite .git/index, which the read-only test would see
    later = (repo / "b.txt").stat().st_mtime + 3600
    os.utime(repo / "b.txt", (later, later))

    stub = root / "bin"
    stub.mkdir()
    (root / "sessions.json").write_text(SESSIONS)
    (stub / "claude").write_text(
        "#!/bin/sh\n"
        f'printf "%s\\n" "$*" >> "{root / "claude-calls"}"\n'
        f'[ "$1" = agents ] && exec cat "{root / "sessions.json"}"\n'
        "exit 0\n"
    )
    (stub / "claude").chmod(0o755)
    env = dict(
        os.environ, COBALT_REPO_ROOT=str(repo), COBALT_WT_ROOT=str(wt),
        PATH=f"{stub}{os.pathsep}{os.environ['PATH']}", HOME=str(root / "home"), **GIT_ENV,
    )
    return repo, wt, env, root


def run(env: dict, script: Path = SCRIPT, **extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(script)], env=dict(env, **extra), capture_output=True, text=True, timeout=120
    )


def block(out: str, name: str) -> str:
    lines = out.splitlines()
    start = lines.index(name)
    body = []
    for line in lines[start + 1:]:
        if line in ("LOCK", "SESSIONS", "WINDOW", "MAIN", "WORKTREES", "HOUSES"):
            break
        body.append(line)
    return "\n".join(body)


def test_every_block_carries_its_facts_and_nothing_changes(desk):
    repo, wt, env, root = desk
    before = tree_hash(repo, wt)
    done = run(env, ORDER_OPEN_NOW="2026-01-05T12:00:00")
    assert done.returncode == 0, done.stderr
    out = done.stdout
    names = [line for line in out.splitlines() if line in ("LOCK", "SESSIONS", "WINDOW", "MAIN", "WORKTREES", "HOUSES")]
    assert names == ["LOCK", "SESSIONS", "WINDOW", "MAIN", "WORKTREES", "HOUSES"]

    lock = block(out, "LOCK")
    assert str(wt / "open-wt" / ".env") in lock
    assert "owner open-wt" in lock
    assert "free" not in lock

    sessions = block(out, "SESSIONS")
    assert "aaaa1111 cto-desk /x/desk running working" in sessions
    assert "bbbb2222 alpha-build /x/wt/alpha running idle" in sessions
    assert "cccc3333" not in sessions

    main = block(out, "MAIN")
    assert "ahead of origin/main: 2" in main
    assert "uncommitted tracked changes: yes" in main

    worktrees = block(out, "WORKTREES")
    merged = next(line for line in worktrees.splitlines() if "merged-wt" in line)
    opened = next(line for line in worktrees.splitlines() if "open-wt" in line)
    assert "ops/merged-job" in merged and " merged" in merged and "unmerged" not in merged
    assert "ops/open-job" in opened and "unmerged" in opened
    assert "0 days" in merged and "0 days" in opened

    assert block(out, "HOUSES").strip() == "not probed"
    assert tree_hash(repo, wt) == before


def test_a_free_lock_and_a_clean_main_say_so(desk):
    repo, wt, env, root = desk
    (wt / "open-wt" / ".env").unlink()
    shutil.rmtree(wt / LOCK_NAME)
    (repo / "a.txt").write_text("a\n")
    done = run(env, ORDER_OPEN_NOW="2026-01-05T12:00:00")
    assert done.returncode == 0, done.stderr
    assert block(done.stdout, "LOCK").strip() == "free"
    assert "uncommitted tracked changes: no" in block(done.stdout, "MAIN")


@pytest.mark.parametrize(
    "now, window",
    [
        ("2026-01-05T20:30:00", "pause"),        # Monday, in the 20:00–21:00 pause
        ("2026-01-05T22:15:00", "overnight"),    # Monday night
        ("2026-01-06T02:00:00", "overnight"),    # Tuesday before 04:00, after a weekday
        ("2026-01-10T02:00:00", "overnight"),    # Saturday before 04:00, after Friday
        ("2026-01-10T12:00:00", "weekend"),      # Saturday
        ("2026-01-11T21:30:00", "weekend"),      # Sunday evening
        ("2026-01-12T02:00:00", "weekend"),      # Monday before 04:00, after Sunday
        ("2026-01-05T12:00:00", "closed — a deploy needs his dated order"),  # Monday midday
        ("2026-01-05T04:00:00", "closed — a deploy needs his dated order"),  # Monday 04:00
    ],
)
def test_the_window_for_each_clock(desk, now, window):
    repo, wt, env, root = desk
    done = run(env, ORDER_OPEN_NOW=now)
    assert done.returncode == 0, done.stderr
    lines = block(done.stdout, "WINDOW").splitlines()
    assert lines[0] == f"window: {window}"
    assert any("holidays are not known" in line for line in lines)


def test_a_utc_clock_is_read_in_new_york(desk):
    repo, wt, env, root = desk
    done = run(env, ORDER_OPEN_NOW="2026-01-06T01:30:00+00:00")  # Monday 20:30 ET
    assert done.returncode == 0, done.stderr
    assert block(done.stdout, "WINDOW").splitlines()[0] == "window: pause"


def test_house_probe_beside_it_is_run(desk, tmp_path):
    repo, wt, env, root = desk
    ops = root / "ops-copy"
    ops.mkdir()
    shutil.copy(SCRIPT, ops / "order-open.sh")
    (ops / "house-probe.sh").write_text("#!/bin/sh\necho 'house grok: ready'\n")
    done = run(env, script=ops / "order-open.sh", ORDER_OPEN_NOW="2026-01-05T12:00:00")
    assert done.returncode == 0, done.stderr
    assert block(done.stdout, "HOUSES").strip() == "house grok: ready"


def test_an_unreadable_session_list_still_exits_0(desk):
    repo, wt, env, root = desk
    (root / "sessions.json").write_text("not json")
    done = run(env, ORDER_OPEN_NOW="2026-01-05T12:00:00")
    assert done.returncode == 0, done.stderr
    assert "unreadable" in block(done.stdout, "SESSIONS")
