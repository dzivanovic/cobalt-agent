"""ops/desk/desk-watch.sh, the desk's ONE watch command (card 17 A2).

Every run reads a tmp card and tmp reports; the poll interval is cut by
DESK_WATCH_POLL so the waits take seconds.
"""

from __future__ import annotations

import os
import subprocess
import threading
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
WATCH = REPO / "ops" / "desk" / "desk-watch.sh"


@pytest.fixture
def card(tmp_path):
    reports = tmp_path / "reports"
    reports.mkdir()
    build = reports / "x-job-build.md"
    check = reports / "x-job-check.md"
    card = tmp_path / "01-x-job-card.md"
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: 1a2b3c4d\nTIP: 5e6f7a8b\nREPORT: {build}\nCHECK REPORT: {check}\n"
        "HOUSE B: as needed\nTREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n"
    )
    env = dict(os.environ, DESK_WATCH_POLL="1")
    return card, build, check, env


def watch(*args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(WATCH), *args], env=env, capture_output=True, text=True, timeout=120
    )


def test_a_report_already_at_its_stop_line_returns_at_once(card):
    card, build, check, env = card
    build.write_text("# x\n\nbody\n\nBUILT · job: x · tip: 1a2b3c4d\n\n")
    started = time.monotonic()
    done = watch("build", str(card), "30", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "BUILT · job: x · tip: 1a2b3c4d"
    assert time.monotonic() - started < 5


def test_a_changed_last_line_that_matches_returns_it(card):
    card, build, check, env = card
    build.write_text("# x\n\n(run in progress)\n")

    def finish():
        time.sleep(2)
        build.write_text("# x\n\nFAILED: W — x\n")

    writer = threading.Thread(target=finish)
    writer.start()
    done = watch("build", str(card), "30", env=env)
    writer.join()
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "FAILED: W — x"


def test_kind_check_reads_the_check_report_not_the_report(card):
    card, build, check, env = card
    build.write_text("BUILT · job: x\n")
    check.write_text("# check\n\nCHECK DONE · job: x\n")
    done = watch("check", str(card), "30", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "CHECK DONE · job: x"
    # negative control: a BUILT line in the CHECK REPORT is no stop line of a check
    check.write_text("BUILT · job: x\n")
    done = watch("check", str(card), "2", env=env)
    assert done.returncode == 2
    assert "STILL RUNNING" in done.stdout


def test_a_stop_word_in_the_middle_of_the_file_does_not_fire(card):
    card, build, check, env = card
    build.write_text("BUILT · job: x\n\n(run in progress — next step under ## CONTINUE)\n")
    done = watch("build", str(card), "3", env=env)
    assert done.returncode == 2
    assert done.stdout.strip() == (
        "STILL RUNNING after 3s — last line: (run in progress — next step under ## CONTINUE)"
    )


def test_no_change_within_the_limit_exits_2(card):
    card, build, check, env = card
    build.write_text("(run in progress)\n")
    started = time.monotonic()
    done = watch("build", str(card), "3", env=env)
    assert done.returncode == 2
    assert done.stdout.startswith("STILL RUNNING after 3s")
    assert time.monotonic() - started >= 3


def test_a_missing_report_is_waited_for(card):
    card, build, check, env = card

    def appear():
        time.sleep(2)
        build.write_text("BUILT · job: x\n")

    writer = threading.Thread(target=appear)
    writer.start()
    done = watch("build", str(card), "30", env=env)
    writer.join()
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "BUILT · job: x"


def test_more_than_7000_seconds_is_refused(card):
    card, build, check, env = card
    build.write_text("BUILT · job: x\n")
    done = watch("build", str(card), "7001", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert done.stdout == ""


@pytest.mark.parametrize(
    "kind,line",
    [
        ("deploy", "DEPLOYED · tag: x"),
        ("devfix", "REBUILT · job: x"),
        ("deploy", "FAILED: G — x"),
    ],
)
def test_each_kind_reads_its_own_stop_word(card, kind, line):
    card, build, check, env = card
    build.write_text(line + "\n")
    done = watch(kind, str(card), "30", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == line


def test_close_takes_the_report_path_itself(card, tmp_path):
    card, build, check, env = card
    close = tmp_path / "close-2026-01-02.md"
    close.write_text("CLOSE PUSHED · day: x\n")
    done = watch("close", str(close), "30", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "CLOSE PUSHED · day: x"


@pytest.mark.parametrize(
    "args",
    [("ship", "CARD", "30"), ("build", "CARD", "x"), ("build", "NOCARD", "30"), ("build",)],
)
def test_a_bad_call_is_refused(card, args):
    card, build, check, env = card
    build.write_text("BUILT · job: x\n")
    mapped = [
        str(card) if a == "CARD" else str(card.parent / "missing.md") if a == "NOCARD" else a
        for a in args
    ]
    done = watch(*mapped, env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
