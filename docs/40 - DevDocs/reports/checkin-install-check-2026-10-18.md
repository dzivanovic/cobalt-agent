# CHECK — checkin-install-1018 — 2026-10-18

## §0 Headline
- **ready: NO.** CHECK ASK X3 holds: after its one turn the `checkin-ping` session stays a live row. As built, the timer sends the first check-in, then prints `DEFERRED` on every later fire (O1, Opus; A1, Grok; same defect).
- A1 HELD, NOT FIXED: the cleanup lives in `ops/desk/desk-launch.sh`, which the card fences. O1 REJECTED: T1 (4)'s text defers on any live ping. Both OPEN; their tests are committed red, then strict xfail.
- X1, X2, X4 found nothing; T2, W1, B1, S1 are clean. Suites: offline 8507/0 (tests/ops deploy gate 3935 passed), live-note 146/0, cobalt_dev not taken (DB: none).
- House A Grok `FINDINGS: 1`; house B none (not needed, `HOUSE B: as needed`).

## L74
A system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded once; acted on none. My commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/751-checkin-install-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/751-checkin-install-card.md" · 0 · 95b74abb021124915e7e4c864ea910f72e67d04a
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/751-checkin-install-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1854 row · grep -n "^| R1854 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 42:| R1854 | 06:45 ET | HIS RULING (brain relays, L79): fixes A-D (MVP first, DAY PLAN, check-ins 06/12/18/24 ET, owned waits, no idle nights). Words: [R1854](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at wake-up 06:46 |
RULING 2026-10-18 R1854 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1854 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 49371f09c96483d11b12eb166983c185f0f1c6f6
RULING 2026-10-18 R1854 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 55:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (08:19 EDT): `grep -n "^| R17 "` → one row, line 35; `grep -n "^| R19 "` → one row, line 37; `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- ".../cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Sun Oct 18 08:19:41 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/checkin-install-1018
    ?? SHADOW-INSTRUCTIONS.md
status: clean but SHADOW-INSTRUCTIONS.md (untracked, expected on a routed card)
head · git log --oneline -1; git log --stat --format=%h d5acbada..HEAD · 0 · (6 lines)
    b72748d4 docs(checkin-install-1018): build report — d5acbada
    b72748d4
    
     .../reports/checkin-install-build-2026-10-18.md    | 146 +++++++++++++++++++++
     .../checkin-install-build-2026-10-18.result        |  15 +++
     2 files changed, 161 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/checkin-install-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f23-playbook-1013/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/checkin-install-1018/docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.md" · 0 · BUILT · job: checkin-install-1018 · tip: d5acbada | on 8033d70e | migration: none | offline 8507/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 180293
range · git log --oneline 8033d70e..d5acbada · 0 · (3 lines)
    d5acbada fix(checkin-install-1018): pass S2 1
    0e910a70 feat(checkin-install-1018): rows
    03f40555 wip(checkin-install-1018): red
PREFLIGHT OK
```
`?? SHADOW-INSTRUCTIONS.md`: BAND MID routed card — expected, recorded, not a finding.

