"""The fixed files' launch lines (card 2026-10-03/02 adoption-hubs, rows A4 and A6).

His 2026-10-02 R39 (direction row 2): permission by class — `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`
on every line, `Bash(COBALT_ENV=dev uv run cobalt db *)` on the build, check, devfix and deploy
lines, `Bash(COBALT_ENV=production*)` denied on build, check and devfix. His R38 (direction row
1): the bare-command flag on the lines. His 2026-10-03 R3: every Grok seat runs grok-4.7.

A line is the ONE line of the fixed file beginning `claude --bg ` (desk-launch.sh reads it so),
split as the shell splits it. desk-launch.sh runs the line by `eval`, so the flag's `$(…)` is
written `\\$(…)` in the file: a dry launch prints that spelling, and a real launch with a stub
`claude` that records its arguments shows the session receives the flag byte for byte. The tmp
repo stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) and a tmp directory for
/Users/cobalt/cobalt-wt (COBALT_WT_ROOT), the shape of tests/ops/test_desk_launch_prechecks.py.
Nothing here reads a real card, report, `.env` or database.
"""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
KINDS = {"build": "BUILD-HUB.md", "check": "CHECK-HUB.md", "deploy": "DEPLOY-HUB.md", "devfix": "DEVFIX-HUB.md"}

CLASS_A = "Bash(sh /Users/cobalt/cobalt/ops/desk/*)"
CLASS_B = "Bash(COBALT_ENV=dev uv run cobalt db *)"
PROD_DENY = "Bash(COBALT_ENV=production*)"
FLAG = ("ONE bare command per Bash call: no &&, ;, |, redirect, newline or $(…) outside quotes. "
        "A call the hook blocks is NOT A REFUSAL: resend it as single calls.")
# the flag as the line spells it: desk-launch.sh evals the line, so `$` is escaped inside "…"
FLAG_SRC = '--append-system-prompt "' + FLAG.replace("$", "\\$") + '"'

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}
APPROVED_R1 = "| R1 | 07:00 ET | HIS RULING (constructed): the job may run. | HIS RULING · APPROVED |"


