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
        (self.prompts / "CTO-DESK-WAKEUP.md").write_text(
            "# wake-up (constructed)\n- LAUNCH (successor): `claude --bg \"Read wake\" --permission-mode "
            "dontAsk --remote-control cto-desk --name cto-desk`\n")
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
                     head: str | None = None, carry: str = "`held unfixed: 0` and `ready: YES`",
                     tips: str | None = None, row: bool = True, fix: str | None = None) -> None:
        """`fix` None: today's six columns; a string: the `fix report` column with that cell."""
        code_tip = code_tip or self.tip
        head = head or self.head
        fix_col, fix_sep, fix_cell = ("", "", "") if fix is None else (" fix report |", "---|", f" {fix} |")
        ship = f"| 1 | `ops/x-job` | `{code_tip}` | `{head}` | `{self.check_report}` | {carry} |{fix_cell}\n" if row else ""
        self.deploy.write_text(
            "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
            f"BASE: main\nTIP: {tips or head}\nREPORT: {self.reports / 'deploy-x.md'}\nRULINGS: {rulings}\n"
            "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n\n"
            f"| # | branch | code tip | branch head | check report | its stop line must carry |{fix_col}\n"
            f"|---|---|---|---|---|---|{fix_sep}\n{ship}\n"
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


def test_x1_a_check_whose_branch_adds_code_past_its_tip_refuses(desk):
    """CHECK-HUB.md PREFLIGHT: HEAD is TIP or a docs-only commit above it (check O2)."""
    (desk.job_wt / "src" / "y.py").write_text("Y = 1\n")
    desk.commit_job("src past the tip")
    refused(desk, desk.launch("check", str(desk.card)), "the tip is not the code tip")


def test_x1_a_check_whose_tip_is_not_on_the_branch_head_refuses(desk):
    """The branch rewound below TIP (check O2)."""
    git(desk.job_wt, "reset", "-q", "--hard", desk.base)
    desk.write_build_report(desk.built_line())
    refused(desk, desk.launch("check", str(desk.card)), "the tip is not the code tip")


@pytest.mark.parametrize("extra", [("E3",), ("PASS-2",)])
def test_x1_a_check_resume_or_pass_2_on_its_own_code_commits_launches(desk, extra):
    """Negative control for check O2: a resume or a second pass sits on the check's own fixes."""
    (desk.job_wt / "src" / "y.py").write_text("Y = 1\n")
    desk.commit_job("the check's own fix")
    desk.check_report.write_text("# check\n\nCHECK DONE · job: x-job · pass: 1 · house B: needed\n")
    done = desk.launch("check", str(desk.card), *extra)
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.job_wt)]


# ---- L3: every check committed and clean (kind deploy)---------------------------------------


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


def test_l3_a_deploy_card_whose_ships_table_has_no_row_refuses(desk):
    """The R41 answer to DECISION 3 (i): a head no check was proven for is never merged."""
    desk.ship()
    desk.write_deploy(row=False)
    desk.commit("card")
    refused(desk, desk.launch("deploy", str(desk.deploy)),
            f"deploy: ## SHIPS has no row; TIP head {desk.head} is checked by no row — "
            "add its ## SHIPS row and commit its check report")
    assert not desk.gate_left()


def test_l3_a_tip_head_that_is_the_head_of_no_ships_row_refuses(desk):
    """The R41 answer to DECISION 3 (ii): the second TIP head has no row."""
    desk.ship()
    desk.write_deploy(tips=f"{desk.head} {desk.base}")
    desk.commit("card")
    refused(desk, desk.launch("deploy", str(desk.deploy)),
            f"deploy: TIP head {desk.base} is the branch head of no ## SHIPS row — "
            "add its ## SHIPS row and commit its check report")
    assert not desk.gate_left()


def test_x1_a_ships_row_whose_head_tip_does_not_list_refuses(desk):
    """DEPLOY-HUB.md P3: each row's branch head is 'the same value TIP lists' (check O1)."""
    git(desk.repo, "branch", "ops/y-job", desk.tip)
    other = desk.reports / "y-job-check.md"
    other.write_text(f"# y-job check\n\n{check_line(desk.tip)}\n\n")
    desk.deploy.write_text(desk.deploy.read_text().replace(
        "|\n\n## MARKERS",
        f"|\n| 2 | `ops/y-job` | `{desk.tip}` | `{desk.tip}` | `{other}` | `held unfixed: 0` and `ready: YES` |\n\n## MARKERS"))
    desk.ship()
    refused(desk, desk.launch("deploy", str(desk.deploy)),
            f"deploy ops/y-job: the branch head {desk.tip} is no head TIP lists")
    assert not desk.gate_left()


