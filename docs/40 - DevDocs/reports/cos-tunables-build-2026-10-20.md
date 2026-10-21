# cos-tunables — build report 2026-10-20 (band-routed, BAND: MID)

Card: `docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md` · JOB `cos-tunables` · BRANCH `ops/cos-tunables` · BASE `e69d5ab8` · builder `grok-4.7` (BAND MID, SHADOW-HUB `## BUILDERS` / BAND ROUTING) · gate seat `cos-tunables-gate` (Opus 5.5). A routed card: no `SHADOW OF:`; stop line `BUILT ·` (SHADOW-HUB `:28`, `:57`).

## §0 Headline
Grok 4.7 built card 933's three rows under the Opus gate seat. The two cos tunables are set to the brain's DEFAULTS, 10 and 30. The `com.cobalt.cos` row is `enabled: true`. The `cos` and `hitl` probes answer OWED-unknown while the owed file lists cos. Tip `17f45d80`.
The gate's first run was red on one test outside the card's files: `test_sheet_daymode_probe.py` left `cos` and `hitl` unstubbed. One S2 pass fixed it (SCOPE). The second gate run was green: offline 4899/0, with-DB 5871/0, live-note 148/0, `cobalt_dev` back at 0013 with F2 = F0.
Three DECISIONS: no mutation runs (the seat cannot edit tests or src), the unreadable-owed-file path has no test, and the SCOPE test file. None is for Dejan.

## L74
The session's harness reminders (system turns, not tool results) asked commits to end with a `Claude-Session:` line. BUILD-HUB L74: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Recorded once; not acted on. 17:54 EDT.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "<card>"` (17:54):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · fa9fdbe56453a4df5ddaa0360f085b2fc71faf2d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/933-cos-tunables-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"`:
```
clock · date · 0 · Tue Oct 20 17:54:05 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-tunables
head · git log --oneline -1 · 0 · e69d5ab8 docs(desk): R2211 933 amend drafted, preflight r2 941
diff · git diff --stat e69d5ab8 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-tunables · 0 · e69d5ab8 docs(desk): R2211 933 amend drafted, preflight r2 941
env here · ls /Users/cobalt/cobalt-wt/cos-tunables/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat e69d5ab8` → `docs(desk): R2211 933 amend drafted, preflight r2 941`; 4 files, 35 insertions, 6 deletions, all under `docs/40 - DevDocs/`.
- `uv run cobalt jobs restarts e69d5ab8..HEAD` → `path	change	rule	restart` / `RESTARTS: none` (empty range).
- THE CARD'S SYMBOLS (each its own grep, hits):
  - `tunables.yaml`: `1008:  - key: cos.poll_interval_s` · `1017:  - key: cos.session_rotate_at` · `1026:  - key: hitl.request_ttl_min` · `1038:  - key: hitl.page_base_url`; `value: null` at `:1009` and `:1027` (Read).
  - `src/cobalt/cos/session.py`: `51:POLL_KEY = "cos.poll_interval_s"` · `72:class CosConfigError(RuntimeError):` · `76:def tunable_int(key: str) -> int:`; `:81-84` the null / bool / non-int / <=0 raises (Read).
  - `src/cobalt/cos/run.py`: `95:    from .session import POLL_KEY, CosSession, tunable_int` · `99:    poll_s = tunable_int(POLL_KEY)`.
  - `src/cobalt/hitl/actions.py`: `33:TTL_KEY = "hitl.request_ttl_min"` · `62:def request_ttl_min() -> int:`.
  - `bootstrap_owed`: `src/cobalt/jobs/watchdog.py:63:def bootstrap_owed(path: Optional[Path] = None) -> frozenset[str]:` · `src/cobalt/jobs/watchdog.py:437:                    owed = bootstrap_owed()` · `src/cobalt/smoke/checks.py:433:                from cobalt.jobs.watchdog import bootstrap_owed` · `src/cobalt/smoke/checks.py:435:                owed = bootstrap_owed()`. `BootstrapOwedError` `watchdog.py:59`; `BOOTSTRAP_OWED_PATH` `:55`; disabled skip `if not spec.enabled:` `:387`; OWED finding `:441-446` (Read).
  - `checks.py` `_launchctl` `:415-451`: FAIL `:444-447`, PASS with `OWED (deferred bootstrap): …` `:448-451` (Read).
  - `probes.py`: `COS_LABEL` `:126`, `def cos(` `:135`, the no-heartbeat red `:155-156`, `def hitl(` `:167`, `store.probe_counts()` `:179` (Read).
  - `runner.py:148-149`: `# F20 C4b (X9: this is the call site): unknown, never red, while` / `# com.cobalt.cos ships `enabled: false`.` (Read).
  - `jobs.yaml`: `- label: com.cobalt.cos` `:206`; `grep -rn -F "enabled: false" configs/cobalt/jobs.yaml` → `configs/cobalt/jobs.yaml:214:    enabled: false` (one line; DEPLOY PROOF marker 1 before = 1).
  - `ls ops/com.cobalt.cos.plist` → `ops/com.cobalt.cos.plist`.
  - Callers: `grep -rn -F "probes.cos(" src tests` → `tests/cobalt/test_cos_probes.py:29`, `:31`, `:33`, `:40`; `grep -rn -F "probes.hitl(" src tests` → `tests/cobalt/test_cos_probes.py:40`, `:49`, `:51`, `:55`; the runner calls `probe_mod.cos(ts)` / `probe_mod.hitl(ts)` at `runner.py:150-151`.
  - Tests: `test_cos_offline.py:270-294` (`test_each_cos_tunable_is_read_loud` `:272`, `test_the_shipped_cos_rows` `:287`, the `None` pin `:294`); `test_cos_registry.py:21` `test_the_row_is_a_disabled_self_resident`, `:28` `assert spec.enabled is False`; `test_cos_probes.py:26`, `:37`, `:45`; `test_smoke.py:1578-1603` (`_k18`, `OWED_LABEL`, `_Spec`).
