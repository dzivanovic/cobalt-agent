# card 39 deploy card — preflight, 2026-10-06

Card `prompts/2026-10-06/45-deploy-card-39-card.md` · job `deploy-drc-d5-o1-b2-1006` · branch `ops/drc-d5-o1-b2-1006`. Read-only. (`git -C` = `git -C /Users/cobalt/cobalt`; AFTER counts read in the clean worktree `/Users/cobalt/cobalt-wt/drc-d5-o1-b2-1006`, `src/` = branch head.)

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C … rev-parse --verify 38e0d47e^{commit}` | `38e0d47e0063f18866442d607bdf44cd0d123b9b` | OK |
| 2 | `git -C … rev-parse --short=8 ops/drc-d5-o1-b2-1006` (card TIP = branch head) | `38e0d47e` | OK |
| 3 | `git -C … merge-base --is-ancestor edd4d584 ops/drc-d5-o1-b2-1006` | exit 0, no output | OK |
| 4 | `git -C … diff --stat edd4d584..ops/drc-d5-o1-b2-1006` | one file: `reports/drc-d5-o1-b2-build-2026-10-06.md` (89+, 4-); no `src`, `tests`, `configs`, `ops` | OK |
| 5 | `git -C … diff --stat main...ops/drc-d5-o1-b2-1006` | 13 files, 527 insertions, 20 deletions: 5 docs/drc md, build report, `build.py`, `imports.py`, `reconcile.py`, `store.py`, `units.py`, `test_drc_d5.py`, `test_drc_d5_db.py` = the card's list | OK |
| 6 | `tail -n 3` of check report | last line `CHECK DONE · job: drc-d5-o1-b2 · pass: 1 · tip: 9be877dc · … held unfixed: 1 · … ready: NO · …` | OK |
| 7 | `tail -n 3` of build (fix) report | last line `BUILT · job: drc-d5-o1-b2 · tip: edd4d584 \| on 4d9e451c \| … rows: 4 of 4 …` | OK |
| 8 | check report committed, clean: `log -1 --format=%h --` / `diff --stat --` | `9b8786ae` / empty | OK |
| 9 | fix report committed, clean | `e2461938` / empty | OK |
| 10 | `merge-base --is-ancestor 9be877dc edd4d584` | exit 0 | OK |
| 11 | `diff --stat edd4d584 38e0d47e -- . ":(exclude)docs"` | empty | OK |
| 12 | BEFORE `grep -c -F "_open_items"` main `store.py` | `0` (card: 0) | OK |
| 13 | BEFORE `"then refused"` main `reconcile.py` | `0` (card: 0) | OK |
| 14 | BEFORE `"kept = derived_day"` main `build.py` | `0` (card: 0) | OK |
| 15 | BEFORE `"def _items(rows"` main `imports.py` | `0` (card: 0) | OK |
| 16 | AFTER `_open_items` worktree `store.py` | `3` (card: 3) | OK |
| 17 | AFTER `then refused` worktree `reconcile.py` | `1` (card: 1) | OK |
| 18 | AFTER `kept = derived_day` worktree `build.py` | `1` (card: 1) | OK |
| 19 | AFTER `def _items(rows` worktree `imports.py` | `1` (card: 1) | OK |
| 20 | `rev-parse --verify deploy/deploy-drc-d5-o1-b2-1006` | `fatal: Needed a single revision` (absent) | OK |
| 21 | `rev-parse --verify deploy-2026-10-06-drc-d5-o1-b2` | `fatal: Needed a single revision` (absent) | OK |
| 22 | `ls /Users/cobalt/cobalt-wt/deploy-drc-d5-o1-b2-1006` | `No such file or directory` | OK |
| 23 | `ls` REPORT `reports/deploy-deploy-drc-d5-o1-b2-1006.md` | `No such file or directory` | OK |
| 24 | `grep -c -F "«FILL"` card | `0` | OK |
| 25 | card committed: `log -1 --format=%h -- <card>` | `b055be71` | OK |
| 26 | card clean: `diff --stat -- <card>` | empty | OK |
| 27 | R326 `cto-2026-10-03.md:332` | `HIS RULING · APPROVED`; file not in `git status` (committed, clean) | OK |
| 28 | R412 `cto-2026-10-05.md:109` | `APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a)` | OK |
| 29 | R474 `cto-2026-10-05.md:140` | `HIS RULING · APPROVED` | OK |
| 30 | RESTARTS home for every shipped path: build report `## RESTARTS` (`:16-34`) vs check 5 | 13 rows = the 13 shipped files: 5 `src/cobalt/drc/*` `static import reach` → `com.cobalt.aset,com.cobalt.radar`; 2 tests `test/documentation; no resident`; 6 `DOCS`; no `UNCLASSIFIED` | OK |
| 31 | launcher `ops/desk/desk-launch.sh:813-868` read against the card (see below) | P3 head in TIP, both literals match, `fixed_ok` passes, head adds docs only | OK |
| 32 | MIGRATIONS/SET: card `none`/`none`; precedent flake-fix-2 card has `MIGRATIONS: none`, `SET: none`; no migration file, no `ops/` path in check 5 | same values | OK |

### Check 31 detail (launcher, quoted)
- `:813-815` `case " $tip " in *" $shead "*) ;;` — TIP `38e0d47e`, SHIPS head `38e0d47e` → OK.
- `:830-834` literals `held unfixed: 1` and `ready: NO` each matched by `*"$lit "*` against the check's last line. Quoted from it: `… · held unfixed: 1 · open: 3 · …` and `… · ready: NO · decisions: 2 · …` → OK.
- `:838` `ltip` = `9be877dc` (only one ` tip: ` in the line); not `ctip` (`edd4d584`), not `shead` → `fixed_ok` (`:841-857`) runs: FIX-ROUND cell (col 8) = `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d5-o1-b2-build-2026-10-06.md`, under `$REPORTS`, exists, committed `e2461938`, unmodified (check 9); `9be877dc` ancestor of `edd4d584` (check 10); last line starts `BUILT · job: drc-d5-o1-b2 · tip: edd4d584 |` and matches `"BUILT ·"*"tip: $ctip"*` → OK.
- `:861-868` branch head `38e0d47e` = row; `edd4d584` ancestor of it (check 3); `diff --stat edd4d584 38e0d47e -- . ':(exclude)docs'` empty (check 11) → OK.

The draft's two DECISIONS (TIP = branch head; RULINGS omit R545, R390) are the desk's kept defaults; not failed.

## ISSUES
None.

PREFLIGHT DONE · card: deploy-card-39-45 · checks: 32 · fails: 0 · ready: YES
