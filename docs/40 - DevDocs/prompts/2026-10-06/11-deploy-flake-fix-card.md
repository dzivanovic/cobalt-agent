JOB: deploy-flake-fix-1006
LADDER: OFF-LADDER — cto-2026-10-03.md R326
BRANCH: deploy/deploy-flake-fix-1006
WORKTREE: deploy-flake-fix-1006
BASE: main
TIP: f520debb
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-flake-fix-1006.md
RULINGS: 2026-10-03 R326, 2026-10-05 R412
TAG: deploy-2026-10-06-flake-fix
MIGRATIONS: none
SET: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/flake-fix-1006` | `f520debb` | `f520debb` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-check-2026-10-06.md` | `held unfixed: 0` and `ready: YES` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/flake-fix-1006`, 3 files, 383 insertions, 4 deletions), each with its RESTARTS class (the check's `uv run cobalt jobs restarts d1adf256..HEAD`; the check's line `RESTARTS: none`, no `UNCLASSIFIED` row): `tests/cobalt/test_drc_store.py` (test/documentation; no resident); `docs/40 - DevDocs/cobalt/drc/store.md` (the one DevDocs line BUILD-HUB E3 requires, plus the check's dated line; DOCS); `docs/40 - DevDocs/reports/flake-fix-build-2026-10-06.md` (the build report; DOCS). RESTARTS: none. A test-side fix: no `src/` path, no `ops/desk/` path, no `tests/cobalt/conftest.py` and no migration file is in the diff (the check's `## Checked against the branch` (iii) and (vi), each empty).

## MARKERS
- `grep -c -F "migration retry" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `8`
- `grep -c -F "conn = None" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `1` (check H2, H3: the attempt's connection starts unset, so the open sits inside the `try`)
- `grep -c -F "def test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `1`
- `grep -c -F "def test_the_migrated_fixture_fails_on_a_third_deadlock_after_two_retries" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `1`
- `grep -c -F "def test_the_migrated_fixture_does_not_retry_another_error" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `1`
- `grep -c -F "def test_the_migrated_fixture_retries_when_opening_the_first_attempt_deadlocks" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `1` (check H2)
- `grep -c -F "def test_the_migrated_fixture_closes_a_failed_attempt_when_rollback_fails" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · before `0` · after `1` (check H3)
- `grep -c -F "flake-fix" "/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/drc/store.md"` · before `0` · after `2`

## SMOKE READS
- retry test (F1) · `grep -c -F "def test_the_migrated_fixture_retries_once_when_the_first_migration_attempt_deadlocks" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · exit 0, a count of 1 or more
- open-deadlock test (H2) · `grep -c -F "def test_the_migrated_fixture_retries_when_opening_the_first_attempt_deadlocks" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · exit 0, a count of 1 or more
- rollback-failure test (H3) · `grep -c -F "def test_the_migrated_fixture_closes_a_failed_attempt_when_rollback_fails" /Users/cobalt/cobalt/tests/cobalt/test_drc_store.py` · exit 0, a count of 1 or more

## RECORDS
- flake-fix: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/flake-fix-check-2026-10-06.md` last line: CHECK DONE · job: flake-fix · pass: 2 · tip: f520debb · house B: Grok FINDINGS: 3 · findings: 3 · dropped: 0 · held: 3 · fixed: 0 · held unfixed: 0 · open: 0 · suites: offline 3932/0 · with-DB 886/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 135367
- flake-fix: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/flake-fix-1006` → `f520debb` (also the head of `git -C /Users/cobalt/cobalt log --oneline main..ops/flake-fix-1006`); code tip `f520debb` (the check's fix commit, H2 H3; its red tests are `814f56fd`); the job card's own TIP header reads `d1fee872` (the build tip); the build report commit `0ff56462` sits between them (docs only). Pass 1 house A was Sol, pass 2 house B was Grok. The gate on `f520debb` (pass 1, stands for pass 2): offline 3932/0, with-DB 886/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut. The fix here covers the `migrated` fixture of `tests/cobalt/test_drc_store.py` only.
- FOLLOW-UP for him, NOT part of this deploy: the build's DECISION W. The other tests that open `db.connect_migration` and run `_apply(conn, FORWARD)` themselves (`test_p4_migrations.py`, `test_voice_store.py`, `test_archiver_migrations.py`, `radar_migrated_support.py`, `test_drc_d2_fix_r1_db.py` and others) keep no retry; a card of their own if one deadlocks (job card `## NOT IN THIS JOB`).
- AFTER values above were read from the checked-out worktree `/Users/cobalt/cobalt-wt/flake-fix-1006` (HEAD `f520debb`, verified), BEFORE values from main's working tree, at drafting time 2026-10-06 02:38 EDT; the deploy re-proves each with `git -C /Users/cobalt/cobalt show f520debb:<path>`.
- Absent today: `git rev-parse --verify` of `deploy/deploy-flake-fix-1006` and of `deploy-2026-10-06-flake-fix` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-flake-fix-1006` and of the REPORT path both failed.
- one feature per deploy (his R390).
