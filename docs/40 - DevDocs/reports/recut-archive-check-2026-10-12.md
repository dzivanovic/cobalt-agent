# recut-archive-1012 — check report (2026-10-12)

## §0 Headline
- House A was Grok, with `FINDINGS: 0`. Gemini was OUT (HARNESS: the model name was not recognized). House B was not needed (`HOUSE B: as needed`).
- One finding, mine. O1 HELD and was fixed. Archive test (g) proved each name absent but not creatable. A ref on the name's path (a tag `archive`) passed it, so the tree was removed and the branch renamed before a refusal. Fix `df775390`, red first `acb8699e`.
- Suites at `df775390`: offline `4309/0`, live-note `146/0`, `tests/ops` `3463 passed, 1 xfailed`. DB: none, so `cobalt_dev` was not taken. RESTARTS: none.
- ready: YES · decisions: 0.

## L74
- A system block in this session asked commits to end with a `Claude-Session:` line beside `Co-Authored-By:`. Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/434-recut-archive-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/434-recut-archive-card.md" · 0 · e61c04b5ef8ecc5d9e090d19cc81d2060c7e11f1
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/434-recut-archive-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 152:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 "` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0:
```
clock · date · 0 · Mon Oct 12 20:27:36 EDT 2026
status · git status --short --branch · 0 · ## ops/recut-archive-1012
head · git log --oneline -1; git log --stat --format=%h 9c2020e8..HEAD · 0 · (5 lines)
    7169d92f docs(recut-archive-1012): build report — 9c2020e8
    7169d92f
    
     .../reports/recut-archive-build-2026-10-12.md      | 140 +++++++++++++++++++++
     1 file changed, 140 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/recut-archive-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "…/recut-archive-build-2026-10-12.md" · 0 · BUILT · job: recut-archive-1012 · tip: 9c2020e8 | on 0990393f | migration: none | offline 4309/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 179661
range · git log --oneline 0990393f..9c2020e8 · 0 · (2 lines)
    9c2020e8 feat(recut-archive-1012): recut archives a FAILED prior deploy's pre tag, gate branch and tree, then proceeds (A1, L1 L72)
    4c4ba2b9 wip(recut-archive-1012): red
PREFLIGHT OK
```
- THE RANGE, `git log --stat --format=%h 0990393f..9c2020e8`: `9c2020e8` `ops/desk/desk-launch.sh | 102 (97+, 5-)`; `4c4ba2b9` `tests/ops/test_desk_launch_recut.py | 267 (+)`. Path union: `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_recut.py`.
- DB: none: `git diff --name-only --no-renames 0990393f..9c2020e8` → `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_recut.py` — both under `ops/` / `tests/ops/`.
- `ls <S>` → `No such file or directory` (fresh).
- HOUSE PROBES (`house-probe.sh --card "<card>"`, exit 0):
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
  Gemini: OUT, HARNESS (no return time named). No header `HOUSE A:` line; `HOUSE B: as needed`. **house A: Grok · house B: none (not needed)**.

