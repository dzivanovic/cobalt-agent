JOB: stop-guard-work
LADDER: OFF-LADDER — reports/cto-2026-10-18.md R1841
BRANCH: deploy/stop-guard-work
WORKTREE: deploy-stop-guard-work
BASE: main
TIP: 9c359688
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-stop-guard-work.md
RULINGS: 2026-10-18 R1841, 2026-10-18 R1863
TAG: deploy-2026-10-18-stop-guard-work
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/stop-guard-work-1018` | `9c359688` | `9c359688` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stop-guard-work-check-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "def next_unlaunched" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · before `0` · after `1`
- `grep -c -F "test_w1_the_1017_2107_shape_with_nothing_live_blocks" /Users/cobalt/cobalt/tests/ops/test_stop_guard.py` · before `0` · after `1`

## SMOKE READS
- stop-guard tests · `uv run pytest -q tests/ops/test_stop_guard.py` · green: `0 failed`

## RECORDS
- stop-guard-work-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stop-guard-work-check-2026-10-18.md` last line: CHECK DONE · job: stop-guard-work-1018 · pass: 1 · tip: 9c359688 · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8508/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none (committed range; the tool's line names only the untracked SHADOW-INSTRUCTIONS.md) · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 191580
- stop-guard-work-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/stop-guard-work-1018` → `9c359688`; code tip `9c359688`
- written by deploy-card.sh at 2026-10-18 10:14 ET (`date`); trial merge of the heads onto main in order: clean
