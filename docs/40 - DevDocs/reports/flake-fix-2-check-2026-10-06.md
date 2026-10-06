# flake-fix-2 — check report 2026-10-06

## §0 Headline
- 10 findings: 4 mine, 2 from Sol, 4 from Grok. None dropped. One held and is fixed. Four are REJECTED and stay open as follow-ups (A1, B1, B2, B4). One is out of scope (B3).
- A2 (Sol) held: the XL76 harness called `open_migrated` before its `try`, so a failed migration step no longer printed `harness_applies=False`. The red is `10b4d7a3`; the fix is `1a52ad0d`.
- X1–X4 are answered by running them: the loop is written once (O1); no `_apply` caller is missing (O2); the red test fails with `DeadlockDetected` from the radar test's own migration step when the retry is removed (O3).
- The gate passed on `1a52ad0d`: offline 3937/0, with-DB 4820/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0), `.env` is removed, RESTARTS none. ready: YES, decisions: 0.

## L74
A system reminder at session start asked commits to end with a `Claude-Session:` line. Recorded once here. Not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md"`, exit 0, output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md" · 0 · db48db78f03d1cf3a42dff2bf805e07f4638c7e3
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/14-flake-fix-2-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-03 R326 row · grep -n "^| R326 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · 332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — D5 ships at `c96b5118` with O1 pinned (follow-up card: items' store + B2 wording); second-writer survey gets its 5 read strings, this seat only; F15 P2 X11 → follow-up card. Words: `cto-2026-10-05-words.md` R326–R327. | HIS RULING · APPROVED |
RULING 2026-10-03 R326 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R326 |" -- "docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · b133743171ec855e164c445ceef03e657eb50eeb
RULING 2026-10-03 R326 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-03.md" · 0 · the row as grepped
RULING 2026-10-05 R412 row · grep -n "^| R412 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 109:| R412 | 10-05 13:16 ET | HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); drafter rule (contract); order preflight.sh x2, then hub text; no outside-house reads; production HOLD ([words](cto-2026-10-05-words.md)). | APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) |
RULING 2026-10-05 R412 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R412 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · b3583b280d50c829da1d8f5290c2c385b50ef68c
RULING 2026-10-05 R412 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
RULING 2026-10-05 R474 row · grep -n "^| R474 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 140:| R474 | 10-05 21:42 ET | HIS RULING · APPROVED: tonight he is not woken; every conflict goes to the brain, which resolves it; the desk executes its answer and keeps deploying (L43); only an absolute stop waits for morning. In NOW (TONIGHT line). | HIS RULING · APPROVED |
RULING 2026-10-05 R474 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R474 |" -- "docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · 548ee01d911745c95050220e69684ebb94109782
RULING 2026-10-05 R474 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-05.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row, `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` · `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row, `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` · `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`, exit 0, output whole:
```
clock · date · 0 · Tue Oct  6 06:58:03 EDT 2026
status · git status --short --branch · 0 · ## ops/flake-fix-2-1006
head · git log --oneline -1; git log --stat --format=%h fb3117c3..HEAD · 0 · (5 lines)
    b1bee19a docs(flake-fix-2): build report — fb3117c3
    b1bee19a
    
     .../reports/flake-fix-2-build-2026-10-06.md        | 188 +++++++++++++++++++++
     1 file changed, 188 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/flake-fix-2-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/flake-fix-2-1006/docs/40 - DevDocs/reports/flake-fix-2-build-2026-10-06.md" · 0 · BUILT · job: flake-fix-2 · tip: fb3117c3 | on 71f69821 | migration: none | offline 3936/0 | with-DB 4819/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 2 of 3 | decisions: 2 · for Dejan: 0 · tokens: 230163
report: self-check 2 of 3 (recorded)
range · git log --oneline 71f69821..fb3117c3 · 0 · (2 lines)
    fb3117c3 fix(flake-fix-2): one open_migrated helper retries the first migration apply on DeadlockDetected; every self-migrating test calls it (F1, L3 L45)
    5a9fb3b4 wip(flake-fix-2): red — F1 (open_migrated tests, radar_score_migration retry test)
