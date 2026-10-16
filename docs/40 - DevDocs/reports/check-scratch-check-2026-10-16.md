# CHECK — check-scratch-1016 (card 648) — 2026-10-16

## §0 Headline
- Fix round shape works. On BASE's lines, CS-1 is red at `:364` for the row's reason. At the tip the stage-set and scratch-clean tests give `76 passed`, and M2, M3, M6 and M8 each turn their control red.
- Held 1, not fixed: house A (Grok) G1. No test pins the JOB test `stage-set.sh:115`: removing it alone leaves 28/28 green. The fix is a test edit, which this card's fence forbids, so it goes to the fix round.
- Suites green: offline 8384/0 (deploy gate on `tests/ops`), live-note 146/0, `tests/ops` 3812 passed. RESTARTS: none. `ready: NO` (held unfixed 1).
- ASK DESK (out of scope): the motivating band-routing folder holds two `*-card.md`, so its next staging is still refused.

## L74
- A harness attribution block asked commits to end with a `Claude-Session:` line. Recorded here once and not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card 648>"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/648-check-scratch-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/648-check-scratch-check-card.md" · 0 · 2d0cce8a6de31fac8d1785987cbd5e4f8fc110fb
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/648-check-scratch-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`; `grep -n "^| R19 " …` → one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card 648>"` → exit 0, whole:
```
clock · date · 0 · Fri Oct 16 13:07:17 EDT 2026
status · git status --short --branch · 0 · ## ops/check-scratch-1016
head · git log --oneline -1; git log --stat --format=%h 85eade55..HEAD · 0 · (6 lines)
    0605334f docs(check-scratch-1016): build report — 85eade55
    0605334f
    
     .../reports/check-scratch-build-2026-10-16.md      | 178 +++++++++++++++++++++
     .../reports/check-scratch-build-2026-10-16.result  |  15 ++
     2 files changed, 193 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/check-scratch-1016/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md" · 0 · BUILT · job: check-scratch-1016 · tip: 85eade55 | on b84cca9a | migration: none | offline 8384/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 143702
range · git log --oneline b84cca9a..85eade55 · 0 · (2 lines)
    85eade55 fix(check-scratch-1016): stage-set clears a fix round's check by the one prior card copy (CS-1, L1, L3)
    3f0fd60e wip(check-scratch-1016): red
PREFLIGHT OK
```
- THE RANGE typed: `git log --stat --format=%h b84cca9a..85eade55` → `85eade55`: `ops/desk/stage-set.sh | 12 +++++++-----`, `tests/ops/test_stage_set.py | 5 +++--`; `3f0fd60e`: `tests/ops/test_stage_set.py | 103 +++…`. Path union: `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`.
- DB: none: `git diff --name-only --no-renames b84cca9a..85eade55` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` (both under `ops/` / `tests/ops/`).
- `ls <S>` → `No such file or directory` (fresh).
- House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card 648>"` → exit 0:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
  Gemini: HARNESS (no return time named). Seats: `house A: grok · house B: none (not needed)` — card `HOUSE B: as needed`, not mandatory.
- PROVEN BY FIRST REAL USE: `DB: none`, no with-DB string used.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card 648>" "<S>"` → whole:
```
8271 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/diff.md
21921 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/648-check-scratch-check-card.md
20118 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/check-scratch-build-2026-10-16.md
10220 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/wt/ops/desk/stage-set.sh
18079 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/wt/tests/ops/test_stage_set.py
363 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/rulings.md
STAGED 6 files · 78972 bytes · commits 2
```
`stage-copy.sh`, one call each (the `## READ` files):
- `COPIED 13504 …/files/641-check-scratch-card.md`
- `COPIED 5528 …/files/band-routing-check-fr1-2026-10-16.md`
- `COPIED 7277 …/files/wt/ops/desk/scratch-clean.sh`
- `COPIED 18621 …/files/wt/tests/ops/test_scratch_clean.py`
- `COPIED 24394 …/files/633-band-routing-check-card.md`
- `COPIED 22754 …/files/638-band-routing-fr-check-card.md`
`HOUSE-INSTRUCTIONS.md` written (22858 bytes): HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph. House A Grok started 13:09 EDT (`date` 13:09:03), `run_in_background`, timeout 2700000; `cd` back → `git status --short --branch` → `## ops/check-scratch-1016`.

