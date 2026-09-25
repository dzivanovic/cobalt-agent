# Voice slice VT — round-1 derive → DRAFT FINAL (2026-09-25)

Seat `voice-tts-derive-0925` · Opus 5.5 (`claude-opus-5-5`) · started 07:31 ET, DRAFT FINAL written 07:44 ET (`date`).

## §0 Headline
- DRAFT FINAL written: `docs/30 - Design/VOICE-TTS-DRAFT-FINAL-2026-09-25.md` (63,651 B) — `DRAFT FINAL — ASTRA PENDING`; Astra rules round 2 on it (`16` §5), not before 2026-09-26 06:47 ET. 57 fold rows, 33 verbatim; nothing invented; 0 tunables numbered.
- Needs round 2: 4 — Q5 figure gate (flag vs guard), Q4 GPL order (only if VT-X4 finds one), Q8 `tts_voice` / engine value, Q9 lock + widget supersede. Round 2 runs anyway for Astra.
- Owner items: 0 in `## FOR DEJAN` — grok ruled both NOT his (settled by measurement), so both leave (L67 as amended 2026-09-24); ONE approval after round 2.
- A Gemini finding held: YES (M1, M3, M5), none unique to Gemini; 1 Gemini line folded verbatim (VT-X3). Gemini findings held: 3 of 6.
- ESCALATE: 9. No `RE-OPENS A RULING`; no V1-contract change asked.

## AUTHORIZATION

| Gate | Result |
|---|---|
| `DERIVE ROW: R__` whole-line count | 0 → row R109 |
| `cto-2026-09-22.md` R109 | one row, line 56, carries `Make all Opus 5.5 for now` + `derive` |
| R109 committed | `75b2aa57` |
| Launch row for `16` | `cto-2026-09-25.md:41` R33 — carries `VOICE-TTS-PROPOSAL-2026-09-25.md`, `Fable seat: yes`, `derive seat: claude-opus-5-5`; R26 / R32 name the file but carry none of the three literals; `cto-2026-09-26.md` absent (recorded, not fatal) |
| Launch row committed | `b6854e54` |
| Derive launch row | `cto-2026-09-25.md:48` R40 |
| Seat | row names `claude-opus-5-5`; this session runs `claude-opus-5-5` — match |
| Hub stop line | `VOICE TTS TRIBUNAL DONE · round: 1 · …` — committed `31991b51` |
| Anthropic-seat stop line | `VOICE TTS FABLE R1 DONE · …` — committed `7c4546f7` |
| Floor (grok ruled) | `grok: TRIBUNAL R1: BUILD AFTER derive folds the WITH clauses` — met |
| Astra | `METER` — recorded; DRAFT FINAL marked ASTRA PENDING |
| Launch strings | 7 allow + 3 deny, each count 1 in `2026-09-23/12-draft-voice-v3.md` — no new rule |

