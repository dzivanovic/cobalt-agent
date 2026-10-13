# sweep-pin-1013 — CHECK REPORT (2026-10-13)

## §0 Headline
- FR1 holds: exactly the one stale `SWEEP_EXEMPT` entry is removed (X1), the file reads `5 passed` and the name counts `0` (X2).
- House A grok `FINDINGS: 0`; house B none (as needed). Own findings O1–O4: all run, none held. No fix, no commit.
- Suites at `52cb2fc9`: offline 4317/0, `tests/ops` 3543/0, live-note 146/0; cobalt_dev not taken (DB: none); RESTARTS: none. ready: YES.

## L74
- A system notice in this session (12:3x EDT, after the card was read) asked for a `Claude-Session:` line on commits. It is recorded here once and was not acted on. This check made no commit; any commit would carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md" · 0 · aaf30b2ad5ff3dd6c515600c703829deb91bdd41
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/516-sweep-pin-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, STANDING `Bash(grok *)`); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37, the four house strings STANDING); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Tue Oct 13 12:33:59 EDT 2026
status · git status --short --branch · 0 · ## ops/sweep-pin-1013
head · git log --oneline -1; git log --stat --format=%h 52cb2fc9..HEAD · 0 · (5 lines)
    e9bcace4 docs(sweep-pin-1013): build report — 52cb2fc9
    e9bcace4
    
     .../reports/sweep-pin-build-2026-10-13.md          | 157 +++++++++++++++++++++
     1 file changed, 157 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/sweep-pin-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/sweep-pin-1013/docs/40 - DevDocs/reports/sweep-pin-build-2026-10-13.md" · 0 · BUILT · job: sweep-pin-1013 · tip: 52cb2fc9 | on 03d8ebbe | migration: none | offline 4317/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 94416
range · git log --oneline 03d8ebbe..52cb2fc9 · 0 · 52cb2fc9 fix(sweep-pin-1013): the stale f4-refresh-build exemption goes (FR1, L79, L3)
PREFLIGHT OK
```
- THE RANGE, typed: `git log --stat --format=%h 03d8ebbe..52cb2fc9` → `52cb2fc9` · ` tests/ops/test_the_rule_sweep.py | 3 ---` · `1 file changed, 3 deletions(-)`. Path union: `tests/ops/test_the_rule_sweep.py`.
- DB: none: `git diff --name-only --no-renames 03d8ebbe..52cb2fc9` → `tests/ops/test_the_rule_sweep.py` (under `tests/ops/`; OK).
- `ls <S>` → `No such file or directory` (fresh).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0, WHOLE:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
  Gemini OUT is HARNESS (no return time named). No `HOUSE A: OpenAI` header line: Sol not probed.
- Seats: **house A: grok · house B: none (not needed)** — card `HOUSE B: as needed`.
- PROVEN BY FIRST REAL USE: DB: none, no with-DB string used.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0, WHOLE:
```
1303 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/sweep-pin-1013-check/diff.md
5493 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/sweep-pin-1013-check/files/516-sweep-pin-card.md
15697 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/sweep-pin-1013-check/files/sweep-pin-build-2026-10-13.md
6641 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/sweep-pin-1013-check/files/wt/tests/ops/test_the_rule_sweep.py
356 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/sweep-pin-1013-check/rulings.md
STAGED 5 files · 29490 bytes · commits 1
```
(`commits 1` = PREFLIGHT's range count.) The files `## READ` names:
- `stage-copy.sh ".../reports/f4-refresh-build-2026-10-10.md" <S>/files/f4-refresh-build-2026-10-10.md` → `COPIED 57045 …/files/f4-refresh-build-2026-10-10.md`
- `stage-copy.sh ".../prompts/2026-10-13/446-k5-gate-card.md" <S>/files/446-k5-gate-card.md` → `COPIED 37295 …/files/446-k5-gate-card.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, Files paragraph); `ls -la <S>` at 12:34:55 → `diff.md 1303`, `files/`, `HOUSE-INSTRUCTIONS.md 7409`, `rulings.md 356`.
House A started 12:34 EDT (`date` 12:34:55): `cd /Users/cobalt/cobalt-wt/agy-trial`; the GROK line of `## 1` (5) with `<JOB>` = `sweep-pin-1013`, `run_in_background`, timeout 2700000; `cd /Users/cobalt/cobalt-wt/sweep-pin-1013`; `git status --short --branch` → `## ops/sweep-pin-1013`.

