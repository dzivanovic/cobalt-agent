# CHECK — launcher-shadow-check-1011 (pass 1)

## §0 Headline
- The nine rows hold in code: no finding on `desk-launch.sh`, `preflight.sh`, `card-fill.sh`, `desk-done.sh` or the hub lines held. Suites on tip `a8c18242`: offline 4199/0, live-note 146/0, `tests/ops` 3197 passed. RESTARTS: none.
- Grok (house A) wrote 5 findings and I wrote 1, with nothing dropped. One held: the build report says the build adds 66 test cases, and the files collect 58. That fix lies in the build report, outside the rows' files, so it is HELD, NOT FIXED, and the check is `ready: NO` until the builder fixes the figure.
- Four rejected and open: PASS-2 still reads no build report, so a non-shadow `SHADOW BUILT` line passes on PASS-2 (O1, G4; "as today"); the `test_house_probe.py` pin moved (G1); and L9's F2 wording cannot hold on BASE (G5).
- My commits: none.

## L74
The session context carried a system notice asking that commits end with a `Claude-Session:` line. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md"` (exit 0):
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md" · 0 · 7f0b56baf92cfdf25dbe5c0605b9849be7b9e09a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-11/386-launcher-shadow-check-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
RULING 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row, line 35 (`| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` · `APPLIED: LAWS.md L62 …`).
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row, line 37 (`| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` · `APPLIED: LAWS.md L62 …`).
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`date` → `Mon Oct 12 06:12:26 EDT 2026`.
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` (exit 0):
```
clock · date · 0 · Mon Oct 12 06:12:32 EDT 2026
status · git status --short --branch · 0 · ## ops/launcher-shadow-check-1011
head · git log --oneline -1; git log --stat --format=%h a8c18242..HEAD · 0 · (5 lines)
    12ac16cb docs(launcher-shadow-check-1011): build report — a8c18242
    12ac16cb
    
     .../launcher-shadow-check-build-2026-10-11.md      | 62 ++++++++++++++++++----
     1 file changed, 51 insertions(+), 11 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/launcher-shadow-check-1011/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/launcher-shadow-check-1011/docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md" · 0 · BUILT · job: launcher-shadow-check-1011 · tip: a8c18242 | on a76d8855 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 9 of 9 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 273762
range · git log --oneline a76d8855..a8c18242 · 0 · (4 lines)
    a8c18242 fix(launcher-shadow-check-1011): CHECK-HUB line-count pin follows the four shadow lines (L2, L6, L8; L68)
    adc285b3 wip(launcher-shadow-check-1011): W — the RUN probe in docs/_inflight breaks PLACEMENT; no listed string removes it
    ba37c2a9 fix(launcher-shadow-check-1011): a shadow card's check launches on SHADOW BUILT and its one SHADOW-INSTRUCTIONS.md (L1, L2, L4-L9; L1, L3, L72)
    d71ff562 wip(launcher-shadow-check-1011): red
PREFLIGHT OK
```
THE RANGE, `git log --stat --format=%h a76d8855..a8c18242` (exit 0):
```
a8c18242
 tests/ops/test_house_probe.py | 2 +-
adc285b3
 .../launcher-shadow-check-build-2026-10-11.md      | 154 +++++++++++++++++++++
ba37c2a9
 docs/40 - DevDocs/prompts/CHECK-HUB.md |  4 ++++
 ops/desk/card-fill.sh                  | 11 +++++++++--
 ops/desk/desk-done.sh                  | 14 ++++++++------
 ops/desk/desk-launch.sh                | 26 ++++++++++++++++++++++----
 ops/desk/preflight.sh                  | 25 +++++++++++++++++++++++++
d71ff562
 tests/ops/test_card_fill.py             |  77 ++++++++++++++++++
 tests/ops/test_check_hub_shadow.py      |  90 +++++++++++++++++++++
 tests/ops/test_desk_done.py             |  42 ++++++++++
 tests/ops/test_desk_launch_prechecks.py | 137 ++++++++++++++++++++++++++++++++
 tests/ops/test_preflight.py             | 129 ++++++++++++++++++++++++++++++
