JOB: deploy-launcher-fixround-1005
LADDER: OFF-LADDER — workflow set, cto-2026-10-05.md 2026-10-05 R387
BRANCH: deploy/deploy-launcher-fixround-1005
WORKTREE: deploy-launcher-fixround-1005
BASE: main
TIP: a545a4d8
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-launcher-fixround-1005.md
RULINGS: 2026-10-05 R412
TAG: deploy-2026-10-05-launcher-fixround
MIGRATIONS: none
SET: workflow2

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/launcher-fixround-1005` | `a545a4d8` | `a545a4d8` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-05-r2.md` | `held unfixed: 0` and `ready: YES` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/launcher-fixround-1005`, 8 files), each with its RESTARTS class (check report `## Suites`, `jobs restarts 5fb0ddf5..HEAD` at `a545a4d8`): `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh` (each: operator script; no Cobalt reader); `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py` (each: test/documentation; no resident); `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, and the builder's report `docs/40 - DevDocs/reports/launcher-fixround-build-2026-10-05.md` (each: DOCS). RESTARTS: none. No `src/` path is in the diff. The head is the code tip: `git -C /Users/cobalt/cobalt log --oneline a545a4d8..ops/launcher-fixround-1005 -- tests ops configs src` prints nothing, and `rev-parse` gives `a545a4d8d424c72df46d86c240b7484427f0cad2` for the branch.

## MARKERS
- `grep -c -F "is not committed and unmodified" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `0` · after `1`
- `grep -c -F "Fix-round row" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "On a fix-round row (a small fix after the check, his R376, L75)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · before `0` · after `1`
- `grep -c -F "| fix report |" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · before `0` · after `1`

## SMOKE READS
- STEP-0 P2 fix-round clause (F2, check O1r2) · `grep -c -F "is not committed and unmodified" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · exit 0, a count of 1 or more
- hub fix-round line (F3) · `grep -c -F "Fix-round row" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · exit 0, a count of 1 or more
- CARD.md fix-round wording (F4) · `grep -c -F "On a fix-round row (a small fix after the check, his R376, L75)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md"` · exit 0, a count of 1 or more
- `fix report` column in deploy-card.sh (F1) · `grep -c -F "| fix report |" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · exit 0, a count of 1 or more

## RECORDS
- launcher-fixround: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-checks-check-2026-10-05-r2.md` last line: CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3786/0 · with-DB 857/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 152813
- launcher-fixround: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-fixround-1005` → `a545a4d8`; code tip `a545a4d8` (the check's own fix on top of the build's `dc2a80b4`; BASE `5fb0ddf5`)
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- `DEPLOY-HUB.md` is among the shipped files (one inserted line after P2, the F3 hub line). Card 41 deployed first (`1ff72b72`), so main's `DEPLOY-HUB.md` differs from this branch's merge base `5fb0ddf5`. The deploy merges main into the tree and that merge is clean, proved by reading, not running: `git -C /Users/cobalt/cobalt diff 5fb0ddf5 main -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` changes lines 26, 50, 57 (P1), 74, 93, 101, 134, 178, 181 of the base; the branch's diff (`git diff 5fb0ddf5 a545a4d8`) is one insertion after line 58 (P2), which main leaves unchanged. The nearest main hunk is the P1 line 57, one unchanged line (58) away; the hunks do not touch, so git merges them without a conflict.
- The fix-round column (`fix report`) is added by this deploy, so `## SHIPS` carries main's six columns; the row needs no fix report because the check's `tip:` equals the code tip `a545a4d8`.
- OWED, a later card, not part of this deploy (the check's DECISIONS 1): `DEPLOY-HUB.md:58` (P2) says the literals are those "the row's last column names"; on the seven-column `## SHIPS` shape the last column is `fix report`, and the literals are in `its stop line must carry`, the column before it (`CARD.md:47` and the scripts read that column). One-phrase hub fix: "the `its stop line must carry` column".
