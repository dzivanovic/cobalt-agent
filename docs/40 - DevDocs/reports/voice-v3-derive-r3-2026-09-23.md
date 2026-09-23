# VOICE v3 — THIRD DERIVE (R3, the last) — 2026-09-23

Seat `voice-v3-derive-r3-0923` · `claude-opus-5-5` (DERIVE ROW 09-22 R109) · launch row `cto-2026-09-23.md` R49 · started 12:24 ET · FINAL written 12:32 ET · report written 12:3x ET (`date` per line below).

§0 Headline
- Converged: **1 of 3**. R2-3 (ADOPT A-V5, all three seats: new slice V5, 4 h). **For Dejan: 2**, R2-1 (sides A / B) and R2-2 (sides A / B / C).
- FINAL **written**: `docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md`. Every converged point is folded; each unresolved point stands in place with its sides verbatim.
- O1: **ruled B** (R39; scope per R43 = SCOPE-R39). All three `FOLD:` lines carry SCOPE-R39 verbatim. The L28 fold is the desk's (L58), at his approval.
- Total 27 h, ≈38 h (was 22 / ≈31), the same under every letter. **ASTRA PENDING (R13)**: Astra reads the FINAL on Sat 09-26. ESCALATE: 12.

## DIGEST FOR THE DESK

**Seats that ruled round 3:** grok, gemini (hub `33`, `houses that ruled: 2 of 3`) and the Anthropic seat (`34`). Astra was `SKIPPED — R13 (probe UP, recorded)`.

**Who MOVED from round 2** (the houses and the seat crossed on R2-1 and R2-2):
- grok: R2-1 B → N1; R2-2 S → NEITHER; R2-3 B → A-V5.
- gemini: R2-1 B → N1; R2-2 P → N2; R2-3 A-V1 → A-V5.
- the Anthropic seat: R2-1 N1 → B; R2-2 N2 → S; R2-3 A-V5 held.

**R2-1 — FOR DEJAN item 2.**
- Side A = `B`, the Anthropic seat: an age-gated start sweep plus a per-turn sweep.
- Side B = `N1`, grok and gemini: a delete-ALL start sweep, with no per-turn sweep.
- The hub's "CONVERGED 2-0" counts houses only. Rule (ii) is not met: the seat's B rests on file facts that HOLD (`aset.plist:29-30`, `start_aset.sh:69`; hub GM4) plus behaviour that is UNVERIFIABLE (X22 = H1). Nothing it rests on DOES NOT HOLD, and nothing was withdrawn.
- **V1's sweep:** one unlink function under both sides; side A calls it at start and at every turn, side B at start only. V1 stays 9 h.
- **V4's probe:** counts only, never deletes, under both sides. The RESTARTS cell reads `com.cobalt.heartbeat` reload under both sides (a 900 s one-shot job, not a resident). V4 stays 2 h.

**R2-2 — FOR DEJAN item 3, three sides** (ESCALATE 1):
- Side A = `S`, the Anthropic seat: single attempt; "takes no retry" and "no Cobalt ownership" are in the law.
- Side B = `N2`, gemini: "never a three-way merge … records no merge baseline … every later write treats it as his".
- Side C = grok's NEITHER: the retry stays inside `build`; there is no returnable `unit_after`; when `last_after` is None, the existing `baseline_missing` path applies.
- Every side is a span-bound sha256 over before and after, carries SCOPE-R39, and adds +1 h on V3.
- The §6 Cobalt-owned-unit row follows the letter. The his-text row points to the letter's `FOLD:` op.

**R2-3 — CONVERGED `[R3F-09]`.** ADOPT A-V5 from grok, gemini and the Anthropic seat. Slice **V5 — trading-logic drafts**: after V1, 4 h, RESTARTS `com.cobalt.aset` plus the `cobalt.settings` importers (AST walk). The `§9:` and `F-07:` lines are identical in all three; grok's are taken.

**O1:** RULED B (R39) with R43's scope. The fold text is the `FOLD:` line of his item-3 letter.

