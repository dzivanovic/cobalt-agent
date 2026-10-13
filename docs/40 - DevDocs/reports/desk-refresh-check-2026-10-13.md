# Check — desk-refresh-1013 (card 458) — 2026-10-13

## §0 Headline
One pass by house A (Grok, 3 findings) and my own read (2 findings); no house B (Gemini out on a model-name error; the card says `as needed`).
Held and fixed at `824e478b`: O1 (at 300k, an unguarded OWED block wrote the order file and started the refresh without ever showing REFRESH NOW), G1 (with two prefix rows in LIST, the wrong one could be stopped), G2 (a timeout dropped desk-context.sh's first line).
Open, follow-up: O2 (an unreadable LIST launches a successor and skips the stop, as S3 is written) and G3 (child survives `claude stop`: live-only).
Suites: offline 4317/0 · live-note 146/0 · tests/ops 3496 passed (0 failed) · RESTARTS: none · `.env` never present. ready: YES.

## L74
The session's system reminder asked for a `Claude-Session:` trailer on commits (07:19 ET). Recorded once as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "<card>"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/458-desk-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/458-desk-refresh-card.md" · 0 · 902cd0452e676a9050a24ca9bcb3c387f5ea821d
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/458-desk-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · ... · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ... | APPROVED |
STANDING LIST 2026-09-30 R60 committed · ... · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · ... · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " ".../cto-2026-10-12.md" · 0 · 173:| R1138 | 06:10 ET | HIS RULING · APPROVED (...) K1–K5 standing classes ... | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · ... · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · ... · 0 · the row as grepped
AUTHORIZED
```
(Rows shortened with `...` only where the full ruling text repeats; the tool output is in the session.)
House gates: `grep -n "^| R17 "` → line 35 (one row); `grep -n "^| R19 "` → line 37 (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Tue Oct 13 07:19:01 EDT 2026
status · git status --short --branch · 0 · ## ops/desk-refresh-1013
head · git log --oneline -1; git log --stat --format=%h dbc79911..HEAD · 0 · (5 lines)
    27cb4d1e docs(desk-refresh-1013): build report — dbc79911
    27cb4d1e
     .../reports/desk-refresh-build-2026-10-13.md       | 186 +++++++++++++++++++++
     1 file changed, 186 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/desk-refresh-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 ".../desk-refresh-build-2026-10-13.md" · 0 · BUILT · job: desk-refresh-1013 · tip: dbc79911 | on f7d71571 | migration: none | offline 4317/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 205968
range · git log --oneline f7d71571..dbc79911 · 0 · (2 lines)
    dbc79911 feat(desk-refresh-1013): desk size every turn, REFRESH NOW at 300k, forced refresh, wake-up rules (S1 S2 S3 W1, L35 L42 L67)
    43038a8b wip(desk-refresh-1013): red
PREFLIGHT OK
```
THE RANGE `git log --stat --format=%h f7d71571..dbc79911`: dbc79911 → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`; 43038a8b → `tests/ops/test_desk_refresh_wakeup.py`, `tests/ops/test_stop_guard.py`. Path union: those four.
DB: none: `git diff --name-only --no-renames f7d71571..dbc79911` → the same four paths, each under `ops/`, `tests/ops/` or `docs/`.
`ls <S>` → No such file or directory (fresh).
House probes: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings
```
house A: Grok · house B: none (not needed; card `HOUSE B: as needed`). Gemini OUT = HARNESS (model name not recognized; no return time named).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`:
```
29083 <S>/diff.md
21300 <S>/files/458-desk-refresh-card.md
25058 <S>/files/desk-refresh-build-2026-10-13.md
13760 <S>/files/wt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md
27788 <S>/files/wt/ops/desk/stop-guard.py
3226 <S>/files/wt/tests/ops/test_desk_refresh_wakeup.py
39820 <S>/files/wt/tests/ops/test_stop_guard.py
356 <S>/rulings.md
STAGED 8 files · 160391 bytes · commits 2
```
`stage-copy.sh` (each `COPIED <bytes> <dest>`): desk-refresh-answer-2026-10-13.md 3312 · cto-2026-10-13.md 16363 · 446-k5-gate-card.md 35856 · wt/ops/desk/desk-context.sh 3197 · desk-launch.sh 119544 · desk-handover.sh 4726 · wait-desk-idle.sh 1718 · desk-commit.sh 1553 · desk-list.sh 868 · wt/tests/ops/test_desk_wakeup_rule.py 3235 · test_hub_lines.py 13550.
`<S>/HOUSE-INSTRUCTIONS.md` written (HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, Files paragraph).
House A Grok started 07:20:54 ET (`date` before the launch), background task `bzc2bvu4f`; gates rechecked (R17 line 35, R19 line 37); after `cd <WT>`: `## ops/desk-refresh-1013`.

## OWN FINDINGS
Written before any house list was opened.

FINDING O1
ROW: S2 (X2, X3)
CLAIM: `desk()` runs `per_turn` (`ops/desk/stop-guard.py:387`) before the OWED read (`:388`); at 300,000 or more `order()` (`:484-503`) writes the order file and starts the detached `--forced` child, and when the OWED read then raises `Unguarded` (`owed_block` `:279-280`) the hook exits 0 with only `stop-guard: desk not guarded — …`. REFRESH NOW is never shown, yet the order clock runs and the next stop sends WRITE HANDOVER NOW.
RUN: TEST — `tests/ops/test_stop_guard.py`
```python
def test_check_o1_an_unguarded_block_at_300k_gives_no_silent_order(tmp_path):
    d = Sized(tmp_path, n=300000)
    d.lister(DESK_ROW)
    d.owed("owed: none", "OWED: x", stamp())
    r = d.run()
    assert r.returncode == 0 and r.stderr.startswith(UNGUARDED), r.stderr
    assert not d.order.exists(), "the order file was written though REFRESH NOW was never shown"
```
EXPECT: on the tip, `AssertionError: the order file was written though REFRESH NOW was never shown`.

FINDING O2
ROW: S3 (X4)
CLAIM: in `forced()`, an unreadable LIST (`ops/desk/stop-guard.py:577-581`) sets `rows = []`. `others` is then empty, so `desk-launch.sh desk` runs (`:609`), while `ids` is empty, so `claude stop`/`claude rm` are skipped (`:610-613`). Result: a successor is launched beside an old desk that is never stopped, and possibly beside a live successor the LIST could not show. Two desks.
RUN: TEST — `tests/ops/test_stop_guard.py`
```python
def test_check_o2_an_unreadable_list_never_launches_beside_a_live_desk(tmp_path):
    d = Sized(tmp_path)
    d.lister(code=1)
    d.owed("owed: none", stamp())
    d.order.write_text(now_iso() + "\n")
    d.forced()
    calls = d.logged()
    assert "desk-launch.sh desk" not in calls or f"claude stop {SID}" in calls, calls
```
EXPECT: on the tip, `AssertionError: ['desk-commit.sh docs(desk): HANDOVER FORCED 5f91403d …', 'desk-launch.sh desk']`.

## Findings
Grok finished at 07:37:14 ET (`date` at the notice). Its stdout ended with the path of `<S>/house-a.md`, which Grok wrote itself (2281 bytes, `FINDINGS: 3`). There is no house B.
- G1 · Grok · X4 · `own()` takes a shorter listed id that prefixes the session id as the old desk, so a row listed first stops the wrong id · TEST
- G2 · Grok · S1 · a timeout drops desk-context.sh's first output line and prints `timed out after 20 s` · TEST
- G3 · Grok · X5 · the child is detached with `start_new_session=True` and DEVNULL pipes; outliving `claude stop` is UNPROVEN · COMMAND (`grep -n "start_new_session=True" ops/desk/stop-guard.py`)

## Dropped
none (every block carries a `def test_` or a `grep` command)

## RUNS
Each test was put at the end of `tests/ops/test_stop_guard.py` with no change to its form, and run alone with `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py::<test>` on `dbc79911` (tree clean but the added tests).
- O1 · opus-own · `::test_check_o1_an_unguarded_block_at_300k_gives_no_silent_order` · `1 failed` — `E       AssertionError: the order file was written though REFRESH NOW was never shown` (`r.returncode == 0` and the stderr starting `stop-guard: desk not guarded — ` both held, so the first assert passed) · **HELD**
- O2 · opus-own · `::test_check_o2_an_unreadable_list_never_launches_beside_a_live_desk` · `1 failed` — `E       AssertionError: ['desk-commit.sh docs(desk): HANDOVER FORCED 5f91403d …/cto-2026-10-13.md', 'desk-launch.sh desk']` · **REJECTED — S3: "After the waits: a live `cto-desk` row of `desk-list.sh` … → log it, launch nothing. Else, … `sh <here>/desk-launch.sh desk`; `claude stop <id>` then `claude rm <id>`, `<id>` the `desk-list.sh` row id … (no such row: skip both)"**. With an unreadable LIST no live row is seen, so the card's Else branch launches and skips the stop. The test was removed with the Edit tool. OPEN.
- G1 · Grok · `::test_x4_a_shorter_prefix_listed_first_is_stopped` · `1 failed` — `E       AssertionError: ['claude stop 5f91403d']` (`At index 0 diff: 'claude stop 5f91403d' != 'claude stop 5f91403d-3f67-445e-a654-8eedc3cc8a0b'`) · **HELD**. S3 says "the `desk-list.sh` row id that is a prefix of the session id"; with two such rows the card does not pick one, and X4 asks about exactly this wrong stop. The fix keeps the card's prefix rule and takes the `cto-desk` row first.
- G2 · Grok · `::test_s1_a_timeout_keeps_the_first_output_line` · `1 failed` in 20.95 s — `E         - DESK SIZE UNREAD — no transcript for x` / `E         + DESK SIZE UNREAD — timed out after 20 s` · **HELD** (S1: "a timeout: `DESK SIZE UNREAD — <its first output line, or the exit>`")
- G3 · Grok · `grep -n "start_new_session=True" ops/desk/stop-guard.py` → `498:                start_new_session=True,` · **UNSETTLED — the claim is that the child outlives `claude stop` of the old desk, which only a live desk can show; the grep shows the flag only.** OPEN.
Red commit: `d867b9e2 wip(desk-refresh-1013): check red — O1 G1 G2` (`tests/ops/test_stop_guard.py`, 34 insertions).

## FIXES
- O1, G1, G2: `824e478b fix(desk-refresh-1013): per-turn part after the OWED read, timeout keeps the first line, the cto-desk row stopped first (check O1 G1 G2)`, `ops/desk/stop-guard.py` (12+/4−):
  - O1: `desk()` runs `per_turn` after the OWED read, so a raised `Unguarded` (in `owed_block` or `unsettled`) exits before any order file or child exists. The stderr order is unchanged: the turn lines first, the OWED line last.
  - G2: `measure()` on `TimeoutExpired` takes the first line of the output captured so far (bytes decoded) and falls back to `timed out after 20 s`.
  - G1: `forced()` builds `ids` from the prefix rows named `cto-desk` first, then the other prefix rows.
  After the fix: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_desk_refresh_wakeup.py tests/ops/test_idle_wake.py` → `123 passed, 15 warnings in 58.79s` (0 failed).
  DevDocs: `ops/desk/stop-guard.py` has no page under `docs/40 - DevDocs/cobalt/` (Glob `docs/40 - DevDocs/**/*stop-guard*` → prompts and reports only). Following the desk's message (R1339: "the header comment of stop-guard.py is the doc"), each fix carries an in-line `(check <id>)` comment and no page was written.

## Suites
DB: none card, so W is (a0), (a), (e) plus `tests/ops`, on `824e478b`:
- RESTARTS: `uv run cobalt jobs restarts f7d71571..HEAD`, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-refresh-build-2026-10-13.md	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_desk_refresh_wakeup.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames f7d71571` → `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `docs/40 - DevDocs/reports/desk-refresh-build-2026-10-13.md`, `ops/desk/stop-guard.py`, `tests/ops/test_desk_refresh_wakeup.py`, `tests/ops/test_stop_guard.py`, each under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 5 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-refresh-1013 offline` → `offline 4317/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-refresh-1013-offline-20261013-074030.log` (exit 0).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-refresh-1013 livenote` → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-refresh-1013-livenote-20261013-074034.log` (exit 0).
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3496 passed, 1 xfailed, 16 warnings in 736.43s (0:12:16)` (exit 0). That is the build's 3493 plus the 3 check tests.
- with-DB: not run (DB: none); no lock taken. `.env`: `ls /Users/cobalt/cobalt-wt/desk-refresh-1013/.env` → No such file or directory (never present).

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` (W1), `ops/desk/stop-guard.py` (S1–S3), `tests/ops/test_stop_guard.py` (S1–S3), `tests/ops/test_desk_refresh_wakeup.py` (W1). My commits: `tests/ops/test_stop_guard.py` and `ops/desk/stop-guard.py`, both in the rows' `files`. Nothing in the fence.

## Checked against the branch
- (i) `git log --oneline dbc79911..HEAD -- . ":(exclude)docs"` → `824e478b fix(desk-refresh-1013): …(check O1 G1 G2)` · `d867b9e2 wip(desk-refresh-1013): check red — O1 G1 G2`. `<tip now>` = `824e478b`.
- (ii) `git log --stat --format=%h dbc79911..HEAD` → `824e478b` `ops/desk/stop-guard.py` (row S1–S3 file) · `d867b9e2` `tests/ops/test_stop_guard.py` (test file) · `27cb4d1e` the build report (docs). Nothing WIDENED.
- (iii) `git log --oneline f7d71571..HEAD -- src configs .claude ops/desk/desk-context.sh ops/desk/desk-launch.sh ops/desk/desk-handover.sh ops/desk/wait-desk-idle.sh ops/desk/desk-list.sh ops/desk/desk-commit.sh ops/desk/bare-guard.py ops/desk/idle-wake.py` → empty.
- (iv) `grep -n -F "def <test>" tests/ops/test_stop_guard.py`: O1 → `1096:`, G1 → `1105:`, G2 → `1116:`, one line each. `d867b9e2` (red) sits below `824e478b` (fix) in (i).
- (v) see `## Suites` (`.env`) and the closing `git status`.
- (vi) `git log --stat --format=%h f7d71571..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no migration and no with-DB test, so no gate lists are carried.
- (vii) card RECORDS: `git log -1 --format=%h f7d71571 -- <the three files>` → `bc25c523` (as recorded) · `grep -c -F "GAVE UP after 3 blocks" /Users/cobalt/cobalt-wt/.job-state/DESK-STOP` → `22` (as recorded) · `grep -c -F "session list unreadable" …/DESK-STOP` → `0` (as recorded) · `ls /Users/cobalt/cobalt/tests/ops/test_desk_refresh_wakeup.py` → No such file (main, before the merge, as recorded). Not run: `git -C /Users/cobalt/cobalt rev-parse` and `git -C … status` (neither is a listed prefix).
- (viii) L32: this report holds no ticker, price or trading date of his. The ids are the test constant `SID` and the session ids the card itself carries.

## OPEN
- O2 · REJECTED — S3's Else branch. When `desk-list.sh` fails in `forced()`, the refresh still runs `desk-launch.sh desk` and skips `claude stop`/`claude rm`. The result is a successor beside the old desk, and maybe beside a live successor the LIST could not show. The run showed the call log `['desk-commit.sh …', 'desk-launch.sh desk']`. To settle: a card line deciding whether an unreadable LIST launches, refuses, or retries. The test text is under `## OWN FINDINGS`.
- G3 · UNSETTLED — live-only. Whether the detached `--forced` child (`start_new_session=True`, DEVNULL pipes, `ops/desk/stop-guard.py:498`) outlives the old desk's `claude stop`. To settle: the first live forced refresh, where a `DESK-REFRESH` line `claude rm <id>` must follow the `claude stop <id>` line.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
House B was `none available` (Gemini out), so the open items are listed here once more. They ship to the follow-up list:
- O2 (above): the forced refresh on an unreadable LIST launches a successor without stopping the old desk. Default taken: left as S3 is written (REJECTED), with no fix.
- G3 (above): the child's survival past `claude stop` is UNPROVEN. Default taken: shipped; the first live forced refresh's `DESK-REFRESH` lines prove it or disprove it.

## RECORDS
- Grok produced `house-a.md` itself (`FINDINGS: 3`); its stdout ended with the path. Gemini was OUT at the probe: `error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` (HARNESS; not launched; the card does not need house B).
- Dropped findings: none.
- REFUSED, not needed: none. CONTINUED: none. No lock take (DB: none).
- L74: the session's system reminder asked for a `Claude-Session:` commit trailer. It is recorded under `## L74` and was not acted on.
- A message from `cto-desk` arrived at 07:19 ET: "FOR THE CHECK: card 458 build 2026-10-13 brain: E2, ASK 1 and ASK 2 KEEP (a test that pins BASE behaviour is shown red by its mutation; a non-numeric wait is refused and logged, untested; the header comment of stop-guard.py is the doc). Desk row R1339." Recorded as a fact; it grants nothing. It was used only for the DevDocs line under `## FIXES`.
- CHECK ASKS, as run: X1 — `tests/ops` and `test_stop_guard.py` green, and the existing tests are unedited (`git show dbc79911 -- tests/ops/test_stop_guard.py` touches only a new test); with no `desk-context.sh`, `per_turn` returns `[]`. X2 — `test_s1_the_continuation_stop_runs_no_size` green; the size-only branch writes `0`. X3 — REFRESH NOW is pinned byte for byte, and the 299,999 / 300,000 edge is pinned. X4 — G1 fixed; O2 open. X5 — G3 UNSETTLED (live-only); the hook does not wait on `Popen`. X6 — the OWED read and the QUEUE read are unchanged; the stamp is read anywhere up to the next `## `.
- files opened: 14 — CHECK-HUB.md, the card, the house-probe output, `ops/desk/stop-guard.py`, `ops/desk/desk-context.sh`, `tests/ops/test_stop_guard.py` (parts), `ops/desk/desk-launch.sh` (360-373, 540-567), the build report (`## RESTARTS` to the end), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), the Grok task output, `<S>/house-a.md`, BUILD-HUB.md (`## THE LOCK`, E2–W), the live-note gate output and the offline gate output. Plus the diffs by `git diff` / `git show`.
- Check of `desk-refresh-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: desk-refresh-1013 · pass: 1 · tip: 824e478b · house A: Grok FINDINGS: 3 · findings: 5 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 182458