## DIGEST FOR THE DESK
Seats that ruled round 1: grok in full (17 items); gemini in full (17 items, 2 min); the Anthropic seat in full (blind, `17`); Astra METER (probe 06:5x, return 2026-09-26 06:47). Anthropic-seat claims: 28 hub-checked (25 HOLD, 3 UNVERIFIABLE → experiments), 1 WITHDRAWN (not folded); UNCHECKED claims folded: 0.
What the DRAFT FINAL changed from the proposal, item by item:
- T10 status → grok's "DOES NOT HOLD as written" (F-01). T16 → the seat's: RECORDED at V1-BUILD:454, not an experiment (F-02); VT range → VT-X9.
- T20–T27 added: the seat's five missed facts (tap path, restarts-test pins, heartbeat env, no-`turn_id` replies, no synth path) and grok's three (`Probe` no AMBER, `speak()` at `:252`, reference kit not a path) (F-05, F-06). T8 → grok's (F-07). L31 wording → "person or vendor" (F-57).
- Q1 route → the seat's route rule: 409 `device_voice` on `pending_action` rows (tap-path stale read-back, FC1–FC6), 404s, 413 (F-08).
- Q2 → grok's: one WAV, no 1.5 s constant (F-09). Q3 → grok's: ONNX first; `tts_speed` bound from VT-X4, not 0.5–2.0 (F-10).
- Q6 → the seat's fallback wording: abort is never a failure; no-`turn_id` replies; one `voiceReply` replaces `speak()` (F-13). Owner item 2 folded as grok's "server first" (F-14).
- Q7 → the seat's: probe reads only `/voice/status` (heartbeat has no model-dir env, FC9/FC10) (F-15) + grok's `Probe` level field (F-16).
- (b) → the seat's "voiced at most once" (F-21); `device-os` future engine deleted, grok (F-22).
- (c) → grok's VT-X4 = VT-1's merge bar (F-23); the seat's direct `onnxruntime` pin (F-24).
- (d) → the seat's `no-store`, revoke, silent-output refusal, claim scope (F-25).
- (f) → the seat's `test_jobs_restarts.py` pins, reads line RECORDED, heartbeat plist line (F-27–F-29); grok's `ops/fetch-voice-models.sh` (F-30).
- FINAL amendments: A, B, D, E kept; C + the seat's silence row + grok's stale-fetch line (F-35); F → grok's (keeps the FINAL's `[F-26]`) (F-38); NEW: E5 result cell → grok's (R23) (F-39).
- Experiments: X1 grok (F-40), X2 seat (F-41), X3 grok + seat + gemini (F-42), X4 grok + seat (F-43); new VT-X7 (grok cache test), VT-X8 (seat silent output), VT-X9 (restarts on the VT range).
- Owner item 1 → grok's (g) item 1; leaves FOR DEJAN (F-50).
Round 2: Astra's full first ruling on all 17 items (always) + `## NEEDS ROUND 2` R2-1…R2-4 for the other seats.
Chunks under the DRAFT FINAL: VT-0 (experiments; VT-X3 in the owed device session) · VT-1 synth + keys + pin + fetch command · VT-2 route + status block · VT-3 widget · VT-4 probe + `Probe` level + DevDocs; 0 write-path chunks; builder Opus 5.5 `auto`; new-build check seats Fable-type (Opus 5.5, R109) · Astra · Grok (L67). RESTARTS: `com.cobalt.aset` + whatever `cobalt jobs restarts` names for the lock change + the `voice.yaml` reads line (VT-X9); heartbeat one-shot, no restart.
Hours: 7.5 h seats, ≈ 10.5 h with one fix round — the proposal's, unchanged; GUESS / UNVERIFIED. +≈2 h only if R2-2 picks a sidecar (the seat's figure, UNVERIFIED).

## Fold table
`seats` = seats that ruled the item (of 4: grok, gemini, Anthropic seat; Astra METER). `A`/`AW`/`R` as the hub's table. `Gem held?` = was a Gemini finding on this item folded, and did it hold.

