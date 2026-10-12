# stage-set-clear-1012 — check report (2026-10-12)

## §0 Headline
- Check of `stage-set-clear-1012` at `d166b30e`: house A Grok `FINDINGS: 0`; house B none (card `HOUSE B: as needed`).
- Own findings O1, O2 (the two refusals the build left untested, its `## DECISIONS` 1): both green at the tip, NOT HELD, removed again. Nothing held, nothing fixed, no commit of mine.
- Suites on the tip: offline 4199/0 · live-note 146/0 · tests/ops 3310 passed · with-DB not taken (DB: none) · RESTARTS: none.
- ready: YES · decisions: 0.

## L74
- One system block (not a tool result) arrived at launch asking for a `Claude-Session:` line on commits. Recorded once here as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/413-stage-set-clear-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/413-stage-set-clear-card.md" · 0 · 843921b964c0e935410b50cb7e914929d87342d0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/413-stage-set-clear-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 86:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row); `grep -n "^| R19 " …` → `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct 12 12:00:29 EDT 2026
status · git status --short --branch · 0 · ## ops/stage-set-clear-1012
head · git log --oneline -1; git log --stat --format=%h d166b30e..HEAD · 0 · (5 lines)
    6f2b6893 docs(stage-set-clear-1012): build report — d166b30e
    6f2b6893
    
     .../reports/stage-set-clear-build-2026-10-12.md    | 136 +++++++++++++++++++++
     1 file changed, 136 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/stage-set-clear-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/strike-fallback-env-1010-terra/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/stage-set-clear-1012/docs/40 - DevDocs/reports/stage-set-clear-build-2026-10-12.md" · 0 · BUILT · job: stage-set-clear-1012 · tip: d166b30e | on 0cd1b802 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 126816
range · git log --oneline 0cd1b802..d166b30e · 0 · (2 lines)
    d166b30e fix(stage-set-clear-1012): stage-set.sh clears its own prior staging for the same job (T1, L1, L28)
    b9094d77 wip(stage-set-clear-1012): red