def test_l3_a_step_d0_resume_with_no_ships_row_is_not_re_checked(desk):
    desk.write_deploy(row=False, tips=f"{desk.head} {desk.base}")
    desk.commit("card")
    (desk.wt / "x-gate").mkdir()
    done = desk.launch("deploy", str(desk.deploy), "STEP-D0")
    assert done.returncode == 0, done.stderr


def test_l3_a_step_d0_resume_is_not_re_checked(desk):
    desk.ship(check_line(desk.tip, ready="NO"))
    (desk.wt / "x-gate").mkdir()
    done = desk.launch("deploy", str(desk.deploy), "STEP-D0")
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.repo)]


# ---- F1: the small-fix tip (his R376, LAWS L75; deploy of 03d, cto-2026-10-05.md R405) ---------

DEPLOY_CARD = REPO / "ops" / "desk" / "deploy-card.sh"


def fix_round(desk: Desk, *, cell: bool = True, last: str | None = None,
              commit_report: bool = True, checked: str | None = None) -> tuple[str, str]:
    """The check ran on `checked` (default the build's tip); a small fix by the original builder
    then moved the code tip past it, and its fix-round report ends `BUILT · … tip: <code tip>`.
    `last` may carry FIXED / CHECKED for the two tips. Returns (checked, fixed)."""
    checked = checked or desk.tip
    (desk.job_wt / "src" / "x.py").write_text("X = 2\n")
    desk.commit_job("small fix after the check")
    fixed = short(desk.job_wt)
    report = desk.reports / "x-job-fix-build.md"
    desk.write_deploy(code_tip=fixed, head=fixed, fix=str(report) if cell else "")
    desk.ship(check_line(checked))
    line = (last or desk.built_line(fixed)).replace("FIXED", fixed).replace("CHECKED", checked)
    report.write_text(f"# x-job fix round\n\n## RECORDS\n- constructed\n\n{line}\n\n")
    if commit_report:
        desk.commit("fix report")
    return checked, fixed


def neither(checked: str, fixed: str) -> str:
    return (f"deploy ops/x-job: the check's tip '{checked}' is neither the code tip {fixed} "
            f"nor the branch head {fixed} — the check is not clean")


def test_f1_a_fix_round_past_the_checked_tip_launches(desk):
    """RED on BASE: refused with `neither the code tip`."""
    fix_round(desk)
    done = desk.launch("deploy", str(desk.deploy))
    assert done.returncode == 0, done.stderr
    assert (desk.wt / "x-gate").is_dir()
    assert desk.called() == [str(desk.repo)]


@pytest.mark.parametrize("case", ["(a) empty cell", "(b) BUILT for the checked tip",
                                  "(b) FAILED line naming the code tip", "(c) report uncommitted",
                                  "(d) checked tip not an ancestor"])
def test_f1_a_fix_round_missing_one_proof_still_refuses(desk, case):
    """Negative controls: each refuses on BASE already, and still refuses on the fixed script."""
    if case == "(a) empty cell":
        checked, fixed = fix_round(desk, cell=False)
    elif case == "(b) BUILT for the checked tip":
        checked, fixed = fix_round(desk, last=desk.built_line("CHECKED"))
    elif case == "(b) FAILED line naming the code tip":
        checked, fixed = fix_round(desk, last="FAILED: W — x · tip: FIXED")
    elif case == "(c) report uncommitted":
        checked, fixed = fix_round(desk, commit_report=False)
    else:
        checked, fixed = fix_round(desk, checked=short(desk.repo))  # main's cards commit
    refused(desk, desk.launch("deploy", str(desk.deploy)), neither(checked, fixed))
    assert not desk.gate_left()


def test_f1_a_fix_report_edited_after_its_commit_still_refuses(desk):
    checked, fixed = fix_round(desk)
    report = desk.reports / "x-job-fix-build.md"
    report.write_text(report.read_text() + "an edit after the commit\n" + desk.built_line(fixed) + "\n")
    refused(desk, desk.launch("deploy", str(desk.deploy)), neither(checked, fixed))
    assert not desk.gate_left()


