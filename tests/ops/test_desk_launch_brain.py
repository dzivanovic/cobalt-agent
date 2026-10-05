"""desk-launch.sh brain "<handover>": the standing brain seat on BRAIN-HUB.md (card 07 brain-hub, B2).

Every run copies ops/desk/desk-launch.sh into tmp_path/ops/ beside two stubs: desk-context.sh
(the desk-size guard, passing unless a test makes it refuse) and desk-list.sh (LIST rows
`id · name · cwd · status · state`). COBALT_REPO_ROOT points the script at a tmp repo whose
BRAIN-HUB.md is a constructed one-line fixed file; one test runs the tree's own BRAIN-HUB.md
(B1) through the same script. `claude` is a stub on PATH that records its cwd and arguments.
Nothing here reads a real session list, a real handover or a real database.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
FILL = "«FILL"  # the fill token, built so this file never spells it
INSTALL = "«INSTALL"
# `07b` P5 (his 10-04 R189): the brain's line defaults to Opus; `--fable` puts Fable on it instead
OPUS = "--model claude-opus-5-5"
FABLE = "--model claude-fable-5-1"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

# a constructed fixed file: its one line carries the one token `brain` fills
STANDIN_LINE = (
    "claude --bg \"Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BRAIN-HUB.md' and "
    "follow it exactly. HANDOVER: '<handover>'\" --model claude-opus-5-5 --permission-mode auto "
    "--remote-control brain --name brain --allowedTools \"Read\" "
    "\"Bash(git -C /Users/cobalt/cobalt log*)\" --disallowedTools \"AskUserQuestion\" "
    "\"EnterWorktree\" \"Bash(git push*)\" --add-dir /Users/cobalt/cobalt"
)

# constructed LIST ids
DESK = "d35c0001"
BRAIN = "b2a10001"
BUILDER = "b0110001"


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
    def __init__(self, tmp_path: Path, hub_text: str):
        self.tmp = tmp_path
        self.repo = tmp_path / "repo"
        self.wt = tmp_path / "wt"
        self.wt.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        self.hub = self.prompts / "BRAIN-HUB.md"
        self.hub.write_text(hub_text)
        self.handover = self.prompts / "2026-01-02" / "08-brain-handover.md"
        self.handover.write_text("SEAT: brain (constructed handover)\nFIRST REPLY: three sentences.\n")
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "base")

        ops = tmp_path / "ops"
        ops.mkdir()
        self.launch = ops / "desk-launch.sh"
        shutil.copy(LAUNCH, self.launch)
        self.guard(refuse=False)
        self.live([(DESK, "cto-desk")])
        self.calls = tmp_path / "claude-calls"
        write_exe(tmp_path / "bin" / "claude",
                  f'printf "%s | %s\\n" "$PWD" "$*" >> "{self.calls}"\nexit 0\n')
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}", **GIT_ENV,
        )

    def guard(self, refuse: bool) -> None:
        body = 'echo "REFUSED: desk at 300000 tokens — REFRESH first"\nexit 3\n' if refuse else "exit 0\n"
        write_exe(self.launch.parent / "desk-context.sh", body)

    def live(self, rows: list[tuple[str, str]], status: int = 0) -> None:
        """The desk-list.sh stub beside the copy: one LIST row per (id, name)."""
        out = "".join(f"printf '%s\\n' '{i} · {n} · ~/cobalt · idle · working'\n" for i, n in rows)
        write_exe(self.launch.parent / "desk-list.sh", f"{out}exit {status}\n")

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def launch_run(self, *args: str, dry: bool = True) -> subprocess.CompletedProcess:
        env = dict(self.env, DESK_LAUNCH_DRY="1") if dry else self.env
        return subprocess.run(
            ["sh", str(self.launch), *args], env=env, cwd=self.tmp,
            capture_output=True, text=True, timeout=120,
        )

    def filled(self, line: str, handover: Path | None = None) -> str:
        return line.replace("<handover>", str(handover or self.handover))


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path, "# BRAIN-HUB (constructed, installed)\n\n" + STANDIN_LINE + "\n")


def refused(done: subprocess.CompletedProcess, text: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert done.stdout == ""


# ---- the good case -------------------------------------------------------------------------


def test_a_good_handover_prints_the_cd_and_the_filled_line(desk):
    done = desk.launch_run("brain", str(desk.handover))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [f"cd {desk.repo}", desk.filled(STANDIN_LINE)]
    assert not desk.calls.exists()


def test_a_good_handover_runs_the_line_from_the_repo(desk):
    done = desk.launch_run("brain", str(desk.handover), dry=False)
    assert done.returncode == 0, done.stderr
    calls = desk.calls.read_text().splitlines()
    assert len(calls) == 1
    cwd, args = calls[0].split(" | ", 1)
    assert Path(cwd).resolve() == desk.repo.resolve()
    assert args.startswith("--bg Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BRAIN-HUB.md'")
    assert f"HANDOVER: '{desk.handover}'" in args
    assert "--remote-control brain --name brain" in args


def test_other_live_sessions_do_not_block_a_brain(desk):
    """Negative control: a live desk, a build whose name starts with brain, a judge — no `brain`."""
    desk.live([(DESK, "cto-desk"), (BUILDER, "brain-hub-build"), ("j0d90001", "judge"),
               ("b2a10002", "brainy")])
    done = desk.launch_run("brain", str(desk.handover))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == desk.filled(STANDIN_LINE)


# ---- a live brain: never a second one (his 2026-09-30 R76) ---------------------------------


@pytest.mark.parametrize("dry", [True, False])
def test_a_live_brain_is_refused_and_nothing_runs(desk, dry):
    desk.live([(DESK, "cto-desk"), (BRAIN, "brain")])
    done = desk.launch_run("brain", str(desk.handover), dry=dry)
    refused(done, f"a session named brain is live ({BRAIN})")
    assert "2026-09-30 R76" in done.stderr
    assert not desk.calls.exists()


@pytest.mark.parametrize("case", ["list fails", "list missing"])
def test_an_unreadable_session_list_is_refused(desk, case):
    """Fail closed: a brain never launches beside a brain it cannot rule out."""
    if case == "list fails":
        desk.live([], status=1)
    else:
        (desk.launch.parent / "desk-list.sh").unlink()
    done = desk.launch_run("brain", str(desk.handover), dry=False)
    refused(done, "the session list is unreadable")
    assert not desk.calls.exists()


# ---- the handover: a dated prompts folder, no fill token -----------------------------------


def test_a_handover_holding_the_fill_token_is_refused(desk):
    desk.handover.write_text(f"SEAT: brain\nSTATE: {FILL} at handover\n")
    done = desk.launch_run("brain", str(desk.handover))
    refused(done, "the handover still holds a fill token")


@pytest.mark.parametrize("where", [
    "reports/08-brain-handover.md",
    "08-brain-handover.md",                 # prompts/ itself, no date folder
    "notadate/08-brain-handover.md",
    "2026-1-02/08-brain-handover.md",
    "2026-01-02/sub/08-brain-handover.md",  # one folder deeper
    "2026-01-02/08-brain-handover.txt",
    "../outside/08-brain-handover.md",
])
def test_a_handover_outside_a_dated_prompts_folder_is_refused(desk, where):
    if where.startswith("reports/"):
        path = desk.reports / where.split("/", 1)[1]
    else:
        path = desk.prompts / where
    if ".." not in where:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("SEAT: brain\n")
    done = desk.launch_run("brain", str(path), dry=False)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr and "handover" in done.stderr, done.stderr
    assert not desk.calls.exists()


def test_a_handover_path_with_a_quote_is_refused(desk):
    path = desk.prompts / "2026-01-02" / "08-brain'x.md"
    path.write_text("SEAT: brain\n")
    done = desk.launch_run("brain", str(path))
    refused(done, "the handover path holds a character outside")


def test_a_missing_handover_is_refused(desk):
    done = desk.launch_run("brain", str(desk.prompts / "2026-01-02" / "09-brain-handover.md"))
    refused(done, "no such handover")


@pytest.mark.parametrize("args", [[], ["a", "b"]])
def test_the_usage_is_one_handover(desk, args):
    done = desk.launch_run("brain", *args)
    refused(done, "usage: desk-launch.sh brain <absolute handover path>")


# ---- the fixed file -------------------------------------------------------------------------


def test_a_hub_still_carrying_its_install_token_is_refused(desk):
    desk.hub.write_text(f"# BRAIN-HUB ({INSTALL})\n\n{STANDIN_LINE}\n")
    desk.commit("token")
    done = desk.launch_run("brain", str(desk.handover))
    refused(done, "the fixed file still carries its")


def test_an_uncommitted_hub_change_is_refused(desk):
    desk.hub.write_text("# BRAIN-HUB (changed)\n\n" + STANDIN_LINE.replace("auto", "plan") + "\n")
    done = desk.launch_run("brain", str(desk.handover))
    refused(done, "the fixed file differs from its commit")


def test_a_hub_line_that_does_not_name_the_brain_seat_is_refused(desk):
    desk.hub.write_text("# BRAIN-HUB\n\n" + STANDIN_LINE.replace("--name brain", "--name other") + "\n")
    desk.commit("other name")
    done = desk.launch_run("brain", str(desk.handover))
    refused(done, "the brain line does not name the seat brain")


def test_the_desk_size_guard_runs_first(desk):
    desk.guard(refuse=True)
    done = desk.launch_run("brain", str(desk.handover), dry=False)
    assert (done.returncode, done.stdout) == (3, "REFUSED: desk at 300000 tokens — REFRESH first\n")
    assert not desk.calls.exists()


# ---- B1 through B2: the tree's own BRAIN-HUB.md ----------------------------------------------


def launch_line(text: str) -> str:
    own = [ln for ln in text.splitlines() if ln.startswith("claude --bg ")]
    if own:
        return own[0]
    return re.search(r"`(claude --bg \"Read [^`]*)`", text).group(1)


def test_the_trees_brain_hub_line_is_printed_with_its_handover_filled(tmp_path):
    text = (HUBS / "BRAIN-HUB.md").read_text()
    lines = [ln for ln in text.splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1
    assert INSTALL not in text  # filled on his approval row (R358)
    desk = Desk(tmp_path, text.replace(INSTALL, "INSTALLED-IN-TEST"))
    done = desk.launch_run("brain", str(desk.handover))
    assert done.returncode == 0, done.stderr
    out = done.stdout.splitlines()
    assert out == [f"cd {desk.repo}", desk.filled(lines[0])]
    assert "<" not in out[-1] and ">" not in out[-1]
    assert "--model claude-opus-5-5 --permission-mode auto --remote-control brain --name brain" in out[-1]


def test_the_trees_brain_hub_allow_list_is_23s_byte_for_byte_but_the_write_pair():
    """NOT IN THIS JOB: the brain's allow list is `23`'s line, no string added or dropped; B4
    replaces `23`'s bare `"Write" "Edit"` by the two scoped Edit strings, in the same place.
    `07b` P5: the model word is the one variable — `23`'s Fable, the hub's Opus default."""
    hub = launch_line((HUBS / "BRAIN-HUB.md").read_text())
    judge = launch_line((HUBS / "2026-10-02" / "23-brain-judge.md").read_text())
    assert hub[hub.index(" --model "):hub.index(" --allowedTools ")] == \
        judge[judge.index(" --model "):judge.index(" --allowedTools ")].replace(FABLE, OPUS)
    allow = judge[judge.index(" --allowedTools "):]
    assert allow.count(f" {BARE_PAIR} ") == 1
    assert hub[hub.index(" --allowedTools "):] == allow.replace(f" {BARE_PAIR} ", f" {SCOPED_PAIR} ")


# ---- B4: the brain's write strings, scoped -------------------------------------------------

# the two scoped strings of B4 (an Edit rule governs Write on the same glob, BUILD-HUB.md line 14)
SCOPED_PAIR = (
    '"Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)" '
    '"Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/prompts/20*/**)"'
)
BARE_PAIR = '"Write" "Edit"'


def assert_writes_scoped(line: str) -> None:
    assert SCOPED_PAIR in line, line
    assert ' "Write"' not in line, line
    assert ' "Edit"' not in line, line


def test_the_trees_brain_line_holds_the_scoped_pair_and_no_bare_write_or_edit(tmp_path):
    text = (HUBS / "BRAIN-HUB.md").read_text()
    desk = Desk(tmp_path, text.replace(INSTALL, "INSTALLED-IN-TEST"))
    done = desk.launch_run("brain", str(desk.handover))
    assert done.returncode == 0, done.stderr
    assert_writes_scoped(done.stdout.splitlines()[-1])


def test_o1_a_brain_line_through_the_prompt_kind_is_refused_beside_a_live_brain(tmp_path):
    """Check O1: the prompt kind is a second road to the brain seat, beside a live brain (R76)."""
    desk = Desk(tmp_path, "# BRAIN-HUB (constructed, installed)\n\n" + STANDIN_LINE + "\n")
    # the prompt kind reads its cwd only under /Users/cobalt/: point those roots at tmp_path
    text = desk.launch.read_text()
    desk.launch.write_text(text.replace("\\/Users\\/cobalt\\/", str(tmp_path).replace("/", "\\/") + "\\/"))
    prompt = desk.prompts / "2026-01-02" / "09-brain-prompt.md"
    prompt.write_text(
        f"cd {desk.repo}\n\nclaude --bg \"Read '{prompt}' and follow it exactly.\" "
        "--model claude-fable-5-1 --permission-mode auto --remote-control brain --name brain "
        "--allowedTools \"Read\" --disallowedTools \"AskUserQuestion\" \"EnterWorktree\" "
        "\"Bash(git push*)\"\n")
    desk.commit("a brain prompt")
    desk.live([(DESK, "cto-desk"), (BRAIN, "brain")])
    done = desk.launch_run("prompt", str(prompt))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr and "brain" in done.stderr, done.stderr


# ---- B5: the prompt kind refuses a brain line (check O1 route (a), one path, L3) ---------------

BRAIN_SEAT_REFUSAL = "a brain seat launches by desk-launch.sh brain <handover>"


def prompt_world(tmp_path: Path, seat: str, dry: bool = True) -> tuple[Desk, subprocess.CompletedProcess]:
    """A committed one-off prompt whose line carries `seat`, launched by the prompt kind; no live brain."""
    desk = Desk(tmp_path, "# BRAIN-HUB (constructed, installed)\n\n" + STANDIN_LINE + "\n")
    # the prompt kind reads its cwd only under /Users/cobalt/: point those roots at tmp_path
    text = desk.launch.read_text()
    desk.launch.write_text(text.replace("\\/Users\\/cobalt\\/", str(tmp_path).replace("/", "\\/") + "\\/"))
    prompt = desk.prompts / "2026-01-02" / "09-seat-prompt.md"
    prompt.write_text(
        f"cd {desk.repo}\n\nclaude --bg \"Read '{prompt}' and follow it exactly.\" "
        f"--model claude-fable-5-1 --permission-mode auto {seat} "
        "--allowedTools \"Read\" --disallowedTools \"AskUserQuestion\" \"EnterWorktree\" "
        "\"Bash(git push*)\"\n")
    desk.commit("a seat prompt")
    return desk, desk.launch_run("prompt", str(prompt), dry=dry)


@pytest.mark.parametrize("seat", [
    "--remote-control brain --name helper",
    "--remote-control helper --name brain",
    "--remote-control brain --name brain",
])
@pytest.mark.parametrize("dry", [True, False])
def test_b5_a_prompt_line_naming_the_brain_seat_is_refused_before_anything_runs(tmp_path, seat, dry):
    desk, done = prompt_world(tmp_path, seat, dry=dry)
    refused(done, BRAIN_SEAT_REFUSAL)
    assert not desk.calls.exists()


@pytest.mark.parametrize("seat", [
    "--remote-control brain-survey --name brain-survey",
    "--remote-control brainy --name helper",
])
def test_b5_a_prompt_line_on_another_seat_still_launches(tmp_path, seat):
    """Negative control: only the exact seat name `brain` is refused."""
    _, done = prompt_world(tmp_path, seat)
    assert done.returncode == 0, done.stderr
    assert seat in done.stdout.splitlines()[-1]


@pytest.mark.parametrize("seat", [
    '--remote-control "brain" --name "brain"',
    "--remote-control helper --name 'brain'",
    "--remote-control  brain --name helper",
])
def test_check_o1_a_quoted_or_spaced_brain_seat_is_refused_too(tmp_path, seat):
    """Check r2 O1: the shell strips the quotes and the extra blank at eval; the seat is `brain`."""
    desk, done = prompt_world(tmp_path, seat, dry=False)
    refused(done, BRAIN_SEAT_REFUSAL)
    assert not desk.calls.exists()


def test_a_hub_with_the_bare_pair_fails_the_scope_check(tmp_path):
    """Negative control: the check above is red on a hub line that carries `23`'s bare pair."""
    text = (HUBS / "BRAIN-HUB.md").read_text().replace(INSTALL, "INSTALLED-IN-TEST")
    desk = Desk(tmp_path, text.replace(f" {SCOPED_PAIR} ", f" {BARE_PAIR} "))
    done = desk.launch_run("brain", str(desk.handover))
    assert done.returncode == 0, done.stderr
    line = done.stdout.splitlines()[-1]
    assert f" {BARE_PAIR} " in line
    with pytest.raises(AssertionError):
        assert_writes_scoped(line)


