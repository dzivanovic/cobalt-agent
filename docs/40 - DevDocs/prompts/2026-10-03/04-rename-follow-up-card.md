JOB: rename-follow-up
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R77
BRANCH: ops/rename-follow-up-1003
WORKTREE: rename-follow-up-1003
BASE: a09f0862
TIP:
REPORT: /Users/cobalt/cobalt-wt/rename-follow-up-1003/docs/40 - DevDocs/reports/rename-follow-up-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R77, 2026-10-02 R157

## ROWS

WHY: the check of card `15` (`reports/ops-glob-check-2026-10-02.md` O3) showed that `changes()` in `src/cobalt/jobs/restarts.py` does not emit the OLD path of a rename or copy line, so a plist that named the old path derives no restart. The judge ruled it a follow-up, not a hold (R77): the gap predates card `15`. The red is the O3 test kept verbatim in that report. One row.

| row | what | red first | files |
|---|---|---|---|
| O3 | `changes()` emits the old path of a `git diff --name-status` rename (`R<nn>\told\tnew`) or copy (`C<nn>\told\tnew`) line as a DELETE of the old path, beside the new path's ADD/MODIFY; every other line shape is unchanged. The RESTARTS derivation then classifies both paths as it does today | the O3 test of `reports/ops-glob-check-2026-10-02.md`, verbatim, in `tests/cobalt/test_jobs_restarts.py` (or the file O3 names): a rename of a classified path → the old path is in the change set as a delete. RED on `BASE`: the old path is absent | `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py` |

## NOT IN THIS JOB
- Any classification rule, glob or class home in `restarts.py`; `configs/cobalt/jobs.yaml`.
- Any other finding of the `15` check: all closed or held in their own places.

## READ
- `reports/ops-glob-check-2026-10-02.md` O3 (the test and the run that showed it).
- `src/cobalt/jobs/restarts.py` `changes()` and its callers; `tests/cobalt/test_jobs_restarts.py`.

## CHECK ASKS
- X1 Does a rename whose old and new paths fall in different classes derive BOTH restarts? Write the test.
- X2 Is any caller of `changes()` fed a shape (`--name-only`, a porcelain line) the new parsing misreads?

## RECORDS
- Judge answer, 10:0x ET 10-02 (R77): follow-up, not a fix before the 10-02 deploy; `reports/brain-direction-2026-10-02.md` `## TOMORROW` row "rename follow-up".
- This job touches `src/`: it takes the lock as `BUILD-HUB.md` says (pass 1 with `--db-only` after card `01`). The restart set is derived by the build (L42); `restarts.py` itself is in a class — the RESTARTS line says which.
