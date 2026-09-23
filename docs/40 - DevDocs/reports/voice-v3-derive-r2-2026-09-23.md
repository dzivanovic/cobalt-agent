# VOICE v3 — second derive (round 2) — 2026-09-23

Seat `voice-v3-derive-r2-0923` · `claude-opus-5-5` (09-22 R109) · started 10:53 ET · report written 10:55 ET.

§0 Headline
- Converged: **0 of 3**. R2-1, R2-2 and R2-3 all go to `## NEEDS ROUND 3` (L67: round 3 is the last; L39: what it leaves → Dejan).
- R2-1: both houses ADOPT B, but the Anthropic seat moved to NEITHER on a claim no hub checked and that does not fail on read (rule (ii) not met). R2-2: three different answers (S / P / NEITHER). R2-3: three different answers (B / A-V1 / A-V5).
- FINAL: **not written** (the rule: only at 3 of 3). The derived design stays the round-3 input.
- O1: **ruled B** — `cto-2026-09-23.md` R39, his words quoted below; the desk's "widened" reading goes past FOLD B's scope clause → `ASK DESK` 1. ASTRA PENDING (09-22 R13): Astra reads the derived design and the round-3 result on Sat 09-26.

## DIGEST FOR THE DESK

- Seats that ruled round 2: Grok, Gemini (houses; hub `24`, `houses that ruled: 2 of 3`), the Anthropic seat (`25`). Astra: `METER — proceed on three`.
- **R2-1 — NEEDS ROUND 3.** Grok ADOPT B, Gemini ADOPT B, the Anthropic seat NEITHER. The hub's "CONVERGED 2-0" counted houses only. Under this derive's rule, the seat's contrary answer counts unless its claim fails or was withdrawn. It rests on B's own cross-key refusal plus `KeepAlive` (`ops/com.cobalt.aset.plist:42-43`, read by the derive), and neither fails.
  - All three seats already agree on these sub-points: the heartbeat never unlinks (a); the `scratch_max_age_s ≤ stt_timeout_s` refusal is kept (b); V4's `voice_scratch` probe only COUNTS (d).
  - Still split: B's age-gated start sweep plus a per-turn sweep, against a delete-ALL start sweep with no per-turn sweep.
- **V4's probe under R2-1:** count-only under every answer. The V4 row's text is still round 3's, because it comes from whichever R2-1 wording wins.
- **R2-2 — NEEDS ROUND 3.**
  - Grok ADOPT S: span-bound, "takes no retry" and "remains his" in the law.
  - Gemini ADOPT P: "that one diff", "note changed". Its supporting claims G4 and G5 DO NOT HOLD as worded.
  - The Anthropic seat NEITHER: span-bound, retry left to the design, "never a three-way merge … records no merge baseline".
  - All three FOLD A / FOLD B pairs differ only in the scope clause.
- **R2-3 — NEEDS ROUND 3.**
  - Grok ADOPT B: no slice in V1–V4; `unsupported`.
  - Gemini ADOPT A: V1, 12 h, `settings/propose.py`. Its claim G10 DOES NOT HOLD as worded.
  - The Anthropic seat ADOPT A: new V5 after V1, 4 h, owner-drafted file in `data/voice-drafts/`.
  - All three agree that voice never APPLIES a trading-logic change (L40: it only drafts, to the owner).
- **O1:** ruled B (R39). The FOLD B mechanics are R2-2's, still split. The L28 fold waits for round 3 and the FINAL.
- **Build prompts wait on:**
  - the round-3 FINAL and his ONE approval;
  - the S1 model-access seam document, before V1;
  - DRC D2 + D3 merged, plus seam S2's D3/D5-3 changes, before V2;
  - the first-gate experiments, derived E1–E11 and X1–X5, X12, X13, plus the round-2 runs listed under `## ESCALATE` 6.
- Hours: not recomputed (no FINAL). The derived total stands: 22 h, ≈31 h, GUESS / UNVERIFIED.

## Preconditions (checked 10:54 ET, one Bash call each)

