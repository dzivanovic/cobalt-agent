# VOICE v3 — ONE PRESS-TO-TALK WIDGET, A CONVERSATIONAL AGENT THAT DOES WHAT HE SAYS (proposal, 2026-09-23)

Proposer: one house (Anthropic, `claude-opus-5-5`, seat `voice-v3-draft-0923`), for the four-house tribunal (L67). Origin: his **R18** (`reports/cto-2026-09-23.md` §4, 07:2x ET) — binding, not reopened here. It SUPERSEDES the scope and audio defaults of `docs/30 - Design/DRC-VOICE-v2-2026-09-22.md` (cited `v2 §n` / `[F-nn]`); what v2 still gives this design is kept by citation (§12). Ladder: S3 design lane (09-22 R100), parallel to every build (L72). No value of his appears here (L32): tickers, prices, note text and spoken words are written as `<ticker>`, `<price>`, `<text>`.

**His directive (R18), the inputs of this design, never questions:**
- (a) ONE press-to-talk widget inside Cobalt; BIDIRECTIONAL — Cobalt answers by voice; a conversational agent that EXECUTES what he asks, including knowing which field in which file to update from his words; it covers EVERY speech function discussed (per-trade answers, per-day block, no-trade reason, DRC, any command).
- (b) Audio is EPHEMERAL: local agent scratch only, deleted once transcribed and the command has run; NEVER in the vault, NEVER in the database (no audio rows, no audio blobs), NEVER in git.
- (c) Every house has the same permissions as the desk — the record button included (L44).
- Set aside by his instruction (L73, recorded in R18): L57's "replayable" for audio. The stored inputs are the transcript and the executed command.
- (d) The design questions of v2 (W2–W12) were the houses' to settle. This proposal settles each one (§11) and brings him ONE owner item, the only one that passes the test "his money, his data, his time, or a law he owns — and no house can decide it".

## 1. FACT BASE

| # | Claim | file:line | Status |
|---|---|---|---|
| F1 | No voice / STT / TTS code in the new core; the "3-tier local voice stack" is a requirement, not an install | v2 V1–V3 (`DRC-VOICE-v2-2026-09-22.md:21-23`); `COBALT-REQUIREMENTS.md:206-208` | PROVEN (v2, hub-checked) |
| F2 | The new core makes NO model call today: no LiteLLM / model-endpoint caller under `src/cobalt/` (only the old tree `src/cobalt_agent/llm.py` imports LiteLLM); the heartbeat only probes the local model's port | `grep -rln -i litellm src/cobalt` → none; `heartbeat/probes.py:252` (`def mainframe`, port 1234) | PROVEN (whole-tree grep, this run) |
| F3 | The routing v2 derive words L5 as "ONE model-access module" for every model call Cobalt's code makes; the routing cluster is FROZEN until that tribunal rules | `ROUTING-v2-2026-09-22.md:32`; LAWS "How to read this file" (routing cluster frozen) | PROVEN (text) |
| F4 | The one web surface is the ASET FastAPI app; its routes are the sheet, radar, `/size`, `/fill`, `/attest`, card move / stop, radar card key / dot / promote / release | `aset/web.py:852-1391` (`@app.get` / `@app.post`) | PROVEN |
| F5 | A card stop edit is a store call behind the entry guard: `_check_entry_allowed()` then `CardStore.record_stop_edit(card_id, from_stop, to_stop)`; the route body reads the form through `str(v)` | `aset/web.py:1239-1273` | PROVEN |
| F6 | The ASET page has no authentication; dev binds loopback on port 5010; the local override binds `lan` | `configs/dev/aset.yaml:32-41`; v2 V8 | PROVEN (v2) |
| F7 | His ruling: Cobalt stays PRIVATE and ISOLATED on the tailnet; the phone is on the tailnet; the trading PC joined it 2026-09-20 | `topics/devices.md:30`, `:11`, `:31` | PROVEN (his words) |
| F8 | Local model: Qwen3.8-27B 8-bit MLX (`mainframe`), thinking always on and inlined; `/no_think` soft switch works; decode ≈22 tok/s, TTFT 0.8 s, tool-calling 14/14; LM Studio can serve TWO models side by side | `topics/devices.md:12`, `:17`, `:21` | PROVEN (recorded measurements) |
| F9 | `VaultWriter` has `create_if_absent`, `upsert_unit` (with `skip_if`), and `upsert_region` — the ONE marker-less variant (L28 clause 2a) — and `restore`; every op passes `_session_gate` (the `market_reset` hard block) | `vaultwrite/writer.py:559`, `:644`, `:652`, `:895`, `:1066`, `:387`; `session/guard.py:1`, `:41` | PROVEN |
| F10 | The DRC build (drafted, not built) creates HIS blank units `drc-trades/voice-<trade_id>` (create-once) and `drc-day/voice-no-trades`; A31 is built by D5-3 as `drc-day/open_items` | `prompts/2026-09-22/50-drc-d3-build.md:10`, `:13`; `52-drc-d5-build.md:18` | PROVEN (text; line numbers move on re-issue — grep the anchors) |
| F11 | Backup sources are the vault and the credential vault only; nothing under the home dir outside them is snapshotted | `configs/cobalt/backup.yaml:37-41` | PROVEN |
| F12 | `MediaRecorder` needs a secure context; `tailscale serve` gives an HTTPS tailnet-only URL in front of a loopback port; browser `speechSynthesis` speaks on the device and lists `localService` voices | UNCITED — verify (E1, E5, E8) | UNPROVEN |
| F13 | faster-whisper decodes phone containers without a system ffmpeg; Metal engines need one | v2 V21 | UNPROVEN (E2, E3) |

