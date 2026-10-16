"""ops/desk/stage-set.sh — a check's whole reading set staged for a house in one call (card 19 worker-steps S4).

A tmp repo stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) and a tmp directory for
/Users/cobalt/cobalt-wt (COBALT_WT_ROOT), with its own agy-trial/scratch/. The job worktree
is a real `git worktree add`; its working copy is dirtied before staging, so every byte
staged is proved to come from git at TIP, never from the working files.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
STAGE = REPO / "ops" / "desk" / "stage-set.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
REPORT_REL = "docs/40 - DevDocs/reports/x-job-build.md"
SPACED = "src/a dir/with space.py"


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


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


@pytest.fixture
def job(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    (wt / "agy-trial" / "scratch").mkdir(parents=True)
    write(repo / "src" / "m.py", "X = 1\n")
    write(repo / "docs" / "page.md", "page\n")
    write(repo / ".gitignore", ".env\n")
    write(repo / "docs" / "40 - DevDocs" / "reports" / "cto-2026-01-02.md",
          "| row |\n| R1 | 09:00 ET | HIS RULING: the job. | APPROVED |\n")
    git(repo, "init", "-q", "-b", "main")
    base = commit(repo, "base")
    job_wt = wt / "x-job"
    git(repo, "worktree", "add", "-q", "-b", "ops/x-job", str(job_wt), base)
    write(job_wt / "tests" / "test_m.py", "def test_m():\n    assert False\n")
    commit(job_wt, "wip(x-job): red")
    write(job_wt / "src" / "m.py", "X = 2\n")
    write(job_wt / "tests" / "test_m.py", "def test_m():\n    assert True\n")
    write(job_wt / "docs" / "page.md", "page, changed\n")
    write(job_wt / SPACED, "S = 1\n")
    tip = commit(job_wt, "fix(x-job): m")
    write(job_wt / REPORT_REL, "# report\n\nBUILT · job: x-job\n")
    commit(job_wt, "docs(x-job): build report")
    card = repo / "docs" / "40 - DevDocs" / "prompts" / "2026-01-02" / "01-x-job-card.md"
    write(card, (
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {base}\nTIP: {tip}\nREPORT: {job_wt / REPORT_REL}\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
    ))
    commit(repo, "card")
    # the working copy differs from TIP: git, not the files, is the source
    write(job_wt / "src" / "m.py", "X = 'dirty'\n")
    write(job_wt / SPACED, "S = 'dirty'\n")
    env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo), **GIT_ENV)
    dest = wt / "agy-trial" / "scratch" / "tribunal-bars-0920" / "x-job-check"
    return wt, repo, job_wt, base, tip, card, env, dest


def stage(env: dict, card: Path, dest: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(STAGE), str(card), str(dest)], env=env, capture_output=True, text=True, timeout=120
    )


def blob(job_wt: Path, rev: str) -> bytes:
    return subprocess.run(["git", "cat-file", "blob", rev], cwd=job_wt, capture_output=True, check=True).stdout


def test_the_whole_set_is_staged_byte_equal_to_git_at_tip(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    done = stage(env, card, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    for path in ("src/m.py", "tests/test_m.py", "docs/page.md", SPACED):
        staged = dest / "files" / "wt" / path
        assert staged.read_bytes() == blob(job_wt, f"{tip}:{path}"), path
    assert (dest / "files" / "wt" / "src" / "m.py").read_text() == "X = 2\n"
    assert (dest / "files" / card.name).read_bytes() == card.read_bytes()
    assert (dest / "files" / "x-job-build.md").read_text() == "# report\n\nBUILT · job: x-job\n"
    diff = (dest / "diff.md").read_text()
    assert diff.splitlines()[0] == f'=== git log -p {base}..{tip} -- . ":(exclude)docs" (in {job_wt}) ==='
    assert sum(1 for ln in diff.splitlines() if ln.startswith("commit ")) == 2
    assert "page, changed" not in diff and "docs/page.md" not in diff
    rulings = (dest / "rulings.md").read_text()
    assert f'grep -n "^| R1 " "{repo}/docs/40 - DevDocs/reports/cto-2026-01-02.md"' in rulings
    assert "2:| R1 | 09:00 ET | HIS RULING: the job. | APPROVED |" in rulings
    lines = done.stdout.splitlines()
    files = sorted(p for p in dest.rglob("*") if p.is_file())
    assert lines[-1].startswith(f"STAGED {len(files)} files · ")
    assert lines[-1].endswith(" · commits 2")
    total = sum(p.stat().st_size for p in files)
    assert f" · {total} " in lines[-1]
    for p in files:
        assert f"{p.stat().st_size} {p}" in lines, p
    assert not any(p.name == ".env" for p in dest.rglob("*"))


def test_a_dest_outside_the_scratch_folder_is_refused(job, tmp_path):
    wt, repo, job_wt, base, tip, card, env, dest = job
    outside = wt / "agy-trial" / "elsewhere"
    done = stage(env, card, outside)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert not outside.exists()


def test_a_dest_with_dotdot_is_refused(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    sneaky = wt / "agy-trial" / "scratch" / ".." / "out"
    done = stage(env, card, sneaky)
    assert done.returncode == 1
    assert not (wt / "agy-trial" / "out").exists()


def test_a_non_empty_dest_is_refused_and_left_as_it_was(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    dest.mkdir(parents=True)
    (dest / "house-a.md").write_text("FINDINGS: 0\n")
    done = stage(env, card, dest)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert sorted(p.name for p in dest.iterdir()) == ["house-a.md"]


def test_an_env_path_in_the_diff_is_refused_with_the_dest_left_empty(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    git(job_wt, "checkout", "-q", "--", ".")
    write(job_wt / "configs" / ".env", "COBALT_TEST_CONSTRUCTED=1\n")
    git(job_wt, "add", "-f", "configs/.env")
    git(job_wt, "commit", "-q", "-m", "an env in the diff")
    new_tip = git(job_wt, "rev-parse", "--short=8", "HEAD")
    card.write_text(card.read_text().replace(f"TIP: {tip}", f"TIP: {new_tip}"))
    commit(repo, "card at the new tip")
    done = stage(env, card, dest)
    assert done.returncode == 1
    assert not dest.exists() or list(dest.iterdir()) == []


def test_l3_an_accented_worktree_is_refused_under_a_utf8_locale(job):
    """Card 03 L3: `[!A-Za-z0-9._-]` admits `é` under en_US.UTF-8 unless the script runs LC_ALL=C."""
    wt, repo, job_wt, base, tip, card, env, dest = job
    card.write_text(card.read_text().replace("WORKTREE: x-job", "WORKTREE: x-jobé"))
    commit(repo, "card with an accented worktree")
    env = dict(env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    done = stage(env, card, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: WORKTREE 'x-jobé' is not one directory name" in done.stderr
    assert not dest.exists() or list(dest.iterdir()) == []


@pytest.mark.parametrize("args", [[], ["one"], ["/no/such/card.md", "/tmp/x"]])
def test_a_bad_call_is_refused(job, args):
    wt, repo, job_wt, base, tip, card, env, dest = job
    done = subprocess.run(["sh", str(STAGE), *args], env=env, capture_output=True, text=True, timeout=60)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")


# Card 413 T1: a re-check of the same JOB clears its own prior staging, and nothing else.
CHECK_A = "docs/40 - DevDocs/reports/x-job-check-a.md"
CHECK_B = "docs/40 - DevDocs/reports/x-job-check-b.md"


def prior_staging(job, *, dest=None, report="main", change=True):
    """A first check staged at `dest`, its hub and house files beside it; then the card names a new check report.

    report: "main" (the prior check report committed on main), "untracked" (never committed),
    "branch" (committed only on the job branch, never on main).
    """
    wt, repo, job_wt, base, tip, card, env, fixture_dest = job
    dest = dest or fixture_dest
    card.write_text(card.read_text().replace(
        "TREE STATE:", f"CHECK REPORT: {repo / CHECK_A}\nTREE STATE:"))
    if report == "branch":
        write(job_wt / CHECK_A, "# check a\n")
        git(job_wt, "add", "--", CHECK_A)
        git(job_wt, "commit", "-q", "-m", "check a on the job branch")
    else:
        write(repo / CHECK_A, "# check a\n")
    paths = [str(card.relative_to(repo))] + ([CHECK_A] if report == "main" else [])
    git(repo, "add", "--", *paths)
    git(repo, "commit", "-q", "-m", "card with check a")
    done = stage(env, card, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    (dest / "HOUSE-INSTRUCTIONS.md").write_text("instructions\n")
    (dest / "house-a.md").write_text("FINDINGS: 0\n")
    (dest / "files" / "extra.md").write_text("a stage-copy copy\n")
    if change:
        card.write_text(card.read_text().replace(
            f"CHECK REPORT: {repo / CHECK_A}", f"CHECK REPORT: {repo / CHECK_B}"))
        git(repo, "add", "--", str(card.relative_to(repo)))
        git(repo, "commit", "-q", "-m", "card with check b")
    return dest


def snapshot(root: Path) -> dict:
    seen = {}
    for dirpath, dirnames, filenames in os.walk(root):
        for name in dirnames + filenames:
            p = Path(dirpath) / name
            rel = str(p.relative_to(root))
            if p.is_symlink():
                seen[rel] = ("link", os.readlink(p))
            elif p.is_dir():
                seen[rel] = ("dir",)
            else:
                seen[rel] = ("file", p.read_bytes())
    return seen


def test_c1_a_recheck_clears_its_own_prior_staging(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job)
    done = stage(env, card, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[0] == f"cleared: {dest} (prior check {repo / CHECK_A})"
    assert lines[-1].startswith("STAGED ")
    assert not (dest / "HOUSE-INSTRUCTIONS.md").exists()
    assert not (dest / "house-a.md").exists()
    assert not (dest / "files" / "extra.md").exists()
    staged_card = (dest / "files" / card.name).read_bytes()
    assert staged_card == blob(repo, f"HEAD:{card.relative_to(repo)}")
    assert f"CHECK REPORT: {repo / CHECK_B}".encode() in staged_card


def _foreign_file(dest):
    (dest / "notes.txt").write_text("notes\n")


def _symlink_in_wt(dest):
    os.symlink("/etc/hosts", dest / "files" / "wt" / "link")


def _env_in_wt(dest):
    (dest / "files" / "wt" / ".ENV").write_text("COBALT_TEST_CONSTRUCTED=1\n")


def _git_dir_in_files(dest):
    (dest / "files" / ".git").mkdir()
    (dest / "files" / ".git" / "HEAD").write_text("ref: refs/heads/main\n")


def _card_copy_one_byte(dest):
    copy = next(p for p in (dest / "files").iterdir() if p.name.endswith("-card.md"))
    copy.write_text(copy.read_text().replace("| row | what |", "| row | whAt |"))


@pytest.mark.parametrize("case, kwargs, spoil", [
    ("c2-foreign-file", {}, _foreign_file),
    ("c3-prior-report-untracked", {"report": "untracked"}, None),
    ("c4-prior-report-off-main", {"report": "branch"}, None),
    ("c5-symlink", {}, _symlink_in_wt),
    ("c6-dot-env", {}, _env_in_wt),
    ("c7-dot-git", {}, _git_dir_in_files),
    ("c8-card-copy-edited", {}, _card_copy_one_byte),
    ("c9-prior-is-this-check", {"change": False}, None),
])
def test_c2_c9_a_dest_that_fails_a_test_is_refused_and_untouched(job, case, kwargs, spoil):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, **kwargs)
    if spoil:
        spoil(dest)
    before = snapshot(dest)
    done = stage(env, card, dest)
    assert done.returncode == 1, case + done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), case + done.stderr
    assert "cleared:" not in done.stdout, case
    assert snapshot(dest) == before, case


def test_c10_a_range_refusal_comes_before_the_clear(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job)
    write(job_wt / "configs" / ".env", "COBALT_TEST_CONSTRUCTED=1\n")
    git(job_wt, "add", "-f", "configs/.env")
    git(job_wt, "commit", "-q", "-m", "an env in the diff")
    new_tip = git(job_wt, "rev-parse", "--short=8", "HEAD")
    card.write_text(card.read_text().replace(f"TIP: {tip}", f"TIP: {new_tip}"))
    git(repo, "add", "--", str(card.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "card at the new tip")
    done = stage(env, card, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith("REFUSED: ")
    assert "cleared:" not in done.stdout
    assert (dest / "house-a.md").read_text() == "FINDINGS: 0\n"


def test_c11_another_jobs_folder_is_not_cleared(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    other = dest.parent / "other-check"
    prior_staging(job, dest=other)
    before = snapshot(other)
    done = stage(env, card, other)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {other}")
    assert "cleared:" not in done.stdout
    assert snapshot(other) == before


def test_c12_the_script_removes_only_by_its_two_rm_rf_lines():
    text = STAGE.read_text()
    assert "git clean" not in text
    assert "-delete" not in text
    removing = [ln for ln in text.splitlines() if "rm -r" in ln]
    assert len(removing) == 2, removing
    assert all("rm -rf" in ln for ln in removing), removing


# Card 641 CS-1: the check of a fix round is a second card of the same JOB under another file name;
# it clears the first pass's folder, whose card copy carries the first card's name.
FR_CARD = "02-x-job-fr-card.md"


def fr_card(job, *, check=CHECK_B) -> Path:
    """A second committed card of the same JOB beside the first, naming `check` as its CHECK REPORT."""
    wt, repo, job_wt, base, tip, card, env, dest = job
    second = card.parent / FR_CARD
    second.write_text(card.read_text().replace(
        f"CHECK REPORT: {repo / CHECK_A}", f"CHECK REPORT: {repo / check}"))
    git(repo, "add", "--", str(second.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "fix round check card")
    return second


def first_copy(dest: Path, card: Path) -> Path:
    return dest / "files" / card.name


def test_cs1_a_fix_rounds_check_clears_the_first_passes_folder(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    second = fr_card(job)
    done = stage(env, second, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[0] == f"cleared: {dest} (prior check {repo / CHECK_A})"
    assert lines[-1].startswith("STAGED ")
    assert (dest / "files" / FR_CARD).read_bytes() == blob(repo, f"HEAD:{second.relative_to(repo)}")
    assert not first_copy(dest, card).exists()
    assert not (dest / "house-a.md").exists()
    assert not (dest / "HOUSE-INSTRUCTIONS.md").exists()
    assert not (dest / "files" / "extra.md").exists()


def _two_card_copies(job, dest, card):
    (dest / "files" / "03-x-job-other-card.md").write_bytes(first_copy(dest, card).read_bytes())


def _copy_of_another_job(job, dest, card):
    copy = first_copy(dest, card)
    copy.write_text(copy.read_text().replace("JOB: x-job\n", "JOB: y-job\n"))


def _copy_no_prompts_card(job, dest, card):
    # a card-shaped blob committed on main, but outside the prompts folder (one line more than the
    # card, so its blob is no version of any prompts card)
    wt, repo = job[0], job[1]
    page = repo / "docs" / "page.md"
    page.write_text(first_copy(dest, card).read_text() + "a page, not a card\n")
    git(repo, "add", "--", "docs/page.md")
    git(repo, "commit", "-q", "-m", "a card-shaped page")
    first_copy(dest, card).unlink()
    (dest / "files" / "x-card.md").write_bytes(page.read_bytes())


def _foreign_file_cs1(job, dest, card):
    (dest / "notes.txt").write_text("notes\n")


def _no_card_copy(job, dest, card):
    first_copy(dest, card).unlink()


def refused_untouched(job, spoil, check=CHECK_B):
    """The first pass staged, `spoil` applied, the SECOND card staged: refused, the dest untouched."""
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    if spoil:
        spoil(job, dest, card)
    second = fr_card(job, check=check)
    before = snapshot(dest)
    done = stage(env, second, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before


def test_cs1_control_two_card_copies_are_refused(job):
    refused_untouched(job, _two_card_copies)


def test_cs1_control_a_prior_copy_of_another_job_is_refused(job):
    refused_untouched(job, _copy_of_another_job)


def test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused(job):
    refused_untouched(job, _copy_no_prompts_card)


def test_cs1_control_the_second_pass_with_the_same_check_report_is_refused(job):
    refused_untouched(job, None, check=CHECK_A)


def test_cs1_control_a_foreign_file_blocks_the_clear(job):
    refused_untouched(job, _foreign_file_cs1)


def test_cs1_control_no_prior_card_copy_is_refused(job):
    refused_untouched(job, _no_card_copy)
