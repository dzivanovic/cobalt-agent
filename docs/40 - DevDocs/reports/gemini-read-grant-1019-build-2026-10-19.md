# gemini-read-grant-1019 — build report (2026-10-19)

## §0 Headline
Built at `ad4c8dfe` on `0ac7746e`. C1: the guard admits the agy builder call only when the seat's cwd is exactly `<WT>/<worktree>`. C2: the launcher starts the Gemini gate seat in its worktree; this is pinned by a test and the launch path is unchanged. T1: new kind `desk-launch.sh x1-copy <worktree> <leg>`. H2: the X1 paragraph now runs six legs, 0a to 0f. H3: the Gemini builder text says no fetch and that a denial ends its run.
Suites: offline 8796/0, live-note 147/0, tests/ops 4066 passed. DB: none, so no lock was taken.
Two decisions, none for Dejan: (1) the card's H2 test forbids `cli.log`, but the card's own verbatim H2 text names it once. The text was kept and that one assert dropped. (2) Whether the hook's `cwd` follows a `cd` is unproven here (the card's own UNPROVEN line). D1 is the desk's job after the deploy.

## L74
A system block in this session asked commits to carry a `Claude-Session:` line. Recorded here once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md" · 0 · 42d456ab44895016452834348cb816fddfe15402
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1942 row · grep -n "^| R1942 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 30:| R1942 | 20:47 ET | HIS RULING · APPROVED (relayed by the brain 20:46, L79): "A for gemini" — a K5 card in which desk-launch.sh shadow adds and removes the one write_file rule in the agy settings.json; NEEDS HIS HAND entry closed. | APPLIED: areas/cobalt.md NOW at wake-up 01:57 |
RULING 2026-10-18 R1942 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1942 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 55d8b50e607b5d4eb1b86354e336323252aec34c
RULING 2026-10-18 R1942 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
```
clock · date · 0 · Mon Oct 19 09:05:09 EDT 2026
status · git status --short --branch · 0 · ## ops/gemini-read-grant-1019
head · git log --oneline -1 · 0 · 0ac7746e docs(desk): preflight 837 NO (smoke line), drafter 838 amend 4, R2017
diff · git diff --stat 0ac7746e · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/gemini-read-grant-1019 · 0 · 0ac7746e docs(desk): preflight 837 NO (smoke line), drafter 838 amend 4, R2017
env here · ls /Users/cobalt/cobalt-wt/gemini-read-grant-1019/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

`git show --stat 0ac7746e` → `0ac7746e docs(desk): preflight 837 NO (smoke line), drafter 838 amend 4, R2017` · 3 files changed, 76 insertions(+), 2 deletions(-) (`838-draft-gemini-read-grant-amend4.md`, `reports/cto-2026-10-19.md`, `reports/gemini-xcopy-preflight-2026-10-19.md`).

THE CARD'S SYMBOLS (Read / Grep tool and `grep -n -F`, each re-found by content on BASE):
- `ops/desk/bare-guard.py`: `def builder_call(command, s):` `:1180`; docstring `:1181-1185`; `target = os.path.join(WT_ROOT, wt)` `:1190`; the agy mode check `:1213-1215`; `.env` → `ROUTE["G7 env"]` `:1216-1217`; `"G7": "route: the desk launches",` `:87`; `seat` `:788`, `cwd = os.path.normpath(cwd) if … os.path.isabs(cwd) else ""` `:790`; `PLAIN_PROMPT = re.compile(r'"[^"\\$`]*"')` `:122`; `WT_ROOT = os.path.normpath(…)` `:60`.
- callers: `grep -rn -F "builder_call(" ops/desk` → `bare-guard.py:1118` (a shell `-c` body), `:1121` (the one launch), `:1180` (the def).
- `ops/desk/desk-launch.sh`: `:216` the roots comment; `:236` `AGY=${COBALT_AGY_SETTINGS:-…}`; `refuse()` `:384-387`; `run_launch` `:431-447` (`cd $1` dry `:433`, `cd "$1"` `:440`, `eval "$2"` `:442`); usage `:520`; desk-size guard `:526-532` (`if [ "$kind" != "desk" ]; then` `:530`); `grant-sweep` `:1121-1151`; the card-kind usage `:1153`; the kind refusal `:1175`; `build|shadow)` `dir="$WT/$wt"` `:2573-2576`; grant block `:2665-2694`; `run_launch "$dir" …` `:2695`.
- `ops/desk/scratch-clean.sh` `plain()` `:46-51`.
- `SHADOW-HUB.md`: `:10` the line; `:12` `The launcher refuses`; `:28` `- Gemini:`; `:30` `X1 for Gemini`; `:42` the `` `You are <GROK `` line; `:49` the builder-call rule; `:59` `4. THE INSTRUCTIONS`. `grep -c -F "X1 for Gemini"` → `2`.
- `CHECK-HUB.md:95` the GEMINI line (holds `Run NO shell command - not cat, grep, ls or any pipe`).
- `grep -rn -F "any pipe" tests ops src` → nothing (exit 1).
- tests: `test_bare_guard.py` `roots` `:28-39`, `call`/`run` `:274-288`, `assert_denied`/`assert_allowed` `:291-298`, `G7_ROUTE` `:157`, `JOB_WT` `:159`, `ENV_ROUTE` `:2217`, `test_s3_…` `:2268`, `gemini_seat`/`gemini` `:2468-2483`, `test_k5_a_gemini_gate_seat_runs_the_gemini_command` `:2486`, `test_k5_any_other_gemini_shape_is_g7` `:2493`, `test_k5_s7_the_gemini_call_with_env_is_denied` `:2526`, last line `:2553`; `test_desk_launch_shadow.py` `Desk` `:90-170`, `write_exe` `:83` (called `:112`), `:204-210`, `write_agy`/`signed_gemini` `:352-359`, `HOUSE` `:479`, `sweep` `:489-494`, last line `:690`; `test_shadow_hub_file.py` `test_k5_the_gemini_x1_paragraph` `:187-194`, `test_s7_…` `:200`, `test_k5_the_gemini_x1_read_step` `:406-413`, last line `:429`.

