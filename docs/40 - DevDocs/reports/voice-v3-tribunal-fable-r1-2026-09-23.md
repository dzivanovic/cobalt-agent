BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: 2026-09-23 (started 07:40 EDT, ruling written 07:4x EDT; times from `date`)

## DIGEST FOR THE DESK

TRIBUNAL R1: BUILD AFTER seam S1 document, V1a/V1b experiments, and the blank-fill guard wording folded

- T1 ADOPT WITH — the CLI's `--confirm` is dev-only; in production a confirm comes only from the widget (L37).
- T2 ADOPT.
- T3 ADOPT WITH — the Plan call, not only the transcribe, stays off the event loop; E6 measures both.
- T4 ADOPT WITH — card stop through ONE function extracted from the route; trading-logic asks are refused until a HITL-card slice exists.
- T5 ADOPT.
- T6 ADOPT WITH — sha binds the TARGET span, not the whole note; a confirmed write takes no writer retry.
- T7 ADOPT WITH — add `drc.voice.bind` so an unbound (R2-V5) answer can be bound at the DRC, then landed.
- T8 ADOPT WITH — only the voice module deletes scratch; the heartbeat probe counts leftovers and never deletes (L40).
- T9 ADOPT WITH — `upsert_region` does not enforce "blank only"; the check must run inside the write, under the guard.
- T10 ADOPT WITH — `voice_turns` rows are not session-gated (the `cobalt_jobs` precedent); a read works at 20:15.
- T11 ADOPT WITH — split V1 into V1a (text turn + card stop) and V1b (audio); `tailscale serve` moves into V1b; pin `python-multipart`.
- T12 ADOPT.
- (a) ADOPT WITH — F2 and F9 each carry one wrong detail; §1 misses the recompute inside `record_stop_edit`, the web-private entry guard, the direct `litellm` pin and the unpinned `python-multipart`.
- (b) ADOPT — one landing writer holds for the 11:00 / DRC / re-import walk.
- (c) ADOPT WITH — any cloud fallback for the Plan call belongs to the routing lane, in the model-access module; voice code names a route and never a provider.
- (d) ADOPT WITH — four DRC FINAL changes named, carried, not folded.
- (e) ADOPT WITH — orders/platform/trading PC NONE; one model-approval path (CLI `--confirm` in prod) closed; the loopback exposure is pre-existing and named.
- (f) ADOPT WITH — the stop act DOES recompute size through the existing engine (`cards/store.py:668-674`); §14's "nothing computes size" is corrected, and L52's bar (a)–(d) is met.
- (g) ADOPT WITH — O1 is his; the fold must also cover his text inside his voice units, and bind to the target span.

Experiments: keep E1–E11, change E4 and E6; new X1 (noise/silence clips never match a confirm word), X2 (the blank-fill guard under a concurrent save), X3 (the loopback / proxy source address as uvicorn reports it), X4 (the body marker deleted after a crash), X5 (spoken price → transcript format → parser clarify rate).
Owner items: 1 — O1 (a law he owns: L28), fold text revised in (g).
WITHDRAWN: 2. ESCALATE: 3.

## Rulings

### T1 — architecture: one widget, one turn function, three callers, one model call per turn (§2, §8)
**ADOPT WITH** — replace §8's second sentence with: "Any house holding a build or check seat runs the same path in DEV (NN#16) with synthetic audio or text; `--dry-run` prints the Plan, the resolution and the exact diff with no write. The CLI's `--confirm <turn_id>` is refused when `COBALT_ENV=production` (named refusal, exit non-zero): in production an ACT is confirmed only by the widget — a tap, or his next spoken or typed turn in the same widget session. No house, the desk included, confirms a production act (L37)."
- The shape holds against the code. There is one web surface (`aset/web.py:852-1391`), no upload route today (`grep UploadFile src/cobalt` → 0), and no model caller in the new core (the litellm / endpoint greps → 0 in `src/cobalt`).
- Failing sequence as written: the proposal ships `cobalt voice turn --text … [--confirm <turn_id>]` to the production host. A hub on the host runs `COBALT_ENV=production uv run cobalt voice turn --text "move the stop on card <id> to <price>"`, reads back the turn id, then runs `--confirm <id>`. A production card stop is then approved by a model, not by him. L37 (`LAWS.md:212-214`) bans exactly this. The design itself invites it: §8 says "any house … runs the same path".
- Parity (R18 (c), L44) is kept: every house, the desk included, has the same dev path and the same lack of a production confirm.

### T2 — capture and exposure (§2.1, §2.2, §11 W6 / W11)
**ADOPT.**
- Reading the `UploadFile` bytes and never the `str(v)` idiom holds against the code: that idiom sits at six sites (`web.py:947, 1048, 1147, 1190, 1247, 1282`).
- W11 keys on what E8 shows. With uvicorn's proxy-header handling, a request that `tailscale serve` relays from 127.0.0.1 may carry the tailnet client's address instead of 127.0.0.1. That is a behaviour claim, so it goes to X3 (with E8), not an objection.
- The LAN refusal matters only if production binds `lan`. The committed dev file binds `loopback` (`configs/dev/aset.yaml:40`); which file production loads is v2 E7 (UNPROVEN).

