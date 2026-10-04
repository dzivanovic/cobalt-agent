"""ops/desk/desk-watch.sh, the desk's ONE watch command (card 17 A2; card 09 W1, the idle exit).

Every run reads a tmp card and tmp reports; the poll interval is cut by
DESK_WATCH_POLL so the waits take seconds. The watch runs from a staged copy under
tmp_path/ops (with wait-stop-line.sh, whose --idle probe it calls) whose worktree root is
re-pointed at tmp_path/wt, so the WAKE file is tmp_path/wt/.job-state/WAKE; desk-list.sh
beside it is a stub that answers from tmp_path/answers (one LIST answer per call, the last
one repeated; default `busy · working`). Nothing outside tmp_path is read or run.
"""

from __future__ import annotations

import os
import subprocess
import threading
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
OPS = REPO / "ops" / "desk"
WATCH: Path  # set per test by the card fixture: the staged copy


def stage(tmp_path: Path) -> Path:
    """Stage desk-watch.sh and wait-stop-line.sh, a passing guard and the LIST stub."""
    ops = tmp_path / "ops"
    ops.mkdir(exist_ok=True)
    for name in ("desk-watch.sh", "wait-stop-line.sh"):
        text = (OPS / name).read_text().replace("/Users/cobalt/cobalt-wt", str(tmp_path / "wt"))
        (ops / name).write_text(text)
    (ops / "desk-context.sh").write_text("exit 0\n")
    # each call prints the next line of `answers` as the rows of the sessions it names:
    # `<name> <status> <state>` words, `;` between rows, `none` for no row; the last repeats
    (ops / "desk-list.sh").write_text(
        f'a="{tmp_path}/answers"; c="{tmp_path}/list-calls"\n'
        'echo call >> "$c"\n'
        'if [ -f "$a" ]; then\n'
        '  n=$(($(wc -l < "$c"))); t=$(($(wc -l < "$a"))); [ "$n" -le "$t" ] || n=$t\n'
        '  row=$(sed -n "${n}p" "$a")\n'
        'else\n'
        '  row="x-job-build busy working;x-job-check busy working;x-job-devfix busy working;'
        'deploy-hub-x-job busy working;close-0102 busy working"\n'
        'fi\n'
        '[ "$row" = none ] && exit 0\n'
        'printf "%s\\n" "$row" | tr ";" "\\n" | while read -r name status state; do\n'
        '  echo "aaaa0001 · $name · ~/cobalt-wt/x-job · $status · $state"\n'
        'done\n'
    )
    return ops / "desk-watch.sh"


@pytest.fixture
def card(tmp_path):
    global WATCH
    WATCH = stage(tmp_path)
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


def answers(tmp_path: Path, *rows: str) -> None:
    (tmp_path / "answers").write_text("".join(r + "\n" for r in rows))


SEVEN = "# x\n\none\n\ntwo\nthree\nfour\n\nfive\nsix\n(run in progress — next step under ## CONTINUE)\n\n"
LAST_FIVE = ["three", "four", "five", "six", "(run in progress — next step under ## CONTINUE)"]
WAKE_LINE = "2026-01-02T10:00:00-05:00 x-job IDLE (run in progress — next step under ## CONTINUE)"


def append_wake(tmp_path: Path, line: str) -> None:
    wake = tmp_path / "wt" / ".job-state" / "WAKE"
    wake.parent.mkdir(parents=True, exist_ok=True)
    with wake.open("a") as f:
        f.write(line + "\n")


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


# ---- card 09 W1: the watch exits on idle --------------------------------------------------------

