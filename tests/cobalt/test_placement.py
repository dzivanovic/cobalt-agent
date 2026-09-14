"""docs/PLACEMENT.md, enforced — the 2026-09-13 tree-cleanup sweep.

Three shapes: a tree that should pass clean, one with a violation in
each of the two areas this sweep actually polices (docs/00 - Project/
and docs/_inflight/), and the COBALT_INFLIGHT_OK escape hatch.
"""

import pytest

from cobalt.placement.check import check_tree


def _make_tree(tmp_path, entries):
    for rel, content in entries.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content)
    return tmp_path


def test_passing_tree_is_clean(tmp_path):
    tree = _make_tree(
        tmp_path,
        {
            "PLACEMENT.md": "map",
            "00 - Project/PROJECT-LEDGER.md": "ledger",
            "00 - Project/BACKLOG.md": "backlog",
            "00 - Project/COBALT-REQUIREMENTS.md": "reqs",
            "00 - Project/README.md": "readme",
            "00 - Project/MVP-CHARTER-v0_2.md": "charter",
            "00 - Project/SPRINT-LADDER-v0_1.md": "ladder",
            "00 - Project/INCIDENT-2026-09-03-notes.md": "notes",
            "40 - DevDocs/plans/plan-x.md": "plan",
            "40 - DevDocs/reports/report-x.md": "report",
            "40 - DevDocs/incidents/2026-09-11-foo/notes.md": "incident",
            "40 - DevDocs/INDEX.md": "index",
            "40 - DevDocs/cobalt/foo.md": "wiki",
            "_inflight/README.md": "readme",
            "10 - Decisions/ADR-0001.md": "adr",
            "20 - Assessment/ASSESSMENT.md": "assessment",
            "30 - Design/design.md": "design",
            "50 - Roles/MODELS.md": "models",
            "60 - Agent Output/Morning_Briefing_2026-09-13.md": "briefing",
            "_archive/captures/2026-09-10/whatever.md": "capture",
            "90 - References/INDEX.md": "index",
            "90 - References/random-licensed-asset.pdf": "asset",
        },
    )
    assert check_tree(tree) == []


def test_stray_file_at_docs_root_fails(tmp_path):
    tree = _make_tree(tmp_path, {"STRAY-NOTES.md": "oops"})
    violations = check_tree(tree)
    assert len(violations) == 1
    assert "STRAY-NOTES.md" in violations[0]


def test_00_project_disallows_unlisted_file(tmp_path):
    tree = _make_tree(
        tmp_path,
        {"00 - Project/PROJECT-LEDGER.md": "ledger", "00 - Project/capture-dump.md": "dump"},
    )
    violations = check_tree(tree)
    assert len(violations) == 1
    assert "capture-dump.md" in violations[0]
    assert "allowlist" in violations[0]


def test_00_project_disallows_subdirectory(tmp_path):
    tree = _make_tree(
        tmp_path, {"00 - Project/incident-2026-09-03/dump.sql": "dump"}
    )
    violations = check_tree(tree)
    assert len(violations) == 1
    assert "no subdirectories" in violations[0]


def test_inflight_disallows_extra_files(tmp_path):
    tree = _make_tree(
        tmp_path,
        {"_inflight/README.md": "readme", "_inflight/plan-leftover.md": "stale"},
    )
    violations = check_tree(tree)
    assert len(violations) == 1
    assert "plan-leftover.md" in violations[0]


def test_inflight_ok_env_escape_hatch(tmp_path, monkeypatch):
    tree = _make_tree(
        tmp_path,
        {"_inflight/README.md": "readme", "_inflight/plan-leftover.md": "stale"},
    )
    monkeypatch.setenv("COBALT_INFLIGHT_OK", "1")
    assert check_tree(tree) == []


def test_missing_docs_root_is_clean(tmp_path):
    assert check_tree(tmp_path / "does-not-exist") == []
