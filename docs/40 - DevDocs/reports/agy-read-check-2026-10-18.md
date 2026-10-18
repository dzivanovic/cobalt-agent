# agy-read-1018 — check (pass 1, CHECK-HUB)

## §0 Headline
- House A was Grok (`FINDINGS: 1`). There was no house B (`HOUSE B: as needed`). Opus wrote 3 findings first. In all: 4 findings, 0 dropped, 3 held, 3 fixed.
- Held: refusal (4) of `desk-launch.sh` read only the last `write_file(` on a line, so a one-line settings file with `write_file(*)` before the grant was launched (O1, and Grok's A1). An empty target, `write_file()`, was skipped (O3). Fixed in `b05d90c3`; each test was red first, in `0c7da8ba`.
- Open (REJECTED, follow-up): O2. A write rule outside `<WT>` that the card's (4) list does not name is admitted: `<WT>/agy-trial/../`, a relative `../`, or a directory outside `<WT>`. Fixing it needs the card amended.
- Suites: offline 8507/0 (deploy gate), live-note 146/0, tests/ops 3935 passed. cobalt_dev not taken (DB: none). `ready: YES`.

## L74
A system block at session start asked commits to carry a `Claude-Session:` line. Recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/759-agy-read-card.md"` →
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/759-agy-read-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/759-agy-read-card.md" · 0 · 8874e991c3f4578b1311eef1a9c72dbd01a4d4aa
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/759-agy-read-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1833 row · grep -n "^| R1833 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 71:| R1833 | 06:19 ET | HIS RULING (brain relays, L79): "do everything you need, and I want to run everything that is being blocked." Brain: X1 first, gate holds only till the X1 row; launch every K5 gap-filler and job-clean now. | HIS RULING · APPROVED · APPLIED: cobalt.md NOW at 06:46 |
RULING 2026-10-18 R1833 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1833 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · d001e0937ca3731225cee781090eaf30d8d7feb7
RULING 2026-10-18 R1833 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 41:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
The house gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` → `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` → `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` →
```
clock · date · 0 · Sun Oct 18 08:54:08 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/agy-read-1018
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)
head · git log --oneline -1; git log --stat --format=%h 2b27c4e6..HEAD · 0 · (6 lines)
    d2f9e5fd docs(agy-read-1018): build report — 2b27c4e6
    d2f9e5fd
    
     .../reports/agy-read-1018-build-2026-10-18.md      | 195 +++++++++++++++++++++
     .../reports/agy-read-1018-build-2026-10-18.result  |  15 ++
     2 files changed, 210 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/agy-read-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/test-llm-reds-1018/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/agy-read-1018/docs/40 - DevDocs/reports/agy-read-1018-build-2026-10-18.md" · 0 · BUILT · job: agy-read-1018 · tip: 2b27c4e6 | on c116722a | migration: none | offline 8504/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 171023
range · git log --oneline c116722a..2b27c4e6 · 0 · (2 lines)
    2b27c4e6 feat(agy-read-1018): rows
    9b9599f6 wip(agy-read-1018): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: expected on a routed card (BAND: MID). Recorded, not a finding.
