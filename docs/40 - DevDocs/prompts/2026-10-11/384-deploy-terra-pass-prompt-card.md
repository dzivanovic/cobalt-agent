JOB: terra-pass-prompt-1011
LADDER: OFF-LADDER — reports/cto-2026-10-11.md R1107
BRANCH: deploy/terra-pass-prompt-1011
WORKTREE: deploy-terra-pass-prompt-1011
BASE: main
TIP: 7e0cc8a2
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-terra-pass-prompt-1011.md
RULINGS: 2026-10-11 R1107
TAG: deploy-2026-10-11-terra-pass-prompt
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/terra-pass-prompt-1011` | `a790e54d` | `7e0cc8a2` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/terra-pass-prompt-check-2026-10-11.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "or only commands that read files; no command that writes, deletes or uses the network (TERRA)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before count `0` · after count `1` (the pass prompt line)
- `grep -c -F -e "accepted by HIS word 2026-10-11 (R1107)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before count `0` · after count `1` (the Terra note)

## SMOKE READS
- Terra read sentence is on main · `grep -c -F -e "or only commands that read files; no command that writes, deletes or uses the network (TERRA)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · prints 1
- Grok and Sonnet keep the no-command line · `grep -c -F -e "Run <no command (GROK, SONNET) or" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · prints 1

## RECORDS
- terra-pass-prompt-1011: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/terra-pass-prompt-check-2026-10-11.md` last line: CHECK DONE · job: terra-pass-prompt-1011 · pass: 1 · tip: a790e54d · house A: Grok FINDINGS: 1 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 157961
- terra-pass-prompt-1011: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/terra-pass-prompt-1011` → `7e0cc8a2`; code tip `a790e54d`
- written by deploy-card.sh at 2026-10-11 16:31 ET (`date`); trial merge of the heads onto main in order: clean
