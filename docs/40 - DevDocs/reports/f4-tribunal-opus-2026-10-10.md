BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Sat Oct 10 12:59:51 EDT 2026

## DIGEST FOR THE DESK
TRIBUNAL R1: ADOPT AFTER baseline-built rows, stamp as a row, refresh lock, reuse daymode daily_note_path
- Authorization: FABLE ROW R109 (cto-2026-09-22.md:56, committed 75b2aa57) · launch row R876 (cto-2026-10-10.md:27, all three literals, committed 31503324) · R849 :54 · R95 (cto-2026-09-23.md:103) · proposal + seam committed (8426e8f5) · 10/10 launch strings present in `13-f15…` · this session = claude-opus-5-5. PASS.
- C1 ADOPT
- C2 ADOPT
- C3 ADOPT
- C4 ADOPT WITH — build Cobalt's proposal from `last_after`, not from disk; disk-built proposal duplicates his inserted line and leaves adjacent rows stale one refresh; one refresh lock.
- C5 ADOPT WITH — `n/a (manual)` only into a COBALT VIX/BTC row; `fields` keys exactly the five tickers.
- C6 ADOPT WITH — stamp line classed like a row (his edit survives); daily's retry uses refresh's builder; calendar flag lives in the trading stamp.
- C7 ADOPT WITH — values-age from the previous flag when already degraded; refresh exits 1 after writing a degraded unit (L9 mission control).
- C8 ADOPT WITH — absent note OR absent trading unit (the sheet's stub) → run_daily_prefill; T12 narrowed to existing notes.
- C9 ADOPT
- C10 ADOPT
- C11 ADOPT WITH — rules unit gets a create-time `as of HH:MM ET` line (Charter:82-83 "Cobalt blocks stamped").
- C12 ADOPT WITH · SELF: yes · EVIDENCE: UNMEASURED — L29-floor seat, default Opus 5.5; never auto mode on the build launch.
- S1 ADOPT WITH — reuse `cobalt.daymode.note.daily_note_path` (L3); `ensure_daily_note` runs the whole daily path.
- S2 ADOPT
- S3 ADOPT
- (a) ADOPT WITH — §2 holds; add missed: aset stub creator, existing path helper, radar restart, smoke row.
- (b) ADOPT WITH — the walk confirms §3 and finds 3 sequences that break the proposal's §4.4; C4 wording closes them.
- (c) ADOPT WITH — L52/L8 not triggered; L1 exit table added; cadence is not L53's scan cadence.
- (d) ADOPT WITH — seam misses daymode/note.py, smoke/s2.yaml, generated.yaml, ops/README.md.
- (e) ADOPT WITH · SELF: yes · EVIDENCE: UNMEASURED — one chunk, GUESS 6–8 h, 11 with-DB tests under L76.
- (f) ADOPT WITH — RESTARTS: com.cobalt.aset AND com.cobalt.radar (tunables.yaml), bootstrap prefill-refresh; R3 missed radar.
- Experiments: X1 real-merge walk (T2b/T3/T3b/T15/T16/T17) · X2 Obsidian Sync stale revert >10 writes · X3 table re-padding on open · X4 GFM render of stamp + VIX header · X5 Finviz 429 with radar at ceiling · X6 heartbeat on a failed one-shot · X7 jinja2 Undefined on partial context · X8 two concurrent refreshes · X9 ET stamp under non-ET TZ · X10 launchd 105-entry plist.
- OWNER: none (C2 cadence fails the owner test: an engine tunable, Charter:84 delegates "config cadence").
- SELF: yes lines: 2 · UNMEASURED: 2.
- WITHDRAWN: 3.
- ESCALATE: 1 (a `git status` of ~/cobalt printed the hub report's filename; content never opened — desk judges blindness).

## Rulings

### C1 — new `prefill refresh` subcommand + job `com.cobalt.prefill-refresh`; `prefill daily` unchanged
ADOPT
- `Schedule._one_shape` allows exactly one of `at` / `every_min` / `every_min_tunable` (jobs/config.py:94-101): the 05:15 `at` and a windowed interval cannot share a row. A second job is forced, not chosen.
- 05:15 idempotency (daily.py:491-504) stays untouched.

### C2 — 30 min, 05:45–15:45 ET, weekdays, tunables `source: dwv`, `status: proposed`
ADOPT
- Re-derived: firings = 05:45 + 30k while ≤ 15:45 → (15:45−05:45)/30 + 1 = 600/30 + 1 = 21 per weekday (jobs/config.py:198-219 expands exactly this); 08:45 = 05:45 + 6×30 → a firing (the Charter test, Charter:86). Plist entries = 21 × 5 weekdays = 105.
- Finviz per run: 1 screener (market.py:63-67) + 2 calendar (calendar.py:48-53, called at daily.py:517-518) = 3; per 30 min = 0.1 rpm; 63 a weekday.
- L53: "the scan cadence" is the radar's (radar/notes.py:338-341 names the radar window/bucket); the refresh is an engine tunable whose cadence the Charter itself delegates ("refreshes on config cadence", Charter:84). `source: dwv` is a legal enum (tunables.py:70-73). His ceiling value is not changed (see C9).

### C3 — refresh only `trading/market_table` and `market_calendar/market_calendar`
ADOPT
- rules = his ticks, daymode has its own writer (daymode/note.py:128-165), heartbeat is its own (heartbeat/runner.py:205). Nothing else in the template is Cobalt's to repeat.

### C4 — ownership rule
ADOPT WITH:
> "Refresh builds Cobalt's proposed body for `trading/market_table` FROM `store.last_after(note, "trading", "market_table")` — the baseline — never from the on-disk text. Every line of the baseline is kept as it is, except (1) the stamp line, replaced with a fresh one, and (2) each SPY/QQQ/IWM row that is COBALT, replaced with fresh values. A row, or the stamp line, is HUMAN — kept exactly as the baseline has it — when (a) its on-disk text differs from its baseline text and matches no row of `store.recent_afters(...)`, or (b) a `store.overrides_for(note)` row with `section = trading` and `unit = market_table` has a `human_text` line byte-equal to its on-disk text. Lines on disk that are not in the baseline are never put into the proposal: the merge carries them (merge.py:20-21) and records his edits as overrides (merge.py:23-26). When `last_after` is None the unit is not written, the run report says `baseline missing` and the run exits 1. `prefill daily` and `prefill refresh` take one exclusive non-blocking lock per note for their whole run; a second run exits 0 printing `NOT RUN — prefill already running for <note>`."
- Walk 1 (his inserted line, T3 — proposal as written): base=[st1,"",VIX,sep,SPY_o,QQQ_o,IWM_o,BTC]; at 06:00 he inserts X before QQQ; 06:15 proposal-from-disk = [st2,"",VIX,sep,SPY_n,X,QQQ_n,IWM_n,BTC]. merge3: human view `insert` at 5 → inserts_at[5]=[X] (merge.py:90-91); cobalt-vs-base = replace(4,7→4,8) (no common line); not touched → out gets cobalt[4:8] (SPY_n,X,QQQ_n,IWM_n) THEN pending [X] (merge.py:142-159). Disk after: X twice. His text changed on the first refresh.
- Walk 2 (his SPY edit, T2 — proposal as written): 06:15 cobalt carries SPY_h; base SPY_o,QQQ_o,IWM_o; replace(4,7) touched (group at 4) → SPY_h, then base[5], base[6] (merge.py:150-153): QQQ/IWM keep 05:15 values while the new stamp says `as of 06:15 · QQQ cobalt`. A false-fresh stamp for one refresh.
- With the replacement: 06:15 cobalt = base SPY_o (equal) + QQQ_n, IWM_n → equal-branch emits his SPY_h with an override (merge.py:127-135, conflict False); separate replace refreshes QQQ/IWM. 06:45: baseline now holds SPY_h, rule (b) keeps it; X now in the baseline is kept. 08:45 same. No byte of his changes.
- Walk 3 (race, X8): scheduled 06:15:00 refresh A and manual 06:15:01 refresh B both read baseline L0 (no X); A writes L1 (X carried by the merge); B's proposal from L0 lacks X; base=L1=human → Cobalt "deletes" X (merge.py:141-159, untouched) → X erased. `job_run` serializes nothing (jobs/wrapper.py:125-200) → the lock. Price: ~10 lines in `cli.py`/`daily.py`, T15.
- Residual (T3b decides): an insertion anchored INSIDE the run of refreshed rows (before SPY/QQQ/IWM) is emitted after the run once (merge.py:143-159 `pending`) — moved, not lost. If T3b is red on the built code: merge.py, inside a `replace` with `b2-b1 == c2-c1`, emits `inserts_at[b1+k]` before `cobalt[c1+k]` (~6 lines, the shared write path, one merge test). Else accept.
- `writer.py` stays unchanged; calendar stays whole-unit as proposed.

### C5 — VIX/BTC `n/a (manual)`; owner map `daily_refresh.fields`
ADOPT WITH:
> "`n/a (manual)` is written only into a blank cell of a VIX or BTC row that is COBALT under §4.4; a HUMAN VIX/BTC row is carried exactly as the baseline has it, blank cells included. `daily_refresh.fields` must name exactly SPY, QQQ, IWM, VIX and BTC — a missing or unknown key, or `cobalt` for VIX or BTC, refuses the load."
- Failing sequence (proposal as written, T1's own edit): 05:15 VIX row `| VIX | n/a (manual) | n/a (manual) |` (template, daily.md.j2:41 after F4); 06:00 he replaces it with `| VIX | 18.2 |  |`; 06:15 the "blank cell gets n/a" exception proposes `| VIX | 18.2 | n/a (manual) |` → touched → his row kept (override), baseline absorbs it (writer.py:795); 06:45 base==human, Cobalt's row differs → Cobalt wins (merge.py:14-15) → his row changed before 08:45. T1 red.
- VIX is the table's HEADER row (daily.md.j2:41-42): the per-row rule must include line 1 of the table; noted for the builder.

### C6 — stamp + flag line first in each refreshable unit, ET via `SessionClock.to_et`
ADOPT WITH:
> "The stamp line is classed by the §4.4 rule like a row: Cobalt's stamp line is the unit's first line unless HUMAN; a HUMAN stamp line is kept as the baseline has it and a fresh stamp line is inserted above it. Every body F4 writes to `trading` or `market_calendar` — the template at create, `prefill daily`'s retry (daily.py:563-588, state `retry`) and `prefill refresh` — comes from one builder and starts with the stamp line. The calendar's ownership flag (`calendar cobalt` / `cobalt-degraded` / `human`) is written in the TRADING unit's flag line, because a calendar unit that is his is never written."
- Failing sequence (R5 as written): 06:00 he appends "— check QQQ gap" to the stamp line; 06:15 merge keeps it (touched, override); baseline absorbs (writer.py:795); 06:45 base==human, Cobalt proposes a new stamp → Cobalt wins (merge.py:14-15): his words erased. L28 "a Cobalt line he changed → human wins" (LAWS.md:197) is broken; R5's "Accepted" cannot stand.
- Failing sequence (calendar flag): 06:00 he edits an event; 06:15 refresh leaves the calendar unit unwritten (§4.4) so its first line still reads `as of 05:15 ET · calendar cobalt` — a false flag all day.
- Failing sequence (daily retry): `prefill daily` re-run on a FAILED table builds `build_market_table_body` = table only (daily.py:336-353) → the stamp line is missing from Cobalt's proposal, present in base and human → Cobalt's deletion wins.

### C7 — dead source: keep last values, flag `cobalt-degraded` with their age, never `FAILED`
ADOPT WITH:
> "The age in `values as of HH:MM` is read from the baseline's flag line: the field's previous `values as of` time when it was already degraded, else the baseline stamp's `as of` time. A refresh that writes any degraded field writes the note first, then ends with exit code 1 and `job.result.degraded = [<fields>]`, so F17 marks the run failed (jobs/wrapper.py:178-191)."
- Failing sequence: 07:45 good; 08:15 Finviz dead → `as of 08:15 ET · SPY cobalt-degraded (… values as of 07:45)`; 08:45 still dead → "time from the previous stamp line" = 08:15 → says values as of 08:15; they are 07:45's.
- L9 (LAWS.md:133): a dead source is a red banner on mission control, not only a note flag; exit 0 leaves the job row green (cli.py:61-70). Whether the heartbeat turns a failed one-shot red: X6.

### C8 — refresh on an absent note creates it through the daily path
ADOPT WITH:
> "When today's note is absent, or present without a `trading` unit (the sheet's stub, aset/daily_note.py:103-104, :184), `prefill refresh` calls `run_daily_prefill(when)` — rules regeneration included, exactly the 05:15 path — returns its result and does not refresh in the same run. An absent calendar unit with his text under the heading stays skipped (daily.py:578-582). T12 reads: 'a refresh of a note whose trading unit exists never calls `regenerate_rules_config`'; T8 covers the absent note AND the stub; `configs/cobalt/generated.yaml:36` `written_by` names both jobs."
- The proposal contradicts itself: §4.1 runs the daily path, which calls `regenerate_rules_config()` (daily.py:482), while §4.3/T12 say refresh never calls it.
- Stub scenario: 05:15 job FAILED (exit 1); he saves a card at 06:00 → `create_if_absent(stub)` + cards unit (aset/daily_note.py:184-185); 06:15 refresh: note exists, no trading unit — the proposal says nothing.

### C9 — no prefill consumer in the L53 shared gate; inventory strings updated
ADOPT
- Radar is counted at the ceiling when its rpm is unknown (radar/notes.py:357-363); adding prefill would refuse it. The ungated gap is already the strict xfail (test_finviz_consumers.py:69-75) with its owner (P4 STEP-6). The refresh adds 0.1 rpm inside radar's 04:00-20:00 window: whether Finviz then 429s is X5, not a defect (L70). The strict-xfail reason should also name `prefill-refresh` (text only).

### C10 — manual trigger = CLI only
ADOPT
- Charter:84 asks for "manual trigger"; no surface is named.

### C11 — no stamp on the rules unit
ADOPT WITH:
> "The rules unit carries one create-time line `as of HH:MM ET · rules from Rules.md` as its first line, rendered at create and by `prefill daily`'s absent-slot fill only; refresh never touches it. Whether the daymode unit's stage line satisfies 'stamped' or `daymode.note.render_body` (daymode/note.py:94-97) gains ` · as of HH:MM ET` is settled by the derive (a house question, not an owner item)."
- Charter:82-83 (his text): "the note exists at 05:15 with Cobalt blocks stamped 'as of HH:MM'". Rules is a Cobalt block (daily.md.j2:23-29). One line, no merge risk: the unit is never re-written after 05:15 (daily.py:574-577).

### C12 — build seat Opus 5.5; house B mandatory at check
ADOPT WITH:
> "Build seat: the top implementation model of any house that meets L29 (default Opus 5.5, `claude-opus-5-5`, per SPRINT-LADDER-v0_1.md:939 'S5-P1 · Opus 5'); the build launch is never auto mode (L29, L62 — a vault write path). Check: the L67 BUILD CHECK FLOW with MANDATORY HOUSE B (this build writes his daily note)."
SELF: yes
EVIDENCE: UNMEASURED — RULED L29 (LAWS.md:204), RULED R109; the ladder line is a plan, not a measurement. I did not search check reports for HOLD counts against the Anthropic house on vault write paths; none is cited either way.
- L29 floor: "Claude: Opus 5 floor" and "Any house may hold any seat … once (1) that floor is met and (2) a permission gate is proven" — Opus 5.5 is lawful, not exclusive.

### S1 — F4 owns `daily.py`; F5 imports `daily_note_path`, `ensure_daily_note`, `format_stamp`
ADOPT WITH:
> "F5 imports `cobalt.daymode.note.daily_note_path(day)` (daymode/note.py:238-255, already the shared resolver of heartbeat/runner.py:176-181 and aset/web.py:514, :580); F4 adds no second path helper (L3). `async ensure_daily_note(when) -> DailyPrefillResult` runs `run_daily_prefill(when)` when today's note is absent or lacks the `trading` unit, else returns without writing — never a bare `create_if_absent` with a partial template context. `format_stamp(when) -> str` returns `as of HH:MM ET` through `SessionClock.to_et`, which refuses a naive datetime (clock.py:262-272)."
- A partial context: `Environment(...)` at daily.py:238 sets no `undefined=`, so missing keys would render empty (X7); an empty rules unit then reads `filled` to slot_state (daily.py:435) and is never refilled — a plausible-empty block (L1).

### S2 — separate top-level keys `daily_refresh:` / `checkpoints:`; `prefill:` untouched
ADOPT
- Every `prefill.yaml` reader loads only the `prefill` key through `load_prefill_paths` (prefill/config.py:156-163; callers drc/template.py:38, :70, replay/line.py:211, smoke/checks.py:129, taxonomy/trade_note_migration.py:59, aset/web.py:35). A new top-level key breaks none. Priced alternative (a separate file outside aset's `reads`) saves one aset restart per edit of the block; the block changes rarely → not worth a file.

### S3 — F5's jobs row after F4's; F5 section `market_context` under `### Market Context:`
ADOPT
- Disjoint units; the human `-` (daily.md.j2:52) stays outside; the lock of C4 covers only `prefill daily`/`refresh` — F5 writes another unit and needs none.

### (a) — the fact base
ADOPT WITH (add to `## 2`): "The sheet creates a stub daily note when absent (aset/daily_note.py:103-104, :184) — a second creator. `cobalt.daymode.note.daily_note_path` (daymode/note.py:238-255) already resolves the note path. `tunables.yaml` is in the reads of com.cobalt.aset (jobs.yaml:69) and com.cobalt.radar (jobs.yaml:200). Smoke row K12.1 (configs/cobalt/smoke/s2.yaml:572-579) checks prefill-daily; F4 adds one for prefill-refresh."
- §2 cited lines, each opened: jobs.yaml:207-212 HOLDS · cli.py:30-45 HOLDS · daily.py:463-473 HOLDS · :412-435 HOLDS · :574-577 HOLDS · writer.py:673-690 HOLDS · merge.py:23-26 HOLDS · daily.py:328-353 HOLDS · market.py:7-11 HOLDS · daily.md.j2:5 header HOLDS.
- §3: writer.py:774-795 `unit_after = merged_body` HOLDS; :800-802 HOLDS; :886-890 base = `last_after` HOLDS; merge.py:14-15 base == human → Cobalt wins HOLDS. Three steps confirmed on the code (Walk 2's mechanism).
- §4.8 writer list: heartbeat (runner.py:205), cards (aset/daily_note.py:185), daymode (note.py:159) HOLD; missed the stub `create_if_absent` (aset/daily_note.py:184). No other `upsert_unit` caller targets the daily note (grep list in Self-attack).

### (b) — the ownership walk
ADOPT WITH C4's wording.
- 05:15 create seeds one baseline per unit (writer.py:638-640, :650-670).
- SPY edit 06:00 → 06:15/06:45/08:45: proposal as written = adjacent-row lag (Walk 2), his row survives; with C4 wording: no lag, no change to his bytes.
- Insert in trading unit: proposal as written = duplicate at 06:15 (Walk 1); with C4 = carried, possibly moved once (T3b).
- Calendar edit: whole-unit freeze holds (never written); flag defect → C6.
- Sync revert of a whole unit: per-row (a) misses, writer `_merge_base` takes disk as base (writer.py:886-919) → Cobalt wins cleanly, no override; a revert older than 10 writes (5 h at 30 min) is classed his and frozen (X2) — a writer-wide property.
- Two refreshes same minute: Walk 3 → lock.
- Heartbeat write between store read and refresh write: different unit; snapshot re-taken in build (writer.py:565-566), mtime guard (:492-498) → one retry; second abort raises → exit 1 (cli.py:67-70). No byte of his changes.
- He types the VIX cell: C5 sequence.
- False COBALT: his row byte-equal to a recent Cobalt row → (a) misses, but the merge still keeps his on that refresh (touched → human wins) and (b) holds after. False HUMAN: only via the >10-write revert (X2) or table re-padding (X3).
- Smaller mechanism: yes, in `daily.py`. A repeating-writer mode in writer.py touches the one write path of 12 callers (Self-attack list) and still needs F4's per-row rule; priced larger.

### (c) — L52 / L8 / L1 / L53
ADOPT WITH (add to `## 4`): "L1 exits: dead source → degraded write then exit 1 (C7); unknown/missing `fields` key, `cobalt` for VIX/BTC, a `units` value other than the two → `PrefillConfigError` at load, exit 1 (cli.py:67-70); missing `prefill.refresh_*` tunable → `JobConfigError` (jobs/config.py:133-137, :147-151); note unwritable or changed twice → `VaultWriteError`/`NoteChangedOnDisk` (writer.py:576-580), exit 1; baseline missing → no write, exit 1 (C4); a missed firing → the windowed `is_missed` (jobs/config.py:155-181)."
- L52: F4 reaches no card, scores and ranks nothing; the prebell ranked watchlist is out (§6). L8: no n. L53: see C2 / C9 — no ceiling changed, the cadence is not the scan cadence; `source: dwv`, `status: proposed` is lawful for an engine tunable.

### (d) — the F4/F5 seam
ADOPT WITH (add rows to seam §5): "`src/cobalt/daymode/note.py` — `daily_note_path` used by both, edited by neither · `configs/cobalt/smoke/s2.yaml` — F4 adds one job_row for `com.cobalt.prefill-refresh`, F5 its own · `configs/cobalt/generated.yaml:36` — F4 only · `ops/README.md` plist table — each its own row."
- Order leaves F5 no F4-owned line (seam §1, :9). The three helpers are enough once S1's wording applies. `format_stamp(when)` is ET-correct for a tz-aware `when` (daily.py:479 is `.astimezone()`); a naive one raises (clock.py:262-272).

### (e) — chunks and seats
ADOPT WITH: "ONE chunk (the ownership rule cannot be proven without the job, and L75 keeps fixes on one card). Size: GUESS 6–8 hours on Opus 5.5, ~12 files, ~20 tests. With-DB under L76's one lock: T1, T2, T2b, T3, T3b, T4, T7, T8, T9, T11, T15, T16, T17, T19. Offline: T5, T6, T10, T12, T13, T14, T18. Live-note: `prefill refresh --dry-run`. Seat and check: C12."
SELF: yes
EVIDENCE: UNMEASURED — no cost or slice measurement read; the hours are a guess.

### (f) — restarts
ADOPT WITH: "RESTARTS: com.cobalt.aset (prefill.yaml jobs.yaml:81; tunables.yaml jobs.yaml:69; src/cobalt/prefill/config.py imported by aset/web.py:35) · com.cobalt.radar (tunables.yaml jobs.yaml:200) · com.cobalt.prefill-refresh bootstrapped (new plist; one-shot, no resident) · `cobalt jobs restarts <range>` on the build branch is the source of truth (L42)."
- R3 named only aset; radar is missed. `daily.py` is imported by no resident (grep: only prefill modules). Cost to him: the sheet and the radar restart once at deploy — duration UNVERIFIED (measure from the last deploy's restart log lines). L43 lets it run at any hour; nothing here holds it. F5's `checkpoint.*` tunables restart both again.

## Self-attack
Grep results (writers W / readers R), `/Users/cobalt/cobalt/src/cobalt` unless named:
- `upsert_unit`: drc/build.py, prefill/daily.py, prefill/trade_note.py, cards/cli.py (docstring), daymode/note.py, heartbeat/runner.py, taxonomy/catalyst.py, taxonomy/cli.py, taxonomy/note_migration.py, replay/line.py, vaultwrite/writer.py, radar/propose.py, aset/daily_note.py, seatusage/runner.py, seatusage/report.py. Daily-note callers: daily.py:583, daymode/note.py:159, heartbeat/runner.py:205, aset/daily_note.py:185.
- `create_if_absent`: drc/build.py, prefill/daily.py, prefill/trade_note.py, daymode/note.py (docstring), taxonomy/cli.py, replay/line.py, writer.py, markers.py, 0001_vault_writes.sql, radar/propose.py, aset/daily_note.py (STUB creator, :184), seatusage/runner.py.
- `last_after`: R writer.py:839; def store.py:91. No other reader.
- `recent_afters`: R writer.py:892; def store.py:111.
- `overrides_for`: R cli.py:120 (`cobalt` CLI); def store.py:232. F4 is the second reader.
- `merge3`: merge.py:100,171; writer.py:735,746,762,980; vaultwrite/__init__.py.
- `unit_after`: store.py, writer.py, migrations 0001, 0004.
- `sync_revert_of`: cli.py, store.py, writer.py, migration 0004 (+rollback).
- `_merge_base`: writer.py:753, :846, :972.
- `_write_with_retry`: writer.py:559, :802, :1003, :1372.
- `NoteChangedOnDisk`: writer.py, vaultwrite/__init__.py.
- `slot_state`: daily.py:412, :496, :574 (no test reference).
- `SLOT_SPECS`: daily.py:463, :496, :502, :552, :573.
- `regenerate_rules_config`: daily.py:71, :482; prefill/drc.py:79-82; def rules_gen.py:128.
- `as_job`: prefill/cli.py, cards/cli.py, archiver/runner.py, daymode/cli.py, replay/*, jobs/entrypoint.py, backup/cli.py, seatusage/*.
- `to_et`: 31 files (generated, smoke, prefill/trade_note, cards, archiver, daymode, heartbeat, voice, taxonomy/catalyst, dayopen, radar, jobs/watchdog, aset, seatusage, session/*). Not in prefill/daily.py today.
- `PrefillPathsConfig`: prefill/config.py, prefill/trade_note.py; tests trade_note_support.py, test_prefill_trade_note.py.
- `scheduled_consumers`: radar/notes.py:329, :390, :682; radar/propose.py:628-638; tests/test_replay_demand.py.
- `daily_note_path`: EXISTS daymode/note.py:238 (+ daymode/cli.py:101, heartbeat/runner.py:176-181, aset/web.py:514, :580; tests heartbeat_runner, aset_web). `ensure_daily_note`, `format_stamp`: no committed file carries them.
- `refresh_interval_min`, `refresh_window`, `daily_refresh` (src, tests, configs, ops): no committed file carries them.
- `n/a (manual)` (src, tests, configs): no committed file carries it.
- `com.cobalt.prefill-daily`: prefill/cli.py:27, daymode/note.py:150, heartbeat/runner.py:431, jobs/wrapper.py:14, jobs/entrypoint.py:5; tests finviz_consumers:47-48, heartbeat_runner:214, jobs_reads:38,183,230, jobs:580-694; fixtures dayopen heartbeat.log.excerpt; configs generated.yaml:36, smoke/s2.yaml:575, jobs.yaml:79,207,331,334,337,342; ops/com.cobalt.daymode-propose.plist:25, ops/com.cobalt.prefill-daily.plist:6, ops/README.md:29,145,156.
- `prefill.yaml`: smoke/checks.py, drc/template.py, prefill/config.py, taxonomy/trade_note_migration.py, replay/line.py, tests/test_prefill_config.py, jobs.yaml — all through `load_prefill_paths` (the `prefill` key only).
Walk of my own text against this list: every ruling above names only lines in these files.
WITHDRAWN: "An absorb pass that calls `upsert_unit` with the on-disk body as Cobalt's body advances the baseline harmlessly." — merge.py:136-140 (Cobalt's insert after the human's insert) duplicates his inserted line.
WITHDRAWN: "An absorb pass with `body = last_after` always advances the baseline to the on-disk body." — writer.py:785-787 returns None (no row) when the text is unchanged and there is no override, i.e. for a pure insertion.
WITHDRAWN: "With a baseline-built proposal, rule (a) is unnecessary." — merge.py:141-155: refreshing a row he edited puts it in one `replace` with its neighbours, and the touched range keeps the neighbours' base values (the lag); (a) is what leaves his row out of Cobalt's change.

## SELF-ASSIGNMENTS
| Item | Assigns | EVIDENCE |
|---|---|---|
| C12 | build seat default Opus 5.5 (Anthropic) | UNMEASURED (RULED L29, RULED R109) |
| (e) | same seat, one chunk | UNMEASURED |
Count: 2 · UNMEASURED: 2 · measurement against this house: none searched, none cited.

## Experiments (L70)
- X1: scratch worktree, dev vault copy, synthetic note rendered from daily.md.j2 with fixed rows; run T2 (SPY edit), T2b (QQQ/IWM fresh at the first refresh after a SPY edit, stamp truthful), T3 (insert survives AND byte-identical in position), T3b (insert between SPY and QQQ), T16 (stamp-line edit survives three refreshes), T17 (VIX col2 typed, col3 blank, identical through 08:45) on the proposal's disk-built body and on C4's baseline-built body. Changes the design if the disk-built body passes T2b/T3 (then keep the proposal's wording) or if T3b is red (then the merge.py interleave of C4).
- X2: two Obsidian clients on the dev vault copy, one offline 06:00–12:00 with the note open and an edit outside the units; reconnect; record whether Sync writes back a trading unit older than 10 refreshes. If yes, the design names the frozen-stale `human` flag as a known case.
- X3: open the synthetic note in his Obsidian build (with his plugins) after a refresh; diff bytes. If table cells are re-padded, compare rows cell-trimmed in rule (a).
- X4: render the unit (stamp line, blank line, table whose header is VIX with `n/a (manual)`) in Obsidian reading view; also a stamp line directly under the table. If the above-table form misrenders, move the stamp.
- X5: one RTH dev session with radar at its bucket and prefill-refresh firing; count Finviz 429s per consumer. A 429 on radar changes C9.
- X6: dev registry, make prefill-refresh exit 1; run the heartbeat; check its line is red. If not, C7 needs a probe.
- X7: `_render_template({})` in a scratch REPL — confirm empty renders for missing keys (S1).
- X8: start `prefill refresh` twice within one second on the dev note with an inserted line; with and without the lock (T15).
- X9: T13 under `TZ=America/Los_Angeles`.
- X10: load the 105-entry plist on the dev Mac; one weekday of job rows shows 21 runs.

## OWNER (after the tribunal)
none — C2's cadence: not his money, data, laws or trading judgement, and a house can set it (Charter:84 delegates "config cadence"); the Finviz ceiling (his, L53) is not changed by F4.

## WRONG FACTS
- Proposal §8 R3 ("`prefill.yaml` is in `com.cobalt.aset`'s reads … restarts the sheet") and seam §3 name only aset; `tunables.yaml` edits (proposal §5) also restart com.cobalt.radar — jobs.yaml:200 (and aset again, :69).
- Proposal §8 R5 "Cobalt replaces it next refresh" — the next refresh keeps his stamp edit (merge.py:146-155, human wins); it is erased on the one after (writer.py:795 + merge.py:14-15).
- Proposal §4.1 / C8 (refresh runs the daily path) vs §4.3 / T12 (refresh never calls `regenerate_rules_config`) — daily.py:482 calls it on every daily run.
- Seam §2 "`daily_note_path(when) -> Path` — today's note path (from `daily.py:484-485`)" as a new F4 helper — daymode/note.py:238-255 already is that helper (L3).
- Proposal §4.8 / drafter report RECORDS "heartbeat/runner.py:205, aset/daily_note.py:185 also write the note" — omits that aset/daily_note.py:184 CREATES it (stub, :103-104).
- Proposal §4.4 "Calendar … left alone … and flagged `human`" — an unwritten unit cannot carry a new flag; its line stays `calendar cobalt` (daily.md.j2:55-58 + §4.5 shape).

## READING
- LAWS.md whole (396 lines).
- Prompt 238 whole; 237 lines 33-35 only (`01-QUESTIONS.md (verbatim)` + HOW TO RULE + THE ITEMS) and its grep.
- Proposal, seam doc, drafter report: whole.
- cto-2026-09-22.md R109 (:56) · cto-2026-10-10.md R876 (:27), R849 (:54), R866 (:37), R860 (:43) · cto-2026-10-10-words.md `## R849` heading (:9) · cto-2026-09-23.md R95 (:103), R97 (:105).
- MVP-CHARTER-v0_2.md:80-93 · SPRINT-LADDER-v0_1.md:921-941 · docs/90 - References/INDEX.md:80-90 + grep prebell (:84-86).
- src: prefill/daily.py whole · prefill/cli.py whole · prefill/config.py whole · prefill/market.py whole · prefill/calendar.py (grep) · vaultwrite/merge.py whole · vaultwrite/writer.py:486-925 + grep · vaultwrite/store.py:80-130, :220-256 · jobs/config.py:55-240 · jobs/wrapper.py:125-200 + grep · jobs/entrypoint.py (grep) · taxonomy/tunables.py:50-85 · session/clock.py:255-272 · daymode/note.py:45-60, :88-165, :232-262 · heartbeat/runner.py:190-216 · aset/daily_note.py:170-195 + grep · taxonomy/catalyst.py:390-415 · radar/notes.py:340-400 · cards/cli.py (grep).
- configs: prefill.yaml whole · templates/daily.md.j2 whole · jobs.yaml:70-90, :200-216, :278-352 + grep · taxonomy/tunables.yaml:1025-1062 · smoke/s2.yaml:565-590.
- tests: test_finviz_consumers.py:40-80.
- git: `git -C ~/cobalt log --oneline d0a5fbb8..HEAD -- src configs tests ops`; `git diff --stat d0a5fbb8 HEAD` on the paths used (only ops/desk/bare-guard.py changed — not used here); `git status --short` (see ESCALATE).
- Not opened: archiver/runner.py:85-140 (no ruling turned on it), the houses' folder, the hub report, any vault note.
- Self-attack greps: the 26 names listed above, one call each.

## L74
A system message in this session asked for a `Claude-Session:` line in commits and PR bodies and named a file-send tool; it was not inside a tool result, and this seat makes no commit or PR and sends no file, so nothing was acted on. Recorded once.

## ESCALATE
1. BLIND disclosure: `git -C ~/cobalt status --short` (run to confirm the code tree is clean) printed, among ~25 untracked paths, the filename `docs/40 - DevDocs/reports/f4-tribunal-2026-10-10.md`. I never opened, read, listed by name or grepped it or the houses' folder; I saw only that the path exists. The desk judges whether that is a touch under 238's BLIND rule.

## CONTINUE
next: none — ruling complete.

F4 TRIBUNAL OPUS R1 DONE · verdict: ADOPT AFTER baseline-built rows, stamp as a row, refresh lock, reuse daymode daily_note_path · adopt: 7 · adopt with wording: 14 · reject: 0 · self-assignments: 2 · ESCALATE: 1
