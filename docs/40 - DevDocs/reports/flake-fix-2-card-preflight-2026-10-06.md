# flake-fix-2 card preflight — 2026-10-06 (read-only; no test run)

Card `prompts/2026-10-06/14-flake-fix-2-card.md`; draft report `reports/flake-fix-2-draft-2026-10-06.md`. HEAD = main = `767af53c`; `tests/` on main equals BASE (`git diff --stat 71f69821 main -- tests` empty), so every `file:line` was read from the tree.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git merge-base --is-ancestor 71f69821 main` | exit 0, no output (`rev-parse 71f69821` = `71f6982158ec…`; main = `767af53c`) | OK |
| 1b | `git rev-parse --verify ops/flake-fix-2-1006` | `fatal: Needed a single revision` (branch is new) | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/flake-fix-2-1006` | `No such file or directory` | OK |
| 1d | header read | `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; JOB, LADDER, BRANCH, WORKTREE, BASE, REPORT, RULINGS present. No `DB:` line: `CARD.md` makes `DB` optional, `none` only when every file is under `ops/`, `tests/ops/` or `docs/`, "left out otherwise"; the card's files are under `tests/cobalt/`, so omission is right (the prompt's "DB line present" is read as that) | OK |
| 2a | `grep -n "^| R326 " reports/cto-2026-10-03.md` | `332:\| R326 \| 10-05 06:19 ET \| HIS RULING: A on all three … \| HIS RULING · APPROVED \|`; `log -1 -S"\| R326 \|"` = `b1337431` | OK |
| 2b | `grep -n "^| R412 " reports/cto-2026-10-05.md` | `109:\| R412 \| … \| HIS RULING: drop pre-merge (d2) … \| APPROVED (in cto-desk-contract.md …; launch gate L7a) \|`; `log -1 -S` = `b3583b28` | OK |
| 2c | `grep -n "^| R474 " reports/cto-2026-10-05.md` | `140:\| R474 \| … \| HIS RULING · APPROVED: tonight he is not woken … \| HIS RULING · APPROVED \|`; `log -1 -S` = `548ee01d` | OK |
| 3a | card cites vs tree, `test_drc_store.py` | `migrated` fixture 231-265, loop 237-252 (`range(1, 4)`, print `migration retry {attempt}: DeadlockDetected`), `_patch_apply` 354, fixture tests 392/407/422, open/rollback tests 430 and 456 (to 481), `connect_migration` patched with one-positional-arg lambdas at 445/475 | OK |
| 3b | `test_radar_score_migration.py` | `_migration_conn` 299-302; used 307 (apply 309) and 418 (apply 420, `_apply(conn, FORWARD)`) | OK |
| 3c | `radar_migrated_support.py` | `migrated_radar` 72-95; open 78-79, apply 82; 7 test files import it (`test_cards_picks`, `_radar_handicap_store`, `_radar_handicap_fix_r1_runs`, `_radar_panel`, `_radar_handicap_dry_run`, `_radar_migrated_harness`, `_radar_store`) as the card lists | OK |
| 3d | `test_p4` / `test_voice_store` / `test_archiver` / `test_stale_score_db` / `test_radar_handicap_store` | p4 `_migration_conn` 304-307, 443→446, 485→487, 548→550; voice 165-168, 187→189, 203→205; archiver 446-449, 454→456, 471→473, 504→506; stale 134-139, 172→174; handicap_store `_conn` 145-148, 175→177: all match | OK |
| 3e | `test_tenancy.py`, `test_xl76_membership_harness.py` | tenancy opens 546-549 (`[FWD_0003]`) and 573-577 (`FORWARD`); harness open 150-151, `started` 154, apply 155, `apply_ms` 156; `SRC` 59 and 311 (one-caller lint reads `src/` only) | OK |
| 3f | `grep -rn "_apply(conn, FORWARD)\|_migration_conn()" tests/` | files returned: `test_xl76_membership_harness`, `test_p4_migrations`, `radar_migrated_support`, `test_stale_score_db`, `test_drc_store`, `test_voice_store`, `test_tenancy`, `test_archiver_migrations`, `test_radar_score_migration` = 9 files, all named in the card's files list. The card's own grep also has `connect_migration(`, which adds `test_radar_handicap_store.py` (`_conn` 145; it applies migrations); it is named too. Nothing the card names is outside the two greps | OK (the prompt's narrower grep lacks `test_radar_handicap_store`; the card's broader grep and a read both include it) |
| 3g | non-callers | `test_migrate_proof.py` (probes via `cli._schema_of`, no direct `_apply` on its conn), `test_dev_rebuild_db.py:43` (fixture, `SET LOCAL`), `test_xl76_devdb_absence.py:22` (viewdef reads), `test_db_only_selection.py:458` (inside a `'''…'''` string), `test_xl76_membership_harness.py:182` (catalog read): none applies migrations. Also `test_db_credentials.py:156` and `test_db_only_selection.py:656` open and apply nothing (the card does not name them; fine) | OK |
| 3h | importability of `migration_retry` | `tests/cobalt/` has no `__init__.py`; `radar_migrated_support` is imported bare (`test_radar_store.py:9`); `tests/experiments/handicap_h1/conftest.py:26` inserts `tests/cobalt` on `sys.path`, so item (10) can import it too | OK |
| 4a | red test red on BASE | new `test_the_migration_step_retries_a_first_deadlock` patches the module's `_apply` global (`from … import _apply` at line 31, so `setitem(globals(), "_apply", fake)` is the same mechanism `test_drc_store.py:373` uses); the test calls the existing test, whose line 420 `_apply(conn, FORWARD)` hits `fake`, raises `DeadlockDetected`, `finally` rolls back and closes, and nothing retries, so it fails with `DeadlockDetected` at line 420. `requires_db` is `pytest.mark.skipif` (line 36), so a direct call works; red needs `POSTGRES_HOST`/`POSTGRES_USER`, as the card states | OK |
| 4b | green leg | `open_migrated(_apply, FORWARD)` resolves `_apply` in the test module's globals at call time (the fake), attempt 1 raises, the helper closes that connection, prints `migration retry 1: DeadlockDetected`, attempt 2 runs the real `_apply`; `capsys` holds the line | OK |
| 4c | `test_migration_retry.py` reds and controls | no `migration_retry.py` on BASE (`ls` → No such file), so the import errors (red); `UndefinedTable` is not `DeadlockDetected`, so the loop re-raises at once with no print; a third deadlock hits `attempt == 3` and raises after two prints; the rollback-raises case closes in `finally` (same shape as the fixture, `test_drc_store.py:246-249`, and its test at 456) | OK |
| 5 | no new command | rows use `uv run pytest`, the gate (`ops/desk/gate.sh` via BUILD-HUB W, on the allow line `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`); files all under `tests/`; NOT IN THIS JOB fences `src/`, `src/cobalt/db_migrations/`, `tests/cobalt/conftest.py`, server settings (R411 row 107, R412 row 109) | OK |
| 6a | `grep -c -F "«FILL"` card / draft | card `0`; draft `1` (line 23 is prose: "no `«FILL` token", not a token) | OK |
| 6b | `git diff --stat -- <card> <draft>` | empty | OK |
| 6c | `git log -1 --format=%h -- <card>` / `-- <draft>` | `767af53c` / `767af53c` | OK |

## ISSUES

None. Notes, not fails: (1) the R326 row sits in `cto-2026-10-03.md` but is stamped `10-05 06:19 ET`; the card's `2026-10-03 R326` follows the file. (2) In `test_p4_migrations.py` the `open_migrated(_apply, base)` call must come after `_merge_order_bases(order)` (line 445), which the card's order already allows.

PREFLIGHT DONE · card: flake-fix-2-14 · checks: 24 · fails: 0 · ready: YES
