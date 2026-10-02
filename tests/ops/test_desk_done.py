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


@pytest.fixture
def stubs(tmp_path):
    bin_ = tmp_path / "bin"
    bin_.mkdir()
    calls = tmp_path / "calls"
    agents = tmp_path / "agents.json"
    agents.write_text(json.dumps(AGENTS))
    stop_exit = tmp_path / "stop-exit"
    stop_exit.write_text("0")
    (bin_ / "claude").write_text(
        "#!/bin/sh\n"
        f'if [ "$1" = agents ]; then cat "{agents}"; exit 0; fi\n'
        f'printf "claude %s\\n" "$*" >> "{calls}"\n'
        f'if [ "$1" = stop ]; then exit "$(cat "{stop_exit}")"; fi\n'
        "exit 0\n"
    )
    (bin_ / "herdr").write_text(f'#!/bin/sh\nprintf "herdr %s\\n" "$*" >> "{calls}"\nexit 0\n')
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


def test_a_bad_kind_is_refused(stubs):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("BUILT · job: x\n")
    done = done_("aaaa1111", str(report), "ship", env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert recorded(calls) == []
