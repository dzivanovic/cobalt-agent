JOB: gemini-builder-row-attempt2
LADDER: OFF-LADDER — reports/cto-2026-10-17.md R1738
BRANCH: deploy/gemini-builder-row-attempt2
WORKTREE: deploy-gemini-builder-row-attempt2
BASE: main
TIP: 5fea0cc4
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gemini-builder-row-attempt2.md
RULINGS: 2026-10-17 R1738
TAG: deploy-2026-10-17-gemini-builder-row
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/gemini-builder-row-fr1` | `52a0600d` | `5fea0cc4` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-fr1-check-2026-10-17.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 40m" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "gemini-4-argon-high) ;;" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "card 671 G2/FR-1: agy --add-dir D or --add-dir=D (D/**), read for agy only" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1`

## SMOKE READS
- shadow tests · `uv run pytest -q tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py` · green: `0 failed`

## RECORDS
- gemini-builder-row-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-fr1-check-2026-10-17.md` last line: CHECK DONE · job: gemini-builder-row-fr1 · pass: 1 · tip: 52a0600d · house A: grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8491/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 190470
- gemini-builder-row-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-builder-row-fr1` → `5fea0cc4`; code tip `52a0600d`
- written by deploy-card.sh at 2026-10-17 19:14 ET (`date`); trial merge of the heads onto main in order: clean
