# F4 tribunal round-2 derive — 2026-10-10 (seat `f4-tribunal-r2-derive-1010`, `claude-opus-5-5`)

## §0 Headline
- Wrote **FINAL WITH OPEN ITEMS (R2-4, R2-7)** over `docs/30 - Design/F4-FINAL-2026-10-10.md`. Five items closed, each on a house wording taken verbatim: R2-1, R2-2, R2-5 and R2-6 on Grok's; R2-3 on Astra's position B, which Gemini adopted. Two items stay open: R2-4 (L53 total demand) and R2-7 (the stub note).
- Owner items: 0. Absent: Astra (NOT SEATED: the OpenAI seat was held, R917; OpenAI is reserved, L67 [R920]). The floor is MET: Grok and Gemini ruled in full.
- A Gemini finding held: **yes**. Gemini findings held: 11 of 21. Its R2-3 adoption was folded. Its R2-6 and R2-7 wordings were not: R2-F26 holds against the `load_rules_config()` they rely on.
- I hold a side (the Anthropic house proposed, ruled blind and derived), so I recommend nothing. ESCALATE: 12.

## DIGEST FOR THE DESK
- R2-1: closed on Grok's wording, verbatim ([F-26]). Gemini's ADOPT B gives the same three answers: (i) the calendar stays byte-identical with its flag outside it; (ii) an insertion stays in position through one `merge3` change; (iii) ownership is computed per attempt via `body_fn`. Gated by X1, X2, X4, X11, X12.
- R2-2: closed on Grok's wording, verbatim ([F-27]). His edited stamp stays. Gemini ADOPT B agrees. Gated by T16 under X1.
- R2-3: closed on B verbatim ([F-28]): "Refresh exits nonzero for degradation. Never derive value age from the latest attempt stamp." Gemini ADOPT B. Grok gives the same answers, but its wording is not folded: it carries `cli.py:347`, and R2-F6 DOES NOT HOLD. Gated by X5.
- R2-4: OPEN. Gemini says omit refresh from the gate; Grok says include it and hold it at zero until X8. Grok's wording rests on R2-F7, which DOES NOT HOLD for the radar. One A/B for him, or round 3.
- R2-5: closed on Grok's wording, verbatim ([F-30]): rules and daymode carry `as of HH:MM ET`. Gemini's "no stamp" leaves Cobalt blocks unstamped against his Charter text (R2-F13, R2-F14 HOLD). It is carried as a dissent, not offered as an A/B (L77). Gated by X7.
- R2-6: closed on Grok's wording, verbatim ([F-31]): reuse `daymode.note.daily_note_path(to_et(when).date())`; `format_stamp` stays in `daily.py`; `ensure_daily_note` never regenerates. Gemini agrees on the mechanism, but its wording names `load_rules_config()` (R2-F26).
- R2-7: OPEN. Both houses agree: no regeneration and no `run_daily_prefill` on a stub. They split on which units are added: two (Gemini) or every absent `SLOT_SPECS` slot, rules and daymode included (Grok). Neither wording folds as written. One A/B for him, or round 3.
- Houses in round 2: Grok in full (ADOPT AFTER), Gemini in full (ADOPT), Astra NOT SEATED. Grok's turn ended 12 minutes past its deadline (hub ESCALATE 4).
- Opus seat: 18 claims hub-checked (FC27–FC44, all HOLD), 1 WITHDRAWN, and unrun timing claims that became X11–X13, T2b and T3b. None of its wordings was taken (a house wording was taken each time, or the item is open). No derive read of a seat claim was needed.
- Self-assignments: none in round 2. The build seat stays as the law leaves it (C12: Opus 5.5, house B mandatory).
- Chunks: one, F4-1. Builder Opus 5.5 (L29), never on auto mode. Check flow L67 with MANDATORY house B. No migration. With-DB tests run under the L76 lock. Gated by X1–X12 (X13 if R2-4 closes on inclusion) and by R2-4 and R2-7 closing.
- RESTARTS: `com.cobalt.aset` and `com.cobalt.radar` restart, and `com.cobalt.prefill-refresh` is loaded. The `daymode/note.py`, `writer.py` and `merge.py` changes are classified by `cobalt jobs restarts` on the branch.
- Hours, all GUESS and unmeasured: Grok 8 h · Astra 12–20 h · Gemini ~5.5 h · Opus seat 6–8 h. Round 2's line counts are unmeasured too.

