# check-scratch-fr1 — CHECK report 2026-10-17

## §0 Headline
- Check of `ops/check-scratch-fr1` at `b093f192`: every card row re-run. MK-1, CL-1a, CL-1b reds on BASE, and M1–M8 behave as the build said, except M4 (the link test stays green under it because `:102` refuses the link first) and M6 (the numeric sort is pinned by no test). The two retired tests go red against the tip's script, and D1 is confirmed (keep `0`).
- House A Grok: 1 finding (A1, X7), red for its reason, REJECTED as fail-closed and unreachable from a launch (open). House B: none (not needed; Gemini OUT on a harness error).
- Own O1 HELD: the legacy branch's `HOUSE A:` filter (`stage-set.sh:134`) is pinned by no test now that every FR-1 test runs through the marker. Its fix is one test, which this card fences, so it is NOT FIXED and goes to the fix round.
- Suites green: offline `8393/0` (tests/ops `3821 passed, 1 xfailed`, deploy gate), live-note `146/0`, two-file `85 passed`; RESTARTS none; no commit by this check.
- ready: NO (held unfixed 1).

## L74
One system block in this session asked for a `Claude-Session:` line in commit messages: recorded here, not acted on (no commit was made).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/690-check-scratch-fr1-check-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/690-check-scratch-fr1-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/690-check-scratch-fr1-check-card.md" · 0 · 573e96fd422a73dbe5a2bad8ab56cb35395d4e7c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/690-check-scratch-fr1-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …/cto-2026-09-24.md` · 0 · one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …/cto-2026-09-24.md` · 0 · one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · 0 · `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`date` · 0 · `Sat Oct 17 10:13:33 EDT 2026`

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Sat Oct 17 10:13:37 EDT 2026
status · git status --short --branch · 0 · ## ops/check-scratch-fr1
head · git log --oneline -1; git log --stat --format=%h b093f192..HEAD · 0 · (6 lines)
    5f42c4f3 docs(check-scratch-fr1): build report — b093f192
    5f42c4f3
    
     .../reports/check-scratch-fr1-build-2026-10-17.md  | 166 +++++++++++++++++++++
     .../check-scratch-fr1-build-2026-10-17.result      |  15 ++
     2 files changed, 181 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/check-scratch-fr1/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/check-scratch-fr1/docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md" · 0 · BUILT · job: check-scratch-fr1 · tip: b093f192 | on 79f6f2f3 | migration: none | offline 8393/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 160227
range · git log --oneline 79f6f2f3..b093f192 · 0 · (2 lines)
    b093f192 fix(check-scratch-fr1): stage-set records STAGED-CARD and clearable() reads it, legacy highest-numbered fallback (MK-1, CL-1, L3, L67)
    0d52929f wip(check-scratch-fr1): red
PREFLIGHT OK
```
THE RANGE: `git log --stat --format=%h 79f6f2f3..b093f192` · 0:
```
b093f192

 ops/desk/stage-set.sh       | 70 +++++++++++++++++++++++++++++----------------
 tests/ops/test_stage_set.py | 12 ++------
 2 files changed, 48 insertions(+), 34 deletions(-)
0d52929f

 tests/ops/test_stage_set.py | 135 ++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 135 insertions(+)
```
Path union: `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. Commits: 2.

DB: none: `git diff --name-only --no-renames 79f6f2f3 b093f192` · 0 · `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py` — every path under `ops/` or `tests/ops/`.

`ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-fr1-check` · 1 · `No such file or directory` → fresh.

