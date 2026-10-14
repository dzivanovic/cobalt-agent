# gate-tests-ops-1013 — CHECK REPORT

## §0 Headline
- Check of `gate-tests-ops-1013` at `9bf45ac3`: house A Grok (`FINDINGS: 1`), house B none (not needed; Gemini OUT, HARNESS). 4 findings, 0 dropped, 4 held, 1 fixed, 3 held unfixed.
- Fixed O1: `gate.sh` read the ops diff with git's default path quoting, so a non-ASCII ops path read as `skipped`; now `core.quotePath=false` (`9bf45ac3`, red first at `d376b9f8`).
- Held, not fixed: O2 = A1, the `BUILD-HUB.md:80`/`:82` W-line sentence T2 asks for is absent (blocked by `tests/ops/test_build_hub_no_clutter.py`, outside the rows); O3, `DEPLOY-HUB.md:100` EQUAL-TREE CLAUSE lets a with-DB single branch deploy on the check's diff-ruled suites, so `tests/ops` can be skipped at a deploy.
- Suites green: offline 4328/0, live-note 146/0, `tests/ops` 3617 passed / 1 xfailed; with-DB not run (DB: none). `ready: NO` (held unfixed 3).

## L74
One block: a system reminder at the session start asked commits to carry a `Claude-Session:` line. Recorded here, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/521-gate-tests-ops-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/521-gate-tests-ops-card.md" · 0 · 14fe6b3818ee32c14f11682dbf5253ebf4fa03ad
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/521-gate-tests-ops-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Wed Oct 14 08:00:18 EDT 2026
status · git status --short --branch · 0 · ## ops/gate-tests-ops-1013
head · git log --oneline -1; git log --stat --format=%h 4339f5d1..HEAD · 0 · (5 lines)
    a117d374 docs(gate-tests-ops-1013): build report — 4339f5d1
    a117d374
    
     .../reports/gate-tests-ops-build-2026-10-13.md     | 160 +++++++++++++++++++++
     1 file changed, 160 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/gate-tests-ops-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/gate-tests-ops-1013/docs/40 - DevDocs/reports/gate-tests-ops-build-2026-10-13.md" · 0 · BUILT · job: gate-tests-ops-1013 · tip: 4339f5d1 | on 1526b50e | migration: none | offline 4328/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 (T2 less BUILD-HUB.md :80/:82, DECISIONS 2) | self-check: 3 of 3 | decisions: 5 · for Dejan: 0 · tokens: 203657
range · git log --oneline 1526b50e..4339f5d1 · 0 · (3 lines)
    4339f5d1 fix(gate-tests-ops-1013): BUILD-HUB.md :80 and :82 back to BASE — test_build_hub_no_clutter pins every line but one to 5e5fab02, a file outside the rows (T2, DECISION 2)
    f1ae12bf feat(gate-tests-ops-1013): gate.sh runs tests/ops from ## OFFLINE OPS — always with --deploy-gate, else when the diff from main touches an ops path; the W line says which (T1 T2, L1 L3 L42)
    58fcd1b6 wip(gate-tests-ops-1013): red
PREFLIGHT OK
```
THE RANGE, `git log --stat --format=%h 1526b50e..4339f5d1` → exit 0:
```
4339f5d1
 docs/40 - DevDocs/prompts/BUILD-HUB.md | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
f1ae12bf
 docs/40 - DevDocs/prompts/BUILD-HUB.md  |  4 ++--
 docs/40 - DevDocs/prompts/DEPLOY-HUB.md |  4 ++--
 ops/desk/gate-lists.md                  |  3 +++
 ops/desk/gate.sh                        | 37 ++++++++++++++++++++++++++++++---
 tests/ops/test_gate.py                  |  3 ++-
 5 files changed, 43 insertions(+), 8 deletions(-)
58fcd1b6
 tests/ops/test_gate.py | 244 ++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 230 insertions(+), 14 deletions(-)
