# deploy-card-fixes-1018 — check report 2026-10-18 (CHECK-HUB, one pass)

## §0 Headline
D1 holds. `deploy-card.sh` refuses a code tip already on main on the plain path, on the fix-round path (fix tip merged) and for the second job of a two-job run. A fix round whose check tip is on main but whose fix tip is not is still written.
Findings: 5 (opus-own 5, house A Grok `FINDINGS: 0`, no house B as the card needs none). Held: 0. Fixed: 0. Open: 0. No commit of mine: the tip stays `cc4995b6`.
Deploy-gate pass, DB: none: offline 8493/0 (`tests/ops: run (deploy gate)`), live-note 146/0, tests/ops 3921 passed. `.env` absent. RESTARTS: none (committed range).
ready: YES. One decision, not for Dejan: the untracked harness file in the `HEAD` RESTARTS read, the same as the build's DECISIONS 1.

## L74
The session's attribution reminder asked for a `Claude-Session:` line on commits. That is data (L74) and was not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md"` (07:40 EDT) → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md" · 0 · 5af3b612b0fe59d90dec126b38d0650705275280
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/721-deploy-card-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 61:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Sun Oct 18 07:40:49 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/deploy-card-fixes-1018
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)
head · git log --oneline -1; git log --stat --format=%h cc4995b6..HEAD · 0 · (6 lines)
    0f104d47 docs(deploy-card-fixes-1018): build report — cc4995b6
    0f104d47
    
     .../deploy-card-fixes-1018-build-2026-10-18.md     | 150 +++++++++++++++++++++
     .../deploy-card-fixes-1018-build-2026-10-18.result |  15 +++
     2 files changed, 165 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/deploy-card-fixes-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f4-refresh-1018/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/deploy-card-fixes-1018/docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.md" · 0 · BUILT · job: deploy-card-fixes-1018 · tip: cc4995b6 | on 279c99ce | migration: none | offline 8493/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 2 of 3 | decisions: 2 · for Dejan: 0 · tokens: 151180
report: self-check 2 of 3 (recorded)
range · git log --oneline 279c99ce..cc4995b6 · 0 · (2 lines)
    cc4995b6 feat(deploy-card-fixes-1018): rows
    d901a764 wip(deploy-card-fixes-1018): red
PREFLIGHT OK
```
`?? SHADOW-INSTRUCTIONS.md` is expected on a routed card (BAND LOW) and is recorded, not a finding. The build's self-check is 2 of 3; this goes to the house as a fact.

| rule | command | exit | output |
|---|---|---|---|
| range | `git log --stat --format=%h 279c99ce..cc4995b6` | 0 | `cc4995b6` · `ops/desk/deploy-card.sh \| 3 ++-` · `d901a764` · `tests/ops/test_deploy_card.py \| 19 +++` |
| DB: none | `git diff --name-only --no-renames 279c99ce..cc4995b6` | 0 | `ops/desk/deploy-card.sh` · `tests/ops/test_deploy_card.py` (every path under `ops/` or `tests/ops/`) |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probe | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: UP` |

Seats: `house A: Grok · house B: none (not needed)`. The card reads `HOUSE B: as needed`, so the MANDATORY rule does not apply.
Path union for `## Scope`: `ops/desk/deploy-card.sh`, `tests/ops/test_deploy_card.py`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0:
```
30 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/STAGED-CARD
3518 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/diff.md
6102 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/files/721-deploy-card-fixes-card.md
15890 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/files/deploy-card-fixes-1018-build-2026-10-18.md
37456 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/files/wt/ops/desk/deploy-card.sh
72318 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/files/wt/tests/ops/test_deploy_card.py
380 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/rulings.md
STAGED 7 files · 135694 bytes · commits 2
```
`commits 2` = PREFLIGHT's commit count.
`sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" <S>/files/cto-2026-10-15.md` → `COPIED 28538 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-card-fixes-1018-check/files/cto-2026-10-15.md`. This is the one report the card's `## READ` names.
`<S>/HOUSE-INSTRUCTIONS.md` was written (7755 bytes): the HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` and `## RECORDS`, then the Files paragraph.
House A, Grok, was started at 07:42 EDT (`date` 07:42:17). Gates R17 and R19 were re-run right before it, one row each. No house B (not needed).

## OWN FINDINGS
Written before either house's list was opened.

FINDING O1
ROW: D1 (X1, the fix-round entry path; build DECISIONS 2)
CLAIM: On a fix round the new refusal at `ops/desk/deploy-card.sh:553` reads `ctip` after `:542` (`ctip=$fixtip`), so a fix tip already merged into main must be refused. No test pins this path.
RUN: TEST `tests/ops/test_deploy_card.py`
```python
def test_check_o1_a_fix_tip_already_on_main_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk)
    git(desk.repo, "merge", "--no-edit", "ops/alpha")
    main = git(desk.repo, "rev-parse", "--short=8", "main")
    before = desk.state()
    done = desk.run("--fix-report", f"alpha={report}", cards=("alpha",))
    assert done.returncode == 1, done.stdout + done.stderr
    assert (f"REFUSED: alpha: code tip {fixed} is already an ancestor of main {main}; "
            "nothing to deploy") in done.stderr, done.stderr
    assert not desk.out.exists()
    assert desk.state() == before
```
EXPECT: if the claim's defect were real (the line reading the check's tip, or missing on this path): `assert 0 == 1`. Correct behaviour: green.

