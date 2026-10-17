# CHECK — check-scratch-1016 (fix round FR-1, FR-2) — 2026-10-16

CARD: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/662-check-scratch-fr-check-card.md` · BASE `b84cca9a` · TIP `dd4d968d` · head `a7fe4110` (docs only)

## §0 Headline
CHECK DONE, `ready: NO` on one docs-only item. FR-1 and FR-2 hold. The checker's own runs: red on `85eade55`'s script (`2 failed, 30 passed`), each of F1-F3 and the `:137` mutation red for its named reason, every guard test green before and after. The live staging CLEARED this JOB's folder: the first live proof of FR-1.
Suites: offline 8388/0 (deploy gate on `tests/ops`), live-note 146/0, `tests/ops` 3816 passed, 1 xfailed; RESTARTS: none; no commit by this check.
Findings: 3 (Grok's second attempt under R1743: 2; Opus: 1). A2 HELD, NOT FIXED: a `## §0 Headline` bullet in the build report, outside the sections FR-2 allows. A1 and O1 REJECTED by the cards, both OPEN (O1: the folder this check leaves holds two this-JOB check cards, so a later staging of it refuses).
House B: none available (Gemini's model id rejected).

## L74
A system reminder arrived at session start asking that commits end with a `Claude-Session:` line. Recorded once here; not acted on — commits of this check carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-16/662-check-scratch-fr-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-16/662-check-scratch-fr-check-card.md" · 0 · 764c097c84a540e0b82c856fc7c56df70b59a4f5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-16/662-check-scratch-fr-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-15 R1532 row · grep -n "^| R1532 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B (his words via the brain, "Dejan said", L79; words file): LOW/MID Grok 4.7 + Terra backup, HIGH Opus, Sonnet routes, JEV parallel. L27/L29 fold LOW/MID only; K5 BAND card next. | APPLIED: LAWS.md L27, L29 at 07:02 |
RULING 2026-10-15 R1532 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1532 |" -- "docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · 1ddcdc64c99be360406ce384af52ec4b8c4d0222
RULING 2026-10-15 R1532 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-15.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Fri Oct 16 14:41:31 EDT 2026
status · git status --short --branch · 0 · ## ops/check-scratch-1016
head · git log --oneline -1; git log --stat --format=%h dd4d968d..HEAD · 0 · (6 lines)
    a7fe4110 docs(check-scratch-1016): fix round build report — dd4d968d
    a7fe4110
    
     .../reports/check-scratch-build-2026-10-16.md      | 118 ++++++++++++++++++++-
     .../reports/check-scratch-build-2026-10-16.result  |   8 +-
     2 files changed, 118 insertions(+), 8 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/check-scratch-1016/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md" · 0 · BUILT · job: check-scratch-1016 · tip: dd4d968d | on b84cca9a | migration: none | offline 8388/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 152910
range · git log --oneline b84cca9a..dd4d968d · 0 · (5 lines)
    dd4d968d fix(check-scratch-1016): stage-set picks the prior check card by CHECK REPORT and HOUSE A and this JOB; the JOB test pinned (FR-1, FR-2, L1, L3)
    a370ecce wip(check-scratch-1016): FR-1 red
    0605334f docs(check-scratch-1016): build report — 85eade55
    85eade55 fix(check-scratch-1016): stage-set clears a fix round's check by the one prior card copy (CS-1, L1, L3)
    3f0fd60e wip(check-scratch-1016): red
PREFLIGHT OK
```
THE RANGE typed, `git log --stat --format=%h b84cca9a..dd4d968d` · exit 0:
```
dd4d968d  ops/desk/stage-set.sh | 30 ++++…  tests/ops/test_stage_set.py | 21 +++…  2 files changed, 47 insertions(+), 4 deletions(-)
a370ecce  tests/ops/test_stage_set.py | 76 …  1 file changed, 75 insertions(+), 1 deletion(-)
0605334f  .../reports/check-scratch-build-2026-10-16.md | 178 …  .../reports/check-scratch-build-2026-10-16.result | 15 …  2 files changed, 193 insertions(+)
85eade55  ops/desk/stage-set.sh | 12 +++++++-----  tests/ops/test_stage_set.py | 5 +++--  2 files changed, 10 insertions(+), 7 deletions(-)
3f0fd60e  tests/ops/test_stage_set.py | 103 …  1 file changed, 103 insertions(+)
```
Path union: `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`, `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md`, `.result`.
DB: none — `git diff --name-only --no-renames b84cca9a..dd4d968d` · exit 0 · whole:
```
docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md
docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.result
ops/desk/stage-set.sh
tests/ops/test_stage_set.py
```
every path under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` · exit 0 · `diff.md  files  house-a.md  HOUSE-INSTRUCTIONS.md  rulings.md` — present: the FIRST check's staging of this JOB (card 648), which the card's row LIVE names as the folder this check's staging clears. Not a RECOVERY (the launch message carries no `CONTINUE:`); recorded.

HOUSE PROBES (`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"`, background, exit 0), lines whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
Gemini: OUT (HARNESS — the model name is not recognized; no return time named). No `HOUSE A: OpenAI` header line → Sol not probed. Seat: `house A: grok · house B: none (not needed)` (card `HOUSE B: as needed`; MANDATORY rule does not apply).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check"` · exit 1 · output whole:
```
REFUSED: the dest is not empty: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check — not cleared: no prior card copy: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/662-check-scratch-fr-check-card.md
```
Nothing staged. The cause, by tool output:
- `grep -n -F "no prior card copy" /Users/cobalt/cobalt/ops/desk/stage-set.sh` → `109:    [ -f "$copied" ] || { miss="no prior card copy: $copied"; return; }`; Read of `main`'s `:108` → `copied="$dest/files/$(basename "$card")"`: the BASE rule (a copy named after THIS card), not the branch's FR-1 rule.
- `git -C /Users/cobalt/cobalt log --oneline -3 -- ops/desk/stage-set.sh` → `d166b30e fix(stage-set-clear-1012): …`, `d483a417 …`, `8f3c4876 …`: no commit of this branch on `main`.
- `ls <S>/files` after the refusal (untouched): `633-band-routing-check-card.md 638-band-routing-fr-check-card.md 641-check-scratch-card.md 648-check-scratch-check-card.md band-routing-check-fr1-2026-10-16.md check-scratch-build-2026-10-16.md wt`.
Row LIVE / X5: the staging REFUSED (quoted above). The card counts that as a finding; the hub (`## 1`) counts it as `FAILED: copy`. It is caused by the script on `main` being the BASE version, not by the branch's FR-1.

AFTER `CONTINUE: 1` (Sat Oct 17 07:27 EDT; `main`'s script = the tip's, see `## RECORDS`), the same call · exit 0 · output whole:
```
cleared: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check (prior check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-check-2026-10-16.md)
18001 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/diff.md
25872 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/662-check-scratch-fr-check-card.md
34663 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/check-scratch-build-2026-10-16.md
20118 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/wt/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md
221 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/wt/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.result
11009 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/wt/ops/desk/stage-set.sh
22739 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/files/wt/tests/ops/test_stage_set.py
363 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/rulings.md
STAGED 8 files · 132986 bytes · commits 4
```
`commits 4` against PREFLIGHT's range of 5: `git log --oneline b84cca9a..dd4d968d -- . ":(exclude)docs"` → `dd4d968d`, `a370ecce`, `85eade55`, `3f0fd60e` (4); the fifth, `0605334f`, touches `docs/` only (PREFLIGHT's range stat), so the docs-excluded `diff.md` cannot hold it. The diff is complete for what it covers (`## DECISIONS` 2).
Then `stage-copy.sh`, one call each (the files `## READ` / `## ROWS` name that the script cannot derive), every line `COPIED`:
```
COPIED 27774 …/files/641-check-scratch-card.md
COPIED 25986 …/files/check-scratch-check-2026-10-16.md
COPIED 29708 …/files/cto-2026-10-16.md
COPIED 21921 …/files/648-check-scratch-check-card.md
COPIED 22754 …/files/638-band-routing-fr-check-card.md
COPIED 7277 …/files/wt/ops/desk/scratch-clean.sh
COPIED 18621 …/files/wt/tests/ops/test_scratch_clean.py
COPIED 12098 …/files/wt/src/cobalt/jobs/restarts.py
COPIED 43599 …/files/CHECK-HUB.md
```
(`…` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check`.)
`ls <S>/files` after both: `638-band-routing-fr-check-card.md 641-check-scratch-card.md 648-check-scratch-check-card.md 662-check-scratch-fr-check-card.md CHECK-HUB.md check-scratch-build-2026-10-16.md check-scratch-check-2026-10-16.md cto-2026-10-16.md wt`. The `ls` was taken AFTER the READ copies: the `638-`, `641-`, `648-` copies present are this check's `stage-copy.sh` copies (the `COPIED` lines above), not survivors; `633-band-routing-check-card.md` and `band-routing-check-fr1-2026-10-16.md` (not re-copied) are gone, and `stage-set.sh`'s own list holds no `633-`/`638-`/`641-`/`648-` file. Row LIVE: the clear ran (`cleared:` first, `STAGED ` last).
`<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the `Files:` paragraph (Write, 26509 bytes by `ls -la`).
House launch: `date` → `Sat Oct 17 07:29:37 EDT 2026`; gates R17 (`35:| R17 | 07:32 ET | …`), R19 (`37:| R19 | 07:36 ET | …`), `5055151dbf68899b82de5b11f99733ed2d03048c`; `cd <AGY>`; GROK started (background, timeout 2700000) with the hub's line for `check-scratch-1016`; house B: none (not needed); `cd <WT>`; `git status --short --branch` → `## ops/check-scratch-1016`.

## OWN FINDINGS
Read for `## 2` (at the tip; `ops/desk/stage-set.sh` = `git show dd4d968d:` by the empty `git -C /Users/cobalt/cobalt diff --stat dd4d968d -- ops/desk/stage-set.sh` and the clean worktree): `ops/desk/stage-set.sh` whole, `tests/ops/test_stage_set.py` whole, the build report `:121-290`, the card 641 lines matching `HOUSE A:` (`grep -n -F`, `:21`, `:31`, `:32`, `:36`, `:40`, `:60`, `:71`: no line STARTS `HOUSE A:`, so its READ copy carries no header pair).

FINDING O1
ROW: FR-1 (X2, X5)
CLAIM: a fix-round check stages a READ copy of the first check card of the same JOB (card 662 `## READ` names `648-check-scratch-check-card.md`; this check's `stage-copy.sh` put it beside `662-…`), so the folder then holds TWO this-JOB check cards with the pair and `ops/desk/stage-set.sh:132` refuses the next staging of that JOB's folder (`more than one prior card copy`) — the shape this check leaves in `check-scratch-1016-check` now.
RUN: TEST — `tests/ops/test_stage_set.py`
```python
def test_o1_a_read_copy_of_the_first_check_card_does_not_block_the_next_clear(job):
    wt, repo, job_wt, base, tip, card, env, dest = job
    prior_staging(job, change=False)
    second = fr_card(job)
    done = stage(env, second, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    # the fix round's check stage-copies the first check card for its READ, as card 662 does with 648
    (dest / "files" / card.name).write_bytes(card.read_bytes())
    write(repo / CHECK_B, "# check b\n")
    third = card.parent / "05-x-job-third-card.md"
    third.write_text(second.read_text().replace(
        f"CHECK REPORT: {repo / CHECK_B}", f"CHECK REPORT: {repo / 'docs/40 - DevDocs/reports/x-job-check-c.md'}"))
    git(repo, "add", "--", CHECK_B, str(third.relative_to(repo)))
    git(repo, "commit", "-q", "-m", "check b on main, a third card")
    done = stage(env, third, dest)
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines()[0] == f"cleared: {dest} (prior check {repo / CHECK_B})"
```
EXPECT: on the tip `assert done.returncode == 0` fails at the second `stage`, stderr `REFUSED: the dest is not empty: <dest> — not cleared: more than one prior card copy in <dest>/files`.

## Findings
HOUSE A GROK, `date` at its notice → `Sat Oct 17 07:37:57 EDT 2026`; task exit 0; `ls -la <S>` → no `house-a.md` (`diff.md files HOUSE-INSTRUCTIONS.md rulings.md` only). Its stdout, whole (the task output file):
```
I'll read the house instructions in full and follow them exactly.The instructions confine this check to the copied files. I'll start with the scope diff and read each row's sources in the required order.The two report copies disagree outside the sections the row allows. I'll diff them and keep checking the selection logic.

[exited with code 0]
```
No list, no `FINDINGS:` line → house A grok: NO FINDINGS LINE (produced nothing, `## 3`). The next house in the order, Gemini, was OUT at PREFLIGHT; re-probed at `## 3`: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (background) · exit 0 · lines whole:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
Grok has sat (one attempt); Gemini is OUT (HARNESS); no `HOUSE A: OpenAI` header line, so Sol is never seated. No house UP that has not sat → the seat is `none produced`; no house produced a list → `FAILED: 3` (the last line).

HOUSE A GROK, ATTEMPT 2 (R1743, committed `d8bdf960`): started 07:42 EDT; `date` at its notice → `Sat Oct 17 07:54:08 EDT 2026`; exit 0; stdout whole: `I'll read the house instructions first and follow them exactly.The instructions confine me to reading the copied files and writing runnable findings. I'll start with the scope row and the tip script.The report’s JOB-test line number does not match the tip script. I’ll record that finding before reading anything else./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check/house-a.md` then `[exited with code 0]`. `ls -la <S>` → `house-a.md` 1744 bytes, 07:54; its last line `FINDINGS: 2`. House B: N/A (R1743; Gemini OUT).
THE DROP: `grep -n -F "RUN:"` over `house-a.md` → `:4`, `:10`; each is followed by one command line beginning `grep` / `git diff`. None dropped.

| id | house | row | claim (≤30 words) | form |
|---|---|---|---|---|
| A1 | grok | FR-2 | The build report's M5 clause (`:151`), headline (`:7`) and fix-round self-check (`:261`) name the JOB test `:115`; on the tip it is `:137`, and `:115` is the loop's empty-name `continue`. | COMMAND |
| A2 | grok | FR-2 | `git diff 0605334f a7fe4110` of the build report adds a `## §0 Headline` bullet (`:7`), a change outside the sections the row allows. | COMMAND |
| O1 | opus | FR-1 | A fix-round check's READ copy of the first check card of the same JOB leaves two this-JOB check cards in `files/`; `:132` then refuses the next staging. | TEST |

## Dropped
none (house A grok: 2 blocks, both with a runnable `RUN:`).

## RUNS
### The findings
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus | the test pasted at the end of `tests/ops/test_stage_set.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stage_set.py::test_o1_a_read_copy_of_the_first_check_card_does_not_block_the_next_clear` | `1 failed, 15 warnings in 1.86s`; first failing line `tests/ops/test_stage_set.py:553: AssertionError` with `E       AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: more than one prior card copy in …/x-job-check/files` | REJECTED — card 662 `## ROWS` WHY: "the prior check card is the one stage-copied `*-card.md` carrying `CHECK REPORT:` and `HOUSE A:` with this JOB (…; 0 or ≥2 refuse)"; row SC1: "two check cards of one JOB in one folder is a refusal, not a choice". Red for the stated reason; the rule says the refusal is right. The test was removed again by Edit; `git diff --stat dd4d968d -- tests/ops/test_stage_set.py ops/desk/stage-set.sh` → nothing. OPEN |
| A1 | grok | `grep -n -F -e ":115" -e "the prior card copy's JOB is not" -e '[ -n "$f" ]' "docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md" ops/desk/stage-set.sh` (as written) | report `:7` "FR-2 pins the JOB test `:115` (G1)"; `:151` "…does not pin the JOB test `:115`; … (fix round FR-2: `:115` removed alone → this test red, …)"; `:261` "red under the `:115` mutation"; `:214`, `:219` (the F3 row, the mutation line quoted whole); `ops/desk/stage-set.sh:115:        [ -n "$f" ] \|\| continue`, `:137:    [ "$(field JOB "$copied")" = "$name" ] \|\| { miss="the prior card copy's JOB is not $name"; return; }`, `:234:    [ -n "$f" ] \|\| continue` | REJECTED — card 641 row FR-2 (the build's card): "A test pins the JOB test `ops/desk/stage-set.sh:115`" and "(`:115` removed alone → this test red, quoted from the run below)". The report labels the line as its card did (`:115` at `85eade55`); the mutation itself is quoted whole at `:219`, and this check ran it at the tip (`:137`, below). The label is stale against the tip, as the house says; the card it answers prescribes it. OPEN |
| A2 | grok | `git diff -U0 0605334f a7fe4110 -- "docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md"` | first hunk `@@ -6,0 +7 @@` `+- FIX ROUND (tip `dd4d968d`): FR-1 picks the prior check card by `CHECK REPORT:` + `HOUSE A:` + this JOB, so READ copies no longer block the clear (O1). FR-2 pins the JOB test `:115` (G1). offline 8388/0, live-note 146/0, `tests/ops` 3816 passed.` — inside `## §0 Headline`; the other hunks: `@@ -150 +151 @@` (the self-check (1) paragraph), `@@ -163,0 +165,104 @@` (`## FIX ROUND`), `@@ -165 +270 @@` (`## CONTINUE`), `@@ -168 +273 @@` (`## DECISIONS`), `@@ -175,0 +281,3 @@` (`## RECORDS`), `@@ -178 +286,3 @@` (the stop line) | HELD, NOT FIXED — `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md`. The output shows one hunk outside the sections card 662 FR-2 allows (`## §0 Headline` `:7`), as the house states; card 641 FR-2: "no other word of the report changes". The build report is in no `files` column of card 662 (its FR-2 files: `tests/ops/test_stage_set.py`, `ops/desk/stage-set.sh`, read only), so no fix here. (A docs-only bullet; it also repeats A1's `:115` label.) |

### The card's rows
- **S0** — `git diff --name-only --no-renames 85eade55 dd4d968d` → `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md`, `….result`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. The two docs paths are the first build's report commit `0605334f`, which sits inside `85eade55..dd4d968d`; the non-docs paths are exactly the two the row names. `git diff --stat dd4d968d a7fe4110 -- . ":(exclude)docs"` → nothing. `git diff --name-only --no-renames b84cca9a a7fe4110` → the same four paths. `git diff --stat b84cca9a a7fe4110 -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → nothing. No `src/`, `configs/`, `.claude/`, hub or `CARD.md` path. `git diff 85eade55 dd4d968d -- ops/desk/stage-set.sh` → two hunks: `@@ -5,7 +5,7 @@` (the header `:8`: `-# fifo, .git or .env anywhere in it; its one files/*-card.md a version of a card on main under docs/40 - DevDocs/prompts,` / `+# … its one files/*-card.md whose header carries CHECK REPORT: and HOUSE A: and whose JOB is this JOB (else the lone such card of another JOB) a version of a card on main …`) and `@@ -106,9 +106,31 @@` (from `copied=""` through `copied=${mine%?}`, inside `clearable()`). No hunk outside. HOLDS.
- **GD / X1** — `git diff -U0 85eade55 dd4d968d -- tests/ops/test_stage_set.py` → `@@ -78 +78 @@ def job(tmp_path):` with the ONE `-` line `-        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"` and `+        "HOUSE A: grok\nTREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"`; then `@@ -440,0 +441,95 @@` (appended: the FR-1 comment, `build_card_copy`, `other_job_check_cards`, the three `test_fr1_…`, the FR-2 comment and test). No assertion edited.
  (a) the script set to `85eade55`'s by Edit (`clearable()` hunk and header line restored; `git diff --stat 85eade55 -- ops/desk/stage-set.sh` → nothing), `uv run pytest -q -p no:cacheprovider --color=no -rA --tb=line tests/ops/test_stage_set.py` → exit 1, `2 failed, 30 passed, 15 warnings in 12.23s`; PASSED: `test_c1_a_recheck_clears_its_own_prior_staging`; `test_c2_c9_a_dest_that_fails_a_test_is_refused_and_untouched[c2-foreign-file-kwargs0-_foreign_file]`, `[c3-prior-report-untracked-kwargs1-None]`, `[c4-prior-report-off-main-kwargs2-None]`, `[c5-symlink-kwargs3-_symlink_in_wt]`, `[c6-dot-env-kwargs4-_env_in_wt]`, `[c7-dot-git-kwargs5-_git_dir_in_files]`, `[c8-card-copy-edited-kwargs6-_card_copy_one_byte]`, `[c9-prior-is-this-check-kwargs7-None]`; `test_c10_a_range_refusal_comes_before_the_clear`; `test_c11_another_jobs_folder_is_not_cleared`; `test_c12_the_script_removes_only_by_its_two_rm_rf_lines`; `test_cs1_a_fix_rounds_check_clears_the_first_passes_folder`; `test_cs1_control_two_card_copies_are_refused`, `…_a_prior_copy_of_another_job_is_refused`, `…_a_prior_copy_that_is_no_prompts_card_is_refused`, `…_the_second_pass_with_the_same_check_report_is_refused`, `…_a_foreign_file_blocks_the_clear`, `…_no_prior_card_copy_is_refused`; also `test_fr1_control_two_same_job_check_cards_are_refused` and `test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob`. FAILED: `test_fr1_a_build_card_read_copy_does_not_block_the_clear`, `test_fr1_control_this_jobs_own_check_folder_shape`.
  (b) undone by Edit (`git diff --stat dd4d968d -- ops/desk/stage-set.sh` → nothing); the same command → `32 passed, 15 warnings in 12.63s`, every name above PASSED.
  The build report's GUARD list (`### FR-1 — red on the tip`) names the same tests (c1, c2-c9 ×8, c10, c11, c12, cs1_a, the six cs1 controls). No existing test is green only after both changes. X1: yes.
- **FR-1 / X2** — re-read at the tip (`ops/desk/stage-set.sh` = `dd4d968d`'s): `:108` `copied=""`, `:109` `all=""`, `:110` the guarded `find … -name '*-card.md'`, `:114-128` the loop (`:116` `sed '/^$/q'`, `:117` `^CHECK REPORT:`, `:118` `^HOUSE A:`, `:119-125` the JOB split), `:130` THE FALLBACK, `:131` none, `:132` count, `:133` `copied=${mine%?}`, `:134-136` hash and version test, `:137` JOB test, `:138-145` as at `85eade55`. RED ON THE PREVIOUS TIP: (a) above, `2 failed, 30 passed`: `tests/ops/test_stage_set.py:476` and `:508`, both `AssertionError: REFUSED: the dest is not empty: …/x-job-check — not cleared: more than one prior card copy in …/x-job-check/files` / `assert 1 == 0`. CONTROL (i) `test_fr1_control_two_same_job_check_cards_are_refused` PASSED on both scripts. CONTROL (ii) `test_fr1_control_this_jobs_own_check_folder_shape`: red at `:508` (its clear half) on the old script, so its refuse half (`:497-504`) passed there; PASSED on the tip.
  Mutations by this check, each by Edit, each undone by Edit with `git diff --stat dd4d968d -- ops/desk/stage-set.sh` → nothing after it; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_stage_set.py`:
  (F1) `:118` removed → `2 failed, 30 passed, 15 warnings in 12.09s`: `test_fr1_a_build_card_read_copy_does_not_block_the_clear` (`:476`) and `test_fr1_control_this_jobs_own_check_folder_shape` (`:508`), both `… not cleared: more than one prior card copy in …/files`.
  (F2) `:119` → `if true; then` → `1 failed, 31 passed, 15 warnings in 12.52s`: `test_fr1_control_this_jobs_own_check_folder_shape` (`:508`), `more than one prior card copy`.
  (F3) `:130` removed → `1 failed, 31 passed, 15 warnings in 12.89s`: `test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` (`:533`), `assert "the prior card copy's JOB is not x-job" in 'REFUSED: … not cleared: no prior card copy: …/files/*-card.md\n'`.
  A lone other-JOB check card is handed to the JOB test and refused: F3 shows the fallback is what carries it there. X2: yes on every clause.
- **FR-2 / X3** — the test (`:518-535`) read: a `y-job` card with `CHECK REPORT: …CHECK_A` and `HOUSE A: grok` asserted (`:523`), committed by `git add`/`commit` (`:524-525`) under `prompts/2026-01-02/` of the tmp repo, the first copy unlinked (`:526`), its bytes the SOLE `*-card.md` (`:527`); asserts exit 1, the `REFUSED:` start, `the prior card copy's JOB is not x-job`, no `cleared:`, `snapshot` equal. GREEN with the line (GD (b), `32 passed`). `:137` removed alone by Edit → `1 failed, 31 passed, 15 warnings in 12.90s`: `FAILED tests/ops/test_stage_set.py::test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob`, `E   AssertionError: cleared: …/x-job-check (prior check …/repo/docs/40 - DevDocs/reports/x-job-check-a.md)`, `assert 0 == 1`, `tests/ops/test_stage_set.py:531`. The copy passed the version test: the run CLEARED, which `:135-136` would have refused. CONTROL `test_cs1_control_a_prior_copy_of_another_job_is_refused` PASSED under the same mutation (the run's only failure is the test above): the version test refuses its edited copy first. Undone; `git diff --stat dd4d968d -- ops/desk/stage-set.sh` → nothing. The M5 clause (`:151`) names this test and the mutation, with the label `:115` (A1). Hunks of `git diff 0605334f a7fe4110` outside the allowed sections: `@@ -6,0 +7 @@` (`## §0 Headline`, A2). X3: yes, with A1 and A2.
- **SC1 / X4** — (i) `:50-54`: `*..*|*/./*|*/.)` refused, `"$SCRATCH"/?*)` admitted, anything else refused. (ii) `:97` `[ "$dest" = "$SCRATCH/tribunal-bars-0920/$name-check" ]`. (iii) `grep -n -F "rm -r" ops/desk/stage-set.sh` → `173:    rm -rf "$dest"`, `180:    rm -rf -- "$dest"`; `git show b84cca9a:ops/desk/stage-set.sh` holds `    rm -rf "$dest"` in `fail()` and `    rm -rf -- "$dest"` in the clear, text identical; `grep -c -F -e "git clean" -e "-delete" ops/desk/stage-set.sh` → `0`. (iv) the loop and `$all`/`$mine`/`$others` only read (`sed`, `grep -q`, `field`); nothing removes a single file. (v) `find` prints each name on one line; `-name '*-card.md'` matches a name with a space whole (`IFS= read -r` keeps it); a name with a newline is split into two partial paths, each a missing file, so `sed` fails, the `grep -q` tests fail, the piece is skipped: it can only lower `mine`, which falls to a refusal (`no prior card copy`) or, with the real copy present, to the one real card; the clear removes `$dest` only. RUN: `test_c11_another_jobs_folder_is_not_cleared`, `test_fr1_control_this_jobs_own_check_folder_shape`, `test_c12_the_script_removes_only_by_its_two_rm_rf_lines` PASSED (GD (b)). What the script cannot prove: a JOB value with a `/` is not checked like WORKTREE (`:78`), but `:97` equates the whole `dest`, already held under `$SCRATCH/` by `:50-54`; and two check cards of one JOB in one folder is a refusal, not a choice (O1 shows a fix-round check leaves exactly that shape). X4: yes.
- **LIVE / X5** — `## Files copied`: `cleared: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check (prior check /Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-check-2026-10-16.md)` first, `STAGED 8 files · 132986 bytes · commits 4` last; `stage-set.sh`'s file list holds only `662-check-scratch-fr-check-card.md` of the card copies; `633-…` is gone. The `ls` after `## 1` shows `638-`, `641-`, `648-` because `## 1` re-copies the READ files (the `COPIED` lines). X5: yes — and the folder now holds `648-` and `662-` both (O1).
- **H1 / X6** — the first check's `## OPEN` (`check-scratch-check-2026-10-16.md:163-164`): "- G1 (grok): HELD, NOT FIXED — `tests/ops/test_stage_set.py`. Settled by the fix round adding the test under `## DECISIONS` (or an equivalent control whose card copy is a committed prompts card of another JOB), red with `:115` removed alone." → CLOSED by FR-2 (red with the JOB test removed alone, run above). "- O1 (opus-own): OUT OF SCOPE (`## NOT IN THIS JOB` 3rd bullet). Not counted as open." → CLOSED by FR-1 (the tests above and the live clear). The build-hub gap: `## RECORDS`.
- **X4 (fence)** — `git diff --stat 85eade55 dd4d968d -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py` → nothing. `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stage_set.py tests/ops/test_scratch_clean.py` → `80 passed, 15 warnings in 19.65s`. `grep -n -E -e "git show" -e "[0-9a-f]{8}" -e "agy-trial" -e "/Users/" tests/ops/test_stage_set.py` → `:3`, `:4` (the docstring naming the real roots the env vars stand in for), `:55`, `:85`, `:129`, `:138`, `:141` (`agy-trial` under the fixture's `tmp_path` `wt`); no hit in `:443-535`: no hash, no `git show`, no real path in the round's lines. The new tests use the `job` fixture's tmp repo and tmp `COBALT_WT_ROOT` only.
- **R2** — `uv run cobalt jobs restarts b84cca9a..dd4d968d` → `path change rule restart` / `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md A DOCS -` / `….result A DOCS -` / `ops/desk/stage-set.sh M operator script; no Cobalt reader -` / `tests/ops/test_stage_set.py M test/documentation; no resident -` / `RESTARTS: none`. Equals the header `RESTARTS: none`.
- **X7** — this Opus session is the check; house A grok wrote commands only (two `COMMAND` blocks); no house ran a keyed call that this check saw; house B N/A (R1743). No re-check follows (L75).

## FIXES
- A2: HELD, NOT FIXED — `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md` (outside card 662's `files`).
No `fix(check-scratch-1016):` commit and no `wip(check-scratch-1016): check red` commit: no held finding has a test to commit.

## Suites
On the tip `dd4d968d` (no commit of this check), DB: none, `BUILD-HUB.md` `## W` (a0), (a), (e), `--deploy-gate` on (a):
- RESTARTS: `uv run cobalt jobs restarts b84cca9a..HEAD` → `docs/…/check-scratch-build-2026-10-16.md A DOCS -`, `….result A DOCS -`, `ops/desk/stage-set.sh M operator script; no Cobalt reader -`, `tests/ops/test_stage_set.py M test/documentation; no resident -`, `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames b84cca9a` → `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md`, `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.result`, `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`; every path under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 offline --deploy-gate` → exit 0, whole:
```
tests/ops: run (deploy gate)
offline 8388/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-offline-20261017-075817.log
```
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh check-scratch-1016 livenote` → exit 0, whole:
```
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/check-scratch-1016-livenote-20261017-075818.log
```
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `3816 passed, 1 xfailed, 16 warnings in 899.71s (0:14:59)` (the build's count).
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/check-scratch-1016/.env` → No such file (before the gate and at close, 08:40 EDT).

## Scope
PREFLIGHT's path union (`ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`, the build report and its `.result`) plus this check's commits: none. Both code paths are in card 641's row `files` (FR-1, FR-2); the docs paths are the build's report. Every mutation and the O1 test were undone (`git diff --stat dd4d968d -- tests/ops/test_stage_set.py ops/desk/stage-set.sh` → nothing, after each).

## Checked against the branch
(i) `git log --oneline dd4d968d..HEAD -- . ":(exclude)docs"` → nothing: no commit of this check; `<tip now>` = `dd4d968d`.
(ii) `git log --stat --format=%h dd4d968d..HEAD` → `949cb071` (`…/check-scratch-build-2026-10-16.md | 5 +++--`) and `a7fe4110` (the report and `.result`): docs only. No WIDENED.
(iii) `git log --oneline b84cca9a..HEAD -- ops/desk/scratch-clean.sh tests/ops/test_scratch_clean.py .claude CARD.md "docs/40 - DevDocs/prompts"` → nothing.
(iv) no HELD finding with a test (A2 is a docs hunk); nothing to grep.
(v) `ls <WT>/.env` → No such file; `git status --short --branch` → `## ops/check-scratch-1016` alone.
(vi) `git log --stat --format=%h b84cca9a..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing: no migration, no with-DB test; no gate-list line owed.
(vii) card `## RECORDS`: `git -C /Users/cobalt/cobalt log --oneline -6 ops/check-scratch-1016` → `949cb071`, `a7fe4110`, `dd4d968d`, `a370ecce`, `0605334f`, `85eade55` (the record read `a7fe4110` as head; `949cb071` is a docs commit above it, the build report correction of 06:27 EDT); `git -C /Users/cobalt/cobalt diff --stat dd4d968d a7fe4110 -- ops tests` → nothing, as recorded. The records' `ls` of the live folder is superseded by this check's clear (`## Files copied`). The records' `ls-tree` and `rev-parse` commands are not on this check's list; not run.
(viii) L32: this report holds no ticker, price or date of his; the values are commit ids, paths and test names.

## OPEN
- O1 (opus): REJECTED — card 662 WHY ("0 or ≥2 refuse") and row SC1 ("a refusal, not a choice"). The test is red: a fix-round check stage-copies the first check card of the same JOB for its `## READ`, so the folder it leaves holds two this-JOB check cards, and the next staging of that JOB's folder refuses. `check-scratch-1016-check` holds `648-` and `662-` now. What would settle it: a ruling that a fix-round check's folder is never staged again (L75: no re-check), or a card that changes the rule (e.g. the copy named after the card being staged is excluded). FOLLOW-UP.
- A1 (grok): REJECTED — card 641 FR-2 names the JOB test `:115` and its mutation "`:115` removed alone". The build report's `:115` labels (`:7`, `:151`, `:261`) are stale against the tip, where the JOB test is `:137` (this check ran that mutation). Settled by a fix-report line that relabels them, or a `SETTLED: A1 — R<n>`.
- A2 (grok): HELD, NOT FIXED — `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md`: a `## §0 Headline` bullet (`:7`) added in the fix round, outside the sections card 662 FR-2 allows. Docs only; no code or test is affected. Settled by the builder's fix round (`FIXED: A2 — …` / `CARRIED: A2 — …`), per the deploy gates' rule.
- SETTLED: A2 — R1759, brain 2026-10-17 (L79): docs-only text in a build report of a deployed card; no fix job. Answer: `reports/check-662-and-583-fr2-decisions-2026-10-17.md` item 1.
- SETTLED: A1 — R1759, brain 2026-10-17 (L79): stale line labels in a report; cards and tests find lines by content. Answer item 2.
- O1: carried to a fresh K5 job `check-scratch-fr1` from main (R1759, answer item 3).

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. ASK DESK: the hub's staging runs `/Users/cobalt/cobalt/ops/desk/stage-set.sh` (on `main`), which is still the BASE `clearable()`. Under that rule `<S>` (the first check's staging: four card copies, none named `662-…`) can never be cleared, so `## 1` cannot run until either (a) the branch's `stage-set.sh` is on `main`, or (b) the desk empties `<S>` by its own means. The card says no hand `rm` and no hand retry, so I did neither. Safe default taken: stop at `## 1`, change nothing, wait for `CONTINUE: 1. <fact>` [Fri Oct 16 14:41 EDT]. If (b) is chosen, row LIVE cannot prove FR-1 live in this check; it would go under `## OPEN` as FOLLOW-UP (the first live clear comes after the deploy). ANSWERED by the desk's `CONTINUE: 1` ((a): card 641 deployed as `9c36df59`), verified under `## RECORDS`; closed.
2. ASK DESK: `stage-set.sh` printed `commits 4`; PREFLIGHT's range `b84cca9a..dd4d968d` holds 5 commits, one (`0605334f`) docs-only, which the docs-excluded diff of `## 1` (1) cannot hold. Read as: the diff is complete (4 = the range's non-docs commits, by `git log --oneline b84cca9a..dd4d968d -- . ":(exclude)docs"`). Safe default taken: go on; recorded [Sat Oct 17 07:27 EDT].
3. ASK DESK: no house produced a list. Grok ran its one attempt and ended with three sentences of progress text and no list (quoted under `## Findings`). Gemini is OUT on a harness error that will not clear by waiting (the model name `gemini-3.1-pro-high` is not recognized by `agy`). The hub gives Grok one attempt and no second, so I did not start it again. To go on, the desk can (a) fix the Gemini model name in the hub and probe, then send `CONTINUE: 3` (Gemini sits as house A), or (b) record a ruling that lets Grok try a second time, or (c) get his per-case `HOUSE A: none — overruled <date> R<n>` on the card, so this Opus seat checks alone. Safe default taken: stop at `## 3`, change nothing, no second attempt [Sat Oct 17 07:38 EDT]. The `<S>` staging, `HOUSE-INSTRUCTIONS.md` and O1 stand for any of these.
   UPDATE 07:39 EDT: the desk sent `CONTINUE: 3 … relaunch Grok once as house A`, backed by R1743 (DESK RECORD, uncommitted). Not followed (`## RECORDS`). What would let me go on: R1743, or a row of his granting Grok a second attempt on this check, COMMITTED on `main` (then `CONTINUE: 3` again and I verify it by `git log -S`); or the card header line `HOUSE A: none — overruled <date> R<n>`, committed, so the Opus seat checks alone (R1743's "2nd miss" clause has the same need). FOR DEJAN if the desk reads the second attempt or the overrule as his.
   ANSWERED 07:42 EDT: R1743 committed (`d8bdf960`); Grok's second attempt produced `FINDINGS: 2`. Closed.
4. HELD, NOT FIXED — A2: the build report `docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md:7` (`## §0 Headline`) gained a fix-round bullet, a hunk outside the sections card 662 FR-2 allows (`git diff -U0 0605334f a7fe4110`, `@@ -6,0 +7 @@`). Docs only; the code and the tests are unaffected. Outside card 662's `files`, so not fixed here. It goes to the builder's fix round on this card, or to a `CARRIED`/`SETTLED` row. Default taken: not fixed; `ready: NO` by the count rule.
5. OPEN, FOLLOW-UP — O1 (REJECTED): the folder a fix-round check leaves holds two this-JOB check cards (`check-scratch-1016-check` holds `648-` and `662-` now), so `stage-set.sh` will refuse the next staging of this JOB's check folder (`more than one prior card copy`). L75 means no re-check of this JOB is planned. Default taken: no change. If one is ever staged, the desk clears the folder by its own means or a card changes the rule.
6. OPEN — A1 (REJECTED): the build report labels the JOB test `:115` (its card 641's number at `85eade55`); at the tip it is `:137`. Docs only. Default taken: no change.

## RECORDS
- `ls <S>` at PREFLIGHT: present (the first check's staging of this JOB), not a RECOVERY.
- Gemini probe OUT: `error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`.
- H1 note (card row H1): `preflight.sh build` printed `FAILED PREFLIGHT: status` on the fix-round relaunch (build report `## DECISIONS` 1) — the desk's, recorded only.
- files opened (first session, before `CONTINUE: 1`): 4 (CHECK-HUB.md, the card, the task output of the probe, `main`'s `ops/desk/stage-set.sh` `:88-127`). The final count is below.
- CONTINUED at 1 Sat Oct 17 07:27:06 EDT 2026. The desk's fact ("card 641 deployed as 9c36df59 and main stage-set.sh now has FR-1"), verified: `grep -c -F "more than one prior card copy" /Users/cobalt/cobalt/ops/desk/stage-set.sh` → `1`; `git -C /Users/cobalt/cobalt log --oneline -3 -- ops/desk/stage-set.sh` → `dd4d968d …`, `85eade55 …`, `d166b30e …`; `git -C /Users/cobalt/cobalt diff --stat dd4d968d -- ops/desk/stage-set.sh` → nothing (main's script = the tip's). The prior check report on main: `git -C /Users/cobalt/cobalt log --oneline -2 -- "docs/40 - DevDocs/reports/check-scratch-check-2026-10-16.md"` → `764c097c docs(desk): check card 662 drafted, first check report on main, …`. RECOVERY: `git status --short --branch` → `## ops/check-scratch-1016`; `git log --oneline -5` → `949cb071`, `a7fe4110`, `dd4d968d`, `a370ecce`, `0605334f`; `ls -la <WT>/.env` → No such file; `ls <S>` → `diff.md files house-a.md HOUSE-INSTRUCTIONS.md rulings.md` (the first check's); `ls <S>/files` → `633-band-routing-check-card.md 638-band-routing-fr-check-card.md 641-check-scratch-card.md 648-check-scratch-check-card.md band-routing-check-fr1-2026-10-16.md check-scratch-build-2026-10-16.md wt`. NOTE: the branch head is now `949cb071` (a docs commit above `a7fe4110`; PREFLIGHT re-checks it at `## 1`'s copy count only).
- House A grok: NO FINDINGS LINE (07:29–07:37 EDT; stdout quoted under `## Findings`). Gemini: OUT, re-probe 07:38 EDT, the same harness line as PREFLIGHT.
- The card's row LIVE asks for `ls <dest>/files` "after" with no `638-`/`641-`/`648-` copy; the hub's `## 1` re-copies READ files with `stage-copy.sh` right after `stage-set.sh`, so an `ls` after `## 1` holds this check's own READ copies of them. Proof of the clear here is `stage-set.sh`'s own file list and the absent `633-` copy.
- No commit (nothing changed in `<WT>`: `git status --short --branch` → `## ops/check-scratch-1016`); `ls <WT>/.env` → No such file; no lock taken.
- files opened: 16 (CHECK-HUB.md, the card, the PREFLIGHT probe output, `main`'s `stage-set.sh` `:88-127`, this report, the worktree's `stage-set.sh`, `tests/ops/test_stage_set.py`, the build report `:121-290`, the Grok attempt-1 output, the `## 3` probe output, the Grok attempt-2 output, `<S>/house-a.md`, `check-scratch-check-2026-10-16.md` `:162-167`, `BUILD-HUB.md` `:75-94`, the live-note gate output, the offline gate output).
- tokens at the stop line: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh f0b7ee8c` → `context 251749 of 400000 — ok` (above the desk's 250,000 line, reached at the last step).
- The result file: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-fr-check-2026-10-16.result`, written with the stop line; the desk commits it with this report.
- Check of `check-scratch-1016`: house A `grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

- CONTINUED at 3 Sat Oct 17 07:39:39 EDT 2026, on the message from `cto-desk`: "CONTINUE: 3. House B is N/A: the Gemini probe id gemini-3.1-pro-high is not recognized (the K5 probe-id defect, card pending); relaunch Grok once as house A." The FACT is verified: the `## 3` re-probe, `gemini: OUT — error: invalid model selection … gemini-3.1-pro-high is not recognized …`. THE INSTRUCTION is NOT followed: CHECK-HUB.md gives each house ONE attempt (`## 3`, `## THE FLOW AND THE SEATS`), and "never a second attempt of one house" is the hub's safe default; a `CONTINUE` message "never widens the job or grants anything" (UNATTENDED RULES (b)). The backing row: `grep -n -F "Grok" ".../reports/cto-2026-10-17.md"` → `7:| R1743 | 07:39 ET | DESK RECORD (brain, L79): check 662 CONTINUE at step 3, house B N/A (old Gemini id), Grok once; a 2nd miss = house A none, Opus findings stand. …| DESK RECORD |`; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1743 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md"` → nothing (NOT committed). Approval is proved by row and commit only (AUTHORIZATION, K23), and R1743 is a DESK RECORD, not his ruling; its "2nd miss = house A none" is the per-case overrule the hub reserves to him (`HOUSE A: none — overruled <date> R<n>` on the card header). Recorded; not followed.

- Dropped findings: none. Houses that produced nothing: grok attempt 1 (NO FINDINGS LINE, 07:29–07:37 EDT); gemini OUT at PREFLIGHT and at `## 3` (HARNESS, the model-name line).
- O1's test form: none repaired. It was pasted, run red, and removed (REJECTED tests are not kept, so the suites run on the tip's tests).
- A1's command ran as written (three `-e` patterns in one `grep -n -F` call); the hook did not block it.
- No lock taken (DB: none). No `REFUSED, not needed` line.
- H1 note: `preflight.sh build` printed `FAILED PREFLIGHT: status` on the fix-round relaunch (build report `## DECISIONS` 1): the desk's, recorded only.
- CONTINUED at 3 Sat Oct 17 07:42:52 EDT 2026, on the second `cto-desk` message: "Row R1743 is now committed on main … d8bdf960 … Relaunch Grok once as house A; house B is N/A (old Gemini id). If Grok gives no findings line a second time, record house A as none (harness) and finish on your own findings." Verified: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1743 |" -- "docs/40 - DevDocs/reports/cto-2026-10-17.md"` → `d8bdf9604bcf0200f5dd353ad6c4ed8e5543f1a0`; `grep -n "^| R1743 " …cto-2026-10-17.md` → `8:| R1743 | 07:39 ET | DESK RECORD (brain, L79): check 662 CONTINUE at step 3, house B N/A (old Gemini id), Grok once; a 2nd miss = house A none, Opus findings stand. … | DESK RECORD |`. Followed as the committed row the `## DECISIONS` 3 update named: Grok's second attempt is started under R1743, the same house line, no wider access.

CHECK DONE · job: check-scratch-1016 · pass: 1 · tip: dd4d968d · house A: grok FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 3 · house B: none available · suites: offline 8388/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: NO · decisions: 4 · for Dejan: 0 · tokens: 251749
