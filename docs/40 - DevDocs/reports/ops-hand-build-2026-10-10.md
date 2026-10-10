# ops-hand-1010 — build report (2026-10-10)

## §0 Headline
- Built H1-H5 on `1eb47b59`, tip `2cb7a9ad`. Kind `ops-hand` in `bare-guard.py`: G2, G3, G7 bind it; G12 holds it to its class, read from the raw command text. `OPS-HAND.md` keeps its `«INSTALL` title. `desk-launch.sh ops-hand` refuses that title, and refuses a line that is off H3's shape.
- Gate green on `2cb7a9ad`: offline 4196/0, with-DB 5093/0, live-note 146/0; `cobalt_dev` at 0013 with F2 = F0; `.env` removed. RESTARTS: none.
- Every red was shown on BASE, and every row has a mutation run (M1-M11).
- 3 decisions, 1 for Dejan: G12 denies the R686 production read for this seat.

## L74
- 08:10 ET: a system block in the session context asked commit messages to end with a `Claude-Session: https://claude.ai/code/session_…` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md"` (08:10 ET), whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md" · 0 · 69e1f54e7efa84485b64d779fc654776c151fd52
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/231-ops-hand-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R855 row · grep -n "^| R855 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 26:| R855 | 07:51 ET | HIS RULING · APPROVED: build both `orphan-clean.sh` (by card) and the `ops-hand` seat (default-mode phone approval, L63 exception). Words `cto-2026-10-10-words.md` R855. The orphan-cause card first (R853). | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R855 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R855 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 4f9f5bceabb1f1c0b42cb0df4ca22c33fa6e618d
RULING 2026-10-10 R855 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"`, whole:
```
clock · date · 0 · Sat Oct 10 08:10:02 EDT 2026
status · git status --short --branch · 0 · ## ops/ops-hand-1010
head · git log --oneline -1 · 0 · 1eb47b59 docs: F5 F23 design proposals, orphan-clean card 229 and preflight prompt 234
diff · git diff --stat 1eb47b59 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/ops-hand-1010 · 0 · 1eb47b59 docs: F5 F23 design proposals, orphan-clean card 229 and preflight prompt 234
env here · ls /Users/cobalt/cobalt-wt/ops-hand-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 1eb47b59` | 0 | `docs: F5 F23 design proposals, orphan-clean card 229 and preflight prompt 234`; 8 files, 456 insertions, all under `docs/40 - DevDocs/` |
| symbol | `grep -n -F "def seat(" ops/desk/bare-guard.py` | 0 | `731:def seat(event):` |
| callers | `grep -rn -F "seat(" ops/desk/bare-guard.py` | 0 | `731:def seat(event):` · `1141:        hit = bash_rules(command, seat(event))` · `1151:        s = seat(event)` |
| symbol | `grep -n -F "def worktree_of(" ops/desk/bare-guard.py` | 0 | `668:def worktree_of(cwd):` |
| callers | `grep -n -F "bash_rules(" ops/desk/bare-guard.py` | 0 | `1015:def bash_rules(command, s):` · `1141:        hit = bash_rules(command, seat(event))` |
| symbol | `grep -n -F "LAUNCHERS = " ops/desk/bare-guard.py` | 0 | `88:LAUNCHERS = ("claude", "codex", "grok", "agy")` |
| symbol | `grep -n -F "run_launch" ops/desk/desk-launch.sh` | 0 | `216` (comment) · `219:run_launch() {` · callers `386`, `407`, `546`, `618`, `1213`, `1224` |
| symbol | `grep -n -F "committed()" ops/desk/desk-launch.sh` | 0 | `183:committed() {` |
| pin | `grep -n -F "is none of build, check, deploy" ops/desk/desk-launch.sh tests/ops/test_desk_launch_devfix.py` | 0 | `desk-launch.sh:98` (header) · `desk-launch.sh:675` (refusal) · `test_desk_launch_devfix.py:383` (pin) |
| symbol | `grep -n -F "def worktree(" ops/desk/stop-guard.py` | 0 | `112:def worktree(cwd):` |
| symbol | `grep -n -F "CARD.search" ops/desk/stop-guard.py` | 0 | `152:    m = CARD.search(text or "")` · `405:    if text is not None and not CARD.search(text):` |
| desk allow | `grep -n -F "Bash(sh /Users/cobalt/.claude/ops/*)" /Users/cobalt/cobalt/.claude/settings.json` | 0 | `30:      "Bash(sh /Users/cobalt/.claude/ops/*)",` (card: `:29` at `d0a5fbb8`; one line lower at main HEAD, same string) |
| desk allow | `grep -n -F "claude stop" /Users/cobalt/cobalt/.claude/settings.json` | 0 | `20:      "Bash(claude stop *)",` (card: `:19`; same string) |
| sizes | `wc -l` | 0 | `desk-launch.sh` 1224 · `bare-guard.py` 1214 · `test_bare_guard.py` 1871 · `test_stop_guard.py` 774 |
| new files | `ls "docs/40 - DevDocs/prompts/OPS-HAND.md" tests/ops/test_desk_launch_ops_hand.py` | 1 | both `No such file or directory` (new in this build) |
| READ tail | `tail -n 3 …/reports/aset-orphan-answer-2026-10-10.md` | 0 | last line `FOR THE CHECK: aset-orphan brain 10-10 — AbandonProcessGroup true (plist:29) plus exec uv run (start_aset.sh:73) orphans python on bootout; …` |
| READ tail | `tail -n 3 …/reports/cto-2026-10-10.md` | 0 | last line `HANDOVER: predecessor 91f18257 → successor c3a40831 at 07:52 · pane w2:pV1` |
| restarts | `uv run cobalt jobs restarts 1eb47b59..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` (empty range) |