PREFLIGHT OK
```
- Self-check `2 of 3` recorded; it goes to the houses as a fact (the build report's DECISION F1-b).
- THE RANGE, `git log --stat --format=%h 71f69821..fb3117c3` → `fb3117c3`: `docs/40 - DevDocs/cobalt/db_migrations/cli.md` 3, `docs/40 - DevDocs/cobalt/drc/store.md` 3, `tests/cobalt/migration_retry.py` 45, `tests/cobalt/radar_migrated_support.py` 6, `tests/cobalt/test_archiver_migrations.py` 17, `tests/cobalt/test_drc_store.py` 22, `tests/cobalt/test_p4_migrations.py` 20, `tests/cobalt/test_radar_handicap_store.py` 11, `tests/cobalt/test_radar_score_migration.py` 14, `tests/cobalt/test_stale_score_db.py` 12, `tests/cobalt/test_tenancy.py` 9, `tests/cobalt/test_voice_store.py` 13, `tests/experiments/handicap_h1/test_xl76_membership_harness.py` 9 — `13 files changed, 83 insertions(+), 101 deletions(-)`; `5a9fb3b4`: `tests/cobalt/test_migration_retry.py` 114, `tests/cobalt/test_radar_score_migration.py` 21 — `2 files changed, 135 insertions(+)`. Path union: 14 paths, 2 under `docs/`, 12 under `tests/`.
- `ls /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/flake-fix-2-check` → exit 1, `No such file or directory` (fresh).
- `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` → exit 0: `sol: UP` · `grok: UP` · `gemini: UP`.
- **house A: OpenAI Sol · house B: Grok.** HOUSE B: as needed (not mandatory).
- Proven by first real use: the with-DB strings at a lock take or `gate.sh`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`, exit 0, output whole (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/flake-fix-2-check`):
```
24708 <S>/diff.md
9514 <S>/files/14-flake-fix-2-card.md
35675 <S>/files/flake-fix-2-build-2026-10-06.md
24217 <S>/files/wt/docs/40 - DevDocs/cobalt/db_migrations/cli.md
15593 <S>/files/wt/docs/40 - DevDocs/cobalt/drc/store.md
1820 <S>/files/wt/tests/cobalt/migration_retry.py
3080 <S>/files/wt/tests/cobalt/radar_migrated_support.py
26947 <S>/files/wt/tests/cobalt/test_archiver_migrations.py
25397 <S>/files/wt/tests/cobalt/test_drc_store.py
3659 <S>/files/wt/tests/cobalt/test_migration_retry.py
28126 <S>/files/wt/tests/cobalt/test_p4_migrations.py
11284 <S>/files/wt/tests/cobalt/test_radar_handicap_store.py
23648 <S>/files/wt/tests/cobalt/test_radar_score_migration.py
11555 <S>/files/wt/tests/cobalt/test_stale_score_db.py
31024 <S>/files/wt/tests/cobalt/test_tenancy.py
12531 <S>/files/wt/tests/cobalt/test_voice_store.py
7319 <S>/files/wt/tests/experiments/handicap_h1/test_xl76_membership_harness.py
1150 <S>/rulings.md
STAGED 18 files · 297247 bytes · commits 2
```
(The script printed full paths; `<S>` abbreviates them here.) `commits 2` = PREFLIGHT's range count; `grep -c "^commit " <S>/diff.md` → `2`.
`stage-copy.sh`, the three reports `## READ` names: `COPIED 31016 <S>/files/flake-fix-build-2026-10-06.md` · `COPIED 43305 <S>/files/flake-fix-check-2026-10-06.md` · `COPIED 7282 <S>/files/second-writer-survey-2026-10-05.md`. The `## READ` test files are among the staged files above.
`<S>/HOUSE-INSTRUCTIONS.md` written: the HOUSE TEXT, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
Launch, 06:59:41 EDT (`date`), house gates re-run (R17 row 35, R19 row 37, R19 commit `5055151d…`), `cd /Users/cobalt/cobalt-wt/agy-trial`; house A Sol `codex exec …` (task `bf8da5o4l`) and house B Grok `grok -m grok-4.7 … house-b.md` (task `bslb20g2s`), both `run_in_background`, timeout 2700000; `cd` back; `git status --short --branch` → `## ops/flake-fix-2-1006`.

## OWN FINDINGS
Written before either house's list was opened. Read: the card, the diff `71f69821..fb3117c3` (tests), `tests/cobalt/migration_retry.py`, `tests/experiments/handicap_h1/test_xl76_membership_harness.py:100-195`, `tests/experiments/handicap_h1/conftest.py`, `tests/cobalt/test_dev_rebuild_db.py:30-69`, `tests/cobalt/test_db_only_selection.py:330-479`, `tests/cobalt/test_drc_d2_fix_r1_db.py:95-129`, plus `grep -rn -F "connect_migration" tests/` and `grep -rln -F "_apply(" tests/` at the tip. Each finding states the defect it tests for; a clean run means the defect is absent.

FINDING O1
ROW: X1
CLAIM: a copy of the retry loop is left in a test file besides `tests/cobalt/migration_retry.py:45` (the loop's print line).
RUN: COMMAND `grep -rn -F "migration retry {attempt}" tests/`
EXPECT: a hit in a file other than `tests/cobalt/migration_retry.py`.

FINDING O2
ROW: X3
CLAIM: a test still opens its own migration connection inline (`autocommit = False` after `connect_migration`) and applies migrations on it. Every `connect_migration` hit at the tip outside the helper is a catalog read, a fake, or a pass-through (`tests/experiments/handicap_h1/test_xl76_membership_harness.py:181`, `tests/cobalt/test_dev_rebuild_db.py:43`, `tests/cobalt/test_migrate_proof.py:190`…, `tests/cobalt/test_drc_store.py:427`).
RUN: COMMAND `grep -rn -F "autocommit = False" tests/cobalt tests/experiments`
EXPECT: a hit in a file whose next lines call `_apply(conn` on that connection.

FINDING O3
ROW: F1 (red first) / X4
CLAIM: `test_the_migration_step_retries_a_first_deadlock` (`tests/cobalt/test_radar_score_migration.py:506`) stays green when the helper's retry is removed, so it does not pin the fix.
RUN: TEST — the existing test, run with-DB inside one lock take, once with `tests/cobalt/migration_retry.py:44` changed to `if True:` (no retry; made and undone with Edit, never committed) and once as committed.
EXPECT: if the claim is true, the mutated run passes. (The fix holds if the mutated run FAILS with `psycopg.errors.DeadlockDetected` raised from the `open_migrated` call at `test_radar_score_migration.py:411`.)

FINDING O4
ROW: SCOPE
CLAIM: the build moved the import of `migration_retry` into a file that cannot resolve it: `tests/experiments/handicap_h1/test_xl76_membership_harness.py:112` imports `migration_retry` by bare name, and only `tests/experiments/handicap_h1/conftest.py:26` puts `tests/cobalt` on `sys.path`.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/handicap_h1/test_xl76_membership_harness.py::test_xl76_2_3_harness_shape_at_step_1`
EXPECT: `ModuleNotFoundError: No module named 'migration_retry'` if the claim is true. Offline the test skips (`requires_db`), so a clean run shows a skip, not an import error.

No defect seen on reading that needs a new test. The two items the build already raised, F1-a (the XL76 harness errors at setup, `offline_skip_guard`) and F1-b (15 of 17 call sites unpinned), are not repeated as findings: F1-a is a red outside the row (the fence), and F1-b names no wrong behaviour at the tip.

## Findings
House A Sol `<S>/house-a.md` (`FINDINGS: 2`); house B Grok `<S>/house-b.md`, written by Grok itself (`FINDINGS: 4`). Both opened only after `## OWN FINDINGS` was written, at 07:12:03 EDT (`date`). THE DROP: every block has a `RUN:` line followed by a `def test_` or one command beginning `git diff` / `uv run pytest`; none dropped.

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| O1 | own | X1 | a copy of the retry loop is left outside `migration_retry.py` | COMMAND |
| O2 | own | X3 | a test still opens a migration conn inline and applies migrations on it | COMMAND |
| O3 | own | F1 / X4 | the radar_score red test stays green when the helper's retry is removed | TEST (mutation) |
| O4 | own | SCOPE | the XL76 harness cannot import `migration_retry` by bare name | COMMAND |
| A1 | Sol | X1 | the range is not tests-only: two DevDocs files changed | COMMAND |
| A2 | Sol | F1 | XL76 calls `open_migrated` before its `try`, so a failing migration no longer prints `harness_applies=False` | TEST |
| B1 | Grok | X3 | `tests/experiments/stale_score/test_xl76_devdb_absence.py:22-26` runs the 0015 rollback (`OWNER TO`) on its own migration conn without the helper | TEST |
| B2 | Grok | F1 | 15 of 17 call sites have no test pinning the retry line | TEST |
| B3 | Grok | F1 | the handicap_h1 conftest lacks `offline_skip_guard`, so the edited XL76 caller never runs | COMMAND |
| B4 | Grok | X1 | the tip is not tests-only: two DevDocs files | COMMAND |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -rn -F "migration retry {attempt}" tests/` | one hit, `tests/cobalt/migration_retry.py:45:            print(f"migration retry {attempt}: DeadlockDetected")` | NOT HELD — the loop is written once (X1) |
| O2 | own | `grep -rn -F "autocommit = False" tests/cobalt tests/experiments` | hits read one by one: `conftest.py:301`, `test_migrate_proof.py:191/289/308/1328/1678/2118`, `test_x5_tap_refresh_db.py:333`, `test_tenancy.py:252`, `test_archiver_migrations.py:579/596/624`, `test_radar_score_migration.py:334/359`, `test_dev_rebuild_db.py:44`, `test_xl76_membership_harness.py:182`, `test_x12_transition_ids_db.py:153` — each a catalog read, a lock holder or a `real_connect` row probe, none calls `_apply`; plus `tests/experiments/stale_score/test_xl76_devdb_absence.py:23`, which executes the `0015` rollback SQL (B1) | NOT HELD for `_apply` callers (X3: none missing from the row's list); the raw-SQL case is B1 |
| O3 | own | with-DB, one lock take: `tests/cobalt/migration_retry.py:44` → `if True:` (Edit), `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=short tests/cobalt/test_radar_score_migration.py::test_the_migration_step_retries_a_first_deadlock`; undone (Edit); same command | mutated: `1 failed in 0.08s`, chain `:521 test_card_checks_index_and_receipt_immutability_on_cobalt_dev()` → `:411 conn = open_migrated(_apply, FORWARD)` → `migration_retry.py:35 apply(conn, paths)` → `:517 in fake` → `E   psycopg.errors.DeadlockDetected: constructed by flake-fix-2 F1`. Restored: `PASSED …::test_the_migration_step_retries_a_first_deadlock`, `1 passed in 0.27s`. `git diff --stat` after the undo → only the not-yet-committed A2 test | NOT HELD — the test pins the fix (X4: the red is a call-phase `DeadlockDetected` from the radar test's own migration step, now at `:411`, which on BASE was `:420`) |
| O4 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/handicap_h1/test_xl76_membership_harness.py::test_xl76_2_3_harness_shape_at_step_1` | `SKIPPED [1] …:104: XL76 (2)/(3): needs cobalt_dev (run inside THE LOCK)` · `1 skipped in 0.01s`; no import error (`tests/experiments/handicap_h1/conftest.py:26` puts `tests/cobalt` on `sys.path`) | NOT HELD |
| A1 | Sol | `git diff --name-only 71f69821..fb3117c3` | 14 paths: `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/drc/store.md`, and 12 under `tests/` | REJECTED — `BUILD-HUB.md` `## E3`: "Each changed module gets ONE dated line in its page under `docs/40 - DevDocs/cobalt/`"; `CHECK-HUB.md` `## 7` (ii) allows docs paths. The output is as claimed; the two docs paths are the required DevDocs lines, not code |
| A2 | Sol | its test, pasted whole into `tests/cobalt/test_migration_retry.py`, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_migration_retry.py::test_xl76_reports_false_when_the_migration_step_fails` | `1 failed in 0.07s`: `tests/cobalt/test_migration_retry.py:145: AssertionError` · `E       AssertionError: assert 'XL76: harness_applies=False' in ''` | HELD — `open_migrated` sat before the `try` (`test_xl76_membership_harness.py:152` at TIP), so the `finally` that prints `harness_applies` never ran. At BASE the apply sat inside that `try`. Committed red `10b4d7a3` |
| B1 | Grok | its test, pasted into `tests/cobalt/test_migration_retry.py`, run alone | `1 failed in 0.04s`: `tests/cobalt/test_migration_retry.py:161: AssertionError` · `E       assert 'open_migrated' in '"""XL76 (L76: no migration left applied …` (the three asserts above it passed) | REJECTED — the card's row: "A test that only reads a catalog on `db.connect_migration` and applies nothing is not a caller (… `tests/experiments/stale_score/test_xl76_devdb_absence.py:22` …): not changed." Red for the stated reason; the file does run the `0015` rollback (`ALTER VIEW … OWNER TO`) inside a rolled-back transaction, so it can meet the same deadlock. Test removed again (Edit). OPEN |
| B2 | Grok | its test, pasted into `tests/cobalt/test_migration_retry.py`, run alone | `1 failed in 0.05s`: `tests/cobalt/test_migration_retry.py:186: AssertionError` · `E       AssertionError: ['tests/cobalt/radar_migrated_support.py', 'tests/cobalt/test_p4_migrations.py', 'tests/cobalt/test_voice_store.py', 'tests/cobalt/test_archiver_migrations.py', 'tests/cobalt/test_stale_score_db.py', 'tests/cobalt/test_tenancy.py', ...]` | REJECTED — the row's `red first` names the radar-score test and the four helper tests only. Red for the stated reason; it is the build's own DECISION F1-b (15 call sites unpinned). Test removed again (Edit). OPEN |
| B3 | Grok | `uv run pytest -q -p no:cacheprovider --tb=short tests/experiments/handicap_h1/test_xl76_membership_harness.py::test_xl76_1_the_with_db_callers` | exit 1, `ERROR at setup of test_xl76_1_the_with_db_callers` · `def dev_db_tx(monkeypatch, request, offline_skip_guard):` · `E       fixture 'offline_skip_guard' not found` · `1 error in 0.01s`. `git log --oneline 71f69821..fb3117c3 -- tests/experiments/handicap_h1/conftest.py tests/cobalt/conftest.py` → empty (neither conftest changed by the build) | REJECTED — `## NOT IN THIS JOB`: "`tests/cobalt/conftest.py`" and "A red outside this row: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here." The output is as claimed; the red predates the build. OUT OF SCOPE (the build's DECISION F1-a) |
| B4 | Grok | same command as A1 | same 14 paths | REJECTED — as A1 |

## FIXES
| id | fix | held test → | commit |
|---|---|---|---|
| A2 | `tests/experiments/handicap_h1/test_xl76_membership_harness.py`: `conn = None` and `applies = False` before the `try`; `started`, `open_migrated(_apply, FORWARD)` and `apply_ms` inside it; the `finally` rolls back and closes only an opened `conn`, then prints `harness_applies`. The `started`/`apply_ms` timer still wraps the call (row (10)). DevDocs: `docs/40 - DevDocs/cobalt/db_migrations/cli.md` `## 2026-10-06 — flake-fix-2 check (A2)` | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_migration_retry.py tests/experiments/handicap_h1/test_xl76_membership_harness.py::test_xl76_2_3_harness_shape_at_step_1 tests/experiments/handicap_h1/test_xl76_membership_harness.py::test_xl76_close_0014_absent_on_cobalt_dev` → `5 passed, 2 skipped in 0.05s` (the two skips: `requires_db`, offline). `test_xl76_1` left out: B3's setup error, outside the row | `1a52ad0d fix(flake-fix-2): XL76 harness opens through open_migrated inside its try, so a failed migration step still prints harness_applies=False (check A2)` |

## Suites
RESTARTS first: `uv run cobalt jobs restarts 71f69821..HEAD` (HEAD `1a52ad0d`) → 15 rows, 3 `DOCS` and 12 `test/documentation; no resident`, all restart `-`, no `UNCLASSIFIED`; last line `RESTARTS: none`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh flake-fix-2-1006 all --deploy --tickers PRB` (no `--deselect`, no `--migration`; `PRB` is the constructed ticker the build's with-DB test writes in its rolled-back transaction), exit 0, verdict lines whole:
```
offline 3937/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (PRB)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4820/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/flake-fix-2-1006-all-20261006-071443.log
```
- The log ran on my tip: `grep -n -F "1a52ad0d" <log>` → `925:`, `1155:`, `1835:`, `1889:` `code: 1a52ad0d (clean) · /Users/cobalt/cobalt-wt/flake-fix-2-1006`.
- `grep -n -F " passed" <log>` → `861: 3937 passed, 786 skipped, 2 xfailed` (offline = the build's 3936 + A2's test) · `1085: 4632 passed, 7 skipped, 82 deselected, 4 xfailed` (pass 1) · `1771: 188 passed, 1 deselected` (pass 2; 4632 + 188 = 4820) · `1964: 146 passed, 1 skipped` (live-note). None of the seven SKIPPED lines is marked `OUTSIDE the allowed set`.
- `cobalt_dev: 0013 — F2 = F0`. `.env: removed`; `ls /Users/cobalt/cobalt-wt/flake-fix-2-1006/.env` → `No such file or directory` (07:42:50 EDT).

## Scope
PREFLIGHT's union: 14 paths (2 `docs/`, 12 `tests/`), all in F1's `files` or DevDocs lines. My commits add `tests/cobalt/test_migration_retry.py` (A2's test) and `tests/experiments/handicap_h1/test_xl76_membership_harness.py` (A2's fix), both in F1's `files`, and one DevDocs line. No `src/`, migration, conftest or `ops/desk/` path in `71f69821..HEAD`.

## Checked against the branch
- (i) `git log --oneline fb3117c3..HEAD -- . ":(exclude)docs"` → `1a52ad0d fix(flake-fix-2): XL76 harness opens through open_migrated inside its try, so a failed migration step still prints harness_applies=False (check A2)` · `10b4d7a3 wip(flake-fix-2): check red — A2`. `<tip now>` = `1a52ad0d`.
- (ii) `git log --stat --format=%h fb3117c3..HEAD` → `1a52ad0d`: `docs/40 - DevDocs/cobalt/db_migrations/cli.md` 3, `…/experiments/handicap_h1/test_xl76_membership_harness.py` 12; `10b4d7a3`: `tests/cobalt/test_migration_retry.py` 31; `b1bee19a`: the build report. Every non-docs path is in F1's `files`. No WIDENED.
- (iii) `git log --oneline 71f69821..HEAD -- src tests/cobalt/conftest.py ops/desk` → empty.
- (iv) `grep -n -F "def test_xl76_reports_false_when_the_migration_step_fails" tests/cobalt/test_migration_retry.py` → `117:def test_xl76_reports_false_when_the_migration_step_fails(monkeypatch, capsys):`; its red `10b4d7a3` sits below its fix `1a52ad0d` in (i).
- (vi) `git log --stat --format=%h 71f69821..HEAD -- src/cobalt/db_migrations tests/cobalt` → no migration file; the only new with-DB test (`test_the_migration_step_retries_a_first_deadlock`) runs at 0013 (it passed at 0013 in O3). No gate-list change owed.
- (vii) The card's RECORDS name `git -C /Users/cobalt/cobalt rev-parse HEAD` (not a listed prefix; not run) and the R326 / R412 / R474 rows, re-read by `authorize.sh` at AUTHORIZATION (rows 332, 109, 140). R501 is a desk record; not re-read.
- (viii) L32: this report holds no ticker, price or date of his; `PRB` is the build's constructed ticker.

## OPEN
FOLLOW-UP items. There is no second pass.
- A1 / B4 (Sol, Grok), REJECTED: X1's "touches only `tests/`" reads against two DevDocs files. These are the dated lines `BUILD-HUB.md` `## E3` requires, not code. Settled if the desk confirms that X1's `tests/` means "no code outside `tests/`".
- B1 (Grok), REJECTED by the card's row: `tests/experiments/stale_score/test_xl76_devdb_absence.py:22-26` runs the `0015` rollback SQL (`ALTER VIEW … OWNER TO`) on its own `connect_migration` connection, without the retry. The card names that file as not a caller. It can still meet the same autovacuum deadlock, but no gate suite runs `tests/experiments` (the build report's `gate-lists.md` grep), so a hit costs no gate rerun. Settled by a card of its own if it ever deadlocks.
- B2 (Grok), REJECTED by the row's `red first` list: 15 of the 17 call sites have no test that fails if they go back to an inline open. This is the build's DECISION F1-b. Settled by the desk choosing an offline lint (the build report's suggestion) on a later card, or no pin.
- OUT OF SCOPE, not open: B3 (Grok). `tests/experiments/handicap_h1/conftest.py` re-exports `dev_db_tx` without `offline_skip_guard`, so `test_xl76_1` errors at setup, and with `.env` so would `test_xl76_2_3`. Neither conftest changed in the range. The fence (`## NOT IN THIS JOB`, "a red outside this row") keeps it out. It is the build's DECISION F1-a. A2's fix is proven offline by its own test, which calls the harness function directly.

## CONTINUE
next: none — CLOSE done; the desk verifies and commits the report.

## DECISIONS
none

## RECORDS
- House A Sol finished at the notice 07:06:49 EDT (`date`), exit 0, `tokens used 198,389`. Sol writes no file; I wrote its FINAL message (output lines 8405-8448, ending `FINDINGS: 2`) to `<S>/house-a.md`. Its stream also printed the files it read (the earlier flake-fix check report among them) and draft blocks; only the final message is the list.
- House B Grok finished at the notice 07:12:03 EDT, exit 0; stdout ended with the path `<S>/house-b.md`; `ls -la <S>` → `house-b.md` 4423 bytes, 07:11, written by Grok. Its last line `FINDINGS: 4`.
- No house produced nothing. No finding dropped.
- B1's and B2's tests were pasted, run red, and removed again with Edit before the red commit, so `10b4d7a3` holds A2's test only.
- Extra lock take (O3): `take-devdb-lock.sh flake-fix-2-1006 90` → `lock taken: flake-fix-2-1006`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, this worktree's; `<FP>` before `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, after the same; `release-devdb-lock.sh` → `lock released`; `ls …/.env` → `No such file or directory` (07:14:13 EDT). `.env: removed, proven gone (O3)`.
- No `REFUSED, not needed` line; no `CONTINUED` line.
- Read beyond the hub's list: I read the build report whole, not only its four named sections. Files opened (23): CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK` to `## W`); the build report; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `tests/cobalt/test_db_only_selection.py`; `tests/cobalt/test_dev_rebuild_db.py`; `tests/experiments/handicap_h1/test_xl76_membership_harness.py`; `tests/experiments/handicap_h1/conftest.py`; `tests/cobalt/test_drc_d2_fix_r1_db.py`; `tests/cobalt/test_archiver_migrations.py`; `tests/experiments/stale_score/test_xl76_devdb_absence.py`; `tests/cobalt/test_radar_score_migration.py`; `tests/cobalt/test_tenancy.py`; `tests/cobalt/test_migration_retry.py`; `docs/40 - DevDocs/cobalt/db_migrations/cli.md`; `<S>/house-b.md`; the task outputs of the probe, Sol, Grok, the lock take and the gate. The diff was read through `git diff`.
- Check of `flake-fix-2`: house A `Sol`, house B `Grok`, and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: flake-fix-2 · pass: 1 · tip: 1a52ad0d · house A: Sol FINDINGS: 2 · findings: 10 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 4 · suites: offline 3937/0 · with-DB 4820/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 23 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 203860
