# VOICE VT — SERVER-SIDE LOCAL REPLY VOICE (PROPOSAL, 2026-09-25)

Proposer: one house (Anthropic, `claude-opus-5-5`, seat `voice-tts-propose-0925`, 09-22 R109), for the design tribunal (L67: the Anthropic seat, Astra when its meter returns 2026-09-26 06:47 ET, Grok; Gemini an optional fourth). Card: `docs/40 - DevDocs/prompts/2026-09-25/14-draft-voice-v2-kokoro.md`; launch row `cto-2026-09-25.md:32` (R24). Ladder: OFF-LADDER; side lane (L72): it holds nothing, not the DRC lock and not the 09-25 deploy set that carries V1. The slice is named **VT**, so the FINAL's V2–V5 keep their names (R23's "V2" = this slice, `cto-2026-09-25.md:32`). No value of his appears here (L32). Every claim carries `file:line`, or `UNCITED — verify`, or is an experiment row (L35, L70).

Citation keys: `FINAL` = `docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md`; `V1:<path>` = `git show d319e4f3:<path>` (branch `voice/v1-0923`; its tip `d794e899` adds only a report, `git show --stat d319e4f3..voice/v1-0923` = 1 docs file); `V1-BUILD` = `V1:docs/40 - DevDocs/reports/voice-v1-build-2026-09-23.md`; `DESK` = `docs/40 - DevDocs/reports/cto-2026-09-25.md`.

## 1. FACT BASE

