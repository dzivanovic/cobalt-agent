# BACKLOG.md — Cobalt kanban + backlog

Source of truth for work state. Derived from docs/20 - Assessment/TRIAGE.md
(ruled 2026-08-22). Dispositions live THERE; this board only tracks
sequencing and progress. Sprint ladder below the pre-beta lane is NOT
locked — the MVP Charter re-derives it.

Update rule (CLAUDE.md): keep this board current as you work; move cards,
don't duplicate them.

---

## INCIDENT LOG

- **2026-08-25 — prod agent down, misdiagnosed as strangler-boundary
  leak.** Actual root cause: `mattermost` container's baked
  `MM_SQLSETTINGS_DATASOURCE` env var (docker-compose substitutes
  `${POSTGRES_PASSWORD}` from `.env` at container CREATE time) went
  stale after the Postgres password rotation on 2026-08-24 — the
  container was never recreated, so it kept the old password, degraded
  to `Database Status: UNHEALTHY`, and the agent's Mattermost login
  failed ("Invalid or expired session"). Coincided in time with the
  ASET/role-pack commits but was unrelated — confirmed no import
  crosses src/cobalt_agent/ ↔ src/cobalt/, and the old config loader's
  glob (`configs/*.yaml`, non-recursive) never reaches `configs/dev/`.
  Fix: `docker compose --profile core up -d --no-deps mattermost`
  (recreate only, re-substitutes current `.env`) — no code or config
  moved. Also killed an orphaned pre-incident agent process (untracked
  by the PID file, running since 2026-08-21) before the clean restart.
  Standing rule from this: recreate `mattermost` (and any other service
  reading `${POSTGRES_PASSWORD}`-family vars) after every Postgres
  password rotation — `docker restart` alone does not re-read `.env`.

