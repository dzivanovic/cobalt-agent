"""Card 2026-10-15/583 band-routing-1015, rows B1-B6 (his 2026-10-15 R1532, routing B).

B1, B2 and B4 read the real hubs and pin only the lines their own row adds, found by content
(brain R1472). B3 runs ops/desk/desk-launch.sh from a tmp copy against a tmp repo (the `Desk` of
tests/ops/test_desk_launch_shadow.py, copied here): a constructed BUILD-HUB.md line, a constructed
SHADOW-HUB.md whose `## BUILDERS` holds the three builder rows and the band table, and cards dated
2026-10-16 (on or after BAND_FROM) or 2026-01-02 (older). B5 runs the launcher's check arm and
ops/desk/preflight.sh on a routed card's worktree holding the untracked SHADOW-INSTRUCTIONS.md.
B6 runs ops/desk/bare-guard.py as the hook runs it, for the shadow gate seat's writes. `claude`
is a stub; nothing here launches a seat or reads a real card, report or `.env`.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
PREFLIGHT = REPO / "ops" / "desk" / "preflight.sh"
GUARD = REPO / "ops" / "desk" / "bare-guard.py"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

NEW_DAY = "2026-10-16"  # on BAND_FROM
OLD_DAY = "2026-01-02"  # before it
BAND_REFUSAL = "REFUSED: incomplete card: BAND must be LOW, MID or HIGH"


def lines_of(name: str) -> list[str]:
    return (HUBS / name).read_text(encoding="utf-8").splitlines()


def one_index(ls: list[str], head: str) -> int:
    hits = [i for i, ln in enumerate(ls) if ln.startswith(head)]
    assert len(hits) == 1, (head, hits)
    return hits[0]


def section(ls: list[str], name: str) -> list[str]:
    """The lines under `## <name>` up to the next `## ` heading (test_shadow_hub_file.section)."""
    start = one_index(ls, f"## {name}")
    out = []
    for ln in ls[start + 1:]:
        if ln.startswith("## "):
            break
        out.append(ln)
    return out


# ---- B1: CARD.md names BAND --------------------------------------------------------------------


def test_b1_card_md_names_band_once_in_the_header_table_and_once_in_its_paragraph():
    ls = lines_of("CARD.md")
    rows = [i for i, ln in enumerate(ls) if ln.startswith("| `BAND` |")]
    assert len(rows) == 1
    row = ls[rows[0]]
    for word in ("LOW", "MID", "HIGH", "R1532", "higher band"):
        assert word in row, word
    assert one_index(ls, "| `DB` |") < rows[0] < one_index(ls, "| `RULINGS` |")
    para = one_index(ls, "BAND is set by the drafter")
    assert one_index(ls, "| `PROOF TEST` |") < para < one_index(ls, "## THE BODY")
    for word in ("2026-10-16", "REFUSED: incomplete card: BAND must be LOW, MID or HIGH", "condition 3"):
        assert word in ls[para], word


def test_b1_control_the_other_header_rows_stand():
    ls = lines_of("CARD.md")
    for key in ("JOB", "LADDER", "HOUSE B", "DB", "RULINGS"):
        assert sum(ln.startswith(f"| `{key}` |") for ln in ls) == 1, key


# ---- B2: SHADOW-HUB.md carries the band table and the ledger rule ------------------------------


def test_b2_builders_holds_the_band_table_once():
    sect = section(lines_of("SHADOW-HUB.md"), "BUILDERS")
    got = {}
    for band in ("LOW", "MID", "HIGH"):
        hits = [ln for ln in sect if ln.startswith(f"| {band} |")]
        assert len(hits) == 1, (band, hits)
        got[band] = hits[0]
    for band in ("LOW", "MID"):
        assert "grok-4.7" in got[band] and "gpt-5.6-terra" in got[band], got[band]
    assert "Opus 5.5" in got["HIGH"]
    assert "grok" not in got["HIGH"] and "terra" not in got["HIGH"], got["HIGH"]
    assert "R1532" in "\n".join(sect)


def test_b2_results_table_carries_the_ruling_and_the_ledger_triggers():
    text = "\n".join(section(lines_of("SHADOW-HUB.md"), "RESULTS TABLE"))
    assert "R1532" in text
    assert "n = 10" in text
    assert "two cards in a row" in text
    assert "Routing takes effect only on his word" not in text


def test_b2_control_the_three_builder_rows_stand():
    sect = section(lines_of("SHADOW-HUB.md"), "BUILDERS")
    rows = [ln for ln in sect if ln.startswith("| `")]
    ids = sorted(ln.split("|")[1].strip().strip("`") for ln in rows)
    assert ids == sorted(["grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra"])
    assert "claude-opus-5-5" not in "\n".join(sect)


# ---- B4: BUILD-HUB.md names the band routing before its launch line ----------------------------


def test_b4_build_hub_names_the_band_routing_once_before_the_launch_line():
    ls = lines_of("BUILD-HUB.md")
    hits = [i for i, ln in enumerate(ls) if ln.startswith("BAND (his 2026-10-15 R1532):")]
    assert len(hits) == 1
    para = ls[hits[0]]
    for word in ("SHADOW-HUB.md", "LOW or MID", "desk-launch.sh build <card>"):
        assert word in para, word
    assert one_index(ls, "(1) it enters") < hits[0] < one_index(ls, "claude --bg ")


def test_b4_control_the_launch_line_and_the_model_line_stand():
    ls = lines_of("BUILD-HUB.md")
    line = ls[one_index(ls, "claude --bg ")]
    assert line.count("--model claude-opus-5-5") == 1
    assert sum(ln.startswith("MODEL: Opus 5.5") for ln in ls) == 1


# ---- the B3 harness (the Desk of test_desk_launch_shadow.py, copied by content) ----------------

SHADOW_HUB_PATH = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"
BUILD_HUB_PATH = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"
SIGN = "«" + "SIGN"
UNSIGNED = f"NEEDS HIS SIGN-OFF {SIGN}: his row»"
SIGNED = "HIS RULING · APPROVED 2026-01-02 R1"
ALLOW = {
    "grok-4.7": "Bash(grok -m grok-4.7 --sandbox cobalt-job *)",
    "claude-sonnet-5-5": "Bash(claude -p --model claude-sonnet-5-5 *)",
    "gpt-5.6-terra": "Bash(codex exec --skip-git-repo-check -m gpt-5.6-terra -s workspace-write *)",
}
SLUG = {"grok-4.7": "grok", "claude-sonnet-5-5": "sonnet", "gpt-5.6-terra": "terra"}
COMMAND = {
    "grok-4.7": 'grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/<worktree>/**)" -p "<pass prompt>"',
    "claude-sonnet-5-5": 'claude -p --model claude-sonnet-5-5 --permission-mode dontAsk "<pass prompt>"',
    "gpt-5.6-terra": 'codex exec --skip-git-repo-check -m gpt-5.6-terra -s workspace-write -C /Users/cobalt/cobalt-wt/<worktree> "<pass prompt>" < /dev/null',
}
BAND_TABLE = (
    "| band | builder | backup |\n|---|---|---|\n"
    "| LOW | `grok-4.7` | `gpt-5.6-terra` |\n"
    "| MID | `grok-4.7` | `gpt-5.6-terra` |\n"
    "| HIGH | Opus 5.5 (the `BUILD-HUB.md` line, unchanged) | none; Grok only on his word, per card |\n"
    '| routing, hubs, preflights | Sonnet 5.5 ("for now") | none |\n'
)
BUILD_LINE = (
    f"claude --bg \"Read '{BUILD_HUB_PATH}' and follow it exactly. CARD: '<card>'\" "
    "--model claude-opus-5-5 --permission-mode dontAsk --remote-control <job>-build --name <job>-build "
    '--allowedTools "Read" "Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)" '
    '--disallowedTools "AskUserQuestion" "EnterWorktree" --add-dir /Users/cobalt/cobalt-wt'
)


def shadow_line(mode: str = "--permission-mode dontAsk") -> str:
    return (
        f"claude --bg \"Read '{SHADOW_HUB_PATH}' and follow it exactly. CARD: '<card>' MODEL: <model>\" "
        f"--model claude-opus-5-5 {mode} --remote-control <job>-gate --name <job>-gate "
        '--allowedTools "Read" "Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)" <builder allow> '
        '--disallowedTools "AskUserQuestion" "EnterWorktree" --add-dir /Users/cobalt/cobalt-wt'
    )


def shadow_hub_text(line: str, signed: tuple[str, ...] = ("grok-4.7", "gpt-5.6-terra")) -> str:
    rows = "".join(
        f"| `{m}` | `{SLUG[m]}` | `{ALLOW[m]}` | `{COMMAND[m]}` | {SIGNED if m in signed else UNSIGNED} |\n"
        for m in ALLOW
    )
    return (
        f"# SHADOW-HUB (constructed, installed)\n\n{line}\n\n## BUILDERS\n\n"
        f"| id | slug | builder allow | builder command | SIGN |\n|---|---|---|---|---|\n{rows}\n"
        f"BAND ROUTING (constructed):\n\n{BAND_TABLE}\n## PROCEDURE\n\nconstructed\n"
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
        for day in (NEW_DAY, OLD_DAY):
            (self.prompts / day).mkdir(parents=True)
        self.reports.mkdir(parents=True)
        (self.prompts / "BUILD-HUB.md").write_text(f"# BUILD-HUB (constructed, installed)\n\n{BUILD_LINE}\n")
        self.shadow = self.prompts / "SHADOW-HUB.md"
        self.shadow.write_text(shadow_hub_text(shadow_line()))
        (self.reports / "cto-2026-01-02.md").write_text(
            "| R1 | 07:00 ET | HIS RULING (constructed). | HIS RULING · APPROVED |\n")
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")
        self.base = git(self.repo, "rev-parse", "--short=8", "HEAD")
        ops = tmp_path / "ops"
        ops.mkdir()
        self.launch = ops / "desk-launch.sh"
        shutil.copy(LAUNCH, self.launch)
        write_exe(ops / "desk-context.sh", "exit 0\n")
        self.calls = tmp_path / "claude-calls"
        write_exe(tmp_path / "bin" / "claude",
                  'if [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
                  f'printf "%s | %s\\n" "$PWD" "$*" >> "{self.calls}"\nexit 0\n')
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}", **GIT_ENV,
        )

    def report_for(self, job: str) -> str:
        return str(self.wt / job / "docs" / "40 - DevDocs" / "reports" / f"{job}-build.md")

    def card_for(self, band: str | None, day: str = NEW_DAY, job: str = "x-band", **over: str | None) -> Path:
        keys = {
            "JOB": job,
            "LADDER": "OFF-LADDER — constructed",
            "BRANCH": f"ops/{job}",
            "WORKTREE": job,
            "BASE": self.base,
            "TIP": "",
            "REPORT": self.report_for(job),
            "RULINGS": "2026-01-02 R1",
            "BAND": band,
        }
        keys.update(over)
        card = self.prompts / day / f"01-{job}-card.md"
        head = "".join(f"{k}: {v}\n" if v else f"{k}:\n" for k, v in keys.items() if v is not None)
        card.write_text(head + "\n## ROWS\n\n| row | what |\n|---|---|\n| X1 | constructed |\n")
        self.commit(f"card {job}")
        return card

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "--allow-empty", "-m", msg)

    def set_shadow(self, text: str) -> None:
        self.shadow.write_text(text)
        self.commit("hub")

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


# ---- B3: desk-launch.sh build <card> picks the builder by BAND ---------------------------------


@pytest.mark.parametrize("band", ["LOW", "MID"])
def test_b3_a_low_or_mid_card_launches_the_shadow_gate_seat_with_the_band_builder(desk, band):
    """(1) LOW and (2) MID: the build kind re-enters as the gate seat with the band's builder."""
    done = desk.run("build", str(desk.card_for(band)))
    assert done.returncode == 0, done.stderr
    assert "MODEL: grok-4.7" in done.stdout, done.stdout
    assert "--remote-control x-band-gate" in done.stdout
    assert f"BAND: {band} → grok-4.7 (backup gpt-5.6-terra)" in done.stderr, done.stderr


