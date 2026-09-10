Reading additional input from stdin...
OpenAI Codex v0.153.4
--------
workdir: /Users/cobalt/cobalt-wt/s2-p1-radar-pool
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: medium
reasoning summaries: none
session id: 01a08bf5-d7ab-7e63-9eac-323c4cd11be9
--------
user
Round 2. Round 1 ended on a usage limit without a verdict. Review docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md and s2-p1-brief.md, focusing on the RULINGS ADDENDUM section and its consistency with the rest, against ADR-0008, DATA-SOURCE-MEMO, the archiver collector, db_migrations/ and src/cobalt/jobs/. Output BLOCKERS (file:line) / RISKS / VERDICT.
hook: SessionStart
hook: SessionStart Completed
codex
I’ll read the plan and brief, then check the RULINGS ADDENDUM against the architecture decisions, source memo, collector, migrations, and job code.
exec
/bin/zsh -lc "pwd; rg --files -g 'AGENTS.md' -g '*s2-p1*' -g '*ADR-0008*' -g '*DATA-SOURCE-MEMO*' -g '*archiver*' -g '*collector*' -g '*migration*'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
/Users/cobalt/cobalt-wt/s2-p1-radar-pool
src/cobalt/taxonomy/note_migration.py
src/cobalt/taxonomy/trade_note_migration.py
src/cobalt/archiver/collector.py
tests/taxonomy/test_note_migration.py
tests/taxonomy/test_trade_note_migration.py
ops/com.cobalt.archiver.plist
tests/cobalt/test_archiver_report.py
tests/cobalt/test_archiver_collector.py
tests/cobalt/test_archiver_store.py
tests/cobalt/test_archiver_config.py
docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r1.md
docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md
docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md
docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md
docs/30 - Design/DATA-SOURCE-MEMO.md
docs/30 - Design/archiver-runs.md
docs/40 - DevDocs/cobalt/archiver/collector.md
docs/40 - DevDocs/cobalt/taxonomy/note_migration.md
docs/40 - DevDocs/cobalt/taxonomy/trade_note_migration.md
docs/10 - Decisions/ADR-0008-two-layer-data-model.md
docs/40 - DevDocs/tests/cobalt/test_archiver_store.md
docs/40 - DevDocs/tests/cobalt/test_archiver_collector.md
docs/40 - DevDocs/tests/cobalt/test_archiver_config.md
docs/40 - DevDocs/tests/cobalt/test_archiver_report.md

