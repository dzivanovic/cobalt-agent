JOB: f16-close-fr3
LADDER: S5 · F16 close
BRANCH: deploy/f16-close-fr3
WORKTREE: deploy-f16-close-fr3
BASE: main
TIP: e7688a8f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f16-close-fr3.md
RULINGS: none
TAG: deploy-2026-10-20-f16-close-fr3
MIGRATIONS: none
SET: f16-close
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f16-close-fr3` | `1aea7418` | `e7688a8f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f16-close-fr3-check-2026-10-20.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "Playbook (F23): " /Users/cobalt/cobalt/src/cobalt/cli.py` · before `0` · after `1`
- `grep -c -F "Daily refresh (F4): " /Users/cobalt/cobalt/src/cobalt/cli.py` · before `0` · after `1`
- `grep -c -F "with no consumer (F16)" /Users/cobalt/cobalt/src/cobalt/taxonomy/loader.py` · before `0` · after `1`

## SMOKE READS
- validate · `COBALT_ENV=production uv run cobalt validate` · green: exit 0, a line starting `Playbook (F23): ` and a line starting `Daily refresh (F4): `, the last line `Placement (docs/PLACEMENT.md): tree clean.`

## RECORDS
- f16-close-fr3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f16-close-fr3-check-2026-10-20.md` last line: CHECK DONE · job: f16-close-fr3 · pass: 1 · tip: 1aea7418 · house A: Grok FINDINGS: 1 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8863/0 · with-DB 5758/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 195502
- f16-close-fr3: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f16-close-fr3` → `e7688a8f`; code tip `1aea7418`
- written by deploy-card.sh at 2026-10-20 03:37 ET (`date`); trial merge of the heads onto main in order: clean
