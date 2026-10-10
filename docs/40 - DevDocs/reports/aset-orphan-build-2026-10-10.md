# aset-orphan-1010 — build report (2026-10-10)

CARD: `docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md` · BRANCH `ops/aset-orphan-1010` · BASE `ddaae952` · started 08:02:47 EDT

## §0 Headline
Row A built: `ops/start_aset.sh` now runs `uv sync --inexact`, then `exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset`, so launchd's pid is the python and a bootout leaves no child behind. The plist is unchanged.
Row B audit: of the 15 plists, aset was the only KeepAlive job that paired `AbandonProcessGroup` with a `uv` pid. No other plist or script changed.
Three suites green on `1987849b`: offline 4196/0 · with-DB 5093/0 · live-note 146/0; `cobalt_dev` back at 0013 (F2 = F0). RESTARTS: com.cobalt.aset.
6 decisions, none for Dejan. Main one: `uv sync --help` was refused on this launch line, so `--inexact` is built as the card states but not proven by tool output.

## L74
none.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md"` → exit 0, WHOLE:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md" · 0 · ea3ac11c70799e8b6d7de0f75c1ca3f974ff4d60
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, WHOLE:
```
clock · date · 0 · Sat Oct 10 08:03:06 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/aset-orphan-1010
    ?? "docs/40 - DevDocs/reports/aset-orphan-build-2026-10-10.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · ddaae952 docs(desk): R860 S5 tribunal shape
diff · git diff --stat ddaae952 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/aset-orphan-1010 · 0 · ddaae952 docs(desk): R860 S5 tribunal shape
env here · ls /Users/cobalt/cobalt-wt/aset-orphan-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat ddaae952` · 0 · `docs(desk): R860 S5 tribunal shape` — `docs/40 - DevDocs/reports/cto-2026-10-10.md | 1 +`.

