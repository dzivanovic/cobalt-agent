# order-open-test — build report 2026-10-03

## §0 Headline
Q1 is built. `test_every_block_carries_its_facts_and_nothing_changes` now runs a tmp copy of `order-open.sh` with a stub `house-probe.sh` beside it, so it reaches no house. It was red on BASE on the real probe, and red under the mutation. `order-open.sh` was not edited: it already finds the probe at `$(dirname "$0")`.
`tests/ops` at the tip: `471 passed, 1 xfailed`. The suites: offline 3737/0, with-DB 4578/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0) and `.env` is removed.
There are 2 decisions. The file's other 12 tests still run the real script, so they still reach the real houses. After this change no test asserts the `not probed` branch.

## L74
No block inside a tool result asked for anything. A system reminder asked for a `Claude-Session:` commit trailer; it was not added (see `## RECORDS`).

## AUTHORIZATION

Started `Sat Oct  3 07:41:00 EDT 2026` (`date`).

| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (none) |
| card placeholders | `grep -n -E "«FIL[L]" "<card>"` | 1 | (none) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/01b-order-open-test-card.md"` | 0 | `129876355eadfb70a6119408bcf33b5422a530a6` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (none) |
| STANDING R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R20 (lock strings) | `grep -n "^| R20 " cto-2026-10-01.md` | 0 | `28:| R20 | 08:31 ET | **HIS RULING** ... the lock-script strings ... | APPROVED |` |
| R20 committed | `git -C ... log -1 --format=%H -S"| R20 |" -- ".../cto-2026-10-01.md"` | 0 | `23c7cdeb217d98a24bbe81fc838909c6095f6839` |
| R47 | `grep -n "^| R47 " cto-2026-10-02.md` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A) ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C ... log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^| R154 " cto-2026-10-02.md` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock ... | HIS RULING · APPROVED |` |
| R154 committed | `git -C ... log -1 --format=%H -S"| R154 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^| R157 " cto-2026-10-02.md` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week ... | HIS RULING · APPROVED |` |
| R157 committed | `git -C ... log -1 --format=%H -S"| R157 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

All hold.

## PREFLIGHT

| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/order-open-test-1003` + `?? "docs/40 - DevDocs/reports/order-open-test-build-2026-10-03.md"` (this report, written first per REPORT) |
| HEAD = BASE | `git log --oneline -1` | 0 | `77d19438 fix(lock-relief): the offline skip mark on the 68 tests G1's guard named at the W proof run (G1, P2; L68)` |
| main checkout sees it | `git -C /Users/cobalt/cobalt log --oneline -1 ops/order-open-test-1003` | 0 | `77d19438 fix(lock-relief): ...` (same) |
| no diff | `git diff --stat 77d19438` | 0 | (none) |
| BASE | `git show --stat 77d19438` | 0 | 12 files under `tests/cobalt/`, `59 insertions(+)`, subject as above |
| no .env | `ls /Users/cobalt/cobalt-wt/order-open-test-1003/.env` | 1 | `No such file or directory` |
| lock state | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (no .env in any worktree) |
| symbol | `grep -n -F "def test_every_block_carries_its_facts_and_nothing_changes" tests/ops/test_order_open.py` | 0 | `131:def test_every_block_carries_its_facts_and_nothing_changes(desk):` |
| symbol | `grep -n -F "house-probe.sh" ops/desk/order-open.sh` | 0 | `15:#   HOUSES     the output of house-probe.sh beside this script when that file exists, else \`not probed\`` · `132:if [ -f "$here/house-probe.sh" ]; then` · `133:    sh "$here/house-probe.sh" 2>&1 \|\| echo "house-probe.sh exited non-zero"` |
| probe resolution | `grep -n -F "here=" ops/desk/order-open.sh` | 0 | `27:here=$(dirname "$0")` — the probe is already found beside the script; the card's one-line script change is NOT needed |
| callers | `grep -rn -F "order-open.sh" tests ops src` | 0 | `tests/ops/test_order_open.py:1`, `:20` (`SCRIPT = REPO / "ops" / "desk" / "order-open.sh"`), `:210`, `:212`; `ops/desk/order-open.sh:2` |
| probe beside | `ls ops/desk` | 0 | `house-probe.sh` and `order-open.sh` both present |
| wc | `wc -l tests/ops/test_order_open.py ops/desk/order-open.sh` | 0 | `222` · `137` |
| READ report | `tail -n 3 ".../reports/lock-relief-build-2026-10-03.md"` (this worktree) | 1 | `No such file or directory` — the report lives on the lock-relief branch; read from `/Users/cobalt/cobalt-wt/lock-relief-1003/...` instead |
| READ report | `tail -n 3 "/Users/cobalt/cobalt-wt/lock-relief-1003/docs/40 - DevDocs/reports/lock-relief-build-2026-10-03.md"` | 0 | last line `BUILT · job: lock-relief · tip: 77d19438 \| on bb816d45 \| ... \| decisions: 6 · for Dejan: 1` |
| DECISION 1 source | `grep -n -F "DECISION 1" <that report>` | 0 | `186:` ... the one red, `tests/ops/test_order_open.py::test_every_block_carries_its_facts_and_nothing_changes` (`assert 'sol: OUT — R... or directory' == 'not probed'`) ... → DECISION 1. |
| judge's item | `grep -n -F "order-open" ".../reports/lock-relief-decisions-2026-10-03.md"` | 0 | `9:| 1 | tests/ops/test_order_open.py red on BASE ... a stub house-probe.sh on a tmp PATH, as tests/ops/test_house_probe.py does ... only if order-open.sh resolves the probe by a fixed path instead of $(dirname "$0"), that one line ...` |
| RESTARTS | `uv run cobalt jobs restarts 77d19438..HEAD` | 0 | `docs/40 - DevDocs/reports/order-open-test-build-2026-10-03.md	A	DOCS	-` · `RESTARTS: none` (no commit in range; the tool also lists the untracked report) |

