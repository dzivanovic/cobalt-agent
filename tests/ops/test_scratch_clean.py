"""scratch-clean.sh (card 2026-10-12/389 cleanup-class, row C1; his 2026-10-12 R1138 part 1, K1).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT), a tmp directory standing in for /Users/cobalt/cobalt-wt (COBALT_WT_ROOT)
holding one REAL registered worktree `x-job`, and a tmp directory standing in for
/Users/cobalt/.claude/jobs (COBALT_JOBS_ROOT) holding `job1/tmp`, with CLAUDE_JOB_DIR set to
`job1`. Every refusal is two-sided: its control, differing in that one thing, is removed.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRATCH_CLEAN = REPO / "ops" / "desk" / "scratch-clean.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
IGNORE = ".env\n!docs/_inflight/\ndocs/_inflight/*\n!docs/_inflight/README.md\n__pycache__/\n"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


class Desk:
    def __init__(self, tmp_path: Path) -> None:
        root = tmp_path.resolve()
        self.root = root
        self.repo = root / "repo"
        self.wt = root / "wt"
        self.jobs = root / "jobs"
        self.repo.mkdir()
        self.wt.mkdir()
        (self.jobs / "job1" / "tmp").mkdir(parents=True)
        self.job_dir = self.jobs / "job1"
        self.job_tmp = self.job_dir / "tmp"

        for rel, text in {
            ".gitignore": IGNORE,
            "a.txt": "a\n",
            "docs/x.md": "x\n",
            "docs/_inflight/README.md": "readme\n",
            "docs/mixed/t.md": "tracked\n",
            "src/pkg/mod.py": "x = 1\n",
        }.items():
            (self.repo / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.repo / rel).write_text(text)
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "base")

        self.job_wt = self.wt / "x-job"
        git(self.repo, "worktree", "add", "-q", "-b", "ops/x-job", str(self.job_wt), "main")

        self.env = dict(
            os.environ, COBALT_REPO_ROOT=str(self.repo), COBALT_WT_ROOT=str(self.wt),
            COBALT_JOBS_ROOT=str(self.jobs), CLAUDE_JOB_DIR=str(self.job_dir), **GIT_ENV,
        )

    def put(self, path: Path, text: str = "scratch\n") -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def run(self, *args: str, env: dict | None = None, cwd: Path | None = None) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["sh", str(SCRATCH_CLEAN), *args], env=self.env if env is None else env,
            cwd=cwd, capture_output=True, text=True, timeout=120,
        )


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def snap(p: Path):
    """The path's bytes, link target or tree, never following a link; None when absent."""
    if not os.path.lexists(p):
        return None
    if p.is_symlink():
        return ("link", os.readlink(p))
    if p.is_dir():
        return ("dir", sorted((c.name, snap(c)) for c in p.iterdir()))
    return ("file", p.read_bytes())


def removed(desk: Desk, path: Path | str, env: dict | None = None) -> None:
    done = desk.run(str(path), env=env)
    assert done.returncode == 0, done.stdout + done.stderr
    lines = done.stdout.splitlines()
    assert lines[0] == f"RUN: rm -rf -- {path}", lines
    assert lines[-1] == f"scratch-clean: removed {path}", lines
    assert done.stderr == ""
    assert not os.path.lexists(str(path))


def refused(desk: Desk, args: tuple[str, ...], *targets: Path, why: str, env: dict | None = None,
            cwd: Path | None = None) -> str:
    """Refused for the named reason `why` (a fragment of the one REFUSED line): the guards
    overlap, so a refusal by another guard would hide a broken one."""
    before = [snap(t) for t in targets]
    done = desk.run(*args, env=env, cwd=cwd)
    assert done.returncode == 1, done.stdout + done.stderr
    err = done.stderr.splitlines()
    assert len(err) == 1 and err[0].startswith("REFUSED: "), done.stderr
    assert why and why in err[0], err[0]
    assert "RUN:" not in done.stdout
    assert done.stdout == ""
    assert [snap(t) for t in targets] == before
    for t in targets:
        assert os.path.lexists(t), t
    return err[0]


# ---- ACCEPTED ------------------------------------------------------------------------------


def test_a1_an_ignored_inflight_probe_is_removed(desk):
    """The 386 shape (cto-2026-10-11.md R1135): a RUN probe under docs/_inflight/."""
    probe = desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py")
    removed(desk, probe)
    assert (desk.job_wt / "docs" / "_inflight" / "README.md").read_text() == "readme\n"


def test_a2_an_ignored_pycache_directory_is_removed(desk):
    cache = desk.job_wt / "src" / "pkg" / "__pycache__"
    desk.put(cache / "mod.cpython-314.pyc")
    desk.put(cache / "other.cpython-314.pyc")
    removed(desk, cache)
    assert (desk.job_wt / "src" / "pkg" / "mod.py").read_text() == "x = 1\n"


