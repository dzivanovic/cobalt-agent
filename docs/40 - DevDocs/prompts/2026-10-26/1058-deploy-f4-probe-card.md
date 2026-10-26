JOB: f4-probe
LADDER: S5-P2 · F4
BRANCH: deploy/f4-probe
WORKTREE: deploy-f4-probe
BASE: main
TIP: 07b507f9
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f4-probe.md
RULINGS: none
TAG: deploy-2026-10-26-f4-probe
MIGRATIONS: none
SET: f4-probe
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f4-probe` | `150296da` | `07b507f9` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-probe-check-2026-10-26.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py` · before `ls: /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py: No such file or directory` · after `/Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py`
- `grep -c -F "PROBE_ITEMS = (" /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py` · before `0` · after `1`
- `grep -c -F "test_x7_the_daymode_unit_still_starts_as_of_after_a_later_daymode_write" /Users/cobalt/cobalt/tests/cobalt/test_prefill_refresh.py` · before `0` · after `1`

## SMOKE READS
- the probe module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/prefill/refresh_probe.py` · exit 0, listed
- the refresh plist stays on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` · exit 0, listed

## RECORDS
- f4-probe: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-probe-check-2026-10-26.md` last line: CHECK DONE · job: f4-probe · pass: 1 · tip: 150296da · house A: Grok FINDINGS: 0 · findings: 7 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9131/0 · with-DB 5967/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 26 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 208781
- f4-probe: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-probe` → `07b507f9`; code tip `150296da`
- written by deploy-card.sh at 2026-10-26 10:53 ET (`date`); trial merge of the heads onto main in order: clean
