JOB: needs-his-hand-1012
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1138
BRANCH: deploy/needs-his-hand-1012
WORKTREE: deploy-needs-his-hand-1012
BASE: main
TIP: c2352cb8
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-needs-his-hand-1012.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-needs-his-hand
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/needs-his-hand-1012` | `ad73d04a` | `c2352cb8` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/needs-his-hand-check-2026-10-12.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "## NEEDS HIS HAND" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md"` · before count `0` · after count `1` (the REPORT shape line)
- `grep -c -F -e "## NEEDS HIS HAND" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md"` · before count `0` · after count `1` (the VERDICT line)

## SMOKE READS
- The close prompt carries the section on main · `grep -c -F -e "## NEEDS HIS HAND" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md"` · prints 1
- The day-open prompt carries it on main · `grep -c -F -e "## NEEDS HIS HAND" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md"` · prints 1

## RECORDS
- needs-his-hand-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/needs-his-hand-check-2026-10-12.md` last line: CHECK DONE · job: needs-his-hand-1012 · pass: 1 · tip: ad73d04a · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 154283
- needs-his-hand-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/needs-his-hand-1012` → `c2352cb8`; code tip `ad73d04a`
- written by deploy-card.sh at 2026-10-12 08:17 ET (`date`); trial merge of the heads onto main in order: clean
