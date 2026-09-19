# QUESTIONS — house check of `53-deploy-d3.md`, the UNATTENDED PRODUCTION DEPLOY PROMPT for deploy 3

Nobody sits at this prompt's terminal. It takes two resident services down, merges two branches into the live tree, applies two migrations to the live database, and brings the services back. It is APPROVED by Dejan already (`cto-2026-09-19.md` §4 R36) on three conditions, one of which is that you find **zero launch blockers**. A defect you do not name here runs tonight against a live trading system.

It is deploy 2's prompt (`38-deploy-p4.md`) evolved: that file ran three times today, was checked by three house rounds, and ended `P4 DEPLOY DONE`. `vs-deploy2.worddiff.txt` is the word-level diff from it to this one (`[-removed-]` / `{+added+}`) — **the diff is where the risk is.** `approval-list.md` is the rule-string delta Dejan approved. `build-check.md` is the houses' verdict on the CODE this deploys.

**Q1 — the one-fast-forward design, which is new and is the biggest change.** Deploy 2 merged one branch and threw its gate worktree away. This prompt builds `stack/deploy3-0919` from `main`, merges BOTH branches into it, runs both suites on it, and then fast-forwards `main` **to that same branch**. Its stated reason: the two branches are siblings off one `main`, so ff-merging one makes the other non-ff, and the tree that lands is then byte-identical to the tree the gate proved. (a) Is that reasoning sound? (b) Is the fast-forward actually guaranteed — what makes `main` still an ancestor of the gate branch at §4.3, and what happens if it is not? (c) Does anything in the prompt still treat the gate branch as a throwaway, contradicting §7's cleanup note? (d) Is there a case where the gate goes green and the merge then lands something the gate did not test?

**Q2 — the rule strings.** Check `approval-list.md` against the real launch line in `53-deploy-d3.md`: are exactly those 10 new, those 41 identical to deploy 2's approved line, and those 14 dropped? Does any step type a command that NO rule covers — in particular every `launchctl`, `tag`, `merge`, `cp`/`rm` and `db migrate` spelling? Is any rule present that no step uses? `push` must appear nowhere.

**Q3 — residents and the safe-state rule.** §4.2 takes both residents down; §8 brings them back. (a) If one `bootout` succeeds and the other fails, does the prompt leave production with a resident DOWN, and does its FAILED line state the true state? (b) `com.cobalt.replay` arrived with deploy 2 and is NOT booted out in §8 here — is that right, given §8 reverts only this deploy's range? (c) Can §8 be entered twice, or loop?

**Q4 — the migration.** Only `0010` and `0011` are new. (a) Does the prompt's gate hold the proof table to exactly those, and would it catch a third unexpected `CREATED`? (b) Is the "the harness commits before it prints" case handled — can the run ever report "nothing applied" when the migrations are in fact committed? (c) Is it true that no production rollback is typed in any branch?

**Q5 — the L68 gate's with-DB steps.** (b) baseline, (c) forward, (d) suite, (e) post-suite proof, (f) restore, (g) `.env` cleanup, (h) red-branch restore. (a) Is `.env` always removed before every stop line, on every red path? (b) Is the post-restore comparison made against (e) and not (b) — deploy 2 false-stopped because it compared against the pre-suite baseline? (c) Can any red branch leave `cobalt_dev` in a state no other lane expects, without saying so?

**Q6 — the clock.** Start ≤ 20:15 ET, re-checked once before the bootout, hard edge the 21:40 nightly backup. (a) Is the point of no return stated consistently — can any hour send a *successful* merge to §8? (b) Is 20:15 actually enough for the measured ≈3–4 minute outage plus smoke? (c) Do the Mon–Fri-only claims about `com.cobalt.archiver` (20:30) and `com.cobalt.replay` (21:10) hold — check the plists yourself.

**Q7 — what did the evolution from deploy 2 break?** Read every `{+added+}` region of the diff and ask whether it contradicts a sentence the diff did NOT touch. Deploy 2's own checks found exactly this class three rounds running.

**Q8 — anything else that would damage production**, severity BLOCKER / MAJOR / MINOR, one-line fix each.

**Not findings:** the four MINORs in `build-check.md` (carried deliberately, disclosed to Dejan), the `append`-mode switch, and the missing `git push` rule. Verdict line: `VERDICT: RUN AS IS` / `RUN AFTER FIXES <n>` / `DO NOT RUN <n>`.
