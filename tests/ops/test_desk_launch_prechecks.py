"""desk-launch.sh's pre-checks (card prompts/2026-10-02/21-launcher-checks-card.md, R47).

L1 the ruling rows (build, check, deploy, devfix), L2 the build is built (check), L3 every
check committed and clean (deploy), L4 the WATCH line and the header. Every refusal is
`REFUSED: <what> — <the fix>` on stderr, exit 1, `claude` never called, no worktree added.

The `desk` shape of tests/ops/test_devdb_lock.py: a tmp repo standing in for
/Users/cobalt/cobalt (COBALT_REPO_ROOT) with the fixed files, a committed
`cto-2026-01-02.md` holding the approved row R1, a job branch whose code commit is the tip
and whose build-report commit is a docs-only head, a job card, a deploy card, a devfix card;
a tmp directory standing in for /Users/cobalt/cobalt-wt (COBALT_WT_ROOT); and a stub `claude`
on PATH that records its cwd. Nothing here reads a real card, report, `.env` or database.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

# constructed one-line fixed files for the kinds whose tree file is not installed in a tmp repo
DEVFIX_LINE = (
    "claude --bg \"Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEVFIX-HUB.md' and "
    "follow it exactly. CARD: '<card>' TABLE: <table> PROOF: <proof test>\" "
    "--model claude-opus-5-5 --permission-mode dontAsk --remote-control <job>-devfix "
    "--name <job>-devfix --allowedTools \"Read\" "
    "--disallowedTools \"AskUserQuestion\" \"EnterWorktree\" --add-dir /Users/cobalt/cobalt-wt"
)
CLOSE_LINE = (
    "claude --bg \"Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and "
    "follow it exactly. DATE: <date>\" --permission-mode dontAsk --remote-control close-<mmdd> "
    "--name close-<mmdd> --disallowedTools \"AskUserQuestion\" \"EnterWorktree\""
)

APPROVED_R1 = "| R1 | 07:00 ET | HIS RULING (constructed): the job may run. | HIS RULING · APPROVED |"
RULINGS_HEAD = "# cto 2026-01-02 (constructed)\n\n| # | time | row | status |\n|---|---|---|---|\n"
OTHER_TIP = "0000beef"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def short(cwd: Path) -> str:
    return git(cwd, "rev-parse", "--short=8", "HEAD")


def check_line(tip: str, *, ready: str = "YES", held_unfixed: int = 0) -> str:
    return (f"CHECK DONE · job: x-job · pass: 1 · tip: {tip} · held: 0 · fixed: 0 · "
            f"held unfixed: {held_unfixed} · open: 0 · ready: {ready} · decisions: 0 · for Dejan: 0")


class Desk:
    def __init__(self, tmp_path: Path):
        self.wt = tmp_path / "wt"
        self.repo = tmp_path / "repo"
        self.wt.mkdir()
        self.repo.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        for hub in ("BUILD-HUB.md", "CHECK-HUB.md", "DEPLOY-HUB.md"):
            shutil.copy(HUBS / hub, self.prompts / hub)
        (self.prompts / "DEVFIX-HUB.md").write_text("# DEVFIX-HUB (constructed, installed)\n\n" + DEVFIX_LINE + "\n")
        (self.prompts / "CLOSE-HUB.md").write_text("# CLOSE-HUB (constructed, installed)\n\n" + CLOSE_LINE + "\n")
        self.rulings = self.reports / "cto-2026-01-02.md"
        self.rulings.write_text(RULINGS_HEAD + APPROVED_R1 + "\n")
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")
        self.base = short(self.repo)

        # the job's branch: a code commit (the code tip), then its build report (a docs-only head)
        self.job_wt = self.wt / "x-job"
        git(self.repo, "worktree", "add", "-q", "-b", "ops/x-job", str(self.job_wt), self.base)
        (self.job_wt / "src").mkdir()
        (self.job_wt / "src" / "x.py").write_text("X = 1\n")
        self.commit_job("code")
        self.tip = short(self.job_wt)
        self.build_report = self.job_wt / "docs" / "40 - DevDocs" / "reports" / "x-job-build.md"
        self.write_build_report(self.built_line())
        self.head = short(self.job_wt)

        self.check_report = self.reports / "x-job-check.md"
        day = self.prompts / "2026-01-02"
        self.card = day / "01-x-job-card.md"
        self.deploy = day / "02-x-deploy-card.md"
        self.devfix = day / "03-x-fix-card.md"
        self.write_card()
        self.write_deploy()
        self.write_devfix()
        self.commit("cards")

        stub = tmp_path / "bin"
        stub.mkdir()
        self.calls = tmp_path / "claude-calls"
        (stub / "claude").write_text(
            '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
            f'printf "%s\\n" "$PWD" >> "{self.calls}"\nexit "${{CLAUDE_STUB_EXIT:-0}}"\n'
        )
        (stub / "claude").chmod(0o755)
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{stub}:{os.environ['PATH']}", **GIT_ENV,
        )

    # ---- writers ----------------------------------------------------------------------------

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def commit_job(self, msg: str) -> None:
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", msg)

    def built_line(self, tip: str | None = None, job: str = "x-job") -> str:
        return (f"BUILT · job: {job} · tip: {tip or self.tip} | on {self.base} | migration: none | "
                "rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0")

    def write_build_report(self, last: str) -> None:
        self.build_report.parent.mkdir(parents=True, exist_ok=True)
        self.build_report.write_text(f"# x-job build\n\n## RECORDS\n- constructed\n\n{last}\n\n")
        self.commit_job("report")

    def write_rulings(self, *rows: str, commit: bool = True) -> None:
        self.rulings.write_text(RULINGS_HEAD + "".join(r + "\n" for r in rows))
        if commit:
            self.commit("rulings")

    def write_card(self, rulings: str = "2026-01-02 R1", extra: str = "") -> None:
        self.card.write_text(
            "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
            f"BASE: {self.base}\nTIP: {self.tip}\nREPORT: {self.build_report}\n"
            f"CHECK REPORT: {self.check_report}\n{extra}HOUSE B: as needed\n"
            f"TREE STATE: unchanged\nRULINGS: {rulings}\n\n## ROWS\n| row | what |\n"
        )

    def write_deploy(self, rulings: str = "none", code_tip: str | None = None,
                     head: str | None = None, carry: str = "`held unfixed: 0` and `ready: YES`") -> None:
        code_tip = code_tip or self.tip
        head = head or self.head
        self.deploy.write_text(
            "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
            f"BASE: main\nTIP: {head}\nREPORT: {self.reports / 'deploy-x.md'}\nRULINGS: {rulings}\n"
            "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n\n"
            "| # | branch | code tip | branch head | check report | its stop line must carry |\n"
            "|---|---|---|---|---|---|\n"
            f"| 1 | `ops/x-job` | `{code_tip}` | `{head}` | `{self.check_report}` | {carry} |\n\n"
            "## MARKERS\n## SMOKE READS\n"
        )

    def write_devfix(self, rulings: str = "2026-01-02 R1") -> None:
        self.devfix.write_text(
            "JOB: x-fix\nLADDER: OFF-LADDER\nBRANCH: ops/x-fix\nWORKTREE: x-fix\n"
            f"BASE: {self.base}\nREPORT: {self.reports / 'devfix-x-fix.md'}\nRULINGS: {rulings}\n"
            "TABLE: user.x_table\nPROOF TEST: tests/cobalt/test_x_proof.py\n\n## RECORDS\n- constructed\n"
        )

    def ship(self, last: str | None = None, commit: bool = True) -> None:
        """The check report of the deploy card's one SHIPS row, in the main tree."""
        self.check_report.write_text(f"# x-job check\n\n{last or check_line(self.tip)}\n\n")
        if commit:
            self.commit("check report")

    # ---- runs -------------------------------------------------------------------------------

    def launch(self, *args: str, dry: bool = False, **extra: str) -> subprocess.CompletedProcess:
        env = dict(self.env, **extra)
        if dry:
            env["DESK_LAUNCH_DRY"] = "1"
        return subprocess.run(
            ["sh", str(LAUNCH), *args], env=env, capture_output=True, text=True, timeout=120
        )

    def called(self) -> list[str]:
        return self.calls.read_text().splitlines() if self.calls.exists() else []

    def gate_left(self) -> bool:
        ref = subprocess.run(
            ["git", "-C", str(self.repo), "show-ref", "--verify", "--quiet", "refs/heads/deploy/x-deploy"],
            env=dict(os.environ, **GIT_ENV), capture_output=True,
        )
        return (self.wt / "x-gate").exists() or ref.returncode == 0


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def watch(kind: str, target: Path) -> str:
    return f'WATCH: sh {LAUNCH.parent}/desk-watch.sh {kind} "{target}"'


