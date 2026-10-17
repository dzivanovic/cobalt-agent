JOB: gemini-builder-row
LADDER: OFF-LADDER — reports/cto-2026-10-17.md R1738
BRANCH: deploy/gemini-builder-row
WORKTREE: deploy-gemini-builder-row
BASE: main
TIP: 06d31180
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gemini-builder-row.md
RULINGS: 2026-10-17 R1738
TAG: deploy-2026-10-17-gemini-builder-row
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/gemini-builder-row-1017` | `695f8bde` | `06d31180` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-check-2026-10-17.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.md` |

## MARKERS
- `grep -c -F "agy --model gemini-4-argon-high --mode accept-edits --sandbox --print-timeout 40m" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "gemini-4-argon-high) ;;" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "card 671 G2/FR-1: agy --add-dir D or --add-dir=D (D/**), read for agy only" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1`

## SMOKE READS
- shadow tests · `uv run pytest -q tests/ops/test_desk_launch_shadow.py tests/ops/test_shadow_hub_file.py tests/ops/test_bare_guard.py` · green: `0 failed`

## RECORDS
- gemini-builder-row: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-build-2026-10-17.md` at `06d31180` last line: BUILT · job: gemini-builder-row · tip: 695f8bde | on 7f415a4f | migration: none | offline 8416/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 123553
- gemini-builder-row: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-builder-row-check-2026-10-17.md` last line: CHECK DONE · job: gemini-builder-row · pass: 1 · tip: 7b986738 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8413/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 212150
- gemini-builder-row: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-builder-row-1017` → `06d31180`; code tip `695f8bde`
- written by deploy-card.sh at 2026-10-17 16:28 ET (`date`); trial merge of the heads onto main in order: clean
