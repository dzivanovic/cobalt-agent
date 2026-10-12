"""CHECK-HUB.md's shadow lines (card prompts/2026-10-11/386-launcher-shadow-check-card.md L2, L6, L8).

Read on the real file, as tests/ops/test_hub_lines.py reads it. The hub lines are the brain's and
the drafter's wording, byte for byte; the launch line and THE MECHANICAL ROWS bullet stay as they
are at `git show HEAD:`.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUB_REL = "docs/40 - DevDocs/prompts/CHECK-HUB.md"
HUB = REPO / HUB_REL

L2_LINE = (
    "On a shadow card the check counts and holds findings exactly as on any card and fixes none. "
    "Its stop line writes `held: <n> (opus-own <a> · house <b>)`; on a Grok-built shadow, Grok's own "
    "findings are written apart as `grok-own <g>` and not counted in `<a>` ([F-03]). It writes "
    "`ready: N/A (shadow, never deployed)`. The grade is read from `opus-own <a>` against the "
    "original's Opus-own held count (SHADOW-HUB :76, [F-04])."
)
L6_LINE = (
    "CHECK-HUB §7(v) and `## PREFLIGHT`: on a shadow card, `?? SHADOW-INSTRUCTIONS.md` at the "
    "worktree root is expected and recorded, not a finding."
)
L8_LINE = (
    "On a shadow card the build report's last non-blank line starts SHADOW BUILT · job: <JOB> · "
    "tip: <TIP> and carries no self-check field; preflight.sh checks it so."
)


def lines() -> list[str]:
    return HUB.read_text(encoding="utf-8").splitlines()


def head_lines() -> list[str]:
    out = subprocess.run(["git", "show", f"HEAD:{HUB_REL}"], cwd=REPO, capture_output=True,
                         text=True, check=True).stdout
    return out.splitlines()


def at(prefix: str, of: list[str] | None = None) -> int:
    hits = [i for i, ln in enumerate(of if of is not None else lines()) if ln.startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]


def test_l2_the_shadow_line_sits_after_no_second_pass_and_before_laws():
    text = lines()
    hits = [i for i, ln in enumerate(text) if ln.startswith("On a shadow card the check counts and holds findings")]
    assert len(hits) == 1, hits
    line = text[hits[0]]
    assert line == L2_LINE
    for part in ("fixes none", "held: <n> (opus-own <a> · house <b>)", "grok-own <g>",
                 "ready: N/A (shadow, never deployed)", "[F-03]", "[F-04]"):
        assert part in line, part
    assert at("NO SECOND PASS, NO FURTHER HOUSE") < hits[0] < at("## LAWS")


def test_l2_the_launch_line_is_unchanged():
    now = [ln for ln in lines() if ln.startswith("claude --bg ")]
    then = [ln for ln in head_lines() if ln.startswith("claude --bg ")]
    assert len(now) == 1
    assert now == then
    assert now[0].count("--permission-mode dontAsk") == 1


def test_l6_the_instructions_sentence_sits_under_preflight_and_under_7():
    text = lines()
    hits = [i for i, ln in enumerate(text) if ln == L6_LINE]
    assert len(hits) == 2, hits
    assert at("## PREFLIGHT") < hits[0] < at("## 1. ")
    assert at("## 7. ") < hits[1] < at("## 8. ")
    assert text[hits[1] - 1].startswith("(i) ")


def test_l8_the_shadow_built_line_sits_directly_under_the_mechanical_rows_bullet():
    text = lines()
    hits = [i for i, ln in enumerate(text) if ln.startswith("On a shadow card the build report's last non-blank line")]
    assert len(hits) == 1, hits
    line = text[hits[0]]
    assert line == L8_LINE
    assert "SHADOW BUILT · job: <JOB> · tip: <TIP>" in line
    assert "no self-check field" in line
    bullet = at("- THE MECHANICAL ROWS")
    assert at("## PREFLIGHT") < hits[0] < at("## 1. ")
    assert hits[0] == bullet + 1
    assert text[bullet] == head_lines()[at("- THE MECHANICAL ROWS", head_lines())]