House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · 0 · lines whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
No `HOUSE A: OpenAI` header line → Sol not probed. Card `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**. Gemini OUT is HARNESS (an unknown model id), a harness record (card X9).

Proven by first real use: `git add` / `git commit` (none needed unless a test is committed), `uv run pytest *` at `## 4`, `sh …/gate.sh` at `## 6`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
15820 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-fr1-check/diff.md
33779 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-fr1-check/files/690-check-scratch-fr1-check-card.md
23721 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-fr1-check/files/check-scratch-fr1-build-2026-10-17.md
12538 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-fr1-check/files/wt/ops/desk/stage-set.sh
28613 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-fr1-check/files/wt/tests/ops/test_stage_set.py
719 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-fr1-check/rulings.md
STAGED 6 files · 115190 bytes · commits 2
```
`commits 2` = PREFLIGHT's range count (2). The `## READ` files, each `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh <source> <S>/files/<name>`:
- `COPIED 20898 …/files/681-check-scratch-fr1-card.md`
- `COPIED 4606 …/files/check-662-and-583-fr2-decisions-2026-10-17.md`
- `COPIED 27774 …/files/641-check-scratch-card.md`
- `COPIED 21921 …/files/648-check-scratch-check-card.md`
- `COPIED 14787 …/files/677-gemini-probe-id-check-card.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph).
House A Grok started 10:16 EDT (`date` 10:16:33; gates R17, R19 re-run, one row each), `run_in_background`, timeout 2700000. No house B (not needed).

## OWN FINDINGS
Written before any house list was opened (read: the card, the diff `79f6f2f3..b093f192`, `ops/desk/stage-set.sh` and `tests/ops/test_stage_set.py` at the tip, the build report's named sections, cobalt.md's two sections).

FINDING O1
ROW: CL-1b (HOUSE TEXT (1)/(5))
CLAIM: The legacy branch's build-copy filter `grep -q '^HOUSE A:' || continue` (`ops/desk/stage-set.sh:134`) is pinned by no test at the tip: since the tip's `prior_staging` writes `STAGED-CARD`, every FR-1 test (`tests/ops/test_stage_set.py:465`, `:480`) now runs the MARKER branch (the build report's own `## PRE-STOP SELF-CHECK` (2): "now through the marker"), and the one legacy test (`:574`) ranks its build copy `01-…` below the check cards, so removing `:134` leaves the file green; a build-card READ copy numbered above the prior check card (the shape of this very check's folder: build card 681 copied beside check card 690 is the reverse, but any build card drafted after its first check card is not) would then be taken as the prior card.
RUN: TEST — `tests/ops/test_stage_set.py`
```python
def test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    (dest / "STAGED-CARD").unlink(missing_ok=True)
    build = build_card_copy(dest, card, name="05-x-job-build-card.md")
    second = fr_card(job)
    done = stage(env, second, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines()[0] == f"cleared: {dest} (prior check {repo / CHECK_A})"
    assert not build.exists()
```
EXPECT: on the tip `1 passed` (the behaviour is right); with `:134` removed by Edit, `tests/ops/test_stage_set.py` WITHOUT this test stays `37 passed` (the claim: unpinned) while this test fails with `assert 1 == 0` / `the prior card copy is no version of a card on main` (the build copy, numbered 05, taken as prior).

FINDINGS: 1

## Findings
Grok's completion notice at 10:30 (`date` 10:30:56); `ls -la <S>` → `house-a.md` 1322 bytes (10:30), written by Grok itself; its stdout was its progress lines and the path. House B: none (not needed). `grep -n -F "RUN:"` on `house-a.md` → line 4 `RUN: TEST`, followed by the test file and a `def test_` function: kept.
- A1 · Grok · X7 · `stage-set.sh:242` writes any basename; a card not ending `-card.md` (`01-x-job-notes.md`) stages, and the next staging of that dest refuses at `:118` (`the STAGED-CARD marker is not one card file name`) · TEST
- O1 · Opus · CL-1b · the legacy `HOUSE A:` filter (`:134`) is pinned by no test: every FR-1 test now runs the marker branch · TEST

Grok's list, whole (`<S>/house-a.md`):
```
FINDING 1
ROW: X7
CLAIM: `ops/desk/stage-set.sh:242` writes `$(basename "$card")` with no `*-card.md` check, so a card named `01-x-job-notes.md` stages, and the next staging of that same dest refuses at `ops/desk/stage-set.sh:118` (`the STAGED-CARD marker is not one card file name`) with the folder left in place; an interior space in a name that still ends `-card.md` does not do this, and no test pins a basename that misses the `*-card.md` arm (`tests/ops/test_stage_set.py:117`).
RUN: TEST
tests/ops/test_stage_set.py
def test_a_card_basename_that_does_not_end_card_md_makes_the_next_staging_refuse(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    plain = card.parent / "01-x-job-notes.md"
    plain.write_text(card.read_text())
    git(repo, "add", "--", str(plain.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "a card whose name does not end -card.md")
    first = stage(env, plain, dest)
    assert first.returncode == 0, first.stdout + first.stderr
    assert (dest / "STAGED-CARD").read_text() == "01-x-job-notes.md\n"
    again = stage(env, card, dest)
    assert again.returncode == 0, again.stdout + again.stderr
EXPECT: `AssertionError: assert 1 == 0` and stderr `REFUSED: the dest is not empty: <dest> — not cleared: the STAGED-CARD marker is not one card file name`
FINDINGS: 1
```
(The cite `tests/ops/test_stage_set.py:117` is a wrong line, the `files = sorted(…)` line of the whole-set test; the claim stands on `:118`/`:242` of the script.)

