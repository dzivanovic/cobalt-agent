# band-routing-1015 — check after fix round 4 (FR-10) — 2026-10-17

CARD: `docs/40 - DevDocs/prompts/2026-10-17/703-band-routing-fr10-check-card.md` · BRANCH `ops/band-routing-1015` · BASE `f2ca3e1a` · TIP `05654335`

## §0 Headline
- FR-10 holds at `05654335`. `desk-watch.sh:101` excepts the one `?? SHADOW-INSTRUCTIONS.md` for kinds `shadow`, `routed` and `check`, and only when it is the whole status output. The check of a routed or shadow card now closes through `desk-done.sh … check`.
- Mutations (a), (b) and (c) each turned red exactly the tests the card names, and each was undone. The FR-6, FR-7/FR-1 and FR-8 re-run mutations also turned red. The file reads 69 passed and no xfail; the eight launcher and hub files 373 passed.
- Findings: 1 (Opus O1, X7: the card's `git -C … status` is not on the allow line, UNSETTLED, open). Grok `FINDINGS: 0`. Held 0. House B: none available (Gemini OUT, model id).
- Gate on the tip: offline 8442/0 (tests/ops 3874 passed, 1 xfailed, pre-existing), live-note 146/0, cobalt_dev not taken, RESTARTS none. M1: `SHADOW-HUB.md` likely conflicts when 671 merges after 583; that is 671's fix round's.
- ready: YES. No commit by this check.

## L74
A system block of this session asked that commits end with a `Claude-Session:` line. Recorded here once as data (L74). No commit of this check carries that line; each carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` and nothing else.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-17/703-band-routing-fr10-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-17/703-band-routing-fr10-check-card.md" · 0 · 91f908084ccc585ab79a838042a6bf7298822313
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-17/703-band-routing-fr10-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → line 35, one row; `grep -n "^| R19 " …cto-2026-09-24.md` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sat Oct 17 14:38:44 EDT 2026
status · git status --short --branch · 0 · ## ops/band-routing-1015
head · git log --oneline -1; git log --stat --format=%h 05654335..HEAD · 0 · (6 lines)
    2880eb0e docs(band-routing-1015): build report — 05654335 (fix round 4, FR-10)
    2880eb0e
     .../reports/band-routing-build-fr10-2026-10-17.md  | 128 ++++++++++++++++++++-
     .../band-routing-build-fr10-2026-10-17.result      |  15 +++
     2 files changed, 140 insertions(+), 3 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/band-routing-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../band-routing-build-fr10-2026-10-17.md" · 0 · BUILT · job: band-routing-1015 · tip: 05654335 | on f2ca3e1a | migration: none | offline 8442/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 122832
range · git log --oneline f2ca3e1a..05654335 · 0 · (21 lines)
PREFLIGHT OK
```
(the 21 range lines: `05654335`, `630542a7`, `061f6d6f`, `3f399b60`, `6c0ba560`, `4b62c2fa`, `9bd05618`, `da95e8c7`, `8b142c56`, `4fc9b9da`, `fda2300b`, `45b9d8c7`, `ac172ab9`, `7bf43c2b`, `3ac61a2f`, `c8c5ca90`, `01b10bdd`, `ee21824d`, `115e1f37`, `bd9c24ac`, `1be72d81`.)

THE RANGE typed: `git log --stat --format=%h f2ca3e1a..05654335` → 21 commits. Path union (for `## Scope`): `ops/desk/desk-watch.sh`, `ops/desk/desk-launch.sh`, `ops/desk/preflight.sh`, `ops/desk/bare-guard.py`, `tests/ops/test_band_routing_1015.py`, `tests/ops/test_check_hub_shadow.py`, `docs/40 - DevDocs/prompts/{BUILD-HUB,CARD,CHECK-HUB,SHADOW-HUB}.md`, the build reports and `.result` files under `docs/40 - DevDocs/reports/`.

DB: none: `git diff --name-only --no-renames f2ca3e1a..05654335` → 19 paths, every one under `ops/`, `tests/ops/` or `docs/`:
```
docs/40 - DevDocs/prompts/BUILD-HUB.md
docs/40 - DevDocs/prompts/CARD.md
docs/40 - DevDocs/prompts/CHECK-HUB.md
docs/40 - DevDocs/prompts/SHADOW-HUB.md
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md
docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result
docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md
docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.result
docs/40 - DevDocs/reports/band-routing-build-fr10-2026-10-17.md
docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md
docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.result
docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.md
docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.result
ops/desk/bare-guard.py
ops/desk/desk-launch.sh
ops/desk/desk-watch.sh
ops/desk/preflight.sh
tests/ops/test_band_routing_1015.py
tests/ops/test_check_hub_shadow.py
```
`ls <S>` → present: `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md STAGED-CARD`. `STAGED-CARD` reads `692-band-routing-fr3-check-card.md`: this folder is the previous check's (card 692, same JOB name), not this session's work. This launch carries no `CONTINUE:`, so it is a fresh check and not RECOVERY. The folder is staged again for card 703 (`## 1`).

House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (run_in_background) · exit 0:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
No `HOUSE A: OpenAI` header, so Sol is not probed. Seats: `house A: grok · house B: none (not needed)`. The card reads `HOUSE B: as needed`, so the MANDATORY rule does not apply. Gemini's OUT is a HARNESS line: the CLI rejects the model id, the case X6 describes (card 670 pending). It is a harness record, not a finding.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0. Its first line: `cleared: <S> (prior check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/band-routing-check-fr3-2026-10-17.md)`. Per-file lines (bytes, dest under `<S>`):
```
36 STAGED-CARD
75068 diff.md
24603 files/703-band-routing-fr10-check-card.md
17895 files/band-routing-build-fr10-2026-10-17.md
34998 files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md
20258 files/wt/docs/40 - DevDocs/prompts/CARD.md
43727 files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md
17407 files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
25728 files/wt/docs/40 - DevDocs/reports/band-routing-build-2026-10-15.md
220 files/wt/docs/40 - DevDocs/reports/band-routing-build-2026-10-15.result
20584 files/wt/docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.md
220 files/wt/docs/40 - DevDocs/reports/band-routing-build-fr1-2026-10-16.result
880 files/wt/docs/40 - DevDocs/reports/band-routing-build-fr10-2026-10-17.md
24427 files/wt/docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.md
220 files/wt/docs/40 - DevDocs/reports/band-routing-build-fr6-2026-10-16.result
17413 files/wt/docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.md
220 files/wt/docs/40 - DevDocs/reports/band-routing-build-fr9-2026-10-17.result
56410 files/wt/ops/desk/bare-guard.py
136683 files/wt/ops/desk/desk-launch.sh
12483 files/wt/ops/desk/desk-watch.sh
11676 files/wt/ops/desk/preflight.sh
42268 files/wt/tests/ops/test_band_routing_1015.py
4899 files/wt/tests/ops/test_check_hub_shadow.py
363 rulings.md
STAGED 24 files · 588686 bytes · commits 14
```
`commits 14` against PREFLIGHT's 21: the diff is `-- . ":(exclude)docs"`, and the 7 range commits that touch only `docs/` (`061f6d6f`, `6c0ba560`, `da95e8c7`, `4fc9b9da`, `ac172ab9`, `3ac61a2f`, `115e1f37`, per the `--stat` above) carry no hunk in it. 21 − 7 = 14, so the diff is complete for its pathspec. The previous check accepted the same shape.
`stage-copy.sh`, one call each:
```
COPIED 98461 <S>/files/583-band-routing-card.md
COPIED 36200 <S>/files/band-routing-check-fr3-2026-10-17.md
COPIED 28466 <S>/files/671-gemini-builder-row-card.md
COPIED 8725 <S>/files/670-gemini-probe-id-card.md
COPIED 7293 <S>/files/wt/ops/desk/desk-done.sh
```
`<S>/HOUSE-INSTRUCTIONS.md` (Write, 25198 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS`, and the Files paragraph.
House A `grok` started 14:41 EDT (`date` 14:41:05; gates R17 line 35 and R19 line 37 re-grepped; `cd <AGY>`, the GROK line, `cd <WT>`, `git status --short --branch` → `## ops/band-routing-1015`). No house B.

## OWN FINDINGS
Written at 14:43 EDT (`date`) before any house list was opened. Read: `git diff 3f399b60 05654335 -- ops/desk/desk-watch.sh tests/ops/test_band_routing_1015.py`; `desk-watch.sh` whole at the tip (worktree head `2880eb0e` = tip in code); `preflight.sh:150-174`; `desk-launch.sh:1780-1829`; `test_band_routing_1015.py:480-739`; `test_close_automation_1015.py:125-154`; the build report whole; the fr3 check `## OWN FINDINGS` through `## RECORDS`; cobalt.md from `## What Cobalt is`; BUILD-HUB `## W` (grep). Greps: `SHADOW-INSTRUCTIONS` over `ops/desk/{desk-launch,desk-watch,preflight,desk-done,wait-stop-line}.sh`; `devfix` over `desk-launch.sh`; `tree not clean` over `tests/ops`; `SHADOW-INSTRUCTIONS` count over `tests/ops`; `status|clean|kind` and `worktree|git ` over `desk-done.sh`; `status|SHADOW` over `wait-stop-line.sh`; `SHADOW-INSTRUCTIONS` over the worktree CHECK-HUB.

What the read shows (to be proved by the runs in `## RUNS`):
- The hunk is one line out and one in. `desk-watch.sh:101` reads `case "$kind" in shadow|routed|check) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt="" ;; esac`. It is a whole-output string equality inside `unclean()`, and `unclean()` is called only as `why=$(unclean)` (`:129`, `:138`, in `close_worker`, skipped for `prodwrite` and `close` at `:126`). So `dirt` lives in a subshell. A second line of any kind keeps "tree not clean". `:103-110` (report committed, session busy) are unchanged.
- Kinds that reach the tree test: `build`, `check`, `devfix` (`:72`), `shadow` (`:73`) and `routed` (`:74`). `deploy` sets no `wt` (`:75`, `wt=-`), so it never reads the tree. The file is excepted for `shadow`, `routed` and `check`, and stays dirt for `build` and `devfix`. Both are right: a routed build is watched as `routed` (FR-6), a HIGH or plain build has no such file, and a devfix is a fresh worktree on its own card (`desk-launch.sh:63`, `:1882`).
- The three places now agree for the check. `desk-launch.sh:1817` excepts the file for the check of a shadow card or a routed tree (`:1784-1796`). `preflight.sh:159` excepts it for a shadow or routed card. CHECK-HUB `:64`/`:117` (worktree) name the shadow card and the routed card. `desk-watch.sh:101` now excepts it for kind `check` with no card read.
- CONSEQUENCE: the watcher closes a plain card's check whose tree holds only the file. That tree cannot pass the launcher: `:1817` refuses a plain card's check with the file present ("is not clean (the check session commits there)"). So the case needs the file to appear during the check. No hub sentence, test or script promises a KEPT for it. `tree not clean` in `tests/ops` appears only at `test_close_automation_1015.py:144` (kind `build`, `stray.txt`) and `test_band_routing_1015.py:681`, `:700`, `:729` (build, routed, and the new check control, each with a second line or kind build).
- X3: `desk-done.sh` holds no `git` or `worktree` call and no tree test, and `wait-stop-line.sh` reads no status. Nothing past `unclean()` would keep or hang the check close on the file.
- The FR-10 control (`:720`) tests its named case. RWatch's default card is `BAND: LOW` with the `CHECK REPORT` line added; the last line is `CHECK DONE · job: x · pass: 1`; the tree holds the file and `notes.txt`; kind `check`; the row is `x-job-check`.
- Not a finding (low value; recorded under X2): no test pins `devfix` reading the file as dirt. A mutation `shadow|routed|check|devfix)` would stay green. A devfix tree never holds the file, so the pin would guard a case that cannot arise.

The read found no defect. One finding came after it, at the S0 run, before any house list was opened. The card's X7 asks that a refusal be quoted as a finding:

FINDING O1
ROW: S0 (X7)
CLAIM: Row S0 names `git -C /Users/cobalt/cobalt-wt/band-routing-1015 status --short --branch`, and the launch line refuses it. The list carries `Bash(git status*)` and `Bash(git -C * diff*)` but no `git -C * status`.
RUN: COMMAND `git -C /Users/cobalt/cobalt-wt/band-routing-1015 status --short --branch`
EXPECT: `Permission to use Bash has been denied because Claude Code is running in don't ask mode.`

## Findings
House A Grok finished at 14:49 EDT (`date` 14:49:13; background exit 0). `ls -la <S>` → `house-a.md` 12 bytes. `<S>/house-a.md`, whole: `FINDINGS: 0`. Grok's stdout ended with the path and the line "The close-step change matches the row: one `case` arm, exact one-line status, and the new control pins a second untracked file. No defect to hand over." House B: none (not needed; `HOUSE B: as needed`).
No house finding to keep.

## Dropped
none (Grok wrote no `FINDING` block)

## RUNS
### The findings
- O1 · opus · `git -C /Users/cobalt/cobalt-wt/band-routing-1015 status --short --branch` → `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` · Verdict: **UNSETTLED — the command is not on the list** (the launch line has `Bash(git status*)`, not `git -C * status`). The fact it was after is proved by the listed `git status --short --branch` from `<WT>` → `## ops/band-routing-1015`. Nothing in the branch is wrong; the card's wording is. It stays OPEN.

### The card's rows
- S0 · `git diff --name-only --no-renames 3f399b60 05654335` → `docs/40 - DevDocs/reports/band-routing-build-fr10-2026-10-17.md`, `ops/desk/desk-watch.sh`, `tests/ops/test_band_routing_1015.py` (exactly the three). `git diff --stat 05654335 2880eb0e -- . ":(exclude)docs"` → nothing. `git diff --stat 3f399b60 05654335` → report `35 +`, `desk-watch.sh | 2 +-`, `test_band_routing_1015.py | 18 ++++++++++-` (53+, 2-). `git diff --name-only --no-renames f2ca3e1a..05654335` → the 19 paths under PREFLIGHT, the same 19 as the build report's (a0). It holds no `src/`, `configs/` or `.claude/` path and no `desk-done.sh`. `git diff 3f399b60 05654335 -- ops/desk/desk-watch.sh` → one hunk `@@ -98,7 +98,7 @@ unclean()`: `-    case "$kind" in shadow|routed) …` / `+    case "$kind" in shadow|routed|check) …`. FR-6's arms `:65`/`:74`, the mapping `:156` and FR-9's comment `:100` are context only. The test diff: `@@ -701,7 +701,6 @@` removes only the `@pytest.mark.xfail(strict=True, reason="check fr3 O1: …")` line, and `@@ -714,6 +713,23 @@` adds the FR-10 comment block and `test_fr10_control_…`. No other body changed. Status: see O1 (the `git -C` form is refused); `git status --short --branch` → `## ops/band-routing-1015`.
- FR-10 · `git show 05654335:ops/desk/desk-watch.sh` and the worktree copy agree (status clean, code identical): `:72` `build|check|devfix) … wt=$(header WORKTREE) …`, `:97` `unclean() {`, `:99` `dirt=$(git -C … status --short 2>&1)`, `:100` the FR-9 comment, `:101` `case "$kind" in shadow|routed|check) [ "$dirt" != "?? SHADOW-INSTRUCTIONS.md" ] || dirt="" ;; esac`, `:102` `[ -z "$dirt" ] || { echo "tree not clean"; return; }`, `:103-110` unchanged. Callers: `close_worker` `:129` and `:138`, `why=$(unclean)` (a subshell); `:126` skips `prodwrite` and `close`. The three places now match for the check: `desk-launch.sh:1817` (shadow or `routed_tree`, `:1793-1796`), `preflight.sh:159` (shadow or routed), `desk-watch.sh:101` (kind `check`, card unread). The watcher's rule is wider than the launcher's: every check, not only a routed or shadow card's. The launcher refuses a plain card's check with the file present (`:1818`), so the extra width needs the file to appear during a check. Kinds that still read the file as dirt: `build` and `devfix` (`:72`, through `close_worker` `:129`/`:138`). `deploy` never reads the tree (`:75`, `wt=-`). Both are right, as in `## OWN FINDINGS`. `tree not clean` in `tests/ops` (Grep): `test_close_automation_1015.py:144` (build, `stray.txt`), `test_band_routing_1015.py:681` (build), `:700` (routed, second line), `:729` (check, second line). None pins the old KEPT for a check holding only the file. `SHADOW-INSTRUCTIONS` in `ops/desk/*.sh` (Grep): `desk-launch.sh:199`, `:1815`, `:1817`; `desk-watch.sh:100`, `:101`; `preflight.sh:119`, `:158`, `:159`, `:167`, `:169`. CHECK-HUB `:64`/`:117` (worktree) name the shadow card and the routed card. None promises a KEPT for a check. `xfail|runxfail` in the test file (Grep) → no hit.
  GREEN: `uv run pytest -q -rA -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py -k "check_o1 or check_fr3 or fr9 or fr10"` → `8 passed, 61 deselected, 15 warnings in 9.72s`: `PASSED …::test_check_o1_a_routed_closeout_on_a_gate_seat_tree_hands_build_to_desk_done`, `…::test_fr9_a_shadow_card_tree_holding_only_the_instructions_file_closes`, `…::test_fr9_control_a_build_kind_tree_holding_that_file_is_still_kept`, `…::test_fr9_control_a_routed_tree_with_any_other_untracked_line_is_still_kept[untracked]`, `…[modified]`, `…::test_check_fr3_o1_a_routed_or_shadow_cards_check_closes_on_the_instructions_file[routed]`, `…[shadow]`, `…::test_fr10_control_a_check_kind_tree_with_a_second_untracked_file_is_still_kept`. The FR-10 control tests its named case (`## OWN FINDINGS`).
  MUTATIONS (Edit, `-k "check_o1 or check_fr3 or fr9 or fr10"`, `--tb=line`):
  (a) `:101` back to `shadow|routed)`. While mutated, `git diff 630542a7 -- ops/desk/desk-watch.sh` → nothing (the red commit's text). Result: `2 failed, 6 passed`. `[routed]` and `[shadow]` `:713`: `AssertionError: CHECK DONE · job: x · pass: 1` / `KEPT sess-x01: tree not clean` / `assert [] == ['sess-x01 /p...ild.md check']`, so the stub was never called. (No `--runxfail`: the marker is gone.)
  (b) `case "$kind" in *)` → `1 failed, 7 passed`: `test_fr9_control_a_build_kind_…` `:681` `assert 'CLOSED sess-x01' == 'KEPT sess-x0...ree not clean'`.
  (c) the equality as a glob inside the kind gate (`case "$kind" in shadow|routed|check) case "$dirt" in *SHADOW-INSTRUCTIONS.md*) dirt="" ;; esac ;; esac`) → `3 failed, 5 passed`: `[untracked]` and `[modified]` `:700` and `test_fr10_control_…` `:729`, each `assert 'CLOSED sess-x01' == 'KEPT sess-x0...ree not clean'`. A first form dropped the kind gate too (`case "$dirt" in *SHADOW-INSTRUCTIONS.md*) dirt="" ;; esac` alone) and gave `4 failed`: the same three plus the build control `:681`.
  Undo: `:101` restored by Edit; `git diff --stat 05654335 -- ops/desk/desk-watch.sh` → nothing; the GREEN run above came after it. Hand run: not needed. `test_fr10_control_…` is exactly the check tree with `?? SHADOW-INSTRUCTIONS.md` plus `?? notes.txt`, and it is KEPT. The controls were green before and after.
- D1 · build report `:144-145` `## DECISIONS` / `none`; stop line `:157` `… decisions: 0 · for Dejan: 0 · tokens: 122832`. Both confirmed. `## §0 Headline` `:9` `FIXED: O1 — tests/ops/test_band_routing_1015.py::test_check_fr3_o1_a_routed_or_shadow_cards_check_closes_on_the_instructions_file`. That is the fr3 check's one `## OPEN` item (O1, `:220`) and the test this check ran (both cases PASSED; red under (a)). The one-word widening is the smallest form. It is wider than the fr3 check's suggested form (derive shadow or routed from the card), and the card states that as its CONSEQUENCE, so it is kept. The `:100` comment and the header `:16-23` and usage lines `:2`, `:49` not naming `check` are a record by the fence. No test or hub reads that comment (`tree not clean` and `SHADOW-INSTRUCTIONS` greps above).
- M1 · merge bases: 671 `git merge-base ops/gemini-builder-row-1017 main` → `7f415a4f37c9fbd4875c5c5e53fe25f8ae367653`; 670 `… ops/gemini-probe-id-1017 main` → `f2140694cc0266eef1f5d042155ebaf956a7f408`. Heads: 671 `8ba22eaf`, 670 `9f281a6a`. Stats on the three files: 583 → `SHADOW-HUB.md | 15`, `bare-guard.py | 5`, `desk-launch.sh | 80` (90+, 10-); 671 → `SHADOW-HUB.md | 12`, `bare-guard.py | 15`, `desk-launch.sh | 4` (22+, 9-); 670 → nothing. 670's whole stat: `CHECK-HUB.md`, `STANDING-LIST.md`, its report and `.result`, `ops/desk/house-probe.sh`, `tests/ops/test_house_probe.py`, so it touches none of the three. Hunk headers (`git diff -U0`; both branches from the same pre-images `1b63a76d`, `0a486be5`, `f3d3f3b4`):
  - `SHADOW-HUB.md`: 583 `@@ -27,0 +28,9 @@` (BAND ROUTING + table), `@@ -44 +53 @@`, `@@ -61 +70 @@`, `@@ -73 +82 @@`. 671 `@@ -12 +12 @@`, `@@ -15 +15 @@`, `@@ -21,0 +22 @@`, `@@ -26,0 +28,3 @@` (Gemini note + X1), `@@ -29 +33 @@` (the `<pass prompt>` line), `@@ -88 +92 @@`. 583's insert after old `:27` sits between 671's insert after `:26` and its change at `:29`, one unchanged line on each side. **A textual conflict is likely.**
  - `bare-guard.py`: 583 `@@ -1276,0 +1277,5 @@` (`g5`); 671 `@@ -1184,2 +1184,2 @@`, `@@ -1201,2 +1200,0 @@`, `@@ -1203,0 +1202,6 @@`, `@@ -1208,0 +1213,3 @@` (`builder_call`). Disjoint by about 68 lines: no conflict.
  - `desk-launch.sh`: 583 `@@ -378,0 +379 @@` (`routed=""`), 671 `@@ -376,0 +377 @@` (a comment). Two unchanged lines lie between them: adjacent, so a conflict is possible. 583 `@@ -390,0 +392,4 @@` (`--routed`) and 671 `@@ -398 +399,2 @@` (the `gemini-*` arm) are 7 lines apart, likely clean. 583's other hunks (`-986`, `-991`, `-1629`, `-1658`, `-1663`, `-1680`, `-1730`, `-1751`, `-2290`) are not touched by 671.
  In deploy order 583, 671, 670, any conflict falls on the second deploy (671 onto a main carrying 583): likely `SHADOW-HUB.md`, possibly `desk-launch.sh:376-379`. That is 671's fix round's to resolve; nothing is resolved here. 670 has no overlap. FR-10 adds no line to the three files (S0). This is read from the hunks: `git merge-tree` is not on the list. The same answer as the fr3 check's M1.
- E1 · one mutation per row the fr3 check named, each undone with Edit, and the undo proved by `git diff --stat 05654335 -- <file>` → nothing:
  FR-6: `desk-watch.sh:156` mapping back to `"$kind"` → `2 failed, 3 passed` (`-k "fr6 or check_o1"`): `test_fr6_a_routed_closeout_…` `:576` and `test_check_o1_…` `:656`, `assert ['sess-x01 /p...ld.md routed'] == ['sess-x01 /p...ild.md build']`.
  FR-7/FR-1: the pass-through `*/./*|*//*) ;;` line removed (`desk-launch.sh:991`) → `2 failed, 7 passed` (`-k "fr7 or o3 or o2 or fr1"`): `test_o2_…` `:382` and `test_fr1_…` `:393`, each `REFUSED: the card must be …/prompts/<YYYY-MM-DD>/<nn>-<job>-card.md: …/prompts/./2026-10-16/…` (and `prompts//2026-10-16/…`) in place of `the card path holds '/./' or '//'`.
  FR-8: SHADOW-HUB `:28`'s clause back to `(R1532: Terra backup; 2026-10-14 item 7: a 429 is retried, never a backup)` → `2 failed, 2 passed` (`-k "fr8 or fr4"`): `test_fr4_…` `:464` and `test_fr8_…` `:634`, `AssertionError: brain 2026-10-16, reading R1532's 'Terra backup'`.
  Reads: `desk-watch.sh:65` `routed) report=$(header REPORT) || exit 1; re='^(BUILT ·|FAILED)' ;;`, `:74` `routed) … session="$job-gate" ;;`, `:156` the mapping; `desk-launch.sh:990-1000` the two card `case`s (`the card must be` at `:992`, `:994`); SHADOW-HUB `:28` ends `… R1471 (7) is recorded in the direction file)):`. `git status --short --branch` after all undos → `## ops/band-routing-1015`.
  Pins: `uv run pytest -q -rA -p no:cacheprovider --color=no tests/ops/test_band_routing_1015.py` → `69 passed, 15 warnings in 23.61s`, no xfailed. The PASSED lines include every `test_b1_…` (2), `test_b2_…` (3), `test_b3_…` (16 cases), `test_b4_…` (2), `test_b5_…` (10 cases), `test_b6_…` (3), and the controls `test_b1_control_…`, `test_b2_control_…`, `test_b3_control_…` (3), `test_b4_control_…`, `test_b5_control_…` (6 cases), `test_b6_control_…` (2), `test_fr1_control_…`, `test_fr2_control_…`, `test_fr3_control_…` (2 cases), `test_fr4_control_…`, `test_fr5_control_…`, `test_fr6_control_…` (2), `test_fr7_control_…`, `test_fr8_control_…`, `test_fr9_control_…` (3 cases), `test_fr10_control_…`. `git diff --stat 3f399b60 05654335 -- <the eight files>` → nothing. `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/ops/test_band_routing_1015.py` → no output (exit 1). The eight files: see `## Suites`.
