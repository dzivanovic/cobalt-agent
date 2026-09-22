# DRC PER-TRADE VOICE CAPTURE — PROPOSAL (2026-09-22)

Proposer: one house (Anthropic, `claude-opus-5-5`, seat `drc-voice-propose-0922`), for the four-house tribunal (L67). Origin: `cto-2026-09-22.md` §4 R100 (17:5x ET), his words "A, B as soon as possible." — no voice in the DRC build slice (A); a per-trade VOICE CAPTURE designed now as its own item, parallel lane (L72). It attaches to `docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md` (cited `v2 §n` / `v2:line`) as ruled by R90–R103. Content source: his coach's spec `docs/_inflight/DRC-automation-spec-2026-09-22.md` (gitignored, L32) — cited `SPEC §n`, keys only, no value of his. Nothing here reaches scoring, ranking, grading or sizing (§9). Vendor / project names appear only as the dependency being proposed, never in an identifier (L31).

## 1. FACT BASE

| # | Claim | file:line | Status |
|---|---|---|---|
| V1 | No voice / STT / TTS code: grep `whisper\|voice\|speech\|transcri` over `src configs ops dev_utils pyproject.toml` hits only unrelated words | grep, this run (`cards/models.py:240`, `ops/pg_role.py:15`, `generate_constitution.py:291` a TODO) | PROVEN (whole-tree read, L35) |
| V2 | The "3-tier local voice stack" is a REQUIREMENT, not an install: faster-whisper STT → small local router → tiers → Kokoro TTS | `docs/00 - Project/COBALT-REQUIREMENTS.md:206-208` | PROVEN (text) |
| V3 | The assessment rated the voice docs ASPIRATIONAL — "none built" | `docs/20 - Assessment/08-documentation-audit.md:82` | PROVEN |
| V4 | CLAUDE.md "Environment facts" lists the voice stack as an interface beside Mattermost and the vault | `CLAUDE.md` Environment facts, "Interfaces:" bullet | PROVEN (text) — contradicts V1/V3 → ESCALATE 1 |
| V5 | The Charter named local-Whisper-class plugins a "DRC dictation candidate" and the engines research only | `MVP-CHARTER-v0_2.md:412-413` | PROVEN (text) |
| V6 | There is NO inbound DM path: `notify/mattermost.py` is outbound HTTP only | `src/cobalt/notify/mattermost.py:6-11`; `S3-EXITS-v3-2026-09-22.md:65` (F27) | PROVEN |
| V7 | The one web surface is the ASET app; it serves a mobile viewport | `aset/web.py:83`, `:384` | PROVEN |
| V8 | The ASET page has NO authentication; dev binds loopback, the local override binds `lan`, both files carry the warning | `configs/dev/aset.yaml:36-41`; `configs/dev/aset.local.yaml:25-28` | PROVEN · which file production loads = v2 E7 (UNPROVEN) |
| V9 | The DRC v2 import path adds a BYTES method on `VaultWriter` (the text `_commit` cannot write bytes) and puts files under the imports dir; R92 moved that dir to `1 - Trading/5 - Review/_imports/drc/<date>/` | v2:70 `[F-06]`; `vaultwrite/writer.py:457`, `:470`; `cto-2026-09-22.md` §4 R92 | PROVEN (design text + code) — the bytes method is NOT BUILT (D2) |
| V10 | His per-trade answer lines sit in their own unit `drc-trades/voice-<trade_id>` next to that trade's Cobalt block, created blank ONCE and never upserted again | v2:139 `[F-21]` (T6); `cto-2026-09-22.md` §4 R99 | PROVEN (ruled) |
| V11 | The DRC note is created only when both inputs are placed on a trading day with trades, and on every market trading day otherwise | `cto-2026-09-22.md` §4 R66 (b), R93 | PROVEN (ruled) |
| V12 | Rule adherence stays the DRC coach session's judgement over the whole day; no rule→checker map this build | `cto-2026-09-22.md` §4 R101 | PROVEN (ruled) |
| V13 | SPEC per-trade voice fields: setup name, catalyst, read + flip, entry self-tag, exit structure, re-entry what's-new, stop-move structure, mistakes/lesson; stored VERBATIM beside parsed fields; nothing inferred about state | SPEC §1.2 "Per trade", §9 | PROVEN (text, keys only) |
| V14 | The diff model rules those as HIS rows: B3, B9, B10, B11, B12, B15, B16, B17 (structure), B18 | v2:311-326 (R71) | PROVEN (ruled) |
| V15 | Host: M3 Ultra, 96 GB unified; LM Studio wired limit 88 GB; the local LLM is Qwen3.8-27B 8-bit, not a speech model; no STT model in `~/.lmstudio/models` | `topics/devices.md:8`, `:12`, `:17`; `ls ~/.lmstudio/models` this run | PROVEN |
| V16 | No `ffmpeg`, `whisper*` or `sox` in `/opt/homebrew/bin` | `ls /opt/homebrew/bin` this run | PROVEN (that dir only — not a whole-host claim, L35) |
| V17 | The lock carries `huggingface-hub`, `tokenizers`; not `ctranslate2`, `av`, `onnxruntime`, either engine | `uv.lock:1983`, `:5310` | PROVEN |
| V18 | Phone = Android on the tailnet; the trading PC JOINED the tailnet 2026-09-20 by his word | `topics/devices.md:11`, `:31` | PROVEN — contradicts v2 F17 ("not on the tailnet", `SPRINT-LADDER-v0_1.md:610`) → ESCALATE 2 |
| V19 | Browser microphone capture (`getUserMedia` / `MediaRecorder`) needs a secure context (HTTPS or `localhost`); a plain `http://<host>:5010` page on the phone gets no microphone | UNCITED — verify (V-E1) | UNPROVEN |
| V20 | `<input type="file" accept="audio/*" capture>` is not gated by the secure context and hands off to the phone's recorder | UNCITED — verify (V-E1) | UNPROVEN |
| V21 | faster-whisper runs on CPU on Apple Silicon (CTranslate2, no Metal) and decodes webm/opus/m4a through PyAV without a system ffmpeg; mlx-whisper runs on Metal but loads audio through a system ffmpeg | UNCITED — verify (V-E2, V-E3) | UNPROVEN |

