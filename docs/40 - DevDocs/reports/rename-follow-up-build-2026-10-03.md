# rename-follow-up — build report 2026-10-03

## §0 Headline
- Row O3 built: `changes()` now emits the old path of a rename/copy line as `D`, so a renamed file a resident read still derives its restart or escalates. Tip `393f3ad5` on `a09f0862`.
- Red first: the O3 test, verbatim, plus a `changes()` line-shape test. Both red on BASE, both green at the tip, both red under the undo mutation.
- Suites: offline 3739/0, with-DB 846/0 (673 + 173), live-note 146/0. `cobalt_dev` back at 0013 with F2 = F0. `.env` removed.
- RESTARTS: com.cobalt.radar. Two decisions, neither for Dejan.

## L74
- 11:29 ET (session start): a harness system reminder (not a tool result) asked commits to end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once; not acted on — commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74, BUILD-HUB).

## AUTHORIZATION
Started `date` → `Sat Oct  3 11:29:57 EDT 2026`.
| check | command | exit · output |
|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | exit 1, no output |
| card placeholders | `grep -n -E "«FIL[L]" "<card>"` | exit 1, no output |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/04-rename-follow-up-card.md"` | `caa390aa5391b6a4796c805d0f6ce9bf6d8e139a` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | no output |
| STANDING LIST R60 (2026-09-30) | `grep -n "^| R60 " cto-2026-09-30.md` | `46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C ... log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING 2026-10-02 R47 | `grep -n "^| R47 " cto-2026-10-02.md` | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C ... log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING 2026-10-02 R157 | `grep -n "^| R157 " cto-2026-10-02.md` | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week ... | HIS RULING · APPROVED |` |
| R157 committed | `git -C ... log -1 --format=%H -S"| R157 |" -- ".../cto-2026-10-02.md"` | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
Authorization holds.

