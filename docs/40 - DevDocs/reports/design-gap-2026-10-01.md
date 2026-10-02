# Design gap — what the redesigned workflow still needs to land (2026-10-01 20:40 ET)

Asked by Dejan (cto-2026-10-01.md R40): looking at the brain's rulings, what is missing so the process works as designed.
Sources read: `brain-workflow-review-2026-10-01.md` (§0, FOLLOWED, CLASSIFIER, RECOMMENDATIONS), `brain-parallel-builds-2026-10-01.md` (§0, RULINGS), `plans/fixed-files-2026-09-30/` listing, `prompts/CHECK-HUB.md` `## 1`, `ops/desk/`, today's §4.

## §0 Headline
- Worker step scripts were never part of the installed design. The 09-30 "new scripts" (his words, `cto-2026-09-30-words.md` R69) were the desk's scripts (`desk-launch.sh`, list, wait, measure) and six fixed files with standing bare-command lists. Workers still type each command, and the check stages house copies by retyping file content (`CHECK-HUB.md` `## 1` (3)), which is what blocked `04`.
- Five more pieces are built or ruled but not installed or not run (table).

## Gaps
| # | piece | state on disk | what lands it |
|---|---|---|---|
| G1 | worker step scripts (one script per fixed-file step: stage, lock take/release, suites, house start) | never designed; one exists since 20:35: `ops/desk/stage-copy.sh` (R37, R39) | a design card, then a build, check, deploy; each fixed file's list shrinks to its scripts |
| G1a | one bare command per call, enforced (his R44) | not built | tomorrow's G1 card carries the brain's 3 parts (`cto-2026-10-01-words.md` `## R45`): guard with NOT A REFUSAL message, the resend law line, `--append-system-prompt` on the desk and worker launch lines; proof `ls && ls` |
| G2 | the lock scripts + amended L76 (brain parallel-builds A, his R17–R20) | built `ad114188` (tip `a9339f0a`), check not run, not installed; L76 "in force at install" | `07` check, then the desk installs the two symlinks |
| G3 | desk-size guard (launch refused at ≥300,000) | check pass 1 `ready: NO`, house B owed | PASS-2, then deploy |
| G4 | the nightly close (`CLOSE-HUB.md`, installed 09-30) | never run: no `close-*` report exists; main is 85 commits ahead of origin | `desk-launch.sh close <date>` each night |
| G5 | standing `BRAIN-HUB.md` | parked "later" (R5) | a drafter after the brain review |
| G6 | brain review recommendations 7–10 (X5 told + fix card; prefix-widening line; L61 / K19a / `UL:28` interpreter caveat; the auto-mode prose setting) | no 10-01 desk row shows them ruled or done | the desk tells him X5 + files its card; 9 and 10 are his rulings |
| G7 | non-Anthropic desk verbs (X8) | not needed while the desk is Anthropic | before another house takes the desk |