`wc -l`: bare-guard.py 1427 · desk-launch.sh 2695 · SHADOW-HUB.md 116 · test_bare_guard.py 2553 · test_desk_launch_shadow.py 690 · test_shadow_hub_file.py 429.

`uv run cobalt jobs restarts 0ac7746e..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/reports/gemini-read-grant-1019-build-2026-10-19.md	A	DOCS	-
RESTARTS: none
```
(the one path is this report, untracked; no commit in the range.)

Card `## RECORDS` copied: R2005/R2007/R2011/R2015 rows; THE SETTLEMENT R1804; 717 legs 0a and 0b; the last-run pointer; the gate seat's cwd; the guard; the test forms; the workspace line; the preflight; BAND HIGH; RESTARTS K10; amends 829, 832, 836, 838; OWED. Re-read here: the `desk-launch.sh` and guard `file:line`s above; the `grep -c -F "X1 for Gemini"` → 2 and `"any pipe"` → nothing. Not re-read (outside the list's reach, `~/.gemini` is NOT IN THIS JOB): the 717 `cli.log` lines.

DB: none — no lock probe; the with-DB strings are not used by this build.

## E0 BASELINE
`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (on `0ac7746e`) → `4730 passed, 866 skipped, 4 xfailed, 36 warnings in 792.37s (0:13:12)`; 0 failed, 0 errors.
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.57s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` names no `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests written, no `src/` or `ops/` edit:
- `tests/ops/test_bare_guard.py` (appended after `:2553`): helper `seat_in`; `test_c1_a_gemini_call_from_outside_its_worktree_is_g7` [x1-canary, repo, wt root, below the worktree, other worktree]; `test_c1_control_from_the_worktree_is_admitted` [no slash, trailing `/`]; `test_c1_the_pin_is_gemini_only`; `test_c1_env_is_still_g7_env_from_the_worktree`.
- `tests/ops/test_desk_launch_shadow.py` (appended after `:690`): `test_c2_the_gemini_gate_seat_starts_in_its_worktree`; helpers `x1copy`, `x1wt`, `agy_run`, `nothing_written`; the T1 tests the card names, plus `test_t1_an_id_that_is_not_36_hex_characters_is_refused` (`## RECORDS`).
- `tests/ops/test_shadow_hub_file.py`: `test_k5_the_gemini_x1_paragraph` changed as named (`X1 WRITE OK` → `X1 READ OK`, `## PASSES row 0 (X1)` → `## PASSES rows 0a to 0f (X1)`); appended `one_line`, `test_c1_the_hub_names_the_cwd_pin`, `test_h2_x1_runs_one_launch_per_leg_from_the_worktree`, `test_h3_the_gemini_builder_is_told_no_fetch`. One assert of the card's H2 list is left out (`DECISION H2`).

