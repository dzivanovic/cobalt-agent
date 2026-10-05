"""ops/desk/preflight.sh — the mechanical PREFLIGHT rows of a build or a check (card 19 worker-steps S2).

A tmp repo stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) and a tmp directory for
/Users/cobalt/cobalt-wt (COBALT_WT_ROOT); the job worktree is a real `git worktree add` of
the tmp repo at BASE. Nothing outside tmp_path is read or written.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
PREFLIGHT = REPO / "ops" / "desk" / "preflight.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
REPORT_REL = "docs/40 - DevDocs/reports/x-job-build.md"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def commit(cwd: Path, msg: str) -> str:
    git(cwd, "add", "-A")
    git(cwd, "commit", "-q", "-m", msg)
    return git(cwd, "rev-parse", "--short=8", "HEAD")


@pytest.fixture
def job(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    (repo / "src").mkdir(parents=True)
    (repo / "docs").mkdir()
    (wt / "beta").mkdir(parents=True)
    (repo / "src" / "a.py").write_text("A = 1\n")
    (repo / "docs" / "x.md").write_text("doc\n")
    (repo / ".gitignore").write_text(".env\n")
    # the reports folder is tracked, as in the real tree: an untracked report shows as its own path
    (repo / "docs" / "40 - DevDocs" / "reports").mkdir(parents=True)
    (repo / "docs" / "40 - DevDocs" / "reports" / "x-earlier.md").write_text("# earlier\n")
    git(repo, "init", "-q", "-b", "main")
    base = commit(repo, "base")
    job_wt = wt / "x-job"
    git(repo, "worktree", "add", "-q", "-b", "ops/x-job", str(job_wt), base)
    prompts = repo / "docs" / "40 - DevDocs" / "prompts" / "2026-01-02"
    prompts.mkdir(parents=True)
    card = prompts / "01-x-job-card.md"
    env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo), **GIT_ENV)
    return wt, repo, job_wt, base, card, env


def write_card(card: Path, job_wt: Path, base: str, tip: str = "", check_report: str = "") -> None:
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {base}\nTIP: {tip}\nREPORT: {job_wt / REPORT_REL}\nCHECK REPORT: {check_report}\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
    )


def built(job_wt: Path, last: str) -> str:
    """A src commit (the tip), then the build report as a docs-only commit above it."""
    (job_wt / "src" / "a.py").write_text("A = 2\n")
    tip = commit(job_wt, "fix(x-job): a")
    report = job_wt / REPORT_REL
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(f"# report\n\n{last.format(tip=tip)}\n\n")
    commit(job_wt, "docs(x-job): build report")
    return tip


GOOD_LAST = "BUILT · job: x-job · tip: {tip} | on base | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0"


def preflight(env: dict, kind: str, card: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(PREFLIGHT), kind, str(card)], env=env, capture_output=True, text=True, timeout=120
    )


def last_line(done: subprocess.CompletedProcess) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.strip()][-1]


def rules(done: subprocess.CompletedProcess) -> list[str]:
    return [ln.split(" · ")[0] for ln in done.stdout.splitlines() if " · " in ln and not ln.startswith(" ")]


def test_a_build_at_base_passes_with_every_row(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    done = preflight(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    assert rules(done) == ["clock", "status", "head", "diff", "main repo", "env here", "env anywhere"]
    assert "## ops/x-job" in done.stdout


def test_a_build_on_its_own_wip_commit_passes(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / "tests").mkdir()
    (job_wt / "tests" / "test_a.py").write_text("def test_a():\n    assert False\n")
    commit(job_wt, "wip(x-job): red")
    done = preflight(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"


def test_a_worktree_on_another_branch_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    git(job_wt, "checkout", "-q", "-b", "other")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: status"


def test_an_uncommitted_file_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / "src" / "b.py").write_text("B = 1\n")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: status"


def test_a_build_on_a_foreign_commit_fails(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / "src" / "a.py").write_text("A = 3\n")
    commit(job_wt, "feat(x-job): not a wip")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"


def env_row(done: subprocess.CompletedProcess, rule: str) -> str:
    return next(ln for ln in done.stdout.splitlines() if ln.startswith(f"{rule} · "))


def test_an_env_in_this_worktree_fails_naming_it(job):
    """Card 02 A9: this worktree's .env is this job's failure; it is not listed as a sibling."""
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    (job_wt / ".env").write_text("COBALT_TEST_CONSTRUCTED=1\n")
    done = preflight(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: env here"
    assert env_row(done, "env here").endswith(f" · {job_wt / '.env'}")
    assert env_row(done, "env anywhere").endswith(" · siblings holding .env: none")


@pytest.mark.parametrize("kind", ["build", "check"])
def test_an_env_in_a_sibling_worktree_is_information_and_the_preflight_passes(job, kind):
    """Card 02 A9 (his 10-01 R20: the take waits): a sibling's .env is listed, never this job's failure."""
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST) if kind == "check" else ""
    write_card(card, job_wt, base, tip)
    (wt / "beta" / ".env").write_text("COBALT_TEST_CONSTRUCTED=1\n")
    (wt / "gamma").mkdir()
    (wt / "gamma" / ".env").write_text("COBALT_TEST_CONSTRUCTED=1\n")
    done = preflight(env, kind, card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    siblings = f"{wt / 'beta' / '.env'}, {wt / 'gamma' / '.env'}"
    assert env_row(done, "env anywhere").endswith(f" · siblings holding .env: {siblings}")


def test_no_env_anywhere_reads_none(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    done = preflight(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert env_row(done, "env anywhere").endswith(" · siblings holding .env: none")


def test_a_check_on_a_built_branch_passes_with_a_docs_only_commit_above_tip(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    assert rules(done) == ["clock", "status", "head", "env here", "env anywhere", "report", "range"]
    assert "fix(x-job): a" in done.stdout  # the range, quoted


def test_a_check_whose_report_ends_failed_fails(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, "FAILED: W — x")
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: report"


def test_a_check_whose_report_is_below_three_self_checks_passes_and_records_it(job):
    """Card 20 F1 (BUILD-HUB.md:97, CHECK-HUB.md:61): a lower self-check count is recorded, not failed."""
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST.replace("self-check: 3 of 3", "self-check: 2 of 3"))
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    assert "report: self-check 2 of 3 (recorded)" in done.stdout.splitlines()


def test_a_check_whose_report_has_no_self_check_field_fails(job):
    """Card 20 F1, negative control: no `self-check: <k> of 3` field still fails `report`."""
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST.replace(" | self-check: 3 of 3", ""))
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: report"


def test_a_check_with_a_src_commit_above_tip_fails(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    write_card(card, job_wt, base, tip)
    (job_wt / "src" / "a.py").write_text("A = 4\n")
    commit(job_wt, "fix(x-job): after the tip")
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"


# ---- card 03c M1: the card's own report, untracked and alone, is expected ---------------------
CHECK_REL = "docs/40 - DevDocs/reports/x-job-check.md"
EXPECTED = "status: clean but the report (untracked, expected)"


def untracked(job_wt: Path, rel: str) -> None:
    path = job_wt / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("# report\n\n(run in progress — next step under ## CONTINUE)\n")


def test_m1_a_build_with_its_untracked_report_alone_passes(job):
    """BUILD-HUB `## REPORT`: the first Write creates the report before PREFLIGHT runs."""
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    untracked(job_wt, REPORT_REL)
    done = preflight(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    assert EXPECTED in done.stdout.splitlines()
    assert REPORT_REL in done.stdout  # the status output, quoted in the row


def test_m1_the_report_and_one_more_untracked_file_fail_naming_the_other(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    untracked(job_wt, REPORT_REL)
    (job_wt / "src" / "b.py").write_text("B = 1\n")
    done = preflight(env, "build", card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert last_line(done) == "FAILED PREFLIGHT: status"
    assert "?? src/b.py" in done.stdout
    assert EXPECTED not in done.stdout


def test_m1_a_modified_tracked_report_is_not_the_expected_line(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    untracked(job_wt, REPORT_REL)
    commit(job_wt, "wip(x-job): red")
    (job_wt / REPORT_REL).write_text("# report\n\nchanged\n")
    done = preflight(env, "build", card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert last_line(done) == "FAILED PREFLIGHT: status"
    assert EXPECTED not in done.stdout


def test_m1_another_untracked_file_alone_still_fails(job):
    """Negative control: the one ignored line is the card's report path, nothing else."""
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base)
    untracked(job_wt, "docs/40 - DevDocs/reports/x-other-build.md")
    done = preflight(env, "build", card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert last_line(done) == "FAILED PREFLIGHT: status"
    assert EXPECTED not in done.stdout


def test_m1_a_build_does_not_ignore_the_check_report(job):
    wt, repo, job_wt, base, card, env = job
    write_card(card, job_wt, base, check_report=str(repo / CHECK_REL))
    untracked(job_wt, CHECK_REL)
    done = preflight(env, "build", card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert last_line(done) == "FAILED PREFLIGHT: status"


def test_m1_a_check_with_its_untracked_check_report_alone_passes(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    write_card(card, job_wt, base, tip, check_report=str(repo / CHECK_REL))
    untracked(job_wt, CHECK_REL)
    done = preflight(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
    assert EXPECTED in done.stdout.splitlines()


def test_m1_a_check_with_its_check_report_and_one_more_untracked_file_fails(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    write_card(card, job_wt, base, tip, check_report=str(repo / CHECK_REL))
    untracked(job_wt, CHECK_REL)
    (job_wt / "src" / "b.py").write_text("B = 1\n")
    done = preflight(env, "check", card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert last_line(done) == "FAILED PREFLIGHT: status"
    assert "?? src/b.py" in done.stdout


# ---- card 20 F2: a PASS-2 check reads the head at pass 1's `tip:` (CHECK-HUB.md:120) ----------
PASS1_LAST = (
    "CHECK DONE · job: x-job · pass: 1 · tip: {fix} · house A: h1 FINDINGS 1 · findings: 1 · dropped: 0"
    " · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: {house_b} · suites: offline 1/0"
    " · with-DB 0/0 · live-note 1/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none"
    " · files opened: 1 · ready: NO · decisions: 0 · for Dejan: 0"
)


def checked(job_wt: Path, house_b: str) -> str:
    """Pass 1's fix (a src commit above the card's TIP), then its CHECK REPORT as a docs-only commit."""
    (job_wt / "src" / "a.py").write_text("A = 5\n")
    fix = commit(job_wt, "fix(x-job): pass 1")
    path = job_wt / CHECK_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# check\n\n{PASS1_LAST.format(fix=fix, house_b=house_b)}\n\n")
    commit(job_wt, "docs(x-job): check report pass 1")
    return fix


def test_a_pass_2_check_with_the_pass_1_tip_above_the_card_tip_passes(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    checked(job_wt, "needed")
    write_card(card, job_wt, base, tip, check_report=str(job_wt / CHECK_REL))
    done = preflight(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"


def test_a_pass_1_report_that_says_house_b_not_needed_keeps_the_card_tip(job):
    """Negative control: only `house B: needed` moves the head reference."""
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    checked(job_wt, "not needed")
    write_card(card, job_wt, base, tip, check_report=str(job_wt / CHECK_REL))
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"


def test_a_pass_2_check_with_a_src_commit_above_the_pass_1_tip_fails(job):
    """Negative control: above pass 1's tip, only docs-only commits pass."""
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    checked(job_wt, "needed")
    (job_wt / "src" / "a.py").write_text("A = 6\n")
    commit(job_wt, "fix(x-job): after pass 1")
    write_card(card, job_wt, base, tip, check_report=str(job_wt / CHECK_REL))
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"


def test_l3_an_accented_worktree_is_refused_under_a_utf8_locale(job):
    """Card 03 L3: `[!A-Za-z0-9._-]` admits `é` under en_US.UTF-8 unless the script runs LC_ALL=C.
    The directory exists: only the name is refused."""
    wt, repo, job_wt, base, card, env = job
    (wt / "x-jobé").mkdir()
    write_card(card, job_wt, base)
    card.write_text(card.read_text().replace("WORKTREE: x-job", "WORKTREE: x-jobé"))
    env = dict(env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    done = preflight(env, "build", card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: WORKTREE 'x-jobé' is not one directory name" in done.stderr


@pytest.mark.parametrize("args", [[], ["build"], ["deploy", "x"], ["build", "/no/such/card.md"]])
def test_a_bad_call_is_refused(job, args):
    wt, repo, job_wt, base, card, env = job
    done = subprocess.run(
        ["sh", str(PREFLIGHT), *args], env=env, capture_output=True, text=True, timeout=60
    )
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
