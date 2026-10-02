"""ops/desk/bare-guard.py, the PreToolUse hook of his 2026-10-01 R45 part 1 (card 17 A1).

Every case runs the script as a subprocess with the hook's JSON on stdin, the way
Claude Code calls a PreToolUse hook. Exit 0 lets the call through; exit 2 blocks it
and its stderr is the one line the session reads.
"""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
GUARD = REPO / "ops" / "desk" / "bare-guard.py"
BLOCK_HEAD = "NOT A REFUSAL. Dejan's rule: one bare command per call, and this call contains "
BLOCK_TAIL = (
    ". Resend the SAME commands now, one per call, in order. "
    "Do not report this to Dejan as a failure."
)


def guard(stdin: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["python3", str(GUARD)], input=stdin, capture_output=True, text=True, timeout=60
    )


def bash(command: str) -> str:
    return json.dumps(
        {"hook_event_name": "PreToolUse", "tool_name": "Bash", "tool_input": {"command": command}}
    )


PASS = [
    "ls -la /tmp",
    'git commit -m "a; b and c > d"',
    'COBALT_ENV=dev uv run cobalt db query --side user "SELECT a || b FROM t"',
    'grep -n -E "^(BUILT|FAILED)" file',
    'codex exec -s read-only "Reply OK." < /dev/null',
    'git commit -m "first line\nsecond line"',
    "grep -n -F 'a | b && c' file",
    "echo it\\'s",
]


@pytest.mark.parametrize("command", PASS)
def test_a_bare_command_passes(command):
    done = guard(bash(command))
    assert done.returncode == 0, done.stderr
    assert done.stderr == ""


BLOCK = [
    ("ls && ls", "`&&`"),
    ("cd x; ls", "`;`"),
    ("ls | head", "a pipe `|`"),
    ("ls || ls", "`||`"),
    ("echo hi > f", "a redirect `>`"),
    ("sort < f", "a redirect `<`"),
    ("sleep 2 &", "a background `&`"),
    ("ls\nls", "a newline"),
    ("echo $(date)", "`$(`"),
    ('echo "$(date)"', "`$(`"),
    ("echo `date`", "a backtick"),
    ('echo "`date`"', "a backtick"),
    ("ls < /dev/null && ls", "`&&`"),
]


@pytest.mark.parametrize("command,found", BLOCK)
def test_a_compound_command_is_blocked_naming_what_was_found(command, found):
    done = guard(bash(command))
    assert done.returncode == 2, done.stderr
    line = done.stderr.strip()
    assert line.startswith(BLOCK_HEAD), line
    assert line.endswith(BLOCK_TAIL), line
    assert found in line[len(BLOCK_HEAD) : -len(BLOCK_TAIL)], line


def test_the_block_line_is_exactly_the_ruled_text():
    done = guard(bash("ls && ls"))
    assert done.stderr == BLOCK_HEAD + "`&&`" + BLOCK_TAIL + "\n"


def test_the_dev_null_exception_is_only_the_exact_ending():
    assert guard(bash('codex exec "x" < /dev/null')).returncode == 0
    assert guard(bash('codex exec "x" < /dev/null ')).returncode == 2
    assert guard(bash('codex exec "x" </dev/null')).returncode == 2
    assert guard(bash('codex exec "x" < /dev/nullx')).returncode == 2


@pytest.mark.parametrize(
    "stdin",
    [
        json.dumps({"tool_name": "Read", "tool_input": {"file_path": "/a && b"}}),
        json.dumps({"tool_name": "Edit", "tool_input": {"command": "ls && ls"}}),
        "{not json",
        "",
        json.dumps({"tool_name": "Bash", "tool_input": {"command": 5}}),
        json.dumps({"tool_name": "Bash"}),
        json.dumps([1, 2]),
    ],
)
def test_another_tool_or_a_broken_input_passes(stdin):
    done = guard(stdin)
    assert done.returncode == 0, done.stderr
