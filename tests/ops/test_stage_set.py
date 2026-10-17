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
        "HOUSE A: grok\nTREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
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
    (dest / "STAGED-CARD").write_text("x-card.md\n")


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


# Card 641 FR-1: a check stages READ copies of other cards into files/; the prior check card is the
# one whose header carries CHECK REPORT: and HOUSE A: and whose JOB is this JOB.
def build_card_copy(dest: Path, card: Path, name: str = "01-x-job-build-card.md") -> Path:
    """A build card's READ copy: the card text without `HOUSE A:`, `CHECK REPORT:` kept."""
    copy = dest / "files" / name
    copy.write_text(card.read_text().replace("HOUSE A: grok\n", ""))
    return copy


def other_job_check_cards(job, dest: Path) -> list[Path]:
    """Two check cards of `y-job` (CHECK REPORT: and HOUSE A:), committed under prompts, copied into files/."""
    wt, repo, job_wt, base, tip, card, env, fixture_dest = job
    copies = []
    for name, check in (("03-y-job-check-card.md", CHECK_A), ("04-y-job-fr-check-card.md", CHECK_B)):
        other = card.parent / name
        other.write_text(card.read_text().replace("JOB: x-job\n", "JOB: y-job\n").replace(
            f"CHECK REPORT: {repo / CHECK_A}", f"CHECK REPORT: {repo / check}"))
        git(repo, "add", "--", str(other.relative_to(repo)))
        git(repo, "commit", "-q", "-m", f"y-job card {name}")
        copy = dest / "files" / name
        copy.write_bytes(other.read_bytes())
        copies.append(copy)
    return copies


