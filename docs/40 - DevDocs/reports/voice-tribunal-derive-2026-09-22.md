# Voice tribunal — derive v2 (seat `voice-tribunal-derive-0922`, claude-opus-5-5, row R108)

## §0 Headline
- v2 written: `docs/30 - Design/DRC-VOICE-v2-2026-09-22.md` — 32 fold rows, 17 taken verbatim (grok 14, Fable seat 2, the experiments row quoting both 1), 0 invented mechanisms; 0 re-opened rulings.
- **Round 2 NEEDED: 2 items** — R2-V1 (build seeds the voice unit's initial body vs blank + one landing function) and R2-V5 (a card matched by >1 trade: unbound vs earliest). The tribunal does not close yet.
- Owner items: 12 (W1–W6 + W7–W12), none a precondition to build. ESCALATE: 12 (5 DRC-FINAL seam changes, the seam document owed before D2 launches).
- **ASTRA PENDING (R13)**: Astra reads this v2 when its meter returns (Sat 09-26).

## DIGEST FOR THE DESK
What v2 changed from the proposal, item by item:
- T-V1: append made idempotent on the capture row / capture id (3 of 3); byte-prefix check replaced; sibling unit dropped. Initial body at build vs blank + one landing function → R2-V1.
- T-V2: in-request transcribe kept + reap of a stale `running` row + dedupe of a repeat post (grok verbatim); off-loop wording not taken, X1/X2 decide.
- T-V3: faster-whisper only; a Metal engine only via V-E2 + V-E3 and a named deploy step (grok).
- T-V4, T-V7: proposal kept (3 of 3 ADOPT).
- T-V5: >1-trade case → R2-V5; A31 home = DRC D5-3 `drc-day/open_items` (seam).
- T-V6: date = card's trading date or `/drc` date field, never clock/speech (grok).
- T-V8: `model_dir` outside vault + repo; swap = config change + `com.cobalt.aset` restart (grok).
- T-V9: `/voice` inherits the existing bind, no new gate (grok); Gemini's tailnet-only → W11.
- T-V10: proposal kept + X6; on/off and list home → W8.
- (a): V22–V27 added (Fable seat verbatim); V6 narrowed to the new core; V4 and V18 stay desk record items.
- (b)/(c)/(d)/(e): audio only via D2-2's bytes method; a block lands only from a `done` row whose sha matches the stored file; append never takes the sync-revert win; handler reads bytes (never `str(v)`), zero-byte FAILs, empty transcript lands no block (all grok verbatim).
- (f): seam document owed (L72 P-b) with grok's six entries + five carried DRC-FINAL items; Gemini's "v2 is the seam doc" DOES NOT HOLD.
- (g) + WRONG FACTS: V2 cannot deploy after D2 without D3 (Fable WF2, FC3); migration unnumbered (desk's, L68); 19 h / ≈27 h unchanged, UNVERIFIED.
- Experiments: V-E1–V-E5 (V-E4, V-E5 widened, grok verbatim) + X1–X9, X11, X12. Hub's X10 not taken.
Seats that ruled round 1: grok in full · Gemini in full · Fable seat in full (R106, claude-opus-5-5) · Astra `METER — proceed on three` (R13), ASTRA PENDING.
Fable claims: 6 hub-checked (FC1–FC6, 6 HOLD); taken-or-cited UNCHECKED claims read by the derive: 6 (V23, V24, V27, WF3, D3-4 CLI group, create_if_absent missing parent) — all HOLD on read; none counted as hub HOLDS.
Round 2: R2-V1, R2-V5 — both are two seats disagreeing on whether a mechanism is CORRECT (L3 one landing path; binding a clip to the wrong trade).
Owner items: W1 capture points · W2 audio retention · W3 audio home · W4 cloud STT · W5 scope · W6 phone mic · W7 limits + unset behaviour · W8 hint on/off + list home · W9 no-trade voice later · W10 `drc_voice` row retention · W11 `/voice` tailnet-only · W12 his clips in git.
Chunks under v2: V1 (DB, Opus 5 floor, one migration, RESTARTS none) · V2 (vault imports + DB, `com.cobalt.aset`) · V3 (vault, `com.cobalt.aset`) · V4 (no write, probe resident derived). 3 write-path chunks; ≥3 checkers each (L67/R46).
Waits on his clips: V-E2, X6 (his clips + corrected text), V-E1 (his phone + trading-PC browser), X11/X12 (a real phone file) → V1 waits on V-E2, V-E3, X8.
Waits on DRC: X5 needs D2-2 built; X9 needs D1/D2; V2 needs D2 merged and deploys only with D2+D3; V3 needs D3 merged + R2-V1 + R2-V5 + D5-3's A31 line.
Seam: grok carried item 3 (D2-2 confinement / `voice/` sub-path / missing `<date>/` folder) must be settled BEFORE D2 launches.
Hours 09-24 → 10-07 (GUESS): voice ≈ 19 h seats (≈27 h with fix rounds) + ≈ 2 h V-E + ≈ 3–5 h X-experiments (GUESS, no seat estimated them) beside the DRC build (v2 §9: D1 7 + D2 7 + D3 9–10 + D4 4 h + D5, not re-read) and S3 C1–C4 (not read by this derive). V1 + experiments fit before the DRC deploy; V2/V3 land at or after it.

## Fold table

| F-nn | item | seats that ruled it | whose wording | adopted verbatim? | why (≤25 words) |
|---|---|---|---|---|---|
| F-01 | T-V1 landing | 3 of 4 (grok, Gemini, Fable seat) | grok (`grok-ruling.md:7`) | yes | Idempotency 3 of 3 (hub WRONG FACTS 3 HOLDS, FC1 HOLDS); Gemini's predicate misses a line typed below; initial-body clause OPEN R2-V1. |
| F-02 | T-V2 sync vs job | 3 of 4 (grok, Gemini, Fable seat) | grok (`:17`) | yes | House wording; Fable off-loop text not taken — equally correct pending X2 (V23 UNCHECKED by a hub — read by the derive at `web.py:946`). |
| F-03 | T-V3 engine | 3 of 4 | grok (`:26`) | yes | Gemini ADOPT; Fable's absolute-path binary wording not taken, house wording covers the named deploy step. |
| F-04 | T-V4 fallback | 3 of 4 | proposal kept | no — proposal kept | ADOPT 3 of 3. |
| F-05 | T-V5 binding | 3 of 4 | proposal kept, OPEN | not taken | SPLIT on correctness: grok + Fable unbound vs Gemini earliest (hub Checked row D3-2 direction HOLDS for grok) → R2-V5. |
| F-06 | T-V6 pre-DRC holding | 3 of 4 | grok (`:51`) | yes | Gemini, Fable ADOPT; grok adds the date source; A31 wording carried as a seam item. |
| F-07 | T-V7 mapping | 3 of 4 | proposal kept | no — proposal kept | ADOPT 3 of 3; verbatim only. |
| F-08 | T-V8 provisioning | 3 of 4 | grok (`:67`) | yes | Gemini ADOPT; Fable's `reads:`/sha256 wording not taken, house wording equally correct (L42 derives the restart). |
| F-09 | T-V9 surface | 3 of 4 | grok (`:75`) | yes | Hub Checked row `BACKLOG.md:150-151` HOLDS; Fable same default; Gemini's tailnet-only → owner item W11. |
| F-10 | T-V10 hint | 3 of 4 | proposal kept + X6 | no — proposal kept | Lawful 3 of 3; X6 (grok, Fable); Fable's off-until-X6 + list home → owner item W8 (his value, L53). |
| F-11 | (a) V22–V27, V6 narrowed | 3 of 4 | Fable seat (a) | yes | FC5, FC2, FC4 HOLD; V23/V24/V27 UNCHECKED by a hub — read by the derive at `web.py:946-1282`, `50:8`; grok WF2 converges. |
| F-12 | (a) V1 grep | 3 of 4 | proposal kept | no — proposal kept | Hub Checked row `generate_constitution.py:291` HOLDS; grok WF1 is a packet-staging gap. |
| F-13 | (a) V4 / author ESCALATE 1 | 3 of 4 | proposal kept | no — desk record | CLAUDE.md wording is a desk record item; v2 does not edit CLAUDE.md. |
| F-14 | (a) V18 / author ESCALATE 2 + Fable WF3 | 3 of 4 | proposal kept + pointer | no — desk record | Fable WF3 UNCHECKED by a hub — read by the derive at `aset.yaml:33-35`, `aset/__main__.py:4-6`: HOLDS. |
| F-15 | (b) audio writer | 3 of 4 | grok (`:123`) | yes | One bytes writer 3 of 3; Fable flat-name path not taken (house); sub-path legality → X5 + seam entry 3. |
| F-16 | (c) no transcript without audio | 3 of 4 | grok (`:143`) | yes | Gemini same substance; Fable (c) competing wording not taken — house equally correct. |
| F-17 | (c) test clips of his | 2 of 4 (grok V-E2, Fable seat) | proposal kept | no — proposal kept | Fable's "never enter git" vs proposal/grok "stripped" → owner item W12 (his data, DRC O15 precedent). |
| F-18 | (d) sync revert | 3 of 4 | grok (`:151`) | yes | Fable's contrary sentence WITHDRAWN (its Self-attack) — not folded; X4 replaces it. |
| F-19 | (e) capture handler | 3 of 4 | grok (`:159`, `:163`) | yes | `str(v)` sites read by the derive (`web.py:947` …); Gemini, Fable concur on zero-byte FAIL. |
| F-20 | (e) card/trade-key belongs to the date | 1 of 4 (Fable seat) | Fable seat (e) | not taken | House (e) wording taken; Fable paragraph overlaps it — not blended; carried to ESCALATE for the seam document. |
| F-21 | (f) seam document | 3 of 4 | grok (`:178`, carried `:182-186`) | yes | FC6 HOLDS (L72 P-b); Fable converges; carried items are DRC FINAL — carried as a seam. |
| F-22 | (f) "v2 is the seam document" | 1 of 4 (Gemini) | Gemini | not taken | Hub Checked row L72: DOES NOT HOLD. |
| F-23 | WRONG FACTS: D2 never deploys alone | 1 of 4 (Fable seat) | Fable seat WF2 | yes | FC3 HOLDS (`49-drc-d2-build.md:3`). |
| F-24 | (g) V1 CLI group | 1 of 4 (Fable seat) | proposal kept | not taken | Fable's wording carries `land --date` (R2-V1); D3-4 owns `cobalt drc` (read by the derive at `50:27`) — seam ESCALATE. |
| F-25 | WRONG FACTS: A31 not in D3 | 2 of 4 (grok carried 4, Fable WF1) | grok (`:185`) | yes | FC4 HOLDS; A31 = D5-3 `drc-day/open_items`, read by the derive at `52-drc-d5-build.md:18` — DRC FINAL — carried as a seam. |
| F-26 | WRONG FACTS: byte-prefix not idempotent | 3 of 4 (Gemini; grok, Fable concur) | settled by F-01 | no — via F-01 | Hub WRONG FACTS 3 HOLDS. |
| F-27 | V-E4 widened | 2 of 4 (grok, Fable seat) | grok (`:208`) | yes | Fable's X3/X4 split kept as their own rows. |
| F-28 | V-E5 widened | 2 of 4 (grok, Fable seat) | grok (`:210`) | yes | Adds the concurrent `/fill`; Fable's X2 covers `/size`. |
| F-29 | §9 L52 / the bar | — | proposal re-answered | no | Re-stated for v2 with L1, L3, L23, L25, L28, L57; two L3/L1 points left open as named. |
| F-30 | new experiments X1–X9, X11, X12 | 2 of 4 (grok, Fable seat) | seats' texts quoted | yes | Every UNVERIFIABLE-FROM-READS row → an experiment before its chunk (L70); hub's X10 not taken (hub is not a seat). |
| F-31 | owner items W7–W12 | 3 of 4 | pointers only | no | Raised by grok, Fable seat, Gemini; no value proposed by any seat. |
| F-32 | (g) migration + estimate | 3 of 4 | proposal kept | no — proposal kept | Number the desk's at L68 (3 of 3); 19 h / ≈27 h held UNVERIFIED by all three. |

## NEEDS ROUND 2

**R2-V1 — T-V1: does the DRC build seed the voice unit's INITIAL body with already-bound transcripts, or create it BLANK and land every transcript through ONE landing function?**
- Grok (b), verbatim: "The unit has two jobs and one writer class. The build's first create uses `upsert_unit` + `skip_if` (D3-2). Every later transcript uses `append_to_unit`. The build does not append and does not upsert that unit on a re-run." (T-V1: "The build does not call `append_to_unit`."; its (b) walk has the build's create-once write an already-bound block as the initial body, `grok-ruling.md:129`.) Gemini (f): "D3's create-once must be modified. It cannot just create the voice unit blank; it must query `drc_voice` for bound captures and populate the INITIAL body of the unit during the build."
- Fable seat T-V1, verbatim: "The proposal's §4.1 (initial body at creation) plus §4.2 (append) is two landing writers of one unit (L3). §4.1 also changes v2 T6's "creates blank" (`DRC-AUTOMATION-v2:139`; `50-drc-d3-build.md:9`, `:20`). One path removes both problems." Its wording: "His unit `drc-trades/voice-<trade_id>` is created BLANK exactly as v2 T6 / D3-2 create it. Every transcript lands through ONE function, `land_pending(date)`. It is called by the build right after the voice units are created, by the upload request after a transcribe, by the page's retry, and by `cobalt voice land --date`." (full text `voice-tribunal-fable-r1-2026-09-22.md:32`)
- Question for round 2: Is a build-time initial body plus a later `append_to_unit` ONE landing path under L3 (one writer class), or two landing writers of one unit — and which shape does the seam document give D3?

**R2-V5 — T-V5: when more than one trade matches one card (D3-2's trade → nearest prior card), where does a card capture land?**
- Grok T-V5, verbatim: "If the window key is unset, or two trades match one card, or two cards match one trade, the captures stay in `drc_voice` and the build lists `voice not bound: card <id>` on A31, naming the trade keys when there are two. They are never copied onto both trades and never chosen by nearest." Fable seat T-V5: "It is never split, never guessed onto the earliest or latest trade."
- Gemini T-V5, verbatim: "if a card matches multiple trades, the capture binds to the earliest trade, unmatched to A31." Reason: "Binding to the earliest matched trade provides a deterministic home without dropping data."
- Question for round 2: Is binding to the earliest matched trade a correct deterministic rule, or a guess that can put a clip about one attempt on another attempt's unit — given that the unbound capture is kept and listed, not dropped?

## OWNER ITEMS (after the tribunal)

None is a precondition to build (hub ESCALATE 9; checked again here: no seat wrote one as a precondition). Values stay his; tests use constructed settings (L69).
- **W1** capture points — proposal.
- **W2** audio retention — proposal; grok + Fable seat: B sets aside L57.
- **W3** audio home — proposal; "~1 MB/min" UNCITED → X12 (grok), V-E3 (Fable).
- **W4** cloud STT when local is down — proposal.
- **W5** scope — proposal; grok: R100 already sets per-trade.
- **W6** phone microphone — proposal; V-E1 informs.
- **W7** max upload size, max clip length, transcribe time limit (L53) and behaviour while unset — grok (size, clip; unset upload FAILs; time limit an engine tunable), Fable seat W7 (all three his; unset upload unbounded).
- **W8** vocabulary hint on/off + home of his structure list — Fable seat W8.
- **W9** per-day / no-trade voice into `drc-day/voice-no-trades`, later slice — Fable seat W9.
- **W10** `drc_voice` row retention / pruning — Gemini.
- **W11** `/voice` tailnet-only restriction — Gemini (vs grok, Fable seat).
- **W12** his clips in git (stripped) or none (synthetic sound in real-shape container) — proposal/grok vs Fable seat (c).

## FOR DEJAN

W1 — Where do you record? A (v2 default): a mic button on each filled/closed card on your phone or desk during the day, AND on each trade row of `/drc` at the DRC. B: only on the `/drc` trade row, at the DRC. A: proposal; B: proposal's alternative. Grok, Gemini, Fable seat: framed correctly.

W2 — After a clip is transcribed into your DRC, is the audio kept? A (v2 default): kept as long as its transcript, so any block can be re-played and re-transcribed. B: deleted once the text lands in your note. A: proposal, Gemini; grok + Fable seat say B means a block can no longer be replayed (L57 set aside).

W3 — Where do the audio files live? A (v2 default): in your vault next to the day's imports (`1 - Trading/5 - Review/_imports/drc/<date>/`), synced to every device. B: a folder on the Mac only, not synced. A: proposal, Gemini. Size per minute is not known yet — measured from a real phone clip (X12).

W4 — When the local speech-to-text is down, what do you see? A (v2 default): a red "transcript pending — local speech-to-text down" on the card / `/drc` row, audio kept, a retry button; you can type meanwhile. B: your audio is sent to a named cloud speech service instead. All three seats: framed correctly.

W5 — What does voice cover? A (v2 default): per-trade answers only. B: also your per-day block and next-day review grade in the same build. A: proposal; grok: your R100 already set per-trade; the per-day block is a later key (see W9).

W6 — How does the phone record? A: the ASET page is served over HTTPS on your tailnet, and you record inside the page. B (v2 builds first): tap record → your phone's recorder app opens → the file uploads to the page; no change to how the page is exposed. V-E1 tests both on your phone before you choose.

W7 — Limits on a clip: max upload size, max clip length, how long a transcription may run. These are your numbers. A (v2 default, grok): until you set a size, an upload FAILs rather than guessing; the time limit is an engine setting. B (Fable seat): all three are yours; until set, uploads are unbounded, no clip limit, the time limit fails loud.

W8 — Vocabulary hint (the day's tickers + your exit-structure words, given to the engine to spell them right). A (v2 default): on, from config, stored with each transcript; turned off if X6 shows it inserts words you did not say. B (Fable seat): off until X6 passes; your structure list lives in your settings, never in a committed file.

W9 — Voice on a no-trade day. A (v2 default): not in this build; you type your "why no trades" as today. B (Fable seat): a later slice records into the "Why no trades today" unit your R93 DRC already creates.

W10 — The database row of each clip (text, engine, timings). A (v2 default): kept, no pruning. B (Gemini): a pruning schedule you set.

W11 — Who can reach the record button? A (v2 default; grok, Fable seat): whoever can reach the ASET page today — same as `/size` and `/fill`, until the access-token backlog item ships. B (Gemini): the voice upload only answers devices on your tailnet; a LAN-only browser is refused.

W12 — Test files. A (v2 default; proposal, grok): tests use your real clips' shape, stripped of what you name. B (Fable seat): no recording of your voice ever enters git; tests use synthetic sound in the phone's real file format, your clips stay on the Mac.

## Redactions

Count: **0**. No audio, transcript, note line, coach-spec value, ticker, price or P&L of his is in either file. Seat scenario spans that name a ticker or card/trade example (grok `:45`, Fable `:52`) were not copied. No seat proposed a value for one of his keys (no `<key>: value proposed by` pointer needed).

## READING

- `61-voice-tribunal-derive.md` (whole); `LAWS.md` 1–442 (full).
- Hub `voice-tribunal-2026-09-22.md` 1–224; `grok-ruling.md` 1–236; `gemini-ruling.md` 1–116; Fable `voice-tribunal-fable-r1-2026-09-22.md` 1–218.
- Proposal `DRC-VOICE-PROPOSAL-2026-09-22.md` 1–128; `drc-voice-propose-2026-09-22.md` 1–58.
- `cto-2026-09-22.md` rows R66, R90, R92, R93, R99, R100, R101, R106, R108 (grep).
- `DRC-AUTOMATION-v2-2026-09-22.md` 28–36, 60–72, 76–92, 136–150, 174–178, 222–232, 290–298.
- `49-drc-d2-build.md` 1–9, 19–23 + grep; `50-drc-d3-build.md` 1–9, 20, 25, 28 + grep (voice / A26 / D3-4); `52-drc-d5-build.md` grep (D5-3).
- Code/config spot reads (check only): `aset/__main__.py` 1–8; `configs/dev/aset.yaml` 30–41; `aset/web.py` grep (async def / `str(v)` / to_thread); `configs/cobalt/jobs.yaml` 60–72; `heartbeat/probes.py` 465–500; `vaultwrite/writer.py` 457–475, 525–555, 575–590 + grep.

## ESCALATE

1. **NEEDS ROUND 2: R2-V1** (T-V1 initial body vs one landing function) — also a DRC-FINAL change either way (D3 seeds the body, or D3 calls one landing function); the seam document takes round 2's answer.
2. **NEEDS ROUND 2: R2-V5** (T-V5 >1 trade per card).
3. **DRC FINAL — seam, BEFORE D2 LAUNCHES** (grok carried 3; Fable (f)(1); X5): D2-2's confinement must say whether `<date>/voice/` is legal and whether the bytes method creates a missing `<date>/` folder (a daytime card capture precedes the day's first import; `create_if_absent` refuses a missing parent, `writer.py:580-584`).
4. **DRC FINAL — seam** (grok carried 2): `append_to_unit` is a new `VaultWriter` op, added by V3 on top of D2-2's writer change.
5. **DRC FINAL — seam** (grok carried 4; Fable WF1, FC4): the `voice not bound` line must be carried onto D5-3's `drc-day/open_items` (`52-drc-d5-build.md:18`), whose prompt says voice is not in D5 (R100).
6. **DRC FINAL — seam** (grok carried 5): D3's `orphaned` line above his text needs one idempotent edge-insert (not `skip_if`, not an upsert, not a suffix append) — D3's writer, not a voice chunk.
7. **Seam document owed** (L72 P-b; grok (f), Fable (f), FC6): before D2 or V2 launches, cited by D2, D3, V2, V3 prompts. Fable-named entries the grok wording does not cover: `trade_id` stability (X9), `aset/web.py` route order, the CLI group (D3-4 owns `cobalt drc`, `50:27`; the proposal's `cobalt drc voice` would create it first if V1 runs before D3).
8. **DOES NOT HOLD — carried, not pressed after collate**: Gemini (f) "ONE seam document: `DRC-AUTOMATION-v2-2026-09-22.md`" (hub Checked row L72).
9. **Not folded, for the seam document**: Fable (e) — the route checks the card id is an `aset_sizings` row of the posted date, or the trade key a trade of that date's parsed log (mirrors D2-3's screenshot rule, `49:24`); the house (e) wording taken does not state it.
10. **Desk record (author ESCALATE 1)**: CLAUDE.md lists a "3-tier local voice stack" as an interface; none is built (V1, V3). No edit here.
11. **Desk record (author ESCALATE 2 + Fable WF3, read by the derive)**: "trading PC NOT on Tailscale" stands at v2 F17 (`SPRINT-LADDER-v0_1.md:610`), `configs/dev/aset.yaml:33-35` and `src/cobalt/aset/__main__.py:4-6`, against `topics/devices.md:31` (R27). No edit here.
12. **ASTRA PENDING (R13)**: Astra reads v2 (and round 2's result) on Sat 09-26. Round 2 after 2026-09-23 23:59 ET needs his word for `grok` / `agy` (R30 ends; R105 is scoped to `53`–`57`).
No `RE-OPENS A RULING`, no precondition-to-build, no `ASK DESK`. L74: nothing committed by this seat (no git write). MEMORY: none. RULING: none.

## CONTINUE
- 21:45:57 ET — preconditions verified: placeholders 0 · `DERIVE ROW: R108` ×1 · R108 at cto-2026-09-22.md:50 carries both literals, his words "Opus 5.5", committed d2189802 · cto-2026-09-23.md missing (recorded, not fatal) · seat = claude-opus-5-5 (row / launch line / this session) · hub stop line committed 1665a5f0, houses that ruled 2 of 3, astra `METER — proceed on three` · Fable stop line committed 75b2aa57 · 7 allow + 3 deny strings each count 1 in `22-draft-setups-tribunal.md`.
- 21:50:15 ET — all inputs read; fold decisions made.
- 21:53:03 ET — v2 written (`docs/30 - Design/DRC-VOICE-v2-2026-09-22.md`).
- 21:53:33 ET — this report written whole. next: none — derive complete. NEXT STEP, not this seat's: the desk commits both files; a round-2 hub is drafted for R2-V1 and R2-V5 only; Astra reads the FINAL Sat 09-26 (R13).

VOICE DERIVED v2 · folds: 32 · verbatim: 17 · needs round 2: 2 · owner items: 12 · ESCALATE: 12
