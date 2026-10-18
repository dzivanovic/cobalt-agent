JOB: gemini-probe-id
LADDER: OFF-LADDER — reports/cto-2026-10-17.md R1736
BRANCH: deploy/gemini-probe-id
WORKTREE: deploy-gemini-probe-id
BASE: main
TIP: 9f281a6a
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gemini-probe-id.md
RULINGS: 2026-10-17 R1736
TAG: deploy-2026-10-17-gemini-probe-id
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/gemini-probe-id-1017` | `744128d7` | `9f281a6a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-probe-id-check-2026-10-17.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "agy --model gemini-4-argon-high" /Users/cobalt/cobalt/ops/desk/house-probe.sh` · before `0` · after `2`
- `grep -c -F "agy --model gemini-4-argon-high" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`

## SMOKE READS
- gemini probe · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh gemini` · green: `gemini: UP`
- probe tests · `uv run pytest -q tests/ops/test_house_probe.py` · green: `0 failed`

## RECORDS
- gemini-probe-id: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-probe-id-check-2026-10-17.md` last line: CHECK DONE · job: gemini-probe-id · pass: 1 · tip: 744128d7 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 8389/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 179030
- gemini-probe-id: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-probe-id-1017` → `9f281a6a`; code tip `744128d7`
- written by deploy-card.sh at 2026-10-17 20:09 ET (`date`); trial merge of the heads onto main in order: clean
