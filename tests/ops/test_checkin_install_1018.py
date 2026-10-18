"""checkin-timer.sh, its plist, and the check-in texts (card 2026-10-18 751, rows T1 T2 P1 W1 B1 S1).

Every timer run points the script at a tmp repo (COBALT_REPO_ROOT, a stub desk-launch.sh that
records its arguments and exits ${LAUNCH_EXIT:-0}), a tmp directory (COBALT_WT_ROOT, where the
per-date log lands) and a stub desk-list.sh (COBALT_DESK_LIST) that prints constructed session
rows. The sender is a stub notify.sh (COBALT_NOTIFY). No date stub: the script reads the clock.
Nothing here calls launchctl, claude, or Mattermost.
"""

from __future__ import annotations

import os
import plistlib
import subprocess
from pathlib import Path

import pytest

import test_desk_launch_prechecks as dl
import test_hub_lines as hub_lines
from cobalt.jobs import restarts
from cobalt.jobs.restarts import Change, classify
from test_desk_launch_prechecks import (  # noqa: F401 — desk is the fixture, used by name
    Desk,
    desk,
    dry_prompt,
    staged_launcher,
)

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "checkin-timer.sh"
PLIST = REPO / "ops" / "desk" / "com.cobalt.checkin-timer.plist"
PROMPTS = REPO / "docs" / "40 - DevDocs" / "prompts"
PING = PROMPTS / "CHECKIN-PING.md"
WAKEUP = PROMPTS / "CTO-DESK-WAKEUP.md"
BRAIN = PROMPTS / "BRAIN-HUB.md"
STANDING = PROMPTS / "STANDING-LIST.md"

LAUNCH_STUB = """#!/bin/sh
printf '%s\\n' "$*" >> "$CALLS"
echo "stub launched: $*"
exit "${LAUNCH_EXIT:-0}"
"""

LIST_STUB = """#!/bin/sh
[ ! -f "$LIST_FAIL" ] || exit 1
cat "$LIST_ROWS"
"""

NOTIFY_STUB = """#!/bin/sh
printf '%s\\n' "$*" >> "$NOTIFY_OUT"
"""

DESK_MISSING = "checkin-timer: desk missing — relaunch with desk-launch.sh desk"

CTO = "aaaa1111-0000-4000-8000-000000000001 · cto-desk · ~/cobalt · running · idle"
PING_ROW = "dddd4444-0000-4000-8000-000000000004 · checkin-ping · ~/cobalt · running · idle"
# negative control: the name field is not cto-desk; the cwd merely holds the words
LOOKALIKE = "cccc3333-0000-4000-8000-000000000003 · x-build · ~/cobalt-wt/cto-desk · running · busy"

TRIGGER_PREFIXES = (
    "- A tool or harness gap → ",
    "- Day-open → ",
    "- A CHECK-IN message (checkin-timer.sh ",
    "- A wait written anywhere ",
)
TRIGGER_RULINGS = ("R1854 A", "R1854 B", "R1854 B", "R1854 C")
ALLOW = ["Read", "SendMessage", "Bash(date*)"]


@pytest.fixture
def box(tmp_path):
    repo = tmp_path / "repo"
    (repo / "ops" / "desk").mkdir(parents=True)
    (repo / "docs" / "40 - DevDocs" / "prompts").mkdir(parents=True)
    launcher = repo / "ops" / "desk" / "desk-launch.sh"
    launcher.write_text(LAUNCH_STUB)
    listing = tmp_path / "desk-list.sh"
    listing.write_text(LIST_STUB)
    rows = tmp_path / "rows.txt"
    rows.write_text(CTO + "\n")
    wt = tmp_path / "wt"
    wt.mkdir()
    sender = tmp_path / "notify.sh"
    sender.write_text(NOTIFY_STUB)
    sender.chmod(0o755)

    class Box:
        pass

    b = Box()
    b.repo, b.wt, b.rows, b.launcher, b.listing = repo, wt, rows, launcher, listing
    b.calls = tmp_path / "calls.txt"
    b.list_fail = tmp_path / "list-fail"
    b.notify = tmp_path / "notify.txt"

    def run(extra: dict | None = None, drop: tuple = ()):
        env = dict(
            os.environ,
            COBALT_REPO_ROOT=str(repo),
            COBALT_WT_ROOT=str(wt),
            COBALT_DESK_LIST=str(listing),
            CALLS=str(b.calls),
            LIST_ROWS=str(rows),
            LIST_FAIL=str(b.list_fail),
            COBALT_NOTIFY=str(sender),
            NOTIFY_OUT=str(b.notify),
        )
        env.update(extra or {})
        for k in drop:
            env.pop(k, None)
        return subprocess.run(
            ["sh", str(SCRIPT)], env=env, capture_output=True, text=True, timeout=60,
            cwd=tmp_path,
        )

    def calls() -> list[str]:
        return b.calls.read_text().splitlines() if b.calls.exists() else []

    def notes() -> list[str]:
        return b.notify.read_text().splitlines() if b.notify.exists() else []

    b.run, b.calls_made, b.notes = run, calls, notes
    return b


