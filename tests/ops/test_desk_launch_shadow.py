"""desk-launch.sh shadow <card> --model <id>: the gate seat on SHADOW-HUB.md (card 2026-10-11 324, S2).

Every run copies ops/desk/desk-launch.sh into tmp_path/ops/ beside a passing desk-size guard
(desk-context.sh). COBALT_REPO_ROOT points it at a tmp repo whose SHADOW-HUB.md is a constructed
fixed file: one launch line carrying every token the kind fills, and a `## BUILDERS` table of the
four builder rows, Grok's signed (a constructed row), the other three still holding the sign mark.
COBALT_WT_ROOT points it at a tmp worktree root. `claude` is a stub on PATH that records its cwd
and arguments. One test runs the tree's own SHADOW-HUB.md through the same script. Nothing here
launches a seat.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
REAL = REPO / "docs" / "40 - DevDocs" / "prompts" / "SHADOW-HUB.md"
INSTALL = "«" + "INSTALL"  # built so this file never spells the token whole
SIGN = "«" + "SIGN"
UNSIGNED = f"NEEDS HIS SIGN-OFF {SIGN}: his row»"
SIGNED = "HIS RULING · APPROVED 2026-01-02 R1"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

HUB_PATH = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"
ALLOW = {
    "grok-4.7": "Bash(grok -m grok-4.7 --sandbox cobalt-job *)",
    "claude-sonnet-5-5": "Bash(claude -p --model claude-sonnet-5-5 *)",
    "gpt-5.6-terra": "Bash(codex exec --skip-git-repo-check -m gpt-5.6-terra -s workspace-write *)",
    "gemini-4-argon-high": "Bash(agy --model gemini-4-argon-high --mode accept-edits --sandbox *)",
}
SLUG = {"grok-4.7": "grok", "claude-sonnet-5-5": "sonnet", "gpt-5.6-terra": "terra", "gemini-4-argon-high": "gemini"}
COMMAND = {
    "grok-4.7": 'grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/<worktree>/**)" -p "<pass prompt>"',
    "claude-sonnet-5-5": 'claude -p --model claude-sonnet-5-5 --permission-mode dontAsk "<pass prompt>"',
    "gpt-5.6-terra": 'codex exec --skip-git-repo-check -m gpt-5.6-terra -s workspace-write -C /Users/cobalt/cobalt-wt/<worktree> "<pass prompt>" < /dev/null',
    "gemini-4-argon-high": 'agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 40m --add-dir /Users/cobalt/cobalt-wt/<worktree> --print="<pass prompt>"',
}


def line_for(mode: str = "--permission-mode dontAsk") -> str:
    return (
        f"claude --bg \"Read '{HUB_PATH}' and follow it exactly. CARD: '<card>' MODEL: <model>\" "
        f"--model claude-opus-5-5 {mode} --remote-control <job>-gate --name <job>-gate "
        '--allowedTools "Read" "Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)" <builder allow> '
        '--disallowedTools "AskUserQuestion" "EnterWorktree" --add-dir /Users/cobalt/cobalt-wt'
    )


def hub_text(line: str, signed: tuple[str, ...] = ("grok-4.7",), title: str = "# SHADOW-HUB (constructed, installed)") -> str:
    rows = "".join(
        f"| `{m}` | `{SLUG[m]}` | `{ALLOW[m]}` | `{COMMAND[m]}` | {SIGNED if m in signed else UNSIGNED} |\n"
        for m in ALLOW
    )
    return (
        f"{title}\n\n{line}\n\n## BUILDERS\n\n| id | slug | builder allow | builder command | SIGN |\n"
        f"|---|---|---|---|---|\n{rows}\n## PROCEDURE\n\nconstructed\n"
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
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        self.fixed = self.prompts / "SHADOW-HUB.md"
        self.fixed.write_text(hub_text(line_for()))
        (self.reports / "cto-2026-01-02.md").write_text(
            "| R1 | 07:00 ET | HIS RULING (constructed). | HIS RULING · APPROVED |\n")
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")
        self.base = git(self.repo, "rev-parse", "--short=8", "HEAD")
        self.card = self.card_for("grok")
        ops = tmp_path / "ops"
        ops.mkdir()
        self.launch = ops / "desk-launch.sh"
        shutil.copy(LAUNCH, self.launch)
        write_exe(ops / "desk-context.sh", "exit 0\n")
        self.calls = tmp_path / "claude-calls"
        write_exe(tmp_path / "bin" / "claude",
                  'if [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
                  f'printf "%s | %s\\n" "$PWD" "$*" >> "{self.calls}"\nexit 0\n')
        self.agy = tmp_path / "agy-settings.json"
        self.agy.write_text(json.dumps(
            {"permissions": {"allow": [f"write_file({self.wt}/x-job-gemini/)"]}},
            indent=2,
        ) + "\n")
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            COBALT_AGY_SETTINGS=str(self.agy),
            PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}", **GIT_ENV,
        )

    def card_for(self, slug: str, **over: str | None) -> Path:
        job = f"x-job-{slug}"
        keys = {
            "JOB": job,
            "LADDER": "OFF-LADDER — constructed",
            "BRANCH": f"shadow/{job}",
            "WORKTREE": job,
            "BASE": self.base,
            "TIP": "",
            "REPORT": str(self.wt / job / "docs" / "40 - DevDocs" / "reports" / f"{job}-build.md"),
            "RULINGS": "2026-01-02 R1",
            "SHADOW OF": str(self.prompts / "2026-01-02" / "01-x-job-card.md"),
        }
        keys.update(over)
        card = self.prompts / "2026-01-02" / f"02-{job}-card.md"
        head = "".join(f"{k}: {v}\n" for k, v in keys.items() if v is not None)
        card.write_text(head + "\n## ROWS\n\n| row | what |\n|---|---|\n| X1 | constructed |\n")
        self.commit(f"card {job}")
        return card

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def set_hub(self, text: str) -> None:
        self.fixed.write_text(text)
        self.commit("hub")

    def run(self, *args: str, dry: bool = True) -> subprocess.CompletedProcess:
        env = dict(self.env, DESK_LAUNCH_DRY="1") if dry else self.env
        return subprocess.run(
            ["sh", str(self.launch), "shadow", *args], env=env, cwd=self.tmp,
            capture_output=True, text=True, timeout=120,
        )

    def filled(self, model: str, card: Path | None = None) -> str:
        card = card or self.card
        job = f"x-job-{SLUG[model]}"
        return (
            line_for().replace("<card>", str(card)).replace("<job>", job).replace("<worktree>", job)
            .replace("<model>", model).replace("<builder allow>", f'"{ALLOW[model]}"')
        )


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def refused(done: subprocess.CompletedProcess, text: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert done.stdout == ""


# ---- the good case (the positive control) ---------------------------------------------------


def test_a_signed_model_prints_the_add_the_cd_and_the_line(desk):
    done = desk.run(str(desk.card), "--model", "grok-4.7")
    assert done.returncode == 0, done.stderr
    wt = desk.wt / "x-job-grok"
    assert done.stdout.splitlines() == [
        f"git -C {desk.repo} worktree add -b shadow/x-job-grok {wt} {desk.base}",
        f"cd {wt}",
        desk.filled("grok-4.7"),
    ]
    line = done.stdout.splitlines()[2]
    assert f'"{ALLOW["grok-4.7"]}"' in line
    for other in ("claude-sonnet-5-5", "gpt-5.6-terra"):
        assert ALLOW[other] not in line
    assert "WATCH: sh " in done.stderr and " shadow " in done.stderr
    assert not desk.calls.exists()
    assert not wt.exists()  # a dry run makes nothing


def test_a_signed_model_launches_from_the_worktree_it_adds(desk):
    done = desk.run(str(desk.card), "--model", "grok-4.7", dry=False)
    assert done.returncode == 0, done.stderr
    cwd, args = desk.calls.read_text().splitlines()[0].split(" | ", 1)
    assert Path(cwd).resolve() == (desk.wt / "x-job-grok").resolve()
    assert "MODEL: grok-4.7" in args
    assert "--remote-control x-job-grok-gate --name x-job-grok-gate" in args
    assert git(desk.repo, "rev-parse", "--abbrev-ref", "shadow/x-job-grok") == "shadow/x-job-grok"


# ---- the refusals: exit 1, each its own reason, nothing launched -----------------------------


def test_an_unsigned_model_is_refused_beside_a_signed_one(desk):
    """THE TEST he asked for: signed Grok passes, unsigned Sonnet in the same fixture refuses."""
    assert desk.run(str(desk.card), "--model", "grok-4.7").returncode == 0
    card = desk.card_for("sonnet")
    refused(desk.run(str(card), "--model", "claude-sonnet-5-5"), "shadow: model claude-sonnet-5-5: builder line not signed")


def test_a_gemini_id_is_refused_by_name(desk):
    refused(desk.run(str(desk.card), "--model", "gemini-3.1-pro-high"),
            "shadow: model 'gemini-3.1-pro-high' is a Gemini id not admitted; gemini-4-argon-high is the one Gemini builder (R1738)")


# ---- card 2026-10-16 671 L1: of the Gemini ids only gemini-4-argon-high (R1738) ---------------


def test_k5_gemini_4_argon_high_is_admitted(desk):
    desk.set_hub(hub_text(line_for(), signed=("grok-4.7", "gemini-4-argon-high")))
    card = desk.card_for("gemini")
    done = desk.run(str(card), "--model", "gemini-4-argon-high")
    assert done.returncode == 0, done.stderr
    line = done.stdout.splitlines()[-1]
    assert "MODEL: gemini-4-argon-high" in line
    assert '"Bash(agy --model gemini-4-argon-high --mode accept-edits --sandbox *)"' in line


@pytest.mark.parametrize("model", ["gemini-4-argon-medium", "gemini-4-argon-low"])
def test_k5_gemini_medium_and_low_are_refused(desk, model):
    desk.set_hub(hub_text(line_for(), signed=("grok-4.7", "gemini-4-argon-high")))
    refused(desk.run(str(desk.card_for("gemini")), "--model", model),
            f"shadow: model '{model}' is a Gemini id not admitted; gemini-4-argon-high is the one Gemini builder (R1738)")


def test_an_id_not_in_the_table_is_refused(desk):
    refused(desk.run(str(desk.card), "--model", "gpt-5.6-sol"), "shadow: model 'gpt-5.6-sol' is no id of ## BUILDERS")


def test_no_model_is_refused(desk):
    refused(desk.run(str(desk.card)), "shadow: --model <id> is required")


def test_two_models_are_refused(desk):
    refused(desk.run(str(desk.card), "--model", "grok-4.7", "--model", "grok-4.7"),
            "shadow: --model is given 2 times; one model per launch")


def test_the_install_title_is_refused(desk):
    desk.set_hub(hub_text(line_for(), title=f"# SHADOW-HUB {INSTALL}: his row»"))
    refused(desk.run(str(desk.card), "--model", "grok-4.7"), f"the fixed file still carries its {INSTALL} token")


def test_the_line_in_auto_is_refused(desk):
    desk.set_hub(hub_text(line_for("--permission-mode auto")))
    refused(desk.run(str(desk.card), "--model", "grok-4.7"), "shadow: permission mode 'auto' is not dontAsk")


def test_two_permission_modes_are_refused(desk):
    desk.set_hub(hub_text(line_for("--permission-mode dontAsk --permission-mode auto")))
    refused(desk.run(str(desk.card), "--model", "grok-4.7"), "shadow: the line states --permission-mode 2 times, not once")


def test_bypass_permissions_on_the_line_is_refused(desk):
    desk.set_hub(hub_text(line_for() + " --permission-mode bypassPermissions"))
    refused(desk.run(str(desk.card), "--model", "grok-4.7"), "shadow: bypassPermissions on the line (L55)")


def test_no_shadow_of_is_refused(desk):
    card = desk.card_for("grok", **{"SHADOW OF": None})
    refused(desk.run(str(card), "--model", "grok-4.7"), "shadow: the card's header has no 'SHADOW OF:' line")


def test_a_branch_outside_shadow_is_refused(desk):
    card = desk.card_for("grok", BRANCH="s3/x")
    refused(desk.run(str(card), "--model", "grok-4.7"), "shadow: BRANCH 's3/x' does not start 'shadow/'")


def test_a_job_slug_of_another_model_is_refused(desk):
    card = desk.card_for("sonnet")
    refused(desk.run(str(card), "--model", "grok-4.7"), "shadow: JOB 'x-job-sonnet' does not end in '-grok' (model grok-4.7)")


def test_an_uncommitted_fixed_file_is_refused(desk):
    desk.fixed.write_text(hub_text(line_for()) + "\n")
    refused(desk.run(str(desk.card), "--model", "grok-4.7"), "the fixed file differs from its commit")


# ---- the tree's own SHADOW-HUB.md through the same script ------------------------------------


def test_the_real_file_launches_a_signed_grok(desk):
    """The real text with its install token and Grok's sign mark filled as the desk fills them."""
    text = REAL.read_text()
    title, rest = text.split("\n", 1)
    title = title.split(INSTALL)[0] + SIGNED
    lines = rest.split("\n")
    for k, x in enumerate(lines):
        if x.startswith("| `grok-4.7` |"):
            lines[k] = x.replace(UNSIGNED, SIGNED)
    desk.set_hub(title + "\n" + "\n".join(lines))
    done = desk.run(str(desk.card), "--model", "grok-4.7")
    assert done.returncode == 0, done.stderr
    line = done.stdout.splitlines()[-1]
    assert f'"{ALLOW["grok-4.7"]}" --disallowedTools ' in line
    assert "MODEL: grok-4.7" in line and "<" not in line
    terra = desk.run(str(desk.card_for("terra")), "--model", "gpt-5.6-terra")
    assert terra.returncode == 0, terra.stderr  # card 355 S1: signed on his R1069
    gemini = desk.run(str(desk.card_for("gemini")), "--model", "gemini-4-argon-high")
    assert gemini.returncode == 0, gemini.stderr  # card 671 L1: the real row, signed on his R1738


