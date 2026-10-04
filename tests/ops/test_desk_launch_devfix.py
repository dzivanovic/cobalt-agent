"""desk-launch.sh devfix "<card>": the dev-maintenance kind beside `build` (card 12 devfix-route, F2).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT) and a tmp directory standing in for /Users/cobalt/cobalt-wt
(COBALT_WT_ROOT), the shape of tests/ops/test_devdb_lock.py. The fixed file in the
tmp repo is a constructed one-line DEVFIX-HUB.md whose line carries every token the
script fills; one test runs the tree's own DEVFIX-HUB.md (F1) through the same
script. `claude` is a stub on PATH that records its cwd. Nothing here reads a real
`.env`, a real card or a real database.
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

# a constructed fixed file: its one line carries every token `devfix` fills
STANDIN_LINE = (
    "claude --bg \"Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEVFIX-HUB.md' and "
    "follow it exactly. CARD: '<card>' TABLE: <table> PROOF: <proof test>\" "
    "--model claude-opus-5-5 --permission-mode dontAsk --remote-control <job>-devfix "
    "--name <job>-devfix --allowedTools \"Read\" "
    "\"Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)\" "
    "--disallowedTools \"AskUserQuestion\" \"EnterWorktree\" --add-dir /Users/cobalt/cobalt-wt"
)

TABLE = "user.x_table"
PROOF = "tests/cobalt/test_x_proof.py::test_x_holds"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def card_text(base: str, reports: Path, **over: str) -> str:
    keys = {
        "JOB": "x-fix",
        "LADDER": "OFF-LADDER — cto-2026-01-02.md 2026-01-02 R1",
        "BRANCH": "ops/x-fix",
        "WORKTREE": "x-fix",
        "BASE": base,
        "REPORT": str(reports / "devfix-x-fix-2026-01-02.md"),
        "RULINGS": "2026-01-02 R1",
        "TABLE": TABLE,
        "PROOF TEST": PROOF,
    }
    keys.update(over)
    head = "".join(f"{k}: {v}\n" for k, v in keys.items() if v is not None)
    return head + "\n## RECORDS\n- constructed\n"


class Desk:
    def __init__(self, tmp_path: Path, hub_text: str):
        self.wt = tmp_path / "wt"
        self.repo = tmp_path / "repo"
        self.wt.mkdir()
        self.repo.mkdir()
        (self.repo / ".env").write_text(CONSTRUCTED_ENV)
        for name in ("alpha", "beta"):
            (self.wt / name).mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        shutil.copy(HUBS / "BUILD-HUB.md", self.prompts / "BUILD-HUB.md")
        (self.prompts / "DEVFIX-HUB.md").write_text(hub_text)
        # the approved, committed row the cards' RULINGS cite (desk-launch.sh, card 21 L1)
        (self.reports / "cto-2026-01-02.md").write_text(
            "| R1 | 07:00 ET | HIS RULING (constructed). | HIS RULING · APPROVED |\n")
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "base")
        self.base = git(self.repo, "rev-parse", "--short=8", "HEAD")
        self.card = self.prompts / "2026-01-02" / "01-x-fix-card.md"
        self.write_card()
        self.commit("card")
        stub = tmp_path / "bin"
        stub.mkdir()
        self.calls = tmp_path / "claude-calls"
        (stub / "claude").write_text(
            '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
            f'printf "%s\\n" "$PWD" >> "{self.calls}"\nexit 0\n'
        )
        (stub / "claude").chmod(0o755)
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{stub}:{os.environ['PATH']}", **GIT_ENV,
        )

    def write_card(self, **over: str) -> None:
        self.card.write_text(card_text(self.base, self.reports, **over))

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def launch(self, *args: str, dry: bool = True) -> subprocess.CompletedProcess:
        env = dict(self.env, DESK_LAUNCH_DRY="1") if dry else self.env
        return subprocess.run(
            ["sh", str(LAUNCH), *args], env=env, capture_output=True, text=True, timeout=120
        )

    def filled(self, line: str) -> str:
        return (
            line.replace("<card>", str(self.card)).replace("<job>", "x-fix")
            .replace("<worktree>", "x-fix").replace("<table>", TABLE)
            .replace("<proof test>", PROOF)
        )


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path, "# DEVFIX-HUB (constructed, installed)\n\n" + STANDIN_LINE + "\n")


def refused(done: subprocess.CompletedProcess, text: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert done.stdout == ""


# ---- a good card -------------------------------------------------------------------------


def test_a_good_card_prints_the_worktree_add_the_cd_and_the_filled_line(desk):
    done = desk.launch("devfix", str(desk.card))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [
        f"git -C {desk.repo} worktree add -b ops/x-fix {desk.wt / 'x-fix'} {desk.base}",
        f"cd {desk.wt / 'x-fix'}",
        desk.filled(STANDIN_LINE),
    ]
    assert not (desk.wt / "x-fix").exists()


def test_a_good_card_runs_the_add_and_the_line_in_the_new_worktree(desk):
    done = desk.launch("devfix", str(desk.card), dry=False)
    assert done.returncode == 0, done.stderr
    assert git(desk.wt / "x-fix", "rev-parse", "--abbrev-ref", "HEAD") == "ops/x-fix"
    assert git(desk.wt / "x-fix", "rev-parse", "--short=8", "HEAD") == desk.base
    assert desk.calls.read_text().splitlines() == [str(desk.wt / "x-fix")]


def test_an_existing_worktree_on_the_branch_is_reused_not_re_cut(desk):
    git(desk.repo, "worktree", "add", "-q", "-b", "ops/x-fix", str(desk.wt / "x-fix"), desk.base)
    done = desk.launch("devfix", str(desk.card))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [f"cd {desk.wt / 'x-fix'}", desk.filled(STANDIN_LINE)]


def test_the_trees_devfix_hub_line_is_printed_with_its_tokens_filled(tmp_path):
    """F1 through F2: the fixed file's ONE line, its tokens filled, every path under a root."""
    text = (HUBS / "DEVFIX-HUB.md").read_text()
    lines = [ln for ln in text.splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1
    assert "«INSTALL" in text  # the title token stands until his approval row
    desk = Desk(tmp_path, text.replace("«INSTALL", "INSTALLED-IN-TEST"))
    done = desk.launch("devfix", str(desk.card))
    assert done.returncode == 0, done.stderr
    out = done.stdout.splitlines()
    assert out[-1] == desk.filled(lines[0])
    assert "<" not in out[-1] and ">" not in out[-1]
    assert f"CARD: '{desk.card}'" in out[-1]
    assert "--remote-control x-fix-devfix --name x-fix-devfix" in out[-1]


# ---- the refusals: exit 1, the REFUSED text, nothing run -----------------------------------


@pytest.mark.parametrize(
    "bad",
    ["x_table", "public.x_table", "user.", "user.X_table", "user.x-table", "user.x;drop",
     "system.x table", "user.x.y", "users.x_table", "user.x_tablé"],
)
def test_a_table_outside_system_or_user_names_is_refused(desk, bad):
    desk.write_card(TABLE=bad)
    desk.commit("card")
    refused(desk.launch("devfix", str(desk.card)),
            f"incomplete card: TABLE '{bad}' is not system.<name> or user.<name> with <name> in [a-z0-9_]")


@pytest.mark.parametrize(
    "bad",
    ["tests/ops/test_x.py", "tests/cobalt/test_x.txt", "tests/cobalt/sub/test_x.py",
     "tests/cobalt/../test_x.py", "tests/cobalt/.py", "tests/cobalt/test_x.py::a b",
     "tests/cobalt/test_x.py::a$b", "tests/cobalt/test_x.py::", "/tmp/tests/cobalt/test_x.py",
     "tests/cobalt/test_x.py::a|b", "tests/cobalt/test_é.py", "tests/cobalt/test_x.py::test_é"],
)
def test_a_proof_test_outside_tests_cobalt_is_refused(desk, bad):
    desk.write_card(**{"PROOF TEST": bad})
    desk.commit("card")
    refused(desk.launch("devfix", str(desk.card)),
            f"incomplete card: PROOF TEST '{bad}' is not tests/cobalt/<file>.py with an optional ::<name> in [A-Za-z0-9_:.]")


@pytest.mark.parametrize("good", ["tests/cobalt/test_x.py", "tests/cobalt/test_x.py::TestX::test_y.z"])
def test_a_proof_test_file_alone_or_with_a_dotted_name_passes(desk, good):
    """Negative control for the PROOF TEST refusal."""
    desk.write_card(**{"PROOF TEST": good})
    desk.commit("card")
    done = desk.launch("devfix", str(desk.card))
    assert done.returncode == 0, done.stderr
    assert f"PROOF: {good}" in done.stdout


@pytest.mark.parametrize("key", ["TABLE", "PROOF TEST", "BASE", "REPORT", "RULINGS"])
def test_a_missing_key_is_refused(desk, key):
    desk.write_card(**{key: None})
    desk.commit("card")
    refused(desk.launch("devfix", str(desk.card)), f"incomplete card: '{key}' is empty")


def test_a_report_outside_reports_devfix_is_refused(desk):
    for bad in (desk.reports / "x-fix-2026-01-02.md",
                desk.wt / "x-fix" / "docs" / "40 - DevDocs" / "reports" / "devfix-x.md",
                desk.reports / "devfix-x.txt"):
        desk.write_card(REPORT=str(bad))
        desk.commit("card")
        refused(desk.launch("devfix", str(desk.card)),
                f"incomplete card: a devfix REPORT must be {desk.reports}/devfix-<name>.md")


def test_a_report_name_outside_its_spelled_set_is_refused(desk):
    bad = desk.reports / "devfix-x_tablé.md"
    desk.write_card(REPORT=str(bad))
    desk.commit("card")
    refused(desk.launch("devfix", str(desk.card)),
            f"incomplete card: a devfix REPORT must be {desk.reports}/devfix-<name>.md")


def test_a_report_already_present_is_refused_on_a_first_launch(desk):
    (desk.reports / "devfix-x-fix-2026-01-02.md").write_text("(run in progress)\n")
    refused(desk.launch("devfix", str(desk.card)), "the devfix report already exists")


def test_a_held_lock_is_refused(desk):
    (desk.wt / "beta" / ".env").write_text(CONSTRUCTED_ENV)
    refused(desk.launch("devfix", str(desk.card)), "with-DB launch refused: the cobalt_dev lock is held")
    (desk.wt / "beta" / ".env").unlink()
    (desk.wt / LOCK_NAME).mkdir()
    (desk.wt / LOCK_NAME / "owner").write_text("beta\n")
    refused(desk.launch("devfix", str(desk.card)),
            "with-DB launch refused: the cobalt_dev lock is held by beta")
    assert not (desk.wt / "x-fix").exists()


def test_a_card_uncommitted_or_changed_is_refused(desk):
    desk.write_card(TABLE="user.y_table")
    refused(desk.launch("devfix", str(desk.card)), f"the card differs from its commit: {desk.card}")
    new = desk.prompts / "2026-01-02" / "02-y-fix-card.md"
    new.write_text(card_text(desk.base, desk.reports))
    refused(desk.launch("devfix", str(new)), f"the card is not committed on main: {new}")


def test_a_fixed_file_changed_since_its_commit_is_refused(desk):
    hub = desk.prompts / "DEVFIX-HUB.md"
    hub.write_text(hub.read_text() + "\nedited\n")
    refused(desk.launch("devfix", str(desk.card)), f"the fixed file differs from its commit: {hub}")


def test_a_fixed_file_still_carrying_its_install_token_is_refused(desk):
    hub = desk.prompts / "DEVFIX-HUB.md"
    hub.write_text("# DEVFIX-HUB («INSTALL: <date> R<n>)\n\n" + STANDIN_LINE + "\n")
    desk.commit("hub")
    refused(desk.launch("devfix", str(desk.card)), "the fixed file still carries its «INSTALL token")


def test_a_worktree_on_another_branch_is_refused(desk):
    git(desk.repo, "worktree", "add", "-q", "-b", "other", str(desk.wt / "x-fix"), desk.base)
    refused(desk.launch("devfix", str(desk.card)),
            f"{desk.wt / 'x-fix'} is on 'other', the card says 'ops/x-fix'")


def test_a_base_not_on_main_is_refused(desk):
    git(desk.repo, "checkout", "-q", "-b", "side")
    (desk.repo / "side.txt").write_text("side\n")
    desk.commit("side")
    side = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    git(desk.repo, "checkout", "-q", "main")
    desk.write_card(BASE=side)
    desk.commit("card")
    refused(desk.launch("devfix", str(desk.card)), f"BASE '{side}' is not a commit on main")


def test_a_base_not_8_hex_is_refused(desk):
    desk.write_card(BASE="main")
    desk.commit("card")
    refused(desk.launch("devfix", str(desk.card)), "incomplete card: BASE 'main' is not 8 hex characters")


# ---- a resume step, as build -----------------------------------------------------------------


def test_a_resume_skips_its_own_lock_and_prefixes_continue(desk):
    git(desk.repo, "worktree", "add", "-q", "-b", "ops/x-fix", str(desk.wt / "x-fix"), desk.base)
    (desk.wt / LOCK_NAME).mkdir()
    (desk.wt / LOCK_NAME / "owner").write_text("x-fix\n")
    (desk.wt / "x-fix" / ".env").write_text(CONSTRUCTED_ENV)
    (desk.reports / "devfix-x-fix-2026-01-02.md").write_text("FAILED: STEP 3 — x\n")
    done = desk.launch("devfix", str(desk.card), "STEP 3")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [
        f"cd {desk.wt / 'x-fix'}",
        desk.filled(STANDIN_LINE).replace('claude --bg "Read ', 'claude --bg "CONTINUE: STEP 3. Read ', 1),
    ]


def test_a_resume_still_refuses_another_worktrees_lock(desk):
    (desk.wt / "beta" / ".env").write_text(CONSTRUCTED_ENV)
    refused(desk.launch("devfix", str(desk.card), "STEP 3"),
            "with-DB launch refused: the cobalt_dev lock is held")


# ---- the other kinds print as at BASE ------------------------------------------------------


def test_build_still_prints_its_add_cd_and_line(desk):
    card = desk.prompts / "2026-01-02" / "03-x-job-card.md"
    report = desk.wt / "x-job" / "docs" / "40 - DevDocs" / "reports" / "x-job-build.md"
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {desk.base}\nTIP:\nREPORT: {report}\nTREE STATE: unchanged\n"
        "RULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
    )
    desk.commit("build card")
    line = next(ln for ln in (HUBS / "BUILD-HUB.md").read_text().splitlines()
                if ln.startswith("claude --bg "))
    done = desk.launch("build", str(card))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [
        f"git -C {desk.repo} worktree add -b ops/x-job {desk.wt / 'x-job'} {desk.base}",
        f"cd {desk.wt / 'x-job'}",
        line.replace("<card>", str(card)).replace("<job>", "x-job").replace("<worktree>", "x-job"),
    ]


