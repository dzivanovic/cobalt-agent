# QUESTIONS — round 2 (the fold), house check of `53-deploy-d3.md`

Round 1 found **two launch blockers** in this unattended production deploy prompt and nine further REAL findings. The desk folded eleven of them. **This round reads ONE thing: the fold** (`fold-r2.worddiff.txt`, `[-removed-]` / `{+added+}`) against the file as it now stands. Round 1's headline and complete verdict table are in `round1-verdicts.md`. No rule string changed — `approval-list.md` is unchanged and Dejan's approval (R36) still binds the same 51 rules.

**Q1 — F1, the first blocker.** Round 1: the run's own commits (§1.6, §3.1, §3.3) move `main` after the stack is cut, so the old 4.1 hard-stopped on every launch and 4.3 could not fast-forward. The fold takes option (ii): 4.1 now merges `main` INTO the stack worktree, proves the result is docs-only, and tests `merge-base --is-ancestor main <stack-final>`. (a) Does that actually make the fast-forward at 4.3 possible in every case? (b) Is the docs-only proof correct and sufficient — could code enter the stack through that merge and go untested? (c) What happens if that merge conflicts, and is nothing down at that point? (d) Does any sentence elsewhere in the file still assume `main` has not moved?

**Q2 — F2, the second blocker.** Round 1: `git revert --no-edit <pre-merge>..HEAD` cannot revert merge commits, and the range now holds two (soon three). The fold reverts newest-first, one command per commit, `-m 1` for merges. (a) Is `-m 1` the right parent — does it leave production on the code it was on before the merge? (b) Is the order right? (c) Is the non-conflict error branch now named, and is "keep the new code" a safe terminal state? (d) Does the third merge that F1's fix adds change the answer?

**Q3 — the other nine folds.** F3 (the §4.2 exception restored in both global places), F4 (the branch tips named in 2.3 — ops code tip `954cabb`, archiver `85b6d7c`), F5 (1.5 now stops on a foreign commit before the production snapshot), F6 ((h)'s trigger widened to (b)–(f), compare against (e) if it ran else (b)), F7 (P7 informational, both ranges), F9 (0010/0011 "stay" qualified by "if 4.5 ran"), F10 (the wrong `Placement:` rationale deleted), F11 (`jobs.yaml:242`). For each: does the new text say what it claims, and did it break a neighbouring sentence?

**Q4 — WHAT DID THIS FOLD BREAK?** Read every `{+added+}` region and ask whether it contradicts a sentence the diff did NOT touch. Round 1's F3 was exactly this class, inherited from the previous prompt.

**Q5 — the rule strings, again.** The fold was supposed to change none. Verify against the real launch line in `53-deploy-d3-after.md`: still 51 rules, still the 10 new + 41 identical of `approval-list.md`, and does any step — especially the new 4.1 merge and the new §8 (1) revert spellings — type a command no rule covers?

**Q6 — anything else that would damage production.** Findings round 1 ruled NOT REAL are not re-opened; if you disagree, one line and move on.

Not findings: the four MINORs in the build check, the `append`-mode switch, the missing `git push` rule, and F8 (unused rules that are part of the approved line).

Verdict line: `VERDICT: RUN AS IS` / `RUN AFTER FIXES <n>` / `DO NOT RUN <n>`. Severity BLOCKER / MAJOR / MINOR, one-line fix each.