```
Path union (for `## Scope`): the 12 paths below.
DB: none — `git diff --name-only --no-renames a76d8855..a8c18242` (exit 0):
```
docs/40 - DevDocs/prompts/CHECK-HUB.md
docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md
ops/desk/card-fill.sh
ops/desk/desk-done.sh
ops/desk/desk-launch.sh
ops/desk/preflight.sh
tests/ops/test_card_fill.py
tests/ops/test_check_hub_shadow.py
tests/ops/test_desk_done.py
tests/ops/test_desk_launch_prechecks.py
tests/ops/test_house_probe.py
tests/ops/test_preflight.py
```
Every path is under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` → `No such file or directory` (fresh).
House probe, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` (exit 0):
```
grok: UP
gemini: UP
```
No `HOUSE A: OpenAI` header line: Sol not probed. `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.
Build self-check: `self-check: 3 of 3`.

## Files copied
`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/launcher-shadow-check-1011-check`.
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` (exit 0):
```
35681 <S>/diff.md
21460 <S>/files/386-launcher-shadow-check-card.md
27780 <S>/files/launcher-shadow-check-build-2026-10-11.md
42186 <S>/files/wt/docs/40 - DevDocs/prompts/CHECK-HUB.md
20312 <S>/files/wt/docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md
4403 <S>/files/wt/ops/desk/card-fill.sh
2896 <S>/files/wt/ops/desk/desk-done.sh
93234 <S>/files/wt/ops/desk/desk-launch.sh
10924 <S>/files/wt/ops/desk/preflight.sh
9109 <S>/files/wt/tests/ops/test_card_fill.py
3696 <S>/files/wt/tests/ops/test_check_hub_shadow.py
7809 <S>/files/wt/tests/ops/test_desk_done.py
69265 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py
10952 <S>/files/wt/tests/ops/test_house_probe.py
24406 <S>/files/wt/tests/ops/test_preflight.py
370 <S>/rulings.md
STAGED 16 files · 384483 bytes · commits 3
```
`commits 3` against PREFLIGHT's 4: the diff is `git log -p <BASE>..<TIP> -- . ":(exclude)docs"`, and the fourth commit, `adc285b3`, touches the build report only (THE RANGE above). `git log --oneline a76d8855..a8c18242 -- . ":(exclude)docs"` → `a8c18242`, `ba37c2a9`, `d71ff562` (3); `grep -c "^commit " <S>/diff.md` → `3`; `grep -n -F "commit " <S>/diff.md` → `2:commit a8c18242…`, `24:commit ba37c2a9…`, `213:commit d71ff562…`. The diff is complete; see `## DECISIONS` 1.
`stage-copy.sh`, the files `## READ` names that the script does not derive:
- `COPIED 11448 <S>/files/wt/tests/ops/test_hub_lines.py`
- `COPIED 15934 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md`
- `COPIED 9707 <S>/files/366-shadow-strike-fallback-env-1010-sonnet-card.md`
- `COPIED 21304 <S>/files/strike-fallback-env-1010-sonnet-build-2026-10-11.md`
- `COPIED 33741 <S>/files/324-shadow-hub-card.md`
`<S>/HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
House A Grok started 06:15 ET (`date` → `Mon Oct 12 06:15:38 EDT 2026`; gates R17 line 35, R19 line 37, commit `5055151d…` re-run). House B: none (not needed). `git status --short --branch` after the return → `## ops/launcher-shadow-check-1011`.

## OWN FINDINGS
Written before either house list was opened. Read: the card, the diff `a76d8855..a8c18242` (code, tests, hub), the four scripts at the tip (`desk-launch.sh:1369-1440`, `preflight.sh:40-279`, `card-fill.sh` whole, `desk-done.sh` whole), the five test files' added tests, `test_desk_launch_prechecks.py:73-212, 223-228, 326-367`, card 366's header, the build report's `## RESTARTS`, `## W`, `## FOR THE CHECK` and last line.