THE RANGE `git log --stat --format=%h 8033d70e..d5acbada` · exit 0:
```
d5acbada
 tests/ops/test_checkin_install_1018.py | 7 +++++--
0e910a70
 docs/40 - DevDocs/prompts/BRAIN-HUB.md       |   3 +
 docs/40 - DevDocs/prompts/CHECKIN-PING.md    |   6 ++
 docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md |   4 +
 docs/40 - DevDocs/prompts/STANDING-LIST.md   |  14 +++
 ops/desk/checkin-timer.sh                    | 141 +++++++++++++++++++++++++++
 ops/desk/com.cobalt.checkin-timer.plist      |  38 ++++++++
03f40555
 tests/ops/test_checkin_install_1018.py | 327 +++++++++++++++++++++++++++++++++
```
DB: none — `git diff --name-only --no-renames 8033d70e..d5acbada` · exit 0: `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/CHECKIN-PING.md`, `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/checkin-timer.sh`, `ops/desk/com.cobalt.checkin-timer.plist`, `tests/ops/test_checkin_install_1018.py` — every path under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` · exit 1 · `No such file or directory` → fresh.
House probes `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0 · lines whole: `grok: UP` · `gemini: UP`.
house A: Grok · house B: none (not needed) — card `HOUSE B: as needed`; no `HOUSE A: OpenAI` header line (OpenAI not probed).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/checkin-install-1018-check`):
```
28 <S>/STAGED-CARD
23265 <S>/diff.md
18169 <S>/files/751-checkin-install-card.md
17648 <S>/files/checkin-install-build-2026-10-18.md
7849 <S>/files/wt/docs/40 - DevDocs/prompts/BRAIN-HUB.md
793 <S>/files/wt/docs/40 - DevDocs/prompts/CHECKIN-PING.md
14844 <S>/files/wt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md
47651 <S>/files/wt/docs/40 - DevDocs/prompts/STANDING-LIST.md
6099 <S>/files/wt/ops/desk/checkin-timer.sh
1832 <S>/files/wt/ops/desk/com.cobalt.checkin-timer.plist
12348 <S>/files/wt/tests/ops/test_checkin_install_1018.py
733 <S>/rulings.md
STAGED 12 files · 151259 bytes · commits 3
```
`commits 3` = PREFLIGHT's range count (3). `stage-copy.sh`, each exit 0:
`COPIED 66534 <S>/files/brain-direction-2026-10-02.md` · `COPIED 5344 <S>/files/draft-desk-refresh-2026-10-13.md` · `COPIED 6897 <S>/files/wt/ops/desk/close-timer.sh` · `COPIED 2112 <S>/files/wt/ops/desk/com.cobalt.close-timer.plist` · `COPIED 16055 <S>/files/wt/tests/ops/test_close_timer.py` · `COPIED 136832 <S>/files/wt/ops/desk/desk-launch.sh` · `COPIED 76069 <S>/files/wt/tests/ops/test_desk_launch_prechecks.py` · `COPIED 12098 <S>/files/wt/src/cobalt/jobs/restarts.py` · `COPIED 13611 <S>/files/wt/tests/ops/test_hub_lines.py` · `COPIED 2723 <S>/files/wt/tests/ops/test_desk_refresh_wakeup.py` · `COPIED 3235 <S>/files/wt/tests/ops/test_desk_wakeup_rule.py` · `COPIED 21839 <S>/files/wt/tests/ops/test_desk_launch_brain.py`.
Not copied: `M/topics/cto-desk-contract.md` (a vault note, `## 1` (3)).
`<S>/HOUSE-INSTRUCTIONS.md` written: HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
House start 08:21 EDT: gates re-run (R17 line 35, R19 line 37, `5055151d…` non-empty); `ls -la <S>` listed; `cd <AGY>`; Grok started `run_in_background` (task `b0r9t8df5`); `cd <WT>`; `git status --short --branch` → `## ops/checkin-install-1018` + `?? SHADOW-INSTRUCTIONS.md` (routed card, expected). House B: none (not needed).

## OWN FINDINGS
Written by 08:23 EDT (`date`), before any house list was opened.

FINDING O1
ROW: X3 (T1 step 4)
CLAIM: `ops/desk/checkin-timer.sh:108-121` defers on ANY live `checkin-ping` row, but a finished `claude --bg` session keeps its pid and shows `idle` (the launcher replaces exactly such idle same-name rows for card kinds, `ops/desk/desk-launch.sh:2364-2397`; `ops/desk/wait-stop-line.sh:25-28` reads `idle` rows as alive, `gone` only when no row), and the kind `prompt` exits in `run_launch` at `ops/desk/desk-launch.sh:749` before that replacement, so nothing ever closes the first ping: every later fire prints `DEFERRED` and no check-in after the first is sent.
RUN: TEST — `tests/ops/test_checkin_install_1018.py`:
```python
def test_x3_a_finished_ping_row_does_not_defer_the_next_fire(box):
    # a ping whose one turn ended: status `idle`, state not `working` (wait-stop-line.sh:25-28)
    finished = "dddd4444-0000-4000-8000-000000000004 · checkin-ping · ~/cobalt · idle · done"
    box.rows.write_text(CTO + "\n" + finished + "\n")
    done = box.run()
    assert done.returncode == 0, done.stderr
    assert "DEFERRED" not in done.stdout
    prompt = box.repo / "docs" / "40 - DevDocs" / "prompts" / "CHECKIN-PING.md"
    assert box.calls_made() == [f"prompt {prompt}"]
```
EXPECT: red at `assert "DEFERRED" not in done.stdout` (stdout `DEFERRED: ping live — dddd4444-…`).

