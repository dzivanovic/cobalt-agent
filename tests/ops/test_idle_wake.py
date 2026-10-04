"""ops/desk/idle-wake.py, the worker's Notification hook (card prompts/2026-10-03/09-worker-watch-card.md N1).

Every run stages copies of the hook and of stop-guard.py (whose report finder it uses) with the
worktree root re-pointed at tmp_path/wt, so the WAKE file is tmp_path/wt/.job-state/WAKE.
Nothing outside tmp_path is read or written.
"""

import json
import os
import re
import subprocess
from pathlib import Path

OPS = Path(__file__).resolve().parents[2] / "ops" / "desk"
HUB = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts"
# <ISO time with the ET offset> <worktree> IDLE <last line>
LINE = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d-0[45]:00 (\S+) IDLE (.*)$")


class World:
    def __init__(self, tmp_path: Path):
        self.tmp = tmp_path
        ops = tmp_path / "ops"
        ops.mkdir()
        for name in ("idle-wake.py", "stop-guard.py"):
            text = (OPS / name).read_text().replace("/Users/cobalt/cobalt-wt", str(tmp_path / "wt"))
            (ops / name).write_text(text)
        self.hook = ops / "idle-wake.py"
        self.wake = tmp_path / "wt" / ".job-state" / "WAKE"
        self.wt = tmp_path / "wt" / "x-job-0102"
        reports = self.wt / "docs" / "40 - DevDocs" / "reports"
        reports.mkdir(parents=True)
        self.report = reports / "x-job-build-2026-01-02.md"
        self.card = tmp_path / "01-x-job-card.md"
        self.card.write_text(f"JOB: x-job\nWORKTREE: x-job-0102\nREPORT: {self.report}\nCHECK REPORT:\n")
        self.transcript = tmp_path / "transcript.jsonl"
        text = f"Read '{HUB}/BUILD-HUB.md' and follow it exactly. CARD: '{self.card}'"
        self.transcript.write_text(json.dumps({"type": "user", "message": {"role": "user", "content": text}}) + "\n")

    def run(self, kind: str = "idle_prompt", cwd=None, raw: str | None = None):
        event = {
            "session_id": "s-1", "transcript_path": str(self.transcript),
            "cwd": str(self.wt if cwd is None else cwd), "hook_event_name": "Notification",
            "message": "Claude is waiting for your input", "notification_type": kind,
        }
        return subprocess.run(
            ["python3", str(self.hook)], input=json.dumps(event) if raw is None else raw,
            capture_output=True, text=True, timeout=30, env=dict(os.environ, LC_ALL="C"),
        )

    def lines(self) -> list[str]:
        return self.wake.read_text().splitlines() if self.wake.exists() else []


def test_an_idle_notification_appends_one_line_with_the_worktree_and_the_last_line(tmp_path):
    w = World(tmp_path)
    w.report.write_text("# r\n\nbody\n\n(run in progress — next step under ## CONTINUE)\n\n")
    r = w.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")
    (line,) = w.lines()
    m = LINE.match(line)
    assert m, line
    assert m.groups() == ("x-job-0102", "(run in progress — next step under ## CONTINUE)")


def test_no_report_writes_no_report(tmp_path):
    w = World(tmp_path)
    assert w.run().returncode == 0
    (line,) = w.lines()
    assert LINE.match(line).groups() == ("x-job-0102", "no report")


def test_a_non_idle_notification_writes_nothing(tmp_path):
    w = World(tmp_path)
    w.report.write_text("prose\n")
    for kind in ("permission_prompt", "auth_success", "elicitation_dialog", ""):
        assert w.run(kind=kind).returncode == 0
    assert not w.wake.exists()
    assert not w.wake.parent.exists()


def test_a_cwd_outside_the_worktrees_writes_nothing(tmp_path):
    w = World(tmp_path)
    w.report.write_text("prose\n")
    for cwd in ("/Users/cobalt/cobalt", str(tmp_path / "wt"), str(tmp_path / "wt-other" / "x")):
        assert w.run(cwd=cwd).returncode == 0
    assert not w.wake.exists()


def test_a_second_idle_appends_a_second_line(tmp_path):
    w = World(tmp_path)
    w.report.write_text("prose one\n")
    w.run()
    w.report.write_text("prose two\n")
    w.run(cwd=w.wt / "src")
    lines = w.lines()
    assert [LINE.match(x).groups() for x in lines] == [
        ("x-job-0102", "prose one"), ("x-job-0102", "prose two")]


def test_the_hook_never_blocks(tmp_path):
    w = World(tmp_path)
    r = w.run(raw="not json")
    assert (r.returncode, r.stderr) == (0, "")
    # an unwritable WAKE folder: still exit 0
    (tmp_path / "wt" / ".job-state").write_text("a file where the folder should be")
    w.report.write_text("prose\n")
    r = w.run()
    assert r.returncode == 0


def test_the_hook_leaves_no_bytecode_beside_the_scripts(tmp_path):
    w = World(tmp_path)
    w.run()
    assert sorted(p.name for p in (tmp_path / "ops").iterdir()) == ["idle-wake.py", "stop-guard.py"]
