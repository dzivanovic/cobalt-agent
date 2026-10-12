# draft-reapplied-tip — card 411 (K5)

## §0 Headline
Card 411 is drafted at `prompts/2026-10-12/411-reapplied-tip-card.md`. It adds THE RE-APPLIED RULE (R1207 (a)-(d)) as one text in `deploy-card.sh`, `desk-launch.sh` and `deploy-step0.sh`, plus one CARD.md :48 clause. Rows A1-A4 and RUN rows R1-R2.
Reading the code shows two more rows are needed: `desk-launch.sh:1341` and `deploy-step0.sh:674` run the same ancestry refusal, so a deploy card cut by `deploy-card.sh` alone could not launch.
Reading the code also shows 1012b FAILS the rule as written: (a) at `tests/ops/test_desk_launch_prodwrite.py` (one docstring line) and (b) at `ops/desk/desk-done.sh` (lines carry both changes). The red "1012b accepted" cannot go green.
Default: fallback B for 392 (a fresh check of 1012b). Card 411 stands for later re-applies.

## DECISIONS
1. ASK DESK [11:19 ET]: 1012b fails R1207 under the rule as written. (a): `git diff b96737bf 62ea5957 -- tests/ops/test_desk_launch_prodwrite.py` changes `desk-launch.sh:889` → `:892` in P1's docstring, so the patch-ids differ. (b): `desk-done.sh` lines 2, 6-9 and 22 each carry both the prodwrite change and `ba37c2a9`'s shadow change, so no hunk is "unchanged" under any hunk split. → fallback B (a fresh check of 1012b). Card 411 launches only if the desk keeps it for later re-applies, and its census line expects 392 REFUSED.
2. ASK DESK [11:19 ET]: the seam commit. `1966c239` is a merge (`Merge branch 'main' into deploy/launcher-shadow-check-1011`). Against its first parent it holds no `desk-done.sh` hunk, so the hunks are `ba37c2a9`'s. Default: no flag. The rule derives the seam paths and commits by git: `git log --no-merges <checked base>..<new base> -- <path>` on a path whose patch-ids differ. Card 392's files cells name paths only and mark no seam or commit.
3. ASK DESK [11:19 ET]: (d) can't be proved by git. It is a read of the fix report's `BUILT ·` line. The `tests/ops` run (1012b: 3403 passed) appears on no stop line. Default: the line's ` offline <n>/0`, ` with-DB <n>/0` and ` live-note <n>/0` fields, as today's fix round trusts that line. The deploy gate runs at the deploy.
4. ASK DESK [11:19 ET]: the build report `docs/40 - DevDocs/reports/prodwrite-seat-build-2026-10-12.md` is one of card 392's 17 names, and every build writes its own, so (a) would always refuse it. Default: (a) and (c) skip `docs/40 - DevDocs/reports/` (`deploy-card.sh:471` already lets docs/ move past the code tip).

## RECORDS
- `date` → `Mon Oct 12 11:16:38 EDT 2026`; `main` HEAD `8f6aac21`.
- `cto-2026-10-12.md`: R1206 `:9`, R1207 `:8`, R1208 `:7`, R1194 `:21`, R1192 `:23`, R1188 `:27`, R1187 `:28`, R1156 `:57`, R1138 `:75` (grep).
- `deploy-card.sh` read whole (564 lines). The fix-report reader is `:436-469`, the ancestor refusals `:461` and `:470`, the docs-only rule `:471-472`, THE RULE `:135-394`, and the trial merge `:505-528`.
- `CARD.md:48` read: it names the ancestor form of a fix round only.
- 1012b build report (`git show ops/prodwrite-seat-1012b:…`): last line `BUILT · job: prodwrite-seat-1012 · tip: 62ea5957 | on 7744ece9 | … offline 4199/0 | with-DB 0/0 | live-note 146/0 | … · re-applied from b96737bf onto 62ea5957`. `## E2 RED` records the `:892` docstring.
- Card 392 header: `BASE: 7744ece9`, `TIP: 89fd13c5`, `BRANCH: ops/prodwrite-seat-1012b`, `CHECK REPORT …/prodwrite-seat-check-2026-10-12.md`. Row S2's files cell = the 17 paths.
- Check report last line: `… tip: b96737bf · … held unfixed: 0 · open: 1 · … ready: YES …`.
- `git log --oneline -6 ops/prodwrite-seat-1012b` → `d206838d`, `62ea5957`, `f3866240`, `7744ece9`, …. `git log --oneline 86b9daa5..b96737bf` → 5 job commits. `git log --oneline 7744ece9..86b9daa5` → nothing.
- `git diff --stat b96737bf 62ea5957 -- ops tests <3 prompts>`: `test_desk_launch_prodwrite.py 2 +-` is the only path beyond main's movement (`git diff --stat 86b9daa5 7744ece9`).
- Read side by side (`git diff 86b9daa5 b96737bf` vs `git diff 7744ece9 62ea5957`): `desk-launch.sh`, `test_desk_done.py` and `test_desk_launch_prechecks.py` differ only in `@@` line numbers and `index` lines, so (a) holds there.
- `desk-done.sh`: `git log 86b9daa5..7744ece9 -- ops/desk/desk-done.sh` → `ba37c2a9` only (parent `d71ff562`). `git show --stat 1966c239` → parents `c09a532f 96e163ee`, one file (a deploy report). `git diff 1966c239^1 1966c239 -- ops/desk/desk-done.sh` → nothing. The checked, seam and re-applied diffs were read whole.
- `desk-launch.sh:1334-1347`, `:1359-1366` and `deploy-step0.sh:596-715` read: both run `merge-base --is-ancestor` on the check tip and the fix tip (`:1341`, `:674`). This is the basis for rows A2 and A3.
- THE RULE end markers: `deploy-card.sh:394`, `desk-launch.sh:1278`, `deploy-step0.sh:398`.
- `git patch-id` appears in no `ops/` file (Grep). The desk runs `deploy-card.sh` through `Bash(sh /Users/cobalt/.claude/ops/*)` (`.claude/settings.json:30`). `ls -la /Users/cobalt/.claude/ops/` shows the three scripts linked to the repo, so INSTALL is none.
- Test anchors: `test_deploy_card.py` `fix_round :442`, `_fix_refused :500`, `:523`, `rule_text :795`, `test_h1 … :801`; `test_desk_launch_prechecks.py` `fix_round :696`, `neither :720`, `:726`, `:736-740`; `test_deploy_step0.py` `fix_round :578`, `:619`, `:628-637`. `tests/ops/test_card_reapplied.py` is absent.
- Precedent: card 397 (header, INSTALL, R2 RESTARTS, DEPLOY PROOF shape). `restarts.py :38`, `:225-228`, `:232`, `:246`.
- `wc -l`: deploy-card.sh 564 · deploy-step0.sh 805 · desk-launch.sh 1775 · test_deploy_card.py 1203 · test_deploy_step0.py 876 · CARD.md 139.
- The card's only `«FILL` is on BASE (grep `:7`).

DRAFTED · decisions: 4
</content>
</invoke>