**Build prompts wait on:**
- his ONE approval, with item 2's and item 3's letters;
- the desk's L28 fold under L58, before V3's voice-ordered edit class switches on;
- the S1 seam document, before V1;
- DRC D2 + D3 merged, plus S2's D3 / D5-3 changes, before V2;
- the first-gate experiments:
  - before V1: E1–E8, E10, X1, X3, X5, X12, X13, G2 / K5, X22;
  - before V2: E9, E11, X2, X4;
  - before V3: X21, X23.

## Preconditions

| check | result |
|---|---|
| DERIVE ROW | `grep -c -x -E` → 1; line 1 `R109` |
| R109 row | `cto-2026-09-22.md:56`, one row, carries "Make all Opus 5.5 for now" and `claude-opus-5-5` |
| R109 committed | `75b2aa5790368bdd52e5802b64780567960163ed` |
| R109 still stands | `cto-2026-09-23.md` rows :4, :23 (R21 "09-22 R109 … STANDS"), :24, :36, :38, :40, :44, :48, :52 cite it; none ends or changes it. Re-checked after the desk file changed on disk at 12:3x: new row R50 (:53) does not touch R109 or O1 |
| seat | this session's model id `claude-opus-5-5` = the launch `--model` = R109 |
| launch row | `cto-2026-09-23.md:52` R49 names `35-voice-v3-derive-r3.md` |
| hub r3 stop line | `VOICE V3 TRIBUNAL R3 DONE · grok: TRIBUNAL R3: BUILD · gemini: TRIBUNAL R3: BUILD · astra: SKIPPED — R13 (probe UP, recorded) · houses that ruled: 2 of 3 · converged: 2 of 3 · ESCALATE: 11`; committed `15a725331d8f6f46c6a2fd35fe02a281670e52a5` |
| seat r3 stop line | `VOICE V3 TRIBUNAL FABLE R3 DONE · R2-1: ADOPT B · R2-2: ADOPT S · R2-3: ADOPT A-V5 · ESCALATE: 4`; committed `eb410b69e78e943a0e46c81eb6fb87ea48ff8de3` |
| a house ruled | grok answered R2-1 ADOPT, R2-2 NEITHER, R2-3 ADOPT; gemini ADOPT on all three |
| Astra | `SKIPPED — R13 (probe UP, recorded)` → recorded; FINAL header `ASTRA PENDING (R13)` |
| launch strings | 7 allow + 3 deny, quotes included; each `grep -c -F` → 1 in `22-draft-setups-tribunal.md` |
| O1 R39 | `cto-2026-09-23.md:42` carries `write to everywhere with my confirmation` |
| O1 R43 | `cto-2026-09-23.md:46` carries `houses rule mechanics only` |
| later O1 rows | run date 09-23: no desk file from 09-24 on; nothing to check |
| SCOPE-R39 in each `FOLD:` source | `grep -c -F` → grok r3 1 · gemini r3 1 · the Anthropic seat r3 1 |

**R39, verbatim:** `| R39 | 10:2x ET | VOICE O1 (L28 scope), his words: "I want my word to allow write to everywhere with my confirmation, is that one of the options (on cobalt voice question)" → **B, widened to his words**: a voice-ordered edit may change ANY field of ANY note in his vault — his own text, his dictated-answer units, everywhere — ONLY on his spoken or tapped confirmation of the read-back ("<field>: <before> → <after>"), span-bound, versioned (mechanics = round 2, R2-2). The L28 amendment text is written by the voice FINAL (`26`) quoting this row and folded into LAWS.md by the desk at approval of the FINAL (L58); until then L28 stands unchanged. | APPROVED — into `26`'s FOR DEJAN (answered); LAWS fold at FINAL approval; memory APPLIED |`

**R43, verbatim:** `| R43 | 11:0x ET | — DESK RECORD + LAUNCH, no new words of his: `26` STOPPED `VOICE V3 FINAL DERIVED · converged: 0 of 3 · round 3: 3 · O1: ruled B · FINAL: not written · ESCALATE: 9`. Its ASK DESK 1 (the desk's "widened" R39 vs FOLD B's scope clause) — DESK ANSWER: the scope is HIS words ("allow write to everywhere with my confirmation") = any field of any note on his confirmation; houses rule mechanics only. Round 3 (the last, L39) → drafter `prompts/2026-09-23/32-draft-voice-v3-r3.md` LAUNCHED; what round 3 leaves reaches him as one A/B per item. | DESK LAUNCH — no fold |`

