BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Fri Sep 25 06:49:59 EDT 2026

## DIGEST FOR THE DESK
Closing line: `TRIBUNAL R1: BUILD AFTER the Q1 stored-reply guard and test_jobs_restarts seam are written in`
- Q1 ADOPT WITH — a tap's reply is never stored; the route would speak the stale read-back. 409 guard on `pending_action` rows.
- Q2 ADOPT — one in-memory WAV; `no-store` header added under (d).
- Q3 ADOPT — `onnxruntime 1.30.0` is in the lock, no torch; direct pin wording under (c).
- Q4 ADOPT WITH — order: path without it → priced sidecar → one licence yes/no to him.
- Q5 ADOPT WITH — read-backs never server-voiced in VT; Q1's guard is the mechanism, not a flag.
- Q6 ADOPT WITH — own abort is never a failure (else device voice speaks into his recording); one voice per reply.
- Q7 ADOPT WITH — probe reads only the resident's `/voice/status`; heartbeat process would read the DEV `model_dir`.
- Q8 ADOPT WITH — L31 bars person/vendor names (LAWS.md:182); `faster-whisper` is an artifact name, not bound.
- Q9 ADOPT WITH — non-blocking acquire → 503 `busy`; a blocking lock queues synthesis for aborted clients.
- Q10 ADOPT — L57 for audio already set aside (FINAL:22); VT-X6 informational.
- (a) ADOPT WITH — T10 and T16 corrected; five facts §1 missed, tap path first.
- (b) ADOPT WITH — one reply voiced at most once; walk shows no second path.
- (c) ADOPT WITH — VT-1 blocked on a recorded VT-X4; network-off + write trace; direct `onnxruntime` pin.
- (d) ADOPT WITH — `Cache-Control: no-store`; refuse silent output; abort never AMBER.
- (e) ADOPT — NONE, given Q1's guard; runtime cache writes are VT-X4's to observe.
- (f) ADOPT WITH — add `test_jobs_restarts.py` to the SEAM; T16 is recorded fact (V1-BUILD:454), not experiment.
- (g) ADOPT WITH — item 1 passes (taste), houses' default ships; item 2 fails (R23 + measurement settle it).
Experiments: VT-X1, X2, X3 (changed), X4 (changed), X5, X6 (informational) kept · new X7 silent output, X8 busy rate.
Owner items: 1 PASSES (not a precondition) · 2 FAILS.
WITHDRAWN: 1 · ESCALATE: 1

## Rulings

**Q1 — Route. ADOPT WITH:**
> **Route rule.** `GET /voice/tts?session=<id>&turn_id=<id>` sits behind `Depends(peer_gate)`. A missing row, or `row.session_id ≠ session` → 404 `no such turn in this session`. `row.pending_action IS NOT NULL` → 409 `device_voice`: the row is a read-back, or a pending action a tap has since resolved, and a tap never stores its own reply (`turn.py:258-274`, `confirm.py:66-118`). `row.reply` NULL or empty → 404 `no reply stored`. `len(reply) > tts_max_chars` → 413. Anything else → synthesize `row.reply`. The widget fetches only for a response with `r.ok` and a `turn_id`. A 409 `device_voice` is spoken by the device voice with no AMBER line. Every other non-200 is spoken by the device voice with AMBER `server voice down (<class>)`. Tests: tap Confirm, then GET → 409 · a spoken `yes` turn, then GET → 200 with that turn's own stored reply · another session's `turn_id` → 404.

