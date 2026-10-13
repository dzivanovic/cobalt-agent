# backup-flock-1012 — build report (card 441)

## §0 Headline
- F1 built: `snapshot()` holds `STAGING/.backup.lock` (wait `LOCK_WAIT_S = 1800`, then `BackupError`) and its `finally` removes only its own dump. R3 run: `RESTARTS: com.cobalt.radar`.
- Tip `964b6105`; gate green: offline 4316/0 · with-DB 5219/0 · live-note 146/0; `cobalt_dev: 0013 — F2 = F0`; `.env` removed.
- Seven tests (`TestStagingLock` T1–T7), each red for its reason at E2 or under a mutation.

## L74
- A system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded here; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md"`, exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md" · 0 · 514c84bf3018baa65d832c9c05c4b633c8593f77
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 165:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, exit 0:
```
clock · date · 0 · Mon Oct 12 22:03:50 EDT 2026
status · git status --short --branch · 0 · ## ops/backup-flock-1012
head · git log --oneline -1 · 0 · 86dc425a docs(desk): R1297-R1298 preflight of card 441, brain T1 row text pasted
diff · git diff --stat 86dc425a · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/backup-flock-1012 · 0 · 86dc425a docs(desk): R1297-R1298 preflight of card 441, brain T1 row text pasted
env here · ls /Users/cobalt/cobalt-wt/backup-flock-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 86dc425a` | 0 | `docs(desk): R1297-R1298 preflight of card 441, brain T1 row text pasted`; 3 files (card, `backup-flock-preflight-2026-10-12.md`, `cto-2026-10-12.md`), 47 insertions, 3 deletions |
| symbol STAGING | `grep -n -F "STAGING" src/cobalt/backup/restic.py` | 0 | `15:`, `48:STAGING = Path.home() / "cobalt-backups" / "staging"`, `180:    STAGING.mkdir(parents=True, exist_ok=True)`, `184:            dump = dump_database(cfg.database.name, STAGING)`, `196:        for leftover in STAGING.glob("*.sql"):` |
| callers of snapshot() | `grep -rn -F "snapshot(" src` | 0 | the one caller of `restic.snapshot`: `src/cobalt/backup/cli.py:49:        result = snapshot(dry_run=args.dry_run)`; definition `src/cobalt/backup/restic.py:162`; every other hit is a different function (`settings/card.py:212`, `seatusage/report.py:324`, `_snapshot`/`_resolve_snapshot`/`pool_snapshot`/`score_snapshot`/`_card_snapshot`/`_parse_snapshot`/`previous_snapshot`) |
| callers of dump_database() | `grep -rn -F "dump_database(" src` | 0 | `restic.py:155` (def), `restic.py:184` (the one call) |
| pgdump write | `grep -n -F "out.open(" src/cobalt/backup/pgdump.py` | 0 | `99:    with out.open("wb") as fh:` |
| precedent constant | `grep -n -F "BACKUP_MAX_AGE_S" src/cobalt/db_apply.py` | 0 | `58:BACKUP_MAX_AGE_S = 900` (plus `:17`, `:227`, `:229`, `:231`, `:322`) |
| precedent pin | `grep -n -F "BACKUP_MAX_AGE_S" tests/cobalt/test_db_apply.py` | 0 | `390:    assert db_apply.BACKUP_MAX_AGE_S == 900` |
| house flock | `grep -n -F "class DirectoryLock" src/cobalt/voice/scratch.py` | 0 | `193:class DirectoryLock:` (`os.open … 0o600` `:200`, `os.chmod` `:210`, pid write `:211-212`, Read tool) |
| line counts | `wc -l src/cobalt/backup/restic.py tests/cobalt/test_backup.py` | 0 | `295 src/cobalt/backup/restic.py` · `226 tests/cobalt/test_backup.py` |
| READ tail | `tail -n 3 ".../reports/cto-2026-10-12.md"` | 0 | last line `HANDOVER: predecessor fd1710af → successor 745a6747 at 21:45 · pane w2:pV1` |
| READ tail | `tail -n 3 ".../reports/deploy-recut-archive-1012.md"` | 0 | last line `DEPLOYED deploy-2026-10-12-recut-archive 4bf3e614 \| set: none \| migrations: none \| gate: offline 4309/0 · with-DB 5212/0 · live-note 146/0 \| RESTARTS: none \| smoke: GREEN \| decisions: 4 · for Dejan: 0 · tokens: 177654` |
| R1289 | `grep -n -F "\| R1289 " ".../cto-2026-10-12.md"` | 0 | `17:\| R1289 \| 21:43 ET \| DESK RECORD brain L79, 434 D2.4: cause = \`backup run\` raced the nightly (shared \`STAGING/cobalt_brain.sql\`, \`finally\` globs \`*.sql\`); …` |
| restarts | `uv run cobalt jobs restarts 86dc425a..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` (empty range) |

