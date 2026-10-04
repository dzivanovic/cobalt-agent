"""desk-context.sh --guard reads the desk-list.sh BESIDE itself (card 2026-10-03/03
adoption-scripts, row L4: the hermetic guard; ops-seam DECISION 2).

A tmp copy of desk-context.sh sits beside a stub desk-list.sh that records each call and
prints one constructed live row. HOME points at tmp_path and a stub `claude` on PATH records
any call, so a guard that still reads /Users/cobalt/.claude/ops/desk-list.sh (which runs
`claude agents --json`) shows on the call log instead of reaching a real session list.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTEXT = REPO / "ops" / "desk" / "desk-context.sh"


def test_the_guard_calls_the_sibling_desk_list_and_nothing_under_home(tmp_path):
    ops = tmp_path / "ops"
    ops.mkdir()
    shutil.copy(CONTEXT, ops / "desk-context.sh")
    sibling_calls = tmp_path / "sibling-calls"
    (ops / "desk-list.sh").write_text(
        f'printf "called %s\\n" "$*" >> "{sibling_calls}"\n'
        "printf '%s\\n' '0000aaaa-0000 · x-build · ~/x · idle · idle'\n"
    )
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    claude_calls = tmp_path / "claude-calls"
    (bin_dir / "claude").write_text(f'#!/bin/sh\nprintf "%s\\n" "$*" >> "{claude_calls}"\necho "[]"\n')
    (bin_dir / "claude").chmod(0o755)
    env = dict(os.environ, HOME=str(tmp_path / "home"), PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}")
    env.pop("CLAUDE_JOB_DIR", None)
    done = subprocess.run(
        ["sh", str(ops / "desk-context.sh"), "--guard"], env=env, capture_output=True, text=True, timeout=60
    )
    assert done.returncode == 0, done.stdout + done.stderr
    assert sibling_calls.exists(), "the desk-list.sh beside desk-context.sh was not called"
    assert sibling_calls.read_text().splitlines() == ["called "]
    assert not claude_calls.exists(), claude_calls.read_text()
    # no cto-desk row: the guard skips, as DECISION G-A rules
    assert "WARNING: desk size unread — guard skipped" in done.stderr


def test_the_script_names_no_path_under_the_home_ops_folder():
    assert "/Users/cobalt/.claude/ops" not in CONTEXT.read_text()
