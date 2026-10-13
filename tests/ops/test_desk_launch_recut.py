"""desk-launch.sh recut "<deploy card>" (card 2026-10-03/03 adoption-scripts, row L5).

A deploy whose gate FAILED is recut in ONE call: gate-clean.sh on the failed gate; new BRANCH,
WORKTREE, TAG (`-attempt<n>`, n = the highest attempt present + 1) and REPORT
(`deploy-<…>-attempt<n>.md`) on the card; the card committed by desk-commit.sh; the desk row
by desk-row.sh; then the `deploy` kind's launch on the recut card. DESK_LAUNCH_DRY=1 makes
that last launch dry, as it does for every kind.

A tmp repo stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) with the three hub files, a
job branch whose check report is committed and clean, a deploy card, its failed gate
(a real worktree holding one merge) and a FAILED deploy report; a tmp directory stands in
for /Users/cobalt/cobalt-wt (COBALT_WT_ROOT); a stub `claude` on PATH records its cwd.
"""

from __future__ import annotations

import datetime
import os
import re
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
FAILED_LINE = "FAILED: gate — G (c) — tests/cobalt/test_x.py::test_y · rollback: not used"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def has_ref(repo: Path, ref: str) -> bool:
    return subprocess.run(
        ["git", "-C", str(repo), "show-ref", "--verify", "--quiet", ref], capture_output=True,
    ).returncode == 0


class Desk:
    def __init__(self, tmp_path: Path):
        root = tmp_path.resolve()
        self.wt = root / "wt"
        self.repo = root / "repo"
        self.wt.mkdir()
        self.repo.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        for hub in ("BUILD-HUB.md", "CHECK-HUB.md", "DEPLOY-HUB.md"):
            shutil.copy(HUBS / hub, self.prompts / hub)
        # today's desk report, where desk-row.sh appends (constructed rows only)
        self.today = self.reports / f"cto-{datetime.date.today():%Y-%m-%d}.md"
        self.today.write_text(
            "# cto (constructed)\n\n| # | time | row | status |\n|---|---|---|---|\n"
            "| R1 | 07:00 ET | a constructed row. | RECORD |\n\n## §5 CURRENT\n"
        )
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")

        # the job: a code commit (the tip), its build report (a docs-only head), its clean check
        self.job_wt = self.wt / "x-job"
        git(self.repo, "worktree", "add", "-q", "-b", "ops/x-job", str(self.job_wt), "main")
        (self.job_wt / "src").mkdir()
        (self.job_wt / "src" / "x.py").write_text("X = 1\n")
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", "code")
        self.tip = git(self.job_wt, "rev-parse", "--short=8", "HEAD")
        (self.job_wt / "docs" / "x-build.md").write_text("BUILT\n")
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", "report")
        self.head = git(self.job_wt, "rev-parse", "--short=8", "HEAD")
        self.check = self.reports / "x-job-check.md"
        self.check.write_text(
            f"# check\n\nCHECK DONE · job: x-job · pass: 1 · tip: {self.tip} · held unfixed: 0 · "
            "open: 0 · ready: YES · decisions: 0 · for Dejan: 0\n"
        )

        self.report = self.reports / "deploy-2026-01-02-1.md"
        self.card = self.prompts / "2026-01-02" / "02-x-deploy-card.md"
        self.card.write_text(
            "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
            f"BASE: main\nTIP: {self.head}\nREPORT: {self.report}\nRULINGS: none\n"
            "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n\n"
            "| # | branch | code tip | branch head | check report | its stop line must carry |\n"
            "|---|---|---|---|---|---|\n"
            f"| 1 | `ops/x-job` | `{self.tip}` | `{self.head}` | `{self.check}` | `held unfixed: 0` and `ready: YES` |\n\n"
            "## MARKERS\n## SMOKE READS\n"
        )
        self.commit("cards and checks")

        # the failed attempt: its gate holds one merge of the job; its report ends FAILED
        self.gate = self.wt / "x-gate"
        git(self.repo, "worktree", "add", "-q", "-b", "deploy/x-deploy", str(self.gate), "main")
        git(self.gate, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
        self.write_report(FAILED_LINE)

        stub = root / "bin"
        stub.mkdir()
        self.calls = root / "claude-calls"
        (stub / "claude").write_text(
            '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
            f'printf "%s\\n" "$PWD" >> "{self.calls}"\n'
        )
        (stub / "claude").chmod(0o755)
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{stub}:{os.environ['PATH']}", DESK_LAUNCH_DRY="1", **GIT_ENV,
        )

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def write_report(self, last: str) -> None:
        self.report.write_text(f"# deploy (constructed)\n\n## RECORDS\n- constructed\n\n{last}\n\n")
        self.commit("deploy report")

    def recut(self, *extra: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["sh", str(LAUNCH), "recut", str(self.card), *extra], env=self.env,
            capture_output=True, text=True, timeout=120,
        )

    def header(self) -> dict[str, str]:
        out = {}
        for line in self.card.read_text().splitlines():
            if not line.strip():
                break
            key, _, value = line.partition(": ")
            out[key] = value
        return out

    def called(self) -> list[str]:
        return self.calls.read_text().splitlines() if self.calls.exists() else []


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def index_of(lines: list[str], pattern: str) -> int:
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            return i
    raise AssertionError(f"no line matches {pattern!r}:\n" + "\n".join(lines))


