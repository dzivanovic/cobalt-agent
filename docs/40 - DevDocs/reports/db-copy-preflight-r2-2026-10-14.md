# Card 547 `db-copy-1014` — preflight round 2 (read-only)

HEAD `1733c5aa`. Card `prompts/2026-10-14/547-db-copy-card.md`. Nothing was run but reads; no test was executed.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <card>`; `git log --oneline -- <card>` | diff empty; last commit `1733c5aa` | OK |
| 2 | `grep -c "«FILL" <card>` | `0` (the launcher's refused token is absent) | OK |
| 3 | header vs `CARD.md` build column | JOB, LADDER, BRANCH, WORKTREE, BASE, TIP (empty), REPORT, CHECK REPORT, HOUSE B, DB, RULINGS all present. The only empty values are BASE and TIP (the desk's). CLASS, INSTALL and RESTARTS also appear in cards 537 and 548. | OK |
| 4 | `git diff HEAD --stat -- ops/desk tests/ops BUILD-HUB CHECK-HUB DEPLOY-HUB src/cobalt/env.py src/cobalt/devdb.py` | empty: every `file:line` read from the tree is HEAD's | OK |
| 5 | `gate.sh` anchors, read at HEAD | all hold: `:30` THE LOCK, `:130-181` first reader block, `:145` `one()`, `:156-159`, `:182` OFFLINE, `:194` PASS1_DEPLOY, `:213` run(), `:255` held_env, `:267` take, `:288` ours-alone, `:291` release, `:352-368` cleanup, `:362-364` STILL PRESENT, `:375-395` proof_clean, `:397` do_offline, `:422` do_withdb, `:493` F2=F0, `:494` `release \|\| exit 1` | OK |
| 6 | `desk-launch.sh:1082-1089`, `:1091-1098`, `:2119` | `lock_free`, `lock_dir_free` and the gate-worktree `.env` check are where the card says | OK |
| 7 | `gate-lists.md` `:3-8`, `:10`; `BUILD-HUB.md:83`, `:81`, `:12` | hold. A `## COPY …` mention in a backticked paragraph starts with a backtick, so the sections reader does not read it as a heading. | OK |
| 8 | tests anchors: `test_devdb_lock.py` `:38-48`, `:51-54`, `:200-264`, `:267-276`, `:279-335`; `test_gate.py` `:171-204`, `:234`, `:256`; `test_hub_lines.py:54-57`; `restarts.py:225-234`, `:245-246`; `release-devdb-lock.sh:20-33` | all hold. Check 12 of round 1 is closed: both named tests exist at `:234` and `:256`. | OK |
| 9 | `take-devdb-lock.sh:61-63` (row E1: "the copy of `take-devdb-lock.sh:61-63` (`cp "$REPO/.env" …`, `REPO=…`)") | at HEAD `:61-63` is `done` / `holder=` / `printf`. `REPO=` is `:26`; the `cp` is `:49`. | FAIL |
| 10 | each red names its failing reason on BASE | E1 (1-4): script absent, exit 127. G1 (5, 6, 7, 8, 9, 11): no `dev-copy` call, or lock directory held and stub `sleep` called. L1 (12): exit 1 `lock is held`. D1 (14), H1 (16): section or line absent. Negative controls (10), (13), (15), (17) are marked GREEN on BASE. | OK |
| 11 | `tests/ops/test_build_hub_no_clutter.py:57-60` after H1 edits `BUILD-HUB.md:83`; the card says "523 H3 (3) repairs it" | Still a FAIL. `test_no_other_line_changes_from_base` is `ls[:i] + ls[i+2:] == base_lines()` with `BASE = "5e5fab02"` (`:15`, `:57-60`). Today it is green: `git diff --stat 5e5fab02 HEAD -- BUILD-HUB.md` is 2 insertions, the no-clutter pair. 523 H3 (3) only drops the `FIX-ROUND REPORT` line and the `§0 Headline` line, and 523 FR-T1 touches `test_hub_text_1013.py` only. Neither exempts the `- (b) THE LOCK` line. Card 548 RF2 (the ordered-subsequence repair) lists its own EXEMPT prefixes and does not list `- (b) THE LOCK` either. So after H1 the test is red under every repair any open card writes, and the card's own final run (`… test_build_hub_no_clutter.py`, "`0 failed`") cannot pass. The card edits `:83` and says the test is "not edited here". 523's merge is also reverted at HEAD (`cdf2233c`), so no repair is on `main` yet. | FAIL |
| 12 | no test pins a whole file, a whole fixed-file line equal to a commit, or a BASE literal | tests (1)-(17) pin by content (counts of lines found by their start, `startswith`, the names). None reads `git show`, a commit or a hash. The one BASE pin in the run is the existing test of check 11, not a new test. | OK |
| 13 | launch lines and laws | no `claude --bg ` line, allow or deny string is edited. The new script runs under the existing `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`. Test (17) holds that. LAWS and RULING 7 are not touched (L76 is named as the desk's, `ASK DESK 2`). | OK |
| 14 | RESTARTS class homes (K10) | `ops/desk/` → "operator script; no Cobalt reader" (`restarts.py:230-234`). `docs/` → `DOCS` (`:225-228`). `tests/` → "test/documentation; no resident" (`:245-246`). `RESTARTS: none` holds. | OK |
| 15 | overlap with 521, 523, 537, 546, 548, 549, 550 | none on a line range. 521: `gate.sh:2`, `:72`, `:86-112`, `:156-159`, `:182`, `:397-400`, `BUILD-HUB:80`, `:82`. 523: `BUILD-HUB:105`, a new `:112`. 537: `BUILD-HUB:12`, `:65`, `:80-82`, `DEPLOY-HUB:11`. 546: `pre-commit`, `DEPLOY-HUB`. 548: `BUILD-HUB:109`, `CHECK-HUB:125`, `desk-launch.sh:1450-1489`, `deploy-card.sh`. 549: `CTO-DESK-WAKEUP:13`. 550: `CARD.md`. 547 takes `desk-launch.sh:1082-1089`, `BUILD-HUB:83`, and `gate.sh` after `:37`, after `:194`, `:255-263`, `:352-368`, `:375-395`, `:422-501`. The shared files are 548 and 523 with the no-clutter test body (not 547's), and 521 with `gate.sh`/`gate-lists.md` (disjoint lines, found by content). | OK |
| 16 | what blocks the card's own deploy | one deploy at a time; 537 deploys first. The build waits for card 523's recut to deploy. At HEAD the 523 merge is reverted (`cdf2233c`), so this card cannot build yet. 521 touches the same `gate.sh` and `gate-lists.md` files, so the later deploy re-finds its lines by content. | OK |

## ISSUES

1. FAIL (check 11): H1 turns `tests/ops/test_build_hub_no_clutter.py::test_no_other_line_changes_from_base` red, and neither 523 H3 (3) nor 548 RF2 exempts `BUILD-HUB.md:83`. Add that test to the files of row H1 and repair it by content, with the `- (b) THE LOCK` line exempt and no BASE literal kept. Alternatively, drop the claim that 523 repairs it.
2. FAIL (check 9): row E1 cites `take-devdb-lock.sh:61-63` for the `cp "$REPO/.env"` and `REPO=`. At HEAD they are `:49` (`cp`) and `:26` (`REPO=`).
3. NOTE: test (7) wording "the drop NOT called a second time … one drop at step 2, one at the trap is allowed" is loose. State the exact call sequence expected after a failed create.
4. NOTE: the 523 merge is reverted at HEAD, so the build-after-523 order is not yet satisfiable.

PREFLIGHT DONE · card: db-copy-1014 · checks: 16 · fails: 2 · ready: NO
