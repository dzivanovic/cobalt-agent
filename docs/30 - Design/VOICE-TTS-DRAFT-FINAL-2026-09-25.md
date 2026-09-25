# VOICE VT — SERVER-SIDE LOCAL REPLY VOICE (DRAFT FINAL — ASTRA PENDING (round 2 not before 2026-09-26 06:47 ET), 2026-09-25)

**DRAFT FINAL, derived by the round-1 derive.** Never named FINAL while Astra is unseated. Seat `voice-tts-derive-0925` (`claude-opus-5-5`, DERIVE ROW `cto-2026-09-22.md` R109 — "Make all Opus 5.5 for now"); tribunal launch row `cto-2026-09-25.md` R33 (`Fable seat: yes` · `derive seat: claude-opus-5-5`), derive launch row `cto-2026-09-25.md` R40. Fold table: `docs/40 - DevDocs/reports/voice-tts-derive-2026-09-25.md` `## Fold table` (rows `F-nn`).
**How to read it.** This is the proposal, whole, in its own order. A paragraph a round-1 ruling changed is REPLACED in place and tagged `[F-nn]` (its fold row). A point still open is tagged `[R2-n]`; its sides stand verbatim in `## OPEN TO ROUND 2` below. Everything untagged is the proposal's text unchanged. `[F-nn]` in this file always means THIS derive's fold row; a FINAL tag quoted inside a seat's wording or the proposal's text (`[F-01]`, `[F-08]`, `[F-25]`, `[F-26]` …) is the FINAL's or v2's own tag, as written there.
**Inputs:**
- Proposal `docs/30 - Design/VOICE-TTS-PROPOSAL-2026-09-25.md` (24,961 B, committed `a2fc3315`); author report `docs/40 - DevDocs/reports/voice-tts-propose-2026-09-25.md` (ESCALATE 1–3).
- His rulings, never re-opened: `cto-2026-09-25.md` **R23** ("Do A, We will build Kokoro next on a side lane so A and drafter for Kokoro, but it can land in later deploy" — the server voice is ORDERED; the FINAL §2.5 condition "only if E5 fails" is SET ASIDE; VT lands in a later deploy); desk records R21, R22 (his questions, not rulings), R25 (three desk readings); `cto-2026-09-24.md` R107 (V1 = A, closed by R23); `cto-2026-09-23.md` R95, R96, R97 (design seats; Gemini the optional fourth; each derive states whether a Gemini finding held); `cto-2026-09-22.md` R109 (the Anthropic seat and this derive on Opus 5.5).
- Round 1 (every seat that ruled): hub report `docs/40 - DevDocs/reports/voice-tts-tribunal-2026-09-25.md` (file-checks G1–G19, M1–M8, FC1–FC28); raw rulings `~/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/voice-tts/r1/grok-ruling.md` and `…/r1/gemini-ruling.md`; the Anthropic seat (Opus 5.5 per R109, `Fable seat: yes` per R33) `docs/40 - DevDocs/reports/voice-tts-tribunal-fable-r1-2026-09-25.md`.
- **Astra: `METER — ASTRA PENDING`.** Astra rules round 2 on THIS DRAFT FINAL (`16` §5: all 17 round-1 items and the derive report's `## NEEDS ROUND 2`), launched not before 2026-09-26 06:47 ET; the other seats rule only on `## NEEDS ROUND 2` and on any item where Astra's ruling disagrees on whether a mechanism is correct. The round-2 derive names the FINAL.

Proposer: one house (Anthropic, `claude-opus-5-5`, seat `voice-tts-propose-0925`, 09-22 R109), for the design tribunal (L67: the Anthropic seat, Astra when its meter returns 2026-09-26 06:47 ET, Grok; Gemini an optional fourth). Card: `docs/40 - DevDocs/prompts/2026-09-25/14-draft-voice-v2-kokoro.md`; launch row `cto-2026-09-25.md:32` (R24). Ladder: OFF-LADDER; side lane (L72): it holds nothing, not the DRC lock and not the 09-25 deploy set that carries V1. The slice is named **VT**, so the FINAL's V2–V5 keep their names (R23's "V2" = this slice, `cto-2026-09-25.md:32`). No value of his appears here (L32). Every claim carries `file:line`, or `UNCITED — verify`, or is an experiment row (L35, L70).

Citation keys: `FINAL` = `docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md`; `V1:<path>` = `git show d319e4f3:<path>` (branch `voice/v1-0923`; its tip `d794e899` adds only a report, `git show --stat d319e4f3..voice/v1-0923` = 1 docs file); `V1-BUILD` = `V1:docs/40 - DevDocs/reports/voice-v1-build-2026-09-23.md`; `DESK` = `docs/40 - DevDocs/reports/cto-2026-09-25.md`.

## 1. FACT BASE

