JOB: f5-x3-values
LADDER: OFF-LADDER — reports/cto-2026-10-20.md R2217
BRANCH: deploy/f5-x3-values
WORKTREE: deploy-f5-x3-values
BASE: main
TIP: 3680824c
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f5-x3-values.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-f5-x3-values
MIGRATIONS: none
SET: f5-x3-values
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f5-x3-values` | `e9245a8e` | `3680824c` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-values-check-2026-10-20.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "source: UNMEASURED" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `2` · after `0`
- `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `2`
- `grep -c -F "(warm model)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1`
- `grep -c -F "cold load 8.67 s from the mainframe log (proxy, not a live cold call)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1`

## SMOKE READS
- checkpoint plists stay on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` · exit 0, listed

## RECORDS
- f5-x3-values: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-values-check-2026-10-20.md` last line: CHECK DONE · job: f5-x3-values · pass: 1 · tip: e9245a8e · house A: Grok FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8971/0 · with-DB 5870/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 153731
- f5-x3-values: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-x3-values` → `3680824c`; code tip `e9245a8e`
- written by deploy-card.sh at 2026-10-21 00:11 ET (`date`); trial merge of the heads onto main in order: clean
