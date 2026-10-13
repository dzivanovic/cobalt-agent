"""desk-launch.sh fills DEPLOY-HUB.md's `<launchd strings>` from the card's `## LAUNCHD` (card
2026-10-13/496 plist-step-c, row L1).

The `Desk` fixture is tests/ops/test_hub_lines.py's shape: a tmp main repo (COBALT_REPO_ROOT)
with this tree's DEPLOY-HUB.md, a built job branch, its committed check report and a committed
deploy card; COBALT_WT_ROOT a tmp directory. Every launch is dry (DESK_LAUNCH_DRY=1): nothing
runs. Constructed labels and commands only.
"""

from __future__ import annotations

import os
import shlex
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

DRY = "COBALT_ENV=production uv run prefill refresh --dry-run"
BOOTOUT = "Bash(launchctl bootout gui/501/com.cobalt.prefill-refresh)"
BOOTSTRAP = "Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist)"
BUILD_CARD = "prompts/2026-01-02/01-x-job-card.md"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def tools(line: str, option: str) -> list[str]:
    words = shlex.split(line)
    out, inside = [], False
    for w in words:
        if w.startswith("--"):
            inside = w == option
            continue
        if inside:
            out.append(w)
    return out


def launchctl_strings(line: str) -> list[str]:
    return [s for s in tools(line, "--allowedTools") if s.startswith("Bash(launchctl ")]


class Desk:
    """A tmp main repo with this tree's DEPLOY-HUB.md, a built job branch, a job card, and a
    deploy card with its committed check report."""

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
        (prompts / "DEPLOY-HUB.md").write_text((HUBS / "DEPLOY-HUB.md").read_text(encoding="utf-8"),
                                               encoding="utf-8")
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
        (day / "01-x-job-card.md").write_text(
            "JOB: x-job\n\n## ROWS\n| row | what | red first | files |\n"
            "| C2 | the plist | T | `ops/com.cobalt.prefill-refresh.plist` |\n")
        self.card = day / "02-x-deploy-card.md"
        self.head_text = (
            "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
            f"BASE: main\nTIP: {head}\nREPORT: {reports / 'deploy-x.md'}\nRULINGS: none\n"
            "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n\n"
            "| # | branch | code tip | branch head | check report | its stop line must carry |\n"
            f"|---|---|---|---|---|---|\n| 1 | `ops/x-job` | `{tip}` | `{head}` | `{check_report}` | "
            "`held unfixed: 0` and `ready: YES` |\n\n## MARKERS\n## SMOKE READS\n")
        self.set_card("")
        self.env = dict(os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
                        DESK_LAUNCH_DRY="1", **GIT_ENV)

    def commit(self) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "x")

    def set_card(self, launchd: str) -> None:
        self.card.write_text(self.head_text + launchd)
        self.commit()

    def launch(self) -> subprocess.CompletedProcess:
        return subprocess.run(["sh", str(LAUNCH), "deploy", str(self.card)], env=self.env,
                              capture_output=True, text=True, timeout=120)

    def line(self) -> str:
        done = self.launch()
        assert done.returncode == 0, done.stderr
        (line,) = [ln for ln in done.stdout.splitlines() if ln.startswith("claude --bg ")]
        return line


def section(*lines: str) -> str:
    return "\n## LAUNCHD\n" + "".join(f"{ln}\n" for ln in lines)


def card_line(label="com.cobalt.prefill-refresh", mode="add", card=BUILD_CARD, dry=DRY, gate=None):
    out = f"{label} · {mode} · {card}:C2 · dry run: {dry}"
    return out + (f" · gate: {gate}" if gate is not None else "")


TODAY_EIGHT = 8


def test_l1_a_named_label_gets_exactly_its_strings(tmp_path):
    desk = Desk(tmp_path)
    today = launchctl_strings(desk.line())
    assert len(today) == TODAY_EIGHT, today
    desk.set_card(section(card_line()))
    line = desk.line()
    allow = tools(line, "--allowedTools")
    for s in (BOOTSTRAP, BOOTOUT, f"Bash({DRY})"):
        assert allow.count(s) == 1, (s, allow)
    assert sorted(launchctl_strings(line)) == sorted(today + [BOOTOUT, BOOTSTRAP])
    # the hub carries the token once, after the radar kickstart -k string
    hub_line = [ln for ln in (HUBS / "DEPLOY-HUB.md").read_text(encoding="utf-8").splitlines()
                if ln.startswith("claude --bg ")][0]
    assert hub_line.count(" <launchd strings>") == 1
    assert '"Bash(launchctl kickstart -k gui/501/com.cobalt.radar)" <launchd strings>' in hub_line


def test_l1_no_section_no_new_string(tmp_path):
    desk = Desk(tmp_path)
    line = desk.line()
    assert len(launchctl_strings(line)) == TODAY_EIGHT
    assert "<launchd strings>" not in line
    # byte for byte the line of the hub with the token removed (today's hub)
    hub = (HUBS / "DEPLOY-HUB.md").read_text(encoding="utf-8")
    if " <launchd strings>" in hub:
        (desk.repo / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md").write_text(
            hub.replace(" <launchd strings>", ""), encoding="utf-8")
        desk.commit()
    assert desk.line() == line


def test_l1_a_deferred_label_gets_no_string(tmp_path):
    desk = Desk(tmp_path)
    desk.set_card(section(card_line(mode="deferred", dry="none", gate="X8, X15")))
    line = desk.line()
    assert len(launchctl_strings(line)) == TODAY_EIGHT
    assert "prefill-refresh" not in line


@pytest.mark.parametrize("bad", [
    card_line(label="com.cobalt.Bad_Label"),
    card_line(label="com.cobalt.aset"),
    card_line(label="com.cobalt.radar"),
    card_line(label="com.cobalt.agent"),
    "REPEAT",
    card_line(mode="remove"),
    card_line(card="prompts/2026-01-02/99-none-card.md"),
    card_line(card="reports/x-card.md"),
    card_line(dry="COBALT_ENV=production uv run prefill refresh"),
    card_line(dry="COBALT_ENV=production uv run a b c d e --dry-run"),
    card_line(dry="COBALT_ENV=production uv run prefill * --dry-run"),
    card_line(dry="COBALT_ENV=production uv run prefill refresh --dry-run; rm x"),
    card_line(mode="deferred", dry="none"),
    "TWO",
])
def test_l1_each_refusal(tmp_path, bad):
    desk = Desk(tmp_path)
    if bad == "REPEAT":
        launchd = section(card_line(), card_line(mode="change"))
    elif bad == "TWO":
        launchd = section(card_line()) + section(card_line(label="com.cobalt.other"))
    else:
        launchd = section(bad)
    desk.set_card(launchd)
    done = desk.launch()
    assert done.returncode != 0, done.stdout
    assert "REFUSED" in done.stderr, done.stderr


def test_l1_no_generated_launchctl_string_holds_a_wildcard(tmp_path):
    desk = Desk(tmp_path)
    today = tools(desk.line(), "--allowedTools")
    desk.set_card(section(card_line(), card_line(label="com.cobalt.other-job", mode="change", dry="none")))
    new = [s for s in tools(desk.line(), "--allowedTools") if s not in today]
    assert all("*" not in s for s in new), new
    assert all(s.startswith(("Bash(launchctl boot", "Bash(COBALT_ENV=production uv run ")) for s in new), new