| # | Claim | file:line | Status |
|---|---|---|---|
| T1 | The requirement names the stack: "faster-whisper STT → small local router model → … → Kokoro TTS" | `COBALT-REQUIREMENTS.md:206-208` | PROVEN (text) [F-03: unchanged — grok's challenge DOES NOT HOLD, hub G3] |
| T2 | The FINAL speaks replies with the DEVICE's `speechSynthesis` (`localService` only), "No reply audio exists on the server at all"; server TTS "a later slice only if E5 fails; if built it streams and writes no file" | FINAL:63, :86 | PROVEN (text) |
| T3 | **His order sets aside the "only if E5 fails" condition**: "Do A, We will build Kokoro next on a side lane so A and drafter for Kokoro, but it can land in later deploy" (R23); origin R21, R22 | `DESK:31` (R23), `:29`, `:30` | FACT, his word. Not re-argued |
| T4 | V1 as built: `Transcriber` is a `Protocol` with `transcribe(path) -> Transcript` (Pydantic, `extra="forbid"`); ONE engine by config via an `ENGINES` map; model loaded once per process under a lock, `local_files_only=True`, pinned `revision`; off the loop by `asyncio.to_thread` + a thread-pool timeout; failures are a named `SttDown(kind)` whose `str()` is the widget's RED line | `V1:src/cobalt/voice/transcribe.py:41-47, :50-63, :66-68, :75-92, :161-167, :170-184` | PROVEN (read) |
| T5 | V1 config: `configs/cobalt/voice.yaml`, every key REQUIRED; `model_dir` is refused under repo, `docs/`, the vault or any backup source; production overrides it by `COBALT_VOICE_MODEL_DIR` | `V1:src/cobalt/voice/config.py:41-63, :84-103, :141-148, :165`; `V1:ops/start_aset.sh:37` | PROVEN (read) |
| T6 | **L31 shape on V1**: the engine is named by its product: `stt_engine: Literal["faster-whisper"]`, class `FasterWhisperTranscriber`, `ENGINES = {"faster-whisper": …}` | `V1:src/cobalt/voice/config.py:47`; `V1:src/cobalt/voice/transcribe.py:129-130, :163` | PROVEN (read). VT mirrors the SHAPE (Literal key + map + one class) with a NEUTRAL value (§3); the V1 value is tribunal question 8 [F-57, F-18 below] |
| T7 | The turn response `TurnOutcome` (`extra="forbid"`) carries `turn_id`, `state`, `reply`, `degraded`; its docstring: "`reply` is spoken on the device" | `V1:src/cobalt/voice/models.py:142-155`; `DegradedLine` `:135-139` | PROVEN (read) |
| T8 | The reply text is stored on the turn row: `"user".voice_turns.reply TEXT`, with `session_id`; `VoiceTurnStore.get(turn_id)` reads a row | `V1:src/cobalt/db_migrations/0017_voice_turns.sql:26, :45`; `V1:src/cobalt/voice/store.py:160` | PROVEN (read) [F-07 below] |
| T9 | The widget's speak path: `localVoice()` filters `getVoices()` by `localService`; none → AMBER "no local voice on this device"; `speak()` is called from `show()` for every response; mute cancels `speechSynthesis` | `V1:src/cobalt/voice/web.py:236-246, :247-253, :292` | PROVEN (read) [F-04: unchanged — grok's challenge DOES NOT HOLD, hub G4] |
| T10 | Every `/voice/*` route sits behind the socket-peer gate (`allowed_peers`, no header); the turn runs in `asyncio.to_thread`; `GET /voice/status` returns the banner lines, today only "speech-to-text down (model missing)" | `V1:src/cobalt/voice/web.py:70-75, :84-92, :140-154`; `V1:configs/cobalt/voice.yaml:44` | [F-01 below — DOES NOT HOLD as written] |
| T12 | V1's E2 measured RSS beside LM Studio via `vm_stat` `wired down` (≈30.7 GB, unchanged); tiny.en peak 1041 MB | `V1-BUILD:113, :127` | PROVEN (recorded) |
| T13 | 96 GB Mac Studio; LM Studio wired limit 88 GB | `topics/devices.md:8` | PROVEN (recorded) |
| T14 | V1's E10: `onnxruntime 1.30.0 (MIT)` and `av 18.1.0` are already in the lock (via faster-whisper); `av` bundles `libx264`/`libx265` (GPL-2 upstream), FLAGGED | `V1-BUILD:84-101, :435` | PROVEN (recorded) |
| T15 | V1's device session (E1, E3, E5, E8, X3) is still OWED before any V1 ship | `V1-BUILD:446, :448`; `DESK:31` | PROVEN (recorded) |
| T16 | `configs/cobalt/voice.yaml` is not listed in `com.cobalt.aset`'s `reads:` at `d319e4f3` (the list holds `configs/dev/aset.yaml`, `taxonomy/tunables.yaml`, `backup.yaml`) | `V1:configs/cobalt/jobs.yaml:66-76` | [F-02 below — the `grep` wording and the UNCITED classification DO NOT HOLD] |
| T17 | A reference kit runs Kokoro as a separate local OpenAI-compatible HTTP server (`/v1/audio/speech`, default voice `af_heart`) | `docs/90 - References/claudeclaw-kit/POWER_PACKS.md:575-578, :606-608` | PROVEN (text of a reference, L15: reference only) |
| T18 | Kokoro's own dependency tree — model weights and their licence, the Python runtime (a PyTorch package or an ONNX runtime package), the grapheme-to-phoneme step and whether it loads a native `espeak-ng` library (GPL-3.0 upstream) — is NOT in any file of this install | `grep -rli kokoro` over `src`, `configs`, `pyproject.toml`, `uv.lock` → none | UNCITED — verify → **VT-X4** (never a guess, L15, L70) |
| T19 | A new POST route turns the radar panel's POST allowlist guard red | `topics/cto-desk.md:136` (09-25 lesson 1) | PROVEN (recorded) |
| T20 | [F-05] the Anthropic seat, verbatim: "The tap path returns a reply it never stores (`turn.py:258-274`; `confirm.py:66-118`) — Q1." | seat (a) MISSED (1) | HOLDS — hub FC1–FC6 |
| T21 | [F-05] the Anthropic seat, verbatim: "`tests/cobalt/test_jobs_restarts.py:180-194` and `:408-421` pin every function reaching `load_voice_config`; a new route handler joins them — (f)." | seat (a) MISSED (2) | HOLDS — hub FC14 (the set starts at `:164`) |
| T22 | [F-05] the Anthropic seat, verbatim: "The heartbeat plist carries no `COBALT_VOICE_MODEL_DIR` (grep `ops/` → only `start_aset.sh:37`) — Q7." | seat (a) MISSED (3) | HOLDS — hub FC9 |
| T23 | [F-05] the Anthropic seat, verbatim: "The widget voices synthetic responses that have no `turn_id` (`web.py:89`, `:259`, `:261`, `:282`) — Q6." | seat (a) MISSED (4) | HOLDS — hub FC15 |
| T24 | [F-05] the Anthropic seat, verbatim: "No server synthesis path exists today: `scratch.py:54`'s `audio/wav` is an upload content type (grep `synthes`, `speechSynthesis` → the widget only)." | seat (a) MISSED (5) | HOLDS — hub FC16 |
| T25 | [F-06] grok, verbatim: "`Probe.line()` has no AMBER (`22-v1-ops.excerpt.md`). The §7 AMBER heartbeat cannot be said with the class as built. Q7." | grok (a) §1 missed | HOLDS — hub G6 |
| T26 | [F-06] grok, verbatim: "`web.py:252` calls `speak()` on every response. That call is the existing speech path. VT must not leave it in place beside the new fetch. Q9. No other speech path is in the V1 tree." | grok (a) §1 missed | HOLDS — hub G8 |
| T27 | [F-06] grok, verbatim: "The reference kit's `/tmp` `say` path and cloud TTS (`24-reference.excerpt.md:13-24`) are not a Cobalt path. They are the path VT must not grow." | grok (a) §1 missed | HOLDS — hub G17 |

