JOB: checkin-install
LADDER: OFF-LADDER — reports/cto-2026-10-18.md R1854
BRANCH: deploy/checkin-install
WORKTREE: deploy-checkin-install
BASE: main
TIP: 964ba1b5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-checkin-install.md
RULINGS: 2026-10-18 R1841, 2026-10-18 R1854
TAG: deploy-2026-10-18-checkin-install
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/checkin-install-1018` | `964ba1b5` | `964ba1b5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/checkin-install-check-r2-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "checkin-timer.sh" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `0` · after `1`
- `grep -c -F "MVP FIRST" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `0` · after `1`
- `grep -c -F "## CHECK-IN" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BRAIN-HUB.md"` · before `0` · after `1`
- `grep -c -F "## 10. THE CHECK-IN TIMER" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md"` · before `0` · after `1`

## SMOKE READS
- timer script · `ls /Users/cobalt/cobalt/ops/desk/checkin-timer.sh` · exit 0, listed
- timer plist · `ls /Users/cobalt/cobalt/ops/desk/com.cobalt.checkin-timer.plist` · exit 0, listed
- ping prompt · `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECKIN-PING.md"` · exit 0, listed
- ping in the timer · `grep -c -F "CHECKIN-PING.md" /Users/cobalt/cobalt/ops/desk/checkin-timer.sh` · exit 0, a count of 1 or more

## RECORDS
- checkin-install-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/checkin-install-check-r2-2026-10-18.md` last line: CHECK DONE · job: checkin-install-1018 · pass: 1 · tip: 964ba1b5 · house A: Grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8516/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 203412
- checkin-install-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/checkin-install-1018` → `964ba1b5`; code tip `964ba1b5`
- written by deploy-card.sh at 2026-10-18 16:26 ET (`date`); trial merge of the heads onto main in order: clean
