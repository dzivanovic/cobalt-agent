JOB: cos-env-load
LADDER: S5-P3 · F20
BRANCH: deploy/cos-env-load
WORKTREE: deploy-cos-env-load
BASE: main
TIP: 773fe012
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-env-load.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-21-cos-env-load
MIGRATIONS: none
SET: cos-env-load
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/cos-env-load` | `5b813fa4` | `773fe012` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-env-load-check-2026-10-21.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "ENV_FILE = Path(__file__)" /Users/cobalt/cobalt/src/cobalt/cos/run.py` · before `0` · after `1`
- `grep -c -F "load_dotenv(ENV_FILE)" /Users/cobalt/cobalt/src/cobalt/cos/run.py` · before `0` · after `1`
- `grep -c -F "def test_e1_a_launchd_start_reads_the_repo_env_file" /Users/cobalt/cobalt/tests/cobalt/test_cos_env_load.py` · before `0` · after `1`

## SMOKE READS
- the cos module is on the tree · `ls /Users/cobalt/cobalt/src/cobalt/cos/run.py` · exit 0, listed
- cos stays owed, not bootstrapped by this deploy · `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/data/deploy/bootstrap-owed.json` · exit 0, `1`

## RECORDS
- cos-env-load: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-env-load-check-2026-10-21.md` last line: CHECK DONE · job: cos-env-load · pass: 1 · tip: 5b813fa4 · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9076/0 · with-DB 5922/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.cos com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 189692
- cos-env-load: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-env-load` → `773fe012`; code tip `5b813fa4`
- written by deploy-card.sh at 2026-10-21 20:06 ET (`date`); trial merge of the heads onto main in order: clean
