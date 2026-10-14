"""BUILD-HUB row NO CLUTTER (card 2026-10-12/389 cleanup-class, row H1; his 2026-10-12 R1138 part 2).

Read on the real file, as tests/ops/test_hub_lines.py `hub_line` reads it. The one line sits in
its own paragraph between `## E2 ` and `## E3 `; no other line of the file changes from BASE.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUB_REL = "docs/40 - DevDocs/prompts/BUILD-HUB.md"
HUB = REPO / HUB_REL
BASE = "5e5fab02"
NO_CLUTTER = (
    "A RUN probe is staged outside the worktree (`$CLAUDE_JOB_DIR/tmp` or `/tmp/<job>-run/`), never under "
    "`docs/` or `src/`, and it is gone before W; W's PLACEMENT tests are the proof. A stray scratch path in "
    "the worktree is removed with `sh /Users/cobalt/cobalt/ops/desk/scratch-clean.sh \"<path>\"`."
)


def lines() -> list[str]:
    return HUB.read_text(encoding="utf-8").splitlines()


def base_lines() -> list[str]:
    done = subprocess.run(["git", "show", f"{BASE}:{HUB_REL}"], cwd=REPO, capture_output=True,
                          text=True, check=True)
    return done.stdout.splitlines()


def test_exactly_one_line_is_the_no_clutter_text():
    assert lines().count(NO_CLUTTER) == 1


def test_it_is_its_own_paragraph_after_e2_and_before_e3():
    ls = lines()
    i = ls.index(NO_CLUTTER)
    assert ls[i - 1] == "" and ls[i + 1] == ""
    assert ls[i - 2].startswith("Write each row's `red first` test"), ls[i - 2]
    assert ls[i - 3].startswith("## E2 "), ls[i - 3]
    assert ls[i + 2].startswith("## E3 "), ls[i + 2]


def test_it_names_the_script_and_the_script_is_in_the_tree():
    assert "ops/desk/scratch-clean.sh" in NO_CLUTTER
    assert (REPO / "ops" / "desk" / "scratch-clean.sh").is_file()


def test_the_launch_line_is_byte_identical_to_base():
    now = [ln for ln in lines() if ln.startswith("claude --bg ")]
    then = [ln for ln in base_lines() if ln.startswith("claude --bg ")]
    assert len(now) == 1 and now == then


def test_no_other_line_changes_from_base():
    ls = lines()
    i = ls.index(NO_CLUTTER)
    assert ls[:i] + ls[i + 2:] == base_lines()
