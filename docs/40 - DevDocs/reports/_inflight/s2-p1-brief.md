# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`

You build S2-P1 (radar pool + Finviz bar poller) in this worktree. Everything you need is in this
file. The plan it implements is `docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md`,
in this worktree. Where the two disagree, the plan wins; say so in the report.

## 0. Who does what

| House | Does | Cannot |
|---|---|---|
| **You (Sol)**, high effort, `-s workspace-write`, network on | write code, tests, docs, the report, inside this worktree | commit, rebase, write outside the worktree, touch the real vault or `cobalt_brain` |
| **Hub (Sonnet)** | launches you, verifies against ground truth, commits per step on `sprint-2/radar-pool`, runs what your sandbox cannot | build |
| **Dejan** | approves the HITL card | — |

**Hub, before launching you:** (1) if `ops/heartbeat-market-reset` has merged to main, rebase this
branch onto main first; (2) if the plan's §9 says the Astra review loop has not run, run it and fold
fixes into the plan before launch; (3) export the dev DB credentials into your environment without
printing them.

**Two runs.** RUN A = steps 0–13 (stage 1). Stop, print `DONE`. The hub commits stage 1, then
relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
Step G is **hub only, after Dejan's approval** — you never run it.

**Stop rules.** A step you cannot finish → mark it `NOT RUN` or `FAILED` in the report with the
exact error line (scrubbed), then continue with the steps that do not depend on it. Never mark a
test passing that did not run. 3 failed attempts at the same thing → stop that step, ESCALATE.
Print `DONE` as the very last line of every run, nothing after it.

## 1. Laws (binding — a violation is a failed step)

