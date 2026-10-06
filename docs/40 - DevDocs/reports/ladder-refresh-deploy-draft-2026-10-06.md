# ladder-refresh-deploy-draft — 2026-10-06

## §0 Headline
Deploy card for card 54 (radar ladder refresh, R556) is written: `prompts/2026-10-06/60-deploy-ladder-refresh-card.md`.
One SHIPS row, code tip = branch head = `ed19060f`, check `ready: YES`, `held unfixed: 0`. RESTARTS `com.cobalt.aset com.cobalt.radar`.
Branch, worktree, tag and report are all absent; main holds no copy of the build report. `«FILL` count 0.
One decision for the desk: the live `GET /radar` proof is no smoke read.

## CARD
- JOB: deploy-radar-ladder-refresh-1006 · LADDER: OFF-LADDER — reports/radar-screen-trace-2026-10-06.md 2026-10-06 R556
- BRANCH: deploy/deploy-radar-ladder-refresh-1006 · WORKTREE: deploy-radar-ladder-refresh-1006 · BASE: main · TIP: ed19060f
- REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-radar-ladder-refresh-1006.md
- RULINGS: 2026-10-06 R556 · TAG: deploy-2026-10-06-radar-ladder-refresh · MIGRATIONS: none · SET: none
- SHIPS: `ops/radar-ladder-refresh-1006`, stop line `held unfixed: 0` and `ready: YES`; 4 files, 483 insertions, 2 deletions.
- MARKERS / SMOKE READS: `tickLadder` 0→2, `window.setInterval(tickLadder,interval)` 0→1, `window.setInterval(refreshPool,interval)` 1→1.

## DECISIONS
- ASK DESK: the live proof (`logs/aset.log` shows `GET /radar` at the pool's interval from a loaded page) is not a smoke read the deploy hub can run: it needs his browser open after the restart, and a grep count would pass on his earlier single load. Default: left out of `## SMOKE READS`, named in the card's `## RECORDS` as a desk read after the deploy. [before the deploy launches, 10-06 evening]

## RECORDS
- Read: the prompt; `prompts/2026-10-06/45-deploy-card-39-card.md` and `34-deploy-guard-g2-card.md` (header, SHIPS, RECORDS wording); `54-radar-ladder-refresh-card.md`; the check report whole; the build report `## DECISIONS` and last line (worktree); `ops/desk/desk-launch.sh:788`–`:872` (`ships_checked`) and `:960`–`:1001` (deploy path). `prompts/CARD.md` was not opened beyond a section count (the two sibling cards set the format).
- `git -C /Users/cobalt/cobalt log --oneline -7 ops/radar-ladder-refresh-1006` → `ed19060f` at the head; `git diff --stat ed19060f ops/radar-ladder-refresh-1006 -- . ":(exclude)docs"` → nothing. `git rev-parse --short=8 ops/radar-ladder-refresh-1006` → `ed19060f`.
- `git diff --stat main...ops/radar-ladder-refresh-1006` → `radar_panel.md` 4, the build report 173, `radar_panel.py` 34, `test_radar_panel.py` 274; 4 files, 483 insertions, 2 deletions. The class strings come from the check's `jobs restarts` table.
- Absent: `git rev-parse --verify` of the deploy branch and of the tag, `ls` of the worktree, the REPORT and main's copy of the build report: all failed (exit 128 / 1).
- The check report is committed (`git log -1` → `02b15e1f`) and `git status` at session start lists it clean. The launcher accepts the stop line: each literal is read mid-line followed by a space (`desk-launch.sh:830`–`:834`), the check tip equals the code tip (`:858`).
- MARKERS: BEFORE by `grep -c -F` on main's `radar_panel.py` (`tickLadder` 0, the new timer 0, the `refreshPool` timer 1); AFTER by `git show ed19060f:src/cobalt/aset/radar_panel.py` read through the Grep tool on the saved output (`tickLadder` on lines 1578 and 1606, the pool timer 1), because a pipe is not on the allow line.
- Carried for him, in the card: the X29 setup error (UNPROVEN, `conftest.py:262`); the `post()` race, closed by the check's `sendGeneration` fix.
- One tool call (several `;` in one Bash) was refused by the bare-command hook; resent one per call. No new command was needed.

CARD 54 DEPLOY CARD DRAFTED · decisions: 1
