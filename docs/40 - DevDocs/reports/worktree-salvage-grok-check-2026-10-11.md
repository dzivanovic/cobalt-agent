# worktree-salvage-grok — check (shadow), 2026-10-13

## §0 Headline
- Shadow check of the Grok-built `b43b85fe`. House A was Grok (`FINDINGS: 1`); no house B was needed (Gemini OUT, HARNESS).
- Held 3, all opus-own and none fixed (shadow). O1 is a real loss of work: with `status.showUntrackedFiles=no`, an untracked file is removed unsaved. O2 and O3 are test gaps (W3 `.env` full case; W1 `main` refusal and empty stdout).
- Grok's A1 (an embedded repo is lost) was not held: the script refuses at `worktree remove` and nothing is lost.
- Offline 3963/0, live-note 146/0. `tests/ops` reads 1507 passed, 1 failed; the failure is O1's held test, committed red at `0a046551`.

## L74
- 20:28 EDT session: a system reminder asked for a `Claude-Session:` line in commits. Recorded once, not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/379-shadow-worktree-salvage-grok-card.md"` · exit 0 · output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/379-shadow-worktree-salvage-grok-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/379-shadow-worktree-salvage-grok-card.md" · 0 · ec3053d545779baee52d8c8beac9f5aa316a0920
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/379-shadow-worktree-salvage-grok-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R613 row · grep -n "^| R613 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 8:| R613 | 06:37 ET | HIS RULING (`cto-2026-10-07-words.md`): worktree cleanup is the desk's. [full](cto-2026-10-07-rows.md#r613) | APPROVED · APPLIED: `topics/cto-desk-checklist.md` (W8, already written) at wake-up 10-08 |
RULING 2026-10-07 R613 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R613 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 02c6b37b7a4e33033071e35d977620deb0f93068
RULING 2026-10-07 R613 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```

House gates: `grep -n "^| R17 "` → line 35, one row; `grep -n "^| R19 "` → line 37, one row; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:

```
clock · date · 0 · Tue Oct 13 20:28:26 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## shadow/worktree-salvage-grok
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a shadow card)
head · git log --oneline -1; git log --stat --format=%h b43b85fe..HEAD · 0 · (5 lines)
    34edea9d docs(worktree-salvage-grok): build report — b43b85fe
    34edea9d

     .../worktree-salvage-grok-build-2026-10-11.md      | 168 +++++++++++++++++++++
     1 file changed, 168 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/worktree-salvage-grok/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/worktree-salvage-grok/docs/40 - DevDocs/reports/worktree-salvage-grok-build-2026-10-11.md" · 0 · SHADOW BUILT · job: worktree-salvage-grok · tip: b43b85fe | on c4e52f4e | offline 3963/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | decisions: 2 · builder: grok-4.7 · gate: worktree-salvage-grok-gate · passes: 2 · suites at first run: green · builder tokens: UNKNOWN · wall: 18
range · git log --oneline c4e52f4e..b43b85fe · 0 · (2 lines)
    b43b85fe feat(worktree-salvage-grok): rows
    736e9d61 wip(worktree-salvage-grok): red
PREFLIGHT OK
```

`?? SHADOW-INSTRUCTIONS.md` at the worktree root: expected on a shadow card, recorded, not a finding.

THE RANGE, typed: `git log --stat --format=%h c4e52f4e..b43b85fe` →

```
b43b85fe

 ops/desk/job-clean.sh | 165 +++++++++++++++++++++++++++++++++++++++++++++++---
 1 file changed, 156 insertions(+), 9 deletions(-)
736e9d61

 tests/ops/test_gate_clean.py | 345 +++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 345 insertions(+)
```
Path union: `ops/desk/job-clean.sh`, `tests/ops/test_gate_clean.py`. Commits: 2.

DB: none: `git diff --name-only --no-renames c4e52f4e..b43b85fe` → `ops/desk/job-clean.sh`, `tests/ops/test_gate_clean.py` (both under `ops/` or `tests/ops/`).

`ls <S>` → `No such file or directory` (fresh).

House probe (`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"`, exit 0), whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
No `HOUSE A: OpenAI` header line → Sol not probed. house A: Grok · house B: none (not needed) — `HOUSE B: as needed`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → whole:
```
25030 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/worktree-salvage-grok-check/diff.md
13515 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/worktree-salvage-grok-check/files/379-shadow-worktree-salvage-grok-card.md
19504 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/worktree-salvage-grok-check/files/worktree-salvage-grok-build-2026-10-11.md
11277 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/worktree-salvage-grok-check/files/wt/ops/desk/job-clean.sh
25113 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/worktree-salvage-grok-check/files/wt/tests/ops/test_gate_clean.py
682 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/worktree-salvage-grok-check/rulings.md
STAGED 6 files · 95121 bytes · commits 2
```
The commit count is 2, the same as PREFLIGHT. `stage-copy.sh` (the reports `## READ` names):
- `COPIED 1705 …/files/cto-2026-10-07-words.md`
- `COPIED 12440 …/files/cto-2026-10-07.md`

