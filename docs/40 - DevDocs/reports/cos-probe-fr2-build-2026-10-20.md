# cos-probe-fr2 — build report (2026-10-20)

## §0 Headline
- BUILT `74169800` on `27c35e37`: `cobalt cos probe` runs under the real HOME with a scratch cwd `<root>/work/`; the plant is a cwd `.mcp.json`; the auth check quotes `loggedIn` and `authMethod` only.
- Rows H1–H4, R1, D0 built; every red shown on BASE, every mutation red.
- Gate green: offline 4895/0 · with-DB 5867/0 · live-note 148/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS `com.cobalt.radar`.
- Two ASK DESK items, each with the card's default taken; none for Dejan.

## L74
- The session's attribution reminder asked for a `Claude-Session:` line in commits. Recorded as DATA (BUILD-HUB L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md"` (12:38 EDT) → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md" · 0 · c26575dd5ea1f2d94652bcd9bd54ff75dc024c60
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/918-cos-probe-realhome-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted below |
| BASE | `git show --stat 27c35e37` | 0 | `docs(desk): R2178 cos-probe-fr2 preflight launched` · `docs/40 - DevDocs/reports/cto-2026-10-20.md \| 5 +++--` · `1 file changed, 3 insertions(+), 2 deletions(-)` |
| symbol | `grep -n -F "def _auth_exit" src/cobalt/cos/probe.py` | 0 | `130:def _auth_exit(cwd: Path) -> int:` |
| symbol | `grep -n -F "def _scratch" src/cobalt/cos/probe.py` | 0 | `167:def _scratch():` |
| symbol | `grep -n -F "def _probe_env" src/cobalt/cos/probe.py` | 0 | `179:def _probe_env(home: Path, extra: dict[str, str]) -> dict[str, str]:` |
| symbol | `grep -n -F "def _plant" src/cobalt/cos/probe.py` | 0 | `293:def _plant(root: Path) -> Path:` |
| symbol | `grep -n -F "def _verdict" src/cobalt/cos/probe.py` | 0 | `437:def _verdict(item: str) -> tuple[bool, str]:` |
| symbol | `grep -n -F ".claude.json" src/cobalt/cos/probe.py` | 0 | `12:` (docstring), `298:    (root / "home" / ".claude.json").write_text(...` |
| symbol | `grep -n -F "under the scratch HOME" src/cobalt/cos/probe.py` | 0 | `454:                    return False, f"auth: claude auth status exit {code} under the scratch HOME"` |
| symbol | `grep -n -F "ALLOWED_ENV = " src/cobalt/cos/session.py` | 0 | `54:ALLOWED_ENV = ("PATH", "HOME", "USER", "LANG", "COBALT_ENV")` |
| symbol | `grep -n -F "def child_env" src/cobalt/cos/session.py` | 0 | `93:def child_env(parent: Optional[dict] = None) -> dict[str, str]:` |
| symbol | `grep -n -F "def _scrubbed_environ" src/cobalt/cos/session.py` | 0 | `118:def _scrubbed_environ(env: dict[str, str]):` |
| callers | `grep -rn -F "_probe_env(" src` | 0 | `probe.py:179` (def), `probe.py:451` (`_verdict`) |
| callers | `grep -rn -F "_auth_exit(" src` | 0 | `probe.py:130` (def), `probe.py:452` (`_verdict`) |
| callers | `grep -rn -F "_plant(" src` | 0 | `probe.py:293` (def), `probe.py:314` (`_live_scratch`), `probe.py:342` (`_x11`) |
| callers | `grep -rn -F "_scratch(" src` | 0 | `probe.py:167` (def), `probe.py:449` (`_verdict`); other hits are `_live_scratch`, `voice/scratch.py`, `classify/config.py` (unrelated names) |
| callers | `grep -rn -F "cos.probe" src` | 0 | `probe.py:434` (the ITEMS assert) only |
| size | `wc -l` | 0 | `472 src/cobalt/cos/probe.py` · `502 tests/cobalt/test_cos_probe.py` · `50 docs/40 - DevDocs/cobalt/cos/README.md` |
| READ tail | `tail -n 3 …/cos-gate-run-2026-10-20.md` | 0 | `GATES DONE · ok: 5 · fail: 6 · not run: 3` |
| READ tail | `tail -n 3 …/cos-probe-fr1-check-2026-10-20.md` | 0 | `CHECK DONE · job: cos-probe-fr1 · pass: 1 · tip: da47500a · … · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 181890` |
| READ tail | `tail -n 3 …/draft-cos-gate-rerun-2026-10-20.md` | 0 | `DRAFTED · decisions: 5` |
| RESTARTS empty | `uv run cobalt jobs restarts 27c35e37..HEAD` | 0 | `path change rule restart` · `docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md A DOCS -` (this report, untracked) · `RESTARTS: none` |