The card's records, re-read: `restic.py` 295 lines and `test_backup.py` 226 (wc above); the dump write `restic.py:184` → `:159` → `pgdump.py:99`; the glob `restic.py:196`; the one caller `backup/cli.py:49`; `BACKUP_MAX_AGE_S = 900` at `db_apply.py:58` pinned at `test_db_apply.py:390`; house shape `scratch.py:200`, `:210-212` (the card cites `:211` for chmod; the file holds `os.chmod` at `:210`, `os.ftruncate` `:211`, `os.pwrite` `:212`).

DB: the card carries no `DB: none` key; W runs the gate with the lock.

`<FP>` (copied whole before the first run): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`, exit 0: `4309 passed, 806 skipped, 1 xfailed, 36 warnings in 661.87s (0:11:01)`.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`, exit 0: `146 passed, 1 skipped, 15 warnings in 28.93s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`class TestStagingLock` in `tests/cobalt/test_backup.py` (T1–T4). No with-DB red; no lock taken at E2. `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_backup.py` on `86dc425a` + tests: `4 failed, 23 passed in 0.07s`. Each red's first line:
- T1 `test_two_snapshots_started_together_both_finish`: `AssertionError: {'run2': FileNotFoundError('/private/var/folders/…/test_two_snapshots_started_tog0/cobalt_brain.sql')}` — run 2's `FileNotFoundError`, the row's reason.
- T2 `test_a_lock_held_past_the_wait_fails_loud`: `Failed: DID NOT RAISE <class 'cobalt.backup.restic.BackupError'>`.
- T3 `test_the_cleanup_leaves_another_sql_file_in_place`: `AssertionError: the cleanup removed a .sql file this run did not write`.
- T4 `test_the_lock_wait_is_thirty_minutes`: `AttributeError: module 'cobalt.backup.restic' has no attribute 'LOCK_WAIT_S'`.
- Rewritten once: T2's first red was `AttributeError: … has no attribute 'LOCK_WAIT_S'` at its `monkeypatch.setattr`; it now passes `raising=False`, and its red is `DID NOT RAISE`, the row's reason.
- The 23 existing tests (`TestSnapshotRefusals`, `TestMountGuard`, `TestStagingPath` among them) passed.
Commit `f28bb2bf wip(backup-flock-1012): red`.

## E3 THE ROWS
F1, `src/cobalt/backup/restic.py`: `LOCK_WAIT_S = 1800` with its `#:` comment after `STAGING`; imports `fcntl`, `time`; in `snapshot()`, after `STAGING.mkdir` and before the `try`, `os.open(STAGING / ".backup.lock", O_RDWR | O_CREAT, 0o600)`, `os.chmod(…, 0o600)`, `flock(LOCK_EX | LOCK_NB)` retried each ≤1 s until `LOCK_WAIT_S` has passed, then `BackupError` naming the lock path, the seconds waited and the holder pid (fd closed, nothing written or removed); the pid written once taken. The dump path is `STAGING / f"{cfg.database.name}.sql"`, set before `dump_database` runs; the `finally` unlinks that one path (`missing_ok=True`), then `LOCK_UN` and `os.close`. `STAGING` and `LOCK_WAIT_S` are read at call time. Header and `finally` comment carry the rule. DevDocs: `docs/40 - DevDocs/cobalt/backup/restic.md` `## 2026-10-12 — backup-flock-1012`.

