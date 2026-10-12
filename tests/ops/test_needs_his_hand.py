"""The NEEDS HIS HAND section of the close and day-open prompts (card 2026-10-12/393, row N1).

His standing item 3 (reports/hands-off-answer-2026-10-12.md:13, LAWS L81, R1138 of
reports/cto-2026-10-12.md): an item only he can do goes into ONE named section of the report, one
entry each in his shape, raised by day only; at night it waits in that section and the rest runs.
The two prompts are read from this tree as tests/ops/test_hub_lines.py reads a hub; nothing is
run, and no launch line, allow string or deny string changes.
"""

from __future__ import annotations

import shlex
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
NAMES = ["CLOSE-HUB.md", "DAY-OPEN-QWEN.md"]

SECTION = "## NEEDS HIS HAND"
# his item 3, byte for byte
SHAPE = "what was blocked · by which rule or tool · why no seat could do it · the exact line he types · what it unblocks"
RULES = ["`none`", "never around a permission check", "by day only", "at night it waits in this section and the rest runs"]
LINE_COUNT = {"CLOSE-HUB.md": 66, "DAY-OPEN-QWEN.md": 30}


def read(name: str) -> str:
    return (HUBS / name).read_text(encoding="utf-8")


def shape_line(lines: list[str], name: str) -> int:
    hits = [i for i, ln in enumerate(lines) if SHAPE in ln]
    assert len(hits) == 1, f"{name}: {len(hits)} lines hold the entry shape"
    return hits[0]


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


@pytest.mark.parametrize("name", NAMES)
def test_the_section_is_named_once_in_each_file(name):
    assert read(name).count(SECTION) == 1


@pytest.mark.parametrize("name", NAMES)
def test_the_entry_shape_is_written_once_byte_for_byte(name):
    assert read(name).count(SHAPE) == 1


@pytest.mark.parametrize("name", NAMES)
def test_the_four_rules_stand_in_the_one_line(name):
    lines = read(name).splitlines()
    line = lines[shape_line(lines, name)]
    for rule in RULES:
        assert rule in line, f"{name}: {rule!r} missing from the shape line"


def test_the_section_sits_where_the_text_puts_it():
    close = read("CLOSE-HUB.md").splitlines()
    chain = [i for i, ln in enumerate(close) if ln.startswith("`<REPORT>`, shaped: ")]
    assert len(chain) == 1
    assert "`## DECISIONS` → `## NEEDS HIS HAND` → `## RECORDS`" in close[chain[0]]
    assert shape_line(close, "CLOSE-HUB.md") == chain[0] + 1

    day = read("DAY-OPEN-QWEN.md").splitlines()
    table = [i for i, ln in enumerate(day) if ln.startswith("Table: check | verdict")]
    assert len(table) == 1
    assert shape_line(day, "DAY-OPEN-QWEN.md") == table[0] + 1
    assert day[-1] == "/no_think"


def test_nothing_else_changed():
    for name, count in LINE_COUNT.items():
        assert len(read(name).splitlines()) == count, name

    launch = [ln for ln in read("CLOSE-HUB.md").splitlines() if ln.startswith("claude --bg ")]
    assert len(launch) == 1
    assert len(tools(launch[0], "--allowedTools")) == 21
    assert len(tools(launch[0], "--disallowedTools")) == 11
    assert "--permission-mode dontAsk" in launch[0]
    assert "NEEDS" not in launch[0]

    assert read("DAY-OPEN-QWEN.md").count("COBALT_ENV=production uv run cobalt day-open verdict") == 1