FINDING O1
ROW: X1 (L1)
CLAIM: A PASS-2 `check` launch never reads the build report's last line (`ops/desk/desk-launch.sh:1411` `if [ -z "$pass2" ]`), so a NON-shadow card whose report ends `SHADOW BUILT · …` launches on PASS-2, the one path X1 names on which a non-shadow card's `SHADOW BUILT` line is accepted.
RUN: TEST — `tests/ops/test_desk_launch_prechecks.py`
```python
def test_check_386_o1_a_pass_2_on_a_non_shadow_card_refuses_its_shadow_built_line(desk):
    last = f"SHADOW BUILT · job: x-job · tip: {desk.tip} | on {desk.base}"
    desk.write_build_report(last)
    desk.check_report.write_text("# check\n\nCHECK DONE · job: x-job · pass: 1 · house B: needed\n")
    refused(desk, desk.launch("check", str(desk.card), "PASS-2"), f"not built — {last}")
```
EXPECT: `assert done.returncode == 1` fails (`0 == 1`): the PASS-2 launches.

Reading notes on the other asks (no runnable defect found, so no finding block):
- X2: the new `case` arms (`desk-launch.sh:1416`, `preflight.sh:263`) take the tip bare or followed by a space; `card-fill.sh:74` takes `[0-9a-f]{8}(?=\s|$)` and an exact JOB. The tests pin a TIP with a ninth digit and a JOB `x-jobber` on all three.
- X3: `git diff a76d8855..a8c18242 -- "docs/40 - DevDocs/prompts/CHECK-HUB.md"` adds four lines and changes none; the L2 line matches the card's text as read.
- X4: `desk-launch.sh:1428` and `preflight.sh:143` compare the whole porcelain output (desk-launch) or the one line under the branch line (preflight) to `?? SHADOW-INSTRUCTIONS.md`, and only with `shadow` set.

## Findings
House A Grok finished at 06:36 ET (`date` → `Mon Oct 12 06:36:21 EDT 2026`, exit 0). It wrote `<S>/house-a.md` itself (2683 bytes, `ls -la`) and printed only that path; its list ends `FINDINGS: 5`. House B: none (not needed).
- G1 · Grok · SCOPE · `tests/ops/test_house_probe.py:193` changed (123 → 127), a path in no row's files · COMMAND
- G2 · Grok · SCOPE · the build report blob at the tip ends `FAILED: W`, not the `BUILT` line · COMMAND
- G3 · Grok · L1 · the report claims 66 added cases across the four `test_386_` files; they collect 58 · COMMAND
- G4 · Grok · X1 · a non-shadow card's `SHADOW BUILT` line is accepted on PASS-2 (`desk-launch.sh:1411`) · TEST
- G5 · Grok · L9 · F2's two kind-`shadow` cases are red on BASE for `unknown kind`, not for the row's reason · COMMAND

## Dropped
none. Each `FINDING` block in `house-a.md` has a `RUN:` line followed by a test function or a command with an allowed beginning.

