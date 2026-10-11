JOB: held-closed-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R993
BRANCH: deploy/held-closed-1010
WORKTREE: deploy-held-closed-1010
BASE: main
TIP: 9556c9ca
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-held-closed-1010.md
RULINGS: 2026-10-05 R438, 2026-10-11 R1009
TAG: deploy-2026-10-11-held-closed
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/held-closed-1010` | `9556c9ca` | `9556c9ca` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/held-closed-check-2026-10-11.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "has no FIXED line" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before count `0` · after count `1` (card 317 H4, the held-row text of P2)
- `grep -c -F -e "CARRIED" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before count `0` · after count `1` (card 317 H4, the held-row sentence of CARD.md; scripts, tests and hub text only, no resident)

## SMOKE READS
- the held-row text is on main · `grep -c -F -e "has no FIXED line" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · prints 1
- the CARD.md sentence is on main · `grep -c -F -e "CARRIED" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · prints 1

## RECORDS
- held-closed-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/held-closed-check-2026-10-11.md` last line: CHECK DONE · job: held-closed-1010 · pass: 1 · tip: 9556c9ca · house A: Sol FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 3 · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 220633
- held-closed-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/held-closed-1010` → `9556c9ca`; code tip `9556c9ca`
- written by deploy-card.sh at 2026-10-11 06:47 ET (`date`); trial merge of the heads onto main in order: clean