Read lines re-read from the files (Read tool): `bare-guard.py` 1-40, 77-88, 668-752, 1015-1043, 1131-1215 match the card's line numbers; `desk-launch.sh` 219-235, 308-320, 411-547 match (`:443`, `:493`, `:543` refusal texts as the card names); `stop-guard.py` 112-118, 384-411 match.

Card records copied: code read at `d0a5fbb8` 07:50-07:59 ET by the drafter; hook entry `~/.claude/settings.json` PreToolUse `bare-guard.py` on every Bash call; the 10-10 commands needing his hand (`kill 39280` R851, `kill -9 39280` R854, `launchctl kickstart` of aset R837); FIRST LIVE PROOF is the desk's after D1-D4; RESTARTS homes `OPS_DESK_PREFIX` / tests `:245` / `DOCS`; RESTARTS none expected; the seat's first Read is itself a prompt (NOT KNOWN). Re-read: the two `settings.json` lines above (one line lower at HEAD); the rest are the drafter's or the desk's facts, not re-readable by this list.

Header: the card carries no `DB:` line, so it is not a "DB: none" card; W runs the whole gate.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `1eb47b59` → `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 721.51s (0:12:01)`; 0 failed, 0 errors (skips include `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`, covered by the live-note run).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.79s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Test files written (no `src/`, no `ops/` edit): `tests/ops/test_bare_guard.py` (H1, H2; appended section `card 231 ops-hand`), `tests/ops/test_desk_launch_ops_hand.py` (NEW, H4 + H3), `tests/ops/test_stop_guard.py` (H5 pin). Offline, on `1eb47b59`:
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_ops_hand.py --tb=no -rfE` → `35 failed`. Every refusal case: exit 1 with `REFUSED: usage: desk-launch.sh <build|check|deploy|devfix|recut> <absolute card path> [PASS-2] [<resume step>]` (the `:655` usage line, no argument) or, with an argument, `REFUSED: kind 'ops-hand' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops` (`:675`); so the case's own reason is absent. The positive controls fail by exit code (`assert 1 == 0`). The three `test_h3_*` fail because `docs/40 - DevDocs/prompts/OPS-HAND.md` does not exist yet (H3 is written at E3).
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_bare_guard.py tests/ops/test_stop_guard.py -k "h1_ or h2_ or h5_" --tb=line -rfE` → `44 failed, 19 passed, 1779 deselected`. Every red's first line: `AssertionError: (0, '')` / `assert 0 == 2` (the guard let it through: seat `None`). Reds: H1 (a) `test_h1_the_ops_hand_seat_is_denied_production`, H1 (b) `test_h1_the_ops_hand_seat_is_denied_a_second_session`, all 8 H2 deny cases, `kill -2 2`, all 32 X1 spellings, the ledger G12 test. Green as named: negative controls (c) `test_h1_the_same_cwd_reading_another_prompt_is_unknown`, (d) `test_h1_a_later_message_naming_ops_hand_keeps_the_seats_own_kind[brain|build]`, the H2 brain control, the 4 H2 pass cases and 9 class shapes (exit 0 on BASE, as the card says), the G1 compound case, and the H5 pin `test_h5_the_ops_hand_seat_stops_freely` (green on BASE: a pin).
- No with-DB red (no lock take at E2). No RUN row has a test (H6 is the RESTARTS table).
- Commit `8fdd14d7 wip(ops-hand-1010): red — H1 H2 H4 tests, H5 pin`.

