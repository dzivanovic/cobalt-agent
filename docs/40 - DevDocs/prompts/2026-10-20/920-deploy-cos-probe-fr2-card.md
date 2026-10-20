JOB: cos-probe-fr2
LADDER: S5-P2 · F20
BRANCH: deploy/cos-probe-fr2
WORKTREE: deploy-cos-probe-fr2
BASE: main
TIP: dfea631a
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-probe-fr2.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-20-cos-probe-fr2
MIGRATIONS: none
SET: cos-probe
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/cos-probe-fr2` | `dfea631a` | `dfea631a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr2-check-2026-10-20.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "under the scratch HOME" /Users/cobalt/cobalt/src/cobalt/cos/probe.py` · before `1` · after `0`
- `grep -c -F ".claude.json" /Users/cobalt/cobalt/src/cobalt/cos/probe.py` · before `2` · after `0`
- `grep -c -F "def test_auth_runs_under_the_real_home_and_a_login_there_passes" /Users/cobalt/cobalt/tests/cobalt/test_cos_probe.py` · before `0` · after `1`
- `grep -c -F "## 2026-10-20 — cos-probe-fr2" "/Users/cobalt/cobalt/docs/40 - DevDocs/cobalt/cos/README.md"` · before `0` · after `1`

## SMOKE READS
(No suite line here: `deploy-smoke.sh` `shape()` maps only `ls`, `grep -c -F`, `curl` and `db query`, so a `uv run pytest` line is RED `no mapped shape`; the gate's offline suite covers the probe tests.)

## RECORDS
- cos-probe-fr2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr2-check-2026-10-20.md` last line: CHECK DONE · job: cos-probe-fr2 · pass: 1 · tip: dfea631a · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8970/0 · with-DB 5869/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 178055
- cos-probe-fr2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-probe-fr2` → `dfea631a`; code tip `dfea631a`
- written by deploy-card.sh at 2026-10-20 14:46 ET (`date`); trial merge of the heads onto main in order: clean