# ---- 07b P5: the brain's model — Opus by default, `--fable` on the brain's own ask -------------


def test_p5_the_default_line_holds_opus(desk):
    done = desk.launch_run("brain", str(desk.handover))
    assert done.returncode == 0, done.stderr
    line = done.stdout.splitlines()[-1]
    assert f" {OPUS} " in line and "claude-fable-5-1" not in line, line


@pytest.mark.parametrize("dry", [True, False])
def test_p5_fable_puts_fable_on_the_line_instead(desk, dry):
    done = desk.launch_run("brain", str(desk.handover), "--fable", dry=dry)
    assert done.returncode == 0, done.stderr
    if dry:
        assert done.stdout.splitlines() == [
            f"cd {desk.repo}", desk.filled(STANDIN_LINE).replace(OPUS, FABLE)]
        return
    calls = desk.calls.read_text().splitlines()
    assert len(calls) == 1
    args = calls[0].split(" | ", 1)[1]
    assert f" {FABLE} " in args and "claude-opus-5-5" not in args, args


@pytest.mark.parametrize("value", [
    "--opus", "fable", "--Fable", "--fable=1", "--model", "claude-fable-5-1", "-f", "",
])
@pytest.mark.parametrize("dry", [True, False])
def test_p5_any_other_value_is_refused(desk, value, dry):
    done = desk.launch_run("brain", str(desk.handover), value, dry=dry)
    refused(done, "usage: desk-launch.sh brain <absolute handover path> [--fable]")
    assert not desk.calls.exists()


