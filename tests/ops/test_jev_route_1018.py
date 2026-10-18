"""The JEV keyed wrapper, its close step and its allow string (card 2026-10-18/715, rows W1-W3).

His 2026-10-18 R1830 (F12): `ops/jev-route.sh` is the one path that opens the OpenRouter key
(JEV design §7). NO KEYED CALL RUNS HERE: every wrapper run is against a stub `uv` on PATH and a
DECOY key file under tmp_path; nothing opens the real key file, the vault, a ledger or a socket.
CLOSE-HUB.md is read from this tree as tests/ops/test_hub_lines.py reads a hub. Every test pins
only the lines this card changes, found by content (brain R1472).
"""

from __future__ import annotations

import fnmatch
import json
import os
import shlex
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
WRAPPER = REPO / "ops" / "jev-route.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
CLOSE = HUBS / "CLOSE-HUB.md"
GUARD = REPO / "ops" / "desk" / "bare-guard.py"

DECOY = "decoy-w1-not-a-key"
SOURCE_LINE = '. "$KEY_FILE"'
EXEC_LINE = 'exec uv run cobalt classify route --day "$2" --run'
EXPORT_LINE = 'export COBALT_VAULT_FILE="/Users/cobalt/cobalt/data/.cobalt_vault"'
W3 = "Bash(sh /Users/cobalt/cobalt/ops/jev-route.sh --day *)"
STEP_CMD = "sh /Users/cobalt/cobalt/ops/jev-route.sh --day <day>"

# CLOSE-HUB.md:10 at drafting (card 715 RECORDS), in order: the lines this card changes
CLOSE_ALLOW_BEFORE = [
    "Read",
    "Grep",
    "Glob",
    "Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)",
    "Edit(//Users/cobalt/cobalt/docs/00 - Project/**)",
    "Edit(//Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md)",
    "Bash(git add *)",
    "Bash(git commit *)",
    "Bash(git status*)",
    "Bash(git log*)",
    "Bash(git diff*)",
    "Bash(git show*)",
    "Bash(git tag --list*)",
    "Bash(COBALT_ENV=production uv run cobalt validate*)",
    "Bash(COBALT_ENV=production uv run cobalt heartbeat show*)",
    "Bash(ls *)",
    "Bash(grep *)",
    "Bash(tail *)",
    "Bash(wc *)",
    "Bash(date*)",
    "Bash(git push origin main)",
]
CLOSE_DENY = [
    "AskUserQuestion",
    "EnterWorktree",
    "Bash(git push*--force*)",
    "Bash(git push* -f*)",
    "Bash(git push*+*)",
    "Bash(git push*:*)",
    "Bash(git push*--delete*)",
    "Bash(git push* -d*)",
    "Bash(git push*--mirror*)",
    "Bash(git push*--all*)",
    "Bash(git push*--tags*)",
]
CLOSE_OTHER_WORDS = [
    "claude", "--bg",
    "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and follow it exactly. DATE: <date>",
    "--model", "claude-sonnet-5-5", "--permission-mode", "dontAsk",
    "--remote-control", "close-<mmdd>", "--name", "close-<mmdd>",
    "--allowedTools", "--disallowedTools",
    "--add-dir", "/Users/cobalt/Vault", "--add-dir", "/Users/cobalt/cobalt",
]


# ---- the line, read as tests/ops/test_hub_lines.py reads it (copied, not imported) ------------


