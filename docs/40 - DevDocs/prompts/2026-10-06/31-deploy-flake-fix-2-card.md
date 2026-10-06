JOB: deploy-flake-fix-2-1006
LADDER: OFF-LADDER — cto-2026-10-03.md R326
BRANCH: deploy/deploy-flake-fix-2-1006
WORKTREE: deploy-flake-fix-2-1006
BASE: main
TIP: 1a52ad0d
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-flake-fix-2-1006.md
RULINGS: 2026-10-03 R326, 2026-10-05 R412, 2026-10-05 R474
TAG: deploy-2026-10-06-flake-fix-2
MIGRATIONS: none
SET: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/flake-fix-2-1006` | `1a52ad0d` | `1a52ad0d` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-2-check-2026-10-06.md` | `held unfixed: 0` and `ready: YES` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/flake-fix-2-1006`, 15 files, 442 insertions, 101 deletions), each with its RESTARTS class (the check's `uv run cobalt jobs restarts 71f69821..HEAD`: 15 rows, 3 DOCS and 12 `test/documentation; no resident`, no `UNCLASSIFIED` row; the check's line `RESTARTS: none`):
- `tests/cobalt/migration_retry.py` (new; the one `open_migrated(apply, paths)` helper), `tests/cobalt/test_migration_retry.py` (new; the helper's tests and A2's test), `tests/cobalt/test_drc_store.py`, `tests/cobalt/radar_migrated_support.py`, `tests/cobalt/test_radar_score_migration.py`, `tests/cobalt/test_p4_migrations.py`, `tests/cobalt/test_voice_store.py`, `tests/cobalt/test_archiver_migrations.py`, `tests/cobalt/test_stale_score_db.py`, `tests/cobalt/test_tenancy.py`, `tests/cobalt/test_radar_handicap_store.py`, `tests/experiments/handicap_h1/test_xl76_membership_harness.py`: all test/documentation; no resident.
- `docs/40 - DevDocs/cobalt/db_migrations/cli.md` and `docs/40 - DevDocs/cobalt/drc/store.md` (the dated DevDocs lines BUILD-HUB E3 requires, plus the check's A2 line; DOCS).
- `docs/40 - DevDocs/reports/flake-fix-2-build-2026-10-06.md` (the build report; DOCS).
RESTARTS: none. A test-side fix: no `src/` path, no `ops/desk/` path, no `tests/cobalt/conftest.py` and no migration file is in the diff (the check's `## Checked against the branch` (iii) and (vi), each empty).

## MARKERS
- `grep -c -F "def open_migrated(apply, paths)" /Users/cobalt/cobalt/tests/cobalt/migration_retry.py` · before: file absent on main (`ls` exit 1) · after `1`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `3`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/radar_migrated_support.py` · before `0` · after `2`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_radar_score_migration.py` · before `0` · after `3`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_p4_migrations.py` · before `0` · after `4`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_voice_store.py` · before `0` · after `3`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_archiver_migrations.py` · before `0` · after `4`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_stale_score_db.py` · before `0` · after `2`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_tenancy.py` · before `0` · after `3`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/cobalt/test_radar_handicap_store.py` · before `0` · after `2`
- `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/experiments/handicap_h1/test_xl76_membership_harness.py` · before `0` · after `2` (check A2: the open sits inside the `try`)
- `grep -c -F "migration retry" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `8` · after `7` (the loop and its print line moved to the helper; the fixture's tests keep their asserts)
- `grep -c -F "def test_the_migration_step_retries_a_first_deadlock" /Users/cobalt/cobalt/tests/cobalt/test_radar_score_migration.py` · before `0` · after `1`
- `grep -c -F "def test_first_deadlock_retries_once_on_a_fresh_connection" /Users/cobalt/cobalt/tests/cobalt/test_migration_retry.py` · before: file absent on main · after `1`
- `grep -c -F "def test_xl76_reports_false_when_the_migration_step_fails" /Users/cobalt/cobalt/tests/cobalt/test_migration_retry.py` · before: file absent on main · after `1` (check A2)
- `grep -c -F "flake-fix-2" "/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/db_migrations/cli.md"` · before `0` · after `2`
- `grep -c -F "flake-fix-2" "/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/drc/store.md"` · before `0` · after `1`

## SMOKE READS
- the shared helper (F1) · `grep -c -F "def open_migrated(apply, paths)" /Users/cobalt/cobalt/tests/cobalt/migration_retry.py` · exit 0, a count of 1 or more
- the radar-score retry test (F1 red) · `grep -c -F "def test_the_migration_step_retries_a_first_deadlock" /Users/cobalt/cobalt/tests/cobalt/test_radar_score_migration.py` · exit 0, a count of 1 or more
- the XL76 harness through the helper (A2) · `grep -c -F "open_migrated" /Users/cobalt/cobalt/tests/experiments/handicap_h1/test_xl76_membership_harness.py` · exit 0, a count of 1 or more
- the A2 test · `grep -c -F "def test_xl76_reports_false_when_the_migration_step_fails" /Users/cobalt/cobalt/tests/cobalt/test_migration_retry.py` · exit 0, a count of 1 or more

## RECORDS
- flake-fix-2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-2-check-2026-10-06.md` last line: CHECK DONE · job: flake-fix-2 · pass: 1 · tip: 1a52ad0d · house A: Sol FINDINGS: 2 · findings: 10 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 4 · suites: offline 3937/0 · with-DB 4820/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 23 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 203860
- flake-fix-2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/flake-fix-2-1006` → `1a52ad0d` (also the head of `git -C /Users/cobalt/cobalt log --oneline main..ops/flake-fix-2-1006`, 5 commits, not merged); code tip `1a52ad0d` (the check's fix commit, A2; its red test is `10b4d7a3`); the job card's own TIP header reads `fb3117c3` (the build tip); the build report commit `b1bee19a` sits between them (docs only). House A was Sol, house B was Grok. The gate on `1a52ad0d`: offline 3937/0, with-DB 4820/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut. This job moves the retry into one shared helper and covers every self-migrating test the job card lists.
- FOLLOW-UP for him, NOT part of this deploy: the check's `## OPEN`. A1 / B4: X1's "touches only `tests/`" against the two required DevDocs lines (settled if the desk confirms X1 means no code outside `tests/`). B1: `tests/experiments/stale_score/test_xl76_devdb_absence.py:22-26` runs the 0015 rollback on its own connection without the helper; no gate suite runs `tests/experiments`; a card of its own if it ever deadlocks. B2: 15 of the 17 call sites have no test pinning them to the helper; the desk may choose an offline lint on a later card, or no pin.
- FOLLOW-UP for him, NOT part of this deploy: the build's F1-a (the XL76 harness file errors at setup, `fixture 'offline_skip_guard' not found`; `tests/experiments/handicap_h1/conftest.py` re-exports `dev_db_tx` without it; no gate suite runs it; the check's B3, out of scope) and F1-b (the same gap as B2).
- AFTER values above were read from the checked-out worktree `/Users/cobalt/cobalt-wt/flake-fix-2-1006` (the branch `ops/flake-fix-2-1006`, head `1a52ad0d` verified by `rev-parse`), BEFORE values from main's working tree, at drafting time 2026-10-06 07:45 EDT; the deploy re-proves each with `git -C /Users/cobalt/cobalt show 1a52ad0d:<path>`.
- Absent today: `git rev-parse --verify` of `deploy/deploy-flake-fix-2-1006` and of `deploy-2026-10-06-flake-fix-2` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-flake-fix-2-1006` and of the REPORT path both failed.
- one feature per deploy (his R390).