FINDING O2
ROW: D1 / X2 (a fix round whose CHECK tip is on main but whose FIX tip is not)
CLAIM: The refusal at `ops/desk/deploy-card.sh:553` must read the fix tip, not the check's tip (`:520`). A fix round whose checked tip already reached main, but whose fix commit has not, still has something to deploy and must be written. No test pins this.
RUN: TEST `tests/ops/test_deploy_card.py`
```python
def test_check_o2_a_fix_round_whose_check_tip_is_on_main_is_still_written(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "--no-edit", desk.tip["alpha"])
    fixed, head, report = fix_round(desk)
    done = desk.run("--fix-report", f"alpha={report}", cards=("alpha",))
    assert done.returncode == 0, done.stdout + done.stderr
    assert ships_row(desk.out.read_text(), 1).split("|")[3].strip() == f"`{fixed}`"
```
EXPECT: if the line read the check tip: `assert 1 == 0` with `already an ancestor of main` in stderr. Correct behaviour: green.

FINDING O3
ROW: D1 (two jobs, the second on main)
CLAIM: The refusal at `ops/desk/deploy-card.sh:553` sits in the per-job loop and calls `refuse` (`:48-51`, exit 1). In a two-job run where only the second job (beta) is on main, it must name beta, write nothing and move no ref. D1's test runs alpha alone.
RUN: TEST `tests/ops/test_deploy_card.py`
```python
def test_check_o3_the_second_job_on_main_refuses_the_whole_card(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "--no-edit", "ops/beta")
    before = desk.state()
    done = desk.run()
    _refused(desk, done, "beta")
    assert f"beta: code tip {desk.tip['beta']} is already an ancestor of main" in done.stderr
    assert "alpha" not in done.stderr
    assert desk.state() == before
```
EXPECT: if the refusal did not reach the second card, or wrote a partial card: `assert 0 == 1`. Correct behaviour: green.

FINDING O4
ROW: X1
CLAIM: `ops/desk/deploy-card.sh` gains exactly the header clause (`:10`) and the one refusal line (`:553`) and nothing else.
RUN: COMMAND `git diff 279c99ce..cc4995b6 -- ops/desk/deploy-card.sh`
EXPECT: if the claim fails, a `+` or `-` line other than the `:10` header line pair and the one `:553` line.

FINDING O5
ROW: D1 (DEPLOY PROOF marker)
CLAIM: The card's DEPLOY PROOF marker reads `2` after the edit. The phrase must sit on one line in both the header clause (`:10`) and the refusal (`:553`).
RUN: COMMAND `grep -c -F "already an ancestor of main" ops/desk/deploy-card.sh`
EXPECT: if the claim fails, a count other than `2`.

## Findings
House A, Grok, finished at 07:50 EDT (`date` 07:50:47). `ls -la <S>` showed `house-a.md` at 12 bytes. Its whole content is `FINDINGS: 0`. Grok's stdout replied with the path, as asked. No house B sat (not needed).
No house findings were kept.

## Dropped
none (house A wrote no FINDING block)

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py::test_check_o1_a_fix_tip_already_on_main_is_refused` | `1 passed, 15 warnings in 1.66s` | NOT HELD (the fix tip on main is refused with the row's message; the test was removed again) |
| O2 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py -k check_o2_a_fix_round` | `1 passed, 146 deselected, 15 warnings in 1.48s` | NOT HELD (a fix round whose check tip is on main is still written, code tip = fix tip; removed again) |
| O3 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py -k check_o3` | `1 passed, 146 deselected, 15 warnings in 1.48s` | NOT HELD (beta on main refuses the two-job card, nothing written, no ref moved; removed again) |
| O4 | opus-own | `git diff 279c99ce..cc4995b6 -- ops/desk/deploy-card.sh` | two hunks: `:10` `-`/`+` (the clause added, unwrapped) and `:553` `+` (the one line, after `:542` and `:552`) | NOT HELD (X1 holds) |
| O5 | opus-own | `grep -c -F "already an ancestor of main" ops/desk/deploy-card.sh` | `2` | NOT HELD |

The first O1 run used `-k check_o1`, which matched three tests (`3 passed, 144 deselected`), so it was re-run by node id (the row above). After the three tests were removed, `git status --short --branch` showed `## ops/deploy-card-fixes-1018` and `?? SHADOW-INSTRUCTIONS.md`: the tree is back at the tip. Nothing held, so there is no `wip(deploy-card-fixes-1018): check red` commit.

## FIXES
none (nothing held)