## Fold table
| F-nn | Item | Houses that ruled it | Whose wording | Adopted verbatim? | Gemini finding held? | Why |
|---|---|---|---|---|---|---|
| F-26 | R2-1 (with (b), round-1 F-18) | 2 of 2 (Grok AW, Gemini B) + seat AW | Grok | yes | yes (R2-F2 per-attempt HOLDS); Gemini's wording not folded | (i)–(iii) agree; Grok's is smaller (one merge change, no identical-insert fix). R2-F2, F3, F11, F33 HOLD; R2-F1, F4 → X2, X1. Seat lock not taken (X12). |
| F-27 | R2-2 | 2 of 2 (Grok AW, Gemini B) + seat AW | Grok | yes | yes (F30, r1); R2-F4 UNVERIFIABLE → T16 | Same mechanism; B's 01-QUESTIONS text is elided ("…"), not pasteable. Seat's "fresh stamp above" not taken: one more line and a named false positive. |
| F-28 | R2-3 | 2 of 2 (Gemini B, Grok AW) + seat AW | Astra B via Gemini | yes | yes (R2-F5 HOLDS); folded | Grok's wording carries `cli.py:347` (R2-F6 DOES NOT HOLD), so it is not folded. Not taken: Grok's raise-in-block and baseline-age text (FC9 fact kept). |
| F-29 | R2-4 | 2 of 2 (Gemini A, Grok AW) + seat AW | none: OPEN | not taken | yes (R2-F9, F10); R2-F8 UNVERIFIABLE | Split on correctness: omit (Gemini) versus L53 requires inclusion (Grok). Grok's wording rests on R2-F7, which DOES NOT HOLD for the radar. |
| F-30 | R2-5 | 2 of 2 (Grok AW, Gemini A) + seat AW | Grok | yes | no (R2-F17 DOES NOT HOLD; R2-F14 HOLDS against A) | His Charter text binds (R2-F13, F14 HOLD). Gemini A leaves blocks unstamped and is carried as a dissent. R2-F15 HOLDS; R2-F16 → X7. Not taken: seat's `render_body(as_of)`. |
| F-31 | R2-6 | 2 of 2 (Grok AW, Gemini AW) + seat AW | Grok | yes | yes (R2-F18, F19); Gemini's wording not folded | Same verdict; Gemini names `load_rules_config()`, and R2-F26 HOLDS that it reads the committed file in dev. R2-F18, F20 HOLD; R2-F21 is a citation only. Seat's `stamp.py` not taken. |
| F-32 | R2-7 | 2 of 2 (Grok AW, Gemini AW) + seat AW | none: OPEN | not taken | yes (R2-F22); wording not folded | Split on the units added. Gemini's rewrites [F-08] with `load_rules_config()` (R2-F26). Grok's writes rules and daymode (R2-F25), against §4.3 and its own [F-30]. |
| F-33 | EXPERIMENTS (round 2) | Grok, Gemini + seat | Grok (X1–X10 changes), Opus seat (X11–X13) | yes | n/a (Gemini kept X1–X10 unchanged) | Hub L70 table. Each UNVERIFIABLE row (R2-F1, F4, F8, F16, F27, F29, FC35 timing) is gated. X13 applies only if R2-4 closes on inclusion. |

(AW = ADOPT WITH; A / B = ADOPT A / ADOPT B. No round-1 `[F-nn]` paragraph was amended, so no `[F-nn+]` tag was needed.)

## OPEN AFTER ROUND 2
**R2-4 · C9: L53 total demand.**
- Position A, Gemini (ADOPT A). The quoted A text: “Adding a positive prefill rpm on top of a ceiling-bound radar can refuse the gate … X4, and it is not required to adopt the omission.” Gemini's reason: "Astra's REJECT demands an admission allocation that is mathematically impossible without altering Dejan's ruled ceiling or radar cadence; measurement X8 governs."
- Position B, Grok (ADOPT WITH), verbatim: "`prefill-refresh` is a `DemandConsumer` in `scheduled_consumers` (`radar/notes.py:329-396`). Manual refresh is the same consumer passed as `extra` to `check_scheduled_demand`. Rpm, once admitted, is `3 / prefill.refresh_interval_min` (3 is hub FC5; the interval is the engine tunable already proposed at 30). `check_total_demand` is unchanged: it raises when `peak_rpm > ceiling` (`radar/notes.py:276-284`). When `radar_rpm` is None, radar's rpm is the ceiling (`radar/notes.py:361-362` in the hub's check; the staged function sets `rpm = bound` and `basis = "bucket bound (ceiling)"`). Any positive refresh rpm then refuses every caller, radar included. That refusal must not ship. Until X8 records a measured radar rpm such that the peak with refresh is at or under the ceiling, the listed consumer stays in `counted` with basis `not admitted pending X8` and contributes 0, and refresh fetches nothing (degraded path, R2-3). The same commit that sets a positive rpm enables the fetch. The L53 test calls `check_total_demand` with a fixture ceiling under which refresh alone passes and radar-plus-refresh exceeds, and expects `TotalDemandExceeded`. A string change to `test_finviz_consumers.py:47-48` or the xfail reason at `:71` does not satisfy L53 (`LAWS.md:290-291`). `radar.finviz_max_rpm` and the scan cadence are not edited." Astra's round-1 REJECT is on the same side (in the design's `## Dissents, verbatim`).
- Hub rows that bear on it:
  - R2-F7 DOES NOT HOLD for radar: radar's own admission counts its planned total (`radar/notes.py:440-446`).
  - R2-F8 is UNVERIFIABLE (Gemini's 50 + 3 uses the ceiling as radar's rpm).
  - R2-F9 HOLDS (the ceiling is a ruled value). R2-F10 is arithmetic OK (0.1 rpm).
  - FC27–FC30 HOLD: the strike loop already gates with radar's planned rpm; an unreadable plan counts the radar at the ceiling.
  - L53 (`LAWS.md:290-291`): "A budget check measures total demand across every consumer of a shared transport, with a test proving refusal when the total exceeds the ceiling though one consumer alone would pass."