## Fold table

Three seats ruled round 3 on each item: grok, gemini and the Anthropic seat. "r2" is the seat's round-2 answer.

| R3F | item | seats (n, named) | answers (r3; r2 beside) | whose wording | adopted verbatim? | why (≤25 words) |
|---|---|---|---|---|---|---|
| R3F-01 | R2-1 | 3: grok, gemini, Anthropic seat | grok N1 (r2 B) · gemini N1 (r2 B) · seat B (r2 N1) | — | FOR DEJAN (item 2) | Rule (i) fails, since the answers differ. Rule (ii) fails: the seat's B rests on GM4's file facts (HOLD) and X22 / H1 (UNVERIFIABLE); nothing DOES NOT HOLD |
| R3F-02 | R2-1 `§5:` slot | 3 | seat: B's bullet · grok = gemini: N1's bullet | seat `…fable-r3…:35`; grok `:26` = gemini `:7` | FOR DEJAN — sides A / B verbatim | Different mechanisms. Side B carries a sentence the seat WITHDREW (W1) → ESCALATE 2 |
| R3F-03 | R2-1 `V4:` slot | 3 | seat's own row · grok's and gemini's rows (the same except "…") | side A: seat `:37`; side B: gemini `:8` (the shorter house line) | FOR DEJAN | Hub `## Rulings table`: the house rows differ only by "…" spelled out → same mechanism, shorter taken → ESCALATE 3 |
| R3F-04 | R2-1, common to both sides: only the voice module deletes; the heartbeat counts (`[F-22]` note) | 3 | all three | text of both sides' `§5:` | yes (as a pointer, not a fold of R2-1) | GK2, K1–K4 HOLD; both sides' verbatim text says so |
| R3F-05 | R2-2 | 3 | grok NEITHER (r2 S) · gemini N2 (r2 P) · seat S (r2 N2) | — | FOR DEJAN (item 3) | Three distinct answers. No supporting claim DOES NOT HOLD; GM9–GM11 and GK11 PARTLY HOLD |
| R3F-06 | R2-2 `FOLD:` slot | 3 | S · N2 · grok's | seat `:63`; gemini `:17`; grok `:51` | FOR DEJAN — A / B / C verbatim | SCOPE-R39 in each (count 1 each); the mechanisms differ on retry and on the no-baseline clause (hub ESCALATE 8) |
| R3F-07 | R2-2 `§6:` slot (Cobalt-owned unit) | 3 | S · N2 · grok's | seat `:61`; gemini `:16`; grok `:49` | FOR DEJAN | None excludes a unit class (SCOPE-R39 kept). Seat's `restore` claims UNCHECKED by a hub — read by the derive at `writer.py:1102-1106`, `:1145-1162` |
| R3F-08 | §6 his-non-blank-text row | — | O1 RULED B | pointer to item 3's `FOLD:` op | yes (a pointer, no new mechanism) | R39 / R43; op per his letter |
| R3F-09 | R2-3 | 3 | grok A-V5 (r2 B) · gemini A-V5 (r2 A-V1) · seat A-V5 (r2 A-V5) | grok | **yes — CONVERGED (i)** | Same label, two houses among them; G10 no longer pressed; GK14–GK21, GM12–GM15, C18–C22 HOLD |
| R3F-10 | R2-3 `§9:` V5 row | 3 | identical | grok `:74` (= gemini `:24` = seat `:87`) | yes | Identical in all three (hub counts 1, 1, 1); the house line taken |
| R3F-11 | R2-3 `F-07:` line | 3 | identical | grok `:76` | yes | Identical in all three (hub counts 1, 1, 1) |
| R3F-12 | V3 row (O1 dependency, hours) | — | every R2-2 side +1 h | seat `:65`; grok `:47`; N2 price seat r2 `:51` | yes (arithmetic + "O1 RULED B (R39)" marker) | The sides' own numbers; the marker per the prompt |
| R3F-13 | total hours | — | — | arithmetic | yes | 9+7+5+2+4 = 27; 27 × 1.4 = 37.8 ≈ 38; GUESS / UNVERIFIED kept |
| R3F-14 | experiments | — | E7 sharpening, X20, X21 (two sharpenings), G2 / K5, X22 = H1, X23 = H2, K10 = X2 | seat, grok, hub | yes (merged, attributed) | L70; each placed before the slice it gates |
| R3F-15 | V1 Depends cell | — | + G2 / K5, X22 | hub r3 `## Experiments named` (gates V1) | yes | Gate reference only |
| R3F-16 | L52 and the bar: L7, L28, L40 | — | — | derive, citing the rows above | yes | Re-answered for the FINAL |
| R3F-17 | OWNER ITEMS O1 | — | RULED B | his words, R43 | yes | R39 / R43 verbatim |