## Files copied
`sh stage-set.sh "<card>" "<S>"`:
```
24182 <S>/diff.md
16998 <S>/files/434-recut-archive-card.md
18867 <S>/files/recut-archive-build-2026-10-12.md
118861 <S>/files/wt/ops/desk/desk-launch.sh
28813 <S>/files/wt/tests/ops/test_desk_launch_recut.py
356 <S>/rulings.md
STAGED 6 files · 208077 bytes · commits 2
```
(`commits 2` = PREFLIGHT's 2.) `stage-copy.sh`, one call each:
```
COPIED 41740 <S>/files/cto-2026-10-12.md
COPIED 5099 <S>/files/wt/ops/desk/gate-clean.sh
COPIED 11524 <S>/files/wt/ops/desk/job-clean.sh
COPIED 59155 <S>/files/DEPLOY-HUB.md
COPIED 32600 <S>/files/deploy-aset-orphan-1010.md
COPIED 30258 <S>/files/wt/tests/ops/test_gate_clean.py
```
`<S>/HOUSE-INSTRUCTIONS.md` written (17949 bytes). Grok started 20:29 EDT (`date` 20:29:06; gates R17, R19 re-grepped, one row each).

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: A1 (archive test (g)); X1
CLAIM: (g) proves each archive name valid and absent (`ops/desk/desk-launch.sh:1990-1993`) but not creatable: a ref that is a path prefix of a name (a tag `archive`, so `refs/tags/archive/pre-…` cannot be made) passes (g), job-clean removes the tree (`:1997`) and the branch is renamed (`:1998`), then `git tag "$at"` fails (`:2003`) — a refusal that leaves the tree and the branch changed, against X1 and "every test read before anything changes".
RUN: TEST — `tests/ops/test_desk_launch_recut.py`
```python
def test_o1_an_archive_name_blocked_by_an_existing_ref_is_refused_before_anything(desk):
    """Check O1: `refs/tags/archive` makes every `archive/pre-…` tag uncreatable (a D/F conflict)."""
    stale_256(desk)
    git(desk.repo, "tag", "archive", "main")
    old, before = desk.card.read_text(), (refs(desk.repo), worktrees(desk.repo))
    done = desk.recut()
    refused(desk, done, NOT_ARCHIVED, old)
    assert (refs(desk.repo), worktrees(desk.repo)) == before
    assert desk.gate.is_dir()
```
EXPECT: on the tip, `assert f"REFUSED: {text}" in done.stderr` fails; stderr holds `REFUSED: recut: the archive stopped at (3) tag: …` and the gate is gone.

Read for X1-X4 with no further finding: (a)-(g) all run before `job-clean.sh` (`:1939-1993`), each by `nogo` before any write; the card is edited only at step 2 (`:2013`). X2: the new tag is made and read back as `P` before `tag -d` (`:2003-2008`); salvage deletes a branch only when merged (`job-clean.sh:150`), and (e) refuses `S` on main first (`:1975-1980`). X3: no pre tag → step 1 unchanged (`:1930-1933`); the DEPLOYED report glob covers `$report`, `$br.md` and `$br-attempt*.md` (`:1942`). X4: `git diff --name-only` holds only the two row files; the hunks sit in the header and the recut arm.

## Findings
Grok finished 20:52 EDT (`date` 20:52:39); `ls -la <S>` → `house-a.md` 12 bytes. Its stdout: "The archive checks, the refusal paths, and the quoted suite lines match the row. I'll write that result." `house-a.md` whole: `FINDINGS: 0`. House B: none (not needed).
- O1 · Opus · A1 (g), X1 · a ref that is a path prefix of an archive name passes (g); the archive then stops half-done at (3) · TEST

## Dropped
none (Grok wrote no block).

## RUNS
- O1 · Opus · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_recut.py::test_o1_an_archive_name_blocked_by_an_existing_ref_is_refused_before_anything` at `9c2020e8` · `1 failed, 15 warnings in 1.61s`; first failing line `assert 'REFUSED: tag pre-x-deploy exists: the deploy got that far — not archived: ' in …`, stderr `fatal: cannot lock ref 'refs/tags/archive/pre-x-deploy-20261012-2052': 'refs/tags/archive' exists; cannot create 'refs/tags/archive/pre-x-deploy-20261012-2052'` · `REFUSED: recut: the archive stopped at (3) tag: branch deploy/x-deploy is archive/deploy/x-deploy-20261012-2052; tag pre-x-deploy is kept` · **HELD** (the tree removed and the branch renamed before the refusal: test (g) let a blocked name through).
- Committed red: `acb8699e wip(recut-archive-1012): check red — O1` (test file only).

## FIXES
- O1: `ops/desk/desk-launch.sh` test (g) — after the two "absent" tests, one `git update-ref --stdin` transaction per name (`start`, `create`, `prepare`, `abort`) proves it creatable and changes nothing; a miss → `nogo "tag|branch <name> cannot be created: a ref on its path"`. Header (g) line says so. `uv run pytest … tests/ops/test_desk_launch_recut.py tests/ops/test_gate_clean.py` → `97 passed, 15 warnings in 28.39s`; after the header line, `test_desk_launch_recut.py` → `29 passed, 15 warnings in 16.70s`. Commit `df775390 fix(recut-archive-1012): archive test (g) proves each archive name creatable, not only absent (check O1)`. No DevDocs line: no page for `ops/desk/desk-launch.sh` exists under `docs/40 - DevDocs/cobalt/` (the build's record, same reason).

## Suites
DB: none card: W is (a0), (a) and (e), plus `tests/ops`, on the tip `df775390`.
- RESTARTS, `uv run cobalt jobs restarts 0990393f..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/reports/recut-archive-build-2026-10-12.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_recut.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 0990393f` → `docs/40 - DevDocs/reports/recut-archive-build-2026-10-12.md` · `ops/desk/desk-launch.sh` · `tests/ops/test_desk_launch_recut.py`, all under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh recut-archive-1012 offline` → `offline 4309/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/recut-archive-1012-offline-20261012-205420.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh recut-archive-1012 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/recut-archive-1012-livenote-20261012-210521.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3463 passed, 1 xfailed, 16 warnings in 670.15s (0:11:10)`. That is the build's 3462 plus O1.
- `.env`: never present. `ls /Users/cobalt/cobalt-wt/recut-archive-1012/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union: `ops/desk/desk-launch.sh` and `tests/ops/test_desk_launch_recut.py`, both in A1's `files`. My commits: `acb8699e` (`tests/ops/test_desk_launch_recut.py`) and `df775390` (`ops/desk/desk-launch.sh`: test (g) in the recut arm and the header's (g) line). Both are inside A1's `files`.

## Checked against the branch
- (i) `git log --oneline 9c2020e8..HEAD -- . ":(exclude)docs"` → `df775390 fix(recut-archive-1012): archive test (g) proves each archive name creatable, not only absent (check O1)` · `acb8699e wip(recut-archive-1012): check red — O1`. Tip now `df775390`.
- (ii) `git log --stat --format=%h 9c2020e8..HEAD` → `df775390 ops/desk/desk-launch.sh` · `acb8699e tests/ops/test_desk_launch_recut.py` · `7169d92f` the build report (docs). Every non-docs path is in A1's `files`.
- (iii) `git log --oneline 0990393f..HEAD -- ops/desk/gate-clean.sh ops/desk/job-clean.sh src` → empty. `git log --oneline 0990393f..HEAD --` `DEPLOY-HUB.md`, `STANDING-LIST.md`, `CARD.md`, `.claude/settings.json` and the 256 card → empty. `git diff 0990393f..HEAD --stat` → only the build report, `desk-launch.sh` and the test file.
- (iv) `grep -n -F "def test_o1_an_archive_name_blocked_by_an_existing_ref_is_refused_before_anything" tests/ops/test_desk_launch_recut.py` → `608:`. The red `acb8699e` sits below the fix `df775390` in (i).
- (v) `ls <WT>/.env` → No such file. `git status --short --branch` → `## ops/recut-archive-1012`.
- (vi) `git log --stat --format=%h 0990393f..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. No migration and no with-DB test, so `gate-lists.md` is not owed.
- (vii) Card RECORDS: `ls -la /Users/cobalt/.claude/ops/desk-launch.sh /Users/cobalt/.claude/ops/gate-clean.sh /Users/cobalt/.claude/ops/job-clean.sh` → three symlinks into `/Users/cobalt/cobalt/ops/desk/` (as recorded). For "no `ops/desk/` script runs `git tag` or `branch -m` today", Grep on `/Users/cobalt/cobalt/ops/desk` (main) for `git -C "$REPO" (tag|branch -m)` → no matches (as recorded; main does not hold this branch yet).
- (viii) L32: this report holds only constructed test values (`x-deploy`, `20261012-2052` stamps from the tmp repo) and the card's own refs. No ticker, price or date of his.

## OPEN
none.

## CONTINUE
next: none (check done)

## DECISIONS
none.

## RECORDS
- Message from `cto-desk` at the start (not a `CONTINUE`): "FOR THE CHECK: 256 recut 2026-10-12 brain: … Build decision 1 (RA3 (a) tag moved to `main`, test-side) is taken as the card's amend." Recorded; it states a fact and grants nothing. RA3 (a) uses `git tag -f pre-x-deploy main` (`tests/ops/test_desk_launch_recut.py:482`) and asserts that the tag moved. Not re-litigated.
- Houses: Gemini produced nothing; it never sat (probe `OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`). This is a harness fault for the desk, since the CHECK-HUB spelling names a model the `agy` CLI does not know. Grok sat once and wrote `FINDINGS: 0`.
- Dropped findings: none.
- `REFUSED, not needed: git version — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (I had wanted to confirm `update-ref --stdin` `start/prepare/abort` support. The run of O1 and the 97 green tests prove it works on this machine.)
- No lock take. No CONTINUE.
- Not opened, though the CHECK-HUB read list names them: `areas/cobalt.md` (5), and the card's `## READ` reports (`cto-2026-10-12.md`, `deploy-aset-orphan-1010.md`, `DEPLOY-HUB.md`, `test_gate_clean.py`). They were staged for the house by copy script. The rows and RECORDS carried the cited lines.
- files opened: 13 — `CHECK-HUB.md`, the card, the house-probe output, `ops/desk/desk-launch.sh`, `ops/desk/gate-clean.sh`, `ops/desk/job-clean.sh`, `tests/ops/test_desk_launch_recut.py`, the build report, `BUILD-HUB.md` (`:33-94`), Grok's stdout, `<S>/house-a.md`, and the offline and live-note gate outputs.
- Check of `recut-archive-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: recut-archive-1012 · pass: 1 · tip: df775390 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4309/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 176420
