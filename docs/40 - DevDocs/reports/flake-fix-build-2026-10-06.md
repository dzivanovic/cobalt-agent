# flake-fix — build report 2026-10-06

## §0 Headline
- F1 is built at `d1fee872`. `migrated` in `tests/cobalt/test_drc_store.py` now retries its migration step on `DeadlockDetected`: at most twice, each time on a fresh connection, after rolling back and closing the failed one. It prints `migration retry <n>: DeadlockDetected` on each retry. No `src/` change.
- Three with-DB tests pin it: the two reds on BASE behaviour and the negative control green. Four mutations each turned a test red.
- Gate call 2 is green: offline 3932/0, with-DB 884/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`.
- Gate call 1 went red on the same autovacuum deadlock in `test_radar_score_migration.py:420`, a self-migrating test the card fences out. That is `DECISION W`, FOR DEJAN: does it get a card of its own?

## L74
The session's attribution reminder (a system message, not a tool result) asked for a `Claude-Session:` line in commits. BUILD-HUB L74 rules commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, and the reminder defers to the user's rules, so the build acted on none of it.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md"` (00:50 EDT), output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md" · 0 · 356b4646ecfbcf6e12cb937ceb1458c39dc1f30d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/02-flake-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
Each row: rule · command · exit · output verbatim.

- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 · output whole:
```
clock · date · 0 · Tue Oct  6 00:50:37 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/flake-fix-1006
    ?? "docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · d1adf256 docs(desk): R483 R327 met by P2 smoke; flake-fix drafter prompt
diff · git diff --stat d1adf256 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/flake-fix-1006 · 0 · d1adf256 docs(desk): R483 R327 met by P2 smoke; flake-fix drafter prompt
env here · ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- BASE · `git show --stat d1adf256` · 0 · `d1adf256 docs(desk): R483 R327 met by P2 smoke; flake-fix drafter prompt` — `docs/40 - DevDocs/prompts/2026-10-06/01-draft-flake-fix.md | 11 +++`, `docs/40 - DevDocs/reports/cto-2026-10-06.md | 2 ++`, `2 files changed, 13 insertions(+)`
- SYMBOL · `grep -n -F "def migrated(" tests/cobalt/test_drc_store.py` · 0 · `232:def migrated(monkeypatch):`
- SYMBOL · `grep -n -F "_apply(conn, FORWARD)" tests/cobalt/test_drc_store.py` · 0 · `237:        _apply(conn, FORWARD)`
- SYMBOL · `grep -n -F "requires_db = " tests/cobalt/test_drc_store.py` · 0 · `48:requires_db = pytest.mark.skipif(`
- SYMBOL · `grep -n -F "def connect_migration(" src/cobalt/db.py` · 0 · `269:def connect_migration(dbname: str, *, allow_prod: bool = False) -> psycopg.Connection:`
- SYMBOL · `grep -n -F "def _apply(" src/cobalt/db_migrations/cli.py` · 0 · `631:def _apply(conn, paths) -> None:`
- SYMBOL · `grep -n -F "def test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current" tests/cobalt/test_drc_k2_experiments.py` · 0 · `332:def test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current(migrated):`; the import of `migrated` is at `test_drc_k2_experiments.py:49` (Read, lines 43-51).
- CALLERS · `grep -rn -F "from test_drc_store import" tests` · 0 · 26 hits. The files that import the `migrated` fixture by name, multi-line or inline: `test_drc_d2_fix_r2_db.py:41`, `test_drc_d5_db.py:37`, `test_drc_imports_db.py:28`, `test_drc_k2_fix_r1_runs.py:19`, `test_drc_d2_fix_r1_runs.py:35`, `test_drc_k2_fix_r2_store.py:36`, `test_drc_d2_fix_r1_db.py:36`, `test_drc_k2_store.py:49`, `test_drc_d3_fix_r1_db.py:34`, `test_drc_k2_fix_r2_runs.py:28`, `test_drc_d5_experiments_db.py:27` (`D, STATS, migrated, requires_db, weekday_calendar`), `test_drc_k3_db.py:23`, `test_drc_d3_experiments.py:23` (`D, migrated, requires_db`), `test_drc_d2_experiments.py:40`, `test_drc_k2_experiments.py:43`, `test_drc_k1_store.py:34`, `test_drc_k1_experiments.py:41`, `test_drc_k2_fix_r1_store.py:54`, `test_drc_build_db.py:35`. The others import only constants or `weekday_calendar`.
- CALLERS · `grep -rn -F "import migrated" tests` · 0 · only `radar_migrated_support.migrated_radar` and `world_support.migrated_world`: different fixtures, outside this row (card `## NOT IN THIS JOB`).
- WC · `wc -l tests/cobalt/test_drc_store.py` · 0 · `513 tests/cobalt/test_drc_store.py`
- READ tail · `tail -n 3 "docs/40 - DevDocs/reports/second-writer-survey-2026-10-05.md"` · 0 · last line: `SURVEY DONE · writer: not found · — · ticks: 6 (4 lock free) · sightings: 0 · redactions: mattermost by gate pytest runs (inferred) · deadlocks settled: 4/4 · decisions: 2`
- READ tail · `tail -n 3 "docs/40 - DevDocs/reports/deploy-deploy-k3-1005-attempt2.md"` · 0 · last line: `FAILED: gate — G (c) — test_x9 in test_drc_k2_experiments.py, setup ERROR DeadlockDetected, the known flake in an untouched test (migrated fixture; hub stop line above) · rollback: not used · decisions: 3 · for Dejan: 0`
- RESTARTS · `uv run cobalt jobs restarts d1adf256..HEAD` · 0 · `docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md	A	DOCS	-` / `RESTARTS: none`. The range holds no commit; the tool lists the untracked report only.
- CARD RECORDS (copied): (1) "Proved against BASE `d1adf256` … every `file:line` above read from the working tree"; re-read: every `file:line` in the card matched the greps above (232/237/48/269/631/49/332; `migrated` spans 231-249 in the Read). (2) "R326 is row 332 of `reports/cto-2026-10-03.md`; R412 is row 109 of `reports/cto-2026-10-05.md`"; re-read by `authorize.sh`: `332:| R326 |` and `109:| R412 |`, both committed.
- DB: the card carries no "DB: none" key. Per THE LOCK, PREFLIGHT takes no lock. The with-DB strings are proven at E2's take.

## E0 BASELINE
- Offline, on `d1adf256`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `3932 passed, 780 skipped, 2 xfailed, 36 warnings in 614.54s (0:10:14)`. 0 failed, 0 errors. The skips are the offline `requires_db` and live-vault skips (last one quoted: `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`).
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.65s`. The one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Three tests added to `tests/cobalt/test_drc_store.py`, all `@requires_db`, with no `src/` edit. Each uses a helper fixture (`deadlock_first`, `deadlock_always`, `undefined_table_first`) that patches this module's `_apply` through `monkeypatch.setitem(globals(), "_apply", …)`. The fake raises the named error on its first N calls and runs the real `_apply` after that. The test then gets the fixture with `request.getfixturevalue("migrated")`. Beyond the card's asserts, the tests also pin X2: they count the connections the fake was handed and assert that the failed ones are `.closed` and distinct.

- Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_drc_store.py` → `17 passed, 18 skipped in 0.09s` (the three new tests skip offline: `Postgres env settings not available`).
- With-DB, ONE lock take (THE LOCK (a)–(b)): `take-devdb-lock.sh flake-fix-1006 90` → `lock taken: flake-fix-1006` (01:03:33 EDT); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/flake-fix-1006/.env`.
  - `<FP>` (typed as in BUILD-HUB THE LOCK) → `F0` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
  - `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → last lines `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` / `TABLES 0011`; `SLOTS ok · highest user.aset_sizings 922 of 1600`; `NOTHING WAS APPLIED`. Together these equal `gate-lists.md:47-48` `## LEVEL 0013` = `TABLES 0011 · FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, so the level is 0013. No forward was run.
  - `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_drc_store.py` → `2 failed, 33 passed in 1.45s`:
    - `FAILED …::test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks`: `E   psycopg.errors.DeadlockDetected: constructed by flake-fix F1` at `test_drc_store.py:348` (the fake's `raise fail_with(…)`, reached through `request.getfixturevalue("migrated")`). It FAILED in the call phase: no setup error, no skip. This is the row's red: the fixture has no retry.
    - `FAILED …::test_the_migrated_fixture_fails_on_a_third_deadlock_after_two_retries`: `E   AssertionError: assert 'migration retry 1: DeadlockDetected' in ''` at `:397`. This is the row's red: the print lines are missing.
    - `PASSED …::test_the_migrated_fixture_does_not_retry_another_error`: the negative control is green on BASE, as the card asks.
  - `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0.
  - The lock's (d): `release-devdb-lock.sh flake-fix-1006` → `lock released`; `ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env` → `No such file or directory` (01:04:30 EDT).
- Commit `ac55ec16 wip(flake-fix): red — migrated fixture retry tests (F1)`.

## E3 THE ROWS
**F1** (re-read `test_drc_store.py:231-249` before the edit; the fixture matched the card). The edit: the open, `autocommit = False` and `_apply(conn, FORWARD)` now sit in a `for attempt in range(1, 4)` loop. On `psycopg.errors.DeadlockDetected` the loop calls `conn.rollback()`, then `conn.close()`, then re-raises if `attempt == 3`, else prints `migration retry {attempt}: DeadlockDetected` and goes round. On any other exception (`except BaseException`) it calls `conn.rollback()` and `conn.close()` and raises. That keeps today's behaviour, where the outer `finally` rolled back and closed. `counter`, `_connect`, the monkeypatch, `yield conn` and the final `rollback()` / `close()` are unchanged. The diff is in `## FOR THE CHECK`.

- Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_drc_store.py tests/cobalt/test_drc_k2_experiments.py` → `19 passed, 31 skipped in 0.11s`.
- With-DB, a SECOND lock take (a `## RECORDS` line): `lock taken: flake-fix-1006` (01:05:07 EDT); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's. `<FP>` → F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`.
  - Green: `COBALT_ENV=dev uv run pytest -q -rA --show-capture=no -p no:cacheprovider --color=no --tb=line tests/cobalt/test_drc_store.py tests/cobalt/test_drc_k2_experiments.py` → `50 passed in 2.43s`, including `PASSED …::test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks`, `PASSED …::test_the_migrated_fixture_fails_on_a_third_deadlock_after_two_retries`, `PASSED …::test_the_migrated_fixture_does_not_retry_another_error` and `PASSED tests/cobalt/test_drc_k2_experiments.py::test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current`.
  - THE MUTATIONS, each made with Edit, run alone as `COBALT_ENV=dev uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=line tests/cobalt/test_drc_store.py -k migrated_fixture`, then undone with Edit:
    - M1, undo the fix (`if attempt == 3:` → `if attempt >= 1:`, so no retry) → `2 failed, 1 passed, 32 deselected`; first failing line `E   psycopg.errors.DeadlockDetected: constructed by flake-fix F1` (`:363`); second `E   AssertionError: assert 'migration retry 1: DeadlockDetected' in ''` (`:412`).
    - M2, the third deadlock swallowed (`if attempt == 3:` → `if attempt == 4:`) → `1 failed, 2 passed, 32 deselected, 1 error`; `E   Failed: DID NOT RAISE <class 'psycopg.errors.DeadlockDetected'>` (`:409`), with captured `migration retry 3: DeadlockDetected`. The teardown error is `psycopg.OperationalError: the connection is closed`, a consequence of the mutation.
    - M3, the failed connection not closed (deadlock branch's `conn.close()` removed) → `2 failed, 1 passed, 32 deselected`; `E   assert (False)` / `+  where False = <psycopg.Connection [IDLE] (host=localhost user=cobalt database=cobalt_dev) …>.closed` (`:401`); `E   assert False` / `all(…)` (`:416`).
    - M4, the negative control broken (`except psycopg.errors.DeadlockDetected:` → `except psycopg.Error:`) → `1 failed, 2 passed, 32 deselected`; `E   Failed: DID NOT RAISE <class 'psycopg.errors.UndefinedTable'>` (`:422`), with captured `migration retry 1: DeadlockDetected`.
    - Undone: `git diff` showed only the fix against `ac55ec16`. One cosmetic Edit after that removed a blank line after `try:`. Then the green re-ran: `COBALT_ENV=dev uv run pytest -q -rfE … tests/cobalt/test_drc_store.py tests/cobalt/test_drc_k2_experiments.py` → `50 passed in 2.43s`.
  - `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = F0. `release-devdb-lock.sh flake-fix-1006` → `lock released`; `ls …/.env` → `No such file or directory` (01:06:32 EDT).
- No test stayed green under its mutation; none was rewritten.
- DevDocs: `docs/40 - DevDocs/cobalt/drc/store.md` gets `## 2026-10-06 — flake-fix`, one line, placed before `## Tests`.
- Commit `d1fee872 fix(flake-fix): migrated fixture retries the migration step on DeadlockDetected (F1, L1 L45 L76)`.

## RESTARTS
`uv run cobalt jobs restarts d1adf256..HEAD` (HEAD = `d1fee872`), table whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md	A	DOCS	-
tests/cobalt/test_drc_store.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
`<tip>` = `d1fee872`. This build adds no with-DB test needing a level above 0013 (all three run inside `migrated`'s rolled-back transaction), so it has no `--deselect`, no `--migration`, and no `ops/desk/gate-lists.md` edit. It writes no ticker, so it has no `--tickers`.

**Gate call 1** — `sh /Users/cobalt/cobalt/ops/desk/gate.sh flake-fix-1006 all` → exit 1, verdict lines whole:
```
offline 3932/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
RED (exit 1): 1 failed, 695 passed, 7 skipped, 4012 deselected, 2 xfailed, 12 warnings in 119.76s (0:01:59)
…
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/flake-fix-1006-all-20261006-010703.log
```
The one failure was outside this row (`DECISION W`). In that log, `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:875`), there is no `dev forward` line (no forward ran), and `lock released` is at `:1081`. `ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env` → `No such file or directory`.

**Gate call 2** (one more call on the same tip, `## RECORDS`) — `sh /Users/cobalt/cobalt/ops/desk/gate.sh flake-fix-1006 all` → exit 0, verdict lines whole:
```
offline 3932/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 884/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/flake-fix-1006-all-20261006-012006.log
```
- (a) offline → `3932 passed, 783 skipped, 2 xfailed, 36 warnings in 596.02s` (`:858`) → `<p>` = 3932. Added by this build: the three `test_the_migrated_fixture_*` tests. They skip offline, so they are in the skip count, not `<p>`.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:875`); `LEVEL 0013`.
- (c) PASS 1, executed command (`grep -n -F "tests/cobalt tests/taxonomy --db-only" <log>`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py` (gate call 1 log `:929`; the same PASS 1 line of `gate-lists.md:24`) → `696 passed, 7 skipped, 4012 deselected, 2 xfailed, 12 warnings in 123.62s` (`:998`) → `<d1>` = 696. The 7 SKIPPED lines are quoted in the verdict above. None is marked `OUTSIDE the allowed set`, and none is a test of this build. PASS 1 prints `-rs` only, so the three new tests have no `PASSED` line (`grep -n -F "PASSED tests/cobalt/test_drc_store.py::test_the_migrated_fixture" <log>` → nothing). They ran here with 0 failed.
- (c2) `dev forward: APPLIED 01:32:23` (`:1000`); `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1075`).
- (c3) PASS 2 (the `gate-lists.md:30` command; this build deselected nothing from pass 1) → `188 passed, 1 deselected, 5 warnings in 226.32s` (`:1684`) → `<d2>` = 188. This build has no PASS 2 id. `<d>` = 696 + 188 = 884 = `with-DB 884/0`.
- (c3r) `stray rows: not read (no --tickers given)`: this build writes no ticker.
- (e) live-note → `146 passed, 1 skipped, 15 warnings in 25.42s` (`:1871`) → `<l>` = 146. The skip is `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1749`) = F0 → **`cobalt_dev: 0013 — F2 = F0`**; `lock released` (`:1802`); `.env: removed`; `ls /Users/cobalt/cobalt-wt/flake-fix-1006/.env` → `No such file or directory`.
- Extra, read only: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1382 passed, 1 xfailed, 15 warnings in 358.93s`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown RED for its named reason. E2, on BASE behaviour: `…retries_once…` → `psycopg.errors.DeadlockDetected: constructed by flake-fix F1` out of `getfixturevalue` (FAILED in the call phase); `…fails_on_a_third_deadlock…` → `assert 'migration retry 1: DeadlockDetected' in ''`. The negative control `…does_not_retry_another_error` is green on BASE and red under M4 (`DID NOT RAISE <class 'psycopg.errors.UndefinedTable'>`). In E3, M1 turned both row tests red and M2 / M3 each turned the pinned clause red (quoted in `## E3`). No test stayed green, and none was rewritten.
(2) Every entry path was pinned. The fixture has one body. Its callers are the 19 files PREFLIGHT's `grep -rn -F "from test_drc_store import" tests` lists as importing `migrated`, and they all reach the same body. The three branches are pinned: deadlock then success (`…retries_once…`), deadlock ×3 (`…third_deadlock…`), another error (`…does_not_retry_another_error…`). The plain success path is pinned by every existing `migrated` test (`50 passed` in E3, including `test_x9_gate_…`, and gate PASS 1 `696 passed`). The tests also pin connection hygiene (X2): failed connections are `.closed` and distinct, and the live one is not closed.
(3) Every `file:line`, count and quote was re-read at the tip. Calls re-run after `d1fee872`: `grep -n -F "def migrated(" tests/cobalt/test_drc_store.py` → `232`; `grep -n -F "raise fail_with(" …` → `362` (it was `348` at `ac55ec16`, the E2 line); `grep -n -F "migration retry 1: DeadlockDetected" …` → `395`, `411`; `wc -l` → `607`; `grep -n -F "_apply(conn, FORWARD)" tests/cobalt/test_radar_score_migration.py` → `309`, `310`, `420`; `git diff d1adf256 -- tests/cobalt/test_drc_store.py` (in `## FOR THE CHECK`); `git diff --name-only --no-renames d1adf256` → `docs/40 - DevDocs/cobalt/drc/store.md`, `tests/cobalt/test_drc_store.py`. The E3 mutation line numbers (`:363`, `:409`, `:412`, `:401`, `:416`, `:422`) are from the mutated tree. That tree still held the blank line after `try:`, so each number is one more than at the tip.

