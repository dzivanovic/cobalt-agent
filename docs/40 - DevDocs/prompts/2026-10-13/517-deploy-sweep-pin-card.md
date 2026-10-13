JOB: sweep-pin-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1406, R1412
BRANCH: deploy/sweep-pin-1013
WORKTREE: deploy-sweep-pin-1013
BASE: main
TIP: e9bcace4
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-sweep-pin-1013.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-13-sweep-pin
MIGRATIONS: none
SET: radar
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/sweep-pin-1013` | `52cb2fc9` | `e9bcace4` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/sweep-pin-check-2026-10-13.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "f4-refresh-build-2026-10-10.md" /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` · before `1` · after `0`

## SMOKE READS
- the sweep pin is green on production main (desk reading: the deploy's point) · `uv run pytest -q tests/ops/test_the_rule_sweep.py` in `/Users/cobalt/cobalt` · green: `5 passed`, `0 failed`

## RECORDS
- sweep-pin-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/sweep-pin-check-2026-10-13.md` last line: CHECK DONE · job: sweep-pin-1013 · pass: 1 · tip: 52cb2fc9 · house A: grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 122315
- sweep-pin-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/sweep-pin-1013` → `e9bcace4`; code tip `52cb2fc9`
- written by deploy-card.sh at 2026-10-13 12:53 ET (`date`); trial merge of the heads onto main in order: clean