## E3 THE ROWS
Re-read before edit: `bare-guard.py` 731-752, 1015-1043; `desk-launch.sh` 308, 411-547, 549-619.
- H1 `ops/desk/bare-guard.py`: `seat()` gets `elif hub == OPS_HAND_FILE: kind = OPS_HAND` right after the hub kinds, before every cwd rule; G7 binds `kind == OPS_HAND` beside `WORKERS`; G2, G3 unchanged (kind not None, not deploy); G4 does not bind it (not in `GIT_SHAPED`); G1 unchanged.
- H2 `ops/desk/bare-guard.py`: rule G12 after G1 in `bash_rules`: `kind == OPS_HAND and not ops_class(command)` → `ROUTE["G12"]`, the card's line verbatim. `ops_class` reads the RAW text: `KILL` fullmatch `kill(?: -(?:TERM|15|KILL|9|0))? (?:[2-9]|[1-9][0-9]+)`; `KICKSTART` fullmatch `launchctl kickstart(?: -k)? gui/[0-9]+/com\.cobalt\.([A-Za-z0-9._-]+)` plus `os.path.isfile(REPO_ROOT/ops/com.cobalt.<label>.plist)`; reads: the text is `ps`, `pgrep`, `launchctl print` or starts with one of them plus a space. A quote, an expansion, a wrapper, a path verb, a second space or a second operand is not the plain shape → G12.
- H3 `docs/40 - DevDocs/prompts/OPS-HAND.md` (NEW): title carries `«INSTALL: his row»`; text per H3; ONE `claude --bg ` line, byte-equal to H3's (pinned by `test_h3_the_real_line_is_h3s_shape`).
- H4 `ops/desk/desk-launch.sh`: kind `ops-hand` after kind `brain` (so after the size guard `:318-320`); refusals in order: argument; not installed; `committed`; `«INSTALL`; not one `^claude --bg ` line; `--permission-mode` not once; `bypassPermissions` / `dangerously-skip-permissions`; mode not `default`; seat not named once; each of the 17 deny strings; allow set not exactly the four (also `--allowed-tools` / `--allowedTools=` spellings); the three copied gates with the prompt kind's own text (`:443`, `:493`, `:543`, stamp empty); `settings.local.json` present; check_paths; desk-list.sh unreadable; a live `ops-hand` row. Then `mkdir` of `<WT>/.ops-hand` (not in a dry run) and `run_launch`. Usage line `:308` names `ops-hand`; a header line under WHAT THE DESK TYPES. The `:675` text and header `:98` unchanged; the `prompt` kind unchanged.
- H5: no code change; the pin.
- Fix during E3 (said so): the first allow-set check failed the clean line because `tool_list … allow` prints the `--allowedTools` flag word itself; the awk now skips that word. Test rewritten: `test_h1_a_later_message_naming_ops_hand_keeps_the_seats_own_kind` stayed green for `build` under every mutation (a worker and ops-hand give the same answer to (a) and (b)), so it now also asserts `rm -f /tmp/x` is allowed (G12 for ops-hand).
- Greens after the rows: `tests/ops/test_bare_guard.py tests/ops/test_stop_guard.py` → `1842 passed`; `tests/ops/test_desk_launch_ops_hand.py` → `35 passed`; all `tests/ops` → `2799 passed, 1 xfailed, 15 warnings in 521.32s`; final row files + brain/devfix launcher neighbours → `1991 passed, 15 warnings in 108.72s`.

THE MUTATIONS (Edit tool, each undone with Edit; `git diff --stat` after the last undo → only the fix: `bare-guard.py | 37`, `desk-launch.sh | 87`, `test_bare_guard.py | 2`; `stop-guard.py` absent):

