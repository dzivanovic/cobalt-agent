"""docs/40 - DevDocs/prompts/SHADOW-HUB.md, the gate seat's fixed file (card 2026-10-11 324, S1, S5, S7).

Every test reads the tree's own file. Its one launch line is BUILD-HUB.md line 12's with
SHADOW-HUB.md read in its place, the gate seat's name and ONE more token, `<builder allow>`;
its `## BUILDERS` table holds the four builder rows (R1019: no Opus and no Sol arm); its
`## RESULTS TABLE` is the routing table's shape (R1014). Nothing is launched.
"""

from __future__ import annotations

import os
import re
import shlex
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
PROMPTS = REPO / "docs" / "40 - DevDocs" / "prompts"
SHADOW = PROMPTS / "SHADOW-HUB.md"
BUILD = PROMPTS / "BUILD-HUB.md"
SIGN = "«" + "SIGN"  # built so this file never spells the mark whole
TOKEN = "<builder allow>"
WT_GLOB = "/Users/cobalt/cobalt-wt/<worktree>/**"
IDS = ["grok-4.7", "claude-sonnet-5-5", "gpt-5.6-terra", "gemini-4-argon-high"]
ALLOW = {
    "grok-4.7": "Bash(grok -m grok-4.7 --sandbox cobalt-job *)",
    "claude-sonnet-5-5": "Bash(claude -p --model claude-sonnet-5-5 *)",
    "gpt-5.6-terra": "Bash(codex exec --skip-git-repo-check -m gpt-5.6-terra -s workspace-write *)",
    "gemini-4-argon-high": "Bash(agy --model gemini-4-argon-high --mode accept-edits --sandbox *)",
}


def text() -> str:
    return SHADOW.read_text()


def launch_lines(t: str) -> list[str]:
    return [x for x in t.splitlines() if x.startswith("claude --bg ")]


def tools(line: str, flag: str, ends: tuple[str, ...]) -> list[str]:
    """The words of one tool list: from `flag` to the first of `ends`; a "…" span is one word."""
    rest = line.split(f" {flag} ", 1)[1]
    for end in ends:
        rest = rest.split(f" {end} ", 1)[0]
    return re.findall(r'"[^"]*"|<builder allow>|\S+', rest)


def build_line() -> str:
    lines = launch_lines(BUILD.read_text())
    assert len(lines) == 1
    return lines[0]


def section(t: str, name: str) -> str:
    m = re.search(rf"^## {re.escape(name)}[ \t]*$(.*?)(?=^## |\Z)", t, re.M | re.S)
    assert m, f"no ## {name}"
    return m.group(1)