## FOR THE CHECK
- Range `d1adf256..d1fee872`: `ac55ec16 wip(flake-fix): red — migrated fixture retry tests (F1)`; `d1fee872 fix(flake-fix): migrated fixture retries the migration step on DeadlockDetected (F1, L1 L45 L76)`. The report commit comes after.
- Paths: `tests/cobalt/test_drc_store.py` and `docs/40 - DevDocs/cobalt/drc/store.md` (X1: the test file holds only the `migrated` fixture and the new helper, fixtures and tests).
- The fixture diff at the tip:
```
 def migrated(monkeypatch):
-    conn = db.connect_migration(env.DEV_DB_NAME)
-    conn.autocommit = False
+    # flake-fix F1: an autovacuum worker can deadlock the migration step;
+    # the whole step is retried at most twice, each on a fresh connection.
+    for attempt in range(1, 4):
+        conn = db.connect_migration(env.DEV_DB_NAME)
+        conn.autocommit = False
+        try:
+            _apply(conn, FORWARD)
+            break
+        except psycopg.errors.DeadlockDetected:
+            conn.rollback()
+            conn.close()
+            if attempt == 3:
+                raise
+            print(f"migration retry {attempt}: DeadlockDetected")
+        except BaseException:
+            conn.rollback()
+            conn.close()
+            raise
     counter = iter(range(10_000))
     try:
-        _apply(conn, FORWARD)
-
         def _connect(dbname, *, side, allow_prod=False):
```
  The new tests sit at `test_drc_store.py:347-424` (helper `_patch_apply`, fixtures `deadlock_first` / `deadlock_always` / `undefined_table_first`, the three tests).