| # | row | mutation | run | result, first failing line |
|---|---|---|---|---|
| M1 | H1 undo | `elif False and hub == OPS_HAND_FILE:` | `-k "h1_ or h2_"` | `44 failed, 18 passed`; `AssertionError: (0, '')` (both H1 reds, all G12 denies) |
| M2 | H1 control (c) | kind also by `cwd.endswith("/.ops-hand")` | `-k h1_` | `1 failed, 4 passed`: `test_h1_the_same_cwd_reading_another_prompt_is_unknown`, `AssertionError: route: the desk launches` |
| M3 | H1 control (d) | kind also by `OPS-HAND.md` anywhere in the transcript (after the hub kinds) | `-k h1_` | `1 failed, 4 passed`: `…keeps_the_seats_own_kind[brain]`; `[build]` stayed green → test rewritten (above) |
| M3b | H1 control (d) | the any-message check BEFORE the hub kinds | `-k h1_` (rewritten test) | `2 failed, 3 passed`: `[brain]` and `[build]`, `AssertionError: route: ops-hand runs only its class …` |
| M4 | H2 undo | `if False and kind == OPS_HAND and not ops_class(…)` | `-k "h1_ or h2_"` | `42 failed, 20 passed`; every H2 deny and X1 case |
| M4b | H2 pass | `ops_class` always False | `-k "h2_a_command_of_the_class_passes or h2_every_class_shape"` | `13 failed, 1 passed` (the 1 = `kill -2 2`, a deny) |
| M5 | H2 control | G12 for every kind (`if not ops_class(…)`) | `-k h2_the_same_kill_from_a_brain` | `1 failed`: `AssertionError: route: ops-hand runs only its class …` |
| M6 | H1 G7 | `(kind in WORKERS or False)` | `-k h1_` | `1 failed, 4 passed`: (b) `assert 'route: ops-h...e is a card\n' == 'route: the desk launches\n'` |
| M7 | H2 plist | kickstart `return True or os.path.isfile(…)` | `-k h2_` | `1 failed, 56 passed`: `x1…[launchctl kickstart -k gui/501/com.cobalt.nosuch]` |
| M8 | H4 undo | `if [ "$kind" = "ops-handX" ]` | launcher file | `34 failed, 1 passed` (the 1 = `test_h3_the_real_line_is_h3s_shape`, which reads the file, not the launcher) |
| M9 | H4 mode gate | `true || [ "$pm" = "default" ] || refuse` | launcher file (with M10) | `test_mode_auto_is_refused`: `assert 0 == 1` (the auto line dry-ran) |
| M10 | H3 | `OPS-HAND.md` mode `default` → `auto` | launcher file (with M9) | `test_h3_the_real_line_is_h3s_shape` and `test_h3_the_real_file_passes_once_his_row_fills_the_title` red (`- sion-mode default … + sion-mode auto`); `3 failed, 32 passed` total |
| M11 | H5 pin | `stop-guard.py:405` `if False and text is not None …` | `-k h5_` | `1 failed`: `assert (2, '', 'NOT ...then stop.\n') == (0, '', '')` |

DevDocs: no page for `bare-guard.py` or `desk-launch.sh` under `docs/40 - DevDocs/cobalt/` (`grep -rln -F "bare-guard" "docs/40 - DevDocs/cobalt"` → nothing; `desk-launch` only in `cobalt/jobs/restarts.md`, which is `restarts.py`'s page); none created (as guard-d2's build, its ASK DESK 1). See `## RECORDS`.

Commit `2cb7a9ad feat(ops-hand-1010): ops-hand seat kind, G12 closed class, OPS-HAND.md, launcher kind (H1-H5, L63 D1-D4 his, L3, L42)`.

## RESTARTS
`uv run cobalt jobs restarts 1eb47b59..HEAD` (08:45 ET), whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/OPS-HAND.md	A	DOCS	-
docs/40 - DevDocs/reports/ops-hand-build-2026-10-10.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_ops_hand.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row; every label is the card's expected class home (H6).

