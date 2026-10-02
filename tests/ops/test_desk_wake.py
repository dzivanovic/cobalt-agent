"""desk-wake.sh and desk-handover.sh (card 18 desk-tools-b, row B4).

Every run points the scripts at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT) and a tmp directory standing in for /Users/cobalt/cobalt-wt
(COBALT_WT_ROOT); HOME is a tmp directory, so no transcript of a real session is
read. `claude` is a stub on PATH that answers `agents --json` from a file and
records every call. A run that needs the scripts beside it (desk-context.sh,
wait-desk-idle.sh) runs a copy of the script under test in a tmp ops folder.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

REPO = Path(__file__).resolve().parents[2]
OPS = REPO / "ops" / "desk"
WAKE = OPS / "desk-wake.sh"
HANDOVER = OPS / "desk-handover.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

PRED = "aaaa1111-0000-4000-8000-000000000001"


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
            if p.is_file():
                h.update(p.read_bytes())
    return h.hexdigest()


def today_et() -> dt.date:
    return dt.datetime.now(ZoneInfo("America/New_York")).date()


TODAY_REPORT = """# CTO desk — constructed

## §0 Headline
Opened by desk zero-marker (constructed).

## §4 Rulings
| # | time | ruling / record | status |
|---|---|---|---|
| R1 | 06:00 ET | row one text | RECORD |
| R2 | 07:00 ET | row two text | RECORD |
| R3 | 08:00 ET | row three text | RECORD |
| R4 | 09:00 ET | row four text | APPROVED — pending fold |
| R5 | 10:00 ET | row five text | RECORD |
| R6 | 11:00 ET | row six text | RECORD |

## §5 CURRENT
| session | id |
|---|---|
| CTO desk | current-marker |

## §5 HISTORY
| old | history-marker |
HANDOVER: predecessor aaaa1111 → successor bbbb2222 at 08:30 ET
"""

YESTERDAY_REPORT = """# CTO desk — constructed, the day before

## §0 Headline
Yesterday's headline.

## §4 Rulings
| # | time | ruling / record | status |
|---|---|---|---|
| R8 | 09:00 ET | yesterday plain row | RECORD |
| R9 | 10:00 ET | yesterday pending row {pad} | APPROVED — pending fold |

