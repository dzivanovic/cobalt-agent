# F4 tribunal round-3 derive — 2026-10-10 (seat `f4-tribunal-r3-derive-1010`, `claude-opus-5-5`)

## §0 Headline
- Wrote **FINAL WITH OPEN ITEM (R2-4)** over `docs/30 - Design/F4-FINAL-2026-10-10.md`. **R2-7 closed** on Grok's wording verbatim ([F-35]), plus the one [F-26] sentence it needs ([F-36+], R3-F13 HOLDS). **R2-4 stays open on its FORM only.** Inclusion is law (R931). Gemini ADOPTs the strike-loop form with a derived interval; Grok says it is wrong (R3-F3) and gives a fixed-rate form. That goes to him as ONE line.
- Owner items: 0. Absent: Astra, NOT SEATED (reserved for the model tribunal, his R920). Floor MET: Grok and Gemini ruled in full.
- A Gemini finding held: **yes**. Gemini findings held: 9 of 14 (round 3). None of Gemini's wordings was folded: its R2-7 wording carries R3-F6 and R3-F7 (DO NOT HOLD), and its R2-4 ADOPT is one side of the open split.
- I hold a side (the Anthropic house proposed, ruled blind and derived), so I recommend nothing (L37). ESCALATE: 13.

## DIGEST FOR THE DESK
- **R2-4: OPEN.** Split on correctness, not voted (L37, L39):
  - Gemini `ADOPT`: the 278 form as quoted, a derived interval with the schedule as its floor.
  - Grok `ADOPT WITH`: no derived interval; the gate is shown `3/prefill.refresh_interval_min`.
  - Grok's failing sequence against A holds as arithmetic (R3-F3). Gemini's refusal clause in (ii) cannot be checked from reads (R3-F5).
  - Both houses agree on the rest: refresh is passed as `extra`, never sits in `scheduled_consumers`, never refuses the radar, and an unreadable plan means no GET, `cobalt-degraded`, nonzero exit.
- **R2-7: CLOSED** by Grok's wording, verbatim ([F-35]). Both houses ruled ADOPT WITH on the same scope.
  - Gemini's wording was not folded: R3-F6 (`market.py:283`, `calendar.py:284`) and R3-F7 (`daily.py:392-395`) DO NOT HOLD.
  - Grok's carries `daily.py:14-24` and reads no rules (R3-F12, F16, F21, F22 HOLD).
