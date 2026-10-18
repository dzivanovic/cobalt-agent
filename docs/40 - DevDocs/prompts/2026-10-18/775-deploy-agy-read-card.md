JOB: agy-read
LADDER: OFF-LADDER — reports/cto-2026-10-18.md R1863
BRANCH: deploy/agy-read
WORKTREE: deploy-agy-read
BASE: main
TIP: b05d90c3
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-agy-read.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-18-agy-read
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/agy-read-1018` | `b05d90c3` | `b05d90c3` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/agy-read-check-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "holds no allow rule" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "X1-READ.txt" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "antigravity-cli/settings.json" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`

## SMOKE READS
- no fetch rule · `grep -c -F "read_url(" /Users/cobalt/.gemini/antigravity-cli/settings.json` · green: `0`
- grant sentence · `grep -c -F "write_file(/Users/cobalt/cobalt-wt/<worktree>/)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · green: `1`

## RECORDS
- agy-read-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/agy-read-check-2026-10-18.md` last line: CHECK DONE · job: agy-read-1018 · pass: 1 · tip: b05d90c3 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8507/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 189802
- agy-read-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/agy-read-1018` → `b05d90c3`; code tip `b05d90c3`
- written by deploy-card.sh at 2026-10-18 09:59 ET (`date`); trial merge of the heads onto main in order: clean