## W THE THREE SUITES
`<tip>` = `2cb7a9ad`. The card has no `DB:` header, so the whole gate ran. `sh /Users/cobalt/cobalt/ops/desk/gate.sh ops-hand-1010 all --deploy`: no `--deselect`, because this build adds no with-DB test; no `--tickers`; no `--migration`. Exit 0. Verdict lines, whole:
```
offline 4196/0
lock: waited 38 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/ops-hand-1010-all-20261010-084612.log
```
No line is marked `OUTSIDE the allowed set`.
- (a) offline: `4196 passed, 800 skipped, 1 xfailed, 36 warnings in 698.25s` (log :879) → `<p>` = 4196. This build adds no test under `tests/cobalt` or `tests/taxonomy`; its tests are under `tests/ops` (2799 passed, 1 xfailed, at E3).
- (b) the lock was taken (`lock taken: ops-hand-1010`, log :885) after a wait of 38 min. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :896); the proof-only gave `LEVEL 0013`.
- (c) PASS 1, whole (deploy), the executed command (log :952), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py` → `4888 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 793.47s` (log :1108) → `<d1>` = 4888. The 7 skips are the 7 SKIPPED lines above, each with its reason; none is outside the allowed set.
- (c2) `dev forward: APPLIED 09:49:30` (log :1110); `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (log :1188).
- (c3) PASS 2: `205 passed, 1 deselected, 5 warnings in 228.28s` (log :1962) → `<d2>` = 205. This build has no with-DB test id to name. `<d>` = 4888 + 205 = 5093, the same as the gate's `with-DB 5093/0`.
- (c3r) `stray rows: not read (no --tickers given)`: this build writes no ticker.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :2030) equals F0 in every field, so **`cobalt_dev: 0013 — F2 = F0`**. Then `release-devdb-lock.sh ops-hand-1010` → `lock released` (log :2083-2084); `ls /Users/cobalt/cobalt-wt/ops-hand-1010/.env` → `No such file or directory`, so **`.env: removed, proven gone (W)`**.
- (e) live-note: `146 passed, 1 skipped, 15 warnings in 27.07s` (log :2153) → `<l>` = 146. The skip is `test_replay_line.py:266`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red for its named reason. E2 reds on BASE: 35 launcher cases (the `:655`/`:675` refusal, the missing OPS-HAND.md) and 44 guard cases (`AssertionError: (0, '')`). The controls and pass cases that are green on BASE were reddened by their mutation: (c) by M2; (d) by M3b, after the test was rewritten when M3 left `[build]` green; the brain control by M5; the pass cases by M4b; `nosuch` by M7; the H5 pin by M11; the H3 tests by M10. The only test no mutation reddened at E3 is `test_h3_the_real_line_is_h3s_shape` under M8; M10 reddens it.
(2) Every entry path is pinned. The callers of `seat()` (PREFLIGHT, re-read at the tip): `:1172` (`bash_rules`) is pinned by every H1/H2 test. `:1182` (`decide`, Write/Edit) is not pinned for kind `ops-hand`: DECISION 2. The callers of `run_launch` are unchanged; the new call is pinned by `test_a_clean_fixed_file_launches_from_the_seat_dir_it_makes`. Cwd states covered: `<wt>/.ops-hand` (dot-name skip), the repo (brain), a worktree (build). Message states covered: first message, later message, another prompt. Spelling edge inputs: X1, 32 cases. Launcher states covered: every refusal, a dry run, a real run, and a live/unreadable list.
(3) Everything in this report was re-read from tool output at the tip `2cb7a9ad`: `grep -n -F "OPS_HAND" ops/desk/bare-guard.py` → `:97`, `:98`, `:760-761`, `:1054`, `:1059`; `grep -n -F "ops-hand" ops/desk/desk-launch.sh` → `:37-38`, `:311`, `:624-702`; `grep -rn -F "seat(" ops/desk/bare-guard.py` → `:747`, `:1172`, `:1182`; `grep -c -F "claude --bg " …/OPS-HAND.md` → `1`. The gate figures were grepped from the log (line numbers above).