def refused(desk: Desk, done: subprocess.CompletedProcess, text: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert "WATCH:" not in done.stdout + done.stderr
    assert desk.called() == []


# ---- L1: the ruling rows ---------------------------------------------------------------------


def test_l1_a_build_on_an_approved_committed_row_launches(desk):
    """Negative control for every L1 refusal."""
    done = desk.launch("build", str(desk.card))
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.job_wt)]


def test_l1_a_cited_row_that_is_absent_refuses(desk):
    desk.write_card(rulings="2026-01-02 R1, 2026-01-02 R2")
    desk.commit("card")
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R2: no such row")


def test_l1_a_row_whose_rulings_file_is_absent_refuses(desk):
    desk.write_card(rulings="2026-01-03 R1")
    desk.commit("card")
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-03 R1: no such row")


def test_l1_a_row_that_reads_record_not_his_ruling_refuses(desk):
    desk.write_rulings("| R1 | 07:00 ET | RECORD (constructed): the job may run. | RECORD · APPROVED |")
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R1: not HIS RULING + APPROVED")


def test_l1_a_his_ruling_row_not_approved_refuses(desk):
    desk.write_rulings("| R1 | 07:00 ET | HIS RULING (constructed): the job may run. | HIS RULING · PENDING |")
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R1: not HIS RULING + APPROVED")