def test_p5_a_flag_after_fable_is_refused(desk):
    done = desk.launch_run("brain", str(desk.handover), "--fable", "--fable")
    refused(done, "usage: desk-launch.sh brain <absolute handover path> [--fable]")


@pytest.mark.parametrize("hub_line", [
    STANDIN_LINE.replace(OPUS, FABLE),                                   # no Opus word
    STANDIN_LINE.replace("--permission-mode", f"{OPUS} --permission-mode"),  # the Opus word twice
], ids=["no-opus", "opus-twice"])
@pytest.mark.parametrize("flag", [[], ["--fable"]])
def test_p5_a_hub_line_that_does_not_default_to_opus_is_refused(desk, flag, hub_line):
    """`--fable` replaces the Opus word; a line without exactly one Opus word is refused, never
    launched on whatever model it names."""
    desk.hub.write_text("# BRAIN-HUB\n\n" + hub_line + "\n")
    desk.commit("fable default")
    done = desk.launch_run("brain", str(desk.handover), *flag)
    refused(done, f"the brain line does not default to {OPUS}")


def test_p5_the_trees_hub_line_takes_fable_on_the_flag(tmp_path):
    text = (HUBS / "BRAIN-HUB.md").read_text()
    desk = Desk(tmp_path, text.replace(INSTALL, "INSTALLED-IN-TEST"))
    done = desk.launch_run("brain", str(desk.handover), "--fable")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == desk.filled(launch_line(text)).replace(OPUS, FABLE)


def section(text: str, head: str) -> str:
    body = text.split(f"\n{head}\n", 1)[1]
    return body.split("\n## ", 1)[0]


def test_p5_the_hubs_measure_asks_the_desk_for_a_successor_and_names_its_model():
    """His 10-04 R188, R189, R191: at 500,000 the brain messages `cto-desk` for its own
    replacement, naming the next seat's model; it measures every ten answers."""
    text = (HUBS / "BRAIN-HUB.md").read_text()
    measure = section(text, "## MEASURE")
    assert "every ten answers" in measure
    assert "500,000" in measure
    assert "MESSAGE `cto-desk`" in measure and "replacement" in measure
    assert "`--fable`" in measure and "design task is open" in measure
    assert "MODEL: Opus 5.5 (`claude-opus-5-5`)" in text


def test_p5_the_standing_list_names_the_two_model_words_as_the_only_variable():
    text = (HUBS / "STANDING-LIST.md").read_text()
    seven = text.split("\n## 7. `BRAIN-HUB.md`", 1)[1]
    assert f"`{OPUS}`" in seven and f"`{FABLE}`" in seven
    assert "the only variable" in seven
