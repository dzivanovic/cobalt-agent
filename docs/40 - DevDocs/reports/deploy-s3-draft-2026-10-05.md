# deploy-s3-draft — the S3 deploy card, drafted 2026-10-05

## §0 Headline
- Card `prompts/2026-10-05/02-deploy-s3-card.md` written: TIP `3e40359a c96b5118 6269f05e 47ec01c5`, MIGRATIONS `none`, TAG `deploy-2026-10-05-1`, D5 shipped with O1 carried.
- Every code tip is an ancestor of its head; only P2's head moves past its tip, by one docs file. Every trial merge is clean.
- Desk answered all four ASKs. The proven MARKERS and SMOKE READS are now in the card: `grep -c -F "«FILL"` → `0`.
- RULINGS `2026-10-03 R326, 2026-10-03 R327` KEPT. R327 now names `deploy-s3-1005`, but that row edit is uncommitted (RECORDS). Commit it before launch.

## SHIPS PROOF
main = `57c7502c` (`git -C /Users/cobalt/cobalt rev-parse main` → `57c7502cecf092bc2092c083bcae6741a8bf5458`, 06:2x EDT).

### 1 drc-k3 — `drc/k3-surfaces-1004`
- check line (`tail -n 3`): `CHECK DONE · job: drc-k3 · pass: 2 · tip: 3e40359a · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 1 · suites: offline 3871/0 · with-DB 863/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0`
- committed `a1c846ff` (2026-10-04 22:09); `git diff --stat` on the file → nothing.
- code tip `3e40359a`; head `rev-parse --short=8 drc/k3-surfaces-1004` → `3e40359a`.
- ancestor: `merge-base --is-ancestor 3e40359a 3e40359a` → exit 0. The head is the tip, so the docs-only proof is trivial.
- merge-tree `main 3e40359a` → exit 0, tree `6fdc700180f942150b22575b8395d52d89648a5f`.

### 2 drc-d5 — `drc/d5-reconcile-1004`
- check line: `CHECK DONE · job: drc-d5 · pass: 2 · tip: c96b5118 · house B: Grok FINDINGS: 4 · findings: 4 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 3 · suites: offline 3898/0 · with-DB 867/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 18 · ready: NO · decisions: 5 · for Dejan: 3`
- committed `a1a1f33f` (2026-10-05 01:30); `git diff --stat` → nothing.
- code tip `c96b5118`; head `rev-parse --short=8 drc/d5-reconcile-1004` → `c96b5118`.
- ancestor: `merge-base --is-ancestor c96b5118 c96b5118` → exit 0. The head is the tip. K3 is inside it: `merge-base --is-ancestor 3e40359a c96b5118` → exit 0.
- merge-tree `main c96b5118` → exit 0, tree `08de26af9c2b472301f5c61077d1e5240ad0a4cb`.
- SHIPS last column: `held unfixed: 1` and `ready: NO` · carried: O1 — 2026-10-03 R326.

### 3 f15-p2 — `f15/p2-replay-1004`
- check line: `CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · house A: Grok FINDINGS: 0 (Sol METER) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0`
- committed `4e8795dc` (2026-10-05 00:40); `git diff --stat` → nothing.
- code tip `437c7299`; head `rev-parse --short=8 f15/p2-replay-1004` → `6269f05e`.
- ancestor: `merge-base --is-ancestor 437c7299 6269f05e` → exit 0.
- docs only: `diff --name-only 437c7299 6269f05e` → `docs/40 - DevDocs/reports/f15-p2-build-2026-10-04.md`; with `-- . ":(exclude)docs"` → nothing.
- merge-tree `c96b5118 6269f05e` → exit 0, `c02eeec78fbca5aae6d14328ff5cedbecf849a2e`; `main 6269f05e` → exit 0, `022d9f195c007a022c516618c40aa745ea55d3a5`.

### 4 cobalt-guard-b — `ops/cobalt-guard-b-1004`
- check line: `CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 47ec01c5 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3782/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 7 · ready: YES · decisions: 1 · for Dejan: 0`
- committed `e3202c78` (2026-10-04 20:39); `git diff --stat` → nothing.
- code tip `47ec01c5`; head `rev-parse --short=8 ops/cobalt-guard-b-1004` → `47ec01c5`.
- ancestor: `merge-base --is-ancestor 47ec01c5 47ec01c5` → exit 0. The head is the tip.
- merge-tree `main 47ec01c5` → exit 0, `e78a2a55242bb97577608d0d76aaac3681837794`; `6269f05e 47ec01c5` → exit 0, `eecf9303046606121aeaf6042a20c92e0b2ed8b7`.

### MIGRATIONS
- `git diff --stat main 6269f05e -- src/cobalt/db_migrations` → nothing. The same for `main 47ec01c5` and for three-dot `main...<head>` on both. Value: `none`.

