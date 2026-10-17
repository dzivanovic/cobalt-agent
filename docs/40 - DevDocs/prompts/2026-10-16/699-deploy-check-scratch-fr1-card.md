JOB: check-scratch-fr1
LADDER: OFF-LADDER — reports/check-662-and-583-fr2-decisions-2026-10-17.md item 3 (brain, DESK RECORD R1759)
BRANCH: deploy/check-scratch-fr1
WORKTREE: deploy-check-scratch-fr1
BASE: main
TIP: 3879fdbb
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-check-scratch-fr1.md
RULINGS: 2026-10-12 R1138, 2026-10-15 R1532
TAG: deploy-2026-10-17-check-scratch-fr1
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/check-scratch-fr1` | `2e84ac75` | `3879fdbb` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-fr1-check-2026-10-17.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md` |

## MARKERS
- `grep -c -F "STAGED-CARD write failed" /Users/cobalt/cobalt/ops/desk/stage-set.sh` · before `0` · after `1`
- `grep -c -F "test_mk1_staging_writes_the_marker_naming_the_card" /Users/cobalt/cobalt/tests/ops/test_stage_set.py` · before `0` · after `1`

## SMOKE READS
- stage-set tests · `uv run pytest -q tests/ops/test_stage_set.py` · green: `0 failed`

## RECORDS
- check-scratch-fr1: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-fr1-build-2026-10-17.md` at `3879fdbb` last line: BUILT · job: check-scratch-fr1 · tip: 2e84ac75 | on 79f6f2f3 | migration: none | offline 8394/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 1 of 1 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 108345
- check-scratch-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-fr1-check-2026-10-17.md` last line: CHECK DONE · job: check-scratch-fr1 · pass: 1 · tip: b093f192 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 8393/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 248568
- check-scratch-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/check-scratch-fr1` → `3879fdbb`; code tip `2e84ac75`
- written by deploy-card.sh at 2026-10-17 12:15 ET (`date`); trial merge of the heads onto main in order: clean