@pytest.mark.parametrize("band", [None, "low", "LOWISH", ""])
def test_b3_a_missing_or_bad_band_is_refused_on_a_new_card(desk, band):
    """(3) no BAND line, a lower-case value, a longer word, an empty value: refused, no launch."""
    done = desk.run("build", str(desk.card_for(band)), dry=False)
    assert done.returncode == 1, done.stdout + done.stderr
    assert BAND_REFUSAL in done.stderr, done.stderr
    assert not desk.calls.exists()


@pytest.mark.parametrize("band,model", [("HIGH", "grok-4.7"), (None, "grok-4.7"), ("LOW", "claude-sonnet-5-5")])
def test_b3_routed_flag_is_refused_off_its_band(desk, band, model):
    """(4) --routed on a HIGH card, on a card with no BAND, and with an id that is no band id."""
    refused(desk.run("shadow", str(desk.card_for(band)), "--model", model, "--routed"),
            "shadow: --routed needs a card with BAND LOW or MID and its builder or backup id")


def test_b3_a_routed_launch_keeps_the_signed_row_and_the_mode_refusals(desk):
    """(5) the routed launch still meets the shadow arm's signed-row and mode refusals."""
    card = desk.card_for("LOW")
    desk.set_shadow(shadow_hub_text(shadow_line(), signed=()))
    refused(desk.run("build", str(card)), "shadow: model grok-4.7: builder line not signed")
    desk.set_shadow(shadow_hub_text(shadow_line() + " --permission-mode bypassPermissions"))
    refused(desk.run("build", str(card)), "shadow: bypassPermissions on the line (L55)")


