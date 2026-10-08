"""The desk's close-wait rule in prompts/CTO-DESK-WAKEUP.md (card 2026-10-08 106 G5; his 10-08 R658).

(a) reads the wake-up for the rule's fixed parts. (b) and (c) run a copy of
ops/desk/wait-stop-line.sh under tmp_path, with a stub desk-context.sh beside it (exit 0, the
tests/ops/test_install_ops.py way), on a constructed close report: the two outcomes the rule
acts on, a timeout (exit 2) and a CLOSE PUSHED last line (exit 0). Nothing outside tmp_path is
read or written but the two repo files.
"""

from __future__ import annotations

import subprocess
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WAKEUP = REPO / "docs" / "40 - DevDocs" / "prompts" / "CTO-DESK-WAKEUP.md"
WAIT = REPO / "ops" / "desk" / "wait-stop-line.sh"

DAY = "2031-05-14"
DONE_LINE = "CLOSE PUSHED abc1234 · days: 1 · ledger: 2 lines · decisions: 0 · for Dejan: 0"


def stage(tmp_path: Path) -> Path:
    ops = tmp_path / "ops"
    ops.mkdir()
    script = ops / "wait-stop-line.sh"
    script.write_text(WAIT.read_text())
    script.chmod(0o755)
    stub = ops / "desk-context.sh"
    stub.write_text("#!/bin/sh\nexit 0\n")
    stub.chmod(0o755)
    return script


def test_the_wakeup_holds_the_close_wait_rule():
    text = WAKEUP.read_text()
    for part in (
        "CLOSE WAIT (his 10-08 R658)",
        "wait-stop-line.sh \"<close report>\" '^CLOSE PUSHED '",
        "desk-launch.sh close <date> yourself",
    ):
        assert part in text, part


def test_the_wait_on_a_missing_close_report_times_out_with_exit_2(tmp_path):
    script = stage(tmp_path)
    report = tmp_path / f"close-{DAY}.md"
    done = subprocess.run(
        ["sh", str(script), str(report), "^CLOSE PUSHED ", "1"],
        capture_output=True, text=True, timeout=60,
    )
    assert done.returncode == 2, done
    assert "TIMEOUT after 1s" in done.stdout


def test_the_wait_ends_with_exit_0_when_the_close_pushes(tmp_path):
    script = stage(tmp_path)
    report = tmp_path / f"close-{DAY}.md"
    report.write_text(f"# close {DAY}\n\n(run in progress — next step under ## CONTINUE)\n")
    p = subprocess.Popen(
        ["sh", str(script), str(report), "^CLOSE PUSHED ", "60"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    )
    time.sleep(2)
    report.write_text(f"# close {DAY}\n\n## RECORDS\n\n{DONE_LINE}\n")
    out, err = p.communicate(timeout=60)
    assert p.returncode == 0, (out, err)
    assert out.splitlines() == [DONE_LINE]
