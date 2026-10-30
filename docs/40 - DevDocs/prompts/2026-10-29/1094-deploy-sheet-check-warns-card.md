JOB: sheet-check-warns
LADDER: OFF-LADDER — reports/cto-2026-10-29.md R2563
BRANCH: deploy/sheet-check-warns
WORKTREE: deploy-sheet-check-warns
BASE: main
TIP: e43330f5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-sheet-check-warns.md
RULINGS: 2026-10-29 R2563
TAG: deploy-2026-10-29-sheet-check-warns
MIGRATIONS: none
SET: sheet-check-warns
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/sheet-check-warns` | `3a0b4ed3` | `e43330f5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/sheet-check-warns-check-2026-10-29.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/sheet-check-warns-build-2026-10-29.md` |

## MARKERS
- `grep -c -F "def sheet_warning(" /Users/cobalt/cobalt/src/cobalt/daymode/match.py` · before `0` · after `1`
- `grep -c -F "def assert_sheet_matches(" /Users/cobalt/cobalt/src/cobalt/daymode/match.py` · before `1` · after `0`
- `grep -c -F "assert_sheet_matches(" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `3` · after `0`

## SMOKE READS
- the match module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/daymode/match.py` · exit 0, listed
- the web module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, listed

## RECORDS
- sheet-check-warns: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/sheet-check-warns-build-2026-10-29.md` at `e43330f5` last line: BUILT · job: sheet-check-warns · tip: 3a0b4ed3 | on 78a6ab4a | migration: none | offline 5042/0 | with-DB 6014/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 8 of 8 | self-check: 2 of 3 | decisions: 4 · for Dejan: 0 · tokens: 95048
- sheet-check-warns: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/sheet-check-warns-check-2026-10-29.md` last line: CHECK DONE · job: sheet-check-warns · pass: 1 · tip: d57714468 · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 3 · fixed: 2 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 9178/0 · with-DB 6014/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: NO · decisions: 1 · for Dejan: 0 · tokens: 174160
- sheet-check-warns: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/sheet-check-warns` → `e43330f5`; code tip `3a0b4ed3`
- written by deploy-card.sh at 2026-10-29 20:56 ET (`date`); trial merge of the heads onto main in order: clean
