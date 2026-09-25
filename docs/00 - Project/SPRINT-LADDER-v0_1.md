# COBALT SPRINT LADDER — v0.1 (order RULED 09-04: radar before exits)

**Derived from:** MVP-CHARTER v0.2 (ratified 09-04) §3 F1–F23, §5, §7, §8,
§12, §13; PROJECT-LEDGER through the incident-thread close (rulings 6–9
folded, env-law/migration report DONE). Not derived from the 08-22 ladder.
**Laws applied:** each sprint only adds · sprint acceptance = full smoke of
all delivered functionality on dev vault + cobalt_dev, then one live morning
· L28 writers first · L29 model rule · F9 one-week cap · 19a before 19b ·
§8.7 building inside the window accepted until MVP.
**Sequencing rule (ruled 09-04):** radar (selection + awareness) precedes
exits/DRC automation. Reasoning on record: the radar has no manual
substitute (two names by eye vs 50 in the pool); the exit-coaching loop
already runs by hand in the DRC chat; the expectancy corpus must sample the
playbook's population (radar cards), not what Dejan spotted by eye; sim /
shadow-card training (R2 rung) needs the radar. Hand-logged legs cover the
gap until F11 lands.
**Timebox:** 9 build weeks 09-08 → 10-28, acceptance run 10-29 → 11-04
(**dates pulled forward 2026-09-09**: S1 closed 09-08, ten days early; every later
sprint moved up by the same shape; original 09-04 dates in the git history).
Charter says ~2 months; this is 2 months + 1 week — flagged, not hidden.

**Starting state (from the ledger, proven):** cobalt_brain live, cobalt_dev
dev/test, COBALT_ENV law in code, vaultwrite one path (L28) with
vault_writes/overrides, ASET sheet iter 4 (fixed-dollar keys, mode toggle,
fill recompute, FILLED status), prefill-daily 05:15 + prefill-drc 15:40 +
archiver 20:30 plists loaded on the resolver, bars migrated (4.56M rows),
com.cobalt.obsidian supervised, boot contract met, tunables.yaml 30 rows +
validate, taxonomy v0.7 + trade_defs batches 1–2 in DB, heartbeat probes
built (host not yet), 92 real cards in cobalt_brain.

---

## Ladder at a glance

| Sprint | Weeks | Adds (Charter F-ids) | §7 metric served |
|---|---|---|---|
| S1 Foundation + firewall | 09-08 → 09-18 (2) | F1 · F7 (manual cards) · F6 · F18 · F17 · F19 · F16 sweep · bars.ts ADR | adherence, prep (nothing silent again) |
| S2 Radar 19a | 09-10 → 09-23 (2) | F2 · F8 · F10 · F3 · Radar panel (§5) · F12 · F13 | selection quality, awareness; expectancy corpus starts on the right population |
| S3 Exits + DRC on radar cards | 09-24 → 10-07 (2) | F11 · F22 · F14 · F15 | exit efficiency, adherence measurement, expectancy |
| S4 19b strike alert — CAPPED | 10-08 → 10-14 (1) | F9 | bandwidth (+ adherence under fire) |
| S5 Prep + platform + playbook | 10-15 → 10-28 (2) | F4 · F5 · F20 · F21 · F23 · F16 close | prep, bandwidth |
| Acceptance | 10-29 → 11-04 | §12: every MUST on live vault + DB, 5 days green, ≥3 live mornings | — |

**Expectation set with the ruling:** the radar raises candidates, not the
trade count — rule 10 and the trade-count band still cap what is taken.
Expect the miss line and cost-of-discipline rows (`excluded_by: rule_10 |
trade_count_band | window`, with counterfactual R from archived bars) to
grow first; that tally is the Friday-review input for loosening rule 10.
Reasoning over that corpus (Guardian advisory, replay + shadow configs) is
post-MVP lane; the MVP builds the corpus only.

---

## S1 — Foundation + firewall (09-08 → 09-18) — UNCHANGED

**Precondition folds:** env-law report DONE (rulings 6–9) — S1 starts from
cobalt_brain live. Open items inherited into S1: TESTARCH row delete;
`bars.ts` ET-under-+00 (Data-Model ADR rules it before any join — the 19a/19b
detectors join bars, so it lands here). Tailscale on the trading PC = his;
S1-P1 line 0 reports peer status, nothing more.

| Feature | Charter acceptance (test) | What S1 delivers |
|---|---|---|
| **F1 Session clock** | Card at 18:30 and 21:30 show the right session; the 21:30 one is blocked. | `cobalt.session`: premarket 04:00–09:30 / rth / aftermarket 16:00–20:00 / market_reset 20:00–21:00 hard-block / overnight; NYSE calendar (holidays, early closes) as config; boundaries = tunables rows; `session` column on cards, alerts, vault_writes; market_reset block enforced in the write path. |
| **F7 Card state machine** (manual cards) — **DELIVERED S1-P2** | DRC counts match Postgres rows; no card exists without a state. | `card_state` enum + `card_transitions` table (from, to, at, evidence JSON, actor cobalt/you); existing ASET rows mapped (card = WATCH, FILLED status = FILLED); sheet gains ARM / DISARM / TRIGGERED / FILLED / PASS / EXPIRE controls; trigger-while-unarmed = MISSED row (manual entry at S1, detector at S2/S4). |
| **F6 Two-stage day mode + match check** — **DELIVERED S1-P2** | He loads the full sheet on a half day → card refused with the reason. | Pre-09:00 = lowest *enabled* sheet by system rule (half today); 09:00 proposal row (mode, reason from prior DRC stub + goal band + calendar; "no prior DRC" = loud) with his approve/overrule + reason persisted; `.htk` loaded-sheet check refuses cards on mismatch. Trade-count goal band = tunables rows, value pending Rules Engine session. |
| **F18 Heartbeat** — **DELIVERED S1-P3** | Unload a plist → red within one interval, on the out-of-band channel. | Heartbeat host job: services alive · archiver freshness (last run + row delta) · every ops plist loaded + last exit code · Obsidian running; red/green block in daily note (L28 unit) + Mattermost DM; red also by email via Layer-B Google OAuth (alert path ≠ monitored path). |
| **F17 Task integrity, minimal** — **DELIVERED S1-P3** | A hung poller is surfaced as a zombie within one heartbeat interval. | `jobs` table: every launchd job = persisted row with state (pending/running/done/failed), timeout, heartbeat stamp; watchdog marks zombies; kill phrase (config) stops all; failed = loud via F18. |
| **F19 Exfiltration guard** — **DELIVERED S1-P3** | A token in a DM payload is redacted before send. | Outbound secret-regex redactor as one function on every channel (Mattermost, email, log lines); patterns = config; tested against the rotated-secret shapes from 08-23. |
| **F16 sweep** — **DELIVERED S1-P1/P2/P3** | `validate` passes; no inline literal in a predicate. | Every threshold introduced this sprint = tunables row with a consumer; loader fails loud on unknown keys (already). Sweep repeats every sprint. |
| **bars.ts ADR-0007** (decided-with-veto) | — | Reinterpret stored ET-as-UTC values to true UTC (`America/New_York`), dump = rollback, row-count + md5 proof, archiver writes UTC from now; run outside 20:00–21:30. |

**S1 smoke:** prefill-daily, prefill-drc, archiver, obsidian, mainframe,
heartbeat all as job rows, green; one manual card walked WATCH → ARMED →
TRIGGERED → FILLED → CLOSED with every transition in `card_transitions`;
a card attempted at 20:30 refused; a full-sheet card on a half day refused;
plist unload → red email within one interval. Then one live morning on the
ASET sheet with the new controls.

**Code prompts owed (all Opus 5 — every one touches a DB or vault write path):**
- S1-P1 · fresh · Tailscale status line 0 · TESTARCH delete · ADR-0007 bars.ts · F1 session clock + column stamps + market_reset block · F16 sweep. **(issued 09-04 · DELIVERED 09-04, branch `sprint-1/foundation`, unpushed)**
- S1-P2 · fresh · F7 card_state + transitions + sheet controls · F6 two-stage mode + proposal row + `.htk` match refusal. **(issued 09-04 · DELIVERED 09-04, branch `sprint-1/foundation`, unpushed)**
- S1-P3 · fresh · F19 redactor · F17 jobs table + watchdog + kill phrase · F18 heartbeat host (note unit + DM + email) · S1 smoke script + report. **(issued 09-04 · DELIVERED 09-04, branch `sprint-1/foundation`, unpushed. Email = NOT BUILT: no send path exists — see the outcome below.)**

### S1-P1 outcome (2026-09-04) — what landed, what it changed

- **Tailscale (read-only, line 0):** NO Windows peer on the tailnet.
  Three devices: `cobalt` 100.70.206.126 (this Mac), `dejans-s25`
  100.66.219.53 (android, offline 1d), `fedora` 100.104.48.21 (linux,
  offline 10h). The trading PC has not joined — still his, and it gates
  the S2/S4 strike-alert path (Charter: pinned tab over Tailscale).
- **TESTARCH deleted** from `cobalt_brain.bars` under the RULING 8
  discipline: 4,755,478 → 4,755,477, `ROW_COUNT` 1, guarded transaction.
  Closes ADR-0006's first follow-up. No other test residue found.
- **ADR-0007 ruled and executed.** `bars.ts` reinterpreted ET-under-UTC
  → true UTC across 4,755,477 rows in one 42 s transaction, DST-aware,
  content md5 identical, `ts` md5 changed, PK re-added clean. Dump =
  rollback (316 MB, sha256 in the ADR). The collector now emits
  tz-aware UTC and `Bar.ts` is `AwareDatetime`; proven on the real
  production path (21,718 rows written, table grew 261 — everything
  else upserted onto reinterpreted keys). **The 19a/19b bars join is
  unblocked.**
- **F1 delivered** as `src/cobalt/session/` — resolver, NYSE calendar as
  config, `market_reset` hard block with a `session_blocks` counter,
  `session` column on `aset_sizings` + `vault_writes` (backfilled on
  both databases, now NOT NULL), `cobalt session now/backfill/blocks`.
  60 F1 tests, 362 green overall.
- **F16 sweep clean.** Eight `session.*` boundary rows plus
  `session.blocks.heartbeat_window` (42 tunables total); `cobalt
  validate` is now a first-class command and covers the calendar and the
  boundaries as well as the taxonomy.

**Carried out of S1-P1 (not blocking):**
- `configs/cobalt/calendar/nyse-2026.yaml` holiday/early-close dates are
  **derived, not fetched** — Dejan to confirm. Config-only correction.
- No `nyse-2025.yaml`, so `session()` over the 2025 third of the bars
  corpus raises `CalendarError` by design. Add the file when a 2025 join
  is actually needed.
- `bars` has no `session` column (derivable from `ts`); revisit if S2
  makes the derived cost real.

### S1-P2 outcome (2026-09-04) — what landed, what it changed

- **Dump hygiene (my error in P1, corrected):** the 316 MB bars dump was
  **never committed** — `git ls-files` and `git log --all --stat --
  '*bars-dump*'` both empty, so no branch rewrite was needed. It was
  held out of git by ONE location-based `.gitignore` rule covering the
  incident folder; the same file one directory over would have been
  tracked. Moved to `~/cobalt-backups/` (mode 700), sha256 re-verified
  identical, `.gitignore` gained content-based `*.sql` / `bars-dump-*`
  rules **plus** a `!src/cobalt/*/migrations/*.sql` carve-out — without
  it `*.sql` would have silently swallowed every future migration.
  Repo 4.7G → 4.4G; `.git` unchanged at 116M (the proof it was never in
  history). ADR-0007's Rollback section updated.

- **F1 calendar gap closed:** `configs/cobalt/calendar/nyse-2025.yaml`
  ships (11 holidays incl. the 01-09 National Day of Mourning, 3 early
  closes incl. 07-03 which is a half day in 2025 but not 2026). Proven:
  2025-11-28 12:00 ET → `rth`, 13:30 ET → `aftermarket`. The 2026 file
  was not touched. This closes S1-P1's carried `CalendarError` item.

