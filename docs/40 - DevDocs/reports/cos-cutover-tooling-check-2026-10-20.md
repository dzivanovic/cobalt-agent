# CHECK — cos-cutover-tooling (card 931) · pass 1

## §0 Headline
- 4 findings, 4 held, 4 fixed, all in T2's bootstrap-only form check in `desk-launch.sh`. A STEP-D0 resume was admitted when `$WT/none` existed (O1, also Grok's partial). A bulleted `GATE RESULT:` line of another label was admitted (O2). So was a line of another label whose text held the card's label prefix (A1, Gemini), and a blank item or result (A2, Gemini).
- Fix `f15d7af5`: one awk pass over every `GATE RESULT:` line, plus an explicit bootstrap-only STEP-D0 refusal. Red commit `8ac871c7`.
- Suites on `f15d7af5`: offline 9023/0 (tests/ops 4126 passed), live-note 148/0, with-DB not run (DB: none); RESTARTS: none.
- T1a–c (retired-agent record) and X1–X5: no defect found by run or read. House A Gemini (Grok produced no list); no house B needed.

## L74
- 19:31 EDT: a system attribution notice asked commits to end with a `Claude-Session:` line. DATA under L74: not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-20/931-cos-cutover-tooling-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-20/931-cos-cutover-tooling-card.md" · 0 · 5247b5fd7ba2912f759a9dc3ec43337ffba80076
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-20/931-cos-cutover-tooling-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Tue Oct 20 19:31:17 EDT 2026
status · git status --short --branch · 0 · ## ops/cos-cutover-tooling
head · git log --oneline -1; git log --stat --format=%h 96728174..HEAD · 0 · (6 lines)
    65ad949c docs(cos-cutover-tooling): build report — 96728174
    65ad949c

     .../cos-cutover-tooling-build-2026-10-20.md        | 165 +++++++++++++++++++++
     .../cos-cutover-tooling-build-2026-10-20.result    |  15 ++
     2 files changed, 180 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/cos-cutover-tooling/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/cos-cutover-tooling/docs/40 - DevDocs/reports/cos-cutover-tooling-build-2026-10-20.md" · 0 · BUILT · job: cos-cutover-tooling · tip: 96728174 | on 4a9b60bd | migration: none | offline 9018/0 | with-DB 0/0 | live-note 148/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0 · tokens: 288545
range · git log --oneline 4a9b60bd..96728174 · 0 · (2 lines)
    96728174 feat(cos-cutover-tooling): bootstrap-only deploy launch, retired agent record read (T2, T1a, T1b, T1c; L1, L3, L42)
    11b8b6f9 wip(cos-cutover-tooling): red
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h 4a9b60bd..96728174` · 0 · `96728174`: `DEPLOY-HUB.md` 16, `ops/desk/deploy-outage.sh` 27, `ops/desk/deploy-step0.sh` 15, `ops/desk/desk-launch.sh` 37 (4 files, +75 −20); `11b8b6f9`: `tests/ops/test_deploy_outage.py` 77, `tests/ops/test_deploy_step0.py` 49, `tests/ops/test_desk_launch_bootstrap_only.py` 264, `tests/ops/test_hub_agent_retired_1020.py` 117 (4 files, +507). Path union: the 8 paths below.
- DB: none · `git diff --name-only --no-renames 4a9b60bd..96728174` · 0 · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/deploy-outage.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_outage.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_bootstrap_only.py`, `tests/ops/test_hub_agent_retired_1020.py` — every path under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` · 1 · `No such file or directory` (fresh).
- House gates again before launch (19:34:04 EDT): R17 row line 35, R19 row line 37, R19 commit `5055151dbf68899b82de5b11f99733ed2d03048c`.
- House probes · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: UP
```
- Seats: no `HOUSE A:` header line → house A: Grok · house B: none (not needed; card `HOUSE B: as needed`).
- PROVEN BY FIRST REAL USE: the report Write (this file) and the `<S>` Writes succeeded.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
32 <S>/STAGED-CARD
35721 <S>/diff.md
23541 <S>/files/931-cos-cutover-tooling-card.md
25275 <S>/files/cos-cutover-tooling-build-2026-10-20.md
69874 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
16612 <S>/files/wt/ops/desk/deploy-outage.sh
46839 <S>/files/wt/ops/desk/deploy-step0.sh
156560 <S>/files/wt/ops/desk/desk-launch.sh
28266 <S>/files/wt/tests/ops/test_deploy_outage.py
52152 <S>/files/wt/tests/ops/test_deploy_step0.py
11864 <S>/files/wt/tests/ops/test_desk_launch_bootstrap_only.py
4166 <S>/files/wt/tests/ops/test_hub_agent_retired_1020.py
386 <S>/rulings.md
STAGED 13 files · 471288 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/cos-cutover-tooling-check`; commits 2 = PREFLIGHT's range count.) `stage-copy.sh`, each `COPIED <bytes> <dest>`:
- 4960 `files/cos-bootstrap-decisions-2026-10-20.md`
- 8231 `files/929-deploy-cos-bootstrap-card.md` (the working file; see `## RECORDS`)
- 36631 `files/wt/docs/30 - Design/F20-FINAL-2026-10-11.md`
- 10047 `files/wt/tests/ops/test_desk_launch_launchd.py`
- 3534 `files/wt/tests/ops/test_hub_cos_restart_1019.py`
- 4102 `files/wt/tests/ops/test_hub_deferred_1018.py`
- 76069 `files/wt/tests/ops/test_desk_launch_prechecks.py`
- 12118 `files/wt/src/cobalt/jobs/restarts.py`
- 27232 `files/wt/configs/cobalt/jobs.yaml`
`<S>/HOUSE-INSTRUCTIONS.md` written (24093 bytes): HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
House A Grok started 19:34 EDT (`run_in_background`, timeout 2700000); `cd <WT>` → `git status --short --branch` → `## ops/cos-cutover-tooling`.

