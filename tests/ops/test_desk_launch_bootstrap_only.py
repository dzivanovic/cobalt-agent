"""desk-launch.sh deploy admits a BOOTSTRAP-ONLY card (card 2026-10-20/931, row T2).

The `Desk` fixture is tests/ops/test_desk_launch_launchd.py's shape: a tmp main repo
(COBALT_REPO_ROOT) with this tree's DEPLOY-HUB.md, a built job branch, its committed check report,
a committed build card naming the plist in its row's `files`, and a normal deploy card;
COBALT_WT_ROOT a tmp directory. The bootstrap-only card is card 929's FORM (its header keys and
sections) with constructed values only. Every launch is dry (DESK_LAUNCH_DRY=1): nothing runs.
"""

from __future__ import annotations

import os
import re
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

LABEL = "com.cobalt.prefill-refresh"
BOOTOUT = f"Bash(launchctl bootout gui/501/{LABEL})"
BOOTSTRAP = f"Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/{LABEL}.plist)"
BUILD_CARD = "prompts/2026-01-02/01-x-job-card.md"
FILL = chr(0xAB) + "FILL"
MERGE_HEX = re.compile(r"merge --no-edit [0-9a-f]{8}\b")


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


def launchd_line(label: str = LABEL, mode: str = "add") -> str:
    return f"{label} · {mode} · {BUILD_CARD}:C2 · dry run: none"


def gate_lines(label: str = LABEL) -> list[str]:
    return [f"GATE RESULT: {label} · X{n} · OK" for n in (1, 2, 3)]


def boot_card(*, reports: Path, tip: str = "none", branch: str = "none", wt: str = "none",
              ships: str = "", migrations: str = "none", tag: str = "x-tag", rulings: str = "none",
              launchd: list[str] | None = None, gates: list[str] | None = None,
              markers: bool = True, extra: str = "") -> str:
    """Card 929's form, constructed values only."""
    launchd = [launchd_line()] if launchd is None else launchd
    gates = gate_lines() if gates is None else gates
    text = (
        f"JOB: x-boot\nLADDER: OFF-LADDER\nBRANCH: {branch}\nWORKTREE: {wt}\nBASE: main\n"
        f"TIP: {tip}\nREPORT: {reports / 'deploy-x.md'}\nRULINGS: {rulings}\nTAG: {tag}\n"
        f"MIGRATIONS: {migrations}\nSET: x\nTICKERS: none\nWAITS: x-one DEPLOYED, x-two DEPLOYED\n\n"
        + ships
        + "## LAUNCHD\n" + "".join(f"{ln}\n" for ln in launchd)
        + "\n## GATE RESULTS\n" + "".join(f"{ln}\n" for ln in gates)
        + "\n## NOT IN THIS JOB\n- A merge, an outage, a restart.\n\n"
    )
    if markers:
        text += "## MARKERS\n- `ls /nowhere/marker` · before `No such file or directory` · after `listed`\n\n"
    text += (
        "## SMOKE READS\n- one · `ls /nowhere/marker` · `0`\n\n"
        "## CHECK ASKS\n- X1 one.\n\n## RECORDS\n- a desk fact\n" + extra
    )
    return text


