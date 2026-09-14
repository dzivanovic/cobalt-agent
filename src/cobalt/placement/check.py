"""Placement-law sweep (F16 gate) — docs/PLACEMENT.md's map, enforced.

Scope, per docs/PLACEMENT.md: every file under `docs/` except the two
tiers PLACEMENT.md excludes outright (`_archive/` — captures are
gitignored but still live on disk; `90 - References/` — untracked working
material). Four D6 tiers PLACEMENT.md does not re-litigate
(`10 - Decisions`, `20 - Assessment`, `30 - Design`, `50 - Roles`) pass
through unchecked — they stay governed by CLAUDE.md's Documentation
standard, not by this sweep. `40 - DevDocs/` also carries the
per-.py-file wiki proper (`cobalt/`, `ops/`, `tests/`, `INDEX.md`, loose
topic docs) alongside the `plans/`/`reports/`/`incidents/` substructure
this cleanup added — both pass.

`00 - Project/` and `_inflight/` are the two tiers this sweep actually
polices, because those are the two areas the 2026-09-13 cleanup found
sprawling: captures and per-session dumps landing loose in the project
record, and duplicate in-flight copies never cleared at merge.
"""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DOCS_ROOT = REPO_ROOT / "docs"

_IGNORED_NAMES = {".DS_Store"}

#: Top-level docs/ entries this sweep recognizes at all. Everything else
#: directly under docs/ is a violation — CLAUDE.md's "never at repo root,
#: never in a new ad-hoc folder" applies one level down too.
_KNOWN_TOP_LEVEL = {
    "00 - Project",
    "10 - Decisions",
    "20 - Assessment",
    "30 - Design",
    "40 - DevDocs",
    "50 - Roles",
    "60 - Agent Output",
    "90 - References",
    "0 - Inbox",
    "_archive",
    "_inflight",
    "PLACEMENT.md",
}

#: Tiers this sweep excludes from recursion entirely (own rules elsewhere:
#: _archive/captures/ is gitignored-but-kept, 90 - References/ is
#: untracked-except-INDEX.md via .gitignore, not this validator).
_UNCHECKED_SUBTREES = {"_archive", "90 - References"}

#: docs/00 - Project/ — canonical CLAUDE.md residents plus this cleanup's
#: additions. Exact filenames, then prefix patterns.
_PROJECT_EXACT = {
    "PROJECT-LEDGER.md",
    "BACKLOG.md",
    "COBALT-REQUIREMENTS.md",
    "README.md",
}
_PROJECT_PREFIXES = (
    "MVP-CHARTER",
    "SPRINT-LADDER",
    "TRIAGE",
    "INCIDENT-",
)


def _project_file_allowed(name: str) -> bool:
    if name in _PROJECT_EXACT:
        return True
    if name.startswith(_PROJECT_PREFIXES):
        return True
    # Dated ledger appendix files, e.g. PROJECT-LEDGER-appendix-2026-09-13.md
    if name.startswith("PROJECT-LEDGER-"):
        return True
    return False


def check_tree(docs_root: Path | None = None) -> list[str]:
    """Return placement-law violations for `docs_root` (default: repo
    docs/). Empty list = clean tree."""
    root = docs_root if docs_root is not None else DOCS_ROOT
    violations: list[str] = []
    inflight_ok = os.environ.get("COBALT_INFLIGHT_OK") == "1"

    if not root.is_dir():
        return violations

    for entry in sorted(root.iterdir()):
        if entry.name in _IGNORED_NAMES:
            continue
        if entry.name not in _KNOWN_TOP_LEVEL:
            violations.append(
                f"{entry.relative_to(root.parent)}: not a directory named in "
                "docs/PLACEMENT.md — file into one of the sanctioned tiers, "
                "never at repo root or in a new ad-hoc folder"
            )
            continue
        if entry.name in _UNCHECKED_SUBTREES:
            continue
        if entry.name == "PLACEMENT.md":
            continue
        if entry.name == "_inflight":
            if not entry.is_dir():
                continue
            for f in sorted(entry.rglob("*")):
                if f.is_dir() or f.name in _IGNORED_NAMES:
                    continue
                if f.name == "README.md" and f.parent == entry:
                    continue
                if inflight_ok:
                    continue
                violations.append(
                    f"{f.relative_to(root.parent)}: docs/_inflight/ may hold only "
                    "README.md (set COBALT_INFLIGHT_OK=1 for a deliberate in-flight "
                    "window)"
                )
            continue
        if entry.name == "00 - Project":
            if not entry.is_dir():
                continue
            for f in sorted(entry.iterdir()):
                if f.name in _IGNORED_NAMES:
                    continue
                if f.is_dir():
                    violations.append(
                        f"{f.relative_to(root.parent)}: docs/00 - Project/ holds "
                        "record files only, no subdirectories"
                    )
                    continue
                if not _project_file_allowed(f.name):
                    violations.append(
                        f"{f.relative_to(root.parent)}: not on docs/00 - Project/'s "
                        "allowlist (PROJECT-LEDGER.md, BACKLOG.md, "
                        "COBALT-REQUIREMENTS.md, README.md, MVP-CHARTER*, "
                        "SPRINT-LADDER*, a TRIAGE pointer, dated ledger-appendix or "
                        "INCIDENT-*-notes.md files)"
                    )
            continue
        # Every other known tier (including 40 - DevDocs's plans/reports/
        # incidents substructure, and the four untouched D6 tiers) passes
        # through: this sweep polices sprawl, not the whole tree's shape.

    return violations
