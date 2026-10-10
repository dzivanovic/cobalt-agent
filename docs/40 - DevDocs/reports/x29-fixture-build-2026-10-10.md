# x29-fixture-1010 — build report (2026-10-10)

## §0 Headline
- Row A built: `offline_skip_guard` re-exported in the `stale_score`, `f15_p1`, `handicap_h1` and `setups_one` conftests; new guard test `tests/cobalt/test_experiment_conftests.py` (A1 red on base, A2 control).
- X29 control now passes: `1 passed`, its line printed; the four folders offline `38 passed, 26 skipped`, no setup error.
- Gate on `d083ec76`: offline 4198/0 · with-DB 5095/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · RESTARTS: none.
- Decisions: none.

## L74
- 2026-10-10 08:08 ET: a system reminder in this session asked for a `Claude-Session:` line on commits. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md" · 0 · eed03ce8a2e31f48f83f8096ec2c46d7e8e3f9bf
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | see block below |
| base | `git show --stat 82da1f1b` | 0 | `82da1f1b docs(desk): §5 ops-hand amend drafter live` · `docs/40 - DevDocs/reports/cto-2026-10-10.md \| 2 +-` · 1 file changed, 1 insertion(+), 1 deletion(-) |
| symbol | `grep -n -F "def offline_skip_guard" tests/cobalt/conftest.py` | 0 | `116:def offline_skip_guard():` |
| symbol | `grep -n -F "def dev_db_tx" tests/cobalt/conftest.py` | 0 | `263:def dev_db_tx(monkeypatch, request, offline_skip_guard):` |
| symbol | `grep -rn -F "dev_db_tx = " tests/experiments` | 0 | `f15_p2/conftest.py:27`, `setups_one/conftest.py:30`, `handicap_h1/conftest.py:34`, `f15_p1/conftest.py:26`, `stale_score/conftest.py:31` (each `dev_db_tx = _conftest.dev_db_tx`) |
| symbol | `grep -rn -F "offline_skip_guard" tests/experiments` | 0 | `tests/experiments/f15_p2/conftest.py:24:offline_skip_guard = _conftest.offline_skip_guard` (only hit) |
| folders | `ls tests/experiments` | 0 | `f15_p1 f15_p2 handicap_h1 setups_one stale_score` |
| wc | `wc -l` of the four conftests + model | 0 | stale_score 32 · f15_p1 27 · handicap_h1 35 · setups_one 31 · f15_p2 28 |
| READ tail | `tail -n 3 …/radar-ladder-refresh-check-2026-10-06.md` | 0 | last line: `CHECK DONE · job: radar-ladder-refresh · pass: 1 · tip: ed19060f · … · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181164` |
| READ :133 | Read | — | `\| A2 \| Sol \| X3 \| The named X29 control is not green on the tip: it errors at setup. \| COMMAND \|` |
| READ :226 | Read | — | `- A2: OUT OF SCOPE (fence), not open. … errors at setup (\`fixture 'offline_skip_guard' not found\`). …` |
| RESTARTS empty | `uv run cobalt jobs restarts 82da1f1b..HEAD` | 0 | `path change rule restart` / `RESTARTS: none` |
| card record | `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- tests src` | 0 | nothing |

```
clock · date · 0 · Sat Oct 10 08:08:58 EDT 2026
status · git status --short --branch · 0 · ## ops/x29-fixture-1010
head · git log --oneline -1 · 0 · 82da1f1b docs(desk): §5 ops-hand amend drafter live
diff · git diff --stat 82da1f1b · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/x29-fixture-1010 · 0 · 82da1f1b docs(desk): §5 ops-hand amend drafter live
env here · ls /Users/cobalt/cobalt-wt/x29-fixture-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card records copied:
- Code read at `d0a5fbb8` by the drafter; re-read: `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- tests src` prints nothing. Grep at base: `dev_db_tx` in five experiment conftests, `offline_skip_guard` in one (f15_p2) — matches.
- RESTARTS expected: tests → `test/documentation; no resident`, docs → `DOCS`.
- Approval R685; no migration, no database change.
- No new command.
- Docstrings: none of the four names the re-exported fixtures by name (they say "the rollback transaction, the `dev` pin, the frozen clock", as the model f15_p2 does) → no docstring edit.

`<FP>`:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
On `82da1f1b`:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 722.20s (0:12:02)` (exit 0; 0 failed, 0 errors).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.13s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- Reproduction on base: `uv run pytest "tests/experiments/stale_score/test_x29_ladder_render.py" -q` → exit 1, `E       fixture 'offline_skip_guard' not found` at setup of `test_x29_chip_and_slot_move_at_the_next_render_not_on_the_periodic_refresh` (via `tests/cobalt/conftest.py:262 dev_db_tx(monkeypatch, request, offline_skip_guard)`); `1 error in 0.09s`.