def test_b3_a_resume_step_on_a_routed_card_is_refused(desk):
    """(6) a resume step is not carried to the gate seat."""
    done = desk.run("build", str(desk.card_for("LOW")), "STEP-X")
    refused(done, "BAND routed builds start fresh")


def test_b3_the_backup_is_a_hand_launch(desk):
    """(7) the desk's hand launch of the band's backup id."""
    done = desk.run("shadow", str(desk.card_for("MID")), "--model", "gpt-5.6-terra", "--routed")
    assert done.returncode == 0, done.stderr
    assert "MODEL: gpt-5.6-terra" in done.stdout
    assert "--remote-control x-band-gate" in done.stdout


def test_b3_a_routed_launch_is_a_real_build_not_a_shadow(desk):
    """(8) the card's own ops/ BRANCH and its REPORT; the build kind's re-entry prints the same."""
    card = desk.card_for("LOW")
    report = desk.report_for("x-band")
    for args in (("shadow", str(card), "--model", "grok-4.7", "--routed"), ("build", str(card))):
        done = desk.run(*args)
        assert done.returncode == 0, done.stderr
        printed = done.stdout + done.stderr
        assert "worktree add -b ops/x-band " in done.stdout, done.stdout
        assert "shadow/" not in done.stdout
        assert report in printed, printed


