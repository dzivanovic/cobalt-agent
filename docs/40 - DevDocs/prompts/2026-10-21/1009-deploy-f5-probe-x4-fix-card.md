JOB: f5-probe-x4-fix
LADDER: S5-P2 · F5
BRANCH: deploy/f5-probe-x4-fix
WORKTREE: deploy-f5-probe-x4-fix
BASE: main
TIP: 820a8f21
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f5-probe-x4-fix.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-f5-probe-x4-fix
MIGRATIONS: none
SET: f5-probe-x4-fix
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f5-probe-x4-fix` | `8525c6f7` | `820a8f21` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-x4-fix-check-2026-10-21.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "def _at_repo" /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` · before `0` · after `1`
- `grep -c -F "X4_GROUPS_KEPT = " /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` · before `0` · after `1`
- `grep -c -F "def test_fr3_x4_reaches_no_finviz" /Users/cobalt/cobalt/tests/cobalt/test_checkpoint_probe.py` · before `0` · after `1`

## SMOKE READS
- the probe module is on the restarted tree · `ls /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` · exit 0, listed
- checkpoint plists stay on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` · exit 0, listed

## RECORDS
- f5-probe-x4-fix: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-x4-fix-check-2026-10-21.md` last line: CHECK DONE · job: f5-probe-x4-fix · pass: 1 · tip: 8525c6f7 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9078/0 · with-DB 5924/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 177591
- f5-probe-x4-fix: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-probe-x4-fix` → `820a8f21`; code tip `8525c6f7`
- written by deploy-card.sh at 2026-10-21 20:46 ET (`date`); trial merge of the heads onto main in order: clean
