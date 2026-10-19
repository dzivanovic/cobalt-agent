"""CARD.md's migration checklist (card 2026-10-13 448 C1): a migration that creates a table adds its
grant.

The real file of this tree is read as text, as tests/ops/test_prodwrite_hub.py reads it; the
section is split out the same way (`\\n## ` ends it).
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
HEAD = "## A MIGRATION ROW, CHECKLIST"


def _text() -> str:
    return (HUBS / "CARD.md").read_text(encoding="utf-8")


def test_k1_card_md_holds_the_migration_checklist_once():
    assert _text().count(f"\n{HEAD}") == 1


def test_k2_the_checklist_names_the_grant_its_pin_and_the_gate_lists():
    section = _text().split(f"\n{HEAD}", 1)[1].split("\n## ", 1)[0]
    for needle in ("cobalt_apply_<side>", "GRANT SELECT, INSERT, UPDATE, DELETE", "test_dml_roles_db.py",
                   "gate-lists.md", "CREATED_TABLES"):
        assert needle in section, needle