def test_f1_a_fix_report_outside_the_reports_folder_still_refuses(desk):
    checked, fixed = fix_round(desk)
    stray = desk.prompts / "x-job-fix-build.md"
    stray.write_text((desk.reports / "x-job-fix-build.md").read_text())
    desk.write_deploy(code_tip=fixed, head=fixed, fix=str(stray))
    desk.commit("fix report outside reports")
    refused(desk, desk.launch("deploy", str(desk.deploy)), neither(checked, fixed))
    assert not desk.gate_left()


@pytest.mark.parametrize("line_tip", ["code tip", "head"])
def test_f1_a_card_of_todays_shape_passes_as_today(desk, line_tip):
    """No fix round: six columns, or the fix column with its cell empty (deploy-card.sh's rows)."""
    (desk.job_wt / "docs" / "late.md").write_text("late\n")
    desk.commit_job("docs past the code tip")
    new_head = short(desk.job_wt)
    for fix in (None, ""):
        desk.write_deploy(head=new_head, fix=fix)
        desk.ship(check_line(new_head if line_tip == "head" else desk.tip))
        done = desk.launch("deploy", str(desk.deploy))
        assert done.returncode == 0, done.stderr
        assert (desk.wt / "x-gate").is_dir()
        git(desk.repo, "worktree", "remove", "--force", str(desk.wt / "x-gate"))
        git(desk.repo, "branch", "-D", "deploy/x-deploy")


def ships_lines(text: str) -> list[str]:
    """The SHIPS header, its separator and its rows: the table lines under `## SHIPS`."""
    body = text.split("## SHIPS", 1)[1].split("\n## ", 1)[0]
    return [ln for ln in body.splitlines() if ln.startswith("|")]


def test_f1_deploy_card_writes_the_fix_report_column_and_its_empty_cell(desk):
    desk.ship()
    out = desk.prompts / "2026-01-02" / "05-x-set-deploy-card.md"
    done = subprocess.run(
        ["sh", str(DEPLOY_CARD), "--job", "x-set", "--set", "xset", "--worktree", "x-gate",
         "--tag", "x-tag", "--out", str(out), str(desk.card)],
        env=desk.env, capture_output=True, text=True, timeout=120,
    )
    assert done.returncode == 0, done.stderr
    header, sep, row = ships_lines(out.read_text())
    assert header.endswith("| fix report |"), header
    assert row.startswith("| 1 |") and row.endswith("| |"), row
    assert header.count("|") == sep.count("|") == row.count("|")


def test_f1_card_md_ships_header_has_the_fix_report_column_and_a_matching_separator():
    lines = (HUBS / "CARD.md").read_text().splitlines()
    i = next(n for n, ln in enumerate(lines) if ln.startswith("| # | branch | code tip |"))
    header, sep = lines[i], lines[i + 1]
    assert header.endswith("| fix report |"), header
    assert set(sep) <= set("|-")
    assert header.count("|") == sep.count("|")


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


def test_l4_a_real_desk_launch_prints_no_watch_line(desk):
    """The R41 answer to DECISION 3, gap (a): `desk` is no kind L4 names."""
    done = desk.launch("desk")
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.repo)]
    assert "WATCH:" not in done.stdout + done.stderr


def test_l4_a_real_prompt_launch_prints_no_watch_line(desk, tmp_path):
    """The R41 answer to DECISION 3, gap (a): `prompt` is no kind L4 names. The prompt kind reads
    its cwd only as a `cd /Users/cobalt/…` string, so it runs from a copy whose path pattern is
    re-pointed at tmp_path (the staging of tests/ops/test_desk_size_guard.py), guard stubbed."""
    staged = tmp_path / "ops" / "desk-launch.sh"
    staged.parent.mkdir()
    staged.write_text(LAUNCH.read_text().replace("\\/Users\\/cobalt\\/", str(tmp_path).replace("/", "\\/") + "\\/"))
    (tmp_path / "ops" / "desk-context.sh").write_text("#!/bin/sh\nexit 0\n")
    pfile = desk.prompts / "2026-01-02" / "04-x-prompt.md"
    pfile.write_text(
        f"cd {desk.repo}\n\nclaude --bg \"Read '{pfile}' and follow it exactly.\" --permission-mode auto "
        "--remote-control x-prompt --name x-prompt --disallowedTools \"AskUserQuestion\" \"EnterWorktree\"\n")
    desk.commit("prompt")
    done = subprocess.run(["sh", str(staged), "prompt", str(pfile)], env=desk.env,
                          capture_output=True, text=True, timeout=120)
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.repo)]
    assert "WATCH:" not in done.stdout + done.stderr