def refused_line(done) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.startswith("REFUSED: ")][0]


def ping_launch_line(text: str) -> str:
    """The one backticked `claude --bg` span, found by content."""
    mark = "`claude --bg "
    found = []
    for ln in text.splitlines():
        at = ln.find(mark)
        if at == -1:
            continue
        rest = ln[at + 1:]
        end = rest.find("`")
        assert end != -1, ln
        found.append(rest[:end])
    assert len(found) == 1, found
    return found[0]


def lines_under(text: str, heading_prefix: str) -> list[str]:
    lines = text.splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith(heading_prefix))
    body = []
    for ln in lines[start + 1:]:
        if ln.startswith("## "):
            break
        body.append(ln)
    return body


# ---- T1: the script ------------------------------------------------------------------------


def test_t1_a_live_desk_gets_one_ping_launch_and_a_log(box):
    done = box.run()
    assert done.returncode == 0, done.stderr
    prompt = box.repo / "docs" / "40 - DevDocs" / "prompts" / "CHECKIN-PING.md"
    assert box.calls_made() == [f"prompt {prompt}"]
    logs = sorted((box.wt / ".timer-logs").glob("checkin-*.log"))
    assert len(logs) == 1
    assert "fire: checkin" in logs[0].read_text()
    assert f"LAUNCHED: checkin — exit 0 — log {logs[0]}" in done.stdout
    assert not box.notify.exists()


def test_t1_no_cto_desk_row_sends_one_notify_and_launches_nothing(box):
    # negative control: a cwd that holds `cto-desk` is not a desk; the name field decides
    box.rows.write_text(LOOKALIKE + "\n")
    done = box.run()
    assert done.returncode == 1, done.stderr
    assert "DESK MISSING: no check-in sent" in done.stdout
    assert box.notes() == [DESK_MISSING]
    assert box.calls_made() == []


def test_t1_a_live_ping_defers(box):
    box.rows.write_text(CTO + "\n" + PING_ROW + "\n")
    done = box.run()
    assert done.returncode == 0, done.stderr
    ping_id = PING_ROW.split(" · ", 1)[0]
    assert f"DEFERRED: ping live — {ping_id}" in done.stdout
    assert box.calls_made() == []
    assert not box.notify.exists()


def test_t1_a_missing_launcher_is_refused(box):
    box.launcher.unlink()
    done = box.run()
    assert done.returncode == 1, done.stderr
    assert refused_line(done) == f"REFUSED: no launcher: {box.launcher}"
    assert box.notes() == ["checkin-timer: " + refused_line(done)]
    assert box.calls_made() == []


def test_t1_an_unreadable_list_is_refused(box):
    box.list_fail.write_text("x")
    done = box.run()
    assert done.returncode == 1, done.stderr
    assert box.calls_made() == []
    assert box.notes() == [DESK_MISSING, "checkin-timer: " + refused_line(done)]
    box.notify.unlink()
    box.listing.unlink()
    done = box.run()
    assert done.returncode == 1, done.stderr
    assert refused_line(done).startswith("REFUSED: no session list: ")
    assert box.notes() == [DESK_MISSING, "checkin-timer: " + refused_line(done)]
    assert box.calls_made() == []


def test_t1_a_failed_launch_notifies_and_keeps_its_exit(box):
    done = box.run(extra={"LAUNCH_EXIT": "4"})
    assert done.returncode == 4, done.stderr
    logs = sorted((box.wt / ".timer-logs").glob("checkin-*.log"))
    assert len(logs) == 1
    assert f"LAUNCHED: checkin — exit 4 — log {logs[0]}" in done.stdout
    assert box.notes() == [f"checkin-timer: REFUSED: launcher exit 4 — log {logs[0]}"]


# ---- T2: the plist and the derivation ------------------------------------------------------


def test_t2_the_plist_fires_at_0600_1200_1800_2400_and_runs_the_script():
    data = plistlib.loads(PLIST.read_bytes())
    assert data["Label"] == "com.cobalt.checkin-timer"
    assert data["StartCalendarInterval"] == [
        {"Hour": h, "Minute": 0} for h in (6, 12, 18, 0)
    ]
    assert data["ProgramArguments"] == ["sh", "/Users/cobalt/cobalt/ops/desk/checkin-timer.sh"]
    assert data["StandardOutPath"] == "/Users/cobalt/cobalt-wt/.timer-logs/checkin-timer.out"
    assert data["StandardErrorPath"] == "/Users/cobalt/cobalt-wt/.timer-logs/checkin-timer.err"
    assert data["WorkingDirectory"] == "/Users/cobalt/cobalt"
    assert data["RunAtLoad"] is False
    assert "/Users/cobalt/.local/bin" in data["EnvironmentVariables"]["PATH"].split(":")


