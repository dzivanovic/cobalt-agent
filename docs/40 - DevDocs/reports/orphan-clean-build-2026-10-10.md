# orphan-clean-1010 — build report (2026-10-10)

## §0 Headline
- `ops/desk/orphan-clean.sh` built: rows O1–O4, 4 of 4. Tip `0ddb7114` on `1286d448`.
- Gate green: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`. `tests/ops` 2739 passed at the tip.
- 36 new tests, all red on BASE because the script did not exist. Nine mutations, two of them negative controls, each turned the named test red, and each was undone.
- One decision for the desk (D1): the card's launchctl rule refuses a job that is loaded but has no pid, and that may be the incident's own state.

## L74
One system notice in this session asked for an extra `Claude-Session:` trailer on commits. It was recorded here and not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md" · 0 · 1eb47b5928dfc5fb90fe0fa950da19c2c6681bc2
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 17:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| base | `git show --stat 1286d448` | 0 | `1286d448 docs(desk): R861 aset-orphan preflight launch` · `docs/40 - DevDocs/reports/cto-2026-10-10.md \| 1 +` |
| lock take | `grep -n -F "DirectoryLock(" src/cobalt/voice/web.py` | 0 | `161:    lock = scratch.DirectoryLock(cfg.scratch_dir)  # ScratchLocked → the start fails loud` |
| port | `grep -n -F "5010" src/cobalt/aset/config.py` | 0 | `82:    port: int = Field(default=5010, gt=0, lt=65536)` |
| lock name | `grep -n -F "LOCK_NAME" src/cobalt/voice/scratch.py` | 0 | `43:LOCK_NAME = ".lock"` · `199:        self.path = self.directory / LOCK_NAME` · `247:        if entry.name == LOCK_NAME:` · `266:    "CONTENT_TYPES", "DirectoryLock", ...` |
| scratch dir | Read `ops/start_aset.sh` | — | `35:export COBALT_VOICE_SCRATCH_DIR="/Users/cobalt/.cobalt/voice-scratch"` · `73:exec uv run python -m cobalt.aset` |
| pid write / release | Read `src/cobalt/voice/scratch.py` 193–231 | — | `212:        os.pwrite(self._fd, str(os.getpid()).encode(), 0)`; `release` 225–231 unlocks and closes, never truncates |
| plist | Read `ops/com.cobalt.aset.plist` | — | `29: <key>AbandonProcessGroup</key>` `30: <true/>` |
| restarts ops/desk | `grep -n -F "operator script" src/cobalt/jobs/restarts.py` | 0 | `232:                Classification(path, item.change, "operator script; no Cobalt reader", ())` |
| radar argv | `grep -n -F "ProgramArguments" -A 5 ops/com.cobalt.radar.plist` | 0 | `18: /Users/cobalt/.local/bin/uv` `19: run` `20: cobalt` `21: radar` |
| agent argv | `grep -n -F "main.py" cobalt.sh` | 0 | `59:        nohup uv run src/cobalt_agent/main.py > logs/mattermost_session.log 2>&1 &` |
| CLASSES | `grep -n -F "CLASSES" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | 0 | `31:## CLASSES — approved once, 2026-10-02 R39` |
| NEVER launchctl | `grep -n -F "launchctl" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | 0 | `23:- \`launchctl\` on a build or check line; on the deploy line, on no label but ...` (and 29, 145–148, 151) |
| READ tail | `tail -n 3 ".../aset-orphan-answer-2026-10-10.md"` | 0 | last line: `FOR THE CHECK: aset-orphan brain 10-10 — AbandonProcessGroup true (plist:29) plus exec uv run (start_aset.sh:73) orphans python on bootout; ...` |
| READ tail | `tail -n 3 ".../cto-2026-10-10.md"` | 0 | last line: `HANDOVER: predecessor 91f18257 → successor c3a40831 at 07:52 · pane w2:pV1` |
| RESTARTS | `uv run cobalt jobs restarts 1286d448..HEAD` | 0 | `docs/40 - DevDocs/reports/orphan-clean-build-2026-10-10.md	A	DOCS	-` · `RESTARTS: none` (the untracked report only; no code path) |
| wc -l | new files only (`ops/desk/orphan-clean.sh`, `tests/ops/test_orphan_clean.py`) | — | do not exist at BASE |

