# deploy-card-fixes-1018 — build report 2026-10-18 (routed, BAND LOW, builder grok-4.7, gate seat Opus 5.5)

## §0 Headline
D1 is built by grok-4.7 in two passes, T and S, with no S2. `deploy-card.sh` now refuses a job whose code tip is already an ancestor of main: one new line after `:552` and one header clause. The new test was red on BASE (exit 0, card written) and is green at the tip.
Tip `cc4995b6` on BASE `279c99ce`. Results: offline 8493/0, live-note 146/0, tests/ops 3921 passed, DB: none (no lock), RESTARTS: none on the committed range.
The DEPLOY PROOF marker reads `2`. Decisions: 2, neither for Dejan. One is the restarts read of the untracked harness file. The other is the unpinned fix-round entry path of the new refusal (self-check 2 of 3).

## L74
The session's attribution reminder asked for a `Claude-Session:` line on commits (data, L74). Not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md"` (06:33 EDT):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md" · 0 · 3de69cfd3090fffdce7097597b9be0ccfc73517e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 24:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED — pending fold |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"`:
```
clock · date · 0 · Sun Oct 18 06:33:47 EDT 2026
status · git status --short --branch · 0 · ## ops/deploy-card-fixes-1018
head · git log --oneline -1 · 0 · 279c99ce docs(desk): rename prompt 720 (launcher refuses -card.md names)
diff · git diff --stat 279c99ce · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/deploy-card-fixes-1018 · 0 · 279c99ce docs(desk): rename prompt 720 (launcher refuses -card.md names)
env here · ls /Users/cobalt/cobalt-wt/deploy-card-fixes-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
The card has no `SHADOW OF:`. It is a routed card (BAND: LOW → `grok-4.7`, per the band table under SHADOW-HUB `## BUILDERS`), so its stop line is BUILD-HUB's `BUILT ·`.

| rule | command | exit | output |
|---|---|---|---|
| BASE stat | `git show --stat 279c99ce` | 0 | `docs(desk): rename prompt 720 (launcher refuses -card.md names)` · 1 file changed, 1 insertion(+), 1 deletion(-) |
| ancestor refusals | `grep -n -F "merge-base --is-ancestor" ops/desk/deploy-card.sh` | 0 | `541: … "$ctip" "$fixtip" …` · `550:    git -C "$REPO" merge-base --is-ancestor "$ctip" "$head" \|\| refuse "$job: code tip $ctip is not an ancestor of the head $head of $branch"` |
| header clause | `grep -n -F "the code tip is not an ancestor of the head;" ops/desk/deploy-card.sh` | 0 | `10:# \`ready: YES\`, or names no tip; the code tip is not an ancestor of the head; the head adds` |
| marker before | `grep -c -F "already an ancestor of main" ops/desk/deploy-card.sh` | 0 | `0` |
| Desk fixture | `grep -n -F "class Desk" tests/ops/test_deploy_card.py` | 0 | `47:class Desk:` |
| wc | `wc -l ops/desk/deploy-card.sh tests/ops/test_deploy_card.py` | 0 | `644` · `1442` |
| READ report | `tail -n 3 ".../reports/cto-2026-10-15.md"` | 0 | last line `HANDOVER: predecessor f8f8324b → successor 8e552225 at 19:24 · pane w2:pV1` |
| restarts | `uv run cobalt jobs restarts 279c99ce..HEAD` | 0 | `RESTARTS: none` (empty range) |