### T3 — local speech-to-text (§2.3)
**ADOPT WITH** — append to §2.3: "The Plan call is off the event loop too: the model-access module's call is awaited on an async client or run through `to_thread`, never a blocking call inside the `async def` route. E6 measures `/size` and `/fill` latency during a transcribe AND during a Plan call."
- Every ASET POST route is `async def` (`web.py:946, 1047, 1139, 1182, 1240`), and a grep for `to_thread|run_in_threadpool` in `web.py` finds nothing. §2.3 moves the transcribe off the loop, but §2.4 says nothing about the model call.
- Failing sequence: at 09:45 a voice turn's Plan call is in flight. `UNVERIFIED — E4 measures its latency`: F8's ≈22 tok/s for a Plan of a few hundred tokens suggests seconds. At that moment he presses Compute on `/size` for an entry. If the call blocks the loop, the sheet stalls for its full length at entry time (X-claim → E6 as changed).
- The engine choice, pinned offline model files and no cloud STT are kept from v2 `[F-03]`/`[F-08]` (`DRC-VOICE-v2-2026-09-22.md:86-87`).

### T4 — the agent and its tool boundary (§2.4)
**ADOPT WITH** — (1) Replace §3's card-stop "Tool (owner)" cell with: "`cards.set_stop` → ONE function `set_card_stop(card_id, to_stop)` extracted from the route body `aset/web.py:1247-1257` (entry guard `_check_entry_allowed` `web.py:95`, open-card lookup, `Decimal` parse, `CardStore.record_stop_edit`); the `/card/{id}/stop` route and the voice tool both call it; the route's rendered output is unchanged." (2) Replace §2.4's HARD REFUSALS second clause with: "any request that would change trading logic (settings, rules, strategies, setup definitions, thresholds) is `refuse`d aloud with a fixed sentence naming L7 until a slice builds the HITL-card tool; no V1–V3 tool writes `trader_settings`, `configs/`, rules, strategies or setup definitions."
- (1) The stop logic today lives INLINE in the route (`web.py:1247-1257`), and the entry guard is private to `web.py` (`:95`, called at 8 sites). A voice tool that calls `record_stop_edit` directly re-implements the lookup and the guard. A tool that skips the guard is worse: on a dev instance with no `COBALT_ALLOW_DEV_ENTRY`, the page refuses a stop edit (`web.py:96-101`) and the voice path would allow it — two stop-edit paths with different gates (L3). Price: ≈30 lines move out of `web.py` into one function in V1a, one test that the route still refuses the same cases, no behaviour change.
- (2) The slice plan (§9) builds no HITL-card tool, so the §2.4 text describes a path no slice builds. Refusing is what V1–V3 actually do; the wording makes that explicit. L7 is unchanged either way.
- The closed candidate lists, verbatim `Span`s checked by code, reads rendered by code and the figures rule all hold. Nothing in them needs the model to be right for a number to be right.

### T5 — replies by the device's speech synthesis (§2.5)
**ADOPT.** No reply audio exists on the server, which is the smallest reading of R18 (b). `localService` availability is E5, correctly an experiment.

### T6 — confirmation (§2.6)
**ADOPT WITH** — replace §2.6 (c) with: "(c) the owning expert's re-computed TARGET still matches: the pending action stores `target_sha256 = sha256(target id ‖ the target span's bytes at read-back ‖ the after bytes)` (a unit id or a located region for a vault write; card id ‖ from_stop ‖ to_stop ‖ card state for a stop). At execution the expert recomputes it from a fresh read; a mismatch → REFUSED, the new before → after read aloud, re-confirm. A voice-confirmed write is executed with the writer's one retry DISABLED: a `NoteChangedOnDisk` ends the action as REFUSED, never a second attempt computed from bytes he did not hear."
- Whole-note diff hashing fails on normal use. Scenario: at 16:40 he is typing in his DRC's risk paragraph while he dictates a per-trade answer. Obsidian saves, and the note's bytes change outside the target unit. A sha over the whole-file diff, or its hunk line numbers, then differs, so every confirm is refused and re-read, in a loop. Binding the target span removes that and still catches an edit OF the target.
- The retry: `_write_with_retry` re-reads and re-builds once after `NoteChangedOnDisk` (`writer.py:530-552`). For a confirmed edit, that second build is a diff he never heard read back. T9 gives the concrete damage.
- Confirm-word matching by code, the TTL, and reads never needing confirmation are kept. A false "yes" from a noisy clip is X1.