Read and found nothing runnable to hand over: X1 (the dry test drives the real launcher's kind `prompt`; `tools()` pins the three strings), X2 (each of steps 1–3 has its test, notify counts asserted exactly), X4 (the three fixed files' diff is additions only, at the rows' places), T2, W1, B1, S1. Build report: its stop line's `RESTARTS:` carries six residents from the untracked `SHADOW-INSTRUCTIONS.md` (its DECISION 1); the committed range classifies with no restart — recorded under `## RECORDS`, settled by this check's own derivation at `## 6`.

## Findings
Grok finished 08:31 EDT (task `b0r9t8df5`, exit 0; stdout: its path, then `[exited with code 0]`). `ls -la <S>` → `house-a.md` 2498 bytes, 08:31. Its list ends `FINDINGS: 1`. House B: none (not needed).
`grep -n -F "RUN:"` on `house-a.md` → `4:RUN: TEST — tests/ops/test_checkin_install_1018.py`, followed by `def test_` at line 6: kept.

| id | house | row | claim | run |
|---|---|---|---|---|
| A1 | Grok | X3 | kind `prompt` exits in `run_launch` before the only `desk-done.sh` cleanup, so a finished `checkin-ping` stays a live row and `checkin-timer.sh` defers every later fire | TEST |

## Dropped
none

## RUNS
Both tests pasted into `tests/ops/test_checkin_install_1018.py` by Edit, unchanged (no form repair). Context fact for both: `sh /Users/cobalt/cobalt/ops/desk/desk-list.sh` (08:33 EDT) lists rows whose turn has ended still live with a pid, e.g. `bede3dc9 · brain · ~/cobalt · idle · working` and `c268db2c · strike-fallback-env-1018-gemini-gate · … · idle · blocked`. A `claude --bg` seat stays a live row after its turn ends.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_checkin_install_1018.py::test_x3_a_finished_ping_row_does_not_defer_the_next_fire` | `1 failed, 15 warnings in 1.53s` · first failing line `E       AssertionError: assert 'DEFERRED' not in 'DEFERRED: p...0000000004\n'` (`DEFERRED: ping live — dddd4444-0000-4000-8000-000000000004`) | REJECTED — T1 (4) "a live row named exactly `checkin-ping` → `DEFERRED: ping live — <id>`, exit 0": the script does what the row says. The defect is the row's design: the finished ping is never closed. Stays OPEN |
| A1 | Grok | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_checkin_install_1018.py::test_x3_a_finished_ping_is_not_left_as_a_named_session` | `1 failed, 15 warnings in 1.51s` · first failing line `E       AssertionError: ["--bg Read '…/CHECKIN-PING.md' and follow it exactly. --model claude-sonnet-5-5 --permission-mode auto --remote-control checkin-ping --name checkin-ping --allowedTools Read SendMessage Bash(date*) --disallowedTools AskUserQuestion EnterWorktree Bash(git push*)"]`: the real kind `prompt` runs the one `--bg` call and no cleanup | HELD, NOT FIXED — `ops/desk/desk-launch.sh` (the kind `prompt` exits in `run_launch` at `:749` before the same-name replacement at `:2364-2397`; the card fences `desk-launch.sh`: "no change") |

HELD tests committed before any fix: `d614e296 wip(checkin-install-1018): check red — O1 A1` (both tests; O1's stays as the OPEN item's test). Both are passed to W as `--deselect` (`## 6`).

## FIXES
- A1: HELD, NOT FIXED — `ops/desk/desk-launch.sh` (fenced; `## DECISIONS` D1).
- No fix commit: the only fix inside the rows' files (O1, `checkin-timer.sh` step 4) would contradict T1 (4)'s text. REJECTED, OPEN, `## DECISIONS` D1.

## Suites
RESTARTS: `uv run cobalt jobs restarts 8033d70e..HEAD` (exit 1), table whole:
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/prompts/BRAIN-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECKIN-PING.md	A	DOCS	-
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.md	A	DOCS	-
docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.result	A	DOCS	-
ops/desk/checkin-timer.sh	A	operator script; no Cobalt reader	-
ops/desk/com.cobalt.checkin-timer.plist	A	operator script; no Cobalt reader	-
tests/ops/test_checkin_install_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The only UNCLASSIFIED row is the untracked `SHADOW-INSTRUCTIONS.md` (routed card, never committed). Every committed path derives no restart. Classifying it would mean editing `configs/`, which a DB: none card does not allow: not made, D2.
W (DB: none: (a0), (a), (e)):
- (a0) `git diff --name-only --no-renames 8033d70e` → the 7 row paths + `docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.md` + `.result`. Every path is under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 9 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh checkin-install-1018 offline --deploy-gate` (08:33 EDT, exit 0), verdict lines whole:
  `tests/ops: run (deploy gate)` · `offline 8507/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/checkin-install-1018-offline-20261018-083339.log`. `grep -c -F "OUTSIDE the allowed set" <log>` → `0`. `grep -n -F "xfailed" <log>` → `888:4572 passed, 806 skipped, 1 xfailed, 36 warnings in 771.02s (0:12:51)` · `960:3935 passed, 3 xfailed, 16 warnings in 984.02s (0:16:24)`. The tests/ops run is the (a0) `tests/ops` pytest: 3935 passed, 0 failed. Its 3 xfailed = the existing 1 + the check's 2 strict xfails (O1, A1).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh checkin-install-1018 livenote` (exit 0): `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/checkin-install-1018-livenote-20261018-090321.log`.
- With-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/checkin-install-1018/.env` → `No such file or directory` (09:04 EDT). `git status --short --branch` → `## ops/checkin-install-1018` + `?? SHADOW-INSTRUCTIONS.md` (routed card, expected).
- New tests shown red first: both (`## RUNS`), then marked strict xfail.

## Scope
PREFLIGHT's path union (7 paths) = the rows' `files`: `ops/desk/checkin-timer.sh` (T1), `ops/desk/com.cobalt.checkin-timer.plist` (T2), `docs/40 - DevDocs/prompts/CHECKIN-PING.md` (P1), `CTO-DESK-WAKEUP.md` (W1), `BRAIN-HUB.md` (B1), `STANDING-LIST.md` (S1), `tests/ops/test_checkin_install_1018.py` (all rows). My commits touch only `tests/ops/test_checkin_install_1018.py`. X4: `git diff 8033d70e..d5acbada` of the three fixed files holds only `+` lines: 3 (B1, between `## HOW YOU ANSWER A JUDGE REQUEST` and `## MEASURE`), 4 (W1, after the last `ON TRIGGER` row), 14 (S1, after §9; the last of them is a blank line at end of file). No removed line.

## Checked against the branch
- (i) `git log --oneline d5acbada..HEAD -- . ":(exclude)docs"` → `3108359f wip(checkin-install-1018): check — O1 A1 strict xfail until the fix round` · `d614e296 wip(checkin-install-1018): check red — O1 A1`. `<tip now>` = `3108359f`.
- (ii) `git log --stat --format=%h d5acbada..HEAD` → `3108359f` and `d614e296`: `tests/ops/test_checkin_install_1018.py` only; `b72748d4`: the build report and its `.result` (docs). No other path: no WIDENED.
- (iii) `git log --oneline 8033d70e..HEAD -- ops/desk/stop-guard.py tests/ops/test_stop_guard.py ops/desk/close-timer.sh ops/desk/com.cobalt.close-timer.plist tests/ops/test_close_timer.py ops/desk/desk-launch.sh` → empty.
- (iv) `grep -n -F "def test_x3_a_finished_ping" tests/ops/test_checkin_install_1018.py` → `194:def test_x3_a_finished_ping_row_does_not_defer_the_next_fire(box):` · `206:def test_x3_a_finished_ping_is_not_left_as_a_named_session(desk, tmp_path):`. Both in `d614e296` (red). No `fix(<JOB>):` commit: neither is fixed. `3108359f` adds `@pytest.mark.xfail(strict=True, …)` to each, assertions unchanged: once fixed they XPASS and a strict xfail turns red, so the fix round must remove the marker.
- (v) `ls <WT>/.env` → `No such file or directory`. `git status --short --branch`: see `## Suites`.
- (vi) `git log --stat --format=%h 8033d70e..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate-lists row owed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt log -1 -S "| R1854 |"` → `49371f09…` (AUTHORIZATION); `… -S"| R1841 |"` → `7317d540`; `wc -l ops/desk/close-timer.sh` → `164` (matches "164 lines"); `grep -rln "close" ops/ "--include=*.plist"` → `ops/desk/com.cobalt.close-timer.plist`, `ops/com.cobalt.cards-expire.plist` (the record names the first only; the pattern file is the first). The WAKE PATH `grep -rn -E "…|…"` is a regex alternation, which this file's form rule does not allow (plain fixed strings only): not run. The BASE `ls` absences are shown by the range: each of the four files is `A` in the RESTARTS table.
- (viii) L32: this report holds constructed ids and session names only. No ticker, price or date of his.

## OPEN
- O1 (Opus) · REJECTED — T1 (4). The timer defers on any live `checkin-ping` row, and a finished `--bg` ping stays a live row (desk-list shows ended turns as `idle · working` / `idle · blocked`). After the first check-in, every later fire prints `DEFERRED`. Settled by: a desk ruling on the ping's close, which the fix round builds. Either the timer closes an idle `checkin-ping` (`desk-done.sh <id>`) before launching, or the kind `prompt` replaces same-name idle rows as the card kinds do. Then `test_x3_a_finished_ping_row_does_not_defer_the_next_fire` passes and loses its xfail marker.
- A1 (Grok) · HELD, NOT FIXED — `ops/desk/desk-launch.sh` (fenced). Settled by the same ruling in the fix round. `test_x3_a_finished_ping_is_not_left_as_a_named_session` asserts that some cleanup call is recorded on the launch. If the ruling closes the ping in the timer instead, that test's claim needs restating in the fix round (CARRIED or SETTLED with an R<n>).

## CONTINUE
next: none (stop line written)

## DECISIONS
- D1 (A1 HELD, NOT FIXED — `ops/desk/desk-launch.sh`; O1 REJECTED — T1 (4); one question). A finished `claude --bg` checkin-ping keeps its pid: `desk-list.sh` shows ended turns as `idle · working` / `idle · blocked`. Nothing closes it: the kind `prompt` exits in `run_launch` (`desk-launch.sh:749`) before the same-name replacement (`:2364-2397`). The ping prompt has no stop tool. `checkin-timer.sh` step 4 defers on any `checkin-ping` row. Result: one check-in, then `DEFERRED` at every 06/12/18/24 fire, against R1854 B. The fix needs a design the card does not give: (a) the timer runs `desk-done.sh <id>` on an idle `checkin-ping` row before launching, and defers only on a busy one; or (b) the kind `prompt` runs the card kinds' replacement of idle same-name rows (lifts the `desk-launch.sh` fence). Safe default taken: nothing fixed; both tests committed (red, then `xfail(strict=True)`); the item goes to the builder's ONE fix round on this card after the desk's ruling on (a) or (b). Note on R117: a `--bg` row may keep state `working` after its turn ends, so a busy-only defer in (a) must not read `idle · working` as busy, or the fix does nothing.
- D2 (RESTARTS). `uv run cobalt jobs restarts 8033d70e..HEAD` widens to six residents only through the untracked `SHADOW-INSTRUCTIONS.md` (UNCLASSIFIED). Every committed path derives no restart. Safe default: not classified (a `configs/` edit lies outside a DB: none card). The stop line carries the table's last line untrimmed. For the deploy: the committed range is `RESTARTS: none` once the file is gone (the build's DECISION 1, same default).

