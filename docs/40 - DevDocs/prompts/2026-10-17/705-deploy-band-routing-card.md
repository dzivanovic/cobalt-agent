JOB: band-routing-1015
LADDER: OFF-LADDER — reports/cto-2026-10-15.md R1532
BRANCH: deploy/band-routing-1015
WORKTREE: deploy-band-routing-1015
BASE: main
TIP: 2880eb0e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-band-routing-1015.md
RULINGS: 2026-10-15 R1532
TAG: deploy-2026-10-17-band-routing-1015
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/band-routing-1015` | `05654335` | `2880eb0e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/band-routing-check-fr4-2026-10-17.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "BAND" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `0` · after `2` (the new header row and the new paragraph, one line each)
- `grep -c -F "BAND ROUTING" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before `0` · after `1`
- `grep -c -F "BAND (his 2026-10-15 R1532)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/ops/test_band_routing_1015.py` · before `No such file or directory` · after `/Users/cobalt/cobalt/tests/ops/test_band_routing_1015.py`

## SMOKE READS
- BAND_FROM in the launcher · `grep -c -F "BAND_FROM" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · green: a count of `2` or more (before the deploy it is `0`)
- band routing tests · `uv run pytest -q tests/ops/test_band_routing_1015.py` · green: `0 failed`

## RECORDS
- band-routing-1015: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/band-routing-check-fr4-2026-10-17.md` last line: CHECK DONE · job: band-routing-1015 · pass: 1 · tip: 05654335 · house A: grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8442/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 226790
- band-routing-1015: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/band-routing-1015` → `2880eb0e`; code tip `05654335`
- written by deploy-card.sh at 2026-10-17 15:17 ET (`date`); trial merge of the heads onto main in order: clean