def test_t2_the_timer_derives_no_restart(monkeypatch):
    assert PLIST.exists() and SCRIPT.exists() and PING.exists()
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("ops/desk/checkin-timer.sh", "A"),
        Change("ops/desk/com.cobalt.checkin-timer.plist", "A"),
        Change("docs/40 - DevDocs/prompts/CHECKIN-PING.md", "A"),
    ])
    got = {row.path: row for row in classify("HEAD...HEAD")}
    for path in ("ops/desk/checkin-timer.sh", "ops/desk/com.cobalt.checkin-timer.plist"):
        assert got[path].rule == "operator script; no Cobalt reader"
        assert got[path].restarts == ()
        assert got[path].escalate is False
    doc = got["docs/40 - DevDocs/prompts/CHECKIN-PING.md"]
    assert doc.rule == "DOCS"
    assert doc.restarts == ()


# ---- P1: the ping prompt, through the real launcher ----------------------------------------


def test_p1_the_real_launcher_accepts_the_ping_line_dry(desk: Desk, tmp_path):
    text = PING.read_text(encoding="utf-8").replace("/Users/cobalt/cobalt", str(desk.repo))
    pfile = desk.prompts / "CHECKIN-PING.md"
    pfile.write_text(text)
    desk.commit("ping")
    done = dl.dry_prompt(desk, tmp_path, pfile)
    assert done.returncode == 0, done.stderr
    line = [ln for ln in done.stdout.splitlines() if ln.startswith("claude --bg ")]
    assert len(line) == 1, done.stdout
    assert line[0].count("--remote-control checkin-ping") == 1
    assert line[0].count("--name checkin-ping") == 1
    assert line[0].count("--permission-mode auto") == 1
    # negative control: acceptEdits is not auto or plan (desk-launch.sh refuses the mode)
    pfile.write_text(text.replace("--permission-mode auto", "--permission-mode acceptEdits"))
    desk.commit("ping refused")
    refused = dl.dry_prompt(desk, tmp_path, pfile)
    assert refused.returncode == 1, refused.stdout + refused.stderr
    assert "permission mode 'acceptEdits'" in refused.stderr


def test_p1_the_ping_line_allows_exactly_three_strings():
    line = ping_launch_line(PING.read_text(encoding="utf-8"))
    assert hub_lines.tools(line, "--allowedTools") == ALLOW


# ---- W1 / B1 / S1: the three fixed files, lines found by content ---------------------------


def test_w1_the_wakeup_carries_the_four_trigger_rows():
    under = lines_under(WAKEUP.read_text(encoding="utf-8"), "ON TRIGGER — open, then act")
    found = []
    for prefix in TRIGGER_PREFIXES:
        hits = [ln for ln in under if ln.startswith(prefix)]
        assert len(hits) == 1, prefix
        found.append(hits[0])
    for ln, ruling in zip(found, TRIGGER_RULINGS, strict=True):
        assert ruling in ln


def test_b1_the_brain_hub_carries_the_check_in_answer():
    lines = BRAIN.read_text(encoding="utf-8").splitlines()
    heads = [i for i, ln in enumerate(lines) if ln == "## CHECK-IN"]
    assert len(heads) == 1
    nxt = lines[heads[0] + 1]
    assert "R1854 B" in nxt
    assert "done · slipping and why · what you changed" in nxt
    judge = next(i for i, ln in enumerate(lines) if ln == "## HOW YOU ANSWER A JUDGE REQUEST")
    measure = next(i for i, ln in enumerate(lines) if ln == "## MEASURE")
    assert judge < heads[0] < measure


def test_s1_the_standing_list_carries_section_10():
    lines = STANDING.read_text(encoding="utf-8").splitlines()
    heads = [i for i, ln in enumerate(lines) if ln.startswith("## 10. THE CHECK-IN TIMER")]
    assert len(heads) == 1
    section = []
    for ln in lines[heads[0]:]:
        if section and ln.startswith("## "):
            break
        section.append(ln)
    assert any("CHECKIN-PING.md" in ln for ln in section)
    table = [ln for ln in section if ln.startswith("|")]
    blob = "\n".join(table)
    for string in ("`Read`", "`SendMessage`", "`Bash(date*)`"):
        assert blob.count(string) == 1, string
