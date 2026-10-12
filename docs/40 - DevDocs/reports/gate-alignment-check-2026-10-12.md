# gate-alignment-1012 — check report (2026-10-12)

## §0 Headline
Check of `gate-alignment-1012` (card 397), one pass. House A Grok found nothing (`FINDINGS: 0`); no house B was needed.
My read found 2. O1 HELD and is fixed at `1178554e`: a REJECTED verdict quoting ` · ` could not be settled, and now it can, with the same bytes in all three scripts. O2 is REJECTED by row G1 (OPEN, follow-up).
Suites green on `1178554e`: offline 4199/0, live-note 146/0, `tests/ops` 3172 passed. RESTARTS: none. `ready: YES`.

## L74
A system reminder at the session's start asked that commits carry a `Claude-Session:` line. It is data; I acted on none of it. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/397-gate-alignment-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/397-gate-alignment-card.md" · 0 · 1916b5fadca84532fbda6d337df59466549bb56a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/397-gate-alignment-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 38:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row · `grep -n "^| R19 "` → line 37, one row · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 12 08:17:50 EDT 2026
status · git status --short --branch · 0 · ## ops/gate-alignment-1012
head · git log --oneline -1; git log --stat --format=%h f47fb5d7..HEAD · 0 · (5 lines)
    dc68e8ac docs(gate-alignment-1012): build report — f47fb5d7
    dc68e8ac
    
     .../reports/gate-alignment-build-2026-10-12.md     | 196 +++++++++++++++++++++
     1 file changed, 196 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/gate-alignment-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/gate-alignment-1012/docs/40 - DevDocs/reports/gate-alignment-build-2026-10-12.md" · 0 · BUILT · job: gate-alignment-1012 · tip: f47fb5d7 | on b5462afd | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 285193
range · git log --oneline b5462afd..f47fb5d7 · 0 · (3 lines)
    f47fb5d7 fix(gate-alignment-1012): THE RULE names card 397 once, in its header, pinned (G1; L1, L72)
    f3dc5e33 fix(gate-alignment-1012): THE RULE reads a held id from RUNS or FIXES, settles open by desk record, CHECK-HUB says so (G1, G2, H3; L1, L3, L72)
    edcedd7b wip(gate-alignment-1012): red
