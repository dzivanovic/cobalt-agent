# DRAFT — gate-alignment card 397 (2026-10-12)

## §0 Headline
- Card `prompts/2026-10-12/397-gate-alignment-card.md` written, `CLASS: K5`, job `gate-alignment-1012`. `BASE` holds the desk's one `«FILL`; `TIP` is empty.
- Rows: G1 reads a held id from `## RUNS` or `## FIXES`, and a fix round's `FIXED:` line closes it. G2 counts `open:` as held unfixed only, plus `REJECTED`/`UNSETTLED` ids each settled by `SETTLED: <id> — R<n>` against a DESK RECORD row. H3 edits CHECK-HUB inside lines `:104`, `:107` and `:123`. R1 runs 386 against both scripts; R2 is RESTARTS.
- Every edit sits in THE RULE, the one text shared by `deploy-card.sh`, `desk-launch.sh` and `deploy-step0.sh`. No CHECK-HUB line is added and none sits on 386's `:113` seam, so 386 then deploys unchanged on its committed check plus F1.
- Decisions: 5 ASK DESK, each with its default taken.

## DECISIONS
1. ASK DESK: G2 keeps the settlement record in the fix report as `SETTLED: <id> — R<k>` lines. `R<k>` is looked up the way CARRIED looks up its row, in `cto-<check date>.md`. A brain answer recorded the next day (R1149 is in `cto-2026-10-12.md`; 386's check is dated 10-11) would not be found. 386 does not hit this: its committed last line already reads `open: 1`. Default taken: CARRIED's lookup, so THE RULE keeps one desk-file read. Alternative: also read the next day's `cto-` file. [07:17 ET]
2. ASK DESK: G1 takes held-unfixed ids from `## FIXES` bullets carrying `HELD, NOT FIXED` (CHECK-HUB `:107`'s own wording), plus today's two `## RUNS` forms. A RUNS bullet ending `**HELD**` alone is not counted, because the check may have fixed it. Default taken: as written. [07:17 ET]
3. ASK DESK: 386 deploys on its check report as committed at `86b9daa5`. That commit already carries the R1154 `## DESK CORRECTION` appended, and its last line reads `open: 1`. R1157 rules out any further edit. Against the original line (`open: 5`), G2 would need four `SETTLED:` lines in F1, which means an F1 edit. Default taken: the committed file stands as it is, and R1 and the DEPLOY PROOF read it. [07:17 ET]
4. ASK DESK: `deploy-card.sh` copies every non-marker `## DEPLOY PROOF` line into the deploy card's `## SMOKE READS`. So the 386 line will show up in 397's deploy card. Its arguments are partly the desk's, so it cannot be typed whole. Default taken: the line is marked census, the desk's next step and not a gate; the desk may drop it from the deploy card. [07:17 ET]
5. ASK DESK: R1 runs the worktree's `deploy-card.sh`, and that path is not covered by CLASS (a) `sh /Users/cobalt/cobalt/ops/desk/*`. Default taken: a probe staged under `$CLAUDE_JOB_DIR/tmp` (BUILD-HUB E2's RUN form, outside the worktree after 386's `docs/_inflight` stray), with `--out` under the same tmp. [07:17 ET]

## RECORDS
- Clock `date` → `Mon Oct 12 07:14:17 EDT 2026`; `main` HEAD `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `4c4d1dcb`.
- Read: `prompts/CARD.md`; `reports/cto-2026-10-12.md` R1149 (`:15`), R1154 (`:10`), R1157 (`:7`), R1138 (`:26`); `prompts/CHECK-HUB.md` (grep of verdict, count and stop-line lines: `:104`, `:107`, `:114`, `:120`, `:123`); `ops/desk/desk-launch.sh:1000-1109`; `ops/desk/deploy-card.sh` whole; `ops/desk/deploy-step0.sh:160-179`; the 386 check report whole; F1 report `git show ops/launcher-shadow-check-1011:<path>` whole; `git show 66c4fefc:tests/ops/test_check_hub_shadow.py`; `tests/ops/test_deploy_card.py:606-695`, `:718-747`; card 389 whole; the header lines of cards 386 and 392; `topics/writing-rules.md`.
- THE RULE's place: `grep -n` of `THE RULE|held_rule` → `deploy-card.sh:135`, `:155`, `:324`, caller `:395`; `desk-launch.sh:1016`, `:1036`, `:1205`, caller `:1284`; `deploy-step0.sh:139`, `:159`, `:328`, caller `:585`. Id read at `deploy-card.sh:160-163` / `desk-launch.sh:1041-1044` / `deploy-step0.sh:164-167`. `open:` test at `:172-175` / `:1053-1056` / `:176-179`. CARRIED desk lookup at `deploy-card.sh:228-229`, `:306-317`.
- Pinned refusal texts: `grep -rn -F "under ## RUNS" tests/ops` → `test_desk_launch_prechecks.py:767`, `test_deploy_card.py:727`, `:738`, `:741`, `:828`, `:863`. `grep -rn -F "but not 'open:" tests/ops` → `test_deploy_card.py:730`.
- Fixtures: `grep -n` → `held_round` at `test_deploy_card.py:618` (`runs_text` `:621`), `test_desk_launch_prechecks.py:711` (`:714`, `:744`), `test_deploy_step0.py:704` (`:707`, `:746`). The one-text pin is at `test_deploy_card.py:800`.
- 386 on `main`'s THE RULE: last line `held unfixed: 1 · open: 1 · ready: NO` (`:230`). RUNS G3 `· **HELD**.` (`:168`) gives 0 ids, so it is refused at the count (`deploy-card.sh:176-179`).
- 386 branch: `git log --oneline -4 ops/launcher-shadow-check-1011` → `ef754d0b`, `66c4fefc`, `418af955`, `12ac16cb`. `git diff --stat 66c4fefc ef754d0b` → the build report only. The check report's history: `86b9daa5`, `ea4063f4`. Card 386 last commit `7f549bb1`.
- Merge seam: `git diff -U0 a76d8855 66c4fefc -- CHECK-HUB.md` → inserts after `:21`, `:61`, `:113`. `git diff --stat a76d8855 HEAD` over CHECK-HUB, the three scripts and their three test files → nothing.
- Counts: `wc -l` → CHECK-HUB 123, deploy-card.sh 494, desk-launch.sh 1687, deploy-step0.sh 735, test_deploy_card.py 962, test_desk_launch_prechecks.py 1307, test_deploy_step0.py 846, test_house_probe.py 280. `grep -c -F "card 397"` and `grep -c -F "SETTLED: "` over the three scripts and CHECK-HUB → 0 each.
- INSTALL: `ls -la /Users/cobalt/.claude/ops/{desk-launch,deploy-card,deploy-step0}.sh` → three links into `/Users/cobalt/cobalt/ops/desk/`.
- RESTARTS: `grep -n` of `restarts.py` → `:38` `OPS_DESK_PREFIX`, `:225-228` DOCS, `:232` operator script, `:246` test/documentation.
- Card placeholder check: `grep -c -F "«"` over card 397 → `1` (BASE).
- No commit, no launch, no git write.

DRAFTED · decisions: 5