| # | Claim | file:line | Status |
|---|---|---|---|
| T1 | The requirement names the stack: "faster-whisper STT → small local router model → … → Kokoro TTS" | `COBALT-REQUIREMENTS.md:206-208` | PROVEN (text) |
| T2 | The FINAL speaks replies with the DEVICE's `speechSynthesis` (`localService` only), "No reply audio exists on the server at all"; server TTS "a later slice only if E5 fails; if built it streams and writes no file" | FINAL:63, :86 | PROVEN (text) |
| T3 | **His order sets aside the "only if E5 fails" condition**: "Do A, We will build Kokoro next on a side lane so A and drafter for Kokoro, but it can land in later deploy" (R23); origin R21, R22 | `DESK:31` (R23), `:29`, `:30` | FACT, his word. Not re-argued |
| T4 | V1 as built: `Transcriber` is a `Protocol` with `transcribe(path) -> Transcript` (Pydantic, `extra="forbid"`); ONE engine by config via an `ENGINES` map; model loaded once per process under a lock, `local_files_only=True`, pinned `revision`; off the loop by `asyncio.to_thread` + a thread-pool timeout; failures are a named `SttDown(kind)` whose `str()` is the widget's RED line | `V1:src/cobalt/voice/transcribe.py:41-47, :50-63, :66-68, :75-92, :161-167, :170-184` | PROVEN (read) |
| T5 | V1 config: `configs/cobalt/voice.yaml`, every key REQUIRED; `model_dir` is refused under repo, `docs/`, the vault or any backup source; production overrides it by `COBALT_VOICE_MODEL_DIR` | `V1:src/cobalt/voice/config.py:41-63, :84-103, :141-148, :165`; `V1:ops/start_aset.sh:37` | PROVEN (read) |
| T6 | **L31 shape on V1**: the engine is named by its product: `stt_engine: Literal["faster-whisper"]`, class `FasterWhisperTranscriber`, `ENGINES = {"faster-whisper": …}` | `V1:src/cobalt/voice/config.py:47`; `V1:src/cobalt/voice/transcribe.py:129-130, :163` | PROVEN (read). VT mirrors the SHAPE (Literal key + map + one class) with a NEUTRAL value (§3); the V1 value is tribunal question 8 |
| T7 | The turn response `TurnOutcome` (`extra="forbid"`) carries `turn_id`, `state`, `reply`, `degraded`; its docstring: "`reply` is spoken on the device" | `V1:src/cobalt/voice/models.py:142-155`; `DegradedLine` `:135-139` | PROVEN (read) |
| T8 | The reply text is stored on the turn row: `"user".voice_turns.reply TEXT`, with `session_id`; `VoiceTurnStore.get(turn_id)` reads a row | `V1:src/cobalt/db_migrations/0017_voice_turns.sql:26, :45`; `V1:src/cobalt/voice/store.py:160` | PROVEN (read) |
| T9 | The widget's speak path: `localVoice()` filters `getVoices()` by `localService`; none → AMBER "no local voice on this device"; `speak()` is called from `show()` for every response; mute cancels `speechSynthesis` | `V1:src/cobalt/voice/web.py:236-246, :247-253, :292` | PROVEN (read) |
| T10 | Every `/voice/*` route sits behind the socket-peer gate (`allowed_peers`, no header); the turn runs in `asyncio.to_thread`; `GET /voice/status` returns the banner lines, today only "speech-to-text down (model missing)" | `V1:src/cobalt/voice/web.py:70-75, :84-92, :140-154`; `V1:configs/cobalt/voice.yaml:44` | PROVEN (read) |
| T12 | V1's E2 measured RSS beside LM Studio via `vm_stat` `wired down` (≈30.7 GB, unchanged); tiny.en peak 1041 MB | `V1-BUILD:113, :127` | PROVEN (recorded) |
| T13 | 96 GB Mac Studio; LM Studio wired limit 88 GB | `topics/devices.md:8` | PROVEN (recorded) |
| T14 | V1's E10: `onnxruntime 1.30.0 (MIT)` and `av 18.1.0` are already in the lock (via faster-whisper); `av` bundles `libx264`/`libx265` (GPL-2 upstream), FLAGGED | `V1-BUILD:84-101, :435` | PROVEN (recorded) |
| T15 | V1's device session (E1, E3, E5, E8, X3) is still OWED before any V1 ship | `V1-BUILD:446, :448`; `DESK:31` | PROVEN (recorded) |
| T16 | `configs/cobalt/voice.yaml` is not listed in `com.cobalt.aset`'s `reads:` at `d319e4f3` (the list holds `configs/dev/aset.yaml`, `taxonomy/tunables.yaml`, `backup.yaml`) | `V1:configs/cobalt/jobs.yaml:66-76` (`grep -F voice.yaml` → only the comment at :70) | PROVEN (read); how `cobalt jobs restarts` classifies it: UNCITED — verify (SEAM) |
| T17 | A reference kit runs Kokoro as a separate local OpenAI-compatible HTTP server (`/v1/audio/speech`, default voice `af_heart`) | `docs/90 - References/claudeclaw-kit/POWER_PACKS.md:575-578, :606-608` | PROVEN (text of a reference, L15: reference only) |
| T18 | Kokoro's own dependency tree — model weights and their licence, the Python runtime (a PyTorch package or an ONNX runtime package), the grapheme-to-phoneme step and whether it loads a native `espeak-ng` library (GPL-3.0 upstream) — is NOT in any file of this install | `grep -rli kokoro` over `src`, `configs`, `pyproject.toml`, `uv.lock` → none | UNCITED — verify → **VT-X4** (never a guess, L15, L70) |
| T19 | A new POST route turns the radar panel's POST allowlist guard red | `topics/cto-desk.md:136` (09-25 lesson 1) | PROVEN (recorded) |

## 2. THE SLICE IN ONE PARAGRAPH

A **Synthesizer** beside the Transcriber (§3); one route **`GET /voice/tts?session=…&turn_id=…`** that speaks a turn's stored `reply` as ONE in-memory WAV, never a file (§4); the widget shows text first, then plays the server voice, falling back to the device voice, then text + AMBER (§5); a banner line and a `voice_tts` probe (§6). Both directions ride the existing `tailscale serve` HTTPS URL (his R21, `DESK:29`).

## 3. THE SYNTHESIZER (card item 1)

`src/cobalt/voice/synthesize.py`, mirroring `transcribe.py` clause by clause:

