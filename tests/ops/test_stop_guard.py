"""ops/desk/stop-guard.py, the worker's Stop hook (card prompts/2026-10-03/09-worker-watch-card.md S1)
and the desk seat's (card prompts/2026-10-06/66-desk-stop-guard-card.md G1-G6).

Every run stages a copy of the hook whose worktree root is re-pointed at tmp_path/wt and whose repo
at tmp_path/repo; the hook JSON is built per case with a constructed transcript, card and report.
Nothing outside tmp_path is read or written (the watch tests start one `sh` under tmp_path and
read the process list through the hook's pgrep).
"""

import json
import os
import re
import signal
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

OPS = Path(__file__).resolve().parents[2] / "ops" / "desk"
SENTENCE = (
    "NOT A REFUSAL. Your report's last line is not a stop line. Write the step's stop line, "
    "or FAILED: <step> — <what> — <reason>, or ASK DESK: <one question>, then stop."
)
HUB = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts"


def stage(tmp_path: Path) -> Path:
    """Copy ops/desk/stop-guard.py with its worktree root re-pointed at tmp_path/wt and its repo
    (the quoted constant only) at tmp_path/repo."""
    text = (OPS / "stop-guard.py").read_text()
    text = text.replace("/Users/cobalt/cobalt-wt", str(tmp_path / "wt"))
    text = text.replace('"/Users/cobalt/cobalt"', '"%s"' % (tmp_path / "repo"))
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


# ---- the desk seat (card 66 G1-G6) ---------------------------------------------------------

DESK_LINE = "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly."
UNGUARDED = "stop-guard: desk not guarded — "
GAVE_UP = re.compile(r"^\S+ s-1 GAVE UP after 3 blocks — start it: ")
ROW = "b43daef9-0000 · x-job-build · ~/cobalt-wt/x · busy · working"


def today() -> str:
    """The ET date as the hook computes it."""
    return str(datetime.now(ZoneInfo("America/New_York")).date())


class Desk:
    """The staged repo as the desk's cwd, a desk transcript and today's desk report."""

    def __init__(self, tmp_path: Path, first: str = DESK_LINE, kind: str | None = "bg"):
        self.tmp = tmp_path
        self.kind = kind
        self.hook = stage(tmp_path)
        self.repo = tmp_path / "repo"
        reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        reports.mkdir(parents=True)
        self.report = reports / f"cto-{today()}.md"
        self.transcript = tmp_path / "desk.jsonl"
        self.count = Path(str(self.transcript) + ".desk-stop")
        self.desk_stop = tmp_path / "wt" / ".job-state" / "DESK-STOP"
        self.first(first)

    def first(self, text: str) -> None:
        """The launch entry carries `"sessionKind": <kind>` (card 106 G1); kind=None omits it."""
        launch = {"type": "user", "message": {"role": "user", "content": text}, "sessionId": "s-1"}
        if self.kind is not None:
            launch["sessionKind"] = self.kind
        lines = [
            {"type": "summary", "summary": "x"},
            {"type": "user", "isMeta": True, "message": {"role": "user", "content": "caveat"}},
            launch,
            {"type": "assistant", "message": {"role": "assistant",
                                              "content": [{"type": "text", "text": "ok"}]}},
            {"type": "user", "message": {"role": "user", "content": DESK_LINE}},
        ]
        self.transcript.write_text("".join(json.dumps(x) + "\n" for x in lines))

    def owed(self, *block: str, heading: str = "## §5 CURRENT") -> None:
        """Today's report in the desk's shape: the block under `heading`, then the session table."""
        self.report.write_text(
            "# CTO desk\n\n## §0 Headline\nx\n\n## §4\n| R | t |\n|---|---|\n\n"
            f"{heading}\n" + "".join(x + "\n" for x in block) + "\n"
            "| session | id | prompt · tab | watch | waits for → then |\n|---|---|---|---|---|\n"
            "| CTO desk | `0000aaaa` | x | none | x |\n\n## §5 HISTORY\n| x |\n"
        )

    def lister(self, *rows: str, code: int = 0) -> None:
        """A fake desk-list.sh beside the staged hook."""
        body = "".join("printf '%%s\\n' '%s'\n" % r for r in rows)
        (self.hook.parent / "desk-list.sh").write_text(f"#!/bin/sh\n{body}exit {code}\n")

    def run(self, active: bool = False, cwd=None):
        event = {
            "session_id": "s-1", "transcript_path": str(self.transcript),
            "cwd": str(self.repo if cwd is None else cwd), "hook_event_name": "Stop",
            "stop_hook_active": active,
        }
        return subprocess.run(
            ["python3", str(self.hook)], input=json.dumps(event),
            capture_output=True, text=True, timeout=60, env=dict(os.environ, LC_ALL="C"),
        )


