JOB: deploy-guard-g2-1006
LADDER: OFF-LADDER — cto-2026-10-06.md R511
BRANCH: deploy/deploy-guard-g2-1006
WORKTREE: deploy-guard-g2-1006
BASE: main
TIP: 19f75dc6
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-guard-g2-1006.md
RULINGS: 2026-10-06 R511, 2026-10-05 R412, 2026-10-05 R474
TAG: deploy-2026-10-06-guard-g2
MIGRATIONS: none
SET: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/guard-g2-1006` | `19f75dc6` | `19f75dc6` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-check-2026-10-06.md` | `held unfixed: 0` and `ready: YES` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/guard-g2-1006`, 5 files, 624 insertions, 3 deletions), each with its RESTARTS class (the check's `uv run cobalt jobs restarts 3c257bb9..HEAD`: the five paths `DOCS` / `operator script; no Cobalt reader` / `test/documentation; no resident`; the check's line `RESTARTS: none`):
- `ops/desk/bare-guard.py` (G2 passes a launcher-stamped seat's one production `db query`: `marked_read`, `MARKER`, the `"first"` key of `seat()`; operator script; no Cobalt reader) and `ops/desk/desk-launch.sh` (R1: the prompt kind stamps ` PROD-READ: <date> R<n>` for a proven row and refuses a typed one; operator script; no Cobalt reader).
- `tests/ops/test_bare_guard.py` and `tests/ops/test_desk_launch_prechecks.py` (test/documentation; no resident).
- `docs/40 - DevDocs/reports/guard-g2-build-2026-10-06.md` (the build report; DOCS).
RESTARTS: none. No `src/` path, no migration file and no DevDocs module page is in the diff (the check: `bare-guard.py` and `desk-launch.sh` have no page under `docs/40 - DevDocs/cobalt/`; its `## Checked against the branch` (iii) and (vi), each empty).

## MARKERS
- `grep -c -F "def marked_read(command, s)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1`
- `grep -c -F "MARKER = re.compile" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1`
- `grep -c -F "and not marked_read(command, s)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1` (the G2 row at `bash_rules`)
- `grep -c -F "PROD-READ:" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `8` (R1 stamp and refusal)
- `grep -c -F "production reads?([^[:alpha:]]|\$)" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1` (check A1, B4: the row must name a production read as words)
- `grep -c -F "MARKED_KINDS" /Users/cobalt/cobalt/tests/ops/test_bare_guard.py` · before `0` · after `3`
- `grep -c -F "def test_g2_a_marked_seat_is_denied_a_production_word_in_a_brace_word" /Users/cobalt/cobalt/tests/ops/test_bare_guard.py` · before `0` · after `1` (check O3)
- `grep -c -F "def test_r1_a_disapproved_row_stamps_nothing" /Users/cobalt/cobalt/tests/ops/test_desk_launch_prechecks.py` · before `0` · after `1` (check A1)

## SMOKE READS
- the G2 pass (R2) · `grep -c -F "def marked_read(command, s)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more
- the G2 row in the rule · `grep -c -F "and not marked_read(command, s)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more
- the launcher stamp (R1) · `grep -c -F "PROD-READ:" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more
- the check's A1 fix · `grep -c -F "production reads?([^[:alpha:]]|\$)" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more

## RECORDS
- guard-g2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-check-2026-10-06.md` last line: CHECK DONE · job: guard-g2 · pass: 1 · tip: 19f75dc6 · house A: Sol FINDINGS: 5 · findings: 15 · dropped: 0 · held: 11 · fixed: 11 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 5 · suites: offline 3932/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 216430
- guard-g2: head `git -C /Users/cobalt/cobalt log --oneline -4 ops/guard-g2-1006` → `19f75dc6` (the check's fix commit, also the code tip), `5093b1ca` (check red tests), `61999cc5` (build report, docs only), `ce19a3fd` (the build tip, the job card's own TIP header); BASE of the job card `3c257bb9`. House A was Sol, house B was Grok. The gate on `19f75dc6`: offline 3932/0, live-note 146/0, tests/ops 1462 passed (1 xfailed), with-DB not run (`DB: none`), `cobalt_dev: not taken`, `.env: removed`.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut.
- Where the files reach the desk (read at drafting): `/Users/cobalt/.claude/ops/desk-launch.sh` and `/Users/cobalt/.claude/ops/bare-guard.py` are symlinks into `/Users/cobalt/cobalt/ops/desk/` (`ls -la /Users/cobalt/.claude/ops/`), and the hook entry runs the repo copy; both take effect when the deploy merges to main. `ops/desk/install-fixed.sh` installs a prompt-title token (`«INSTALL`) and copies no desk script, so the deploy hub does not run it; it is an existing script but `DEPLOY-HUB.md` does not name it (`grep -n -F "install-fixed"` → nothing). No new command.
- FOLLOW-UP for him, NOT part of this deploy: the check's `## OPEN`. A3: CONTROL (b) as typed cannot go red under the leading-shape mutation (the build's `db migrate --prod` case carries it). A4: CONTROL (e) is red on BASE on its G1 deny text only. B3: a marked `db query … "DELETE FROM t"` passes the guard (R2(ii) reads no SQL; `guard_select` and `BEGIN READ ONLY` in `src/cobalt/db_query.py` refuse it at run time); the desk rules whether "a write verb" covers SQL text.
- FOLLOW-UP for him, NOT part of this deploy: the check's DECISIONS 3 and 4. (3) `ruling_row` (`ops/desk/desk-launch.sh`, `*"HIS RULING"*APPROVED*`) also accepts a `DISAPPROVED` status for every kind that calls it; only the prompt stamp was fixed. (4) UNPROVEN: the `desk` kind launches the wake-up file's typed line with no `PROD-READ:` test while the guard counts a marked desk seat (`MARKED_KINDS`). Each is a card of its own.
- R511 on main reads `APPROVED — pending fold` (`reports/cto-2026-10-06.md` line 38 at drafting; the line number moves). R412 reads `APPROVED (in cto-desk-contract.md …)` and R474 reads `HIS RULING · APPROVED` (`reports/cto-2026-10-05.md` lines 109, 140).
- AFTER values above were read from the checked-out worktree `/Users/cobalt/cobalt-wt/guard-g2-1006` (the branch `ops/guard-g2-1006`, head `19f75dc6` verified by `rev-parse`), BEFORE values from main's working tree, at drafting time 2026-10-06 08:39 EDT; the deploy re-proves each with `git -C /Users/cobalt/cobalt show 19f75dc6:<path>`.
- Absent today: `git rev-parse --verify` of `deploy/deploy-guard-g2-1006` and of `deploy-2026-10-06-guard-g2` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-guard-g2-1006` and of the REPORT path both failed.
- one feature per deploy (his R390).