- The Anthropic seat holds a third form: gate refresh like the strike loop, and never put it in `scheduled_consumers`. It is a seat wording, not a house's. I hold a side and do not weigh it.
- The question: is refresh counted in the shared Finviz gate (B) or left outside it (A)? Under B, which form is a house mechanism question for round 3.

**R2-7 · C8: the stub note.**
- Position A, Gemini (ADOPT WITH), verbatim. It is quoted whole in the design §4.1. The operative clause: "If the note exists without a `trading` unit (such as the sheet's stub, `aset/daily_note.py:103-104`, `:184`), refresh does not call `run_daily_prefill` or rules regeneration; instead, it upserts the refreshable units (`trading/market_table` and `market_calendar/market_calendar`) into the existing file via `upsert_unit` at their configured placements (`TRADING_PLACEMENT`, `MARKET_CALENDAR_PLACEMENT`), leaving all existing stub content intact."
- Position B, Grok (ADOPT WITH), verbatim. It is quoted whole in the design §4.1. The operative clause: "It renders the absent slots from the same read-only inputs as the [F-08] create and `upsert_unit`s each absent slot at its `SLOT_SPECS` placement (`daily.py:463-473`, `:573-588`), then returns."
- Hub rows that bear on it:
  - R2-F25 HOLDS: `SLOT_SPECS` holds rules and daymode, so B writes both.
  - R2-F26 HOLDS: `load_rules_config()` is env-blind, which defects A's [F-08] rewrite.
  - R2-F22 and R2-F23 HOLD: `upsert_unit` appends a missing section, and `create_if_absent` on an existing file writes nothing.
  - R2-F24: B's `daily.py:230-235` cite is wrong; the deleted-branch note is at `:14-24`.
- Neither wording folds as written. So after his word, a house's clean wording is still owed: round 3 for R2-7 only.
- The question: on a stub, does refresh add only the market table and calendar (A), or every missing Cobalt block (B)?

## OWNER ITEMS
none. Grok, Gemini and the Opus seat each said none (hub `## OWNER ITEMS`). Grok's conditional — "A later finding that no positive refresh rpm fits under the measured peak would be his ceiling to change" — is no precondition, and no house says the cadence needs `source: ruling`. R2-4 and R2-7 are carried splits (L39), not owner items.

## FOR DEJAN
What you'll see in your daily note after the deploy:
- Above the market table, one line: `as of HH:MM ET · SPY cobalt · QQQ cobalt · IWM … · VIX n/a (manual) · BTC n/a (manual) · calendar cobalt`. The rules block opens with `as of 05:15 ET · rules from Rules.md`, and the day-mode line gains an `as of` time.
- `n/a (manual)` in the VIX and BTC cells until you type in them.
- A cell you edit stays yours all day. So does a line you insert (at the place you put it) and a stamp line you edit. A calendar you edit is never rewritten: the trading line says `calendar human`.
- When Finviz is down, the last good numbers stay with `cobalt-degraded (finviz fetch failed; values as of <time of the last good fetch>)`, and the job counts as failed. Whether that shows red on mission control is measured before the build (X5).
- Cost: about 3 Finviz requests a run, every 30 min from 05:45 to 15:45 ET (a proposed value). At most about 42 vault-write rows a weekday.
- At deploy, the sheet (aset) and the radar restart once. How long the sheet is down is not measured (X9).