- **F7 delivered** as `src/cobalt/cards/` — the edge table as ONE table
  in code (exported to DevDocs by `edge_table_markdown()`, so the wiki
  cannot drift), `card_transitions` as the ledger, `card_stop_edits` for
  decision 11, and `cobalt cards state/history/move/backfill/expire/edges`.
  `aset_sizings` gained `state` (NOT NULL) + `state_at`; `status` stays
  readable and is no longer written. A card and its genesis transition
  are now written in ONE transaction, with the state set *in the INSERT*.
  A fill is a `TRIGGERED → FILLED` transition, so filling an un-triggered
  card is refused by name. `counts_for_date` moved off `status` — left
  there it would have reported 0 trades taken from this sprint forward.

- **F6 delivered** as `src/cobalt/daymode/`, on Dejan's 09-04 ruling that
  **`reduced` is a ROLE, not a sheet**. `sheet_modes` in
  `configs/cobalt/aset.yaml` became an ordered config list
  (`order: [half, full]` + `sheets:`), the mode ladder is DERIVED
  (`["reduced"] + order` → `reduced < half < full`), and
  `daymode.reduced_sheet` is the pointer (today `half`). Nothing in
  `src/` names a sheet as a literal; a mocked `quarter` ladder in the
  tests repoints the floor and every refusal message with no code change.
  Charter §8 collision #2 is unchanged — `reduced_sheet: half` is what it
  encodes.

- **The `.htk` match check is an ATTESTATION, and here is why.** Slice
  2's "match check" was found to be one static string in the daily-note
  template — `SHEET_MODE_LINE`, two pairs of markdown checkboxes that
  read nothing, compare nothing and refuse nothing. There is no other
  `.htk` reference in `src/`. Nor could there be: the trading PC is not
  on the tailnet (S1-P1 line 0) and CLAUDE.md forbids touching DAS at
  all. So the honest fallback shipped: he states which file he loaded,
  it persists on the `day_modes` row, and card creation is refused while
  it disagrees — *including when nothing has been attested*, which is
  exactly the state in which a full-size key gets pressed on a
  reduced-size day.

- **F16 sweep clean.** Three new tunables rows (`daymode.stage2_open`
  09:00; `daymode.trade_count_band.min`/`.max` as PLACEHOLDER pending
  the Rules Engine session), 45 total. `cobalt validate` now also covers
  the sheet order, the day-mode ladder and pointer, the band rows, and
  card-state reachability.

- **Two launchd jobs installed and loaded:** `com.cobalt.cards-expire`
  (16:05 ET) and `com.cobalt.daymode-propose` (09:00 ET), both carrying
  `COBALT_ENV=production` and the absolute `uv` path. Registration in the
  F17 `jobs` table is S1-P3's; each plist carries a TODO with its label.

- **Backfill, cobalt_brain (92 cards, as the ladder's starting state
  says):** `EXPIRED 87 · FILLED 4 · WATCH 1`. 92 genesis transition rows,
  every one marked `evidence->>'backfill' = 'S1-P2'` and session-stamped,
  0 rows left NULL, `state SET NOT NULL` applied clean. cobalt_dev's
  `aset_sizings` is empty (RULING 7.1d's transactional tests leave
  nothing behind), so its backfill was a schema-only no-op.

- **Three defects found and fixed inside this prompt, two of them only
  because the work was proven on real data:**
  1. A `FILLED` card had no `CLOSE` button — `_card_controls` looked
     labels up per legal edge and had no entry for `CLOSED`, so the first
     card to actually fill would have raised `KeyError` while painting
     the sheet. Caught by review before it shipped.
  2. `cobalt cards backfill` opened with a full `ensure_schema()`, which
     applies `state SET NOT NULL` — failing on exactly the un-backfilled
     rows the command exists to fix. **Invisible on cobalt_dev** (empty
     table, constraint applies to zero rows, all tests pass); it surfaced
     on the first real run against cobalt_brain's 92.
  3. A stop edit moved `stop` and nothing else, leaving `shares` and
     `used_risk` describing the OLD stop — a card asking for a position
     it had not sized. The recompute is now factored out of
     `compute_sizing` (one path), and in-trade holds the share count and
     moves open risk instead, since a moved stop cannot un-buy shares.
  Plus one on the real vault: a DRC left on its template placeholder
  (`grade (A+, A, B, C, etc..)`) counted as a filled DRC and suppressed
  the step-down.

- **Tests:** 88 new (47 F7 + 41 F6), including all 53 illegal edges
  enumerated from the table itself. New-core suite **496 green**.
  (Old-tree `tests/test_cortex.py`, `test_scribe.py`, `test_scheduler.py`,
  `test_postgres_memory.py`, `test_finviz_extractor.py` fail as they did
  before this prompt — `cobalt_agent`, untouched by the strangler rule;
  verified no new-core frame appears in any of their tracebacks.)

- **NN#16 lesson, caught live: a config RESHAPE is a deploy.** Reshaping
  `configs/cobalt/aset.yaml` took the running `com.cobalt.aset` sheet to
  HTTP 500 the moment it happened — `_render` calls
  `load_sheet_modes_config()` on **every request**, so the long-running
  process was reading the NEW file shape through its OLD Pydantic model
  (`full`/`half` required, `order`/`sheets` forbidden). It failed LOUD
  and refused to serve rather than sizing off a half-parsed config, which
  is the behaviour we want — but the window between editing the file and
  restarting the service is a real outage, and nothing in the process
  warned that its config had changed underneath it. Restored by
  kickstarting the LaunchAgent (L28's restart-on-deploy rule, applied to
  a config edit rather than a code deploy). It happened on a Friday
  evening inside the `market_reset` window with the market shut. Worth a
  standing habit: **a config-shape change and its service restart are one
  action.**

**Behaviour changes Dejan will notice on the sheet, Monday morning:**
1. The FULL/HALF toggle is **gone** — the sheet mode follows the day mode.
2. **He must attest an `.htk` before the first card of the day.** Nothing
   attested = card refused. One click on the banner selector.
3. Today's rung is **reduced → half sheet, key B only.** An A key is
   refused with the reason on screen.
4. A fill now requires the card to be ARMED and marked TRIGGERED first —
   both are one click each in the open-cards list.

**Carried out of S1-P2 (not blocking):**
- `daymode.trade_count_band.{min,max}` are PLACEHOLDER, and the
  proposal's step-down rule set is provisional — both belong to the
  **Rules Engine session**. While the band is unruled it acts as an
  adverse signal that pins the proposal to the floor.
- `SizingInput.sheet_mode` is still the `SheetMode` enum (full/half),
  on the live sizing path and deliberately not reshaped. `cobalt
  validate` now refuses a declared sheet with no enum member, so the
  quarter sheet cannot land half-wired.
- `preferred_windows_ref` is free prose; the expiry resolver only
  trusts unambiguous strings and falls back to the session close
  otherwise. Making those refs machine-readable is a taxonomy change
  for the Rules Engine session.

