"""ops/desk/desk-done.sh, a finished worker closed in one call (card 17 A5, checklist W8).

`claude` and `herdr` are stubs on PATH that record their arguments; the stub
`claude agents --json` answers a constructed session list. No real session is
touched.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
DONE = REPO / "ops" / "desk" / "desk-done.sh"
AGENTS = [
    {"id": "aaaa1111", "name": "x-job-build", "state": "idle"},
    {"id": "bbbb2222", "name": "brain", "state": "idle"},
    {"id": "cccc3333", "name": "brain-2", "state": "idle"},
    {"id": "dddd4444", "name": "cto-desk", "state": "idle"},
    {"id": "eeee5555", "name": "deploy-hub-x", "state": "idle"},
]


# the stubs' state (card 2026-10-15 580 C1, ASK DESK 12): `claude rm <id>` drops the row from the
# agents file; `herdr tab close <tab>` drops that tab's panes unless the file `keep-panes` exists
STATE = """import json, sys
what, path, value = sys.argv[1:4]
doc = json.load(open(path))
if what == "rm":
    doc = [a for a in doc if not (isinstance(a, dict) and a.get("id") == value)]
else:
    doc["result"]["panes"] = [p for p in doc["result"]["panes"] if p.get("tab_id") != value]
json.dump(doc, open(path, "w"))
"""


@pytest.fixture
def stubs(tmp_path):
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    calls = tmp_path / "calls"
    agents = tmp_path / "agents.json"
    agents.write_text(json.dumps(AGENTS))
    stop_exit = tmp_path / "stop-exit"
    stop_exit.write_text("0")
    panes = tmp_path / "panes.json"
    panes.write_text(json.dumps({"id": "cli:pane:list", "result": {"panes": []}}))
    state = tmp_path / "state.py"
    state.write_text(STATE)
    (bin_ / "claude").write_text(
        "#!/bin/sh\n"
        f'if [ "$1" = agents ]; then cat "{agents}"; exit 0; fi\n'
        f'printf "claude %s\\n" "$*" >> "{calls}"\n'
        f'if [ "$1" = stop ]; then exit "$(cat "{stop_exit}")"; fi\n'
        f'if [ "$1" = rm ]; then python3 "{state}" rm "{agents}" "$2"; fi\n'
        "exit 0\n"
    )
    (bin_ / "herdr").write_text(
        "#!/bin/sh\n"
        f'if [ "$1 $2" = "pane list" ]; then cat "{panes}"; exit 0; fi\n'
        f'printf "herdr %s\\n" "$*" >> "{calls}"\n'
        f'if [ "$1 $2" = "tab close" ] && [ ! -f "{tmp_path}/keep-panes" ]; then\n'
        f'  python3 "{state}" tab "{panes}" "$3"\nfi\n'
        "exit 0\n"
    )
    (bin_ / "claude").chmod(0o755)
    (bin_ / "herdr").chmod(0o755)
    report = tmp_path / "report.md"
    env = dict(os.environ, PATH=f"{bin_}{os.pathsep}{os.environ['PATH']}")
    return report, calls, stop_exit, agents, env


def done_(*args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(DONE), *args], env=env, capture_output=True, text=True, timeout=60
    )


def recorded(calls: Path) -> list[str]:
    return calls.read_text().splitlines() if calls.exists() else []


def test_a_built_report_stops_removes_and_closes_the_tab_in_order(stubs):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("# x\n\nBUILT · job: x-job · tip: 1a2b3c4d\n\n")
    done = done_("aaaa1111", str(report), "build", "w2:tGX", env=env)
    assert done.returncode == 0, done.stderr
    assert recorded(calls) == [
        "claude stop aaaa1111",
        "claude rm aaaa1111",
        "herdr tab close w2:tGX",
    ]
    for call in recorded(calls):
        assert call in done.stdout


def test_without_a_tab_no_herdr_call(stubs):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("CHECK DONE · job: x\n")
    done = done_("aaaa1111", str(report), "check", env=env)
    assert done.returncode == 0, done.stderr
    assert recorded(calls) == ["claude stop aaaa1111", "claude rm aaaa1111"]


@pytest.mark.parametrize("kind", ["build", "check"])
def test_a_failed_build_or_check_is_kept_for_continue(stubs, kind):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("FAILED: W — x\n")
    done = done_("aaaa1111", str(report), kind, "w2:tGX", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: FAILED — the worker is kept for CONTINUE"), done.stderr
    assert recorded(calls) == []


@pytest.mark.parametrize("kind", ["deploy", "devfix", "close"])
def test_a_failed_deploy_devfix_or_close_is_closed(stubs, kind):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("FAILED: G — x\n")
    done = done_("eeee5555", str(report), kind, "w2:tGX", env=env)
    assert done.returncode == 0, done.stderr
    assert recorded(calls) == [
        "claude stop eeee5555",
        "claude rm eeee5555",
        "herdr tab close w2:tGX",
    ]


@pytest.mark.parametrize(
    "kind,last",
    [
        ("build", "(run in progress — next step under ## CONTINUE)"),
        ("build", "CHECK DONE · job: x"),
        ("check", "BUILT · job: x"),
        ("deploy", "  FAILED: indented"),
    ],
)
def test_a_last_line_that_is_no_stop_line_of_its_kind_is_refused(stubs, kind, last):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("BUILT · job: x\n\n" + last + "\n")
    done = done_("aaaa1111", str(report), kind, env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: still running"), done.stderr
    assert recorded(calls) == []


WRITTEN = "WRITTEN · job: x-write · rows: 3 · backup: local/1a2b3c4d"


def test_d1_a_written_prodwrite_report_stops_removes_and_closes_the_tab_in_order(stubs):
    """Card 392 W5. RED on BASE: REFUSED: unknown kind: prodwrite."""
    report, calls, stop_exit, agents, env = stubs
    report.write_text(f"# x\n\n{WRITTEN}\n\n")
    done = done_("aaaa1111", str(report), "prodwrite", "w2:tGX", env=env)
    assert done.returncode == 0, done.stderr
    assert recorded(calls) == ["claude stop aaaa1111", "claude rm aaaa1111", "herdr tab close w2:tGX"]


def test_d2_a_failed_prodwrite_is_refused_and_kept(stubs):
    """Card 392 W5, both sides: refused (unknown kind) on BASE; refused and kept after."""
    report, calls, stop_exit, agents, env = stubs
    report.write_text("FAILED: verify — before 3 after 4 expected 3 · backup: local/1a2b3c4d\n")
    done = done_("aaaa1111", str(report), "prodwrite", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert recorded(calls) == []


def test_d2_a_build_on_a_written_line_is_still_running(stubs):
    """Two-sided: green on BASE and after."""
    report, calls, stop_exit, agents, env = stubs
    report.write_text(f"{WRITTEN}\n")
    done = done_("aaaa1111", str(report), "build", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: still running"), done.stderr
    assert recorded(calls) == []


def test_a_missing_report_is_refused(stubs):
    report, calls, stop_exit, agents, env = stubs
    done = done_("aaaa1111", str(report), "build", env=env)
    assert done.returncode == 1
    assert recorded(calls) == []


@pytest.mark.parametrize("sid", ["bbbb2222", "cccc3333", "dddd4444"])
def test_a_brain_or_the_desk_is_refused(stubs, sid):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("BUILT · job: x\n")
    done = done_(sid, str(report), "build", "w2:tGX", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert recorded(calls) == []


@pytest.mark.parametrize("answer", ["[]", "not json"])
def test_a_session_not_in_the_list_or_an_unreadable_list_is_refused(stubs, answer):
    report, calls, stop_exit, agents, env = stubs
    agents.write_text(answer)
    report.write_text("BUILT · job: x\n")
    done = done_("aaaa1111", str(report), "build", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert recorded(calls) == []


def test_a_failing_stop_ends_the_script_with_no_rm(stubs):
    report, calls, stop_exit, agents, env = stubs
    stop_exit.write_text("1")
    report.write_text("BUILT · job: x\n")
    done = done_("aaaa1111", str(report), "build", "w2:tGX", env=env)
    assert done.returncode == 1
    assert "claude stop aaaa1111" in done.stderr
    assert recorded(calls) == ["claude stop aaaa1111"]


# ---- card 386 L9: kind shadow, the shadow gate seat's and role trial's stop words ---------------


@pytest.mark.parametrize("last", [
    "SHADOW BUILT · job: x-job · tip: 1a2b3c4d | on 0f0e0d0c | wall: 1",
    "SHADOW ROLE · drafter · builder: grok-4.7 · wall: 1",
])
def test_386_f1_a_shadow_stop_line_stops_removes_and_closes_the_tab_in_order(stubs, last):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("# x\n\n" + last + "\n\n")
    done = done_("aaaa1111", str(report), "shadow", "w2:tGX", env=env)
    assert done.returncode == 0, done.stderr
    assert recorded(calls) == [
        "claude stop aaaa1111",
        "claude rm aaaa1111",
        "herdr tab close w2:tGX",
    ]


@pytest.mark.parametrize("kind,last", [
    ("build", "SHADOW BUILT · job: x-job · tip: 1a2b3c4d"),
    ("shadow", "BUILT · job: x-job · tip: 1a2b3c4d"),
    ("shadow", "CHECK DONE · job: x"),
])
def test_386_f2_a_stop_line_of_the_other_kind_is_refused(stubs, kind, last):
    report, calls, stop_exit, agents, env = stubs
    report.write_text(last + "\n")
    done = done_("aaaa1111", str(report), kind, env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: still running"), done.stderr
    assert recorded(calls) == []


def test_386_f3_a_failed_shadow_is_kept_for_continue(stubs):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("FAILED: x — y\n")
    done = done_("aaaa1111", str(report), "shadow", "w2:tGX", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: FAILED — the worker is kept for CONTINUE"), done.stderr
    assert recorded(calls) == []


def test_a_bad_kind_is_refused(stubs):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("BUILT · job: x\n")
    done = done_("aaaa1111", str(report), "ship", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert recorded(calls) == []


# ---- card 2026-10-15 580 C1: the tab by its title and the three-way proof -----------------------


def live(agents: Path) -> None:
    """The worker's row carries a pid, so desk-list.sh beside the script lists it."""
    rows = json.loads(agents.read_text())
    for row in rows:
        if row["id"] == "aaaa1111":
            row["pid"] = 4242
    agents.write_text(json.dumps(rows))


