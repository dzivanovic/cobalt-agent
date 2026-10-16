JOB: jev-shadow-fr1
LADDER: OFF-LADDER — reports/cto-2026-10-15.md R1467, R1532, R1535
BRANCH: deploy/jev-shadow-fr1
WORKTREE: deploy-jev-shadow-fr1
BASE: main
TIP: d2066509
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-jev-shadow-fr1.md
RULINGS: 2026-10-15 R1532, 2026-10-15 R1535
TAG: deploy-2026-10-16-jev-shadow-fr1
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `feat/jev-shadow-fr1` | `6a74fa0c` | `d2066509` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md` |

## MARKERS
- `grep -c -F "def build_launch" /Users/cobalt/cobalt/src/cobalt/classify/route.py` · before `0` · after `1`
- `grep -c -F "NOT_BUILD_HEADERS" /Users/cobalt/cobalt/src/cobalt/classify/route.py` · before `0` · after `2`

## SMOKE READS
- ONE SMOKE READ after the merge: `uv run pytest -q tests/cobalt/test_jev_shadow_1015.py` → `0 failed`; and `uv run cobalt classify route --card "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" --dry-run` → one `ROUTE DRY` line and `cards=1 calls=1`, zero network.
- RESTARTS at the deploy: the table R2 derives (expected `com.cobalt.radar`, the build report's own `RESTARTS:`; the FR-O2 fix touches `src/cobalt/classify/route.py` only).

## RECORDS
- jev-shadow-fr1: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-build-fr1-2026-10-16.md` at `d2066509` last line: BUILT · job: jev-shadow-fr1 · tip: 6a74fa0c | on f6ca1455 | migration: none | offline 4572/0 | with-DB 5475/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 1 of 1 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 187978
- jev-shadow-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md` last line: CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · house A: grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8307/0 · with-DB 5471/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407
- jev-shadow-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-shadow-fr1` → `d2066509`; code tip `6a74fa0c`
- written by deploy-card.sh at 2026-10-16 07:48 ET (`date`); trial merge of the heads onto main in order: clean
