JOB: f5-probe
LADDER: S5-P2 · F5
BRANCH: deploy/f5-probe
WORKTREE: deploy-f5-probe
BASE: main
TIP: a25a4f91
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f5-probe.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-f5-probe
MIGRATIONS: none
SET: f5-probe
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f5-probe` | `a25a4f91` | `a25a4f91` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-check-2026-10-21.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` · before `ls: /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py: No such file or directory` · after `/Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py`
- `grep -c -F "PROBE_ITEMS = (" /Users/cobalt/cobalt/src/cobalt/prefill/checkpoints.py` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/cobalt/test_checkpoint_probe.py` · before `ls: /Users/cobalt/cobalt/tests/cobalt/test_checkpoint_probe.py: No such file or directory` · after `/Users/cobalt/cobalt/tests/cobalt/test_checkpoint_probe.py`

## SMOKE READS
- the probe module is on the restarted tree · `ls /Users/cobalt/cobalt/src/cobalt/prefill/checkpoint_probe.py` · exit 0, listed
- checkpoint plists stay on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` · exit 0, listed

## RECORDS
- f5-probe: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-probe-check-2026-10-21.md` last line: CHECK DONE · job: f5-probe · pass: 1 · tip: a25a4f91 · house A: Grok FINDINGS: 6 · findings: 7 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 5 · house B: none available · suites: offline 9070/0 · with-DB 5916/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 211581
- f5-probe: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-probe` → `a25a4f91`; code tip `a25a4f91`
- written by deploy-card.sh at 2026-10-21 14:26 ET (`date`); trial merge of the heads onto main in order: clean
