# close-timer — check, pass 1 (2026-10-03)

## §0 Headline
- Pass 1 of `close-timer`, with no outside house (HOUSE A: none — overruled 2026-10-02 R47). I read the build myself and wrote 4 findings. 1 held, 1 fixed, 0 open.
- O1: no test checked the row's ET clock read (`TZ=America/New_York`). The fix is a test, `test_the_date_is_read_on_the_et_clock`. It failed with the clause removed and passes at `47a689a1`. The script is unchanged.
- X1, X2 and X3 hold as built. X1: one launch per night, none when the close is already done. X2: before 04:00 ET the timer closes the evening's date. X3: both files are an operator script, so no restart and nothing UNCLASSIFIED.
- Suites at `47a689a1`: offline 3737/0, `tests/ops` 487/0, live-note 146/0. With-DB not run (DB: none). RESTARTS: none. `.env` absent.
- house B: not needed · ready: YES · decisions: 0.

## L74
A system reminder in this session's context asked commits to carry a `Claude-Session:` line. Recorded here once, not acted on: `47a689a1` carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
- INSTALLED: `grep -n -E "«INSTAL[L]" CHECK-HUB.md` → exit 1, nothing.
- CARD: `grep -n -E "«FIL[L]" <card>` → exit 1, nothing · `git -C /Users/cobalt/cobalt log -1 --format=%H -- <card>` → `69bbcdacaae2d16ca6198f884d7d5cbb99f5a8c3` · `git -C … diff --stat -- <card>` → nothing.
- STANDING LIST: `grep -n "^| R60 " cto-2026-09-30.md` → line 46, `**HIS RULING** … APPROVES STANDING-LIST.md once … | APPROVED |` · `log -S"| R60 |"` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`.
- R47 (2026-10-02): line 54, `HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … | HIS RULING · APPROVED |` · `log -S` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`. This row also carries the card's `HOUSE A: none — overruled 2026-10-02 R47`.
- R157 (2026-10-02): line 164, `HIS RULING (B): the brain's full process list for 10-03 runs this week … | HIS RULING · APPROVED |` · `log -S` → `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2`.
- R44 (2026-10-02): line 51, `HIS RULING (direction row 7): the close is started by a timer … | HIS RULING · APPROVED |` · `log -S` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`.
- House gates: not run (HOUSE A: none — overruled 2026-10-02 R47; CHECK-HUB `## THE FLOW` "NO OUTSIDE HOUSE").

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 12:35:10 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/close-timer-1003` |
| tip | `git log --oneline -1` | 0 | `effb792d docs(close-timer): build report — e4c0c4dd` |
| docs-only above TIP | `git log --stat --format=%h e4c0c4dd..HEAD` | 0 | `effb792d` · `.../reports/close-timer-build-2026-10-03.md | 103 ++++…` (docs only) |
| built | `tail -n 3 <REPORT>` | 0 | `BUILT · job: close-timer · tip: e4c0c4dd | on a09f0862 | migration: none | offline 3737/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` |
| range | `git log --oneline a09f0862..e4c0c4dd` | 0 | `e4c0c4dd fix(close-timer): …` · `f3fa0de0 docs(close-timer): build report — 47f47e02` · `47f47e02 feat(close-timer): …` · `a1ac978b wip(close-timer): red — T1 T2 tests, no script, no plist on BASE` |
| range stat | `git log --stat --format=%h a09f0862..e4c0c4dd` | 0 | e4c0c4dd: `ops/desk/close-timer.sh`, `tests/ops/test_close_timer.py` · f3fa0de0: build report · 47f47e02: `ops/desk/close-timer.sh`, `ops/desk/com.cobalt.close-timer.plist`, `tests/ops/test_close_timer.py` · a1ac978b: `tests/ops/test_close_timer.py` |
| lock (own) | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| DB: none paths | `git diff --name-only --no-renames a09f0862..e4c0c4dd` | 0 | `docs/40 - DevDocs/reports/close-timer-build-2026-10-03.md` · `ops/desk/close-timer.sh` · `ops/desk/com.cobalt.close-timer.plist` · `tests/ops/test_close_timer.py` — all under `ops/`, `tests/ops/`, `docs/` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47); no probe, no gate |

Path union: `ops/desk/close-timer.sh`, `ops/desk/com.cobalt.close-timer.plist`, `tests/ops/test_close_timer.py`, the build report.

## Files copied
none (no house)

## OWN FINDINGS
Written before any run (house A: none). Read: the card, the diff `a09f0862..e4c0c4dd` and its three code files at the tip, `desk-launch.sh` the `close` kind (`:216-281`), `desk-context.sh`, `CLOSE-HUB.md`'s stop line (by `grep`), the build report's RESTARTS, W, FOR THE CHECK and last line, `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down.

