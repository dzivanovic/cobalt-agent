# Check — held-table-row-1011 (card 361)

## §0 Headline
- Check of `held-table-row-1011` at tip `0188faa1` (no commit of the check). House A was Grok (`FINDINGS: 0`). House B: none (card `as needed`).
- There were 5 own findings. None held. O3 and O5 are NOT HELD.
- O1, O2 and O4 are REJECTED by the card's THE READ, which counts any last cell that holds `**HELD**` and splits rows on `|`. All three are OPEN as follow-up.
- Suites, all 0 failed: offline 4199/0 · live-note 146/0 · `tests/ops` 3132 passed, 1 xfailed. `cobalt_dev` not taken (DB: none). RESTARTS: none. `ready: YES`.

## L74
- 2026-10-11 12:57 ET: a system reminder in this session asked commits to end with a `Claude-Session:` line. Recorded as data (L74); commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 ·
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/361-held-table-row-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/361-held-table-row-card.md" · 0 · a06a541f257e02938710056b5971f07a381eca4f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/361-held-table-row-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 25:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 "` → row 35 (STANDING `Bash(grok *)`); `grep -n "^| R19 "` → row 37 (four house strings standing); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 ·
```
clock · date · 0 · Sun Oct 11 12:57:24 EDT 2026
status · git status --short --branch · 0 · ## ops/held-table-row-1011
head · git log --oneline -1; git log --stat --format=%h 0188faa1..HEAD · 0 · (5 lines)
    6625875e docs(held-table-row-1011): build report — 0188faa1
    6625875e
    
     .../reports/held-table-row-build-2026-10-11.md     | 142 +++++++++++++++++++++
     1 file changed, 142 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/held-table-row-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../held-table-row-build-2026-10-11.md" · 0 · BUILT · job: held-table-row-1011 · tip: 0188faa1 | on 2f877800 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 142972
range · git log --oneline 2f877800..0188faa1 · 0 · (2 lines)
    0188faa1 fix(held-table-row-1011): the held-id read takes a table row whose last cell holds **HELD** (T1, L3, L72)
    9b335b87 wip(held-table-row-1011): red
