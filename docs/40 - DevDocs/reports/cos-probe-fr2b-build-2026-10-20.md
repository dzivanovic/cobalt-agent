# cos-probe-fr2b — build report (2026-10-20)

## §0 Headline
- Card 918's diff re-applied by Edit on BASE `656f2ca1`: the three spec files at tip `9b912c83` match `dfea631a` byte for byte (E1 (b) empty). No other code moved (E1 (c) empty).
- P1 red on BASE's `probe.py` (12 failed, the four named reds for the card's reasons); green after P2 (40 passed); six mutations, each red.
- Gate on `9b912c83`: offline 4897/0 · with-DB 5869/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`. One SLOTS SELF-HEAL (`user.aset_sizings` 1546 → 54) before the second gate call.
- RESTARTS: com.cobalt.radar. One decision: the `FileNotFoundError` branch of `_auth_exit` has no test. Not Dejan's.

## L74
- The session's harness reminder asked for a `Claude-Session:` line in commits. Recorded once as data (L74); acted on none. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md" · 0 · a6ce8042c88b016cf77b1e8246602fc1c36ab1ab
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/923-cos-probe-fr2b-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Tue Oct 20 15:06:50 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cos-probe-fr2b
    ?? "docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 656f2ca1 docs(desk): R2190 amend drafted, preflight r2 366fc707 live
diff · git diff --stat 656f2ca1 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-probe-fr2b · 0 · 656f2ca1 docs(desk): R2190 amend drafted, preflight r2 366fc707 live
env here · ls /Users/cobalt/cobalt-wt/cos-probe-fr2b/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 656f2ca1` | 0 | `656f2ca1 docs(desk): R2190 amend drafted, preflight r2 366fc707 live` · `docs/40 - DevDocs/reports/cto-2026-10-20.md | 7 ++++---` · 1 file changed, 4 insertions(+), 3 deletions(-) |
| symbol | `grep -n -F "under the scratch HOME" src/cobalt/cos/probe.py` | 0 | `454:                    return False, f"auth: claude auth status exit {code} under the scratch HOME"` |
| symbol | `grep -n -F ".claude.json" src/cobalt/cos/probe.py` | 0 | `12:    \`finally\`. His \`~/.claude.json\` and \`~/.claude/\` are never touched.` · `298:    (root / "home" / ".claude.json").write_text(json.dumps({"mcpServers": {PLANTED_SERVER: {` |
| symbol | `grep -n -F "def test_the_spawn_runs_under_a_scratch_home_never_the_real_one" tests/cobalt/test_cos_probe.py` | 0 | `288:def test_the_spawn_runs_under_a_scratch_home_never_the_real_one(rig, monkeypatch, capsys, tmp_path):` |
| symbol | `grep -n -F "## 2026-10-20 — cos-probe-fr1 (check)" "docs/40 - DevDocs/cobalt/cos/README.md"` | 0 | `49:## 2026-10-20 — cos-probe-fr1 (check)` |
| wc | `wc -l` the three row files | 0 | `472 src/cobalt/cos/probe.py` · `502 tests/cobalt/test_cos_probe.py` · `50 docs/40 - DevDocs/cobalt/cos/README.md` |
| spec base | `git diff --stat 27c35e37 HEAD --` the three paths | 0 | nothing (main's three files = the spec's base) |
| spec | `git diff 27c35e37..dfea631a --` the three paths | 0 | read whole (README +6; probe.py 81+/30−; test_cos_probe.py 147+/14−) |
| READ tail | `tail -n 3 …/reports/cos-probe-fr2-check-2026-10-20.md` | 0 | `CHECK DONE · job: cos-probe-fr2 · pass: 1 · tip: dfea631a · … · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 178055` |
| READ tail | `tail -n 3 …/reports/deploy-cos-probe-fr2.md` | 0 | `FAILED: 4.7 (d) — marker 4 \`grep -c -F "## 2026-10-20 — cos-probe-fr2" README.md\` read 2, card after 1 (the string also matches the check's heading) · rollback: used — … · decisions: 1 · for Dejan: 0 · tokens: 229692` |
| record | `git merge-base --is-ancestor dfea631a HEAD` | 0 | (no output; ancestor, as the card's record says) |
| RESTARTS | `uv run cobalt jobs restarts 656f2ca1..HEAD` | 0 | `docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.md A DOCS -` · `RESTARTS: none` (the empty commit range; the tool listed the untracked report) |

Card `## RECORDS`, copied and re-read where the list can: PURE RE-APPLICATION re-read (`git diff --stat 27c35e37 HEAD` over the three paths → nothing); `merge-base --is-ancestor dfea631a HEAD` re-read → exit 0; MARKERS before re-read (1, 2 present at `:454`, `:12`/`:298`; the H1 test name absent; README's last section `cos-probe-fr1 (check)`); RESTARTS carried (`com.cobalt.radar`), re-derived at R1; RULINGS R1863 re-read by `authorize.sh`. The drafter's BASE `be5fc23d` was reset by the desk to `656f2ca1` (card header).

PROVEN BY FIRST REAL USE: CLASS (a) at AUTHORIZATION (ran); `uv run pytest` / `COBALT_LIVE_VAULT_ROOT=… uv run pytest` at E0 (ran); `git add` / `git commit` at E2 (ran); the with-DB strings at W's gate (no E2 with-DB red in this job).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4886 passed, 878 skipped, 4 xfailed, 36 warnings in 740.00s (0:12:19)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.81s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (not `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
P1: `tests/cobalt/test_cos_probe.py` brought to `dfea631a`'s bytes with the Edit tool, hunk by hunk; `git diff --stat dfea631a -- tests/cobalt/test_cos_probe.py` → nothing. RUN on BASE's `probe.py`: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py` → `12 failed, 28 passed in 2.26s` (rerun with `--tb=line`: `12 failed, 28 passed in 2.07s`). The four named reds, first lines:
- `test_auth_runs_under_the_real_home_and_a_login_there_passes` → `AssertionError: ['PROBE X11 FAIL auth: claude auth status exit 1 under the scratch HOME']` (:445).
- `test_a_missing_home_is_refused` → `AssertionError: [['claude', 'auth', 'status']]` (:455; the auth stub is reached).
- `test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home` → `AssertionError: the spawn runs under the real HOME` · `+ c0000gn/T/cos-probe-psw83k8_/home` (:302; env HOME is the scratch home).
- `test_auth_quotes_logged_in_and_method_only` → `AssertionError: PROBE X11 FAIL auth: claude auth status exit 1 under the scratch HOME` (:474).
Also red: `test_each_pass_rule_fails_on_its_own_breach` (:284, X2 'planted' — the test's plant reader now reads `work/.mcp.json`), `test_auth_failure_is_a_fail_line_and_nothing_spawns` (:417), `test_a_home_that_is_not_a_directory_is_refused` (:463), `test_auth_quote_line_on_an_ok_run` (:486 IndexError, no AUTH stderr line), `test_auth_quote_unreadable_values_are_unread` ×3 (:499), `test_auth_quote_a_value_with_a_trailing_newline_is_unread` (:627). Green on BASE: the H4 control `test_the_probe_opens_no_file_under_the_real_home` (card 918 H4 allows it) and `test_x2_a_write_over_the_plant_is_a_written_file` (BASE plants in `home/`, so any `.mcp.json` in the cwd is a written file); both shown red under their E3 mutations.
Commit `2208f9bf wip(cos-probe-fr2b): red — test_cos_probe.py ported byte-equal to dfea631a (P1)`.

## E3 THE ROWS
- P2: `src/cobalt/cos/probe.py` brought to `dfea631a`'s bytes with the Edit tool (10 hunks). D0: the README's two sections appended unchanged. `git diff --stat dfea631a --` the three paths → nothing.
- Green: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py` → `40 passed in 2.49s`.
- Card offline suite: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` → `74 passed in 4.67s`; after the mutations were undone, `74 passed in 4.70s`.
- No dated DevDocs line of this job's own: D0 is the record (the card's row D0).

THE MUTATIONS (each made and undone with the Edit tool, `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_cos_probe.py`):
| # | mutation | summary | first failing line |
|---|---|---|---|
| M1 (H1) | `_probe_env` sets `env["HOME"] = tempfile.gettempdir()` | `2 failed, 38 passed` | `test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home` `:302 AssertionError: the spawn runs under the real HOME`; `test_auth_runs_under_the_real_home_and_a_login_there_passes` `:445` |
| M2 (H2) | both HOME refusals `if False:` | `2 failed, 38 passed` | `test_a_missing_home_is_refused` `:455 AssertionError: [['claude', 'auth', 'status']]`; `test_a_home_that_is_not_a_directory_is_refused` `:463` |
| M3 (H3) | `_auth_quote` loops `list(data) or AUTH_KEYS` | `3 failed, 37 passed` | `test_auth_quotes_logged_in_and_method_only` `:474 … (loggedIn=false authMethod=none email=unread orgId=constructed-org)`; `test_auth_quote_line_on_an_ok_run` `:486`; `test_auth_quote_unreadable_values_are_unread[{"authMethod": 7}]` `:499` |
| M4 (O1) | `_AUTH_VALUE.match` for `fullmatch` | `1 failed, 39 passed` | `test_auth_quote_a_value_with_a_trailing_newline_is_unread` `:627 … (loggedIn=false authMethod=none )` |
| M5 (O2) | entries filter `if p.name not in before` | `1 failed, 39 passed` | `test_x2_a_write_over_the_plant_is_a_written_file` `:635 AssertionError: ('X2', 'PROBE X2 OK no process, …` |
| M6 (H4 control) | `_probe_env` opens `$HOME/.claude.json` | `1 failed, 39 passed` | `test_the_probe_opens_no_file_under_the_real_home` `:529 AssertionError: ['/private/var/…/real-home/.claude.json']` |
After M6's undo: `git diff --stat dfea631a --` the three paths → nothing; `git diff --stat` → the two port files only (`README.md | 6 ++`, `probe.py | 111`).
Commit `9b912c83 fix(cos-probe-fr2b): port probe.py and the cos README byte-equal to dfea631a (P2, D0; L3, L72)`.

E1 (RUN, on `9b912c83`):
(a) `git diff --stat 27c35e37 9b912c83 --` the three paths:
```
 docs/40 - DevDocs/cobalt/cos/README.md |   6 ++
 src/cobalt/cos/probe.py                | 111 +++++++++++++++++------
 tests/cobalt/test_cos_probe.py         | 161 ++++++++++++++++++++++++++++++---
 3 files changed, 234 insertions(+), 44 deletions(-)
```
`git diff --stat 27c35e37 dfea631a --` the three paths: the same four lines, line for line.
(b) `git diff dfea631a 9b912c83 --` the three paths → nothing.
(c) `git diff --stat dfea631a 9b912c83 -- src tests configs ops` → nothing.

DEPLOY PROOF on the worktree tree (the card's paths read under `/Users/cobalt/cobalt` after deploy): `grep -c -F "under the scratch HOME" src/cobalt/cos/probe.py` → `0`; `grep -c -F ".claude.json" src/cobalt/cos/probe.py` → `0`; `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes" tests/cobalt/test_cos_probe.py` → `1`; `grep -c -F "## 2026-10-20 — cos-probe-fr2" "docs/40 - DevDocs/cobalt/cos/README.md"` → `2`. Each equals the card's `after`.

## RESTARTS
R1: `uv run cobalt jobs restarts 656f2ca1..HEAD` (HEAD `9b912c83`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2b-build-2026-10-20.md	A	DOCS	-
src/cobalt/cos/probe.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No UNCLASSIFIED row; the header's `RESTARTS: com.cobalt.radar` matches.

## W THE THREE SUITES
`<tip>` = `9b912c83`. No with-DB test, migration or ticker in this build: no `--deselect`, `--tickers` or `--migration`.

FIRST CALL `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-probe-fr2b all --deploy` → exit 1, whole:
```
tests/ops: skipped (no ops paths)
offline 4897/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
RED (exit 3): no pytest summary line
Exit: cobalt_dev column slots: user.aset_sizings 1546 of 1600 — run a devfix (cobalt db dev-rebuild user.aset_sizings) before any with-DB gate
! _pytest.outcomes.Exit: cobalt_dev column slots: user.aset_sizings 1546 of 1600 — run a devfix (cobalt db dev-rebuild user.aset_sizings) before any with-DB gate !
.env: removed
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr2b-all-20261020-152414.log
```
A slot-guard exit → SLOTS SELF-HEAL (THE LOCK). The gate had already released the lock, so the heal ran in one by-hand take (`## RECORDS`):
- `sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh cos-probe-fr2b 90` → `lock taken: cos-probe-fr2b` (exit 0). `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/cos-probe-fr2b/.env`.
- `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` (= the first gate's `F0`, log `:974`).
- `COBALT_ENV=dev uv run cobalt db dev-rebuild user.aset_sizings --dry-run` → `DRY RUN — ROLLED BACK · max_attnum 1546 → 54 · rows 1 = 1 · catalog digest equal`.
- `COBALT_ENV=dev uv run cobalt db dev-rebuild user.aset_sizings` → `REBUILT user.aset_sizings · max_attnum 1546 → 54 · rows 1 = 1 · catalog digest equal`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `NOTHING WAS APPLIED` · `SLOTS ok · highest user.card_stop_edits 1006 of 1600` · `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `TABLES 0011` (the tool prints no `LEVEL` line. The gate's own proof-only read `LEVEL 0013` both times).
- `sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh cos-probe-fr2b` → `lock released`; `ls /Users/cobalt/cobalt-wt/cos-probe-fr2b/.env` → No such file. Released 15:37 (`date` 15:37:24).

SECOND CALL, the same command → exit 0, whole:
```
tests/ops: skipped (no ops paths)
offline 4897/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5869/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr2b-all-20261020-153727.log
```
`grep -n -F "OUTSIDE" <log>` → nothing: no skip outside the allowed set.
- (a) offline: log `:956` `4897 passed, 878 skipped, 4 xfailed, 36 warnings in 719.94s (0:11:59)` → `offline 4897/0`; `tests/ops: skipped (no ops paths)`. Tests this build adds or renames (all in `tests/cobalt/test_cos_probe.py`): `test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home`, `test_auth_runs_under_the_real_home_and_a_login_there_passes`, `test_a_missing_home_is_refused`, `test_a_home_that_is_not_a_directory_is_refused`, `test_auth_quotes_logged_in_and_method_only`, `test_auth_quote_line_on_an_ok_run`, `test_auth_quote_unreadable_values_are_unread` (×3), `test_the_probe_opens_no_file_under_the_real_home`, `test_auth_quote_a_value_with_a_trailing_newline_is_unread`, `test_x2_a_write_over_the_plant_is_a_written_file`.
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:974`); `LEVEL 0013` (`:1029`).
- (c) pass 1 (`:1030` `pass 1: whole (deploy)`), the executed command (`:1032`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py` → `:1200` `5625 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 884.65s (0:14:44)` → `<d1>` 5625.
- (c2) `:1202` **`dev forward: APPLIED 16:04:38`** (the standing FORWARD of `gate-lists.md`, no migration of this build); `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1286`).
- (c3) pass 2 (`:1288`, the PASS 2 command of `gate-lists.md`, nothing added for this build) → `:2182` `244 passed, 1 deselected, 5 warnings in 238.01s (0:03:58)` → `<d2>` 244; `<d>` = 5625 + 244 = 5869 = `with-DB 5869/0`.
- (c3r) `stray rows: not read (no --tickers given)`: this build writes no ticker.
- (f) ROLLBACK `:2186` `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013`; `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2256`) = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`**. Release `:2311`–`:2312` `lock released`; `.env: removed`.
- (e) live-note `:2383` `148 passed, 1 skipped, 15 warnings in 26.66s` → `live-note 148/0`; the one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. E2 (BASE `probe.py`): 12 reds, first lines quoted under `## E2 RED`. E3 mutations M1–M6: each test green on BASE went red under its mutation (H4 control under M6 `:529`, the O2 test under M5 `:635`). The O1 test went red under M4 (`:627`), the H1–H3 tests under M1–M3. No test stayed green under its mutation.
(2) Callers (`grep -rn -F "<fn>(" src`): `_probe_env` ← `probe.py:501` (`_verdict`; pinned by the M1, M2 tests); `_auth_exit` ← `probe.py:502` (pinned by every `_probe` test through the `subprocess.run` stub); `_auth_quote` ← `probe.py:178` (pinned by the M3, M4 tests) and `probe.py:177`, the `FileNotFoundError` branch, which no test reaches → `## DECISIONS` 1; `_plant` ← `probe.py:361` (`_live_scratch`, M5 test) and `:392` (`_x11`, `test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home` asserts the plant). Item paths X2, X10, X11, X12 are run by the H4 control and the scenarios. HOME unset and HOME not a directory are pinned by the M2 tests.
(3) Re-read at tip `9b912c83`: E1 (a)–(c) run on `9b912c83`; the four DEPLOY PROOF greps and the four caller greps were run after the fix commit, with no code commit since; `git log --oneline 656f2ca1..HEAD` → `9b912c83`, `2208f9bf`; the gate log lines were re-read by `grep -n -F` / Read at the line numbers cited.

## FOR THE CHECK
- Range `656f2ca1..9b912c83`: `2208f9bf wip(cos-probe-fr2b): red — test_cos_probe.py ported byte-equal to dfea631a (P1)` · `9b912c83 fix(cos-probe-fr2b): port probe.py and the cos README byte-equal to dfea631a (P2, D0; L3, L72)`. Then the report commit.
- Per row: P1 red `12 failed, 28 passed` (E2); P2 green `40 passed`; card offline suite `74 passed`; mutations M1–M6 (E3 table); D0 = the README bytes (E1 (b)).
- E1 (RUN) whole under `## E3`; R1 (RUN) whole under `## RESTARTS`.
- Caller greps: PRE-STOP (2).
- Suites: offline 4897/0, with-DB 5869/0 (5625 + 244), live-note 148/0; the commands are under `## W`.
- Fingerprints: by-hand heal take F0 = `664 35 272c95bbb12241e3611e4b36326ccf87`; second gate F0 `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `954 47 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 `664 35 272c95bbb12241e3611e4b36326ccf87`.
- Lock: first gate taken and released inside `gate.sh` (log `…-152414.log`); by-hand take 15:36–15:37 (`date` 15:36:39 before, 15:37:24 after); second gate taken (`:963`, waited 0 min) and released (`:2312`) inside `gate.sh`, forward applied 16:04:38.
- X4 at tip: `grep -c -F ".claude.json" src/cobalt/cos/probe.py` → `0`; the H4 control's mutation (M6) red.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. `probe.py:177`: when `claude` is not on PATH, `_auth_exit` returns `127, _auth_quote("")` and no test reaches that branch (PRE-STOP (2)). It is card 918's code, unchanged by this port. The card fences off any test-file line that differs from `dfea631a`, so no test was added. UNPROVEN (L70). Safe default taken: carried as is for the check to weigh. Not Dejan's.

## RECORDS
- Started 15:06:39 EDT (`date`).
- L74: the harness reminder asked for a `Claude-Session:` line. Recorded once under `## L74`; not followed.
- `git merge-base --is-ancestor dfea631a HEAD` typed at PREFLIGHT to re-read the card's record. It is not a listed string, but it ran (exit 0, no output).
- One extra lock take (by hand, 15:36–15:37) for SLOTS SELF-HEAL: `user.aset_sizings` rebuilt on `cobalt_dev`, max_attnum 1546 → 54, rows 1 = 1, catalog digest equal. Fingerprint unchanged. One more gate call followed (W's second call). The gate released the lock after its slot-guard exit, so "in the SAME lock take" could not hold; the heal took its own lock.
- `.env: removed, proven gone (W self-heal take)`; `.env: removed, proven gone (W second gate)`.
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cos-probe-fr2b · tip: 9b912c83 | on 656f2ca1 | migration: none | offline 4897/0 | with-DB 5869/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 166019