- F1: the reds, mutations and greens are as quoted in `## E2 RED` and `## E3 THE ROWS`. The card has no RUN row.
- Caller greps: as in `## PREFLIGHT` (`from test_drc_store import`, 26 hits, 19 of them import `migrated`).
- Suites: offline 3932/0; with-DB 884/0 (696 + 188); live-note 146/0. The commands and log lines are under `## W`.
- Fingerprints per lock take:
  - E2 take (01:03:33 – 01:04:30 EDT): F0 = `664 35 272c95bb…` before and after.
  - E3 take (01:05:07 – 01:06:32 EDT): F0 = `664 35 272c95bb…` before and after.
  - Gate 1 (log `…-010703.log`): F0 `:875`, no forward, `lock released` `:1081`.
  - Gate 2 (log `…-012006.log`): F0 `664 35 272c95bbb12241e3611e4b36326ccf87` `:875`, F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` `:1075`, F2 `664 35 272c95bbb12241e3611e4b36326ccf87` `:1749`, `lock released` `:1802`.
- RESTARTS table as under `## RESTARTS` → `RESTARTS: none`.
- Records copied at PREFLIGHT: the card's two records, re-read (`## PREFLIGHT`).
- Check asks: X1, the diff paths above. X2, the fixture's deadlock branch rolls back and closes before the next `connect_migration`, pinned by the `.closed` asserts and M3. X3, the third deadlock is raised (M2) and the other-error path is raised at once (control, M4). X4, the E2 red was `FAILED` in the call phase with `DeadlockDetected` raised through `getfixturevalue`: no setup ERROR, no skip.