### T7 — the function map and "which field in which file" (§3, §4)
**ADOPT WITH** — add a §3 row: "| Bind an unbound answer (R2-V5) at or after the DRC ("that answer goes to the second trade") | `drc.voice.bind` (voice module; lands through `land_pending`) | the pending turn → one trade of the closed list the build matched to that card | append-only | yes |". Replace §12's R2-V5 row with: "SETTLED: unbound at the build when >1 trade matches the card; listed on A31; bound later only by his `drc.voice.bind` turn against the matched trades; never nearest, never earliest."
- §4's "clarify at capture" cannot catch R2-V5. At 11:00 the candidate list is today's cards, and the answer binds to card `<id>` unambiguously. The ambiguity only appears at the build, when D3-2 matches two trades to that one card (trade → nearest prior card, `50-drc-d3-build.md:27`). Without a bind act, the line stays on A31, and D5-3 re-renders open items "on every later DRC until resolved" (`52-drc-d5-build.md:21`) with no operation that resolves it. Price: one tool entry and one test in V2. It reuses `land_pending`, so it adds no new writer.
- Note, field, value by code, and zero or two-plus candidates → `clarify`: these hold. Per-trade HIS fields are the voice unit, not cells. The trade blocks are Cobalt units (`50:27`), so "set <field> on trade <n>" mostly resolves to §6's Cobalt-unit refusal or a blank template cell. The map is correct, just narrower than its row label suggests.

### T8 — the ephemeral-audio lifecycle (§5)
**ADOPT WITH** — replace §5's "Crash leftovers" bullet with: "The voice module sweeps: on `com.cobalt.aset` start and at the start of every turn it deletes scratch files older than `scratch_max_age_s` (AMBER line per file; a failed unlink RED). The heartbeat's `voice_scratch` probe only COUNTS such files and never deletes (L40 — the voice module owns its scratch). The config schema refuses `scratch_max_age_s ≤ stt_timeout_s`."
- As written, §5 has "every heartbeat" deleting files while §9 V4 says "probes read". That puts a second side-effect owner on the scratch dir (L40). Failing sequence: `stt_timeout_s` is set above `scratch_max_age_s` from E2's numbers. A long clip is still transcribing when the heartbeat fires and unlinks it, and the turn fails for a reason nobody can see. The cross-key check stops that config from loading (L1, L10).
- The scratch path checks hold against the files. The prod parent `/Users/cobalt/.cobalt` exists, mode `drwx------` (`ls`, this run). The dev parent `/Users/cobalt/.cobalt-dev` does not exist, so the loader creates it at 0700 or FAILs; the builder picks one, and nothing is guessed. Neither path is under a `backup.yaml` source (`:37-41`).

### T9 — the vault-write path (§6)
**ADOPT WITH** — replace §6's blank-cell row "Op" cell with: "`upsert_region` with a `require_blank` predicate evaluated INSIDE its `build(snapshot)` on every attempt (the target span must still be the template's blank cell, else REFUSED — never merged); called with the retry disabled (T6)". Add to §6: "On a trading day D3 creates no day-level voice unit (`50-drc-d3-build.md:10` creates `drc-day/voice-no-trades` on no-trade days only); until a DRC FINAL change adds one, per-day speech on a trading day lands only in blank template cells."
- `upsert_region` does not enforce "blank → value only". With no baseline row, `base = human` (`writer.py:946-948`). Base equal to human means "only Cobalt changed → Cobalt wins" (`merge.py:14-15`). So whatever sits in the span is replaced. The only existing clause-2a caller checks blankness OUTSIDE the call, against the file (`seatusage/runner.py:141-147`).
- Failing sequence: at 16:52 he says "put <text> in <Label>" on a blank cell, the read-back classifies it blank, and he says "yes". Between the confirm's recheck and `_commit`, Obsidian saves his own typing into that cell. `_commit` aborts (`writer.py:464-469`). The retry re-snapshots (`:535-537`), finds his text, has no baseline, merges Cobalt over it, and writes: his text is replaced without O1. The predicate inside `build` plus no retry closes it.
- Price: one optional kwarg on `upsert_region` (≈10 lines at `writer.py:895-935`), 3 tests (blank → fills; non-blank → refused; changed between read and commit → refused, file unchanged), V2.
- Kept: append into his voice units (v2 `[F-01]` / `[F-18]`), Cobalt units never edited by voice, his non-blank text only under O1, one landing function, unbound listed.

### T10 — failure modes and the turn state machine (§7)
**ADOPT WITH** — add to §7: "`voice_turns` writes are NOT session-gated (as `cobalt_jobs`, `jobs/store.py:12-18`): a turn row is the voice module's own state, not trading record. Inside `market_reset` a read turn is answered; every ACT is refused by its owning expert's own gate (`VaultWriter._session_gate`, `writer.py:387-416`; `record_stop_edit`'s `assert_writable`, `cards/store.py:659`)."
- Every new-core store the builder will copy from gates its own writes (`assert_writable` in `cards/store.py`, `radar/store.py`, `daymode/store.py`). Following that pattern, at 20:15 "what is on radar" fails, because its L18 row cannot be written. `jobs/store.py:12-18` is the ruled precedent for leaving own-state tables ungated.
- The state machine, the reap and the loud table hold. E7 is the kill test.