exec
/bin/zsh -lc "rg --files -g 'AGENTS.md' -g '*' db_migrations src/cobalt/jobs; nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md'; nl -ba 'docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
rg: db_migrations: No such file or directory (os error 2)
src/cobalt/jobs/cli.py
src/cobalt/jobs/entrypoint.py
src/cobalt/jobs/__init__.py
src/cobalt/jobs/watchdog.py
src/cobalt/jobs/models.py
src/cobalt/jobs/config.py
src/cobalt/jobs/wrapper.py
src/cobalt/jobs/migrations/0001_cobalt_jobs.sql
src/cobalt/jobs/store.py
src/cobalt/jobs/killswitch.py
     1	# S2-P1 PLAN — Radar pool + Finviz bar poller (2026-09-10)
     2	
     3	Architect: Opus 5 (plan + brief, no build) · Reviewer: Codex `gpt-6-astra`, read-only, ≤3 rounds ·
     4	Branch `sprint-2/radar-pool` off `main` `f646640` · Worktree `~/cobalt-wt/s2-p1-radar-pool` ·
     5	Build: Codex `gpt-5.6-sol` · Hub: Sonnet · Sprint S2 = 09-10 → 09-23.
     6	
     7	## §0 Headline
     8	
     9	- P1 ships the F2 resident `com.cobalt.radar` (4 screens + static lists → ≤ `radar.pool_cap` names, membership history), a Finviz i1 poller into `system.bars`, the account-mode tag, J1, `cobalt db query`, and an F18 `radar` probe.
    10	- User data moves user-side through vault notes only: screens (R1, existing note) and lists (R4, new note). One HITL card, one hub-run write, last, after Dejan approves.
    11	- Two merge stages: stage 1 = everything but the archiver's source switch; stage 2 = archiver reads the Lists note and `watchlists.yaml` is deleted, only after an equality proof on prod.
    12	- Precondition: `ops/heartbeat-market-reset` (uncommitted today, carries `db_migrations/0003`) merges first; this branch is rebased before build.
    13	- ESCALATE: 6 (§8). Review: 0 of 3 Astra rounds completed (Codex usage limit hit in round 1) — plan UNREVIEWED, see §9.
    14	
    15	## Line 0 — ADR-0008 in force
    16	
    17	| Law | How P1 honours it | Evidence |
    18	|---|---|---|
    19	| Two schemas, side per store | `RadarStore.SIDE = Side.SYSTEM`; mirror via existing `TraderSettingsStore` (`Side.USER`); `BarStore`, `JobStore` system | ADR-0008 D1; `db.py:115-133` |
    20	| Every new table in the placement map or the suite fails | `radar_pool`, `radar_membership` move from `DECLARED_TABLES` to a new `CREATED_TABLES` dict (created by a db_migration directly on its side), iterated by the proof table | `placement.py:65-79`; `test_tenancy.py:102-171` |
    21	| Already declared system-side | yes — `radar_pool`, `radar_membership` | `placement.py:72-75` |
    22	| Account-mode tag | `"user".aset_sizings.account_mode ∈ {live, sim}`, stamped from `"user".day_modes.account_mode` (new column, see E1); shown on every card | ADR-0008 D2 row 1 |
    23	| Migration in the fixed list, rollback SQL, digests unchanged | `src/cobalt/db_migrations/0004_radar_pool.sql` + `0004_radar_pool.rollback.sql`, appended to `FORWARD` / prepended to `REVERSE` after heartbeat's 0003; `DIGEST_EXCLUDED_COLUMNS` gains `account_mode`, `pool_member_id` | `db_migrations/__init__.py:25-31`; heartbeat worktree diff (0003 pattern) |
    24	| Cross-side refs schema-qualified | `system.radar_membership(id)` in SQL; lint `TestStoresNameOnlyTheirOwnSide` covers new stores | `test_tenancy.py:385-431` |
    25	| `"user"` always quoted | `psycopg.sql.Identifier`; reserved-word lint | `test_tenancy.py:348-383` |
    26	
    27	## §1 Facts the plan rests on (verified read-only 09-10)
    28	
    29	| # | Fact | Evidence |
    30	|---|---|---|
    31	| F1 | `cobalt db migrate --rollback` executes the WHOLE `REVERSE` tuple. With 0003 and 0004 registered, rolling back 0004 would also reverse 0003 and 0002 (every table back to `public`). | `db_migrations/cli.py:170`; heartbeat diff `REVERSE = (0003, 0002)` |
    32	| F2 | `cobalt_user` has SELECT on `system`, not REFERENCES — the J1 FK needs an explicit grant. | `0001_schemas.sql` §4–§5 |
    33	| F3 | No live/sim value exists anywhere: not in `day_modes`, `trader_settings`, or configs. | `daymode/migrations/0001_day_modes.sql`; `grep account_mode` → one SQL comment |
    34	| F4 | `TraderSettings._build` fails on MISSING keys only; extra `radar.*` rows cannot break the sheet. | `settings/models.py` `_build`; consumers `aset/config.py:267`, `daymode/config.py:311` |
    35	| F5 | `watchlists.yaml` holds three DERIVED tiers (`tier_a/b/c`), not the four TradingView lists. Its only reader is `archiver/config.py:19`. | file header lines 8–24; grep (other hits are comments) |
    36	| F6 | `fetch_bars` returns the whole i1 export: ~14 calendar days, ~9.4k rows/ticker. | `archiver/collector.py:159-174`; DATA-SOURCE-MEMO §2a |
    37	| F7 | Screener export `v=152&c=0..150` returns 151 named columns; `t=` multi-ticker works. | DATA-SOURCE-MEMO §1, §0 |
    38	| F8 | `ft=` is unverified; three of the four pasted screen URLs carry `ft=4`; R1's key list has no `ft`. | DATA-SOURCE-MEMO §0; vault note (read-only) |
    39	| F9 | Charter §9 names no request rate (Finviz Elite owned, $0 new spend). Measured points only: 5 names @10 s clean (LIVE-FEED-SPIKE §A); nightly archiver ~1,055 req / 23 min at 1.2 s sleep. | `MVP-CHARTER-v0_2.md:323-334`; `archiver/runner.py:27` |
    40	| F10 | market_reset 20:00–21:00 ET: gated writes raise `SessionBlocked`; the heartbeat died there 8 times because it caught the refusal instead of asking the clock first. | `heartbeat-blackout-2026-09-10.md`; `session/guard.py` |
    41	| F11 | `tunables.yaml` is re-read by `com.cobalt.aset`; a new `TunableUnit`/`Status`/`Source` value is the 09-09 sheet-outage class. | `jobs.yaml:67-69` (`taxonomy/loader.py:79`); `jobs/config.py:256-273` |
    42	| F12 | Resident + `supervisor: self` is a new shape; `should_keep_running` exists for "the S2 radar poller"; watchdog skips PID probes for `self`. | `wrapper.py:165-180`; `watchdog.py:369-383` |
    43	| F13 | Radar Screens note: four `##` sections of prose bullets, no fenced blocks; the Day Scan gate is prose. | vault note (read-only); day-open §4 C.4 |
    44	| F14 | `cobalt_dev` holds **0** bars; the replay session must be created in dev. | `select count(*) from system.bars` on cobalt_dev = 0 |
    45	| F15 | Sol: writes outside the worktree denied, commit denied, network on; no `psql`; psycopg→localhost UNVERIFIED; the worktree has no `.env`. | day-open §1.3; `ls .env` |
    46	| F16 | `data/` and `logs/` are gitignored. | `.gitignore:2,6`; `git check-ignore data/radar-cache/x.csv` |
    47	| F17 | `VaultWriter.upsert_unit` creates a missing section at a `Placement`; `create_if_absent` never rewrites an existing file; both refuse in market_reset. | `vaultwrite/writer.py:559-678` |
    48	
    49	## §2 Decisions
    50	
    51	### D1 — Sources: two vault notes, one parser (R1, R4)
    52	
    53	- **Screens** — `1 - Trading/Radar Screens.md` (exists). `ScreenBlock` (extra=forbid): `screen` (display name → key = snake slug, unique), `f` (grammar `^[a-z0-9_.]+(,[a-z0-9_.]+)*$`; `%`, `&`, `=`, `auth` refused), `sort` (`^-?[a-z0-9_]+$`), `columns` (list[int] 0–150, display only), `active_from` / `active_to` (`"HH:MM"` ET, from < to), `enabled` (bool).
    54	- **Lists (R4 choice)** — NEW note `1 - Trading/Radar Lists.md`. `ListBlock` (extra=forbid): `list` (key), `description`, `tickers` (uppercase, unique), `radar` (bool: pool source), `archive` (list[`Interval`], may be empty), `backfill_default` (exactly one true across blocks), `enabled`. One optional `ExcludeBlock` `{exclude: [tickers]}` → `excluded_by = manual`.
    55	- **Why a vault note, one path:** R1 already makes a note the truth for half the radar's inputs; the same parser, hashing, mirror and degradation code serve the other half with no new machinery. A `trader_settings`-only path would need a second editing surface (seed YAML + CLI) and split radar inputs across two homes. **Why a separate note:** ~260 tickers would bury his screen prose, and `create_if_absent` gives the lists write its own write_id without touching `Radar Screens.md`.
    56	- **Parser** (`cobalt.radar.notes`): reads the file bytes ONCE per check and hashes those bytes (no torn reads under Obsidian Sync). Only fenced ```` ```yaml ```` blocks are read; every yaml fence in a note must validate as that note's block type (a non-validating fence = a named parse failure, never skipped). Prose and `cobalt:` markers are ignored. Hashes: sha256 per block (fence body) + sha256 per note.
    57	- **Reload:** note sha256 compared each cycle; on change → re-parse → mirror.
    58	- **Mirror:** `"user".trader_settings` through the existing `TraderSettingsStore.put` (the one write path, `settings/store.py:60`). Keys `radar.note.screens`, `radar.note.lists`, `radar.screen.<key>`, `radar.list.<key>`, `radar.exclude`; value `{block, block_sha256, note_sha256, status: ok|parse_failed|removed, error}`; `source = vault:<note path>@<sha12>`. No new user-side table.
    59	- **Parse failure (R1):** the failed block contributes nothing; its mirror row → `parse_failed` (the DB never presents the previous version as current); pool row `degraded = true` naming the source; members whose every source is degraded are HELD; F18 `radar` RED naming the screen/list. Never an empty pool from a failure.
    60	- **R2 fixtures:** `tests/fixtures/radar/radar-screens.example.md` — exactly ONE synthetic screen, fenced format, `active_from: "10:00"` (exercises the gate); `tests/fixtures/radar/radar-lists.example.md` — synthetic lists (≥60 liquid large caps by rule, one ETF for `not_equity`, one `exclude`). The seed-parser test renders its prose input FROM the screen fixture, so no second screen definition exists. Suite test (content, not filenames): no tracked file under `src/cobalt/`, `configs/cobalt/`, `tests/cobalt/`, `ops/` or `docs/40 - DevDocs/` contains Finviz filter grammar (`f=` followed by `sh_|ta_|fa_|an_|cap_|exch_|geo_|idx_|ind_|sec_|news_|earningsdate_|ipodate_|targetprice_`) outside `tests/fixtures/radar/`. It also catches E5 if that report is committed unredacted.
    61	
    62	### D2 — The one-time seed write (R1 + R4): hub only, HITL-gated, last
    63	
    64	- `cobalt radar seed --dry-run` derives the four screen blocks deterministically from the note's prose: `f` from the "Export call (derived)" line's `f=` value, cross-checked equal to the backticked codes on the "Filters" line (mismatch → refuse); `sort` from the "Sort" bullet; `columns` from the columns bullet; `screen` from the heading after "—". `active_from: "10:00"` for Day Scan quotes its prose verbatim; any window the prose does not state is emitted as the radar's full active span from the session tunables and marked `# PROPOSED — no window stated in prose`. Every derived field carries a `# from: "<verbatim source line>"` comment. `enabled: true`.
    65	- Placement: each block goes after the last non-blank line of its own `##` section via `upsert_unit(section="radar-screen-<n>", unit_id="radar-screen:<key>", placement=…)`: 4 write_ids. Test: every pre-existing line byte-identical; the diff is insertions only.
    66	- Lists note: `create_if_absent` from a template rendered from `watchlists.yaml` — three blocks `tier_a / tier_b / tier_c` verbatim (description, tickers, intervals → `archive`, `radar: true`, `backfill_default` on `tier_a`), with the YAML header's derivation rules and flagged judgment calls carried as prose. 1 write_id.
    67	- Refusals: blocks already present (create-once); market_reset; `--apply` without `--hitl <token>`; `COBALT_ENV` not matching the target vault.
    68	- `--apply --hitl <token>` records the token as the writer `run_id`, prints each write_id and its `cobalt vault restore --write-id` line.
    69	- **The card** (hub-prepared): the dry-run unified diff + its sha256, the verbatim-source table per field, the PROPOSED windows, the `ft=4` comparison (E4), and the rollback lines. Approval = the token in Dejan's own words. Sol builds and tests the command against fixtures only; the real dry-run and apply are LIVE steps L6.
    70	
    71	### D3 — Tables: `db_migrations/0004_radar_pool.sql` (+ rollback)
    72	
    73	```
    74	system.radar_pool
    75	  pool_key         TEXT PRIMARY KEY CHECK (pool_key ~ '^[a-z0-9_]+$')
    76	  state            TEXT NOT NULL CHECK (state IN ('scanning','idle','paused_market_reset','stopped'))
    77	  degraded         BOOLEAN NOT NULL DEFAULT false
    78	  degraded_sources JSONB NOT NULL DEFAULT '[]'   -- [{source, reason, since}]
    79	  sources          JSONB NOT NULL DEFAULT '[]'   -- active source ids with sha12
    80	  session          TEXT NOT NULL                 -- F1 at last stamp
    81	  cap              INTEGER NOT NULL
    82	  members          INTEGER NOT NULL
    83	  last_scan_at     TIMESTAMPTZ
    84	  last_scan_ms     INTEGER
    85	  budget           JSONB                          -- {planned_rpm, limit_rpm}
    86	  updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
    87	
    88	system.radar_membership                           -- one row per EPISODE
    89	  id             BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    90	  pool_key       TEXT NOT NULL REFERENCES system.radar_pool(pool_key)
    91	  ticker         TEXT NOT NULL
    92	  trade_date     DATE NOT NULL                    -- ET
    93	  first_seen_at  TIMESTAMPTZ NOT NULL
    94	  entered_at     TIMESTAMPTZ                      -- NULL = never admitted
    95	  left_at        TIMESTAMPTZ
    96	  source         TEXT NOT NULL                    -- 'screen:<key>@<sha12>' | 'list:<key>@<sha12>' (best-ranked at first sight)
    97	  sources        JSONB NOT NULL                   -- every source id that listed it while open
    98	  rank_at_entry  INTEGER
    99	  excluded_by    TEXT CHECK (excluded_by IN ('config_cap','not_equity','screen_inactive','manual'))
   100	  session        TEXT NOT NULL                    -- F1 at first sight
   101	  CHECK (entered_at IS NOT NULL OR excluded_by IS NOT NULL)
   102	  CHECK (left_at IS NULL OR left_at >= first_seen_at)
   103	  UNIQUE INDEX (pool_key, ticker) WHERE left_at IS NULL
   104	  INDEX (trade_date, ticker)
   105	
   106	"user".aset_sizings  ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))
   107	                     ADD pool_member_id BIGINT REFERENCES system.radar_membership(id)
   108	"user".day_modes     ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))
   109	```
   110	
   111	- Episode rules: admitted → `entered_at`, `excluded_by` NULL. Dropped by cap / manual / window → `left_at` + `excluded_by`. Fell off every source → `left_at`, `excluded_by` NULL. Never admitted → `entered_at` NULL + `excluded_by`, closed when it stops being a candidate. Later admission of an excluded candidate closes that episode and opens an admitted one (J1 points at admitted episodes). First active cycle of a new trade date closes every open episode at the prior session end.
   112	- Ownership + grants: `OWNER TO cobalt_system` on both tables; `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`; `GRANT SELECT ON system.radar_pool TO cobalt_user`.
   113	- Nullable in P1: `pool_member_id` stays nullable forever (manual cards). `account_mode` NOT NULL is a later migration after E1 (the `aset 0004_session → 0005_session_not_null` precedent).
   114	- Rollback SQL: drop `pool_member_id`, both `account_mode` columns, `DROP TABLE system.radar_membership, system.radar_pool`. **Cost, stated:** membership history and account-mode stamps are lost; the L1 `pg_dump` is the belt.
   115	- **Rollback domain fix (F1):** `cobalt db migrate --rollback` REQUIRES `--down-to NNNN` and reverses only registered migrations newer than NNNN, newest first; without it, it refuses and lists targets. Round-trip test: `migrate → --rollback --down-to 0003 → migrate` gives identical digests, and 0003's columns survive the 0004 rollback. **Hardening verdict:** adopted; a whole-list rollback in prod is one keystroke from moving every table to `public`.
   116	
   117	### D4 — Pool job `com.cobalt.radar` (F2)
   118	
   119	- **Registry:** resident, `supervisor: self`, `timeout_s: 300`, `enabled: false` at merge (flipped in L11 after the first clean scan — `com.cobalt.herdr` precedent, `jobs.yaml:130-136`), `reads:` DERIVED by instrumenting one cycle's `open`/`read_text` (09-09 method), each entry citing file:line.
   120	- **Plist:** `uv run cobalt radar run`; `RunAtLoad true`; `KeepAlive {SuccessfulExit: false}` (a kill-switch exit 0 is not respawned; a crash is); `COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`; `logs/radar.{log,err}`. `ops/README.md` gains: after `cobalt resume`, `launchctl kickstart gui/$(id -u)/com.cobalt.radar`.
   121	- **Loop:** `job_run` wrapper; `should_keep_running` checked each cycle; one cycle per `radar.scan_interval`.
   122	- **Session gating (asked first, never caught):** F1 session ∉ `active_sessions` (radar.yaml: `premarket, rth, aftermarket`) → `idle`, no Finviz call, pool row stamped. `market_reset` → `paused_market_reset`: ZERO writes to pool, membership, bars or mirror; only the F17 job heartbeat stamps, as the heartbeat fix already does. The decision comes from `session_clock()` before the cycle starts, not from a caught `SessionBlocked` (F10). **A cycle is asked twice:** at start, and again immediately before its single commit (pool + membership in one transaction, then bars, then mirror). A cycle that started at 19:59:50 and would commit at 20:00:05 is dropped whole and logged; no partial write lands in the window.
   123	- **Fetch:** active screens = `enabled ∧ active_from ≤ now_et < active_to ∧ session active` → `GET /export/screener?v=152&f=<f>&o=<sort>&c=0,1,…,150`. Lists with `radar: true` → `GET /export/screener?v=152&t=<chunk>&c=0,…,150` chunked by `list_chunk_size`. Raw responses cached to `data/radar-cache/<trade_date>/<source_key>-<HHMMSS>.csv` (gitignored; retention in radar.yaml). Parsed by header NAME (`required_headers` in radar.yaml; a missing header = source failure). Token via `archiver.collector.resolve_token`; every string through `collector.scrub`.
   124	- **Decision (pure function, no I/O, table-tested):** (1) `exclude` block → `manual`; (2) `not_equity` rule (radar.yaml `{header, values}`; values OBSERVED in a recorded export, never guessed) → `not_equity`; (3) rank per radar.yaml `rank:` — P1 default (E2): screen hits desc → best screen position asc → Relative Volume desc → ticker asc, every list-only name after every screen name; (4) top `radar.pool_cap` admitted, rest `config_cap`; (5) a member whose only sources went inactive (window or `enabled: false`) leaves with `screen_inactive`, unless an active list still carries it; (6) a degraded source's members are held and not re-ranked; it adds no new names. Held members count against the cap FIRST: admissions fill only `pool_cap − held`, and a held member is never evicted to admit a new name, so the cap invariant holds while a source is down.
   125	- **Outage:** HTTP error / non-CSV body / header mismatch → that source degraded (named, `since`), pool row degraded, members held; clears on the next good fetch; F18 RED while degraded. Never an empty pool.
   126	- **Budget:** one token bucket per process for every Finviz call (screener + stock) at `radar.finviz_max_rpm`. `cobalt radar check` (dry-run config check) and `run` startup REFUSE when `cap × 60 / poll_interval + active screens + list chunks per minute > finviz_max_rpm`.
   127	
   128	### D5 — Finviz bar poller (same process)
   129	
   130	- After each pool step, for admitted members in rank order: `fetch_bars(ticker, Interval.I1, token)`; keep bars with `ts > watermark` (per ticker, seeded from `max(ts)` in `system.bars`) AND `ts + 1 min ≤ now` (closed bars only); `BarStore.upsert_bars` (one path, archiver schema; the 20:30 archiver finalizes the same keys identically).
   131	- **i1 → 2m:** pure `cobalt.archiver.aggregate.aggregate(bars, minutes)`, buckets floored from 00:00 ET, NOT stored. Stored `i2` stays Finviz's own from the archiver, so no key has two writers. Test on the replay day: aggregate(i1) vs archiver i2 → agreement % in the report; any systematic mismatch (bucket alignment, volume) → ESCALATE, never tuned away.
   132	- Cadence `radar.poll_interval` (60 s) → ≥2 polls per 2m bar.
   133	
   134	### D6 — Account-mode tag
   135	
   136	- `"user".day_modes.account_mode` set by `cobalt daymode account-mode live|sim [--date]` (market_reset-gated like every day-mode write). E1 rules the real flow.
   137	- `AsetStore` INSERT (`aset/store.py:109`) stamps `account_mode` from today's `day_modes` row. The card shows `LIVE`, `SIM`, or a loud `ACCOUNT MODE UNSET` badge. P1 never refuses a card on it (what the sheet accepts is unchanged).
   138	- `pool_member_id`: column + FK only; nothing writes it in P1 (S2-P2).
   139	
   140	### D7 — J1
   141	
   142	Suite: catalog proof that the FK on `"user".aset_sizings.pool_member_id` references `system.radar_membership(id)`. As `cobalt_user`: SELECT `system.radar_membership` OK, INSERT denied, an `aset_sizings` insert with a valid id OK and with an invalid id FK-fails. As `cobalt_system`: SELECT `"user".aset_sizings` denied.
   143	
   144	### D8 — `cobalt db query` (R3)
   145	
   146	- `cobalt db query --side user|system [--prod] [--format json|table] [--limit 1000] "<sql>"`. Connection = `db.connect(dbname, side=…)` (factory, `cobalt_app`, SET ROLE). `--prod` = `allow_prod=True` (RULING 7 tooling seam); otherwise `env.resolve_db_name()`. Lives in `src/cobalt/db_query.py`, registered under the existing `db` group (`db_migrations/cli.py:196`). No new `psycopg.connect`.
   147	- **Code guard (before the server):** a tokenizer aware of quotes, dollar-quotes and comments. Exactly one statement; first keyword `SELECT` or `WITH`. Refused anywhere as a bare word: INSERT UPDATE DELETE MERGE TRUNCATE CREATE ALTER DROP GRANT REVOKE COPY CALL DO SET RESET LOCK VACUUM ANALYZE REFRESH COMMENT LISTEN NOTIFY PREPARE EXECUTE DEALLOCATE DISCARD INTO, and `FOR UPDATE|SHARE|NO KEY UPDATE|KEY SHARE`. Functions `set_config pg_sleep pg_terminate_backend pg_cancel_backend pg_advisory_* lo_* dblink* pg_read_file pg_read_binary_file pg_ls_dir nextval setval` are refused. Refusal = exit 2 with one loud line naming the token.
   148	- **Belt:** `BEGIN READ ONLY`; `SET LOCAL statement_timeout` from tunable `db.query.timeout_s`; query wrapped `SELECT * FROM (<sql>) AS q LIMIT n` (a data-modifying CTE cannot sit in a subquery); always ROLLBACK; `current_user` asserted equal to the side role afterwards. Output passes through F19 redaction before print.
   149	- Tests: every refused class; keyword inside a string literal passes; multi-statement; data-modifying CTE; `set_config('role', …)` switch; user side reads `system.x` qualified; `cobalt_brain` without `--prod` refuses.
   150	
   151	### D9 — F18 `radar` probe
   152	
   153	`probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat` (`heartbeat/runner.py:83-107`). `enabled: false` → OK "NOT PROBED". No pool row → RED. `market_reset` → OK "paused". Inactive session → OK "idle (<session>)". Active session → RED when `now − last_scan_at > heartbeat.radar_max_age_s`; RED when degraded (each source + reason + since); RED when any mirror row is `parse_failed` (names the screen/list).
   154	
   155	### D10 — Config
   156	
   157	- `configs/cobalt/taxonomy/tunables.yaml`, EXISTING units/status/source values only (F11): `radar.pool_cap` 50 `count`; `radar.scan_interval` 60 `duration`; `radar.poll_interval` 60 `duration`; `radar.finviz_max_rpm` `count` (value from build step 1); `heartbeat.radar_max_age_s` 180 `duration`; `db.query.timeout_s` 30 `duration`. If no existing enum value fits a row → ESCALATE; do not add one.
   158	- NEW `configs/cobalt/radar.yaml` (Pydantic, extra=forbid; `cobalt radar check` = dry-run): `pool_key`, `notes {screens, lists}`, `active_sessions`, `export {v: 152, columns: 0-150, required_headers}`, `list_chunk_size`, `not_equity {header, values}`, `rank`, `cache {dir: data/radar-cache, retention_days}`.
   159	- `configs/cobalt/jobs.yaml`: the `com.cobalt.radar` row (D4).
   160	- Boundary: both new paths under `configs/cobalt/` (old loader glob is top-level only) — checked before adding, not after.
   161	
   162	### D11 — Stage 2: the archiver onto the Lists note; `watchlists.yaml` leaves
   163	
   164	- `archiver/config.py` builds its targets from the Lists note via `cobalt.radar.notes` (read + validate, NO mirror write — the archiver runs inside market_reset). `archive_targets` = sorted unique `(ticker, interval)` over enabled lists; `backfill_targets(t)` = the `backfill_default` list's intervals. Missing or failed note → loud failure (job `failed`, F18 red).
   165	- No archiver plist change: in production `resolve_vault_path()` returns the real vault from `COBALT_ENV=production` alone (`vault.py:159-160`), which the archiver plist already sets.
   166	- Sides: the archiver still opens only system-side DB stores (ADR-0008 D2 row unchanged); it reads one vault FILE. The radar job's D2 row: `RadarStore`, `BarStore`, `JobStore` → system; `TraderSettingsStore` (mirror) → user.
   167	- **Equality proof before delete:** `cobalt radar sources --archiver-diff --yaml-rev <sha>` prints `archive_targets` and `backfill_targets` from the note vs from `watchlists.yaml` at that git revision — must be empty. Fixture test in the suite; prod run in L8.
   168	- **Stage 2 commit** = archiver switch + test re-target + `git rm configs/cobalt/watchlists.yaml`, last on the branch. Its rollback = `git revert <stage2>`. It is separate because the 20:30 archiver needs the note, and the note exists only after L6, which needs stage-1 code on main.
   169	
   170	### D12 — Smoke (dev vault + cobalt_dev) — sprint acceptance
   171	
   172	| # | Check | Pass |
   173	|---|---|---|
   174	| S0 | Recorded session: `COBALT_ENV=dev uv run archiver --backfill <T>` for every fixture ticker (F14) | ≥1 full trading day of i1 + i2 in cobalt_dev; the day is named in the report |
   175	| S1 | `cobalt db migrate` on cobalt_dev; `--rollback --down-to 0003`; `migrate` | proof clean, radar tables CREATED, digests identical across the round-trip |
   176	| S2 | Replay `cobalt radar scan --replay <day> --from 04:00 --to 16:00` over cached screener CSVs built from the corpus by `cobalt radar replay-build <day>` (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions present; replay-only, named as such) | pool churns: ≥1 enter and ≥1 leave |
   177	| S3 | Cap | `max(open admitted members) ≤ radar.pool_cap` at every cycle (SQL over membership), including cycles with a degraded source |
   178	| S4 | Entry on RVOL | a name whose proxy RVOL crosses the fixture screen's threshold at T has `entered_at ≤ T + scan_interval` |
   179	| S5 | `excluded_by` | ≥1 row each of `config_cap`, `not_equity`, `screen_inactive`, `manual` |
   180	| S6 | Window gate | no episode with `source` = the fixture screen entered before 10:00 ET; ≥1 after |
   181	| S7 | market_reset | a cycle at 20:30 ET: row counts in pool, membership, bars, `trader_settings` unchanged; state `paused_market_reset`; no `SessionBlocked` in logs |
   182	| S8 | Degraded | fixture source → HTTP 500: pool row degraded, members held, probe RED naming it; broken block → mirror `parse_failed`, probe RED naming it |
   183	| S9 | Poller | member i1 bars upserted, closed bars only, watermark honoured; aggregate-vs-i2 agreement % reported |
   184	| S10 | Probe | `radar` OK fresh / RED stale in session / OK idle out of session |
   185	| S11 | Account mode + J1 | card stamped + badge rendered (`GET /` on a dev sheet); UNSET badge when day row NULL; J1 suite green |
   186	| S12 | Whole system | `uv run pytest tests/cobalt tests/taxonomy` green; `uv run cobalt validate` exit 0; `cobalt jobs readers` for every changed config path; R2 grep clean |
   187	| S13 | Stage 2 | archiver-diff empty on fixtures; `archiver --backfill` still works from the note |
   188	
   189	Sol runs the smoke against a worktree-local vault copy (`data/smoke-vault`, gitignored) because it cannot write `~/dev-vault-cobalt` (F15). The hub re-runs S1–S13 against `~/dev-vault-cobalt` + cobalt_dev as ground truth (L35).
   190	
   191	## §3 Houses and RESTARTS (R5)
   192	
   193	Build = `gpt-5.6-sol`, high effort, `-s workspace-write -c sandbox_workspace_write.network_access=true`, cannot commit. Hub = Sonnet: launch, wait, verify against ground truth, commit on branch. Gated vault write = hub, after approval.
   194	
   195	RESTARTS, derived by rule from the expected diff (Sol re-derives it from the real `git diff --name-status main...HEAD`):
   196	
   197	| Path (expected) | Rule | RESTART |
   198	|---|---|---|
   199	| `ops/com.cobalt.radar.plist` (A) | plist in diff | `com.cobalt.radar` — bootstrap (new) |
   200	| `configs/cobalt/taxonomy/tunables.yaml` (M) | in a resident's `reads:` → `com.cobalt.aset` (`jobs.yaml:69`, `taxonomy/loader.py:79`) | `com.cobalt.aset` kickstart |
   201	| `configs/cobalt/radar.yaml` (A) | only in radar's `reads:` | covered by the bootstrap |
   202	| `configs/cobalt/jobs.yaml` (M, and again in L11) | registry | `cobalt jobs register` |
   203	| `configs/cobalt/watchlists.yaml` (D, stage 2) | `cobalt jobs readers` → none (archiver is a one-shot) | none |
   204	| `src/**` incl. `db_migrations/0004*.sql` | code | none (the migration is LIVE step L3, not a restart) |
   205	| `tests/**`, `docs/**`, `ops/README.md` | tests/docs | none |
   206	| anything else | unclassified | ESCALATE, never dropped |
   207	
   208	## §4 Build step 1 — Finviz throttle re-measure (FIRST)
   209	
   210	- `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`. Names = the 50 synthetic-fixture tickers. Refuses 09:00–16:00 ET on trading days (his live session) and inside market_reset.
   211	- Per cycle: sequential `/export/stock?p=i1` for each name, then one screener call with the fixture filter. STOP at the first non-200, 429, redirect, non-CSV body or header mismatch.
   212	- Per stage: requests, achieved req/min, statuses, p50/p95 latency, bytes → `data/radar-throttle-<ts>.json` + a printed table.
   213	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`; the row's `consumers` cites the report. If the 10 s stage is clean, the report says "no throttle observed up to N req/min" (a floor, not a ceiling). Never extrapolate.
   214	- Token resolution fails in the sandbox → NOT RUN with the scrubbed error line; the hub runs the same command. Offline steps continue. READY FOR MERGE requires the number.
   215	
   216	## §5 NOT in P1
   217	
   218	Precondition evaluator (F8), dots / ladder (F10), radar panel, F3 rank display, F12 missed replay, F13 auto-archive. Writing `pool_member_id`. `account_mode NOT NULL`. Hysteresis at the cap. The four-list re-export (E3).
   219	
   220	## §6 LIVE block — named steps, one rollback domain each
   221	
   222	Window: trading-day 16:15–19:40 ET or a weekend daytime. Never 09:00–16:00, 20:00–21:30, 21:25–21:55 (backup), or 23:27–23:47 (generated commit).
   223	
   224	| Step | Action | Proof | Rollback (domain) |
   225	|---|---|---|---|
   226	| L0 PRECONDITIONS | heartbeat fix merged + deployed + green; branch rebased; suite green on the rebased head; report READY FOR MERGE; `git tag pre-s2-p1` on main | report + tag | — |
   227	| L1 SNAPSHOT | `uv run cobalt backup run` | restic id + dump printed | belt for DB + vault |
   228	| L2 CODE stage 1 | hub rebases the branch onto current main (the nightly generated commit moves main), then `git -C ~/cobalt merge --ff-only <stage1-sha>`; `git tag s2-p1-stage1` | `git log -1` | reset to `pre-s2-p1` + RESTARTS again (code) |
   229	| L3 DB | `uv run cobalt db migrate --allow-prod` | every existing table OK; radar tables CREATED | `cobalt db migrate --allow-prod --rollback --down-to 0003` (DB) |
   230	| L4 REGISTRY | `uv run cobalt validate`; `uv run cobalt jobs register` | exit 0; radar row `enabled: false` | re-register at the previous tag |
   231	| L5 RESTARTS stage 1 | `launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` | `curl -s :5010/api/health` → `ok:true`; next beat `sheet daymode` OK | kickstart again after the code rollback |
   232	| L6 VAULT (HITL) | hub, after approval: `COBALT_ENV=production uv run cobalt radar seed --dry-run` → diff sha256 == card's; then `--apply --hitl <token>` | 5 write_ids printed | `uv run cobalt vault restore --write-id <id>` ×5, or the L1 snapshot (vault) |
   233	| L7 SOURCES | `uv run cobalt radar sources` | every block `ok`; Day Scan `active_from "10:00"`; list counts == YAML counts | — |
   234	| L8 PROOF | `uv run cobalt radar sources --archiver-diff --yaml-rev HEAD` | empty diff | — |
   235	| L9 CODE stage 2 | `git merge --ff-only sprint-2/radar-pool`; `git tag s2-p1`; `cobalt jobs readers configs/cobalt/watchlists.yaml` | readers: none | `git revert <stage2-sha>` (source switch) |
   236	| L10 LAUNCHD | `cp ops/com.cobalt.radar.plist ~/Library/LaunchAgents/`; `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.radar.plist` | first cycle in `logs/radar.log`; `cobalt db query --prod --side system "select state, degraded, members, last_scan_at from radar_pool"` | `launchctl bootout gui/$(id -u)/com.cobalt.radar` (launchd) |
   237	| L11 ENABLE | `jobs.yaml` `enabled: true` on main; `cobalt jobs register` | registry | flip back + register |
   238	| L12 HEARTBEAT | next beat | GREEN, `radar` line present | — |
   239	| L13 NEXT SESSION | 04:00+ `scanning`; Day Scan: no episode before 10:00, sources list it active after; 20:00–21:00 radar row counts constant, no RED; 20:30 archiver exit 0, target count == prior night | `cobalt db query` + logs | per domain above |
   240	
   241	## §7 Risks
   242	
   243	| Risk | Mitigation |
   244	|---|---|
   245	| Finviz lockout on his Elite login (probe or poller) during trading | probe refuses 09:00–16:00; stop-on-first-error ramp; 0.5 safety factor; single token bucket; startup budget refusal |
   246	| Real screen data reaching the repo (reports, cache, fixtures) | cache under gitignored `data/`; reports name screens by key only, never `f=`; R2 grep + suite test |
   247	| Rebase conflicts with the heartbeat fix | expected in `db_migrations/__init__.py`, `db_migrations/cli.py` (digest list), `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`, `test_jobs.py` — rebase first, never after |
   248	| First resident + `self`: zombie path unexercised | watchdog test: stale heartbeat → `zombie`; plist unloaded → RED |
   249	| i1 export ~9.4k rows × 50 names per poll = parse cost | watermark filter before model build; `last_scan_ms` on the pool row; smoke reports p95 cycle ms |
   250	| Cap-boundary oscillation → episode churn | smoke reports episodes/day; hysteresis is E2's ruling |
   251	| Cache growth (~7k CSVs per trading day) | retention in radar.yaml; smoke measures bytes/day |
   252	| Finviz serves `p=i2` natively (DATA-SOURCE-MEMO A.2.1), so i1→2m aggregation may disagree with Finviz's own 2m bars | ruled i1→2m kept; the S9 agreement % against archived i2 decides; a systematic mismatch is ESCALATE, not a silent switch |
   253	| A cycle straddling 20:00 ET | second session check before commit; dropped whole (D4) |
   254	| Sol cannot reach cobalt_dev or has no DB env | the hub exports DB env from `~/cobalt/.env` at launch (never printed); DB tests Sol cannot run are reported NOT RUN, and the hub runs them |
   255	
   256	## §8 ESCALATE
   257	
   258	```
   259	ESCALATE:
   260	E1 ACCOUNT MODE SOURCE — no live/sim value exists anywhere (day_modes, trader_settings, configs).
   261	   P1 adds nullable day_modes.account_mode + a CLI setter, stamps cards, shows a loud UNSET badge,
   262	   never refuses a card. Rule: who sets it and when (sheet day-mode step?), and must an UNSET card be refused.
   263	E2 POOL RANK AT THE CAP — today's static tiers alone (~260 names) exceed pool_cap 50 five-fold, so the
   264	   rank rule chooses the pool every minute. P1 default: screen names first (hits, screen position), then
   265	   list names by RVOL, ticker tie-break, no hysteresis. Selection logic: rule it or replace it.
   266	E3 FOUR LISTS NOT RECOVERABLE — watchlists.yaml holds 3 derived tiers, not Green/Red/SMB Daily Watch/
   267	   Watchlist. P1 migrates the tiers verbatim (source = list:tier_a…). Re-export the four lists into the
   268	   Lists note if membership must name them.
   269	E4 ft=4 DROPPED BY THE R1 KEY LIST — 3 of 4 pasted URLs carry it; meaning unverified. The card shows
   270	   ticker sets with vs without ft=4 per screen; any difference needs an `ft` key added to R1's contract.
   271	E5 USER DATA IN AN UNCOMMITTED REPORT — docs/40 - DevDocs/reports/day-open-2026-09-10.md §2 C.1 quotes
   272	   all four screens' full f= strings and columns; it commits at day close → L32 breach. Redact first.
   273	E6 R5 RULE GAP — "code → none" leaves a resident on stale code whenever no reads: file changes (here the
   274	   sheet's account-mode stamp/badge). P1 is covered only because tunables.yaml restarts the sheet anyway.
   275	   Rule: does a code change under a resident's import tree restart it.
   276	```
   277	
   278	## §9 DISSENT
   279	
   280	No review round completed, so there are no reviewer objections to adopt or decline.
   281	
   282	- **Round 1 FAILED:** `codex exec -m gpt-6-astra` hit "You've hit your usage limit … try again at 11:31 AM" after 72,175 tokens. The model read the plan, ADR-0008, DATA-SOURCE-MEMO, `db_migrations/`, `jobs/wrapper.py`, `jobs/watchdog.py` and `daymode/store.py`, then stopped without issuing any BLOCKER, RISK or VERDICT. Capture: `plan-s2-p1-astra-r1.md`.
   283	- Its last progress message named three boundaries it was about to check: disabled-job startup, scans crossing market_reset, held members vs the pool cap. The architect checked them without the reviewer. The last two were real gaps and are fixed in D4 and D12 S3. The first holds: `job_run` does not read `enabled` (`wrapper.py:122-162`).
   284	- **Rounds 2–3:** not run. Codex has one shared five-hour pool (`limit_id codex`, day-open §1.4), the same pool Sol builds on. The hub should run the review command (same prompt, same capture path pattern) after the reset and BEFORE launching Sol. Objections left after round 3 are added here, one line each.
   285	
   286	=== RULINGS ADDENDUM 2026-09-10 (Dejan) ===
   287	E1 Account mode: standing value `live` in "user".trader_settings; a per-day `sim` switch on the morning sheet-attestation control (same control that attests the .htk sheet, one extra tap) writes day_modes.account_mode for that day only; every card is stamped from day override → standing value; a card with no value is REFUSED, loud — never stamped UNSET and let through.
   288	E2 Pool rule — lives in the vault note beside the screens (user data, L32), read by the collector like the screen blocks:
   289	```yaml
   290	pool:
   291	  cap: 50
   292	  priority: [screens, lists]
   293	  rank_metric:
   294	    premarket: volume        # 04:00–09:30 via the F1 session clock
   295	    rth: rvol                # 09:30 onward
   296	  overrides:
   297	    morning_low_float: volume      # this screen ranks by volume in every session
   298	    day_scan_after: "10:00"        # Day Scan takes first priority among screens after 10:00
   299	  stickiness_scans: 3              # out of the top 50 for 3 consecutive scans before dropping
   300	```
   301	Names not admitted get a membership row with `excluded_by = config_cap`.
   302	E3 Static lists: move the three merged tiers as they are; membership `source` names the tier. Named-list attribution comes later, if he re-exports the four TV lists into the vault.
   303	E4 `ft=4`: the HITL card shows each screen's ticker set with and without `ft=4`; any difference → `ft` joins the block contract; no difference → dropped.
   304	E5 User data in reports: before ANY commit, replace the four screens' `f=` strings in every report, plan and review file with "see vault note"; add a repo-wide grep for those strings to the report's checklist.
   305	E6 RESTARTS rule: plist in diff → that job; changed file in a resident's `reads:` → that resident; any src/ change → every resident whose entrypoint imports the changed module (static import walk in the report); unproven → all residents; unclassified path → ESCALATE, never dropped.
   306	E7 Credentials: NO DB credentials in Sol's environment or the worktree during the build. Sol runs everything that needs no DB; the hub runs the DB-backed suite, migrations on cobalt_dev, and the dev-vault smoke.
   307	E8 The R1 vault write (four YAML blocks + pool block into `1 - Trading/Radar Screens.md`) is NOT part of the build: Sol writes the parser, the synthetic fixture and a `cobalt radar screens propose` command that prints the proposed blocks + the ft=4 comparison. The hub runs the proposal at LIVE time; Dejan approves the HITL card; only then does the writer write.
   308	=== END ADDENDUM ===
     1	# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`
     2	
     3	You build S2-P1 (radar pool + Finviz bar poller) in this worktree. Everything you need is in this
     4	file. The plan it implements is `docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md`,
     5	in this worktree. Where the two disagree, the plan wins; say so in the report.
     6	
     7	## 0. Who does what
     8	
     9	| House | Does | Cannot |
    10	|---|---|---|
    11	| **You (Sol)**, high effort, `-s workspace-write`, network on | write code, tests, docs, the report, inside this worktree | commit, rebase, write outside the worktree, touch the real vault or `cobalt_brain` |
    12	| **Hub (Sonnet)** | launches you, verifies against ground truth, commits per step on `sprint-2/radar-pool`, runs what your sandbox cannot | build |
    13	| **Dejan** | approves the HITL card | — |
    14	
    15	**Hub, before launching you:** (1) if `ops/heartbeat-market-reset` has merged to main, rebase this
    16	branch onto main first; (2) if the plan's §9 says the Astra review loop has not run, run it and fold
    17	fixes into the plan before launch; (3) export the dev DB credentials into your environment without
    18	printing them.
    19	
    20	**Two runs.** RUN A = steps 0–13 (stage 1). Stop, print `DONE`. The hub commits stage 1, then
    21	relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
    22	Step G is **hub only, after Dejan's approval** — you never run it.
    23	
    24	**Stop rules.** A step you cannot finish → mark it `NOT RUN` or `FAILED` in the report with the
    25	exact error line (scrubbed), then continue with the steps that do not depend on it. Never mark a
    26	test passing that did not run. 3 failed attempts at the same thing → stop that step, ESCALATE.
    27	Print `DONE` as the very last line of every run, nothing after it.
    28	
    29	## 1. Laws (binding — a violation is a failed step)
    30	
    31	1. **Production is sacred (NN#16).** Dev only: `COBALT_ENV=dev`, database `cobalt_dev`, vault =
    32	   `data/smoke-vault` (gitignored copy you make of `~/dev-vault-cobalt`). Never open
    33	   `/Users/cobalt/Vault/Think`. Never connect to `cobalt_brain`. Never `launchctl` anything.
    34	2. **User data never enters the repo (L32).** No real screen, filter string, list or dollar figure in
    35	   any tracked file, report, fixture, test or log line you paste. The repo ships exactly ONE synthetic
    36	   example screen (R2).
    37	3. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error
    38	   string passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
    39	4. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent
    40	   fallback, no plausible-empty artifact, no default invented for a missing value.
    41	5. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
    42	   `archiver.collector.fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
    43	   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
    44	   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`.
    45	6. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted
    46	   (`psycopg.sql.Identifier` in Python); cross-side SQL is schema-qualified (`system.radar_membership`);
    47	   every new table is on a side in `src/cobalt/db_migrations/placement.py` or the suite fails.
    48	7. **Config-as-code.** Pydantic schema per config file, `extra="forbid"`, dry-run command. New-core
    49	   config lives only under `configs/cobalt/` (never `configs/*.yaml` top level).
    50	8. **Tunables.** Thresholds are `configs/cobalt/taxonomy/tunables.yaml` rows. Use EXISTING
    51	   `TunableUnit` / `TunableStatus` / `TunableSource` values only — adding an enum value breaks the
    52	   live ASET sheet (09-09 outage). No fitting value → ESCALATE.
    53	9. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE writing; never rely on catching
    54	   `SessionBlocked`. Radar writes nothing in that window.
    55	10. **Tools fetch, code computes.** No LLM anywhere in P1. All numbers are deterministic code.
    56	11. **Tests per step.** `uv run pytest` for the step's tests before moving on; the whole suite at
    57	    step 13.
    58	12. **Names.** One name per concept across SQL, Python, config and docs (`radar_pool`,
    59	    `radar_membership`, `account_mode`, `pool_member_id`, `excluded_by`).
    60	
    61	## 2. Rulings you implement (09-10, binding)
    62	
    63	- **R1 Radar Screens contract.** Vault note `1 - Trading/Radar Screens.md` gets one fenced YAML block
    64	  per screen: `screen, f, sort, columns, active_from, active_to (session clock, ET), enabled`. It is
    65	  written ONCE, through the vault writer, under ONE HITL card, prose untouched. After that Cobalt only
    66	  reads the note: parse fenced blocks only, reload on file-hash change, mirror each block + hash into
    67	  `"user".trader_settings`; `radar_membership.source` names screen + hash. Parse failure → pool row
    68	  degraded + heartbeat `radar` probe RED naming the screen; never the previous version silently. Day
    69	  Scan is active from 10:00 ET via the F1 session clock — a field, never code.
    70	- **R2 Synthetic example screen.** Exactly one, same fenced format, as the test fixture under
    71	  `tests/fixtures/`; real screens never enter the repo. `git ls-files | grep -i radar` stays clean of
    72	  user data.
    73	- **R3 `cobalt db query`.** Read-only CLI: factory connection, SET ROLE per side, SELECT-only enforced in
    74	  code (reject anything else, loud), output JSON/table. The workers' DB read path.
    75	- **R4 Static lists are user data.** They move user-side by the same mechanism as R1. Plan choice: a new
    76	  vault note `1 - Trading/Radar Lists.md` with fenced blocks. The archiver keeps working through the
    77	  migration (stage 2).
    78	- **R5 Houses + RESTARTS by rule.** plist in diff → that job; changed file in a resident's `reads:` →
    79	  that resident; registry → `register`; code/tests/docs → none; anything unclassified → ESCALATE.
    80	
    81	## 3. Environment
    82	
    83	- Run everything from this worktree with `uv run …`. Tests: `uv run pytest tests/cobalt tests/taxonomy`.
    84	- DB env: the hub exports the Postgres credentials into your environment at launch. If a DB-backed test
    85	  or command fails to connect, record `NOT RUN (db unreachable: <scrubbed error>)` and continue.
    86	- No `psql` on this host. Before step 3 lands, reach the DB only through repo code; after it lands, use
    87	  `uv run cobalt db query --side system|user "<select>"`.
    88	- Finviz token: `cobalt.archiver.collector.resolve_token()`. If it fails in your sandbox, the live half
    89	  of step 1 is `NOT RUN`; the hub runs it.
    90	- Vault for smoke: `cp -R ~/dev-vault-cobalt data/smoke-vault` once, then
    91	  `COBALT_VAULT_PATH=$PWD/data/smoke-vault`. `data/` and `logs/` are gitignored — confirm with
    92	  `git check-ignore` before writing anything there.
    93	- DevDocs layout: one page per `.py` file at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
    94	  `docs/40 - DevDocs/tests/cobalt/<file>.md`, and a line in `docs/40 - DevDocs/INDEX.md`.
    95	
    96	## 4. Build steps
    97	
    98	Each step lists its files, then the tests that must pass before the next step starts.
    99	
   100	### Step 0 — Base check (no code)
   101	- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql`. Present → the heartbeat fix is in
   102	  your base; build on it. Absent → build on main as is, register 0004 after 0002, and list in the report
   103	  the files that will conflict at merge: `db_migrations/__init__.py`, `db_migrations/cli.py`,
   104	  `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`,
   105	  `tests/cobalt/test_jobs.py`.
   106	- Record `git rev-parse HEAD` in the report.
   107	
   108	### Step 1 — Finviz throttle re-measure (FIRST)
   109	- `src/cobalt/radar/throttle.py` + `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`.
   110	- Names = the 50 first tickers of the synthetic lists fixture (step 5 creates it; create that fixture
   111	  file now if needed).
   112	- Refuses on trading days between 09:00 and 16:00 ET, and inside market_reset (use `session_clock()` and
   113	  the NYSE calendar).
   114	- Per cycle: sequential `fetch_bars(t, Interval.I1, token)` for each name, then one
   115	  `/export/screener?v=152&f=<fixture f>&c=0,…,150` call. STOP at the first non-200, 429, redirect,
   116	  non-CSV body or header mismatch.
   117	- Per stage record: requests, achieved req/min, status counts, p50/p95 latency ms, bytes. Write
   118	  `data/radar-throttle-<UTC ts>.json` and print a table.
   119	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`. If every stage was clean, write
   120	  "no throttle observed up to N req/min". Never extrapolate.
   121	- **Tests (mocked HTTP):** stop-on-first-error per class; refusal inside the forbidden window; rpm math;
   122	  token never appears in output (assert `auth=REDACTED`).
   123	- **Live run:** allowed only outside the forbidden window. Otherwise, or on token failure, `NOT RUN`.
   124	
   125	### Step 2 — Migration 0004, rollback bound, placement, J1
   126	- `src/cobalt/db_migrations/0004_radar_pool.sql` and `0004_radar_pool.rollback.sql` with exactly the
   127	  plan's §D3 DDL. Tables are created schema-qualified, `OWNER TO cobalt_system`;
   128	  `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`;
   129	  `GRANT SELECT ON system.radar_pool TO cobalt_user`. The rollback header states its cost.
   130	- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring lines.
   131	- `db_migrations/cli.py`: the digest excludes `account_mode` and `pool_member_id` (extend the heartbeat
   132	  fix's `DIGEST_EXCLUDED_COLUMNS` if present; otherwise generalize `TENANCY_COLUMN` into that tuple).
   133	  `--rollback` REQUIRES `--down-to NNNN`; it reverses only registered migrations newer than NNNN, newest
   134	  first; without it, it refuses and lists targets.
   135	- `placement.py`: move `radar_pool`, `radar_membership` out of `DECLARED_TABLES` into a new
   136	  `CREATED_TABLES` dict ("created by a db_migration directly on its side"), included in `PLACEMENT` and
   137	  in the proof table; extend the SQL/Python agreement test to 0004.
   138	- **Tests** (`tests/cobalt/test_tenancy.py`, `tests/cobalt/test_radar_migration.py`):
   139	  migrate twice idempotent; `migrate → --rollback --down-to 0003 → migrate` digests identical;
   140	  0003's columns (if present) survive the 0004 rollback; `--rollback` without `--down-to` refuses;
   141	  placement test green; J1 — FK catalog proof, `cobalt_user` SELECT OK / INSERT denied on
   142	  `system.radar_membership`, valid id insert OK / invalid FK-fails, `cobalt_system` SELECT on
   143	  `"user".aset_sizings` denied; membership CHECKs (`entered_at IS NOT NULL OR excluded_by IS NOT NULL`)
   144	  and the partial unique index reject bad rows.
   145	
   146	### Step 3 — `cobalt db query` (R3)
   147	- `src/cobalt/db_query.py`, registered as `db query` in `db_migrations/cli.py`'s `db` group.
   148	- `--side user|system` (required), `--prod` (`allow_prod=True`), `--format json|table`, `--limit`
   149	  (default 1000). Connection = `db.connect(dbname, side=…)`.
   150	- The guard and the belt exactly as plan §D8 (tokenizer aware of quotes, dollar-quotes and comments;
   151	  single SELECT/WITH; refused words and functions; `BEGIN READ ONLY`; `SET LOCAL statement_timeout`
   152	  from tunable `db.query.timeout_s`; `SELECT * FROM (<sql>) AS q LIMIT n`; always ROLLBACK;
   153	  `current_user` asserted; output through F19 redaction).
   154	- **Tests** (`tests/cobalt/test_db_query.py`): each refused class exits 2 with the token named; a
   155	  keyword inside a string literal passes; multi-statement refused; data-modifying CTE refused;
   156	  `set_config('role', …)` refused; user side reads `system.bars` qualified; `cobalt_brain` without
   157	  `--prod` refuses (no connection attempted); the `psycopg.connect` lint still passes.
   158	
   159	### Step 4 — Config
   160	- `configs/cobalt/radar.yaml` + `src/cobalt/radar/config.py` (Pydantic, `extra="forbid"`): `pool_key`,
   161	  `notes {screens: "1 - Trading/Radar Screens.md", lists: "1 - Trading/Radar Lists.md"}`,
   162	  `active_sessions [premarket, rth, aftermarket]`,
   163	  `export {v: 152, columns: "0-150", required_headers: [...]}`, `list_chunk_size`,
   164	  `not_equity {header, values}`, `rank`, `cache {dir: data/radar-cache, retention_days}`.
   165	- `required_headers` and the `not_equity` values come from a REAL recorded export header (step 6
   166	  captures one) — until then mark them `# UNVERIFIED` and a test asserts they are replaced before step 13.
   167	- `tunables.yaml` rows: `radar.pool_cap` 50 count; `radar.scan_interval` 60 duration;
   168	  `radar.poll_interval` 60 duration; `radar.finviz_max_rpm` count (step 1 value);
   169	  `heartbeat.radar_max_age_s` 180 duration; `db.query.timeout_s` 30 duration. Mirror the neighbouring
   170	  rows' `scope/dynamic/status/source/consumers` shape.
   171	- `cobalt radar check`: validates radar.yaml + tunables, and REFUSES when
   172	  `pool_cap × 60 / poll_interval + max active screens + list chunks per minute > finviz_max_rpm`.
   173	- **Tests** (`tests/cobalt/test_radar_config.py`): bad key crashes naming the file; budget refusal; every
   174	  new tunable resolves; `load_tunables()` still validates (the ASET sheet reads this file).
   175	
   176	### Step 5 — Notes parser, fixtures, mirror (R1, R2, R4)
   177	- `src/cobalt/radar/models.py` (`ScreenBlock`, `ListBlock`, `ExcludeBlock`, `SourceSet`, `ExcludedBy`),
   178	  `src/cobalt/radar/notes.py` (plan §D1): read bytes once, hash those bytes, fenced ```` ```yaml ````
   179	  blocks only, every yaml fence must validate, sha256 per block and per note, key slugs unique.
   180	- Mirror via `TraderSettingsStore.put`: keys `radar.note.screens`, `radar.note.lists`,
   181	  `radar.screen.<key>`, `radar.list.<key>`, `radar.exclude`; value
   182	  `{block, block_sha256, note_sha256, status: ok|parse_failed|removed, error}`;
   183	  `source = vault:<note path>@<sha12>`. Writes only when the note hash changed. Never writes inside
   184	  market_reset.
   185	- Fixtures: `tests/fixtures/radar/radar-screens.example.md` — ONE synthetic screen (`screen: Example
   186	  Session Scan`, synthetic `f`, `active_from: "10:00"`, `active_to: "16:00"`, `enabled: true`, a short
   187	  prose paragraph around it). `tests/fixtures/radar/radar-lists.example.md` — synthetic lists: ≥60
   188	  large-cap tickers (rule: well-known index heavyweights, not copied from any file in this repo), one
   189	  ETF (for `not_equity`), one `exclude` block, `archive` intervals, exactly one `backfill_default`.
   190	- **Tests** (`tests/cobalt/test_radar_notes.py`): fixture parses; each field's validation failure names
   191	  the block; a non-validating yaml fence is a named failure; prose/markers ignored; hash stable across
   192	  re-reads and changes on a one-byte edit; parse failure → mirror row `parse_failed`, never the old
   193	  block; `TraderSettings.from_db()` returns identically with the radar rows present (the sheet cannot
   194	  break); R2 test (file CONTENTS): no tracked file under `src/cobalt/`, `configs/cobalt/`,
   195	  `tests/cobalt/`, `ops/` or `docs/40 - DevDocs/` contains `f=` followed by
   196	  `sh_|ta_|fa_|an_|cap_|exch_|geo_|idx_|ind_|sec_|news_|earningsdate_|ipodate_|targetprice_`,
   197	  outside `tests/fixtures/radar/` (use `git ls-files` for the tracked set).
   198	
   199	### Step 6 — Screener collector, cache, replay
   200	- `src/cobalt/radar/collector.py`: `ScreenerCollector` protocol; `FinvizScreenerCollector` —
   201	  `GET https://elite.finviz.com/export/screener?v=152&f=<f>&o=<sort>&c=0,…,150` for screens and
   202	  `…&t=<chunk>&c=…` for lists; one process-wide token bucket at `radar.finviz_max_rpm` shared with the
   203	  poller; raw CSV cached to `data/radar-cache/<trade_date>/<source_key>-<HHMMSS>.csv`; parse by header
   204	  NAME; missing header / non-CSV / HTTP error → `SourceFailure` (named, never an empty list); every
   205	  string scrubbed.
   206	- Capture ONE real export header with the fixture filter (if network + token work) and pin
   207	  `required_headers` + `not_equity` from it; cite the capture file in the report (the header row only,
   208	  no data rows pasted).
   209	- `src/cobalt/radar/replay.py`: `ReplayCollector` serving cached CSVs by virtual clock, and
   210	  `cobalt radar replay-build <day>` that synthesizes snapshots from `system.bars` i1 in cobalt_dev
   211	  (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions
   212	  present; supports only the fixture screen's filter codes; any other code fails loud). Named
   213	  replay-only in its docstring.
   214	- **Tests** (`tests/cobalt/test_radar_collector.py`): recorded-CSV parse; header mismatch → failure;
   215	  HTML body → failure; `t=` chunking; token bucket pacing (fake clock); cache path under a gitignored
   216	  dir; scrub.
   217	
   218	### Step 7 — Pool decision + store
   219	- `src/cobalt/radar/pool.py`: a pure function `decide(candidates, open_members, sources, cfg, now) →
   220	  transitions`, no I/O, implementing plan §D4 steps 1–6 (manual, not_equity, rank, cap, screen_inactive,
   221	  degraded sources held).
   222	- `src/cobalt/radar/store.py`: `RadarStore` (`SIDE = Side.SYSTEM`) — pool row upsert, membership
   223	  episodes per plan §D3 (open, admit, exclude, leave, trade-date rollover), all transitions of one
   224	  cycle in ONE transaction.
   225	- **Tests** (`tests/cobalt/test_radar_pool.py`, `test_radar_store.py`): table tests for every rule and
   226	  every `excluded_by` value; cap never exceeded; rank tie-break deterministic; a degraded source's
   227	  members held AND counted against the cap first (admissions fill only `pool_cap − held`; a held member
   228	  is never evicted); re-admission closes the excluded episode and opens a new one; rollover closes the prior
   229	  day; store-side lint (own side or qualified).
   230	
   231	### Step 8 — Bar poller + aggregation
   232	- `src/cobalt/radar/poller.py`: for admitted members in rank order, `fetch_bars(t, Interval.I1, token)`
   233	  through the shared token bucket; keep `ts > watermark` (seeded from `max(ts)` per ticker in
   234	  `system.bars`) and `ts + 1 min ≤ now`; `BarStore.upsert_bars`.
   235	- `src/cobalt/archiver/aggregate.py`: pure `aggregate(bars, minutes)`, buckets floored from 00:00 ET,
   236	  OHLCV rules explicit. Never stored.
   237	- **Tests** (`tests/cobalt/test_radar_poller.py`, `test_archiver_aggregate.py`): watermark; open bar
   238	  excluded; upsert idempotent; aggregation on hand-built bars incl. a DST day and a missing minute; an
   239	  agreement check vs stored `i2` on the replay day (DB test) printing the % — any systematic mismatch
   240	  goes to ESCALATE, not a tweak.
   241	
   242	### Step 9 — Resident runner, registry, plist
   243	- `src/cobalt/radar/runner.py` + `cobalt radar run` / `cobalt radar scan --once [--replay <day>
   244	  --from HH:MM --to HH:MM]`: `job_run("com.cobalt.radar")`; `should_keep_running` each cycle; session
   245	  asked FIRST (plan §D4): inactive → `idle`; market_reset → `paused_market_reset` with ZERO radar writes;
   246	  otherwise reload notes → fetch → decide → store → poll bars; one cycle per `radar.scan_interval`;
   247	  `last_scan_ms` stamped. The session is asked AGAIN immediately before the cycle's commit; a cycle
   248	  whose commit would land in market_reset is dropped whole and logged.
   249	- `configs/cobalt/jobs.yaml`: `com.cobalt.radar` — resident, `supervisor: self`, `timeout_s: 300`,
   250	  `enabled: false`, `reads:` derived by instrumenting one `scan --once` (patch `open` / `Path.read_text`
   251	  and record repo-relative paths), each entry with a `# file.py:line (loader)` comment.
   252	- `ops/com.cobalt.radar.plist`: `ProgramArguments` `/Users/cobalt/.local/bin/uv run cobalt radar run`;
   253	  `WorkingDirectory /Users/cobalt/cobalt`; `RunAtLoad true`; `KeepAlive {SuccessfulExit false}`;
   254	  `COBALT_ENV production`; `COBALT_VAULT_PATH /Users/cobalt/Vault/Think`; `PATH` as the archiver plist;
   255	  logs `logs/radar.log` / `logs/radar.err`. No double hyphen inside XML comments.
   256	- `ops/README.md`: radar handover + "after `cobalt resume`, `launchctl kickstart
   257	  gui/$(id -u)/com.cobalt.radar`".
   258	- **Tests** (`tests/cobalt/test_radar_runner.py`, `test_jobs.py`): market_reset cycle writes nothing
   259	  (row counts); a cycle started at 19:59:50 ET with a fake clock that reaches 20:00:05 at commit writes
   260	  nothing; idle cycle makes no HTTP call; kill switch → clean exit 0; `uv run cobalt validate`
   261	  exit 0 (registry ↔ plist); watchdog: stale heartbeat on this resident → `zombie`.
   262	
   263	### Step 10 — F18 `radar` probe
   264	- `probes.radar(now)` in `src/cobalt/heartbeat/probes.py`, added to `take_beat` in
   265	  `heartbeat/runner.py`, exactly plan §D9.
   266	- **Tests** (`tests/cobalt/test_heartbeat.py`): each branch (not probed / no row / paused / idle / fresh /
   267	  stale / degraded names sources / parse_failed names the screen).
   268	
   269	### Step 11 — Account-mode tag
   270	- `"user".day_modes.account_mode` setter: `cobalt daymode account-mode live|sim [--date YYYY-MM-DD]`,
   271	  market_reset-gated like the other day-mode writes.
   272	- `aset/store.py` INSERT stamps `account_mode` from today's `day_modes` row; `aset/web.py` renders a
   273	  `LIVE` / `SIM` / `ACCOUNT MODE UNSET` badge on every card. No card is refused because of it.
   274	- **Tests** (`test_daymode.py`, `test_aset_store.py`, `test_aset_web.py`): setter gated; stamp from the
   275	  row; NULL → UNSET badge; existing card flows unchanged (whole aset test files green).
   276	
   277	### Step 12 — Seed command (fixtures and smoke vault ONLY)
   278	- `src/cobalt/radar/seed.py` + `cobalt radar seed --dry-run | --apply --hitl <token> [--only
   279	  screens|lists]` per plan §D2: prose → blocks with `# from:` verbatim-source comments and
   280	  `# PROPOSED` markers; `upsert_unit` per screen section; `create_if_absent` for the Lists note rendered
   281	  from `configs/cobalt/watchlists.yaml`; create-once refusal; market_reset refusal; `--apply` without
   282	  `--hitl` refuses; prints write_ids + restore lines; `--probe-ft` compares each screen's ticker set with
   283	  and without `ft=4` (hub use).
   284	- **You run it only with `COBALT_VAULT_PATH=$PWD/data/smoke-vault`.** Its prose input is rendered from
   285	  the screen fixture inside the test — no second screen definition.
   286	- **Tests** (`tests/cobalt/test_radar_seed.py`): every pre-existing line byte-identical, diff is
   287	  insertions only; `f` mismatch between the export line and the filters line refuses; the lists note
   288	  round-trips to the same targets as the YAML; second apply refuses; `restore` by write_id returns the
   289	  original bytes.
   290	
   291	### Step 13 — Smoke + report (end of RUN A)
   292	- Run plan §D12 S0–S12 against `data/smoke-vault` + `cobalt_dev` (S0 = `COBALT_ENV=dev uv run archiver
   293	  --backfill <T>` for each synthetic list ticker; it writes only to cobalt_dev). One row per check:
   294	  PASS/FAIL/NOT RUN + the evidence command and its key output line.
   295	- Whole suite: `uv run pytest tests/cobalt tests/taxonomy` (count passed/failed/skipped);
   296	  `uv run cobalt validate`; `uv run cobalt radar check`; `git ls-files | grep -i radar` listing.
   297	- DevDocs page for every new or changed `.py` (layout in §3) + INDEX lines.
   298	- RESTARTS: derive from `git diff --name-status main...HEAD` plus untracked files (`git status
   299	  --porcelain`), one row per path, by the R5 rule, using `uv run cobalt jobs readers <path>` for every
   300	  changed config path. Unclassified → ESCALATE.
   301	- Write the report (§5). Print `DONE`.
   302	
   303	### Step 14 — RUN B: stage 2 (archiver onto the Lists note)
   304	- `archiver/config.py` reads targets from the Lists note via `cobalt.radar.notes` (read + validate only,
   305	  no mirror write); `archive_targets` / `backfill_targets` per plan §D11; missing or failed note → loud.
   306	- `cobalt radar sources [--json] [--archiver-diff --yaml-rev <sha>]`.
   307	- Tests re-targeted to the lists fixture; `git rm`-equivalent: delete `configs/cobalt/watchlists.yaml`
   308	  from the working tree (the hub commits the deletion).
   309	- **Tests:** render a Lists note FROM `configs/cobalt/watchlists.yaml` at RUN A's commit (the hub gives
   310	  you the sha) with the step-12 seed code into `data/smoke-vault`; archiver-diff between that note and
   311	  the YAML at the same sha is empty (the synthetic lists fixture is NOT the comparison — it is different
   312	  data by design); `archiver --backfill <T>` works from the note on cobalt_dev; the whole suite green.
   313	- Update the report (S13 row, stage-2 file list, RESTARTS rows). Print `DONE`.
   314	
   315	### Step G — HUB ONLY, after Dejan approves the HITL card (never Sol)
   316	Run as plan §6 L6–L8, from `~/cobalt` after stage 1 is merged, outside market_reset:
   317	`COBALT_ENV=production uv run cobalt radar seed --dry-run` (diff sha256 must equal the card's) →
   318	`--apply --hitl <token>` → `cobalt radar sources` → `--archiver-diff --yaml-rev HEAD` empty.
   319	
   320	## 5. Report — `docs/40 - DevDocs/reports/s2-p1-2026-09-10.md`
   321	
   322	Report discipline: §0 headline ≤5 lines (what changed, status, ESCALATE count) → tables → ESCALATE.
   323	No restating this brief, no process narration.
   324	
   325	1. **§0 Headline** — READY FOR MERGE / NOT READY (+ the blocking rows).
   326	2. **Base** — `HEAD` sha at step 0; heartbeat fix present or not; expected conflicts.
   327	3. **Steps** — table: step · status · files · tests (passed/failed/skipped) · evidence.
   328	4. **Throttle** — the stage table, `finviz_max_rpm`, or NOT RUN + reason.
   329	5. **Smoke** — S0–S13 table.
   330	6. **Migration proof** — the printed proof tables (forward, rollback --down-to 0003, forward).
   331	7. **`reads:` derivation** — each path with file:line.
   332	8. **RESTARTS derivation** — path · change · rule · restart.
   333	9. **LIVE block** — plan §6 L0–L13, with real shas/tags filled where known, and the rollback column.
   334	10. **DISSENT** — copy plan §9 verbatim.
   335	11. **ESCALATE** — plan E1–E6 carried verbatim + anything new, one line each.
   336	12. **Stage 2 file list** (RUN B).
   337	
   338	You cannot write outside the worktree; the hub copies the report to `~/cobalt/docs/_inflight/` for the
   339	vault.
   340	
   341	Print `DONE` last.
   342	
   343	=== RULINGS ADDENDUM 2026-09-10 (Dejan) ===
   344	E1 Account mode: standing value `live` in "user".trader_settings; a per-day `sim` switch on the morning sheet-attestation control (same control that attests the .htk sheet, one extra tap) writes day_modes.account_mode for that day only; every card is stamped from day override → standing value; a card with no value is REFUSED, loud — never stamped UNSET and let through.
   345	E2 Pool rule — lives in the vault note beside the screens (user data, L32), read by the collector like the screen blocks:
   346	```yaml
   347	pool:
   348	  cap: 50
   349	  priority: [screens, lists]
   350	  rank_metric:
   351	    premarket: volume        # 04:00–09:30 via the F1 session clock
   352	    rth: rvol                # 09:30 onward
   353	  overrides:
   354	    morning_low_float: volume      # this screen ranks by volume in every session
   355	    day_scan_after: "10:00"        # Day Scan takes first priority among screens after 10:00
   356	  stickiness_scans: 3              # out of the top 50 for 3 consecutive scans before dropping
   357	```
   358	Names not admitted get a membership row with `excluded_by = config_cap`.
   359	E3 Static lists: move the three merged tiers as they are; membership `source` names the tier. Named-list attribution comes later, if he re-exports the four TV lists into the vault.
   360	E4 `ft=4`: the HITL card shows each screen's ticker set with and without `ft=4`; any difference → `ft` joins the block contract; no difference → dropped.
   361	E5 User data in reports: before ANY commit, replace the four screens' `f=` strings in every report, plan and review file with "see vault note"; add a repo-wide grep for those strings to the report's checklist.
   362	E6 RESTARTS rule: plist in diff → that job; changed file in a resident's `reads:` → that resident; any src/ change → every resident whose entrypoint imports the changed module (static import walk in the report); unproven → all residents; unclassified path → ESCALATE, never dropped.
   363	E7 Credentials: NO DB credentials in Sol's environment or the worktree during the build. Sol runs everything that needs no DB; the hub runs the DB-backed suite, migrations on cobalt_dev, and the dev-vault smoke.
   364	E8 The R1 vault write (four YAML blocks + pool block into `1 - Trading/Radar Screens.md`) is NOT part of the build: Sol writes the parser, the synthetic fixture and a `cobalt radar screens propose` command that prints the proposed blocks + the ft=4 comparison. The hub runs the proposal at LIVE time; Dejan approves the HITL card; only then does the writer write.
   365	=== END ADDENDUM ===

exec
/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md' | sed -n '128,380p'; nl -ba 'docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md' | sed -n '1,145p'; rg --files -g AGENTS.md /Users/cobalt/cobalt-wt /Users/cobalt/.codex 2>/dev/null | head -40" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
   128	### D5 — Finviz bar poller (same process)
   129	
   130	- After each pool step, for admitted members in rank order: `fetch_bars(ticker, Interval.I1, token)`; keep bars with `ts > watermark` (per ticker, seeded from `max(ts)` in `system.bars`) AND `ts + 1 min ≤ now` (closed bars only); `BarStore.upsert_bars` (one path, archiver schema; the 20:30 archiver finalizes the same keys identically).
   131	- **i1 → 2m:** pure `cobalt.archiver.aggregate.aggregate(bars, minutes)`, buckets floored from 00:00 ET, NOT stored. Stored `i2` stays Finviz's own from the archiver, so no key has two writers. Test on the replay day: aggregate(i1) vs archiver i2 → agreement % in the report; any systematic mismatch (bucket alignment, volume) → ESCALATE, never tuned away.
   132	- Cadence `radar.poll_interval` (60 s) → ≥2 polls per 2m bar.
   133	
   134	### D6 — Account-mode tag
   135	
   136	- `"user".day_modes.account_mode` set by `cobalt daymode account-mode live|sim [--date]` (market_reset-gated like every day-mode write). E1 rules the real flow.
   137	- `AsetStore` INSERT (`aset/store.py:109`) stamps `account_mode` from today's `day_modes` row. The card shows `LIVE`, `SIM`, or a loud `ACCOUNT MODE UNSET` badge. P1 never refuses a card on it (what the sheet accepts is unchanged).
   138	- `pool_member_id`: column + FK only; nothing writes it in P1 (S2-P2).
   139	
   140	### D7 — J1
   141	
   142	Suite: catalog proof that the FK on `"user".aset_sizings.pool_member_id` references `system.radar_membership(id)`. As `cobalt_user`: SELECT `system.radar_membership` OK, INSERT denied, an `aset_sizings` insert with a valid id OK and with an invalid id FK-fails. As `cobalt_system`: SELECT `"user".aset_sizings` denied.
   143	
   144	### D8 — `cobalt db query` (R3)
   145	
   146	- `cobalt db query --side user|system [--prod] [--format json|table] [--limit 1000] "<sql>"`. Connection = `db.connect(dbname, side=…)` (factory, `cobalt_app`, SET ROLE). `--prod` = `allow_prod=True` (RULING 7 tooling seam); otherwise `env.resolve_db_name()`. Lives in `src/cobalt/db_query.py`, registered under the existing `db` group (`db_migrations/cli.py:196`). No new `psycopg.connect`.
   147	- **Code guard (before the server):** a tokenizer aware of quotes, dollar-quotes and comments. Exactly one statement; first keyword `SELECT` or `WITH`. Refused anywhere as a bare word: INSERT UPDATE DELETE MERGE TRUNCATE CREATE ALTER DROP GRANT REVOKE COPY CALL DO SET RESET LOCK VACUUM ANALYZE REFRESH COMMENT LISTEN NOTIFY PREPARE EXECUTE DEALLOCATE DISCARD INTO, and `FOR UPDATE|SHARE|NO KEY UPDATE|KEY SHARE`. Functions `set_config pg_sleep pg_terminate_backend pg_cancel_backend pg_advisory_* lo_* dblink* pg_read_file pg_read_binary_file pg_ls_dir nextval setval` are refused. Refusal = exit 2 with one loud line naming the token.
   148	- **Belt:** `BEGIN READ ONLY`; `SET LOCAL statement_timeout` from tunable `db.query.timeout_s`; query wrapped `SELECT * FROM (<sql>) AS q LIMIT n` (a data-modifying CTE cannot sit in a subquery); always ROLLBACK; `current_user` asserted equal to the side role afterwards. Output passes through F19 redaction before print.
   149	- Tests: every refused class; keyword inside a string literal passes; multi-statement; data-modifying CTE; `set_config('role', …)` switch; user side reads `system.x` qualified; `cobalt_brain` without `--prod` refuses.
   150	
   151	### D9 — F18 `radar` probe
   152	
   153	`probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat` (`heartbeat/runner.py:83-107`). `enabled: false` → OK "NOT PROBED". No pool row → RED. `market_reset` → OK "paused". Inactive session → OK "idle (<session>)". Active session → RED when `now − last_scan_at > heartbeat.radar_max_age_s`; RED when degraded (each source + reason + since); RED when any mirror row is `parse_failed` (names the screen/list).
   154	
   155	### D10 — Config
   156	
   157	- `configs/cobalt/taxonomy/tunables.yaml`, EXISTING units/status/source values only (F11): `radar.pool_cap` 50 `count`; `radar.scan_interval` 60 `duration`; `radar.poll_interval` 60 `duration`; `radar.finviz_max_rpm` `count` (value from build step 1); `heartbeat.radar_max_age_s` 180 `duration`; `db.query.timeout_s` 30 `duration`. If no existing enum value fits a row → ESCALATE; do not add one.
   158	- NEW `configs/cobalt/radar.yaml` (Pydantic, extra=forbid; `cobalt radar check` = dry-run): `pool_key`, `notes {screens, lists}`, `active_sessions`, `export {v: 152, columns: 0-150, required_headers}`, `list_chunk_size`, `not_equity {header, values}`, `rank`, `cache {dir: data/radar-cache, retention_days}`.
   159	- `configs/cobalt/jobs.yaml`: the `com.cobalt.radar` row (D4).
   160	- Boundary: both new paths under `configs/cobalt/` (old loader glob is top-level only) — checked before adding, not after.
   161	
   162	### D11 — Stage 2: the archiver onto the Lists note; `watchlists.yaml` leaves
   163	
   164	- `archiver/config.py` builds its targets from the Lists note via `cobalt.radar.notes` (read + validate, NO mirror write — the archiver runs inside market_reset). `archive_targets` = sorted unique `(ticker, interval)` over enabled lists; `backfill_targets(t)` = the `backfill_default` list's intervals. Missing or failed note → loud failure (job `failed`, F18 red).
   165	- No archiver plist change: in production `resolve_vault_path()` returns the real vault from `COBALT_ENV=production` alone (`vault.py:159-160`), which the archiver plist already sets.
   166	- Sides: the archiver still opens only system-side DB stores (ADR-0008 D2 row unchanged); it reads one vault FILE. The radar job's D2 row: `RadarStore`, `BarStore`, `JobStore` → system; `TraderSettingsStore` (mirror) → user.
   167	- **Equality proof before delete:** `cobalt radar sources --archiver-diff --yaml-rev <sha>` prints `archive_targets` and `backfill_targets` from the note vs from `watchlists.yaml` at that git revision — must be empty. Fixture test in the suite; prod run in L8.
   168	- **Stage 2 commit** = archiver switch + test re-target + `git rm configs/cobalt/watchlists.yaml`, last on the branch. Its rollback = `git revert <stage2>`. It is separate because the 20:30 archiver needs the note, and the note exists only after L6, which needs stage-1 code on main.
   169	
   170	### D12 — Smoke (dev vault + cobalt_dev) — sprint acceptance
   171	
   172	| # | Check | Pass |
   173	|---|---|---|
   174	| S0 | Recorded session: `COBALT_ENV=dev uv run archiver --backfill <T>` for every fixture ticker (F14) | ≥1 full trading day of i1 + i2 in cobalt_dev; the day is named in the report |
   175	| S1 | `cobalt db migrate` on cobalt_dev; `--rollback --down-to 0003`; `migrate` | proof clean, radar tables CREATED, digests identical across the round-trip |
   176	| S2 | Replay `cobalt radar scan --replay <day> --from 04:00 --to 16:00` over cached screener CSVs built from the corpus by `cobalt radar replay-build <day>` (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions present; replay-only, named as such) | pool churns: ≥1 enter and ≥1 leave |
   177	| S3 | Cap | `max(open admitted members) ≤ radar.pool_cap` at every cycle (SQL over membership), including cycles with a degraded source |
   178	| S4 | Entry on RVOL | a name whose proxy RVOL crosses the fixture screen's threshold at T has `entered_at ≤ T + scan_interval` |
   179	| S5 | `excluded_by` | ≥1 row each of `config_cap`, `not_equity`, `screen_inactive`, `manual` |
   180	| S6 | Window gate | no episode with `source` = the fixture screen entered before 10:00 ET; ≥1 after |
   181	| S7 | market_reset | a cycle at 20:30 ET: row counts in pool, membership, bars, `trader_settings` unchanged; state `paused_market_reset`; no `SessionBlocked` in logs |
   182	| S8 | Degraded | fixture source → HTTP 500: pool row degraded, members held, probe RED naming it; broken block → mirror `parse_failed`, probe RED naming it |
   183	| S9 | Poller | member i1 bars upserted, closed bars only, watermark honoured; aggregate-vs-i2 agreement % reported |
   184	| S10 | Probe | `radar` OK fresh / RED stale in session / OK idle out of session |
   185	| S11 | Account mode + J1 | card stamped + badge rendered (`GET /` on a dev sheet); UNSET badge when day row NULL; J1 suite green |
   186	| S12 | Whole system | `uv run pytest tests/cobalt tests/taxonomy` green; `uv run cobalt validate` exit 0; `cobalt jobs readers` for every changed config path; R2 grep clean |
   187	| S13 | Stage 2 | archiver-diff empty on fixtures; `archiver --backfill` still works from the note |
   188	
   189	Sol runs the smoke against a worktree-local vault copy (`data/smoke-vault`, gitignored) because it cannot write `~/dev-vault-cobalt` (F15). The hub re-runs S1–S13 against `~/dev-vault-cobalt` + cobalt_dev as ground truth (L35).
   190	
   191	## §3 Houses and RESTARTS (R5)
   192	
   193	Build = `gpt-5.6-sol`, high effort, `-s workspace-write -c sandbox_workspace_write.network_access=true`, cannot commit. Hub = Sonnet: launch, wait, verify against ground truth, commit on branch. Gated vault write = hub, after approval.
   194	
   195	RESTARTS, derived by rule from the expected diff (Sol re-derives it from the real `git diff --name-status main...HEAD`):
   196	
   197	| Path (expected) | Rule | RESTART |
   198	|---|---|---|
   199	| `ops/com.cobalt.radar.plist` (A) | plist in diff | `com.cobalt.radar` — bootstrap (new) |
   200	| `configs/cobalt/taxonomy/tunables.yaml` (M) | in a resident's `reads:` → `com.cobalt.aset` (`jobs.yaml:69`, `taxonomy/loader.py:79`) | `com.cobalt.aset` kickstart |
   201	| `configs/cobalt/radar.yaml` (A) | only in radar's `reads:` | covered by the bootstrap |
   202	| `configs/cobalt/jobs.yaml` (M, and again in L11) | registry | `cobalt jobs register` |
   203	| `configs/cobalt/watchlists.yaml` (D, stage 2) | `cobalt jobs readers` → none (archiver is a one-shot) | none |
   204	| `src/**` incl. `db_migrations/0004*.sql` | code | none (the migration is LIVE step L3, not a restart) |
   205	| `tests/**`, `docs/**`, `ops/README.md` | tests/docs | none |
   206	| anything else | unclassified | ESCALATE, never dropped |
   207	
   208	## §4 Build step 1 — Finviz throttle re-measure (FIRST)
   209	
   210	- `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`. Names = the 50 synthetic-fixture tickers. Refuses 09:00–16:00 ET on trading days (his live session) and inside market_reset.
   211	- Per cycle: sequential `/export/stock?p=i1` for each name, then one screener call with the fixture filter. STOP at the first non-200, 429, redirect, non-CSV body or header mismatch.
   212	- Per stage: requests, achieved req/min, statuses, p50/p95 latency, bytes → `data/radar-throttle-<ts>.json` + a printed table.
   213	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`; the row's `consumers` cites the report. If the 10 s stage is clean, the report says "no throttle observed up to N req/min" (a floor, not a ceiling). Never extrapolate.
   214	- Token resolution fails in the sandbox → NOT RUN with the scrubbed error line; the hub runs the same command. Offline steps continue. READY FOR MERGE requires the number.
   215	
   216	## §5 NOT in P1
   217	
   218	Precondition evaluator (F8), dots / ladder (F10), radar panel, F3 rank display, F12 missed replay, F13 auto-archive. Writing `pool_member_id`. `account_mode NOT NULL`. Hysteresis at the cap. The four-list re-export (E3).
   219	
   220	## §6 LIVE block — named steps, one rollback domain each
   221	
   222	Window: trading-day 16:15–19:40 ET or a weekend daytime. Never 09:00–16:00, 20:00–21:30, 21:25–21:55 (backup), or 23:27–23:47 (generated commit).
   223	
   224	| Step | Action | Proof | Rollback (domain) |
   225	|---|---|---|---|
   226	| L0 PRECONDITIONS | heartbeat fix merged + deployed + green; branch rebased; suite green on the rebased head; report READY FOR MERGE; `git tag pre-s2-p1` on main | report + tag | — |
   227	| L1 SNAPSHOT | `uv run cobalt backup run` | restic id + dump printed | belt for DB + vault |
   228	| L2 CODE stage 1 | hub rebases the branch onto current main (the nightly generated commit moves main), then `git -C ~/cobalt merge --ff-only <stage1-sha>`; `git tag s2-p1-stage1` | `git log -1` | reset to `pre-s2-p1` + RESTARTS again (code) |
   229	| L3 DB | `uv run cobalt db migrate --allow-prod` | every existing table OK; radar tables CREATED | `cobalt db migrate --allow-prod --rollback --down-to 0003` (DB) |
   230	| L4 REGISTRY | `uv run cobalt validate`; `uv run cobalt jobs register` | exit 0; radar row `enabled: false` | re-register at the previous tag |
   231	| L5 RESTARTS stage 1 | `launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` | `curl -s :5010/api/health` → `ok:true`; next beat `sheet daymode` OK | kickstart again after the code rollback |
   232	| L6 VAULT (HITL) | hub, after approval: `COBALT_ENV=production uv run cobalt radar seed --dry-run` → diff sha256 == card's; then `--apply --hitl <token>` | 5 write_ids printed | `uv run cobalt vault restore --write-id <id>` ×5, or the L1 snapshot (vault) |
   233	| L7 SOURCES | `uv run cobalt radar sources` | every block `ok`; Day Scan `active_from "10:00"`; list counts == YAML counts | — |
   234	| L8 PROOF | `uv run cobalt radar sources --archiver-diff --yaml-rev HEAD` | empty diff | — |
   235	| L9 CODE stage 2 | `git merge --ff-only sprint-2/radar-pool`; `git tag s2-p1`; `cobalt jobs readers configs/cobalt/watchlists.yaml` | readers: none | `git revert <stage2-sha>` (source switch) |
   236	| L10 LAUNCHD | `cp ops/com.cobalt.radar.plist ~/Library/LaunchAgents/`; `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.radar.plist` | first cycle in `logs/radar.log`; `cobalt db query --prod --side system "select state, degraded, members, last_scan_at from radar_pool"` | `launchctl bootout gui/$(id -u)/com.cobalt.radar` (launchd) |
   237	| L11 ENABLE | `jobs.yaml` `enabled: true` on main; `cobalt jobs register` | registry | flip back + register |
   238	| L12 HEARTBEAT | next beat | GREEN, `radar` line present | — |
   239	| L13 NEXT SESSION | 04:00+ `scanning`; Day Scan: no episode before 10:00, sources list it active after; 20:00–21:00 radar row counts constant, no RED; 20:30 archiver exit 0, target count == prior night | `cobalt db query` + logs | per domain above |
   240	
   241	## §7 Risks
   242	
   243	| Risk | Mitigation |
   244	|---|---|
   245	| Finviz lockout on his Elite login (probe or poller) during trading | probe refuses 09:00–16:00; stop-on-first-error ramp; 0.5 safety factor; single token bucket; startup budget refusal |
   246	| Real screen data reaching the repo (reports, cache, fixtures) | cache under gitignored `data/`; reports name screens by key only, never `f=`; R2 grep + suite test |
   247	| Rebase conflicts with the heartbeat fix | expected in `db_migrations/__init__.py`, `db_migrations/cli.py` (digest list), `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`, `test_jobs.py` — rebase first, never after |
   248	| First resident + `self`: zombie path unexercised | watchdog test: stale heartbeat → `zombie`; plist unloaded → RED |
   249	| i1 export ~9.4k rows × 50 names per poll = parse cost | watermark filter before model build; `last_scan_ms` on the pool row; smoke reports p95 cycle ms |
   250	| Cap-boundary oscillation → episode churn | smoke reports episodes/day; hysteresis is E2's ruling |
   251	| Cache growth (~7k CSVs per trading day) | retention in radar.yaml; smoke measures bytes/day |
   252	| Finviz serves `p=i2` natively (DATA-SOURCE-MEMO A.2.1), so i1→2m aggregation may disagree with Finviz's own 2m bars | ruled i1→2m kept; the S9 agreement % against archived i2 decides; a systematic mismatch is ESCALATE, not a silent switch |
   253	| A cycle straddling 20:00 ET | second session check before commit; dropped whole (D4) |
   254	| Sol cannot reach cobalt_dev or has no DB env | the hub exports DB env from `~/cobalt/.env` at launch (never printed); DB tests Sol cannot run are reported NOT RUN, and the hub runs them |
   255	
   256	## §8 ESCALATE
   257	
   258	```
   259	ESCALATE:
   260	E1 ACCOUNT MODE SOURCE — no live/sim value exists anywhere (day_modes, trader_settings, configs).
   261	   P1 adds nullable day_modes.account_mode + a CLI setter, stamps cards, shows a loud UNSET badge,
   262	   never refuses a card. Rule: who sets it and when (sheet day-mode step?), and must an UNSET card be refused.
   263	E2 POOL RANK AT THE CAP — today's static tiers alone (~260 names) exceed pool_cap 50 five-fold, so the
   264	   rank rule chooses the pool every minute. P1 default: screen names first (hits, screen position), then
   265	   list names by RVOL, ticker tie-break, no hysteresis. Selection logic: rule it or replace it.
   266	E3 FOUR LISTS NOT RECOVERABLE — watchlists.yaml holds 3 derived tiers, not Green/Red/SMB Daily Watch/
   267	   Watchlist. P1 migrates the tiers verbatim (source = list:tier_a…). Re-export the four lists into the
   268	   Lists note if membership must name them.
   269	E4 ft=4 DROPPED BY THE R1 KEY LIST — 3 of 4 pasted URLs carry it; meaning unverified. The card shows
   270	   ticker sets with vs without ft=4 per screen; any difference needs an `ft` key added to R1's contract.
   271	E5 USER DATA IN AN UNCOMMITTED REPORT — docs/40 - DevDocs/reports/day-open-2026-09-10.md §2 C.1 quotes
   272	   all four screens' full f= strings and columns; it commits at day close → L32 breach. Redact first.
   273	E6 R5 RULE GAP — "code → none" leaves a resident on stale code whenever no reads: file changes (here the
   274	   sheet's account-mode stamp/badge). P1 is covered only because tunables.yaml restarts the sheet anyway.
   275	   Rule: does a code change under a resident's import tree restart it.
   276	```
   277	
   278	## §9 DISSENT
   279	
   280	No review round completed, so there are no reviewer objections to adopt or decline.
   281	
   282	- **Round 1 FAILED:** `codex exec -m gpt-6-astra` hit "You've hit your usage limit … try again at 11:31 AM" after 72,175 tokens. The model read the plan, ADR-0008, DATA-SOURCE-MEMO, `db_migrations/`, `jobs/wrapper.py`, `jobs/watchdog.py` and `daymode/store.py`, then stopped without issuing any BLOCKER, RISK or VERDICT. Capture: `plan-s2-p1-astra-r1.md`.
   283	- Its last progress message named three boundaries it was about to check: disabled-job startup, scans crossing market_reset, held members vs the pool cap. The architect checked them without the reviewer. The last two were real gaps and are fixed in D4 and D12 S3. The first holds: `job_run` does not read `enabled` (`wrapper.py:122-162`).
   284	- **Rounds 2–3:** not run. Codex has one shared five-hour pool (`limit_id codex`, day-open §1.4), the same pool Sol builds on. The hub should run the review command (same prompt, same capture path pattern) after the reset and BEFORE launching Sol. Objections left after round 3 are added here, one line each.
   285	
   286	=== RULINGS ADDENDUM 2026-09-10 (Dejan) ===
   287	E1 Account mode: standing value `live` in "user".trader_settings; a per-day `sim` switch on the morning sheet-attestation control (same control that attests the .htk sheet, one extra tap) writes day_modes.account_mode for that day only; every card is stamped from day override → standing value; a card with no value is REFUSED, loud — never stamped UNSET and let through.
   288	E2 Pool rule — lives in the vault note beside the screens (user data, L32), read by the collector like the screen blocks:
   289	```yaml
   290	pool:
   291	  cap: 50
   292	  priority: [screens, lists]
   293	  rank_metric:
   294	    premarket: volume        # 04:00–09:30 via the F1 session clock
   295	    rth: rvol                # 09:30 onward
   296	  overrides:
   297	    morning_low_float: volume      # this screen ranks by volume in every session
   298	    day_scan_after: "10:00"        # Day Scan takes first priority among screens after 10:00
   299	  stickiness_scans: 3              # out of the top 50 for 3 consecutive scans before dropping
   300	```
   301	Names not admitted get a membership row with `excluded_by = config_cap`.
   302	E3 Static lists: move the three merged tiers as they are; membership `source` names the tier. Named-list attribution comes later, if he re-exports the four TV lists into the vault.
   303	E4 `ft=4`: the HITL card shows each screen's ticker set with and without `ft=4`; any difference → `ft` joins the block contract; no difference → dropped.
   304	E5 User data in reports: before ANY commit, replace the four screens' `f=` strings in every report, plan and review file with "see vault note"; add a repo-wide grep for those strings to the report's checklist.
   305	E6 RESTARTS rule: plist in diff → that job; changed file in a resident's `reads:` → that resident; any src/ change → every resident whose entrypoint imports the changed module (static import walk in the report); unproven → all residents; unclassified path → ESCALATE, never dropped.
   306	E7 Credentials: NO DB credentials in Sol's environment or the worktree during the build. Sol runs everything that needs no DB; the hub runs the DB-backed suite, migrations on cobalt_dev, and the dev-vault smoke.
   307	E8 The R1 vault write (four YAML blocks + pool block into `1 - Trading/Radar Screens.md`) is NOT part of the build: Sol writes the parser, the synthetic fixture and a `cobalt radar screens propose` command that prints the proposed blocks + the ft=4 comparison. The hub runs the proposal at LIVE time; Dejan approves the HITL card; only then does the writer write.
   308	=== END ADDENDUM ===
     1	# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`
     2	
     3	You build S2-P1 (radar pool + Finviz bar poller) in this worktree. Everything you need is in this
     4	file. The plan it implements is `docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md`,
     5	in this worktree. Where the two disagree, the plan wins; say so in the report.
     6	
     7	## 0. Who does what
     8	
     9	| House | Does | Cannot |
    10	|---|---|---|
    11	| **You (Sol)**, high effort, `-s workspace-write`, network on | write code, tests, docs, the report, inside this worktree | commit, rebase, write outside the worktree, touch the real vault or `cobalt_brain` |
    12	| **Hub (Sonnet)** | launches you, verifies against ground truth, commits per step on `sprint-2/radar-pool`, runs what your sandbox cannot | build |
    13	| **Dejan** | approves the HITL card | — |
    14	
    15	**Hub, before launching you:** (1) if `ops/heartbeat-market-reset` has merged to main, rebase this
    16	branch onto main first; (2) if the plan's §9 says the Astra review loop has not run, run it and fold
    17	fixes into the plan before launch; (3) export the dev DB credentials into your environment without
    18	printing them.
    19	
    20	**Two runs.** RUN A = steps 0–13 (stage 1). Stop, print `DONE`. The hub commits stage 1, then
    21	relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
    22	Step G is **hub only, after Dejan's approval** — you never run it.
    23	
    24	**Stop rules.** A step you cannot finish → mark it `NOT RUN` or `FAILED` in the report with the
    25	exact error line (scrubbed), then continue with the steps that do not depend on it. Never mark a
    26	test passing that did not run. 3 failed attempts at the same thing → stop that step, ESCALATE.
    27	Print `DONE` as the very last line of every run, nothing after it.
    28	
    29	## 1. Laws (binding — a violation is a failed step)
    30	
    31	1. **Production is sacred (NN#16).** Dev only: `COBALT_ENV=dev`, database `cobalt_dev`, vault =
    32	   `data/smoke-vault` (gitignored copy you make of `~/dev-vault-cobalt`). Never open
    33	   `/Users/cobalt/Vault/Think`. Never connect to `cobalt_brain`. Never `launchctl` anything.
    34	2. **User data never enters the repo (L32).** No real screen, filter string, list or dollar figure in
    35	   any tracked file, report, fixture, test or log line you paste. The repo ships exactly ONE synthetic
    36	   example screen (R2).
    37	3. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error
    38	   string passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
    39	4. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent
    40	   fallback, no plausible-empty artifact, no default invented for a missing value.
    41	5. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
    42	   `archiver.collector.fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
    43	   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
    44	   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`.
    45	6. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted
    46	   (`psycopg.sql.Identifier` in Python); cross-side SQL is schema-qualified (`system.radar_membership`);
    47	   every new table is on a side in `src/cobalt/db_migrations/placement.py` or the suite fails.
    48	7. **Config-as-code.** Pydantic schema per config file, `extra="forbid"`, dry-run command. New-core
    49	   config lives only under `configs/cobalt/` (never `configs/*.yaml` top level).
    50	8. **Tunables.** Thresholds are `configs/cobalt/taxonomy/tunables.yaml` rows. Use EXISTING
    51	   `TunableUnit` / `TunableStatus` / `TunableSource` values only — adding an enum value breaks the
    52	   live ASET sheet (09-09 outage). No fitting value → ESCALATE.
    53	9. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE writing; never rely on catching
    54	   `SessionBlocked`. Radar writes nothing in that window.
    55	10. **Tools fetch, code computes.** No LLM anywhere in P1. All numbers are deterministic code.
    56	11. **Tests per step.** `uv run pytest` for the step's tests before moving on; the whole suite at
    57	    step 13.
    58	12. **Names.** One name per concept across SQL, Python, config and docs (`radar_pool`,
    59	    `radar_membership`, `account_mode`, `pool_member_id`, `excluded_by`).
    60	
    61	## 2. Rulings you implement (09-10, binding)
    62	
    63	- **R1 Radar Screens contract.** Vault note `1 - Trading/Radar Screens.md` gets one fenced YAML block
    64	  per screen: `screen, f, sort, columns, active_from, active_to (session clock, ET), enabled`. It is
    65	  written ONCE, through the vault writer, under ONE HITL card, prose untouched. After that Cobalt only
    66	  reads the note: parse fenced blocks only, reload on file-hash change, mirror each block + hash into
    67	  `"user".trader_settings`; `radar_membership.source` names screen + hash. Parse failure → pool row
    68	  degraded + heartbeat `radar` probe RED naming the screen; never the previous version silently. Day
    69	  Scan is active from 10:00 ET via the F1 session clock — a field, never code.
    70	- **R2 Synthetic example screen.** Exactly one, same fenced format, as the test fixture under
    71	  `tests/fixtures/`; real screens never enter the repo. `git ls-files | grep -i radar` stays clean of
    72	  user data.
    73	- **R3 `cobalt db query`.** Read-only CLI: factory connection, SET ROLE per side, SELECT-only enforced in
    74	  code (reject anything else, loud), output JSON/table. The workers' DB read path.
    75	- **R4 Static lists are user data.** They move user-side by the same mechanism as R1. Plan choice: a new
    76	  vault note `1 - Trading/Radar Lists.md` with fenced blocks. The archiver keeps working through the
    77	  migration (stage 2).
    78	- **R5 Houses + RESTARTS by rule.** plist in diff → that job; changed file in a resident's `reads:` →
    79	  that resident; registry → `register`; code/tests/docs → none; anything unclassified → ESCALATE.
    80	
    81	## 3. Environment
    82	
    83	- Run everything from this worktree with `uv run …`. Tests: `uv run pytest tests/cobalt tests/taxonomy`.
    84	- DB env: the hub exports the Postgres credentials into your environment at launch. If a DB-backed test
    85	  or command fails to connect, record `NOT RUN (db unreachable: <scrubbed error>)` and continue.
    86	- No `psql` on this host. Before step 3 lands, reach the DB only through repo code; after it lands, use
    87	  `uv run cobalt db query --side system|user "<select>"`.
    88	- Finviz token: `cobalt.archiver.collector.resolve_token()`. If it fails in your sandbox, the live half
    89	  of step 1 is `NOT RUN`; the hub runs it.
    90	- Vault for smoke: `cp -R ~/dev-vault-cobalt data/smoke-vault` once, then
    91	  `COBALT_VAULT_PATH=$PWD/data/smoke-vault`. `data/` and `logs/` are gitignored — confirm with
    92	  `git check-ignore` before writing anything there.
    93	- DevDocs layout: one page per `.py` file at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
    94	  `docs/40 - DevDocs/tests/cobalt/<file>.md`, and a line in `docs/40 - DevDocs/INDEX.md`.
    95	
    96	## 4. Build steps
    97	
    98	Each step lists its files, then the tests that must pass before the next step starts.
    99	
   100	### Step 0 — Base check (no code)
   101	- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql`. Present → the heartbeat fix is in
   102	  your base; build on it. Absent → build on main as is, register 0004 after 0002, and list in the report
   103	  the files that will conflict at merge: `db_migrations/__init__.py`, `db_migrations/cli.py`,
   104	  `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`,
   105	  `tests/cobalt/test_jobs.py`.
   106	- Record `git rev-parse HEAD` in the report.
   107	
   108	### Step 1 — Finviz throttle re-measure (FIRST)
   109	- `src/cobalt/radar/throttle.py` + `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`.
   110	- Names = the 50 first tickers of the synthetic lists fixture (step 5 creates it; create that fixture
   111	  file now if needed).
   112	- Refuses on trading days between 09:00 and 16:00 ET, and inside market_reset (use `session_clock()` and
   113	  the NYSE calendar).
   114	- Per cycle: sequential `fetch_bars(t, Interval.I1, token)` for each name, then one
   115	  `/export/screener?v=152&f=<fixture f>&c=0,…,150` call. STOP at the first non-200, 429, redirect,
   116	  non-CSV body or header mismatch.
   117	- Per stage record: requests, achieved req/min, status counts, p50/p95 latency ms, bytes. Write
   118	  `data/radar-throttle-<UTC ts>.json` and print a table.
   119	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`. If every stage was clean, write
   120	  "no throttle observed up to N req/min". Never extrapolate.
   121	- **Tests (mocked HTTP):** stop-on-first-error per class; refusal inside the forbidden window; rpm math;
   122	  token never appears in output (assert `auth=REDACTED`).
   123	- **Live run:** allowed only outside the forbidden window. Otherwise, or on token failure, `NOT RUN`.
   124	
   125	### Step 2 — Migration 0004, rollback bound, placement, J1
   126	- `src/cobalt/db_migrations/0004_radar_pool.sql` and `0004_radar_pool.rollback.sql` with exactly the
   127	  plan's §D3 DDL. Tables are created schema-qualified, `OWNER TO cobalt_system`;
   128	  `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`;
   129	  `GRANT SELECT ON system.radar_pool TO cobalt_user`. The rollback header states its cost.
   130	- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring lines.
   131	- `db_migrations/cli.py`: the digest excludes `account_mode` and `pool_member_id` (extend the heartbeat
   132	  fix's `DIGEST_EXCLUDED_COLUMNS` if present; otherwise generalize `TENANCY_COLUMN` into that tuple).
   133	  `--rollback` REQUIRES `--down-to NNNN`; it reverses only registered migrations newer than NNNN, newest
   134	  first; without it, it refuses and lists targets.
   135	- `placement.py`: move `radar_pool`, `radar_membership` out of `DECLARED_TABLES` into a new
   136	  `CREATED_TABLES` dict ("created by a db_migration directly on its side"), included in `PLACEMENT` and
   137	  in the proof table; extend the SQL/Python agreement test to 0004.
   138	- **Tests** (`tests/cobalt/test_tenancy.py`, `tests/cobalt/test_radar_migration.py`):
   139	  migrate twice idempotent; `migrate → --rollback --down-to 0003 → migrate` digests identical;
   140	  0003's columns (if present) survive the 0004 rollback; `--rollback` without `--down-to` refuses;
   141	  placement test green; J1 — FK catalog proof, `cobalt_user` SELECT OK / INSERT denied on
   142	  `system.radar_membership`, valid id insert OK / invalid FK-fails, `cobalt_system` SELECT on
   143	  `"user".aset_sizings` denied; membership CHECKs (`entered_at IS NOT NULL OR excluded_by IS NOT NULL`)
   144	  and the partial unique index reject bad rows.
   145	

exec
/bin/zsh -lc "nl -ba 'docs/10 - Decisions/ADR-0008-two-layer-data-model.md' | head -190; nl -ba 'docs/30 - Design/DATA-SOURCE-MEMO.md' | head -190; nl -ba src/cobalt/archiver/collector.py | sed -n '1,300p'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
     1	# ADR-0008 — Two-layer data model: user data vs system data
     2	
     3	Date: 2026-09-08
     4	Status: Accepted (architect spike, Fable 5.1; rulings 0, a–g decided-with-veto by
     5	Dejan 09-08, one per message; implemented by an Opus 5 lead-developer session on
     6	`sprint-2/data-model`)
     7	Implements: **L32** (user-data / system-data law, 09-05; tenancy R2 09-06) and
     8	**L31** (names rule, 09-06). Relates to: ADR-0001 (trade_defs as data — superseded
     9	in part: the repo no longer carries populated defs), ADR-0004 (L28, the one vault
    10	write path — reused unchanged, frontmatter site included), ADR-0005/0006 (RULING 7
    11	environment law and the one connection factory — extended, not replaced).
    12	Gates: SPRINT-LADDER S2-P1 line 0.
    13	
    14	## Context
    15	
    16	Cobalt-the-system is only the schema and engine that make any trader's strategies
    17	pluggable: taxonomy anatomy (regime, range, gap, extension, leg, session clock), the
    18	card engine, the radar, alerts, the rules-engine schema. Everything named after a
    19	trade, everything SMB- or cheat-sheet-derived, every setting that is one trader's
    20	choice, and every note in `1 - Trading` is user data — never shipped to or visible
    21	to another Cobalt user (L32).
    22	
    23	On 2026-09-08 the code did not know the difference:
    24	
    25	- Every new-core table sat in `public` of `cobalt_brain` beside 17 old-tree tables
    26	  (`memory_logs`, `graph_nodes`, `graph_edges`, `hitl_proposals`,
    27	  `browser_fast_path`, `instruments`, `market_snapshots`, `daily_in_play`,
    28	  `key_levels`, `news_events`, `news_mentions`, `order_fills`, `strategy_signals`,
    29	  `system_alerts`, `themes`, `trades`, `trading_accounts`). One login role,
    30	  `cobalt`, the docker superuser, owned all of it. `search_path` was
    31	  `"$user", public`.
    32	- The 13 populated trade_defs were committed YAML under
    33	  `configs/cobalt/taxonomy/trade_defs/`, cross-checked against
    34	  `cameron_grid.yaml` (a person's name in a config key, L31) and
    35	  `variables/<id>.yaml`. The same 13 defs existed a second time, verbatim, inside
    36	  the 22 strategy notes written on 09-06 (`1 - Trading/4 - Strategies/<note>.md`,
    37	  `cobalt:section definition` units) — a one-path violation waiting for the first
    38	  edit to either copy.
    39	- The vault key (`trade_def:` frontmatter, kebab: `big-dog`, `nine-ema-scalp`) and
    40	  the YAML key (`id:`, snake: `big_dog`, `ema9_scalp`) were not inter-derivable
    41	  for 3 of 13, and nothing in the repo owned the map.
    42	- 69 trade notes in `1 - Trading/2 - Trades/` carried `strategy:` as free text
    43	  (33 blank; aliases like `Big Dawg`, `Offside Scalp`, `Fashionable Late Scalp`;
    44	  leading spaces and doubled quotes from Templater) and none carried `trade_def:`,
    45	  so every `## Instances` dataview rendered empty.
    46	- The trader's own dollar sheet, enabled grades, reduced mode, `.htk` template and
    47	  step-downs lived in committed config (`configs/cobalt/aset.yaml`,
    48	  `daymode.yaml`).
    49	- The 09-06 strategy-note batch was hand-work with no L28 record; its ledger line
    50	  cited a restic snapshot ("09-05 21:40") that does not exist.
    51	
    52	Facts verified read-only during the spike, and binding on the design:
    53	
    54	- `user` is a **reserved word** in PostgreSQL 16 (`pg_get_keywords` catcode R);
    55	  `system` is unreserved.
    56	- `cobalt` is `rolsuper = true`; superusers bypass every grant regardless of
    57	  `INHERIT`.
    58	- `pg_read_all_data` exists (PG14+).
    59	- `VaultWriter.upsert_region` (ADR-0004) already is the marker-less frontmatter
    60	  write site: 3-way merge, write_id, restore. A first write on a unit with no
    61	  baseline takes Cobalt's body wholesale (base := human) — exactly right for
    62	  migrating Cobalt-seeded units.
    63	- The `cfg()` key grammar (§13.1) and `per_trade(<id>)` scope accept `[a-z0-9_]`
    64	  only: a kebab slug cannot appear verbatim in a tunable key, and would read as
    65	  subtraction to a future predicate parser.
    66	- The SSD restic repo holds three snapshots: `24f3f36b` 2026-09-06 08:30:23,
    67	  `472ade44` 09-06 21:40:08, `0d55d7b5` 09-07 21:40:03. The 09-06 batch began
    68	  09:21 → its pre-state is `24f3f36b`.
    69	
    70	## Decision
    71	
    72	### D1 — Tenancy A: one database, two schemas, per-store sides (RULED L32 R2; item 0)
    73	
    74	- One database `cobalt_brain` (dev twin `cobalt_dev`). Two schemas: **`system`**
    75	  and **`"user"`**. The user-side schema keeps the name `user` (ruled 09-08:
    76	  "user will have more roles and more user settings outside of being trader
    77	  only") and is therefore **always quoted** — in every migration, grant,
    78	  `search_path`, hand query and Python (`psycopg.sql.Identifier`). A suite lint
    79	  test fails on any unquoted `user.` reference under `src/cobalt`. The word
    80	  "trader" survives only inside table/field names (`trader_settings`, `traders`,
    81	  `trader_id`, `trade_key`).
    82	- Two `NOLOGIN` roles: **`cobalt_user`** (ALL on `"user"`, SELECT on `system`) and
    83	  **`cobalt_system`** (ALL on `system`, **nothing** on `"user"` — system never reads
    84	  user data). Each schema and every new-core table is **owned** by its side role
    85	  (`ALTER … OWNER TO`): ownership is not a grant and would otherwise leak every
    86	  privilege back to the login role. A third `NOLOGIN` role **`cobalt_backup`** is
    87	  a member of `pg_read_all_data` for `pg_dump --role=cobalt_backup`.
    88	- **The side is chosen per store, never per process.** Every store declares
    89	  `SIDE = Side.USER | Side.SYSTEM` and opens its connections through the one
    90	  factory, `cobalt.db.connect(dbname, side=…)`, which does
    91	  `SET ROLE <side role>; SET search_path = <own schema only>` (no `public`). A job
    92	  that touches both sides holds one connection per side; there is no "both" role.
    93	  Cross-side references are written **schema-qualified** (`system.bars`), never
    94	  resolved through `search_path`. A wrong-side statement fails loud twice over:
    95	  relation-not-found (search_path) or permission denied (grants).
    96	- **`user_id`.** `"user".traders(id, handle, created_at)`, seeded `id = 1,
    97	  handle = 'primary'` (no name). Every user-side table carries
    98	  `user_id INTEGER NOT NULL REFERENCES "user".traders(id)` with
    99	  `DEFAULT current_setting('cobalt.trader_id')::int`. The factory sets the GUC
   100	  from `configs/cobalt/tenant.yaml` (`trader_id: 1` — which local trader this
   101	  install serves; committed; a product install ships it as 1). A connection that
   102	  did not pass through the factory has no GUC and every INSERT fails loud; no
   103	  literal default anywhere. Existing rows are backfilled to 1 in the same
   104	  migration.
   105	- **`public` is untouched** for the 17 old-tree tables (strangler rule). The
   106	  placement test carries that list frozen: a NEW table landing in `public`, or any
   107	  table not on exactly one side of the placement map, fails the suite.
   108	- **Superuser login — weighed, split (Revision 2).** `NOINHERIT` on `cobalt` buys
   109	  nothing while it is the superuser; after the factory's `SET ROLE` the session's
   110	  current role is a non-superuser and the grants bite, so per-store enforcement is
   111	  real. The only closure for "a connection that skips the factory" is a
   112	  non-superuser app login. Target state, ruled here; implementation split:
   113	  - this sprint: ownership to side roles, `cobalt_backup`, and a suite test that no
   114	    `psycopg.connect` exists under `src/cobalt` outside `db.py`;
   115	  - next ops prompt (owed): `cobalt_app` LOGIN NOINHERIT with its own credential in
   116	    VaultManager/.env, member of `cobalt_user`, `cobalt_system`, `cobalt_backup`;
   117	    factory and `pgdump.py` connect as it; superuser `cobalt` reserved for
   118	    `db migrate --allow-prod` and docker; every production plist restarted in the
   119	    same action (L28 restart-on-deploy). No credential change rides inside a
   120	    data-model migration — two rollback domains would become three.
   121	
   122	### D2 — Placement (RULED item 2; `cobalt_email_sends` revised under g)
   123	
   124	| table | side | note |
   125	|---|---|---|
   126	| `aset_sizings` (cards), `card_transitions`, `card_stop_edits` | user | + `user_id`; S2 adds `account_mode`, `pool_member_id → system.radar_membership(id)` |
   127	| `day_modes` | user | + `user_id` |
   128	| `vault_writes`, `vault_overrides` | user | + `user_id` (note text is user data) |
   129	| `trade_defs`, `tunables` (per-trade rows), `trader_settings`, `traders` — NEW | user | loaded copies of vault units / seeded settings |
   130	| `setup_trade_matrix` | user | a VIEW `(trade_def, setup_ref, relation)` unnested from `trade_defs` |
   131	| legs/fills, missed, DRC rows, prediction records | user | S2-P4 / S3 — declared now so the placement test names them |
   132	| `bars` | system | 4.84M rows; `SET SCHEMA` is catalog-only |
   133	| `radar_pool`, `radar_membership` (S2-P1) | system | |
   134	| `cobalt_jobs`, `cobalt_kill_switch`, `cobalt_redactions`, `session_blocks` | system | |
   135	| `cobalt_email_sends` | **system** | revised 09-08: channel log (`ts, ok, caller, message_id, detail`), no personal data — same class as `cobalt_redactions` |
   136	| taxonomy anatomy instances (S2-P2) | system | |
   137	| 17 old-tree tables | public | frozen allowlist, untouched |
   138	
   139	Per launchd job, which side each of its stores connects as:
   140	
   141	| job | stores → side |
   142	|---|---|
   143	| `com.cobalt.aset` | AsetStore, CardStore, DayModeStore, VaultWriteStore → user; SessionBlockStore → system |
   144	| `prefill-daily` / `prefill-drc` | AsetStore, DayModeStore, VaultWriteStore → user; SessionBlockStore, JobStore → system |
   145	| `cards-expire` · `daymode-propose` | CardStore / DayModeStore (+ VaultWriteStore) → user; JobStore → system |
   146	| `archiver` | BarStore, JobStore → system only |
   147	| `heartbeat` | JobStore, kill switch, SessionBlockStore, RedactionStore, EmailSendStore → system; VaultWriteStore (daily-note red/green block) → user |
   148	| `cobalt notify email-test` | EmailSendStore, RedactionStore → system |
   149	| `backup` | `pg_dump` as the login role (`--role=cobalt_backup` once D1's ops prompt lands), both schemas, no store |
   150	| `agent` (old tree) | `public` only, untouched · `mainframe`, `obsidian`: no DB |
   151	
   152	Tunables split: engine rows stay in `configs/cobalt/taxonomy/tunables.yaml`
   153	(system); trader rows (every `per_trade(...)` row) become user data (D3.3);
   154	trader-level settings become `"user".trader_settings` (D3.4).
   155	
   156	### D3 — The vault note is the trade_def's truth (RULED item 3; a, b, d, e)
   157	
   158	- **Source of truth** = the `cobalt:unit trade_def:<slug>` inside
   159	  `<!-- cobalt:section definition -->` of `1 - Trading/4 - Strategies/<note>.md`,
   160	  read through `cobalt.vault.resolve_vault_path()`. The DB row
   161	  (`"user".trade_defs`: `slug` PK, `def` jsonb, `md5`, `note_path`, `loaded_at`,
   162	  `user_id`) is a loaded, validated copy. One path: vault unit → loader →
   163	  `"user".trade_defs`.
   164	- **Key (a).** The frontmatter `trade_def:` slug — lowercase kebab, no `$`, no
   165	  leading digit — **is the id**. `id:` is removed from the YAML unit; the loader
   166	  injects `id = slug`; a unit that still carries `id:` fails loud ("id comes from
   167	  frontmatter `trade_def:`"). Grammar-safe spelling for `cfg()` keys and
   168	  `per_trade()` scope is ONE helper, `trade_key(slug) = slug.replace('-', '_')`.
   169	  Consequence: `ema9_scalp.*` tunable rows re-key to `nine_ema_scalp.*`; every
   170	  other key already equals `trade_key(slug)`. Schema: "v0.4 minus authored `id`
   171	  and `name`, plus structured `quality_factors[]`" — recorded here, folded into the
   172	  taxonomy at S2-P2's v0.8 bump.
   173	- **Display name (e).** `TradeDef.name` = frontmatter `name:` (loader-injected
   174	  like `id`); `name:` is removed from the unit; where the YAML's former name
   175	  differed it joins `aliases[]` (Back$ide Scalp, Rubber Band Scalp, Big Dog
   176	  Consolidation, Gap, Give and Go, Hitchhiker Scalp, Fashionably Late Scalp,
   177	  Back-Through Open).
   178	- **Loader.** Parses frontmatter with the existing `_FRONTMATTER_RE` pattern
   179	  (no new dependency), finds the `definition` section and its units with
   180	  `vaultwrite.markers`, loads the fenced YAML, injects id/name, validates
   181	  `TradeDef`, fails loud on any populated unit that does not validate. A unit
   182	  whose body is empty or holds only a partial mapping (see the matrix below) is a
   183	  **draft**: skipped with a listed warning, never an error. Frontmatter `status:`
   184	  is checked, not trusted: `defined` iff the unit validated, `draft` otherwise;
   185	  `playbook` is never typed (earned at n ≥ 30, R3). Frontmatter `class:` /
   186	  `family:` (d) are checked against the unit and any drift is listed; the human
   187	  wins; `cobalt taxonomy sync-frontmatter` re-aligns with a diff.
   188	  `python -m cobalt.taxonomy.validate` reads the vault.
   189	- **The three former cross-checks (b).**
   190	  1. `cameron_grid.yaml` → dies. The def's own `valid_setups[]` is the truth. The
     1	# Data-Source Spike, Phase A — Finviz Elite Export API
     2	
     3	**Method:** empirical probing only. There is no official Finviz API
     4	documentation; the 9 screenshots in `docs/90 - References/` (Finviz's
     5	own in-app "Automating Export" panels) were the starting point, not the
     6	spec — several details below were discovered by direct HTTP requests
     7	that contradict or extend what the screenshots show. Every finding is
     8	tagged **CONFIRMED** (fetched, evidence attached) or **INFERRED**
     9	(pattern/plausible, not independently verified) — the latter is Phase
    10	B's job to close (Dejan capturing the Finviz web pages, including the
    11	collapsed "Learn More" parameter panels the screenshots don't show).
    12	
    13	**Constraints honored:** read-only GETs only; ~1.2s between requests
    14	(≈50 requests total across two probe runs); auth token resolved via
    15	the existing vault-backed `FinvizApiClient` and never printed or logged
    16	— every URL and error string below is scrubbed. No FMP, no
    17	TradingView, no pipeline/old-tree code changes.
    18	
    19	**Probed:** 2026-08-27, against a live Finviz Elite Elite-tier account,
    20	ticker MSFT as the reference instrument for `/export/stock`.
    21	
    22	---
    23	
    24	## 0. Confirmed baseline from the old tree (`FinvizApiClient` + friends)
    25	
    26	Read: `src/cobalt_agent/skills/research/finviz_api.py` (the HTTP client —
    27	KEEP-AS-IS per TRIAGE, "grows"), `finviz_extractor.py` (Playwright
    28	scraper, TRIAGE-KILLed, browser-only info, not API-relevant),
    29	`enrich_metadata.py` (a live caller), and the `dev_utils/live_run_finviz*`
    30	scripts (thin wrappers, no new information).
    31	
    32	**What the client already gets right (CONFIRMED against my own probing):**
    33	- Base URL `https://elite.finviz.com`, token appended as `&auth=<token>`.
    34	  Matches every screenshot exactly.
    35	- `export.ashx?v=…&f=<filters>&c=<col indices>` for screener — the
    36	  `.ashx` path still works but 301-redirects to `/export/screener` (the
    37	  screenshots say this explicitly; I didn't re-verify the redirect
    38	  itself since old-tree code is out of scope to touch, but the
    39	  destination path is confirmed reachable directly).
    40	- `f=` filter syntax (`key_value` comma-joined, e.g.
    41	  `sh_price_o1,sh_avgvol_o5000`) — CONFIRMED, used throughout my probes.
    42	- `c=` column-index selection — CONFIRMED exactly: requesting
    43	  `c=0,1,2,3,4,5,6` returned precisely those 7 columns in that order.
    44	- `MASTER_COLUMNS` (indices `0`–`150`, 151 total) — CONFIRMED: a single
    45	  `c=0..150` request returned exactly 151 named columns (full list in
    46	  §1 Screener below). The client's assumption that this is a stable,
    47	  complete field universe is validated.
    48	- `t=` as a direct multi-ticker override for `export.ashx` (used in
    49	  `enrich_metadata.py`, bypassing the filter compiler) — CONFIRMED as a
    50	  general pattern; ticker-list-via-`t=` also works on other endpoints
    51	  (see per-family notes).
    52	
    53	**Where probing contradicts or extends the client's assumptions:**
    54	
    55	| Client assumption | Finding |
    56	|---|---|
    57	| `get_news(ticker)` — passing a ticker filters the news feed (`news_export.ashx?t={ticker}`) | **CONTRADICTED.** `/export/news?v=1` and `/export/news?v=1&t=MSFT` returned byte-identical first rows (same headline, same everything) across the full response. `t=` appears to have **no effect** on `/export/news` — it always returns the general market feed. See §1 News and §4. |
    58	| `get_quote()` targets `quote_export.ashx?t={ticker}&ty=c&p=d&b=1` | **Superseded, not confirmed necessary.** The documented current endpoint is `/export/stock?t=…&p=…` with no `ty=`/`b=` params at all (confirmed in the Stock screenshot's example URL). New-core `prefill.py` already moved off this legacy path for exactly this reason (the `.ashx` form 301-redirects). `ty=c`/`b=1` were not independently tested — they may be inert legacy params from an older API surface. |
    59	| `PRESET_QUERIES` use `v=150`; `execute_dynamic_screener` uses `v=152` | **Not a contradiction.** The official screenshot's own example uses `v=111`. All three values I've now seen work — `v=` looks like a Finviz-internal "view/column-preset ID" selector, not a version number; multiple valid IDs coexist. |
    60	| `PRESET_QUERIES` all include `ft=4` | **UNVERIFIED — not isolated.** I never tested `ft=` in isolation (the client always pairs it with a filter set). Meaning unconfirmed; likely a filter-type/universe toggle. Flagged for Phase B. |
    61	| `tc=7` used nowhere in the old client, but discovered on the Insider screenshot | Confirmed as a working filter parameter (see §1 Insider) but its **value semantics are unknown** — "7" is a Finviz-internal transaction-type code, not a raw SEC Form 4 code letter. INFERRED that other integers select other transaction types; not probed. |
    62	
    63	---
    64	
    65	## 1. Per-family findings (all eleven)
    66	
    67	Each entry: endpoint path, params tried, **CONFIRMED** result, and gaps.
    68	
    69	### Screener — CONFIRMED, working exactly as documented
    70	`GET /export/screener?v=<id>&f=<filters>&c=<col indices>&auth=…`
    71	- `v=111` (default view) → 200, 11 columns (`No., Ticker, Company,
    72	  Sector, Industry, Country, Market Cap, P/E, Price, Change, Volume`).
    73	- `v=152&c=0,1,2,3,4,5,6` → 200, exactly the 7 requested columns.
    74	- `v=152&c=0..150` (all indices) → 200, **all 151 named columns**,
    75	  confirming the client's `MASTER_COLUMNS` claim. Full field list (a
    76	  sample of the notable ones — Tier-1/Tier-2 relevant fields bolded):
    77	  `No, Ticker, Company, Sector, Industry, Country, Market Cap, P/E,
    78	  Forward P/E, PEG, P/S, P/B, P/Cash, P/FCF, Dividend Yield, Payout
    79	  Ratio, EPS(ttm), EPS Growth (This/Next Year, Past/Next 5Y, QoQ), Sales
    80	  Growth (Past 5Y, QoQ), **Shares Outstanding, Shares Float, Insider
    81	  Ownership, Insider Transactions, Institutional Ownership,
    82	  Institutional Transactions, Short Float, Short Ratio**, Return on
    83	  (Assets/Equity/Invested Capital), Current/Quick Ratio, LT/Total
    84	  Debt-to-Equity, Gross/Operating/Profit Margin, Performance (Week
    85	  through YTD, plus **1/2/3/5/10/15/30-min and 1/2/4-hour rolling
    86	  performance — 10 intraday-granularity columns**), Beta, **Average
    87	  True Range**, Volatility (Week/Month), 20/50/200-day SMA, 50-day &
    88	  52-week High/Low, RSI(14), Change from Open, Gap, Analyst Recom,
    89	  Average/Relative Volume, Price, Change, Volume, **Earnings Date**,
    90	  Target Price, IPO Date, After-Hours Close/Change/Volume, Book/Cash
    91	  per share, Dividend, Employees, **EPS Next Q, Income, Optionable,
    92	  Shortable, Short Interest, Float %**, OHL, Trades, [ETF-only block:
    93	  Asset Type, ETF Type, Region, Category, Tags, AUM, NAV, Net Flows
    94	  (1M/3M/YTD/1Y), multi-year Returns], **EPS/Revenue Surprise**,
    95	  Exchange, Dividend TTM/Ex-Date, 52-Week Range, **News Time, News URL,
    96	  News Title**, 3/5/10-year Performance, EPS/Sales Growth 3Y, Enterprise
    97	  Value, EV/EBITDA, EV/Sales, Dividend Growth (1/3/5Y), Daily Digest.
    98	- **New finding, not in any screenshot:** columns 135–137 (`News Time`,
    99	  `News URL`, `News Title`) put a per-ticker latest-headline directly in
   100	  screener output. Given `/export/news`'s `t=` filter doesn't work
   101	  (above), **this may be the actual working path to per-ticker news**,
   102	  not the dedicated News endpoint. INFERRED — only saw the column names
   103	  exist and are part of the schema; didn't verify populated values for
   104	  a specific low-news ticker vs. a high-news one.
   105	- Gap: `ft=` parameter meaning unconfirmed (see §0).
   106	
   107	### Portfolio — CONFIRMED endpoint exists, needs a real Dejan-owned ID
   108	`GET /export/portfolio?pid=<id>&auth=…`
   109	- Bare and `pid=1` both → **404, body `"Portfolio not found."`** — a
   110	  specific, meaningful error (not a generic route-404), confirming the
   111	  endpoint and `pid=` param both exist and are being validated, but no
   112	  portfolio with ID `1` exists on this account. INFERRED that `pid=`
   113	  needs one of Dejan's own saved-portfolio IDs from the Finviz UI —
   114	  untested with a real one (none created yet). Gap for Phase B.
   115	
   116	### Stock — see §2, the priority section.
   117	
   118	### Groups — CONFIRMED reachable, response empty with params tried
   119	`GET /export/groups?g=<?>&auth=…`
   120	- Bare and `g=sector` both → **200, `text/csv`, empty body.** The route
   121	  exists and doesn't error, but produces no rows with either param
   122	  tried. INFERRED that a required param (view ID like `v=`, or a
   123	  different `g=` enum value — Finviz's UI groups by sector, industry,
   124	  country, capitalization) is missing. Gap for Phase B — this family is
   125	  the least-confirmed of the eleven.
   126	
   127	### Options — CONFIRMED
   128	`GET /export/options?t=<ticker>&ty=oc&e=<expiry YYYY-MM-DD>&auth=…`
   129	- `t=MSFT&ty=oc&e=2026-09-18` → 200, 206 rows, 17 columns: `Contract
   130	  Name, Last Trade, Strike, Last Close, Bid, Ask, Change $, Change %,
   131	  Volume, Open Int., Type, IV, Delta, Gamma, Theta, Vega, Rho`.
   132	- Full Greeks present (Delta/Gamma/Theta/Vega/Rho) — stronger than
   133	  §8 Tier-3's minimum ask (IV rank/skew/OI). IV rank/percentile and term
   134	  structure are NOT directly given (only per-contract IV) — would need
   135	  to be computed from repeated pulls across expiries/dates.
   136	- `ty=` only tested as `oc`; other values (single-strike view?) INFERRED
   137	  to exist, not probed (Tier-3 is "design now, build later" — matches
   138	  the low-effort spend here).
   139	
   140	### Latest Filings — CONFIRMED
   141	`GET /export/latest-filings?t=<ticker>&o=<sort>&auth=…`
   142	- `t=MSFT&o=-filingDate` → 200, 1828 rows, 6 columns: `Filing Date,
   143	  Report Date, Form, Description, Filing, Document`.
   144	- The `Form` column (10-K, 10-Q, 8-K, S-3, 424B5, Form 4, …) makes this
   145	  a plausible, previously-unconsidered path toward §8 Tier-1's
   146	  dilution-risk monitoring (effective S-3s/ATMs) — filter/scan `Form`
   147	  client-side. Not filed as a direct requirements match originally;
   148	  worth a design note.
   149	
   150	### News — CONFIRMED, with the client-contradicting finding from §0
   151	`GET /export/news?v=1[&t=<ticker>]&auth=…`
   152	- `v=1` → 200, 180 rows, 5 columns: `Title, Source, Date, Url,
   153	  Category`.
   154	- `v=1&t=MSFT` → 200, 180 rows, **identical first row to the
   155	  ticker-less call**. `t=` is not filtering. See §0's contradiction
   156	  entry and §4.
   157	- `v=` only tested as `1`; other values INFERRED to exist (maybe a
   158	  blogs/press-release toggle) — not probed.
   159	
   160	### Insider — CONFIRMED, filtering works
   161	`GET /export/insiders?tc=<code>[&t=<ticker>]&auth=…`
   162	- `tc=7` alone → 200, 200 rows (**hit what looks like a row cap** — see
   163	  Managers/Funds below for a *documented* 500-row cap; 200 may be a
   164	  separate, undocumented cap for this family, or coincidental — not
   165	  isolated).
   166	- `tc=7&t=MSFT` → 200, 94 rows — **different from the untargeted count,
   167	  confirming `t=` DOES filter here** (unlike News). 12 columns: `Ticker,
   168	  Owner, Owner CIK, Relationship, Date, Transaction, Cost, #Shares,
   169	  Value ($), #Shares Total, SEC Form 4, SEC Form 4 Link`.
   170	- `tc=` value semantics (why "7") — INFERRED/unknown, gap for Phase B.
   171	
   172	### Managers — CONFIRMED, exact mechanics as documented
   173	- List: `GET /export/managers?search=<partial name>&auth=…` — `search=
   174	  berkshire` → 200, 10 rows, 14 columns (`Name, Portfolio Manager,
   175	  Investor ID, Report Date, Portfolio Value, # Investments, New
   176	  Purchased, Sold Out, Added, Reduced, Top 10 Concentration (%),
   177	  Turnover (%), Time Held Top 10, Time Held All`). **500-row cap is
   178	  documented in-app** (screenshot text), not hit here since the search
   179	  matched only 10.
   180	- Holdings: `GET /export/managers/<investor ID>/holdings&auth=…` (path
   181	  segment, not a query param — confirmed both the bare-ID form and the
   182	  name-slug form work per the screenshot; I used the bare-ID form live)
   183	  → 200, 30 rows, 14 columns (`Ticker, Name, Type, Sector, Industry,
   184	  Shares Held, Market Value, % Portfolio, Prev. % Portfolio, Change in
   185	  Shares, % Change, % Ownership, Avg. Price, Q 1st Owned`).
   186	
   187	### Funds — CONFIRMED, identical mechanics to Managers
   188	- List: `GET /export/funds?search=<partial name>&auth=…` — `search=
   189	  fidelity` → 200, **exactly 500 rows** — the documented row cap
   190	  **CONFIRMED hit** in practice. 14 columns (same shape as Managers'
     1	"""Finviz `/export/stock` intraday-bar fetcher. Fail-loud, secret-safe.
     2	
     3	Reuses the existing vault-backed `FinvizApiClient` for token resolution
     4	only (same one-directional read-across-the-strangler-boundary pattern
     5	as `aset/prefill.py`) — the old tree stays untouched.
     6	
     7	Per DATA-SOURCE-MEMO.md's confirmed findings:
     8	- `p=` is a validated enum here (Interval) — bare/unrecognized values
     9	  silently return the full daily dataset with no error. Any response
    10	  whose dates lack a time-of-day component is exactly that failure
    11	  mode and is rejected loudly, never stored.
    12	- Response columns are always exactly Date, Open, High, Low, Close,
    13	  Volume — a mismatch is also rejected loudly.
    14	- Finviz's own date strings are inconsistently formatted between
    15	  intervals (`i1/i2/i5` give clean 12-hour "04:00 AM"; `i15/i30` have
    16	  been observed giving a 24-hour hour with a bolted-on AM/PM suffix
    17	  like "15:45 PM") — `_parse_finviz_datetime` handles both.
    18	
    19	TIMEZONE (ADR-0007, 2026-09-04). Finviz's export carries a bare ET
    20	wall clock with no offset and no tz name — "09/03/2026 09:30 AM" is
    21	09:30 *America/New_York*. Until ADR-0007 this parser returned that
    22	naive value unchanged, psycopg handed it to a `timestamptz` column,
    23	and Postgres (session `TimeZone = Etc/UTC`) stamped it `09:30+00`.
    24	4.75M rows were therefore ET digits wearing a UTC label: every one of
    25	them wrong by the ET offset, and every join against them wrong by the
    26	same. The corpus was reinterpreted in place by ADR-0007; this parser
    27	is the other half — it localizes to `America/New_York` (DST-aware, so
    28	the offset is the one that applied on that date) and converts to UTC
    29	before the value ever reaches a `Bar`. Bars are tz-aware UTC from
    30	here on; sessions are reasoned about in ET by `cobalt.session`, never
    31	by wall clock.
    32	"""
    33	
    34	import csv
    35	import io
    36	import re
    37	from datetime import datetime, timezone
    38	from decimal import Decimal, InvalidOperation
    39	from zoneinfo import ZoneInfo
    40	
    41	import httpx
    42	
    43	from cobalt_agent.skills.research.finviz_api import FinvizApiClient
    44	
    45	from .models import Bar, Interval
    46	
    47	EXPECTED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]
    48	_AUTH_RE = re.compile(r"auth=[^&\s'\"]+")
    49	
    50	# Finviz's export timestamps are bare ET wall clock (ADR-0007).
    51	FINVIZ_TZ = ZoneInfo("America/New_York")
    52	
    53	
    54	class CollectorError(RuntimeError):
    55	    """Fetch or shape-validation failure — never store, never guess."""
    56	
    57	
    58	def scrub(text: str) -> str:
    59	    return _AUTH_RE.sub("auth=REDACTED", text)
    60	
    61	
    62	async def resolve_token() -> str:
    63	    client = FinvizApiClient()
    64	    try:
    65	        return await client._resolve_vault_credentials(client.FINVIZ_DOMAIN)
    66	    except Exception as e:
    67	        raise CollectorError(f"Finviz token resolution failed: {scrub(str(e))}") from e
    68	
    69	
    70	def _parse_finviz_datetime(raw: str) -> datetime:
    71	    """Parse one Finviz date cell into a tz-aware UTC datetime.
    72	
    73	    The string is a bare ET wall clock. It is localized to
    74	    `America/New_York` and converted to UTC (ADR-0007) — the returned
    75	    value is ALWAYS tz-aware, never naive.
    76	    """
    77	    return _parse_finviz_wall_clock(raw).replace(tzinfo=FINVIZ_TZ).astimezone(
    78	        timezone.utc
    79	    )
    80	
    81	
    82	def _parse_finviz_wall_clock(raw: str) -> datetime:
    83	    """The naive ET wall clock exactly as Finviz wrote it. Format handling
    84	    only — the timezone is applied by `_parse_finviz_datetime`."""
    85	    raw = raw.strip()
    86	    parts = raw.split(" ")
    87	    if len(parts) < 2:
    88	        # No time-of-day component at all -> this is the daily-fallback
    89	        # shape (bare/unrecognized p= silently returns daily). We never
    90	        # request daily, so this is always a failure, never a valid row.
    91	        raise CollectorError(
    92	            f"Date {raw!r} has no time-of-day component — Finviz likely "
    93	            "fell back to daily (unrecognized interval), refusing to store."
    94	        )
    95	    date_part, time_part = parts[0], parts[1]
    96	
    97	    # Clean 12-hour form: "04:00 AM" / "06:52 AM" (date_part time_part meridiem)
    98	    try:
    99	        return datetime.strptime(raw, "%m/%d/%Y %I:%M %p")
   100	    except ValueError:
   101	        pass
   102	
   103	    # Observed quirk: a 24-hour hour with a bolted-on AM/PM suffix, e.g.
   104	    # "08/26/2026 15:45 PM". Parse the 24-hour time, ignore the suffix.
   105	    try:
   106	        return datetime.strptime(f"{date_part} {time_part}", "%m/%d/%Y %H:%M")
   107	    except ValueError:
   108	        pass
   109	
   110	    raise CollectorError(f"Unparseable Finviz datetime: {raw!r}")
   111	
   112	
   113	def parse_csv_response(text: str, ticker: str, interval: Interval) -> list[Bar]:
   114	    """Pure parsing/validation — no I/O. Raises CollectorError on any
   115	    shape mismatch; never returns a partial or guessed result."""
   116	    rows = list(csv.reader(io.StringIO(text)))
   117	    if not rows:
   118	        raise CollectorError(f"Empty response for {ticker}/{interval.value}.")
   119	
   120	    header = rows[0]
   121	    if header != EXPECTED_COLUMNS:
   122	        raise CollectorError(
   123	            f"Unexpected columns for {ticker}/{interval.value}: {header} "
   124	            f"(expected {EXPECTED_COLUMNS})"
   125	        )
   126	
   127	    if len(rows) == 1:
   128	        raise CollectorError(f"No data rows for {ticker}/{interval.value}.")
   129	
   130	    bars: list[Bar] = []
   131	    for row in rows[1:]:
   132	        if len(row) != 6:
   133	            raise CollectorError(
   134	                f"Malformed row for {ticker}/{interval.value}: {row!r}"
   135	            )
   136	        date_s, open_s, high_s, low_s, close_s, vol_s = row
   137	        try:
   138	            ts = _parse_finviz_datetime(date_s)
   139	            bars.append(
   140	                Bar(
   141	                    ticker=ticker,
   142	                    interval=interval,
   143	                    ts=ts,
   144	                    open=Decimal(open_s),
   145	                    high=Decimal(high_s),
   146	                    low=Decimal(low_s),
   147	                    close=Decimal(close_s),
   148	                    volume=int(Decimal(vol_s)),
   149	                )
   150	            )
   151	        except (InvalidOperation, ValueError) as e:
   152	            raise CollectorError(
   153	                f"Unparseable row for {ticker}/{interval.value}: {row!r} ({e})"
   154	            ) from e
   155	
   156	    return bars
   157	
   158	
   159	async def fetch_bars(ticker: str, interval: Interval, token: str) -> list[Bar]:
   160	    """Fetch one (ticker, interval)'s bars over the network, then
   161	    validate/parse via `parse_csv_response`."""
   162	    ticker = ticker.strip().upper()
   163	    url = "https://elite.finviz.com/export/stock"
   164	    params = {"t": ticker, "p": interval.value, "auth": token}
   165	    try:
   166	        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
   167	            response = await client.get(url, params=params)
   168	            response.raise_for_status()
   169	    except Exception as e:
   170	        raise CollectorError(
   171	            f"Fetch failed for {ticker}/{interval.value}: {scrub(str(e))}"
   172	        ) from e
   173	
   174	    return parse_csv_response(response.text, ticker, interval)

codex
The addendum conflicts with several build instructions: account-mode refusal, vault-owned pool rules, credential handling, and restart rules. I’m also checking whether the proposed collector and job interfaces can support the stated acceptance tests.
exec
/bin/zsh -lc "nl -ba src/cobalt/jobs/wrapper.py | sed -n '1,280p'; nl -ba src/cobalt/jobs/watchdog.py | sed -n '305,415p'; nl -ba src/cobalt/db_migrations/cli.py | sed -n '1,255p'; cat src/cobalt/db_migrations/__init__.py; nl -ba src/cobalt/db_migrations/placement.py | tail -70" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
     1	"""F17b: the wrapper every scheduled job runs inside.
     2	
     3	Charter §3 F17: "marks running/done/failed with exit code and stamps
     4	heartbeat_at at least every timeout_s/3 for long jobs."
     5	
     6	TWO WAYS IN, one implementation:
     7	
     8	    # a Python entry point (prefill, archiver, cards-expire, …)
     9	    with job_run("com.cobalt.archiver") as run:
    10	        summary = do_the_work()
    11	        run.result = {"rows_written": summary.rows_written}
    12	
    13	    # anything else, from a plist
    14	    uv run cobalt jobs run com.cobalt.prefill-daily -- uv run prefill daily
    15	
    16	WHAT IT GUARANTEES, in order:
    17	
    18	1. THE KILL SWITCH IS CHECKED FIRST. A stopped Cobalt does not start a
    19	   one-shot at all — except the heartbeat, whose validated registry flag
    20	   keeps the watcher running so it can report the stop itself.
    21	2. `running` is marked before the work, with `started_at`.
    22	3. A BEATER THREAD stamps `heartbeat_at` every `timeout_s /
    23	   jobs.heartbeat_fraction` (5 min for the 15-min archiver window). This
    24	   is the ONLY thing that distinguishes a long job from a hung one — the
    25	   archiver legitimately runs 23 minutes, so "started and did not
    26	   finish" cannot be the zombie test.
    27	4. `done` (exit 0) or `failed` (exit code + the exception, redacted
    28	   through F19 on the way into the column) — and `failed` is LOUD.
    29	5. The exception is RE-RAISED. The wrapper reports; it never swallows.
    30	
    31	The beater thread is a daemon: if the job process dies hard, the thread
    32	dies with it, `heartbeat_at` stops advancing, and the watchdog draws the
    33	right conclusion. A thread that outlived its job would keep a dead job
    34	looking alive, which is the exact failure this feature exists to catch.
    35	"""
    36	
    37	from __future__ import annotations
    38	
    39	import threading
    40	import traceback
    41	from contextlib import contextmanager
    42	from typing import Any, Optional
    43	
    44	from loguru import logger
    45	
    46	from . import killswitch
    47	from .config import JobSpec, load_job_registry
    48	from .store import JobStore
    49	
    50	#: The tunables row governing how often a long job stamps (F16).
    51	HEARTBEAT_FRACTION_KEY = "jobs.heartbeat_fraction"
    52	
    53	#: Exit code a job uses when the kill switch turned it away. ZERO, on
    54	#: purpose — see guarantee 1.
    55	STOPPED_EXIT_CODE = 0
    56	
    57	
    58	class JobStopped(RuntimeError):
    59	    """The kill switch is engaged; this run did not happen."""
    60	
    61	
    62	def heartbeat_fraction() -> int:
    63	    from cobalt.taxonomy.loader import load_tunables
    64	
    65	    row = load_tunables().by_key.get(HEARTBEAT_FRACTION_KEY)
    66	    if row is None:
    67	        raise RuntimeError(
    68	            f"tunable {HEARTBEAT_FRACTION_KEY!r} is missing from tunables.yaml — the "
    69	            "wrapper reads its stamp interval from config and has no built-in "
    70	            "default (F16)."
    71	        )
    72	    return int(row.value)
    73	
    74	
    75	class _Beater:
    76	    """Stamps `heartbeat_at` on a timer until the run ends."""
    77	
    78	    def __init__(self, store: JobStore, label: str, every_s: float):
    79	        self.store = store
    80	        self.label = label
    81	        self.every_s = max(1.0, every_s)
    82	        self._stop = threading.Event()
    83	        self._thread = threading.Thread(
    84	            target=self._loop, name=f"beat:{label}", daemon=True
    85	        )
    86	
    87	    def _loop(self) -> None:
    88	        while not self._stop.wait(self.every_s):
    89	            try:
    90	                self.store.beat(self.label)
    91	            except Exception as e:  # noqa: BLE001
    92	                # A missed stamp is not a reason to kill the job. It IS a
    93	                # reason to say so: the watchdog may conclude ZOMBIE from
    94	                # this, and an operator needs the other half of the story.
    95	                logger.error(
    96	                    "F17: heartbeat stamp FAILED for {} ({}: {}) — the job is still "
    97	                    "running; the watchdog may see a stale heartbeat.",
    98	                    self.label, type(e).__name__, e,
    99	                )
   100	
   101	    def __enter__(self) -> "_Beater":
   102	        self._thread.start()
   103	        return self
   104	
   105	    def __exit__(self, *exc) -> None:
   106	        self._stop.set()
   107	
   108	
   109	class JobRun:
   110	    """Handle a wrapped job can hang its result on."""
   111	
   112	    def __init__(self, spec: JobSpec):
   113	        self.spec = spec
   114	        self.label = spec.label
   115	        #: Whatever the run wants F18 to be able to report — the
   116	        #: archiver's `rows_written` is what makes "archiver freshness
   117	        #: (last run + rows written)" answerable.
   118	        self.result: Optional[dict[str, Any]] = None
   119	
   120	
   121	@contextmanager
   122	def job_run(
   123	    label: str,
   124	    *,
   125	    store: Optional[JobStore] = None,
   126	    register: bool = True,
   127	    allow_prod: bool = False,
   128	):
   129	    """Run a block as a registered job. See the module docstring."""
   130	    registry = load_job_registry()
   131	    spec = registry.spec(label)
   132	    store = store or JobStore()
   133	
   134	    def bookkeeping(stage: str, operation) -> bool:
   135	        try:
   136	            operation()
   137	            return True
   138	        except Exception as e:  # noqa: BLE001 - heartbeat must still launch
   139	            if not spec.kill_switch_exempt:
   140	                raise
   141	            logger.error(
   142	                "F17: {} {} FAILED ({}: {}) — heartbeat subprocess WILL STILL RUN; "
   143	                "its database probe and out-of-band alert own this outage.",
   144	                label, stage, type(e).__name__, e,
   145	            )
   146	            return False
   147	
   148	    bookkeeping(
   149	        "schema setup", lambda: store.ensure_schema(allow_prod=allow_prod)
   150	    )
   151	    if register:
   152	        bookkeeping(
   153	            "registration", lambda: store.register(spec, allow_prod=allow_prod)
   154	        )
   155	
   156	    if killswitch.is_active(store):
   157	        state = killswitch.read(store)
   158	        if not spec.kill_switch_exempt:
   159	            logger.error("F17: {} REFUSED TO START — {}", label, state.describe())
   160	            raise JobStopped(state.describe())
   161	        logger.error(
   162	            "F17: {} is kill-switch EXEMPT and WILL RUN — {}",
   163	            label,
   164	            state.describe(),
   165	        )
   166	
   167	    bookkeeping("mark_running", lambda: store.mark_running(label))
   168	    run = JobRun(spec)
   169	    every_s = spec.timeout_s / heartbeat_fraction()
   170	    logger.info(
   171	        "F17: {} RUNNING (timeout {}s, heartbeat every {:.0f}s)",
   172	        label, spec.timeout_s, every_s,
   173	    )
   174	    try:
   175	        with _Beater(store, label, every_s):
   176	            yield run
   177	    except BaseException as e:
   178	        error = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}"
   179	        finish = store.mark_wrapper_finished if spec.kill_switch_exempt else store.mark_finished
   180	        bookkeeping(
   181	            "mark_finished",
   182	            lambda: finish(
   183	                label,
   184	                exit_code=1,
   185	                error=error,
   186	                result=run.result,
   187	            ),
   188	        )
   189	        logger.error("F17: {} FAILED — {}: {}", label, type(e).__name__, e)
   190	        raise            # the wrapper reports; it never swallows
   191	    finish = store.mark_wrapper_finished if spec.kill_switch_exempt else store.mark_finished
   192	    bookkeeping(
   193	        "mark_finished",
   194	        lambda: finish(label, exit_code=0, result=run.result),
   195	    )
   196	    logger.info("F17: {} DONE", label)
   197	
   198	
   199	def should_keep_running(label: str, *, store: Optional[JobStore] = None) -> bool:
   200	    """A RESIDENT's own loop check. `False` means exit cleanly now.
   201	
   202	    Residents call this where they can stop without tearing out of a
   203	    write. Cobalt's residents today are supervised by launchd rather than
   204	    wrapped (see jobs.yaml), so this exists for the first new-core
   205	    resident — the S2 radar poller — and for anything the chief of staff
   206	    grows into.
   207	    """
   208	    if killswitch.is_active(store):
   209	        logger.error(
   210	            "F17: kill switch engaged — {} is exiting cleanly at its next safe point.",
   211	            label,
   212	        )
   213	        return False
   214	    return True
   215	
   216	
   217	__all__ = [
   218	    "HEARTBEAT_FRACTION_KEY",
   219	    "STOPPED_EXIT_CODE",
   220	    "JobRun",
   221	    "JobStopped",
   222	    "heartbeat_fraction",
   223	    "job_run",
   224	    "should_keep_running",
   225	]
   305	    store.ensure_schema()
   306	    ts = now or clock_mod.now_utc()
   307	    now_et = session_clock().to_et(ts)
   308	    fraction = _tunable_int("jobs.heartbeat_fraction")
   309	    grace = timedelta(minutes=_tunable_int(MISSED_GRACE_KEY))
   310	
   311	    findings: list[Finding] = []
   312	    rows = {r["label"]: r for r in store.all()}
   313	
   314	    for spec in registry.jobs:
   315	        row = rows.get(spec.label)
   316	
   317	        # -- IS THIS JOB EVEN SUPPOSED TO BE LOADED? A registry row with
   318	        # `enabled: false` is a job that has been BUILT and reviewed but
   319	        # not yet handed over to launchd. Every check below asks a
   320	        # question whose honest answer for such a job is "of course not"
   321	        # — probing it would put a permanent red on the beat for a state
   322	        # somebody chose deliberately, and a standing red is how a
   323	        # heartbeat stops being read. It is REPORTED, not hidden: the
   324	        # line is on the block, it just is not a failure.
   325	        if not spec.enabled:
   326	            findings.append(
   327	                Finding(
   328	                    spec.label, True, "disabled",
   329	                    "registered but NOT LOADED BY DESIGN (`enabled: false` in "
   330	                    "configs/cobalt/jobs.yaml) — nothing is probed and nothing is "
   331	                    "claimed. Flip the flag as the last step of its handover.",
   332	                )
   333	            )
   334	            continue
   335	
   336	        # -- IS THE PLIST EVEN LOADED? Charter §3 F18: "every ops plist
   337	        # loaded + last exit code". Asked of EVERY job, resident and
   338	        # one-shot alike, and asked FIRST.
   339	        #
   340	        # This check was missing from the first version of this function,
   341	        # and running the Charter's own acceptance test for real is what
   342	        # found it: `launchctl bootout com.cobalt.cards-expire` and the
   343	        # heartbeat stayed green, because a one-shot between runs looks
   344	        # identical whether its plist is loaded or gone. An unloaded
   345	        # one-shot has no PID to lose and no state to change — it simply
   346	        # never fires again, and MISSED would not say so until its next
   347	        # scheduled time plus the grace, which for a Friday-evening
   348	        # unload is Monday.
   349	        if probe:
   350	            try:
   351	                status = launchctl_status(spec.label)
   352	            except Exception as e:  # noqa: BLE001
   353	                findings.append(
   354	                    Finding(spec.label, False, (row or {}).get("state", "unknown"),
   355	                            f"launchd PROBE FAILED ({type(e).__name__}: {e}) — loaded "
   356	                            "state UNKNOWN, which is not the same as loaded")
   357	                )
   358	                continue
   359	            if not status.loaded:
   360	                # A RESIDENT's row IS its liveness, so it is marked. A
   361	                # ONE-SHOT's row is the record of its LAST RUN, and
   362	                # "the plist is gone" is a fact about launchd, not about
   363	                # that run — overwriting `state` and `exit_code` with it
   364	                # would destroy the only record of how the job last
   365	                # ended, and leave a stale `failed` behind after the
   366	                # plist is reloaded (which is exactly what happened the
   367	                # first time this ran: reload restored the plist and the
   368	                # row still said failed). It is reported, not written.
   369	                if row is not None and spec.kind is JobKind.RESIDENT:
   370	                    store.mark_probe(spec.label, alive=False, detail=status.detail, now=ts)
   371	                findings.append(Finding(spec.label, False, "not loaded", status.detail))
   372	                continue
   373	
   374	        if row is None:
   375	            store.register(spec)
   376	            findings.append(
   377	                Finding(spec.label, False, "unregistered",
   378	                        "no jobs row existed — registered now; nothing has run yet")
   379	            )
   380	            continue
   381	
   382	        # -- residents someone else supervises: PROBE them -------------
   383	        if spec.supervisor is not Supervisor.SELF:
   384	            if not probe:
   385	                findings.append(Finding(spec.label, True, row["state"], "probe skipped"))
   386	                continue
   387	            try:
   388	                if spec.supervisor is Supervisor.LAUNCHD:
   389	                    alive = status.pid is not None
   390	                    detail = status.detail
   391	                else:
   392	                    alive, detail = pidfile_alive(spec)
   393	            except Exception as e:  # noqa: BLE001 - a broken probe is its own red
   394	                findings.append(
   395	                    Finding(spec.label, False, row["state"],
   396	                            f"PROBE FAILED ({type(e).__name__}: {e}) — liveness UNKNOWN, "
   397	                            "which is not the same as 'up' and is reported as red")
   398	                )
   399	                continue
   400	            store.mark_probe(spec.label, alive=alive, detail=detail, now=ts)
   401	            findings.append(
   402	                Finding(
   403	                    spec.label, alive,
   404	                    JobState.RUNNING.value if alive else JobState.FAILED.value,
   405	                    f"{detail} [{spec.supervisor} probe]",
   406	                )
   407	            )
   408	            continue
   409	
   410	        # -- jobs the wrapper reports on -------------------------------
   411	        state = row["state"]
   412	
   413	        if state == JobState.RUNNING.value:
   414	            started, beat = row["started_at"], row["heartbeat_at"]
   415	            ran_for = (ts - started).total_seconds() if started else 0
     1	"""`cobalt db migrate [--allow-prod] [--rollback]` — ADR-0008's harness.
     2	
     3	WHAT IT PRINTS IS THE POINT. A migration that moves twelve tables between
     4	schemas and adds a column to six of them is a migration whose claim
     5	("nothing was lost") has to be checkable by looking, not by trusting. So
     6	every run captures, per table, BEFORE and AFTER:
     7	
     8	  * where it lives (`public` / `system` / `"user"`),
     9	  * `count(*)`,
    10	  * a content digest: `md5(string_agg(row::text, '|' ORDER BY <pk>))`.
    11	
    12	THE DIGEST EXCLUDES every column added by these migrations: `user_id`,
    13	`vault_outcome`, and `vault_reason`. A digest over the whole row would
    14	differ before and after by construction and would prove nothing. Taking
    15	it over `to_jsonb(t)` minus those columns makes the two digests comparable,
    16	and an inequality is a real finding: the rows themselves changed. `to_jsonb`
    17	serialises keys in a stable order, so the digest does not depend on
    18	column order either — which matters, because `SET SCHEMA` and `ADD
    19	COLUMN` both touch the catalog the naive `row::text` reads.
    20	
    21	ORDERED BY THE PRIMARY KEY, read from the catalog per table rather than
    22	hard-coded: `bars` is keyed `(ticker, interval, ts)`, `day_modes` by
    23	`trade_date`, `cobalt_jobs` by `label`, the rest by `id`.
    24	
    25	`--rollback` runs the registered reverse migrations newest-first
    26	and prints the same proof table. Running `migrate`, then `--rollback`,
    27	then `migrate` again must land on the same digests — the suite asserts
    28	exactly that round-trip on `cobalt_dev`.
    29	
    30	`--allow-prod` reaches `cobalt_brain` without flipping the process into
    31	production mode (RULING 7's one-off-tooling seam). Without it the target
    32	is whatever `COBALT_ENV` resolves.
    33	"""
    34	
    35	from __future__ import annotations
    36	
    37	import argparse
    38	from typing import Optional
    39	
    40	from psycopg import sql
    41	
    42	from cobalt import db, env
    43	
    44	from . import FORWARD, REVERSE
    45	from .placement import MOVED_TABLES, SEEDED_TABLES
    46	
    47	#: Columns introduced by the registered migrations. Excluding them makes a
    48	#: populated row comparable before and after a shape-only migration.
    49	DIGEST_EXCLUDED_COLUMNS = ("user_id", "vault_outcome", "vault_reason")
    50	
    51	#: Where a new-core table may legitimately be found, in look-up order.
    52	SEARCHED_SCHEMAS = ("public", "user", "system")
    53	
    54	
    55	class MigrationError(RuntimeError):
    56	    """The migration could not be run or could not be proven."""
    57	
    58	
    59	def _schema_of(conn, table: str) -> Optional[str]:
    60	    row = conn.execute(
    61	        "SELECT schemaname FROM pg_tables "
    62	        "WHERE tablename = %s AND schemaname = ANY(%s) LIMIT 1",
    63	        (table, list(SEARCHED_SCHEMAS)),
    64	    ).fetchone()
    65	    return row[0] if row else None
    66	
    67	
    68	def _pk_columns(conn, schema: str, table: str) -> list[str]:
    69	    rows = conn.execute(
    70	        """
    71	        SELECT a.attname
    72	        FROM pg_index i
    73	        JOIN pg_attribute a
    74	          ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
    75	        WHERE i.indrelid = (quote_ident(%s) || '.' || quote_ident(%s))::regclass
    76	          AND i.indisprimary
    77	        ORDER BY array_position(i.indkey::int2[], a.attnum)
    78	        """,
    79	        (schema, table),
    80	    ).fetchall()
    81	    if not rows:
    82	        raise MigrationError(
    83	            f"{schema}.{table} has no primary key, so its rows cannot be put in a "
    84	            "deterministic order and no content digest can be taken. Every "
    85	            "new-core table has one; this is a real finding, not a tooling gap."
    86	        )
    87	    return [r[0] for r in rows]
    88	
    89	
    90	def _probe(conn, table: str) -> dict:
    91	    """(schema, rows, digest) for `table`, wherever it currently lives."""
    92	    schema = _schema_of(conn, table)
    93	    if schema is None:
    94	        return {"schema": None, "rows": None, "digest": None}
    95	    pk = _pk_columns(conn, schema, table)
    96	    row_json = sql.SQL("to_jsonb(t)")
    97	    for column in DIGEST_EXCLUDED_COLUMNS:
    98	        row_json = sql.SQL("({row_json} - {column})").format(
    99	            row_json=row_json, column=sql.Literal(column)
   100	        )
   101	    query = sql.SQL(
   102	        "SELECT count(*), "
   103	        "md5(coalesce(string_agg(({row_json})::text, '|' ORDER BY {order}), '')) "
   104	        "FROM {rel} AS t"
   105	    ).format(
   106	        row_json=row_json,
   107	        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
   108	        rel=sql.Identifier(schema, table),
   109	    )
   110	    rows, digest = conn.execute(query).fetchone()
   111	    return {"schema": schema, "rows": int(rows), "digest": digest}
   112	
   113	
   114	def _probe_all(conn) -> dict[str, dict]:
   115	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
   116	    return {t: _probe(conn, t) for t in sorted(tables)}
   117	
   118	
   119	def _print_proof(before: dict[str, dict], after: dict[str, dict]) -> int:
   120	    """Render the proof table. Returns the number of CHANGED digests."""
   121	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
   122	    header = (
   123	        f"{'table':<20} {'side':<7} {'schema before -> after':<26} "
   124	        f"{'rows':<15} {'digest before -> after':<21} verdict"
   125	    )
   126	    print(header)
   127	    print("-" * len(header))
   128	    changed = 0
   129	    for name in sorted(tables):
   130	        b, a = before[name], after[name]
   131	        where = f"{b['schema'] or '-'} -> {a['schema'] or '-'}"
   132	        rows = f"{'-' if b['rows'] is None else b['rows']} -> " \
   133	               f"{'-' if a['rows'] is None else a['rows']}"
   134	        dig = f"{(b['digest'] or '-')[:8]} -> {(a['digest'] or '-')[:8]}"
   135	        if b["schema"] is None and a["schema"] is None:
   136	            verdict = "ABSENT"
   137	        elif b["digest"] == a["digest"] and b["rows"] == a["rows"]:
   138	            verdict = "OK"
   139	        elif b["schema"] is None:
   140	            verdict = "CREATED"
   141	        else:
   142	            verdict = "CHANGED"
   143	            changed += 1
   144	        print(
   145	            f"{name:<20} {tables[name].value:<7} {where:<26} {rows:<15} "
   146	            f"{dig:<21} {verdict}"
   147	        )
   148	    print("-" * len(header))
   149	    print(
   150	        f"{len(tables)} table(s) proven; digest excludes "
   151	        f"{', '.join(DIGEST_EXCLUDED_COLUMNS)}. "
   152	        + ("content UNCHANGED on every table."
   153	           if changed == 0
   154	           else f"{changed} table(s) CHANGED — investigate before proceeding.")
   155	    )
   156	    return changed
   157	
   158	
   159	def _apply(conn, paths) -> None:
   160	    """Run whole .sql files, one transaction for the lot.
   161	
   162	    Each file is handed to the server ENTIRE rather than split on ';':
   163	    these migrations are DO blocks, and a splitter would cut them at the
   164	    first semicolon inside the body. psycopg uses the simple query
   165	    protocol when there are no parameters, which accepts multiple
   166	    statements — and the migrations take no parameters by design.
   167	    """
   168	    for path in paths:
   169	        print(f"-- applying {path.name}")
   170	        conn.execute(path.read_text())
   171	
   172	
   173	def cmd_migrate(args: argparse.Namespace) -> None:
   174	    dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()
   175	    direction = "ROLLBACK" if args.rollback else "FORWARD"
   176	    paths = REVERSE if args.rollback else FORWARD
   177	
   178	    print(f"cobalt db migrate — {direction} on {dbname}")
   179	    conn = db.connect_migration(dbname, allow_prod=args.allow_prod)
   180	    conn.autocommit = False
   181	    try:
   182	        before = _probe_all(conn)
   183	        _apply(conn, paths)
   184	        after = _probe_all(conn)
   185	        conn.commit()
   186	    except BaseException:
   187	        conn.rollback()
   188	        raise
   189	    finally:
   190	        conn.close()
   191	
   192	    print()
   193	    changed = _print_proof(before, after)
   194	    if changed:
   195	        raise MigrationError(
   196	            f"{changed} table(s) changed content across the migration. The "
   197	            "migration is committed; the proof is not clean — compare against the "
   198	            "pg_dump taken before this run."
   199	        )
   200	
   201	
   202	def add_parser(sub) -> None:
   203	    group = sub.add_parser("db", help="Database migrations (ADR-0008 two-layer model)")
   204	    gsub = group.add_subparsers(dest="command", required=True)
   205	
   206	    migrate = gsub.add_parser(
   207	        "migrate",
   208	        help="Create the system/\"user\" schemas and move every new-core table.",
   209	    )
   210	    migrate.add_argument(
   211	        "--allow-prod",
   212	        action="store_true",
   213	        help="Target cobalt_brain (run from ~/cobalt only, outside market hours).",
   214	    )
   215	    migrate.add_argument(
   216	        "--rollback",
   217	        action="store_true",
   218	        help="Reverse registered migrations: heartbeat columns dropped, tables moved to public.",
   219	    )
   220	    migrate.set_defaults(func=cmd_migrate)
   221	
   222	
   223	__all__ = ["MigrationError", "add_parser", "cmd_migrate"]
"""The two-layer data model's migrations (ADR-0008).

`0001_schemas.sql`  — schemas, roles, grants, ownership, `"user".traders`,
                      the `cobalt.trader_id` GUC convention.
`0002_move_tables.sql` — every new-core table onto its side, plus
                      `user_id` on the user side.
`0002_move_tables.rollback.sql` — the reverse, catalog-only.
`0003_heartbeat_vault_outcome.sql` — durable heartbeat vault delivery.
`0003_heartbeat_vault_outcome.rollback.sql` — removes those two columns.

These are the DATABASE-WIDE migrations and they are the only ones that
live outside a feature module. A module's own DDL still lives in its own
`migrations/` directory and is still executed by its store's
`ensure_schema()`; those files create tables UNQUALIFIED and land them in
whichever schema the factory pinned on the connection.

Run them with `cobalt db migrate` (`--allow-prod` from ~/cobalt only,
`--rollback` to reverse 0003 then 0002). Nothing runs them implicitly: a store's
`ensure_schema()` asserts the schemas exist and tells you to run the CLI.
"""

from pathlib import Path

MIGRATIONS_DIR = Path(__file__).parent

#: Applied in this order, every time, both idempotent.
FORWARD = (
    MIGRATIONS_DIR / "0001_schemas.sql",
    MIGRATIONS_DIR / "0002_move_tables.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
)

#: `--rollback`, newest first. 0001 is deliberately NOT reversed.
REVERSE = (
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
)

__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
    70	    "drc_rows": Side.USER,
    71	    "prediction_records": Side.USER,
    72	    # S2-P1 — the radar. System: the pool and its membership history are
    73	    # engine artefacts any trader's strategies plug into.
    74	    "radar_pool": Side.SYSTEM,
    75	    "radar_membership": Side.SYSTEM,
    76	    # S2-P2 — taxonomy anatomy instances (regime, range, gap, extension,
    77	    # leg, session clock). The anatomy IS the system.
    78	    "anatomy_instances": Side.SYSTEM,
    79	}
    80	
    81	#: Every table this codebase has ruled on.
    82	PLACEMENT: dict[str, Side] = {
    83	    **MOVED_TABLES,
    84	    **SEEDED_TABLES,
    85	    **MODULE_TABLES,
    86	    **DECLARED_TABLES,
    87	}
    88	
    89	#: The old tree's tables, frozen in `public` and never touched
    90	#: (strangler rule). They exist in `cobalt_brain`; `cobalt_dev` has none
    91	#: of them, so the test asserts containment, not equality.
    92	OLD_TREE_PUBLIC_TABLES: frozenset[str] = frozenset({
    93	    "memory_logs",
    94	    "graph_nodes",
    95	    "graph_edges",
    96	    "hitl_proposals",
    97	    "browser_fast_path",
    98	    "instruments",
    99	    "market_snapshots",
   100	    "daily_in_play",
   101	    "key_levels",
   102	    "news_events",
   103	    "news_mentions",
   104	    "order_fills",
   105	    "strategy_signals",
   106	    "system_alerts",
   107	    "themes",
   108	    "trades",
   109	    "trading_accounts",
   110	})
   111	
   112	
   113	def side_of(table: str) -> Side:
   114	    """The ruled side of `table`, or a loud failure naming this file."""
   115	    try:
   116	        return PLACEMENT[table]
   117	    except KeyError:
   118	        raise KeyError(
   119	            f"table {table!r} has no ruled side. Every new table is declared on "
   120	            "exactly one side in cobalt/db_migrations/placement.py (ADR-0008 D2) "
   121	            "before it is created."
   122	        ) from None
   123	
   124	
   125	def tables_on(side: Side) -> frozenset[str]:
   126	    """Every ruled table on `side`, declared-but-unbuilt ones included."""
   127	    return frozenset(t for t, s in PLACEMENT.items() if s is side)
   128	
   129	
   130	__all__ = [
   131	    "DECLARED_TABLES",
   132	    "MODULE_TABLES",
   133	    "MOVED_TABLES",
   134	    "OLD_TREE_PUBLIC_TABLES",
   135	    "PLACEMENT",
   136	    "SEEDED_TABLES",
   137	    "side_of",
   138	    "tables_on",
   139	]

exec
/bin/zsh -lc "nl -ba src/cobalt/archiver/store.py | sed -n '45,155p'; nl -ba src/cobalt/settings/store.py | sed -n '35,100p'; rg -n 'attest|day_modes|INSERT INTO|def insert' src/cobalt/aset/store.py src/cobalt/aset/web.py src/cobalt/daymode/store.py; nl -ba src/cobalt/jobs/watchdog.py | sed -n '410,455p'; nl -ba src/cobalt/session/guard.py | sed -n '35,135p'; git status --short; rg -n 'i1|14 calendar|timestamp' 'docs/30 - Design/DATA-SOURCE-MEMO.md' | tail -15" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
    45	        with self._connect() as conn:
    46	            db.assert_schemas_exist(conn)
    47	            conn.execute(MIGRATION_SQL.read_text())
    48	
    49	    def upsert_bars(self, bars: list[Bar]) -> int:
    50	        """Insert or refresh `bars`. Returns the number of rows written.
    51	
    52	        ON CONFLICT DO UPDATE (not DO NOTHING): a re-run refreshes a bar
    53	        that Finviz may have finalized/revised since the last pull,
    54	        rather than freezing it at its first-seen (possibly provisional)
    55	        values. PK (ticker, interval, ts) makes this a true idempotent
    56	        upsert either way — no duplicates, ever.
    57	        """
    58	        if not bars:
    59	            return 0
    60	        rows = [
    61	            (
    62	                b.ticker,
    63	                b.interval.value,
    64	                b.ts,
    65	                b.open,
    66	                b.high,
    67	                b.low,
    68	                b.close,
    69	                b.volume,
    70	            )
    71	            for b in bars
    72	        ]
    73	        with self._connect() as conn:
    74	            with conn.cursor() as cur:
    75	                cur.executemany(
    76	                    """
    77	                    INSERT INTO bars (ticker, interval, ts, open, high, low, close, volume)
    78	                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    79	                    ON CONFLICT (ticker, interval, ts) DO UPDATE SET
    80	                        open = EXCLUDED.open,
    81	                        high = EXCLUDED.high,
    82	                        low = EXCLUDED.low,
    83	                        close = EXCLUDED.close,
    84	                        volume = EXCLUDED.volume
    85	                    """,
    86	                    rows,
    87	                )
    88	        return len(rows)
    89	
    90	    def count_rows(self) -> int:
    91	        with self._connect() as conn:
    92	            row = conn.execute("SELECT count(*) FROM bars").fetchone()
    93	        return int(row[0]) if row else 0
    35	        return db.connect(self.db_name, side=self.SIDE)
    36	
    37	    def ensure_schema(self) -> None:
    38	        with self._connect() as conn:
    39	            db.assert_schemas_exist(conn)
    40	            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
    41	                conn.execute(migration.read_text())
    42	
    43	    # -- reads --------------------------------------------------------
    44	
    45	    def rows(self) -> list[dict[str, Any]]:
    46	        with self._connect() as conn:
    47	            cur = conn.execute(
    48	                "SELECT key, value, source, updated_at FROM trader_settings "
    49	                "ORDER BY key"
    50	            )
    51	            columns = [d.name for d in cur.description]
    52	            return [dict(zip(columns, r)) for r in cur.fetchall()]
    53	
    54	    def values(self) -> dict[str, Any]:
    55	        """`{key: value}` — what `TraderSettings.from_db` builds from."""
    56	        return {row["key"]: row["value"] for row in self.rows()}
    57	
    58	    # -- the one write path -------------------------------------------
    59	
    60	    def put(self, rows: dict[str, Any], *, source: str) -> dict[str, str]:
    61	        """Upsert every setting in `rows`. Returns `{key: created|updated
    62	        |unchanged}` so the caller can report what actually moved.
    63	
    64	        One transaction: a half-applied settings load is a config that
    65	        validates nowhere, which is the failure the per-top-level-setting
    66	        row layout was chosen to avoid in the first place.
    67	        """
    68	        before = self.values()
    69	        outcome: dict[str, str] = {}
    70	        conn = self._connect()
    71	        conn.autocommit = False
    72	        try:
    73	            with conn.cursor() as cur:
    74	                for key, value in rows.items():
    75	                    if key in before and before[key] == value:
    76	                        outcome[key] = "unchanged"
    77	                        continue
    78	                    outcome[key] = "updated" if key in before else "created"
    79	                    cur.execute(
    80	                        """
    81	                        INSERT INTO trader_settings (key, value, source, updated_at)
    82	                        VALUES (%s, %s::jsonb, %s, now())
    83	                        ON CONFLICT (user_id, key) DO UPDATE SET
    84	                            value = EXCLUDED.value,
    85	                            source = EXCLUDED.source,
    86	                            updated_at = EXCLUDED.updated_at
    87	                        """,
    88	                        (key, json.dumps(value), source),
    89	                    )
    90	            conn.commit()
    91	        except BaseException:
    92	            conn.rollback()
    93	            raise
    94	        finally:
    95	            conn.close()
    96	        return outcome
    97	
    98	
    99	__all__ = ["MIGRATIONS_DIR", "TraderSettingsStore"]
src/cobalt/aset/web.py:122: .attest{display:flex;gap:8px;align-items:center;margin-top:8px}
src/cobalt/aset/web.py:123: .attest select{flex:1}
src/cobalt/aset/web.py:124: .attest button{margin-top:0;white-space:nowrap}
src/cobalt/aset/web.py:366:    # except the .htk"), and the .htk he attested has to agree with it.
src/cobalt/aset/web.py:430:# F6 day-mode banner + attestation, F7 card controls (S1-P2)
src/cobalt/aset/web.py:455:def _read_back_note_attestation(cfg, day, row: dict | None, store) -> dict | None:
src/cobalt/aset/web.py:458:    A box he ticked in today's daily note IS an attestation, read at
src/cobalt/aset/web.py:460:    the record (persisted through the same `attest_sheet` the selector
src/cobalt/aset/web.py:470:    note = daymode_note.read_attestation(path.read_text(encoding="utf-8"), cfg)
src/cobalt/aset/web.py:473:    settled = daymode_note.reconcile(note, (row or {}).get("attested_sheet"))
src/cobalt/aset/web.py:474:    if settled and settled != (row or {}).get("attested_sheet"):
src/cobalt/aset/web.py:475:        store.attest_sheet(day, filename=settled)
src/cobalt/aset/web.py:477:            "daymode: attestation {} read back from the daily note {}", settled, path
src/cobalt/aset/web.py:499:        row = _read_back_note_attestation(cfg, day, row, store)
src/cobalt/aset/web.py:506:        logger.error("daymode: note/selector attestation conflict: {}", e)
src/cobalt/aset/web.py:516:    status suffix for the banner; never raises — an attestation that
src/cobalt/aset/web.py:519:    reason to lose the attestation."""
src/cobalt/aset/web.py:527:            attested=(row or {}).get("attested_sheet"),
src/cobalt/aset/web.py:534:        logger.error("daymode note write FAILED (attestation stands): {}", e)
src/cobalt/aset/web.py:547:    attested = (row or {}).get("attested_sheet")
src/cobalt/aset/web.py:553:        match_html = f'<span style="color:#24d986">✓ {e(attested)} matches</span>'
src/cobalt/aset/web.py:566:        f'<span class="muted">(attested, not read — Cobalt never touches DAS)</span></div>',
src/cobalt/aset/web.py:581:        f'<option value="{e(f)}"{" selected" if f == attested else ""}>{e(f)}</option>'
src/cobalt/aset/web.py:585:        '<form class="attest" method="post" action="/attest">'
src/cobalt/aset/web.py:891:                attested=None, mode="(unresolved)",
src/cobalt/aset/web.py:906:        # Two separate refusals — the attested sheet must BE the mode in
src/cobalt/aset/web.py:1061:@app.post("/attest", response_class=HTMLResponse)
src/cobalt/aset/web.py:1062:async def attest(request: Request) -> str:
src/cobalt/aset/web.py:1078:                attested=None, mode="(none)",
src/cobalt/aset/web.py:1084:        store.attest_sheet(day, filename=filename)
src/cobalt/daymode/store.py:1:"""F6 persistence: one `day_modes` row per trading day.
src/cobalt/daymode/store.py:57:            cur = conn.execute("SELECT * FROM day_modes WHERE trade_date = %s", (day,))
src/cobalt/daymode/store.py:81:                "INSERT INTO day_modes (trade_date, stage, proposed, reason, session, created_at) "
src/cobalt/daymode/store.py:108:                f"no day_modes row for {day} — there is nothing to decide yet. "
src/cobalt/daymode/store.py:114:                "early `.htk` attestation, while stage 1 was still in force. There is "
src/cobalt/daymode/store.py:126:                "UPDATE day_modes SET decided = %s, decided_by = %s, decided_at = %s, "
src/cobalt/daymode/store.py:132:    def attest_sheet(
src/cobalt/daymode/store.py:138:        exists so he can attest before 09:00, while stage 1 is still in
src/cobalt/daymode/store.py:142:        session = assert_writable("daymode.attest", target=day.isoformat(), now=ts)
src/cobalt/daymode/store.py:145:                "INSERT INTO day_modes (trade_date, stage, proposed, reason, session, "
src/cobalt/daymode/store.py:146:                "attested_sheet, attested_at) "
src/cobalt/daymode/store.py:149:                "attested_sheet = EXCLUDED.attested_sheet, attested_at = EXCLUDED.attested_at",
src/cobalt/daymode/store.py:153:                    "attested before any proposal — stage 1 in force",
src/cobalt/daymode/store.py:164:                "attested_sheet, reason FROM day_modes ORDER BY trade_date DESC LIMIT %s",
src/cobalt/aset/store.py:109:                    INSERT INTO aset_sizings (
   410	        # -- jobs the wrapper reports on -------------------------------
   411	        state = row["state"]
   412	
   413	        if state == JobState.RUNNING.value:
   414	            started, beat = row["started_at"], row["heartbeat_at"]
   415	            ran_for = (ts - started).total_seconds() if started else 0
   416	            stale_for = (ts - beat).total_seconds() if beat else None
   417	            stale_limit = spec.timeout_s / fraction
   418	            if ran_for > spec.timeout_s and (stale_for is None or stale_for > stale_limit):
   419	                reason = (
   420	                    f"ZOMBIE: running {ran_for / 60:.0f} min (timeout "
   421	                    f"{spec.timeout_s / 60:.0f} min) and the heartbeat is "
   422	                    + (f"{stale_for / 60:.0f} min stale" if stale_for else "missing")
   423	                    + f" (limit {stale_limit / 60:.0f} min). The beater thread dies "
   424	                    "with its process, so a stale stamp means the process is gone."
   425	                )
   426	                store.mark_zombie(spec.label, reason=reason)
   427	                findings.append(Finding(spec.label, False, JobState.ZOMBIE.value, reason))
   428	            else:
   429	                findings.append(
   430	                    Finding(spec.label, True, state,
   431	                            f"running {ran_for / 60:.0f} min, heartbeat fresh")
   432	                )
   433	            continue
   434	
   435	        if state in {s.value for s in RED_STATES}:
   436	            findings.append(
   437	                Finding(spec.label, False, state,
   438	                        (row["last_error"] or "no error text recorded")[:300])
   439	            )
   440	            continue
   441	
   442	        # -- MISSED: a fact about an absent run, not a state -----------
   443	        if spec.kind is JobKind.ONE_SHOT:
   444	            missed, detail = is_missed(spec, row, now_et=now_et, grace=grace)
   445	            if missed:
   446	                findings.append(Finding(spec.label, False, f"{state} (MISSED)", detail))
   447	                continue
   448	
   449	        launchd_note = (
   450	            f" · launchd: loaded, last exit {status.last_exit}"
   451	            if probe and status.last_exit is not None else " · launchd: loaded"
   452	        ) if probe else ""
   453	        findings.append(
   454	            Finding(
   455	                spec.label, True, state,
    35	from . import clock as clock_mod
    36	from .clock import ET, SessionClock, session_clock
    37	from .models import BLOCKED_SESSION, Session
    38	from .store import SessionBlockStore
    39	
    40	
    41	class SessionBlocked(RuntimeError):
    42	    """A write was refused because of the session it was attempted in."""
    43	
    44	    def __init__(self, message: str, *, session: Session, actor: str):
    45	        super().__init__(message)
    46	        self.session = session
    47	        self.actor = actor
    48	
    49	
    50	def block_message(clock: SessionClock, ts: datetime, actor: str) -> str:
    51	    """The one loud line. Names the window, the clock, and the lift."""
    52	    et = clock.to_et(ts)
    53	    lifts_at, next_session = clock.next_boundary(ts)
    54	    return (
    55	        f"REFUSED ({actor}): it is {et:%H:%M:%S} ET on {et:%Y-%m-%d} — inside "
    56	        f"MARKET RESET, the {_window_text(clock)} ET hard block. Cobalt writes "
    57	        f"nothing in this window: the day's record is closing and the bar "
    58	        f"archiver runs inside it. The block lifts at "
    59	        f"{lifts_at.astimezone(ET):%H:%M} ET ({next_session})."
    60	    )
    61	
    62	
    63	def _window_text(clock: SessionClock) -> str:
    64	    windows = {w.session: w for w in clock.windows_for(clock_mod.now_utc().astimezone(ET).date())}
    65	    window = windows.get(BLOCKED_SESSION)
    66	    if window is None:  # today is closed; read the boundaries directly
    67	        return "20:00-21:00"
    68	    return f"{window.start:%H:%M}-{window.end:%H:%M}"
    69	
    70	
    71	def note_ungated(
    72	    actor: str,
    73	    *,
    74	    target: Optional[str] = None,
    75	    why: str,
    76	    now: Optional[datetime] = None,
    77	    clock: Optional[SessionClock] = None,
    78	    store: Optional[SessionBlockStore] = None,
    79	) -> Session:
    80	    """Migration/repair tooling ran inside the block. Say so, loudly.
    81	
    82	    RULED 2026-09-04 (S1-P3, decided-with-veto): migration and repair
    83	    tooling stays UNGATED in `market_reset`. `VaultWriter.restore` and
    84	    `CardStore.backfill` already carried that carve-out in comments; the
    85	    reasoning is the same in both — locking recovery out for the
    86	    20:00-21:00 window would mean the one hour you most need to repair
    87	    state is the hour you cannot. Card CREATION stays refused: that is
    88	    trading record, and the block exists for it.
    89	
    90	    The price of the carve-out is that it may never happen QUIETLY. Every
    91	    such run inside the window logs ONE LOUD LINE and increments the same
    92	    counter F18 displays, tagged `ungated_run` so a repair is never read
    93	    as a refusal.
    94	
    95	    OUTSIDE the window this does nothing at all — no log line, no row. A
    96	    backfill at two in the afternoon is not an event.
    97	    """
    98	    clock = clock or session_clock()
    99	    ts = now or clock_mod.now_utc()
   100	    session = clock.session(ts)
   101	    if session is not BLOCKED_SESSION:
   102	        return session
   103	
   104	    et = clock.to_et(ts)
   105	    message = (
   106	        f"UNGATED ({actor}): it is {et:%H:%M:%S} ET on {et:%Y-%m-%d} — inside "
   107	        f"MARKET RESET, where every ordinary write is refused. This ran anyway "
   108	        f"under the migration/repair carve-out (ruled 2026-09-04): {why}. It is "
   109	        "counted on the heartbeat so that a repair inside the block can never be "
   110	        "a quiet one."
   111	    )
   112	    logger.error(message)
   113	    (store or SessionBlockStore()).record(
   114	        session=session.value,
   115	        actor=actor,
   116	        target=target,
   117	        reason=message,
   118	        kind=SessionBlockStore.UNGATED_RUN,
   119	    )
   120	    return session
   121	
   122	
   123	def assert_writable(
   124	    actor: str,
   125	    *,
   126	    target: Optional[str] = None,
   127	    now: Optional[datetime] = None,
   128	    clock: Optional[SessionClock] = None,
   129	    store: Optional[SessionBlockStore] = None,
   130	) -> Session:
   131	    """Refuse the caller if the session forbids writing; else return it.
   132	
   133	    `actor` names the write site ("vaultwrite", "aset.card", ...) and is
   134	    what the refusal message, the log line and the counter row all carry.
   135	    `now` is the seam the F1 tests freeze — production passes nothing and
 M "docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md"
 M "docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md"
?? "docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r1.md"
?? "docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md"
244:  timestamps carry HH:MM, granularity between consecutive rows matches
247:  size monotonically: `{i1, i5}` ≈ 2–3 weeks (with premarket/after-hours
248:  included), `{i15}` ≈ 3 weeks (regular hours only — the extended-hours
249:  cutoff happens between `i5` and `i15`), `{i30, h}` ≈ **9.6 months**
253:  daily — they are not shorthand for `i5`/`i15`/etc. Anyone guessing
268:(2522-row baseline) or `p=i1` (9451-row baseline), returned **exactly
273:on `p=i1` specifically (in case date-range only applies to intraday,
336:| **Stock** | 6-col OHLCV at 8 real granularities (d/w/m/i1/i5/i15/i30/h); volume present everywhere; depth tiers empirically mapped | **History-depth param name unconfirmed** (highest-priority Phase B item) | **Critical** — setups engine + backtesting both depend on this |
412:Slots into the same depth tier as `i1`/`i5` (~2 weeks, premarket
416:same ~2-week live-detection window as `i1`/`i5`, no depth penalty for
417:using `i2` over `i1`.
419:**Fresh `i1`/`i5` re-pull** (same day, ~50 minutes after the original
425:| `i1` | 9451 rows, starts 04:00 AM | 9499 rows, starts 04:00 AM | ✅ start time unchanged; row count grew by 48 — matches ~48 new 1-min bars accumulating in the ~48-minute gap between probes (a good internal consistency check that this is a live, continuously-updating feed, not a cached/stale snapshot) |
546:| **Stock**          | 6-col OHLCV at **9** real granularities (i1/i2/i5/i15/i30/h/d/w/m); volume present everywhere; depth tiers empirically mapped and re-verified stable across a fresh pull                          | History-depth param name still unconfirmed (Phase B's top item, unchanged)                               | **Critical** — `i2` is Dejan's actual trading timeframe and is now confirmed in the same ~2-week live-detection tier as `i1`/`i5` |
604:identically on `i1`/`i5`/`i15` (only `i2` and `i30` were probed); the

codex
**BLOCKERS (file:line)**

Paths below are under `docs/40 - DevDocs/reports/_inflight/`; `plan` = `plan-s2-p1-2026-09-10.md`, `brief` = `s2-p1-brief.md`.

1. **Account-mode implementation contradicts E1.** `plan:137`, `plan:185`, `brief:272` explicitly permit UNSET cards. E1 (`plan:287`, `brief:344`) requires refusal, standing-setting fallback, and a per-day SIM control on sheet attestation. Rewrite implementation, acceptance tests, and LIVE initialization together; otherwise the build implements the opposite behavior.

2. **E2/E8’s pool block cannot pass the specified parser.** `plan:53`, `plan:56`, `brief:177` accept only screen blocks in the Screens note, with extra fields forbidden. E2/E8 require a pool block there. Meanwhile `plan:124`, `plan:157`, `plan:158`, and `brief:167` retain competing rank/cap definitions in committed configuration. Add a validated pool contract, user-side mirror, synthetic fixture, and proposal/writer integration; remove competing trader-specific defaults. This follows ADR-0008’s distinction between engine configuration and trader settings.

3. **The ruled ranking algorithm remains incomplete.** `plan:293` specifies premarket/RTH metrics but enables aftermarket at `plan:122`; mixed volume/RVOL screen results have no defined comparison. `plan:299` requires three-scan stickiness while `plan:218` excludes hysteresis. Define ordering, streak reset/persistence, and precedence among stickiness, degraded holds, manual exclusion, and cap reductions. Lowering the vault cap below held membership also defeats `plan:124`’s claimed cap invariant.

4. **Credential instructions directly violate E7.** `brief:17`, `brief:84`, and `plan:254` instruct the hub to export DB credentials into Sol’s environment. `plan:189` and `brief:292` assign DB smoke to Sol. E7 forbids both. Remove those instructions and explicitly split offline checks from hub-owned DB acceptance gates.

5. **Restart instructions still contradict E6.** `plan:204` and `brief:79` say code changes require no restart; `plan:231` hard-codes only ASET. E6 requires import-based resident analysis with all residents as the fallback. Update the deployment and rollback commands from that analysis, not just the report checklist.

6. **The market-reset “single commit” guarantee is incompatible with the write sequence.** `plan:122`, `brief:246` promise whole-cycle discard but perform pool/membership, bars, and mirror writes separately. `BarStore.upsert_bars` opens its own transaction (`src/cobalt/archiver/store.py:73`); `TraderSettingsStore.put` commits independently (`src/cobalt/settings/store.py:90`). ADR-0008 requires separate side connections. A check before the first commit cannot prevent subsequent writes crossing 20:00 or undo earlier commits. Specify achievable transaction boundaries and test crossing the boundary between store writes.

7. **E4 can require a schema change after stage-1 deployment.** `plan:303`, `plan:307` defer the comparison to LIVE, but `plan:53` forbids `ft`, and `plan:123` omits it from requests. If ticker sets differ, the approved proposal cannot run through the deployed contract. Ship optional validated `ft` support beforehand, or explicitly stop rollout for a code revision and review.

8. **The throttle probe cannot observe its required stop conditions through the mandated API.** `brief:114` requires `fetch_bars`; `brief:115` requires stopping on redirects and recording response metrics. The collector follows redirects (`src/cobalt/archiver/collector.py:166`) and returns only parsed bars (`:174`), hiding redirect history, status, and response bytes. Define a shared observable transport interface and test redirect refusal there.

**RISKS**

- `plan:130`: seed the watermark by **ticker and `interval='i1'`**, not ticker alone. Strict watermarks also defer corrections and missing older bars until archiving; the existing store explicitly supports revised bars.
- `brief:135`: adding created tables to migration proof also needs direction-aware handling of intentional drops. The current proof reports removal as `CHANGED` and raises **after commit** (`src/cobalt/db_migrations/cli.py:142`, `:193`).
- `plan:132`: a 60-second setting does not prove two polls per two-minute bar. Sequential network latency, full-export parsing, and token-bucket waits need an achieved-cadence acceptance threshold.
- `plan:153`: scan freshness does not establish bar freshness. Define how individual poll failures reach F18 while scans and the wrapper’s independent heartbeat remain healthy.
- `plan:304`: E5’s repo-wide exact-string check is broader than the tracked-directory grammar test at `plan:60`; both checks need explicit ownership before commits.

**VERDICT: BLOCKED — revise before build.**

The proposed table placement and J1 grants agree with ADR-0008. The disabled-job startup sequence also holds: `job_run` does not gate on `enabled`. The addendum, however, has not been integrated into executable instructions and acceptance criteria. This was a read-only review; no DB or live-network validation was run.
tokens used
59,721
**BLOCKERS (file:line)**

Paths below are under `docs/40 - DevDocs/reports/_inflight/`; `plan` = `plan-s2-p1-2026-09-10.md`, `brief` = `s2-p1-brief.md`.

1. **Account-mode implementation contradicts E1.** `plan:137`, `plan:185`, `brief:272` explicitly permit UNSET cards. E1 (`plan:287`, `brief:344`) requires refusal, standing-setting fallback, and a per-day SIM control on sheet attestation. Rewrite implementation, acceptance tests, and LIVE initialization together; otherwise the build implements the opposite behavior.

2. **E2/E8’s pool block cannot pass the specified parser.** `plan:53`, `plan:56`, `brief:177` accept only screen blocks in the Screens note, with extra fields forbidden. E2/E8 require a pool block there. Meanwhile `plan:124`, `plan:157`, `plan:158`, and `brief:167` retain competing rank/cap definitions in committed configuration. Add a validated pool contract, user-side mirror, synthetic fixture, and proposal/writer integration; remove competing trader-specific defaults. This follows ADR-0008’s distinction between engine configuration and trader settings.

3. **The ruled ranking algorithm remains incomplete.** `plan:293` specifies premarket/RTH metrics but enables aftermarket at `plan:122`; mixed volume/RVOL screen results have no defined comparison. `plan:299` requires three-scan stickiness while `plan:218` excludes hysteresis. Define ordering, streak reset/persistence, and precedence among stickiness, degraded holds, manual exclusion, and cap reductions. Lowering the vault cap below held membership also defeats `plan:124`’s claimed cap invariant.

4. **Credential instructions directly violate E7.** `brief:17`, `brief:84`, and `plan:254` instruct the hub to export DB credentials into Sol’s environment. `plan:189` and `brief:292` assign DB smoke to Sol. E7 forbids both. Remove those instructions and explicitly split offline checks from hub-owned DB acceptance gates.

5. **Restart instructions still contradict E6.** `plan:204` and `brief:79` say code changes require no restart; `plan:231` hard-codes only ASET. E6 requires import-based resident analysis with all residents as the fallback. Update the deployment and rollback commands from that analysis, not just the report checklist.

6. **The market-reset “single commit” guarantee is incompatible with the write sequence.** `plan:122`, `brief:246` promise whole-cycle discard but perform pool/membership, bars, and mirror writes separately. `BarStore.upsert_bars` opens its own transaction (`src/cobalt/archiver/store.py:73`); `TraderSettingsStore.put` commits independently (`src/cobalt/settings/store.py:90`). ADR-0008 requires separate side connections. A check before the first commit cannot prevent subsequent writes crossing 20:00 or undo earlier commits. Specify achievable transaction boundaries and test crossing the boundary between store writes.

7. **E4 can require a schema change after stage-1 deployment.** `plan:303`, `plan:307` defer the comparison to LIVE, but `plan:53` forbids `ft`, and `plan:123` omits it from requests. If ticker sets differ, the approved proposal cannot run through the deployed contract. Ship optional validated `ft` support beforehand, or explicitly stop rollout for a code revision and review.

8. **The throttle probe cannot observe its required stop conditions through the mandated API.** `brief:114` requires `fetch_bars`; `brief:115` requires stopping on redirects and recording response metrics. The collector follows redirects (`src/cobalt/archiver/collector.py:166`) and returns only parsed bars (`:174`), hiding redirect history, status, and response bytes. Define a shared observable transport interface and test redirect refusal there.

**RISKS**

- `plan:130`: seed the watermark by **ticker and `interval='i1'`**, not ticker alone. Strict watermarks also defer corrections and missing older bars until archiving; the existing store explicitly supports revised bars.
- `brief:135`: adding created tables to migration proof also needs direction-aware handling of intentional drops. The current proof reports removal as `CHANGED` and raises **after commit** (`src/cobalt/db_migrations/cli.py:142`, `:193`).
- `plan:132`: a 60-second setting does not prove two polls per two-minute bar. Sequential network latency, full-export parsing, and token-bucket waits need an achieved-cadence acceptance threshold.
- `plan:153`: scan freshness does not establish bar freshness. Define how individual poll failures reach F18 while scans and the wrapper’s independent heartbeat remain healthy.
- `plan:304`: E5’s repo-wide exact-string check is broader than the tracked-directory grammar test at `plan:60`; both checks need explicit ownership before commits.

**VERDICT: BLOCKED — revise before build.**

The proposed table placement and J1 grants agree with ADR-0008. The disabled-job startup sequence also holds: `job_run` does not gate on `enabled`. The addendum, however, has not been integrated into executable instructions and acceptance criteria. This was a read-only review; no DB or live-network validation was run.