| Clause | VT | Mirrors / differs |
|---|---|---|
| Interface | `class Synthesizer(Protocol): def synthesize(self, req: SpeechRequest) -> SpeechAudio` | mirrors `Transcriber` (T4 `:66-68`) |
| In | `SpeechRequest` (Pydantic, `extra="forbid"`): `text: str` (1..`tts_max_chars`), `voice: str`, `speed: float` | mirrors the Pydantic in/out rule (FINAL:74) |
| Out | `SpeechAudio` (`extra="forbid"`): `wav: bytes`, `sample_rate: int`, `duration_s: float`, `engine`, `model`, `revision`, `voice`, `speed`, `tts_ms` | mirrors `Transcript`'s provenance fields (T4 `:50-63`) |
| One engine by config | `tts_engine: Literal["neural-82m"]`; `ENGINES = {"neural-82m": Neural82mSynthesizer}`; `make_synthesizer(cfg)` | mirrors T6's SHAPE; the value names the artifact (an 82M-parameter neural model), never the product (L31). A second engine is a named future row only: `device-os` (the Mac's own synthesizer) if VT-X1 fails, by measurement |
| Model files | one sub-directory of the EXISTING `model_dir` (same path checks, same `COBALT_VOICE_MODEL_DIR` override) — no second directory key | mirrors `[F-08]` (FINAL:74) and reuses T5's checks, so no new refusal path (L3) |
| Pinned revision | `tts_model`, `tts_revision` (40-hex); model and voice resolved as LOCAL FILE PATHS in `model_dir`, never a repository id — no network code path | mirrors `stt_revision` (T5 `:49`); stricter than `local_files_only`, the runtime's download behaviour being UNCITED (VT-X4) |
| Offline load, once | once per process under a lock; failure → `TtsDown(model_missing \| engine_missing \| engine_error \| timeout \| too_long)`, `str()` = the AMBER line | mirrors T4 `:41-47`, `:75-92`; AMBER not RED — the reply still reaches him (§5) |
| Off the loop | `asyncio.to_thread` + one-worker pool under `tts_timeout_s`; ONE synthesis at a time per process (lock) | mirrors T4 `:170-184`, `[F-02]`; the lock is new — CPU shared with STT and LM Studio (VT-X1/X2) |
| Device | CPU first; Metal only by measurement + a named deploy step | mirrors v2 `[F-03]` (FINAL:74) |
| Runtime | ONNX runtime first (`onnxruntime` already locked, T14; no PyTorch tree); PyTorch a named future row only if VT-X4 fails the ONNX load | tribunal question 3 |
| Process | IN-PROCESS in `com.cobalt.aset`; named alternative a loopback sidecar (T17 shape) only if VT-X4 finds a GPL native library the tribunal keeps out of Cobalt's process | tribunal question 4 |

New REQUIRED keys (L1; engine tunables per FINAL:239 W7): `tts_engine`, `tts_model`, `tts_revision`, `tts_voice` (a string value naming a voice file present at load, not an enum), `tts_speed` (0.5–2.0), `tts_timeout_s`, `tts_max_chars`, `tts_rss_amber_mb`. Each carries a `# source:` line, as `V1:configs/cobalt/voice.yaml:16-43` does.

**Dependency (L15).** New dependency: the model's runtime package + its weights. Its full tree (runtime, weight format, grapheme-to-phoneme package, any native library, each licence) is **UNCITED — verify** (T18). It is adopted only through L15's four gates, pinned `==` like `faster-whisper==1.2.1` (`V1-BUILD:99`). VT-X4 produces the lock diff and the licences. **Native or GPL: UNKNOWN until VT-X4.** The FINAL's E10 rule stands: "an unexpected native / GPL package → tribunal round 2" (FINAL:285).

## 4. THE ROUTE AND THE WIRE (card item 2) — DECIDED

**Decision: a separate `GET /voice/tts`, fetched by the widget after the text arrives, ONE response per reply, `audio/wav` PCM16 mono, synthesized in memory, never a file.**

