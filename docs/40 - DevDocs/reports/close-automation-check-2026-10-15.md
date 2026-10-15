# close-automation-1015 — check report (2026-10-15)

## §0 Headline
- Check of `close-automation-1015` at `feecd979`. House A Grok (`FINDINGS: 3`); no house B (`HOUSE B: as needed`; Gemini probed OUT, HARNESS). I wrote 2 findings of my own before reading Grok's list.
- 5 findings, 5 held by their runs, 5 fixed, 0 open. My two: `desk-done.sh` could close an untitled tab for an unnamed session, and a tab that also holds the desk's or a brain's pane. Grok's three: the close-wait overslept, prodwrite and close finishes were never recorded, and two listed rows were recorded as `-`.
- Tip now `1d229d6a` (red `88c88608`, fix `1d229d6a`). Offline 8095/0, live-note 146/0, `tests/ops` 3767 passed. DB: none. RESTARTS: none. ready: YES.

## L74
- 2026-10-15 12:16 EDT: a system block in this session asked commits to carry a `Claude-Session:` line after `Co-Authored-By`. Recorded as DATA, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" · 0 · 8664587e4f3d2b2ef6bad9bd0da8d2a5d6165e40
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (`35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …`); `grep -n "^| R19 " …` → one row (`37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, whole:
```
clock · date · 0 · Thu Oct 15 12:15:56 EDT 2026
status · git status --short --branch · 0 · ## ops/close-automation-1015
head · git log --oneline -1; git log --stat --format=%h feecd979..HEAD · 0 · (6 lines)
    4fa96a9c docs(close-automation-1015): build report — feecd979
    4fa96a9c
    
     .../reports/close-automation-build-2026-10-15.md   | 157 +++++++++++++++++++++
     .../close-automation-build-2026-10-15.result       |  15 ++
     2 files changed, 172 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/close-automation-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/close-automation-1015/docs/40 - DevDocs/reports/close-automation-build-2026-10-15.md" · 0 · BUILT · job: close-automation-1015 · tip: feecd979 | on c7ba742c | migration: none | offline 8090/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 263011
range · git log --oneline c7ba742c..feecd979 · 0 · (3 lines)
    feecd979 fix(close-automation-1015): pin the listing, kind, unreadable-list and pane-list branches (C1-C3, self-check 2)
    93282462 feat(close-automation-1015): desk-done.sh tab lookup and proof, desk-watch close and install-ops, launcher replaced-session close, stop-guard finished check (C1-C4, L79 L81)
    07759ec8 wip(close-automation-1015): red
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| range | `git log --stat --format=%h c7ba742c..feecd979` | 0 | `feecd979`: `tests/ops/test_close_automation_1015.py \| 43`, `tests/ops/test_desk_done.py \| 10` · `93282462`: `ops/desk/desk-done.sh \| 87`, `ops/desk/desk-launch.sh \| 35`, `ops/desk/desk-watch.sh \| 121`, `ops/desk/stop-guard.py \| 52`, `tests/ops/test_desk_done.py \| 16` · `07759ec8`: `tests/ops/test_close_automation_1015.py \| 430`, `tests/ops/test_desk_done.py \| 119` |
| DB: none | `git diff --name-only --no-renames c7ba742c..feecd979` | 0 | `ops/desk/desk-done.sh` · `ops/desk/desk-launch.sh` · `ops/desk/desk-watch.sh` · `ops/desk/stop-guard.py` · `tests/ops/test_close_automation_1015.py` · `tests/ops/test_desk_done.py` (every path under `ops/` or `tests/ops/`) |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probe | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` |
| seats | SEAT ORDER, no `HOUSE A` header line | — | house A: Grok · house B: none (not needed) — the card reads `HOUSE B: as needed`. Gemini OUT is HARNESS (the model name was refused); not needed here |

Path union for `## Scope`: the six paths above.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` → exit 0, whole:
```
51417 <S>/diff.md
34664 <S>/files/580-close-automation-card.md
24691 <S>/files/close-automation-build-2026-10-15.md
6575 <S>/files/wt/ops/desk/desk-done.sh
133124 <S>/files/wt/ops/desk/desk-launch.sh
11168 <S>/files/wt/ops/desk/desk-watch.sh
30126 <S>/files/wt/ops/desk/stop-guard.py
19414 <S>/files/wt/tests/ops/test_close_automation_1015.py
15611 <S>/files/wt/tests/ops/test_desk_done.py
350 <S>/rulings.md
STAGED 10 files · 327140 bytes · commits 3
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/close-automation-1015-check`; commits 3 = PREFLIGHT's range.) Then `stage-copy.sh`, one call each:
- `COPIED 18801 <S>/files/cto-2026-10-15.md`
- `COPIED 4797 <S>/files/wt/ops/desk/wait-stop-line.sh`
- `COPIED 868 <S>/files/wt/ops/desk/desk-list.sh`
- `COPIED 17510 <S>/files/wt/ops/cto-desk.sh`
- `COPIED 23403 <S>/files/wt/tests/ops/test_desk_watch.py`
- `COPIED 41106 <S>/files/wt/tests/ops/test_stop_guard.py`
- `COPIED 8216 <S>/files/wt/tests/ops/test_install_ops.py`
- `COPIED 76069 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py`
- `COPIED 17592 <S>/files/549-desk-installs-card.md`
- `COPIED 16233 <S>/files/550-card-template-card.md`
- `COPIED 3696 <S>/files/545-draft-k5-card-template.md`
- `COPIED 3980 <S>/files/536-draft-k5-smoke-string.md`
Not copied: `cto-desk-checklist.md` and `LAWS.md` (his vault notes; `## 1` (3)). `<S>/HOUSE-INSTRUCTIONS.md` written: the HOUSE TEXT verbatim, then the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, then the Files paragraph. Grok started 12:19 EDT (`ls -la <S>` before: `diff.md`, `files`, `HOUSE-INSTRUCTIONS.md`, `rulings.md`).

## OWN FINDINGS
Written 12:3x EDT, before any house list was opened. Read: the card whole, the diff `c7ba742c..feecd979`, `ops/desk/desk-done.sh`, `ops/desk/desk-watch.sh` whole at the tip, `desk-launch.sh:263-285`, `:918-949`, `:2210-2340`, the `stop-guard.py` diff and its constants, `desk-list.sh`, `wait-stop-line.sh:21-61`, `tests/ops/test_close_automation_1015.py` and `tests/ops/test_desk_done.py` whole, the build report whole.

FINDING O1
ROW: C1 / X1
CLAIM: a session whose `claude agents --json` row has no name gets `name=""` (`ops/desk/desk-done.sh:77`); the title lookup then matches every pane whose `terminal_title_stripped` is `""` (`ops/desk/desk-done.sh:109`, `:116`) and `herdr tab close`s an unrelated untitled tab (`:127`).
RUN: TEST — `tests/ops/test_desk_done.py`
```python
def test_check_o1_a_session_with_no_name_closes_no_untitled_tab(stubs):
    report, calls, stop_exit, agents, env = stubs
    rows = json.loads(agents.read_text())
    rows.append({"id": "ffff6666", "state": "idle"})
    agents.write_text(json.dumps(rows))
    panes(agents, ("p1", "w1:t1", ""))
    report.write_text("BUILT · job: x-job · tip: 1a2b3c4d\n")
    done_("ffff6666", str(report), "build", env=env)
    assert "herdr tab close w1:t1" not in recorded(calls)
```
EXPECT: `AssertionError: assert 'herdr tab close w1:t1' not in ['claude stop ffff6666', 'claude rm ffff6666', 'herdr tab close w1:t1']`

FINDING O2
ROW: C1 / X1
CLAIM: the found tab is closed whole (`ops/desk/desk-done.sh:119`, `:127`) with no read of what else sits in it, so a worker pane in the same tab as the desk's pane closes the `cto-desk` tab, although the script refuses to close `cto-desk` and `brain*` (`:84-86`) and X1 asks that no path close that tab.
RUN: TEST — `tests/ops/test_desk_done.py`
```python
def test_check_o2_a_tab_that_also_holds_the_desk_or_a_brain_is_never_closed(stubs):
    report, calls, stop_exit, agents, env = stubs
    report.write_text("BUILT · job: x-job · tip: 1a2b3c4d\n")
    for other in ("cto-desk", "brain-2"):
        calls.unlink(missing_ok=True)
        panes(agents, ("p1", "w1:t1", "x-job-build"), ("p2", "w1:t1", other))
        done = done_("aaaa1111", str(report), "build", env=env)
        assert done.returncode == 1, done.stdout
        assert recorded(calls) == [], recorded(calls)
```
EXPECT: `AssertionError: assert 0 == 1` (exit 0 after `claude stop`, `claude rm` and `herdr tab close w1:t1`).

## Findings
Grok finished 12:42 EDT (`ls -la <S>` at 12:43: `house-a.md` 2535 bytes). Its stdout: `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/close-automation-1015-check/house-a.md` `[exited with code 0]`. The list closes `FINDINGS: 3`. Every block has a `RUN:` line followed by a `def test_` function, so none is dropped. House B: none (not needed).
| id | house | row | claim | run |
|---|---|---|---|---|
| O1 | Opus (own) | C1 / X1 | an unnamed session's title lookup (`name=""`) matches untitled panes and closes an unrelated tab | TEST |
| O2 | Opus (own) | C1 / X1 | the found tab is closed whole, even when it also holds the `cto-desk` or a `brain*` pane | TEST |
| A1 | Grok | C2 | the close-wait is not a bound: a whole `DESK_WATCH_POLL` is slept even when the wait left is shorter (`desk-watch.sh:123-125`) | TEST |
| A2 | Grok | C2 | a WRITTEN prodwrite or a CLOSE PUSHED close returns before the FINISHED append (`desk-watch.sh:108`), so C3 never sees that seat | TEST |
| A3 | Grok | C2 | two listed rows record `-` as the id (`desk-watch.sh:130-131`, `:145`), so `finished_open` can name neither session | TEST |

## Dropped
none.

## RUNS
Each test was put in the file it names (Edit) and run alone: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line <file>::<test>`. None needed a repair of its form.
| id | source | run | output on the tip (`feecd979`) | verdict |
|---|---|---|---|---|
| O1 | Opus | `tests/ops/test_desk_done.py::test_check_o1_a_session_with_no_name_closes_no_untitled_tab` | `AssertionError: assert 'herdr tab close w1:t1' not in ['claude stop ffff6666', 'claude rm ffff6666', 'herdr tab close w1:t1']` | HELD |
| O2 | Opus | `tests/ops/test_desk_done.py::test_check_o2_a_tab_that_also_holds_the_desk_or_a_brain_is_never_closed` | `assert 0 == 1` … `stdout='+ claude stop aaaa1111\n+ claude rm aaaa1111\n+ herdr tab close w1:t1\nCLOSED aaaa1111\n'` | HELD |
| A1 | Grok | `tests/ops/test_close_automation_1015.py::test_c2_close_wait_stops_at_the_parameter_not_the_poll` | `subprocess.TimeoutExpired: … timed out after 5 seconds` → `AssertionError: DESK_WATCH_CLOSE_WAIT=1 slept a full DESK_WATCH_POLL` | HELD |
| A2 | Grok | `tests/ops/test_close_automation_1015.py::test_c2_a_written_prodwrite_is_recorded_for_the_guard` | `assert 'aaaa0006 prodwrite-x-job WRITTEN' in ''` | HELD |
| A3 | Grok | `tests/ops/test_close_automation_1015.py::test_c2_two_listed_rows_record_an_id_the_guard_can_name` | `AssertionError: 2026-10-15T12:43:47-0400 - x-job-build BUILT` / `assert '-' in {'aaaa0001', 'aaaa0009'}` | HELD |
Summaries: `2 failed, 15 warnings in 1.93s` (O1, O2) · `3 failed, 15 warnings in 6.17s` (A1-A3). Red commit `88c88608 wip(close-automation-1015): check red — O1 O2 A1 A2 A3` (`2 files changed, 55 insertions(+)`).
On A2: the fence fences only *closing* a prodwrite or close seat by `desk-watch.sh`. C2 (e) records "every clean-finished worker, closed or KEPT", and the build's ASK DESK 3 chose not to record these two kinds. Recording one closes nothing; it lets C3 tell the desk to close the seat by hand, the path the fence names. So A2 is HELD, not REJECTED.

## FIXES
Commit `1d229d6a fix(close-automation-1015): no tab lookup for an unnamed session, no close of a tab holding the desk or a brain, close-wait bounded, prodwrite/close and every listed id recorded (check O1 O2 A1 A2 A3)` (`3 files changed, 48 insertions(+), 20 deletions(-)`), rows' files only:
- O1: FIXED in `ops/desk/desk-done.sh`. The title lookup runs only when `name` is not empty; an unnamed session gets no tab.
- O2: FIXED in `ops/desk/desk-done.sh`. Before any stop, the tab to be closed (found or passed) is read with `panes titles <tab>`. A pane titled `cto-desk` or `brain*` there prints `KEPT <id>: tab <tab> also holds a brain or the desk`, exit 1. An unreadable pane list gives `KEPT <id>: pane list unreadable`. The header got one sentence.
- A1: FIXED in `ops/desk/desk-watch.sh` `close_worker`. Each sleep is `min(DESK_WATCH_POLL, close-wait left)`.
- A2: FIXED in `ops/desk/desk-watch.sh` `close_worker`. A non-FAILED prodwrite or close still prints `KEPT <session>: closed through desk-done.sh by the desk` and waits for nothing, and it now appends its FINISHED line. A FAILED prodwrite or close prints the same line as before and writes nothing.
- A3: FIXED in `ops/desk/desk-watch.sh` `close_worker`. Two or more listed rows append one FINISHED line per listed id; none listed still writes `-`.
- One assertion of the build's own test changed, because A2 changes what it pins. In `test_c2_deploy_prodwrite_and_close_kinds` (`tests/ops/test_close_automation_1015.py`), the FINISHED count after DEPLOYED + FAILED deploy + WRITTEN prodwrite went from `== 1` to `== 2`. No test of the files ORDER pins was edited.
- After the fix: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_done.py tests/ops/test_close_automation_1015.py tests/ops/test_desk_watch.py tests/ops/test_stop_guard.py tests/ops/test_install_ops.py` → `228 passed, 15 warnings in 156.03s (0:02:36)`.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` documents these ops scripts (the build's record, `## RECORDS`), so no dated line was written.

## Suites
On the tip `1d229d6a`. DB: none, so W is (a0), (a) with `--deploy-gate`, and (e) (`BUILD-HUB.md` `## W`).
- RESTARTS: `uv run cobalt jobs restarts c7ba742c..HEAD` → the table: two `docs/…build-2026-10-15.{md,result}` `A DOCS -`; `ops/desk/desk-done.sh`, `desk-launch.sh`, `desk-watch.sh`, `stop-guard.py` `M operator script; no Cobalt reader -`; `tests/ops/test_close_automation_1015.py` `A`, `tests/ops/test_desk_done.py` `M`, `test/documentation; no resident -`; last line `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames c7ba742c` → the two build-report docs, `ops/desk/desk-done.sh`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/stop-guard.py`, `tests/ops/test_close_automation_1015.py`, `tests/ops/test_desk_done.py`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh close-automation-1015 offline --deploy-gate` → exit 0, whole: `tests/ops: run (deploy gate)` · `offline 8095/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/close-automation-1015-offline-20261015-124751.log`. In the log, `:885` `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 715.07s (0:11:55)` and `:955` `3767 passed, 1 xfailed, 16 warnings in 864.38s (0:14:24)` (the build's 3762 plus the 5 check tests).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh close-automation-1015 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/close-automation-1015-livenote-20261015-131443.log`. Its one skip (`:56`) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`; it does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3767 passed, 1 xfailed, 16 warnings in 854.57s (0:14:14)`
- `.env`: never present (DB: none, no lock taken). `ls /Users/cobalt/cobalt-wt/close-automation-1015/.env` → `ls: /Users/cobalt/cobalt-wt/close-automation-1015/.env: No such file or directory`. `git status --short --branch` → `## ops/close-automation-1015`.

## Scope
PREFLIGHT's path union (`ops/desk/desk-done.sh`, `desk-launch.sh`, `desk-watch.sh`, `stop-guard.py`, `tests/ops/test_close_automation_1015.py`, `tests/ops/test_desk_done.py`) plus my commits (`ops/desk/desk-done.sh`, `ops/desk/desk-watch.sh`, `tests/ops/test_close_automation_1015.py`, `tests/ops/test_desk_done.py`). Every path is in the `files` of row C1 or C2/C4, or is a test file. Nothing is under `src/`, `configs/` or a fenced path.

## Checked against the branch
- (i) `git log --oneline feecd979..HEAD -- . ":(exclude)docs"` → `1d229d6a fix(close-automation-1015): … (check O1 O2 A1 A2 A3)` · `88c88608 wip(close-automation-1015): check red — O1 O2 A1 A2 A3`. `<tip now>` = `1d229d6a`.
- (ii) `git log --stat --format=%h feecd979..HEAD` → `1d229d6a`: `ops/desk/desk-done.sh | 13`, `ops/desk/desk-watch.sh | 52`, `tests/ops/test_close_automation_1015.py | 3` · `88c88608`: `tests/ops/test_close_automation_1015.py | 33`, `tests/ops/test_desk_done.py | 22` · `4fa96a9c`: the build report and `.result` (docs). Every non-docs path is a row's file or a test file: no WIDENED.
- (iii) `git log --oneline c7ba742c..HEAD -- ops/desk/wait-stop-line.sh ops/desk/desk-list.sh ops/desk/idle-wake.py ops/desk/desk-context.sh ops/desk/bare-guard.py src configs .claude` → empty. `git diff c7ba742c..HEAD --stat -- ops/desk/desk-launch.sh tests/ops/test_desk_watch.py tests/ops/test_stop_guard.py tests/ops/test_install_ops.py tests/ops/test_desk_launch_prechecks.py` → only `ops/desk/desk-launch.sh | 35 +++…` (the build's one block); the four pinned test files are unedited. `install-ops` (`desk-launch.sh:921-949`) is not in the diff.
- (iv) `grep -n -F "def <name>"` → `tests/ops/test_desk_done.py:382` (O1), `:393` (O2); `tests/ops/test_close_automation_1015.py:195` (A1), `:209` (A2), `:219` (A3). Each lies in `88c88608` (red), which sits below `1d229d6a` (fix) in (i).
- (v) `ls <WT>/.env` and `git status --short --branch`: see `## Suites` and CLOSE.
- (vi) `git log --stat --format=%h c7ba742c..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate-list change is owed.
- (vii) card `## RECORDS`: `git -C /Users/cobalt/cobalt diff HEAD --stat -- ops/desk/desk-done.sh tests/ops/test_desk_done.py ops/desk/desk-watch.sh ops/desk/stop-guard.py ops/desk/desk-launch.sh` → nothing (main's working tree is clean on these files). `grep -rn -F "unsettled(" ops tests` → `ops/desk/stop-guard.py:345` (def), `:382` (docstring), `:426` (the one caller, in `desk()`). `grep -rn -F "desk-done.sh" ops/desk` → the callers are `desk-watch.sh:151` and `desk-launch.sh:2320`; every other hit is a comment, a message or the script's own usage. The `rev-parse` records use no listed prefix and were not re-run.
- (viii) L32: this report holds only constructed test values (`aaaa…`, `ffff6666`, `w1:t1`, `x-job`) and this repo's commit ids. No ticker, price or date of his.

## OPEN
none. Every finding is HELD and FIXED.

## CONTINUE
next: none (CHECK DONE)

## DECISIONS
none.

## RECORDS
- Gemini probe: `OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; no seat needed it). The desk may want the probe's Gemini model name looked at before a card that needs house B.
- Dropped findings: none. Every house that sat produced a list. No `REFUSED, not needed` line. No `CONTINUE`. No lock take (DB: none).
- L74: one system block asked for a `Claude-Session:` line in commits. It is recorded under `## L74` and was not followed.
- One builder assertion was changed as part of fix A2 (`## FIXES`).
- The report and `close-automation-check-2026-10-15.result` live on `main` (`/Users/cobalt/cobalt`). My git writes run only in `<WT>` (UNATTENDED RULES CWD), so both are left for the desk to commit together.
- Not opened: `areas/cobalt.md` (WHAT YOU READ (5)). The card, the hub and the code carried what this ops-only check needed. Recorded as a miss of the read list.
- files opened: 13 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` to `## W`), the build report, `ops/desk/desk-done.sh`, `ops/desk/desk-watch.sh`, `ops/desk/desk-list.sh`, `ops/desk/wait-stop-line.sh`, `ops/desk/desk-launch.sh` (`:263-287`, `:918-949`, `:2210-2340`), `tests/ops/test_close_automation_1015.py`, `tests/ops/test_desk_done.py`, `<S>/rulings.md`, `<S>/house-a.md`. Also read, without opening a file: `stop-guard.py` (by `git diff` and `grep`) and the task outputs of the probe, Grok, the gate and `tests/ops`.
- Check of `close-automation-1015`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: close-automation-1015 · pass: 1 · tip: 1d229d6a · house A: Grok FINDINGS: 3 · findings: 5 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8095/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 226015