- `wc -l`: `tunables.yaml` 1172 · `jobs.yaml` 472 · `probes.py` 934 · `runner.py` 570 · `test_cos_offline.py` 583 · `test_cos_registry.py` 48 · `test_cos_probes.py` 71.
- `tail -n 3 "docs/40 - DevDocs/reports/cos-bootstrap-decisions-2026-10-20.md"` → last line: `RECORDS: cos bootstrap 929 — no listener overlap (F-14 kept, run.py:44-57); … tunables card sets jobs.yaml:214 enabled: true; … MIGRATIONS none (additive CREATE IF NOT EXISTS) — brain 9b07db5a 2026-10-20`.
- DevDocs pages of the changed modules: `docs/40 - DevDocs/cobalt/heartbeat/probes.md`, `docs/40 - DevDocs/cobalt/heartbeat/runner.md` (Glob).
- The card's `## RECORDS`, copied: drafter `draft-cos-tunables` (prompt 932), BASE read `bd7bc0c9` at draft (the card's BASE line is now `e69d5ab8`); DEPLOYS BEFORE card 929; cos stays unloaded and OWED; K18 FAIL fires on `not_loaded` or `loaded_disabled` (re-read above, `checks.py:444-447`); the watchdog skip `watchdog.py:387-396` (re-read); values 10 and 30 are the brain's DEFAULTS; `jobs.yaml:217` `timeout_s: 1200` > 900 + 10 (re-read `:217`); RESTARTS: `tunables.yaml` read by aset, radar, cos — the builder's `cobalt jobs restarts` line is the record; MIGRATIONS none.
- RULINGS: `2026-10-18 R1863` (AUTHORIZED row above).
- SHADOW card checks: the card carries no `SHADOW OF:` (a routed card, BAND: MID → `grok-4.7`); no original build report, so no admitted exceptions; the fence is the rows' files plus the two DevDocs pages (BUILD-HUB E3's dated line).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `e69d5ab8` → `4897 passed, 878 skipped, 4 xfailed, 36 warnings in 765.10s (0:12:45)`, exit 0; the skips are `Postgres env settings not available`, `reaches cobalt_dev (lock-relief G1)` and `COBALT_LIVE_VAULT_ROOT not set` (the live-note run below covers those).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.49s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Builder pass T (Grok) wrote the three test files; seat commit `e3f05089 wip(cos-tunables): red`. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_offline.py tests/cobalt/test_cos_registry.py tests/cobalt/test_cos_probes.py` → `3 failed, 30 passed in 2.21s`. Each red, first line:
- T1 `test_the_shipped_cos_rows` → `AssertionError: ('cos.poll_interval_s', None)` (the row's reason: `value` is `None`).
- T2 `test_k18_reads_cos_as_owed_while_unloaded` → `AssertionError: assert 'OWED (deferred bootstrap): com.cobalt.cos' in '22 registry label(s) match launchd'` (the row's reason: disabled, so no OWED clause). Its CONTROL (owed file empty → FAIL) sits after the red assert and is not reached on BASE; it runs at E3.
- P1 `test_cos_probe_is_unknown_green_while_owed` → `AssertionError: assert (False is True)` on `Probe(name='cos', ok=False, detail='no heartbeat — the CoS loop has never stamped')` (the row's reason). Its CONTROL (nothing owed → cos `ok=False` "no heartbeat", hitl raises) precedes the red assert in the test and PASSED on BASE.
- The changed pins `test_disabled_row_is_unknown`, `test_the_row_is_a_self_resident`, and the two monkeypatched tests: green on BASE (the card: "RED on BASE: none" for the P1 pin).

## E3 THE ROWS
Builder pass S (Grok) wrote the six row files; seat commit `2a8b0315 feat(cos-tunables): rows`. Diff stat:
```
 configs/cobalt/jobs.yaml                     | 16 ++++++++--------
 configs/cobalt/taxonomy/tunables.yaml        |  4 ++--
 docs/40 - DevDocs/cobalt/heartbeat/probes.md |  3 +++
 docs/40 - DevDocs/cobalt/heartbeat/runner.md |  3 +++
 src/cobalt/heartbeat/probes.py               | 14 +++++++++++---
 src/cobalt/heartbeat/runner.py               |  2 +-
 6 files changed, 28 insertions(+), 14 deletions(-)
