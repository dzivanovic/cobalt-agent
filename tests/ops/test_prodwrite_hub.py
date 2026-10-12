"""PRODWRITE-HUB.md, the production-write seat's fixed file (card 2026-10-12 392 W1; his R1138, K3 + K5).

The real file of this tree is read as tests/ops/test_hub_lines.py reads a hub: its ONE line
beginning `claude --bg `, split as the shell splits it. The line's `<prod write>` token is the one
string desk-launch.sh fills from the card (row W2); unquoted, the shell reads it as two words.
STANDING-LIST.md and CARD.md gain one section each; both are read here too. Nothing here reads a
real card, report, `.env` or database.
"""

from __future__ import annotations

import re
import shlex
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
HUB = HUBS / "PRODWRITE-HUB.md"

CLASS_A = "Bash(sh /Users/cobalt/cobalt/ops/desk/*)"
FLAG = ("ONE bare command per Bash call: no &&, ;, |, redirect, newline or $(…) outside quotes. "
        "A call the hook blocks is NOT A REFUSAL: resend it as single calls.")
FLAG_SRC = '--append-system-prompt "' + FLAG.replace("$", "\\$") + '"'

ALLOW = [
    "Read",
    "Grep",
    "Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-*)",
    "Bash(sh /Users/cobalt/cobalt/ops/desk/authorize.sh prodwrite *)",
    "Bash(sh /Users/cobalt/cobalt/ops/desk/desk-context.sh *)",
    "Bash(git -C /Users/cobalt/cobalt log*)",
    "Bash(git -C /Users/cobalt/cobalt diff*)",
    "Bash(git -C /Users/cobalt/cobalt rev-parse*)",
    "Bash(ls *)",
    "Bash(grep *)",
    "Bash(tail *)",
    "Bash(date*)",
    "Bash(COBALT_ENV=production uv run cobalt backup status)",
    "Bash(COBALT_ENV=production uv run cobalt backup run)",
    "Bash(COBALT_ENV=production uv run cobalt db query *)",
]
TOKEN = "<prod write>"
PROD_ALLOWED = {
    "Bash(COBALT_ENV=production uv run cobalt backup status)",
    "Bash(COBALT_ENV=production uv run cobalt backup run)",
    "Bash(COBALT_ENV=production uv run cobalt db query *)",
}
DENY = [
    "AskUserQuestion",
    "EnterWorktree",
    "Bash(git push*)",
    "Bash(COBALT_ENV=production uv run cobalt db migrate*)",
    "Bash(COBALT_ENV=production uv run cobalt backup restore*)",
]
STEPS = ["AUTHORIZATION", "SHAPE", "BACKUP", "ROLLBACK", "WRITE", "VERIFY"]
ROW_CELLS = ["row", "command", "table", "count read", "expected rows", "backup", "inverse"]


def hub_line(path: Path = HUB) -> str:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1, f"{path.name}: {len(lines)} launch lines"
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


def test_exactly_one_launch_line():
    assert len([ln for ln in HUB.read_text(encoding="utf-8").splitlines() if ln.startswith("claude --bg ")]) == 1


def test_the_line_runs_opus_in_dontask_once_and_never_bypass():
    line = hub_line()
    assert line.count("--model claude-opus-5-5") == 1, line
    assert line.count("--permission-mode dontAsk") == 1, line
    assert line.count("--permission-mode") == 1, line
    assert "bypassPermissions" not in line


def test_the_allow_list_is_the_fifteen_strings_then_the_one_token():
    line = hub_line()
    # the shell reads the unquoted token as two words; the line holds it once, last of the allow list
    assert tools(line, "--allowedTools") == ALLOW + TOKEN.split(" ")
    assert line.count(TOKEN) == 1
    assert line.count(f" {TOKEN} --disallowedTools ") == 1


def test_every_production_allow_string_is_one_of_the_three():
    for s in tools(hub_line(), "--allowedTools"):
        if "COBALT_ENV=production" in s:
            assert s in PROD_ALLOWED, s


def test_no_class_a_string_on_the_line():
    line = hub_line()
    assert CLASS_A not in line
    assert "Bash(sh /Users/cobalt/cobalt/ops/desk/*)" not in tools(line, "--allowedTools")