**R2-4 — is the refresh counted in the shared Finviz gate?** (houses split; no recommendation)
- A (Gemini): not counted. Your table refreshes every 30 min as above. The gate does not see those ~3 requests a run, and the L53 refusal test is not written for them. Astra (round 1) rejected this.
- B (Grok; Astra round 1; the Anthropic seat): counted before it fetches. When the gate has no room, that refresh fetches nothing, so you see the `cobalt-degraded` flag and a failed job. In Grok's form, refresh fetches nothing at all until a measurement (X8) shows room. The exact form is settled in round 3.

**R2-7 — the sheet made today's note before 05:15 ran: what does refresh add?** (houses split; no recommendation)
- A (Gemini): only the market table and the calendar. The rules block is not added that day.
- B (Grok; the Anthropic seat similar): every missing Cobalt block — rules (read from Rules.md, nothing regenerated), day mode, market table, calendar — once, then normal refreshes.
- Either way the cards you saved and the stub stay untouched. The final wording comes from round 3 on this item alone.

Then the one approval: **approve the F4 FINAL?** — asked once, after your word on R2-4 and R2-7, or after round 3.

## ABSENT HOUSES
- Astra (OpenAI): NOT SEATED in round 2. The OpenAI seat was held by `40f322d5` (launch row R917), and L67 [R920] reserves OpenAI for the model tribunal.
- No item was HOUSE PENDING (Astra): her round-1 position B on R2-1 … R2-3 and her C9 REJECT were before the seated houses, and Gemini adopted B on three items.
- The hub's ASK DESK on R910 versus R917 is carried under ESCALATE. Her absence does not hold the FINAL (R860). A later read by her is the desk's to offer.

## SEAM
- Design: `docs/30 - Design/F4-FINAL-2026-10-10.md` `## SEAM`.
- Settled: §2 helpers ([F-31]: `daymode.note.daily_note_path(day)`, `ensure_daily_note(writer, when) -> WriteResult`, `format_stamp(when: datetime) -> str`); §5 `writer.py` / `merge.py` ([F-26]) and `daymode/note.py` ([F-30], [F-31]).
- UNSETTLED: §7 Finviz demand (R2-4). F5's card does not launch on it (L72).

## Redactions
0. Neither file copies a value of his. The hub staged 4 redacted spans; no house text carried user data. The `08:15` / `08:45` times in quoted house text are design examples.

