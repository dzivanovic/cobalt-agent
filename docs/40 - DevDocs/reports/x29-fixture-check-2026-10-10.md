# x29-fixture-1010 — check (2026-10-10)

## §0 Headline
- Row A holds at the tip: the five experiment conftests all re-export `offline_skip_guard`. X1: none lacks it. X3: A1 goes red for each of the four lines removed. X2: nothing errors at setup, with or without Postgres, and nothing fails G1.
- One finding held (S1, Sol): A1 accepted `offline_skip_guard = <any value>`. Fixed in the row's test file (`3c00e204`), shown red first (`4a690fbe`).
- Gate on `3c00e204`: offline 4199/0 · with-DB 5096/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed` · RESTARTS: none.
- One decision, not for Dejan: two f15_p1 with-DB experiment tests are red on a `src` signature (`proposed_key_reason`). This red is inside the fence and is not fixed here.

## L74
- 2026-10-10, at the start of this session: a system reminder asked for a `Claude-Session:` line on commits. Recorded once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md" · 0 · 89e80b09ae4505e4592f65ab91439039a0e9de1f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/242-x29-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " …cto-2026-09-24.md` → one row (line 35, STANDING `Bash(grok *)`); `grep -n "^| R19 " …cto-2026-09-24.md` → one row (line 37, the four house strings STANDING); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Sat Oct 10 10:50:59 EDT 2026
status · git status --short --branch · 0 · ## ops/x29-fixture-1010
head · git log --oneline -1; git log --stat --format=%h d083ec76..HEAD · 0 · (5 lines)
    e1d5a6b0 docs(x29-fixture-1010): build report — d083ec76
    e1d5a6b0
    
     .../reports/x29-fixture-build-2026-10-10.md        | 172 +++++++++++++++++++++
     1 file changed, 172 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/x29-fixture-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/x29-fixture-1010/docs/40 - DevDocs/reports/x29-fixture-build-2026-10-10.md" · 0 · BUILT · job: x29-fixture-1010 · tip: d083ec76 | on 82da1f1b | migration: none | offline 4198/0 | with-DB 5095/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 117750
range · git log --oneline 82da1f1b..d083ec76 · 0 · (2 lines)
    d083ec76 fix(x29-fixture-1010): experiment conftests re-export offline_skip_guard (A, L1 L45)
    67fb195a wip(x29-fixture-1010): red — experiment conftests lack offline_skip_guard (A)
PREFLIGHT OK
```
THE RANGE, typed: `git log --stat --format=%h 82da1f1b..d083ec76` · exit 0:
```
d083ec76
 tests/experiments/f15_p1/conftest.py      | 1 +
 tests/experiments/handicap_h1/conftest.py | 1 +
 tests/experiments/setups_one/conftest.py  | 1 +
 tests/experiments/stale_score/conftest.py | 1 +
 4 files changed, 4 insertions(+)
67fb195a
 tests/cobalt/test_experiment_conftests.py | 38 +++++++++++++++++++++++++++++++
 1 file changed, 38 insertions(+)
```
Path union: the four experiment conftests + `tests/cobalt/test_experiment_conftests.py` (all in row A's `files`). Commits: 2.
Card is not "DB: none" (no such header line): the gate runs `all --deploy`.
`ls <S>` · exit 1 · `No such file or directory` → fresh.
House probe `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: UP
```
house A: Sol (`gpt-5.6-sol`) · house B: Grok (`grok-4.7`). HOUSE B: as needed — the MANDATORY rule does not apply; both up anyway.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole:
```
4607 <S>/diff.md
6033 <S>/files/242-x29-card.md
1347 <S>/files/wt/tests/cobalt/test_experiment_conftests.py
1060 <S>/files/wt/tests/experiments/f15_p1/conftest.py
1540 <S>/files/wt/tests/experiments/handicap_h1/conftest.py
1298 <S>/files/wt/tests/experiments/setups_one/conftest.py
1354 <S>/files/wt/tests/experiments/stale_score/conftest.py
19512 <S>/files/x29-fixture-build-2026-10-10.md
384 <S>/rulings.md
STAGED 9 files · 37135 bytes · commits 2
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/x29-fixture-1010-check`; commits 2 = PREFLIGHT's count.)
`stage-copy.sh`, each its own call:
- `COPIED 26515 <S>/files/radar-ladder-refresh-check-2026-10-06.md`
- `COPIED 27689 <S>/files/deploy-deploy-radar-ladder-refresh-1006.md`
- `COPIED 9809 <S>/files/s5-weekend-and-parked-answer-2026-10-10.md`
- `COPIED 77759 <S>/files/BACKLOG.md`
- `COPIED 18003 <S>/files/wt/tests/cobalt/conftest.py`
- `COPIED 1065 <S>/files/wt/tests/experiments/f15_p2/conftest.py`
- `COPIED 3017 <S>/files/wt/tests/experiments/stale_score/test_x29_ladder_render.py`
`<S>/HOUSE-INSTRUCTIONS.md` written (8487 bytes): HOUSE TEXT verbatim, then the card's ROWS, NOT IN THIS JOB, CHECK ASKS, RECORDS, then Files.
Houses started 10:52:28 EDT (date): house A Sol (task b55pji8cr), house B Grok (task b6pl9rfyu); return `cd` then `git status --short --branch` → `## ops/x29-fixture-1010`.

