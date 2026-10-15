"""Card 546 (deploy-freeze-1014, his R1471 item 1): a deploy freezes only the paths it ships.

ops/desk/deploy-shipped.sh (D1), the narrowed deploy guard of ops/desk/pre-commit (F1) and
the two DEPLOY-HUB.md lines (H1). Every run points COBALT_REPO_ROOT at a tmp real-git repo
built in tmp_path; the real repo is never touched. Brain R1472 (a): a test pins only the
lines this card changes, found by content; no whole fixed-file line, no commit literal.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
DESK = REPO / "ops" / "desk"
SHIPPED = DESK / "deploy-shipped.sh"
HOOK = DESK / "pre-commit"
HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md"

HUB_PATH = "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"
CARD_DIR = "docs/40 - DevDocs/prompts/2026-10-14"
REPORT_PATH = "docs/40 - DevDocs/reports/deploy-x.md"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

LIVE_X = '[{"id":"a1","name":"deploy-hub-x","pid":123}]'


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout


def card_text(repo: Path, job: str, tip: str) -> str:
    return (
        f"JOB: {job}\nBRANCH: deploy/{job}\nBASE: main\nTIP: {tip}\n"
        f"REPORT: {repo}/{REPORT_PATH}\n\n## SHIPS\n"
    )


def commit_file(repo: Path, rel: str, text: str, msg: str) -> None:
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    git(repo, "add", "--", rel)
    git(repo, "commit", "-q", "-m", msg, "--", rel)


@pytest.fixture
def deploy(tmp_path):
    """main with one commit; branch ops/x adds docs/a.md; the card x on main names its head."""
    repo = (tmp_path / "repo").resolve()
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    commit_file(repo, "docs/base.md", "base\n", "base")
    git(repo, "checkout", "-q", "-b", "ops/x")
    commit_file(repo, "docs/a.md", "a\n", "a")
    head = git(repo, "rev-parse", "HEAD").strip()[:8]
    git(repo, "checkout", "-q", "main")
    commit_file(repo, f"{CARD_DIR}/90-x-card.md", card_text(repo, "x", head), "card")
    cut = git(repo, "rev-parse", "HEAD").strip()
    env = dict(os.environ, COBALT_REPO_ROOT=str(repo), **GIT_ENV)
    return repo, cut, env


def shipped(*args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(SHIPPED), *args], env=env, capture_output=True, text=True, timeout=60
    )


# ---- D1: deploy-shipped.sh ------------------------------------------------------------------


def test_d1_lists_the_heads_paths_and_the_hub_file(deploy):
    repo, cut, env = deploy
    done = shipped("--job", "x", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [HUB_PATH, "docs/a.md"]
    # the card path form prints the same list
    by_path = shipped(str(repo / CARD_DIR / "90-x-card.md"), env=env)
    assert by_path.returncode == 0, by_path.stderr
    assert by_path.stdout == done.stdout


def test_d1_moved_prints_a_shipped_path_that_changed_on_main(deploy):
    repo, cut, env = deploy
    commit_file(repo, "docs/a.md", "a on main\n", "main moves a shipped path")
    done = shipped("--moved", cut, "--job", "x", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == ["docs/a.md"]


def test_d1_moved_is_empty_when_only_an_unshipped_path_moved(deploy):
    """NEGATIVE CONTROL: a path the deploy does not ship moved on main → nothing."""
    repo, cut, env = deploy
    commit_file(repo, "docs/other.md", "other\n", "main moves an unshipped path")
    done = shipped("--moved", cut, "--job", "x", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout == ""


def test_d1_a_build_card_of_the_same_job_is_not_the_deploy_card(deploy):
    """Check ask X4: a build or check card (BASE is 8 hex) with the same JOB is not counted."""
    repo, cut, env = deploy
    head = git(repo, "rev-parse", "ops/x").strip()[:8]
    build = card_text(repo, "x", head).replace("BASE: main", f"BASE: {head}")
    commit_file(repo, f"{CARD_DIR}/89-x-build-card.md", build, "build card")
    done = shipped("--job", "x", env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [HUB_PATH, "docs/a.md"]


@pytest.mark.parametrize(
    "case",
    ["unknown job", "two cards", "bad head", "short head", "no TIP line", "card outside prompts", "bad rev"],
)
def test_d1_refuses_no_card_two_cards_and_a_bad_head(deploy, case, tmp_path):
    repo, cut, env = deploy
    args = ["--job", "x"]
    if case == "unknown job":
        args = ["--job", "nosuchjob"]
    elif case == "two cards":
        # a recut naming the same, valid head: only the one-card rule can refuse it
        head = git(repo, "rev-parse", "ops/x").strip()[:8]
        commit_file(repo, f"{CARD_DIR}/91-x-card.md", card_text(repo, "x", head), "recut")
    elif case == "bad head":
        commit_file(repo, f"{CARD_DIR}/92-y-card.md", card_text(repo, "y", "zzzzzzzz"), "y")
        args = ["--job", "y"]
    elif case == "short head":
        head = git(repo, "rev-parse", "ops/x").strip()[:7]
        commit_file(repo, f"{CARD_DIR}/92-y-card.md", card_text(repo, "y", head), "y")
        args = ["--job", "y"]
    elif case == "no TIP line":
        commit_file(repo, f"{CARD_DIR}/93-z-card.md", "JOB: z\nBASE: main\n", "z")
        args = ["--job", "z"]
    elif case == "card outside prompts":
        outside = tmp_path / "90-x-card.md"
        outside.write_text((repo / CARD_DIR / "90-x-card.md").read_text())
        args = [str(outside)]
    elif case == "bad rev":
        args = ["--moved", "nosuchrev", "--job", "x"]
    done = shipped(*args, env=env)
    assert done.returncode == 1, (done.returncode, done.stderr)
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert done.stdout == ""


# ---- F1: the narrowed deploy guard -----------------------------------------------------------


@pytest.fixture
def guarded(deploy, tmp_path):
    """The real hook copied into the tmp repo; a stub claude names the live deploy hub."""
    repo, cut, env = deploy
    hooks = tmp_path / "hooks"
    hooks.mkdir()
    shutil.copy(HOOK, hooks / "pre-commit")
    (hooks / "pre-commit").chmod(0o755)
    git(repo, "config", "core.hooksPath", str(hooks))
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    stub = bin_dir / "claude"

    def live(json_text: str | None) -> None:
        if json_text is None:
            stub.write_text("#!/bin/sh\nexit 1\n")
        else:
            stub.write_text(f"#!/bin/sh\nprintf '%s\\n' '{json_text}'\n")
        stub.chmod(0o755)

    live(LIVE_X)
    env = dict(env, COBALT_DESK_DIR=str(DESK), PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}")
    return repo, env, live


def commit_with_hook(repo: Path, rel: str, text: str, env: dict) -> subprocess.CompletedProcess:
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
    subprocess.run(["git", "add", "--", rel], cwd=repo, env=env, check=True)
    return subprocess.run(
        ["git", "commit", "-q", "-m", "desk", "--", rel],
        cwd=repo, env=env, capture_output=True, text=True, timeout=120,
    )


def test_f1_a_shipped_path_is_refused_while_the_report_is_uncommitted(guarded):
    repo, env, live = guarded
    done = commit_with_hook(repo, "docs/a.md", "a on main\n", env)
    assert done.returncode == 1, done.stderr
    assert "ships" in done.stderr and "docs/a.md" in done.stderr, done.stderr


def test_f1_an_unshipped_path_commits_while_the_report_is_uncommitted(guarded):
    """The new-rule control. GREEN on BASE too, only because BASE's guard is skipped in a
    tmp repo (its toplevel test names the fixed path); its force is tests (5) and (7)."""
    repo, env, live = guarded
    done = commit_with_hook(repo, "docs/other.md", "other\n", env)
    assert done.returncode == 0, done.stderr


def test_f1_every_path_is_refused_once_the_report_is_committed_on_main(guarded):
    repo, env, live = guarded
    first = commit_with_hook(repo, REPORT_PATH, "report\n", env)
    assert first.returncode == 0, first.stderr
    done = commit_with_hook(repo, "docs/other.md", "other\n", env)
    assert done.returncode == 1, done.stderr
    assert "a deploy hub is live" in done.stderr, done.stderr
    assert "ships" not in done.stderr, done.stderr


def test_f1_the_report_path_alone_commits(guarded):
    """NEGATIVE CONTROL: the deploy's own report always passes."""
    repo, env, live = guarded
    done = commit_with_hook(repo, REPORT_PATH, "report\n", env)
    assert done.returncode == 0, done.stderr


