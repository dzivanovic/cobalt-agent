"""CARD.md, the job card's fixed format (card 2026-10-14 550 C1, C2; his R1471 item 6, brain R1472).

The real file of this tree is read as text, as tests/ops/test_prodwrite_hub.py reads it; every
line is found by its content. Only the lines rows C1 and C2 add are pinned: no commit is read and
no line is compared to one (brain R1472).
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"

# The placeholder token desk-launch.sh refuses, built here so this file holds no literal of it.
FILL = chr(0xAB) + "FILL"

PROOF_START = "`## DEPLOY PROOF` (build, check; REQUIRED"
CITES = "## HOW A CARD CITES AND PINS"


def _lines() -> list[str]:
    return (HUBS / "CARD.md").read_text(encoding="utf-8").splitlines()


def _one(lines: list[str], start: str) -> int:
    hits = [n for n, ln in enumerate(lines) if ln.startswith(start)]
    assert len(hits) == 1, (start, hits)
    return hits[0]


def test_c1_card_md_requires_deploy_proof_once_between_check_asks_and_records():
    lines = _lines()
    hits = [n for n, ln in enumerate(lines) if ln.startswith(PROOF_START)]
    assert len(hits) == 1
    i = hits[0]
    line = lines[i]
    for needle in ("· before ", "· after ", "deploy-card.sh:534-543", "`## MARKERS`",
                   "`## SMOKE READS`", FILL):
        assert needle in line, needle
    assert _one(lines, "`## CHECK ASKS`") < i < _one(lines, "`## RECORDS`")


def test_c2_card_md_states_the_citing_and_pinning_rules_once():
    lines = _lines()
    heads = [n for n, ln in enumerate(lines) if ln == CITES]
    assert len(heads) == 1
    h = heads[0]
    end = next(n for n in range(h + 1, len(lines)) if lines[n].startswith("## "))
    section = lines[h + 1:end]
    for start in ("- RULINGS:", "- ANCHORS:", "- TESTS:", "- DEPLOY PROOF:"):
        assert sum(ln.startswith(start) for ln in section) == 1, start
    text = "\n".join(section)
    for needle in ("his R1471", "brain R1472", "a whole fixed-file line equal to a commit",
                   "a BASE hash"):
        assert needle in text, needle
    last = _one(lines, "- State of the desk (a meter that is out, a tab id, a watch id).")
    example = _one(lines, "## EXAMPLE 1 — the E1 fix, at its BUILD launch")
    assert last < h < example


# Fix round (card 2026-10-15 597, FR-O1, FR-O2, FR-G2, FR-G3): the C1 line and the C2 section,
# found by their content.

CREDIT = ("his R1471 (6): rulings by R number, no HEAD hashes, anchors by file:line; the rest per "
          "the brain's gap-filler rows (handover 520 OWED 6, DESK RECORD)")


def _proof_line(lines: list[str]) -> str:
    return lines[_one(lines, PROOF_START)]


def _cites_text(lines: list[str]) -> str:
    h = _one(lines, CITES)
    end = next(n for n in range(h + 1, len(lines)) if lines[n].startswith("## "))
    return "\n".join(lines[h + 1:end])


def test_fr_o1_both_credits_read_r1471_6_and_the_gap_filler_rows():
    lines = _lines()
    line, text = _proof_line(lines), _cites_text(lines)
    assert CREDIT in line
    assert CREDIT in text
    assert "R1471 item 6" not in line
    assert "R1471 (item 6)" not in text


def test_fr_o2_marker_clause_is_the_markers_form_with_grep_or_ls():
    line = _proof_line(_lines())
    assert "marker lines in the form of `## MARKERS` (grep -c -F or ls)" in line
    assert "per file" not in line


def test_fr_g2_smoke_line_carries_a_label_first():
    line = _proof_line(_lines())
    assert "label · the command typed whole · what a green answer looks like" in line


def test_fr_g3_refusal_clause_cites_desk_launch_994_and_deploy_card_31():
    line = _proof_line(_lines())
    assert "does not launch (`desk-launch.sh:994`, `deploy-card.sh:31`)" in line