def builders(t: str) -> dict[str, list[str]]:
    rows = {}
    for line in section(t, "BUILDERS").splitlines():
        if not line.startswith("| `"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows[cells[0].strip("`")] = cells
    return rows


def command(cells: list[str]) -> str:
    return cells[3].strip().strip("`")


def write_targets(cmd: str) -> set[str]:
    """Every path the command lets its model write: grok `--allow "Write(X)"`, claude
    `Edit(//X)` / `Write(//X)` (the leading `/` of `//` marks an absolute path), codex `-C D` (D/**),
    agy `--add-dir D` (D/**, card 671 G2)."""
    out = set(re.findall(r'--allow "Write\(([^)]*)\)"', cmd))
    out |= {p[1:] for p in re.findall(r'"(?:Edit|Write)\((//[^)]*)\)"', cmd)}
    out |= {d + "/**" for d in re.findall(r" -C (\S+)", cmd)}
    out |= {d + "/**" for d in re.findall(r" --add-dir (\S+)", cmd)}
    return out


# ---- S1: the line ---------------------------------------------------------------------------


def test_s1_exactly_one_launch_line():
    assert len(launch_lines(text())) == 1


def test_s1_the_mode_is_dont_ask_once():
    line = launch_lines(text())[0]
    assert line.count("--permission-mode") == 1
    assert " --permission-mode dontAsk " in line


def test_s1_the_allow_list_is_build_hubs_26_plus_the_builder_token():
    line = launch_lines(text())[0]
    base = tools(build_line(), "--allowedTools", ("--disallowedTools",))
    assert len(base) == 26
    assert tools(line, "--allowedTools", ("--disallowedTools",)) == base + [TOKEN]


def test_s1_the_deny_list_is_build_hubs_4():
    ends = ("--add-dir",)
    base = tools(build_line(), "--disallowedTools", ends)
    assert len(base) == 4
    assert tools(launch_lines(text())[0], "--disallowedTools", ends) == base


def test_s1_the_rest_of_the_line_is_build_hubs_with_the_gate_seat():
    line = launch_lines(text())[0]
    want = build_line().replace("BUILD-HUB.md' and follow it exactly. CARD: '<card>'",
                                "SHADOW-HUB.md' and follow it exactly. CARD: '<card>' MODEL: <model>")
    want = want.replace("--remote-control <job>-build --name <job>-build",
                        "--remote-control <job>-gate --name <job>-gate")
    want = want.replace(' --disallowedTools ', f' {TOKEN} --disallowedTools ', 1)
    assert line == want


def test_s1_builders_holds_exactly_the_four_ids():
    rows = builders(text())
    assert sorted(rows) == sorted(IDS)
    sect = section(text(), "BUILDERS")
    for gone in ("claude-opus-5-5", "gpt-5.6-sol", "gemini-4-argon-medium", "gemini-4-argon-low", "gemini-3.1-pro-high"):
        assert gone not in sect


@pytest.mark.parametrize("model", IDS)
def test_s1_each_row_holds_its_allow_string_and_a_command_under_it(model):
    cells = builders(text())[model]
    assert cells[2].strip("`") == ALLOW[model]
    prefix = ALLOW[model][len("Bash("):-len("*)")]
    assert command(cells).startswith(prefix)


@pytest.mark.parametrize("model", IDS)
def test_s1_every_builder_writes_only_its_worktree(model):
    assert write_targets(command(builders(text())[model])) == {WT_GLOB}


@pytest.mark.parametrize("word", ["--always-approve", "danger-full-access", "bypassPermissions"])
def test_s1_no_wide_flag_on_the_line_or_in_builders(word):
    assert word not in launch_lines(text())[0]
    assert word not in section(text(), "BUILDERS")


@pytest.mark.parametrize("model", IDS)
def test_s1_every_sign_cell_holds_his_row(model):
    cell = builders(text())[model][4]
    row = "2026-10-17 R1738" if model == "gemini-4-argon-high" else "2026-10-11 R1069"
    assert f"{row} · HIS RULING · APPROVED" in cell
    assert SIGN not in cell


def test_s1_the_claude_builder_runs_no_command():
    cmd = command(builders(text())["claude-sonnet-5-5"])
    assert " --permission-mode dontAsk " in cmd
    assert '--disallowedTools "Bash" ' in cmd


# ---- card 2026-10-16 671 H1, X2: the Gemini builder row (R1738) -------------------------------


def test_k5_the_gemini_builder_runs_no_shell():
    cmd = command(builders(text())["gemini-4-argon-high"])
    assert cmd.count(" --mode ") == 1
    for part in (" --mode accept-edits ", " --sandbox ", " --add-dir /Users/cobalt/cobalt-wt/<worktree> ",
                 '--print="<pass prompt>"'):
        assert part in cmd, part


def test_k5_no_line_names_the_old_gemini_id():
    assert [x for x in text().splitlines() if "gemini-3.1-pro-high" in x] == []


def test_k5_the_launcher_sentence_names_the_one_gemini_id():
    lines = [x for x in text().splitlines() if x.startswith("The launcher refuses")]
    assert len(lines) == 1
    assert "a Gemini id other than gemini-4-argon-high," in lines[0]


def test_k5_the_gemini_x1_paragraph():
    lines = [x for x in text().splitlines() if x.startswith("X1 for Gemini")]
    assert len(lines) == 1
    assert lines[0] in section(text(), "BUILDERS").splitlines()
    for part in ("x1-canary/probe/.env", "x1-canary/CANARY.txt", "OUTSIDE.txt", "X1 WRITE OK",
                 "INCOMPLETE", "## PASSES row 0 (X1)"):
        assert part in lines[0], part
    assert "x1-canary/.env" not in lines[0]


# ---- S7: the .env precondition --------------------------------------------------------------


def test_s7_every_pass_is_preceded_by_the_env_check():
    lines = [x for x in text().splitlines() if x.strip()]
    seen = set()
    for k, line in enumerate(lines):
        m = re.match(r"pass (T|S|S2) — ", line)
        if not m:
            continue
        seen.add(m.group(1))
        assert "ls -la /Users/cobalt/cobalt-wt/<worktree>/.env" in lines[k - 1], line
        assert "No such file" in lines[k - 1], line
    assert seen == {"T", "S", "S2"}


def test_s7_terra_keeps_its_network_off():
    cells = builders(text())["gpt-5.6-terra"]
    assert "network_access" not in command(cells)
    assert "network: off" in " | ".join(cells)


# ---- S5: the results table ------------------------------------------------------------------


def results() -> str:
    return section(text(), "RESULTS TABLE")


@pytest.mark.parametrize(
    "words",
    [
        "AT LEVEL", "CLOSE BELOW", "BELOW", "INCOMPLETE",
        "CAN BUILD", "CAN BUILD WITH A REVIEW", "NOT YET",
        "insufficient data (n=1 per band)", "n=2 per band",
        "LOW 0-2 · MID 3-6 · HIGH ≥7",
        "`NOT YET` = `not this band, on this evidence`",
    ],
)
def test_s5_the_table_holds(words):
    assert words in results()


@pytest.mark.parametrize("model", ["Opus 5.5", "Sol"])
def test_s5_the_two_not_measured_rows(model):
    rows = [x for x in results().splitlines() if x.startswith(f"| {model} |")]
    assert len(rows) == 1
    assert "can build every band — his word, 2026-10-11 R1019, not measured" in rows[0]


def test_s5_the_harness_difference_prints_once():
    line = "the originals ran their own commands; the arms write only, under an Opus gate seat"
    assert results().count(line) == 1


@pytest.mark.parametrize("word", ["failed", "rank"])
def test_s5_no_failed_and_no_rank_in_the_table(word):
    assert not re.search(rf"\b{word}\b", results(), re.I)


# ---- check of shadow-hub-1011: the findings, each run alone ---------------------------------


def test_s1_pass_s_is_not_restricted_to_src_and_tests():
    procedure = section(text(), "THE PROCEDURE (BUILD-HUB's steps; only the differences are written here)")

    assert "Pass S: the src/ rows" not in procedure
    assert "rows' files under `src/` and `tests/`" not in procedure


def test_s5_the_unavailable_model_has_its_na_row():
    rows = [
        line
        for line in results().splitlines()
        if line.startswith("| Gemini ")
    ]

    assert len(rows) == 1
    assert "N/A —" in rows[0]


def test_s1_the_built_line_can_record_a_db_none_gate():
    assert "cobalt_dev: not taken" in text()


# ---- the fix round of shadow-hub-1011 (card 324 F1, F2) --------------------------------------

READ_WT = "Read(//Users/cobalt/cobalt-wt/<worktree>/**)"


def sonnet_words(worktree: str = "<worktree>") -> list[str]:
    """The Sonnet `builder command`, `shlex`-split with `<worktree>` and the prompt filled."""
    cmd = command(builders(text())["claude-sonnet-5-5"])
    cmd = cmd.replace("<worktree>", worktree).replace('"<pass prompt>"', '"PROMPTWORD"')
    return shlex.split(cmd)


def tool_list(ws: list[str], flag: str) -> list[str]:
    """The words after `flag` up to the next word that starts with `--`."""
    out = []
    for w in ws[ws.index(flag) + 1:]:
        if w.startswith("--"):
            break
        out.append(w)
    return out


def test_f1_the_sonnet_prompt_comes_right_after_the_model():
    ws = sonnet_words()
    k = ws.index("PROMPTWORD")
    assert ws[k - 2:k] == ["--model", "claude-sonnet-5-5"]
    for flag in ("--allowedTools", "--disallowedTools"):
        assert "PROMPTWORD" not in tool_list(ws, flag)
    for flag in ("--allowedTools", "--disallowedTools", "--permission-mode"):
        assert k < ws.index(flag)


@pytest.mark.parametrize("worktree", ["<worktree>", "x-job-sonnet"])
def test_f2_the_sonnet_read_is_its_worktree_only(worktree):
    allowed = tool_list(sonnet_words(worktree), "--allowedTools")
    reads = [w for w in allowed if w == "Read" or w.startswith("Read(")]
    assert reads == [READ_WT.replace("<worktree>", worktree)]
    assert "Read" not in allowed


# ---- the fix round of install-shadow-hub-1011 (card 355 F1, check O1) ------------------------

AUTHORIZE = REPO / "ops" / "desk" / "authorize.sh"
INSTALL_TITLE = "INSTALL: 2026-10-11 R1069 · HIS RULING · APPROVED"
GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


def git(cwd: Path, *args: str) -> None:
    subprocess.run(["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
                   env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True)


def test_f1_the_real_title_passes_the_authorize_line_one_gate(tmp_path):
    """authorize.sh shadow reads line 1 for `INSTALL: <date> R<n>` and proves that row
    (test_authorize.py's `desk` shape: a tmp repo as COBALT_REPO_ROOT; the real repo is never read)."""
    title = text().split("\n", 1)[0]
    assert title == INSTALL_TITLE

    repo = tmp_path / "repo"
    prompts = repo / "docs" / "40 - DevDocs" / "prompts"
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    (prompts / "2026-01-02").mkdir(parents=True)
    reports.mkdir(parents=True)
    (prompts / "SHADOW-HUB.md").write_text(title + "\n\nbody\n")
    (reports / "cto-2026-10-11.md").write_text(
        "| row | time | what | state |\n|---|---|---|---|\n"
        "| R1069 | 09:00 ET | HIS RULING: installs the hub. | HIS RULING · APPROVED |\n")
    (reports / "cto-2026-01-02.md").write_text(
        "| row | time | what | state |\n|---|---|---|---|\n"
        "| R2 | 09:05 ET | HIS RULING: the job's ruling. | HIS RULING · APPROVED |\n")
    card = prompts / "2026-01-02" / "01-x-job-card.md"
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        "BASE: 0000aaaa\nTIP:\nREPORT: /nowhere/x-job-build.md\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R2\n\n## ROWS\n| row | what |\n")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    env = dict(os.environ, COBALT_REPO_ROOT=str(repo), COBALT_WT_ROOT=str(tmp_path / "wt"), **GIT_ENV)
    done = subprocess.run(["sh", str(AUTHORIZE), "shadow", str(card)], env=env,
                          capture_output=True, text=True, timeout=120)

    assert "STANDING LIST 2026-10-11 R1069 row · " in done.stdout, done.stdout + done.stderr
    assert "the title names no INSTALL" not in done.stdout
    assert done.returncode == 0, done.stdout + done.stderr


# ---- card 2026-10-18 759 H1: the Gemini GRANT and the X1 read (R1863) ------------------------


def test_k5_the_gemini_grant_sentence():
    lines = [x for x in text().splitlines() if x.startswith("- Gemini:")]
    assert len(lines) == 1
    line = lines[0]
    assert "write_file(/Users/cobalt/cobalt-wt/<worktree>/)" in line
    assert "/Users/cobalt/.gemini/antigravity-cli/settings.json" in line
    assert "read_url" in line
    assert "removes it when the job closes" in line
    refuses = [x for x in text().splitlines() if x.startswith("The launcher refuses")]
    assert len(refuses) == 1
    assert "agy settings break the GRANT" in refuses[0]


def test_k5_the_gemini_grant_bounds():
    """The brain's bounds, R1872: one assert each on the same `- Gemini:` line."""
    lines = [x for x in text().splitlines() if x.startswith("- Gemini:")]
    assert len(lines) == 1
    line = lines[0]
    assert "on every outcome (BUILT, FAILED, killed)" in line
    assert "an orphaned rule found at the next launch is removed first and recorded" in line
    assert "no other line of that file changes" in line
    assert "one Gemini worktree at a time" in line
    assert line.count("write_file(/Users/cobalt/cobalt-wt/<worktree>/)") == 1
    assert "write_file(*)" not in line
    assert "regex:" not in line


def test_k5_the_gemini_x1_read_step():
    lines = [x for x in text().splitlines() if x.startswith("X1 for Gemini")]
    assert len(lines) == 1
    line = lines[0]
    assert "X1-READ.txt" in line
    assert "X1_READ_<job>" in line
    assert "READ OK" in line
    assert "read inside the worktree refused" in line


# ---- card 2026-10-18 800 H1: the launcher owns the Gemini grant (R1942) ----------------------


def test_g4_the_launcher_owns_the_grant():
    lines = [x for x in text().splitlines() if x.startswith("- Gemini:")]
    assert len(lines) == 1
    line = lines[0]
    assert "the launcher adds and removes it (his 2026-10-18 A)" in line
    assert "desk-launch.sh grant-sweep" in line
    assert "the desk never edits that file" in line
    assert "with its Edit tool" not in line
    refuses = [x for x in text().splitlines() if x.startswith("The launcher refuses")]
    assert len(refuses) == 1
    assert "another Gemini worktree's rule has a live gate seat" in refuses[0]