class Desk:
    """A tmp main repo with this tree's DEPLOY-HUB.md, a built job branch, a build card, a normal
    deploy card with its committed check report, and a bootstrap-only card."""

    def __init__(self, tmp_path: Path):
        self.wt = tmp_path / "wt"
        self.repo = tmp_path / "repo"
        self.wt.mkdir()
        self.repo.mkdir()
        prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        day = prompts / "2026-01-02"
        day.mkdir(parents=True)
        self.reports.mkdir(parents=True)
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
        self.head = git(job, "rev-parse", "--short=8", "HEAD")

        check_report = self.reports / "x-job-check.md"
        check_report.write_text(
            f"CHECK DONE · job: x-job · pass: 1 · tip: {tip} · held unfixed: 0 · ready: YES\n")
        (day / "01-x-job-card.md").write_text(
            "JOB: x-job\n\n## ROWS\n| row | what | red first | files |\n"
            f"| C2 | the plist | T | `ops/{LABEL}.plist` |\n")
        self.ships = (
            "## SHIPS\n\n| # | branch | code tip | branch head | check report | its stop line must carry |\n"
            f"|---|---|---|---|---|---|\n| 1 | `ops/x-job` | `{tip}` | `{self.head}` | `{check_report}` | "
            "`held unfixed: 0` and `ready: YES` |\n\n"
        )
        self.normal = day / "02-x-deploy-card.md"
        self.normal.write_text(
            "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
            f"BASE: main\nTIP: {self.head}\nREPORT: {self.reports / 'deploy-y.md'}\nRULINGS: none\n"
            "TAG: y-tag\nMIGRATIONS: none\nSET: x-job\n\n" + self.ships + "## MARKERS\n## SMOKE READS\n")
        self.card = day / "03-x-boot-card.md"
        self.set_card()
        self.env = dict(os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
                        DESK_LAUNCH_DRY="1", **GIT_ENV)

    def commit(self) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "x")

    def set_card(self, **kw) -> None:
        self.card.write_text(boot_card(reports=self.reports, **kw))
        self.commit()

    def launch(self, card: Path | None = None, *extra: str) -> subprocess.CompletedProcess:
        return subprocess.run(["sh", str(LAUNCH), "deploy", str(card or self.card), *extra],
                              env=self.env, capture_output=True, text=True, timeout=120)


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def test_t2_the_929_form_is_admitted(desk):
    """RED on BASE: exit 1, `incomplete card: no '## SHIPS' section` (the `section SHIPS` read)."""
    done = desk.launch()
    assert done.returncode == 0, done.stderr
    (line,) = [ln for ln in done.stdout.splitlines() if ln.startswith("claude --bg ")]
    allow = tools(line, "--allowedTools")
    assert allow.count(BOOTOUT) == 1 and allow.count(BOOTSTRAP) == 1, allow
    assert not MERGE_HEX.search(line), line
    assert not [ln for ln in done.stdout.splitlines() if "worktree add" in ln], done.stdout
    assert "--name deploy-hub-x-boot" in line


def test_t2_a_normal_card_still_cuts_its_gate(desk):
    """CONTROL, green on BASE and after: a card with a ## SHIPS row and an 8-hex TIP runs as today."""
    done = desk.launch(desk.normal)
    assert done.returncode == 0, done.stderr
    adds = [ln for ln in done.stdout.splitlines() if " worktree add -b deploy/x-deploy " in ln]
    assert adds == [f"git -C {desk.repo} worktree add -b deploy/x-deploy {desk.wt}/x-gate main"], done.stdout
    (line,) = [ln for ln in done.stdout.splitlines() if ln.startswith("claude --bg ")]
    assert f"merge --no-edit {desk.head})" in line


PARTIAL = {
    "TIP alone none": dict(branch="deploy/x-boot", wt="x-gate"),
    "BRANCH alone none": dict(tip="aaaaaaaa", wt="x-gate"),
    "WORKTREE alone none": dict(tip="aaaaaaaa", branch="deploy/x-boot"),
    "TIP and BRANCH none": dict(wt="x-gate"),
    "a ## SHIPS section": dict(ships="SHIPS"),
    "MIGRATIONS not none": dict(migrations="0099 · x"),
    "zero ## LAUNCHD lines": dict(launchd=[]),
    "two ## LAUNCHD lines": dict(launchd=[launchd_line(), launchd_line("com.cobalt.other-job")]),
    "mode change": dict(launchd=[launchd_line(mode="change")]),
    "mode deferred": dict(launchd=[f"{launchd_line(mode='deferred')} · gate: X1"]),
    "no GATE RESULT line": dict(gates=[]),
    "a GATE RESULT of another label": dict(gates=gate_lines() + gate_lines("com.cobalt.other-job")[:1]),
    "a GATE RESULT with no result": dict(gates=[f"GATE RESULT: {LABEL} · X1"]),
}


@pytest.mark.parametrize("case", sorted(PARTIAL))
def test_t2_every_partial_form_is_refused(desk, case):
    """Each partial form → exit 1, `bootstrap-only card`, nothing on stdout.

    BASE refuses each of them too (exit 1, nothing on stdout), by another message: most by the
    `## SHIPS` read, the three `none` with a `## SHIPS` by `TIP 'none' is not 8 hex characters`.
    The message is the assertion that tells them apart, so each is RED on BASE by it alone.
    """
    kw = dict(PARTIAL[case])
    if kw.get("ships") == "SHIPS":
        kw["ships"] = desk.ships
    desk.set_card(**kw)
    done = desk.launch()
    assert done.returncode == 1, done.stdout
    assert done.stdout == ""
    assert "REFUSED: deploy: bootstrap-only card: " in done.stderr, done.stderr


