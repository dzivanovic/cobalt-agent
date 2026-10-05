JOB: deploy-hub-text-1005
LADDER: OFF-LADDER — workflow set, cto-2026-10-05.md 2026-10-05 R387
BRANCH: deploy/deploy-hub-text-1005
WORKTREE: deploy-hub-text-1005
BASE: main
TIP: 2abb7d99
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-hub-text-1005.md
RULINGS: 2026-10-05 R412
TAG: deploy-2026-10-05-hub-text
MIGRATIONS: none
SET: workflow2

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/hub-text-1005` | `6b939b00` | `2abb7d99` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-check-2026-10-05.md` | `held unfixed: 0` and `ready: YES` |

Files it ships (`git -C /Users/cobalt/cobalt diff --stat main...ops/hub-text-1005`): `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/CHECK-HUB.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, and the build report `docs/40 - DevDocs/reports/hub-text-build-2026-10-05.md` (the one report commit `2abb7d99` after the code tip; docs only). RESTARTS: none (each file is `docs/**`, DOCS, no resident; check report RESTARTS table). No `ops/desk/` script and no `src/` path is in the diff.

## MARKERS
- `grep -c -F "No restart window binds a deploy (L43, his R389)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "each feature deploys alone on its existing check (his R390)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "first runs the gate on the merged hub text" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "(L75, his R376)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`
- `grep -c -F "desk-context.sh <your session id>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `1`
- `grep -c -F "(d2)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `2` · after `0`

## SMOKE READS
- no restart window binds a deploy (F1) · `grep -c -F "No restart window binds a deploy (L43, his R389)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · exit 0, a count of 1 or more
- one feature per deploy (F2) · `grep -c -F "each feature deploys alone on its existing check (his R390)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · exit 0, a count of 1 or more
- small fix by the original builder (F3) · `grep -c -F "(L75, his R376)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · exit 0, a count of 1 or more
- MEASURE token source (F4) · `grep -c -F "desk-context.sh <your session id>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · exit 0, a count of 1 or more

## RECORDS
- hub-text: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-text-check-2026-10-05.md` last line: CHECK DONE · job: hub-text · pass: 1 · tip: 6b939b00 · house A: none (overruled 2026-10-05 R412) · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 1 · for Dejan: 0
- hub-text: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-text-1005` → `2abb7d99`; code tip `6b939b00`
- G (d2): per the sibling cards' RECORDS wording on its state at deploy time; no Grok read (R412).
- `DEPLOY-HUB.md` is among the shipped files: its one read by another house is overruled for this set by his R412.
