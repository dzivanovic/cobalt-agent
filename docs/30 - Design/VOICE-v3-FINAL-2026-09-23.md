# VOICE v3 — ONE PRESS-TO-TALK WIDGET, A CONVERSATIONAL AGENT THAT DOES WHAT HE SAYS (FINAL, 2026-09-23) — ASTRA PENDING (R13)

**FINAL, derived by the third derive (R3, the last round — L67, L39).** Seat `voice-v3-derive-r3-0923` (`claude-opus-5-5`, DERIVE ROW 09-22 R109), launch row `cto-2026-09-23.md` R49. Fold table: `docs/40 - DevDocs/reports/voice-v3-derive-r3-2026-09-23.md` `## Fold table` (rows `R3F-nn`). Every point open after round 2 is REPLACED in place: a converged point by the converged wording, verbatim, tagged `[R3F-nn]`; an unresolved point by its sides, each verbatim, labelled `**[R3-<item> side <A|B|C> — <seats>]**`, followed by the line naming his letter. Everything else is the derived design's text, unchanged.
**Inputs of this FINAL:**
- The derived design `docs/30 - Design/VOICE-v3-derived-2026-09-23.md` (committed `fc82bfa`), itself the proposal `VOICE-v3-proposal-2026-09-23.md` (`153c4b8`) amended by round 1 (`[F-nn]`, fold table `reports/voice-v3-derive-2026-09-23.md`).
- Round 2: hub report `docs/40 - DevDocs/reports/voice-v3-tribunal-r2-2026-09-23.md` (C1–C8, G1–G13, K1–K20); raw rulings `scratch/tribunal-bars-0920/voice-v3-tribunal/r2/grok-ruling-r2.md` and `…/r2/gemini-ruling-r2.md` (worktree `~/cobalt-wt/agy-trial`); the Anthropic seat `docs/40 - DevDocs/reports/voice-v3-tribunal-fable-r2-2026-09-23.md`; the second derive `docs/40 - DevDocs/reports/voice-v3-derive-r2-2026-09-23.md`.
- Round 3: hub report `docs/40 - DevDocs/reports/voice-v3-tribunal-r3-2026-09-23.md` (C9–C22, GM1–GM15, GK1–GK21, H1, H2); raw rulings `…/r3/grok-ruling-r3.md` and `…/r3/gemini-ruling-r3.md`; the Anthropic seat `docs/40 - DevDocs/reports/voice-v3-tribunal-fable-r3-2026-09-23.md`.
- His rulings, never reopened: `cto-2026-09-23.md` R18 (VOICE v3 DIRECTIVE), R39 (O1), R43 (O1 scope = his words; houses rule mechanics only); `cto-2026-09-22.md` R92, R93, R99, R100, R109 (seat model).
- Astra: round 2 `METER — proceed on three`; round 3 `SKIPPED — R13 (probe UP, recorded)`. **ASTRA PENDING (R13): Astra reads this FINAL on Sat 09-26.**
**Outcome of round 3 (the last; no round 4):**
- R2-1 (who deletes crash-leftover scratch audio, and when): UNRESOLVED — `## FOR DEJAN` item 2 (side A = `B`, the Anthropic seat; side B = `N1`, grok and gemini).
- R2-2 (O1's fold mechanics under SCOPE-R39): UNRESOLVED — `## FOR DEJAN` item 3 (side A = `S`, the Anthropic seat; side B = `N2`, gemini; side C = grok's NEITHER).
- R2-3 (which slice builds the trading-logic draft-and-send tool): CONVERGED — ADOPT A-V5, grok, gemini and the Anthropic seat; slice V5 `[R3F-09]`.
- O1: RULED B (R39); scope per R43 (`## OWNER ITEMS`).

Proposer: one house (Anthropic, `claude-opus-5-5`, seat `voice-v3-draft-0923`), for the four-house tribunal (L67). Origin: his **R18** (`reports/cto-2026-09-23.md` §4, 07:2x ET) — binding, not reopened here. It SUPERSEDES the scope and audio defaults of `docs/30 - Design/DRC-VOICE-v2-2026-09-22.md` (cited `v2 §n` / `[F-nn]`); what v2 still gives this design is kept by citation (§12). Ladder: S3 design lane (09-22 R100), parallel to every build (L72). No value of his appears here (L32): tickers, prices, note text and spoken words are written as `<ticker>`, `<price>`, `<text>`.

**His directive (R18), the inputs of this design, never questions:**
- (a) ONE press-to-talk widget inside Cobalt; BIDIRECTIONAL — Cobalt answers by voice; a conversational agent that EXECUTES what he asks, including knowing which field in which file to update from his words; it covers EVERY speech function discussed (per-trade answers, per-day block, no-trade reason, DRC, any command).
- (b) Audio is EPHEMERAL: local agent scratch only, deleted once transcribed and the command has run; NEVER in the vault, NEVER in the database (no audio rows, no audio blobs), NEVER in git.
- (c) Every house has the same permissions as the desk — the record button included (L44).
- Set aside by his instruction (L73, recorded in R18): L57's "replayable" for audio. The stored inputs are the transcript and the executed command.
- (d) The design questions of v2 (W2–W12) were the houses' to settle. This proposal settles each one (§11) and brings him ONE owner item, the only one that passes the test "his money, his data, his time, or a law he owns — and no house can decide it".

## Status after round 3

| item | outcome | whose text | slice it gates |
|---|---|---|---|
| R2-1 — crash-leftover scratch audio (§5 bullet, §9 V4 row) | UNRESOLVED → `## FOR DEJAN` item 2 | side A: the Anthropic seat (`B`) · side B: grok, gemini (`N1`) | V1 (the sweep), V4 (the probe row) |
| R2-2 — O1 fold mechanics (the `FOLD:` text, §6 Cobalt-owned-unit row) | UNRESOLVED → `## FOR DEJAN` item 3 | side A: the Anthropic seat (`S`) · side B: gemini (`N2`) · side C: grok (NEITHER) | V3 (the voice-ordered edit class); the L28 fold at his approval |
| R2-3 — trading-logic draft-and-send slice | CONVERGED `[R3F-09]` | grok's lines (identical in gemini's and the Anthropic seat's) | V5 (new; after V1) |
| O1 — L28 scope | RULED B (R39); scope per R43 | his words | V3 |

## 1. FACT BASE

