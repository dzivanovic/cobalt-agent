BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: 2026-09-22 (start 19:27 ET, rulings written 19:32 ET — `date`)

## DIGEST FOR THE DESK

TRIBUNAL R1: BUILD AFTER the seam document, one landing path, and V-E1–V-E5 plus X1–X9

- T-V1 ADOPT WITH — `append_to_unit` is the ONLY landing path. The build creates the voice unit blank (as in v2). The op is idempotent on `capture <id>`, checked inside the retry closure.
- T-V2 ADOPT WITH — keep transcription in the request, but run it off the event loop (every ASET POST route is `async def`). A stale `running` row reads `failed`. If X1 shows the resident dying, switch to a child process.
- T-V3 ADOPT WITH — V-E2 picks the engine. A system binary is allowed only as a pinned deploy step with its own probe, never a PATH lookup.
- T-V4 ADOPT
- T-V5 ADOPT WITH — a card matched by >1 trade binds nothing (listed as not bound). The "not bound" list needs a home that D3 does not build (A31).
- T-V6 ADOPT
- T-V7 ADOPT
- T-V8 ADOPT WITH — model files live outside the vault and the repo. `voice.yaml` goes into `com.cobalt.aset` `reads:`, so a swap is a config change plus a restart as one action.
- T-V9 ADOPT WITH — `/voice` inherits the existing bind. No new listener or port. W6-A is his and not in V2.
- T-V10 ADOPT WITH — his structure list is user data, so it never goes in committed `voice.yaml` (L32). Bias ships off until X6.
- (a) ADOPT WITH — V1–V18 hold. V19–V21 are correctly experiments. §1 missed six facts (old-tree websocket listener, `async def` routes, `str(v)` form idiom, `upsert_region`, A31 not in D3, `drc-day/voice-no-trades`).
- (b) ADOPT WITH — audio goes straight to D2-2's bytes method, never through `imports.place` (which would fire a DRC build). One landing function is called by both the build and the request.
- (c) ADOPT WITH — transcribe from the stored vault file after a sha256 match. The transitive dependency list comes from X8. V1's fixture is real-shape container bytes with no voice of his.
- (d) ADOPT WITH — idempotency comes from the snapshot, and a concurrent edit gets one retry and then refuses. Inside `market_reset`: refuse, state `not landed`. A sync revert after landing is X4.
- (e) ADOPT WITH — the server checks that the card id or trade key belongs to the form's date. Zero bytes or an unknown container fails. A size limit is his key. Trading PC: NONE.
- (f) ADOPT WITH — one seam document with 8 named entries before V2/V3 prompts. Two proposal points change the DRC FINAL (initial body, A31) and are carried.
- (g) ADOPT WITH — V1 gets its own `cobalt voice` CLI group (D3-4 owns `cobalt drc`). No migration number is assumed. The 19 h estimate holds as the proposal's own, UNVERIFIED.
- Experiments: V-E1–V-E5 kept (V-E4 and V-E5 widened) plus X1–X9, 14 in total.
- Owner items: W1–W6 framed as the proposal frames them, except W2-B (conflicts with L57) and W3's MB/min figure (UNCITED). Missing: W7 (clip length / transcribe time / upload size are his keys), W8 (vocabulary list and bias switch), W9 (no-trade voice unit under W5).
- WITHDRAWN: 1 · ESCALATE: 3

## Rulings

