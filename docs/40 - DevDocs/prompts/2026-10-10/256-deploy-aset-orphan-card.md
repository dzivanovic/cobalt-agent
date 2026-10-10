JOB: aset-orphan-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R853
BRANCH: deploy/aset-orphan-1010
WORKTREE: deploy-aset-orphan-1010
BASE: main
TIP: f72dbb9a
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-aset-orphan-1010.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-10-aset-orphan
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/aset-orphan-1010` | `1987849b` | `f72dbb9a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/aset-orphan-check-2026-10-10.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset' /Users/cobalt/cobalt/ops/start_aset.sh` · before `0` · after `1` (row A: the start script execs the python itself)
- DEPLOY PROOF (job card `222`): after 4.2 `ps -p <old aset pid>` → header only; after 4.6 `launchctl print gui/501/com.cobalt.aset` → `state = running`, same pid read again after the smoke

## SMOKE READS
- the start script's direct exec line · `grep -c -F 'exec "$REPO_ROOT/.venv/bin/python" -m cobalt.aset' /Users/cobalt/cobalt/ops/start_aset.sh` · exit 0, a count of 1 or more

## RECORDS
- aset-orphan-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/aset-orphan-check-2026-10-10.md` last line: CHECK DONE · job: aset-orphan-1010 · pass: 1 · tip: 1987849b · house A: Sol FINDINGS: 1 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: Gemini FINDINGS: 5 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset · files opened: 13 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 163668
- aset-orphan-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/aset-orphan-1010` → `f72dbb9a`; code tip `1987849b`
- written by deploy-card.sh at 2026-10-10 11:29 ET (`date`); trial merge of the heads onto main in order: clean
