JOB: plist-step-c-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1374
BRANCH: deploy/plist-step-c-1013
WORKTREE: deploy-plist-step-c-1013
BASE: main
TIP: 6b2dabd5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-plist-step-c-1013.md
RULINGS: 2026-10-13 R1341
TAG: deploy-2026-10-13-plist-step-c
MIGRATIONS: none
SET: radar
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/plist-step-c-1013` | `c1fc230d` | `6b2dabd5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/plist-step-c-check-2026-10-13.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md` |

## MARKERS
- `ls /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh` · before `No such file or directory` · after the path printed
- `grep -c -F "bootstrap-owed.json" /Users/cobalt/cobalt/ops/desk/deploy-step-c.sh` · before `No such file` · after `3`
- `grep -c -F "bootstrap-owed.json" /Users/cobalt/cobalt/src/cobalt/smoke/checks.py` · before `0` · after `1`

## SMOKE READS
- `COBALT_ENV=production uv run cobalt smoke s2` → K18 PASS, and no `OWED` line (no label is deferred yet, so the new path is inert)
- `launchctl print gui/501/com.cobalt.radar` → `state = running` after the radar restart (use the uid that `id -u` prints if it is not 501)

## RECORDS
- plist-step-c-1013: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/plist-step-c-build-2026-10-13.md` at `6b2dabd5` last line: BUILT · job: plist-step-c-1013 · tip: c1fc230d | on 5214e50b | migration: none | offline 4328/0 | with-DB 5231/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 14 of 14 | self-check: 3 of 3 | decisions: 6 · for Dejan: 0 · tokens: 179297
- plist-step-c-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/plist-step-c-check-2026-10-13.md` last line: CHECK DONE · job: plist-step-c-1013 · pass: 1 · tip: 6c3402af · house A: Grok FINDINGS: 7 · findings: 10 · dropped: 0 · held: 6 · fixed: 6 · held unfixed: 0 · open: 4 · house B: none available · suites: offline 4327/0 · with-DB 5230/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 255726
- plist-step-c-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/plist-step-c-1013` → `6b2dabd5`; code tip `c1fc230d`
- written by deploy-card.sh at 2026-10-13 21:04 ET (`date`); trial merge of the heads onto main in order: clean