def test_b3_control_a_high_card_builds_on_the_build_hub_line(desk):
    done = desk.run("build", str(desk.card_for("HIGH")))
    assert done.returncode == 0, done.stderr
    assert "--model claude-opus-5-5" in done.stdout
    assert "--remote-control x-band-build" in done.stdout
    assert "MODEL:" not in done.stdout


def test_b3_control_an_old_card_with_no_band_builds_as_before(desk):
    done = desk.run("build", str(desk.card_for(None, day=OLD_DAY)))
    assert done.returncode == 0, done.stderr
    assert "--model claude-opus-5-5" in done.stdout
    assert "MODEL:" not in done.stdout
    assert "BAND:" not in done.stderr


def test_b3_control_shadow_without_routed_still_demands_its_own_header(desk):
    refused(desk.run("shadow", str(desk.card_for("LOW")), "--model", "grok-4.7"),
            "shadow: the card's header has no 'SHADOW OF:' line")


def test_o2_a_new_card_named_through_a_dot_folder_still_needs_its_band(desk):
    card = desk.card_for(None)
    odd = str(desk.prompts) + "/./" + str(card.relative_to(desk.prompts))
    done = desk.run("build", odd)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: the card path holds '/./' or '//'" in done.stderr, done.stderr


# ---- FR-1 (check O2): a card path holding '/./' or '//' is refused, naming the path ----------


def test_fr1_a_double_slash_card_path_is_refused_naming_it(desk):
    card = desk.card_for(None)
    odd = str(desk.prompts) + "//" + str(card.relative_to(desk.prompts))
    done = desk.run("build", odd)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: the card path holds '/./' or '//'" in done.stderr, done.stderr
    assert odd in done.stderr, done.stderr


def test_fr1_control_a_plain_card_path_still_launches(desk):
    done = desk.run("build", str(desk.card_for("LOW")))
    assert done.returncode == 0, done.stderr
    assert "BAND: LOW → grok-4.7" in done.stderr, done.stderr


@pytest.mark.xfail(strict=True, reason="check r2 O1: HELD, NOT FIXED — ops/desk/desk-launch.sh (fenced)")
def test_o1_a_routed_builds_watch_line_waits_on_the_build_stop_line(desk):
    done = desk.run("build", str(desk.card_for("LOW")))
    assert done.returncode == 0, done.stderr
    printed = done.stdout + done.stderr
    assert "desk-watch.sh shadow " not in printed, printed


@pytest.mark.xfail(strict=True, reason="check r2 O3: HELD, NOT FIXED — ops/desk/desk-launch.sh (fenced)")
def test_o3_a_card_outside_a_date_folder_still_needs_its_band(desk):
    card = desk.card_for(None)
    flat = desk.prompts / card.name
    flat.write_text(card.read_text())
    desk.commit("flat card")
    done = desk.run("build", str(flat))
    assert done.returncode == 1, done.stdout + done.stderr


@pytest.mark.xfail(strict=True, reason="check r2 G1: HELD, NOT FIXED — ops/desk/desk-launch.sh (fenced)")
def test_x5_routed_build_watch_does_not_wait_on_built(desk):
    done = desk.run("build", str(desk.card_for("LOW")))
    assert done.returncode == 0, done.stderr
    watch = [ln for ln in done.stderr.splitlines() if ln.startswith("WATCH:")]
    assert watch == [ln for ln in watch if "desk-watch.sh routed " in ln], watch


# ---- FR-2 (check O4): CHECK-HUB excepts a routed card from the untracked instructions file ----

FR2_HOLD = "is expected and recorded, not a finding"
FR2_CLAUSE = "on a shadow card or a routed card (BAND LOW or MID, dated on or after BAND_FROM)"


def test_fr2_check_hub_excepts_a_routed_card_from_the_untracked_instructions_file():
    hits = [ln for ln in lines_of("CHECK-HUB.md") if FR2_HOLD in ln]
    assert len(hits) == 2, hits
    assert sum(FR2_CLAUSE in ln for ln in hits) == 2


def test_fr2_control_the_two_lines_stay_where_they_are():
    ls = lines_of("CHECK-HUB.md")
    hits = [i for i, ln in enumerate(ls) if FR2_HOLD in ln]
    assert len(hits) == 2, hits
    assert one_index(ls, "## PREFLIGHT") < hits[0] < one_index(ls, "## 1. ")
    assert one_index(ls, "## 7. ") < hits[1] < one_index(ls, "## 8. ")


# ---- FR-3 (check O1): CARD.md requires BAND on a routed build's check card --------------------


def test_fr3_card_md_requires_band_on_a_routed_builds_check_card():
    ls = lines_of("CARD.md")
    cell = ls[one_index(ls, "| `BAND` |")].split("|")[3]
    for word in ("required", "LOW or MID", "copied"):
        assert word in cell, cell


# ---- FR-4 (check O3/G3): a routed fix round is a fresh HIGH card; the backup cites its rulings -