## FOR DEJAN

O1 — ruled B, cto-2026-09-23.md R39: "I want my word to allow write to everywhere with my confirmation, is that one of the options (on cobalt voice question)"; scope per the desk's R43: any field of any note, on his confirmation.

**2. R2-1 — when is leftover audio from a crash deleted?**
You press and speak; Cobalt crashes mid-transcribe and launchd restarts it at once. You hear nothing; that clip's scratch file is left on the Mac. A: the restart keeps any clip younger than the age limit; your next press deletes it (AMBER), and the heartbeat counts it meanwhile. B: the restart deletes every file in the scratch folder at once (AMBER). Changes §5 and the §9 V4 row. Round 3 was the last: both houses hold B, the Anthropic seat holds A, and no hub row fails either side.

- **Side A — `B`** — held by the Anthropic seat (round 3). Grok and gemini held it in round 2.
  - `§5:` **Crash leftovers:** The voice module sweeps: on `com.cobalt.aset` start and at the start of every turn it deletes scratch files older than `scratch_max_age_s` (AMBER line per file; a failed unlink RED). The heartbeat's `voice_scratch` probe only COUNTS such files and never deletes (L40 — the voice module owns its scratch). The config schema refuses `scratch_max_age_s ≤ stt_timeout_s`.
  - `V4:` | **V4 — ops** | `voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s` in the `scratch_dir` it resolves through the voice config's one loader, and names that directory in its detail line: some → AMBER with the count and the oldest age, none → OK, unreadable → RED unknown; it never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist` (as `COBALT_VAULT_PATH`, `:20-21`); model-fetch deploy step; the `tailscale serve` deploy step (§11 W6); DevDocs | no (probes read) | — | V1 | `com.cobalt.heartbeat` (plist in the diff → reload, L42; a 900 s one-shot job, `heartbeat.plist:60-61`) | 2 |
  - Hub rows:
    - GM1: HOLDS as B's logic; the ages are UNVERIFIABLE FROM READS.
    - GM2: HOLDS.
    - GM4: HOLDS as design text. The file facts it cites hold: `aset.plist:29-30` `AbandonProcessGroup` true; `start_aset.sh:69` `exec uv run python -m cobalt.aset`. Whether a killed job can leave a live child is UNVERIFIABLE FROM READS → X22 / H1.
    - C9: HOLDS (static keys); the respawn delay is UNVERIFIABLE FROM READS → E7 sharpening.
    - C11, C12: HOLD.
    - Round 2: K1–K4, C3, C4, G1, G3 HOLD; G2 / K5 UNVERIFIABLE → run.