`uv run pytest -q -p no:cacheprovider --color=no --tb=no -rf -k "c1_ or c2_ or t1_ or h2_ or h3_ or the_gemini_x1_paragraph" tests/ops/test_bare_guard.py tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py` on BASE → `36 failed, 62 passed, 1917 deselected, 15 warnings in 5.97s`. The reds and their first lines:
- the 5 `test_c1_a_gemini_call_from_outside_its_worktree_is_g7[…]`: `AssertionError: (0, '')` / `assert 0 == 2` (admitted on BASE: the row's reason).
- every `test_t1_…` except two: `REFUSED: kind 'x1-copy' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops, prodwrite` (BASE has no kind). `test_t1_a_wrong_argument_count_is_refused[three]`: `REFUSED: two resume steps: '0c' and 'extra'` (BASE parses the extra word as a card's resume step, still no `x1-copy:` text). `test_t1_runs_under_a_desk_size_guard_that_exits_7`: `assert 7 == 0` (BASE guards the kind).
- `test_k5_the_gemini_x1_paragraph`: `AssertionError: X1 READ OK`. `test_c1_the_hub_names_the_cwd_pin`: `assert "a Gemini call only while the seat's cwd is exactly <worktree> (R2011)" in 'The launcher refuses …'`. `test_h2_…`: `assert 'one agy launch per leg, R2007' in "X1 for Gemini (R1738; …"`. `test_h3_…`: `assert 'NO shell command and no URL fetch; … (GEMINI)' in '`You are <GROK …'`.
- GREEN on BASE, as the card says: `test_c2_the_gemini_gate_seat_starts_in_its_worktree` (a PIN, recorded); `test_c1_control_from_the_worktree_is_admitted` ×2, `test_c1_the_pin_is_gemini_only`, `test_c1_env_is_still_g7_env_from_the_worktree` (controls).
Committed `4a215342 wip(gemini-read-grant-1019): red`. With-DB reds: none (DB: none).

## E3 THE ROWS
- C1: `ops/desk/bare-guard.py` `builder_call`. After the agy mode check: `if head == "agy" and s["cwd"] != target:` / `return False  # R2011: a Gemini call only from its worktree` (`:1217-1218` at the tip). The docstring gains `Gemini: from the worktree only (cwd == <worktree>, R2011).` `SHADOW-HUB.md:12` gains `; a Gemini call only while the seat's cwd is exactly <worktree> (R2011)`. `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_bare_guard.py` → `1885 passed, 15 warnings in 64.55s (0:01:04)`.
- T1: `ops/desk/desk-launch.sh`. The `:216` comment names `COBALT_AGY_HOME`. `AGY_HOME=${COBALT_AGY_HOME:-/Users/cobalt/.gemini/antigravity-cli}` sits beside `AGY`. The usage line gains `| x1-copy <worktree> <leg>`. The guard reads `if [ "$kind" != "desk" ] && [ "$kind" != "x1-copy" ]; then`, and its comment names x1-copy as launching nothing. The block `# ---- kind x1-copy: …` follows `grant-sweep` (`:1155` at the tip) with checks (1) to (6), the copy and the four `X1-COPY:` lines. `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_desk_launch_shadow.py` → `72 passed, 15 warnings in 16.37s`.
- C2: no edit (a pin).
- H2: `SHADOW-HUB.md:30` replaced whole by the card's text, verbatim.
- H3: `:42`. The GEMINI clause reads `NO shell command and no URL fetch; read and write files with your file tools only; a denial ends your run (GEMINI)`. `Pass <0a | 0b | 0c | 0d | 0e | 0f | T | S | S2>: <this leg's one X1 step under ## X1, nothing else |`. After the closing backtick comes ` For GEMINI in the X1 legs, Pass 0a to 0f, the clause reads NO shell command; read and write files with your file tools only; a denial ends your run, as leg 0b asks the fetch the fence must deny.` `:59` gains ` For a Gemini MODEL its first line under the title is: Run NO shell command and no URL fetch; read and write files with your file tools only; a denial ends your run.`
- After the hub edits: `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_shadow_hub_file.py tests/ops/test_desk_launch_shadow.py` → `130 passed, 15 warnings in 16.59s`.

THE MUTATIONS (each made with Edit, run alone, then undone with Edit):
- C1: the inserted `if` taken out. `-k test_c1_ tests/ops/test_bare_guard.py` → `5 failed, 4 passed, 1876 deselected`; the first failing line is `AssertionError: (0, '')` / `assert 0 == 2`; every `test_c1_a_gemini_call_from_outside…` case is red.
- C2: `dir="$WT/$wt"` of the `build|shadow)` arm changed to `dir="$REPO"`. `-k test_c2_` → `1 failed, 71 deselected`; `assert 'cd /private/..._seat_s0/repo' == 'cd /private/.../x-job-gemini'`.
- T1 (3): the per-word `[ "$w" = "$WT/$xwt" ] || refuse …` and the `[ "$words" -ge 1 ]` line taken out. `-k test_t1_a_foreign_workspace_is_refused` → `6 failed, 66 deselected` (all six shapes).
- T1 guard: the line restored to `if [ "$kind" != "desk" ]; then`. `-k test_t1_runs_under_a_desk_size_guard_that_exits_7` → `1 failed`; `assert 7 == 0`.
- H2: `leg 0f, the outside-cwd leg` taken out. `test_h2_…` is red: `AssertionError: leg 0f, the outside-cwd leg`.
- H3: `and no URL fetch` taken out of the pass prompt line. `test_h3_…` is red: `assert 'NO shell command and no URL fetch; … (GEMINI)' in '`You are <GROK …'`.
- `git diff --stat` after the undos → `SHADOW-HUB.md | 8 +--`, `bare-guard.py | 5 +-`, `desk-launch.sh | 91 ++++…` (the fix only). Committed `ad4c8dfe feat(gemini-read-grant-1019): Gemini call only from its worktree, x1-copy kind, X1 per leg, builder no-fetch text (C1, C2, T1, H2, H3; L1, L3, L67)`.

P1 (RUN, quoted):
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4066 passed, 1 xfailed, 16 warnings in 908.53s (0:15:08)`.
- `grep -n -F "R2011: a Gemini call only from its worktree" ops/desk/bare-guard.py` → `1218:        return False  # R2011: a Gemini call only from its worktree`.
- `grep -n -F -e "cwd is exactly <worktree> (R2011)" -e "the cwd pin, R2011" "docs/40 - DevDocs/prompts/SHADOW-HUB.md"` → two hits, `12:The launcher refuses …; a Gemini call only while the seat's cwd is exactly <worktree> (R2011). Every other launch stays G7.` and `30:X1 for Gemini (R1738; card 367's row, the reads a STOP; one agy launch per leg, R2007; the cwd pin, R2011): …` (each whole line is in the tool output; line 30 is the H2 text above).
- `grep -n -F "kind x1-copy: the X1 leg's agy transcript" ops/desk/desk-launch.sh` → `1155:# ---- kind x1-copy: the X1 leg's agy transcript into its worktree (card 2026-10-19 827 T1, R2015) --`.
- `uv run cobalt jobs restarts 0ac7746e..HEAD` → see `## RESTARTS`; `RESTARTS: none`.

## RESTARTS
`uv run cobalt jobs restarts 0ac7746e..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gemini-read-grant-1019-build-2026-10-19.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `ad4c8dfe`.
- (a0) `git diff --name-only --no-renames 0ac7746e` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/bare-guard.py`, `ops/desk/desk-launch.sh`, `tests/ops/test_bare_guard.py`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **cobalt_dev: not taken (DB: none — 6 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-read-grant-1019 offline` → `tests/ops: run (docs/40 - DevDocs/prompts/SHADOW-HUB.md)` · `offline 8796/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-read-grant-1019-offline-20261019-092625.log`. In the log: `941:4730 passed, 866 skipped, 4 xfailed, 36 warnings in 788.33s (0:13:08)`, `1015:4066 passed, 1 xfailed, 16 warnings in 908.84s (0:15:08)`. The tests this build adds are named in `## E2 RED`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gemini-read-grant-1019 livenote` → `live-note 147/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gemini-read-grant-1019-livenote-20261019-095513.log`. `grep -n -F "COBALT_LIVE_VAULT_ROOT not set" <log>` → nothing.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `4066 passed, 1 xfailed, 16 warnings in 908.53s (0:15:08)`.
- with-DB: not run (DB: none). (b) to (d) and (f): not run (DB: none).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red. The C1 outside cases, every T1 test, and the C1 hub, H2, H3 and changed `x1_paragraph` tests were red on BASE (`## E2 RED`). The mutations made red C1 (5 cases), C2 (the pin), T1 (3) (6 shapes), the T1 guard exemption, H2 and H3 (`## E3`). The C1 controls and the C2 pin were green on BASE, as the card says. Not mutated one by one: each T1 refusal test, though each was red on BASE for the missing kind. — 3 of 3 by the hub's rule (red against BASE or a mutation).
(2) Callers: `grep -rn -F "builder_call(" ops/desk` → `:1118` (a shell `-c` body) and `:1121` (the launch). `:1121` is pinned by every C1 test. `:1118` returns G7 for any `-c` body (a builder call is never wrapped). The cwd check sits inside `builder_call`, so it also judges a `-c` body, which is still G7. The kind `x1-copy` has one entry, `desk-launch.sh x1-copy`; its arg count, name, leg, link, existing-copy, cli.log, workspace, conversation, stale and transcript paths are each pinned by a T1 test. The desk-size guard is pinned for both x1-copy and grant-sweep. — 3 of 3.
(3) Re-read at the tip: the P1 greps (`:1218`, `:12`, `:30`, `:1155`) ran after `ad4c8dfe`; `git log --oneline 0ac7746e..HEAD` → the two commits; `grep -c -F "cli.log"` on the hub → `1`; `git diff --name-only` as quoted. — 3 of 3.

## FOR THE CHECK
- Range `0ac7746e..ad4c8dfe`: `4a215342 wip(gemini-read-grant-1019): red`; `ad4c8dfe feat(gemini-read-grant-1019): Gemini call only from its worktree, x1-copy kind, X1 per leg, builder no-fetch text (C1, C2, T1, H2, H3; L1, L3, L67)`.
- Per row: reds, mutations and greens are in `## E2 RED` and `## E3 THE ROWS`; P1's output is quoted whole there.
- Caller greps: `## PRE-STOP SELF-CHECK` (2).
- Suites: offline 8796/0, live-note 147/0, tests/ops 4066 passed (`## W`). With-DB: not run (DB: none). `<F0>`/`<F1>`/`<F2>`: not run (DB: none). Lock taken/released: not run (DB: none).
- RESTARTS table: `## RESTARTS`.
- Records copied at PREFLIGHT: `## PREFLIGHT`.
- For X1 (CHECK ASKS): the cwd test is a fixed-string `!=` on the hook `cwd` after `seat`'s `normpath`. A `..` path that normalizes to `<target>` is admitted as `<target>`; a symlink to the worktree, a case variant, or an empty or relative `cwd` (made `""` by `seat`) is refused. Grok, Sonnet and Terra calls are unchanged (`test_c1_the_pin_is_gemini_only`, `test_s3_…`).
- For X4: the per-word compare `[ "$w" = "$WT/$xwt" ]` runs with `set -f` and `IFS=' '`. Every `grep` is `-F`. The id is checked by `case` on `*[!0-9a-f-]*` and `${#id} -eq 36`. The source must be a regular file and not a link. The destination worktree must not be a link, and neither copy may exist (`-e` or `-L`). Only `soft-denying` lines are copied from `cli.log`.

## CONTINUE
next: CLOSE (done at the stop line)

## DECISIONS
- DECISION H2 (ASK DESK, 10:11 from `date`): the card's H2 test says the `X1 for Gemini` line "does not hold … `cli.log`". The card's own replacement text, copied whole as H2 orders, holds `cli.log` once, in verdict (1)'s parenthesis: `cli.log still points at leg 0e's run` (amend 838's NOTE 1). `grep -c -F "cli.log"` on the hub → `1`. The two cannot both hold. The default taken: the hub text is verbatim, and `test_h2_…` asserts every other part and every other absent string (`X1 WRITE OK`, `the seat runs pass 0. Before pass 0`, `x1-transcript.sh`, `/Users/cobalt/.gemini`) but not `cli.log`. The desk may instead reword verdict (1) and restore the assert. The X1 text names `cli.log` only to explain why x1-copy is not run for a blocked leg 0f; the seat is still told to read nothing under `/Users/cobalt/.gemini`.
- DECISION 2 (UNPROVEN, carried from the card's `## RECORDS`, THE GUARD): whether the hook event's `cwd` follows the seat's `cd` is not proven by this build (CHECK ASKS X2). C1 holds only if it does. H2's leg 0f is the live proof, and verdict (1) stops the arm if the guard admits agy from `x1-canary`. The default taken: built as carded; the live proof is the desk's 717 relaunch (OWED).

## RECORDS
- L74: one system block in this session asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- One test beyond the card's list: `test_t1_an_id_that_is_not_36_hex_characters_is_refused`. It pins check (4)'s id rule, which CHECK ASKS X4 names; it is in T1's file and widens no row.
- DevDocs: there is no module page under `docs/40 - DevDocs/cobalt/` for `ops/desk/bare-guard.py` or `ops/desk/desk-launch.sh` (`Grep` for `desk-launch|bare-guard` under `docs/40 - DevDocs` outside `reports/`, `prompts/` → only `plans/fixed-files-2026-09-30/*`, `cobalt/jobs/restarts.md`, `SESSION-CLOSE.md`). None was created; the cards before this one that changed these files added none either.
- No extra lock take (DB: none). No `REFUSED, not needed` line. No `CONTINUED` line.
- The card's records, as re-read at PREFLIGHT, are in `## PREFLIGHT`. OWED (the desk's, after the deploy): `grant-sweep` if 717's write rule is still in the settings file, D1, then `desk-launch.sh shadow <717 card> --model gemini-4-argon-high` once; 718 and 719 after, one at a time.
- `.env`: never present in this worktree (DB: none).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: gemini-read-grant-1019 · tip: ad4c8dfe | on 0ac7746e | migration: none | offline 8796/0 | with-DB 0/0 | live-note 147/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 223806