THE CARD'S SYMBOLS (rule · command · exit · output):
| symbol | command | exit | output |
|---|---|---|---|
| start_aset.sh:73 | `grep -n -F "exec uv run python -m cobalt.aset" ops/start_aset.sh` | 0 | `73:exec uv run python -m cobalt.aset` |
| start_aset.sh:67 / :35 / :68–72 | Read `ops/start_aset.sh` whole (73 lines) | — | `67:cd "$REPO_ROOT"`; `35:export COBALT_VOICE_SCRATCH_DIR="/Users/cobalt/.cobalt/voice-scratch"`; `:68–72` the "Resolve uv via PATH" comment. (A `grep -F` with `$` in the pattern printed nothing — the hub's no-`$` rule; the Read is the proof.) |
| aset.plist:29–30 | `grep -n -F "AbandonProcessGroup" ops/com.cobalt.aset.plist` | 0 | `29:    <key>AbandonProcessGroup</key>` (`:30 <true/>` by Read) |
| scratch.py DirectoryLock | `grep -n -F "class DirectoryLock" src/cobalt/voice/scratch.py` | 0 | `193:class DirectoryLock:` (`:202 fcntl.flock(self._fd, fcntl.LOCK_EX \| fcntl.LOCK_NB)`, `:209 raise ScratchLocked(...)` by Read) |
| ScratchLocked | `grep -n -F "ScratchLocked" src/cobalt/voice/scratch.py` | 0 | `21:`, `72:class ScratchLocked(RuntimeError):`, `209:`, `266:` |
| ops/README.md:31 | `grep -n -F "start_aset.sh" ops/README.md` | 0 | `31:\| \`com.cobalt.aset.plist\` \| \`ops/start_aset.sh\` → \`uv run python -m cobalt.aset\` (ASET sizing widget, :5010) \| RunAtLoad + KeepAlive (persistent) \| \`ops/start_aset.sh\` \| yes \|` (+ lines 78, 84, 92, 112, 147, 149) |
| test_jobs_reads.py:98–101 | `grep -n -F "start_aset.sh:73" tests/cobalt/test_jobs_reads.py` | 0 | `100:        (ops/start_aset.sh:73), the radar (ops/com.cobalt.radar.plist) and` |
| every `start_aset.sh:73` citation | `grep -rn -F "start_aset.sh:73" configs src tests ops` | 0 | `configs/cobalt/jobs.yaml:88`, `configs/cobalt/jobs.yaml:89`, `tests/cobalt/test_jobs_reads.py:100` |
| jobs.yaml:87–89 | Read | — | `87: - "ops/start_aset.sh" # ops/com.cobalt.aset.plist:25 (the program)…`; `88/89: "pyproject.toml"/"uv.lock" # ops/start_aset.sh:73 (exec uv run python -m cobalt.aset): uv syncs the environment from it when the process starts` |
| jobs.yaml:139–145 | Read | — | `140: # shape, not a preference: cobalt.sh spawns the agent detached` / `# (\`nohup\`, and the plist sets AbandonProcessGroup) and EXITS 0.` |
| cobalt.sh:59, :71 | Read `cobalt.sh:55–72` | — | `59: nohup uv run src/cobalt_agent/main.py > logs/mattermost_session.log 2>&1 &`; `71: kill -15 "$PID"` |
| run_backup.sh:39 | `grep -n -F "exec" ops/run_backup.sh ops/start_mainframe.sh` | 0 | `ops/run_backup.sh:39:exec /Users/cobalt/.local/bin/uv run cobalt backup run` |
| start_mainframe.sh stop_previous_heartbeat | `grep -n -F "stop_previous_heartbeat" ops/start_mainframe.sh` | 0 | `71:`, `191:stop_previous_heartbeat() {`, `245:stop_previous_heartbeat                  # was: pkill -9 -f caffeinate` |
| archiver store.py:64 | `grep -n -F "pg_try_advisory_lock" src/cobalt/archiver/store.py` | 0 | `64:        "SELECT pg_try_advisory_lock(%s)", (ARCHIVE_RUN_LOCK_KEY,)` |
| DEPLOY-HUB:88 | Read line 88 | — | `… A plist ADDED or MODIFIED anywhere under ops/ is refused, except one under ops/desk/ …` |
| DEPLOY-HUB:137 | Read line 137 | — | `4.2 for each of \`com.cobalt.aset\`, \`com.cobalt.radar\` in \`<restart set>\`: \`launchctl bootout gui/501/<label>\`; …` |
| restarts.py:198–260 | Read | — | `245–246: tests/ → "test/documentation; no resident"`; `247–248: ops/README.md → "operations documentation; no resident"`; `207–210: readers → "resident reads"` |
| plist list | Glob `ops/com.cobalt.*.plist` | — | 15 files: agent, archiver, aset, backup, cards-expire, daymode-propose, generated, heartbeat, herdr, mainframe, obsidian, prefill-daily, radar, replay, seat-usage (the card says 16; its own enumeration names 15 — `## DECISIONS` 2) |

`wc -l`: `73 ops/start_aset.sh` · `411 ops/README.md` · `238 tests/cobalt/test_jobs_reads.py` (`tests/ops/test_launchd_orphan.py` is new).
`tail -n 3` of `aset-orphan-answer-2026-10-10.md` → last line: `FOR THE CHECK: aset-orphan brain 10-10 — AbandonProcessGroup true (plist:29) plus exec uv run (start_aset.sh:73) orphans python on bootout; fix one of (i)/(ii) with a RED file test; audit all resident plists; the pgrep hub row is his (L9), recorded not built; the deploy's own 4.2 proves no orphan via ps -p of the old pid.`

`uv sync --help` (the card's row A ask) → REFUSED by `dontAsk` (not a listed string). `## DECISIONS` 1.

`## RECORDS` of the card, copied: code read at `d0a5fbb8`, main HEAD at draft `c3a484e4`, no non-docs diff since (desk's fact; not re-readable on my list beyond `git -C` log); RESTARTS expectation (re-read at RESTARTS); DEPLOY PROOF (the deploy's, not mine); approval row R685 (re-read at AUTHORIZATION: row 38, APPROVED); no new command.

`uv run cobalt jobs restarts ddaae952..HEAD` · 0 · (first run created `.venv`, 253 packages) →
```
path	change	rule	restart
docs/40 - DevDocs/reports/aset-orphan-build-2026-10-10.md	A	DOCS	-
RESTARTS: none
```
(the only path is this report, untracked; no code in the range.)

DB: the card carries no "DB: none" key; no lock probe (L76 as amended). PROVEN BY FIRST REAL USE as the hub's table.

## E0 BASELINE
`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) · 0 · `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 708.35s (0:11:48)` — 0 failed, 0 errors.
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · 0 · `146 passed, 1 skipped, 15 warnings in 31.29s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
NEW `tests/ops/test_launchd_orphan.py` (A1, B1 ×4 [radar, aset, herdr, obsidian], B2, B3). No with-DB red: no lock taken at E2.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_launchd_orphan.py` · 1 · `2 failed, 5 passed, 15 warnings in 0.95s`. Reds, first lines:
- A1: `E       AssertionError` at `assert lines[-2:] == [SYNC_LINE, EXEC_LINE]` — `At index 0 diff: 'cd "$REPO_ROOT"' != 'uv sync --inexact'` (the last two code lines are `cd "$REPO_ROOT"`, `exec uv run python -m cobalt.aset`: row A's named reason).
- B1[com.cobalt.aset]: `E       assert "start_aset.sh ends 'exec uv run python -m cobalt.aset': exec uv run, launchd's pid is uv" is None` (row B's named reason).
- Green as named: B1[com.cobalt.radar], B1[com.cobalt.herdr], B1[com.cobalt.obsidian], B2, B3 (negative control).

## E3 THE ROWS
### Row A — `ops/start_aset.sh`
Re-read `:67` `cd "$REPO_ROOT"`, `:68–72` the uv-PATH comment, `:73` `exec uv run python -m cobalt.aset`. The `:68–72` comment is replaced by one saying why the python is exec'd directly; the tail is now (`grep -n -F "uv sync --inexact" ops/start_aset.sh` → `77:uv sync --inexact`):
```
77 uv sync --inexact
78 exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset
```
`ops/README.md:31` `Runs` cell → `` `ops/start_aset.sh` → `uv sync --inexact`, then `exec .venv/bin/python -m cobalt.aset` (ASET sizing widget, :5010; launchd's pid is the python) ``. `tests/cobalt/test_jobs_reads.py:100` docstring citation `start_aset.sh:73` → `start_aset.sh:77, \`uv sync --inexact\` before its exec`. The plist is untouched.
`--inexact` NOT confirmed by `uv sync --help` (refused, `## DECISIONS` 1).

### Row B — the audit, re-read at `ddaae952` (15 plists; `grep -n -F` of `<key>KeepAlive</key>`, `<key>AbandonProcessGroup</key>` (-A 1), `<key>ProgramArguments</key>` (-A 2), `<string>/` over every plist)
| plist | ProgramArguments[0] | KeepAlive | AbandonProcessGroup | finding |
|---|---|---|---|---|
| radar | `:18` `/Users/cobalt/.local/bin/uv` | `:28` dict (SuccessfulExit false) | absent | launchd kills the group: clean |
| aset | `:25` `ops/start_aset.sh` | `:42` true | `:29` true | WAS orphan-prone (`exec uv run`); row A fixed: B1 green |
| herdr | `:62` `/opt/homebrew/bin/herdr` | `:79` dict | absent | the binary itself: clean |
| obsidian | `:30` `/Applications/Obsidian.app/Contents/MacOS/Obsidian` | `:35` true | absent | the binary itself: clean |
| mainframe | `:35` `ops/start_mainframe.sh` | absent | absent | resident without KeepAlive; group killed; sweeps its own (`start_mainframe.sh:191 stop_previous_heartbeat() {`): clean |
| agent | `:25` `cobalt.sh` | absent | `:32` true | load-bearing: `cobalt.sh:59 nohup uv run … &` then exit 0; old tree (strangler), `cobalt.sh:71 kill -15 "$PID"` signals the `uv` pid — listed, not changed |
| archiver | `:25` `/Users/cobalt/.local/bin/uv` | absent | `:31` true | one-shot, `uv run` child; lock `store.py:64 pg_try_advisory_lock` released at run end; not booted out by a deploy: not harmful |
| backup | `:63` `ops/run_backup.sh` (`:39 exec /Users/cobalt/.local/bin/uv run cobalt backup run`) | absent | `:67` true | one-shot, no port: not harmful |
| cards-expire | `:33` uv | absent | `:41` true | one-shot, no port: not harmful |
| daymode-propose | `:27` uv | absent | `:35` true | one-shot, no port: not harmful |
| generated | `:33` uv | absent | `:46` true | one-shot, no port: not harmful |
| heartbeat | `:30` uv (`:39` uv again: the wrapped subprocess, `jobs run com.cobalt.heartbeat`) | absent | `:47` true | one-shot, no port: not harmful |
| prefill-daily | `:26` uv | absent | `:33` true | one-shot, no port: not harmful |
| replay | `:20` uv | absent | `:28` true | one-shot, no port: not harmful |
| seat-usage | `:34` uv | absent | `:42` true | one-shot, no port: not harmful |
No case the drafter's audit missed; row B changes no plist and no script beyond row A. (DEPLOY-HUB.md:137: 4.2 boots out `com.cobalt.aset`, `com.cobalt.radar` only.)

### Greens
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_launchd_orphan.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py` · 0 · `54 passed, 15 warnings in 17.95s`.
The other readers of `ops/start_aset.sh` (`grep -rn -F "start_aset" tests src`: `test_voice_config.py:211` reads its exports, `test_aset_vault.py:66` a comment, `test_jobs_restarts.py:145–186` path classification): `uv run pytest … tests/cobalt/test_voice_config.py tests/cobalt/test_aset_vault.py` · 0 · `77 passed in 0.49s`.
`uv run pytest -q -p no:cacheprovider --color=no tests/ops tests/cobalt/test_jobs_reads.py` · 0 · `2733 passed, 1 xfailed, 15 warnings in 526.00s (0:08:45)`.

### THE MUTATIONS (Edit tool, undone by Edit; `git diff --stat` after → only the three fix files, the test file identical to its red commit)
- A (undo the fix: last line back to `exec uv run python -m cobalt.aset`) → `2 failed, 5 passed`: A1 `At index 1 diff: 'exec uv run python -m cobalt.aset' != 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset'`; B1[com.cobalt.aset] `assert "start_aset.sh ends 'exec uv run python -m cobalt.aset': exec uv run, launchd's pid is uv" is None`.
- A′ (drop `uv sync --inexact`) → `1 failed, 6 passed`: A1 `At index 0 diff: 'cd "$REPO_ROOT"' != 'uv sync --inexact'`.
- B (helper's `exec uv` check off: `== "never-uv"`) → `1 failed, 6 passed`: B3 `TypeError: argument of type 'NoneType' is not a container or iterable` (line 122, the `exec uv run` case unflagged).
- B′ (helper's `AbandonProcessGroup` check removed) → `2 failed, 5 passed`: B1[com.cobalt.radar] `assert "/Users/cobalt/.local/bin/uv: launchd's pid is uv; its child is abandoned on bootout" is None`; B3 `… com.constructed.no-abandon.plist …` flagged.
`git diff --stat` after the last undo → `ops/README.md | 2 +-`, `ops/start_aset.sh | 17 +++++++++++------`, `tests/cobalt/test_jobs_reads.py | 2 +-` (3 files).
DevDocs: no `src/` module changed; there is no page for `ops/start_aset.sh` under `docs/40 - DevDocs/cobalt/` (`ls` of it: module folders only); its doc row is `ops/README.md:31` (edited). `## RECORDS`.
Commit `1987849b fix(aset-orphan-1010): start_aset.sh execs the venv python so launchd's pid is the python (A, B; L1, L42)`.

## RESTARTS
`uv run cobalt jobs restarts ddaae952..HEAD` · 0 · WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/aset-orphan-build-2026-10-10.md	A	DOCS	-
ops/README.md	M	operations documentation; no resident	-
ops/start_aset.sh	M	resident reads	com.cobalt.aset
tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
tests/ops/test_launchd_orphan.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset
```
No UNCLASSIFIED; matches the card's expectation.

## W THE THREE SUITES
`<tip>` = `1987849b`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh aset-orphan-1010 all --deploy` (background; no `--deselect`: this build adds no with-DB test; no `--tickers`: none written; no `--migration`) · exit 0. Verdict lines WHOLE:
```
offline 4196/0
lock: waited 17 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/aset-orphan-1010-all-20261010-083000.log
```
`grep -n -F "OUTSIDE the allowed set" <log>` → nothing. The `COBALT_LIVE_VAULT_ROOT` skips above are pass 1 (with-DB) skips; the live-note pass is `146/0`.
- (a) offline `4196/0`. This build's tests are under `tests/ops/` (not in the offline set): `tests/ops/test_launchd_orphan.py` — A1, B1[com.cobalt.radar], B1[com.cobalt.aset], B1[com.cobalt.herdr], B1[com.cobalt.obsidian], B2, B3 — run at E3 with all of `tests/ops`: `2733 passed, 1 xfailed`.
- (b) lock taken (`885:lock taken: aset-orphan-1010`, after `lock: waited 17 min` from the 08:30:00 gate start); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's (`890`). `896:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; proof-only → `LEVEL 0013`.
- (c) pass 1, executed command (`952`), WHOLE: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py` (the gate-lists' standing deselects; none added by this build).
- (c2) `1110:dev forward: APPLIED 09:12:51`; `1188:F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2: no id of this build. `<d>` = `with-DB 5093/0`.
- (c3r) `stray rows: not read (no --tickers given)` — this build writes no ticker.
- (e) `live-note 146/0`.
- (f) `2030:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`** (`2082`); `2084:lock released`; `2088:.env: removed`; `ls /Users/cobalt/cobalt-wt/aset-orphan-1010/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown red: A1 — E2 red (`'cd "$REPO_ROOT"' != 'uv sync --inexact'`) and mutations A, A′; B1[com.cobalt.aset] — E2 red and mutation A; B1[com.cobalt.radar] — mutation B′; B3 — mutations B (`TypeError … NoneType`) and B′ (`no-abandon` flagged); B2 — a pin on the parameter set (radar first, aset present), its own content is the list B1 reads; it was not mutated (the plist set is fixed files). B1[herdr], B1[obsidian] are green cases of the same function whose branches B, B′ break. `test_jobs_reads.py` changed in a docstring only (no assertion). No test stayed green under its mutation.
(2) Entry paths: the readers of `ops/start_aset.sh` (`grep -rn -F "start_aset" tests src`): `test_voice_config.py:211` (exports, 77 passed with `test_aset_vault.py`), `test_jobs_restarts.py:145–186` (classification; 54 passed), `com.cobalt.aset.plist:25` (B1[com.cobalt.aset]). Flag combinations of `orphan_prone`: KeepAlive absent / set, AbandonProcessGroup absent / true, program `uv` / `.sh` ending `exec uv` / `.sh` ending `exec <venv python>` — B3's five cases plus the four real plists (dict and bool KeepAlive). Not pinned: a `.sh` whose last line is not an `exec` at all (the helper returns a reason; no real KeepAlive plist has one) — `## DECISIONS` 5.
(3) Re-read at the tip: `git show 1987849b:ops/start_aset.sh` (tail `uv sync --inexact` / `exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset`), `grep -n -F "start_aset.sh:77" tests/cobalt/test_jobs_reads.py` → `100:`, `grep -n -F "uv sync --inexact" ops/start_aset.sh` → `77:`, `git log --oneline ddaae952..HEAD`, the gate log lines by `grep -n -F` (`F0: `, `F1: `, `F2`, `dev forward`, `pass 1: whole (deploy)`, `lock`).

## FOR THE CHECK
- Range `ddaae952..1987849b`: `c3da0511 wip(aset-orphan-1010): red`; `1987849b fix(aset-orphan-1010): start_aset.sh execs the venv python so launchd's pid is the python (A, B; L1, L42)`. Report commit follows.
- Per row: reds at `## E2 RED`; mutations and greens at `## E3 THE ROWS`; caller greps at `## PREFLIGHT` and self-check (2). No RUN row on this card.
- Suites: offline `4196/0` · with-DB `5093/0` (pass 1 command above) · live-note `146/0`; log `/Users/cobalt/cobalt-wt/.gate-logs/aset-orphan-1010-all-20261010-083000.log`.
- F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `908 45 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. One lock take (W): taken after a 17-minute wait from 08:30:00, released at the gate's end (`lock released`, before 09:18:16 `date`).
- RESTARTS: `RESTARTS: com.cobalt.aset` (table at `## RESTARTS`).
- X1: after row A, `ProgramArguments[0]` is `start_aset.sh`, whose last line `exec`s the venv python, so launchd's pid becomes the python; `uv sync --inexact` runs in the foreground and exits before the `exec` (a child that has ended; nothing is backgrounded). Not run live here (the deploy's).
- X2: `uv sync --help` was refused on this launch line; NOT quoted (`## DECISIONS` 1).
- X3: the audit table at `## E3 THE ROWS` row B, re-derived from the 15 plists by grep.
- The card's records as copied at PREFLIGHT.

## CONTINUE
next: none — BUILT; the desk verifies and launches the check.

## DECISIONS
1. `uv sync --help` (the card's row A "confirm `--inexact` … and quote the line") is not on the launch line's list: refused by `dontAsk`. So the claim that `uv sync --inexact` syncs the same environment `uv run` did (project, default groups, lock, extraneous packages kept) is UNPROVEN by tool output here (L35). Safe default taken: built the line exactly as the card states (L72); the check's X2 quotes `uv sync --help` / `uv run --help`.
2. The card says "16 at `d0a5fbb8`"; `ops/com.cobalt.*.plist` at `ddaae952` holds 15, and the card's own enumeration names the same 15. Safe default: audited all 15; no plist is missing from the audit.
3. `configs/cobalt/jobs.yaml:88–89` comments still cite `ops/start_aset.sh:73 (exec uv run python -m cobalt.aset)`: stale after row A (now `:77 uv sync --inexact`, then the exec). Both rows stay true (the start script syncs from both files at start). Left untouched (the card's fence: jobs.yaml not edited).
4. `tests/cobalt/test_jobs_reads.py:96` test name `test_every_resident_that_starts_through_uv_run_re_reads_the_uv_files` and its docstring's "Three residents start that way" now read loosely for aset (it starts through `uv sync`, not `uv run`). Only the `:100` citation was changed, as the row allows; the name and wording left.
5. `orphan_prone`'s "last line is not an `exec`" branch has no B3 case (B3 is the card's five; no real KeepAlive plist reaches it). Left as built; a sixth case is the check's call.
6. DevDocs: no `src/` module changed and `docs/40 - DevDocs/cobalt/` has no page for `ops/start_aset.sh`; no dated DevDocs line written. `ops/README.md:31` is the doc that changed.

## RECORDS
- `REFUSED, not needed: uv sync --help — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (named by the card, not by a hub step; recorded, `## DECISIONS` 1.)
- `grep -n -F "cd \"$REPO_ROOT\"" ops/start_aset.sh` printed nothing (a `$` in a double-quoted argument, against the hub's rule); the Read of the whole file stood in.
- One lock take (W, inside `gate.sh`); no extra take. `.env: removed, proven gone (W)`.
- The gate's proof-only printed `code: 1987849b (DIRTY: 1 path(s))`: the uncommitted report, the only dirty path.
- The card's `## RECORDS` as re-read at PREFLIGHT: approval row R685 (AUTHORIZATION row 38, APPROVED); RESTARTS expectation matched; DEPLOY PROOF and no-new-command are the desk's.
- L74 / attribution: a mid-session system reminder asked commits to also carry a `Claude-Session:` line. The hub (L74) says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only; both commits carry only that line.
- `## L74`: no block inside a tool result asked for an instruction.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: aset-orphan-1010 · tip: 1987849b | on ddaae952 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset | rows: 2 of 2 | self-check: 3 of 3 | decisions: 6 · for Dejan: 0 · tokens: 145288
