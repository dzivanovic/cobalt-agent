# Touches survey spec (brain via L79, his asks R1351, R1352, 2026-10-13)

Read-only Sonnet survey, no lock. Output `reports/touches-2026-10-13.md`. Compare with `job-stats-2026-09-30.md` where it overlaps.

Scope: every card or job with any worker since 2026-10-05. Sources: `reports/*-{draft,amend,preflight,build,check,decisions}-*.md`, the deploy reports, the `cto-2026-10-0[5-9]` and `cto-2026-10-1[0-3]` DESK RECORD rows, `git log --since=2026-10-05` subjects (wip/feat/fix/docs per job).

A touch = each worker session on a card: drafter, amend, preflight round, build, fix round, check, deploy attempt, recut, and the brain or desk decisions answered.

STANDARD touches per card (the normal path, never a problem): drafter 1 · brain decisions on the draft 1 · preflight 1 · build 1 · brain decisions on the build 1 · check 1 · deploy card 1 · deploy 1 = 8. A hub-text or docs card with no build decisions = 7. A survey or spike = 2 (drafter plus report).

REWORK = every touch beyond the standard: an amend or re-issue, a preflight round after the first, a fix round, a rebuild or relaunch, a failed deploy and its recut, a CONTINUE after a FAILED step, a correction of a report, and a NEW card spawned only to unblock this one (counted against the card it unblocked).

Output order, first for him:
(a) the standard per card type, one line each;
(b) REWORK totals: cards with any rework, total rework touches, average per reworked card;
(c) rework causes ranked by touches (gate or parser, classifier denial, seam, preflight wording, lock or harness, the model's own code defect, design changed mid-card), each with a count of cards;
(d) feature (MVP) vs harness, and by builder model.
Then the full per-card table (touches by kind, total, wall days first draft to DEPLOYED or open, feature or harness), the top 10 by touches with one-line main cause, and a summary for him of at most 10 bullets, plain words, first line the average touches per item.

FOR THE CHECK: touches survey 2026-10-13 his refinement: standard touches per card type defined (8 build card, 7 docs card, 2 survey); rework = every touch beyond, including spawned unblock cards; rework ranked by cause, feature vs harness, by model
