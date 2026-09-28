# MEASURE — the desk wake-up read on the final files

Measured 2026-09-27 ≈23:5x EDT by the derive (`startup-derive-0927`) with `wc -c` on `final/`. "before" = the sitting's Measure rows 1–20 (`reports/desk-startup-tuning-2026-09-27.md:18–37`, sum 301,337 — hub CK25 ARITHMETIC OK). "after" = `wc -c` of the final file, or the proposal's estimate MARKED `est.` (`PROPOSAL.md` "After T19" and its earlier tables). Tokens = bytes ÷ 4 and ÷ 3, planning estimates only.

| # | item | before B | after B | source |
|---|---|---|---|---|
| 1 | `cto-<prev>.md` RECONCILE grep | 85,956 | ≈0 est. | PROPOSAL "After file 2": pending-fold grep, 0 pending rows that day |
| 2 | `LAWS.md` | 89,839 | 53,168 | `wc -c final/LAWS.md` (draft 40,617; +12,551 = the live sentences restored, LAW PRESERVATION) |
| 3 | `cto-<today>.md` RECONCILE grep | 20,874 | ≈0 est. | as row 1 |
| 4 | §4 rows after HANDOVER | 19,443 | ≈3,500 est. | PROPOSAL:78 (19,443 − 15,943); PROPOSAL:38 says ≈1,600 (hub CK27: the two disagree) |
| 5 | `CLAUDE.md` (harness auto-load) | 16,590 | 126 | `wc -c final/CLAUDE.md` |
| 6 | `topics/cto-desk-contract.md` | 14,553 | 10,641 | `wc -c final/cto-desk-contract.md`; the live file is 16,153 today (the sitting's 14,553 is older) |
| 7 | `prompts/CTO-DESK-WAKEUP.md` | 13,102 | 7,478 | `wc -c final/CTO-DESK-WAKEUP.md` |
| 8 | ladder S3 slice | 9,949 | ≈6,380 est. | PROPOSAL "After file 2" |
| 9 | one live hub's report read | 7,860 | ≈1,821 est. | PROPOSAL row 16 (per hub; × live hubs) |
| 10 | `day-open-<today>.md` | ~5,800 | ≈741 est. | PROPOSAL row 11 (`## VERDICT` only) |
| 11 | §5 CURRENT | 4,011 | 4,011 est. | unchanged by the design |
| 12 | newest close Laws-fold list | 3,392 | 3,392 est. | unchanged by the design (read when a close is newer than the last reconcile) |
| 13 | `areas/cobalt.md` (was NOW + frontmatter only) | 1,902 | ≈5,275 est. | `wc -c final/cobalt.md` 4,067 − the 76 B «snapshot» line + NOW ≈1,284 (PROPOSAL:49 estimate); now read whole |
| 14 | `INDEX.md` | 1,912 | 2,042 | `wc -c final/INDEX.md` |
| 15 | HANDOVER last line | 1,655 | ≈66 est. | PROPOSAL row 3 (the pinned shape) |
| 16 | `preferences.md` | 1,456 | 953 | `wc -c final/preferences.md` |
| 17 | Ladder at a glance | 1,417 | 1,417 est. | unchanged |
| 18 | `git log --oneline -5` | 665 | 665 est. | unchanged |
| 19 | §0 Headline | 561 | 561 est. | unchanged |
| 20 | prompts/<today>/ listing | ~400 | ~400 est. | unchanged |
| 21 | `profile.md` (newly on the start path) | 0 | 706 | `wc -c` live `profile.md` (unchanged file) |
| — | `writing-rules.md` | 0 | 0 | final INDEX puts it under `## before writing` — "do not open it at start" |
| — | **total** | **301,337** | **≈103,343** | rows 1–21 |

Tokens: before 301,337 B ≈ 75,300 (÷4) · ≈ 100,400 (÷3); after ≈103,343 B ≈ 25,800 (÷4) · ≈ 34,400 (÷3). Removed ≈197,994 B ≈ 49,500 tokens (÷4) = 36% of the measured 136,059; ≈ 66,000 (÷3) = 49%.

Always-loaded block (INDEX + profile + preferences, final): 2,042 + 706 + 953 = 3,701 B; `wc -m` = 1,974 + 691 + 939 = 3,604 characters — under 4,000.

Against the proposal's ≈82,800: the final is ≈20,500 B heavier — LAWS +12,551 (the restored law sentences), contract +1,590 (the six live rules carried and the words pointer), wake-up +1,237 (the SEAT PROFILE and HANDOVER wordings the houses gave), INDEX +554, cobalt.md +964 over PROPOSAL:49's 4,311, preferences +43; and ≈3,608 B of the gap is arithmetic, not files: PROPOSAL "After file 2" subtracts a 24,012 B base for CLAUDE + INDEX + cobalt.md (16,590 + 1,912 + 5,510) where the sitting's table carries 20,404 (rows 5 + 13 + 14; row 13 is NOW + frontmatter, 1,902, not the whole file) — the derive's own arithmetic, UNCHECKED by a hub.

What the next desk's measure can and cannot test: its first §5 MEASURE (`desk-context.sh` tokens against 136,059) tests whether a whole wake-up got cheaper on that day; it cannot prove this byte table, the ÷4 conversion or the harness share of the 136,059 (experiment X7), and the first wake-up after apply still reads the day's pre-apply §4 rows (Grok Q9) — so the byte figure is checked only by the per-file `wc -c` the VERIFY step logs beside the token figure.
