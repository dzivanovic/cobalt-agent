"""LOCALE-PROOF: `export LC_ALL=C` is the first statement of every ops/desk/*.sh (card
2026-10-03/03 adoption-scripts, row L3; devfix-route check DECISION 1).

Under a UTF-8 locale a bracket range such as `[!A-Za-z0-9._-]` lets an accented letter
through, and `[!a-z0-9-]` a capital. Each script that validates a value with a range has one
refusal test beside its own tests; this file holds the position test for every script.
"""

from __future__ import annotations

from pathlib import Path

import pytest

DESK = Path(__file__).resolve().parents[2] / "ops" / "desk"
SCRIPTS = sorted(DESK.glob("*.sh"))


def first_statement(path: Path) -> str:
    """The first line after the shebang and the header comment that is not blank."""
    lines = path.read_text().splitlines()
    assert lines[0] == "#!/bin/sh", path.name
    for line in lines[1:]:
        if line.strip() and not line.startswith("#"):
            return line
    raise AssertionError(f"{path.name}: no statement")


def test_every_desk_script_is_found():
    assert len(SCRIPTS) >= 24, [p.name for p in SCRIPTS]


@pytest.mark.parametrize("path", SCRIPTS, ids=lambda p: p.name)
def test_the_first_statement_is_export_lc_all_c(path):
    assert first_statement(path) == "export LC_ALL=C"


@pytest.mark.parametrize("path", SCRIPTS, ids=lambda p: p.name)
def test_lc_all_is_exported_once(path):
    assert path.read_text().count("export LC_ALL=C") == 1
