JOB: deploy-03d-1005
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: deploy/deploy-03d-1005
WORKTREE: deploy-03d-1005
BASE: main
TIP: 07655b9b
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-03d-1005-attempt2.md
RULINGS: 2026-10-05 R391, 2026-10-05 R392, 2026-10-05 R408
TAG: deploy-2026-10-05-03d
MIGRATIONS: none
SET: workflow1

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/adoption-port-1005` | `36fa02ad` | `07655b9b` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-05-r2.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "args.no_db" /Users/cobalt/cobalt/src/cobalt/cli.py` · before `0` · after `1`
- `grep -c -F "validate --no-db" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`

## SMOKE READS
- validate --no-db flag · `grep -c -F "args.no_db" /Users/cobalt/cobalt/src/cobalt/cli.py` · exit 0, a count of 1 or more
- hub (d2) line · `grep -c -F "validate --no-db" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · exit 0, a count of 1 or more

## RECORDS
- adoption-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-05.md` last line: CHECK DONE · job: adoption-port · pass: 1 · tip: 53b56384 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3787/0 · with-DB 856/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0
- adoption-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/adoption-port-1005` → `07655b9b`; code tip `36fa02ad`
- G (d2) SKIPPED this run only (his R391): main's hub still runs the old (d2); this deploy ships the new one. D2.4 validate checks stand. No Grok read (his R392).
- written by deploy-card.sh at 2026-10-05 09:03 ET (`date`); trial merge of the heads onto main in order: clean