Card `## RECORDS`, copied: (1) "Stacked on card `01`'s tip `77d19438` (judge, `reports/lock-relief-decisions-2026-10-03.md` item 1); ships in set 1 with `01`." — re-read: HEAD = `77d19438`, judge's row 1 quoted above. (2) "No `DB` key: under `main`'s hub text this card takes the lock as every card does; its own proof is the `tests/ops` run in E2 / E3."

Stub shape (`tests/ops/test_house_probe.py:74-78`): `"sol: UP"`, `f"grok: OUT — {LIMIT_TEXT}"`, `"gemini: OUT — TIMEOUT"`.

`<FP>`, copied whole: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE

On `77d19438`:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 744 skipped, 1 xfailed, 36 warnings in 586.74s (0:09:46)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.96s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED

Q1's red, as the card names it — the test itself run alone on `BASE`, on the real probe: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_order_open.py::test_every_block_carries_its_facts_and_nothing_changes` → `1 failed, 15 warnings in 16.44s`:
```
>       assert block(out, "HOUSES").strip() == "not probed"
E       AssertionError: assert 'sol: OUT — R... or directory' == 'not probed'
E         - not probed
E         + sol: OUT — Reading additional input from stdin...
E         + grok: OUT — /Users/cobalt/cobalt-wt/order-open-test-1003/ops/desk/house-probe.sh: line 61: cd: /private/var/folders/.../test_every_block_carries_its_f0/wt/agy-trial: No such file or directory
E         + gemini: OUT — /Users/cobalt/cobalt-wt/order-open-test-1003/ops/desk/house-probe.sh: line 65: cd: /private/var/folders/.../test_every_block_carries_its_f0/wt/agy-trial: No such file or directory
tests/ops/test_order_open.py:161: AssertionError
```
The real probe's line: `sol: OUT — Reading additional input from stdin...` (a real `codex` was reached).

The test then rewritten (`tests/ops/test_order_open.py`): a tmp copy of `order-open.sh` in `<tmp>/ops-copy/` with a stub `house-probe.sh` beside it printing `STUB_HOUSES = ["sol: UP", "grok: OUT — usage", "gemini: OUT — TIMEOUT"]`; the run uses the copy; the HOUSES assertion is `block(out, "HOUSES").splitlines() == STUB_HOUSES`; the `tree_hash(repo, wt) == before` assertion and every other block assertion unchanged. `order-open.sh` already resolves the probe as `$here/house-probe.sh` with `here=$(dirname "$0")` (`ops/desk/order-open.sh:27`, `:132`), so the script is NOT edited.

