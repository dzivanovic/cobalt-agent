## CHECKS

Card: `prompts/2026-10-06/02-flake-fix-card.md`. Nothing was run but read-only git, grep and ls. No test was run.

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor d1adf256 main` | exit 0, no output | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/flake-fix-1006` | `fatal: Needed a single revision` (exit 128): the branch is new | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/flake-fix-1006` | `No such file or directory`: the worktree is new | OK |
| 1d | read the card header | `TIP:`, `CHECK REPORT:` and `HOUSE B:` are empty. JOB, LADDER, BRANCH, WORKTREE, BASE, REPORT (inside the worktree) and RULINGS are present. There is no `DB:` line, which `CARD.md` allows because the files are under `tests/cobalt/` (a with-DB job takes the lock). | OK |
| 2a | `grep -n "^| R326 " reports/cto-2026-10-03.md` | `332:\| R326 \| 10-05 06:19 ET \| HIS RULING: A on all three … \| HIS RULING · APPROVED \|` | OK |
| 2b | `grep -n "^| R412 " reports/cto-2026-10-05.md` | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|` | OK. `HIS RULING` and `APPROVED` both appear. |
| 2c | `git log -1 --format=%h -S"\| R326 \|" -- …cto-2026-10-03.md` | `b1337431` | OK |
| 2d | `git log -1 --format=%h -S"\| R412 \|" -- …cto-2026-10-05.md` | `b3583b28` | OK |
| 3a | `grep -n` on `tests/cobalt/test_drc_store.py`; `git diff --stat d1adf256 --` on the four files is empty, so the tree equals BASE | `26:from cobalt.db_migrations.cli import _apply, _rollback_paths`; `48:requires_db = pytest.mark.skipif(`; `232:def migrated(monkeypatch):`; `233:conn = db.connect_migration(env.DEV_DB_NAME)`; `234:conn.autocommit = False`; `237:_apply(conn, FORWARD)`; `245:monkeypatch.setattr(db, "connect", _connect)`; `248:conn.rollback()`; `249:conn.close()`. The decorator is on line 231 (`@pytest.fixture`), so `migrated` spans 231-249. | OK |
| 3b | `src/cobalt/db_migrations/cli.py:631-642` | `631:def _apply(conn, paths) -> None:` … `640: for path in paths:` `641: print(f"-- applying {path.name}")` `642: conn.execute(path.read_text())`. Whole `.sql` files, one transaction. | OK |
| 3c | `src/cobalt/db.py:269` | `def connect_migration(dbname: str, *, allow_prod: bool = False) -> psycopg.Connection:` | OK |
| 3d | `grep -n migrated tests/cobalt/test_drc_k2_experiments.py` | line 49 `migrated,` (the import block, which the drafter read as 41-49); `332:def test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current(migrated):` | OK |
| 3e | `tests/cobalt/conftest.py`, `grep -n migrat` | lines 161, 162, 286, 287 only: an import of `SLOT_WARN_AT` and docstrings. There is no migration fixture. | OK |
| 3f | `second-writer-survey-2026-10-05.md` lines 5, 35-38, 43-44 | line 5: "every blocker is a Postgres **autovacuum worker**". Lines 35-38 are the four rows K3-1, K3-2, D5-1 and D5-2. Line 44: "Fix directions (not applied …): disable autovacuum …, or retry on `DeadlockDetected`, or order lock acquisition." | OK |
| 3g | `deploy-deploy-k3-1005-attempt2.md` lines 6 and 160 | line 6: `psycopg.errors.DeadlockDetected in the migrated fixture (tests/cobalt/test_drc_store.py:237 _apply(conn, FORWARD))` of `test_x9…`. Line 160: `FAILED: gate — G (c) — … test_x9 … setup ERROR psycopg.errors.DeadlockDetected`. | OK |
| 3h | card line 14: "judged by the brain, R326"; `## NOT IN THIS JOB` line 24: "his R326 rejected it" (disabling autovacuum) | R326's row (332) rules A on three items: D5 ships pinned, the survey gets its 5 read strings, F15 P2 X11 goes to a follow-up. Its words (`cto-2026-10-05-words.md` lines 3-4) do not mention autovacuum, a retry or the flake. `grep -n -i -E "R326\|autovacuum"` on that file returns only the heading. R326 does not reject disabling autovacuum and does not rule on this fix. | FAIL |
| 4a | read the fixture at BASE (231-249) and the card's red test | `_apply` is read as a module global at call time, so a monkeypatch of this module's `_apply` takes effect. BASE has no retry, so a first call that raises `DeadlockDetected` propagates out of the fixture. Inside `request.getfixturevalue("migrated")` that is a test failure, not a setup error and not a skip. `conn.rollback()` and `conn.close()` run in `finally`, so there is no leak. | OK (red for the stated reason) |
| 4b | card's third-deadlock test | BASE raises on the first attempt and prints no `migration retry` line, so the `retry 1:` and `retry 2:` assertions fail. After the fix, three attempts print retries 1 and 2, the third raises, and there is no `retry 3`. | OK (red for the missing prints) |
| 4c | card's green leg and negative control | Green: the first call raises before any SQL runs, the second runs the real `_apply` on a fresh connection, and the tables exist. Negative control: `UndefinedTable` is not `DeadlockDetected`, so it propagates at once, and BASE and the fix both print no `migration retry`. | OK (green on BASE and after, as the card says) |
| 5 | read the card's rows, files and fence | The only file is `tests/cobalt/test_drc_store.py`. There is no `src/` change, migration file or server setting, and no new command (`## NOT IN THIS JOB` forbids one, citing R412). The `cobalt_dev` lock is the one `BUILD-HUB.md` already names. | OK |
| 6a | `grep -c -F "«FILL" …02-flake-fix-card.md` | `0` | OK |
| 6b | `git diff --stat -- <card> <draft report>` | empty | OK |
| 6c | `git log -1 --format=%h -- <card>`; `-- <draft report>` | `e849653f`; `e849653f` | OK |

## ISSUES
- Check 3h: the card attributes to R326 two things R326 does not hold, namely "judged by the brain, R326" for the autovacuum finding and "his R326 rejected it" for disabling autovacuum. Neither is in R326's row or words. Fix: reword both to name the survey report (lines 5, 35-44) and, if the brain's row is the authority, cite that row's R-number. Add it to `RULINGS` and to the LADDER line if it is a ruling. No code fact is affected.

PREFLIGHT DONE · card: flake-fix-02 · checks: 24 · fails: 1 · ready: NO