## DECISIONS
1. **ASK DESK — the RULINGS date [06:24].** The prompt gives `2026-10-05 R326, 2026-10-05 R327`. `authorize.sh` `prove()` (line 85) reads `reports/cto-<date>.md`. `cto-2026-10-05.md` does not exist (`ls reports/`), and both rows are `cto-2026-10-03.md:332–333`. The precedent card `07` cites R216, a 10-04 row in the same file, as `2026-10-03 R216`. Default taken: `RULINGS: 2026-10-03 R326, 2026-10-03 R327`, with the SHIPS carry cell `carried: O1 — 2026-10-03 R326` to match. If the desk opens `cto-2026-10-05.md` and moves the rows into it, change both places back to `2026-10-05`.
2. **ASK DESK — window P1 (iv) [06:24].** P1 (iv) requires a RULINGS row that overrules L66 / L43 "for THIS deploy and names this card's `JOB`". R327 reads "S3 deploys this morning, any hour". It names the set, not `deploy-s3-1005`. Window (v) does not hold: K3, D5 and P2 each derive `RESTARTS: com.cobalt.aset com.cobalt.radar`. `date` → Mon 06:22 EDT, a trading day, outside (i)–(iii). A strict hub ends `FAILED PREFLIGHT: window`. Default taken: the card is unchanged, and `## RECORDS` ties R327 to `JOB: deploy-s3-1005`. Desk options: the desk's own R327 row text names the JOB, or the hub accepts the RECORDS line. It is the desk's call; the drafter edits no ruling row.
3. **ASK DESK — MARKERS and SMOKE READS [06:24].** No job card (01, 03, 02, 06) has `## DEPLOY PROOF` (`grep -c "^## DEPLOY PROOF"` → 0 on all four). As `deploy-card.sh` would, the card holds 8 `«FILL»` lines. Default taken: FILL. Proven candidates follow. "before" is `grep -c` / `ls` on the `main` checkout. "after" is the job's worktree file. Each pickaxe proves which head commit adds the string:
   - `grep -c -F "def superseded_stated_ids" /Users/cobalt/cobalt/src/cobalt/drc/store.py` · before `0` · after `1` (K3 `49948783`; D5 worktree also `1`)
   - `ls /Users/cobalt/cobalt/src/cobalt/drc/reconcile.py` · before `No such file or directory` · after listed (D5 `3c1f75b8`, `--diff-filter=A`)
   - `grep -c -F "def corpus(" /Users/cobalt/cobalt/src/cobalt/cards/predictions.py` · before `0` · after `1` (P2 `735d0344`)
   - `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `3` (guard-b `c74edcd3`)
   - smoke candidates (new test files of the stack, `git diff --name-status main...6269f05e -- tests`): `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_drc_k3.py` · `…/test_drc_d5.py` · `…/test_f15_p2_replay.py`, each a count of 1 or more. For guard-b, `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py`, a count of 1 or more. These were not run at "after"; the files land with the merge.
   - Not proven: that each worktree's checkout is at its head. This seat runs no `git -C` on `cobalt-wt`. The pickaxe on `/Users/cobalt/cobalt` stands in for that proof.
4. **ASK DESK — the trial-merge chain [06:24].** `deploy-card.sh` chains each step with `commit-tree`, a git write this seat may not run. Default taken: two-way merges that cover the chain: `main`+K3, `main`+D5 (D5 holds K3), D5+P2, `main`+P2 (P2 holds D5's built tip `3c1f75b8`), `main`+guard-b, P2+guard-b. All are clean. guard-b touches only `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py`, which no other head touches. STEP-T is the binding merge.

## RECORDS
- The O1 carry: pinned `tests/cobalt/test_drc_d5.py::test_check_o1_a_re_paired_date_keeps_its_stored_unresolved_item` (strict `xfail`; D5 check `## OPEN` pass 2 and `## DECISIONS` 3). It ships under R326 (`cto-2026-10-03.md:332`, `HIS RULING · APPROVED`).
- D5's other open rows are not held: A3 = B4 is REJECTED, KEEP (R325, under 09-22 R67). B2 is REJECTED under D5-3; its wording goes to the follow-up card.
- Follow-up cards owed (R326): (1) O1 + B2 wording (`store.py:935` re-pair keeps `build_day.derived["unresolved"]`, or the items get their own store; then remove the xfail). (2) F15 P2 X11, the no-trigger row (`f15-p2-build-2026-10-04.md` DECISION 3: `replay_card` → `no_trigger`, no `missed` row, `awaiting nightly replay` for good).
- R327 (`cto-2026-10-03.md:333`, `HIS RULING · APPROVED — pending fold`) sets the window for this one deploy (L73: his direct instruction). DECISIONS 2 covers how the hub proves it.
- Tags: `refs/tags/deploy-2026-10-05-1` and `refs/tags/pre-deploy-s3-1005` are absent (`rev-parse --verify --quiet` exit 1). Gate worktree `deploy-1005-1` is not yet under `/Users/cobalt/cobalt-wt/` (the desk runs `worktree add`).
- Not committed: the card and this report sit unstaged on `main` for the desk (no git write on this seat).
- DESK ANSWERS, cross-session from `cto-desk`, after the first stop line:
  - ASK 1 KEEP `2026-10-03`.
  - ASK 2: R327 names the JOB. `grep -n "^| R327 "` → `…any hour: overrules L66/L43 for JOB \`deploy-s3-1005\`…`. `git log -S"for JOB \`deploy-s3-1005\`" -- cto-2026-10-03.md` → nothing: the edit is not committed. `authorize.sh` proves the row "at HEAD", so commit it before launch.
  - ASK 3: the 4 markers and 4 smoke reads from DECISIONS 3 replace the 8 FILL lines in the card. Their after values are worktree reads: tests `54` / `27` / `32`, and the marker counts as listed. A card `## RECORDS` line names the proofs. `grep -c -F "«FILL"` on the card → `0`.
  - ASK 4 KEEP: the two-way merges stand; STEP-T binds.

DRAFTED · card: prompts/2026-10-05/02-deploy-s3-card.md · fills: 0 · decisions: 4