| F | item | seats that ruled it | whose wording | verbatim? | Gem held? | why (≤25 words) |
|---|---|---|---|---|---|---|
| F-01 | WRONG FACTS T10 | 3 of 4 (grok, gemini, seat) | grok | yes | no | G1/FC11 HOLD; house over seat, equally correct; gemini's "T10: HOLDS" DOES NOT HOLD (M2) |
| F-02 | WRONG FACTS T16 | 3 of 4 | Anthropic seat | yes | no | FC12/FC13 HOLD; grok's "correctly UNPROVEN" DOES NOT HOLD for V1's range (G13); VT range → VT-X9 |
| F-03 | (a) T1 | 3 of 4 | proposal kept | not taken | n/a | grok's "desk's paraphrase" DOES NOT HOLD (G3) |
| F-04 | (a) T9 | 3 of 4 | proposal kept | not taken | n/a | grok's range objection DOES NOT HOLD (G4) |
| F-05 | (a) missed facts T20–T24 | 3 of 4 | Anthropic seat | yes | no | FC1, FC14, FC9, FC15, FC16 HOLD; no house named these; gemini "Missed: NONE" DOES NOT HOLD (M2) |
| F-06 | (a) missed facts T25–T27 | 3 of 4 | grok | yes | no | G6, G8, G17 HOLD; grok's status_lines bullet = F-01; "replay synthesized" bullet not needed |
| F-07 | (a) T8 status | 3 of 4 | grok | yes | n/a | G5 HOLDS: `get` has no session filter; the route compares session |
| F-08 | Q1 route | 3 of 4 (grok AW, gemini A, seat AW) | Anthropic seat | yes | n/a | FC1–FC6 HOLD: grok's route speaks a tapped row's stale read-back; not equally correct. Grok's digit-409 → R2-1; its log-only clause lost |
| F-09 | Q2 wire | 3 of 4 (grok AW, gemini A, seat A) | grok | yes | n/a | G7 HOLDS: 1.5 s unmeasured; no tunable number before its experiment; gemini kept 1.5 s — not taken |
| F-10 | Q3 runtime | 3 of 4 (3 A) | grok | yes | n/a | 3-0; grok's text removes the unmeasured 0.5–2.0 bound (W6 HOLDS) |
| F-11 | Q4 GPL / native g2p | 3 of 4 (3 AW, three orders) | not taken → R2-2 | not taken | n/a | M7: contradiction on sidecar's licence reach and price; no file settles it; binds only if VT-X4 finds one |
| F-12 | Q5 VT-X5 gate | 3 of 4 (grok AW, gemini A, seat AW) | not taken → R2-1 | not taken | n/a | grok (flag, every digit reply) vs seat (guard, read-backs only, "never a config flag"): each calls the other's mechanism wrong |
| F-13 | Q6 fallback | 3 of 4 (grok A, gemini A, seat AW) | Anthropic seat | yes | yes (M3) | FC15/FC17 HOLD; grok's Q6 lacks no-`turn_id` handling and leans on its unfolded digit-409; mid-play sentence → R2-4 |
| F-14 | Q6 / (g) owner item 2 | 3 of 4 | grok ((g) item 2) | yes | no | grok and seat: not his (R23, L23, measurement) → leaves FOR DEJAN; gemini "taste" NOT NAMED against the test |
| F-15 | Q7 probe | 3 of 4 (grok AW, gemini A, seat AW) | Anthropic seat | yes | no | FC9/FC10 HOLD: heartbeat reads DEV `model_dir`; grok's file check did not address it; gemini "stall the event loop" DOES NOT HOLD (M4) |
| F-16 | Q7 Probe level | 3 of 4 | grok | yes | n/a | G6 HOLDS: `Probe` has no AMBER; the folded Q7's AMBER needs it. Seam line UNSETTLED vs V4 |
| F-17 | Q8 `tts_voice` + engine value | 3 of 4 (grok AW, gemini A, seat AW) | not taken → R2-3 | not taken | n/a | M8: lawfulness of a person's name / as-shipped id disputed; 82M uncited (W6/W7) |
| F-18 | Q8 V1's `faster-whisper` names | 3 of 4 | RECORDED for V1 BACKLOG (R25 reading (1)) | not taken | n/a | never a VT fold; grok: not a breach proven; seat: not bound; gemini: binds V1 |
| F-19 | Q9 single-flight + abort | 3 of 4 (grok AW, gemini A, seat AW) | not taken → R2-4 | not taken | n/a | lock frees at timeout (grok) vs keeps lock, 503 busy (seat; FC20 UNVERIFIABLE); mid-play error: fall back vs no replay |
| F-20 | Q10 L57 | 3 of 4 (grok AW, gemini A, seat A) | proposal kept | not taken | n/a | 2 A; grok's flag clause is R2-1; its `no-store`/revoke carried by F-25 |
| F-21 | (b) one path — voiced once | 2 of 4 AW + gemini no word | Anthropic seat | yes | yes (M3) | M3 omission HOLDS (all three); grok's (b) rests on unfolded Q1/Q5/Q9; "no frame played" clause → R2-4 |
| F-22 | (b) `device-os` engine | 2 of 4 AW | grok | yes | n/a | uncontested; L3: a server `device-os` is a second synthesizer; cost of keeping: a second engine path |
| F-23 | (c) L15 merge bar | 2 of 4 AW + gemini "Yes" | grok | yes | n/a | house over seat; seat's "VT-1 does not start until X4 committed" not taken — VT-0 runs X4 first anyway, 0 h difference |
| F-24 | (c) direct pin | 2 of 4 AW | Anthropic seat | yes | n/a | FC7/FC8 HOLD; grok's text does not address the transitive `onnxruntime` |
| F-25 | (d) loud + replayable | 2 of 4 AW + gemini "Yes" | Anthropic seat | yes | no | FC28/G19 omission HOLDS; grok's table not taken (audio-error row → R2-4, digit row → R2-1); gemini "all loud" DOES NOT HOLD (M6) |
| F-26 | (e) boundary | 3 of 4 NONE | proposal kept | not taken | yes (M1) | NONE from all three given F-08; gemini's `peer_gate` citation holds (M1) |
| F-27 | (f) restarts-test pins | 2 of 4 AW + gemini "Yes" | Anthropic seat | yes | n/a | FC14 HOLDS; no house named it |
| F-28 | (f) `voice.yaml` reads | 3 of 4 | Anthropic seat | yes | yes (M5) | FC13 HOLDS for V1's range; UNPROVEN on VT's range until VT-X9 (G13); gemini "real gap" HOLDS (M5) |
| F-29 | (f) heartbeat plist | 2 of 4 AW | Anthropic seat | yes | n/a | FC9 HOLDS; follows F-15 |
| F-30 | (f) fetch command path | 2 of 4 AW | grok | yes | n/a | G14 HOLDS (none exists); names the proposal's ONE command; "neutral stems" → R2-3 |
| F-31 | (f) nine keys | 2 of 4 AW | not taken → R2-1 | not taken | n/a | `tts_readback_server` is grok's R2-1 side; SEAM line UNSETTLED |
| F-32 | (f) `/voice/status` `tts.last`/`rss_mb` | 2 of 4 AW | not taken | not taken | n/a | F-15 folds the seat's `tts` block (`present`, `model_dir`, `last`, `rss_peak_mb`); two shapes would be a second status contract |
| F-33 | FINAL amendment A | 3 of 4 | proposal kept | not taken | n/a | grok and gemini: correct and minimal |
| F-34 | FINAL amendment B | 3 of 4 | proposal kept | not taken | n/a | grok's whole replacement carries the Q5 flag; seat's one sentence is its Q5 side — both R2-1; R23 sentence kept |
| F-35 | FINAL amendment C | 3 of 4 | proposal + seat row + grok line | yes | n/a | silence row follows F-25; grok's stale-fetch line follows F-13; seat's busy row → R2-4 |
| F-36 | FINAL amendment D | 3 of 4 | proposal kept | not taken | n/a | engine value → R2-3; "Depends on" updated at round-2 derive |
| F-37 | FINAL amendment E | 3 of 4 | proposal kept | not taken | n/a | rows = the DRAFT FINAL's experiments as ruled |
| F-38 | FINAL amendment F | 2 of 4 (grok AW, gemini A) | grok | yes | n/a | keeps the FINAL's `[F-26]` path (FINAL :371, "Reaches the card: YES"); proposal's F could read as retiring it |
| F-39 | FINAL amendment — E5 cell (new) | 1 of 4 (grok) | grok | yes | n/a | G10 HOLDS: FINAL :281 still says a failed E5 creates the slice; R23 set that aside |
| F-40 | VT-X1 | 3 of 4 | grok | yes | n/a | drops the 1.5 s line (G7); adds `duration_s`; house over seat (seat also adds `sample_rate`) |
| F-41 | VT-X2 | 3 of 4 | proposal + seat | yes | n/a | measures `ru_maxrss` as the folded Q7 reads it; grok's X2 = proposal |
| F-42 | VT-X3 | 3 of 4 | proposal + grok + seat + gemini | yes | yes (M3) | each addition attributed, none merged; grok's digit-409 check runs only under R2-1 grok side; G18/FC24/FC18 → observed here |
| F-43 | VT-X4 | 3 of 4 | proposal + grok + seat | yes | n/a | model card count, stems, speed range (grok); network-off synthesis + write trace + version check (seat) |
| F-44 | VT-X5 | 3 of 4 | proposal kept | not taken | n/a | what it unlocks is R2-1 |
| F-45 | VT-X6 | 3 of 4 | proposal kept | not taken | n/a | informational (seat); grok's flag → R2-1 |
| F-46 | VT-X7 (grok X7) | 1 of 4 | grok | yes | n/a | G18 UNVERIFIABLE FROM READS → experiment (L70) |
| F-47 | VT-X8 (seat X7) | 1 of 4 | Anthropic seat | yes | n/a | G19 emission UNVERIFIABLE → experiment; gates F-25's refusal |
| F-48 | seat X8 busy rate | 1 of 4 | held for R2-4 | not taken | n/a | measures a non-blocking lock not yet chosen; its "busy > 5 %" is unmeasured |
| F-49 | VT-X9 restarts on VT range | 2 of 4 (grok, seat) | grok's sentence, scoped by G13 | yes | n/a | G13: V1's range recorded, VT range UNVERIFIABLE → experiment |
| F-50 | (g) owner item 1 | 3 of 4 (grok R, gemini no word, seat AW) | grok ((g) item 1) | yes | no | grok ruled it NOT his (VT-X5 clarity count) → leaves FOR DEJAN by the prompt's rule; seat and gemini quoted in the DRAFT FINAL |
| F-51 | (g) a third item — Q4 (3) licence | 1 of 4 (seat) | not taken | not taken | n/a | conditional on a VT-X4 result that does not exist; rides R2-2 |
| F-52 | §9 chunks / hours | 3 of 4 | proposal kept | not taken | n/a | no seat priced a change for what the fold takes |
| F-53 | WRONG FACTS W3 (mute) | 1 of 4 (grok) | proposal kept, annotated | not taken | n/a | W3 inference HOLDS, VT unbuilt → VT-X3 "mute mid-play"; grok's timeout clause is R2-4 |
| F-54 | WRONG FACTS W4 (GET side effect) | 1 of 4 (grok) | proposal kept | not taken | n/a | W4: a reading of §6, not a defect |
| F-55 | WRONG FACTS W5 (R21) | 1 of 4 (grok) | proposal kept | not taken | n/a | G9: not established — the proposal cites his words |
| F-56 | WRONG FACTS W6 / W7 (0.5–2.0, 82M) | 1 of 4 (grok) | carried by F-10 / R2-3 | not taken | n/a | HOLD; 0.5–2.0 removed by F-10; 82M is R2-3 / VT-X4 |
| F-57 | WRONG FACTS W8 (L31 "product") | 1 of 4 (seat) | Anthropic seat | yes | n/a | W8 HOLDS (`LAWS.md:182`) |