```
clock · date · 0 · Sat Oct 10 08:03:26 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/orphan-clean-1010
    ?? "docs/40 - DevDocs/reports/orphan-clean-build-2026-10-10.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 1286d448 docs(desk): R861 aset-orphan preflight launch
diff · git diff --stat 1286d448 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/orphan-clean-1010 · 0 · 1286d448 docs(desk): R861 aset-orphan preflight launch
env here · ls /Users/cobalt/cobalt-wt/orphan-clean-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
Card RECORDS copied: RESTARTS none (re-read: `restarts.py:232`, above); DB: every row file under `ops/` or `tests/ops/` (the card header carries no `DB: none`, so W runs the full gate); THE WIDENING (CLASS (a), `STANDING-LIST.md` lines 23, 31, 36 re-read above); OWED ON HIS APPROVAL: the `STANDING-LIST.md` line for `--kill` (not in this job); incident facts pid 39280 / 66658 (`cto-2026-10-10.md` R851, R854 re-read above).

`<FP>`: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"` (run inside `gate.sh` at W).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 704.70s (0:11:44)`. The only skips naming `COBALT_LIVE_VAULT_ROOT` are the offline run's two expected ones (`test_catalyst.py:365`, `test_predicate.py:262`).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.85s`. Skip: `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC ... not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`tests/ops/test_orphan_clean.py` (478 lines), commit `2dede2d3 wip(orphan-clean-1010): red`. Offline, no with-DB red, no lock taken at E2.
`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_orphan_clean.py` → `36 failed, 15 warnings in 1.17s`. Every red has the rows' named reason, "no script":
- `E   FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/orphan-clean-1010/ops/desk/orphan-clean.sh'` (the script-text tests)
- `E   AssertionError: sh: /Users/cobalt/cobalt-wt/orphan-clean-1010/ops/desk/orphan-clean.sh: No such file or directory` / `assert 127 == 1` (O1: `sh` exits 127, not 1), and `assert 127 == 0` (O2–O4).
- `E   AssertionError: assert [] == [['-TERM', '7002']]` (`test_pid_reused_between_term_and_kill_is_not_signalled`, line 476: no script, so no TERM).

Harness (card text): `ps`, `launchctl` and `lsof` are Python stubs placed first on PATH, ahead of the `tests/ops/conftest.py` guard bin. They answer from `table.json` and log argv to `calls.jsonl`. `ORPHAN_CLEAN_KILL` is a stub that edits the table. `ORPHAN_CLEAN_GRACE=1`. `Fake.run` asserts after every run that no stub log names a pid outside the table. `test_script_text_holds_no_broad_kill` asserts that the script text holds none of `pkill`, `pgrep`, `killall` or `kill -9 $(`. Every pid and start time is constructed (7xxx, the year 2099).