- R3 · `uv run cobalt jobs restarts 3f399b60..05654335` → `band-routing-build-fr10-2026-10-17.md A DOCS -` · `ops/desk/desk-watch.sh M operator script; no Cobalt reader -` · `tests/ops/test_band_routing_1015.py M test/documentation; no resident -` · `RESTARTS: none`. `… f2ca3e1a..05654335` → 19 rows: the 13 `docs/` paths `DOCS`; `bare-guard.py`, `desk-launch.sh`, `desk-watch.sh`, `preflight.sh` `operator script; no Cobalt reader`; `test_band_routing_1015.py` (A) and `test_check_hub_shadow.py` (M) `test/documentation; no resident`; `RESTARTS: none`. The header's `none` holds.
- G1 · see `## Suites`.
- X4 · FR-10 changes no hub: `git diff --name-only 3f399b60 05654335` holds no `docs/40 - DevDocs/prompts/` path. X6: Grok ran from the staged copies, wrote `FINDINGS: 0`, and made no keyed call this check can see. House B: N/A (Gemini OUT on the CLI's model id), a harness record.

## FIXES
none (no finding HELD). No `fix(band-routing-1015):` and no `wip(band-routing-1015): check red` commit; no DevDocs line (no module changed).

## Suites
On the tip `05654335`. No commit by this check; the worktree head `2880eb0e` adds only docs. DB: none, so W is (a0), (a) and (e).
- RESTARTS: `uv run cobalt jobs restarts f2ca3e1a..05654335` → 19 rows, `RESTARTS: none` (`## RUNS` R3).
- (a0) `git diff --name-only --no-renames f2ca3e1a..05654335` → 19 paths, each under `ops/`, `tests/ops/` or `docs/` (PREFLIGHT). **`cobalt_dev: not taken (DB: none — 19 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 offline --deploy-gate` (background, exit 0), whole:
```
tests/ops: run (deploy gate)
offline 8442/0
log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-offline-20261017-144921.log
```
  In the log: `:888` `4568 passed, 806 skipped, 1 xfailed, 36 warnings in 663.20s (0:11:03)`; `:959` (tests/ops whole) `3874 passed, 1 xfailed, 16 warnings in 844.78s (0:14:04)`, the build's own count. The 1 xfail is the pre-existing one, not this file's (the file has no xfail).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh band-routing-1015 livenote` (background, exit 0), whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/band-routing-1015-livenote-20261017-151445.log`. Log `:56` `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`); `:57` `146 passed, 1 skipped, 15 warnings in 25.38s`.