- **2026-09-03 — morning prefill silent, root cause: launchd's
  posix_spawn does not resolve a bare program name via the job's own
  EnvironmentVariables PATH.** `com.cobalt.prefill-daily.plist` fired on
  schedule (05:15) and `com.cobalt.prefill-drc.plist` the evening before
  (09-02 15:40) — both loaded, both exited immediately with `78:
  EX_CONFIG` and ZERO stdout/stderr, no alert. Confirmed by an isolated
  diagnostic LaunchAgent: bare `uv` as `ProgramArguments[0]` reproduces
  the exact signature (exit 78, empty logs); an absolute path exits 0.
  The 08-31 "fix" (see the slice-2 entry below) that replaced the
  plists' wrong hardcoded `/opt/homebrew/bin/uv` with a bare `uv`
  (modeled on `ops/start_aset.sh`'s pattern) was never exercised
  end-to-end — the plists sat uninstalled from 08-31 until this
  session — so the fix's own flaw went undetected: `start_aset.sh`'s
  bare `uv` works because bash's own shebang does the PATH search
  before `exec`ing it; a bare name directly in a plist's
  `ProgramArguments` has no shell in front of it, and launchd's
  posix_spawn does not reliably do that search itself.
  `com.cobalt.archiver.plist` carried the ORIGINAL wrong-hardcoded-path
  bug (`/opt/homebrew/bin/uv` doesn't exist on this machine) and was
  also not loaded at all. Fix: all three now use the absolute
  `/Users/cobalt/.local/bin/uv`, installed and verified (see
  `docs/40 - DevDocs` / ops session recap for the day). **Standing
  rule:** any `ops/*.plist` `ProgramArguments[0]` that invokes a binary
  directly (not through a wrapper script's own shebang) must be an
  ABSOLUTE path — a bare name is a launchd footgun regardless of what
  `EnvironmentVariables.PATH` says. See the heartbeat-probe follow-up
  below.

## NOW (in build)

- **STATUS 2026-09-24, S3 day 1 (close hub `close-0924`; ladder: `SPRINT-LADDER-v0_1.md` S3 `### Status 2026-09-24`; sprint S3 stop 2026-10-07 — ON TIME).** Production = NINE deploys since 09-19: the previous eight + `deploy-2026-09-24` (`a2d320b8`, the setups seven + Second Chance fix + mover-bars fix; the first run `FAILED: 4.7 (b)` at 11:40 and rolled back, the re-land landed 13:27 ET, residents down 114 s); pushed 09-24 R74 (`49018abd..de48c19b` + tag). His four assumed rows are in `Assumed Defaults.md` (write_ids 3579 / 3581) and loaded (`cobalt taxonomy load` 15:43:35). Tonight's smoke: AMBER 36 / 39 — the 21:10 replay FAILED at 21:40 (`DeadlineExceeded` at the `line` step; ticket below); K9.4 fix shows, K17 gone. BUILT-NOT-MERGED: stale-score r2 `358f1f75` (CHECKED), handicap H1 r2 `27df13f1` (check `45` DONE: opus FIX with 2 HOLDS, grok BUILD STANDS, ready 1 of 2 — an L75 fix round is owed), voice V1 fix r2 `d319e4f3` (round-3 check `55` queued), DRC D1 (BUILT + CHECKED) + K1 fix r1 `40cf173e` (check `49` queued; K2 drafted). PENDING SITTINGS unheld: Second Chance REDESIGN first, then VWAP Continuation (R13 / R14). Status only — scope and order change by his ruling alone.
- **OFF-LADDER, 09-24 (each carries its ruling; full detail in `SPRINT-LADDER-v0_1.md` S3 `### Status 2026-09-24` and `reports/close-2026-09-24.md`):** setups seven + Second Chance fix DONE-LIVE (09-23 R83; 09-24 R39 / R45) · mover-bars fix DONE-LIVE (R7) · assumed rows written + taxonomy load (R55 / R58) · GATE EARLY → L68 and L76 new, L67 / L62 amended (R9 / R10 / R12 / R17 / R19) · DRC overnight-position lane: proposal → tribunal (2 rounds) → v3, R51 "A" / R52 "b", K1 + fix r1 BUILT (R22) · voice V1 fix rounds 1–2 BUILT, round-3 check queued · stale-score r2 + H1 r2 BUILT-NOT-MERGED (R84 / R89) · sitting packets drafted (R14).
- (superseded by the two bullets above — kept for its detail) **STATUS 2026-09-24 (close hub `close-0923`, one close for 09-22 + 09-23; ladder: `SPRINT-LADDER-v0_1.md` `### Status 2026-09-24`; sprint S2 stop 2026-09-23 — LATE).** Production = EIGHT deploys since 09-19: the three 2026-09-19 + three 2026-09-21 + `deploy-2026-09-22` (`d2d82e70`, 12:26 ET, stale marker + ops 0921, residents down 93 s) + `deploy-2026-09-23` (`4e4577c3`, 16:56 ET, the S2 smoke fix, ONE branch, residents down 17 s); pushed 09-22 R29 (`5b208a0..be2c91e` + tag) and 09-23 R92 (`origin/main` = `49018abd`). **S2 does NOT close:** the one live day is banked (09-21 R13), but the smoke night is AMBER 32 / 34 on 09-23 (`smoke green for S2: no`) — K9.4 (one stored loser has no bars) and K17 (five stray `docs/_inflight/` files). The replay failed 09-21 and 09-22, ran clean 09-23 21:10 ET. The seven-setups ladder change is BUILT + CHECKED (`setups/seven-0921` `c60a7f00`) and deploys 09-24 on his DONE TRADING (09-23 R83); the house read of its deploy prompt was IN PROGRESS at close. S3 opens 09-24. Status only — scope and order change by his ruling alone.
- **OFF-LADDER, 09-22 and 09-23 (each carries its ruling; full detail in `SPRINT-LADDER-v0_1.md` `### Status 2026-09-24` and `reports/close-2026-09-23.md`):** LAWS sitting held + applied (09-22 R80–R88; L75 new, L12 retired) · stale marker + ops 0921 DONE-LIVE · S2 smoke fix DONE-LIVE · stale-score design CLOSED, build `46` stopped mid-STEP-2 · float handicap design FINAL, H1 not started · S3 exits design FINAL · DRC design derived, D1 BUILT (14 HOLDS, fix round owed), D2–D5 wait · voice v3 FINAL approved, V1 BUILT, its check FAILED on packet size · JEV (typesafe.ai) trial BUILT, one keyed probe run, checks A r1–r3 · routing tribunal DONE (owner items 20–37 ruled), X5 PAUSED · dev-DB repaired (`head: 0011`) · ASET attest forensics DONE (rows below) · Opus 5.5 seat rulings (09-22 R32 / R36 / R76 / R109); checker seats changed 09-23 R95–R97 (L67 amendment PROPOSED in the close).
- **OFF-LADDER, 09-21 (each carries its ruling; full detail in `SPRINT-LADDER-v0_1.md` `### Status 2026-09-22` and `reports/close-2026-09-21.md`):** bars chunks 1a + 2 round 3 DONE, both CHECKED (BUILT-NOT-MERGED, nothing before WED 09-23) · float handicap proposed + Fable-seat ruled, three-house round 1 could not run (Anthropic incident), TUE · stale marker BUILT (`s2/stale-marker-0921`), check `68` TUE · stale score proposed + Fable seat approved, tribunal TUE · typesafe classifier research DONE, trial approved (his hand for funding) · ops 6a BUILT → checked → fix → checked → fix round 3 (the last) BUILT, check `81` TUE; 6b re-drafted as a fresh-host restore drill, waits on restic rotation · S3 exits proposed + Fable seat approved, tribunal TUE · DRC sitting packet READY (his sitting, he names the time) · restic rotation still NOT DONE (his hand, exposed since 09-11).
- **OFF-LADDER, 09-20 (each carries its ruling):**
  - **Bars-lifecycle tribunal + build chunks** — 09-18 R17 · 09-19 R10/R15 · 09-20 R9 (i1 only), R13, R19–R22 (twelve owner rulings), R25. Tribunal DONE (3 rounds → `docs/30 - Design/BARS-LIFECYCLE-FINAL-2026-09-20.md`); chunk E DONE + checked 3 of 3 (`bars/chunk-e-0920` `982d958`); chunk 1a BUILT, fix 1 + 1b BUILT (`793f452`, `1404f23`), round 2 checked 2 of 3 (gemini HARNESS), 12 of 13 FIX rows closed, X9/X14 naming reconciliation open → round 3 = a CHECK by three houses (`bars/chunk-1a-0920` `6961ee0`); chunk 2 BUILT, fix BUILT (`d768674`), round 2 checked 3 of 3 split 2–1, 4 of 5 FIX rows closed → round-3 fix next (`bars/chunk-2-0920` `1351da6`). BUILT-NOT-MERGED; nothing deploys before WED 09-23; all `requires_db` first runs on `cobalt_dev` and the L68 stacked gate of 1a + 2 still ahead; chunk 4's drafter carries R45 and the `--proof-only --full` gap. His: O1 (unreadable first bounds read aborts a cycle on a plain table — A/B asked 09-20 21:14 ET, unanswered, blocks nothing), O2–O4, O6 of `reports/bars-2-fix-draft-2026-09-20.md`.
  - **Laws audit (R10) and memory research (R11)** — DONE registers (`reports/laws-audit-2026-09-20.md`, `docs/30 - Design/memory-history-2026-09-20.md`); the two sittings are in PENDING SITTINGS below.
  - **His-plate audit (R26)** — DONE (`reports/his-plate-audit-2026-09-20.md`).
  - **Restic password rotation** — NOT DONE (R41 "no"); his hand; step list drafted Mon 09-21 with `ops-0921` (R42). Entry checklist item 2 below stays OPEN.
  - Carried from 09-19, unchanged: append-only archiver DONE-LIVE in `upsert`, ONE shadow night Mon 20:30 ET (R35; `shadow_compare` on, 09-20 R29), `append` switch NOT STARTED · ops 0919 DONE-LIVE · **R34 C** (stagger the pool cadences) NOT STARTED · `cmd_migrate` must refuse `--allow-prod` unless `COBALT_ENV=production` · `31-packet` yaml copies and `2026-09-20/16-packet/` stay untracked (R40: no settings packet yaml goes to git).
  - **`ops-0921`** (Mon 09-21, Opus-hub drafted, design-free): restic step list + key store into restic's include set + restore proof, the stale `cli.md:113-124` paragraph (the desk's citation names no path; `docs/40 - DevDocs/cobalt/db_migrations/cli.md` is the only DevDoc `cli.md` long enough to have those lines — the drafter confirms), `UNATTENDED-LAUNCH.md` lines "never wrap a command to read its exit status" and `--disallowedTools Bash(git push*)` on every `~/cobalt` hub, the eight stale `claude agents` registry rows, the empty "Cards apply" herdr tab, the four build MINORs (G-A1, G-A2, H1, H2 — H2's tail-anchored contiguity pins will redden on `0012`), `CLAUDE.md:95-96`.

- **S2-P4: picks, value column, nightly replay + counterfactual R, movers benchmark and miss line, `cobalt smoke s2` (2026-09-17). DONE-LIVE 2026-09-19 (deploy 2, `5b58b7b`, tag `deploy-2026-09-19b`); was BUILD COMPLETE (chunks A–C), HUB VERIFICATION PENDING.**
  - Plan: `docs/40 - DevDocs/plans/plan-s2-p4-2026-09-15.md`. Decision record: ADR-0010.
  - **Builder reports:** `docs/40 - DevDocs/reports/s2-p4-build-opus-{A,B,C}-2026-09-17.md`.
  - **Built:**
    - migrations 0008/0009;
    - the `rank_metric`/`rank_value` column;
    - F3 `"user".picks` in the fill transaction;
    - `com.cobalt.replay` at 21:05 Mon–Fri: movers + i1 archive, card misses with cf-R and immutable receipts, the `drc-misses/miss_line` unit;
    - the shared L53 total-demand gate;
    - `cobalt smoke s2`, read-only, K1–K18 from `configs/cobalt/smoke/s2.yaml`.
  - **Hub owes:**
    - the `requires_db`/`requires_vault` tests on cobalt_dev;
    - `cobalt validate`;
    - `cobalt jobs restarts main..HEAD`;
    - the dev replay end-to-end;
    - the leak scan and the commit (L46).
  - **Deploy gates (ESCALATE):**
    - the L53 gate refuses the archiver and replay under the unchanged `finviz_max_rpm` ceiling (Dejan's ruling);
    - P2 formation binding;
    - `radar.benchmark` values;
    - `trade_count_band` values.
  - **S2 close:** `cobalt smoke s2 --prod --cutoff <P4 D1 instant>` ≥ 09-22 evening. GREEN = S2 done.

- **S2-P2 — Radar cards: F8 precondition evaluator + F10 dots / ladder / taps (2026-09-16): DONE-LIVE — shipped dark in deploy 1 (`2893a7f`, 2026-09-19 08:25 ET), switched ON 12:30:01 ET (R20, `cards-golive-2026-09-19.md`), first render Mon 2026-09-21 04:00 ET; was BUILD CHUNKS A–C COMPLETE, HUB VERIFICATION PENDING.**
  Plan `docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md` (R1–R11), ADR-0009.
  Branch `sprint-2/cards`. Chunk A (`ca184c8`): migrations 0006/0007, the §10.5 predicate AST, anatomy detectors. Chunk B (`17eb35f`): S5 evaluate stage, dots/scoring, snap-down key taps, health pills. Chunk C (uncommitted, builder report `docs/40 - DevDocs/reports/s2-p2-build-opus-C-2026-09-16.md`): `/radar` ladder wired to `"user".radar_cards_v` with badges, hollow shadow dots, the 1–10 tap strip, key row and promote; explicit POST allowlist + GET sentinels; taxonomy v0.8 (schema 0.5 behind the 0.4 loader gate, `taxonomy catalyst-review`/`catalyst-apply`); `cards trail-fit-draft`; `cards shadow-report`; `radar audit-export`.
  Owed before merge (hub): `requires_db` + `requires_vault` tests, `cobalt db migrate` on cobalt_dev (0007 changed again in chunk C), `cobalt validate`, `cobalt jobs restarts main..HEAD`, dev replay, audit bundle staging. Ships dark (R9). Carried: curve tribunal (S3), catalyst markup (Dejan, D3), alignment default ruling (plan §8 item 4), `panel-cards.real-shape.json` cut (hub).

- **S2-P3 — Radar panel (2026-09-15): DONE-LIVE — merged 09-15 (`ebb1231`, tag `deploy-2026-09-15`; `sprint-2/radar-panel` has no commit outside main); §5 acceptance (2–3 live mornings beside DAS) 0 banked, first Mon 2026-09-21; was BUILD COMPLETE, HUB VERIFICATION PENDING.**
  Read-only `GET /radar` pool view + card-ladder shell and
  `GET /api/radar/pool?since=` refresh path built in the ASET process.
  Store read layer, strict Pydantic views, fail-loud source/freshness
  handling, responsive pure renderers, offline fixture contract tests, and
  DevDocs are complete. Focused offline suite: 88 passed, 1 skipped
  (`requires_db`, hub-owned). Full repository suite is blocked during
  collection by the pre-existing old-tree `FinvizStockData` import; hub must
  run the DB test and verify/commit the artifact.

- **Pre-beta slice 1 — ASET semi-auto sheet** (days)
  Deterministic sizing engine in src/cobalt/: daily stop = account ÷ 50;
  grade→risk A+ 80% / A 30% / B 15% / C 5% / D-SAW 0%; entry/stop/direction
  → risk $ + shares. Grade and stops always Dejan's input; prefill last
  price via FinvizApiClient path. Every sizing persisted to Postgres
  (cobalt_dev; table may be reshaped by data-model ADR). Surface: simplest
  working local form (trade-reporter Flask pattern). Fail-loud. Tests +
  smoke. Spec: docs/90 - References/aset_daily_position_sizer.html +
  Daily_Stop_Model_Card.pdf. Gate: stop and show Dejan the working sheet.
  STATUS 2026-08-25: iteration 2 live (broker hard cap $430 enforced,
  auto-prefill on ticker tab-out, entry prepopulation, grade default B,
  LONG/SHORT toggle, append-only Save-to-Daily-Note with git-ignore
  safety gate). Awaiting Dejan review.
  STATUS 2026-08-25 (cont.): server bind is config-driven
  (configs/dev/aset*.yaml server.bind: loopback|lan); Dejan's local
  config now runs "lan" so the Windows trading PC (same home network,
  not Tailscale) can reach it — reachable URL(s) print on startup.
  Prefill token issue resolved (Finviz token in the vault now valid;
  prefill confirmed live during the 2026-08-26 smoke test).
  STATUS 2026-08-26 — vault-path migration: real Obsidian vault is now
  /Users/cobalt/Vault/Think (config: configs/dev/vault.yaml, resolver:
  src/cobalt/vault.py — TRIAGE 2.6's ONE resolver, new-core only, old
  tree's four-way ambiguity untouched). Save-to-Daily-Note now targets
  "1 - Trading/1- Daily Notes/YYYY-MM-DD.md" under that root; the
  git-check-ignore safety gate is retired — replaced by an "outside the
  repo working tree" check, which is now the actual safety property
  (the vault is genuinely outside the repo, not just gitignored inside
  it). Stub-with-banner on a missing note added. Smoke-tested end to end
  into the real vault (card landed in today's real daily note).
  Old playground-vault writes (docs/0 - Inbox) retired, left as-is —
  **flagged, not migrated**: two test ```aset cards from prior smoke
  tests sit in docs/0 - Inbox/2026-08-25.md (both ticker MRNA, fake
  sizing data) — not real trades, not auto-migrated into the real vault
  to avoid injecting synthetic entries into Dejan's real trading record.
  Dejan: delete, ignore, or say if you want them ported by hand.
  Backlogged follow-on (do not build yet): ticker field autocompletes
  from the daily in-play list once that pipeline exists; non-list
  tickers show an inline "not in today's in-play list" note (no popup),
  still allowed. Access token for the LAN-bound sheet (currently
  unauthenticated by design/acceptance, see server.bind config comments).
  STATUS 2026-08-27 — iteration 4, sizing-model replacement (ruled by
  Dejan): daily-stop x grade-percentage model RETIRED — replaced by
  fixed-dollar-per-grade sheet mode (FULL/HALF), mirroring Dejan's DAS
  hotkey files exactly (configs/cobalt/aset.yaml: full A 135/B 60, half
  A 70/B 30). Grade selector now offers only A and B (the only
  sheet-mode-tradeable grades); C/D still fail loud server-side as
  "not tradeable" if they ever reach compute_sizing, rather than
  computing a meaningless size — dropdown just never offers them.
  "Compute & persist" now ALSO appends the card to the daily note in the
  same action (the separate Save button and POST /note route are gone —
  a card that isn't in the journal didn't happen). A new "actual fill"
  field recomputes shares at the real fill price (same grade dollars,
  same stop) and appends a linked FILL UPDATE block to the note
  (>=25% distance change vs. the planned card shows a visible, non-popup
  "stop may no longer be structural" warning) — both the original card
  and every fill update stay in the audit trail. broker_hard_stop and
  daily_stop_default retired from AsetConfig (account_size kept for the
  future 1%-of-account computed mode). New migration
  0002_aset_sizings_sheet_mode.sql (sheet_mode added, daily_stop/risk_pct
  dropped); AsetStore.ensure_schema() generalized to run every
  migrations/*.sql file in order (strips full-line -- comments before
  splitting on ';' — psycopg executes one statement at a time). All
  tests updated and green (engine/config/daily_note/store, incl. the
  live Postgres roundtrip). Live-smoke-tested end to end against the
  real vault: full-mode B card computed, persisted (id 73), and
  auto-appended; a 40c-away fill recomputed cleanly with no warning
  (12.75% distance change); a second, larger fill correctly triggered
  the structural warning (134.90% distance change) and appended its own
  linked block; HALF-mode server-side dollar switch verified (B -> $30,
  correct per config) via direct POST. One piece NOT live-browser
  verified: physically clicking the FULL/HALF toggle button in this
  session's browser-automation tool — click delivery failed to reach
  the button (elementFromPoint confirms correct hit-testing; the same
  failure reproduces on the pre-existing LONG/SHORT toggle in a fresh
  tab, so it's a session/tool-level issue, not new-code regression);
  setMode()'s client logic was verified directly (correct $ hint
  swap) and the server-side compute path was verified by direct POST.
  Dejan: please do one real click of the FULL/HALF toggle by hand to
  close this out. Leftover: a TESTHALF row (id present, ticker
  TESTHALF) landed in cobalt_dev and one TESTHALF card landed in
  today's real daily note from that verification POST — flagged, not
  deleted (same policy as the earlier SMOKETEST/TESTARCH leftovers).
  Old percentage-model code (GRADE_RISK_PCT, enforce_broker_cap,
  daily_stop_from_account, temp_prefill_daily_stop) deleted outright,
  not deprecated in place — one-path rule. DevDocs for the seven
  touched/new files regenerated and committed (b032691).
  STATUS 2026-08-27 (cont.) — config completion, same-day follow-up
  (ruled by Dejan): configs/cobalt/aset.yaml's grade ladder extended to
  the FULL truth — A_plus/A/B/C/D dollar figures per sheet mode (full A+
  345/A 135/B 60/C 21/D 0, half A+ 170/A 70/B 30/C 11/D 0; A/B unchanged,
  match the .htk files; A+/C derived from the canonical ASET percentage
  map at current bases; D always $0, enforced by a Pydantic field
  validator, not just convention). UI/compute availability split into a
  separate enabled_grades: [A, B] field. TRADEABLE_GRADES (the hardcoded
  models.py constant) is gone — engine.compute_sizing now takes
  enabled_grades as an explicit argument, so enabling a grade later is a
  config edit only; a new test (test_enabled_grades_is_config_driven_not_hardcoded)
  proves this by swapping which grades are enabled and watching the
  refusal follow the config, not the code. Grade dropdown now lists all
  five grades; A+/C/D render as disabled <option>s with a suffixed label
  ("reserved" / "no trade (SAW)") — greyed, structurally unselectable via
  the native dropdown, and refused server-side too if bypassed by a
  direct POST. All tests green (incl. live Postgres roundtrip). Live-
  smoke-tested: full-mode B computed unchanged ($60 budget, 60 shares);
  direct POSTs for C, A+, and D all correctly refused ("not enabled ...
  no trade (SAW)") and wrote nothing to Postgres or the daily note.
  DevDocs regenerated for models/engine/config/web.py + their tests.

- **Pre-beta slice 2 — DRC & Daily prefill engine** (src/cobalt/prefill/)
  Templates-as-config: Daily.md + DRC.md ported to Jinja
  (configs/cobalt/templates/*.md.j2), structure/section names verbatim,
  Templater `{{ }}` prompts replaced by prefilled fields. Guardian rule
  set unified into configs/cobalt/rules.yaml (the vault's own Rules.md
  "THE 12 RULES" + Daily.md's uncovered lines, quoted verbatim) — the
  single source for the morning rules block, the rule-adherence
  checklist, and (later) Guardian's own enforcement. Morning Daily Note
  (`uv run prefill daily`, scheduled 05:15 ET weekdays): SPY/QQQ/IWM via
  the confirmed Finviz /export/screener v=111; VIX/BTC render "n/a
  (manual)" loudly (neither is Finviz-servable); today's economic +
  earnings calendar via /export/calendar; day-mode checkbox line;
  rule-adherence checklist. Trade notes: every computed ASET card now
  also creates/updates "1 - Trading/2 - Trades/<Trade-...>.md" (wired
  into web.py's /size handler) so the daily note's dataview table lights
  up — Cobalt owns 5 frontmatter keys only, everything else (strategy,
  RVOL, exit, P&L) stays his, preserved verbatim on any re-run. Evening
  DRC (`uv run prefill drc`, scheduled 15:40 ET): per-ticker
  Catalyst/Set-Up/Trade scaffold from the day's cards (AsetStore.for_date,
  America/New_York boundary), re-entry-rule prompts (#2 needs written
  info, #3+ stands down), excitement-audit question on reversion-tagged
  strategies (configs/cobalt/strategies.yaml, seed list), Risk Parameters
  from today's actual sheet mode. PRINCIPLE enforced throughout:
  create-if-absent from template, else append a fenced, idempotency-
  marker-guarded "Cobalt Prefill" block — existing content never read
  for mutation. 131 tests (incl. Postgres integration for the new
  AsetStore.for_date). STATUS 2026-08-31: shipped + smoke-tested against
  the real vault — today's Daily Note (append path, since Templater had
  already created it), a trade note backfilled from a real card computed
  before the wiring landed, and a DRC draft from today's real cards (no
  Friday 08-28 cards existed in cobalt_dev to use as the spec'd smoke
  case — substituted today's date; flagged, not silently swapped).
  Known gaps, not closed this sprint: DevDocs for the new tests/cobalt/
  test_prefill_*.py files (skipped — src/cobalt/prefill/*.py DevDocs are
  complete); the two new launchd plists are committed to ops/ only, NOT
  installed to ~/Library/LaunchAgents — Dejan's call, needs a real
  05:15/15:40 unattended run to fully verify before relying on it.
  STATUS 2026-08-31 (cont.) — **Slice 2.1 correction**, from Dejan's
  review of the first live note: fill-IN-PLACE inside his actual
  sections replaces the old append-a-block-below-everything design.
  rules.yaml is now GENERATED from the vault's Rules.md (not hand-
  authored) — Rules.md migrated once (each of the 12 lines got exactly
  one trailing Obsidian tag, `#process/#sizing/#time_window/#re_entry/
  #circuit_breaker/#hard_stop`, text otherwise verbatim); Daily.md's old
  Trade Rules list dropped as a source entirely (ruled outdated 08-23,
  the six merged lines are gone); rules.yaml regenerates on every
  prefill run (daily AND drc) and fails loud naming the exact line if a
  tag's missing/wrong/duplicated. The 12 rules render exactly once, as
  a single tagged checkbox list — no more separate "Guardian rules" +
  "Rule adherence" split. Sizing rule (#2) is mode-aware at render time:
  content-detected splice (not tied to rule position) pulls "B = $30
  half / $60 full, A = $70 half / $135 full" straight from ASET's own
  sheet-mode config. Daily template rebuilt with three named Cobalt
  slots (rules/trading/market_calendar), each wrapped in its own
  `<!-- cobalt-slot:NAME -->` marker; an existing note gets per-slot
  editing (marker present → skip; blank/prior-FAILED → fill + mark;
  Dejan's real content already there → skip, report, no mark) instead
  of a bottom-of-file append. Trading table: SPY/QQQ/IWM only, per-row
  fill/skip; VIX/BTC always blank (no more "n/a (manual)" text — same
  table, no second table). A missing anchor (note doesn't match the
  expected shape at all) fails the WHOLE run loud rather than guessing
  an insertion point — edit plan built in memory first, so a failure
  never leaves a half-edited file. Validated against a copy of the real
  08-31 note in a new outside-repo dev vault (~/dev-vault-cobalt, not
  Dejan's real one) — confirmed idempotent, confirmed his hand-filled
  Trading row survives untouched, confirmed the blank Market Calendar
  slot fills correctly even though the rules slot inserts ahead of the
  OLD template's still-present stale Risk Profile prose (that prose
  itself is untouched — only the Jinja template used for fresh notes
  dropped it; Dejan's own Templater file at 5 - Templates/Daily.md was
  NOT touched, so a Templater-created note still carries it until he
  updates that file himself). Both prefill launchd plists' hardcoded
  /opt/homebrew/bin/uv fixed to a bare `uv` (same bug as archiver/
  mainframe, ops/README.md) — still not installed. 19 rewritten daily
  tests + 13 new rules-generator tests + a real DRC test-isolation bug
  found and fixed along the way (drc.py's tests were silently reading
  the REAL vault's Rules.md via an unpatched import binding — now
  patched, and a regression assertion added). 148 non-integration + 5
  integration tests green.

## NEXT (immediate lane, in order)

- **Pre-beta slice 3 — Prebell-lite** (2–3 wks thin, then weekly iteration)
  Regime tiles, catalyst calendar, in-play candidates from existing scanner
  data. Fail-loud from line one.

- [x] **CLOSED 2026-09-15 (ops/2026-09-15 commit) — radar probe flap.** `_pool_row`
      carries `poll_failures` + `failed_stage='bars'` through S2; `BarPoller.poll`
      drops carried records for non-members (IMCC). Trace: reports/cto-2026-09-15.md §1.2.
- [x] **CLOSED 2026-09-15 (ops/2026-09-15 commit) — email channel RETIRED** (ruled 09-14).
      Code removed (git history keeps it: `git show 0ed37f5:src/cobalt/notify/email.py`);
      `cobalt_email_sends` table kept (drop = separate HITL).
- [x] **CLOSED 2026-09-15 (ops/2026-09-15 commit) — L42 O9 classifier rule.** `docs/`
      and root markdown with no reader → `DOCS`, no restart.
- [ ] **TICKET (09-15, ops) — named-secret API has no caller.** `redact/secrets.py`
      `read_secret` / `put_secret` / `secret_names` were used only by the retired
      Gmail consent flow; their tests left with `test_notify_email.py`. Rule: keep
      (re-test) or retire.
- [x] **CLOSED 2026-09-15 (ops/2026-09-15 commit) — TICKET (09-14, Dejan) — Rules.md parser tolerance.** `RulesSourceError`
      on rule #11: `...never break-even.#process` (no space before the tag)
      read as "found none" → `com.cobalt.prefill-drc` RED from the 11:24 edit.
      Dejan fixes the note himself; the parser must accept a tag glued to the
      final punctuation (L45 companion: fix the parser, never the note). Fixture
      = real-shape line; failing test first.
- [ ] **TICKET (09-21, ops fix r3 ESCALATE 5) — `restarts.py:243-244` hard-codes a `watchlists.yaml` `if` that predates the classifier table.** An L3 cleanup (`src/` change, its own restart derivation): fold the special case into the table-driven rule the 09-15 classifier already uses. Not urgent — found while proving `configs/cobalt/backup.yaml`'s reader path.
- [ ] **TICKET (09-21, ops-0921 finding, `SESSION-CLOSE.md` step 5) — the always-loaded-block measure uses `wc -m` (characters), not `wc -c` (bytes).** `SESSION-CLOSE.md` step 5 and `close-2026-09-20.md`'s own measure used `wc -c`; the 4,000-character cap is a character count. Fix the routine's own wording; print both in the close report until fixed.
- [ ] **TICKET (09-21, deploy 21b ESCALATE 1) — the degraded-line deploy took 116 s residents-down vs the <60 s target.** The hub's own per-call overhead between the two bootouts and the merge, not a code defect; input to the stacked-deploy drafter (fewer calls inside the pause).
- [ ] **TICKET (09-21, DRC packet ESCALATE 1) — the miss line's 21:10 ET replay write lands after the 15:41 ET DRC read window.** F14's acceptance and the S3 smoke put the miss line on the same-day 15:41 DRC, but the replay that writes it runs at 21:10 — the smoke as worded cannot pass as written. Input to S3-P3's design and to every close's ladder status until resolved.
- [ ] **TICKET (09-21, S3 exits proposal ESCALATE 1) — a radar-card fill records no price and no shares today** (`aset/web.py:1198-1209`). Until S3-P1 ships the fill path, live mornings need his hand-logged fill price + shares in the DRC chat, the same as legs.
- [ ] **TICKET (09-23 R4 (a), 09-22 R130) — the setups test-cutter accepts an odd time spelling instead of failing loud.** `tests/fixtures/radar/_cut_setups_fixtures.py:38` and `:59-61`: an odd time spelling passes through unchanged instead of `SystemExit` (the `[R4] F4` fail-loud clause; the committed cut is unaffected, 956/956). His words: "Everything waiting for me is approved." — SHIP with it, BACKLOG the fix (desk recommendation: the cutter is a dev tool, not a production path). Setups r4 check `SETUPS CHECK R4 DONE … defects that HOLD: 1`.
- [ ] **TICKET (09-23 R31) — the ASET attest trio, carried FORWARD with the day-mode logic, NOT fixed on the sheet (09-23 R30).** From `ASET ATTEST FORENSICS DONE · cause: BUG · fix size: small` (`aset-attest-forensics-2026-09-23.md`): (1) refusals are SILENT — only `/size`'s `SheetMismatch` logs (`web.py:987-988`); `/size` `:990`, `:992` and every `/attest` failure (`:1170`, `:1172`) log nothing and `/attest` returns 200 on failure — his 09-22 refusal left no trace; (2) `day_modes` keeps NO attest history (`store.py:152-169` upsert overwrites) — a first vs a second attest cannot be told apart; (3) `GET /` sends no `Cache-Control` — a second device can show a cached pre-attest page that "asks again" (most likely cause of his report; UNPROVEN, no timestamped access log). One build row for the successor lane that retires the sheet (the day-mode / radar-panel path that lives on): loud logging on every refusal, a non-200 on a failed attest, an attest history table, `Cache-Control: no-store` on every page that shows day-mode state — L67-checked with that build. His words 09-23 08:4x: "if this logic is going to go forward into the new process, I need it reviewed and fixed."
- [ ] **TICKET (09-22 R121, his "A") — stop resolvers declare no `tunable_keys`.** Latent: no current definition is affected (all three checkers); built when a new definition needs it. Setups owner item Q1 of `setups-fix-r4-draft-2026-09-22.md`.
- [ ] **TICKET (09-22 midday lesson 1, `topics/cto-desk.md`) — the heartbeat should say AMBER for a carried per-ticker poll record, not RED.** A carried per-ticker bars-poll failure (one thin name, `reason: stale`) stamps `failed_stage='bars'` and the radar probe reads RED for as long as it is carried (`poller.py:67`, `runner.py:376`, `probes.py:106`); it refused the 11:06 daytime deploy preflight 09-22. Rule: AMBER with the ticker named; RED only when the poll itself fails or the pool row is `degraded`. Every deploy prompt since carries a named-baseline exception + a second read ≥100 s later meanwhile.
- [ ] **TICKET (09-22 R80, L63 status note) — the unattended write-path launch-mode scratch test.** `--permission-mode acceptEdits` + `--allowedTools` ASKS on an unlisted Bash (a dialog, L63); `auto` denies silently but L29 forbids auto on a write path. No launch shape is proven to satisfy both. A Sonnet hub proves in a scratch test (L70) what `acceptEdits` does with a listed, an unlisted and a pathspec-shaped Bash vs `auto` + the same list; then `UNATTENDED-LAUNCH.md` and L62's write-path shape are corrected from evidence and the laws packet's L62 recommendation is re-read. Until then `acceptEdits` + the full allowlist is INTERIM PRACTICE. Related 09-23 R104 ops item: why reading the with-DB output trips the auto-mode classifier `[Credential Leakage]`.
- [ ] **TICKET (09-24 R56 / R54 ESC 1) — `taxonomy assumed write --dry-run` refuses on an absent note while `--apply` creates it.** `--dry-run` cannot preview a first write to a note that does not exist (`upsert_unit never creates a note — call create_if_absent() with a template first`), so a deploy prompt's dry-run gate on a first note write FAILS by construction (`deploy-2026-09-24-reland.md` ESCALATE 1; the rows were written by the re-issued STEP-6 `34` on his 09-24 R55 "A", the dev-vault diff standing as the preview). Fix: `--dry-run` must preview the create.
- [ ] **TICKET (09-24 R59, L45 — the parser, never his note) — `cards.expire` falls back to the session close on a bare `4:00`.** After the 15:43 `taxonomy load`, 13 × `cards.expire: falling back to the session close (16:00:00) — preferred_windows_ref 'sheet: 9:59-4:00' is not unambiguously resolvable` (INFO, `cards/expire.py:116`; `_resolve_window_end` refuses a bare `4:00` as ambiguous and lands on the RTH close, the intended deadline). Not a red. Fix: resolve `h:mm-h:mm` ranges whose second time is below the floor as PM when the first is a morning time, or accept `sheet:` refs as the sheet's own window.
- [ ] **TICKET (09-24 R95, RED) — the nightly replay misses its deadline with 13 setups live.** 09-24 21:10 ET run FAILED 21:40:06 (`step line failed — DeadlineExceeded: line: past the deadline 21:35:00 ET`, `replay.err`): movers + cards ended 21:10:37, the formations step then ran ≈ 29.5 min (`scans=235 formations=197 … counts={… 'formed': 3225 …}` vs 09-23's `formations=0`, whole run 2 min 19 s), so the `line` step never ran and the 09-24 miss line was NOT written (smoke K7, K10.1, K10.2). The 09-25 21:10 replay fails the same way unless fixed. Fix drafter prompt `prompts/2026-09-24/56-draft-replay-deadline-fix.md` (→ `57` build → `58` check); an owner-shaped remedy (moving the 21:40 backup, his 09-19 R32 hard edge) is NOT taken by the desk — it reaches him only if no engine-side fix exists.
- [ ] **TICKET (09-24 smoke look ESCALATE 5) — the smoke's K9.1 / K9.4 no longer print `not_archived`.** Evidence now reads `top_n ok` only (09-23: `top_n ok; not_archived ok`); the numbers come from K9.7 / K9.10 / K9.9 / K9.12, so the proof still reads. A smoke-print item, not a defect. (ESCALATE 4 of the same look — `replay.log:109` reading "tonight's 20:30 ET run: done" — is the archiver precondition record, printed in the same shape on 09-22 / 09-23; NOT REAL, R95.)
- [ ] **INFORMATION FOR HIM (09-24 R88 ESC 6 / R89) — the X24 premarket `—` will be frequent.** 629 of 660 premarket ticker-days on `cobalt_dev` miss minutes, so a thin name's premarket stale-score shows `—`. His R38 "A" stands; nothing to rule unless he wants otherwise.
- [ ] **TICKET (09-24 R64 / R94 ESC 5 — the desk's ruling owed) — the voice D6 boundary.** `tests/cobalt/test_radar_panel_cards.py` changed outside prompt `43`'s named list (a necessary consequence of the widget on `/radar`; its revert would turn the `/radar` byte-equality red). R64 ruled it KEPT AS BUILT; the check packet of `55` carries it as a scope row. Formal desk ruling still on the close list.
- [ ] **TICKET (09-24 K2 drafter ESCALATE 1 / R81) — the DRC overnight-lane FINAL document is owed.** No v3 FINAL file exists; `51` / `52` cite `DRC-OVERNIGHT-POSITION-v3-2026-09-24.md` + R51 / R52 directly (the `39` / `40` precedent). Astra reads the FINAL Sat 09-26 06:47. Not a build blocker.
- [ ] **TICKET (09-24 R64 / R41 — design lane, L72) — voice X-E10: a tribunal round 2 on the `av` wheel's bundled `libx264` / `libx265` (FINAL:285).** The FINAL's column routes "an unexpected native / GPL package" to tribunal round 2; the desk's reading (a local-only private tool's dependency wheel is not a ship blocker unless the FINAL's letter names it) is not a ruling. Seats per L67 (Anthropic Opus 5.5 · Grok; Astra from 09-26 06:47). Beside it: the `[F-08]` FINAL wording — `VOICE-v3-FINAL-2026-09-23.md:89` still reads "Unicode casefold, strip"; the built rule (and the desk's R34 reading) is NFKC + casefold + strip + strip `. , ! ?` — a FINAL docs edit, not law.
- [ ] **TICKET (09-24 R54 ESC 10 / R56) — cleanup after the 09-24 deploy event.** Worktrees `stacked-0923`, `setups-c1`, `mover-bars` (deploy and build branches merged into `a2d320b8` / superseded), the rows folder, scratch; the empty "DEPLOY" herdr tab `w2:t8C` (closable only by his hand); eleven pid-less `working` rows in `claude agents --json` under `~/cobalt-wt/agy-trial` / `s2-p4` (daemon-less leftovers); the `main`-side redaction of the real E1 date in three DRC docs (R21 ESC 1, history NOT rewritten, L54).
- [ ] **FUTURE (09-21, R45c, his words) — a conversational setup-builder surface.** "There should actually be in the future... an area where I can talk to you and you can walk me through all the multiple questions and we build another setup." Not now — a queue item for the S5 / playbook lane once the seven-setups build's Lego pattern (registries keyed by data, not by trade name) is proven live.

- [ ] **TICKET (09-25 R23, his "A" on 09-24 R107) — voice V1's A1 refusal pattern over-refuses the pronoun `I`.** `src/cobalt/voice/tools.py:61` (`re.I` + `(?-i:[A-Z]{1,5})\b`) refuses ordinary card phrasings where `short` / `close` is followed by the capital `I` or by a ticker after another word (`what is the stop on the XYZ short I opened`); each gets the fixed refusal and nothing executes (safe side). Fix in V1's next round, after his device session (E1 E3 E5 E8 X3): the pattern excludes the pronoun `I` and takes the ticker only directly after the verb. Source: `reports/voice-v1-fix-r2-check-2026-09-24.md` (Opus ESCALATE 1, file-checked), `cto-2026-09-24.md` R107, `cto-2026-09-25.md` R23.

## DESIGN SESSIONS (register — planning hard cap: two calendar weeks total)

- [ ] **1. Trading Taxonomy Session** — FIRST. Absorbs variable registries.
      Inputs: Setups & Trades xlsx, cheat-sheet library, Jure examples,
      Dejan's walkthrough. Outputs: canonical vocabulary + §6 amendment,
      playbook schema ADR, per-playbook variable registry (incl. ≥1
      human-only tape dot each). Unlocks: strategies.yaml redesign, setups
      engine, semaphore board.
- [ ] **2. Data-Model + Vault combined block** — one weekend, back-to-back.
      Outputs: data-model ADR + embedder ADR (both GATE the memory port),
      Mattermost DB-split final call (recorded position: SPLIT), vault
      structure (Karpathy write-time vs Jones query-time vs Obsidian
      linking), inbox-as-interface policy, lazy-migration scoping.
- [ ] **3. Data-Source Spike** — NOT a session; sprint-0's first Claude
      Code task. Deliverable: data-source verification memo — all ELEVEN
      Finviz export families fired end-to-end, intraday bars VERIFIED (not
      assumed), FMP pricing, TradingView MCP state. Blocks any Charter item
      depending on data sources.
- [ ] **4. Product Definition sittings** (timeboxed) — Day-in-the-Life →
      mission-control/semaphore/Trade-Radar mockups (prebell/DRC/RUBRIC
      refs; Moderna Day-2 worked example) → MoSCoW with forced subtraction
      → **MVP Charter** → sprint ladder re-derived. Validation = working
      pre-beta slices on live mornings, not static mockups. Charter must
      show capacity math, trader-metric success criteria, build/trade
      firewall, ~5-variable semaphore scope.
- [ ] **5. Rules Engine Session** — post-Charter; gates Guardian, not MVP.
      Rule schema (trigger/state/action-ladder/channel/window), authoring
      path (DM/voice → draft config → HITL-token activation; Cobalt may
      PROPOSE rules through the same gate), hot-reload, boundary vs
      playbook variables.
- [ ] **6. HITL rebuild** — spec already ratified; implementation sprint.

## PORT/BUILD CANDIDATES (unsequenced — Charter derives the ladder)

KEEP-AS-IS ports (through the test/config gate; see TRIAGE for riders):
- MemoryProvider ABC (only if new core wants the contract) · db_status.py
  (minus DEBUG dump) · tools/knowledge.py
- BrowserTool as fetch-primitive · live_run_{finviz,quote,dynamic} smoke
  scripts · FinvizApiClient (seed → grows config-driven across all 11
  export families) · MetadataEnricher (minus secret-dumping sink)
- Mattermost REST helpers + native WS loop (cache IDs) ·
  Proposal/IntentAlignment models · MATTERMOST_CREDS vault routing
- rules.yaml trading_rules · FinanceTool (stopgap; deprecated when FMP
  collectors land) · LLM routing class (+retries/timeouts/fallback/effort/
  cost capture) · config.yaml models/profiles/network · prompts.yaml
  (dead sections removed/wired) · dev_utils/test_routing.py
- Filesystem tools + jail · CobaltSettings core · VaultManager ·
  manage_vault.py · docker-compose · generate_context.py
- cobalt.sh (KEEP-CONCEPT: PID/health/dev-prod awareness)

KEEP-CONCEPT / REBUILD (old code as spec):
- PostgresMemory core (conn factory, DDL-once, embeddings via routing) ·
  HITLProposalStore (per HITL spec) · init_5_pillar_schema (guarded)
- Domain whitelist · vault credential injection · ScannerOrchestrator +
  scanners.yaml (prime MVP-pillar-1 organ) · SemanticTagger + themes
- ProposalEngine live methods · DANGEROUS_TOOLS → risk-tiered capability
  classes
- Strategos · Playbook (one validated reader + registry) · rules.yaml
  cortex_routing · daily_in_play writer (never-built pillar-1 terminus)
- Cortex classification (deterministic, T=0) · OrchestratorEngine (one
  chief-of-staff) · BaseDepartment (one loop, one grammar) · PromptEngine
- Scribe (blocked by Vault Session) · obsidian_vault_path ONE resolver ·
  CobaltScheduler (timezone-correct, jobs in YAML) · launchd plists into
  ops/ + supervision · wipe/reset utilities (prod guards, never as-is)

NEW BUILDS (named requirements):
- Authenticated persistent browser sessions (smbtraining, SMB realtime
  board, FinancialJuice): persistent context, days-to-weeks unattended, no
  keep-alive, credential-refresh flow, logged-out = typed failure + LOUD
  alert, drift = alert + redesign.
- Grading/EV/sizing engine (spec: §6 + ASET sizer + Opportunity Framing
  xlsx; slice 1 is its first sliver) · Priority setups engine (dependency:
  intraday bar source VERIFIED at Spike) · Briefing engine (ONE, prebell
  model, both old paths die) · In-play rules as deterministic function over
  typed snapshots.

REDESIGN (blocked on session/ADR): 5-pillar schema + dual hitl_proposals
DDL (Data-Model Session) · embedder ADR · memory/browser/HITL/scribe/
scheduler/strategy tests · strategies.yaml schema (Taxonomy) · approval
interceptor (HITL spec) · supervision/out-of-band alerting · keys: alias
block → direct vault naming · .env/DATABASE_URL two-phase boot ·
Cortex._run_ops routing · 0-Inbox policy (inbox = interface).

## GATED (post-MVP)

- **Host OS upgrade (macOS 27) — deferred project** (ruled 2026-09-17,
  Dejan, R18: "is it still too risky for us to do that mid sprints and if
  so can we just today build deferred sprint or project and put it in the
  list for after we're done with what we're building right now … there's
  nothing stopping us to run on the old version it's not outdated yet").
  The Mac Studio stays on macOS Sequoia 15.x until the current build lane
  is done (S2-P2 D2 + P4 D1 live, MVP readiness). Not the OS's maturity —
  our host IS production (NN#16): OrbStack/Postgres, LM Studio MLX and the
  88 GB wired-memory setting, herdr, Tailscale, launchd jobs and restic all
  ride on it, and the upgrade buys the trading system nothing now. Gate
  first recorded 2026-09-03/04 (LEDGER:650, then named for Tahoe).
  ENTRY CHECKLIST when it is scheduled (one ops hub, a weekend, outside
  market days): (1) Cobalt key store in restic's include set + a fresh full
  restore proof (owed since 09-11); (2) restic password rotated (exposed
  09-11, his hand; 2026-09-20 R41: "no" — NOT rotated, step list due Mon
  09-21 with `ops-0921`); (3) second backup copy decided (offsite leg deferred
  09-11 R5; one local USB disk today); (4) compatibility check with
  versions for every resident + seat CLI; (5) pre-upgrade snapshot +
  `pg_dump`, bring-back checklist (`cobalt.sh`, LaunchAgents, heartbeat
  GREEN, day-open GREEN); (6) rollback plan stated honestly — a macOS
  major has no one-command rollback, the fallback is rebuild + restore, so
  the rebuild manifest (parked to S5) comes first or with it.
  Point updates inside Sequoia (15.8 security) are NOT this project:
  allowed any evening after 21:05 on his word, heartbeat check after.
- **Sessions-as-jobs gap analysis** (recorded 2026-09-16, Dejan: "record a
  gap") — the CTO-desk/hub practice built by hand on 09-15/16 (desk = L6
  chief of staff; prompt file = L16 registry entry; `claude agents` +
  wake-up reconcile = L18 job table + watchdog; `ASK DESK`/ESCALATE report
  lines = L38 asks; L58 = hand-run memory write) is what the laws specify
  and Cobalt has not built for agent sessions. Four gaps from real use:
  (1) session registry + liveness as Cobalt data (L18/L34 rows for agent
  sessions, not only launchd jobs); (2) ask/escalation routing as data;
  (3) HITL approvals as real tokens (L7 status note; L61 chat-approve is
  interim); (4) the Cobalt memory write command (L58 interim). Deliverable:
  a bounded gap analysis by a hub — `topics/cto-desk.md` + L58–L61 practice
  vs L6/L16/L18/L34/L38 and the MVP Charter — output an ADR candidate, no
  build. Timing: after S2 closes 09-23, unless the Anthropic meter is idle
  earlier. Owner: desk writes the prompt.
- **Cobalt mailbox on Dejan's domain** (ruled A 2026-09-16 21:3x, "after
  MVP, and if there is a desire for Cobalt to have an email address"):
  he owns an outward-facing domain with unlimited addresses. Two rows,
  both post-MVP, neither a design session: (a) IDENTITY — a Cobalt-owned
  address for vendor accounts (Finviz, X, data vendors) so no personal
  address sits in a vendor account; policy only, zero build; (b) INBOX
  COLLECTOR — deterministic IMAP pull into the cache for mail-only feeds
  (broker statements, earnings mailers), L9 collector shape, L32 user
  data. Outbound email stays RETIRED (09-14, Mattermost only, L14).
  NOT a backlog item, ruled out 09-16: a public, domain-hosted mission
  control — the tailnet already reaches every device of the one user;
  a public surface adds 2FA/TLS/hardening/patch duty under NN#16 for no
  capability; revisit only for an inbound-webhook vendor or a second
  human user (Tailscale Serve for a nicer tailnet URL if wanted).
- **Guardian sprint** — gates: grading/EV live + alerting + Rules Engine
  session. Content: real-time enforcement of the Guardian rule set
  (TRIAGE: 7 rules; live as DRC checkboxes until then); rule deactivation
  during market hours requires HITL token + cooling delay. Includes
  **trade-awareness spike**: read-only DAS log tail vs quick voice/DM
  trade logging — §3 boundary (no platform integration, no execution)
  absolute.

## STANDING FOLLOW-UPS

- [ ] **ESCALATE (next ops prompt) — the F18 `herdr` probe reads the list
      the SessionStart hook guard protects.** `herdr agent list` is what
      `heartbeat.probes.herdr` asserts on, and it is the same list a
      reverted hook pointer corrupts: a herdr bump replaces the
      herdr-managed hook script and can rewrite
      `~/.claude/settings.json`'s `hooks.SessionStart`, which today
      points at the non-herdr-managed guard
      `~/.claude/hooks/herdr-harness-guard.sh` (added 2026-09-08 to stop
      a Grok session double-firing Claude's inherited hook). If that
      pointer goes back to the herdr script, every Grok session reports
      itself as `claude` in `agent list` — and the probe would report a
      green, plausible, WRONG seat roster. The failure is silent in both
      places at once. **Decide in the next ops prompt whether the probe
      should verify the pointer itself** (cheap: stat the guard file and
      read one JSON key) or whether the manual checklist line in
      `docs/40 - DevDocs/reports/codex-seat-test-2026-09-07.md` §10 is
      enough. Blocks nothing today — `com.cobalt.herdr` ships
      `enabled: false` and the probe is not running — but it must be
      settled BEFORE the herdr handover flips that flag.

- [ ] Consolidate the Taxonomy draft chain (v0.2–v0.7, committed
      2026-09-03) into a standalone v0.8. v0.7 is an amendment layer over
      v0.4/v0.6, not a self-contained document — the chain currently IS
      the spec; next taxonomy bump should fold it into one clean file.
- [ ] Heartbeat probe: "every ops/ plist expected loaded is loaded" —
      `launchctl print gui/$UID/<label>` for each committed `ops/*.plist`,
      red + DM alert if a shipped job isn't bootstrapped. An uninstalled
      schedule is a silent failure by construction (this is how
      `com.cobalt.archiver` sat unloaded and the prefill plists sat
      uninstalled from 08-31 to 09-03, unnoticed). Note from the 09-03
      incident (see INCIDENT LOG): loaded-state alone is not sufficient
      — both prefill plists WERE loaded and still failed silently at the
      launchd spawn level (exit 78, no output). The probe should also
      compare each job's `last exit code` against 0/"never exited" and
      alert on a nonzero code, not just on not-loaded. Thin heartbeat
      lane (PROJECT-LEDGER 08-29/31).
- [ ] docs/00 - Project/COBALT-REQUIREMENTS.md §6 vocabulary amendment —
      after Taxonomy Session.
- [ ] Persona strings + vault-seeder content harvested as reference/intent
      history before any old-tree deletion commit.
- [x] Collect Dejan's existing Obsidian DRC/prep Templater templates
      (slice-2 prefill input) — found already in the vault's own
      5 - Templates/ (Daily.md, DRC.md, Individual Trade Template.md,
      TRADE REPORT CARD.md), ported to Jinja 2026-08-31.
- [x] docs/50 - Roles/ role-pack template + MODELS.md fleet tiering seeded
      (2026-08-25): planning=Fable, coach=Fable, DRC=Sonnet,
      logistics=Sonnet; promotion rule = model follows function.
- [x] TRIAGE.md committed to docs/20 - Assessment/ (2026-08-24).
- [x] New reference artifacts in docs/90 - References/ + INDEX entries; licensed
      PPTX local-only under gitignored assets/ (2026-08-24).
- [x] CLAUDE.md "Current phase" rewritten for build phase (2026-08-24).
- [2026-09-21 · ops-0921] Bare `uv run pytest -q` stops at collection on tests/test_finviz_extractor.py:34 (ImportError: cannot import name 'FinvizStockData') — old-tree tests under `testpaths = ["tests"]` (pyproject.toml:91); every gate runs `tests/cobalt tests/taxonomy` and never sees it. Desk's call: exclude the old-tree tests from the default collection, or leave the red. Evidence: reports/ops-2026-09-21.md item 4.

## DONE

- Assessment passes 0–8 + ASSESSMENT.md synthesis (2026-08-21/22).
- Path-jail hotfix (06-H1) (2026-08-22).
- docs/90 - References under version control; Finviz token rotation
  recorded (2026-08-22/24).
- Docs restructure to the D6 standard: docs/ reorganized into
  00 - Project / 10 - Decisions / 20 - Assessment / 30 - Design /
  40 - DevDocs / 50 - Roles / 90 - References / _archive; playground
  vault (0 - Inbox, 0 - Projects) untouched, out of scope (2026-08-26).
- TRIAGE ruling session → TRIAGE.md (2026-08-22).

## Taxonomy replay validation (v0.7 §13/§13.1)

Superseded 2026-09-02 (v0.7 schema v0.4 commit): the itemized list this
section used to carry is now a query, not a hand-maintained list
(v0.7 change log #19 — "Tunable slot"). Every `config, dynamic`
quantity (v0.6/v0.7 §0 "Dynamic definitions" law) is a row in
`configs/cobalt/taxonomy/tunables.yaml`
(`src/cobalt/taxonomy/tunables.py`'s `TunableRow`); the backlog is
`tunables.replay_backlog(registry)` — every row with `dynamic: true`
and `status != solidified` — surfaced by
`python -m cobalt.taxonomy.validate`'s summary line and covered by
`tests/taxonomy/test_trade_defs.py::test_dynamic_tunables_appear_in_replay_backlog`.
Corpus for every row: the Bar Archiver's minute-bar history
(`src/cobalt/archiver`, `configs/cobalt/watchlists.yaml` tickers). Pass
criterion is **TBD at n≥30** per row until a replay session sets it and
writes `status` (never `value` — a value change stays a Dejan ruling).

30 rows seeded at the v0.7 commit, all `replay_pending` or `proposed`
(none `solidified` yet) — read `tunables.yaml` directly for the current
set; do not re-duplicate it here.

## PENDING SITTINGS (standing — the desk carries these on every plate until Dejan holds or cancels them; ruled 2026-09-20 R10; narrowed 2026-09-21 R48)
**R48 (09-21, 18:12 ET), his words: "The only sitting that I think we need is the one that needs me. It's a DRC sitting... because the DRC needs to be designed by me... not by the tribunal."** LAWS CONSOLIDATION and SHORT-TERM MEMORY/DISK are NO LONGER sittings of his — each becomes a DESIGN ITEM (one house proposes, the four-house tribunal rules and derives, L67; the result reaches him as ONE approval; a law file is never voted, L39 — what the houses cannot settle stays OPEN for him). Only the DRC TEMPLATE sitting stays his.
| sitting / design item | prepared by | opened | status |
|---|---|---|---|
| **DRC TEMPLATE REVIEW** (Dejan + Claude; his docx + SMB template → the live Templater template) — S3-P3's precondition, his sitting under R48 | `30 - Design/DRC-SITTING-PACKET-2026-09-21.md` (READY 09-21: 15 decisions, 12 blocking S3-P3, 30 min) | 2026-09-10 (ladder "Rulings/inputs owed before S3") | **HELD 2026-09-22 15:14 ET** (09-22 R60 "DRC this week" → R65–R73 and R89–R103: coach spec as content, trade-reporter as the automation pattern, no PDF, input-driven DRC, diff model ruled A×4, Fable tribunal seat, all 21 owner items ruled); the DRC design then went to the four-house tribunal (`DRC DERIVED v2`, `30 - Design/DRC-AUTOMATION-v2-2026-09-22.md`); D1 BUILT 09-23 |
| **LAWS CONSOLIDATION** — 74 laws, 46 carrying amendments, contradictions known (L58 vs SESSION-CLOSE steps 3–4; L29's auto-mode clause vs the build hubs' launch lines; the routing cluster open since 09-13; L46/L54/L68 merge discipline) — now a DESIGN ITEM under R48, not his sitting | `laws-audit-0920` → `docs/40 - DevDocs/reports/laws-audit-2026-09-20.md` (input) | 2026-09-20 | **DONE 2026-09-22 as HIS sitting again** (09-22 R4 "Laws are all mine" supersedes 09-21 R48(a) for laws only; R80–R88, 14 of 14 items ruled; `LAWS.md` + `LAWS-HISTORY.md` applied ≈17:4x ET from `30 - Design/LAWS-FINAL-2026-09-22.md`, 75 entries, L75 new, L12 retired, trace `LAWS FINAL TRACED · clauses: 382 … dropped: 0`). Two follow-ups stay on the plate: the routing tribunal's FINAL fold (routing-cluster laws frozen until it rules) and the close's PROPOSED laws (`close-2026-09-23.md`) |
| **SECOND CHANCE REDESIGN** (his sitting with the desk; he is the output authority, L67 sitting clause) — his R116 / R117 anatomy vs the built `range_break.py`; Second Chance stays off the radar until it is redesigned | `reports/sitting-second-chance-2026-09-24.md` (85 lines: four decisions with recommendations, six settled by the houses, cheat sheet p.1–2 quoted, provenance per clause, `## HIS EXAMPLES` empty) | 2026-09-24 (R13 / R14) | **PENDING — UNHELD.** Runs on his word, FIRST (R14). He brings 5–10 chart examples + other traders' playbooks; a redesign then goes to the four-house tribunal (L67) → build → `taxonomy load`. Seam: A-17's level set also feeds vwap-continuation's `rejected` avoid — settle in one document before either build (L72) |
| **VWAP CONTINUATION REVIEW** (his cheat sheet, plain words; `dist.k.vwap` A-16 held out of the deploy, R118) | `reports/sitting-vwap-continuation-2026-09-24.md` (80 lines: three decisions) | 2026-09-24 (R13 / R14) | **PENDING — UNHELD.** After Second Chance (R14); same examples rule. `dist.k.vwap` is not in `Assumed Defaults.md` (R56) |
| **SHORT-TERM MEMORY / DISK** — five `public` pillar tables exist and are inert; 3 of 30 components do memory's job; 72 % of report facts reach memory; no path back from `INDEX.md`; no catalog of the ~100 k files. His scope (09-20 R18): recallable AND lean, indexed, covering every house's agents — now a DESIGN ITEM under R48, not his sitting | `memory-history-0920` → `docs/30 - Design/memory-history-2026-09-20.md`; `topics/memory-system.md` (input) | 2026-09-20 | **OWED: a proposal drafter, then the four-house tribunal.** Research READY 09-20; "nothing pruned without an emptiness proof" stands (09-20 R10/R11); the tribunal derives, not the desk |