def test_fr4_the_routed_fix_round_is_a_fresh_high_card_and_the_backup_cites_its_rulings():
    ls = lines_of("SHADOW-HUB.md")
    line = ls[one_index(ls, "BAND ROUTING (")]
    for part in ("its own fresh job card with BAND: HIGH", "brain 2026-10-16, reading R1532's 'Terra backup'",
                 "R1471 (7) is recorded in the direction file", "never on a 429"):
        assert part in line, part
    assert "the fix round goes to the same builder" not in line


def test_fr4_control_the_band_table_stands():
    sect = section(lines_of("SHADOW-HUB.md"), "BUILDERS")
    for band in ("LOW", "MID", "HIGH"):
        assert sum(ln.startswith(f"| {band} |") for ln in sect) == 1, band


# ---- FR-5 (check G2): the shadow procedure excepts a routed card on its two lines --------------

FR5_NOTE = "(a routed card: no `SHADOW OF`; stop line `BUILT ·` as `:28`)"


def test_fr5_the_procedure_excepts_a_routed_card_on_its_two_lines():
    ls = lines_of("SHADOW-HUB.md")
    counts = [ls[one_index(ls, head)].count(FR5_NOTE) for head in ("2. PREFLIGHT:", "`SHADOW BUILT · job: ")]
    assert counts == [1, 1]


def test_fr5_control_the_shadow_stop_line_stays():
    ls = lines_of("SHADOW-HUB.md")
    assert "SHADOW BUILT · job: <JOB> · tip: <tip>" in ls[one_index(ls, "`SHADOW BUILT · job: ")]


# ---- FR-6 (check r2 O1/G1): a routed launch is watched as kind `routed` on <job>-gate ---------

WATCH_SH = REPO / "ops" / "desk" / "desk-watch.sh"
WAIT_SH = REPO / "ops" / "desk" / "wait-stop-line.sh"
ROUTED_STOP = "BUILT · job: x · tip: 1a2b3c4d | on 0f0e0d0c | rows: 1 of 1"
SHADOW_STOP = "SHADOW BUILT · job: x · tip: 1a2b3c4d | on 0f0e0d0c"
IDLE_GATE = "aaaa0001 · x-job-gate · ~/cobalt-wt/x-job · idle · idle"
IDLE_JOB_BUILD = "aaaa0001 · x-job-build · ~/cobalt-wt/x-job · idle · idle"


class RWatch:
    """desk-watch.sh and wait-stop-line.sh staged in <root>/ops with the worktree root re-pointed at
    <root>/wt (test_close_automation_1015.Watch's shape, copied by content); a desk-list.sh stub
    answering from <root>/list; a desk-done.sh stub that logs its arguments (when `done`); the
    worktree repo <root>/wt/x-job holding the report; a card dated on BAND_FROM."""

    def __init__(self, root: Path, done: bool, last: str, shadow: bool = False):
        root.mkdir(parents=True, exist_ok=True)
        self.ops = root / "ops"
        self.ops.mkdir()
        for src in (WATCH_SH, WAIT_SH):
            (self.ops / src.name).write_text(src.read_text().replace("/Users/cobalt/cobalt-wt", str(root / "wt")))
        (self.ops / "desk-context.sh").write_text("exit 0\n")
        self.list = root / "list"
        self.list.write_text("")
        (self.ops / "desk-list.sh").write_text(f'#!/bin/sh\ncat "{self.list}"\n')
        self.log = root / "done-log"
        if done:
            (self.ops / "desk-done.sh").write_text(f'printf "%s\\n" "$*" >> "{self.log}"\necho "CLOSED $1"\n')
        self.wt = root / "wt" / "x-job"
        self.wt.mkdir(parents=True)
        git(self.wt, "init", "-q", "-b", "main")
        self.report = self.wt / "docs" / "x-job-build.md"
        self.report.parent.mkdir()
        self.report.write_text(f"# x-job build\n\nbody\n\n{last}\n")
        git(self.wt, "add", "-A")
        git(self.wt, "commit", "-q", "-m", "report")
        self.card = root / "prompts" / NEW_DAY / "01-x-job-card.md"
        self.card.parent.mkdir(parents=True)
        head = "SHADOW OF: constructed\nBRANCH: shadow/x-job\n" if shadow else "BAND: LOW\nBRANCH: ops/x-job\n"
        self.card.write_text(
            f"JOB: x-job\nLADDER: OFF-LADDER\n{head}WORKTREE: x-job\nBASE: 1a2b3c4d\nTIP: 5e6f7a8b\n"
            f"REPORT: {self.report}\nRULINGS: 2026-01-02 R1\n\n## ROWS\n"
        )
        self.env = dict(os.environ, DESK_WATCH_POLL="1", DESK_WATCH_CLOSE_WAIT="2", **GIT_ENV)

    def rows(self, *rows: str) -> None:
        self.list.write_text("".join(r + "\n" for r in rows))

    def run(self, kind: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["sh", str(self.ops / "desk-watch.sh"), kind, str(self.card), "30"],
            env=self.env, capture_output=True, text=True, timeout=120,
        )

    def logged(self) -> list[str]:
        return self.log.read_text().splitlines() if self.log.exists() else []