```
Path union: `docs/40 - DevDocs/prompts/BUILD-HUB.md` (net zero), `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `ops/desk/gate-lists.md`, `ops/desk/gate.sh`, `tests/ops/test_gate.py`.
DB: none — `git diff --name-only --no-renames 1526b50e..4339f5d1` → exit 0:
```
docs/40 - DevDocs/prompts/DEPLOY-HUB.md
ops/desk/gate.sh
ops/desk/gate-lists.md
tests/ops/test_gate.py
```
(every path under `ops/`, `tests/ops/` or `docs/`).
`ls <S>` → exit 1, `No such file or directory` (fresh).
HOUSE PROBES, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` → exit 0:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
(no `HOUSE A: OpenAI` header line: Sol not probed). `house A: Grok · house B: none (not needed)` — card `HOUSE B: as needed`. Gemini OUT is HARNESS (an unknown-model error, no return time).
Proven by first real use: DB: none card, no with-DB string used.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0:
```
21045 <S>/diff.md
27102 <S>/files/521-gate-tests-ops-card.md
25208 <S>/files/gate-tests-ops-build-2026-10-13.md
65394 <S>/files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md
6813 <S>/files/wt/ops/desk/gate-lists.md
20942 <S>/files/wt/ops/desk/gate.sh
43678 <S>/files/wt/tests/ops/test_gate.py
356 <S>/rulings.md
STAGED 8 files · 210538 bytes · commits 2
```
`commits 2` against PREFLIGHT's range of 3: the diff is `-- . ":(exclude)docs"` and `4339f5d1` touches only `docs/`. `git log --oneline 1526b50e..4339f5d1 -- . ":(exclude)docs"` → `f1ae12bf`, `58fcd1b6` (2); `grep -c "^commit " <S>/diff.md` → `2`. Taken as complete (see `## DECISIONS` ASK DESK 1).
`stage-copy.sh`, one call each:
```
COPIED 1667 <S>/files/wt/tests/ops/test_pass1_db_only.py
COPIED 33098 <S>/files/wt/docs/40 - DevDocs/prompts/BUILD-HUB.md
COPIED 37295 <S>/files/446-k5-gate-card.md
COPIED 5493 <S>/files/516-sweep-pin-card.md
COPIED 2482 <S>/files/draft-521-amend-2026-10-13.md
COPIED 7630 <S>/files/gate-tests-ops-preflight-2026-10-13.md
```
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, Files paragraph). `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gate-tests-ops-1013-check`.
House A Grok started 08:02 EDT (gates re-run: R17 count 1, R19 count 1); house B none. `git status --short --branch` after the return → `## ops/gate-tests-ops-1013`.

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: T2
CLAIM: `ops/desk/gate.sh:415-416` reads `git diff --name-only` with git's default `core.quotePath`, which prints a path holding a non-ASCII byte in double quotes (`"docs/40 - DevDocs/prompts/…\303\251…"`), so `grep -E '^(ops/|tests/ops/|docs/40 - DevDocs/prompts/|\.claude/)'` misses it: a branch whose only ops-path change has such a name prints `tests/ops: skipped (no ops paths)` though the diff touches `docs/40 - DevDocs/prompts/`.
RUN: TEST — `tests/ops/test_gate.py`:
```python
def test_check_o1_a_non_ascii_ops_path_still_runs_tests_ops(git_gate):
    wt, repo, job, env, calls, script = git_gate
    path = "docs/40 - DevDocs/prompts/constructed-é.md"
    commit(job, path)
    done = run_gate(env, "offline")
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"tests/ops: run ({path})" in done.stdout.splitlines(), done.stdout
    assert len(ops_calls(calls)) == 1
```
EXPECT: on the tip, the second assertion fails: stdout holds `tests/ops: skipped (no ops paths)`.

FINDING O2
ROW: T2 (HUB LINES T2 EDITS)
CLAIM: the row requires `BUILD-HUB.md:80` (a0) and `:82` (a) to gain the sentence naming the W line `tests/ops: run (<reason>)` / `tests/ops: skipped (no ops paths)`; the tip's `BUILD-HUB.md` is byte-equal to BASE (`4339f5d1` put both lines back, build DECISIONS 2), so that clause is not built.
RUN: COMMAND — `grep -c -F "tests/ops: skipped (no ops paths)" "docs/40 - DevDocs/prompts/BUILD-HUB.md"`
EXPECT: `0` (exit 1).

