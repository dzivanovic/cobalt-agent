JOB: runner
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/runner-1003
WORKTREE: runner-1003
BASE: «FILL: card 02 adoption-hubs' BUILT tip (the runner drives the adopted hub files)»
TIP:
REPORT: /Users/cobalt/cobalt-wt/runner-1003/docs/40 - DevDocs/reports/runner-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R157

## ROWS

WHY: between a build's BUILT line and its check's `ready: YES` the desk today makes about 25 turns (verify, fill, commit, launch, watch, tab) and the silent gaps cost up to 7 h 12 min (10-01). `reports/brain-unattended-2026-10-02.md` E 21 and `## THE STANDARD` 5: `job-run.sh <card>` is a SHELL runner, not a model, that chains build → verify → card fill → check → pass 2 → `READY`, through `desk-launch.sh`, and wakes the desk only on `FAILED`, `for Dejan > 0` or `READY`. It is tried on ONE real card at the end of the build, by the desk, not by the builder. Every script here is POSIX `sh`, `export LC_ALL=C` first, tested with stubs in `tests/ops/`.

| row | what | red first | files |
|---|---|---|---|
| J1 | `ops/desk/job-run.sh "<card>"`: detached (`nohup`, its own log `$WT/.job-logs/<job>.log`), one STATE FILE `$WT/.job-state/<job>` holding one word of `BUILDING · BUILT · CHECKING · PASS-2 · READY · FAILED · FOR-DEJAN` and the last stop line. Steps, each by the scripts on `main`: `desk-launch.sh build "<card>"` → `desk-watch.sh build "<card>"` (stop line) → on `BUILT`: `card-fill.sh "<card>"` (TIP, CHECK REPORT, HOUSE B) → `desk-launch.sh check "<card>"` → `desk-watch.sh check` → on `ready: YES` with `open: 0`: `READY`; with `open > 0` and a house B up: `desk-launch.sh check "<card>" PASS-2` → watch → `READY` or `FAILED`. A stop line with `for Dejan: <n>`, n > 0 → state `FOR-DEJAN`, stop. A stop line `decisions: <n>`, n > 0, for Dejan 0 → state `DECISIONS`, stop (the judge seat answers; the desk resumes with `job-run.sh "<card>" --from <step>`). `FAILED` anywhere → state `FAILED` with the line, stop. It never sends CONTINUE, never edits a card but through `card-fill.sh`, never commits but through `desk-commit.sh`, never stops or removes a session (the desk's `desk-done.sh`) | `tests/ops/test_job_run.py`: stubs for `desk-launch.sh`, `desk-watch.sh`, `card-fill.sh`, `desk-commit.sh` on a tmp root, each answering from a per-test script: a clean run → the call order above and `READY`; a build `FAILED` → state `FAILED`, no check launched; `decisions: 1 · for Dejan: 0` → `DECISIONS`, stop; `for Dejan: 1` → `FOR-DEJAN`; `open: 2` with house B up → a `PASS-2` launch; `--from check` resumes without a second build. RED on `BASE`: no such file | `ops/desk/job-run.sh`, `tests/ops/test_job_run.py` |
| J2 | THE WAKE. On each stop the runner appends one line to `$WT/.job-state/WAKE` (`<time> <job> <state> <stop line>`) and, when `desk-wake.sh` (card `18`) exists beside it, calls it with that line; the desk's wake-up reads `WAKE` first. No other channel (no message to a session from a script: a session is reached only by the desk) | in `tests/ops/test_job_run.py`: the `WAKE` line per stop; the `desk-wake.sh` stub called once per stop with the line; absent stub → the file line only. RED on `BASE`: no file | `ops/desk/job-run.sh`, `tests/ops/test_job_run.py` |
| J3 | `desk-launch.sh run "<card>"`: the kind that starts J1 detached and prints the state-file path and the log path; `desk-launch.sh run "<card>" --status` prints the state file. Refuses a card already in a non-final state. The launcher's header comment lists the kind | `tests/ops/test_desk_launch_run.py`, `DESK_LAUNCH_DRY=1`: the kind prints the detached command and the paths; `--status` prints the state; a running state → `REFUSED`. RED on `BASE`: `REFUSED: kind 'run' is none of …` | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_run.py` |

## NOT IN THIS JOB
- Any hub file; `STANDING-LIST.md` (the runner is the desk's tool: it runs under the desk's allow, which already carries `sh /Users/cobalt/cobalt/ops/desk/*` after card `02`'s lines, or his settings' class string).
- The deploy (`deploy-card.sh`, `DEPLOY-HUB.md`); the runner ends at `READY`.
- A model anywhere in the runner; a message to a session; a CONTINUE.
- The trial on a real card: the desk's, after the check (a `## RECORDS` line of the desk, not a row here).

## READ
- `reports/brain-unattended-2026-10-02.md` E 21, E 8, E 15, E 17, E 18, E 23; `## THE STANDARD` 5, 10; A 2.
- `ops/desk/desk-launch.sh` (every kind's `case`, `run_launch`), `desk-watch.sh`, `card-fill.sh`, `desk-commit.sh`, `desk-row.sh`, `desk-wake.sh`, `desk-done.sh` at `BASE`: their header comments are their contracts.
- `docs/40 - DevDocs/prompts/BUILD-HUB.md` `## STOP LINE` and `CHECK-HUB.md`'s stop line: the fields the runner parses (`decisions:`, `for Dejan:`, `ready:`, `open:`, `tip:`).

## CHECK ASKS
- X1 Can the runner launch a check on a build whose stop line it misread (a `FAILED` line containing the word `BUILT`, a report with two candidate last lines)? Write the test.
- X2 Can two runners run one card at once? Can a runner outlive the desk's `desk-done.sh` of its session and act on a removed session?
- X3 Does every stop of the runner leave a `WAKE` line the wake-up can act on with no other read?

## RECORDS
- `DB: none`: every file is under `ops/` or `tests/ops/`.
- The runner's first real trial: the desk runs `desk-launch.sh run` on the LAST card of 10-03 that is still to build (the desk picks it and records which); its stop lines are the trial's proof.
- Base: card `02`'s BUILT tip, because the runner's steps are the adopted hub files' steps; it ships in the same set as `02` and `03`.
