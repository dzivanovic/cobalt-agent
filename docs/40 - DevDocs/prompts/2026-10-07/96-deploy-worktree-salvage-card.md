JOB: worktree-salvage-1007
LADDER: OFF-LADDER — reports/cto-2026-10-07-words.md 2026-10-07 R613
BRANCH: deploy/worktree-salvage-1007
WORKTREE: deploy-worktree-salvage-1007
BASE: main
TIP: 71d34bd9
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-worktree-salvage-1007.md
RULINGS: 2026-10-07 R613
TAG: deploy-2026-10-07-worktree-salvage
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/worktree-salvage-1007` | `71d34bd9` | `71d34bd9` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/worktree-salvage-check-2026-10-07.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "SALVAGED:" /Users/cobalt/cobalt/ops/desk/job-clean.sh` · before `0` · after `4` (the salvage report line)
- `grep -c -F "def test_salvage_usage_names_the_salvage_form" /Users/cobalt/cobalt/tests/ops/test_gate_clean.py` · before `0` · after `1` (W1)

## SMOKE READS
- salvage form in the script · `grep -c -F "SALVAGED:" /Users/cobalt/cobalt/ops/desk/job-clean.sh` · exit 0, a count of 1 or more
- W1 test present · `grep -c -F "def test_salvage_usage_names_the_salvage_form" /Users/cobalt/cobalt/tests/ops/test_gate_clean.py` · exit 0, a count of 1 or more

RESTARTS: none. Every path is under `ops/`, `tests/ops/` or `docs/` (the check's stop line: `RESTARTS: none`). No `src/` path, no migration, no resident. No allow-list change.

## RECORDS
- worktree-salvage: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/worktree-salvage-check-2026-10-07.md` last line: CHECK DONE · job: worktree-salvage · pass: 1 · tip: 71d34bd9 · house A: Sol FINDINGS: 3 · findings: 7 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 175727
- worktree-salvage: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/worktree-salvage-1007` → `71d34bd9`; code tip `71d34bd9`
- written by deploy-card.sh at 2026-10-07 11:11 ET (`date`); trial merge of the heads onto main in order: clean
