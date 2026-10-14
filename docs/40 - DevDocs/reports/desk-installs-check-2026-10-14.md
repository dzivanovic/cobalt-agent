# desk-installs-1014 — check report (2026-10-14)

## §0 Headline
- Check of card 549 (I1, I2, S1, R3) on `4bc73283`. House A Grok (`FINDINGS: 1`). No house B: Gemini's probe was OUT, and `HOUSE B: as needed`.
- 7 findings (6 mine, 1 Grok's). I ran every one. Held 0, fixed 0, open 0. O5 (stale `STANDING-LIST.md:173`) is OUT OF SCOPE (the fence).
- Suites on the tip: offline 4328/0 · live-note 146/0 · `tests/ops` 3603 passed / 0 failed. `cobalt_dev: not taken` (DB: none). `.env` absent. `RESTARTS: none`.
- I made no commit. ready: YES.

## L74
A system note at session start asked for a `Claude-Session:` line on commits. Recorded here and not followed: no commit was made, and CHECK-HUB L74 allows only `Co-Authored-By`.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 0 · 1a855e4b9b934876c5da87f8e880973b84e7769e
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-14/549-desk-installs-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 11:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (at AUTHORIZATION and again at 08:32 before the launch): `grep -n "^| R17 "` → one row (`35:| R17 | 07:32 ET | …`). `grep -n "^| R19 "` → one row (`37:| R19 | 07:36 ET | …`). `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty). At the launch I typed `grep -c` instead of `grep -n`: `1` and `1`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Wed Oct 14 08:30:35 EDT 2026
status · git status --short --branch · 0 · ## ops/desk-installs-1014
head · git log --oneline -1; git log --stat --format=%h 4bc73283..HEAD · 0 · (5 lines)
    d72ee2ac docs(desk-installs-1014): build report — 4bc73283
    d72ee2ac
    
     .../reports/desk-installs-build-2026-10-14.md      | 70 +++++++++++++++++++---
     1 file changed, 61 insertions(+), 9 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/desk-installs-1014/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/desk-installs-1014/docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md" · 0 · BUILT · job: desk-installs-1014 · tip: 4bc73283 | on 6ee9b8d6 | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 161189
range · git log --oneline 6ee9b8d6..4bc73283 · 0 · (4 lines)
    4bc73283 fix(desk-installs-1014): the rule sweep holds a floor and zero mismatches, not a count (S1, L79, R1476)
    d77c0e9c wip(desk-installs-1014): W — tests/ops red outside the rows (test_the_rule_sweep 21 vs 18, from 8b813ca7)
    6ff7d9a4 feat(desk-installs-1014): SendMessage on the desk line and its STANDING-LIST §4 row; launch-line BASE pin repaired (I1, I2; L81 K5, R1471)
    7e1f3020 wip(desk-installs-1014): red — I1, I2 tests
PREFLIGHT OK
```
- THE RANGE, typed (`git log --stat --format=%h 6ee9b8d6..4bc73283`, exit 0): `4bc73283` `tests/ops/test_the_rule_sweep.py` (+9 −5) · `d77c0e9c` `docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md` (+139) · `6ff7d9a4` `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` (2 ±), `docs/40 - DevDocs/prompts/STANDING-LIST.md` (+1), `tests/ops/test_desk_refresh_wakeup.py` (+1 −14) · `7e1f3020` `tests/ops/test_desk_installs_1014.py` (+106).
- DB: none. `git diff --name-only --no-renames 6ee9b8d6..4bc73283` (exit 0) prints `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md`, `tests/ops/test_desk_installs_1014.py`, `tests/ops/test_desk_refresh_wakeup.py` and `tests/ops/test_the_rule_sweep.py`. Every path is under `tests/ops/` or `docs/`.
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- House probes (`house-probe.sh --card "<card>"`, exit 0):
  ```
  grok: UP
  gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
  ```
  The card has no `HOUSE A` header line, so OpenAI was not probed. **house A: grok · house B: none (not needed)** (`HOUSE B: as needed`). Gemini's OUT is a HARNESS line (a model-name error), not a meter.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` (exit 0):
```
8058 <S>/diff.md
17093 <S>/files/549-desk-installs-card.md
23565 <S>/files/desk-installs-build-2026-10-14.md
13774 <S>/files/wt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md
46296 <S>/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
16600 <S>/files/wt/docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md
3776 <S>/files/wt/tests/ops/test_desk_installs_1014.py
2723 <S>/files/wt/tests/ops/test_desk_refresh_wakeup.py
6875 <S>/files/wt/tests/ops/test_the_rule_sweep.py
350 <S>/rulings.md
STAGED 10 files · 139110 bytes · commits 3
```
`commits 3` against PREFLIGHT's 4. The diff runs over `-- . ":(exclude)docs"`, and `git log --oneline 6ee9b8d6..4bc73283 -- . ":(exclude)docs"` prints three commits (`4bc73283`, `6ff7d9a4`, `7e1f3020`). The fourth, `d77c0e9c`, touches only a docs file, so the diff's own pathspec excludes it. I read the counts as matching (see `## RECORDS`).
`stage-copy.sh` (each exit 0):
- `COPIED 16230 <S>/files/survey-blockers-2026-10-12.md`
- `COPIED 25054 <S>/files/cto-2026-10-14.md`
- `COPIED 1439 <S>/files/cto-2026-10-14-words.md`
- `COPIED 127758 <S>/files/wt/ops/desk/desk-launch.sh`
- `COPIED 13550 <S>/files/wt/tests/ops/test_hub_lines.py`
- `COPIED 16425 <S>/files/537-deploy-smoke-string-card.md`
- `COPIED 18862 <S>/files/523-hub-text-card.md`

LAWS.md was not copied (the hub's rule). `<S>/HOUSE-INSTRUCTIONS.md` holds the HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS and RECORDS, and the Files paragraph. `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/desk-installs-1014-check`.

## OWN FINDINGS
I wrote these before opening any house file.

FINDING O1
ROW: X1
CLAIM: the diff of the two docs files holds more than one changed line at `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md:13` and one added line at `docs/40 - DevDocs/prompts/STANDING-LIST.md:167`.
RUN: COMMAND `git diff -U0 6ee9b8d6 4bc73283 -- "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: a hunk other than `@@ -13 +13 @@` (wake-up) and `@@ -166,0 +167 @@` (list), or a changed byte of `:13` outside the inserted ` "SendMessage"`.

FINDING O2
ROW: X2
CLAIM: kind `desk` of `ops/desk/desk-launch.sh:545-563` refuses the new line, or does not hand `SendMessage` to the session inside its `--allowedTools`. No test runs kind `desk` on the real wake-up: the `Desk` class of `tests/ops/test_hub_lines.py:185-268` stages only the four hubs.
RUN: TEST `tests/ops/test_desk_installs_1014.py` · `test_x2_desk_launch_desk_hands_the_session_sendmessage_in_its_allow_list(tmp_path)`. It builds a tmp repo holding the real wake-up, committed, and a stub `claude` that records its arguments. It runs `sh ops/desk/desk-launch.sh desk` dry (`DESK_LAUNCH_DRY=1`) and asserts the printed line's `--allowedTools` holds `SendMessage` once. It then runs it for real and asserts the recorded arguments between `--allowedTools` and `--disallowedTools` hold `SendMessage` once, as the last string. The full function was pasted as written in the run (`## RUNS`) and removed again.
EXPECT: a refusal (`returncode` 1, the `refuse` line on stderr), or `SendMessage` missing from the session's allow arguments.

FINDING O3
ROW: X2
CLAIM: `ops/desk/desk-launch.sh` changes in `6ee9b8d6..4bc73283`.
RUN: COMMAND `git diff --stat 6ee9b8d6..4bc73283 -- ops`
EXPECT: a line naming `ops/desk/desk-launch.sh`.

FINDING O4
ROW: X3
CLAIM: a test or script besides `tests/ops/test_desk_installs_1014.py` holds the desk's whole `- LAUNCH ` line, found by the old end of its allow list.
RUN: COMMAND `grep -rn -F 'merge-base*)" --disallowedTools' tests ops`
EXPECT: a hit in `tests/` or `ops/` (the wake-up itself is under `docs/`, which is not searched).

FINDING O5
ROW: I2 / X4
CLAIM: `docs/40 - DevDocs/prompts/STANDING-LIST.md:173` still reads `NEW strings left on the desk line: the five deny strings, no allow.` That is false once `:167` adds a NEW allow. The card keeps the line unchanged.
RUN: COMMAND `grep -n -F "the five deny strings, no allow." "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: `173:STRUCK IN LOOP 2: … NEW strings left on the desk line: the five deny strings, no allow.`

FINDING O6
ROW: S1
CLAIM: `tests/ops/test_the_rule_sweep.py:149-154` fails on the tip, where the window holds 21 check reports, above the floor of 18.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py`
EXPECT: a failure of `test_the_sweep_swept_what_it_pins`.

## Findings
| id | house | row | claim | form |
|---|---|---|---|---|
| G1 | grok (house A) | S1 | The build report `:6` still says `STOPPED at W … Waiting for the desk's CONTINUE` and quotes the old red, while the test on the tip has `CHECKS_FLOOR = 18` | COMMAND (`grep`) |

House B: none (not needed; Gemini OUT at the probe).

## Dropped
none. G1's `RUN:` line is followed by one `grep` command line.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | `git diff -U0 6ee9b8d6 4bc73283 -- <wake-up> <list>` | two hunks only: `@@ -13 +13 @@` (`:13` identical except ` "SendMessage"` inserted after `"Bash(git -C * merge-base*)"` and before ` --disallowedTools`) and `@@ -166,0 +167 @@` (the new `` | `SendMessage` | **NEW** (one allow string, class K5 of L81, his 2026-10-14 R1471; … `` row, the card's text byte for byte) | NOT HELD (X1: yes) |
| O2 | opus | the test above, pasted into `tests/ops/test_desk_installs_1014.py`, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_installs_1014.py::test_x2_desk_launch_desk_hands_the_session_sendmessage_in_its_allow_list` | `1 passed, 15 warnings in 1.01s` | NOT HELD (X2: the dry and the real launch of kind `desk` both hand `SendMessage` to the session, last in the allow list); removed again with Edit, `git status --short --branch` → `## ops/desk-installs-1014` |
| O3 | opus | `git diff --stat 6ee9b8d6..4bc73283 -- ops` | (nothing) | NOT HELD (X2: `desk-launch.sh` unchanged) |
| O4 | opus | `grep -rn -F 'merge-base*)" --disallowedTools' tests ops` | (nothing, exit 1) | NOT HELD (X3: no other whole-line pin) |
| O5 | opus | `grep -n -F "the five deny strings, no allow." "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | `173:STRUCK IN LOOP 2: the first draft's NEW allow `Bash(git -C /Users/cobalt/cobalt worktree add *)` — `desk-launch.sh` runs the `worktree add`. NEW strings left on the desk line: the five deny strings, no allow.` | REJECTED — card I2: "`:172` (`NEW strings left on the desk line: the five deny strings, no allow.`) … stand unchanged" and `## NOT IN THIS JOB` ("every other line of `STANDING-LIST.md` but the one new row"): OUT OF SCOPE |
| O6 | opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` | `5 passed, 15 warnings in 1.49s` | NOT HELD |
| G1 | grok | `grep -n -e "Waiting for the desk" -e "CHECKS_FLOOR = 18" "docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md" "tests/ops/test_the_rule_sweep.py"` | `docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md:131:The edit: `CHECKS_SWEPT: int \| None = 18` / … → `CHECKS_FLOOR = 18` …` and `tests/ops/test_the_rule_sweep.py:62:CHECKS_FLOOR = 18` | NOT HELD. No `Waiting for the desk` line: Grok read the staged report as of `TIP` (`d77c0e9c`, the stop at W). The final report is the docs commit `d72ee2ac` above `TIP`, and it records S1 as fixed (`### CONTINUED at W`). |

Nothing held, so there is no `wip(desk-installs-1014): check red` commit.

## FIXES
none (nothing held).

## Suites
This card is DB: none. W as `BUILD-HUB.md` gives it ((a0), (a), (e), and `tests/ops`), on the tip `4bc73283` (HEAD `d72ee2ac`, one docs-only commit above it):
- RESTARTS: `uv run cobalt jobs restarts 6ee9b8d6..HEAD` (exit 0):
  ```
  path	change	rule	restart
  docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
  docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
  docs/40 - DevDocs/reports/desk-installs-build-2026-10-14.md	A	DOCS	-
  tests/ops/test_desk_installs_1014.py	A	test/documentation; no resident	-
  tests/ops/test_desk_refresh_wakeup.py	M	test/documentation; no resident	-
  tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
  RESTARTS: none
  ```
- (a0): `git diff --name-only --no-renames 6ee9b8d6` prints the six paths above, all under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- (a): `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 offline` → exit 0: `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-installs-1014-offline-20261014-085021.log`.
- (e): `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-installs-1014 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-installs-1014-livenote-20261014-085021.log`. Its one skip (`grep -n -F "SKIPPED"` of the log): `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3603 passed, 1 xfailed, 16 warnings in 760.32s (0:12:40)`. `grep -c -F "SKIPPED"` of its output → `0`.
- with-DB: not run (DB: none).
- `.env`: `ls /Users/cobalt/cobalt-wt/desk-installs-1014/.env` → `No such file or directory`. It was never present and no lock was taken.

## Scope
PREFLIGHT's path union is the six paths above: the two docs files and three test files the rows name, plus the build report. My commits: none. Every non-report path is in a row's `files`. `tests/ops/test_the_rule_sweep.py` is S1's file.

## Checked against the branch
- (i) `git log --oneline 4bc73283..HEAD -- . ":(exclude)docs"` prints nothing: no commit of mine, so `<tip now>` = `4bc73283`.
- (ii) `git log --stat --format=%h 4bc73283..HEAD` → `d72ee2ac` · `.../reports/desk-installs-build-2026-10-14.md | 70 +++++++++++++++++++---` (docs only).
- (iii) `git log --oneline 6ee9b8d6..HEAD -- ops/desk/desk-launch.sh .claude src configs` prints nothing: the fence is empty.
- (iv) No held finding, so there is nothing to check.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/desk-installs-1014`.
- (vi) `git log --stat --format=%h 6ee9b8d6..HEAD -- src/cobalt/db_migrations tests/cobalt` prints nothing: no migration and no with-DB test, so the gate lists are not needed.
- (vii) Card records:
  - `git -C /Users/cobalt/cobalt diff --stat HEAD -- "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md" ops/desk/desk-launch.sh` prints nothing (as recorded).
  - Record "Cards 546, 547 and 548 did not exist … UNPROVEN": `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-14"` now lists `546-deploy-freeze-card.md`, `547-db-copy-card.md`, `548-result-file-card.md` and `550-card-template-card.md`. `grep -l -F "CTO-DESK-WAKEUP"` of the four prints nothing. `grep -l -F "STANDING-LIST"` names 546 and 547. Their hits read `STANDING-LIST.md` `## CLASSES`, `:25`, `:109` and `:139-140`, none of them §4 (`:159-173`). No overlap with this card.
  - X3's grep: O4 above, nothing.
- (viii) L32: this report holds no ticker, price or date of his. The dates are run clocks and file names.

COUNTING: findings 7 (opus 6, house A 1) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0 (O5 is OUT OF SCOPE by the card, not open).

## OPEN
none. OUT OF SCOPE: O5, `STANDING-LIST.md:173` "the five deny strings, no allow." is now stale (one NEW allow stands at `:167`). The card keeps it unchanged (I2, `## NOT IN THIS JOB`; the drafter's ASK DESK default: not edited). A later card may restate it.

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
none.

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: Gemini did not sit. Its probe line: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; the model name the CHECK-HUB Gemini line pins is not recognized by `agy`). House B was not needed (`HOUSE B: as needed`).
- Grok: started 08:32 EDT, notice at 08:49:31 EDT. It wrote `<S>/house-a.md` itself (845 bytes, `FINDINGS: 1`). Its stdout named the path.
- Grok's staged copy of the build report was the `TIP` version (`d77c0e9c`, the stop at W), not HEAD's `d72ee2ac`. `stage-set.sh` stages from git at `TIP`. That is why G1 saw a stale "Waiting" line.
- stage-set's `commits 3` against PREFLIGHT's 4: the diff's pathspec excludes `docs`, and the one docs-only commit `d77c0e9c` drops out (`git log --oneline 6ee9b8d6..4bc73283 -- . ":(exclude)docs"` → 3 commits). I read the counts as matching and did not fail the copy.
- `REFUSED, not needed: git diff 6ee9b8d6..4bc73283 -- tests docs/40\ -\ DevDocs/prompts — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` I read the staged `diff.md` and ran the quoted `git diff -U0` instead.
- O2's test was written, run green, and removed with Edit. The tree is clean.
- Lock takes: none (DB: none).
- `tokens:` `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 339603b5-7817-4a81-99de-e6058748da5a` → `context 154389 of 400000 — ok`.
- files opened: 12. `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); the build report (`## RESTARTS` to the last line); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `ops/desk/desk-launch.sh` (`:225-314`, `:330-374`, `:530-574`); `STANDING-LIST.md` (`:155-174`); `tests/ops/test_the_rule_sweep.py`; `tests/ops/test_hub_lines.py`; `<S>/diff.md`; `<S>/house-a.md`; `tests/ops/test_desk_installs_1014.py` (Edit, O2). I also read the background-task outputs of the probe, Grok, the two gates and `tests/ops`.
- Check of `desk-installs-1014`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: desk-installs-1014 · pass: 1 · tip: 4bc73283 · house A: grok FINDINGS: 1 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 154389
