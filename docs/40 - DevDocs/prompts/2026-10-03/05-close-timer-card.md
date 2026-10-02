JOB: close-timer
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/close-timer-1003
WORKTREE: close-timer-1003
BASE: «FILL: the 8-hex head of main after card 01 lock-relief is DEPLOYED»
TIP:
REPORT: /Users/cobalt/cobalt-wt/close-timer-1003/docs/40 - DevDocs/reports/close-timer-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R157, 2026-10-02 R44

## ROWS

WHY: four nights (09-28 … 10-01) ended with no close because the desk's context or his evening ended first; NOW sat at four times its cap. His ruling (direction row 7): the close is started by a timer. `reports/brain-unattended-2026-10-02.md` E 10: a launchd job starts `desk-launch.sh close <date>` at 21:05 ET and hourly while a deploy hub is live. His install loads the plist; this card builds and tests it and registers it so RESTARTS knows it.

| row | what | red first | files |
|---|---|---|---|
| T1 | `ops/desk/close-timer.sh`: run by launchd; computes `<date>` (ET, by `TZ=America/New_York date +%F`); refuses when `desk-launch.sh` is absent; when a deploy hub is live (a `deploy-hub-*` session in `desk-list.sh`'s output, read by `desk-context.sh` or directly) it prints `DEFERRED: deploy live — <name>` and exits 0 (launchd fires again on the hour); when today's close report `reports/close-<date>.md` already ends in its stop line it prints `DONE ALREADY` and exits 0; otherwise it runs `sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh close <date>` once and logs its output to `$WT/.timer-logs/close-<date>.log`. `export LC_ALL=C` first | `tests/ops/test_close_timer.py`: stubs for `desk-launch.sh` and `desk-list.sh` on a tmp root record calls: a free evening → one `close <date>` call; a live deploy hub → `DEFERRED`, no call; a finished close report → `DONE ALREADY`, no call; a missing launcher → `REFUSED`. RED on `BASE`: no such file | `ops/desk/close-timer.sh`, `tests/ops/test_close_timer.py` |
| T2 | The plist `ops/desk/com.cobalt.close-timer.plist`: `StartCalendarInterval` at 21:05 and every hour from 22:05 to 03:05 ET (launchd uses the Mac's local clock; the hours are listed, one dict each), `ProgramArguments` = `sh /Users/cobalt/cobalt/ops/desk/close-timer.sh`, `StandardOutPath` / `StandardErrorPath` under `/Users/cobalt/cobalt-wt/.timer-logs/`, `RunAtLoad` false. The jobs registry `configs/cobalt/jobs.yaml` gains the label `com.cobalt.close-timer` in the class that restarts nothing (an operator timer, no Cobalt reader; the class name as `restarts.py` has it) | `tests/ops/test_close_timer.py`: `plutil -lint` is not on the list, so the test parses the plist with `plistlib` and asserts the label, the seven calendar entries, the program line and the log paths; `tests/cobalt/test_jobs.py` (or the registry test that exists) asserts the label is registered and its class derives no restart. RED on `BASE`: no plist, no label | `ops/desk/com.cobalt.close-timer.plist`, `configs/cobalt/jobs.yaml`, `tests/ops/test_close_timer.py`, the registry test |
| T3 | HIS INSTALL TEXT, in `## RECORDS` of the build report and in `ops/desk/close-timer.sh`'s header: the two commands he types once (`cp` of the plist into `~/Library/LaunchAgents/`, `launchctl bootstrap gui/$(id -u) <path>`) and the one read that proves it (`launchctl print gui/$(id -u)/com.cobalt.close-timer` → the next fire time). RUN — asserts nothing: quote the header | — | `ops/desk/close-timer.sh` (header only) |

## NOT IN THIS JOB
- Loading the plist, any `launchctl`, any write under `~/Library`: his install.
- `desk-launch.sh close`, `CLOSE-HUB.md`: the close itself stands as built.
- A timer for anything else (the day-open, the wake-up).

## READ
- `reports/brain-unattended-2026-10-02.md` E 10, D 10.
- `ops/desk/desk-launch.sh` the `close` kind; `ops/desk/desk-context.sh`; `ops/desk/desk-list.sh` (tracked by card `03`; if `BASE` does not carry it yet, read `/Users/cobalt/.claude/ops/desk-list.sh` is NOT yours — the desk copies its text into this card's `## RECORDS`).
- `configs/cobalt/jobs.yaml` and `src/cobalt/jobs/restarts.py` (the registry's shape and the class with no reader); `tests/cobalt/test_jobs.py`.
- An existing plist of the project for the shape (`ls` under `ops/` or `configs/`; the prefill job's plist `com.cobalt.prefill-daily` is the precedent named in NOW).

## CHECK ASKS
- X1 With a deploy hub live at 21:05 and gone at 23:40: exactly one close launched that night? With the close already done by hand: none?
- X2 Does the timer ever run `close` for a date other than the ET date at fire time (after midnight ET it is the next date: is that the close his ruling wants, or the evening's? Name what the script does and why).
- X3 Is the label registered so the RESTARTS derivation neither restarts it nor flags it UNCLASSIFIED?

## RECORDS
- This job touches `configs/`: it takes the lock as `BUILD-HUB.md` says (not `DB: none`).
- X2 is answered by the card: the close of `<date>` is the evening's date; a fire after midnight ET uses the PREVIOUS date when `reports/close-<previous date>.md` does not yet end in its stop line, else today's. Build it so; the check reads the test.
- `desk-list.sh` dependency: `desk-context.sh --guard` on `main` reads it; whichever copy is beside the script at `BASE` is the one T1 uses.
