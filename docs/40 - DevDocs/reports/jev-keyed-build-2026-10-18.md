# jev-keyed-1018 — build report (2026-10-18)

## §0 Headline
- BUILT: W1, W1c, W2 and W3 on tip `9780e4eb`. The JEV keyed wrapper is `ops/jev-route.sh`, CLOSE-HUB gains STEP 7b, CLOSE-HUB:10 gains its one allow string (R1830), and card 591's F12 fence now allows exactly that wrapper.
- Gate: offline 8514/0 · with-DB 5476/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed. RESTARTS: `com.cobalt.radar`.
- The first gate call was red on card 591's fence (DECISION W-1). The desk widened the card (W1c), and the second gate call is green. No keyed call ran.

## L74
none

## AUTHORIZATION
Started 06:35:30 EDT (`date`). `sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md"` → exit 0:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md" · 0 · 7fa97ec0bf110e41eb41f5b35433b369f7e65f4e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/715-jev-keyed-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1830 row · grep -n "^| R1830 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 29:| R1830 | 06:14 ET | HIS RULING: yes to JEV F12 (keyed wrapper allow string); "no card needed, run tribunal and JEV build". Words: [cto-2026-10-18-words.md#R1830](cto-2026-10-18-words.md). Asked brain what remains and what "no card" covers. | HIS RULING · APPROVED — pending fold |
RULING 2026-10-18 R1830 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1830 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 15af08b4218bdb9fb80c52ab7fa7784c9f14bf86
RULING 2026-10-18 R1830 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:

```
clock · date · 0 · Sun Oct 18 06:35:43 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## feat/jev-keyed-1018
    ?? "docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · b95e5d8c docs(desk): §5 CURRENT two drafters live
diff · git diff --stat b95e5d8c · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 feat/jev-keyed-1018 · 0 · b95e5d8c docs(desk): §5 CURRENT two drafters live
env here · ls /Users/cobalt/cobalt-wt/jev-keyed-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat b95e5d8c` | 0 | `docs(desk): §5 CURRENT two drafters live` · `docs/40 - DevDocs/reports/cto-2026-10-18.md | 7 ++++---` · `1 file changed, 4 insertions(+), 3 deletions(-)` |
| symbol | `grep -n -F "OPS_TOOLS" src/cobalt/jobs/restarts.py` | 0 | `36:OPS_TOOLS = frozenset({"ops/cto-desk.sh", "ops/fetch-voice-models.sh", "ops/fetch_voice_models.py"})` · `230:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` |
| callers | `grep -rn -F "OPS_TOOLS" src` | 0 | the same two hits (`restarts.py:36`, `:230`); no other reader |
| symbol | `grep -n -F "claude --bg" "docs/40 - DevDocs/prompts/CLOSE-HUB.md"` | 0 | `10:claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' …` ONE hit (21 allow, 11 deny, by Read of the line) |
| symbol | `grep -n -F "def test_the_voice_model_fetch_scripts_derive_no_restart" tests/cobalt/test_jobs_restarts.py` | 0 | `111:` (the card says `:110-119`; by content the test is `:111-120`) |
| symbol | `grep -n -F "LINE_COUNT" tests/ops/test_needs_his_hand.py` | 0 | `25:LINE_COUNT = {"CLOSE-HUB.md": 66, "DAY-OPEN-QWEN.md": 30}` · `84:    for name, count in LINE_COUNT.items():` (the `== 21` is `:89`, by Read) |
| symbol | `grep -n -F "def add_route_parsers" src/cobalt/classify/route.py` | 0 | `803:def add_route_parsers(csub) -> None:` (by Read: `:805` `--card`/`--day` group required, `:808` `--dry-run`/`--run` group required, `:812` `--repo` default None → `cfgmod.REPO_ROOT` `:761`) |
| symbol | `grep -n -F "def run_batch" src/cobalt/classify/route.py` | 0 | `487:def run_batch(router: Router, cards: list[CardText], *, wall_clock_s: float,` |
| symbol | `grep -n -F "def closed_cards" src/cobalt/classify/route.py` | 0 | `561:def closed_cards(repo: Path, day: str) -> list[str]:` |
| symbol | `grep -n -F "spend_cap_usd" configs/cobalt/classify/route.yaml` | 0 | `23:  spend_cap_usd: 5` |
| symbol | `grep -n -F "def seat" ops/desk/bare-guard.py` | 0 | `788:def seat(event):` |
| symbol | `grep -n -F "def bash_rules" ops/desk/bare-guard.py` | 0 | `1085:def bash_rules(command, s):` |
| symbol | `grep -n -F "exit 78" ops/run_backup.sh` | 0 | `31:    exit 78   # EX_CONFIG, the same signature the 09-03 prefill failure used` |
| shape | `git show f4e8de85:ops/run_classify_trial.sh` | 0 | 25 lines; `set -e`, `export COBALT_VAULT_FILE="/Users/cobalt/cobalt/data/.cobalt_vault"`, `KEY_FILE="$HOME/.cobalt_key"`, the missing-file `echo` + `exit 78`, `source "$KEY_FILE"`, `exec /Users/cobalt/.local/bin/uv run cobalt classify "$@"` — as the card's RECORDS state |
| carried test | `git show f4e8de85:tests/cobalt/test_classify_door.py` | 0 | last test `test_the_wrapper_is_secret_free_and_execs_the_cli`: bans `COBALT_MASTER`, `OPENROUTER`, `set -x`, `printenv` in non-`#` lines |
| wc | `wc -l` of CLOSE-HUB.md, restarts.py, test_jobs_restarts.py, test_needs_his_hand.py, jobs/restarts.md | 0 | `66` · `281` · `646` · `94` · `56` |
| DevDoc tail | `tail -n 12 "docs/40 - DevDocs/cobalt/jobs/restarts.md"` | 0 | last section `## 2026-10-08 — stt-model-fix-1008` (`OPS_TOOLS` adds the fetch scripts) |
| RESTARTS | `uv run cobalt jobs restarts b95e5d8c..HEAD` | 0 | `docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md	A	DOCS	-` · `RESTARTS: none` (only the untracked report; no commit in the range) |

`## READ` reports re-read (Read tool): `jev-f12-answer-2026-10-18.md` whole (last line: the `## FOR THE CHECK` paragraph); `jev-design-decisions-2026-10-14.md:14` row 6; `jev-tribunal-fold-answer-2026-10-15.md:21` F9, `:24` F12; design §4 `:111-117`, §7 `:143-158`, §8 S7/S9/S10 `:170-173`.

Card `## RECORDS` copied (re-read where the list can): the drafter record (BASE `b95e5d8c`: re-read, `git log --oneline -1`); THE TRIAL SHAPE (re-read, `git show f4e8de85:…`); `CLOSE-HUB.md:10` 21 allow / 11 deny / 66 lines / STEP 7 `:55-56`, blank `:57`, STEP 8 `:58`, STOP LINE `:64-66`, shape line `:34` (re-read by Read); the router `route.py:757-813` (re-read by Read); THE GUARD `seat` `:788-823`, G3 `:871-955`, `bash_rules` `:1085-1135` (re-read by Read); RESTARTS derivation (re-read `restarts.py:225-262`); THE FIRST KEYED BATCH, the check flow, the rulings proof, "nothing was run but reads" (desk facts, not re-readable by this list).

PROVEN BY FIRST REAL USE: class (a) by `authorize.sh` and `preflight.sh` (both ran). The card carries no `DB: none` key; no with-DB test is added (every new test is offline), so E2 takes no lock; W's `gate.sh` is the first with-DB use.

## E0 BASELINE
- Offline, on `b95e5d8c`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0, `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 752.72s (0:12:32)` (0 failed, 0 errors).
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0, `146 passed, 1 skipped, 15 warnings in 30.39s`; the one skip `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests only, no `src/` edit. Files: `tests/ops/test_jev_route_1018.py` (NEW, W1 (1)-(4), W2 (1)-(4) and its control, W3 (1)-(4)); `tests/cobalt/test_jobs_restarts.py` (`test_the_jev_route_wrapper_derives_no_restart`, inserted after `test_the_voice_model_fetch_scripts_derive_no_restart`, in its shape); `tests/ops/test_needs_his_hand.py` (`:25` `66` → `69`, `:89` `21` → `22`, no other line). No with-DB red: no lock taken at E2.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_jev_route_1018.py tests/cobalt/test_jobs_restarts.py` → exit 1, `18 failed, 26 passed, 15 warnings in 17.28s`. First lines of each red (from the `--tb=line` rerun, `18 failed, 4 passed, 15 warnings in 1.65s`):
- W1 (1) `test_w1_the_wrapper_text_is_secret_free`: `E   FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/jev-keyed-1018/ops/jev-route.sh'`
- W1 (2) `test_w1_one_date_execs_the_router_with_the_decoy`: `E   AssertionError: sh: /Users/cobalt/cobalt-wt/jev-keyed-1018/ops/jev-route.sh: No such file or directory` · `assert 127 == 0`
- W1 (3) `test_w1_any_other_argument_is_refused[args0..args8]` (9 reds): `assert 127 == 64` each (`sh` exit 127, the file does not exist)
- W1 (4) `test_w1_a_missing_key_file_is_exit_78_with_no_call`: `assert 127 == 78`
- W1 (b) `test_the_jev_route_wrapper_derives_no_restart`: `E   AssertionError: assert ('com.cobalt....cobalt.radar') == ()` · `Left contains 6 more items, first extra item: 'com.cobalt.agent'` (it escalates: `UNCLASSIFIED`, every resident)
- W2 (1) `test_w2_the_close_step_runs_the_wrapper_once`: `E   assert 0 == 1` · `+  where 0 = len([])`
- W2 (2) `test_w2_the_report_shape_names_the_section`: `E   AssertionError: assert 0 == 1`
- W2 (4) `test_w2_the_step_command_matches_the_w3_string`: `E   assert 0 == 1` · `+  where 0 = len([])`
- W3 (1) `test_w3_the_close_line_gains_exactly_the_one_string`: `E   AssertionError: assert 0 == 1` (`.count('Bash(sh /Users/cobalt/cobalt/ops/jev-route.sh --day *)')`)
- W3 (4) `test_w3_the_list_line_counts_22_and_names_r1830`: `E   assert '22 allow, 11 deny' in "THE LIST: 21 allow, 11 deny; …"`
- GREEN on BASE, as the card names: W2 (3) `test_w2_the_stop_line_is_unchanged_by_the_step`, the control `test_w2_control_the_guard_admits_the_close_call`, W3 (2) `test_w3_no_production_deny_or_allow_changes`, W3 (3) `test_w3_no_other_line_or_settings_file_names_the_wrapper` (the 4 passed).
- `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_needs_his_hand.py` → `1 failed, 7 passed`: `test_nothing_else_changed` `E   AssertionError: CLOSE-HUB.md` · `assert 66 == 69`.

Each red is its row's reason. Committed `bc55ef6e wip(jev-keyed-1018): red — W1-W3 tests on BASE`.

## E3 THE ROWS
Re-read by content before each edit: `restarts.py:36` `OPS_TOOLS`; `CLOSE-HUB.md` `:10`, `:12`, `:34`, `:55-58` (Read).
- **W1** `ops/jev-route.sh` NEW (26 lines: header comment, `set -e`, the argument check — `[ "$#" -eq 2 ] || exit 64`, `[ "$1" = "--day" ] || exit 64`, a `case` of `[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]`, else `exit 64` — then the `COBALT_VAULT_FILE` export, `cd /Users/cobalt/cobalt`, `KEY_FILE="$HOME/.cobalt_key"`, `[ -f "$KEY_FILE" ] || exit 78`, `. "$KEY_FILE"`, `exec uv run cobalt classify route --day "$2" --run`). `restarts.py:36` `OPS_TOOLS` gains `"ops/jev-route.sh"`. DevDoc `docs/40 - DevDocs/cobalt/jobs/restarts.md` gains `## 2026-10-18 — jev-keyed-1018`. Green: `-k "w1 or jev_route_wrapper"` → `13 passed, 31 deselected`.
- **W2** CLOSE-HUB: three lines after STEP 7's blank line, before `## 8.` (heading, body, blank); the shape line gains `→ `## 7b JEV``. Green: W2 (1)-(3) and the control pass; W2 (4) and the line-count pin `== 22` stay red until W3 (they read W3's string).
- **W3** CLOSE-HUB `:10` gains `"Bash(sh /Users/cobalt/cobalt/ops/jev-route.sh --day *)"` after `"Bash(git push origin main)"`; `:12` `21 allow` → `22 allow` and the one sentence. Green: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_jev_route_1018.py tests/ops/test_needs_his_hand.py tests/ops/test_hub_lines.py tests/cobalt/test_jobs_restarts.py` → `82 passed, 15 warnings in 19.41s`.

MUTATIONS (Edit, run alone, quoted, undone by Edit):

| row | mutation | run | result, first failing line |
|---|---|---|---|
| W1 | `KEY_FILE=…` and `. "$KEY_FILE"` moved above the argument check (the source line alone above it would fail on an unset `KEY_FILE`, a different reason) | `-k w1_any_other` | `9 failed`: `E   AssertionError: assert not True` · `+    where exists = PosixPath('…/sourced').exists` (`$W1_SOURCED` present) |
| W1 | `--run` cut from the exec line | `-k "w1_the_wrapper or w1_one_date"` | `2 failed`: (1) `assert 'exec uv run ...te --day "$2"' == 'exec uv run ...ay "$2" --run'`; (2) `At index 6 diff: '/Users/cobalt/cobalt' != '--run'` |
| W1 | `echo "$COBALT_MASTER_KEY"` added before the exec | `-k "w1_the_wrapper or w1_one_date"` | `2 failed`: (1) `E   AssertionError: echo`; (2) `E   AssertionError: assert ('decoy-w1-not-a-key\n' == ''` (the decoy in stdout) |
| W1 (b) | `"ops/jev-route.sh"` removed from `OPS_TOOLS` | `tests/cobalt/test_jobs_restarts.py -k jev_route_wrapper` | `1 failed`: `E   AssertionError: assert ('com.cobalt....cobalt.radar') == ()` |
| W2 | `never fails the close and never stops it` cut from the step | `-k w2_the_close_step` | `1 failed`: `E   AssertionError: never fails the close and never stops it` |
| W2 | the step moved after `## 8.`'s heading (first try added a second `## 8.` heading: red `ValueError: too many values to unpack (expected 1, got 2)`, a different reason, so redone as a true move) | `-k w2_the_close_step` | `1 failed`: `E   assert 58 < 57` |
| W3 | a second string `"Bash(sh /Users/cobalt/cobalt/ops/*)"` added to `:10` | `-k w3_the_close_line` | `1 failed`: `E   AssertionError: assert 23 == 22` |
| W3 | the W3 string spelled `--day*` | `-k "w3_the_close_line or w2_the_step_command"` | `2 failed`: W2 (4) `assert 'sh /Users/co...ute.sh --day*' == 'sh /Users/co...te.sh --day *'`; W3 (1) `E   AssertionError: assert 0 == 1` |

After the undos: `git diff --stat` → the three files of the fix only (`restarts.md | 4`, `CLOSE-HUB.md | 9`, `restarts.py | 2`), `git diff b95e5d8c -- CLOSE-HUB.md` re-read whole (R1 below). No test stayed green under its mutation. Committed `5071698a feat(jev-keyed-1018): JEV keyed wrapper, close step 7b, its one allow string (W1-W3, L41, L42, R1830)`.

R1 (RUN, asserts nothing):
- `uv run pytest -q -p no:cacheprovider tests/ops/test_jev_route_1018.py tests/ops/test_needs_his_hand.py tests/ops/test_hub_lines.py tests/cobalt/test_jobs_restarts.py` → `82 passed, 15 warnings in 19.07s` (`tests/ops/test_hub_lines.py` unedited, among them).
- `uv run pytest -q tests/ops` → exit 0, `3941 passed, 1 xfailed, 16 warnings in 973.38s (0:16:13)`.
- `git diff b95e5d8c -- "docs/40 - DevDocs/prompts/CLOSE-HUB.md"` → three hunks holding the four named changes: hunk 1 `@@ -7,9 +7,9 @@` = W3 `:10` (one string added after `"Bash(git push origin main)"`, nothing else on the line) and W3 `:12` (`22 allow` and the one sentence); hunk 2 `@@ -31,7 +31,7 @@` = W2 (b) the shape line (`→ `## 7b JEV``); hunk 3 `@@ -55,6 +55,9 @@` = W2 (a) the three added lines. W3's two lines fall in one hunk; no other line changed.
- `uv run cobalt jobs restarts b95e5d8c..HEAD` → RESTARTS below; `ops/jev-route.sh` `operator script; no Cobalt reader`, `tests/`, `docs/` none, `src/cobalt/jobs/restarts.py` `static import reach` → `com.cobalt.radar`; no `ESCALATE`.

## RESTARTS
`uv run cobalt jobs restarts b95e5d8c..HEAD` (at `5071698a`, with the report untracked):

```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/prompts/CLOSE-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/jev-keyed-build-2026-10-18.md	A	DOCS	-
ops/jev-route.sh	A	operator script; no Cobalt reader	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/ops/test_jev_route_1018.py	A	test/documentation; no resident	-
tests/ops/test_needs_his_hand.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row: nothing to classify in `jobs.yaml`.

## W THE THREE SUITES
### Second gate call (the verdict), `<tip>` = `9780e4eb`
`sh /Users/cobalt/cobalt/ops/desk/gate.sh jev-keyed-1018 all --deploy` → exit 0, verdict lines whole:

```
tests/ops: run (docs/40 - DevDocs/prompts/CLOSE-HUB.md)
offline 8514/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5476/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/jev-keyed-1018-all-20261018-072815.log
```
- (a) offline: `4573 passed, 806 skipped, 1 xfailed, 36 warnings in 762.11s` (log `:888`) + `tests/ops` `3941 passed, 1 xfailed, 16 warnings in 998.81s` (`:960`) = `offline 8514/0`. The W line: `tests/ops: run (docs/40 - DevDocs/prompts/CLOSE-HUB.md)` (`:890`). Tests this build adds: the 21 of `tests/ops/test_jev_route_1018.py` and `tests/cobalt/test_jobs_restarts.py::test_the_jev_route_wrapper_derives_no_restart`; W1c edits `tests/cobalt/test_jev_shadow_1015.py::test_f12_no_route_wrapper_in_ops`.
- (b) `lock taken: jev-keyed-1018` (`:966`, waited 0 min); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's (`:971`). `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:977`); proof-only → `LEVEL 0013`.
- (c) pass 1, `pass 1: whole (deploy)` (`:1031`), executed command (`:1033`), copied whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py` → `5271 passed, 7 skipped, 99 deselected, 3 xfailed, 43 warnings in 929.37s` (`:1194`) = `<d1>` 5271. The 7 skipped are the SKIPPED lines above; none is marked `OUTSIDE the allowed set` (`grep -n -F "OUTSIDE"` of the log → nothing).
- (c2) `dev forward: APPLIED 08:13:51` (`:1196`); `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1274`).
- (c3) pass 2 (`:1276`, the PASS 2 list of `ops/desk/gate-lists.md`; this build deselects nothing) → `205 passed, 1 deselected, 5 warnings in 242.92s` (`:2048`) = `<d2>` 205; `<d>` = 5271 + 205 = `with-DB 5476/0`. This build adds no with-DB test.
- (c3r) `stray rows: not read (no --tickers given)`: no with-DB test of this build writes a ticker.
- (c4) not run: no migration added.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (`:2052`); `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2116`) = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`** (`:2168`); `lock released` (`:2170`); `.env: removed` (`:2174`); my own `ls /Users/cobalt/cobalt-wt/jev-keyed-1018/.env` → `No such file or directory` (08:19 EDT).
- (e) live-note → `146 passed, 1 skipped, 15 warnings in 29.84s` (`:2239`) = `live-note 146/0`; its one skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- The proof-only line `code: 9780e4eb (DIRTY: 1 path(s))` (`:2164`): the one dirty path was this report, uncommitted during the run. No code path was dirty.

### First gate call (red), `<tip>` = `5071698a` `sh /Users/cobalt/cobalt/ops/desk/gate.sh jev-keyed-1018 all --deploy` (no `--deselect`, no `--tickers`, no `--migration`: this build adds no with-DB test and no migration) → exit 1, its output whole:

```
RED (exit 1): 1 failed, 4572 passed, 806 skipped, 1 xfailed, 36 warnings in 766.70s (0:12:46)
SKIPPED [1] tests/cobalt/test_vaultwrite.py:493: Postgres env settings not available
… (the SKIPPED lines, each "Postgres env settings not available" or "reaches cobalt_dev (lock-relief G1)", and two "COBALT_LIVE_VAULT_ROOT not set" lines for tests/taxonomy/test_catalyst.py:365 and tests/taxonomy/test_predicate.py:262)
1 failed, 4572 passed, 806 skipped, 1 xfailed, 36 warnings in 766.70s (0:12:46)
log: /Users/cobalt/cobalt-wt/.gate-logs/jev-keyed-1018-all-20261018-071120.log
```

(a) OFFLINE red, the one failure (log `:81-98`):
```
_______________________ test_f12_no_route_wrapper_in_ops _______________________
    def test_f12_no_route_wrapper_in_ops():
        hits = []
        for p in sorted((REPO / "ops").rglob("*")):
            if p.is_file():
                try:
                    if "classify route" in p.read_text():
                        hits.append(p.name)
                except UnicodeDecodeError:
                    continue
