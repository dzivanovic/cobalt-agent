JOB: check-scratch-1016
LADDER: OFF-LADDER — reports/cto-2026-10-15.md R1532
BRANCH: deploy/check-scratch-1016
WORKTREE: deploy-check-scratch-1016
BASE: main
TIP: 949cb071
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-check-scratch-1016.md
RULINGS: 2026-10-17 R1731
TAG: deploy-2026-10-17-check-scratch-1016
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/check-scratch-1016` | `dd4d968d` | `949cb071` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-check-2026-10-16.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md` |

## MARKERS
- `grep -c -F "more than one prior card copy" /Users/cobalt/cobalt/ops/desk/stage-set.sh` · before `0` · after `1`
- `grep -c -F "test_cs1_a_fix_rounds_check_clears_the_first_passes_folder" /Users/cobalt/cobalt/tests/ops/test_stage_set.py` · before `0` · after `1`

## SMOKE READS
- stage-set tests · `uv run pytest -q tests/ops/test_stage_set.py` · green: `0 failed`
EXTRA READ (R1731): deployed before its fix-round check, HIS RULING A, 2026-10-16. In the build report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md` quote the FR-1 and FR-2 red-green lines and the guard test `test_fr1_a_build_card_read_copy_does_not_block_the_clear`; the deploy report carries them. After the merge, `uv run pytest -q tests/ops/test_stage_set.py` green.

## RECORDS
- check-scratch-1016: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-build-2026-10-16.md` at `949cb071` last line: BUILT · job: check-scratch-1016 · tip: dd4d968d | on b84cca9a | migration: none | offline 8388/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 2 of 2 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 152910
- check-scratch-1016: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/check-scratch-check-2026-10-16.md` last line: CHECK DONE · job: check-scratch-1016 · pass: 1 · tip: 85eade55 · house A: grok FINDINGS: 1 · findings: 2 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 8384/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 185748
- check-scratch-1016: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/check-scratch-1016` → `949cb071`; code tip `dd4d968d`
- written by deploy-card.sh at 2026-10-17 06:29 ET (`date`); trial merge of the heads onto main in order: clean