def test_l1_a_row_approved_only_in_the_working_tree_refuses(desk):
    desk.write_rulings("| R1 | 07:00 ET | HIS RULING (constructed): the job may run. | HIS RULING · PENDING |")
    desk.write_rulings(APPROVED_R1, commit=False)
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R1: not committed")


def test_l1_a_row_written_only_in_the_working_tree_refuses(desk):
    desk.write_card(rulings="2026-01-02 R1, 2026-01-02 R2")
    desk.commit("card")
    desk.write_rulings(APPROVED_R1, APPROVED_R1.replace("| R1 |", "| R2 |"), commit=False)
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R2: not committed")


def test_l1_a_row_on_two_lines_refuses(desk):
    desk.write_rulings(APPROVED_R1, APPROVED_R1)
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R1: not one row (2 lines")


@pytest.mark.parametrize("house", ["HOUSE A: none — overruled 2026-01-02 R9", "HOUSE B: as needed · overruled 2026-01-02 R9"])
def test_l1_a_house_line_whose_overruled_row_is_absent_refuses(desk, house):
    desk.write_card(extra=house + "\n" if house.startswith("HOUSE A") else "")
    if house.startswith("HOUSE B"):
        desk.card.write_text(desk.card.read_text().replace("HOUSE B: as needed\n", house + "\n"))
    desk.commit("card")
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R9: no such row")


def test_l1_a_house_line_whose_overruled_row_is_approved_launches(desk):
    desk.write_card(extra="HOUSE A: none — overruled 2026-01-02 R1\n")
    desk.commit("card")
    done = desk.launch("build", str(desk.card))
    assert done.returncode == 0, done.stderr


def test_l1_a_rulings_item_not_date_and_row_refuses(desk):
    desk.write_card(rulings="2026-01-02 R1, R2")
    desk.commit("card")
    refused(desk, desk.launch("build", str(desk.card)), "incomplete card: RULINGS item 'R2' is not '<date> R<n>'")


@pytest.mark.parametrize("kind", ["check", "deploy", "devfix"])
def test_l1_every_kind_refuses_an_absent_row(desk, kind):
    if kind == "check":
        desk.write_card(rulings="2026-01-02 R2")
        card = desk.card
    elif kind == "deploy":
        desk.ship()
        desk.write_deploy(rulings="2026-01-02 R2")
        card = desk.deploy
    else:
        desk.write_devfix(rulings="2026-01-02 R2")
        card = desk.devfix
    desk.commit("card")
    refused(desk, desk.launch(kind, str(card)), "ruling 2026-01-02 R2: no such row")
    assert not (desk.wt / "x-gate").exists()
    assert not (desk.wt / "x-fix").exists()


def test_l1_a_deploy_with_rulings_none_needs_no_rulings_file(desk):
    desk.ship()
    git(desk.repo, "rm", "-q", str(desk.rulings))
    desk.commit("no rulings file")
    done = desk.launch("deploy", str(desk.deploy))
    assert done.returncode == 0, done.stderr


# ---- L2: the build is built (kind check) -----------------------------------------------------


def test_l2_a_check_launches_on_the_built_line_for_its_job_and_tip(desk):
    """Negative control for every L2 refusal."""
    done = desk.launch("check", str(desk.card))
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.job_wt)]


