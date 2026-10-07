JOB: launcher-next-flow-1006
LADDER: OFF-LADDER — reports/next-flow-answer-2026-10-05.md 2026-10-05 R438
BRANCH: deploy/launcher-next-flow-1006
WORKTREE: deploy-launcher-next-flow-1006
BASE: main
TIP: 66e20fc2
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-launcher-next-flow-1006.md
RULINGS: 2026-10-05 R438, 2026-10-06 R588
TAG: deploy-2026-10-06-launcher-next-flow
MIGRATIONS: none
SET: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/launcher-next-flow-1006` | `055018c0` | `66e20fc2` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-next-flow-check-2026-10-06.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "TICKERS" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · before `0` · after `1` (N8, the deploy card carries the build's tickers)
- `grep -c -F "TICKERS" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `0` · after `2` (N8, the card row)
- `grep -c -F "def test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row" /Users/cobalt/cobalt/tests/ops/test_desk_launch_recut.py` · before `0` · after `1` (N7)

## SMOKE READS
- N8 in the script · `grep -c -F "TICKERS" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · exit 0, a count of 1 or more
- N8 in the card format · `grep -c -F "TICKERS" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · exit 0, a count of 1 or more
- N7 test present · `grep -c -F "def test_n7_a_long_failed_line_is_cut_to_fit_the_desk_row" /Users/cobalt/cobalt/tests/ops/test_desk_launch_recut.py` · exit 0, a count of 1 or more

RESTARTS: none. Every path is under `ops/`, `tests/ops/` or `docs/` (the check: `uv run cobalt jobs restarts 8e33fdc4..HEAD` last line `RESTARTS: none`, 10 rows; its `## Suites`). No `src/` path and no migration. The check left one OPEN item (A1: the fix-report blob is read at `desk-launch.sh:848` before P3 proves the head; P3 refuses an unproven head anyway): it goes on the follow-up list, not into this deploy.

## RECORDS
- launcher-next-flow: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-next-flow-check-2026-10-06.md` last line: CHECK DONE · job: launcher-next-flow · pass: 1 · tip: 055018c0 · house A: Sol FINDINGS: 2 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 0 · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 191425
- launcher-next-flow: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-next-flow-1006` → `66e20fc2`; code tip `055018c0`
- written by deploy-card.sh at 2026-10-06 20:56 ET (`date`); trial merge of the heads onto main in order: clean
