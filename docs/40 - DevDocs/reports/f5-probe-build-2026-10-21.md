# f5-probe — build report 2026-10-21

## §0 Headline
- `cobalt checkpoint probe <item> [--keep-groups PATH]` is built for X4, X5, X6, X7, X10, X13 (new `src/cobalt/prefill/checkpoint_probe.py`). `fetch_groups` and `fetch_figures` gain `keep=`; the run path passes none.
- 10 rows of 10: nine built (P1 P2 G1 X6 X4 X13 H1 C1 D0) and R1 run. 39 reds shown on BASE, and each row's mutation was shown red, then undone.
- Gate on `c2565a9f`: offline 4943/0, with-DB 5915/0, live-note 148/0. `cobalt_dev` is at 0013 with F2 = F0, `.env` is removed, RESTARTS is `com.cobalt.radar`.
- Four DECISIONS, none for Dejan. No live run, Finviz GET, model call or plist load happened in this job.

## L74
- The session's harness attribution notice asked for a `Claude-Session:` line on commits. It is recorded once here as data. BUILD-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, so none was added.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/973-f5-probe-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-21/973-f5-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-21/973-f5-probe-card.md" · 0 · 41804777b7d57249e7d1406531dcb37ca0fb3e6f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-21/973-f5-probe-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Wed Oct 21 12:19:14 EDT 2026
status · git status --short --branch · 0 · ## ops/f5-probe
head · git log --oneline -1 · 0 · d988d543 docs(desk): R2282 brain rulings on 970, f5-probe drafter prompt 972
diff · git diff --stat d988d543 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f5-probe · 0 · d988d543 docs(desk): R2282 brain rulings on 970, f5-probe drafter prompt 972
env here · ls /Users/cobalt/cobalt-wt/f5-probe/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat d988d543` → `docs(desk): R2282 brain rulings on 970, f5-probe drafter prompt 972`, 2 files changed (`prompts/2026-10-21/972-draft-f5-probe.md` +14, `reports/cto-2026-10-21.md` +5).

THE CARD'S SYMBOLS (at BASE):
| rule | command | exit | output |
|---|---|---|---|
| checkpoints.py symbols | `grep -n -E "^(async )?def (window_refusal\|parse_groups\|fetch_groups\|fetch_figures\|compute_delta\|_strings\|validate_reply\|narrate\|default_stores\|check_demand\|run_checkpoint\|cmd_run\|add_parser\|_response_schema)\(\|^(WRITER\|GROUPS_URL\|SECTORS\|PHRASES\|_SYSTEM)" src/cobalt/prefill/checkpoints.py` | 0 | `91:WRITER` · `104:GROUPS_URL` · `107:SECTORS` · `115:PHRASES` · `167:def window_refusal` · `200:def parse_groups` · `224:async def fetch_groups(groups)` · `238:def fetch_figures(cfg)` · `283:def compute_delta` · `353:def _strings` · `363:def validate_reply` · `394:def _response_schema` · `405:_SYSTEM` · `413:def narrate` · `559:def default_stores` · `576:def check_demand` · `652:def run_checkpoint(` · `813:def cmd_run` · `837:def add_parser` |
| callers of fetch_groups | `grep -rn -F "fetch_groups(" src` | 0 | `checkpoints.py:224` (def), `checkpoints.py:242` (in `fetch_figures`) |
| callers of fetch_figures | `grep -rn -F "fetch_figures(" src` | 0 | `checkpoints.py:238` (def), `checkpoints.py:704` (in `run_checkpoint`) |
| env / guard / note / vault | `grep -n -E "^def (resolve_env\|refuse_if_secret_shaped\|daily_note_path\|resolve_vault_path)" …` | 0 | `env.py:60`, `guard.py:40`, `note.py:250`, `vault.py:155` |
| test seams | `grep -n -E "^def groups_http\|^def cp\(\|def test_0745_at_0820\|^class TestNumbers" tests/cobalt/test_checkpoints_offline.py` | 0 | `138:def cp`, `307:def groups_http`, `327:class TestNumbers`, `682:test_0745_at_0820_is_refused_exit_2` |
| radar import | `grep -rn -F "cobalt.cli" configs/cobalt/jobs.yaml` | 0 | `203: imports: [cobalt.cli]` (and comment lines 439, 455, 463) |
| CLI mount | `grep -n -E "checkpoints\|def main\|…" src/cobalt/cli.py` | 0 | `91: from cobalt.prefill import checkpoints as checkpoints_cli`, `579: checkpoints_cli.add_parser(sub)` |
| wc -l (files to edit) | `wc -l …` | 0 | `checkpoints.py` 852, `test_checkpoints_offline.py` 931, `prefill/checkpoints.md` 74, `cli.md` 151 |
| `## READ` reports | `tail -n 3` | 0 | `draft-f5-gate-run-2026-10-21.md` → `DRAFTED · decisions: 11`; `f5-x3-measure-2026-10-20.md` → `BUILT · job: f5-x3-measure · tip: de976722 …` |
| restarts, empty range | `uv run cobalt jobs restarts d988d543..HEAD` | 0 | only this report (untracked, DOCS); `RESTARTS: none` |

The card's `## RECORDS` were copied and re-read. `checkpoints.py:747-751` is the note stop. `env.py:60-70`, `client.py:126-133`, `vault.py:155` and `note.py:250` were re-read and match. The `fetch_groups` lines `:224-235`, `fetch_figures` `:238`, `add_parser` `:837-844` and `run_checkpoint` `:652` match. `data/deploy/bootstrap-owed.json` was not read: it is gitignored and not a row's file. The RULINGS row is proved by AUTHORIZATION above.

## E0 BASELINE
- Offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4904 passed, 878 skipped, 4 xfailed, 36 warnings in 772.94s (0:12:52)`, exit 0.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.16s`. The one skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_checkpoint_probe.py tests/cobalt/test_checkpoints_offline.py` → `39 failed, 62 passed in 4.12s`. The new tests are `tests/cobalt/test_checkpoint_probe.py` (38) and `TestNumbers::test_keep_gets_the_body_before_the_parse`.
- 37 tests are red at their first probe call, with argparse exit 2 and `cobalt checkpoint: error: argument command: invalid choice: 'probe' (choose from run)`. That is the reason the card names. Examples: `test_the_probe_is_mounted…: assert 2 == 0`, `test_production_and_unset_env_are_refused[X4]: assert (2, '') == (1, 'PROBE X4...(dev only)\n')`. In the C1 control (`test_an_unknown_item_is_refused[X2]`) the message names `'probe'`, not the item, as the card says.
- `TestNumbers::test_keep_gets_the_body_before_the_parse` → `TypeError: fetch_groups() got an unexpected keyword argument 'keep'`, the reason the card names.
- `test_the_run_path_writes_no_body` → `AssertionError: fetch_groups passes keep= on … assert []`. It is red on its first pin, the `keep=` source check by content: BASE has no `keep=` line. The card's row G1 names no separate red for it.
- No with-DB red, so no lock was taken at E2. No RUN row is a test.
- Commit `c6433002 wip(f5-probe): red`.

## E3 THE ROWS
Every `file:line` was re-found by content before the edit. Commit `c2565a9f feat(f5-probe): cobalt checkpoint probe X4/X5/X6/X7/X10/X13, the keep seam (P1 P2 G1 X6 X4 X13 H1 C1 D0, L1 L28 L32 L45)`.
- P1: `checkpoints.py:849` `PROBE_ITEMS = (...)` (one line), `:843` `cmd_probe` (lazy import, `SystemExit(main(...))`), and `:860-866` the `probe` parser after `run`. `run` is unchanged.
- P2, X6, X4, X13, H1: `src/cobalt/prefill/checkpoint_probe.py` (378 lines).
- G1: `fetch_groups(groups, *, keep=None)` calls `keep(response.text)` after `raise_for_status` and before `parse_groups`. `fetch_figures(cfg, *, keep=None)` passes it on only when it is not None (`:248`), so the call is identical when `keep=None`.
- D0: the dated sections in `prefill/checkpoints.md` and `cli.md`.
- Green after the rows: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoint_probe.py tests/cobalt/test_checkpoints_offline.py` → `101 passed in 5.59s`.
- The card's offline suite: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_checkpoint_probe.py tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_finviz_consumers.py` → `104 passed, 1 xfailed in 5.73s`, run again at the fix with the same result.
- `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_placement.py` → `7 passed in 0.04s`.

THE MUTATIONS were each made with Edit, run alone, then undone with Edit. `git diff --stat` afterwards shows only the fix (`checkpoints.py | 36 +++++++++++++++++++++++++++++-------`).
| row | mutation | test(s) | result, first failing line |
|---|---|---|---|
| P1 | subparser `"probe"` → `"probe-mutant"` | `test_the_probe_is_mounted…` | 1 failed: `assert 2 == 0` (`invalid choice: 'probe' (choose from run, probe-mutant)`) |
| P2 (a) | `if mode != env.DEV and False:` | `test_production_and_unset_env_are_refused` | 6 failed: `assert (0, 'PROBE X4... hits none\n') == (1, 'PROBE X4...(dev only)\n')` |
| P2 (b) | `shutil.rmtree` removed from `_scratch` | `test_the_scratch_dir_is_gone_after_the_run` | 1 failed: `assert not ['/var/folders/…/f5-probe-z8brkk36', …]` |
| P2 (c) | `checkpoints.default_stores()` before the item | `test_no_write_no_dm_no_db_no_launchctl` | 1 failed: `PROBE X4 FAIL error AssertionError` |
| G1 | `keep(...)` moved after `parse_groups` | `TestNumbers::test_keep_gets_the_body_before_the_parse` | 1 failed: `a body the parse refuses still reached keep first` |
| G1 (run path) | `keep = None  # mutant` in `cmd_run` | `test_the_run_path_writes_no_body` | 1 failed: `assert 'keep' not in 'def cmd_run...'` |
| G1 (file) | kept lines = every line of the body | `test_keep_groups_writes_header_and_eleven_rows_once` | 1 failed: `At index 1 diff: '' != '"1","Basic Materials",…'` |
| X6 | `refused` matches `degraded (mutant)` | `test_x6_one_prompt_refused_fails` | 1 failed: `assert 0 == 1` |
| X6 (rule D) | no rotation (`names[i]`) | `test_x6_four_prompts_one_per_slot_pair` | 1 failed: `assert ({'index_move', 'rank_move'} <= …` (no `rank_move`) |
| X4 | `VALID_BAR = 14` | `test_x4_fifteen_valid_is_ok_fourteen_fails` | 1 failed: `assert 0 == 1` |
| X4 (word) | whole-string match only | `test_x4_a_number_word_fails_and_names_the_phrase` | 1 failed: `assert 0 == 1` |
| X4 (request) | `_SYSTEM + " "` | `test_x4_request_equals_narrates` | 1 failed: `Differing items: {'messages': …}` |
| X4 (text) | invalid kind = `result.content` | `test_x4_clause_holds_no_reply_text` | 1 failed: `'PROBE X4 FAIL valid 0/20 · invalid kinds {"lines": … "constructed reply words"}=20 …'` |
| X13 | the window pre-check `and False` | `test_x13_*` | 1 failed, 1 passed: `'PROBE X13 FAIL refused: X13 reached a store (get)\n'.startswith('PROBE X13 FAIL — 07:15 ')` |
| X13 (OK) | fire at close − 5 min | `test_x13_four_late_fires_refused_ok` | 1 failed: `assert (1, 'PROBE X1...ot called)\n') == (0, …)` |
| H1 | `if item in HIS_LEGS and False:` | `test_his_legs_are_not_run_and_call_nothing` | 3 failed: `assert (1, 'PROBE X5...r KeyError\n') == (3, …)` |
| C1 | `choices=PROBE_ITEMS` removed | `test_an_unknown_item…`, `test_each_item…` | 3 failed, 10 passed: `assert (1 == 2)` |
| C1 (line) | verdict and clause on two lines | `test_each_item_prints_one_line_and_exits_by_verdict` | 10 failed: `exactly one stdout line … assert (3 == 2)` |

The one mutation that stayed green was a no-op. My first X4-request mutation Edit did not apply ("String to replace not found"), so that run tested the unmutated code: `1 passed`. I redid the Edit and the test went red (row above). No test was rewritten.

## RESTARTS
`uv run cobalt jobs restarts d988d543..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/checkpoints.md	M	DOCS	-
docs/40 - DevDocs/reports/f5-probe-build-2026-10-21.md	A	DOCS	-
src/cobalt/prefill/checkpoint_probe.py	A	static import reach	com.cobalt.radar
src/cobalt/prefill/checkpoints.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_checkpoint_probe.py	A	test/documentation; no resident	-
tests/cobalt/test_checkpoints_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. R1: the drafter's reading `com.cobalt.radar` matches the tool's last line.

DEPLOY PROOF marker reads:
- On the build tree: `ls …/f5-probe/src/cobalt/prefill/checkpoint_probe.py …/tests/cobalt/test_checkpoint_probe.py …/ops/com.cobalt.checkpoint-0715.plist` → all three listed. `grep -c -F "PROBE_ITEMS = (" …/f5-probe/src/cobalt/prefill/checkpoints.py` → `1`.
- On main (before): `ls /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` → exit 1, `No such file or directory`. `grep -c -F "PROBE_ITEMS = (" /Users/cobalt/cobalt/src/cobalt/prefill/checkpoints.py` → `0`.

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f5-probe all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`, no `--migration`) → exit 0. `<tip>` = `c2565a9f`.
```
tests/ops: skipped (no ops paths)
offline 4943/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5915/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f5-probe-all-20261021-123802.log
```
- (a) offline: `4943 passed, 878 skipped, 4 xfailed` (log :956). Of these, 39 tests are this build's (38 in `test_checkpoint_probe.py` and 1 in TestNumbers). The tests/ops line is `tests/ops: skipped (no ops paths)`.
- (b) `lock taken: f5-probe` (log :963). F0 = `664 35 272c95bbb12241e3611e4b36326ccf87` (log :974). LEVEL 0013.
- (c) pass 1, `pass 1: whole (deploy)` (log :1030). The executed command (log :1032), whole:
  `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py`
  → `5671 passed, 9 skipped, 138 deselected, 7 xfailed` (log :1200). The 9 SKIPPED lines are quoted above; the gate marks none of them `OUTSIDE the allowed set`.