### T-V1 — landing
**ADOPT WITH:** "His unit `drc-trades/voice-<trade_id>` is created BLANK exactly as v2 T6 / D3-2 create it. Every transcript lands through ONE function, `land_pending(date)`. It is called by the build right after the voice units are created, by the upload request after a transcribe, by the page's retry, and by `cobalt voice land --date`. For each bound, transcribed, not-landed capture whose unit exists, it calls ONE new `VaultWriter.append_to_unit(path, section, unit_id, block)`. `append_to_unit` gates on `_session_gate`, runs through `_write_with_retry`/`_commit` (the same sha256 + mtime guard), and computes inside its build closure, from that snapshot: if the unit body already contains `capture <id>`, it writes nothing, returns `already_landed`, and the caller marks the row landed; otherwise new text = old text with the block inserted immediately before the unit's close marker. It asserts that removing the inserted bytes gives back the old text byte-for-byte. It versions `unit_before`/`unit_after` on `vault_writes`, reports action `updated`, and never merges, reorders or removes a line. After its one retry, a second concurrent change is a loud refusal and the capture stays `transcribed, not landed`."
- The proposal's §4.1 (initial body at creation) plus §4.2 (append) is two landing writers of one unit (L3). §4.1 also changes v2 T6's "creates blank" (`DRC-AUTOMATION-v2:139`; `50-drc-d3-build.md:9`, `:20`). One path removes both problems. Cost: one extra atomic rewrite per capture at build time. Nothing is added to D3's `build.py` beyond one call.
- It is not an "upsert again": `upsert_unit` merges via `merge3` against `_merge_base` (`writer.py:724-733`). The append replaces nothing, so R99's "a re-drop never rewrites them" holds.
- Why the check must sit inside the closure: `_write_with_retry` re-calls `build(snapshot)` on a `NoteChangedOnDisk` (`writer.py:535-552`). Scenario: the build's `land_pending` and a 17:10 request's `land_pending` both read the unit without capture 7. The request commits first. The build's `_commit` sees the sha change (`:463-469`) and retries, and its closure now finds `capture 7`, so it skips. Without the check, capture 7 lands twice.
- The proposal's "byte-prefix check" alone is a tautology when computed from the same snapshot. The guard that catches his concurrent edit is `_commit`'s. The removed-bytes identity is the real invariant.

### T-V2 — sync in request vs one-shot job
**ADOPT WITH:** "The upload request writes the audio through the bytes method, inserts the `drc_voice` row `pending`, and then runs the ONE transcribe function OFF the ASET event loop (a plain `def` route or an explicit thread offload, never a blocking call inside an `async def` route). The row goes `running` → `done | failed` (L18). A `running` row older than the configured transcribe time limit is rendered and treated as `failed: stt stale (process died)` by the page, the retry and the heartbeat probe; the retry re-runs the same function. If X1 shows that an engine fault kills `com.cobalt.aset`, or V-E5 shows the resident's memory is too heavy, transcription moves to a child process running `cobalt voice transcribe --id <n>` (the same function), which the request waits on up to the limit."
- Fact: every POST route in `aset/web.py` is `async def` (`:946`, `:1047`, `:1139`, `:1182`, `:1240`, `:1295`, `:1347`, `:1386`, `:1391`), and `grep run_in_threadpool|to_thread` → 0. Scenario: 10:04 capture on a CLOSED card, and a transcribe taking T s (UNVERIFIED — V-E5) inside an `async def` blocks the loop. At 10:04+5 s his `/size` POST for the next card waits T s. Whether it blocks is a behaviour claim → X2.
- A process death leaves `running` forever: an exception handler cannot run after a SIGKILL, and D2's E11 (`49-drc-d2-build.md:23`) proves only a raised exception. The stale rule reuses the proposal's own limit key and adds no number.

### T-V3 — engine
**ADOPT WITH:** "V-E2 picks the engine and model on his clips. A Metal engine that needs a system `ffmpeg` or a built binary is taken only if faster-whisper fails V-E2 on his own accuracy/latency keys. The binary then enters as a named, version-pinned deploy step in `ops/README.md`, located by an absolute path in `voice.yaml`, with a heartbeat line that probes it (L9). Never a `PATH` lookup, never an unpinned `brew install`."
- V16 holds (`ls /opt/homebrew/bin/{ffmpeg,sox,whisper-cli}` → none). A PATH lookup would bind to whatever a later Homebrew upgrade puts there, so a replay (L57) would not reproduce.

### T-V4 — fallback
**ADOPT.** One engine, loud pending, audio kept, retry. He can always type (the DRC never waits on voice). A second local engine is a second dependency set under L15 for a case V-E2/X1 have not shown to exist.

