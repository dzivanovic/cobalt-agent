JOB: deploy-radar-ladder-refresh-1006
LADDER: OFF-LADDER — reports/radar-screen-trace-2026-10-06.md 2026-10-06 R556
BRANCH: deploy/deploy-radar-ladder-refresh-1006
WORKTREE: deploy-radar-ladder-refresh-1006
BASE: main
TIP: ed19060f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-radar-ladder-refresh-1006.md
RULINGS: 2026-10-06 R556
TAG: deploy-2026-10-06-radar-ladder-refresh
MIGRATIONS: none
SET: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/radar-ladder-refresh-1006` | `ed19060f` | `ed19060f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-ladder-refresh-check-2026-10-06.md` | `held unfixed: 0` and `ready: YES` |

Card 54 (radar ladder refresh, his R556: the pool timer also refreshes the ladder through `tickLadder`). The check ended `held unfixed: 0 · open: 0 · ready: YES` at tip `ed19060f`, which is also the branch head and the code tip.

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/radar-ladder-refresh-1006`, 4 files, 483 insertions, 2 deletions), each with its RESTARTS class (the check's `uv run cobalt jobs restarts 8c554d77..HEAD`: four rows, no `UNCLASSIFIED`):
- `src/cobalt/aset/radar_panel.py` (`PANEL_JS` only: `tickLadder` and its timer line): class `static import reach` → `com.cobalt.aset,com.cobalt.radar`.
- `tests/cobalt/test_radar_panel.py` (test/documentation; no resident).
- `docs/40 - DevDocs/cobalt/aset/radar_panel.md` and `docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md` (DOCS).
RESTARTS: com.cobalt.aset com.cobalt.radar (the deploy restarts aset and radar, about 50 s down). No migration file, no `ops/` path in the diff. This deploy MUST land before the 10-07 09:30 ET open and alone (his R390).

## MARKERS
- `grep -c -F "tickLadder" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `2` (the function line and the timer line)
- `grep -c -F "window.setInterval(tickLadder,interval)" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `1`
- `grep -c -F "window.setInterval(refreshPool,interval)" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `1` · after `1` (unchanged)

## SMOKE READS
- the ladder tick function · `grep -c -F "tickLadder" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more
- the ladder timer line · `grep -c -F "window.setInterval(tickLadder,interval)" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more
- the pool timer line, unchanged · `grep -c -F "window.setInterval(refreshPool,interval)" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more

## RECORDS
- radar-ladder-refresh: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-ladder-refresh-check-2026-10-06.md` last line: CHECK DONE · job: radar-ladder-refresh · pass: 1 · tip: ed19060f · house A: Sol FINDINGS: 6 · findings: 12 · dropped: 0 · held: 11 · fixed: 11 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 3 · suites: offline 3963/0 · with-DB 4847/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181164
- radar-ladder-refresh: build report `/Users/cobalt/cobalt-wt/radar-ladder-refresh-1006/docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md` last line: BUILT · job: radar-ladder-refresh | tip: d2330003 | on 8c554d77 | migration: none | offline 3952/0 | with-DB 4836/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 172093
- Tips: build `d2330003`; ship `ed19060f` (the check's fix commit, also the code tip and the branch head; `git -C /Users/cobalt/cobalt log --oneline -7 ops/radar-ladder-refresh-1006` → `ed19060f`, `1e7fe5f2` check red tests, `94ef37fe` build report, `d2330003`, `7ba8880e`; `git diff --stat ed19060f ops/radar-ladder-refresh-1006 -- . ":(exclude)docs"` prints nothing). The gate on `ed19060f`: offline 3963/0, with-DB 4847/0, live-note 146/0, `cobalt_dev: 0013`, `.env: removed`. The launcher's deploy path reads the stop line's literals `held unfixed: 0` and `ready: YES` mid-line, each followed by a space (`ops/desk/desk-launch.sh:830`–`:834`), and the check tip equals the code tip (`:858`).
- The build report exists only in the worktree; main holds no copy (`ls` of `docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md` on main failed), so the deploy merge adds it with no add/add.
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- Autovacuum (R479): a `DeadlockDetected` in the gate is an autovacuum worker, not a second writer; rerun once via recut.
- The `post()` race the build report names (its DECISION 2: a `post()` that begins and ends inside one tick's fetch let the tick swap an older ladder) was closed by the check (O3 = A1 = B1, `sendGeneration`); carried here as a record only.
- FOLLOW-UP for him, NOT part of this deploy: the X29 control `tests/experiments/stale_score/test_x29_ladder_render.py` errors at setup (`fixture 'offline_skip_guard' not found`, `tests/cobalt/conftest.py:262`), UNPROVEN, a card of its own (the check's DECISION 1; the build touches neither file).
- FOLLOW-UP for the desk, NOT part of this deploy: the live proof (card 54 decision 4), `logs/aset.log` showing `GET /radar` at the pool's interval from a loaded page, is no smoke read: it needs his browser open after the restart, and a count taken before it would pass on his one earlier page load. No existing allowed command proves it at the deploy; the desk reads it after the deploy.
- AFTER values above were read from `git -C /Users/cobalt/cobalt show ed19060f:src/cobalt/aset/radar_panel.py` (`tickLadder` on lines 1578 and 1606, the `refreshPool` timer once), BEFORE values from main's working tree (`tickLadder` 0, the new timer 0, the `refreshPool` timer 1), at drafting time 2026-10-06; the deploy re-proves each with `git -C /Users/cobalt/cobalt show ed19060f:<path>`.
- Absent today: `git rev-parse --verify` of `deploy/deploy-radar-ladder-refresh-1006` and of `deploy-2026-10-06-radar-ladder-refresh` both failed; `ls` of `/Users/cobalt/cobalt-wt/deploy-radar-ladder-refresh-1006` and of the REPORT path both failed.
- one feature per deploy (his R390).