```
- Row tests: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_offline.py tests/cobalt/test_cos_registry.py tests/cobalt/test_cos_probes.py` → `33 passed in 2.15s` (the three E2 reds green; T2's CONTROL, owed file empty → FAIL with `com.cobalt.cos` in `enabled but not loaded`, now reached and green).
- The card's adjacent suites: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py tests/cobalt/test_smoke.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_registries.py tests/cobalt/test_heartbeat*.py` → `259 passed, 19 skipped in 195.55s (0:03:15)`; every skip `Postgres env settings not available` (with-DB, the gate's).
- DEPLOY PROOF markers on the worktree: `grep -c -F "enabled: false" configs/cobalt/jobs.yaml` → `0`; `grep -c -F "DEFAULT (brain; his word may change it)" configs/cobalt/taxonomy/tunables.yaml` → `2`.
- SCOPE: every path in the two commits is a row's file or the two DevDocs pages of E3; no `SCOPE` record.
- THE MUTATIONS: not made. The seat never edits `src/` or `tests/` (SHADOW-HUB `## RULES OF THE SEAT`) and Grok runs no command. The mutation evidence is each new test's red on BASE (E2: the fix absent = the fix undone) and T2's control (FAIL with the owed file empty, green at the rows). See `## PRE-STOP SELF-CHECK` (1) and `## DECISIONS`.

## RESTARTS
`uv run cobalt jobs restarts e69d5ab8..HEAD` reads the working tree too and listed the untracked `SHADOW-INSTRUCTIONS.md` as `UNCLASSIFIED` (exit 1; it is never committed, SHADOW-HUB step 4). On the committed range, tip named:
`uv run cobalt jobs restarts e69d5ab8..2a8b0315` →
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/40 - DevDocs/cobalt/heartbeat/probes.md	M	DOCS	-
docs/40 - DevDocs/cobalt/heartbeat/runner.md	M	DOCS	-
src/cobalt/heartbeat/probes.py	M	static import reach	com.cobalt.radar
src/cobalt/heartbeat/runner.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_probes.py	M	test/documentation; no resident	-
tests/cobalt/test_cos_registry.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No UNCLASSIFIED committed path. The derived line names `com.cobalt.cos` beside the header's `com.cobalt.aset com.cobalt.radar`; the card's RECORDS: the derived line is the record, and the hub records cos `not loaded — skipped` (card 869).