1. **Production is sacred (NN#16).** Dev only: `COBALT_ENV=dev`, database `cobalt_dev`, vault =
   `data/smoke-vault` (gitignored copy you make of `~/dev-vault-cobalt`). Never open
   `/Users/cobalt/Vault/Think`. Never connect to `cobalt_brain`. Never `launchctl` anything.
2. **User data never enters the repo (L32).** No real screen, filter string, list or dollar figure in
   any tracked file, report, fixture, test or log line you paste. The repo ships exactly ONE synthetic
   example screen (R2).
3. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error
   string passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
4. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent
   fallback, no plausible-empty artifact, no default invented for a missing value.
5. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
   `archiver.collector.fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`.
6. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted
   (`psycopg.sql.Identifier` in Python); cross-side SQL is schema-qualified (`system.radar_membership`);
   every new table is on a side in `src/cobalt/db_migrations/placement.py` or the suite fails.
7. **Config-as-code.** Pydantic schema per config file, `extra="forbid"`, dry-run command. New-core
   config lives only under `configs/cobalt/` (never `configs/*.yaml` top level).
8. **Tunables.** Thresholds are `configs/cobalt/taxonomy/tunables.yaml` rows. Use EXISTING
   `TunableUnit` / `TunableStatus` / `TunableSource` values only — adding an enum value breaks the
   live ASET sheet (09-09 outage). No fitting value → ESCALATE.
9. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE writing; never rely on catching
   `SessionBlocked`. Radar writes nothing in that window.
10. **Tools fetch, code computes.** No LLM anywhere in P1. All numbers are deterministic code.
11. **Tests per step.** `uv run pytest` for the step's tests before moving on; the whole suite at
    step 13.
12. **Names.** One name per concept across SQL, Python, config and docs (`radar_pool`,
    `radar_membership`, `account_mode`, `pool_member_id`, `excluded_by`).

## 2. Rulings you implement (09-10, binding)

- **R1 Radar Screens contract.** Vault note `1 - Trading/Radar Screens.md` gets one fenced YAML block
  per screen: `screen, f, sort, columns, active_from, active_to (session clock, ET), enabled`. It is
  written ONCE, through the vault writer, under ONE HITL card, prose untouched. After that Cobalt only
  reads the note: parse fenced blocks only, reload on file-hash change, mirror each block + hash into
  `"user".trader_settings`; `radar_membership.source` names screen + hash. Parse failure → pool row
  degraded + heartbeat `radar` probe RED naming the screen; never the previous version silently. Day
  Scan is active from 10:00 ET via the F1 session clock — a field, never code.
- **R2 Synthetic example screen.** Exactly one, same fenced format, as the test fixture under
  `tests/fixtures/`; real screens never enter the repo. `git ls-files | grep -i radar` stays clean of
  user data.
- **R3 `cobalt db query`.** Read-only CLI: factory connection, SET ROLE per side, SELECT-only enforced in
  code (reject anything else, loud), output JSON/table. The workers' DB read path.
- **R4 Static lists are user data.** They move user-side by the same mechanism as R1. Plan choice: a new
  vault note `1 - Trading/Radar Lists.md` with fenced blocks. The archiver keeps working through the
  migration (stage 2).
- **R5 Houses + RESTARTS by rule.** plist in diff → that job; changed file in a resident's `reads:` →
  that resident; registry → `register`; code/tests/docs → none; anything unclassified → ESCALATE.

## 3. Environment

- Run everything from this worktree with `uv run …`. Tests: `uv run pytest tests/cobalt tests/taxonomy`.
- DB env: the hub exports the Postgres credentials into your environment at launch. If a DB-backed test
  or command fails to connect, record `NOT RUN (db unreachable: <scrubbed error>)` and continue.
- No `psql` on this host. Before step 3 lands, reach the DB only through repo code; after it lands, use
  `uv run cobalt db query --side system|user "<select>"`.
- Finviz token: `cobalt.archiver.collector.resolve_token()`. If it fails in your sandbox, the live half
  of step 1 is `NOT RUN`; the hub runs it.
- Vault for smoke: `cp -R ~/dev-vault-cobalt data/smoke-vault` once, then
  `COBALT_VAULT_PATH=$PWD/data/smoke-vault`. `data/` and `logs/` are gitignored — confirm with
  `git check-ignore` before writing anything there.
- DevDocs layout: one page per `.py` file at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
  `docs/40 - DevDocs/tests/cobalt/<file>.md`, and a line in `docs/40 - DevDocs/INDEX.md`.

## 4. Build steps

Each step lists its files, then the tests that must pass before the next step starts.

### Step 0 — Base check (no code)
- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql`. Present → the heartbeat fix is in
  your base; build on it. Absent → build on main as is, register 0004 after 0002, and list in the report
  the files that will conflict at merge: `db_migrations/__init__.py`, `db_migrations/cli.py`,
  `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`,
  `tests/cobalt/test_jobs.py`.
- Record `git rev-parse HEAD` in the report.

### Step 1 — Finviz throttle re-measure (FIRST)
- `src/cobalt/radar/throttle.py` + `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`.
- Names = the 50 first tickers of the synthetic lists fixture (step 5 creates it; create that fixture
  file now if needed).
- Refuses on trading days between 09:00 and 16:00 ET, and inside market_reset (use `session_clock()` and
  the NYSE calendar).
- Per cycle: sequential `fetch_bars(t, Interval.I1, token)` for each name, then one
  `/export/screener?v=152&f=<fixture f>&c=0,…,150` call. STOP at the first non-200, 429, redirect,
  non-CSV body or header mismatch.
- Per stage record: requests, achieved req/min, status counts, p50/p95 latency ms, bytes. Write
  `data/radar-throttle-<UTC ts>.json` and print a table.
- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`. If every stage was clean, write
  "no throttle observed up to N req/min". Never extrapolate.
- **Tests (mocked HTTP):** stop-on-first-error per class; refusal inside the forbidden window; rpm math;
  token never appears in output (assert `auth=REDACTED`).
- **Live run:** allowed only outside the forbidden window. Otherwise, or on token failure, `NOT RUN`.

### Step 2 — Migration 0004, rollback bound, placement, J1
- `src/cobalt/db_migrations/0004_radar_pool.sql` and `0004_radar_pool.rollback.sql` with exactly the
  plan's §D3 DDL. Tables are created schema-qualified, `OWNER TO cobalt_system`;
  `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`;
  `GRANT SELECT ON system.radar_pool TO cobalt_user`. The rollback header states its cost.
- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring lines.
- `db_migrations/cli.py`: the digest excludes `account_mode` and `pool_member_id` (extend the heartbeat
  fix's `DIGEST_EXCLUDED_COLUMNS` if present; otherwise generalize `TENANCY_COLUMN` into that tuple).
  `--rollback` REQUIRES `--down-to NNNN`; it reverses only registered migrations newer than NNNN, newest
  first; without it, it refuses and lists targets.
- `placement.py`: move `radar_pool`, `radar_membership` out of `DECLARED_TABLES` into a new
  `CREATED_TABLES` dict ("created by a db_migration directly on its side"), included in `PLACEMENT` and
  in the proof table; extend the SQL/Python agreement test to 0004.
- **Tests** (`tests/cobalt/test_tenancy.py`, `tests/cobalt/test_radar_migration.py`):
  migrate twice idempotent; `migrate → --rollback --down-to 0003 → migrate` digests identical;
  0003's columns (if present) survive the 0004 rollback; `--rollback` without `--down-to` refuses;
  placement test green; J1 — FK catalog proof, `cobalt_user` SELECT OK / INSERT denied on
  `system.radar_membership`, valid id insert OK / invalid FK-fails, `cobalt_system` SELECT on
  `"user".aset_sizings` denied; membership CHECKs (`entered_at IS NOT NULL OR excluded_by IS NOT NULL`)
  and the partial unique index reject bad rows.

### Step 3 — `cobalt db query` (R3)
- `src/cobalt/db_query.py`, registered as `db query` in `db_migrations/cli.py`'s `db` group.
- `--side user|system` (required), `--prod` (`allow_prod=True`), `--format json|table`, `--limit`
  (default 1000). Connection = `db.connect(dbname, side=…)`.
- The guard and the belt exactly as plan §D8 (tokenizer aware of quotes, dollar-quotes and comments;
  single SELECT/WITH; refused words and functions; `BEGIN READ ONLY`; `SET LOCAL statement_timeout`
  from tunable `db.query.timeout_s`; `SELECT * FROM (<sql>) AS q LIMIT n`; always ROLLBACK;
  `current_user` asserted; output through F19 redaction).
- **Tests** (`tests/cobalt/test_db_query.py`): each refused class exits 2 with the token named; a
  keyword inside a string literal passes; multi-statement refused; data-modifying CTE refused;
  `set_config('role', …)` refused; user side reads `system.bars` qualified; `cobalt_brain` without
  `--prod` refuses (no connection attempted); the `psycopg.connect` lint still passes.

### Step 4 — Config
- `configs/cobalt/radar.yaml` + `src/cobalt/radar/config.py` (Pydantic, `extra="forbid"`): `pool_key`,
  `notes {screens: "1 - Trading/Radar Screens.md", lists: "1 - Trading/Radar Lists.md"}`,
  `active_sessions [premarket, rth, aftermarket]`,
  `export {v: 152, columns: "0-150", required_headers: [...]}`, `list_chunk_size`,
  `not_equity {header, values}`, `rank`, `cache {dir: data/radar-cache, retention_days}`.
- `required_headers` and the `not_equity` values come from a REAL recorded export header (step 6
  captures one) — until then mark them `# UNVERIFIED` and a test asserts they are replaced before step 13.
- `tunables.yaml` rows: `radar.pool_cap` 50 count; `radar.scan_interval` 60 duration;
  `radar.poll_interval` 60 duration; `radar.finviz_max_rpm` count (step 1 value);
  `heartbeat.radar_max_age_s` 180 duration; `db.query.timeout_s` 30 duration. Mirror the neighbouring
  rows' `scope/dynamic/status/source/consumers` shape.
- `cobalt radar check`: validates radar.yaml + tunables, and REFUSES when
  `pool_cap × 60 / poll_interval + max active screens + list chunks per minute > finviz_max_rpm`.
- **Tests** (`tests/cobalt/test_radar_config.py`): bad key crashes naming the file; budget refusal; every
  new tunable resolves; `load_tunables()` still validates (the ASET sheet reads this file).

### Step 5 — Notes parser, fixtures, mirror (R1, R2, R4)
- `src/cobalt/radar/models.py` (`ScreenBlock`, `ListBlock`, `ExcludeBlock`, `SourceSet`, `ExcludedBy`),
  `src/cobalt/radar/notes.py` (plan §D1): read bytes once, hash those bytes, fenced ```` ```yaml ````
  blocks only, every yaml fence must validate, sha256 per block and per note, key slugs unique.
- Mirror via `TraderSettingsStore.put`: keys `radar.note.screens`, `radar.note.lists`,
  `radar.screen.<key>`, `radar.list.<key>`, `radar.exclude`; value
  `{block, block_sha256, note_sha256, status: ok|parse_failed|removed, error}`;
  `source = vault:<note path>@<sha12>`. Writes only when the note hash changed. Never writes inside
  market_reset.
- Fixtures: `tests/fixtures/radar/radar-screens.example.md` — ONE synthetic screen (`screen: Example
  Session Scan`, synthetic `f`, `active_from: "10:00"`, `active_to: "16:00"`, `enabled: true`, a short
  prose paragraph around it). `tests/fixtures/radar/radar-lists.example.md` — synthetic lists: ≥60
  large-cap tickers (rule: well-known index heavyweights, not copied from any file in this repo), one
  ETF (for `not_equity`), one `exclude` block, `archive` intervals, exactly one `backfill_default`.
- **Tests** (`tests/cobalt/test_radar_notes.py`): fixture parses; each field's validation failure names
  the block; a non-validating yaml fence is a named failure; prose/markers ignored; hash stable across
  re-reads and changes on a one-byte edit; parse failure → mirror row `parse_failed`, never the old
  block; `TraderSettings.from_db()` returns identically with the radar rows present (the sheet cannot
  break); R2 test (file CONTENTS): no tracked file under `src/cobalt/`, `configs/cobalt/`,
  `tests/cobalt/`, `ops/` or `docs/40 - DevDocs/` contains `f=` followed by
  `sh_|ta_|fa_|an_|cap_|exch_|geo_|idx_|ind_|sec_|news_|earningsdate_|ipodate_|targetprice_`,
  outside `tests/fixtures/radar/` (use `git ls-files` for the tracked set).

### Step 6 — Screener collector, cache, replay
- `src/cobalt/radar/collector.py`: `ScreenerCollector` protocol; `FinvizScreenerCollector` —
  `GET https://elite.finviz.com/export/screener?v=152&f=<f>&o=<sort>&c=0,…,150` for screens and
  `…&t=<chunk>&c=…` for lists; one process-wide token bucket at `radar.finviz_max_rpm` shared with the
  poller; raw CSV cached to `data/radar-cache/<trade_date>/<source_key>-<HHMMSS>.csv`; parse by header
  NAME; missing header / non-CSV / HTTP error → `SourceFailure` (named, never an empty list); every
  string scrubbed.
- Capture ONE real export header with the fixture filter (if network + token work) and pin
  `required_headers` + `not_equity` from it; cite the capture file in the report (the header row only,
  no data rows pasted).
- `src/cobalt/radar/replay.py`: `ReplayCollector` serving cached CSVs by virtual clock, and
  `cobalt radar replay-build <day>` that synthesizes snapshots from `system.bars` i1 in cobalt_dev
  (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions
  present; supports only the fixture screen's filter codes; any other code fails loud). Named
  replay-only in its docstring.
- **Tests** (`tests/cobalt/test_radar_collector.py`): recorded-CSV parse; header mismatch → failure;
  HTML body → failure; `t=` chunking; token bucket pacing (fake clock); cache path under a gitignored
  dir; scrub.

### Step 7 — Pool decision + store
- `src/cobalt/radar/pool.py`: a pure function `decide(candidates, open_members, sources, cfg, now) →
  transitions`, no I/O, implementing plan §D4 steps 1–6 (manual, not_equity, rank, cap, screen_inactive,
  degraded sources held).
- `src/cobalt/radar/store.py`: `RadarStore` (`SIDE = Side.SYSTEM`) — pool row upsert, membership
  episodes per plan §D3 (open, admit, exclude, leave, trade-date rollover), all transitions of one
  cycle in ONE transaction.
- **Tests** (`tests/cobalt/test_radar_pool.py`, `test_radar_store.py`): table tests for every rule and
  every `excluded_by` value; cap never exceeded; rank tie-break deterministic; a degraded source's
  members held AND counted against the cap first (admissions fill only `pool_cap − held`; a held member
  is never evicted); re-admission closes the excluded episode and opens a new one; rollover closes the prior
  day; store-side lint (own side or qualified).

### Step 8 — Bar poller + aggregation
- `src/cobalt/radar/poller.py`: for admitted members in rank order, `fetch_bars(t, Interval.I1, token)`
  through the shared token bucket; keep `ts > watermark` (seeded from `max(ts)` per ticker in
  `system.bars`) and `ts + 1 min ≤ now`; `BarStore.upsert_bars`.
- `src/cobalt/archiver/aggregate.py`: pure `aggregate(bars, minutes)`, buckets floored from 00:00 ET,
  OHLCV rules explicit. Never stored.
- **Tests** (`tests/cobalt/test_radar_poller.py`, `test_archiver_aggregate.py`): watermark; open bar
  excluded; upsert idempotent; aggregation on hand-built bars incl. a DST day and a missing minute; an
  agreement check vs stored `i2` on the replay day (DB test) printing the % — any systematic mismatch
  goes to ESCALATE, not a tweak.

### Step 9 — Resident runner, registry, plist
- `src/cobalt/radar/runner.py` + `cobalt radar run` / `cobalt radar scan --once [--replay <day>
  --from HH:MM --to HH:MM]`: `job_run("com.cobalt.radar")`; `should_keep_running` each cycle; session
  asked FIRST (plan §D4): inactive → `idle`; market_reset → `paused_market_reset` with ZERO radar writes;
  otherwise reload notes → fetch → decide → store → poll bars; one cycle per `radar.scan_interval`;
  `last_scan_ms` stamped. The session is asked AGAIN immediately before the cycle's commit; a cycle
  whose commit would land in market_reset is dropped whole and logged.
- `configs/cobalt/jobs.yaml`: `com.cobalt.radar` — resident, `supervisor: self`, `timeout_s: 300`,
  `enabled: false`, `reads:` derived by instrumenting one `scan --once` (patch `open` / `Path.read_text`
  and record repo-relative paths), each entry with a `# file.py:line (loader)` comment.
- `ops/com.cobalt.radar.plist`: `ProgramArguments` `/Users/cobalt/.local/bin/uv run cobalt radar run`;
  `WorkingDirectory /Users/cobalt/cobalt`; `RunAtLoad true`; `KeepAlive {SuccessfulExit false}`;
  `COBALT_ENV production`; `COBALT_VAULT_PATH /Users/cobalt/Vault/Think`; `PATH` as the archiver plist;
  logs `logs/radar.log` / `logs/radar.err`. No double hyphen inside XML comments.
- `ops/README.md`: radar handover + "after `cobalt resume`, `launchctl kickstart
  gui/$(id -u)/com.cobalt.radar`".
- **Tests** (`tests/cobalt/test_radar_runner.py`, `test_jobs.py`): market_reset cycle writes nothing
  (row counts); a cycle started at 19:59:50 ET with a fake clock that reaches 20:00:05 at commit writes
  nothing; idle cycle makes no HTTP call; kill switch → clean exit 0; `uv run cobalt validate`
  exit 0 (registry ↔ plist); watchdog: stale heartbeat on this resident → `zombie`.

### Step 10 — F18 `radar` probe
- `probes.radar(now)` in `src/cobalt/heartbeat/probes.py`, added to `take_beat` in
  `heartbeat/runner.py`, exactly plan §D9.
- **Tests** (`tests/cobalt/test_heartbeat.py`): each branch (not probed / no row / paused / idle / fresh /
  stale / degraded names sources / parse_failed names the screen).

### Step 11 — Account-mode tag
- `"user".day_modes.account_mode` setter: `cobalt daymode account-mode live|sim [--date YYYY-MM-DD]`,
  market_reset-gated like the other day-mode writes.
- `aset/store.py` INSERT stamps `account_mode` from today's `day_modes` row; `aset/web.py` renders a
  `LIVE` / `SIM` / `ACCOUNT MODE UNSET` badge on every card. No card is refused because of it.
- **Tests** (`test_daymode.py`, `test_aset_store.py`, `test_aset_web.py`): setter gated; stamp from the
  row; NULL → UNSET badge; existing card flows unchanged (whole aset test files green).

### Step 12 — Seed command (fixtures and smoke vault ONLY)
- `src/cobalt/radar/seed.py` + `cobalt radar seed --dry-run | --apply --hitl <token> [--only
  screens|lists]` per plan §D2: prose → blocks with `# from:` verbatim-source comments and
  `# PROPOSED` markers; `upsert_unit` per screen section; `create_if_absent` for the Lists note rendered
  from `configs/cobalt/watchlists.yaml`; create-once refusal; market_reset refusal; `--apply` without
  `--hitl` refuses; prints write_ids + restore lines; `--probe-ft` compares each screen's ticker set with
  and without `ft=4` (hub use).
- **You run it only with `COBALT_VAULT_PATH=$PWD/data/smoke-vault`.** Its prose input is rendered from
  the screen fixture inside the test — no second screen definition.
- **Tests** (`tests/cobalt/test_radar_seed.py`): every pre-existing line byte-identical, diff is
  insertions only; `f` mismatch between the export line and the filters line refuses; the lists note
  round-trips to the same targets as the YAML; second apply refuses; `restore` by write_id returns the
  original bytes.

### Step 13 — Smoke + report (end of RUN A)
- Run plan §D12 S0–S12 against `data/smoke-vault` + `cobalt_dev` (S0 = `COBALT_ENV=dev uv run archiver
  --backfill <T>` for each synthetic list ticker; it writes only to cobalt_dev). One row per check:
  PASS/FAIL/NOT RUN + the evidence command and its key output line.
- Whole suite: `uv run pytest tests/cobalt tests/taxonomy` (count passed/failed/skipped);
  `uv run cobalt validate`; `uv run cobalt radar check`; `git ls-files | grep -i radar` listing.
- DevDocs page for every new or changed `.py` (layout in §3) + INDEX lines.
- RESTARTS: derive from `git diff --name-status main...HEAD` plus untracked files (`git status
  --porcelain`), one row per path, by the R5 rule, using `uv run cobalt jobs readers <path>` for every
  changed config path. Unclassified → ESCALATE.
- Write the report (§5). Print `DONE`.

### Step 14 — RUN B: stage 2 (archiver onto the Lists note)
- `archiver/config.py` reads targets from the Lists note via `cobalt.radar.notes` (read + validate only,
  no mirror write); `archive_targets` / `backfill_targets` per plan §D11; missing or failed note → loud.
- `cobalt radar sources [--json] [--archiver-diff --yaml-rev <sha>]`.
- Tests re-targeted to the lists fixture; `git rm`-equivalent: delete `configs/cobalt/watchlists.yaml`
  from the working tree (the hub commits the deletion).
- **Tests:** render a Lists note FROM `configs/cobalt/watchlists.yaml` at RUN A's commit (the hub gives
  you the sha) with the step-12 seed code into `data/smoke-vault`; archiver-diff between that note and
  the YAML at the same sha is empty (the synthetic lists fixture is NOT the comparison — it is different
  data by design); `archiver --backfill <T>` works from the note on cobalt_dev; the whole suite green.
- Update the report (S13 row, stage-2 file list, RESTARTS rows). Print `DONE`.

### Step G — HUB ONLY, after Dejan approves the HITL card (never Sol)
Run as plan §6 L6–L8, from `~/cobalt` after stage 1 is merged, outside market_reset:
`COBALT_ENV=production uv run cobalt radar seed --dry-run` (diff sha256 must equal the card's) →
`--apply --hitl <token>` → `cobalt radar sources` → `--archiver-diff --yaml-rev HEAD` empty.

## 5. Report — `docs/40 - DevDocs/reports/s2-p1-2026-09-10.md`

Report discipline: §0 headline ≤5 lines (what changed, status, ESCALATE count) → tables → ESCALATE.
No restating this brief, no process narration.

1. **§0 Headline** — READY FOR MERGE / NOT READY (+ the blocking rows).
2. **Base** — `HEAD` sha at step 0; heartbeat fix present or not; expected conflicts.
3. **Steps** — table: step · status · files · tests (passed/failed/skipped) · evidence.
4. **Throttle** — the stage table, `finviz_max_rpm`, or NOT RUN + reason.
5. **Smoke** — S0–S13 table.
6. **Migration proof** — the printed proof tables (forward, rollback --down-to 0003, forward).
7. **`reads:` derivation** — each path with file:line.
8. **RESTARTS derivation** — path · change · rule · restart.
9. **LIVE block** — plan §6 L0–L13, with real shas/tags filled where known, and the rollback column.
10. **DISSENT** — copy plan §9 verbatim.
11. **ESCALATE** — plan E1–E6 carried verbatim + anything new, one line each.
12. **Stage 2 file list** (RUN B).

You cannot write outside the worktree; the hub copies the report to `~/cobalt/docs/_inflight/` for the
vault.

Print `DONE` last.