| # | Claim | file:line | Status |
|---|---|---|---|
| F1 | No voice / STT / TTS code in the new core; the "3-tier local voice stack" is a requirement, not an install | v2 V1–V3 (`DRC-VOICE-v2-2026-09-22.md:21-23`); `COBALT-REQUIREMENTS.md:206-208` | PROVEN (v2, hub-checked) |
| F2 | The new core makes NO model call today: no LiteLLM / model-endpoint caller under `src/cobalt/` (only the old tree `src/cobalt_agent/llm.py` imports LiteLLM); the heartbeat only probes the local model's port | `grep -rln -i litellm src/cobalt` → none; `heartbeat/probes.py:252` (`def mainframe`, port 1234) | [F-20] HOLDS for the new core; DOES NOT HOLD in its detail "only … `llm.py` imports LiteLLM" — `cobalt_agent/tools/extractor.py:22` and `cobalt_agent/memory/postgres.py:31` import it too (old tree). Add: `litellm == 1.81.8` is ALREADY a direct dependency (`pyproject.toml:16`), so the S1 module adds no new dependency if it uses it · [F-21] hub C1/C3: `src/cobalt/radar/audit_export.py:7` matches the `openai` grep on the prose "The OpenAI house recomputes `card_score`"; its imports (`:43-61`) carry no litellm / openai / httpx — it is NOT a model caller |
| F3 | The routing v2 derive words L5 as "ONE model-access module" for every model call Cobalt's code makes; the routing cluster is FROZEN until that tribunal rules | `ROUTING-v2-2026-09-22.md:32`; LAWS "How to read this file" (routing cluster frozen) | PROVEN (text) |
| F4 | The one web surface is the ASET FastAPI app; its routes are the sheet, radar, `/size`, `/fill`, `/attest`, card move / stop, radar card key / dot / promote / release | `aset/web.py:852-1391` (`@app.get` / `@app.post`) | PROVEN |
| F5 | A card stop edit is a store call behind the entry guard: `_check_entry_allowed()` then `CardStore.record_stop_edit(card_id, from_stop, to_stop)`; the route body reads the form through `str(v)` | `aset/web.py:1239-1273` | [F-20] HOLDS; MISSED: `record_stop_edit` gates itself (`cards/store.py:659`), refuses outside `STOP_EDITABLE` (`:661`), and RECOMPUTES `shares`/`per_share_risk` through `engine.recompute_for_stop` (`:668-674`, `:708`, `:730`) |
| F6 | The ASET page has no authentication; dev binds loopback on port 5010; the local override binds `lan` | `configs/dev/aset.yaml:32-41`; v2 V8 | PROVEN (v2) |
| F7 | His ruling: Cobalt stays PRIVATE and ISOLATED on the tailnet; the phone is on the tailnet; the trading PC joined it 2026-09-20 | `topics/devices.md:30`, `:11`, `:31` | PROVEN (his words) |
| F8 | Local model: Qwen3.8-27B 8-bit MLX (`mainframe`), thinking always on and inlined; `/no_think` soft switch works; decode ≈22 tok/s, TTFT 0.8 s, tool-calling 14/14; LM Studio can serve TWO models side by side | `topics/devices.md:12`, `:17`, `:21` | PROVEN (recorded measurements) |
| F9 | `VaultWriter` has `create_if_absent`, `upsert_unit` (with `skip_if`), and `upsert_region` — the ONE marker-less variant (L28 clause 2a) — and `restore`; every op passes `_session_gate` (the `market_reset` hard block) | `vaultwrite/writer.py:559`, `:644`, `:652`, `:895`, `:1066`, `:387`; `session/guard.py:1`, `:41` | [F-20] HOLDS for line numbers; DOES NOT HOLD in two details: "every op passes `_session_gate`" — `restore` is UNGATED by ruling (`session/guard.py:82-84`; the gate is called at `writer.py:565, 664, 922` only); and `upsert_region` is not "blank → value only" (T9: `writer.py:946-951`, `merge.py:14-15`); its own docstring calls it "the frontmatter carve-out" (`writer.py:904-918`), with one non-frontmatter caller (`seatusage/runner.py:147`) |
| F10 | The DRC build (drafted, not built) creates HIS blank units `drc-trades/voice-<trade_id>` (create-once) and `drc-day/voice-no-trades`; A31 is built by D5-3 as `drc-day/open_items` | `prompts/2026-09-22/50-drc-d3-build.md:10`, `:13`; `52-drc-d5-build.md:18` | [F-20] HOLDS by anchor: `50:10` (R93), `50:13` (R99); D5-3 is at `52:21` now (the proposal warned lines move); `52:26` "NOT IN D5: … voice (R100)" |
| F11 | Backup sources are the vault and the credential vault only; nothing under the home dir outside them is snapshotted | `configs/cobalt/backup.yaml:37-41` | [F-20] HOLDS; add: the nightly dump of `cobalt_brain` (`backup.yaml:47-49`) carries `voice_turns` TRANSCRIPTS into backups — text, not audio, consistent with R18 (b) |
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

[F-01] One widget, one turn function, three callers (`POST /voice/turn`, `cobalt voice turn`, tests). A turn that needs a Plan makes exactly one call, through the one model-access module, and no other caller. A turn whose row is `awaiting_confirm` makes zero model calls and only matches confirm or cancel. The same turn that returns a Plan never executes an ACT.

**2.1 The widget.** One floating press-to-talk button rendered on every ASET page (the sheet, `/radar`, and `/drc` when the DRC build ships it) by one shared template partial. Hold-to-talk (release = send) and tap-to-toggle both map to the same `start()` / `stop()`. Beside it: a text box (the typed turn — same endpoint, same function, L3), the last reply as text, a mute toggle for spoken replies, a Confirm / Cancel pair shown only while an action is pending, and the degraded banner (§7).
[F-10] The floating widget sends no card id and no trade id. UI context narrows only when the control he pressed belongs to one card or one trade row, or the page is showing exactly one. Geometric nearest is never a candidate. A weekday name that is not uniquely today or earlier against the session clock clarifies; it never selects a future date. Zero candidates or two-plus clarify; never nearest, never earliest. Field id must exist exactly once in the note's own enumerated fields. Unparseable value clarifies. Free text lands verbatim.

**2.2 Capture.** `MediaRecorder` in the page (E1 fixes the container per device). The upload is multipart; the handler reads the `UploadFile` bytes itself — never the `str(v)` form idiom (v2 `[F-19]`; F5). A zero-byte or non-file part FAILs and names the reason. Length and size bounds are engine tunables (§11 W7). Who may reach the route: §11 W11 `[F-03]`.

**2.3 Local speech-to-text.** v2 §5 kept whole where it holds: a `Transcriber` interface (Pydantic in / out), one engine chosen by config, faster-whisper first on the host's CPU, Metal engines only by measurement and a named deploy step (v2 `[F-03]`), model files fetched once into `model_dir` outside vault and repo, pinned revision, `local_files_only` (v2 `[F-08]`). The engine runs off the event loop (`to_thread`) so a transcribe never stalls `/size` or `/fill` (v2 X2, V-E5 measure it). No cloud STT (L23; L25 — no route).
[F-04] The Plan call is off the event loop too: the model-access module's call is awaited on an async client or run through `to_thread`, never a blocking call inside the `async def` route. E6 measures `/size` and `/fill` latency during a transcribe AND during a Plan call.

**2.4 The conversational agent and its tool boundary (tools fetch, agents reason; numbers are code).**
- The agent is a REGISTRY ENTRY, not code (L16): `configs/cobalt/agents/voice.yaml` — charter, the model route name, the tool allowlist, the confirm and cancel word lists. It speaks as Cobalt's chief of staff to him, one throat (L14); experts stay backstage.
- Per turn it gets, from code: the transcript, the last `history_turns` turns of this widget session (from `voice_turns` rows — the agent itself is stateless, L2), the clock, and CLOSED CANDIDATE LISTS built by code (today's cards with ids, the DRC's parsed trades with ids, the target note's addressable fields with ids, the tool list with argument schemas). No credential, env value or config secret ever enters the prompt (L4, L41): the prompt builder takes only whitelisted fields.
- It returns ONE typed `Plan` (Pydantic; a parse failure = FAILED turn, loud): `kind` (one of `answer`, `act`, `clarify`, `unsupported`, `refuse`), `tool` (a name from the allowlist), `args` whose every free value is a `Span` — a verbatim substring of the transcript, checked by code — or a candidate id from a closed list, and `say` (optional prose without figures).
- One model call per turn, through the model-access module (F3); the route is local first (`mainframe`, `/no_think`, F8); the same call shape can go to a second small local model if E4 says latency needs it (L23, L26 — assignment by measurement). [F-23] V1 builds the local lane only. Whether the Plan call carries any fallback is the routing lane's (L23/L25, frozen until the routing tribunal rules), configured in the model-access module, never in voice code: voice code names a ROUTE, never a provider or endpoint. Speech-to-text has no cloud engine (W4).
- The tool boundary: READ tools return data; the reply for a read is rendered by a code template from that data. ACT tools never write: each one is an ASK to the expert that owns the side effect (L38, L40) — vault writes through the owning module's function and `VaultWriter`, card state through `CardStore`, a DRC build through its own command. The voice module owns exactly one side effect: its own `voice_turns` rows. [F-22: WRONG FACT (grok WF5, read by the derive at proposal `:56`, `:89`, `:201`) — the voice module also writes and unlinks its scratch files (§5).] [R3F-04] It is their only deleter; the heartbeat's `voice_scratch` probe only counts them — the text of both R2-1 sides (§5). When the voice module sweeps is R2-1, his letter (`## FOR DEJAN` item 2).
- Figures: [F-05] Figures check: a numeric token in `say` (maximal run of digits and one decimal point) that is not a numeric token in the tool result is dropped and the code template is spoken. Per-character digits do not pass. Read tools return already-stored fields only. "size on <ticker>" reads the stored sizing row and does not call `POST /size` or the sizer. No voice tool computes a score, rank, grade, or size. A dictated grade is his value, parsed from a closed set, and is never written into a Cobalt unit and never as a line beginning `Grade:` or `Goal:`. (Proposal kept:) A value he dictates is parsed by a deterministic parser per field type (price, share count, time, date, grade from a closed set); the read-back speaks the PARSED value, so a mis-hearing is caught before it lands.
- HARD REFUSALS by code, whatever the Plan says: anything that places, changes or cancels an order or touches his trading platform (no such tool exists; `refuse` with a fixed sentence); any tool marked `trading_logic: true` in the registry (settings, rules, strategies, thresholds) is never executed by voice — it is drafted as the exact change + sha256 and sent to him as a HITL card over the existing outbound notify, and approved only where L7 says approvals happen today (the desk chat). This keeps L7 intact without an amendment. [R3F-11] Built in V5 (§9); before V5, `unsupported` with the owner's command named.

**2.5 Reply by voice.** The reply text is shown in the widget and spoken by the DEVICE's own speech synthesis (`speechSynthesis`, a `localService` voice only). No reply audio exists on the server at all. No local voice on a device → text only, with an AMBER "no local voice on this device" line (L9). A server-side local TTS engine (the requirement's named one) is a later slice only if E5 fails; if built it streams and writes no file.