These lines were read by content at BASE with the Read tool: `:520` `ctip=…`, `:521` `head=…`, `:541-542` the fix round (`ctip=$fixtip`), `:550` the head-ancestor refusal, `:551-552` the docs-only refusal, and `:566-576` DEPLOY PROOF. In the tests, `tests/ops/test_deploy_card.py:47-130` is `Desk`: alpha branches off main, and `:100-101` commits "checks and cards" on main after it. The card's `## RECORDS` were re-read against these and they hold.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 771.94s (0:12:51)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.88s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
`SHADOW-INSTRUCTIONS.md` was written: the whole card, the R1833 row, no exceptions, BUILD-HUB E2 and E3 verbatim, and the fence (`ops/desk/deploy-card.sh`, `tests/ops/test_deploy_card.py`). It stays untracked.
Pass T (see `## PASSES`) wrote `test_d1_a_tip_already_on_main_is_refused` at the end of `tests/ops/test_deploy_card.py` (+19). It was committed as `d901a764 wip(deploy-card-fixes-1018): red`.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py -k d1` on the BASE script → `1 failed, 143 deselected, 15 warnings in 1.39s`. The first red line, `E       AssertionError: deploy-card: …/03-deploy-x-set-card.md written (1 job(s), TIP bca0931a)` / `E       assert 0 == 1`, is the row's named reason: exit 0 and the card written. The CONTROL (main's short hash in stderr) is an assert in the same test and is red on BASE with it.

## E3 THE ROWS
Pass S changed `ops/desk/deploy-card.sh` (+2 −1) and was committed as `cc4995b6 feat(deploy-card-fixes-1018): rows`. The diff:
```
-# `ready: YES`, or names no tip; the code tip is not an ancestor of the head; the head adds
+# `ready: YES`, or names no tip; the code tip is not an ancestor of the head; the code tip is already an ancestor of main; the head adds
@@ -550,6 +550,7 @@
     [ -z "$past" ] || refuse "$job: the head $head adds paths outside docs/ past the code tip $ctip: $(printf '%s' "$past" | tr '\n' ' ')"
+    git -C "$REPO" merge-base --is-ancestor "$ctip" refs/heads/main && refuse "$job: code tip $ctip is already an ancestor of main $(git -C "$REPO" rev-parse --short=8 refs/heads/main); nothing to deploy"
```
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_card.py -k d1` → `1 passed, 143 deselected, 15 warnings in 1.11s`.
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_card.py` → `144 passed, 15 warnings in 61.31s`. This is CONTROL 2: the existing unmerged runs stay green, unedited.
- `grep -c -F "already an ancestor of main" ops/desk/deploy-card.sh` → `2`, the DEPLOY PROOF's after value.
- MUTATION: the seat never edits `ops/` or `tests/` (SHADOW-HUB RULES; guard G5, kind shadow). The undone fix is therefore the BASE script at `d901a764`, and D1's red there (E2, above) is the mutation red. No DevDocs module page names `deploy-card` (Grep of `docs/40 - DevDocs/cobalt` → no files), so no page line is written.

## RESTARTS
`uv run cobalt jobs restarts 279c99ce..HEAD` exits 1. The tool also reads untracked files (`git ls-files --others`, `src/cobalt/jobs/restarts.py:90`):
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The committed range, `uv run cobalt jobs restarts 279c99ce..cc4995b6` → exit 0:
```
path	change	rule	restart
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
RESTARTS: none
```
The untracked harness file is not classified (DECISIONS 1, as on the shadow checks of 2026-10-11).

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 279c99ce` → `ops/desk/deploy-card.sh` · `tests/ops/test_deploy_card.py`. Every path is under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-card-fixes-1018 offline` → exit 0:
  ```
  tests/ops: run (ops/desk/deploy-card.sh)
  offline 8493/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-card-fixes-1018-offline-20261018-065200.log
  ```
  This build adds one test, `tests/ops/test_deploy_card.py::test_d1_a_tip_already_on_main_is_refused`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-card-fixes-1018 livenote` → exit 0:
  ```
  live-note 146/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-card-fixes-1018-livenote-20261018-072110.log
  ```
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3921 passed, 1 xfailed, 16 warnings in 966.05s (0:16:06)`.
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/deploy-card-fixes-1018/.env` → `No such file or directory`.

## PASSES
| pass | env check | command as run | wall | builder tokens | diff stat | commit |
|---|---|---|---|---|---|---|
| T | `ls -la /Users/cobalt/cobalt-wt/deploy-card-fixes-1018/.env` → `No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/deploy-card-fixes-1018/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. Reply with the list of files you wrote."` | 06:48:30 → 06:49:40 (1.2 min) | UNKNOWN (Grok prints none, L70) | `tests/ops/test_deploy_card.py \| 19 +++` · 1 file changed, 19 insertions(+) | `d901a764 wip(deploy-card-fixes-1018): red` |
| S | same → `No such file or directory` | the same command with `Pass S: the rows.` | 06:49:52 → 06:50:28 (0.6 min) | UNKNOWN | `ops/desk/deploy-card.sh \| 3 ++-` · 1 file changed, 2 insertions(+), 1 deletion(-) | `cc4995b6 feat(deploy-card-fixes-1018): rows` |

