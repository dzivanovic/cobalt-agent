# D5 deploy card (64) — preflight, 2026-10-05

Card: `prompts/2026-10-05/64-deploy-d5-card.md`. Read only; one file written (this one). No git write, no launch.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt rev-parse --verify c96b5118^{commit}` | `c96b51185c5995d4e9e4293d2e28c602f83ad6ec` | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse drc/d5-reconcile-1004` | `c96b51185c5995d4e9e4293d2e28c602f83ad6ec` (the card's TIP is the branch head, and the code tip equals it) | OK |
| 1c | `git -C /Users/cobalt/cobalt log --oneline c96b5118..drc/d5-reconcile-1004 -- tests src configs ops` | (empty) | OK |
| 1d | `tail -n 2` of the check report, last line | `CHECK DONE · job: drc-d5 · pass: 2 · tip: c96b5118 · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · suites: offline 3898/0 · with-DB 867/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 18 · ready: NO · decisions: 5 · for Dejan: 3`. The card's SHIPS cell spells `` `held unfixed: 1` and `ready: NO` ``; the card's `## RECORDS` quotes the same last line. | OK |
| 1e | `git diff --stat -- <check report>` · `git log -1 --format=%h -- <check report>` | (empty) · `a1a1f33f` (committed, clean) | OK |
| 2 | `desk-launch.sh` `ships_checked` (lines 779, 787-795) | `lits=$(printf '%s\n' "$carry" \| grep -o '`[^`]*`' \| tr -d '`')`; `clast=$(grep -v '^[[:space:]]*$' "$crep" \| tail -n 1)`; `case "$clast" in *"$lit"\|*"$lit "*) ;;`. Literal `held unfixed: 1` is followed by ` · open: 3 …` in the last line, so the `*"$lit "*` arm matches. Literal `ready: NO` is followed by ` · decisions: 5 …`, so the same arm matches. The tip rule (816): `ltip` from the last line is `c96b5118` = `ctip` = `shead`. Line 819-826: head `c96b5118` = row head, code tip is an ancestor of it, no non-docs diff. | OK |
| 3a | `git rev-parse --verify deploy/deploy-d5-1005` | `fatal: Needed a single revision` (exit 128) | OK (new) |
| 3b | `git rev-parse --verify deploy-2026-10-05-d5` | `fatal: Needed a single revision` (exit 128) | OK (new) |
| 3c | `ls /Users/cobalt/cobalt-wt/deploy-d5-1005` | `No such file or directory` | OK (new) |
| 3d | `ls "…/reports/deploy-deploy-d5-1005.md"` | `No such file or directory` | OK (new) |
| 4a | `grep -n -E "^\| R(326\|350\|412) "` in `cto-2026-10-03.md` and `cto-2026-10-05.md` | `332:\| R326 \| 10-05 06:19 ET \| HIS RULING: A on all three — D5 ships at c96b5118 with O1 pinned … \| HIS RULING · APPROVED \|` · `23:\| R350 \| 10-05 06:47 ET \| HIS RULING (brain relay …): 10-02 R4 already let D5 ship with O1 pinned … \| HIS RULING · APPROVED \|` · `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) from DEPLOY-HUB … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|`. Each row carries `HIS RULING` and `APPROVED`. R412's status cell is `APPROVED (in …)`, not `HIS RULING · APPROVED`; the `HIS RULING` text is in its body cell. It matches the L7a rule as stated, and the same R412 stands on the K3 card (`51-deploy-k3-card.md`). | OK |
| 4b | `git log -1 --format=%h -S"\| R<n> \|" -- <cto file>` | R326 `b1337431` · R350 `e89ef63a` · R412 `b3583b28` (all committed). The first two hashes are the ones the card quotes. | OK |
| 5a | `grep -c -F "reconcile" …/units.py` on main · `grep -c -F "refused_cards" …/build.py` on main | `5` · `0` (card `before`: 5 and 0) | OK |
| 5b | `ls` of `reconcile.py`, `test_drc_d5.py`, `test_drc_d5_db.py`, `test_drc_d5_experiments_db.py` on main | `No such file or directory` ×4 (card `before`) | OK |
| 5c | after counts at `c96b5118` (the checked-out branch worktree `/Users/cobalt/cobalt-wt/drc-d5-1004`; `grep -c -F`) | `reconcile` in units.py `8` · `refused_cards` in build.py `2` · `NO_WRITER_CODE` in reconcile.py `4` · `requires_db` in test_drc_d5_db.py `4`. `git -C … show c96b5118:src/cobalt/drc/units.py` read whole: 8 lines hold `reconcile` (counted by hand, as no pipe is allowed). All equal the card's `after`. | OK |
| 5d | `git -C /Users/cobalt/cobalt diff --stat main...drc/d5-reconcile-1004` | `15 files changed, 2124 insertions(+), 29 deletions(-)`: the 5 DevDocs pages, the build report, `ops/desk/gate-lists.md`, `drc_page.py`, `build.py`, `imports.py`, `reconcile.py`, `units.py`, and 3 test files. This is the SHIPS row's list, with no P2 file. The RESTARTS class of each (build report `## RESTARTS`, lines 192-208): DOCS ×6 `-`; `gate-lists.md` `operator script; no Cobalt reader`; the five `src` files `static import reach` → `com.cobalt.aset,com.cobalt.radar`; 3 tests `test/documentation; no resident`. These match the card, and there is no `UNCLASSIFIED`. Last line `RESTARTS: com.cobalt.aset com.cobalt.radar`. | OK |
| 5e | `merge-base main drc/d5-reconcile-1004` · `merge-base --is-ancestor 07a4b8fe main` · `diff --stat main...drc/d5-reconcile-1004 -- src/cobalt/db_migrations` · `diff --stat 3e40359a..c96b5118 -- tests/cobalt/test_drc_k3.py` | `3e40359ac99508105d7bed5dc849ca336f3bd1b3` · exit 0 · (empty) · (empty) — the card's other facts hold | OK |
| 6 | main's `CARD.md` header (line 44) and `deploy-card.sh` (line 207) against the card | CARD.md: `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|`; deploy-card.sh: `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|`; the card (line 15): the same seven columns, in the same order. `deploy-card.sh` lines 130-131 demand `held unfixed: 0` and `ready: YES`, as the card says. | OK |
| 7a | `grep -c -F "«FILL" …/64-deploy-d5-card.md` | `0` | OK |
| 7b | shape against `prompts/CARD.md` and the sibling `2026-10-05/51-deploy-k3-card.md` | All header keys of a deploy card are present (`JOB LADDER BRANCH WORKTREE BASE TIP REPORT RULINGS TAG MIGRATIONS SET`); `BASE: main`; the REPORT is `reports/deploy-<…>.md`; the body runs `## SHIPS`, `## MARKERS`, `## SMOKE READS`, `## RECORDS` in order; `MIGRATIONS: none`, so no `## READ-BACK` and no production `db query`. The markers are `ls` and `grep -c -F` only. The card and 51 follow the same layout; the RECORDS wording differs only where the facts differ (D5 carries `held unfixed: 1`, K3 has a fix round). | OK |
| 8 | `git diff --stat -- <card> <drafter report>` · `git log -1 --format=%h -- <card>` · `… -- <drafter report>` | (empty) · `495b7bce` · `495b7bce` | OK |

Note, not a FAIL: the card's RECORDS names main as `d664b926`; main is now at `495b7bce`. The card's claim (`07a4b8fe` is in main) holds.

## ISSUES
None.

PREFLIGHT DONE · card: d5-deploy-64 · checks: 8 · fails: 0 · ready: YES