## Dropped
none

## RUNS
### The card's rows (each a RUN; every mutation by Edit, undone by Edit, the undo proved by `git diff --stat b093f192 -- ops/desk/stage-set.sh` → printed nothing, after each)

**S0** · `git diff --stat 79f6f2f3 b093f192` → `ops/desk/stage-set.sh | 70 +++++++++++++--------` · `tests/ops/test_stage_set.py | 147 +++++++++++++++++++++++++++++++++++++++++---` · `2 files changed, 183 insertions(+), 34 deletions(-)`. `git diff --name-only --no-renames 79f6f2f3 b093f192` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. `git diff --name-only --no-renames 79f6f2f3 5f42c4f3` → `docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md`, `docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.result`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. `git diff --stat b093f192 5f42c4f3 -- . ":(exclude)docs"` → nothing. `git diff --stat 79f6f2f3 5f42c4f3 -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → nothing. No `src/`, `configs/`, `.claude/`, hub or `CARD.md` path. `git -C /Users/cobalt/cobalt-wt/check-scratch-fr1 status --short --branch` → REFUSED (not on the allow line, `## RECORDS`); `git status --short --branch` in `<WT>` → `## ops/check-scratch-fr1`. `git diff 79f6f2f3 b093f192 -- ops/desk/stage-set.sh` → four hunks: `@@ -4,8 +4,8 @@` (header `:7-8`), `@@ -95,7 +95,7 @@` (`:98`, `! -name STAGED-CARD` added, no other clause changed), `@@ -106,31 +106,52 @@` (the prior-card block `:108-154`; the lines `:155-` onward appear only as context), `@@ -218,6 +239,7 @@` (the marker line `:242`). No hunk outside.

