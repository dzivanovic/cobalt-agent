# Gain-measure survey — the brain's reading for Dejan · 2026-10-05

Source: `gain-measure-survey-2026-10-05.md` §0, BASELINE, DECISIONS. The survey's rows come from three sub-agents, and only its baseline was re-verified. Treat the numbers as close, not exact.

## §0 What the numbers say
1. **Waiting for the deploy is the biggest sink, not building.** READY jobs waited 3 to 8 hours on 10-02 and up to 28 hours (close-timer, 1,673 min) for one batched deploy. On 10-04, guard-b waited 591 min and K3 501 min, and D5 waited 289 min for a ruling (that wait is now ended by the 10-05 standing row).
2. **Batches fail together.** There were 5 failed deploy attempts against 6 deployed. Every failure was the deploy process tripping on itself (a conftest red at gate G(c), a preflight mismatch, a step-C fail, the d2 hub order), not a feature's own bug. One bad item holds every ready item in the batch.
3. **The lock is less of a problem than it was.** 10-02 had 14 lock FAILED and holds of 17 to 30 min. After 10-03 most checks ran with no database and held no lock, and 10-04 had no lock FAILED. What is left are deadlock reds on `cobalt_dev` (K3 lost 64 min, D5 16 min), which is tonight's second-writer survey's question.
4. **Cost per job cannot be measured yet.** Only day totals are recorded. Opus carries about 90% of output tokens each day (2.5 to 3.5 M a day).

## RECOMMENDATIONS — his to rule (scope and process)
- **R1. Deploy each feature when it is READY, not in one evening batch.** This attacks sinks 1 and 2 together. It needs a deploy-flow card from a drafter. The lock and gate stay as they are.
- **R2. Before a deploy, run the gate once on the merged hub text whenever a batch changes `DEPLOY-HUB.md` or `gate.sh`.** Today's d2 failure was a hub change that no gate had run. Small; a row for the deploy-flow card.
- **R3. Do not build the second dev database now.** The lock waits have mostly gone. Decide after tonight's second-writer survey explains the deadlocks.
- **R4. Record tokens per worker at its stop line** (the desk reads MEASURE when it removes a worker), so the next survey can price each job. Small; a desk record change.

The survey's three ASK DESK items were each settled by a sensible default. Nothing holds.
