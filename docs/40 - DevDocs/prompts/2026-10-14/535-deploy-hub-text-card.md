JOB: hub-text-1013
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1295, reports/cto-2026-10-13.md R1309, R1341
BRANCH: deploy/hub-text-1013
WORKTREE: deploy-hub-text-1013
BASE: main
TIP: 0f4a49c5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-1013.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-14-hub-text
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/hub-text-1013` | `3894a878` | `0f4a49c5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-check-2026-10-13.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "21:30-22:30 ET" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "FIX-ROUND REPORT (brain R1309):" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `grep -c -F "no untracked file at the stop line" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`

## SMOKE READS
- `uv run pytest tests/ops/test_hub_text_1013.py tests/ops/test_hub_lines.py tests/ops/test_build_hub_no_clutter.py` → all passed (docs-only deploy: no resident, no restart, no production command)

## RECORDS
- hub-text-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-check-2026-10-13.md` last line: CHECK DONE · job: hub-text-1013 · pass: 1 · tip: 3894a878 · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 138522
- hub-text-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-text-1013` → `0f4a49c5`; code tip `3894a878`
- written by deploy-card.sh at 2026-10-14 06:47 ET (`date`); trial merge of the heads onto main in order: clean