## RUNS
- O1 · own · `uv run pytest -q -rs -p no:cacheprovider --color=no "tests/ops/test_desk_launch_prechecks.py::test_check_386_o1_…"` (run with G4) · `2 failed`; first failing line `E       assert 0 == 1` (the PASS-2 launches: stdout `RUN: claude --bg "PASS-2. Read …`) · **REJECTED — row L1 "a `SHADOW BUILT` line on it is refused, as today" and `desk-launch.sh:1410` "a PASS-2 launch keeps the test it has"**: PASS-2 has never read the build report (`test_l2_a_pass_2_launch_keeps_the_test_it_has`, `:362`, launches on `FAILED: W — x`), and the card names a resume (A6), not a PASS-2, for this test. The test was removed with the Edit tool. OPEN.
- G4 · Grok · the same run (its test pasted as written, `shadow_built` from the file) · `2 failed`; `test_x1_pass2_of_a_non_shadow_card_accepts_a_shadow_built_line` `E       assert 0 == 1` · **REJECTED — the same card line as O1**. Test removed. OPEN.
- G1 · Grok · `git diff a76d8855..HEAD -- tests/ops/test_house_probe.py` · the hunk `-    assert len(lines) == 123` / `+    assert len(lines) == 127  # card 386 L2, L6 (two), L8: four shadow lines` · **REJECTED — rows L2, L6 and L8** add four lines to `CHECK-HUB.md`, so the 123-line pin of card 298 S1 has to move; CHECK-HUB `## 7` (ii) admits a test file outside the rows. The build's DECISION 2 names it. OPEN.
- G2 · Grok · `git show "HEAD:docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md"` · its last line is `BUILT · job: launcher-shadow-check-1011 · tip: a8c18242 | on a76d8855 | … | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 273762`, not `FAILED: W — …` · **NOT HELD**. Its copy under `files/wt/` is the blob at TIP `a8c18242`; the report was finished in the docs-only commit `12ac16cb` above TIP (PREFLIGHT `head`).
- G3 · Grok · `uv run pytest --collect-only -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py tests/ops/test_preflight.py tests/ops/test_card_fill.py tests/ops/test_desk_done.py -k 386` · first run `59/270 tests collected (210 deselected)`, which included my temporary O1 test; re-run after it was removed: `58/268 tests collected (210 deselected)`. The report line (`grep -n -F "66 cases"` → `140: … This build adds the 386 tests (66 cases across test_desk_launch_prechecks.py, test_preflight.py, test_card_fill.py, test_desk_done.py) and tests/ops/test_check_hub_shadow.py (4).`) is not what the files collect: 21 + 19 + 12 + 6 = 58; with the 4 hub tests, 62 = E2's `15 failed, 47 passed`. · **HELD**.
- G5 · Grok · `git show a76d8855:ops/desk/desk-done.sh` · line 2 `# desk-done.sh <session id> "<report>" <build|check|deploy|devfix|close> [<tab>]`, and the `case "$kind"` holds no `shadow)` arm · **REJECTED — row L9**: its own F1 says "RED on `BASE`: `REFUSED: unknown kind: shadow`", so any kind-`shadow` case is red on BASE for that reason; the build report (E2) names this and shows the case red for its own reason under the E3 mutation `^(SHADOW )?(BUILT|ROLE)`. OPEN.
No HELD finding has a test (G3 is a COMMAND), so no `wip(launcher-shadow-check-1011): check red` commit. `git status --short --branch` after the removals → `## ops/launcher-shadow-check-1011`.

## FIXES
- G3: **HELD, NOT FIXED — `docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md`** (the build report). It is not a file `## ROWS` names, and CHECK-HUB `## 5` fixes only inside the rows' files. No code changes; the fix is one figure, `66` → `58`, at `:140`. `## DECISIONS` 2.

## Suites
No commit of mine: the tip is the build's TIP `a8c18242` (HEAD `12ac16cb`, docs only above it). DB: none card, so W is (a0), (a), (e) and `tests/ops`, as `BUILD-HUB.md` `## W` gives it.
- RESTARTS: `uv run cobalt jobs restarts a76d8855..HEAD` → 12 rows (`CHECK-HUB.md` and the build report `DOCS`; the four `ops/desk/` scripts `operator script; no Cobalt reader`; the six `tests/ops/` files `test/documentation; no resident`), each `-`; last line **`RESTARTS: none`**.
- (a0) `git diff --name-only --no-renames a76d8855` → the 12 paths of PREFLIGHT, each under `ops/`, `tests/ops/` or `docs/` → **`cobalt_dev: not taken (DB: none — 12 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-shadow-check-1011 offline` (exit 0) → **`offline 4199/0`**, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-offline-20261012-063752.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-shadow-check-1011 livenote` (exit 0) → **`live-note 146/0`**, `log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-shadow-check-1011-livenote-20261012-063754.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (exit 0) → **`3197 passed, 1 xfailed, 15 warnings in 646.51s (0:10:46)`**; `grep -c -F "SKIPPED"` over its output → `0`.
- With-DB: not run (DB: none), `with-DB 0/0`; `cobalt_dev: not taken`.
- `.env`: `ls /Users/cobalt/cobalt-wt/launcher-shadow-check-1011/.env` → `No such file or directory` (06:50 ET); no lock was taken.