def test_a_failed_deploy_is_recut_and_its_launch_printed_in_order(desk):
    old_card = desk.card.read_text()
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    out = done.stdout.splitlines()
    new_report = desk.reports / "deploy-2026-01-02-1-attempt2.md"

    # the failed gate is cleaned first (gate-clean.sh's own lines)
    i_clean = out.index(f"gate-clean: {desk.gate} and deploy/x-deploy removed")
    assert not desk.gate.exists() and not has_ref(desk.repo, "refs/heads/deploy/x-deploy")

    # the new values, the commit, the row, the launch line — in that order
    i_values = out.index("RECUT: x-deploy attempt 2")
    assert out[i_values + 1:i_values + 5] == [
        "BRANCH: deploy/x-deploy -> deploy/x-deploy-attempt2",
        "WORKTREE: x-gate -> x-gate-attempt2",
        "TAG: x-tag -> x-tag-attempt2",
        f"REPORT: {desk.report} -> {new_report}",
    ]
    i_commit = index_of(out, r"docs\(desk\): RECUT x-deploy attempt 2")
    i_row = index_of(out, r"^\| R2 \| \d\d:\d\d ET \| RECUT x-deploy attempt 2 — "
                     + re.escape(FAILED_LINE) + r" \| RECORD \|$")
    i_launch = out.index(f"git -C {desk.repo} worktree add -b deploy/x-deploy-attempt2 {desk.wt}/x-gate-attempt2 main")
    assert i_clean < i_values < i_commit < i_row < i_launch
    assert out[i_launch + 1] == f"cd {desk.repo}"
    assert out[i_launch + 2].startswith("claude --bg ")
    assert done.stderr.splitlines()[-1] == f'WATCH: sh {LAUNCH.parent}/desk-watch.sh deploy "{desk.card}"'

    # the card: four values changed, nothing else; committed by desk-commit.sh
    header = desk.header()
    assert (header["BRANCH"], header["WORKTREE"], header["TAG"], header["REPORT"]) == (
        "deploy/x-deploy-attempt2", "x-gate-attempt2", "x-tag-attempt2", str(new_report))
    assert desk.card.read_text() == (
        old_card.replace("BRANCH: deploy/x-deploy\n", "BRANCH: deploy/x-deploy-attempt2\n")
        .replace("WORKTREE: x-gate\n", "WORKTREE: x-gate-attempt2\n")
        .replace("TAG: x-tag\n", "TAG: x-tag-attempt2\n")
        .replace(f"REPORT: {desk.report}\n", f"REPORT: {new_report}\n"))
    assert git(desk.repo, "log", "-1", "--format=%s", "--", str(desk.card)) == "docs(desk): RECUT x-deploy attempt 2"
    assert git(desk.repo, "status", "--porcelain", "--", str(desk.card)) == ""
    # the desk row, in today's desk report
    assert f"| RECUT x-deploy attempt 2 — {FAILED_LINE} | RECORD |" in desk.today.read_text()
    # a dry launch: no session, no new gate
    assert desk.called() == []
    assert not (desk.wt / "x-gate-attempt2").exists()


