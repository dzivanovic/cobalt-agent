"""close-timer.sh and its plist (card 2026-10-03 05 close-timer, rows T1 T2).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT, holding a stub ops/desk/desk-launch.sh that records its
arguments), a tmp directory standing in for /Users/cobalt/cobalt-wt
(COBALT_WT_ROOT, where the per-date log lands) and a stub desk-list.sh
(COBALT_DESK_LIST) that prints constructed session rows. `date` is a stub on
PATH: a plain read of the clock answers FAKE_NOW, and a `date -j …` (date
arithmetic, no clock) runs the real /bin/date. Every date is constructed.
"""

from __future__ import annotations

import os
import plistlib
import subprocess
from pathlib import Path

import pytest

from cobalt.jobs import restarts
from cobalt.jobs.restarts import Change, classify

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "close-timer.sh"
PLIST = REPO / "ops" / "desk" / "com.cobalt.close-timer.plist"

EVENING = "2031-05-14"
NEXT_DAY = "2031-05-15"

DATE_STUB = """#!/bin/sh
if [ "$1" = "-j" ]; then exec /bin/date "$@"; fi
for a in "$@"; do fmt=$a; done
exec /bin/date -j -f "%Y-%m-%d %H:%M" "$FAKE_NOW" "$fmt"
"""

# the clock answers FAKE_NOW only when read in ET; any other zone reads a constructed 04:05
DATE_STUB_ET_ONLY = """#!/bin/sh
if [ "$1" = "-j" ]; then exec /bin/date "$@"; fi
for a in "$@"; do fmt=$a; done
now="2031-05-15 04:05"
[ "$TZ" != "America/New_York" ] || now=$FAKE_NOW
exec /bin/date -j -f "%Y-%m-%d %H:%M" "$now" "$fmt"
"""

LAUNCH_STUB = """#!/bin/sh
printf '%s\\n' "$*" >> "$CALLS"
echo "stub launched: $*"
exit 0
"""

LIST_STUB = """#!/bin/sh
[ ! -f "$LIST_FAIL" ] || exit 1
cat "$LIST_ROWS"
"""

CTO = "aaaa1111-0000-4000-8000-000000000001 · cto-desk · ~/cobalt · running · idle"
HUB = "bbbb2222-0000-4000-8000-000000000002 · deploy-hub-set9 · ~/cobalt · running · busy"
# negative control: a name that is not a deploy hub, a cwd that holds the words
LOOKALIKE = "cccc3333-0000-4000-8000-000000000003 · x-build · ~/cobalt-wt/deploy-hub-x · running · busy"

DONE_LINE = "CLOSE PUSHED abc1234 · days: 1 · ledger: 2 lines · decisions: 0 · for Dejan: 0"


@pytest.fixture
def box(tmp_path):
    repo = tmp_path / "repo"
    (repo / "ops" / "desk").mkdir(parents=True)
    (repo / "docs" / "40 - DevDocs" / "reports").mkdir(parents=True)
    launcher = repo / "ops" / "desk" / "desk-launch.sh"
    launcher.write_text(LAUNCH_STUB)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    (bin_dir / "date").write_text(DATE_STUB)
    (bin_dir / "date").chmod(0o755)
    listing = tmp_path / "desk-list.sh"
    listing.write_text(LIST_STUB)
    rows = tmp_path / "rows.txt"
    rows.write_text(CTO + "\n")
    wt = tmp_path / "wt"
    wt.mkdir()

    class Box:
        pass

    b = Box()
    b.repo, b.wt, b.rows, b.launcher = repo, wt, rows, launcher
    b.calls = tmp_path / "calls.txt"
    b.list_fail = tmp_path / "list-fail"
    b.reports = repo / "docs" / "40 - DevDocs" / "reports"

    def run(now: str):
        env = dict(
            os.environ,
            PATH=f"{bin_dir}:{os.environ['PATH']}",
            FAKE_NOW=now,
            COBALT_REPO_ROOT=str(repo),
            COBALT_WT_ROOT=str(wt),
            COBALT_DESK_LIST=str(listing),
            CALLS=str(b.calls),
            LIST_ROWS=str(rows),
            LIST_FAIL=str(b.list_fail),
        )
        return subprocess.run(
            ["sh", str(SCRIPT)], env=env, capture_output=True, text=True, timeout=60
        )

    def calls() -> list[str]:
        return b.calls.read_text().splitlines() if b.calls.exists() else []

    def report(day: str, last: str) -> None:
        (b.reports / f"close-{day}.md").write_text(f"# close {day}\n\n## RECORDS\n\n{last}\n\n")

    b.run, b.calls_made, b.report = run, calls, report
    return b


# ---- T1: the script ------------------------------------------------------------------------


def test_a_free_evening_launches_one_close_of_that_date_and_logs_it(box):
    done = box.run(f"{EVENING} 21:05")
    assert done.returncode == 0, done.stderr
    assert box.calls_made() == [f"close {EVENING}"]
    assert f"LAUNCHED: close {EVENING}" in done.stdout
    log = box.wt / ".timer-logs" / f"close-{EVENING}.log"
    assert f"stub launched: close {EVENING}" in log.read_text()


def test_a_live_deploy_hub_defers_and_launches_nothing(box):
    box.rows.write_text(CTO + "\n" + HUB + "\n")
    done = box.run(f"{EVENING} 21:05")
    assert done.returncode == 0, done.stderr
    assert "DEFERRED: deploy live — deploy-hub-set9" in done.stdout
    assert box.calls_made() == []