## Scope
PREFLIGHT's path union (12 paths) against the rows' `files`: `ops/desk/desk-launch.sh` (L1, L4), `ops/desk/preflight.sh` (L5, L6), `ops/desk/card-fill.sh` (L7), `ops/desk/desk-done.sh` (L9), `docs/40 - DevDocs/prompts/CHECK-HUB.md` (L2, L6, L8), `tests/ops/test_desk_launch_prechecks.py` (L1, L4), `tests/ops/test_preflight.py` (L5, L6), `tests/ops/test_card_fill.py` (L7), `tests/ops/test_desk_done.py` (L9), `tests/ops/test_check_hub_shadow.py` (L2, L6, L8), the build report (docs). Outside every row's files: `tests/ops/test_house_probe.py` (a test file; G1, the build's DECISION 2). The edits sit inside the fenced line ranges: `preflight.sh` hunks at BASE `:104-106` and `:127-131` (status block) and `:241` (report row); `card-fill.sh` at `:53` and `:64-71`; `desk-done.sh` at `:2-28`. The `CHECK-HUB.md` fence line ("beyond the one line of row L2") is overridden by rows L6 and L8, which name the file for three more lines; the diff adds exactly those four lines. My commits: none.

## Checked against the branch
- (i) `git log --oneline a8c18242..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `a8c18242`.
- (ii) `git log --stat --format=%h a8c18242..HEAD` → `12ac16cb`, `.../launcher-shadow-check-build-2026-10-11.md | 62 ++++++++++++++++++----` (docs only).
- (iii) `git log --oneline a76d8855..HEAD -- ops/desk/authorize.sh ops/desk/desk-watch.sh ops/desk/stage-set.sh ops/desk/stop-guard.py ops/desk/bare-guard.py ops/desk/job-clean.sh ops/desk/gate.sh ops/desk/deploy-card.sh ops/desk/deploy-step0.sh "…/SHADOW-HUB.md" "…/BUILD-HUB.md" "…/CARD.md" "…/STANDING-LIST.md" src` → empty.
- (iv) no HELD finding carries a test (G3 is a COMMAND).
- (vi) `git log --stat --format=%h a76d8855..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not involved.
- (vii) the card's `## RECORDS`: `ls -la /Users/cobalt/.claude/ops/desk-launch.sh` → `lrwxr-xr-x … /Users/cobalt/.claude/ops/desk-launch.sh -> /Users/cobalt/cobalt/ops/desk/desk-launch.sh` (as recorded); `ls -la /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet/.env` → `No such file or directory` (as recorded). The record's `grep -n BUILT|self-check|status` and `git -C …strike… status` are not typed: a `|` pattern and a `git -C <other worktree> status` are outside the listed forms (`## RECORDS`). The `tail -n 2` record: `tail -n 2 ".../strike-fallback-env-1010-sonnet-build-2026-10-11.md"` → `SHADOW BUILT · job: strike-fallback-env-1010-sonnet · tip: 813036e8 | on 8f4bbe28 | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: … | decisions: 4 · builder: claude-sonnet-5-5 · gate: strike-fallback-env-1010-sonnet-gate · passes: 2 · suites at first run: green · builder tokens: 273992 · wall: 1.2`, with no `self-check:` field (as recorded).
- (viii) L32: this report quotes constructed test values and the desk's job names and commit ids only; no ticker, price or trading date of his.

