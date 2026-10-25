JOB: deploy-radar-mirror-scope-port2
LADDER: OFF-LADDER — reports/survey-settings-writer-2026-10-23.md R2389
BRANCH: deploy/deploy-radar-mirror-scope-port2
WORKTREE: deploy-radar-mirror-scope-port2
BASE: main
TIP: 50116c45
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-radar-mirror-scope-port2.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-24-radar-mirror-scope-port2
MIGRATIONS: none
SET: radar-mirror-scope-port
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/radar-mirror-scope-port` | `283389ff` | `50116c45` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port-check-2026-10-24.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · before `0` · after `1`
- `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · before `0` · after `1`

## SMOKE READS
- the radar notes module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · exit 0, listed
- the scope test is on the tree · `ls /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · exit 0, listed

## RECORDS
- radar-mirror-scope-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port-check-2026-10-24.md` last line: CHECK DONE · job: radar-mirror-scope-port · pass: 1 · tip: 283389ff · house A: Gemini FINDINGS: 0 · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 167121
- radar-mirror-scope-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port` → `50116c45`; code tip `283389ff`
- written by deploy-card.sh at 2026-10-24 22:32 ET (`date`); trial merge of the heads onto main in order: clean
