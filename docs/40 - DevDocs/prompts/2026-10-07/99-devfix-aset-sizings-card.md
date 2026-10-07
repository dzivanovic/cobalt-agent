# Devfix card: cobalt db dev-rebuild user.aset_sizings

JOB: devfix-aset-sizings-1007
LADDER: OFF-LADDER — reports/deploy-radar-direction-color-1007.md 2026-10-07 R638
BRANCH: ops/devfix-aset-sizings-1007
WORKTREE: devfix-aset-sizings-1007
BASE: 73cbf7a1
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-aset-sizings-2026-10-07.md
RULINGS: 2026-10-07 R625
TABLE: user.aset_sizings
PROOF TEST: tests/cobalt/test_dev_rebuild_db.py::test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings

## RECORDS
- `user.aset_sizings` 1538 of 1600 at the `cobalt_dev` slot guard (`reports/deploy-radar-direction-color-1007.md:5`, `:86`, `:124`).
- 1534 before the forward migrate of 0014–0022; the migrate took `max_attnum` 1534 → 1538 (`:93-95`).
- The proof test asserts `slot_report` equals the slot read; the rebuild's `REBUILT … max_attnum <b> → <a>` line proves the drop.