| check | result |
|---|---|
| DERIVE ROW | `grep -c -x -E` → 1; `R109` |
| R109 row | `cto-2026-09-22.md:56`, one row, carries "Make all Opus 5.5 for now" and `claude-opus-5-5` |
| R109 committed | `75b2aa5790368bdd52e5802b64780567960163ed` |
| R109 still stands | `cto-2026-09-23.md` rows :4, :23, :24, :36, :38, :40, :44 cite it; none ends or changes it |
| seat | this session `claude-opus-5-5` = launch `--model` = R109 |
| launch row | `cto-2026-09-23.md:44` R41 names `26-voice-v3-derive-r2.md` |
| hub stop line | `VOICE V3 TRIBUNAL R2 DONE · grok: TRIBUNAL R2: BUILD · gemini: TRIBUNAL R2: BUILD · astra: METER — proceed on three · houses that ruled: 2 of 3 · converged: 1 of 3 · ESCALATE: 8`; committed `9abaf637488f66c62e2a91d02b6d35c542c426fc` |
| seat stop line | `VOICE V3 TRIBUNAL FABLE R2 DONE · R2-1: NEITHER · R2-2: NEITHER · R2-3: ADOPT A (V5) · ESCALATE: 2`; committed `279a7be233e3005d686939e67562df2dd6356c33` |
| a house ruled | Grok and Gemini each answered R2-1, R2-2, R2-3 with `ADOPT` |
| Astra | `METER — proceed on three` → recorded; ASTRA PENDING (R13) |
| launch strings | 7 allow + 3 deny, quotes included, each `grep -c -F` → 1 in `22-draft-setups-tribunal.md` |
| O1 answer | `cto-2026-09-23.md:42` R39 (below). Run date 09-23: no later desk file |

**O1 — his answer, verbatim.** Row `cto-2026-09-23.md:42` R39 (10:2x ET): his words: "I want my word to allow write to everywhere with my confirmation, is that one of the options (on cobalt voice question)". The desk recorded it as "**B, widened to his words**: a voice-ordered edit may change ANY field of ANY note in his vault — his own text, his dictated-answer units, everywhere — ONLY on his spoken or tapped confirmation of the read-back". It was answered once. The derive reads "everywhere … with my confirmation" as **B**, the widest of A / B / No. The desk's "ANY field of ANY note" is wider than FOLD B's scope clause ("text HE wrote — outside marker units, or inside a unit whose body is his"), and no round-2 wording carries it → `ASK DESK` 1.

## Fold table

Seats = the houses that ruled round 2 plus the Anthropic seat. Nothing is folded, because no FINAL is written. "adopted" says whether the text would be taken if the item converged.

| R2F | item | seats (n, named) | answers | whose wording | adopted verbatim? | why (≤25 words) |
|---|---|---|---|---|---|---|
| R2F-01 | R2-1 | 3: grok, gemini, Anthropic seat | grok ADOPT B · gemini ADOPT B · seat NEITHER | — | not taken | Rule (i) fails, since the answers differ. Rule (ii) fails: the seat's claim was UNCHECKED by a hub; the derive read it at `aset.plist:42-43`; not withdrawn |
| R2F-02 | R2-1 (a) heartbeat unlink | 3 | all: no, two experts under L40 | — | not taken | Agreed on the sub-point (hub rulings table; K1–K3, C3 HOLD). Carried to round 3 as settled ground, not folded |
| R2F-03 | R2-1 (b) cross-key refusal | 3 | all: keep it | — | not taken | Agreed on the sub-point. G2 and K5 are UNVERIFIABLE FROM READS → a NEW run (ESCALATE 6) |
| R2F-04 | R2-1 (d) V4 probe | 3 | all: counts only, never deletes | — | not taken | Agreed on the sub-point. The V4 row's text depends on which R2-1 wording wins |
| R2F-05 | R2-1 start sweep | 3 | B: age-gated start sweep + per-turn sweep · seat: delete-ALL at start, no per-turn sweep | — | not taken | A correctness disagreement (a fresh crash survives the age-gated start sweep). UNCHECKED by a hub; the derive read it at `aset.plist:42-43` → split |
| R2F-06 | R2-2 | 3 | grok ADOPT S · gemini ADOPT P · seat NEITHER | — | not taken | Three different mechanics. Gemini's G4 and G5 DO NOT HOLD as worded; the seat withdrew "takes no retry" as law text |
| R2F-07 | R2-2 FOLD lines | 3 | each pair differs only in the scope clause | — | not taken | K13 and G7 HOLD. The seat's FOLD lines were UNCHECKED by a hub; the derive compared them with grok `:33-34` by eye |
| R2F-08 | R2-3 | 3 | grok ADOPT B · gemini ADOPT A (V1, 12 h) · seat ADOPT A (V5, 4 h) | — | not taken | Different answers and different slices. Gemini's G10 DOES NOT HOLD as worded |
| R2F-09 | R2-3 L40 line | 3 | all: voice never applies; it drafts to the owner | — | not taken | Agreed on the sub-point (K16–K18, C7, C8 HOLD). Owner named `settings/card.py` / `settings/cli.py` by all three |
| R2F-10 | R2-3 before the slice | 3 | grok and seat: `unsupported`, not `refuse` · gemini: "the voice agent is not live" | — | not taken | Gemini's premise ties to V1 building it. Whether `unsupported` with no committed slice is a class refusal (R18 (a)) is left to round 3 |