**[F-01] T10, status — grok, verbatim:** "DOES NOT HOLD as written. Peer gate, `to_thread`, and `GET /voice/status` hold (`web.py:71-76`, `:84-93`, `:141-155`; routes at `02-greps.txt:46-50`). "today only speech-to-text down (model missing)" does not. `status_lines` starts from `_SWEEP_LINES` (`web.py:144`) and startup appends reaper lines (`:180-183`). `voice.yaml:44` is `allowed_peers`, which the citation also covers." (Hub G1 / FC11 HOLD; line numbers are the staged excerpt's, ±1 of `web.py:140-149`, `:180-183`.)

**[F-02] T16, status — the Anthropic seat, verbatim:**
- "T16 DOES NOT HOLD as an experiment:
  - `grep -c -F -e voice.yaml jobs.yaml` = 0; line :70's comment names `voice/config.py`, not `voice.yaml`.
  - The derivation already ran on V1's range and named `configs/cobalt/voice.yaml` `UNCLASSIFIED CONFIG` (V1-BUILD:454). The gap is RECORDED, not UNPROVEN."

(Hub G2, FC12, FC13 HOLD. Hub G13: RECORDED for V1's range; the classification on the VT range is UNVERIFIABLE FROM READS → **VT-X9**, `## First-gate experiments`.)

**[F-07] T8, status — grok, verbatim:** "HOLDS. `0017:26` `session_id`, `:45` `reply` (nullable). `store.py:160` `get` by `turn_id` only, no session filter. The route must compare `session_id` (Q1)." (Hub G5 HOLDS.)

**[F-57] T6 and the L31 line — the Anthropic seat's WRONG FACT 3, verbatim:** "LAWS.md:182 reads "Person or vendor names never in code identifiers, schema, config keys, enum values or system design docs"." (Hub W8 HOLDS: the proposal read L31 as barring a "product name".)

## 2. THE SLICE IN ONE PARAGRAPH

A **Synthesizer** beside the Transcriber (§3); one route **`GET /voice/tts?session=…&turn_id=…`** that speaks a turn's stored `reply` as ONE in-memory WAV, never a file (§4); the widget shows text first, then plays the server voice, falling back to the device voice, then text + AMBER (§5); a banner line and a `voice_tts` probe (§6). Both directions ride the existing `tailscale serve` HTTPS URL (his R21, `DESK:29`). [F-55: unchanged — grok's WRONG FACT on "his R21" is not established, hub G9: the proposal cites his words, not a ruling.]

## 3. THE SYNTHESIZER (card item 1)

`src/cobalt/voice/synthesize.py`, mirroring `transcribe.py` clause by clause:

| Clause | VT | Mirrors / differs |
|---|---|---|
| Interface | `class Synthesizer(Protocol): def synthesize(self, req: SpeechRequest) -> SpeechAudio` | mirrors `Transcriber` (T4 `:66-68`) |
| In | `SpeechRequest` (Pydantic, `extra="forbid"`): `text: str` (1..`tts_max_chars`), `voice: str`, `speed: float` | mirrors the Pydantic in/out rule (FINAL:74) |
| Out | `SpeechAudio` (`extra="forbid"`): `wav: bytes`, `sample_rate: int`, `duration_s: float`, `engine`, `model`, `revision`, `voice`, `speed`, `tts_ms` | mirrors `Transcript`'s provenance fields (T4 `:50-63`) |
| One engine by config | `tts_engine: Literal["neural-82m"]`; `ENGINES = {"neural-82m": Neural82mSynthesizer}`; `make_synthesizer(cfg)` **[R2-3: the engine VALUE and class name are open]** | mirrors T6's SHAPE; the value names the artifact (an 82M-parameter neural model), never the product (L31). **[F-22] grok (b), verbatim, in place of the proposal's `device-os` future-row sentence:** "`device-os` on the server would be a second synthesizer next to the widget's `speechSynthesis`. It is not built." |
| Model files | one sub-directory of the EXISTING `model_dir` (same path checks, same `COBALT_VOICE_MODEL_DIR` override) — no second directory key | mirrors `[F-08]` (FINAL:74) and reuses T5's checks, so no new refusal path (L3) |
| Pinned revision | `tts_model`, `tts_revision` (40-hex); model and voice resolved as LOCAL FILE PATHS in `model_dir`, never a repository id — no network code path | mirrors `stt_revision` (T5 `:49`); stricter than `local_files_only`, the runtime's download behaviour being UNCITED (VT-X4) |
| Offline load, once | once per process under a lock; failure → `TtsDown(model_missing \| engine_missing \| engine_error \| timeout \| too_long)`, `str()` = the AMBER line | mirrors T4 `:41-47`, `:75-92`; AMBER not RED — the reply still reaches him (§5) |
| Off the loop | `asyncio.to_thread` + one-worker pool under `tts_timeout_s`; ONE synthesis at a time per process (lock) **[R2-4: the lock's mode is open]** | mirrors T4 `:170-184`, `[F-02]`; the lock is new — CPU shared with STT and LM Studio (VT-X1/X2) |
| Device | CPU first; Metal only by measurement + a named deploy step | mirrors v2 `[F-03]` (FINAL:74) |
| Runtime | **[F-10] grok (Q3), verbatim:** "ADOPT. ONNX first: `uv.lock` already names `onnxruntime` (`02-greps.txt:79-80`, pulled in by `faster-whisper`). PyTorch is added only if VT-X4 shows that locked runtime cannot load the pinned weights offline. The MIT line and `1.30.0` are the E10 record (`23-v1-build.excerpt.md:45`), not re-read from the lock here; VT-X4 re-reads them." | tribunal question 3 — ruled ADOPT 3-0 |
| Process | IN-PROCESS in `com.cobalt.aset`; named alternative a loopback sidecar (T17 shape) only if VT-X4 finds a GPL native library the tribunal keeps out of Cobalt's process **[R2-2: the order if VT-X4 finds one is open; binds only then]** | tribunal question 4 |

New REQUIRED keys (L1; engine tunables per FINAL:239 W7): `tts_engine`, `tts_model`, `tts_revision`, `tts_voice` (a string value naming a voice file present at load, not an enum) **[R2-3: what that value may be is open]**, `tts_speed` (bound: [F-10] below), `tts_timeout_s`, `tts_max_chars`, `tts_rss_amber_mb`. Each carries a `# source:` line, as `V1:configs/cobalt/voice.yaml:16-43` does. **[R2-1: grok's side adds a ninth, `tts_readback_server`.]** No tunable carries a number until its experiment sets it (`## First-gate experiments`).

**[F-10] `tts_speed`, grok (Q3), verbatim:** "`tts_speed`'s schema bound is the range VT-X4 records from the runtime, not 0.5–2.0. That interval is not in the staged files. The yaml value is the speed the passing VT-X5 run used. No new chunk: the pin stays in VT-1, and VT-1 may not merge a pin that differs from VT-X4's lock diff." (Hub W6 HOLDS.)

**Dependency (L15).** New dependency: the model's runtime package + its weights. Its full tree (runtime, weight format, grapheme-to-phoneme package, any native library, each licence) is **UNCITED — verify** (T18). It is adopted only through L15's four gates, pinned `==` like `faster-whisper==1.2.1` (`V1-BUILD:99`). VT-X4 produces the lock diff and the licences. **Native or GPL: UNKNOWN until VT-X4.** The FINAL's E10 rule stands: "an unexpected native / GPL package → tribunal round 2" (FINAL:285).

**[F-23] grok ((c)), verbatim:** "ADOPT WITH the four gates named as VT-1's merge bar. L15 (`27-laws-excerpt.md`): third-party code is reference only; a pattern is adoptable only when it is proven, conformant with our laws, industry-standard, and reviewed-clean. VT-X4 is that bar: lock diff, licence of weights, runtime, grapheme-to-phoneme, and native libs, offline load from an empty `model_dir` (`model_missing`), and load with the network off. VT-1 cannot merge without that diff. "ONNX first" is argued from the lock's existing `onnxruntime`, not from a Kokoro package (none is locked). It is not a claim the ONNX model file exists."

**[F-24] the Anthropic seat ((c)), verbatim:** "`onnxruntime` is today only a transitive dependency of faster-whisper (`uv.lock:1388-1395`; absent from `pyproject.toml` — grep, 0 hits). If VT imports it, it becomes a direct `==` pin." (Hub FC7, FC8 HOLD.)

## 4. THE ROUTE AND THE WIRE (card item 2) — DECIDED

**Decision: a separate `GET /voice/tts`, fetched by the widget after the text arrives, ONE response per reply, `audio/wav` PCM16 mono, synthesized in memory, never a file.**

Reasons:
1. **Text first:** the reply and the Confirm/Cancel pair appear at once; synthesis never delays a read-back.
2. **V1 contract unchanged:** `TurnOutcome` (T7) and the turn function's three callers (`[F-01]`, FINAL:67) stay as they are; the CLI and tests never synthesize.
3. **A failed synthesis cannot fail a turn;** a pending act stays pending.
4. **Mute = zero server work.** [F-53: grok's WRONG FACT — true only for a mute before the fetch is sent; hub W3: HOLDS as an inference from V1's pattern, UNVERIFIABLE FROM READS for VT → VT-X3 "mute mid-play" observes it.]
5. **It speaks only what Cobalt said:** `session` + `turn_id` → the row (T8); a different `session_id` → named 404; the stored `reply` is synthesized. No arbitrary text, so it is not a free text-to-audio endpoint.
6. **GET:** no side effect, and the POST allowlist guard is untouched (T19). The build re-runs the guard anyway.

**[F-08] Route rule — the Anthropic seat (Q1), verbatim:**
> **Route rule.** `GET /voice/tts?session=<id>&turn_id=<id>` sits behind `Depends(peer_gate)`. A missing row, or `row.session_id ≠ session` → 404 `no such turn in this session`. `row.pending_action IS NOT NULL` → 409 `device_voice`: the row is a read-back, or a pending action a tap has since resolved, and a tap never stores its own reply (`turn.py:258-274`, `confirm.py:66-118`). `row.reply` NULL or empty → 404 `no reply stored`. `len(reply) > tts_max_chars` → 413. Anything else → synthesize `row.reply`. The widget fetches only for a response with `r.ok` and a `turn_id`. A 409 `device_voice` is spoken by the device voice with no AMBER line. Every other non-200 is spoken by the device voice with AMBER `server voice down (<class>)`. Tests: tap Confirm, then GET → 409 · a spoken `yes` turn, then GET → 200 with that turn's own stored reply · another session's `turn_id` → 404.

(Hub FC1–FC6 HOLD. **[R2-1]** whether a reply that is NOT a read-back but carries a figure is also held to the device voice until VT-X5, and by what mechanism, is open.)

**[F-09] Streaming — grok (Q2), verbatim, in place of the proposal's streaming paragraph:** "One in-memory `audio/wav` (stdlib `wave` into a buffer, no file). No streaming in VT. No 1.5 s constant. Sentence chunks are a round-2 question only after the VT-X1 record exists, and only if that record says one body is too slow. That same record sets `tts_timeout_s` and `tts_max_chars`. Their `# source:` lines cite it." (Hub G7 HOLDS: the 1.5 s figure is not in the FINAL.)

**L57 — §2.5's "streams and writes no file": the first half AMENDED, the second KEPT.** The audio lives only in process memory and the HTTP body. It never reaches disk, the DB, the vault or git (R18 (b)'s bar, FINAL:20). Its stored inputs are the row's `reply` (T8) and the committed config (engine, model, revision, voice, speed), so it is re-derivable if VT-X6 shows the output is deterministic. If not, the claim narrows to "text replayable, audio not" (the FINAL's R18 reading for audio, FINAL:22). [F-20: kept — the Anthropic seat and gemini ADOPT; grok's Q10 wording not taken, its flag clause is R2-1; its `no-store` and object-URL clauses are carried by [F-25].]

**[F-25] Loud, and replayable — the Anthropic seat ((d)), verbatim:**
> - The route sets `Cache-Control: no-store` on every `/voice/tts` response.
> - The widget revokes the object URL on `ended`, `error` and abort.
> - `synthesize()` refuses an output with zero samples, or with all samples zero → `TtsDown(engine_error)`, detail `silent output` (AMBER; the device voice speaks).
> - Scope of the "no audio stored" claim: the design controls the memory it drops, the response body and its cache header. What `tailscale serve` and the browser do with a `no-store` body is VT-X3's to observe, never claimed.

(Hub FC28 / G19: the silent-output omission HOLDS; whether an engine ever emits silence is VT-X8. The cache behaviour is VT-X3 and VT-X7.)

**Transport:** the existing `tailscale serve` HTTPS URL (FINAL:238 W6, :243 W11) and the existing peer gate (T10). **Nothing new to secure.** Any peer the gate allows can already POST a turn and read its `reply` as JSON (`[F-25]`, FINAL:373); getting it as audio adds no new capability. [F-26: (e) boundary — NONE from all three seats, given the route rule [F-08].]

## 5. THE WIDGET (card item 3)

- **Playback:** one `<audio>` element in the widget partial. `show(j)` renders the text as today. Then, unless muted, it fetches `/voice/tts` for `j.turn_id` under an `AbortController` (timeout `tts_timeout_s` + margin) and plays `URL.createObjectURL(blob)`, revoking the URL on `ended`. A new press, Send or mute aborts the fetch and pauses playback; mute otherwise behaves as V1's. ([F-25] adds `error` and abort to the revoke.) **[R2-4: how a newer `show()` supersedes an older fetch is open.]**
- **Autoplay / user gesture (EXPERIMENT, not fact):** `play()` runs after an await that follows the gesture. Whether his phone and trading-PC browsers allow that is **VT-X3**. The design unlocks the element inside the gesture handler (a silent `play()` on `pointerdown` / Send). A rejection is caught and made loud.
- **FALLBACK ORDER (L23, L9): server voice → device `localService` voice → text + AMBER.** **[F-13] the Anthropic seat (Q6), verbatim, in place of the proposal's two step bullets:**
  > **Fallback — each hop loud (L9), except his own stop.**
  > 1. A response with no `turn_id` (`web.py:89`, `:259`, `:261`, `:282`), or a 409 `device_voice` → device voice; no server-voice line.
  > 2. 404, 413, 503, fetch timeout, or `play()` rejected before the first audio frame → device voice + AMBER `server voice down (<class>)`.
  > 3. No `localService` voice → text, with V1's AMBER `no local voice on this device` (`web.py:244`) beside the line from step 2.
  >
  > An abort the widget itself caused (a new press, Send, mute) is never a failure: no fallback, no AMBER. An `error` after playback began → AMBER `server voice stopped (<class>)`, and the device voice does not replay the reply. `show()` calls one `voiceReply(j)` INSTEAD of V1's `speak()` (`web.py:252`) — never both.

  (Hub FC15, FC17 HOLD; M3: the abort omission in the proposal HOLDS — gemini's, grok's and the seat's finding. **[R2-4]** the sentence on an `error` after playback began is contested by grok's Q9.)
  - Why server first: local on Cobalt's own host (L23), the same voice on every device, the requirement's engine (T1), and his order (T3). The fallback is also local. **[F-14] grok ((g) item 2), verbatim, in place of "The phone's preference is OWNER ITEM 2; this order is the default until he rules.":** "Item 2. Server voice first on the phone, by L23 and by Q6. VT-X3 can force tap-to-play where `play()` is refused. It does not ask him which voice is first."
- **One voice per reply. [F-21] the Anthropic seat ((b)), verbatim:** "One reply is voiced at most once: by the server voice, or — only if no audio frame has played — by the device voice. Never both, and never after a widget-caused abort (Q6)." (**[R2-4]** the clause "only if no audio frame has played" is the same contested point.)
- **Figures:** a read-back he confirms by ear (FINAL:88) must speak the figures its text shows. Until **VT-X5** passes, read-backs use the device voice. **[R2-1: the scope and mechanism of this gate are open; under [F-08] every `pending_action` row is 409 `device_voice`.]**

## 6. PROBES AND FAILURE MODES (card item 4)

**Banner (V1's `status_lines`, T10):** add one line. Server-voice model or engine missing → AMBER "server voice down (<class>)". The check is local only (never a download), like `model_present` (T4 `:95-104`).

**`voice_tts` probe. [F-15] the Anthropic seat (Q7), verbatim, in place of the proposal's probe bullets and its "detail line" sentence:**
> `voice_tts` reads ONLY the resident's `GET /voice/status` over loopback (an allowed peer, `voice.yaml:44`). The resident fills that route's `tts` block:
> - `present`: model and voice files in the RESIDENT's `model_dir`, a local lookup;
> - `model_dir`;
> - `last`: the last synthesis outcome class and its time;
> - `rss_peak_mb`: `resource.getrusage(RUSAGE_SELF).ru_maxrss`, E2's method (V1-BUILD:104) — the whole resident's peak.
>
> `present` false → RED `model missing (<dir>)`. `last` in {timeout, engine_error, busy, silent} → AMBER. `rss_peak_mb` > `tts_rss_amber_mb` → AMBER with the number. Unreachable or non-200 → RED unknown. The heartbeat process imports no engine and resolves no `model_dir`. It never synthesizes.

(Hub FC9, FC10, FC26 HOLD: the heartbeat plist sets no `COBALT_VOICE_MODEL_DIR`, so a file check in the heartbeat process would read the committed DEV `model_dir`. The `busy` class exists only under one side of **[R2-4]**.)

**[F-16] the probe's level — grok (Q7), verbatim:** "`Probe.line()` today prints only OK, `??`, or RED (`22-v1-ops.excerpt.md`, `probes.py:36-37`). VT-4 adds one level field on that class so AMBER is not stored as `ok=False`." (Hub G6 HOLDS; `V1:src/cobalt/heartbeat/probes.py:30-41`.)

The probe never synthesizes: the heartbeat is a 900 s one-shot (FINAL:206).

**Deploy model-fetch step (V4's shape, FINAL:206):** ONE command fetches every voice model (STT and TTS) at its pinned revision into `COBALT_VOICE_MODEL_DIR`, verifies the files and proves an offline load. It is the only code path with network. Whichever of V4 and VT builds first creates it (SEAM, L3). The §7 rows are in §8 C.
**[F-30] grok ((f)), verbatim:** "The fetch command's path is `ops/fetch-voice-models.sh`. Whichever of V4 and VT builds first creates it; the other calls it. It is the only network path. It writes weights and the neutral voice stems." (Hub G14 HOLDS: no fetch file exists under `ops/`. **[R2-3]** "the neutral voice stems" is grok's side of the voice-value question.)

## 7. EXPERIMENTS (L70) — placed before VT

Moved whole, as the rulings leave them, to `## First-gate experiments (L70)` below [F-40 … F-49].

## 8. THE FINAL's AMENDMENTS — verbatim, ready for the desk's fold

Moved whole, as the rulings leave them, to `## FINAL AMENDMENTS (for the desk's fold)` below [F-33 … F-39].

## 9. CHUNKS AND ESTIMATE (seat hours, GUESS / UNVERIFIED, ×1.4 fix factor as FINAL:222)

| Chunk | What | Write path | Mode (L29) | h |
|---|---|---|---|---|
| VT-0 | VT-X1, X2, X4, X5, X6 on the Mac (dev, scratch worktree, synthetic text only); VT-X3 in his device session | none | Opus 5.5, `auto` (no vault / DB write) | 1.5 |
| VT-1 | `synthesize.py` + config keys + schema refusals + dependency pin + the shared model-fetch command | none (model files into the dev `model_dir`) | Opus 5.5, `auto` | 2 |
| VT-2 | `GET /voice/tts` (row read, session check, 404/413/503 named) + `/voice/status` tts block | none (a DB READ of `voice_turns`) | Opus 5.5, `auto` | 1.5 |
| VT-3 | widget: `<audio>`, gesture unlock, abort, fallback chain + AMBER lines, mute; the read-back gate from VT-X5 | none (front end) | Opus 5.5, `auto` | 1.5 |
| VT-4 | `voice_tts` probe + DevDocs + the §7 rows' tests | none (probe reads) | Opus 5.5, `auto` | 1 |

**Total 7.5 h seats, ≈ 10.5 h with one fix round. GUESS / UNVERIFIED.** Write-path chunks by L29's list: **0**. The GATE EARLY with-DB suite (L68) still takes the `cobalt_dev` lock (L76); for a one-prompt build that holds the lock, the desk picks the mode under L63's interim practice.
[F-52] Chunks and hours unchanged: no seat priced a chunk change for what the fold takes (the Anthropic seat's Q1 price: "one `if` and three tests in VT-2, and one condition in VT-3"). The experiments the fold adds run where `## First-gate experiments` places them. The one priced alternative is **[R2-2]**'s sidecar (the Anthropic seat: "≈ +2 h, one more chunk, UNVERIFIED"), only if VT-X4 finds a native or GPL step. No chunk's BUILD depends on an owner item.

## 10. SEAM (L72) — cited by the VT build prompt and by any V1 / V4 prompt that overlaps

Moved whole, as the rulings leave it, to `## SEAM` below [F-27 … F-32].

## 11. WHAT THE TRIBUNAL MUST RULE (≤10)

The proposal's ten questions, as asked (round 1 ruled; the fold rows say where each landed):
1. Route: separate `GET /voice/tts` by `turn_id` (text first), or audio inside the turn response? Proposal: separate. → [F-08]
2. Wire: one in-memory WAV, or streaming? Proposal: one body; sentence chunks only if VT-X1 misses 1.5 s. → [F-09] (no 1.5 s line)
3. Runtime: ONNX first (`onnxruntime` already locked, T14), or the PyTorch package? Proposal: ONNX. → [F-10]
4. If VT-X4 finds GPL/native grapheme-to-phoneme code: in-process, loopback sidecar (T17), or a path without it? It reaches him only if no non-GPL path exists. → **[R2-2]**
5. VT-X5's figure round-trip as a hard gate on server-voiced read-backs? → **[R2-1]**
6. Fallback order server → device → text + AMBER, as the default until OWNER ITEM 2? → [F-13], [F-14]
7. `voice_tts` = file presence + the resident's `/voice/status` over loopback, never a synthesis? → [F-15], [F-16]
8. L31: V1's `stt_engine: "faster-whisper"` / `FasterWhisperTranscriber` (T6) puts a product name in an enum value and an identifier. Rename it to a neutral id in V1's next round? And may a `tts_voice` value contain a person's name? → V1 names: RECORDED for the V1 BACKLOG ticket, never a VT chunk [F-18]; the `tts_voice` value: **[R2-3]**
9. Single-flight synthesis per process + client abort on a new press? → **[R2-4]**
10. L57 (§4): no audio is stored; the reply plus the pinned config are its stored inputs, proven by VT-X6? → [F-20], [F-25]

## OPEN TO ROUND 2 (sides verbatim; the question round 2 must answer is in the derive report's `## NEEDS ROUND 2`)

**[R2-1] Q5 — the figure gate (with Q1's digit clause and amendment B's read-back sentence).**
- **Side A — grok (Q5), verbatim:** "VT-X5 is a hard gate on every server-voiced reply that contains a digit, not only on confirm read-backs. Required key `tts_readback_server` (bool, no code default). `# source:` is the VT-X5 record. The value is false until that record shows zero numeric mismatches on every read template and every read-back template. While false, Q1's 409 stands and the widget calls `speak()` once on that reply. The key is the ninth required voice key." · "§7 VT-X5 covers "every read / read-back template"; §5 and amendment B gate only "a read-back". At 10:50:00 he asks for a stop, the turn is `answered` (not `awaiting_confirm`), and the reply is "stop is 12.5". A read-back-only gate lets the server speak it before any round trip. One boolean in the route, enforced before VT-3's playback, is enough. No new chunk." · grok (Q1), the 409 it refers to: "While `tts_readback_server` is false, a `reply` that contains a digit is not synthesized: named 409 `voice: figures stay on the device voice`." (Grok's own whole-§2.5 replacement carries this side into amendment B; it stands in the raw ruling, `grok-ruling.md:179`.)
- **Side B — the Anthropic seat (Q5), verbatim:** "Read-backs — every row with `pending_action` set — are never spoken by the server voice in VT. Q1's 409 `device_voice` guard is the mechanism: unconditional, with its test. VT-X5 runs in VT-0 and is recorded. Lifting the guard for `awaiting_confirm` rows after VT-X5 shows 0 mismatches is a later change with its own check, never a config flag." · "Why. The proposal named no mechanism ("until VT-X5 passes, read-backs use the device voice", proposal:82). One guard settles both Q1 and Q5, at zero added size. A flag would be a switch on the path he confirms acts by ear (FINAL:88)." · its amendment-B sentence: "A read-back is never spoken by the server voice in VT (Q5)."
- **gemini (Q5), ADOPT the proposal, verbatim:** "Enforcing `VT-X5` as a hard gate ensures figures and numbers within read-backs are not hallucinated during the grapheme-to-phoneme step. Defaulting to the device voice until this accuracy is verified prevents the trader from confirming incorrect data by ear."
- Fact both sides meet (hub FC1–FC6): a tap never stores its own reply, so a tapped row still holds the read-back as `reply`; [F-08] 409s every such row.

**[R2-2] Q4 — a GPL or native grapheme-to-phoneme step, if VT-X4 finds one (binds VT-1 only then; FINAL:285's E10 rule already sends it to round 2).**
- **Side A — grok (Q4), verbatim:** "VT-X4 lists every licence. If an in-process load is non-GPL (the licence class VT-X4 records: MIT, BSD, Apache, or the same), it is in-process inside `com.cobalt.aset`. If the only in-process load needs GPL or a native grapheme-to-phoneme library, that library is not imported into `com.cobalt.aset`. The one alternative is a loopback sidecar on `127.0.0.1` only: no tailnet port, no cloud provider, and no file from the reference kit. He is asked only when that sidecar also has no non-GPL licence. In-process GPL is rejected, not offered." · "… A sidecar that exists only when the in-process path is unlawful is still one synthesizer, not two. Price: no extra chunk; the sidecar is a VT-X4 result, built inside VT-1 only if that result says so."
- **Side B — gemini (Q4), verbatim:** "`ADOPT WITH a loopback sidecar`. Loading a GPL or native grapheme-to-phoneme library in-process risks the stability and licensing of the main `com.cobalt.aset` application. A loopback sidecar securely isolates the dependency on the host while fulfilling the requirement without adding a cloud path."
- **Side C — the Anthropic seat (Q4), verbatim:** "If VT-X4 finds a native or GPL-licensed grapheme-to-phoneme step: 1. Round 2 first looks for a path without it: another grapheme-to-phoneme package that passes E10's shape (lock diff, licences, offline load) and keeps VT-X5's figures intact. 2. A loopback sidecar is priced before it is chosen: a new launchd resident, plist, `jobs.yaml` row, restart rule, probe and RSS line (≈ +2 h, one more chunk, UNVERIFIED). Whether a separate process changes the licence's reach is a legal claim no house settles from memory. 3. If neither path exists, ONE question reaches him: accept that licence in this private install, yes or no. It is his law, not a mechanism (L67)." · "Why. The proposal left the order open and the sidecar unpriced. Choosing it silently would add a resident (L42, L3)."

**[R2-3] Q8 — the `tts_voice` value and the engine value.**
- **Side A — grok (Q8), verbatim:** "`tts_*` keys are lawful. The engine value is `neural-local` and the one class is `NeuralSynthesizer`, unless VT-X4's own model card states a parameter count of 82 million, in which case the value may be `neural-82m`. The `# source:` line cites that card. `82m` is not a fact in this packet (T18). `tts_voice` is a neutral stem (`v01`, `v02`, …) chosen by the one fetch command. The value must not be a person's name or a vendor's name. The vendor's filename may remain a file inside `model_dir`; the yaml points at the stem. One `ENGINES` entry. No `device-os` engine." · "At 12:00 a yaml committed as `tts_voice: af_sarah` puts a person's name in system config. The neutral stem avoids that without a second naming scheme in code: the map is a file the fetch command writes beside the weights."
- **Side B — the Anthropic seat (Q8), verbatim:** "L31 (LAWS.md:182) bars PERSON or VENDOR names from identifiers, schema, config keys, enum values and system design docs. - `neural-82m`, `Neural82mSynthesizer` and `tts_*` are lawful. - `tts_voice`'s VALUE is the voice file's id exactly as the pinned model ships it. It is an artifact id (L31: "cite the artifact") and a free string — never an enum value, identifier, schema name or design-doc text. The design names it only as `tts_voice`."
- **Side C — gemini (Q8), verbatim:** "The proposed `neural-82m` identifiers strictly comply with L31 by excluding product names. … A `tts_voice` value may contain a person's name as it references an internal model profile, not a commercial vendor."
- Law text (hub M8): "Person or vendor names never in code identifiers, schema, config keys, enum values or system design docs". Fact (hub W6/W7 HOLD): the 82M count is in no staged file; VT-X4 records the model card.

**[R2-4] Q9 — the lock, and how the widget supersedes, aborts and recovers (with [F-13]'s `error`-after-playback sentence and [F-21]'s "only if no audio frame has played" clause).**
- **Side A — grok (Q9), verbatim:** "One process lock covers load and synthesize. The widget keeps a generation integer, bumped on pointer-down, Send, mute, and every `show()`. Each bump aborts the in-flight fetch and pauses the audio element. A completion whose generation is stale is discarded and does not call `speak()`. Abort, mute, and a stale generation are not failures: no device voice and no AMBER. A non-200, a timeout, a `play()` rejection, or an audio `error` on the current generation falls back once. `show()` does not call `speak()` unless that fallback fires or the route returned 409. Mute before the fetch sends nothing. Mute after the fetch has started does not kill the worker (V1's decode thread is the same: `transcribe.py:13-15`); the lock frees when the call returns or `tts_timeout_s` fires." · grok (d), its row: "`play()` or audio `error` | device voice + AMBER "server voice blocked by this browser"; heartbeat —".
- **Side B — the Anthropic seat (Q9), verbatim:** "One synthesis at a time per process, by a NON-BLOCKING acquire. A request that finds the lock held returns 503 `busy` at once; the widget uses the device voice + AMBER `server voice busy`. Nothing queues. A synthesis whose caller timed out keeps the lock until it ends — the thread cannot be killed, as in `transcribe.py:170-179`'s shape. `/voice/status` records `last` = `busy` or `timeout`." · its Q6 sentence: "An `error` after playback began → AMBER `server voice stopped (<class>)`, and the device voice does not replay the reply." · its experiment: "X8 NEW (Mac, dev ASET): three synthetic text turns 1 s apart while each synthesis runs. Count 503 `busy` per 100 replies at VT-X1's measured synthesis time → busy > 5 % → sentence-chunked synthesis goes to round 2, as the proposal's §4 foresaw." · its amendment-C row: "Server voice busy | device voice; AMBER `server voice busy` | `voice_tts` AMBER (last)".
- **gemini (Q9), ADOPT the proposal, verbatim:** "Implementing a single-flight lock ensures that synthesis does not monopolize CPU resources needed by STT and LM Studio. Client abort on a new press or mute properly cancels the fetch, eliminating wasted server load for interrupted responses."
- Facts (hub G15, FC19 HOLD): V1's decode thread cannot be killed; each V1 call builds its own one-worker pool. FC20 (aborted clients' syntheses queue behind a blocking lock) is UNVERIFIABLE FROM READS.

## First-gate experiments (L70)

Run before the chunk they gate, in dev (synthetic text only, never his), in a scratch worktree, or on his devices in the device session he already owes (V1's E1 / E3 / E5 / E8 / X3, T15). Each seat's change to a row is folded verbatim and attributed, never merged into another seat's. No tunable carries a number until its row sets it.

**Before VT-1** (VT-0: Mac, dev, scratch worktree)

| # | What (where) | Result that changes the design | Changes folded |
|---|---|---|---|
| VT-X4 | E10-shaped (FINAL:285): scratch `uv add <runtime>==<pin>` → lock diff with licences (weights, runtime, grapheme-to-phoneme, native libs; self-reports as `V1-BUILD:84-90`); offline load from an EMPTY `model_dir` → `model_missing`; network off | native / GPL (e.g. `espeak-ng`) → round 2 on tribunal question 4 (**[R2-2]**); VT-1 cannot merge without its diff ([F-23]) | [F-43] grok: "X4: KEEP. Scratch worktree, `uv add <runtime>==<pin>`, lock diff, licences of weights, runtime, grapheme-to-phoneme, native libs. Offline load from an empty `model_dir` → `model_missing`. Network off → still loads. Record the model card's parameter count, the voice-file stems, and the speed range the runtime accepts. GPL or native g2p → Q4's order, not an in-process import." · the Anthropic seat: "load plus one synthesis of synthetic text with the network OFF, and a file-write trace (`fs_usage` on the process); whether the runtime package accepts the locked `onnxruntime 1.30.0`. Result that changes the design: any network attempt or file write outside `model_dir` → round 2 (Q4 / (c)); a version conflict → round 2 on Q3." |
| VT-X8 | [F-47] (the Anthropic seat's X7) "X7 NEW (Mac, dev): synthesize synthetic replies that are digits-only, symbols-only, a single word and the empty-after-strip edge. Count outputs with zero or all-zero samples → sets whether (d)'s silent-output refusal ever fires; any hit → a text pre-check per field type in round 2." | as the row says; gates VT-1's `synthesize()` refusal ([F-25]) | new (hub G19: the emission is UNVERIFIABLE FROM READS) |
| VT-X1 | Mac, CPU, dev: time to FIRST AUDIO BYTE for ≈60/200/500-char replies, cold and warm, also while a transcribe and a Plan call run (E6's shape, FINAL:282); `/size` and `/fill` latency meanwhile | [F-40] per grok's change (right); sets `tts_timeout_s`, `tts_max_chars` | [F-40] grok: "X1: KEEP, change the trigger. Mac, dev, CPU, synthetic text only. Time to first audio byte for short, middle, and long replies (the proposal's ≈60 / ≈200 / ≈500 characters), cold and warm, while a transcribe and a Plan call run; `/size` and `/fill` meanwhile. Also record `duration_s`. Sets `tts_timeout_s` and `tts_max_chars`. A warm middle-length time the houses then call too slow, or `duration_s` of 0, goes to round 2 (chunks, or silence as `engine_error`). No 1.5 s line in the design." |
| VT-X2 | resident RSS after the load; `vm_stat` `wired down` before/after with LM Studio resident (T12, T13) | swap pressure → sidecar or smaller runtime; sets `tts_rss_amber_mb` | [F-41] the Anthropic seat: "VT-X2 KEEP. It also sets `tts_rss_amber_mb` against `ru_maxrss` as Q7 names it (the whole resident)." |
| VT-X5 | synthetic figures in every read / read-back template (generated, never his): synthesize → V1's Transcriber → numeric tokens vs the text's (`[F-05]` rule, FINAL:83) | a mismatch → a code normalizer per field type until 0; read-backs stay on the device voice until then | [F-44] kept; what the result unlocks is **[R2-1]** (grok's X5: "Zero → the key may be true"; the Anthropic seat's: "It does not lift Q5's guard inside VT") |
| VT-X6 | same text twice, and after a restart → identical bytes? | no → §4's L57 line narrows to "text replayable, audio not" | [F-45] kept (informational); grok's "the flag stays false" is **[R2-1]** |

**Before VT-2** (the route exists in the scratch tree)

| # | What (where) | Result that changes the design | Changes folded |
|---|---|---|---|
| VT-X7 | [F-46] (grok's X7) "X7: ADD, inside the X4 scratch tree, not a new chunk. One GET of a synthetic reply with `Cache-Control: no-store`, then change `tts_voice` and restart, then GET the same URL. A body that still matches the pre-change bytes means the header is not enough on that path; round 2 adds a cache-buster that does not land in the vault. This is the measurement Q10 does not pretend to have run." | as the row says | new (hub G18: UNVERIFIABLE FROM READS) |

**Before VT-3** (his device session — joins V1's owed E1 / E3 / E5 / E8 / X3; one session, asked once, R25 reading (3))

| # | What (where) | Result that changes the design | Changes folded |
|---|---|---|---|
| VT-X3 | **Device session** (phone + trading-PC browser over `tailscale serve`, with V1's owed E1/E5/E8, T15): fetch-then-play after press and Send; gesture unlock; mute mid-play; a new press stops playback; WAV transfer time on the phone | `play()` refused → tap-to-play ("▶") on that browser + AMBER; WAV too slow → [F-42] grok's result (right) | [F-42] grok: "X3: KEEP, drop "Opus via `av`". Phone and trading-PC browser over `tailscale serve`, in the owed device session, synthetic replies. Fetch-then-play after press and Send; gesture unlock; mute mid-play; a new press; two overlapping turns (only the later reply may be heard); a 409 digit reply speaks on the device once. `play()` refused → tap-to-play on that browser plus AMBER. WAV too slow → round 2 picks a smaller body whose encoder is already on VT-X4's licence list. Not `av`'s flagged `libx264`/`libx265` (those were accepted for decode-only, `23-v1-build.excerpt.md:19`)." (its "409 digit reply" check runs only if **[R2-1]** takes grok's side) · the Anthropic seat: "a `no-store` WAV is absent from the browser cache afterwards (inspect the browser's cache listing); a press mid-fetch voices nothing (Q6); a tap Confirm voices the device's "Done" line, not the read-back (Q1); `play()` after an awaited fetch following the gesture: allowed or refused. Result that changes the design: cached → the route or the proxy needs a further header (round 2); refused play → tap-to-play + AMBER as proposed." · gemini: "Ensure `AbortError` does not trigger device voice fallback." |

**Before VT-4 / the deploy drafter's derivation**

| # | What (where) | Result that changes the design | Changes folded |
|---|---|---|---|
| VT-X9 | [F-49] grok ((f) RESTARTS), verbatim: "Whether `cobalt jobs restarts` today prints nothing, UNCLASSIFIED, or `com.cobalt.aset` is an experiment: the command was not run (L70)." — scoped by hub G13: RECORDED for V1's range (`V1-BUILD:454`, `UNCLASSIFIED CONFIG`); run it on the VT branch's range in dev | hub G13's three outcomes: prints nothing / UNCLASSIFIED / `com.cobalt.aset`; L42: unclassified → ESCALATE, never dropped; the `reads:` line is added either way ([F-28]) | new (hub G13: UNVERIFIABLE FROM READS on the current tree) |

Held for round 2, not run until it rules: the Anthropic seat's X8 (busy rate) — **[R2-4]**.

## FINAL AMENDMENTS (for the desk's fold)

The desk's fold into `docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md`, AFTER round 2 names the FINAL — never this derive's. Each block is the proposal's §8 text verbatim, or replaced whole by a seat's verbatim wording, tagged with its fold row.

**A. §2 diagram line (FINAL:63) — replace with:** [F-33: proposal kept — grok and gemini: correct and minimal]
`  → reply text → widget shows it, then plays the server's local voice for it (GET /voice/tts); device voice, then text + AMBER, as fallback (§2.5)`

**B. §2.5 (FINAL:86) — replace whole with:** [F-34: proposal kept; its read-back sentence is **[R2-1]** — grok's whole replacement and the Anthropic seat's one-sentence change both carry a side of it; his R23 sentence kept]
> **2.5 Reply by voice.** The reply text is shown in the widget first. Then the widget fetches `GET /voice/tts?session=<id>&turn_id=<id>` over the same tailnet HTTPS URL. The route sits behind the same peer gate, reads that turn's stored `reply`, synthesizes it with the local `Synthesizer` (one engine by config, weights pinned in `model_dir`, offline load, off the event loop), and returns ONE in-memory `audio/wav` body. **No reply audio is ever written: not to disk, the database, the vault or git.** Its stored inputs are the turn's `reply` and the committed voice config. The widget plays it in the page. **Fallback order, each step loud (L9): server voice → the device's own `speechSynthesis` (`localService` voice only) → text only**, each with an AMBER line naming the class. Mute skips the fetch. A read-back is spoken by the server voice only once VT-X5 shows its figures survive synthesis. His R23 (`cto-2026-09-25.md:31`) ordered this slice regardless of E5; E5 now only decides whether the second fallback exists on a device. Slice VT (§9); design `docs/30 - Design/VOICE-TTS-PROPOSAL-2026-09-25.md`.

(At the round-2 derive, the design path names the FINAL VT file, and B takes whichever side of **[R2-1]** round 2 settles.)

**C. §7 table (after FINAL:184) — add rows:** [F-35: proposal's rows kept; the Anthropic seat's silence row and grok's line added verbatim; the seat's busy row is **[R2-4]**]

| Failure | He sees / hears | Heartbeat |
|---|---|---|
| Server voice engine or model file missing | device voice speaks; AMBER "server voice down (model missing)" | `voice_tts` RED |
| Synthesis timeout / engine error | device voice speaks; AMBER "server voice down (<class>)" | `voice_tts` AMBER (last outcome) |
| Browser refused playback | device voice speaks; AMBER "server voice blocked by this browser" | — |
| Reply longer than `tts_max_chars` | device voice speaks; AMBER "reply too long for the server voice" | — |
| Resident RSS above `tts_rss_amber_mb` | — | `voice_tts` AMBER with the number |
| Neither server nor device voice | text only + both AMBER lines | as above |
| Engine emitted silence | device voice; AMBER `server voice down (engine error)` | `voice_tts` AMBER (last) |

grok ((f)), verbatim: "C's rows include Q9's "stale or aborted fetch → silence, no device voice, heartbeat —"".

**D. §9 — add row after V5 (FINAL:220):** [F-36: proposal kept; its engine value `neural-82m` is **[R2-3]**; its "Depends on" gains the fold's VT-X7 … VT-X9 at the round-2 derive]

| Slice | What runs end to end | Write path | Migration | Depends on | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| **VT — server local voice** | `Synthesizer` (one engine by config, `neural-82m`, CPU, offline, off-loop, single-flight); `GET /voice/tts` by `turn_id` behind the peer gate; widget in-page playback with fallback server → device → text + AMBER; banner line; `voice_tts` probe; the voice model-fetch deploy step (shared with V4) | none (reads `voice_turns`; audio in memory only) | — | V1 CHECKED and merged (09-24 R107 "A", `cto-2026-09-25.md:31`); VT-X1…X6 | `com.cobalt.aset` (voice module imported by `cobalt.aset.web`, `V1:src/cobalt/aset/web.py:83`) + whatever `cobalt jobs restarts` names for the `pyproject.toml` / `uv.lock` change (V1 precedent: 6 UNCLASSIFIED, `V1-BUILD:468`) + `configs/cobalt/voice.yaml` in `com.cobalt.aset`'s `reads:` (T16); the heartbeat is a one-shot (no restart) | 7.5 |

**E. `## First-gate experiments` — add a block "Before VT"** with rows VT-X1…VT-X6 exactly as §7 above. VT-X3 runs in the same device session as E1/E5/E8/X3. [F-37: proposal kept; "§7 above" = this file's `## First-gate experiments`, VT-X1 … VT-X9 as the rulings leave them]

**E5 result cell (FINAL:281) — replace with:** [F-39: grok ((f)), verbatim — hub G10 HOLDS: the cell still says a failed E5 creates the server slice, which R23 set aside]
`none local → that device has no second hop (text + AMBER); the server voice is still first (R23)`

**F. `## L52 and the bar` (FINAL:369) — add:** [F-38: grok ((f)), verbatim, in place of the proposal's sentence — scoped so it cannot be read as retiring the FINAL's `[F-26]`]
"VT's synthesizer reaches no score: it speaks text the turn already rendered and computes, ranks, grades and sizes nothing. [F-26] is unchanged."

## SEAM

(L72 P-b.) The document the later VT build prompt cites, and any V1 / V4 prompt that overlaps. Lines cite `d319e4f3` (read at the V1 worktree `~/cobalt-wt/voice-v1`, tip `d794e899` = `d319e4f3` + one report). **VT branches off `main` AFTER V1 merges.** A line marked **UNSETTLED** is a reading, not a settled seam; the build prompt may not launch on it until round 2 or the desk settles it.

**VT touches these V1 files:**
- `src/cobalt/voice/web.py`: the new `GET /tts` beside `peer_gate` (`:70`); a tts line in `status_lines` (`:140`) and the `tts` block on `/voice/status` ([F-15]); the widget's `localVoice` (`:236`), `speak` (`:241`), `show` (`:247`) — `show()`'s `speak(j.reply, …)` (`:252`) is replaced by ONE `voiceReply(j)` ([F-13]); mute (`:292`); the docstring line "No reply audio exists on the server." (`:29`) replaced.
- `src/cobalt/voice/config.py` + `configs/cobalt/voice.yaml`: the `tts_*` keys (§3), with `# source:` lines (`voice.yaml:16-43` pattern); `model_dir` (`config.py:45`), `MODEL_ENV` (`:34`), the env loop (`:141`) and its check (`:165`) unchanged; `allowed_peers` (`voice.yaml:44`) unchanged. **UNSETTLED: eight keys, or nine with `tts_readback_server` — [R2-1].**
- `src/cobalt/voice/models.py`: **no shape change**; only the docstring at `:143` ("`reply` is spoken on the device") is updated. The new models live in `synthesize.py`.
- `src/cobalt/voice/store.py`: read-only through `get()` (`:160`; no session filter — the route compares `session_id`, [F-07], [F-08]). `transcribe.py`: unchanged (VT-X5 calls it).
- `configs/cobalt/jobs.yaml`: `com.cobalt.aset`'s `reads:` (`:67`; comment `:70`). [F-28] the Anthropic seat ((f)), verbatim: "`configs/cobalt/voice.yaml`'s absence from `com.cobalt.aset`'s `reads:` is RECORDED (V1-BUILD:454, `UNCLASSIFIED CONFIG`): a real gap, not an experiment. The `jobs.yaml` line stands." — **UNPROVEN on the VT range (L70) until VT-X9 runs `cobalt jobs restarts`** (hub G13). The deploy drafter's derivation of tonight's tree is R25 reading (2), not a VT hold.
- `pyproject.toml` (`:58`, `faster-whisper==1.2.1`) / `uv.lock` (`:1388-1395`, `onnxruntime` `:3280`): one pinned runtime (VT-X4; [F-10], [F-23]); a direct `onnxruntime` `==` pin if VT imports it ([F-24]).
- `tests/cobalt/test_radar_panel_cards.py`: `POST_ALLOWLIST` (`:667`), `GET_ONLY` (`:674`), the assert (`:685`) — re-run; a GET route should leave `POST_ALLOWLIST` alone (T19), and the build proves it.
- `tests/cobalt/test_jobs_restarts.py`: [F-27] the Anthropic seat ((f)), verbatim: "`tests/cobalt/test_jobs_restarts.py`: `EXPECTED_BACKUP_YAML_READERS` (:180-194) and the `entrypoints` set (:408-421) pin every function reaching `load_voice_config`. The new route handler, and any helper it calls that reaches `get_config`, joins both sets with a `# VT` comment. It is listed under VT-2, as `POST_ALLOWLIST` is (T19)." (At `d319e4f3` the set opens at `:164`, with `peer_gate` `:183` and `status_lines` `:189`; the entrypoints assert is `:408-421` — hub FC14.)
- Not touched: `src/cobalt/aset/web.py` (router include `:83`; grok (f): "No change there"); `tools.py`; `TurnOutcome`'s fields and the turn function's three callers.

**Seam with V4** (FINAL:206):
- `src/cobalt/heartbeat/probes.py`: VT's `voice_tts` sits beside V4's `voice_stt` / `voice_plan` / `voice_scratch`. `class Probe` (`:30`; `ok` `:34`, `unknown` `:38`, `line()` `:40-41`) gains ONE level field ([F-16], VT-4). **UNSETTLED: which of V4 and VT adds the level field if V4 builds first** — grok places it in VT-4 and says "V4's future AMBER scratch probe uses the same field"; no seat names the first-to-build rule for it (the FINAL's V4 row needs AMBER for `voice_scratch` too). The desk settles it in this section before either prompt launches (L72 P-b).
- The ONE model-fetch deploy command, `ops/fetch-voice-models.sh` ([F-30]; none exists under `ops/` today, hub G14). The first to build creates it; the second calls it. Never two fetch commands (L3). **UNSETTLED: what it writes for voices — "the neutral voice stems" (grok) or the files as shipped (the Anthropic seat) — [R2-3].**
- `ops/com.cobalt.heartbeat.plist`: [F-29] the Anthropic seat ((f)), verbatim: "`ops/com.cobalt.heartbeat.plist` needs no voice env under Q7. V4's `voice_stt`, if it resolves `model_dir` in the heartbeat process, needs `COBALT_VOICE_MODEL_DIR` there — a V4 seam line." (At `d319e4f3` the plist sets `COBALT_VAULT_PATH` `:20` and no `COBALT_VOICE_MODEL_DIR`; `ops/start_aset.sh:37` sets it for the resident only.)
- **UNSETTLED, only if [R2-2] chooses a sidecar:** a new resident — plist, `jobs.yaml` row, restart rule, probe and RSS line (the Anthropic seat's list).

**V1's next round** (A1 fix, `tools.py:61`, `DESK:31`): **no seam**; VT leaves `tools.py` alone. V1's `faster-whisper` names: a V1 BACKLOG ticket (R25 reading (1)), never a VT chunk ([F-18]).

**DRC D2 / D3:** **nothing.** No DRC file read, no vault unit, no D2 / D3 change (FINAL:311-321 S2 unchanged).

## Dissents, verbatim

None. No seat wrote `DO NOT BUILD`. The one `REJECT` of round 1 — grok's on item (g), "REJECT both owner items as items for him" — is FOLLOWED ([F-14], [F-50]), so it is not a dissent. Positions this DRAFT FINAL does not take are carried verbatim in `## OPEN TO ROUND 2`, and each not-taken wording is named in the fold table.

## The bar

- **L1 / L9 — every hop loud.** Every fallback hop names its class in an AMBER line ([F-13] steps 2–3, [F-25]'s `silent output`); a missing model or an unreachable resident is RED on the probe, a timeout / engine error / RSS over the line AMBER ([F-15]), and the `Probe` class gains a level so AMBER is not stored as RED ([F-16]). A widget-caused abort is silent by design and named as such ([F-13]); a 409 `device_voice` speaks on the device with no AMBER ([F-08]). Every new key is REQUIRED; a missing one crashes the load (§3). Open: the `busy` hop and the `error`-after-playback hop ([R2-4]).
- **L3 — one path.** One `Synthesizer`, one engine by config, and no `device-os` second engine ([F-22]); one route; one `model_dir` (a sub-directory, §3); one config loader (`load_voice_config`, and the heartbeat resolves none, [F-15]); one status route (`/voice/status` extended); one model-fetch command (`ops/fetch-voice-models.sh`, [F-30]); one reply voiced at most once, V1's `speak()` call replaced, never kept beside ([F-13], [F-21], T26).
- **L15 — the new dependency.** Adopted only through the four gates, VT-X4 being VT-1's merge bar ([F-23]); pinned `==`, `onnxruntime` direct if imported ([F-24]). Its licences and native status are EXPERIMENT rows until VT-X4 runs (L70) — UNKNOWN, never folded as fact. A native or GPL step → [R2-2].
- **L23 — local first.** Server voice (local, on Cobalt's host) → the device's `localService` voice → text; no cloud hop anywhere; the only network code path is the deploy-time fetch, and VT-X4 shows the runtime load does not use it ([F-23]; the fallback order is the houses', [F-14]).
- **L31 — names.** VT's identifiers and keys (`tts_*`, `Synthesizer`, `SpeechRequest`, `SpeechAudio`, `TtsDown`, `voice_tts`) carry no person or vendor name ([F-57]: the law bars "Person or vendor names"). The engine value and the `tts_voice` value are open ([R2-3]). V1's `faster-whisper` identifiers are the V1 BACKLOG ticket's (R25 reading (1)) — recorded, never a VT chunk ([F-18]).
- **L52.** VT reaches no score ([F-38]); the FINAL's `[F-26]` path is unchanged.
- **L57.** The stored inputs are the row's `reply` and the committed voice config; VT-X6 is informational and narrows the claim to "text replayable, audio not" if the bytes differ ([F-20]); the claim covers what the design controls — memory, the body, its `no-store` header ([F-25]); the browser and proxy are observed by VT-X3 / VT-X7, never claimed.
- **L28 / L32 / boundary.** VT writes nothing to the vault, no row, no file (§4, [F-25]). No value of his is here; every experiment uses synthetic text. Nothing in VT reads, writes or infers from his trading platform; the phone and the trading PC are browser tabs that play a WAV (hub item (e): NONE from all three seats).

## OWNER ITEMS

**None reaches him.** The proposal's two items, as the rulings leave them:
1. **Voice and speed** (the proposal: "Recommend B" — he picks from samples in the device session). [F-50] grok ((g) item 1), verbatim: "Item 1. `tts_voice` is the neutral stem that wins VT-X5's clarity count. `tts_speed` is the speed that run used. He can change the yaml later; that edit is not this tribunal's approval and not a precondition of VT-1. The device session he already owes (T15) may play samples. It is not a gate." (Its "neutral stem" is grok's side of **[R2-3]**.) Held against: the Anthropic seat — item 1 "PASSES: it is his taste in what he hears, and no house can hear for him. It is NOT a precondition."; gemini — "Voice and speed: taste in what he hears."
2. **On the phone, server voice or device voice first** (the proposal: "Recommend A" — server first). [F-14] grok ((g) item 2), as in §5. The Anthropic seat: "OWNER ITEM 2 FAILS: server-first is settled by his own order (R23, `cto-2026-09-25.md:31`) and by measurement." Held against: gemini — "Phone fallback priority when both exist: taste in latency vs voice consistency."

Both leave `## FOR DEJAN` because a seat ruled each NOT his and settled by measurement (grok: VT-X5's clarity count; L23 and Q6), under L67 as amended 2026-09-24. No chunk's build depends on either. A third item — the Anthropic seat's "Q4 (3) only if reached: accepting a GPL licence in this private install — his law." — is conditional on a VT-X4 result that does not exist; it is not a decision now and rides **[R2-2]**.

What reaches him, after round 2: ONE approval — "approve the VT FINAL?".

## L52 / L31

- **L52:** nothing in VT reaches the card's score. It speaks reply text that code already rendered, and it computes, ranks, grades and sizes nothing. ([F-38]: the FINAL amendment F is grok's wording.)
- **L31:** no product or vendor name appears in any identifier, config key or enum value this proposal adds (`neural-82m`, `Neural82mSynthesizer`, `tts_*`). "Kokoro" appears only in prose, quotes and citations. [F-57: the law bars person or vendor names, `LAWS.md:182`; the engine value is **[R2-3]**.]