## OWN FINDINGS
Written before any house list was opened. Read: the card, the diff `82da1f1b..d083ec76`, the five touched files and `f15_p2/conftest.py` whole, `tests/cobalt/conftest.py:100–310` and `:388`, `test_x29_ladder_render.py`, the build report whole, `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down.

FINDING O1
ROW: X1
CLAIM: After the fix every experiment conftest that re-exports `dev_db_tx` also re-exports `offline_skip_guard` (tree: five folders, `tests/experiments/f15_p1/conftest.py:24,27`, `handicap_h1/conftest.py:32,35`, `setups_one/conftest.py:28,31`, `stale_score/conftest.py:29,32`, `f15_p2/conftest.py:24,27`), and no nested conftest sits below them that A1's one-level glob (`tests/cobalt/test_experiment_conftests.py:20`) would miss.
RUN: COMMAND `grep -rn -F "dev_db_tx = " tests/experiments` and `grep -rn -F "offline_skip_guard = " tests/experiments` (two calls, compare the folder sets)
EXPECT: if a defect stands, a folder in the first list and not the second, or a hit deeper than `tests/experiments/<folder>/conftest.py`.

FINDING O2
ROW: X3
CLAIM: A1 (`tests/cobalt/test_experiment_conftests.py:25`) goes red when ANY one of the four added lines is removed, not only `stale_score`'s (the build's mutation covered `stale_score` alone).
RUN: COMMAND, for each of `f15_p1`, `handicap_h1`, `setups_one`, `stale_score` in turn: remove its `offline_skip_guard = _conftest.offline_skip_guard` line with Edit, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_experiment_conftests.py`, restore with Edit.
EXPECT: if the claim fails, `2 passed` with a line removed; if it holds, `1 failed, 1 passed` naming that one folder each time.

FINDING O3
ROW: X2 (offline half), A
CLAIM: Without the Postgres settings no test of the four folders errors at setup any more (the build report's `38 passed, 26 skipped` claim, `x29-fixture-build-2026-10-10.md:151`, is the builder's; L35).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/stale_score tests/experiments/f15_p1 tests/experiments/setups_one tests/experiments/handicap_h1`
EXPECT: if a defect stands, an `ERROR at setup` line or `fixture 'offline_skip_guard' not found`.

FINDING O4
ROW: X2 (with-Postgres half)
CLAIM: With the Postgres settings present (one lock take), the four folders' tests may still fail: either at setup, or by G1 (`with-DB test without an offline skip mark`) in a `_db` module (`tests/experiments/stale_score/test_x2_stale_sequence_db.py:16` per the card's fence) — the half the build left to the check (`x29-fixture-build-2026-10-10.md:151`).
RUN: COMMAND `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/stale_score tests/experiments/f15_p1 tests/experiments/setups_one tests/experiments/handicap_h1` inside one lock take, `<FP>` before and after.
EXPECT: if a defect stands, an ERROR at setup or a `FAILED` line naming G1; `<FP>` after = before.

FINDING O5
ROW: A (the green RUN)
CLAIM: The X29 control prints its line and passes at the tip (`tests/experiments/stale_score/test_x29_ladder_render.py:59–63`; the build's claim `x29-fixture-build-2026-10-10.md:83–91`).
RUN: COMMAND `uv run pytest "tests/experiments/stale_score/test_x29_ladder_render.py" -q -rP`
EXPECT: if a defect stands, an ERROR at setup or a failed assertion instead of `1 passed` and the `X29:` line.

## Findings
Lists opened at 10:59:41 EDT (`date`), after both houses ended. Sol ended 10:56:47 EDT (exit 0; its FINAL message written by me to `<S>/house-a.md`, ending `FINDINGS: 1`). Grok ended 10:59:41 EDT (exit 0; it wrote `<S>/house-b.md` itself, 12 bytes, whole content `FINDINGS: 0`; stdout: "The four conftests re-export the guard, and the new test matches the row. No defect to hand over.").
Form check: `grep -n -F "RUN:" <S>/house-a.md` → `4:RUN: TEST — \`tests/cobalt/test_experiment_conftests.py\`` followed by a `def test_` → kept.

