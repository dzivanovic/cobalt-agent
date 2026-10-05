JOB: deploy-guard-b-1005
LADDER: S3-P3 · F14
BRANCH: deploy/deploy-guard-b-1005
WORKTREE: deploy-guard-b-1005
BASE: main
TIP: 47ec01c5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-guard-b-1005.md
RULINGS: 2026-10-05 R390, 2026-10-05 R391, 2026-10-05 R392
TAG: deploy-2026-10-05-guard-b
MIGRATIONS: none
SET: workflow2

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/cobalt-guard-b-1004` | `47ec01c5` | `47ec01c5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cobalt-guard-b-check-2026-10-04-r3.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `3`

## SMOKE READS
- cobalt-guard-b awk fence · `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more

## RECORDS
- cobalt-guard-b: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cobalt-guard-b-check-2026-10-04-r3.md` last line: CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 47ec01c5 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3782/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0
- cobalt-guard-b: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cobalt-guard-b-1004` → `47ec01c5`; code tip `47ec01c5`
- G (d2) SKIPPED this run only (his R391): main's hub still runs the old (d2) until 03d ships. No Grok read.