## 2. ARCHITECTURE — one turn, end to end

```
[widget: press] → MediaRecorder blob → POST /voice/turn (tailnet HTTPS)
  → scratch file <scratch_dir>/<turn_id>.<ext>   (0600, outside repo/vault/backup)
  → Transcriber (local, in-process)             → transcript row committed
  → scratch file UNLINKED                          (the deletion point, §5)
  → context fetch (code: clock, today's cards, the DRC's parsed trades, the target note's field list)
  → ONE model call via the model-access module (local first): a typed Plan
  → resolver (code): note → target → field → write class → value parse
  → read tools: answer rendered by code  |  side effect: read-back + pending action
  → reply text → widget shows it + speaks it (device TTS)
[next press: "yes" / tap Confirm] → deterministic confirm match → the OWNING expert executes → reply
```

**2.1 The widget.** One floating press-to-talk button rendered on every ASET page (the sheet, `/radar`, and `/drc` when the DRC build ships it) by one shared template partial. Hold-to-talk (release = send) and tap-to-toggle both map to the same `start()` / `stop()`. Beside it: a text box (the typed turn — same endpoint, same function, L3), the last reply as text, a mute toggle for spoken replies, a Confirm / Cancel pair shown only while an action is pending, and the degraded banner (§7). The page sends, with each turn, the deterministic UI context it already holds: page name, the card id or trade row the widget was pressed nearest to (if any), and the widget session id. Context narrows candidates; it never overrides what he said.

**2.2 Capture.** `MediaRecorder` in the page (E1 fixes the container per device). The upload is multipart; the handler reads the `UploadFile` bytes itself — never the `str(v)` form idiom (v2 `[F-19]`; F5). A zero-byte or non-file part FAILs and names the reason. Length and size bounds are engine tunables (§11 W7).

**2.3 Local speech-to-text.** v2 §5 kept whole where it holds: a `Transcriber` interface (Pydantic in / out), one engine chosen by config, faster-whisper first on the host's CPU, Metal engines only by measurement and a named deploy step (v2 `[F-03]`), model files fetched once into `model_dir` outside vault and repo, pinned revision, `local_files_only` (v2 `[F-08]`). The engine runs off the event loop (`to_thread`) so a transcribe never stalls `/size` or `/fill` (v2 X2, V-E5 measure it). No cloud STT (L23; L25 — no route).