Totals: 57 rows · verbatim yes 33 (grok 16, the Anthropic seat 14, mixed 3) · not taken 24. **Held side, stated (L37):** this derive is the seat that ruled round 1. 14 folds take that seat's wording; each rests on a hub FC row that HOLDS where the house wording on the same point was not equally correct, or where no house wrote a wording. Where a house wording was equally correct (T10, (c) merge bar, VT-X1), the house's was taken.

## NEEDS ROUND 2
Full sides verbatim: DRAFT FINAL `## OPEN TO ROUND 2`. Astra rules round 2 regardless.
- **R2-1 — Q5 figure gate (+ Q1's digit clause, amendment B's read-back sentence, key count).** Grok: "VT-X5 is a hard gate on every server-voiced reply that contains a digit … Required key `tts_readback_server`". The Anthropic seat: "Read-backs — every row with `pending_action` set — are never spoken by the server voice in VT … never a config flag." Question: is a reply that is NOT a read-back but carries a figure held to the device voice until VT-X5? By a config key or by code? If anything ever lifts the read-back gate, how is a tapped row (FC1: it keeps the read-back as `reply`) kept from being spoken?
- **R2-2 — Q4 (binds VT-1 only if VT-X4 finds a native / GPL g2p step).** Grok: "The one alternative is a loopback sidecar on `127.0.0.1` only … Price: no extra chunk". Gemini: "ADOPT WITH a loopback sidecar". The Anthropic seat: "Round 2 first looks for a path without it … A loopback sidecar is priced before it is chosen … Whether a separate process changes the licence's reach is a legal claim no house settles from memory." Question: in what order are the three options taken, what does a sidecar cost (resident, plist, restart rule, probe), and does a separate process change the licence's reach?
- **R2-3 — Q8 values.** Grok: "`tts_voice` is a neutral stem (`v01`, `v02`, …) … must not be a person's name or a vendor's name"; engine `neural-local` unless the card states 82M. The Anthropic seat: "`tts_voice`'s VALUE is the voice file's id exactly as the pinned model ships it … an artifact id". Gemini: "A `tts_voice` value may contain a person's name". Question: under L31's "Person or vendor names never in … config keys, enum values or system design docs", may a config VALUE carry a shipped voice id that is a person's name? And is the engine value `neural-82m` before VT-X4 records the count?
- **R2-4 — Q9 lock + widget supersede.** Grok: "the lock frees when the call returns or `tts_timeout_s` fires"; "an audio `error` on the current generation falls back once"; a generation integer. The Anthropic seat: "NON-BLOCKING acquire … 503 `busy` … A synthesis whose caller timed out keeps the lock until it ends"; "An `error` after playback began → … the device voice does not replay the reply." Question: blocking or non-blocking lock, and does the lock outlive a timed-out caller? Is a generation integer the supersede mechanism? After playback began, does an `error` fall back to the device voice or not?

