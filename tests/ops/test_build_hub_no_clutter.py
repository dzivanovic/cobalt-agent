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


# card 2026-10-14/548 RF2 (brain R1472: a card pins only the lines its own card changes): a BASE
# line that starts with one of these is another card's to change, and is not held here. Each
# other line of BASE is still in the file, in order; a line a card adds (the FIX-ROUND line of
# 523 H2, the RESULT FILE text 548 appends) is free.
EXEMPT = (
    'A "DB: none" build writes',  # 548 RF2 (:109)
    "claude --bg ",  # 537 (:12)
    "L1 a missing input",  # 480 H6 (:17)
    "`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`",  # 537 (:65)
    '- (a0) A "DB: none" CARD ONLY:',  # 537 (:80)
    "- THE GATE, ONE CALL",  # 537 (:81)
    "- (a) OFFLINE",  # 537 (:82)
    "- `## §0 Headline`",  # 523 H3 (:105)
    "`<tip>` = the last code commit",  # 480 H6 (:111)
    "- (b) THE LOCK",  # 547 H1 (:83)
)


def unmatched(now: list[str], then: list[str]) -> list[str]:
    """The BASE lines, exempt ones aside, that `now` does not hold in BASE's order."""
    missing, at = [], 0
    for ln in then:
        if ln.startswith(EXEMPT):
            continue
        if ln in now[at:]:
            at = now.index(ln, at) + 1
        else:
            missing.append(ln)
    return missing


def test_no_other_line_changes_from_base():
    # card 2026-10-13/523 rows H2 and H3 (brain R1309): the one new FIX-ROUND line and the one
    # CLOSE line they change; pinned in tests/ops/test_hub_text_1013.py
    # card 2026-10-14/547 row H1 (EXEMPT: it edits the W (b) line); pinned in tests/ops/test_db_copy_1014.py
    fix_round = "FIX-ROUND REPORT (brain R1309):"
    close_last = "- `## §0 Headline` (≤5 lines). Commit the report"
    now = lines()
    then = base_lines()
    assert sum(ln.startswith(fix_round) for ln in now) == 1
    assert sum(ln.startswith(close_last) for ln in now) == 1
    assert sum(ln.startswith(close_last) for ln in then) == 1
    assert sum(ln.startswith("- (b) THE LOCK") for ln in now) == 1
    assert unmatched(now, then) == []


def test_the_pin_fails_on_a_missing_base_line_and_passes_on_an_exempt_change():
    """Negative control (548 RF2 (5)): a copy missing a non-exempt BASE line is caught; a copy
    whose exempt line of another card is replaced is not."""
    then = base_lines()
    held = next(i for i, ln in enumerate(then) if ln.startswith("## E0 "))
    assert unmatched(then[:held] + then[held + 1:], then) == [then[held]]
    other = next(i for i, ln in enumerate(then) if ln.startswith("- THE GATE, ONE CALL"))
    assert unmatched(then[:other] + ["- THE GATE, ONE CALL (another card's text)"] + then[other + 1:], then) == []
