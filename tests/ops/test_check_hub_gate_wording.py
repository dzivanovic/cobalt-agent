"""CHECK-HUB.md's RUNS and stop-line wording say what the deploy gates read (card
prompts/2026-10-12/397-gate-alignment-card.md H3, R1157 (3), R1160).

Read on the real file, as tests/ops/test_check_hub_shadow.py reads it (card 386): `lines()` is the
file, `head_lines()` is `git show HEAD:`. Three edits inside existing lines; no line is added.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUB_REL = "docs/40 - DevDocs/prompts/CHECK-HUB.md"
HUB = REPO / HUB_REL

H3_A = ("; one whose fix lies outside the rows' files is written `HELD, NOT FIXED — <file>` on this row "
        "and on its `## FIXES` row (`## 5`)")
H3_B = " on its `## RUNS` row and as `- <id>: HELD, NOT FIXED — <file>` under `## FIXES`"
H3_C = (
    "THE DEPLOY GATES (THE RULE in `deploy-card.sh`, `desk-launch.sh`, `deploy-step0.sh`) read a held "
    "id from its `## RUNS` or `## FIXES` row marked `HELD, NOT FIXED`, closed by the fix round's "
    "`FIXED: <id> — tests/<path>.py::<name>` or `CARRIED: <id> — <test id> — R<n>`; `open:` past "
    "`held unfixed` passes only for `REJECTED` or `UNSETTLED` ids the fix report settles, one "
    "`SETTLED: <id> — R<n>` each, R<n> a DESK RECORD row found by this rule. This report is never "
    "edited to pass a gate."
)


def lines() -> list[str]:
    return HUB.read_text(encoding="utf-8").splitlines()


def head_lines() -> list[str]:
    out = subprocess.run(["git", "show", f"HEAD:{HUB_REL}"], cwd=REPO, capture_output=True,
                         text=True, check=True).stdout
    return out.splitlines()


def one(prefix: str) -> str:
    hits = [ln for ln in lines() if ln.startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def test_h3_runs_and_fixes_name_held_not_fixed():
    """RED on BASE: `assert 0 == 1` ((a) absent)."""
    a = one("A TEST: put it")
    assert a.count(H3_A) == 1
    assert "for the finding's stated reason" + H3_A + " · `NOT HELD`" in a
    b = one("Only inside the files")
    assert b.count(H3_B) == 1
    assert "is `HELD, NOT FIXED — <file>`" + H3_B + ": it is counted `held unfixed`" in b


def test_h3_the_ready_line_names_what_the_gates_read():
    """RED on BASE: `assert 0 == 1` (no line holds `SETTLED: <id> — R<n>`)."""
    hits = [ln for ln in lines() if "SETTLED: <id> — R<n>" in ln]
    assert len(hits) == 1
    assert hits[0].startswith("`ready: YES` only when")
    assert hits[0].count(H3_C) == 1
    assert hits[0].endswith(" Then stop. " + H3_C)


def test_h3_no_line_is_added():
    """Two-sided control, green on BASE and after."""
    assert len(lines()) == len(head_lines())
