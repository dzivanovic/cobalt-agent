JOB: gemini-read-grant-1019
LADDER: OFF-LADDER — reports/cto-2026-10-19.md R2005
BRANCH: deploy/gemini-read-grant-1019
WORKTREE: deploy-gemini-read-grant-1019
BASE: main
TIP: 7e165648
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gemini-read-grant-1019.md
RULINGS: 2026-10-18 R1863, 2026-10-18 R1942
TAG: deploy-2026-10-19-gemini-read-grant-1019
MIGRATIONS: none
SET: gemini-grant
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/gemini-read-grant-1019` | `7e165648` | `7e165648` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-read-grant-1019-check-2026-10-19.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "R2011: a Gemini call only from its worktree" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1`
- `grep -c -F "kind x1-copy: the X1 leg's agy transcript" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "a Gemini call only while the seat's cwd is exactly <worktree> (R2011)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "leg 0f, the outside-cwd leg" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "one agy launch per leg, R2007" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "X1 WRITE OK" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `1` · after `0`
- `grep -c -F "Run NO shell command and no URL fetch; read and write files with your file tools only; a denial ends your run." "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1` (step 4; the pass prompt line holds the clause with `(GEMINI)` in place of the full stop)

## SMOKE READS
- x1-copy refuses a foreign worktree · `sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh x1-copy x1-canary 0a` · green: exit 1, stderr holds `REFUSED: x1-copy` (writes nothing: `x1-canary` is a refused name; before the deploy it also exits 1 but with `REFUSED: kind 'x1-copy' is none of`, so it is red on that string alone). The string is `refuse()`'s `REFUSED: %s` (`git show main:ops/desk/desk-launch.sh` `:384-387`) with T1's `x1-copy: <reason>`.
- sweep, dry · `DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt/ops/desk/desk-launch.sh grant-sweep` · green: exit 0, last line `GRANT-SWEEP: 0 would be removed, 0 live` (card 800's form, `prompts/2026-10-18/800-gemini-grant-card.md` `## DEPLOY PROOF`; unchanged by this job)

## RECORDS
- gemini-read-grant-1019: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gemini-read-grant-1019-check-2026-10-19.md` last line: CHECK DONE · job: gemini-read-grant-1019 · pass: 1 · tip: 7e165648 · house A: Grok FINDINGS: 3 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 8799/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 26 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 197976
- gemini-read-grant-1019: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gemini-read-grant-1019` → `7e165648`; code tip `7e165648`
- written by deploy-card.sh at 2026-10-19 11:18 ET (`date`); trial merge of the heads onto main in order: clean