## §5 CURRENT
| yesterday-current |
"""


class Desk:
    def __init__(self, tmp_path: Path) -> None:
        root = tmp_path.resolve()
        self.root = root
        self.repo = root / "repo"
        self.wt = root / "wt"
        self.repo.mkdir()
        self.wt.mkdir()
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        self.reports.mkdir(parents=True)
        today = today_et()
        self.today = self.reports / f"cto-{today.isoformat()}.md"
        self.yesterday = self.reports / f"cto-{(today - dt.timedelta(days=1)).isoformat()}.md"
        self.today.write_text(TODAY_REPORT)
        self.yesterday.write_text(YESTERDAY_REPORT.replace("{pad}", "x" * 400))
        (self.reports / f"cto-{today.isoformat()}-words.md").write_text("his words, never read\n")
        prompts = self.repo / "docs" / "40 - DevDocs" / "prompts" / today.isoformat()
        prompts.mkdir(parents=True)
        (prompts / "01-x-job-card.md").write_text("JOB: x-job\n")
        (prompts / "02-y-brain.md").write_text("prompt\n")
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "constructed desk day")

        self.sessions = root / "sessions.json"
        self.calls = root / "claude-calls"
        self.set_sessions([
            {"id": PRED, "name": "cto-desk", "cwd": "/nonexistent/desk", "status": "running",
             "state": "idle", "pid": 101, "sessionId": "no-such-session"},
            {"id": "bbbb2222", "name": "alpha-build", "cwd": "/nonexistent/wt", "status": "running",
             "state": "working", "pid": 102, "sessionId": "s2"},
        ])
        stub = root / "bin"
        stub.mkdir()
        # FLIP_AT=<n>: from the n-th `agents` call on, every row answers state idle
        (stub / "claude").write_text(
            "#!/bin/sh\n"
            f'printf "%s\\n" "$*" >> "{self.calls}"\n'
            'if [ "$1" = agents ]; then\n'
            f'    n=$(grep -c "^agents" "{self.calls}")\n'
            '    if [ -n "${FLIP_AT:-}" ] && [ "$n" -ge "$FLIP_AT" ]; then\n'
            f'        sed "s/\\"working\\"/\\"idle\\"/g" "{self.sessions}"\n'
            "    else\n"
            f'        cat "{self.sessions}"\n'
            "    fi\n"
            "fi\n"
            "exit 0\n"
        )
        (stub / "claude").chmod(0o755)
        (root / "home").mkdir()
        self.env = dict(
            os.environ, COBALT_REPO_ROOT=str(self.repo), COBALT_WT_ROOT=str(self.wt),
            PATH=f"{stub}{os.pathsep}{os.environ['PATH']}", HOME=str(root / "home"), **GIT_ENV,
        )

    def set_sessions(self, rows: list[dict]) -> None:
        self.sessions.write_text(json.dumps(rows))

    def ops_copy(self, script: Path, *beside: tuple[str, str | Path]) -> Path:
        ops = self.root / "ops-copy"
        ops.mkdir(exist_ok=True)
        shutil.copy(script, ops / script.name)
        for name, src in beside:
            if isinstance(src, Path):
                shutil.copy(src, ops / name)
            else:
                (ops / name).write_text(src)
        return ops / script.name

    def run(self, script: Path, *args: str, **extra: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["sh", str(script), *args], env=dict(self.env, **extra),
            capture_output=True, text=True, timeout=120,
        )

    def call_lines(self) -> list[str]:
        return self.calls.read_text().splitlines() if self.calls.exists() else []


def heading_block(out: str, name: str) -> str:
    lines = out.splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(f"== {name}"))
    body = []
    for line in lines[start + 1:]:
        if line.startswith("== "):
            break
        body.append(line)
    return "\n".join(body)


# ---- desk-wake.sh ---------------------------------------------------------------------


def test_wake_prints_the_desk_state_in_order_and_changes_nothing(tmp_path):
    desk = Desk(tmp_path)
    before = tree_hash(desk.repo, desk.wt)
    done = desk.run(WAKE)
    assert done.returncode == 0, done.stderr
    out = done.stdout
    heads = [line for line in out.splitlines() if line.startswith("== ")]
    assert [h.split(" ")[1] for h in heads] == [
        "LAST", "SESSIONS", "§0", "§4", "§5", "PENDING", "PROMPTS", "GIT",
    ]
    assert heading_block(out, "LAST").strip() == "HANDOVER: predecessor aaaa1111 → successor bbbb2222 at 08:30 ET"
    sessions = heading_block(out, "SESSIONS")
    assert f"{PRED} cto-desk /nonexistent/desk running idle" in sessions
    assert "bbbb2222 alpha-build" in sessions
    assert "zero-marker" in heading_block(out, "§0")

    rows = heading_block(out, "§4")
    for n in ("four", "five", "six"):
        assert f"row {n} text" in rows
    for n in ("one", "two", "three"):
        assert f"row {n} text" not in rows
    assert "08:30" in next(h for h in heads if h.startswith("== §4"))

    current = heading_block(out, "§5")
    assert "current-marker" in current
    assert "history-marker" not in out

    pending = heading_block(out, "PENDING")
    assert "row four text" in pending
    assert "yesterday pending row" in pending
    assert "yesterday plain row" not in pending
    assert all(len(line) <= 300 for line in pending.splitlines())
    assert "APPROVED — pending fold" not in next(
        line for line in pending.splitlines() if "yesterday pending row" in line
    )  # cut at 300 characters, before its status column

    prompts = heading_block(out, "PROMPTS")
    assert "01-x-job-card.md" in prompts and "02-y-brain.md" in prompts
    assert "constructed desk day" in heading_block(out, "GIT")
    assert "CONTEXT" not in out
    assert tree_hash(desk.repo, desk.wt) == before


def test_wake_with_no_handover_line_prints_every_row(tmp_path):
    desk = Desk(tmp_path)
    desk.today.write_text(TODAY_REPORT.replace("HANDOVER: predecessor aaaa1111 → successor bbbb2222 at 08:30 ET\n", ""))
    done = desk.run(WAKE)
    assert done.returncode == 0, done.stderr
    rows = heading_block(done.stdout, "§4")
    for n in ("one", "two", "three", "four", "five", "six"):
        assert f"row {n} text" in rows
    assert heading_block(done.stdout, "LAST").strip() == "| old | history-marker |"


def test_wake_with_an_id_prints_the_context_line_beside_it(tmp_path):
    desk = Desk(tmp_path)
    script = desk.ops_copy(WAKE, ("desk-context.sh", '#!/bin/sh\necho "context 123 of 400000 — ok for $1"\n'))
    done = desk.run(script, "abcd1234")
    assert done.returncode == 0, done.stderr
    assert heading_block(done.stdout, "CONTEXT").strip() == "context 123 of 400000 — ok for abcd1234"


def test_wake_refuses_a_bad_id(tmp_path):
    desk = Desk(tmp_path)
    done = desk.run(WAKE, "abc;rm")
    assert done.returncode == 1
    assert "REFUSED" in done.stderr


# ---- desk-handover.sh -----------------------------------------------------------------


def handover(desk: Desk, pred: str = PRED, **extra: str) -> subprocess.CompletedProcess:
    script = desk.ops_copy(HANDOVER, ("wait-desk-idle.sh", OPS / "wait-desk-idle.sh"))
    return desk.run(script, pred, **extra)


def test_an_idle_predecessor_is_stopped_then_removed(tmp_path):
    desk = Desk(tmp_path)
    done = handover(desk)
    assert done.returncode == 0, done.stdout + done.stderr
    acts = [line for line in desk.call_lines() if not line.startswith("agents")]
    assert acts == [f"stop {PRED}", f"rm {PRED}"]
    printed = [line for line in done.stdout.splitlines() if line.startswith("RUN: ")]
    assert printed == [f"RUN: claude stop {PRED}", f"RUN: claude rm {PRED}"]


def test_a_predecessor_still_working_is_refused_and_never_stopped(tmp_path):
    desk = Desk(tmp_path)
    rows = json.loads(desk.sessions.read_text())
    rows[0]["state"] = "working"
    desk.set_sessions(rows)
    done = handover(desk, DESK_HANDOVER_WAIT="1")
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: predecessor still working" in done.stderr
    assert not [line for line in desk.call_lines() if not line.startswith("agents")]


def test_a_timeout_then_not_working_is_stopped(tmp_path):
    """The wait times out, then LIST shows the predecessor no longer working: stop, rm."""
    desk = Desk(tmp_path)
    rows = json.loads(desk.sessions.read_text())
    rows[0]["state"] = "working"
    desk.set_sessions(rows)
    # calls 1 (the name check) and 2 (the wait's one look) answer working; 3 answers idle
    done = handover(desk, DESK_HANDOVER_WAIT="1", FLIP_AT="3")
    assert done.returncode == 0, done.stdout + done.stderr
    assert "TIMEOUT" in done.stdout
    acts = [line for line in desk.call_lines() if not line.startswith("agents")]
    assert acts == [f"stop {PRED}", f"rm {PRED}"]


@pytest.mark.parametrize("name", ["brain", "cto-desk-2", "alpha-build", ""])
def test_a_session_not_named_cto_desk_is_refused(tmp_path, name):
    desk = Desk(tmp_path)
    rows = json.loads(desk.sessions.read_text())
    rows[0]["name"] = name
    desk.set_sessions(rows)
    done = handover(desk)
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert [line for line in desk.call_lines() if not line.startswith("agents")] == []


def test_an_id_not_in_the_list_is_refused(tmp_path):
    desk = Desk(tmp_path)
    done = handover(desk, pred="dddd4444")
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert [line for line in desk.call_lines() if not line.startswith("agents")] == []


@pytest.mark.parametrize("bad", ["", "abc", "aaaa1111;x", "../aaaa1111", "AAAA1111"])
def test_a_bad_id_is_refused_before_any_call(tmp_path, bad):
    desk = Desk(tmp_path)
    done = handover(desk, pred=bad)
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert desk.call_lines() == []


# ---- the check (card 18 X3, RECORDS item 7) -------------------------------------------


def _stub_agents_from(desk: Desk, n: int, later: str) -> None:
    """`agents` calls before the n-th answer the sessions file; from the n-th on, `later`."""
    (desk.root / "bin" / "claude").write_text(
        "#!/bin/sh\n"
        f'printf "%s\\n" "$*" >> "{desk.calls}"\n'
        'if [ "$1" = agents ]; then\n'
        f'    k=$(grep -c "^agents" "{desk.calls}")\n'
        f'    if [ "$k" -ge {n} ]; then printf "%s" \'{later}\'; else cat "{desk.sessions}"; fi\n'
        "fi\n"
        "exit 0\n"
    )


def _working(desk: Desk) -> None:
    rows = json.loads(desk.sessions.read_text())
    rows[0]["state"] = "working"
    desk.set_sessions(rows)


def _nothing_stopped(desk: Desk, done: subprocess.CompletedProcess) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED" in done.stderr
    assert not [line for line in desk.call_lines() if not line.startswith("agents")]


def test_check_o1_a_list_read_that_fails_during_the_wait_never_stops_a_working_desk(tmp_path):
    desk = Desk(tmp_path)
    _working(desk)
    _stub_agents_from(desk, 2, "")
    _nothing_stopped(desk, handover(desk, DESK_HANDOVER_WAIT="30"))


def test_check_o3_a_handover_line_without_et_still_cuts_the_rows(tmp_path):
    desk = Desk(tmp_path)
    desk.today.write_text(TODAY_REPORT.replace("at 08:30 ET\n", "at 08:30\n"))
    done = desk.run(WAKE)
    assert done.returncode == 0, done.stderr
    rows = heading_block(done.stdout, "§4")
    assert "row four text" in rows
    assert "row three text" not in rows
