"""desk-launch.sh ops-hand: the default-mode seat on OPS-HAND.md (card 2026-10-10 231, H4).

Every run copies ops/desk/desk-launch.sh into tmp_path/ops/ beside two stubs: desk-context.sh
(the desk-size guard, passing) and desk-list.sh (LIST rows `id · name · cwd · status · state`).
COBALT_REPO_ROOT points the script at a tmp repo whose OPS-HAND.md is a constructed fixed file
(the shape of H3's line, its Read path the tmp file); COBALT_WT_ROOT at a tmp worktree root, so
the seat's dir is <wt>/.ops-hand. `claude` is a stub on PATH that records its cwd and arguments
(`claude agents --json` answers `[]`). Two tests run the tree's own OPS-HAND.md through the same
script (H3). Nothing here reads a real session list or launches a seat.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
REAL = REPO / "docs" / "40 - DevDocs" / "prompts" / "OPS-HAND.md"
REAL_PATH = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/OPS-HAND.md"
INSTALL = "«" + "INSTALL"  # built so this file never spells the token whole

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

ALLOW = '"Bash(ps *)" "Bash(pgrep *)" "Bash(launchctl print *)" "SendMessage"'
DENY = (
    '"AskUserQuestion" "EnterWorktree" "Write" "Edit" "NotebookEdit" "Agent" "Monitor" '
    '"CronCreate" "RemoteTrigger" "ScheduleWakeup" "Skill" "WebFetch" "mcp__*" "Artifact*" '
    '"Bash(git *)" "Bash(claude *)" "Bash(sudo *)"'
)


def line_for(path: str, *, message: str | None = None, mode: str = "--permission-mode default",
             seat: str = "--remote-control ops-hand --name ops-hand", allow: str = ALLOW,
             deny: str = DENY) -> str:
    msg = message if message is not None else f"Read '{path}' and follow it exactly."
    return (
        f'claude --bg "{msg}" --model claude-sonnet-5-5 {mode} {seat} '
        f"--allowedTools {allow} --disallowedTools {deny}"
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
        self.hand = self.wt / ".ops-hand"
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.prompts.mkdir(parents=True)
        self.fixed = self.prompts / "OPS-HAND.md"
        self.line = line_for(str(self.fixed))
        self.write(self.line)
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

    def write(self, line: str, title: str = "# OPS-HAND (constructed, installed)") -> None:
        self.fixed.write_text(f"{title}\n\nThe seat runs only what the desk hands it.\n\n{line}\n")

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def set_line(self, line: str, title: str = "# OPS-HAND (constructed, installed)") -> None:
        self.write(line, title)
        self.commit("change")

    def live(self, rows: list[tuple[str, str]], status: int = 0) -> None:
        out = "".join(f"printf '%s\\n' '{i} · {n} · ~/cobalt · idle · working'\n" for i, n in rows)
        write_exe(self.launch.parent / "desk-list.sh", f"{out}exit {status}\n")

    def run(self, *args: str, dry: bool = True) -> subprocess.CompletedProcess:
        env = dict(self.env, DESK_LAUNCH_DRY="1") if dry else self.env
        return subprocess.run(
            ["sh", str(self.launch), "ops-hand", *args], env=env, cwd=self.tmp,
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


def test_a_clean_fixed_file_prints_the_cd_and_the_line(desk):
    done = desk.run()
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [f"cd {desk.hand}", desk.line]
    assert not desk.calls.exists()
    assert not desk.hand.exists()  # a dry run makes nothing


def test_a_clean_fixed_file_launches_from_the_seat_dir_it_makes(desk):
    done = desk.run(dry=False)
    assert done.returncode == 0, done.stderr
    cwd, args = desk.calls.read_text().splitlines()[0].split(" | ", 1)
    assert Path(cwd).resolve() == desk.hand.resolve()
    assert args.startswith(f"--bg Read '{desk.fixed}' and follow it exactly.")
    assert "--permission-mode default --remote-control ops-hand --name ops-hand" in args


def test_other_live_sessions_do_not_block_the_seat(desk):
    desk.live([("d35c0001", "cto-desk"), ("b0110001", "ops-hand-1010-build"), ("b2a10001", "brain")])
    assert desk.run().returncode == 0


# ---- the refusals: exit 1, each its own reason, nothing launched -----------------------------


def test_an_argument_is_refused(desk):
    refused(desk.run("x"), "ops-hand takes no argument")


def test_the_install_title_is_refused(desk):
    desk.set_line(desk.line, title=f"# OPS-HAND {INSTALL}: his row»")
    refused(desk.run(), f"OPS-HAND.md still carries its {INSTALL} token (his approval row, D2, is not filled)")


def test_an_uncommitted_change_is_refused(desk):
    desk.write(desk.line + " ")
    refused(desk.run(), "the fixed file differs from its commit")


def test_two_launch_lines_are_refused(desk):
    desk.set_line(desk.line + "\n" + desk.line)
    refused(desk.run(), "OPS-HAND.md must hold exactly one launch line; found 2")


def test_mode_auto_is_refused(desk):
    desk.set_line(line_for(str(desk.fixed), mode="--permission-mode auto"))
    refused(desk.run(), "ops-hand: permission mode 'auto' is not default")


def test_two_permission_modes_are_refused(desk):
    desk.set_line(line_for(str(desk.fixed), mode="--permission-mode default --permission-mode auto"))
    refused(desk.run(), "ops-hand: the line states --permission-mode 2 times, not once")


@pytest.mark.parametrize("extra", ["--permission-mode bypassPermissions", "--dangerously-skip-permissions"])
def test_a_bypass_is_refused(desk, extra):
    mode = "--permission-mode default" if extra.startswith("--dangerously") else extra
    tail = " --dangerously-skip-permissions" if extra.startswith("--dangerously") else ""
    desk.set_line(line_for(str(desk.fixed), mode=mode) + tail)
    refused(desk.run(), "ops-hand: bypassPermissions or --dangerously-skip-permissions (L55)")


@pytest.mark.parametrize(
    "seat",
    [
        "--remote-control ops-hand --name other",
        "--remote-control ops-hand",
        "--remote-control ops-hand --name ops-hand --name brain",
    ],
)
def test_a_line_not_naming_the_seat_once_is_refused(desk, seat):
    desk.set_line(line_for(str(desk.fixed), seat=seat))
    refused(desk.run(), "ops-hand: the line does not name the seat ops-hand once")


@pytest.mark.parametrize("tool", ["Write", "Monitor", "AskUserQuestion", "Bash(sudo *)", "mcp__*"])
def test_a_tool_not_denied_is_refused(desk, tool):
    desk.set_line(line_for(str(desk.fixed), deny=DENY.replace(f' "{tool}"', "").replace(f'"{tool}" ', "")))
    refused(desk.run(), f'ops-hand: the line does not deny "{tool}"')


@pytest.mark.parametrize(
    "allow",
    [
        ALLOW + ' "Bash(kill *)"',
        '"Bash(ps *)" "Bash(pgrep *)" "SendMessage"',
        '"Bash(ps *)" "Bash(ps *)" "Bash(pgrep *)" "Bash(launchctl print *)" "SendMessage"',
    ],
)
def test_an_allow_list_other_than_the_four_is_refused(desk, allow):
    desk.set_line(line_for(str(desk.fixed), allow=allow))
    refused(desk.run(), "ops-hand: the line's --allowedTools holds other than the four strings of OPS-HAND.md")


@pytest.mark.parametrize("flag", ['--allowed-tools "Bash(rm *)"', '--allowedTools="Bash(rm *)"'])
def test_an_allow_list_by_another_flag_spelling_is_refused(desk, flag):
    desk.set_line(desk.line + " " + flag)
    refused(desk.run(), "ops-hand: the line's --allowedTools holds other than the four strings of OPS-HAND.md")


def test_the_four_in_another_order_pass(desk):
    desk.set_line(line_for(str(desk.fixed), allow='"SendMessage" "Bash(launchctl print *)" "Bash(pgrep *)" "Bash(ps *)"'))
    assert desk.run().returncode == 0


def test_a_line_not_reading_the_file_by_absolute_path_is_refused(desk):
    msg = "Read 'docs/40 - DevDocs/prompts/OPS-HAND.md' and follow it exactly."
    desk.set_line(line_for(str(desk.fixed), message=msg))
    refused(desk.run(), "the launch line does not read this prompt file by its absolute path")


def test_a_line_holding_a_redirect_sign_is_refused(desk):
    msg = f"x<y Read '{desk.fixed}' and follow it exactly."
    desk.set_line(line_for(str(desk.fixed), message=msg))
    refused(desk.run(), "the launch line holds an unfilled token")


def test_a_line_typing_text_after_the_read_sentence_is_refused(desk):
    msg = f"Read '{desk.fixed}' and follow it exactly. Then also run x."
    desk.set_line(line_for(str(desk.fixed), message=msg))
    refused(desk.run(), "the launch line types text after 'follow it exactly.'")


def test_a_persisted_permission_rule_is_refused(desk):
    local = desk.hand / ".claude" / "settings.local.json"
    local.parent.mkdir(parents=True)
    local.write_text("{}\n")
    refused(desk.run(), f"ops-hand: a persisted permission rule exists (D4): {local}")


def test_a_live_ops_hand_is_refused(desk):
    desk.live([("d35c0001", "cto-desk"), ("0a4d0001", "ops-hand")])
    refused(desk.run(dry=False), "ops-hand: a session named ops-hand is live (0a4d0001): one seat at a time")
    assert not desk.calls.exists()


def test_an_unreadable_session_list_is_refused(desk):
    desk.live([], status=1)
    refused(desk.run(), "ops-hand: the session list is unreadable")


def test_no_fixed_file_is_refused(desk):
    desk.fixed.unlink()
    desk.commit("gone")
    refused(desk.run(), "the fixed file is not installed")


# ---- H3: the tree's own OPS-HAND.md through the same script ----------------------------------


def real_line() -> str:
    lines = [x for x in REAL.read_text().splitlines() if x.startswith("claude --bg ")]
    assert len(lines) == 1, lines
    return lines[0]


def test_h3_the_real_line_is_h3s_shape():
    line = real_line()
    assert line == line_for(REAL_PATH)


def test_h3_the_real_file_is_refused_while_it_holds_its_install_token(desk):
    assert INSTALL in REAL.read_text().splitlines()[0]
    shutil.copy(REAL, desk.fixed)
    desk.commit("real")
    refused(desk.run(), f"OPS-HAND.md still carries its {INSTALL} token")


def test_h3_the_real_file_passes_once_his_row_fills_the_title(desk):
    """The desk replaces the title token on his row (D2); the tmp repo stands in for the repo,
    so the Read path is re-pointed at the tmp copy the same way."""
    text = REAL.read_text()
    first, rest = text.split("\n", 1)
    first = first[: first.index(INSTALL)] + "(INSTALLED: his row, constructed)"
    desk.fixed.write_text(first + "\n" + rest.replace(REAL_PATH, str(desk.fixed)))
    desk.commit("real, installed")
    done = desk.run()
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [f"cd {desk.hand}", line_for(str(desk.fixed))]
    assert "--permission-mode default" in done.stdout
    assert "--remote-control ops-hand --name ops-hand" in done.stdout