PREFLIGHT OK
```
- THE RANGE: `git log --stat --format=%h 2f877800..0188faa1` → `0188faa1`: `ops/desk/deploy-card.sh | 7`, `ops/desk/deploy-step0.sh | 7`, `ops/desk/desk-launch.sh | 7` (15+, 6−); `9b335b87`: `tests/ops/test_deploy_card.py | 76`, `tests/ops/test_deploy_step0.py | 18`, `tests/ops/test_desk_launch_prechecks.py | 19` (104+, 9−). Path union: those six.
- DB: none: `git diff --name-only --no-renames 2f877800..0188faa1` → `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py` — all under `ops/` or `tests/ops/`.
- `ls <S>` · exit 1 · `No such file or directory` → fresh.
- House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · `grok: UP` / `gemini: UP`.
- Seats: house A: Grok · house B: none (not needed — card `HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 ·
```
18733 <S>/diff.md
12847 <S>/files/361-held-table-row-card.md
18303 <S>/files/held-table-row-build-2026-10-11.md
26796 <S>/files/wt/ops/desk/deploy-card.sh
35036 <S>/files/wt/ops/desk/deploy-step0.sh
92123 <S>/files/wt/ops/desk/desk-launch.sh
45298 <S>/files/wt/tests/ops/test_deploy_card.py
41226 <S>/files/wt/tests/ops/test_deploy_step0.py
63165 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py
370 <S>/rulings.md
STAGED 10 files · 353897 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/held-table-row-1011-check`; commits 2 = PREFLIGHT's range count.)
- `stage-copy.sh` → `COPIED 25999 <S>/files/install-shadow-hub-check-2026-10-11.md`; `COPIED 23609 <S>/files/317-held-closed-card.md`. `wc -c`: 25999 = 25999, 23609 = 23609 against the originals.
- `<S>/HOUSE-INSTRUCTIONS.md` (14595 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
- House A Grok started 12:58 ET (`date` 12:58:50 ET; gates R17 row 35, R19 commit `5055151d…` re-read); `cd` back, `git status --short --branch` → `## ops/held-table-row-1011`. House B: none (not needed).

## OWN FINDINGS
Written 2026-10-11 before any house list was opened. All tests go in `tests/ops/test_deploy_card.py` (fixtures `Desk`, `held_round`, `_fix_refused`, `TABLE_HEAD`, `FIXED_O1` already there).

FINDING O1
ROW: T1 (X2)
CLAIM: The table branch counts every `**HELD**` verdict (`ops/desk/deploy-card.sh:162-163`), while the bullet branch counts only `HELD, NOT FIXED` (`:161`); CHECK-HUB `## 4` writes `HELD` in `## RUNS` whether or not the check then fixed it, so a table-form check that held O1 (fixed by the check) and O2 (left unfixed, `held unfixed: 1`) is refused `lists 2`.
RUN: TEST
```python
def test_check_own_o1_a_table_row_held_and_fixed_by_the_check_is_counted(tmp_path):
    desk = Desk(tmp_path)
    rows = (TABLE_HEAD
            + "| O1 | own | `tests/x.py::test_o1`, alone | `1 failed` | **HELD** — red for its stated reason (constructed) |\n"
            + "| O2 | own | `tests/x.py::test_o2`, alone | `1 failed` | **HELD** — red for its stated reason (constructed) |\n")
    fixed, head, report = held_round(desk, lines=["FIXED: O2 — tests/x.py::test_o1"], runs_text=rows)
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: the check {desk.check['alpha']} lists 2 HELD, NOT FIXED row(s) under "
                 "## RUNS (O1 O2), its last line says 'held unfixed: 1'")
```
EXPECT: passes on the tip (the refusal stands): a check whose own fix closed O1 cannot ship its fix round for O2 in table form.

FINDING O2
ROW: T1 (X2)
CLAIM: A verdict `NOT HELD — … **HELD** …` counts as held (`ops/desk/deploy-card.sh:163`, `index(v, "**HELD**")` anywhere in the cell).
RUN: TEST
```python
def test_check_own_o2_a_not_held_verdict_quoting_bold_held_is_not_counted(tmp_path):
    desk = Desk(tmp_path)
    rows = TABLE_HEAD + ("| O1 | own | `tests/x.py::test_o1`, alone | `1 passed` | "
                         "NOT HELD — the house said **HELD**; green on the tip (constructed) |\n")
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=rows)
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: the check {desk.check['alpha']} lists 0 HELD, NOT FIXED row(s) under "
                 "## RUNS (none), its last line says 'held unfixed: 1'")
```
EXPECT: fails on the tip: `returncode == 0` where the refusal (1) was expected.

FINDING O3
ROW: T1 (X2)
CLAIM: The edges THE READ ignores (a leading space, a table row under `## OPEN`, a backtick id, a path id, a `**NOT HELD**` verdict, a one-cell row) — no test pins them (`tests/ops/test_deploy_card.py:809-873` holds none); if any counts, `lists 0` is not printed.
RUN: TEST
```python
@pytest.mark.parametrize("rows", [
    pytest.param("  | O1 | own | r | o | **HELD** — x (constructed) |\n", id="leading space"),
    pytest.param("## OPEN\n| O1 | own | r | o | **HELD** — x (constructed) |\n", id="under OPEN"),
    pytest.param("| `O1` | own | r | o | **HELD** — x (constructed) |\n", id="backtick id"),
    pytest.param("| tests/x.py | own | r | o | **HELD** — x (constructed) |\n", id="path id"),
    pytest.param("| O 1 | own | r | o | **HELD** — x (constructed) |\n", id="space in id"),
    pytest.param("| O1 | own | r | o | **NOT HELD** — x (constructed) |\n", id="bold NOT HELD"),
    pytest.param("| **HELD** |\n", id="one cell"),
])
def test_check_own_o3_table_edges_count_no_held_id(tmp_path, rows):
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=TABLE_HEAD + rows)
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: the check {desk.check['alpha']} lists 0 HELD, NOT FIXED row(s) under "
                 "## RUNS (none), its last line says 'held unfixed: 1'")
```
EXPECT: a case fails with `returncode == 0` if that edge counts as a held id.

FINDING O4
ROW: T1 (X2)
CLAIM: A verdict cell holding a markdown-escaped pipe (`\|`) inside a code span is cut at that pipe (`ops/desk/deploy-card.sh:162`, `split($0, c, "|")`), so a real `**HELD**` verdict is missed.
RUN: TEST
```python
def test_check_own_o4_an_escaped_pipe_in_the_verdict_keeps_the_held_id(tmp_path):
    desk = Desk(tmp_path)
    rows = TABLE_HEAD + ("| O1 | own | `tests/x.py::test_o1`, alone | `1 failed` | "
                         "**HELD** — red: `a \\| b` (constructed) |\n")
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=rows)
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
```
EXPECT: fails on the tip: exit 1, stderr `lists 0 HELD, NOT FIXED row(s) under ## RUNS (none)`.

FINDING O5
ROW: X4
CLAIM: The new awk uses only POSIX awk (`split` with a one-character separator, `sub`, `index`); no `gensub` in the three scripts (`ops/desk/deploy-card.sh:160-163`).
RUN: COMMAND `grep -n -F "gensub" ops/desk/deploy-card.sh ops/desk/desk-launch.sh ops/desk/deploy-step0.sh`
EXPECT: a line printed if the claim is false; exit 1, no output if true.

## Findings
House A Grok finished 13:10 ET (`date` 13:10:04 ET; exit 0). `<S>/house-a.md` (12 bytes) reads exactly `FINDINGS: 0`. Grok's stdout: "The three scripts and the new tests match the row. No defect is pinned to a run." House B: none.
Kept: O1 · own · T1/X2 · table branch counts every `**HELD**`, so a check-fixed held row counts as unfixed · TEST
O2 · own · T1/X2 · `NOT HELD — … **HELD** …` verdict counts as held · TEST
O3 · own · T1/X2 · seven edge rows count no held id · TEST
O4 · own · T1/X2 · an escaped `\|` in the verdict cell hides `**HELD**` · TEST
O5 · own · X4 · no `gensub` in the three scripts · COMMAND

## Dropped
none

## RUNS
Each test was put in `tests/ops/test_deploy_card.py` with Edit and run as `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_card.py -k "test_check_own_o"` → `2 failed, 8 passed, 87 deselected, 15 warnings in 4.92s`.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `test_check_own_o1_a_table_row_held_and_fixed_by_the_check_is_counted` | passed: the refusal `lists 2 HELD, NOT FIXED row(s) under ## RUNS (O1 O2), its last line says 'held unfixed: 1'` stands on the tip | REJECTED — card THE READ: "the verdict … counts only when it holds the bold word `**HELD**`"; the table form has no `NOT FIXED` mark by the card's design. OPEN; test removed again |
| O2 | own | `test_check_own_o2_a_not_held_verdict_quoting_bold_held_is_not_counted` | `1 failed`: `AssertionError: deploy-card: … 03-deploy-x-set-card.md written (2 job(s), …)` / `assert 0 == 1` at `tests/ops/test_deploy_card.py:503` | REJECTED — red for its stated reason, but card THE READ counts a last cell that "holds the bold word `**HELD**`" anywhere. OPEN; test removed again |
| O3 | own | `test_check_own_o3_table_edges_count_no_held_id` (7 cases: leading space, under OPEN, backtick id, path id, space in id, bold NOT HELD, one cell) | `7 passed` | NOT HELD — every edge is ignored as THE READ says (X2 answered); test removed again |
| O4 | own | `test_check_own_o4_an_escaped_pipe_in_the_verdict_keeps_the_held_id` | `1 failed`: `REFUSED: alpha: the check … lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), its last line says 'held unfixed: 1'` / `assert 1 == 0` at `tests/ops/test_deploy_card.py:922` | REJECTED — red for its stated reason, but card THE READ says "split on `|`". OPEN; test removed again |
| O5 | own | `grep -n -F "gensub" ops/desk/deploy-card.sh ops/desk/desk-launch.sh ops/desk/deploy-step0.sh` | no output (exit 1) | NOT HELD — X4: the awk uses `split` (single-character separator), `sub`, `index` only; the suite ran it on macOS `/usr/bin/awk` |
After the removals: `git status --short --branch` → `## ops/held-table-row-1011` (tree at the tip). No HELD test, so no `wip(held-table-row-1011): check red` commit.
CHECK ASKS: X1 — `test_h1_the_rule_is_one_text_in_the_three_scripts` is in the offline suite (see `## Suites`); the diff carries the same three added lines in each script (`git diff 2f877800..0188faa1`). X2 — O2, O3, O4. X3 — one text (X1); the step0 and launch tests read the same table row green. X4 — O5.

## FIXES
none (no HELD finding).

## Suites
Tip `0188faa1` (no commit of the check). DB: none card, W as `BUILD-HUB.md` gives it: (a0), (a), (e), plus `tests/ops`.
- RESTARTS: `uv run cobalt jobs restarts 2f877800..HEAD` → 7 rows (the build report `DOCS`; three `ops/desk/*.sh` `operator script; no Cobalt reader`; three `tests/ops/*.py` `test/documentation; no resident`), last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 2f877800` → `docs/40 - DevDocs/reports/held-table-row-build-2026-10-11.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. `cobalt_dev: not taken (DB: none — 7 paths)`.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh held-table-row-1011 offline` · exit 0 → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/held-table-row-1011-offline-20261011-131057.log`
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh held-table-row-1011 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/held-table-row-1011-livenote-20261011-132142.log`
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → `3132 passed, 1 xfailed, 15 warnings in 596.05s (0:09:56)` (holds `test_h1_the_rule_is_one_text_in_the_three_scripts` and the build's T1 tests).
- `.env`: `ls /Users/cobalt/cobalt-wt/held-table-row-1011/.env` → `No such file or directory` (13:32 ET). The check took no lock.

## Scope
PREFLIGHT path union: `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_card.py`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`. All six are in T1's `files`. The check made no commit. No path to a score, rank, grade or size: the change is the operator scripts' held-id read only.

## Checked against the branch
- (i) `git log --oneline 0188faa1..HEAD -- . ":(exclude)docs"` → empty. No commit of the check; `<tip now>` = `0188faa1`.
- (ii) `git log --stat --format=%h 0188faa1..HEAD` → `6625875e`: only `.../reports/held-table-row-build-2026-10-11.md | 142 +` (docs).
- (iii) `git log --oneline 2f877800..HEAD -- configs src ops/desk/authorize.sh ops/desk/bare-guard.py ops/desk/install-fixed.sh "docs/40 - DevDocs/prompts"` → empty (the fence is untouched).
- (iv) No HELD finding, so no test to re-find.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/held-table-row-1011`.
- (vi) `git log --stat --format=%h 2f877800..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. No migration and no with-DB test, so `gate-lists.md` is not owed.
- (vii) Card record "the parsers of a held row": `grep -n -F "HELD, NOT FIXED" ops/desk/deploy-card.sh ops/desk/desk-launch.sh ops/desk/deploy-step0.sh` at the tip → awk `deploy-card.sh:161`, `desk-launch.sh:1042`, `deploy-step0.sh:165`; refusals `:177`/`:208`, `:1058`/`:1089`, `:181`/`:212`; comments `:141`, `:1022`, `:145`. That is the drafter's base lines moved by the build's added lines (+1 at the awk, +3 below it). This holds.
- (viii) L32: this report holds constructed test values only.

## OPEN
- O1 · REJECTED — card THE READ. A table-form check that held a finding and then fixed it still lists that id as **HELD**. With a second held, unfixed finding (`held unfixed: 1`) it is refused `lists 2`. The bullet form tells the two apart through `HELD, NOT FIXED`; the table form has no such mark. Would settle it: a card that also reads a fixed mark in the table form, or a CHECK-HUB rule that a table verdict reads `**HELD, NOT FIXED**` (a fixed file, his). FOLLOW-UP.
- O2 · REJECTED — card THE READ. A verdict `NOT HELD — … **HELD** …` counts as held: `index(v, "**HELD**")` matches anywhere in the cell. Would settle it: a card that requires the cell to *start* `**HELD**`. FOLLOW-UP.
- O4 · REJECTED — card THE READ ("split on `|`"). A markdown-escaped `\|` inside the verdict cell cuts the cell, and the held id is missed (the refusal reads `lists 0`). The real report `install-shadow-hub-check-2026-10-11.md:184` has no such pipe, so card 355's case reads right. Would settle it: a card that splits on unescaped `|` only. FOLLOW-UP.

## CONTINUE
next: done

## DECISIONS
none

## RECORDS
- Dropped findings: none. House A Grok wrote `FINDINGS: 0` (12 bytes, 13:09 ET). No house produced nothing.
- House B: none (not needed) — card `HOUSE B: as needed`; Gemini probed UP and was not seated. The stop line writes `none (not needed)`.
- The probe tests O1–O4 were added to `tests/ops/test_deploy_card.py` and removed again with Edit. The tree is back at the tip (`git status` clean).
- CHECK ASKS answered: X1 yes (the one-text pin is green in `tests/ops`; the diff adds the same three lines in each script; bullet-only tests `test_h1_*`/`test_h2_*`/`test_h3_*` and `test_t1_a_bullet_row_is_still_counted` are green). X2: O2, O3 and O4 (the seven edges in O3 are ignored as the card says; `NOT HELD — … **HELD** …` and an escaped pipe are OPEN). X3: one text, so no difference. X4: POSIX awk only (O5); the suites ran on macOS `/usr/bin/awk`. GNU awk was not run (no listed command for it).
- L74: one system reminder asked for a `Claude-Session:` line. It was not followed, and the check made no commit.
- files opened: 9 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); `ops/desk/deploy-card.sh:134-178`; `tests/ops/test_deploy_card.py` (`:590-679` and the imports); `reports/install-shadow-hub-check-2026-10-11.md:178-191`; the build report (`:91-128` and its last line); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `<S>/house-a.md`.
- Check of `held-table-row-1011`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: held-table-row-1011 · pass: 1 · tip: 0188faa1 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 137086