def test_f1_no_live_hub_commits_anything(guarded):
    """NEGATIVE CONTROL: no deploy-hub- session → no freeze."""
    repo, env, live = guarded
    live("[]")
    done = commit_with_hook(repo, "docs/a.md", "a on main\n", env)
    assert done.returncode == 0, done.stderr


def test_f1_an_unreadable_session_list_commits_with_the_note(guarded):
    repo, env, live = guarded
    live(None)
    done = commit_with_hook(repo, "docs/a.md", "a on main\n", env)
    assert done.returncode == 0, done.stderr
    assert "could not read the session list" in done.stderr, done.stderr


@pytest.mark.parametrize(
    "json_text",
    [
        '[{"id":"a1","name":"deploy-hub-nocard","pid":123}]',
        '[{"id":"a1","name":"deploy-hub-x","pid":123},{"id":"a2","name":"deploy-hub-y","pid":124}]',
    ],
    ids=["no card", "two live hubs"],
)
def test_f1_a_card_that_cannot_be_found_refuses_all_paths(guarded, json_text):
    repo, env, live = guarded
    live(json_text)
    done = commit_with_hook(repo, "docs/other.md", "other\n", env)
    assert done.returncode == 1, done.stderr
    assert "a deploy hub is live" in done.stderr, done.stderr


