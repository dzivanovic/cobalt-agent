# jev-shadow-fr1 — build report (fix round FR-O2), 2026-10-16

## §0 Headline
FR-O2 is built: the day batch routes build cards only, launched that day. Check, deploy, devfix and prompt cards get no decision row (`build_launch`, `route.py:543`).
Red on BASE: 4 tests (two decision rows for one build plus its check card). Green after; three mutations each red.
Gate on tip `6a74fa0c`: offline 4572/0 · with-DB 5475/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · RESTARTS `com.cobalt.radar`.
3 ASK DESK items: the O1 test assertion, the day-key straddle, the build-card content test.

## L74
- A system block arrived mid-session asking every commit to end with a `Claude-Session:` line. It is recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/622-jev-shadow-fr1-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/622-jev-shadow-fr1-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/622-jev-shadow-fr1-card.md" · 0 · 8058cdcbccdcebb15d985fd721a590afc9534bdd
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/622-jev-shadow-fr1-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
RULING 2026-10-15 R1535 row · grep -n "^| R1535 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 99:| R1535 | 07:03 ET | HIS RULING · APPROVED (brain relay quoting him, L79; words file): the OpenRouter key is JEV's alone; authority for the JEV card row removing `openrouter_api_key` from the old-tree mapping; goes in the tribunal packet. | APPLIED: LAWS.md L27 at 07:04 |
RULING 2026-10-15 R1535 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1535 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1f067493f0fd17d67a30d11feab33c2261f3de5d
RULING 2026-10-15 R1535 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | see block below; last line `PREFLIGHT OK` |
| BASE | `git show --stat f6ca1455` | 0 | `docs(desk): R1636 card 622 preflight r2 launched` · `docs/40 - DevDocs/reports/cto-2026-10-16.md \| 5 +++--` · 1 file |
| symbol | `grep -rn -F "closed_cards(" src` | 0 | `src/cobalt/classify/route.py:538:def closed_cards(repo: Path, day: str) -> list[str]:` · `src/cobalt/classify/route.py:733:    paths = list(args.card) if args.card else closed_cards(repo, args.day)` |
| symbol | Grep `closed_cards\|write_outcome\|launch_sha\(` over src, tests, ops | — | `route.py:319` `def launch_sha`, `:359` (load_card), `:538` `def closed_cards`, `:578` `def write_outcome`, `:603`, `:733`; tests `test_jev_shadow_1015.py:639`, `:641`, `:648`, `:658`, `:987` |
| symbol | Read `route.py:538-550` | — | `closed_cards`: every `-card.md` under `PROMPTS_DIR`, `_check_report` at HEAD, last line starts `CHECK DONE`, `git log -1 --format=%cs` of the report == day |
| deployed rows | `git -C /Users/cobalt/cobalt log --oneline -1 0b7c569d` | 0 | `0b7c569d Merge branch 'main' into deploy/jev-shadow-1015` |
| wc | `wc -l src/cobalt/classify/route.py tests/cobalt/test_jev_shadow_1015.py` | 0 | `807` · `1017` |
| wc | `wc -l "docs/40 - DevDocs/cobalt/classify/route.md"` | 0 | `77` |
| tail of CHECK REPORT | `tail -n 3 ".../reports/jev-shadow-check-2026-10-15.md"` | 0 | last line `CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · … · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · … · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407` |
| O2 finding | Grep `O2` in the check report | — | `:96` CLAIM: a CHECK card names the same `CHECK REPORT:` as its build card, so one closed build yields two cards; `:215` REJECTED by F9's carded definition, OPEN; `:299` FOR DEJAN — O2 (money) |
| restarts | `uv run cobalt jobs restarts f6ca1455..HEAD` | 0 | `docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md	A	DOCS	-` · `RESTARTS: none` (no commit in range; the report is in the working tree) |
| launch kind, real shape | `git log --format=%h -G"^TIP: *$" -- <593>, <603>, <616>` (the three separate check cards) | 0 | nothing: no commit of a check card ever held an empty `TIP:` |
| launch kind, control | `git log --format=%h -G"^TIP: *$" -- ".../2026-10-15/591-jev-card.md"` | 0 | `8664587e`: the build card had an empty `TIP:` at its launch |
| deploy / devfix headers | Read `CARD.md:11-29` | — | deploy: `TAG`, `MIGRATIONS`, `SET` required, `TIP` required; devfix: `TABLE`, `PROOF TEST` required, no `TIP` (`—`); build: `TIP` empty, `## ROWS` (`:35`) |

