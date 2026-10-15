JOB: card-template-1015
LADDER: OFF-LADDER — reports/cto-2026-10-14.md R1471, R1472
BRANCH: deploy/card-template-1015
WORKTREE: deploy-card-template-1015
BASE: main
TIP: ec9c8926
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-card-template-1015.md
RULINGS: 2026-10-14 R1471
TAG: deploy-2026-10-15-card-template
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/card-template-1014` | `5a29de43` | `ec9c8926` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/card-template-check-2026-10-14.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "## DEPLOY PROOF" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `0` · after `2`
- `grep -c -F "HOW A CARD CITES AND PINS" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/ops/test_card_template_1014.py` · before `No such file or directory` · after `/Users/cobalt/cobalt/tests/ops/test_card_template_1014.py`

## SMOKE READS
- RULE: the two counts on `TIP` are the counts printed above (the `## DEPLOY PROOF` text sits on the C1 line and the C2 `- DEPLOY PROOF:` line); a count other than the one printed fails the deploy's marker read.
- ONE SMOKE READ after the merge: `uv run pytest -q tests/ops/test_card_template_1014.py` → `0 failed` (the new pins hold on the landed tree; they read `CARD.md` as it stands, no commit).

## RECORDS
- card-template-1014: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/card-template-check-2026-10-14.md` last line: CHECK DONE · job: card-template-1014 · pass: 1 · tip: 5a29de43 · house A: Grok FINDINGS: 3 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 5 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 153702
- card-template-1014: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/card-template-1014` → `ec9c8926`; code tip `5a29de43`
- written by deploy-card.sh at 2026-10-15 11:22 ET (`date`); trial merge of the heads onto main in order: clean
