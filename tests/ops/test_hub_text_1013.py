"""Hub-text card 2026-10-13/523 (hub-text-1013), rows H1-H3 (brain R1295, R1309).

Read on the real hubs, as tests/ops/test_hub_lines.py `hub_line` reads them; the BASE text by
`git show`, as tests/ops/test_build_hub_no_clutter.py reads it. H1: DEPLOY-HUB P1 names the
nightly backup window. H2: BUILD-HUB states the fix round's FIXED line per held id. H3: BUILD-HUB's
stop-line step names no untracked file, with the launcher's one shadow exception.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
HUBS_REL = "docs/40 - DevDocs/prompts"
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
BASE = "ce548f10"

P1 = "- **P1 DATE**"
H1_OLD_TAIL = "it runs at any hour, day or night."
H1_NEW_TAIL = (
    "it runs at any hour, day or night, but it never starts within the nightly backup window "
    "21:30-22:30 ET (brain R1295; D2.4's `backup run` stays off it): a `date` inside the window → "
    "`FAILED PREFLIGHT: P1 — backup window`, nothing changed."
)

FIX_ROUND = "FIX-ROUND REPORT (brain R1309):"
H2_LINE = (
    "FIX-ROUND REPORT (brain R1309): the report of that fix round writes, at column 0, one line "
    "`FIXED: <finding id> — <test id>` for every held id of the check (a carried one: "
    "`CARRIED: <finding id> — <test id> — R<n>`, the shape `CARD.md` `## SHIPS` reads and "
    "`DEPLOY-HUB.md` P2 proves); a held id with no such line fails the deploy's P2 read."
)
TIP_LINE = "`<tip>` = the last code commit"
TOKENS = "`tokens: <n>` = the figure "

CLOSE_LAST = "- `## §0 Headline` (≤5 lines). Commit the report"
H3_OLD = "then `git status --short --branch` → `## <BRANCH>` only;"
H3_NEW = (
    "then `git status --short --branch` → `## <BRANCH>` only, no `??` line (no untracked file at the "
    "stop line, brain R1309; a shadow card's one untracked root `SHADOW-INSTRUCTIONS.md` is the "
    "launcher's only exception, `desk-launch.sh`, card 386 L4);"
)


def text(name: str) -> str:
    return (HUBS / name).read_text(encoding="utf-8")


def base_text(name: str) -> str:
    done = subprocess.run(["git", "show", f"{BASE}:{HUBS_REL}/{name}"], cwd=REPO, capture_output=True,
                          text=True, check=True)
    return done.stdout


def hub_line(name: str) -> str:
    lines = [ln for ln in (HUBS / name).read_text(encoding="utf-8").splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1, f"{name}: {len(lines)} launch lines"
    return lines[0]


def only(lines: list[str], start: str) -> str:
    hits = [ln for ln in lines if ln.startswith(start)]
    assert len(hits) == 1, f"{start!r}: {len(hits)} lines"
    return hits[0]


# ---- H1: DEPLOY-HUB P1 names the backup window (R1295) ---------------------------------------

def test_h1_p1_names_the_backup_window_once_in_its_own_line():
    t = text("DEPLOY-HUB.md")
    assert t.count("21:30-22:30 ET") == 1
    hit = [ln for ln in t.splitlines() if "21:30-22:30 ET" in ln][0]
    assert hit.startswith(P1), hit
    assert "No restart window binds a deploy (L43, his R389)" in hit
    assert "FAILED PREFLIGHT: P1 — backup window" in hit
    then = only(base_text("DEPLOY-HUB.md").splitlines(), P1)
    assert then.endswith(H1_OLD_TAIL)
    assert hit == then[: -len(H1_OLD_TAIL)] + H1_NEW_TAIL


def test_h1_the_launch_line_and_every_other_line_stand():
    then = base_text("DEPLOY-HUB.md").splitlines()
    assert [hub_line("DEPLOY-HUB.md")] == [ln for ln in then if ln.startswith("claude --bg ")]
    now = text("DEPLOY-HUB.md").splitlines()
    only(now, P1)
    only(then, P1)
    assert [ln for ln in now if not ln.startswith(P1)] == [ln for ln in then if not ln.startswith(P1)]


# ---- H2: BUILD-HUB, the fix round's FIXED line per held id (R1309 row A) -----------------------

def test_h2_the_build_hub_states_the_fixed_line_per_held_id():
    t = text("BUILD-HUB.md")
    ls = t.splitlines()
    hits = [i for i, ln in enumerate(ls) if ln.startswith(FIX_ROUND)]
    assert len(hits) == 1, hits
    i = hits[0]
    line = ls[i]
    assert line == H2_LINE
    for literal in ("FIXED: <finding id> — <test id>", "CARRIED: <finding id> — <test id> — R<n>",
                    "every held id", "fails the deploy's P2 read"):
        assert literal in line, literal
    assert ls[i - 1].startswith(TIP_LINE), ls[i - 1]
    assert t.count(TOKENS) == 1 and TOKENS in ls[i - 1]


# ---- H3: BUILD-HUB, no untracked file at the stop line (R1309 row B) ---------------------------

def test_h3_the_build_hub_stop_line_step_names_no_untracked_file():
    ls = text("BUILD-HUB.md").splitlines()
    hits = [ln for ln in ls if "no untracked file at the stop line" in ln]
    assert len(hits) == 1, hits
    line = hits[0]
    assert line.startswith(CLOSE_LAST), line
    assert line.count("SHADOW-INSTRUCTIONS.md") == 1
    assert line.count("## <BRANCH>") == 1
    then = only(base_text("BUILD-HUB.md").splitlines(), CLOSE_LAST)
    assert then.count(H3_OLD) == 1
    assert line == then.replace(H3_OLD, H3_NEW)


def test_h3_the_launcher_still_carries_the_shadow_exception():
    assert LAUNCH.read_text(encoding="utf-8").count("?? SHADOW-INSTRUCTIONS.md") == 1
