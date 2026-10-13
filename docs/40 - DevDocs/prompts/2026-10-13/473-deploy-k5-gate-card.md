JOB: k5-gate-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1310, R1311, R1316
BRANCH: deploy/k5-gate-1013
WORKTREE: deploy-k5-gate-1013
BASE: main
TIP: 56472a30
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-k5-gate-1013.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-13-k5-gate
MIGRATIONS: none
SET: radar
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/k5-gate-1013` | `5b3c525b` | `56472a30` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/k5-gate-check-2026-10-13.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · before `0` · after `1`
- `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "card 446" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/ops/test_the_rule_sweep.py` · before `absent` · after `present`

## SMOKE READS
- 304 passes THE RULE (census, the desk's next step after this deploy and after row CR, not a gate of this set) · `sh /Users/cobalt/.claude/ops/deploy-card.sh` with the desk's own `--job`, `--set`, `--worktree`, `--tag` and `--out`, then `--fix-report "f4-refresh-1010=/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md" "<the 304 job card>"` · green: `deploy-card: … written (1 job(s), …)`, its SHIPS row literals `` `held unfixed: 2` and `ready: NO` ``; the check report and the fix report unchanged

## RECORDS
- k5-gate-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/k5-gate-check-2026-10-13.md` last line: CHECK DONE · job: k5-gate-1013 · pass: 1 · tip: 5b3c525b · house A: Grok FINDINGS: 1 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 228916
- k5-gate-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/k5-gate-1013` → `56472a30`; code tip `5b3c525b`
- written by deploy-card.sh at 2026-10-13 07:33 ET (`date`); trial merge of the heads onto main in order: clean