## OPEN
Follow-up items (no second pass):
1. G3 — HELD, NOT FIXED: the build report's `:140` says the build adds 66 cases across the four files; they collect 58. Settled by one edit of that figure in the build report, the builder's fix round (`## DECISIONS` 2).
2. O1 and G4 — REJECTED: a PASS-2 `check` launch never reads the build report's last line, so a non-shadow card ending `SHADOW BUILT` launches on PASS-2 (both tests red, `assert 0 == 1`). Settled by a ruling: either PASS-2 stays "as today" (CHECK-HUB says there is no PASS-2 any more, his R438), or a row makes the `not built` test cover it. Same path as the build's DECISION 3.
3. G1 — REJECTED: `tests/ops/test_house_probe.py:193` sits outside the rows' files. Settled by the desk accepting the build's DECISION 2, or by moving the pin into a row.
4. G5 — REJECTED: F2's kind-`shadow` cases cannot be green on BASE as row L9's F2 wording says, because kind `shadow` is unknown there (row L9's own F1 line). Settled by the drafter's reading of L9; no code change.

## CONTINUE
next: 8 (done)

## DECISIONS
1. ASK DESK: `stage-set.sh` printed `commits 3`, PREFLIGHT counted 4. The hub's diff command excludes `docs`, and the fourth commit (`adc285b3`) touches only the build report, so it can never appear in `diff.md`. Safe default taken: the copy is treated as complete (the three non-docs commits are proven above) and the house started. [06:15 ET]
2. HELD, NOT FIXED — G3, `docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md:140`. The report claims "66 cases" for the build's tests in four files, and `pytest --collect-only -k 386` collects 58 (`## RUNS`). This check may write only the rows' files, so it stays for the builder's one fix round on this card: change `66` to `58`. No code or test changes, and the suite totals stand (`3197 passed` again here). It makes this check `ready: NO`.
3. ASK DESK: the stop line's `house B:` field offers `<name> <line>` or `none available`. Neither fits this card: Gemini was UP, but `HOUSE B: as needed` seats no house B. Safe default taken: the field reads `none (not needed)`, the wording PREFLIGHT records. [06:50 ET]

## RECORDS
- Dropped findings: none.
- No house produced nothing: Grok produced `FINDINGS: 5`. House B was not seated (`HOUSE B: as needed`). Gemini was UP at the probe.
- Not typed, outside the listed forms (no refusal occurred): the card record's `grep -n BUILT|self-check|status` (a `|` pattern) and `git -C /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet status --porcelain --branch`. The card's RUN line `DESK_LAUNCH_DRY=1 sh …` is the builder's (a `VAR=` prefix, not listed).
- Temporary tests: O1 and G4 were pasted into `tests/ops/test_desk_launch_prechecks.py`, run, and removed with the Edit tool. `git status --short --branch` → `## ops/launcher-shadow-check-1011` after the removal and at the close.
- Lock: none taken (DB: none).
- L74: the session's system notice asking for a `Claude-Session:` commit line (see `## L74`). No commit was made.
- files opened: 13: `CHECK-HUB.md`; `BUILD-HUB.md` (`:1-40`, `:67-92`); the card 386; the build report (`:109-195`, then whole by `git show HEAD:`); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `ops/desk/desk-launch.sh` (`:1366-1445`); `ops/desk/preflight.sh` (`:40-279`); `ops/desk/card-fill.sh`; `ops/desk/desk-done.sh` (tip, and BASE by `git show`); `tests/ops/test_desk_launch_prechecks.py` (`:73-212`, `:223-228`, `:326-367`); card 366 (`:1-14`); 366's build report (`tail -n 2`); `<S>/house-a.md`. The diffs of the other test files were read with `git diff`. The background task output files were also read (probe, house, gates, suite).
- Tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh faed89b0` → `context 236094 of 400000 — ok`.
- Check of `launcher-shadow-check-1011`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: launcher-shadow-check-1011 · pass: 1 · tip: a8c18242 · house A: Grok FINDINGS: 5 · findings: 6 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 5 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 236094

## DESK CORRECTION (R1154, brain R1149, 2026-10-12)
Original lines, unchanged above: `## RUNS` :168's G3 bullet ends `· **HELD**.`, and the stop line :223 reads `open: 5`.
Why: desk-launch.sh held_rule (:1041-1057) reads `open:` as held unfixed and wants a held RUNS bullet to end `HELD, NOT FIXED`. The check counted G3 plus the four rejected findings (O1, G4, G1, G5) as open. The four rejected are settled KEEP by the brain (R1149: O1/G4 PASS-2 path dead under R438; G1 pin 123→127 is the same feature, SCOPE; G5 wording kept), so they are not open. G3 is held, not fixed in this check, and fixed by F1 (`FIXED: G3 — tests/ops/test_check_hub_shadow.py::test_build_report_case_count_matches_collection`).
Corrected G3 RUNS bullet:
- G3 · Grok · `uv run pytest --collect-only -q -p no:cacheprovider --color=no tests/ops/test_desk_launch_prechecks.py tests/ops/test_preflight.py tests/ops/test_card_fill.py tests/ops/test_desk_done.py -k 386` · `58/268 tests collected (210 deselected)`; the build report's `:140` says 66 · HELD, NOT FIXED.
CHECK DONE · job: launcher-shadow-check-1011 · pass: 1 · tip: a8c18242 · house A: Grok FINDINGS: 5 · findings: 6 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 236094
