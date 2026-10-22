JOB: x15-hitl-probe-port
LADDER: OFF-LADDER — reports/cto-2026-10-21.md R2285
BRANCH: deploy/x15-hitl-probe-port-attempt2
WORKTREE: deploy-x15-hitl-probe-port-attempt2
BASE: main
TIP: c062baf7
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-x15-hitl-probe-port-attempt2.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-x15-hitl-probe-port-attempt2
MIGRATIONS: none
SET: x15-hitl-probe-port
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/x15-hitl-probe-port` | `304d5f3b` | `c062baf7` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x15-hitl-probe-port-check-2026-10-21.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "def _hitl_key_script" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1`
- `grep -c -F '@app.get("/hitl/x15-probe"' /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1`
- `grep -c -F 'add_parser("x15-send"' /Users/cobalt/cobalt/src/cobalt/hitl/cli.py` · before `0` · after `1`

## SMOKE READS
- the probe page answers after the aset restart · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/hitl/x15-probe` · exit 0, `200` (before the deploy it answers `422`, by reading `web.py:1451-1452`)
- the sheet answers after the aset restart · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` · exit 0, `200`

## RECORDS
- x15-hitl-probe-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x15-hitl-probe-port-check-2026-10-21.md` last line: CHECK DONE · job: x15-hitl-probe-port · pass: 1 · tip: 304d5f3b · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9086/0 · with-DB 5932/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 157088
- x15-hitl-probe-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x15-hitl-probe-port` → `c062baf7`; code tip `304d5f3b`
- written by deploy-card.sh at 2026-10-21 20:42 ET (`date`); trial merge of the heads onto main in order: clean