Green: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_backup.py tests/cobalt/test_db_apply.py tests/cobalt/test_db_credentials.py tests/cobalt/test_generated_commit.py` → `175 passed, 3 skipped in 12.24s` (skips: `test_db_credentials.py:179`, `:191`, `:202` `requires_db: live factory role proofs need cobalt_dev`).

Mutations (Edit tool, each undone, `-k TestStagingLock`):
| mutation | result | first failing line |
|---|---|---|
| M1 the `finally` globs `STAGING.glob("*.sql")` again | `1 failed, 3 passed` | T3 `AssertionError: the cleanup removed a .sql file this run did not write` |
| M2 the `fcntl.flock(fd, LOCK_EX \| LOCK_NB)` call removed | `2 failed, 2 passed` | T1 `AssertionError: {'run2': FileNotFoundError('…/cobalt_brain.sql')}`; T2 `Failed: DID NOT RAISE <class 'cobalt.backup.restic.BackupError'>` |
| M3 `LOCK_WAIT_S = 900` | `1 failed, 3 passed` | T4 `assert 900 == 1800` |
After undo: `git diff --stat` → ` src/cobalt/backup/restic.py | 58 ++++++++++++++++++++++++++++++++++++++++-----` (the fix only); `tests/cobalt/test_backup.py` → `27 passed in 10.33s`.
Commit `e9964a3d fix(backup-flock-1012): snapshot() holds STAGING/.backup.lock and removes only its own dump (F1, L1, L28)`.

Entry paths pinned after the first commit (PRE-STOP SELF-CHECK 2), tests only, in `TestStagingLock`:
- T5 `test_a_dump_that_raises_mid_write_is_removed_and_the_lock_released` (CHECK ASK X1, X2).
- T6 `test_with_the_database_off_nothing_in_staging_is_removed` (X1).
- T7 `test_a_dry_run_takes_the_lock_and_removes_its_own_dump` (the `dry_run` flag of `backup/cli.py:49`).
- T1 now sets `LOCK_WAIT_S` to `3 * WAIT` (30 s, `raising=False`) and joins at `5 * WAIT`: a lock never released fails T1 loud instead of hanging 1800 s (found by M6 below; the first M6 run hung and was stopped).

| mutation | result | first failing line |
|---|---|---|
| M4 `dump = dump_database(cfg.database.name, STAGING)` (path bound after the write) | `1 failed, 6 passed` | T5 `AssertionError: assert not True` (`cobalt_brain.sql` exists) |
| M5 the `finally` unlinks `STAGING / f"{cfg.database.name}.sql"` whether or not the run reached the dump | `1 failed, 6 passed` | T6 `FileNotFoundError: … test_with_the_database_off_not0/cobalt_brain.sql` |
| M6 `LOCK_UN` and `os.close` removed from the `finally` | `4 failed, 3 passed in 30.29s` | T1 `{'run2': BackupError('another backup run holds …/.backup.lock (pid 86517); waited 30.0 s (LOCK_WAIT_S 30). No dump was written and nothing in STAGING was removed.')}`; T5, T6, T7 `assert False` (`_lock_is_free`) |
| M2 again, on the bounded T1 | `2 failed` | T1 `{'run2': FileNotFoundError('…/cobalt_brain.sql')}`; T2 `DID NOT RAISE` |
After undo: `git diff --stat` → `tests/cobalt/test_backup.py` only (the uncommitted tests); green `178 passed, 3 skipped in 12.17s` (same four files). Commit `964b6105 fix(backup-flock-1012): pin the raising dump, database-off and dry-run paths; T1 wait bounded (F1, L1)`.

R3 (RUN): see `## RESTARTS`; the table matches the row's expected `com.cobalt.radar`.

## RESTARTS
`uv run cobalt jobs restarts 86dc425a..HEAD`, exit 0 (the tool lists the untracked report too):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/backup/restic.md	M	DOCS	-
docs/40 - DevDocs/reports/backup-flock-build-2026-10-12.md	A	DOCS	-
src/cobalt/backup/restic.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_backup.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. Re-run at `964b6105`: the same table, last line `RESTARTS: com.cobalt.radar`.