- **Side B — `N1`** — held by grok and gemini (round 3). The Anthropic seat held it in round 2. It carries the sentence the Anthropic seat WITHDREW in round 3 (W1: "the upload handler is the directory's one writer and no turn of a new process is live, so any file present is a leftover").
  - `§5:` (grok `grok-ruling-r3.md:26` = gemini `gemini-ruling-r3.md:7`) **Crash leftovers:** the voice module is the ONLY deleter of scratch files (L40): the turn's `finally:` unlink above, and on every `com.cobalt.aset` start, before the first request is served, a sweep that deletes EVERY file in `scratch_dir` — the upload handler is the directory's one writer and no turn of a new process is live, so any file present is a leftover; one AMBER line per file deleted (a turn died mid-way), an unlink that fails is RED (L9). One unlink function serves the turn and the sweep (L3). The heartbeat's `voice_scratch` probe (V4) only COUNTS: files older than `scratch_max_age_s` → AMBER with the count and the oldest age; none → OK; `scratch_dir` unreadable → RED unknown; it never deletes. The probe resolves `scratch_dir` through the voice config's one loader; the production override is carried in `ops/com.cobalt.heartbeat.plist` exactly as `COBALT_VAULT_PATH` is (`:20-21`) and in `ops/start_aset.sh` (`:32`), and the probe's detail line names the directory it read. The config schema refuses `scratch_max_age_s ≤ stt_timeout_s` (L10).
  - `V4:` (gemini `gemini-ruling-r3.md:8`, the shorter house line) | **V4 — ops** | `voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s`, never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; … | no (probes read) | — | V1 | `com.cobalt.heartbeat` reload (plist in the diff, L42) | 2 |
  - Grok's `V4:` line (`grok-ruling-r3.md:28`) is the same row, with "…" spelled out as "model-fetch deploy step; the `tailscale serve` deploy step (§11 W6); DevDocs".
  - Hub rows:
    - GM3: HOLDS as N1's text; "immediately" is UNVERIFIABLE FROM READS.
    - GM4: HOLDS as design text; one adjacent behaviour is UNVERIFIABLE FROM READS → X22 / H1.
    - GM5, GK3: HOLD as design text.
    - GK1: HOLDS (range +2); no `ThrottleInterval`.
    - GK2: HOLDS.
    - GK4, GK5: HOLD.
    - C9, C10, C11, C12: HOLD.
    - Round 2: K1–K4, C3, C4, G1, G3 HOLD.
- DESK RECOMMENDATION: <filled by the desk before it sends; the derive writes nothing here — L37>
- What each side builds: V1 9 h under both sides. Side A has one sweep function called at start and at every turn; side B calls it at start only, with no age test (grok ±0 h, `grok-ruling-r3.md:24`; the seat "V1 h unchanged", `…fable-r3…:39`). V4 is 2 h under both. Total unchanged: 27 h, ≈38 h.

**3. R2-2 — after you confirm a voice edit, what happens to your new text?**
You say "change <field> in <note> to <text>", hear "<before> → <after>", and say yes; Cobalt replaces only that span. The three sides differ on two points:
- if you save elsewhere in the note between the read-back and the write, is the write refused and read back (A), or retried against the fresh file (B, C)?
- when Cobalt itself later writes that spot, what does it keep: A — your bytes win once, logged; B — "every later write treats it as his"; C — your bytes win against the baseline on record, but Cobalt's text applies when no baseline exists.
Round 3 was the last, and the three seats hold three different texts.