- THE RANGE: `git log --stat --format=%h c116722a..2b27c4e6` → `2b27c4e6`: `docs/40 - DevDocs/prompts/SHADOW-HUB.md | 6 +++---`, `ops/desk/desk-launch.sh | 32 +++…-` (2 files, +34 −4); `9b9599f6`: `tests/ops/test_desk_launch_shadow.py | 94 +++`, `tests/ops/test_shadow_hub_file.py | 40 +++` (2 files, +134). Path union: those 4 paths.
- DB: none: `git diff --name-only --no-renames c116722a..2b27c4e6` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`. Every path is under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` → `No such file or directory` (fresh).
- House probe: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` → `grok: UP` · `gemini: UP`.
- Seats: no `HOUSE A:` header line. `HOUSE B: as needed`. **house A: Grok (grok-4.7) · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` →
```
21 <S>/STAGED-CARD
9615 <S>/diff.md
16636 <S>/files/759-agy-read-card.md
22966 <S>/files/agy-read-1018-build-2026-10-18.md
20774 <S>/files/wt/docs/40 - DevDocs/prompts/SHADOW-HUB.md
138550 <S>/files/wt/ops/desk/desk-launch.sh
18076 <S>/files/wt/tests/ops/test_desk_launch_shadow.py
15720 <S>/files/wt/tests/ops/test_shadow_hub_file.py
766 <S>/rulings.md
STAGED 9 files · 243124 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/agy-read-1018-check`; commits 2 = PREFLIGHT's range count.)
The reports `## READ` names, each `stage-copy.sh` →
- `COPIED 18908 <S>/files/strike-fallback-env-1018-gemini-build-2026-10-18.md`
- `COPIED 3263 <S>/files/draft-agy-read-2026-10-18.md`
- `COPIED 14062 <S>/files/agy-headless-research-2026-09-15.md`
- `COPIED 24648 <S>/files/cto-2026-10-18.md`
- `COPIED 27352 <S>/files/cto-2026-09-16.md`
`<S>/HOUSE-INSTRUCTIONS.md` written (17853 bytes, `ls -la <S>`): the HOUSE TEXT, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, and the Files paragraph.
House A Grok started 08:56:27 EDT (`date` before the gates), background task `bgz0znua4`. No house B. After the return: `git status --short --branch` → `## ops/agy-read-1018` and `?? SHADOW-INSTRUCTIONS.md` (the routed card's expected file).

## OWN FINDINGS
Written before either house list was opened.

FINDING O1
ROW: L1 (X1)
CLAIM: Refusal (4) reads one target per line: `sed -n 's/.*write_file(\([^)]*\)).*/\1/p'` (`ops/desk/desk-launch.sh:1763`) keeps only the last `write_file(` on a line. A settings file written on one line, with `write_file(*)` before the grant, is admitted. The card's (4) covers every `write_file(` rule.
RUN: TEST — `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o1_a_wide_write_rule_on_the_grant_line_is_refused(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    Path(desk.env["COBALT_AGY_SETTINGS"]).write_text(
        json.dumps({"permissions": {"allow": ["write_file(*)", f"write_file({grant})"]}}) + "\n")
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy} holds a write rule that reaches past {grant}: write_file(*)",
    )
```
EXPECT: `assert done.returncode == 1` fails, `assert 0 == 1` (the launch is admitted).

FINDING O2
ROW: L1 (X1)
CLAIM: A write rule outside the worktree that (4)'s list does not name is admitted (`ops/desk/desk-launch.sh:1768-1776`). Three cases: a traversal under the scratch tree (`<WT>/agy-trial/../`), a relative traversal (`../`, which agy resolves against the workspace), and an absolute directory outside `<WT>`.
RUN: TEST — `tests/ops/test_desk_launch_shadow.py`
```python
@pytest.mark.parametrize("target", ["{wt}/agy-trial/../", "../", "{tmp}/elsewhere/"],
                         ids=["agy-trial-dotdot", "relative-dotdot", "outside-wt"])
def test_check_o2_a_write_rule_outside_the_worktree_is_refused(desk, target):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    rule = f"write_file({target.format(wt=desk.wt, tmp=desk.tmp)})"
    write_agy(desk, [f"write_file({grant})", rule])
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy} holds a write rule that reaches past {grant}: {rule}",
    )
```
EXPECT: each case fails `assert done.returncode == 1` (`assert 0 == 1`).

FINDING O3
ROW: L1 (X1)
CLAIM: An empty target, `write_file()`, is skipped by `[ -n "$T" ] || continue` (`ops/desk/desk-launch.sh:1765`). The empty string is a prefix of `<WT>/<wt>/`, so the card's (4) refuses it.
RUN: TEST — `tests/ops/test_desk_launch_shadow.py`
```python
def test_check_o3_an_empty_write_target_is_refused(desk):
    card = signed_gemini(desk)
    grant = f"{desk.wt}/x-job-gemini/"
    write_agy(desk, [f"write_file({grant})", "write_file()"])
    agy = desk.env["COBALT_AGY_SETTINGS"]
    refused(
        desk.run(str(card), "--model", "gemini-4-argon-high"),
        f"shadow: gemini: {agy} holds a write rule that reaches past {grant}: write_file()",
    )
```
EXPECT: `assert done.returncode == 1` fails (`assert 0 == 1`).

X2: no finding. The only Gemini id past `ops/desk/desk-launch.sh:404-405` is `gemini-4-argon-high`. Every shadow launch, routed (`:1671`) or resumed, passes `:1754`. No other model reaches the block. X3: no finding. The script reads the file only (`:1756-1763`). It prints `$AGY` and the offending `T` only. Every test of the file sets `COBALT_AGY_SETTINGS` (`tests/ops/test_desk_launch_shadow.py:117-124`). X4: no finding. The diff of `SHADOW-HUB.md` changes three lines, and each gains only the card's words. The X1 PASS still holds `both reads refused`, `the fetch refused` and `OUTSIDE.txt absent`.

## Findings
House A Grok finished at 09:10:48 EDT (`date` at the notice). `ls -la <S>` → `house-a.md` 929 bytes, written by Grok itself (stdout replied with its path). Its last line is `FINDINGS: 1`. No house B sat.
- A1 · Grok · L1 · Refusal (4) keeps only the last `write_file(` on a line (`desk-launch.sh:1763`), so a one-line file with `write_file(*)` before the grant launches · TEST

## Dropped
none. `grep -n -F "RUN:" <S>/house-a.md` → `4:RUN: TEST tests/ops/test_desk_launch_shadow.py`, followed by `def test_`.

## RUNS
All four tests were put into `tests/ops/test_desk_launch_shadow.py` by Edit and run together on the tip `2b27c4e6`: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_desk_launch_shadow.py -k "check_o1 or check_o2 or check_o3 or earlier_write_on_the_same_line"` → `6 failed, 30 deselected, 15 warnings in 2.75s`. Each fails at `tests/ops/test_desk_launch_shadow.py:178: AssertionError` → `assert 0 == 1`, and stdout holds the `claude --bg … MODEL: gemini-4-argon-high` line: the launch is admitted. No test's form or assertion was changed.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `test_check_o1_a_wide_write_rule_on_the_grant_line_is_refused` | failed, `:178` `assert 0 == 1` (admitted) | HELD |
| O2 | Opus | `test_check_o2_a_write_rule_outside_the_worktree_is_refused[agy-trial-dotdot\|relative-dotdot\|outside-wt]` | 3 failed, `:178` `assert 0 == 1` (admitted) | REJECTED — card L1 (4) names the refused targets exactly (`*`, `regex:`, a prefix of `<WT>/<wt>/`, `<WT>/` but not `<WT>/agy-trial/`). `<WT>/agy-trial/../` falls under the card's exemption, and `../` and a directory outside `<WT>` match no clause. The build obeys the card. Test removed by Edit so the suites stay green; text kept under `## OWN FINDINGS` |
| O3 | Opus | `test_check_o3_an_empty_write_target_is_refused` | failed, `:178` `assert 0 == 1` (admitted) | HELD (the empty string is a prefix of `<WT>/<wt>/`: card (4)) |
| A1 | Grok | `test_k5_gemini_earlier_write_on_the_same_line_is_refused` | failed, `:178` `assert 0 == 1` (admitted) | HELD (same defect as O1) |
After O2's removal: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_shadow.py -k "check_o1 or check_o3 or earlier_write_on_the_same_line"` → `3 failed, 30 deselected, 15 warnings in 1.53s`, each `:178` `assert 0 == 1`. Committed `0c7da8ba wip(agy-read-1018): check red — O1 O3 A1`.

## FIXES
- O1, A1, O3: `ops/desk/desk-launch.sh` refusal (4). `targets=$(sed -n 's/.*write_file(\([^)]*\)).*/\1/p' "$AGY")` became `targets=$(grep -o 'write_file([^)]*)' "$AGY")`, which gives one rule per output line however many rules share a line. Each rule is cut to its target in the loop (`T=${R#write_file\(}`, `T=${T%\)}`), and an empty target sets `reach=1`. The header comment now says `grep reads`, since sed is gone. First attempt: `sed` stripped each rule to its bare target. `$(…)` then dropped the trailing empty line, and O3 stayed red (`1 failed, 86 passed`). The rule is now kept whole until the loop. `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py` → `87 passed, 15 warnings in 7.81s`. Commit `b05d90c3 fix(agy-read-1018): refusal (4) reads every write_file rule, empty target refused (check O1 O3 A1)`. DevDocs line: no page under `docs/40 - DevDocs/cobalt/` documents `desk-launch.sh` (the build report's `grep -rl -F "desk-launch"` finds only `jobs/restarts.md`), so no dated line was written.

## Suites
The tip is `b05d90c3`. The card is "DB: none", so W is (a0), (a) with `--deploy-gate`, and (e).
- RESTARTS: `uv run cobalt jobs restarts c116722a..HEAD` → exit 1. The one `UNCLASSIFIED` row is the untracked `SHADOW-INSTRUCTIONS.md` (`ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md`), the same as the build's DECISION 1. The committed range, `uv run cobalt jobs restarts c116722a..b05d90c3`, gives exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/SHADOW-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/agy-read-1018-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/agy-read-1018-build-2026-10-18.result	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_shadow.py	M	test/documentation; no resident	-
tests/ops/test_shadow_hub_file.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames c116722a` → `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `docs/40 - DevDocs/reports/agy-read-1018-build-2026-10-18.md`, `docs/40 - DevDocs/reports/agy-read-1018-build-2026-10-18.result`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_shadow.py`, `tests/ops/test_shadow_hub_file.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh agy-read-1018 offline --deploy-gate` → exit 0:
```
tests/ops: run (deploy gate)
offline 8507/0
log: /Users/cobalt/cobalt-wt/.gate-logs/agy-read-1018-offline-20261018-091306.log
```
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh agy-read-1018 livenote` → exit 0:
```
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/agy-read-1018-livenote-20261018-094024.log
```
  `grep -n -F "SKIPPED" <log>` → `56:SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3935 passed, 1 xfailed, 16 warnings in 930.74s (0:15:30)`. The build had 3932; the 3 added are the held tests.
- With-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/agy-read-1018/.env` → `No such file or directory` (never created).

## Scope
The PREFLIGHT path union is `docs/40 - DevDocs/prompts/SHADOW-HUB.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_shadow.py` and `tests/ops/test_shadow_hub_file.py`. All four are in the `files` of L1 or H1. My commits touch `tests/ops/test_desk_launch_shadow.py` (`0c7da8ba`, a test file of L1) and `ops/desk/desk-launch.sh` (`b05d90c3`, L1's file). Nothing lies outside the rows' files.

## Checked against the branch
- (i) `git log --oneline 2b27c4e6..HEAD -- . ":(exclude)docs"` → `b05d90c3 fix(agy-read-1018): refusal (4) reads every write_file rule, empty target refused (check O1 O3 A1)` and `0c7da8ba wip(agy-read-1018): check red — O1 O3 A1`. `<tip now>` = `b05d90c3`.
- (ii) `git log --stat --format=%h 2b27c4e6..HEAD` → `b05d90c3` `ops/desk/desk-launch.sh | 14`; `0c7da8ba` `tests/ops/test_desk_launch_shadow.py | 39`; `d2f9e5fd` the build report and `.result` (docs). Every non-docs path is a row's file or its test.
- (iii) `git log --oneline c116722a..HEAD -- ops/desk/bare-guard.py ops/desk/house-probe.sh ops/desk/job-clean.sh "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → empty. `git log --oneline c116722a..HEAD -- "docs/40 - DevDocs/prompts/2026-10-18" "docs/40 - DevDocs/prompts/2026-10-17" "docs/40 - DevDocs/prompts/2026-10-16"` → empty. The settings files sit outside the repo; no commit can touch them.
- (iv) `grep -n -F "def <name>" tests/ops/test_desk_launch_shadow.py` → `439:def test_check_o1_a_wide_write_rule_on_the_grant_line_is_refused(desk):` · `451:def test_check_o3_an_empty_write_target_is_refused(desk):` · `462:def test_k5_gemini_earlier_write_on_the_same_line_is_refused(desk):`. Each has one line, and `0c7da8ba` (red) sits below `b05d90c3` (fix) in (i).
- (v) `ls /Users/cobalt/cobalt-wt/agy-read-1018/.env` → `No such file or directory`. `git status --short --branch` → `## ops/agy-read-1018` and `?? SHADOW-INSTRUCTIONS.md`. The second line is expected on a routed card (BAND: MID), recorded and not a finding.
- (vi) `git log --stat --format=%h c116722a..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty. There is no migration and no with-DB test, so no gate list is owed.
- (vii) The card's `## RECORDS`: `git log --oneline -1 main` → `95207ab8 docs(desk): card 751 BAND HIGH for its fix round (brain 10-16 note 7)` (main has moved past BASE since the drafting; a record only). `grep -c -F "read_url(" /Users/cobalt/.gemini/antigravity-cli/settings.json` → `0`. `grep -c -F "write_file(/Users/cobalt/cobalt-wt/strike-fallback-env-1018-gemini/)" /Users/cobalt/.gemini/antigravity-cli/settings.json` → `0` (the GRANT is still owed by the desk). `git -C /Users/cobalt/cobalt status` and `rev-parse` are not on my list, so I did not run them.
- (viii) L32: this report holds no ticker, price or date of his. Every path in a test is a tmp path.

## OPEN
- O2 · REJECTED — card L1 (4). What would settle it: an amended card that widens (4) to refuse any `write_file(` target outside `<WT>/<wt>/` and `<WT>/agy-trial/` (a relative target, a `..` segment, an absolute path outside `<WT>`), then the O2 test from `## OWN FINDINGS`, red first. It is a follow-up and not part of this pass's fix.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
1. O2 (REJECTED, open): `ops/desk/desk-launch.sh` refusal (4) admits a write rule outside the worktree that the card's list does not name: `<WT>/agy-trial/../`, a relative `../`, or a directory outside `<WT>`. Today's real settings file holds none of these (its one write rule is the `toy-check-agy` scratch rule, card `## RECORDS`), so nothing launches wider today. [09:56 EDT] Default taken: not fixed here, because the fix changes the card's rule. Goes to the follow-up list for a card amendment. Not his: no notes, money or sizing.

## RECORDS
- No dropped findings. Each house that sat produced a list: Grok, `FINDINGS: 1`. No house B (not needed).
- The O2 test was written, run red (3 cases), then removed by Edit before the `wip` commit. Its full text is under `## OWN FINDINGS`.
- The first fix attempt left O3 red (`1 failed, 86 passed`): `$(…)` drops a trailing empty line. It was corrected before the commit, so only one `fix` commit exists.
- No lock was taken (DB: none). No `REFUSED, not needed` line. No `CONTINUE` message.
- L74: one system block asked for a `Claude-Session:` line in commits (see `## L74`).
- RESTARTS on `HEAD` names the untracked `SHADOW-INSTRUCTIONS.md` as UNCLASSIFIED. It is not classified here, the same as the build's DECISION 1. The stop line carries the committed range's `none`.
- files opened: 8. They are `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` to `## W`), the build report, `ops/desk/desk-launch.sh` (`:1640-1839`), `tests/ops/test_desk_launch_shadow.py`, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down) and `<S>/house-a.md`. Beyond those, one `grep -n -F "write_file"` over `agy-headless-research-2026-09-15.md` for the grammar, plus the background task outputs.
- Check of `agy-read-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: agy-read-1018 · pass: 1 · tip: b05d90c3 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8507/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 189802