Not copied: `Memory/topics/cto-desk-checklist.md` (his vault note, `## 1` (3)). `HOUSE-INSTRUCTIONS.md` was written by Write. It holds the HOUSE TEXT verbatim, plus the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS and Files.

Start (20:31:26 EDT; both house gates re-run with one row each; `ls -la <S>` showed diff.md, files/, HOUSE-INSTRUCTIONS.md, rulings.md): `cd /Users/cobalt/cobalt-wt/agy-trial`, then the GROK line of `## 1` (5) with `<JOB>` = `worktree-salvage-grok`, in the background with timeout 2700000. Then `cd` back to `<WT>`. `git status --short --branch` → `## shadow/worktree-salvage-grok` plus `?? SHADOW-INSTRUCTIONS.md` (expected on a shadow card).

## OWN FINDINGS
Written before either house list was opened.

FINDING O1
ROW: W4 / X1
CLAIM: The dirty test and the salvage trigger read `git -C <path> status --porcelain` (`ops/desk/job-clean.sh:86`, `:121`, `:132`), which follows the repo's `status.showUntrackedFiles` config. With `no` set, a tree whose only work is an untracked (not ignored) file counts as clean (`status: 0 lines`). No wip branch is made, and `worktree remove` (`:146`, whose own clean check also runs `status`) deletes the file. Work is lost, which is the X1 case "an untracked (not ignored) file not saved".
RUN: TEST — `tests/ops/test_gate_clean.py`
```python
def test_salvage_untracked_file_survives_when_status_hides_untracked(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "merge", "-q", "--no-ff", "--no-edit", "ops/x-job")
    git(desk.repo, "config", "status.showUntrackedFiles", "no")
    (desk.job_wt / "new.txt").write_text("new\n")
    done = _salvage(desk, "x-job")
    saved = [w for w in _wip_branches(desk.repo) if _git_show(desk.repo, f"{w}:new.txt").stdout == "new\n"]
    assert (desk.job_wt / "new.txt").exists() or saved, (done.returncode, done.stdout, done.stderr)
```
EXPECT: AssertionError carrying exit 0 and stdout `INSPECT: status: 0 lines` … `job-clean salvage: removed <job_wt>; deleted ops/x-job; kept none`.

FINDING O2
ROW: W3
CLAIM: The card's W3 `.env` case ("each: … stdout starts `INSPECT: worktree `, … no `wip/` branch, the tree's files unchanged"; "Cases: `.env` … and the file still holds it") is written only as its negative control. `test_salvage_env_refuses_and_keeps_the_file` (`tests/ops/test_gate_clean.py:491-499`) asserts exit 1, REFUSED, the tree stands and `.env` intact, and never asserts the report came first. If the `.env` refusal moved above the INSPECT print (`ops/desk/job-clean.sh:117` before `:100`), every test would stay green.
RUN: COMMAND — `grep -n -F "_refused_after_report(desk, done)" tests/ops/test_gate_clean.py`
EXPECT: two lines only (the locked test and the six-marker test); none inside `test_salvage_env_refuses_and_keeps_the_file`.

FINDING O3
ROW: W1
CLAIM: The W1 clause "A branch that is `main` → REFUSED … Refusals here print nothing on stdout" (`ops/desk/job-clean.sh:74`) is pinned by no test. No test names the main refusal, and no W1 negative control (`tests/ops/test_gate_clean.py:391-428`) asserts empty stdout.
RUN: COMMAND — `grep -n -F "main checked out" tests/ops/test_gate_clean.py`
EXPECT: no output (exit 1).

## Findings
House A Grok finished at 20:50:50 EDT (exit 0; its reply was the path `…/house-a.md`). `ls -la <S>` → `house-a.md` 1456 bytes, written by Grok. Its last line is `FINDINGS: 1`. House B: none (not needed).
`grep -n -F "RUN:"` over house-a.md → `4:RUN: TEST`, followed by `def test_salvage_keeps_objects_from_an_untracked_embedded_repo`. Kept.