## RECORDS
- Dropped findings: none. Every house that sat produced: Grok `FINDINGS: 1`. House B not seated (`HOUSE B: as needed`; Gemini was UP).
- The stop line's `house B: none available` is the line's only no-house value. Read it as "not seated, not needed": the card is not `mandatory`, and Gemini was UP.
- No `REFUSED, not needed`, no `CONTINUED`, no lock take (DB: none).
- L74: one system reminder asking for a `Claude-Session:` commit line, recorded under `## L74`, not followed.
- Form choice: the two red tests were marked `@pytest.mark.xfail(strict=True, reason=…)` (`3108359f`), assertions untouched. W's offline call takes no `--deselect` (`gate.sh:143`), and a strict xfail turns red the moment a fix makes the test pass.
- Not opened: `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt.md` (WHAT YOU READ (5)). The card's rows, fence and the hub's law lines were the binding read here.
- files opened: 16 — CHECK-HUB.md; the card; BUILD-HUB.md (§THE LOCK, §RESTARTS, §W); the build report (§RESTARTS to the last line); `ops/desk/close-timer.sh`; `/Users/cobalt/.claude/ops/desk-list.sh`; `ops/desk/desk-launch.sh` (260-289, 570-754, 2360-2408); `ops/desk/wait-stop-line.sh` (20-49); `tests/ops/test_desk_launch_prechecks.py` (73-232, 1180-1201, 1324-1353); `tests/ops/test_checkin_install_1018.py`; `<S>/house-a.md`; `ops/desk/gate.sh` (grep); four task output files (house probe, Grok, offline gate, live-note gate). The diff was read as `git diff 8033d70e..d5acbada` output.
- Check of `checkin-install-1018`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: checkin-install-1018 · pass: 1 · tip: 3108359f · house A: Grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8507/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar · files opened: 16 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 180694