**2.4 The conversational agent and its tool boundary (tools fetch, agents reason; numbers are code).**
- The agent is a REGISTRY ENTRY, not code (L16): `configs/cobalt/agents/voice.yaml` — charter, the model route name, the tool allowlist, the confirm and cancel word lists. It speaks as Cobalt's chief of staff to him, one throat (L14); experts stay backstage.
- Per turn it gets, from code: the transcript, the last `history_turns` turns of this widget session (from `voice_turns` rows — the agent itself is stateless, L2), the clock, and CLOSED CANDIDATE LISTS built by code (today's cards with ids, the DRC's parsed trades with ids, the target note's addressable fields with ids, the tool list with argument schemas). No credential, env value or config secret ever enters the prompt (L4, L41): the prompt builder takes only whitelisted fields.
- It returns ONE typed `Plan` (Pydantic; a parse failure = FAILED turn, loud): `kind` (one of `answer`, `act`, `clarify`, `unsupported`, `refuse`), `tool` (a name from the allowlist), `args` whose every free value is a `Span` — a verbatim substring of the transcript, checked by code — or a candidate id from a closed list, and `say` (optional prose without figures).
- One model call per turn, through the model-access module (F3); the route is local first (`mainframe`, `/no_think`, F8); the same call shape can go to a second small local model if E4 says latency needs it (L23, L26 — assignment by measurement). No cloud route is built (L25).
- The tool boundary: READ tools return data; the reply for a read is rendered by a code template from that data. ACT tools never write: each one is an ASK to the expert that owns the side effect (L38, L40) — vault writes through the owning module's function and `VaultWriter`, card state through `CardStore`, a DRC build through its own command. The voice module owns exactly one side effect: its own `voice_turns` rows.
- Figures: any digit in `say` that is not in the tool result is dropped and the code template is spoken instead (a deterministic check). A value he dictates is parsed by a deterministic parser per field type (price, share count, time, date, grade from a closed set); the read-back speaks the PARSED value, so a mis-hearing is caught before it lands.
- HARD REFUSALS by code, whatever the Plan says: anything that places, changes or cancels an order or touches his trading platform (no such tool exists; `refuse` with a fixed sentence); any tool marked `trading_logic: true` in the registry (settings, rules, strategies, thresholds) is never executed by voice — it is drafted as the exact change + sha256 and sent to him as a HITL card over the existing outbound notify, and approved only where L7 says approvals happen today (the desk chat). This keeps L7 intact without an amendment.

**2.5 Reply by voice.** The reply text is shown in the widget and spoken by the DEVICE's own speech synthesis (`speechSynthesis`, a `localService` voice only). No reply audio exists on the server at all. No local voice on a device → text only, with an AMBER "no local voice on this device" line (L9). A server-side local TTS engine (the requirement's named one) is a later slice only if E5 fails; if built it streams and writes no file.

**2.6 Confirmation of side effects by voice.** Every ACT produces a pending action: the owning expert's DRY-RUN result (the exact before → after for a vault write, the exact field change for a card), its `diff_sha256`, and a spoken read-back ("<field> in <note> for <date>: <before> → <after>. Say yes to do it."). Execution happens only when (a) his NEXT turn's normalized transcript equals a word from the registry's closed confirm list — matched by code, never by the model (L37) — or he taps Confirm, (b) the pending action is younger than `confirm_ttl_s`, and (c) the owning expert's re-computed diff still has the same sha256 (the note or card did not change underneath — else REFUSED, re-read aloud). A cancel word, any other speech, or the TTL ends the pending action unexecuted. Reads never ask for confirmation.

## 3. HOW EACH SPEECH FUNCTION MAPS ONTO IT

