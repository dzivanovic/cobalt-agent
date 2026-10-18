# jev-keyed-1018 — build report (2026-10-18)

## §0 Headline
- W1-W3 are built and committed at `5071698a`. Each row's reds were shown on BASE and every mutation went red. Row tests: 82 passed. `tests/ops`: 3941 passed.
- RESTARTS: `com.cobalt.radar`, no UNCLASSIFIED.
- STOPPED at W (a): one offline red outside the rows, card 591's F12 fence `test_f12_no_route_wrapper_in_ops`, which forbids the wrapper R1830 approved. DECISION W-1 asks the desk to add that test to the card. No lock taken, no `.env`.

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
`<tip>` = `5071698a`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh jev-keyed-1018 all --deploy` (no `--deselect`, no `--tickers`, no `--migration`: this build adds no with-DB test and no migration) → exit 1, its output whole:

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

E2 and E3 did not show this red: my row runs did not include `tests/cobalt/test_jev_shadow_1015.py`. It is card 591's F12 fence (`# -- F12: the fence — no route wrapper under ops/`, `:899`). It pins that no `ops/` file holds `classify route`, which is the wrapper his R1830 now approves (W1 must exec `uv run cobalt classify route --day "$2" --run`). The file is in the card's `## NOT IN THIS JOB` ("every existing test but `tests/ops/test_needs_his_hand.py` … and the one appended test"), and BUILD-HUB W allows a W fix "inside the rows' files only". So I can't fix it here (DECISION W-1).

## PRE-STOP SELF-CHECK
Not reached (stopped at W).

## FOR THE CHECK
Not reached (stopped at W). Commits so far on `b95e5d8c..5071698a`: `bc55ef6e wip(jev-keyed-1018): red — W1-W3 tests on BASE`, `5071698a feat(jev-keyed-1018): JEV keyed wrapper, close step 7b, its one allow string (W1-W3, L41, L42, R1830)`.

## CONTINUE
next: W — after the desk widens the card for DECISION W-1: the fix in `tests/cobalt/test_jev_shadow_1015.py` (one test), commit it as `fix(jev-keyed-1018):`, re-run RESTARTS, then the gate call again.

## DECISIONS
- DECISION W-1 (blocks W; outside the card's rows): `tests/cobalt/test_jev_shadow_1015.py::test_f12_no_route_wrapper_in_ops` (card 591's F12 fence, `:899-910`) is red at `5071698a`: `AssertionError: assert ['jev-route.sh'] == []`. The fence pins what R1830 removed. The card's `## NOT IN THIS JOB` keeps that file closed, so this build didn't touch it. ASK DESK: add that one test to the card's `files` (W1), so the next build round can rewrite it in this row's shape. A suggested shape, not built: the only `ops/` file naming `classify route` is `ops/jev-route.sh`, and its one such line is the `exec` line. Then send `CONTINUE: W`. Safe default taken: nothing edited, the build stopped at W.

## RECORDS
- Commit attribution: a system message in this session asked for a `Claude-Session:` line on commits. BUILD-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, and the user's instructions take precedence, so I followed that. The message didn't come from a tool result, so I logged it here, not under `## L74`.
- No lock was taken in this build (E2 had no with-DB red; the gate stopped at (a)). `.env`: never present in this worktree, `ls` → `No such file or directory` (07:24 EDT check).
- No keyed call ran: every wrapper run was `sh ops/jev-route.sh` against the tmp `uv` stub and the tmp decoy key file; no Bash command named the key file or the vault.
- Card RECORDS as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

FAILED: W — offline red outside the card's rows — tests/cobalt/test_jev_shadow_1015.py::test_f12_no_route_wrapper_in_ops: AssertionError: assert ['jev-route.sh'] == [] (card 591's F12 fence; the file is NOT IN THIS JOB; DECISION W-1)