@pytest.mark.parametrize("last", [
    "FAILED: W — x",
    "BUILT · job: x-job · tip: 0000beef | on x",
    "BUILT · job: x-other · tip: TIP | on x",
    "BUILT · job: x-job · tip: TIP9 | on x",
    "(run in progress — next step under ## CONTINUE)",
])
def test_l2_a_report_not_ending_in_its_built_line_refuses(desk, last):
    last = last.replace("TIP", desk.tip)
    desk.write_build_report(last)
    refused(desk, desk.launch("check", str(desk.card)), f"not built — {last}")


def test_l2_a_missing_build_report_refuses(desk):
    git(desk.job_wt, "rm", "-q", str(desk.build_report))
    desk.commit_job("no report")
    refused(desk, desk.launch("check", str(desk.card)), f"not built — no build report: {desk.build_report}")


def test_l2_a_check_resume_still_needs_the_built_line(desk):
    desk.write_build_report("FAILED: W — x")
    refused(desk, desk.launch("check", str(desk.card), "E3"), "not built — FAILED: W — x")


def test_l2_a_pass_2_launch_keeps_the_test_it_has(desk):
    desk.write_build_report("FAILED: W — x")
    desk.check_report.write_text("# check\n\nCHECK DONE · job: x-job · pass: 1 · house B: needed\n")
    done = desk.launch("check", str(desk.card), "PASS-2")
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.job_wt)]


# ---- L3: every check committed and clean (kind deploy) ---------------------------------------


def test_l3_a_deploy_on_a_committed_clean_check_launches(desk):
    """Negative control for every L3 refusal: the row's head is the build report's docs-only commit."""
    desk.ship()
    done = desk.launch("deploy", str(desk.deploy))
    assert done.returncode == 0, done.stderr
    assert (desk.wt / "x-gate").is_dir()
    assert desk.called() == [str(desk.repo)]


def break_uncommitted(desk):
    desk.ship(commit=False)
    return f"deploy ops/x-job: the check report is not committed or differs from its commit — commit {desk.check_report}"


def break_dirty(desk):
    desk.ship()
    desk.check_report.write_text(desk.check_report.read_text() + "edited\n")
    return f"deploy ops/x-job: the check report is not committed or differs from its commit — commit {desk.check_report}"


def break_absent(desk):
    return f"deploy ops/x-job: no check report — commit {desk.check_report}"


def break_ready_no(desk):
    desk.ship(check_line(desk.tip, ready="NO"))
    return f"deploy ops/x-job: its stop line lacks 'ready: YES' — the check is not clean: {check_line(desk.tip, ready='NO')}"


def break_held_unfixed(desk):
    desk.ship(check_line(desk.tip, held_unfixed=1))
    return f"deploy ops/x-job: its stop line lacks 'held unfixed: 0' — the check is not clean: {check_line(desk.tip, held_unfixed=1)}"


def break_other_tip(desk):
    desk.ship(check_line(OTHER_TIP))
    return f"deploy ops/x-job: the check's tip '{OTHER_TIP}' is neither the code tip {desk.tip} nor the branch head {desk.head} — the check is not clean"


def break_src_past_tip(desk):
    (desk.job_wt / "src" / "y.py").write_text("Y = 1\n")
    desk.commit_job("src past the code tip")
    new_head = short(desk.job_wt)
    desk.write_deploy(head=new_head)
    desk.ship()
    return f"deploy ops/x-job: the head adds more than docs past {desk.tip} — the head moved:"


def break_stale_head(desk):
    (desk.job_wt / "docs" / "late.md").write_text("late\n")
    desk.commit_job("docs past the row's head")
    desk.ship()
    return f"deploy ops/x-job: the branch head is {short(desk.job_wt)}, the row says {desk.head} — the head moved:"


def break_tip_not_ancestor(desk):
    main_tip = short(desk.repo)  # the cards commit: on main, not on the job's branch
    desk.write_deploy(code_tip=main_tip)
    desk.ship(check_line(main_tip))
    return f"deploy ops/x-job: the code tip {main_tip} is not an ancestor of {desk.head} — the head moved:"