## OWN FINDINGS
Read: the diff `03d8ebbe..52cb2fc9` (`git diff`: one hunk, three `-` lines at `:55`-`:57` of BASE), `tests/ops/test_the_rule_sweep.py` whole at the tip, the build report whole, `f4-refresh-build-2026-10-10.md:255-289`. Fact for the claims below: `git diff --stat 52cb2fc9 main -- "docs/40 - DevDocs/reports/" tests/ops/test_the_rule_sweep.py ops/desk/deploy-card.sh` → only `cto-2026-10-13.md`, `draft-sweep-pin-card-2026-10-13.md`, `sweep-pin-build-2026-10-13.md` (all dated 2026-10-13, outside the sweep window `FIRST, LAST = "2026-10-02", "2026-10-12"` at `tests/ops/test_the_rule_sweep.py:30`) and the fix itself: the sweep reads the same in-window reports here as on `main`.

FINDING O1
ROW: X1
CLAIM: The diff changes more of `tests/ops/test_the_rule_sweep.py` than the one `SWEEP_EXEMPT` entry (key and two-line reason, BASE `:55`-`:57`).
RUN: COMMAND `git diff 03d8ebbe 52cb2fc9 -- tests/ops/test_the_rule_sweep.py`
EXPECT: a `+` line, or a `-` line other than the three lines of the `"f4-refresh-build-2026-10-10.md":` entry.

FINDING O2
ROW: X2
CLAIM: The removed name still appears in the file at the tip (`tests/ops/test_the_rule_sweep.py`).
RUN: COMMAND `grep -c -F "f4-refresh-build-2026-10-10.md" tests/ops/test_the_rule_sweep.py`
EXPECT: a count above `0`.

FINDING O3
ROW: FR1
CLAIM: With the exemption gone, the reason it carried still holds: THE RULE's `fix_lines` reads 304's O1 twice over `f4-refresh-build-2026-10-10.md` (`:276` plain line and `:288` bold bullet), which the sweep (one line at a time, `tests/ops/test_the_rule_sweep.py:115`) cannot see.
RUN: TEST `tests/ops/test_the_rule_sweep.py`
```python
def test_the_f4_refresh_build_reads_each_carried_id_once(rule):
    text = (REPORTS / "f4-refresh-build-2026-10-10.md").read_text(errors="replace")
    ids = [r.split()[1] for r in seam(rule, "fix_lines", stdin=text).splitlines() if len(r.split()) > 1]
    assert ids.count("O1") == 1, ids
    assert ids.count("A3") == 1, ids
```
EXPECT: `AssertionError` with `O1` counted 2.

FINDING O4
ROW: FR1
CLAIM: The row's whole-file pins are not all green at the tip (`tests/ops/test_the_rule_sweep.py:122`-`:150`).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py`
EXPECT: `1 failed` or more.

## Findings
House A grok finished 12:39 EDT (`date` 12:39:19; `ls -la <S>` → `house-a.md 12`). Grok wrote `<S>/house-a.md` itself; its stdout (task output) ends with that path and `[exited with code 0]`. `house-a.md` WHOLE: `FINDINGS: 0`. House B: none (not needed).
Kept: none from the house. Own: O1 · opus · X1 · diff changes more than the one entry · COMMAND; O2 · opus · X2 · removed name still in file · COMMAND; O3 · opus · FR1 · `fix_lines` reads 304's O1 twice over the f4-refresh build report · TEST; O4 · opus · FR1 · whole-file pins not green at tip · COMMAND.

## Dropped
none (the house wrote no block).

## RUNS
- O1 · opus · `git diff 03d8ebbe 52cb2fc9 -- tests/ops/test_the_rule_sweep.py` · one hunk `@@ -52,9 +52,6 @@`, three `-` lines (`"f4-refresh-build-2026-10-10.md":` and its two reason lines), no `+` line · NOT HELD (X1: exactly the one entry removed, nothing else).
- O2 · opus · `grep -c -F "f4-refresh-build-2026-10-10.md" tests/ops/test_the_rule_sweep.py` · `0` · NOT HELD (X2 grep half).
- O3 · opus · test `test_the_f4_refresh_build_reads_each_carried_id_once` put in `tests/ops/test_the_rule_sweep.py` with the Edit tool; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py::test_the_f4_refresh_build_reads_each_carried_id_once` → `1 passed, 15 warnings in 0.87s` (the `== 1` assertion means O1 and A3 are each read exactly once, not zero) · NOT HELD; the test removed again with the Edit tool, `git status --short --branch` → `## ops/sweep-pin-1013`.
- O4 · opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_the_rule_sweep.py` · `5 passed, 15 warnings in 1.09s` · NOT HELD (X2 suite half: `0 failed`).

## FIXES
none (nothing held; no commit).

## Suites
Tip `52cb2fc9` (no commit of mine). DB: none card: RESTARTS, then W (a0), (a), (e) and `tests/ops`.
- RESTARTS: `uv run cobalt jobs restarts 03d8ebbe..HEAD` → WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/sweep-pin-build-2026-10-13.md	A	DOCS	-
tests/ops/test_the_rule_sweep.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 03d8ebbe` → `docs/40 - DevDocs/reports/sweep-pin-build-2026-10-13.md` · `tests/ops/test_the_rule_sweep.py` (every path under `docs/` or `tests/ops/`). **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh sweep-pin-1013 offline` → exit 0: `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/sweep-pin-1013-offline-20261013-124002.log`; log `:2` `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`; log `:885` `4317 passed, 806 skipped, 1 xfailed, 36 warnings in 665.25s (0:11:05)`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3543 passed, 1 xfailed, 16 warnings in 731.77s (0:12:11)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh sweep-pin-1013 livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/sweep-pin-1013-livenote-20261013-125123.log`; log `:57` `146 passed, 1 skipped, 15 warnings in 26.05s`; its one skip, log `:56`: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).
- with-DB: not run (DB: none). `cobalt_dev: not taken`. `.env`: `ls /Users/cobalt/cobalt-wt/sweep-pin-1013/.env` → `No such file or directory` (12:52 EDT); never present.