Why. A separate GET after the text is right; the gap is which text the row holds.
- Failing scenario: 09:40:00 he says "move the stop on `<ticker>` to `<price>`". Row T1 goes `awaiting_confirm` with `reply` = the read-back (`turn.py:377-380`).
- 09:40:05 he taps Confirm. `_tap` builds a DRY `_Rec` on T1 (`turn.py:260`) and returns `turn_id=T1` with reply "Done. …" (`confirm.py:108`). `confirm_pending` moves T1 executing → done without passing `reply=` (`confirm.py:73`, `:99`).
- So `GET /voice/tts?turn_id=T1` speaks "… Say yes to do it." AFTER the stop was written. If the expert refused (`confirm.py:88-92`), the text shows RED "Refused: …" while the server voice asks him to confirm again.
- A spoken "yes" is safe: that turn writes its own reply on its own row (`turn.py:253`, `:419`).
- Price: one `if` and three tests in VT-2, and one condition in VT-3. No V1 change.

**Q2 — Wire. ADOPT.** One body is simpler and testable, and WAV needs no encoder. Size = 2 B × `sample_rate` × `duration_s`. Both values are UNVERIFIED — VT-X1 records them, VT-X3 times the transfer on the phone. The cache header is under (d).

**Q3 — Runtime. ADOPT.** The lock argues it:
- `onnxruntime 1.30.0` is present (`uv.lock:3280-3281`) as faster-whisper's dependency (`uv.lock:1388-1395`).
- There is no `name = "torch"` entry in the lock (grep, 0 hits).
- Whether the model's package accepts 1.30.0 is VT-X4's to show. The direct-pin wording is under (c).

**Q4 — GPL / native grapheme-to-phoneme step. ADOPT WITH:**
> If VT-X4 finds a native or GPL-licensed grapheme-to-phoneme step:
> 1. Round 2 first looks for a path without it: another grapheme-to-phoneme package that passes E10's shape (lock diff, licences, offline load) and keeps VT-X5's figures intact.
> 2. A loopback sidecar is priced before it is chosen: a new launchd resident, plist, `jobs.yaml` row, restart rule, probe and RSS line (≈ +2 h, one more chunk, UNVERIFIED). Whether a separate process changes the licence's reach is a legal claim no house settles from memory.
> 3. If neither path exists, ONE question reaches him: accept that licence in this private install, yes or no. It is his law, not a mechanism (L67).

Why. The proposal left the order open and the sidecar unpriced. Choosing it silently would add a resident (L42, L3).

**Q5 — VT-X5 as a hard gate. ADOPT WITH:**
> Read-backs — every row with `pending_action` set — are never spoken by the server voice in VT. Q1's 409 `device_voice` guard is the mechanism: unconditional, with its test. VT-X5 runs in VT-0 and is recorded. Lifting the guard for `awaiting_confirm` rows after VT-X5 shows 0 mismatches is a later change with its own check, never a config flag.

Why. The proposal named no mechanism ("until VT-X5 passes, read-backs use the device voice", proposal:82). One guard settles both Q1 and Q5, at zero added size. A flag would be a switch on the path he confirms acts by ear (FINAL:88).

**Q6 — Fallback order. ADOPT WITH:**
> **Fallback — each hop loud (L9), except his own stop.**
> 1. A response with no `turn_id` (`web.py:89`, `:259`, `:261`, `:282`), or a 409 `device_voice` → device voice; no server-voice line.
> 2. 404, 413, 503, fetch timeout, or `play()` rejected before the first audio frame → device voice + AMBER `server voice down (<class>)`.
> 3. No `localService` voice → text, with V1's AMBER `no local voice on this device` (`web.py:244`) beside the line from step 2.
>
> An abort the widget itself caused (a new press, Send, mute) is never a failure: no fallback, no AMBER. An `error` after playback began → AMBER `server voice stopped (<class>)`, and the device voice does not replay the reply. `show()` calls one `voiceReply(j)` INSTEAD of V1's `speak()` (`web.py:252`) — never both.

Why. Server-first is his order (R23), and both hops are local (L23).
- Failing scenario without the abort clause: 10:02:00 the reply is shown and the fetch is in flight. 10:02:01 he presses to talk. `start()` aborts the fetch, and a catch-all "fetch failed → device voice" speaks the old reply WHILE the microphone records (`web.py:273-286`). The next transcript then carries Cobalt's own words.
- Mute is safe only by accident: V1's `speak()` returns when `muted` (`web.py:242`).

