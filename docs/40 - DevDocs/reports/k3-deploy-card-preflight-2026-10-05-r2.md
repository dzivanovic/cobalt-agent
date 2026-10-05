# K3 deploy card preflight, round 2 (2026-10-05)

Card: `prompts/2026-10-05/51-deploy-k3-card.md`. Read-only. Every command was run on this seat; outputs quoted.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | 3c: card line 36 (RECORDS) | `Window: a feature deploys when READY at any hour (LAWS L43; his R389, the NOW line). Production has been down since R327; K3's restart … is a start. Residents are down before the merge (L66)…` The R327 window claim is gone; R327 appears only as the fact "down since" (lines 19, 36, 38), not as K3's window or skip. | OK |
| 1b | 3e: card line 8 `RULINGS: 2026-10-05 R412`; R376 only in line 34 as the seam's origin ("his R376; card `03`…"), not in RULINGS, not a window/skip | R376 no longer listed | OK |
| 1c | 3f: R390 only in line 38 ("one feature per deploy (his R390)…"), not in RULINGS, not a window/skip | R390 no longer listed | OK |
| 1d | `grep -n "^| R412 " reports/cto-2026-10-05.md` | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) from DEPLOY-HUB … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|` (HIS RULING and APPROVED) | OK |
| 1e | `git log -1 --format=%h -S"\| R412 " -- reports/cto-2026-10-05.md`; `git diff --stat -- <that file>` | `b3583b28`; diff empty (committed, clean) | OK |
| 1f | `grep -n "R327\|R368\|R376\|R390\|RULINGS"` on the card | RULINGS line 8 = R412 only; R368 appears nowhere; RECORDS lines 34/36/38 as above | OK |
| 2a | `rev-parse --verify 3e40359a^{commit}` | `3e40359ac99508105d7bed5dc849ca336f3bd1b3` | OK |
| 2b | `rev-parse --short=8 drc/k3-surfaces-1004` | `3e40359a` (head = TIP) | OK |
| 2c | `log --oneline 3e40359a..drc/k3-surfaces-1004 -- tests src configs ops`; `merge-base --is-ancestor 3e40359a drc/k3-surfaces-1004` | both empty, exit 0 | OK |
| 2d | `tail -n 1 reports/drc-k3-check-2026-10-04.md` | `CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · … held unfixed: 0 · … RESTARTS: com.cobalt.aset com.cobalt.radar · … ready: YES · …` | OK |
| 2e | `diff --stat -- <check report>`; `log -1 --format=%h -- <check report>` | empty; `a1c846ff` | OK |
| 3a | `rev-parse --verify deploy/deploy-k3-1005` | `fatal: Needed a single revision` | OK |
| 3b | `rev-parse --verify deploy-2026-10-05-k3` | `fatal: Needed a single revision` | OK |
| 3c | `ls /Users/cobalt/cobalt-wt/deploy-k3-1005` | `No such file or directory` | OK |
| 3d | `ls reports/deploy-deploy-k3-1005.md` | `No such file or directory` | OK |
| 4a | `grep -c -F "def superseded_stated_ids" src/cobalt/drc/store.py` (main) / `git grep -c` at `3e40359a` | `0` / `3e40359a:src/cobalt/drc/store.py:1` (before 0, after 1) | OK |
| 4b | `grep -c -F "CALENDAR_INPUT" src/cobalt/drc/build.py` (main) / at `3e40359a` | `0` / `3e40359a:src/cobalt/drc/build.py:2` (before 0, after 2) | OK |
| 4c | `ls tests/cobalt/test_drc_k3.py` (main) / `git show 3e40359a:` same path | `No such file or directory` / file content shown | OK |
| 4d | `git diff --stat main...3e40359a` | 20 files, 2590 insertions, 43 deletions: the 5 `docs/…/drc/*.md`, `reports/drc-k3-build-2026-10-04.md`, `src/cobalt/aset/{drc_page,web}.py`, `src/cobalt/drc/{build,cli,imports,store,units}.py`, 7 tests. Same 20 as the SHIPS row; classes on the card: six src `com.cobalt.aset,com.cobalt.radar`, `drc/cli.py` `com.cobalt.radar`, tests no resident, docs DOCS; RESTARTS `com.cobalt.aset com.cobalt.radar` = the check's line | OK |
| 5a | `grep -n "\| # \| branch"` in `prompts/CARD.md` and `ops/desk/deploy-card.sh` | `CARD.md:44` and `deploy-card.sh:207`, both `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|`; card row 1 has seven cells, last empty | OK |
| 5b | `02-deploy-s3-card.md` K3 line | `MIGRATIONS: none` (line 10), `SET: s3` (line 11); row 17 same branch, tips, check report, literals (six columns, the older shape, no fix cell). Card: `MIGRATIONS: none`, `SET: s3` | OK |
| 6a | `grep -c -F "«FILL"` on the card | `0` | OK |
| 6b | `diff --stat -- <card>`; `log -1 --format=%h -- <card>` | empty; `6a5e12ae` (committed, clean) | OK |

## ISSUES
- none
- Note (not a FAIL): the trial merge `main 3e40359a` → `6fdc7001` quoted at card line 36 was taken at main `57c7502c`; main has moved. It is git objects only, and the card's merge-by-reading line (merge-base `979ec797`) stands.

PREFLIGHT DONE · card: k3-deploy-51 · checks: 24 · fails: 0 · ready: YES
