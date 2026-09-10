# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`

You build S2-P1 (radar pool + Finviz bar poller) in this worktree. The plan it implements is
`docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md` (FINAL). Section references (D1…D15, §3, §4)
point there. Where the two disagree, the plan wins; say so in the report.

## 0. Who does what

| House | Does | Cannot |
|---|---|---|
| **You (Sol)**, high effort, `-s workspace-write`, network on | code, offline tests, fixtures, migrations as files, plist, DevDocs, the report — inside this worktree | commit, rebase, write outside the worktree, connect to ANY database, touch any vault |
| **Hub (Sonnet)** | launches you, verifies, commits per step on `sprint-2/radar-pool`; runs migrations on cobalt_dev, the DB-backed suite, the dev-vault smoke (plan D15 H1–H12), and the live throttle probe if yours was NOT RUN | build |
| **Dejan** | approves the HITL card | — |

**Hub, before launching you:** the branch is rebased on main `16847eb` and the plan is FINAL. Launch with NO
database environment: no `POSTGRES_*` variables in your environment, no `.env` in the worktree.

**Two runs.** RUN A = steps 0–13 (stage 1). Print `DONE`. The hub runs H1–H11 and commits stage 1, then
relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
Plan D13's real propose/apply and §6 LIVE steps are hub-only; you never run them.

**Stop rules.** A step you cannot finish → `NOT RUN` or `FAILED` in the report with the exact error line
(scrubbed), then continue with the steps that do not depend on it. Never mark a test passing that did not run.
3 failed attempts at the same thing → stop that step, ESCALATE. `DONE` is the last line of every run.

## 1. Laws (binding — a violation is a failed step)

1. **No credentials (E7).** You never connect to a database. Never read, copy or create a `.env`; never read
   `~/cobalt/.env`; never export or set `POSTGRES_*`. Every test that needs a DB carries `requires_db`
   (the existing pattern, `tests/cobalt/test_aset_store.py:30`) and skips in your environment.