def missing(d: Desk) -> str:
    return f"start it: the OWED block under ## §5 CURRENT of {d.report}\n"


# G1 — the desk seat


def test_g1_the_desk_with_no_owed_block_is_blocked(tmp_path):
    d = Desk(tmp_path)
    d.owed()
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", missing(d))


@pytest.mark.parametrize("kind", [None, "fg"], ids=["key-absent", "fg"])
def test_g1_a_foreground_session_that_read_the_wake_up_is_not_the_desk(tmp_path, kind):
    """Card 106 G1: the desk is a background session; the same launch text in any other seat
    lets the turn end silently."""
    d = Desk(tmp_path, kind=kind)
    d.owed()
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g1_a_cwd_below_the_repo_is_the_desk(tmp_path):
    d = Desk(tmp_path)
    d.owed()
    assert d.run(cwd=d.repo / "src").returncode == 2


@pytest.mark.parametrize(
    "first",
    [
        f"Read '{HUB}/BRAIN-HUB.md' and follow it exactly.",
        f"Read '{HUB}/DEPLOY-HUB.md' and follow it exactly. CARD: '{HUB}/2026-01-02/01-x-card.md'",
        f"Read '{HUB}/CLOSE-HUB.md' and follow it exactly.",
        f"Read '{HUB}/2026-10-06/65-draft-desk-stop-guard.md' and follow it exactly.",
        "Please open CTO-DESK-WAKEUP.md and follow it exactly.",
        f"Read '{HUB}/BRAIN-HUB.md' first. Then Read '{HUB}/CTO-DESK-WAKEUP.md' and follow it.",
    ],
    ids=["brain", "deploy", "close", "prompt-seat", "prose", "later-read"],
)
def test_g1_no_other_seat_in_the_repo_is_the_desk(tmp_path, first):
    d = Desk(tmp_path, first=first)
    d.owed()
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g1_the_desk_message_outside_the_repo_is_not_the_desk(tmp_path):
    d = Desk(tmp_path)
    d.owed()
    (tmp_path / "repo-other").mkdir()
    r = d.run(cwd=tmp_path / "repo-other")
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g1_an_unreadable_desk_transcript_is_not_the_desk(tmp_path):
    d = Desk(tmp_path)
    d.owed()
    d.transcript.unlink()
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


# G2 — the OWED block


def test_g2_owed_none_lets_the_turn_end(tmp_path):
    d = Desk(tmp_path)
    d.owed("owed: none")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g2_an_item_waiting_on_him_lets_the_turn_end(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: fold R1 | waiting on Dejan")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g2_an_item_with_no_marker_blocks(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", "start it: rebuild x\n")


def test_g2_an_item_with_an_unknown_marker_blocks(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x | later")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: rebuild x\n")


def test_g2_no_report_for_today_blocks(tmp_path):
    d = Desk(tmp_path)
    assert not d.report.exists()
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", missing(d))


def test_g2_a_report_with_no_current_section_blocks(tmp_path):
    d = Desk(tmp_path)
    d.report.write_text("# CTO desk\n\n## §0 Headline\nowed: none\n")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, missing(d))


def test_g2_the_block_under_history_only_blocks(tmp_path):
    d = Desk(tmp_path)
    d.report.write_text(
        "# CTO desk\n\n## §5 CURRENT\n| session | id |\n|---|---|\n\n## §5 HISTORY\nowed: none\n"
    )
    r = d.run()
    assert (r.returncode, r.stderr) == (2, missing(d))


