JOB: desk-installs-1015
LADDER: OFF-LADDER — reports/cto-2026-10-14.md R1471
BRANCH: deploy/desk-installs-1015
WORKTREE: deploy-desk-installs-1015
BASE: main
TIP: 66cf78d8
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-desk-installs-1015.md
RULINGS: 2026-10-14 R1471
TAG: deploy-2026-10-15-desk-installs
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/desk-installs-1014` | `7c8db6e1` | `66cf78d8` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-installs-fr1-check-2026-10-15.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "\"SendMessage\" --disallowedTools" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `0` · after `1`
- `grep -c -F "| \`SendMessage\` | **NEW**" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md"` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/ops/test_desk_installs_1014.py` · before `No such file` · after the path

## SMOKE READS
- Docs and tests only; a docs-and-tests deploy restarts nothing (`RESTARTS: none`) and takes no production command. The merge puts the new allow string on the line `desk-launch.sh desk` reads at the NEXT desk REFRESH; the running desk keeps its old line until then.
- Proof of the string itself: its first use (the desk's `SendMessage` to a seat is not denied by the classifier); a denial is recorded as a `## RECORDS` line, never routed around (L81 (3)).

## RECORDS
- desk-installs-1014: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-installs-fr1-check-2026-10-15.md` last line: CHECK DONE · job: desk-installs-1014 · pass: 1 · tip: 7c8db6e1 · house A: grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 173481
- desk-installs-1014: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-installs-1014` → `66cf78d8`; code tip `7c8db6e1`
- written by deploy-card.sh at 2026-10-15 10:27 ET (`date`); trial merge of the heads onto main in order: clean