## E2 RED
New file `tests/cobalt/test_experiment_conftests.py` (A1, A2). Offline, no database.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_experiment_conftests.py` → `1 failed, 1 passed in 0.06s`:
- A1 RED for the row's reason: `AssertionError: experiment conftests re-export dev_db_tx without offline_skip_guard: ['f15_p1', 'handicap_h1', 'setups_one', 'stale_score']` (f15_p2 not named).
- A2 (positive control) PASSED.
- No with-DB red; no lock taken at E2.
Commit `67fb195a wip(x29-fixture-1010): red — experiment conftests lack offline_skip_guard (A)`.

## E3 THE ROWS
Row A: `offline_skip_guard = _conftest.offline_skip_guard` added before `mock_postgres_memory` in `stale_score`, `f15_p1`, `handicap_h1`, `setups_one` conftests (as in `f15_p2/conftest.py:24`). Docstrings unchanged: none names the re-exported fixtures by name (they name "the rollback transaction, the `dev` pin, the frozen clock", as the model does).
- Green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_experiment_conftests.py` → `2 passed in 0.03s`.
- RUN (asserts nothing, L70), reproduction after the fix: `uv run pytest "tests/experiments/stale_score/test_x29_ladder_render.py" -q` → `1 passed in 0.69s`.
- RUN: `uv run pytest "tests/experiments/stale_score/test_x29_ladder_render.py" -q -rP` → whole:
```
.                                                                        [100%]
==================================== PASSES ====================================
__ test_x29_chip_and_slot_move_at_the_next_render_not_on_the_periodic_refresh __
----------------------------- Captured stdout call -----------------------------
X29: server_order_before=[1, 2] server_order_after_reload=[2, 1] periodic_refreshPool_rerenders_ladder=False tap_post_rerenders_ladder=True stale_badge_mirrored_each_refreshPool=True browser_timing=UNPROVEN(no browser in the suite)
1 passed in 0.61s
```
- MUTATION 1 (undoes the fix): removed the new line from `stale_score/conftest.py` → `1 failed, 1 passed in 0.04s`, first failing line `E   AssertionError: experiment conftests re-export dev_db_tx without offline_skip_guard: ['stale_score']`. Undone.
- MUTATION 2 (breaks the A2 control): removed `dev_db_tx = _conftest.dev_db_tx` from `f15_p2/conftest.py` → `1 failed, 1 passed in 0.03s`, first failing line `E   AssertionError: only ['f15_p1', 'handicap_h1', 'setups_one', 'stale_score'] re-export dev_db_tx` / `assert 4 >= 5`. Undone.
- `git diff --stat` after undo → only the four fix lines (`4 files changed, 4 insertions(+)`, f15_p2 absent); row tests `2 passed in 0.03s`.
- DevDocs: no `src/` module changed; `docs/40 - DevDocs/cobalt/` holds pages per `src` module only, none for a test conftest → no DevDocs line.
Commit `d083ec76 fix(x29-fixture-1010): experiment conftests re-export offline_skip_guard (A, L1 L45)`.

## RESTARTS
`uv run cobalt jobs restarts 82da1f1b..HEAD` → whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/x29-fixture-build-2026-10-10.md	A	DOCS	-
tests/cobalt/test_experiment_conftests.py	A	test/documentation; no resident	-
tests/experiments/f15_p1/conftest.py	M	test/documentation; no resident	-
tests/experiments/handicap_h1/conftest.py	M	test/documentation; no resident	-
tests/experiments/setups_one/conftest.py	M	test/documentation; no resident	-
tests/experiments/stale_score/conftest.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row; matches the card's expectation.