**Rulings/inputs owed before S2:** health thresholds (mock #8) for the panel's
IN-TRADE health line — before S2-P3. Detail-column order (mock #11) — S2-P3.
Trade-count goal band value (his; band ships as placeholder in S1).
Taxonomy v0.8 consolidation (§13.1 wording + stop.buffer re-rule) — natural
bump point is S2-P2, the precondition evaluator.

---

### S1-P3 outcome (2026-09-04) — what landed, what it changed

**S1 SMOKE: GREEN.** `scripts/smoke_s1.sh` — 19 checks across F1, F6,
F7, F16, F17, F18 and F19, plus the 650-test new-core suite. Repeatable:
hard-pinned to `cobalt_dev` + the dev vault, every card it creates
deleted in a `finally`.

**The four P2 corrections, all proven:**

- **(a) The reduced rung is a SIZE rung, not a grade ban.**
  `reduced_enabled_grades: [B] -> [A, B]`. On today's rung A is
  accepted, A+ refused (the *account* ladder does not enable it), B
  accepted.
- **(b) The attested-sheet selector is DERIVED.** The hand-written
  `file -> mode` list is gone, `reduced_day.htk` with it — a name that
  matched no key table in `aset.yaml`, offered to him as an attestation
  for a sheet that did not exist as a config row. The list also mapped
  files to RUNGS, when a `.htk` is a key table and a key table is a
  SHEET. Now one name per declared sheet from `hotkey_file_template`,
  and the match check compares sheet to sheet. Adding `quarter` to
  `aset.yaml` puts `quarter.htk` in the selector with no code change and
  no edit to `daymode.yaml` — asserted by test.
- **(c) One-click fill on manual cards.** `aset_sizings.origin`
  (manual | radar, backfilled manual). `CardStore.fill()` is the single
  way to reach FILLED; on a manual card it walks the rest of the route
  itself, writing the missing ARMED/TRIGGERED rows with `actor=cobalt`,
  evidence `{"auto": "manual_fill"}`, at the fill's own timestamp, all
  in ONE transaction. **The edge table is unchanged** — the route comes
  from a breadth-first walk of `ALLOWED`, and a test asserts for every
  state that the shortcut can only walk edges the table already carries.
  A radar card gets no shortcut and is refused by name. Proven on
  cobalt_dev: manual WATCH + one click = 3 rows; the same click on a
  radar card = genesis row only.
- **(d) The daily note's sheet-mode line goes both ways.**
  `daily.py:76`'s dead checkbox string is deleted and replaced by a
  Cobalt-owned L28 unit carrying the decided mode and one checkbox per
  declared sheet. A box he ticks in Obsidian IS an attestation, read
  back at the next sheet request. A disagreement between the note and
  the record is a REFUSAL showing both — proven on the dev vault with
  diffs, in all four directions.
- **(e) The step-down rules moved into `daymode.stepdowns`.** The FACTS
  stay in code (they are queries against the calendar, the cards and the
  DRC note); the EFFECT and the words are the table's. A signal the code
  can compute but the table does not rule is refused at load — turning a
  rule off is `effect: none`, visibly. Defaults are byte-for-byte what
  S1-P2 shipped.

**F19 exfiltration guard.** One `redact()` on every outbound channel.
17 patterns + a LITERAL guard for the four 08-23 username/password
rotations that no shape can describe. Fails closed, idempotent, partial
(a redacted DSN stays readable). Proven live: a DM containing seven
fabricated secret shapes arrived with six redactions counted and every
value gone. **No secret value is anywhere in git** — the shapes were
derived from the vault programmatically and never printed.

**F17 task integrity.** Ten `cobalt_jobs` rows, one per plist, with
state / timeout / heartbeat. ZOMBIE needs both halves (past timeout AND
a stale heartbeat — the archiver runs 23 minutes on a normal night).
MISSED is a fact about an absent run, not a state. Kill phrase
`COBALT STOP` via `cobalt stop`, proven both directions; the DM half is
not wired because the only Mattermost *listener* lives in the old tree.

**F18 heartbeat.** `com.cobalt.heartbeat` installed and loaded, every 15
min, `COBALT_ENV=production`, RunAtLoad. Red/green block in the live
daily note as an L28 unit, updated in place, one diff per beat. DM on
red + one green summary a day. **Charter test passed on production for
real:** green → `launchctl bootout com.cobalt.cards-expire` → RED on the
DM within the same interval, naming the label and the reload command →
`launchctl bootstrap` → green, exit code intact.

**THE EMAIL CHANNEL WAS NOT BUILT, and that is the finding.** Charter §3
F18 specifies email via the Layer-B Google OAuth path. **No email send
path exists in this repo** — no `smtplib`, no `sendmail`, no Gmail/OAuth
client, no credentials file, no `send_email` anywhere in `src/`, `ops/`,
`dev_utils/` or `configs/`. `google-api-python-client` is a dependency
and `googleapiclient` appears in the old tree only as a Gemini/LLM
import; the vault holds API keys, not an OAuth token. Per the prompt I
did not build OAuth. Every red now says so out loud. **The consequence
is the exact hole "alert path ≠ monitored path" exists to close:** the
DM goes over Mattermost, which is one of the monitored services. → P4.

**Five defects found, three of them only by running the acceptance tests
against production rather than against a fixture:**

1. **`jobs` is MATTERMOST's table.** `cobalt_brain` is the same Postgres
   database Mattermost runs in — 129 tables, 116 of them Mattermost's,
   including a `jobs` with 164,320 rows. `CREATE TABLE IF NOT EXISTS
   jobs` did nothing, silently. The first production query failed loud
   (`column "label" does not exist`), which is the only reason this was
   a ten-second diagnosis rather than a week of green heartbeats
   reporting on Mattermost's work queue. The three tables introduced
   here are now `cobalt_jobs` / `cobalt_kill_switch` /
   `cobalt_redactions`. **The larger issue is unruled:** every future
   new-core table is one generic name away from this, and a
   `DROP`/`TRUNCATE` aimed at the wrong name has Mattermost in blast
   radius. Worth a ruling — a schema of its own, or a prefix convention
   made law.

   > **CORRECTION (2026-09-04, added by the split session; the paragraph
   > above is left as written per the frozen-record policy.)** "116 of
   > them Mattermost's" was arithmetic, not an inventory: 129 total minus
   > 13 assumed ours. A pristine Mattermost 11.4.0 reference install —
   > same image digest, empty database, its own migrations — creates
   > **103** tables. Cobalt's half is **28**, every one with a
   > `CREATE TABLE` in this repo. So 13 Cobalt tables were being counted
   > as Mattermost's, and a `DROP` guarded by "the 116" would have
   > destroyed them. The ruling that closed this went further than either
   > option offered above: **one database per product** — see ADR-0006's
   > 2026-09-04 section.
2. **The Charter's own F18 test failed the first time.** Only RESIDENTS
   were probed against launchd, so unloading a one-shot's plist left the
   heartbeat green — between runs an unloaded one-shot looks identical
   to a loaded one. Every job is now asked, and launchd's last exit code
   is reported (78 = EX_CONFIG, the 09-03 signature).
3. **A dev prefill run was rewriting the committed production
   `rules.yaml`.** One `COBALT_ENV=dev uv run prefill daily` rewrote its
   `source`, `source_sha256` and all twelve rule texts to the DEV
   vault's copy. RULING 7 env-scoped the database and the vault and
   stopped there; the generated artifact kept one hardcoded target.
   Nothing failed — only `git status` showed it. Now env-scoped, with no
   default.
4. **`com.cobalt.archiver.plist` was malformed XML** (a double hyphen
   inside an XML comment). launchd's parser is lenient and has been
   running it nightly all along; `plistlib` refuses it, so every tool
   that reads plists failed on that one file. Note that `plutil -lint`
   *passes* it — plistlib is the stricter reader.
5. **Two of my own, caught before they shipped:** F19 redacting per
   pattern over the previous pattern's output let a later row match an
   earlier row's placeholder (one secret, two hits, wrong attribution);
   and an interval job was UNMISSABLE, so a 15-minute heartbeat measured
   against a 30-minute grace reported green forever, including while
   stopped.

**The `market_reset` ruling (decided-with-veto) is implemented.**
Migration and repair tooling stays ungated inside the block — the
carve-outs already existed in `restore` and `backfill`, and what was
missing was the price. Every such run now logs one loud line and lands
in `session_blocks` with `kind = 'ungated_run'`, in the same counter F18
shows. The two kinds are displayed separately and never summed. Card
creation stays refused, asserted by its own test.

**A LIVE-VAULT INCIDENT DURING THIS SESSION, for the record.**
`docs/00 - Project/SPRINT-LADDER-v0_1.md` — this file — was overwritten
at 21:44 by an older copy while the session was running. I read the
374-line version at 21:33 and found a 200-line one at 21:50, with the
S1-P1 and S1-P2 outcome sections gone. Nothing in this prompt wrote it.
`docs/` is symlinked into the real vault at `0 - Projects/Cobalt`, so
Obsidian Sync carried a stale copy from another device over the top —
the same mechanism as the 09-03/04 daily-note incident, on a git-tracked
file this time, which is the only reason it was recoverable
(`git checkout` from HEAD). **The unresolved half: `docs/` is a live
Sync target, so any uncommitted doc edit in this tree is one stale
device away from being lost.** L28 protects notes Cobalt writes; it does
not protect the repo's own docs.

**Tests:** 613 new-core (up from 496 at S1-P2) — 64 F19, 45 F17, 15
day-mode note, plus the one-click-fill and step-down-table cases.
`cobalt validate` green, including the two new cross-checks.

**Carried out of S1-P3 (not blocking):**
- The **out-of-band alert channel** (Charter §3 F18) → P4. Building it
  means client registration, consent, refresh-token storage in the
  vault, and a new secret shape for F19 — not something to improvise
  inside a heartbeat.
- The **shared-database ruling**: Cobalt's trading record and
  Mattermost's tables in one database. Prefix convention, or a
  schema of its own. **RULED AND DONE 2026-09-04** — neither: one
  database per product. Mattermost moved to `mattermost`;
  `cobalt_brain` is Cobalt's 28 tables alone (ADR-0006). The count
  in this section was wrong — 103 Mattermost tables, not 116.
- **`docs/` as a Sync target** — see the incident above.
- **DevDocs**: `src/cobalt/vaultwrite/` (5 files) and
  `taxonomy/__init__.py` still have no page. Pre-existing gap, not
  introduced here.
- The **archiver's first observed run** is tonight's 20:30; until then
  its freshness probe reports "no run OBSERVED yet" rather than red.

---

## S2 — Radar 19a (09-10 → 09-23; was 09-21 → 10-02, pulled forward 09-09)

| Feature | Charter acceptance (test) | What S2 delivers |
|---|---|---|
| **F2 Radar pool 24×5** | A name entering on RVOL at 14:10 appears within one scan cycle; pool never exceeds config cap. | Pool job: 4 TV static lists + 4 Finviz dynamic screens → ≤50 rotating names, churn every `radar.scan_interval` (60 s start), premarket included, membership history persisted (`excluded_by` on drop). |
| **F8 Card at precondition (19a)** | A Rubberband precondition on a pool name produces a card within one scan interval; every field badge-owned. | Precondition evaluator over polled Finviz bars at `working_timeframe` (2m) for the six radar trades (Rubberband first, then Back$ide, Fashionably Late, Hitchhiker, Second Chance, Big Dog); WATCH card lands with setup → trade, trigger, structural stop (buffer 0.02), proposed key, dots + WHY; expiry per `preferred_windows_ref`; account mode (live / sim) tagged on every card. |
| **F10 Dots / ladder / accept-up-down** (pulled forward: F8 lands scored cards) | An A+ tap on a half day records A+ and sizes at A $70 with the notice. | Computable dots scored 1–10 with WHY from the `trade_def`'s scored variables (Finviz screener fields: RVOL, spread, float, catalyst grade, ATR…); judgment dots (tape, conviction) hollow, 1–10 tap strip; keys A+/A/B/C/pass, fixed dollars per sheet, disabled keys greyed with would-be dollars; tap = grade recorded, sized at nearest enabled key, loud. |
| **F3 Focus list with conviction WHY** | DRC shows his pick and Cobalt's rank for every card. | Rank = conviction × proximity (opaque score); ~4 focus names each with one WHY line; promote/release; pick-vs-rank logged (row now; DRC rendering lands with F14 in S3). |
| **Radar panel (§5 host)** | Acceptance = 2–3 live mornings beside DAS on a static render before the card slice is called done. | ASET Flask sheet grown into the ladder: strips, #1 + #2 open, detail column drops below at <1150 px, ARMED/IN-TRADE pinned above WATCH, owner badges, health line (thresholds per mock #8 ruling). Front-end only = Sonnet-eligible. Fixes the 09-02 ASET-tab focus-handoff fumble (hotkey focus never on the panel). |
| **F12 Missed records via nightly replay** | Nightly report lists misses with the gate/variable that excluded them. | Archiver post-run: replay every `trade_def` trigger over the day's bars; trigger on an unarmed/absent card = MISSED row with `excluded_by` (incl. `rule_10`, `trade_count_band`, `window`) and counterfactual R from bars. |
| **F13 Auto-archive + benchmark + miss line** | A Tesla-class mover absent from the pool appears in the miss line with `excluded_by`. | Top-N movers archived nightly regardless of watchlist; benchmark query (movers ≥ config move) diffed against the in-play set; one miss line — into the existing DRC prefill now, the SMB-format DRC note at S3. |

**S2 smoke:** dev-vault day replay on a recorded session: pool churns, a
Rubberband card lands within one interval, ranked focus list, MISSED rows
with `excluded_by` and counterfactual R present; then live mornings 1–3
beside DAS on the panel (cards graded by tap, fill via the existing
fill-recompute; legs hand-logged in the DRC chat until S3).

**Code prompts owed:**
- S2-P1 · Opus 5 · fresh · **line 0: ADR-0008 in force** — `system` / `"user"` schemas, side per store; pool + membership tables land in `system`; the account-mode tag is a `"user".aset_sizings` column; every new table declared in the placement map or the suite fails; first cross-side joins J1-J4 per ADR-0008 · F2 pool job + membership history · Finviz bar poller at working TF (reuses the spike's client path) · account-mode tag.
- S2-P2 · Opus 5 · fresh · F8 precondition evaluator, Rubberband first, then the other five · F10 dot scoring + ladder sizing + tap recording · taxonomy v0.8 bump.
- S2-P3 · Sonnet · fresh · Radar panel front-end (no write path) — ladder, strips, badges, tap strip, phone frame · F3 rank + WHY display.
- S2-P4 · Opus 5 · fresh · F3 pick-vs-rank rows · F12 nightly replay + counterfactual R · F13 top-N archive + benchmark + miss line · S2 smoke.
- Parallel, non-write: Agent SDK spike (Sonnet) — two-session test (subscription CoS + local worker via LiteLLM proxy), HITL hooks question — so S5's F20 does not start cold.

### Status 2026-09-24
Fourth status block (SESSION-CLOSE step 4a, ruled 09-19 R14); replaces `### Status 2026-09-22` (one block only). Written by close hub `close-0923` (one close for 09-22 + 09-23) from `reports/cto-2026-09-22.md` (§4 R1–R130) + `reports/cto-2026-09-23.md` (§4 R1–R112) + `reports/s2-smoke-look-2026-09-23.md`, re-verified against the tree (L35): `git tag --list "deploy-2026-09-2*"` = five (`deploy-2026-09-21`, `-21b`, `-21h`, `deploy-2026-09-22` = `d2d82e70` 12:26 ET stale marker + ops 0921, `deploy-2026-09-23` = `4e4577c3` 16:56 ET the S2 smoke fix, ONE branch); `origin/main` = `49018abd` (pushed 09-22 R29 and 09-23 R92), main 18 docs commits ahead. Unmerged branches at close: `setups/seven-0921` `c60a7f00` (BUILT + CHECKED for 09-24), `cards/stale-score-0922` `57925f3b` (wip, stopped), `drc/d1-trading-log` `7ed5e5ee`, `voice/v1-0923` `28b6b0c6`, `jev/trial-0923` `f4e8de85`, `radar/handicap-h1-0922` `be4c79b5` (cut, no build), `bars/chunk-1a-0920` and `bars/chunk-2-0920` (both CHECKED 09-21, still unmerged). What changed since the last block: two production deploys (09-22 stale marker + ops 0921; 09-23 the S2 smoke fix); the `radar.benchmark` row loaded 09-22 07:04 ET; the LAWS sitting held and applied (75 laws, L75 new, L12 retired); the replay failed 09-21 and 09-22, then SUCCEEDED 09-23 21:10 ET; tonight's smoke is AMBER 32/34 (K9.4, K17), so S2 does not close on its stop date; S3's designs (S3 exits, DRC, voice) advanced; the seven-setups build went through four fix/check rounds and a live-note round and is READY for the 09-24 deploy. Status only — scope, dates and order change by his ruling alone. Legend: DONE-LIVE · DONE-DARK · BUILT-NOT-MERGED · NOT STARTED · BUILDING.

| Feature / prompt | Status | Evidence |
|---|---|---|
| F2 Radar pool 24×5 (S2-P1) | DONE-LIVE | S2-P1 live 09-13 (`7bca336`); L13 acceptance run 09-14. Smoke 09-23 21:40 ET: K1 `com.cobalt.radar` running (pid 79755), K2 `radar_pool` primary OK. `deploy-2026-09-22` restarted `com.cobalt.aset` only (radar not restarted); `deploy-2026-09-23` restarted both (residents down 17 s). Day-open GREEN 09-22 and 09-23 (radar scanning premarket, 50 members). |
| F8 Card at precondition (S2-P2) | DONE-LIVE — **live morning 1 banked** | Switched ON 2026-09-19 12:30:01 ET. **Mon 09-21 04:00 ET premarket = live morning 1** (R13 "A": a morning counts when radar and panel ran correctly beside DAS, even with an empty ladder — BANKED). Live today = ONE evaluable definition (Rubberband path A; 12 of 13 defs `not_evaluable` on missing atoms, ADR-0009). Smoke K6 (fills = FILLED transitions with a picks row): fills 9 on the 09-22 look, 13 on the 09-23 look, `missing ok` — cards did form and were filled. The seven-setups ladder change is NOT live yet — see its row. |
| F10 Dots / ladder / accept-up-down (S2-P2) | DONE-LIVE | `htf_level_proximity` curve live since 09-20 (four curves total). The STALE marker (09-21 R36: row + card badge on stale-bars tickers) is **DONE-LIVE since `deploy-2026-09-22` 12:29 ET** (`s2/stale-marker-0921` round 2 tip `27eaa0c`; the live badge proven by inference, not a browser — deploy ESCALATE 5). Stale-score (`—` instead of a score on stale bars, 09-22 R37–R45) and the float handicap are separate rows below. |
| F3 Focus list, conviction WHY | DONE-LIVE | Unchanged. |
| Radar panel (§5 host) — S2-P3 | S2-P3 DONE-LIVE; **live day banked (Mon 09-21, R13)** | Ladder always the top of `/radar`, pool below (`deploy-2026-09-21`); a per-ticker bars-poll failure shows a named degraded banner, not a failed page (`deploy-2026-09-21h`); a slim red degraded line above the ladder (`deploy-2026-09-21b`, residents down 116 s vs the <60 s target); the STALE row + card badge (`deploy-2026-09-22`, aset restart ≈93 s down). Smoke K4.1–K4.4 PASS 09-23 (HTTP 200 incl. `/radar` with the value column and `/api/radar/pool`; K4.4 read 422 on the 09-22 look and 200 with `?since=` on 09-23). The heartbeat may read RED for a carried per-ticker poll failure in RTH (09-22 deploy first run refused on it; BACKLOG). |
| **F8/F10 LADDER CHANGE — all 13 setup definitions at defaults (09-21 R15/R17/R18/R44, his)** | **BUILT-NOT-MERGED — built and checked, deploys 09-24 on his DONE TRADING (09-23 R83)** | ONE build of the whole `SETUPS-AT-DEFAULTS-FINAL` (09-21 R44). `SETUPS ONE BUILD BUILT dd4a9b9` (09-22 09:42 ET, 9 of 9 steps, offline 2419/0, migration `0013_tunables_slug_nullable`) → check r1 (`SETUPS ONE CHECK DONE`, 3 of 4 houses, 3 HOLDS, ready 0 of 3) → fix r2 `826d284` → fixture cut `65c08a0` → fix r3 `be44eb4` → check r2r3 (5 HOLDS) → fix r4 `f5aaeb4` → check r4 (`SETUPS CHECK R4 DONE`, 3 houses ready YES, 1 HOLD: the test fixture cutter's fail-loud clause, SHIPPED with backlog by 09-23 R4(a)) → blind code seat `SETUPS BLIND CODE SEAT DONE · grok · MATCH 7 + 17 · MISMATCH 0` → the 09-23 stacked deploy stopped three times on gates (`FAILED: 2.2` ladder SHA pin; `2.3 (d)` live-note proof red) and the branch was DROPPED from that night's set (09-23 R78: Second Chance does not form against his live notes) → live-note fix `SETUPS LIVE NOTE FIX BUILT c9a11e14 | offline 2483/0 | with-DB 2838/0 | live-note 131/0` (`2026-09-24/01`) → check r1 (Gemini's 1 HOLD) → fix r2 `df7817a6` (with-DB skipped by 09-23 R104) → `SETUPS FIX R2 CHECK DONE · round: 2 · opus / grok FIX STANDS · defects that HOLD: 0`. Branch `setups/seven-0921` tip `c60a7f00`. Deploy prompt `2026-09-24/05-setups-deploy.md` DRAFTED (0 new strings; migration 0013; STEP-6 writes FIVE rows into his `Assumed Defaults.md`: 09-22 R119 ×3 incl. `dist.k.vwap`, 09-23 R82 A-19 / A-20); its house read `06` was IN PROGRESS at close. Known red carried into every later gate: vwap-continuation after STEP-6 (09-23 R107; a 09-25 vwap fix round owed). His L7 "approve" of the eight definitions the branch makes evaluable is recorded (09-23 R11 (c), reaffirmed in R52 / R109). |
| F12 Missed records (nightly replay) — S2-P4 | DONE-LIVE — **first SUCCESSFUL replay 09-23 21:10 ET** | Replay history: 09-21 21:10 FAILED (no `radar.benchmark` row); 09-22 21:10 FAILED (`movers: Change '' is not a percentage`); 09-23 21:10:00 → 21:12:19 ET DONE, exit 0 (`s2-smoke-look-2026-09-23.md`; log: `scans=235 … movers 40 · archived 39 · card misses 7 · mover misses 24 · … line updated`; 28 blank-`Change` rows per side counted as unranked, not fatal). Archiver nightly ran 09-21, 09-22, 09-23 (K13 PASS). One open item: `archive_incomplete: 1` (K9.4, one of 20 stored losers has no bars; ticker not yet named). |
| F13 Auto-archive + benchmark + miss line — S2-P4 | DONE-LIVE | `radar.benchmark` row loaded 09-22 07:04 ET (`top_n 20`, `min_move_pct 10`, sha256 verified; 09-22 R1 / R2). The 09-23 run wrote the miss line into `DRC-2026-09-23.md` (K10.1 unit `drc-misses/miss_line` present, K10.2 `vault_writes` 1 row); the 09-21 and 09-22 nights are recorded gaps (09-23 R17 (6), his "A"). A radar-card fill records no price and no shares today — live mornings need his hand-logged fill price + shares in the DRC chat (carried to BACKLOG). |
| S2-P1 / S2-P2 / S2-P3 / S2-P4 (code prompts) | DONE-LIVE ×4 | Unchanged since 09-20. |
| S2 smoke (`cobalt smoke s2 --prod`) | **RAN TWICE, NOT GREEN — AMBER 32 / 34 on 09-23** | 09-22 21:33 ET look (`S2 SMOKE LOOK DONE · replay ran: yes 21:10 FAILED · checks: 23 green / 11 red · … smoke green for S2: no`); the `58` relaunch that morning had `FAILED: window — too late` (its window is 21:20–23:30 ET; the desk's slip, re-issued as `03`). 09-23 21:44 ET look (`S2 SMOKE LOOK DONE · deploy: none · replay ran: yes 21:10 DONE · checks: 32 green / 2 red · reds expected tonight: 0 · real or UNPLACED reds: 2 · smoke green for S2: no · S2: DOES NOT CLOSE`): the two reds are **K9.4** (1 of 20 stored losers has no bars, `archive_incomplete: 1`; ticker unread) and **K17** (`cobalt validate` exit 1: five stray files under `docs/_inflight/`, unchanged since 09-22). Every 09-22 red — K3, K4.4, K7, K8.1, K9.2/.3/.5/.6, K10.1/.2 — cleared by the 09-23 smoke-only deploy. |
| Live mornings / S2 close (R46) | **S2 CLOSED 2026-09-23 on his override (`cto-2026-09-23.md` R113, 22:0x ET: the 09-23 smoke ruled GREEN, K17 + K9.4 set aside) — ONE live day banked (Mon 09-21); the green smoke night was ruled green, not measured green** (the close hub wrote "S2 LATE" before the ruling; corrected by desk `39116a00` 22:4x ET) | R46 (09-21): ONE live day beside DAS + ONE green smoke night. The live day is banked (R13). The smoke look's own verdict 09-23 21:44 ET: `smoke green for S2: no` (clause (c): 2 real reds) → **S2 LATE** (stop date 2026-09-23 passed). The reason in the look's own words: "S2 DOES NOT CLOSE — first failing clause: (c). The live day is banked (R46); this rule reads the green night only. The desk and he decide what follows (L37)." Both reds are small in the look's own words (K17 a housekeeping move; K9.4 needs one DB read to name the ticker). Nothing in either day's record sets a new S2 date — scope and dates change by his ruling alone. |
| Agent SDK spike (parallel, non-write) | NOT STARTED — decided: KEPT | Unchanged; no hub has re-scoped it yet. |

**Stop date: 2026-09-23. CLOSED 2026-09-23 on its stop date, by his override** (`cto-2026-09-23.md` R113, 22:0x ET, his words: "I don't want to call the smoke test a failure because housekeeping isn't done … I call this smoke test green; the failures are irelevant at best … Green and move on please." — L73 per-case override of 09-21 R46 clause (c) for K17 + K9.4; K17 leaves the S2 smoke for good, R114 "yes A"; the K9.4 mover-bars fix is `prompts/2026-09-24/07`). The close hub wrote "LATE" at 22:0x before the ruling; corrected by desk `39116a00` at 22:4x ET. The close's reasoning, as written: 09-21 R46 narrows S2 close to ONE live day beside DAS + ONE green smoke night. The one live day is **BANKED** (Monday 09-21, R13). The green smoke night was **NOT achieved by the stop date**: the 09-22 night's replay FAILED again (`Change ''`, an S2 smoke fix built and deployed the next afternoon, `deploy-2026-09-23`), and on 09-23 the replay ran clean but the smoke is AMBER with two real reds (K9.4, K17) — `smoke green for S2: no · S2: DOES NOT CLOSE` (`s2-smoke-look-2026-09-23.md`). **S3 preconditions:** the DRC template review — his sitting — was HELD 09-22 (15:14 ET, R60 → R65–R72 and the 21 owner items R90–R103; the DRC then went to the four-house tribunal, `DRC DERIVED v2`, R90 settling R2-1); the stop-override authority (mock #6) is RULED (09-20 R38, below). Owed for S2 (desk / hubs, from the two reds): a hub moves the five `docs/_inflight/` files per PLACEMENT (or the in-flight window is opened deliberately; 09-23 R17 (7): `_inflight` is the desk's own workspace); a read-only DB read names K9.4's ticker.

Owner rulings of 09-22 and 09-23 that touch S2/S3/S4 (each with its words in brief; full text in the 09-22 and 09-23 ledger appendices; `09-22 R<n>` / `09-23 R<n>` are the desk reports' §4 rows):
- **09-22 R1 / R2 (06:18 / 07:02 ET "approved")** — the replay benchmark `radar.benchmark` = `top_n 20`, `min_move_pct 10`; loaded 07:04 ET. STATE CHANGE: a `"user".trader_settings` row.
- **09-22 R3 (06:43 ET)** and **09-23 R5 / R83 (06:2x / 16:3x ET "I want the work done after I am done trading." / "A")** — per-case overrides (L73) of L43's one-deploy-per-evening + radar-restart window and L66's pause timing: 09-22 deploys from 11:00 ET; 09-23 and 09-24 deploys run on his "done trading" word.
- **09-22 R13 (09:4x ET "A")** — the three design tribunals (float handicap, stale-score, S3 exits) run this week on Grok · Gemini · Fable without Astra (Codex meter out to Sat 09-26 06:47 ET).
- **09-22 R32 / R36 / R76 / R109 (13:20 / 13:45 / 16:24 / 19:34 ET)** — Opus tasks on `claude-opus-5-5`; every Fable- and Opus-type seat incl. the desk on Opus 5.5 until his evaluation; each Fable seat asked; then "Make all Opus 5.5 for now" (standing). **09-23 R100 (18:33 ET)**: the next desk refresh launches on `claude-fable-5-1`.
- **09-22 R58 (14:28 ET) → R74 (16:1x ET)** — METER BRAKE through 09-27 (build lane only), then LIFTED ("full allotment for the week").
- **09-22 R61 (14:46 ET)** — no per-setup ON/OFF dial; `radar.cards_enabled` stays the one switch; tuning is the noise tool (supersedes R46).
- **09-22 R26 (12:1x ET "B")** — float handicap: pool-wide division; tribunal closed. **R52–R57 (14:19–14:23 ET)**: `missing: apply`, `combinator: any`, a DEAD column → factor 1, `decisive` suffix only, unhandicapped name first on a tie. **R37–R45 (14:05–14:10 ET)**: stale-score items 1–9. **R46–R51**: setups owner items (the `stop.buffer` label → dollars).
- **09-22 R60 / R65–R73 (14:42–16:05 ET)** and **R89–R103 (17:45–18:1x ET)** — the DRC sitting held: coach spec + trade-reporter pattern, no PDF, input-driven DRC, diff model A×4, Fable tribunal seat, all 21 owner items. **R67 (15:48 ET)** S3 exits R2-2: a held-count statement wins, DAS import reconciles (DAS is truth), overnight positions carry. **R114 / R116 / R117** DRC inputs (two hand-dropped CSV-in-`.md` files, one-to-one playbook names).
- **09-22 R80–R88 (16:55–17:2x ET)** — the LAWS sitting: routing tribunal runs (R81); L58 / L37 / L7 / L46 / L54 / L68 folds (R82); L43 kept at one deploy EVENT per evening carrying every branch (R83); L12 retired (R84); L75 new (R85); 09-21 P-d into L67, D5 into L48, K4 into L1 (R86); the agreed remainder (R87); trace before fold (R88). STATE CHANGE: `LAWS.md` applied ≈17:4x ET (75 entries).
- **09-22 R119 / R120 / R121 (21:18–21:2x ET "A")** — three word-only values into `Assumed Defaults.md` as ASSUMED (written by the setups deploy); an engine dial stays one number per setup that reads it; stop resolvers' `tunable_keys` = BACKLOG.
- **09-23 R18 / R39 / R56 / R57 (07:2x–13:13 ET)** — VOICE v3: one bidirectional widget, ephemeral audio, every house the same permissions; a voice-ordered edit of any field of any note on his confirmation; FINAL approved. STATE CHANGE: `LAWS.md` L28 amended 13:13 ET.
- **09-23 R21 (07:5x ET)** — routing owner items 20–37 (32: no house-specific writer profile; 33: a seat names a model family and resolves to its highest current model unless pinned; 34: Grok a standing blind-code seat).
- **09-23 R34 / R38 / R42 (09:2x–11:0x ET)** — JEV = the typesafe.ai typed classifier; trial via OpenRouter on Cobalt's funded key, model `typesafe/jev-1.13`, cap $5; N3 (trial runs) NOT yet approved.
- **09-23 R79 / R81 / R82 (16:0x–16:3x ET)** — the setups branch deploys 09-24 (not 09-23); GATE EARLY (a longer, more complete first round beats several rounds); Second Chance A-19 / A-20 ASSUMED. **R107 (20:58 ET "A")**: the vwap seam — all three R119 rows written, the vwap-continuation live-note red is a KNOWN RED.
- **09-23 R92 (17:4x ET)** — push approved provided everything checks out (executed). **R95 / R96 / R97 (18:08–18:1x ET)** — checker seats: designs + new builds Fable · Astra · Grok; every other check Opus · Sol · Grok (Opus + Grok when the OpenAI meter is short); never one house; Gemini out of code checks and deploy reads, optional fourth seat on new designs. STATE CHANGE (proposed, close list): L67's 09-21 R46 clause.

Owner rulings of 09-21 that touch S2/S3/S4 (each with its words in brief; full text in the 09-21 ledger appendix):
- **R13 (08:26 ET "A")** — a morning counts as live for S2 when radar and panel ran correctly beside DAS, even with an empty ladder; BANKED Monday.
- **R46 (18:05 ET)** — S2 closes on ONE live day + ONE green smoke night (narrows the prior "2–3 live mornings" reading); checker seats for finished-build code checks = Sol (OpenAI) + Opus 5 (Anthropic), design work keeps Astra + Fable. STATE CHANGE: `LAWS.md` L67 amended.
- **R47 (18:09 ET)** — each evening's ONE deploy carries every branch built and checked that day, as one stacked set. STATE CHANGE: `LAWS.md` L43 amended.
- **R15/R17/R18 (08:29–08:5x ET)** — all 13 setup definitions become evaluable at defaults, his seven daily setups first; no owner ruling before cards fire. **R44 (17:50 ET)** — the whole FINAL is one build, one check, one deploy (LADDER CHANGE row above).
- **R21 (10:43 ET "A")** and **R28–R30 (12:40–12:56 ET)** — device/product facts folded into the rows above; float-handicap tribunal round 1 could not run tonight (incident), carried TUE with a date-gate re-issue first.

Owner rulings of 09-20 that touch S2/S3/S4 (each with its words; the memory lines are the desk's):
- **R38 (18:38 ET "B with your addition") — stop-override authority (mock #6)**, the S3 precondition "before S3-P2": when he edits the stop, HIS stop becomes the plan until he resets it; Cobalt's structural stop stays visible beside it; the gap is recorded on the trade for the DRC / Friday review. Binds S3-P2's prompt (F11/F22). The "Rulings/inputs owed before S3" line and the carried item below are marked accordingly.
- **R27 (18:16 ET) — S4 preconditions:** "the trading PC on Tailscale is done"; the `.htk` files are labelled with "half" and "full" in the name (exact filenames not known). Both S4 preconditions (`:646-647`) met by his word; the audit's contradiction (ladder vs `cto-2026-09-16.md:123`) is settled — the PC IS on the tailnet.
- **R28 (18:19 ET) — device fact:** `sudo crontab -l` run by him → "crontab: no crontab for root": the root crontab is EMPTY, no root-level scheduled job exists on the Mac Studio; the carried item (`:658`) is closed.
- **R40 (18:44 ET) — device facts:** herdr IS handed to launchd · the Qwen Code upstream issue IS filed · `COBALT_VAULT_PATH` is NOT set in his interactive shell · whether the 09-19 settings copies in git matter: he does not know (desk decision, his veto: the two committed `23-packet` copies stay; no settings packet yaml is added to git from now on).
- R29–R31, R34, R36, R37 (18:21–18:36 ET, all "A"/confirm): archiver O-6 / R2-1 / C1 ruled for the shadow night; leg-count numbers his; replay deadline A2 and ESCALATE 19 accepted as built. Nothing in S2's scope changed.

OFF-LADDER work of 2026-09-20 (ruled, not on a ladder line; each with the ruling that ordered it):
- **Bars-lifecycle tribunal and its build chunks** — 09-18 R17 · 09-19 R10/R15 · 09-20 R9 (i1 only), R13 (tribunal launched), R19–R22 (all twelve owner rulings), R25 (chunks 1a + 2 launched). Tribunal DONE in three rounds → `BARS-LIFECYCLE-FINAL-2026-09-20.md` (`ef184bb`). **Chunk E** DONE + checked 3 of 3 (`BARS CHUNK E DONE · experiments run: 20 of 20 · AS EXPECTED: 18 · NOT AS EXPECTED: 2 (E-6b, E-9)`; check `houses that checked: 3 of 3`; branch `bars/chunk-e-0920` `982d958`). **Chunk 1a** BUILT (`c597bfe`), round-1 check split (astra FIX FIRST), fix 1 BUILT (`793f452`, X1–X13) + fix 1b BUILT (`1404f23`, X14, the child-name seam), round 2 checked by 2 of 3 (gemini HARNESS): 12 of 13 FIX rows closed, X9/X14 naming reconciliation open → round 3 is a CHECK by all three houses with X14 in the question set; branch tip `6961ee0`. **Chunk 2** BUILT (`47ef9af`), round-1 check 2 of 3 (astra METER), fix BUILT (`d768674`), round 2 checked 3 of 3, split 2–1 (astra FIX AGAIN X1 + O4-in-memory-range), 4 of 5 FIX rows closed → a round-3 fix (the last) is next; branch tip `1351da6`. **BUILT-NOT-MERGED — nothing deploys before WED 09-23** (R20 order 2: the Lists `[i1]` + writer refusal land Wed evening; the swap is a weekend he names after the rehearsal). Still ahead: every `requires_db` first run on `cobalt_dev` (19 tests written, never run), the L68 stacked gate of `bars/chunk-1a-0920` + `bars/chunk-2-0920`, chunk 4's drafter (R45; the `--proof-only --full` gap), his O1 (asked 21:14 ET, unanswered, blocks nothing) and O2–O4, O6.
- **Laws audit (09-20 R10) and memory research (09-20 R11)** — DONE, read-only registers (`laws-audit-2026-09-20.md`, `memory-history-2026-09-20.md`); both sittings PENDING (table in `BACKLOG.md`); L71–L74 and L68 (twice amended) folded from the 09-19 close's proposals (R2–R8).
- **His-plate audit (09-20 R26)** — DONE (`his-plate-audit-2026-09-20.md`: 39 rows, DONE 6 · OPEN 27 · NOT ESTABLISHED 6); its answers folded into R27/R28/R40/R41.
- **Restic password rotation** — NOT DONE (09-20 R41 "no"); his hand; the step list is drafted Monday with `ops-0921` (R42).
- Standing from 09-19, unchanged: three production deploys (`deploy-2026-09-19`, `-19b`, `-19c`); the append-only archiver in `upsert` (first nightly Mon 20:30 ET; the `append` switch is his separate ruling, NOT STARTED); ops 0919 items DONE-LIVE; the L68 stacked gate as practice; **R34 C** (stagger the pool cadences) NOT STARTED; fund rule and card values sit inside F13 / F8 / F10 above.

OFF-LADDER work of 2026-09-21 (ruled, not on a ladder line; each with the ruling that ordered it):
- **Bars chunks 1a + 2, round 3 (the last, L67)** — DONE in the morning: chunk 2 round-3 fix BUILT `fac0baf` (Y1–Y4) → chunk 1a check r3 3 of 3 FIX STANDS (`reports/bars-chunk-1a-check-r3-2026-09-21.md`, X9/X14 one shape settled — gemini's headless-shell cause found and fixed) → chunk 2 check r3 3 of 3 FIX STANDS (`reports/bars-chunk-2-check-r3-2026-09-21.md`). **BOTH CHUNKS CHECKED** (three rounds each); nothing deploys before WED 09-23 (09-20 R20); still ahead: `requires_db` first runs on `cobalt_dev`, the L68 stacked gate of the two branches, chunk 4's drafter.
- **Float handicap (R28–R30)** — a soft penalty (never exclusion) on float < 50 M or market cap < 500 M, thresholds confirmed; design proposed (chunks: 3, migration: yes); Fable seat ruled BUILD AFTER (blind, R30); three-house round 1 staged but **could not run — Anthropic incident**; TUE, its date gate needs a one-line re-issue to R39's literal first.
- **Stale marker (R36) — BUILT.** `s2/stale-marker-0921` `ca9566f`: row + card badge on stale-bars tickers, `RESTARTS: com.cobalt.aset`, BUILT-NOT-MERGED; four-checker check `68` owed TUE (R49 seats).
- **Stale score (R36 ESC 1 → R51)** — a card-scoring-on-stale-bars design proposed (4 options, recommended C); Fable DESIGN seat approved; tribunal prompts `62`/`63` owed TUE.
- **Typesafe classifier research (R31/R34/R35/R37)** — broad research DONE (11 of 11 domains, 23 examples, 8 latency facts, 19 trial measurements); the hands-on trial APPROVED (his spend, his hands for sign-up/key — never in chat/`.env`); the design tribunal runs after S2 closes and the setups chunks are built (queue item, never dropped).
- **Ops 6a (09-20 R41/R42, R43)** — 6a (vault key store into restic's include set) BUILT, checked r1 4 of 4 (2 dissents on the classifier), fix `77` BUILT `ac2e7ae` (jobs.yaml rule), checked r2 3 of 4 (Sol FIX AGAIN, reader-proof gap), fix round 3 (the last) `80` BUILT `af77d6b` (code-derived reader proof through wrappers). `ops/2026-09-21` `8f3db83`, BUILT-NOT-MERGED; check `81` (four checkers) owed TUE. 6b (a production restore read) is re-drafted as a **fresh-host restore drill** before it runs (three checkers found the README-copy proof insufficient); waits on his restic rotation.
- **S3 exits proposal + tribunal (R48, R57)** — `S3-EXITS-PROPOSAL-2026-09-21.md` (6 chunks, 5 write-path, 2 migrations, ≈50 h build estimate); Fable DESIGN seat approved (R57); tribunal prompts `73`–`75` drafted (astra required), runs TUE beside the three-house round.
- **DRC sitting packet (R48, R52) — READY.** 15 decisions, 12 blocking S3-P3, ≈30 min; his sitting, he names the time — stays PENDING with its age.
- **Anthropic incident 20:57–22:0x ET** — status.claude.com "Elevated errors for multiple models" (Fable, Opus 5, Mythos); `38` (handicap tribunal) and `58` (S2 smoke first look) both ended every turn on 500/529 and were stopped for the night, staged work intact, nothing lost; the Opus `acceptEdits` build (`65`) kept working through it.
- **Restic password rotation** — still NOT DONE; his hand (exposed since 09-11, now 10+ days).

OFF-LADDER work of 2026-09-22 and 2026-09-23 (ruled, not on a ladder line; each with the ruling that ordered it; status per the legend, evidence in the ledger blocks):
- **Stale marker + ops 0921 (09-21 R36 / R42 / R43; stacked deploy 09-22 R3 / R10)** — **DONE-LIVE**, `deploy-2026-09-22` `d2d82e70` (branches `s2/stale-marker-0921` round 2 `27eaa0c` and `ops/2026-09-21` `8f3db83`; `STACKED DEPLOY DONE d2d82e7 … residents down 93 s · rollback: not used`). Ops 6b (a fresh-host restore drill) NOT STARTED, waits on his restic rotation.
- **S2 smoke fix (09-22 `76`, 09-23 R1 / R2 / R26)** — **DONE-LIVE**, `deploy-2026-09-23` `4e4577c3` (`S2 SMOKE FIX BUILT b510b65` → checked r1 + r2, 3 × YES; the ONE-branch `SMOKE ONLY DEPLOY DONE`, residents down 17 s). The replay's blank-`Change` crash is fixed (09-23 21:10 run DONE).
- **Setups seven-setups build + Second Chance fix (09-21 R44; 09-22 R46–R51, R119; 09-23 R78 / R79 / R82 / R83 / R107)** — **BUILT-NOT-MERGED (built + checked, deploy 09-24)**; see the F8/F10 LADDER CHANGE row. The prompt-named `2026-09-24/01` Second Chance fix is BUILT `c9a11e14`, not "building" — it ran 17:00–17:56 ET on 09-23.
- **Stale-score (09-21 R51; 09-22 R37–R45, `31` / `32`)** — design **CLOSED** (`STALE SCORE DERIVED v2 … needs round 2: 0`, all 9 owner items ruled); build `46` **BUILDING (stopped by the desk 09-23 R73)**: branch `cards/stale-score-0922` `57925f3b` holds RED tests, no code; it stacks on `setups/seven-0921`, resumes after the 09-24 deploy (one `CONTINUE:` line, the dev-DB lock).
- **Float handicap H1 (09-21 R28–R30; 09-22 R26 / R52–R57)** — design **FINAL** (v3 + R26; tribunal closed); build **NOT STARTED**: `27` / `28` drafted, worktree `radar/handicap-h1-0922` cut (`be4c79b5`) with no build; `47` waits for the 09-24 deploy (the `0013` / `0014` migration seam).
- **S3 exits (09-21 R48 / R57; 09-22 R58 / R62 / R67)** — design **FINAL** (`S3-EXITS-v3-2026-09-22.md` + R67; Astra reads Sat 09-26); build prompt owed; **NOT STARTED** (the S3-P1 / S3-P2 line, S3 opens 09-24).
- **DRC automation (09-22 R60 / R65–R73, R89–R105, R114–R117; 09-23 R17, R59, R60)** — design derived (`DRC-AUTOMATION-v2`); **D1 BUILT-NOT-MERGED** (`DRC D1 BUILT f6798406`, offline 2126/0, with-DB 250/0; branch `drc/d1-trading-log` `7ed5e5ee`; migration renumbered by the desk at its deploy); **D1 check DONE** (`… defects that HOLD: 14 · ready for the next chunk: 2 of 3`) — a classify-first fix round (L75) is owed; D2–D5 NOT STARTED (D4 → D2 → D3 order; they wait on the D1 fix and E1 — his real DAS export + TradeZella log dropped 09-18).
- **Voice v3 (09-22 R100 / R106 / R108; 09-23 R18 / R39 / R56 / R57)** — design **FINAL, approved for build** (`VOICE-v3-FINAL-2026-09-23.md`, sha256 prefix `8c469b9544282b55`); **V1 BUILT-NOT-MERGED** (`VOICE V1 BUILT 566d1848`, report `28b6b0c6`; its migration `0017` was rolled back off `cobalt_dev` 09-23 15:09); V1 check `FAILED: packet` (over the 230,000 B ceiling, no checker launched) — a re-cut packet plan is owed; V2–V5 NOT STARTED; his phone session 09-24 (R92).
- **JEV trial (typesafe.ai classifier; 09-21 R34 / R35; 09-23 R34 / R38 / R42 / R86 / R89)** — **BUILT-NOT-MERGED, probe run**: build `45f647a` → fix r1 `043c3ba8` → fix r2 `772b60af` → fix r3 `09f38f4d` (report `f4e8de85`); check A rounds 1–3 (`SECRETS CLEAN ×3`, 1 HOLD F7-COST fixed in r3); ONE keyed probe run (`JEV PROBE DONE · $1.3188e-05 of $5`); check B / the final check `74` and N3 (trial runs, not yet approved) owed.
- **Routing (09-22 R81, R104, R109; 09-23 R7 / R21 / R24 / R25 / R28)** — tribunal DONE (`ROUTING DERIVED v2`, 18 owner items; 20–37 ruled 09-23 R21; Astra reads Sat 09-26); the retrospective validation X5 **BUILDING (PAUSED by the desk, `PAUSE` file, last line `(run in progress — next step under ## CONTINUE)`)**, the Sonnet shadow build X1 NOT STARTED (its worktree cut approved, never launched), Terra X2 waits on the Codex meter.
- **LAWS sitting (09-22 R4 / R80–R88)** — **DONE-LIVE (the file)**: `LAWS.md` applied 09-22 ≈17:4x ET; `LAWS.md` L28 amended again 09-23 13:13 ET. The close's PROPOSED L67 amendment (R95) and the two GATE EARLY law candidates (09-23 R81) are in `close-2026-09-23.md`.
- **ASET attest forensics (09-23 R29 / R30 / R31)** — DONE (`ASET ATTEST FORENSICS DONE · cause: BUG · fix size: small`); NO fix on the sheet itself; three gaps (silent refusals, no attest history, no `Cache-Control` on `GET /`) carried to the successor lane, BACKLOG row added.
- **Dev-DB repair (09-22 R122 / R124; 09-23 R4 (c) / R12 / R15 / R16)** — **DONE**: `DEVDB REPAIRED · head: 0011 · max dropped: 0 · tenancy: 34/0 · r3 reds: 3/0` (Opus 5.5, `acceptEdits`, the D6 gate re-issued); voice V1's `0017` rolled back off `cobalt_dev` 09-23.
- **Bars chunks 1a + 2 (09-20 R25)** — **BUILT-NOT-MERGED, CHECKED since 09-21**; neither day's record names their next step; ≥ 3 days unmerged (L46 as amended 09-22 R82 C6: named on the plate or merged / deleted) — ESCALATE in `close-2026-09-23.md`.

### S2-P1 prompt — DRAFTED 2026-09-09 (architect session PART 2), NOT RUN

Runs once Dejan hands over the 4 Finviz dynamic screens (user data — vault note or
`"user".trader_settings`, never the repo; the repo ships one synthetic example screen).
Opus 5 · fresh · worktree `~/cobalt-wt/s2-p1-radar-pool` off main · report + READY FOR MERGE ·
LIVE block names RESTARTS via `cobalt jobs readers` (Ops prompt 09-09 item G).

- **Line 0: ADR-0008 in force.** `system` / `"user"` schemas, side per store; every new table
  declared in `src/cobalt/db_migrations/placement.py` or the placement test fails.
  `radar_pool` + `radar_membership` are already DECLARED system-side; the account-mode tag is a
  `"user".aset_sizings` column. First cross-side join J1
  (`"user".aset_sizings.pool_member_id → system.radar_membership.id`); suite asserts sides.
- **F2 pool job `com.cobalt.radar`** (resident, F17 wrapper, `reads:` declared): sources = the
  4 TV static lists (today `configs/cobalt/watchlists.yaml` tiers — user data by L32, moved
  user-side in this prompt, ADR-0008 ESCALATE 8) + the 4 Finviz dynamic screens
  (`/export/screener?v=152&f=<filters>&c=<cols>` per DATA-SOURCE-MEMO §1; deterministic
  collector, cached CSV, no LLM) → ≤ `radar.pool_cap` (tunable, 50) rotating names; churn
  every `radar.scan_interval` (tunable, 60 s); premarket included via the F1 session clock;
  membership history persisted (`entered_at`, `left_at`, `source`, `excluded_by ∈
  {config_cap, not_equity, manual}`); a dead source = degraded flag on the pool row and a red
  F18 line, never an empty pool.
- **Finviz bar poller at `working_timeframe`** (2m, `configs/cobalt/taxonomy/defaults.yaml`)
  for pool names: reuses `cobalt.archiver.collector.fetch_bars` + its token resolution (the
  live-feed spike's path); i1 → 2m aggregation deterministic; bars land in `system.bars` with
  the archiver's schema (one path, no second bars table). First build step: re-measure Finviz
  throttle at 50 names on a 10 s grid and report the number before the cadence is set.
- **Account-mode tag:** `"user".aset_sizings.account_mode ∈ {live, sim}` from the day-mode
  row / trader_settings, stamped on every card; migration + placement + tests.
- **Smoke (dev vault + cobalt_dev):** replay a recorded session from the archiver corpus —
  pool churns, cap holds, a name entering on RVOL appears within one interval, membership rows
  carry `excluded_by`; F18 gains a `radar` freshness probe.
- **NOT in P1:** precondition evaluator, dots, panel, F12/F13 — S2-P2…P4 as listed above.

**Rulings/inputs owed before S3:** DRC template review session (Dejan +
Claude, his docx + SMB template → live Templater template) — before S3-P3.
Stop-override authority (mock #6) — before S3-P2. **[RULED 2026-09-20 R38 —
"B with your addition": his edited stop is the plan until reset, Cobalt's
stop stays visible, the gap is recorded; see `### Status 2026-09-21`.]**


LADDER EDITS 2026-09-10

1. In the F2 Radar pool row and the S2-P1 prompt block, replace
   "≤ `radar.pool_cap` (tunable, 50)" with:
   "≤ the cap in the vault pool block (`kind: pool` in `1 - Trading/Radar Screens.md`,
   50 today). Committed config carries engine tunables only — never a cap, rank rule,
   metric choice or stickiness (ruled 09-10)."

2. Replace the heading "### S2-P1 prompt — DRAFTED 2026-09-09 (architect session PART 2), NOT RUN"
   with:
   "### S2-P1 — BUILT 2026-09-10, IN HUB GATE; LIVE 09-11 after close"
   and replace its first paragraph with:
   "Screens filed 09-09. Plan FINAL 09-10 (`_inflight/plan-s2-p1-2026-09-10.md`, Astra 3 rounds,
   dissent recorded). Houses: Opus 5 architect · GPT-6-Astra plan review · GPT-5.6-Sol build
   (`-s workspace-write`, no DB, cannot commit) · Sonnet hub verifies and commits.
   Worktree `~/cobalt-wt/s2-p1-radar-pool`, branch `sprint-2/radar-pool` off main.
   Two stages: stage 1 = steps 0–13, stage 2 = the archiver moving to the Lists note.
   LIVE 09-11 after close, including the HITL vault write (one deploy per evening, L43)."

3. Add to the S2-P1 bullet list (scope that grew after the draft):
   - Screens/Lists contract: fenced YAML per screen + one `kind: pool` block in
     `1 - Trading/Radar Screens.md`, and `1 - Trading/Radar Lists.md` for the static lists;
     written once via propose → HITL card → apply, then read-only with hash reload and a
     `"user".trader_settings` mirror. Stage 2 deletes `configs/cobalt/watchlists.yaml`.
   - `cobalt db query` — read-only, SELECT-only enforced in code, factory connection with
     SET ROLE (no `psql` on the host).
   - `cobalt jobs restarts <range>` — the L42 derivation tool, output pasted in every report.
   - Account mode: standing `live` in trader_settings, per-day sim switch on the sheet
     attestation, card refused when unresolved.
   - Rank rules per the 09-10 pool ruling (volume premarket / RVOL after 09:30, Morning Low
     Float always volume, Day Scan first among screens from 10:00, screens before lists,
     stickiness 3 scans).

4. In "Carried open items", the restic bullet: strike
   "**still needs copying into a password manager off both devices**" — `RESTIC_PASSWORD` and the
   Cobalt store master key have been in LastPass since 09-09. Replace with:
   "Password in LastPass (09-09). OWED: the Cobalt key store into the nightly include set plus a
   restore proof. B2 offsite still OFF — one local copy has already failed once (09-06)."

---

## S3 — Exits + DRC on radar cards (09-24 → 10-07; was 10-05 → 10-16)

**S3 opens 2026-09-24 (stop 10-07).** Designs already at a FINAL: S3 exits (F11 · F22) — `S3-EXITS-v3-2026-09-22.md` + 09-22 R67 (Astra reads Sat 09-26); DRC (F14) — `DRC-AUTOMATION-v2-2026-09-22.md` derived, R2-1 settled by 09-22 R90, all 21 owner items ruled (R90–R103), build prompts drafted and D1 already BUILT (`f6798406`, checked, 14 HOLDS). F15 prediction records: no design yet. (Off-ladder but S3-adjacent: voice v3 FINAL, approved 09-23 R57.)

| Feature | Charter acceptance (test) | What S3 delivers |
|---|---|---|
| **F11 Fill recompute + fill/exit capture** | Fill 27% past plan → warning, FILLED row, DRC counts it as a trade; a ½-off tap during the trade produces an estimated leg without a keystroke. | TRIGGERED → FILLED @ [last poll, editable] + PASS; drift warning scaled to ATR (his 09-03 defect), >20% distance = "re-read stop"; `legs` table {card, shares, price, time, flag estimated/confirmed}; ½ · ⅓ · flat · typed compounding off running shares; running 0 → CLOSED; realized R provisional while any leg estimated; DM line "TSLA filled 372.82 10" / "TSLA out 374.50 all" writes the same rows. No tap by expiry → EXPIRED. **Attestation check (ruled 09-04, soft):** the `.htk` sheet stays a self-report — he states which file he loaded, it persists on the `day_modes` row, and a fill is recorded against that stated sheet. Reading DAS's own loaded-hotkey state, and overwriting the attestation from it, are DEFERRED: the trading PC is not on the tailnet and CLAUDE.md forbids touching DAS at all, so a hard check has nothing to read. The soft check still refuses card creation while the attestation disagrees — including when nothing has been attested. |
| **F22 Trade-note auto-creation** | A fill at 10:12 has a trade note by 10:13. | On FILLED: trade note via vaultwrite (create-if-absent, frontmatter site, L28) lighting the dataview table; legs update the note in place. Verify whether slice-2's version exists; if so, convert to the state-machine event. |
| **F14 DRC prefill / reconcile / DRC→mode** | 09:00 proposal quotes the prior DRC; DRC note exists at 15:41 with every Cobalt field filled. | Separate `DRC-YYYY-MM-DD.md` in SMB format from the reviewed Templater template; prefilled 15:40: cards written / trades taken (FILLED only), every unfilled card asked taken/passed/discarded, pick-vs-rank, miss line, cost-of-discipline tally, adherence checkboxes, excitement audit, estimated legs to confirm, time blocks, PnL; daily note gets 3-line stub + link; next-morning F6 proposal cites it. `drc_builder` PDF = SHOULD, only if the sprint has room. |
| **F15 Prediction records** | Any card's grade replays from stored inputs. | Every score + WHY stored with its inputs and joined to the card outcome (legs, realized R, MISSED counterfactual); a `replay(card_id)` command recomputes the grade from stored inputs and diffs. This is the corpus the post-MVP reasoning layer trains on. |

**S3 smoke:** one live morning: radar card graded by tap, filled, ½ off,
closed; trade note at fill; DRC note at 15:41 with the estimated leg, pick-
vs-rank and miss line; next morning's 09:00 proposal quotes that DRC;
replay of the card's grade matches.

**Code prompts owed:**
- S3-P1 · Opus 5 · fresh · F11 legs, scale-out, ATR-scaled drift, DM fallback line, EXPIRED timer.
- S3-P2 · Opus 5 · fresh · F22 trade note as state event · stop editing per override ruling.
- S3-P3 · Opus 5 · fresh · F14 DRC note (after the template review) · F15 prediction records + replay · S3 smoke.

### Status 2026-09-24
S3 status block (SESSION-CLOSE step 4a, ruled 09-19 R14); S3's first; the S2 block of the same name above stays as the 09-23 close wrote it. Written by close hub `close-0924` from `reports/cto-2026-09-24.md` (§4 R1–R95, all §5 blocks), the last line of every 09-24 report, the four build reports read from their branches (`git show`), and `s2-smoke-look-2026-09-24.md`; re-verified against the tree (L35): `git tag --list "deploy-2026-09-24*"` = `deploy-2026-09-24` → `a2d320b8`; `origin/main` = `de48c19b` (pushed 09-24 R74), main 34 docs commits ahead. Status only — scope, dates and order change by his ruling alone. Legend: DONE-LIVE · DONE-DARK · BUILT-NOT-MERGED · BUILDING · NOT STARTED.

| S3 feature | Status | Evidence |
|---|---|---|
| F11 Fill recompute + fill/exit capture | NOT STARTED | Design FINAL: `S3-EXITS-v3-2026-09-22.md` + 09-22 R67 (Astra reads Sat 09-26 06:47). No build prompt, no branch, no report dated 09-24. |
| F22 Trade-note auto-creation | NOT STARTED | Same design; S3-P2 line. No build prompt, no branch. |
| F14 DRC prefill / reconcile / DRC→mode | BUILDING | D1 BUILT + CHECKED (`DRC D1 FIX R1 BUILT d1342595`; `DRC D1 FIX R1 CHECK DONE · round: 2 · … defects that HOLD: 0`, R31; branch `drc/d1-trading-log`, migration `0016`). Overnight-position lane: tribunal CLOSED at round 2 (R51 "A", R52 "b"; `DRC-OVERNIGHT-POSITION-v3-2026-09-24.md`); K1 `DRC K1 BUILT 9a0fc900` (migration `0018`, `offline 2438/0 · with-DB 2843/0 · live-note 142/0`) → check r1 `… defects that HOLD: 3 · ready for K2: NO` → fix r1 `DRC K1 FIX R1 BUILT 40cf173e` (`offline 2441/0 · with-DB 2848/0 · live-note 142/0`); fix-r1 check `49` queued, not launched; K2 drafted (`51` / `52`, `DRC K2 BUILD DRAFTED · migration: none`), not launched; D2–D5 NOT STARTED. Nothing DRC is merged; `0016` / `0018` absent on `cobalt_dev` (build probes). |
| F15 Prediction records | NOT STARTED | No design, no prompt. |

**Stop date: 2026-10-07. S3: ON TIME — day 1 of 14.** Reason: the sprint's one BUILDING feature (F14) advanced by two built chunks and a closed design lane on day 1; F11 / F22 are design-FINAL with no build prompt yet and F15 has no design, but 13 days remain and nothing in the day's record slips a date. Watch items (not a slip): the DRC stack's deploy (D1 → D4 → D2 → D3 + K1 + K2) is not drafted; the dev-DB lock (L76) serialises every with-DB build; nothing was built or drafted for F11 / F22 today because the day went to the setups deploy, its re-land and the off-ladder builds below.

OFF-LADDER work of 2026-09-24 (ruled, not on a ladder line; each with the ruling that ordered it):
| Item | Status | Ruling · evidence |
|---|---|---|
| Setups seven + Second Chance fix (all 13 definitions at defaults) | DONE-LIVE | 09-21 R44 / R15; 09-23 R83 "A" (deploy on DONE TRADING); 09-24 R3 / R39 / R45. `deploy-2026-09-24` = `a2d320b8` (the re-land; the first run `FAILED: 4.7 (b)` at 11:40 and rolled back, R42). `SETUPS DEPLOY RELAND DONE · reland: a2d320b8 · tag: deploy-2026-09-24 · rows: 0 …`. His four assumed rows written after (R55 / R56, write_ids 3579 / 3581; `dist.k.vwap` held, R118) and loaded (`cobalt taxonomy load` 15:43:35, R58 / R59). Second Chance REDESIGN and VWAP Continuation review = PENDING SITTINGS (R13 / R14), packets drafted, unheld. |
| Mover-bars fix (K9.4) | DONE-LIVE | 09-24 R7 "I approve A"; same deploy (`replay/mover-partial-0924`, `MOVER BARS FIX BUILT b69a6681`, check `… FIX STANDS ×2 · defects that HOLD: 0`). Tonight's smoke: K9.4 shows (gainers 0/0, losers 1/1), K17 gone. |
| Stale-score r2 | BUILT-NOT-MERGED | 09-22 R37–R45; 09-23 R58; 09-24 R68 (rebase pair). `STALE SCORE BUILT 01ee8bcd`, branch `cards/stale-score-0922` tip `358f1f75` (migration `0015`, `cobalt_dev` at `0013`); CHECKED R88 (`STALE SCORE CHECK DONE · round: 1 · BUILD STANDS ×2 · defects that HOLD: 0`). Deploys in the 09-25 set with H1 (ONE set, L43), after the deploy prompt is drafted. |
| Handicap H1 r2 | BUILT-NOT-MERGED | 09-22 R26 / R52–R57. `HANDICAP H1 BUILT 27df13f1 | on f6643d41 | … | migration: 0014 rolled back | h=1 identity: proven`; branch `radar/handicap-h1-0922`. Check `45` last line: `(run in progress — next step under ## CONTINUE)` — IN PROGRESS at close, not judged. |
| Voice V1 (voice v3 FINAL) | BUILT-NOT-MERGED | 09-23 R57; 09-24 R43 / R60 / R68. Round 1 (parts A–D) 24 HOLDS → fix r1 `VOICE V1 FIX R1 BUILT d4e48f22` → check r2 `VOICE V1 FIX R1 CHECK DONE · round: 2 · opus: DEFECT REMAINS · grok: FIX STANDS · defects that HOLD: 3` → fix r2 `VOICE V1 FIX R2 BUILT d319e4f3 | … | FIX: 7 of 7` (branch `voice/v1-0923`, migration `0017` rolled back). Round-3 check `55` (the last) queued, not launched — a HOLD there goes to him as ONE message. His DEVICE SESSION is OWED before any ship (R71). |
| DRC overnight-position lane (F14) | see the F14 row | 09-24 R22 (his design order); R51 "A", R52 "b". Tribunal closed; K1 BUILT + fix r1 BUILT; the lane's FINAL document is owed (no v3 FINAL file — `51` / `52` cite v3 + R51 / R52). |
| Replay deadline regression | RED — fix NOT STARTED | Ordered by no ruling; desk record R95. The 09-24 21:10 replay FAILED at 21:40:06 (`DeadlineExceeded` at the `line` step, deadline 21:35 ET): 13 setups live → the formations step ≈ 29.5 min on 3,225 formed. K10.1 / K10.2 (the miss line for 09-24) not written. Fix drafter prompt `56-draft-replay-deadline-fix.md` written and RUNNING at close (`57-replay-deadline-fix-build.md` untracked, mid-run); its report `replay-deadline-fix-draft-2026-09-24.md` does not exist yet, the fix BUILD is not started. 09-25's 21:10 replay fails the same way unless a fix lands in the 09-25 set. |
| Overnight-lane tribunal, sitting packets, and the day's prompt drafters | DONE (design / drafts) | R14 packets (`sitting-packets-draft-2026-09-24.md`, `SITTING PACKETS DRAFTED · packets: 2`); each drafter stopped on its own `… DRAFTED` line (ledger block 2026-09-24). |

---

## S4 — 19b trigger detection + strike alert (10-08 → 10-14, ONE WEEK, CAPPED; was 10-19 → 10-23)

**Preconditions (must be true on 10-19 or the sprint slips, not stretches):**
trading PC on Tailscale (his) · `.htk` hotkey labels checked against
`{DAYMODE}-{KEY}-{SIDE}` (his, mock #3) · F8 live since S2.

| Feature | Charter acceptance (test) | Week plan |
|---|---|---|
| **F9 19b, focus scale** | Alert on the panel ≤5 s after bar close, premarket + RTH; if Finviz throttles at 3 s, criterion re-rules to what 10 s delivers (~8 s). | Day 1: re-measure at 2–3 s cadence, premarket + RTH, ≤5 names (spike script pattern, measurement only) → criterion fixed. Days 2–3: price-cross detector with the card's confirmation policy on ≤5 ARMED names; TRIGGERED transition + MISSED on unarmed. Days 4–5: SSE push → pinned browser tab on the PC over Tailscale, browser notification + sound, three numbers + hotkey; Mattermost DM phone fallback. Friday: whatever is proven ships; remainder → post-MVP lane (toast listener, other trigger types). |

**Code prompts owed:** S4-P1 · Opus 5 · fresh · re-measure + detector;
S4-P2 · Opus 5 · fresh · SSE delivery + notification + fallback + week report.

---

## S5 — Prep + platform + playbook (10-15 → 10-28; was 10-26 → 11-06)

**Flag:** this is the ladder's heaviest slot (F20/F21 are the Agent SDK
bring-up). It holds only if the S2 SDK spike ran. If S5 overflows, F4/F5
(prep, §7 rank 5) are not cut — they are MUST — but F23 PPTX renderer is the
first candidate to slip into the acceptance week, since M11 is weekly.

| Feature | Charter acceptance (test) | What S5 delivers |
|---|---|---|
| **F4 Prefill all day, ownership flags** | He writes at 06:00, prefill re-runs at 08:45, his text byte-identical; diff row in `vault_writes`. | Config cadence + manual trigger; per-field flag cobalt / cobalt-degraded / human; "as of HH:MM" stamps; VIX/BTC loud "n/a (manual)". |
| **F5 Market-context checkpoints** | 08:15 block cites what changed since 07:45; source outage = degraded, never blank. | 07:15/07:45/08:15/08:45 jobs: Finviz numbers deterministic; single-house narrative (Claude on subscription via fast wire, L22) receives the filtered list only, returns delta vs previous; missed checkpoint loud. |
| **F20 Chief of staff, thin** | A config-drafted agent appears only after an approved HITL card. | One resident SDK session on subscription auth; he talks only to it (Mattermost); HITL cards in one place, Approve/Deny; agent registry as data (L16), no agent code. |
| **F21 Genesis import + continuity pack** | Cobalt answers "why is the stop buffer 0.02" from the imported record. | Ledger + vault history through the memory pipeline into cobalt_brain; continuity briefs stored in Think outside the repo (authoring = Dejan + fleet chats, starts during S2). |
| **F23 Playbook PPTX renderer** | One deck per setup family with the latest cards. | trade-reporter renderer from playbook data; Sunday 18:00 job. |
| **F16 close** | `validate` passes; no inline literal in a predicate. | Final sweep across all consumers. |

**Code prompts owed:** S5-P1 · Opus 5 · fresh · F4 cadence + flags; S5-P2 ·
Opus 5 · fresh · F5 checkpoints; S5-P3 · Opus 5 · fresh · F20 CoS + HITL +
registry; S5-P4 · Opus 5 · fresh · F21 genesis import; S5-P5 · Sonnet · fresh ·
F23 renderer (no vault write). SHOULD Vital Dawn only if a slot frees.

---

## Acceptance week (10-29 → 11-04; was 11-09 → 11-13) — Charter §12

Every §3 MUST passes its test on the live vault + live DB, five consecutive
trading days, heartbeat green, card used in ≥3 live mornings. Then the
post-MVP lane (§11) fights for slots at sprint boundaries.

## Carried open items (owner)

- Trading PC joins Tailscale (his) — S4 precondition; S1-P1 reports status. **[DONE by his word 2026-09-20 R27: "the trading PC on Tailscale is done."]**
- `.htk` label check (his) — S4 precondition. **[DONE by his word 2026-09-20 R27: the `.htk` files carry "half" / "full" in the name; exact filenames not known.]**
- `.htk` attestation is self-report until S3 — the soft check ships in S1 and stands through S2; F11 is where a fill is first recorded against the attested sheet. Nothing reads DAS before then, and nothing is planned to (ruled 09-04).
- Health thresholds (#8) + detail-column order (#11) — before S2-P3.
- DRC template review session (Dejan + Claude) — before S3-P3.
- Stop-override authority (#6) — before S3-P2. **[RULED 2026-09-20 R38.]**
- Trade-count goal band value (his, Rules Engine session) — placeholder in S1.
- Hand-logged legs in the DRC chat continue until F11 lands (S3).
- Vault backup restic → B2 + SSD (gated, before Tahoe) — **SSD LEG ARMED 2026-09-05; B2 PENDING** (branch `ops/backup-arm`). `com.cobalt.backup` is loaded and runs 21:40 every day, all week, after the archiver's 20:30. First real snapshot `21b03675`: 551 files, 422.7 MiB, 439.3 MB added, 3m40s, exit 0 — the vault plus a fresh 360 MB `cobalt_brain` dump, to a 500 GB APFS volume at `/Volumes/COBALT-BACKUP` (physical `disk4`). **Restore proven against THIS repository, not a throwaway**: one daily note restored byte-identical to live (15,548 bytes, 396 lines, same sha256), and the dump reloaded into a scratch database matching `cobalt_brain` on all 28 tables, 4,792,389 rows, and md5 `4a80bf6d…` over 4.79M ordered `bars` rows; the scratch database is gone. `RESTIC_PASSWORD` is in the vault AND mirrored to `/Volumes/COBALT-BACKUP/RESTIC-PASSWORD-README.txt` (0600) — **still needs copying into a password manager off both devices**, because a repository password held only on the machine it backs up is unrecoverable the day that machine dies, and one held only on the backup disk goes with the disk. New this arming: a mandatory `requires_mount` guard — an unplugged SSD fails the run loud naming the mount and the heartbeat's `backup` probe says so, instead of `/Volumes/COBALT-BACKUP` being silently created on the boot disk and the boot disk being backed up to itself, exit 0, green. **B2 STILL OFF**: the vault holds no B2 credential; the leg stays configured and disabled so arming it is a `repo` + `enabled: true` diff. Until it exists there is ONE copy of the corpus, on a disk beside the machine it protects — offsite is the remaining half of the ruling. 22 backup tests, `ops/pending/` is now empty.
- **SSD died 2026-09-06, replaced by HDD — repository re-initialised, B2 offsite still next.** The 500 GB SSD's enclosure or drive stopped enumerating on any machine; it and its one snapshot (`21b03675`) are gone — there was never a second copy, which is exactly the gap B2 exists to close. Replacement is a 1 TB APFS volume, same name/mount (`/Volumes/COBALT-BACKUP`, physical `disk4`), `os.path.ismount` proven True before anything touched it. `restic init` created a fresh repository (`db07ce09bd`) using the SAME `RESTIC_PASSWORD` already in the vault — the password survived because it never lived only on the dead disk — and `RESTIC-PASSWORD-README.txt` was rewritten on the new disk at 0600. `launchctl kickstart com.cobalt.backup` produced snapshot `24f3f36b`: 594 files, 439.6 MB added, ~6s, exit 0. Restore drill repeated against THIS repository: `1 - Trading/1- Daily Notes/2026-09-04.md` restored and diffed byte-identical (sha256 `4369d560…` both sides). Heartbeat beat GREEN after, 11 jobs/8 probes, backup probe 0.1 h old. **B2 is still the remaining half** — a single local copy has now failed once already; offsite is the fix, not a second local disk.
- **Mattermost database split — DONE 2026-09-04** (ruled 09-04, branch `ops/mattermost-split`). Mattermost moved off `cobalt_brain` into its own `mattermost` database; Cobalt keeps `cobalt_brain`, its name, its role and every plist value. `cobalt_brain` is 131 tables → 28, all Cobalt's. The S1-P3 registry's "116 of them Mattermost's" was WRONG — a pristine Mattermost 11.4.0 reference install proves 103, and 13 of the 28 Cobalt tables had been counted as Mattermost's. Dropping "the 116" would have destroyed them.
- **Mattermost Postgres role — DONE 2026-09-05** (ruled 09-05, branch `ops/mattermost-role`, unpushed). Mattermost no longer authenticates as the `cobalt` superuser. Role `mattermost` has LOGIN and nothing else — no superuser/createdb/createrole/replication/bypass-RLS, no role membership — and owns database `mattermost` plus all 103 tables, 5 matviews, 297 indexes and 6 enum types in it; zero `cobalt`-owned objects remain there. `CONNECT` on `cobalt_brain` and `cobalt_dev` revoked from `PUBLIC`, proven by connection attempt (`FATAL: permission denied for database "cobalt_brain"`). Downtime 15 s (22:17:29 → 22:17:44 ET); `--no-deps` kept Postgres from being bounced this time (the db container id was identical before and after, unlike 09-04). Proof: health ×3 OK, all 7 Mattermost connections in `pg_stat_activity` as role `mattermost` and none as `cobalt`, DM landed in `mattermost.posts` (646 → 647), agent boot post landed after `launchctl kickstart` (647 → 648), heartbeat GREEN 11 jobs / 8 probes, 635 tests green. **The catch worth remembering: the ruling's `REASSIGN OWNED BY cobalt TO mattermost` would have handed `cobalt_brain`, `cobalt_dev`, `postgres` and both templates to the new role** — it reassigns *shared* objects regardless of the connected database, proven on throwaways before production was touched; an explicit per-object `ALTER … OWNER TO` loop was substituted. `.env` is now ruled the **bootstrap tier** (only credentials needed before the vault can open); the vault copy is what enrols the password in F19's literal guard (15 → 16 values). **The fence is one-directional**: `cobalt` still reaches `mattermost` because it is a superuser. **Next ruling = demote `cobalt`** — it is the remaining half.
- `sudo crontab -l` (his). **[DONE 2026-09-20 R28: "crontab: no crontab for root" — the root crontab is empty.]** Push of taxonomy/trade-defs-v0_3 (his). rules.yaml + gemini-era-vault-side commit ruling. (Plate audit 2026-09-20: the taxonomy push and `rules.yaml` / gemini-era commit `fdf79d0` are DONE by record — `his-plate-audit-2026-09-20.md` §0.)
- Taxonomy v0.8 consolidation — at S2-P2.
- Spike leftovers: TV webhook extended hours + alert-slot cap — post-MVP SHOULD, untouched here.
