JOB: cos-probe-fr1
LADDER: S5-P3 · F20
BRANCH: deploy/cos-probe-fr1
WORKTREE: deploy-cos-probe-fr1
BASE: main
TIP: da47500a
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-probe-fr1.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-20-cos-probe-fr1
MIGRATIONS: none
SET: cos-probe
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/cos-probe-fr1` | `da47500a` | `da47500a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr1-check-2026-10-20.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/src/cobalt/cos/probe.py` · before `ls: /Users/cobalt/cobalt/src/cobalt/cos/probe.py: No such file or directory` · after `/Users/cobalt/cobalt/src/cobalt/cos/probe.py`
- `grep -c -F "def test_x20_redact_keeps_the_card_fragment_key" /Users/cobalt/cobalt/tests/cobalt/test_hitl_offline.py` · before `0` · after `1`
- probe mounted · `grep -c -F 'csub.add_parser("probe"' /Users/cobalt/cobalt/src/cobalt/cos/cli.py` · before `0` · after `1` (replaces `uv run cobalt cos probe --help`, which the deploy hub's launch line does not admit; the mount itself is pinned by `test_cos_probe.py::test_the_probe_is_mounted_and_lists_the_seven_items` in the offline suite above)

## SMOKE READS
(No suite line here: `deploy-smoke.sh` `shape()` maps only `ls`, `grep -c -F`, `curl` and `db query`, so a `uv run pytest` line is RED `no mapped shape`; STEP-G runs the suites, and the markers above prove the files landed.)

## RECORDS
- cos-probe-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-probe-fr1-check-2026-10-20.md` last line: CHECK DONE · job: cos-probe-fr1 · pass: 1 · tip: da47500a · house A: Grok FINDINGS: 7 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 6 · house B: none available · suites: offline 8959/0 · with-DB 5858/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 181890
- cos-probe-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-probe-fr1` → `da47500a`; code tip `da47500a`
- house B: none seated (`HOUSE B: as needed`); the check's own record says so (RECORDS: "House B: not seated"); desk reading: the set is a probe CLI under `src/cobalt/cos/` plus tests, no daily-note writer.
- written by deploy-card.sh at 2026-10-20 11:58 ET (`date`); trial merge of the heads onto main in order: clean