```
clock · date · 0 · Tue Oct 20 12:39:10 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/cos-probe-fr2
    ?? "docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 27c35e37 docs(desk): R2178 cos-probe-fr2 preflight launched
diff · git diff --stat 27c35e37 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/cos-probe-fr2 · 0 · 27c35e37 docs(desk): R2178 cos-probe-fr2 preflight launched
env here · ls /Users/cobalt/cobalt-wt/cos-probe-fr2/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card `## RECORDS`, re-read where my list can: BASE is `27c35e37` (the desk's reset, not the drafter's `56abaea2`; `git diff --stat 27c35e37` → nothing, BASE touches docs only). `.claude.json` in `probe.py` → 2 hits (`:12`, `:298`) = the record's `2`; `under the scratch HOME` → 1 (`:454`) = `1`; README last section `## 2026-10-20 — cos-probe-fr1 (check)` at `:49` (Read) = the record. `probe.py` line numbers `:130`, `:167`, `:179`, `:293`, `:437`, `:451-454` match the record; `_scratch`'s body `:166-176`, `_plant`'s `.claude.json` write `:298`, `scratch_dir=root / "home" / "work"` `:246` re-read with Read. Test file: `auth_home` `:120`, auth stub `:143-149`, `_start_planted` `:197-200`, `:288`, `:322`, `:412` (`:416` literal), `:481` re-read with Read. `session.py` `:54`, `:93-95`, `:98-115` (`:105`, `:106`, `:108`), `:118` re-read. The fr1 check `:121` G2 HELD, `:123` G4 UNSETTLED, `:192` OPEN G4 re-read with Read. The gate run `:10-17`, F20-FINAL `:84`/`:91`, `cto-2026-10-18.md:90` (AUTHORIZATION row above) and the RESTARTS reading are copied as the record states; R1 runs the tool.

Lock: none at PREFLIGHT (BUILD-HUB L76). The rows add no with-DB test; the only take is W's gate.
`<FP>`, copied whole: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"` (run by `gate.sh` at W).