>       assert hits == []
E       AssertionError: assert ['jev-route.sh'] == []
tests/cobalt/test_jev_shadow_1015.py:910: AssertionError
```
The gate stopped after (a): (b) to (f) and (e) did not run. `grep -n -F "verdict"` of the log → nothing. No lock taken: `ls -la /Users/cobalt/cobalt-wt/.cobalt_dev.lock` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/jev-keyed-1018/.env` → `No such file or directory`. `cobalt_dev` was not touched.

E2 and E3 did not show this red: my row runs did not include `tests/cobalt/test_jev_shadow_1015.py`. It is card 591's F12 fence (`# -- F12: the fence — no route wrapper under ops/`, `:899`). It pins that no `ops/` file holds `classify route`, which is the wrapper his R1830 now approves (W1 must exec `uv run cobalt classify route --day "$2" --run`). The file is in the card's `## NOT IN THIS JOB` ("every existing test but `tests/ops/test_needs_his_hand.py` … and the one appended test"), and BUILD-HUB W allows a W fix "inside the rows' files only". So I couldn't fix it in that round. I stopped with DECISION W-1. The desk answered by widening the card with row W1c (`329fc1ef`). W1c is built (`## RECORDS`), and the second gate call above is green.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red for its named reason.
- E2 reds on BASE: W1 (1)-(4), W1 (b), W2 (1), (2), (4), W3 (1), (4), and the `test_needs_his_hand.py` pin (`assert 66 == 69`).
- E3 mutation reds (table above): W1 ×4 (sourced marker present; `--run` cut; `echo` of the key, which also fails on the decoy in stdout; `OPS_TOOLS` entry removed), W2 ×2 (`never fails` cut; step moved after `## 8.`), W3 ×2 (second ops string; `--day*`).
- W1c: red `assert ['jev-route.sh'] == []` before the edit; mutations `['jev-route.s...un_backup.sh'] == ['jev-route.sh']` and `[] == ['jev-route.sh']`.
- The four controls the card names green on BASE and after: W2 (3), the guard control, W3 (2), W3 (3). They stay green because the card defines them as controls.
- No test stayed green under its mutation.

