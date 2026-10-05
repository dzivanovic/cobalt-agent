# launcher-fixround deploy card 47 — preflight r2 (read-only), 2026-10-05

Card: `prompts/2026-10-05/47-deploy-launcher-fixround-card.md`. Every command below was run by this seat; output quoted.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | round-1 FAIL 5 (7 columns): card `## SHIPS` header now | `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` (card line 15; row line 17 ends `` `held unfixed: 0` and `ready: YES` \| ``): six columns, same as main's `CARD.md:44` and `deploy-card.sh:207`. Card line 38 records that `fix report` is added by this deploy and the row needs none (check `tip:` = code tip). | OK |
| 1b | round-1 FAIL 6a (base hunk numbers): card line 37 vs `git diff -U0 5fb0ddf5 main -- DEPLOY-HUB.md` | card: "changes lines 26, 50, 57 (P1), 74, 93, 101, 134, 178, 181 of the base". Diff hunks: `@@ -26`, `-50`, `-57`, `-74`, `-93 +92,0`, `-101 +99,0`, `-134`, `-178`, `-181`. Same nine numbers. | OK |
| 1c | round-1 FAIL 7b (glued OWED bullet): card lines 37, 38, 39 | `- DEPLOY-HUB.md …` (37), `- The fix-round column …` (38), `- OWED, a later card …` (39): each its own line. | OK |
| 2a | `git -C /Users/cobalt/cobalt rev-parse --verify a545a4d8^{commit}` | `a545a4d8d424c72df46d86c240b7484427f0cad2` | OK |
| 2b | `git -C /Users/cobalt/cobalt rev-parse ops/launcher-fixround-1005` | `a545a4d8d424c72df46d86c240b7484427f0cad2` (head = TIP = code tip, so the ancestor test is trivial) | OK |
| 2c | `git -C /Users/cobalt/cobalt log --oneline a545a4d8..ops/launcher-fixround-1005 -- tests ops configs src` | nothing | OK |
| 2d | `tail -n 1 …/launcher-checks-check-2026-10-05-r2.md` | `CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · … · held unfixed: 0 · open: 0 · … · RESTARTS: none · … · ready: YES · …` | OK |
| 2e | `git log -1 --format=%h -- <check report>` · `git diff --stat -- <check report>` | `6bf0b815` · nothing (committed, clean) | OK |
| 3 | `rev-parse --verify` on `deploy/deploy-launcher-fixround-1005` and on tag `deploy-2026-10-05-launcher-fixround`; `ls` of `/Users/cobalt/cobalt-wt/deploy-launcher-fixround-1005` and of the report path | both `fatal: Needed a single revision` (exit 128); both `ls`: `No such file or directory` | OK |
| 4 | `grep -n "^| R412 " reports/cto-2026-10-05.md`; `git diff --stat` and `git log -1 --format=%h` on that file | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|`; diff nothing; log `ea890645`. The card's only `RULINGS` entry is R412. (`LADDER` also cites R387, line 62: `HIS RULING (L79, via brain) … \| APPLIED`; not a `RULINGS` entry; siblings 39 and 41 cite it the same way.) | OK |
| 5a | markers on main, `before` | step0 `is not committed and unmodified` → `0`; hub `Fix-round row` → `0`; CARD.md `On a fix-round row (a small fix after the check, his R376, L75)` → `0`; deploy-card.sh `\| fix report \|` → `0`. Card says `0` ×4. | OK |
| 5b | `after` at `a545a4d8`, read from `git diff -U0 main...a545a4d8` of each file (`git grep` is outside the allowlist; counted by eye) | step0: 1 (the `why=` line, `is not committed and unmodified`); hub: 1 (`- Fix-round row (its \`fix report\` cell…`, from `git diff 5fb0ddf5 a545a4d8`); CARD.md: 1 (`On a fix-round row (a small fix after the check, his R376, L75)`); deploy-card.sh: 1 (header `\| fix report \|`; the ships row ends `\| \|`, no match). Card says `1` ×4. | OK |
| 5c | `git -C /Users/cobalt/cobalt diff --stat main...a545a4d8` | 8 files, 586 insertions, 11 deletions: `prompts/CARD.md`, `prompts/DEPLOY-HUB.md`, `reports/launcher-fixround-build-2026-10-05.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py`. The card lists exactly these 8, each with a class (operator script / test / DOCS); `RESTARTS: none`; no `src/`. | OK |
| 6a | main's `CARD.md:44` and `deploy-card.sh:207` | both `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` (six columns); card 47 header identical | OK |
| 6b | `grep -n` of readers in `desk-launch.sh` | `:714 carry=$(… awk -F'\|' '{print $7}')` (literals = column 6); `:705 … $5` (check report); `:764` generic `$i` cell reader. Six-column rows, no count test. | OK |
| 7a | `git diff -U0 5fb0ddf5 main -- DEPLOY-HUB.md` (see 1b) vs the branch's `git diff -U0 5fb0ddf5 a545a4d8 -- DEPLOY-HUB.md` | main's nearest hunk is `@@ -57` (P1, one line); branch `@@ -58,0 +59 @@`: one inserted line after base line 58 (P2). Line 58 is unchanged on main, one line between the hunks, so the hunks do not touch. The card's claim matches. Merge itself not run (`merge-tree` is outside the allowlist). | OK |
| 8a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 8b | shape against `CARD.md` (header keys, `## SHIPS`, `## MARKERS`, `## SMOKE READS`, `## RECORDS`) and siblings 39, 41 | same header keys (JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, RULINGS, TAG, MIGRATIONS, SET) and section order; six-column SHIPS; MARKERS with `before`/`after`; SMOKE READS with exit/count. Card 47 has 4 markers and 4 smoke reads. | OK |
| 9 | `git diff --stat -- <card>` · `git log -1 --format=%h -- <card>` | nothing · `ea890645` (committed, clean) | OK |

## ISSUES
None.

PREFLIGHT DONE · card: launcher-fixround-deploy-47 · checks: 19 · fails: 0 · ready: YES