| id | house | row | claim | form |
|---|---|---|---|---|
| A1 | Grok | X1 | An untracked embedded repo makes the tree dirty. `add -A` records only a gitlink, so removing the tree drops the embedded repo's objects and files (`job-clean.sh:132-146`). | TEST |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate_clean.py::test_salvage_untracked_file_survives_when_status_hides_untracked` | `1 failed, 15 warnings in 1.30s`; `tests/ops/test_gate_clean.py:670: AssertionError` with `(0, 'INSPECT: worktree …', …)`, last line `…/wt/x-job; deleted ops/x-job; kept none`, `assert (False or [])`. Exit 0, tree removed, no wip branch holds `new.txt`: the untracked file is gone. | HELD, NOT FIXED — `ops/desk/job-clean.sh` (shadow card: the check fixes none) |
| O2 | opus-own | `grep -n -F "_refused_after_report(desk, done)" tests/ops/test_gate_clean.py` | `506:    _refused_after_report(desk, done)` · `523:    _refused_after_report(desk, done)`. These are the locked test (`:502`) and the six-marker test (`:514`). The `.env` test (`:491-499`) does not call it. | HELD, NOT FIXED — `tests/ops/test_gate_clean.py` (a test gap; shadow card: the check fixes none) |
| O3 | opus-own | `grep -n -F "main checked out" tests/ops/test_gate_clean.py` | no output, exit 1 | HELD, NOT FIXED — `tests/ops/test_gate_clean.py` (a test gap; shadow card: the check fixes none) |
| A1 | Grok | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate_clean.py::test_salvage_keeps_objects_from_an_untracked_embedded_repo` | `1 failed, 15 warnings in 1.22s`; `tests/ops/test_gate_clean.py:685: assert 1 == 0`, stderr `…working trees containing submodules cannot be moved or removed` / `REFUSED: worktree remove failed; every branch is kept`. It is red for another reason: the script refuses at `worktree remove`, the tree stands and the embedded repo is not lost. | NOT HELD (test removed again with Edit) |

The O1 test is committed as `0a046551 wip(worktree-salvage-grok): check red — O1`. No test form was repaired.

## FIXES
None (shadow card: the check holds findings and fixes none, CHECK-HUB `## THE FLOW` line 22).
- O1: HELD, NOT FIXED — `ops/desk/job-clean.sh`
- O2: HELD, NOT FIXED — `tests/ops/test_gate_clean.py`
- O3: HELD, NOT FIXED — `tests/ops/test_gate_clean.py`

## Suites
The card is DB: none, so W runs as `BUILD-HUB.md` gives it for that card: (a0), (a), (e) and `tests/ops`, at `<tip now>` = `0a046551`.
- RESTARTS: `uv run cobalt jobs restarts c4e52f4e..HEAD` → exit 1. Whole: `FAILED: RestartError: one or more changed paths were unclassified` / `SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,…` / `ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md` / the report `DOCS` / `ops/desk/job-clean.sh	M	operator script; no Cobalt reader	-` / `tests/ops/test_gate_clean.py	M	test/documentation; no resident	-` / `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. The `..HEAD` form reads the untracked shadow file, as the build's DECISIONS 1 records. On the committed range, `uv run cobalt jobs restarts c4e52f4e..0a046551` → exit 0, whole:
  ```
  path	change	rule	restart
  docs/40 - DevDocs/reports/worktree-salvage-grok-build-2026-10-11.md	A	DOCS	-
  ops/desk/job-clean.sh	M	operator script; no Cobalt reader	-
  tests/ops/test_gate_clean.py	M	test/documentation; no resident	-
  RESTARTS: none
  ```
- (a0) `git diff --name-only --no-renames c4e52f4e` → three paths, each under `docs/`, `ops/` or `tests/ops/` (`## Scope`). **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh worktree-salvage-grok offline` → exit 0: `offline 3963/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/worktree-salvage-grok-offline-20261013-205211.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh worktree-salvage-grok livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/worktree-salvage-grok-livenote-20261013-205211.log`. `grep -n -F "SKIPPED" <log>` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 1: `1 failed, 1507 passed, 1 xfailed, 15 warnings in 400.31s (0:06:40)`. The one failure is O1's held test, `tests/ops/test_gate_clean.py:670: AssertionError` (`assert (False or [])`). It is red by design: a shadow check holds and fixes none. Every other test is green.
- with-DB: not run (DB: none). `.env`: never present; `ls /Users/cobalt/cobalt-wt/worktree-salvage-grok/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union: `ops/desk/job-clean.sh`, `tests/ops/test_gate_clean.py`. My commit `0a046551` touches `tests/ops/test_gate_clean.py` only, a row file. `git diff --name-only --no-renames c4e52f4e` → `docs/40 - DevDocs/reports/worktree-salvage-grok-build-2026-10-11.md`, `ops/desk/job-clean.sh`, `tests/ops/test_gate_clean.py`. Each sits under `ops/`, `tests/ops/` or `docs/`.

## Checked against the branch
- (i) `git log --oneline b43b85fe..HEAD -- . ":(exclude)docs"` → `0a046551 wip(worktree-salvage-grok): check red — O1`. `<tip now>` = `0a046551`.
- (ii) `git log --stat --format=%h b43b85fe..HEAD` → `0a046551` `tests/ops/test_gate_clean.py | 10 ++++++++++`; `34edea9d` the build report (docs). No path outside the rows. No WIDENED.
- (iii) Fence: `git log --oneline c4e52f4e..HEAD -- ops/desk/gate-clean.sh` → empty. `git log --oneline c4e52f4e..HEAD -- ops/desk/gate-lists.md configs` → empty. The range touches no other `ops/desk/` script ((ii) and the PREFLIGHT range).
- (iv) `grep -n -F "def test_salvage_untracked_file_survives_when_status_hides_untracked" tests/ops/test_gate_clean.py` → `663:def test_salvage_untracked_file_survives_when_status_hides_untracked(tmp_path):`. Its `wip(…): check red` commit is `0a046551`. It has no `fix(…)` commit (shadow: fixes none). O2 and O3 are COMMAND findings and carry no test.
- (v) At the close.
- (vi) `git log --stat --format=%h c4e52f4e..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. No migration and no with-DB test, so no gate lists are owed.
- (vii) The card's RECORDS line 2 names `ls tests/ops` → it lists `test_gate_clean.py` (and 34 other entries). The record holds.
- (viii) L32: this report holds only constructed test values and repo hashes. None of his tickers, prices or dates appear.