def test_the_real_file_holds_no_install_token_and_no_sign_mark():
    """Card 355 S1, his R1069: SHADOW-HUB.md and SPIKE-HUB.md are installed and signed."""
    for path in (REAL, REAL.with_name("SPIKE-HUB.md")):
        text = path.read_text()
        assert INSTALL not in text, path.name
        assert SIGN not in text, path.name


def test_s2_a_role_trial_refuses_a_non_grok_model(desk):
    desk.set_hub(
        hub_text(
            line_for(),
            signed=("grok-4.7", "claude-sonnet-5-5"),
        )
    )
    card = desk.card_for("sonnet", ROLE="drafter")

    refused(
        desk.run(str(card), "--model", "claude-sonnet-5-5"),
        "shadow: ROLE trials run only grok-4.7",
    )


# ---- card 2026-10-18 759 L1: the launcher confines Gemini (R1863) ----------------------------


def write_agy(desk: Desk, rules: list[str]) -> None:
    Path(desk.env["COBALT_AGY_SETTINGS"]).write_text(
        json.dumps({"permissions": {"allow": rules}}, indent=2) + "\n")


def signed_gemini(desk: Desk) -> Path:
    desk.set_hub(hub_text(line_for(), signed=("grok-4.7", "gemini-4-argon-high")))
    return desk.card_for("gemini")