OTHER = {
    "a FILL token": (dict(extra=f"- {FILL}: x\n"), "tokens listed above still stand"),
    "the card edited after its commit": ("EDIT", "the card differs from its commit"),
    "the deploy report present": ("REPORT", "the deploy report already exists"),
    "a TAG with a slash": (dict(tag="a/b"), "is not a plain tag name"),
    "RULINGS x": (dict(rulings="x"), "RULINGS must start"),
    "the agent as the label": (
        dict(launchd=[launchd_line("com.cobalt.agent")], gates=gate_lines("com.cobalt.agent")),
        "is a resident"),
    "no ## MARKERS": (dict(markers=False), "no '## MARKERS' section"),
    "a STEP-D0 resume": ("STEP", "a resume needs the gate worktree"),
    "a held lock dir": ("LOCK", "the cobalt_dev lock is held"),
}


@pytest.mark.parametrize("case", sorted(OTHER))
def test_t2_every_other_refusal_still_fires(desk, case):
    """On the admitted 929 form, each other refusal fires its own message.

    On BASE the deploy arm's own refusals (TAG, the label, MARKERS, the resume, the report, the
    lock) are hidden behind the `## SHIPS` refusal, so those cases are RED there; the FILL token,
    the edited card and RULINGS are read before the deploy arm and fire on BASE as after.
    """
    change, message = OTHER[case]
    extra: tuple[str, ...] = ()
    if isinstance(change, dict):
        desk.set_card(**change)
    elif change == "EDIT":
        desk.card.write_text(desk.card.read_text() + "- edited\n")
    elif change == "REPORT":
        (desk.reports / "deploy-x.md").write_text("x\n")
    elif change == "STEP":
        extra = ("STEP-D0",)
    elif change == "LOCK":
        (desk.wt / ".cobalt_dev.lock").mkdir()
        (desk.wt / ".cobalt_dev.lock" / "owner").write_text("other-job\n")
    done = desk.launch(None, *extra)
    assert done.returncode == 1, done.stdout
    assert "REFUSED: " in done.stderr and message in done.stderr, done.stderr
    assert "## SHIPS" not in done.stderr, done.stderr


# ---- the check of card 931 (O1, O2 its own; A1, A2 house A Gemini) ------------------------------


def test_o1_a_step_d0_resume_of_a_bootstrap_only_card_is_refused_with_a_none_dir(desk):
    """Check O1: a bootstrap-only card has no gate, so STEP-D0 is refused whatever $WT holds."""
    (desk.wt / "none").mkdir()
    done = desk.launch(None, "STEP-D0")
    assert done.returncode == 1, done.stdout
    assert "REFUSED: " in done.stderr, done.stderr


def test_o2_a_bulleted_gate_result_of_another_label_is_refused(desk):
    """Check O2: no GATE RESULT line names another label, bulleted or not."""
    desk.set_card(gates=gate_lines() + ["- GATE RESULT: com.cobalt.other-job · X1 · OK"])
    done = desk.launch()
    assert done.returncode == 1, done.stdout
    assert "REFUSED: deploy: bootstrap-only card: " in done.stderr, done.stderr


def test_t2_a_gate_result_of_another_label_mentioning_the_card_label_is_refused(desk):
    desk.set_card(
        gates=[f"GATE RESULT: com.cobalt.other-job · X1 · after GATE RESULT: {LABEL} · OK"]
    )
    done = desk.launch()
    assert done.returncode == 1, done.stdout
    assert done.stdout == ""
    assert "REFUSED: deploy: bootstrap-only card: " in done.stderr, done.stderr


@pytest.mark.parametrize(
    "line",
    [
        f"GATE RESULT: {LABEL} ·   · OK",
        f"GATE RESULT: {LABEL} · X1 ·  ",
    ],
)
def test_t2_a_gate_result_with_a_blank_item_or_result_is_refused(desk, line):
    desk.set_card(gates=[line])
    done = desk.launch()
    assert done.returncode == 1, done.stdout
    assert done.stdout == ""
    assert "REFUSED: deploy: bootstrap-only card: " in done.stderr, done.stderr