## OWNER ITEMS
- The proposal's item 1 (voice and speed, recommends B) and item 2 (phone: server or device first, recommends A) both LEAVE `## FOR DEJAN`. The rule: a seat ruled each NOT his and settled by measurement. Grok's (g): "REJECT both owner items as items for him … Even if taste qualified, a house can decide both." Item 1: VT-X5's clarity count. Item 2: L23 + Q6, with the Anthropic seat concurring ("R23 and measurement settle it").
- Not followed, quoted: the Anthropic seat, item 1 "PASSES: it is his taste in what he hears, and no house can hear for him"; gemini, both "taste" (hub: NOT NAMED against the test).
- Third item: the Anthropic seat's "Q4 (3) only if reached: accepting a GPL licence in this private install — his law". It is conditional on a VT-X4 result that does not exist, so it is not a decision now and it rides R2-2.

## FOR DEJAN
No decision for you from this round. Round 2 (Astra) runs first. After it, one question: "approve the VT FINAL?". Not asked now.
What you would hear, as the DRAFT FINAL stands:
- **After you speak.** The reply text appears first. Then Cobalt's own voice reads it, generated on the Mac. This works in the phone's and the trading-PC's browser tab; nothing is installed on either.
- **Confirmations.** A read-back that asks you to confirm is spoken by the phone's or PC's own voice. This DRAFT FINAL does not settle whether plain answers with figures also stay on that voice until the figure test passes. That is round 2.
- **When the server voice is down.** The device's own voice speaks, with an amber line naming why. If there is no device voice either, you get text and both amber lines.
- **When you press again or mute.** Playback stops, and the old reply is never spoken over your recording.
- **The device session you already owe.** VT's playback checks join the V1 checks on your phone and trading PC, in one session. You may hear the candidate voices there. It is not a gate, and you can change the voice in its config later.

