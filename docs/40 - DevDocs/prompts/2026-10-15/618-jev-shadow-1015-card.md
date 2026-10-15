JOB: jev-shadow-1015
LADDER: OFF-LADDER — reports/cto-2026-10-15.md R1467, R1532, R1535
BRANCH: deploy/jev-shadow-1015
WORKTREE: deploy-jev-shadow-1015
BASE: main
TIP: 5316fafe
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-jev-shadow-1015.md
RULINGS: 2026-10-15 R1532 R1535
TAG: deploy-2026-10-15-jev-shadow
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `feat/jev-shadow-1015` | `5316fafe` | `5316fafe` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/src/cobalt/classify/route.py` · before `No such file or directory` · after `/Users/cobalt/cobalt/src/cobalt/classify/route.py`
- `ls /Users/cobalt/cobalt/configs/cobalt/classify/route.yaml` · before `No such file or directory` · after `/Users/cobalt/cobalt/configs/cobalt/classify/route.yaml`
- `ls /Users/cobalt/cobalt/src/cobalt/classify/collector.py` · before `No such file or directory` · after `/Users/cobalt/cobalt/src/cobalt/classify/collector.py`
- `grep -c -F "'openrouter_api_key': 'api_key'" /Users/cobalt/cobalt/src/cobalt_agent/config.py` · before `1` · after `0`
- `grep -c -F "spend_ledger:" /Users/cobalt/cobalt/configs/cobalt/classify/trial.yaml` · before `No such file or directory` · after `1`

## SMOKE READS
- SMOKE READ, no marker (ASK DESK 19; outside `/Users/cobalt/cobalt`): `ls /Users/cobalt/.cobalt/classify` → `No such file or directory` (the deploy makes no keyed call and writes no ledger).
- ONE SMOKE READ after the merge: `uv run pytest -q tests/cobalt/test_jev_shadow_1015.py` → `0 failed`; and `uv run cobalt classify route --card "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" --dry-run` → one `ROUTE DRY` line and `cards=1 calls=1`, zero network.
- RESTARTS at the deploy: the table R2 derives (the check derived `com.cobalt.agent com.cobalt.aset com.cobalt.radar`): the old agent restarts with no OpenRouter key in its config (R1535), Z0 having found no running service on `openrouter` (brain 0e848919, 2026-10-15). The `openrouter_api_key` marker's `after 0` holds only because Z0 found none; a Z0 STOP means this card does not deploy. JEV O2: 591 deploys now; FR-O2 (build cards only) in fix round jev-shadow-fr1, no re-check; no keyed batch before FR-O2 is deployed — brain 0e848919 10-15.

## RECORDS
- jev-shadow-1015: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/jev-shadow-check-2026-10-15.md` last line: CHECK DONE · job: jev-shadow-1015 · pass: 1 · tip: 5316fafe · house A: grok FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8307/0 · with-DB 5471/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 3 · for Dejan: 1 · tokens: 329407
- jev-shadow-1015: head `git -C /Users/cobalt/cobalt rev-parse --short=8 feat/jev-shadow-1015` → `5316fafe`; code tip `5316fafe`
- written by deploy-card.sh at 2026-10-15 17:27 ET (`date`); trial merge of the heads onto main in order: clean