# ---- F5: the prompt kind's write strings (deny list never counts; allow list on his row) -------

# the second-writer survey's launch line (prompts/2026-10-05/01-second-writer-survey.md), its
# prompt path filled per test: `git commit` sits in its deny list, the `COBALT_ENV=dev` db query
# string in its allow list
SURVEY_LINE = (
    "claude --bg \"Read '{pfile}' and follow it exactly.\" --model claude-sonnet-5-5 --permission-mode auto "
    "--remote-control second-writer-survey --name second-writer-survey --allowedTools \"Read\" \"Write\" "
    "\"Edit\" \"Bash(COBALT_ENV=dev uv run cobalt db query --side system *)\" \"Bash(lsof -nP -iTCP:5432*)\" "
    "\"Bash(lsof -a -p *)\" \"Bash(ps -o *)\" \"Bash(sleep *)\" \"Bash(git -C /Users/cobalt/cobalt show*)\" "
    "\"Bash(git -C /Users/cobalt/cobalt log*)\" \"Bash(ls *)\" \"Bash(grep *)\" \"Bash(tail *)\" \"Bash(wc *)\" "
    "\"Bash(date*)\" --disallowedTools \"AskUserQuestion\" \"EnterWorktree\" \"Bash(git push*)\" "
    "\"Bash(git commit*)\" \"Bash(COBALT_ENV=dev uv run pytest*)\" \"Bash(COBALT_ENV=dev uv run cobalt db migrate*)\" "
    "\"Bash(COBALT_ENV=dev uv run cobalt db query --side system --prod*)\" "
    "\"Bash(sh /Users/cobalt/.claude/ops/take-devdb-lock.sh*)\" \"Bash(ps e*)\" \"Bash(ps -E*)\" "
    "--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt"
)
WRITE_REFUSAL = "on a prompt line: a write-path launch is a fixed file"


def staged_launcher(tmp_path: Path) -> Path:
    """The staging of test_l4_a_real_prompt_launch_prints_no_watch_line: the cwd pattern re-pointed
    at tmp_path, the desk-size guard stubbed."""
    staged = tmp_path / "ops" / "desk-launch.sh"
    staged.parent.mkdir()
    staged.write_text(LAUNCH.read_text().replace("\\/Users\\/cobalt\\/", str(tmp_path).replace("/", "\\/") + "\\/"))
    (tmp_path / "ops" / "desk-context.sh").write_text("#!/bin/sh\nexit 0\n")
    return staged


def survey_prompt(desk: Desk, rulings: str | None, line: str = SURVEY_LINE) -> Path:
    """A committed prompt in the survey's shape: the cwd, an optional RULINGS line, the launch line
    in a backticked span of the header (as the real prompt holds it)."""
    pfile = desk.prompts / "2026-01-02" / "05-second-writer-survey.md"
    head = "" if rulings is None else f"RULINGS: {rulings}\n"
    pfile.write_text(
        f"MODEL: Sonnet 5.5 · its line: `cd {desk.repo}`, then `{line.format(pfile=pfile)}` · SESSION: fresh\n"
        f"{head}\n# SURVEY (constructed)\n")
    desk.commit("prompt")
    return pfile


def launch_prompt(desk: Desk, tmp_path: Path, pfile: Path) -> subprocess.CompletedProcess:
    return subprocess.run(["sh", str(staged_launcher(tmp_path)), "prompt", str(pfile)], env=desk.env,
                          capture_output=True, text=True, timeout=120)


def test_f5_the_survey_prompt_launches_on_its_rulings_row(desk, tmp_path):
    """RED on BASE: refused on `git commit` (its deny list), then on the `COBALT_ENV=dev` db query
    string (its allow list)."""
    done = launch_prompt(desk, tmp_path, survey_prompt(desk, "2026-01-02 R1"))
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.repo)]


def test_f5_a_write_string_in_the_deny_list_is_never_a_write_string(desk, tmp_path):
    """(a) alone: no RULINGS line, no write string allowed; `git commit` and `COBALT_ENV=` only denied."""
    line = SURVEY_LINE.replace("\"Bash(COBALT_ENV=dev uv run cobalt db query --side system *)\" ", "")
    done = launch_prompt(desk, tmp_path, survey_prompt(desk, None, line))
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.repo)]


