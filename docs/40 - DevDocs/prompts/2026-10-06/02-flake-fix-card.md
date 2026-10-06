JOB: flake-fix
LADDER: OFF-LADDER — cto-2026-10-03.md R326
BRANCH: ops/flake-fix-1006
WORKTREE: flake-fix-1006
BASE: d1adf256
TIP:
REPORT: /Users/cobalt/cobalt-wt/flake-fix-1006/docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md
CHECK REPORT:
HOUSE B:
RULINGS: 2026-10-03 R326, 2026-10-05 R412

## ROWS

WHY: four with-DB runs failed on `psycopg.errors.DeadlockDetected` at the migration step; each blocker is a Postgres autovacuum worker, not a second writer (`reports/second-writer-survey-2026-10-05.md` lines 5, 35-38; the survey ran under R326, and the brain's judgment of it is R479, a desk record). The fix is test-side only: no production code, no migration file, no server setting. The last failure: `test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current`, setup ERROR in the `migrated` fixture at `tests/cobalt/test_drc_store.py:237` `_apply(conn, FORWARD)` (`reports/deploy-deploy-k3-1005-attempt2.md` lines 6 and 160).

| row | what | red first | files |
|---|---|---|---|
| F1 | THE `migrated` FIXTURE RETRIES THE MIGRATION STEP ON DEADLOCK. The fixture that applies the migrations to `cobalt_dev` is `migrated` at `tests/cobalt/test_drc_store.py:231-249` (not a `conftest.py` fixture: `tests/cobalt/conftest.py` holds no migration step); `test_drc_k2_experiments.py:49` imports it by name, as do other with-DB files. It opens `db.connect_migration(env.DEV_DB_NAME)` (line 233), sets `autocommit = False`, and runs `_apply(conn, FORWARD)` (line 237). The fixture retries the WHOLE step (open, `autocommit = False`, `_apply(conn, FORWARD)`) on `psycopg.errors.DeadlockDetected`, at most twice (three attempts in all), each attempt a fresh connection and transaction (the failed attempt's connection is rolled back and closed first), and prints `migration retry <n>: DeadlockDetected` (n = 1, 2) each time. Any other error, or a third deadlock, propagates as today. The rest of the fixture (the `_connect` monkeypatch, the final rollback and close) is unchanged | in `tests/cobalt/test_drc_store.py`, `@requires_db`: ADD `test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks` (a helper fixture, listed BEFORE `migrated` in the test's arguments, monkeypatches this module's `_apply` so its first call raises `psycopg.errors.DeadlockDetected` and later calls run the real `_apply`; the test gets the fixture with `request.getfixturevalue("migrated")` and asserts the printed output holds `migration retry 1: DeadlockDetected` and that a table of `TABLES` exists on the returned connection). RED on `BASE`: the test FAILS (not a setup error) with `psycopg.errors.DeadlockDetected` raised out of `request.getfixturevalue("migrated")`, because the fixture has no retry. ADD `test_the_migrated_fixture_fails_on_a_third_deadlock_after_two_retries` (the patched `_apply` always raises `DeadlockDetected` → `getfixturevalue` raises `DeadlockDetected`, output holds `migration retry 1:` and `migration retry 2:` and no `migration retry 3`): RED on `BASE` for the missing print lines. ADD a negative control, green on `BASE` and after (say so in the report): `test_the_migrated_fixture_does_not_retry_another_error` (the patched `_apply` raises `psycopg.errors.UndefinedTable` → raised at once, output holds no `migration retry`). The red tests needs `POSTGRES_HOST` and `POSTGRES_USER` (the tests skip offline); run with-DB under the one `cobalt_dev` lock per `BUILD-HUB.md` | `tests/cobalt/test_drc_store.py` |

Deploy gate: the row ends with the gate, not a smoke of its own. The job's tip deploys only through `DEPLOY-HUB.md` (one feature per deploy); the gate's with-DB pass runs the whole suite green on the combined tree before the merge, and the fixture's retry is what the gate's STEP-G reads for a `DeadlockDetected` setup ERROR.

## NOT IN THIS JOB
- Any `src/` file; any file under `src/cobalt/db_migrations/` (migrations `0002` and `0007` are production DDL and stay as they are); `tests/cobalt/conftest.py` (it holds no migration step).
- Disabling autovacuum or any server setting (the server may also host production; the brain's judgment (R479, a desk record) puts the fix test-side: a retry in the migration fixture).
- The other tests that open `db.connect_migration` and run `_apply(conn, FORWARD)` themselves (`test_p4_migrations.py`, `test_voice_store.py`, `test_archiver_migrations.py`, `radar_migrated_support.py`, `test_drc_d2_fix_r1_db.py` and others): not changed here; a card of their own if one deadlocks.
- A new command, script or `ops/desk/` change: the build seat uses only its allow line (R412).
- A red outside this row: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `tests/cobalt/test_drc_store.py` lines 12-34 (imports), 48-51 (`requires_db`), 231-249 (`migrated`), 292-330 (the tests that use it).
- `src/cobalt/db_migrations/cli.py:631-642` (`_apply`: whole `.sql` files in one transaction) and `src/cobalt/db.py:269` (`connect_migration`).
- `tests/cobalt/test_drc_k2_experiments.py:41-49` and `:332` (`test_x9`, the flaky test).
- `reports/second-writer-survey-2026-10-05.md` lines 5, 35-44; `reports/deploy-deploy-k3-1005-attempt2.md` lines 6, 160.

## CHECK ASKS
- X1 Does the diff touch only `tests/cobalt/test_drc_store.py`, and inside it only the `migrated` fixture and the new tests?
- X2 Does each retry attempt open a fresh `connect_migration` connection and a fresh transaction, with the failed one rolled back and closed first (no connection leaked)?
- X3 Is a third deadlock, and any error that is not `DeadlockDetected`, raised as before?
- X4 Is the red test red on `BASE` for the stated reason (the raise out of `getfixturevalue`), not for a setup error or a skip?

## RECORDS
- Proved against BASE `d1adf256` (`git -C /Users/cobalt/cobalt rev-parse HEAD`, 2026-10-06): every `file:line` above read from the working tree, which `git status` shows clean for `tests/cobalt/test_drc_store.py`, `tests/cobalt/conftest.py` and both ruling files; the drafter's report holds each read.
- R326 is row 332 of `reports/cto-2026-10-03.md` (`HIS RULING`, `APPROVED`); R412 is row 109 of `reports/cto-2026-10-05.md` (`HIS RULING`, `APPROVED`); both files are committed.