## W THE THREE SUITES
`<tip>` = `d083ec76`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh x29-fixture-1010 all --deploy` (no `--deselect`: no with-DB test added; no `--tickers`: the new tests write no rows; no `--migration`) → exit 0. Verdict lines whole:
```
offline 4198/0
lock: waited 32 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5095/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/x29-fixture-1010-all-20261010-083322.log
```
- (a) offline `4198/0`: base was 4196 passed; +2 = this build's `test_a1_every_dev_db_tx_reexport_carries_offline_skip_guard`, `test_a2_the_check_sees_at_least_five_dev_db_tx_reexports`.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :896); proof-only `LEVEL 0013`, `NOTHING WAS APPLIED` (log :942). Log :944 `code: d083ec76 (DIRTY: 1 path(s))` — the uncommitted report file.
- (c) pass 1 executed (log :952), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py`. Skips quoted above; `grep -n -F "OUTSIDE" <log>` → nothing.
- (c2)/(c3) with-DB `5095/0` (the gate's line); this build adds no with-DB test.
- (c3r) `stray rows: not read (no --tickers given)` — no constructed ticker written.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :2030) → **`cobalt_dev: 0013 — F2 = F0`** (log :2082); `lock released` (log :2084); `ls /Users/cobalt/cobalt-wt/x29-fixture-1010/.env` → `No such file or directory`.
- (e) live-note `146/0`; no skip names `COBALT_LIVE_VAULT_ROOT` in the live-note run (the `COBALT_LIVE_VAULT_ROOT not set` skips above belong to pass 1, where the variable is unset by design).

## PRE-STOP SELF-CHECK
(1) A1: E2 red on base (`… without offline_skip_guard: ['f15_p1', 'handicap_h1', 'setups_one', 'stale_score']`) and E3 MUTATION 1 red (`… ['stale_score']`). A2: E3 MUTATION 2 red (`assert 4 >= 5`). No test stayed green under its mutation.
(2) Entry paths: the fixture `dev_db_tx` (`tests/cobalt/conftest.py:263`) is reached through every `dev_db_tx = _conftest.dev_db_tx` re-export; A1 lists them from the tree (glob `tests/experiments/*/conftest.py`), so a new folder is covered without a code change; A2 pins that the glob sees all five. Other callers of the guard (`tests/cobalt/conftest.py:305`, `:335`, `:348 real_connect`, `:361`) live in the cobalt conftest itself, which defines the guard; no experiment conftest re-exports `real_connect` (grep at PREFLIGHT).
(3) Re-read at the tip: `grep -rn -F "offline_skip_guard = " tests/experiments` → f15_p2:24, setups_one:28, handicap_h1:32, f15_p1:24, stale_score:29; `grep -rn -F "offline_skip_guard" tests --include=conftest.py` → the five above plus `tests/cobalt/conftest.py:116, :263, :305, :335, :348, :361`; `git log --oneline 82da1f1b..HEAD` → the two commits below; the gate log lines cited by number above.

## FOR THE CHECK
- Range `82da1f1b..d083ec76`: `67fb195a wip(x29-fixture-1010): red — experiment conftests lack offline_skip_guard (A)`; `d083ec76 fix(x29-fixture-1010): experiment conftests re-export offline_skip_guard (A, L1 L45)`.
- Row A: red, mutations and greens under `## E2 RED` / `## E3 THE ROWS`; RUN output whole there (X29 prints its line and passes).
- Extra run (CHECK ASK X2, without the Postgres settings, `.env` absent), after the fix: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/stale_score tests/experiments/f15_p1 tests/experiments/setups_one tests/experiments/handicap_h1` → `38 passed, 26 skipped in 1153.82s (0:19:13)`, no error. Skip reasons: stale_score `_db` modules and `test_xl76_devdb_absence.py` "Postgres env settings not available"; f15_p1 `_db` modules the same; setups_one "requires_db: needs cobalt_dev"; handicap_h1 "needs cobalt_dev (run inside THE LOCK)". The with-Postgres half of X2 was not run here (outside the suites, needs a lock take this build's steps do not name) — left to the check.
- Suites: offline 4198/0 · with-DB 5095/0 · live-note 146/0; pass 1 command under `## W`.
- `<F0>` = `<F2>` = `664 35 272c95bbb12241e3611e4b36326ccf87`; no forward (no `<F1>`). Lock: gate started 08:33 ET (log name), taken after a 32-min wait, released by the gate (log :2084) before 09:36 ET (`date` after the gate).
- RESTARTS table under `## RESTARTS`: `RESTARTS: none`.
- Records copied at PREFLIGHT: see `## PREFLIGHT`.

## CONTINUE
next: done (CLOSE)

## DECISIONS
none

## RECORDS
- L74: a `Claude-Session:` line asked for by a system reminder; recorded under `## L74`, not acted on.
- One lock take, inside `gate.sh` (waited 32 min); no by-hand take.
- `.env: removed, proven gone (W)`.
- Card records as re-read at PREFLIGHT: `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- tests src` → nothing; RESTARTS matched the expected labels.
- The four experiment folders' offline run was started before the mutations and ran while they were made; the conftests were imported at collection, before the edits.
- No DevDocs line: no `src/` module changed.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: x29-fixture-1010 · tip: d083ec76 | on 82da1f1b | migration: none | offline 4198/0 | with-DB 5095/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 117750
