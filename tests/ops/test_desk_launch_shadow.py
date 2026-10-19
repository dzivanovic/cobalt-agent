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


def test_k5_gemini_without_its_worktree_grant_is_added(desk):
    """Card 800 G1: a missing grant is the launcher's to add; the dry run says so and writes nothing."""
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    write_agy(desk, [f"read_file({grant})"])
    agy = desk.env["COBALT_AGY_SETTINGS"]
    before = Path(agy).read_bytes()
    done = desk.run(str(card), "--model", "gemini-4-argon-high")
    assert done.returncode == 0, done.stderr
    assert f"GRANT: would add write_file({grant}) to {agy}" in done.stderr
    assert Path(agy).read_bytes() == before


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
    ["{wt}/", "*", "regex:.*"],
    ids=[
        "write_file(<tmp wt>/)",
        "write_file(*)",
        "write_file(regex:.*)",
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


# ---- card 2026-10-18 800 G1-G3: the launcher adds and removes the grant (R1942) --------------


HOUSE = ["read_file(/Users/cobalt/cobalt/docs/)", "command(cat *)"]


def fake_claude(desk: Desk, agents: str = "[]", agents_rc: int = 0, bg_rc: int = 0) -> None:
    """The stub on PATH: `claude agents --json` prints `agents` (exit `agents_rc`); a launch exits `bg_rc`."""
    write_exe(desk.tmp / "bin" / "claude",
              f"if [ \"$1\" = \"agents\" ]; then printf '%s\\n' '{agents}'; exit {agents_rc}; fi\n"
              f'printf "%s | %s\\n" "$PWD" "$*" >> "{desk.calls}"\nexit {bg_rc}\n')


def sweep(desk: Desk, dry: bool = False) -> subprocess.CompletedProcess:
    env = dict(desk.env, DESK_LAUNCH_DRY="1") if dry else desk.env
    return subprocess.run(
        ["sh", str(desk.launch), "grant-sweep"], env=env, cwd=desk.tmp,
        capture_output=True, text=True, timeout=120,
    )


def gate(name: str) -> str:
    return json.dumps([{"id": "s1", "pid": 1, "name": name, "status": "idle", "state": "idle"}])


def test_g1_the_717_shape_launches_and_holds_its_grant(desk):
    card = signed_gemini(desk)
    grant = f"write_file({desk.wt}/x-job-gemini/)"
    write_agy(desk, HOUSE)
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 0, done.stderr
    calls = desk.calls.read_text().splitlines()
    assert len(calls) == 1 and "MODEL: gemini-4-argon-high" in calls[0]
    assert desk.agy.read_text().count(f'"{grant}"') == 1
    assert f"GRANT: added {grant} to {desk.agy}" in done.stderr


def test_g1_a_dry_run_writes_nothing(desk):
    card = signed_gemini(desk)
    write_agy(desk, HOUSE)
    before = desk.agy.read_bytes()
    done = desk.run(str(card), "--model", "gemini-4-argon-high")
    assert done.returncode == 0, done.stderr
    assert f"GRANT: would add write_file({desk.wt}/x-job-gemini/) to {desk.agy}" in done.stderr
    assert desk.agy.read_bytes() == before


def test_g1_a_failed_launch_removes_the_grant(desk):
    card = signed_gemini(desk)
    grant = f"write_file({desk.wt}/x-job-gemini/)"
    write_agy(desk, HOUSE)
    before = desk.agy.read_bytes()
    fake_claude(desk, bg_rc=1)
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 1, done.stderr
    assert f"GRANT: added {grant} to {desk.agy}" in done.stderr
    assert f"GRANT: removed {grant} from {desk.agy} (launch failed)" in done.stderr
    assert desk.agy.read_bytes() == before


def test_g1_invalid_json_is_refused_and_not_written(desk):
    card = signed_gemini(desk)
    desk.agy.write_text('{"permissions": {"allow": [')
    before = desk.agy.read_bytes()
    refused(desk.run(str(card), "--model", "gemini-4-argon-high", dry=False),
            f"shadow: gemini: {desk.agy} is not valid JSON with a permissions.allow list; nothing written")
    assert desk.agy.read_bytes() == before
    assert not desk.calls.exists()


def test_g1_an_inline_allow_list_is_refused(desk):
    card = signed_gemini(desk)
    desk.agy.write_text('{"permissions": {"allow": ["read_file(/x/)"]}}\n')
    before = desk.agy.read_bytes()
    refused(desk.run(str(card), "--model", "gemini-4-argon-high", dry=False),
            f"shadow: gemini: {desk.agy}: permissions.allow is not one rule per line; nothing written")
    assert desk.agy.read_bytes() == before
    assert not desk.calls.exists()


def test_g1_a_job_that_is_not_its_worktree_is_refused(desk):
    signed_gemini(desk)
    card = desk.card_for(
        "gemini", WORKTREE="x-job-other",
        REPORT=str(desk.wt / "x-job-other" / "docs" / "40 - DevDocs" / "reports" / "x-job-other-build.md"))
    before = desk.agy.read_bytes()
    refused(desk.run(str(card), "--model", "gemini-4-argon-high", dry=False),
            "shadow: gemini: JOB 'x-job-gemini' is not its WORKTREE 'x-job-other' "
            "(the gate seat x-job-other-gate names the rule's owner)")
    assert desk.agy.read_bytes() == before


def test_g2_a_live_gemini_rule_refuses_the_launch(desk):
    card = signed_gemini(desk)
    other = f"write_file({desk.wt}/x-job-other/)"
    write_agy(desk, [other, *HOUSE])
    fake_claude(desk, agents=gate("x-job-other-gate"))
    before = desk.agy.read_bytes()
    refused(desk.run(str(card), "--model", "gemini-4-argon-high", dry=False),
            f"shadow: gemini: {desk.agy} holds {other} and x-job-other-gate is live: "
            "one Gemini build at a time (card 759 serial rule)")
    assert desk.agy.read_bytes() == before
    assert not desk.calls.exists()


def test_g2_an_orphan_is_removed_first_and_recorded(desk):
    card = signed_gemini(desk)
    grant = f"write_file({desk.wt}/x-job-gemini/)"
    other = f"write_file({desk.wt}/x-job-other/)"
    write_agy(desk, [other, *HOUSE])
    dry = desk.run(str(card), "--model", "gemini-4-argon-high")
    assert dry.returncode == 0, dry.stderr
    assert f"ORPHAN: would remove {other} from {desk.agy} (no live x-job-other-gate)" in dry.stderr
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 0, done.stderr
    removed = f"ORPHAN: removed {other} from {desk.agy} (no live x-job-other-gate)"
    assert removed in done.stderr
    assert done.stderr.index(removed) < done.stderr.index(f"GRANT: added {grant}")
    rules = json.loads(desk.agy.read_text())["permissions"]["allow"]
    assert rules == [grant, *HOUSE]


def test_g2_a_dotted_orphan_never_touches_the_grant(desk):
    """THE REGEX CASE: `x.job-gemini` read as a regex matches `x-job-gemini`; every match is a fixed string."""
    card = signed_gemini(desk)
    grant = f"write_file({desk.wt}/x-job-gemini/)"
    dotted = f"write_file({desk.wt}/x.job-gemini/)"
    write_agy(desk, [grant, dotted, *HOUSE])
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 0, done.stderr
    assert json.loads(desk.agy.read_text())["permissions"]["allow"] == [grant, *HOUSE]
    write_agy(desk, [dotted, grant, *HOUSE])
    fake_claude(desk, agents=gate("x-job-gemini-gate"))
    done = sweep(desk)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == "GRANT-SWEEP: 1 removed, 1 live"
    assert json.loads(desk.agy.read_text())["permissions"]["allow"] == [grant, *HOUSE]


def test_g2_grant_sweep_removes_orphans_and_keeps_live(desk):
    live = f"write_file({desk.wt}/x-job-live/)"
    dead = f"write_file({desk.wt}/x-job-dead/)"
    write_agy(desk, [live, dead, *HOUSE])
    fake_claude(desk, agents=gate("x-job-live-gate"))
    before = desk.agy.read_bytes()
    dry = sweep(desk, dry=True)
    assert dry.returncode == 0, dry.stderr
    assert dry.stdout.splitlines() == [
        f"ORPHAN: would remove {dead} from {desk.agy} (no live x-job-dead-gate)",
        "GRANT-SWEEP: 1 would be removed, 1 live",
    ]
    assert desk.agy.read_bytes() == before
    fake_claude(desk, agents_rc=1)
    bad = sweep(desk)
    assert bad.returncode == 1 and "REFUSED: " in bad.stderr, bad.stdout + bad.stderr
    assert desk.agy.read_bytes() == before
    fake_claude(desk, agents=gate("x-job-live-gate"))
    done = sweep(desk)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [
        f"ORPHAN: removed {dead} from {desk.agy} (no live x-job-dead-gate)",
        "GRANT-SWEEP: 1 removed, 1 live",
    ]
    assert json.loads(desk.agy.read_text())["permissions"]["allow"] == [live, *HOUSE]


def test_g3_the_file_is_byte_equal_but_for_the_one_rule(desk):
    card = signed_gemini(desk)
    trial = f"write_file({desk.wt}/agy-trial/scratch/toy-check-agy/)"
    b = (
        "{\n"
        '  "model": "constructed",\n'
        '  "ui": "café",\n'
        '  "permissions": {\n'
        '    "allow": [\n'
        '      "read_file(/Users/cobalt/cobalt/docs/)",\n'
        '      "command(cat *)",\n'
        f'      "{trial}"\n'
        "    ]\n"
        "  },\n"
        '  "trustedWorkspaces": [\n'
        '    "/Users/cobalt/cobalt-wt/agy-trial"\n'
        "  ]\n"
        "}\n"
    ).encode("utf-8")
    desk.agy.write_bytes(b)
    desk.agy.chmod(0o640)
    line = f'      "write_file({desk.wt}/x-job-gemini/)",\n'.encode()
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 0, done.stderr
    a = desk.agy.read_bytes()
    assert a.count(line) == 1 and a.replace(line, b"", 1) == b
    assert desk.agy.stat().st_mode & 0o777 == 0o640
    swept = sweep(desk)
    assert swept.returncode == 0, swept.stderr
    assert swept.stdout.splitlines()[-1] == "GRANT-SWEEP: 1 removed, 0 live"
    assert desk.agy.read_bytes() == b
    assert desk.agy.stat().st_mode & 0o777 == 0o640
    fake_claude(desk, bg_rc=1)
    failed = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert failed.returncode == 1, failed.stderr
    assert desk.agy.read_bytes() == b
    assert desk.agy.stat().st_mode & 0o777 == 0o640


def test_g1_truncated_json_that_mentions_read_url_is_the_json_refusal(desk):
    card = signed_gemini(desk)
    desk.agy.write_text('{"permissions": {"allow": ["read_url(*)"]')
    before = desk.agy.read_bytes()
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high", dry=False),
        f"shadow: gemini: {desk.agy} is not valid JSON with a permissions.allow list; nothing written",
    )
    assert desk.agy.read_bytes() == before
    assert not desk.calls.exists()