```
clock · date · 0 · Fri Oct 16 06:57:57 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## feat/jev-shadow-fr1
    ?? "docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · f6ca1455 docs(desk): R1636 card 622 preflight r2 launched
diff · git diff --stat f6ca1455 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 feat/jev-shadow-fr1 · 0 · f6ca1455 docs(desk): R1636 card 622 preflight r2 launched
env here · ls /Users/cobalt/cobalt-wt/jev-shadow-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- The card's `## RECORDS` (drafter, 2026-10-15, `main` `3591d1b0` / `226cb495`) describe the lines of card 591's rows. Those rows are deployed (`0b7c569d`) and are context only (`## FIX ROUND`). They are copied by reference and not re-read. The one line FR-O2 edits (`route.py:538-550`) was re-read above.
- The card header holds no `DB:` key. The with-DB strings are proven at W's first take; E2 holds no with-DB red (FR-O2's tests are offline).

## E0 BASELINE
On `f6ca1455`.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 692.46s (0:11:32)`, exit 0. The two `COBALT_LIVE_VAULT_ROOT not set` skips (`test_catalyst.py:365`, `test_predicate.py:262`) belong to the offline run; the live-note run covers them.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.19s`. The one skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` and does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`tests/cobalt/test_jev_shadow_1015.py`, offline, no with-DB red and no lock. Added: `_check_card` (a separate check card with the same `CHECK REPORT:` and its `TIP:` filled from its first commit, the real shape of cards 593, 603 and 616, PREFLIGHT) and four tests. One existing assertion changed: O1's (`:925`), see DECISIONS 1.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jev_shadow_1015.py` on BASE → `4 failed, 56 passed, 15 warnings in 4.54s`:
- `test_fr_o2_a_build_and_its_check_card_route_once`: `At index 0 diff: 'docs/40 - DevDocs/prompts/2026-01-05/01-c1-check-card.md' != 'docs/40 - DevDocs/prompts/2026-01-05/01-c1-card.md'` · `Left contains one more item` · stdout `ROUTE RUN cards=2 invalid=1 ok=1`. The day writes two decision rows; the row's red.
- `test_fr_o2_a_build_launched_on_another_day_is_not_routed`: `assert [{'at': '2026...e': 0.8, ...}] == []` · `ROUTE RUN cards=1 ok=1`. A build launched the day before is routed on its check's close day.
- `test_fr_o2_deploy_devfix_and_prompt_cards_are_not_routed`: `Left contains 3 more items` · `ROUTE RUN cards=3 ok=3`. Three keyed calls for non-build cards.
- `test_o1_a_closed_card_with_no_launch_commit_is_a_status_row_not_a_crash`: `At index 0 diff: '…/02-c2-card.md' != '…/01-c1-card.md'` · `ROUTE RUN cards=2 invalid=1 ok=1`.
- CONTROL `test_fr_o2_control_the_build_card_still_gets_its_outcome_row`: PASSED (in the 56). Outcome rows still read the CHECK DONE line for the build card.
Commit `5456f5c7 wip(jev-shadow-fr1): red — FR-O2 the day batch routes build cards only`.