def test_w1_a_session_idle_for_two_polls_exits_3_with_the_idle_line_and_five_lines(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle blocked")
    done = watch("build", str(card), "20", env=env)
    assert done.returncode == 3, done.stdout + done.stderr
    assert done.stdout.splitlines() == ["IDLE: x-job-build — no WAKE line", *LAST_FIVE]
    assert (tmp_path / "list-calls").read_text().count("call") == 2


def test_w1_one_idle_poll_between_busy_ones_never_fires(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle done", "x-job-build busy working",
            "x-job-build idle done", "x-job-build busy working",
            "x-job-build idle done", "x-job-build busy working")
    done = watch("build", str(card), "6", env=env)
    assert done.returncode == 2, done.stdout
    assert done.stdout.startswith("STILL RUNNING after 6s")


def test_w1_idle_with_state_working_is_a_background_run_not_idle(card, tmp_path):
    """X3: a worker inside a long background run shows `idle · working`; the state decides."""
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle working")
    done = watch("build", str(card), "4", env=env)
    assert done.returncode == 2, done.stdout
    assert done.stdout.startswith("STILL RUNNING after 4s")


def test_w1_a_changed_last_line_restarts_the_idle_count(card, tmp_path):
    card, build, check, env = card
    build.write_text("(run in progress — next step under ## CONTINUE)\n")
    answers(tmp_path, "x-job-build idle blocked")

    def progress():
        time.sleep(1.5)
        build.write_text("RESUMED: E2 11:00\n")

    writer = threading.Thread(target=progress)
    writer.start()
    started = time.monotonic()
    done = watch("build", str(card), "20", env=env)
    writer.join()
    assert done.returncode == 3, done.stdout
    assert done.stdout.splitlines()[0] == "IDLE: x-job-build — no WAKE line"
    # poll 1 idle; poll 2 sees a new last line and counts it as the first idle; poll 3 fires
    assert (tmp_path / "list-calls").read_text().count("call") == 3
    assert time.monotonic() - started >= 3


def test_w1_a_wake_line_for_the_worktree_exits_3_at_the_first_poll(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle blocked")

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, WAKE_LINE)

    writer = threading.Thread(target=wake)
    writer.start()
    done = watch("build", str(card), "20", env=env)
    writer.join()
    assert done.returncode == 3, done.stdout
    assert done.stdout.splitlines() == [f"IDLE: x-job-build — {WAKE_LINE}", *LAST_FIVE]
    assert (tmp_path / "list-calls").read_text().count("call") == 1


def test_w1_old_wake_lines_and_other_worktrees_never_fire(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    # idle polls open the WAKE gate; a busy one between them keeps the two-poll rule quiet
    answers(tmp_path, "x-job-build idle done", "x-job-build busy working",
            "x-job-build idle done", "x-job-build busy working")
    append_wake(tmp_path, WAKE_LINE)  # before the watch began

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, "2026-01-02T10:01:00-05:00 x-job-other IDLE prose")
        append_wake(tmp_path, "2026-01-02T10:01:00-05:00 y-job IDLE x-job")

    writer = threading.Thread(target=wake)
    writer.start()
    done = watch("build", str(card), "3", env=env)
    writer.join()
    assert done.returncode == 2, done.stdout
    assert done.stdout.startswith("STILL RUNNING after 3s")


def test_w1_a_wake_line_while_the_listing_shows_the_session_working_does_not_fire(card, tmp_path):
    """X3: the listing's state decides; a WAKE line beside `working` is a background wait."""
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle working")

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, WAKE_LINE)

    writer = threading.Thread(target=wake)
    writer.start()
    done = watch("build", str(card), "3", env=env)
    writer.join()
    assert done.returncode == 2, done.stdout


def test_w1_a_wake_line_raised_while_working_is_spent_by_the_busy_poll(card, tmp_path):
    """X3 (check O1): a WAKE line beside `working` is a background wait; one idle poll after it
    is not two."""
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle working", "x-job-build idle done",
            "x-job-build busy working", "x-job-build busy working")

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, WAKE_LINE)

    writer = threading.Thread(target=wake)
    writer.start()
    done = watch("build", str(card), "4", env=env)
    writer.join()
    assert done.returncode == 2, done.stdout
    assert done.stdout.startswith("STILL RUNNING after 4s")