def test_g2_the_block_before_a_blank_line_and_the_table_is_read_as_the_block(tmp_path):
    d = Desk(tmp_path)
    d.owed("owed: none")
    assert "owed: none\n\n| session |" in d.report.read_text()
    assert d.run().returncode == 0
    d.owed("OWED: a | waiting on Dejan", "OWED: b")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: b\n")


# G3 — live is checked, not trusted


def test_g3_a_live_session_id_lets_the_turn_end(tmp_path):
    d = Desk(tmp_path)
    d.lister(ROW)
    d.owed("OWED: build x | live: b43daef9")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g3_a_session_id_with_no_row_blocks(tmp_path):
    d = Desk(tmp_path)
    d.lister("c0ffee00-0000 · y-job-build · ~/cobalt-wt/y · busy · working")
    d.owed("OWED: build x | live: b43daef9")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: build x\n")


def test_g3_the_desks_own_row_is_not_live(tmp_path):
    d = Desk(tmp_path)
    d.lister("b43daef9-0000 · cto-desk · ~/cobalt · busy · working")
    d.owed("OWED: build x | live: b43daef9")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: build x\n")


def test_g3_a_short_id_is_not_live(tmp_path):
    d = Desk(tmp_path)
    d.lister("ab12cdef-0000 · x-job-build · ~/cobalt-wt/x · busy · working")
    d.owed("OWED: build x | live: ab12")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: build x\n")


def watcher(tmp_path: Path, watched: Path) -> subprocess.Popen:
    """A staged wait-stop-line.sh on `watched`: one `sh` whose command line names the path."""
    script = tmp_path / "w" / "wait-stop-line.sh"
    script.parent.mkdir(exist_ok=True)
    script.write_text("#!/bin/sh\nsleep 60\n")
    return subprocess.Popen(["sh", str(script), str(watched)], start_new_session=True)


def test_g3_a_running_watch_on_the_path_lets_the_turn_end(tmp_path):
    d = Desk(tmp_path)
    watched = tmp_path / "x-job-build.md"
    d.owed(f"OWED: watch x | live: watch {watched}")
    p = watcher(tmp_path, watched)
    try:
        r = d.run()
    finally:
        os.killpg(p.pid, signal.SIGKILL)
        p.wait()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g3_a_watch_with_no_process_blocks(tmp_path):
    d = Desk(tmp_path)
    watched = tmp_path / "x-job-build.md"
    d.owed(f"OWED: watch x | live: watch {watched}")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: watch x\n")


# G4 — the block and the count