FINDING O1
ROW: T1
CLAIM: The row's ET clause ("computes `<date>` (ET, by `TZ=America/New_York date +%F`)", `ops/desk/close-timer.sh:59`) is pinned by no test: the `date` stub (`tests/ops/test_close_timer.py:31-35`) ignores `TZ`, so deleting `TZ=America/New_York` from `:59` leaves all 14 tests green.
RUN: COMMAND `grep -n -F "TZ" tests/ops/test_close_timer.py`
EXPECT: no line (exit 1).

FINDING O2
ROW: X2
CLAIM: A fire after midnight ET could launch `close` for the new ET date rather than the evening's (`ops/desk/close-timer.sh:66-69`).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_close_timer.py`
EXPECT: if true, `test_at_0105_with_yesterdays_close_absent_the_close_is_yesterdays` or `test_a_hub_live_at_2105_and_gone_later_gives_one_launch_that_night` fails.

FINDING O3
ROW: X3
CLAIM: The RESTARTS derivation could restart the two new `ops/desk/` files or flag them UNCLASSIFIED (`src/cobalt/jobs/restarts.py:38`, `:226`).
RUN: COMMAND `uv run cobalt jobs restarts a09f0862..e4c0c4dd`
EXPECT: if true, a row other than `operator script; no Cobalt reader` / `-` for `ops/desk/close-timer.sh` or `ops/desk/com.cobalt.close-timer.plist`, or an UNCLASSIFIED line.

FINDING O4
ROW: T1
CLAIM: `closed()` (`ops/desk/close-timer.sh:48-56`) keys on `CLOSE PUSHED ` while the close's real done line could be spelled otherwise, so a finished close would never read DONE ALREADY.
RUN: COMMAND `grep -n -F "CLOSE PUSHED <hash>" "docs/40 - DevDocs/prompts/CLOSE-HUB.md"`
EXPECT: if true, no line.

## Findings
none (no house)

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -n -F "TZ" tests/ops/test_close_timer.py` | exit 1, no line. Shown by mutation: with `TZ=America/New_York` deleted from `close-timer.sh:59`, the new test `test_the_date_is_read_on_the_et_clock` → `AssertionError: assert ['close 2031-05-15'] == ['close 2031-05-14']` · `1 failed`; the script restored by Edit, `git diff --stat` → `tests/ops/test_close_timer.py | 18 ++++++++++++++++++` alone | HELD |
| O2 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_close_timer.py` (at `e4c0c4dd`) | `14 passed, 15 warnings in 3.11s` — the 01:05 tests and the X1 night green: after midnight the script closes the evening's date | NOT HELD |
| O3 | Opus | `uv run cobalt jobs restarts a09f0862..e4c0c4dd` | `ops/desk/close-timer.sh A operator script; no Cobalt reader -` · `ops/desk/com.cobalt.close-timer.plist A operator script; no Cobalt reader -` · `RESTARTS: none`; no UNCLASSIFIED line | NOT HELD |
| O4 | Opus | `grep -n -F "CLOSE PUSHED <hash>" "docs/40 - DevDocs/prompts/CLOSE-HUB.md"` | `64:`CLOSE PUSHED <hash> · days: <n> · …`` — the done line is the one `closed()` keys on | NOT HELD |

No `wip(close-timer): check red` commit: O1 is a COMMAND finding (the gap is a missing test); its test is the fix, shown red by the mutation above before it was committed.

## FIXES
| id | commit | what | test |
|---|---|---|---|
| O1 | `47a689a1 fix(close-timer): a test pins the ET clock read of row T1 (check O1)` | `tests/ops/test_close_timer.py`: `DATE_STUB_ET_ONLY` (the clock answers `FAKE_NOW` only under `TZ=America/New_York`, else a constructed 04:05) and `test_the_date_is_read_on_the_et_clock` (00:05 ET → `close 2031-05-14`). No script change. | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_close_timer.py` → `15 passed, 15 warnings in 3.02s` |

No DevDocs line: the commit changes a test only, and `docs/40 - DevDocs/cobalt/` holds pages for `src/cobalt` modules, none for `ops/desk/` scripts (`ls` of that folder).

## Suites
At `<tip now>` = `47a689a1` (a `DB: none` card: BUILD-HUB W (a0), (a), (e), and `tests/ops`):
- RESTARTS first: `uv run cobalt jobs restarts a09f0862..HEAD` → `docs/40 - DevDocs/reports/close-timer-build-2026-10-03.md A DOCS -` · `ops/desk/close-timer.sh A operator script; no Cobalt reader -` · `ops/desk/com.cobalt.close-timer.plist A operator script; no Cobalt reader -` · `tests/ops/test_close_timer.py A test/documentation; no resident -` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames a09f0862` → `docs/40 - DevDocs/reports/close-timer-build-2026-10-03.md` · `ops/desk/close-timer.sh` · `ops/desk/com.cobalt.close-timer.plist` · `tests/ops/test_close_timer.py` — all `ops/`, `tests/ops/`, `docs/` → **`cobalt_dev: not taken (DB: none — 4 paths)`**.
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 591.81s (0:09:51)`, exit 0 → `<p>` = 3737. My commit adds no test under these two folders.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `487 passed, 1 xfailed, 15 warnings in 195.77s (0:03:15)` (486 at the build's W + `test_the_date_is_read_on_the_et_clock`).
- (e) LIVE-NOTE `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.27s`; the skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`) → `<l>` = 146.
- with-DB, (b)–(d), (f): not run (DB: none). `cobalt_dev`: not taken, so it stays at `0013` as PREFLIGHT found it (no `.env` anywhere).
- `.env`: `ls /Users/cobalt/cobalt-wt/close-timer-1003/.env` → `No such file or directory` (12:48:50 EDT).