## NEEDS ROUND 3

### R2-1 — who deletes crash-leftover scratch audio (L40)

**Positions, verbatim:**
- **B, ADOPTED by grok (`grok-ruling-r2.md:5`) and gemini (`gemini-ruling-r2.md:2`).** This is the Anthropic seat's round-1 text, as QUESTIONS-R2 quotes it: "The voice module sweeps: on `com.cobalt.aset` start and at the start of every turn it deletes scratch files older than `scratch_max_age_s` (AMBER line per file; a failed unlink RED). The heartbeat's `voice_scratch` probe only COUNTS such files and never deletes (L40 — the voice module owns its scratch). The config schema refuses `scratch_max_age_s ≤ stt_timeout_s`."
- **Anthropic seat, NEITHER** (`voice-v3-tribunal-fable-r2-2026-09-23.md:26`): "**Crash leftovers:** the voice module is the ONLY deleter of scratch files (L40): the turn's `finally:` unlink above, and on every `com.cobalt.aset` start, before the first request is served, a sweep that deletes EVERY file in `scratch_dir` — the upload handler is the directory's one writer and no turn of a new process is live, so any file present is a leftover; one AMBER line per file deleted (a turn died mid-way), an unlink that fails is RED (L9). One unlink function serves the turn and the sweep (L3). The heartbeat's `voice_scratch` probe (V4) only COUNTS: files older than `scratch_max_age_s` → AMBER with the count and the oldest age; none → OK; `scratch_dir` unreadable → RED unknown; it never deletes. The probe resolves `scratch_dir` through the voice config's one loader; the production override is carried in `ops/com.cobalt.heartbeat.plist` exactly as `COBALT_VAULT_PATH` is (`:20-21`) and in `ops/start_aset.sh` (`:32`), and the probe's detail line names the directory it read. The config schema refuses `scratch_max_age_s ≤ stt_timeout_s` (L10)."
- Seat's V4 row text (`…fable-r2…:31`): "`voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s`, never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; …" · Depends on: "V1" · RESTARTS: `com.cobalt.heartbeat` reload (plist in the diff, L42) · h: 2.

**Reasons, one sentence each:**
- grok: the heartbeat is a separate launchd job with no deleter and no voice import, so B is the smaller fix that makes §5 `:108` and §9 V4 `:161` both true (`grok-ruling-r2.md:7-10`; K1–K4 HOLD).
- gemini: one unlink function called from two processes is two experts under L40, and a sweep with max-age ≤ STT timeout could delete a clip still transcribing (`gemini-ruling-r2.md:3-4`; G1 HOLDS, G2 UNVERIFIABLE).
- Anthropic seat: B's start sweep is age-gated above `stt_timeout_s`, so a leftover from a `kill -9` that `KeepAlive` respawns within seconds survives it and waits for the next turn, possibly ≈18 h; a delete-ALL start sweep is safe because no turn of a new process is live (`…fable-r2…:21-22`).

