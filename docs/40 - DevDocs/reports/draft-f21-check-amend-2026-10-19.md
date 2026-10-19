## §0 Headline
Card 820 amended: row S0 and the `Range files` line now say 42 paths (were 37). Count proven by reading the command's output line by line.
Parts sum to 42: 8 DevDocs pages + 1 gate-lists + 1 `cli.py` + 4 `db_migrations` + 5 `genesis` modules + 2 fixtures + 21 tests (3 genesis + 18 moved pins). "Eighteen moved pin files" holds. Nothing else changed. Nothing committed.

## DECISIONS
None.

## RECORDS
- 2026-10-19 07:32 EDT (`date`). Command: `git -C /Users/cobalt/cobalt diff --name-only --no-renames 40e646ed 66439da6`; I counted the lines I read: docs 8, `ops/desk/gate-lists.md` 1, `src/cobalt/cli.py` 1, `db_migrations` (two `0026` sql, `__init__.py`, `placement.py`) 4, `genesis` modules 5, fixtures 2, tests 21 (minus `test_genesis_db`, `test_genesis_experiments_db`, `test_genesis_offline` = 18 pin files) = 42.
- Edits: `820-f21-genesis-check-card.md` line 22 (row S0) and line 77 (`Range files`), "37" → "42" only.

DRAFTED · decisions: 0