## W THE THREE SUITES
### W run 1 — tip `2a8b0315` (18:20)
`sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-tunables all --deploy` → exit 1, verdict lines:
```
RED (exit 1): 1 failed, 4898 passed, 878 skipped, 4 xfailed, 36 warnings in 759.86s (0:12:39)
1 failed, 4898 passed, 878 skipped, 4 xfailed, 36 warnings in 759.86s (0:12:39)
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261020-182034.log
```
(a) OFFLINE red; the gate stopped at (a), so no lock was taken (`ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory`). The red (log `:87-172`): `TestItIsWiredIntoTheBeat.test_the_runner_asks_it_right_after_sheet_http` (`tests/cobalt/test_sheet_daymode_probe.py:187` `runner.take_beat()` → `runner.py:150` `probe_mod.cos(ts)` → `probes.py:158` `job_store.get(COS_LABEL)` → `cobalt.db.DbConfigError: Missing Postgres settings for the APP credential: …`). The cause: the test stubs every probe but `cos` and `hitl`. With T2 the row is enabled, and the worktree holds no gitignored `data/deploy/bootstrap-owed.json`, so P1's owed answer does not apply and the real store is built. The rows cause this red, so it is the model's red, not the harness's. The card's files did not name the test. → pass S2 1.

Pass S2 1 (Grok, 18:34:05–18:34:35) wrote `tests/cobalt/test_sheet_daymode_probe.py` only. `git diff --stat` → `tests/cobalt/test_sheet_daymode_probe.py | 4 ++++` / `1 file changed, 4 insertions(+)`: it adds `"cos", "hitl"` to the test's stub tuple, with a 3-line comment. The seat recorded the path as `SCOPE` (outside the rows' files; named for S2 in SHADOW-INSTRUCTIONS.md) and did not revert it. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_sheet_daymode_probe.py tests/cobalt/test_cos_probes.py` → `15 passed in 5.19s`. Commit `17f45d80 fix(cos-tunables): pass S2 1`. RESTARTS again, `uv run cobalt jobs restarts e69d5ab8..17f45d80` → the run-1 table plus `tests/cobalt/test_sheet_daymode_probe.py	M	test/documentation; no resident	-`; `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.

### W run 2 — tip `17f45d80` (18:34–19:07)
`sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-tunables all --deploy` → exit 0, verdict lines whole:
```
tests/ops: skipped (no ops paths)
offline 4899/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5871/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261020-183449.log
```
- (a) `offline 4899/0`; this build adds `test_k18_reads_cos_as_owed_while_unloaded` (`test_cos_registry.py`) and `test_cos_probe_is_unknown_green_while_owed` (`test_cos_probes.py`) (4897 at E0 + 2). `tests/ops: skipped (no ops paths)`.
- (b) `lock taken: cos-tunables` (log `:963`), `lock: waited 0 min`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → only `/Users/cobalt/cobalt-wt/cos-tunables/.env` (`:968`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:974`); `LEVEL 0013`.
- (c) pass 1 (`grep -n -F "pass 1: whole (deploy)"` → `:1030`), the executed command, log `:1032`: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`. Every SKIPPED line the gate printed is quoted above; `grep -n -F "OUTSIDE the allowed set"` on the log → no hit.
- (c2) `dev forward: APPLIED 19:02:54` (`:1202`); `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1286`). (c3) pass 2, log `:1288`. (c3r) `stray rows: not read (no --tickers given)`: this build writes no ticker.
- (e) `live-note 148/0`. (f) rollback `--down-to 0013` (`:2186`); `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2256`) = F0; `cobalt_dev: 0013 — F2 = F0`; `lock released` (`:2312`); `ls /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory` (`:2315`). Re-checked by the seat at 19:07: `ls -la /Users/cobalt/cobalt-wt/cos-tunables/.env` → `No such file or directory`.
- No migration added (`migration: none`); the forward and back applied the existing migrations above 0013 only.