# ---- card 2026-10-19 827 C2: the Gemini gate seat starts in its worktree (a pin, R2011) --------


def test_c2_the_gemini_gate_seat_starts_in_its_worktree(desk):
    card = signed_gemini(desk)
    write_agy(desk, HOUSE)
    wt = desk.wt / "x-job-gemini"
    dry = desk.run(str(card), "--model", "gemini-4-argon-high")
    assert dry.returncode == 0, dry.stderr
    out = dry.stdout.splitlines()
    assert out[-2] == f"cd {wt}", out
    assert out[-1].startswith("claude --bg ") and "MODEL: gemini-4-argon-high" in out[-1]
    done = desk.run(str(card), "--model", "gemini-4-argon-high", dry=False)
    assert done.returncode == 0, done.stderr
    cwd, args = desk.calls.read_text().splitlines()[0].split(" | ", 1)
    assert Path(cwd).resolve() == wt.resolve()
    assert "MODEL: gemini-4-argon-high" in args


# ---- card 2026-10-19 827 T1: kind x1-copy, the X1 leg's agy transcript (R2015) ---------------

ID = "00000000-0000-4000-8000-000000000001"
ID2 = "00000000-0000-4000-8000-000000000002"
CANARY = '{"step": 6, "status": "DONE", "output": "X1_CANARY=not-a-secret"}\n'
SOFT = 'I0101 00:00:00.000000 1 print.go:88] Print mode: soft-denying tool confirmation "ViewFile" at step 6'