## PREFLIGHT
| rule | command | exit · output |
|---|---|---|
| branch | `git status --short --branch` | `## ops/rename-follow-up-1003` + `?? "docs/40 - DevDocs/reports/rename-follow-up-build-2026-10-03.md"` (this report, written first per REPORT) |
| base | `git log --oneline -1` | `a09f0862 docs(desk): 10-03 R30-R34 set 1 deployed; refusals list; his rulings` |
| branch in main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/rename-follow-up-1003` | `a09f0862 ...` (same) |
| no diff | `git diff --stat a09f0862` | no output |
| base stat | `git show --stat a09f0862` | `docs/40 - DevDocs/reports/cto-2026-10-03-words.md | 6 ++++++` · `docs/40 - DevDocs/reports/cto-2026-10-03.md | 19 +++++++++++++++++--` · `2 files changed, 23 insertions(+), 2 deletions(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/rename-follow-up-1003/.env` | exit 1, `No such file or directory` |
| any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | exit 1, `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| symbol `changes()` | `grep -n "def changes" src/cobalt/jobs/restarts.py` | `69:def changes(git_range: str) -> list[Change]:` |
| callers | `grep -rn -F "changes(" src` | `src/cobalt/jobs/restarts.py:69:def changes(...)` · `src/cobalt/jobs/restarts.py:190:    for item in changes(git_range):` · `src/cobalt/radar/evaluate.py:1324:def formation_changes(...)` · `:1907: ... formation_changes(...)` (a different function) |
| test callers | `grep -rn -F "changes(" tests/cobalt` | no output (tests monkeypatch `restarts.changes` with a lambda) |
| fake `_git` in tests | `grep -rn -F "_git" tests/cobalt/test_jobs_restarts.py` | no output |
| O3 in READ report | `grep -n -F "O3" ".../ops-glob-check-2026-10-02.md"` | `66:FINDING O3` · `105:| O3 · own | test added ... 1 failed in 0.51s ... AssertionError: [Classification(path='ops/desk/start_aset.sh', change='R', rule='operator script; no Cobalt reader', restarts=(), escalate=False)]` · `134:- O3 · own · REJECTED. changes() (src/cobalt/jobs/restarts.py:79) keeps only the last tab field ...` |
| wc | `wc -l src/cobalt/jobs/restarts.py tests/cobalt/test_jobs_restarts.py` | `277` · `589` |
| tail of READ report | `tail -n 3 ".../ops-glob-check-2026-10-02.md"` | last line `CHECK DONE · job: ops-glob · pass: 1 · tip: 9fa18f14 · ... · open: 1 · ... ready: YES · decisions: 1 · for Dejan: 0` |
| restarts empty | `uv run cobalt jobs restarts a09f0862..HEAD` | `docs/40 - DevDocs/reports/rename-follow-up-build-2026-10-03.md	A	DOCS	-` · `RESTARTS: none` — the one row is this untracked report (HEAD range includes untracked files); no code path |
| DB | card header carries no `DB: none` | lock at W only (no with-DB red in this row) |

The card's `## RECORDS`, copied and re-read:
- "Judge answer, 10:0x ET 10-02 (R77): follow-up ...; `reports/brain-direction-2026-10-02.md` `## TOMORROW` row "rename follow-up"." Re-read: `grep -n "^| R77 " cto-2026-10-02.md` → `84:| R77 | 10:05 ET | DESK RECORD (R41): brain rules 15 ops-glob O3 ships to the follow-up list, no fix tonight; ... a changes() rename card is on the direction's TOMORROW table. | DESK RECORD |`; `grep -n -F "rename" brain-direction-2026-10-02.md` → `92:| rename follow-up | the judge's answer to ops-glob-check-2026-10-02.md O3 (10:0x ET): changes() ... also emits the OLD path of a rename or copy line, as a delete; ...| Opus only |`.
- "This job touches `src/`: it takes the lock as BUILD-HUB.md says (pass 1 with `--db-only` after card `01`). ..." Re-read: BUILD-HUB (c) carries `--db-only` (line 89).
- "Origin: desk row 2026-10-02 R77 ..." — same R77 row above.

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 643.47s (0:10:43)`; 0 failed, 0 errors.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.04s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- Note: the report's PREFLIGHT edit was written the same turn the offline run was launched (just before it); no file was written while it was in flight after that.

## E2 RED
Two tests added to `tests/cobalt/test_jobs_restarts.py` (after `test_a_resident_wrapper_script_is_not_an_operator_script`):
- `test_check_o3_a_rename_out_of_a_read_path_into_ops_desk_still_restarts_or_escalates` — the O3 test of `ops-glob-check-2026-10-02.md` `:71-78`, verbatim.
- `test_changes_emits_the_old_path_of_a_rename_or_copy_as_a_delete` — `changes()` on an `R100`, a `C075`, an `M`, an `A` and a `D` line; the old paths of R/C are `D`, the new paths keep `R`/`C`, the M/A/D lines are unchanged (the row's "every other line shape is unchanged", the negative control inside the same assertion).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py` → `2 failed, 19 passed in 13.00s`. Reds:
- `E       AssertionError: [Classification(path='ops/desk/start_aset.sh', change='R', rule='operator script; no Cobalt reader', restarts=(), escalate=False)]` at `tests/cobalt/test_jobs_restarts.py:151` — the row's reason: the old path `ops/start_aset.sh` is absent (matches O3's EXPECT).
- `E       AssertionError: assert [Change(path=..., change='M')] == [Change(path=...nge='D'), ...]` · `At index 1 diff: Change(path='docs/new.md', change='A') != Change(path='configs/cobalt/radar.yaml', change='D')` · `Right contains 2 more items, first extra item: Change(path='ops/start_aset.sh', change='D')` at `:168` — old paths absent.
No with-DB red. Commit `3506e45a wip(rename-follow-up): red — O3 rename old path absent from changes()`.

## E3 THE ROWS
Row O3 — `src/cobalt/jobs/restarts.py` `changes()` `collect()`: when `status[0]` is `R` or `C` and the line has three tab fields, `rows[parts[1]] = "D"` before the new path is recorded as before (`rows[parts[-1]] = status[0]`). Nothing else changed.
- Green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py` → `45 passed in 15.62s`.
- MUTATION 1 (undo the fix: `rows[parts[1]] = "D"` → `pass`): `2 failed, 19 passed in 12.91s`; first failing line `E   AssertionError: [Classification(path='ops/desk/start_aset.sh', change='R', rule='operator script; no Cobalt reader', restarts=(), escalate=False)]` (`:151`), and `:168` as at E2. Undone with Edit.
- MUTATION 2 (the old path keeps the R/C letter, not a delete: `rows[parts[1]] = status[0]`): `1 failed, 20 passed in 13.21s`; `At index 1 diff: Change(path='configs/cobalt/radar.yaml', change='C') != Change(path='configs/cobalt/radar.yaml', change='D')` (`:168`). The O3 test stays green under this mutation by design (it asserts the restart, not the letter); the second test pins the letter. Undone with Edit.
- `git diff --stat` after undo → ` src/cobalt/jobs/restarts.py | 4 ++++` · `1 file changed, 4 insertions(+)` (the fix only); re-run → `45 passed in 15.81s`.
- DevDocs: `docs/40 - DevDocs/cobalt/jobs/restarts.md` `## 2026-10-03 — rename-follow-up`.
- Commit `393f3ad5 fix(rename-follow-up): changes() emits the old path of a rename/copy as a delete (O3, L42)`.