def test_fr1_a_build_card_read_copy_does_not_block_the_clear(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    assert "HOUSE A: grok\n" in first_copy(dest, card).read_text()
    build = build_card_copy(dest, card)
    assert "HOUSE A:" not in build.read_text() and "CHECK REPORT:" in build.read_text()
    second = fr_card(job)
    done = stage(env, second, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[0] == f"cleared: {dest} (prior check {repo / CHECK_A})"
    assert lines[-1].startswith("STAGED ")
    assert not build.exists()


def test_fr1_control_this_jobs_own_check_folder_shape(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    check_copy = first_copy(dest, card)
    build = build_card_copy(dest, card)
    others = other_job_check_cards(job, dest)
    second = fr_card(job)
    # refuse half: without this JOB's check card copy, two check cards of another JOB clear nothing
    kept = check_copy.read_bytes()
    check_copy.unlink()
    before = snapshot(dest)
    done = stage(env, second, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before
    # clear half: this JOB's check card copy back beside the build copy and the y-job cards
    check_copy.write_bytes(kept)
    done = stage(env, second, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[0] == f"cleared: {dest} (prior check {repo / CHECK_A})"
    assert lines[-1].startswith("STAGED ")
    for gone in [check_copy, build, *others]:
        assert not gone.exists(), gone
    assert (dest / "files" / FR_CARD).read_bytes() == blob(repo, f"HEAD:{second.relative_to(repo)}")


# Card 641 FR-2: a copy that is a version of a prompts card on main, so only the JOB test refuses it.
def test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    other = card.parent / "03-y-job-card.md"
    other.write_text(card.read_text().replace("JOB: x-job\n", "JOB: y-job\n"))
    assert f"CHECK REPORT: {repo / CHECK_A}\n" in other.read_text() and "HOUSE A: grok\n" in other.read_text()
    git(repo, "add", "--", str(other.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "a y-job card")
    first_copy(dest, card).unlink()
    (dest / "files" / other.name).write_bytes(other.read_bytes())
    (dest / "STAGED-CARD").write_text(other.name + "\n")
    second = fr_card(job)
    before = snapshot(dest)
    done = stage(env, second, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), done.stderr
    assert "the prior card copy's JOB is not x-job" in done.stderr, done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before


# Card 681 MK-1: the staging records the card it staged in <dest>/STAGED-CARD, its basename on one line.
def test_mk1_staging_writes_the_marker_naming_the_card(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    done = stage(env, card, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    marker = dest / "STAGED-CARD"
    assert marker.is_file() and not marker.is_symlink()
    assert marker.read_text() == card.name + "\n"


def test_mk1_a_restaging_rewrites_the_marker_with_the_new_card(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    second = fr_card(job)
    done = stage(env, second, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines()[0].startswith("cleared: ")
    assert (dest / "STAGED-CARD").read_text() == FR_CARD + "\n"


# Card 681 CL-1: clearable() takes the prior card from the marker; an unmarked folder (staged before
# the marker) takes the highest-numbered same-JOB check card of files/.
CHECK_C = "docs/40 - DevDocs/reports/x-job-check-c.md"
CHECK_R2 = "docs/40 - DevDocs/reports/x-job-check-r2.md"


def same_job_check_card(job, name: str, check: str) -> Path:
    """A committed check card of x-job under prompts (CHECK REPORT: `check`, HOUSE A:), not copied anywhere."""
    wt, repo, job_wt, base, tip, card, env, dest = job
    other = card.parent / name
    other.write_text(card.read_text().replace(
        f"CHECK REPORT: {repo / CHECK_A}", f"CHECK REPORT: {repo / check}"))
    git(repo, "add", "--", str(other.relative_to(repo)))
    git(repo, "commit", "-q", "-m", f"x-job card {name}")
    return other


def commit_report(job, rel: str) -> None:
    repo = job[1]
    write(repo / rel, f"# {rel}\n")
    git(repo, "add", "--", rel)
    git(repo, "commit", "-q", "-m", f"report {rel}")


def test_mk2_legacy_real_shape_of_the_band_routing_folder_clears(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    (dest / "STAGED-CARD").unlink(missing_ok=True)
    commit_report(job, CHECK_B)
    build = build_card_copy(dest, card)
    copies = [first_copy(dest, card), build]
    for name, check in (("02-x-job-check-card.md", CHECK_R2), ("03-x-job-fr-check-card.md", CHECK_B)):
        other = same_job_check_card(job, name, check)
        copy = dest / "files" / name
        copy.write_bytes(other.read_bytes())
        copies.append(copy)
    assert sorted(p.name for p in (dest / "files").glob("*-card.md")) == sorted(p.name for p in copies)
    third = same_job_check_card(job, "04-x-job-fr2-check-card.md", CHECK_C)
    done = stage(env, third, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[0] == f"cleared: {dest} (prior check {repo / CHECK_B})"
    assert lines[-1].startswith("STAGED ")
    for gone in copies:
        assert not gone.exists(), gone


def test_mk2_control_a_marker_naming_another_jobs_card_is_refused(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    others = other_job_check_cards(job, dest)
    (dest / "STAGED-CARD").write_text(others[0].name + "\n")
    second = fr_card(job)
    before = snapshot(dest)
    done = stage(env, second, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), done.stderr
    assert "the prior card copy's JOB is not x-job" in done.stderr, done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before


def test_mk2_two_same_job_cards_with_a_marker_clear_only_by_the_marker(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    commit_report(job, CHECK_B)
    higher = same_job_check_card(job, "02-x-job-fr-check-card.md", CHECK_B)
    (dest / "files" / higher.name).write_bytes(higher.read_bytes())
    third = same_job_check_card(job, "03-x-job-fr2-check-card.md", CHECK_C)
    # refuse half: the marker names a card that is not in files/
    (dest / "STAGED-CARD").write_text("09-x-job-gone-card.md\n")
    before = snapshot(dest)
    done = stage(env, third, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), done.stderr
    assert "no prior card copy" in done.stderr, done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before
    # clear half: the marker names the LOWER card, which wins over the higher-numbered one
    (dest / "STAGED-CARD").write_text(card.name + "\n")
    done = stage(env, third, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[0] == f"cleared: {dest} (prior check {repo / CHECK_A})"
    assert lines[-1].startswith("STAGED ")


def test_mk2_control_a_marker_that_is_no_card_file_name_is_refused(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    (dest / "STAGED-CARD").write_text("../x-card.md\n")
    second = fr_card(job)
    before = snapshot(dest)
    done = stage(env, second, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), done.stderr
    assert "the STAGED-CARD marker is not one card file name" in done.stderr, done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before


def test_mk2_control_a_marker_that_is_a_link_is_refused(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    (dest / "STAGED-CARD").unlink(missing_ok=True)
    os.symlink(dest / "files" / card.name, dest / "STAGED-CARD")
    second = fr_card(job)
    before = snapshot(dest)
    done = stage(env, second, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(f"REFUSED: the dest is not empty: {dest}"), done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before


def test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    (dest / "STAGED-CARD").unlink(missing_ok=True)
    build = build_card_copy(dest, card, name="05-x-job-build-card.md")
    second = fr_card(job)
    done = stage(env, second, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines()[0] == f"cleared: {dest} (prior check {repo / CHECK_A})"
    assert not build.exists()
