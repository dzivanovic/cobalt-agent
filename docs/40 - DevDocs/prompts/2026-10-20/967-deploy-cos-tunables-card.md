JOB: cos-tunables
LADDER: OFF-LADDER — reports/cos-bootstrap-decisions-2026-10-20.md 2026-10-20 R2201
BRANCH: deploy/cos-tunables
WORKTREE: deploy-cos-tunables
BASE: main
TIP: 0b8bf093
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-tunables.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-cos-tunables
MIGRATIONS: none
SET: cos-tunables
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/cos-tunables` | `0b8bf093` | `0b8bf093` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-tunables-check-fr1-2026-10-21.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "enabled: false" "/Users/cobalt/cobalt/configs/cobalt/jobs.yaml"` · before `1` · after `0`
- `grep -c -F "DEFAULT (brain; his word may change it)" "/Users/cobalt/cobalt/configs/cobalt/taxonomy/tunables.yaml"` · before `0` · after `0`
- FR-3: aset answers on the HITL page, a read-only GET from the Mac · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/hitl` · any HTTP status from aset counts (a tailnet or TLS error, no status, is RED); `grep -c -F "https://cobalt.taild24291.ts.net" "/Users/cobalt/cobalt/configs/cobalt/taxonomy/tunables.yaml"` · before `0` · after `1`

## SMOKE READS
- cos plist stays unloaded, present on disk · `ls /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` · exit 0, listed
- marker 1 needs zero `enabled: false` lines in `jobs.yaml` after the build (the T2 comment must not spell it); marker 2 needs exactly 0 lines carrying `DEFAULT (brain; his word may change it)` in `tunables.yaml` (the two `value:` lines of T1 carry the source comment instead; the string is written nowhere).
- the sheet answers after the restart · `curl -s -o /dev/null -w %{http_code} https://cobalt.taild24291.ts.net/` · exit 0, `200`

## RECORDS
- cos-tunables: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-tunables-check-fr1-2026-10-21.md` last line: CHECK DONE · job: cos-tunables · pass: 1 · tip: 0b8bf093 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 8976/0 · with-DB 5875/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 181651
- cos-tunables: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-tunables` → `0b8bf093`; code tip `0b8bf093`
- written by deploy-card.sh at 2026-10-21 02:34 ET (`date`); trial merge of the heads onto main in order: clean