Green with the stub: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_order_open.py` → `14 passed, 15 warnings in 183.08s (0:03:03)`.

No with-DB red: no lock taken at E2. No RUN row. Commit `e57da4c9 wip(order-open-test): red — Q1 test on a stub house-probe.sh; its red is the BASE run on the real probe`.

## E3 THE ROWS

Q1 — no `src/` or script edit (above). MUTATION (the one change that undoes the fix: the stub is not written, so the copy finds no probe): removed the three `(ops / "house-probe.sh").write_text(...)` lines with Edit; `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_order_open.py::test_every_block_carries_its_facts_and_nothing_changes` → `1 failed, 15 warnings in 1.21s`, first failing line `tests/ops/test_order_open.py:166: AssertionError: assert ['not probed'] == ['sol: UP', '...UT — TIMEOUT']`. Undone with Edit; `git diff --stat` → (none), the tree back at the fix. (The mutation chosen reaches no house; undoing the fix by running the real `SCRIPT` is the E2 run above.)

Row's tip check: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `471 passed, 1 xfailed, 15 warnings in 372.81s (0:06:12)`; 0 failed.

DevDocs: no page under `docs/40 - DevDocs/cobalt/` names `order-open` (`grep -rln -F "order-open" "docs/40 - DevDocs/cobalt"` → nothing); no module changed, so no dated line.

Commit `ccb70d7e fix(order-open-test): the order-open block test reads a stub house-probe.sh, never a real house (Q1; L45, L68)` (the module docstring sentence: "A test that reads HOUSES runs a tmp copy of the script with a stub house-probe.sh beside it: no house is called.").

## RESTARTS

`uv run cobalt jobs restarts 77d19438..HEAD` (HEAD `ccb70d7e`):
```
path	change	rule	restart
docs/40 - DevDocs/reports/order-open-test-build-2026-10-03.md	A	DOCS	-
tests/ops/test_order_open.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES

`<tip>` = `ccb70d7e`.

- (a) OFFLINE, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 744 skipped, 1 xfailed, 36 warnings in 599.19s (0:09:59)`; 0 failed, 0 errors → `<p>` = 3737. Tests this build adds: none (one test rewritten: `tests/ops/test_order_open.py::test_every_block_carries_its_facts_and_nothing_changes`, outside this suite; its own run: `tests/ops` → `471 passed, 1 xfailed`, under `## E3 THE ROWS`).
- (b) THE LOCK: take launched after W (a) completed (last `date` before it: 08:02:49 EDT), `lock taken: order-open-test-1003` at 08:23 (`.env` mtime `Oct  3 08:23`; `date` 08:24:00 EDT). `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  3 08:23 /Users/cobalt/cobalt-wt/order-open-test-1003/.env` alone. `<F0>` = `664	35	272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed; `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` absent (`-`); `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: ccb70d7e (DIRTY: 1 path(s))` (the untracked report) → `cobalt_dev` at `0013`.
- (c) PASS 1 at `0013`, executed WHOLE (main's `BUILD-HUB.md` pass-1 command byte for byte, no `--deselect` added — this build adds no with-DB test):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py`
  → `4405 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 703.73s (0:11:43)`; 0 failed, 0 errors. Every SKIPPED line:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
  → `<d1>` = 4405.
- (c2) FORWARD, `COBALT_ENV=dev uv run cobalt db migrate` → `-- applying 0001_schemas.sql` … `0011_archive_incidents.sql`, `0013_tunables_slug_nullable.sql`, `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql`; the 8 tables `CREATED`, every other `OK`, `content UNCHANGED on every table.`; no `CHANGED`. No migration of this build. `dev forward: APPLIED 08:36:46 EDT`. `<F1>` = `893	44	126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed WHOLE (main's pass-2 command byte for byte, nothing added):
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  → `173 passed, 1 deselected, 5 warnings in 219.91s (0:03:39)`; 0 failed, 0 errors; no SKIPPED line (the `ERROR`-level lines in the output are logged refusals of passing tests). This build has no with-DB test id. `<d2>` = 173; `<d>` = 4405 + 173 = 4578.
- (c3r) This build's with-DB tests write no constructed ticker (it has none), so the `aset_sizings` query has no ticker to name; not run.
- (c4) No migration added: not run.
- (e) LIVE-NOTE, `.env` absent (run before the take), `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.65s`; the skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC ...` names no `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → `0022_prediction_records.rollback.sql`, `0021`, `0020`, `0019`, `0018`, `0017`, `0016`, `0015`, `0014_radar_handicap.rollback.sql`, newest first; the 8 tables `DROPPED`, every other `OK`, `content UNCHANGED on every table.` `<F2>` = `664	35	272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **cobalt_dev: 0013 — F2 = F0**. Lock (d): `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh order-open-test-1003` → `lock released`; `ls /Users/cobalt/cobalt-wt/order-open-test-1003/.env` → `No such file or directory` (08:41:13 EDT). `.env: removed, proven gone (W)`.

## PRE-STOP SELF-CHECK