**Q7 — `voice_tts` probe. ADOPT WITH:**
> `voice_tts` reads ONLY the resident's `GET /voice/status` over loopback (an allowed peer, `voice.yaml:44`). The resident fills that route's `tts` block:
> - `present`: model and voice files in the RESIDENT's `model_dir`, a local lookup;
> - `model_dir`;
> - `last`: the last synthesis outcome class and its time;
> - `rss_peak_mb`: `resource.getrusage(RUSAGE_SELF).ru_maxrss`, E2's method (V1-BUILD:104) — the whole resident's peak.
>
> `present` false → RED `model missing (<dir>)`. `last` in {timeout, engine_error, busy, silent} → AMBER. `rss_peak_mb` > `tts_rss_amber_mb` → AMBER with the number. Unreachable or non-200 → RED unknown. The heartbeat process imports no engine and resolves no `model_dir`. It never synthesizes.

Why. Failing scenario for the proposal's file check in the heartbeat process:
- `COBALT_VOICE_MODEL_DIR` is exported only in `ops/start_aset.sh:37` (grep over `ops/`, `src/`, `configs/` → that line and two comments). `ops/com.cobalt.heartbeat.plist` does not set it.
- So `load_voice_config()` in the heartbeat returns the committed DEV `model_dir` `/Users/cobalt/.cobalt-dev/voice-models` (`voice.yaml:19`; env loop `config.py:141-146`).
- Production's empty `/Users/cobalt/.cobalt/voice-models` then reads GREEN wherever the dev dir holds the files.
- The change is smaller than the proposal's: it drops two checks and an engine import from the heartbeat, and adds no `load_voice_config` reader to `test_jobs_restarts.py`.

**Q8 — L31. ADOPT WITH:**
> L31 (LAWS.md:182) bars PERSON or VENDOR names from identifiers, schema, config keys, enum values and system design docs.
> - `neural-82m`, `Neural82mSynthesizer` and `tts_*` are lawful.
> - `tts_voice`'s VALUE is the voice file's id exactly as the pinned model ships it. It is an artifact id (L31: "cite the artifact") and a free string — never an enum value, identifier, schema name or design-doc text. The design names it only as `tts_voice`.
> - V1's `faster-whisper` names the library, an artifact, not a person or a vendor. L31 does not bind it, and its rename is not a law defect.

Why. The proposal (T6, §11 Q8, ESCALATE 1) reads L31 as "product name". The law text says person or vendor, and its own example `cameron_grid` is a person. See WRONG FACTS 3 and ESCALATE 1.

**Q9 — Single-flight + client abort. ADOPT WITH:**
> One synthesis at a time per process, by a NON-BLOCKING acquire. A request that finds the lock held returns 503 `busy` at once; the widget uses the device voice + AMBER `server voice busy`. Nothing queues. A synthesis whose caller timed out keeps the lock until it ends — the thread cannot be killed, as in `transcribe.py:170-179`'s shape. `/voice/status` records `last` = `busy` or `timeout`.