def test_the_deny_list_is_the_five_strings():
    assert tools(hub_line(), "--disallowedTools") == DENY


def test_the_line_carries_the_flag_once():
    line = hub_line()
    assert line.count("--append-system-prompt") == 1
    assert line.count(FLAG_SRC) == 1, line


def test_the_title_names_its_standing_row():
    title = HUB.read_text(encoding="utf-8").splitlines()[0]
    assert title.startswith("# PRODWRITE-HUB — the production-write seat (INSTALLED "), title
    assert "INSTALL: 2026-10-12 R1138" in title, title


def test_the_stop_line_paragraph_names_both_endings():
    text = HUB.read_text(encoding="utf-8")
    stop = text.split("\n## STOP LINE", 1)[1].split("\n## ", 1)[0]
    assert "`WRITTEN · job: <JOB> · rows: <n> · backup: <path>`" in stop, stop
    assert "`FAILED: <reason>`" in stop, stop


def test_the_steps_stand_in_order_backup_before_the_write():
    lines = HUB.read_text(encoding="utf-8").splitlines()
    at = {}
    for i, ln in enumerate(lines):
        m = re.match(r"^## \(\w+\) ([A-Z]+)", ln)
        if m and m.group(1) in STEPS:
            assert m.group(1) not in at, f"two {m.group(1)} headings"
            at[m.group(1)] = i
    assert list(at) == STEPS, at
    assert at["BACKUP"] < at["ROLLBACK"] < at["WRITE"] < at["VERIFY"], at


def test_card_md_holds_one_prodwrite_section_with_the_ruling_and_the_seven_cells():
    text = (HUBS / "CARD.md").read_text(encoding="utf-8")
    assert text.count("\n## A PRODWRITE CARD, IN SHORT") == 1
    section = text.split("\n## A PRODWRITE CARD, IN SHORT", 1)[1].split("\n## ", 1)[0]
    assert "WRITE RULING" in section, section
    assert "| " + " | ".join(ROW_CELLS) + " |" in section, section


def test_standing_list_holds_one_section_nine_citing_r1138():
    text = (HUBS / "STANDING-LIST.md").read_text(encoding="utf-8")
    heads = [ln for ln in text.splitlines() if ln.startswith("## 9. `PRODWRITE-HUB.md`")]
    assert len(heads) == 1, heads
    assert "2026-10-12 R1138" in heads[0], heads[0]


# ---- card 2026-10-12 417 K3: the hub and the card format say the `db apply` proof -------------

SQL_ROWS = ["SQL FILE committed", "SQL FILE unchanged", "SQL SHA256", "SQL CARD BLOCK"]


def section(text: str, head: str) -> str:
    return text.split(f"\n{head}", 1)[1].split("\n## ", 1)[0]


def test_s1_step_zero_names_the_four_sql_rows():
    step0 = section(HUB.read_text(encoding="utf-8"), "## (0) AUTHORIZATION")
    for name in SQL_ROWS:
        assert name in step0, name


def test_s2_shape_reproves_the_hash_and_the_card_block():
    shape = section(HUB.read_text(encoding="utf-8"), "## (1) SHAPE")
    assert "--sha256" in shape
    assert "## SQL" in shape


def test_s3_the_never_line_is_unchanged_by_db_apply():
    (never,) = [ln for ln in HUB.read_text(encoding="utf-8").splitlines() if ln.startswith("NEVER:")]
    assert "a production schema change" in never
    assert "DDL" not in never and "db apply" not in never


def test_s4_card_md_names_the_sql_section_and_the_apply_file():
    text = (HUBS / "CARD.md").read_text(encoding="utf-8")
    prodwrite = section(text, "## A PRODWRITE CARD, IN SHORT")
    assert "## SQL" in prodwrite
    assert "-apply.sql" in prodwrite


def test_shape_reproves_the_verb_the_characters_and_the_table():
    shape = HUB.read_text(encoding="utf-8").split("\n## (1) SHAPE", 1)[1].split("\n## ", 1)[0]
    assert "db migrate" in shape
    assert "db dev-rebuild" in shape
    for ch in (";", "$", "|", "`"):
        assert ch in shape, ch
    assert "system." in shape and "user." in shape