def test_fr6_the_routed_watcher_admits_built_and_watches_the_gate_session(desk, tmp_path):
    card = desk.card_for("LOW")
    launched = desk.run("build", str(card))
    assert launched.returncode == 0, launched.stderr
    assert f'desk-watch.sh routed "{card}"' in launched.stderr, launched.stderr
    w = RWatch(tmp_path / "w1", done=False, last=ROUTED_STOP)
    done = w.run("routed")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[0] == ROUTED_STOP, done.stdout
    w = RWatch(tmp_path / "w2", done=False, last="(run in progress — next step under ## CONTINUE)")
    w.rows(IDLE_GATE)
    done = w.run("routed")
    assert done.returncode == 3, done.stdout + done.stderr
    assert done.stdout.startswith("IDLE: x-job-gate"), done.stdout
    w = RWatch(tmp_path / "w3", done=False, last="(run in progress — next step under ## CONTINUE)")
    w.rows(IDLE_JOB_BUILD)
    done = w.run("routed")
    assert done.returncode == 3, done.stdout + done.stderr
    assert done.stdout.startswith("GONE: x-job-gate"), done.stdout


def test_fr6_a_routed_closeout_hands_build_to_desk_done(tmp_path):
    w = RWatch(tmp_path / "w", done=True, last=ROUTED_STOP)
    w.rows(IDLE_GATE)
    done = w.run("routed")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[0] == ROUTED_STOP, done.stdout
    assert w.logged() == [f"aaaa0001 {w.report} build"], w.logged()


def test_fr6_control_a_shadow_card_closeout_still_passes_shadow(tmp_path):
    w = RWatch(tmp_path / "w", done=True, last=SHADOW_STOP, shadow=True)
    w.rows(IDLE_GATE)
    done = w.run("shadow")
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[0] == SHADOW_STOP, done.stdout
    assert w.logged() == [f"aaaa0001 {w.report} shadow"], w.logged()


def test_fr6_control_a_high_card_and_a_real_shadow_keep_their_watch(desk):
    high = desk.card_for("HIGH")
    done = desk.run("build", str(high))
    assert done.returncode == 0, done.stderr
    assert [ln for ln in done.stderr.splitlines() if ln.startswith("WATCH:")] == [
        f'WATCH: sh {desk.launch.parent}/desk-watch.sh build "{high}"']
    shadow = desk.card_for(None, day=OLD_DAY, job="x-band-grok", BRANCH="shadow/x-band-grok",
                           **{"SHADOW OF": str(high)})
    done = desk.run("shadow", str(shadow), "--model", "grok-4.7")
    assert done.returncode == 0, done.stderr
    assert [ln for ln in done.stderr.splitlines() if ln.startswith("WATCH:")] == [
        f'WATCH: sh {desk.launch.parent}/desk-watch.sh shadow "{shadow}"']


# ---- FR-7 (check r2 O3): a card outside $PROMPTS/<YYYY-MM-DD>/ is refused, naming it ----------


@pytest.mark.parametrize("where", ["01-x-band-card.md", "drafts/01-x-band-card.md",
                                   f"{NEW_DAY}/sub/01-x-band-card.md"])
def test_fr7_a_card_outside_a_date_folder_is_refused_naming_it(desk, where):
    card = desk.card_for("LOW")
    odd = desk.prompts / where
    odd.parent.mkdir(parents=True, exist_ok=True)
    odd.write_text(card.read_text())
    desk.commit("odd card")
    done = desk.run("build", str(odd), dry=False)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: the card must be" in done.stderr, done.stderr
    assert str(odd) in done.stderr, done.stderr
    assert not desk.calls.exists()


def test_fr7_control_a_dated_card_still_launches(desk):
    done = desk.run("build", str(desk.card_for("LOW")))
    assert done.returncode == 0, done.stderr
    assert "BAND: LOW → grok-4.7" in done.stderr, done.stderr


# ---- FR-8 (check r2 O2/G2): the 429 clause is cited as the brain's reading -------------------


def test_fr8_the_429_clause_is_cited_as_the_brains_reading():
    ls = lines_of("SHADOW-HUB.md")
    line = ls[one_index(ls, "BAND ROUTING (")]
    for part in ("brain 2026-10-16, reading R1532's 'Terra backup'", "a 429 is recorded and retried, never a backup",
                 "R1471 (7) is recorded in the direction file"):
        assert part in line, part
    assert "2026-10-14 item 7" not in line
    assert "R1532: Terra backup" not in line


def test_fr8_control_the_rest_of_the_line_and_the_table_stand():
    ls = lines_of("SHADOW-HUB.md")
    line = ls[one_index(ls, "BAND ROUTING (")]
    assert "its own fresh job card with BAND: HIGH" in line
    assert "never on a 429" in line
    sect = section(ls, "BUILDERS")
    for band in ("LOW", "MID", "HIGH"):
        assert sum(ln.startswith(f"| {band} |") for ln in sect) == 1, band