**2.6 Confirmation of side effects by voice.** Every ACT produces a pending action: the owning expert's DRY-RUN result (the exact before → after for a vault write, the exact field change for a card), its `diff_sha256`, and a spoken read-back ("<field> in <note> for <date>: <before> → <after>. Say yes to do it.").
[F-08] While a row is `awaiting_confirm` and younger than `confirm_ttl_s`, the turn function makes no model call. The whole normalized transcript (Unicode casefold, strip) must equal the single confirm word `yes`, or he taps Confirm. The single cancel word is `no`. Any other transcript, `no`, or the TTL ends the pending action with nothing executed, and that transcript is not planned in the same turn. Widening either word waits on an E4 measurement that the added word never appears as a one-word transcript of a non-confirm in the test set. A confirm word in the same transcript as the request does not execute. One single-flight token: the first confirm or cancel commits; a second in-flight request finds no pending action. Execution re-computes the owning expert's diff and requires the same sha256. A reaped `executing` row is never retried.
[F-09] (c) the owning expert's re-computed TARGET still matches: the pending action stores `target_sha256 = sha256(target id ‖ the target span's bytes at read-back ‖ the after bytes)` (a unit id or a located region for a vault write; card id ‖ from_stop ‖ to_stop ‖ card state for a stop). At execution the expert recomputes it from a fresh read; a mismatch → REFUSED, the new before → after read aloud, re-confirm. A voice-confirmed write is executed with the writer's one retry DISABLED: a `NoteChangedOnDisk` ends the action as REFUSED, never a second attempt computed from bytes he did not hear.
Reads never ask for confirmation.

## 3. HOW EACH SPEECH FUNCTION MAPS ONTO IT

| Function (R18 "every speech function") | Tool (owner) | Target | Write class (§6) | Confirm |
|---|---|---|---|---|
| Per-trade answer (narrative about one trade) | `drc.voice.append` (DRC module → `VaultWriter`) | `drc-trades/voice-<trade_id>` | append-only into his voice unit (v2 `[F-01]`) | yes |
| Per-trade answer BEFORE the DRC exists (during the day) | same tool; the turn row holds `card_id` + text as `pending_landing` | lands at the build through ONE landing function `land_pending(date)` | append-only | yes (at capture; landing needs none — it lands what he confirmed) |
| Per-day block (his day fields) | `drc.voice.fill` / `append` | the DRC's day-level blank cells or his day voice unit `[F-14: on a trading day no day voice unit exists — see §6]` | blank-cell fill (2a) or append | yes |
| No-trade reason | `drc.voice.append` | `drc-day/voice-no-trades` | append-only | yes |
| DRC field edit ("set <field> on trade <n> to <value>") | `drc.voice.fill` | the resolved field | by field state (§6) | yes |
| DRC commands (build now, status, what is missing) | `drc.build` / `drc.status` (DRC module) | — | the command's own writes | build: yes; status: no |
| Card stop | [F-06] `cards.set_stop` → ONE function `set_card_stop(card_id, to_stop)` extracted from the route body `aset/web.py:1247-1257` (entry guard `_check_entry_allowed` `web.py:95`, open-card lookup, `Decimal` parse, `CardStore.record_stop_edit`); the `/card/{id}/stop` route and the voice tool both call it; the route's rendered output is unchanged. | an open card | DB (the store's own row) | yes |
| Questions ("what is on radar", "my open cards", "size on <ticker>") | read tools over the existing stores | — | none | no |
| Anything else | `unsupported` → "I can't do that yet" + the turn row marked `unsupported` (the desk reads the count as a backlog feed) | — | none | — |
| [F-11] Bind an unbound answer (R2-V5) at or after the DRC ("that answer goes to the second trade") | `drc.voice.bind` (voice module; lands through `land_pending`) | the pending turn → one trade of the closed list the build matched to that card | append-only | yes |

## 4. "WHICH FIELD IN WHICH FILE" — resolved by code, never guessed

1. **Which note.** `NoteRef(kind, date)`: `kind` is a closed enum (DRC, daily note, trade note; cards and radar are not files). The date is parsed by code from the transcript spans (today / yesterday / weekday / explicit date) against the session clock; the path comes from the existing path resolvers (`load_prefill_paths()` and the DRC's own) — never a path built by the model. (Weekday rule: `[F-10]`.)
2. **Which trade or card.** Candidates are enumerated by code: today's cards (`aset_sizings`) and, once the DRC exists, its parsed trades. The Plan's spans (ticker text, side, ordinal, entry time) are matched by code; the UI context (§2.1, as narrowed by `[F-10]`) narrows. Exactly one → bound. Zero or two-plus → `clarify`: the agent reads the candidates back by their code-rendered labels and waits. Never the nearest, never the earliest (v2 R2-V5 — this proposal takes the unbound side; binding at the DRC: `[F-11]`).
3. **Which field.** Code enumerates the ADDRESSABLE FIELDS of that note from the note itself, at request time: marker units by id, template labels (`<Label>:` lines and headings), blank cells, his voice units. The model picks one field id from that closed list; code checks it exists exactly once. The labels are read from his files at runtime, never committed (L32).
4. **Which write class.** Decided by code from the field's STATE (§6), never by the model.
5. **Which value.** A verbatim `Span`, parsed by the field type's deterministic parser; unparseable → `clarify`, never a guess. Free text lands verbatim.

## 5. THE EPHEMERAL-AUDIO LIFECYCLE (R18 (b))

- **Scratch path:** `scratch_dir` in `configs/cobalt/voice.yaml` — production value `/Users/cobalt/.cobalt/voice-scratch/`, dev value `/Users/cobalt/.cobalt-dev/voice-scratch/` (the committed default is the dev path, like `configs/dev/vault.yaml`'s dev default; production sets its own through the same explicit override pattern its launchd env already uses for the vault). The config schema REFUSES to load (L1, L10) when `scratch_dir` is relative, or sits under the repo root, under the resolved vault path, under `docs/`, or under any `backup.yaml` source (F11). Directory mode 0700, files 0600, name `<turn_id>.<ext>`.
- **Life:** written by the upload handler (the voice module's one file writer — not a vault write, not the DRC bytes method) → read by the Transcriber → **UNLINKED in a `finally:` right after the transcript row commits, or on any failure of the turn** — the deletion point. The audio is never needed again: every later step (plan, confirm, execute) runs from text. The row records `audio_deleted_at`. A failed transcribe keeps nothing: he says it again or types.
- **[R3-R2-1 side A — the Anthropic seat (`B`)]** **Crash leftovers:** The voice module sweeps: on `com.cobalt.aset` start and at the start of every turn it deletes scratch files older than `scratch_max_age_s` (AMBER line per file; a failed unlink RED). The heartbeat's `voice_scratch` probe only COUNTS such files and never deletes (L40 — the voice module owns its scratch). The config schema refuses `scratch_max_age_s ≤ stt_timeout_s`.
- **[R3-R2-1 side B — grok, gemini (`N1`)]** **Crash leftovers:** the voice module is the ONLY deleter of scratch files (L40): the turn's `finally:` unlink above, and on every `com.cobalt.aset` start, before the first request is served, a sweep that deletes EVERY file in `scratch_dir` — the upload handler is the directory's one writer and no turn of a new process is live, so any file present is a leftover; one AMBER line per file deleted (a turn died mid-way), an unlink that fails is RED (L9). One unlink function serves the turn and the sweep (L3). The heartbeat's `voice_scratch` probe (V4) only COUNTS: files older than `scratch_max_age_s` → AMBER with the count and the oldest age; none → OK; `scratch_dir` unreadable → RED unknown; it never deletes. The probe resolves `scratch_dir` through the voice config's one loader; the production override is carried in `ops/com.cobalt.heartbeat.plist` exactly as `COBALT_VAULT_PATH` is (`:20-21`) and in `ops/start_aset.sh` (`:32`), and the probe's detail line names the directory it read. The config schema refuses `scratch_max_age_s ≤ stt_timeout_s` (L10).
- HIS LETTER SELECTS ONE SIDE (## FOR DEJAN, item 2); the build reads only the side he selects.
- **Never in the database:** `voice_turns` has no bytes column; it keeps `audio_sha256`, byte length and duration only (dedupe of a repeated post, and audit), which are not a recording. A schema test asserts no `bytea` / large-object column on any voice table.
- **Never in git:** the scratch path is outside the repo by the config check above; a suite test fails if `git ls-files` lists any audio extension; tests SYNTHESIZE their audio at test time into `tmp_path` in the real container format E1 fixes (speech from the host's own synthesizer, tones for decoder tests) — never a recording of his voice, never a committed audio file (L45 real shape, L32).
- **Never in the vault:** no path under the vault is ever a scratch path (config check); the vault receives only text, through `VaultWriter`.

## 6. THE L28 PATH FOR VOICE-ORDERED EDITS

A voice-ordered edit of his notes is a Cobalt vault write (R18; L28 SCOPE binds Cobalt the program; L65 is desk-only). Each write class, by the target field's state:

| Field state (code decides) | Op | L28 basis |
|---|---|---|
| His voice unit (`drc-trades/voice-<id>`, `drc-day/voice-no-trades`, a day voice unit) | `append_to_unit` — idempotent on the turn id, suffixes the bytes it read under the mtime guard or refuses, never merges, never takes the sync-revert win (v2 `[F-01]`, `[F-18]`) | append of a marked unit Cobalt created; his bytes unchanged |
| A BLANK template cell / bullet outside markers | [F-13] Blank cells outside markers are filled only by `upsert_region` with `blank_only=true` (new flag, default false, about 15 lines in `vaultwrite/writer.py` plus tests, slice V2/V3, no second writer). `blank_only` writes only when the located span is empty or whitespace, and it does not take the sync-revert win; a non-empty span is refused as the O1 class and is not merged. | clause 2a |

The Cobalt-owned-unit row (R2-2's `§6:` line):

**[R3-R2-2 side A — the Anthropic seat (`S`)]**

| Field state (code decides) | Op | L28 basis |
|---|---|---|
| A Cobalt-owned unit | on his confirmed read-back (SCOPE-R39): the O1 span op — the same op as his own text: replaces only the confirmed span inside the unit body, single attempt, under the mtime guard and `_session_gate`, never `merge3`, never `upsert_unit` (which would record his bytes as the producer's `unit_after` baseline, `writer.py:766`); versioning row with before, after, `unit_before` / `unit_after` = the span bytes and the turn id, keyed by a section label no producer writes, so `last_after` never returns it (`store.py:102-104`) and `restore` still locates it by content (`writer.py:1145-1162, :1020-1038`). For a computed value, the reply also names that value's own correction path (R90 resolve action / A28, v2 §2) as the lasting fix, because the unit's producer rewrites the unit. | L28 as amended (O1, R39): his confirmed bytes are his — the producer's next `upsert_unit` merges against its own last `unit_after`, the human wins and one `vault_overrides` row is logged (`merge.py:18-24`) |

**[R3-R2-2 side B — gemini (`N2`)]**

| Field state (code decides) | Op | L28 basis |
|---|---|---|
| A Cobalt-owned unit | voice edit via `upsert_region` recording no merge baseline | numbers are code; human-wins untouched |

**[R3-R2-2 side C — grok (NEITHER)]**

| Field state (code decides) | Op | L28 basis |
|---|---|---|
| A Cobalt-owned unit | the one confirmed span-replace: `build` refuses unless the span equals the confirmed before bytes, then writes the confirmed after bytes, no `merge3`, no `unit_after` that `last_after` would return | a Cobalt line he changed is his against the baseline already on record — the next write human-wins and logs an override (L28). `last_after` None stays the existing `baseline_missing` path |

HIS LETTER SELECTS ONE SIDE (## FOR DEJAN, item 3); the build reads only the side he selects.

| Field state (code decides) | Op | L28 basis |
|---|---|---|
| HIS NON-BLANK TEXT outside markers | [R3F-08] O1 RULED B (R39): writable on his confirmed read-back by the voice-ordered edit op that the `FOLD:` text of his letter describes (`## FOR DEJAN`, item 3) — the same op as the Cobalt-owned-unit row of that side (SCOPE-R39: "his own text, his voice units and Cobalt's own units alike"). Until the desk folds the L28 amendment at his approval of this FINAL (L58), L28 stands unchanged and this class is refused aloud, naming the field and why | L28 as amended by O1 (R39) at his approval — the `FOLD:` text of his letter |
| A trading-logic field | never executed by voice (§2.4), HITL card | L7 |