def test_a3_an_untracked_file_at_the_top_is_removed(desk):
    removed(desk, desk.put(desk.job_wt / "scratch.txt"))


def test_a4_an_untracked_directory_with_a_nested_directory_is_removed(desk):
    desk.put(desk.job_wt / "scratch" / "a" / "b" / "c.txt")
    desk.put(desk.job_wt / "scratch" / "top.txt")
    removed(desk, desk.job_wt / "scratch")


def test_a5_a_file_and_a_directory_under_the_job_tmp_are_removed(desk):
    removed(desk, desk.put(desk.job_tmp / "probe.py"))
    desk.put(desk.job_tmp / "run" / "deep" / "out.txt")
    removed(desk, desk.job_tmp / "run")
    assert desk.job_tmp.is_dir()


def test_a6_a_link_inside_is_removed_and_its_outside_target_is_intact(desk):
    outside = desk.put(desk.root / "outside.txt", "keep\n")
    desk.put(desk.job_wt / "scratch" / "f.txt")
    (desk.job_wt / "scratch" / "ln").symlink_to(outside)
    removed(desk, desk.job_wt / "scratch")
    assert outside.read_text() == "keep\n"


# ---- REFUSED: R1 arguments ------------------------------------------------------------------


def test_r1_no_argument_or_two_arguments_are_refused(desk):
    f = desk.put(desk.job_wt / "scratch.txt")
    refused(desk, (), f, why="usage:")
    refused(desk, (str(f), str(f)), f, why="usage:")
    removed(desk, f)


# ---- R2 the path's shape --------------------------------------------------------------------


def test_r2_a_relative_path_is_refused(desk):
    f = desk.put(desk.job_wt / "scratch.txt")
    refused(desk, ("scratch.txt",), f, why="is not an absolute path", cwd=desk.job_wt)
    removed(desk, f)


def test_r2_an_empty_path_is_refused(desk):
    f = desk.put(desk.job_wt / "scratch.txt")
    refused(desk, ("",), f, why="is not an absolute path", cwd=desk.job_wt)
    removed(desk, f)


def test_r2_a_path_with_a_newline_is_refused(desk):
    f = desk.put(desk.job_wt / "scratch.txt")
    g = desk.put(desk.job_wt / "scratch.txt\nx")
    refused(desk, (f"{f}\nx",), f, g, why="holds a newline")
    refused(desk, (f"{f}\n",), f, g, why="holds a newline")
    removed(desk, f)


# ---- R3 `..` ----------------------------------------------------------------------------------


def test_r3_a_dotdot_component_is_refused(desk):
    probe = desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py")
    refused(desk, (f"{desk.job_wt}/docs/../docs/_inflight/run_x.py",), probe, why="has a .. component")
    removed(desk, probe)


def test_r3_a_trailing_dotdot_is_refused(desk):
    inflight = desk.job_wt / "docs" / "_inflight"
    desk.put(inflight / "sub" / "f.txt")
    refused(desk, (f"{inflight}/sub/..",), inflight, why="has a .. component")
    removed(desk, inflight / "sub")


# ---- R4 existence -----------------------------------------------------------------------------


def test_r4_a_path_that_does_not_exist_is_refused(desk):
    f = desk.job_wt / "scratch.txt"
    done = desk.run(str(f))
    assert done.returncode == 1, done.stdout + done.stderr
    err = done.stderr.splitlines()
    assert len(err) == 1 and err[0].startswith("REFUSED: "), done.stderr
    assert "does not exist" in err[0], err[0]
    assert done.stdout == ""
    assert not os.path.lexists(f)
    desk.put(f)
    removed(desk, f)


def test_r4_a_dangling_link_is_refused(desk):
    f = desk.job_wt / "scratch.txt"
    f.symlink_to(desk.job_wt / "nowhere")
    refused(desk, (str(f),), f, why="does not resolve")
    f.unlink()
    removed(desk, desk.put(f))


# ---- R5 no symlink hop --------------------------------------------------------------------------


def test_r5_the_target_a_link_is_refused(desk):
    probe = desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py")
    link = desk.job_wt / "docs" / "_inflight" / "link.py"
    link.symlink_to(probe)
    refused(desk, (str(link),), link, probe, why="is not its own realpath")
    removed(desk, probe)


def test_r5_a_link_directory_on_the_way_is_refused(desk):
    probe = desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py")
    (desk.job_wt / "lnk").symlink_to(desk.job_wt / "docs" / "_inflight")
    refused(desk, (f"{desk.job_wt}/lnk/run_x.py",), probe, why="is not its own realpath")
    removed(desk, probe)


