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
**Timebox:** 9 build weeks 09-08 → 11-06, acceptance run 11-09 → 11-13.
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
| S2 Radar 19a | 09-21 → 10-02 (2) | F2 · F8 · F10 · F3 · Radar panel (§5) · F12 · F13 | selection quality, awareness; expectancy corpus starts on the right population |
| S3 Exits + DRC on radar cards | 10-05 → 10-16 (2) | F11 · F22 · F14 · F15 | exit efficiency, adherence measurement, expectancy |
| S4 19b strike alert — CAPPED | 10-19 → 10-23 (1) | F9 | bandwidth (+ adherence under fire) |
| S5 Prep + platform + playbook | 10-26 → 11-06 (2) | F4 · F5 · F20 · F21 · F23 · F16 close | prep, bandwidth |
| Acceptance | 11-09 → 11-13 | §12: every MUST on live vault + DB, 5 days green, ≥3 live mornings | — |

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

## S2 — Radar 19a (09-21 → 10-02)

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
- S2-P1 · Opus 5 · fresh · F2 pool job + membership history · Finviz bar poller at working TF (reuses the spike's client path) · account-mode tag.
- S2-P2 · Opus 5 · fresh · F8 precondition evaluator, Rubberband first, then the other five · F10 dot scoring + ladder sizing + tap recording · taxonomy v0.8 bump.
- S2-P3 · Sonnet · fresh · Radar panel front-end (no write path) — ladder, strips, badges, tap strip, phone frame · F3 rank + WHY display.
- S2-P4 · Opus 5 · fresh · F3 pick-vs-rank rows · F12 nightly replay + counterfactual R · F13 top-N archive + benchmark + miss line · S2 smoke.
- Parallel, non-write: Agent SDK spike (Sonnet) — two-session test (subscription CoS + local worker via LiteLLM proxy), HITL hooks question — so S5's F20 does not start cold.

**Rulings/inputs owed before S3:** DRC template review session (Dejan +
Claude, his docx + SMB template → live Templater template) — before S3-P3.
Stop-override authority (mock #6) — before S3-P2.

---

## S3 — Exits + DRC on radar cards (10-05 → 10-16)

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

---

## S4 — 19b trigger detection + strike alert (10-19 → 10-23, ONE WEEK, CAPPED)

**Preconditions (must be true on 10-19 or the sprint slips, not stretches):**
trading PC on Tailscale (his) · `.htk` hotkey labels checked against
`{DAYMODE}-{KEY}-{SIDE}` (his, mock #3) · F8 live since S2.

| Feature | Charter acceptance (test) | Week plan |
|---|---|---|
| **F9 19b, focus scale** | Alert on the panel ≤5 s after bar close, premarket + RTH; if Finviz throttles at 3 s, criterion re-rules to what 10 s delivers (~8 s). | Day 1: re-measure at 2–3 s cadence, premarket + RTH, ≤5 names (spike script pattern, measurement only) → criterion fixed. Days 2–3: price-cross detector with the card's confirmation policy on ≤5 ARMED names; TRIGGERED transition + MISSED on unarmed. Days 4–5: SSE push → pinned browser tab on the PC over Tailscale, browser notification + sound, three numbers + hotkey; Mattermost DM phone fallback. Friday: whatever is proven ships; remainder → post-MVP lane (toast listener, other trigger types). |

**Code prompts owed:** S4-P1 · Opus 5 · fresh · re-measure + detector;
S4-P2 · Opus 5 · fresh · SSE delivery + notification + fallback + week report.

---

## S5 — Prep + platform + playbook (10-26 → 11-06)

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

## Acceptance week (11-09 → 11-13) — Charter §12

Every §3 MUST passes its test on the live vault + live DB, five consecutive
trading days, heartbeat green, card used in ≥3 live mornings. Then the
post-MVP lane (§11) fights for slots at sprint boundaries.

## Carried open items (owner)

- Trading PC joins Tailscale (his) — S4 precondition; S1-P1 reports status.
- `.htk` label check (his) — S4 precondition.
- `.htk` attestation is self-report until S3 — the soft check ships in S1 and stands through S2; F11 is where a fill is first recorded against the attested sheet. Nothing reads DAS before then, and nothing is planned to (ruled 09-04).
- Health thresholds (#8) + detail-column order (#11) — before S2-P3.
- DRC template review session (Dejan + Claude) — before S3-P3.
- Stop-override authority (#6) — before S3-P2.
- Trade-count goal band value (his, Rules Engine session) — placeholder in S1.
- Hand-logged legs in the DRC chat continue until F11 lands (S3).
- Vault backup restic → B2 + SSD (gated, before Tahoe) — **SSD LEG ARMED 2026-09-05; B2 PENDING** (branch `ops/backup-arm`). `com.cobalt.backup` is loaded and runs 21:40 every day, all week, after the archiver's 20:30. First real snapshot `21b03675`: 551 files, 422.7 MiB, 439.3 MB added, 3m40s, exit 0 — the vault plus a fresh 360 MB `cobalt_brain` dump, to a 500 GB APFS volume at `/Volumes/COBALT-BACKUP` (physical `disk4`). **Restore proven against THIS repository, not a throwaway**: one daily note restored byte-identical to live (15,548 bytes, 396 lines, same sha256), and the dump reloaded into a scratch database matching `cobalt_brain` on all 28 tables, 4,792,389 rows, and md5 `4a80bf6d…` over 4.79M ordered `bars` rows; the scratch database is gone. `RESTIC_PASSWORD` is in the vault AND mirrored to `/Volumes/COBALT-BACKUP/RESTIC-PASSWORD-README.txt` (0600) — **still needs copying into a password manager off both devices**, because a repository password held only on the machine it backs up is unrecoverable the day that machine dies, and one held only on the backup disk goes with the disk. New this arming: a mandatory `requires_mount` guard — an unplugged SSD fails the run loud naming the mount and the heartbeat's `backup` probe says so, instead of `/Volumes/COBALT-BACKUP` being silently created on the boot disk and the boot disk being backed up to itself, exit 0, green. **B2 STILL OFF**: the vault holds no B2 credential; the leg stays configured and disabled so arming it is a `repo` + `enabled: true` diff. Until it exists there is ONE copy of the corpus, on a disk beside the machine it protects — offsite is the remaining half of the ruling. 22 backup tests, `ops/pending/` is now empty.
- **SSD died 2026-09-06, replaced by HDD — repository re-initialised, B2 offsite still next.** The 500 GB SSD's enclosure or drive stopped enumerating on any machine; it and its one snapshot (`21b03675`) are gone — there was never a second copy, which is exactly the gap B2 exists to close. Replacement is a 1 TB APFS volume, same name/mount (`/Volumes/COBALT-BACKUP`, physical `disk4`), `os.path.ismount` proven True before anything touched it. `restic init` created a fresh repository (`db07ce09bd`) using the SAME `RESTIC_PASSWORD` already in the vault — the password survived because it never lived only on the dead disk — and `RESTIC-PASSWORD-README.txt` was rewritten on the new disk at 0600. `launchctl kickstart com.cobalt.backup` produced snapshot `24f3f36b`: 594 files, 439.6 MB added, ~6s, exit 0. Restore drill repeated against THIS repository: `1 - Trading/1- Daily Notes/2026-09-04.md` restored and diffed byte-identical (sha256 `4369d560…` both sides). Heartbeat beat GREEN after, 11 jobs/8 probes, backup probe 0.1 h old. **B2 is still the remaining half** — a single local copy has now failed once already; offsite is the fix, not a second local disk.
- **Mattermost database split — DONE 2026-09-04** (ruled 09-04, branch `ops/mattermost-split`). Mattermost moved off `cobalt_brain` into its own `mattermost` database; Cobalt keeps `cobalt_brain`, its name, its role and every plist value. `cobalt_brain` is 131 tables → 28, all Cobalt's. The S1-P3 registry's "116 of them Mattermost's" was WRONG — a pristine Mattermost 11.4.0 reference install proves 103, and 13 of the 28 Cobalt tables had been counted as Mattermost's. Dropping "the 116" would have destroyed them.
- **Mattermost Postgres role — DONE 2026-09-05** (ruled 09-05, branch `ops/mattermost-role`, unpushed). Mattermost no longer authenticates as the `cobalt` superuser. Role `mattermost` has LOGIN and nothing else — no superuser/createdb/createrole/replication/bypass-RLS, no role membership — and owns database `mattermost` plus all 103 tables, 5 matviews, 297 indexes and 6 enum types in it; zero `cobalt`-owned objects remain there. `CONNECT` on `cobalt_brain` and `cobalt_dev` revoked from `PUBLIC`, proven by connection attempt (`FATAL: permission denied for database "cobalt_brain"`). Downtime 15 s (22:17:29 → 22:17:44 ET); `--no-deps` kept Postgres from being bounced this time (the db container id was identical before and after, unlike 09-04). Proof: health ×3 OK, all 7 Mattermost connections in `pg_stat_activity` as role `mattermost` and none as `cobalt`, DM landed in `mattermost.posts` (646 → 647), agent boot post landed after `launchctl kickstart` (647 → 648), heartbeat GREEN 11 jobs / 8 probes, 635 tests green. **The catch worth remembering: the ruling's `REASSIGN OWNED BY cobalt TO mattermost` would have handed `cobalt_brain`, `cobalt_dev`, `postgres` and both templates to the new role** — it reassigns *shared* objects regardless of the connected database, proven on throwaways before production was touched; an explicit per-object `ALTER … OWNER TO` loop was substituted. `.env` is now ruled the **bootstrap tier** (only credentials needed before the vault can open); the vault copy is what enrols the password in F19's literal guard (15 → 16 values). **The fence is one-directional**: `cobalt` still reaches `mattermost` because it is a superuser. **Next ruling = demote `cobalt`** — it is the remaining half.
- `sudo crontab -l` (his). Push of taxonomy/trade-defs-v0_3 (his). rules.yaml + gemini-era-vault-side commit ruling.
- Taxonomy v0.8 consolidation — at S2-P2.
- Spike leftovers: TV webhook extended hours + alert-slot cap — post-MVP SHOULD, untouched here.