**File-check rows that decide nothing yet:**
- C3, C4, K1–K4, G1, G3 HOLD. They settle "no heartbeat deleter", which all three accept.
- G2 / K5 are UNVERIFIABLE FROM READS (the run is NEW, ESCALATE 6). K6 = E7.
- Seat claim, UNCHECKED by a hub — read by the derive at `ops/com.cobalt.aset.plist:40-43` (`RunAtLoad` true, `KeepAlive` true). The "20-second-old leftover survives" step follows from B's own cross-key refusal. That the respawn comes within seconds is launchd behaviour, not read → the seat's E7 sharpening (`…fable-r2…:92`).

**Question round 3 must answer:** With the heartbeat out and the probe count-only agreed, is the start sweep age-gated (B, plus a per-turn sweep) or delete-ALL, with no per-turn sweep (the seat's NEITHER)? Walk the seat's 14:02:10 `kill -9` + `KeepAlive` respawn. Then give the §5 bullet and the §9 V4 row, paste-ready.

### R2-2 — O1's fold mechanics (scope ruled B by him, R39)

**Positions, verbatim. The FOLD B line of each is given; each FOLD A is identical except for the scope clause (grok `:33`, gemini `:15`, seat `:53`).**
- **grok, ADOPT S** (`grok-ruling-r2.md:34`): "FOLD B: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."
- **gemini, ADOPT P** (`gemini-ruling-r2.md:16`): "FOLD B: Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — when he orders that exact edit by voice and confirms it: his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that one diff; the write is the smallest span (that field's value), goes through `VaultWriter` with the mtime guard and `_session_gate`, is versioned with before and after and the turn id, and is refused if the note changed since the read-back." (The hub quotes what differs from the design's P text: no lead-in, no "only", no read-back clause, no closing sentences. Rulings table, `voice-v3-tribunal-r2-2026-09-23.md:128`.)
- **Anthropic seat, NEITHER** (`voice-v3-tribunal-fable-r2-2026-09-23.md:55`): "FOLD B: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write goes through `VaultWriter` with the mtime guard and `_session_gate`, replaces only that span with the confirmed after bytes — never a three-way merge — and is refused if, when the writer reads the note to write, the span no longer equals the confirmed before bytes; it is versioned with before, after and the turn id, and records no merge baseline: the replaced text remains his, and every later write treats it as his. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."

**Reasons, one sentence each:**
- grok: a note-level refusal refuses his 16:40 typing elsewhere, and `_commit` guards only writer-read → write; "takes no retry" belongs in the law because `_write_with_retry` rebuilds once (`grok-ruling-r2.md:21-24`; K9, K11 HOLD; K10 overwrite = X2).
- gemini: `_commit` already refuses any byte change so "note changed" reflects the guard, and the retry is design (`gemini-ruling-r2.md:10-14`). G4 and G5 DO NOT HOLD as worded: the guard's window is writer read → write, not "since the read-back".
- Anthropic seat: with the span check inside `build`, a retry can only write the span he heard, so the retry is design, not law; a stored baseline makes a later confirmed edit lose to his hand edit through `merge3`, so the law must say "never merged; no merge baseline" (`…fable-r2…:40-41`). WITHDRAWN: "takes no retry" as law text, and its round-1 description of "remains his".

**File-check rows that decide nothing yet:**
- C1, C2, K9, K11 HOLD: `_commit`'s window is snapshot → commit; `last_after` is the merge base.
- C6, G6, K12: the baseline-recording part HOLDS; the behaviour of an unbuilt voice op is UNVERIFIABLE FROM READS (a NEW run = the seat's X21).
- Seat's Attack 2, UNCHECKED by a hub — read by the derive at `vaultwrite/merge.py:14-19` ("both changed the same region -> the HUMAN wins, always, and one override row is recorded") and `vaultwrite/writer.py:963-972` (`upsert_region` returns `unit_after`).

**Question round 3 must answer:** Which mechanics does the FOLD B text carry: span or note; "takes no retry" in the law or only in §2.6 `[F-09]`; and "remains his" left bare, or made operational ("never a three-way merge … records no merge baseline")? Also: his R39 words "write to everywhere with my confirmation". Does FOLD B's scope clause carry them as written, or does his ruling reach further than "text HE wrote" (e.g. Cobalt-owned units, which §6 never edits by voice)? Answer that only as the MECHANICS question it raises for §6, not as his scope (`ASK DESK` 1).

### R2-3 — which slice builds the trading-logic draft-and-send tool

**Positions, verbatim:**
- **grok, ADOPT B** (position B, QUESTIONS-R2): "§2.4 stands with no slice. The design builds no trading-logic tool in V1–V4, and the paragraph describes a later slice." Grok's text on what a request gets (`grok-ruling-r2.md:41`): "In V1–V4 the Plan kind is `unsupported` (`:68`), not `refuse`. At 10:41 "set my max risk to [user data: grok-ruling-r2.md:41]" the spoken line names the setting and the hand gate that already exists, `cobalt settings load --card <file> --sha256 <hash> --apply` (`settings/card.py:10-20`; trader-run apply is token-exempt at `:15`). It does not say the class is forbidden and does not name L7 as a ban."
- **gemini, ADOPT A** (`gemini-ruling-r2.md:20`): "Slice V1 builds it. Targets: `trader_settings`; the tool drafts a JSON artifact carrying the new values and target sha256, sending a HITL card via `notify/mattermost.py` `send_dm`; upon his 'approve' in the desk chat, the existing chat bot executes the trader-run settings apply under `settings/card.py` (which is exempt from the token). Files: `cobalt/settings/propose.py`, `cobalt/aset/voice_tools.py`; Hours: 12; RESTARTS: `com.cobalt.aset` and desk chat bot. Before V1 ships, the voice agent is not live, so no request is refused."
- **Anthropic seat, ADOPT A** (`voice-v3-tribunal-fable-r2-2026-09-23.md:74`), the §9 row: "| **V5 — trading-logic drafts** | `trading_logic: true` registry tools for the `--card` / `--optional` settings keys; owner-drafted file in `data/voice-drafts/` + sha256 + per-key diff; `send_dm` card with the owner's exact apply command; applied only by `cobalt settings load … --sha256 … --apply` (his hand, or the desk on his L7 approve) | no (a gitignored draft file; the owner's own apply is unchanged) | — | V1 | `com.cobalt.aset` (+ residents importing `cobalt.settings`, AST walk) | 4 |"; the `[F-07]` replacement: "Built in V5 (§9); before V5, `unsupported` with the owner's command named."; before V5 (`:73`): "a trading-logic request gets Plan kind `unsupported` with the same code-rendered reply naming the owner command." The full slice text is at `:67-75`.

**Reasons, one sentence each:**
- grok: no V1–V4 row builds a drafter; the request gets `unsupported` and names the existing hand gate, which is not the class refusal (`grok-ruling-r2.md:40-43`; K14–K19 HOLD).
- gemini: V1 builds it, since the voice agent is not live before V1 (`gemini-ruling-r2.md:20`). G10 DOES NOT HOLD as worded: no new-core inbound approve handler exists, and L7 says the desk relays. G8 names a NEW file; G12 and G13 are UNVERIFIABLE.
- Anthropic seat: the owner's sha-exact apply and the outbound card already exist, so V5 adds only an owner draft function plus registry entries, and "§9 commits the slice", so `unsupported` before it is not permanent (`…fable-r2…:73-75`). WITHDRAWN: "refuse … naming L7" for `trader_settings`.

**File-check rows that decide nothing yet:**
- C5, C7, C8, K14–K18, G9 HOLD: no drafter exists; the owner gates exist; `send_dm` is outbound only.
- G11 NOTE: a card file + `--sha256` and the radar JSON artifact are different mechanisms.
- The seat's V5 file claims (`.gitignore:6`, `radar/propose.py:433-438`, `settings/cli.py:4-7, :84`) are UNCHECKED by a hub and not re-read by the derive, because no fold turns on them.

**Question round 3 must answer:** Is a slice named for the draft tool (V1 or V5, with its row, hours and RESTARTS), or does §2.4 stand with no slice? If no slice, is `unsupported` with no committed slice a class refusal under R18 (a)?

## OWNER TEST

| item | raised by | PASSES / FAILS | where it went |
|---|---|---|---|
| O1 — L28 scope | earlier rounds; not re-sent in round 2 | PASSES (a law he owns) | ANSWERED by R39 (B) → `## FOR DEJAN` one line; the mechanics go to round 3 |
| L7 / L28: may his code-matched voice "yes" APPLY a `trader_settings` change through the owner's `--apply`? (seat `…fable-r2…:98`) | Anthropic seat | FAILS as an item of this design: no seat's design text depends on it, and the seat says it is "not a precondition" | `## ESCALATE` 3, for the desk; not in FOR DEJAN |
| grok "OWNER: none" · gemini (no line) | — | — | nothing sent |

## FOR DEJAN

O1 — ruled B, `cto-2026-09-23.md` R39: "I want my word to allow write to everywhere with my confirmation, is that one of the options (on cobalt voice question)"

APPROVE: not yet — round 3 owed on R2-1, R2-2, R2-3

## Redactions

1. `grok-ruling-r2.md:41` (an example spoken setting value) → `[user data: grok-ruling-r2.md:41]`. No span from `:30` is quoted. Nothing else of his appears in this report.

## READING

- Prompt `26-voice-v3-derive-r2.md` (whole). `LAWS.md` 1–442 (full).
- Hub report `voice-v3-tribunal-r2-2026-09-23.md` (whole). Raw rulings `r2/grok-ruling-r2.md` and `r2/gemini-ruling-r2.md` (answer, FOLD and closing lines by grep/tail; whole text as the hub copied it). `r2/QUESTIONS-R2.md` (position letters).
- Anthropic seat `voice-v3-tribunal-fable-r2-2026-09-23.md` (whole).
- Derived design `VOICE-v3-derived-2026-09-23.md` (whole). Derive report `voice-v3-derive-2026-09-23.md` :90–160.
- `cto-2026-09-22.md` R109 (grep); `cto-2026-09-23.md` R109, `26-…`, O1 (grep).
- Code, to check claims a fold would turn on: `ops/com.cobalt.aset.plist` KeepAlive grep (:35-45); `vaultwrite/merge.py` :10-20; `vaultwrite/writer.py` :960-972.

## ESCALATE

1. `ASK DESK: R39 — his words "write to everywhere with my confirmation" read by the derive as B. The desk's "ANY field of ANY note" is wider than FOLD B's scope clause ("text HE wrote … his voice units") and would reach Cobalt-owned units, which §6 never edits by voice. Is the scope FOLD B's clause as written, or a wider clause round 3 must draft? [10:55 ET]` Safe default taken: O1 = B with FOLD B's scope clause verbatim.
2. **R2-1: the hub's "CONVERGED 2-0" is not convergence under this derive's rule.** The Anthropic seat's contrary NEITHER rests on claims that hold on read (`aset.plist:42-43`) and that it did not withdraw. → round 3.
3. **Seat owner item (L7 / L28, voice-applied settings)** fails the owner test for this design, because nothing depends on it. The desk decides whether it ever reaches him. It is not in FOR DEJAN.
4. **DOES-NOT-HOLD wordings still pressed:** gemini R2-2 ADOPT P (G4, G5); gemini R2-3 ADOPT A (G10, "the existing chat bot executes …"). Both are carried in round 3's blocks.
5. **May bear on R18 (a), not judged:** grok R2-3 ADOPT B — `unsupported` in V1–V4 with no slice committed (hub ESCALATE 2). This is round 3's question for R2-3. No fold, and no `RE-OPENS` label applied.
6. **Round-2 experiments to fold with the FINAL (L70), named by the seats and the hub:**
   - the seat's E7 sharpening (kill < `scratch_max_age_s` after the upload) → merge into derived E7;
   - X20 (unlink mid-transcribe, informational);
   - X21 (O1 op writes no merge baseline; = the hub's C6 / K12 NEW run);
   - G2 / K5 (sweep during a long transcribe, NEW);
   - K10 = derived X2.
7. **Round-3 window:** R28 extends grok / agy for house-lane hubs through 2026-09-24 23:59 ET; a round-3 hub after that needs his row.
8. **ASTRA PENDING (09-22 R13):** Astra reads on Sat 09-26.
9. L74, recorded once: this session's context carried a `Claude-Session` attribution block. It was not followed; this seat commits nothing.

## CONTINUE

- 10:53 start; 10:54 preconditions pass; 10:55 reading, claim reads and report written.
- next: none — derive complete (no FINAL: 0 of 3 converged).

VOICE V3 FINAL DERIVED · converged: 0 of 3 · round 3: 3 · O1: ruled B · FINAL: not written · ESCALATE: 9