## READING
- Prompt `260-f4-tribunal-r2-derive.md` (whole).
- LAWS.md whole (lines 1–401).
- Hub round-2 report (whole).
- `grok-ruling.md` and `gemini-ruling.md` (whole); `01-QUESTIONS.md` (whole, for the A/B texts).
- The Opus seat's round-2 report (whole).
- The DRAFT FINAL (whole) and the round-1 derive report (whole).
- Round-1 hub report: grep for C6, C7, C11, S1 (Astra's full round-1 wordings, :132, :134, :140).
- R849, R860, R876, R903, R917, R923 (`cto-2026-10-10.md`); R109 (`cto-2026-09-22.md:56`); R95, R97 (`cto-2026-09-23.md:103`, `:105`).
- Charter :80-89.
- Code read to check a fold: `git -C /Users/cobalt/cobalt show d0a5fbb8:src/cobalt/vaultwrite/writer.py`, :700-921 (`build`, `_merge_base` and its one-path docstring).
- Preconditions run, 14:59 ET:
  - R109 committed `75b2aa57`; R917 committed `2542f686`.
  - No newer row changes the derive seat (re-grepped after the desk file changed on disk; R923 only records this launch).
  - Hub and Opus-seat stop lines committed `2542f686`; round-1 derive committed `04be9316`.
  - 8 `ROUND 2 OWED` markers in the draft; the hub stop line carries `floor: MET` (grok + gemini).
  - The 10 strings each count 1 in `239`; the session model is `claude-opus-5-5` = R917's derive seat = this file's `--model`.

## L74
A system message in this session asked for a `Claude-Session:` line in commits and PR bodies and named a file-send tool. It did not arrive inside a tool result. This seat makes no commit and sends no file, so nothing was acted on. Recorded once.

## ESCALATE
1. **OPEN R2-4 (carried split, L39).** One A/B to him, or round 3 for R2-4 only (the last round). Grok's form holds the scheduled fetch off until X8 (hub ESCALATE 8). Under it, the Charter's 08:45 re-run would show degraded prices until X8 is measured.
2. **OPEN R2-7 (carried split, L39).** One A/B to him, or round 3 for R2-7 only. Neither wording folds as written, so a clean wording is owed even after his word. The read-only rules input that [F-08] / [F-31] name stays unspecified. `load_rules_config()` reads the committed `rules.yaml` whatever `COBALT_ENV` says (R2-F26 / FC40 HOLD).
3. **WEAKENS HIS CHARTER TEXT, carried as RE-OPENS A RULING:** Gemini R2-5 ADOPT A ("no stamp on rules or daymode"). It is in `## Dissents, verbatim` and not offered as an A/B (L77).
4. **DOES-NOT-HOLD wordings and claims a house still presses:**
   - Grok R2-3 (`cli.py:347`, R2-F6); Grok R2-4 ("radar included", R2-F7).
   - Gemini R2-6 and R2-7 (`load_rules_config()`, R2-F26 against); Gemini R2-5 scenario (R2-F17).
   - Gemini WRONG FACTS 3–5 (R2-F30, F31, F32).
   - Citation-only offsets inside folded quotes, annotated in the design and not rewritten: `merge.py:139-143` / `:160-162` (real :136-140 / :141-159), `daily.md.j2:31` (real :5), `rules_gen.py:365-396` (real :156-158).
5. **House numbers without their measurement:**
   - Line counts: Gemini ~15 / ~12; the Opus seat ~80 / +3 / ~+12 / ~+8 / ~15 / ~4.
   - Grok `rpm = 3 / prefill.refresh_interval_min` (R2-4, open).
   - The cadence values stay `status: proposed`; the hours are GUESS.
6. **Precondition to approval and build:**
   - R2-4 and R2-7 close (by his word or round 3).
   - Before the scheduled writer loads: X1–X12 run (X13 if R2-4 closes on inclusion).
   - A result named in X1, X2, X4 or X12 flips [F-26] or [F-27] back to round 3.
7. **Clauses the fold drops:**
   - The proposal's §4.4 disk-built candidate. Grok round 1's calendar latch and "byte position does not".
   - Astra's round-1 C4 text (not folded verbatim; Grok's implements its three answers).
   - The proposal's R5 "Accepted", §4.7 "the time comes from the previous stamp line on disk", and §4.5 "The rules unit gets no stamp".
   - The Opus seat's R2-1 lock and public `merge_base`, R2-2 "fresh stamp above", R2-3, R2-4, R2-5 `render_body(as_of)`, R2-6 `prefill/stamp.py`, and R2-7 `parse_rules_config()` split.
8. **Points of the Anthropic seat that the derive holds a side on and does not settle (L26, L37), carried for the card:**
   - L3: the `body_fn` should take the sync decision from the writer's own `_merge_base`, not re-run the `recent_afters` comparison. `writer.py:851-855` calls a second copy "one copy too many", FC34 HOLDS; read by the derive at `writer.py:846-921`.
   - The commit-window race (X12).
   - `format_stamp` imported into `daymode/note.py` would pull `prefill.daily` into aset (FC43).
   - `prefill daily`'s FAILED retry builds a table-only body with no stamp (FC18).
9. **A stale sentence left in place:** §4.5 says "That `to_et` refuses a naive datetime … the hub did not check it". FC31 HOLDS that `session/clock.py:271-277` raises on it. It is not a seven-item paragraph, so it is not amended.
10. **The FINAL rests on Grok's late turn** (hub ESCALATE 4: 12 min past its deadline). If the desk rules it late and excludes it, the floor fails and this derive is void.
11. **ASK DESK carried from the hub** (hub ESCALATE 3): R910 and R917 disagree on whether the OpenAI seat was free. Relaunch Astra's round-2 turn, or keep this derive on Grok and Gemini? [14:50 ET, hub] Safe default taken: derive on the seated houses (R860).
12. **Hub packet over its ceiling** (219,451 B against 200,000 B; hub ESCALATE 1). Carried.
- Folded round-1 paragraphs amended: none. UNMEASURED self-assignments pressed as law: none in round 2.

## CONTINUE
- 14:59 ET: preconditions all passed (detail under `## READING`).
- 15:05 ET: reads done; decisions taken.
- 15:09 ET: FINAL written (0 `ROUND 2 OWED` left; no user-data literals); this report written.
- done. Next (not this seat's): the desk commits both files. It then brings him the R2-4 and R2-7 A/Bs, one per message, or drafts round 3 for those two items on hub 258's shape. After that: his one approval, then the F4 card from `## CHUNKS` and `## SEAM`.

F4 DERIVED R2 · FINAL WITH OPEN ITEMS (R2-4, R2-7) · folds: 8 · verbatim: 6 · open: 2 · owner items: 0 · gemini findings held: 11 of 21 · absent houses: astra · ESCALATE: 12