### T11 — slices and experiments (§9, §10)
**ADOPT WITH** — replace the V1 row with two chunks, checked separately or together:
"| **V1a — text turn** | text box on the ASET pages; `/voice/turn` (text only); the model-access module (seam S1); Plan + resolver for cards; read tools; ONE confirmed act — card stop through `set_card_stop` (T4); `voice_turns` + migration; CLI; degraded banner | DB | ONE | S1 document; E4, E6 | `com.cobalt.aset` |" and
"| **V1b — audio** | widget capture; scratch lifecycle + sweep; Transcriber; device TTS; `python-multipart` pinned direct in `pyproject.toml` (locked only transitively today, `uv.lock:4460`; `pyproject.toml` has `fastapi`/`uvicorn` at `:32-33` and no multipart pin) unless D2 has pinned it first; the `tailscale serve` deploy step (moved from V4) | DB | — | V1a; E1, E2, E3, E5, E7, E8, E10 | `com.cobalt.aset` |"; V4 keeps probes, the model-fetch step and DevDocs.
- The proposal's V1 waits on E1, which needs his phone (his hands). If E1 slips a day, the agent, resolver and confirm (none of which need audio) wait with it. Splitting it adds no files; it re-orders chunks and gets the first real command running sooner.
- The serve step belongs with capture. On the proposal's own premise (F12 → E1), a V1 phone press on a plain-http page gets no recorder, so V1's phone path works only after V4. Putting the serve step in V1b makes "first conversation" true on his phone.
- Card stop as the first real command HOLDS as the smallest. It already exists behind one store call and lands in the DB, not the vault.
- The migration count HOLDS: main's list ends at `0011` (`db_migrations/__init__.py:67-79`), `voice_turns` needs a `placement.py` USER entry, and the number is the desk's at L68. The hours stay the proposal's guess (UNVERIFIED — builders re-derive).

### T12 — v2's twelve owner items settled; keep / supersede (§11, §12)
**ADOPT.**
- W7 is correct by L53's text (`LAWS.md:296`): committed config may carry engine tunables. The reserved items are the Finviz ceiling, the scan cadence and the pool-block settings, and a clip length or timeout is none of those.
- W4: building no cloud STT is lawful under L23/L25 (fallback is "permitted", `LAWS.md:143`, never required), and it proposes nothing about his audio leaving the host.
- W10 keeps transcripts as the stored input of an executed act. That is R18's replacement for L57 on audio, so the houses may decide it.
- §12's R2-V5 row is amended by T7.