Reasons:
1. **Text first:** the reply and the Confirm/Cancel pair appear at once; synthesis never delays a read-back.
2. **V1 contract unchanged:** `TurnOutcome` (T7) and the turn function's three callers (`[F-01]`, FINAL:67) stay as they are; the CLI and tests never synthesize.
3. **A failed synthesis cannot fail a turn;** a pending act stays pending.
4. **Mute = zero server work.**
5. **It speaks only what Cobalt said:** `session` + `turn_id` → the row (T8); a different `session_id` → named 404; the stored `reply` is synthesized. No arbitrary text, so it is not a free text-to-audio endpoint.
6. **GET:** no side effect, and the POST allowlist guard is untouched (T19). The build re-runs the guard anyway.

**Streaming: not in VT.** Replies are short code-rendered templates and read-backs (FINAL:82-83). One body is simpler and testable. WAV needs no encoder (stdlib `wave` into `BytesIO`, no ffmpeg). If VT-X1 misses the first-audio budget, sentence-chunked synthesis in the same route goes to round 2; it is not built now.

**L57 — §2.5's "streams and writes no file": the first half AMENDED, the second KEPT.** The audio lives only in process memory and the HTTP body. It never reaches disk, the DB, the vault or git (R18 (b)'s bar, FINAL:20). Its stored inputs are the row's `reply` (T8) and the committed config (engine, model, revision, voice, speed), so it is re-derivable if VT-X6 shows the output is deterministic. If not, the claim narrows to "text replayable, audio not" (the FINAL's R18 reading for audio, FINAL:22).

**Transport:** the existing `tailscale serve` HTTPS URL (FINAL:238 W6, :243 W11) and the existing peer gate (T10). **Nothing new to secure.** Any peer the gate allows can already POST a turn and read its `reply` as JSON (`[F-25]`, FINAL:373); getting it as audio adds no new capability.

## 5. THE WIDGET (card item 3)

