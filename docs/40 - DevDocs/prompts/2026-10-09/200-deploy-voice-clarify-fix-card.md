JOB: voice-clarify-fix-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R770
BRANCH: deploy/voice-clarify-fix-1009
WORKTREE: deploy-voice-clarify-fix-1009
BASE: main
TIP: 4465b758
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-voice-clarify-fix-1009.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-09-voice-clarify-fix
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/voice-clarify-fix-1009` | `9feda305` | `4465b758` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-clarify-fix-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "#cv-voice .cv-row[hidden]{display:none}" /Users/cobalt/cobalt/src/cobalt/voice/web.py` · before `0` · after `1` (the hidden-row CSS rule, row B)
- `grep -c -F "\"candidates\"" /Users/cobalt/cobalt/src/cobalt/voice/turn.py` · before `0` · after `1` (the plan clarify records its candidates, row C1)

## SMOKE READS
- the hidden-row rule in the voice widget code · `grep -c -F "#cv-voice .cv-row[hidden]{display:none}" /Users/cobalt/cobalt/src/cobalt/voice/web.py` · exit 0, a count of 1 or more
- the plan clarify candidates record in the voice turn code · `grep -c -F "\"candidates\"" /Users/cobalt/cobalt/src/cobalt/voice/turn.py` · exit 0, a count of 1 or more

## RECORDS
- voice-clarify-fix-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/voice-clarify-fix-check-2026-10-09.md` last line: CHECK DONE · job: voice-clarify-fix-1009 · pass: 1 · tip: 9feda305 · house A: Sol FINDINGS: 1 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 1 · suites: offline 4060/0 · with-DB 4947/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 161041
- voice-clarify-fix-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/voice-clarify-fix-1009` → `4465b758`; code tip `9feda305`
- written by deploy-card.sh at 2026-10-09 20:40 ET (`date`); trial merge of the heads onto main in order: clean