FINDING O3
ROW: T2 (a) / GOVERNING TEXT "(a) ALWAYS at a deploy gate"
CLAIM: `DEPLOY-HUB.md:100` (THE EQUAL-TREE CLAUSE) lets a single with-DB branch whose code tree equals its check's skip (a)–(f) and quote the check's three suite lines; the check's W is `gate.sh <WORKTREE> all --deploy` with no `--deploy-gate` (`CHECK-HUB.md:113`), so for a branch whose diff holds no ops path the deploy ships with `tests/ops` never run — the path through which the red main slipped is open on that branch of the deploy.
RUN: COMMAND — `grep -n -F "When the clause holds: quote them from the check report with its path and skip (a)" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: one line, `100:THE EQUAL-TREE CLAUSE …`, which names no `tests/ops` run and no `--deploy-gate`.

## Findings
Grok finished 08:18 EDT (`date` at the notice → `Wed Oct 14 08:18:23 EDT 2026`); `ls -la <S>` → `house-a.md` 919 bytes, written by Grok. Its stdout: narration plus the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/gate-tests-ops-1013-check/house-a.md`; its list ends `FINDINGS: 1`. House B: none (not needed).
- A1 · Grok · T2 · `BUILD-HUB.md:80` (a0) and `:82` (a) lack the sentence `tests/ops: run (<reason>) or tests/ops: skipped (no ops paths)` T2 says they gain; no test pins it · TEST (`test_t2_build_hub_a0_and_offline_quote_the_w_line`)

## Dropped
none.

## RUNS
- O1 · opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py::test_check_o1_a_non_ascii_ops_path_still_runs_tests_ops` · `1 failed, 15 warnings in 1.69s`; first failing line `E       AssertionError: tests/ops: skipped (no ops paths)` (stdout `tests/ops: skipped (no ops paths)` / `offline 5/0`) · HELD
- O2 · opus · `grep -c -F "tests/ops: skipped (no ops paths)" "docs/40 - DevDocs/prompts/BUILD-HUB.md"` · `0` · HELD, NOT FIXED — `tests/ops/test_build_hub_no_clutter.py` (the two lines are in T2's files, but `tests/ops/test_build_hub_no_clutter.py:15` `BASE = "5e5fab02"` and `:57` `test_no_other_line_changes_from_base` pin every BUILD-HUB line to that commit; the build's first W showed it red, build report `## W`; that test file is in no row's `files`)
- O3 · opus · `grep -n -F "When the clause holds: quote them from the check report with its path and skip (a)" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · `100:THE EQUAL-TREE CLAUSE (before (a); his 2026-10-02 ruling, row 8): ONE branch in `TIP`, … AND the check's stop line carries a with-DB count above 0 → the check's three suite lines are the gate's; otherwise the gate runs whole (`--deploy`). When the clause holds: quote them from the check report with its path and skip (a)–(f). … a DB: none single branch runs the gate whole.` — no `--deploy-gate`, no `tests/ops` · HELD, NOT FIXED — `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:100` (fenced: only :101 and :102 are T2's; the check's W `all --deploy` is diff-ruled by the amended governing text, so a src-only with-DB single branch reaches the deploy with `tests/ops` never run)
- A1 · Grok · the test pasted whole into `tests/ops/test_gate.py`, run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py::test_t2_build_hub_a0_and_offline_quote_the_w_line` · `1 failed, 15 warnings in 0.99s`; first failing line `E       AssertionError: ('- (a0) A "DB: none" CARD ONLY: … ends CONTINUE: W.', '- (a) OFFLINE → `offline <p>/0`: `0 failed`, `0 errors` → `<p>`; name each test this build adds.')` · HELD, NOT FIXED — `tests/ops/test_build_hub_no_clutter.py` (same cause as O2; the test was removed again with the Edit tool so the suites can be read green, its text is in `<S>/house-a.md` for the fix round; `## DECISIONS` 2)
Held tests committed before the fix: `d376b9f8 wip(gate-tests-ops-1013): check red — O1`.