def test_r5_a_link_to_a_registered_worktree_is_refused(desk):
    probe = desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py")
    (desk.wt / "link-job").symlink_to(desk.job_wt)
    refused(desk, (f"{desk.wt}/link-job/docs/_inflight/run_x.py",), probe, why="is not its own realpath")
    removed(desk, probe)


@pytest.mark.parametrize("spelling", ["{wt}/docs/./_inflight/run_x.py", "{wt}/docs//_inflight/run_x.py"])
def test_r5_a_dot_or_doubled_slash_component_is_refused(desk, spelling):
    probe = desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py")
    refused(desk, (spelling.format(wt=desk.job_wt),), probe, why="is not its own realpath")
    removed(desk, probe)


def test_r5_a_trailing_slash_is_refused(desk):
    sub = desk.job_wt / "docs" / "_inflight" / "sub"
    desk.put(sub / "f.txt")
    refused(desk, (f"{sub}/",), sub, why="is not its own realpath")
    removed(desk, sub)


# ---- R6 under one root, strictly below it ----------------------------------------------------


def test_r6_the_repo_roots_own_ignored_file_is_refused(desk):
    main_probe = desk.put(desk.repo / "docs" / "_inflight" / "run_x.py")
    refused(desk, (str(main_probe),), main_probe, why="is outside")
    removed(desk, desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py"))


def test_r6_the_worktree_root_and_a_worktree_itself_are_refused(desk):
    f = desk.put(desk.job_wt / "scratch.txt")
    refused(desk, (str(desk.wt),), desk.job_wt, why="is outside")
    refused(desk, (str(desk.job_wt),), desk.job_wt, why="is a worktree itself")
    assert git(desk.job_wt, "rev-parse", "--abbrev-ref", "HEAD") == "ops/x-job"
    removed(desk, f)


def test_r6_a_directory_git_does_not_know_is_refused(desk):
    loose = desk.put(desk.wt / "not-a-worktree" / "f")
    refused(desk, (str(loose),), loose, why="is not a registered worktree")
    removed(desk, desk.put(desk.job_wt / "f"))


def test_r6_a_prefix_of_a_registered_name_is_refused(desk):
    loose = desk.put(desk.wt / "x-jo" / "f")
    refused(desk, (str(loose),), loose, why="is not a registered worktree")
    removed(desk, desk.put(desk.job_wt / "f"))


def test_r6_agy_trial_is_refused_though_registered(desk):
    git(desk.repo, "worktree", "add", "-q", "-b", "ops/agy", str(desk.wt / "agy-trial"), "main")
    f = desk.put(desk.wt / "agy-trial" / "scratch" / "f")
    refused(desk, (str(f),), f, why="agy-trial")
    removed(desk, desk.put(desk.job_wt / "scratch" / "f"))


def test_r6_the_job_tmp_itself_is_refused(desk):
    f = desk.put(desk.job_tmp / "f")
    refused(desk, (str(desk.job_tmp),), desk.job_tmp, why="is outside")
    removed(desk, f)


@pytest.mark.parametrize("job_dir", [None, "{wt}/x-job", "{jobs}", "{jobs}/job1/", "{jobs}/job1/tmp", "{root}/job1"])
def test_r6_a_job_tmp_path_without_its_job_dir_is_refused(desk, job_dir):
    f = desk.put(desk.job_tmp / "f")
    env = dict(desk.env)
    if job_dir is None:
        env.pop("CLAUDE_JOB_DIR")
    else:
        env["CLAUDE_JOB_DIR"] = job_dir.format(wt=desk.wt, jobs=desk.jobs, root=desk.root)
        # a real job-shaped directory outside COBALT_JOBS_ROOT: refused by its place, not its absence
        (desk.root / "job1" / "tmp").mkdir(parents=True)
    refused(desk, (str(f),), f, why="CLAUDE_JOB_DIR", env=env)
    removed(desk, f)


def test_r6_a_path_under_tmp_outside_both_roots_is_refused(desk):
    f = desk.put(desk.root / "elsewhere" / "f")
    refused(desk, (str(f),), f, why="is outside")
    removed(desk, desk.put(desk.job_tmp / "f"))


# ---- R7 never .git -------------------------------------------------------------------------------


def test_r7_the_worktrees_git_file_is_refused(desk):
    dotgit = desk.job_wt / ".git"
    refused(desk, (str(dotgit),), dotgit, why="names .git")
    removed(desk, desk.put(desk.job_wt / ".gitx"))


def test_r7_an_ignored_directory_holding_a_nested_git_is_refused(desk):
    cache = desk.job_wt / "src" / "pkg" / "__pycache__"
    desk.put(cache / "mod.pyc")
    desk.put(cache / "deep" / ".git" / "HEAD", "ref: refs/heads/main\n")
    refused(desk, (str(cache),), cache, why="holds .git below it")
    (cache / "deep" / ".git" / "HEAD").unlink()
    (cache / "deep" / ".git").rmdir()
    removed(desk, cache)


def test_r7_a_case_variant_of_git_is_refused(desk):
    scratch = desk.job_wt / "scratch"
    desk.put(scratch / ".GIT" / "x")
    refused(desk, (str(scratch),), scratch, why="holds .git below it")
    refused(desk, (str(scratch / ".GIT" / "x"),), scratch, why="names .git")
    (scratch / ".GIT" / "x").rename(scratch / "x")
    (scratch / ".GIT").rmdir()
    removed(desk, scratch)


# ---- R8 never .env --------------------------------------------------------------------------------


def test_r8_the_worktrees_env_is_refused(desk):
    env_file = desk.put(desk.job_wt / ".env", "COBALT_TEST_CONSTRUCTED=1\n")
    refused(desk, (str(env_file),), env_file, why="names .env")
    removed(desk, desk.put(desk.job_wt / ".envrc"))


def test_r8_a_case_variant_of_env_is_refused(desk):
    env_file = desk.put(desk.job_wt / ".ENV", "COBALT_TEST_CONSTRUCTED=1\n")
    refused(desk, (str(env_file),), env_file, why="names .env")
    removed(desk, desk.put(desk.job_wt / ".ENVRC"))


def test_r8_an_ignored_directory_holding_an_env_is_refused(desk):
    cache = desk.job_wt / "src" / "pkg" / "__pycache__"
    desk.put(cache / "mod.pyc")
    desk.put(cache / "deep" / ".env", "COBALT_TEST_CONSTRUCTED=1\n")
    refused(desk, (str(cache),), cache, why="holds .env below it")
    (cache / "deep" / ".env").unlink()
    removed(desk, cache)


def test_r8_a_job_tmp_directory_holding_an_env_is_refused(desk):
    run = desk.job_tmp / "run"
    desk.put(run / ".Env", "COBALT_TEST_CONSTRUCTED=1\n")
    refused(desk, (str(run),), run, why="holds .env below it")
    (run / ".Env").unlink()
    desk.put(run / "f")
    removed(desk, run)


# ---- R9 git proves it ------------------------------------------------------------------------------


def test_r9_a_tracked_file_is_refused(desk):
    tracked = desk.job_wt / "docs" / "x.md"
    refused(desk, (str(tracked),), tracked, why="is tracked")
    removed(desk, desk.put(desk.job_wt / "docs" / "y.md"))


def test_r9_a_modified_tracked_file_is_refused(desk):
    tracked = desk.put(desk.job_wt / "docs" / "x.md", "edited\n")
    refused(desk, (str(tracked),), tracked, why="is tracked")
    removed(desk, desk.put(desk.job_wt / "docs" / "y.md", "edited\n"))


def test_r9_a_directory_with_one_tracked_file_is_refused(desk):
    mixed = desk.job_wt / "docs" / "mixed"
    untracked = desk.put(mixed / "u.md")
    refused(desk, (str(mixed),), mixed, why="holds a tracked file")
    removed(desk, untracked)
    assert (mixed / "t.md").read_text() == "tracked\n"


def test_r9_the_worktrees_docs_is_refused(desk):
    desk.put(desk.job_wt / "docs" / "_inflight" / "run_x.py")
    refused(desk, (str(desk.job_wt / "docs"),), desk.job_wt / "docs", why="holds a tracked file")
    desk.put(desk.job_wt / "notes" / "_inflight" / "run_x.py")
    removed(desk, desk.job_wt / "notes")


# ---- R10 a job tmp path inside a git tree -----------------------------------------------------------


def test_r10_a_job_tmp_git_work_tree_is_refused(desk):
    nested = desk.job_tmp / "repo"
    desk.put(nested / "f.txt")
    git(nested, "init", "-q")
    refused(desk, (str(nested),), nested, why="holds .git below it")
    refused(desk, (str(nested / "f.txt"),), nested, why="sits inside a git work tree")
    plain = desk.put(desk.job_tmp / "plain" / "f.txt").parent
    removed(desk, plain)


# ---- SOURCE ------------------------------------------------------------------------------------------


def test_scratch_clean_holds_one_rm_and_no_other_removal():
    """As test_job_clean_is_never_forced: comments included."""
    text = SCRATCH_CLEAN.read_text()
    calls = [ln for ln in text.splitlines() if ln.strip().startswith("rm ")]
    assert [c.strip() for c in calls] == ['rm -rf -- "$p" 2>/dev/null'], calls
    assert [form for form in ("git clean", "git rm", "-delete", "--force") if form in text] == []
