# desk-tools-a — build report 2026-10-02

## §0 Headline
BUILT: rows A1–A6 at tip `d4bad986` on `9fa18f14`. That is 7 new `ops/desk/` scripts and 6 new `tests/ops/` files (123 tests); no existing file is edited.
Three suites green: offline 3784, with-DB 4383 + 171 = 4554, live-note 146. `cobalt_dev` back at `0013` with F2 = F0; `.env` removed; RESTARTS: none.
X1 by reasoning: the guard let `$'…'` quoting hide a `;`. A red test came first, then the fix. One mutation stayed green (A1 m3); its test was rewritten.
One stop at W: the lock was held by `dev-rebuild-1002`. CONTINUED by `cto-desk` at 10:37.
DECISION 1 (not his): the new scripts are committed `0644`, while their neighbours are `0755`.

## L74
The harness's attribution reminder in this session asks commits to end with a `Claude-Session:` line. Recorded here as data, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" …/prompts/BUILD-HUB.md` | 1 | nothing |
| card complete | `grep -n -E "«FIL[L]" …/17-desk-tools-a-card.md` | 1 | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/17-desk-tools-a-card.md"` | 0 | `2f286234f9edc62ef05aa41e526ed6dea88b9b3d` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | nothing |
| STANDING LIST 2026-09-30 R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C … log -1 --format=%H -S"\| R60 \|" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING 2026-10-02 R47 | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; …) … \| HIS RULING · APPROVED \|` |
| R47 committed | `git -C … log -1 --format=%H -S"\| R47 \|" -- cto-2026-10-02.md` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING 2026-10-02 R38 | `grep -n "^\| R38 " cto-2026-10-02.md` | 0 | `45:\| R38 \| 07:57 ET \| HIS RULING (direction row 1): the bare-command fix, all three parts (10-01 R45) … \| HIS RULING · APPROVED \|` |
| R38 committed | `git -C … log -1 --format=%H -S"\| R38 \|" -- cto-2026-10-02.md` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:03:27 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/desk-tools-a-1002` |
| head | `git log --oneline -1` | 0 | `9fa18f14 fix(ops-glob): every path under ops/desk/ is an operator script, by rule (G1, L42, L3)` |
| main repo's view | `git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-tools-a-1002` | 0 | same commit `9fa18f14` |
| clean | `git diff --stat 9fa18f14` | 0 | nothing |
| base | `git show --stat 9fa18f14` | 0 | `docs/40 - DevDocs/cobalt/jobs/restarts.md \| 4 ++++` · `src/cobalt/jobs/restarts.py \| 4 +++-` · `2 files changed, 7 insertions(+), 1 deletion(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/desk-tools-a-1002/.env` | 1 | `No such file or directory` |
| no .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| READ: size rule | `grep -n -F "def size" ops/desk/pre-commit` | 0 | `43:def size(l):` |
| RECORDS: ops/desk rule | `grep -n -F "operator script" src/cobalt/jobs/restarts.py` | 0 | `228: Classification(path, item.change, "operator script; no Cobalt reader", ())` |
| RECORDS: tests rule (`restarts.py:239`) | `grep -n -F "tests/" src/cobalt/jobs/restarts.py` | 0 | `241: if not rule and path.startswith("tests/"):` — the card's `:239` is the HARNESS line; the tests rule sits at `:241` (the rule itself is as the card states) |
| READ: desk report tail | `tail -n 3 …/reports/cto-2026-10-02.md` | 0 | last line `HANDOVER: predecessor 30eca1db → successor 85f601c7 at 08:08 ET` |
| READ: §4 shape | Read `cto-2026-10-02.md` | — | `## §4 Rulings 2026-10-02` at :6, header `\| R \| time \| ruling / record \| status \|`, last row `81:\| R74 \| 10:03 ET \| LAUNCHED build 17 … \| LAUNCHED \|`, `## §5 CURRENT` at :83 |
| READ: CARD header | Read `CARD.md` | — | `## THE HEADER` at :9; keys `REPORT` :19, `CHECK REPORT` :20, `HOUSE B` :21, `TIP` :18 |
| READ: test shape | `git show aeefb6df:tests/ops/test_devdb_lock.py` | 0 | read whole: tmp roots via `COBALT_WT_ROOT` / `COBALT_REPO_ROOT`, `GIT_ENV`, stub `claude` on `PATH`, `sh <script>` by subprocess |
| new files absent | `ls ops/desk/bare-guard.py … install-fixed.sh` | 1 | each `No such file or directory` (7) |
| tests/ops absent | `ls tests/ops` | 1 | `No such file or directory` |
| wc -l | — | — | every file a row writes is new; no existing file is edited |
| RESTARTS empty | `uv run cobalt jobs restarts 9fa18f14..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |

Card records copied: (1) RESTARTS class homes `ops/desk/*` → operator script, `tests/ops/*` → test/documentation — re-read above (`:228`, `:241`). (2) `tests/ops/` not on base — re-read above. (3) W runs `tests/cobalt tests/taxonomy`; the ops tests run by name; no with-DB test. (4) no outside house (R47) — re-read above.

THE LOCK PROBE (take 0): (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; (b) `cp …/.env …/desk-tools-a-1002/.env` → 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`; taken `10:04:06 EDT`.

`<FP>` (typed exactly):
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

`<Fp>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.

`COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed; the tables of the migrations above `0013` (`drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns`) absent (`-`); no `CHANGED`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 9fa18f14 (clean)`. The output prints no level line; the absent tables are the shape of `0013`.

(d) `rm …/desk-tools-a-1002/.env` → 0; `ls …/.env` → `No such file or directory`; released `10:04:22 EDT`. `.env: removed, proven gone (PREFLIGHT)`.

PROVEN BY FIRST REAL USE: `uv run pytest *` and the live-note string at E0 (both ran); `git add *` / `git commit *` at E2 (`e00b120f`); the with-DB pytest, the migrate and the rollback strings at W (c)–(f).

## E0 BASELINE
On `9fa18f14`. Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 637.86s (0:10:37)`; 0 failed, 0 errors. Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.27s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Six NEW test files under `tests/ops/` (no `conftest.py`, card record 2), each running its script by `subprocess` against tmp roots (`COBALT_REPO_ROOT`), stubs of `claude` / `herdr` on `PATH` in `test_desk_done.py`, constructed values only. No `src/` edit.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_bare_guard.py tests/ops/test_desk_watch.py tests/ops/test_card_fill.py tests/ops/test_desk_row.py tests/ops/test_desk_done.py tests/ops/test_install_fixed.py` → `117 failed, 15 warnings in 7.50s`, 0 passed. Every red is the row's named reason, no such file; first line of the first red: `can't open file '/Users/cobalt/cobalt-wt/desk-tools-a-1002/ops/desk/bare-guard.py': [Errno 2] No such file or directory`; the `sh` rows fail the same way (`sh` cannot open the script; the exit-0 / exit-1 / exit-2 asserts fail). No RUN row on this card. No with-DB red (no lock take). Commit `e00b120f wip(desk-tools-a): red — six desk scripts, no such file yet (A1-A6)`.

## E3 THE ROWS
Built in card order; only the rows' files; no existing file edited (`## NOT IN THIS JOB`). Commit `d4bad986 feat(desk-tools-a): …(A1-A6, L1, L3, L42)`.

| row | file | green (its tests alone) | mutations (Edit, run, undone) → red |
|---|---|---|---|
| A1 | `ops/desk/bare-guard.py` | `36 passed` | (m1) quotes not tracked (`quote = c` → `pass`) → `5 failed, 25 passed`, first: `[git commit -m "a; b and c > d"]` blocked naming `` `;`, a redirect `>` ``. (m2) `` ` `` / `$(` not looked for inside double quotes → `2 failed, 28 passed`: `[echo "$(date)"]`, ``[echo "`date`"]``. (m3) the prefix before ` < /dev/null` not scanned → GREEN at first: **test rewritten** — added `ls && codex exec "x" < /dev/null` and `cat f \| codex exec "x" < /dev/null` → under m3 `2 failed, 30 passed`. (m4) no exception (always scan whole) → `2 failed, 30 passed`: `[codex exec -s read-only "Reply OK." < /dev/null]`, `test_the_dev_null_exception_is_only_the_exact_ending`. (m5, X1 by reasoning) `$'…'` ANSI-C quotes not tracked — the build's first scanner; red before the fix: `2 failed, 34 passed`: ``[echo $'\''; ls-`;`]`` passed, `[echo $'a\'b; c']` blocked; the fix adds the `$'` state → `36 passed` |
| A2 | `ops/desk/desk-watch.sh` | `15 passed` | (m1) `check` reads `REPORT` → `1 failed`: `test_kind_check_reads_the_check_report_not_the_report` (`STILL RUNNING after 30s — last line: BUILT · job: x`). (m2) stop word looked for anywhere in the file → `1 failed, 14 passed`: `test_a_stop_word_in_the_middle_of_the_file_does_not_fire` (`assert 0 == 2`). (m3) cap `7000` → `70000` → `1 failed`: `test_more_than_7000_seconds_is_refused` (`assert 0 == 1`) |
| A3 | `ops/desk/card-fill.sh` | `16 passed` | (m1) job name not compared → `2 failed, 14 passed`: `job: y-job`, `job: x-jobber` (`assert 0 == 1`). (m2) the whole card treated as header → `4 failed, 12 passed`, first: `REFUSED: the card's header has 2 TIP lines`. (m3) `self-check: 3 of 3` gate off → `1 failed, 15 passed`: the `self-check: 2 of 3` case |
| A4 | `ops/desk/desk-row.sh`, `ops/desk/desk-commit.sh` | `21 passed` | (m1) n = last row + 1 → `1 failed, 20 passed`: `\| R3 \| 10:22 ET \| RECORD: four. \| RECORD \|` (a number that exists, X3). (m2) LAUNCHED exception off → `1 failed`: `REFUSED: the row is 309 characters, over 300`. (m3) code-path refusal off → `6 failed, 15 passed`: `src/x.py`, `SRC`, `configs/a.yaml`, `ops/desk/x.sh`, `tests/x.py`, `docs/../src/x.py` |
| A5 | `ops/desk/desk-done.sh` | `19 passed` | (m1) brain / desk guard off → `3 failed, 16 passed`: `bbbb2222` (brain), `cccc3333` (brain-2), `dddd4444` (cto-desk). (m2) a FAILED build / check closed → `2 failed, 17 passed`: `[build]`, `[check]`. (m3) a failing step does not stop → `1 failed, 18 passed`: `test_a_failing_stop_ends_the_script_with_no_rm` |
| A6 | `ops/desk/install-fixed.sh` | `16 passed` | (m1) commit proof off → `1 failed, 15 passed`: `test_an_uncommitted_row_is_refused`. (m2) `APPROVED` check off → `1 failed, 15 passed`: `test_a_row_without_approved_is_refused`. (m3) prompts-folder check off → `3 failed, 13 passed`: `[sub]`, `[reports]`, `[outside]` |

All six together at the fix: `119 passed, 15 warnings in 18.77s`; after the A1 X1 addition `test_bare_guard.py` alone `36 passed`. After every mutation the Edit was undone; `git status --short` before the commit showed only the new files and `tests/ops/test_bare_guard.py` (the m3 / X1 additions).

DevDocs: no line written. `docs/40 - DevDocs/cobalt/` holds pages for `src/cobalt` modules only (`ls` above: `__init__.md` … `voice`); the card changes no module and edits no existing file.

## RESTARTS
`uv run cobalt jobs restarts 9fa18f14..HEAD` (at `d4bad986`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/desk-tools-a-build-2026-10-02.md	A	DOCS	-
ops/desk/bare-guard.py	A	operator script; no Cobalt reader	-
ops/desk/card-fill.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-commit.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-done.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-row.sh	A	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	A	operator script; no Cobalt reader	-
ops/desk/install-fixed.sh	A	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	A	test/documentation; no resident	-
tests/ops/test_card_fill.py	A	test/documentation; no resident	-
tests/ops/test_desk_done.py	A	test/documentation; no resident	-
tests/ops/test_desk_row.py	A	test/documentation; no resident	-
tests/ops/test_desk_watch.py	A	test/documentation; no resident	-
tests/ops/test_install_fixed.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; nothing added to `configs/cobalt/jobs.yaml`.

## W THE THREE SUITES
`<tip>` = `d4bad986`.
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 621.70s (0:10:21)`; 0 failed, 0 errors → `<p>` = 3784. This build adds no test under `tests/cobalt` or `tests/taxonomy` (its tests are `tests/ops/*`, run by name in E2 / E3, card record 3).
- (b) first attempt, THE LOCK (a) at `10:36` EDT: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 10:36 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env`; not taken; STOPPED (UNATTENDED RULES (b)), wip `2b85c6ec`. CONTINUED 10:37 (`## RECORDS`).
- (b) take 1 (W): (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (10:37:19); (b) `cp …` → 0; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/desk-tools-a-1002/.env`; taken `10:37:26 EDT`. `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` (= `<Fp>`). `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables; the eight tables above `0013` absent (`-`); no `CHANGED`; `NOTHING WAS APPLIED`; `code: 2b85c6ec (DIRTY: 1 path(s))` (the report). Level `0013`.
- (c) PASS 1 (background), executed WHOLE, no added `--deselect` (this build has no with-DB test):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk`
  → `4383 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 766.68s (0:12:46)`; 0 failed, 0 errors → `<d1>` = 4383. Every SKIPPED line:
  `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → applying `0001_schemas.sql` … `0013_tunables_slug_nullable.sql`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql`; 8 tables `CREATED`, every other `OK`, no `CHANGED`; `content UNCHANGED on every table.` No migration of this build. **dev forward: APPLIED 10:51:02 EDT.** `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2 (background), executed WHOLE, nothing added (no with-DB test of this build):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  → `171 passed, 1 deselected, 5 warnings in 223.71s (0:03:43)`; 0 failed, 0 errors, no SKIPPED line (`grep -n -F "SKIPPED"` → nothing); `grep -c -F "PASSED"` → 171 → `<d2>` = 171. `<d>` = 4383 + 171 = 4554.
- (c3r) This build's with-DB tests write no ticker (it adds none); no query owed.
- (c4) No migration added: not run.
- (f) ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0022_prediction_records.rollback.sql`, `0021`, `0020`, `0019`, `0018`, `0017`, `0016`, `0015`, `0014_radar_handicap.rollback.sql`, newest first; 8 tables `DROPPED`, every other `OK`; `content UNCHANGED on every table.` `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **cobalt_dev: 0013 — F2 = F0**. The lock's (d): `rm …/desk-tools-a-1002/.env` → 0; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; released `10:55:30 EDT`. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.61s`; the skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …` (it does not name `COBALT_LIVE_VAULT_ROOT`) → `<l>` = 146.
- The rows' own tests at the tip: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/…` (the six files) → `123 passed, 15 warnings in 19.84s`.

## PRE-STOP SELF-CHECK
(1) Every added test shown red for its named reason: all 117 at E2 (`117 failed`, no such file, `e00b120f`); per row, the E3 mutations above turn its tests red (A1 m1–m5, A2 m1–m3, A3 m1–m3, A4 m1–m3, A5 m1–m3, A6 m1–m3). One stayed green: A1 m3. Its test was rewritten (two compound commands ending ` < /dev/null`), and they went red under m3. The X1 additions were red before their fix (`2 failed, 34 passed`). — holds.
(2) Every entry path pinned: the scripts are new and nothing calls them yet (`grep -rn -F "desk-watch.sh" src ops configs` → only its own lines and `desk-done.sh:4`'s comment; `grep -rn -F "bare-guard" src ops configs .claude` → only `ops/desk/bare-guard.py:2`). Installing the hook and running any script for real are fenced out by `## NOT IN THIS JOB`. Each script's entry is its argument line, and each is pinned. Every kind of `desk-watch.sh` / `desk-done.sh` is tested, plus a bad kind, a bad or over-limit number and a missing card or report. `card-fill.sh` is tested with and without `--no-house`, with filled versus empty values, and on a second run. `desk-row.sh` is tested on order R1, R3, R2, on the 300 / 301 edge, on LAUNCHED versus other statuses, and with no §5. `desk-commit.sh` is tested on relative, absolute, `..`, outside and each code root, plus the hook's exit. `install-fixed.sh` is tested with `R1` and `1`, R1 versus R11 / R12, duplicate, uncommitted, unapproved, no token, unclosed token, token elsewhere and three wrong folders. `bare-guard.py` is tested on non-Bash, broken JSON and each operator inside and outside quotes. — holds.
(3) Every `file:line`, count and quote re-read at the tip: `grep -n -F "tests/" src/cobalt/jobs/restarts.py` → `241:`; `grep -n -F "operator script" …` → `228:`; `git diff --stat 9fa18f14 d4bad986` → `13 files changed, 1466 insertions(+)` (7 scripts, 6 tests); `git log --oneline 9fa18f14..HEAD` → the three commits below; the suite summaries are quoted from their output files (`tail`, `grep -c`). — holds.

## FOR THE CHECK
- Range `9fa18f14..d4bad986` (+ report commits). Commits: `e00b120f wip(desk-tools-a): red — six desk scripts, no such file yet (A1-A6)` · `d4bad986 feat(desk-tools-a): bare-guard hook, desk-watch, card-fill, desk-row, desk-commit, desk-done, install-fixed (A1-A6, L1, L3, L42)` · `2b85c6ec wip(desk-tools-a): W — cobalt_dev lock held by dev-rebuild-1002` (report only) · the report commit at CLOSE.
- Per row reds, mutations and greens: `## E2 RED` and the `## E3 THE ROWS` table. No RUN row on the card.
- Caller greps: self-check (2).
- Suites and executed commands: `## W THE THREE SUITES`. `<F0>` = `<Fp>` = `<F2>` = `664 · 35 · 272c95bb…`; `<F1>` = `893 · 44 · 126f2d69…`. Lock takes: PREFLIGHT 10:04:06–10:04:22; W 10:37:26–10:55:30 (EDT).
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: `## PREFLIGHT`.
- CHECK ASKS, for the checker: X1 — the build's own reasoning found and closed the `$'…'` hole. Left as built: `$((1+1))` is blocked as `$(`. A `#` comment holding an operator is blocked (conservative). A heredoc is blocked as `<`. A bar or redirect inside single or double quotes passes. X2 — the guards are pinned by A5 m1 / m2. Also refused, with no stop or rm: a session missing from the list, or a list that cannot be read. X3 — pinned by A4 m1; a row goes only after the last row line before the first `## §5`. X4 — only line 1 is rewritten (`partition("\n")`), and a token left anywhere refuses. The row proof is pinned by A6 m1 / m2.

## CONTINUE
next: CLOSE (done at the commit of this report).

## DECISIONS
- DECISION 1 (safe default taken): the seven new scripts are committed mode `0644` (`ls -la ops/desk`: `-rw-r--r--` each), while their neighbours (`desk-launch.sh`, `wait-stop-line.sh`, …) are `0755`. `chmod` and `git update-index --chmod` are not on the build's list. Each header gives its usage as run through `sh` / `python3` (the tests run them so), which works at `0644`; a direct `ops/desk/<name>.sh` call does not. The desk or the install step sets `+x` if direct calls are wanted.

## RECORDS
- `.env: removed, proven gone (PREFLIGHT)`.
- Card record `restarts.py:239` re-read: the tests rule is at `src/cobalt/jobs/restarts.py:241` (`:239` is the HARNESS line); the rule is as the card states.
- Stopped at W (b) `10:36:36 EDT`: cobalt_dev lock held by `/Users/cobalt/cobalt-wt/dev-rebuild-1002/.env`.
- **dev forward: APPLIED 10:51:02 EDT** — from here every ending runs W (f).
- CONTINUED at W 10:37 ET — message from `cto-desk` ("the cobalt_dev lock is free now"); verified: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` at `10:37:19 EDT`.
- `cobalt_dev: 0013 — F2 = F0` (W (f)); `.env: removed, proven gone (W)`.
- Lock takes: two (PREFLIGHT probe, W); no extra take (no with-DB red at E2).
- L74: one attribution reminder asking for a `Claude-Session:` line; recorded under `## L74`, not acted on.
- No `REFUSED, not needed` line: no command was refused.
- Card records as re-read at PREFLIGHT: `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: desk-tools-a · tip: d4bad986 | on 9fa18f14 | migration: none | offline 3784/0 | with-DB 4554/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