- The eight launcher and hub files (E1): `uv run pytest -q tests/ops/test_shadow_hub_file.py tests/ops/test_desk_launch_shadow.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_watch.py tests/ops/test_close_automation_1015.py tests/ops/test_check_hub_shadow.py tests/ops/test_card_template_1014.py tests/ops/test_preflight.py` → `373 passed, 16 warnings in 178.40s (0:02:58)`.
- with-DB: not run (DB: none). cobalt_dev: not taken. `.env`: `ls /Users/cobalt/cobalt-wt/band-routing-1015/.env` → `No such file or directory` (never created).

## Scope
PREFLIGHT's path union: 19 paths, all under `ops/`, `tests/ops/` or `docs/`. This check made no commit. Every mutation was undone: `git diff --stat 05654335 -- <file>` → nothing for `desk-watch.sh`, `desk-launch.sh` and `SHADOW-HUB.md`, and `git status --short --branch` → `## ops/band-routing-1015`.

## Checked against the branch
(i) `git log --oneline 05654335..HEAD -- . ":(exclude)docs"` → nothing; tip now `05654335`. (ii) `git log --stat --format=%h 05654335..HEAD` → `2880eb0e`, the two report files under `docs/` only. (iii) `git log --oneline f2ca3e1a..HEAD -- ops/desk/desk-done.sh .claude/settings.json .claude/settings.json.bak src configs LAWS.md` → nothing. `git log --oneline 3f399b60..HEAD -- ops/desk/desk-launch.sh ops/desk/preflight.sh ops/desk/bare-guard.py ops/desk/desk-done.sh "docs/40 - DevDocs/prompts"` → nothing. (iv) No HELD finding. (v) `ls …/.env` → No such file; `git status --short --branch` → `## ops/band-routing-1015`. (vi) `git log --stat --format=%h f2ca3e1a..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no gate-list change needed. (vii) Card RECORDS: `git log --oneline ops/band-routing-1015 -5` → `2880eb0e`, `05654335`, `630542a7`, `061f6d6f`, `3f399b60`, as recorded. `git diff --name-only 05654335 2880eb0e` → the fr10 report and its `.result`, as recorded. Merge bases `7f415a4f…`, `f2140694…` and the three-file stats match (M1). The tip anchors `:72`, `:97`, `:100`, `:101`, `:113`, `preflight.sh:159`, `desk-launch.sh:1817`, and test `:494`, `:496`, `:497`, `:500`, `:649`, `:663`, `:673`, `:686`, `:705`, `:720` all match (Read). (viii) L32: this report holds constructed test values and repo ids only.
COUNT: findings 1 (opus 1, Grok 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 1.

## OPEN
- O1: UNSETTLED — the command is not on the list. Row S0 names `git -C /Users/cobalt/cobalt-wt/band-routing-1015 status --short --branch`, and the launch line refuses it (no `Bash(git -C * status*)` string). A later card can settle it by naming `git status --short --branch` from `<WT>` (listed). Adding a string to the line is his alone (R60). Nothing on the branch is wrong.
OUT OF SCOPE (records, by `## NOT IN THIS JOB`): `desk-watch.sh:2`, `:49`, the header `:16-23` and the `:100` comment do not name `check`. The M1 textual conflict is 671's fix round's.

