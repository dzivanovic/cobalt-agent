JOB: close-timer
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/close-timer-1003
WORKTREE: close-timer-1003
BASE: a09f0862
TIP:
REPORT: /Users/cobalt/cobalt-wt/close-timer-1003/docs/40 - DevDocs/reports/close-timer-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-02 R157, 2026-10-02 R44

## ROWS

WHY: four nights (09-28 … 10-01) ended with no close because the desk's context or his evening ended first; NOW sat at four times its cap. His ruling (direction row 7): the close is started by a timer. `reports/brain-unattended-2026-10-02.md` E 10: a launchd job starts `desk-launch.sh close <date>` at 21:05 ET and hourly while a deploy hub is live. His install loads the plist; this card builds and tests it and registers it so RESTARTS knows it.

| row | what | red first | files |
|---|---|---|---|
| T1 | `ops/desk/close-timer.sh`: run by launchd; computes `<date>` (ET, by `TZ=America/New_York date +%F`); refuses when `desk-launch.sh` is absent; when a deploy hub is live (a `deploy-hub-*` session in `desk-list.sh`'s output, read by `desk-context.sh` or directly) it prints `DEFERRED: deploy live — <name>` and exits 0 (launchd fires again on the hour); THE DATE is the EVENING's: before 04:00 ET the timer's `<date>` is yesterday's ET date, else today's. When `reports/close-<date>.md` already ends in its stop line → `DONE ALREADY`, exit 0, no launcher call (so the 00:05–03:05 fires after a finished close launch nothing and log one line each); otherwise it runs `sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh close <date>` once and logs its output to `$WT/.timer-logs/close-<date>.log`. `export LC_ALL=C` first | `tests/ops/test_close_timer.py`: stubs for `desk-launch.sh` and `desk-list.sh` on a tmp root record calls: a free evening → one `close <date>` call; a live deploy hub → `DEFERRED`, no call; a finished close report → `DONE ALREADY`, no call; a missing launcher → `REFUSED`; a fire at 01:05 ET with yesterday's close done → `DONE ALREADY`, no call; at 01:05 with yesterday's close absent → `close <yesterday>`. RED on `BASE`: no such file | `ops/desk/close-timer.sh`, `tests/ops/test_close_timer.py` |
| T2 | The plist `ops/desk/com.cobalt.close-timer.plist`: `StartCalendarInterval` at 21:05 and every hour from 22:05 to 03:05 ET (launchd uses the Mac's local clock; the hours are listed, one dict each), `ProgramArguments` = `sh /Users/cobalt/cobalt/ops/desk/close-timer.sh`, `StandardOutPath` / `StandardErrorPath` under `/Users/cobalt/cobalt-wt/.timer-logs/`, `RunAtLoad` false. No registry row: the timer is an operator job under `restarts.py`'s `OPS_DESK_PREFIX` rule (both files), never heartbeat-probed, never restarted by a deploy | `tests/ops/test_close_timer.py`: `plutil -lint` is not on the list, so the test parses the plist with `plistlib` and asserts the label, the seven calendar entries, the program line and the log paths; `tests/ops/test_close_timer.py` asserts, through `restarts.py`'s classifier called on the two paths, that both class as operator script, no reader. RED on `BASE`: no plist | `ops/desk/com.cobalt.close-timer.plist`, `tests/ops/test_close_timer.py` |
| T3 | HIS INSTALL TEXT, in `## RECORDS` of the build report and in `ops/desk/close-timer.sh`'s header: first line `mkdir -p /Users/cobalt/cobalt-wt/.timer-logs` (the header says launchd's own log paths need the folder before the first fire); then the two commands he types once (`cp` of the plist into `~/Library/LaunchAgents/`, `launchctl bootstrap gui/$(id -u) <path>`) and the one read that proves it (`launchctl print gui/$(id -u)/com.cobalt.close-timer` → the next fire time). RUN — asserts nothing: quote the header | — | `ops/desk/close-timer.sh` (header only) |

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
- X2 is answered by row T1 as amended (the evening's date before 04:00 ET). Build it so; the check reads the test.
- FOR THE CHECK: Build decisions 1–5 answered by the judge: D1 KEEP (no registry row; the OPS_DESK_PREFIX rule classes the timer); D2 and D4 fixed by rows T1 and T3 amended (the evening's date before 04:00; mkdir of the log folder in his install); D3, D5 KEEP.
- `desk-list.sh` dependency: `desk-context.sh --guard` on `main` reads it; whichever copy is beside the script at `BASE` is the one T1 uses.
