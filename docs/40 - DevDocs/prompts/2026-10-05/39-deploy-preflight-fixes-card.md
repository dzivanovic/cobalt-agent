JOB: deploy-preflight-fixes-1005
LADDER: OFF-LADDER — workflow set, cto-2026-10-05.md 2026-10-05 R387
BRANCH: deploy/deploy-preflight-fixes-1005
WORKTREE: deploy-preflight-fixes-1005
BASE: main
TIP: 0af97be7
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-preflight-fixes-1005.md
RULINGS: 2026-10-05 R412
TAG: deploy-2026-10-05-preflight-fixes
MIGRATIONS: none
SET: workflow2

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/preflight-fixes-1005` | `0af97be7` | `0af97be7` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/preflight-fixes-check-2026-10-05.md` | `held unfixed: 0` and `ready: YES` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/preflight-fixes-1005`): `ops/desk/preflight.sh`, `tests/ops/test_preflight.py`, `tests/ops/test_desk_launch_brain.py`, and the build report under `docs/`. RESTARTS: none (operator script, tests, docs; check report RESTARTS table). No hub file is in the diff.

## MARKERS
- `grep -c -F "card 20 F2" /Users/cobalt/cobalt/ops/desk/preflight.sh` · before `0` · after `2`
- `grep -c -F "card 20 F1" /Users/cobalt/cobalt/ops/desk/preflight.sh` · before `0` · after `2`
- `grep -c -F "(recorded)" /Users/cobalt/cobalt/ops/desk/preflight.sh` · before `0` · after `2`

## SMOKE READS
- pass-2 head reference (F2) · `grep -c -F "card 20 F2" /Users/cobalt/cobalt/ops/desk/preflight.sh` · exit 0, a count of 1 or more
- self-check count recorded (F1) · `grep -c -F "(recorded)" /Users/cobalt/cobalt/ops/desk/preflight.sh` · exit 0, a count of 1 or more

## RECORDS
- preflight-fixes: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/preflight-fixes-check-2026-10-05.md` last line: CHECK DONE · job: preflight-fixes · pass: 1 · tip: 0af97be7 · house A: none (overruled 2026-10-05 R412) · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0
- preflight-fixes: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/preflight-fixes-1005` → `0af97be7`; code tip `0af97be7`
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