## RESTARTS
`uv run cobalt jobs restarts a09f0862..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/reports/rename-follow-up-build-2026-10-03.md	A	DOCS	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No UNCLASSIFIED row. (The report row is the untracked report; HEAD ranges include untracked files.)

## W THE THREE SUITES
`<tip>` = `393f3ad5`. TREE STATE: unchanged — this build adds no with-DB test and no migration (`git log --oneline a09f0862..HEAD` → `393f3ad5 fix(...)`, `3506e45a wip(...)`; the diff touches `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, the DevDocs page).
`<FP>` used (copied whole): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`
- (a) OFFLINE, clean run with `.env` absent: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 638.02s (0:10:38)` → `<p>` = 3739 (E0 3737 + the two added tests: `test_check_o3_a_rename_out_of_a_read_path_into_ops_desk_still_restarts_or_escalates`, `test_changes_emits_the_old_path_of_a_rename_or_copy_as_a_delete`). An earlier run of (a) overlapped the lock window (see `## RECORDS`) and is not counted.
- (b) `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh rename-follow-up-1003 90` → `lock taken: rename-follow-up-1003` (exit 0, `date` 11:44:11 EDT). `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  3 11:44 /Users/cobalt/cobalt-wt/rename-follow-up-1003/.env`. `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `36 table(s) probed on cobalt_dev` · `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: 393f3ad5 (DIRTY: 1 path(s))`; the tables of 0014+ (`drc_*`, `legs`, `prediction_records`, `voice_turns`) print `-` (absent) → `cobalt_dev` at `0013`.
- (c) PASS 1, executed byte for byte (no added deselect): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py` → `673 passed, 7 skipped, 3803 deselected, 2 xfailed, 12 warnings in 121.76s (0:02:01)` → `<d1>` = 673. SKIPPED lines:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
- (c2) `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → applied `0001`…`0011`, `0013`, then `0014_radar_handicap.sql` … `0022_prediction_records.sql` in order; 7 tables `CREATED`; `content UNCHANGED on every table.`; no `CHANGED`. **dev forward: APPLIED 11:46:53 EDT**. `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed byte for byte (no addition): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones` → `173 passed, 1 deselected, 5 warnings in 231.03s (0:03:51)`; no SKIPPED line → `<d2>` = 173. This build has no with-DB test id. `<d>` = 673 + 173 = 846.
- (c3r) not run: this build's tests write no ticker to `aset_sizings` (no with-DB test added); the query has no constructed ticker to name.
- (c4) not applicable: no migration added.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022` … `0014` rollback in newest-first order; 7 tables `DROPPED`; `content UNCHANGED on every table.` `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **cobalt_dev: 0013 — F2 = F0**.
- lock (d): `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh rename-follow-up-1003` → `lock released`; `ls /Users/cobalt/cobalt-wt/rename-follow-up-1003/.env` → `No such file or directory`; `date` 11:51:24 EDT. **.env: removed, proven gone (W)**.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.17s`; skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC ... not set` (does not name `COBALT_LIVE_VAULT_ROOT`) → `<l>` = 146.

## PRE-STOP SELF-CHECK
(1) Every added test shown red: `test_check_o3_...` red at E2 (`:151` `AssertionError: [Classification(path='ops/desk/start_aset.sh', change='R', ...)]`) and under MUTATION 1; `test_changes_emits_...` red at E2 and under MUTATION 1 (`:168`) and MUTATION 2 (`Change(path='configs/cobalt/radar.yaml', change='C') != ... change='D'`). The O3 test stays green under MUTATION 2 by its design (it asserts restart/escalate, not the letter); the letter is pinned by the second test. ✔
(2) Entry paths: the only caller of `changes()` is `src/cobalt/jobs/restarts.py:194` (`for item in changes(git_range):` in `classify`; re-grep at the tip), pinned by the O3 test (classify through a faked `_git`). `changes()` feeds `collect()` only `git diff --name-status` output (three calls: the range, the worktree, `--cached`); `ls-files --others` lines go straight to `rows[path] = "A"` and never reach `collect()`. Line shapes pinned: `R100`, `C075` (three fields), `M`, `A`, `D` (two fields). ✔
(3) Re-read at the tip: `git show 393f3ad5:src/cobalt/jobs/restarts.py` (fix at `:80-83`); `grep -n -F "rows[parts[1]]" src/cobalt/jobs/restarts.py` → `82:                rows[parts[1]] = "D"`; `grep -rn -F "changes(" src` → `:69`, `:194`, and `radar/evaluate.py:1324`/`:1907` (`formation_changes`, unrelated); `grep -n -F "def test_c" tests/cobalt/test_jobs_restarts.py` → `:144`, `:154`; `git log --oneline a09f0862..HEAD` → the two commits. (PREFLIGHT's `:190` for the caller is the BASE line; at the tip it is `:194`, the fix added four lines above it.) ✔

## FOR THE CHECK
- Range `a09f0862..393f3ad5`: `3506e45a wip(rename-follow-up): red — O3 rename old path absent from changes()` · `393f3ad5 fix(rename-follow-up): changes() emits the old path of a rename/copy as a delete (O3, L42)`.
- Row O3: reds, mutations and greens under `## E2 RED` and `## E3 THE ROWS` (quoted). Final green `45 passed in 15.81s` (`test_jobs_restarts.py` + `test_jobs_reads.py`).
- Caller grep: `src/cobalt/jobs/restarts.py:194` only (PREFLIGHT, re-run at tip).
- RUN rows: none on this card.
- Suites: offline `3739 passed, 745 skipped, 1 xfailed`; with-DB pass 1 `673 passed, 7 skipped, 3803 deselected, 2 xfailed`, pass 2 `173 passed, 1 deselected`; live-note `146 passed, 1 skipped` (commands under `## W`).
- `<F0>` `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` = `<F0>`. Lock taken 11:44:11 EDT, released 11:51:24 EDT.
- RESTARTS table: under `## RESTARTS`; `RESTARTS: com.cobalt.radar`.
- For CHECK ASK X1 (not written here; the card gives it to the check): `classify()` handles each `Change` independently, so the old path (`D`) and the new path are each classified by their own class.
- For CHECK ASK X2: `collect()` is fed only `--name-status` output; `--name-only`/porcelain is not fed anywhere in `restarts.py`. The R/C branch requires three tab fields, so a two-field line is unchanged.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: CLOSE (report commit)