(2) Every entry path is pinned by a test.
- `OPS_TOOLS`'s one reader is `restarts.py:230` (`grep -rn -F "OPS_TOOLS" src`, PREFLIGHT). `test_the_jev_route_wrapper_derives_no_restart` pins it.
- Wrapper entry paths:
  - one valid date: W1 (2);
  - every refused argument shape, including a second word, `;`, `--day=`, `--card` and an extra `--run`: W1 (3);
  - the key file missing: W1 (4);
  - its one caller, the CLOSE-HUB step: W2 (1);
  - its one allow string: W3 (1) and W2 (4);
  - the guard admitting the close seat's call: the W2 control;
  - no other launch line, fixed file or settings file naming it: W3 (3);
  - card 591's fence allowing exactly this file: W1c.

(3) Every `file:line`, count and quote was re-read at the tip, `9780e4eb`.
- `git show 9780e4eb:ops/jev-route.sh`: 26 lines, as quoted in E3.
- `grep -n -F "ops/jev-route.sh" src/cobalt/jobs/restarts.py`: `36:`.
- `grep -n -F "ops/jev-route.sh" "docs/40 - DevDocs/prompts/CLOSE-HUB.md"`: `10:` and `59:` only.
- `wc -l`: CLOSE-HUB `69`, wrapper `26`.
- `grep -n -F "assert hits ==" tests/cobalt/test_jev_shadow_1015.py`: `911:    assert hits == ["jev-route.sh"]`. The other hit, `324:`, is a different test, untouched.
- `git log --oneline b95e5d8c..HEAD`: the four commits below.
- The gate log lines cited were grepped (`F0: `, `F1: `, `F2: `, `dev forward: APPLIED`, `pass 1: whole (deploy)`, `tests/ops: `, ` passed`, `OUTSIDE`).

