JOB: guard-g2-open-reads-1008
LADDER: OFF-LADDER — reports/cto-2026-10-08.md R686
BRANCH: deploy/guard-g2-open-reads-1008
WORKTREE: deploy-guard-g2-open-reads-1008
BASE: main
TIP: 828f28dc
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-guard-g2-open-reads-1008.md
RULINGS: 2026-10-08 R686
TAG: deploy-2026-10-08-guard-g2-open-reads
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/guard-g2-open-reads-1008` | `828f28dc` | `828f28dc` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-open-reads-check-2026-10-08.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "def prod_read(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1` (O1, the production read for every seat)
- `grep -c -F "def keychain_read(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1` (O2, secrets beside .env)

## SMOKE READS
- production read function present · `grep -c -F "def prod_read(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more
- secret guard present · `grep -c -F "def is_secret(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more

## RECORDS
- guard-g2-open-reads-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-open-reads-check-2026-10-08.md` last line: CHECK DONE · job: guard-g2-open-reads-1008 · pass: 1 · tip: 828f28dc · house A: Sol FINDINGS: 4 · findings: 11 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 3 · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 227244
- guard-g2-open-reads-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-g2-open-reads-1008` → `828f28dc`; code tip `828f28dc`
- RESTARTS: none. Every path is under `ops/` or `tests/ops/` (the check's stop line: `RESTARTS: none`). No `src/` path, no migration, no resident.
- written by deploy-card.sh at 2026-10-08 12:51 ET (`date`); trial merge of the heads onto main in order: clean