@pytest.mark.parametrize("case", [
    "no RULINGS line", "RULINGS none", "row absent", "row not HIS RULING", "row approved uncommitted",
    "write string outside both lists",
])
def test_f5_a_write_string_allowed_without_his_row_is_refused_as_today(desk, tmp_path, case):
    """Each refuses with today's write-string refusal, `claude` never called. Green on BASE too
    (refused there on `git commit`): the negative controls of the row."""
    rulings, line = "2026-01-02 R1", SURVEY_LINE
    if case == "no RULINGS line":
        rulings = None
    elif case == "RULINGS none":
        rulings = "none"
    elif case == "row absent":
        rulings = "2026-01-02 R2"
    elif case == "row not HIS RULING":
        desk.write_rulings(APPROVED_R1.replace("HIS RULING", "RECORD"))
    elif case == "write string outside both lists":
        line = SURVEY_LINE.replace(" --add-dir /Users/cobalt/Vault",
                                   " --append-system-prompt \"git add your report\" --add-dir /Users/cobalt/Vault")
    if case == "row approved uncommitted":
        desk.write_rulings(APPROVED_R1.replace("HIS RULING · APPROVED", "RECORD"))
        pfile = survey_prompt(desk, rulings)
        desk.write_rulings(APPROVED_R1, commit=False)
    else:
        pfile = survey_prompt(desk, rulings, line)
    done = launch_prompt(desk, tmp_path, pfile)
    refused(desk, done, "write string '")
    assert WRITE_REFUSAL in done.stderr, done.stderr
    if case == "write string outside both lists":
        assert "REFUSED: write string 'git add' " in done.stderr, done.stderr


def test_f5_a_ruled_write_line_still_runs_auto_or_plan_only(desk, tmp_path):
    """His row widens the write strings only; the permission-mode refusal stands."""
    line = SURVEY_LINE.replace("--permission-mode auto", "--permission-mode dontAsk")
    refused(desk, launch_prompt(desk, tmp_path, survey_prompt(desk, "2026-01-02 R1", line)),
            "permission mode 'dontAsk'")


# ---- card 03c M4: TREE STATE is optional on build and check cards -----------------------------


def set_tree_state(desk: Desk, line: str | None) -> None:
    """The job card with its `TREE STATE: unchanged` line replaced by `line` (None: no line)."""
    text = desk.card.read_text()
    assert "TREE STATE: unchanged\n" in text
    new = text.replace("TREE STATE: unchanged\n", "" if line is None else line + "\n")
    if new != text:
        desk.card.write_text(new)
        desk.commit("card: tree state")


@pytest.mark.parametrize("kind", ["build", "check"])
def test_m4_a_card_without_tree_state_launches(desk, kind):
    set_tree_state(desk, None)
    assert "TREE STATE" not in desk.card.read_text()
    done = desk.launch(kind, str(desk.card))
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.job_wt)]


@pytest.mark.parametrize("kind", ["build", "check"])
@pytest.mark.parametrize("line", ["TREE STATE: unchanged", "TREE STATE: row A3"])
def test_m4_a_card_with_a_valid_tree_state_still_launches(desk, kind, line):
    """Negative control: yesterday's cards launch unchanged."""
    set_tree_state(desk, line)
    done = desk.launch(kind, str(desk.card))
    assert done.returncode == 0, done.stderr
    assert desk.called() == [str(desk.job_wt)]


@pytest.mark.parametrize("kind", ["build", "check"])
@pytest.mark.parametrize("line", ["TREE STATE: nonsense", "TREE STATE:", "TREE STATE: row"])
def test_m4_a_card_with_a_tree_state_of_another_shape_is_refused(desk, kind, line):
    set_tree_state(desk, line)
    refused(desk, desk.launch(kind, str(desk.card)),
            "incomplete card: TREE STATE must be 'unchanged' or 'row <id>'")


def test_card03_l3_an_uppercase_job_is_refused_under_a_utf8_locale(desk):
    """Card 2026-10-03/03 L3: `[!a-z0-9-]` admits a capital under en_US.UTF-8 unless the
    script runs LC_ALL=C."""
    desk.card.write_text(desk.card.read_text().replace("JOB: x-job", "JOB: X-job"))
    desk.commit("card with an uppercase job")
    done = desk.launch("build", str(desk.card), LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    refused(desk, done, "incomplete card: JOB 'X-job' must be [a-z0-9-]")


def test_l4_the_header_says_installed_and_tested(desk):
    text = LAUNCH.read_text()
    assert "NOT INSTALLED" not in text
    assert "installed launcher" in text.splitlines()[1]
    assert "tests/ops/" in text.splitlines()[1]