**MK-1** · read at the tip: `:240` card copy, `:241` report copy, `:242` `printf '%s\n' "$(basename "$card")" > "$dest/STAGED-CARD" || fail "STAGED-CARD write failed"`, then the `files/wt` loop `:244-250`; `fail()` `:192-197` removes `$dest` and re-makes it empty when it existed; the listing `:254` is `find . -type f` over `$dest`, so the marker is listed and counted. Header `:7-8` names `STAGED-CARD` and "holds the basename of the card". Tests at the tip: `PASSED …::test_mk1_staging_writes_the_marker_naming_the_card`, `PASSED …::test_mk1_a_restaging_rewrites_the_marker_with_the_new_card`, control `PASSED …::test_the_whole_set_is_staged_byte_equal_to_git_at_tip` (the `-rA` run below). RED on BASE (the script returned to `79f6f2f3` by four Edits; `git diff --stat 79f6f2f3 -- ops/desk/stage-set.sh` → nothing; the 7 new tests are byte-equal between `0d52929f` and the tip, `git diff -U0` X6): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py -k "mk1 or mk2 or test_the_whole_set"` → `6 failed, 2 passed, 29 deselected` — `test_mk1_staging_writes_…`: `E       AssertionError: assert (False)` / `+  where False = is_file()`; `test_mk1_a_restaging_…`: `E       FileNotFoundError: [Errno 2] No such file or directory: '…/x-job-check/STAGED-CARD'`; the two passed are the whole-set control and the link control. Restored; `git diff --stat b093f192 -- ops/desk/stage-set.sh` → nothing. M1 (`:242` removed) → `2 failed, 35 passed`: `FAILED …::test_mk1_staging_writes_the_marker_naming_the_card`, `FAILED …::test_mk1_a_restaging_rewrites_the_marker_with_the_new_card`; the whole-set control green under it. X1: YES.

**CL-1a** · read at the tip `:108-121` as the card states: `:110` enters on `-e || -L`; `:112` regular, not a link, `wc -l` = 1 and `sed -n '$='` = 1; `:115-119` `*/*|.|..` → miss, `*-card.md` → on, `*` → miss; `:120` the named file regular, not a link, else `no prior card copy: $dest/files/$m`; `:121` `copied`. No other `files/` card is read on that branch (the `find` of `:126` sits in the `else`). Greens: the four `PASSED …::test_mk2_control_a_marker_naming_another_jobs_card_is_refused`, `…_two_same_job_cards_with_a_marker_clear_only_by_the_marker`, `…_no_card_file_name_is_refused`, `…_a_link_is_refused`. RED on BASE (same run as MK-1): `test_mk2_two_same_job_…` → `E       AssertionError: REFUSED: the dest is not empty: … — not cleared: an entry the check did not write: …/x-job-check/STAGED-CARD`; `…_no_card_file_name_…` → the same `an entry the check did not write: …/STAGED-CARD`; `…_another_jobs_card_…` (run alone, `--tb=line`) → `E   AssertionError: REFUSED: the dest is not empty: … — not cleared: an entry the check did not write: …/x-job-check/STAGED-CARD`; the link test GREEN on BASE. M2 (`:110` → `if false; then`) → `3 failed, 34 passed`: the other-job, two-same-job and no-card-name tests, first line `E   AssertionError: cleared: …/x-job-check (prior check …/x-job-check-a.md)`. M3 (the `*/*|.|..` arm removed) → `1 failed`: `…_no_card_file_name_is_refused`, `E   AssertionError: REFUSED: the dest is not empty: … — not cleared: no prior card copy: …/x-job-check/files/../x-card.md` (still refused, by `:120`; the test pins the message). M4 (`:112` reduced to `[ -e "$marker" ]` plus the line tests) → `37 passed`: the link stays refused, by `:102` (`find "$dest" -mindepth 1 -maxdepth 1 ! -name files ! -type f` → `an entry that is not a regular file`), which runs before the marker branch; `:112`'s `-f`/`! -L` is unreachable for a link or a folder named `STAGED-CARD`. X2: YES (marker beside a higher-numbered same-JOB card clears by the marker alone; other-JOB, missing file, non-card name, link refuse, dest untouched — the snapshot assertions).
X7: a marker the script wrote itself makes its next staging refuse only when the staged card's basename does not end `-card.md` (→ `the STAGED-CARD marker is not one card file name`) or holds a newline (two lines → the same miss). Both fail closed; BASE refused the first too (its `find … -name '*-card.md'` found no card: `no prior card copy`). Glob `**/*-check*.md` under `prompts/2026-10-16/`: the check cards there all end `-check-card.md`; the other hits are draft and preflight prompts (`-draft-…`, `…-preflight.md`), never staged as a card. A space is fine (`$m` is quoted at `:120-121`). None in practice.

**CL-1b** · read at the tip `:122-153` as the card states (`:126` `-type f -name '*-card.md'`; `:132` header to the first blank line; `:133-134` the pair; `:135` JOB; `:136-137` the leading number, `${n:-0}`; `:147` `sort -t "$tab" -k1,1n -k2,2 | tail -n 1 | cut -f2-`; `:148-150` the lone other-JOB card; `:152` else `no prior card copy`). `grep -c -F "more than one prior card copy" ops/desk/stage-set.sh` at the tip → `0` (BASE carries it: the diff's `-` line `[ "$(printf '%s' "$mine" | wc -l | tr -d ' ')" = 1 ] || { miss="more than one prior card copy in $dest/files"; return; }`). The tests after the block (`:155-166`, the version, JOB and prior-report tests) are context lines in the diff: unchanged from BASE. Green: `PASSED …::test_mk2_legacy_real_shape_of_the_band_routing_folder_clears`. RED on BASE (run alone): `E   AssertionError: REFUSED: the dest is not empty: … — not cleared: more than one prior card copy in …/x-job-check/files` / `assert 1 == 0`. The retired tests, bodies from BASE's file run against the tip's script from a throwaway file in the job scratchpad (`/Users/cobalt/.claude/jobs/1eeacab5/tmp/test_retired_bodies.py`, importing the repo's helpers): `2 failed` — `test_cs1_control_two_card_copies_are_refused` and `test_fr1_control_two_same_job_check_cards_are_refused`, each `E   AssertionError: cleared: …/x-job-check (prior check …/x-job-check-a.md)` / `assert 0 == 1` at `tests/ops/test_stage_set.py:414`. M5 (`tail -n 1` → `head -n 1`) → `1 failed`: `…_legacy_real_shape_…`, `E   AssertionError: assert 'cleared: /pr...b-check-a.md)' == 'cleared: /pr...b-check-b.md)'`. M6 (`-k1,1n` → `-k1,1`) → `37 passed`: the numeric key is pinned by no test (the tests use equal-width `01…04`); a real crossing needs two same-JOB check cards in one unmarked folder whose numbers differ in width (e.g. `999-…` and `1000-…`): card numbers run at 6xx, and an unmarked folder exists only until each job's next staging after deploy; recorded, not a finding (card: "a finding only if a real card name can do it"). D1: confirmed in code (`:136-137`, `${n:-0}`) and by hand (`/Users/cobalt/.claude/jobs/1eeacab5/tmp/test_d1_no_digit.py`: an unmarked folder with `01-x-job-card.md` (CHECK_A) and `x-job-nodigit-check-card.md` (CHECK_B) → `1 passed`, stdout `cleared: …/x-job-check (prior check …/x-job-check-a.md)`): the no-digit card ranks below the numbered one. Recommendation to the desk: keep `0`. X3: YES.

**CL-2** · the `-rA` run of the whole file at the tip (below) carries a `PASSED` line for every named test: `[c2-foreign-file…]`, `[c3-prior-report-untracked…]`, `[c4-prior-report-off-main…]`, `[c5-symlink…]`, `[c6-dot-env…]`, `[c7-dot-git…]`, `[c8-card-copy-edited…]`, `[c9-prior-is-this-check…]`, `test_c10_…`, `test_c11_…`, `test_cs1_control_a_prior_copy_of_another_job_is_refused`, `…_no_prompts_card_is_refused`, `…_the_second_pass_with_the_same_check_report_is_refused`, `…_a_foreign_file_blocks_the_clear`, `…_no_prior_card_copy_is_refused`, `test_cs1_rewritten_job_line_…`. Each goes through `refused_untouched` (`:405-417`) or its own body: exit 1, stderr starts `REFUSED: the dest is not empty: <dest>`, `snapshot(dest) == before`. `test_cs1_control_no_prior_card_copy_is_refused`'s stderr (throwaway `/Users/cobalt/.claude/jobs/1eeacab5/tmp/test_cl2_stderr.py`, the same steps): `1 REFUSED: the dest is not empty: …/x-job-check — not cleared: no prior card copy: …/x-job-check/files/01-x-job-card.md` — the marker branch's `:120`. M7 (`-- "docs/40 - DevDocs/prompts"` dropped from `:156`) → `1 failed`: `test_cs1_control_a_prior_copy_that_is_no_prompts_card_is_refused`, `E   AssertionError: cleared: …/x-job-check (prior check …/x-job-check-a.md)` / `assert 0 == 1` — the version test is what refuses it. M8 (`:158`, the JOB test, removed) → `2 failed, 35 passed`: `FAILED …::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob`, `FAILED …::test_mk2_control_a_marker_naming_another_jobs_card_is_refused` (`test_cs1_control_a_prior_copy_of_another_job_is_refused` stays green under M8: its edited copy is no version on `main`, the version test refuses it). X4: YES.
X5: with a marker, only the file it names can become `copied` (`:121`); a card of another job whose JOB line equals this one IS this job's card for the script (the JOB test reads the line), and it then still needs to be a version of a prompts card on `main`, name a committed prior report on `main` other than this check's own. Without a marker: any regular `files/*-card.md` whose header carries `CHECK REPORT:` and `HOUSE A:`, whose JOB is this JOB and which ranks highest — the one input is a same-JOB check card committed on `main` with a committed `CHECK REPORT`, copied into `files/` by hand or by `stage-copy.sh`; that is the design (card fence, item 4). The legacy filter that keeps a build card's READ copy out (`:134`) is pinned by no test: finding O1.

**SC1** · (i) `:50-54`: `*..*|*/./*|*/.)` refused, only `"$SCRATCH"/?*` passes; (ii) `:97` `[ "$dest" = "$SCRATCH/tribunal-bars-0920/$name-check" ]`; (iii) `grep -n -F "rm -r" ops/desk/stage-set.sh` → `194:    rm -rf "$dest"`, `201:    rm -rf -- "$dest"`; the diff has no hunk on either line (equal to BASE); `grep -c -F -e "git clean" -e "-delete" ops/desk/stage-set.sh` → `0`; `PASSED …::test_c12_the_script_removes_only_by_its_two_rm_rf_lines`; (iv) `$m` is read by `sed -n '1p'` (`:114`), never sourced or evaluated, and reaches a path only at `:120-121` after the `:115-119` arms; the legacy `$f` comes from `find "$dest/files" -mindepth 1 -maxdepth 1` (`:126`). `PASSED …::test_c11_another_jobs_folder_is_not_cleared`, `PASSED …::test_mk2_control_a_marker_naming_another_jobs_card_is_refused`. What the script cannot prove: a `JOB:` value is not validated like `WORKTREE` (`:78`), but `:97` equates the whole `$dest`, already held under `$SCRATCH/` by `:50-54` (no `..`); a marker is trusted for the NAME only, every content test still runs on the named copy. No path outside `$SCRATCH/tribunal-bars-0920/<JOB>-check` is removed. X7 (rm/clean part): YES.

**H1** · (1) the reds above. (2) `grep -rn -F "clearable" ops/desk` → `ops/desk/stage-set.sh:90:# clearable: …`, `:92:clearable() {`, `:173:        clearable`: one caller, at `:173` on the tip; the build report says `:152` (`## PRE-STOP SELF-CHECK` (2), `## FOR THE CHECK`), BASE's number — the prior-card block grew by 21 lines above it. `grep -n -F "STAGED-CARD" ops/desk/stage-set.sh` → `:7`, `:8`, `:98`, `:109`, `:113`, `:116`, `:118`, `:242`: one write site (`:242`). (3) `grep -n -E "^def test_(mk1|mk2|cs1|fr1)" tests/ops/test_stage_set.py` → the seven new at `:531`, `:540`, `:574`, `:597`, `:612`, `:637`, `:651`, plus `:359`, `:420`, `:424`, `:428`, `:432`, `:436`, `:465`, `:480`, `:509`. `git log --oneline 79f6f2f3..b093f192` → two commits (PREFLIGHT). `grep -n -F "_two_card_copies" tests/ops/test_stage_set.py` → `375:def _two_card_copies(job, dest, card):` only: dead code; a note, not a finding (the card allowed four existing-test edits; the throwaway above still used it to run the retired body).