def refused(desk: Desk, done: subprocess.CompletedProcess, text: str, old_card: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert "WATCH:" not in done.stdout + done.stderr
    assert desk.called() == []
    assert desk.card.read_text() == old_card
    assert git(desk.repo, "status", "--porcelain", "--", str(desk.card)) == ""
    assert "RECUT" not in desk.today.read_text()


def test_a_deploy_that_did_not_fail_is_refused(desk):
    desk.write_report("DEPLOYED · job: x-deploy · tag: x-tag")
    old = desk.card.read_text()
    refused(desk, desk.recut(), "recut: the deploy report does not end FAILED", old)
    assert desk.gate.is_dir()


def test_a_deploy_whose_rollback_ran_is_refused(desk):
    desk.write_report("FAILED: 4.3 — merge — x · rollback: used — migrations applied: none — aset: UP — radar: UP")
    old = desk.card.read_text()
    refused(desk, desk.recut(), "recut: the failed deploy names 'rollback: used'", old)
    assert desk.gate.is_dir()


def test_main_holding_the_gate_branch_is_refused_by_gate_clean(desk):
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "deploy/x-deploy")
    old = desk.card.read_text()
    refused(desk, desk.recut(), "main contains the gate's head", old)
    assert desk.gate.is_dir()


def test_an_attempt_name_already_present_is_never_reused(desk):
    """X5: a branch deploy/x-deploy-attempt2 already stands: the recut is attempt 3."""
    git(desk.repo, "branch", "deploy/x-deploy-attempt2", "main")
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    assert "RECUT: x-deploy attempt 3" in done.stdout.splitlines()
    header = desk.header()
    assert header["BRANCH"] == "deploy/x-deploy-attempt3"
    assert header["REPORT"] == str(desk.reports / "deploy-2026-01-02-1-attempt3.md")


def test_a_recut_of_a_recut_counts_from_the_cards_own_attempt(desk):
    """The card already carries attempt 2: the next is attempt 3, the suffix never doubled."""
    desk.card.write_text(desk.card.read_text()
                         .replace("BRANCH: deploy/x-deploy\n", "BRANCH: deploy/x-deploy-attempt2\n")
                         .replace("WORKTREE: x-gate\n", "WORKTREE: x-gate-attempt2\n")
                         .replace("TAG: x-tag\n", "TAG: x-tag-attempt2\n"))
    desk.commit("the card at attempt 2")
    git(desk.repo, "worktree", "move", str(desk.gate), str(desk.wt / "x-gate-attempt2"))
    git(desk.repo, "branch", "-m", "deploy/x-deploy", "deploy/x-deploy-attempt2")
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    header = desk.header()
    assert (header["BRANCH"], header["WORKTREE"], header["TAG"]) == (
        "deploy/x-deploy-attempt3", "x-gate-attempt3", "x-tag-attempt3")
    assert header["REPORT"] == str(desk.reports / "deploy-2026-01-02-1-attempt3.md")


LONG_MIDDLE = "tests/cobalt/test_x.py::test_y " * 13 + "y" * 3  # 406 characters
LONG_LINE = "FAILED: gate — G (c) — " + LONG_MIDDLE + " · rollback: not used"


