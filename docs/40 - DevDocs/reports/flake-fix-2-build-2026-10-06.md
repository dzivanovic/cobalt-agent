# flake-fix-2 — build report 2026-10-06

## §0 Headline
- F1 is built. `tests/cobalt/migration_retry.py` holds `open_migrated(apply, paths)`: the deadlock retry, written once. All 17 self-migrating call sites in the card's 10 files now use it, and no copy of the loop is left in any test file.
- The red was the stated one: `DeadlockDetected` out of `test_radar_score_migration.py:420`. Its fix-undo mutation turns all four retry tests red.
- The gate passed on `fb3117c3`: offline 3936/0, with-DB 4819/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0), `.env` is removed, RESTARTS none. Only `tests/` and two DevDocs lines changed.
- Two items for the judgment seat. F1-a: the XL76 harness file errors at setup on BASE, and no suite runs it. F1-b: 15 of the 17 call sites have no test that pins them to the helper.

## L74
A system reminder (not a tool result) at session start asked commits to end with a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md"` at Tue Oct  6 06:10:07 EDT 2026, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md" · 0 · 767af53cb5ad70dd5bf4fe21c6b1906488d81f2c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R474 row · grep -n "^| R474 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 140:| R474 | 10-05 21:42 ET | HIS RULING · APPROVED: tonight he is not woken; every conflict goes to the brain, which resolves it; the desk executes its answer and keeps deploying (L43); only an absolute stop waits for morning. In NOW (TONIGHT line). | HIS RULING · APPROVED |
RULING 2026-10-05 R474 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R474 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 548ee01d911745c95050220e69684ebb94109782
RULING 2026-10-05 R474 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, output whole:
```
clock · date · 0 · Tue Oct  6 06:10:27 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/flake-fix-2-1006
    ?? "docs/40 - DevDocs/reports/flake-fix-2-build-2026-10-06.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 71f69821 docs(desk): brain FIX on the self-migrating tests, drafter prompt 13; R501
diff · git diff --stat 71f69821 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/flake-fix-2-1006 · 0 · 71f69821 docs(desk): brain FIX on the self-migrating tests, drafter prompt 13; R501
env here · ls /Users/cobalt/cobalt-wt/flake-fix-2-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 71f69821` | 0 | `docs(desk): brain FIX on the self-migrating tests, drafter prompt 13; R501` · `docs/40 - DevDocs/prompts/2026-10-06/13-draft-flake-fix-2.md | 11 +++` · `docs/40 - DevDocs/reports/cto-2026-10-06.md | 1 +` · `2 files changed, 12 insertions(+)` |
| callers | `grep -rn -F "connect_migration(" tests/` | 0 | 34 hits. Callers that apply: `test_xl76_membership_harness.py:150`, `test_p4_migrations.py:305`, `radar_migrated_support.py:78`, `test_radar_handicap_store.py:146`, `test_stale_score_db.py:137`, `test_drc_store.py:240`, `test_voice_store.py:166`, `test_tenancy.py:546`, `test_tenancy.py:573`, `test_archiver_migrations.py:447`, `test_radar_score_migration.py:300`. No apply (read a catalog, assert on the call, or text): `test_xl76_membership_harness.py:182` (catalog read, rolled back), `test_xl76_devdb_absence.py:22`, `test_db_credentials.py:156` (captured fake), `test_db_only_selection.py:458` and `:656` (the guard test: `pytest.raises(AssertionError)`), `test_migrate_proof.py` (13 hits), `test_drc_store.py:443` (the open-deadlock test's pass-through), `test_tenancy.py:336`/`:354` (comment and message text), `test_dev_rebuild_db.py:4`/`:43` |
| callers | `grep -rn -F "_migration_conn()" tests/` | 0 | `test_p4_migrations.py:304` def, `:443`, `:485`, `:548`; `test_stale_score_db.py:134` def, `:172`; `test_voice_store.py:165` def, `:187`, `:203`; `test_archiver_migrations.py:446` def, `:454`, `:471`, `:504`; `test_radar_score_migration.py:299` def, `:307`, `:418` |
| callers | `grep -rn -F "_apply(conn, FORWARD)" tests/` | 0 | `test_xl76_membership_harness.py:155`; `test_p4_migrations.py:487`, `:550`; `radar_migrated_support.py:82`; `test_stale_score_db.py:177`, `:179`; `test_drc_store.py:242`; `test_voice_store.py:189`, `:192`, `:205`; `test_tenancy.py:577`; `test_archiver_migrations.py:456`, `:473`, `:474`, `:506`, `:536`, `:550`; `test_radar_score_migration.py:309`, `:310`, `:420` (plus two docstring lines) |
| handicap `_conn` | `grep -n -F "_conn()" tests/cobalt/test_radar_handicap_store.py` | 0 | `145:def _conn():` · `175:    conn = _conn()` |
| sizes | `wc -l` of the ten edited files | 0 | drc_store 664 · radar_migrated_support 95 · radar_score_migration 510 · p4_migrations 609 · voice_store 287 · archiver_migrations 642 · stale_score_db 255 · tenancy 741 · radar_handicap_store 241 · xl76_membership_harness 195 |
| READ | `tail -n 3` flake-fix build report | 0 | `BUILT · job: flake-fix · tip: d1fee872 | on d1adf256 | … | decisions: 1 · for Dejan: 1 · tokens: 175288` |
| READ | `tail -n 3` flake-fix check report | 0 | `CHECK DONE · job: flake-fix · pass: 2 · tip: f520debb · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 135367` |
| READ | `tail -n 3` second-writer survey | 0 | `SURVEY DONE · writer: not found · — · ticks: 6 (4 lock free) · … · deadlocks settled: 4/4 · decisions: 2` |
| RESTARTS empty | `uv run cobalt jobs restarts 71f69821..HEAD` | 0 | only the untracked report row (`DOCS`, `-`) · `RESTARTS: none` |

Card line numbers re-read from the files: all match, with one drift: `test_stale_score_db.py`'s first apply is at `:174` as the card says (`_apply(conn, [p for p in FORWARD if p.name < "0015"])`); the `_apply(conn, FORWARD)` hits at `:177`/`:179` are its later applies and stay.

Card records copied: (1) proved against BASE `71f69821`, every `file:line` read from a clean tree; (2) R326 = row 332 of `cto-2026-10-03.md`, R412 = row 109 and R474 = row 140 of `cto-2026-10-05.md` — re-read by `authorize.sh` above (lines 332, 109, 140, each `HIS RULING` · `APPROVED`); (3) the brain's ruling is desk row R501 in `cto-2026-10-06.md` — a desk record, not re-read (no RULINGS entry).

PROVEN BY FIRST REAL USE: class (a) proven at AUTHORIZATION and here; the pytest strings at E0; git add/commit at E2; the with-DB strings at W's gate take (the card's red is with-DB, but E2 runs it under the lock — see E2).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `71f69821` → `3932 passed, 785 skipped, 2 xfailed, 36 warnings in 600.29s (0:10:00)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.57s`, exit 0. The one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests written (no `src/` edit, no helper yet): `tests/cobalt/test_migration_retry.py` (new; four tests, no DB) and `test_the_migration_step_retries_a_first_deadlock` added at the end of `tests/cobalt/test_radar_score_migration.py` (`@requires_db`).
- Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_migration_retry.py tests/cobalt/test_radar_score_migration.py` → exit 2, `1 error in 0.12s`: `tests/cobalt/test_migration_retry.py:16: in <module> from migration_retry import open_migrated` / `E   ModuleNotFoundError: No module named 'migration_retry'`. The row's red (the import error) for all four, the negative control `test_another_error_is_not_retried` included (it can only go green once the module exists, as the row says).
- With-DB, ONE lock take: `take-devdb-lock.sh flake-fix-2-1006 90` → `lock taken: flake-fix-2-1006` (06:22:53 EDT); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/flake-fix-2-1006/.env`. `<FP>` → **F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`**. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `NOTHING WAS APPLIED` · `SLOTS ok · highest user.aset_sizings 1030 of 1600` · `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `TABLES 0011` — the pair `gate-lists.md` names `## LEVEL 0013` (the prior build's report reads it the same way, `flake-fix-build-2026-10-06.md:75`). No forward.
  - `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_score_migration.py` → `1 failed, 43 passed in 0.88s`: `FAILED tests/cobalt/test_radar_score_migration.py::test_the_migration_step_retries_a_first_deadlock`, `E   psycopg.errors.DeadlockDetected: constructed by flake-fix-2 F1`. `test_card_checks_index_and_receipt_immutability_on_cobalt_dev` itself PASSED.
  - Same file, `--tb=short -k test_the_migration_step_retries_a_first_deadlock` → `1 failed, 43 deselected in 0.07s`, the chain: `:529 test_card_checks_index_and_receipt_immutability_on_cobalt_dev()` → **`:420 in test_card_checks_index_and_receipt_immutability_on_cobalt_dev` `_apply(conn, FORWARD)`** → `:525 in fake raise psycopg.errors.DeadlockDetected(...)`. A call-phase FAILED, not a skip or setup error: the row's stated reason (X4).
  - `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `release-devdb-lock.sh flake-fix-2-1006` → `lock released`; `ls /Users/cobalt/cobalt-wt/flake-fix-2-1006/.env` → `No such file or directory` (06:23:31 EDT).
- Commit `5a9fb3b4 wip(flake-fix-2): red — F1 (open_migrated tests, radar_score_migration retry test)`, 2 files, 135 insertions.

## E3 THE ROWS
F1, built in one commit `fb3117c3 fix(flake-fix-2): one open_migrated helper retries the first migration apply on DeadlockDetected; every self-migrating test calls it (F1, L3 L45)` (13 files, 83 insertions, 101 deletions).
- NEW `tests/cobalt/migration_retry.py`: ONE function `open_migrated(apply, paths)`, the loop of `test_drc_store.py:237-252` at BASE moved unchanged (per attempt `conn = None`; `db.connect_migration(env.DEV_DB_NAME)`, `autocommit = False`, `apply(conn, paths)` in one `try`; on `BaseException` an opened conn gets `rollback()` with `close()` in a `finally`; re-raise unless `DeadlockDetected` on attempt 1 or 2, which prints `migration retry <n>: DeadlockDetected`); returns the open connection.
- Callers (each open + `autocommit = False` + FIRST apply → `conn = open_migrated(_apply, <first paths>)`; later applies untouched). `grep -rn -F "open_migrated(" tests/` at the tip → 17 caller lines: (1) `test_drc_store.py:236` (`migrated`; the `_connect` monkeypatch, yield and final rollback unchanged); (2) `radar_migrated_support.py:79`; (3) `test_radar_score_migration.py:301`, `:411` (`_migration_conn` removed); (4) `test_p4_migrations.py:439` (`base`, computed before the open), `:479`, `:541` (`_migration_conn` removed); (5) `test_voice_store.py:182`, `:197`; (6) `test_archiver_migrations.py:448`, `:464`, `:496`; (7) `test_stale_score_db.py:165` (`[p for p in FORWARD if p.name < "0015"]`; imported inside the test beside its other local imports); (8) `test_tenancy.py:547` (`[FWD_0003]`), `:572` (`FORWARD`); (9) `test_radar_handicap_store.py:169` (`< 14`; `_conn` removed); (10) `test_xl76_membership_harness.py:152` (`started` / `apply_ms` now wrap the `open_migrated` call). Imports no longer used after the removed opens were dropped (`db, env` in radar_score_migration, archiver, handicap store; `env` in p4).
- `grep -rn -F "_migration_conn" tests/` at the tip → one hit, `test_db_only_selection.py:644` (a test NAME, `test_x1_an_unmarked_migration_connection_…`), no helper left. `grep -rn -F "connect_migration(" tests/` at the tip → the non-callers of PREFLIGHT only, plus `migration_retry.py:33` (the helper) and `test_drc_store.py:427` (the open-deadlock test's pass-through). No retry loop is left in any test file (X1).
- `test_tenancy.py::test_connect_migration_has_exactly_one_caller` reads `SRC` only (`grep -n -A4 -F "def _python_files"` → `:312 return sorted(p for p in SRC.rglob("*.py") …)`): not edited, green below.
- DevDocs: `docs/40 - DevDocs/cobalt/drc/store.md` `## 2026-10-06 — flake-fix-2` (the fixture's loop moved), `docs/40 - DevDocs/cobalt/db_migrations/cli.md` `## 2026-10-06 — flake-fix-2` (the helper and its callers).

Greens:
- Offline, the ten edited files + the helper test + the seven `migrated_radar` users: `uv run pytest -q -rs -p no:cacheprovider --color=no <16 files>` → `293 passed, 121 skipped, 1 error in 1.47s`. The 1 error: `ERROR at setup of test_xl76_1_the_with_db_callers` — `fixture 'offline_skip_guard' not found` (`tests/cobalt/conftest.py:262` `dev_db_tx(monkeypatch, request, offline_skip_guard)`, which `tests/experiments/handicap_h1/conftest.py` re-exports without `offline_skip_guard`). Alone: `uv run pytest … tests/experiments/handicap_h1/test_xl76_membership_harness.py` → `2 skipped, 1 error in 0.01s`, the same error. Neither conftest is changed (`git diff --stat 71f69821 -- tests/experiments/handicap_h1/conftest.py tests/cobalt/conftest.py` → nothing) and `test_xl76_1` is not in the diff. Outside the row: DECISION F1-a. No gate suite runs `tests/experiments` (`grep -n -F "experiments" ops/desk/gate-lists.md` → no hit).
- `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_migration_retry.py` → `4 passed in 0.03s`.
- With-DB, ONE more lock take (a `## RECORDS` line): `lock taken: flake-fix-2-1006` (06:26:05 EDT), one `.env` line (this worktree). `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `COBALT_ENV=dev uv run pytest -q -rfEs -p no:cacheprovider --color=no --tb=line <the 15 tests/cobalt files above> --deselect` (the five PASS 1 ids of `gate-lists.md:24` that sit in these files: `test_tenancy.py::TestMigrationRoundTrip`, `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default`, `test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction`, `::test_the_reaper_fails_stale_rows_and_never_retries`, `::test_single_flight_under_two_real_connections`) → **`404 passed, 2 skipped, 6 deselected in 9.80s`**; skips `test_cards_picks.py:388`, `:401`, both in the allowed set (`gate-lists.md:45`). The three `migrated` retry tests and the two at the fixture's open / rollback tests passed in it, and `test_the_migration_step_retries_a_first_deadlock` passed.

THE MUTATIONS (made and undone with Edit, never committed):
- M1, the fix undone (`or attempt == 3` → `or attempt >= 1`: no retry). Offline `tests/cobalt/test_migration_retry.py` → `2 failed, 2 passed in 0.03s`: `FAILED …::test_first_deadlock_retries_once_on_a_fresh_connection` (`E   psycopg.errors.DeadlockDetected: constructed by flake-fix-2 F1`, `:58`), `FAILED …::test_third_deadlock_raises_after_two_retries` (`E   AssertionError: assert 'migration retry 1: DeadlockDetected' in ''`, `:86`). With-DB, same lock take: `COBALT_ENV=dev uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_score_migration.py tests/cobalt/test_drc_store.py -k "retries or migrated_fixture"` → `4 failed, 2 passed, 75 deselected in 0.17s`: `FAILED tests/cobalt/test_radar_score_migration.py::test_the_migration_step_retries_a_first_deadlock` (`E   psycopg.errors.DeadlockDetected: constructed by flake-fix-2 F1`, `:517`), `FAILED …test_drc_store.py::test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks` (`:348`), `…::test_the_migrated_fixture_fails_on_a_third_deadlock_after_two_retries` (`assert 'migration retry 1: DeadlockDetected' in ''`, `:397`), `…::test_the_migrated_fixture_retries_when_opening_the_first_attempt_deadlocks` (`constructed while opening the first migration attempt`, `:424`). Undone → same command `6 passed, 75 deselected in 0.52s`.
- M2, the negative control broken (the condition → `if attempt == 3:`: every error retried) → `1 failed, 3 passed in 0.03s`: `FAILED …::test_another_error_is_not_retried` (`E   Failed: DID NOT RAISE <class 'psycopg.errors.UndefinedTable'>`, `:98`). Undone.
- M3, close moved out of the `finally` (`conn.rollback()` then `conn.close()`) → `1 failed, 3 passed in 0.03s`: `FAILED …::test_failed_attempt_is_closed_when_its_rollback_raises` (`E   assert (1 == 1 and False is True)`, `:113`). Undone.
- After the undos: `git diff --stat` → the ten modified tracked files only (helper untracked then), `uv run pytest … tests/cobalt/test_migration_retry.py` → `4 passed in 0.03s`; the with-DB re-run above green. `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `release-devdb-lock.sh flake-fix-2-1006` → `lock released`; `ls …/.env` → `No such file or directory` (06:26:48 EDT).

## RESTARTS
`uv run cobalt jobs restarts 71f69821..HEAD` (HEAD `fb3117c3`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/reports/flake-fix-2-build-2026-10-06.md	A	DOCS	-
tests/cobalt/migration_retry.py	A	test/documentation; no resident	-
tests/cobalt/radar_migrated_support.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
tests/cobalt/test_migration_retry.py	A	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_store.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_stale_score_db.py	M	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_store.py	M	test/documentation; no resident	-
tests/experiments/handicap_h1/test_xl76_membership_harness.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
`<tip>` = `fb3117c3` (`git log --oneline -1` after the gate). ONE call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh flake-fix-2-1006 all --deploy --tickers PRB` (no `--deselect`: no test of this build needs a level above 0013; `--tickers PRB`: the constructed ticker the new with-DB test writes, through the test it calls, inside its rolled-back transaction; no `--migration`) → exit 0. Verdict lines whole:
```
offline 3936/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (PRB)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4819/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/flake-fix-2-1006-all-20261006-062757.log
```
- (a) offline `3936 passed, 786 skipped, 2 xfailed, 36 warnings in 591.36s (0:09:51)` (log `:861`) → **3936** = E0's 3932 + the 4 new `test_migration_retry.py` tests.
- (b) lock taken (log `:866-867`, waited 0 min); **F0** `664 35 272c95bbb12241e3611e4b36326ccf87` (`:878`); proof-only `TABLES 0011` · `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` (`:926-927`) → `LEVEL 0013` (`:930`).
- (c) PASS 1, whole (deploy) (`:931`), executed command (`:933`) whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py` → `4631 passed, 7 skipped, 82 deselected, 4 xfailed, 43 warnings in 747.23s (0:12:27)` (`:1085`) → **d1 = 4631**. The 7 skips are the 7 SKIPPED lines above; none is marked `OUTSIDE the allowed set`. This build's with-DB tests (`test_the_migration_step_retries_a_first_deadlock` and every edited with-DB test) run in this pass, not deselected.
- (c2) `dev forward: APPLIED 06:50:40` (`:1087`); **F1** `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1162`).
- (c3) PASS 2, executed command (`:1164`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones tests/cobalt/test_drc_d5_db.py tests/cobalt/test_drc_d5_experiments_db.py tests/cobalt/test_f15_p2_replay_db.py` → `188 passed, 1 deselected, 5 warnings in 224.60s (0:03:44)` (`:1771`) → **d2 = 188**; d = 4631 + 188 = **4819** = the gate's `with-DB 4819/0`. No test of this build was deselected from pass 1, so no `PASSED <id>` of this build is owed in pass 2. The edited `test_tenancy.py::TestMigrationRoundTrip` and `test_stale_score_db.py` ran here green.
- (c3r) `stray rows: none (PRB)`.
- (f) **F2** `664 35 272c95bbb12241e3611e4b36326ccf87` (`:1842`) → **`cobalt_dev: 0013 — F2 = F0`** (`:1893`); `release-devdb-lock.sh flake-fix-2-1006` → `lock released` (`:1894-1895`); `.env: removed`; `ls /Users/cobalt/cobalt-wt/flake-fix-2-1006/.env` → `No such file or directory` (06:55:49 EDT).
- (e) live-note `146 passed, 1 skipped, 15 warnings in 25.15s` (`:1964`) → **146**; the skip is `test_replay_line.py:266` `COBALT_TEST_LIVE_DRC`, it does not name `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control." BACKED. `test_the_migration_step_retries_a_first_deadlock`: E2 red on BASE (`DeadlockDetected` via `:420`) and M1 red at the tip (`:517`). `test_first_deadlock_retries_once_on_a_fresh_connection` and `test_third_deadlock_raises_after_two_retries`: E2 import-error red, then M1 red (`:58`, `:86`). `test_another_error_is_not_retried`: E2 import-error red, then M2 red (`DID NOT RAISE … UndefinedTable`, `:98`). `test_failed_attempt_is_closed_when_its_rollback_raises`: E2 import-error red, then M3 red (`assert (1 == 1 and False is True)`, `:113`). The fixture's three retry tests and its open-deadlock test, all now running through the helper, are red under M1 (`:348`, `:397`, `:424`). The two that stayed green under M1 (`does_not_retry_another_error`, `closes_a_failed_attempt_when_rollback_fails`) are covered by M2 and M3 through the helper's own tests. No test stayed green under its own mutation, so none was rewritten.
(2) "Every entry path of each rule pinned by a test." PARTLY. The helper's own paths are each pinned: first deadlock, third deadlock, another error, rollback raises (the four helper tests), plus a deadlock while opening (`test_drc_store.py::test_the_migrated_fixture_retries_when_opening_the_first_attempt_deadlocks`, red under M1). Of the 17 call sites PREFLIGHT found, `test_drc_store.py:236` and `test_radar_score_migration.py:411` have a retry test of their own. The other 15 ran green on `cobalt_dev` in pass 1 or pass 2 of the gate, except `test_xl76_membership_harness.py:152` (F1-a). No test fails if one of those 15 goes back to an inline open. The card names no such test, so this gap is DECISION F1-b and the self-check is 2 of 3.
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." BACKED. Re-run at the tip: `git show --stat fb3117c3` (13 files, 83+/101-), `grep -rn -F "open_migrated(" tests/cobalt tests/experiments` (17 call lines plus the 4 helper-test calls and the `def` at `migration_retry.py:25`, line numbers as quoted in E3), `git diff --name-only --no-renames 71f69821` (14 paths: 2 docs, 12 `tests/`), and the gate log greps for `F0: `, `F1: `, `F2`, `dev forward: APPLIED`, `pass 1: whole (deploy)`, ` passed` and `$ COBALT_ENV=dev uv run pytest`.

## FOR THE CHECK
- Range `71f69821..fb3117c3`: `5a9fb3b4 wip(flake-fix-2): red — F1 (open_migrated tests, radar_score_migration retry test)`, `fb3117c3 fix(flake-fix-2): one open_migrated helper retries the first migration apply on DeadlockDetected; every self-migrating test calls it (F1, L3 L45)`. The report commit follows on top; it is not the tip.
- F1 reds, mutations and greens: `## E2 RED` and `## E3 THE ROWS` above (quoted). Caller greps: `## PREFLIGHT` (at BASE) and `## E3` (at the tip).
- X1: the diff is `tests/` plus two DevDocs files (`git diff --name-only --no-renames 71f69821`, 14 paths). The loop is written once, in `migration_retry.py:30-45`, and `test_drc_store.py`'s copy is gone (`git show --stat`: `test_drc_store.py | 22 ++---`).
- X2: the helper's four tests and M1–M3.
- X3: all 17 call sites in the card's list call the helper. No other BASE hit applies migrations on its own connection: `test_xl76_membership_harness.py:181/182` is the catalog read; `test_db_only_selection.py:656` is the guard test; `test_db_credentials.py:156` asserts on a fake. None of them is in the card's non-caller list, and each was read and left as it was.
- X4: the E2 `--tb=short` chain above.
- RUN rows: none on this card.
- Suites: `## W` (executed pass 1 and pass 2 commands copied whole). Fingerprints: E2 take F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, F-after equal; E3 take F0 equal, F-after equal; gate F0 `664 35 272c95bbb12241e3611e4b36326ccf87` / F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` / F2 = F0. Lock times: E2 06:22:53 taken → 06:23:31 released; E3 06:26:05 → 06:26:48; gate taken at `:866` (waited 0 min), released at `:1894-1895`. Every release was followed by a check that `.env` is gone.
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: `## PREFLIGHT` last paragraph.

## CONTINUE
next: none — CLOSE done; the desk verifies and launches the check (L67).

## DECISIONS
- **DECISION F1-a: the XL76 harness test file cannot run, and no suite runs it. UNPROVEN on BASE by a run (L70); outside the row.** `uv run pytest … tests/experiments/handicap_h1/test_xl76_membership_harness.py` → `2 skipped, 1 error`: `ERROR at setup of test_xl76_1_the_with_db_callers — fixture 'offline_skip_guard' not found` (`tests/cobalt/conftest.py:262`, `dev_db_tx(monkeypatch, request, offline_skip_guard)`; `tests/experiments/handicap_h1/conftest.py` re-exports `dev_db_tx` without it). Neither conftest is in the diff, and `test_xl76_1` was not edited. With `.env`, `test_xl76_2_3_harness_shape_at_step_1` (caller (10), edited here) would hit the same setup error. That makes caller (10)'s edit proven by reading only, never by a run. No gate suite names `tests/experiments` (`gate-lists.md` grep → no hit). Default taken: not fixed here (the card's fence lists `## NOT IN THIS JOB`: "A red outside this row"). Its own card if the desk wants `tests/experiments/handicap_h1` runnable.
- **DECISION F1-b: 15 of the 17 call sites have no test that pins them to the helper.** Only `test_drc_store.py` `migrated` and `test_radar_score_migration.py:411` have a retry test. A later edit that goes back to an inline open in any other caller would pass every suite. The card names one with-DB red only. Default taken: no extra test (THE ROWS: build only the card's rows). If the desk wants it, the cheap pin is an offline lint in `test_migration_retry.py` that fails if any `tests/` file other than `migration_retry.py` calls `connect_migration(` and `_apply(` on the same connection. `self-check: 2 of 3` follows from this item.

## RECORDS
- L74: one system reminder asked for a `Claude-Session:` commit line. It is recorded under `## L74` and was not acted on.
- Extra lock take: E3, 06:26:05–06:26:48 EDT. It ran the edited with-DB files green and the M1 with-DB mutation before the gate, so a red would cost no gate rerun. F before = F after = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `.env: removed, proven gone (E3)`. Also `.env: removed, proven gone (E2)` and `(W)`.
- Card records re-read at PREFLIGHT: R326 / R412 / R474 at rows 332 / 109 / 140 (`authorize.sh`). R501 is a desk record and was not re-read.
- `test_xl76_membership_harness.py`: `apply_ms` now also times the connection open and any retry. Before, an apply failure inside its `try` printed `harness_applies=False`. Now that failure raises from `open_migrated`, before the `try`, so the line is not printed. The test fails either way.
- No `REFUSED, not needed` line; no `CONTINUED` line.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: flake-fix-2 · tip: fb3117c3 | on 71f69821 | migration: none | offline 3936/0 | with-DB 4819/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 2 of 3 | decisions: 2 · for Dejan: 0 · tokens: 230163