- (c2) `dev forward: APPLIED 13:06:11` (log :1202). F1 = `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (log :1286).
- (c3) pass 2 → `244 passed, 1 deselected` (log :2182). `<d>` = 5671 + 244 = 5915 = `with-DB 5915/0`.
- (c3r) `stray rows: not read (no --tickers given)`. This build's tests write no rows.
- (f) F2 = `664 35 272c95bbb12241e3611e4b36326ccf87` (log :2256) = F0, field for field: **`cobalt_dev: 0013 — F2 = F0`**. `lock released` (log :2312), `.env: removed`. `ls /Users/cobalt/cobalt-wt/f5-probe/.env` → `No such file or directory`.
- (e) live-note `148 passed, 1 skipped` (log :2383), so `live-note 148/0`. Its one skip is `COBALT_TEST_LIVE_DRC`.

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." All 39 are red on BASE (E2). Each row's tests are also red under its mutation (E3 table). That covers `test_checkpoint_run_is_unchanged`: it is red on BASE at `invalid choice: 'probe'` (its first call), and its recorder control passes green. No test was rewritten. ✔
(2) "Every entry path of each rule pinned by a test — callers by grep, flag combinations, other card / day states, edge inputs."
- `fetch_groups` has 2 callers (the def and the `fetch_figures` pass-on). They are pinned by TestNumbers (with and without `keep`, and a refused body) and by `test_keep_groups…` (the real `fetch_groups` through X6).
- `fetch_figures` callers are `run_checkpoint:710`, with no `keep` (pinned by `test_the_run_path_writes_no_body`), and `checkpoint_probe.py:187` (pinned by the X6 and X4 tests).
- Flag combinations are pinned: `--keep-groups` with X4 refused, outside the root refused, existing refused, a redact hit, and the write.
- Each env state is pinned: production, unset and dev.
- Each verdict of every item is pinned (C1 parametrized). ✔
(3) "Every file:line, count and quote in the report re-read from tool output at the tip." Re-run at the tip:
- `grep -n -E "keep=|^PROBE_ITEMS|^def cmd_probe|^async def fetch_groups|^def fetch_figures|probe = csub" src/cobalt/prefill/checkpoints.py` → `224`, `242`, `248`, `843`, `849`, `860`.
- `grep -rn -F "fetch_figures(" src` → `checkpoints.py:242`, `checkpoints.py:710`, `checkpoint_probe.py:187`.
- `grep -rn -F "fetch_groups(" src` → `:224`, `:248`.
- `wc -l` → `checkpoint_probe.py` 378, `checkpoints.py` 874, `test_checkpoint_probe.py` 467, `test_checkpoints_offline.py` 947.
- `git show --stat c2565a9f` → 4 files, +413 −7.
- The gate log was read with `grep -n -E "F0: |F1: |F2: |pass 1: whole|lock taken|lock released|dev forward"` and `grep -n -E "passed|failed"`. ✔

## FOR THE CHECK
- Range `d988d543..c2565a9f`, two commits: `c6433002 wip(f5-probe): red` and `c2565a9f feat(f5-probe): cobalt checkpoint probe X4/X5/X6/X7/X10/X13, the keep seam (P1 P2 G1 X6 X4 X13 H1 C1 D0, L1 L28 L32 L45)`. The report commit follows.
- Per-row reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS`. The caller greps: `## PREFLIGHT` and self-check (3).
- RUN row R1: the RESTARTS table above, whole.
- Suites and the executed pass-1 command: `## W`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 = F0. The lock was taken at log :963 and released at log :2312, inside one gate call between 12:38 and 13:11 EDT. Clock reads: gate log name `20261021-123802`, `date` 13:11:23 EDT.
- CHECK ASKS pointers:
  - X1: the boundary is in `checkpoint_probe.py` `_verdict`/`_scratch`, pinned by `test_no_write_no_dm_no_db_no_launchctl`, `test_the_scratch_dir_is_gone_after_the_run` and `test_the_run_path_writes_no_body`.
  - X2: `_dev_only` comes first, pinned by `test_production_and_unset_env_are_refused` (all six items, no fetch, no call).
  - X3: clauses hold kinds and counts. `narrate`'s logger is disabled during the probe. X4 is pinned by `test_x4_clause_holds_no_reply_text`, the kept file by `test_keep_groups…`.
  - X4: FINAL `:178`, `:180` and `:187`. Exit codes are pinned by C1. The X13 pre-check is DECISION 1.
  - X5: TestNumbers and the whole offline suite are green, and `checkpoint run` is unchanged.
  - X6: the RESTARTS table.
