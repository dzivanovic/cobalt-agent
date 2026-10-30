JOB: launcher-tip-prefix
LADDER: OFF-LADDER — reports/cto-2026-10-29.md R2571
BRANCH: deploy/launcher-tip-prefix
WORKTREE: deploy-launcher-tip-prefix
BASE: main
TIP: 3a6c1bfa
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-launcher-tip-prefix.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-29-launcher-tip-prefix
MIGRATIONS: none
SET: launcher-tip-prefix
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/launcher-tip-prefix` | `2da6759e` | `3a6c1bfa` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-tip-prefix-check-2026-10-29.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.md` |

## MARKERS
- `grep -c -F "card 1085" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after the count the builder quotes from its `TIP` (at least `1`)
- `grep -c -F "card 1085" /Users/cobalt/cobalt/ops/desk/preflight.sh` · before `0` · after the count the builder quotes from its `TIP` (at least `1`)
- `grep -c -F "test_1085" /Users/cobalt/cobalt/tests/ops/test_desk_launch_prechecks.py` · before `0` · after the count the builder quotes from its `TIP` (at least `4`)
- `grep -c -F "test_1085" /Users/cobalt/cobalt/tests/ops/test_preflight.py` · before `0` · after the count the builder quotes from its `TIP` (at least `1`)

## SMOKE READS
- ONE SMOKE READ after the merge: `uv run pytest -q -p no:cacheprovider tests/ops/test_desk_launch_prechecks.py tests/ops/test_preflight.py` → `0 failed`.
- AFTER DEPLOYED, the desk's: `sh /Users/cobalt/.claude/ops/desk-launch.sh install-ops` once (card 580); its last line quoted: `0 linked` (both scripts are linked already, symlinks into `/Users/cobalt/cobalt/ops/desk/`), and `grep -c -F "card 1085" /Users/cobalt/.claude/ops/desk-launch.sh` prints at least `1`. The first real check launch on a 9-hex build stop line is the live proof (L81 (3)); a refusal the desk did not expect is a `## RECORDS` line, never routed around.

## RECORDS
- launcher-tip-prefix: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-tip-prefix-build-2026-10-29.md` at `3a6c1bfa` last line: BUILT · job: launcher-tip-prefix · tip: 2da6759e | on 4f1c991f | migration: none | offline 9185/0 | with-DB 0/0 | live-note 148/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 106862
- launcher-tip-prefix: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-tip-prefix-check-2026-10-29.md` last line: CHECK DONE · job: launcher-tip-prefix · pass: 1 · tip: 5babf712 · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none available · suites: offline 9181/1 · with-DB 0/0 · live-note 148/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 2 · for Dejan: 0 · tokens: 163970
- launcher-tip-prefix: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-tip-prefix` → `3a6c1bfa`; code tip `2da6759e`
- written by deploy-card.sh at 2026-10-29 22:34 ET (`date`); trial merge of the heads onto main in order: clean
