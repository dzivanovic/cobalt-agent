"""ops/desk/stop-guard.py, the worker's Stop hook (card prompts/2026-10-03/09-worker-watch-card.md S1).

Every run stages a copy of the hook whose worktree root is re-pointed at tmp_path/wt; the hook
JSON is built per case with a constructed transcript, card and report. Nothing outside tmp_path
is read or written.
"""

import json
import os
import subprocess
from pathlib import Path

import pytest

OPS = Path(__file__).resolve().parents[2] / "ops" / "desk"
SENTENCE = (
    "NOT A REFUSAL. Your report's last line is not a stop line. Write the step's stop line, "
    "or FAILED: <step> — <what> — <reason>, or ASK DESK: <one question>, then stop."
)
HUB = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts"


def stage(tmp_path: Path) -> Path:
    """Copy ops/desk/stop-guard.py with its worktree root re-pointed at tmp_path/wt."""
    text = (OPS / "stop-guard.py").read_text()
    text = text.replace("/Users/cobalt/cobalt-wt", str(tmp_path / "wt"))
    dst = tmp_path / "ops" / "stop-guard.py"
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(text)
    return dst


class World:
    """A worktree under the staged root with a card, its report and a session transcript."""

    def __init__(self, tmp_path: Path, hub: str = "BUILD-HUB.md"):
        self.tmp = tmp_path
        self.hook = stage(tmp_path)
        self.wt = tmp_path / "wt" / "x-job-0102"
        reports = self.wt / "docs" / "40 - DevDocs" / "reports"
        reports.mkdir(parents=True)
        self.report = reports / "x-job-build-2026-01-02.md"
        self.check_report = reports / "x-job-check-2026-01-02.md"
        self.card = tmp_path / "cards" / "01-x-job-card.md"
        self.card.parent.mkdir()
        self.card.write_text(
            "JOB: x-job\nBRANCH: ops/x-job-0102\nWORKTREE: x-job-0102\nBASE: 1a2b3c4d\nTIP:\n"
            f"REPORT: {self.report}\nCHECK REPORT: {self.check_report}\nDB: none\n\n## ROWS\n"
        )
        self.transcript = tmp_path / "transcript.jsonl"
        self.launch(hub)

    def launch(self, hub: str, prefix: str = "") -> None:
        """The transcript in the real line shape; its first user message is the hub launch line."""
        text = f"{prefix}Read '{HUB}/{hub}' and follow it exactly. CARD: '{self.card}'"
        lines = [
            {"type": "summary", "summary": "x"},
            {"type": "user", "isMeta": True, "message": {"role": "user", "content": "caveat"}},
            {"type": "user", "message": {"role": "user", "content": text},
             "uuid": "u-1", "sessionId": "s-1"},
            {"type": "assistant", "message": {"role": "assistant",
                                              "content": [{"type": "text", "text": "ok"}]}},
            {"type": "user", "message": {"role": "user", "content": "CARD: 'not-this-one'"}},
        ]
        self.transcript.write_text("".join(json.dumps(x) + "\n" for x in lines))

    def run(self, cwd=None, active: bool = False, raw: str | None = None):
        event = {
            "session_id": "s-1", "transcript_path": str(self.transcript),
            "cwd": str(self.wt if cwd is None else cwd), "hook_event_name": "Stop",
            "stop_hook_active": active,
        }
        return subprocess.run(
            ["python3", str(self.hook)], input=json.dumps(event) if raw is None else raw,
            capture_output=True, text=True, timeout=30, env=dict(os.environ, LC_ALL="C"),
        )


def test_a_built_last_line_lets_the_turn_end(tmp_path):
    w = World(tmp_path)
    w.report.write_text("# r\n\nbody\n\nBUILT · job: x-job · tip: 1a2b3c4d\n\n")
    r = w.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_a_prose_last_line_blocks_once_with_the_sentence(tmp_path):
    w = World(tmp_path)
    w.report.write_text("# r\n\nBUILT · job: x-job\n\nI will now wait for the suite.\n")
    r = w.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", SENTENCE + "\n")


def test_the_same_prose_with_stop_hook_active_ends_the_turn(tmp_path):
    """The loop guard: the second Stop of the same turn is never blocked."""
    w = World(tmp_path)
    w.report.write_text("# r\n\nI will now wait for the suite.\n")
    r = w.run(active=True)
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_the_desk_and_the_brain_cwd_is_exempt_and_reads_no_report(tmp_path):
    w = World(tmp_path)
    # a transcript that does not parse would block a worker: here it is never opened
    w.transcript.write_text("not json\n")
    w.report.write_text("prose\n")
    for cwd in ("/Users/cobalt/cobalt", str(tmp_path / "wt"), str(tmp_path / "wt-other" / "x")):
        r = w.run(cwd=cwd)
        assert (r.returncode, r.stdout, r.stderr) == (0, "", ""), cwd


def test_no_report_file_blocks_with_the_sentence(tmp_path):
    """A worker with no report has not started its fixed file."""
    w = World(tmp_path)
    assert not w.report.exists()
    r = w.run()
    assert (r.returncode, r.stderr) == (2, SENTENCE + "\n")