- The records copied at PREFLIGHT are listed in `## PREFLIGHT`.

## CONTINUE
next: none. The build is done; the check is next (the desk's).

## DECISIONS
1. ASK DESK: X13 calls `window_refusal` for each slot before `run_checkpoint`. A window that admits the late fire is FAIL `— <slot> admitted at close + 5 min by window_refusal (run_checkpoint not called)`, and nothing is fetched. Calling `run_checkpoint` on an admitted window would send the gate check and 2 Finviz GETs live, while X13's stated live cost is none. The card's `FAIL — <slot> <action> exit <n>` stays for a `run_checkpoint` that returns other than refused. [13:11 EDT] Default: kept as built.
2. ASK DESK: `redact()` records an F19 counter row (`RedactionStore`, a database write) on any hit. This happens in G1's check of the kept body and in the guard inside `call_sync` on X6's real path. So "no database at all" holds only when nothing is secret-shaped. [13:11 EDT] Default: the card's call `redact(..., channel="modelaccess")` is kept with counting on, as every other caller does (`redact/guard.py:93-95` allows `record=False` to the log guard only).
3. ASK DESK: the card sets the refusal clauses `FAIL refused: <EnvConfigError's first sentence>` and `NOT RUN — Finviz gate: <reason>`. For an unknown `COBALT_ENV` the first sentence carries the variable's value (`COBALT_ENV is 'x' — …`). The gate reason is `check_demand`'s `<ExceptionName>: <message>`, which can carry rpm counts. [13:11 EDT] Default: built as the card says. Neither holds a secret, a market figure or model text.
4. ASK DESK: `fetch_figures` passes `keep=` on only when it is not None. So the call with no `keep` is byte-for-byte the old call, and the offline fake `groups(params)` still fits. [13:11 EDT] Default: kept.

## RECORDS
- Cleanup owed: the P2 (b) mutation (rmtree removed) left three empty dirs, `/var/folders/4b/psjqxccx3vddp35n_5k16spc0000gn/T/f5-probe-z8brkk36`, `…/f5-probe-t0298et7` and `…/f5-probe-n6tbde6a`. They are outside the worktree, and `rm` of them is not on the list.
- The first X4-request mutation Edit did not apply ("String to replace not found"), so its run was `1 passed` on the unmutated code. The Edit was redone and the test went red.
- No extra lock take, no REFUSED, no CONTINUED.
- L74: one notice. It is recorded under `## L74`; nothing was acted on.
- `tokens`: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh cf5a0353-c36a-4cde-b7bc-6b5c8a9806b9` → `context 261746 of 400000 — ok`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f5-probe · tip: c2565a9f | on d988d543 | migration: none | offline 4943/0 | with-DB 5915/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 10 of 10 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0 · tokens: 261746