def x1copy(desk: Desk, wt: str, leg: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(desk.launch), "x1-copy", wt, leg],
        env=dict(desk.env, COBALT_AGY_HOME=str(desk.tmp / "agy-home")), cwd=desk.tmp,
        capture_output=True, text=True, timeout=120,
    )


def x1wt(desk: Desk) -> Path:
    wt = desk.wt / "x-job-gemini"
    wt.mkdir(exist_ok=True)
    return wt


def agy_run(desk: Desk, workspace: str | list[str], ids: tuple[str, ...] = (ID,), transcript: bool = True) -> Path:
    """A constructed agy home: `cli.log` a link to the run's log, one `workspaceDirs=[…]` line per
    list given, one `Created conversation` line per id, one soft-denying line; the transcript."""
    home = desk.tmp / "agy-home"
    log = home / "log" / "cli-20260101_000000.log"
    log.parent.mkdir(parents=True, exist_ok=True)
    lists = [workspace] if isinstance(workspace, str) else workspace
    lines = [f"I0101 00:00:00.000000 1 server.go:470] workspaceDirs=[{w}]" for w in lists]
    lines += [f"I0101 00:00:00.000000 1 server.go:1199] Created conversation {i} (backend=BACKEND_TYPE_UNSPECIFIED)"
              for i in ids]
    lines.append(SOFT)
    log.write_text("\n".join(lines) + "\n")
    link = home / "cli.log"
    if link.is_symlink():
        link.unlink()
    link.symlink_to("log/cli-20260101_000000.log")
    if transcript:
        src = home / "brain" / ids[0] / ".system_generated" / "logs" / "transcript.jsonl"
        src.parent.mkdir(parents=True, exist_ok=True)
        src.write_text(CANARY)
    return home


