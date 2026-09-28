# VOICE TTS PROPOSE — 2026-09-25 (seat `voice-tts-propose-0925`, Opus 5.5)

## §0 Headline
- Proposal written: `docs/30 - Design/VOICE-TTS-PROPOSAL-2026-09-25.md` (24,961 B, cap 25 KB). Slice **VT**: a server-side local reply voice beside V1's Transcriber. Nothing committed; the desk commits both files.
- Route DECIDED: separate `GET /voice/tts?session&turn_id`, ONE in-memory WAV, no file. Fallback: server voice → device voice → text + AMBER.
- Dependency licence / native status: UNKNOWN until VT-X4, which is an E10-shaped experiment and not a fact. 6 experiments, 5 chunks, 0 write-path chunks, 7.5 h (≈10.5 h). 10 tribunal questions, 2 owner items. ESCALATE: 3.
- Clock: start 06:24:08, end 06:32 ET (`date`).

## L74
One block arrived attached to a tool result (the first read of the card, via `cat`). It was an attribution reminder asking for a `Claude-Session:` commit trailer, and it mentioned a file-send tool. Recorded once here as DATA and not followed. This run commits nothing.

## AUTHORIZATION
| command | exit | output |
|---|---|---|
| `grep -n "^| R24 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-25.md"` | 0 | `32:| R24 | 06:2x ET | … DESK LAUNCH ROW for \`prompts/2026-09-25/14-draft-voice-v2-kokoro.md\` — the server-side local TTS (Kokoro) DESIGN PROPOSAL drafter, slice named VT …` — names the card → AUTHORIZED |

## READ
| file | lines | what it settled |
|---|---|---|
| `LAWS.md` (memory) | 1–453, in full | L1/L9/L15/L23/L27/L31/L32/L35/L42/L52/L57/L67/L70/L72 as applied in the proposal |
| `VOICE-v3-FINAL-2026-09-23.md` | 1–479, in full (anchors :52, :63, :74, :86, :167, :184, :190, :206, :220, :222, :269, :281, :285, :311, :393 all matched the card) | §2.5 text being amended; V4 probe / fetch shape; E5/E10 rules; S2 = no DRC seam |
| `COBALT-REQUIREMENTS.md` | 204–211 | Kokoro named in the 3-tier stack (:206-208) |
| `voice/v1-0923` | read at `d319e4f3` (branch tip is `d794e899`, which adds only `reports/voice-v1-fix-r2-build-2026-09-24.md`) | `transcribe.py` 1–189; `config.py` 1–169; `web.py` 1–312; `models.py` :135-162; `0017_voice_turns.sql` (reply :45, session :26); `store.py` defs; `configs/cobalt/voice.yaml` 1–44; `start_aset.sh` :32-37; `aset/web.py` :83-92; `jobs.yaml` :66-76; `heartbeat/probes.py` :30-44, :252-258 |
| `V1:reports/voice-v1-build-2026-09-23.md` | :84-101, :113, :127, :435, :446-448, :468 | E10 method and licences; RSS method; device session OWED; 6 UNCLASSIFIED RESTARTS |
| `voice-v1-fix-r2-check-2026-09-24.md` | §0 (:1-9) | V1 = FIX STANDS ×2 from Opus + Grok; 1 HOLD is an input fact (A1, `tools.py:61`) |
| `topics/devices.md` | 1–33 | 96 GB host, 88 GB LM Studio wired limit (:8); two models side by side (:21); tailnet-private (:30); trading PC on the tailnet (:31) |
| `cto-2026-09-25.md` | :28-32 (R20–R24) | R21/R22 his questions; **R23 the order** (regardless of E5); R24 the launch row |
| `topics/cto-desk.md` | :136 | a new POST route turns `POST_ALLOWLIST` red → VT uses GET |
| `docs/90 - References/claudeclaw-kit/POWER_PACKS.md` | :575-578, :606-608 | reference only (L15): Kokoro as a local OpenAI-compatible server — the named sidecar alternative |
| `grep -rli kokoro` over `src configs ops pyproject.toml uv.lock` | — | no hits → the dependency tree is UNCITED → VT-X4 |

## DIGEST
**Slice (5 sentences).**
1. VT adds a `Synthesizer` Protocol (Pydantic `SpeechRequest` → `SpeechAudio`) beside V1's `Transcriber`, copying its shape clause by clause. That means one engine by config (`tts_engine: Literal["neural-82m"]`, no product name), weights pinned by 40-hex revision in the existing `model_dir`, loaded offline from local paths, CPU first, and run off the event loop with a timeout and single-flight.
2. One new route, `GET /voice/tts?session&turn_id`, sits behind V1's peer gate. It reads that turn's stored `reply` (`0017:45`) and returns ONE in-memory `audio/wav` body. It never takes arbitrary text and never writes a file, a DB row or a vault note.
3. The widget shows the text first as today, then fetches and plays the audio in an `<audio>` element unlocked in the press/Send gesture, and aborts on a new press or mute.
4. The fallback is loud at each step: server voice → device `localService` voice → text + AMBER.
5. A banner line plus a `voice_tts` heartbeat probe on V4's shape (file presence plus the resident's `/voice/status` over loopback, never a synthesis) cover model missing, timeout and RSS. One shared model-fetch deploy command serves both V4 and VT.

