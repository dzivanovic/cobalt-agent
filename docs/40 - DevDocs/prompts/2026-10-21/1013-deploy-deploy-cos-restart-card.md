JOB: deploy-cos-restart
LADDER: OFF-LADDER — reports/cto-2026-10-21.md R2355
BRANCH: deploy/deploy-cos-restart
WORKTREE: deploy-deploy-cos-restart
BASE: main
TIP: 3770387d
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-cos-restart.md
RULINGS: 2026-10-18 R1863, 2026-10-20 R2240
TAG: deploy-2026-10-22-deploy-cos-restart
MIGRATIONS: none
SET: deploy-cos-restart
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/deploy-cos-restart` | `3770387d` | `3770387d` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-restart-check-2026-10-21.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "Bash(launchctl bootout gui/501/com.cobalt.cos)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "Bash(launchctl kickstart -k gui/501/com.cobalt.cos)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `1` · after `0`
- `grep -c -F "Bash(launchctl kickstart -k gui/501/com.cobalt.cos)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md"` · before `0` · after `1`
- `grep -c -F "(a cos outside it is not read)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "— cos: <UP|DOWN>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "cos: DOWN" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`

## SMOKE READS
- the cos plist the bootstrap string names is on the tree · `ls /Users/cobalt/cobalt/ops/com.cobalt.cos.plist` · exit 0, listed
- the admit test is on the tree · `grep -c -F "def test_f2_a_loaded_running_cos_is_admitted_at_step_r" /Users/cobalt/cobalt/tests/ops/test_deploy_cos_restart_1021.py` · exit 0, `1`

## RECORDS
- deploy-cos-restart: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-restart-check-2026-10-21.md` last line: CHECK DONE · job: deploy-cos-restart · pass: 1 · tip: 3770387d · house A: Grok FINDINGS: 5 · findings: 9 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 9094/0 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 216150
- deploy-cos-restart: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-cos-restart` → `3770387d`; code tip `3770387d`
- written by deploy-card.sh at 2026-10-22 01:26 ET (`date`); trial merge of the heads onto main in order: clean
