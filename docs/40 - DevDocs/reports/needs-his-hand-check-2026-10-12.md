# needs-his-hand-1012 — CHECK (CHECK-HUB.md, card 2026-10-12/393)

## §0 Headline
Check of `needs-his-hand-1012` at `ad73d04a`. House A Grok found nothing; house B was not needed.
I wrote 4 findings: 2 NOT HELD and 2 REJECTED (open). Nothing held, so nothing was fixed and nothing was committed.
The two open items: on the day-open's S0 path the seat has no allowed way to write the new section, and the anchor "above that last line" does not exist there. The card's text orders that wording, so this goes to the desk.
Suites: offline 4199/0, live-note 146/0, tests/ops 3143 passed. RESTARTS: none. ready: YES.

## L74
A system reminder at session start asked commits to end with a `Claude-Session:` line. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md" · 0 · b7419d552da8386933baf3640acf87c002731208
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/393-needs-his-hand-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 22:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
HOUSE GATES: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, the standing `Bash(grok *)`); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37, the four house strings standing); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Mon Oct 12 06:59:23 EDT 2026
status · git status --short --branch · 0 · ## ops/needs-his-hand-1012
head · git log --oneline -1; git log --stat --format=%h ad73d04a..HEAD · 0 · (5 lines)
    c2352cb8 docs(needs-his-hand-1012): build report — ad73d04a
    c2352cb8
    
     .../reports/needs-his-hand-build-2026-10-12.md     | 177 +++++++++++++++++++++
     1 file changed, 177 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/needs-his-hand-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/needs-his-hand-1012/docs/40 - DevDocs/reports/needs-his-hand-build-2026-10-12.md" · 0 · BUILT · job: needs-his-hand-1012 · tip: ad73d04a | on 6468fb5e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 130764
range · git log --oneline 6468fb5e..ad73d04a · 0 · (2 lines)
    ad73d04a feat(needs-his-hand-1012): NEEDS HIS HAND section in the close and day-open prompts (N1, L81, L1, L28)
    cd13e4e8 wip(needs-his-hand-1012): red
PREFLIGHT OK
```
THE RANGE: `git log --stat --format=%h 6468fb5e..ad73d04a` · exit 0:
```
ad73d04a
 docs/40 - DevDocs/prompts/CLOSE-HUB.md     | 3 ++-
 docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md | 1 +
 2 files changed, 3 insertions(+), 1 deletion(-)
cd13e4e8
 tests/ops/test_needs_his_hand.py | 94 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 94 insertions(+)
```
Path union: `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md`, `tests/ops/test_needs_his_hand.py`.
DB: none: `git diff --name-only --no-renames 6468fb5e..ad73d04a` · exit 0 → the three paths above; each under `docs/` or `tests/ops/`.
`ls <S>` · exit 1 · `No such file or directory` (fresh).
HOUSE PROBES: `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: UP
```
house A: Grok (grok-4.7) · house B: none (not needed — card `HOUSE B: as needed`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0:
```
4174 <S>/diff.md
10657 <S>/files/393-needs-his-hand-card.md
18455 <S>/files/needs-his-hand-build-2026-10-12.md
15331 <S>/files/wt/docs/40 - DevDocs/prompts/CLOSE-HUB.md
4030 <S>/files/wt/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md
3539 <S>/files/wt/tests/ops/test_needs_his_hand.py
355 <S>/rulings.md
STAGED 7 files · 56541 bytes · commits 1
```
`commits 1` against PREFLIGHT's range of 2: the staged diff is `-- . ":(exclude)docs"`, and only `cd13e4e8` touches a non-docs path (`ad73d04a` touches only the two prompts under `docs/`). The count matches the command's own range. Because of that exclusion the prompts' diff was not in `diff.md`; it was saved by `git diff 6468fb5e..ad73d04a -- <the two prompts>` (background) and written whole to `<S>/files/prompts-diff.md` (the Write tool; `stage-copy.sh` refused the temp source: `REFUSED: the source is not under a job worktree or the main tree's docs/`).
`stage-copy.sh` → `COPIED 5788 <S>/files/hands-off-answer-2026-10-12.md` · `COPIED 7094 <S>/files/cto-2026-10-12.md` · `COPIED 11448 <S>/files/wt/tests/ops/test_hub_lines.py` · `COPIED 12847 <S>/files/361-held-table-row-card.md`.
`<S>/HOUSE-INSTRUCTIONS.md` written (12987 bytes): HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, the Files paragraph.
House A Grok started 07:01 EDT (`date` 07:01:35; gates R17, R19 re-grepped, one row each), `run_in_background`, timeout 2700000. House B: none (not needed).