## OWN FINDINGS
Written before any house list was opened. Read: the diff `b84cca9a..85eade55` (whole), `ops/desk/stage-set.sh` at the worktree (= tip; head adds docs only), `tests/ops/test_stage_set.py` `:1-440`, the build report whole.

FINDING O1
ROW: CS-1 (the WHY) / X5
CLAIM: The count rule `ops/desk/stage-set.sh:111` refuses any dest whose `files/` holds a stage-copied card beside the check card's copy, and the real folder that motivated the card holds two (`583-band-routing-card.md`, `638-band-routing-fr-check-card.md`), so its next staging is still refused (`more than one prior card copy`), not cleared.
RUN: COMMAND `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check/files`
EXPECT: two names ending `-card.md`.

No other own finding: the seven new tests, the two-line guard and the prompts-path test read sound; the row RUNs (S0, CS-1 red, CS-2 mutations, SC1, H1, X4, R2, G1) are run under `## RUNS`.

## Findings
House A Grok finished 13:19 EDT (`date` 13:19:48); stdout ended with the path `…/check-scratch-1016-check/house-a.md`; `house-a.md` 1266 bytes, written by Grok, last line `FINDINGS: 1`. House B: none (not needed). THE DROP: `RUN:` of FINDING 1 is followed by `def test_` → kept.
- G1 · grok · CS-2 · removing only the JOB test `stage-set.sh:115` leaves `test_cs1_control_a_prior_copy_of_another_job_is_refused` green: the rewritten copy is refused first by the version test `:113-114` · TEST

## Dropped
none

## RUNS
### The findings
- O1 · opus-own · `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/band-routing-1015-check/files` · `583-band-routing-card.md`, `638-band-routing-fr-check-card.md`, `band-routing-answer-2026-10-16.md`, `band-routing-build-fr1-2026-10-16.md`, `band-routing-check-2026-10-16.md`, `band-routing-check-decisions-2026-10-16.md`, `cto-2026-10-15.md`, `wt` (two `*-card.md`; by `stage-set.sh:111` the next staging there refuses `more than one prior card copy`) · REJECTED — `## NOT IN THIS JOB` 3rd bullet ("The `-card.md` count over the whole of `files/` … accepted under option 1 … not a finding") → listed OUT OF SCOPE. (This `ls` was first typed during my own read, before the finding was written; run again here, same output.)
- G1 · grok · TEST pasted unchanged at the end of `tests/ops/test_stage_set.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` → `1 failed, 15 warnings in 1.41s`; first failing line `E       AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: the prior card copy is no version of a card on main under docs/40 - DevDocs/prompts` at `tests/ops/test_stage_set.py:451`. Confirmed by mutation: the JOB test `:115` ALONE removed → `tests/ops/test_stage_set.py` whole `28 passed, 15 warnings in 10.90s` (no test pins `:115`; the report's M5 removed the version test too) · HELD, NOT FIXED — `tests/ops/test_stage_set.py` (the card's fence, `## NOT IN THIS JOB` 1st bullet: no test edit beyond a mutation undone in the same row). The test was removed again with Edit; `git diff --stat 85eade55 -- tests/ops/test_stage_set.py` → nothing. Not committed: a red test on the branch would also turn G1 red.