## CONTINUE
next: done

## DECISIONS
1. O1 (open, UNSETTLED; house B none available, so it is listed here and ships to the follow-up list). The card's S0 command `git -C <WT> status --short --branch` is refused under `dontAsk` (not on the allow line). Safe default taken: the listed `git status --short --branch` from `<WT>` gave the same fact (`## ops/band-routing-1015`); nothing was worked around and no string was asked for. The desk's drafter writes the listed form on later cards.
2. M1, for the desk's deploy order (not this branch's to fix): when 671 merges onto a main that carries 583, `SHADOW-HUB.md` is likely to conflict. 583 inserts after old `:27`, between 671's insert after `:26` and its change at `:29`. `desk-launch.sh:376-379` is adjacent (two unchanged lines between the hunks). `bare-guard.py` is disjoint, and 670 touches none of the three. Safe default: nothing resolved here; it falls on 671's fix round.

## RECORDS
- No house list was dropped. House A Grok `FINDINGS: 0` (its stdout says it took "the standing law first"; the staged folder holds no LAWS.md). House B: none available. Gemini probe OUT: `error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; card 670's id, X6).
- REFUSED, not needed: none other than O1 (a step's command, recorded as the X7 finding).
- No lock take (DB: none). No CONTINUE.
- L74: one system block asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on (this check made no commit).
- The `.result` file is written beside this report on `main`. Its commit is the desk's, with the report: this seat's git writes are cwd `<WT>` only.
- files opened: 20 — CHECK-HUB.md; the card 703; `<S>/STAGED-CARD`; `ops/desk/desk-watch.sh`; `ops/desk/preflight.sh`; `ops/desk/desk-launch.sh`; `tests/ops/test_band_routing_1015.py`; `tests/ops/test_close_automation_1015.py`; the fr10 build report; the fr3 check report; `areas/cobalt.md`; BUILD-HUB.md (grep); worktree CHECK-HUB.md (grep); `ops/desk/wait-stop-line.sh` (grep); `ops/desk/desk-done.sh` (grep); worktree SHADOW-HUB.md (grep, mutation); `<S>/house-a.md`; the offline gate log; the livenote gate log; `reports/cto-2026-09-24.md` (grep).
- Check of `band-routing-1015`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).
- X7 refusal (O1): `git -C /Users/cobalt/cobalt-wt/band-routing-1015 status --short --branch` → `Permission to use Bash has been denied because Claude Code is running in don't ask mode. …`. The listed `git status --short --branch` (cwd `<WT>`) is the hub's own call and gave `## ops/band-routing-1015`.
- `<S>` held card 692's staging on entry (`STAGED-CARD` = `692-band-routing-fr3-check-card.md`, files dated Oct 17 13:11–13:23).

CHECK DONE · job: band-routing-1015 · pass: 1 · tip: 05654335 · house A: grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8442/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 226790