Why. With a blocking lock inside the per-call one-worker pool (the `transcribe_with_timeout` shape, `transcribe.py:170-179`, `shutdown(wait=False)`), every timed-out caller leaves a thread waiting on the lock.
- Failing scenario: synthesis takes S > `tts_timeout_s` (UNVERIFIED — VT-X1). Presses at 09:31:00, :01 and :02 each abort the previous fetch in the widget only.
- The server then synthesizes all three back to back, for clients already gone, on the CPU the next transcribe needs (E6's concern, FINAL:282).
- The non-blocking form is the same size as the proposal's lock. X8 measures how often `busy` fires.

**Q10 — L57 / §2.5. ADOPT.**
- R18 already set aside L57's "replayable" for audio (FINAL:22). The proposal's narrowing "text replayable, audio not" is that reading.
- VT-X6 is informational and gates nothing.
- The stored inputs are the row's `reply` (`0017:45`) and the committed config in git. "Streams" amended, "writes no file" kept: correct.

**(a) The fact base. ADOPT WITH** these corrections and additions:
- HOLD:
  - T1 (`COBALT-REQUIREMENTS.md:206-208`)
  - T2 (FINAL:63, :86)
  - T3 (`cto-2026-09-25.md:29-31`)
  - T4 (`transcribe.py:41-47`, `:50-63`, `:66-68`, `:75-91`, `:161-167`, `:170-184`)
  - T5 (`config.py:41-63`, `:84-103`, `:141-148`, `:165`; `start_aset.sh:37`)
  - T6 (`config.py:47`; `transcribe.py:129-130`, `:163`)
  - T7 (`models.py:142-155`, `:135-139`)
  - T8 (`0017:26`, `:45`; `store.py:160`)
  - T9 (`web.py:236-253`, `:292`)
  - T12 (V1-BUILD:113, :127)
  - T13 (`devices.md:8`)
  - T14 (V1-BUILD:84-101, :435; `uv.lock:3280-3281`)
  - T15 (V1-BUILD:446, :448)
  - T17 (`POWER_PACKS.md:575-578`, `:606-608`)
  - T18 (grep `kokoro` over `src`, `configs`, `pyproject.toml`, `uv.lock` → 0)
  - T19 (`topics/cto-desk.md:136` (1))
- T10 DOES NOT HOLD in part: "today only 'speech-to-text down (model missing)'". `status_lines` also returns the start-sweep and reaper lines (`web.py:143`, `:180-182`) and "voice config unreadable" (`web.py:148`).
- T16 DOES NOT HOLD as an experiment:
  - `grep -c -F -e voice.yaml jobs.yaml` = 0; line :70's comment names `voice/config.py`, not `voice.yaml`.
  - The derivation already ran on V1's range and named `configs/cobalt/voice.yaml` `UNCLASSIFIED CONFIG` (V1-BUILD:454). The gap is RECORDED, not UNPROVEN.
- T18 is correctly an experiment (VT-X4).
- MISSED:
  - (1) The tap path returns a reply it never stores (`turn.py:258-274`; `confirm.py:66-118`) — Q1.
  - (2) `tests/cobalt/test_jobs_restarts.py:180-194` and `:408-421` pin every function reaching `load_voice_config`; a new route handler joins them — (f).
  - (3) The heartbeat plist carries no `COBALT_VOICE_MODEL_DIR` (grep `ops/` → only `start_aset.sh:37`) — Q7.
  - (4) The widget voices synthetic responses that have no `turn_id` (`web.py:89`, `:259`, `:261`, `:282`) — Q6.
  - (5) No server synthesis path exists today: `scratch.py:54`'s `audio/wav` is an upload content type (grep `synthes`, `speechSynthesis` → the widget only).

**(b) L3 — one path. ADOPT WITH:**
> One reply is voiced at most once: by the server voice, or — only if no audio frame has played — by the device voice. Never both, and never after a widget-caused abort (Q6).

Walk:
- T: the reply row is written before the response returns (`turn.py:349-351`, `:377`).
- T+0.2 s: fetch → 200.
- T+1 s: the second press aborts it and pauses playback. The server finishes that synthesis holding the lock. The new turn's fetch returns 503 `busy` if it arrives inside that window (Q9) → device voice + AMBER.
- T+2 s: mute pauses and aborts; nothing speaks.
- A resident restart between the turn and the fetch: the fetch fails → device voice + AMBER. The row survives in the DB, and the first synthesis after the restart pays the cold load (VT-X1).
- Second paths: none — one Synthesizer, one route, one `model_dir` (a sub-dir), one loader (`load_voice_config`), one status route (`/voice/status` extended) and one fetch command (the §10 seam).

**(c) L15 / L23. ADOPT WITH:**
> - VT-1 does not start until VT-X4's lock diff, licence list and outcome sit in a committed report. If VT-X4 found a native or GPL package, VT-1 also waits for round 2's ruling (FINAL:285).
> - `onnxruntime` is today only a transitive dependency of faster-whisper (`uv.lock:1388-1395`; absent from `pyproject.toml` — grep, 0 hits). If VT imports it, it becomes a direct `==` pin.
> - VT-X4 also runs load plus one synthesis with the network OFF and a file-write trace. Any network attempt or file written outside `model_dir` → round 2: it would be a cloud path or a file.

Why.
- "ONNX first" is argued from the lock (Q3), not assumed.
- Memory is argued, not measured, until VT-X2. An 82M-parameter model at 4 B per weight ≈ 0.33 GB (82×10⁶ × 4 B). The parameter count is itself UNVERIFIED until VT-X4.
- The order server → device (`localService` only, `web.py:238`) → text has no cloud hop: lawful under L23.
- The only network code path is the deploy fetch.

**(d) L1 / L9 / L57. ADOPT WITH:**
> - The route sets `Cache-Control: no-store` on every `/voice/tts` response.
> - The widget revokes the object URL on `ended`, `error` and abort.
> - `synthesize()` refuses an output with zero samples, or with all samples zero → `TtsDown(engine_error)`, detail `silent output` (AMBER; the device voice speaks).
> - Scope of the "no audio stored" claim: the design controls the memory it drops, the response body and its cache header. What `tailscale serve` and the browser do with a `no-store` body is VT-X3's to observe, never claimed.

Why.
- A GET body without `no-store` may be kept in the phone browser's disk cache. That would put reply audio on a disk, against "no reply audio is ever written" in amendment B.
- An engine that loads but emits silence is the one path in §6/§8 C with no line at all.
- A widget-caused abort must be silent (Q6).
- The narrowing if VT-X6 fails is correctly stated (Q10).

**(e) The boundary. ADOPT — NONE**, once Q1's guard is in:
- Stored `reply` only: no free text reaches the engine.
- Session match → 404. Same `peer_gate`.
- No file, no row, no note — a runtime cache write is VT-X4's (c) to observe.
- Nothing installed on the trading PC or phone: a browser tab plays a WAV.
- No trading-platform read, and nothing reaches score, rank, grade or size (L52).

**(f) The seam. ADOPT WITH** — add to §10:
> - `tests/cobalt/test_jobs_restarts.py`: `EXPECTED_BACKUP_YAML_READERS` (:180-194) and the `entrypoints` set (:408-421) pin every function reaching `load_voice_config`. The new route handler, and any helper it calls that reaches `get_config`, joins both sets with a `# VT` comment. It is listed under VT-2, as `POST_ALLOWLIST` is (T19).
> - `configs/cobalt/voice.yaml`'s absence from `com.cobalt.aset`'s `reads:` is RECORDED (V1-BUILD:454, `UNCLASSIFIED CONFIG`): a real gap, not an experiment. The `jobs.yaml` line stands.
> - `ops/com.cobalt.heartbeat.plist` needs no voice env under Q7. V4's `voice_stt`, if it resolves `model_dir` in the heartbeat process, needs `COBALT_VOICE_MODEL_DIR` there — a V4 seam line.
> - Amendment B: its read-back sentence becomes "A read-back is never spoken by the server voice in VT (Q5)."
> - Amendment C gains two rows: "Server voice busy | device voice; AMBER `server voice busy` | `voice_tts` AMBER (last)" and "Engine emitted silence | device voice; AMBER `server voice down (engine error)` | `voice_tts` AMBER (last)".

V1's contract is untouched: `TurnOutcome` and the three callers are unchanged, and `models.py` changes in its docstring only. A–F otherwise change no clause VT does not need.

**(g) The owner test. ADOPT WITH:**
> - OWNER ITEM 1 (voice and speed) PASSES: it is his taste in what he hears, and no house can hear for him. It is NOT a precondition. VT-1 ships the houses' default: the candidate voice with the fewest VT-X5 figure mismatches at `tts_speed` 1.0, ties broken by VT-X1 latency. In the device session he already owes, he hears the candidates (generated in dev from synthetic text, played on the Mac) and may name another. That changes one committed config value and restarts `com.cobalt.aset`.
> - OWNER ITEM 2 FAILS: server-first is settled by his own order (R23, `cto-2026-09-25.md:31`) and by measurement. If VT-X1 or VT-X3 miss the budget, round 2 changes the order — a houses' change.
> - No other item passes, except Q4 (3) if it is ever reached.

## Self-attack
The prompt's grep list, run over `/Users/cobalt/cobalt-wt/voice-v1` (tip `d794e899`, clean; code = `d319e4f3`):
- `Transcriber`: defined `transcribe.py:67`; used `:166`, `:170`, `:182`; mentioned `scratch.py:6`. Untouched by VT; VT-X5 calls it.
- `ENGINES`: `transcribe.py:163`, `:167`, `:187`. VT adds its own map in `synthesize.py`.
- `stt_engine`: `config.py:47`; `transcribe.py:161`, `:167`; `voice.yaml:21`. Written to rows at `turn.py:213` → `0017:35`, and listed in `store.py:40`. A V1 rename would leave old rows holding the old value — a BACKLOG note, not VT's.
- `model_dir`: `config.py:45`, `:141`, `:165`; `transcribe.py:76`, `:84`, `:100`. No heartbeat reader today.
- `COBALT_VOICE_MODEL_DIR`: `config.py:34` (`MODEL_ENV`); `ops/start_aset.sh:37`; comments at `config.py:8` and `voice.yaml:8`. It is NOT in the heartbeat plist.
- `local_files_only`: `transcribe.py:84`, `:100`.
- `SttDown`: defined `transcribe.py:41`; raised `:89-90`, `:126`, `:147`, `:177`; caught `turn.py:188`, `:195`.
- `TurnOutcome`: `models.py:142`; built only through `turn.py:165-166 _outcome`.
- `reply`:
  - stored by `rec.go` / `rec.fail` at `turn.py:161`, `:250`, `:253`, `:317-325`, `:349`, `:377`, `:419`;
  - NOT stored by `_tap` (`turn.py:260`, dry) or by `confirm.py:71-118`;
  - read by `store.py:186` (history) and by the widget at `web.py:248`, `:252`;
  - synthetic widget replies at `web.py:89`, `:259`, `:261`, `:282`.
- `voice_turns`: `store.py` (every write and read), `0017`, `placement.py:91`, `db_migrations/__init__.py:88`, `:93`.
- `session_id`: `web.py:112`, `:117`, `:127`; `turn.py:59`, `:71`, `:142`, `:261`, `:291`, `:406`; `store.py:96-196`; `cli.py:48`, `:66`, `:69`. Widget: `SESSION` per page load (`web.py:227`).
- `peer_gate`: `web.py:70`, `:95`, `:130`, `:135`, `:152`; `test_jobs_restarts.py:183`, `:414`.
- `allowed_peers`: `config.py:63-72`; `web.py:72`; `voice.yaml:44` = loopback only.
- `status_lines`: `web.py:140`, `:154`; `test_voice_web.py:152`; `test_jobs_restarts.py:189`.
- `speechSynthesis` / `localVoice` / `speak` / `mute`: `web.py:236-246`, `:252`, `:292` only.
- `POST_ALLOWLIST`: `test_radar_panel_cards.py:667-673`, `:685`. A GET leaves it unchanged; `GET_ONLY` (:674) does not list `/voice/*`.
- `voice_stt`: only a failure class (`turn.py:189`, `:196`; `test_voice_turn.py:219`). No probe exists; V4 is unbuilt.
- `onnxruntime`: `uv.lock:1395`, `:3280`. Absent from `src/` and `pyproject.toml`.
- Also: `voice_tts`, `voice/tts`, `Synthesizer` → 0 hits.

My text walked against this list:
- Every `file:line` above was opened or grepped this run.
- WITHDRAWN: "the heartbeat's voice probe resolves `model_dir` the way V4's `voice_stt` already does" — no `voice_stt` probe exists; `voice_stt` is only a failure class (`turn.py:189`, `:196`). The sentence is struck; Q7 rests only on `start_aset.sh:37` plus the plist grep.
- I make NO claim about what peer address `tailscale serve` presents (E8/X3 owed, V1-BUILD:448). Q7 relies only on loopback being in `allowed_peers` (`voice.yaml:44`).

## Experiments (L70)
- VT-X1 KEEP (first audio; cold and warm; under STT + Plan load). Records `sample_rate` and `duration_s` per character. It also sets `tts_timeout_s` and `tts_max_chars`.
- VT-X2 KEEP. It also sets `tts_rss_amber_mb` against `ru_maxrss` as Q7 names it (the whole resident).
- VT-X3 CHANGED. It adds, on his phone and the trading-PC browser over `tailscale serve`:
  - a `no-store` WAV is absent from the browser cache afterwards (inspect the browser's cache listing);
  - a press mid-fetch voices nothing (Q6);
  - a tap Confirm voices the device's "Done" line, not the read-back (Q1);
  - `play()` after an awaited fetch following the gesture: allowed or refused.
  - Result that changes the design: cached → the route or the proxy needs a further header (round 2); refused play → tap-to-play + AMBER as proposed.
- VT-X4 CHANGED. It adds, in a scratch worktree:
  - load plus one synthesis of synthetic text with the network OFF, and a file-write trace (`fs_usage` on the process);
  - whether the runtime package accepts the locked `onnxruntime 1.30.0`.
  - Result that changes the design: any network attempt or file write outside `model_dir` → round 2 (Q4 / (c)); a version conflict → round 2 on Q3.
- VT-X5 KEEP. It becomes the default-voice selector (g). It does not lift Q5's guard inside VT.
- VT-X6 KEEP as INFORMATIONAL: it gates nothing (Q10).
- X7 NEW (Mac, dev): synthesize synthetic replies that are digits-only, symbols-only, a single word and the empty-after-strip edge. Count outputs with zero or all-zero samples → sets whether (d)'s silent-output refusal ever fires; any hit → a text pre-check per field type in round 2.
- X8 NEW (Mac, dev ASET): three synthetic text turns 1 s apart while each synthesis runs. Count 503 `busy` per 100 replies at VT-X1's measured synthesis time → busy > 5 % → sentence-chunked synthesis goes to round 2, as the proposal's §4 foresaw.

## OWNER (after the tribunal)
- OWNER ITEM 1 — voice and speed: PASSES. It is his taste in what he hears, and no house can hear for him. Not a precondition; the houses' default ships (g).
- OWNER ITEM 2 — server or device voice first: FAILS. R23 and measurement settle it.
- Q4 (3) only if reached: accepting a GPL licence in this private install — his law.

## WRONG FACTS
1. Proposal:20 (T10) "today only 'speech-to-text down (model missing)'". `web.py:143` (sweep lines), `:148` (config unreadable) and `:180-182` (reaper lines) contradict it.
2. Proposal:25 (T16): "`grep -F voice.yaml` → only the comment at :70" and "how `cobalt jobs restarts` classifies it: UNCITED".
   - `grep -c -F -e voice.yaml configs/cobalt/jobs.yaml` = 0; `jobs.yaml:70` names `voice/config.py`.
   - V1-BUILD:454 records the derivation's `UNCLASSIFIED CONFIG` for `configs/cobalt/voice.yaml`.
3. Proposal:16 (T6), :175 (§11 Q8), :195 (L31 line), and its report's ESCALATE 1 (`voice-tts-propose-2026-09-25.md:93`) read L31 as barring a "product name". LAWS.md:182 reads "Person or vendor names never in code identifiers, schema, config keys, enum values or system design docs".

## READING
- AUTHORIZATION (06:49–06:51 ET), every check passed:
  - The FABLE ROW unfilled-count is 0, so the row is R109.
  - R109 is at `cto-2026-09-22.md:56`, carries `Make all Opus 5.5 for now` and `claude-opus-5-5`, and is committed `75b2aa57`.
  - The launch row R33 is at `cto-2026-09-25.md:41` and carries all three literals; it is committed `b6854e54`. `cto-2026-09-26.md` is absent (recorded).
  - This session runs `claude-opus-5-5`, the model R109 names.
  - R23 (:31) and R95 (:103) carry their literals.
  - The proposal is committed `a2fc3315`.
  - The 7 allow and 3 deny strings each count 1 in `2026-09-23/12`.
- Prompt `17-…anthropic-seat.md` (whole); `16-voice-tts-tribunal.md` :32–42 only (the `01-QUESTIONS.md` paragraph).
- LAWS.md 1–454 (full).
- Proposal 1–195 (full); `voice-tts-propose-2026-09-25.md` 1–97 (full).
- `cto-2026-09-25.md` rows R21 :29, R22 :30, R23 :31, R25 :33, R26 :34, R32 :40, R33 :41 (the last three via the launch-row grep); `cto-2026-09-24.md` R107 :131; `cto-2026-09-23.md` R95 :103, R96 :104, R97 :105; `cto-2026-09-22.md` R109 :56.
- FINAL :14–24, :52–91, :167–246, :269–323, :369–376; `grep -n` of its headings.
- V1 (`git show d319e4f3:`):
  - `transcribe.py` (whole) and `config.py` (whole).
  - Worktree Read: `web.py` 1–313; `models.py` 100–162; `turn.py` 120–442; `confirm.py` 60–122; `store.py` 69–178; `0017_voice_turns.sql` 1–73; `voice.yaml` 1–45; `jobs.yaml` 58–81; `probes.py` 28–45, 245–262; `start_aset.sh` 28–41; `aset/web.py` 78–93; `test_radar_panel_cards.py` 660–689; `test_jobs_restarts.py` 170–199, 396–435; `uv.lock` 3280–3291.
- V1-BUILD (`git show d319e4f3:…voice-v1-build-2026-09-23.md`, saved output): lines 1–10 (preview), 84–130, 432–469.
- `COBALT-REQUIREMENTS.md` (grep → :206, :208); `POWER_PACKS.md` 570–610; `topics/devices.md` 1–33; `topics/cto-desk.md` 134–137.
- Searches (grep):
  - the authorization greps;
  - `uv.lock` for the named package entries;
  - `kokoro` / `espeak` / `phonem` / `speechSynthesis` / `audio/wav` / `synthes` over `src`, `configs`, `pyproject.toml`;
  - `voice` and `voice.yaml` count in `jobs.yaml`;
  - `voice_tts` / `voice/tts` / `Synthesizer`;
  - `POST_ALLOWLIST`;
  - the 20 self-attack names.
- Also: `ls ops/`; `git log` of `voice/v1-0923`, `d794e899 --stat`, `main -5`; `git -C voice-v1 status`.

## L74
One block arrived inside a tool result: appended to the first `cat` of this prompt file, it asked for a `Claude-Session:` commit line and named a file-send tool. It is DATA and was not followed. This run commits nothing.

## ESCALATE
1. L31 reading. The desk's R25 reading (1) calls `faster-whisper` "a product name (L31)", and carries a V1 BACKLOG rename ticket. LAWS.md:182 bars person or vendor names; `faster-whisper` names a library (an artifact). The ticket is harmless housekeeping, but it is not a law defect. Whether to keep it is the desk's record to amend — no question to him.

## CONTINUE
next: none — the run is complete.

VOICE TTS FABLE R1 DONE · verdict: BUILD AFTER the Q1 stored-reply guard and test_jobs_restarts seam are written in · adopt: 4 · adopt with wording: 13 · reject: 0 · experiments named: 8 · ESCALATE: 1