def desk_row_size(row: str) -> int:
    """desk-row.sh's own count (`size(row)`, :36-40): a LAUNCHED row without its backticked spans."""
    if row.rstrip().endswith("| LAUNCHED |"):
        row = re.sub(r"`[^`]*`", "", row)
    return len(row)


def test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row(desk):
    """Card 63 N7. RED on BASE: exit 1, `recut: the desk row would be … over desk-row.sh's 300`."""
    assert len(LONG_MIDDLE) > 400
    desk.write_report(LONG_LINE)
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    rows = [ln for ln in desk.today.read_text().splitlines() if "RECUT x-deploy attempt 2" in ln]
    assert len(rows) == 1, rows
    row = rows[0]
    assert desk_row_size(row) <= 300, (desk_row_size(row), row)
    text = row.split(" ET | ", 1)[1]
    assert text.startswith("RECUT x-deploy attempt 2 — FAILED: gate — "), row
    assert row.endswith(" · rollback: not used | RECORD |"), row
    assert "…" in text, row
    # the cut keeps the middle's start, in order, and drops its end
    cut = text.removeprefix("RECUT x-deploy attempt 2 — FAILED: gate — ").removesuffix(
        " · rollback: not used | RECORD |")
    middle_kept = cut.removesuffix("…")
    assert cut.endswith("…") and ("G (c) — " + LONG_MIDDLE).startswith(middle_kept), cut
    # the row desk-row.sh printed is the row written
    assert row in done.stdout.splitlines(), done.stdout
    assert desk.header()["BRANCH"] == "deploy/x-deploy-attempt2"


@pytest.mark.parametrize("line", [
    pytest.param("FAILED: gate — G (c) — " + LONG_MIDDLE, id="(b) no rollback field"),
    pytest.param("FAILED: gate — G (c) — " + LONG_MIDDLE + " · rollback: used", id="(c) rollback used"),
])
def test_n7_a_long_line_the_cut_does_not_reach_still_refuses(desk, line):
    """Negative controls, green on BASE and after: no ` · rollback:` → refused for its size;
    `rollback: used` → refused as today, before any size is read."""
    desk.write_report(line)
    old = desk.card.read_text()
    done = desk.recut()
    if "rollback: used" in line:
        refused(desk, done, "recut: the failed deploy names 'rollback: used'", old)
    else:
        refused(desk, done, "recut: the desk row would be ", old)
        assert "characters, over desk-row.sh's 300" in done.stderr, done.stderr
    assert desk.gate.is_dir()


@pytest.mark.parametrize("extra", [("E3",), ("PASS-2",), ("E3", "PASS-2")])
def test_card03_l5_a_third_argument_is_refused_before_anything_runs(desk, extra):
    """AMENDED 10-03 (judge, ASK DESK 13): an ignored argument is a guess (L1)."""
    old = desk.card.read_text()
    done = desk.recut(*extra)
    refused(desk, done, "recut takes one argument, the card", old)
    # before anything: not even the desk-size guard's line
    assert (done.stdout, done.stderr) == ("", "REFUSED: recut takes one argument, the card\n")
    assert desk.gate.is_dir() and has_ref(desk.repo, "refs/heads/deploy/x-deploy")


def test_the_header_names_the_recut_kind():
    text = LAUNCH.read_text()
    assert 'desk-launch.sh recut "<absolute deploy card path>"' in text


# ---- card 2026-10-12 434 A1: a FAILED prior deploy's stale refs are archived, then the recut runs --

LINE_256 = (
    "FAILED PREFLIGHT: main moved outside docs since the cut — 55 paths (…); the desk re-cuts the "
    "gate · rollback: not used · aset: UP · radar: not in the set · decisions: 4 · for Dejan: 0 · "
    "tokens: 100737"
)
PRE_REFUSAL = "tag pre-x-deploy exists: the deploy got that far"
NOT_ARCHIVED = PRE_REFUSAL + " — not archived: "


def short(repo: Path, rev: str) -> str:
    return git(repo, "rev-parse", "--short=8", rev)