def panes(agents: Path, *rows: tuple[str, str, str]) -> Path:
    """The stub `herdr pane list` answer: (pane_id, tab_id, terminal_title_stripped) rows."""
    path = agents.parent / "panes.json"
    path.write_text(json.dumps({"id": "cli:pane:list", "result": {"panes": [
        {"pane_id": p, "tab_id": t, "terminal_title_stripped": title} for p, t, title in rows
    ]}}))
    return path


def test_c1_a_closed_worker_is_proved_gone_and_prints_closed_last(stubs):
    report, calls, stop_exit, agents, env = stubs
    live(agents)
    held = panes(agents, ("p1", "w9:t9", "x-job-build"), ("p2", "w9:t8", "other-seat"))
    report.write_text("# x\n\nBUILT · job: x-job · tip: 1a2b3c4d\n\n")
    done = done_("aaaa1111", str(report), "build", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == "CLOSED aaaa1111"
    assert recorded(calls) == ["claude stop aaaa1111", "claude rm aaaa1111", "herdr tab close w9:t9"]
    assert all(row["id"] != "aaaa1111" for row in json.loads(agents.read_text()))
    assert [p["tab_id"] for p in json.loads(held.read_text())["result"]["panes"]] == ["w9:t8"]


def test_c1_two_tabs_with_the_title_are_kept_before_any_stop(stubs):
    report, calls, stop_exit, agents, env = stubs
    panes(agents, ("p1", "w9:t9", "x-job-build"), ("p2", "w9:t7", "x-job-build"))
    report.write_text("BUILT · job: x-job · tip: 1a2b3c4d\n")
    done = done_("aaaa1111", str(report), "build", env=env)
    assert done.returncode == 1
    assert done.stdout.startswith("KEPT aaaa1111: 2 tabs titled x-job-build"), done.stdout
    assert recorded(calls) == []


def test_c1_a_tab_that_stays_is_kept(stubs, tmp_path):
    report, calls, stop_exit, agents, env = stubs
    panes(agents, ("p1", "w9:t9", "x-job-build"))
    (tmp_path / "keep-panes").write_text("")
    report.write_text("BUILT · job: x-job · tip: 1a2b3c4d\n")
    done = done_("aaaa1111", str(report), "build", env=env)
    assert done.returncode == 1
    assert done.stdout.splitlines()[-1] == "KEPT aaaa1111: tab still present", done.stdout


def test_c1_a_listed_row_that_stays_is_kept(stubs, tmp_path):
    report, calls, stop_exit, agents, env = stubs
    ops = tmp_path / "ops"
    ops.mkdir()
    (ops / "desk-done.sh").write_text(DONE.read_text())
    (ops / "desk-list.sh").write_text(
        "#!/bin/sh\nprintf '%s\\n' 'aaaa1111 · x-job-build · ~/cobalt-wt/x · idle · idle'\n"
    )
    report.write_text("BUILT · job: x-job · tip: 1a2b3c4d\n")
    done = subprocess.run(
        ["sh", str(ops / "desk-done.sh"), "aaaa1111", str(report), "build"],
        env=env, capture_output=True, text=True, timeout=60,
    )
    assert done.returncode == 1
    assert done.stdout.splitlines()[-1] == "KEPT aaaa1111: LIST row still present", done.stdout


def test_c1_replaced_form_closes_without_a_report(stubs):
    report, calls, stop_exit, agents, env = stubs
    panes(agents, ("p1", "w9:t9", "x-job-build"))
    done = done_("aaaa1111", "--replaced", env=env)
    assert done.returncode == 0, done.stderr
    assert recorded(calls) == ["claude stop aaaa1111", "claude rm aaaa1111", "herdr tab close w9:t9"]
    assert done.stdout.splitlines()[-1] == "CLOSED aaaa1111"
    for sid in ("bbbb2222", "dddd4444"):
        refused = done_(sid, "--replaced", env=env)
        assert refused.returncode == 1
        assert refused.stderr.startswith("REFUSED: "), refused.stderr
    assert recorded(calls) == ["claude stop aaaa1111", "claude rm aaaa1111", "herdr tab close w9:t9"]


def test_c1_control_desk_list_stays_read_only():
    text = (REPO / "ops" / "desk" / "desk-list.sh").read_text()
    assert "claude stop" not in text
    assert "claude rm" not in text
    assert "herdr" not in text