## 2. WHAT HE SAYS

Per trade, free speech, one clip or several per trade; nothing forced. What the clip is FOR (SPEC §1.2 per trade = v2 B-rows ruled HIS): setup name if not on the card, catalyst, read at entry + flip, entry self-tag, exit structure, re-entry "what's new", the structure a stop moved to, mistake / lesson. A spoken correction to an auto value lands verbatim and changes no number (A28 and R90's resolve action stay the only correction paths).

Out of scope (R100 says per-trade): the per-day block and the next-day review grade (SPEC §1.2) — W5; the same path takes them later with a new binding key.

## 3. WHERE AND WHEN

Two capture points, one mechanism, both bind by a key the page already holds — no speech is ever used to decide WHICH trade it is about.

| Point | Device | When | Binds by |
|---|---|---|---|
| C-card: a record control on each FILLED / CLOSED card in the ASET panel | phone (tailnet) or desk (trading PC browser, LAN / tailnet; the Mac) | DURING the day, right after an exit, while it is fresh | `card_id` (the card row, `aset_sizings`) |
| C-drc: a record control on each trade row of the `/drc` page (v2 §2) | same | AT the DRC, after the import lists the trades | trade key from the parsed export |

A C-card capture made before the DRC exists is held (§5) and lands when the build matches that card to its trade (v2 §4 card match). A card that matches no trade keeps its capture in `drc_voice`; the DRC lists it under A31 `voice not bound: card <id>` — never dropped, never guessed onto a trade.

Microphone path (V19, V20 — UNPROVEN until V-E1): (a) serve the ASET page over HTTPS on the tailnet only (e.g. `tailscale serve`, UNCITED — verify), then the page records in-browser; (b) fallback with no exposure change: the file input hands off to the phone's recorder and uploads the file over the existing page. Which one is W6 (his — (a) is a new exposure of an unauthenticated page, V8). The trading PC gets NO install and NO agent: it is a browser tab, as the ASET panel already is (CLAUDE.md boundary unchanged). Whether that PC has a microphone: not known → V-E1 row.

## 4. HOW IT LANDS — his unit, never his text rewritten (L28)

His answer unit `drc-trades/voice-<trade_id>` is created blank once and never upserted (V10). The transcript must reach it without ever changing a byte he wrote. Proposed (T-V1 is the tribunal's):

1. **At unit creation** (the DRC build, v2 D3): if bound captures exist for the trade, the unit is created with them as its INITIAL body — one block per capture, oldest first, each `> 🎙 <HH:MM ET> · capture <id>` then the transcript verbatim. Still create-once; nothing he wrote exists yet.
2. **After the unit exists** (a capture made at the DRC or later): a NEW `VaultWriter` operation `append_to_unit(unit_id, block)` — reads the unit body under the mtime guard, asserts the new body = old body + one separator + the block (a byte-prefix check, deterministic, no LLM, L28), commits atomically, versions the write row (`vault_writes`) with `unit_before` / `unit_after`. It never edits, reorders or removes a line; if the prefix check fails (a concurrent edit), it refuses loudly and the capture stays `transcribed, not landed` with a retry. One writer for the unit's Cobalt appends (L40); the build's create-once is unchanged.
3. **He edits freely** below or around the blocks; the transcript block is his text the moment it lands — Cobalt never touches that block again (no "correct the transcript" rewrite). A re-transcribe (§6) lands a NEW block labelled `re-transcribed capture <id>`, never replaces the old one.

Alternative (T-V1): a Cobalt-owned sibling unit `drc-trades/voice-transcript-<trade_id>` he copies from — no new writer op, but double work and a split record; the proposer recommends the append.

A vanished trade (re-import drops it): the unit keeps its `orphaned` line (v2 E8); its captures stay in `drc_voice` with the old trade key and show in A31.

## 5. TRANSCRIPTION — local first (L23), loud degradation (L9, L1)

- **Interface.** `Transcriber` (Pydantic in/out: audio path + sha256 + params → `Transcript{text, segments[start,end,text], engine_id, model_id, model_revision, params, duration_s, elapsed_s}`), one implementation per engine, engine chosen by config (`configs/cobalt/voice.yaml`, Pydantic schema + dry-run `cobalt drc voice transcribe --dry-run <file>`, L10). Swap = new collector + config (L9).
- **Named local engine: faster-whisper** (the requirement's own choice, V2), a pinned model (candidate sizes small / medium / large-v3-turbo — V-E2 picks by his real clips: word accuracy on his speech + tickers, latency, memory). Runs on the Mac Studio only. Why this one first: pip-only (uv-lockable, no Homebrew or binary on the host), and decodes phone formats without a system ffmpeg (V21, UNPROVEN → V-E3). Comparators in V-E2: mlx-whisper and whisper.cpp (Metal speed) — each needs a system ffmpeg or a built binary (V16, V21), a host change the tribunal weighs (T-V3). Assignment by measurement, not by house or preference (L26).
- **Model files.** Fetched ONCE at deploy by a named step into a configured dir, pinned by revision; runtime opens them `local_files_only` — no network at transcribe time; a missing model = FAILED naming the path (L1).
- **Vocabulary bias.** Initial prompt = the day's card tickers + his exit-structure list (config) — a decoding hint stored in `params` (L57).
- **Fallback (L25 as amended 09-09).** Primary down (crash / timeout / model missing) → the capture row goes `failed: stt <class>`, the AUDIO IS KEPT, the page shows red `transcript pending — local speech-to-text down (<class>)`, the heartbeat carries a degraded probe (L9; `heartbeat/probes.py` is the existing home), and `cobalt drc voice transcribe --id <n>` or the page's retry re-runs the SAME function (one path, L3). He can always type into his unit (the DRC never waits on voice). No cloud STT: his voice leaving the host is W4, his. A second LOCAL engine as a fallback is T-V4 (proposer: no — one engine, loud pending, retry; a second engine doubles the dependency for a rare case).
- **Where it runs.** Proposed: in the upload request, synchronously, with a clip-length and time limit from config (engine tunables, L53 — not his ceilings), returning `transcribed` or `failed`; the capture row's state is `pending → running → done | failed` (L18), a dead request leaves `failed` (the v2 T2 shape, `[F-08]`). The alternative (T-V2) is a one-shot job per capture. Memory: the model loads inside `com.cobalt.aset` — V-E5 measures the resident's footprint beside LM Studio's 88 GB wired limit (V15).

## 6. WHAT IS STORED — replayable (L57)

| What | Where | Why |
|---|---|---|
| The audio file, as uploaded (no re-encode) | the imports dir R92 named: `1 - Trading/5 - Review/_imports/drc/<date>/voice/<capture_id>.<ext>`, written by the D2 bytes method (V9), refused inside `market_reset` like every vault write (`writer.py:387`) | the source; a transcript is a derived value — without the audio it is not replayable. Home + retention = W2, W3 |
| One row per capture: `"user".drc_voice` — id, date, `card_id` or trade key, audio path + sha256 + bytes + duration, state, `Transcript` fields (text, segments JSON, engine_id, model_id, model_revision, params), landed unit id + `vault_writes` id, `supersedes` (re-transcribe) | Postgres, user side (L32 tenancy), created by the V1 migration (number: the desk's at L68) | the record the note's block is a copy of; re-transcribing with the same audio + model revision + params reproduces it (V-E2 checks determinism) |
| The landed block | his unit, verbatim | his text from then on |

Nothing is summarised, classified or mapped to B-row fields in this item: verbatim only (SPEC §9; V12 — the coach session reads it). Mapping speech to B15/B16/B17 fields (deterministic cue words, or the local model in shadow) is a later slice — T-V7.

## 7. CHUNKS AND ESTIMATE

Order: V-E1…V-E5 (hub-run experiments, no build) → V1 → V2 (after v2 D2 is merged: needs the bytes method and `/drc`) → V3 (after v2 D3: needs the voice unit) → V4. V1 and V-E* run now, beside the DRC build (L72); V2/V3 ride the DRC's deploy or the next one (L43). Seats: Opus 5 floor on every write-path chunk, never auto mode on a write path (L29); each build checked by ≥3 tribunal members (L67 as amended R46). Hours are seat hours; ≈ × 1.4 with one fix round each (factor UNVERIFIED, as in v2 §9).

| Chunk | Files | Write path | Migration | New dependency | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| V1 store + transcriber | new `src/cobalt/voice/{models.py,transcriber.py,local_engine.py,store.py}`; `configs/cobalt/voice.yaml` + schema; `cobalt drc voice transcribe [--dry-run] [--id]` in `cli.py`; migration + `.rollback.sql` for `"user".drc_voice`; `placement.py` entry; tests on HIS real clips' shape (L45 — V-E2's clips, stripped of content he names) | DB — yes | YES — one | faster-whisper (+ its transitive `ctranslate2`, `av`, `onnxruntime`) | none (library) | 5 |
| V2 capture routes | `aset/web.py`: `POST /voice` (card) + the `/drc` trade-row control; recorder markup (in-browser + file-input fallback); audio bytes via the D2 bytes method; transcribe call; status text | vault imports + DB — yes | — | — | `com.cobalt.aset` | 6 |
| V3 landing | `drc/build.py` (create-once body from bound captures); new `VaultWriter.append_to_unit` + tests (prefix check, mtime race, versioned row); A31 `voice not bound` / orphan lines; smoke row (`s2.yaml`) | vault — yes | — | — | `com.cobalt.aset` | 6 |
| V4 ops | heartbeat degraded probe; model-fetch deploy step + `ops/README.md`; DevDocs | no (probe reads) | — | — | derived | 2 |

**Total: 4 chunks, 3 write-path, 19 h seats (5+6+6+2), ≈ 27 h with one fix round each (UNVERIFIED); experiments ≈ 2 h hub time.**

Experiments (L70 — each before the chunk it gates; dev vault / `cobalt_dev` / clips he hands over):

| # | Before | What | Result that changes the design |
|---|---|---|---|
| V-E1 | V2, W6 | phone + trading-PC browser: `MediaRecorder` on the plain-http page (expect none), on a tailnet-HTTPS page, and the file-input recorder hand-off; does the trading PC have a mic | decides W6's options and the recorder markup; no mic at the desk → desk capture = the Mac or phone |
| V-E2 | V1 | 5–10 real clips from him (his voice, tickers, structure words): each candidate engine × model size — word accuracy against his own corrected text, latency, RSS, same-output-twice | picks the engine + model (T-V3); non-deterministic output → `params` pin tightened or replay claim narrowed |
| V-E3 | V1 | decode the phone's actual formats (webm/opus, m4a) with the chosen engine, no system ffmpeg | fail → ffmpeg becomes a named host dependency (tribunal) |
| V-E4 | V3 | `append_to_unit` on the dev vault: his edits above/below, a concurrent edit mid-append, an Obsidian Sync revert (L28 09-09 carve-out) | every byte of his survives; race → refuse, never merge |
| V-E5 | V2 | `com.cobalt.aset` RSS + first-clip latency with the model loaded, LM Studio serving | too heavy → T-V2 flips to a one-shot job |

## 8. OPEN TO THE TRIBUNAL (≤10)

- **T-V1** Landing: `append_to_unit` inside his unit (byte-prefix check) vs a sibling Cobalt transcript unit he copies from. Does the append violate T6's "never upserted again", or is it a distinct, narrower op L28 permits?
- **T-V2** Transcribe in the ASET request (sync, limits, state row) vs a one-shot job per capture.
- **T-V3** Engine: faster-whisper (pip-only, CPU) vs a Metal engine needing a system ffmpeg or binary — V-E2's numbers decide; is a Homebrew/binary host dependency acceptable if it wins?
- **T-V4** Fallback: one local engine + loud pending + retry, vs a second local engine.
- **T-V5** Binding: card id during the day → trade via v2 §4 card match; unmatched → A31 `voice not bound`. Any case where that binding is wrong (two trades from one card, re-entries B2)?
- **T-V6** Pre-DRC holding: captures live in `drc_voice` + imports until the note exists (R66/R93). Sound, or should a C-card capture also write to the day's trade note?
- **T-V7** Field mapping: verbatim only now vs deterministic cue-word split into B15/B16/B17 lines vs local-LLM mapping in shadow (extracted text must quote its source span).
- **T-V8** Model provisioning: pinned revision fetched at deploy, runtime offline — where the files live, and whether a model swap is a config change with its L42 restart.
- **T-V9** Surface: `/voice` on an unauthenticated page (V8). Accept under the existing backlog token item, or bind `/voice` to tailnet-only.
- **T-V10** Vocabulary bias from the day's tickers + his structure list: a lawful decoding hint (stored in params, L57) or a form of inference SPEC §9 forbids?

## 9. L52 / L7 / the bar

Reaches scoring: **no** — no chunk touches scoring, radar, `aset/engine.py` or `daymode/propose.py`; the transcript feeds no grade, size, rule result or proposal. L7 does not bind; T-V7's mapping, if built, renders in shadow. L1 failures name capture + step · L2 no LLM in the path · L3 one transcribe function, one audio writer (D2's), one append op · L9 interface + degraded probe · L23 local only · L28 his bytes never change, versioned · L31 no vendor name in an identifier · L32 user side · L40 route owns no side effect · L45 real clips · L57 audio + model revision + params stored.

## 10. OWNER ITEMS (his, one line each, A/B + recommendation)

- **W1** Capture points — A: card panel during the day AND the `/drc` trade row; B: `/drc` only, at the DRC. **Rec A** (captures while it is fresh; B is A minus one button).
- **W2** Audio retention — A: kept as long as its transcript (replayable, L57); B: deleted once the transcript lands. **Rec A.**
- **W3** Audio home — A: the R92 imports dir in the vault (synced to every device, ~1 MB per spoken minute, UNCITED — verify); B: a non-synced data dir on the Mac. **Rec A** (one imports home, R92).
- **W4** Cloud speech-to-text when local is down — A: none (pending, audio kept, retry, he can type); B: a named cloud engine as the L25 exception handler. **Rec A.**
- **W5** Scope — A: per-trade only (R100); B: also the per-day block and next-day review grade in the same build. **Rec A** (same path takes them next, new binding key only).
- **W6** Phone microphone — A: serve the ASET page over HTTPS on the tailnet (new exposure of an unauthenticated page, tailnet-only); B: phone's recorder app → file upload, no exposure change. **Rec B first, A if V-E1 shows B is clumsy** (B needs no ops change).