## SEAM
DRAFT FINAL `## SEAM`: every V1 file with its `file:line` at `d319e4f3` (spot-checked this run at the V1 worktree). VT branches off `main` AFTER V1 merges. UNSETTLED (L72 P-b):
- the key count, eight or nine (R2-1);
- which of V4 and VT adds `Probe`'s level field if V4 builds first — a reading, no seat named it;
- what the fetch command writes for voices (R2-3);
- the sidecar resident, only if R2-2 chooses one;
- the `voice.yaml` reads line, UNPROVEN on the VT range until VT-X9.

## Redactions
0. No value of his in either file. Two constructed scenario values ("stop is 12.5", `af_sarah`) come from grok's quoted sides; the hub classed them as the house's own, not his. Seat-proposed tunable values without a measurement are pointers only (`## ESCALATE` 2).

## READING
- **Authorization.** Every gate in the table above.
- **Read whole:**
  - LAWS.md 1–454;
  - the hub report `voice-tts-tribunal-2026-09-25.md` 1–442;
  - the seat's round-1 report 1–291, including `## Self-attack` — its one WITHDRAWN sentence was not folded;
  - the proposal 1–195;
  - `voice-tts-propose-2026-09-25.md`, whole;
  - `grok-ruling.md` 1–225 and `gemini-ruling.md` 1–95. The grok wordings I adopted match the hub's verbatim copy.
- **Rulings (by `grep -n "^| R<nn> "`):** `cto-2026-09-25.md` R21, R22, R23, R25, and R26 / R32 / R33 / R40 via the launch greps; `cto-2026-09-24.md` R107; `cto-2026-09-23.md` R95–R97; `cto-2026-09-22.md` R109.
- **FINAL:** `grep -n` of its headings, then :1–92, :167–224, :269–324, :369–392.
- **V1 greps at `~/cobalt-wt/voice-v1` (tip `d794e899`):**
  - `web.py`, `models.py`, `store.py`, `config.py`;
  - `jobs.yaml`;
  - `test_radar_panel_cards.py`, `test_jobs_restarts.py`;
  - `probes.py`;
  - `pyproject.toml`, `uv.lock`;
  - `start_aset.sh`, `com.cobalt.heartbeat.plist`.