- **Side A — `S`** — held by the Anthropic seat (round 3). Grok held S in round 2.
  - `FOLD:` [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace any field of any note in his vault — his own text, his voice units and Cobalt's own units alike — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.
  - `§6:` | A Cobalt-owned unit | on his confirmed read-back (SCOPE-R39): the O1 span op — the same op as his own text: replaces only the confirmed span inside the unit body, single attempt, under the mtime guard and `_session_gate`, never `merge3`, never `upsert_unit` (which would record his bytes as the producer's `unit_after` baseline, `writer.py:766`); versioning row with before, after, `unit_before` / `unit_after` = the span bytes and the turn id, keyed by a section label no producer writes, so `last_after` never returns it (`store.py:102-104`) and `restore` still locates it by content (`writer.py:1145-1162, :1020-1038`). For a computed value, the reply also names that value's own correction path (R90 resolve action / A28, v2 §2) as the lasting fix, because the unit's producer rewrites the unit. | L28 as amended (O1, R39): his confirmed bytes are his — the producer's next `upsert_unit` merges against its own last `unit_after`, the human wins and one `vault_overrides` row is logged (`merge.py:18-24`) |
  - Hub rows:
    - C13 (= C1): HOLDS — attempt 2 re-runs `build`.
    - C14, C15, C16, C17: HOLD.
    - Round 2: C2 / K9 HOLD — `_commit`'s window is snapshot → commit.
    - GK8: HOLDS — a baseline-recording op makes `merge3(B, C, D)` keep C and log an override. This is the failure S's last sentence must forbid.
    - Grok contests that S's sentence forbids that row (`grok-ruling-r3.md:38`: "S's \"no Cobalt ownership is created\" does not forbid that row"). No hub row rules on the reading.
    - The seat's round-3 claims are UNCHECKED by a hub. The derive read them:
      - `writer.py:828-829`: "the base is `last_after` — what Cobalt wrote here last — and anything else on disk is the human's, which wins".
      - `writer.py:1102-1106`: `restore` refuses a row with no section.
      - `writer.py:1145-1162`: a per-unit row whose section is absent is located by `_locate_region`.
    - X23 (= H2) is still to run.
- **Side B — `N2`** — held by gemini (round 3). The Anthropic seat held N2 in round 2.
  - `FOLD:` (`gemini-ruling-r3.md:17`) FOLD B: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace any field of any note in his vault — his own text, his voice units and Cobalt's own units alike — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write goes through `VaultWriter` with the mtime guard and `_session_gate`, replaces only that span with the confirmed after bytes — never a three-way merge — and is refused if, when the writer reads the note to write, the span no longer equals the confirmed before bytes; it is versioned with before, after and the turn id, and records no merge baseline: the replaced text remains his, and every later write treats it as his. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.
  - `§6:` (`gemini-ruling-r3.md:16`) | A Cobalt-owned unit | voice edit via `upsert_region` recording no merge baseline | numbers are code; human-wins untouched |
  - Hub rows:
    - GM6, GM7, GM8: HOLD.
    - GM9: PARTLY HOLDS — for a unit a Cobalt write covers, `last_after` None ⇒ Cobalt's next text applies.
    - GM10: PARTLY HOLDS — `upsert_region` only as a NEW mode.
    - GM11: PARTLY HOLDS — beyond the first next write UNVERIFIABLE FROM READS → H2.
    - GK9: HOLDS, and contradicts "every later write treats it as his" when `last_after` is None (hub ESCALATE 8).
  - None of these rows DOES NOT HOLD.
- **Side C — grok's NEITHER** — held by grok (round 3). It moved from S.
  - `FOLD:` (`grok-ruling-r3.md:51`) [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace any field of any note in his vault — his own text, his voice units and Cobalt's own units alike — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write goes through `VaultWriter` with the mtime guard and `_session_gate`, replaces only that span with the confirmed after bytes — never a three-way merge — and is refused if, when the writer reads the note to write, the span no longer equals the confirmed before bytes; it is versioned with before, after and the turn id, and records no `unit_after` that `last_after` would return for that unit: the replaced text remains his. A later write merges against the baseline already on record, so on-disk bytes that differ from it are his and win, logged as an override; when `last_after` is None the writer's existing `baseline_missing` path applies Cobalt's new text, the same as a hand edit with no baseline. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.
  - `§6:` (`grok-ruling-r3.md:49`) | A Cobalt-owned unit | the one confirmed span-replace: `build` refuses unless the span equals the confirmed before bytes, then writes the confirmed after bytes, no `merge3`, no `unit_after` that `last_after` would return | a Cobalt line he changed is his against the baseline already on record — the next write human-wins and logs an override (L28). `last_after` None stays the existing `baseline_missing` path |
  - Hub rows:
    - GK6: HOLDS on read.
    - GK7: HOLDS on read; the Obsidian timing is UNVERIFIABLE FROM READS.
    - GK8, GK9, GK10, GK12: HOLD.
    - GK11: PARTLY HOLDS — "stays" is UNVERIFIABLE FROM READS → H2.
    - GK13: the price is UNVERIFIABLE FROM READS.
  - Note: grok's price bullet (`grok-ruling-r3.md:47`, not its `FOLD:` or `§6:` line) names "versioning row with no unit key, as `create_if_absent` does at `:603-604`". That is the row shape the Anthropic seat WITHDREW (W4), because `restore` refuses a no-section row (`writer.py:1102-1106`, read by the derive).
- DESK RECOMMENDATION: <filled by the desk before it sends; the derive writes nothing here — L37>
- What each side builds: V3 +1 h under all three sides (seat `…fable-r3…:65`; grok `grok-ruling-r3.md:47`; N2's price, seat round 2 `:51`), so V3 is 5 h. Side A is a single-attempt span op. Sides B and C put the span check inside `build` under the writer's existing retry, and `[F-09]` §2.6 stands ("`[F-09]` still disables the retry; that text stays", grok `:36`). The total is the same under every side: 27 h, ≈38 h.

APPROVE: the VOICE v3 FINAL design (docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md, sha256 taken by the desk at commit) for build, with item 2 = A / B; item 3 = A / B / C — yes / no

## OWNER TEST

| item | raised by | PASSES / FAILS | where it went |
|---|---|---|---|
| O1 — L28 scope | earlier rounds | PASSES (a law he owns) | RULED by R39 / R43; `## FOR DEJAN` gets one line and asks nothing |
| grok "OWNER: none. …" | grok | — | nothing sent |
| gemini (no `OWNER:` line) | — | — | nothing sent |
| Anthropic seat "none" (it does not restate its round-2 L7 / L28 line) | Anthropic seat | — | nothing sent |

No round-3 seat sent him an item. Items 2 and 3 of `## FOR DEJAN` are not owner items: they are what L39 sends him when the last round leaves a split.

## Redactions

- Made by this derive: **0**.
- Carried: **1** placeholder already made by the second derive — `[user data: grok-ruling-r2.md:41]` in the FINAL's `## Dissents, verbatim` (grok r2 R2-3).
- Grok r3 `:59` carries a `[user data]` placeholder (hub ESCALATE 3). That sentence is not quoted anywhere here.
- No ticker, price, note text or spoken word of his appears in the FINAL or in this report.

## READING

- Prompt `35-voice-v3-derive-r3.md` (whole). `LAWS.md` 1–442 (full).
- Hub r3 `voice-v3-tribunal-r3-2026-09-23.md` (whole). Raw rulings `r3/grok-ruling-r3.md` (whole) and `r3/gemini-ruling-r3.md` (whole).
- The Anthropic seat r3 `voice-v3-tribunal-fable-r3-2026-09-23.md` (whole).
- Second derive `voice-v3-derive-r2-2026-09-23.md` (whole).
- Derived design `VOICE-v3-derived-2026-09-23.md` (whole).
- Round-2 FOLD A lines, by grep: `r2/grok-ruling-r2.md:33`, `r2/gemini-ruling-r2.md:15`, `voice-v3-tribunal-fable-r2-2026-09-23.md:53`. Seat r2 price lines by grep (`:32`, `:51`).
- Code, only where a side's unchecked claim turned on it: `vaultwrite/writer.py:824-831`, `:1098-1109`, `:1136-1165`.
- `cto-2026-09-22.md` R109 (grep). `cto-2026-09-23.md`: R109, `35-…`, R39, R43 (grep), and rows R50–R69 (grep) after the on-disk change.

## ESCALATE

1. `ASK DESK: R2-2 leaves three distinct sides after the last round — send A / B / C as drafted, or does the desk narrow it under L39? [12:33 ET]` Safe default taken: all three sides stay, lettered (desk R45 ESC 2: "every distinct round-3 position lettered A / B / C, none dropped").
2. `ASK DESK: R2-1 side B (N1, held by grok and gemini in round 3) carries a sentence the Anthropic seat WITHDREW (W1). The rule says a withdrawn sentence is never folded; both houses now hold it as their own text. Does it stand as a side? [12:33 ET]` Safe default taken: shown as side B, marked with W1 and the hub's GM4 / H1 status. He rules (L39); if he picks B, the sentence is his choice, not a fold on the seat's authority.
3. **R2-1 side B's `V4:` line** is gemini's, the shorter house line (the rule). It keeps a literal "…"; grok's line spells that out as the derived row's remaining words (hub ESCALATE 9). Both are shown in `## FOR DEJAN` item 2. A V4 build under side B reads grok's words for the "…".
4. **Hours recomputation changed the total:** derived 22 h, ≈31 h → FINAL **27 h, ≈38 h** (9 + 7 + 5 + 2 + 4 = 27; 27 × 1.4 = 37.8).
   - The houses' "26 h, ≈36 h" counts V5 only.
   - V3 goes from 4 to 5 under every R2-2 side (+1 h: seat `:65`, grok `:47`, N2 seat r2 `:51`).
   - R2-1 sides are ±0 h.
5. **The hub's "converged: 2 of 3" is not this derive's count** (1 of 3). R2-1 counted houses only; the Anthropic seat's contrary B rests on no DOES-NOT-HOLD claim and on no withdrawn one (rule (ii) not met). The same shape as the second derive's ESCALATE 2, with the seats crossed.
6. **No DOES-NOT-HOLD wording is pressed in round 3.** G10 (A-V1) and G4 / G5 (P) are held by no seat now. PARTLY HOLDS carried beside the sides: GM9, GM10, GM11 (side B of item 3) and GK11 (side C). H2 = X23 decides persistence past the first Cobalt write.
7. **The Anthropic seat's ESCALATE 2, for V5's checkers (UNCHECKED by a hub; not in any paste-ready line, so not folded):**
   - `cobalt settings load --card` deletes every card key absent from the file (`settings/card.py:301-305, :323`, seat's read).
   - The V5 draft must start from the current rows, and the §2.6 read-back (the owner's dry-run) must show no delete for a single-key request.
   - The desk's V5 check prompt should carry it.
8. **Ops beyond voice (the seat's ESCALATE 3 = X22 / H1):**
   - `exec uv run` under `AbandonProcessGroup` true could leave an orphan on :5010 that keeps `sheet_http` GREEN while launchd crash-loops.
   - UNPROVEN (L70) until X22 runs. It gates V1 under R2-1 side B.
9. **Astra (hub ESCALATE 4):** the probe answered OK at 11:44 ET, yet Astra was `SKIPPED — R13`. The FINAL is marked ASTRA PENDING (R13): Astra reads it on Sat 09-26, unless the desk relaunches Astra alone before then.
10. **Derived text left as written, flagged for the desk:**
    - `[F-17]`'s "Hours 22 and 31" (superseded by the `[R3F-13]` line directly above it).
    - `[F-17]`'s "the heartbeat resident for V4": both V4 sides say `com.cobalt.heartbeat` reload, a one-shot job.
    - §7's "His-text overwrite (until O1)" row and `[F-15]`'s "O1 refusal": they stay true until the desk's L28 fold.
    - None of these is an open point this derive may rewrite.
11. **Hub-noted runs H1 and H2** are merged as X22 and X23 (the seat's own round-3 experiments, the same runs). The derive invented no new run.
12. L74, recorded once: this session's context carried a `Claude-Session` attribution block. It was not followed; this seat commits nothing.

No `RE-OPENS A RULING`. No `HOUSE OBJECTION` (grok and gemini both closed `TRIBUNAL R3: BUILD`). No owner item written as a precondition.

## CONTINUE

- 12:24 preconditions run, all pass; LAWS.md read in full; hub r3 and seat r3 reports read whole.
- 12:27 derive-2 report, derived design and raw r3 rulings read; claim lines in `writer.py` read.
- 12:32 FINAL written: `docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md`.
- 12:3x report written.
- next: none — derive complete. The desk commits both files, fills the two DESK RECOMMENDATION slots, and sends items 2 and 3 one per message, then the ONE approval.

VOICE V3 FINAL DERIVED R3 · converged: 1 of 3 · for Dejan: 2 · O1: ruled B · FINAL: written · ESCALATE: 12