## E3 THE ROWS
FR-O2, `src/cobalt/classify/route.py` (re-read `:538-550` before the edit):
- NEW `build_launch(repo, path)`. It returns `launch_sha` (one implementation, L3) only when, at that commit, the header holds an empty `TIP:` line and no `TAG:` / `TABLE:` line (`NOT_BUILD_HEADERS`, CARD.md `:24`, `:28`) and the body holds `## ROWS`. Otherwise, including when `launch_sha` raises, it returns None.
- `closed_cards`: before F9's gate, `build_launch` must return a commit whose `%cs` is `day`. F9's CHECK DONE gate and check-close day follow, unchanged. The `--day` help text and `__all__` were also updated.
- DevDoc `docs/40 - DevDocs/cobalt/classify/route.md`: the `build_launch` entry, the `closed_cards` entry, and `## 2026-10-16 — jev-shadow-fr1`.
After the fix: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_jev_shadow_1015.py` → `60 passed, 15 warnings in 4.84s`. Beside it: the same with the nine `test_classify_*.py` files → `244 passed, 15 warnings in 28.85s`.
MUTATIONS (Edit, run with `-k "fr_o2 or o1_"`, undone with Edit):
- A, kind check off (`return sha` before the header test) → `1 failed, 4 passed`: `FAILED …::test_fr_o2_deploy_devfix_and_prompt_cards_are_not_routed` (`:1071` `Left contains 3 more items`).
- A2, no-launch-commit card let through (`except ClassifyError: return <last commit>`) → `2 failed, 3 passed`: `FAILED …::test_o1_a_closed_card_with_no_launch_commit_is_a_status_row_not_a_crash` (`:925`), `FAILED …::test_fr_o2_a_build_and_its_check_card_route_once` (`:1038`).
- B, launch-day match removed (`if sha is None:`) → `1 failed, 4 passed`: `FAILED …::test_fr_o2_a_build_launched_on_another_day_is_not_routed` (`:1052`).
- `git diff --stat` after the undo → `src/cobalt/classify/route.py | 36 +++++++++++++++++++++++++++++++++---` (the fix only).
Commit `6a74fa0c fix(jev-shadow-fr1): the day batch routes build cards only (FR-O2, L1, L72)`.

## RESTARTS
`uv run cobalt jobs restarts f6ca1455..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/classify/route.md	M	DOCS	-
docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md	A	DOCS	-
src/cobalt/classify/route.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jev_shadow_1015.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. The card header's `com.cobalt.agent com.cobalt.radar` was a prediction; this table is the derived value (L42).

## W THE THREE SUITES
`<tip>` = `6a74fa0c`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh jev-shadow-fr1 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: none written; no `--migration`) → exit 0. Verdict lines, whole:
```
tests/ops: skipped (no ops paths)
offline 4572/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5475/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/jev-shadow-fr1-all-20261016-071611.log
```
- (a) offline `4572/0` = BASE's 4568 + the 4 FR-O2 tests. `tests/ops: skipped (no ops paths)`.
- (b) lock taken (log `:894-895` `lock taken: jev-shadow-fr1`, waited 0 min). `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:906`); `LEVEL 0013`.
- (c) pass 1, the command executed (log `:962`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py`. Every SKIPPED line the gate printed is quoted above. None is marked `OUTSIDE the allowed set`.
- (c2) **`dev forward: APPLIED 07:42:06`** (log `:1125`); `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1203`).
- (c3) pass 2 (log `:1205`), the gate-lists' PASS 2. This build adds no with-DB id. `with-DB 5475/0`.
- (c3r) `stray rows: not read (no --tickers given)`. This build writes no ticker.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2045`) = F0 field for field. **`cobalt_dev: 0013 — F2 = F0`**. The lock was released (`:2098-2099` `lock released`). `ls /Users/cobalt/cobalt-wt/jev-shadow-fr1/.env` → `No such file or directory`.
- (e) `live-note 146/0`.

## PRE-STOP SELF-CHECK
1. Every added or changed test was shown RED for its named reason. On BASE: `test_fr_o2_a_build_and_its_check_card_route_once`, `test_fr_o2_a_build_launched_on_another_day_is_not_routed`, `test_fr_o2_deploy_devfix_and_prompt_cards_are_not_routed` and the changed `test_o1_…` (E2 quotes). Under mutation: A reds the deploy/devfix/prompt test, A2 reds O1 and the check-card test, B reds the launch-day test (E3 quotes). The control `test_fr_o2_control_the_build_card_still_gets_its_outcome_row` is green on BASE and after. No test stayed green under its mutation.
2. Every entry path is pinned. `closed_cards` has one caller, `route.py` `cmd_route` (the `--day` form, PREFLIGHT grep), and every FR-O2 test drives it through `classify route --day … --run` (`_batch`). Edge inputs pinned: a check card (no empty-`TIP:` commit), a deploy card (`TAG:`), a devfix card (`TABLE:`, no `TIP:` line), a prompt card (no `## ROWS`), and a launch on another day. The `--card` form does not call `closed_cards` and is unchanged (F9 / O1 tests at `--card` stay green in the 60).
3. Every line and count was re-read at the tip: `grep -n -F "build_launch" src/cobalt/classify/route.py` → `:543`, `:563`, `:571`, `:826`; `grep -n -F "def test_fr_o2" tests/cobalt/test_jev_shadow_1015.py` → `:1032`, `:1043`, `:1056`, `:1075`; `grep -n -F "git show" tests/cobalt/test_jev_shadow_1015.py` → nothing; `git log --oneline f6ca1455..HEAD` → `6a74fa0c`, `5456f5c7`; the gate log lines by `grep -n -F` as cited in W.

