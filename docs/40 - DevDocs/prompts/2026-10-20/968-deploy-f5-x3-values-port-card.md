JOB: f5-x3-values-port
LADDER: OFF-LADDER — reports/cto-2026-10-20.md R2217
BRANCH: deploy/f5-x3-values-port
WORKTREE: deploy-f5-x3-values-port
BASE: main
TIP: 2672dd43
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f5-x3-values-port.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-f5-x3-values-port
MIGRATIONS: none
SET: f5-x3-values-port
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f5-x3-values-port` | `fc2ffb3b` | `2672dd43` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-values-port-check-2026-10-21.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "source: UNMEASURED" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `2` · after `0`
- `grep -c -F "# source: X3 reports/f5-x3-measure-2026-10-20.md" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `2`
- `grep -c -F "(warm model)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1`
- `grep -c -F "cold load 8.67 s from the mainframe log (proxy, not a live cold call)" "/Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml"` · before `0` · after `1`

## SMOKE READS
- the sheet answers after the aset restart · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` · exit 0, `200`
- checkpoint plists stay on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` · exit 0, listed

## RECORDS
- f5-x3-values-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-x3-values-port-check-2026-10-21.md` last line: CHECK DONE · job: f5-x3-values-port · pass: 1 · tip: fc2ffb3b · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9024/0 · with-DB 5870/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 129162
- f5-x3-values-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-x3-values-port` → `2672dd43`; code tip `fc2ffb3b`
- written by deploy-card.sh at 2026-10-21 03:09 ET (`date`); trial merge of the heads onto main in order: clean
