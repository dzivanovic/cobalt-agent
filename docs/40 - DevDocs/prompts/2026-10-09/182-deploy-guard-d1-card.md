JOB: guard-d1-1009
LADDER: OFF-LADDER — reports/cto-2026-10-08.md 2026-10-08 R707
BRANCH: deploy/guard-d1-1009
WORKTREE: deploy-guard-d1-1009
BASE: main
TIP: e9655b19
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-guard-d1-1009.md
RULINGS: 2026-10-08 R686
TAG: deploy-2026-10-09-guard-d1
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/guard-d1-1009` | `e9655b19` | `e9655b19` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d1-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "PROD_OPTION" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `3` (the option-word pattern for a production flag)
- `grep -c -F "def prod_word" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1` (the production-word test on the words bash runs)

## SMOKE READS
- the option-word pattern in the guard · `grep -c -F "PROD_OPTION" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more
- the production-word test in the guard · `grep -c -F "def prod_word" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more

## RECORDS
- guard-d1-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d1-check-2026-10-09.md` last line: CHECK DONE · job: guard-d1-1009 · pass: 1 · tip: e9655b19 · house A: Sol FINDINGS: 9 · findings: 15 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 4 · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 215804
- guard-d1-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-d1-1009` → `e9655b19`; code tip `e9655b19`
- written by deploy-card.sh at 2026-10-09 15:17 ET (`date`); trial merge of the heads onto main in order: clean