BREAKS = {
    "uncommitted": break_uncommitted, "dirty": break_dirty, "absent": break_absent,
    "ready NO": break_ready_no, "held unfixed 1": break_held_unfixed, "other tip": break_other_tip,
    "src past the code tip": break_src_past_tip, "stale head": break_stale_head,
    "code tip not an ancestor": break_tip_not_ancestor,
}


@pytest.mark.parametrize("name", list(BREAKS))
def test_l3_one_broken_fact_refuses_and_leaves_no_gate(desk, name):
    text = BREAKS[name](desk)
    if git(desk.repo, "status", "--porcelain", "--", str(desk.deploy)):
        # the card alone is committed: the check report keeps the state the break gave it
        git(desk.repo, "add", str(desk.deploy))
        git(desk.repo, "commit", "-q", "-m", "deploy card", "--", str(desk.deploy))
    refused(desk, desk.launch("deploy", str(desk.deploy)), text)
    assert not desk.gate_left()


@pytest.mark.parametrize("line_tip", ["head", "code tip"])
def test_l3_a_docs_only_commit_past_the_code_tip_launches(desk, line_tip):
    """The 10-01 case (deploy-2026-10-01-1.md DECISIONS 1): the check's tip is the docs-only head."""
    (desk.job_wt / "docs" / "late.md").write_text("late\n")
    desk.commit_job("docs past the code tip")
    new_head = short(desk.job_wt)
    desk.write_deploy(head=new_head)
    desk.ship(check_line(new_head if line_tip == "head" else desk.tip))
    done = desk.launch("deploy", str(desk.deploy))
    assert done.returncode == 0, done.stderr
    assert (desk.wt / "x-gate").is_dir()


def test_l3_an_old_shape_check_line_with_its_own_literals_launches(desk):
    desk.write_deploy(carry="`VERDICT: PASS`")
    desk.ship(f"CHECK DONE · job: x-job · tip: {desk.tip} · VERDICT: PASS")
    done = desk.launch("deploy", str(desk.deploy))
    assert done.returncode == 0, done.stderr


def test_l3_a_step_d0_resume_is_not_re_checked(desk):
    desk.ship(check_line(desk.tip, ready="NO"))
    (desk.wt / "x-gate").mkdir()
    done = desk.launch("deploy", str(desk.deploy), "STEP-D0")
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.repo)]


# ---- L4: the WATCH line and the header ---------------------------------------------------------


def test_l4_a_build_launch_ends_its_stdout_with_the_watch_line(desk):
    done = desk.launch("build", str(desk.card))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == watch("build", desk.card)


def test_l4_check_deploy_and_devfix_print_their_watch_lines(desk):
    done = desk.launch("check", str(desk.card))
    assert done.stdout.splitlines()[-1] == watch("check", desk.card), done.stderr
    desk.ship()
    done = desk.launch("deploy", str(desk.deploy))
    assert done.stdout.splitlines()[-1] == watch("deploy", desk.deploy), done.stderr
    done = desk.launch("devfix", str(desk.devfix))
    assert done.stdout.splitlines()[-1] == watch("devfix", desk.devfix), done.stderr


def test_l4_a_close_prints_the_watch_line_on_its_report(desk):
    done = desk.launch("close", "2026-01-02")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == watch("close", desk.reports / "close-2026-01-02.md")


def test_l4_a_dry_run_prints_the_watch_line_after_the_dry_lines(desk):
    done = desk.launch("build", str(desk.card), dry=True)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[0] == f"cd {desk.job_wt}"
    assert "WATCH:" not in done.stdout
    assert done.stderr.splitlines()[-1] == watch("build", desk.card)


def test_l4_a_refused_or_failed_launch_prints_no_watch_line(desk):
    desk.write_card(rulings="2026-01-02 R2")
    desk.commit("card")
    refused(desk, desk.launch("build", str(desk.card)), "ruling 2026-01-02 R2: no such row")
    desk.write_card()
    desk.commit("card")
    done = desk.launch("build", str(desk.card), CLAUDE_STUB_EXIT="1")
    assert done.returncode == 1
    assert desk.called() == [str(desk.job_wt)]
    assert "WATCH:" not in done.stdout + done.stderr


def test_l4_the_header_says_installed_and_tested(desk):
    text = LAUNCH.read_text()
    assert "NOT INSTALLED" not in text
    assert "installed launcher" in text.splitlines()[1]
    assert "tests/ops/" in text.splitlines()[1]
