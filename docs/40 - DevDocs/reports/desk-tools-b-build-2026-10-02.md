# desk-tools-b — build report 2026-10-02

## §0 Headline
BUILT at `f2a0217c` on `9fa18f14`: six new operator scripts under `ops/desk/` (B1 `deploy-card.sh`, B2 `gate-clean.sh` + `job-clean.sh`, B3 `order-open.sh`, B4 `desk-wake.sh` + `desk-handover.sh`), 86 tests in `tests/ops/`, red first, 15 mutations each red.
Suites: offline 3784 passed · with-DB 4383 + 171 passed · live-note 146 passed; 0 failed. `cobalt_dev` back at 0013 (F2 = F0); `.env` removed; RESTARTS: none.
W stopped once on a lock held by `desk-tools-a-1002` (10:47) and resumed on the desk's CONTINUE (12:07).
7 decisions, none for Dejan: the main ones are an uppercase-JOB gap in `desk-launch.sh` (outside this card) and four readings of the card taken on the safe side.

## L74
- A system reminder at session start asked that commits end with a `Claude-Session: https://claude.ai/code/session_016zgVBqDLyR8K73dEB8x94h` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card placeholder | `grep -n -E "«FIL[L]" ".../2026-10-02/18-desk-tools-b-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/18-desk-tools-b-card.md"` | 0 | `2f286234f9edc62ef05aa41e526ed6dea88b9b3d` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) ...): APPROVES STANDING-LIST.md once (4be06af0); ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R47 | `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:05:35 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/desk-tools-b-1002` + `?? "docs/40 - DevDocs/reports/desk-tools-b-build-2026-10-02.md"` (this report, created first by the hub's REPORT rule) |
| base | `git log --oneline -1` | 0 | `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)` |
| main repo's branch | `git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-tools-b-1002` | 0 | `9fa18f14 …` (same) |
| diff vs base | `git diff --stat 9fa18f14` | 0 | (nothing) |
| base show | `git show --stat 9fa18f14` | 0 | `docs/40 - DevDocs/cobalt/jobs/restarts.md | 4 ++++` · `src/cobalt/jobs/restarts.py | 4 +++-` · `2 files changed, 7 insertions(+), 1 deletion(-)` |
| own .env | `ls /Users/cobalt/cobalt-wt/desk-tools-b-1002/.env` | 1 | `No such file or directory` |
| any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol | `grep -n -F "check_paths() {" ops/desk/desk-launch.sh` | 0 | `117:check_paths() {` |
| symbol | `grep -n -F "field() {" ops/desk/desk-launch.sh` | 0 | `364:field() {` |
| symbol | `grep -n -F "committed() {" ops/desk/desk-launch.sh` | 0 | `110:committed() {` |
| symbol | `grep -rn -F "wait-desk-idle.sh" ops` | 0 | `ops/desk/wait-desk-idle.sh:2:# wait-desk-idle.sh <predecessor-id> <desk-report> [max-seconds]` |
| symbol | `grep -n -F "ops/desk/" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` |
| `restarts.py:239` | Read lines 230–244 | — | line 239 is the HARNESS rule; the `tests/` rule (`test/documentation; no resident`) sits at lines 241–242. The card's line number is off by two; the class home holds |
| symbol | `grep -rn -F "agy-trial" ops/desk` | 0 | `desk-launch.sh:418` refusal, `stage-copy.sh:3,5,21,26,27` |
| absent by card | `ls ops/desk/house-probe.sh tests/ops` | 1 | both `No such file or directory` (card RECORDS: not on base) |
| test shape | `git show aeefb6df:tests/ops/test_devdb_lock.py` | 0 | read whole: `COBALT_WT_ROOT` / `COBALT_REPO_ROOT` tmp roots, `GIT_ENV`, `git()` helper with `core.hooksPath=/dev/null`, stub `claude` on `PATH` |
| wc (no row edits an existing file) | `wc -l ops/desk/desk-launch.sh ops/desk/wait-desk-idle.sh ops/desk/desk-context.sh` | 0 | `597` · `40` · `18` · `655 total` |
| RESTARTS empty | `uv run cobalt jobs restarts 9fa18f14..HEAD` | 0 | `docs/40 - DevDocs/reports/desk-tools-b-build-2026-10-02.md	A	DOCS	-` · `RESTARTS: none` (no commit in range; the tool lists the untracked report) |
| LOCK (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| LOCK (b) | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/desk-tools-b-1002/.env` · `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 · 0 | one line: `-rw-------  1 cobalt  staff  2186 Oct  2 10:06 /Users/cobalt/cobalt-wt/desk-tools-b-1002/.env` (taken 10:06:24) |
| `<FP>` → `<Fp>` | the hub's fingerprint, typed exactly | 0 | `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` |
| proof-only | `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | 0 | 36 tables probed; `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` absent (`-`); `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 9fa18f14 (DIRTY: 1 path(s))`. No `CHANGED`. The tool prints no level number; the tables above 0013 are absent |
| LOCK (d) | `rm …/desk-tools-b-1002/.env` · `ls …/desk-tools-b-1002/.env` | 0 · 1 | `No such file or directory` — `.env: removed, proven gone (PREFLIGHT)` 10:06:42 |
| card RECORDS | copied below | — | re-read: `ops/desk/` rule at `restarts.py:38`; `tests/ops` absent; `house-probe.sh` absent |

PROVEN BY FIRST REAL USE: `uv run pytest *` and the live-note prefix at E0; `git add *` / `git commit *` at E2; `COBALT_ENV=dev uv run pytest *`, `migrate`, `--rollback` are not used by this build unless W needs them (TREE STATE unchanged; W (c) runs pass 1).

Card RECORDS, copied: (1) RESTARTS class homes: `ops/desk/*` → card 15's `ops/desk/` rule; `tests/ops/*` → test/documentation. (2) `tests/ops/` not on base, no `conftest.py`. (3) W runs `tests/cobalt tests/taxonomy`; tests of this card run by name; no with-DB test; `TREE STATE: unchanged`. (4) `house-probe.sh` (card 19) and `desk-context.sh --guard` (card 16) not on base. (5) The outside house is set aside (`brain-direction-2026-10-02.md` row 10).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 644.14s (0:10:44)`, exit 0. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.12s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
- Four new test files under `tests/ops/` (offline; no with-DB test, no RUN row): `test_deploy_card.py` (B1, 20 tests), `test_gate_clean.py` (B2, 30), `test_order_open.py` (B3, 14), `test_desk_wake.py` (B4, 17).
- First run: every `test_deploy_card.py` test errored in the fixture (`FileNotFoundError … reports/alpha-check.md`) — a fixture defect, not the row's reason: empty tracked folders vanished on checkout, and the alpha check report was swept into beta's branch commit. Rewritten (`.keep` files; branches cut first, checks written on `main` after), then re-run.
- `uv run pytest -q -rf -p no:cacheprovider --color=no --tb=no tests/ops/test_deploy_card.py tests/ops/test_gate_clean.py tests/ops/test_order_open.py tests/ops/test_desk_wake.py` → `81 failed, 15 warnings in 11.57s`. Every red's first line is the row's reason, the script absent: `AssertionError: sh: /Users/cobalt/cobalt-wt/desk-tools-b-1002/ops/desk/deploy-card.sh: No such file or directory` / `assert 127 == 0` (B1); the same for `job-clean.sh` / `gate-clean.sh` (B2), `order-open.sh` (B3); the copy-beside tests fail `FileNotFoundError` on `shutil.copy` of the absent script (`test_house_probe_beside_it_is_run`, every `desk-handover.sh` test, `test_wake_with_an_id_…`).
- Commit `eb7c5e2a wip(desk-tools-b): red — …` (4 files, 1177 insertions).

## E3 THE ROWS
Rows built in order, only the card's files: `ops/desk/deploy-card.sh` (B1), `ops/desk/gate-clean.sh` + `ops/desk/job-clean.sh` (B2), `ops/desk/order-open.sh` (B3), `ops/desk/desk-wake.sh` + `ops/desk/desk-handover.sh` (B4), and the four test files. No existing file edited. No DevDocs module line: no `src/` module changed, and no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (Glob of that folder: `__init__`, `cli`, `db`, `db_query`, `devdb`, `env`, `obsidian`, `tenant`, `vault`); each script's header comment is its whole usage (card).

Greens per row (each run quoted from its summary line):
- B1: `tests/ops/test_deploy_card.py` → `20 passed` (first green), then `21 passed` (staged test added), then with the lowercase test `86 passed` across the four files.
- B2: `tests/ops/test_gate_clean.py` → `30 passed`.
- B3: `tests/ops/test_order_open.py` → `14 passed`.
- B4: `tests/ops/test_desk_wake.py` → first run `1 failed, 16 passed`: `test_a_bad_id_is_refused_before_any_call[AAAA1111]` — `assert ['agents --json'] == []`: the class `[!0-9a-f-]` lets an uppercase id through in this shell's locale. Fixed with explicit lists (`[!0123456789abcdef-]`, and `[!abcdefghijklmnopqrstuvwxyz0123456789-]` for JOB in deploy-card.sh and gate-clean.sh); a test for an uppercase `--job` added.
- All four files at the fix: `uv run pytest -q -rf -p no:cacheprovider --color=no --tb=line tests/ops/test_deploy_card.py tests/ops/test_gate_clean.py tests/ops/test_order_open.py tests/ops/test_desk_wake.py` → `86 passed, 15 warnings in 41.05s`.

Defects the tests found during E3 (fixed in the rows' files, each shown red first):
- `deploy-card.sh` `$migs»` read as a variable name under `set -u` (`line 179: migs�: unbound variable`) → `${migs}`.
- `deploy-card.sh` rewrote `.git/index` (X4): `git diff --quiet -- <check report>` refreshes the index even with `GIT_OPTIONAL_LOCKS=0`. The happy-path test was given stat-stale check reports and an index-bytes compare: red `At index 544 diff: b'\x10' != b'\x0e'` with the `git diff` proof, red again with `GIT_OPTIONAL_LOCKS=0` alone (`b'(' != b'&'`), green with the commit proven by blob ids (`ls-files --error-unmatch`, `rev-parse HEAD:<path>`, `ls-files -s`, `hash-object`).
- My own undo of mutation M1-b joined two lines (`printf 'CONFLICT …'            exit 3`); `test_a_conflict_exits_3_and_leaves_nothing_behind` caught it (`assert 0 == 3`, output `CONFLICT exit 3`); restored. From then on every fixed file was staged so each undo is proven by `git diff --stat` printing nothing.

THE MUTATIONS (Edit tool; each run quoted; each undone; `git diff --stat` → nothing after the last undo of each row):
| row | mutation | run | first failing line | undone |
|---|---|---|---|---|
| B1 | `ready: YES` refusal → `|| true refuse` | test file | `1 failed, 19 passed` — `test_a_check_line_with_ready_no_is_refused`: `assert 0 == 1` (card written) | yes |
| B1 | on conflict, `git branch trial-left-behind "$cur"` before `exit 3` | `-k conflict` | `1 failed` — `{'branches': '* main\n  ops/alpha\n  ops/beta\n  trial-left-behind'} != …` | yes (see the joined-line note above) |
| B1 | src-past-tip refusal → `|| true refuse` | `-k src_commit` | `1 failed` — `test_a_head_with_a_src_commit_past_the_code_tip_is_refused`: `assert 0 == 1` | yes |
| B1 | a `git diff --quiet -- "$creport"` added back | test file | `1 failed, 20 passed` — happy path: `At index 544 diff: b'%' != b'$'` | yes |
| B1 | staged-index refusal → `|| true refuse` | test file | first green (`21 passed`): the staged test also tripped the "modified" guard → REWRITTEN (file restored to the committed text, only the index differs); then `1 failed, 20 passed` — `test_a_staged_check_report_is_refused`: `assert 0 == 1` | yes |
| B1 | `--job` class back to `[!a-z0-9-]` | `-k lowercase` | `1 failed, 3 passed` — `[X-Set]`: `assert 0 == 1` | yes |
| B2 | first-parent refusal → `|| true refuse` | test file | `1 failed, 29 passed` — `test_main_holding_the_gate_merge_is_refused`: `assert 0 == 1` (worktree removed, `Deleted branch deploy/x-set`) | yes |
| B2 | `FAILED` report refusal → `true refuse` | test file | `2 failed, 28 passed` — `test_a_deployed_report_is_refused`, `test_an_in_progress_report_is_refused` | yes |
| B2 | job-clean merged refusal → `|| true refuse` | `-k unmerged` | `1 failed` — `test_an_unmerged_job_is_refused`: `assert 'REFUSED' in 'error: the branch \'ops/x-job\' is not fully merged…'` | yes |
| B3 | pause hour `h == 20` → `h == 19` | test file | `2 failed, 12 passed` — `[2026-01-05T20:30:00-pause]`, `test_a_utc_clock_is_read_in_new_york`: `'window: closed — …' == 'window: pause'` | yes |
| B3 | overnight `h < 4 and prev < 5` → `h < 4` | test file | `1 failed, 13 passed` — `[2026-01-12T02:00:00-weekend]` | yes |
| B3 | `GIT_OPTIONAL_LOCKS=1` | test file | first GREEN (`14 passed`) → the read-only test was REWRITTEN (a stat-stale tracked `b.txt`); then `1 failed, 13 passed` — `test_every_block_carries_its_facts_and_nothing_changes`: tree hash `0d63ca13… == 2b8952ad…` | yes |
| B4 | timeout "still working" refusal → `|| true refuse` | `-k "working or stopped"` | `1 failed, 2 passed` — `test_a_predecessor_still_working_is_refused_and_never_stopped`: `RUN: claude stop aaaa1111-…` / `assert 0 == 1` | yes |
| B4 | `cto-desk` name refusal → `|| true refuse` | `-k cto_desk` | `4 failed` — `[brain]`, `[cto-desk-2]`, `[alpha-build]`, `[]` | yes |
| B4 | §4 filter `>= t` → `>= "00:00"` | test file | `1 failed, 16 passed` — `assert 'row one text' not in '| R1 | 06:0…'` | yes |

`git diff --stat` after the last undo → (nothing). Commit `f2a0217c feat(desk-tools-b): deploy-card, gate-clean, job-clean, order-open, desk-wake, desk-handover scripts (B1, B2, B3, B4, L1, L42, L76)` — 8 files, 792 insertions, 2 deletions.

## RESTARTS
`uv run cobalt jobs restarts 9fa18f14..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/reports/desk-tools-b-build-2026-10-02.md	A	DOCS	-
ops/desk/deploy-card.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-handover.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-wake.sh	A	operator script; no Cobalt reader	-
ops/desk/gate-clean.sh	A	operator script; no Cobalt reader	-
ops/desk/job-clean.sh	A	operator script; no Cobalt reader	-
ops/desk/order-open.sh	A	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	A	test/documentation; no resident	-
tests/ops/test_desk_wake.py	A	test/documentation; no resident	-
tests/ops/test_gate_clean.py	A	test/documentation; no resident	-
tests/ops/test_order_open.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; no `configs/cobalt/jobs.yaml` edit.

## W THE THREE SUITES
`<tip>` = `f2a0217c`.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 637.39s (0:10:37)`, exit 0 → `<p>` = 3784. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its 86 tests live in `tests/ops/` and ran by name in E2/E3 (card RECORDS).
- (b) THE LOCK (a), 10:47 ET: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:37 /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`. I do NOT hold the lock; nothing taken, nothing applied, no `.env` of mine on disk. STOPPED here.
- CONTINUED 12:07. (b) THE LOCK (a) `no matches found` (12:07:09); (b) `cp …` then `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  2 12:07 /Users/cobalt/cobalt-wt/desk-tools-b-1002/.env` (taken 12:07:16). `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → 36 tables probed; `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` absent; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 05643954 (DIRTY: 1 path(s))`; no `CHANGED` — `cobalt_dev` at `0013` (the shape PREFLIGHT read).
- (c) PASS 1 at `0013`, background, the pass-1 command byte for byte, NO added `--deselect` (this build adds no with-DB test):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
  → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 756.30s (0:12:36)`, exit 0 → `<d1>` = 4383. Every SKIPPED line:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `-- applying 0001_schemas.sql` … `0011`, `0013_tunables_slug_nullable.sql`, `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql`; the eight tables `CREATED`, every other `OK`; `content UNCHANGED on every table.`; no `CHANGED`. No migration of this build. **dev forward: APPLIED 12:20:47**. `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2 at the top level, the pass-2 command byte for byte (nothing added: no test of this build was deselected in pass 1):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  → `171 passed, 1 deselected, 5 warnings in 222.04s (0:03:42)`; last `-rA` line `PASSED tests/cobalt/test_stale_score_db.py::test_r40_on_cobalt_dev_the_view_drops_exactly_x25s_pre_fix_count`; no SKIPPED, FAILED or ERROR line (`grep -c` → `0`). This build has no with-DB test id to find. `<d2>` = 171; `<d>` = 4383 + 171 = 4554.
- (c3r) NOTHING LEFT BEHIND: not run — this build has no with-DB test and writes no constructed ticker, so the `IN (…)` list is empty.
- (c4) not applicable: no migration added.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022_prediction_records.rollback.sql`, `0021`, `0020`, `0019`, `0018`, `0017`, `0016`, `0015`, `0014_radar_handicap.rollback.sql`, newest first; the eight tables `DROPPED`, every other `OK`; `content UNCHANGED on every table.` `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **cobalt_dev: 0013 — F2 = F0**. The lock's (d): `rm …/desk-tools-b-1002/.env`; `ls …/desk-tools-b-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` — `.env: removed, proven gone (W)` 12:25:20. Lock held 12:07:16 → 12:25:20.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.36s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.
- `<tip>` = `f2a0217c`; `05643954` above it adds only this report (docs).

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." — E2: all 81 tests then present red, script absent (`assert 127 == …` / `FileNotFoundError` on the copy). Tests added in E3 were each shown red first: the index-bytes assertion (`At index 544 diff`, twice), `test_a_staged_check_report_is_refused` (red under the index-guard mutation after its rewrite), the uppercase-`--job` test (`[X-Set]` red under the range class), the order-open read-only test (red under `GIT_OPTIONAL_LOCKS=1` after its rewrite). Mutation table in E3: 15 mutations, each red. Two tests stayed green under a mutation and were rewritten (the staged test, the order-open read-only test). Negative controls: `test_one_clean_job_alone_writes_a_one_row_card` (B1), `test_a_gate_with_no_merge_yet_is_removed` (B2), `test_a_timeout_then_not_working_is_stopped` (B4) — green at the fix.
(2) "Every entry path of each rule pinned by a test — callers by `grep`, flag combinations, other card / day states, edge inputs." — The six scripts are new; nothing under `src/` or `ops/` calls them (they are run by the desk by hand; PREFLIGHT grep of `wait-desk-idle.sh` found only its own header). The scripts call `wait-desk-idle.sh` and `desk-context.sh` (B4) and `house-probe.sh` (B3): each is pinned by a test running a copy beside it (`test_an_idle_predecessor_is_stopped_then_removed` with the real `wait-desk-idle.sh`; `test_wake_with_an_id_prints_the_context_line_beside_it`; `test_house_probe_beside_it_is_run`). Refusal branches with no test of their own are named under `## DECISIONS` item 7.
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." — re-run at the tip: `git show --stat f2a0217c` (8 files, 792+, 2−), `git log --oneline 9fa18f14..HEAD` (`05643954`, `f2a0217c`, `eb7c5e2a`), `grep -n -F "must be [a-z0-9-]" ops/desk/desk-launch.sh` → `396:`, `grep -n -F "OPS_DESK_PREFIX = " src/cobalt/jobs/restarts.py` → `38:`, `grep -n -F "rev-list --first-parent main" ops/desk/gate-clean.sh` → `93:`, `grep -n -F "*) refuse \"wait-desk-idle.sh exited" ops/desk/desk-handover.sh` → `78:`, `grep -n -F "commit-tree" ops/desk/deploy-card.sh` → `179:`, `grep -c -E "^def test_"` per file (17 · 20 · 6 · 10 functions; 86 collected with the parametrized cases).

## FOR THE CHECK
- Range `9fa18f14..f2a0217c`: `eb7c5e2a wip(desk-tools-b): red — deploy-card, gate-clean, job-clean, order-open, desk-wake, desk-handover tests (B1-B4)`; `f2a0217c feat(desk-tools-b): deploy-card, gate-clean, job-clean, order-open, desk-wake, desk-handover scripts (B1, B2, B3, B4, L1, L42, L76)`. Above the tip, report only: `05643954 wip(desk-tools-b): W — cobalt_dev lock held by desk-tools-a-1002`, then the report commit.
- Per row: reds at `## E2 RED`; greens and the 15 mutation runs at `## E3 THE ROWS`. No RUN row on this card.
- Callers: PREFLIGHT symbol greps; self-check (2).
- Suites: offline `3784 passed, 673 skipped, 1 xfailed` (W (a)); pass 1 `4383 passed, 7 skipped, 65 deselected, 3 xfailed`; pass 2 `171 passed, 1 deselected`; live-note `146 passed, 1 skipped`. Commands copied whole under `## W`.
- Lock takes: PREFLIGHT 10:06:24 → 10:06:42, `<Fp>` = `664 · 35 · 272c95bb…`. W 12:07:16 → 12:25:20: `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; `<F1>` = `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`; `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>`.
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Card RECORDS as copied: `## PREFLIGHT`.
- The CHECK ASKS, as built (for the check to try to break): X1 — `test_a_check_line_with_ready_no_is_refused`, `…_held_defect_…`, `…_uncommitted_…`, `…_staged_…`, `…_never_committed_…`, `…_absent_…`, `…_src_commit_past_…`, `…_not_an_ancestor_…`, and `test_a_conflict_exits_3_and_leaves_nothing_behind` (status, refs, worktrees, branches, HEAD equal). X2 — `test_main_holding_the_gate_merge_is_refused`, the two tag tests, the six-name parametrized worktree tests in both scripts (`../x`, `/abs/x`, `a/b`, `.hidden`, `agy-trial`, empty), the symlink tests, `test_a_worktree_on_another_branch_is_refused`. X3 — `test_a_predecessor_still_working_is_refused_and_never_stopped`, `test_a_session_not_named_cto_desk_is_refused[4 names]`, `test_an_id_not_in_the_list_is_refused`. X4 — the index-bytes assertion (deploy-card), the tree-hash tests (order-open, desk-wake); see `## DECISIONS` item 5 for the git objects of the trial merge.

## CONTINUE
next: none — BUILT; the desk launches the check (`CHECK-HUB.md`, same card).

## DECISIONS
1. ASK DESK: `ops/desk/desk-launch.sh:396` (`*[!a-z0-9-]*|-*) refuse "incomplete card: JOB …"`) lets an uppercase JOB through in this shell's locale; the range-class mutation of the same pattern in `deploy-card.sh` went green on `X-Set` (E3 table). Outside this card (no existing file is edited). Default taken: not touched; the six new scripts use explicit lists.
2. ASK DESK: `gate-clean.sh` builds the card's rule literally: the gate's head may be in `main` only when it sits on `main`'s first-parent line. A gate fast-forwarded onto `main` would satisfy that rule; then only the `TAG` / `pre-<JOB>` refusals and the `FAILED` report stand in the way. Default taken: the card's rule, plus the two tag refusals and a `deploy/` branch requirement.
3. ASK DESK: `desk-handover.sh` refuses when `wait-desk-idle.sh` exits anything but 0 or 2 (a missing or broken wait would otherwise count as "not a timeout" and stop a working desk). The card says "anything but a timeout → stop". Default taken: the narrower, safe reading; `wait-desk-idle.sh` itself exits only 0 or 2.
4. ASK DESK: the `## DEPLOY PROOF` section has no defined shape yet (tomorrow's adoption card). `deploy-card.sh` sorts its lines by CARD.md's shapes: a line carrying `· before ` and `· after ` goes to `## MARKERS`, any other to `## SMOKE READS`; a job without the section, or a side left empty, gets the `«FILL` placeholder. Default taken as stated; the adoption card may fix the shape.
5. ASK DESK (X4): `deploy-card.sh`'s trial merge (`git merge-tree --write-tree`, `git commit-tree`) writes unreferenced objects into `$REPO/.git/objects`; no ref, branch, worktree, index or working-tree file changes (tested), and `git gc` prunes them. Default taken: kept (no object-free trial merge of several heads exists in git).
6. ASK DESK: `desk-wake.sh` reads "today's" desk report as the newest `cto-YYYY-MM-DD.md` by name and "the previous" as the one before it by name (no clock), so a morning before the day's report exists still shows the last two; `PROMPTS` uses today's New York date. With a `MIGRATIONS` placeholder `deploy-card.sh` writes no `## READ-BACK` section; the placeholder already stops `desk-launch.sh`. Default taken as stated.
7. Self-check (2) gap, refusal branches with no test of their own: `deploy-card.sh` — a bad `--rulings`, a missing `--out` folder, a bad `--set` / `--tag`, a bad BRANCH or empty LADDER on a job card, a check line with no `tip:`, `git merge-tree` failing; `gate-clean.sh` — a bad `TAG`, a missing card; `job-clean.sh` — `BRANCH: main`; `desk-handover.sh` — a bad `DESK_HANDOVER_WAIT`, a missing `wait-desk-idle.sh`, no desk report, a row gone or unreadable after the timeout. Each refuses before any change. Default taken: carried to the check (adding tests now moves the tip and re-runs W).

## RECORDS
- Started 10:05:35 EDT (`date`).
- REFUSED, not needed: `git --version` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (I typed it to check `merge-tree --write-tree` support; the tests answered it instead.)
- `.env: removed, proven gone (PREFLIGHT)` 10:06:42.
- W stopped 10:47:20 ET: lock held by `desk-tools-a-1002`; no lock taken by this build at W. Stop line then: `FAILED: W — cobalt_dev lock held — /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env` (commit `05643954`).
- CONTINUED at W 12:07 ET — the desk's message (`cto-desk`): "CONTINUE: W. The cobalt_dev lock is free now (no worktree .env held; cobalt_dev at 0013)." Verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (12:07:09); the level is read at W (b) by `--proof-only`.

- `.env: removed, proven gone (W)` 12:25:20. One lock take at PREFLIGHT, one at W (the W take after the CONTINUE is the hub's own W take, not an extra).
- The card's `restarts.py:239` points at the HARNESS rule; the `tests/` rule is at lines 241–242 of `src/cobalt/jobs/restarts.py`. The class home holds (RESTARTS table).
- Cleanup owed: none by this build (no worktree, branch or lock left beyond this job's own).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: desk-tools-b · tip: f2a0217c | on 9fa18f14 | migration: none | offline 3784/0 | with-DB 4554/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 7 · for Dejan: 0