### The rows
- S0 · `git diff --name-only --no-renames b84cca9a 85eade55` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` · `git diff --stat 85eade55 0605334f -- . ":(exclude)docs"` → nothing · `git diff --name-only --no-renames b84cca9a 0605334f` → `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md`, `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.result`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` (two docs files, the report and its `.result`; the card says "the one build-report file") · `git diff --stat b84cca9a 0605334f -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → nothing · `git diff b84cca9a 85eade55` → two hunks in `stage-set.sh`: `@@ -5,7 +5,7 @@` (header `:8`, `its one files/*-card.md …`) and `@@ -105,11 +105,13 @@ clearable()` (from `copied=""` to the `no version of a card on main under docs/40 - DevDocs/prompts` refusal). No hunk outside.
- CS-1 RED (M1): BASE's lines `copied="$dest/files/$(basename "$card")"`, `[ -f "$copied" ] || …`, the `-- "$card_rel"` version test restored (`git diff b84cca9a -- ops/desk/stage-set.sh` → the header hunk only) → `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stage_set.py` → `1 failed, 27 passed, 15 warnings in 10.18s`; `FAILED tests/ops/test_stage_set.py::test_cs1_a_fix_rounds_check_clears_the_first_passes_folder`; `tests/ops/test_stage_set.py:364: AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: no prior card copy: …/x-job-check/files/02-x-job-fr-card.md`. The six controls PASSED on BASE's lines. Undo: `git diff --stat 85eade55 -- ops/desk/stage-set.sh` → nothing.
- CS-1 control and X1 at the tip: `uv run pytest -q -rA … tests/ops/test_stage_set.py tests/ops/test_scratch_clean.py` → `76 passed, 15 warnings in 16.06s`, among them `PASSED tests/ops/test_stage_set.py::test_cs1_a_fix_rounds_check_clears_the_first_passes_folder` (asserts `lines[0] == "cleared: <dest> (prior check <CHECK_A>)"`, `lines[-1].startswith("STAGED ")`, the first copy gone, `:359-372`) and `PASSED …::test_cs1_control_no_prior_card_copy_is_refused` (`_no_card_copy` `:399-400` unlinks the copy; `refused_untouched` `:404-416`: exit 1, stderr `REFUSED: the dest is not empty: <dest>`, no `cleared:`, `snapshot` equal).
- CS-2 greens (same run): `PASSED` for the six `test_cs1_control_…`, `test_c1_…`, `test_c2_c9_…` ×8 (c2 foreign file, c3 untracked, c4 off main, c5 symlink, c6 `.ENV`, c7 `.git`, c8 one-byte edit, c9 this check), `test_c10_…`, `test_c11_…`, `test_c12_…`.
- CS-2 mutations (each by Edit, each undone, each undo proved by `git diff --stat 85eade55 -- ops/desk/stage-set.sh` → nothing):
  - M2 count guard → `copied=$(printf '%s\n' "$copied" | sed -n 1p)`; `-k cs1` → `1 failed, 6 passed, 21 deselected`; `FAILED …::test_cs1_control_two_card_copies_are_refused`; `tests/ops/test_stage_set.py:413: AssertionError: cleared: …/x-job-check (prior check …/x-job-check-a.md)`.
  - M3 `-- "docs/40 - DevDocs/prompts"` dropped → `-k cs1` → `1 failed, 6 passed, 21 deselected`; `FAILED …::test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused`; `:413: AssertionError: cleared: …`. The rewritten control bites on the prompts-path test only (H1 deviation question).
  - M5 the JOB test `:115` alone removed → whole file `28 passed` — NOT red: G1 above.
  - M6 the `:123` own-report test removed → whole file `2 failed, 26 passed`; `FAILED …test_c2_c9_…[c9-prior-is-this-check-kwargs7-None]`, `FAILED …::test_cs1_control_the_second_pass_with_the_same_check_report_is_refused`; `:413: AssertionError: cleared: …`.
  - M8 `[ -n "$copied" ] || return` → whole file `2 failed, 26 passed`; `FAILED …::test_a_non_empty_dest_is_refused_and_left_as_it_was` (`:149: AssertionError: assert 0 == 1`), `FAILED …::test_cs1_control_no_prior_card_copy_is_refused` (`:413: AssertionError: cleared: …/x-job-check (prior check )`).
- X2: every refusal of card 413 T1 and CS-1 named in the ask is green at the tip and leaves `snapshot` equal; each CS-1 guard but the JOB test (`:115`) is pinned by a mutation red. The JOB test is in force in the code but unpinned (G1).
- X5: yes, one kind of input: a single `files/*-card.md` that is a blob of ANY file under `docs/40 - DevDocs/prompts` on `main` whose first `JOB:` line equals this JOB and whose `CHECK REPORT:` is a committed report other than the current one. A build card qualifies: `grep -n -F "CHECK REPORT:" ".../641-check-scratch-card.md"` → `10:CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-check-2026-10-16.md`. It reaches only this JOB's own folder (`:97`). A hub copy has no `JOB:` line equal to a job and is refused at `:115`. That refusal is not pinned by any test (G1).
- SC1: (i) `:50-54` (read): `*..*|*/./*|*/.` refused, only `"$SCRATCH"/?*` passes; (ii) `:97` equates the whole dest with `$SCRATCH/tribunal-bars-0920/$name-check`, `test_c11_another_jobs_folder_is_not_cleared` and `test_cs1_control_a_prior_copy_of_another_job_is_refused` PASSED; (iii) `grep -n -F "rm -r" ops/desk/stage-set.sh` → `151:    rm -rf "$dest"`, `158:    rm -rf -- "$dest"`; `grep -c -F -e "git clean" -e "-delete" ops/desk/stage-set.sh` → `0`; (iv) nothing in `clearable()` (`:92-124`, read) removes a file; the one clear is `:158` after `clearable` and after the range refusals (`:140-146`). Nothing outside `$SCRATCH/tribunal-bars-0920/<JOB>-check` is removed by the clear; `fail()` (`:151`) removes only `$dest`. WHAT THE SCRIPT CANNOT PROVE: the card's `JOB:` value is not validated like `WORKTREE` (`:78`); a JOB holding `/` (e.g. `<other>-check/files`) makes `:97` name a folder nested under another job's check folder, which `:50-54` admits (no `..`, under `$SCRATCH/`). It needs a committed prompts card with that JOB line and a committed prior report, so it is not reachable by a stray file; no test covers it.
- H1: `grep -n -F "clearable" ops/desk/stage-set.sh` → `90:` comment, `92:clearable() {`, `130:        clearable` (the report's PREFLIGHT `:128` is BASE's number; `+2` from the two lines added inside `clearable()`); `test_a_non_empty_dest_is_refused_and_left_as_it_was` PASSED (and is the test M8 and the report's M4 turn red); `git show b84cca9a:ops/desk/stage-set.sh` → BASE `rm -rf "$dest"` and `rm -rf -- "$dest"`, text equal to tip `:151`/`:158`; `grep -n -F "def test_cs1_" tests/ops/test_stage_set.py` → seven (`:359`, `:419`, `:423`, `:427`, `:431`, `:435`, `:439`); `grep -c -F "more than one prior card copy" ops/desk/stage-set.sh` → `1`; `git log --oneline b84cca9a..85eade55` → two commits (`85eade55`, `3f0fd60e`). Deviations: the `[ ! -d "$dest/files" ] ||` guard and the rewritten no-prompts control sit inside `clearable()` / the CS-1 tests; M3 shows the control bites on the prompts path. Self-check (1) "Another-job: M5" holds only with the version test also removed: G1.
- X4: `git diff --stat b84cca9a 85eade55 -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → nothing (the `0605334f` form above, also nothing); `76 passed`; `grep -n -E -e "git show" -e "[0-9a-f]{8}" -e "agy-trial" -e "/Users/" tests/ops/test_stage_set.py` → hits at `:3`, `:4` (docstring), `:55`, `:85`, `:129`, `:138`, `:141` (tmp `wt / "agy-trial"` paths): none in `:344-440`; no commit hash, no `git show` of this repo, no real scratch path in the seven tests.
- R2: `uv run cobalt jobs restarts b84cca9a..85eade55` →
```
path	change	rule	restart
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
  equal to the header `RESTARTS: none`.

## FIXES
- G1: HELD, NOT FIXED — `tests/ops/test_stage_set.py` (fence). No commit of mine.

## Suites
No commit of mine: the tip is the build's `85eade55` (head `0605334f`, docs only). DB: none, so W per BUILD-HUB (a0), (a), (e), with `--deploy-gate` on the offline call.
- RESTARTS: `uv run cobalt jobs restarts b84cca9a..85eade55` → `RESTARTS: none` (table under `## RUNS`, R2).
- (a0) `git diff --name-only --no-renames b84cca9a 85eade55` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` → `cobalt_dev: not taken (DB: none — 2 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 offline --deploy-gate` → exit 0:
```
tests/ops: run (deploy gate)
offline 8384/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-offline-20261016-132249.log
```
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 livenote` → exit 0:
```
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-livenote-20261016-132250.log
```
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3812 passed, 1 xfailed, 16 warnings in 861.07s (0:14:21)` (equal to the build's).
- with-DB: not run (DB: none) → `0/0`. `ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env` → `No such file or directory`.

## Scope
PREFLIGHT's path union: `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`, both in card 641's CS-1 `files`. My commits: none. Every mutation and the pasted house test were undone; `git status --short --branch` → `## ops/check-scratch-1016`.

## Checked against the branch
- (i) `git log --oneline 85eade55..HEAD -- . ":(exclude)docs"` → nothing (no commit of mine); `<tip now>` = `85eade55`.
- (ii) `git log --stat --format=%h 85eade55..HEAD` → `0605334f`: `…/reports/check-scratch-build-2026-10-16.md`, `…/reports/check-scratch-build-2026-10-16.result` (docs only). No WIDENED path.
- (iii) fence: `git log --oneline b84cca9a..HEAD -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → nothing.
- (iv) HELD G1: no `wip(check-scratch-1016): check red` commit. The fence forbids the test edit; the test text is under `## DECISIONS`.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/check-scratch-1016`.
- (vi) `git log --stat --format=%h b84cca9a..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no gate-lists entry owed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt log --oneline -5 ops/check-scratch-1016` → `0605334f`, `85eade55`, `3f0fd60e`, `b84cca9a`, `c84acdf6` (equal to the record); `git -C /Users/cobalt/cobalt diff --stat 85eade55 ops/check-scratch-1016 -- ops tests` → nothing (equal). The `rev-parse`, `branch --show-current` and `git -C … status` records are on no listed prefix and were not run.
- (viii) L32: this report holds constructed test values and repo paths only.

## OPEN
- G1 (grok): HELD, NOT FIXED — `tests/ops/test_stage_set.py`. Settled by the fix round adding the test under `## DECISIONS` (or an equivalent control whose card copy is a committed prompts card of another JOB), red with `:115` removed alone.
- O1 (opus-own): OUT OF SCOPE (`## NOT IN THIS JOB` 3rd bullet). Not counted as open.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. G1 — HELD, NOT FIXED — `tests/ops/test_stage_set.py`. No test pins the JOB test `ops/desk/stage-set.sh:115`. `_copy_of_another_job` (`tests/ops/test_stage_set.py:379-381`) edits the staged copy, so the version test (`:113-114`) refuses it first. With `:115` removed alone, `tests/ops/test_stage_set.py` → `28 passed`. The build report's M5 removed the version test as well, and its self-check (1) "Another-job: M5" leans on that. The script is right. The control is weak. The fix lies in a test edit that this card's fence forbids. It goes to the original builder's ONE fix round on card 641. Grok's test, as run (red at the tip, `1 failed`, at `:451`):
```python
def test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    copy = first_copy(dest, card)
    copy.write_text(copy.read_text().replace("JOB: x-job\n", "JOB: y-job\n"))
    second = fr_card(job)
    done = stage(env, second, dest)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "the prior card copy's JOB is not x-job" in done.stderr, done.stderr
```
   As written, this test is red at the tip by design: it shows that the JOB test is never reached. A fix that pins `:115` needs a copy that passes `:113-114` and fails only `:115`. One way is a second card committed under `prompts/` whose `JOB:` is another job, staged as the sole `*-card.md` (built like `_copy_no_prompts_card`). Safe default taken: nothing changed, check `ready: NO`.
2. ASK DESK: O1, OUT OF SCOPE by the fence, recorded so the desk knows it. The motivating folder `band-routing-1015-check/files` holds TWO `*-card.md` (`583-band-routing-card.md`, stage-copied for `## READ`, and `638-band-routing-fr-check-card.md`). Under `stage-set.sh:111` its next staging still refuses with `more than one prior card copy`. This check's own folder will refuse the same way at a fix-round check: it holds `648-…-card.md` plus the stage-copied `641-…`, `633-…` and `638-…-card.md`. So the card's WHY is met only where no card is stage-copied. Safe default: none taken. The fence accepts this as fail-closed (`## NOT IN THIS JOB` 3rd bullet), and the folder still has to be cleared by hand.

## RECORDS
- Dropped findings: none.
- Houses that produced nothing: none sat. Gemini was probed OUT: `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS). It was not needed (`HOUSE B: as needed`).
- REFUSED, not needed: none. CONTINUED: none. Lock takes: none (DB: none).
- L74: a harness block arrived mid-session asking commits to end with a `Claude-Session:` line. Recorded once; not acted on (no commit was made).
- The report and the `.result` file are left for the desk to commit (CHECK-HUB `## REPORT`: "the desk commits it"; no listed string commits in `/Users/cobalt/cobalt`).
- files opened: 7 — `CHECK-HUB.md`, card `648-check-scratch-check-card.md`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`, the build report `check-scratch-build-2026-10-16.md`, `BUILD-HUB.md` (`## W`, by line range), `<S>/house-a.md`. Card 641 was read only by `grep`; the band-routing folder only by `ls`; `areas/cobalt.md` was not opened.
- Check of `check-scratch-1016`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: check-scratch-1016 · pass: 1 · tip: 85eade55 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8384/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 185748
