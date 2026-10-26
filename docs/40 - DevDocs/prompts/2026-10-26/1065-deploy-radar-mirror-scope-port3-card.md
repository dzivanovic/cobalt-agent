JOB: radar-mirror-scope-port3
LADDER: OFF-LADDER — reports/survey-settings-writer-2026-10-23.md R2389
BRANCH: deploy/radar-mirror-scope-port3
WORKTREE: deploy-radar-mirror-scope-port3
BASE: main
TIP: 304a0b03
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-radar-mirror-scope-port3.md
RULINGS: none
TAG: deploy-2026-10-26-radar-mirror-scope-port3
MIGRATIONS: none
SET: radar-mirror-scope-port3
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/radar-mirror-scope-port3` | `671e0215` | `304a0b03` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port3-check-2026-10-24.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "MIRROR_SOURCE_PREFIX = " /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · before `0` · after `1`
- `grep -c -F "def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical" /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · before `0` · after `1`

## SMOKE READS
- the radar notes module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/radar/notes.py` · exit 0, listed
- the scope test is on the tree · `ls /Users/cobalt/cobalt/tests/cobalt/test_radar_mirror_scope.py` · exit 0, listed

## RECORDS
- radar-mirror-scope-port3: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-mirror-scope-port3-check-2026-10-24.md` last line: CHECK DONE · job: radar-mirror-scope-port3 · pass: 1 · tip: 671e0215 · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9120/0 · with-DB 5956/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165034
- radar-mirror-scope-port3: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-mirror-scope-port3` → `304a0b03`; code tip `671e0215`
- written by deploy-card.sh at 2026-10-26 15:49 ET (`date`); trial merge of the heads onto main in order: clean