## CONTINUE
next: none (BUILT; the desk launches CHECK-HUB)

## DECISIONS
- **DECISION W (FOR DEJAN — scope: a follow-up card).** The first gate call (`log: /Users/cobalt/cobalt-wt/.gate-logs/flake-fix-1006-all-20261006-010703.log`) went red in PASS 1 at 0013 on ONE test outside this row: `1 failed, 695 passed, 7 skipped, 4012 deselected, 2 xfailed, 12 warnings in 119.76s`. The test was `test_card_checks_index_and_receipt_immutability_on_cobalt_dev` at `tests/cobalt/test_radar_score_migration.py:420` (`_apply(conn, FORWARD)`, on its own `_migration_conn()`, not the `migrated` fixture). The error, quoted from log lines 988-992: `psycopg.errors.DeadlockDetected: deadlock detected` / `DETAIL:  Process 2062153 waits for AccessExclusiveLock on relation 165614 of database 165601; blocked by process 2062083.` / `Process 2062083 waits for ShareLock on transaction 4039059; blocked by process 2062153.` / `CONTEXT:  SQL statement "ALTER TABLE system.bars OWNER TO cobalt_system"`. This is the same statement as the survey's K3-1 row. The blocker's identity was not read (no server-log read in this seat), so it is UNPROVEN (L70). The card fences this file out: `## NOT IN THIS JOB` says "the other tests that open `db.connect_migration` and run `_apply(conn, FORWARD)` themselves … a card of their own if one deadlocks". It was not fixed here. Safe default taken: the gate ran once more on the same tip (`## RECORDS`). The open question for Dejan: should `test_radar_score_migration.py` and the other self-migrating tests get the same retry on a card of their own?

## RECORDS
- Extra lock take: E3 took the lock a second time (01:05:07 – 01:06:32 EDT) for the with-DB green and the four mutations. E2's take (01:03:33 – 01:04:30 EDT) had already been released before the `src`-free fix was written. `.env: removed, proven gone (E2)`; `.env: removed, proven gone (E3)`; `.env: removed, proven gone (W, gate 1 and gate 2)`.
- One more gate call: gate call 2 on the same tip `d1fee872`, after gate call 1 went red on `test_radar_score_migration.py:420` (`DECISION W`). No code changed between the two calls.
- At E0 the report Edit (PREFLIGHT section) was sent in the same tool batch as the background offline run's launch, so a doc file was written as that run started. No test reads the report.
- L74: the session's attribution reminder asked for a `Claude-Session:` line. It was not acted on (`## L74`).
- Card records as re-read at PREFLIGHT: R326 = `cto-2026-10-03.md:332`, R412 = `cto-2026-10-05.md:109`, both committed (authorize.sh). The `file:line`s match BASE.
- No `REFUSED, not needed` line; no `CONTINUED` line.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: flake-fix · tip: d1fee872 | on d1adf256 | migration: none | offline 3932/0 | with-DB 884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 1 · tokens: 175288