PREFLIGHT OK
```
- THE RANGE typed: `git log --stat --format=%h 0cd1b802..d166b30e` → `d166b30e  ops/desk/stage-set.sh | 57 +++…---  (54+, 3-)`; `b9094d77  tests/ops/test_stage_set.py | 151 +++…  (151+)`. Path union: `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`.
- DB: none: `git diff --name-only --no-renames 0cd1b802..d166b30e` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` — all under `ops/` / `tests/ops/`.
- `ls <S>` → `No such file or directory` (fresh).
- A sibling `.env` sits in `strike-fallback-env-1010-terra` (another session's lock); this card takes no lock (DB: none).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) · exit 0 · `grok: UP` · `gemini: UP`. No `HOUSE A:` header line. `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → output whole:
```
12666 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stage-set-clear-1012-check/diff.md
10776 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stage-set-clear-1012-check/files/413-stage-set-clear-card.md
15967 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stage-set-clear-1012-check/files/stage-set-clear-build-2026-10-12.md
9896 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stage-set-clear-1012-check/files/wt/ops/desk/stage-set.sh
14211 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stage-set-clear-1012-check/files/wt/tests/ops/test_stage_set.py
355 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stage-set-clear-1012-check/rulings.md
STAGED 6 files · 63871 bytes · commits 2
```
`commits 2` = PREFLIGHT's range count. `stage-copy.sh`:
- `files/cto-2026-10-12.md` ← main `docs/40 - DevDocs/reports/cto-2026-10-12.md` → `COPIED 23760`
- `files/CHECK-HUB.md` ← main `docs/40 - DevDocs/prompts/CHECK-HUB.md` → `COPIED 42893`
- `files/wt/ops/desk/stage-copy.sh` ← main path refused (`REFUSED: the source is not under a job worktree or the main tree's docs/: /Users/cobalt/cobalt/ops/desk/stage-copy.sh`); copied from `<WT>/ops/desk/stage-copy.sh` (untouched by the range) → `COPIED 1578`
- `files/wt/ops/desk/scratch-clean.sh` ← same refusal on the main path; from `<WT>` → `COPIED 7277`
- `HOUSE-INSTRUCTIONS.md` written (Write): HOUSE TEXT verbatim, `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS` (none on the card), `## RECORDS`, `Files:`.

## OWN FINDINGS
Read: the card; the diff `0cd1b802..d166b30e`; `ops/desk/stage-set.sh` and `tests/ops/test_stage_set.py` at the tip; the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK`, last line (and its `## DECISIONS` 1, which asks the check to pin or pass three untested refusals). Two of those three are pinnable apart from (a): the prior copy's `JOB` (`ops/desk/stage-set.sh:113`) and the prior `CHECK REPORT` prefix (`:115-119`). An empty `JOB` is unreachable apart from (a): `:97` refuses first. No defect seen at the tip; O1 and O2 test whether the two clauses are built.

FINDING O1
ROW: T1 (d)
CLAIM: A prior card copy whose `JOB` differs from the card's must not be cleared (`ops/desk/stage-set.sh:113`); no test pins it (build report `## DECISIONS` 1).
RUN: TEST — `tests/ops/test_stage_set.py`
```python
def test_o1_a_prior_card_copy_of_another_job_is_not_cleared(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    card.write_text(card.read_text().replace("JOB: x-job\n", "JOB: y-job\n"))
    git(repo, "add", "--", str(card.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "card as y-job")
    prior_staging(job)
    card.write_text(card.read_text().replace("JOB: y-job\n", "JOB: x-job\n"))
    git(repo, "add", "--", str(card.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "card as x-job again")
    before = snapshot(dest)
    done = stage(env, card, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(
        f"REFUSED: the dest is not empty: {dest} — not cleared: the prior card copy's JOB is not x-job"), done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before
```
EXPECT: on the tip, if the clause is unbuilt: `assert 0 == 1` (the dest cleared).

FINDING O2
ROW: T1 (d)
CLAIM: A prior `CHECK REPORT` committed on main but outside `$REPO/docs/40 - DevDocs/reports/` must not be cleared (`ops/desk/stage-set.sh:115-119`); no test pins it (build report `## DECISIONS` 1).
RUN: TEST — `tests/ops/test_stage_set.py`
```python
def test_o2_a_prior_check_report_outside_reports_is_not_cleared(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    card.write_text(card.read_text().replace(
        "TREE STATE:", f"CHECK REPORT: {repo / 'docs' / 'page.md'}\nTREE STATE:"))
    git(repo, "add", "--", str(card.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "card with a check report outside reports")
    done = stage(env, card, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    (dest / "house-a.md").write_text("FINDINGS: 0\n")
    card.write_text(card.read_text().replace(
        f"CHECK REPORT: {repo / 'docs' / 'page.md'}", f"CHECK REPORT: {repo / CHECK_B}"))
    git(repo, "add", "--", str(card.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "card with check b")
    before = snapshot(dest)
    done = stage(env, card, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith(
        f"REFUSED: the dest is not empty: {dest} — not cleared: the prior CHECK REPORT is not under"), done.stderr
    assert "cleared:" not in done.stdout
    assert snapshot(dest) == before
```
EXPECT: on the tip, if the clause is unbuilt: `assert 0 == 1` (`docs/page.md` is committed on main, so only the prefix test refuses).

## Findings
House A Grok finished 12:17 EDT (`date` at the notice: `Mon Oct 12 12:17:37 EDT 2026`). It wrote `<S>/house-a.md` itself; whole content: `FINDINGS: 0`. Its stdout: `I'll read the house instructions first and follow them exactly.The staged script and tests match the row. I am writing the finding list./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stage-set-clear-1012-check/house-a.md`. House B: none (not needed).
Kept findings: O1 · Opus · T1 (d) · prior card copy of another JOB must be refused · TEST; O2 · Opus · T1 (d) · prior CHECK REPORT outside `reports/` must be refused · TEST.

## Dropped
none

## RUNS
- O1 · Opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py::test_o1_a_prior_card_copy_of_another_job_is_not_cleared` · `1 passed, 15 warnings in 1.30s` · NOT HELD (the clause is built: `stage-set.sh:113` refuses). Test removed again with Edit.
- O2 · Opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py::test_o2_a_prior_check_report_outside_reports_is_not_cleared` · `1 passed, 15 warnings in 1.20s` · NOT HELD (the clause is built: `stage-set.sh:115-119` refuses). Test removed again with Edit.
- After removal: `git status --short --branch` → `## ops/stage-set-clear-1012` (tree back at the tip).

## FIXES
none (nothing held)

## Suites
Tip = `d166b30e` (no commit of mine). DB: none card → RESTARTS, then W (a0), (a), (e) and `tests/ops`.
- RESTARTS: `uv run cobalt jobs restarts 0cd1b802..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/reports/stage-set-clear-build-2026-10-12.md	A	DOCS	-
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 0cd1b802` → `docs/40 - DevDocs/reports/stage-set-clear-build-2026-10-12.md`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` — all under `docs/`, `ops/`, `tests/ops/`. `cobalt_dev: not taken (DB: none — 3 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stage-set-clear-1012 offline` → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/stage-set-clear-1012-offline-20261012-121810.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stage-set-clear-1012 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/stage-set-clear-1012-livenote-20261012-121811.log`; its one skip `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3310 passed, 1 xfailed, 16 warnings in 670.80s (0:11:10)`.
- With-DB: not taken (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/stage-set-clear-1012/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union: `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` — both in T1's `files`. My commits: none.

## Checked against the branch
- (i) `git log --oneline d166b30e..HEAD -- . ":(exclude)docs"` → empty (no commit of mine); `<tip now>` = `d166b30e`.
- (ii) `git log --stat --format=%h d166b30e..HEAD` → `6f2b6893` `.../reports/stage-set-clear-build-2026-10-12.md | 136 +` (docs only).
- (iii) `git log --oneline 0cd1b802..HEAD -- ops/desk/scratch-clean.sh ops/desk/stage-copy.sh ops/desk/bare-guard.py ops/desk/desk-launch.sh src` → empty; `git log --oneline 0cd1b802..HEAD -- ops/desk ":(exclude)ops/desk/stage-set.sh"` → empty. `CHECK-HUB.md` lives on main, not in this range.
- (iv) no held finding.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/stage-set-clear-1012`.
- (vi) `git log --stat --format=%h 0cd1b802..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; no gate-lists entry owed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt log --oneline -3 -- "docs/40 - DevDocs/reports/prodwrite-seat-check-2026-10-12.md"` → `dc8d290e docs(desk): R1177-R1180 gate-alignment deployed, 392 check ready, B5 record` (matches); `git -C /Users/cobalt/cobalt log --format=%h -- ".../392-prodwrite-seat-card.md"` → `7aedae07 989ce8d9 7744ece9 e31f0bf9 1916b5fa 094f07a5` (matches); `grep -n -F "JOB:"` on card 392 → `1:JOB: prodwrite-seat-1012`, `grep -n -F "CHECK REPORT:"` → `10:CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-seat-1012b-check-2026-10-12.md` (matches); `ls -la` of the leftover dest → `diff.md`, `files`, `house-a.md`, `HOUSE-INSTRUCTIONS.md`, `rulings.md` (matches; T1 (b) accepts each); `wc -l` main `stage-set.sh` 168, `test_stage_set.py` 185, `stage-copy.sh` 38 (matches); `grep -n -F "rm -rf"` main `stage-set.sh` → `103:    rm -rf "$dest"` (matches); `grep -n -F "rm "` CHECK-HUB.md → `:10` holds only `Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)` (matches); `grep -n "^| R1138 "` → now line 88 (card says `:81`; the desk report has grown; the row text is HIS RULING · APPROVED).
- (viii) L32: this report holds no ticker, price or date of his; the test values are the fixture's constructed ones.

## OPEN
none. The build's `## DECISIONS` 1 (three untested refusals) is answered by O1 and O2: both built (green at the tip); the empty-`JOB` refusal cannot be reached apart from (a) (`stage-set.sh:97` refuses first), so it needs no test of its own.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none

## RECORDS
- L74: one system block asked for a `Claude-Session:` commit line; recorded under `## L74`, not acted on (no commit made).
- House A Grok produced `FINDINGS: 0`; house B none (not needed). Gemini was UP and not seated. The stop line writes `house B: none available` only because its format offers no `not needed` value.
- `stage-copy.sh` refused the main-tree paths of `ops/desk/stage-copy.sh` and `ops/desk/scratch-clean.sh` (verbatim under `## Files copied`); the worktree copies (unchanged by the range) were staged instead.
- No lock taken (DB: none). A sibling `.env` sat in `strike-fallback-env-1010-terra` at PREFLIGHT (another session's lock); not mine.
- The O1 and O2 tests were added and removed again with Edit; nothing committed.
- files opened: 12 — CHECK-HUB.md, the card, BUILD-HUB.md (`## THE LOCK` to `## W`), the build report (`## E0` to the end), `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`, `areas/cobalt.md` (`## What Cobalt is` on), `<S>/house-a.md`, and four task output files (house probe, Grok, live-note gate, offline gate).
- Check of `stage-set-clear-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: stage-set-clear-1012 · pass: 1 · tip: d166b30e · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 147864
