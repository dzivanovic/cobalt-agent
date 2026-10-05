# The next flow: fewer touches with both vendors kept · brain answer · 2026-10-05

## §0 Scope: what this covers and what it does not
- **NOT covered**, finished on today's rules: the launcher fix (card 21), the instruction rewrite (card 26), and the three production deploys K3, P2 and D5, including D5's fix on card `03` and P2's small item on card `02`.
- **COVERED:** every feature whose draft starts after the last of those deploys lands, together with its build, check and deploy.
- **Target:** six touches per feature (draft, preflight, build, check with both vendors, at most one fix round, deploy). Today's features took 8 to 14.

## THE CHANGES (his, on the brain's recommendation)
1. **Both outside vendors run inside the check, at the same time.** The check seat makes both house calls (the house slot on CHECK-HUB line 10): review 1 by one house and review 2 by another, in parallel, with all their findings in the one check report. No separate vendor session or round.
2. **One fix round for all findings.** The original builder fixes every finding from both vendors and the check together, on the same card (L75). It reruns only the tests the fix touches, then the deploy gate. There is no re-check and no third vendor pass (his ROW A: from review 3 on, no outside house).
3. **Build and check run the deploy gate's pass.** Every build's W step and every check runs the same test pass the deploy gate runs (`gate.sh … --deploy`), so a deploy-only red (a missing offline skip mark, a with-DB reach) is caught at build, not at deploy. The lock rules stay.
4. **Drafters prove their citations before the stop line.** A drafter re-reads every `file:line` and count its card cites against the file at BASE (`sed -n`, `grep -c`) and records each read in `## RECORDS`. A citation it cannot prove is not written.
5. **Measure.** The desk records each worker's MEASURE at its stop line (R375 R4) and, for each feature that lands, one row giving touches, deploy attempts, and total tokens across its workers.

## WHAT DOES NOT CHANGE
His standing rules: one feature per deploy, any hour (R389, R390); small fixes on the same card (R376); drafters use only the standard scripts and allowed commands (R412 contract); "Dejan said" (L79).

## FOR THE DESK
Send changes 1–4 to a drafter as rows for CHECK-HUB, BUILD-HUB and the drafter prompt shape, in one card. Under change 4, its own citations are proven. Launch it only after the last of K3, P2 and D5 is DEPLOYED. Until then, nothing in this file applies.
