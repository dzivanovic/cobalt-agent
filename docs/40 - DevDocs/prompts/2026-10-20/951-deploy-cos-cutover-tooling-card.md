JOB: cos-cutover-tooling
LADDER: OFF-LADDER — reports/cos-bootstrap-decisions-2026-10-20.md 2026-10-20 brain 9b07db5a (L79)
BRANCH: deploy/cos-cutover-tooling
WORKTREE: deploy-cos-cutover-tooling
BASE: main
TIP: f15d7af5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-cutover-tooling.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-20-cos-cutover-tooling
MIGRATIONS: none
SET: cos-cutover
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/cos-cutover-tooling` | `f15d7af5` | `f15d7af5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-cutover-tooling-check-2026-10-20.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "card 931 T2" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "is retired; a retired label is never restarted" /Users/cobalt/cobalt/ops/desk/deploy-outage.sh` · before `0` · after `1`
- `grep -c -F "retired (recorded)" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `0` · after `1`
- `grep -c -F "com.cobalt.agent recorded retired" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `8`

## SMOKE READS
- The markers count LINES (`grep -c -F`): the builder puts `retired (recorded)` (`deploy-step0.sh`) and `is retired; a retired label is never restarted` (`deploy-outage.sh`) on exactly one line each of their script; the header comment and the dry-run mirror word it differently.

## RECORDS
- cos-cutover-tooling: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-cutover-tooling-check-2026-10-20.md` last line: CHECK DONE · job: cos-cutover-tooling · pass: 1 · tip: f15d7af5 · house A: Gemini FINDINGS: 2 · findings: 4 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9023/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 236240
- cos-cutover-tooling: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-cutover-tooling` → `f15d7af5`; code tip `f15d7af5`
- written by deploy-card.sh at 2026-10-20 20:25 ET (`date`); trial merge of the heads onto main in order: clean