def hub_line(name: str) -> str:
    lines = [ln for ln in (HUBS / name).read_text(encoding="utf-8").splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1, f"{name}: {len(lines)} launch lines"
    return lines[0]


def tools(line: str, option: str) -> list[str]:
    """The strings after `--allowedTools` or `--disallowedTools`, up to the next option."""
    words = shlex.split(line)
    out, inside = [], False
    for w in words:
        if w.startswith("--"):
            inside = w == option
            continue
        if inside:
            out.append(w)
    return out


# ---- the four lines, read from this tree -----------------------------------------------------


@pytest.mark.parametrize("name", sorted(KINDS.values()))
def test_each_line_carries_the_two_class_strings_once_and_no_string_they_replace(name):
    line = hub_line(name)
    allow = tools(line, "--allowedTools")
    assert allow.count(CLASS_A) == 1, allow
    assert allow.count(CLASS_B) == 1, allow
    assert [s for s in allow if s.startswith("Bash(sh ") and s != CLASS_A] == []
    assert [s for s in allow if s.startswith("Bash(COBALT_ENV=dev uv run cobalt db") and s != CLASS_B] == []
    assert "sh /Users/cobalt/.claude/ops/" not in line


@pytest.mark.parametrize("name", ["BUILD-HUB.md", "CHECK-HUB.md", "DEVFIX-HUB.md"])
def test_build_check_and_devfix_deny_every_production_string(name):
    line = hub_line(name)
    assert tools(line, "--disallowedTools").count(PROD_DENY) == 1
    assert [s for s in tools(line, "--allowedTools") if "COBALT_ENV=production" in s] == []


@pytest.mark.parametrize("name", sorted(KINDS.values()))
def test_each_line_carries_the_flag_once(name):
    line = hub_line(name)
    assert line.count("--append-system-prompt") == 1
    assert line.count(FLAG_SRC) == 1, line


def test_the_desk_line_of_the_wakeup_carries_the_flag_once():
    (launch,) = [ln for ln in (HUBS / "CTO-DESK-WAKEUP.md").read_text(encoding="utf-8").splitlines()
                 if ln.startswith("- LAUNCH ")]
    assert launch.count("--append-system-prompt") == 1
    assert launch.count(FLAG_SRC) == 1, launch


def test_the_grok_launch_line_pins_grok_4_7_after_the_command_word():
    (grok,) = [ln for ln in (HUBS / "CHECK-HUB.md").read_text(encoding="utf-8").splitlines()
               if ln.startswith("- **GROK:** ")]
    assert grok.count("-m grok-4.7") == 1
    assert "`grok -m grok-4.7 --sandbox cobalt-job " in grok


def test_the_deploy_gate_f_names_the_rollback_a_resume_types_by_hand():
    """THE ONE RESUME runs G (f) by hand when it finds <GATE>/.env: G (f) must name what it types."""
    text = (HUBS / "DEPLOY-HUB.md").read_text(encoding="utf-8")
    step_g = text.split("\n## STEP-G ", 1)[1].split("\n## ", 1)[0]
    (f,) = [ln for ln in step_g.splitlines() if ln.startswith("- (f) ")]
    assert "the ROLLBACK command of" in f and "ops/desk/gate-lists.md" in f, f
    assert "`<FP>`" in f, f


# ---- desk-launch.sh carries the flag through, dry and real -----------------------------------


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


class Desk:
    """A tmp main repo with this tree's four fixed files, a built job branch, a job card (build
    and check), a deploy card with its committed check report, a devfix card; a stub `claude`
    that writes each argument it gets on a line of its own."""

    def __init__(self, tmp_path: Path):
        self.wt = tmp_path / "wt"
        self.repo = tmp_path / "repo"
        self.wt.mkdir()
        self.repo.mkdir()
        prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        day = prompts / "2026-01-02"
        day.mkdir(parents=True)
        reports.mkdir(parents=True)
        for name in KINDS.values():
            # DEVFIX-HUB.md is a draft until his row: its title token is stood in, nothing else
            text = (HUBS / name).read_text(encoding="utf-8").replace("«INSTALL", "INSTALLED-IN-TEST")
            (prompts / name).write_text(text, encoding="utf-8")
        (reports / "cto-2026-01-02.md").write_text(APPROVED_R1 + "\n")
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        self.commit()
        base = git(self.repo, "rev-parse", "--short=8", "HEAD")

        job = self.wt / "x-job"
        git(self.repo, "worktree", "add", "-q", "-b", "ops/x-job", str(job), base)
        (job / "ops").mkdir()
        (job / "ops" / "x.sh").write_text("true\n")
        git(job, "add", "-A")
        git(job, "commit", "-q", "-m", "code")
        tip = git(job, "rev-parse", "--short=8", "HEAD")
        build_report = job / "docs" / "40 - DevDocs" / "reports" / "x-job-build.md"
        build_report.parent.mkdir(parents=True, exist_ok=True)
        build_report.write_text(f"BUILT · job: x-job · tip: {tip} | self-check: 3 of 3\n")
        git(job, "add", "-A")
        git(job, "commit", "-q", "-m", "report")
        head = git(job, "rev-parse", "--short=8", "HEAD")

        check_report = reports / "x-job-check.md"
        check_report.write_text(
            f"CHECK DONE · job: x-job · pass: 1 · tip: {tip} · held unfixed: 0 · ready: YES\n")
        self.cards = {
            "build": day / "01-x-job-card.md",
            "check": day / "01-x-job-card.md",
            "deploy": day / "02-x-deploy-card.md",
            "devfix": day / "03-x-fix-card.md",
        }
        self.cards["build"].write_text(
            "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
            f"BASE: {base}\nTIP: {tip}\nREPORT: {build_report}\n"
            f"CHECK REPORT: {reports / 'x-job-check-new.md'}\n"
            "HOUSE B: as needed\nTREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n")
        self.cards["deploy"].write_text(
            "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
            f"BASE: main\nTIP: {head}\nREPORT: {reports / 'deploy-x.md'}\nRULINGS: none\n"
            "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n\n"
            "| # | branch | code tip | branch head | check report | its stop line must carry |\n"
            f"|---|---|---|---|---|---|\n| 1 | `ops/x-job` | `{tip}` | `{head}` | `{check_report}` | "
            "`held unfixed: 0` and `ready: YES` |\n\n## MARKERS\n## SMOKE READS\n")
        self.cards["devfix"].write_text(
            "JOB: x-fix\nLADDER: OFF-LADDER\nBRANCH: ops/x-fix\nWORKTREE: x-fix\n"
            f"BASE: {base}\nREPORT: {reports / 'devfix-x-fix.md'}\nRULINGS: 2026-01-02 R1\n"
            "TABLE: user.x_table\nPROOF TEST: tests/cobalt/test_x_proof.py\n\n## RECORDS\n- constructed\n")
        self.commit()

        stub = tmp_path / "bin"
        stub.mkdir()
        self.calls = tmp_path / "claude-args"
        (stub / "claude").write_text(
            '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
            f'for a in "$@"; do printf "%s\\n" "$a"; done >> "{self.calls}"\nexit 0\n')
        (stub / "claude").chmod(0o755)
        self.env = dict(os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
                        PATH=f"{stub}:{os.environ['PATH']}", **GIT_ENV)

    def commit(self) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "x")

    def launch(self, kind: str, dry: bool) -> subprocess.CompletedProcess:
        env = dict(self.env, DESK_LAUNCH_DRY="1") if dry else self.env
        return subprocess.run(["sh", str(LAUNCH), kind, str(self.cards[kind])], env=env,
                              capture_output=True, text=True, timeout=120)


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


@pytest.mark.parametrize("kind", sorted(KINDS))
def test_a_dry_launch_of_each_kind_prints_a_line_holding_the_flag(desk, kind):
    done = desk.launch(kind, dry=True)
    assert done.returncode == 0, done.stderr
    (line,) = [ln for ln in done.stdout.splitlines() if ln.startswith("claude --bg ")]
    assert line.count(FLAG_SRC) == 1, line


def test_a_real_launch_hands_the_session_the_flag_byte_for_byte(desk):
    """desk-launch.sh evals the line: the `$(…)` must reach `claude` as written, not run."""
    done = desk.launch("build", dry=False)
    assert done.returncode == 0, done.stderr
    args = desk.calls.read_text(encoding="utf-8").splitlines()
    assert args.count("--append-system-prompt") == 1
    assert args[args.index("--append-system-prompt") + 1] == FLAG
    assert "command not found" not in done.stderr