# ---- B5: a routed card's untracked SHADOW-INSTRUCTIONS.md is not dirt at its check -------------


class CheckDesk:
    """A tmp repo with the real CHECK-HUB.md, a built job branch (a code commit, the tip, then its
    build report), a check card and a stub `claude` (test_desk_launch_prechecks.Desk's shape)."""

    def __init__(self, tmp_path: Path):
        self.wt = tmp_path / "wt"
        self.repo = tmp_path / "repo"
        self.wt.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        for day in (NEW_DAY, OLD_DAY):
            (self.prompts / day).mkdir(parents=True)
        self.reports.mkdir(parents=True)
        shutil.copy(HUBS / "CHECK-HUB.md", self.prompts / "CHECK-HUB.md")
        (self.reports / "cto-2026-01-02.md").write_text(
            "| R1 | 07:00 ET | HIS RULING (constructed). | HIS RULING · APPROVED |\n")
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "base")
        self.base = git(self.repo, "rev-parse", "--short=8", "HEAD")
        self.job_wt = self.wt / "x-job"
        git(self.repo, "worktree", "add", "-q", "-b", "ops/x-job", str(self.job_wt), self.base)
        (self.job_wt / "src").mkdir()
        (self.job_wt / "src" / "x.py").write_text("X = 1\n")
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", "code")
        self.tip = git(self.job_wt, "rev-parse", "--short=8", "HEAD")
        self.report = self.job_wt / "docs" / "40 - DevDocs" / "reports" / "x-job-build.md"
        self.report.parent.mkdir(parents=True, exist_ok=True)
        self.report.write_text(
            f"# x-job build\n\nBUILT · job: x-job · tip: {self.tip} | on {self.base} | migration: none | "
            "rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0\n")
        git(self.job_wt, "add", "-A")
        git(self.job_wt, "commit", "-q", "-m", "docs(x-job): build report")
        self.check_report = self.reports / "x-job-check.md"
        stub = tmp_path / "bin"
        stub.mkdir()
        (stub / "claude").write_text('#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\nexit 0\n')
        (stub / "claude").chmod(0o755)
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{stub}:{os.environ['PATH']}", DESK_LAUNCH_DRY="1", **GIT_ENV,
        )

    def card(self, band: str | None, day: str = NEW_DAY) -> Path:
        card = self.prompts / day / "01-x-job-card.md"
        band_line = "" if band is None else f"BAND: {band}\n"
        card.write_text(
            "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
            f"BASE: {self.base}\nTIP: {self.tip}\nREPORT: {self.report}\n"
            f"CHECK REPORT: {self.check_report}\nHOUSE B: as needed\nTREE STATE: unchanged\n"
            f"RULINGS: 2026-01-02 R1\n{band_line}\n## ROWS\n| row | what |\n"
        )
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "card")
        return card

    def check(self, card: Path) -> subprocess.CompletedProcess:
        (self.job_wt / "SHADOW-INSTRUCTIONS.md").write_text("# constructed\n")
        return subprocess.run(["sh", str(LAUNCH), "check", str(card)], env=self.env,
                              capture_output=True, text=True, timeout=120)

    def preflight(self, card: Path) -> subprocess.CompletedProcess:
        (self.job_wt / "SHADOW-INSTRUCTIONS.md").write_text("# constructed\n")
        return subprocess.run(["sh", str(PREFLIGHT), "check", str(card)], env=self.env,
                              capture_output=True, text=True, timeout=120)


@pytest.fixture
def cdesk(tmp_path):
    return CheckDesk(tmp_path)


NOT_CLEAN = "is not clean (the check session commits there)"


@pytest.mark.parametrize("band", ["LOW", "MID"])
def test_b5_a_routed_tree_with_its_untracked_instructions_reaches_its_check(cdesk, band):
    done = cdesk.check(cdesk.card(band))
    assert NOT_CLEAN not in done.stderr, done.stderr
    assert done.returncode == 0, done.stderr


@pytest.mark.parametrize("band,day", [(None, NEW_DAY), ("HIGH", NEW_DAY), ("LOW", OLD_DAY)])
def test_b5_control_a_tree_that_is_not_routed_is_still_dirty_at_its_check(cdesk, band, day):
    done = cdesk.check(cdesk.card(band, day))
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {cdesk.job_wt} {NOT_CLEAN}" in done.stderr, done.stderr


@pytest.mark.parametrize("band", ["LOW", "MID"])
def test_b5_a_routed_tree_with_its_untracked_instructions_passes_preflight_status(cdesk, band):
    done = cdesk.preflight(cdesk.card(band))
    assert "FAILED PREFLIGHT: status" not in done.stdout, done.stdout
    assert done.stdout.splitlines()[-1] == "PREFLIGHT OK", done.stdout + done.stderr


@pytest.mark.parametrize("band,day", [(None, NEW_DAY), ("HIGH", NEW_DAY), ("LOW", OLD_DAY)])
def test_b5_control_a_tree_that_is_not_routed_still_fails_preflight_status(cdesk, band, day):
    done = cdesk.preflight(cdesk.card(band, day))
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stdout.splitlines()[-1] == "FAILED PREFLIGHT: status"