def nothing_written(desk: Desk, done: subprocess.CompletedProcess, text: str, before: list[str]) -> None:
    refused(done, f"x1-copy: {text}")
    assert sorted(os.listdir(desk.wt / "x-job-gemini")) == before


@pytest.mark.parametrize("twice", [False, True], ids=["<wt>", "<wt> <wt>"])
def test_t1_copies_the_transcript_of_its_own_workspace(desk, twice):
    wt = x1wt(desk)
    home = agy_run(desk, f"{wt} {wt}" if twice else str(wt))
    done = x1copy(desk, "x-job-gemini", "0c")
    assert done.returncode == 0, done.stderr
    copy = wt / "x1-0c.transcript"
    src = home / "brain" / ID / ".system_generated" / "logs" / "transcript.jsonl"
    assert copy.read_bytes() == src.read_bytes()
    grep = subprocess.run(["grep", "-c", "-F", "X1_CANARY", str(copy)], capture_output=True, text=True)
    assert grep.stdout == "1\n"
    assert (wt / "x1-0c.log").read_text() == f"conversation {ID}\n{SOFT}\n"
    assert done.stdout.splitlines() == [
        f"X1-COPY: 0c conversation {ID}",
        f"X1-COPY: 0c workspace {wt}",
        f"X1-COPY: 0c copied {copy} ({len(CANARY)} bytes)",
        "X1-COPY: 0c soft-denying 1",
    ]


@pytest.mark.parametrize(
    "shape", ["x1-canary", "x1-canary and wt", "wt and other", "below wt", "wt root", "empty"],
)
def test_t1_a_foreign_workspace_is_refused(desk, shape):
    wt = x1wt(desk)
    workspace = {
        "x1-canary": f"{desk.wt}/x1-canary",
        "x1-canary and wt": f"{desk.wt}/x1-canary {wt}",
        "wt and other": f"{wt} {desk.wt}/other-0101",
        "below wt": f"{wt}/docs",
        "wt root": str(desk.wt),
        "empty": "",
    }[shape]
    agy_run(desk, workspace)
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0c"), f"0c cli.log names workspace {workspace}, not {wt}", [])