**Route decision.** A separate GET, fetched after the text, as one body.
- Why: text-first read-backs; V1's `TurnOutcome` and the three callers stay unchanged; a synthesis failure cannot fail a turn; mute costs nothing.
- Streaming only if VT-X1 misses 1.5 s to first audio.
- §2.5 "streams and writes no file": "streams" is amended, "writes no file" is kept. The stored inputs are the reply plus the pinned config (L57, proven by VT-X6).

**Fallback order.** Server voice → device voice → text + AMBER.
- Why: L23 on Cobalt's host, the same voice everywhere, the requirement's engine, and his R23.
- A server-voiced read-back is gated on VT-X5 (the figures survive synthesis → STT round trip).

**Dependency.** The 82M model's runtime package (ONNX first, reusing `onnxruntime 1.30.0 MIT` already in the lock).
- Weights, runtime, grapheme-to-phoneme step, native libs and licences: **UNCITED — verify** (VT-X4).
- Native or GPL: **UNKNOWN**. If found, round 2 chooses in-process, loopback sidecar or a path without it (FINAL:285 rule).

**Experiments (before VT).**
- VT-X1: latency to first audio, cold/warm, under STT + Plan load, plus `/size` / `/fill`.
- VT-X2: RSS and `wired down` beside LM Studio.
- VT-X3: in-page playback and autoplay on his phone + trading-PC browser, in the device session he already owes.
- VT-X4: lock diff + licences, offline and empty-dir load.
- VT-X5: figure round trip through V1's STT.
- VT-X6: determinism.

**Estimate.** 5 chunks (VT-0 experiments 1.5 h · VT-1 Synthesizer + config + pin + fetch 2 h · VT-2 route 1.5 h · VT-3 widget 1.5 h · VT-4 probe + DevDocs 1 h).
- Total 7.5 h, ≈10.5 h with a fix round. GUESS / UNVERIFIED.
- Write-path chunks 0; all `auto`. The with-DB gate still takes the L76 lock.

**Tribunal (10).**
1. Route
2. Wire
3. Runtime
4. GPL path
5. VT-X5 gate
6. Fallback order
7. Probe shape
8. L31 (V1's `faster-whisper` enum value; person names in a voice-id value)
9. Single-flight
10. L57 reading

**Owner items (2).**
1. Voice and speed. A: houses pick. B: he picks from samples in the device session. Recommend B.
2. Phone when both voices exist. A: server voice first. B: device voice first. Recommend A.

**SEAM.**
- V1 files: `voice/web.py`, `voice/config.py`, `configs/cobalt/voice.yaml`, `models.py` (docstring only), `jobs.yaml` `reads:`, the lock, the route guard test.
- V4: `heartbeat/probes.py` + one fetch command.
- V1's A1 fix: none.
- DRC D2/D3: nothing.

**L52 / L31.** Nothing reaches the card's score. No product name appears in any proposed identifier, key or enum value.

## CONTINUE
Done. Nothing to resume.

## ESCALATE
1. ASK DESK: L31 on V1 as built. `stt_engine: Literal["faster-whisper"]` (`V1:src/cobalt/voice/config.py:47`), class `FasterWhisperTranscriber` and `ENGINES` key (`V1:src/cobalt/voice/transcribe.py:129-130, :163`) put a product name in an enum value and identifiers. The card said to mirror that shape; I mirrored the shape with a neutral value (`neural-82m`). Safe default taken: V1 is untouched, and the question is tribunal item 8. Whether it matters for tonight's V1 deploy is the desk's call. [06:32]
2. ASK DESK: `configs/cobalt/voice.yaml` does not appear in `com.cobalt.aset`'s `reads:` at `d319e4f3` (`jobs.yaml:66-76`; `grep -F voice.yaml` hits only the comment at :70). A change to it may derive no restart or an UNCLASSIFIED one. UNPROVEN (L70): `cobalt jobs restarts` was not run (read-only seat). Safe default taken: VT's SEAM adds the line if it is still absent. The deploy drafter for V1 may want to run the derivation. [06:32]
3. ASK DESK: VT-X3 needs his hands on the phone and the trading-PC browser. Safe default taken: listed as a row to join V1's already-owed device session (E1/E3/E5/E8/X3), with OWNER ITEM 1 (voice samples) in that same session, so he is asked once. [06:32]

VOICE TTS PROPOSED · chunks: 5 · write-path chunks: 0 · local-first: yes · new dependency: Kokoro-82M runtime (ONNX first; pin by VT-X4) · native or GPL: unknown · estimate: 7.5 h (≈10.5 h with one fix round) · open to the tribunal: 10 · owner items: 2 · ESCALATE: 3