@pytest.mark.parametrize("day", [NEW_DAY, OLD_DAY])
def test_fr3_control_an_opus_builds_check_card_without_band_still_launches(cdesk, day):
    """FR-3 'optional otherwise': an Opus build's tree, no untracked file, a check card with no BAND."""
    card = cdesk.card(None, day)
    done = subprocess.run(["sh", str(LAUNCH), "check", str(card)], env=cdesk.env,
                          capture_output=True, text=True, timeout=120)
    assert "REFUSED" not in done.stderr, done.stderr
    assert done.returncode == 0, done.stderr


# ---- B6: G5's shadow branch admits the report's result file -----------------------------------

G5_FENCE = (
    "route: this seat writes only inside its fence (a worker: its worktree and its report; "
    "the brain: reports/ and prompts/20*/; nothing under /Users/cobalt/Vault); "
    "a fixed file changes by a card row"
)
JOB_WT = "x-band"


def guard_env(tmp_path: Path) -> dict:
    return dict(os.environ, COBALT_WT_ROOT=str(tmp_path / "wt"), COBALT_REPO_ROOT=str(tmp_path / "repo"))


def gate_seat(tmp_path: Path) -> tuple[dict, Path]:
    """The routed gate seat as desk-launch.sh shadow makes it: cwd the card's worktree, the launch
    message reading SHADOW-HUB.md with `CARD:` and `MODEL:`; returns the seat and the card's REPORT."""
    wt = tmp_path / "wt"
    prompts = tmp_path / "repo" / "docs" / "40 - DevDocs" / "prompts"
    (prompts / NEW_DAY).mkdir(parents=True)
    hub = prompts / "SHADOW-HUB.md"
    hub.write_text(shadow_hub_text(shadow_line()))
    report = wt / JOB_WT / "docs" / "40 - DevDocs" / "reports" / f"{JOB_WT}-build.md"
    card = prompts / NEW_DAY / f"01-{JOB_WT}-card.md"
    card.write_text(
        f"JOB: {JOB_WT}\nBRANCH: ops/{JOB_WT}\nWORKTREE: {JOB_WT}\nREPORT: {report}\nDB: none\nBAND: LOW\n\n"
        "## ROWS\n\n| row | what | red first | files |\n|---|---|---|---|\n| X1 | x | x | `ops/desk/x.py` |\n"
    )
    cwd = wt / JOB_WT
    cwd.mkdir(parents=True)
    first = f"Read '{hub}' and follow it exactly. CARD: '{card}' MODEL: grok-4.7"
    transcript = tmp_path / "t-shadow.jsonl"
    transcript.write_text(
        json.dumps({"type": "queue-operation", "operation": "enqueue", "sessionId": "sess-test-1"}) + "\n"
        + json.dumps({"type": "user", "sessionId": "sess-test-1",
                      "message": {"role": "user", "content": first}}) + "\n"
    )
    return {"cwd": str(cwd), "transcript": str(transcript)}, report


def write(tmp_path: Path, path: Path, seat: dict) -> subprocess.CompletedProcess:
    event = {
        "session_id": "sess-test-1", "transcript_path": seat["transcript"], "cwd": seat["cwd"],
        "permission_mode": "dontAsk", "hook_event_name": "PreToolUse", "tool_name": "Write",
        "tool_input": {"file_path": str(path), "content": "x\n"},
    }
    return subprocess.run(["python3", str(GUARD)], input=json.dumps(event), env=guard_env(tmp_path),
                          capture_output=True, text=True, timeout=60)


def test_b6_the_gate_seat_writes_its_result_file(tmp_path):
    seat, report = gate_seat(tmp_path)
    result = report.with_name(report.name[: -len(".md")] + ".result")
    done = write(tmp_path, result, seat)
    assert done.returncode == 0, done.stderr
    assert done.stderr == ""


def test_b6_control_the_report_passes_and_every_other_path_is_still_fenced(tmp_path):
    seat, report = gate_seat(tmp_path)
    assert write(tmp_path, report, seat).returncode == 0
    others = [
        report.with_name(report.name + ".result"),  # the .md kept: not the name the readers read
        report.with_name("other-build.result"),
        tmp_path / "wt" / JOB_WT / "src" / "x.result",
        tmp_path / "wt" / JOB_WT / "src" / "x.py",
    ]
    for path in others:
        done = write(tmp_path, path, seat)
        assert done.returncode == 2, (path, done.stderr)
        assert done.stderr == G5_FENCE + "\n", (path, done.stderr)


def test_b6_control_a_link_named_as_the_result_file_is_fenced(tmp_path):
    seat, report = gate_seat(tmp_path)
    result = report.with_name(report.name[: -len(".md")] + ".result")
    result.parent.mkdir(parents=True, exist_ok=True)
    target = tmp_path / "elsewhere.txt"
    target.write_text("x\n")
    result.symlink_to(target)
    done = write(tmp_path, result, seat)
    assert done.returncode == 2, done.stderr
    assert done.stderr == G5_FENCE + "\n"