@pytest.mark.parametrize("n", [0, 2])
def test_t1_zero_or_two_workspace_lines_are_refused(desk, n):
    wt = x1wt(desk)
    agy_run(desk, [str(wt)] * n)
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0c"), f"0c cli.log holds {n} workspaceDirs= lines", [])


def test_t1_a_missing_transcript_is_refused(desk):
    wt = x1wt(desk)
    home = agy_run(desk, str(wt), transcript=False)
    path = home / "brain" / ID / ".system_generated" / "logs" / "transcript.jsonl"
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0c"), f"0c no transcript at {path}", [])


def test_t1_no_cli_log_is_refused(desk):
    x1wt(desk)
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0c"), "0c no cli.log at", [])


@pytest.mark.parametrize("ids", [(), (ID, ID2)], ids=["0", "2"])
def test_t1_no_or_two_conversations_is_refused(desk, ids):
    wt = x1wt(desk)
    agy_run(desk, str(wt), ids=ids, transcript=False)
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0c"), f"0c cli.log holds {len(ids)} Created conversation lines", [])


def test_t1_an_id_that_is_not_36_hex_characters_is_refused(desk):
    wt = x1wt(desk)
    agy_run(desk, str(wt), ids=("00000000-0000-4000-8000-00000000000G",), transcript=False)
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0c"), "0c conversation id", [])


def test_t1_a_stale_log_is_refused(desk):
    wt = x1wt(desk)
    agy_run(desk, str(wt))
    (wt / "x1-0a.log").write_text(f"conversation {ID}\n")
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0b"), f"0b stale: {wt}/x1-0a.log", ["x1-0a.log"])


@pytest.mark.parametrize("bad", ["leg 0g", "../x", "x1-canary", "link"])
def test_t1_a_bad_leg_or_worktree_is_refused(desk, bad):
    wt = x1wt(desk)
    agy_run(desk, str(wt))
    (desk.wt / "x1-canary").mkdir()
    (desk.wt / "x-link").symlink_to(wt)
    name, leg = {"leg 0g": ("x-job-gemini", "0g"), "../x": ("../x", "0c"),
                 "x1-canary": ("x1-canary", "0c"), "link": ("x-link", "0c")}[bad]
    nothing_written(desk, x1copy(desk, name, leg), "", [])
    assert os.listdir(desk.wt / "x1-canary") == []


@pytest.mark.parametrize("kind", ["transcript", "log"])
def test_t1_an_existing_copy_is_refused(desk, kind):
    wt = x1wt(desk)
    agy_run(desk, str(wt))
    (wt / f"x1-0c.{kind}").write_text("earlier\n")
    nothing_written(desk, x1copy(desk, "x-job-gemini", "0c"), f"0c {wt}/x1-0c.{kind} exists", [f"x1-0c.{kind}"])
    assert (wt / f"x1-0c.{kind}").read_text() == "earlier\n"


@pytest.mark.parametrize("args", [(), ("x-job-gemini",), ("x-job-gemini", "0c", "extra")],
                         ids=["alone", "one", "three"])
def test_t1_a_wrong_argument_count_is_refused(desk, args):
    wt = x1wt(desk)
    agy_run(desk, str(wt))
    done = subprocess.run(
        ["sh", str(desk.launch), "x1-copy", *args],
        env=dict(desk.env, COBALT_AGY_HOME=str(desk.tmp / "agy-home")), cwd=desk.tmp,
        capture_output=True, text=True, timeout=120,
    )
    nothing_written(desk, done, "", [])


def test_t1_a_missing_worktree_directory_is_refused(desk):
    x1wt(desk)
    agy_run(desk, f"{desk.wt}/x-job-never")
    done = x1copy(desk, "x-job-never", "0c")
    refused(done, "x1-copy: ")
    assert not (desk.wt / "x-job-never").exists()


def test_t1_runs_under_a_desk_size_guard_that_exits_7(desk):
    wt = x1wt(desk)
    agy_run(desk, str(wt))
    write_exe(desk.launch.parent / "desk-context.sh", "exit 7\n")
    done = x1copy(desk, "x-job-gemini", "0c")
    assert done.returncode == 0, done.stderr
    assert (wt / "x1-0c.transcript").read_text() == CANARY
    assert sweep(desk).returncode == 7