## OWN FINDINGS
FINDING O1
ROW: T2
CLAIM: A STEP-D0 resume of a bootstrap-only card is refused only by `[ -d "$WT/$wt" ] || refuse "a resume needs the gate worktree $WT/$wt"` (`ops/desk/desk-launch.sh:2228`), so it is admitted whenever a directory `$WT/none` exists. The row says "a bootstrap-only card has no gate, so `STEP-D0` is refused", and the test `a STEP-D0 resume` (`tests/ops/test_desk_launch_bootstrap_only.py:235`) pins only the case where no such directory exists.
RUN: TEST — `tests/ops/test_desk_launch_bootstrap_only.py`
```python
def test_o1_a_step_d0_resume_of_a_bootstrap_only_card_is_refused_with_a_none_dir(desk):
    """Check O1: a bootstrap-only card has no gate, so STEP-D0 is refused whatever $WT holds."""
    (desk.wt / "none").mkdir()
    done = desk.launch(None, "STEP-D0")
    assert done.returncode == 1, done.stdout
    assert "REFUSED: " in done.stderr, done.stderr
```
EXPECT: `AssertionError` at `done.returncode == 1` (exit 0, a `claude --bg ` line printed).

FINDING O2
ROW: T2
CLAIM: The "no `GATE RESULT:` line naming another label" check reads only column-0 lines (`grep '^GATE RESULT:'`, `ops/desk/desk-launch.sh:2182` and `:2184`), so a bulleted `- GATE RESULT: <other label> · <item> · <result>` line in `## GATE RESULTS` is admitted. The row's clause carries no column-0 limit; only the "at least one" clause does.
RUN: TEST — `tests/ops/test_desk_launch_bootstrap_only.py`
```python
def test_o2_a_bulleted_gate_result_of_another_label_is_refused(desk):
    """Check O2: no GATE RESULT line names another label, bulleted or not."""
    desk.set_card(gates=gate_lines() + ["- GATE RESULT: com.cobalt.other-job · X1 · OK"])
    done = desk.launch()
    assert done.returncode == 1, done.stdout
    assert "REFUSED: deploy: bootstrap-only card: " in done.stderr, done.stderr
```
EXPECT: `AssertionError` at `done.returncode == 1` (exit 0).

The CHECK ASKS X1–X5 are answered by runs under `## RUNS` (each a control or a quoted command), not by findings.