| Function (R18 "every speech function") | Tool (owner) | Target | Write class (§6) | Confirm |
|---|---|---|---|---|
| Per-trade answer (narrative about one trade) | `drc.voice.append` (DRC module → `VaultWriter`) | `drc-trades/voice-<trade_id>` | append-only into his voice unit (v2 `[F-01]`) | yes |
| Per-trade answer BEFORE the DRC exists (during the day) | same tool; the turn row holds `card_id` + text as `pending_landing` | lands at the build through ONE landing function `land_pending(date)` | append-only | yes (at capture; landing needs none — it lands what he confirmed) |
| Per-day block (his day fields) | `drc.voice.fill` / `append` | the DRC's day-level blank cells or his day voice unit | blank-cell fill (2a) or append | yes |
| No-trade reason | `drc.voice.append` | `drc-day/voice-no-trades` | append-only | yes |
| DRC field edit ("set <field> on trade <n> to <value>") | `drc.voice.fill` | the resolved field | by field state (§6) | yes |
| DRC commands (build now, status, what is missing) | `drc.build` / `drc.status` (DRC module) | — | the command's own writes | build: yes; status: no |
| Card stop | `cards.set_stop` → `CardStore.record_stop_edit` behind `_check_entry_allowed()` (F5) | an open card | DB (the store's own row) | yes |
| Questions ("what is on radar", "my open cards", "size on <ticker>") | read tools over the existing stores | — | none | no |
| Anything else | `unsupported` → "I can't do that yet" + the turn row marked `unsupported` (the desk reads the count as a backlog feed) | — | none | — |

## 4. "WHICH FIELD IN WHICH FILE" — resolved by code, never guessed

1. **Which note.** `NoteRef(kind, date)`: `kind` is a closed enum (DRC, daily note, trade note; cards and radar are not files). The date is parsed by code from the transcript spans (today / yesterday / weekday / explicit date) against the session clock; the path comes from the existing path resolvers (`load_prefill_paths()` and the DRC's own) — never a path built by the model.
2. **Which trade or card.** Candidates are enumerated by code: today's cards (`aset_sizings`) and, once the DRC exists, its parsed trades. The Plan's spans (ticker text, side, ordinal, entry time) are matched by code; the UI context (§2.1) narrows. Exactly one → bound. Zero or two-plus → `clarify`: the agent reads the candidates back by their code-rendered labels and waits. Never the nearest, never the earliest (v2 R2-V5 — this proposal takes the unbound side).
3. **Which field.** Code enumerates the ADDRESSABLE FIELDS of that note from the note itself, at request time: marker units by id, template labels (`<Label>:` lines and headings), blank cells, his voice units. The model picks one field id from that closed list; code checks it exists exactly once. The labels are read from his files at runtime, never committed (L32).
4. **Which write class.** Decided by code from the field's STATE (§6), never by the model.
5. **Which value.** A verbatim `Span`, parsed by the field type's deterministic parser; unparseable → `clarify`, never a guess. Free text lands verbatim.

## 5. THE EPHEMERAL-AUDIO LIFECYCLE (R18 (b))

- **Scratch path:** `scratch_dir` in `configs/cobalt/voice.yaml` — production value `/Users/cobalt/.cobalt/voice-scratch/`, dev value `/Users/cobalt/.cobalt-dev/voice-scratch/` (the committed default is the dev path, like `configs/dev/vault.yaml`'s dev default; production sets its own through the same explicit override pattern its launchd env already uses for the vault). The config schema REFUSES to load (L1, L10) when `scratch_dir` is relative, or sits under the repo root, under the resolved vault path, under `docs/`, or under any `backup.yaml` source (F11). Directory mode 0700, files 0600, name `<turn_id>.<ext>`.
- **Life:** written by the upload handler (the voice module's one file writer — not a vault write, not the DRC bytes method) → read by the Transcriber → **UNLINKED in a `finally:` right after the transcript row commits, or on any failure of the turn** — the deletion point. The audio is never needed again: every later step (plan, confirm, execute) runs from text. The row records `audio_deleted_at`. A failed transcribe keeps nothing: he says it again or types.
- **Crash leftovers:** on resident start and on every heartbeat, a sweep deletes any scratch file older than `scratch_max_age_s`; finding one is AMBER (it means a turn died mid-way), an unlink that fails is RED (L9).
- **Never in the database:** `voice_turns` has no bytes column; it keeps `audio_sha256`, byte length and duration only (dedupe of a repeated post, and audit), which are not a recording. A schema test asserts no `bytea` / large-object column on any voice table.
- **Never in git:** the scratch path is outside the repo by the config check above; a suite test fails if `git ls-files` lists any audio extension; tests SYNTHESIZE their audio at test time into `tmp_path` in the real container format E1 fixes (speech from the host's own synthesizer, tones for decoder tests) — never a recording of his voice, never a committed audio file (L45 real shape, L32).
- **Never in the vault:** no path under the vault is ever a scratch path (config check); the vault receives only text, through `VaultWriter`.

## 6. THE L28 PATH FOR VOICE-ORDERED EDITS

A voice-ordered edit of his notes is a Cobalt vault write (R18; L28 SCOPE binds Cobalt the program; L65 is desk-only). Each write class, by the target field's state:

| Field state (code decides) | Op | L28 basis |
|---|---|---|
| His voice unit (`drc-trades/voice-<id>`, `drc-day/voice-no-trades`, a day voice unit) | `append_to_unit` — idempotent on the turn id, suffixes the bytes it read under the mtime guard or refuses, never merges, never takes the sync-revert win (v2 `[F-01]`, `[F-18]`) | append of a marked unit Cobalt created; his bytes unchanged |
| A BLANK template cell / bullet outside markers | `upsert_region` (F9), blank → value only, versioned | clause 2a |
| A Cobalt-owned unit | never edited by voice: a spoken correction of a computed value goes to that value's own correction path (R90's resolve action / A28, v2 §2) and the agent says so | numbers are code; human-wins untouched |
| HIS NON-BLANK TEXT outside markers | **not writable under L28 today.** Until he rules OWNER ITEM O1, the agent refuses this class aloud, names the field and says why | O1 |
| A trading-logic field | never executed by voice (§2.4), HITL card | L7 |

Every write: `_session_gate` (refused inside `market_reset`, spoken as such), versioned to Postgres with the unified diff, the `vault_writes` id stored on the turn row, atomic write + mtime guard, and the confirm-time sha256 check (§2.6). Pre-DRC landing: ONE landing function `land_pending(date)` (v2 R2-V1, the single-path side): the DRC build creates his voice unit BLANK exactly as D3 does today and then calls `land_pending`; the widget's confirm calls the same function when the unit already exists. One landing writer (L3).

## 7. FAILURE MODES AND THEIR LOUD STATES (L1, L9, L18)

Turn state machine on `voice_turns`: `received → transcribing → planned → (answered | awaiting_confirm → executing) → done | failed | cancelled | expired | unsupported`. A row still `transcribing` / `executing` past its limit is reaped to `failed: <class>` (v2 `[F-02]`).

| Failure | He sees / hears | Heartbeat |
|---|---|---|
| No microphone / permission denied | widget red: "no microphone on this device" — text box still works | — |
| Local STT down / model file missing | red: "speech-to-text down (<class>)"; audio already deleted; text box works | `voice_stt` RED |
| Empty transcript | "I heard nothing" — no plan, no write | — |
| Local model down / Plan does not parse | red: "Cobalt can't think right now (<class>)" — nothing executed | `voice_plan` RED (reuses the `mainframe` probe) |
| Ambiguous target / unparseable value | `clarify` read-back of the candidates | — |
| Target changed since read-back | "your note changed — here is the new before → after" (re-confirm) | — |
| `market_reset` | "writes are blocked until 21:00" — nothing queued | — |
| His-text overwrite (until O1) / trading logic | spoken refusal naming the field and the law | — |
| Scratch leftover / unlink failure | — | `voice_scratch` AMBER / RED |
| No local TTS voice on the device | reply as text + AMBER line | — |

## 8. EVERY HOUSE, THE RECORD BUTTON INCLUDED (R18 (c), L44)

One turn function, three callers, no per-house gate: the widget route `POST /voice/turn`, the CLI `cobalt voice turn --audio <file> | --text "<text>" [--confirm <turn_id>] [--dry-run]`, and the tests. Any house holding a build or check seat runs the same path in DEV (NN#16: `cobalt_dev`, the dev vault, dev config) with synthetic audio or text; `--dry-run` prints the Plan, the resolution and the exact diff with no write (L10's dry-run). Production is reached only through deploys, as for every other path.

## 9. SLICE PLAN

Seats: Opus 5 floor on every write-path chunk, never auto mode on a write path (L29); each build checked by ≥3 tribunal members (L67 as amended R46). Hours are seat hours, a GUESS until the builders re-derive them.

| Slice | What runs end to end | Write path | Migration | Depends on | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| **V1 — first conversation** (the smallest end-to-end conversation that runs a real command) | widget + text box on the ASET pages; `/voice/turn`; scratch lifecycle + sweep; Transcriber (faster-whisper); the model-access call (F2/F3 — see seam S1); Plan + resolver for cards; read tools (open cards, radar pool, a card's numbers — code-rendered); ONE confirmed act: **card stop** via `CardStore.record_stop_edit`; device TTS; CLI; `voice_turns`; degraded banner | DB (`voice_turns`; the card store's own row) | ONE (`"user".voice_turns`; number: the desk's at L68) | E1–E4, E6, E7, E10 | `com.cobalt.aset` | 9 |
| **V2 — DRC by voice** | per-trade answer (append + `land_pending`), no-trade reason, per-day block (blank cells + his day units), DRC field fill, `drc.build` / `drc.status`; `append_to_unit` (new `VaultWriter` op) | vault | — | DRC D2 + D3 merged (voice units exist); E9 | `com.cobalt.aset` | 7 |
| **V3 — any note field** | field enumeration for the daily note and trade notes; blank-cell fills; the his-text class switched on only if O1 is ruled | vault | — | V2; O1 for the overwrite class only | `com.cobalt.aset` | 4 |
| **V4 — ops** | `voice_stt` / `voice_plan` / `voice_scratch` probes; model-fetch deploy step; the `tailscale serve` deploy step (§11 W6); DevDocs | no (probes read) | — | V1 | the heartbeat resident | 2 |

**Total 22 h seats (9+7+4+2), ≈ 31 h with one fix round each (factor ×1.4, UNVERIFIED as in v2 §7).** V1 needs nothing from the DRC build and can land in any evening deploy after its checks (L43). V2 rides the deploy that carries DRC D2 + D3 or a later one.

## 10. EXPERIMENTS OWED — measured on his devices (L70)

Run before the slice they gate, in dev; his hands only where a device is his (the phone's microphone prompt, once).

| # | Before | What (where) | Result that changes the design |
|---|---|---|---|
| E1 | V1 | his Android phone, the trading-PC browser and the Mac: the widget page over `tailscale serve` HTTPS — `MediaRecorder` available? which container / codec? a plain-http page as control; does the trading PC have a microphone | no recorder over tailnet HTTPS → W6 re-opens; the container list fixes the handler and the synthetic fixtures |
| E2 | V1 | STT on the Mac Studio: faster-whisper sizes vs Metal comparators on SYNTHETIC speech in E1's containers carrying the words the desk uses (setup names, exit words, card-style tickers generated, not his) — word accuracy, latency, RSS beside LM Studio's 88 GB wired limit; same output twice | picks engine + size; a Metal winner needs its named deploy step (v2 `[F-03]`) |
| E3 | V1 | decode E1's real phone files with the chosen engine and no system ffmpeg | fail → ffmpeg becomes a named host dependency (v2 `[F-03]`) |
| E4 | V1 | the Plan call on `mainframe` with `/no_think`: parse-valid rate and latency over a constructed utterance set (every §3 function, ambiguous and hostile cases, a trade-execution request); same on a second small local model beside it | parse-valid rate too low → tighter schema / fewer candidates; latency → second small model (L23 route by measurement) |
| E5 | V1 | `speechSynthesis` on his phone and the trading-PC browser: `localService` voices present? speaks inside the page? | none local → text-only on that device + server local TTS slice |
| E6 | V1 | `/fill` and `/size` latency while a turn transcribes (v2 X2, V-E5) | stall → the Transcriber moves to a one-shot job of the same function |
| E7 | V1 | `kill -9` of `com.cobalt.aset` mid-transcribe and mid-execute | row not reaped to `failed`, or scratch file survives the sweep → lifecycle fix before ship |
| E8 | V1 | `tailscale serve` in front of the loopback port: the source address and headers the route sees; a LAN client's request to `/voice/turn` | the tailnet-only check (§11 W11) keys on what this shows |
| E9 | V2 | dev vault: `append_to_unit` and `land_pending` twice; a crash between commit and row update; his edit during an append; an Obsidian Sync revert; a call in `market_reset` (v2 V-E4, X3, X4) | any double block or changed byte of his → op fixed before V2 ships |
| E10 | V1 | scratch worktree `uv add faster-whisper` → full lock diff with licences (v2 X8); offline model load and a missing model file (v2 X7) | an unexpected native / GPL package → tribunal round 2 |
| E11 | V2 | re-import a superseding log leaving one trade unchanged: identical `trade_id`? (v2 X9) | not identical → the seam fixes the id rule before V2 |

## 11. v2 OWNER ITEMS W1–W12 — SETTLED BY THE HOUSES (none reaches him)

| v2 item | v3 answer | Basis |
|---|---|---|
| W1 capture points | ONE widget on every ASET page | R18 (a) |
| W2 audio retention | deleted at transcription | R18 (b) |
| W3 audio home | local scratch, §5 | R18 (b) |
| W4 cloud STT when local is down | none; loud red, text box works | L23, L25 (no route); his voice leaving the host would be a new decision, not proposed |
| W5 scope | every speech function, §3 | R18 (a) |
| W6 phone microphone | the widget is served over `tailscale serve` HTTPS on the tailnet, proxied to the existing loopback / LAN port; nothing public | his 09-16 ruling "private and isolated on the tailnet" (F7); E1, E8 |
| W7 limits | `max_clip_s`, `max_upload_bytes`, `stt_timeout_s`, `confirm_ttl_s`, `scratch_max_age_s`, `history_turns` are ENGINE TUNABLES in `configs/cobalt/voice.yaml`, each set by the V1 builder from E2 / E4 measurements with its source line; a missing key crashes the load (L1). L53 reserves only the Finviz ceiling, scan cadence and pool settings — not these | L53 text, L10 |
| W8 vocabulary hint | off until E2 shows the hint inserts no unspoken word; when on, the hint is today's card tickers read from the DB at runtime, never a committed list | L32, v2 X6 |
| W9 no-trade voice | in scope, §3 | R18 (a) |
| W10 row retention | `voice_turns` rows kept, no pruning: they are the stored inputs of every executed command (L57 as set aside) | L57 |
| W11 who reaches the route | `/voice/*` answers only requests arriving through the tailnet proxy or from loopback; a LAN client is refused with a named 403 — narrower than the page, because this route can write his vault | F7, E8 |
| W12 his clips in git | none; synthetic audio generated at test time | R18 (b) |

## 12. WHAT v3 KEEPS FROM v2, AND WHAT IT SUPERSEDES

| v2 clause | v3 |
|---|---|
| §5 Transcriber interface, faster-whisper first, Metal by measurement `[F-03]`, `model_dir` pinned offline `[F-08]`, off-loop `[F-02]` reap | KEPT |
| `[F-19]` bytes read from `UploadFile`, zero-byte FAIL, empty transcript lands nothing | KEPT |
| `[F-01]` idempotent `append_to_unit`; `[F-18]` no sync-revert win | KEPT (now for every his-voice unit) |
| T-V7 verbatim only for narrative | KEPT for narrative answers; a field edit is his explicit order, parsed by code |
| R2-V1 (initial body vs one landing function) | SETTLED here by the proposer on the single-path side (`land_pending`), for this tribunal to rule |
| R2-V5 (>1 trade per card) | SETTLED here: unbound, `clarify` at capture, listed on A31 if still unbound |
| §3 binding "never by speech" | SUPERSEDED: speech resolved by code against closed candidate lists (§4) — R18 "knowing which field in which file … by my word" |
| §6 audio in the R92 imports dir, `drc_voice` holding audio path + sha as the stored input, `[F-15]` audio through D2-2's bytes method, `[F-16]` "no transcript without audio" | SUPERSEDED by R18 (b) and L57 set aside; the D2 bytes method carries no voice |
| W1–W12 as owner items; V-E2 on his clips | SUPERSEDED (§11; E2 on synthetic speech) |
| Seam entries 1, 2, 4, 5 (D3 unit creation, `append_to_unit`, A31 line in D5-3, the `orphaned` edge-insert) | KEPT; entry 3 (`voice/` sub-path under D2-2) VOID |

## 13. SEAM (L72 P-b) — one document both lanes cite before either launches

- **S1 model access.** The new core has no model caller (F2) and the routing cluster is frozen (F3). V1 needs one call. The seam document names ONE module (`src/cobalt/modelaccess/` or whatever name the routing lane rules) that V1 creates with the local lane only and the routing build extends — never a second copy (L3). Which lane creates it first is the desk's ordering, stated in the seam document.
- **S2 DRC.** v2 seam entries 1, 2, 4, 5 carried; `land_pending(date)` is called by D3's build after it creates the voice units; A31's `voice not bound` line is rendered by D5-3 from `voice_turns` rows.
- **Shared files:** `aset/web.py` (routes, the widget partial), `vaultwrite/writer.py` (`append_to_unit`), `drc/build.py`, `db_migrations/placement.py`, `heartbeat/probes.py`.

## 14. L52 / L7 / THE BAR

Reaches scoring: NO — nothing computes a score, rank, grade or size; the one card act (stop) is the same human-fed edit the page makes, marked YOURS (F5). L52 does not bind; L67's tribunal is this one. L7: no variable flips to engine-fed; trading-logic changes are never executed by voice (§2.4). L1 §7 · L2 each press is an event; no wake word, no listening loop · L3 one turn function, one landing function, one scratch writer · L4 / L41 no secret in any prompt · L9 probes + banners · L14 one voice · L16 the agent is a registry entry · L18 the turn row is the task row · L23 / L25 local only, no cloud route · L28 §6 · L32 transcripts are user-side rows; nothing of his committed · L37 confirm matched by code · L40 the voice module owns only its rows · L44 §8 · L45 real container, synthetic content · L57 as set aside: transcript + Plan + resolution + confirm + the expert's write id are the stored inputs.

## OWNER ITEMS

**O1 — L28 amendment: may Cobalt overwrite HIS OWN non-blank text when he orders that exact edit by voice and confirms it?** Why no house can decide it: L28 is law and forbids it (Cobalt writes only its marker units and blank cells; human text wins); a law changes only by his ruling (Preamble "Dejan rules"; L58; L73 — no house skips or waives a law step). Everything else in this design runs without it; only the "change what I already wrote" class waits (§6, V3). Fold text proposed, for his yes / no:

> [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text outside marker units — his text included — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that one diff; the write is the smallest span (that field's value), goes through `VaultWriter` with the mtime guard and `_session_gate`, is versioned with before and after and the turn id, and is refused if the note changed since the read-back. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.