**X6** · `git diff -U0 79f6f2f3 b093f192 -- tests/ops/test_stage_set.py` → `@@ -393,0 +394 @@` `+    (dest / "STAGED-CARD").write_text("x-card.md\n")`; `@@ -419,4 +419,0 @@` `-def test_cs1_control_two_card_copies_are_refused(job):` `-    refused_untouched(job, _two_card_copies)` and two blank lines; `@@ -483,6 +479,0 @@` `-def test_fr1_control_two_same_job_check_cards_are_refused(job):` with its 3-line body and two blank lines; `@@ -527,0 +519 @@` `+    (dest / "STAGED-CARD").write_text(other.name + "\n")`; `@@ -535,0 +528,135 @@` the appended block. No assertion edited. Grep (`git show|[0-9a-f]{8}|agy-trial|/Users/`) over the file → hits at `:3`, `:4` (the module docstring), `:55`, `:85`, `:129`, `:138`, `:141` (`wt / "agy-trial" / …` under `tmp_path`): none in the appended block `:528-`; no commit hash, no `git show` of this repo, no real scratch path. M8 red (CL-2). X6: YES.

**F1** · from `/Users/cobalt/cobalt`: `git -C /Users/cobalt/cobalt diff --name-only --no-renames 79f6f2f3 b093f192` → `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. `git -C /Users/cobalt/cobalt diff --stat f2ca3e1a ops/band-routing-1015 -- ops tests src configs` → `ops/desk/bare-guard.py | 5 +` · `ops/desk/desk-launch.sh | 80 +++-` · `ops/desk/desk-watch.sh | 9 +-` · `ops/desk/preflight.sh | 26 +-` · `tests/ops/test_band_routing_1015.py | 904 ++++…` · `tests/ops/test_check_hub_shadow.py | 3 +-` · `6 files changed, 1015 insertions(+), 12 deletions(-)`. Hubs: `BUILD-HUB.md | 2 ++` · `CARD.md | 3 +++` · `CHECK-HUB.md | 4 ++--` · `SHADOW-HUB.md | 15 ++++++++++++---` · `4 files changed, 19 insertions(+), 5 deletions(-)`. No file in common. `git -C /Users/cobalt/cobalt log --oneline -1 ops/band-routing-1015` → `6c0ba560 …`; its worktree's `ops/desk` equals the branch (`git -C /Users/cobalt/cobalt-wt/band-routing-1015 diff --stat ops/band-routing-1015 -- ops/desk` → nothing); `grep -n -F "stage-set"` and `grep -n -F "STAGED-CARD"` over that worktree's `desk-launch.sh`, `desk-watch.sh`, `preflight.sh` → no hit (exit 1, empty). None. X8: YES. `git merge-tree`: not run (not on the allow line; `## DECISIONS`).