## OWN FINDINGS
Written before either house list was opened (house A's completion, if any, not read).

FINDING O1
ROW: N1 (the S0 path), X3
CLAIM: The day-open line (`docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md:29`) tells the seat on the S0 path to "append it to the file the command wrote", but the command's own docstring names `cobalt day-open verdict` as "the local seat's only write path under the Qwen allowlist" (`src/cobalt/dayopen/cli.py:10-12`), and that path writes only a `SEAT VERDICT:` line (`src/cobalt/dayopen/report.py:122`); the seat has no allowed way to write the section there.
RUN: COMMAND `grep -n -F "the local seat's only write" src/cobalt/dayopen/cli.py`
EXPECT: `11:`SEAT VERDICT:` line to that day's report — the local seat's only write`

FINDING O2
ROW: N1 (the S0 path)
CLAIM: "Above that last line" (`DAY-OPEN-QWEN.md:29`) anchors on the `NEXT:` last line of `:28`, but the file the S0 command writes has no `NEXT:` line (`src/cobalt/dayopen/report.py:54-68` ends with the VERDICT section and `OVERALL:`; `:122` appends `SEAT VERDICT:`), so on that path the anchor does not exist.
RUN: COMMAND `grep -n -F "NEXT" src/cobalt/dayopen/report.py`
EXPECT: no output (exit 1).

FINDING O3
ROW: X2
CLAIM: The prompts' diff holds a changed line beyond THE TEXT's three (the chain edit, the close line, the day-open line), or touches `CLOSE-HUB.md:10`.
RUN: COMMAND `git diff --stat 6468fb5e..ad73d04a -- "docs/40 - DevDocs/prompts/CLOSE-HUB.md" "docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md"`
EXPECT: more than `3 insertions(+), 1 deletion(-)` if the claim holds.

FINDING O4
ROW: X4
CLAIM: An existing test or script reads the close's shape chain or the day-open's `Table:` line, so the edit could change its result.
RUN: COMMAND `grep -rn -F "shaped:" tests ops` (and the same for `Table: check`, `## REPORT (L48)`, `NEEDS`)
EXPECT: a hit outside `tests/ops/test_needs_his_hand.py` if the claim holds.

## Findings
House A Grok finished 07:12 EDT (`date` 07:12:34; task exit 0). `<S>/house-a.md` (12 bytes, written by Grok) reads whole: `FINDINGS: 0`. Its stdout: "The prompts, the new test, and the diff match the row. No runnable defect." House B: none (not needed).
No house finding to keep.

## Dropped
none (house A wrote no FINDING block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -n -F "the local seat's only write" src/cobalt/dayopen/cli.py` | `11:`SEAT VERDICT:` line to that day's report — the local seat's only write` | REJECTED — card THE TEXT, `DAY-OPEN-QWEN.md` line quoted "byte for byte" incl. "(on the S0 path too: append it to the file the command wrote)", and the fence "The day-open command's own report writer (`cobalt day-open`): its output is not edited here; the seat appends the section". The output shows the claim, but the card orders this text. OPEN |
| O2 | own | `grep -n -F "NEXT" src/cobalt/dayopen/report.py` | no output, exit 1 | REJECTED — the same card line and fence as O1: the S0 file has no `NEXT:` line, so "Above that last line" has no anchor on that path. OPEN |
| O3 | own | `git diff --stat 6468fb5e..ad73d04a -- <the two prompts>` | `CLOSE-HUB.md | 3 ++-` · `DAY-OPEN-QWEN.md | 1 +` · `2 files changed, 3 insertions(+), 1 deletion(-)` | NOT HELD (the full diff, saved at staging, shows exactly the chain edit and the two new lines; `CLOSE-HUB.md:10` is not in the diff) |
| O4 | own | `grep -rn -F "shaped:" tests ops` · `grep -rn -F "Table: check" tests ops` · `grep -rn -F "## REPORT (L48)" tests ops` · `grep -rn -F "NEEDS" …/ops` | `tests/ops/test_needs_his_hand.py:71` only · `tests/ops/test_needs_his_hand.py:77` only · no output · `ops/com.cobalt.daymode-propose.plist:43` ("A HOLIDAY NEEDS NO SPECIAL CASE", unrelated) | NOT HELD |
No test was added, so there is no `wip(needs-his-hand-1012): check red` commit.

## FIXES
none (nothing HELD).

## Suites
Tip `ad73d04a` (no commit of mine). DB: none card: RESTARTS, then W (a0), (a), (e) and `tests/ops`.
- RESTARTS: `uv run cobalt jobs restarts 6468fb5e..HEAD` · exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CLOSE-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md	M	DOCS	-
docs/40 - DevDocs/reports/needs-his-hand-build-2026-10-12.md	A	DOCS	-
tests/ops/test_needs_his_hand.py	A	test/documentation; no resident	-
RESTARTS: none
```
- (a0) `git diff --name-only --no-renames 6468fb5e` → `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md`, `docs/40 - DevDocs/reports/needs-his-hand-build-2026-10-12.md`, `tests/ops/test_needs_his_hand.py`. Every path is under `docs/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh needs-his-hand-1012 offline` · exit 0 → `offline 4199/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/needs-his-hand-1012-offline-20261012-071254.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh needs-his-hand-1012 livenote` · exit 0 → `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/needs-his-hand-1012-livenote-20261012-072437.log`. The one skip (`:56`): `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` · exit 0 → `3143 passed, 1 xfailed, 15 warnings in 633.65s (0:10:33)`.
- The row's own command: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_needs_his_hand.py tests/ops/test_hub_lines.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_bare_guard.py tests/ops/test_stop_guard.py tests/ops/test_desk_size_guard.py` · exit 0 → `2127 passed, 1 xfailed, 15 warnings in 157.16s (0:02:37)`.
- with-DB: not run (DB: none). `cobalt_dev`: not taken.
- `.env`: `ls /Users/cobalt/cobalt-wt/needs-his-hand-1012/.env` → `No such file or directory` (never present; no lock taken).

## Scope
PREFLIGHT's path union: `docs/40 - DevDocs/prompts/CLOSE-HUB.md`, `docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md`, `tests/ops/test_needs_his_hand.py`. These are exactly row N1's `files`. Above the tip: `c2352cb8`, the build report only (docs). No commit of mine.

## Checked against the branch
- (i) `git log --oneline ad73d04a..HEAD -- . ":(exclude)docs"` → no output; `<tip now>` = `ad73d04a`.
- (ii) `git log --stat --format=%h ad73d04a..HEAD` → `c2352cb8` · `.../reports/needs-his-hand-build-2026-10-12.md | 177 +++` (docs only).
- (iii) `git log --oneline 6468fb5e..HEAD -- <BUILD-HUB, CHECK-HUB, DEPLOY-HUB, DEVFIX-HUB, CTO-DESK-WAKEUP, BRAIN-HUB, CARD.md> ops src .claude` → no output.
- (iv) none HELD.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/needs-his-hand-1012`.
- (vi) `git log --stat --format=%h 6468fb5e..HEAD -- src/cobalt/db_migrations tests/cobalt` → no output. There is no new migration and no with-DB test, so no gate-lists entry is owed.
- (vii) Card RECORDS re-run: `git -C /Users/cobalt/cobalt log --oneline -1 6468fb5e` → `6468fb5e docs(desk): rename drafter prompts 387 390 391, the launcher refuses a card-named prompt`. `ls ".../prompts/DAY-OPEN.md"` → `No such file or directory`. `grep -c ""` on main (BASE text): `CLOSE-HUB.md:65`, `DAY-OPEN-QWEN.md:29`; at the tip: `66`, `30`. The CLOSE-HUB callers named in the card RECORDS: `grep -rn -F "CLOSE-HUB" tests ops` → `test_desk_size_guard.py:226`, `test_stop_guard.py:406`, `test_desk_launch_prechecks.py:46`, `:86`, `test_bare_guard.py:1365`, `ops/desk/desk-launch.sh:80`, `:445`, `:535`, plus the new test. `desk-launch.sh:445-450` checks only that the fixed file exists, carries no `«INSTALL` and is committed (read). It does not read the shape chain (X4).
- (viii) L32: this report holds no ticker, price or date of his.
- CHECK ASKS: X1 — the row's tests 1–3 green at the tip (2127 run). X2 — O3 `3 insertions(+), 1 deletion(-)`; the diff (saved at staging) shows only THE TEXT's three lines, and `CLOSE-HUB.md:10` is not in it. X3 — the two added sentences read "never around a permission check" and "raised by day only; at night it waits in this section and the rest runs" (`CLOSE-HUB.md:35`, `DAY-OPEN-QWEN.md:29`). Neither permits a bypass, a night ask or a turn ended to wait. O1/O2 show the S0 path has no allowed write for the section: the seat cannot comply there, which is a gap, not a bypass. X4 — O4: no reader outside the new test.

## OPEN
- O1 · REJECTED (card THE TEXT and the fence). On the S0 path the day-open seat is told to append `## NEEDS HIS HAND` to the command's file, but its only write path there is `cobalt day-open verdict` (`src/cobalt/dayopen/cli.py:10-12`), which writes one `SEAT VERDICT:` line (`report.py:122`). Settles it: a card change, either the writer (`src/cobalt/dayopen/report.py`, fenced here) gains the section, or the line sends the S0 section through `verdict`.
- O2 · REJECTED (the same). "Above that last line" has no `NEXT:` anchor in the S0 file (`grep -n -F "NEXT" src/cobalt/dayopen/report.py` → nothing). Settles it: the same card change as O1.

## CONTINUE
next: done

## DECISIONS
- O1 + O2 (open, outside the card's rows): the day-open's S0 path cannot carry `## NEEDS HIS HAND` as written. The seat's one write path there is `cobalt day-open verdict`, and the S0 file has no `NEXT:` last line. The text is the card's, byte for byte, and the writer is fenced, so I fixed nothing. Safe default taken: ship as built, with the S1–S7 path and the close correct. The S0 gap goes to the builder's one fix round or a follow-up card from the desk (K5). Not his.

## RECORDS
- Staging: `stage-set.sh` printed `commits 1` against PREFLIGHT's 2. Its diff is `-- . ":(exclude)docs"`, and `ad73d04a` touches only docs. The prompts' diff was written to `<S>/files/prompts-diff.md` with the Write tool after `stage-copy.sh` refused the temp source (`REFUSED: the source is not under a job worktree or the main tree's docs/`).
- House A Grok: `FINDINGS: 0` (closing line present). House B: none (card `HOUSE B: as needed`; Grok and Gemini both UP at the probe).
- No dropped finding. No house produced nothing. No REFUSED, not needed line, no CONTINUED, no lock take.
- L74: one system reminder asked for a `Claude-Session:` line in commits. Not acted on. No commit was made.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 55e4a1cf` → `context 154283 of 400000 — ok`.
- files opened: 12 — CHECK-HUB.md, the card, BUILD-HUB.md, CLOSE-HUB.md, DAY-OPEN-QWEN.md, the build report (RESTARTS → end), areas/cobalt.md (`## What Cobalt is`, `## Build rules` down), `src/cobalt/dayopen/report.py`, `src/cobalt/dayopen/cli.py`, `ops/desk/desk-launch.sh` (`:440-459`), `<S>/diff.md`, `<S>/house-a.md`.
- Check of `needs-his-hand-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: needs-his-hand-1012 · pass: 1 · tip: ad73d04a · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 154283