## W THE THREE SUITES
`<tip>` = `964b6105`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh backup-flock-1012 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: it writes no rows; no `--migration`), exit 0. Verdict lines whole:
```
offline 4316/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5219/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/backup-flock-1012-all-20261012-222721.log
```
- (a) offline `4316 passed, 806 skipped, 1 xfailed, 36 warnings in 639.51s` (log `:885`); E0 was 4309, this build adds 7 (T1–T7 of `TestStagingLock`). No skip line is marked `OUTSIDE the allowed set`.
- (b) `lock taken: backup-flock-1012` (`:891`); `ls -la /Users/cobalt/cobalt-wt/*/.env` → this worktree's only (`:896`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:902`); proof-only `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` / `TABLES 0011` → `LEVEL 0013`. It printed `code: 964b6105 (DIRTY: 1 path(s))`: the uncommitted report.
- (c) pass 1, executed (`:958`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py` → `5014 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 786.06s` (`:1115`) = `<d1>` 5014.
- (c2) `dev forward: APPLIED 22:51:31` (`:1117`); `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1195`).
- (c3) pass 2 → `205 passed, 1 deselected, 5 warnings in 227.70s` (`:1969`) = `<d2>` 205; `<d>` = 5014 + 205 = 5219 = `with-DB 5219/0`. No with-DB test of this build.
- (c3r) `stray rows: not read (no --tickers given)`: no with-DB test of this build writes a ticker.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2037`) → **`cobalt_dev: 0013 — F2 = F0`**; `lock released` (`:2091`); **`.env: removed`**; `ls /Users/cobalt/cobalt-wt/backup-flock-1012/.env` → `No such file or directory`.
- (e) live-note `146 passed, 1 skipped, 15 warnings in 25.37s` (`:2160`) → `live-note 146/0`; the skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`).

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its reason: T1–T4 at E2 (run 2's `FileNotFoundError`, `DID NOT RAISE`, `the cleanup removed a .sql file this run did not write`, `AttributeError … LOCK_WAIT_S`) and again under M1–M3; T5 under M4, T6 under M5, T7 (and T1, T5, T6) under M6. One test rewritten at E2 (T2, `raising=False`); T1 bounded after M6 hung, then red again under M2.
(2) Entry paths: the one caller `src/cobalt/backup/cli.py:49` (`snapshot(dry_run=args.dry_run)`) reaches `snapshot()`, which every test calls directly; its `dry_run` flag → T7; database on → T1, T3; database off → T6; the dump raising → T5; the lock held past the wait → T2; the two refusals (zero armed, unmounted) fire before the lock → `TestSnapshotRefusals`, `TestMountGuard`, green at the tip.
(3) Re-read at the tip `964b6105`: `grep -n -F "LOCK_WAIT_S" src/cobalt/backup/restic.py` → `56:LOCK_WAIT_S = 1800`, `:203`, `:210`, `:213`; `grep -rn -F "LOCK_WAIT_S" src configs` → `restic.py` only; `grep -n -F "unlink" src/cobalt/backup/restic.py` → `:190` (comment), `240:                dump.unlink(missing_ok=True)`; `grep -n -F "glob" src/cobalt/backup/restic.py` → nothing; `grep -n -F "def test_" tests/cobalt/test_backup.py` → T1 `:273` … T4 `:412`; the gate log lines above by `grep -n -F`.

## FOR THE CHECK
- Range `86dc425a..964b6105`: `f28bb2bf wip(backup-flock-1012): red` · `e9964a3d fix(backup-flock-1012): snapshot() holds STAGING/.backup.lock and removes only its own dump (F1, L1, L28)` · `964b6105 fix(backup-flock-1012): pin the raising dump, database-off and dry-run paths; T1 wait bounded (F1, L1)`.
- F1 reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS`. Callers: `## PREFLIGHT` (`backup/cli.py:49`, `restic.py:184`).
- R3 output: `## RESTARTS`.
- Suites, `F0` / `F1` / `F2`, lock taken / released: `## W THE THREE SUITES` (one take, inside `gate.sh`, `lock: waited 0 min`).
- CHECK ASKS: X1 the one unlink is `restic.py:240`, of `dump`, set only once the run reaches the dump; a refusal or a lock timeout returns before `dump` exists (T2: no dump called; T6). X2 the flock is taken before `dump_database`, released in the `finally` after the unlink; the acquire block closes the fd on every raise (`except BaseException: os.close(fd)`). X3 the lock file is never unlinked (unlink grep above); restic's targets are `cfg.sources` plus `dump`. X4 run 2 starts only after `dump1_written`; on BASE its `FileNotFoundError` is ordered by `run1_done`, no sleep. X5 `LOCK_WAIT_S = 1800` at `restic.py:56`, no other home.
- Records copied at PREFLIGHT: there.

## CONTINUE
next: CLOSE

## DECISIONS
none

## RECORDS
- A first gate call at `e9964a3d` (log `/Users/cobalt/cobalt-wt/.gate-logs/backup-flock-1012-all-20261012-221912.log`) was stopped in its offline pass to pin T5–T7 first; before the stop `ls -la /Users/cobalt/cobalt-wt/backup-flock-1012/.env` → No such file; after it `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` and the `.env` → No such file. No lock was held.
- A first M6 run of the whole class hung on T1 (run 2 waiting the real 1800 s) and was stopped; T1 was bounded (E3).
- T1's order: the row names run 2's `FileNotFoundError` as the red; its prose also says "on BASE run 1 then raises FileNotFoundError". On BASE run 1 reads run 2's same-named dump and finishes; run 2, released by `run1_done`, finds its dump globbed away. The red is run 2's, the row's named reason.
- The house shape cited as `scratch.py:211` for `os.chmod` is at `:210` (`:211` `ftruncate`, `:212` `pwrite`).
- No extra lock take. No `REFUSED, not needed` line. No `CONTINUE` message.
- `.env: removed, proven gone (W)`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: backup-flock-1012 · tip: 964b6105 | on 86dc425a | migration: none | offline 4316/0 | with-DB 5219/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 173752