**R2** · `uv run cobalt jobs restarts 79f6f2f3..b093f192` →
```
path	change	rule	restart
ops/desk/stage-set.sh	M	operator script; no Cobalt reader	-
tests/ops/test_stage_set.py	M	test/documentation; no resident	-
RESTARTS: none
```
= the header (`none`).

**The whole file at the tip** · `uv run pytest -q -rA -p no:cacheprovider --color=no --tb=no -W ignore::DeprecationWarning tests/ops/test_stage_set.py` → 37 `PASSED` lines (each test of the file, named above) · `37 passed in 16.99s`.

### The findings
Both tests were appended to `tests/ops/test_stage_set.py` by Edit (no repair of form), run, then removed by Edit (the card fences every test edit: no test is committed); `git diff --stat b093f192 -- ops/desk/stage-set.sh tests/ops/test_stage_set.py` → nothing; `git status --short --branch` → `## ops/check-scratch-fr1`.

- O1 · Opus · on the tip `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_stage_set.py::test_a_card_basename_… tests/ops/test_stage_set.py::test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card` → O1 `.` (passed: the behaviour is right). With `:134` (`printf '%s\n' "$head" | grep -q '^HOUSE A:' || continue`) removed by Edit: `uv run pytest -q -p no:cacheprovider --color=no --tb=line -rf tests/ops/test_stage_set.py -k "not does_not_end_card_md"` → `1 failed, 37 passed, 1 deselected`: every one of the file's 37 tests green, only `FAILED tests/ops/test_stage_set.py::test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card`, `E   AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: the prior card copy is no version of a card on main under docs/40 - DevDocs/prompts` / `assert 1 == 0` (the build copy `05-…` taken as the prior card). Undone. · **HELD, NOT FIXED — tests/ops/test_stage_set.py** (the fix is this test added; the card fences any test edit).
- A1 · Grok · same run: `F` → `E   AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: the STAGED-CARD marker is not one card file name` / `assert 1 == 0` at `tests/ops/test_stage_set.py:675` (red for its stated reason). · **REJECTED — `## NOT IN THIS JOB`: "A folder staged before this deploy with no check card in `files/` at all refuses `no prior card copy` and the dest stays untouched: fails closed; named, not a finding"** — the same stance applies: the input fails closed (exit 1, dest untouched), BASE refused it too (its `find … -name '*-card.md'` finds no card → `no prior card copy`), and no launched card can be that input: `grep -n -F "the card must be" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` → `987:    *) refuse "the card must be $PROMPTS/<date>/<nn>-<job>-card.md" ;;` with `986:    "$PROMPTS"/*-card.md) ;;`. Stays OPEN (the desk settles it, or the fix round adds a `*-card.md` test at `:242`).