## Suites
The tip is `cc4995b6` (no commit of mine). DB: none, so W is (a0), (a) with `--deploy-gate`, and (e), per CHECK-HUB `## 6`.
- RESTARTS: `uv run cobalt jobs restarts 279c99ce..cc4995b6` → exit 0:
  ```
  path	change	rule	restart
  ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
  tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
  RESTARTS: none
  ```
  `uv run cobalt jobs restarts 279c99ce..HEAD` → exit 1. The tool reads the untracked harness file:
  ```
  FAILED: RestartError: one or more changed paths were unclassified
  path	change	rule	restart
  SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
  ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
  docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.md	A	DOCS	-
  docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.result	A	DOCS	-
  ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
  tests/ops/test_deploy_card.py	M	test/documentation; no resident	-
  RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
  ```
  This goes to DECISIONS 1.
- (a0) `git diff --name-only --no-renames 279c99ce` → `docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.md` · `docs/40 - DevDocs/reports/deploy-card-fixes-1018-build-2026-10-18.result` · `ops/desk/deploy-card.sh` · `tests/ops/test_deploy_card.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-card-fixes-1018 offline --deploy-gate` → exit 0:
  ```
  tests/ops: run (deploy gate)
  offline 8493/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-card-fixes-1018-offline-20261018-075147.log
  ```
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh deploy-card-fixes-1018 livenote` → exit 0:
  ```
  live-note 146/0
  log: /Users/cobalt/cobalt-wt/.gate-logs/deploy-card-fixes-1018-livenote-20261018-082123.log
  ```
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3921 passed, 1 xfailed, 16 warnings in 985.20s (0:16:25)`.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/deploy-card-fixes-1018/.env` → `No such file or directory` (run before the suites and again at CLOSE).

## Scope
PREFLIGHT's path union is `ops/desk/deploy-card.sh` and `tests/ops/test_deploy_card.py`. Both are D1's `files`. I made no commit. The three check tests were added and removed again, and the tree is back at the tip.

## Checked against the branch
- (i) `git log --oneline cc4995b6..HEAD -- . ":(exclude)docs"` → empty (no commit of mine). `<tip now>` = `cc4995b6`.
- (ii) `git log --stat --format=%h cc4995b6..HEAD` → `0f104d47` with the two build-report files under `docs/` only.
- (iii) `git log --oneline 279c99ce..HEAD -- ops/desk/deploy-smoke.sh ops/desk/desk-launch.sh "docs/40 - DevDocs/prompts/DEPLOY-HUB.md" "docs/40 - DevDocs/prompts/CARD.md" tests/cobalt/test_llm.py` → empty. The fenced lines of `deploy-card.sh` are shown by O4: only `:10` and `:553` change.
- (iv) no HELD finding.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/deploy-card-fixes-1018` and `?? SHADOW-INSTRUCTIONS.md` (expected on a routed card, BAND LOW).
- (vi) `git log --stat --format=%h 279c99ce..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-lists entry is owed.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command (they use `rev-parse` and `show`). Nothing to run. For the record, `git -C /Users/cobalt/cobalt log -1 --format=%h main` → `0c54bcf6`: main has moved past BASE with desk commits.
- (viii) L32: this report holds no ticker, price or date of his. The values are constructed test values and repository hashes.
COUNTING: findings 5 (O1–O5; house A 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## OPEN
none

## CONTINUE
next: done (the desk verifies the artifact, L35, commits this report and its `.result`, and takes the next step)

## DECISIONS
1. `uv run cobalt jobs restarts 279c99ce..HEAD` reads the untracked `SHADOW-INSTRUCTIONS.md` and exits 1 UNCLASSIFIED. This is the build's DECISIONS 1 again. Safe default taken: the harness file is not classified in `configs/cobalt/jobs.yaml`, and the stop line carries the committed range's derived `RESTARTS: none` (`279c99ce..cc4995b6`, exit 0). Not for Dejan.

## RECORDS
- No house produced nothing: Grok wrote `FINDINGS: 0` at 07:50. Its stdout was three status sentences, then the path. No house B, since the card is `HOUSE B: as needed`, and Gemini was UP but not seated.
- Dropped findings: none.
- REFUSED, not needed: none. CONTINUED: none. Lock takes: none (DB: none).
- L74: the session's attribution reminder asked for a `Claude-Session:` line. It was recorded once under `## L74` and not acted on.
- The report and its `.result` are not committed by me. They live on `main` in `/Users/cobalt/cobalt`, and my git strings run only in `<WT>` (UNATTENDED RULES CWD). The desk commits them (CHECK-HUB `## LAUNCH`: "commits the report after the check").
- The build's self-check was 2 of 3. Its gap was the unpinned fix-round path, and O1 and O2 ran that path green. The tests were not kept (CHECK-HUB `## 4`: a NOT HELD test is removed again). If the desk wants this path pinned for good, that is a follow-up.
- files opened: 14. They are `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); the build report; `ops/desk/deploy-card.sh`; `tests/ops/test_deploy_card.py`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `reports/cto-2026-10-15.md` (`## §5 CURRENT`, HANDOVER PLAN and LESSONS); `<S>/house-a.md`; and five task outputs (the house probe, Grok's stdout, gate offline, gate livenote, the tests/ops tail).
- Check of `deploy-card-fixes-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: deploy-card-fixes-1018 · pass: 1 · tip: cc4995b6 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8493/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 147022