@pytest.mark.parametrize("report", [None, "/elsewhere/deploy-x.md"], ids=["no REPORT", "REPORT outside docs"])
def test_f1_a_card_report_that_cannot_be_read_refuses_all_paths(guarded, report):
    """Arm (ii) fails closed: no REPORT: line, or one outside docs/, freezes every path."""
    repo, env, live = guarded
    card = repo / CARD_DIR / "90-x-card.md"
    lines = [line for line in card.read_text().splitlines() if not line.startswith("REPORT: ")]
    if report is not None:
        lines.append(f"REPORT: {report}")
    commit_file(repo, f"{CARD_DIR}/90-x-card.md", "\n".join(lines) + "\n", "card report")
    done = commit_with_hook(repo, "docs/other.md", "other\n", env)
    assert done.returncode == 1, done.stderr
    assert "a deploy hub is live" in done.stderr, done.stderr


def test_f1_a_staged_rename_of_a_shipped_path_is_refused(guarded):
    """Check O1: renaming a shipped path moves it on main; git lists only the new name."""
    repo, env, live = guarded
    commit_file(repo, HUB_PATH, "hub\n", "the hub file on main")  # hooks off: the fixture's own write
    subprocess.run(["git", "mv", "--", HUB_PATH, "docs/hub-moved.md"], cwd=repo, env=env, check=True)
    done = subprocess.run(
        ["git", "commit", "-q", "-m", "desk"],
        cwd=repo, env=env, capture_output=True, text=True, timeout=120,
    )
    assert done.returncode == 1, done.stderr
    assert HUB_PATH in done.stderr, done.stderr


def test_f1_a_report_line_with_a_trailing_blank_freezes_all_once_committed(guarded):
    repo, env, live = guarded
    card = repo / CARD_DIR / "90-x-card.md"
    text = card.read_text().replace(REPORT_PATH + "\n", REPORT_PATH + " \n")
    commit_file(repo, f"{CARD_DIR}/90-x-card.md", text, "card report blank")
    first = commit_with_hook(repo, REPORT_PATH, "report\n", env)
    assert first.returncode == 0, first.stderr
    done = commit_with_hook(repo, "docs/other.md", "other\n", env)
    assert done.returncode == 1, done.stderr
    assert "a deploy hub is live" in done.stderr, done.stderr


def test_f1_the_hook_is_one_deploy_guard_and_one_row_gate():
    """NEGATIVE CONTROL, green on BASE and after."""
    text = HOOK.read_text()
    assert text.count("# ---- deploy guard (begin)") == 1
    assert text.count("# ---- deploy guard (end)") == 1
    assert text.count("pre-commit: desk rows over 300 characters") == 1


# ---- H1: the hub text -----------------------------------------------------------------------


def hub_lines(prefix: str) -> list[str]:
    return [line for line in HUB.read_text().splitlines() if line.startswith(prefix)]


def test_h1_the_desk_line_names_the_shipped_paths_and_the_full_freeze_after_d20():
    lines = hub_lines("THE DESK WHILE YOU RUN")
    assert len(lines) == 1
    line = lines[0]
    assert "of a path this set ships" in line
    assert "deploy-shipped.sh" in line
    assert "of any path once your D2.0 report is committed" in line
    assert (
        "no desk commit and no staging on `main` from the launch to your stop line "
        "(the pre-commit guard refuses it)"
    ) not in line


def test_h1_d20_reverifies_the_shipped_paths_before_the_report_commit():
    lines = hub_lines("- D2.0 COMMIT THE REPORT")
    assert len(lines) == 1
    line = lines[0]
    assert line.count("deploy-shipped.sh --moved <m0>") == 1
    assert line.count("FAILED: D2.0 — shipped path moved since BASE") == 1
    assert line.index("deploy-shipped.sh --moved <m0>") < line.index(
        "git -C /Users/cobalt/cobalt add"
    )


def test_h1_the_other_freeze_lines_stand():
    """NEGATIVE CONTROL, green on BASE and after: the checks beside the new one stand."""
    text = HUB.read_text()
    assert text.count("main moved outside docs since the cut") == 1
    assert "main moved outside docs since the cut" in hub_lines("- MAIN:")[0]
    assert text.count("foreign commit on main") == 1
    assert "foreign commit on main" in hub_lines("4.3 ")[0]
    assert len(hub_lines("claude --bg ")) == 1
    d20 = hub_lines("- D2.0 COMMIT THE REPORT")
    assert len(d20) == 1
    assert d20[0].count("docs(report): deploy <JOB> — gate green on <m1>") == 1