## FOR THE CHECK
- Range `b95e5d8c..9780e4eb`:
  - `bc55ef6e wip(jev-keyed-1018): red — W1-W3 tests on BASE`
  - `5071698a feat(jev-keyed-1018): JEV keyed wrapper, close step 7b, its one allow string (W1-W3, L41, L42, R1830)`
  - `38134214 wip(jev-keyed-1018): W — offline red outside the rows (card 591 F12 fence test)` (report only)
  - `9780e4eb fix(jev-keyed-1018): card 591 F12 fence allows exactly ops/jev-route.sh (W1c, R1830)`
- Per row, the reds, mutations and greens are in `## E2 RED`, `## E3 THE ROWS` and `## RECORDS` (W1c). The caller greps are in `## PREFLIGHT`. R1's output is in `## E3 THE ROWS` (R1), whole.
- Suites, each run by the second gate call: offline `8514/0`, with-DB `5476/0`, live-note `146/0`. The commands are in `## W` (pass 1 copied whole).
- `F0` `664 35 272c95bbb12241e3611e4b36326ccf87` · `F1` `908 45 126f2d6983fa59f9d0eaaff7da7dd29c` · `F2` = `F0`. The lock was taken once, by `gate.sh` (log `:966`, waited 0 min), and released at `:2170`. Forward was applied 08:13:51 and rolled back to `0013`.
- RESTARTS table in `## RESTARTS` (plus the W1c row in `## RECORDS`): `RESTARTS: com.cobalt.radar`.
- The records copied at PREFLIGHT are in `## PREFLIGHT`.
- X1: the key file is sourced only after the argument check (W1 (3) pins that `$W1_SOURCED` stays absent). The script has no output line. Only `--day <YYYY-MM-DD>` reaches `uv` (W1 (2), W1 (3)).
- X2: every wrapper run used a tmp `HOME`, a decoy key file and a stub `uv` on `PATH`. No test or command opened the real key file, the vault, a ledger or a socket.
- X5: a second word, a `;` or a newline makes `$#` ≠ 2 or breaks the `case`, and the wrapper exits 64 (W1 (3) cases `["--day","2026-01-02","--run"]`, `["--day","2026-01-02; ls"]`).