## E3 THE ROWS
Commit `0ddb7114 feat(orphan-clean-1010): ops/desk/orphan-clean.sh finds, verifies and kills an aset orphan by pid (O1-O4, L1, L3)`. One new file, `ops/desk/orphan-clean.sh` (264 lines).
- O1: a closed `case` holds the one label, `aset`. The only call shapes are `<label>` and `--kill <label>`; any other shape is refused before any read. The header names every command the script runs, its lock, port and job, and R851/R853/R854/R855.
- O2: `ps -A -o pid= -o ppid= -o command=`. A candidate has ppid 1 and exactly 3 words: `<path>/python|python3|python3.N`, `-m`, `cobalt.aset`. `launchctl print gui/501/com.cobalt.aset` returns `Could not find service` (no job pid), or exactly one top-level (one-tab) `state = running` line and one `pid = <n>` line (the job pid, SPARED); any other output is REFUSED. Each remaining candidate goes through `lsof` for the lock (`n<lock>`) and the port (`p<pid>`), then a `ps -p <pid> -o ppid= -o lstart= -o command=` identity read (ppid 1). Any UNVERIFIED candidate → REFUSED after the loop, nothing signalled.
- O3: the dry run prints `WOULD KILL:` and the dry-run last line, or `none found`.
- O4: each signal is preceded by an identity re-read (else `REFUSED: <pid> changed before <SIG>`). Then `RUN:` is printed, `"$KILL" -TERM`, polled once a second up to the grace, then `-KILL`, polled again. Then `KILLED: <pid> (<SIG>)`, or `FAILED: <pid> survived KILL` with exit 1.
- Row greens: `tests/ops/test_orphan_clean.py` → `36 passed, 15 warnings in 14.38s`. After every mutation was undone → `36 passed, 15 warnings in 14.44s`. Beside them, `tests/ops` → `2739 passed, 1 xfailed, 15 warnings in 536.45s`.
- DevDocs: no `src/` module changed. No page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` scripts (`house-probe.sh` has none either; grep above). No line was written (RECORDS).

THE MUTATIONS (made and undone with Edit; after each undo the file passed 36/36 and a grep for the mutation strings came back empty, exit 1):
| row | mutation | run | red (first failing line) |
|---|---|---|---|
| O1 | `aset)` → `aset\|radar)` | `-k test_label_table` | `2 failed, 7 passed` · `assert 0 == 1` (`radar` dry-run and `--kill radar` accepted) |
| O2 | `is_candidate "$@" \|\| continue` → `case "$*" in *cobalt.aset*)` substring | `-k test_find_and_verify` | `1 failed` · `At index 0 diff: 'CANDIDATE: 7100 ppid 1 /Users/cobalt/.local/bin/uv run python -m cobalt.aset' != 'CANDIDATE: 7002 ...'` |
| O2 neg. control | the job-pid test → `if false` | `-k test_spares_the_job_pid` | `1 failed` · `assert [] == ["SPARED: 730...et's own pid"]` |
| O2 (4) | `[ "$holds" = no ]` → `= never` | `-k unverifiable` | `2 failed` · `assert 0 == 1` (`RUN: kill -TERM 7002` / `KILLED: 7002 (TERM)` on a candidate holding neither) |
| O2 (2) | launchctl state/pid refusals → `:` | `-k test_unknown_launchctl_shape` | `5 failed, 1 passed` (the exit-5 case is refused by the exit-code branch, not by this check) |
| O3 | `[ "$mode" = dry ]` → `= never` | `-k test_dry_run_kills_nothing` | `1 failed` · `assert [] == ['WOULD KILL: 7002']` |
| O4 | `elif signal "$pid" KILL` → `elif false` | `-k "escalates or survives"` | `2 failed` · `FAILED: 7002 survived KILL` / `assert [['-TERM', '7002']] == [['-TERM', '7...ILL', '7002']]` |
| O4 | pre-signal re-read → `: \|\| refuse` | `-k test_pid_reused_is_not_signalled` | `1 failed` · `assert 0 == 1` (`RUN: kill -TERM 7002` sent to the reused pid) |
| O4 neg. control | `[ "$ppid" = 1 ] \|\| continue` → `: \|\| continue` | `-k "test_kill_term_enough or test_find_and_verify"` | `2 failed` · `CANDIDATE: 7101 ...` / `UNVERIFIED: 7101 — ps -p no longer shows it with ppid 1` (the healthy child becomes a candidate; the identity read's ppid check refuses the run) |

## RESTARTS
`uv run cobalt jobs restarts 1286d448..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/reports/orphan-clean-build-2026-10-10.md	A	DOCS	-
ops/desk/orphan-clean.sh	A	operator script; no Cobalt reader	-
tests/ops/test_orphan_clean.py	A	test/documentation; no resident	-
RESTARTS: none
```

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh orphan-clean-1010 all --deploy` (no `--deselect`, no `--tickers`, no `--migration`: this build adds no with-DB test). Exit 0. Verdict lines:
```
offline 4196/0
lock: waited 71 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5093/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/orphan-clean-1010-all-20261010-083102.log
```
No skip is marked `OUTSIDE the allowed set`. Log reads: `896:F0: 664 35 272c95bbb12241e3611e4b36326ccf87` · `1188:F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` · `2030:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (F2 = F0 field for field). Lock: `884:$ sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh orphan-clean-1010 90` → `885:lock taken: orphan-clean-1010` (waited 71 min) · `2083:$ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh orphan-clean-1010` → `2084:lock released`. `944: code: 0ddb7114 (DIRTY: 1 path(s))` = the untracked report.
Pass 1 executed (log line 952): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py`
The gate's suites do not include `tests/ops`, so it was run at the tip by itself: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `2739 passed, 1 xfailed, 15 warnings in 502.66s (0:08:22)`.
`ls /Users/cobalt/cobalt-wt/orphan-clean-1010/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red: all 36 at E2 (no script; the lines are quoted above). Each row's logic was also shown red under its mutation in E3's table, including both negative controls (`test_spares_the_job_pid`; the residents under the ppid mutation). No test stayed green under its mutation. `launchctl4` (exit 5) is pinned by the exit-code branch, not by the shape check; that branch is part of the same rule.
(2) Callers: `grep -rn -F "orphan-clean.sh" src ops` → only the script's own lines 2, 3, 64 and 67. No other caller exists; nothing calls it yet (the STANDING-LIST line is owed, RECORDS). Entry paths pinned:
- the 9 call shapes (`test_label_table_and_refusals`);
- dry run / `--kill` × verified / spared / none (`test_dry_run_*`, `test_spares_the_job_pid`, `test_kill_*`);
- the job loaded / not found / 6 unknown shapes;
- lock and port proofs (`test_find_and_verify`, `test_verified_by_the_port`);
- the 3 interpreter spellings;
- 5 decoys;
- ps, lsof and odd-line failures;
- pid reuse before TERM and between TERM and KILL;
- TERM-ignoring and unkillable.
(3) Re-read at the tip: `git show 0ddb7114:ops/desk/orphan-clean.sh` (whole); `git log --oneline 1286d448..HEAD`; `wc -l` of both files; the gate log greps for `F0: `, `F1: `, `F2: `, `pass 1: whole (deploy)` and `lock`; `ls .env`.

## FOR THE CHECK
- Range `1286d448..0ddb7114`: `2dede2d3 wip(orphan-clean-1010): red` · `0ddb7114 feat(orphan-clean-1010): ops/desk/orphan-clean.sh finds, verifies and kills an aset orphan by pid (O1-O4, L1, L3)`.
- Reds, mutations, greens: `## E2 RED`, `## E3 THE ROWS`. RUN rows: none on this card.
- Suites: `## W THE THREE SUITES`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `908 45 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. The lock was taken after a 71-min wait and released at log line 2084.
- RESTARTS: `## RESTARTS` (none).
- Records copied at PREFLIGHT: `## PREFLIGHT`.
- X1: the script signals only a pid that passed every one of these:
  - ppid 1 and an exact 3-word command;
  - not the launchctl job pid;
  - `lsof` lock or port proof;
  - identity read with ppid 1;
  - an identity unchanged right before each signal.
  The `.lock` content is never read.