## FOR THE CHECK
- Range `1eb47b59..2cb7a9ad`: `8fdd14d7 wip(ops-hand-1010): red — H1 H2 H4 tests, H5 pin`; `2cb7a9ad feat(ops-hand-1010): ops-hand seat kind, G12 closed class, OPS-HAND.md, launcher kind (H1-H5, L63 D1-D4 his, L3, L42)`.
- Per row, the reds, mutations and greens are under `## E2 RED` and `## E3 THE ROWS` (table M1-M11).
- Caller greps: under `## PREFLIGHT`, and under self-check (3) as re-read at the tip.
- RUN row H6: the RESTARTS table, whole, under `## RESTARTS`.
- The three suites, with the pass 1 command, are under `## W`. F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `908 45 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. Lock: taken after waiting 38 min (log :885, :888), released at log :2084 after `dev forward: APPLIED 09:49:30`; gate log `/Users/cobalt/cobalt-wt/.gate-logs/ops-hand-1010-all-20261010-084612.log`.
- The records copied at PREFLIGHT are under `## PREFLIGHT`.
- For X1: G12 reads the raw text with `re.fullmatch`. A wrapper (`env`, `command`, `nohup`), a path verb, quoting (`'…'`, `$'…'`), a brace word, `-s KILL`, `-n 9`, `--`, a leading zero, a second operand, `%job`, `$PID` or a double space each fail the plain shape → G12 (pinned in `test_h2_x1_any_other_spelling_is_denied`). Compound forms are G1's to deny first (`test_h2_a_compound_command_is_g1s_to_deny_first`).
- For X2: the kind comes from `first_message()` (the first non-meta user record), the first `Read '…'` in it, by basename. A later message never sets it: test (d) and M3/M3b.
- For X3: the launcher neighbours were unchanged and green: `test_desk_launch_brain.py` and `test_desk_launch_devfix.py` ran in the 1991-passed run, the `:675` text and header `:98` were not touched, and the `prompt` kind block is byte-unchanged (`git diff 1eb47b59 -- ops/desk/desk-launch.sh` adds lines only after kind `brain`, plus the usage line and three header lines).
- For X4: the read verbs are `ps`, `pgrep` and `launchctl print` plus arguments. G1 still denies a redirect, pipe, `$(` or backtick before G12 runs. The launch line denies Write, Edit, NotebookEdit, Agent and the rest of the 17 strings; the launcher refuses a line that lacks any of them.

## CONTINUE
next: none — run complete (the desk launches the check)

## DECISIONS
- DECISION 1 (FOR DEJAN): the R686 production read for the ops-hand seat. H1 says "G3 and G2 as for every seat (the R686 production `db query` read still passes)". H2 says every call outside the class is exit 2. Default taken: G2 lets the read through (G2's answer is unchanged), and G12 then denies it, because it is not in the class. Pinned by `test_h2_x1_any_other_spelling_is_denied[COBALT_ENV=production uv run cobalt db query --prod --side user "SELECT 1"]`. A seat-wide read for ops-hand would mean widening the class, which is his row (D3).
- DECISION 2: a caller no test pins. `decide()` `:1182` (Write/Edit) for kind `ops-hand` meets G6 and G5's fixed-file rule only (the kind is neither a worker nor brain), with no fence. Before this build the seat was kind `None`, with no G5 at all. Write, Edit and NotebookEdit are denied on the launch line. Default taken: left as built, not pinned; the check decides whether a fence is owed.
- DECISION 3: refusals added beyond the card's list, all stricter: `--dangerously-skip-permissions` alongside `bypassPermissions`; the `--allowed-tools` and `--allowedTools=` spellings under the allow gate; `check_paths`; an unreadable desk-list.sh, as kind `brain` does. Also, OPS-HAND.md tells the seat to ask the desk for the `ps` line when a `kill` arrives without one, and to run nothing until then. Default taken: kept.

## RECORDS
- CONTINUED / REFUSED: none. No extra lock take: one take, inside the gate.
- L74: one system block asked for a `Claude-Session:` commit line (`## L74`); not acted on. BASE `1eb47b59` itself carries such a line (`git show --stat`), which is data.
- Card records re-read at PREFLIGHT: `settings.json` holds `Bash(sh /Users/cobalt/.claude/ops/*)` at `:30` and `Bash(claude stop *)` at `:20` at main HEAD; the card cites `:29` and `:19` at `d0a5fbb8`. Same strings, one line lower.
- Card fact corrected by tool output: on BASE, `desk-launch.sh ops-hand` with no argument refuses with the `:655` usage line, not `:675`; `:675` appears only with an argument. Each refusal test asserts its own reason, so both are red on BASE.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` for `bare-guard.py` or `desk-launch.sh`, so none was created (the guard-d2 build did the same, its ASK DESK 1).
- The gate waited 38 min for the `cobalt_dev` lock (another session held it).
- Context at the last step: `desk-context.sh` → `context 279960 of 400000 — ok`, above the desk's 250,000 line (UNATTENDED RULES (c)).
- Not proven here (the card's NOT KNOWN): whether `--remote-control` relays a default-mode permission prompt to his phone. That is the desk's first live proof after D1-D4.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: ops-hand-1010 · tip: 2cb7a9ad | on 1eb47b59 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 3 · for Dejan: 1 · tokens: 279960