def stale_256(desk: Desk) -> tuple[str, str]:
    """The 256 shape (deploy-aset-orphan-1010.md :130, :132, :146, :248): the report committed on
    main (D2.0, `<pre-merge>` = P), `pre-<job>` at P (D2.6), main merged into the gate (D2.1,
    `<stack-final>` = S, S^2 = P), then the report FAILED and committed on main."""
    desk.report.write_text("# deploy (constructed)\n\n## Deploy table\n- D2.0 gate green\n")
    desk.commit("docs(report): deploy x-deploy — gate green")
    p = short(desk.repo, "main")
    git(desk.repo, "tag", "pre-x-deploy", "main")
    git(desk.gate, "merge", "-q", "--no-edit", "main")
    s = short(desk.gate, "HEAD")
    desk.report.write_text(
        "# deploy (constructed)\n\n## Deploy table\n"
        f"- D2.0 … `rev-parse --short=8 main` → `{p}` = `<pre-merge>`.\n"
        f"- D2.2 `<stack-final>` = `{s}`; `rev-parse --short=8 {s}^2` → `{p}` = `<pre-merge>`.\n\n"
        f"{LINE_256}\n"
    )
    desk.commit("deploy report")
    return p, s


def refs(repo: Path) -> str:
    return git(repo, "for-each-ref", "--format=%(refname) %(objectname)")


def worktrees(repo: Path) -> str:
    return git(repo, "worktree", "list", "--porcelain")


def archive_refs(repo: Path) -> list[str]:
    out = git(repo, "for-each-ref", "--format=%(refname)", "refs/tags/archive", "refs/heads/archive")
    return out.splitlines()


def nothing_archived(desk: Desk, done: subprocess.CompletedProcess, old_card: str,
                     before: tuple[str, str], gate: Path) -> None:
    """Exit 1 by the archive's own refusal; refs, trees, card and desk report as they were."""
    refused(desk, done, NOT_ARCHIVED, old_card)
    assert (refs(desk.repo), worktrees(desk.repo)) == before
    assert gate.is_dir()
    assert "ARCHIVE:" not in done.stdout


def test_ra1_the_256_state_is_archived_then_recut(desk):
    """RED on BASE: exit 1, `REFUSED: tag pre-x-deploy exists: the deploy got that far`."""
    p, s = stale_256(desk)
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    out = done.stdout.splitlines()

    i_run = out.index(f"RUN: sh {LAUNCH.parent}/job-clean.sh salvage x-gate")
    i_salv = out.index(f"job-clean salvage: removed {desk.gate}; deleted none; kept deploy/x-deploy")
    i_branch = index_of(out, r"^ARCHIVE: branch deploy/x-deploy -> archive/deploy/x-deploy-\d{8}-\d{4} \("
                        + s + r"\)$")
    i_tag = index_of(out, r"^ARCHIVE: tag pre-x-deploy -> archive/pre-x-deploy-\d{8}-\d{4} \(" + p + r"\)$")
    i_done = out.index("ARCHIVE: x-deploy done; recut proceeds")
    i_values = out.index("RECUT: x-deploy attempt 2")
    assert i_run < i_salv < i_branch < i_tag < i_done < i_values
    assert not any(line.startswith("gate-clean:") for line in out), done.stdout

    # the archive: both names under archive/, on the same commits, one stamp
    stamp = re.search(r"archive/pre-x-deploy-(\d{8}-\d{4})", out[i_tag]).group(1)
    assert f"archive/deploy/x-deploy-{stamp}" in out[i_branch]
    assert short(desk.repo, f"refs/tags/archive/pre-x-deploy-{stamp}^{{commit}}") == p
    assert short(desk.repo, f"refs/heads/archive/deploy/x-deploy-{stamp}") == s
    assert not has_ref(desk.repo, "refs/tags/pre-x-deploy")
    assert not has_ref(desk.repo, "refs/heads/deploy/x-deploy")
    assert not desk.gate.exists()
    assert str(desk.gate) not in worktrees(desk.repo)

    # then the recut as today (:178-193): the four values, the commit, the row, the launch
    new_report = desk.reports / "deploy-2026-01-02-1-attempt2.md"
    assert out[i_values + 1:i_values + 5] == [
        "BRANCH: deploy/x-deploy -> deploy/x-deploy-attempt2",
        "WORKTREE: x-gate -> x-gate-attempt2",
        "TAG: x-tag -> x-tag-attempt2",
        f"REPORT: {desk.report} -> {new_report}",
    ]
    i_commit = index_of(out, r"docs\(desk\): RECUT x-deploy attempt 2")
    i_row = index_of(out, r"^\| R2 \| \d\d:\d\d ET \| RECUT x-deploy attempt 2 — FAILED PREFLIGHT: .* \| RECORD \|$")
    i_launch = out.index(f"git -C {desk.repo} worktree add -b deploy/x-deploy-attempt2 {desk.wt}/x-gate-attempt2 main")
    assert i_values < i_commit < i_row < i_launch
    assert out[i_launch + 1] == f"cd {desk.repo}"
    assert out[i_launch + 2].startswith("claude --bg ")
    assert done.stderr.splitlines()[-1] == f'WATCH: sh {LAUNCH.parent}/desk-watch.sh deploy "{desk.card}"'
    assert desk.header()["BRANCH"] == "deploy/x-deploy-attempt2"
    assert desk.called() == []


