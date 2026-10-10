# F4 tribunal derive — 2026-10-10 (seat `f4-tribunal-derive-1010`, `claude-opus-5-5`)

## §0 Headline
- I derived a **DRAFT FINAL**: `docs/30 - Design/F4-FINAL-2026-10-10.md`. It has 25 fold rows, 10 house wordings adopted verbatim, and **7 items that need round 2** (C4 with (b), C6, C7, C9, C11, S1, C8's stub case).
- There are no owner items. No house is absent: Astra, Grok and Gemini all ruled round 1 in full, and the floor is MET.
- A Gemini finding held: **yes**. Gemini findings held: 6 of 12. Of the six, only F33 was Gemini's alone (it supports C1). Gemini's "False COBALT: None" (F7) does not hold.
- I hold a side (the Anthropic house proposed and ruled round 1), so I recommend nothing. ESCALATE: 10.

## DIGEST FOR THE DESK
- Changed from the proposal, item by item:
  - C1: Astra's wording folded. Refresh never calls rules regeneration, absent-note create included (F2 HOLDS).
  - C2: values kept, `status: proposed`. Measurement is X8; Astra's admission clause rides R2-4.
  - C3: proposal kept.
  - C4: ROUND 2 (R2-1). The proposal's per-row rule (a) does not survive F6; the calendar text contradicts itself (F5).
  - C5: Astra's wording folded (exact keys, the placeholder stays manual, typed cells kept byte for byte).
  - C6: ROUND 2 (R2-2) on stamp ownership and where the calendar flag lives. Place and ET zone are agreed.
  - C7: ROUND 2 (R2-3) on the exit code for a degraded refresh and where the value age comes from.
  - C8: Astra's wording folded (shared create-if-absent, no regeneration, re-read on a create race). The stub-note case is ROUND 2 (R2-7).
  - C9: ROUND 2 (R2-4). Astra REJECTs leaving refresh out of the L53 gate, and F27 holds behind it.
  - C10: proposal kept.
  - C11: ROUND 2 (R2-5). Does Charter:82-83 "Cobalt blocks stamped" reach the rules unit? FC20 holds that the rules block is a Cobalt block.
  - C12: proposal kept, by law (L29, L67).
  - S1: ROUND 2 (R2-6). A second `daily_note_path` would duplicate daymode's (FC25 HOLDS).
  - S2, S3: Astra's wordings folded (config.py and cli.py ownership; real-writer concurrency proof).
  - (a): Astra's wording plus the Opus seat's added facts, folded (FC1–FC4 hold).
  - (b): goes to round 2 with C4.
  - (c): proposal kept (L52 not triggered).
  - (d): the seam is completed from rows that hold (F13, F23, FC4).
  - (e): Grok's "ONE chunk" folded.
  - (f): Astra's wording folded. RESTARTS adds radar (FC1).
  - EXPERIMENTS: Astra's wording folded; X1–X10 deduplicated across houses.
  - WRONG FACTS: corrected where the hub's rows hold.
- Round 1: Astra in full (21 of 21, `ADOPT AFTER …`), Grok in full (`ADOPT AFTER C4 latch, baseline, sync wording`), Gemini in full (`ADOPT`). None PARTIAL, none NOT SEATED, none on METER.
- Opus seat: 24 claims hub-checked (18 HOLD, 1 DOES NOT HOLD (FC8), 5 UNVERIFIABLE), plus 2 not counted (FC22 arithmetic, FC26). None were left UNCHECKED, and I needed no derive-read of a seat claim to take a wording. 3 WITHDRAWN claims, none folded.
- Self-assignments: none folded as MEASURED. The C12 build seat stays as RULED by law (L29, L67). Four were left out as UNMEASURED: Grok C12, Grok (e), Opus seat C12, Opus seat (e).
- Round 2 covers 7 items. Each is a place where two houses disagree on whether a mechanism is correct, or where a house REJECTs (C9). Detail is under `## NEEDS ROUND 2`.
- Chunks: one, F4-1. Builder Opus 5.5 (L29); never auto mode on the build launch; check flow L67 with MANDATORY house B; no migration; with-DB tests T1, T2, T3, T4, T7, T8, T9, T11 under the L76 lock. It is gated by X1–X10 and by round 2 closing.
- RESTARTS (derived): `com.cobalt.aset` and `com.cobalt.radar` restart; `com.cobalt.prefill-refresh` is loaded (one-shot).
- Hours, all GUESS and unmeasured: Grok 8 h · Astra 12–20 h · Gemini ~5.5 h · Opus seat 6–8 h. The proposal gives none.

## Fold table
| F-nn | Item | Houses that ruled it | Whose wording | Adopted verbatim? | SELF | Gemini finding held? | Why |
|---|---|---|---|---|---|---|---|
| F-01 | C1 | 3 of 3 (Astra AW, Grok A, Gemini A) + Opus seat A | Astra | yes | no | yes (F33) | Checked F2 HOLDS (absent-note path regenerates rules). Grok's C8 says the same. No competing wording. |
| F-02 | C2 | 3 of 3 (Astra AW, Grok A, Gemini A) + seat A | proposal kept | not taken | no | yes (F17 arithmetic) | Astra's last clause is C9's REJECT, so the round-2 question; values stay `status: proposed`. Measurement is X8. |
| F-03 | C3 | 3 of 3 A + seat A | proposal kept | no (proposal kept) | no | n/a (no finding) | All four ADOPT. |
| F-04 | C4 | 3 of 3 (Astra AW, Grok AW, Gemini A) + seat AW | none: ROUND 2 (R2-1) | not taken | no | no (F7 DOES NOT HOLD) | F5 and F6 hold against the proposal. Astra and Grok disagree on calendar latch, insertion position and snapshot timing. Writer extension (Astra) is larger. |
| F-05 | C5 | 3 of 3 (Astra AW, Grok AW, Gemini A) + seat AW | Astra | yes | no | n/a (no finding) | Equivalent to Grok's strict five keys, plus the placeholder-stays-manual rule. Seat's FC16 is UNVERIFIABLE (X1/T17). |
| F-06 | C6 | 3 of 3 (Astra AW, Grok A, Gemini A) + seat AW | none on ownership: ROUND 2 (R2-2) | not taken | no | n/a (no finding) | F30 HOLDS (regex claims a human line). Astra keeps his stamp, Grok replaces it under L28. Calendar flag place is tied to R2-1. |
| F-07 | C7 | 3 of 3 (Astra AW, Grok A, Gemini A) + seat AW | none: ROUND 2 (R2-3) | not taken | no | n/a (no finding) | F34: Grok says exit 0, Astra says exit nonzero; the two disagree on lawfulness under L1/L9. FC9 HOLDS. Age source contested. |
| F-08 | C8 | 3 of 3 (Astra AW, Grok AW, Gemini A) + seat AW | Astra | yes | no | n/a (no finding) | F2, FC19 HOLD. Grok's equal wording is not taken; Astra's adds the create-race rule (L28). The seat's regeneration wording is not taken. The stub case goes to R2-7. |
| F-09 | C9 | 3 of 3 (Astra REJECT, Grok A, Gemini A) + seat A | none: ROUND 2 (R2-4) | not taken | no | no (F29 DOES NOT HOLD) | A REJECT whose claim HOLDS (F27). Astra's price is demand call sites plus tests; the proposal's is inventory text only. |
| F-10 | C10 | 3 of 3 A + seat A | proposal kept | no (proposal kept) | no | n/a (no finding) | All four ADOPT. |
| F-11 | C11 | 3 of 3 A + seat AW | none: ROUND 2 (R2-5) | not taken | no | n/a (no finding) | FC20 HOLDS: the Charter (his text) stamps Cobalt blocks. The seat's wording hands the derive a question it cannot settle. |
| F-12 | C12 | 3 of 3 A + seat AW | proposal kept (law: L29, L67) | no (proposal kept) | Grok yes UNMEASURED; seat yes UNMEASURED | n/a (no finding) | SELF UNMEASURED (Self-assignments rows Grok C12, Opus C12). The seat stays as L29/L67 leave it. |
| F-13 | S1 | 3 of 3 (Astra AW, Grok A, Gemini A) + seat AW | none: ROUND 2 (R2-6) | not taken | no | n/a (no finding) | FC25 HOLDS: a new `daily_note_path` duplicates daymode's (L3). The seat's `ensure_daily_note` regenerates, against F-08. |
| F-14 | S2 | 3 of 3 (Astra AW, Grok A, Gemini A) + seat A | Astra | yes | no | yes (F13) | F13 HOLDS (config.py was missing from the seam). Consistent with every ruling. |
| F-15 | S3 | 3 of 3 (Astra AW, Grok A, Gemini A) + seat A | Astra | yes | no | n/a (no finding) | F10 HOLDS (retry reuses a fixed body). Grok's F5-off-cli.py was a finding, not a wording. |
| F-16 | (a) | Astra AW; Grok, Gemini findings + seat AW | Astra | yes | no | yes (F1); no (F15) | F8 HOLDS. F9 is UNVERIFIABLE, so Astra's replacement drops that claim. Gemini's F15 citation does not hold. |
| F-17 | (a) | as F-16 | Opus seat (additive) | yes | no | n/a | FC1, FC2, FC3, FC4 HOLD. No house wording competes; facts only. |
| F-18 | (b) | Astra AW; Grok, Gemini findings + seat AW | none: ROUND 2 (with R2-1) | not taken | no | no (F7); yes (F19) | Astra's (b) builds on her C4 writer extension, which is in round 2. F7 DOES NOT HOLD. |
| F-19 | (c) | Astra AW; Grok, Gemini findings + seat AW | proposal kept (L52 not triggered) | not taken | no | yes (F17) | Astra's exit clause is R2-3. The seat's wording cites `is_missed`, FC8 DOES NOT HOLD. |
| F-20 | (d) | Astra AW; Grok, Gemini findings + seat AW | none whole; seam completed from held rows | not taken | no | yes (F13); no (F14) | Astra's text carries the round-2 writer and demand items. The seat's text depends on S1 and lists generated.yaml under its own C8. F13, F23, FC4 HOLD. |
| F-21 | (e) | Astra AW; Grok text; Gemini text + seat AW | Grok ("ONE chunk" and its reason) | yes | Grok yes UNMEASURED (seat part not folded) | yes (F20) | Smaller mechanism. Astra and Gemini take two chunks (an extra stop and check point). SELF UNMEASURED: seat clause dropped. Hours 5.5–20 GUESS. |
| F-22 | (f) | Astra AW; Grok, Gemini findings + seat AW | Astra | yes | no | no (F18 UNVERIFIABLE) | Radar is added by L42 rule from FC1 (it reads tunables). The seat's equal wording is not taken (house preferred). |
| F-23 | EXPERIMENTS | all | Astra | yes | no | n/a | The X list is deduplicated from the hub's L70 table; every UNVERIFIABLE row is placed there. |
| F-24 | OWNER | all say none | proposal kept | no (proposal kept) | no | yes (agrees) | No item passes the owner test; L53's ceiling and scan cadence are unchanged. |
| F-25 | WRONG FACTS | all | corrections from held rows (F8, F2, F13, F22, FC1, FC2) | no | no | yes (F1, F13); no (F15) | Applied by file-check row. Gemini's WRONG FACT 3 does not hold (F15). |

(AW = ADOPT WITH; A = ADOPT.)

## NEEDS ROUND 2
**R2-1 · C4 + (b): the ownership mechanism.**
- Grok: “Refresh classifies, then builds the cobalt proposal from `last_after`'s unit body … The word `human` in the stamp is the latch … An insertion whose anchor is a base line the proposal replaces is emitted after that replaced line … Text survives; byte position does not. … Reordering `pending` ahead of the replacement would be a one-path change to `merge.py` for every writer; not in F4.”
- Astra: “compute them against the writer’s current snapshot on every attempt. Extend the existing writer with an optional snapshot-bound body builder … Carry human additions once, in position: fix and test identical human/proposal insertions in the existing merge. Never use a timestamp-shaped line as proof of ownership.”
- Gemini: ADOPT of the proposal's disk-built rule, resting on F7, which DOES NOT HOLD.
- The Anthropic seat: baseline-built, plus a per-note lock (FC15, UNVERIFIABLE).
- Round 2 must answer, against L28's "human text preserved verbatim in position": (i) the calendar flag, written inside the unit as a latch, or the unit left byte-identical with the flag outside it? (ii) may an insertion anchored on a replaced line move, or must `merge.py` keep it in place? (iii) is ownership computed once, or per write attempt (F10)? X1, X2 and X4 supply the data.

**R2-2 · C6: stamp ownership.**
- Proposal / Grok (ADOPT): “A line matching `^as of \d\d:\d\d ET` inside the unit is Cobalt's and is replaced” (R5 "Accepted").
- Astra: “Preserve a human-edited stamp and any timestamp-shaped human insertion … A human-owned calendar unit remains byte-identical; its human flag is reported outside that unit.” The Anthropic seat agrees on keeping his stamp edit.
- Question: may Cobalt replace a stamp line he edited (F30 HOLDS; FC17 → T16)?

**R2-3 · C7: degraded refresh.**
- Grok: “Exit 0: the job result lists every degraded field (L1's degraded form, not a silent blank).”
- Astra: “Refresh exits nonzero for degradation. Never derive value age from the latest attempt stamp.” The Anthropic seat agrees and cites FC9: F17 marks a run failed only on an exception.
- Question: is exit 0 with listed fields lawful under L1/L9, and is the age read from the previous stamp or from the last success?

**R2-4 · C9 (with C2's admission clause): L53 total demand.**
- Astra REJECT (quoted whole in `## Dissents, verbatim`).
- Grok: “Adding a positive prefill rpm on top of a ceiling-bound radar can refuse the gate … X4, and it is not required to adopt the omission.” Gemini and the Anthropic seat ADOPT the omission.
- Question: does L53's "test proving refusal when the total exceeds the ceiling" require refresh demand inside the gate, and if so, what lawful allocation is there with radar declared at the ceiling (F27), without touching his ceiling or scan cadence? X8 supplies the data.

**R2-5 · C11: the rules-unit stamp against the Charter.**
- Grok: “M1's "stamped as of 05:15" is satisfied by the refreshable units plus the header time.” Astra and Gemini ADOPT no stamp.
- The Anthropic seat: “Charter:82-83 (his text): "the note exists at 05:15 with Cobalt blocks stamped 'as of HH:MM'". Rules is a Cobalt block” (FC20 HOLDS).
- Question: does the Charter's acceptance text require a stamp on the rules unit, and on the daymode unit?

**R2-6 · S1: path helper and `ensure_daily_note`.**
- Astra: “exports `daily_note_path(when: datetime) -> Path` … All require an aware instant and derive the note date and stamp in ET.”
- The Anthropic seat: “F5 imports `cobalt.daymode.note.daily_note_path(day)` … F4 adds no second path helper (L3).” FC25 HOLDS; the signatures differ (`date` vs `when`).
- Question: reuse daymode's helper (fed an ET date from an aware instant) or add a new one, under L3? And what is `ensure_daily_note`'s contract, given that F-08 forbids regeneration?

**R2-7 · C8: the stub note.**
- The Anthropic seat: “When today's note is absent, or present without a `trading` unit (the sheet's stub, aset/daily_note.py:103-104, :184), `prefill refresh` calls `run_daily_prefill(when)` — rules regeneration included”. FC2 HOLDS that the stub exists.
- Astra and Grok forbid regeneration from refresh. Neither covers a note that exists without a `trading` unit.
- Question: what does refresh do with a stub note, without regenerating rules?

## OWNER ITEMS
none. Astra, Grok, Gemini and the Opus seat each say none, with reasons (hub `## OWNER ITEMS`). No house claims the refresh cadence is L53's to him, and every house says his ceiling and scan cadence are unchanged.

## FOR DEJAN
- What you'll see in your daily note after the deploy:
  - Above the market table and the calendar, one line: `as of HH:MM ET · SPY cobalt · …`.
  - `n/a (manual)` in the VIX and BTC cells until you type in them.
  - A cell you edited stays yours through the day. How that is guaranteed is still in round 2.
  - When Finviz is down, the last numbers stay with a `cobalt-degraded … values as of HH:MM` flag.
- Cost: about 3 Finviz requests per refresh, every 30 min from 05:45 to 15:45 ET (a proposed value).
- At deploy, the sheet (aset) and the radar restart once. How long the sheet is down has not been measured.
- Owner items: none.
- The one approval, "approve the F4 FINAL?", comes after round 2. It is not asked now.

## ABSENT HOUSES
none. Astra, Grok and Gemini all ruled round 1 in full (hub stop line: `houses that ruled: 3 of 3 seated`).

## SEAM
- Design: `docs/30 - Design/F4-FINAL-2026-10-10.md` `## SEAM`.
- UNSETTLED (L72), reading only until round 2 closes:
  - §2: the `daily_note_path` and `ensure_daily_note` signatures F5 imports (R2-6). `format_stamp(when) -> str` is settled.
  - §5: `writer.py` / `merge.py` ownership (R2-1) and `daymode/note.py` (R2-6).
  - §7: Finviz demand (R2-4).
- F5's card should not launch on those lines before round 2.

## Redactions
0. Neither file copies a value of his. The houses' illustrative prices (Astra's synthetic tokens, Grok's "illustrative", Gemini's walk values) were not copied.

## READING
- LAWS.md whole (397 lines).
- Hub report whole.
- `astra-ruling.md`, `grok-ruling.md`, `gemini-ruling.md` whole.
- Opus-seat report whole.
- Proposal, seam doc and drafter report whole.
- R849, R860, R866 (`cto-2026-10-10.md`), R109 (`cto-2026-09-22.md:56`), R95 and R97 (`cto-2026-09-23.md:103`, `:105`), each by grep.
- Charter:80-88.
- `configs/cobalt/generated.yaml` (grep `prefill`: `:36`).
- The desk file was re-grepped for `derive seat` at 13:22 after it changed on disk. It still has only R876.
- Not opened: other code files. No fold turned on a claim the hub had not checked, except `generated.yaml:36`, which I read myself.

## L74
A system message in this session asked for a `Claude-Session:` line in commits and PR bodies and named a file-send tool. It did not arrive inside a tool result, and this seat makes no commit or PR and sends no file, so nothing was acted on. Recorded once.

## ESCALATE
1. **Precondition to approval and build**: round 2 is owed on R2-1 to R2-7. The FINAL's §4.4, §4.5 (stamp ownership), §4.7, C9, C11 and the S1 helpers are not buildable until it closes.
2. **A DOES-NOT-HOLD wording a house still presses**: Gemini's C4 ADOPT rests on "False COBALT: None" (F7, DOES NOT HOLD).
3. **DOES-NOT-HOLD citations**: Gemini F14, F15, F16, F29; Grok F28, F29 (packet offsets); the Opus seat's FC8 (`is_missed`, `jobs/config.py:94-101`). The seat's (c) wording is not folded for that reason.
4. **House numbers without their measurement**: Gemini "~150 lines … ~50 lines" and "1–2 second websocket reconnection … zero data loss" (F18). The cadence values 30 min, 05:45–15:45 and `timeout_s: 300` stay `status: proposed` (Astra: "UNVERIFIED candidates"). The hours are GUESS: Astra 12–20, Grok 8, Gemini ~5.5, Opus seat 6–8.
5. **Self-assignments UNMEASURED (4)**, none folded: Grok C12, Grok (e), Opus seat C12, Opus seat (e). The build seat stays as L29 and L67 leave it.
6. **Clauses the fold drops**:
   - the proposal's §4.1 "it runs the `daily` path first" (replaced by F-01 and F-08);
   - the Opus seat's C8 and S1 regeneration wording;
   - its (d) row "`generated.yaml:36` `written_by` names both jobs";
   - its (c) exit table (FC8);
   - its C12 and (e) wordings (SELF UNMEASURED);
   - Astra's C2, (c), (d) and (e) wordings (they depend on round-2 items);
   - Grok's C5 and C8 wordings (equivalent Astra wordings taken).
7. **The Charter acceptance clause** "Cobalt blocks stamped" is uncertified until R2-5 closes.
8. **Precondition to the build's scheduled writer**: X1–X10 run first. Astra's C12 note that "The permission gate must be proven before write-path work; this packet supplies no such check record" is carried for the card.
9. **The Opus seat's BLIND disclosure** (its ESCALATE 1, hub FC26): its `git status` printed the hub report's filename. The desk judges it.
10. **Hub packet notes, carried**: L8 was not staged (F12); the writer excerpt cut `_seed_baselines` (F25, settled by FC11); houses cited packet offsets as real-file lines.

## CONTINUE
done 13:25 ET: both files written. Next (not this seat's): the desk commits both files and drafts a round-2 hub for R2-1…R2-7 only, on hub 237's shape with the same approved strings.

F4 DERIVED · DRAFT FINAL · folds: 25 · verbatim: 10 · needs round 2: 7 · owner items: 0 · gemini findings held: 6 of 12 · absent houses: none · ESCALATE: 10
