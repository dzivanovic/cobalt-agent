"""desk-launch.sh spike <prompt>: the scratch-dir research seat on SPIKE-HUB.md (card 2026-10-11 324, P2).

Every run copies ops/desk/desk-launch.sh into tmp_path/ops/ beside a passing desk-size guard and
a desk-list.sh stub (LIST rows `id · name · cwd · status · state`). COBALT_REPO_ROOT points it at a
tmp repo whose SPIKE-HUB.md is a constructed fixed file (prompt 330's line shape, its Read path the
tmp file, `<prompt>` its one token) and whose dated prompt is committed; COBALT_WT_ROOT at a tmp
worktree root, so the scratch dir is <wt>/sdk-spike-1010. `claude` is a stub on PATH that records
its cwd and arguments. Nothing here launches a seat.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
SIGN = "«" + "SIGN"  # built so this file never spells the mark whole

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


def line_for(hub: str, mode: str = "--permission-mode dontAsk") -> str:
    return (
        f"claude --bg \"Read '{hub}' and follow it exactly. PROMPT: '<prompt>'\" --model claude-opus-5-5 "
        f"{mode} --remote-control sdk-spike-live --name sdk-spike-live "
        '--allowedTools "Read" "Write(//Users/cobalt/cobalt-wt/sdk-spike-1010/**)" "Bash(ls *)" '
        '--disallowedTools "Bash(git *)" "AskUserQuestion" "EnterWorktree" '
        "--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt"
    )


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def write_exe(path: Path, body: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("#!/bin/sh\n" + body)
    path.chmod(0o755)
    return path


class Desk:
    def __init__(self, tmp_path: Path):
        self.tmp = tmp_path
        self.repo = tmp_path / "repo"
        self.wt = tmp_path / "wt"
        self.wt.mkdir()
        self.scratch = self.wt / "sdk-spike-1010"
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.fixed = self.prompts / "SPIKE-HUB.md"
        self.line = line_for(str(self.fixed))
        self.write(self.line)
        self.prompt = self.prompts / "2026-01-02" / "330-x-spike.md"
        self.prompt.write_text("MODEL: constructed spike prompt\n")
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")
        ops = tmp_path / "ops"
        ops.mkdir()
        self.launch = ops / "desk-launch.sh"
        shutil.copy(LAUNCH, self.launch)
        write_exe(ops / "desk-context.sh", "exit 0\n")
        self.live([("d35c0001", "cto-desk")])
        self.calls = tmp_path / "claude-calls"
        write_exe(tmp_path / "bin" / "claude",
                  'if [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
                  f'printf "%s | %s\\n" "$PWD" "$*" >> "{self.calls}"\nexit 0\n')
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}", **GIT_ENV,
        )

    def write(self, line: str, extra: str = "") -> None:
        self.fixed.write_text(f"# SPIKE-HUB (constructed, installed)\n\n{line}\n{extra}")

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def set_line(self, line: str, extra: str = "") -> None:
        self.write(line, extra)
        self.commit("change")

    def live(self, rows: list[tuple[str, str]], status: int = 0) -> None:
        out = "".join(f"printf '%s\\n' '{i} · {n} · ~/cobalt · idle · working'\n" for i, n in rows)
        write_exe(self.launch.parent / "desk-list.sh", f"{out}exit {status}\n")

    def run(self, *args: str, dry: bool = True) -> subprocess.CompletedProcess:
        env = dict(self.env, DESK_LAUNCH_DRY="1") if dry else self.env
        return subprocess.run(
            ["sh", str(self.launch), *args], env=env, cwd=self.tmp,
            capture_output=True, text=True, timeout=120,
        )


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def refused(done: subprocess.CompletedProcess, text: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert done.stdout == ""


# ---- the good case (the positive control) ---------------------------------------------------


def test_a_signed_line_prints_the_cd_and_the_line(desk):
    done = desk.run("spike", str(desk.prompt))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [f"cd {desk.scratch}", desk.line.replace("<prompt>", str(desk.prompt))]
    assert not desk.scratch.exists()  # a dry run makes nothing
    assert not desk.calls.exists()


def test_a_launch_makes_the_plain_scratch_dir_and_runs_there(desk):
    done = desk.run("spike", str(desk.prompt), dry=False)
    assert done.returncode == 0, done.stderr
    assert desk.scratch.is_dir() and not (desk.scratch / ".git").exists()
    cwd, args = desk.calls.read_text().splitlines()[0].split(" | ", 1)
    assert Path(cwd).resolve() == desk.scratch.resolve()
    assert f"PROMPT: '{desk.prompt}'" in args
    assert git(desk.repo, "worktree", "list").count("\n") == 0  # no worktree was added


# ---- the refusals: exit 1, each its own reason, nothing made, nothing launched ----------------


def test_the_sign_mark_is_refused(desk):
    desk.set_line(desk.line, extra=f"\nLINE: NEEDS HIS SIGN-OFF {SIGN}: his row»\n")
    refused(desk.run("spike", str(desk.prompt)), f"spike: SPIKE-HUB.md still holds its {SIGN} mark (his sign-off is not filled)")
    assert not desk.scratch.exists()


def test_mode_auto_is_refused(desk):
    desk.set_line(line_for(str(desk.fixed), mode="--permission-mode auto"))
    refused(desk.run("spike", str(desk.prompt)), "spike: permission mode 'auto' is not dontAsk")


def test_two_permission_modes_are_refused(desk):
    desk.set_line(line_for(str(desk.fixed), mode="--permission-mode dontAsk --permission-mode auto"))
    refused(desk.run("spike", str(desk.prompt)), "spike: the line states --permission-mode 2 times, not once")


def test_bypass_permissions_is_refused(desk):
    desk.set_line(line_for(str(desk.fixed), mode="--permission-mode bypassPermissions"))
    refused(desk.run("spike", str(desk.prompt)), "spike: bypassPermissions on the line (L55)")


def test_a_scratch_path_that_is_a_git_worktree_is_refused(desk):
    desk.scratch.mkdir()
    (desk.scratch / ".git").write_text("gitdir: /x\n")
    refused(desk.run("spike", str(desk.prompt)), f"spike: {desk.scratch} is a git worktree or holds .git")


def test_a_live_spike_session_is_refused(desk):
    desk.live([("d35c0001", "cto-desk"), ("5b1c0001", "sdk-spike-live")])
    refused(desk.run("spike", str(desk.prompt), dry=False), "spike: a session named sdk-spike-live is live (5b1c0001)")
    assert not desk.calls.exists()
    assert not desk.scratch.exists()


def test_no_argument_is_refused(desk):
    refused(desk.run("spike"), "spike takes one argument, the prompt; 0 given")


def test_two_arguments_are_refused(desk):
    refused(desk.run("spike", str(desk.prompt), "x"), "spike takes one argument, the prompt; 2 given")


def test_an_uncommitted_prompt_is_refused(desk):
    desk.prompt.write_text("MODEL: changed\n")
    refused(desk.run("spike", str(desk.prompt)), f"the prompt differs from its commit: {desk.prompt}")


def test_a_prompt_outside_a_dated_folder_is_refused(desk):
    other = desk.prompts / "x-spike.md"
    other.write_text("x\n")
    desk.commit("undated")
    refused(desk.run("spike", str(other)), "spike: a prompt lives directly under")


def test_an_uncommitted_fixed_file_is_refused(desk):
    desk.write(desk.line + " ")
    refused(desk.run("spike", str(desk.prompt)), "the fixed file differs from its commit")


# ---- negative control: the prompt kind keeps refusing dontAsk ---------------------------------


def test_the_prompt_kind_still_refuses_a_dont_ask_line(desk):
    p = desk.prompts / "2026-01-02" / "331-x-prompt.md"
    p.write_text(
        f"`cd {desk.wt}`\n"
        f"claude --bg \"Read '{p}' and follow it exactly.\" --model claude-opus-5-5 --permission-mode dontAsk "
        '--remote-control x --name x --allowedTools "Read" --disallowedTools "AskUserQuestion" "EnterWorktree"\n'
    )
    desk.commit("prompt")
    refused(desk.run("prompt", str(p)), "permission mode 'dontAsk': a one-off prompt runs auto or plan")
