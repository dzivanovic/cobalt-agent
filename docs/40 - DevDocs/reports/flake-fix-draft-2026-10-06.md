## §0 Headline
- Card written: one row F1, test-side only, BASE `d1adf256`, no `«FILL` token.
- The fixture is `migrated` in `tests/cobalt/test_drc_store.py:231`, not a `conftest.py` fixture; the card's one file is that test file.
- Red: a test whose first migration attempt raises `DeadlockDetected` fails on BASE; one more red (third deadlock), one negative control.
- Nothing was run (no database, no pytest): every red claim is derived from reading the code, UNPROVEN until the build.

## CARD
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md`

## DECISIONS
1. The brain's row says "the fixture's `conftest.py` and one test file". `tests/cobalt/conftest.py` holds no migration step; the fixture `test_x9` used is `migrated` in `test_drc_store.py`. The card names `tests/cobalt/test_drc_store.py` as the only file (fixture and new tests together) and fences `conftest.py` out. Answer needed only if he wants the fixture moved into `conftest.py` (a larger change, not done).

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse HEAD` → `d1adf256102cbab146d8b13e0fcd3bac4f853938`: BASE `d1adf256`.
- `grep -n "migrat" tests/cobalt/conftest.py` (via Grep over `tests/**/conftest.py`): lines 161, 162, 286, 287 only (the slot read and a docstring); no fixture applies migrations there.
- Read `tests/cobalt/test_drc_store.py` 200-295: `migrated` at 231-249; `connect_migration` line 233, `autocommit = False` 234, `_apply(conn, FORWARD)` 237, `_connect` monkeypatch 239-245, rollback and close 247-249. `requires_db` at 48-51. Imports `_apply` from `cobalt.db_migrations.cli` at line 26.
- Read `src/cobalt/db_migrations/cli.py:631-642`: `_apply` runs each file whole, one transaction. `src/cobalt/db.py:269`: `connect_migration`.
- `tests/cobalt/test_drc_k2_experiments.py:41-49` imports `migrated` from `test_drc_store`; `:332` `test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current(migrated)`.
- `reports/deploy-deploy-k3-1005-attempt2.md` lines 6 and 160: the setup ERROR `DeadlockDetected` in `migrated` (`test_drc_store.py:237`) for `test_x9`. `grep -n DeadlockDetected` on `deploy-deploy-k3-1005.md` and `deploy-deploy-k3-1005-attempt3.md` prints nothing: only attempt2 holds the line; the card cites attempt2.
- `reports/second-writer-survey-2026-10-05.md` lines 5, 35-38, 43-44: autovacuum is the blocker; "retry on `DeadlockDetected`" is a listed direction.
- `grep -n "^| R326 \|^| R412 "`: `reports/cto-2026-10-03.md:332` R326 `HIS RULING … APPROVED`; `reports/cto-2026-10-05.md:109` R412 `HIS RULING … APPROVED`. `git ls-files` lists both, `git status --short` for both prints nothing (committed, clean).
- Other with-DB files that open `connect_migration` and run `_apply(conn, FORWARD)` themselves (`grep -rn` over `tests/`): listed in the card's `## NOT IN THIS JOB`, not changed.
- `grep -c "«FILL"` on the card → 0.

FLAKE FIX DRAFTED · decisions: 1