@pytest.mark.parametrize(
    "line",
    [
        "BUILT · job: x-job · tip: 1a2b3c4d | on 1a2b3c4d",
        "CHECK DONE · job: x-job · pass: 1",
        "DEPLOYED deploy-2026-10-03-1 at 1a2b3c4d · smoke GREEN",
        "REBUILT · user.x max_attnum 3 → 4",
        "FAILED: E2 — a held lock — reason",
        "FAILED PREFLIGHT: branch",
        "FAILED: W — x · rollback: not used",
        "ASK DESK: which file? [10:00]",
        "(run in progress — next step under ## CONTINUE)",
    ],
)
def test_every_stop_shape_lets_the_turn_end(tmp_path, line):
    w = World(tmp_path)
    w.report.write_text(f"# r\n\nprose\n\n{line}\n  \n")
    r = w.run()
    assert (r.returncode, r.stderr) == (0, "")


@pytest.mark.parametrize(
    "line",
    [
        "RESUMED: E2 11:00",
        "next: E3",
        "CONTINUE: W. the lock is free",
        "  BUILT · job: x-job",
        "The build is BUILT · job: x-job",
        "CHECK DONE",
    ],
)
def test_a_line_that_only_looks_like_a_stop_line_blocks(tmp_path, line):
    w = World(tmp_path)
    w.report.write_text(f"# r\n\n{line}\n")
    r = w.run()
    assert (r.returncode, r.stderr) == (2, SENTENCE + "\n")


def test_a_check_session_reads_the_check_report_not_the_build_report(tmp_path):
    w = World(tmp_path, hub="CHECK-HUB.md")
    w.report.write_text("BUILT · job: x-job · tip: 1a2b3c4d\n")
    r = w.run()
    assert (r.returncode, r.stderr) == (2, SENTENCE + "\n"), "no check report yet: blocked"
    w.check_report.write_text("# c\n\nCHECK DONE · job: x-job · pass: 1\n")
    r = w.run()
    assert (r.returncode, r.stderr) == (0, "")
    # PASS-2 and a CONTINUE prefix keep the same hub
    w.launch("CHECK-HUB.md", prefix="PASS-2. ")
    w.check_report.write_text("# c\n\nprose\n")
    assert w.run().returncode == 2


def test_a_resumed_session_reads_the_card_of_its_launch_message(tmp_path):
    w = World(tmp_path)
    w.launch("BUILD-HUB.md", prefix="CONTINUE: W. ")
    w.report.write_text("FAILED: W — x\n")
    assert w.run().returncode == 0


def test_a_cwd_below_the_worktree_is_a_worker(tmp_path):
    w = World(tmp_path)
    w.report.write_text("prose\n")
    r = w.run(cwd=w.wt / "src")
    assert r.returncode == 2


def test_s2_a_worktree_seat_whose_first_message_names_no_card_never_blocks(tmp_path):
    """S2 (a), check O1: a `prompt` seat under the worktrees has no CARD: and no fixed report."""
    w = World(tmp_path)
    w.report.write_text("# r\n\nI will now wait for the suite.\n")
    r = w.run()
    assert (r.returncode, r.stderr) == (2, SENTENCE + "\n"), "the same prose with CARD: blocks"
    w.transcript.write_text(json.dumps(
        {"type": "user", "message": {"role": "user",
                                     "content": [{"type": "text", "text": "fix the watch in ops/desk"}]}}
    ) + "\n")
    r = w.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_a_transcript_with_no_first_message_blocks(tmp_path):
    """No launch message to read (missing transcript, or none in it): not provably a prompt seat."""
    w = World(tmp_path)
    w.report.write_text("BUILT · job: x-job\n")
    w.transcript.write_text(json.dumps({"type": "summary", "summary": "x"}) + "\n")
    assert w.run().returncode == 2
    w.transcript.unlink()
    assert w.run().returncode == 2


def test_a_list_shaped_first_message_names_its_card(tmp_path):
    w = World(tmp_path)
    w.report.write_text("BUILT · job: x-job\n")
    text = f"Read '{HUB}/BUILD-HUB.md' and follow it exactly. CARD: '{w.card}'"
    w.transcript.write_text(json.dumps(
        {"type": "user", "message": {"role": "user", "content": [{"type": "text", "text": text}]}}
    ) + "\n")
    assert w.run().returncode == 0


def test_an_empty_report_value_blocks(tmp_path):
    w = World(tmp_path, hub="CHECK-HUB.md")
    w.card.write_text(w.card.read_text().replace(f"CHECK REPORT: {w.check_report}", "CHECK REPORT:"))
    w.check_report.write_text("CHECK DONE · job: x-job\n")
    assert w.run().returncode == 2


def test_unreadable_hook_input_never_blocks(tmp_path):
    w = World(tmp_path)
    r = w.run(raw="not json")
    assert (r.returncode, r.stderr) == (0, "")


def test_i1_run_his_install_text(tmp_path):
    """I1, RUN: prints the header's install object (-rP) and loads it as JSON (the proof)."""
    lines = (OPS / "stop-guard.py").read_text().splitlines()
    body = lines[lines.index("# INSTALL BEGIN") + 1 : lines.index("# INSTALL END")]
    text = "\n".join(x[2:] for x in body)
    held = tmp_path / "install.json"
    held.write_text(text + "\n")
    with open(held) as f:
        json.load(f)
    print(text)


def test_the_hook_writes_nothing(tmp_path):
    w = World(tmp_path)
    w.report.write_text("prose\n")
    before = sorted(p for p in tmp_path.rglob("*"))
    w.run()
    w.run(active=True)
    assert sorted(p for p in tmp_path.rglob("*")) == before
