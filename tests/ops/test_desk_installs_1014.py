"""The desk's command installs (card 2026-10-14 549, rows I1 and I2; his 2026-10-14 R1471, class K5 of L81).

Reads the real wake-up and STANDING-LIST.md: `"SendMessage"` once in `--allowedTools` of the desk's
`- LAUNCH` line, the line's other strings found by content, and one §4 row naming the string. Only
the lines the card changes are pinned, by their own text: no commit, no BASE hash, no whole-line
equality. Nothing is written.
"""

from __future__ import annotations

import shlex
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
WAKEUP = HUBS / "CTO-DESK-WAKEUP.md"
STANDING = HUBS / "STANDING-LIST.md"

# the twelve Bash strings of the desk line's allow list (card 549 row I1, its OLD list)
BASH_ALLOW = (
    "Bash(git add *)",
    "Bash(git commit *)",
    "Bash(git log*)",
    "Bash(git show*)",
    "Bash(git status*)",
    "Bash(git diff*)",
    "Bash(git -C * status*)",
    "Bash(git -C * log*)",
    "Bash(git -C * show*)",
    "Bash(git -C * diff*)",
    "Bash(git -C * rev-parse*)",
    "Bash(git -C * merge-base*)",
)


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


def desk_span() -> str:
    """The backticked `claude --bg ` span of the wake-up's one `- LAUNCH ` line."""
    launch = [ln for ln in WAKEUP.read_text(encoding="utf-8").splitlines() if ln.startswith("- LAUNCH ")]
    assert len(launch) == 1, launch
    return "claude --bg " + launch[0].split("`claude --bg ", 1)[1].split("`", 1)[0]


def section_4() -> str:
    text = STANDING.read_text(encoding="utf-8")
    return text.split("\n## 4. THE DESK'S OWN LINE", 1)[1].split("\n## ", 1)[0]


# ---- I1: the desk line ------------------------------------------------------------------------


def test_i1_the_desk_line_allows_sendmessage_once():
    span = desk_span()
    assert tools(span, "--allowedTools").count("SendMessage") == 1
    assert "SendMessage" not in tools(span, "--disallowedTools")


def test_i1_no_other_string_of_the_desk_line_changes():
    span = desk_span()
    allow = tools(span, "--allowedTools")
    non_bash = [s for s in allow if not s.startswith("Bash(")]
    assert set(non_bash) <= {"SendMessage"}, non_bash
    assert [s for s in allow if s.startswith("Bash(") and s not in BASH_ALLOW] == []
    for s in BASH_ALLOW:
        assert allow.count(s) == 1, s
    deny = tools(span, "--disallowedTools")
    assert "AskUserQuestion" in deny
    assert "EnterWorktree" in deny
    assert span.count("--permission-mode auto") == 1
    assert span.count("--remote-control cto-desk --name cto-desk") == 1
    for word in ("COBALT_ENV", ".env", "cobalt_key"):
        assert [s for s in allow if word in s] == [], word


# ---- I2: STANDING-LIST.md §4 ------------------------------------------------------------------


def test_i2_the_standing_list_section_4_names_sendmessage_once():
    rows = [ln for ln in section_4().splitlines() if ln.startswith("| `SendMessage` |")]
    assert len(rows) == 1, rows
    for part in ("R1471", "class K5", "survey row 1"):
        assert part in rows[0], part


def test_i2_the_other_section_4_rows_stand():
    lines = section_4().splitlines()
    for start in (
        "| `Bash(git add *)`",
        "| `Bash(git log*)`",
        "| `Bash(git -C * status*)`",
        "| deny `Edit(src/**)`",
        "| deny `Edit(//Users/cobalt/cobalt/ops/**)`",
    ):
        assert len([ln for ln in lines if ln.startswith(start)]) == 1, start