def recut_by_hand_to_attempt2(desk: Desk) -> Path:
    """As :255-263, with the REPORT moved to attempt 2 too: the gate moved, the branch renamed."""
    report2 = desk.reports / "deploy-2026-01-02-1-attempt2.md"
    report2.write_text(f"# deploy attempt 2 (constructed)\n\n{LINE_256}\n")
    desk.card.write_text(desk.card.read_text()
                         .replace("BRANCH: deploy/x-deploy\n", "BRANCH: deploy/x-deploy-attempt2\n")
                         .replace("WORKTREE: x-gate\n", "WORKTREE: x-gate-attempt2\n")
                         .replace("TAG: x-tag\n", "TAG: x-tag-attempt2\n")
                         .replace(f"REPORT: {desk.report}\n", f"REPORT: {report2}\n"))
    desk.commit("the card at attempt 2")
    gate2 = desk.wt / "x-gate-attempt2"
    git(desk.repo, "worktree", "move", str(desk.gate), str(gate2))
    git(desk.repo, "branch", "-m", "deploy/x-deploy", "deploy/x-deploy-attempt2")
    return gate2


@pytest.mark.parametrize("case", ["(i) the deploy tag exists", "(ii) an earlier attempt's report DEPLOYED"])
def test_ra2_a_deployed_prior_is_refused_before_and_after(desk, case):
    """RED on BASE: stderr lacks `— not archived:` (gate-clean's own refusal)."""
    p, s = stale_256(desk)
    gate, branch = desk.gate, "deploy/x-deploy"
    if case.startswith("(i)"):
        git(desk.repo, "tag", "x-tag", "main")
    else:
        gate, branch = recut_by_hand_to_attempt2(desk), "deploy/x-deploy-attempt2"
        desk.report.write_text(desk.report.read_text()
                               + f"\nDEPLOYED x-tag {p} | set: x-job · constructed\n")
        desk.commit("an earlier attempt DEPLOYED (constructed)")
    old, before = desk.card.read_text(), (refs(desk.repo), worktrees(desk.repo))
    done = desk.recut()
    nothing_archived(desk, done, old, before, gate)
    assert short(desk.repo, "refs/tags/pre-x-deploy^{commit}") == p
    assert short(desk.repo, f"refs/heads/{branch}") == s
    assert archive_refs(desk.repo) == []
    assert NOT_ARCHIVED + "DEPLOYED" in done.stderr, done.stderr