def test_k5_gemini_without_its_worktree_grant_is_refused(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    write_agy(desk, [f"read_file({grant})"])
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f'shadow: gemini: {agy} holds no allow rule "write_file({grant})" (SHADOW-HUB GRANT)',
    )


def test_k5_gemini_without_a_settings_file_is_refused(desk):
    card = signed_gemini(desk)
    agy = Path(desk.env["COBALT_AGY_SETTINGS"])
    agy.unlink()
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: no agy settings file at {agy}",
    )


def test_k5_gemini_with_a_read_url_rule_is_refused(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    write_agy(desk, [f"write_file({grant})", "read_url(*)"])
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy} holds a read_url or execute_url rule; X1's fetch must stay refused",
    )


@pytest.mark.parametrize(
    "target",
    ["{wt}/", "*", "regex:.*", "{wt}/x-job-other/"],
    ids=[
        "write_file(<tmp wt>/)",
        "write_file(*)",
        "write_file(regex:.*)",
        "write_file(<tmp wt>/x-job-other/)",
    ],
)
def test_k5_gemini_with_a_wider_write_rule_is_refused(desk, target):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    rule = f"write_file({target.format(wt=desk.wt)})"
    write_agy(desk, [f"write_file({grant})", rule])
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy} holds a write rule that reaches past {grant}: {rule}",
    )


