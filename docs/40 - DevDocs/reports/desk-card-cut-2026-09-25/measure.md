# MEASURE — the desk's wake-up read, today vs after the cut

Measured 2026-09-25 06:4x–06:51 ET (`date` 06:51:40 at the report pass) with `wc -c`, `sed -n '<a>,<b>p' <file> | wc -c`, `awk '/^## NOW/{f=1} /^## Canonical/{f=0} f' areas/cobalt.md | wc -c`, `git -C /Users/cobalt/cobalt log --oneline -5 | wc -c`, `ls prompts/2026-09-25/ | wc -c`. Tokens = bytes ÷ 4 (the card's estimate; UTF-8 punctuation makes it a floor). `cto-2026-09-25.md` is a LIVE file (130,264 B at 06:41, 140,712 B at 06:51) — its sections are the 06:51 snapshot, line numbers of that moment.

## Per item

| card item | what is read | TODAY bytes | ≈ tokens | AFTER bytes | ≈ tokens |
|---|---|---:|---:|---:|---:|
| — | `prompts/CTO-DESK-WAKEUP.md` itself (the launch prompt) | 12,053 | 3,013 | 12,471 | 3,118 |
| 1 | `INDEX.md` | 1,838 | 460 | 1,838 | 460 |
| 2 | `## NOW` of `areas/cobalt.md` | 1,571 | 393 | 1,571 | 393 |
| 3 | `topics/cto-desk.md` → `topics/cto-desk-contract.md` | 109,997 | 27,499 | 11,914 | 2,979 |
| 4 | `preferences.md` | 1,450 | 363 | 1,450 | 363 |
| 5 | `LAWS.md` in full (L59 — never cut) | 89,839 | 22,460 | 89,839 | 22,460 |
| 6 | `prompts/2026-09-25/` — the listing (see note A) | 382 | 96 | 382 | 96 |
| 6 | `cto-2026-09-25.md` title + `§0 Headline` (lines 1–5) | 646 | 162 | 646 | 162 |
| 6 | `## §4` — TODAY all rows R1–R33 (lines 6–42) → AFTER header + rows after the 06:08 HANDOVER, R21–R33 (lines 6–8, 29–41; R21 is stamped `06:0x`, read by the overlap clause) | 73,542 | 18,386 | 20,778 | 5,195 |
| 6 | `## §5` — TODAY every row since 00:1x (lines 43–106) → AFTER `## §5 CURRENT` as it would be at 06:51 (6 live sessions + OPEN TO HIM + WATCHES + TIMERS; sample below) | 36,595 | 9,149 | 1,650 | 413 |
| 0 / 6 | the last line (the 06:08 HANDOVER, step 0) | 6,203 | 1,551 | 6,203 | 1,551 |
| 7 | `day-open-2026-09-25.md` | 5,827 | 1,457 | 5,827 | 1,457 |
| 7 | `git log --oneline -5` | 1,182 | 296 | 1,182 | 296 |
| 7a | `SPRINT-LADDER-v0_1.md` "Ladder at a glance" (lines 33–53) | 1,417 | 354 | 1,417 | 354 |
| 7a | S3 section + its `### Status 2026-09-24` (lines 639–685) | 9,949 | 2,487 | 9,949 | 2,487 |
| **TOTAL** | | **352,491** | **≈ 88,123** | **167,117** | **≈ 41,779** |

Saving: 185,374 B ≈ 46,344 tokens (53 % of the card). Against the measured 167,323-token wake-up at 06:10 (which also carries the harness prompt, tool schemas, step 8 and step 9 reads), the same wake-up after the cut would measure ≈ 121,000 — IF step 8 is executed as a status read (note B); ≈ 134,000 if step 8 reads today's §4 in full as written.

## Not in the card total (unchanged by this cut)
- Note A — item 6 says "every file" of `prompts/<today>/`: 610,316 B (≈ 152,579 tokens) today, 16 files at 06:4x. No desk has read that in full (the 06:10 measure is 167k in total); the cut leaves the wording as is. ESCALATE 2 in the report.
- Note B — step 8 RECONCILE reads `## §4 Rulings` of today (73,542 B) AND yesterday (`cto-2026-09-24.md` lines 16–141: 176,914 B ≈ 44,229 tokens) plus the close's laws-fold list. The card said "nothing else changes", so step 8 is untouched; a status read (`grep -n "APPROVED" <file>`, fixed string) is the desk's call. ESCALATE 1 in the report.
- The five older HANDOVER lines between §5 and the last line (lines 107–116): 23,726 B. Item 6 AFTER does not name them; under the new step (3) they are finished rows → `## §5 HISTORY` (a desk reading, ESCALATE 3).
- Step 9 reads each live hub's `§0`, last 15 lines and an ESCALATE grep — per hub, unchanged.

## Sample `## §5 CURRENT` as of 06:51 (measured 1,650 B — the shape, facts copied from the §5 rows of that minute)
```
## §5 CURRENT (06:51 ET, desk `54c31994`)
| id | job | prompt | tab | watch + ceiling | waits for |
|---|---|---|---|---|---|
| `54c31994` | CTO desk (FABLE 5.1, R27 line), rc `cto-desk` | CTO-DESK-WAKEUP | `w2:pF` | — | wake-up measure 167,323 at 06:10 |
| `2f2702f2` | REPLAY DEADLINE FIX BUILD, `acceptEdits`, cwd `~/cobalt-wt/replay-deadline`, L76 lock at D7 | `57` (09-24) | `w2:t9X` | `b6jqyem4i`, ≈07:50 | `^(REPLAY DEADLINE FIX BUILT\|FAILED)` on the worktree's `reports/replay-deadline-fix-build-2026-09-24.md`; then `58` on the house lane |
| `b7ff7d67` | DESK CARD CUT DRAFTER, auto, read-only | `19` | `w2:t90` | `bo18nxyne`, ≈07:52 | `^(DESK CARD CUT DRAFTED\|FAILED)` on `reports/desk-card-cut-2026-09-25.md`; then apply (R28) |
| `1f2be40a` | DRC D4 FIX R1 DRAFTER, auto, read-only | `20` | `w2:tA1` | `b5gkn2601`, ≈07:48 | `^(DRC D4 FIX R1 DRAFTED\|FAILED)` on `reports/drc-d4-fix-r1-draft-2026-09-25.md`; then `21` / `22` |
| `72feb9c8` | VOICE TTS TRIBUNAL R1 HUB, house lane, Grok + Gemini | `16` | `w2:tA2` | `b6kel6ngh`, ≈08:20 | `^(VOICE TTS TRIBUNAL DONE\|FAILED)` on `reports/voice-tts-tribunal-2026-09-25.md` |
| `1b725869` | VOICE TTS TRIBUNAL R1 ANTHROPIC SEAT, blind | `17` | `w2:tA3` | `b2f90napk`, ≈08:20 | `^(VOICE TTS FABLE R1 DONE\|FAILED)` on `reports/voice-tts-tribunal-fable-r1-2026-09-25.md` |
| OPEN TO HIM | (1) 09-24 R107 voice V1 — RULED A (R23); (2) Kokoro — ordered (R23), tribunal running | — | — | — | nothing open |
| WATCHES + TIMERS | `b6jqyem4i` · `bo18nxyne` · `b5gkn2601` · `b6kel6ngh` · `b2f90napk` — all die with this desk; re-arm on wake-up | — | — | — | — |
```
(The OPEN TO HIM cell is the drafter's reading of R23 for sizing only; the desk writes the real one.)