2. **Production is sacred (NN#16).** Never open `/Users/cobalt/Vault/Think` or `~/dev-vault-cobalt`; vault
   tests use `tmp_path`. Never `launchctl` anything.
3. **User data never enters the repo (L32, E5).** No real screen, filter string, list or dollar figure in any
   file, report, fixture, test or pasted log line. The repo ships exactly ONE synthetic screen (R2).
4. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error string
   passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
5. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent fallback,
   no plausible-empty artifact, no default invented for a missing value.
6. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
   `archiver.collector.finviz_get` / `fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`, `AsetStore.save`,
   `DayModeStore.attest_sheet`.
7. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted (`psycopg.sql.Identifier`);
   cross-side SQL is schema-qualified; every table is on a side in `db_migrations/placement.py`.
8. **Config-as-code.** Pydantic, `extra="forbid"`, a dry-run command. New-core config only under
   `configs/cobalt/`. Committed config carries engine tunables only — never a cap, rank rule, metric choice
   or stickiness (those are the vault pool block's, D2).
9. **Tunables.** EXISTING `TunableUnit` / `TunableStatus` / `TunableSource` values only (09-09 outage). No
   fitting value → ESCALATE.
10. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE each write stage; never rely on catching
    `SessionBlocked`. Radar writes nothing in that window.
11. **Tools fetch, code computes.** No LLM anywhere in P1.
12. **Tests per step.** The step's tests before moving on; the whole offline suite at step 13.
13. **Names.** One name per concept: `radar_pool`, `radar_membership`, `account_mode`, `aset.account_mode`,
    `pool_member_id`, `excluded_by`, `below_cap_streak`, `scan_id`, `failed_stage`, `poll_failures`, `ticker`.

## 2. Rulings you implement (09-10, binding)

- **R1 Screens contract.** Vault note `1 - Trading/Radar Screens.md`: one fenced YAML block per screen —
  `screen, f, sort, columns, active_from, active_to, enabled`, plus optional `ft` (D1). Cobalt only reads the
  note: fenced blocks only, reload on file-hash change, mirror each block + hash into `"user".trader_settings`;
  `radar_membership.source` names source + hash. Parse failure → degraded + `radar` probe RED naming it.
- **R2** Exactly one synthetic screen, as a fixture under `tests/fixtures/radar/`.
- **R3 `cobalt db query`.** Read-only CLI, SELECT-only enforced in code (D10).
- **R4 Static lists** move user-side by the same mechanism: vault note `1 - Trading/Radar Lists.md`.
- **E1 / D1 Account mode.** Card stamp = `day_modes.account_mode` for the day → `trader_settings['aset.account_mode']`
  (standing, `live` seeded by migration 0004) → neither = card REFUSED, loud, logged, no row. The sim switch is
  a select on the attestation form writing `day_modes.account_mode` for that day (D8).
- **E2 / D2 Pool rule** = its own block kind `kind: pool` in the Screens note, own schema, exactly one;
  missing → pool frozen, degraded, probe RED. The cap lives there.
- **D3 Ranking.** premarket = volume, rth = RVOL, aftermarket = volume; overnight and market_reset do not scan.
  Every scan ranks all candidates; stickiness per plan D3's precedence table; the cap is hard; Morning Low Float
  ranks by volume in every session; Day Scan first among screens from 10:00.
- **E3** The three tiers move as they are; `source` names the tier.
- **E4 / D7** `ft` is an optional screen-block key from day one; the LIVE comparison decides whether a proposed
  block carries it.
- **E6 / D5 RESTARTS** by rule, derived by `cobalt jobs restarts`, printed in the report (plan §3).
- **D6** Per-store transactions in the fixed order membership → pool row → mirror → bars, each idempotent,
  partial failure named on the pool row; the session is checked inside each store transaction through its
  `before_commit` hook (D5).
- **E8** The vault write is propose (you build + offline tests) → HITL card → apply (hub).
- **D8** The throttle probe observes status, redirects and elapsed through `finviz_get`'s `on_metrics` (D6).

## 3. Environment

- Everything from this worktree with `uv run …`. Offline suite: `uv run pytest tests/cobalt tests/taxonomy`.
- DB-backed tests: mark `requires_db` (skip without `POSTGRES_HOST`/`POSTGRES_USER`). Give every store a
  fake or an injected connection so its logic is testable offline; the SQL itself is tested by the hub.
- Finviz token: `resolve_token()`. If it fails in your sandbox, the live throttle run is `NOT RUN`.
- Vault tests: `tmp_path` + `COBALT_VAULT_PATH` monkeypatched to it.
- `data/` and `logs/` are gitignored — confirm with `git check-ignore` before writing there.
- DevDocs: one page per `.py` at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
  `docs/40 - DevDocs/tests/cobalt/<file>.md`, a line each in `docs/40 - DevDocs/INDEX.md`.

## 4. Build steps

Each step lists files, then the tests that must pass before the next step.

### Step 0 — Base check (no code)
- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql` must succeed (main `16847eb`). Absent →
  STOP, report `FAILED: base is not 16847eb`.
- Record `git rev-parse HEAD`.

### Step 1 — Finviz transport + throttle probe (FIRST; plan D6, §4)
- `archiver/collector.py`: `FetchMetrics` model; `finviz_get(path, params, token, *, on_metrics=None)` with
  today's client settings (timeout 30 s, `follow_redirects=True`); `on_metrics` fires before `raise_for_status`
  with `status`, `redirect_statuses` (from `response.history`), `elapsed_ms`, `bytes`, `content_type`, or
  `error` on a transport failure. `fetch_bars(ticker, interval, token, *, on_metrics=None)` calls it.
- `src/cobalt/radar/throttle.py` + `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`:
  names = first 50 tickers of the lists fixture (create `tests/fixtures/radar/radar-lists.example.md` now);
  refuses 09:00–16:00 ET on trading days and in market_reset; per cycle sequential `fetch_bars(…, on_metrics=)`
  then one screener call through `finviz_get` with the fixture filter; STOP at the first status ≠ 200, any
  redirect, error, non-CSV body or header mismatch; per stage: requests, achieved req/min, status counts,
  p50/p95 ms, bytes → `data/radar-throttle-<UTC ts>.json` + printed table;
  `finviz_max_rpm = floor(0.5 × highest clean stage req/min)`; all clean → "no throttle observed up to N req/min".
- **Tests (mocked HTTP, `test_radar_throttle.py`, `test_archiver_collector.py`):** each stop class incl. a 302
  followed to 200 (redirect seen in `redirect_statuses`); refusal windows; rpm math; `auth=REDACTED`; existing
  archiver collector tests unchanged and green.
- **Live run** outside the forbidden window only; otherwise or on token failure `NOT RUN`. The number (or
  NOT RUN) is the report's first row.

### Step 2 — Migration 0004 as files, bounded rollback, direction-aware proof, placement (plan D4)
- `src/cobalt/db_migrations/0004_radar_pool.sql` + `0004_radar_pool.rollback.sql`: exactly plan D4's DDL,
  grants, ownership, the `aset.account_mode` seed and the rollback (header states its cost).
- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring.
- `db_migrations/cli.py`: `DIGEST_EXCLUDED_COLUMNS` + `account_mode`, `pool_member_id`; `--rollback` REQUIRES
  `--down-to NNNN` (refuses before connecting, lists targets) and runs only newer reverse files, newest first;
  verdicts `CREATED` / `DROPPED` / `CHANGED` computed BEFORE commit; `CHANGED` rolls back.
- `placement.py`: `radar_pool`, `radar_membership` → new `CREATED_TABLES`, in `PLACEMENT` and the proof set.
- **Offline tests (`test_radar_migration.py`, `test_tenancy.py`):** 0004 DDL ↔ placement agreement (parse the
  SQL text); `--down-to` file selection; refusal without `--down-to` with no connection attempted; verdict
  function table; abort-before-commit ordering with a fake connection.
- **`requires_db` tests (hub):** idempotent migrate; round trip digests; 0003 columns survive; seed row
  present/absent; J1 (plan D9); membership CHECKs and both unique indexes reject bad rows.

### Step 3 — `cobalt db query` (plan D10)
- `src/cobalt/db_query.py`, registered as `db query`. Guard pure and separately importable.
- **Offline tests (`test_db_query.py`):** every refused class exits 2 naming the token; keyword in a literal
  passes; multi-statement; data-modifying CTE; `set_config('role', …)`; `cobalt_brain` without `--prod` refuses
  before connecting; the `psycopg.connect` lint still passes.
- **`requires_db`:** READ ONLY belt, timeout, `current_user`, user side reads `system.bars` qualified.

### Step 4 — Config (plan D12)
- `configs/cobalt/radar.yaml` + `src/cobalt/radar/config.py`: `pool_key`, `notes {screens, lists}`,
  `export {v: 152, columns: "0-150", required_headers, metric_headers {volume, rvol}}`, `list_chunk_size`,
  `not_equity {header, values}`, `cache {dir: data/radar-cache, retention_days}`. `required_headers`,
  `metric_headers` and `not_equity` come from a real header capture (step 6); until then `# UNVERIFIED` and a
  test that fails at step 13 if still marked.
- `tunables.yaml`: `radar.scan_interval` 60 duration; `radar.poll_interval` 60 duration;
  `radar.poll_overlap_bars` 5 count; `radar.finviz_max_rpm` count (step 1); `heartbeat.radar_max_age_s` 180 duration; `db.query.timeout_s` 30
  duration — neighbouring rows' `scope/dynamic/status/source/consumers` shape. The cap is never a tunable (it lives in the pool block).
- `jobs/config.py`: `JobSpec.imports: Optional[list[str]]`; `jobs.yaml`: `imports:` on every resident per
  plan §3.
- `cobalt radar check`: validates radar.yaml + tunables.
- **Tests (`test_radar_config.py`, `test_jobs.py`):** bad key crashes naming the file; every new tunable
  resolves; `load_tunables()` validates; `load_job_registry()` validates with `imports`.

### Step 5 — Notes parser, block kinds, mirror, fixtures (plan D1, D2)
- `src/cobalt/radar/models.py`: `ScreenBlock` (optional `ft`), `PoolBlock`, `ListBlock`, `ExcludeBlock`,
  `SourceSet`, `ExcludedBy`. `src/cobalt/radar/notes.py`: bytes read once and hashed; yaml fences only;
  dispatch by `kind` per note (D1); exactly one pool block; override keys cross-checked; budget check (D2);
  sha256 per block and note.
- Mirror via `TraderSettingsStore.put` with plan D1's keys and statuses; "changed" against the stored
  `note_sha256`; no write in market_reset.
- Fixtures: `radar-screens.example.md` — ONE screen block `example_session_scan` (synthetic `f`,
  `active_from: "10:00"`, `active_to: "16:00"`, `enabled: true`), ONE pool block (`cap: 5`,
  `stickiness_scans: 2`, `priority: [screens, lists]`, `rank_metric` for premarket/rth/aftermarket,
  `overrides: {example_session_scan: {first_from: "10:00"}}`), prose in the "Export call (derived)" /
  "Filters" / "Sort" shape. `radar-lists.example.md` — ≥60 large caps (well-known index heavyweights, not
  copied from any repo file), one ETF, one `kind: exclude` block, `archive` intervals, one `backfill_default`.
- **Offline tests (`test_radar_notes.py`):** plan D15 O5; each field failure names the block; prose/markers
  ignored; hash stable, changes on a one-byte edit; mirror with a fake store → `parse_failed` / `missing`,
  never the old block; `TraderSettings._build` succeeds with radar rows present; R2 content test (plan D1).

### Step 6 — Screener collector, cache, replay (plan D6)
- `src/cobalt/radar/collector.py`: `ScreenerCollector` protocol; `FinvizScreenerCollector` through
  `finviz_get` (screens with optional `&ft=`; lists via `t=` chunks); one process-wide token bucket; cache
  path; header-name parse; `SourceFailure` on missing header / non-CSV / HTTP error / redirect.
- Capture ONE real export header with the fixture filter (network + token) and pin `required_headers`,
  `metric_headers`, `not_equity` from it; cite the capture file (header row only) in the report.
- `src/cobalt/radar/replay.py`: `ReplayCollector` serving snapshots by virtual clock; pure
  `snapshots_from_bars(bars, screen, prior_sessions)` (RVOL proxy per plan D15 H4; only the fixture screen's
  filter codes; any other code fails loud); `cobalt radar replay-build <day>` reads `system.bars` (DB, hub).
- **Offline tests (`test_radar_collector.py`, `test_radar_replay.py`):** recorded-CSV parse; header mismatch;
  HTML body; redirect; `t=` chunking; token bucket (fake clock); cache path gitignored; scrub; snapshot synthesis
  from generated bars.

### Step 7 — Pool decision + store (plan D3, D5)
- `src/cobalt/radar/pool.py`: pure `decide(candidates, open_members, blocks, sources, now) → transitions`
  implementing plan D3's rank key and precedence table exactly.
- `src/cobalt/radar/store.py`: `RadarStore` (`SIDE = Side.SYSTEM`) — S1 membership transitions and S2 pool row,
  each one transaction taking `before_commit`, idempotent per plan D5; `assert_writable("radar.<stage>")`.
- **Offline tests (`test_radar_pool.py`):** plan D15 O2; one table test per D3 step; rank key with mixed
  metrics never compares volume to RVOL; first_from before/after 10:00; cap lowered below held; streak
  reset/freeze/leave on the (N+1)-th scan; the cap-1 case (incumbent always ranked below one newcomer: retained
  at streaks 1..N, leaves at N+1 — retention never resets the streak); rollover closes the prior day.
- **`requires_db` (`test_radar_store.py`):** idempotent re-apply of a `scan_id`; unique indexes; store lint.

### Step 8 — Bar poller + aggregation (plan D7)
- `src/cobalt/radar/poller.py`: admitted members in rank order, `fetch_bars` through the shared bucket;
  closed bars with `ts > watermark(ticker, 'i1') − radar.poll_overlap_bars` minutes;
  `BarStore.upsert_bars(bars, before_commit=gate("bars"))`; `poll_failures` entries with reasons `error` and
  `stale` (rth only), onset and recovery per plan D7.
- `src/cobalt/archiver/store.py`: `upsert_bars(bars, *, before_commit=None)`, the hook called last inside the
  connection context; `None` = today's behaviour.
- `src/cobalt/archiver/aggregate.py`: pure `aggregate(bars, minutes)`, floored from 00:00 ET, explicit OHLCV.
- **Offline tests (`test_radar_poller.py`, `test_archiver_aggregate.py`):** watermark with a fake store; overlap re-upsert;
  open bar excluded; `error` and rth `stale` entries with onset and recovery, no stale rule outside rth; aggregation incl. a DST day and a missing minute.
- **`requires_db`:** upsert idempotent; aggregate vs stored i2 agreement % on the replay day (hub, H7).

### Step 9 — Resident runner, stages, registry, plist (plan D5)
- `src/cobalt/radar/runner.py` + `cobalt radar run` / `cobalt radar scan --once [--replay <day> --from HH:MM
  --to HH:MM]`: `job_run`; `should_keep_running`; session asked first; S1 → S2 → S3 → S4, each store call given
  `before_commit=gate(stage)` (raises `StageDropped` in market_reset, rolling that transaction back; later
  stages and remaining S4 tickers skipped); `settings/store.py`: `put(rows, *, source, before_commit=None)`,
  the hook called immediately before `conn.commit()`; partial-failure handling and `failed_stage` stamping per plan D5; `scan_id` monotonic.
- `jobs.yaml`: `com.cobalt.radar` row per plan D5; `reads:` derived by instrumenting one offline
  `scan --once` with fakes (patch `open` / `Path.read_text`, repo-relative paths), each with `# file.py:line`.
- `ops/com.cobalt.radar.plist` per plan D5 (`PATH` as the archiver plist; no double hyphen in XML comments);
  `ops/README.md` radar handover.
- **Offline tests (`test_radar_runner.py`, `test_jobs.py`):** plan D15 O3, O4; idle cycle makes no HTTP call;
  market_reset cycle writes nothing (fakes); kill switch → exit 0; `cobalt validate` exit 0 (registry ↔ plist);
  watchdog: stale heartbeat on this resident → `zombie`.
- **`requires_db` (hub, H5):** the hook raising inside `RadarStore`, `TraderSettingsStore.put`,
  `BarStore.upsert_bars` and between S4 tickers rolls back; existing settings and archiver tests green.

### Step 10 — F18 `radar` probe (plan D11)
- `probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat`.
- **Offline tests (`test_heartbeat.py`, row source faked):** every D11 branch.

### Step 11 — Account mode (plan D8)
- `src/cobalt/aset/account_mode.py`: `resolve(conn, day)` → `live|sim` or `AccountModeUnresolved`.
- `aset/store.py` `save`: resolve on the same transaction before the INSERT; INSERT writes `account_mode`.
- `daymode/store.py` `attest_sheet(day, *, filename, account_mode=None, now=None)`: one upsert, `COALESCE` keeps
  the column when `account_mode` is None.
- `aset/web.py`: attestation form select; `POST /attest` validates and passes it; banner shows
  `ACCOUNT LIVE` / `ACCOUNT SIM` or that cards are refused; every card shows its stamp.
- **Offline tests (`test_aset_account_mode.py`, `test_aset_web.py`):** plan D15 O7 with fakes; the upsert SQL
  text keeps `COALESCE`; whole existing aset/daymode offline tests green.
- **`requires_db` (hub, H9):** stamp live / sim / refusal on cobalt_dev via TestClient.

### Step 12 — Propose / apply (plan D13)
- `src/cobalt/radar/propose.py` + `cobalt radar screens propose --pool-block <file> [--ft-compare]`,
  `cobalt radar lists propose`, `cobalt radar screens apply --proposal <artifact> --hitl <token> --sha256 <sha>`,
  `cobalt radar lists apply --proposal <artifact> --hitl <token> --sha256 <sha>` — derivation, `# from:` and
  `# PROPOSED` markers, pool-block validation, the proposal artifact per plan D13 (inputs + final units +
  target-note sha, sha256 over canonical JSON), diff, refusals, write_ids + restore lines. Apply writes exactly
  the artifact's units: no re-derivation, no network.
- `src/cobalt/radar/sources.py` + `cobalt radar sources [--json] [--archiver-diff --yaml-rev <sha>]`:
  `archive_targets(note)` / `backfill_targets(note, t)` — the functions stage 2's archiver will call. Stage 1,
  because LIVE L7/L8 run before stage 2 merges.
- **Offline tests (`test_radar_propose.py`, `tmp_path`):** prose → blocks from the screen fixture (no second
  screen definition); `f` mismatch between the export line and the filters line refuses; invalid pool-block file
  refused; diff insertions only; sha stable; `--ft-compare` with mocked HTTP adds `ft: 4` only where sets differ;
  lists proposal round-trips to the same targets as the YAML; the artifact records every input; apply refuses a
  changed artifact sha and a changed target note before calling the writer; `cobalt radar sources
  --archiver-diff` is empty for a Lists note rendered from `watchlists.yaml` at HEAD (the synthetic lists
  fixture is NOT the comparison).
- **`requires_db` (hub, H11):** apply writes, second apply refuses, `restore --write-id` byte-identical.

### Step 13 — RESTARTS tool, offline gate, report (end of RUN A)
- `src/cobalt/jobs/restarts.py` + `cobalt jobs restarts <git-range>`: plan §3 rule; static ast walk from each
  resident's `imports:`; unresolvable dynamic import or missing `imports:` → all residents; unclassified →
  ESCALATE line; untracked files included when the range ends at the working tree.
  **Tests (`test_jobs_restarts.py`):** each rule; a string-loaded module declared vs undeclared.
- Run plan D15 O1–O10. One row each: PASS / FAIL / NOT RUN + the command and its key output line.
- DevDocs for every new or changed `.py` + INDEX lines.
- RESTARTS: `uv run cobalt jobs restarts main...HEAD` output pasted as the derivation table.
- Write the report (§5). Print `DONE`.

### Step 14 — RUN B: stage 2 (plan D14)
- `archiver/config.py` reads targets from the Lists note through `cobalt.radar.sources.archive_targets` /
  `backfill_targets` (built in step 12; read + validate only); missing or failed note → loud.
- Tests re-targeted to the lists fixture; delete `configs/cobalt/watchlists.yaml` from the working tree (the
  hub commits the deletion).
- **Offline tests:** archiver config built from a Lists note rendered by `lists propose` from `watchlists.yaml`
  at RUN A's sha (the hub gives it) into `tmp_path` equals the targets that YAML produced. **`requires_db`
  (hub, H12):** `archiver --backfill <T>` from the note.
- Update the report (stage-2 file list, `cobalt jobs restarts <RUN A sha>...HEAD`). Print `DONE`.

## 5. Report — `docs/40 - DevDocs/reports/s2-p1-2026-09-10.md`

§0 headline ≤5 lines (what changed, status, ESCALATE count) → tables → ESCALATE. No restating this brief.

1. **§0 Headline** — READY FOR HUB GATE / NOT READY (+ blocking rows).
2. **Throttle** — `radar.finviz_max_rpm = N` (or NOT RUN + reason) first, then the stage table.
3. **Base** — HEAD sha at step 0.
4. **Steps** — step · status · files · tests (passed / failed / skipped `requires_db`) · evidence.
5. **Offline gate** — O1–O10.
6. **Hub gate** — H1–H12, every row `NOT RUN (hub)`; the hub fills them.
7. **Header capture** — file path + header row only.
8. **`reads:` derivation** — each path with file:line.
9. **RESTARTS derivation** — the tool's output: path · change · rule · restart, and the `RESTARTS:` line.
10. **LIVE block** — plan §6 L0–L13 with real shas where known, rollback column kept.
11. **DISSENT** — plan §9 DISSENT verbatim.
12. **ESCALATE** — plan §8 verbatim + anything new, one line each.
13. **Stage 2 file list** (RUN B).

You cannot write outside the worktree; the hub copies the report to `docs/_inflight/` for the vault.

Print `DONE` last.