- **[F-26] amended:** one sentence becomes [F-36+], per Grok verbatim (R3-F13 HOLDS; the Opus seat's FC61 makes the same reading). `baseline_missing` now applies only to a unit already on disk.
- **Houses in round 3:** Grok in full, Gemini in full, Astra NOT SEATED. No METER stops.
- **Opus seat:** the hub checked 22 of its claims (FC45–FC66: 15 HOLD, 3 ARITHMETIC OK, 3 UNVERIFIABLE, 1 DOES NOT HOLD). 0 are UNCHECKED, and the derive read no seat claim itself. None of its wordings was taken. Its X8 addition (FC47), X14 and X15 are folded as experiments (X8, X15, X16).
- **Chunks:** one, F4-1.
  - Builder: Opus 5.5 (L29), never in auto mode. Check: L67 with MANDATORY house B. No migration. With-DB tests run under the L76 lock.
  - Gates: X1–X16 run before the scheduled writer loads, with X13 now unconditional. X17–X18 and the form-B clauses of X13 and X14 follow his R2-4 ruling.
- **RESTARTS:** unchanged. `com.cobalt.aset` and `com.cobalt.radar` restart, and `com.cobalt.prefill-refresh` is loaded. Round 3 touches only `prefill/daily.py`.
- **Hours:** all GUESS. Grok 8 h · Astra 12–20 h · Gemini ~5.5 h · Opus seat 6–8 h. [F-35] says "about 12 lines" (unmeasured).

## Fold table
| F-nn | Item | Houses that ruled it | Whose wording | Adopted verbatim? | Gemini finding held? | Why |
|---|---|---|---|---|---|---|
| F-34 | R2-4 (form) | 2 of 2 (Gemini ADOPT, Grok AW) + seat AW | none: OPEN | not taken | yes (R3-F8, F9, F19 HOLD; R3-F10 OK); R3-F5 UNVERIFIABLE, R3-F20 DNH | Split on correctness: R3-F3 (ARITH OK) shows the derived interval admits a true peak of 50.05; Gemini keeps it (R3-F5 → X18). Settled half (counted) is law, R931. |
| F-35 | R2-7 | 2 of 2 (Grok AW, Gemini AW) + seat AW | Grok | yes | yes (R3-F11, F12, F21 HOLD); its wording not folded | Same verdict, same scope. Gemini's cites DO NOT HOLD (R3-F6, F7). Seat's guard and template body are not taken; the house's wording is preferred, and the seat's points go to ESCALATE. |
| F-36+ | [F-26] one sentence (amends F-26) | Grok (Opus seat alike) | Grok | yes | n/a (Gemini amended no folded paragraph) | R3-F13 HOLDS (reading the text): the bare `last_after is None → exit 1` would refuse every stub fill. The duplicate "Do not add a second baseline writer." is kept verbatim. |
| F-37 | EXPERIMENTS (round 3) | Grok, Gemini + seat; hub | Grok (X6, X8, X13, X14), Opus seat (X8 add, X15, X16), hub (X17, X18) | yes | no: Gemini's X13 rests on R3-F20 (DNH) and is not folded; its X6 matches Grok's | UNVERIFIABLE rows R3-F3, F5, F13, F22, FC47, FC57 are gated (L70). The form-B clauses are marked as such. |

(AW = ADOPT WITH. Round-3 Gemini rows: R3-F2, F5, F6, F7, F8, F9, F10, F11, F12, F19, F20, F21, F23, F24, which is 14. Of these, 9 HOLD or are ARITHMETIC OK: F2, F8, F9, F10, F11, F12, F19, F21, F23. F5 is UNVERIFIABLE, F24 is UNVERIFIED, and F6, F7, F20 DO NOT HOLD.)

## OPEN AFTER ROUND 3
**R2-4 · C9: the FORM of refresh's place in the shared Finviz gate.** Inclusion is settled (R931, L53) and is not part of this question.
- **Position A, Gemini (`ADOPT`)**, verbatim. The form as quoted in `278`'s `01-QUESTIONS.md` R2-4 is in the design's §8 R4, word for word. Its operative clause: "refresh's interval is derived from the measured headroom, not fixed at a value; refresh's demand is checked as one more consumer passed as `extra` to the same gate with the radar's planned rate, and refresh is NOT listed in `scheduled_consumers` (`radar/notes.py:329-396`); when no headroom exists, `IntervalRefused` takes refresh to the degraded path". Gemini's (ii), verbatim: "`prefill.refresh_interval_min` (30 min) is the floor under the derived interval (`max(floor_s, derived)` as in `strike/detector.py:108`), not replaced; launchd firings cannot exceed this cadence, and if headroom requires an interval > floor, the run is refused."
- **Position B, Grok (`ADOPT WITH`)**, verbatim. It is quoted whole in §8 R4. Operative: "Otherwise it calls `check_scheduled_demand("prefill-refresh", radar_rpm=planned_rpm, extra=[DemandConsumer(name="prefill-refresh", rpm=3/prefill.refresh_interval_min, window=the DemandWindow of prefill.refresh_window)])` … `prefill.refresh_interval_min` (proposed 30, `source: dwv`, `status: proposed`) is the launchd schedule and the floor. It is not replaced by `poll_interval`." Its defect claim against A: "Showing the derived interval there while launchd still fires every 30 min admits a rate the job does not keep."
- **Hub rows:**
  - R3-F1, R3-F2 and R3-F4 HOLD: the resident waits its derived interval; the plist is fixed at install; `poll_interval` raises only at ≤0.
  - R3-F3 is ARITHMETIC OK (Grok's sequence: a gate peak of 50, a true peak of 50.05). Whether the float sum passes at exactly 50.0 is X17.
  - R3-F5 is UNVERIFIABLE (no one-shot refusal mechanism is in the files) → X18.
  - R3-F20 DOES NOT HOLD (Gemini's X13 expects `IntervalRefused` at headroom 0.05).
  - R3-F9 and R3-F19 HOLD: both forms leave the radar unrefused, and an unreadable plan fetches nothing.
- **Not a house:** the Anthropic seat holds a third reading (no derived interval; the gate is shown 3 rpm for the run's burst; FC47 UNVERIFIABLE, FC48 OK). It is carried, not weighed.
- **The question:** does refresh derive its interval from the headroom, with the 30-min schedule as its floor (A), or show the gate its schedule's fixed rate, `3/prefill.refresh_interval_min` (B)?

## OWNER ITEMS
none. Grok: "Nothing in the two items is his money, his data, his laws, or his trading judgement that no house can decide." Gemini said `none`, and so did the Opus seat. R2-4 is a carried split (L39), not an owner item. No chunk's build depends on an owner item.

## FOR DEJAN
What you'll see in your daily note after the deploy:
- **The stamp line.** One line above the market table: `as of HH:MM ET · SPY cobalt · QQQ cobalt · IWM … · VIX n/a (manual) · BTC n/a (manual) · calendar cobalt`. The rules block opens with `as of 05:15 ET · rules from Rules.md`, and the day-mode line gains an `as of` time.
- **VIX and BTC** show `n/a (manual)` until you type in them.
- **Your edits stay yours.** A cell you edit stays yours all day, and so does a line you insert or a stamp you edit. A calendar you edit is never rewritten.
- **When the sheet made today's note first** (a stub), refresh adds only the market table and the calendar. Your saved cards and the stub stay untouched.
- **When Finviz is down,** or the radar's plan leaves no room under your 50/min ceiling, or the radar's plan can't be read: the last good numbers stay with `cobalt-degraded`, and that job counts as failed. The radar is never refused because of refresh.
- **Cost:** 3 Finviz requests a run, every 30 min from 05:45 to 15:45 ET (a proposed value, measured by X8), counted against your ceiling. At most about 42 vault-write rows a weekday.
- **At deploy,** the sheet (aset) and the radar restart once. How long the sheet is down is not measured (X9).

**R2-4 — how refresh is counted against your 50/min Finviz ceiling** (houses split; no recommendation):
- **A (Gemini):** refresh's rate is derived from the room the radar's plan leaves, with the 30-min schedule as its floor. It fetches whenever any room is left. But with less than 0.1/min of room, the gate counts it at that room while the schedule still sends 0.1/min, a peak of up to 50.05 (R3-F3; X17). Whether a run can refuse "above the floor" is unproven (X18).
- **B (Grok):** refresh is counted at its schedule's fixed 3 requests per 30 min (0.1/min). It fetches only when the plan leaves at least 0.1/min. Otherwise that refresh shows `cobalt-degraded` and the job fails.

Then the one approval: **approve the F4 FINAL?** It is asked with your word on R2-4.

## ABSENT HOUSES
- Astra (OpenAI) was NOT SEATED (reserved for the model tribunal, his R920). Launch row R949 reads `openai seat: held by the model tribunal`.
- No item was one only she could answer. Her round-1 C9 REJECT stays in `## Dissents, verbatim` until R2-4 closes. Its inclusion half is now law (R931).
- Her absence does not hold the FINAL (R860; the floor is MET with Grok and Gemini).

## SEAM
- Design: `docs/30 - Design/F4-FINAL-2026-10-10.md` `## SEAM`.
- Settled in round 3: §6, the stub row ([F-35]: two units only).
- Still UNSETTLED: §7, Finviz demand. Inclusion is settled (R931), and the gate cite is corrected per FC60. The form is OPEN (R2-4), and F5's card does not launch on it (L72).

## Redactions
0. Neither file copies a value of his. The hub staged 0 redactions, and no house text carried user data. The `08:45` / `49.95` / `50` figures in quoted text are design and fixture values.

## READING
- Prompt `280-f4-tribunal-r3-derive.md`, whole.
- LAWS.md, whole (1–401).
- Hub round-3 report, whole.
- `grok-ruling.md`, `gemini-ruling.md` and `01-QUESTIONS.md` (r3), whole.
- Opus seat round-3 report, whole.
- FINAL WITH OPEN ITEMS, whole (304 lines). The round-2 derive report, whole.
- No code was opened: every fold turns on a hub row.
- Preconditions run at 17:27 ET, each as its own call:
  - R109: `cto-2026-09-22.md:56`, committed `75b2aa57`.
  - Launch row R949: `cto-2026-10-10.md:9`, committed `ee8666dc`, carrying all three literals. No later row changes the seat.
  - R931: line 26, committed `ecfc36ec`.
  - Hub and Opus stop lines: committed `7979e772`.
  - R2 derive: committed `c44612dd`. The FINAL had 10 `OPEN AFTER ROUND 2` markers.
  - Floor MET.
  - All 10 launch strings count 1 each in `260`.
  - Session model `claude-opus-5-5` = R949's derive seat = this file's `--model`.

## L74
A system message in this session asked for a `Claude-Session:` line in commits and named a file-send tool. It did not arrive inside a tool result. This seat makes no commit and sends no file, so nothing was acted on. Recorded once.

## ESCALATE
1. **OPEN R2-4 (carried split, L39).** It goes to him as ONE line with the approval; there is no round 4. Gemini (A) and Grok (B) disagree on whether the derived-interval form is correct (R3-F3, R3-F5).
2. **CONTRADICTS L53 / R931:** Gemini's round-2 R2-4 omit position. It is carried in `## Dissents, verbatim` and never folded. No round-3 wording omits refresh, edits the ceiling or cadence, refuses the radar, or reads rules on the stub path.
3. **DOES-NOT-HOLD claims still in house text:**
   - Gemini R2-7: R3-F6 and R3-F7. Its wording is not folded.
   - Gemini X13: R3-F20. Not folded.
   - Opus seat FC54: window end 15:50 versus the design's 15:45. Annotated in X8.
4. **Numbers without their measurement:**
   - Grok: `rpm=3/prefill.refresh_interval_min` (form B), "about 30 lines" and "about 12 lines" (the latter is inside [F-35]).
   - Gemini: "~15 lines", and X13's 49.95.
   - Seat: `rpm=3.0`, the window of 300 s, "~20 lines" and "~25 lines".
   - The cadence stays `source: dwv`, `status: proposed`. The hours are GUESS.
5. **Folded paragraph amended:** [F-26] → [F-36+], one sentence. The replacement repeats "Do not add a second baseline writer." beside the folded copy; both are left verbatim.
6. **Preconditions to build:**
   - His word on R2-4.
   - X1–X16 run before the scheduled writer loads. X17 and X18 run only under form A.
   - A red X16 (his hand-typed table changed, or run 2 not on §4.4) means [F-35] is wrong as folded. It goes to him with the card; there is no round 4.
   - A red X15 adds a strike-side reservation row on the F4 card.
7. **Clauses the fold drops:**
   - Gemini's R2-7 wording, whole.
   - Grok's R2-4 companion edits to §4.2, §6 and §9. They ride with B.
   - From the seat: its R2-4 and R2-7 wordings, its T8 text, its X6 change (FC56, which rests on its unfolded wording) and its X13 change. That X13 change expects a refusal at planned 47.5, which neither house form gives.
   - The FINAL §8 R4 proposal sentence "refuse the radar" is struck (R3-F14, R3-F15).
   - The §6 "NOT in F4" bullet on the gate is struck (inclusion is in F4, R931).
   - The SEAM §7 gate cite `357-363` is corrected to `276-284` / `384-391` (FC60).
8. **Seat points the derive holds a side on (L26, L37), carried for him and the card, not folded:**
   - (a) The burst: 3 requests in one minute versus 3/30 (FC47 UNVERIFIABLE → X8).
   - (b) [F-35] + [F-36+] re-add a trading unit he deleted (markers included) at the next refresh. The seat calls this against L28 human-wins. No hub row checked it, and X16's "not recreated" assertion is recorded as data, not a gate.
   - (c) An unmarked table he types under `### Trading` in a stub may be wrapped as `seed`, with Cobalt winning (FC57 UNVERIFIABLE → X16).
   - (d) The stub body's render path. [F-35] names the inputs but not the template. FC55 HOLDS that the `build_market_table_body` no-table branch renders bare rows with no separator or VIX/BTC rows. T6, T8 and X16 assert the shape.
9. **Carried from the seat's ESCALATE 1 and the round-2 derive's ESCALATE 2:** the read-only rules input for [F-08] / [F-31]'s absent-note create is still unnamed, and `load_rules_config()` is env-blind (R2-F26). Neither paragraph is a round-3 item, so neither is amended.
10. **Hub ESCALATE 10:** R949 is stamped 17:25 ET, while the hub's clock read 17:00 at preflight. Carried, not gated.
11. **Hub ESCALATE 11:** Gemini sat on R949's `gemini: sits`. The hub did not decide L67's R921 case (money, sizing, his vault, or a Grok/Anthropic split). The design writes his vault note, which is one of R921's cases; the derive records this and settles nothing.
12. **Hub packet:** `02-greps.txt` / `02-greps-1.txt` are the hub's transcription and are UNVERIFIED line by line. No fold rests on them alone.
13. **Stale sentences left in place** (not round-3 paragraphs): §4.5's "That `to_et` refuses a naive datetime … the hub did not check it" (FC31, round 2), and the round-2 derive's FOR DEJAN line on Grok's round-2 form (FC62). The latter is not in the FINAL.
- UNMEASURED self-assignments pressed as law: none. RE-OPENS A RULING: none. ASK DESK: none.

## CONTINUE
- 17:27 ET: preconditions all passed (detail under `## READING`).
- 17:29 ET: reads done; decisions taken.
- 17:33 ET: FINAL written in place: 0 `OPEN AFTER ROUND 2` markers left, 15 `OPEN AFTER ROUND 3` mentions, [F-34]–[F-37] present.
- done. Next (not this seat's): the desk commits both files, then brings him `## FOR DEJAN` (the R2-4 line plus the one approval). After his word, it drafts the F4 card from `## CHUNKS` and `## SEAM`.

F4 DERIVED R3 · FINAL WITH OPEN ITEM (R2-4) · folds: 4 · verbatim: 3 · open: 1 · owner items: 0 · gemini findings held: 9 of 14 · absent houses: astra · ESCALATE: 13