def test_prompt_still_prints_its_cd_and_line(desk):
    pfile = desk.prompts / "2026-01-02" / "04-x-prompt.md"
    line = (
        f"claude --bg \"Read '{pfile}' and follow it exactly.\" --model claude-opus-5-5 "
        "--permission-mode auto --remote-control x-prompt --name x-prompt --allowedTools \"Read\" "
        "--disallowedTools \"AskUserQuestion\" \"EnterWorktree\" --add-dir /Users/cobalt/cobalt"
    )
    # the prompt kind reads its cwd only as a `cd /Users/cobalt/…` string; the dry run prints it
    # and enters nothing, so the cwd root here is the real path name
    pfile.write_text(f"`cd /Users/cobalt/cobalt-wt/x-prompt-wt`\n\n{line}\n")
    desk.commit("prompt")
    done = subprocess.run(
        ["sh", str(LAUNCH), "prompt", str(pfile)],
        env=dict(desk.env, COBALT_WT_ROOT="/Users/cobalt/cobalt-wt", DESK_LAUNCH_DRY="1"),
        capture_output=True, text=True, timeout=120,
    )
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == ["cd /Users/cobalt/cobalt-wt/x-prompt-wt", line]


def test_an_unknown_kind_names_devfix_among_the_kinds(desk):
    refused(desk.launch("nokind", str(desk.card)),
            "kind 'nokind' is none of build, check, deploy, devfix, recut, desk, prompt, close, install-ops")
