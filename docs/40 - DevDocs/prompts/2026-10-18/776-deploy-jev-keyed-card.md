JOB: jev-keyed
LADDER: OFF-LADDER — reports/cto-2026-10-18.md R1830
BRANCH: deploy/jev-keyed
WORKTREE: deploy-jev-keyed
BASE: main
TIP: df6a000f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-jev-keyed.md
RULINGS: 2026-10-18 R1830
TAG: deploy-2026-10-18-jev-keyed
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `feat/jev-keyed-1018` | `9780e4eb` | `df6a000f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-keyed-check-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/ops/jev-route.sh` · before `No such file or directory` · after `/Users/cobalt/cobalt/ops/jev-route.sh`
- `grep -c -F "Bash(sh /Users/cobalt/cobalt/ops/jev-route.sh --day *)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md"` · before `0` · after `1`
- `grep -c -F "## 7b. JEV SHADOW BATCH" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md"` · before `0` · after `1`
- `grep -c -F "ops/jev-route.sh" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` · before `0` · after `1`

## SMOKE READS
- wrapper installed · `ls /Users/cobalt/cobalt/ops/jev-route.sh` · exit 0, listed
- restarts DevDoc section · `grep -c -F "jev-keyed-1018" "/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/jobs/restarts.md"` · exit 0, a count of 1 or more

## RECORDS
- jev-keyed-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-keyed-check-2026-10-18.md` last line: CHECK DONE · job: jev-keyed-1018 · pass: 1 · tip: 9780e4eb · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8514/0 · with-DB 5476/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 178753
- jev-keyed-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-keyed-1018` → `df6a000f`; code tip `9780e4eb`
- written by deploy-card.sh at 2026-10-18 10:01 ET (`date`); trial merge of the heads onto main in order: clean