## E0 BASELINE
On `27c35e37`:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` · exit 0 · `4886 passed, 878 skipped, 4 xfailed, 36 warnings in 736.42s (0:12:16)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 0 · `146 passed, 1 skipped, 15 warnings in 32.59s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written in `tests/cobalt/test_cos_probe.py` (no `src/` edit): the rig gains `auth_stdout` (the stub's stdout, default `constructed auth output`); `_start_planted` reads `<cwd>/.mcp.json`; `:288` rewritten as `test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home`; the `:416` literal moved; NEW `test_auth_runs_under_the_real_home_and_a_login_there_passes`, `test_a_missing_home_is_refused`, `test_a_home_that_is_not_a_directory_is_refused` (H1's second refusal branch), `test_auth_quotes_logged_in_and_method_only`, `test_auth_quote_line_on_an_ok_run` (H3's "every run, OK or FAIL"), `test_auth_quote_unreadable_values_are_unread` (3 params: a non-matching string, a non-string and a missing key, non-dict JSON), `test_the_probe_opens_no_file_under_the_real_home` (H4 control).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py` · exit 1 · `11 failed, 27 passed in 2.14s`. Each red's first line (on top of it, `--tb=line` for the H1 three):
- H1 `test_auth_runs_under_the_real_home_and_a_login_there_passes` · `AssertionError: ['PROBE X11 FAIL auth: claude auth status exit 1 under the scratch HOME']` (the card's named red).
- H1 `test_a_missing_home_is_refused` · `AssertionError: [['claude', 'auth', 'status']]` (`:455`, the probe reached the auth stub; the card's named red).
- H1 `test_a_home_that_is_not_a_directory_is_refused` · `AssertionError: [['claude', 'auth', 'status']]` (`:463`).
- H2 `test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home` · `AssertionError: the spawn runs under the real HOME` · `- …/real-home` `+ …/T/cos-probe-2_5qfloi/home` (the card's named red).
- H2 `test_each_pass_rule_fails_on_its_own_breach` · `AssertionError: ('X2', 'planted', 'PROBE X2 OK no process, file, contents or tool call (0 allowlisted tool calls; turn ok=False)` (the plant is not in the cwd on BASE: `_start_planted` reads `<cwd>/.mcp.json`).
- H3 `test_auth_failure_is_a_fail_line_and_nothing_spawns` · `AssertionError: PROBE X11 FAIL auth: claude auth status exit 1 under the scratch HOME`.
- H3 `test_auth_quotes_logged_in_and_method_only` · `- under the real HOME (loggedIn=false authMethod=none)` `+ under the scratch HOME` (the card's named red).
- H3 `test_auth_quote_line_on_an_ok_run` · `IndexError: list index out of range` (no stderr line on BASE).
- H3 `test_auth_quote_unreadable_values_are_unread[×3]` · `AssertionError: PROBE X11 FAIL auth: claude auth status exit 1 under the scratch HOME`.
- H4 `test_the_probe_opens_no_file_under_the_real_home` · PASSED on BASE (the control, green as the card states).
No with-DB red: no lock taken at E2. Commit `7b1427af wip(cos-probe-fr2): red — H1, H2, H3 tests, H4 control` (`1 file changed, 127 insertions(+), 14 deletions(-)`).

## E3 THE ROWS
`src/cobalt/cos/probe.py` (each place re-found by content):
- H1: `_probe_env(extra)` no longer sets HOME; it refuses `HOME is not set in the parent env` / `HOME is not a directory` (no value printed) before any spawn; `_verdict` passes no home; the auth check stays first, argv `AUTH_ARGV`, `cwd` = `root / "work"`.
- H2: `_scratch` makes `<root>/work/` only; `_turn` `scratch_dir=root / "work"`; canary at `root / "canary.txt"`; `_plant` writes `root / "work" / ".mcp.json"` (stub and marker in `<root>`); `_live_scratch` subtracts the cwd entries before the turn; `_x12` `ps` cwd `root / "work"`; docstring rewritten ((a) the real HOME, (b) scratch, (c) the CLI's own state and the 67-session bound, (d)–(g) kept).
- H3: `_auth_quote(stdout)` (JSON in memory, `AUTH_KEYS = ("loggedIn", "authMethod")`, `_AUTH_VALUE = ^[a-z0-9._-]+$`, else `unread`); `_auth_exit` returns `(code, quote)`; `_verdict` prints `AUTH exit <n> · <quote>` to stderr before the result, FAIL clause `auth: claude auth status exit <n> under the real HOME (<quote>)`.
- H4: no code beyond H1–H3; `grep -c -F ".claude.json" src/cobalt/cos/probe.py` → `0`; `grep -c -F "security" src/cobalt/cos/probe.py` → `0`.
- D0: `## 2026-10-20 — cos-probe-fr2` at the end of `docs/40 - DevDocs/cobalt/cos/README.md`.
Rows' tests: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_cos_probe.py tests/cobalt/test_hitl_offline.py tests/cobalt/test_cos_offline.py` · exit 0 · `72 passed in 4.64s` (the card's ORDER suite; again after the mutations: `72 passed in 4.71s`).

THE MUTATIONS (Edit, run, undone with Edit, never committed):
| row | mutation | run | first failing line |
|---|---|---|---|
| H1 | `_probe_env` adds `env["HOME"] = tempfile.gettempdir()` | `-k "real_home_and_a_login or writes_only_in_its_scratch"` · `2 failed, 36 deselected` | `AssertionError: the spawn runs under the real HOME` · `AssertionError: ['PROBE X11 FAIL auth: claude auth status exit 1 under the real HOME (loggedIn=unread authMethod=unread)']` |
| H1 control | the two `ProbeRefused` HOME checks removed | `-k "missing_home or not_a_directory"` · `2 failed, 36 deselected` | `AssertionError: [['claude', 'auth', 'status']]` (both) |
| H2 | `_plant` writes `root / ".mcp.json"` (outside the cwd) | `-k "writes_only_in_its_scratch or fails_on_its_own_breach"` · `2 failed, 36 deselected` | `AssertionError: ('X2', 'planted', 'PROBE X2 OK …')` · `AssertionError: the project-scope plant sits in the scratch cwd during the turn` |
| H2 | `_live_scratch` drops `- before` | `-k "prints_one_line_and_exits_by_verdict and X2"` · `1 failed, 1 passed, 36 deselected` | `AssertionError: PROBE X2 FAIL file written in cwd: .mcp.json` |
| H3 | `_auth_quote` returns `" ".join(parts) + " " + stdout` | `-k "auth_quote or auth_failure_is_a_fail_line"` · `6 failed, 32 deselected` | `… under the real HOME (loggedIn=unread authMethod=unread constructed auth output)` · `… (loggedIn=false authMethod=none {"loggedIn": false, … "email": "constructed@example.invalid", "orgId": "constructed-org"})` · `AUTH exit 0 · loggedIn=true authMethod=claude.ai {…}` · the three unread params |
| H4 | `_plant` adds `(Path.home() / ".claude.json").read_text()` (the card's) | `-k "opens_no_file"` · `1 failed, 37 deselected` | `AssertionError: ['/private/var/…/test_the_probe_opens_no_file_u0/real-home/.claude.json']` |
After the last undo: `git diff --stat` → `src/cobalt/cos/probe.py | 107 +++…` (the fix, uncommitted then), `grep -c -F ".claude.json" src/cobalt/cos/probe.py` → `0`, suite `72 passed in 4.71s`.
Commit `74169800 fix(cos-probe-fr2): probe runs under the real HOME with a scratch cwd; cwd plant; auth quote (H1-H4, D0; L1, L28, L41)` (`2 files changed, 81 insertions(+), 29 deletions(-)`).

DEPLOY PROOF reads on this tree (the card's `after` values; main is read by the desk after the deploy): `grep -c -F "under the scratch HOME" src/cobalt/cos/probe.py` → `0` · `.claude.json` → `0` · `def test_auth_runs_under_the_real_home_and_a_login_there_passes` → `1` · `## 2026-10-20 — cos-probe-fr2` in the README → `1` · the offline trio → `72 passed`.

## RESTARTS
R1 · `uv run cobalt jobs restarts 27c35e37..HEAD` · exit 0 · whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cos/README.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-probe-fr2-build-2026-10-20.md	A	DOCS	-
src/cobalt/cos/probe.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_cos_probe.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row; = the card header's `RESTARTS: com.cobalt.radar`.

## W THE THREE SUITES
`<tip>` = `74169800`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-probe-fr2 all --deploy` (no `--deselect`: no with-DB test added; no `--tickers`: none written; no `--migration`) · exit 0 · verdict lines whole:
```
tests/ops: skipped (no ops paths)
offline 4895/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5867/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/cos-probe-fr2-all-20261020-125651.log
```
- (a) offline `4895 passed, 878 skipped, 4 xfailed, 36 warnings in 717.82s` (log `:956`) → `<p>` = 4895; this build's tests among them (the 7 new ids + 3 params, the rewritten `:288`). The W line `tests/ops: skipped (no ops paths)`.
- (b) lock taken (log `:962-966`, `lock taken: cos-probe-fr2`, `lock: waited 0 min`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → this worktree's line only, `:968`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:974`); proof-only `LEVEL 0013`.
- (c) pass 1 (`:1030` `pass 1: whole (deploy)`), the executed command (`:1032`) whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py` → `5623 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 883.29s` (`:1201`) → `<d1>` = 5623. Every SKIPPED line the gate printed is quoted above; `grep -n -F "OUTSIDE" <log>` → nothing.
- (c2) `dev forward: APPLIED 13:23:59` (`:1203`), `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1287`).
- (c3) pass 2, the PASS 2 command of `ops/desk/gate-lists.md` (log `:1289`) → `244 passed, 1 deselected, 5 warnings in 237.11s` (`:2184`) → `<d2>` = 244; `<d>` = 5623 + 244 = 5867 = the gate's `with-DB 5867/0`. This build adds no with-DB id.
- (c3r) `stray rows: not read (no --tickers given)` (this build writes no ticker).
- (e) live-note `148 passed, 1 skipped, 15 warnings in 26.49s` (`:2385`) → `<l>` = 148; no skip naming `COBALT_LIVE_VAULT_ROOT` in it (the live-note run's skip is `test_replay_line.py:266`, `COBALT_TEST_LIVE_DRC`).
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2258`) = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`** (`:2312`); `lock released` (`:2314`); `.env: removed` (`:2318`); `ls /Users/cobalt/cobalt-wt/cos-probe-fr2/.env` → `No such file or directory` (my own call after the gate).

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown red: H1 ×3, H2 ×2, H3 ×4 (incl. 3 params) red at E2 on BASE (quoted under `## E2 RED`); H4 control green on BASE and red under the card's mutation (`## E3`); every row's mutation red (`## E3` table); X2-OK red under the `- before` mutation. No test stayed green under its mutation; none rewritten.
(2) Entry paths: `_probe_env` caller `probe.py:499` (`_verdict`) → pinned by the H1 tests (HOME the parent's; missing; not a directory); `_auth_exit` caller `:500` → H3 tests + `test_auth_and_ps_are_spawned_with_cwd_inside_scratch` (cwd in the scratch); `_plant` callers `:361` (`_live_scratch`, X2/X10) and `:390` (`_x11`) → `test_each_pass_rule_fails_on_its_own_breach` (X2, X10 `planted`) and the H2 test (X11); `_scratch` caller (`_verdict`) → the H2 refusal half; the quote's value shapes (bool, matching string, non-matching string, non-string, missing key, non-dict JSON, non-JSON) → H3 tests; OK and FAIL runs both print the AUTH line → `test_auth_quote_line_on_an_ok_run`, `test_auth_quotes_logged_in_and_method_only`.
(3) Re-read at the tip: `git log --oneline 27c35e37..HEAD`, `git diff --stat 27c35e37 HEAD` (`3 files changed, 208 insertions(+), 43 deletions(-)`), `grep -n -F` of `_probe_env(` (`:220`, `:499`), `_auth_exit(` (`:170`, `:500`), `_plant(` (`:339`, `:361`, `:390`), `def test_` in the test file (new ids at `:288`, `:429`, `:452`, `:460`, `:469`, `:482`, `:495`, `:503`), the four DEPLOY PROOF counts, the gate log greps.

## FOR THE CHECK
- Range `27c35e37..74169800`: `7b1427af wip(cos-probe-fr2): red — H1, H2, H3 tests, H4 control` · `74169800 fix(cos-probe-fr2): probe runs under the real HOME with a scratch cwd; cwd plant; auth quote (H1-H4, D0; L1, L28, L41)`.
- Per row: reds `## E2 RED`; mutations and greens `## E3 THE ROWS`; callers `## PREFLIGHT` and self-check (2).
- R1 output whole: `## RESTARTS`.
- Suites: `## W` (executed commands, summaries). `<F0>` `664 35 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` `664 35 272c95bbb12241e3611e4b36326ccf87`. Lock: one take, by `gate.sh`, `lock: waited 0 min`; released (`lock released`); the gate started 12:56 (log name `…-20261020-125651`), the report written 13:39.
- CHECK ASK X2: `grep -c -F ".claude.json" src/cobalt/cos/probe.py` → `0`; `grep -c -F "security" …` → `0`; H4 mutation red (`## E3`).
- CHECK ASK X5: the pass rules of `_x11`, `_x12`, `_x3`, `_run_dms`, `_x14`, `_x17` are unchanged in `git diff 27c35e37 -- src/cobalt/cos/probe.py` (only `_x12`'s `ps` cwd path changes); `_live_scratch` changes the paths and the `before` subtraction only.
- Records copied at PREFLIGHT: `## PREFLIGHT` last paragraph.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. ASK DESK (card H2 item 1, the plant) [13:39]: under the real HOME the user-config plant would be his own CLI state file, never written. Default taken (the card's): a project-scope `<root>/work/.mcp.json` naming `browser` with the same `sys.executable` stub; X2 / X10's written-file check ignores it by the before-set. F20-FINAL `:84` / `:91` say "user config"; the gate seat reads X11 as proving a project-scope server stays out of a `setting_sources=[]`, `strict_mcp_config=True` session.
2. ASK DESK (card H3 item 2, the auth quote) [13:39]: default taken (the card's): one stderr line `AUTH exit <n> · loggedIn=<v> authMethod=<v>` on every run, the FAIL clause carrying the same quote; every other key dropped in memory.

## RECORDS
- L74: the session's attribution reminder asked for a `Claude-Session:` line; recorded under `## L74`, not acted on.
- RUN not needed by this card: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (the "DB: none" (a0) command; this card is not "DB: none"); it passed the 600 s foreground limit and was moved to the background; its result does not count toward any figure of this report.
- The gate's proof-only tables at F0 (`:992`) and F2 (`:2276`) show `cobalt_redactions` 530 → 531 rows (digest `b454bede…` → `f85773a4…`); the fingerprint sees no rows and this build writes none (no with-DB test, no ticker). Fact for the desk; nothing deleted.
- `SLOTS WARN user.aset_sizings max_attnum 1474 of 1600` at F0 (`:1023`) → `1510 of 1600` at F2 (`:2307`): a warning, not a guard exit; no self-heal run.
- `code: 74169800 (DIRTY: 1 path(s))` in the log: the untracked report, the only uncommitted path then.
- Card records re-read at PREFLIGHT (`## PREFLIGHT`); BASE `27c35e37` (the desk's reset of the drafter's `56abaea2`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cos-probe-fr2 · tip: 74169800 | on 27c35e37 | migration: none | offline 4895/0 | with-DB 5867/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 191388