## CONTINUE
next: none — BUILT

## DECISIONS
none open. DECISION W-1 (the card 591 F12 fence red at the first gate call) was answered by the desk's card widening, row W1c at `329fc1ef`. It is built and green (`## RECORDS`).

## RECORDS
- Commit attribution: a system message in this session asked for a `Claude-Session:` line on commits. BUILD-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, and the user's instructions take precedence, so I followed that. The message didn't come from a tool result, so I logged it here, not under `## L74`.
- First gate call: no lock taken (E2 had no with-DB red; the gate stopped at (a)); `.env` absent (07:24 EDT check). Second gate call: the one lock take, by `gate.sh`; `.env: removed, proven gone (W)` (`ls` → `No such file or directory`, 08:19 EDT).
- No keyed call ran: every wrapper run was `sh ops/jev-route.sh` against the tmp `uv` stub and the tmp decoy key file; no Bash command named the key file or the vault.
- Card RECORDS as re-read at PREFLIGHT: see `## PREFLIGHT`.
- CONTINUED at W 07:27:02 EDT: the desk's `CONTINUE: W` (from `cto-desk`) stated that card 715 was widened at `329fc1ef` with row W1c. I checked it myself: `git -C /Users/cobalt/cobalt log --oneline -3 -- <card>` → `329fc1ef docs(desk): card 715 widened by one test (W-1)`; `git -C /Users/cobalt/cobalt diff 7fa97ec0 329fc1ef -- <card>` → row W1c added, the test named in W1's `files`, `## NOT IN THIS JOB` opened for that one test; `authorize.sh build <card>` re-run → `CARD COMMITTED · … · 329fc1ef…`, `CARD UNCHANGED · … nothing`, `AUTHORIZED`. The R1830 row now reads `HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46` (`:62`).
- W1c (built at RESUME): red first, `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_jev_shadow_1015.py -k f12_no_route_wrapper` → `1 failed, 59 deselected`: `E   AssertionError: assert ['jev-route.sh'] == []`. Edit: `assert hits == []` → `assert hits == ["jev-route.sh"]` with one comment line citing R1830 (F12); nothing else in the file. Green: `tests/cobalt/test_jev_shadow_1015.py` → `60 passed, 15 warnings in 6.01s`. MUTATIONS: a `# classify route` line added to `ops/run_backup.sh` → `E   AssertionError: assert ['jev-route.s...un_backup.sh'] == ['jev-route.sh']`; the wrapper's `classify route` text broken to `classify  route` (it stands in for removing the file: no listed string deletes a file) → `E   AssertionError: assert [] == ['jev-route.sh']`; both undone by Edit, `git status --short` → only the test file and the report. Committed `9780e4eb fix(jev-keyed-1018): card 591 F12 fence allows exactly ops/jev-route.sh (W1c, R1830)`. RESTARTS again → the same table plus `tests/cobalt/test_jev_shadow_1015.py	M	test/documentation; no resident	-`, `RESTARTS: com.cobalt.radar`.
- Extra gate call: the second `gate.sh … all --deploy`, on `<tip>` `9780e4eb` (BUILD-HUB W: a red at W → fix, commit, RESTARTS and W again).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: jev-keyed-1018 · tip: 9780e4eb | on b95e5d8c | migration: none | offline 8514/0 | with-DB 5476/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 264537