def test_g4_three_blocks_then_the_fourth_stop_gives_up_and_records(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x")
    codes = [d.run(active=a).returncode for a in (False, True, True, True)]
    assert codes == [2, 2, 2, 0]
    lines = d.desk_stop.read_text().splitlines()
    assert len(lines) == 1 and GAVE_UP.match(lines[0]), lines
    assert lines[0].endswith("start it: rebuild x")
    assert not d.count.exists()
    r = d.run(active=False)
    assert (r.returncode, r.stderr) == (2, "start it: rebuild x\n"), "a new message resets the count"


def test_g4_a_new_message_resets_the_count(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x")
    assert [d.run(active=a).returncode for a in (False, True)] == [2, 2]
    assert d.count.read_text().strip() == "2"
    assert d.run(active=False).returncode == 2
    assert d.count.read_text().strip() == "1"


def test_g4_a_settled_block_removes_the_count(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x")
    assert d.run().returncode == 2
    assert d.count.exists()
    d.owed("owed: none")
    r = d.run(active=True)
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")
    assert not d.count.exists()
    assert not d.desk_stop.exists()


def test_g4_the_first_unsettled_item_is_named(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: w | waiting on Dejan", "OWED: a", "OWED: b")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", "start it: a\n")


# G5 — fail open, never a loop


def unguarded(r) -> None:
    assert r.returncode == 0, r
    assert r.stderr.startswith(UNGUARDED) and r.stderr.count("\n") == 1, r.stderr


def test_g5_a_garbage_block_fails_open(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED:  | | live:")
    unguarded(d.run())


@pytest.mark.parametrize(
    "block",
    [
        ("OWED: x | live: b43daef9 | waiting on Dejan",),
        ("owed: none", "OWED: x | waiting on Dejan"),
        ("OWED: x | live: ",),
    ],
    ids=["two-bars", "none-beside-an-item", "empty-live"],
)
def test_g5_an_unparseable_block_fails_open(tmp_path, block):
    d = Desk(tmp_path)
    d.owed(*block)
    unguarded(d.run())


def test_g5_a_directory_at_the_report_path_fails_open(tmp_path):
    d = Desk(tmp_path)
    d.report.mkdir()
    unguarded(d.run())


UNREADABLE = "session list unreadable — fix it\n"


def test_g2_a_failing_desk_list_blocks(tmp_path):
    """Card 106 G2: an unreadable session list blocks, it never lets the desk end unguarded."""
    d = Desk(tmp_path)
    d.lister(ROW, code=1)
    d.owed("OWED: build x | live: b43daef9")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", UNREADABLE)


def test_g2_no_desk_list_beside_the_hook_blocks(tmp_path):
    d = Desk(tmp_path)
    assert not (d.hook.parent / "desk-list.sh").exists()
    d.owed("OWED: build x | live: b43daef9")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", UNREADABLE)


def test_g2_a_desk_list_that_times_out_blocks(tmp_path):
    d = Desk(tmp_path)
    (d.hook.parent / "desk-list.sh").write_text("#!/bin/sh\nexec sleep 40\n")
    d.owed("OWED: build x | live: b43daef9")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", UNREADABLE)


def test_g2_an_unreadable_list_gives_up_after_three_blocks_and_records(tmp_path):
    d = Desk(tmp_path)
    d.lister(ROW, code=1)
    d.owed("OWED: build x | live: b43daef9")
    codes = [d.run(active=a).returncode for a in (False, True, True, True)]
    assert codes == [2, 2, 2, 0]
    lines = d.desk_stop.read_text().splitlines()
    assert len(lines) == 1, lines
    assert re.match(r"^\S+ s-1 GAVE UP after 3 blocks — session list unreadable — fix it$", lines[0]), lines
    assert not d.count.exists()


def test_g2_owed_none_never_runs_a_failing_list(tmp_path):
    d = Desk(tmp_path)
    d.lister(ROW, code=1)
    d.owed("owed: none")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g5_a_directory_at_the_count_file_fails_open(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x")
    d.count.mkdir()
    unguarded(d.run())


def test_g5_active_with_no_count_file_fails_open(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x")
    assert not d.count.exists()
    unguarded(d.run(active=True))


def test_g5_a_count_file_out_of_range_fails_open(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: rebuild x")
    d.count.write_text("7\n")
    unguarded(d.run(active=True))


@pytest.mark.parametrize(
    "block",
    [("OWED: ",), ("OWED: a | waiting on Dejan", "OWED: ")],
    ids=["alone", "after-an-item"],
)
def test_check_o1_an_empty_item_line_fails_open(tmp_path, block):
    d = Desk(tmp_path)
    d.owed(*block)
    unguarded(d.run())


def test_g3_a_relative_path_cannot_match_an_unrelated_watch(tmp_path):
    d = Desk(tmp_path)
    watched = tmp_path / "elsewhere" / "x-job-build.md"
    d.owed("OWED: watch x | live: watch x-job-build.md")
    p = watcher(tmp_path, watched)
    try:
        r = d.run()
    finally:
        os.killpg(p.pid, signal.SIGKILL)
        p.wait()
    assert (r.returncode, r.stderr) == (2, "start it: watch x\n")


def test_g5_a_bare_empty_item_fails_open(tmp_path):
    d = Desk(tmp_path)
    d.owed("OWED: ")
    r = d.run()
    assert r.returncode == 0, r
    assert r.stderr.startswith(UNGUARDED) and r.stderr.count("\n") == 1, r.stderr
