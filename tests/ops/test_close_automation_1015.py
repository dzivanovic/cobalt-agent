"""Card 2026-10-15 580 close-automation: C2 desk-watch.sh closes a clean-finished worker through
desk-done.sh and the launcher closes a replaced session first; C3 stop-guard.py blocks the desk's
stop while a finished worker is unkept and still listed; C4 desk-watch.sh runs install-ops after a
DEPLOYED whose set touches ops/desk.

Every run stages its scripts under tmp_path with the worktree root re-pointed at tmp_path/wt (the
shape of tests/ops/test_desk_watch.py and tests/ops/test_stop_guard.py); `claude`, `desk-list.sh`
and `desk-done.sh` are stubs. Every git repo is a tmp repo built here. Nothing outside tmp_path is
read, written or closed.
"""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

REPO = Path(__file__).resolve().parents[2]
OPS = REPO / "ops" / "desk"
GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
STOP = "BUILT · job: x-job · tip: 1a2b3c4d | on 0f0e0d0c | rows: 1 of 1"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def repo_at(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    git(path, "init", "-q", "-b", "main")
    return path


def commit(path: Path, msg: str) -> None:
    git(path, "add", "-A")
    git(path, "commit", "-q", "-m", msg)


# ---- C2 / C4: the staged watch -----------------------------------------------------------------


class Watch:
    """desk-watch.sh and wait-stop-line.sh staged in tmp_path/ops, a LIST stub answering from
    tmp_path/list, a worktree repo tmp_path/wt/x-job holding the build report, a main repo
    tmp_path/main holding the check report, and the card."""

    def __init__(self, tmp_path: Path, done: bool = True):
        self.tmp = tmp_path
        self.ops = tmp_path / "ops"
        self.ops.mkdir()
        for name in ("desk-watch.sh", "wait-stop-line.sh"):
            text = (OPS / name).read_text().replace("/Users/cobalt/cobalt-wt", str(tmp_path / "wt"))
            (self.ops / name).write_text(text)
        (self.ops / "desk-context.sh").write_text("exit 0\n")
        self.list = tmp_path / "list"
        self.list.write_text("")
        (self.ops / "desk-list.sh").write_text(f'#!/bin/sh\ncat "{self.list}"\n')
        self.log = tmp_path / "done-log"
        if done:
            (self.ops / "desk-done.sh").write_text(
                f'printf "%s\\n" "$*" >> "{self.log}"\necho "+ claude stop $1"\necho "CLOSED $1"\n'
            )
        self.finished = tmp_path / "wt" / ".job-state" / "FINISHED"
        self.wt = repo_at(tmp_path / "wt" / "x-job")
        self.build = self.wt / "docs" / "x-job-build.md"
        self.build.parent.mkdir()
        self.build.write_text(f"# x-job build\n\nbody\n\n{STOP}\n")
        commit(self.wt, "report")
        self.main = repo_at(tmp_path / "main")
        self.check = self.main / "x-job-check.md"
        self.check.write_text("# x-job check\n\nbody\n\nCHECK DONE · job: x-job · pass: 1\n")
        commit(self.main, "check report")
        self.card = tmp_path / "01-x-job-card.md"
        self.card.write_text(
            "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
            f"BASE: 1a2b3c4d\nTIP: 5e6f7a8b\nREPORT: {self.build}\nCHECK REPORT: {self.check}\n"
            "RULINGS: 2026-01-02 R1\n\n## ROWS\n"
        )
        self.env = dict(os.environ, DESK_WATCH_POLL="1", **GIT_ENV)

    def rows(self, *rows: str) -> None:
        self.list.write_text("".join(r + "\n" for r in rows))

    def run(self, kind: str = "build", card: Path | None = None, **extra: str):
        return subprocess.run(
            ["sh", str(self.ops / "desk-watch.sh"), kind, str(card or self.card), "30"],
            env=dict(self.env, **extra), capture_output=True, text=True, timeout=120,
        )

    def logged(self) -> list[str]:
        return self.log.read_text().splitlines() if self.log.exists() else []


IDLE_BUILD = "aaaa0001 · x-job-build · ~/cobalt-wt/x-job · idle · idle"
IDLE_CHECK = "aaaa0001 · x-job-check · ~/cobalt-wt/x-job · idle · idle"


def test_c2_a_clean_stop_line_closes_the_worker_and_prints_closed_after_it(tmp_path):
    w = Watch(tmp_path)
    w.rows(IDLE_BUILD)
    done = w.run(DESK_WATCH_CLOSE_WAIT="2")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [STOP, "CLOSED aaaa0001"]
    assert w.logged() == [f"aaaa0001 {w.build} build"]
    lines = w.finished.read_text().splitlines()
    assert len(lines) == 1 and lines[0].endswith(" aaaa0001 x-job-build BUILT"), lines


def test_c2_a_failed_stop_line_is_kept_and_runs_nothing(tmp_path):
    w = Watch(tmp_path)
    w.rows(IDLE_BUILD)
    w.build.write_text("# x\n\nFAILED: x\n")
    commit(w.wt, "failed")
    done = w.run(DESK_WATCH_CLOSE_WAIT="1")
    assert done.returncode == 0, done.stderr
    assert "KEPT x-job-build: FAILED" in done.stdout, done.stdout
    assert w.logged() == []
    assert not w.finished.exists()


@pytest.mark.parametrize("case", ["tree", "report", "busy"])
def test_c2_a_dirty_tree_an_uncommitted_report_or_a_busy_session_is_kept(tmp_path, case):
    w = Watch(tmp_path)
    kind, row = "build", IDLE_BUILD
    if case == "tree":
        (w.wt / "stray.txt").write_text("x\n")
        want = "KEPT aaaa0001: tree not clean"
    elif case == "report":
        kind, row = "check", IDLE_CHECK
        w.check.write_text(w.check.read_text().replace("body", "edited body"))
        want = "KEPT aaaa0001: report not committed"
    else:
        row = row.replace("idle · idle", "busy · working")
        want = "KEPT aaaa0001: session busy"
    w.rows(row)
    done = w.run(kind, DESK_WATCH_CLOSE_WAIT="1")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == want, done.stdout
    assert w.logged() == []
    assert len(w.finished.read_text().splitlines()) == 1


@pytest.mark.parametrize("rows,want", [
    ((), "KEPT x-job-build: no listed session"),
    ((IDLE_BUILD, IDLE_BUILD.replace("aaaa0001", "aaaa0009")), "KEPT x-job-build: 2 listed sessions"),
])
def test_c2_no_listed_row_or_two_are_kept(tmp_path, rows, want):
    w = Watch(tmp_path)
    w.rows(*rows)
    done = w.run(DESK_WATCH_CLOSE_WAIT="0")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [STOP, want]
    assert w.logged() == []


def test_c2_deploy_prodwrite_and_close_kinds(tmp_path):
    w = Watch(tmp_path)
    w.rows("aaaa0005 · deploy-hub-x-job · ~/cobalt · idle · idle",
           "aaaa0006 · prodwrite-x-job · ~/cobalt · idle · idle")
    deployed = "DEPLOYED deploy-t notahead | set: none"
    w.build.write_text(f"# d\n\n{deployed}\n")
    done = w.run("deploy", DESK_WATCH_CLOSE_WAIT="0")
    assert done.stdout.splitlines()[:2] == [deployed, "CLOSED aaaa0005"], done.stdout
    assert w.logged() == [f"aaaa0005 {w.build} deploy"]
    w.build.write_text("# d\n\nFAILED: 4.3 — x\n")
    done = w.run("deploy", DESK_WATCH_CLOSE_WAIT="0")
    assert done.stdout.splitlines() == [
        "FAILED: 4.3 — x", "KEPT deploy-hub-x-job: FAILED deploy, closed through desk-done.sh by the desk"]
    written = "WRITTEN · job: x-job · rows: 3"
    w.build.write_text(f"# p\n\n{written}\n")
    done = w.run("prodwrite", DESK_WATCH_CLOSE_WAIT="0")
    assert done.stdout.splitlines() == [written, "KEPT prodwrite-x-job: closed through desk-done.sh by the desk"]
    assert w.logged() == [f"aaaa0005 {w.build} deploy"]
    # check 2026-10-15 A2: the DEPLOYED deploy and the WRITTEN prodwrite are each recorded
    assert len(w.finished.read_text().splitlines()) == 2


def test_c2_close_wait_stops_at_the_parameter_not_the_poll(tmp_path):
    w = Watch(tmp_path)
    (w.wt / "stray.txt").write_text("x\n")
    w.rows(IDLE_BUILD)
    try:
        subprocess.run(
            ["sh", str(w.ops / "desk-watch.sh"), "build", str(w.card), "30"],
            env=dict(w.env, DESK_WATCH_POLL="30", DESK_WATCH_CLOSE_WAIT="1"),
            capture_output=True, text=True, timeout=5,
        )
    except subprocess.TimeoutExpired as exc:
        raise AssertionError("DESK_WATCH_CLOSE_WAIT=1 slept a full DESK_WATCH_POLL") from exc


def test_c2_a_written_prodwrite_is_recorded_for_the_guard(tmp_path):
    w = Watch(tmp_path)
    w.rows("aaaa0006 · prodwrite-x-job · ~/cobalt · idle · idle")
    w.build.write_text("WRITTEN · job: x-job · rows: 3\n")
    done = w.run("prodwrite", DESK_WATCH_CLOSE_WAIT="0")
    assert done.returncode == 0, done.stderr
    text = w.finished.read_text() if w.finished.exists() else ""
    assert "aaaa0006 prodwrite-x-job WRITTEN" in text, text


def test_c2_two_listed_rows_record_an_id_the_guard_can_name(tmp_path):
    w = Watch(tmp_path)
    w.rows(IDLE_BUILD, IDLE_BUILD.replace("aaaa0001", "aaaa0009"))
    done = w.run(DESK_WATCH_CLOSE_WAIT="0")
    assert done.returncode == 0, done.stderr
    line = w.finished.read_text().splitlines()[0]
    assert line.split()[1] in {"aaaa0001", "aaaa0009"}, line


def test_c2_control_the_stop_line_alone_when_no_desk_done(tmp_path):
    w = Watch(tmp_path, done=False)
    w.rows(IDLE_BUILD)
    done = w.run()
    assert done.returncode == 0, done.stderr
    assert done.stdout == STOP + "\n"


def test_c2_control_an_idle_exit_closes_nothing(tmp_path):
    w = Watch(tmp_path)
    w.rows(IDLE_BUILD)
    w.build.write_text("# x\n\n(run in progress — next step under ## CONTINUE)\n")
    done = w.run(DESK_WATCH_CLOSE_WAIT="1")
    assert done.returncode == 3, done.stderr
    assert done.stdout.startswith("IDLE: x-job-build"), done.stdout
    assert w.logged() == []


# ---- C2: the launcher closes a replaced session first -------------------------------------------


def prechecks_desk():
    """The Desk world of tests/ops/test_desk_launch_prechecks.py, loaded by path."""
    spec = importlib.util.spec_from_file_location(
        "prechecks_world", Path(__file__).with_name("test_desk_launch_prechecks.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.Desk


class Launcher:
    """A staged desk-launch.sh beside a passing guard and a stub desk-done.sh; a stub `claude`
    whose `agents --json` answers from a file and whose other calls are logged."""

    def __init__(self, tmp_path: Path):
        self.desk = prechecks_desk()(tmp_path)
        self.ops = tmp_path / "launch-ops"
        self.ops.mkdir()
        (self.ops / "desk-launch.sh").write_text((OPS / "desk-launch.sh").read_text())
        (self.ops / "desk-context.sh").write_text("exit 0\n")
        self.calls = tmp_path / "calls"
        self.answer = tmp_path / "done-answer"
        self.answer.write_text("CLOSED aaaa0002\n")
        self.done_exit = tmp_path / "done-exit"
        self.done_exit.write_text("0")
        (self.ops / "desk-done.sh").write_text(
            f'printf "desk-done %s\\n" "$*" >> "{self.calls}"\necho "+ claude stop $1"\n'
            f'cat "{self.answer}"\nexit "$(cat "{self.done_exit}")"\n'
        )
        self.agents = tmp_path / "agents.json"
        self.agents.write_text("[]")
        bin_ = tmp_path / "bin2"
        bin_.mkdir()
        (bin_ / "claude").write_text(
            "#!/bin/sh\n"
            f'if [ "$1" = agents ]; then cat "{self.agents}"; exit 0; fi\n'
            f'printf "claude %s\\n" "$1" >> "{self.calls}"\nexit 0\n'
        )
        (bin_ / "claude").chmod(0o755)
        self.env = dict(self.desk.env, PATH=f"{bin_}:{self.desk.env['PATH']}")

    def row(self, status: str = "idle", state: str = "idle") -> None:
        self.agents.write_text(json.dumps([
            {"id": "aaaa0002", "name": "x-job-build", "pid": 4242, "status": status, "state": state},
            {"id": "aaaa0003", "name": "x-job-build", "status": "idle", "state": "idle"},
            {"id": "aaaa0004", "name": "y-job-build", "pid": 4243, "status": "busy", "state": "working"},
        ]))

    def launch(self):
        return subprocess.run(
            ["sh", str(self.ops / "desk-launch.sh"), "build", str(self.desk.card)],
            env=self.env, capture_output=True, text=True, timeout=120,
        )

    def called(self) -> list[str]:
        return self.calls.read_text().splitlines() if self.calls.exists() else []


def test_c2_the_launcher_closes_a_replaced_session_first(tmp_path):
    lx = Launcher(tmp_path)
    lx.row()
    done = lx.launch()
    assert done.returncode == 0, done.stderr
    assert lx.called() == ["desk-done aaaa0002 --replaced", "claude --bg"]
    assert "RUN: CLOSED aaaa0002" in done.stderr

    for status, state, answer, code in (
        ("busy", "working", "CLOSED aaaa0002\n", "0"),
        ("idle", "idle", "KEPT aaaa0002: tab still present\n", "1"),
    ):
        lx.calls.unlink(missing_ok=True)
        lx.row(status, state)
        lx.answer.write_text(answer)
        lx.done_exit.write_text(code)
        refused = lx.launch()
        assert refused.returncode == 1
        assert "REFUSED: a session named x-job-build is still" in refused.stderr, refused.stderr
        assert "claude --bg" not in lx.called()

    lx.calls.unlink(missing_ok=True)
    lx.agents.write_text("")
    refused = lx.launch()
    assert refused.returncode == 1
    assert "REFUSED: claude agents --json could not be read" in refused.stderr, refused.stderr
    assert lx.called() == []


# ---- C3: the desk's stop and a finished worker ---------------------------------------------------

DESK_LINE = "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly."
FINISHED_LINE = "2026-01-02T10:00:00-05:00 b43daef9-0000 x-job-build BUILT"
IDLE_ROW = "b43daef9-0000 · x-job-build · ~/cobalt-wt/x · idle · idle"


class Desk:
    """The Desk helper of tests/ops/test_stop_guard.py, copied by content: the staged hook, the
    staged repo as the desk's cwd, a desk transcript and today's desk report."""

    def __init__(self, tmp_path: Path):
        text = (OPS / "stop-guard.py").read_text()
        text = text.replace("/Users/cobalt/cobalt-wt", str(tmp_path / "wt"))
        text = text.replace('"/Users/cobalt/cobalt"', '"%s"' % (tmp_path / "repo"))
        self.hook = tmp_path / "ops" / "stop-guard.py"
        self.hook.parent.mkdir()
        self.hook.write_text(text)
        self.repo = tmp_path / "repo"
        reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        reports.mkdir(parents=True)
        day = datetime.now(ZoneInfo("America/New_York")).date()
        self.report = reports / f"cto-{day}.md"
        self.transcript = tmp_path / "desk.jsonl"
        self.desk_stop = tmp_path / "wt" / ".job-state" / "DESK-STOP"
        self.finished = tmp_path / "wt" / ".job-state" / "FINISHED"
        launch = {"type": "user", "message": {"role": "user", "content": DESK_LINE},
                  "sessionId": "s-1", "sessionKind": "bg"}
        self.transcript.write_text(json.dumps(launch) + "\n")

    def owed(self, *block: str) -> None:
        self.report.write_text(
            "# CTO desk\n\n## §5 CURRENT\n" + "".join(x + "\n" for x in block) + "\n"
            "| session | id | prompt · tab | watch | waits for → then |\n|---|---|---|---|---|\n"
            "| CTO desk | `0000aaaa` | x | none | x |\n\n## §5 HISTORY\n| x |\n"
        )

    def lister(self, *rows: str) -> None:
        body = "".join("printf '%%s\\n' '%s'\n" % r for r in rows)
        (self.hook.parent / "desk-list.sh").write_text(f"#!/bin/sh\n{body}exit 0\n")

    def finish(self, *lines: str) -> None:
        self.finished.parent.mkdir(parents=True, exist_ok=True)
        self.finished.write_text("".join(x + "\n" for x in lines))

    def run(self, active: bool = False):
        event = {
            "session_id": "s-1", "transcript_path": str(self.transcript), "cwd": str(self.repo),
            "hook_event_name": "Stop", "stop_hook_active": active,
        }
        return subprocess.run(
            ["python3", str(self.hook)], input=json.dumps(event),
            capture_output=True, text=True, timeout=60, env=dict(os.environ, LC_ALL="C"),
        )


def test_c3_a_finished_listed_unkept_worker_blocks_with_close_id(tmp_path):
    d = Desk(tmp_path)
    d.finish(FINISHED_LINE)
    d.lister(IDLE_ROW)
    d.owed("owed: none")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: close b43daef9-0000\n")


def test_c3_three_blocks_then_gives_up_and_records(tmp_path):
    d = Desk(tmp_path)
    d.finish(FINISHED_LINE)
    d.lister(IDLE_ROW)
    d.owed("owed: none")
    codes = [d.run(active=a).returncode for a in (False, True, True, True)]
    assert codes == [2, 2, 2, 0]
    lines = d.desk_stop.read_text().splitlines()
    assert len(lines) == 1 and lines[0].endswith("start it: close b43daef9-0000"), lines


def test_c3_an_unreadable_list_blocks_as_unreadable(tmp_path):
    d = Desk(tmp_path)
    d.finish(FINISHED_LINE)
    (d.hook.parent / "desk-list.sh").write_text("#!/bin/sh\nexit 1\n")
    d.owed("owed: none")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "session list unreadable — fix it\n")


def test_c3_control_a_kept_worker_lets_the_turn_end(tmp_path):
    d = Desk(tmp_path)
    d.finish(FINISHED_LINE)
    d.lister(IDLE_ROW)
    d.owed("OWED: keep x-job-build | live: b43daef9")
    r = d.run()
    assert (r.returncode, r.stderr) == (0, "")


def test_c3_control_a_closed_worker_lets_the_turn_end(tmp_path):
    d = Desk(tmp_path)
    d.finish(FINISHED_LINE)
    d.lister("c0ffee00-0000 · y-job-build · ~/cobalt-wt/y · busy · working")
    d.owed("owed: none")
    r = d.run()
    assert (r.returncode, r.stderr) == (0, "")


def test_c3_control_no_finished_file_changes_nothing(tmp_path):
    d = Desk(tmp_path)
    d.lister(IDLE_ROW)
    d.owed("owed: none")
    r = d.run()
    assert (r.returncode, r.stderr) == (0, "")


# ---- C4: install-ops after a DEPLOYED whose set touches ops/desk --------------------------------


class Deploy:
    """The world of tests/ops/test_install_ops.py: a tmp repo (COBALT_REPO_ROOT), a tmp link folder
    (COBALT_OPS_LINK_DIR), the staged watch with a real copy of desk-launch.sh beside it."""

    def __init__(self, tmp_path: Path, second: str):
        self.w = Watch(tmp_path, done=False)
        (self.w.ops / "desk-launch.sh").write_text((OPS / "desk-launch.sh").read_text())
        self.repo = repo_at(tmp_path / "repo")
        (self.repo / "docs").mkdir()
        (self.repo / "docs" / "a.md").write_text("one\n")
        commit(self.repo, "first")
        git(self.repo, "tag", "pre-x-job")
        path = self.repo / second
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("# constructed\n")
        commit(self.repo, "second")
        self.head = git(self.repo, "rev-parse", "--short=8", "HEAD")
        self.links = tmp_path / "links"
        self.links.mkdir()
        self.report = tmp_path / "deploy-x.md"
        self.card = tmp_path / "02-x-deploy-card.md"
        self.card.write_text(
            f"JOB: x-job\nLADDER: OFF-LADDER\nREPORT: {self.report}\nRULINGS: none\n\n## SHIPS\n"
        )
        self.w.env.update(COBALT_REPO_ROOT=str(self.repo), COBALT_OPS_LINK_DIR=str(self.links))
        self.w.env.pop("CLAUDE_JOB_DIR", None)

    def deployed(self) -> str:
        return (f"DEPLOYED deploy-t {self.head} | set: none | migrations: none | gate: offline 1/0 · "
                "with-DB 1/0 · live-note 1/0 | RESTARTS: none | smoke: GREEN | decisions: 0 · "
                "for Dejan: 0 · tokens: 1")

    def run(self, last: str):
        self.report.write_text(f"# deploy\n\nbody\n\n{last}\n")
        return self.w.run("deploy", self.card)


def test_c4_a_set_that_adds_an_ops_desk_script_leaves_no_script_unlinked(tmp_path):
    d = Deploy(tmp_path, "ops/desk/newone.sh")
    done = d.run(d.deployed())
    assert done.returncode == 0, done.stderr
    assert (d.links / "newone.sh").is_symlink()
    assert done.stdout.splitlines()[-1].startswith("install-ops: 1 linked"), done.stdout


def test_c4_control_a_set_with_no_ops_desk_path_runs_no_install_ops(tmp_path):
    d = Deploy(tmp_path, "docs/b.md")
    done = d.run(d.deployed())
    assert done.returncode == 0, done.stderr
    assert list(d.links.iterdir()) == []
    assert done.stdout == d.deployed() + "\n"


def test_c4_control_a_failed_deploy_runs_no_install_ops(tmp_path):
    d = Deploy(tmp_path, "ops/desk/newone.sh")
    done = d.run("FAILED: 4.3 — x")
    assert done.returncode == 0, done.stderr
    assert list(d.links.iterdir()) == []