(1) The one changed test, `test_every_block_carries_its_facts_and_nothing_changes`: RED at E2 on BASE on the real probe (`AssertionError: assert 'sol: OUT — R... or directory' == 'not probed'`, `tests/ops/test_order_open.py:161`), and RED under the E3 mutation (stub not written) at `tests/ops/test_order_open.py:166: AssertionError: assert ['not probed'] == ['sol: UP', '...UT — TIMEOUT']`; green at the fix. No test stayed green under its mutation.
(2) Callers of `order-open.sh` (`grep -rn -F "order-open.sh" tests ops src`): only `tests/ops/test_order_open.py` (`:20` `SCRIPT`, `:210`/`:212` at BASE). Entry paths of HOUSES (`ops/desk/order-open.sh:132-136`): a probe beside the script → pinned by the rewritten test (three stub lines) and by `test_house_probe_beside_it_is_run`; no probe beside it (`not probed`) → no test pins it now (the BASE test did, on a tree that no longer has that shape) → DECISION 2. The other tests of the file run the real `SCRIPT` → DECISION 1.
(3) Re-read at the tip: `git show ccb70d7e:tests/ops/test_order_open.py` (whole file, read), `grep -n -F "STUB_HOUSES" tests/ops/test_order_open.py` → `24:`, `140:`, `170:`; `git log --oneline 77d19438..HEAD` → `ccb70d7e`, `e57da4c9`; `ops/desk/order-open.sh:27`, `:132` from PREFLIGHT's greps (file unchanged: not in the diff).

## FOR THE CHECK

- Range `77d19438..ccb70d7e`: `e57da4c9 wip(order-open-test): red — Q1 test on a stub house-probe.sh; its red is the BASE run on the real probe` · `ccb70d7e fix(order-open-test): the order-open block test reads a stub house-probe.sh, never a real house (Q1; L45, L68)`.
- Q1: red, mutation, greens — under `## E2 RED` and `## E3 THE ROWS`. `ops/desk/order-open.sh` NOT edited: it already finds the probe at `$(dirname "$0")/house-probe.sh` (`:27`, `:132`).
- Caller greps: under `## PREFLIGHT`.
- No RUN row.
- Suites and executed commands: under `## W THE THREE SUITES`. `tests/ops` at the fix: `471 passed, 1 xfailed`.
- Lock: one take, launched after 08:02:49 → taken 08:23 → released 08:41 EDT. `<F0>` `664 35 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` `664 35 272c95bbb12241e3611e4b36326ccf87`.
- RESTARTS table: under `## RESTARTS`.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS

1. The other 12 tests in `tests/ops/test_order_open.py` (`test_a_free_lock_and_a_clean_main_say_so`, the 9 `test_the_window_for_each_clock` cases, `test_a_utc_clock_is_read_in_new_york`, `test_an_unreadable_session_list_still_exits_0`) call `run(env, ...)` with the default `script=SCRIPT` (`:115`), the real `ops/desk/order-open.sh`, which runs the real `house-probe.sh` beside it (`:132-133`). So each of them still reaches the real houses. They stay green because none of them asserts HOUSES. Measured: the file took `14 passed ... in 183.08s` against `1.21s` for the stubbed test alone. The card's row covers one test ("THE ROWS build only the card's rows"), so they were not changed. Safe default taken: unchanged. If the desk wants to close this, it is a one-row card: point the fixture at a stubbed copy for every test.
2. After this row no test pins the `not probed` branch (`ops/desk/order-open.sh:134-135`, no probe beside the script). The E3 mutation shows that the branch prints `['not probed']`, but nothing asserts it. A test was not added because that is outside the row. Safe default taken: not added. It could go in the same one-row card as item 1.

## RECORDS

- `.env: removed, proven gone (W)`. One lock take only (W); none at E2 (no with-DB red).
- The take was launched after 08:02:49 EDT and reported `lock taken` with `.env` written at 08:23. It waited inside its retry loop, and nothing failed.
- Pass 1 and pass 2 are main's `BUILD-HUB.md` commands (the hub this launch was given, and the card's record 2: "under `main`'s hub text"), not BASE's branch copy of the hub that lock-relief edited (`--db-only`).
- The card's `READ` report `reports/lock-relief-build-2026-10-03.md` is not on this branch's tree. It was read from `/Users/cobalt/cobalt-wt/lock-relief-1003/`.
- `.venv` was created in this worktree by the first `uv run`. It is not tracked and nothing of it is committed.
- No `REFUSED` and no `CONTINUE` arrived.
- L74: no block inside a tool result asked for anything. A system reminder at launch asked for commit trailers ending `Claude-Session: https://claude.ai/code/session_01TVWacqDH8ZicbG1uq5tNf6`. The hub's L74 line governs commit trailers, so the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- The card's records as re-read: under `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: order-open-test · tip: ccb70d7e | on 77d19438 | migration: none | offline 3737/0 | with-DB 4578/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0