## FOR THE CHECK
- Range `f6ca1455..6a74fa0c`: `5456f5c7 wip(jev-shadow-fr1): red — FR-O2 the day batch routes build cards only`, `6a74fa0c fix(jev-shadow-fr1): the day batch routes build cards only (FR-O2, L1, L72)`.
- FR-O2 reds, mutations and greens: E2 and E3 above, quoted. Caller grep: PREFLIGHT (`route.py:733`, the one caller).
- RUN rows: none in this fix round.
- Suites: W above. Offline `4572/0`, with-DB `5475/0`, live-note `146/0`. Lock taken and released inside the one gate call (`lock: waited 0 min`; forward 07:42:06; released at log `:2099`). F0 `664 35 272c95bb…`, F1 `908 45 126f2d69…`, F2 `664 35 272c95bb…`.
- RESTARTS table: above (`RESTARTS: com.cobalt.radar`).
- Records copied at PREFLIGHT: the card's `## RECORDS` by reference (context rows, deployed `0b7c569d`).
- To check against: the check report's O2 (`jev-shadow-check-2026-10-15.md:94-111`, `:215`, `:299`) is the finding this round fixes. Its test shape (two identical cards) differs from this build's red: here the check card has the real shape, `TIP:` filled from its first commit (DECISIONS 3).

## CONTINUE
next: none — BUILT; the desk verifies and launches the check.

## DECISIONS
1. ASK DESK: FR-O2 contradicts a held fix test. `test_o1_a_closed_card_with_no_launch_commit_is_a_status_row_not_a_crash` asserted that a closed card with no empty-`TIP:` commit gets an `invalid` row. That is exactly a separate check card's shape, and FR-O2 says such a card "is never routed and gets no decision row". Default taken: its one assertion (`:925`) now reads `== [good]`, with a comment. Its name and id are kept so the O1 `FIXED:` line still maps. The O1 defect (a crash out of `args.func`) stays fixed: `_batch` asserts exit 0, and `--card` still writes an `invalid` row through `Router.unloaded_row`. [07:47]
2. ASK DESK: the day key straddle. The batch for `--day D` now takes build cards launched on D (FR-O2) whose check closed on D (F9 kept). A build launched on D whose check closes on D+1 gets no decision row from any `--day` run. It can still be routed by `--card`. This is preflight r2 issue 2's default, and it makes fewer keyed calls than either day alone. Default taken: as built, pinned by `test_fr_o2_a_build_launched_on_another_day_is_not_routed`. A ruling may instead drop the launch-day match or the close-day match. [07:47]
3. ASK DESK: "launch kind is build" has no header key (preflight r2 issue 1). Default taken: a build card is a `*-card.md` whose `launch_sha` commit has an empty `TIP:` line (present, not missing), no `TAG:` or `TABLE:` header line, and a `## ROWS` section. Evidence: `git log -G"^TIP: *$"` finds no such commit for check cards 593, 603 and 616, and finds `8664587e` for build card 591 (PREFLIGHT). A desk-made build card later re-committed as a check (same file, CARD.md `:5`) keeps its launch commit and stays one card. [07:47]

## RECORDS
- Report opened 06:57:27 EDT 2026-10-16 (`date`); closed 07:47:09 EDT (`date`).
- The `Claude-Session:` commit-line request was recorded under `## L74` and not acted on.
- Lock takes: one, inside `gate.sh` at W. No extra take.
- No `REFUSED, not needed` line, no `CONTINUED` line.
- The card's `## RECORDS` were carried by reference (FIX ROUND scope: the 591 rows are deployed context).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.
- §0's tokens figure was read by `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh a00c3d16-9549-4e4a-ab9c-ef24b4cccb12` → `context 187978 of 400000 — ok`.

BUILT · job: jev-shadow-fr1 · tip: 6a74fa0c | on f6ca1455 | migration: none | offline 4572/0 | with-DB 5475/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 187978