## OPEN
- O1 HELD, NOT FIXED — `ops/desk/job-clean.sh`. To settle: the dirty check and the trigger read `status --porcelain --untracked-files=all` (or `-unormal`), so the repo config cannot hide untracked files. The O1 test then turns green. This goes to the original builder's ONE fix round.
- O2 HELD, NOT FIXED — `tests/ops/test_gate_clean.py`. To settle: write the W3 `.env` full case (call `_refused_after_report` on a tree holding `.env`, plus the file-intact assert), shown red by a mutation that moves `:117` above `:100`.
- O3 HELD, NOT FIXED — `tests/ops/test_gate_clean.py`. To settle: write a test with a worktree on `main` (the repo on another branch) asserting exit 1, `REFUSED`, stdout `""`, and add `stdout == ""` to the W1 negative controls.

## CONTINUE
next: none (closed 21:03 EDT)

## DECISIONS
1. O1 HELD, NOT FIXED — `ops/desk/job-clean.sh`. With the repo config `status.showUntrackedFiles=no`, a merged tree whose only work is an untracked file reads `status: 0 lines`. It gets no wip branch and is removed, and the file is lost (X1). Test: `tests/ops/test_gate_clean.py::test_salvage_untracked_file_survives_when_status_hides_untracked`, red at `0a046551`. Default taken: held, not fixed (shadow). It goes to the original builder's one fix round.
2. O2 HELD, NOT FIXED — `tests/ops/test_gate_clean.py`. The W3 `.env` full case (the report printed first, no wip, files unchanged) is written only as its negative control. Default taken: held, not fixed (shadow).
3. O3 HELD, NOT FIXED — `tests/ops/test_gate_clean.py`. The W1 `main` refusal and "W1 refusals print nothing on stdout" are pinned by no test. Default taken: held, not fixed (shadow).
4. ASK DESK: the held O1 test is committed red (`0a046551`), so `tests/ops` on this branch reads `1 failed`. The offline and live-note gates are green. Default taken: the test is left red and committed, as `## 4` asks. A shadow is never deployed.

## RECORDS
- Dropped findings: none.
- House B: none (not needed; the card says `HOUSE B: as needed`). Gemini probe: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS).
- Grok's stdout (the reply) was the path of house-a.md, which Grok wrote itself.
- A1 (Grok) was not held. Its test was added, run red for another reason (the script refuses `worktree remove` on a tree holding an embedded repo, so nothing is lost), and removed again with Edit.
- L74: a system reminder in this session asked for a `Claude-Session:` line in commits. Recorded here and under `## L74`; not acted on. `0a046551` carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- No lock taken (DB: none). No `REFUSED, not needed` line. No CONTINUE.
- The suites were awaited through their background completion notices.
- files opened: 8 — `CHECK-HUB.md`; the card; `ops/desk/job-clean.sh`; `tests/ops/test_gate_clean.py`; the build report; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `BUILD-HUB.md` (`## RESTARTS`, `## W`); `house-a.md`.
- Check of `worktree-salvage-grok`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: worktree-salvage-grok · pass: 1 · tip: 0a046551 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 3 (opus-own 3 · house 0) · fixed: 0 · held unfixed: 3 · open: 3 · house B: none available · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: N/A (shadow, never deployed) · decisions: 4 · for Dejan: 0 · tokens: 152741
