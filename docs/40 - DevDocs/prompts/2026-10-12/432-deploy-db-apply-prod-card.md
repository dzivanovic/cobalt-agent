JOB: db-apply-prod-1012
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1138
BRANCH: deploy/db-apply-prod-1012
WORKTREE: deploy-db-apply-prod-1012
BASE: main
TIP: fba1454e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-db-apply-prod-1012.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-db-apply-prod
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/db-apply-prod-1012` | `fba1454e` | `fba1454e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-apply-prod-check-2026-10-12.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "PARSER_PG_MAJOR" "/Users/cobalt/cobalt/src/cobalt/db_apply.py"` · before the file is absent · after count `1` or more (the verb's module)
- `grep -c -F -e "pglast" "/Users/cobalt/cobalt/pyproject.toml"` · before count `0` · after a count of `1` or more (the one new dependency)

## SMOKE READS
- The verb's module is on main · `grep -c -F -e "PARSER_PG_MAJOR" "/Users/cobalt/cobalt/src/cobalt/db_apply.py"` · prints 1 or more
- The dependency is on main · `grep -c -F -e "pglast" "/Users/cobalt/cobalt/pyproject.toml"` · prints 1 or more

## RECORDS
- db-apply-prod-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/db-apply-prod-check-2026-10-12.md` last line: CHECK DONE · job: db-apply-prod-1012 · pass: 1 · tip: fba1454e · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 4309/0 · with-DB 5212/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 290333
- db-apply-prod-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/db-apply-prod-1012` → `fba1454e`; code tip `fba1454e`
- written by deploy-card.sh at 2026-10-12 18:18 ET (`date`); trial merge of the heads onto main in order: clean
