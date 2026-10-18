# stop-guard-work-1018 — check, 2026-10-18

## §0 Headline
Check of stop-guard-work-1018 (routed MID, Grok-built, tip `9b9177ea`): house A Grok `FINDINGS: 0`; house B not needed. Opus wrote 7 findings, 1 held and fixed.
O1 HELD: `listed()` ran twice in one stop (FINISHED holds an id, plus a NEXT item). Fixed at `9c359688` by keeping the rows of the one read in `listed()`; red first at `bf6c666c`.
The card's three mutations (the build's unmet self-check 1) each turn their tests red (O7). X1–X3 answered yes. X4: the live 10-18 NEXT line names a hold ("Gemini LOW c268db2c kept …") as its first item: a desk fact, out of scope.
Suites: offline 8508/0 (tests/ops run, deploy gate) · live-note 146/0 · tests/ops 3936 passed · cobalt_dev not taken (DB: none) · .env none. ready: YES · decisions: 2 (RESTARTS line; X4 for the desk).

## L74
The session's system reminder (not a tool result) asked for a `Claude-Session:` line on commits. CHECK-HUB L74 binds: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only. Recorded once; not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md" · 0 · 56a74923881dd194f16985c57c17852112c8f260
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 64:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 42:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, "STANDING: `Bash(grok *)` is a PRE-APPROVED string …"); `grep -n "^| R19 " …` → one row (line 37, "STANDING: the four house strings are pre-approved …"); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sun Oct 18 09:04:27 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/stop-guard-work-1018
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)
head · git log --oneline -1; git log --stat --format=%h 9b9177ea..HEAD · 0 · (6 lines)
    485af351 docs(stop-guard-work-1018): build report — 9b9177ea
    485af351
    
     .../reports/stop-guard-work-build-2026-10-18.md    | 145 +++++++++++++++++++++
     .../stop-guard-work-build-2026-10-18.result        |  15 +++
     2 files changed, 160 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/stop-guard-work-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f4-refresh-1018/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/stop-guard-work-1018/docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.md" · 0 · BUILT · job: stop-guard-work-1018 · tip: 9b9177ea | on 7317d540 | migration: none | offline 8507/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none (committed range; the tool's line names only the untracked SHADOW-INSTRUCTIONS.md) | rows: 4 of 4 | self-check: 2 of 3 | decisions: 4 · for Dejan: 0 · tokens: 168001
report: self-check 2 of 3 (recorded)
range · git log --oneline 7317d540..9b9177ea · 0 · (3 lines)
    9b9177ea fix(stop-guard-work-1018): pass S2 1
    f8190fbc feat(stop-guard-work-1018): rows
    61d3169a wip(stop-guard-work-1018): red