### (a) THE FACT BASE
**ADOPT WITH** — corrections below, pasted into §1.
| F | Verdict | file:line |
|---|---|---|
| F1 | HOLDS — `grep -rn -i "voice\|whisper\|transcri" src/cobalt` → one unrelated hit (`cards/models.py:240`); `COBALT-REQUIREMENTS.md:206-208` | |
| F2 | HOLDS for the new core; DOES NOT HOLD in its detail "only … `llm.py` imports LiteLLM" — `cobalt_agent/tools/extractor.py:22` and `cobalt_agent/memory/postgres.py:31` import it too (old tree). Add: `litellm == 1.81.8` is ALREADY a direct dependency (`pyproject.toml:16`), so the S1 module adds no new dependency if it uses it | `pyproject.toml:16` |
| F3 | HOLDS | `ROUTING-v2-2026-09-22.md:32`; `LAWS.md:17` |
| F4 | HOLDS (plus three `GET /api/*` routes, `web.py:870, 887, 933`, not listed) | |
| F5 | HOLDS; MISSED: `record_stop_edit` gates itself (`cards/store.py:659`), refuses outside `STOP_EDITABLE` (`:661`), and RECOMPUTES `shares`/`per_share_risk` through `engine.recompute_for_stop` (`:668-674`, `:708`, `:730`) | |
| F6 | HOLDS | `configs/dev/aset.yaml:32-41` |
| F7 | HOLDS | `topics/devices.md:11, :30, :31` |
| F8 | HOLDS | `topics/devices.md:12, :17, :21` |
| F9 | HOLDS for line numbers; DOES NOT HOLD in two details: "every op passes `_session_gate`" — `restore` is UNGATED by ruling (`session/guard.py:82-84`; the gate is called at `writer.py:565, 664, 922` only); and `upsert_region` is not "blank → value only" (T9: `writer.py:946-951`, `merge.py:14-15`); its own docstring calls it "the frontmatter carve-out" (`writer.py:904-918`), with one non-frontmatter caller (`seatusage/runner.py:147`) | |
| F10 | HOLDS by anchor: `50:10` (R93), `50:13` (R99); D5-3 is at `52:21` now (the proposal warned lines move); `52:26` "NOT IN D5: … voice (R100)" | |
| F11 | HOLDS; add: the nightly dump of `cobalt_brain` (`backup.yaml:47-49`) carries `voice_turns` TRANSCRIPTS into backups — text, not audio, consistent with R18 (b) | |
| F12, F13 | correctly UNPROVEN → experiments (E1, E5, E8; E2, E3) | |
MISSED by §1: the entry guard is private to `web.py` (`:95`) — T4; `python-multipart` is not a direct dependency — T11; `jobs/store.py:12-18` is the ungated own-state precedent — T10; `heartbeat/runner.py:140` already runs `probe_mod.mainframe()`, so `voice_plan` reuses a probe that runs today; `prefill/vault_writer.py` is another new-core helper that resolves vault paths (`:19-50`), and voice does not use it (the owning module's writer is named per field, T9). No existing voice code, upload route or model caller in the new core.

### (b) L3 — ONE PATH
**ADOPT.** Walk (turn ids and dates only):
- 11:00, no DRC: turn T1 about card `<id>` → confirm → `voice_turns` row `pending_landing` (the voice module's only writer). No vault write, and nothing is written to `_imports/`, because the D2 bytes method carries no voice (§12).
- At the DRC, ≈16:30: D3-2's build `create_if_absent`s the note, creates `drc-trades/voice-<trade_id>` blank via `upsert_unit(…, skip_if=…)` (`50:13`, `writer.py:680-682`), then calls `land_pending(date)`. That appends T1's block through `append_to_unit`, idempotent on the turn id.
- A second answer T2 about the same trade, now with the DRC present: confirm → `land_pending(date)` → `append_to_unit` suffixes T2's block. T1 is not re-landed (row has its write id).
- Re-import: the build re-runs; `skip_if` matches, so the unit is skipped; `land_pending(date)` finds T1 and T2 landed and writes nothing.
- One turn function, one Transcriber, one model-access module (S1), one landing writer (`land_pending` → `append_to_unit`), and one scratch writer that is not a vault writer (§5). T7's bind act goes through the same `land_pending`, so no second path appears.

### (c) ROUTING AND LOCAL-FIRST (cited, never rewritten)
**ADOPT WITH** — replace §2.4's "No cloud route is built (L25)" with: "V1 builds the local lane only. Whether the Plan call carries any fallback is the routing lane's (L23/L25, frozen until the routing tribunal rules), configured in the model-access module, never in voice code: voice code names a ROUTE, never a provider or endpoint. Speech-to-text has no cloud engine (W4)."
- L23's text reads "local-first with cloud fallback" (`LAWS.md:133`). L25 makes the fallback an exception handler that is "permitted" (`:143`). Neither is rewritten here. The wording keeps voice from pre-deciding the routing lane's answer, and S1 stays the one place a fallback could ever live.
- S1 is lawful as the laws stand: it builds the ONE module that ROUTING-v2's derive wording names (`:32`), and it does not create a second path.
- Single-shot typed Plan = L22's fast wire (`LAWS.md:129`). Because the model only chooses and code acts, no chassis session is needed.
- The new dependency: faster-whisper and its transitive packages (`ctranslate2`, `av`, `onnxruntime` — none in `uv.lock` today; `huggingface-hub` `:1983` and `tokenizers` `:5310` already are) are UNVERIFIED until E10's lock diff. Memory beside the 88 GB wired limit (`devices.md:8`) is argued, not measured → E2.

### (d) HIS BYTES (L28, R99)
**ADOPT WITH** — add to §13 S2, carried to the desk, not folded (each is a change to the DRC FINAL):
"(a) D3-2 calls `land_pending(date)` right after it creates the voice units (`50:27`). (b) D5-3's `drc-day/open_items` renders `voice not bound: turn <id>` from `voice_turns` (D5 excludes voice today, `52:26`). (c) D3 persists each trade's matched card id where `land_pending` reads it (`drc_rows.inputs` carries the card `id`, `DRC-AUTOMATION-v2-2026-09-22.md:117`). (d) Optional: a day-level voice unit on TRADING days (today only `drc-day/voice-no-trades` on no-trade days, `50:10`) — absent it, T9's sentence stands."
- Crash between the vault write and the row update: the `vault_writes` row commits only AFTER the file write (`vaultwrite/store.py:191-230`). A crash after `os.replace` (`writer.py:476`) but before that commit therefore leaves the block on disk with no audit row. On retry, the turn-id marker inside the body is the only guard, so both checks (row, then body) are required, as v2 `[F-01]` says. If he deletes the marker line before the retry, the block is appended twice → X4.
- Re-drop or re-build: nothing re-lands (b). A vanished trade keeps its unit and gets the `orphaned` line (D3's writer, v2 seam 5).
- His edit while a confirm is pending: T6 plus T9 close the retry path.
- Sync revert: `append_to_unit` never takes the win (v2 `[F-18]`, kept).
- `market_reset`: every vault op is gated (`writer.py:565, 664, 922`) and the card stop is gated (`cards/store.py:659`). `restore` is ungated by ruling, and voice never calls it.

### (e) THE BOUNDARY
**ADOPT WITH** — T1's CLI wording, plus add to §14: "EXISTING EXPOSURE, not widened: the ASET routes carry no authentication (`configs/dev/aset.yaml:36-38`), so any process on the host can POST `/card/{id}/stop` today and could POST `/voice/turn` twice (act, then "yes"). A voice confirm proves his intent only as far as the page's access does; the backlog access token closes both."
- Orders / platform: NONE. The tool list is closed, no order tool exists, and code refuses whatever the Plan says.
- Trading PC: NONE installed. It is a browser tab over tailnet HTTPS, and a microphone permission there is a browser setting.
- Trading-logic change without L7 approval: NONE after T4 (2) (refused until a HITL-card slice exists).
- A secret reaching the model: NONE on the stated design (whitelisted prompt fields; LM Studio local, no key).
- A model-judged approval: ONE path, the production CLI `--confirm` (T1), closed by T1. The loopback HTTP exposure is pre-existing (above) and named, not solved here.

### (f) THE CARD (L52)
**ADOPT WITH** — replace §14's first sentence with: "Reaches the card: YES, by one human-fed act. A voice stop edit calls the same `record_stop_edit` the page calls, which recomputes `shares` and `per_share_risk` through `engine.recompute_for_stop` (`cards/store.py:668-674`) — the existing arithmetic, no new computation. L52's bar: (a) the stop is his dictated value, parsed by code and read back; the size comes from the existing engine; (b) no new ranking authority; (c) the seam is `set_card_stop` → `CardStore.record_stop_edit`, a real artifact; (d) auditable through the stop-edit row (`cards/migrations/0002_card_stop_edits.sql`) and the turn row. Nothing computes a score, rank or grade."
- As written, §14 says nothing computes a size, but `cards/store.py:730` writes `shares`. The act is lawful; the sentence describing it was wrong.

### (g) THE OWNER TEST
**ADOPT WITH** — O1 is his: a law he owns (L28), which no house can amend (Preamble; L58; L73). No other item passes the test, and the proposal settled nothing that is his. Replace the fold text with:
> [amended <date>] VOICE-ORDERED EDIT. Cobalt may replace text HE wrote — outside marker units, or inside a unit whose body is his (his voice units) — only when he orders that exact edit in a turn of Cobalt's voice / text widget and confirms it: the widget reads back note, field and before → after; his confirmation (a word from the closed confirm list matched by code, or a tap) is bound by sha256 to that target span's before and after bytes; the write replaces only that span, goes through `VaultWriter` with the mtime guard and `_session_gate`, takes no retry, is versioned with before, after and the turn id, and is refused if the span changed since the read-back. The replaced text remains his: no Cobalt ownership of it is created. The trader is in the loop (as for `cobalt settings load --apply`, 2026-09-15); this is not a model-judged approval (L37). Nothing else in this law changes.
- Failing sequence under the proposal's fold: at 16:50 he says "change my lesson on trade two to <text>". The target is his landed text INSIDE `drc-trades/voice-<id>`, which is a marker unit. The proposal's fold covers only "text outside marker units", so the edit is refused even after he rules yes. The rest of the fold changes match T6 (span-bound sha, no retry) and keep the text his, so a later Cobalt merge never treats it as Cobalt's baseline.

## Self-attack

Greps run (`grep -rn <name> /Users/cobalt/cobalt/src/cobalt`, one call each), writers / readers:
- `create_if_absent` — defined `writer.py:559`; callers `prefill/drc.py:427`, `prefill/daily.py:523`, `prefill/trade_note.py:151`, `radar/propose.py:753`, `aset/daily_note.py:184`, `seatusage/runner.py:107`. Voice calls none; D3 does.
- `upsert_unit` — `writer.py:644`; callers `prefill/drc.py:447`, `prefill/daily.py:558`, `daymode/note.py:159`, `heartbeat/runner.py:205`, `taxonomy/note_migration.py:872,880`, `taxonomy/cli.py:223`, `taxonomy/catalyst.py:404`, `replay/line.py:172`, `radar/propose.py:756`, `aset/daily_note.py:185`, `seatusage/runner.py:126`. Voice calls none.
- `upsert_region` — `writer.py:895`; callers `prefill/trade_note.py:162`, `taxonomy/cli.py:334`, `taxonomy/trade_note_migration.py:298`, `taxonomy/note_migration.py:888`, `seatusage/runner.py:147` (the only clause-2a caller; its blank check is outside the call, `:141-143`). Voice adds one caller (T9).
- `skip_if` — `writer.py:652, 680, 780` only; no caller on main (D3 adds one, `50:13`).
- `_commit` — `writer.py:457`, called only at `:527`. The other `_commit`/`before_commit` hits are DB stores, unrelated.
- `_session_gate` — `writer.py:387`; called at `:565, :664, :922`; not in `restore`.
- `assert_writable` — `settings/cli.py:170,249`, `settings/card.py:322`, `cards/store.py:267,659,851`, `daymode/store.py:78,104,151`, `radar/store.py:75,178,224,263,349`, `aset/web.py:954,1056,1303,1359,1377`, `writer.py:411`.
- `market_reset` — the guard (`session/guard.py`), clock (`session/clock.py`), `jobs/store.py:13` (deliberately ungated), `heartbeat/runner.py:71`, radar / archiver pauses, migrations 0003/0005.
- `record_stop_edit` — defined `cards/store.py:643`; sole caller `aset/web.py:1257`.
- `_check_entry_allowed` — `aset/web.py:95`; called at `:936, 949, 1050, 1192, 1249, 1302, 1358, 1376`.
- `request.form` — `aset/web.py:947, 1048, 1147, 1190, 1247, 1282`.
- `UploadFile` — 0 hits.
- `load_prefill_paths` — `prefill/config.py:151`; readers `smoke/checks.py:128`, `prefill/drc.py:383`, `daymode/drc.py:95`, `taxonomy/trade_note_migration.py:59`, `replay/line.py:160`, `aset/web.py:1020`.
- `resolve_vault_path` — `vault.py:145`; ≈25 readers (prefill, taxonomy, radar, archiver, cards, replay, aset, smoke); every writer path goes through it.
- `mainframe` — `heartbeat/probes.py:252` (probe), `heartbeat/runner.py:140`, `probes.py:862`, `jobs/restarts.py:34`, `seatusage/report.py:287` (comment). No caller of the model.
- `litellm` — 0 in `src/cobalt`; old tree imports at `cobalt_agent/llm.py:12,152`, `tools/extractor.py:22`, `memory/postgres.py:31`; direct pin `pyproject.toml:16`.
- `Probe` — 57 constructions in `heartbeat/probes.py`, 1 in `heartbeat/runner.py`.
- `DECLARED_TABLES` — `db_migrations/placement.py:106, 125, 170`; no `voice_turns` (V1a adds a USER entry).
- `aset_sizings` — writers `cards/store.py` (`:339, 622, 708, 730, 976, 1032, 1040, 1169, 1222, 1246-1252`) and `aset/store.py:116, 233`; voice reads it for candidates and writes only through `record_stop_edit`.
- `voice`, `whisper` — 0 hits. `transcri` — `cards/models.py:240` (unrelated).
- Names added, not on main (`grep -rn` of the eight names over `src/cobalt` → 0): `write_import_bytes` (`49:26`), `run_drc_build` (`50:27`), `drc-trades/voice-` (`50:13`, `:27`), `voice-no-trades` (`50:10`), `open_items` (`52:21`); `append_to_unit`, `land_pending` and `voice_turns` appear in none of `49`/`50`/`52` and only in the proposal (19 matching lines across the eight names there).

Walk of my own text against that list:
WITHDRAWN: "`python-multipart` is not in the lock" — `uv.lock:4460` lists it; the correct claim, used in T11, is that it is not a DIRECT dependency in `pyproject.toml`.
WITHDRAWN: "the heartbeat would need a new mainframe probe for `voice_plan`" — `heartbeat/runner.py:140` already runs `probe_mod.mainframe()`; §7's "reuses the `mainframe` probe" is right.

## Experiments (L70)

Kept as written: E1, E2, E3, E5, E7, E8, E9, E10, E11. Changed:
- E4 (changed): the Plan call on `mainframe` with `/no_think` over the constructed set, run ALSO while another client holds the local model (e.g. a Qwen Code seat mid-generation). Result that changes the design: queueing latency beyond `stt_timeout_s` + the Plan budget → the second small local model (F8, L23 by measurement) becomes V1a, not later.
- E6 (changed): `/size` and `/fill` latency on a dev ASET server while (i) a transcribe runs and (ii) a Plan call is in flight. Result: either stalls → that call moves off the loop (T3), or the Transcriber becomes a one-shot of the same function.
New:
- X1: on the home server, the chosen engine/size over 50 synthetic clips of silence, breath, cough, keyboard and room noise (generated at test time), plus 20 short non-confirm words. Count transcripts that normalize to a confirm-list word. Any > 0 → a spoken confirm also needs the engine's no-speech / low-confidence fields under a tunable, or ACTs on a card become tap-only.
- X2: dev vault, a test with `_precommit_hook` (`writer.py:461-462`) writing text into the target blank cell between snapshot and commit. Pass: REFUSED, file byte-identical to the hook's write. As written today (no predicate, one retry) the expected result is an overwrite. The test proves T9's fix.
- X3: dev ASET behind `tailscale serve` on the Mac: log `request.client.host` and the forwarded headers for a phone request, a Mac-browser `http://127.0.0.1` request and a LAN-client request (if bind `lan`). Result: fixes W11's check (loopback vs tailnet address vs header). A LAN client indistinguishable from the proxy → the `/voice/*` gate needs the tailnet identity header, or production stays `loopback` + serve only.
- X4: dev vault, land a block, kill between `os.replace` and the `vault_writes` commit (hook), delete the block's turn-id line by hand, then retry `land_pending`. Result: a second block → the marker needs a second form (e.g. hash of the block bytes) or the unit gets a Cobalt-owned ledger line.
- X5: synthetic speech of price / share / time utterances in several spoken forms (with and without "point", with and without a time-like reading), through the chosen engine, then the field parsers. Result: the share of clarifies per field type. A price transcribed as a clock time and parsed as a price would be a wrong value → that parser must refuse `H:MM` shapes.

## OWNER (after the tribunal)

- O1 — a law he owns (L28): may Cobalt replace text he wrote, when he orders that exact edit by voice/text and confirms it? No house can amend a law (Preamble; L58; L73). Fold text: (g) above. Only V3's overwrite class waits on it; no other slice needs it.

## WRONG FACTS

1. Proposal §1 F2 "only the old tree `src/cobalt_agent/llm.py` imports LiteLLM" — `src/cobalt_agent/tools/extractor.py:22`, `src/cobalt_agent/memory/postgres.py:31` import it too. (Old tree; no design effect.)
2. Proposal §1 F9 "every op passes `_session_gate`" (restore listed) — `session/guard.py:82-84` (restore ungated by the 09-04 ruling); `writer.py:565, 664, 922` are the only gate calls.
3. Proposal §6 blank-cell row "`upsert_region` (F9), blank → value only" — `writer.py:946-951` + `merge.py:14-15`: with no baseline the op replaces whatever is in the span. "Blank only" is a caller check today (`seatusage/runner.py:141-147`).
4. Proposal §14 "nothing computes a score, rank, grade or size" — `cards/store.py:668-674`, `:730`: the stop act recomputes `shares`.
5. Proposal §5 "on every heartbeat, a sweep deletes" vs §9 V4 "no (probes read)" — the proposal contradicts itself (`VOICE-v3-proposal-2026-09-23.md:90` vs `:139`).
6. Proposal §3 per-day row "or his day voice unit" — no day voice unit exists on a trading day in the DRC build (`50-drc-d3-build.md:10`, `:27`: `drc-day/voice-no-trades` on no-trade days only).

## READING

- Prompt `prompts/2026-09-23/14-voice-v3-tribunal-fable-seat.md` (whole); `prompts/2026-09-23/13-voice-v3-tribunal.md` :32–42 (the `01-QUESTIONS.md (verbatim)` paragraph through `TRIBUNAL R1:` only).
- `LAWS.md` 1–442 (full).
- `docs/30 - Design/VOICE-v3-proposal-2026-09-23.md` (whole); `reports/voice-v3-draft-2026-09-23.md` (whole).
- `reports/cto-2026-09-22.md` :56 (R109), :65, :66, :72, :73 (R100, R99, R93, R92); `cto-2026-09-23.md` :4, :21 (R18), :23 (R20), :24 (R21, cites R109 "STANDS" — recorded, does not stop); `cto-2026-09-21.md` :57 (R46); `areas/cobalt-product-definition.md` :68 (grep R18; :44 matched too).
- `docs/30 - Design/DRC-VOICE-v2-2026-09-22.md` :15–199; `reports/voice-tribunal-derive-2026-09-22.md` :72–85 + grep.
- `topics/devices.md` (whole, 33 lines).
- `ROUTING-v2-2026-09-22.md` :30–33; `COBALT-REQUIREMENTS.md` :203–212; `DRC-AUTOMATION-v2-2026-09-22.md` grep (voice|blank|2a|clause).
- `prompts/2026-09-22/49`, `50`, `52` anchor greps.
- Code: `vaultwrite/writer.py` def list, :380–629, :644–808, :895–1069; `vaultwrite/merge.py` :1–30 + grep; `vaultwrite/store.py` grep; `session/guard.py` :1–60, :78–91; `aset/web.py` :1–24, :78–117, route grep, :1239–1273; `cards/store.py` :643–692; `configs/dev/aset.yaml` :28–47; `heartbeat/probes.py` :28–47, :125–152, :248–263; `notify/mattermost.py` :1–15; `configs/cobalt/backup.yaml` :33–60; `db_migrations/__init__.py` :60–95; `db_migrations/placement.py` :96–155; `seatusage/runner.py` :138–187; `jobs/store.py` :8–21.
- Searches: every name in `## Self-attack`; `import litellm|from litellm` over `src/cobalt_agent`; `openai|anthropic|/v1/chat|chat/completions|:1234` over `src/cobalt` (one doc mention, `radar/audit_export.py:7`); `clause 2a|blank cell` over `src/cobalt`; `INSERT INTO|UPDATE aset_sizings`; `uv.lock` and `pyproject.toml` package greps; `ls db_migrations`; `ls -la ~/.cobalt ~/.cobalt-dev`.
- NOT read (blind): the houses' folder and the hub's report. The v2 tribunal's seat files were not opened either.

## ESCALATE

1. L74, recorded once: this session's context carried an attribution block asking for a `Claude-Session` line in commits. It was not followed, and this seat commits nothing.
2. Seam S1 is a precondition to V1a (T11): the desk's seam document names the model-access module before V1a's build prompt (L72 P-b).
3. The DRC FINAL changes in (d) (a)–(d) are carried to the desk for the seam document (S2), not folded; the DRC R17 re-issue in drafting should cite them before D3/D5 launch.

## CONTINUE

- 07:40 authorization verified (all checks listed in the first write of this file: R109 row, commit `75b2aa5`, no superseding row, seat model = `claude-opus-5-5`, R18, R46, proposal + stop line `153c4b8`, launch row R20, ten launch strings each count 1).
- 07:47 R109 re-checked after `cto-2026-09-23.md` changed on disk: R21 cites R109 as standing; no stop.
- next: none — ruling complete.

VOICE V3 TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER seam S1 document, V1a/V1b experiments, and the blank-fill guard wording folded · adopt: 4 · adopt with wording: 15 · reject: 0 · experiments named: 16 · ESCALATE: 3