def _ra3_tag_moved(desk, p, s):
    git(desk.repo, "tag", "-f", "pre-x-deploy", "main")  # main is one commit past P (the report)
    assert short(desk.repo, "refs/tags/pre-x-deploy^{commit}") != p


def _ra3_gate_moved_on(desk, p, s):
    git(desk.gate, "commit", "-q", "--allow-empty", "-m", "one more on the gate")


def _ra3_report_off(desk, p, s):
    other = short(desk.repo, f"{s}^1")
    desk.report.write_text(desk.report.read_text().replace(s, other))
    desk.commit("the report names another stack-final")


def _ra3_main_holds_gate(desk, p, s):
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "deploy/x-deploy")


def _ra3_gate_switched(desk, p, s):
    git(desk.gate, "switch", "-q", "-c", "x-other")


def _ra3_env(desk, p, s):
    (desk.gate / ".env").write_text("X=constructed\n")


def _ra3_lock(desk, p, s):
    lock = desk.wt / ".cobalt_dev.lock"
    lock.mkdir()
    (lock / "owner").write_text("x-gate\n")


@pytest.mark.parametrize("move, reason", [
    pytest.param(_ra3_tag_moved, "is not the report's <pre-merge>", id="(a) tag moved"),
    pytest.param(_ra3_gate_moved_on, "is not the report's <stack-final>", id="(b) gate moved on"),
    pytest.param(_ra3_report_off, "is not the report's <stack-final>", id="(c) report names another"),
    pytest.param(_ra3_main_holds_gate, "main contains the gate's head", id="(d) main holds the gate"),
    pytest.param(_ra3_gate_switched, "with deploy/x-deploy checked out", id="(e) gate switched"),
    pytest.param(_ra3_env, "/.env exists", id="(f) .env in the gate"),
    pytest.param(_ra3_lock, "the lock directory", id="(g) lock owned by the gate"),
])
def test_ra3_a_ref_off_its_report_is_refused_before_and_after(desk, move, reason):
    """RED on BASE: stderr lacks `— not archived:` (gate-clean's own refusal)."""
    p, s = stale_256(desk)
    move(desk, p, s)
    old, before = desk.card.read_text(), (refs(desk.repo), worktrees(desk.repo))
    done = desk.recut()
    nothing_archived(desk, done, old, before, desk.gate)
    assert archive_refs(desk.repo) == []
    refusal = [ln for ln in done.stderr.splitlines() if ln.startswith("REFUSED: " + NOT_ARCHIVED)]
    assert len(refusal) == 1 and reason in refusal[0], done.stderr


def test_ra4_a_salvage_refusal_archives_nothing(desk):
    """RED on BASE: the refusal is gate-clean's."""
    stale_256(desk)
    git(desk.repo, "worktree", "lock", str(desk.gate))
    old, before = desk.card.read_text(), (refs(desk.repo), worktrees(desk.repo))
    done = desk.recut()
    assert done.returncode == 1, done.stdout + done.stderr
    assert "INSPECT: locked: yes" in done.stdout.splitlines(), done.stdout
    assert f"REFUSED: recut: job-clean.sh salvage refused; nothing archived: {desk.gate}" in done.stderr, done.stderr
    assert (refs(desk.repo), worktrees(desk.repo)) == before
    assert desk.gate.is_dir() and desk.card.read_text() == old
    assert archive_refs(desk.repo) == [] and "ARCHIVE:" not in done.stdout
    assert "RECUT" not in desk.today.read_text()