Grok's replies: T `- tests/ops/test_deploy_card.py`, S `- ops/desk/deploy-card.sh`. No S2 pass was needed; suites at first run: green. Every path is inside the fence: no SCOPE.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its named reason. `test_d1_a_tip_already_on_main_is_refused` was red on the BASE script (`assert 0 == 1`, card written; E2) and green at `cc4995b6` (E3).
(2) The new line sits on one entry path: the per-job loop, after `:552`, read for every card. The plain path (no `--fix-report`, tip merged into main) is pinned by D1. The fix-round path (`ctip=$fixtip`, `:542`, with that fix tip merged into main) is pinned by no test. It is named under DECISIONS 2 and not pinned here, because the seat writes no test and the card's row names none.
(3) Each figure was re-read from tool output at the tip. `git show cc4995b6:ops/desk/deploy-card.sh` shows `:10` with the clause. `grep -c -F "already an ancestor of main" ops/desk/deploy-card.sh` → `2`. `git diff --name-only --no-renames 279c99ce` lists two paths. The suites were run on `cc4995b6`.

## FOR THE CHECK
- `279c99ce..cc4995b6`: `d901a764 wip(deploy-card-fixes-1018): red` · `cc4995b6 feat(deploy-card-fixes-1018): rows`.
- D1's red, green and mutation are as quoted in E2 and E3. CONTROL 2 is the whole file at 144 passed.
- X1: the only added script line is `:553`, plus the header clause on `:10` (diff in E3). It sits after `:542` (`ctip=$fixtip`), so it reads the fix tip on a fix round.
- X2: the existing tests, unedited, are green at the tip (144 passed). That covers the unmerged runs with and without `--fix-report`, including `test_a_fix_report_fills_the_ships_row_cell_and_code_tip`.
- Note: the header line `:10` is now 137 characters, unwrapped (the instructions allowed a rewrap). `already an ancestor of main` stays on one line, as the card requires.
- Suites: offline 8493/0 and live-note 146/0 (commands and logs in W), tests/ops 3921 passed, with-DB not run (DB: none). F0/F1/F2: not run (DB: none). Lock: not run (DB: none).
- RESTARTS tables are in `## RESTARTS`. The records copied at PREFLIGHT are in `## PREFLIGHT`.

## CONTINUE
next: done (the desk verifies the artifact, L35, and launches the check)

## DECISIONS
1. `uv run cobalt jobs restarts 279c99ce..HEAD` reads the untracked `SHADOW-INSTRUCTIONS.md` and exits 1 UNCLASSIFIED. The default taken is the one the 2026-10-11 shadow checks took: the harness file is not classified in `jobs.yaml`. The committed range `279c99ce..cc4995b6` derives `RESTARTS: none`, which the stop line carries. X9 (the file's ignored path) settles this. Not for Dejan.
2. No test pins the new refusal on the fix-round path, where a `--fix-report` fix tip is already merged into main. The line reads `ctip` after `:542`, so it applies there by construction. The default taken is to leave it unpinned here: the row names one test and the seat writes no test. The check may pin it. Not for Dejan.

## RECORDS
- The card's records were re-read at PREFLIGHT (`:550`, `:551-552`, `:542`, `:8-11`, `Desk :47-120`, `:100-101`): they hold.
- Builder: grok-4.7 (BAND LOW, routed). Gate seat: this session, Opus 5.5. Passes: 2 (T, S), with no S2. Builder wall: 1.8 min. Seat wall: 06:33 → 07:38 (65 min).
- `SHADOW-INSTRUCTIONS.md` is the one untracked file, as the launcher allows (card 386 L4).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-card-fixes-1018 · tip: cc4995b6 | on 279c99ce | migration: none | offline 8493/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 2 of 3 | decisions: 2 · for Dejan: 0 · tokens: 151180