## DECISIONS
- DECISION 1 (card wording): the row says the old path is emitted "beside the new path's ADD/MODIFY" and "every other line shape is unchanged". Default taken: the new path keeps the letter it had before (`R`/`C`, i.e. unchanged), and only the old path is added as `D`. No rule in `classify()` reads `R` or `C` (only `item.change == "A"` for a new one-shot plist), so the derivation is the same either way. Not FOR DEJAN.
- DECISION 2 (row on `cobalt_dev`): `system.cobalt_redactions` read 252 rows at the `--proof-only` (11:44) and 253 at the forward's "before" probe (11:46), after pass 1 ran (and while the overlapping offline run was in flight, see `## RECORDS`). F2 = F0 compares schema, not rows; the one added row is in a system table, no ticker. Default taken: nothing deleted (no string allows it); the desk decides whether it matters. Not FOR DEJAN.

## RECORDS
- The first run of W (a) (`bl5vnaqgv`, started 11:43 before the lock take) overlapped the lock window: `.env` was present 11:44–11:51 while it ran. Result `3778 passed, 706 skipped, 1 xfailed, 37 warnings in 669.14s` — 39 fewer skips than E0 + 2 new tests, i.e. some with-DB tests ran against `cobalt_dev` during it. It is not counted; (a) was re-run clean after the release (`3739 passed, 745 skipped, 1 xfailed`). One lock take only.
- `.env: removed, proven gone (W)`.
- The L74 line (harness reminder asking for a `Claude-Session:` trailer) — see `## L74`; not acted on.
- The card's records, as re-read at PREFLIGHT: R77 desk record (`cto-2026-10-02.md:84`), the TOMORROW row (`brain-direction-2026-10-02.md:92`), pass 1 `--db-only` (BUILD-HUB `:89`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: rename-follow-up · tip: 393f3ad5 | on a09f0862 | migration: none | offline 3739/0 | with-DB 846/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0