| id | house | row | claim | run |
|---|---|---|---|---|
| S1 | A (Sol) | A | A1 accepts any `offline_skip_guard = ` line, so `offline_skip_guard = None` in `stale_score/conftest.py` leaves A1 green though the fixture is gone. | TEST |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -rn -F "dev_db_tx = " tests/experiments`; `grep -rn -F "offline_skip_guard = " tests/experiments` | first: `f15_p2/conftest.py:27`, `setups_one/conftest.py:31`, `handicap_h1/conftest.py:35`, `f15_p1/conftest.py:27`, `stale_score/conftest.py:32`; second: `f15_p2/conftest.py:24`, `setups_one/conftest.py:28`, `handicap_h1/conftest.py:32`, `f15_p1/conftest.py:24`, `stale_score/conftest.py:29` (each `… = _conftest.<name>`). Same five folders, all one level deep. | NOT HELD (X1: none lacks it) |
| O2 | own | Edit removes the guard line in one conftest, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_experiment_conftests.py::test_a1_…` (f15_p1 also with A2), Edit restores; four times | f15_p1: `1 failed, 1 passed in 0.05s`, `E       AssertionError: experiment conftests re-export dev_db_tx without offline_skip_guard: ['f15_p1']` · handicap_h1: `1 failed in 0.04s`, `… ['handicap_h1']` · setups_one: `1 failed in 0.05s`, `… ['setups_one']` · stale_score: `1 failed in 0.04s`, `… ['stale_score']`. After restore `git diff --stat` → only `tests/cobalt/test_experiment_conftests.py \| 21 +` (the S1 test). | NOT HELD (X3: yes, A1 fails for each of the four) |
| O5 | own | `uv run pytest "tests/experiments/stale_score/test_x29_ladder_render.py" -q -rP` | `X29: server_order_before=[1, 2] server_order_after_reload=[2, 1] periodic_refreshPool_rerenders_ladder=False tap_post_rerenders_ladder=True stale_badge_mirrored_each_refreshPool=True browser_timing=UNPROVEN(no browser in the suite)` · `1 passed in 0.58s` | NOT HELD |
| O3 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/stale_score tests/experiments/f15_p1 tests/experiments/setups_one tests/experiments/handicap_h1` (no `.env`, no Postgres settings; at tip `4a690fbe`) | `38 passed, 26 skipped in 1067.48s (0:17:47)`, exit 0, no ERROR. Skips: 12 stale_score (11 `_db` modules + `test_xl76_devdb_absence.py:18`) and 6 f15_p1 `_db` → `Postgres env settings not available`; 5 setups_one → `requires_db: needs cobalt_dev`; 3 handicap_h1 → `needs cobalt_dev (run inside THE LOCK)` | NOT HELD (X2 offline: nothing errors at setup) |
| O4 | own | ONE lock take (11:21:41 EDT, `lock taken: x29-fixture-1010`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → this worktree's line alone); `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` (= the build's F0); `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `NOTHING WAS APPLIED`, `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, last line `TABLES 0011` (no `LEVEL` line is printed by the CLI itself; the fingerprint equals the build gate's F0 at `LEVEL 0013`); `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/experiments/stale_score tests/experiments/f15_p1 tests/experiments/setups_one tests/experiments/handicap_h1`; `<FP>` after → `664 35 272c95bbb12241e3611e4b36326ccf87`; release → `lock released`; `ls …/.env` → `No such file or directory` | `2 failed, 62 passed in 2385.93s (0:39:45)`. `FAILED tests/experiments/f15_p1/test_x12_transition_ids_db.py::test_x12_iii_transition_ids_rise_in_commit_order_under_the_row_lock` and `FAILED tests/experiments/f15_p1/test_x5_tap_vs_refresh_db.py::test_x5_a_tap_and_a_refresh_on_one_card_both_commit`, both `…/tests/experiments/f15_p1/test_x12_transition_ids_db.py:93: TypeError: CardStore.create_radar_card() missing 1 required keyword-only argument: 'proposed_key_reason'`. `grep -n -F "offline skip mark"` → nothing (no G1 refusal); `grep -n -F "SKIPPED"` → nothing; no ERROR at setup (the `ERROR` hits are log lines of passing tests). | NOT HELD (X2 with Postgres: nothing errors at setup, nothing fails G1). The two reds are an experiment test body against a `src` signature — the fence (`## NOT IN THIS JOB`: any experiment test body; a red outside this fix) → `## DECISIONS`, UNPROVEN, OUT OF SCOPE |
| S1 | Sol | the house's test pasted unchanged into `tests/cobalt/test_experiment_conftests.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_experiment_conftests.py::test_a1_rejects_a_non_fixture_offline_skip_guard_assignment` | `1 failed in 0.05s`; first failing line `E       Failed: DID NOT RAISE <class 'AssertionError'>` (`tests/cobalt/test_experiment_conftests.py:58`) | HELD — red for the stated reason. The card's red-first text ("a line starting `offline_skip_guard = `") does not rule an alias to another value right; the row's fix line is `offline_skip_guard = _conftest.offline_skip_guard` |
Committed before the fix: `4a690fbe wip(x29-fixture-1010): check red — S1`.