### T-V5 — binding
**ADOPT WITH:** "A capture binds to exactly the key of the control it was recorded on (card id, or trade key on `/drc`). At landing, a card capture resolves to a trade only through the DRC build's own card match (`AsetStore.for_date`, nearest prior card, same ticker + direction, within `limits.card_match_window_minutes`). A card that no trade matches, a card matched by MORE THAN ONE trade, or a day whose window key is unset leaves the capture unlanded and listed `voice not bound: card <id> — <no trade | k trades | window not given>`. It is never split, never guessed onto the earliest or latest trade. The list renders on the `/drc` page and in ONE Cobalt unit that V3 creates and upserts (name settled in the seam document), because D3 builds no A31 section."
- Scenario: 09:41 entry on card 812, exit 09:50. 10:02 re-entry, same ticker and direction, no new card (B2 attempt #2). Both DAS trades take card 812 as "nearest prior card" (`v2:90` does not forbid it). A 09:55 capture about attempt #1 would go into whichever trade a tie-break picks. So: not bound, and he re-records on the `/drc` trade row.
- Window unset: D3 renders every trade `card: not matched (window not given)` (`50-drc-d3-build.md:20`), so every card capture is unbound until D4's key is set. That is loud and correct.
- A31 "open items carried forward" is a v2 §13 row (`v2:295`) that D3 does not build (`50:28`, "A26–A39 sections other than the ones listed"). The proposal's "the DRC lists it under A31" (`DRC-VOICE-PROPOSAL:46`, `:60`) needs a home.

### T-V6 — pre-DRC holding
**ADOPT.** Holding in `drc_voice` plus the imports dir is the only lawful form. A write into the day's trade note would be a second landing writer (L3), and the trade-note seam (`trade_note_path`, v3) is not built. The note does not exist before the build (R66/R93; D3 creates it).

### T-V7 — field mapping
**ADOPT.** Verbatim only (SPEC §9 heading "Non-negotiables"; R101 keeps judgement in his coach session). Any later mapping is its own design item, in shadow, quoting its source span (CLAUDE.md "verbatim source quotes").

### T-V8 — model provisioning
**ADOPT WITH:** "The model files live in ONE directory named by a `voice.yaml` key, outside the vault (the imports dir syncs to every device, R92) and outside the repo. They are fetched once by a named deploy step pinned to a revision, and each file's sha256 is recorded in the deploy report. The runtime loads with network access disabled (`local_files_only`, proven by X7); a missing file is `FAILED` naming the path. `configs/cobalt/voice.yaml` is added to `com.cobalt.aset`'s `reads:` in `configs/cobalt/jobs.yaml` (beside `configs/dev/aset.yaml`, `jobs.yaml:67-68`), so a model swap is a config change plus that resident's restart as one action (L42). The model id and revision land on every `drc_voice` row (L57)."

### T-V9 — surface
**ADOPT WITH:** "`/voice` and the `/drc` row control are routes on the existing ASET app and inherit its bind exactly (`configs/dev/aset.yaml:39-41`, the local override's `server.bind`). V2 adds no listener, port, certificate or `tailscale serve`. W6-A (HTTPS on the tailnet) is a new exposure of an unauthenticated page: his to rule, built only as an ops item after his word. The access token stays the backlog item (`BACKLOG.md:150-151`)."
- Whoever can reach the page today can already write cards and the note (`POST /size`, `web.py:945-954`). The new class is audio bytes into the SYNCED vault with no size limit. The limit is his key (OWNER W7), not a reason to rebind.

### T-V10 — vocabulary bias
**ADOPT WITH:** "The decoding hint is off unless `voice.yaml`'s switch enables it. When enabled it reads the day's card tickers from `aset_sizings` and his structure list from HIS config home (`trader_settings`, or his note, never committed config, L32; SPEC §7 heading 'Config (trader-specific, never hard-coded)'). The exact hint text is stored in `params` (L57). It is enabled only after X6 shows no hint word appearing in a transcript where he did not say it."
- A decoding hint is not inference about his state. But if it inserts a ticker he never said into a block labelled verbatim, the verbatim claim becomes false. That is an unrun engine behaviour → X6, not a defect.

### (a) Fact base
**ADOPT WITH:** "§1 adds: V22 the old tree carries a websocket Mattermost listener (`src/cobalt_agent/interfaces/mattermost.py`), which the new core must not import (`notify/mattermost.py:6-11`), so V6 holds for the new core only. V23 every ASET POST route is `async def` with no thread offload (`aset/web.py:946` …; grep `run_in_threadpool|to_thread` → 0). V24 the form idiom `{k: str(v) …}` (`web.py:947`, six sites) stringifies values, so the upload route reads the `UploadFile` itself. V25 `VaultWriter` has three write ops today: `create_if_absent :559`, `upsert_unit :644`, `upsert_region :918`; `append_to_unit` is the fourth. V26 A31 is not built by D3 (`50-drc-d3-build.md:28`). V27 D3 creates a second his-voice unit, `drc-day/voice-no-trades`, on no-trade days (`50:6`)."
- V1 HOLDS (my grep over `src configs ops dev_utils pyproject.toml` → `cards/models.py:240`, `ops/pg_role.py:15,19`, `generate_constitution.py:291` only; `src/` includes `cobalt_agent`).
- V2 HOLDS `REQUIREMENTS:206-208`. V3 HOLDS `08-documentation-audit.md:82`. V4 HOLDS (CLAUDE.md "Interfaces:" bullet). V5 HOLDS `MVP-CHARTER:412-413`. V6 HOLDS `notify/mattermost.py:6-11`; `S3-EXITS-v3:65`.
- V7 HOLDS `web.py:83`, `:384`. V8 HOLDS `aset.yaml:36-41`; `aset.local.yaml:25-28` (bind `lan` at `:28`).
- V9 HOLDS `writer.py:457`, `:470-473`, `v2:70`. The bytes method is not on any branch (`git log --all -- src/cobalt/drc` → empty).
- V10 HOLDS `v2:139`, `50:9`. V11 HOLDS (R66 `cto:77`, R93 `:49`; R91 redefines "both" as trading log + stats log, `49:6`). V12 HOLDS `cto:41`.
- V13 HOLDS at heading level (SPEC `:22` §1.2, `:244` §9; field keys not re-read, L32 scope). V14 HOLDS `v2:311-326`.
- V15 HOLDS (`devices.md:8`, `:12`, `:17`; `ls ~/.lmstudio/models/*` → Qwen models only). V16 HOLDS for `ffmpeg`, `sox`, `whisper-cli`. V17 HOLDS `uv.lock:1983`, `:5310`; `grep ctranslate2|onnxruntime|faster-whisper|mlx-whisper` → 0. V18 HOLDS `devices.md:11`, `:31`; `cto-2026-09-20.md:264`.
- V19, V20, V21 are correctly UNPROVEN and correctly experiments (V-E1, V-E2, V-E3).

### (b) L3 — one path
**ADOPT WITH:** "Voice audio is written by calling D2-2's bytes method directly, NEVER through `drc/imports.place`. `place()` recomputes the date's state and writes a `DrcInputsPlaced` event plus a build on READY (`49-drc-d2-build.md:21`), so a voice file routed through it would trigger a DRC build per capture. The audio path is flat in the date folder: `1 - Trading/5 - Review/_imports/drc/<date>/voice-<capture_id>.<ext>`, inside D2-2's confinement to `…/<YYYY-MM-DD>/` (`49:20`), no `voice/` subdirectory."
- Walk. 11:00 capture on card 812: the request calls bytes-method(audio), which writes a `vault_writes` row; then `drc_voice` insert; then transcribe; then `land_pending(D)`. The note is absent, so it is held.
- 16:40 both logs parsed, so the build runs: `create_if_absent` from his template, then units, with the voice unit blank via `upsert_unit(skip_if)`, then `land_pending(D)`. That resolves 812 → trade T1 and calls `append_to_unit`.
- 17:10 capture on the `/drc` row T1: bytes, row, transcribe, `land_pending(D)`, append.
- 17:30 re-import: `create_if_absent` skips (`writer.py:568-578`), the voice unit's `skip_if` skips, and `land_pending` finds every row landed, so zero writes.
- Writers: audio = the bytes method only. His unit = `upsert_unit` once (create) plus `append_to_unit` (land). Both are `VaultWriter`, the vault-write expert (L40). One transcribe function, called by the request, the retry and the CLI.
- With the proposal's §4.1 the build would be a second landing writer. It is struck in T-V1.

### (c) Local-first transcription
**ADOPT WITH:** "The transcriber reads the audio from the vault path the bytes method returned and verifies its sha256 against the `drc_voice` row before decoding. It never transcribes request bytes directly, so no transcript exists without its stored audio (L57). V1's test audio is REAL-SHAPE, not his voice: a container with the codec and parameters of the phone's actual output (V-E3), carrying synthetic sound. His clips stay on the host for V-E2 and never enter git (L32; the L45 companion "real-shape, not verbatim"). Before V1, X8 lists every new transitive package the lock gains, and each is named in V1's report against L15's four gates."
- L15: faster-whisper is industry-standard and is the requirement's own named choice (V2). "Reviewed-clean" and "conformant" cannot be shown from reads. The proposal's transitive list (`ctranslate2`, `av`, `onnxruntime`) is UNVERIFIED → X8.
- Memory beside the 88 GB wired limit (`devices.md:8`) is argued, not measured → V-E5.
- What he sees: a red page line `transcript pending — local speech-to-text down (<class>)`, and a heartbeat line. The model for that probe is `vaultwrite_blocks` (`heartbeat/probes.py:469-497`): a DB count of `failed`, stale-`running` and `not landed` rows today. Loud (L1/L9).

### (d) The append-only unit
**ADOPT WITH:** "`append_to_unit` refuses inside `market_reset` through `_session_gate` (`writer.py:387-416`); the capture stays `transcribed, not landed — market reset`, and the next `land_pending` call after 21:00 lands it. A re-drop or re-build never re-lands, reorders or removes a block: the unit is `skip_if`-created once, and `land_pending` skips landed rows and any unit body already carrying `capture <id>`. A vanished trade's unit keeps D3's `orphaned` line. A capture bound to that trade key is still appended to that existing unit. Captures bound to a trade key absent from the current trading log and with no unit are listed as not bound. Nothing deletes or moves a block."
- Crash between the vault write and the row update: the next `land_pending` finds `capture <id>` in the snapshot, writes nothing and marks the row landed (T-V1). This is idempotent.
- His edit mid-append: `_commit` aborts on sha/mtime (`:463-469`), retries once from a new snapshot that contains his edit, and appends after it. A second change is a loud refusal. His bytes never change.
- Sync revert: an Obsidian Sync copy that drops an already-landed block after landing is not detected by any path (append does no merge; see WITHDRAWN). The block survives in `drc_voice`. Whether that happens is X4.

### (e) Capture surfaces
**ADOPT WITH:** "The voice route validates server-side that the posted card id is an `aset_sizings` row of the posted date (`AsetStore.for_date`), or that the trade key is a trade of that date's current parsed trading log (D2-3's screenshot rule, `49:21`). Anything else is `FAILED` and nothing is stored. A zero-byte file, or a container header outside the set V-E3 proves, is `FAILED` naming the file. An upload over his size key is `FAILED` (OWNER W7). Inside `market_reset` the upload is refused like every D2 upload (R102, `49:9`)."
- Microphone: V19/V20 → V-E1. The file-input path (W6-B) needs nothing new beyond D2-1's direct `python-multipart` pin (`49:19`).
- Trading PC: **NONE**. It is a browser tab to the existing page. No install, no agent, no read of the platform.

### (f) The seam with the DRC build
**ADOPT WITH:** "Before any V2/V3 prompt launches, the desk settles ONE seam document, cited by both the DRC build prompts and the voice prompts (L72 P-b), holding: (1) the bytes method's final name and signature, and whether it creates a missing `<date>/` folder (a card capture at 11:00 precedes every DRC import of that day; `create_if_absent` refuses a missing parent, `writer.py:580-584`); (2) the voice file name inside `<date>/`; (3) `drc-trades/voice-<trade_id>`: section, placement, blank create; (4) the `trade_id` format and whether it is stable across a superseding trading log (X9); (5) the build's single call site for `land_pending` after unit creation; (6) the name of the 'voice not bound' unit (T-V5); (7) `aset/web.py` route order (D2's block sits at the end of the file, `49:22`; voice routes go after it); (8) CLI groups (`cobalt drc` = D3-4; `cobalt voice` = V1)."
- Stacks: V2 stacks on D2-2 (bytes) and D2-4 (`/drc`). V3 stacks on D3-2 (the voice unit, `build.py`). D2 never deploys without D3 (`49:3`), so V2 and V3 effectively both follow the D2+D3 deploy.
- Shared files: `aset/web.py` (D2-4 · V2), `vaultwrite/writer.py` (D2-2 · V3), `drc/build.py` (D3-2 · V3, one call), `cli.py` (D3-4 · V1), `placement.py` + `db_migrations` (D1 · V1), `jobs.yaml` (D3-5 · V2 `reads:`), `smoke/s2.yaml` (D3-6 · V3), `heartbeat/probes.py` (V4 only).
- Changes to the DRC FINAL, carried and not folded: the proposal's §4.1 "initial body" (struck by T-V1), and "the DRC lists it under A31" (A31 not in D3). A voice-owned unit replaces it (T-V5).

### (g) The chunks
**ADOPT WITH:** "V1's CLI is its own group `cobalt voice transcribe [--dry-run] [--id] | land --date` in `src/cobalt/voice/cli.py`, registered once in `cli.py`, never inside D3-4's `cobalt drc` group, so V1 can run before or beside D3 without both creating one parser. V1's migration takes no number: main ends `0011`; unmerged branches add `0012` (`02d67a6`) and `0013` (`61a283f`); DRC D1 adds one unnumbered; the desk numbers V1's at the L68 gate. RESTARTS: V1 none (no resident imports `cobalt.voice` until V2); V2 `com.cobalt.aset` plus the `jobs.yaml` `reads:` entry; V3 `com.cobalt.aset`; V4 whatever `cobalt jobs restarts` derives for the probe; a model swap = `com.cobalt.aset`."
- Seats: V1–V3 are write paths (user table, vault bytes, vault unit), so the L29 Opus 5 floor applies. The mode question is the desk's (L63 status note; the DRC builds run the auto-mode "dev lane", `49:1`).
- Hours: 5+6+6+2 = 19; 19 × 1.4 = 26.6 ≈ 27. These are the proposal's own estimates, and the factor is UNVERIFIED. My changes net ≈ 0 (the §4.1 branch is removed; the idempotency check, stale rule and own CLI group are added). No re-derived schedule.

## Self-attack

Writers and readers found (`grep -rn <name> /Users/cobalt/cobalt/src/cobalt`):
- `create_if_absent`: callers `prefill/drc.py:427`, `prefill/trade_note.py:151`, `prefill/daily.py:523`, `radar/propose.py:753`, `aset/daily_note.py:184`, `seatusage/runner.py:107`; def `writer.py:559`.
- `upsert_unit`: callers `prefill/drc.py:447`, `prefill/daily.py:558`, `daymode/note.py:159`, `heartbeat/runner.py:205`, `taxonomy/note_migration.py:872,880`, `taxonomy/catalyst.py:404`, `taxonomy/cli.py:223`, `replay/line.py:172`, `radar/propose.py:756`, `aset/daily_note.py:185`, `seatusage/runner.py:126`; def `writer.py:644`.
- `skip_if`: `writer.py:652`, `:680`, `:780` only. No caller on main; D3-2 adds the first (`50:9`, `:20`).
- `_commit`: VaultWriter's is `writer.py:457`, called only at `:527`. The other hits are `before_commit` hooks in DB stores (unrelated).
- `_session_gate`: `writer.py:387`; callers `:565`, `:664`, `:922`.
- `assert_writable`: `settings/cli.py`, `settings/card.py`, `cards/store.py`, `daymode/store.py`, `vaultwrite/writer.py`, `radar/store.py`, `aset/web.py` (`:954`), `session/guard.py`, `session/__init__.py`.
- `market_reset`: count hits in `session/*` (clock 13, cli 4, guard 3, store 3, models 2, `__init__` 2), `heartbeat/{runner,probes}` 3 each, `radar/runner` 3, `writer.py` 3, `cards/store.py` 5, others ≤2.
- `_imports`: `vault.py:101` (comment), `smoke/checks.py:20` (unrelated word).
- `request.form`: `aset/web.py:947,1048,1147,1190,1247,1282`.
- `UploadFile`: 0.
- `bind` (word): `aset/config.py:78-86`, `aset/__main__.py:4,6,30,32,41`; `smoke/checks.py:24` and `db_migrations/cli.py:141` are unrelated.
- `sheet_http`: `heartbeat/probes.py:128`, `heartbeat/runner.py:133`, `aset/web.py:891`.
- `Probe`: `heartbeat/probes.py:30` plus constructors; readers `heartbeat/render.py`, `runner.py`, `__init__.py`.
- `DECLARED_TABLES`: `db_migrations/placement.py:106,125,170`.
- `aset_sizings`: 36 files (stores, migrations, `prefill/drc.py`, `daymode/drc.py`, `replay/*`, `aset/{store,web}.py`, `devdb.py`, `session/cli.py`, `db_migrations/*`).
- `for_date`: `aset/store.py:292` (readers `prefill/drc.py:387`, `prefill/daily.py:507`); `daymode/store.py:55` is a different class.
- `voice`, `whisper`: 0 in `src/cobalt`. `transcri`: `cards/models.py:240`, `ops/pg_role.py:15,19` only.
- `drc_`: `smoke/checks.py`, `prefill/{cli,config,drc}.py`, `daymode/{drc,config,propose,cli}.py`, `replay/{line,runner,cli}.py`, `db_migrations/placement.py`.
- Names the DRC build ADDS, not on main (checked in `49`/`50`): `write_import_bytes` `49:20`; `drc_imports` `49:21`; `run_drc_build` `49:21`, `50:20`; `drc-trades/voice-` `50:9`, `50:20`. `git log --all -- src/cobalt/drc` → empty.

My text walked against this list: the only caller that could write `drc-trades/voice-*` besides D3-2's `upsert_unit(skip_if)` is my `append_to_unit`. `land_pending` is its one caller, and it is reached from the build, the request, the retry and the CLI. No second writer. `vault.py:99-101`'s `_imports/` is R3's ownership comment; D2-2 re-points it (`49:20`), and voice adds no second location.

WITHDRAWN: "`append_to_unit` must apply L28's sync-revert carve-out (`_merge_base`) before appending" — `writer.py:822-823`: `_merge_base` is called only by `upsert_unit`/`upsert_region` before `merge3`. An append does no merge and has no base leg, so the carve-out has nothing to act on. Replaced by X4.

## Experiments (L70)

- V-E1 KEPT (phone + trading-PC browser mic, secure context, file-input hand-off, PC mic).
- V-E2 KEPT (engine × model on 5–10 of his clips; accuracy, latency, RSS, determinism).
- V-E3 KEPT, and it feeds the (e) container set and the (c) fixture shape.
- V-E4 WIDENED to X3/X4 below.
- V-E5 WIDENED: RSS and first-clip latency with LM Studio serving, plus the phone's HTTP request lifetime on a long clip while the request waits.
- X1: on a dev ASET server with `cobalt_dev`, `kill -9` the resident mid-transcribe, and separately feed a clip that faults the engine. What changes the design: the row stays `running` after respawn (the stale rule is needed, as written), or an engine fault takes the resident down (T-V2 flips to the child process).
- X2: in a dev server, a `/size` POST issued while a transcribe runs. If its latency grows by the transcribe time, the off-loop wording is mandatory (it already is); if not, the claim is closed.
- X3: in the dev vault, `land_pending` twice; a crash injected between the `vault_writes` commit and the `drc_voice` update; two concurrent `land_pending` calls. Pass: exactly one `capture <id>` block each time. Fail: the idempotency check is not in the closure.
- X4: in the dev vault with Obsidian Sync, land a block, then restore an older synced version of the DRC. Does the block vanish, and does anything detect it? Vanishes silently → a probe comparing landed rows with unit bodies becomes a design item.
- X5: on D2's built bytes method, a write when `_imports/drc/<date>/` does not exist, and a `voice/` sub-path. Refuse vs create decides seam entry (1).
- X6: on his clips, the hint on vs off. Count hint words in the transcript that he did not say (checked against his own corrected text). Any count > 0 → bias stays off.
- X7: model load with the network disabled (`local_files_only`) → loads; one model file removed → `FAILED` naming the path.
- X8: in a scratch worktree, `uv add faster-whisper` → the full `uv.lock` diff: every new package, version and license, for L15's gates. An unexpected native or GPL package → tribunal round 2.
- X9: on `cobalt_dev` after D1/D2, re-import a superseding trading log that leaves one trade unchanged. Is its `trade_id` identical? If not, every re-import orphans that trade's voice unit, and seam entry (4) must fix the id rule before V3.

## OWNER (after the tribunal)

- W1 capture points — framed correctly.
- W2 audio retention — B ("deleted once the transcript lands") conflicts with L57 as the proposal's own §6 argues (the transcript on the row is a derived value). If offered, it names the law it sets aside (L73).
- W3 audio home — "~1 MB per spoken minute" is UNCITED; V-E3's real files give the figure.
- W4 cloud STT — framed correctly.
- W5 scope — framed correctly. Its option B should name the target unit R93 already creates, `drc-day/voice-no-trades` (`50:6`) → W9.
- W6 phone microphone — framed correctly (V-E1 decides the options).
- W7 (MISSING / MIS-FRAMED) — the clip length, the transcribe time limit and an upload size limit are his keys (L53: every limit and window is his), not "engine tunables" in committed config as §5 frames them. Until he sets them: no clip limit is enforced, the time limit fails loud (no default), and upload size is unbounded (R103 answered a CSV, not audio).
- W8 (MISSING) — the vocabulary hint, on or off, and the home of his structure list (T-V10).
- W9 (MISSING) — per-day / no-trade voice via `drc-day/voice-no-trades` (sub-case of W5).

## WRONG FACTS

1. `DRC-VOICE-PROPOSAL:46` and `:60` ("the DRC lists it under A31") — A31 is a v2 §13 row (`DRC-AUTOMATION-v2:295`) that the DRC build as drafted does not build (`50-drc-d3-build.md:28` NOT IN D3 "A26–A39 sections other than the ones listed"; the D3-2 unit list at `50:20` has none).
2. `DRC-VOICE-PROPOSAL:83` orders "V2 (after v2 D2 is merged …) → V3 (after v2 D3 …)" — `49-drc-d2-build.md:3`: "D2 and D3 land in ONE deploy … D2 alone never deploys". V2 cannot follow D2 without D3.
3. `drc-voice-propose-2026-09-22.md:47` names only v2:34 / `SPRINT-LADDER:610` as the stale "not on the tailnet" source. `configs/dev/aset.yaml:33-35` and `src/cobalt/aset/__main__.py:4-6` carry the same stale "NOT Tailscale" wording (vs `devices.md:31`). This is incomplete rather than wrong → ESCALATE 3.

## READING

- LAWS.md 1–442 (full).
- `60-voice-tribunal-fable-seat.md` (full).
- `59-voice-tribunal.md` :32–42 (the question paragraph only).
- `DRC-VOICE-PROPOSAL-2026-09-22.md` 1–128; `drc-voice-propose-2026-09-22.md` 1–58.
- `cto-2026-09-22.md` rows R66, R76, R90, R92, R93, R99, R100, R101, R106 (grep); `cto-2026-09-21.md` R46; `cto-2026-09-20.md` R27.
- `DRC-AUTOMATION-v2` 20–231, 308–327.
- `49-drc-d2-build.md` 1–51; `50-drc-d3-build.md` 1–54.
- `vaultwrite/writer.py` 370–846.
- `vault.py` 92–116.
- `aset/web.py` 1–24, 80–84, 382–386, 940–960, plus the def/route grep.
- `configs/dev/aset.yaml` 28–47; `configs/dev/aset.local.yaml` (grep; key names only cited).
- `notify/mattermost.py` 1–15; `heartbeat/probes.py` 30–44 plus the Probe grep.
- `topics/devices.md` (grep, all lines).
- Searches:
  - `grep` for `jobs.yaml` reads, `uv.lock` names, `placement.py` tables, the BACKLOG token, the REQUIREMENTS/audit/charter voice lines, v2 A31, S3-EXITS F27, SPEC headings (`grep -n -E "^#+ "` only), `aset/__main__.py` Tailscale, and old-tree websocket.
  - `ls /opt/homebrew/bin/{ffmpeg,sox,whisper-cli}` and `ls ~/.lmstudio/models/*`.
  - `git -C /Users/cobalt/cobalt log --all` on `db_migrations` (added), `src/cobalt/drc`, `src/cobalt/voice`.
  - The 20 self-attack greps above.
- Not opened: `db_migrations/__init__.py`, `COBALT-REQUIREMENTS:203-210` beyond grep, `uv.lock` beyond grep, `aset/__main__.py` beyond grep, `web.py` :355 and :1081–1086 (L32).

## ESCALATE

1. The A31 home: the voice "not bound" list needs a unit that D3 does not build. The desk places it in the seam document (T-V5, (f)), carried, not folded into the DRC FINAL.
2. The seam document with eight named entries ((f)) is owed before any V2/V3 prompt launches (L72 P-b). It also binds D2-2's bytes method (folder creation), which is not yet built.
3. Stale "trading PC is NOT on Tailscale" wording also at `configs/dev/aset.yaml:33-35` and `src/cobalt/aset/__main__.py:4-6`. This is a desk record item, added to the proposal's ESCALATE 2.

Notes: L74 — a `Claude-Session:` attribution block arrived appended to a tool result in this session. It was not followed, and nothing was committed. MEMORY: none. RULING: none. ASK DESK: none.

## CONTINUE

Authorization verified 19:27 ET: FABLE ROW grep count 0 → R106. R106 at `cto-2026-09-22.md:36` carries all three literals; committed `01b63ffb`; session model `claude-opus-5-5` = R106's. R76 `:67` "You ask me"; R99 `:43`; R100 `:42`; R46 `cto-2026-09-21.md:57`. Proposal committed `1bcc1a89`; its stop line committed `1bcc1a89`. The ten launch strings each count 1 in `22-draft-setups-tribunal.md`.
next: none — ruling complete 19:32 ET.

VOICE TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER the seam document, one landing path, and V-E1–V-E5 plus X1–X9 · adopt: 3 · adopt with wording: 14 · reject: 0 · experiments named: 14 · ESCALATE: 3