## FIXES
- O1: HELD, NOT FIXED — tests/ops/test_stage_set.py (the card's `## NOT IN THIS JOB` fences any test edit beyond an undone mutation; the fix is the O1 test of `## OWN FINDINGS`, verbatim, appended: green at the tip, red with `:134` removed).
No commit by this check.

## Suites
On the tip `b093f192` (no commit of this check). RESTARTS: `RESTARTS: none` (R2 above). DB: none card:
- (a0) `git diff --name-only --no-renames 79f6f2f3` → `docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md`, `docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.result`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`: every path `docs/`, `ops/` or `tests/ops/` → `cobalt_dev: not taken (DB: none — 4 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-fr1 offline --deploy-gate` · exit 0 · whole: `tests/ops: run (deploy gate)` · `offline 8393/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-fr1-offline-20261017-103218.log`. In the log: `888:4572 passed, 806 skipped, 1 xfailed, 36 warnings in 685.67s (0:11:25)`, `959:3821 passed, 1 xfailed, 16 warnings in 832.20s (0:13:52)`; `grep -c -F "OUTSIDE the allowed set" <log>` → `0`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-fr1 livenote` · exit 0 · `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-fr1-livenote-20261017-105803.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3821 passed, 1 xfailed, 16 warnings in 834.61s (0:13:54)` (= the build's `3821 passed, 1 xfailed`).
- `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stage_set.py tests/ops/test_scratch_clean.py` → `85 passed, 15 warnings in 21.85s` (= the build's `85 passed`).
- With-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/check-scratch-fr1/.env` → `No such file or directory` (never present; no lock taken).

## Scope
PREFLIGHT's path union `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`: both in the rows' `files`. This check committed nothing; its trial tests and mutations were all undone (`git diff --stat b093f192 -- ops/desk/stage-set.sh tests/ops/test_stage_set.py` → nothing; `git status --short --branch` → `## ops/check-scratch-fr1`). Throwaway tests lived only in the job scratchpad `/Users/cobalt/.claude/jobs/1eeacab5/tmp/`.

## Checked against the branch
(i) `git log --oneline b093f192..HEAD -- . ":(exclude)docs"` → nothing: no commit of this check; `<tip now>` = `b093f192`. (ii) `git log --stat --format=%h b093f192..HEAD` → `5f42c4f3` with the build report and its `.result` only (docs). (iii) `git log --oneline 79f6f2f3..HEAD -- ops/desk/scratch-clean.sh ops/desk/desk-watch.sh ops/desk/desk-launch.sh ops/desk/preflight.sh ops/desk/bare-guard.py tests/ops/test_band_routing_1015.py .claude src configs "docs/40 - DevDocs/prompts"` → nothing. (iv) no held finding was fixed or committed (O1 is HELD, NOT FIXED; the card fences test edits). (v) `ls …/.env` → `No such file or directory`; `git status --short --branch` → `## ops/check-scratch-fr1`. (vi) `git log --stat --format=%h 79f6f2f3..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no migration, no with-DB test; gate lists not involved. (vii) `git -C /Users/cobalt/cobalt log --oneline ops/check-scratch-fr1 -5` → `5f42c4f3`, `b093f192`, `0d52929f`, `79f6f2f3`, `caebf457`, as the record says; the card 583 diffs (F1) as the record says. (viii) L32: no ticker, price or date of his in this report; test paths are tmp paths.

## OPEN
- O1 · HELD, NOT FIXED — tests/ops/test_stage_set.py. Settled by the fix round appending the O1 test (`## OWN FINDINGS`, verbatim): green at the tip, red with `:134` removed.
- A1 · REJECTED (fail-closed and unreachable from a launch; see `## RUNS`). Settled by a desk `SETTLED` row, or by the fix round adding a `*-card.md` test before the marker write at `:242`.

## CONTINUE
next: none (CHECK DONE 11:12)

## DECISIONS
1. **O1 HELD, NOT FIXED — tests/ops/test_stage_set.py.** The tip's `prior_staging` writes `STAGED-CARD`, so `test_fr1_a_build_card_read_copy_does_not_block_the_clear` and `test_fr1_control_this_jobs_own_check_folder_shape` now run the marker branch. The legacy branch's build-copy filter `grep -q '^HOUSE A:' || continue` (`ops/desk/stage-set.sh:134`) is pinned by no test: with it removed, the whole file stays `37 passed`. The fix is one test, `test_o1_legacy_a_higher_numbered_build_copy_is_not_the_prior_card` (`## OWN FINDINGS`, verbatim), green at the tip and red with `:134` removed (`the prior card copy is no version of a card on main …`). The card fences test edits, so it goes to the builder's ONE fix round (his R438). Default taken: not fixed here; `ready: NO`.
2. ASK DESK: a `git merge-tree` dry run of this branch with card 583's (`ops/band-routing-1015`) is not on the allow line and was not run. F1 shows by `git diff --stat` that the two path sets share no file, and that nothing in card 583's three scripts names `stage-set` or `STAGED-CARD`. Default taken: no merge dry run. [11:12]
3. ASK DESK (the build's DECISION 1, D1): a same-JOB check card whose name starts with no digit ranks `0`, below every numbered card. Confirmed in code and by one hand run. Recommendation: keep `0`; every real card name starts with a number, and `desk-launch.sh:986` admits only `<nn>-<job>-card.md` shapes. Default kept. [11:12]

## RECORDS
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/check-scratch-fr1 status --short --branch` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (S0's command; the same answer came from `git status --short --branch` in `<WT>`).
- House B: Gemini probe `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS). Not needed on this card (`HOUSE B: as needed`); per X9 a harness record, not a finding.
- Dropped findings: none. No house produced nothing.
- No lock taken; no `.env` at any step. No commit by this check: the trial tests (A1, O1) and the BASE revert / mutations M1–M8 / the O1 mutation were made by Edit and undone by Edit, each undo proved by `git diff --stat b093f192 -- ops/desk/stage-set.sh` (and `tests/ops/test_stage_set.py`) printing nothing. Throwaway files: `/Users/cobalt/.claude/jobs/1eeacab5/tmp/test_retired_bodies.py`, `test_d1_no_digit.py`, `test_cl2_stderr.py`.
- The report and its `.result` sit on `main`'s working tree uncommitted. The desk commits them (`## REPORT`: "the desk commits it"); this session types no git write outside `<WT>`.
- The gate scripts (`gate.sh offline --deploy-gate`, `gate.sh livenote`) ran while the tree was at the tip; no Edit was made during either run.
- files opened: 13. Read: `CHECK-HUB.md`, card 690, `BUILD-HUB.md` (`:33-94`), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` on), the build report (`:118-166`), `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`, `<S>/house-a.md`; the task outputs of the house probe, the Grok run, the offline gate and the live-note gate, and the `tests/ops` run (tail). Greps beyond those: the R17/R19 rows, BUILD-HUB and build-report headings, cobalt.md headings, `desk-launch.sh` (`:986-987`), card 583's three scripts, the gate log.
- Check of `check-scratch-fr1`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: check-scratch-fr1 · pass: 1 · tip: b093f192 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8393/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 248568
