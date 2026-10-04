"""ops/desk/desk-list.sh — the desk's LIST, tracked beside desk-context.sh (card 2026-10-03/03
adoption-scripts, row L4). A listing row without `id` is skipped and counted, never a
traceback (`KeyError: 'id'`, NOW, OWED).

A stub `claude` on PATH answers `agents --json` with a constructed listing.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
LIST = REPO / "ops" / "desk" / "desk-list.sh"

ROWS = [
    {"id": "0000aaaa-0000", "pid": 11, "name": "cto-desk", "cwd": "/Users/cobalt/cobalt", "status": "busy", "state": "working"},
    {"pid": 12, "name": "no-id-row", "cwd": "/tmp", "status": "idle", "state": "idle"},
    {"id": "0000bbbb-0000", "name": "ended", "cwd": "/tmp", "status": "done", "state": "done"},
    {"id": "0000cccc-0000", "pid": 13, "name": "x-build", "cwd": "/tmp/x", "status": "busy", "state": "working"},
]


def run_list(tmp_path: Path, rows: list[dict]) -> subprocess.CompletedProcess:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir(exist_ok=True)
    listing = tmp_path / "listing.json"
    listing.write_text(json.dumps(rows))
    (bin_dir / "claude").write_text(f'#!/bin/sh\ncat "{listing}"\n')
    (bin_dir / "claude").chmod(0o755)
    env = dict(os.environ, PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}")
    return subprocess.run(["sh", str(LIST)], env=env, capture_output=True, text=True, timeout=60)


def test_a_row_without_id_is_skipped_and_counted_not_a_traceback(tmp_path):
    done = run_list(tmp_path, ROWS)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "Traceback" not in done.stderr
    assert done.stdout.splitlines() == [
        "0000aaaa-0000 · cto-desk · ~/cobalt · busy · working",
        "0000cccc-0000 · x-build · /tmp/x · busy · working",
    ]
    assert "skipped 1 live row(s) without an id" in done.stderr


def test_every_row_with_an_id_prints_and_nothing_is_said_on_stderr(tmp_path):
    done = run_list(tmp_path, [r for r in ROWS if "id" in r])
    assert done.returncode == 0, done.stdout + done.stderr
    assert len(done.stdout.splitlines()) == 2
    assert done.stderr == ""