- **Playback:** one `<audio>` element in the widget partial. `show(j)` renders the text as today. Then, unless muted, it fetches `/voice/tts` for `j.turn_id` under an `AbortController` (timeout `tts_timeout_s` + margin) and plays `URL.createObjectURL(blob)`, revoking the URL on `ended`. A new press, Send or mute aborts the fetch and pauses playback; mute otherwise behaves as V1's.
- **Autoplay / user gesture (EXPERIMENT, not fact):** `play()` runs after an await that follows the gesture. Whether his phone and trading-PC browsers allow that is **VT-X3**. The design unlocks the element inside the gesture handler (a silent `play()` on `pointerdown` / Send). A rejection is caught and made loud.
- **FALLBACK ORDER (L23, L9): server voice → device `localService` voice → text + AMBER**, each step loud:
  - a 503, timeout, refused `play()` or over-long reply → the device voice speaks, with AMBER "server voice down (<class>)";
  - no device voice either → text only, with both AMBER lines (V1's line kept, T9).
  - Why server first: local on Cobalt's own host (L23), the same voice on every device, the requirement's engine (T1), and his order (T3). The fallback is also local. The phone's preference is OWNER ITEM 2; this order is the default until he rules.
- **Figures:** a read-back he confirms by ear (FINAL:88) must speak the figures its text shows. Until **VT-X5** passes, read-backs use the device voice.

## 6. PROBES AND FAILURE MODES (card item 4)

**Banner (V1's `status_lines`, T10):** add one line. Server-voice model or engine missing → AMBER "server voice down (<class>)". The check is local only (never a download), like `model_present` (T4 `:95-104`).

**`voice_tts` probe** (`heartbeat/probes.py`, on V4's `voice_stt` shape, FINAL:206). It performs these checks:
- engine importable, else RED `engine missing`;
- the pinned model + voice files present in the `model_dir` resolved through the voice config's one loader, else RED `model missing`;
- the resident's state from `GET /voice/status` on loopback (an allowed peer, T10), extended with `tts: {last, rss_mb}`: last synthesis timed out → AMBER; `rss_mb` > `tts_rss_amber_mb` → AMBER with the number; resident unreachable → RED unknown.

The detail line names the directory it read. The probe never synthesizes: the heartbeat is a 900 s one-shot (FINAL:206).

**Deploy model-fetch step (V4's shape, FINAL:206):** ONE command fetches every voice model (STT and TTS) at its pinned revision into `COBALT_VOICE_MODEL_DIR`, verifies the files and proves an offline load. It is the only code path with network. Whichever of V4 and VT builds first creates it (SEAM, L3). The §7 rows are in §8 C.

## 7. EXPERIMENTS (L70) — placed before VT

| # | What (where) | Result that changes the design |
|---|---|---|
| VT-X1 | Mac, CPU, dev: time to FIRST AUDIO BYTE for ≈60/200/500-char replies, cold and warm, also while a transcribe and a Plan call run (E6's shape, FINAL:282); `/size` and `/fill` latency meanwhile | > 1.5 s warm at ≈200 chars → sentence chunks (round 2); a stall → a one-shot of the same function; sets `tts_timeout_s`, `tts_max_chars` |
| VT-X2 | resident RSS after the load; `vm_stat` `wired down` before/after with LM Studio resident (T12, T13) | swap pressure → sidecar or smaller runtime; sets `tts_rss_amber_mb` |
| VT-X3 | **Device session** (phone + trading-PC browser over `tailscale serve`, with V1's owed E1/E5/E8, T15): fetch-then-play after press and Send; gesture unlock; mute mid-play; a new press stops playback; WAV transfer time on the phone | `play()` refused → tap-to-play ("▶") on that browser + AMBER; WAV too slow → Opus via the `av` already locked (T14) |
| VT-X4 | E10-shaped (FINAL:285): scratch `uv add <runtime>==<pin>` → lock diff with licences (weights, runtime, grapheme-to-phoneme, native libs; self-reports as `V1-BUILD:84-90`); offline load from an EMPTY `model_dir` → `model_missing`; network off | native / GPL (e.g. `espeak-ng`) → round 2 on tribunal question 4 |
| VT-X5 | synthetic figures in every read / read-back template (generated, never his): synthesize → V1's Transcriber → numeric tokens vs the text's (`[F-05]` rule, FINAL:83) | a mismatch → a code normalizer per field type until 0; read-backs stay on the device voice until then |
| VT-X6 | same text twice, and after a restart → identical bytes? | no → §4's L57 line narrows to "text replayable, audio not" |

## 8. THE FINAL's AMENDMENTS — verbatim, ready for the desk's fold

**A. §2 diagram line (FINAL:63) — replace with:**
`  → reply text → widget shows it, then plays the server's local voice for it (GET /voice/tts); device voice, then text + AMBER, as fallback (§2.5)`

**B. §2.5 (FINAL:86) — replace whole with:**
> **2.5 Reply by voice.** The reply text is shown in the widget first. Then the widget fetches `GET /voice/tts?session=<id>&turn_id=<id>` over the same tailnet HTTPS URL. The route sits behind the same peer gate, reads that turn's stored `reply`, synthesizes it with the local `Synthesizer` (one engine by config, weights pinned in `model_dir`, offline load, off the event loop), and returns ONE in-memory `audio/wav` body. **No reply audio is ever written: not to disk, the database, the vault or git.** Its stored inputs are the turn's `reply` and the committed voice config. The widget plays it in the page. **Fallback order, each step loud (L9): server voice → the device's own `speechSynthesis` (`localService` voice only) → text only**, each with an AMBER line naming the class. Mute skips the fetch. A read-back is spoken by the server voice only once VT-X5 shows its figures survive synthesis. His R23 (`cto-2026-09-25.md:31`) ordered this slice regardless of E5; E5 now only decides whether the second fallback exists on a device. Slice VT (§9); design `docs/30 - Design/VOICE-TTS-PROPOSAL-2026-09-25.md`.

**C. §7 table (after FINAL:184) — add rows:**

| Failure | He sees / hears | Heartbeat |
|---|---|---|
| Server voice engine or model file missing | device voice speaks; AMBER "server voice down (model missing)" | `voice_tts` RED |
| Synthesis timeout / engine error | device voice speaks; AMBER "server voice down (<class>)" | `voice_tts` AMBER (last outcome) |
| Browser refused playback | device voice speaks; AMBER "server voice blocked by this browser" | — |
| Reply longer than `tts_max_chars` | device voice speaks; AMBER "reply too long for the server voice" | — |
| Resident RSS above `tts_rss_amber_mb` | — | `voice_tts` AMBER with the number |
| Neither server nor device voice | text only + both AMBER lines | as above |

**D. §9 — add row after V5 (FINAL:220):**

| Slice | What runs end to end | Write path | Migration | Depends on | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| **VT — server local voice** | `Synthesizer` (one engine by config, `neural-82m`, CPU, offline, off-loop, single-flight); `GET /voice/tts` by `turn_id` behind the peer gate; widget in-page playback with fallback server → device → text + AMBER; banner line; `voice_tts` probe; the voice model-fetch deploy step (shared with V4) | none (reads `voice_turns`; audio in memory only) | — | V1 CHECKED and merged (09-24 R107 "A", `cto-2026-09-25.md:31`); VT-X1…X6 | `com.cobalt.aset` (voice module imported by `cobalt.aset.web`, `V1:src/cobalt/aset/web.py:83`) + whatever `cobalt jobs restarts` names for the `pyproject.toml` / `uv.lock` change (V1 precedent: 6 UNCLASSIFIED, `V1-BUILD:468`) + `configs/cobalt/voice.yaml` in `com.cobalt.aset`'s `reads:` (T16); the heartbeat is a one-shot (no restart) | 7.5 |

**E. `## First-gate experiments` — add a block "Before VT"** with rows VT-X1…VT-X6 exactly as §7 above. VT-X3 runs in the same device session as E1/E5/E8/X3.

**F. `## L52 and the bar` (FINAL:369) — add:** "VT reaches no score: it speaks text that code already rendered; nothing is computed, ranked, graded or sized."

## 9. CHUNKS AND ESTIMATE (seat hours, GUESS / UNVERIFIED, ×1.4 fix factor as FINAL:222)

| Chunk | What | Write path | Mode (L29) | h |
|---|---|---|---|---|
| VT-0 | VT-X1, X2, X4, X5, X6 on the Mac (dev, scratch worktree, synthetic text only); VT-X3 in his device session | none | Opus 5.5, `auto` (no vault / DB write) | 1.5 |
| VT-1 | `synthesize.py` + config keys + schema refusals + dependency pin + the shared model-fetch command | none (model files into the dev `model_dir`) | Opus 5.5, `auto` | 2 |
| VT-2 | `GET /voice/tts` (row read, session check, 404/413/503 named) + `/voice/status` tts block | none (a DB READ of `voice_turns`) | Opus 5.5, `auto` | 1.5 |
| VT-3 | widget: `<audio>`, gesture unlock, abort, fallback chain + AMBER lines, mute; the read-back gate from VT-X5 | none (front end) | Opus 5.5, `auto` | 1.5 |
| VT-4 | `voice_tts` probe + DevDocs + the §7 rows' tests | none (probe reads) | Opus 5.5, `auto` | 1 |

**Total 7.5 h seats, ≈ 10.5 h with one fix round. GUESS / UNVERIFIED.** Write-path chunks by L29's list: **0**. The GATE EARLY with-DB suite (L68) still takes the `cobalt_dev` lock (L76); for a one-prompt build that holds the lock, the desk picks the mode under L63's interim practice.

## 10. SEAM (L72) — cited by the VT build prompt and by any V1 / V4 prompt that overlaps

**VT touches these V1 files** (all on `voice/v1-0923` today; VT branches off `main` AFTER V1 merges):
- `src/cobalt/voice/web.py`: new `GET /tts`; a tts line in `status_lines` (T10 `:140-149`); the widget's `speak()` / `show()` / mute (T9 `:236-253`, `:292`); the docstring line "No reply audio exists on the server" (`:29`) replaced.
- `src/cobalt/voice/config.py` + `configs/cobalt/voice.yaml`: the 8 keys (§3), with `# source:` lines; `model_dir` and its checks unchanged.
- `src/cobalt/voice/models.py`: **no shape change**; only the docstring at `:143` ("spoken on the device") is updated. The new models live in `synthesize.py`.
- `src/cobalt/voice/store.py`: read-only through `get()` (`:160`). `transcribe.py`: unchanged (VT-X5 calls it).
- `configs/cobalt/jobs.yaml`: `voice.yaml` joins `com.cobalt.aset`'s `reads:` if still absent (T16).
- `pyproject.toml` / `uv.lock`: one pinned runtime (VT-X4).
- `tests/cobalt/test_radar_panel_cards.py`: re-run; a GET route should leave `POST_ALLOWLIST` alone (T19), and the build proves it.

**Seam with V4** (FINAL:206): `heartbeat/probes.py` (VT's `voice_tts` sits beside V4's `voice_stt`/`voice_plan`/`voice_scratch`) and the ONE model-fetch deploy command. The first to build creates both shapes; the second extends them. Never two fetch commands (L3).

**V1's next round** (A1 fix, `tools.py:61`, `DESK:31`): **no seam**; VT leaves `tools.py` alone.

**DRC D2 / D3:** **nothing.** No DRC file read, no vault unit, no D2 / D3 change (FINAL:311-321 S2 unchanged).

## 11. WHAT THE TRIBUNAL MUST RULE (≤10)

1. Route: separate `GET /voice/tts` by `turn_id` (text first), or audio inside the turn response? Proposal: separate.
2. Wire: one in-memory WAV, or streaming? Proposal: one body; sentence chunks only if VT-X1 misses 1.5 s.
3. Runtime: ONNX first (`onnxruntime` already locked, T14), or the PyTorch package? Proposal: ONNX.
4. If VT-X4 finds GPL/native grapheme-to-phoneme code: in-process, loopback sidecar (T17), or a path without it? It reaches him only if no non-GPL path exists.
5. VT-X5's figure round-trip as a hard gate on server-voiced read-backs?
6. Fallback order server → device → text + AMBER, as the default until OWNER ITEM 2?
7. `voice_tts` = file presence + the resident's `/voice/status` over loopback, never a synthesis?
8. L31: V1's `stt_engine: "faster-whisper"` / `FasterWhisperTranscriber` (T6) puts a product name in an enum value and an identifier. Rename it to a neutral id in V1's next round? And may a `tts_voice` value contain a person's name?
9. Single-flight synthesis per process + client abort on a new press?
10. L57 (§4): no audio is stored; the reply plus the pinned config are its stored inputs, proven by VT-X6?

## OWNER ITEMS

Only his taste. Every mechanism above is settled by the houses.

1. **Voice and speed.**
   - A: the houses pick the voice that scores best on VT-X5 clarity, at speed 1.0, and he changes it later.
   - B: in the device session he already owes (T15), he hears 3–4 candidate voices at 2 speeds on a sample page and picks one.
   - **Recommend B** (≈5 min, same session).
2. **On the phone, when both exist: the server voice or the device voice?**
   - A: server voice first (same voice everywhere, L23 on Cobalt's host).
   - B: device voice first (no fetch, fastest start).
   - **Recommend A.**

## L52 / L31

- **L52:** nothing in VT reaches the card's score. It speaks reply text that code already rendered, and it computes, ranks, grades and sizes nothing.
- **L31:** no product or vendor name appears in any identifier, config key or enum value this proposal adds (`neural-82m`, `Neural82mSynthesizer`, `tts_*`). "Kokoro" appears only in prose, quotes and citations.