- X2: every failing tool path ends in REFUSED, exit 1, before any signal (verify runs fully before the kill loop).
- X3: the stubs come first on PATH, and the conftest guard turns any `launchctl` call that misses the stubs into exit 127. Real `kill` is never reached: `ORPHAN_CLEAN_KILL` is always set in `fake`. Real `ps` and `lsof` cannot be reached while the stubs come first on PATH.
- X4: `mode=dry` is the default; `--kill` must be `$1` with exactly 2 args.
- X5: the header lists `ps -A`, `launchctl print`, both `lsof`, `ps -p`, `kill -TERM/-KILL`, `sleep 1`, `mktemp -d`, `rm -rf` of its own dir, `grep`, `sed`, `printf`, and `TOUCHES:`; `test_header_names_every_command_and_the_reports` checks these.

## CONTINUE
next: none (BUILT)

## DECISIONS
- D1 (ASK DESK, not blocking): the card's O2 (2) says only "Could not find service" or "`state = running` with one `pid`" is readable, and any other launchctl shape is REFUSED. In the R851 incident the job was loaded while KeepAlive restarts failed on the lock. `launchctl print` then likely shows a state other than `running` (e.g. `not running` / `spawn scheduled`) and no `pid =`. If so, the script refuses in the very state it exists for. **Safe default taken:** built as the card says (pinned by `test_unknown_launchctl_shape_fails_loud[launchctl0]`, `state = not running`). Widening it (treat a loaded job with no pid as "no job pid") would be a new row on the card's seam (L72); the desk decides.
- D2 (recorded, not blocking): a `ps -A` failure has no pid to name, and is REFUSED with `ps -A exited <n>: <stderr>`. An unparsable ps line prints `UNVERIFIED: ? — ps line does not parse: <line>`, then REFUSED. Both follow row O2 (4)'s "UNVERIFIED then REFUSED", with `?` in place of the pid.

## RECORDS
- `.env: removed, proven gone (W)`. The gate's lock waited 71 min and was released (`2084:lock released`). No extra lock take.
- DevDocs: no line written. No `src/` module changed, and no page under `docs/40 - DevDocs/cobalt/` holds `ops/desk/` scripts (`house-probe.sh` has no page either).
- Owed on his approval (card RECORDS, not in this job): the `STANDING-LIST.md` line naming where `orphan-clean.sh --kill` may run. Until that line exists, no seat runs `--kill`.
- The card's records, re-read at PREFLIGHT: RESTARTS none (`restarts.py:232`); every file under `ops/` and `tests/ops/`; the CLASS (a) widening (`STANDING-LIST.md` lines 23, 31, 36); incident pids 39280 / 66658 (R851, R854).
- No `REFUSED, not needed` and no `CONTINUED` line.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: orphan-clean-1010 · tip: 0ddb7114 | on 1286d448 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 186094
