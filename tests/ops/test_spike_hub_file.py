"""docs/40 - DevDocs/prompts/SPIKE-HUB.md, the scratch-dir research seat's fixed file (card 2026-10-11 324, P1).

Every test reads the tree's own file. Its one launch line is prompt 330's line
(`prompts/2026-10-11/330-sdk-spike-live.md:1`, copied below as LINE_330 because that prompt is
committed on main after this branch's BASE) with SPIKE-HUB.md read in its place and the prompt
named by `PROMPT: '<prompt>'`. Nothing is launched.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPIKE = REPO / "docs" / "40 - DevDocs" / "prompts" / "SPIKE-HUB.md"
SCRATCH = "/Users/cobalt/cobalt-wt/sdk-spike-1010/"
P330 = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/330-sdk-spike-live.md"
HUB = "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SPIKE-HUB.md"
LINE_330 = (
    f"claude --bg \"Read '{P330}' and follow it exactly.\" --model claude-opus-5-5 "
    "--permission-mode dontAsk --remote-control sdk-spike-live --name sdk-spike-live "
    '--allowedTools "Read" "Edit(//Users/cobalt/cobalt-wt/sdk-spike-1010/**)" '
    '"Write(//Users/cobalt/cobalt-wt/sdk-spike-1010/**)" '
    '"Bash(uv venv /Users/cobalt/cobalt-wt/sdk-spike-1010/.venv)" '
    '"Bash(uv pip install --python /Users/cobalt/cobalt-wt/sdk-spike-1010/.venv claude-agent-sdk==*)" '
    '"Bash(/Users/cobalt/cobalt-wt/sdk-spike-1010/.venv/bin/python /Users/cobalt/cobalt-wt/sdk-spike-1010/*)" '
    '"Bash(ls *)" "Bash(date*)" "WebFetch(domain:anthropic.com)" "WebFetch(domain:www.anthropic.com)" '
    '"WebFetch(domain:docs.anthropic.com)" "WebFetch(domain:code.claude.com)" "WebFetch(domain:pypi.org)" '
    '--disallowedTools "Bash(git *)" "Bash(COBALT_ENV=*)" "Bash(psql*)" "Bash(docker*)" "Bash(cat *)" '
    '"AskUserQuestion" "EnterWorktree" '
    "--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt"
)


def text() -> str:
    return SPIKE.read_text()


def launch_lines() -> list[str]:
    return [x for x in text().splitlines() if x.startswith("claude --bg ")]


def tools(line: str, flag: str, end: str) -> list[str]:
    rest = line.split(f" {flag} ", 1)[1].split(f" {end} ", 1)[0]
    return re.findall(r'"[^"]*"|\S+', rest)


def test_p1_exactly_one_launch_line():
    assert len(launch_lines()) == 1


def test_p1_the_mode_is_dont_ask_once():
    line = launch_lines()[0]
    assert line.count("--permission-mode") == 1
    assert " --permission-mode dontAsk " in line


def test_p1_the_lists_are_330s_string_for_string():
    line = launch_lines()[0]
    assert tools(line, "--allowedTools", "--disallowedTools") == tools(LINE_330, "--allowedTools", "--disallowedTools")
    assert tools(line, "--disallowedTools", "--add-dir") == tools(LINE_330, "--disallowedTools", "--add-dir")


def test_p1_the_line_is_330s_with_the_hub_and_the_prompt_read():
    want = LINE_330.replace(f"Read '{P330}' and follow it exactly.",
                            f"Read '{HUB}' and follow it exactly. PROMPT: '<prompt>'")
    assert launch_lines()[0] == want


def test_p1_every_allowed_write_or_run_path_sits_in_the_scratch_dir():
    allow = tools(launch_lines()[0], "--allowedTools", "--disallowedTools")
    paths = [p for a in allow for p in re.findall(r"/Users/\S*?(?=[)\s]|$)", a)]
    assert paths
    for p in paths:
        assert ("/" + p.lstrip("/")).startswith(SCRATCH), p


def test_p1_no_git_is_allowed():
    allow = tools(launch_lines()[0], "--allowedTools", "--disallowedTools")
    assert not [a for a in allow if "git" in a]
    assert '"Bash(git *)"' in tools(launch_lines()[0], "--disallowedTools", "--add-dir")


def test_p1_the_pin_rule_names_14_days_and_double_equals():
    t = text()
    assert "14 days" in t
    assert "https://pypi.org/pypi/<name>/json" in t
    assert "<name>==<that version>" in t


def test_p1_the_line_is_signed_on_his_row():
    """Card 355 S1, his R1069: the mark is replaced with his row."""
    assert "THE LINE'S SIGN: 2026-10-11 R1069 · HIS RULING · APPROVED (R411:" in text()
    assert ("«" + "SIGN") not in text()