## Findings
- House A, first seat: Grok finished 19:41:01 EDT (`date`; exit 0). `<S>/house-a.md` (955 bytes) holds one block, FINDING 1, and NO `FINDINGS:` line → NO FINDINGS LINE: produced nothing (`## 3`). Kept as `<S>/house-a.grok.partial.md` (first line `PARTIAL — NO FINDINGS LINE`); a partial is not a list. Its stdout: "…The bootstrap resume is not an unconditional refusal. I'll record that, then keep reading." then `[exited with code 0]`.
- House A, second seat: Gemini, the next house UP that has not sat, started 19:41 EDT on its own (gates again: R17 line 35, R19 line 37, R19 commit `5055151d…`); `cd <WT>` → `## ops/cos-cutover-tooling`. Finished 19:49:52 EDT (`date`; exit 0), `FINDINGS: 2`; its printed answer written byte for byte, without `[exited with code 0]`, to `<S>/house-a.md` (Grok's file there was copied to the partial first). House B: none (not needed).
- THE DROP: `grep -n -F "RUN:" <S>/house-a.md` → `4:RUN: TEST …`, `20:RUN: TEST …`; each is followed by a `def test_`: both kept.

| id | house | row | claim | run |
|---|---|---|---|---|
| A1 (Gemini 1) | Gemini | T2 | the other-label check is an unanchored `grep -v -F "GATE RESULT: $blab · "` (`desk-launch.sh:2184`): another label's line whose text holds the card label's prefix is admitted | TEST |
| A2 (Gemini 2) | Gemini | T2 | `.+` in `grep -E '^GATE RESULT: [^ ]+ · .+ · .+'` (`:2180`, `:2182`) matches spaces: a blank item or result is admitted | TEST |

## Dropped
- none dropped by the form rule. (Grok's partial, one block on the same claim as O1, is not a list: `## 3`, NO FINDINGS LINE.)

## RUNS
Every test was added to `tests/ops/test_desk_launch_bootstrap_only.py` exactly as written (no form repair) and run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_bootstrap_only.py::<test>`.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `::test_o1_a_step_d0_resume_of_a_bootstrap_only_card_is_refused_with_a_none_dir` | `1 failed` · `assert 0 == 1` at `:274`; stdout a `claude --bg "CONTINUE: STEP-D0. Read '…/DEPLOY-HUB.md' …` line | HELD |
| O2 | own | `::test_o2_a_bulleted_gate_result_of_another_label_is_refused` | `1 failed` · `assert 0 == 1` at `:282`; the card admitted (a `claude --bg ` line) | HELD |
| A1 | Gemini | `::test_t2_a_gate_result_of_another_label_mentioning_the_card_label_is_refused` | `1 failed` · `assert 0 == 1` at `:291`; admitted | HELD |
| A2 | Gemini | `::test_t2_a_gate_result_with_a_blank_item_or_result_is_refused` | `2 failed` · both cases `assert 0 == 1` at `:306`; admitted | HELD |

Red commit: `8ac871c7 wip(cos-cutover-tooling): check red — O1, O2, A1, A2` (`tests/ops/test_desk_launch_bootstrap_only.py`, 44 insertions).

CHECK ASKS, answered by runs:
- X1 (no record → behaves as on BASE): the builder's named controls sit in `tests/ops` (`test_k2_*`, `test_g1_*`, `test_the_agent_goes_down_by_cobalt_sh_and_up_by_kickstart`, `test_a_label_outside_the_residents_*`, `test_k1_*`, `test_t1_a_record_without_the_agent_line_changes_nothing`, `test_t1_dry_run_with_a_retired_agent_still_reads_the_status`, `test_c_*`). They run in the gate's `tests/ops` pass under `## Suites`. Diff read: each script's new branch is gated by `agent_retired` / `$agent_retired`, and the `elif` at `deploy-outage.sh:448` is BASE's block unchanged.
- X2: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_bootstrap_only.py tests/ops/test_desk_launch_launchd.py tests/ops/test_desk_launch_prechecks.py` after the fix → `233 passed, 15 warnings in 95.79s`. This includes the nine `test_t2_every_other_refusal_still_fires` cases and the control `test_t2_a_normal_card_still_cuts_its_gate`. The diff of `desk-launch.sh` over `4a9b60bd..HEAD` touches only the `bonly` branch, the `[ -n "$bonly" ] ||` guards, the bootstrap-only STEP-D0 refusal and the `add=` guard.
- X3: `grep -rn -F "retired-labels" ops "docs/…/DEPLOY-HUB.md"` → `deploy-outage.sh:5` (comment) and `:93` (the one read), `deploy-step0.sh:77` (`RETIRED=`, read only by `agent_retired()`), `DEPLOY-HUB.md:65` (P8: `grep -c -x -F "com.cobalt.agent" …/retired-labels`, a `Bash(grep *)` string). `ls <WT>/ops/desk/retired-labels` → `No such file or directory`: nothing in this tree writes it.
- X4: with the record, `deploy-outage.sh:96-97` refuses the agent in the set before any call, so the trap (`:337-366`) only walks `$down` ⊆ `$labels` and never names the agent; the final read (`:441-447`) only reads `cobalt.sh status`. Hub: the GATE line (`:93`) takes the agent out of `<restart set>`, so 4.2, 4.6 and STEP-5 (1) never name it; STEP-5 (3) (`:169`) no longer types the kickstart; THE ONE RESUME (e) (`:53`) reads OFFLINE as healthy. No path found.
- X5: the admitted line (O1's printed output above) carries `"Bash(git -C /Users/cobalt/cobalt merge --ff-only none)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/none merge --no-edit main)"`, `"Bash(git -C /Users/cobalt/cobalt-wt/none merge --abort)"`, `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/none/.env)"`, `"Bash(rm /Users/cobalt/cobalt-wt/none/.env)"`, an empty `<tip merges>` (two spaces), and the label's `bootout` / `bootstrap`. Every other string is the normal deploy line's. They stand under R60 (ASK DESK 4, the builder's DECISION 3).

## FIXES
- O1, O2, A1, A2: `f15d7af5 fix(cos-cutover-tooling): bootstrap-only form reads every GATE RESULT line and refuses STEP-D0 (check O1, O2, A1, A2)`, `ops/desk/desk-launch.sh` (+15 −4), inside T2's file.
  - The two `grep '^GATE RESULT:'` checks are replaced by one `awk` pass over every `GATE RESULT:` line, bulleted or not. It splits each line on ` · ` and needs the label to equal `$blab` exactly and the item and result to be non-blank; otherwise `REFUSED: deploy: bootstrap-only card: a GATE RESULT line …`.
  - On a resume, a bootstrap-only card is refused with `deploy: bootstrap-only card: a resume needs the gate worktree, and this card has none; STEP-D0 is refused`. The phrase pinned by the existing `a STEP-D0 resume` case is kept.
  - After: `tests/ops/test_desk_launch_bootstrap_only.py tests/ops/test_desk_launch_launchd.py tests/ops/test_desk_launch_prechecks.py` → `233 passed` (`0 failed`). DEPLOY PROOF `grep -c -F "card 931 T2" ops/desk/desk-launch.sh` → `1` (unchanged).
  - DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers an `ops/desk/` script (the build report's Grep, `## RECORDS`); none written.

## Suites
On `<tip now>` = `f15d7af5`. RESTARTS first: `uv run cobalt jobs restarts 4a9b60bd..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/cos-cutover-tooling-build-2026-10-20.md	A	DOCS	-
docs/40 - DevDocs/reports/cos-cutover-tooling-build-2026-10-20.result	A	DOCS	-
ops/desk/deploy-outage.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_outage.py	M	test/documentation; no resident	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_bootstrap_only.py	A	test/documentation; no resident	-
tests/ops/test_hub_agent_retired_1020.py	A	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 4a9b60bd` → the 8 range paths plus the two build-report files; every path is under `ops/`, `tests/ops/` or `docs/`. **cobalt_dev: not taken (DB: none — 10 paths)**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-cutover-tooling offline --deploy-gate` (background) → exit 0:
  ```
  tests/ops: run (deploy gate)
  offline 9023/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/cos-cutover-tooling-offline-20261020-195252.log
  ```
  In the log: `956:4897 passed, 878 skipped, 4 xfailed, 36 warnings in 751.10s (0:12:31)` and `1031:4126 passed, 1 xfailed, 16 warnings in 905.96s (0:15:05)` (tests/ops: the build's 4121 plus the five check cases); `grep -c -F " failed"` → `0`. That `tests/ops` pass is the (a0) `tests/ops` run; it was not typed a second time.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh cos-cutover-tooling livenote` (background) → exit 0:
  ```
  live-note 148/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/cos-cutover-tooling-livenote-20261020-202057.log
  ```
  `grep -n -F "SKIPPED"` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).
- with-DB: not run (DB: none). `.env`: never present; `ls <WT>/.env` → `No such file or directory` (20:21 EDT).
- Every held test passes (`233 passed`, `## FIXES`), and each was shown red first (`## RUNS`).

## Scope
PREFLIGHT's path union (8 paths: `DEPLOY-HUB.md`, `deploy-outage.sh`, `deploy-step0.sh`, `desk-launch.sh` and their four test files) plus my two commits: `tests/ops/test_desk_launch_bootstrap_only.py` (T2's test file) and `ops/desk/desk-launch.sh` (T2's file). Every path is in a row's `files`. `DEPLOY-HUB.md`'s hunks sit at `:53`, `:65`, `:93`, `:123`, `:150`, `:155`, `:160`, `:169` only (the diff), and `:11` is unchanged.

## Checked against the branch
- (i) `git log --oneline 96728174..HEAD -- . ":(exclude)docs"` → `f15d7af5 fix(cos-cutover-tooling): … (check O1, O2, A1, A2)`, `8ac871c7 wip(cos-cutover-tooling): check red — O1, O2, A1, A2`. `<tip now>` = `f15d7af5`.
- (ii) `git log --stat --format=%h 96728174..HEAD` → `f15d7af5` `ops/desk/desk-launch.sh`; `8ac871c7` `tests/ops/test_desk_launch_bootstrap_only.py`; `65ad949c` the build report and its `.result` (docs). No WIDENED path.
- (iii) `git log --oneline 4a9b60bd..HEAD -- ops/desk/deploy-step-c.sh ops/desk/deploy-card.sh ops/desk/authorize.sh "docs/40 - DevDocs/prompts/CARD.md" src configs` → empty.
- (iv) `grep -n -F "def <name>"` → O1 `:270`, O2 `:278`, A1 `:286`, A2 `:303`, one line each. Their red commit `8ac871c7` sits below `f15d7af5` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/cos-cutover-tooling`.
- (vi) `git log --stat --format=%h 4a9b60bd..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not needed.
- (vii) Card RECORDS: `git -C /Users/cobalt/cobalt diff --stat main -- ops/desk "…/DEPLOY-HUB.md" "…/CARD.md" "…/F20-FINAL-2026-10-11.md" tests/ops` → nothing. `ls -la /Users/cobalt/.claude/ops/` → `desk-launch.sh`, `deploy-step0.sh` and `deploy-outage.sh` are links into `/Users/cobalt/cobalt/ops/desk/` (as recorded). `grep -n -F "deploy-outage.sh"` and `grep -n -F "deploy-step0.sh"` of the hub → one line each, `:65`: P8's new prose naming the record the two scripts read, not a call (the hub still types P8, STEP-4, STEP-5 itself).
- (viii) L32: this report holds constructed test values and repo paths only.

## OPEN
none.

## CONTINUE
next: none (closed)

## DECISIONS
none.

## RECORDS
- Check started 19:31 EDT (preflight `date`), closed 20:21:42 EDT (`date`).
- House A, first seat, Grok (grok-4.7): NO FINDINGS LINE. Its `house-a.md` held one block and no `FINDINGS:` line, kept as `<S>/house-a.grok.partial.md`. Its claim is the same as O1, which held by my run. Gemini (gemini-4-argon-high) then sat in house A: `FINDINGS: 2`.
- House B: none. PREFLIGHT found Gemini UP, but the card's `HOUSE B: as needed` (ops, tests, docs) needs none. The stop-line field reads `none available` because the format offers no `not needed` value.
- REFUSED, not needed: `git -C /Users/cobalt/cobalt show "main:docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md"` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." I read the working file with the Read tool instead (it is the copy staged for the houses).
- The L74 line: `## L74`.
- No lock taken (DB: none); `.env` never present.
- files opened: 16 — `CHECK-HUB.md`, the card, the saved diff output, `ops/desk/deploy-outage.sh`, card 929, the probe output, the build report, `tests/ops/test_desk_launch_bootstrap_only.py`, `tests/ops/test_hub_agent_retired_1020.py`, `DEPLOY-HUB.md`, `ops/desk/desk-launch.sh`, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), Grok's output, Grok's `house-a.md`, Gemini's output.
- Context at close: `context 236240 of 400000 — ok` (`desk-context.sh 453b2c9b`).
- Check of `cos-cutover-tooling`: house A `Gemini` (after Grok produced no list), house B `none`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- REFUSED, not needed: `git -C /Users/cobalt/cobalt show "main:docs/40 - DevDocs/prompts/2026-10-20/929-deploy-cos-bootstrap-card.md"` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Read the working file with the Read tool instead.

CHECK DONE · job: cos-cutover-tooling · pass: 1 · tip: f15d7af5 · house A: Gemini FINDINGS: 2 · findings: 4 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9023/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 236240
