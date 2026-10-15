JOB: card-template-1014-fr1
LADDER: OFF-LADDER — reports/cto-2026-10-14.md R1471, R1472
BRANCH: deploy/card-template-1014-fr1
WORKTREE: deploy-card-template-1014-fr1
BASE: main
TIP: 9e305776
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-card-template-1014-fr1.md
RULINGS: 2026-10-14 R1471
TAG: deploy-2026-10-15-card-template-fr1
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/card-template-1014-fr1` | `439ea472` | `9e305776` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/card-template-check-2026-10-14.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/card-template-build-fr1-2026-10-15.md` |

## MARKERS
- `grep -c -F "his R1471 (6): rulings by R number" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `0` · after `2`
- `grep -c -F "label · the command typed whole" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `1` · after `2`
- `grep -c -F "def test_fr_o1_both_credits" /Users/cobalt/cobalt/tests/ops/test_card_template_1014.py` · before `0` · after `1`

## SMOKE READS
- RULE: the counts on `TIP` are the counts printed above (the fix round's credit text sits on the C1 line and in the C2 section; the label text on the C1 line and one other place); a count other than the one printed fails the deploy's marker read.
- ONE SMOKE READ after the merge: `uv run pytest -q tests/ops/test_card_template_1014.py` → `0 failed` (the new pins hold on the landed tree; they read `CARD.md` as it stands, no commit).

## RECORDS
- card-template-1014-fr1: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/card-template-build-fr1-2026-10-15.md` at `9e305776` last line: BUILT · job: card-template-1014-fr1 · tip: 439ea472 | on 2f6ae8fd | migration: none | offline 8071/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 119323
- card-template-1014-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/card-template-check-2026-10-14.md` last line: CHECK DONE · job: card-template-1014 · pass: 1 · tip: 5a29de43 · house A: Grok FINDINGS: 3 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 5 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 153702
- card-template-1014-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/card-template-1014-fr1` → `9e305776`; code tip `439ea472`
- written by deploy-card.sh at 2026-10-15 15:10 ET (`date`); trial merge of the heads onto main in order: clean