## PRE-STOP SELF-CHECK
(1) PARTLY BACKED. The three new reds were each shown red on BASE for their row's reason (E2). T2's control (owed file empty → FAIL) is green at the rows (E3), and P1's control passed on BASE (E2). No Edit-tool mutation was made: the seat never edits `src/` or `tests/` (SHADOW-HUB), and Grok runs no command. The changed pins (`test_the_row_is_a_self_resident`, `test_disabled_row_is_unknown`, the two `monkeypatch`ed probe tests, the S2 stub) were never shown red against a mutation. Gap → DECISION 1.
(2) PARTLY BACKED. Callers of `probes.cos` / `probes.hitl`: `runner.py:150-151` (pinned by `test_cos_probes.py::test_the_runner_calls_both` and the S2-stubbed `test_sheet_daymode_probe.py` test) and the tests at `test_cos_probes.py` (PREFLIGHT greps). The OWED branch is pinned by `test_cos_probe_is_unknown_green_while_owed`, the not-owed branch by its control and by `test_dead_session_is_red`, and the disabled branch by `test_disabled_row_is_unknown`. Not pinned: the unreadable owed file path (`BootstrapOwedError` raised through `probes.cos` / `probes.hitl`, P1's "it is not swallowed"). Gap → DECISION 2.
(3) BACKED. Re-run at the tip `17f45d80`: `grep -n -F "DEFAULT (brain; his word may change it)" configs/cobalt/taxonomy/tunables.yaml` → `1009:    value: 10  # DEFAULT …`, `1027:    value: 30  # DEFAULT …`; `grep -n -F "enabled: true" configs/cobalt/jobs.yaml` → `:214` among `171, 197, 214, 400`; `grep -c -F "enabled: false" configs/cobalt/jobs.yaml` → `0`; `grep -n -F "watchdog.bootstrap_owed()" src/cobalt/heartbeat/probes.py` → `146`, `181`; `git log --oneline e69d5ab8..HEAD` and `git diff --name-only --no-renames e69d5ab8` (FOR THE CHECK).

## FOR THE CHECK
- Range `e69d5ab8..17f45d80`: `e3f05089 wip(cos-tunables): red` · `2a8b0315 feat(cos-tunables): rows` · `17f45d80 fix(cos-tunables): pass S2 1`.
- `git diff --name-only --no-renames e69d5ab8` → `configs/cobalt/jobs.yaml`, `configs/cobalt/taxonomy/tunables.yaml`, `docs/40 - DevDocs/cobalt/heartbeat/probes.md`, `docs/40 - DevDocs/cobalt/heartbeat/runner.md`, `src/cobalt/heartbeat/probes.py`, `src/cobalt/heartbeat/runner.py`, `tests/cobalt/test_cos_offline.py`, `tests/cobalt/test_cos_probes.py`, `tests/cobalt/test_cos_registry.py`, `tests/cobalt/test_sheet_daymode_probe.py` (SCOPE: outside the card's rows, pass S2 1).
- Per row: T1 red `AssertionError: ('cos.poll_interval_s', None)` → green; T2 red `… 'OWED (deferred bootstrap): com.cobalt.cos' in '22 registry label(s) match launchd'` → green, its control green; P1 red `Probe(name='cos', ok=False, detail='no heartbeat — the CoS loop has never stamped')` → green, its control green on BASE and after. No mutation runs (DECISION 1).
- Suites: W run 2 above (offline 4899/0, with-DB 5871/0, live-note 148/0), commands in the log `/Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261020-183449.log`; W run 1's red log `/Users/cobalt/cobalt-wt/.gate-logs/cos-tunables-all-20261020-182034.log`.
- F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 = F0. The lock was taken and released inside gate run 2 (18:34 start, 19:07 end, `lock: waited 0 min`). Run 1 took no lock.
- RESTARTS: the table under `## RESTARTS` (`com.cobalt.aset com.cobalt.cos com.cobalt.radar`).
- The card's X2 / X3, as far as this build's tests reach: K18 with cos listed is PASS with the OWED clause, and with cos not listed it FAILs (`test_k18_reads_cos_as_owed_while_unloaded`); `probes.cos` with cos listed is OWED-unknown, and with cos not listed it is red "no heartbeat" (`test_cos_probe_is_unknown_green_while_owed`); `probes.hitl` with cos not listed reaches the store. The sweep's OWED path (`watchdog.py:437-449`) is unchanged code and has no new test here.
- No original build: a routed card, no admitted exceptions.

## PASSES
Builder `grok-4.7`, the row's command filled (`grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/cos-tunables/**)" -p "<pass prompt>"`), each after `cd /Users/cobalt/cobalt-wt/cos-tunables`, `run_in_background`, timeout 2700000. Tokens: UNKNOWN (Grok prints none, L70).

| pass | env check (`ls -la …/cos-tunables/.env`) | prompt clause | wall (`date`) | diff stat | commit |
|---|---|---|---|---|---|
| T | `No such file or directory` | `Pass T: tests only under tests/.` | 18:09:54 → 18:14:39 (4.8 min) | 3 files, +126 −15 (`test_cos_offline.py` 4, `test_cos_probes.py` 55, `test_cos_registry.py` 82) | `e3f05089 wip(cos-tunables): red` |
| S | `No such file or directory` | `Pass S: the rows.` | 18:14:59 → 18:16:23 (1.4 min) | 6 files, +28 −14 | `2a8b0315 feat(cos-tunables): rows` |
| S2 1 | `No such file or directory` | `Pass S2: fix the failing lines quoted under PASS S2.` | 18:34:05 → 18:34:35 (0.5 min) | 1 file, +4 | `17f45d80 fix(cos-tunables): pass S2 1` |

Each prompt read: `You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass <X>: <clause> Write only the rows' files. Run no command. Reply with the list of files you wrote.` Grok's replies listed exactly the files in each diff stat. Suites at first run (W run 1): red (1 failed). Re-passes used: 1 of 2. Builder wall in total: 6.7 min. The seat's wall from AUTHORIZATION (17:54) to the stop line (19:08): 74 min.

## CONTINUE
next: none — CLOSE done; the desk verifies and launches the check.

## DECISIONS
1. DECISION 1 (self-check 1): no Edit-tool mutations were made. The seat cannot edit `src/`/`tests/`, and Grok runs no command. The changed pins (`test_the_row_is_a_self_resident`, `test_disabled_row_is_unknown`, the `monkeypatch`ed `test_dead_session_is_red` / `test_pending_past_ttl_and_failed_execution_are_red`, and the S2 stub) were never shown red against a mutation. Safe default taken: the E2 reds on BASE stand as the mutation evidence for the three new tests; the check (CHECK-HUB, L67) runs the mutations.
2. DECISION 2 (self-check 2): P1's "an unreadable owed file raises (`BootstrapOwedError`, L1): it is not swallowed" has no test. `probes.cos` / `probes.hitl` call `watchdog.bootstrap_owed()` uncaught (`probes.py:146`, `:181`), so the code meets it, but nothing pins it. Safe default taken: left for the check; no fix in this build (the card names no such test).
3. DECISION 3 (SCOPE): `tests/cobalt/test_sheet_daymode_probe.py` sits outside the card's rows and was changed in pass S2 1 (`"cos", "hitl"` added to the stubbed probes). The card's T2 enables the row, and in a checkout without the gitignored owed file the unstubbed `probes.cos` reached Postgres (W run 1 red). The card's files did not foresee this test. Safe default taken: the 4-line test stub, recorded SCOPE, not reverted (SHADOW-HUB `## RULES OF THE SEAT`); the check judges it.

## RECORDS
- L74: the harness reminders asked for a `Claude-Session:` commit line; not acted on (`## L74`). Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- `uv run cobalt jobs restarts e69d5ab8..HEAD` counts untracked working-tree files and named the never-committed `SHADOW-INSTRUCTIONS.md` (and this report) in the table, `UNCLASSIFIED` → exit 1. The committed range with the tip named (`e69d5ab8..2a8b0315`, then `e69d5ab8..17f45d80`) reads committed paths only and is the record. For the desk: on a shadow or routed seat the `..HEAD` form trips on the instructions file (R1863: tool polish, one question).
- RESTARTS derived `com.cobalt.aset com.cobalt.cos com.cobalt.radar` vs the header `com.cobalt.aset com.cobalt.radar`: the card's RECORDS make the derived line the record, with cos skipped by the hub as not loaded (card 869).
- W ran twice (run 1 red at (a), no lock taken; run 2 green). One lock take in all, inside gate run 2.
- `.env`: removed, proven gone (W run 2 (f), and the seat's `ls -la` at 19:07).
- The card's records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- One untracked file at the stop: `SHADOW-INSTRUCTIONS.md` (the launcher's exception, SHADOW-HUB step 4).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cos-tunables · tip: 17f45d80 | on e69d5ab8 | migration: none | offline 4899/0 | with-DB 5871/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 3 of 3 | self-check: 1 of 3 | decisions: 3 · for Dejan: 0 · tokens: 180196