def test_a_cwd_that_merely_names_a_deploy_hub_is_not_one(box):
    # negative control: the name field decides, never a substring of the row
    box.rows.write_text(CTO + "\n" + LOOKALIKE + "\n")
    done = box.run(f"{EVENING} 21:05")
    assert "DEFERRED" not in done.stdout
    assert box.calls_made() == [f"close {EVENING}"]


def test_a_finished_close_report_is_done_already(box):
    box.report(EVENING, DONE_LINE)
    done = box.run(f"{EVENING} 22:05")
    assert done.returncode == 0, done.stderr
    assert "DONE ALREADY" in done.stdout
    assert box.calls_made() == []


def test_a_failed_close_report_is_not_done(box):
    # negative control: only the CLOSE PUSHED stop line counts as done
    box.report(EVENING, "FAILED: 8d — push refused — constructed")
    done = box.run(f"{EVENING} 22:05")
    assert "DONE ALREADY" not in done.stdout
    assert box.calls_made() == [f"close {EVENING}"]


def test_a_missing_launcher_is_refused(box):
    box.launcher.unlink()
    done = box.run(f"{EVENING} 21:05")
    assert done.returncode != 0
    assert "REFUSED" in done.stdout + done.stderr
    assert box.calls_made() == []


def test_an_unreadable_session_list_is_refused(box):
    box.list_fail.write_text("x")
    done = box.run(f"{EVENING} 21:05")
    assert done.returncode != 0
    assert "REFUSED" in done.stdout + done.stderr
    assert box.calls_made() == []


def test_at_0105_with_yesterdays_close_absent_the_close_is_yesterdays(box):
    # row T1 (X2): before 04:00 ET the date is the evening's, yesterday's ET date
    done = box.run(f"{NEXT_DAY} 01:05")
    assert done.returncode == 0, done.stderr
    assert box.calls_made() == [f"close {EVENING}"]


def test_at_0105_with_yesterdays_close_done_it_is_done_already(box):
    # row T1: the 00:05–03:05 fires after a finished close launch nothing
    box.report(EVENING, DONE_LINE)
    done = box.run(f"{NEXT_DAY} 01:05")
    assert done.returncode == 0, done.stderr
    assert f"DONE ALREADY: close {EVENING}" in done.stdout
    assert box.calls_made() == []


def test_from_0400_the_date_is_todays(box):
    # row T1: "else today's" — the 04:00 ET line, with yesterday's close still open
    box.run(f"{NEXT_DAY} 04:05")
    assert box.calls_made() == [f"close {NEXT_DAY}"]


def test_the_date_is_read_on_the_et_clock(box):
    # row T1: "(ET, by TZ=America/New_York date +%F)" — 00:05 ET is the evening's fire; the
    # same instant read in another zone (04:05) would close the next date
    (box.wt.parent / "bin" / "date").write_text(DATE_STUB_ET_ONLY)
    done = box.run(f"{NEXT_DAY} 00:05")
    assert done.returncode == 0, done.stderr
    assert box.calls_made() == [f"close {EVENING}"]


def test_a_hub_live_at_2105_and_gone_later_gives_one_launch_that_night(box):
    # X1: deferred at 21:05, launched at the first free fire, done after that
    box.rows.write_text(CTO + "\n" + HUB + "\n")
    assert "DEFERRED" in box.run(f"{EVENING} 21:05").stdout
    assert "DEFERRED" in box.run(f"{EVENING} 22:05").stdout
    box.rows.write_text(CTO + "\n")
    assert f"LAUNCHED: close {EVENING}" in box.run(f"{EVENING} 23:05").stdout
    box.report(EVENING, DONE_LINE)
    assert "DONE ALREADY" in box.run(f"{EVENING} 23:40").stdout
    # after midnight the date is still the evening's: done already, no second call
    for hour in ("00", "01", "02", "03"):
        assert f"DONE ALREADY: close {EVENING}" in box.run(f"{NEXT_DAY} {hour}:05").stdout
    assert box.calls_made() == [f"close {EVENING}"]


def test_the_script_sets_the_c_locale_first():
    lines = [l for l in SCRIPT.read_text().splitlines() if l.strip() and not l.startswith("#")]
    assert lines[0] == "export LC_ALL=C"


# ---- T2: the plist and the derivation ------------------------------------------------------


def test_the_plist_fires_at_2105_and_hourly_to_0305_and_runs_the_script():
    data = plistlib.loads(PLIST.read_bytes())
    assert data["Label"] == "com.cobalt.close-timer"
    assert data["StartCalendarInterval"] == [
        {"Hour": h, "Minute": 5} for h in (21, 22, 23, 0, 1, 2, 3)
    ]
    assert data["ProgramArguments"] == ["sh", "/Users/cobalt/cobalt/ops/desk/close-timer.sh"]
    assert data["StandardOutPath"].startswith("/Users/cobalt/cobalt-wt/.timer-logs/")
    assert data["StandardErrorPath"].startswith("/Users/cobalt/cobalt-wt/.timer-logs/")
    assert data["RunAtLoad"] is False
    # launchd's own PATH holds no `claude`; desk-launch.sh runs it
    assert "/Users/cobalt/.local/bin" in data["EnvironmentVariables"]["PATH"].split(":")


def test_the_timer_derives_no_restart_and_never_escalates(monkeypatch):
    # X3: both files sit under ops/desk/, the operator-script class
    assert PLIST.exists() and SCRIPT.exists()
    monkeypatch.setattr(restarts, "changes", lambda _range: [
        Change("ops/desk/close-timer.sh", "A"),
        Change("ops/desk/com.cobalt.close-timer.plist", "A"),
    ])
    for row in classify("HEAD...HEAD"):
        assert row.rule == "operator script; no Cobalt reader"
        assert row.restarts == ()
        assert row.escalate is False
