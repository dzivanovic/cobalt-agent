# hub-text deploy card 41 — preflight (2026-10-05)

Card: `prompts/2026-10-05/41-deploy-hub-text-card.md`. Read only; every command run by this seat.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git rev-parse --verify 6b939b00^{commit}` | `6b939b0068826ce8c8793d06a7c41147f044f43f` | OK |
| 1b | `git diff --stat 6b939b00..ops/hub-text-1005` | one file: `reports/hub-text-build-2026-10-05.md`, 205 insertions | OK |
| 1c | `git merge-base --is-ancestor 6b939b00 ops/hub-text-1005`; `rev-parse --short=8 ops/hub-text-1005` | exit 0; `2abb7d99` | OK |
| 1d | `tail -n 3` of the check report | last line `CHECK DONE · job: hub-text · pass: 1 · tip: 6b939b00 · … · held unfixed: 0 · … · ready: YES · …` | OK |
| 1e | `git log -1 --format=%h -- hub-text-check-2026-10-05.md` | `fb339571` | OK |
| 2a | `rev-parse --verify deploy/deploy-hub-text-1005` | `fatal: Needed a single revision` (new) | OK |
| 2b | `rev-parse --verify refs/tags/deploy-2026-10-05-hub-text` | `fatal: Needed a single revision` (new) | OK |
| 2c | `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1005` | `No such file or directory` (new) | OK |
| 2d | `ls …/reports/deploy-deploy-hub-text-1005.md` | `No such file or directory` (new) | OK |
| 3 | `grep -n "^| R412 " reports/cto-2026-10-05.md` | line 109: `HIS RULING: drop pre-merge (d2) …` · `APPROVED (in cto-desk-contract.md …; launch gate L7a)`; `git log -1 --format=%h` of the file: `0b09b2b7` | OK |
| 4a | marker 1 on main (`No restart window binds a deploy (L43, his R389)`, DEPLOY-HUB) | `0`; after at `6b939b00`: `1` | OK |
| 4b | marker 2 (`each feature deploys alone on its existing check (his R390)`) | `0`; after `1` | OK |
| 4c | marker 3 (`first runs the gate on the merged hub text`) | `0`; after `1` | OK |
| 4d | marker 4 (`(L75, his R376)`, CHECK-HUB) | `0`; after `1` | OK |
| 4e | marker 5 (`desk-context.sh <your session id>`, BUILD-HUB) | `0`; after `1` | OK |
| 4f | marker 6 (`(d2)`, DEPLOY-HUB) | `2`; after `0` | OK |
| 4g | smoke reads F1–F4 are the same four commands as markers 1, 4, 5 and 2 | after counts 1, 1, 1, 1 (≥1) | OK |
| 4h | `git diff --stat main...6b939b00` | BUILD-HUB, CHECK-HUB, DEPLOY-HUB only (3 files, 15+/17−); `main...ops/hub-text-1005` adds the build report (4 files). The SHIPS row lists exactly these; all are `docs/**`, check says `RESTARTS: none`; no `ops/desk/` or `src/` path | OK |
| 5a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 5b | shape vs `CARD.md` deploy header and sibling card 39 | all deploy keys present, body order SHIPS, MARKERS, SMOKE READS, RECORDS (no READ-BACK, MIGRATIONS none), same shape as 39. One difference: header `TIP: 6b939b00` | FAIL (see ISSUES 1) |
| 6a | `git diff --stat -- <card>` | empty | OK |
| 6b | `git log -1 --format=%h -- <card>` | `0b09b2b7` | OK |

## ISSUES
1. `TIP` header is `6b939b00` (code tip); `CARD.md` says deploy `TIP` is every branch HEAD the gate merges, and the SHIPS row gives that head as `2abb7d99`. Sibling card 39 can't show this (its head equals its tip). Desk decides: set `TIP: 2abb7d99`, or confirm the gate merges the code tip. Merging `6b939b00` would leave the build report out, though `main...ops/hub-text-1005` lists it.

PREFLIGHT DONE · card: hub-text-deploy-41 · checks: 24 · fails: 1 · ready: NO
