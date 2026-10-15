JOB: result-file-1014
LADDER: OFF-LADDER — reports/cto-2026-10-14.md R1471
BRANCH: deploy/result-file-1014
WORKTREE: deploy-result-file-1014
BASE: main
TIP: 55198484
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-result-file-1014.md
RULINGS: 2026-10-14 R1471
TAG: deploy-2026-10-14-result-file
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/result-file-1014` | `55198484` | `55198484` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/result-file-check-2026-10-14.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/ops/desk/result-read.sh` · before `No such file` · after the path
- `grep -c -F "RESULT FILE (his R1471)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `grep -c -F "RESULT FILE (his R1471)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`

## SMOKE READS
- MARKERS (the desk's, for the deploy card): `ls /Users/cobalt/cobalt/ops/desk/result-read.sh` before: no such file; after: the file. `grep -c -F "RESULT FILE (his R1471)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` before `0`, after `1`; the same on `CHECK-HUB.md`: before `0`, after `1`.
- SMOKE READS: the three gates still read a report with NO result file (every deploy before this card): `uv run pytest -q tests/ops/test_deploy_step0.py tests/ops/test_deploy_card.py tests/ops/test_the_rule_sweep.py` → `0 failed`, and `tests/ops/test_result_file.py` → `0 failed`. No production `db query`, no launchd, no restart (`MIGRATIONS: none`).
- FIRST USE: the next build and check that ship write the file; the deploy of the set that follows reads it. A gate that refuses a good file is the card's rollback signal: the stop-line path is untouched, so one revert of this set restores the old read.
EXTRA READ (brain direction, desk row R1508; a production READ, not a db query): `COBALT_ENV=production uv run cobalt smoke s2 --cutoff 2026-10-14T19:39:41-04:00 --prod` WITHOUT `--json`, once, after the merge; record its exit, its report file path, and every check line holding FAIL with its detail line, whole. It does not hold this deploy; the failing check id goes to the desk for the brain.

## RECORDS
- result-file-1014: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/result-file-check-2026-10-14.md` last line: CHECK DONE · job: result-file-1014 · pass: 1 · tip: 55198484 · house A: grok FINDINGS: 5 · findings: 7 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 231660
- result-file-1014: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/result-file-1014` → `55198484`; code tip `55198484`
- written by deploy-card.sh at 2026-10-14 21:32 ET (`date`); trial merge of the heads onto main in order: clean