def test_ra5_a_dirty_gate_is_kept_on_a_wip_branch(desk):
    """RED on BASE: refused at the pre tag."""
    p, s = stale_256(desk)
    (desk.gate / "notes.txt").write_text("constructed\n")
    done = desk.recut()
    assert done.returncode == 0, done.stdout + done.stderr
    wips = git(desk.repo, "for-each-ref", "--format=%(refname:short)", "refs/heads/wip").splitlines()
    assert len(wips) == 1 and re.fullmatch(r"wip/x-gate-salvage-\d{8}", wips[0]), wips
    assert git(desk.repo, "show", f"{wips[0]}:notes.txt") == "constructed"
    out = done.stdout.splitlines()
    index_of(out, r"^ARCHIVE: branch deploy/x-deploy -> archive/deploy/x-deploy-\d{8}-\d{4} \(" + s + r"\)$")
    index_of(out, r"^ARCHIVE: tag pre-x-deploy -> archive/pre-x-deploy-\d{8}-\d{4} \(" + p + r"\)$")
    assert "ARCHIVE: x-deploy done; recut proceeds" in out
    assert not desk.gate.exists()


def recut_arm() -> list[str]:
    """The recut arm: from `recut)` at column 0 to its own `    ;;`, comment lines dropped."""
    lines = LAUNCH.read_text().splitlines()
    start = lines.index("recut)")
    end = lines.index("    ;;", start)
    return [ln for ln in lines[start:end + 1] if not ln.lstrip().startswith("#")]


def test_ra6_the_recut_arm_deletes_no_ref_it_did_not_copy():
    """RED on BASE: `tag "$at"` absent."""
    arm = recut_arm()
    made = [i for i, ln in enumerate(arm) if 'tag "$at"' in ln]
    dropped = [i for i, ln in enumerate(arm) if "tag -d" in ln]
    assert made, "no `tag \"$at\"` in the recut arm"
    assert len(dropped) == 1 and dropped[0] > made[0], (made, dropped)
    for word in ("branch -D", "branch -d", "worktree remove"):
        assert not any(word in ln for ln in arm), word
    # gate-clean.sh: step 1's two lines only (its RUN line and its call)
    calls = [ln.strip() for ln in arm if "gate-clean.sh" in ln]
    assert calls == ["printf 'RUN: sh %s/gate-clean.sh \"%s\"\\n' \"$here\" \"$card\"",
                     'sh "$here/gate-clean.sh" "$card" || exit 1'], calls


@pytest.mark.parametrize("taken", ["tag archive/pre-x-deploy-20261012-1930",
                                   "branch archive/deploy/x-deploy-20261012-1930"])
def test_ra7_an_archive_name_already_present_is_refused(desk, taken):
    """Archive test (g). RED on BASE: stderr lacks `— not archived:`."""
    stale_256(desk)
    stub = desk.wt.parent / "bin"
    (stub / "date").write_text(
        '#!/bin/sh\nif [ "$*" = "+%Y%m%d-%H%M" ]; then echo 20261012-1930; exit 0; fi\nexec /bin/date "$@"\n')
    (stub / "date").chmod(0o755)
    what, name = taken.split(" ")
    git(desk.repo, what, name, "main")
    old, before = desk.card.read_text(), (refs(desk.repo), worktrees(desk.repo))
    done = desk.recut()
    nothing_archived(desk, done, old, before, desk.gate)
    assert archive_refs(desk.repo) == [f"refs/{'tags' if what == 'tag' else 'heads'}/{name}"]
    refusal = [ln for ln in done.stderr.splitlines() if ln.startswith("REFUSED: " + NOT_ARCHIVED)]
    assert len(refusal) == 1 and name in refusal[0], done.stderr


def test_o1_an_archive_name_blocked_by_an_existing_ref_is_refused_before_anything(desk):
    """Check O1: `refs/tags/archive` makes every `archive/pre-…` tag uncreatable (a D/F conflict)."""
    stale_256(desk)
    git(desk.repo, "tag", "archive", "main")
    old, before = desk.card.read_text(), (refs(desk.repo), worktrees(desk.repo))
    done = desk.recut()
    refused(desk, done, NOT_ARCHIVED, old)
    assert (refs(desk.repo), worktrees(desk.repo)) == before
    assert desk.gate.is_dir()