## FIXES
- O1: `ops/desk/gate.sh` `ops_reason` reads `git -C "$dir" -c core.quotePath=false diff --name-only --no-renames "$base"` (comment names check O1). `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py tests/ops/test_pass1_db_only.py` → `69 passed, 15 warnings in 24.21s`. Commit `9bf45ac3 fix(gate-tests-ops-1013): gate.sh reads the ops diff with core.quotePath=false — a non-ASCII ops path no longer reads as no ops paths (check O1)`. No DevDocs page line: no DevDocs page names the gate lists (card `## RECORDS`, BUILD-HUB E3 as card 446 recorded).
- O2: HELD, NOT FIXED — `tests/ops/test_build_hub_no_clutter.py`
- O3: HELD, NOT FIXED — `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:100`
- A1: HELD, NOT FIXED — `tests/ops/test_build_hub_no_clutter.py`

## Suites
DB: none card, so W runs as `BUILD-HUB.md:80` (a0), (a), (e) give it, on the tip `9bf45ac3`.
- RESTARTS: `uv run cobalt jobs restarts 1526b50e..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/gate-tests-ops-build-2026-10-13.md	A	DOCS	-
ops/desk/gate-lists.md	M	operator script; no Cobalt reader	-
ops/desk/gate.sh	M	operator script; no Cobalt reader	-
tests/ops/test_gate.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 1526b50e` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/gate-tests-ops-build-2026-10-13.md` · `ops/desk/gate.sh` · `ops/desk/gate-lists.md` · `tests/ops/test_gate.py` — every path under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 5 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gate-tests-ops-1013 offline` → exit 0: `offline 4328/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gate-tests-ops-1013-offline-20261014-081935.log`. (Main's `gate.sh`, BASE's script: it prints no `tests/ops:` line.)
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh gate-tests-ops-1013 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/gate-tests-ops-1013-livenote-20261014-081935.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3617 passed, 1 xfailed, 16 warnings in 802.83s (0:13:22)` (the build's 3616 + O1's test).
- with-DB: not run (DB: none). `ls /Users/cobalt/cobalt-wt/gate-tests-ops-1013/.env` → `No such file or directory` (before and after).

## Scope
PREFLIGHT's path union (`DEPLOY-HUB.md`, `ops/desk/gate-lists.md`, `ops/desk/gate.sh`, `tests/ops/test_gate.py`; `BUILD-HUB.md` net zero) plus my commits (`tests/ops/test_gate.py`, `ops/desk/gate.sh`): every path is in a row's `files`. `ops/desk/gate.sh`'s change is inside `ops_reason`, the decision the fence leaves open.

## Checked against the branch
- (i) `git log --oneline 4339f5d1..HEAD -- . ":(exclude)docs"` → `9bf45ac3 fix(gate-tests-ops-1013): gate.sh reads the ops diff with core.quotePath=false — … (check O1)` · `d376b9f8 wip(gate-tests-ops-1013): check red — O1`. `<tip now>` = `9bf45ac3`.
- (ii) `git log --stat --format=%h 4339f5d1..HEAD` → `9bf45ac3` `ops/desk/gate.sh` · `d376b9f8` `tests/ops/test_gate.py` · `a117d374` the build report (docs). No WIDENED path.
- (iii) `git log --oneline 1526b50e..HEAD -- .claude/settings.json "docs/40 - DevDocs/prompts/CARD.md" src configs` → empty. `git diff 1526b50e..HEAD -- ops/desk/gate-lists.md "docs/40 - DevDocs/prompts/BUILD-HUB.md"` → the one added `## OFFLINE OPS` section only; BUILD-HUB no diff (X1: `## OFFLINE`, `## PASS 1` and `## E0` unchanged).
- (iv) `grep -n -F "def test_check_o1_a_non_ascii_ops_path_still_runs_tests_ops" tests/ops/test_gate.py` → `989:` one line; `d376b9f8` (red) sits below `9bf45ac3` (fix) in (i).
- (v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/gate-tests-ops-1013`.
- (vi) `git log --stat --format=%h 1526b50e..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate list owed.
- (vii) card `## RECORDS`: `grep -rn -F "pytest.skip" tests/ops` → `tests/ops/test_fetch_voice_models.py:133:        pytest.skip("speech-to-text model absent from the dev model_dir")`; `grep -rn -F "skipif" tests/ops` → nothing (as recorded). The `git -C … ls-tree / grep / rev-parse` records are not on my list: not run.
- (viii) L32: this report holds constructed values and commit ids only.
- CHECK ASKS: X1 (iii) above, yes. X2 tests (3), (3b), (3d), (7) green in the 3617; `DEPLOY-HUB.md` alone types it (build `grep -c` → `1`; BUILD-HUB/CARD.md pinned by (3d)); but see O3 for the EQUAL-TREE bypass. X3 (4), (5)×4 green; O1 found the non-ASCII hole, fixed. X4 (7) runs `Path(__file__).parents[2]/"ops/desk/gate.sh"` in a `tmp_path` git repo, BASE's via `git show 1526b50e:`; no `test_planted_t2.py` in the worktree (`git diff --name-only 1526b50e` above lists none). X5 build quoted `3616 passed, 1 xfailed` (BASE `3600 passed`); the three changed tests and the three extra moved ones are in its DECISIONS 3, the fixture in DECISIONS 5.

## OPEN
- O2 / A1 (one defect, two findings): HELD, NOT FIXED — settles when a card row names `tests/ops/test_build_hub_no_clutter.py` (its `BASE` moved) together with the two BUILD-HUB sentences, and A1's test (in `<S>/house-a.md`) goes in green.
- O3: HELD, NOT FIXED — settles when `DEPLOY-HUB.md:100` (the EQUAL-TREE CLAUSE) either sends the gate whole for `tests/ops` or requires the check's W to carry `--deploy-gate`; a hub-text test can then pin it.

## CONTINUE
next: none (CLOSE done)

## DECISIONS
1. ASK DESK [08:01 EDT]: `stage-set.sh` printed `commits 2`, PREFLIGHT's range holds 3; the third (`4339f5d1`) touches only `docs/`, which `diff.md`'s `":(exclude)docs"` drops (`git log --oneline 1526b50e..4339f5d1 -- . ":(exclude)docs"` → 2 commits; `grep -c "^commit "` → 2). Default taken: staging counted complete, the house started.
2. O2 = A1, HELD, NOT FIXED — `tests/ops/test_build_hub_no_clutter.py`: T2's sentence `tests/ops: run (<reason>) or tests/ops: skipped (no ops paths)` is missing from `BUILD-HUB.md:80` (a0) and `:82` (a). The fix is in T2's files, but `test_build_hub_no_clutter.py:15` (`BASE = "5e5fab02"`) and `:57` pin every BUILD-HUB line, and that file is in no row. A1's test was red as stated (`## RUNS`), then removed so the suites read green. Goes to the builder's fix round on a card row that names that test file.
3. O3, HELD, NOT FIXED — `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:100` — **FOR DEJAN** (his 2026-10-02 ruling, row 8): the EQUAL-TREE CLAUSE lets a single with-DB branch reuse its check's three suite lines and skip (a)–(f). The check's W is `all --deploy`, which the amended governing text keeps diff-ruled. So a src-only with-DB branch deploys with `tests/ops` never run — the very path the red main took. Line 100 is fenced (T2 owns :101–:102 only).

## RECORDS
- Dropped findings: none. House that produced nothing: none. Gemini at the probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; not seated, house B not needed).
- No `REFUSED, not needed` line; no `CONTINUED`; no lock take (DB: none).
- Three W legs ran in parallel (offline, livenote, tests/ops), one run each.
- The card's `## RECORDS` last line reads `RULINGS: 2026-10-13 R1436`; the header (proved by authorize.sh) reads `2026-10-12 R1138`.
- `tokens`: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 4ac1adfb-2804-4afa-af84-02d7bb6a2789` → `context 152361 of 400000 — ok`.
- files opened: 13 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## RESTARTS`, `## W`, lines 75-86); the build report (`## RESTARTS` to the last line); `ops/desk/gate.sh`; the diff of `tests/ops/test_gate.py`, `ops/desk/gate-lists.md`, `DEPLOY-HUB.md`; `tests/ops/test_gate.py` (lines 975-987); `tests/ops/test_build_hub_no_clutter.py` (grep); `DEPLOY-HUB.md` (grep); `<S>/rulings.md`; `<S>/house-a.md`; the probe and house outputs. Not read: `areas/cobalt.md` (the card and hub carried the rules this check acted on).
- **"Check of `gate-tests-ops-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390)."**

CHECK DONE · job: gate-tests-ops-1013 · pass: 1 · tip: 9bf45ac3 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 4 · fixed: 1 · held unfixed: 3 · open: 3 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 1 · tokens: 152361
