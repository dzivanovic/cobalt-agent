# MEASURE — the desk wake-up read on the combined final files

Measured 2026-09-28 06:5x EDT by the derive (`startup-shrink-derive-0928`) with `wc -c` / `grep -b` on `final/`. Rows = `PROPOSAL.md` §5 (the rows of `startup-redesign-2026-09-27/final/MEASURE.md`) plus the trigger-fired sections the round-1 seats named (6c–6e, 12b). "09-27 final" = that folder's MEASURE. "after" = `wc -c` of the final file or its start range, or the proposal's estimate MARKED `est.`. Scenario sum, not a measured session. Tokens = bytes ÷ 4 and ÷ 3, planning estimates only.

| # | item | 09-27 final B | after B | source |
|---|---|---|---|---|
| 1 | `cto-<prev>.md` RECONCILE grep | ≈0 est. | ≈0 est. | unchanged |
| 2 | `LAWS.md` (top → `## Reading`) | 53,168 | 9,266 | `grep -b "^## Reading"` = byte 9,266 of `final/LAWS.md` (file 60,554) |
| 3 | `cto-<today>.md` RECONCILE grep | ≈0 est. | ≈0 est. | unchanged |
| 4 | §4 rows after HANDOVER | ≈3,500 est. | ≈3,500 est. | unchanged |
| 5 | `CLAUDE.md` (harness auto-load) | 126 | 126 | `wc -c final/CLAUDE.md` |
| 6 | `topics/cto-desk-contract.md` | 10,641 | 3,875 | `wc -c final/cto-desk-contract.md` |
| 6b | checklist `## handover` (a HANDOVER wake-up only) | 0 | 1,584 | `grep -b`: 234 → 1,818 in `final/cto-desk-checklist.md` |
| 6c | checklist `## replies` (the plate is a reply — contract trigger "Before any reply") | 0 | 703 | `grep -b`: 6,484 → 7,187 |
| 6d | checklist `## reads` + `## watch` (a live hub: READ 6 reads its report, re-arms its watch) | 0 | 1,279 (447 + 832) | `grep -b`: 6,037 → 6,484; 4,821 → 5,653 |
| 6e | checklist `## memory` + `## rulings` + `writing-rules.md` (RECONCILE applies ≥1 row) + each folded entry | 0 | 4,379 (721 + 910 + 2,748) + entries | `grep -b`: 9,607 → 10,328; 1,818 → 2,728; `wc -c final/writing-rules.md` |
| 7 | `prompts/CTO-DESK-WAKEUP.md` | 7,478 | 6,755 | `wc -c final/CTO-DESK-WAKEUP.md` |
| 8 | ladder S3 slice | ≈6,380 est. | 0 (≈6,380 est. while NOW has no sprint line) | ON TRIGGER sprint line (Grok Q1) |
| 9 | one live hub's report | ≈1,821 est. | ≈1,821 est. | unchanged (per hub) |
| 10 | `day-open` VERDICT | ≈741 est. | ≈741 est. | unchanged |
| 11 | §5 CURRENT | ≈4,011 est. | ≈4,011 est. | unchanged |
| 12 | newest close `Laws fold` list | ≈3,392 est. | ≈3,392 est. — every wake-up until §5 identifies that close as fully reconciled | READ 5 (Astra Q7) |
| 12b | that day's `-words.md` lines for each R on the close list | 0 | not measurable from files | READ 5 (Grok Q6) |
| 13 | `areas/cobalt.md` (top → `## Build rules`) | ≈5,275 est. | ≈2,738 est. | `grep -b "^## Build rules"` = 1,623 on `final/cobalt.md` − 77 (the `«snapshot»` line, 931 → 1,008) + 1,192 (today's live NOW body, `grep -b` 619 → 1,811 on `M/areas/cobalt.md`) |
| 14 | `INDEX.md` | 2,042 | 2,128 | `wc -c final/INDEX.md` |
| 15 | HANDOVER last line | ≈66 est. | ≈66 est. | unchanged |
| 16 | `preferences.md` | 953 | 953 | `wc -c final/preferences.md` |
| 17 | Ladder at a glance | 1,417 | 0 (1,417 while NOW has no sprint line) | ON TRIGGER sprint line |
| 18 | `git log --oneline -5` | ≈665 est. | ≈665 est. | unchanged |
| 19 | §0 Headline | ≈561 est. | ≈561 est. | unchanged |
| 20 | prompts listing | ≈400 est. | ≈400 est. | unchanged |
| 21 | `profile.md` | 706 | 706 | `wc -c` live `profile.md` |
| — | **total, first wake-up after a close** (HANDOVER, one live hub, the close list read, nothing folded, NOW carries the sprint line) | **≈103,343** | **≈45,270** | rows 1–21 + 6b + 6c + 6d |
| — | the same with ≥1 row folded | — | ≈49,649 + each folded entry | + 6e |
| — | **total, a REFRESH wake-up** (no newer close, one live hub) | ≈103,343 | **≈41,878** when §5 marks the newest close fully reconciled · ≈45,270 when it does not | − row 12 |

Scenario adjustments: a crash wake-up (no HANDOVER) −1,584 (row 6b); each further live hub +≈1,821 est.; the first wake-ups after apply, until a close writes NOW's sprint line (live NOW has no stop date), +≈7,797 est. (rows 8 + 17).

Tokens: first wake-up after a close ≈45,270 B ≈ 11,300 (÷4) · ≈ 15,100 (÷3); refresh ≈41,878 B ≈ 10,500 (÷4) · ≈ 14,000 (÷3).

Always-loaded block (INDEX + profile + preferences, final): `wc -m` = 2,060 + 691 + 939 = 3,690 characters — under 4,000 (`wc -c` 2,128 + 706 + 953 = 3,787 B).

Against the proposal's ≈42,510: +2,760 B, named — `## replies` now fires on the plate (+703), `## reads` + `## watch` fire with a live hub (+1,279), the handover section grew with the sprint-line clause (+125), contract +137 (the ASK DESK reply and watch triggers), wake-up +301 (RECONCILE wording, the sprint-line trigger, "Planning"), cobalt.md desk range +148 (the resolver wording and the tags on their own lines) with the NOW operand re-measured (−29), INDEX −22, LAWS Index header +118.

What the next desk's measure can and cannot test: its first §5 MEASURE (`desk-context.sh` tokens against the 136,059 baseline and the 09-28 121,474) tests whether a whole wake-up got cheaper on that day; it cannot prove this byte table, the ÷4 conversion, whether its tools read `LAWS.md` and `areas/cobalt.md` by range or whole (a whole read = 60,554 / ≈5,687 B instead of the slice — X9), or row 12b — so the byte figure is checked only by the per-file `wc -c` of each file that wake-up opened, which the VERIFY step logs beside the token figure.
