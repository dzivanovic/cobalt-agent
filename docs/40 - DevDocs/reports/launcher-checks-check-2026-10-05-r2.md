# launcher-checks — check, pass 1 (r2, fix round F2–F4) · 2026-10-05

## §0 Headline
- Pass 1 of `launcher-checks` (fix round F1–F4), no outside house (R47). 5 own findings; 1 held, fixed; 0 open.
- Held O1: `deploy-step0.sh` P2 passed a fix-round row whose fix report was edited after its commit or never committed. The F3 hub line requires both. Red `59bd4bf8`, fix `a545a4d8`. This settles the build's DECISION 3.
- Gate on `a545a4d8`: offline 3786/0 · with-DB 857/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS: none.
- One decision, not blocking: `DEPLOY-HUB.md:58` still says the literals are in "the last column", and the fence keeps that line unchanged.

## L74
- 17:59 ET: a system reminder in this session asked commits to end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded as data; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md"` → exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 0 · 85b032f203db3ef7e1f05435d8dd708138c82f7c
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-02/21-launcher-checks-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
HOUSE A overruled 2026-10-02 R47 row · grep -n "^| R47 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, built and deployed in a day; card `20` (`deploy-outage.sh`) keeps a Grok check ([words](cto-2026-10-02-words.md#r38-r48)). | HIS RULING · APPROVED |
HOUSE A overruled 2026-10-02 R47 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · 4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a
HOUSE A overruled 2026-10-02 R47 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-02.md" · 0 · the row as grepped
AUTHORIZED
```
House gates and probes: not run — the card carries `HOUSE A: none — overruled 2026-10-02 R47` (CHECK-HUB SEAT ORDER, "NO OUTSIDE HOUSE").

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` → exit 0, output whole:
```
clock · date · 0 · Mon Oct  5 17:59:05 EDT 2026
status · git status --short --branch · 0 · ## ops/launcher-fixround-1005
head · git log --oneline -1; git log --stat --format=%h dc2a80b4..HEAD · 0 · (5 lines)
    a42be127 docs(launcher-checks): build report — dc2a80b4 (fix round F2-F4)
    a42be127
    
     .../reports/launcher-fixround-build-2026-10-05.md  | 105 +++++++++++++++++++--
     1 file changed, 95 insertions(+), 10 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/launcher-fixround-1005/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/launcher-fixround-1005/docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md" · 0 · BUILT · job: launcher-checks · tip: dc2a80b4 | on 5fb0ddf5 | migration: none | offline 3786/0 | with-DB 857/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 235315
range · git log --oneline 5fb0ddf5..dc2a80b4 · 0 · (10 lines)
    dc2a80b4 docs(launcher-checks): CARD.md SHIPS text states the fix-round row rule and the literals column (F4, check O4, R376, L75)
    1cd4601c docs(launcher-checks): DEPLOY-HUB P2 states the fix-round row rule, one new line after P2 (F3, R376, L75)
    4b8289cb wip(launcher-checks): E3 F3 — main not merged into the branch; git merge is not a builder command (F2 built at 7c33d97b)
    7c33d97b fix(launcher-checks): STEP-0 P2 accepts a fix-round row: the check tip an ancestor of the code tip and the fix report BUILT on it; check O1 test passes (F2, R376, L75)
    4e8296fc wip(launcher-checks): red — F2 fix-round row passes STEP-0 P2 (O1 xfail mark removed; negative controls a-c)
    7e7803d5 fix(launcher-checks): F1 negative controls pin the fix report's unmodified and reports-folder clauses (check O2, O3)
    553f8c7b wip(launcher-checks): check red — O1 (deploy-step0.sh P2 refuses the fix-round tip the launcher accepts; strict xfail, held, not fixed: outside card 21's rows)
    36b98d61 docs(launcher-checks): build report — c1746720
    c1746720 fix(launcher-checks): a deploy accepts a check tip below the code tip when the SHIPS row's fix report is committed and BUILT on the code tip; deploy-card.sh and CARD.md carry the fix report column (F1, R376, L75)
    7681e81f wip(launcher-checks): red — F1 fix-round tip launches; fix report column in deploy-card.sh and CARD.md
PREFLIGHT OK
```
- THE RANGE, `git log --stat --format=%h 5fb0ddf5..dc2a80b4` → path union: `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md`, `ops/desk/deploy-step0.sh`, `ops/desk/deploy-card.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`. Every path is under `ops/`, `tests/ops/` or `docs/`.
- `ls <S>` → `opus-1.md` (present). No `CONTINUE:` in the launch message: this is not a recovery; the file is left by the earlier check of this job (recorded under `## RECORDS`, not opened).
- house A: none (overruled 2026-10-02 R47) · house B, if needed: none available (no probe is run under the overrule).