[F-14] On a trading day D3 creates no day-level voice unit (`50-drc-d3-build.md:10` creates `drc-day/voice-no-trades` on no-trade days only); until a DRC FINAL change adds one, per-day speech on a trading day lands only in blank template cells.

Every write: `_session_gate` (refused inside `market_reset`, spoken as such), versioned to Postgres with the unified diff, the `vault_writes` id stored on the turn row, atomic write + mtime guard, and the confirm-time sha256 check (§2.6). Pre-DRC landing: ONE landing function `land_pending(date)` (v2 R2-V1, the single-path side): the DRC build creates his voice unit BLANK exactly as D3 does today and then calls `land_pending`; the widget's confirm calls the same function when the unit already exists. One landing writer (L3).

## 7. FAILURE MODES AND THEIR LOUD STATES (L1, L9, L18)

Turn state machine on `voice_turns`: `received → transcribing → planned → (answered | awaiting_confirm → executing) → done | failed | cancelled | expired | unsupported`. A row still `transcribing` / `executing` past its limit is reaped to `failed: <class>` (v2 `[F-02]`).
[F-15] The state machine stands, plus: a row still `planned` past its limit is reaped to `failed` and executes nothing; `awaiting_confirm` ends only by confirm, cancel, or TTL; a reaped `executing` row is not retried. Empty transcript, dead STT, dead model, bad Plan, ambiguity, sha mismatch, `market_reset`, O1 refusal, and scratch AMBER/RED stand as in §7.
[F-16] `voice_turns` writes are NOT session-gated (as `cobalt_jobs`, `jobs/store.py:12-18`): a turn row is the voice module's own state, not trading record. Inside `market_reset` a read turn is answered; every ACT is refused by its owning expert's own gate (`VaultWriter._session_gate`, `writer.py:387-416`; `record_stop_edit`'s `assert_writable`, `cards/store.py:659`).

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

One turn function, three callers, no per-house gate: the widget route `POST /voice/turn`, the CLI `cobalt voice turn --audio <file> | --text "<text>" [--confirm <turn_id>] [--dry-run]`, and the tests. [F-02] Any house holding a build or check seat runs the same path in DEV (NN#16) with synthetic audio or text; `--dry-run` prints the Plan, the resolution and the exact diff with no write. The CLI's `--confirm <turn_id>` is refused when `COBALT_ENV=production` (named refusal, exit non-zero): in production an ACT is confirmed only by the widget — a tap, or his next spoken or typed turn in the same widget session. No house, the desk included, confirms a production act (L37). Production is reached only through deploys, as for every other path.

## 9. SLICE PLAN

Seats: Opus 5 floor on every write-path chunk, never auto mode on a write path (L29); each build checked by ≥3 tribunal members (L67 as amended R46). Hours are seat hours, a GUESS until the builders re-derive them.

| Slice | What runs end to end | Write path | Migration | Depends on | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| **V1 — first conversation** (the smallest end-to-end conversation that runs a real command) | widget + text box on the ASET pages; `/voice/turn`; scratch lifecycle + sweep; Transcriber (faster-whisper); the model-access call (F2/F3 — see seam S1); Plan + resolver for cards; read tools (open cards, radar pool, a card's numbers — code-rendered); ONE confirmed act: **card stop** via `CardStore.record_stop_edit` (through `set_card_stop`, `[F-06]`); device TTS; CLI; `voice_turns`; degraded banner | DB (`voice_turns`; the card store's own row) | ONE (`"user".voice_turns`; number: the desk's at L68 — `[F-17]`) | `[F-17]` E1–E8, E10; plus X1, X3, X5, X12, X13 (First-gate experiments); [R3F-15] plus G2 / K5 and X22 (= hub H1) | `com.cobalt.aset` | 9 |
| **V2 — DRC by voice** | per-trade answer (append + `land_pending`), no-trade reason, per-day block (blank cells + his day units), DRC field fill, `drc.build` / `drc.status`; `append_to_unit` (new `VaultWriter` op); `drc.voice.bind` (`[F-11]`); `upsert_region` `blank_only` (`[F-13]`) | vault | — | DRC D2 + D3 merged (voice units exist); E9, E11; X2, X4 | `com.cobalt.aset` | 7 |
| **V3 — any note field** | field enumeration for the daily note and trade notes; blank-cell fills; [R3F-12] the voice-ordered edit class — O1 RULED B (R39): any field of any note, on his confirmed read-back, by the op of the R2-2 side his letter selects (§6; `## FOR DEJAN` item 3) | vault | — | V2; O1 RULED B (R39) — the class switches on only after the desk folds the L28 amendment at his approval (L58); X21, X23 (= hub H2) | `com.cobalt.aset` | 5 (4 + 1: the O1 op, +1 h under every R2-2 side) |

V4 row (R2-1's `V4:` line):

**[R3-R2-1 side A — the Anthropic seat (`B`)]**

| Slice | What runs end to end | Write path | Migration | Depends on | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| **V4 — ops** | `voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s` in the `scratch_dir` it resolves through the voice config's one loader, and names that directory in its detail line: some → AMBER with the count and the oldest age, none → OK, unreadable → RED unknown; it never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist` (as `COBALT_VAULT_PATH`, `:20-21`); model-fetch deploy step; the `tailscale serve` deploy step (§11 W6); DevDocs | no (probes read) | — | V1 | `com.cobalt.heartbeat` (plist in the diff → reload, L42; a 900 s one-shot job, `heartbeat.plist:60-61`) | 2 |

**[R3-R2-1 side B — grok, gemini (`N1`); gemini's line, the shorter of the two houses' — grok's spells out its "…" as "model-fetch deploy step; the `tailscale serve` deploy step (§11 W6); DevDocs"]**

| Slice | What runs end to end | Write path | Migration | Depends on | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| **V4 — ops** | `voice_stt` / `voice_plan` / `voice_scratch` probes (`voice_scratch` COUNTS files older than `scratch_max_age_s`, never deletes — §5); the production `scratch_dir` override in `ops/com.cobalt.heartbeat.plist`; … | no (probes read) | — | V1 | `com.cobalt.heartbeat` reload (plist in the diff, L42) | 2 |

HIS LETTER SELECTS ONE SIDE (## FOR DEJAN, item 2); the build reads only the side he selects.

V5 row [R3F-10] (R2-3, converged — ADOPT A-V5; grok's `§9:` line, identical in gemini's and the Anthropic seat's):

| Slice | What runs end to end | Write path | Migration | Depends on | RESTARTS (L42, derived at build) | h |
|---|---|---|---|---|---|---|
| **V5 — trading-logic drafts** | `trading_logic: true` registry tools for the `--card` / `--optional` settings keys; owner-drafted file in `data/voice-drafts/` + sha256 + per-key diff; `send_dm` card with the owner's exact apply command; applied only by `cobalt settings load … --sha256 … --apply` (his hand, or the desk on his L7 approve) | no (a gitignored draft file; the owner's own apply is unchanged) | — | V1 | `com.cobalt.aset` (+ residents importing `cobalt.settings`, AST walk) | 4 |

**[R3F-13] Total 27 h seats (9+7+5+2+4), ≈ 38 h with one fix round each (27 × 1.4 = 37.8; factor ×1.4, UNVERIFIED as in v2 §7) — the same under every side of R2-1 and R2-2. GUESS / UNVERIFIED.** The hours 22 and 31 in `[F-17]` below are superseded by this line.
[F-17] V1 is the smallest end-to-end conversation that runs a real command: the existing human-fed card stop (`22-aset.excerpt.py` `web.py:1239-1273`), not a vault write and not a DRC write. V1 depends on E1–E8 and E10. E9 and E11 stay V2. The one migration is `"user".voice_turns`, number assigned by the desk at L68, and it is not 0012 or 0013: those numbers are already claimed off main (`02-greps.txt.part2:67-72`) while FORWARD's last file on this tree is 0011 (`24-migrations.excerpt.py`). RESTARTS `com.cobalt.aset` for V1–V3 and the heartbeat resident for V4. Hours 22 and 31 are GUESS / UNVERIFIED, not facts. V1 ships in an evening deploy only after those experiments and the S1 seam; V2 ships only after DRC D2 and D3 are merged.

## 10. EXPERIMENTS OWED — measured on his devices (L70)

Moved whole to `## First-gate experiments (L70)` below (the proposal's E1–E11 with the seats' changes, plus the new X rows), each placed before the slice it gates.

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
| W11 who reaches the route | [F-03] `/voice/*` allows a request only from the socket peer address. Loopback is allowed. The peer address E8 records for `tailscale serve` is allowed. Any other peer, including a LAN address, is a named 403. A header the client can set is never the allow key. `tailscale serve` is a tailnet-only HTTPS front of the existing ASET port, not a second app. The upload handler reads the file part as bytes; a zero-byte or non-file part FAILs. It never uses the `str(v)` form idiom. | F7, E8 |
| W12 his clips in git | none; synthetic audio generated at test time | R18 (b) |

## 12. WHAT v3 KEEPS FROM v2, AND WHAT IT SUPERSEDES

| v2 clause | v3 |
|---|---|
| §5 Transcriber interface, faster-whisper first, Metal by measurement `[F-03]`, `model_dir` pinned offline `[F-08]`, off-loop `[F-02]` reap | KEPT |
| `[F-19]` bytes read from `UploadFile`, zero-byte FAIL, empty transcript lands nothing | KEPT |
| `[F-01]` idempotent `append_to_unit`; `[F-18]` no sync-revert win | KEPT (now for every his-voice unit) |
| T-V7 verbatim only for narrative | KEPT for narrative answers; a field edit is his explicit order, parsed by code |
| R2-V1 (initial body vs one landing function) | SETTLED here by the proposer on the single-path side (`land_pending`), for this tribunal to rule |
| R2-V5 (>1 trade per card) | [F-11] SETTLED: unbound at the build when >1 trade matches the card; listed on A31; bound later only by his `drc.voice.bind` turn against the matched trades; never nearest, never earliest. |
| §3 binding "never by speech" | SUPERSEDED: speech resolved by code against closed candidate lists (§4) — R18 "knowing which field in which file … by my word" |
| §6 audio in the R92 imports dir, `drc_voice` holding audio path + sha as the stored input, `[F-15]` audio through D2-2's bytes method, `[F-16]` "no transcript without audio" | SUPERSEDED by R18 (b) and L57 set aside; the D2 bytes method carries no voice |
| W1–W12 as owner items; V-E2 on his clips | SUPERSEDED (§11; E2 on synthetic speech) |
| Seam entries 1, 2, 4, 5 (D3 unit creation, `append_to_unit`, A31 line in D5-3, the `orphaned` edge-insert) | [F-19] W1–W12 stay settled by the houses as in §11, none sent to him. Seam kept: entry 2 (`append_to_unit` on `VaultWriter`, stacked on D2-2, not a second writer), entry 4 (D5-3 renders `voice not bound` from `voice_turns`; the voice route does not write `drc-day/open_items`), entry 5 (D3's idempotent `orphaned` edge-insert). Entry 1 is kept only as create-once blank plus `skip_if`; "the first body may contain blocks" is superseded by `land_pending`. Entry 3 (`voice/` under D2-2) is void. v2 round 2 and v2 `## FOR DEJAN` are not run and not sent. |

## 13. SEAM (L72 P-b) — one document both lanes cite before either launches

Moved to `## Seam` below (S1, S2 as the rulings leave them). Shared files (proposal kept): `aset/web.py` (routes, the widget partial, `set_card_stop` `[F-06]`), `vaultwrite/writer.py` (`append_to_unit`; `upsert_region` `blank_only` `[F-13]`), `drc/build.py`, `db_migrations/placement.py`, `heartbeat/probes.py`.

## 14. L52 / L7 / THE BAR

Re-answered under `## L52 and the bar` below. The proposal's first sentence ("Reaches scoring: NO — nothing computes a score, rank, grade or size") is REPLACED by `[F-26]` there: hub C8 / FC4 found `record_stop_edit` recomputes `shares` (`cards/store.py:668-674`).

## First-gate experiments (L70)

Run before the slice they gate, in dev; his hands only where a device is his (the phone's microphone prompt, once). Proposal's own UNPROVEN rows F12 (`MediaRecorder` / secure context / `speechSynthesis`) and F13 (phone containers without ffmpeg) are these experiments (E1, E5, E8; E2, E3) — never defects. [R3F-14] Round-2 and round-3 runs are merged into the row they repeat and attributed; the new ones are added before the slice they gate.

**Before V1**

| # | What (where) | Result that changes the design | Changes folded |
|---|---|---|---|
| E1 | his Android phone, the trading-PC browser and the Mac: the widget page over `tailscale serve` HTTPS — `MediaRecorder` available? which container / codec? a plain-http page as control; does the trading PC have a microphone | no recorder over tailnet HTTPS → W6 re-opens; the container list fixes the handler and the synthetic fixtures | — |
| E2 | STT on the Mac Studio: faster-whisper sizes vs Metal comparators on SYNTHETIC speech in E1's containers carrying the words the desk uses (setup names, exit words, card-style tickers generated, not his) — word accuracy, latency, RSS beside LM Studio's 88 GB wired limit; same output twice | picks engine + size; a Metal winner needs its named deploy step (v2 `[F-03]`) | grok: "E2 KEEP. Synthetic speech only, in E1's containers, on the Mac Studio, RSS beside the 88 GB wired limit. A Metal winner needs its own deploy step. If RSS beside mainframe is not measured, the engine stays CPU faster-whisper." |
| E3 | decode E1's real phone files with the chosen engine and no system ffmpeg | fail → ffmpeg becomes a named host dependency (v2 `[F-03]`) | — |
| E4 | the Plan call on `mainframe` with `/no_think`: parse-valid rate and latency over a constructed utterance set (every §3 function, ambiguous and hostile cases, a trade-execution request); same on a second small local model beside it | parse-valid rate too low → tighter schema / fewer candidates; latency → second small model (L23 route by measurement) | grok: "E4 KEEP, plus: the set includes a trade-order utterance, a one-word `yes`, and a think-wrapped reply. A think-wrapped reply must FAIL the turn, not execute. Parse-valid rate too low → tighter schema, not a tool loop. Latency → a second small local model inside the same module, or not." · Anthropic seat: "E4 (changed): the Plan call on `mainframe` with `/no_think` over the constructed set, run ALSO while another client holds the local model (e.g. a Qwen Code seat mid-generation). Result that changes the design: queueing latency beyond `stt_timeout_s` + the Plan budget → the second small local model (F8, L23 by measurement) becomes V1a, not later." [derive note: V1a is not adopted (`[F-18]`); the slice it names is V1] |
| E5 | `speechSynthesis` on his phone and the trading-PC browser: `localService` voices present? speaks inside the page? | none local → text-only on that device + server local TTS slice | — |
| E6 | `/fill` and `/size` latency while a turn transcribes (v2 X2, V-E5) | stall → the Transcriber moves to a one-shot job of the same function | Anthropic seat: "E6 (changed): `/size` and `/fill` latency on a dev ASET server while (i) a transcribe runs and (ii) a Plan call is in flight. Result: either stalls → that call moves off the loop (T3), or the Transcriber becomes a one-shot of the same function." |
| E7 | `kill -9` of `com.cobalt.aset` mid-transcribe and mid-execute | row not reaped to `failed`, or scratch file survives the sweep → lifecycle fix before ship | grok: "E7 KEEP, plus: `kill -9` after `record_stop_edit` has committed and before `done`. Restart must leave the stop at the new value once, and must not apply it again." · [R3F-14] E7 sharpening (the Anthropic seat, round 2; cited by grok, gemini and the seat in round 3; hub r3 `## Experiments named`): "`kill -9` `com.cobalt.aset` LESS than `scratch_max_age_s` after the upload, no later turn" — result that changes the design: "the file survives the start sweep → the sweep is age-gated, contrary to N1"; the launchd respawn delay after `kill -9` is behaviour, not read (hub C9, GK1: no `ThrottleInterval` key) |
| E8 | `tailscale serve` in front of the loopback port: the source address and headers the route sees; a LAN client's request to `/voice/turn` | the tailnet-only check (§11 W11) keys on what this shows | grok: "E8 CHANGE. Record the socket peer for loopback, for `tailscale serve`, and for a LAN client. The allow key is that peer, unless the run shows a header the client cannot supply. A client-supplied `X-Forwarded-For: 127.0.0.1` from the LAN must be 403." |
| E10 | scratch worktree `uv add faster-whisper` → full lock diff with licences (v2 X8); offline model load and a missing model file (v2 X7) | an unexpected native / GPL package → tribunal round 2 | — |
| X1 | (Anthropic seat) "on the home server, the chosen engine/size over 50 synthetic clips of silence, breath, cough, keyboard and room noise (generated at test time), plus 20 short non-confirm words. Count transcripts that normalize to a confirm-list word." | "Any > 0 → a spoken confirm also needs the engine's no-speech / low-confidence fields under a tunable, or ACTs on a card become tap-only." | new |
| X3 | (Anthropic seat) "dev ASET behind `tailscale serve` on the Mac: log `request.client.host` and the forwarded headers for a phone request, a Mac-browser `http://127.0.0.1` request and a LAN-client request (if bind `lan`)." | "fixes W11's check (loopback vs tailnet address vs header). A LAN client indistinguishable from the proxy → the `/voice/*` gate needs the tailnet identity header, or production stays `loopback` + serve only." | new (run with E8) |
| X5 | (Anthropic seat) "synthetic speech of price / share / time utterances in several spoken forms (with and without \"point\", with and without a time-like reading), through the chosen engine, then the field parsers." | "the share of clarifies per field type. A price transcribed as a clock time and parsed as a price would be a wrong value → that parser must refuse `H:MM` shapes." | new |
| X12 | (grok) "On cobalt_dev, deterministic price parser only, synthetic text \"four fifty\" and \"4.50\"." | "Same decimal → the parser accepts spoken numbers; otherwise clarify. No model in this run." | new |
| X13 | (grok) "On cobalt_dev, one pending stop edit, two in-flight requests (tap Confirm and transcript `no`)." | "The stop changes at most once, and the row is not both `done` and `cancelled`." | new |
| G2 / K5 | [R3F-14] (round-2 hub G2 / K5; cited by grok in round 3) a sweep firing while a long synthetic clip transcribes, age key ≤ STT-timeout key | the file is unlinked under the Transcriber (gates the V1 config check `scratch_max_age_s ≤ stt_timeout_s`) | round 2, NEW then |
| X20 | [R3F-14] (the Anthropic seat, round 2; cited by grok and the seat in round 3) unlink mid-transcribe | informational: transcript fails or completes; would set the cost of an out-of-process deleter; gates nothing | round 2 |
| X22 | [R3F-14] (the Anthropic seat, round 3, `…fable-r3…:108`; = hub r3 H1, hub-noted) "on the home server, with a throwaway launchd job shaped like `ops/com.cobalt.aset.plist` (`AbandonProcessGroup` true, `KeepAlive` true, ProgramArguments → a script that ends `exec uv run python -m <a stub that binds a port and sleeps>`), `kill -9` the PID launchd reports. Does the python child survive, still holding the port, while launchd respawns? Repeat with a second instance started by hand." · hub H1: "`kill -9` the pid of `com.cobalt.aset` on the home server, then list processes for a surviving `python -m cobalt.aset` child" | seat: "the child survives → a delete-ALL start sweep deletes a live turn's audio (N1 unsafe, B's age gate required)" · hub: "a surviving child that serves turns → a start sweep can delete a live turn's file". Gates V1's start sweep under R2-1 side B; bears on side A only as ops (an orphan on :5010 keeps `sheet_http` GREEN) | new, round 3 |

**Before V2**

| # | What (where) | Result that changes the design | Changes folded |
|---|---|---|---|
| E9 | dev vault: `append_to_unit` and `land_pending` twice; a crash between commit and row update; his edit during an append; an Obsidian Sync revert; a call in `market_reset` (v2 V-E4, X3, X4) | any double block or changed byte of his → op fixed before V2 ships | grok: "E9 KEEP. Dev vault: `append_to_unit` and `land_pending` twice; crash between vault commit and row update; his edit during append; Obsidian Sync revert; `blank_only` refuse on a non-empty span; a call in `market_reset`. Any double block or any changed byte of his → the op is fixed before V2 ships." |
| E11 | re-import a superseding log leaving one trade unchanged: identical `trade_id`? (v2 X9) | not identical → the seam fixes the id rule before V2 | — |
| X2 | (Anthropic seat) "dev vault, a test with `_precommit_hook` (`writer.py:461-462`) writing text into the target blank cell between snapshot and commit." | "Pass: REFUSED, file byte-identical to the hook's write. As written today (no predicate, one retry) the expected result is an overwrite. The test proves T9's fix." [derive note: the T9 fix folded is grok's `blank_only` `[F-13]` with the retry disabled `[F-09]`] | new · [R3F-14] = round-2 K10 (grok: "My round-2 K10 stands only if the check runs once, outside `build` (X2)") |
| X4 | (Anthropic seat) "dev vault, land a block, kill between `os.replace` and the `vault_writes` commit (hook), delete the block's turn-id line by hand, then retry `land_pending`." | "a second block → the marker needs a second form (e.g. hash of the block bytes) or the unit gets a Cobalt-owned ledger line." | new |

**Before V3** [R3F-14]

| # | What (where) | Result that changes the design | Changes folded |
|---|---|---|---|
| X21 | (the Anthropic seat, round 2: the O1 op writes no merge baseline; = round-2 hub C6 / K12 NEW run) · grok's round-3 sharpening (`grok-ruling-r3.md:81`): "Pass: the voice row is not what `last_after` returns for that unit; disk is the confirmed after bytes; a following upsert against a live baseline keeps those bytes and writes one `vault_overrides` row." · the Anthropic seat's round-3 sharpening (`…fable-r3…:110`): "add `cobalt vault restore <id>` of the O1 row. Pass: the span's before bytes come back, located by content (`writer.py:1145-1162`), and `last_after(note, <producer section>, <unit>)` is unchanged by both writes." | grok: "Fail: the confirm itself leaves the span unchanged and logs an override (merge kept the hand edit), or the voice row's `unit_after` equals the after bytes." · hub r3: "a merged span or a returnable baseline → the op merges, contrary to the fold text" | round 2; both round-3 sharpenings attributed, neither merged into the other |
| X23 | (the Anthropic seat, round 3, `…fable-r3…:109`; = hub r3 H2, hub-noted) "dev vault + `cobalt_dev`. A Cobalt unit written by `upsert_unit`; the O1 span op writes a confirmed edit of one line in it; the producer's `upsert_unit` runs twice with a new value on that line." · hub H2: "on the dev vault + `cobalt_dev`, a confirmed voice edit into a Cobalt-owned unit, then TWO Cobalt writes of that unit" | seat: "Expected from the code (`merge.py:14-24`; `writer.py:766, :771-773`): write 1 keeps his line and logs one `vault_overrides` row; write 2 applies the producer's value with no override. Other result → §6's L28 basis and its reply note change." · hub: "whether his confirmed bytes survive the second Cobalt write" (bears on GM11 / GK11) | new, round 3 |

## Seam

**S1 — model access (L72 P-b, L3).** As the rulings leave it (proposal §13 kept; grok (c), gemini (c), Anthropic seat (c) all rule it lawful): the new core has no model caller (F2, hub C3 — `radar/audit_export.py` is prose, not a caller). V1 needs one call. The seam document names ONE module (`src/cobalt/modelaccess/` or whatever name the routing lane rules) that V1 creates with the local lane only and the routing build extends — never a second copy (L3). `litellm` is already a direct dependency (`pyproject.toml:16`, `[F-20]`). Fallback, if any, is the routing lane's, configured in that module, never in voice code (`[F-23]`). **Fact, not a ruling: which lane creates the module first is the desk's ordering; the seam document is a precondition before V1's build prompt** (grok closing line; Anthropic seat ESCALATE 2; hub blocker 1).

**S2 — DRC (a change to the DRC FINAL, carried, never folded here).** What this design needs, from which DRC chunk, and when:
- From D3 (`50-drc-d3-build.md`), before V2: after create-once of `drc-trades/voice-<trade_id>` and `drc-day/voice-no-trades`, call `land_pending(date)`; keep the `orphaned` edge-insert (grok (d); Anthropic seat (d)(a); gemini (d)).
- From D5-3 (`52-drc-d5-build.md:21`), before V2: `drc-day/open_items` also renders `voice not bound` from `voice_turns` (grok (d); seat (d)(b); gemini (d)). D5 excludes voice today (`52:26`).
- From D3, before V2: D3 persists each trade's matched card id where `land_pending` reads it (Anthropic seat (d)(c), citing `DRC-AUTOMATION-v2-2026-09-22.md:117`; UNCHECKED by a hub).
- Optional, Anthropic seat (d)(d): a day-level voice unit on TRADING days; absent it, `[F-14]` stands.
- D2-2's bytes method stays import bytes only; no `voice/` prefix (grok (d); proposal §12).
None of these is in the DRC build prompts today (D3 and D5 both say voice is not in that chunk, R100). The desk places them in the DRC FINAL / its re-issue.

## Dissents, verbatim

No house issued a `REJECT` or `DO NOT BUILD` in round 1, round 2 or round 3 (round 2: grok `TRIBUNAL R2: BUILD`, gemini `TRIBUNAL R2: BUILD`; round 3: grok `TRIBUNAL R3: BUILD`, gemini `TRIBUNAL R3: BUILD`, the Anthropic seat `TRIBUNAL R3: BUILD`).

**Round 1.**

Not followed — `RE-OPENS A RULING (R18)`:
- Anthropic seat, T4 (2): "Replace §2.4's HARD REFUSALS second clause with: \"any request that would change trading logic (settings, rules, strategies, setup definitions, thresholds) is `refuse`d aloud with a fixed sentence naming L7 until a slice builds the HITL-card tool; no V1–V3 tool writes `trader_settings`, `configs/`, rules, strategies or setup definitions.\"" — not folded: it would limit voice below R18 (a)'s "any command"; the gap it names is R2-3.

Not followed — supporting claim DOES NOT HOLD (hub C1, C2):
- Grok, (a) F2: "DOES NOT HOLD as proven. The staged search is `litellm` OR `chat/completions` OR `openai` under `src`, and it lists `src/cobalt/radar/audit_export.py` (`02-greps.txt.part1:9-10`). The proposal's \"none under `src/cobalt`\" (`10-PROPOSAL.md:17`) does not account for that file." Closing condition "class audit_export": classed by the hub — not a model caller (C1, C3).
- Gemini, (a) F2: "DOES NOT HOLD — `10-PROPOSAL.md:17` (missed `src/cobalt/radar/audit_export.py` which contains a model caller)." Closing condition "F2 IS CORRECTED TO ACKNOWLEDGE AUDIT_EXPORT": met by `[F-21]` as a file-checked note; F2 itself HOLDS (C3).

Not followed — premise DOES NOT HOLD as literally stated (hub C8):
- Grok, (f): "Nothing here computes or changes a score, rank, grade, or size if T4's read-tool wording holds. … L52 does not bind."
- Gemini, (f): "Nothing computes a score, rank, grade, or size. The card stop edit acts identically to the manual page edit, calling `CardStore.record_stop_edit` correctly behind the `_check_entry_allowed()` gate."

Superseded by R39 (O1's scope is his words) — the round-1 fold texts, moved here from `## OWNER ITEMS`:
- Proposal's fold text (scope A), as written: "[amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text outside marker units — his text included — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that one diff; the write is the smallest span (that field's value), goes through `VaultWriter` with the mtime guard and `_session_gate`, is versioned with before and after and the turn id, and is refused if the note changed since the read-back. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."
- Anthropic seat's fold text (scope B), as written: "[amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."

**Round 2.**

Superseded by R39 — the round-2 FOLD A / FOLD B texts (each pair differs only in the scope clause):
- grok, ADOPT S, FOLD A (`r2/grok-ruling-r2.md:33`): "FOLD A: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text outside marker units — his text included — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."
- grok, ADOPT S, FOLD B (`r2/grok-ruling-r2.md:34`): "FOLD B: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."
- gemini, ADOPT P, FOLD A (`r2/gemini-ruling-r2.md:15`): "FOLD A: Cobalt may replace text outside marker units — his text included — when he orders that exact edit by voice and confirms it: his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that one diff; the write is the smallest span (that field's value), goes through `VaultWriter` with the mtime guard and `_session_gate`, is versioned with before and after and the turn id, and is refused if the note changed since the read-back."
- gemini, ADOPT P, FOLD B (`r2/gemini-ruling-r2.md:16`): "FOLD B: Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — when he orders that exact edit by voice and confirms it: his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that one diff; the write is the smallest span (that field's value), goes through `VaultWriter` with the mtime guard and `_session_gate`, is versioned with before and after and the turn id, and is refused if the note changed since the read-back."
- the Anthropic seat, NEITHER (N2), FOLD A (`voice-v3-tribunal-fable-r2-2026-09-23.md:53`): "FOLD A: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text outside marker units — his text included — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write goes through `VaultWriter` with the mtime guard and `_session_gate`, replaces only that span with the confirmed after bytes — never a three-way merge — and is refused if, when the writer reads the note to write, the span no longer equals the confirmed before bytes; it is versioned with before, after and the turn id, and records no merge baseline: the replaced text remains his, and every later write treats it as his. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."
- the Anthropic seat, NEITHER (N2), FOLD B (`voice-v3-tribunal-fable-r2-2026-09-23.md:55`): "FOLD B: [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write goes through `VaultWriter` with the mtime guard and `_session_gate`, replaces only that span with the confirmed after bytes — never a three-way merge — and is refused if, when the writer reads the note to write, the span no longer equals the confirmed before bytes; it is versioned with before, after and the turn id, and records no merge baseline: the replaced text remains his, and every later write treats it as his. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes."

Not followed — round-2 answers no round-3 seat holds:
- gemini, round 2, R2-2, ADOPT P (its FOLD lines above); supporting claims G4, G5 DO NOT HOLD as worded (round-2 hub). Gemini moved to ADOPT N2 in round 3.
- grok, round 2, R2-3, ADOPT B: "§2.4 stands with no slice. The design builds no trading-logic tool in V1–V4, and the paragraph describes a later slice." Grok's text on what a request gets (`r2/grok-ruling-r2.md:41`): "In V1–V4 the Plan kind is `unsupported` (`:68`), not `refuse`. At 10:41 \"set my max risk to [user data: grok-ruling-r2.md:41]\" the spoken line names the setting and the hand gate that already exists, `cobalt settings load --card <file> --sha256 <hash> --apply` (`settings/card.py:10-20`; trader-run apply is token-exempt at `:15`). It does not say the class is forbidden and does not name L7 as a ban." Grok moved to ADOPT A-V5 in round 3.
- gemini, round 2, R2-3, ADOPT A (V1) (`r2/gemini-ruling-r2.md:20`): "Slice V1 builds it. Targets: `trader_settings`; the tool drafts a JSON artifact carrying the new values and target sha256, sending a HITL card via `notify/mattermost.py` `send_dm`; upon his 'approve' in the desk chat, the existing chat bot executes the trader-run settings apply under `settings/card.py` (which is exempt from the token). Files: `cobalt/settings/propose.py`, `cobalt/aset/voice_tools.py`; Hours: 12; RESTARTS: `com.cobalt.aset` and desk chat bot. Before V1 ships, the voice agent is not live, so no request is refused." — supporting claim G10 DOES NOT HOLD as worded; G11 NOTE. Gemini moved to ADOPT A-V5 in round 3.

**Round 3.** Every round-3 answer stands in place: R2-3's three answers converged (`[R3F-09]`); R2-1's and R2-2's answers are the lettered sides above (`## FOR DEJAN` items 2 and 3). No round-3 answer re-opens a ruling; no house closed `DO NOT BUILD`.

**Withdrawn by the Anthropic seat — never folded** (`voice-v3-tribunal-fable-r3-2026-09-23.md:97-103`; round-2 withdrawals: that seat's round-2 report and the second derive's `## NEEDS ROUND 3`):
- W1 (R2-1): "the upload handler is the directory's one writer and no turn of a new process is live, so any file present is a leftover" (`voice-v3-tribunal-fable-r2-2026-09-23.md:26`), offered as proof that delete-ALL is safe. — Both houses hold this sentence in round 3 as their own text (R2-1 side B); it stands there only as a side he may pick (`## FOR DEJAN` item 2).
- W2 (R2-1): "(its only residue — an unlink that already failed RED — fails again the same way)" (`…fable-r2…:22`).
- W3 (R2-2): "P states none of the three; S states the first two and the third vaguely" (`…fable-r2…:50`) and "S's vague wording does not close it" (`:51`).
- W4 (R2-2): "The versioning row then carries before/after with no (section, unit) key that `last_after` reads — as `create_if_absent`'s row does (`writer.py:603-604`, `section=None, unit=None`)" (`…fable-r2…:49`), and its price "versioning row with no unit key" (`:51`).
- W5 (R2-3): "`aset/config.py`, `radar/evaluate.py` touch it → `com.cobalt.radar` unless the walk proves otherwise" (`…fable-r2…:72`).
- Round 2: "takes no retry" as law text, and its round-1 description of "remains his" (R2-2); "refuse … naming L7" for `trader_settings` (R2-3).

## L52 and the bar

[F-26] Reaches the card: YES, by one human-fed act. A voice stop edit calls the same `record_stop_edit` the page calls, which recomputes `shares` and `per_share_risk` through `engine.recompute_for_stop` (`cards/store.py:668-674`) — the existing arithmetic, no new computation. L52's bar: (a) the stop is his dictated value, parsed by code and read back; the size comes from the existing engine; (b) no new ranking authority; (c) the seam is `set_card_stop` → `CardStore.record_stop_edit`, a real artifact; (d) auditable through the stop-edit row (`cards/migrations/0002_card_stop_edits.sql`) and the turn row. Nothing computes a score, rank or grade. V5 computes nothing either: it drafts the owner's settings file and hands the owner's own apply command to him (`[R3F-10]`).

[F-25] EXISTING EXPOSURE, not widened: the ASET routes carry no authentication (`configs/dev/aset.yaml:36-38`), so any process on the host can POST `/card/{id}/stop` today and could POST `/voice/turn` twice (act, then "yes"). A voice confirm proves his intent only as far as the page's access does; the backlog access token closes both.

Each law of the bar, for the FINAL (each clause points to the text above):
- **L1** fail-loud: a Plan parse failure FAILs the turn loud (§2.4); every failure has its red/amber line (§7); a missing config key crashes the load (§11 W7).
- **L2** watcher standard: each press is an event; no wake word, no listening loop; the agent is stateless and reads its history from rows (§2.4).
- **L3** one path: one turn function with three callers (`[F-01]`), one Transcriber, one model-access module (S1), one landing writer `land_pending` → `append_to_unit` (§6; `[F-11]` reuses it), one card-stop function `set_card_stop` shared with the page (`[F-06]`), one marker-less op for blank cells (`upsert_region`, `blank_only` flag — no second writer, `[F-13]`).
- **L4 / L41** no credential, env value or config secret enters the prompt (§2.4).
- **L7** [R3F-16] no variable flips to engine-fed; trading-logic changes are never executed by voice (§2.4). V5 builds the draft-and-send tool (`[R3F-10]`, `[R3F-11]`): the owner's file + sha256 + per-key diff, sent by `send_dm`; applied only by `cobalt settings load … --sha256 … --apply` — his hand, or the desk on his L7 approve. Before V5, `unsupported` with the owner's command named.
- **L9** probes + banners (§7); no local TTS voice is AMBER (§2.5).
- **L14 / L16 / L18** one voice; the agent is a registry entry; the turn row is the task row.
- **L23 / L25** V1 builds the local lane only; any Plan-call fallback is the routing lane's, in the model-access module, never in voice code; STT has no cloud engine (`[F-23]`). The routing cluster is cited, not rewritten.
- **L28** [R3F-16] the §6 write classes: append into his voice units, `blank_only` fills of blank cells (`[F-13]`), and — O1 RULED B (R39), SCOPE-R39 — his confirmed voice edit of any field of any note (his own text, his voice units and Cobalt's own units alike) by the op of the R2-2 side his letter selects (`## FOR DEJAN` item 3); confirmed writes bound to the target span with the writer's retry disabled (`[F-09]`); every write gated, versioned, atomic with the mtime guard. The L28 amendment is the `FOLD:` text of his letter; the desk folds it into LAWS.md under L58 at his approval of this FINAL. This derive writes no law file. Until that fold, L28 stands unchanged and the class is refused aloud (§6).
- **L32** transcripts are user-side rows (and reach the `cobalt_brain` backup as text, `[F-20]` F11); nothing of his is committed; test audio is synthetic.
- **L37** confirm is code equality with the single word `yes` or a tap (`[F-08]`), never the model; no house confirms a production act — the CLI `--confirm` is refused in production (`[F-02]`); a confirm turn makes no model call (`[F-01]`).
- **L40** [R3F-16] each side effect has its owning expert (vault → `VaultWriter`, card → `CardStore`, DRC → its command, trading-logic settings → the settings owner's own apply, V5); the voice module owns its rows and its scratch files (`[F-22]`) and is their only deleter; the heartbeat only counts (both R2-1 sides). When the voice module sweeps is his letter (`## FOR DEJAN` item 2).
- **L44** every house runs the same dev path, record button included (§8).
- **L45** real container format, synthetic content (§5).
- **L57 as set aside (R18)** transcript + Plan + resolution + confirm + the expert's write id are the stored inputs.
- Boundary (CLAUDE.md): nothing reads, writes or infers from his trading platform; no order tool exists and code refuses one; the trading PC is a browser tab over tailnet HTTPS, nothing installed.

## OWNER ITEMS

**O1** [R3F-17] — RULED B — `cto-2026-09-23.md` R39, his words: "I want my word to allow write to everywhere with my confirmation, is that one of the options (on cobalt voice question)"; scope (R43): "the scope is HIS words ("allow write to everywhere with my confirmation") = any field of any note on his confirmation; houses rule mechanics only."
- Carried as SCOPE-R39: `Cobalt may replace any field of any note in his vault — his own text, his voice units and Cobalt's own units alike —`.
- The fold text: R2-2 is UNRESOLVED after round 3 → `## FOR DEJAN` item 3, where each side's `FOLD:` line is shown verbatim. All three carry SCOPE-R39 verbatim.
- Fact: the L28 amendment is folded into LAWS.md by the CTO desk under L58, at his approval of this FINAL, using the `FOLD:` text of the letter he picks. Until then L28 stands unchanged.
- The round-1 and round-2 fold texts are superseded by R39 → `## Dissents, verbatim`.

No other owner item: grok "OWNER: none"; gemini wrote no `OWNER:` line; the Anthropic seat "none" (round 3).

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