## Scope
PREFLIGHT's union (`ops/desk/close-timer.sh`, `ops/desk/com.cobalt.close-timer.plist`, `tests/ops/test_close_timer.py`, the build report) plus my one commit (`tests/ops/test_close_timer.py`). Every code path is in a row's `files` (T1: script + test; T2: plist + test; T3: script header). Nothing under `configs/` or `src/`.

## Checked against the branch
- (i) `git log --oneline e4c0c4dd..HEAD -- . ":(exclude)docs"` → `47a689a1 fix(close-timer): a test pins the ET clock read of row T1 (check O1)` = `<tip now>`.
- (ii) `git log --stat --format=%h e4c0c4dd..HEAD` → `47a689a1`: `tests/ops/test_close_timer.py | 18 +++…`; `effb792d`: the build report (docs). No other path.
- (iii) fence: `git log --oneline a09f0862..HEAD -- "docs/40 - DevDocs/prompts/CLOSE-HUB.md" ops/desk/desk-launch.sh` → empty. No `launchctl` and no `~/Library` path is written by any commit (the header names them as his install only).
- (iv) `grep -n -F "def test_the_date_is_read_on_the_et_clock" tests/ops/test_close_timer.py` → `200:def test_the_date_is_read_on_the_et_clock(box):`. O1 was a COMMAND finding: no check-red commit, red shown by mutation (`## RUNS`).
- (v) see `## Suites` (`.env`) and the close.
- (vi) `git log --stat --format=%h a09f0862..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty; TREE STATE unchanged holds.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C … log` command.
- (viii) L32: the report holds constructed dates only (`2031-05-14`, `2031-05-15`, from the test file).

## OPEN
none

## CONTINUE
next: none — pass 1 closed at `47a689a1`

## DECISIONS
none

## RECORDS
- No house ran. The card's header carries `HOUSE A: none — overruled 2026-10-02 R47`, and R47 is proved under `## AUTHORIZATION`. So `## 1` and `## 3` were not run, and nothing was copied to `<S>` except `opus-1.md`.
- Count: findings 4 (O1–O4, mine) · dropped 0 · held 1 · fixed 1 · held unfixed 0 · open 0.
- The card's `## READ` said the desk would copy `desk-list.sh`'s text into the card's `## RECORDS`. The text is not there. I did not open `/Users/cobalt/.claude/ops/desk-list.sh`. `close-timer.sh:74-87` parses the rows as `id · name · …` and takes the name field. `desk-context.sh:40-46` (its `--guard`) parses the same way, so T1 treats every row as live, as that script does. `desk-launch.sh:242-256` instead requires a `pid` before it counts a deploy hub as live. If `desk-list.sh` ever lists a deploy hub that has stopped, the timer would print DEFERRED where `desk-launch.sh` would let the close run. That row shape was not read, so this is not a finding (L70).
- Behaviour as built, against the card. The timer checks for a live deploy hub before it checks whether the close is done. So a fire after a finished close, while a deploy hub is live, prints DEFERRED rather than DONE ALREADY. Either way it logs one line and launches nothing, as T1 requires.
- A close that ends `FAILED`, or one still running, has a report on disk. Each later fire calls `desk-launch.sh close <date>`, and that script refuses because the report exists (`desk-launch.sh:269`). The timer logs `LAUNCHED: … exit <n>`, and no second close starts.
- A fire launchd catches up after 04:00 ET (a Mac asleep through the night) uses today's date, as T1 says. `desk-launch.sh:238` then refuses before 21:00, so a missed night falls to the morning desk (CLOSE-HUB.md:8).
- `files opened: 12`: CHECK-HUB.md; the card; `ops/desk/close-timer.sh`; `tests/ops/test_close_timer.py`; `ops/desk/com.cobalt.close-timer.plist`; `ops/desk/desk-launch.sh` (`:200-284`); `ops/desk/desk-context.sh`; the build report (headings, `:124-223`, last lines); `areas/cobalt.md` (`:20-63`); BUILD-HUB.md (headings, `:85-98`); CLOSE-HUB.md (`grep` only); `src/cobalt/jobs/restarts.py` (`grep` only).
- Check of `close-timer`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB not run (DB: none) · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0