## FIXES
| id | file | change | proof | commit |
|---|---|---|---|---|
| S1 | `tests/cobalt/test_experiment_conftests.py` | new `_aliases(source, name)`: a line that starts `<name> = ` AND ends `.<name>`; A1 checks the guard with it (the `dev_db_tx` listing keeps `_reexports`) | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_experiment_conftests.py` → `3 passed in 0.03s` | `3c00e204 fix(x29-fixture-1010): A1 requires the guard line to alias the fixture (check S1)` |
DevDocs line: none. The changed file is a test; Grep for `test_experiment_conftests` or `experiment conftest` under `docs/40 - DevDocs/cobalt` → no files (the build found the same: pages exist per `src` module only).

## Suites
RESTARTS first: `uv run cobalt jobs restarts 82da1f1b..HEAD` → whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/x29-fixture-build-2026-10-10.md	A	DOCS	-
tests/cobalt/test_experiment_conftests.py	A	test/documentation; no resident	-
tests/experiments/f15_p1/conftest.py	M	test/documentation; no resident	-
tests/experiments/handicap_h1/conftest.py	M	test/documentation; no resident	-
tests/experiments/setups_one/conftest.py	M	test/documentation; no resident	-
tests/experiments/stale_score/conftest.py	M	test/documentation; no resident	-
RESTARTS: none
```
(matches the card's expected labels.)
`sh /Users/cobalt/cobalt/ops/desk/gate.sh x29-fixture-1010 all --deploy` on `3c00e204` (no `--deselect`, no `--tickers`, no `--migration`; started 12:02:21, ended by 12:31:11 EDT) · exit 0 · verdict lines whole:
```
offline 4199/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5096/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/x29-fixture-1010-all-20261010-120220.log
```
- offline 4199 = the build's 4198 + this check's `test_a1_rejects_a_non_fixture_offline_skip_guard_assignment`; with-DB 5096 = 5095 + the same test (pass 1 runs the offline tests again, by design).
- `grep -n -F "OUTSIDE" <log>` → nothing. `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :896) · `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :2030).
- `.env`: `ls /Users/cobalt/cobalt-wt/x29-fixture-1010/.env` → `No such file or directory` (after O4's release and again after the gate). `git status --short --branch` → `## ops/x29-fixture-1010`.
- Every new test shown red first: S1 under `## RUNS` (`DID NOT RAISE`).

## Scope
PREFLIGHT's path union: the four experiment conftests and `tests/cobalt/test_experiment_conftests.py`, all of them in row A's `files`. My commits (`4a690fbe`, `3c00e204`) touch only `tests/cobalt/test_experiment_conftests.py`, which is row A's file. Nothing was built inside `## NOT IN THIS JOB` ((iii) below). No path reaches a score, rank, grade or size: the change is test-only, and RESTARTS shows no resident.

## Checked against the branch
- (i) `git log --oneline d083ec76..HEAD -- . ":(exclude)docs"` → `3c00e204 fix(x29-fixture-1010): A1 requires the guard line to alias the fixture (check S1)` · `4a690fbe wip(x29-fixture-1010): check red — S1`. `<tip now>` = `3c00e204`.
- (ii) `git log --stat --format=%h d083ec76..HEAD` → `3c00e204` and `4a690fbe`: `tests/cobalt/test_experiment_conftests.py` only (row A's file); `e1d5a6b0`: the build report (docs). No other path.
- (iii) fence, each `git log --oneline 82da1f1b..HEAD -- <path>` → EMPTY: `tests/cobalt/conftest.py`, `src`, `tests/experiments/stale_score/test_x29_ladder_render.py`, `ops/desk/gate-lists.md`.
- (iv) `grep -n -F "def test_a1_rejects_a_non_fixture_offline_skip_guard_assignment" tests/cobalt/test_experiment_conftests.py` → `50:def test_a1_rejects_a_non_fixture_offline_skip_guard_assignment(monkeypatch):`; its red `4a690fbe` sits below its fix `3c00e204` in (i).
- (vi) `git log --stat --format=%h 82da1f1b..HEAD -- src/cobalt/db_migrations tests/cobalt` → only `tests/cobalt/test_experiment_conftests.py` (`67fb195a`, `4a690fbe`, `3c00e204`): no migration, no with-DB test needing a level above `0013` → no gate-lists entry owed.
- (vii) card RECORDS: `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- tests src` → ` tests/ops/test_bare_guard.py | 62 ++++…` · `1 file changed, 62 insertions(+)` — the record expected "nothing or only docs"; the one path is `tests/ops`, none of the conftests or files this card reads (recorded under `## RECORDS`). RESTARTS record: matches (`## Suites`).

## OPEN
none. OUT OF SCOPE (fence: "any experiment test body"; "a red outside this fix"): the two f15_p1 with-DB reds of O4, carried under `## DECISIONS`.
Counts: findings 6 (own O1–O5, Sol S1, Grok none) · dropped 0 · held 1 (S1) · fixed 1 · held unfixed 0 · open 0.

## CONTINUE
next: done (CLOSE)

## DECISIONS
- DECISION O4 (UNPROVEN, L70; outside this fix; not FOR DEJAN): with the Postgres settings (O4 run, one lock take), `tests/experiments/f15_p1/test_x12_transition_ids_db.py::test_x12_iii_transition_ids_rise_in_commit_order_under_the_row_lock` and `tests/experiments/f15_p1/test_x5_tap_vs_refresh_db.py::test_x5_a_tap_and_a_refresh_on_one_card_both_commit` fail with `…/tests/experiments/f15_p1/test_x12_transition_ids_db.py:93: TypeError: CardStore.create_radar_card() missing 1 required keyword-only argument: 'proposed_key_reason'`. The experiment's test body calls an older signature. The fence keeps experiment test bodies out of this job, so it is not fixed here. Safe default taken: ship row A as checked; this red goes to the follow-up list. The two tests sit outside the suites (`tests/experiments` is run by explicit path).

## RECORDS
- Clock at first write: Sat Oct 10 10:51:22 EDT 2026; close 12:31:11 EDT.
- Dropped findings: none. No house produced nothing: Sol `FINDINGS: 1`, Grok `FINDINGS: 0`.
- Sol's printed transcript shows it opened `LAWS.md`, `preferences.md` and `profile.md` under `/Users/cobalt/Vault/Think/6 - Permanent/Memory/` with `sed`/`cat`. The HOUSE-INSTRUCTIONS did not name them. Its `-s read-only` sandbox let the reads through. Recorded as a fact. Nothing it read was used here.
- Card RECORDS (vii): `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- tests src` now prints `tests/ops/test_bare_guard.py | 62 +` (main moved after the drafter's read). That file is not one the card reads.
- One extra lock take by hand, for O4 (X2 with Postgres): taken 11:21:41 EDT; `<FP>` before = after = `664 35 272c95bbb12241e3611e4b36326ccf87`; `lock released`; `.env: removed, proven gone (O4)`. The gate's own take waited 0 min.
- REFUSED, not needed: none. CONTINUED: none.
- files opened: 16. They are `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`), the build report, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `tests/cobalt/conftest.py`, the five experiment conftests, `test_x29_ladder_render.py`, `test_experiment_conftests.py`, Sol's output, Grok's output and `<S>/house-b.md`. The background task outputs for the probe, the lock, the runs and the gate were also read.
- Check of `x29-fixture-1010`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: x29-fixture-1010 · pass: 1 · tip: 3c00e204 · house A: Sol FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 0 · suites: offline 4199/0 · with-DB 5096/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 167561