def hub_line(name: str) -> str:
    lines = [ln for ln in (HUBS / name).read_text(encoding="utf-8").splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1, f"{name}: {len(lines)} launch lines"
    return lines[0]


def tools(line: str, option: str) -> list[str]:
    """The strings after `--allowedTools` or `--disallowedTools`, up to the next option."""
    words = shlex.split(line)
    out, inside = [], False
    for w in words:
        if w.startswith("--"):
            inside = w == option
            continue
        if inside:
            out.append(w)
    return out


def other_words(line: str) -> list[str]:
    """The words of the line outside the two tool lists."""
    out, inside = [], False
    for w in shlex.split(line):
        if w.startswith("--"):
            inside = w in ("--allowedTools", "--disallowedTools")
            out.append(w)
            continue
        if not inside:
            out.append(w)
    return out


def close_lines() -> list[str]:
    return CLOSE.read_text(encoding="utf-8").splitlines()


# ---- W1: the wrapper, run against a stub `uv` and a decoy key file -----------------------------


@pytest.fixture
def box(tmp_path):
    home = tmp_path / "home"
    home.mkdir()
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    out = tmp_path / "stub-out"
    sourced = tmp_path / "sourced"
    (home / ".cobalt_key").write_text(f"export COBALT_MASTER_KEY={DECOY}\n" ': > "$W1_SOURCED"\n')
    stub = bin_ / "uv"
    stub.write_text(
        "#!/bin/sh\n"
        'for a in "$@"; do printf "%s\\n" "$a"; done > "$W1_STUB_OUT"\n'
        'pwd >> "$W1_STUB_OUT"\n'
        'printf "%s\\n" "${COBALT_MASTER_KEY:+set}" >> "$W1_STUB_OUT"\n'
        'printf "%s\\n" "$COBALT_VAULT_FILE" >> "$W1_STUB_OUT"\n'
    )
    stub.chmod(0o755)
    env = {"HOME": str(home), "PATH": f"{bin_}:/usr/bin:/bin", "W1_STUB_OUT": str(out), "W1_SOURCED": str(sourced)}

    def run(*args: str) -> subprocess.CompletedProcess:
        return subprocess.run(["sh", str(WRAPPER), *args], env=env, capture_output=True, text=True, timeout=60)

    return {"home": home, "out": out, "sourced": sourced, "run": run}


def test_w1_the_wrapper_text_is_secret_free():
    lines = WRAPPER.read_text(encoding="utf-8").splitlines()
    code = [ln.strip() for ln in lines if ln.strip() and not ln.lstrip().startswith("#")]
    assert code.count(SOURCE_LINE) == 1
    assert code.count('KEY_FILE="$HOME/.cobalt_key"') == 1
    assert len([ln for ln in code if ln.split()[0] == "exec"]) == 1
    assert code[-1] == EXEC_LINE
    assert [ln for ln in code if ln.split()[0] == "export"] == [EXPORT_LINE]
    for banned in ("echo", "printf", "set -x", "printenv", "tee", ">", "COBALT_MASTER", "OPENROUTER", "sk-or-"):
        assert not any(banned in ln for ln in code), banned
    src = code.index(SOURCE_LINE)
    case = [i for i, ln in enumerate(code) if ln.startswith("case ")]
    date = [i for i, ln in enumerate(code) if "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]" in ln]
    refuse = [i for i, ln in enumerate(code) if "exit 64" in ln]
    assert len(case) == 1 and len(date) == 1 and refuse
    assert max(case + date + refuse) < src


def test_w1_one_date_execs_the_router_with_the_decoy(box):
    done = box["run"]("--day", "2026-01-02")
    assert done.returncode == 0, done.stderr
    assert box["out"].read_text().splitlines() == [
        "run", "cobalt", "classify", "route", "--day", "2026-01-02", "--run",
        "/Users/cobalt/cobalt",
        "set",
        "/Users/cobalt/cobalt/data/.cobalt_vault",
    ]
    assert done.stdout == "" and done.stderr == ""
    assert DECOY not in done.stdout + done.stderr


@pytest.mark.parametrize("args", [
    [],
    ["--day"],
    ["2026-01-02"],
    ["--day", "2026-1-02"],
    ["--day", "2026-01-02x"],
    ["--day", "2026-01-02", "--run"],
    ["--day", "2026-01-02; ls"],
    ["--card", "x-card.md"],
    ["--day=2026-01-02"],
])
def test_w1_any_other_argument_is_refused(box, args):
    done = box["run"](*args)
    assert done.returncode == 64, (done.returncode, done.stderr)
    assert not box["out"].exists()      # no `uv` call
    assert not box["sourced"].exists()  # the key file was never sourced
    assert done.stdout == "" and done.stderr == ""


def test_w1_a_missing_key_file_is_exit_78_with_no_call(box):
    (box["home"] / ".cobalt_key").unlink()
    done = box["run"]("--day", "2026-01-02")
    assert done.returncode == 78, (done.returncode, done.stderr)
    assert not box["out"].exists()
    assert done.stdout == "" and done.stderr == ""


# ---- W2: the close step ---------------------------------------------------------------------


def test_w2_the_close_step_runs_the_wrapper_once():
    lines = close_lines()
    heads = [i for i, ln in enumerate(lines) if ln.startswith("## 7b. JEV SHADOW BATCH")]
    assert len(heads) == 1
    (seven,) = [i for i, ln in enumerate(lines) if ln.startswith("## 7. ")]
    (eight,) = [i for i, ln in enumerate(lines) if ln.startswith("## 8. ")]
    assert seven < heads[0] < eight
    body = lines[heads[0] + 1]
    for words in (STEP_CMD, "timeout` 600000", "never retried", "never fails the close and never stops it",
                  "the stop line ignores the step", "Go on to STEP 8",
                  "refused", "key file missing", "tool timeout", "wrapper missing"):
        assert words in body, words
    assert body.count("sh /Users/cobalt/cobalt/ops/jev-route.sh") == 1
    runs = [i for i, ln in enumerate(lines) if "ops/jev-route.sh" in ln and not ln.startswith("claude --bg ")]
    assert runs == [heads[0] + 1]


def test_w2_the_report_shape_names_the_section():
    (shape,) = [ln for ln in close_lines() if ln.startswith("`<REPORT>`, shaped: ")]
    assert shape.count("`## 7 MEASURE` → `## 7b JEV` → `## 8 COMMIT AND PUSH`") == 1


def test_w2_the_stop_line_is_unchanged_by_the_step():
    (stop,) = [ln for ln in close_lines() if ln.startswith("`CLOSE PUSHED ")]
    assert "jev" not in stop and "JEV" not in stop


def test_w2_the_step_command_matches_the_w3_string():
    pattern = "sh /Users/cobalt/cobalt/ops/jev-route.sh --day *"
    assert fnmatch.fnmatchcase("sh /Users/cobalt/cobalt/ops/jev-route.sh --day 2026-01-02", pattern)
    jev = [s for s in tools(hub_line("CLOSE-HUB.md"), "--allowedTools") if "jev-route.sh" in s]
    assert len(jev) == 1
    assert jev[0].startswith("Bash(") and jev[0].endswith(")")
    assert jev[0][len("Bash("):-1] == pattern


def test_w2_control_the_guard_admits_the_close_call(tmp_path):
    """bare-guard.py run as tests/ops/test_bare_guard.py runs it: the close seat (kind None) runs
    STEP 7b's call; no guard change in this job."""
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"  # stands in for /Users/cobalt/cobalt, the close seat's cwd
    wt.mkdir()
    repo.mkdir()
    first = ("Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and follow it exactly. "
             "DATE: 2026-01-02")
    transcript = tmp_path / "t-close.jsonl"
    records = [
        {"type": "queue-operation", "operation": "enqueue", "sessionId": "sess-test-1"},
        {"parentUuid": None, "isSidechain": False, "userType": "external", "cwd": "/constructed",
         "sessionId": "sess-test-1", "type": "user", "message": {"role": "user", "content": first},
         "uuid": "00000000-0000-0000-0000-000000000001", "timestamp": "2026-01-01T13:00:00.000Z"},
    ]
    transcript.write_text("".join(json.dumps(r) + "\n" for r in records))
    event = {
        "session_id": "sess-test-1",
        "transcript_path": str(transcript),
        "cwd": str(repo),
        "permission_mode": "dontAsk",
        "hook_event_name": "PreToolUse",
        "tool_name": "Bash",
        "tool_input": {"command": "sh /Users/cobalt/cobalt/ops/jev-route.sh --day 2026-01-02", "description": "x"},
    }
    env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo))
    done = subprocess.run(["python3", str(GUARD)], input=json.dumps(event), env=env,
                          capture_output=True, text=True, timeout=60)
    assert done.returncode == 0, done.stderr
    assert done.stderr == ""


