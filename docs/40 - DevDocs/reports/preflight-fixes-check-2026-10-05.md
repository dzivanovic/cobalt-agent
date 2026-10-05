# preflight-fixes — check, pass 1 (2026-10-05)

## §0 Headline
- Pass 1 of `preflight-fixes`. House A: none (overruled 2026-10-05 R412). Opus checked alone.
- I wrote 6 findings. One held: O5. F1's recorded count was read from the first `self-check: ` in the line, not from the field the pattern matched. It is fixed in `0af97be7`, with its red in `70b664bd`.
- X1–X4 are answered by run: the diff holds only the two rows. `4 of 3` and another job's line fail `report`. Every last line except pass 1 with `house B: needed` keeps the card's TIP.
- Suites on `0af97be7`: offline 3786/0 · live-note 146/0 · `tests/ops` 1353 passed. RESTARTS: none. `.env` is absent.
- Open 0, house B not needed, ready: YES, decisions: 0.

## L74
A system reminder at session start asked that commits carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md" · 0 · eacb399e057fe3b4310681d80a4da03f7a61456f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-05/20-preflight-fixes-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
HOUSE A overruled 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
HOUSE A overruled 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (run although the card's HOUSE A is overruled; no house is launched):
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · exit 0 · one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (row 35)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · exit 0 · one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (row 37)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · exit 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`date` · exit 0 · `Mon Oct  5 14:09:29 EDT 2026`

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Mon Oct  5 14:09:35 EDT 2026
status · git status --short --branch · 0 · ## ops/preflight-fixes-1005
head · git log --oneline -1; git log --stat --format=%h 08cfc80e..HEAD · 0 · (5 lines)
    13b23d56 docs(preflight-fixes): build report — 08cfc80e
    13b23d56
    
     .../reports/preflight-fixes-build-2026-10-05.md    | 45 +++++++++++++++++++---
     1 file changed, 39 insertions(+), 6 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/preflight-fixes-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/preflight-fixes-1005/docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md" · 0 · BUILT · job: preflight-fixes · tip: 08cfc80e | on b56622fa | migration: none | offline 3786/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
range · git log --oneline b56622fa..08cfc80e · 0 · (5 lines)
    08cfc80e fix(preflight-fixes): brain hub title token asserted filled (F3, L77)
    faeb4749 docs(preflight-fixes): build report — desk row request recorded, not followed (BUILD-HUB (b))
    782b179a docs(preflight-fixes): build report — 48e572e0
    48e572e0 fix(preflight-fixes): self-check below 3 recorded; pass-2 head at pass 1's tip (F1, F2, L1, L72)
    bb81ecd7 wip(preflight-fixes): red
PREFLIGHT OK
```

THE RANGE, typed: `git log --stat --format=%h b56622fa..08cfc80e` · exit 0:
```
08cfc80e  tests/ops/test_desk_launch_brain.py | 2 +-
faeb4749  docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md | 1 +
782b179a  .../reports/preflight-fixes-build-2026-10-05.md | 133 +++
48e572e0  ops/desk/preflight.sh | 48 ++++++++++++++++++++++++++++++++++++++++--------
bb81ecd7  tests/ops/test_preflight.py | 68 +++++-
```
Path union: `ops/desk/preflight.sh`, `tests/ops/test_preflight.py`, `tests/ops/test_desk_launch_brain.py`, `docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md`. Commit count: 5.

DB: none: `git diff --name-only --no-renames b56622fa..08cfc80e` · exit 0:
```
docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md
ops/desk/preflight.sh
tests/ops/test_desk_launch_brain.py
tests/ops/test_preflight.py
```
Every path under `ops/`, `tests/ops/` or `docs/`.

`ls <S>` · exit 1 · `ls: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/preflight-fixes-check: No such file or directory` → fresh.

House: `house A: none (overruled 2026-10-05 R412)`. No house gate run as a seat gate, no probe (CHECK-HUB "NO OUTSIDE HOUSE").

## Files copied
none (house A: none).

## OWN FINDINGS
Read: the card; `git diff b56622fa..08cfc80e -- ops/desk/preflight.sh tests/ops/test_desk_launch_brain.py` and `-- tests/ops/test_preflight.py`; `ops/desk/preflight.sh` whole at the tip; `tests/ops/test_preflight.py` lines 1-340; `BUILD-HUB.md` lines 76-110; the build report from `## E0` to its last line; `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down. All tests below go in `tests/ops/test_preflight.py` and use only its fixtures and helpers (`job`, `built`, `write_card`, `preflight`, `last_line`, `commit`, `GOOD_LAST`, `PASS1_LAST`, `CHECK_REL`).

X1 (a quote, not a finding): `git diff b56622fa..08cfc80e -- ops/desk/preflight.sh` changes header lines 14-16 and 23-24, the check branch of the `head` row (tip lines 147-183) and the `report` row (tip lines 230-238). Nothing else in the file changed. The diff is quoted under `## RUNS` X1.

FINDING O1
ROW: F1 / X2
CLAIM: `ops/desk/preflight.sh:230` lets a last line with `self-check: 4 of 3` pass `report`.
RUN: TEST
```python
def test_x2_a_report_with_self_check_four_of_three_fails(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST.replace("self-check: 3 of 3", "self-check: 4 of 3"))
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: report"
```
EXPECT: if the claim is true, `assert 0 == 1` at the returncode line.

FINDING O2
ROW: F1 / X2
CLAIM: `ops/desk/preflight.sh:230` lets another job's last line with `self-check: 2 of 3` pass `report` and print the recorded line.
RUN: TEST
```python
def test_x2_another_jobs_report_below_three_fails_and_records_nothing(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST.replace("job: x-job", "job: y-job").replace("self-check: 3 of 3", "self-check: 2 of 3"))
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: report"
    assert "(recorded)" not in done.stdout
```
EXPECT: if the claim is true, `assert 0 == 1` at the returncode line.

FINDING O3
ROW: F2 / X3
CLAIM: `ops/desk/preflight.sh:154-167` reads a `tip:` from a CHECK REPORT last line that is not pass 1's `house B: needed` stop line of this job: an in-progress, a `RESUMED`, a `FAILED`, a `CONTINUE`, a pass-2 `CHECK DONE`, or another job's pass-1 line.
RUN: TEST
```python
@pytest.mark.parametrize("last", [
    "(run in progress — next step under ## CONTINUE)",
    "RESUMED: 4 14:00",
    "FAILED: 4 — x",
    "CONTINUE: 4. x",
    "CHECK DONE · job: x-job · pass: 2 · tip: {fix} · house B: needed · ready: NO",
    "CHECK DONE · job: y-job · pass: 1 · tip: {fix} · house B: needed · ready: NO",
])
def test_x3_a_check_report_not_pass_1_needed_keeps_the_card_tip(job, last):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    (job_wt / "src" / "a.py").write_text("A = 5\n")
    fix = commit(job_wt, "fix(x-job): pass 1")
    path = job_wt / CHECK_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# check\n\n{last.format(fix=fix)}\n\n")
    commit(job_wt, "docs(x-job): check report")
    write_card(card, job_wt, base, tip, check_report=str(job_wt / CHECK_REL))
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"
```
EXPECT: if the claim is true, `assert 0 == 1` for the case whose `tip:` was read.

FINDING O4
ROW: F2
CLAIM: real cards name `CHECK REPORT` under the main repo (`/Users/cobalt/cobalt/docs/…`, card line 8), not in the worktree; the F2 tests only place it in the worktree, and `ops/desk/preflight.sh:151-152` may not reach the main-repo file.
RUN: TEST
```python
def test_f2_a_pass_2_check_reads_a_check_report_in_the_main_repo(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    (job_wt / "src" / "a.py").write_text("A = 5\n")
    fix = commit(job_wt, "fix(x-job): pass 1")
    path = repo / CHECK_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# check\n\n{PASS1_LAST.format(fix=fix, house_b='needed')}\n\n")
    write_card(card, job_wt, base, tip, check_report=str(repo / CHECK_REL))
    done = preflight(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "PREFLIGHT OK"
```
EXPECT: if the claim is true, `assert 1 == 0` with `FAILED PREFLIGHT: head`.

FINDING O5
ROW: F1
CLAIM: `ops/desk/preflight.sh:232-233` takes `k` from the FIRST `self-check: ` in the line, while the glob at `:230` may have matched a later one; a line with an earlier `self-check: ` text prints a wrong recorded line (`report: self-check pending | self-check: 2 of 3 (recorded)`), and a `self-check: 3 of 3` line with an earlier `self-check: ` text prints a recorded line it should not.
RUN: TEST
```python
def test_f1_the_recorded_count_is_the_field_the_pattern_matched(job):
    wt, repo, job_wt, base, card, env = job
    last = GOOD_LAST.replace("rows: 1 of 1", "rows: 1 of 1 | note self-check: pending")
    tip = built(job_wt, last.replace("self-check: 3 of 3", "self-check: 2 of 3"))
    write_card(card, job_wt, base, tip)
    done = preflight(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "report: self-check 2 of 3 (recorded)" in done.stdout.splitlines()
```
EXPECT: if the claim is true, the last assertion fails; stdout holds `report: self-check pending | self-check: 2 of 3 (recorded)`.

FINDING O6
ROW: F2 / X3
CLAIM: `ops/desk/preflight.sh:163-165` (a pass-1 `house B: needed` line whose `tip:` is not hex) has no test; the build report's FOR THE CHECK X3 names it untested. If the empty reference fell through, `git log ..HEAD` could pass `head`.
RUN: TEST
```python
def test_x3_a_pass_1_line_whose_tip_is_not_hex_fails_head(job):
    wt, repo, job_wt, base, card, env = job
    tip = built(job_wt, GOOD_LAST)
    (job_wt / "src" / "a.py").write_text("A = 5\n")
    commit(job_wt, "fix(x-job): pass 1")
    path = job_wt / CHECK_REL
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# check\n\n{PASS1_LAST.format(fix='<tip now>', house_b='needed')}\n\n")
    commit(job_wt, "docs(x-job): check report pass 1")
    write_card(card, job_wt, base, tip, check_report=str(job_wt / CHECK_REL))
    done = preflight(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED PREFLIGHT: head"
```
EXPECT: if the claim is true, `assert 0 == 1` at the returncode line.

X4 (no separate test): every non-test line of the `preflight.sh` diff sits in the two rows the card names, and each carries a `card 20 F1` / `card 20 F2` comment citing `BUILD-HUB.md:97` / `CHECK-HUB.md:61` / `CHECK-HUB.md:120`. The usage line `:45` (`[ "$#" -eq 2 ]`) is unchanged, so there is no new argument. O1–O6 run the remaining clauses.

## Findings
none (house A: none).

## Dropped
none.

## RUNS
Each test was put in `tests/ops/test_preflight.py` with the Edit tool, exactly as written under `## OWN FINDINGS`, and run alone with `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_preflight.py::<test>` on `08cfc80e`. No test's form was repaired.

| id | source | run | output | verdict |
|---|---|---|---|---|
| X1 | card ask | `git diff b56622fa..08cfc80e -- ops/desk/preflight.sh` | three hunks only: `@@ -11,14 +11,17 @@` (the header `head` / `report` lines), `@@ -141,18 +144,41 @@` (the check branch of `head`), `@@ -201,9 +227,15 @@` (the `report` row). `:45` usage `[ "$#" -eq 2 ]` is unchanged | answered: yes |
| O1 | own | `::test_x2_a_report_with_self_check_four_of_three_fails` | `1 passed, 15 warnings in 1.08s` | NOT HELD (X2: `4 of 3` fails `report`); removed |
| O2 | own | `::test_x2_another_jobs_report_below_three_fails_and_records_nothing` | `1 passed, 15 warnings in 1.04s` | NOT HELD (X2: another job fails, nothing recorded); removed |
| O3 | own | `::test_x3_a_check_report_not_pass_1_needed_keeps_the_card_tip` (6 cases) | `6 passed, 15 warnings in 2.37s` | NOT HELD (X3: in-progress, RESUMED, FAILED, CONTINUE, pass-2 and other-job lines all keep the card's TIP); removed |
| O4 | own | `::test_f2_a_pass_2_check_reads_a_check_report_in_the_main_repo` | `1 passed, 15 warnings in 1.09s` | NOT HELD (a CHECK REPORT under the main repo is read); removed |
| O5 | own | `::test_f1_the_recorded_count_is_the_field_the_pattern_matched` | `1 failed, 15 warnings in 1.15s`; first failing line `tests/ops/test_preflight.py:452: AssertionError` on `assert "report: self-check 2 of 3 (recorded)" in done.stdout.splitlines()`; with `-vv` the script's stdout holds `report: self-check pending \| self-check: 2 of 3 (recorded)` and `PREFLIGHT OK` | HELD |
| O6 | own | `::test_x3_a_pass_1_line_whose_tip_is_not_hex_fails_head` | `1 passed, 15 warnings in 1.13s` | NOT HELD (X3: a non-hex `tip:` fails `head`); removed |

X4: answered by X1 and the `card 20 F1` / `card 20 F2` comments at tip lines 147-149 and 237. No new argument and no new command.
Red commit: `70b664bd wip(preflight-fixes): check red — O5` (`git diff --stat` before it: `tests/ops/test_preflight.py | 10 ++++++++++`).

## FIXES
| id | file | change | green | commit |
|---|---|---|---|---|
| O5 | `ops/desk/preflight.sh` (the `report` row, F1's file) | `k` is read from the line's LAST `self-check: ` (`${last##*self-check: }`, the stop line's field, `BUILD-HUB.md:106`), and `report` passes only when that field is `[0-3] of 3` | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_preflight.py` → `30 passed, 15 warnings in 6.26s` | `0af97be7 fix(preflight-fixes): self-check count read from the stop line's last field (check O5)` |

DevDocs line: none written. `docs/40 - DevDocs/cobalt/` has no page for `ops/desk/preflight.sh` (Grep `preflight.sh` there → `No files found`). The build recorded the same.

## Suites
On `<tip now>` = `0af97be7`. The card is DB: none, so W runs as `BUILD-HUB.md` `## W` (a0), (a), (e) gives it.
- RESTARTS: `uv run cobalt jobs restarts b56622fa..HEAD` → WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md	A	DOCS	-
ops/desk/preflight.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_brain.py	M	test/documentation; no resident	-
tests/ops/test_preflight.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames b56622fa` → `docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md` · `ops/desk/preflight.sh` · `tests/ops/test_desk_launch_brain.py` · `tests/ops/test_preflight.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. `cobalt_dev: not taken (DB: none — 4 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh preflight-fixes-1005 offline` (exit 0) → `offline 3786/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/preflight-fixes-1005-offline-20261005-141323.log`. Log line 829: `3786 passed, 756 skipped, 1 xfailed, 36 warnings in 629.43s (0:10:29)`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh preflight-fixes-1005 livenote` (exit 0) → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/preflight-fixes-1005-livenote-20261005-142406.log`. Its one SKIPPED line (log line 56) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (exit 0) → `1353 passed, 1 xfailed, 15 warnings in 350.57s (0:05:50)`. The build's run had 1352; the extra pass is the O5 test.
- with-DB: not run (DB: none). `cobalt_dev: not taken`.
- `.env`: `ls /Users/cobalt/cobalt-wt/preflight-fixes-1005/.env` → `No such file or directory`.

## Scope
PREFLIGHT path union: `ops/desk/preflight.sh` (F1, F2), `tests/ops/test_preflight.py` (F1, F2), `tests/ops/test_desk_launch_brain.py` (F3), and the build report (docs). My commits: `70b664bd` touches `tests/ops/test_preflight.py` (the test file of F1); `0af97be7` touches `ops/desk/preflight.sh` (F1's file, its `report` row only). Every path is in some row's `files`.

## Checked against the branch
- (i) `git log --oneline 08cfc80e..HEAD -- . ":(exclude)docs"` → `0af97be7 fix(preflight-fixes): self-check count read from the stop line's last field (check O5)` · `70b664bd wip(preflight-fixes): check red — O5`. `<tip now>` = `0af97be7`.
- (ii) `git log --stat --format=%h 08cfc80e..HEAD` → `0af97be7` `ops/desk/preflight.sh | 12 +++++++++---` · `70b664bd` `tests/ops/test_preflight.py | 10 ++++++++++` · `13b23d56` `.../reports/preflight-fixes-build-2026-10-05.md` (docs). Every non-docs path is in a row's `files`.
- (iii) The fence: `git log --oneline b56622fa..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → empty. `git log --stat --format=%h b56622fa..HEAD -- ops/desk` → only `ops/desk/preflight.sh` (`0af97be7`, `48e572e0`). No other `ops/desk/` file is touched.
- (iv) `grep -n -F "def test_f1_the_recorded_count_is_the_field_the_pattern_matched" tests/ops/test_preflight.py` → `389:def test_f1_the_recorded_count_is_the_field_the_pattern_matched(job):`. Its red commit `70b664bd` sits below its fix `0af97be7` in (i).
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch` → `## ops/preflight-fixes-1005` alone.
- (vi) `git log --stat --format=%h b56622fa..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. No migration and no with-DB test, so no gate-list change is owed.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C … log` command. Nothing to run.
- (viii) L32: this report holds only commit ids, paths, constructed test values and suite counts. It holds no ticker, price or date of his.

COUNTING: findings 6 (O1–O6; house A none) · dropped 0 · held 1 (O5) · fixed 1 · held unfixed 0 · open 0.

## OPEN
none.

## CONTINUE
next: none (closed)

## DECISIONS
none.

## RECORDS
- No house ran: the card carries `HOUSE A: none — overruled 2026-10-05 R412`, and `authorize.sh` proved that row. `## 1` and `## 3` were not run, and no probe was run.
- O1, O2, O3 (6 cases), O4 and O6 were NOT HELD. They answer X2 and X3 by run. Each was removed again with the Edit tool, per `## 4`. The F1 `4 of 3` and other-job cases, the X3 non-`needed` last lines and the non-hex `tip:` therefore have no test of their own on the branch.
- No `REFUSED, not needed`, no `CONTINUED`, no lock take.
- L74: the `Claude-Session:` request (a system reminder at session start) is recorded under `## L74` and was not acted on. `70b664bd` and `0af97be7` carry `Co-Authored-By` only.
- `opus-1.md` is written to `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/preflight-fixes-check/opus-1.md`. House B is not needed.
- files opened: 9 — `CHECK-HUB.md`, the card, `ops/desk/preflight.sh`, `tests/ops/test_preflight.py`, `BUILD-HUB.md` (lines 76-110 and its section headings by grep), the build report (from `## E0` to its last line, plus headings by grep), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down, headings by grep), and the two gate task outputs. `tests/ops/test_desk_launch_brain.py` was read through its diff only.
- Check of `preflight-fixes`, pass 1: house A `none (overruled 2026-10-05 R412)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: preflight-fixes · pass: 1 · tip: 0af97be7 · house A: none (overruled 2026-10-05 R412) · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0