def test_w1_busy_with_a_changed_stop_line_exits_0_as_today(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build busy working")

    def finish():
        time.sleep(1.5)
        build.write_text("# x\n\nBUILT · job: x-job · tip: 1a2b3c4d\n")

    writer = threading.Thread(target=finish)
    writer.start()
    done = watch("build", str(card), "20", env=env)
    writer.join()
    assert done.returncode == 0, done.stdout
    assert done.stdout.strip() == "BUILT · job: x-job · tip: 1a2b3c4d"


def test_w1_a_stop_line_written_as_the_session_goes_idle_wins(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle done")

    def finish():
        time.sleep(1.5)
        build.write_text("# x\n\nFAILED: W — x\n")
        append_wake(tmp_path, WAKE_LINE)  # the idle hook fires as the worker ends its turn

    writer = threading.Thread(target=finish)
    writer.start()
    done = watch("build", str(card), "20", env=env)
    writer.join()
    assert (done.returncode, done.stdout.strip()) == (0, "FAILED: W — x")


def test_w1_a_session_not_in_the_listing_exits_3_gone(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-check busy working")
    done = watch("build", str(card), "20", env=env)
    assert done.returncode == 3, done.stdout
    assert done.stdout.splitlines() == ["GONE: x-job-build", *LAST_FIVE]
    assert (tmp_path / "list-calls").read_text().count("call") == 2


def test_w1_one_missing_listing_between_busy_ones_is_not_gone(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "none", "x-job-build busy working", "none", "x-job-build busy working",
            "x-job-build busy working")
    done = watch("build", str(card), "5", env=env)
    assert done.returncode == 2, done.stdout


def test_w1_two_rows_of_the_session_are_idle_only_when_both_are(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle done;x-job-build busy working")
    assert watch("build", str(card), "3", env=env).returncode == 2
    (tmp_path / "list-calls").unlink(missing_ok=True)
    answers(tmp_path, "x-job-build idle done;x-job-build idle blocked")
    assert watch("build", str(card), "20", env=env).returncode == 3


@pytest.mark.parametrize(
    "kind,session",
    [("check", "x-job-check"), ("devfix", "x-job-devfix"), ("deploy", "deploy-hub-x-job")],
)
def test_w1_each_kind_watches_its_own_session_name(card, tmp_path, kind, session):
    card, build, check, env = card
    build.write_text(SEVEN)
    check.write_text(SEVEN)
    answers(tmp_path, f"{session} idle blocked;x-job-build busy working")
    done = watch(kind, str(card), "20", env=env)
    assert done.returncode == 3, done.stdout
    assert done.stdout.splitlines()[0] == f"IDLE: {session} — no WAKE line"


def test_w1_close_watches_close_mmdd(card, tmp_path):
    card, build, check, env = card
    close = tmp_path / "close-2026-01-02.md"
    close.write_text(SEVEN)
    answers(tmp_path, "close-0102 idle blocked")
    done = watch("close", str(close), "20", env=env)
    assert done.returncode == 3, done.stdout
    assert done.stdout.splitlines()[0] == "IDLE: close-0102 — no WAKE line"


def test_w1_a_close_report_not_named_by_its_date_is_refused(card, tmp_path):
    card, build, check, env = card
    close = tmp_path / "close-notes.md"
    close.write_text(SEVEN)
    done = watch("close", str(close), "20", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")


def test_w1_no_desk_list_beside_the_watch_is_refused_not_gone(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    (WATCH.parent / "desk-list.sh").unlink()
    done = watch("build", str(card), "20", env=env)
    assert done.returncode == 1, done.stdout
    assert "desk-list.sh" in done.stderr and done.stderr.startswith("REFUSED: ")
    assert "GONE" not in done.stdout


def test_w1_an_unreadable_listing_is_never_gone(card, tmp_path):
    card, build, check, env = card
    build.write_text(SEVEN)
    (WATCH.parent / "desk-list.sh").write_text('echo "Traceback" >&2\nexit 1\n')
    done = watch("build", str(card), "3", env=env)
    assert done.returncode == 2, done.stdout


def test_w1_wait_stop_line_with_a_session_exits_3_on_idle(tmp_path):
    stage(tmp_path)
    script = tmp_path / "ops" / "wait-stop-line.sh"
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    (bin_ / "sleep").write_text(f'#!/bin/sh\necho "$1" >> "{tmp_path}/sleep-calls"\n')
    (bin_ / "sleep").chmod(0o755)
    env = dict(os.environ, PATH=f"{bin_}:{os.environ['PATH']}")
    report = tmp_path / "wt" / "x-job" / "docs" / "r.md"
    report.parent.mkdir(parents=True)
    report.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle blocked")
    r = subprocess.run(["sh", str(script), str(report), "^(BUILT|FAILED)", "200", "x-job-build"],
                       env=env, capture_output=True, text=True, timeout=60)
    assert r.returncode == 3, r.stdout + r.stderr
    assert r.stdout.splitlines() == ["IDLE: x-job-build — no WAKE line", *LAST_FIVE]
    # a WAKE line for the worktree of the report path fires at the first poll
    (tmp_path / "list-calls").unlink(missing_ok=True)

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, WAKE_LINE)

    (bin_ / "sleep").write_text(f'#!/bin/sh\necho "$1" >> "{tmp_path}/sleep-calls"\n/bin/sleep 1\n')
    writer = threading.Thread(target=wake)
    writer.start()
    r = subprocess.run(["sh", str(script), str(report), "^(BUILT|FAILED)", "200", "x-job-build"],
                       env=env, capture_output=True, text=True, timeout=60)
    writer.join()
    assert r.returncode == 3, r.stdout + r.stderr
    assert r.stdout.splitlines()[0] == f"IDLE: x-job-build — {WAKE_LINE}"


def test_w1_wait_stop_line_reads_wake_for_a_report_outside_the_worktrees(tmp_path):
    """Check O2: a check or devfix report lives on main; the worktree is the fifth argument."""
    stage(tmp_path)
    script = tmp_path / "ops" / "wait-stop-line.sh"
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    (bin_ / "sleep").write_text("#!/bin/sh\n/bin/sleep 1\n")
    (bin_ / "sleep").chmod(0o755)
    env = dict(os.environ, PATH=f"{bin_}:{os.environ['PATH']}")
    report = tmp_path / "main" / "docs" / "x-job-check.md"
    report.parent.mkdir(parents=True)
    report.write_text(SEVEN)
    answers(tmp_path, "x-job-check idle blocked")

    def wake():
        time.sleep(0.3)
        append_wake(tmp_path, WAKE_LINE)

    writer = threading.Thread(target=wake)
    writer.start()
    r = subprocess.run(
        ["sh", str(script), str(report), "^(CHECK DONE|FAILED)", "200", "x-job-check", "x-job"],
        env=env, capture_output=True, text=True, timeout=60)
    writer.join()
    assert r.returncode == 3, r.stdout + r.stderr
    assert r.stdout.splitlines() == [f"IDLE: x-job-check — {WAKE_LINE}", *LAST_FIVE]


def test_w1_wait_stop_line_without_a_session_reads_no_listing(tmp_path):
    """Negative control: the three-argument call is today's watch (G3 pins the rest)."""
    stage(tmp_path)
    script = tmp_path / "ops" / "wait-stop-line.sh"
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    (bin_ / "sleep").write_text("#!/bin/sh\n")
    (bin_ / "sleep").chmod(0o755)
    env = dict(os.environ, PATH=f"{bin_}:{os.environ['PATH']}")
    report = tmp_path / "wt" / "x-job" / "docs" / "r.md"
    report.parent.mkdir(parents=True)
    report.write_text(SEVEN)
    answers(tmp_path, "x-job-build idle blocked")
    r = subprocess.run(["sh", str(script), str(report), "^(BUILT|FAILED)", "60"],
                       env=env, capture_output=True, text=True, timeout=60)
    assert r.returncode == 2
    assert r.stdout.startswith("TIMEOUT after 60s")
    assert not (tmp_path / "list-calls").exists()