PREFLIGHT OK
```
- THE RANGE, `git log --stat --format=%h b5462afd..f47fb5d7` · exit 0: f47fb5d7 → `ops/desk/deploy-card.sh` 2 +-, `ops/desk/deploy-step0.sh` 2 +-, `ops/desk/desk-launch.sh` 2 +-, `tests/ops/test_deploy_card.py` +10; f3dc5e33 → `docs/40 - DevDocs/prompts/CHECK-HUB.md` 6 +-, the three scripts 101 each; edcedd7b → `tests/ops/test_check_hub_gate_wording.py` +67, `tests/ops/test_deploy_card.py` 228, `tests/ops/test_deploy_step0.py` +30, `tests/ops/test_desk_launch_prechecks.py` +32. Path union: 8 paths (below).
- DB: none · `git diff --name-only --no-renames b5462afd..f47fb5d7` · exit 0:
```
docs/40 - DevDocs/prompts/CHECK-HUB.md
ops/desk/deploy-card.sh
ops/desk/deploy-step0.sh
ops/desk/desk-launch.sh
tests/ops/test_check_hub_gate_wording.py
tests/ops/test_deploy_card.py
tests/ops/test_deploy_step0.py
tests/ops/test_desk_launch_prechecks.py
```
every path under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0: `grok: UP` · `gemini: UP`.
- Seats: no `HOUSE A:` header line; Grok UP → **house A: Grok · house B: none (not needed)** (`HOUSE B: as needed`).
- PROVEN BY FIRST REAL USE: the write strings at their first use; no with-DB string on a DB: none card.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0, each copy proved against its blob id:
```
56483 <S>/diff.md
17309 <S>/files/397-gate-alignment-card.md
28597 <S>/files/gate-alignment-build-2026-10-12.md
42014 <S>/files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md
30981 <S>/files/wt/ops/desk/deploy-card.sh
39221 <S>/files/wt/ops/desk/deploy-step0.sh
96308 <S>/files/wt/ops/desk/desk-launch.sh
2691 <S>/files/wt/tests/ops/test_check_hub_gate_wording.py
58242 <S>/files/wt/tests/ops/test_deploy_card.py
42781 <S>/files/wt/tests/ops/test_deploy_step0.py
64788 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py
355 <S>/rulings.md
STAGED 12 files · 479770 bytes · commits 3
```
`commits 3` = PREFLIGHT's range count (3). The `## READ` files, each `stage-copy.sh`:
- `COPIED 12073 <S>/files/cto-2026-10-12.md`
- `COPIED 26887 <S>/files/launcher-shadow-check-check-2026-10-11.md`
- `COPIED 29008 <S>/files/launcher-shadow-check-build-2026-10-11.md` (from `/Users/cobalt/cobalt-wt/launcher-shadow-check-1011/…`: the F1 report is not on `main`'s disk, `ls` → `No such file or directory`)
- `COPIED 24661 <S>/files/386-launcher-shadow-check-card.md`
- `tests/ops/test_check_hub_shadow.py` from this worktree → `REFUSED: no such plain file: …` (it is card 386's file, not on this branch); copied from 386's worktree instead → `COPIED 4828 <S>/files/test_check_hub_shadow.py`.
`<S>/HOUSE-INSTRUCTIONS.md` written (18305 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
House A Grok started 08:20 ET (`date` → `Mon Oct 12 08:20:21 EDT 2026`), house gates re-run just before (R17 line 35, R19 line 37); `cd <WT>` then `git status --short --branch` → `## ops/gate-alignment-1012`.

## OWN FINDINGS
Written before either house list was opened (house B: none).

FINDING O1
ROW: G2 (X2)
CLAIM: G2 says a SETTLED id is one "whose verdict carries `REJECTED` or `UNSETTLED`", but `ops/desk/deploy-card.sh:357` takes the verdict as the bullet's LAST ` · ` field, so a REJECTED verdict that quotes a card line holding ` · ` (the stop-line separator) cannot be settled and the fix round is refused.
RUN: TEST — `tests/ops/test_deploy_card.py`
```python
def test_o1_a_rejected_verdict_quoting_a_dot_separator_is_settled(tmp_path):
    desk = Desk(tmp_path)
    runs = (HELD_RUN.format(id="O1") + "\n"
            + "- O2 · own · `uv run pytest -q tests/x.py` · `1 failed` · **REJECTED — row X1 \"a · b\"**\n")
    fixed, head, report = held_round(desk, open="2", runs_text=runs, lines=[FIXED_O1, SETTLED_O2])
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
```
EXPECT: `assert 1 == 0`, stderr `REFUSED: alpha: the fix report … settles O2, which is no REJECTED or UNSETTLED id under ## RUNS of the check …`.

FINDING O2
ROW: G1 (X1)
CLAIM: A RUNS table row the check FIXED carries `**HELD**` in its last cell (CHECK-HUB `:104` writes the verdict `HELD`), and `ops/desk/deploy-card.sh:162-163` still counts it as held unfixed, so a check with one real `## FIXES` held id and one fixed table row is refused at the id count.
RUN: TEST — `tests/ops/test_deploy_card.py`
```python
def test_o2_a_fixed_table_row_marked_held_is_not_counted_held_unfixed(tmp_path):
    desk = Desk(tmp_path)
    rows = (TABLE_HEAD + "| O2 | own | `tests/x.py::test_o2` | `1 failed` | **HELD** |\n"
            + "\n## FIXES\n" + FIXES_HELD.format(id="O1") + "\n- O2: fixed in the check's commit (constructed)\n")
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=rows)
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
```
EXPECT: `assert 1 == 0`, stderr `… lists 2 HELD, NOT FIXED row(s) under ## RUNS and ## FIXES (O2 O1), its last line says 'held unfixed: 1'`.

Read and found no finding: X3 (the block's identity is pinned by `test_h1_…`; the old refusal texts stand in the diff), X4 (hunks at `:104`, `:107`, `:123` only, in the diff), X5 (R1 is quoted in the build report; I re-run it at `## 4` as a fact, not a finding), no path to a score, rank, grade or size (`ops/desk/` and `tests/ops/` only, no `src/`).

## Findings
House A Grok finished at 08:33 ET (`date` → `Mon Oct 12 08:33:55 EDT 2026`, exit 0). It wrote `<S>/house-a.md` itself (12 bytes, `ls -la`), which reads `FINDINGS: 0` and nothing else. Its stdout: `… The rule blocks, the three test files, and the check-report shapes match the rows. No runnable defect./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gate-alignment-1012-check/house-a.md`. House B: none (not needed).
- O1 · own · G2 (X2) · a REJECTED verdict that quotes ` · ` cannot be settled: the verdict is read as the bullet's last ` · ` field · TEST
- O2 · own · G1 (X1) · a fixed RUNS table row marked `**HELD**` still counts as held unfixed · TEST

## Dropped
none. Grok wrote no FINDING block.

## RUNS
- O1 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py::test_o1_a_rejected_verdict_quoting_a_dot_separator_is_settled` · `1 failed` (run with O2: `2 failed, 15 warnings in 1.98s`); first failing line `E       AssertionError: REFUSED: alpha: the fix report …/alpha-fix.md settles O2, which is no REJECTED or UNSETTLED id under ## RUNS of the check …/alpha-check-2026-01-02.md` · **HELD**. Committed red at `c0dcebf5`.
- O2 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py::test_o2_a_fixed_table_row_marked_held_is_not_counted_held_unfixed` · `1 failed`; first failing line `E       AssertionError: REFUSED: alpha: the check …/alpha-check-2026-01-02.md lists 2 HELD, NOT FIXED row(s) under ## RUNS and ## FIXES (O2 O1), its last line says 'held unfixed: 1'` · **REJECTED — row G1 "the held ids are the union of (a) today's two `## RUNS` forms"**: the card keeps the `**HELD**` table-row read (card 361 T1). The test was removed with the Edit tool. OPEN.

No other finding was run: Grok wrote none.

## FIXES
- O1: fixed at `1178554e` (red at `c0dcebf5`). THE RULE's `## RUNS` open-id read, in all three scripts with the same bytes (`deploy-card.sh`, `desk-launch.sh`, `deploy-step0.sh`): a bullet is a REJECTED or UNSETTLED id when ANY ` · ` field after its id starts `REJECTED` or `UNSETTLED` (after leading `*`/blanks are cut). Before, only the last field counted. Table rows are unchanged (last cell). The header comment says so. No refusal text changed. After the fix, `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_deploy_card.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_deploy_step0.py tests/ops/test_check_hub_gate_wording.py` → `333 passed, 15 warnings in 152.08s (0:02:32)`, `test_h1_the_rule_is_one_text_in_the_three_scripts` among them. DevDocs line: `docs/40 - DevDocs/cobalt/` has no page for these scripts (Grep `deploy-card` → no files), and the build added none, so there was no page to date.

## Suites
DB: none card: RESTARTS, then W (a0), (a), (e) and `tests/ops`, on `1178554e`.
- RESTARTS: `uv run cobalt jobs restarts b5462afd..HEAD` → 9 rows: `CHECK-HUB.md` and the build report `DOCS`; the three `ops/desk/` scripts `operator script; no Cobalt reader`; the four `tests/ops/` files `test/documentation; no resident`; each `-`. Last line **`RESTARTS: none`**.
- (a0) `git diff --name-only --no-renames b5462afd` → 9 paths, each under `ops/`, `tests/ops/` or `docs/` → **`cobalt_dev: not taken (DB: none — 9 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gate-alignment-1012 offline` (exit 0) → **`offline 4199/0`**, `log: /Users/cobalt/cobalt-wt/.gate-logs/gate-alignment-1012-offline-20261012-083759.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gate-alignment-1012 livenote` (exit 0) → **`live-note 146/0`**, `log: /Users/cobalt/cobalt-wt/.gate-logs/gate-alignment-1012-livenote-20261012-083800.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (exit 0) → **`3172 passed, 1 xfailed, 15 warnings in 638.90s (0:10:38)`** (the build's 3171 plus O1); `grep -c -F "SKIPPED"` over its output → `0`.
- With-DB: not run (DB: none), `with-DB 0/0`. `.env`: `ls /Users/cobalt/cobalt-wt/gate-alignment-1012/.env` → `No such file or directory` (08:49 ET); no lock was taken.

## Scope
PREFLIGHT's path union (8 paths), each in a row's `files`: the three scripts (G1, G2), `tests/ops/test_deploy_card.py`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_deploy_step0.py` (G1, G2), `CHECK-HUB.md` and `tests/ops/test_check_hub_gate_wording.py` (H3). My commits: `c0dcebf5` (`tests/ops/test_deploy_card.py`) and `1178554e` (the three scripts, THE RULE block and its header comment only), all inside G2's files.

## Checked against the branch
- (i) `git log --oneline f47fb5d7..HEAD -- . ":(exclude)docs"` → `1178554e fix(gate-alignment-1012): a SETTLED id's verdict is any RUNS field after the id, so a verdict quoting a separator settles (check O1)` · `c0dcebf5 wip(gate-alignment-1012): check red — O1`. `<tip now>` = `1178554e`.
- (ii) `git log --stat --format=%h f47fb5d7..HEAD` → `1178554e` the three scripts (9 +++++---- each); `c0dcebf5` `tests/ops/test_deploy_card.py` (+9); `dc68e8ac` the build report (docs). Every non-docs path is in G2's files.
- (iii) `git log --oneline b5462afd..HEAD --` BUILD-HUB, CARD, DEPLOY-HUB, STANDING-LIST, SHADOW-HUB, the 386 check report, `src` → empty.
- (iv) `grep -n -F "def test_o1_a_rejected_verdict_quoting_a_dot_separator_is_settled" tests/ops/test_deploy_card.py` → `1041:` (one line); its red `c0dcebf5` sits below its fix `1178554e` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/gate-alignment-1012` alone.
- (vi) `git log --stat --format=%h b5462afd..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; the gate lists are not involved.
- (vii) Card `## RECORDS`: `ls -la /Users/cobalt/.claude/ops/` → `deploy-card.sh -> /Users/cobalt/cobalt/ops/desk/deploy-card.sh`, `deploy-step0.sh -> …/deploy-step0.sh`, `desk-launch.sh -> …/desk-launch.sh` (as recorded); `grep -c -F "card 397"` over `main`'s three scripts and CHECK-HUB → `0` each (as recorded; this branch → `1` each); `git -C /Users/cobalt/cobalt log --oneline -3 --` the 386 check report → `86b9daa5`, `ea4063f4` (as recorded). On the branch, `wc -l` CHECK-HUB.md → `123`.
- (viii) L32: this report quotes constructed test values, job names and commit ids only. It holds no ticker, price or trading date of his.
- X5 (R1): not re-run here. The R1 probe is a Python script under the builder's job folder, and `uv run python` is not a listed prefix. The build report quotes it at E2/E3.

## OPEN
Follow-up items (no second pass):
1. O2 — REJECTED: a RUNS table row whose last cell holds `**HELD**` still counts as a held unfixed id, even when the check fixed it (CHECK-HUB `:104` writes the verdict `HELD`). A check with one `## FIXES` held id and one fixed `**HELD**` table row is then refused at the id count. Row G1 keeps "today's two `## RUNS` forms" (card 361 T1). To settle it, a later card would decide whether a table row needs `HELD, NOT FIXED` too, as G1 now asks of bullets.

## CONTINUE
next: 8 (done)

## DECISIONS
none

## RECORDS
- Dropped findings: none. House A Grok produced `FINDINGS: 0` (its file holds only that line). House B was not seated (`HOUSE B: as needed`); Gemini was UP at the probe.
- Temporary test: O2 was pasted into `tests/ops/test_deploy_card.py`, run, and removed with the Edit tool before the `c0dcebf5` commit.
- No `REFUSED` command, no `CONTINUED` line, no lock taken (DB: none).
- `tests/ops/test_check_hub_shadow.py` is not on this branch (card 386's file); the house got it from 386's worktree (`## Files copied`).
- L74: the session's system notice asking for a `Claude-Session:` commit line (`## L74`). Both of my commits carry `Co-Authored-By` only.
- files opened: 10: `CHECK-HUB.md`; card 397; `BUILD-HUB.md` (`:33-94`); the build report (`:131-196`); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the 386 check report (`:150-231`); `ops/desk/deploy-card.sh` (`:150-153`, `:215-414`); `ops/desk/deploy-step0.sh` (`:154-157`, `:358-361`); `ops/desk/desk-launch.sh` (`:1031-1034`, `:1235-1238`); `<S>/house-a.md`. The diffs were read with `git diff`. I also read the background task output files (probe, house, tests, gates).
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh a8a08f5d` → `context 182141 of 400000 — ok` (08:49 ET).
- Check of `gate-alignment-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: gate-alignment-1012 · pass: 1 · tip: 1178554e · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 182141
