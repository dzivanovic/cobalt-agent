JOB: deploy-freeze-fr1
LADDER: OFF-LADDER — reports/cto-2026-10-14.md R1471, R1472
BRANCH: deploy/deploy-freeze-fr1
WORKTREE: deploy-deploy-freeze-fr1
BASE: main
TIP: 733c6bca
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-freeze-fr1.md
RULINGS: 2026-10-14 R1471
TAG: deploy-2026-10-15-deploy-freeze-fr1
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/deploy-freeze-fr1` | `733c6bca` | `733c6bca` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-freeze-fr1-check-2026-10-15.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "deploy-shipped.sh" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `2`
- `grep -c -F "deploy-shipped.sh" /Users/cobalt/cobalt/ops/desk/pre-commit` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh` · before `No such file or directory` · after `/Users/cobalt/cobalt/ops/desk/deploy-shipped.sh`

## SMOKE READS
- RULE: the three counts on `TIP` are the counts above, one reference per named line; the `.git/hooks/pre-commit` symlink points at `ops/desk/pre-commit` already (`ls -la /Users/cobalt/cobalt/.git/hooks/pre-commit`, Sep 30), so the merged hook is live at the merge.
- ONE SMOKE READ after the merge: `sh /Users/cobalt/cobalt/ops/desk/deploy-shipped.sh --job deploy-freeze-fr1` (green after the merge: the command runs, exit 0, and prints the hub path `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`; once every `TIP` head is merged `git diff --name-only main...<head>` lists nothing, so the list is just the hub file; the narrow list after 4.3 is only the hub file and the guard stays safe through arm (ii) (the report is committed on `main`: every path refused but the report); the deploy's own report commit is allowed by the guard, so the read does not conflict with D2.0).

## RECORDS
- deploy-freeze-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-freeze-fr1-check-2026-10-15.md` last line: CHECK DONE · job: deploy-freeze-fr1 · pass: 1 · tip: 733c6bca · house A: grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8133/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 202217
- deploy-freeze-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-freeze-fr1` → `733c6bca`; code tip `733c6bca`
- written by deploy-card.sh at 2026-10-15 18:30 ET (`date`); trial merge of the heads onto main in order: clean