def test_k5_gemini_with_its_grant_and_the_house_rules_is_admitted(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    write_agy(desk, [
        f"write_file({grant})",
        "read_file(/Users/cobalt/cobalt/docs/)",
        "command(cat *)",
        f"write_file({desk.wt}/agy-trial/scratch/toy-check-agy/)",
    ])
    done = desk.run(str(card), "--model", "gemini-4-argon-high")
    assert done.returncode == 0, done.stderr
    assert "MODEL: gemini-4-argon-high" in done.stdout.splitlines()[-1]


def test_k5_grok_reads_no_agy_settings(desk):
    desk.env["COBALT_AGY_SETTINGS"] = str(desk.tmp / "missing-agy-settings.json")
    done = desk.run(str(desk.card), "--model", "grok-4.7")
    assert done.returncode == 0, done.stderr


# ---- check of card 759 (agy-read-1018-check): findings O1, O3, house A 1 ----------------------


def test_check_o1_a_wide_write_rule_on_the_grant_line_is_refused(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    Path(desk.env["COBALT_AGY_SETTINGS"]).write_text(
        json.dumps({"permissions": {"allow": ["write_file(*)", f"write_file({grant})"]}}) + "\n")
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy} holds a write rule that reaches past {grant}: write_file(*)",
    )


def test_check_o3_an_empty_write_target_is_refused(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    write_agy(desk, [f"write_file({grant})", "write_file()"])
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy} holds a write rule that reaches past {grant}: write_file()",
    )


def test_k5_gemini_earlier_write_on_the_same_line_is_refused(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    agy_path = Path(desk.env["COBALT_AGY_SETTINGS"])
    agy_path.write_text(
        '{"permissions": {"allow": ["write_file(*)", "write_file(' + grant + ')"]}}\n'
    )
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy_path} holds a write rule that reaches past {grant}: write_file(*)",
    )
