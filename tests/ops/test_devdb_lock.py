"""The cobalt_dev lock scripts and desk-launch.sh's launch gate (card 07 devdb-lock, R20, L76).

Every run here points the scripts at a tmp directory standing in for
/Users/cobalt/cobalt-wt (COBALT_WT_ROOT) and a tmp repo standing in for
/Users/cobalt/cobalt (COBALT_REPO_ROOT). The `.env` copied is a constructed
file in that tmp repo; the real one is never read. `claude` is a stub on PATH
that records its cwd and arguments.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
TAKE = REPO / "ops" / "desk" / "take-devdb-lock.sh"
RELEASE = REPO / "ops" / "desk" / "release-devdb-lock.sh"
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
LOCK_NAME = ".cobalt_dev.lock"
CONSTRUCTED_ENV = "COBALT_TEST_CONSTRUCTED=1\n"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


@pytest.fixture
def roots(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    wt.mkdir()
    repo.mkdir()
    (repo / ".env").write_text(CONSTRUCTED_ENV)
    for name in ("alpha", "beta"):
        (wt / name).mkdir()
    env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo))
    return wt, repo, env


def run(script: Path, *args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(script), *args], env=env, capture_output=True, text=True, timeout=300
    )


def owner(wt: Path) -> str:
    return (wt / LOCK_NAME / "owner").read_text().strip()


# ---- L1: the take and the release -------------------------------------------------------


def test_a_take_copies_the_env_by_name_and_records_its_worktree(roots):
    wt, repo, env = roots
    done = run(TAKE, "alpha", "0", env=env)
    assert done.returncode == 0, done.stderr
    assert (wt / LOCK_NAME).is_dir()
    assert owner(wt) == "alpha"
    assert (wt / "alpha" / ".env").read_text() == CONSTRUCTED_ENV
    assert not (wt / "beta" / ".env").exists()


def test_two_takes_at_once_exactly_one_wins(roots):
    wt, repo, env = roots
    for _ in range(5):
        procs = {
            name: subprocess.Popen(
                ["sh", str(TAKE), name, "0"], env=env,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            )
            for name in ("alpha", "beta")
        }
        codes = {name: p.wait(timeout=60) for name, p in procs.items()}
        for p in procs.values():
            p.communicate()
        assert sorted(codes.values()) == [0, 4], codes
        winner = next(name for name, code in codes.items() if code == 0)
        loser = next(name for name, code in codes.items() if code == 4)
        assert owner(wt) == winner
        assert (wt / winner / ".env").exists()
        assert not (wt / loser / ".env").exists()
        assert run(RELEASE, winner, env=env).returncode == 0


def test_the_loser_waits_then_exits_4_naming_the_holder(roots):
    wt, repo, env = roots
    assert run(TAKE, "alpha", "0", env=env).returncode == 0
    started = time.monotonic()
    done = run(TAKE, "beta", "1", env=env)
    waited = time.monotonic() - started
    assert done.returncode == 4, done.stderr
    assert waited >= 55, waited
    assert "cobalt_dev lock not free in 1 min (held by alpha)" in done.stdout + done.stderr
    assert owner(wt) == "alpha"
    assert not (wt / "beta" / ".env").exists()


def test_release_by_the_wrong_worktree_changes_nothing(roots):
    wt, repo, env = roots
    assert run(TAKE, "alpha", "0", env=env).returncode == 0
    done = run(RELEASE, "beta", env=env)
    assert done.returncode == 3, done.stderr
    assert owner(wt) == "alpha"
    assert (wt / "alpha" / ".env").read_text() == CONSTRUCTED_ENV
    # negative control: the holder releases, both are proven gone
    done = run(RELEASE, "alpha", env=env)
    assert done.returncode == 0, done.stderr
    assert "lock released" in done.stdout
    assert not (wt / LOCK_NAME).exists()
    assert not (wt / "alpha" / ".env").exists()


@pytest.mark.parametrize(
    "bad", ["", "a/b", "alpha/sub", "../alpha", "al pha", "al$pha", ".", "..", ".hidden"]
)
def test_a_bad_name_exits_2_and_touches_nothing(roots, bad):
    wt, repo, env = roots
    (wt / "alpha" / "sub").mkdir()  # a real directory: the name itself is refused, not its absence
    assert run(TAKE, bad, "0", env=env).returncode == 2
    assert run(RELEASE, bad, env=env).returncode == 2
    assert not (wt / LOCK_NAME).exists()
    assert sorted(p.name for p in wt.iterdir()) == ["alpha", "beta"]


def test_bad_minutes_exit_2(roots):
    wt, repo, env = roots
    for bad in ("", "x", "-1", "1.5"):
        assert run(TAKE, "alpha", bad, env=env).returncode == 2
    assert not (wt / LOCK_NAME).exists()


def test_release_leaves_the_env_when_no_lock_names_this_worktree(roots):
    wt, repo, env = roots
    (wt / "alpha" / ".env").write_text(CONSTRUCTED_ENV)
    done = run(RELEASE, "alpha", env=env)
    assert done.returncode != 0, done.stdout + done.stderr
    assert (wt / "alpha" / ".env").read_text() == CONSTRUCTED_ENV


def test_release_does_not_remove_a_lock_taken_after_it_saw_none(roots):
    wt, repo, env = roots
    stub = wt / "stubbin"
    stub.mkdir()
    real_rm = shutil.which("rm")
    (stub / "rm").write_text(
        "#!/bin/sh\n"
        "case \"$2\" in\n"
        "*/alpha/.env)\n"
        f"    mkdir \"{wt / LOCK_NAME}\"\n"
        f"    printf '%s\\n' beta > \"{wt / LOCK_NAME / 'owner'}\"\n"
        f"    printf '%s\\n' held-by-beta > \"{wt / 'beta' / '.env'}\"\n"
        "    ;;\n"
        "esac\n"
        f"exec {real_rm} \"$@\"\n"
    )
    (stub / "rm").chmod(0o755)
    done = run(RELEASE, "alpha", env=dict(env, PATH=f"{stub}{os.pathsep}{env['PATH']}"))
    assert (wt / LOCK_NAME / "owner").read_text().strip() == "beta", done.stdout + done.stderr
    assert (wt / "beta" / ".env").read_text() == "held-by-beta\n"


# ---- L2: desk-launch.sh launches build and check while the lock is held -------------------


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


@pytest.fixture
def desk(roots, tmp_path):
    """A tmp main repo with the three fixed files (copied from this tree), one job card
    whose build worktree exists, one deploy card, and a stub `claude`."""
    wt, repo, env = roots
    prompts = repo / "docs" / "40 - DevDocs" / "prompts"
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    (prompts / "2026-01-02").mkdir(parents=True)
    reports.mkdir(parents=True)
    for hub in ("BUILD-HUB.md", "CHECK-HUB.md", "DEPLOY-HUB.md"):
        shutil.copy(HUBS / hub, prompts / hub)
    # the approved, committed row the cards' RULINGS cite (desk-launch.sh, card 21 L1)
    (reports / "cto-2026-01-02.md").write_text(
        "| R1 | 07:00 ET | HIS RULING (constructed). | HIS RULING · APPROVED |\n")
    (repo / ".gitignore").write_text(".env\n")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    base = git(repo, "rev-parse", "--short=8", "HEAD")

    job_wt = wt / "x-job"
    git(repo, "worktree", "add", "-q", "-b", "ops/x-job", str(job_wt), base)
    build_report = job_wt / "docs" / "40 - DevDocs" / "reports" / "x-job-build.md"
    build_report.parent.mkdir(parents=True, exist_ok=True)
    build_report.write_text("BUILT · job: x-job\n")
    git(job_wt, "add", "-A")
    git(job_wt, "commit", "-q", "-m", "build")
    tip = git(job_wt, "rev-parse", "--short=8", "HEAD")
    # the BUILT line a check launch needs (desk-launch.sh, card 21 L2)
    build_report.write_text(f"BUILT · job: x-job · tip: {tip}\n")
    git(job_wt, "add", "-A")
    git(job_wt, "commit", "-q", "-m", "build report")

    card = prompts / "2026-01-02" / "01-x-job-card.md"
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {base}\nTIP: {tip}\nREPORT: {build_report}\n"
        f"CHECK REPORT: {reports / 'x-job-check.md'}\nHOUSE B: as needed\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
    )
    deploy = prompts / "2026-01-02" / "02-x-deploy-card.md"
    deploy.write_text(
        "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
        f"BASE: main\nTIP: {tip}\nREPORT: {reports / 'deploy-x.md'}\nRULINGS: none\n"
        "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n## MARKERS\n## SMOKE READS\n"
    )
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "cards")

    stub = tmp_path / "bin"
    stub.mkdir()
    calls = tmp_path / "claude-calls"
    (stub / "claude").write_text(
        '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
        f'printf "%s\\n" "$PWD" >> "{calls}"\nexit 0\n'
    )
    (stub / "claude").chmod(0o755)
    env = dict(env, PATH=f"{stub}:{os.environ['PATH']}", **GIT_ENV)
    return wt, card, deploy, env, calls


def hold_the_lock(wt: Path, by: str = "beta") -> None:
    (wt / LOCK_NAME).mkdir()
    (wt / LOCK_NAME / "owner").write_text(by + "\n")
    (wt / by / ".env").write_text(CONSTRUCTED_ENV)


def launch(env: dict, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(LAUNCH), *args], env=env, capture_output=True, text=True, timeout=120
    )


def test_build_and_check_launch_while_another_worktree_holds_the_lock(desk):
    wt, card, deploy, env, calls = desk
    hold_the_lock(wt)
    done = launch(env, "build", str(card))
    assert done.returncode == 0, done.stderr
    assert calls.read_text().splitlines() == [str(wt / "x-job")]
    done = launch(env, "check", str(card))
    assert done.returncode == 0, done.stderr
    assert calls.read_text().splitlines() == [str(wt / "x-job")] * 2


def test_a_resume_still_refuses_another_worktrees_env(desk):
    wt, card, deploy, env, calls = desk
    hold_the_lock(wt)
    for kind in ("build", "check"):
        done = launch(env, kind, str(card), "W")
        assert done.returncode == 1
        assert "the cobalt_dev lock is held" in done.stderr
    assert not calls.exists()


def test_a_resume_skips_its_own_env(desk):
    wt, card, deploy, env, calls = desk
    hold_the_lock(wt, by="x-job")
    done = launch(env, "build", str(card), "W")
    assert done.returncode == 0, done.stderr
    assert calls.read_text().splitlines() == [str(wt / "x-job")]


def test_deploy_is_refused_while_another_worktree_holds_the_env(desk):
    wt, card, deploy, env, calls = desk
    (wt / "beta" / ".env").write_text(CONSTRUCTED_ENV)
    done = launch(env, "deploy", str(deploy))
    assert done.returncode == 1
    assert "the cobalt_dev lock is held" in done.stderr
    assert not calls.exists()
    assert not (wt / "x-gate").exists()


def test_deploy_is_refused_while_the_lock_directory_is_held(desk):
    wt, card, deploy, env, calls = desk
    (wt / LOCK_NAME).mkdir()
    (wt / LOCK_NAME / "owner").write_text("beta\n")
    done = launch(env, "deploy", str(deploy))
    assert done.returncode == 1
    assert "the cobalt_dev lock is held by beta" in done.stderr
    assert not calls.exists()
    assert not (wt / "x-gate").exists()


def test_deploy_launches_when_no_lock_is_held(desk):
    """Negative control for the two deploy refusals."""
    wt, card, deploy, env, calls = desk
    done = launch(env, "deploy", str(deploy))
    assert done.returncode == 0, done.stderr
    assert (wt / "x-gate").is_dir()
    assert calls.read_text().splitlines() == [str(Path(env["COBALT_REPO_ROOT"]))]