PREFLIGHT OK
```
- `?? SHADOW-INSTRUCTIONS.md`: routed card (BAND MID), expected, recorded, not a finding.
- Self-check 2 of 3 (lower count): recorded; goes to the house as a fact (the build report is staged whole).
- THE RANGE: `git log --stat --format=%h 7317d540..9b9177ea` → `9b9177ea tests/ops/test_stop_guard.py | 8 ++++++--`; `f8190fbc ops/desk/stop-guard.py | 121 +++`; `61d3169a tests/ops/test_stop_guard.py | 229 +++`. Path union: `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`.
- DB: none: `git diff --name-only --no-renames 7317d540..9b9177ea` → `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` — every path under `ops/` or `tests/ops/`.
- `ls <S>` → "No such file or directory" (fresh).
- House probes (`sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"`, exit 0): `grok: UP` · `gemini: UP`.
- No `HOUSE A:` header line on the card. `HOUSE B: as needed` → **house A: Grok · house B: none (not needed)**.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` (exit 0):
```
28 …/stop-guard-work-1018-check/STAGED-CARD
18568 …/stop-guard-work-1018-check/diff.md
15243 …/stop-guard-work-1018-check/files/739-stop-guard-work-card.md
20593 …/stop-guard-work-1018-check/files/stop-guard-work-build-2026-10-18.md
34882 …/stop-guard-work-1018-check/files/wt/ops/desk/stop-guard.py
50042 …/stop-guard-work-1018-check/files/wt/tests/ops/test_stop_guard.py
769 …/stop-guard-work-1018-check/rulings.md
STAGED 7 files · 140125 bytes · commits 3
```
(`commits 3` = PREFLIGHT's range count.) `## READ` files the script cannot derive, each `stage-copy.sh`:
- `COPIED 25021 …/files/cto-2026-10-17.md`
- `COPIED 24947 …/files/cto-2026-10-18.md` (the desk's working-tree file at 09:05)
- `COPIED 868 …/files/wt/ops/desk/desk-list.sh`
`<S>/HOUSE-INSTRUCTIONS.md` written (16464 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, and the Files paragraph.
House A Grok started 09:06 (`date` 09:06:21; gates re-run: R17 one row, R19 one row, R19 commit `5055151d…`); `cd <AGY>` → grok line → `cd <WT>` → `git status --short --branch` → `## ops/stop-guard-work-1018` / `?? SHADOW-INSTRUCTIONS.md` (the expected routed-card file).

## OWN FINDINGS
Written 09:09 EDT, before either house list was opened.

FINDING O1
ROW: W1
CLAIM: `next_unlaunched` reads `listed()` a second time in one stop when `finished_open` has already read it: `finished_open` runs its own `listed()` (`ops/desk/stop-guard.py:454-455`) and returns only a string, so `desk()` passes `listing=None` on (`:551`) and `next_unlaunched` runs `listed()` again (`:516-517`); W1 says "else `listed()` once".
RUN: TEST — `tests/ops/test_stop_guard.py`
```python
def test_o1_finished_and_next_read_the_list_once(tmp_path):
    d = Desk(tmp_path)
    isolate_pgrep(d)
    calls = tmp_path / "list.log"
    (d.hook.parent / "desk-list.sh").write_text(
        f"#!/bin/sh\necho x >> '{calls}'\nprintf '%s\\n' '{DESK_ROW_LINE}'\n"
    )
    state = tmp_path / "wt" / ".job-state"
    state.mkdir(parents=True, exist_ok=True)
    (state / "FINISHED").write_text("2026-01-02T03:04:05 99990000-0000 x\n")
    d.owed("owed: none", "NEXT: rebuild x")
    r = d.run()
    assert (r.returncode, r.stderr) == (2, "start it: rebuild x\n")
    assert calls.read_text().splitlines() == ["x"]
```
EXPECT: the last assertion fails: `['x', 'x'] == ['x']`.

FINDING O2
ROW: X2
CLAIM: `STATE_1017`, `NEXT_1017` and `HANDOVER_REAL` (`tests/ops/test_stop_guard.py:819-842`) are not byte-identical to lines 108, 109 and 122 of `cto-2026-10-17.md` on main.
RUN: TEST — `tests/ops/test_stop_guard.py` (temporary; reads the committed main file read-only)
```python
def test_o2_the_1017_constants_are_the_lines(tmp_path):
    lines = Path("/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-17.md").read_text().splitlines()
    assert (lines[107], lines[108], lines[121]) == (STATE_1017, NEXT_1017, HANDOVER_REAL)
```
EXPECT: the assertion fails (a differing constant).

FINDING O3
ROW: X3
CLAIM: a stop with no `NEXT` line runs `pgrep` (`ops/desk/stop-guard.py:521` reached without an item).
RUN: TEST — `tests/ops/test_stop_guard.py`
```python
def test_o3_no_next_line_runs_no_pgrep(tmp_path):
    d = Desk(tmp_path)
    text = d.hook.read_text()
    assert '"pgrep", "-l"' in text
    d.hook.write_text(text.replace('"pgrep", "-l"', '"%s", "-l"' % (tmp_path / "no-pgrep")))
    d.owed("owed: none", STATE_1017)
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")
```
EXPECT: stderr `stop-guard: desk not guarded — FileNotFoundError: …` (exit 0) where `""` is asserted.

FINDING O4
ROW: X4
CLAIM: on the working-tree `cto-2026-10-18.md` `## §5 CURRENT` `NEXT` line (line 95 at 09:08) the guard names its first `;`-piece, `Gemini LOW c268db2c kept (…), agy confinement card on HARNESS LIST, spare seats only, MID 718 / HIGH 719 held (R1855)` — a hold, not work to launch (`ops/desk/stop-guard.py:509-513`).
RUN: TEST — `tests/ops/test_stop_guard.py` (temporary; reads the desk's file read-only, the line found by content)
```python
def test_o4_the_1018_next_line(tmp_path):
    live = Path("/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md").read_text().splitlines()
    line = next(x for x in live[live.index("## §5 CURRENT"):] if x.startswith("NEXT ("))
    d = Desk(tmp_path)
    isolate_pgrep(d)
    d.owed("owed: none", line)
    d.lister(DESK_ROW_LINE)
    r = d.run()
    assert r.returncode == 2
    assert r.stderr.startswith("start it: Gemini LOW c268db2c kept (")
    print(r.stderr)
```
EXPECT: green, printing the named item (the claim is shown; a desk fact, not a build defect).

FINDING O5
ROW: W1
CLAIM: W1's clause "inside the same `try` (so `ListUnreadable` reaches `UNREADABLE`)" (`ops/desk/stop-guard.py:550-553`) is pinned by no new test: no test stops with an unwaiting `NEXT` item and an unreadable list.
RUN: TEST — `tests/ops/test_stop_guard.py`
```python
def test_o5_next_with_an_unreadable_list_blocks(tmp_path):
    d = Desk(tmp_path)
    isolate_pgrep(d)
    d.owed("owed: none", "NEXT: rebuild x")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", "session list unreadable — fix it\n")
```
EXPECT: red if the call were outside the `try`; on the tip expected green (a pin, not a defect).

FINDING O6
ROW: W4
CLAIM: W4's "not this session's own id" (`ops/desk/stop-guard.py:499-500`) is pinned by no test: a HANDOVER line naming this session as its own successor, with its own row listed, must still block.
RUN: TEST — `tests/ops/test_stop_guard.py`
```python
def test_o6_a_handover_to_itself_is_still_blocked(tmp_path):
    d = Sized(tmp_path)
    isolate_pgrep(d)
    d.lister(DESK_ROW)
    d.owed("owed: none", STATE_1017, NEXT_1017)
    append_line(d, f"HANDOVER: predecessor {SID[:8]} → successor {SID[:8]} at 21:06 · pane w2:pV1")
    r = d.run()
    assert (r.returncode, r.stdout, r.stderr) == (2, "", block_line(FIRST_1017))
```
EXPECT: on the tip expected green (a pin); red if `:499-500` were removed.

FINDING O7
ROW: W2 (MUTATION; the build's DECISION 2: self-check 1 not met, no mutation run)
CLAIM: the card's three mutations each leave their named tests green: (m1) `next_unlaunched` → `return None` first (`ops/desk/stop-guard.py:509`); (m2) `if worker and watched()` → `if worker or watched()` (`:521`); (m3) `refreshing` → `return False` first (`:489`).
RUN: COMMAND — under each mutation in turn (Edit, run, undo): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k "test_w1 or test_w2 or test_w4"`
EXPECT: `0 failed` under a mutation (a test green when its fix is undone).


## Findings
House A Grok finished 09:23 (`date` 09:23:50); `ls -la <S>` → `house-a.md` 12 bytes, written by Grok. Whole content: `FINDINGS: 0`. Grok's stdout: "…The tip matches the rows I could check by reading. No failing run to hand over./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stop-guard-work-1018-check/house-a.md". House B: none (not needed).
Kept, one row each (`id · house · row · claim · TEST|COMMAND`):
- O1 · opus-own · W1 · `listed()` runs twice in one stop when FINISHED holds an id and NEXT holds an item · TEST
- O2 · opus-own · X2 · the 10-17 constants differ from the main lines · TEST
- O3 · opus-own · X3 · a stop with no NEXT line runs pgrep · TEST
- O4 · opus-own · X4 · the 10-18 NEXT line names a hold as its first item · TEST
- O5 · opus-own · W1 · the ListUnreadable clause of the NEXT path is unpinned · TEST
- O6 · opus-own · W4 · the "not this session's own id" clause is unpinned · TEST
- O7 · opus-own · W2 · the three card mutations leave their tests green · COMMAND

## Dropped
none (Grok wrote no block).

## RUNS
Each test put in `tests/ops/test_stop_guard.py` with Edit, after the W4 tests, run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py::<test>`. No test's form or assertion was repaired.
- O1 · opus-own · `::test_o1_finished_and_next_read_the_list_once` · `1 failed, 15 warnings in 1.39s`; first failing line `E       AssertionError: assert ['x', 'x'] == ['x']` (`tests/ops/test_stop_guard.py:1061`), after the `(2, "start it: rebuild x\n")` assertion passed · **HELD**
- O2 · opus-own · `::test_o2_the_1017_constants_are_the_lines` · `1 passed, 15 warnings in 0.91s` (the three constants equal lines 108, 109, 122 of main's `cto-2026-10-17.md`; X2 answered: real text) · NOT HELD (test removed)
- O3 · opus-own · `::test_o3_no_next_line_runs_no_pgrep` · `1 passed, 15 warnings in 0.94s` (pgrep pointed at a missing binary: no `desk not guarded` line; X3 answered: no pgrep, and no `desk-list.sh` per `test_w1_no_next_line_changes_nothing`) · NOT HELD (test removed)
- O4 · opus-own · `::test_o4_the_1018_next_line` (`-rP`) · `1 passed, 15 warnings in 0.91s`; captured: `start it: Gemini LOW c268db2c kept (SHADOW-INSTRUCTIONS.md untracked; close when clean), agy confinement card on HARNESS LIST, spare seats only, MID 718 / HIGH 719 held (…` · OUT OF SCOPE — `## NOT IN THIS JOB`: "A change of `NEXT`'s form in the live reports" (X4: a desk fact; see DECISIONS) (test removed)
- O5 · opus-own · `::test_o5_next_with_an_unreadable_list_blocks` · `1 passed, 15 warnings in 0.86s` · NOT HELD (test removed)
- O6 · opus-own · `::test_o6_a_handover_to_itself_is_still_blocked` · `1 passed, 15 warnings in 0.85s` · NOT HELD (test removed)
- O7 · opus-own · `uv run pytest -q … tests/ops/test_stop_guard.py -k "test_w1 or test_w2 or test_w4"` under each mutation (Edit, run, undo): (m1) `return None` at the top of `next_unlaunched` → `11 failed, 4 passed, 116 deselected` (the RED test, the first-item, the semicolon, the count-and-record, both `…alone_blocks`, the brain row, and four W4 blocked tests; first failing line `E       AssertionError: assert (0, '', '') == (2, '', 'star...drafters …\n')`); (m2) `worker and watched()` → `or` → `2 failed, 13 passed` (`test_w2_a_live_worker_alone_blocks`, `test_w2_an_armed_watch_alone_blocks`); (m3) `return False` at the top of `refreshing` → `1 failed, 14 passed` (`test_w4_the_blocked_shape_with_a_refresh_to_a_live_successor_passes`: `assert (2, '', 'star...drafters …\n') == (0, '', '')`). `git diff --stat` after the undo → only the test file (the O1 test). Every mutation is caught · NOT HELD. (This also settles the build's self-check 1 / DECISION 2: the three mutations now have quoted output.)
Committed before the fix: `git commit … -- tests/ops/test_stop_guard.py` → `[ops/stop-guard-work-1018 bf6c666c] wip(stop-guard-work-1018): check red — O1`.

## FIXES
- O1: `ops/desk/stop-guard.py` `listed()` keeps its rows in a module list `_LISTED` and returns them on a later call in the same process, so `finished_open`'s read is the one `next_unlaunched` uses (`finished_open`, `unsettled`, `desk()` unchanged, as the fence asks). `::test_o1_…` → `1 passed, 15 warnings in 0.99s`; `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py tests/ops/test_desk_refresh_wakeup.py` → `138 passed, 15 warnings in 60.19s (0:01:00)`. (`idle-wake.py` loads the module fresh and uses only `worktree` and `report_last_line`; the forced path calls `listed()` once per process.) Commit `9c359688 fix(stop-guard-work-1018): listed() reads desk-list.sh once per process (check O1)`. DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/stop-guard.py` (Glob of `*{ops,desk,guard,hook}*` there → only `modelaccess/`, `radar/formation/`, `redact/`, `session/` pages); none written, recorded.

## Suites
On tip `9c359688`, DB: none shape (RESTARTS, then (a0), (a) with `--deploy-gate`, (e), and `tests/ops`):
- RESTARTS: `uv run cobalt jobs restarts 7317d540..HEAD` (exit 1), whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.result	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
  The one UNCLASSIFIED row is the untracked routed-card file `SHADOW-INSTRUCTIONS.md` (expected, never committed); every committed path is `-`. See DECISION 1.
- (a0) `git diff --name-only --no-renames 7317d540` → `docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.md` · `docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.result` · `ops/desk/stop-guard.py` · `tests/ops/test_stop_guard.py`: every path under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-work-1018 offline --deploy-gate` (exit 0): `tests/ops: run (deploy gate)` / `offline 8508/0` / `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-work-1018-offline-20261018-092750.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-work-1018 livenote` (exit 0): `live-note 146/0` / `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-work-1018-livenote-20261018-092751.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (exit 0): `3936 passed, 1 xfailed, 16 warnings in 893.75s (0:14:53)`.
- with-DB: not run (DB: none); `cobalt_dev`: not taken. `.env`: `ls /Users/cobalt/cobalt-wt/stop-guard-work-1018/.env` → `No such file or directory` (10:10).
- The new test `test_o1_finished_and_next_read_the_list_once` was shown red first (`## RUNS` O1) and is green in the offline run.

## Scope
PREFLIGHT path union: `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py` (both in rows W1/W4 `files`). My commits: `bf6c666c` → `tests/ops/test_stop_guard.py` (a test file); `9c359688` → `ops/desk/stop-guard.py` (W1's `files`). The fix touches `listed()` only; `owed_block`, `unsettled`, `queued`, `finished_open`, the cap and `desk()` are unchanged (the X1 diff below).

## Checked against the branch
- (i) `git log --oneline 9b9177ea..HEAD -- . ":(exclude)docs"` → `9c359688 fix(stop-guard-work-1018): listed() reads desk-list.sh once per process (check O1)` · `bf6c666c wip(stop-guard-work-1018): check red — O1`. `<tip now>` = `9c359688`.
- (ii) `git log --stat --format=%h 9b9177ea..HEAD` → `9c359688 ops/desk/stop-guard.py | 13`; `bf6c666c tests/ops/test_stop_guard.py | 16`; `485af351` the build report and `.result` (docs). No other path.
- (iii) Fenced paths: `git log --oneline 7317d540..HEAD -- ops/desk/desk-list.sh ops/desk/desk-context.sh ops/desk/idle-wake.py ops/desk/bare-guard.py` → empty. (No hub file is touched: (ii).)
- (iv) `grep -n -F "def test_o1_finished_and_next_read_the_list_once" tests/ops/test_stop_guard.py` → `1048:def test_o1_finished_and_next_read_the_list_once(tmp_path):`; its red commit `bf6c666c` sits below its fix `9c359688` in (i).
- (v) `ls <WT>/.env` → "No such file or directory"; `git status --short --branch` → `## ops/stop-guard-work-1018` / `?? SHADOW-INSTRUCTIONS.md` (routed card, expected, recorded, not a finding).
- (vi) `git log --stat --format=%h 7317d540..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration, no with-DB test; gate lists not needed.
- (vii) Card RECORDS: `git -C /Users/cobalt/cobalt log --oneline -1 -- ops/desk/stop-guard.py tests/ops/test_stop_guard.py` → `93282462 feat(close-automation-1015): …` (= the record's "last commit … is `93282462`"); `git -C /Users/cobalt/cobalt log --oneline -1 7317d540` → `7317d540 docs(desk): R1841-R1842 no idle desk, stop-guard drafter prompt, handover plan` (= BASE). The record's `rev-parse` and `git status` commands are not on my list; not run.
- X1: `git diff 7317d540..HEAD -- ops/desk/stop-guard.py` → hunks: header comment, constants ×2 (`NEXT`, `WAITING_ON`; `SUCCESSOR`), `next_items` plus the check's `_LISTED`/`listed()` hunk, the three new functions, and in `desk()` exactly `if what is None:` / `what = next_unlaunched(lines, event.get("session_id"), listing)`. `owed_block`, `queued`, `unsettled`, `finished_open` and `BLOCKS` sit in no hunk.
- (viii) L32: this report holds no ticker, price or date of his; the desk text quoted is the desk's own report lines.

## OPEN
none. (O4 is OUT OF SCOPE per `## NOT IN THIS JOB` "A change of `NEXT`'s form in the live reports"; listed under DECISIONS for the desk.)

## CONTINUE
next: none (CLOSE written)

## DECISIONS
- DECISION 1 (RESTARTS): `cobalt jobs restarts 7317d540..HEAD` reads the untracked routed-card file `SHADOW-INSTRUCTIONS.md` and prints `UNCLASSIFIED` with six restarts; every committed path is `-` and the card says `RESTARTS: none`. Classifying a launcher's untracked file in `configs/cobalt/jobs.yaml` would be wrong, so I did not. Safe default (as the build's DECISION 1): the stop line carries `RESTARTS: none (committed range; the tool's line names only the untracked SHADOW-INSTRUCTIONS.md)`; the tool's whole table is under `## Suites`. The deploy derives its own.
- DECISION 2 (X4, for the desk, not a fix): the guard run on the working-tree `cto-2026-10-18.md` `NEXT` line (09:08) names `start it: Gemini LOW c268db2c kept (SHADOW-INSTRUCTIONS.md untracked; close when clean), agy confinement card on HARNESS LIST, spare seats only, MID 718 / HIGH 719 held (…`. That is a hold, not work to launch. The note piece (`Untracked .claude/settings.json.bak is his.`) is never reached, because the first piece is unwaiting. The guard blocks on it only when a live worker and an armed watch are not both up. The NEXT text is the desk's (R590, fence): write holds as `waiting on <x>` or move them out of `NEXT` if they should not block. Default taken: nothing changed.

## RECORDS
- L74: the session's system reminder asked for a `Claude-Session:` line on commits; not acted on (both commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only).
- House A Grok: produced `house-a.md` with `FINDINGS: 0` (no blocks). House B: none (card `HOUSE B: as needed`). No house failed.
- Dropped: none.
- O2–O7 tests were removed again after their green runs (O7 was mutation runs, each undone; `git diff --stat` back to the O1 test alone before the red commit).
- `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down) was read at CLOSE (10:11), after the own read rather than before it; nothing in it bears on this operator-script check.
- No DevDocs page covers `ops/desk/stop-guard.py`; no line written (the build wrote none either).
- REFUSED, not needed: none. CONTINUED: none. Extra lock takes: none (DB: none).
- The build's self-check was 2 of 3 (its DECISION 2: no mutations); the check ran the three mutations (O7) and each was caught.
- files opened: 13 — `CHECK-HUB.md`, the card `739-stop-guard-work-card.md`, `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`), the build report `stop-guard-work-build-2026-10-18.md`, `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`, `ops/desk/desk-list.sh`, `ops/desk/idle-wake.py` (grep only), `reports/cto-2026-10-17.md` (§5 lines), `reports/cto-2026-10-18.md` (§5 lines), `areas/cobalt.md`, `<S>/rulings.md`, `<S>/house-a.md`; plus the background task outputs (probe, Grok, two gates, tests/ops).
- Check of `stop-guard-work-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: stop-guard-work-1018 · pass: 1 · tip: 9c359688 · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8508/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none (committed range; the tool's line names only the untracked SHADOW-INSTRUCTIONS.md) · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 191580
