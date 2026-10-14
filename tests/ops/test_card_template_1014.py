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
