JOB: smoke-string-1014
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1466, R1341
BRANCH: deploy/smoke-string-1014
WORKTREE: deploy-smoke-string-deploy-1014
BASE: main
TIP: c9fcabfa
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-smoke-string-1014.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-14-smoke-string
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/deploy-smoke-string-1014` | `f21900fc` | `c9fcabfa` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-smoke-string-check-2026-10-14.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "cobalt smoke" /Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · before `0` · after `1`
- `grep -c -F "cobalt smoke" /Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md` · before `0` · after `1`
- `grep -c -F "cobalt smoke" /Users/cobalt/cobalt/tests/ops/test_hub_lines.py` · before `0` · after `1`

## SMOKE READS
- RULE: the three counts on `TIP` are the counts printed above (one string, one line in each file); a count other than `1` on `TIP` fails the deploy's marker read.
- ONE SMOKE READ after the merge: `COBALT_ENV=production uv run cobalt smoke s2 --cutoff <the deploy instant, ISO 8601 with offset> --prod --json` (the deploy hub's own line, now on its allow list: green is the command running, no `Permission to use Bash has been denied`; `--json` prints the verdict table and writes no report file; the verdict colour is the set's smoke, not this proof's).

## RECORDS
- deploy-smoke-string-1014: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-smoke-string-check-2026-10-14.md` last line: CHECK DONE · job: deploy-smoke-string-1014 · pass: 1 · tip: f21900fc · house A: Grok FINDINGS: 1 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 178351
- deploy-smoke-string-1014: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-smoke-string-1014` → `c9fcabfa`; code tip `f21900fc`
- written by deploy-card.sh at 2026-10-14 13:56 ET (`date`); trial merge of the heads onto main in order: clean
