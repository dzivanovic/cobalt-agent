JOB: deploy-radar-mirror-scope
LADDER: OFF-LADDER — reports/survey-settings-writer-2026-10-23.md R2389
BRANCH: deploy/deploy-radar-mirror-scope
WORKTREE: deploy-radar-mirror-scope
BASE: main
TIP: 25994142
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-radar-mirror-scope.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-24-radar-mirror-scope
MIGRATIONS: none
SET: radar-mirror-scope
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/radar-mirror-scope` | `25994142` | `25994142` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-check-2026-10-23.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · before `0` · after `1`
- `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · before `0` · after `1`

## SMOKE READS
- the radar notes module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · exit 0, listed
- the scope test is on the tree · `ls /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · exit 0, listed

## RECORDS
- radar-mirror-scope: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-check-2026-10-23.md` last line: CHECK DONE · job: radar-mirror-scope · pass: 1 · tip: 25994142 · house A: Grok FINDINGS: 1 · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 164093
- radar-mirror-scope: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope` → `25994142`; code tip `25994142`
- written by deploy-card.sh at 2026-10-24 18:51 ET (`date`); trial merge of the heads onto main in order: clean