# ---- W3: the one allow string -----------------------------------------------------------------


def test_w3_the_close_line_gains_exactly_the_one_string():
    line = hub_line("CLOSE-HUB.md")
    allow = tools(line, "--allowedTools")
    assert allow.count(W3) == 1
    assert len(allow) == 22
    assert allow.index(W3) == allow.index("Bash(git push origin main)") + 1
    assert [s for s in allow if s != W3] == CLOSE_ALLOW_BEFORE
    assert tools(line, "--disallowedTools") == CLOSE_DENY
    assert other_words(line) == CLOSE_OTHER_WORDS


def test_w3_no_production_deny_or_allow_changes():
    line = hub_line("CLOSE-HUB.md")
    assert [s for s in tools(line, "--disallowedTools") if "COBALT_ENV" in s] == []
    assert [s for s in tools(line, "--allowedTools") if "COBALT_ENV=production" in s] == [
        "Bash(COBALT_ENV=production uv run cobalt validate*)",
        "Bash(COBALT_ENV=production uv run cobalt heartbeat show*)",
    ]


def test_w3_no_other_line_or_settings_file_names_the_wrapper():
    files = sorted(HUBS.glob("*.md")) + sorted(p for p in (REPO / "ops" / "desk").rglob("*") if p.is_file())
    settings = REPO / ".claude" / "settings.json"
    if settings.is_file():
        files.append(settings)
    naming = [p for p in files if b"ops/jev-route.sh" in p.read_bytes()]
    assert [p for p in naming if p != CLOSE] == []
    lines = close_lines()
    heads = [i for i, ln in enumerate(lines) if ln.startswith("## 7b. ")]
    allowed = {i for i, ln in enumerate(lines) if ln.startswith("claude --bg ")} | {i + 1 for i in heads}
    assert {i for i, ln in enumerate(lines) if "ops/jev-route.sh" in ln} <= allowed


def test_w3_the_list_line_counts_22_and_names_r1830():
    (the_list,) = [ln for ln in close_lines() if ln.startswith("THE LIST: ")]
    assert "22 allow, 11 deny" in the_list
    assert "R1830 (F12)" in the_list