## Files copied
none — no house (overrule).

## OWN FINDINGS
Written before any run. House A: none (overrule), so no house list exists to keep apart.

FINDING O1
ROW: F2 (against F3's hub line)
CLAIM: `ops/desk/deploy-step0.sh:387-398` accepts a fix-round row on the fix report's last line and the ancestor test alone; it never tests that the fix report is committed and unmodified, which the F3 hub line (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md:59`) and the launcher (`ops/desk/desk-launch.sh:757-759`) require. A fix report edited after its commit, or never committed, passes STEP-0 P2.
RUN: TEST — `tests/ops/test_deploy_step0.py`, `test_o1r2_a_fix_report_not_committed_and_unmodified_fails_p2[edited after its commit | never committed]` (uses `fix_round`, `last_line`, `git` of that file).
EXPECT: on the tip, `assert done.returncode == 1` fails: the run prints `STEP-0 OK — window: (iii)` and exits 0.

FINDING O2
ROW: X4 / fence
CLAIM: no assertion of `tests/ops/test_devdb_lock.py`, `tests/ops/test_desk_launch_devfix.py`, `tests/ops/test_desk_size_guard.py` changed in the range.
RUN: COMMAND — `git diff --stat 5fb0ddf5..dc2a80b4 -- tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py`
EXPECT: no output.

FINDING O3
ROW: F3
CLAIM: the F3 line sits directly after the P2 line and is the only change to `DEPLOY-HUB.md` (diff `1 +`).
RUN: COMMAND — `grep -n -F "Fix-round row" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; `git diff --stat 5fb0ddf5..dc2a80b4 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: one line at `:59`, directly after the `**P2 EVERY CHECK, COMMITTED**` line at `:58`; `1 insertion(+)`. (A check of the row, not a defect claim.)

FINDING O4
ROW: F4
CLAIM: `CARD.md` carries the F4 sentence once and no longer the old "The last column is" sentence.
RUN: COMMAND — `grep -c -F "the check's \`tip:\` is an ancestor of the code tip" "docs/40 - DevDocs/prompts/CARD.md"`; `grep -n -F "The last column is" "docs/40 - DevDocs/prompts/CARD.md"`
EXPECT: `1`; no line. (A check of the row, not a defect claim.)

FINDING O5
ROW: F2
CLAIM: the F2 tests stay red when the fix is undone (the builder's M10); `tests/ops/test_deploy_step0.py` has `0 xfailed` at the tip.
RUN: COMMAND — `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py`
EXPECT: `42 passed`, no `xfailed`. (A check of the row, not a defect claim.)

## Findings
none — no house.

## Dropped
none.

## RUNS
| id · source | run | output | verdict |
|---|---|---|---|
| O1 · Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py -k o1r2` (the test added with the Edit tool; one form repair before the first run: the never-committed case reads the card file, not `card_text()`, which has no fix column, plus a guard `assert` that the cell was replaced) | `2 failed, 42 deselected, 15 warnings in 2.78s`; first failing line, both cases: `assert 0 == 1` — the run printed `STEP-0 OK — window: (iii)` | HELD |
| O2 · Opus | `git diff --stat 5fb0ddf5..dc2a80b4 -- tests/ops/test_devdb_lock.py tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_size_guard.py` | no output | NOT HELD (X4: no assertion changed) |
| O3 · Opus | `grep -n -F "Fix-round row" ".../DEPLOY-HUB.md"`; `grep -n -F "P2 EVERY CHECK, COMMITTED" ".../DEPLOY-HUB.md"`; `git diff --stat 5fb0ddf5..dc2a80b4 -- ".../DEPLOY-HUB.md"` | `59:  - Fix-round row (its \`fix report\` cell non-empty): …`; `58:- **P2 EVERY CHECK, COMMITTED** (L67). …`; `1 file changed, 1 insertion(+)` | NOT HELD (F3 as the row says) |
| O4 · Opus | Grep tool, count of ``the check's `tip:` is an ancestor of the code tip`` in `CARD.md` (the `grep -c` was blocked by the bare-guard for its backtick: NOT A REFUSAL, resent as the Grep tool); `grep -n -F "The last column is" ".../CARD.md"` | `1`; no output | NOT HELD (F4 as the row says) |
| O5 · Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_deploy_step0.py` (after the O1 fix) | `44 passed, 15 warnings in 26.16s` — 42 of the tip + the two O1 cases; no `xfailed` | NOT HELD |

Red commit: `59bd4bf8 wip(launcher-checks): check red — O1r2 (…)`.

## FIXES
| id | change | proof | commit |
|---|---|---|---|
| O1 | `ops/desk/deploy-step0.sh` P2 check 1, inside the fix-round block F2 added (:391-397 now): on a `BUILT · … tip: <code tip>` fix report, `git -C "$REPO" log -1 --format=%H -- <fix report>` must be non-empty and `git -C "$REPO" diff --stat -- <fix report>` empty (the hub's own P2 pair, the same as the check report's at :409-414), else `why` keeps today's refusal plus `the fix report … is not committed and unmodified`. No other line. | `tests/ops/test_deploy_step0.py` → `44 passed`; with `test_desk_launch_prechecks.py`, `test_deploy_card.py`, `test_deploy_outage.py` → `179 passed, 15 warnings in 92.72s` | `a545a4d8 fix(launcher-checks): STEP-0 P2 accepts a fix-round row only when its fix report is committed and unmodified, as the hub's P2 fix-round line says (check O1r2)` |

DevDocs line: no page for `deploy-step0.sh` under `docs/40 - DevDocs/cobalt/` (Grep `deploy-step0` → no files); none invented, as the build.
This settles the build's DECISION 3 (the hub line and the script differed on that clause): the script now tests what the hub line says.

## Suites
RESTARTS first, `uv run cobalt jobs restarts 5fb0ddf5..HEAD` at `a545a4d8` → whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CARD.md	M	DOCS	-
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md	A	DOCS	-
ops/desk/deploy-card.sh	M	operator script; no Cobalt reader	-
ops/desk/deploy-step0.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_deploy_step0.py	M	test/documentation; no resident	-
tests/ops/test_desk_launch_prechecks.py	M	test/documentation; no resident	-
RESTARTS: none
```
W: `sh /Users/cobalt/cobalt/ops/desk/gate.sh launcher-fixround-1005 all` (no `--deselect`, `--tickers` or `--migration`: the job adds no with-DB test, writes no ticker, adds no migration) on `a545a4d8` → exit 0. Verdict lines, whole:
```
offline 3786/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 857/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/launcher-fixround-1005-all-20261005-180406.log
```
- `cobalt_dev: 0013 — F2 = F0`; `.env: removed`; `ls /Users/cobalt/cobalt-wt/launcher-fixround-1005/.env` → `No such file or directory` (18:20 ET).
- Touched tests (the card's rule; the gate does not run `tests/ops`): `tests/ops/test_deploy_step0.py` `44 passed`, `0 xfailed`; with `test_desk_launch_prechecks.py`, `test_deploy_card.py`, `test_deploy_outage.py` `179 passed, 15 warnings in 92.72s`.
- RESTARTS: none.

## Scope
PREFLIGHT's path union (8 paths, `## PREFLIGHT`) plus my two commits: `tests/ops/test_deploy_step0.py` (row F2's test file) and `ops/desk/deploy-step0.sh` (row F2's file, inside P2 check 1, the fix-round block F2 added). No other path.

## Checked against the branch
- (i) `git log --oneline dc2a80b4..HEAD -- . ":(exclude)docs"` → `a545a4d8 fix(launcher-checks): STEP-0 P2 accepts a fix-round row only when its fix report is committed and unmodified, as the hub's P2 fix-round line says (check O1r2)` · `59bd4bf8 wip(launcher-checks): check red — O1r2 (…)`. `<tip now>` = `a545a4d8`.
- (ii) `git log --stat --format=%h dc2a80b4..HEAD` → `a545a4d8 ops/desk/deploy-step0.sh | 8 +++++++-` · `59bd4bf8 tests/ops/test_deploy_step0.py | 22 ++++` · `a42be127` the build report (docs). Both non-docs paths are in row F2's `files`.
- (iii) `git log --oneline 5fb0ddf5..HEAD -- BUILD-HUB.md CHECK-HUB.md DEVFIX-HUB.md ops/desk/desk-watch.sh .claude/settings.json ops/desk/gate-lists.md` → empty. The three older launcher test files: O2, empty. `DEPLOY-HUB.md` and `CARD.md`: only the F3 line and lines 44-45, 47 (diff above).
- (iv) `grep -n -F "def test_o1r2_a_fix_report_not_committed_and_unmodified_fails_p2" tests/ops/test_deploy_step0.py` → `629:…`; its red commit `59bd4bf8` sits below its fix `a545a4d8` in (i).
- (v) `.env` → No such file; `git status --short --branch` → `## ops/launcher-fixround-1005`.
- (vi) `git log --stat --format=%h 5fb0ddf5..HEAD -- src/cobalt/db_migrations tests/cobalt` → empty: no gate lists owed.
- (vii) the card's `## RECORDS` name no `ls`, `grep` or `git -C … log` command to run.
- (viii) L32: no value of his in this report (tips, paths and constructed test values only).
- Path to a score, rank, grade or size: none (operator scripts and docs under `ops/`, `tests/ops/`, `docs/` only).
- X1: the launcher's fix-round test (F1) is a superset of STEP-0's (both now: committed and unmodified, BUILT on the code tip, ancestor); a launch it accepts is not refused at STEP-0 P2 on those clauses. X2: a six-column row and a seven-column row with an empty cell take today's path (`test_a_check_report_whose_tip_is_not_the_row_s_code_tip_fails`, F2 control (a), F1's `…todays_shape…` — green). X3: F1's refusal tests assert `not desk.gate_left()` (round 1's check). X4: O2. X5: F1, checked in round 1; `test_f1_deploy_card_…` and `test_f1_card_md_…` green in the 179.

COUNTING: findings 5 (Opus 5, house 0) · dropped 0 · held 1 · fixed 1 · held unfixed 0 · open 0.

## OPEN
none.

## CONTINUE
next: done (stop line below).

## DECISIONS
1. `DEPLOY-HUB.md:58` (P2, fenced: byte for byte in this job) still says the literals are those "the row's last column names". On a seven-column `## SHIPS` row the last column is now `fix report`; `CARD.md:47` (F4) and the script (column 7) read the literals from `its stop line must carry`, the column before it. The hub sentence reads wrong for a hand-run P2 on a new-shape card. Not a defect of the rows (the fence keeps line 58), not runnable as a test. Safe default taken: not touched. Owed: a one-phrase hub fix on a card ("the `its stop line must carry` column").

## RECORDS
- No house: `HOUSE A: none — overruled 2026-10-02 R47`; `## 1` and `## 3` not run; no house gate, no probe.
- `ls <S>` at PREFLIGHT showed `opus-1.md`, left by the earlier check of this job; not opened. This pass's sections were written to `<S>/opus-1-r2.md` instead of `<S>/opus-1.md`, so that file is not overwritten unread; no house B reads either (open 0).
- The bare-guard blocked one `grep -c` for its backtick (NOT A REFUSAL); the same count was run with the Grep tool. No `REFUSED, not needed` line. No `CONTINUED`.
- Lock takes: one, the gate's (`lock: waited 0 min`), rolled back to 0013 (`F2 = F0`) and released (`.env: removed`).
- L74: the `Claude-Session:` reminder, recorded under `## L74`; not acted on.
- files opened: 11 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); the build report (`## E2 RED` to the end); `ops/desk/deploy-step0.sh` (:129-134, :300-417); `tests/ops/test_deploy_step0.py` (:1-200, and its diff); `ops/desk/desk-launch.sh` (diff and one Grep); `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (diff and Greps); `docs/40 - DevDocs/prompts/CARD.md` (diff and Grep); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the gate's output file.
- Check of `launcher-checks`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 857/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813