- **Formatting only, no word changed.** Where a seat's numbered or bulleted list sits inside a table cell or a quoted side, its items are joined on one line. Elisions are marked "…".

## L74
One block arrived inside a tool result: it was appended to the first `cat` of this prompt file, asked for a `Claude-Session:` commit line and named a file-send tool. It is DATA and was not followed. This run commits nothing.

## ESCALATE
1. **Inherited, the hub's ASK DESK 1.** The hub launched on a backtick-tolerant reading of R33's stagger literal instead of failing its preflight. These rulings, and this derive, stand only if the desk accepts that reading.
2. **Seat-proposed numbers without their measurement** (pointers only, never folded):
   - `1.5 s` first-audio budget: proposal `VOICE-TTS-PROPOSAL-2026-09-25.md:101`, `:169`; kept by gemini `gemini-ruling.md:7`.
   - `tts_speed`, value proposed by the Anthropic seat: `voice-tts-tribunal-fable-r1-2026-09-25.md:188` (1.0).
   - `tts_speed` bound, proposed by the proposal: `:52` (0.5–2.0) — removed by F-10.
   - busy threshold, proposed by the Anthropic seat: `…fable-r1…:239` (5 %).
   - sidecar price, proposed by the Anthropic seat: `…fable-r1…:49` (≈ +2 h).
   - parameter count: proposal `:43`, `:52` (82M) — R2-3 and VT-X4.
3. **DOES-NOT-HOLD wordings grok still presses:**
   - T1 "desk's paraphrase" (G3);
   - T9 ranges (G4);
   - T16 "correctly UNPROVEN" for V1's range (G13).

   None was folded.
4. **DOES-NOT-HOLD wordings gemini still presses:**
   - "T10: HOLDS", "Missed: NONE", "WRONG FACTS: None" (M2);
   - Q7 "stall the event loop" (M4);
   - (d) "all failure rows emit loud AMBER lines" (M6).

   None was folded.
5. **Preconditions to build:**
   - round 2 (Astra) and the round-2 derive naming the FINAL come first;
   - VT-1 cannot merge without VT-X4's lock diff (F-23);
   - R2-2 binds VT-1 only if VT-X4 finds a native or GPL step;
   - the SEAM's UNSETTLED lines are settled before the VT and V4 build prompts launch.

   No owner item gates a chunk.
6. **Item (g) split.** Grok REJECTs both owner items; the Anthropic seat says item 1 passes and item 2 fails; gemini says both are his taste. Applied here: the prompt's leave-rule (a seat ruled each NOT his). Result: `## FOR DEJAN` = 0. Astra rules (g) in round 2.
7. **ASK DESK: per-line adoption.** Items (a), (b), (c), (f), amendment C and VT-X2/X3/X4 each take verbatim lines from more than one seat, each attributed, no sentence edited. I read that as "choosing between wordings" line by line, not blending. Safe default: taken, and every line is named in the fold table. If the desk reads it as blending, the affected rows are F-05/F-06, F-21/F-22, F-23/F-24, F-27–F-30, F-35 and F-41–F-43. [07:44 ET]
8. **L31 on V1's `faster-whisper` identifiers — a finding for the V1 BACKLOG ticket (R25 reading (1)), never a VT chunk:**
   - grok: "This tribunal does not call an L31 breach the text does not prove";
   - the Anthropic seat: "L31 does not bind it, and its rename is not a law defect";
   - gemini: "L31 binds V1".

   Whether to keep the ticket is the desk's record.
9. **SEAM, UNSETTLED.** Which of V4 and VT adds `Probe`'s level field when V4 builds first. Grok puts it in VT-4, but the FINAL's V4 row also needs AMBER. The desk settles it in the DRAFT FINAL's `## SEAM` before either prompt launches (L72 P-b).

`RE-OPENS A RULING`: none. V1-contract change asked by a seat: none.

## CONTINUE
next: none — the run is complete. Recovery (L60): both files exist; re-read this report and the DRAFT FINAL, never re-derive.

VOICE TTS DERIVED · DRAFT FINAL · folds: 57 · verbatim: 33 · needs round 2: 4 · owner items: 0 · gemini findings held: 3 of 6 · astra: round 2 after 2026-09-26 06:47 · ESCALATE: 9