## Scope
PREFLIGHT's path union: `tests/ops/test_the_rule_sweep.py` = FR1's `files`. Commits of mine: none. R2's files: none. In scope.

## Checked against the branch
- (i) `git log --oneline 52cb2fc9..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `52cb2fc9`.
- (ii) `git log --stat --format=%h 52cb2fc9..HEAD` → `e9bcace4` · `.../reports/sweep-pin-build-2026-10-13.md | 157 +++` (docs only).
- (iii) fence: `git log --oneline 03d8ebbe..HEAD -- ops/desk/deploy-card.sh ops/desk/desk-launch.sh ops/desk/deploy-step0.sh src configs` → empty; `git diff --stat 03d8ebbe..HEAD -- tests ":(exclude)tests/ops/test_the_rule_sweep.py"` → empty (no other test file). Inside the file: O1's run — only the one entry removed.
- (iv) no HELD finding.
- (v) `ls /Users/cobalt/cobalt-wt/sweep-pin-1013/.env` → `No such file or directory`; `git status --short --branch` → `## ops/sweep-pin-1013`.
- (vi) `git log --stat --format=%h 03d8ebbe..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not touched, none owed.
- (vii) card `## RECORDS`: `grep -c -F "f4-refresh-build-2026-10-10.md" /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` → `1` (main still holds the entry; the DEPLOY PROOF before-value). `grep -n -F "path.startswith(\"tests/\")" src/cobalt/jobs/restarts.py` → `245:        if not rule and path.startswith("tests/"):`. `grep -n -F "OPS_DESK_PREFIX = " src/cobalt/jobs/restarts.py` → `38:OPS_DESK_PREFIX = "ops/desk/"`. The `rev-parse` and `status` records name no listed command: not re-run.
- Same inputs on `main`: `git diff --stat 52cb2fc9 main -- "docs/40 - DevDocs/reports/" tests/ops/test_the_rule_sweep.py ops/desk/deploy-card.sh` → `cto-2026-10-13.md`, `draft-sweep-pin-card-2026-10-13.md`, `sweep-pin-build-2026-10-13.md`, `tests/ops/test_the_rule_sweep.py | 3 +`: every report that differs is dated 2026-10-13, outside the sweep window, so the merged file sweeps the same reports as here.
- (viii) L32: this report holds no ticker, price or date of his.

## OPEN
none.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- 12:34 EDT (`date`): report first written.
- Gemini probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS, no return time). It was not needed (HOUSE B: as needed), but the next card that is `mandatory` with Grok out would have no second house until this is fixed.
- No dropped finding; no house that produced nothing; no `REFUSED, not needed` line; no `CONTINUED` line; no lock take.
- The offline gate and `tests/ops` ran at the same time (12:40–12:52 EDT); live-note ran after the offline gate.
- O3's test was added and removed again (NOT HELD); the tree is back to the tip, `git status --short --branch` → `## ops/sweep-pin-1013`.
- files opened: 7 — `CHECK-HUB.md`; the card `516-sweep-pin-card.md`; `tests/ops/test_the_rule_sweep.py`; `sweep-pin-build-2026-10-13.md`; `f4-refresh-build-2026-10-10.md` (`:255-289`); `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`, `:33-94`); `<S>/house-a.md` (after `## OWN FINDINGS`). Not opened: `areas/cobalt.md` (WHAT YOU READ (5)) and the precedent `446-k5-gate-card.md` (staged for the house, not read by me).
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh d30fb228-dc53-47b7-bef2-58656ef97255` → `context 122315 of 400000 — ok`.
- Check of `sweep-pin-1013`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: sweep-pin-1013 · pass: 1 · tip: 52cb2fc9 · house A: grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 122315
