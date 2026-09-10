Reading additional input from stdin...
OpenAI Codex v0.153.4
--------
workdir: /Users/cobalt/cobalt-wt/s2-p1-radar-pool
model: gpt-6-astra
provider: openai
approval: never
sandbox: read-only
reasoning effort: high
reasoning summaries: none
session id: 01a08c11-36e0-7cc0-b4ae-82c2cd864d3a
--------
user
Round 3, final. For each round-2 blocker 1–8 and risk: RESOLVED or OPEN with file:line in the rewritten plan-s2-p1-2026-09-10.md and s2-p1-brief.md; then BLOCKERS / RISKS / VERDICT.
hook: SessionStart
hook: SessionStart Completed
codex
I’ll locate the round-2 findings and check each one against the rewritten plan and brief, with line references for the final verdict.
exec
/bin/zsh -lc "pwd; rg --files -g 'AGENTS.md' -g '*s2*p1*' -g '*round*' -g '*review*'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
/Users/cobalt/cobalt-wt/s2-p1-radar-pool
docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r1.md
docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md
docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r3.md
docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md
docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md

exec
/bin/zsh -lc 'for p in /AGENTS.md /Users/AGENTS.md /Users/cobalt/AGENTS.md /Users/cobalt/cobalt-wt/AGENTS.md /Users/cobalt/cobalt-wt/s2-p1-radar-pool/AGENTS.md; do if [ -f "$p" ]; then cat "$p"; fi; done
rg --files --hidden -g AGENTS.md -g '"'"'!node_modules'"' -g '"'!.git'"' docs
nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md'
nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md'
nl -ba 'docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md'
nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r3.md'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
     1	Reading additional input from stdin...
     2	OpenAI Codex v0.153.4
     3	--------
     4	workdir: /Users/cobalt/cobalt-wt/s2-p1-radar-pool
     5	model: gpt-6-astra
     6	provider: openai
     7	approval: never
     8	sandbox: read-only
     9	reasoning effort: medium
    10	reasoning summaries: none
    11	session id: 01a08bf5-d7ab-7e63-9eac-323c4cd11be9
    12	--------
    13	user
    14	Round 2. Round 1 ended on a usage limit without a verdict. Review docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md and s2-p1-brief.md, focusing on the RULINGS ADDENDUM section and its consistency with the rest, against ADR-0008, DATA-SOURCE-MEMO, the archiver collector, db_migrations/ and src/cobalt/jobs/. Output BLOCKERS (file:line) / RISKS / VERDICT.
    15	hook: SessionStart
    16	hook: SessionStart Completed
    17	codex
    18	I’ll read the plan and brief, then check the RULINGS ADDENDUM against the architecture decisions, source memo, collector, migrations, and job code.
    19	exec
    20	/bin/zsh -lc "pwd; rg --files -g 'AGENTS.md' -g '*s2-p1*' -g '*ADR-0008*' -g '*DATA-SOURCE-MEMO*' -g '*archiver*' -g '*collector*' -g '*migration*'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
    21	 succeeded in 0ms:
    22	/Users/cobalt/cobalt-wt/s2-p1-radar-pool
    23	src/cobalt/taxonomy/note_migration.py
    24	src/cobalt/taxonomy/trade_note_migration.py
    25	src/cobalt/archiver/collector.py
    26	tests/taxonomy/test_note_migration.py
    27	tests/taxonomy/test_trade_note_migration.py
    28	ops/com.cobalt.archiver.plist
    29	tests/cobalt/test_archiver_report.py
    30	tests/cobalt/test_archiver_collector.py
    31	tests/cobalt/test_archiver_store.py
    32	tests/cobalt/test_archiver_config.py
    33	docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r1.md
    34	docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md
    35	docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md
    36	docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md
    37	docs/30 - Design/DATA-SOURCE-MEMO.md
    38	docs/30 - Design/archiver-runs.md
    39	docs/40 - DevDocs/cobalt/archiver/collector.md
    40	docs/40 - DevDocs/cobalt/taxonomy/note_migration.md
    41	docs/40 - DevDocs/cobalt/taxonomy/trade_note_migration.md
    42	docs/10 - Decisions/ADR-0008-two-layer-data-model.md
    43	docs/40 - DevDocs/tests/cobalt/test_archiver_store.md
    44	docs/40 - DevDocs/tests/cobalt/test_archiver_collector.md
    45	docs/40 - DevDocs/tests/cobalt/test_archiver_config.md
    46	docs/40 - DevDocs/tests/cobalt/test_archiver_report.md
    47	
    48	exec
    49	/bin/zsh -lc "rg --files -g 'AGENTS.md' -g '*' db_migrations src/cobalt/jobs; nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md'; nl -ba 'docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
    50	 succeeded in 0ms:
    51	rg: db_migrations: No such file or directory (os error 2)
    52	src/cobalt/jobs/cli.py
    53	src/cobalt/jobs/entrypoint.py
    54	src/cobalt/jobs/__init__.py
    55	src/cobalt/jobs/watchdog.py
    56	src/cobalt/jobs/models.py
    57	src/cobalt/jobs/config.py
    58	src/cobalt/jobs/wrapper.py
    59	src/cobalt/jobs/migrations/0001_cobalt_jobs.sql
    60	src/cobalt/jobs/store.py
    61	src/cobalt/jobs/killswitch.py
    62	     1	# S2-P1 PLAN — Radar pool + Finviz bar poller (2026-09-10)
    63	     2	
    64	     3	Architect: Opus 5 (plan + brief, no build) · Reviewer: Codex `gpt-6-astra`, read-only, ≤3 rounds ·
    65	     4	Branch `sprint-2/radar-pool` off `main` `f646640` · Worktree `~/cobalt-wt/s2-p1-radar-pool` ·
    66	     5	Build: Codex `gpt-5.6-sol` · Hub: Sonnet · Sprint S2 = 09-10 → 09-23.
    67	     6	
    68	     7	## §0 Headline
    69	     8	
    70	     9	- P1 ships the F2 resident `com.cobalt.radar` (4 screens + static lists → ≤ `radar.pool_cap` names, membership history), a Finviz i1 poller into `system.bars`, the account-mode tag, J1, `cobalt db query`, and an F18 `radar` probe.
    71	    10	- User data moves user-side through vault notes only: screens (R1, existing note) and lists (R4, new note). One HITL card, one hub-run write, last, after Dejan approves.
    72	    11	- Two merge stages: stage 1 = everything but the archiver's source switch; stage 2 = archiver reads the Lists note and `watchlists.yaml` is deleted, only after an equality proof on prod.
    73	    12	- Precondition: `ops/heartbeat-market-reset` (uncommitted today, carries `db_migrations/0003`) merges first; this branch is rebased before build.
    74	    13	- ESCALATE: 6 (§8). Review: 0 of 3 Astra rounds completed (Codex usage limit hit in round 1) — plan UNREVIEWED, see §9.
    75	    14	
    76	    15	## Line 0 — ADR-0008 in force
    77	    16	
    78	    17	| Law | How P1 honours it | Evidence |
    79	    18	|---|---|---|
    80	    19	| Two schemas, side per store | `RadarStore.SIDE = Side.SYSTEM`; mirror via existing `TraderSettingsStore` (`Side.USER`); `BarStore`, `JobStore` system | ADR-0008 D1; `db.py:115-133` |
    81	    20	| Every new table in the placement map or the suite fails | `radar_pool`, `radar_membership` move from `DECLARED_TABLES` to a new `CREATED_TABLES` dict (created by a db_migration directly on its side), iterated by the proof table | `placement.py:65-79`; `test_tenancy.py:102-171` |
    82	    21	| Already declared system-side | yes — `radar_pool`, `radar_membership` | `placement.py:72-75` |
    83	    22	| Account-mode tag | `"user".aset_sizings.account_mode ∈ {live, sim}`, stamped from `"user".day_modes.account_mode` (new column, see E1); shown on every card | ADR-0008 D2 row 1 |
    84	    23	| Migration in the fixed list, rollback SQL, digests unchanged | `src/cobalt/db_migrations/0004_radar_pool.sql` + `0004_radar_pool.rollback.sql`, appended to `FORWARD` / prepended to `REVERSE` after heartbeat's 0003; `DIGEST_EXCLUDED_COLUMNS` gains `account_mode`, `pool_member_id` | `db_migrations/__init__.py:25-31`; heartbeat worktree diff (0003 pattern) |
    85	    24	| Cross-side refs schema-qualified | `system.radar_membership(id)` in SQL; lint `TestStoresNameOnlyTheirOwnSide` covers new stores | `test_tenancy.py:385-431` |
    86	    25	| `"user"` always quoted | `psycopg.sql.Identifier`; reserved-word lint | `test_tenancy.py:348-383` |
    87	    26	
    88	    27	## §1 Facts the plan rests on (verified read-only 09-10)
    89	    28	
    90	    29	| # | Fact | Evidence |
    91	    30	|---|---|---|
    92	    31	| F1 | `cobalt db migrate --rollback` executes the WHOLE `REVERSE` tuple. With 0003 and 0004 registered, rolling back 0004 would also reverse 0003 and 0002 (every table back to `public`). | `db_migrations/cli.py:170`; heartbeat diff `REVERSE = (0003, 0002)` |
    93	    32	| F2 | `cobalt_user` has SELECT on `system`, not REFERENCES — the J1 FK needs an explicit grant. | `0001_schemas.sql` §4–§5 |
    94	    33	| F3 | No live/sim value exists anywhere: not in `day_modes`, `trader_settings`, or configs. | `daymode/migrations/0001_day_modes.sql`; `grep account_mode` → one SQL comment |
    95	    34	| F4 | `TraderSettings._build` fails on MISSING keys only; extra `radar.*` rows cannot break the sheet. | `settings/models.py` `_build`; consumers `aset/config.py:267`, `daymode/config.py:311` |
    96	    35	| F5 | `watchlists.yaml` holds three DERIVED tiers (`tier_a/b/c`), not the four TradingView lists. Its only reader is `archiver/config.py:19`. | file header lines 8–24; grep (other hits are comments) |
    97	    36	| F6 | `fetch_bars` returns the whole i1 export: ~14 calendar days, ~9.4k rows/ticker. | `archiver/collector.py:159-174`; DATA-SOURCE-MEMO §2a |
    98	    37	| F7 | Screener export `v=152&c=0..150` returns 151 named columns; `t=` multi-ticker works. | DATA-SOURCE-MEMO §1, §0 |
    99	    38	| F8 | `ft=` is unverified; three of the four pasted screen URLs carry `ft=4`; R1's key list has no `ft`. | DATA-SOURCE-MEMO §0; vault note (read-only) |
   100	    39	| F9 | Charter §9 names no request rate (Finviz Elite owned, $0 new spend). Measured points only: 5 names @10 s clean (LIVE-FEED-SPIKE §A); nightly archiver ~1,055 req / 23 min at 1.2 s sleep. | `MVP-CHARTER-v0_2.md:323-334`; `archiver/runner.py:27` |
   101	    40	| F10 | market_reset 20:00–21:00 ET: gated writes raise `SessionBlocked`; the heartbeat died there 8 times because it caught the refusal instead of asking the clock first. | `heartbeat-blackout-2026-09-10.md`; `session/guard.py` |
   102	    41	| F11 | `tunables.yaml` is re-read by `com.cobalt.aset`; a new `TunableUnit`/`Status`/`Source` value is the 09-09 sheet-outage class. | `jobs.yaml:67-69` (`taxonomy/loader.py:79`); `jobs/config.py:256-273` |
   103	    42	| F12 | Resident + `supervisor: self` is a new shape; `should_keep_running` exists for "the S2 radar poller"; watchdog skips PID probes for `self`. | `wrapper.py:165-180`; `watchdog.py:369-383` |
   104	    43	| F13 | Radar Screens note: four `##` sections of prose bullets, no fenced blocks; the Day Scan gate is prose. | vault note (read-only); day-open §4 C.4 |
   105	    44	| F14 | `cobalt_dev` holds **0** bars; the replay session must be created in dev. | `select count(*) from system.bars` on cobalt_dev = 0 |
   106	    45	| F15 | Sol: writes outside the worktree denied, commit denied, network on; no `psql`; psycopg→localhost UNVERIFIED; the worktree has no `.env`. | day-open §1.3; `ls .env` |
   107	    46	| F16 | `data/` and `logs/` are gitignored. | `.gitignore:2,6`; `git check-ignore data/radar-cache/x.csv` |
   108	    47	| F17 | `VaultWriter.upsert_unit` creates a missing section at a `Placement`; `create_if_absent` never rewrites an existing file; both refuse in market_reset. | `vaultwrite/writer.py:559-678` |
   109	    48	
   110	    49	## §2 Decisions
   111	    50	
   112	    51	### D1 — Sources: two vault notes, one parser (R1, R4)
   113	    52	
   114	    53	- **Screens** — `1 - Trading/Radar Screens.md` (exists). `ScreenBlock` (extra=forbid): `screen` (display name → key = snake slug, unique), `f` (grammar `^[a-z0-9_.]+(,[a-z0-9_.]+)*$`; `%`, `&`, `=`, `auth` refused), `sort` (`^-?[a-z0-9_]+$`), `columns` (list[int] 0–150, display only), `active_from` / `active_to` (`"HH:MM"` ET, from < to), `enabled` (bool).
   115	    54	- **Lists (R4 choice)** — NEW note `1 - Trading/Radar Lists.md`. `ListBlock` (extra=forbid): `list` (key), `description`, `tickers` (uppercase, unique), `radar` (bool: pool source), `archive` (list[`Interval`], may be empty), `backfill_default` (exactly one true across blocks), `enabled`. One optional `ExcludeBlock` `{exclude: [tickers]}` → `excluded_by = manual`.
   116	    55	- **Why a vault note, one path:** R1 already makes a note the truth for half the radar's inputs; the same parser, hashing, mirror and degradation code serve the other half with no new machinery. A `trader_settings`-only path would need a second editing surface (seed YAML + CLI) and split radar inputs across two homes. **Why a separate note:** ~260 tickers would bury his screen prose, and `create_if_absent` gives the lists write its own write_id without touching `Radar Screens.md`.
   117	    56	- **Parser** (`cobalt.radar.notes`): reads the file bytes ONCE per check and hashes those bytes (no torn reads under Obsidian Sync). Only fenced ```` ```yaml ```` blocks are read; every yaml fence in a note must validate as that note's block type (a non-validating fence = a named parse failure, never skipped). Prose and `cobalt:` markers are ignored. Hashes: sha256 per block (fence body) + sha256 per note.
   118	    57	- **Reload:** note sha256 compared each cycle; on change → re-parse → mirror.
   119	    58	- **Mirror:** `"user".trader_settings` through the existing `TraderSettingsStore.put` (the one write path, `settings/store.py:60`). Keys `radar.note.screens`, `radar.note.lists`, `radar.screen.<key>`, `radar.list.<key>`, `radar.exclude`; value `{block, block_sha256, note_sha256, status: ok|parse_failed|removed, error}`; `source = vault:<note path>@<sha12>`. No new user-side table.
   120	    59	- **Parse failure (R1):** the failed block contributes nothing; its mirror row → `parse_failed` (the DB never presents the previous version as current); pool row `degraded = true` naming the source; members whose every source is degraded are HELD; F18 `radar` RED naming the screen/list. Never an empty pool from a failure.
   121	    60	- **R2 fixtures:** `tests/fixtures/radar/radar-screens.example.md` — exactly ONE synthetic screen, fenced format, `active_from: "10:00"` (exercises the gate); `tests/fixtures/radar/radar-lists.example.md` — synthetic lists (≥60 liquid large caps by rule, one ETF for `not_equity`, one `exclude`). The seed-parser test renders its prose input FROM the screen fixture, so no second screen definition exists. Suite test (content, not filenames): no tracked file under `src/cobalt/`, `configs/cobalt/`, `tests/cobalt/`, `ops/` or `docs/40 - DevDocs/` contains Finviz filter grammar (`f=` followed by `sh_|ta_|fa_|an_|cap_|exch_|geo_|idx_|ind_|sec_|news_|earningsdate_|ipodate_|targetprice_`) outside `tests/fixtures/radar/`. It also catches E5 if that report is committed unredacted.
   122	    61	
   123	    62	### D2 — The one-time seed write (R1 + R4): hub only, HITL-gated, last
   124	    63	
   125	    64	- `cobalt radar seed --dry-run` derives the four screen blocks deterministically from the note's prose: `f` from the "Export call (derived)" line's `f=` value, cross-checked equal to the backticked codes on the "Filters" line (mismatch → refuse); `sort` from the "Sort" bullet; `columns` from the columns bullet; `screen` from the heading after "—". `active_from: "10:00"` for Day Scan quotes its prose verbatim; any window the prose does not state is emitted as the radar's full active span from the session tunables and marked `# PROPOSED — no window stated in prose`. Every derived field carries a `# from: "<verbatim source line>"` comment. `enabled: true`.
   126	    65	- Placement: each block goes after the last non-blank line of its own `##` section via `upsert_unit(section="radar-screen-<n>", unit_id="radar-screen:<key>", placement=…)`: 4 write_ids. Test: every pre-existing line byte-identical; the diff is insertions only.
   127	    66	- Lists note: `create_if_absent` from a template rendered from `watchlists.yaml` — three blocks `tier_a / tier_b / tier_c` verbatim (description, tickers, intervals → `archive`, `radar: true`, `backfill_default` on `tier_a`), with the YAML header's derivation rules and flagged judgment calls carried as prose. 1 write_id.
   128	    67	- Refusals: blocks already present (create-once); market_reset; `--apply` without `--hitl <token>`; `COBALT_ENV` not matching the target vault.
   129	    68	- `--apply --hitl <token>` records the token as the writer `run_id`, prints each write_id and its `cobalt vault restore --write-id` line.
   130	    69	- **The card** (hub-prepared): the dry-run unified diff + its sha256, the verbatim-source table per field, the PROPOSED windows, the `ft=4` comparison (E4), and the rollback lines. Approval = the token in Dejan's own words. Sol builds and tests the command against fixtures only; the real dry-run and apply are LIVE steps L6.
   131	    70	
   132	    71	### D3 — Tables: `db_migrations/0004_radar_pool.sql` (+ rollback)
   133	    72	
   134	    73	```
   135	    74	system.radar_pool
   136	    75	  pool_key         TEXT PRIMARY KEY CHECK (pool_key ~ '^[a-z0-9_]+$')
   137	    76	  state            TEXT NOT NULL CHECK (state IN ('scanning','idle','paused_market_reset','stopped'))
   138	    77	  degraded         BOOLEAN NOT NULL DEFAULT false
   139	    78	  degraded_sources JSONB NOT NULL DEFAULT '[]'   -- [{source, reason, since}]
   140	    79	  sources          JSONB NOT NULL DEFAULT '[]'   -- active source ids with sha12
   141	    80	  session          TEXT NOT NULL                 -- F1 at last stamp
   142	    81	  cap              INTEGER NOT NULL
   143	    82	  members          INTEGER NOT NULL
   144	    83	  last_scan_at     TIMESTAMPTZ
   145	    84	  last_scan_ms     INTEGER
   146	    85	  budget           JSONB                          -- {planned_rpm, limit_rpm}
   147	    86	  updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
   148	    87	
   149	    88	system.radar_membership                           -- one row per EPISODE
   150	    89	  id             BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
   151	    90	  pool_key       TEXT NOT NULL REFERENCES system.radar_pool(pool_key)
   152	    91	  ticker         TEXT NOT NULL
   153	    92	  trade_date     DATE NOT NULL                    -- ET
   154	    93	  first_seen_at  TIMESTAMPTZ NOT NULL
   155	    94	  entered_at     TIMESTAMPTZ                      -- NULL = never admitted
   156	    95	  left_at        TIMESTAMPTZ
   157	    96	  source         TEXT NOT NULL                    -- 'screen:<key>@<sha12>' | 'list:<key>@<sha12>' (best-ranked at first sight)
   158	    97	  sources        JSONB NOT NULL                   -- every source id that listed it while open
   159	    98	  rank_at_entry  INTEGER
   160	    99	  excluded_by    TEXT CHECK (excluded_by IN ('config_cap','not_equity','screen_inactive','manual'))
   161	   100	  session        TEXT NOT NULL                    -- F1 at first sight
   162	   101	  CHECK (entered_at IS NOT NULL OR excluded_by IS NOT NULL)
   163	   102	  CHECK (left_at IS NULL OR left_at >= first_seen_at)
   164	   103	  UNIQUE INDEX (pool_key, ticker) WHERE left_at IS NULL
   165	   104	  INDEX (trade_date, ticker)
   166	   105	
   167	   106	"user".aset_sizings  ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))
   168	   107	                     ADD pool_member_id BIGINT REFERENCES system.radar_membership(id)
   169	   108	"user".day_modes     ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))
   170	   109	```
   171	   110	
   172	   111	- Episode rules: admitted → `entered_at`, `excluded_by` NULL. Dropped by cap / manual / window → `left_at` + `excluded_by`. Fell off every source → `left_at`, `excluded_by` NULL. Never admitted → `entered_at` NULL + `excluded_by`, closed when it stops being a candidate. Later admission of an excluded candidate closes that episode and opens an admitted one (J1 points at admitted episodes). First active cycle of a new trade date closes every open episode at the prior session end.
   173	   112	- Ownership + grants: `OWNER TO cobalt_system` on both tables; `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`; `GRANT SELECT ON system.radar_pool TO cobalt_user`.
   174	   113	- Nullable in P1: `pool_member_id` stays nullable forever (manual cards). `account_mode` NOT NULL is a later migration after E1 (the `aset 0004_session → 0005_session_not_null` precedent).
   175	   114	- Rollback SQL: drop `pool_member_id`, both `account_mode` columns, `DROP TABLE system.radar_membership, system.radar_pool`. **Cost, stated:** membership history and account-mode stamps are lost; the L1 `pg_dump` is the belt.
   176	   115	- **Rollback domain fix (F1):** `cobalt db migrate --rollback` REQUIRES `--down-to NNNN` and reverses only registered migrations newer than NNNN, newest first; without it, it refuses and lists targets. Round-trip test: `migrate → --rollback --down-to 0003 → migrate` gives identical digests, and 0003's columns survive the 0004 rollback. **Hardening verdict:** adopted; a whole-list rollback in prod is one keystroke from moving every table to `public`.
   177	   116	
   178	   117	### D4 — Pool job `com.cobalt.radar` (F2)
   179	   118	
   180	   119	- **Registry:** resident, `supervisor: self`, `timeout_s: 300`, `enabled: false` at merge (flipped in L11 after the first clean scan — `com.cobalt.herdr` precedent, `jobs.yaml:130-136`), `reads:` DERIVED by instrumenting one cycle's `open`/`read_text` (09-09 method), each entry citing file:line.
   181	   120	- **Plist:** `uv run cobalt radar run`; `RunAtLoad true`; `KeepAlive {SuccessfulExit: false}` (a kill-switch exit 0 is not respawned; a crash is); `COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`; `logs/radar.{log,err}`. `ops/README.md` gains: after `cobalt resume`, `launchctl kickstart gui/$(id -u)/com.cobalt.radar`.
   182	   121	- **Loop:** `job_run` wrapper; `should_keep_running` checked each cycle; one cycle per `radar.scan_interval`.
   183	   122	- **Session gating (asked first, never caught):** F1 session ∉ `active_sessions` (radar.yaml: `premarket, rth, aftermarket`) → `idle`, no Finviz call, pool row stamped. `market_reset` → `paused_market_reset`: ZERO writes to pool, membership, bars or mirror; only the F17 job heartbeat stamps, as the heartbeat fix already does. The decision comes from `session_clock()` before the cycle starts, not from a caught `SessionBlocked` (F10). **A cycle is asked twice:** at start, and again immediately before its single commit (pool + membership in one transaction, then bars, then mirror). A cycle that started at 19:59:50 and would commit at 20:00:05 is dropped whole and logged; no partial write lands in the window.
   184	   123	- **Fetch:** active screens = `enabled ∧ active_from ≤ now_et < active_to ∧ session active` → `GET /export/screener?v=152&f=<f>&o=<sort>&c=0,1,…,150`. Lists with `radar: true` → `GET /export/screener?v=152&t=<chunk>&c=0,…,150` chunked by `list_chunk_size`. Raw responses cached to `data/radar-cache/<trade_date>/<source_key>-<HHMMSS>.csv` (gitignored; retention in radar.yaml). Parsed by header NAME (`required_headers` in radar.yaml; a missing header = source failure). Token via `archiver.collector.resolve_token`; every string through `collector.scrub`.
   185	   124	- **Decision (pure function, no I/O, table-tested):** (1) `exclude` block → `manual`; (2) `not_equity` rule (radar.yaml `{header, values}`; values OBSERVED in a recorded export, never guessed) → `not_equity`; (3) rank per radar.yaml `rank:` — P1 default (E2): screen hits desc → best screen position asc → Relative Volume desc → ticker asc, every list-only name after every screen name; (4) top `radar.pool_cap` admitted, rest `config_cap`; (5) a member whose only sources went inactive (window or `enabled: false`) leaves with `screen_inactive`, unless an active list still carries it; (6) a degraded source's members are held and not re-ranked; it adds no new names. Held members count against the cap FIRST: admissions fill only `pool_cap − held`, and a held member is never evicted to admit a new name, so the cap invariant holds while a source is down.
   186	   125	- **Outage:** HTTP error / non-CSV body / header mismatch → that source degraded (named, `since`), pool row degraded, members held; clears on the next good fetch; F18 RED while degraded. Never an empty pool.
   187	   126	- **Budget:** one token bucket per process for every Finviz call (screener + stock) at `radar.finviz_max_rpm`. `cobalt radar check` (dry-run config check) and `run` startup REFUSE when `cap × 60 / poll_interval + active screens + list chunks per minute > finviz_max_rpm`.
   188	   127	
   189	   128	### D5 — Finviz bar poller (same process)
   190	   129	
   191	   130	- After each pool step, for admitted members in rank order: `fetch_bars(ticker, Interval.I1, token)`; keep bars with `ts > watermark` (per ticker, seeded from `max(ts)` in `system.bars`) AND `ts + 1 min ≤ now` (closed bars only); `BarStore.upsert_bars` (one path, archiver schema; the 20:30 archiver finalizes the same keys identically).
   192	   131	- **i1 → 2m:** pure `cobalt.archiver.aggregate.aggregate(bars, minutes)`, buckets floored from 00:00 ET, NOT stored. Stored `i2` stays Finviz's own from the archiver, so no key has two writers. Test on the replay day: aggregate(i1) vs archiver i2 → agreement % in the report; any systematic mismatch (bucket alignment, volume) → ESCALATE, never tuned away.
   193	   132	- Cadence `radar.poll_interval` (60 s) → ≥2 polls per 2m bar.
   194	   133	
   195	   134	### D6 — Account-mode tag
   196	   135	
   197	   136	- `"user".day_modes.account_mode` set by `cobalt daymode account-mode live|sim [--date]` (market_reset-gated like every day-mode write). E1 rules the real flow.
   198	   137	- `AsetStore` INSERT (`aset/store.py:109`) stamps `account_mode` from today's `day_modes` row. The card shows `LIVE`, `SIM`, or a loud `ACCOUNT MODE UNSET` badge. P1 never refuses a card on it (what the sheet accepts is unchanged).
   199	   138	- `pool_member_id`: column + FK only; nothing writes it in P1 (S2-P2).
   200	   139	
   201	   140	### D7 — J1
   202	   141	
   203	   142	Suite: catalog proof that the FK on `"user".aset_sizings.pool_member_id` references `system.radar_membership(id)`. As `cobalt_user`: SELECT `system.radar_membership` OK, INSERT denied, an `aset_sizings` insert with a valid id OK and with an invalid id FK-fails. As `cobalt_system`: SELECT `"user".aset_sizings` denied.
   204	   143	
   205	   144	### D8 — `cobalt db query` (R3)
   206	   145	
   207	   146	- `cobalt db query --side user|system [--prod] [--format json|table] [--limit 1000] "<sql>"`. Connection = `db.connect(dbname, side=…)` (factory, `cobalt_app`, SET ROLE). `--prod` = `allow_prod=True` (RULING 7 tooling seam); otherwise `env.resolve_db_name()`. Lives in `src/cobalt/db_query.py`, registered under the existing `db` group (`db_migrations/cli.py:196`). No new `psycopg.connect`.
   208	   147	- **Code guard (before the server):** a tokenizer aware of quotes, dollar-quotes and comments. Exactly one statement; first keyword `SELECT` or `WITH`. Refused anywhere as a bare word: INSERT UPDATE DELETE MERGE TRUNCATE CREATE ALTER DROP GRANT REVOKE COPY CALL DO SET RESET LOCK VACUUM ANALYZE REFRESH COMMENT LISTEN NOTIFY PREPARE EXECUTE DEALLOCATE DISCARD INTO, and `FOR UPDATE|SHARE|NO KEY UPDATE|KEY SHARE`. Functions `set_config pg_sleep pg_terminate_backend pg_cancel_backend pg_advisory_* lo_* dblink* pg_read_file pg_read_binary_file pg_ls_dir nextval setval` are refused. Refusal = exit 2 with one loud line naming the token.
   209	   148	- **Belt:** `BEGIN READ ONLY`; `SET LOCAL statement_timeout` from tunable `db.query.timeout_s`; query wrapped `SELECT * FROM (<sql>) AS q LIMIT n` (a data-modifying CTE cannot sit in a subquery); always ROLLBACK; `current_user` asserted equal to the side role afterwards. Output passes through F19 redaction before print.
   210	   149	- Tests: every refused class; keyword inside a string literal passes; multi-statement; data-modifying CTE; `set_config('role', …)` switch; user side reads `system.x` qualified; `cobalt_brain` without `--prod` refuses.
   211	   150	
   212	   151	### D9 — F18 `radar` probe
   213	   152	
   214	   153	`probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat` (`heartbeat/runner.py:83-107`). `enabled: false` → OK "NOT PROBED". No pool row → RED. `market_reset` → OK "paused". Inactive session → OK "idle (<session>)". Active session → RED when `now − last_scan_at > heartbeat.radar_max_age_s`; RED when degraded (each source + reason + since); RED when any mirror row is `parse_failed` (names the screen/list).
   215	   154	
   216	   155	### D10 — Config
   217	   156	
   218	   157	- `configs/cobalt/taxonomy/tunables.yaml`, EXISTING units/status/source values only (F11): `radar.pool_cap` 50 `count`; `radar.scan_interval` 60 `duration`; `radar.poll_interval` 60 `duration`; `radar.finviz_max_rpm` `count` (value from build step 1); `heartbeat.radar_max_age_s` 180 `duration`; `db.query.timeout_s` 30 `duration`. If no existing enum value fits a row → ESCALATE; do not add one.
   219	   158	- NEW `configs/cobalt/radar.yaml` (Pydantic, extra=forbid; `cobalt radar check` = dry-run): `pool_key`, `notes {screens, lists}`, `active_sessions`, `export {v: 152, columns: 0-150, required_headers}`, `list_chunk_size`, `not_equity {header, values}`, `rank`, `cache {dir: data/radar-cache, retention_days}`.
   220	   159	- `configs/cobalt/jobs.yaml`: the `com.cobalt.radar` row (D4).
   221	   160	- Boundary: both new paths under `configs/cobalt/` (old loader glob is top-level only) — checked before adding, not after.
   222	   161	
   223	   162	### D11 — Stage 2: the archiver onto the Lists note; `watchlists.yaml` leaves
   224	   163	
   225	   164	- `archiver/config.py` builds its targets from the Lists note via `cobalt.radar.notes` (read + validate, NO mirror write — the archiver runs inside market_reset). `archive_targets` = sorted unique `(ticker, interval)` over enabled lists; `backfill_targets(t)` = the `backfill_default` list's intervals. Missing or failed note → loud failure (job `failed`, F18 red).
   226	   165	- No archiver plist change: in production `resolve_vault_path()` returns the real vault from `COBALT_ENV=production` alone (`vault.py:159-160`), which the archiver plist already sets.
   227	   166	- Sides: the archiver still opens only system-side DB stores (ADR-0008 D2 row unchanged); it reads one vault FILE. The radar job's D2 row: `RadarStore`, `BarStore`, `JobStore` → system; `TraderSettingsStore` (mirror) → user.
   228	   167	- **Equality proof before delete:** `cobalt radar sources --archiver-diff --yaml-rev <sha>` prints `archive_targets` and `backfill_targets` from the note vs from `watchlists.yaml` at that git revision — must be empty. Fixture test in the suite; prod run in L8.
   229	   168	- **Stage 2 commit** = archiver switch + test re-target + `git rm configs/cobalt/watchlists.yaml`, last on the branch. Its rollback = `git revert <stage2>`. It is separate because the 20:30 archiver needs the note, and the note exists only after L6, which needs stage-1 code on main.
   230	   169	
   231	   170	### D12 — Smoke (dev vault + cobalt_dev) — sprint acceptance
   232	   171	
   233	   172	| # | Check | Pass |
   234	   173	|---|---|---|
   235	   174	| S0 | Recorded session: `COBALT_ENV=dev uv run archiver --backfill <T>` for every fixture ticker (F14) | ≥1 full trading day of i1 + i2 in cobalt_dev; the day is named in the report |
   236	   175	| S1 | `cobalt db migrate` on cobalt_dev; `--rollback --down-to 0003`; `migrate` | proof clean, radar tables CREATED, digests identical across the round-trip |
   237	   176	| S2 | Replay `cobalt radar scan --replay <day> --from 04:00 --to 16:00` over cached screener CSVs built from the corpus by `cobalt radar replay-build <day>` (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions present; replay-only, named as such) | pool churns: ≥1 enter and ≥1 leave |
   238	   177	| S3 | Cap | `max(open admitted members) ≤ radar.pool_cap` at every cycle (SQL over membership), including cycles with a degraded source |
   239	   178	| S4 | Entry on RVOL | a name whose proxy RVOL crosses the fixture screen's threshold at T has `entered_at ≤ T + scan_interval` |
   240	   179	| S5 | `excluded_by` | ≥1 row each of `config_cap`, `not_equity`, `screen_inactive`, `manual` |
   241	   180	| S6 | Window gate | no episode with `source` = the fixture screen entered before 10:00 ET; ≥1 after |
   242	   181	| S7 | market_reset | a cycle at 20:30 ET: row counts in pool, membership, bars, `trader_settings` unchanged; state `paused_market_reset`; no `SessionBlocked` in logs |
   243	   182	| S8 | Degraded | fixture source → HTTP 500: pool row degraded, members held, probe RED naming it; broken block → mirror `parse_failed`, probe RED naming it |
   244	   183	| S9 | Poller | member i1 bars upserted, closed bars only, watermark honoured; aggregate-vs-i2 agreement % reported |
   245	   184	| S10 | Probe | `radar` OK fresh / RED stale in session / OK idle out of session |
   246	   185	| S11 | Account mode + J1 | card stamped + badge rendered (`GET /` on a dev sheet); UNSET badge when day row NULL; J1 suite green |
   247	   186	| S12 | Whole system | `uv run pytest tests/cobalt tests/taxonomy` green; `uv run cobalt validate` exit 0; `cobalt jobs readers` for every changed config path; R2 grep clean |
   248	   187	| S13 | Stage 2 | archiver-diff empty on fixtures; `archiver --backfill` still works from the note |
   249	   188	
   250	   189	Sol runs the smoke against a worktree-local vault copy (`data/smoke-vault`, gitignored) because it cannot write `~/dev-vault-cobalt` (F15). The hub re-runs S1–S13 against `~/dev-vault-cobalt` + cobalt_dev as ground truth (L35).
   251	   190	
   252	   191	## §3 Houses and RESTARTS (R5)
   253	   192	
   254	   193	Build = `gpt-5.6-sol`, high effort, `-s workspace-write -c sandbox_workspace_write.network_access=true`, cannot commit. Hub = Sonnet: launch, wait, verify against ground truth, commit on branch. Gated vault write = hub, after approval.
   255	   194	
   256	   195	RESTARTS, derived by rule from the expected diff (Sol re-derives it from the real `git diff --name-status main...HEAD`):
   257	   196	
   258	   197	| Path (expected) | Rule | RESTART |
   259	   198	|---|---|---|
   260	   199	| `ops/com.cobalt.radar.plist` (A) | plist in diff | `com.cobalt.radar` — bootstrap (new) |
   261	   200	| `configs/cobalt/taxonomy/tunables.yaml` (M) | in a resident's `reads:` → `com.cobalt.aset` (`jobs.yaml:69`, `taxonomy/loader.py:79`) | `com.cobalt.aset` kickstart |
   262	   201	| `configs/cobalt/radar.yaml` (A) | only in radar's `reads:` | covered by the bootstrap |
   263	   202	| `configs/cobalt/jobs.yaml` (M, and again in L11) | registry | `cobalt jobs register` |
   264	   203	| `configs/cobalt/watchlists.yaml` (D, stage 2) | `cobalt jobs readers` → none (archiver is a one-shot) | none |
   265	   204	| `src/**` incl. `db_migrations/0004*.sql` | code | none (the migration is LIVE step L3, not a restart) |
   266	   205	| `tests/**`, `docs/**`, `ops/README.md` | tests/docs | none |
   267	   206	| anything else | unclassified | ESCALATE, never dropped |
   268	   207	
   269	   208	## §4 Build step 1 — Finviz throttle re-measure (FIRST)
   270	   209	
   271	   210	- `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`. Names = the 50 synthetic-fixture tickers. Refuses 09:00–16:00 ET on trading days (his live session) and inside market_reset.
   272	   211	- Per cycle: sequential `/export/stock?p=i1` for each name, then one screener call with the fixture filter. STOP at the first non-200, 429, redirect, non-CSV body or header mismatch.
   273	   212	- Per stage: requests, achieved req/min, statuses, p50/p95 latency, bytes → `data/radar-throttle-<ts>.json` + a printed table.
   274	   213	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`; the row's `consumers` cites the report. If the 10 s stage is clean, the report says "no throttle observed up to N req/min" (a floor, not a ceiling). Never extrapolate.
   275	   214	- Token resolution fails in the sandbox → NOT RUN with the scrubbed error line; the hub runs the same command. Offline steps continue. READY FOR MERGE requires the number.
   276	   215	
   277	   216	## §5 NOT in P1
   278	   217	
   279	   218	Precondition evaluator (F8), dots / ladder (F10), radar panel, F3 rank display, F12 missed replay, F13 auto-archive. Writing `pool_member_id`. `account_mode NOT NULL`. Hysteresis at the cap. The four-list re-export (E3).
   280	   219	
   281	   220	## §6 LIVE block — named steps, one rollback domain each
   282	   221	
   283	   222	Window: trading-day 16:15–19:40 ET or a weekend daytime. Never 09:00–16:00, 20:00–21:30, 21:25–21:55 (backup), or 23:27–23:47 (generated commit).
   284	   223	
   285	   224	| Step | Action | Proof | Rollback (domain) |
   286	   225	|---|---|---|---|
   287	   226	| L0 PRECONDITIONS | heartbeat fix merged + deployed + green; branch rebased; suite green on the rebased head; report READY FOR MERGE; `git tag pre-s2-p1` on main | report + tag | — |
   288	   227	| L1 SNAPSHOT | `uv run cobalt backup run` | restic id + dump printed | belt for DB + vault |
   289	   228	| L2 CODE stage 1 | hub rebases the branch onto current main (the nightly generated commit moves main), then `git -C ~/cobalt merge --ff-only <stage1-sha>`; `git tag s2-p1-stage1` | `git log -1` | reset to `pre-s2-p1` + RESTARTS again (code) |
   290	   229	| L3 DB | `uv run cobalt db migrate --allow-prod` | every existing table OK; radar tables CREATED | `cobalt db migrate --allow-prod --rollback --down-to 0003` (DB) |
   291	   230	| L4 REGISTRY | `uv run cobalt validate`; `uv run cobalt jobs register` | exit 0; radar row `enabled: false` | re-register at the previous tag |
   292	   231	| L5 RESTARTS stage 1 | `launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` | `curl -s :5010/api/health` → `ok:true`; next beat `sheet daymode` OK | kickstart again after the code rollback |
   293	   232	| L6 VAULT (HITL) | hub, after approval: `COBALT_ENV=production uv run cobalt radar seed --dry-run` → diff sha256 == card's; then `--apply --hitl <token>` | 5 write_ids printed | `uv run cobalt vault restore --write-id <id>` ×5, or the L1 snapshot (vault) |
   294	   233	| L7 SOURCES | `uv run cobalt radar sources` | every block `ok`; Day Scan `active_from "10:00"`; list counts == YAML counts | — |
   295	   234	| L8 PROOF | `uv run cobalt radar sources --archiver-diff --yaml-rev HEAD` | empty diff | — |
   296	   235	| L9 CODE stage 2 | `git merge --ff-only sprint-2/radar-pool`; `git tag s2-p1`; `cobalt jobs readers configs/cobalt/watchlists.yaml` | readers: none | `git revert <stage2-sha>` (source switch) |
   297	   236	| L10 LAUNCHD | `cp ops/com.cobalt.radar.plist ~/Library/LaunchAgents/`; `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.radar.plist` | first cycle in `logs/radar.log`; `cobalt db query --prod --side system "select state, degraded, members, last_scan_at from radar_pool"` | `launchctl bootout gui/$(id -u)/com.cobalt.radar` (launchd) |
   298	   237	| L11 ENABLE | `jobs.yaml` `enabled: true` on main; `cobalt jobs register` | registry | flip back + register |
   299	   238	| L12 HEARTBEAT | next beat | GREEN, `radar` line present | — |
   300	   239	| L13 NEXT SESSION | 04:00+ `scanning`; Day Scan: no episode before 10:00, sources list it active after; 20:00–21:00 radar row counts constant, no RED; 20:30 archiver exit 0, target count == prior night | `cobalt db query` + logs | per domain above |
   301	   240	
   302	   241	## §7 Risks
   303	   242	
   304	   243	| Risk | Mitigation |
   305	   244	|---|---|
   306	   245	| Finviz lockout on his Elite login (probe or poller) during trading | probe refuses 09:00–16:00; stop-on-first-error ramp; 0.5 safety factor; single token bucket; startup budget refusal |
   307	   246	| Real screen data reaching the repo (reports, cache, fixtures) | cache under gitignored `data/`; reports name screens by key only, never `f=`; R2 grep + suite test |
   308	   247	| Rebase conflicts with the heartbeat fix | expected in `db_migrations/__init__.py`, `db_migrations/cli.py` (digest list), `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`, `test_jobs.py` — rebase first, never after |
   309	   248	| First resident + `self`: zombie path unexercised | watchdog test: stale heartbeat → `zombie`; plist unloaded → RED |
   310	   249	| i1 export ~9.4k rows × 50 names per poll = parse cost | watermark filter before model build; `last_scan_ms` on the pool row; smoke reports p95 cycle ms |
   311	   250	| Cap-boundary oscillation → episode churn | smoke reports episodes/day; hysteresis is E2's ruling |
   312	   251	| Cache growth (~7k CSVs per trading day) | retention in radar.yaml; smoke measures bytes/day |
   313	   252	| Finviz serves `p=i2` natively (DATA-SOURCE-MEMO A.2.1), so i1→2m aggregation may disagree with Finviz's own 2m bars | ruled i1→2m kept; the S9 agreement % against archived i2 decides; a systematic mismatch is ESCALATE, not a silent switch |
   314	   253	| A cycle straddling 20:00 ET | second session check before commit; dropped whole (D4) |
   315	   254	| Sol cannot reach cobalt_dev or has no DB env | the hub exports DB env from `~/cobalt/.env` at launch (never printed); DB tests Sol cannot run are reported NOT RUN, and the hub runs them |
   316	   255	
   317	   256	## §8 ESCALATE
   318	   257	
   319	   258	```
   320	   259	ESCALATE:
   321	   260	E1 ACCOUNT MODE SOURCE — no live/sim value exists anywhere (day_modes, trader_settings, configs).
   322	   261	   P1 adds nullable day_modes.account_mode + a CLI setter, stamps cards, shows a loud UNSET badge,
   323	   262	   never refuses a card. Rule: who sets it and when (sheet day-mode step?), and must an UNSET card be refused.
   324	   263	E2 POOL RANK AT THE CAP — today's static tiers alone (~260 names) exceed pool_cap 50 five-fold, so the
   325	   264	   rank rule chooses the pool every minute. P1 default: screen names first (hits, screen position), then
   326	   265	   list names by RVOL, ticker tie-break, no hysteresis. Selection logic: rule it or replace it.
   327	   266	E3 FOUR LISTS NOT RECOVERABLE — watchlists.yaml holds 3 derived tiers, not Green/Red/SMB Daily Watch/
   328	   267	   Watchlist. P1 migrates the tiers verbatim (source = list:tier_a…). Re-export the four lists into the
   329	   268	   Lists note if membership must name them.
   330	   269	E4 ft=4 DROPPED BY THE R1 KEY LIST — 3 of 4 pasted URLs carry it; meaning unverified. The card shows
   331	   270	   ticker sets with vs without ft=4 per screen; any difference needs an `ft` key added to R1's contract.
   332	   271	E5 USER DATA IN AN UNCOMMITTED REPORT — docs/40 - DevDocs/reports/day-open-2026-09-10.md §2 C.1 quotes
   333	   272	   all four screens' full f= strings and columns; it commits at day close → L32 breach. Redact first.
   334	   273	E6 R5 RULE GAP — "code → none" leaves a resident on stale code whenever no reads: file changes (here the
   335	   274	   sheet's account-mode stamp/badge). P1 is covered only because tunables.yaml restarts the sheet anyway.
   336	   275	   Rule: does a code change under a resident's import tree restart it.
   337	   276	```
   338	   277	
   339	   278	## §9 DISSENT
   340	   279	
   341	   280	No review round completed, so there are no reviewer objections to adopt or decline.
   342	   281	
   343	   282	- **Round 1 FAILED:** `codex exec -m gpt-6-astra` hit "You've hit your usage limit … try again at 11:31 AM" after 72,175 tokens. The model read the plan, ADR-0008, DATA-SOURCE-MEMO, `db_migrations/`, `jobs/wrapper.py`, `jobs/watchdog.py` and `daymode/store.py`, then stopped without issuing any BLOCKER, RISK or VERDICT. Capture: `plan-s2-p1-astra-r1.md`.
   344	   283	- Its last progress message named three boundaries it was about to check: disabled-job startup, scans crossing market_reset, held members vs the pool cap. The architect checked them without the reviewer. The last two were real gaps and are fixed in D4 and D12 S3. The first holds: `job_run` does not read `enabled` (`wrapper.py:122-162`).
   345	   284	- **Rounds 2–3:** not run. Codex has one shared five-hour pool (`limit_id codex`, day-open §1.4), the same pool Sol builds on. The hub should run the review command (same prompt, same capture path pattern) after the reset and BEFORE launching Sol. Objections left after round 3 are added here, one line each.
   346	   285	
   347	   286	=== RULINGS ADDENDUM 2026-09-10 (Dejan) ===
   348	   287	E1 Account mode: standing value `live` in "user".trader_settings; a per-day `sim` switch on the morning sheet-attestation control (same control that attests the .htk sheet, one extra tap) writes day_modes.account_mode for that day only; every card is stamped from day override → standing value; a card with no value is REFUSED, loud — never stamped UNSET and let through.
   349	   288	E2 Pool rule — lives in the vault note beside the screens (user data, L32), read by the collector like the screen blocks:
   350	   289	```yaml
   351	   290	pool:
   352	   291	  cap: 50
   353	   292	  priority: [screens, lists]
   354	   293	  rank_metric:
   355	   294	    premarket: volume        # 04:00–09:30 via the F1 session clock
   356	   295	    rth: rvol                # 09:30 onward
   357	   296	  overrides:
   358	   297	    morning_low_float: volume      # this screen ranks by volume in every session
   359	   298	    day_scan_after: "10:00"        # Day Scan takes first priority among screens after 10:00
   360	   299	  stickiness_scans: 3              # out of the top 50 for 3 consecutive scans before dropping
   361	   300	```
   362	   301	Names not admitted get a membership row with `excluded_by = config_cap`.
   363	   302	E3 Static lists: move the three merged tiers as they are; membership `source` names the tier. Named-list attribution comes later, if he re-exports the four TV lists into the vault.
   364	   303	E4 `ft=4`: the HITL card shows each screen's ticker set with and without `ft=4`; any difference → `ft` joins the block contract; no difference → dropped.
   365	   304	E5 User data in reports: before ANY commit, replace the four screens' `f=` strings in every report, plan and review file with "see vault note"; add a repo-wide grep for those strings to the report's checklist.
   366	   305	E6 RESTARTS rule: plist in diff → that job; changed file in a resident's `reads:` → that resident; any src/ change → every resident whose entrypoint imports the changed module (static import walk in the report); unproven → all residents; unclassified path → ESCALATE, never dropped.
   367	   306	E7 Credentials: NO DB credentials in Sol's environment or the worktree during the build. Sol runs everything that needs no DB; the hub runs the DB-backed suite, migrations on cobalt_dev, and the dev-vault smoke.
   368	   307	E8 The R1 vault write (four YAML blocks + pool block into `1 - Trading/Radar Screens.md`) is NOT part of the build: Sol writes the parser, the synthetic fixture and a `cobalt radar screens propose` command that prints the proposed blocks + the ft=4 comparison. The hub runs the proposal at LIVE time; Dejan approves the HITL card; only then does the writer write.
   369	   308	=== END ADDENDUM ===
   370	     1	# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`
   371	     2	
   372	     3	You build S2-P1 (radar pool + Finviz bar poller) in this worktree. Everything you need is in this
   373	     4	file. The plan it implements is `docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md`,
   374	     5	in this worktree. Where the two disagree, the plan wins; say so in the report.
   375	     6	
   376	     7	## 0. Who does what
   377	     8	
   378	     9	| House | Does | Cannot |
   379	    10	|---|---|---|
   380	    11	| **You (Sol)**, high effort, `-s workspace-write`, network on | write code, tests, docs, the report, inside this worktree | commit, rebase, write outside the worktree, touch the real vault or `cobalt_brain` |
   381	    12	| **Hub (Sonnet)** | launches you, verifies against ground truth, commits per step on `sprint-2/radar-pool`, runs what your sandbox cannot | build |
   382	    13	| **Dejan** | approves the HITL card | — |
   383	    14	
   384	    15	**Hub, before launching you:** (1) if `ops/heartbeat-market-reset` has merged to main, rebase this
   385	    16	branch onto main first; (2) if the plan's §9 says the Astra review loop has not run, run it and fold
   386	    17	fixes into the plan before launch; (3) export the dev DB credentials into your environment without
   387	    18	printing them.
   388	    19	
   389	    20	**Two runs.** RUN A = steps 0–13 (stage 1). Stop, print `DONE`. The hub commits stage 1, then
   390	    21	relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
   391	    22	Step G is **hub only, after Dejan's approval** — you never run it.
   392	    23	
   393	    24	**Stop rules.** A step you cannot finish → mark it `NOT RUN` or `FAILED` in the report with the
   394	    25	exact error line (scrubbed), then continue with the steps that do not depend on it. Never mark a
   395	    26	test passing that did not run. 3 failed attempts at the same thing → stop that step, ESCALATE.
   396	    27	Print `DONE` as the very last line of every run, nothing after it.
   397	    28	
   398	    29	## 1. Laws (binding — a violation is a failed step)
   399	    30	
   400	    31	1. **Production is sacred (NN#16).** Dev only: `COBALT_ENV=dev`, database `cobalt_dev`, vault =
   401	    32	   `data/smoke-vault` (gitignored copy you make of `~/dev-vault-cobalt`). Never open
   402	    33	   `/Users/cobalt/Vault/Think`. Never connect to `cobalt_brain`. Never `launchctl` anything.
   403	    34	2. **User data never enters the repo (L32).** No real screen, filter string, list or dollar figure in
   404	    35	   any tracked file, report, fixture, test or log line you paste. The repo ships exactly ONE synthetic
   405	    36	   example screen (R2).
   406	    37	3. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error
   407	    38	   string passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
   408	    39	4. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent
   409	    40	   fallback, no plausible-empty artifact, no default invented for a missing value.
   410	    41	5. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
   411	    42	   `archiver.collector.fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
   412	    43	   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
   413	    44	   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`.
   414	    45	6. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted
   415	    46	   (`psycopg.sql.Identifier` in Python); cross-side SQL is schema-qualified (`system.radar_membership`);
   416	    47	   every new table is on a side in `src/cobalt/db_migrations/placement.py` or the suite fails.
   417	    48	7. **Config-as-code.** Pydantic schema per config file, `extra="forbid"`, dry-run command. New-core
   418	    49	   config lives only under `configs/cobalt/` (never `configs/*.yaml` top level).
   419	    50	8. **Tunables.** Thresholds are `configs/cobalt/taxonomy/tunables.yaml` rows. Use EXISTING
   420	    51	   `TunableUnit` / `TunableStatus` / `TunableSource` values only — adding an enum value breaks the
   421	    52	   live ASET sheet (09-09 outage). No fitting value → ESCALATE.
   422	    53	9. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE writing; never rely on catching
   423	    54	   `SessionBlocked`. Radar writes nothing in that window.
   424	    55	10. **Tools fetch, code computes.** No LLM anywhere in P1. All numbers are deterministic code.
   425	    56	11. **Tests per step.** `uv run pytest` for the step's tests before moving on; the whole suite at
   426	    57	    step 13.
   427	    58	12. **Names.** One name per concept across SQL, Python, config and docs (`radar_pool`,
   428	    59	    `radar_membership`, `account_mode`, `pool_member_id`, `excluded_by`).
   429	    60	
   430	    61	## 2. Rulings you implement (09-10, binding)
   431	    62	
   432	    63	- **R1 Radar Screens contract.** Vault note `1 - Trading/Radar Screens.md` gets one fenced YAML block
   433	    64	  per screen: `screen, f, sort, columns, active_from, active_to (session clock, ET), enabled`. It is
   434	    65	  written ONCE, through the vault writer, under ONE HITL card, prose untouched. After that Cobalt only
   435	    66	  reads the note: parse fenced blocks only, reload on file-hash change, mirror each block + hash into
   436	    67	  `"user".trader_settings`; `radar_membership.source` names screen + hash. Parse failure → pool row
   437	    68	  degraded + heartbeat `radar` probe RED naming the screen; never the previous version silently. Day
   438	    69	  Scan is active from 10:00 ET via the F1 session clock — a field, never code.
   439	    70	- **R2 Synthetic example screen.** Exactly one, same fenced format, as the test fixture under
   440	    71	  `tests/fixtures/`; real screens never enter the repo. `git ls-files | grep -i radar` stays clean of
   441	    72	  user data.
   442	    73	- **R3 `cobalt db query`.** Read-only CLI: factory connection, SET ROLE per side, SELECT-only enforced in
   443	    74	  code (reject anything else, loud), output JSON/table. The workers' DB read path.
   444	    75	- **R4 Static lists are user data.** They move user-side by the same mechanism as R1. Plan choice: a new
   445	    76	  vault note `1 - Trading/Radar Lists.md` with fenced blocks. The archiver keeps working through the
   446	    77	  migration (stage 2).
   447	    78	- **R5 Houses + RESTARTS by rule.** plist in diff → that job; changed file in a resident's `reads:` →
   448	    79	  that resident; registry → `register`; code/tests/docs → none; anything unclassified → ESCALATE.
   449	    80	
   450	    81	## 3. Environment
   451	    82	
   452	    83	- Run everything from this worktree with `uv run …`. Tests: `uv run pytest tests/cobalt tests/taxonomy`.
   453	    84	- DB env: the hub exports the Postgres credentials into your environment at launch. If a DB-backed test
   454	    85	  or command fails to connect, record `NOT RUN (db unreachable: <scrubbed error>)` and continue.
   455	    86	- No `psql` on this host. Before step 3 lands, reach the DB only through repo code; after it lands, use
   456	    87	  `uv run cobalt db query --side system|user "<select>"`.
   457	    88	- Finviz token: `cobalt.archiver.collector.resolve_token()`. If it fails in your sandbox, the live half
   458	    89	  of step 1 is `NOT RUN`; the hub runs it.
   459	    90	- Vault for smoke: `cp -R ~/dev-vault-cobalt data/smoke-vault` once, then
   460	    91	  `COBALT_VAULT_PATH=$PWD/data/smoke-vault`. `data/` and `logs/` are gitignored — confirm with
   461	    92	  `git check-ignore` before writing anything there.
   462	    93	- DevDocs layout: one page per `.py` file at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
   463	    94	  `docs/40 - DevDocs/tests/cobalt/<file>.md`, and a line in `docs/40 - DevDocs/INDEX.md`.
   464	    95	
   465	    96	## 4. Build steps
   466	    97	
   467	    98	Each step lists its files, then the tests that must pass before the next step starts.
   468	    99	
   469	   100	### Step 0 — Base check (no code)
   470	   101	- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql`. Present → the heartbeat fix is in
   471	   102	  your base; build on it. Absent → build on main as is, register 0004 after 0002, and list in the report
   472	   103	  the files that will conflict at merge: `db_migrations/__init__.py`, `db_migrations/cli.py`,
   473	   104	  `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`,
   474	   105	  `tests/cobalt/test_jobs.py`.
   475	   106	- Record `git rev-parse HEAD` in the report.
   476	   107	
   477	   108	### Step 1 — Finviz throttle re-measure (FIRST)
   478	   109	- `src/cobalt/radar/throttle.py` + `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`.
   479	   110	- Names = the 50 first tickers of the synthetic lists fixture (step 5 creates it; create that fixture
   480	   111	  file now if needed).
   481	   112	- Refuses on trading days between 09:00 and 16:00 ET, and inside market_reset (use `session_clock()` and
   482	   113	  the NYSE calendar).
   483	   114	- Per cycle: sequential `fetch_bars(t, Interval.I1, token)` for each name, then one
   484	   115	  `/export/screener?v=152&f=<fixture f>&c=0,…,150` call. STOP at the first non-200, 429, redirect,
   485	   116	  non-CSV body or header mismatch.
   486	   117	- Per stage record: requests, achieved req/min, status counts, p50/p95 latency ms, bytes. Write
   487	   118	  `data/radar-throttle-<UTC ts>.json` and print a table.
   488	   119	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`. If every stage was clean, write
   489	   120	  "no throttle observed up to N req/min". Never extrapolate.
   490	   121	- **Tests (mocked HTTP):** stop-on-first-error per class; refusal inside the forbidden window; rpm math;
   491	   122	  token never appears in output (assert `auth=REDACTED`).
   492	   123	- **Live run:** allowed only outside the forbidden window. Otherwise, or on token failure, `NOT RUN`.
   493	   124	
   494	   125	### Step 2 — Migration 0004, rollback bound, placement, J1
   495	   126	- `src/cobalt/db_migrations/0004_radar_pool.sql` and `0004_radar_pool.rollback.sql` with exactly the
   496	   127	  plan's §D3 DDL. Tables are created schema-qualified, `OWNER TO cobalt_system`;
   497	   128	  `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`;
   498	   129	  `GRANT SELECT ON system.radar_pool TO cobalt_user`. The rollback header states its cost.
   499	   130	- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring lines.
   500	   131	- `db_migrations/cli.py`: the digest excludes `account_mode` and `pool_member_id` (extend the heartbeat
   501	   132	  fix's `DIGEST_EXCLUDED_COLUMNS` if present; otherwise generalize `TENANCY_COLUMN` into that tuple).
   502	   133	  `--rollback` REQUIRES `--down-to NNNN`; it reverses only registered migrations newer than NNNN, newest
   503	   134	  first; without it, it refuses and lists targets.
   504	   135	- `placement.py`: move `radar_pool`, `radar_membership` out of `DECLARED_TABLES` into a new
   505	   136	  `CREATED_TABLES` dict ("created by a db_migration directly on its side"), included in `PLACEMENT` and
   506	   137	  in the proof table; extend the SQL/Python agreement test to 0004.
   507	   138	- **Tests** (`tests/cobalt/test_tenancy.py`, `tests/cobalt/test_radar_migration.py`):
   508	   139	  migrate twice idempotent; `migrate → --rollback --down-to 0003 → migrate` digests identical;
   509	   140	  0003's columns (if present) survive the 0004 rollback; `--rollback` without `--down-to` refuses;
   510	   141	  placement test green; J1 — FK catalog proof, `cobalt_user` SELECT OK / INSERT denied on
   511	   142	  `system.radar_membership`, valid id insert OK / invalid FK-fails, `cobalt_system` SELECT on
   512	   143	  `"user".aset_sizings` denied; membership CHECKs (`entered_at IS NOT NULL OR excluded_by IS NOT NULL`)
   513	   144	  and the partial unique index reject bad rows.
   514	   145	
   515	   146	### Step 3 — `cobalt db query` (R3)
   516	   147	- `src/cobalt/db_query.py`, registered as `db query` in `db_migrations/cli.py`'s `db` group.
   517	   148	- `--side user|system` (required), `--prod` (`allow_prod=True`), `--format json|table`, `--limit`
   518	   149	  (default 1000). Connection = `db.connect(dbname, side=…)`.
   519	   150	- The guard and the belt exactly as plan §D8 (tokenizer aware of quotes, dollar-quotes and comments;
   520	   151	  single SELECT/WITH; refused words and functions; `BEGIN READ ONLY`; `SET LOCAL statement_timeout`
   521	   152	  from tunable `db.query.timeout_s`; `SELECT * FROM (<sql>) AS q LIMIT n`; always ROLLBACK;
   522	   153	  `current_user` asserted; output through F19 redaction).
   523	   154	- **Tests** (`tests/cobalt/test_db_query.py`): each refused class exits 2 with the token named; a
   524	   155	  keyword inside a string literal passes; multi-statement refused; data-modifying CTE refused;
   525	   156	  `set_config('role', …)` refused; user side reads `system.bars` qualified; `cobalt_brain` without
   526	   157	  `--prod` refuses (no connection attempted); the `psycopg.connect` lint still passes.
   527	   158	
   528	   159	### Step 4 — Config
   529	   160	- `configs/cobalt/radar.yaml` + `src/cobalt/radar/config.py` (Pydantic, `extra="forbid"`): `pool_key`,
   530	   161	  `notes {screens: "1 - Trading/Radar Screens.md", lists: "1 - Trading/Radar Lists.md"}`,
   531	   162	  `active_sessions [premarket, rth, aftermarket]`,
   532	   163	  `export {v: 152, columns: "0-150", required_headers: [...]}`, `list_chunk_size`,
   533	   164	  `not_equity {header, values}`, `rank`, `cache {dir: data/radar-cache, retention_days}`.
   534	   165	- `required_headers` and the `not_equity` values come from a REAL recorded export header (step 6
   535	   166	  captures one) — until then mark them `# UNVERIFIED` and a test asserts they are replaced before step 13.
   536	   167	- `tunables.yaml` rows: `radar.pool_cap` 50 count; `radar.scan_interval` 60 duration;
   537	   168	  `radar.poll_interval` 60 duration; `radar.finviz_max_rpm` count (step 1 value);
   538	   169	  `heartbeat.radar_max_age_s` 180 duration; `db.query.timeout_s` 30 duration. Mirror the neighbouring
   539	   170	  rows' `scope/dynamic/status/source/consumers` shape.
   540	   171	- `cobalt radar check`: validates radar.yaml + tunables, and REFUSES when
   541	   172	  `pool_cap × 60 / poll_interval + max active screens + list chunks per minute > finviz_max_rpm`.
   542	   173	- **Tests** (`tests/cobalt/test_radar_config.py`): bad key crashes naming the file; budget refusal; every
   543	   174	  new tunable resolves; `load_tunables()` still validates (the ASET sheet reads this file).
   544	   175	
   545	   176	### Step 5 — Notes parser, fixtures, mirror (R1, R2, R4)
   546	   177	- `src/cobalt/radar/models.py` (`ScreenBlock`, `ListBlock`, `ExcludeBlock`, `SourceSet`, `ExcludedBy`),
   547	   178	  `src/cobalt/radar/notes.py` (plan §D1): read bytes once, hash those bytes, fenced ```` ```yaml ````
   548	   179	  blocks only, every yaml fence must validate, sha256 per block and per note, key slugs unique.
   549	   180	- Mirror via `TraderSettingsStore.put`: keys `radar.note.screens`, `radar.note.lists`,
   550	   181	  `radar.screen.<key>`, `radar.list.<key>`, `radar.exclude`; value
   551	   182	  `{block, block_sha256, note_sha256, status: ok|parse_failed|removed, error}`;
   552	   183	  `source = vault:<note path>@<sha12>`. Writes only when the note hash changed. Never writes inside
   553	   184	  market_reset.
   554	   185	- Fixtures: `tests/fixtures/radar/radar-screens.example.md` — ONE synthetic screen (`screen: Example
   555	   186	  Session Scan`, synthetic `f`, `active_from: "10:00"`, `active_to: "16:00"`, `enabled: true`, a short
   556	   187	  prose paragraph around it). `tests/fixtures/radar/radar-lists.example.md` — synthetic lists: ≥60
   557	   188	  large-cap tickers (rule: well-known index heavyweights, not copied from any file in this repo), one
   558	   189	  ETF (for `not_equity`), one `exclude` block, `archive` intervals, exactly one `backfill_default`.
   559	   190	- **Tests** (`tests/cobalt/test_radar_notes.py`): fixture parses; each field's validation failure names
   560	   191	  the block; a non-validating yaml fence is a named failure; prose/markers ignored; hash stable across
   561	   192	  re-reads and changes on a one-byte edit; parse failure → mirror row `parse_failed`, never the old
   562	   193	  block; `TraderSettings.from_db()` returns identically with the radar rows present (the sheet cannot
   563	   194	  break); R2 test (file CONTENTS): no tracked file under `src/cobalt/`, `configs/cobalt/`,
   564	   195	  `tests/cobalt/`, `ops/` or `docs/40 - DevDocs/` contains `f=` followed by
   565	   196	  `sh_|ta_|fa_|an_|cap_|exch_|geo_|idx_|ind_|sec_|news_|earningsdate_|ipodate_|targetprice_`,
   566	   197	  outside `tests/fixtures/radar/` (use `git ls-files` for the tracked set).
   567	   198	
   568	   199	### Step 6 — Screener collector, cache, replay
   569	   200	- `src/cobalt/radar/collector.py`: `ScreenerCollector` protocol; `FinvizScreenerCollector` —
   570	   201	  `GET https://elite.finviz.com/export/screener?v=152&f=<f>&o=<sort>&c=0,…,150` for screens and
   571	   202	  `…&t=<chunk>&c=…` for lists; one process-wide token bucket at `radar.finviz_max_rpm` shared with the
   572	   203	  poller; raw CSV cached to `data/radar-cache/<trade_date>/<source_key>-<HHMMSS>.csv`; parse by header
   573	   204	  NAME; missing header / non-CSV / HTTP error → `SourceFailure` (named, never an empty list); every
   574	   205	  string scrubbed.
   575	   206	- Capture ONE real export header with the fixture filter (if network + token work) and pin
   576	   207	  `required_headers` + `not_equity` from it; cite the capture file in the report (the header row only,
   577	   208	  no data rows pasted).
   578	   209	- `src/cobalt/radar/replay.py`: `ReplayCollector` serving cached CSVs by virtual clock, and
   579	   210	  `cobalt radar replay-build <day>` that synthesizes snapshots from `system.bars` i1 in cobalt_dev
   580	   211	  (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions
   581	   212	  present; supports only the fixture screen's filter codes; any other code fails loud). Named
   582	   213	  replay-only in its docstring.
   583	   214	- **Tests** (`tests/cobalt/test_radar_collector.py`): recorded-CSV parse; header mismatch → failure;
   584	   215	  HTML body → failure; `t=` chunking; token bucket pacing (fake clock); cache path under a gitignored
   585	   216	  dir; scrub.
   586	   217	
   587	   218	### Step 7 — Pool decision + store
   588	   219	- `src/cobalt/radar/pool.py`: a pure function `decide(candidates, open_members, sources, cfg, now) →
   589	   220	  transitions`, no I/O, implementing plan §D4 steps 1–6 (manual, not_equity, rank, cap, screen_inactive,
   590	   221	  degraded sources held).
   591	   222	- `src/cobalt/radar/store.py`: `RadarStore` (`SIDE = Side.SYSTEM`) — pool row upsert, membership
   592	   223	  episodes per plan §D3 (open, admit, exclude, leave, trade-date rollover), all transitions of one
   593	   224	  cycle in ONE transaction.
   594	   225	- **Tests** (`tests/cobalt/test_radar_pool.py`, `test_radar_store.py`): table tests for every rule and
   595	   226	  every `excluded_by` value; cap never exceeded; rank tie-break deterministic; a degraded source's
   596	   227	  members held AND counted against the cap first (admissions fill only `pool_cap − held`; a held member
   597	   228	  is never evicted); re-admission closes the excluded episode and opens a new one; rollover closes the prior
   598	   229	  day; store-side lint (own side or qualified).
   599	   230	
   600	   231	### Step 8 — Bar poller + aggregation
   601	   232	- `src/cobalt/radar/poller.py`: for admitted members in rank order, `fetch_bars(t, Interval.I1, token)`
   602	   233	  through the shared token bucket; keep `ts > watermark` (seeded from `max(ts)` per ticker in
   603	   234	  `system.bars`) and `ts + 1 min ≤ now`; `BarStore.upsert_bars`.
   604	   235	- `src/cobalt/archiver/aggregate.py`: pure `aggregate(bars, minutes)`, buckets floored from 00:00 ET,
   605	   236	  OHLCV rules explicit. Never stored.
   606	   237	- **Tests** (`tests/cobalt/test_radar_poller.py`, `test_archiver_aggregate.py`): watermark; open bar
   607	   238	  excluded; upsert idempotent; aggregation on hand-built bars incl. a DST day and a missing minute; an
   608	   239	  agreement check vs stored `i2` on the replay day (DB test) printing the % — any systematic mismatch
   609	   240	  goes to ESCALATE, not a tweak.
   610	   241	
   611	   242	### Step 9 — Resident runner, registry, plist
   612	   243	- `src/cobalt/radar/runner.py` + `cobalt radar run` / `cobalt radar scan --once [--replay <day>
   613	   244	  --from HH:MM --to HH:MM]`: `job_run("com.cobalt.radar")`; `should_keep_running` each cycle; session
   614	   245	  asked FIRST (plan §D4): inactive → `idle`; market_reset → `paused_market_reset` with ZERO radar writes;
   615	   246	  otherwise reload notes → fetch → decide → store → poll bars; one cycle per `radar.scan_interval`;
   616	   247	  `last_scan_ms` stamped. The session is asked AGAIN immediately before the cycle's commit; a cycle
   617	   248	  whose commit would land in market_reset is dropped whole and logged.
   618	   249	- `configs/cobalt/jobs.yaml`: `com.cobalt.radar` — resident, `supervisor: self`, `timeout_s: 300`,
   619	   250	  `enabled: false`, `reads:` derived by instrumenting one `scan --once` (patch `open` / `Path.read_text`
   620	   251	  and record repo-relative paths), each entry with a `# file.py:line (loader)` comment.
   621	   252	- `ops/com.cobalt.radar.plist`: `ProgramArguments` `/Users/cobalt/.local/bin/uv run cobalt radar run`;
   622	   253	  `WorkingDirectory /Users/cobalt/cobalt`; `RunAtLoad true`; `KeepAlive {SuccessfulExit false}`;
   623	   254	  `COBALT_ENV production`; `COBALT_VAULT_PATH /Users/cobalt/Vault/Think`; `PATH` as the archiver plist;
   624	   255	  logs `logs/radar.log` / `logs/radar.err`. No double hyphen inside XML comments.
   625	   256	- `ops/README.md`: radar handover + "after `cobalt resume`, `launchctl kickstart
   626	   257	  gui/$(id -u)/com.cobalt.radar`".
   627	   258	- **Tests** (`tests/cobalt/test_radar_runner.py`, `test_jobs.py`): market_reset cycle writes nothing
   628	   259	  (row counts); a cycle started at 19:59:50 ET with a fake clock that reaches 20:00:05 at commit writes
   629	   260	  nothing; idle cycle makes no HTTP call; kill switch → clean exit 0; `uv run cobalt validate`
   630	   261	  exit 0 (registry ↔ plist); watchdog: stale heartbeat on this resident → `zombie`.
   631	   262	
   632	   263	### Step 10 — F18 `radar` probe
   633	   264	- `probes.radar(now)` in `src/cobalt/heartbeat/probes.py`, added to `take_beat` in
   634	   265	  `heartbeat/runner.py`, exactly plan §D9.
   635	   266	- **Tests** (`tests/cobalt/test_heartbeat.py`): each branch (not probed / no row / paused / idle / fresh /
   636	   267	  stale / degraded names sources / parse_failed names the screen).
   637	   268	
   638	   269	### Step 11 — Account-mode tag
   639	   270	- `"user".day_modes.account_mode` setter: `cobalt daymode account-mode live|sim [--date YYYY-MM-DD]`,
   640	   271	  market_reset-gated like the other day-mode writes.
   641	   272	- `aset/store.py` INSERT stamps `account_mode` from today's `day_modes` row; `aset/web.py` renders a
   642	   273	  `LIVE` / `SIM` / `ACCOUNT MODE UNSET` badge on every card. No card is refused because of it.
   643	   274	- **Tests** (`test_daymode.py`, `test_aset_store.py`, `test_aset_web.py`): setter gated; stamp from the
   644	   275	  row; NULL → UNSET badge; existing card flows unchanged (whole aset test files green).
   645	   276	
   646	   277	### Step 12 — Seed command (fixtures and smoke vault ONLY)
   647	   278	- `src/cobalt/radar/seed.py` + `cobalt radar seed --dry-run | --apply --hitl <token> [--only
   648	   279	  screens|lists]` per plan §D2: prose → blocks with `# from:` verbatim-source comments and
   649	   280	  `# PROPOSED` markers; `upsert_unit` per screen section; `create_if_absent` for the Lists note rendered
   650	   281	  from `configs/cobalt/watchlists.yaml`; create-once refusal; market_reset refusal; `--apply` without
   651	   282	  `--hitl` refuses; prints write_ids + restore lines; `--probe-ft` compares each screen's ticker set with
   652	   283	  and without `ft=4` (hub use).
   653	   284	- **You run it only with `COBALT_VAULT_PATH=$PWD/data/smoke-vault`.** Its prose input is rendered from
   654	   285	  the screen fixture inside the test — no second screen definition.
   655	   286	- **Tests** (`tests/cobalt/test_radar_seed.py`): every pre-existing line byte-identical, diff is
   656	   287	  insertions only; `f` mismatch between the export line and the filters line refuses; the lists note
   657	   288	  round-trips to the same targets as the YAML; second apply refuses; `restore` by write_id returns the
   658	   289	  original bytes.
   659	   290	
   660	   291	### Step 13 — Smoke + report (end of RUN A)
   661	   292	- Run plan §D12 S0–S12 against `data/smoke-vault` + `cobalt_dev` (S0 = `COBALT_ENV=dev uv run archiver
   662	   293	  --backfill <T>` for each synthetic list ticker; it writes only to cobalt_dev). One row per check:
   663	   294	  PASS/FAIL/NOT RUN + the evidence command and its key output line.
   664	   295	- Whole suite: `uv run pytest tests/cobalt tests/taxonomy` (count passed/failed/skipped);
   665	   296	  `uv run cobalt validate`; `uv run cobalt radar check`; `git ls-files | grep -i radar` listing.
   666	   297	- DevDocs page for every new or changed `.py` (layout in §3) + INDEX lines.
   667	   298	- RESTARTS: derive from `git diff --name-status main...HEAD` plus untracked files (`git status
   668	   299	  --porcelain`), one row per path, by the R5 rule, using `uv run cobalt jobs readers <path>` for every
   669	   300	  changed config path. Unclassified → ESCALATE.
   670	   301	- Write the report (§5). Print `DONE`.
   671	   302	
   672	   303	### Step 14 — RUN B: stage 2 (archiver onto the Lists note)
   673	   304	- `archiver/config.py` reads targets from the Lists note via `cobalt.radar.notes` (read + validate only,
   674	   305	  no mirror write); `archive_targets` / `backfill_targets` per plan §D11; missing or failed note → loud.
   675	   306	- `cobalt radar sources [--json] [--archiver-diff --yaml-rev <sha>]`.
   676	   307	- Tests re-targeted to the lists fixture; `git rm`-equivalent: delete `configs/cobalt/watchlists.yaml`
   677	   308	  from the working tree (the hub commits the deletion).
   678	   309	- **Tests:** render a Lists note FROM `configs/cobalt/watchlists.yaml` at RUN A's commit (the hub gives
   679	   310	  you the sha) with the step-12 seed code into `data/smoke-vault`; archiver-diff between that note and
   680	   311	  the YAML at the same sha is empty (the synthetic lists fixture is NOT the comparison — it is different
   681	   312	  data by design); `archiver --backfill <T>` works from the note on cobalt_dev; the whole suite green.
   682	   313	- Update the report (S13 row, stage-2 file list, RESTARTS rows). Print `DONE`.
   683	   314	
   684	   315	### Step G — HUB ONLY, after Dejan approves the HITL card (never Sol)
   685	   316	Run as plan §6 L6–L8, from `~/cobalt` after stage 1 is merged, outside market_reset:
   686	   317	`COBALT_ENV=production uv run cobalt radar seed --dry-run` (diff sha256 must equal the card's) →
   687	   318	`--apply --hitl <token>` → `cobalt radar sources` → `--archiver-diff --yaml-rev HEAD` empty.
   688	   319	
   689	   320	## 5. Report — `docs/40 - DevDocs/reports/s2-p1-2026-09-10.md`
   690	   321	
   691	   322	Report discipline: §0 headline ≤5 lines (what changed, status, ESCALATE count) → tables → ESCALATE.
   692	   323	No restating this brief, no process narration.
   693	   324	
   694	   325	1. **§0 Headline** — READY FOR MERGE / NOT READY (+ the blocking rows).
   695	   326	2. **Base** — `HEAD` sha at step 0; heartbeat fix present or not; expected conflicts.
   696	   327	3. **Steps** — table: step · status · files · tests (passed/failed/skipped) · evidence.
   697	   328	4. **Throttle** — the stage table, `finviz_max_rpm`, or NOT RUN + reason.
   698	   329	5. **Smoke** — S0–S13 table.
   699	   330	6. **Migration proof** — the printed proof tables (forward, rollback --down-to 0003, forward).
   700	   331	7. **`reads:` derivation** — each path with file:line.
   701	   332	8. **RESTARTS derivation** — path · change · rule · restart.
   702	   333	9. **LIVE block** — plan §6 L0–L13, with real shas/tags filled where known, and the rollback column.
   703	   334	10. **DISSENT** — copy plan §9 verbatim.
   704	   335	11. **ESCALATE** — plan E1–E6 carried verbatim + anything new, one line each.
   705	   336	12. **Stage 2 file list** (RUN B).
   706	   337	
   707	   338	You cannot write outside the worktree; the hub copies the report to `~/cobalt/docs/_inflight/` for the
   708	   339	vault.
   709	   340	
   710	   341	Print `DONE` last.
   711	   342	
   712	   343	=== RULINGS ADDENDUM 2026-09-10 (Dejan) ===
   713	   344	E1 Account mode: standing value `live` in "user".trader_settings; a per-day `sim` switch on the morning sheet-attestation control (same control that attests the .htk sheet, one extra tap) writes day_modes.account_mode for that day only; every card is stamped from day override → standing value; a card with no value is REFUSED, loud — never stamped UNSET and let through.
   714	   345	E2 Pool rule — lives in the vault note beside the screens (user data, L32), read by the collector like the screen blocks:
   715	   346	```yaml
   716	   347	pool:
   717	   348	  cap: 50
   718	   349	  priority: [screens, lists]
   719	   350	  rank_metric:
   720	   351	    premarket: volume        # 04:00–09:30 via the F1 session clock
   721	   352	    rth: rvol                # 09:30 onward
   722	   353	  overrides:
   723	   354	    morning_low_float: volume      # this screen ranks by volume in every session
   724	   355	    day_scan_after: "10:00"        # Day Scan takes first priority among screens after 10:00
   725	   356	  stickiness_scans: 3              # out of the top 50 for 3 consecutive scans before dropping
   726	   357	```
   727	   358	Names not admitted get a membership row with `excluded_by = config_cap`.
   728	   359	E3 Static lists: move the three merged tiers as they are; membership `source` names the tier. Named-list attribution comes later, if he re-exports the four TV lists into the vault.
   729	   360	E4 `ft=4`: the HITL card shows each screen's ticker set with and without `ft=4`; any difference → `ft` joins the block contract; no difference → dropped.
   730	   361	E5 User data in reports: before ANY commit, replace the four screens' `f=` strings in every report, plan and review file with "see vault note"; add a repo-wide grep for those strings to the report's checklist.
   731	   362	E6 RESTARTS rule: plist in diff → that job; changed file in a resident's `reads:` → that resident; any src/ change → every resident whose entrypoint imports the changed module (static import walk in the report); unproven → all residents; unclassified path → ESCALATE, never dropped.
   732	   363	E7 Credentials: NO DB credentials in Sol's environment or the worktree during the build. Sol runs everything that needs no DB; the hub runs the DB-backed suite, migrations on cobalt_dev, and the dev-vault smoke.
   733	   364	E8 The R1 vault write (four YAML blocks + pool block into `1 - Trading/Radar Screens.md`) is NOT part of the build: Sol writes the parser, the synthetic fixture and a `cobalt radar screens propose` command that prints the proposed blocks + the ft=4 comparison. The hub runs the proposal at LIVE time; Dejan approves the HITL card; only then does the writer write.
   734	   365	=== END ADDENDUM ===
   735	
   736	exec
   737	/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md' | sed -n '128,380p'; nl -ba 'docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md' | sed -n '1,145p'; rg --files -g AGENTS.md /Users/cobalt/cobalt-wt /Users/cobalt/.codex 2>/dev/null | head -40" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
   738	 succeeded in 0ms:
   739	   128	### D5 — Finviz bar poller (same process)
   740	   129	
   741	   130	- After each pool step, for admitted members in rank order: `fetch_bars(ticker, Interval.I1, token)`; keep bars with `ts > watermark` (per ticker, seeded from `max(ts)` in `system.bars`) AND `ts + 1 min ≤ now` (closed bars only); `BarStore.upsert_bars` (one path, archiver schema; the 20:30 archiver finalizes the same keys identically).
   742	   131	- **i1 → 2m:** pure `cobalt.archiver.aggregate.aggregate(bars, minutes)`, buckets floored from 00:00 ET, NOT stored. Stored `i2` stays Finviz's own from the archiver, so no key has two writers. Test on the replay day: aggregate(i1) vs archiver i2 → agreement % in the report; any systematic mismatch (bucket alignment, volume) → ESCALATE, never tuned away.
   743	   132	- Cadence `radar.poll_interval` (60 s) → ≥2 polls per 2m bar.
   744	   133	
   745	   134	### D6 — Account-mode tag
   746	   135	
   747	   136	- `"user".day_modes.account_mode` set by `cobalt daymode account-mode live|sim [--date]` (market_reset-gated like every day-mode write). E1 rules the real flow.
   748	   137	- `AsetStore` INSERT (`aset/store.py:109`) stamps `account_mode` from today's `day_modes` row. The card shows `LIVE`, `SIM`, or a loud `ACCOUNT MODE UNSET` badge. P1 never refuses a card on it (what the sheet accepts is unchanged).
   749	   138	- `pool_member_id`: column + FK only; nothing writes it in P1 (S2-P2).
   750	   139	
   751	   140	### D7 — J1
   752	   141	
   753	   142	Suite: catalog proof that the FK on `"user".aset_sizings.pool_member_id` references `system.radar_membership(id)`. As `cobalt_user`: SELECT `system.radar_membership` OK, INSERT denied, an `aset_sizings` insert with a valid id OK and with an invalid id FK-fails. As `cobalt_system`: SELECT `"user".aset_sizings` denied.
   754	   143	
   755	   144	### D8 — `cobalt db query` (R3)
   756	   145	
   757	   146	- `cobalt db query --side user|system [--prod] [--format json|table] [--limit 1000] "<sql>"`. Connection = `db.connect(dbname, side=…)` (factory, `cobalt_app`, SET ROLE). `--prod` = `allow_prod=True` (RULING 7 tooling seam); otherwise `env.resolve_db_name()`. Lives in `src/cobalt/db_query.py`, registered under the existing `db` group (`db_migrations/cli.py:196`). No new `psycopg.connect`.
   758	   147	- **Code guard (before the server):** a tokenizer aware of quotes, dollar-quotes and comments. Exactly one statement; first keyword `SELECT` or `WITH`. Refused anywhere as a bare word: INSERT UPDATE DELETE MERGE TRUNCATE CREATE ALTER DROP GRANT REVOKE COPY CALL DO SET RESET LOCK VACUUM ANALYZE REFRESH COMMENT LISTEN NOTIFY PREPARE EXECUTE DEALLOCATE DISCARD INTO, and `FOR UPDATE|SHARE|NO KEY UPDATE|KEY SHARE`. Functions `set_config pg_sleep pg_terminate_backend pg_cancel_backend pg_advisory_* lo_* dblink* pg_read_file pg_read_binary_file pg_ls_dir nextval setval` are refused. Refusal = exit 2 with one loud line naming the token.
   759	   148	- **Belt:** `BEGIN READ ONLY`; `SET LOCAL statement_timeout` from tunable `db.query.timeout_s`; query wrapped `SELECT * FROM (<sql>) AS q LIMIT n` (a data-modifying CTE cannot sit in a subquery); always ROLLBACK; `current_user` asserted equal to the side role afterwards. Output passes through F19 redaction before print.
   760	   149	- Tests: every refused class; keyword inside a string literal passes; multi-statement; data-modifying CTE; `set_config('role', …)` switch; user side reads `system.x` qualified; `cobalt_brain` without `--prod` refuses.
   761	   150	
   762	   151	### D9 — F18 `radar` probe
   763	   152	
   764	   153	`probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat` (`heartbeat/runner.py:83-107`). `enabled: false` → OK "NOT PROBED". No pool row → RED. `market_reset` → OK "paused". Inactive session → OK "idle (<session>)". Active session → RED when `now − last_scan_at > heartbeat.radar_max_age_s`; RED when degraded (each source + reason + since); RED when any mirror row is `parse_failed` (names the screen/list).
   765	   154	
   766	   155	### D10 — Config
   767	   156	
   768	   157	- `configs/cobalt/taxonomy/tunables.yaml`, EXISTING units/status/source values only (F11): `radar.pool_cap` 50 `count`; `radar.scan_interval` 60 `duration`; `radar.poll_interval` 60 `duration`; `radar.finviz_max_rpm` `count` (value from build step 1); `heartbeat.radar_max_age_s` 180 `duration`; `db.query.timeout_s` 30 `duration`. If no existing enum value fits a row → ESCALATE; do not add one.
   769	   158	- NEW `configs/cobalt/radar.yaml` (Pydantic, extra=forbid; `cobalt radar check` = dry-run): `pool_key`, `notes {screens, lists}`, `active_sessions`, `export {v: 152, columns: 0-150, required_headers}`, `list_chunk_size`, `not_equity {header, values}`, `rank`, `cache {dir: data/radar-cache, retention_days}`.
   770	   159	- `configs/cobalt/jobs.yaml`: the `com.cobalt.radar` row (D4).
   771	   160	- Boundary: both new paths under `configs/cobalt/` (old loader glob is top-level only) — checked before adding, not after.
   772	   161	
   773	   162	### D11 — Stage 2: the archiver onto the Lists note; `watchlists.yaml` leaves
   774	   163	
   775	   164	- `archiver/config.py` builds its targets from the Lists note via `cobalt.radar.notes` (read + validate, NO mirror write — the archiver runs inside market_reset). `archive_targets` = sorted unique `(ticker, interval)` over enabled lists; `backfill_targets(t)` = the `backfill_default` list's intervals. Missing or failed note → loud failure (job `failed`, F18 red).
   776	   165	- No archiver plist change: in production `resolve_vault_path()` returns the real vault from `COBALT_ENV=production` alone (`vault.py:159-160`), which the archiver plist already sets.
   777	   166	- Sides: the archiver still opens only system-side DB stores (ADR-0008 D2 row unchanged); it reads one vault FILE. The radar job's D2 row: `RadarStore`, `BarStore`, `JobStore` → system; `TraderSettingsStore` (mirror) → user.
   778	   167	- **Equality proof before delete:** `cobalt radar sources --archiver-diff --yaml-rev <sha>` prints `archive_targets` and `backfill_targets` from the note vs from `watchlists.yaml` at that git revision — must be empty. Fixture test in the suite; prod run in L8.
   779	   168	- **Stage 2 commit** = archiver switch + test re-target + `git rm configs/cobalt/watchlists.yaml`, last on the branch. Its rollback = `git revert <stage2>`. It is separate because the 20:30 archiver needs the note, and the note exists only after L6, which needs stage-1 code on main.
   780	   169	
   781	   170	### D12 — Smoke (dev vault + cobalt_dev) — sprint acceptance
   782	   171	
   783	   172	| # | Check | Pass |
   784	   173	|---|---|---|
   785	   174	| S0 | Recorded session: `COBALT_ENV=dev uv run archiver --backfill <T>` for every fixture ticker (F14) | ≥1 full trading day of i1 + i2 in cobalt_dev; the day is named in the report |
   786	   175	| S1 | `cobalt db migrate` on cobalt_dev; `--rollback --down-to 0003`; `migrate` | proof clean, radar tables CREATED, digests identical across the round-trip |
   787	   176	| S2 | Replay `cobalt radar scan --replay <day> --from 04:00 --to 16:00` over cached screener CSVs built from the corpus by `cobalt radar replay-build <day>` (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions present; replay-only, named as such) | pool churns: ≥1 enter and ≥1 leave |
   788	   177	| S3 | Cap | `max(open admitted members) ≤ radar.pool_cap` at every cycle (SQL over membership), including cycles with a degraded source |
   789	   178	| S4 | Entry on RVOL | a name whose proxy RVOL crosses the fixture screen's threshold at T has `entered_at ≤ T + scan_interval` |
   790	   179	| S5 | `excluded_by` | ≥1 row each of `config_cap`, `not_equity`, `screen_inactive`, `manual` |
   791	   180	| S6 | Window gate | no episode with `source` = the fixture screen entered before 10:00 ET; ≥1 after |
   792	   181	| S7 | market_reset | a cycle at 20:30 ET: row counts in pool, membership, bars, `trader_settings` unchanged; state `paused_market_reset`; no `SessionBlocked` in logs |
   793	   182	| S8 | Degraded | fixture source → HTTP 500: pool row degraded, members held, probe RED naming it; broken block → mirror `parse_failed`, probe RED naming it |
   794	   183	| S9 | Poller | member i1 bars upserted, closed bars only, watermark honoured; aggregate-vs-i2 agreement % reported |
   795	   184	| S10 | Probe | `radar` OK fresh / RED stale in session / OK idle out of session |
   796	   185	| S11 | Account mode + J1 | card stamped + badge rendered (`GET /` on a dev sheet); UNSET badge when day row NULL; J1 suite green |
   797	   186	| S12 | Whole system | `uv run pytest tests/cobalt tests/taxonomy` green; `uv run cobalt validate` exit 0; `cobalt jobs readers` for every changed config path; R2 grep clean |
   798	   187	| S13 | Stage 2 | archiver-diff empty on fixtures; `archiver --backfill` still works from the note |
   799	   188	
   800	   189	Sol runs the smoke against a worktree-local vault copy (`data/smoke-vault`, gitignored) because it cannot write `~/dev-vault-cobalt` (F15). The hub re-runs S1–S13 against `~/dev-vault-cobalt` + cobalt_dev as ground truth (L35).
   801	   190	
   802	   191	## §3 Houses and RESTARTS (R5)
   803	   192	
   804	   193	Build = `gpt-5.6-sol`, high effort, `-s workspace-write -c sandbox_workspace_write.network_access=true`, cannot commit. Hub = Sonnet: launch, wait, verify against ground truth, commit on branch. Gated vault write = hub, after approval.
   805	   194	
   806	   195	RESTARTS, derived by rule from the expected diff (Sol re-derives it from the real `git diff --name-status main...HEAD`):
   807	   196	
   808	   197	| Path (expected) | Rule | RESTART |
   809	   198	|---|---|---|
   810	   199	| `ops/com.cobalt.radar.plist` (A) | plist in diff | `com.cobalt.radar` — bootstrap (new) |
   811	   200	| `configs/cobalt/taxonomy/tunables.yaml` (M) | in a resident's `reads:` → `com.cobalt.aset` (`jobs.yaml:69`, `taxonomy/loader.py:79`) | `com.cobalt.aset` kickstart |
   812	   201	| `configs/cobalt/radar.yaml` (A) | only in radar's `reads:` | covered by the bootstrap |
   813	   202	| `configs/cobalt/jobs.yaml` (M, and again in L11) | registry | `cobalt jobs register` |
   814	   203	| `configs/cobalt/watchlists.yaml` (D, stage 2) | `cobalt jobs readers` → none (archiver is a one-shot) | none |
   815	   204	| `src/**` incl. `db_migrations/0004*.sql` | code | none (the migration is LIVE step L3, not a restart) |
   816	   205	| `tests/**`, `docs/**`, `ops/README.md` | tests/docs | none |
   817	   206	| anything else | unclassified | ESCALATE, never dropped |
   818	   207	
   819	   208	## §4 Build step 1 — Finviz throttle re-measure (FIRST)
   820	   209	
   821	   210	- `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`. Names = the 50 synthetic-fixture tickers. Refuses 09:00–16:00 ET on trading days (his live session) and inside market_reset.
   822	   211	- Per cycle: sequential `/export/stock?p=i1` for each name, then one screener call with the fixture filter. STOP at the first non-200, 429, redirect, non-CSV body or header mismatch.
   823	   212	- Per stage: requests, achieved req/min, statuses, p50/p95 latency, bytes → `data/radar-throttle-<ts>.json` + a printed table.
   824	   213	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`; the row's `consumers` cites the report. If the 10 s stage is clean, the report says "no throttle observed up to N req/min" (a floor, not a ceiling). Never extrapolate.
   825	   214	- Token resolution fails in the sandbox → NOT RUN with the scrubbed error line; the hub runs the same command. Offline steps continue. READY FOR MERGE requires the number.
   826	   215	
   827	   216	## §5 NOT in P1
   828	   217	
   829	   218	Precondition evaluator (F8), dots / ladder (F10), radar panel, F3 rank display, F12 missed replay, F13 auto-archive. Writing `pool_member_id`. `account_mode NOT NULL`. Hysteresis at the cap. The four-list re-export (E3).
   830	   219	
   831	   220	## §6 LIVE block — named steps, one rollback domain each
   832	   221	
   833	   222	Window: trading-day 16:15–19:40 ET or a weekend daytime. Never 09:00–16:00, 20:00–21:30, 21:25–21:55 (backup), or 23:27–23:47 (generated commit).
   834	   223	
   835	   224	| Step | Action | Proof | Rollback (domain) |
   836	   225	|---|---|---|---|
   837	   226	| L0 PRECONDITIONS | heartbeat fix merged + deployed + green; branch rebased; suite green on the rebased head; report READY FOR MERGE; `git tag pre-s2-p1` on main | report + tag | — |
   838	   227	| L1 SNAPSHOT | `uv run cobalt backup run` | restic id + dump printed | belt for DB + vault |
   839	   228	| L2 CODE stage 1 | hub rebases the branch onto current main (the nightly generated commit moves main), then `git -C ~/cobalt merge --ff-only <stage1-sha>`; `git tag s2-p1-stage1` | `git log -1` | reset to `pre-s2-p1` + RESTARTS again (code) |
   840	   229	| L3 DB | `uv run cobalt db migrate --allow-prod` | every existing table OK; radar tables CREATED | `cobalt db migrate --allow-prod --rollback --down-to 0003` (DB) |
   841	   230	| L4 REGISTRY | `uv run cobalt validate`; `uv run cobalt jobs register` | exit 0; radar row `enabled: false` | re-register at the previous tag |
   842	   231	| L5 RESTARTS stage 1 | `launchctl kickstart -k gui/$(id -u)/com.cobalt.aset` | `curl -s :5010/api/health` → `ok:true`; next beat `sheet daymode` OK | kickstart again after the code rollback |
   843	   232	| L6 VAULT (HITL) | hub, after approval: `COBALT_ENV=production uv run cobalt radar seed --dry-run` → diff sha256 == card's; then `--apply --hitl <token>` | 5 write_ids printed | `uv run cobalt vault restore --write-id <id>` ×5, or the L1 snapshot (vault) |
   844	   233	| L7 SOURCES | `uv run cobalt radar sources` | every block `ok`; Day Scan `active_from "10:00"`; list counts == YAML counts | — |
   845	   234	| L8 PROOF | `uv run cobalt radar sources --archiver-diff --yaml-rev HEAD` | empty diff | — |
   846	   235	| L9 CODE stage 2 | `git merge --ff-only sprint-2/radar-pool`; `git tag s2-p1`; `cobalt jobs readers configs/cobalt/watchlists.yaml` | readers: none | `git revert <stage2-sha>` (source switch) |
   847	   236	| L10 LAUNCHD | `cp ops/com.cobalt.radar.plist ~/Library/LaunchAgents/`; `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.radar.plist` | first cycle in `logs/radar.log`; `cobalt db query --prod --side system "select state, degraded, members, last_scan_at from radar_pool"` | `launchctl bootout gui/$(id -u)/com.cobalt.radar` (launchd) |
   848	   237	| L11 ENABLE | `jobs.yaml` `enabled: true` on main; `cobalt jobs register` | registry | flip back + register |
   849	   238	| L12 HEARTBEAT | next beat | GREEN, `radar` line present | — |
   850	   239	| L13 NEXT SESSION | 04:00+ `scanning`; Day Scan: no episode before 10:00, sources list it active after; 20:00–21:00 radar row counts constant, no RED; 20:30 archiver exit 0, target count == prior night | `cobalt db query` + logs | per domain above |
   851	   240	
   852	   241	## §7 Risks
   853	   242	
   854	   243	| Risk | Mitigation |
   855	   244	|---|---|
   856	   245	| Finviz lockout on his Elite login (probe or poller) during trading | probe refuses 09:00–16:00; stop-on-first-error ramp; 0.5 safety factor; single token bucket; startup budget refusal |
   857	   246	| Real screen data reaching the repo (reports, cache, fixtures) | cache under gitignored `data/`; reports name screens by key only, never `f=`; R2 grep + suite test |
   858	   247	| Rebase conflicts with the heartbeat fix | expected in `db_migrations/__init__.py`, `db_migrations/cli.py` (digest list), `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`, `test_jobs.py` — rebase first, never after |
   859	   248	| First resident + `self`: zombie path unexercised | watchdog test: stale heartbeat → `zombie`; plist unloaded → RED |
   860	   249	| i1 export ~9.4k rows × 50 names per poll = parse cost | watermark filter before model build; `last_scan_ms` on the pool row; smoke reports p95 cycle ms |
   861	   250	| Cap-boundary oscillation → episode churn | smoke reports episodes/day; hysteresis is E2's ruling |
   862	   251	| Cache growth (~7k CSVs per trading day) | retention in radar.yaml; smoke measures bytes/day |
   863	   252	| Finviz serves `p=i2` natively (DATA-SOURCE-MEMO A.2.1), so i1→2m aggregation may disagree with Finviz's own 2m bars | ruled i1→2m kept; the S9 agreement % against archived i2 decides; a systematic mismatch is ESCALATE, not a silent switch |
   864	   253	| A cycle straddling 20:00 ET | second session check before commit; dropped whole (D4) |
   865	   254	| Sol cannot reach cobalt_dev or has no DB env | the hub exports DB env from `~/cobalt/.env` at launch (never printed); DB tests Sol cannot run are reported NOT RUN, and the hub runs them |
   866	   255	
   867	   256	## §8 ESCALATE
   868	   257	
   869	   258	```
   870	   259	ESCALATE:
   871	   260	E1 ACCOUNT MODE SOURCE — no live/sim value exists anywhere (day_modes, trader_settings, configs).
   872	   261	   P1 adds nullable day_modes.account_mode + a CLI setter, stamps cards, shows a loud UNSET badge,
   873	   262	   never refuses a card. Rule: who sets it and when (sheet day-mode step?), and must an UNSET card be refused.
   874	   263	E2 POOL RANK AT THE CAP — today's static tiers alone (~260 names) exceed pool_cap 50 five-fold, so the
   875	   264	   rank rule chooses the pool every minute. P1 default: screen names first (hits, screen position), then
   876	   265	   list names by RVOL, ticker tie-break, no hysteresis. Selection logic: rule it or replace it.
   877	   266	E3 FOUR LISTS NOT RECOVERABLE — watchlists.yaml holds 3 derived tiers, not Green/Red/SMB Daily Watch/
   878	   267	   Watchlist. P1 migrates the tiers verbatim (source = list:tier_a…). Re-export the four lists into the
   879	   268	   Lists note if membership must name them.
   880	   269	E4 ft=4 DROPPED BY THE R1 KEY LIST — 3 of 4 pasted URLs carry it; meaning unverified. The card shows
   881	   270	   ticker sets with vs without ft=4 per screen; any difference needs an `ft` key added to R1's contract.
   882	   271	E5 USER DATA IN AN UNCOMMITTED REPORT — docs/40 - DevDocs/reports/day-open-2026-09-10.md §2 C.1 quotes
   883	   272	   all four screens' full f= strings and columns; it commits at day close → L32 breach. Redact first.
   884	   273	E6 R5 RULE GAP — "code → none" leaves a resident on stale code whenever no reads: file changes (here the
   885	   274	   sheet's account-mode stamp/badge). P1 is covered only because tunables.yaml restarts the sheet anyway.
   886	   275	   Rule: does a code change under a resident's import tree restart it.
   887	   276	```
   888	   277	
   889	   278	## §9 DISSENT
   890	   279	
   891	   280	No review round completed, so there are no reviewer objections to adopt or decline.
   892	   281	
   893	   282	- **Round 1 FAILED:** `codex exec -m gpt-6-astra` hit "You've hit your usage limit … try again at 11:31 AM" after 72,175 tokens. The model read the plan, ADR-0008, DATA-SOURCE-MEMO, `db_migrations/`, `jobs/wrapper.py`, `jobs/watchdog.py` and `daymode/store.py`, then stopped without issuing any BLOCKER, RISK or VERDICT. Capture: `plan-s2-p1-astra-r1.md`.
   894	   283	- Its last progress message named three boundaries it was about to check: disabled-job startup, scans crossing market_reset, held members vs the pool cap. The architect checked them without the reviewer. The last two were real gaps and are fixed in D4 and D12 S3. The first holds: `job_run` does not read `enabled` (`wrapper.py:122-162`).
   895	   284	- **Rounds 2–3:** not run. Codex has one shared five-hour pool (`limit_id codex`, day-open §1.4), the same pool Sol builds on. The hub should run the review command (same prompt, same capture path pattern) after the reset and BEFORE launching Sol. Objections left after round 3 are added here, one line each.
   896	   285	
   897	   286	=== RULINGS ADDENDUM 2026-09-10 (Dejan) ===
   898	   287	E1 Account mode: standing value `live` in "user".trader_settings; a per-day `sim` switch on the morning sheet-attestation control (same control that attests the .htk sheet, one extra tap) writes day_modes.account_mode for that day only; every card is stamped from day override → standing value; a card with no value is REFUSED, loud — never stamped UNSET and let through.
   899	   288	E2 Pool rule — lives in the vault note beside the screens (user data, L32), read by the collector like the screen blocks:
   900	   289	```yaml
   901	   290	pool:
   902	   291	  cap: 50
   903	   292	  priority: [screens, lists]
   904	   293	  rank_metric:
   905	   294	    premarket: volume        # 04:00–09:30 via the F1 session clock
   906	   295	    rth: rvol                # 09:30 onward
   907	   296	  overrides:
   908	   297	    morning_low_float: volume      # this screen ranks by volume in every session
   909	   298	    day_scan_after: "10:00"        # Day Scan takes first priority among screens after 10:00
   910	   299	  stickiness_scans: 3              # out of the top 50 for 3 consecutive scans before dropping
   911	   300	```
   912	   301	Names not admitted get a membership row with `excluded_by = config_cap`.
   913	   302	E3 Static lists: move the three merged tiers as they are; membership `source` names the tier. Named-list attribution comes later, if he re-exports the four TV lists into the vault.
   914	   303	E4 `ft=4`: the HITL card shows each screen's ticker set with and without `ft=4`; any difference → `ft` joins the block contract; no difference → dropped.
   915	   304	E5 User data in reports: before ANY commit, replace the four screens' `f=` strings in every report, plan and review file with "see vault note"; add a repo-wide grep for those strings to the report's checklist.
   916	   305	E6 RESTARTS rule: plist in diff → that job; changed file in a resident's `reads:` → that resident; any src/ change → every resident whose entrypoint imports the changed module (static import walk in the report); unproven → all residents; unclassified path → ESCALATE, never dropped.
   917	   306	E7 Credentials: NO DB credentials in Sol's environment or the worktree during the build. Sol runs everything that needs no DB; the hub runs the DB-backed suite, migrations on cobalt_dev, and the dev-vault smoke.
   918	   307	E8 The R1 vault write (four YAML blocks + pool block into `1 - Trading/Radar Screens.md`) is NOT part of the build: Sol writes the parser, the synthetic fixture and a `cobalt radar screens propose` command that prints the proposed blocks + the ft=4 comparison. The hub runs the proposal at LIVE time; Dejan approves the HITL card; only then does the writer write.
   919	   308	=== END ADDENDUM ===
   920	     1	# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`
   921	     2	
   922	     3	You build S2-P1 (radar pool + Finviz bar poller) in this worktree. Everything you need is in this
   923	     4	file. The plan it implements is `docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md`,
   924	     5	in this worktree. Where the two disagree, the plan wins; say so in the report.
   925	     6	
   926	     7	## 0. Who does what
   927	     8	
   928	     9	| House | Does | Cannot |
   929	    10	|---|---|---|
   930	    11	| **You (Sol)**, high effort, `-s workspace-write`, network on | write code, tests, docs, the report, inside this worktree | commit, rebase, write outside the worktree, touch the real vault or `cobalt_brain` |
   931	    12	| **Hub (Sonnet)** | launches you, verifies against ground truth, commits per step on `sprint-2/radar-pool`, runs what your sandbox cannot | build |
   932	    13	| **Dejan** | approves the HITL card | — |
   933	    14	
   934	    15	**Hub, before launching you:** (1) if `ops/heartbeat-market-reset` has merged to main, rebase this
   935	    16	branch onto main first; (2) if the plan's §9 says the Astra review loop has not run, run it and fold
   936	    17	fixes into the plan before launch; (3) export the dev DB credentials into your environment without
   937	    18	printing them.
   938	    19	
   939	    20	**Two runs.** RUN A = steps 0–13 (stage 1). Stop, print `DONE`. The hub commits stage 1, then
   940	    21	relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
   941	    22	Step G is **hub only, after Dejan's approval** — you never run it.
   942	    23	
   943	    24	**Stop rules.** A step you cannot finish → mark it `NOT RUN` or `FAILED` in the report with the
   944	    25	exact error line (scrubbed), then continue with the steps that do not depend on it. Never mark a
   945	    26	test passing that did not run. 3 failed attempts at the same thing → stop that step, ESCALATE.
   946	    27	Print `DONE` as the very last line of every run, nothing after it.
   947	    28	
   948	    29	## 1. Laws (binding — a violation is a failed step)
   949	    30	
   950	    31	1. **Production is sacred (NN#16).** Dev only: `COBALT_ENV=dev`, database `cobalt_dev`, vault =
   951	    32	   `data/smoke-vault` (gitignored copy you make of `~/dev-vault-cobalt`). Never open
   952	    33	   `/Users/cobalt/Vault/Think`. Never connect to `cobalt_brain`. Never `launchctl` anything.
   953	    34	2. **User data never enters the repo (L32).** No real screen, filter string, list or dollar figure in
   954	    35	   any tracked file, report, fixture, test or log line you paste. The repo ships exactly ONE synthetic
   955	    36	   example screen (R2).
   956	    37	3. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error
   957	    38	   string passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
   958	    39	4. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent
   959	    40	   fallback, no plausible-empty artifact, no default invented for a missing value.
   960	    41	5. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
   961	    42	   `archiver.collector.fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
   962	    43	   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
   963	    44	   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`.
   964	    45	6. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted
   965	    46	   (`psycopg.sql.Identifier` in Python); cross-side SQL is schema-qualified (`system.radar_membership`);
   966	    47	   every new table is on a side in `src/cobalt/db_migrations/placement.py` or the suite fails.
   967	    48	7. **Config-as-code.** Pydantic schema per config file, `extra="forbid"`, dry-run command. New-core
   968	    49	   config lives only under `configs/cobalt/` (never `configs/*.yaml` top level).
   969	    50	8. **Tunables.** Thresholds are `configs/cobalt/taxonomy/tunables.yaml` rows. Use EXISTING
   970	    51	   `TunableUnit` / `TunableStatus` / `TunableSource` values only — adding an enum value breaks the
   971	    52	   live ASET sheet (09-09 outage). No fitting value → ESCALATE.
   972	    53	9. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE writing; never rely on catching
   973	    54	   `SessionBlocked`. Radar writes nothing in that window.
   974	    55	10. **Tools fetch, code computes.** No LLM anywhere in P1. All numbers are deterministic code.
   975	    56	11. **Tests per step.** `uv run pytest` for the step's tests before moving on; the whole suite at
   976	    57	    step 13.
   977	    58	12. **Names.** One name per concept across SQL, Python, config and docs (`radar_pool`,
   978	    59	    `radar_membership`, `account_mode`, `pool_member_id`, `excluded_by`).
   979	    60	
   980	    61	## 2. Rulings you implement (09-10, binding)
   981	    62	
   982	    63	- **R1 Radar Screens contract.** Vault note `1 - Trading/Radar Screens.md` gets one fenced YAML block
   983	    64	  per screen: `screen, f, sort, columns, active_from, active_to (session clock, ET), enabled`. It is
   984	    65	  written ONCE, through the vault writer, under ONE HITL card, prose untouched. After that Cobalt only
   985	    66	  reads the note: parse fenced blocks only, reload on file-hash change, mirror each block + hash into
   986	    67	  `"user".trader_settings`; `radar_membership.source` names screen + hash. Parse failure → pool row
   987	    68	  degraded + heartbeat `radar` probe RED naming the screen; never the previous version silently. Day
   988	    69	  Scan is active from 10:00 ET via the F1 session clock — a field, never code.
   989	    70	- **R2 Synthetic example screen.** Exactly one, same fenced format, as the test fixture under
   990	    71	  `tests/fixtures/`; real screens never enter the repo. `git ls-files | grep -i radar` stays clean of
   991	    72	  user data.
   992	    73	- **R3 `cobalt db query`.** Read-only CLI: factory connection, SET ROLE per side, SELECT-only enforced in
   993	    74	  code (reject anything else, loud), output JSON/table. The workers' DB read path.
   994	    75	- **R4 Static lists are user data.** They move user-side by the same mechanism as R1. Plan choice: a new
   995	    76	  vault note `1 - Trading/Radar Lists.md` with fenced blocks. The archiver keeps working through the
   996	    77	  migration (stage 2).
   997	    78	- **R5 Houses + RESTARTS by rule.** plist in diff → that job; changed file in a resident's `reads:` →
   998	    79	  that resident; registry → `register`; code/tests/docs → none; anything unclassified → ESCALATE.
   999	    80	
  1000	    81	## 3. Environment
  1001	    82	
  1002	    83	- Run everything from this worktree with `uv run …`. Tests: `uv run pytest tests/cobalt tests/taxonomy`.
  1003	    84	- DB env: the hub exports the Postgres credentials into your environment at launch. If a DB-backed test
  1004	    85	  or command fails to connect, record `NOT RUN (db unreachable: <scrubbed error>)` and continue.
  1005	    86	- No `psql` on this host. Before step 3 lands, reach the DB only through repo code; after it lands, use
  1006	    87	  `uv run cobalt db query --side system|user "<select>"`.
  1007	    88	- Finviz token: `cobalt.archiver.collector.resolve_token()`. If it fails in your sandbox, the live half
  1008	    89	  of step 1 is `NOT RUN`; the hub runs it.
  1009	    90	- Vault for smoke: `cp -R ~/dev-vault-cobalt data/smoke-vault` once, then
  1010	    91	  `COBALT_VAULT_PATH=$PWD/data/smoke-vault`. `data/` and `logs/` are gitignored — confirm with
  1011	    92	  `git check-ignore` before writing anything there.
  1012	    93	- DevDocs layout: one page per `.py` file at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
  1013	    94	  `docs/40 - DevDocs/tests/cobalt/<file>.md`, and a line in `docs/40 - DevDocs/INDEX.md`.
  1014	    95	
  1015	    96	## 4. Build steps
  1016	    97	
  1017	    98	Each step lists its files, then the tests that must pass before the next step starts.
  1018	    99	
  1019	   100	### Step 0 — Base check (no code)
  1020	   101	- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql`. Present → the heartbeat fix is in
  1021	   102	  your base; build on it. Absent → build on main as is, register 0004 after 0002, and list in the report
  1022	   103	  the files that will conflict at merge: `db_migrations/__init__.py`, `db_migrations/cli.py`,
  1023	   104	  `heartbeat/runner.py`, `jobs/config.py`, `jobs/wrapper.py`, `tests/cobalt/test_tenancy.py`,
  1024	   105	  `tests/cobalt/test_jobs.py`.
  1025	   106	- Record `git rev-parse HEAD` in the report.
  1026	   107	
  1027	   108	### Step 1 — Finviz throttle re-measure (FIRST)
  1028	   109	- `src/cobalt/radar/throttle.py` + `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`.
  1029	   110	- Names = the 50 first tickers of the synthetic lists fixture (step 5 creates it; create that fixture
  1030	   111	  file now if needed).
  1031	   112	- Refuses on trading days between 09:00 and 16:00 ET, and inside market_reset (use `session_clock()` and
  1032	   113	  the NYSE calendar).
  1033	   114	- Per cycle: sequential `fetch_bars(t, Interval.I1, token)` for each name, then one
  1034	   115	  `/export/screener?v=152&f=<fixture f>&c=0,…,150` call. STOP at the first non-200, 429, redirect,
  1035	   116	  non-CSV body or header mismatch.
  1036	   117	- Per stage record: requests, achieved req/min, status counts, p50/p95 latency ms, bytes. Write
  1037	   118	  `data/radar-throttle-<UTC ts>.json` and print a table.
  1038	   119	- `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`. If every stage was clean, write
  1039	   120	  "no throttle observed up to N req/min". Never extrapolate.
  1040	   121	- **Tests (mocked HTTP):** stop-on-first-error per class; refusal inside the forbidden window; rpm math;
  1041	   122	  token never appears in output (assert `auth=REDACTED`).
  1042	   123	- **Live run:** allowed only outside the forbidden window. Otherwise, or on token failure, `NOT RUN`.
  1043	   124	
  1044	   125	### Step 2 — Migration 0004, rollback bound, placement, J1
  1045	   126	- `src/cobalt/db_migrations/0004_radar_pool.sql` and `0004_radar_pool.rollback.sql` with exactly the
  1046	   127	  plan's §D3 DDL. Tables are created schema-qualified, `OWNER TO cobalt_system`;
  1047	   128	  `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`;
  1048	   129	  `GRANT SELECT ON system.radar_pool TO cobalt_user`. The rollback header states its cost.
  1049	   130	- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring lines.
  1050	   131	- `db_migrations/cli.py`: the digest excludes `account_mode` and `pool_member_id` (extend the heartbeat
  1051	   132	  fix's `DIGEST_EXCLUDED_COLUMNS` if present; otherwise generalize `TENANCY_COLUMN` into that tuple).
  1052	   133	  `--rollback` REQUIRES `--down-to NNNN`; it reverses only registered migrations newer than NNNN, newest
  1053	   134	  first; without it, it refuses and lists targets.
  1054	   135	- `placement.py`: move `radar_pool`, `radar_membership` out of `DECLARED_TABLES` into a new
  1055	   136	  `CREATED_TABLES` dict ("created by a db_migration directly on its side"), included in `PLACEMENT` and
  1056	   137	  in the proof table; extend the SQL/Python agreement test to 0004.
  1057	   138	- **Tests** (`tests/cobalt/test_tenancy.py`, `tests/cobalt/test_radar_migration.py`):
  1058	   139	  migrate twice idempotent; `migrate → --rollback --down-to 0003 → migrate` digests identical;
  1059	   140	  0003's columns (if present) survive the 0004 rollback; `--rollback` without `--down-to` refuses;
  1060	   141	  placement test green; J1 — FK catalog proof, `cobalt_user` SELECT OK / INSERT denied on
  1061	   142	  `system.radar_membership`, valid id insert OK / invalid FK-fails, `cobalt_system` SELECT on
  1062	   143	  `"user".aset_sizings` denied; membership CHECKs (`entered_at IS NOT NULL OR excluded_by IS NOT NULL`)
  1063	   144	  and the partial unique index reject bad rows.
  1064	   145	
  1065	
  1066	exec
  1067	/bin/zsh -lc "nl -ba 'docs/10 - Decisions/ADR-0008-two-layer-data-model.md' | head -190; nl -ba 'docs/30 - Design/DATA-SOURCE-MEMO.md' | head -190; nl -ba src/cobalt/archiver/collector.py | sed -n '1,300p'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
  1068	 succeeded in 0ms:
  1069	     1	# ADR-0008 — Two-layer data model: user data vs system data
  1070	     2	
  1071	     3	Date: 2026-09-08
  1072	     4	Status: Accepted (architect spike, Fable 5.1; rulings 0, a–g decided-with-veto by
  1073	     5	Dejan 09-08, one per message; implemented by an Opus 5 lead-developer session on
  1074	     6	`sprint-2/data-model`)
  1075	     7	Implements: **L32** (user-data / system-data law, 09-05; tenancy R2 09-06) and
  1076	     8	**L31** (names rule, 09-06). Relates to: ADR-0001 (trade_defs as data — superseded
  1077	     9	in part: the repo no longer carries populated defs), ADR-0004 (L28, the one vault
  1078	    10	write path — reused unchanged, frontmatter site included), ADR-0005/0006 (RULING 7
  1079	    11	environment law and the one connection factory — extended, not replaced).
  1080	    12	Gates: SPRINT-LADDER S2-P1 line 0.
  1081	    13	
  1082	    14	## Context
  1083	    15	
  1084	    16	Cobalt-the-system is only the schema and engine that make any trader's strategies
  1085	    17	pluggable: taxonomy anatomy (regime, range, gap, extension, leg, session clock), the
  1086	    18	card engine, the radar, alerts, the rules-engine schema. Everything named after a
  1087	    19	trade, everything SMB- or cheat-sheet-derived, every setting that is one trader's
  1088	    20	choice, and every note in `1 - Trading` is user data — never shipped to or visible
  1089	    21	to another Cobalt user (L32).
  1090	    22	
  1091	    23	On 2026-09-08 the code did not know the difference:
  1092	    24	
  1093	    25	- Every new-core table sat in `public` of `cobalt_brain` beside 17 old-tree tables
  1094	    26	  (`memory_logs`, `graph_nodes`, `graph_edges`, `hitl_proposals`,
  1095	    27	  `browser_fast_path`, `instruments`, `market_snapshots`, `daily_in_play`,
  1096	    28	  `key_levels`, `news_events`, `news_mentions`, `order_fills`, `strategy_signals`,
  1097	    29	  `system_alerts`, `themes`, `trades`, `trading_accounts`). One login role,
  1098	    30	  `cobalt`, the docker superuser, owned all of it. `search_path` was
  1099	    31	  `"$user", public`.
  1100	    32	- The 13 populated trade_defs were committed YAML under
  1101	    33	  `configs/cobalt/taxonomy/trade_defs/`, cross-checked against
  1102	    34	  `cameron_grid.yaml` (a person's name in a config key, L31) and
  1103	    35	  `variables/<id>.yaml`. The same 13 defs existed a second time, verbatim, inside
  1104	    36	  the 22 strategy notes written on 09-06 (`1 - Trading/4 - Strategies/<note>.md`,
  1105	    37	  `cobalt:section definition` units) — a one-path violation waiting for the first
  1106	    38	  edit to either copy.
  1107	    39	- The vault key (`trade_def:` frontmatter, kebab: `big-dog`, `nine-ema-scalp`) and
  1108	    40	  the YAML key (`id:`, snake: `big_dog`, `ema9_scalp`) were not inter-derivable
  1109	    41	  for 3 of 13, and nothing in the repo owned the map.
  1110	    42	- 69 trade notes in `1 - Trading/2 - Trades/` carried `strategy:` as free text
  1111	    43	  (33 blank; aliases like `Big Dawg`, `Offside Scalp`, `Fashionable Late Scalp`;
  1112	    44	  leading spaces and doubled quotes from Templater) and none carried `trade_def:`,
  1113	    45	  so every `## Instances` dataview rendered empty.
  1114	    46	- The trader's own dollar sheet, enabled grades, reduced mode, `.htk` template and
  1115	    47	  step-downs lived in committed config (`configs/cobalt/aset.yaml`,
  1116	    48	  `daymode.yaml`).
  1117	    49	- The 09-06 strategy-note batch was hand-work with no L28 record; its ledger line
  1118	    50	  cited a restic snapshot ("09-05 21:40") that does not exist.
  1119	    51	
  1120	    52	Facts verified read-only during the spike, and binding on the design:
  1121	    53	
  1122	    54	- `user` is a **reserved word** in PostgreSQL 16 (`pg_get_keywords` catcode R);
  1123	    55	  `system` is unreserved.
  1124	    56	- `cobalt` is `rolsuper = true`; superusers bypass every grant regardless of
  1125	    57	  `INHERIT`.
  1126	    58	- `pg_read_all_data` exists (PG14+).
  1127	    59	- `VaultWriter.upsert_region` (ADR-0004) already is the marker-less frontmatter
  1128	    60	  write site: 3-way merge, write_id, restore. A first write on a unit with no
  1129	    61	  baseline takes Cobalt's body wholesale (base := human) — exactly right for
  1130	    62	  migrating Cobalt-seeded units.
  1131	    63	- The `cfg()` key grammar (§13.1) and `per_trade(<id>)` scope accept `[a-z0-9_]`
  1132	    64	  only: a kebab slug cannot appear verbatim in a tunable key, and would read as
  1133	    65	  subtraction to a future predicate parser.
  1134	    66	- The SSD restic repo holds three snapshots: `24f3f36b` 2026-09-06 08:30:23,
  1135	    67	  `472ade44` 09-06 21:40:08, `0d55d7b5` 09-07 21:40:03. The 09-06 batch began
  1136	    68	  09:21 → its pre-state is `24f3f36b`.
  1137	    69	
  1138	    70	## Decision
  1139	    71	
  1140	    72	### D1 — Tenancy A: one database, two schemas, per-store sides (RULED L32 R2; item 0)
  1141	    73	
  1142	    74	- One database `cobalt_brain` (dev twin `cobalt_dev`). Two schemas: **`system`**
  1143	    75	  and **`"user"`**. The user-side schema keeps the name `user` (ruled 09-08:
  1144	    76	  "user will have more roles and more user settings outside of being trader
  1145	    77	  only") and is therefore **always quoted** — in every migration, grant,
  1146	    78	  `search_path`, hand query and Python (`psycopg.sql.Identifier`). A suite lint
  1147	    79	  test fails on any unquoted `user.` reference under `src/cobalt`. The word
  1148	    80	  "trader" survives only inside table/field names (`trader_settings`, `traders`,
  1149	    81	  `trader_id`, `trade_key`).
  1150	    82	- Two `NOLOGIN` roles: **`cobalt_user`** (ALL on `"user"`, SELECT on `system`) and
  1151	    83	  **`cobalt_system`** (ALL on `system`, **nothing** on `"user"` — system never reads
  1152	    84	  user data). Each schema and every new-core table is **owned** by its side role
  1153	    85	  (`ALTER … OWNER TO`): ownership is not a grant and would otherwise leak every
  1154	    86	  privilege back to the login role. A third `NOLOGIN` role **`cobalt_backup`** is
  1155	    87	  a member of `pg_read_all_data` for `pg_dump --role=cobalt_backup`.
  1156	    88	- **The side is chosen per store, never per process.** Every store declares
  1157	    89	  `SIDE = Side.USER | Side.SYSTEM` and opens its connections through the one
  1158	    90	  factory, `cobalt.db.connect(dbname, side=…)`, which does
  1159	    91	  `SET ROLE <side role>; SET search_path = <own schema only>` (no `public`). A job
  1160	    92	  that touches both sides holds one connection per side; there is no "both" role.
  1161	    93	  Cross-side references are written **schema-qualified** (`system.bars`), never
  1162	    94	  resolved through `search_path`. A wrong-side statement fails loud twice over:
  1163	    95	  relation-not-found (search_path) or permission denied (grants).
  1164	    96	- **`user_id`.** `"user".traders(id, handle, created_at)`, seeded `id = 1,
  1165	    97	  handle = 'primary'` (no name). Every user-side table carries
  1166	    98	  `user_id INTEGER NOT NULL REFERENCES "user".traders(id)` with
  1167	    99	  `DEFAULT current_setting('cobalt.trader_id')::int`. The factory sets the GUC
  1168	   100	  from `configs/cobalt/tenant.yaml` (`trader_id: 1` — which local trader this
  1169	   101	  install serves; committed; a product install ships it as 1). A connection that
  1170	   102	  did not pass through the factory has no GUC and every INSERT fails loud; no
  1171	   103	  literal default anywhere. Existing rows are backfilled to 1 in the same
  1172	   104	  migration.
  1173	   105	- **`public` is untouched** for the 17 old-tree tables (strangler rule). The
  1174	   106	  placement test carries that list frozen: a NEW table landing in `public`, or any
  1175	   107	  table not on exactly one side of the placement map, fails the suite.
  1176	   108	- **Superuser login — weighed, split (Revision 2).** `NOINHERIT` on `cobalt` buys
  1177	   109	  nothing while it is the superuser; after the factory's `SET ROLE` the session's
  1178	   110	  current role is a non-superuser and the grants bite, so per-store enforcement is
  1179	   111	  real. The only closure for "a connection that skips the factory" is a
  1180	   112	  non-superuser app login. Target state, ruled here; implementation split:
  1181	   113	  - this sprint: ownership to side roles, `cobalt_backup`, and a suite test that no
  1182	   114	    `psycopg.connect` exists under `src/cobalt` outside `db.py`;
  1183	   115	  - next ops prompt (owed): `cobalt_app` LOGIN NOINHERIT with its own credential in
  1184	   116	    VaultManager/.env, member of `cobalt_user`, `cobalt_system`, `cobalt_backup`;
  1185	   117	    factory and `pgdump.py` connect as it; superuser `cobalt` reserved for
  1186	   118	    `db migrate --allow-prod` and docker; every production plist restarted in the
  1187	   119	    same action (L28 restart-on-deploy). No credential change rides inside a
  1188	   120	    data-model migration — two rollback domains would become three.
  1189	   121	
  1190	   122	### D2 — Placement (RULED item 2; `cobalt_email_sends` revised under g)
  1191	   123	
  1192	   124	| table | side | note |
  1193	   125	|---|---|---|
  1194	   126	| `aset_sizings` (cards), `card_transitions`, `card_stop_edits` | user | + `user_id`; S2 adds `account_mode`, `pool_member_id → system.radar_membership(id)` |
  1195	   127	| `day_modes` | user | + `user_id` |
  1196	   128	| `vault_writes`, `vault_overrides` | user | + `user_id` (note text is user data) |
  1197	   129	| `trade_defs`, `tunables` (per-trade rows), `trader_settings`, `traders` — NEW | user | loaded copies of vault units / seeded settings |
  1198	   130	| `setup_trade_matrix` | user | a VIEW `(trade_def, setup_ref, relation)` unnested from `trade_defs` |
  1199	   131	| legs/fills, missed, DRC rows, prediction records | user | S2-P4 / S3 — declared now so the placement test names them |
  1200	   132	| `bars` | system | 4.84M rows; `SET SCHEMA` is catalog-only |
  1201	   133	| `radar_pool`, `radar_membership` (S2-P1) | system | |
  1202	   134	| `cobalt_jobs`, `cobalt_kill_switch`, `cobalt_redactions`, `session_blocks` | system | |
  1203	   135	| `cobalt_email_sends` | **system** | revised 09-08: channel log (`ts, ok, caller, message_id, detail`), no personal data — same class as `cobalt_redactions` |
  1204	   136	| taxonomy anatomy instances (S2-P2) | system | |
  1205	   137	| 17 old-tree tables | public | frozen allowlist, untouched |
  1206	   138	
  1207	   139	Per launchd job, which side each of its stores connects as:
  1208	   140	
  1209	   141	| job | stores → side |
  1210	   142	|---|---|
  1211	   143	| `com.cobalt.aset` | AsetStore, CardStore, DayModeStore, VaultWriteStore → user; SessionBlockStore → system |
  1212	   144	| `prefill-daily` / `prefill-drc` | AsetStore, DayModeStore, VaultWriteStore → user; SessionBlockStore, JobStore → system |
  1213	   145	| `cards-expire` · `daymode-propose` | CardStore / DayModeStore (+ VaultWriteStore) → user; JobStore → system |
  1214	   146	| `archiver` | BarStore, JobStore → system only |
  1215	   147	| `heartbeat` | JobStore, kill switch, SessionBlockStore, RedactionStore, EmailSendStore → system; VaultWriteStore (daily-note red/green block) → user |
  1216	   148	| `cobalt notify email-test` | EmailSendStore, RedactionStore → system |
  1217	   149	| `backup` | `pg_dump` as the login role (`--role=cobalt_backup` once D1's ops prompt lands), both schemas, no store |
  1218	   150	| `agent` (old tree) | `public` only, untouched · `mainframe`, `obsidian`: no DB |
  1219	   151	
  1220	   152	Tunables split: engine rows stay in `configs/cobalt/taxonomy/tunables.yaml`
  1221	   153	(system); trader rows (every `per_trade(...)` row) become user data (D3.3);
  1222	   154	trader-level settings become `"user".trader_settings` (D3.4).
  1223	   155	
  1224	   156	### D3 — The vault note is the trade_def's truth (RULED item 3; a, b, d, e)
  1225	   157	
  1226	   158	- **Source of truth** = the `cobalt:unit trade_def:<slug>` inside
  1227	   159	  `<!-- cobalt:section definition -->` of `1 - Trading/4 - Strategies/<note>.md`,
  1228	   160	  read through `cobalt.vault.resolve_vault_path()`. The DB row
  1229	   161	  (`"user".trade_defs`: `slug` PK, `def` jsonb, `md5`, `note_path`, `loaded_at`,
  1230	   162	  `user_id`) is a loaded, validated copy. One path: vault unit → loader →
  1231	   163	  `"user".trade_defs`.
  1232	   164	- **Key (a).** The frontmatter `trade_def:` slug — lowercase kebab, no `$`, no
  1233	   165	  leading digit — **is the id**. `id:` is removed from the YAML unit; the loader
  1234	   166	  injects `id = slug`; a unit that still carries `id:` fails loud ("id comes from
  1235	   167	  frontmatter `trade_def:`"). Grammar-safe spelling for `cfg()` keys and
  1236	   168	  `per_trade()` scope is ONE helper, `trade_key(slug) = slug.replace('-', '_')`.
  1237	   169	  Consequence: `ema9_scalp.*` tunable rows re-key to `nine_ema_scalp.*`; every
  1238	   170	  other key already equals `trade_key(slug)`. Schema: "v0.4 minus authored `id`
  1239	   171	  and `name`, plus structured `quality_factors[]`" — recorded here, folded into the
  1240	   172	  taxonomy at S2-P2's v0.8 bump.
  1241	   173	- **Display name (e).** `TradeDef.name` = frontmatter `name:` (loader-injected
  1242	   174	  like `id`); `name:` is removed from the unit; where the YAML's former name
  1243	   175	  differed it joins `aliases[]` (Back$ide Scalp, Rubber Band Scalp, Big Dog
  1244	   176	  Consolidation, Gap, Give and Go, Hitchhiker Scalp, Fashionably Late Scalp,
  1245	   177	  Back-Through Open).
  1246	   178	- **Loader.** Parses frontmatter with the existing `_FRONTMATTER_RE` pattern
  1247	   179	  (no new dependency), finds the `definition` section and its units with
  1248	   180	  `vaultwrite.markers`, loads the fenced YAML, injects id/name, validates
  1249	   181	  `TradeDef`, fails loud on any populated unit that does not validate. A unit
  1250	   182	  whose body is empty or holds only a partial mapping (see the matrix below) is a
  1251	   183	  **draft**: skipped with a listed warning, never an error. Frontmatter `status:`
  1252	   184	  is checked, not trusted: `defined` iff the unit validated, `draft` otherwise;
  1253	   185	  `playbook` is never typed (earned at n ≥ 30, R3). Frontmatter `class:` /
  1254	   186	  `family:` (d) are checked against the unit and any drift is listed; the human
  1255	   187	  wins; `cobalt taxonomy sync-frontmatter` re-aligns with a diff.
  1256	   188	  `python -m cobalt.taxonomy.validate` reads the vault.
  1257	   189	- **The three former cross-checks (b).**
  1258	   190	  1. `cameron_grid.yaml` → dies. The def's own `valid_setups[]` is the truth. The
  1259	     1	# Data-Source Spike, Phase A — Finviz Elite Export API
  1260	     2	
  1261	     3	**Method:** empirical probing only. There is no official Finviz API
  1262	     4	documentation; the 9 screenshots in `docs/90 - References/` (Finviz's
  1263	     5	own in-app "Automating Export" panels) were the starting point, not the
  1264	     6	spec — several details below were discovered by direct HTTP requests
  1265	     7	that contradict or extend what the screenshots show. Every finding is
  1266	     8	tagged **CONFIRMED** (fetched, evidence attached) or **INFERRED**
  1267	     9	(pattern/plausible, not independently verified) — the latter is Phase
  1268	    10	B's job to close (Dejan capturing the Finviz web pages, including the
  1269	    11	collapsed "Learn More" parameter panels the screenshots don't show).
  1270	    12	
  1271	    13	**Constraints honored:** read-only GETs only; ~1.2s between requests
  1272	    14	(≈50 requests total across two probe runs); auth token resolved via
  1273	    15	the existing vault-backed `FinvizApiClient` and never printed or logged
  1274	    16	— every URL and error string below is scrubbed. No FMP, no
  1275	    17	TradingView, no pipeline/old-tree code changes.
  1276	    18	
  1277	    19	**Probed:** 2026-08-27, against a live Finviz Elite Elite-tier account,
  1278	    20	ticker MSFT as the reference instrument for `/export/stock`.
  1279	    21	
  1280	    22	---
  1281	    23	
  1282	    24	## 0. Confirmed baseline from the old tree (`FinvizApiClient` + friends)
  1283	    25	
  1284	    26	Read: `src/cobalt_agent/skills/research/finviz_api.py` (the HTTP client —
  1285	    27	KEEP-AS-IS per TRIAGE, "grows"), `finviz_extractor.py` (Playwright
  1286	    28	scraper, TRIAGE-KILLed, browser-only info, not API-relevant),
  1287	    29	`enrich_metadata.py` (a live caller), and the `dev_utils/live_run_finviz*`
  1288	    30	scripts (thin wrappers, no new information).
  1289	    31	
  1290	    32	**What the client already gets right (CONFIRMED against my own probing):**
  1291	    33	- Base URL `https://elite.finviz.com`, token appended as `&auth=<token>`.
  1292	    34	  Matches every screenshot exactly.
  1293	    35	- `export.ashx?v=…&f=<filters>&c=<col indices>` for screener — the
  1294	    36	  `.ashx` path still works but 301-redirects to `/export/screener` (the
  1295	    37	  screenshots say this explicitly; I didn't re-verify the redirect
  1296	    38	  itself since old-tree code is out of scope to touch, but the
  1297	    39	  destination path is confirmed reachable directly).
  1298	    40	- `f=` filter syntax (`key_value` comma-joined, e.g.
  1299	    41	  `sh_price_o1,sh_avgvol_o5000`) — CONFIRMED, used throughout my probes.
  1300	    42	- `c=` column-index selection — CONFIRMED exactly: requesting
  1301	    43	  `c=0,1,2,3,4,5,6` returned precisely those 7 columns in that order.
  1302	    44	- `MASTER_COLUMNS` (indices `0`–`150`, 151 total) — CONFIRMED: a single
  1303	    45	  `c=0..150` request returned exactly 151 named columns (full list in
  1304	    46	  §1 Screener below). The client's assumption that this is a stable,
  1305	    47	  complete field universe is validated.
  1306	    48	- `t=` as a direct multi-ticker override for `export.ashx` (used in
  1307	    49	  `enrich_metadata.py`, bypassing the filter compiler) — CONFIRMED as a
  1308	    50	  general pattern; ticker-list-via-`t=` also works on other endpoints
  1309	    51	  (see per-family notes).
  1310	    52	
  1311	    53	**Where probing contradicts or extends the client's assumptions:**
  1312	    54	
  1313	    55	| Client assumption | Finding |
  1314	    56	|---|---|
  1315	    57	| `get_news(ticker)` — passing a ticker filters the news feed (`news_export.ashx?t={ticker}`) | **CONTRADICTED.** `/export/news?v=1` and `/export/news?v=1&t=MSFT` returned byte-identical first rows (same headline, same everything) across the full response. `t=` appears to have **no effect** on `/export/news` — it always returns the general market feed. See §1 News and §4. |
  1316	    58	| `get_quote()` targets `quote_export.ashx?t={ticker}&ty=c&p=d&b=1` | **Superseded, not confirmed necessary.** The documented current endpoint is `/export/stock?t=…&p=…` with no `ty=`/`b=` params at all (confirmed in the Stock screenshot's example URL). New-core `prefill.py` already moved off this legacy path for exactly this reason (the `.ashx` form 301-redirects). `ty=c`/`b=1` were not independently tested — they may be inert legacy params from an older API surface. |
  1317	    59	| `PRESET_QUERIES` use `v=150`; `execute_dynamic_screener` uses `v=152` | **Not a contradiction.** The official screenshot's own example uses `v=111`. All three values I've now seen work — `v=` looks like a Finviz-internal "view/column-preset ID" selector, not a version number; multiple valid IDs coexist. |
  1318	    60	| `PRESET_QUERIES` all include `ft=4` | **UNVERIFIED — not isolated.** I never tested `ft=` in isolation (the client always pairs it with a filter set). Meaning unconfirmed; likely a filter-type/universe toggle. Flagged for Phase B. |
  1319	    61	| `tc=7` used nowhere in the old client, but discovered on the Insider screenshot | Confirmed as a working filter parameter (see §1 Insider) but its **value semantics are unknown** — "7" is a Finviz-internal transaction-type code, not a raw SEC Form 4 code letter. INFERRED that other integers select other transaction types; not probed. |
  1320	    62	
  1321	    63	---
  1322	    64	
  1323	    65	## 1. Per-family findings (all eleven)
  1324	    66	
  1325	    67	Each entry: endpoint path, params tried, **CONFIRMED** result, and gaps.
  1326	    68	
  1327	    69	### Screener — CONFIRMED, working exactly as documented
  1328	    70	`GET /export/screener?v=<id>&f=<filters>&c=<col indices>&auth=…`
  1329	    71	- `v=111` (default view) → 200, 11 columns (`No., Ticker, Company,
  1330	    72	  Sector, Industry, Country, Market Cap, P/E, Price, Change, Volume`).
  1331	    73	- `v=152&c=0,1,2,3,4,5,6` → 200, exactly the 7 requested columns.
  1332	    74	- `v=152&c=0..150` (all indices) → 200, **all 151 named columns**,
  1333	    75	  confirming the client's `MASTER_COLUMNS` claim. Full field list (a
  1334	    76	  sample of the notable ones — Tier-1/Tier-2 relevant fields bolded):
  1335	    77	  `No, Ticker, Company, Sector, Industry, Country, Market Cap, P/E,
  1336	    78	  Forward P/E, PEG, P/S, P/B, P/Cash, P/FCF, Dividend Yield, Payout
  1337	    79	  Ratio, EPS(ttm), EPS Growth (This/Next Year, Past/Next 5Y, QoQ), Sales
  1338	    80	  Growth (Past 5Y, QoQ), **Shares Outstanding, Shares Float, Insider
  1339	    81	  Ownership, Insider Transactions, Institutional Ownership,
  1340	    82	  Institutional Transactions, Short Float, Short Ratio**, Return on
  1341	    83	  (Assets/Equity/Invested Capital), Current/Quick Ratio, LT/Total
  1342	    84	  Debt-to-Equity, Gross/Operating/Profit Margin, Performance (Week
  1343	    85	  through YTD, plus **1/2/3/5/10/15/30-min and 1/2/4-hour rolling
  1344	    86	  performance — 10 intraday-granularity columns**), Beta, **Average
  1345	    87	  True Range**, Volatility (Week/Month), 20/50/200-day SMA, 50-day &
  1346	    88	  52-week High/Low, RSI(14), Change from Open, Gap, Analyst Recom,
  1347	    89	  Average/Relative Volume, Price, Change, Volume, **Earnings Date**,
  1348	    90	  Target Price, IPO Date, After-Hours Close/Change/Volume, Book/Cash
  1349	    91	  per share, Dividend, Employees, **EPS Next Q, Income, Optionable,
  1350	    92	  Shortable, Short Interest, Float %**, OHL, Trades, [ETF-only block:
  1351	    93	  Asset Type, ETF Type, Region, Category, Tags, AUM, NAV, Net Flows
  1352	    94	  (1M/3M/YTD/1Y), multi-year Returns], **EPS/Revenue Surprise**,
  1353	    95	  Exchange, Dividend TTM/Ex-Date, 52-Week Range, **News Time, News URL,
  1354	    96	  News Title**, 3/5/10-year Performance, EPS/Sales Growth 3Y, Enterprise
  1355	    97	  Value, EV/EBITDA, EV/Sales, Dividend Growth (1/3/5Y), Daily Digest.
  1356	    98	- **New finding, not in any screenshot:** columns 135–137 (`News Time`,
  1357	    99	  `News URL`, `News Title`) put a per-ticker latest-headline directly in
  1358	   100	  screener output. Given `/export/news`'s `t=` filter doesn't work
  1359	   101	  (above), **this may be the actual working path to per-ticker news**,
  1360	   102	  not the dedicated News endpoint. INFERRED — only saw the column names
  1361	   103	  exist and are part of the schema; didn't verify populated values for
  1362	   104	  a specific low-news ticker vs. a high-news one.
  1363	   105	- Gap: `ft=` parameter meaning unconfirmed (see §0).
  1364	   106	
  1365	   107	### Portfolio — CONFIRMED endpoint exists, needs a real Dejan-owned ID
  1366	   108	`GET /export/portfolio?pid=<id>&auth=…`
  1367	   109	- Bare and `pid=1` both → **404, body `"Portfolio not found."`** — a
  1368	   110	  specific, meaningful error (not a generic route-404), confirming the
  1369	   111	  endpoint and `pid=` param both exist and are being validated, but no
  1370	   112	  portfolio with ID `1` exists on this account. INFERRED that `pid=`
  1371	   113	  needs one of Dejan's own saved-portfolio IDs from the Finviz UI —
  1372	   114	  untested with a real one (none created yet). Gap for Phase B.
  1373	   115	
  1374	   116	### Stock — see §2, the priority section.
  1375	   117	
  1376	   118	### Groups — CONFIRMED reachable, response empty with params tried
  1377	   119	`GET /export/groups?g=<?>&auth=…`
  1378	   120	- Bare and `g=sector` both → **200, `text/csv`, empty body.** The route
  1379	   121	  exists and doesn't error, but produces no rows with either param
  1380	   122	  tried. INFERRED that a required param (view ID like `v=`, or a
  1381	   123	  different `g=` enum value — Finviz's UI groups by sector, industry,
  1382	   124	  country, capitalization) is missing. Gap for Phase B — this family is
  1383	   125	  the least-confirmed of the eleven.
  1384	   126	
  1385	   127	### Options — CONFIRMED
  1386	   128	`GET /export/options?t=<ticker>&ty=oc&e=<expiry YYYY-MM-DD>&auth=…`
  1387	   129	- `t=MSFT&ty=oc&e=2026-09-18` → 200, 206 rows, 17 columns: `Contract
  1388	   130	  Name, Last Trade, Strike, Last Close, Bid, Ask, Change $, Change %,
  1389	   131	  Volume, Open Int., Type, IV, Delta, Gamma, Theta, Vega, Rho`.
  1390	   132	- Full Greeks present (Delta/Gamma/Theta/Vega/Rho) — stronger than
  1391	   133	  §8 Tier-3's minimum ask (IV rank/skew/OI). IV rank/percentile and term
  1392	   134	  structure are NOT directly given (only per-contract IV) — would need
  1393	   135	  to be computed from repeated pulls across expiries/dates.
  1394	   136	- `ty=` only tested as `oc`; other values (single-strike view?) INFERRED
  1395	   137	  to exist, not probed (Tier-3 is "design now, build later" — matches
  1396	   138	  the low-effort spend here).
  1397	   139	
  1398	   140	### Latest Filings — CONFIRMED
  1399	   141	`GET /export/latest-filings?t=<ticker>&o=<sort>&auth=…`
  1400	   142	- `t=MSFT&o=-filingDate` → 200, 1828 rows, 6 columns: `Filing Date,
  1401	   143	  Report Date, Form, Description, Filing, Document`.
  1402	   144	- The `Form` column (10-K, 10-Q, 8-K, S-3, 424B5, Form 4, …) makes this
  1403	   145	  a plausible, previously-unconsidered path toward §8 Tier-1's
  1404	   146	  dilution-risk monitoring (effective S-3s/ATMs) — filter/scan `Form`
  1405	   147	  client-side. Not filed as a direct requirements match originally;
  1406	   148	  worth a design note.
  1407	   149	
  1408	   150	### News — CONFIRMED, with the client-contradicting finding from §0
  1409	   151	`GET /export/news?v=1[&t=<ticker>]&auth=…`
  1410	   152	- `v=1` → 200, 180 rows, 5 columns: `Title, Source, Date, Url,
  1411	   153	  Category`.
  1412	   154	- `v=1&t=MSFT` → 200, 180 rows, **identical first row to the
  1413	   155	  ticker-less call**. `t=` is not filtering. See §0's contradiction
  1414	   156	  entry and §4.
  1415	   157	- `v=` only tested as `1`; other values INFERRED to exist (maybe a
  1416	   158	  blogs/press-release toggle) — not probed.
  1417	   159	
  1418	   160	### Insider — CONFIRMED, filtering works
  1419	   161	`GET /export/insiders?tc=<code>[&t=<ticker>]&auth=…`
  1420	   162	- `tc=7` alone → 200, 200 rows (**hit what looks like a row cap** — see
  1421	   163	  Managers/Funds below for a *documented* 500-row cap; 200 may be a
  1422	   164	  separate, undocumented cap for this family, or coincidental — not
  1423	   165	  isolated).
  1424	   166	- `tc=7&t=MSFT` → 200, 94 rows — **different from the untargeted count,
  1425	   167	  confirming `t=` DOES filter here** (unlike News). 12 columns: `Ticker,
  1426	   168	  Owner, Owner CIK, Relationship, Date, Transaction, Cost, #Shares,
  1427	   169	  Value ($), #Shares Total, SEC Form 4, SEC Form 4 Link`.
  1428	   170	- `tc=` value semantics (why "7") — INFERRED/unknown, gap for Phase B.
  1429	   171	
  1430	   172	### Managers — CONFIRMED, exact mechanics as documented
  1431	   173	- List: `GET /export/managers?search=<partial name>&auth=…` — `search=
  1432	   174	  berkshire` → 200, 10 rows, 14 columns (`Name, Portfolio Manager,
  1433	   175	  Investor ID, Report Date, Portfolio Value, # Investments, New
  1434	   176	  Purchased, Sold Out, Added, Reduced, Top 10 Concentration (%),
  1435	   177	  Turnover (%), Time Held Top 10, Time Held All`). **500-row cap is
  1436	   178	  documented in-app** (screenshot text), not hit here since the search
  1437	   179	  matched only 10.
  1438	   180	- Holdings: `GET /export/managers/<investor ID>/holdings&auth=…` (path
  1439	   181	  segment, not a query param — confirmed both the bare-ID form and the
  1440	   182	  name-slug form work per the screenshot; I used the bare-ID form live)
  1441	   183	  → 200, 30 rows, 14 columns (`Ticker, Name, Type, Sector, Industry,
  1442	   184	  Shares Held, Market Value, % Portfolio, Prev. % Portfolio, Change in
  1443	   185	  Shares, % Change, % Ownership, Avg. Price, Q 1st Owned`).
  1444	   186	
  1445	   187	### Funds — CONFIRMED, identical mechanics to Managers
  1446	   188	- List: `GET /export/funds?search=<partial name>&auth=…` — `search=
  1447	   189	  fidelity` → 200, **exactly 500 rows** — the documented row cap
  1448	   190	  **CONFIRMED hit** in practice. 14 columns (same shape as Managers'
  1449	     1	"""Finviz `/export/stock` intraday-bar fetcher. Fail-loud, secret-safe.
  1450	     2	
  1451	     3	Reuses the existing vault-backed `FinvizApiClient` for token resolution
  1452	     4	only (same one-directional read-across-the-strangler-boundary pattern
  1453	     5	as `aset/prefill.py`) — the old tree stays untouched.
  1454	     6	
  1455	     7	Per DATA-SOURCE-MEMO.md's confirmed findings:
  1456	     8	- `p=` is a validated enum here (Interval) — bare/unrecognized values
  1457	     9	  silently return the full daily dataset with no error. Any response
  1458	    10	  whose dates lack a time-of-day component is exactly that failure
  1459	    11	  mode and is rejected loudly, never stored.
  1460	    12	- Response columns are always exactly Date, Open, High, Low, Close,
  1461	    13	  Volume — a mismatch is also rejected loudly.
  1462	    14	- Finviz's own date strings are inconsistently formatted between
  1463	    15	  intervals (`i1/i2/i5` give clean 12-hour "04:00 AM"; `i15/i30` have
  1464	    16	  been observed giving a 24-hour hour with a bolted-on AM/PM suffix
  1465	    17	  like "15:45 PM") — `_parse_finviz_datetime` handles both.
  1466	    18	
  1467	    19	TIMEZONE (ADR-0007, 2026-09-04). Finviz's export carries a bare ET
  1468	    20	wall clock with no offset and no tz name — "09/03/2026 09:30 AM" is
  1469	    21	09:30 *America/New_York*. Until ADR-0007 this parser returned that
  1470	    22	naive value unchanged, psycopg handed it to a `timestamptz` column,
  1471	    23	and Postgres (session `TimeZone = Etc/UTC`) stamped it `09:30+00`.
  1472	    24	4.75M rows were therefore ET digits wearing a UTC label: every one of
  1473	    25	them wrong by the ET offset, and every join against them wrong by the
  1474	    26	same. The corpus was reinterpreted in place by ADR-0007; this parser
  1475	    27	is the other half — it localizes to `America/New_York` (DST-aware, so
  1476	    28	the offset is the one that applied on that date) and converts to UTC
  1477	    29	before the value ever reaches a `Bar`. Bars are tz-aware UTC from
  1478	    30	here on; sessions are reasoned about in ET by `cobalt.session`, never
  1479	    31	by wall clock.
  1480	    32	"""
  1481	    33	
  1482	    34	import csv
  1483	    35	import io
  1484	    36	import re
  1485	    37	from datetime import datetime, timezone
  1486	    38	from decimal import Decimal, InvalidOperation
  1487	    39	from zoneinfo import ZoneInfo
  1488	    40	
  1489	    41	import httpx
  1490	    42	
  1491	    43	from cobalt_agent.skills.research.finviz_api import FinvizApiClient
  1492	    44	
  1493	    45	from .models import Bar, Interval
  1494	    46	
  1495	    47	EXPECTED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]
  1496	    48	_AUTH_RE = re.compile(r"auth=[^&\s'\"]+")
  1497	    49	
  1498	    50	# Finviz's export timestamps are bare ET wall clock (ADR-0007).
  1499	    51	FINVIZ_TZ = ZoneInfo("America/New_York")
  1500	    52	
  1501	    53	
  1502	    54	class CollectorError(RuntimeError):
  1503	    55	    """Fetch or shape-validation failure — never store, never guess."""
  1504	    56	
  1505	    57	
  1506	    58	def scrub(text: str) -> str:
  1507	    59	    return _AUTH_RE.sub("auth=REDACTED", text)
  1508	    60	
  1509	    61	
  1510	    62	async def resolve_token() -> str:
  1511	    63	    client = FinvizApiClient()
  1512	    64	    try:
  1513	    65	        return await client._resolve_vault_credentials(client.FINVIZ_DOMAIN)
  1514	    66	    except Exception as e:
  1515	    67	        raise CollectorError(f"Finviz token resolution failed: {scrub(str(e))}") from e
  1516	    68	
  1517	    69	
  1518	    70	def _parse_finviz_datetime(raw: str) -> datetime:
  1519	    71	    """Parse one Finviz date cell into a tz-aware UTC datetime.
  1520	    72	
  1521	    73	    The string is a bare ET wall clock. It is localized to
  1522	    74	    `America/New_York` and converted to UTC (ADR-0007) — the returned
  1523	    75	    value is ALWAYS tz-aware, never naive.
  1524	    76	    """
  1525	    77	    return _parse_finviz_wall_clock(raw).replace(tzinfo=FINVIZ_TZ).astimezone(
  1526	    78	        timezone.utc
  1527	    79	    )
  1528	    80	
  1529	    81	
  1530	    82	def _parse_finviz_wall_clock(raw: str) -> datetime:
  1531	    83	    """The naive ET wall clock exactly as Finviz wrote it. Format handling
  1532	    84	    only — the timezone is applied by `_parse_finviz_datetime`."""
  1533	    85	    raw = raw.strip()
  1534	    86	    parts = raw.split(" ")
  1535	    87	    if len(parts) < 2:
  1536	    88	        # No time-of-day component at all -> this is the daily-fallback
  1537	    89	        # shape (bare/unrecognized p= silently returns daily). We never
  1538	    90	        # request daily, so this is always a failure, never a valid row.
  1539	    91	        raise CollectorError(
  1540	    92	            f"Date {raw!r} has no time-of-day component — Finviz likely "
  1541	    93	            "fell back to daily (unrecognized interval), refusing to store."
  1542	    94	        )
  1543	    95	    date_part, time_part = parts[0], parts[1]
  1544	    96	
  1545	    97	    # Clean 12-hour form: "04:00 AM" / "06:52 AM" (date_part time_part meridiem)
  1546	    98	    try:
  1547	    99	        return datetime.strptime(raw, "%m/%d/%Y %I:%M %p")
  1548	   100	    except ValueError:
  1549	   101	        pass
  1550	   102	
  1551	   103	    # Observed quirk: a 24-hour hour with a bolted-on AM/PM suffix, e.g.
  1552	   104	    # "08/26/2026 15:45 PM". Parse the 24-hour time, ignore the suffix.
  1553	   105	    try:
  1554	   106	        return datetime.strptime(f"{date_part} {time_part}", "%m/%d/%Y %H:%M")
  1555	   107	    except ValueError:
  1556	   108	        pass
  1557	   109	
  1558	   110	    raise CollectorError(f"Unparseable Finviz datetime: {raw!r}")
  1559	   111	
  1560	   112	
  1561	   113	def parse_csv_response(text: str, ticker: str, interval: Interval) -> list[Bar]:
  1562	   114	    """Pure parsing/validation — no I/O. Raises CollectorError on any
  1563	   115	    shape mismatch; never returns a partial or guessed result."""
  1564	   116	    rows = list(csv.reader(io.StringIO(text)))
  1565	   117	    if not rows:
  1566	   118	        raise CollectorError(f"Empty response for {ticker}/{interval.value}.")
  1567	   119	
  1568	   120	    header = rows[0]
  1569	   121	    if header != EXPECTED_COLUMNS:
  1570	   122	        raise CollectorError(
  1571	   123	            f"Unexpected columns for {ticker}/{interval.value}: {header} "
  1572	   124	            f"(expected {EXPECTED_COLUMNS})"
  1573	   125	        )
  1574	   126	
  1575	   127	    if len(rows) == 1:
  1576	   128	        raise CollectorError(f"No data rows for {ticker}/{interval.value}.")
  1577	   129	
  1578	   130	    bars: list[Bar] = []
  1579	   131	    for row in rows[1:]:
  1580	   132	        if len(row) != 6:
  1581	   133	            raise CollectorError(
  1582	   134	                f"Malformed row for {ticker}/{interval.value}: {row!r}"
  1583	   135	            )
  1584	   136	        date_s, open_s, high_s, low_s, close_s, vol_s = row
  1585	   137	        try:
  1586	   138	            ts = _parse_finviz_datetime(date_s)
  1587	   139	            bars.append(
  1588	   140	                Bar(
  1589	   141	                    ticker=ticker,
  1590	   142	                    interval=interval,
  1591	   143	                    ts=ts,
  1592	   144	                    open=Decimal(open_s),
  1593	   145	                    high=Decimal(high_s),
  1594	   146	                    low=Decimal(low_s),
  1595	   147	                    close=Decimal(close_s),
  1596	   148	                    volume=int(Decimal(vol_s)),
  1597	   149	                )
  1598	   150	            )
  1599	   151	        except (InvalidOperation, ValueError) as e:
  1600	   152	            raise CollectorError(
  1601	   153	                f"Unparseable row for {ticker}/{interval.value}: {row!r} ({e})"
  1602	   154	            ) from e
  1603	   155	
  1604	   156	    return bars
  1605	   157	
  1606	   158	
  1607	   159	async def fetch_bars(ticker: str, interval: Interval, token: str) -> list[Bar]:
  1608	   160	    """Fetch one (ticker, interval)'s bars over the network, then
  1609	   161	    validate/parse via `parse_csv_response`."""
  1610	   162	    ticker = ticker.strip().upper()
  1611	   163	    url = "https://elite.finviz.com/export/stock"
  1612	   164	    params = {"t": ticker, "p": interval.value, "auth": token}
  1613	   165	    try:
  1614	   166	        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
  1615	   167	            response = await client.get(url, params=params)
  1616	   168	            response.raise_for_status()
  1617	   169	    except Exception as e:
  1618	   170	        raise CollectorError(
  1619	   171	            f"Fetch failed for {ticker}/{interval.value}: {scrub(str(e))}"
  1620	   172	        ) from e
  1621	   173	
  1622	   174	    return parse_csv_response(response.text, ticker, interval)
  1623	
  1624	codex
  1625	The addendum conflicts with several build instructions: account-mode refusal, vault-owned pool rules, credential handling, and restart rules. I’m also checking whether the proposed collector and job interfaces can support the stated acceptance tests.
  1626	exec
  1627	/bin/zsh -lc "nl -ba src/cobalt/jobs/wrapper.py | sed -n '1,280p'; nl -ba src/cobalt/jobs/watchdog.py | sed -n '305,415p'; nl -ba src/cobalt/db_migrations/cli.py | sed -n '1,255p'; cat src/cobalt/db_migrations/__init__.py; nl -ba src/cobalt/db_migrations/placement.py | tail -70" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
  1628	 succeeded in 0ms:
  1629	     1	"""F17b: the wrapper every scheduled job runs inside.
  1630	     2	
  1631	     3	Charter §3 F17: "marks running/done/failed with exit code and stamps
  1632	     4	heartbeat_at at least every timeout_s/3 for long jobs."
  1633	     5	
  1634	     6	TWO WAYS IN, one implementation:
  1635	     7	
  1636	     8	    # a Python entry point (prefill, archiver, cards-expire, …)
  1637	     9	    with job_run("com.cobalt.archiver") as run:
  1638	    10	        summary = do_the_work()
  1639	    11	        run.result = {"rows_written": summary.rows_written}
  1640	    12	
  1641	    13	    # anything else, from a plist
  1642	    14	    uv run cobalt jobs run com.cobalt.prefill-daily -- uv run prefill daily
  1643	    15	
  1644	    16	WHAT IT GUARANTEES, in order:
  1645	    17	
  1646	    18	1. THE KILL SWITCH IS CHECKED FIRST. A stopped Cobalt does not start a
  1647	    19	   one-shot at all — except the heartbeat, whose validated registry flag
  1648	    20	   keeps the watcher running so it can report the stop itself.
  1649	    21	2. `running` is marked before the work, with `started_at`.
  1650	    22	3. A BEATER THREAD stamps `heartbeat_at` every `timeout_s /
  1651	    23	   jobs.heartbeat_fraction` (5 min for the 15-min archiver window). This
  1652	    24	   is the ONLY thing that distinguishes a long job from a hung one — the
  1653	    25	   archiver legitimately runs 23 minutes, so "started and did not
  1654	    26	   finish" cannot be the zombie test.
  1655	    27	4. `done` (exit 0) or `failed` (exit code + the exception, redacted
  1656	    28	   through F19 on the way into the column) — and `failed` is LOUD.
  1657	    29	5. The exception is RE-RAISED. The wrapper reports; it never swallows.
  1658	    30	
  1659	    31	The beater thread is a daemon: if the job process dies hard, the thread
  1660	    32	dies with it, `heartbeat_at` stops advancing, and the watchdog draws the
  1661	    33	right conclusion. A thread that outlived its job would keep a dead job
  1662	    34	looking alive, which is the exact failure this feature exists to catch.
  1663	    35	"""
  1664	    36	
  1665	    37	from __future__ import annotations
  1666	    38	
  1667	    39	import threading
  1668	    40	import traceback
  1669	    41	from contextlib import contextmanager
  1670	    42	from typing import Any, Optional
  1671	    43	
  1672	    44	from loguru import logger
  1673	    45	
  1674	    46	from . import killswitch
  1675	    47	from .config import JobSpec, load_job_registry
  1676	    48	from .store import JobStore
  1677	    49	
  1678	    50	#: The tunables row governing how often a long job stamps (F16).
  1679	    51	HEARTBEAT_FRACTION_KEY = "jobs.heartbeat_fraction"
  1680	    52	
  1681	    53	#: Exit code a job uses when the kill switch turned it away. ZERO, on
  1682	    54	#: purpose — see guarantee 1.
  1683	    55	STOPPED_EXIT_CODE = 0
  1684	    56	
  1685	    57	
  1686	    58	class JobStopped(RuntimeError):
  1687	    59	    """The kill switch is engaged; this run did not happen."""
  1688	    60	
  1689	    61	
  1690	    62	def heartbeat_fraction() -> int:
  1691	    63	    from cobalt.taxonomy.loader import load_tunables
  1692	    64	
  1693	    65	    row = load_tunables().by_key.get(HEARTBEAT_FRACTION_KEY)
  1694	    66	    if row is None:
  1695	    67	        raise RuntimeError(
  1696	    68	            f"tunable {HEARTBEAT_FRACTION_KEY!r} is missing from tunables.yaml — the "
  1697	    69	            "wrapper reads its stamp interval from config and has no built-in "
  1698	    70	            "default (F16)."
  1699	    71	        )
  1700	    72	    return int(row.value)
  1701	    73	
  1702	    74	
  1703	    75	class _Beater:
  1704	    76	    """Stamps `heartbeat_at` on a timer until the run ends."""
  1705	    77	
  1706	    78	    def __init__(self, store: JobStore, label: str, every_s: float):
  1707	    79	        self.store = store
  1708	    80	        self.label = label
  1709	    81	        self.every_s = max(1.0, every_s)
  1710	    82	        self._stop = threading.Event()
  1711	    83	        self._thread = threading.Thread(
  1712	    84	            target=self._loop, name=f"beat:{label}", daemon=True
  1713	    85	        )
  1714	    86	
  1715	    87	    def _loop(self) -> None:
  1716	    88	        while not self._stop.wait(self.every_s):
  1717	    89	            try:
  1718	    90	                self.store.beat(self.label)
  1719	    91	            except Exception as e:  # noqa: BLE001
  1720	    92	                # A missed stamp is not a reason to kill the job. It IS a
  1721	    93	                # reason to say so: the watchdog may conclude ZOMBIE from
  1722	    94	                # this, and an operator needs the other half of the story.
  1723	    95	                logger.error(
  1724	    96	                    "F17: heartbeat stamp FAILED for {} ({}: {}) — the job is still "
  1725	    97	                    "running; the watchdog may see a stale heartbeat.",
  1726	    98	                    self.label, type(e).__name__, e,
  1727	    99	                )
  1728	   100	
  1729	   101	    def __enter__(self) -> "_Beater":
  1730	   102	        self._thread.start()
  1731	   103	        return self
  1732	   104	
  1733	   105	    def __exit__(self, *exc) -> None:
  1734	   106	        self._stop.set()
  1735	   107	
  1736	   108	
  1737	   109	class JobRun:
  1738	   110	    """Handle a wrapped job can hang its result on."""
  1739	   111	
  1740	   112	    def __init__(self, spec: JobSpec):
  1741	   113	        self.spec = spec
  1742	   114	        self.label = spec.label
  1743	   115	        #: Whatever the run wants F18 to be able to report — the
  1744	   116	        #: archiver's `rows_written` is what makes "archiver freshness
  1745	   117	        #: (last run + rows written)" answerable.
  1746	   118	        self.result: Optional[dict[str, Any]] = None
  1747	   119	
  1748	   120	
  1749	   121	@contextmanager
  1750	   122	def job_run(
  1751	   123	    label: str,
  1752	   124	    *,
  1753	   125	    store: Optional[JobStore] = None,
  1754	   126	    register: bool = True,
  1755	   127	    allow_prod: bool = False,
  1756	   128	):
  1757	   129	    """Run a block as a registered job. See the module docstring."""
  1758	   130	    registry = load_job_registry()
  1759	   131	    spec = registry.spec(label)
  1760	   132	    store = store or JobStore()
  1761	   133	
  1762	   134	    def bookkeeping(stage: str, operation) -> bool:
  1763	   135	        try:
  1764	   136	            operation()
  1765	   137	            return True
  1766	   138	        except Exception as e:  # noqa: BLE001 - heartbeat must still launch
  1767	   139	            if not spec.kill_switch_exempt:
  1768	   140	                raise
  1769	   141	            logger.error(
  1770	   142	                "F17: {} {} FAILED ({}: {}) — heartbeat subprocess WILL STILL RUN; "
  1771	   143	                "its database probe and out-of-band alert own this outage.",
  1772	   144	                label, stage, type(e).__name__, e,
  1773	   145	            )
  1774	   146	            return False
  1775	   147	
  1776	   148	    bookkeeping(
  1777	   149	        "schema setup", lambda: store.ensure_schema(allow_prod=allow_prod)
  1778	   150	    )
  1779	   151	    if register:
  1780	   152	        bookkeeping(
  1781	   153	            "registration", lambda: store.register(spec, allow_prod=allow_prod)
  1782	   154	        )
  1783	   155	
  1784	   156	    if killswitch.is_active(store):
  1785	   157	        state = killswitch.read(store)
  1786	   158	        if not spec.kill_switch_exempt:
  1787	   159	            logger.error("F17: {} REFUSED TO START — {}", label, state.describe())
  1788	   160	            raise JobStopped(state.describe())
  1789	   161	        logger.error(
  1790	   162	            "F17: {} is kill-switch EXEMPT and WILL RUN — {}",
  1791	   163	            label,
  1792	   164	            state.describe(),
  1793	   165	        )
  1794	   166	
  1795	   167	    bookkeeping("mark_running", lambda: store.mark_running(label))
  1796	   168	    run = JobRun(spec)
  1797	   169	    every_s = spec.timeout_s / heartbeat_fraction()
  1798	   170	    logger.info(
  1799	   171	        "F17: {} RUNNING (timeout {}s, heartbeat every {:.0f}s)",
  1800	   172	        label, spec.timeout_s, every_s,
  1801	   173	    )
  1802	   174	    try:
  1803	   175	        with _Beater(store, label, every_s):
  1804	   176	            yield run
  1805	   177	    except BaseException as e:
  1806	   178	        error = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}"
  1807	   179	        finish = store.mark_wrapper_finished if spec.kill_switch_exempt else store.mark_finished
  1808	   180	        bookkeeping(
  1809	   181	            "mark_finished",
  1810	   182	            lambda: finish(
  1811	   183	                label,
  1812	   184	                exit_code=1,
  1813	   185	                error=error,
  1814	   186	                result=run.result,
  1815	   187	            ),
  1816	   188	        )
  1817	   189	        logger.error("F17: {} FAILED — {}: {}", label, type(e).__name__, e)
  1818	   190	        raise            # the wrapper reports; it never swallows
  1819	   191	    finish = store.mark_wrapper_finished if spec.kill_switch_exempt else store.mark_finished
  1820	   192	    bookkeeping(
  1821	   193	        "mark_finished",
  1822	   194	        lambda: finish(label, exit_code=0, result=run.result),
  1823	   195	    )
  1824	   196	    logger.info("F17: {} DONE", label)
  1825	   197	
  1826	   198	
  1827	   199	def should_keep_running(label: str, *, store: Optional[JobStore] = None) -> bool:
  1828	   200	    """A RESIDENT's own loop check. `False` means exit cleanly now.
  1829	   201	
  1830	   202	    Residents call this where they can stop without tearing out of a
  1831	   203	    write. Cobalt's residents today are supervised by launchd rather than
  1832	   204	    wrapped (see jobs.yaml), so this exists for the first new-core
  1833	   205	    resident — the S2 radar poller — and for anything the chief of staff
  1834	   206	    grows into.
  1835	   207	    """
  1836	   208	    if killswitch.is_active(store):
  1837	   209	        logger.error(
  1838	   210	            "F17: kill switch engaged — {} is exiting cleanly at its next safe point.",
  1839	   211	            label,
  1840	   212	        )
  1841	   213	        return False
  1842	   214	    return True
  1843	   215	
  1844	   216	
  1845	   217	__all__ = [
  1846	   218	    "HEARTBEAT_FRACTION_KEY",
  1847	   219	    "STOPPED_EXIT_CODE",
  1848	   220	    "JobRun",
  1849	   221	    "JobStopped",
  1850	   222	    "heartbeat_fraction",
  1851	   223	    "job_run",
  1852	   224	    "should_keep_running",
  1853	   225	]
  1854	   305	    store.ensure_schema()
  1855	   306	    ts = now or clock_mod.now_utc()
  1856	   307	    now_et = session_clock().to_et(ts)
  1857	   308	    fraction = _tunable_int("jobs.heartbeat_fraction")
  1858	   309	    grace = timedelta(minutes=_tunable_int(MISSED_GRACE_KEY))
  1859	   310	
  1860	   311	    findings: list[Finding] = []
  1861	   312	    rows = {r["label"]: r for r in store.all()}
  1862	   313	
  1863	   314	    for spec in registry.jobs:
  1864	   315	        row = rows.get(spec.label)
  1865	   316	
  1866	   317	        # -- IS THIS JOB EVEN SUPPOSED TO BE LOADED? A registry row with
  1867	   318	        # `enabled: false` is a job that has been BUILT and reviewed but
  1868	   319	        # not yet handed over to launchd. Every check below asks a
  1869	   320	        # question whose honest answer for such a job is "of course not"
  1870	   321	        # — probing it would put a permanent red on the beat for a state
  1871	   322	        # somebody chose deliberately, and a standing red is how a
  1872	   323	        # heartbeat stops being read. It is REPORTED, not hidden: the
  1873	   324	        # line is on the block, it just is not a failure.
  1874	   325	        if not spec.enabled:
  1875	   326	            findings.append(
  1876	   327	                Finding(
  1877	   328	                    spec.label, True, "disabled",
  1878	   329	                    "registered but NOT LOADED BY DESIGN (`enabled: false` in "
  1879	   330	                    "configs/cobalt/jobs.yaml) — nothing is probed and nothing is "
  1880	   331	                    "claimed. Flip the flag as the last step of its handover.",
  1881	   332	                )
  1882	   333	            )
  1883	   334	            continue
  1884	   335	
  1885	   336	        # -- IS THE PLIST EVEN LOADED? Charter §3 F18: "every ops plist
  1886	   337	        # loaded + last exit code". Asked of EVERY job, resident and
  1887	   338	        # one-shot alike, and asked FIRST.
  1888	   339	        #
  1889	   340	        # This check was missing from the first version of this function,
  1890	   341	        # and running the Charter's own acceptance test for real is what
  1891	   342	        # found it: `launchctl bootout com.cobalt.cards-expire` and the
  1892	   343	        # heartbeat stayed green, because a one-shot between runs looks
  1893	   344	        # identical whether its plist is loaded or gone. An unloaded
  1894	   345	        # one-shot has no PID to lose and no state to change — it simply
  1895	   346	        # never fires again, and MISSED would not say so until its next
  1896	   347	        # scheduled time plus the grace, which for a Friday-evening
  1897	   348	        # unload is Monday.
  1898	   349	        if probe:
  1899	   350	            try:
  1900	   351	                status = launchctl_status(spec.label)
  1901	   352	            except Exception as e:  # noqa: BLE001
  1902	   353	                findings.append(
  1903	   354	                    Finding(spec.label, False, (row or {}).get("state", "unknown"),
  1904	   355	                            f"launchd PROBE FAILED ({type(e).__name__}: {e}) — loaded "
  1905	   356	                            "state UNKNOWN, which is not the same as loaded")
  1906	   357	                )
  1907	   358	                continue
  1908	   359	            if not status.loaded:
  1909	   360	                # A RESIDENT's row IS its liveness, so it is marked. A
  1910	   361	                # ONE-SHOT's row is the record of its LAST RUN, and
  1911	   362	                # "the plist is gone" is a fact about launchd, not about
  1912	   363	                # that run — overwriting `state` and `exit_code` with it
  1913	   364	                # would destroy the only record of how the job last
  1914	   365	                # ended, and leave a stale `failed` behind after the
  1915	   366	                # plist is reloaded (which is exactly what happened the
  1916	   367	                # first time this ran: reload restored the plist and the
  1917	   368	                # row still said failed). It is reported, not written.
  1918	   369	                if row is not None and spec.kind is JobKind.RESIDENT:
  1919	   370	                    store.mark_probe(spec.label, alive=False, detail=status.detail, now=ts)
  1920	   371	                findings.append(Finding(spec.label, False, "not loaded", status.detail))
  1921	   372	                continue
  1922	   373	
  1923	   374	        if row is None:
  1924	   375	            store.register(spec)
  1925	   376	            findings.append(
  1926	   377	                Finding(spec.label, False, "unregistered",
  1927	   378	                        "no jobs row existed — registered now; nothing has run yet")
  1928	   379	            )
  1929	   380	            continue
  1930	   381	
  1931	   382	        # -- residents someone else supervises: PROBE them -------------
  1932	   383	        if spec.supervisor is not Supervisor.SELF:
  1933	   384	            if not probe:
  1934	   385	                findings.append(Finding(spec.label, True, row["state"], "probe skipped"))
  1935	   386	                continue
  1936	   387	            try:
  1937	   388	                if spec.supervisor is Supervisor.LAUNCHD:
  1938	   389	                    alive = status.pid is not None
  1939	   390	                    detail = status.detail
  1940	   391	                else:
  1941	   392	                    alive, detail = pidfile_alive(spec)
  1942	   393	            except Exception as e:  # noqa: BLE001 - a broken probe is its own red
  1943	   394	                findings.append(
  1944	   395	                    Finding(spec.label, False, row["state"],
  1945	   396	                            f"PROBE FAILED ({type(e).__name__}: {e}) — liveness UNKNOWN, "
  1946	   397	                            "which is not the same as 'up' and is reported as red")
  1947	   398	                )
  1948	   399	                continue
  1949	   400	            store.mark_probe(spec.label, alive=alive, detail=detail, now=ts)
  1950	   401	            findings.append(
  1951	   402	                Finding(
  1952	   403	                    spec.label, alive,
  1953	   404	                    JobState.RUNNING.value if alive else JobState.FAILED.value,
  1954	   405	                    f"{detail} [{spec.supervisor} probe]",
  1955	   406	                )
  1956	   407	            )
  1957	   408	            continue
  1958	   409	
  1959	   410	        # -- jobs the wrapper reports on -------------------------------
  1960	   411	        state = row["state"]
  1961	   412	
  1962	   413	        if state == JobState.RUNNING.value:
  1963	   414	            started, beat = row["started_at"], row["heartbeat_at"]
  1964	   415	            ran_for = (ts - started).total_seconds() if started else 0
  1965	     1	"""`cobalt db migrate [--allow-prod] [--rollback]` — ADR-0008's harness.
  1966	     2	
  1967	     3	WHAT IT PRINTS IS THE POINT. A migration that moves twelve tables between
  1968	     4	schemas and adds a column to six of them is a migration whose claim
  1969	     5	("nothing was lost") has to be checkable by looking, not by trusting. So
  1970	     6	every run captures, per table, BEFORE and AFTER:
  1971	     7	
  1972	     8	  * where it lives (`public` / `system` / `"user"`),
  1973	     9	  * `count(*)`,
  1974	    10	  * a content digest: `md5(string_agg(row::text, '|' ORDER BY <pk>))`.
  1975	    11	
  1976	    12	THE DIGEST EXCLUDES every column added by these migrations: `user_id`,
  1977	    13	`vault_outcome`, and `vault_reason`. A digest over the whole row would
  1978	    14	differ before and after by construction and would prove nothing. Taking
  1979	    15	it over `to_jsonb(t)` minus those columns makes the two digests comparable,
  1980	    16	and an inequality is a real finding: the rows themselves changed. `to_jsonb`
  1981	    17	serialises keys in a stable order, so the digest does not depend on
  1982	    18	column order either — which matters, because `SET SCHEMA` and `ADD
  1983	    19	COLUMN` both touch the catalog the naive `row::text` reads.
  1984	    20	
  1985	    21	ORDERED BY THE PRIMARY KEY, read from the catalog per table rather than
  1986	    22	hard-coded: `bars` is keyed `(ticker, interval, ts)`, `day_modes` by
  1987	    23	`trade_date`, `cobalt_jobs` by `label`, the rest by `id`.
  1988	    24	
  1989	    25	`--rollback` runs the registered reverse migrations newest-first
  1990	    26	and prints the same proof table. Running `migrate`, then `--rollback`,
  1991	    27	then `migrate` again must land on the same digests — the suite asserts
  1992	    28	exactly that round-trip on `cobalt_dev`.
  1993	    29	
  1994	    30	`--allow-prod` reaches `cobalt_brain` without flipping the process into
  1995	    31	production mode (RULING 7's one-off-tooling seam). Without it the target
  1996	    32	is whatever `COBALT_ENV` resolves.
  1997	    33	"""
  1998	    34	
  1999	    35	from __future__ import annotations
  2000	    36	
  2001	    37	import argparse
  2002	    38	from typing import Optional
  2003	    39	
  2004	    40	from psycopg import sql
  2005	    41	
  2006	    42	from cobalt import db, env
  2007	    43	
  2008	    44	from . import FORWARD, REVERSE
  2009	    45	from .placement import MOVED_TABLES, SEEDED_TABLES
  2010	    46	
  2011	    47	#: Columns introduced by the registered migrations. Excluding them makes a
  2012	    48	#: populated row comparable before and after a shape-only migration.
  2013	    49	DIGEST_EXCLUDED_COLUMNS = ("user_id", "vault_outcome", "vault_reason")
  2014	    50	
  2015	    51	#: Where a new-core table may legitimately be found, in look-up order.
  2016	    52	SEARCHED_SCHEMAS = ("public", "user", "system")
  2017	    53	
  2018	    54	
  2019	    55	class MigrationError(RuntimeError):
  2020	    56	    """The migration could not be run or could not be proven."""
  2021	    57	
  2022	    58	
  2023	    59	def _schema_of(conn, table: str) -> Optional[str]:
  2024	    60	    row = conn.execute(
  2025	    61	        "SELECT schemaname FROM pg_tables "
  2026	    62	        "WHERE tablename = %s AND schemaname = ANY(%s) LIMIT 1",
  2027	    63	        (table, list(SEARCHED_SCHEMAS)),
  2028	    64	    ).fetchone()
  2029	    65	    return row[0] if row else None
  2030	    66	
  2031	    67	
  2032	    68	def _pk_columns(conn, schema: str, table: str) -> list[str]:
  2033	    69	    rows = conn.execute(
  2034	    70	        """
  2035	    71	        SELECT a.attname
  2036	    72	        FROM pg_index i
  2037	    73	        JOIN pg_attribute a
  2038	    74	          ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
  2039	    75	        WHERE i.indrelid = (quote_ident(%s) || '.' || quote_ident(%s))::regclass
  2040	    76	          AND i.indisprimary
  2041	    77	        ORDER BY array_position(i.indkey::int2[], a.attnum)
  2042	    78	        """,
  2043	    79	        (schema, table),
  2044	    80	    ).fetchall()
  2045	    81	    if not rows:
  2046	    82	        raise MigrationError(
  2047	    83	            f"{schema}.{table} has no primary key, so its rows cannot be put in a "
  2048	    84	            "deterministic order and no content digest can be taken. Every "
  2049	    85	            "new-core table has one; this is a real finding, not a tooling gap."
  2050	    86	        )
  2051	    87	    return [r[0] for r in rows]
  2052	    88	
  2053	    89	
  2054	    90	def _probe(conn, table: str) -> dict:
  2055	    91	    """(schema, rows, digest) for `table`, wherever it currently lives."""
  2056	    92	    schema = _schema_of(conn, table)
  2057	    93	    if schema is None:
  2058	    94	        return {"schema": None, "rows": None, "digest": None}
  2059	    95	    pk = _pk_columns(conn, schema, table)
  2060	    96	    row_json = sql.SQL("to_jsonb(t)")
  2061	    97	    for column in DIGEST_EXCLUDED_COLUMNS:
  2062	    98	        row_json = sql.SQL("({row_json} - {column})").format(
  2063	    99	            row_json=row_json, column=sql.Literal(column)
  2064	   100	        )
  2065	   101	    query = sql.SQL(
  2066	   102	        "SELECT count(*), "
  2067	   103	        "md5(coalesce(string_agg(({row_json})::text, '|' ORDER BY {order}), '')) "
  2068	   104	        "FROM {rel} AS t"
  2069	   105	    ).format(
  2070	   106	        row_json=row_json,
  2071	   107	        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
  2072	   108	        rel=sql.Identifier(schema, table),
  2073	   109	    )
  2074	   110	    rows, digest = conn.execute(query).fetchone()
  2075	   111	    return {"schema": schema, "rows": int(rows), "digest": digest}
  2076	   112	
  2077	   113	
  2078	   114	def _probe_all(conn) -> dict[str, dict]:
  2079	   115	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
  2080	   116	    return {t: _probe(conn, t) for t in sorted(tables)}
  2081	   117	
  2082	   118	
  2083	   119	def _print_proof(before: dict[str, dict], after: dict[str, dict]) -> int:
  2084	   120	    """Render the proof table. Returns the number of CHANGED digests."""
  2085	   121	    tables = {**MOVED_TABLES, **SEEDED_TABLES}
  2086	   122	    header = (
  2087	   123	        f"{'table':<20} {'side':<7} {'schema before -> after':<26} "
  2088	   124	        f"{'rows':<15} {'digest before -> after':<21} verdict"
  2089	   125	    )
  2090	   126	    print(header)
  2091	   127	    print("-" * len(header))
  2092	   128	    changed = 0
  2093	   129	    for name in sorted(tables):
  2094	   130	        b, a = before[name], after[name]
  2095	   131	        where = f"{b['schema'] or '-'} -> {a['schema'] or '-'}"
  2096	   132	        rows = f"{'-' if b['rows'] is None else b['rows']} -> " \
  2097	   133	               f"{'-' if a['rows'] is None else a['rows']}"
  2098	   134	        dig = f"{(b['digest'] or '-')[:8]} -> {(a['digest'] or '-')[:8]}"
  2099	   135	        if b["schema"] is None and a["schema"] is None:
  2100	   136	            verdict = "ABSENT"
  2101	   137	        elif b["digest"] == a["digest"] and b["rows"] == a["rows"]:
  2102	   138	            verdict = "OK"
  2103	   139	        elif b["schema"] is None:
  2104	   140	            verdict = "CREATED"
  2105	   141	        else:
  2106	   142	            verdict = "CHANGED"
  2107	   143	            changed += 1
  2108	   144	        print(
  2109	   145	            f"{name:<20} {tables[name].value:<7} {where:<26} {rows:<15} "
  2110	   146	            f"{dig:<21} {verdict}"
  2111	   147	        )
  2112	   148	    print("-" * len(header))
  2113	   149	    print(
  2114	   150	        f"{len(tables)} table(s) proven; digest excludes "
  2115	   151	        f"{', '.join(DIGEST_EXCLUDED_COLUMNS)}. "
  2116	   152	        + ("content UNCHANGED on every table."
  2117	   153	           if changed == 0
  2118	   154	           else f"{changed} table(s) CHANGED — investigate before proceeding.")
  2119	   155	    )
  2120	   156	    return changed
  2121	   157	
  2122	   158	
  2123	   159	def _apply(conn, paths) -> None:
  2124	   160	    """Run whole .sql files, one transaction for the lot.
  2125	   161	
  2126	   162	    Each file is handed to the server ENTIRE rather than split on ';':
  2127	   163	    these migrations are DO blocks, and a splitter would cut them at the
  2128	   164	    first semicolon inside the body. psycopg uses the simple query
  2129	   165	    protocol when there are no parameters, which accepts multiple
  2130	   166	    statements — and the migrations take no parameters by design.
  2131	   167	    """
  2132	   168	    for path in paths:
  2133	   169	        print(f"-- applying {path.name}")
  2134	   170	        conn.execute(path.read_text())
  2135	   171	
  2136	   172	
  2137	   173	def cmd_migrate(args: argparse.Namespace) -> None:
  2138	   174	    dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()
  2139	   175	    direction = "ROLLBACK" if args.rollback else "FORWARD"
  2140	   176	    paths = REVERSE if args.rollback else FORWARD
  2141	   177	
  2142	   178	    print(f"cobalt db migrate — {direction} on {dbname}")
  2143	   179	    conn = db.connect_migration(dbname, allow_prod=args.allow_prod)
  2144	   180	    conn.autocommit = False
  2145	   181	    try:
  2146	   182	        before = _probe_all(conn)
  2147	   183	        _apply(conn, paths)
  2148	   184	        after = _probe_all(conn)
  2149	   185	        conn.commit()
  2150	   186	    except BaseException:
  2151	   187	        conn.rollback()
  2152	   188	        raise
  2153	   189	    finally:
  2154	   190	        conn.close()
  2155	   191	
  2156	   192	    print()
  2157	   193	    changed = _print_proof(before, after)
  2158	   194	    if changed:
  2159	   195	        raise MigrationError(
  2160	   196	            f"{changed} table(s) changed content across the migration. The "
  2161	   197	            "migration is committed; the proof is not clean — compare against the "
  2162	   198	            "pg_dump taken before this run."
  2163	   199	        )
  2164	   200	
  2165	   201	
  2166	   202	def add_parser(sub) -> None:
  2167	   203	    group = sub.add_parser("db", help="Database migrations (ADR-0008 two-layer model)")
  2168	   204	    gsub = group.add_subparsers(dest="command", required=True)
  2169	   205	
  2170	   206	    migrate = gsub.add_parser(
  2171	   207	        "migrate",
  2172	   208	        help="Create the system/\"user\" schemas and move every new-core table.",
  2173	   209	    )
  2174	   210	    migrate.add_argument(
  2175	   211	        "--allow-prod",
  2176	   212	        action="store_true",
  2177	   213	        help="Target cobalt_brain (run from ~/cobalt only, outside market hours).",
  2178	   214	    )
  2179	   215	    migrate.add_argument(
  2180	   216	        "--rollback",
  2181	   217	        action="store_true",
  2182	   218	        help="Reverse registered migrations: heartbeat columns dropped, tables moved to public.",
  2183	   219	    )
  2184	   220	    migrate.set_defaults(func=cmd_migrate)
  2185	   221	
  2186	   222	
  2187	   223	__all__ = ["MigrationError", "add_parser", "cmd_migrate"]
  2188	"""The two-layer data model's migrations (ADR-0008).
  2189	
  2190	`0001_schemas.sql`  — schemas, roles, grants, ownership, `"user".traders`,
  2191	                      the `cobalt.trader_id` GUC convention.
  2192	`0002_move_tables.sql` — every new-core table onto its side, plus
  2193	                      `user_id` on the user side.
  2194	`0002_move_tables.rollback.sql` — the reverse, catalog-only.
  2195	`0003_heartbeat_vault_outcome.sql` — durable heartbeat vault delivery.
  2196	`0003_heartbeat_vault_outcome.rollback.sql` — removes those two columns.
  2197	
  2198	These are the DATABASE-WIDE migrations and they are the only ones that
  2199	live outside a feature module. A module's own DDL still lives in its own
  2200	`migrations/` directory and is still executed by its store's
  2201	`ensure_schema()`; those files create tables UNQUALIFIED and land them in
  2202	whichever schema the factory pinned on the connection.
  2203	
  2204	Run them with `cobalt db migrate` (`--allow-prod` from ~/cobalt only,
  2205	`--rollback` to reverse 0003 then 0002). Nothing runs them implicitly: a store's
  2206	`ensure_schema()` asserts the schemas exist and tells you to run the CLI.
  2207	"""
  2208	
  2209	from pathlib import Path
  2210	
  2211	MIGRATIONS_DIR = Path(__file__).parent
  2212	
  2213	#: Applied in this order, every time, both idempotent.
  2214	FORWARD = (
  2215	    MIGRATIONS_DIR / "0001_schemas.sql",
  2216	    MIGRATIONS_DIR / "0002_move_tables.sql",
  2217	    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
  2218	)
  2219	
  2220	#: `--rollback`, newest first. 0001 is deliberately NOT reversed.
  2221	REVERSE = (
  2222	    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
  2223	    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
  2224	)
  2225	
  2226	__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]
  2227	    70	    "drc_rows": Side.USER,
  2228	    71	    "prediction_records": Side.USER,
  2229	    72	    # S2-P1 — the radar. System: the pool and its membership history are
  2230	    73	    # engine artefacts any trader's strategies plug into.
  2231	    74	    "radar_pool": Side.SYSTEM,
  2232	    75	    "radar_membership": Side.SYSTEM,
  2233	    76	    # S2-P2 — taxonomy anatomy instances (regime, range, gap, extension,
  2234	    77	    # leg, session clock). The anatomy IS the system.
  2235	    78	    "anatomy_instances": Side.SYSTEM,
  2236	    79	}
  2237	    80	
  2238	    81	#: Every table this codebase has ruled on.
  2239	    82	PLACEMENT: dict[str, Side] = {
  2240	    83	    **MOVED_TABLES,
  2241	    84	    **SEEDED_TABLES,
  2242	    85	    **MODULE_TABLES,
  2243	    86	    **DECLARED_TABLES,
  2244	    87	}
  2245	    88	
  2246	    89	#: The old tree's tables, frozen in `public` and never touched
  2247	    90	#: (strangler rule). They exist in `cobalt_brain`; `cobalt_dev` has none
  2248	    91	#: of them, so the test asserts containment, not equality.
  2249	    92	OLD_TREE_PUBLIC_TABLES: frozenset[str] = frozenset({
  2250	    93	    "memory_logs",
  2251	    94	    "graph_nodes",
  2252	    95	    "graph_edges",
  2253	    96	    "hitl_proposals",
  2254	    97	    "browser_fast_path",
  2255	    98	    "instruments",
  2256	    99	    "market_snapshots",
  2257	   100	    "daily_in_play",
  2258	   101	    "key_levels",
  2259	   102	    "news_events",
  2260	   103	    "news_mentions",
  2261	   104	    "order_fills",
  2262	   105	    "strategy_signals",
  2263	   106	    "system_alerts",
  2264	   107	    "themes",
  2265	   108	    "trades",
  2266	   109	    "trading_accounts",
  2267	   110	})
  2268	   111	
  2269	   112	
  2270	   113	def side_of(table: str) -> Side:
  2271	   114	    """The ruled side of `table`, or a loud failure naming this file."""
  2272	   115	    try:
  2273	   116	        return PLACEMENT[table]
  2274	   117	    except KeyError:
  2275	   118	        raise KeyError(
  2276	   119	            f"table {table!r} has no ruled side. Every new table is declared on "
  2277	   120	            "exactly one side in cobalt/db_migrations/placement.py (ADR-0008 D2) "
  2278	   121	            "before it is created."
  2279	   122	        ) from None
  2280	   123	
  2281	   124	
  2282	   125	def tables_on(side: Side) -> frozenset[str]:
  2283	   126	    """Every ruled table on `side`, declared-but-unbuilt ones included."""
  2284	   127	    return frozenset(t for t, s in PLACEMENT.items() if s is side)
  2285	   128	
  2286	   129	
  2287	   130	__all__ = [
  2288	   131	    "DECLARED_TABLES",
  2289	   132	    "MODULE_TABLES",
  2290	   133	    "MOVED_TABLES",
  2291	   134	    "OLD_TREE_PUBLIC_TABLES",
  2292	   135	    "PLACEMENT",
  2293	   136	    "SEEDED_TABLES",
  2294	   137	    "side_of",
  2295	   138	    "tables_on",
  2296	   139	]
  2297	
  2298	exec
  2299	/bin/zsh -lc "nl -ba src/cobalt/archiver/store.py | sed -n '45,155p'; nl -ba src/cobalt/settings/store.py | sed -n '35,100p'; rg -n 'attest|day_modes|INSERT INTO|def insert' src/cobalt/aset/store.py src/cobalt/aset/web.py src/cobalt/daymode/store.py; nl -ba src/cobalt/jobs/watchdog.py | sed -n '410,455p'; nl -ba src/cobalt/session/guard.py | sed -n '35,135p'; git status --short; rg -n 'i1|14 calendar|timestamp' 'docs/30 - Design/DATA-SOURCE-MEMO.md' | tail -15" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
  2300	 succeeded in 0ms:
  2301	    45	        with self._connect() as conn:
  2302	    46	            db.assert_schemas_exist(conn)
  2303	    47	            conn.execute(MIGRATION_SQL.read_text())
  2304	    48	
  2305	    49	    def upsert_bars(self, bars: list[Bar]) -> int:
  2306	    50	        """Insert or refresh `bars`. Returns the number of rows written.
  2307	    51	
  2308	    52	        ON CONFLICT DO UPDATE (not DO NOTHING): a re-run refreshes a bar
  2309	    53	        that Finviz may have finalized/revised since the last pull,
  2310	    54	        rather than freezing it at its first-seen (possibly provisional)
  2311	    55	        values. PK (ticker, interval, ts) makes this a true idempotent
  2312	    56	        upsert either way — no duplicates, ever.
  2313	    57	        """
  2314	    58	        if not bars:
  2315	    59	            return 0
  2316	    60	        rows = [
  2317	    61	            (
  2318	    62	                b.ticker,
  2319	    63	                b.interval.value,
  2320	    64	                b.ts,
  2321	    65	                b.open,
  2322	    66	                b.high,
  2323	    67	                b.low,
  2324	    68	                b.close,
  2325	    69	                b.volume,
  2326	    70	            )
  2327	    71	            for b in bars
  2328	    72	        ]
  2329	    73	        with self._connect() as conn:
  2330	    74	            with conn.cursor() as cur:
  2331	    75	                cur.executemany(
  2332	    76	                    """
  2333	    77	                    INSERT INTO bars (ticker, interval, ts, open, high, low, close, volume)
  2334	    78	                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
  2335	    79	                    ON CONFLICT (ticker, interval, ts) DO UPDATE SET
  2336	    80	                        open = EXCLUDED.open,
  2337	    81	                        high = EXCLUDED.high,
  2338	    82	                        low = EXCLUDED.low,
  2339	    83	                        close = EXCLUDED.close,
  2340	    84	                        volume = EXCLUDED.volume
  2341	    85	                    """,
  2342	    86	                    rows,
  2343	    87	                )
  2344	    88	        return len(rows)
  2345	    89	
  2346	    90	    def count_rows(self) -> int:
  2347	    91	        with self._connect() as conn:
  2348	    92	            row = conn.execute("SELECT count(*) FROM bars").fetchone()
  2349	    93	        return int(row[0]) if row else 0
  2350	    35	        return db.connect(self.db_name, side=self.SIDE)
  2351	    36	
  2352	    37	    def ensure_schema(self) -> None:
  2353	    38	        with self._connect() as conn:
  2354	    39	            db.assert_schemas_exist(conn)
  2355	    40	            for migration in sorted(MIGRATIONS_DIR.glob("*.sql")):
  2356	    41	                conn.execute(migration.read_text())
  2357	    42	
  2358	    43	    # -- reads --------------------------------------------------------
  2359	    44	
  2360	    45	    def rows(self) -> list[dict[str, Any]]:
  2361	    46	        with self._connect() as conn:
  2362	    47	            cur = conn.execute(
  2363	    48	                "SELECT key, value, source, updated_at FROM trader_settings "
  2364	    49	                "ORDER BY key"
  2365	    50	            )
  2366	    51	            columns = [d.name for d in cur.description]
  2367	    52	            return [dict(zip(columns, r)) for r in cur.fetchall()]
  2368	    53	
  2369	    54	    def values(self) -> dict[str, Any]:
  2370	    55	        """`{key: value}` — what `TraderSettings.from_db` builds from."""
  2371	    56	        return {row["key"]: row["value"] for row in self.rows()}
  2372	    57	
  2373	    58	    # -- the one write path -------------------------------------------
  2374	    59	
  2375	    60	    def put(self, rows: dict[str, Any], *, source: str) -> dict[str, str]:
  2376	    61	        """Upsert every setting in `rows`. Returns `{key: created|updated
  2377	    62	        |unchanged}` so the caller can report what actually moved.
  2378	    63	
  2379	    64	        One transaction: a half-applied settings load is a config that
  2380	    65	        validates nowhere, which is the failure the per-top-level-setting
  2381	    66	        row layout was chosen to avoid in the first place.
  2382	    67	        """
  2383	    68	        before = self.values()
  2384	    69	        outcome: dict[str, str] = {}
  2385	    70	        conn = self._connect()
  2386	    71	        conn.autocommit = False
  2387	    72	        try:
  2388	    73	            with conn.cursor() as cur:
  2389	    74	                for key, value in rows.items():
  2390	    75	                    if key in before and before[key] == value:
  2391	    76	                        outcome[key] = "unchanged"
  2392	    77	                        continue
  2393	    78	                    outcome[key] = "updated" if key in before else "created"
  2394	    79	                    cur.execute(
  2395	    80	                        """
  2396	    81	                        INSERT INTO trader_settings (key, value, source, updated_at)
  2397	    82	                        VALUES (%s, %s::jsonb, %s, now())
  2398	    83	                        ON CONFLICT (user_id, key) DO UPDATE SET
  2399	    84	                            value = EXCLUDED.value,
  2400	    85	                            source = EXCLUDED.source,
  2401	    86	                            updated_at = EXCLUDED.updated_at
  2402	    87	                        """,
  2403	    88	                        (key, json.dumps(value), source),
  2404	    89	                    )
  2405	    90	            conn.commit()
  2406	    91	        except BaseException:
  2407	    92	            conn.rollback()
  2408	    93	            raise
  2409	    94	        finally:
  2410	    95	            conn.close()
  2411	    96	        return outcome
  2412	    97	
  2413	    98	
  2414	    99	__all__ = ["MIGRATIONS_DIR", "TraderSettingsStore"]
  2415	src/cobalt/aset/web.py:122: .attest{display:flex;gap:8px;align-items:center;margin-top:8px}
  2416	src/cobalt/aset/web.py:123: .attest select{flex:1}
  2417	src/cobalt/aset/web.py:124: .attest button{margin-top:0;white-space:nowrap}
  2418	src/cobalt/aset/web.py:366:    # except the .htk"), and the .htk he attested has to agree with it.
  2419	src/cobalt/aset/web.py:430:# F6 day-mode banner + attestation, F7 card controls (S1-P2)
  2420	src/cobalt/aset/web.py:455:def _read_back_note_attestation(cfg, day, row: dict | None, store) -> dict | None:
  2421	src/cobalt/aset/web.py:458:    A box he ticked in today's daily note IS an attestation, read at
  2422	src/cobalt/aset/web.py:460:    the record (persisted through the same `attest_sheet` the selector
  2423	src/cobalt/aset/web.py:470:    note = daymode_note.read_attestation(path.read_text(encoding="utf-8"), cfg)
  2424	src/cobalt/aset/web.py:473:    settled = daymode_note.reconcile(note, (row or {}).get("attested_sheet"))
  2425	src/cobalt/aset/web.py:474:    if settled and settled != (row or {}).get("attested_sheet"):
  2426	src/cobalt/aset/web.py:475:        store.attest_sheet(day, filename=settled)
  2427	src/cobalt/aset/web.py:477:            "daymode: attestation {} read back from the daily note {}", settled, path
  2428	src/cobalt/aset/web.py:499:        row = _read_back_note_attestation(cfg, day, row, store)
  2429	src/cobalt/aset/web.py:506:        logger.error("daymode: note/selector attestation conflict: {}", e)
  2430	src/cobalt/aset/web.py:516:    status suffix for the banner; never raises — an attestation that
  2431	src/cobalt/aset/web.py:519:    reason to lose the attestation."""
  2432	src/cobalt/aset/web.py:527:            attested=(row or {}).get("attested_sheet"),
  2433	src/cobalt/aset/web.py:534:        logger.error("daymode note write FAILED (attestation stands): {}", e)
  2434	src/cobalt/aset/web.py:547:    attested = (row or {}).get("attested_sheet")
  2435	src/cobalt/aset/web.py:553:        match_html = f'<span style="color:#24d986">✓ {e(attested)} matches</span>'
  2436	src/cobalt/aset/web.py:566:        f'<span class="muted">(attested, not read — Cobalt never touches DAS)</span></div>',
  2437	src/cobalt/aset/web.py:581:        f'<option value="{e(f)}"{" selected" if f == attested else ""}>{e(f)}</option>'
  2438	src/cobalt/aset/web.py:585:        '<form class="attest" method="post" action="/attest">'
  2439	src/cobalt/aset/web.py:891:                attested=None, mode="(unresolved)",
  2440	src/cobalt/aset/web.py:906:        # Two separate refusals — the attested sheet must BE the mode in
  2441	src/cobalt/aset/web.py:1061:@app.post("/attest", response_class=HTMLResponse)
  2442	src/cobalt/aset/web.py:1062:async def attest(request: Request) -> str:
  2443	src/cobalt/aset/web.py:1078:                attested=None, mode="(none)",
  2444	src/cobalt/aset/web.py:1084:        store.attest_sheet(day, filename=filename)
  2445	src/cobalt/daymode/store.py:1:"""F6 persistence: one `day_modes` row per trading day.
  2446	src/cobalt/daymode/store.py:57:            cur = conn.execute("SELECT * FROM day_modes WHERE trade_date = %s", (day,))
  2447	src/cobalt/daymode/store.py:81:                "INSERT INTO day_modes (trade_date, stage, proposed, reason, session, created_at) "
  2448	src/cobalt/daymode/store.py:108:                f"no day_modes row for {day} — there is nothing to decide yet. "
  2449	src/cobalt/daymode/store.py:114:                "early `.htk` attestation, while stage 1 was still in force. There is "
  2450	src/cobalt/daymode/store.py:126:                "UPDATE day_modes SET decided = %s, decided_by = %s, decided_at = %s, "
  2451	src/cobalt/daymode/store.py:132:    def attest_sheet(
  2452	src/cobalt/daymode/store.py:138:        exists so he can attest before 09:00, while stage 1 is still in
  2453	src/cobalt/daymode/store.py:142:        session = assert_writable("daymode.attest", target=day.isoformat(), now=ts)
  2454	src/cobalt/daymode/store.py:145:                "INSERT INTO day_modes (trade_date, stage, proposed, reason, session, "
  2455	src/cobalt/daymode/store.py:146:                "attested_sheet, attested_at) "
  2456	src/cobalt/daymode/store.py:149:                "attested_sheet = EXCLUDED.attested_sheet, attested_at = EXCLUDED.attested_at",
  2457	src/cobalt/daymode/store.py:153:                    "attested before any proposal — stage 1 in force",
  2458	src/cobalt/daymode/store.py:164:                "attested_sheet, reason FROM day_modes ORDER BY trade_date DESC LIMIT %s",
  2459	src/cobalt/aset/store.py:109:                    INSERT INTO aset_sizings (
  2460	   410	        # -- jobs the wrapper reports on -------------------------------
  2461	   411	        state = row["state"]
  2462	   412	
  2463	   413	        if state == JobState.RUNNING.value:
  2464	   414	            started, beat = row["started_at"], row["heartbeat_at"]
  2465	   415	            ran_for = (ts - started).total_seconds() if started else 0
  2466	   416	            stale_for = (ts - beat).total_seconds() if beat else None
  2467	   417	            stale_limit = spec.timeout_s / fraction
  2468	   418	            if ran_for > spec.timeout_s and (stale_for is None or stale_for > stale_limit):
  2469	   419	                reason = (
  2470	   420	                    f"ZOMBIE: running {ran_for / 60:.0f} min (timeout "
  2471	   421	                    f"{spec.timeout_s / 60:.0f} min) and the heartbeat is "
  2472	   422	                    + (f"{stale_for / 60:.0f} min stale" if stale_for else "missing")
  2473	   423	                    + f" (limit {stale_limit / 60:.0f} min). The beater thread dies "
  2474	   424	                    "with its process, so a stale stamp means the process is gone."
  2475	   425	                )
  2476	   426	                store.mark_zombie(spec.label, reason=reason)
  2477	   427	                findings.append(Finding(spec.label, False, JobState.ZOMBIE.value, reason))
  2478	   428	            else:
  2479	   429	                findings.append(
  2480	   430	                    Finding(spec.label, True, state,
  2481	   431	                            f"running {ran_for / 60:.0f} min, heartbeat fresh")
  2482	   432	                )
  2483	   433	            continue
  2484	   434	
  2485	   435	        if state in {s.value for s in RED_STATES}:
  2486	   436	            findings.append(
  2487	   437	                Finding(spec.label, False, state,
  2488	   438	                        (row["last_error"] or "no error text recorded")[:300])
  2489	   439	            )
  2490	   440	            continue
  2491	   441	
  2492	   442	        # -- MISSED: a fact about an absent run, not a state -----------
  2493	   443	        if spec.kind is JobKind.ONE_SHOT:
  2494	   444	            missed, detail = is_missed(spec, row, now_et=now_et, grace=grace)
  2495	   445	            if missed:
  2496	   446	                findings.append(Finding(spec.label, False, f"{state} (MISSED)", detail))
  2497	   447	                continue
  2498	   448	
  2499	   449	        launchd_note = (
  2500	   450	            f" · launchd: loaded, last exit {status.last_exit}"
  2501	   451	            if probe and status.last_exit is not None else " · launchd: loaded"
  2502	   452	        ) if probe else ""
  2503	   453	        findings.append(
  2504	   454	            Finding(
  2505	   455	                spec.label, True, state,
  2506	    35	from . import clock as clock_mod
  2507	    36	from .clock import ET, SessionClock, session_clock
  2508	    37	from .models import BLOCKED_SESSION, Session
  2509	    38	from .store import SessionBlockStore
  2510	    39	
  2511	    40	
  2512	    41	class SessionBlocked(RuntimeError):
  2513	    42	    """A write was refused because of the session it was attempted in."""
  2514	    43	
  2515	    44	    def __init__(self, message: str, *, session: Session, actor: str):
  2516	    45	        super().__init__(message)
  2517	    46	        self.session = session
  2518	    47	        self.actor = actor
  2519	    48	
  2520	    49	
  2521	    50	def block_message(clock: SessionClock, ts: datetime, actor: str) -> str:
  2522	    51	    """The one loud line. Names the window, the clock, and the lift."""
  2523	    52	    et = clock.to_et(ts)
  2524	    53	    lifts_at, next_session = clock.next_boundary(ts)
  2525	    54	    return (
  2526	    55	        f"REFUSED ({actor}): it is {et:%H:%M:%S} ET on {et:%Y-%m-%d} — inside "
  2527	    56	        f"MARKET RESET, the {_window_text(clock)} ET hard block. Cobalt writes "
  2528	    57	        f"nothing in this window: the day's record is closing and the bar "
  2529	    58	        f"archiver runs inside it. The block lifts at "
  2530	    59	        f"{lifts_at.astimezone(ET):%H:%M} ET ({next_session})."
  2531	    60	    )
  2532	    61	
  2533	    62	
  2534	    63	def _window_text(clock: SessionClock) -> str:
  2535	    64	    windows = {w.session: w for w in clock.windows_for(clock_mod.now_utc().astimezone(ET).date())}
  2536	    65	    window = windows.get(BLOCKED_SESSION)
  2537	    66	    if window is None:  # today is closed; read the boundaries directly
  2538	    67	        return "20:00-21:00"
  2539	    68	    return f"{window.start:%H:%M}-{window.end:%H:%M}"
  2540	    69	
  2541	    70	
  2542	    71	def note_ungated(
  2543	    72	    actor: str,
  2544	    73	    *,
  2545	    74	    target: Optional[str] = None,
  2546	    75	    why: str,
  2547	    76	    now: Optional[datetime] = None,
  2548	    77	    clock: Optional[SessionClock] = None,
  2549	    78	    store: Optional[SessionBlockStore] = None,
  2550	    79	) -> Session:
  2551	    80	    """Migration/repair tooling ran inside the block. Say so, loudly.
  2552	    81	
  2553	    82	    RULED 2026-09-04 (S1-P3, decided-with-veto): migration and repair
  2554	    83	    tooling stays UNGATED in `market_reset`. `VaultWriter.restore` and
  2555	    84	    `CardStore.backfill` already carried that carve-out in comments; the
  2556	    85	    reasoning is the same in both — locking recovery out for the
  2557	    86	    20:00-21:00 window would mean the one hour you most need to repair
  2558	    87	    state is the hour you cannot. Card CREATION stays refused: that is
  2559	    88	    trading record, and the block exists for it.
  2560	    89	
  2561	    90	    The price of the carve-out is that it may never happen QUIETLY. Every
  2562	    91	    such run inside the window logs ONE LOUD LINE and increments the same
  2563	    92	    counter F18 displays, tagged `ungated_run` so a repair is never read
  2564	    93	    as a refusal.
  2565	    94	
  2566	    95	    OUTSIDE the window this does nothing at all — no log line, no row. A
  2567	    96	    backfill at two in the afternoon is not an event.
  2568	    97	    """
  2569	    98	    clock = clock or session_clock()
  2570	    99	    ts = now or clock_mod.now_utc()
  2571	   100	    session = clock.session(ts)
  2572	   101	    if session is not BLOCKED_SESSION:
  2573	   102	        return session
  2574	   103	
  2575	   104	    et = clock.to_et(ts)
  2576	   105	    message = (
  2577	   106	        f"UNGATED ({actor}): it is {et:%H:%M:%S} ET on {et:%Y-%m-%d} — inside "
  2578	   107	        f"MARKET RESET, where every ordinary write is refused. This ran anyway "
  2579	   108	        f"under the migration/repair carve-out (ruled 2026-09-04): {why}. It is "
  2580	   109	        "counted on the heartbeat so that a repair inside the block can never be "
  2581	   110	        "a quiet one."
  2582	   111	    )
  2583	   112	    logger.error(message)
  2584	   113	    (store or SessionBlockStore()).record(
  2585	   114	        session=session.value,
  2586	   115	        actor=actor,
  2587	   116	        target=target,
  2588	   117	        reason=message,
  2589	   118	        kind=SessionBlockStore.UNGATED_RUN,
  2590	   119	    )
  2591	   120	    return session
  2592	   121	
  2593	   122	
  2594	   123	def assert_writable(
  2595	   124	    actor: str,
  2596	   125	    *,
  2597	   126	    target: Optional[str] = None,
  2598	   127	    now: Optional[datetime] = None,
  2599	   128	    clock: Optional[SessionClock] = None,
  2600	   129	    store: Optional[SessionBlockStore] = None,
  2601	   130	) -> Session:
  2602	   131	    """Refuse the caller if the session forbids writing; else return it.
  2603	   132	
  2604	   133	    `actor` names the write site ("vaultwrite", "aset.card", ...) and is
  2605	   134	    what the refusal message, the log line and the counter row all carry.
  2606	   135	    `now` is the seam the F1 tests freeze — production passes nothing and
  2607	 M "docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md"
  2608	 M "docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md"
  2609	?? "docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r1.md"
  2610	?? "docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md"
  2611	244:  timestamps carry HH:MM, granularity between consecutive rows matches
  2612	247:  size monotonically: `{i1, i5}` ≈ 2–3 weeks (with premarket/after-hours
  2613	248:  included), `{i15}` ≈ 3 weeks (regular hours only — the extended-hours
  2614	249:  cutoff happens between `i5` and `i15`), `{i30, h}` ≈ **9.6 months**
  2615	253:  daily — they are not shorthand for `i5`/`i15`/etc. Anyone guessing
  2616	268:(2522-row baseline) or `p=i1` (9451-row baseline), returned **exactly
  2617	273:on `p=i1` specifically (in case date-range only applies to intraday,
  2618	336:| **Stock** | 6-col OHLCV at 8 real granularities (d/w/m/i1/i5/i15/i30/h); volume present everywhere; depth tiers empirically mapped | **History-depth param name unconfirmed** (highest-priority Phase B item) | **Critical** — setups engine + backtesting both depend on this |
  2619	412:Slots into the same depth tier as `i1`/`i5` (~2 weeks, premarket
  2620	416:same ~2-week live-detection window as `i1`/`i5`, no depth penalty for
  2621	417:using `i2` over `i1`.
  2622	419:**Fresh `i1`/`i5` re-pull** (same day, ~50 minutes after the original
  2623	425:| `i1` | 9451 rows, starts 04:00 AM | 9499 rows, starts 04:00 AM | ✅ start time unchanged; row count grew by 48 — matches ~48 new 1-min bars accumulating in the ~48-minute gap between probes (a good internal consistency check that this is a live, continuously-updating feed, not a cached/stale snapshot) |
  2624	546:| **Stock**          | 6-col OHLCV at **9** real granularities (i1/i2/i5/i15/i30/h/d/w/m); volume present everywhere; depth tiers empirically mapped and re-verified stable across a fresh pull                          | History-depth param name still unconfirmed (Phase B's top item, unchanged)                               | **Critical** — `i2` is Dejan's actual trading timeframe and is now confirmed in the same ~2-week live-detection tier as `i1`/`i5` |
  2625	604:identically on `i1`/`i5`/`i15` (only `i2` and `i30` were probed); the
  2626	
  2627	codex
  2628	**BLOCKERS (file:line)**
  2629	
  2630	Paths below are under `docs/40 - DevDocs/reports/_inflight/`; `plan` = `plan-s2-p1-2026-09-10.md`, `brief` = `s2-p1-brief.md`.
  2631	
  2632	1. **Account-mode implementation contradicts E1.** `plan:137`, `plan:185`, `brief:272` explicitly permit UNSET cards. E1 (`plan:287`, `brief:344`) requires refusal, standing-setting fallback, and a per-day SIM control on sheet attestation. Rewrite implementation, acceptance tests, and LIVE initialization together; otherwise the build implements the opposite behavior.
  2633	
  2634	2. **E2/E8’s pool block cannot pass the specified parser.** `plan:53`, `plan:56`, `brief:177` accept only screen blocks in the Screens note, with extra fields forbidden. E2/E8 require a pool block there. Meanwhile `plan:124`, `plan:157`, `plan:158`, and `brief:167` retain competing rank/cap definitions in committed configuration. Add a validated pool contract, user-side mirror, synthetic fixture, and proposal/writer integration; remove competing trader-specific defaults. This follows ADR-0008’s distinction between engine configuration and trader settings.
  2635	
  2636	3. **The ruled ranking algorithm remains incomplete.** `plan:293` specifies premarket/RTH metrics but enables aftermarket at `plan:122`; mixed volume/RVOL screen results have no defined comparison. `plan:299` requires three-scan stickiness while `plan:218` excludes hysteresis. Define ordering, streak reset/persistence, and precedence among stickiness, degraded holds, manual exclusion, and cap reductions. Lowering the vault cap below held membership also defeats `plan:124`’s claimed cap invariant.
  2637	
  2638	4. **Credential instructions directly violate E7.** `brief:17`, `brief:84`, and `plan:254` instruct the hub to export DB credentials into Sol’s environment. `plan:189` and `brief:292` assign DB smoke to Sol. E7 forbids both. Remove those instructions and explicitly split offline checks from hub-owned DB acceptance gates.
  2639	
  2640	5. **Restart instructions still contradict E6.** `plan:204` and `brief:79` say code changes require no restart; `plan:231` hard-codes only ASET. E6 requires import-based resident analysis with all residents as the fallback. Update the deployment and rollback commands from that analysis, not just the report checklist.
  2641	
  2642	6. **The market-reset “single commit” guarantee is incompatible with the write sequence.** `plan:122`, `brief:246` promise whole-cycle discard but perform pool/membership, bars, and mirror writes separately. `BarStore.upsert_bars` opens its own transaction (`src/cobalt/archiver/store.py:73`); `TraderSettingsStore.put` commits independently (`src/cobalt/settings/store.py:90`). ADR-0008 requires separate side connections. A check before the first commit cannot prevent subsequent writes crossing 20:00 or undo earlier commits. Specify achievable transaction boundaries and test crossing the boundary between store writes.
  2643	
  2644	7. **E4 can require a schema change after stage-1 deployment.** `plan:303`, `plan:307` defer the comparison to LIVE, but `plan:53` forbids `ft`, and `plan:123` omits it from requests. If ticker sets differ, the approved proposal cannot run through the deployed contract. Ship optional validated `ft` support beforehand, or explicitly stop rollout for a code revision and review.
  2645	
  2646	8. **The throttle probe cannot observe its required stop conditions through the mandated API.** `brief:114` requires `fetch_bars`; `brief:115` requires stopping on redirects and recording response metrics. The collector follows redirects (`src/cobalt/archiver/collector.py:166`) and returns only parsed bars (`:174`), hiding redirect history, status, and response bytes. Define a shared observable transport interface and test redirect refusal there.
  2647	
  2648	**RISKS**
  2649	
  2650	- `plan:130`: seed the watermark by **ticker and `interval='i1'`**, not ticker alone. Strict watermarks also defer corrections and missing older bars until archiving; the existing store explicitly supports revised bars.
  2651	- `brief:135`: adding created tables to migration proof also needs direction-aware handling of intentional drops. The current proof reports removal as `CHANGED` and raises **after commit** (`src/cobalt/db_migrations/cli.py:142`, `:193`).
  2652	- `plan:132`: a 60-second setting does not prove two polls per two-minute bar. Sequential network latency, full-export parsing, and token-bucket waits need an achieved-cadence acceptance threshold.
  2653	- `plan:153`: scan freshness does not establish bar freshness. Define how individual poll failures reach F18 while scans and the wrapper’s independent heartbeat remain healthy.
  2654	- `plan:304`: E5’s repo-wide exact-string check is broader than the tracked-directory grammar test at `plan:60`; both checks need explicit ownership before commits.
  2655	
  2656	**VERDICT: BLOCKED — revise before build.**
  2657	
  2658	The proposed table placement and J1 grants agree with ADR-0008. The disabled-job startup sequence also holds: `job_run` does not gate on `enabled`. The addendum, however, has not been integrated into executable instructions and acceptance criteria. This was a read-only review; no DB or live-network validation was run.
  2659	tokens used
  2660	59,721
  2661	**BLOCKERS (file:line)**
  2662	
  2663	Paths below are under `docs/40 - DevDocs/reports/_inflight/`; `plan` = `plan-s2-p1-2026-09-10.md`, `brief` = `s2-p1-brief.md`.
  2664	
  2665	1. **Account-mode implementation contradicts E1.** `plan:137`, `plan:185`, `brief:272` explicitly permit UNSET cards. E1 (`plan:287`, `brief:344`) requires refusal, standing-setting fallback, and a per-day SIM control on sheet attestation. Rewrite implementation, acceptance tests, and LIVE initialization together; otherwise the build implements the opposite behavior.
  2666	
  2667	2. **E2/E8’s pool block cannot pass the specified parser.** `plan:53`, `plan:56`, `brief:177` accept only screen blocks in the Screens note, with extra fields forbidden. E2/E8 require a pool block there. Meanwhile `plan:124`, `plan:157`, `plan:158`, and `brief:167` retain competing rank/cap definitions in committed configuration. Add a validated pool contract, user-side mirror, synthetic fixture, and proposal/writer integration; remove competing trader-specific defaults. This follows ADR-0008’s distinction between engine configuration and trader settings.
  2668	
  2669	3. **The ruled ranking algorithm remains incomplete.** `plan:293` specifies premarket/RTH metrics but enables aftermarket at `plan:122`; mixed volume/RVOL screen results have no defined comparison. `plan:299` requires three-scan stickiness while `plan:218` excludes hysteresis. Define ordering, streak reset/persistence, and precedence among stickiness, degraded holds, manual exclusion, and cap reductions. Lowering the vault cap below held membership also defeats `plan:124`’s claimed cap invariant.
  2670	
  2671	4. **Credential instructions directly violate E7.** `brief:17`, `brief:84`, and `plan:254` instruct the hub to export DB credentials into Sol’s environment. `plan:189` and `brief:292` assign DB smoke to Sol. E7 forbids both. Remove those instructions and explicitly split offline checks from hub-owned DB acceptance gates.
  2672	
  2673	5. **Restart instructions still contradict E6.** `plan:204` and `brief:79` say code changes require no restart; `plan:231` hard-codes only ASET. E6 requires import-based resident analysis with all residents as the fallback. Update the deployment and rollback commands from that analysis, not just the report checklist.
  2674	
  2675	6. **The market-reset “single commit” guarantee is incompatible with the write sequence.** `plan:122`, `brief:246` promise whole-cycle discard but perform pool/membership, bars, and mirror writes separately. `BarStore.upsert_bars` opens its own transaction (`src/cobalt/archiver/store.py:73`); `TraderSettingsStore.put` commits independently (`src/cobalt/settings/store.py:90`). ADR-0008 requires separate side connections. A check before the first commit cannot prevent subsequent writes crossing 20:00 or undo earlier commits. Specify achievable transaction boundaries and test crossing the boundary between store writes.
  2676	
  2677	7. **E4 can require a schema change after stage-1 deployment.** `plan:303`, `plan:307` defer the comparison to LIVE, but `plan:53` forbids `ft`, and `plan:123` omits it from requests. If ticker sets differ, the approved proposal cannot run through the deployed contract. Ship optional validated `ft` support beforehand, or explicitly stop rollout for a code revision and review.
  2678	
  2679	8. **The throttle probe cannot observe its required stop conditions through the mandated API.** `brief:114` requires `fetch_bars`; `brief:115` requires stopping on redirects and recording response metrics. The collector follows redirects (`src/cobalt/archiver/collector.py:166`) and returns only parsed bars (`:174`), hiding redirect history, status, and response bytes. Define a shared observable transport interface and test redirect refusal there.
  2680	
  2681	**RISKS**
  2682	
  2683	- `plan:130`: seed the watermark by **ticker and `interval='i1'`**, not ticker alone. Strict watermarks also defer corrections and missing older bars until archiving; the existing store explicitly supports revised bars.
  2684	- `brief:135`: adding created tables to migration proof also needs direction-aware handling of intentional drops. The current proof reports removal as `CHANGED` and raises **after commit** (`src/cobalt/db_migrations/cli.py:142`, `:193`).
  2685	- `plan:132`: a 60-second setting does not prove two polls per two-minute bar. Sequential network latency, full-export parsing, and token-bucket waits need an achieved-cadence acceptance threshold.
  2686	- `plan:153`: scan freshness does not establish bar freshness. Define how individual poll failures reach F18 while scans and the wrapper’s independent heartbeat remain healthy.
  2687	- `plan:304`: E5’s repo-wide exact-string check is broader than the tracked-directory grammar test at `plan:60`; both checks need explicit ownership before commits.
  2688	
  2689	**VERDICT: BLOCKED — revise before build.**
  2690	
  2691	The proposed table placement and J1 grants agree with ADR-0008. The disabled-job startup sequence also holds: `job_run` does not gate on `enabled`. The addendum, however, has not been integrated into executable instructions and acceptance criteria. This was a read-only review; no DB or live-network validation was run.
     1	# S2-P1 PLAN — Radar pool + Finviz bar poller (2026-09-10)
     2	
     3	Architect: Opus 5 (plan + brief, no build) · Reviewer: Codex `gpt-6-astra`, read-only, 3 rounds; the plan stands
     4	after round 3 (L39) · Branch `sprint-2/radar-pool`, rebased on `main` `16847eb` (heartbeat fix and `0003` merged) ·
     5	Worktree `~/cobalt-wt/s2-p1-radar-pool` · Build: Codex `gpt-5.6-sol`, no DB credentials · Hub: Sonnet · Sprint S2 = 09-10 → 09-23.
     6	
     7	## §0 Headline
     8	
     9	- Ships resident `com.cobalt.radar` (screens + static lists → a pool capped and ranked by the trader's own pool block, sticky), a Finviz i1 poller into `system.bars`, the account-mode stamp (card refused without one), J1, `cobalt db query`, `cobalt jobs restarts`, F18 `radar` probe.
    10	- Trader data lives only in two vault notes, mirrored user-side; committed config holds engine tunables only. The one vault write is hub-run after a HITL card.
    11	- Sol builds offline with no DB credentials; the hub runs migrations on cobalt_dev, the DB-backed suite and the dev-vault smoke. Two merge stages.
    12	- Rulings E1–E8 and decisions D1–D8 (09-10) are the body below (§R). ESCALATE: 3 (§8). Review: r1 no verdict, r2 BLOCKED (8), r3 final (§9).
    13	
    14	## §R Where each ruling lives
    15	
    16	| Ruling | Section |
    17	|---|---|
    18	| E1 account mode · D1 stamp order, refusal, sim switch | D8 |
    19	| E2 pool rule in the vault · D2 own block kind · D3 ranking + stickiness | D1, D2, D3 |
    20	| E3 tiers move as they are | D1, D13 |
    21	| E4 `ft=4` comparison · D7 optional `ft` now | D1, D13 |
    22	| E5 no real `f=` strings in any report/plan/review | D1 (suite test), §7 (hub exact-string check) |
    23	| E6 RESTARTS by rule · D5 derivation printed | §3, §6 |
    24	| E7 no DB credentials for Sol · D4 split | §3, D15 |
    25	| E8 vault write = propose → card → apply | D13 |
    26	| D6 per-store transactions, fixed order | D5 |
    27	| D8 observable throttle probe | D6, §4 |
    28	
    29	## Line 0 — ADR-0008 in force
    30	
    31	| Law | How P1 honours it | Evidence |
    32	|---|---|---|
    33	| Side per store | `RadarStore`, `BarStore`, `JobStore` → system; `TraderSettingsStore` (mirror, `aset.account_mode`), `AsetStore`, `DayModeStore` → user; one connection per side | ADR-0008:88-95 |
    34	| Placement | `radar_pool`, `radar_membership` move from `DECLARED_TABLES` to a new `CREATED_TABLES` (created by a db_migration on their side), carried by the placement test and the migrate proof | `placement.py:65-79`, ADR-0008:133 |
    35	| Cross-side FK | `"user".aset_sizings.pool_member_id → system.radar_membership(id)`, schema-qualified; `REFERENCES` granted | ADR-0008:126 |
    36	| Engine vs trader data | engine tunables in `tunables.yaml`; the pool rule, screens and lists are vault-note user data, mirrored into `"user".trader_settings` | ADR-0008:152-154 |
    37	| Fixed migration list, rollback SQL | `0004_radar_pool.sql` + `.rollback.sql` appended after `0003`; rollback bounded by `--down-to` | `db_migrations/__init__.py:27-37` |
    38	| `"user"` always quoted | `psycopg.sql.Identifier`; reserved-word lint | `test_tenancy.py` lint |
    39	
    40	## §1 Facts (verified read-only 09-10)
    41	
    42	| # | Fact | Evidence |
    43	|---|---|---|
    44	| F1 | Heartbeat fix merged: `FORWARD = (0001, 0002, 0003)`, `REVERSE = (0003, 0002)`. | `db_migrations/__init__.py:27-37` |
    45	| F2 | `--rollback` runs the whole `REVERSE` tuple; the proof is printed and raised AFTER commit; a table present→absent gets verdict `CHANGED`. | `db_migrations/cli.py:176,185,193-199,135-143` |
    46	| F3 | `cobalt_user` has SELECT on `system`, not REFERENCES. | `0001_schemas.sql` §4–§5 |
    47	| F4 | No live/sim value exists. `TraderSettings._build` fails only on a missing `SETTING_KEYS` row; extra rows cannot break the sheet. | `settings/models.py:29-43,70-71` |
    48	| F5 | Every card INSERT goes through `AsetStore.save`. Attestation: form → `POST /attest` → `DayModeStore.attest_sheet` (market_reset-gated); the daily-note tick read-back calls the same method. | `aset/store.py:75,109`; `aset/web.py:923,585-587,1061,475`; `daymode/store.py:132,142` |
    49	| F6 | `watchlists.yaml` = three derived tiers; only reader `archiver/config.py:19`. | file header |
    50	| F7 | `fetch_bars` follows redirects and returns parsed bars only: status, redirect history, elapsed and bytes are invisible to a caller. i1 export ≈14 days, ~9.4k rows. | `archiver/collector.py:159-174` |
    51	| F8 | Screener `v=152&c=0..150` → 151 named columns; `t=` multi-ticker works; `ft=` meaning unverified. | DATA-SOURCE-MEMO:42-47,60,105 |
    52	| F9 | No request rate is known: 5 names @10 s clean; nightly archiver ~1,055 req / 23 min at 1.2 s. | LIVE-FEED-SPIKE §A; `archiver/runner.py:27` |
    53	| F10 | market_reset 20:00–21:00 ET: gated writes raise `SessionBlocked`; the heartbeat died 8× catching it instead of asking the clock. | `heartbeat-blackout-2026-09-10.md` |
    54	| F11 | `BarStore.upsert_bars` opens its own connection and transaction; `TraderSettingsStore.put` commits its own; a job holds one connection per side. No transaction can span membership, mirror and bars. | `archiver/store.py:73`; `settings/store.py:90`; ADR-0008:91-92 |
    55	| F12 | `tunables.yaml` is re-read by `com.cobalt.aset`; a new enum value is the 09-09 outage class. `duration` rows are integer seconds. | `jobs.yaml:69`; `taxonomy/tunables.py:32-66`; `heartbeat.probe_timeout_s` |
    56	| F13 | Resident + `supervisor: self` is a new shape; `should_keep_running` exists for it; `job_run` does not read `enabled`. | `jobs/wrapper.py:122-162,199` |
    57	| F14 | Radar Screens note: four `##` prose sections, no fenced blocks; the Day Scan gate is prose. | vault note (read-only) |
    58	| F15 | `cobalt_dev` holds 0 bars. | `select count(*) from system.bars` |
    59	| F16 | The worktree has no `.env`; the CLI loads only `<checkout>/.env`; `cobalt.db` reads `POSTGRES_*` from the environment; DB tests already skip without `POSTGRES_HOST`/`POSTGRES_USER` (`requires_db`). | `cli.py:57`; `db.py:168-170`; `test_aset_store.py:30`, `test_daymode.py:51` |
    60	| F17 | `data/`, `logs/` gitignored. | `.gitignore:2,6` |
    61	| F18 | `VaultWriter.create_if_absent`, `upsert_unit(placement=)`, `restore(write_id)` refuse in market_reset and audit through `VaultWriteStore` (user side, DB). | `vaultwrite/writer.py:559,644,1066`; ADR-0008:143 |
    62	| F19 | Static import walk (09-10): `cobalt.aset.web` — loaded by string in `aset/__main__.py` (`uvicorn.run("cobalt.aset.web:app")`) — reaches 47 `cobalt.*` modules incl. `aset.store`, `aset.web`, `daymode.store`, `settings.*`, `cards.*`; NOT `archiver`, `heartbeat`, `jobs`, `db_migrations`, `cli`. `cobalt_agent.main` reaches 0 `cobalt.*` modules. mainframe, obsidian, herdr run no repo Python. | ast walk; `ops/*.plist` ProgramArguments |
    63	| F20 | `cobalt validate` is config-only (no DB connection). | `cli.py:123` |
    64	
    65	## §2 Decisions
    66	
    67	### D1 — Sources: two vault notes, four block kinds, one parser
    68	
    69	- **Screens note** `1 - Trading/Radar Screens.md` (exists):
    70	  - *screen block* — a fence with no `kind` key. `ScreenBlock` (extra=forbid): `screen` (display name → key = snake slug, unique), `f` (`^[a-z0-9_.]+(,[a-z0-9_.]+)*$`; `%`, `&`, `=`, `auth` refused), `sort` (`^-?[a-z0-9_]+$`), `columns` (list[int] 0–150, display only), `active_from` / `active_to` (`"HH:MM"` ET, from < to), `enabled` (bool), and OPTIONAL `ft` (int 0–99, absent by default; sent as `&ft=` only when present). `ft` exists from the first deploy, so the E4 outcome never needs a schema change.
    71	  - *pool block* — `kind: pool`, its own schema (D2). Exactly one per note.
    72	- **Lists note** `1 - Trading/Radar Lists.md` (new, R4):
    73	  - *list block* — no `kind`. `ListBlock` (extra=forbid): `list` (key), `description`, `tickers` (uppercase, unique), `radar` (bool: pool source), `archive` (list[`Interval`]), `backfill_default` (exactly one true across blocks), `enabled`. E3: the three tiers move as they are; membership `source` = `list:tier_a@<sha12>`.
    74	  - *exclude block* — `kind: exclude`, `tickers`; at most one → `excluded_by = manual`.
    75	- **Dispatch:** no `kind` → the note's default block, validated strictly; `kind: pool` (Screens) or `kind: exclude` (Lists) → that schema; any other `kind` value, or a kind in the wrong note → a named parse failure. A fence is never skipped.
    76	- **Parser** `cobalt.radar.notes`: reads the file bytes once per check and hashes those bytes (no torn reads under Obsidian Sync); only ```` ```yaml ```` fences; prose and `cobalt:` markers ignored; sha256 per block and per note.
    77	- **Why vault notes:** R1 already makes a note the truth for screens; one parser, hash, mirror and degradation path serve screens, pool rule and lists. A separate Lists note keeps ~260 tickers out of his screen prose and gives the lists write its own write_id.
    78	- **Mirror:** `TraderSettingsStore.put` (the one write path, `settings/store.py:60`). Keys `radar.note.screens`, `radar.note.lists`, `radar.screen.<key>`, `radar.pool`, `radar.list.<key>`, `radar.exclude`; value `{block, block_sha256, note_sha256, status: ok|parse_failed|missing|removed, error}`; `source = vault:<note path>@<sha12>`. "Changed" is decided against the STORED `note_sha256`, so a skipped mirror stage is redone next cycle (D5).
    79	- **Failure:** a failed screen or list block contributes nothing; its mirror row → `parse_failed`; its members are HELD (D3 step 3); pool row degraded naming it; F18 RED. A pool block that is missing, duplicated, invalid or over budget (D2) → the pool is FROZEN (D3 step 0), mirror `radar.pool` → `missing` or `parse_failed`, pool row degraded with source `pool_block`, F18 RED. Never an empty pool from a failure; the DB never presents a previous version as current.
    80	- **R2 fixtures** (the repo's only screen definition, synthetic): `tests/fixtures/radar/radar-screens.example.md` — ONE screen block `example_session_scan` (`active_from: "10:00"`), ONE pool block (`cap: 5`, `stickiness_scans: 2`, `rank_metric` for all three sessions, `overrides: {example_session_scan: {first_from: "10:00"}}`), and prose in the "Export call (derived)" shape the proposer reads (D13); `tests/fixtures/radar/radar-lists.example.md` — ≥60 large caps by rule, one ETF (`not_equity`), one exclude block. Test variants are `model_copy` of fixture objects, never a second definition.
    81	- **R2/E5 suite test** (content, not filenames): no tracked file under `src/cobalt/`, `configs/cobalt/`, `tests/cobalt/`, `ops/` or `docs/40 - DevDocs/` contains `f=` followed by `sh_|ta_|fa_|an_|cap_|exch_|geo_|idx_|ind_|sec_|news_|earningsdate_|ipodate_|targetprice_`, outside `tests/fixtures/radar/`. The E5 exact-string check is the hub's (§7).
    82	
    83	### D2 — The pool block (`kind: pool`): the trader's rule
    84	
    85	The 09-10 ruling, as the proposal renders it (D13). No committed config file carries these values.
    86	
    87	```yaml
    88	kind: pool
    89	cap: 50                     # hard; never exceeded
    90	priority: [screens, lists]  # a permutation of both
    91	rank_metric:                # exactly these three keys
    92	  premarket: volume         # 04:00–09:30 (F1 session clock)
    93	  rth: rvol                 # 09:30–16:00
    94	  aftermarket: volume       # 16:00–20:00 — architect decision, veto-able (E10)
    95	overrides:                  # keyed by screen key; each must name a screen block in this note
    96	  morning_low_float:
    97	    rank_metric: volume     # this screen ranks by volume in every session
    98	  day_scan:
    99	    first_from: "10:00"     # first among screens from this time; at most one screen
   100	stickiness_scans: 3         # integer ≥ 0
   101	```
   102	
   103	- Pydantic extra=forbid at every level; `rank_metric ∈ {volume, rvol}`; `cap ≥ 1`. An override key that names no screen block → the pool block is `parse_failed`, naming the key.
   104	- **Scanned sessions** = the `rank_metric` keys. The schema admits no `overnight` or `market_reset` key, so those sessions never scan.
   105	- **Budget**, checked on every pool-block load: `cap × 60 / radar.poll_interval + (active screens + list chunks) × 60 / radar.scan_interval ≤ radar.finviz_max_rpm`. Over budget → the pool block is invalid (D1 failure), with the computed numbers in the reason.
   106	- Metric values come from export columns named in `radar.yaml` `export.metric_headers {volume, rvol}` (engine config, pinned from a real header capture).
   107	
   108	### D3 — Ranking and stickiness: the pure function `cobalt.radar.pool.decide`
   109	
   110	A scan ranks ALL candidates. Nothing carries over between scans except each open episode's `below_cap_streak` and `last_rank`.
   111	
   112	**Rank key** (lexicographic total order; a volume number is never compared with an RVOL number):
   113	1. group, in `priority` order (a name listed by any healthy active screen is in `screens`);
   114	2. screens group only: 0 if the name is on the `first_from` screen and `now_et ≥ first_from`, else 1;
   115	3. position: the name's 1-based rank inside its best screen's export, sorted by that screen's metric (override, else the session's) descending; list-only names rank inside the union of radar lists by the session metric; a blank metric cell sorts after every valued cell;
   116	4. note order of that screen;
   117	5. ticker ascending.
   118	
   119	**Decision**, in precedence order:
   120	
   121	| Step | Condition | Result |
   122	|---|---|---|
   123	| 0 | pool block not ok (D1) | FREEZE: no membership transition; pool row degraded `pool_block` |
   124	| 1 | open member is in the exclude block | leaves, `manual` |
   125	| 2 | every source that listed the open member is inactive (window or `enabled: false`) and no active source lists it | leaves, `screen_inactive` |
   126	| 3 | open member not listed by any healthy source but listed by a degraded one | HELD: keeps its seat, streak frozen |
   127	| 4 | candidate is excluded / fails `not_equity` | never admitted, `manual` / `not_equity` |
   128	| 5 | seats = cap − held; if held > cap (cap lowered), the held with the worst `last_rank` leave until held = cap | leaves, `config_cap` |
   129	| 6 | W = the top `seats` of the ranked, non-held candidates | provisional pool |
   130	| 7 | open member ∉ W (ranked below W, or listed nowhere): `below_cap_streak += 1`; if the streak now exceeds `stickiness_scans` | leaves, `config_cap` if still ranked, `excluded_by` NULL if listed nowhere |
   131	| 8 | the remaining step-7 members, best current rank first (unlisted after ranked, then `last_rank`, ticker): each replaces the lowest-ranked newcomer in W; when W holds no newcomer | retained / leaves as in step 7 — the cap is hard |
   132	| 9 | open member ∈ W | streak 0, `last_rank` updated |
   133	| 9 | newcomer ∈ W | admitted, `entered_at`, `rank_at_entry` |
   134	| 9 | ranked candidate ∉ W, not an open member | never-admitted episode, `config_cap` |
   135	
   136	- **Invariant** (property-tested): admitted open members = held + |W| ≤ cap after every scan, for every input, including cap reductions and degraded sources.
   137	- **Streak:** counts consecutive SCANS (idle and paused cycles do not count); resets to 0 when the member is back in W; frozen while held. A member therefore leaves on the (`stickiness_scans` + 1)-th consecutive scan outside W.
   138	- **Reading of the ruling:** "fell below the cap" includes a member that dropped off every active source (screen-filter flicker between scans) — veto-able (E11).
   139	- **Morning Low Float** ranks by volume in every session (its override); **Day Scan** ranks first among screens from 10:00 (its `first_from`); its own `active_from: "10:00"` window also gates it.
   140	- **Episodes:** admitted → `entered_at`, `excluded_by` NULL. Never admitted → `entered_at` NULL + `excluded_by`, closed when it stops being a candidate. A later admission closes that episode and opens an admitted one (J1 points at admitted episodes). The first scanning cycle of a new ET trade date closes every open episode at the prior aftermarket close (`excluded_by` NULL): stickiness never carries across days.
   141	
   142	### D4 — Tables: `db_migrations/0004_radar_pool.sql` (+ rollback)
   143	
   144	```
   145	system.radar_pool
   146	  pool_key         TEXT PRIMARY KEY CHECK (pool_key ~ '^[a-z0-9_]+$')
   147	  state            TEXT NOT NULL CHECK (state IN ('scanning','idle','paused_market_reset','stopped'))
   148	  degraded         BOOLEAN NOT NULL DEFAULT false
   149	  degraded_sources JSONB NOT NULL DEFAULT '[]'   -- [{source, reason, since}]; source 'pool_block' = frozen
   150	  failed_stage     TEXT CHECK (failed_stage IN ('membership','pool_row','mirror','bars'))
   151	  failed_detail    TEXT
   152	  sources          JSONB NOT NULL DEFAULT '[]'   -- active source ids with sha12
   153	  session          TEXT NOT NULL                 -- F1 session at last stamp
   154	  cap              INTEGER                        -- from the pool block; NULL when none was ever valid
   155	  members          INTEGER NOT NULL
   156	  last_scan_id     BIGINT
   157	  last_scan_at     TIMESTAMPTZ
   158	  last_scan_ms     INTEGER
   159	  last_poll_at     TIMESTAMPTZ
   160	  poll_failures    JSONB NOT NULL DEFAULT '[]'   -- [{ticker, reason, since}]
   161	  budget           JSONB                          -- {planned_rpm, limit_rpm}
   162	  updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
   163	
   164	system.radar_membership                           -- one row per EPISODE
   165	  id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
   166	  pool_key         TEXT NOT NULL REFERENCES system.radar_pool(pool_key)
   167	  ticker           TEXT NOT NULL
   168	  trade_date       DATE NOT NULL                  -- ET
   169	  first_seen_at    TIMESTAMPTZ NOT NULL
   170	  entered_at       TIMESTAMPTZ                    -- NULL = never admitted
   171	  left_at          TIMESTAMPTZ
   172	  source           TEXT NOT NULL                  -- 'screen:<key>@<sha12>' | 'list:<key>@<sha12>', best-ranked at first sight
   173	  sources          JSONB NOT NULL                 -- every source id that listed it while open
   174	  rank_at_entry    INTEGER
   175	  last_rank        INTEGER
   176	  below_cap_streak INTEGER NOT NULL DEFAULT 0 CHECK (below_cap_streak >= 0)
   177	  excluded_by      TEXT CHECK (excluded_by IN ('config_cap','not_equity','screen_inactive','manual'))
   178	  session          TEXT NOT NULL                  -- F1 session at first sight
   179	  opened_scan_id   BIGINT NOT NULL
   180	  last_scan_id     BIGINT NOT NULL
   181	  closed_scan_id   BIGINT
   182	  CHECK (entered_at IS NOT NULL OR excluded_by IS NOT NULL)
   183	  CHECK (left_at IS NULL OR left_at >= first_seen_at)
   184	  UNIQUE INDEX (pool_key, ticker) WHERE left_at IS NULL
   185	  UNIQUE (pool_key, opened_scan_id, ticker)
   186	  INDEX (trade_date, ticker)
   187	
   188	"user".aset_sizings  ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))
   189	                     ADD pool_member_id BIGINT REFERENCES system.radar_membership(id)
   190	"user".day_modes     ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))   -- NULL = no override that day
   191	INSERT INTO "user".trader_settings (user_id, key, value, source)
   192	  SELECT id, 'aset.account_mode', '"live"'::jsonb, 'db_migration:0004' FROM "user".traders
   193	  ON CONFLICT (user_id, key) DO NOTHING
   194	```
   195	
   196	- Ownership + grants: `OWNER TO cobalt_system` on both tables; `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`; `GRANT SELECT ON system.radar_pool TO cobalt_user`.
   197	- Nullable: `pool_member_id` forever (manual cards). `aset_sizings.account_mode` is NULL only on rows written before 0004; no new card can be written without it (D8). NOT NULL is a later migration (the `aset 0004_session → 0005_session_not_null` precedent).
   198	- Rollback SQL: drop `pool_member_id` and both `account_mode` columns, `DROP TABLE system.radar_membership, system.radar_pool`, `DELETE FROM "user".trader_settings WHERE (key = 'aset.account_mode' AND source = 'db_migration:0004') OR key LIKE 'radar.%'`. **Cost, stated:** membership history and card stamps are lost; mirror rows are re-derived from the notes; the L1 `pg_dump` is the belt.
   199	- **Rollback domain (F2):** `cobalt db migrate --rollback` REQUIRES `--down-to NNNN` and runs only the reverse files of registered migrations newer than NNNN, newest first; without it, it refuses before connecting and lists targets. Hardening verdict: adopted — a whole-list rollback in prod is one keystroke from moving every table to `public`.
   200	- **Proof (r2 risk 2):** `CREATED_TABLES` are carried by the proof table. Verdicts are direction-aware: forward absent→present `CREATED`; rollback present→absent `DROPPED` for a table the reversed files create; any other difference `CHANGED`. Verdicts are computed BEFORE commit and a `CHANGED` rolls the transaction back (today it commits, then raises: `cli.py:185,193`). `DIGEST_EXCLUDED_COLUMNS` gains `account_mode`, `pool_member_id` (`cli.py:49`). Hardening verdict: adopted.
   201	- Round trip (hub, H1): `migrate → --rollback --down-to 0003 → migrate` → identical digests; 0003's columns survive; radar tables CREATED → DROPPED → CREATED; the seed row present → absent → present.
   202	
   203	### D5 — Resident `com.cobalt.radar`: loop, sessions, stage order (D6 ruling)
   204	
   205	- **Registry:** resident, `supervisor: self`, `timeout_s: 300`, `enabled: false` at merge (flipped at L11 — `com.cobalt.herdr` precedent, `jobs.yaml:127-136`), `reads:` derived by instrumenting one cycle's `open`/`read_text` (09-09 method), `imports: [cobalt.cli]` (§3).
   206	- **Plist:** `/Users/cobalt/.local/bin/uv run cobalt radar run`; `WorkingDirectory /Users/cobalt/cobalt`; `RunAtLoad true`; `KeepAlive {SuccessfulExit: false}` (a kill-switch exit 0 is not respawned; a crash is); `COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`; `logs/radar.{log,err}`. `ops/README.md`: after `cobalt resume`, `launchctl kickstart gui/$(id -u)/com.cobalt.radar`.
   207	- **Loop:** `job_run("com.cobalt.radar")`; `should_keep_running` each cycle; one cycle per `radar.scan_interval`. `scan_id` = cycle start as UTC epoch milliseconds, strictly greater than the stored `last_scan_id` (otherwise the cycle is refused, loud).
   208	- **Session asked first** via `session_clock().session(now)`, never inferred from a caught `SessionBlocked` (F10). A session with no `rank_metric` key → `idle`, no Finviz call. `market_reset` → `paused_market_reset`, zero radar writes; only the wrapper's F17 heartbeat stamps.
   209	- **Stages.** A cycle = reload notes → fetch → `decide` (pure) → **S1 membership → S2 pool row → S3 mirror → S4 bars**. Each stage is its own transaction on its own side's connection: S1 `RadarStore` (system); S2 `RadarStore` (system); S3 `TraderSettingsStore.put` (user; only when a stored `note_sha256` differs); S4 `BarStore.upsert_bars`, one transaction per ticker (system). There is no cross-store transaction (F11).
   210	- **Idempotency:** S1 on `(scan_id, ticker)` — episode opens `ON CONFLICT DO NOTHING` on `(pool_key, opened_scan_id, ticker)`; updates and closes apply only `WHERE last_scan_id < scan_id`. S2 on `scan_id`. S3 on `(key, note_sha256)`. S4 on the bars primary key.
   211	- **market_reset crossing:** the session is asked again immediately before EACH stage's commit. If it is `market_reset`, that stage and every later stage of the cycle are skipped and logged `dropped at <stage>`; nothing is written inside the window. The next non-paused cycle stamps the dropped stage as `failed_stage`.
   212	- **Partial failure:** S1 fails → S2 still runs, writing `degraded = true`, `failed_stage = membership`, then the cycle stops. S2 fails → loud log, stop (F18 turns RED on `last_scan_at` age). S3 fails → the pool row is re-stamped `failed_stage = mirror`; S4 proceeds. An S4 ticker fails → a `poll_failures` entry on the pool row. The next cycle recomputes from stored membership and stored mirror hashes, so a skipped stage heals itself.
   213	- **Belt:** `RadarStore` writes call `assert_writable("radar.<stage>")`. If it raises despite the check, that is a logged stage failure as above, never a retry loop.
   214	
   215	### D6 — Fetch: one Finviz transport (D8 ruling)
   216	
   217	- `archiver/collector.py` gains `finviz_get(path, params, token, *, on_metrics=None) -> httpx.Response`, the one HTTP call for every Finviz export. Client settings unchanged (timeout 30 s, `follow_redirects=True`), so the archiver behaves exactly as today. `on_metrics(FetchMetrics)` fires for every attempt, before `raise_for_status`: `status`, `redirect_statuses` (from `response.history`), `elapsed_ms`, `bytes`, `content_type`, or `error` (exception class) on a transport failure.
   218	- `fetch_bars(ticker, interval, token, *, on_metrics=None)` calls `finviz_get`; `FinvizScreenerCollector` calls `finviz_get`; the throttle probe observes through `on_metrics` (§4). No second httpx client.
   219	- Screens: `GET /export/screener?v=152&f=<f>[&ft=<ft>]&o=<sort>&c=0,…,150`. Lists with `radar: true`: `…&t=<chunk>&c=0,…,150`, chunked by `list_chunk_size`. Raw responses cached to `data/radar-cache/<trade_date>/<source_key>-<HHMMSS>.csv` (retention in radar.yaml). Parsed by header NAME (`export.required_headers`). Missing header, non-CSV body, HTTP error or any redirect → `SourceFailure` naming the source (degraded, D1). Token via `resolve_token`; every string through `scrub`.
   220	- One process-wide token bucket at `radar.finviz_max_rpm` for every Finviz call.
   221	- `not_equity`: radar.yaml `{header, values}` taken from a recorded header capture, never guessed.
   222	
   223	### D7 — Finviz bar poller (same process, S4)
   224	
   225	- For admitted members in rank order: `fetch_bars(ticker, Interval.I1, token)`; keep bars with `ts > watermark(ticker, 'i1')` (seeded from `max(ts) WHERE ticker = … AND interval = 'i1'` in `system.bars`) and `ts + 1 min ≤ now` (closed bars only); `BarStore.upsert_bars`.
   226	- A bar Finviz revises after the watermark passed it is corrected by the 20:30 archiver, which re-pulls the whole export with `ON CONFLICT DO UPDATE` that night.
   227	- **i1 → 2m:** pure `cobalt.archiver.aggregate.aggregate(bars, minutes)`, buckets floored from 00:00 ET, NOT stored; stored `i2` stays the archiver's. H7 reports agreement % vs archived i2; a systematic mismatch → ESCALATE, never tuned away.
   228	- **Cadence:** `radar.poll_interval` 60 s. Accepted only on ACHIEVED cadence: p95 gap between successive successful polls of the same member ≤ 1.5 × `radar.poll_interval` (H7); otherwise ESCALATE.
   229	- Poll failures reach F18 through `poll_failures` (D11).
   230	
   231	### D8 — Account mode (E1)
   232	
   233	- **Stamp order**, for every card: `"user".day_modes.account_mode` for the card's ET trade date → `"user".trader_settings['aset.account_mode']` (the standing value; `live` seeded by 0004) → neither: the card is REFUSED. Only `live` and `sim` are valid; any other stored value is also a refusal.
   234	- **Where:** `cobalt.aset.account_mode.resolve(conn, day)`, called inside `AsetStore.save` (`aset/store.py:75`) on the same user-side transaction, before the INSERT (`:109`), which writes `account_mode`. Every card goes through `save` (F5).
   235	- **Refusal:** `AccountModeUnresolved` names the day and both empty sources; `logger.error`; no row; the sheet shows the failure through the existing card-POST error path. The day-mode banner shows `ACCOUNT LIVE` or `ACCOUNT SIM`, or states that cards are refused (the `DAY MODE UNRESOLVED` pattern, `web.py:541`). Every rendered card shows its stamp.
   236	- `aset.account_mode` is NOT added to `SETTING_KEYS`: a missing row refuses cards, never the whole sheet (F4).
   237	- **Sim switch:** the attestation form (`web.py:585-587`) gains an `account_mode` select (`live` | `sim`, pre-selected to the resolved value). `POST /attest` (`web.py:1061`) passes it to `DayModeStore.attest_sheet(day, filename=…, account_mode=…)` (`daymode/store.py:132`), which writes both columns in its one upsert under the existing market_reset gate (`:142`). A missing or invalid value refuses the attestation; nothing is written. The daily-note tick read-back (`web.py:475`) passes no `account_mode`, and the upsert leaves the column as it was (`COALESCE`).
   238	- Between L3 and L5 the running sheet is old code: a card written in that gap has NULL `account_mode` (LIVE window is outside trading, §6).
   239	- `pool_member_id`: column + FK only; nothing writes it in P1.
   240	
   241	### D9 — J1
   242	
   243	Catalog proof that the FK on `"user".aset_sizings.pool_member_id` references `system.radar_membership(id)`. As `cobalt_user`: SELECT `system.radar_membership` OK, INSERT denied; an `aset_sizings` insert with a valid id OK, with an invalid id FK-fails. As `cobalt_system`: SELECT `"user".aset_sizings` denied. `requires_db`; hub-run (H10).
   244	
   245	### D10 — `cobalt db query` (R3)
   246	
   247	- `cobalt db query --side user|system [--prod] [--format json|table] [--limit 1000] "<sql>"`. Connection = `db.connect(dbname, side=…)` (factory, SET ROLE). `--prod` = `allow_prod=True` (RULING 7 tooling seam); otherwise `env.resolve_db_name()`. `src/cobalt/db_query.py`, registered in the `db` group (`db_migrations/cli.py:202`). No new `psycopg.connect`.
   248	- **Guard (before the server):** tokenizer aware of quotes, dollar-quotes and comments. Exactly one statement; first keyword `SELECT` or `WITH`. Refused as bare words: INSERT UPDATE DELETE MERGE TRUNCATE CREATE ALTER DROP GRANT REVOKE COPY CALL DO SET RESET LOCK VACUUM ANALYZE REFRESH COMMENT LISTEN NOTIFY PREPARE EXECUTE DEALLOCATE DISCARD INTO, and `FOR UPDATE|SHARE|NO KEY UPDATE|KEY SHARE`. Refused functions: `set_config pg_sleep pg_terminate_backend pg_cancel_backend pg_advisory_* lo_* dblink* pg_read_file pg_read_binary_file pg_ls_dir nextval setval`. Refusal = exit 2, one loud line naming the token.
   249	- **Belt:** `BEGIN READ ONLY`; `SET LOCAL statement_timeout` from `db.query.timeout_s`; `SELECT * FROM (<sql>) AS q LIMIT n`; always ROLLBACK; `current_user` asserted equal to the side role; output through F19 redaction.
   250	- The guard is pure (Sol, offline); the belt and connection tests are `requires_db` (hub).
   251	
   252	### D11 — F18 `radar` probe
   253	
   254	`probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat` (`heartbeat/runner.py:98-115`). `enabled: false` → OK "NOT PROBED". No pool row → RED. `market_reset` → OK "paused". Session not scanned → OK "idle (<session>)". Scanning session → RED when `now − last_scan_at > heartbeat.radar_max_age_s`; RED when degraded (each source + reason + since, `pool_block` included); RED when `failed_stage` is set (stage + detail); RED when any mirror row is `parse_failed` or `missing` (names the block); RED when any `poll_failures` entry is older than `heartbeat.radar_max_age_s` (ticker + reason).
   255	
   256	### D12 — Config: engine only
   257	
   258	- `configs/cobalt/taxonomy/tunables.yaml`, EXISTING unit/status/source values only (F12): `radar.scan_interval` 60 `duration`; `radar.poll_interval` 60 `duration`; `radar.finviz_max_rpm` `count` (value from §4); `heartbeat.radar_max_age_s` 180 `duration`; `db.query.timeout_s` 30 `duration`. No fitting enum value → ESCALATE, never a new one.
   259	- NEW `configs/cobalt/radar.yaml` (Pydantic, extra=forbid; `cobalt radar check` = dry-run): `pool_key`, `notes {screens, lists}`, `export {v: 152, columns: "0-150", required_headers, metric_headers {volume, rvol}}`, `list_chunk_size`, `not_equity {header, values}`, `cache {dir: data/radar-cache, retention_days}`. It carries no cap, rank, metric choice, session list or stickiness: those are the pool block's (D2).
   260	- `configs/cobalt/jobs.yaml`: the `com.cobalt.radar` row (D5) and `imports:` on every resident (§3); `JobSpec` gains `imports: Optional[list[str]]`.
   261	- Boundary: both new paths are under `configs/cobalt/` (the old loader's glob is top-level only), checked before adding.
   262	
   263	### D13 — The one vault write (E8): propose → HITL card → apply, hub only
   264	
   265	- `cobalt radar screens propose --pool-block <file> [--ft-compare]` derives the four screen blocks from the note's prose: `f` from the "Export call (derived)" line, cross-checked against the "Filters" line's backticked codes (mismatch → refuse); `sort`, `columns` from their bullets; `screen` from the heading after "—"; Day Scan's `active_from: "10:00"` quoting its prose; a window the prose does not state = the scanning span from the session tunables, marked `# PROPOSED — no window stated in prose`. Every derived field carries `# from: "<verbatim source line>"`. It validates the pool-block file with `PoolBlock` against the derived screen keys, then prints the blocks, a unified diff (insertions only) and its sha256.
   266	- `--ft-compare` (network; hub): for each screen, the ticker set with and without `ft=4`, counts and symmetric difference. A screen whose sets differ gets `ft: 4` in its proposed block; a screen with no difference gets no `ft` (E4). The deployed schema accepts both (D1).
   267	- `cobalt radar lists propose` renders the Lists note from `watchlists.yaml`: `tier_a/b/c` verbatim (E3), `radar: true`, `archive` from intervals, `backfill_default` on `tier_a`, the YAML header's derivation rules as prose; prints the note and its sha256.
   268	- `cobalt radar screens apply --hitl <token> --sha256 <sha>` / `cobalt radar lists apply --hitl <token> --sha256 <sha>`: re-derive, refuse on sha mismatch, then write — screens: `upsert_unit` per `##` section (4 screen units) + 1 pool unit after the last screen section; lists: `create_if_absent` (1). Each prints its write_ids and `cobalt vault restore --write-id` lines; the token is the writer `run_id`. Refusals: blocks already present, market_reset, no token, `COBALT_ENV` not matching the target vault. Test: every pre-existing line byte-identical; the diff is insertions only.
   269	- **The card:** both diffs + sha256s, the verbatim-source table, the PROPOSED windows, the pool block, the ft comparison, the rollback lines. Approval = the token in Dejan's own words.
   270	- Sol builds propose and tests it offline against fixtures. `apply` audits through `VaultWriteStore` (F18), so its tests are `requires_db` and hub-run (H11).
   271	
   272	### D14 — Stage 2: the archiver onto the Lists note; `watchlists.yaml` leaves
   273	
   274	- `archiver/config.py` builds its targets from the Lists note via `cobalt.radar.notes` (read + validate, NO mirror write — the archiver runs inside market_reset). `archive_targets` = sorted unique `(ticker, interval)` over enabled lists; `backfill_targets(t)` = the `backfill_default` list's intervals. Missing or failed note → loud failure (job `failed`, F18 RED).
   275	- No archiver plist change: the archiver plist already sets `COBALT_ENV=production`, from which `resolve_vault_path()` returns the real vault.
   276	- Sides: the archiver still opens only system-side stores (ADR-0008:146) and reads one vault FILE.
   277	- **Equality proof before delete:** `cobalt radar sources --archiver-diff --yaml-rev <sha>` prints `archive_targets` and `backfill_targets` from the note vs `watchlists.yaml` at that revision; must be empty. Fixture test in the suite; prod run at L8.
   278	- **Stage 2 commit** = archiver switch + test re-target + `git rm configs/cobalt/watchlists.yaml`, last on the branch. Rollback = `git revert <stage2>`. Separate because the 20:30 archiver needs the note, and the note exists only after L6, which needs stage-1 code on main.
   279	
   280	### D15 — Acceptance: two gates split by credentials (E7)
   281	
   282	**Sol offline gate** — no DB, no real or dev vault; fakes, mocked HTTP, `tmp_path`.
   283	
   284	| # | Check | Pass |
   285	|---|---|---|
   286	| O1 | `uv run pytest tests/cobalt tests/taxonomy` with no `POSTGRES_*` in the environment | 0 failed; every skip is `requires_db`, listed by test id |
   287	| O2 | `decide` property test: 10,000 seeded random scans incl. cap reductions, degraded sources, excludes, window closes | held + admitted ≤ cap on every scan; streak and precedence (D3 table) hold; every `excluded_by` value produced |
   288	| O3 | Offline replay: bars generated in-test → screener snapshots → `scan --replay` with fake stores, fake clock 04:00–20:30 | ≥1 enter, ≥1 leave; no fixture-screen entry before 10:00 and it ranks first after; metric switches at 09:30 and 16:00; no Finviz call in overnight or market_reset; ≥1 sticky retention and ≥1 stickiness leave |
   289	| O4 | Stage crossing: fake clock reaches 20:00:00 between S1 and S2 | zero fake-store writes after S1; next non-paused cycle stamps `failed_stage`; re-applying the same `scan_id` changes nothing; S3 failure → `failed_stage = mirror` and S4 still runs |
   290	| O5 | Parser | both fixtures parse; missing and duplicate pool block → frozen + mirror status; unknown `kind` named; `ft` absent and present; unknown override key named; over-budget pool block refused with numbers |
   291	| O6 | Throttle + transport (mocked) | 429 / 500 / redirect / HTML / header mismatch each stop the stage; `auth=REDACTED`; archiver collector tests unchanged and green |
   292	| O7 | Account mode (fakes) | resolver table: override, standing, neither, invalid; `save` refuses before the INSERT; attest form renders the select; invalid value refused; read-back path leaves the column |
   293	| O8 | `db query` guard | every refused class exits 2 naming the token; keyword inside a literal passes |
   294	| O9 | Migrations as files | 0004 DDL ↔ placement agreement; `--rollback` without `--down-to` refuses before connecting; `--down-to 0003` selects only 0004's reverse file; verdict function CREATED/DROPPED/CHANGED and abort-before-commit with a fake connection |
   295	| O10 | Whole-system, offline | `uv run cobalt validate` exit 0; `uv run cobalt radar check` exit 0; R2 test green; `plutil -lint ops/com.cobalt.radar.plist`; `uv run cobalt jobs restarts main...HEAD` printed |
   296	
   297	**Hub DB gate** — the hub's own environment, `cobalt_dev` + `~/dev-vault-cobalt` (synthetic fixture notes copied into `1 - Trading/`).
   298	
   299	| # | Check | Pass |
   300	|---|---|---|
   301	| H1 | `COBALT_ENV=dev uv run cobalt db migrate`; `--rollback --down-to 0003`; `migrate` | digests identical; 0003 columns survive; radar tables CREATED → DROPPED → CREATED; `aset.account_mode` row present → absent → present |
   302	| H2 | Full suite with DB env | 0 failed; 0 `requires_db` skipped |
   303	| H3 | Corpus: `COBALT_ENV=dev uv run archiver --backfill <T>` for every fixture list ticker (F15) | ≥1 full trading day of i1 + i2 in cobalt_dev; the day named |
   304	| H4 | `cobalt radar replay-build <day>` + `cobalt radar scan --replay <day> --from 04:00 --to 20:30` (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions present; replay-only) | SQL: open admitted ≤ pool-block cap at every `scan_id`; ≥1 enter/leave; all four `excluded_by`; window gate; a retained row with streak > 0; a proxy-RVOL crossing at T entered by T + `scan_interval`; episodes/day and cache bytes/day reported |
   305	| H5 | market_reset | a cycle at 20:30 ET leaves row counts in `radar_pool`, `radar_membership`, `bars`, `trader_settings` unchanged; no `SessionBlocked` in logs; the O4 crossing repeated against real stores writes nothing after 20:00:00 |
   306	| H6 | Degraded | source HTTP 500 → members held + RED; broken screen block → `parse_failed` + RED; pool block deleted → frozen + RED; injected S3 failure → `failed_stage` + RED |
   307	| H7 | Poller | closed bars only; watermark per `(ticker, 'i1')`; aggregate-vs-i2 agreement %; achieved cadence p95 gap ≤ 1.5 × `poll_interval` |
   308	| H8 | Probe | every D11 branch against dev rows |
   309	| H9 | Account mode (`requires_db` web tests, TestClient on cobalt_dev) | standing `live` → card stamped live; attest with `sim` → card stamped sim; standing row deleted, no override → card refused, loud log line, no row |
   310	| H10 | J1 + `db query` | D9 proofs; both sides query cobalt_dev |
   311	| H11 | propose/apply on `~/dev-vault-cobalt` with the fixture prose note | insertions-only diff; sha mismatch refuses; second apply refuses; `restore --write-id` byte-identical |
   312	| H12 | Stage 2 (RUN B) | archiver-diff empty for a Lists note rendered from `watchlists.yaml` at the RUN A sha; `archiver --backfill <T>` works from the note on cobalt_dev |
   313	
   314	Sprint acceptance = O1–O10 and H1–H12 green, plus `uv run pytest tests/cobalt tests/taxonomy` green on the rebased head.
   315	
   316	## §3 Houses, credentials, RESTARTS
   317	
   318	- **Sol** (`gpt-5.6-sol`, high, `-s workspace-write`, network on, cannot commit): **no DB credentials.** The hub launches Sol with no `POSTGRES_*` variables; the worktree has no `.env` (F16) and none is created or copied; Sol never reads `~/cobalt/.env`. Sol's work is non-DB: parser, fixtures, pool and rank logic with fakes, collectors with mocked HTTP, CLIs, migrations as files, plist, offline tests (O1–O10), the throttle probe (network only). Every DB test carries `requires_db` and skips.
   319	- **Hub** (Sonnet): launches, verifies against ground truth, commits per step on the branch; runs H1–H12 with its own environment; runs the live throttle probe if Sol's was NOT RUN; runs D13 at LIVE time.
   320	- **Dejan:** approves the HITL card.
   321	
   322	**RESTARTS rule (E6):** plist in the diff → that job; a changed file in a resident's `reads:` → that resident; a changed `src/` file → every resident whose `imports:` entry modules statically reach it; a resident with no `imports:`, or whose walk meets a dynamic import it cannot resolve → all residents; an unclassified path → ESCALATE, never dropped.
   323	
   324	**Tool:** `cobalt jobs restarts <git-range>` (`src/cobalt/jobs/restarts.py`) prints path · change · rule · restart and a final `RESTARTS:` line; untracked files are included when the range ends at the working tree. The LIVE block and every rollback run it (§6). `imports:` declared: `com.cobalt.aset` `[cobalt.aset.__main__, cobalt.aset.web]` (the app is loaded by string, F19); `com.cobalt.agent` `[cobalt_agent.main]`; `com.cobalt.mainframe`, `com.cobalt.obsidian`, `com.cobalt.herdr` `[]` (no repo Python, plist-proven); `com.cobalt.radar` `[cobalt.cli]`.
   325	
   326	**Derivation for the expected diff** (Sol re-derives from the real diff; the hub re-runs it at L5 and L9):
   327	
   328	| Path | Change | Rule applied | RESTART |
   329	|---|---|---|---|
   330	| `ops/com.cobalt.radar.plist` | A | plist in diff | `com.cobalt.radar` — bootstrap at L10 |
   331	| `configs/cobalt/taxonomy/tunables.yaml` | M | in `com.cobalt.aset` `reads:` (`jobs.yaml:69`) | `com.cobalt.aset` |
   332	| `configs/cobalt/radar.yaml` | A | in `com.cobalt.radar` `reads:` only | covered by the bootstrap |
   333	| `configs/cobalt/jobs.yaml` | M | registry | `cobalt jobs register` (not a restart) |
   334	| `src/cobalt/aset/store.py`, `aset/web.py`, `aset/account_mode.py` | M, M, A | reached from `cobalt.aset.web` (F19) | `com.cobalt.aset` |
   335	| `src/cobalt/daymode/store.py` | M | reached from `cobalt.aset.web` (F19) | `com.cobalt.aset` |
   336	| `src/cobalt/archiver/collector.py`, `archiver/aggregate.py` | M, A | reached only from `cobalt.cli` (radar, not yet loaded) | none |
   337	| `src/cobalt/radar/**`, `db_query.py`, `db_migrations/**`, `heartbeat/**`, `jobs/**`, `cli.py` | A/M | not reached from `cobalt.aset.web`; `cobalt_agent.main` reaches no `cobalt.*`; mainframe/obsidian/herdr `[]` | none (one-shots import fresh each run) |
   338	| `tests/**`, `docs/**`, `ops/README.md` | A/M | no resident reads or imports them | none |
   339	| stage 2: `archiver/config.py`, `watchlists.yaml` (D) | M, D | not reached from `cobalt.aset.web`; `cobalt jobs readers` → none | none |
   340	| anything else | — | unclassified | ESCALATE |
   341	
   342	Derived: **stage 1 → kickstart `com.cobalt.aset`; bootstrap `com.cobalt.radar` (L10). Stage 2 → none.** Rollback of either stage → the same tool on the reverse range, same restarts.
   343	
   344	## §4 Build step 1 — Finviz throttle re-measure (first)
   345	
   346	- `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`. Names = the first 50 tickers of the synthetic lists fixture. Refuses 09:00–16:00 ET on trading days and inside market_reset.
   347	- Per cycle: sequential `fetch_bars(t, Interval.I1, token, on_metrics=…)` for each name, then one `FinvizScreenerCollector` call with the fixture filter, observed through `on_metrics` (D6). STOP at the first status ≠ 200, any redirect, transport error, non-CSV body or header mismatch.
   348	- Per stage: requests, achieved req/min, status counts, p50/p95 `elapsed_ms`, bytes → `data/radar-throttle-<ts>.json` + a printed table.
   349	- **The number:** `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`, the report's first row; the tunable's `consumers` cites the report. All stages clean → "no throttle observed up to N req/min" (a floor, not a ceiling). Never extrapolated.
   350	- Token resolution fails in Sol's sandbox → NOT RUN with the scrubbed error; the hub runs the same command. READY FOR MERGE requires the number.
   351	
   352	## §5 NOT in P1
   353	
   354	Precondition evaluator (F8), dots / ladder (F10), radar panel, F3 rank display, F12 missed replay, F13 auto-archive. Writing `pool_member_id`. `account_mode NOT NULL`. An editing surface for the standing `aset.account_mode` value. The four-list re-export (E3).
   355	
   356	## §6 LIVE block — named steps, one rollback domain each
   357	
   358	Window: trading day 16:15–19:40 ET, or a weekend daytime. Never 09:00–16:00, 20:00–21:30, 21:25–21:55 (backup), or 23:27–23:47 (generated commit).
   359	
   360	| Step | Action | Proof | Rollback (domain) |
   361	|---|---|---|---|
   362	| L0 PRECONDITIONS | plan FINAL; O1–O10 and H1–H11 green; report READY FOR MERGE; `git tag pre-s2-p1` on main | report + tag | — |
   363	| L1 SNAPSHOT | `uv run cobalt backup run` | restic id + dump printed | belt for DB + vault |
   364	| L2 CODE stage 1 | hub rebases onto current main (the nightly generated commit moves it), then `git -C ~/cobalt merge --ff-only <stage1-sha>`; `git tag s2-p1-stage1` | `git log -1` | `git -C ~/cobalt reset --hard pre-s2-p1`, then L5's rollback (code) |
   365	| L3 DB | `uv run cobalt db migrate --allow-prod` | existing tables OK; radar tables CREATED; `aset.account_mode` seeded | `uv run cobalt db migrate --allow-prod --rollback --down-to 0003` (DB) |
   366	| L4 REGISTRY | `uv run cobalt validate`; `uv run cobalt jobs register` | exit 0; radar row `enabled: false` | re-register at the previous tag |
   367	| L5 RESTARTS stage 1 | `uv run cobalt jobs restarts pre-s2-p1..s2-p1-stage1` (expected: `com.cobalt.aset`, `com.cobalt.radar`); `launchctl kickstart -k gui/$(id -u)/<label>` for each printed resident except `com.cobalt.radar` (L10) | `curl -s :5010/api/health` → `ok:true`; banner shows `ACCOUNT LIVE`; next beat `sheet daymode` OK | after the L2 rollback: `cobalt jobs restarts s2-p1-stage1..pre-s2-p1` and kickstart each printed resident (code) |
   368	| L6 VAULT (HITL) | hub writes the D2 block to `data/radar-pool-block.yaml`; `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt radar screens propose --pool-block data/radar-pool-block.yaml --ft-compare` and `… radar lists propose` → card → token → `… screens apply --hitl <token> --sha256 <sha>` and `… lists apply --hitl <token> --sha256 <sha>` | 6 write_ids printed; each sha == the card's | `uv run cobalt vault restore --write-id <id>` ×6, or the L1 snapshot (vault) |
   369	| L7 SOURCES | `uv run cobalt radar sources` (production env as L6) | every block `ok`; pool block ok, budget within `finviz_max_rpm`; Day Scan `active_from "10:00"`; list counts == YAML counts | — |
   370	| L8 PROOF | `uv run cobalt radar sources --archiver-diff --yaml-rev HEAD` | empty diff | — |
   371	| L9 CODE stage 2 | `git -C ~/cobalt merge --ff-only sprint-2/radar-pool`; `git tag s2-p1`; `uv run cobalt jobs restarts s2-p1-stage1..s2-p1` (expected: none); `uv run cobalt jobs readers configs/cobalt/watchlists.yaml` | readers: none; RESTARTS: none | `git revert <stage2-sha>` + the tool on the revert range (source switch) |
   372	| L10 LAUNCHD | `cp ops/com.cobalt.radar.plist ~/Library/LaunchAgents/`; `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.radar.plist` | first cycle in `logs/radar.log`; `cobalt db query --prod --side system "select state, degraded, failed_stage, members, last_scan_at from radar_pool"` | `launchctl bootout gui/$(id -u)/com.cobalt.radar` (launchd) |
   373	| L11 ENABLE | `jobs.yaml` `enabled: true` on main; `uv run cobalt jobs register` | registry | flip back + register |
   374	| L12 HEARTBEAT | next beat | GREEN, `radar` line present | — |
   375	| L13 NEXT SESSION | 04:00+ `scanning`, ranked by volume; 09:30 rank switches to RVOL; from 10:00 Day Scan names rank first among screens; 16:00 back to volume; 20:00–21:00 radar row counts constant, probe "paused"; 20:30 archiver exit 0, target count == prior night | `cobalt db query` + logs | per domain above |
   376	
   377	## §7 Risks
   378	
   379	| Risk | Mitigation |
   380	|---|---|
   381	| Finviz lockout on his Elite login (probe or poller) | probe refuses 09:00–16:00; stop at the first error; 0.5 safety factor; one token bucket; pool-block budget check |
   382	| Real screen data reaching the repo | cache under gitignored `data/`; reports name screens by key only; R2 suite test (tracked dirs, grammar) owned by the suite; E5 exact-string check owned by the hub before every commit: `git grep -F -f <patterns>` over tracked + staged files, patterns built at run time from the vault note into a gitignored file under `data/`, never committed |
   383	| Premarket `Volume` export column may not be premarket volume (unverified) | L13 compares the 04:30 export `Volume` with summed i1 volume for 3 members; mismatch → ESCALATE (rank code unchanged) |
   384	| Pool-block budget vs the measured rate (cap 50 alone needs 50 req/min of bars at 60 s) | the budget check freezes the pool loudly at L7 instead of throttling; ESCALATE with the numbers |
   385	| Rank reshuffle at the 09:30 and 16:00 metric switch | stickiness damps it; L13 observes episodes around 09:30 |
   386	| First resident + `self`: zombie path unexercised | watchdog test: stale heartbeat → `zombie`; plist unloaded → RED |
   387	| i1 export ~9.4k rows × members per poll | watermark filter before model build; `last_scan_ms`; H7 achieved cadence |
   388	| Cache growth (~7k CSVs per trading day) | retention in radar.yaml; H4 bytes/day |
   389	| i1→2m disagrees with Finviz's own i2 | H7 agreement %; systematic mismatch → ESCALATE |
   390	| Rebase conflicts | branch already rebased on `16847eb`; rebase again at L2, never after |
   391	
   392	**Round-2 RISKS, one line each:**
   393	
   394	| r2 risk | Verdict |
   395	|---|---|
   396	| 1 Watermark keyed by ticker only; revisions deferred | ADOPT the `(ticker, 'i1')` key (D7). DISSENT on intraday revision: the 20:30 archiver corrects revised bars the same night; a rolling re-pull would multiply poll rows. |
   397	| 2 Proof mislabels intentional drops; raises after commit | ADOPT: direction-aware `CREATED`/`DROPPED`, verdicts before commit, `CHANGED` rolls back (D4). |
   398	| 3 A 60 s setting does not prove two polls per 2m bar | ADOPT: achieved-cadence acceptance, p95 gap ≤ 1.5 × `poll_interval` (D7, H7). |
   399	| 4 Scan freshness is not bar freshness | ADOPT: `poll_failures` on the pool row, RED past `heartbeat.radar_max_age_s` (D11). |
   400	| 5 E5 exact-string check vs grammar test ownership | ADOPT: suite owns the grammar test; the hub owns the exact-string check before every commit (row above). |
   401	
   402	## §8 ESCALATE
   403	
   404	```
   405	ESCALATE:
   406	E9  DAY-OPEN REPORT — ~/cobalt/docs/40 - DevDocs/reports/day-open-2026-09-10.md (uncommitted, main checkout)
   407	    still quotes the screens' real f= values (5 lines). E5 bars its commit until redacted. Outside this
   408	    branch: hub or Dejan, before the day-close commit.
   409	E10 AFTERMARKET RANK = volume (D2) — architect decision. Veto before L6, or it ships in the proposed pool block.
   410	E11 RANK READING (D3) — screens interleave by within-screen position (volume and RVOL are never compared);
   411	    stickiness also covers a member that dropped off every source. Veto either before L6.
   412	```
   413	
   414	## §9 Review record and DISSENT
   415	
   416	- **Round 1** — no verdict: Codex usage limit after 72,175 tokens (`plan-s2-p1-astra-r1.md`).
   417	- **Round 2** — BLOCKED, 8 blockers, 5 risks (`plan-s2-p1-astra-r2.md`). Resolution:
   418	
   419	| r2 blocker | Resolved in |
   420	|---|---|
   421	| 1 Account mode permitted unstamped cards | D8 (refusal, stamp order, sim switch), D4 seed, H9, L5 proof |
   422	| 2 Pool block could not pass the screen parser; committed rank/cap | D1 dispatch, D2 schema, D12 engine-only config, fixtures |
   423	| 3 Ranking incomplete; stickiness vs cap | D3 (rank key, precedence table, invariant, streak rules), D2 scanned sessions |
   424	| 4 Credentials exported to Sol; DB smoke on Sol | §3, D15 gate split |
   425	| 5 Restart rule did not follow E6 | §3 rule + tool + derivation, §6 L5/L9 and rollbacks |
   426	| 6 Single-commit claim across stores | D5 stage order, idempotency, per-stage session check, partial failure |
   427	| 7 `ft` needed a schema change after deploy | D1 optional `ft`, D13 comparison |
   428	| 8 Throttle probe could not observe status/redirects | D6 `finviz_get` + `on_metrics`, §4 |
   429	
   430	- **Round 3** — final (`plan-s2-p1-astra-r3.md`); results and DISSENT below.
   431	
   432	### DISSENT
   433	
   434	- r2 risk 1 (intraday bar revisions): the nightly archiver's full re-pull corrects them; a rolling re-pull would multiply poll rows.
     1	# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`
     2	
     3	You build S2-P1 (radar pool + Finviz bar poller) in this worktree. The plan it implements is
     4	`docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md` (FINAL). Section references (D1…D15, §3, §4)
     5	point there. Where the two disagree, the plan wins; say so in the report.
     6	
     7	## 0. Who does what
     8	
     9	| House | Does | Cannot |
    10	|---|---|---|
    11	| **You (Sol)**, high effort, `-s workspace-write`, network on | code, offline tests, fixtures, migrations as files, plist, DevDocs, the report — inside this worktree | commit, rebase, write outside the worktree, connect to ANY database, touch any vault |
    12	| **Hub (Sonnet)** | launches you, verifies, commits per step on `sprint-2/radar-pool`; runs migrations on cobalt_dev, the DB-backed suite, the dev-vault smoke (plan D15 H1–H12), and the live throttle probe if yours was NOT RUN | build |
    13	| **Dejan** | approves the HITL card | — |
    14	
    15	**Hub, before launching you:** the branch is rebased on main `16847eb` and the plan is FINAL. Launch with NO
    16	database environment: no `POSTGRES_*` variables in your environment, no `.env` in the worktree.
    17	
    18	**Two runs.** RUN A = steps 0–13 (stage 1). Print `DONE`. The hub runs H1–H11 and commits stage 1, then
    19	relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
    20	Plan D13's real propose/apply and §6 LIVE steps are hub-only; you never run them.
    21	
    22	**Stop rules.** A step you cannot finish → `NOT RUN` or `FAILED` in the report with the exact error line
    23	(scrubbed), then continue with the steps that do not depend on it. Never mark a test passing that did not run.
    24	3 failed attempts at the same thing → stop that step, ESCALATE. `DONE` is the last line of every run.
    25	
    26	## 1. Laws (binding — a violation is a failed step)
    27	
    28	1. **No credentials (E7).** You never connect to a database. Never read, copy or create a `.env`; never read
    29	   `~/cobalt/.env`; never export or set `POSTGRES_*`. Every test that needs a DB carries `requires_db`
    30	   (the existing pattern, `tests/cobalt/test_aset_store.py:30`) and skips in your environment.
    31	2. **Production is sacred (NN#16).** Never open `/Users/cobalt/Vault/Think` or `~/dev-vault-cobalt`; vault
    32	   tests use `tmp_path`. Never `launchctl` anything.
    33	3. **User data never enters the repo (L32, E5).** No real screen, filter string, list or dollar figure in any
    34	   file, report, fixture, test or pasted log line. The repo ships exactly ONE synthetic screen (R2).
    35	4. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error string
    36	   passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
    37	5. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent fallback,
    38	   no plausible-empty artifact, no default invented for a missing value.
    39	6. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
    40	   `archiver.collector.finviz_get` / `fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
    41	   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
    42	   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`, `AsetStore.save`,
    43	   `DayModeStore.attest_sheet`.
    44	7. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted (`psycopg.sql.Identifier`);
    45	   cross-side SQL is schema-qualified; every table is on a side in `db_migrations/placement.py`.
    46	8. **Config-as-code.** Pydantic, `extra="forbid"`, a dry-run command. New-core config only under
    47	   `configs/cobalt/`. Committed config carries engine tunables only — never a cap, rank rule, metric choice
    48	   or stickiness (those are the vault pool block's, D2).
    49	9. **Tunables.** EXISTING `TunableUnit` / `TunableStatus` / `TunableSource` values only (09-09 outage). No
    50	   fitting value → ESCALATE.
    51	10. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE each write stage; never rely on catching
    52	    `SessionBlocked`. Radar writes nothing in that window.
    53	11. **Tools fetch, code computes.** No LLM anywhere in P1.
    54	12. **Tests per step.** The step's tests before moving on; the whole offline suite at step 13.
    55	13. **Names.** One name per concept: `radar_pool`, `radar_membership`, `account_mode`, `aset.account_mode`,
    56	    `pool_member_id`, `excluded_by`, `below_cap_streak`, `scan_id`, `failed_stage`, `poll_failures`, `ticker`.
    57	
    58	## 2. Rulings you implement (09-10, binding)
    59	
    60	- **R1 Screens contract.** Vault note `1 - Trading/Radar Screens.md`: one fenced YAML block per screen —
    61	  `screen, f, sort, columns, active_from, active_to, enabled`, plus optional `ft` (D1). Cobalt only reads the
    62	  note: fenced blocks only, reload on file-hash change, mirror each block + hash into `"user".trader_settings`;
    63	  `radar_membership.source` names source + hash. Parse failure → degraded + `radar` probe RED naming it.
    64	- **R2** Exactly one synthetic screen, as a fixture under `tests/fixtures/radar/`.
    65	- **R3 `cobalt db query`.** Read-only CLI, SELECT-only enforced in code (D10).
    66	- **R4 Static lists** move user-side by the same mechanism: vault note `1 - Trading/Radar Lists.md`.
    67	- **E1 / D1 Account mode.** Card stamp = `day_modes.account_mode` for the day → `trader_settings['aset.account_mode']`
    68	  (standing, `live` seeded by migration 0004) → neither = card REFUSED, loud, logged, no row. The sim switch is
    69	  a select on the attestation form writing `day_modes.account_mode` for that day (D8).
    70	- **E2 / D2 Pool rule** = its own block kind `kind: pool` in the Screens note, own schema, exactly one;
    71	  missing → pool frozen, degraded, probe RED. The cap lives there.
    72	- **D3 Ranking.** premarket = volume, rth = RVOL, aftermarket = volume; overnight and market_reset do not scan.
    73	  Every scan ranks all candidates; stickiness per plan D3's precedence table; the cap is hard; Morning Low Float
    74	  ranks by volume in every session; Day Scan first among screens from 10:00.
    75	- **E3** The three tiers move as they are; `source` names the tier.
    76	- **E4 / D7** `ft` is an optional screen-block key from day one; the LIVE comparison decides whether a proposed
    77	  block carries it.
    78	- **E6 / D5 RESTARTS** by rule, derived by `cobalt jobs restarts`, printed in the report (plan §3).
    79	- **D6** Per-store transactions in the fixed order membership → pool row → mirror → bars, each idempotent,
    80	  partial failure named on the pool row (D5).
    81	- **E8** The vault write is propose (you build + offline tests) → HITL card → apply (hub).
    82	- **D8** The throttle probe observes status, redirects and elapsed through `finviz_get`'s `on_metrics` (D6).
    83	
    84	## 3. Environment
    85	
    86	- Everything from this worktree with `uv run …`. Offline suite: `uv run pytest tests/cobalt tests/taxonomy`.
    87	- DB-backed tests: mark `requires_db` (skip without `POSTGRES_HOST`/`POSTGRES_USER`). Give every store a
    88	  fake or an injected connection so its logic is testable offline; the SQL itself is tested by the hub.
    89	- Finviz token: `resolve_token()`. If it fails in your sandbox, the live throttle run is `NOT RUN`.
    90	- Vault tests: `tmp_path` + `COBALT_VAULT_PATH` monkeypatched to it.
    91	- `data/` and `logs/` are gitignored — confirm with `git check-ignore` before writing there.
    92	- DevDocs: one page per `.py` at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
    93	  `docs/40 - DevDocs/tests/cobalt/<file>.md`, a line each in `docs/40 - DevDocs/INDEX.md`.
    94	
    95	## 4. Build steps
    96	
    97	Each step lists files, then the tests that must pass before the next step.
    98	
    99	### Step 0 — Base check (no code)
   100	- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql` must succeed (main `16847eb`). Absent →
   101	  STOP, report `FAILED: base is not 16847eb`.
   102	- Record `git rev-parse HEAD`.
   103	
   104	### Step 1 — Finviz transport + throttle probe (FIRST; plan D6, §4)
   105	- `archiver/collector.py`: `FetchMetrics` model; `finviz_get(path, params, token, *, on_metrics=None)` with
   106	  today's client settings (timeout 30 s, `follow_redirects=True`); `on_metrics` fires before `raise_for_status`
   107	  with `status`, `redirect_statuses` (from `response.history`), `elapsed_ms`, `bytes`, `content_type`, or
   108	  `error` on a transport failure. `fetch_bars(ticker, interval, token, *, on_metrics=None)` calls it.
   109	- `src/cobalt/radar/throttle.py` + `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`:
   110	  names = first 50 tickers of the lists fixture (create `tests/fixtures/radar/radar-lists.example.md` now);
   111	  refuses 09:00–16:00 ET on trading days and in market_reset; per cycle sequential `fetch_bars(…, on_metrics=)`
   112	  then one screener call through `finviz_get` with the fixture filter; STOP at the first status ≠ 200, any
   113	  redirect, error, non-CSV body or header mismatch; per stage: requests, achieved req/min, status counts,
   114	  p50/p95 ms, bytes → `data/radar-throttle-<UTC ts>.json` + printed table;
   115	  `finviz_max_rpm = floor(0.5 × highest clean stage req/min)`; all clean → "no throttle observed up to N req/min".
   116	- **Tests (mocked HTTP, `test_radar_throttle.py`, `test_archiver_collector.py`):** each stop class incl. a 302
   117	  followed to 200 (redirect seen in `redirect_statuses`); refusal windows; rpm math; `auth=REDACTED`; existing
   118	  archiver collector tests unchanged and green.
   119	- **Live run** outside the forbidden window only; otherwise or on token failure `NOT RUN`. The number (or
   120	  NOT RUN) is the report's first row.
   121	
   122	### Step 2 — Migration 0004 as files, bounded rollback, direction-aware proof, placement (plan D4)
   123	- `src/cobalt/db_migrations/0004_radar_pool.sql` + `0004_radar_pool.rollback.sql`: exactly plan D4's DDL,
   124	  grants, ownership, the `aset.account_mode` seed and the rollback (header states its cost).
   125	- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring.
   126	- `db_migrations/cli.py`: `DIGEST_EXCLUDED_COLUMNS` + `account_mode`, `pool_member_id`; `--rollback` REQUIRES
   127	  `--down-to NNNN` (refuses before connecting, lists targets) and runs only newer reverse files, newest first;
   128	  verdicts `CREATED` / `DROPPED` / `CHANGED` computed BEFORE commit; `CHANGED` rolls back.
   129	- `placement.py`: `radar_pool`, `radar_membership` → new `CREATED_TABLES`, in `PLACEMENT` and the proof set.
   130	- **Offline tests (`test_radar_migration.py`, `test_tenancy.py`):** 0004 DDL ↔ placement agreement (parse the
   131	  SQL text); `--down-to` file selection; refusal without `--down-to` with no connection attempted; verdict
   132	  function table; abort-before-commit ordering with a fake connection.
   133	- **`requires_db` tests (hub):** idempotent migrate; round trip digests; 0003 columns survive; seed row
   134	  present/absent; J1 (plan D9); membership CHECKs and both unique indexes reject bad rows.
   135	
   136	### Step 3 — `cobalt db query` (plan D10)
   137	- `src/cobalt/db_query.py`, registered as `db query`. Guard pure and separately importable.
   138	- **Offline tests (`test_db_query.py`):** every refused class exits 2 naming the token; keyword in a literal
   139	  passes; multi-statement; data-modifying CTE; `set_config('role', …)`; `cobalt_brain` without `--prod` refuses
   140	  before connecting; the `psycopg.connect` lint still passes.
   141	- **`requires_db`:** READ ONLY belt, timeout, `current_user`, user side reads `system.bars` qualified.
   142	
   143	### Step 4 — Config (plan D12)
   144	- `configs/cobalt/radar.yaml` + `src/cobalt/radar/config.py`: `pool_key`, `notes {screens, lists}`,
   145	  `export {v: 152, columns: "0-150", required_headers, metric_headers {volume, rvol}}`, `list_chunk_size`,
   146	  `not_equity {header, values}`, `cache {dir: data/radar-cache, retention_days}`. `required_headers`,
   147	  `metric_headers` and `not_equity` come from a real header capture (step 6); until then `# UNVERIFIED` and a
   148	  test that fails at step 13 if still marked.
   149	- `tunables.yaml`: `radar.scan_interval` 60 duration; `radar.poll_interval` 60 duration;
   150	  `radar.finviz_max_rpm` count (step 1); `heartbeat.radar_max_age_s` 180 duration; `db.query.timeout_s` 30
   151	  duration — neighbouring rows' `scope/dynamic/status/source/consumers` shape. The cap is never a tunable (it lives in the pool block).
   152	- `jobs/config.py`: `JobSpec.imports: Optional[list[str]]`; `jobs.yaml`: `imports:` on every resident per
   153	  plan §3.
   154	- `cobalt radar check`: validates radar.yaml + tunables.
   155	- **Tests (`test_radar_config.py`, `test_jobs.py`):** bad key crashes naming the file; every new tunable
   156	  resolves; `load_tunables()` validates; `load_job_registry()` validates with `imports`.
   157	
   158	### Step 5 — Notes parser, block kinds, mirror, fixtures (plan D1, D2)
   159	- `src/cobalt/radar/models.py`: `ScreenBlock` (optional `ft`), `PoolBlock`, `ListBlock`, `ExcludeBlock`,
   160	  `SourceSet`, `ExcludedBy`. `src/cobalt/radar/notes.py`: bytes read once and hashed; yaml fences only;
   161	  dispatch by `kind` per note (D1); exactly one pool block; override keys cross-checked; budget check (D2);
   162	  sha256 per block and note.
   163	- Mirror via `TraderSettingsStore.put` with plan D1's keys and statuses; "changed" against the stored
   164	  `note_sha256`; no write in market_reset.
   165	- Fixtures: `radar-screens.example.md` — ONE screen block `example_session_scan` (synthetic `f`,
   166	  `active_from: "10:00"`, `active_to: "16:00"`, `enabled: true`), ONE pool block (`cap: 5`,
   167	  `stickiness_scans: 2`, `priority: [screens, lists]`, `rank_metric` for premarket/rth/aftermarket,
   168	  `overrides: {example_session_scan: {first_from: "10:00"}}`), prose in the "Export call (derived)" /
   169	  "Filters" / "Sort" shape. `radar-lists.example.md` — ≥60 large caps (well-known index heavyweights, not
   170	  copied from any repo file), one ETF, one `kind: exclude` block, `archive` intervals, one `backfill_default`.
   171	- **Offline tests (`test_radar_notes.py`):** plan D15 O5; each field failure names the block; prose/markers
   172	  ignored; hash stable, changes on a one-byte edit; mirror with a fake store → `parse_failed` / `missing`,
   173	  never the old block; `TraderSettings._build` succeeds with radar rows present; R2 content test (plan D1).
   174	
   175	### Step 6 — Screener collector, cache, replay (plan D6)
   176	- `src/cobalt/radar/collector.py`: `ScreenerCollector` protocol; `FinvizScreenerCollector` through
   177	  `finviz_get` (screens with optional `&ft=`; lists via `t=` chunks); one process-wide token bucket; cache
   178	  path; header-name parse; `SourceFailure` on missing header / non-CSV / HTTP error / redirect.
   179	- Capture ONE real export header with the fixture filter (network + token) and pin `required_headers`,
   180	  `metric_headers`, `not_equity` from it; cite the capture file (header row only) in the report.
   181	- `src/cobalt/radar/replay.py`: `ReplayCollector` serving snapshots by virtual clock; pure
   182	  `snapshots_from_bars(bars, screen, prior_sessions)` (RVOL proxy per plan D15 H4; only the fixture screen's
   183	  filter codes; any other code fails loud); `cobalt radar replay-build <day>` reads `system.bars` (DB, hub).
   184	- **Offline tests (`test_radar_collector.py`, `test_radar_replay.py`):** recorded-CSV parse; header mismatch;
   185	  HTML body; redirect; `t=` chunking; token bucket (fake clock); cache path gitignored; scrub; snapshot synthesis
   186	  from generated bars.
   187	
   188	### Step 7 — Pool decision + store (plan D3, D5)
   189	- `src/cobalt/radar/pool.py`: pure `decide(candidates, open_members, blocks, sources, now) → transitions`
   190	  implementing plan D3's rank key and precedence table exactly.
   191	- `src/cobalt/radar/store.py`: `RadarStore` (`SIDE = Side.SYSTEM`) — S1 membership transitions and S2 pool row,
   192	  each one transaction, idempotent per plan D5; `assert_writable("radar.<stage>")`.
   193	- **Offline tests (`test_radar_pool.py`):** plan D15 O2; one table test per D3 step; rank key with mixed
   194	  metrics never compares volume to RVOL; first_from before/after 10:00; cap lowered below held; streak
   195	  reset/freeze/leave on the (N+1)-th scan; rollover closes the prior day.
   196	- **`requires_db` (`test_radar_store.py`):** idempotent re-apply of a `scan_id`; unique indexes; store lint.
   197	
   198	### Step 8 — Bar poller + aggregation (plan D7)
   199	- `src/cobalt/radar/poller.py`: admitted members in rank order, `fetch_bars` through the shared bucket;
   200	  watermark per `(ticker, 'i1')`; closed bars only; `BarStore.upsert_bars`; per-ticker failure →
   201	  `poll_failures`.
   202	- `src/cobalt/archiver/aggregate.py`: pure `aggregate(bars, minutes)`, floored from 00:00 ET, explicit OHLCV.
   203	- **Offline tests (`test_radar_poller.py`, `test_archiver_aggregate.py`):** watermark with a fake store; open bar
   204	  excluded; failure recorded; aggregation incl. a DST day and a missing minute.
   205	- **`requires_db`:** upsert idempotent; aggregate vs stored i2 agreement % on the replay day (hub, H7).
   206	
   207	### Step 9 — Resident runner, stages, registry, plist (plan D5)
   208	- `src/cobalt/radar/runner.py` + `cobalt radar run` / `cobalt radar scan --once [--replay <day> --from HH:MM
   209	  --to HH:MM]`: `job_run`; `should_keep_running`; session asked first; S1 → S2 → S3 → S4 with the session asked
   210	  before each commit; partial-failure handling and `failed_stage` stamping per plan D5; `scan_id` monotonic.
   211	- `jobs.yaml`: `com.cobalt.radar` row per plan D5; `reads:` derived by instrumenting one offline
   212	  `scan --once` with fakes (patch `open` / `Path.read_text`, repo-relative paths), each with `# file.py:line`.
   213	- `ops/com.cobalt.radar.plist` per plan D5 (`PATH` as the archiver plist; no double hyphen in XML comments);
   214	  `ops/README.md` radar handover.
   215	- **Offline tests (`test_radar_runner.py`, `test_jobs.py`):** plan D15 O3, O4; idle cycle makes no HTTP call;
   216	  market_reset cycle writes nothing (fakes); kill switch → exit 0; `cobalt validate` exit 0 (registry ↔ plist);
   217	  watchdog: stale heartbeat on this resident → `zombie`.
   218	
   219	### Step 10 — F18 `radar` probe (plan D11)
   220	- `probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat`.
   221	- **Offline tests (`test_heartbeat.py`, row source faked):** every D11 branch.
   222	
   223	### Step 11 — Account mode (plan D8)
   224	- `src/cobalt/aset/account_mode.py`: `resolve(conn, day)` → `live|sim` or `AccountModeUnresolved`.
   225	- `aset/store.py` `save`: resolve on the same transaction before the INSERT; INSERT writes `account_mode`.
   226	- `daymode/store.py` `attest_sheet(day, *, filename, account_mode=None, now=None)`: one upsert, `COALESCE` keeps
   227	  the column when `account_mode` is None.
   228	- `aset/web.py`: attestation form select; `POST /attest` validates and passes it; banner shows
   229	  `ACCOUNT LIVE` / `ACCOUNT SIM` or that cards are refused; every card shows its stamp.
   230	- **Offline tests (`test_aset_account_mode.py`, `test_aset_web.py`):** plan D15 O7 with fakes; the upsert SQL
   231	  text keeps `COALESCE`; whole existing aset/daymode offline tests green.
   232	- **`requires_db` (hub, H9):** stamp live / sim / refusal on cobalt_dev via TestClient.
   233	
   234	### Step 12 — Propose / apply (plan D13)
   235	- `src/cobalt/radar/propose.py` + `cobalt radar screens propose --pool-block <file> [--ft-compare]`,
   236	  `cobalt radar lists propose`, `cobalt radar screens apply --hitl <token> --sha256 <sha>`,
   237	  `cobalt radar lists apply --hitl <token> --sha256 <sha>` — derivation, `# from:` and `# PROPOSED` markers,
   238	  pool-block validation, diff + sha256, refusals, write_ids + restore lines.
   239	- **Offline tests (`test_radar_propose.py`, `tmp_path`):** prose → blocks from the screen fixture (no second
   240	  screen definition); `f` mismatch between the export line and the filters line refuses; invalid pool-block file
   241	  refused; diff insertions only; sha stable; `--ft-compare` with mocked HTTP adds `ft: 4` only where sets differ;
   242	  lists proposal round-trips to the same targets as the YAML.
   243	- **`requires_db` (hub, H11):** apply writes, second apply refuses, `restore --write-id` byte-identical.
   244	
   245	### Step 13 — RESTARTS tool, offline gate, report (end of RUN A)
   246	- `src/cobalt/jobs/restarts.py` + `cobalt jobs restarts <git-range>`: plan §3 rule; static ast walk from each
   247	  resident's `imports:`; unresolvable dynamic import or missing `imports:` → all residents; unclassified →
   248	  ESCALATE line; untracked files included when the range ends at the working tree.
   249	  **Tests (`test_jobs_restarts.py`):** each rule; a string-loaded module declared vs undeclared.
   250	- Run plan D15 O1–O10. One row each: PASS / FAIL / NOT RUN + the command and its key output line.
   251	- DevDocs for every new or changed `.py` + INDEX lines.
   252	- RESTARTS: `uv run cobalt jobs restarts main...HEAD` output pasted as the derivation table.
   253	- Write the report (§5). Print `DONE`.
   254	
   255	### Step 14 — RUN B: stage 2 (plan D14)
   256	- `archiver/config.py` reads targets from the Lists note via `cobalt.radar.notes` (read + validate only);
   257	  missing or failed note → loud.
   258	- `cobalt radar sources [--json] [--archiver-diff --yaml-rev <sha>]`.
   259	- Tests re-targeted to the lists fixture; delete `configs/cobalt/watchlists.yaml` from the working tree (the
   260	  hub commits the deletion).
   261	- **Offline tests:** a Lists note rendered by `lists propose` from `watchlists.yaml` at RUN A's sha (the hub
   262	  gives it) into `tmp_path`; archiver-diff between it and the YAML at that sha is empty (the synthetic lists
   263	  fixture is NOT the comparison). **`requires_db` (hub, H12):** `archiver --backfill <T>` from the note.
   264	- Update the report (stage-2 file list, `cobalt jobs restarts <RUN A sha>...HEAD`). Print `DONE`.
   265	
   266	## 5. Report — `docs/40 - DevDocs/reports/s2-p1-2026-09-10.md`
   267	
   268	§0 headline ≤5 lines (what changed, status, ESCALATE count) → tables → ESCALATE. No restating this brief.
   269	
   270	1. **§0 Headline** — READY FOR HUB GATE / NOT READY (+ blocking rows).
   271	2. **Throttle** — `radar.finviz_max_rpm = N` (or NOT RUN + reason) first, then the stage table.
   272	3. **Base** — HEAD sha at step 0.
   273	4. **Steps** — step · status · files · tests (passed / failed / skipped `requires_db`) · evidence.
   274	5. **Offline gate** — O1–O10.
   275	6. **Hub gate** — H1–H12, every row `NOT RUN (hub)`; the hub fills them.
   276	7. **Header capture** — file path + header row only.
   277	8. **`reads:` derivation** — each path with file:line.
   278	9. **RESTARTS derivation** — the tool's output: path · change · rule · restart, and the `RESTARTS:` line.
   279	10. **LIVE block** — plan §6 L0–L13 with real shas where known, rollback column kept.
   280	11. **DISSENT** — plan §9 DISSENT verbatim.
   281	12. **ESCALATE** — plan §8 verbatim + anything new, one line each.
   282	13. **Stage 2 file list** (RUN B).
   283	
   284	You cannot write outside the worktree; the hub copies the report to `docs/_inflight/` for the vault.
   285	
   286	Print `DONE` last.
     1	Reading additional input from stdin...
     2	OpenAI Codex v0.153.4
     3	--------
     4	workdir: /Users/cobalt/cobalt-wt/s2-p1-radar-pool
     5	model: gpt-6-astra
     6	provider: openai
     7	approval: never
     8	sandbox: read-only
     9	reasoning effort: high
    10	reasoning summaries: none
    11	session id: 01a08c11-36e0-7cc0-b4ae-82c2cd864d3a
    12	--------
    13	user
    14	Round 3, final. For each round-2 blocker 1–8 and risk: RESOLVED or OPEN with file:line in the rewritten plan-s2-p1-2026-09-10.md and s2-p1-brief.md; then BLOCKERS / RISKS / VERDICT.
    15	hook: SessionStart
    16	hook: SessionStart Completed
    17	codex
    18	I’ll locate the round-2 findings and check each one against the rewritten plan and brief, with line references for the final verdict.
    19	exec
    20	/bin/zsh -lc "pwd; rg --files -g 'AGENTS.md' -g '*s2*p1*' -g '*round*' -g '*review*'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
    21	 succeeded in 0ms:
    22	/Users/cobalt/cobalt-wt/s2-p1-radar-pool
    23	docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r1.md
    24	docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md
    25	docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r3.md
    26	docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md
    27	docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md
    28	

exec
/bin/zsh -lc "tail -n 105 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-astra-r2.md'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
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

exec
/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md' | sed -n '1,210p'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
     1	# S2-P1 PLAN — Radar pool + Finviz bar poller (2026-09-10)
     2	
     3	Architect: Opus 5 (plan + brief, no build) · Reviewer: Codex `gpt-6-astra`, read-only, 3 rounds; the plan stands
     4	after round 3 (L39) · Branch `sprint-2/radar-pool`, rebased on `main` `16847eb` (heartbeat fix and `0003` merged) ·
     5	Worktree `~/cobalt-wt/s2-p1-radar-pool` · Build: Codex `gpt-5.6-sol`, no DB credentials · Hub: Sonnet · Sprint S2 = 09-10 → 09-23.
     6	
     7	## §0 Headline
     8	
     9	- Ships resident `com.cobalt.radar` (screens + static lists → a pool capped and ranked by the trader's own pool block, sticky), a Finviz i1 poller into `system.bars`, the account-mode stamp (card refused without one), J1, `cobalt db query`, `cobalt jobs restarts`, F18 `radar` probe.
    10	- Trader data lives only in two vault notes, mirrored user-side; committed config holds engine tunables only. The one vault write is hub-run after a HITL card.
    11	- Sol builds offline with no DB credentials; the hub runs migrations on cobalt_dev, the DB-backed suite and the dev-vault smoke. Two merge stages.
    12	- Rulings E1–E8 and decisions D1–D8 (09-10) are the body below (§R). ESCALATE: 3 (§8). Review: r1 no verdict, r2 BLOCKED (8), r3 final (§9).
    13	
    14	## §R Where each ruling lives
    15	
    16	| Ruling | Section |
    17	|---|---|
    18	| E1 account mode · D1 stamp order, refusal, sim switch | D8 |
    19	| E2 pool rule in the vault · D2 own block kind · D3 ranking + stickiness | D1, D2, D3 |
    20	| E3 tiers move as they are | D1, D13 |
    21	| E4 `ft=4` comparison · D7 optional `ft` now | D1, D13 |
    22	| E5 no real `f=` strings in any report/plan/review | D1 (suite test), §7 (hub exact-string check) |
    23	| E6 RESTARTS by rule · D5 derivation printed | §3, §6 |
    24	| E7 no DB credentials for Sol · D4 split | §3, D15 |
    25	| E8 vault write = propose → card → apply | D13 |
    26	| D6 per-store transactions, fixed order | D5 |
    27	| D8 observable throttle probe | D6, §4 |
    28	
    29	## Line 0 — ADR-0008 in force
    30	
    31	| Law | How P1 honours it | Evidence |
    32	|---|---|---|
    33	| Side per store | `RadarStore`, `BarStore`, `JobStore` → system; `TraderSettingsStore` (mirror, `aset.account_mode`), `AsetStore`, `DayModeStore` → user; one connection per side | ADR-0008:88-95 |
    34	| Placement | `radar_pool`, `radar_membership` move from `DECLARED_TABLES` to a new `CREATED_TABLES` (created by a db_migration on their side), carried by the placement test and the migrate proof | `placement.py:65-79`, ADR-0008:133 |
    35	| Cross-side FK | `"user".aset_sizings.pool_member_id → system.radar_membership(id)`, schema-qualified; `REFERENCES` granted | ADR-0008:126 |
    36	| Engine vs trader data | engine tunables in `tunables.yaml`; the pool rule, screens and lists are vault-note user data, mirrored into `"user".trader_settings` | ADR-0008:152-154 |
    37	| Fixed migration list, rollback SQL | `0004_radar_pool.sql` + `.rollback.sql` appended after `0003`; rollback bounded by `--down-to` | `db_migrations/__init__.py:27-37` |
    38	| `"user"` always quoted | `psycopg.sql.Identifier`; reserved-word lint | `test_tenancy.py` lint |
    39	
    40	## §1 Facts (verified read-only 09-10)
    41	
    42	| # | Fact | Evidence |
    43	|---|---|---|
    44	| F1 | Heartbeat fix merged: `FORWARD = (0001, 0002, 0003)`, `REVERSE = (0003, 0002)`. | `db_migrations/__init__.py:27-37` |
    45	| F2 | `--rollback` runs the whole `REVERSE` tuple; the proof is printed and raised AFTER commit; a table present→absent gets verdict `CHANGED`. | `db_migrations/cli.py:176,185,193-199,135-143` |
    46	| F3 | `cobalt_user` has SELECT on `system`, not REFERENCES. | `0001_schemas.sql` §4–§5 |
    47	| F4 | No live/sim value exists. `TraderSettings._build` fails only on a missing `SETTING_KEYS` row; extra rows cannot break the sheet. | `settings/models.py:29-43,70-71` |
    48	| F5 | Every card INSERT goes through `AsetStore.save`. Attestation: form → `POST /attest` → `DayModeStore.attest_sheet` (market_reset-gated); the daily-note tick read-back calls the same method. | `aset/store.py:75,109`; `aset/web.py:923,585-587,1061,475`; `daymode/store.py:132,142` |
    49	| F6 | `watchlists.yaml` = three derived tiers; only reader `archiver/config.py:19`. | file header |
    50	| F7 | `fetch_bars` follows redirects and returns parsed bars only: status, redirect history, elapsed and bytes are invisible to a caller. i1 export ≈14 days, ~9.4k rows. | `archiver/collector.py:159-174` |
    51	| F8 | Screener `v=152&c=0..150` → 151 named columns; `t=` multi-ticker works; `ft=` meaning unverified. | DATA-SOURCE-MEMO:42-47,60,105 |
    52	| F9 | No request rate is known: 5 names @10 s clean; nightly archiver ~1,055 req / 23 min at 1.2 s. | LIVE-FEED-SPIKE §A; `archiver/runner.py:27` |
    53	| F10 | market_reset 20:00–21:00 ET: gated writes raise `SessionBlocked`; the heartbeat died 8× catching it instead of asking the clock. | `heartbeat-blackout-2026-09-10.md` |
    54	| F11 | `BarStore.upsert_bars` opens its own connection and transaction; `TraderSettingsStore.put` commits its own; a job holds one connection per side. No transaction can span membership, mirror and bars. | `archiver/store.py:73`; `settings/store.py:90`; ADR-0008:91-92 |
    55	| F12 | `tunables.yaml` is re-read by `com.cobalt.aset`; a new enum value is the 09-09 outage class. `duration` rows are integer seconds. | `jobs.yaml:69`; `taxonomy/tunables.py:32-66`; `heartbeat.probe_timeout_s` |
    56	| F13 | Resident + `supervisor: self` is a new shape; `should_keep_running` exists for it; `job_run` does not read `enabled`. | `jobs/wrapper.py:122-162,199` |
    57	| F14 | Radar Screens note: four `##` prose sections, no fenced blocks; the Day Scan gate is prose. | vault note (read-only) |
    58	| F15 | `cobalt_dev` holds 0 bars. | `select count(*) from system.bars` |
    59	| F16 | The worktree has no `.env`; the CLI loads only `<checkout>/.env`; `cobalt.db` reads `POSTGRES_*` from the environment; DB tests already skip without `POSTGRES_HOST`/`POSTGRES_USER` (`requires_db`). | `cli.py:57`; `db.py:168-170`; `test_aset_store.py:30`, `test_daymode.py:51` |
    60	| F17 | `data/`, `logs/` gitignored. | `.gitignore:2,6` |
    61	| F18 | `VaultWriter.create_if_absent`, `upsert_unit(placement=)`, `restore(write_id)` refuse in market_reset and audit through `VaultWriteStore` (user side, DB). | `vaultwrite/writer.py:559,644,1066`; ADR-0008:143 |
    62	| F19 | Static import walk (09-10): `cobalt.aset.web` — loaded by string in `aset/__main__.py` (`uvicorn.run("cobalt.aset.web:app")`) — reaches 47 `cobalt.*` modules incl. `aset.store`, `aset.web`, `daymode.store`, `settings.*`, `cards.*`; NOT `archiver`, `heartbeat`, `jobs`, `db_migrations`, `cli`. `cobalt_agent.main` reaches 0 `cobalt.*` modules. mainframe, obsidian, herdr run no repo Python. | ast walk; `ops/*.plist` ProgramArguments |
    63	| F20 | `cobalt validate` is config-only (no DB connection). | `cli.py:123` |
    64	
    65	## §2 Decisions
    66	
    67	### D1 — Sources: two vault notes, four block kinds, one parser
    68	
    69	- **Screens note** `1 - Trading/Radar Screens.md` (exists):
    70	  - *screen block* — a fence with no `kind` key. `ScreenBlock` (extra=forbid): `screen` (display name → key = snake slug, unique), `f` (`^[a-z0-9_.]+(,[a-z0-9_.]+)*$`; `%`, `&`, `=`, `auth` refused), `sort` (`^-?[a-z0-9_]+$`), `columns` (list[int] 0–150, display only), `active_from` / `active_to` (`"HH:MM"` ET, from < to), `enabled` (bool), and OPTIONAL `ft` (int 0–99, absent by default; sent as `&ft=` only when present). `ft` exists from the first deploy, so the E4 outcome never needs a schema change.
    71	  - *pool block* — `kind: pool`, its own schema (D2). Exactly one per note.
    72	- **Lists note** `1 - Trading/Radar Lists.md` (new, R4):
    73	  - *list block* — no `kind`. `ListBlock` (extra=forbid): `list` (key), `description`, `tickers` (uppercase, unique), `radar` (bool: pool source), `archive` (list[`Interval`]), `backfill_default` (exactly one true across blocks), `enabled`. E3: the three tiers move as they are; membership `source` = `list:tier_a@<sha12>`.
    74	  - *exclude block* — `kind: exclude`, `tickers`; at most one → `excluded_by = manual`.
    75	- **Dispatch:** no `kind` → the note's default block, validated strictly; `kind: pool` (Screens) or `kind: exclude` (Lists) → that schema; any other `kind` value, or a kind in the wrong note → a named parse failure. A fence is never skipped.
    76	- **Parser** `cobalt.radar.notes`: reads the file bytes once per check and hashes those bytes (no torn reads under Obsidian Sync); only ```` ```yaml ```` fences; prose and `cobalt:` markers ignored; sha256 per block and per note.
    77	- **Why vault notes:** R1 already makes a note the truth for screens; one parser, hash, mirror and degradation path serve screens, pool rule and lists. A separate Lists note keeps ~260 tickers out of his screen prose and gives the lists write its own write_id.
    78	- **Mirror:** `TraderSettingsStore.put` (the one write path, `settings/store.py:60`). Keys `radar.note.screens`, `radar.note.lists`, `radar.screen.<key>`, `radar.pool`, `radar.list.<key>`, `radar.exclude`; value `{block, block_sha256, note_sha256, status: ok|parse_failed|missing|removed, error}`; `source = vault:<note path>@<sha12>`. "Changed" is decided against the STORED `note_sha256`, so a skipped mirror stage is redone next cycle (D5).
    79	- **Failure:** a failed screen or list block contributes nothing; its mirror row → `parse_failed`; its members are HELD (D3 step 3); pool row degraded naming it; F18 RED. A pool block that is missing, duplicated, invalid or over budget (D2) → the pool is FROZEN (D3 step 0), mirror `radar.pool` → `missing` or `parse_failed`, pool row degraded with source `pool_block`, F18 RED. Never an empty pool from a failure; the DB never presents a previous version as current.
    80	- **R2 fixtures** (the repo's only screen definition, synthetic): `tests/fixtures/radar/radar-screens.example.md` — ONE screen block `example_session_scan` (`active_from: "10:00"`), ONE pool block (`cap: 5`, `stickiness_scans: 2`, `rank_metric` for all three sessions, `overrides: {example_session_scan: {first_from: "10:00"}}`), and prose in the "Export call (derived)" shape the proposer reads (D13); `tests/fixtures/radar/radar-lists.example.md` — ≥60 large caps by rule, one ETF (`not_equity`), one exclude block. Test variants are `model_copy` of fixture objects, never a second definition.
    81	- **R2/E5 suite test** (content, not filenames): no tracked file under `src/cobalt/`, `configs/cobalt/`, `tests/cobalt/`, `ops/` or `docs/40 - DevDocs/` contains `f=` followed by `sh_|ta_|fa_|an_|cap_|exch_|geo_|idx_|ind_|sec_|news_|earningsdate_|ipodate_|targetprice_`, outside `tests/fixtures/radar/`. The E5 exact-string check is the hub's (§7).
    82	
    83	### D2 — The pool block (`kind: pool`): the trader's rule
    84	
    85	The 09-10 ruling, as the proposal renders it (D13). No committed config file carries these values.
    86	
    87	```yaml
    88	kind: pool
    89	cap: 50                     # hard; never exceeded
    90	priority: [screens, lists]  # a permutation of both
    91	rank_metric:                # exactly these three keys
    92	  premarket: volume         # 04:00–09:30 (F1 session clock)
    93	  rth: rvol                 # 09:30–16:00
    94	  aftermarket: volume       # 16:00–20:00 — architect decision, veto-able (E10)
    95	overrides:                  # keyed by screen key; each must name a screen block in this note
    96	  morning_low_float:
    97	    rank_metric: volume     # this screen ranks by volume in every session
    98	  day_scan:
    99	    first_from: "10:00"     # first among screens from this time; at most one screen
   100	stickiness_scans: 3         # integer ≥ 0
   101	```
   102	
   103	- Pydantic extra=forbid at every level; `rank_metric ∈ {volume, rvol}`; `cap ≥ 1`. An override key that names no screen block → the pool block is `parse_failed`, naming the key.
   104	- **Scanned sessions** = the `rank_metric` keys. The schema admits no `overnight` or `market_reset` key, so those sessions never scan.
   105	- **Budget**, checked on every pool-block load: `cap × 60 / radar.poll_interval + (active screens + list chunks) × 60 / radar.scan_interval ≤ radar.finviz_max_rpm`. Over budget → the pool block is invalid (D1 failure), with the computed numbers in the reason.
   106	- Metric values come from export columns named in `radar.yaml` `export.metric_headers {volume, rvol}` (engine config, pinned from a real header capture).
   107	
   108	### D3 — Ranking and stickiness: the pure function `cobalt.radar.pool.decide`
   109	
   110	A scan ranks ALL candidates. Nothing carries over between scans except each open episode's `below_cap_streak` and `last_rank`.
   111	
   112	**Rank key** (lexicographic total order; a volume number is never compared with an RVOL number):
   113	1. group, in `priority` order (a name listed by any healthy active screen is in `screens`);
   114	2. screens group only: 0 if the name is on the `first_from` screen and `now_et ≥ first_from`, else 1;
   115	3. position: the name's 1-based rank inside its best screen's export, sorted by that screen's metric (override, else the session's) descending; list-only names rank inside the union of radar lists by the session metric; a blank metric cell sorts after every valued cell;
   116	4. note order of that screen;
   117	5. ticker ascending.
   118	
   119	**Decision**, in precedence order:
   120	
   121	| Step | Condition | Result |
   122	|---|---|---|
   123	| 0 | pool block not ok (D1) | FREEZE: no membership transition; pool row degraded `pool_block` |
   124	| 1 | open member is in the exclude block | leaves, `manual` |
   125	| 2 | every source that listed the open member is inactive (window or `enabled: false`) and no active source lists it | leaves, `screen_inactive` |
   126	| 3 | open member not listed by any healthy source but listed by a degraded one | HELD: keeps its seat, streak frozen |
   127	| 4 | candidate is excluded / fails `not_equity` | never admitted, `manual` / `not_equity` |
   128	| 5 | seats = cap − held; if held > cap (cap lowered), the held with the worst `last_rank` leave until held = cap | leaves, `config_cap` |
   129	| 6 | W = the top `seats` of the ranked, non-held candidates | provisional pool |
   130	| 7 | open member ∉ W (ranked below W, or listed nowhere): `below_cap_streak += 1`; if the streak now exceeds `stickiness_scans` | leaves, `config_cap` if still ranked, `excluded_by` NULL if listed nowhere |
   131	| 8 | the remaining step-7 members, best current rank first (unlisted after ranked, then `last_rank`, ticker): each replaces the lowest-ranked newcomer in W; when W holds no newcomer | retained / leaves as in step 7 — the cap is hard |
   132	| 9 | open member ∈ W | streak 0, `last_rank` updated |
   133	| 9 | newcomer ∈ W | admitted, `entered_at`, `rank_at_entry` |
   134	| 9 | ranked candidate ∉ W, not an open member | never-admitted episode, `config_cap` |
   135	
   136	- **Invariant** (property-tested): admitted open members = held + |W| ≤ cap after every scan, for every input, including cap reductions and degraded sources.
   137	- **Streak:** counts consecutive SCANS (idle and paused cycles do not count); resets to 0 when the member is back in W; frozen while held. A member therefore leaves on the (`stickiness_scans` + 1)-th consecutive scan outside W.
   138	- **Reading of the ruling:** "fell below the cap" includes a member that dropped off every active source (screen-filter flicker between scans) — veto-able (E11).
   139	- **Morning Low Float** ranks by volume in every session (its override); **Day Scan** ranks first among screens from 10:00 (its `first_from`); its own `active_from: "10:00"` window also gates it.
   140	- **Episodes:** admitted → `entered_at`, `excluded_by` NULL. Never admitted → `entered_at` NULL + `excluded_by`, closed when it stops being a candidate. A later admission closes that episode and opens an admitted one (J1 points at admitted episodes). The first scanning cycle of a new ET trade date closes every open episode at the prior aftermarket close (`excluded_by` NULL): stickiness never carries across days.
   141	
   142	### D4 — Tables: `db_migrations/0004_radar_pool.sql` (+ rollback)
   143	
   144	```
   145	system.radar_pool
   146	  pool_key         TEXT PRIMARY KEY CHECK (pool_key ~ '^[a-z0-9_]+$')
   147	  state            TEXT NOT NULL CHECK (state IN ('scanning','idle','paused_market_reset','stopped'))
   148	  degraded         BOOLEAN NOT NULL DEFAULT false
   149	  degraded_sources JSONB NOT NULL DEFAULT '[]'   -- [{source, reason, since}]; source 'pool_block' = frozen
   150	  failed_stage     TEXT CHECK (failed_stage IN ('membership','pool_row','mirror','bars'))
   151	  failed_detail    TEXT
   152	  sources          JSONB NOT NULL DEFAULT '[]'   -- active source ids with sha12
   153	  session          TEXT NOT NULL                 -- F1 session at last stamp
   154	  cap              INTEGER                        -- from the pool block; NULL when none was ever valid
   155	  members          INTEGER NOT NULL
   156	  last_scan_id     BIGINT
   157	  last_scan_at     TIMESTAMPTZ
   158	  last_scan_ms     INTEGER
   159	  last_poll_at     TIMESTAMPTZ
   160	  poll_failures    JSONB NOT NULL DEFAULT '[]'   -- [{ticker, reason, since}]
   161	  budget           JSONB                          -- {planned_rpm, limit_rpm}
   162	  updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
   163	
   164	system.radar_membership                           -- one row per EPISODE
   165	  id               BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY
   166	  pool_key         TEXT NOT NULL REFERENCES system.radar_pool(pool_key)
   167	  ticker           TEXT NOT NULL
   168	  trade_date       DATE NOT NULL                  -- ET
   169	  first_seen_at    TIMESTAMPTZ NOT NULL
   170	  entered_at       TIMESTAMPTZ                    -- NULL = never admitted
   171	  left_at          TIMESTAMPTZ
   172	  source           TEXT NOT NULL                  -- 'screen:<key>@<sha12>' | 'list:<key>@<sha12>', best-ranked at first sight
   173	  sources          JSONB NOT NULL                 -- every source id that listed it while open
   174	  rank_at_entry    INTEGER
   175	  last_rank        INTEGER
   176	  below_cap_streak INTEGER NOT NULL DEFAULT 0 CHECK (below_cap_streak >= 0)
   177	  excluded_by      TEXT CHECK (excluded_by IN ('config_cap','not_equity','screen_inactive','manual'))
   178	  session          TEXT NOT NULL                  -- F1 session at first sight
   179	  opened_scan_id   BIGINT NOT NULL
   180	  last_scan_id     BIGINT NOT NULL
   181	  closed_scan_id   BIGINT
   182	  CHECK (entered_at IS NOT NULL OR excluded_by IS NOT NULL)
   183	  CHECK (left_at IS NULL OR left_at >= first_seen_at)
   184	  UNIQUE INDEX (pool_key, ticker) WHERE left_at IS NULL
   185	  UNIQUE (pool_key, opened_scan_id, ticker)
   186	  INDEX (trade_date, ticker)
   187	
   188	"user".aset_sizings  ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))
   189	                     ADD pool_member_id BIGINT REFERENCES system.radar_membership(id)
   190	"user".day_modes     ADD account_mode TEXT CHECK (account_mode IN ('live','sim'))   -- NULL = no override that day
   191	INSERT INTO "user".trader_settings (user_id, key, value, source)
   192	  SELECT id, 'aset.account_mode', '"live"'::jsonb, 'db_migration:0004' FROM "user".traders
   193	  ON CONFLICT (user_id, key) DO NOTHING
   194	```
   195	
   196	- Ownership + grants: `OWNER TO cobalt_system` on both tables; `GRANT SELECT, REFERENCES ON system.radar_membership TO cobalt_user`; `GRANT SELECT ON system.radar_pool TO cobalt_user`.
   197	- Nullable: `pool_member_id` forever (manual cards). `aset_sizings.account_mode` is NULL only on rows written before 0004; no new card can be written without it (D8). NOT NULL is a later migration (the `aset 0004_session → 0005_session_not_null` precedent).
   198	- Rollback SQL: drop `pool_member_id` and both `account_mode` columns, `DROP TABLE system.radar_membership, system.radar_pool`, `DELETE FROM "user".trader_settings WHERE (key = 'aset.account_mode' AND source = 'db_migration:0004') OR key LIKE 'radar.%'`. **Cost, stated:** membership history and card stamps are lost; mirror rows are re-derived from the notes; the L1 `pg_dump` is the belt.
   199	- **Rollback domain (F2):** `cobalt db migrate --rollback` REQUIRES `--down-to NNNN` and runs only the reverse files of registered migrations newer than NNNN, newest first; without it, it refuses before connecting and lists targets. Hardening verdict: adopted — a whole-list rollback in prod is one keystroke from moving every table to `public`.
   200	- **Proof (r2 risk 2):** `CREATED_TABLES` are carried by the proof table. Verdicts are direction-aware: forward absent→present `CREATED`; rollback present→absent `DROPPED` for a table the reversed files create; any other difference `CHANGED`. Verdicts are computed BEFORE commit and a `CHANGED` rolls the transaction back (today it commits, then raises: `cli.py:185,193`). `DIGEST_EXCLUDED_COLUMNS` gains `account_mode`, `pool_member_id` (`cli.py:49`). Hardening verdict: adopted.
   201	- Round trip (hub, H1): `migrate → --rollback --down-to 0003 → migrate` → identical digests; 0003's columns survive; radar tables CREATED → DROPPED → CREATED; the seed row present → absent → present.
   202	
   203	### D5 — Resident `com.cobalt.radar`: loop, sessions, stage order (D6 ruling)
   204	
   205	- **Registry:** resident, `supervisor: self`, `timeout_s: 300`, `enabled: false` at merge (flipped at L11 — `com.cobalt.herdr` precedent, `jobs.yaml:127-136`), `reads:` derived by instrumenting one cycle's `open`/`read_text` (09-09 method), `imports: [cobalt.cli]` (§3).
   206	- **Plist:** `/Users/cobalt/.local/bin/uv run cobalt radar run`; `WorkingDirectory /Users/cobalt/cobalt`; `RunAtLoad true`; `KeepAlive {SuccessfulExit: false}` (a kill-switch exit 0 is not respawned; a crash is); `COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`; `logs/radar.{log,err}`. `ops/README.md`: after `cobalt resume`, `launchctl kickstart gui/$(id -u)/com.cobalt.radar`.
   207	- **Loop:** `job_run("com.cobalt.radar")`; `should_keep_running` each cycle; one cycle per `radar.scan_interval`. `scan_id` = cycle start as UTC epoch milliseconds, strictly greater than the stored `last_scan_id` (otherwise the cycle is refused, loud).
   208	- **Session asked first** via `session_clock().session(now)`, never inferred from a caught `SessionBlocked` (F10). A session with no `rank_metric` key → `idle`, no Finviz call. `market_reset` → `paused_market_reset`, zero radar writes; only the wrapper's F17 heartbeat stamps.
   209	- **Stages.** A cycle = reload notes → fetch → `decide` (pure) → **S1 membership → S2 pool row → S3 mirror → S4 bars**. Each stage is its own transaction on its own side's connection: S1 `RadarStore` (system); S2 `RadarStore` (system); S3 `TraderSettingsStore.put` (user; only when a stored `note_sha256` differs); S4 `BarStore.upsert_bars`, one transaction per ticker (system). There is no cross-store transaction (F11).
   210	- **Idempotency:** S1 on `(scan_id, ticker)` — episode opens `ON CONFLICT DO NOTHING` on `(pool_key, opened_scan_id, ticker)`; updates and closes apply only `WHERE last_scan_id < scan_id`. S2 on `scan_id`. S3 on `(key, note_sha256)`. S4 on the bars primary key.

exec
/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md' | sed -n '211,465p'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
   211	- **market_reset crossing:** the session is asked again immediately before EACH stage's commit. If it is `market_reset`, that stage and every later stage of the cycle are skipped and logged `dropped at <stage>`; nothing is written inside the window. The next non-paused cycle stamps the dropped stage as `failed_stage`.
   212	- **Partial failure:** S1 fails → S2 still runs, writing `degraded = true`, `failed_stage = membership`, then the cycle stops. S2 fails → loud log, stop (F18 turns RED on `last_scan_at` age). S3 fails → the pool row is re-stamped `failed_stage = mirror`; S4 proceeds. An S4 ticker fails → a `poll_failures` entry on the pool row. The next cycle recomputes from stored membership and stored mirror hashes, so a skipped stage heals itself.
   213	- **Belt:** `RadarStore` writes call `assert_writable("radar.<stage>")`. If it raises despite the check, that is a logged stage failure as above, never a retry loop.
   214	
   215	### D6 — Fetch: one Finviz transport (D8 ruling)
   216	
   217	- `archiver/collector.py` gains `finviz_get(path, params, token, *, on_metrics=None) -> httpx.Response`, the one HTTP call for every Finviz export. Client settings unchanged (timeout 30 s, `follow_redirects=True`), so the archiver behaves exactly as today. `on_metrics(FetchMetrics)` fires for every attempt, before `raise_for_status`: `status`, `redirect_statuses` (from `response.history`), `elapsed_ms`, `bytes`, `content_type`, or `error` (exception class) on a transport failure.
   218	- `fetch_bars(ticker, interval, token, *, on_metrics=None)` calls `finviz_get`; `FinvizScreenerCollector` calls `finviz_get`; the throttle probe observes through `on_metrics` (§4). No second httpx client.
   219	- Screens: `GET /export/screener?v=152&f=<f>[&ft=<ft>]&o=<sort>&c=0,…,150`. Lists with `radar: true`: `…&t=<chunk>&c=0,…,150`, chunked by `list_chunk_size`. Raw responses cached to `data/radar-cache/<trade_date>/<source_key>-<HHMMSS>.csv` (retention in radar.yaml). Parsed by header NAME (`export.required_headers`). Missing header, non-CSV body, HTTP error or any redirect → `SourceFailure` naming the source (degraded, D1). Token via `resolve_token`; every string through `scrub`.
   220	- One process-wide token bucket at `radar.finviz_max_rpm` for every Finviz call.
   221	- `not_equity`: radar.yaml `{header, values}` taken from a recorded header capture, never guessed.
   222	
   223	### D7 — Finviz bar poller (same process, S4)
   224	
   225	- For admitted members in rank order: `fetch_bars(ticker, Interval.I1, token)`; keep bars with `ts > watermark(ticker, 'i1')` (seeded from `max(ts) WHERE ticker = … AND interval = 'i1'` in `system.bars`) and `ts + 1 min ≤ now` (closed bars only); `BarStore.upsert_bars`.
   226	- A bar Finviz revises after the watermark passed it is corrected by the 20:30 archiver, which re-pulls the whole export with `ON CONFLICT DO UPDATE` that night.
   227	- **i1 → 2m:** pure `cobalt.archiver.aggregate.aggregate(bars, minutes)`, buckets floored from 00:00 ET, NOT stored; stored `i2` stays the archiver's. H7 reports agreement % vs archived i2; a systematic mismatch → ESCALATE, never tuned away.
   228	- **Cadence:** `radar.poll_interval` 60 s. Accepted only on ACHIEVED cadence: p95 gap between successive successful polls of the same member ≤ 1.5 × `radar.poll_interval` (H7); otherwise ESCALATE.
   229	- Poll failures reach F18 through `poll_failures` (D11).
   230	
   231	### D8 — Account mode (E1)
   232	
   233	- **Stamp order**, for every card: `"user".day_modes.account_mode` for the card's ET trade date → `"user".trader_settings['aset.account_mode']` (the standing value; `live` seeded by 0004) → neither: the card is REFUSED. Only `live` and `sim` are valid; any other stored value is also a refusal.
   234	- **Where:** `cobalt.aset.account_mode.resolve(conn, day)`, called inside `AsetStore.save` (`aset/store.py:75`) on the same user-side transaction, before the INSERT (`:109`), which writes `account_mode`. Every card goes through `save` (F5).
   235	- **Refusal:** `AccountModeUnresolved` names the day and both empty sources; `logger.error`; no row; the sheet shows the failure through the existing card-POST error path. The day-mode banner shows `ACCOUNT LIVE` or `ACCOUNT SIM`, or states that cards are refused (the `DAY MODE UNRESOLVED` pattern, `web.py:541`). Every rendered card shows its stamp.
   236	- `aset.account_mode` is NOT added to `SETTING_KEYS`: a missing row refuses cards, never the whole sheet (F4).
   237	- **Sim switch:** the attestation form (`web.py:585-587`) gains an `account_mode` select (`live` | `sim`, pre-selected to the resolved value). `POST /attest` (`web.py:1061`) passes it to `DayModeStore.attest_sheet(day, filename=…, account_mode=…)` (`daymode/store.py:132`), which writes both columns in its one upsert under the existing market_reset gate (`:142`). A missing or invalid value refuses the attestation; nothing is written. The daily-note tick read-back (`web.py:475`) passes no `account_mode`, and the upsert leaves the column as it was (`COALESCE`).
   238	- Between L3 and L5 the running sheet is old code: a card written in that gap has NULL `account_mode` (LIVE window is outside trading, §6).
   239	- `pool_member_id`: column + FK only; nothing writes it in P1.
   240	
   241	### D9 — J1
   242	
   243	Catalog proof that the FK on `"user".aset_sizings.pool_member_id` references `system.radar_membership(id)`. As `cobalt_user`: SELECT `system.radar_membership` OK, INSERT denied; an `aset_sizings` insert with a valid id OK, with an invalid id FK-fails. As `cobalt_system`: SELECT `"user".aset_sizings` denied. `requires_db`; hub-run (H10).
   244	
   245	### D10 — `cobalt db query` (R3)
   246	
   247	- `cobalt db query --side user|system [--prod] [--format json|table] [--limit 1000] "<sql>"`. Connection = `db.connect(dbname, side=…)` (factory, SET ROLE). `--prod` = `allow_prod=True` (RULING 7 tooling seam); otherwise `env.resolve_db_name()`. `src/cobalt/db_query.py`, registered in the `db` group (`db_migrations/cli.py:202`). No new `psycopg.connect`.
   248	- **Guard (before the server):** tokenizer aware of quotes, dollar-quotes and comments. Exactly one statement; first keyword `SELECT` or `WITH`. Refused as bare words: INSERT UPDATE DELETE MERGE TRUNCATE CREATE ALTER DROP GRANT REVOKE COPY CALL DO SET RESET LOCK VACUUM ANALYZE REFRESH COMMENT LISTEN NOTIFY PREPARE EXECUTE DEALLOCATE DISCARD INTO, and `FOR UPDATE|SHARE|NO KEY UPDATE|KEY SHARE`. Refused functions: `set_config pg_sleep pg_terminate_backend pg_cancel_backend pg_advisory_* lo_* dblink* pg_read_file pg_read_binary_file pg_ls_dir nextval setval`. Refusal = exit 2, one loud line naming the token.
   249	- **Belt:** `BEGIN READ ONLY`; `SET LOCAL statement_timeout` from `db.query.timeout_s`; `SELECT * FROM (<sql>) AS q LIMIT n`; always ROLLBACK; `current_user` asserted equal to the side role; output through F19 redaction.
   250	- The guard is pure (Sol, offline); the belt and connection tests are `requires_db` (hub).
   251	
   252	### D11 — F18 `radar` probe
   253	
   254	`probes.radar(now)` in `heartbeat/probes.py`, added to `take_beat` (`heartbeat/runner.py:98-115`). `enabled: false` → OK "NOT PROBED". No pool row → RED. `market_reset` → OK "paused". Session not scanned → OK "idle (<session>)". Scanning session → RED when `now − last_scan_at > heartbeat.radar_max_age_s`; RED when degraded (each source + reason + since, `pool_block` included); RED when `failed_stage` is set (stage + detail); RED when any mirror row is `parse_failed` or `missing` (names the block); RED when any `poll_failures` entry is older than `heartbeat.radar_max_age_s` (ticker + reason).
   255	
   256	### D12 — Config: engine only
   257	
   258	- `configs/cobalt/taxonomy/tunables.yaml`, EXISTING unit/status/source values only (F12): `radar.scan_interval` 60 `duration`; `radar.poll_interval` 60 `duration`; `radar.finviz_max_rpm` `count` (value from §4); `heartbeat.radar_max_age_s` 180 `duration`; `db.query.timeout_s` 30 `duration`. No fitting enum value → ESCALATE, never a new one.
   259	- NEW `configs/cobalt/radar.yaml` (Pydantic, extra=forbid; `cobalt radar check` = dry-run): `pool_key`, `notes {screens, lists}`, `export {v: 152, columns: "0-150", required_headers, metric_headers {volume, rvol}}`, `list_chunk_size`, `not_equity {header, values}`, `cache {dir: data/radar-cache, retention_days}`. It carries no cap, rank, metric choice, session list or stickiness: those are the pool block's (D2).
   260	- `configs/cobalt/jobs.yaml`: the `com.cobalt.radar` row (D5) and `imports:` on every resident (§3); `JobSpec` gains `imports: Optional[list[str]]`.
   261	- Boundary: both new paths are under `configs/cobalt/` (the old loader's glob is top-level only), checked before adding.
   262	
   263	### D13 — The one vault write (E8): propose → HITL card → apply, hub only
   264	
   265	- `cobalt radar screens propose --pool-block <file> [--ft-compare]` derives the four screen blocks from the note's prose: `f` from the "Export call (derived)" line, cross-checked against the "Filters" line's backticked codes (mismatch → refuse); `sort`, `columns` from their bullets; `screen` from the heading after "—"; Day Scan's `active_from: "10:00"` quoting its prose; a window the prose does not state = the scanning span from the session tunables, marked `# PROPOSED — no window stated in prose`. Every derived field carries `# from: "<verbatim source line>"`. It validates the pool-block file with `PoolBlock` against the derived screen keys, then prints the blocks, a unified diff (insertions only) and its sha256.
   266	- `--ft-compare` (network; hub): for each screen, the ticker set with and without `ft=4`, counts and symmetric difference. A screen whose sets differ gets `ft: 4` in its proposed block; a screen with no difference gets no `ft` (E4). The deployed schema accepts both (D1).
   267	- `cobalt radar lists propose` renders the Lists note from `watchlists.yaml`: `tier_a/b/c` verbatim (E3), `radar: true`, `archive` from intervals, `backfill_default` on `tier_a`, the YAML header's derivation rules as prose; prints the note and its sha256.
   268	- `cobalt radar screens apply --hitl <token> --sha256 <sha>` / `cobalt radar lists apply --hitl <token> --sha256 <sha>`: re-derive, refuse on sha mismatch, then write — screens: `upsert_unit` per `##` section (4 screen units) + 1 pool unit after the last screen section; lists: `create_if_absent` (1). Each prints its write_ids and `cobalt vault restore --write-id` lines; the token is the writer `run_id`. Refusals: blocks already present, market_reset, no token, `COBALT_ENV` not matching the target vault. Test: every pre-existing line byte-identical; the diff is insertions only.
   269	- **The card:** both diffs + sha256s, the verbatim-source table, the PROPOSED windows, the pool block, the ft comparison, the rollback lines. Approval = the token in Dejan's own words.
   270	- Sol builds propose and tests it offline against fixtures. `apply` audits through `VaultWriteStore` (F18), so its tests are `requires_db` and hub-run (H11).
   271	
   272	### D14 — Stage 2: the archiver onto the Lists note; `watchlists.yaml` leaves
   273	
   274	- `archiver/config.py` builds its targets from the Lists note via `cobalt.radar.notes` (read + validate, NO mirror write — the archiver runs inside market_reset). `archive_targets` = sorted unique `(ticker, interval)` over enabled lists; `backfill_targets(t)` = the `backfill_default` list's intervals. Missing or failed note → loud failure (job `failed`, F18 RED).
   275	- No archiver plist change: the archiver plist already sets `COBALT_ENV=production`, from which `resolve_vault_path()` returns the real vault.
   276	- Sides: the archiver still opens only system-side stores (ADR-0008:146) and reads one vault FILE.
   277	- **Equality proof before delete:** `cobalt radar sources --archiver-diff --yaml-rev <sha>` prints `archive_targets` and `backfill_targets` from the note vs `watchlists.yaml` at that revision; must be empty. Fixture test in the suite; prod run at L8.
   278	- **Stage 2 commit** = archiver switch + test re-target + `git rm configs/cobalt/watchlists.yaml`, last on the branch. Rollback = `git revert <stage2>`. Separate because the 20:30 archiver needs the note, and the note exists only after L6, which needs stage-1 code on main.
   279	
   280	### D15 — Acceptance: two gates split by credentials (E7)
   281	
   282	**Sol offline gate** — no DB, no real or dev vault; fakes, mocked HTTP, `tmp_path`.
   283	
   284	| # | Check | Pass |
   285	|---|---|---|
   286	| O1 | `uv run pytest tests/cobalt tests/taxonomy` with no `POSTGRES_*` in the environment | 0 failed; every skip is `requires_db`, listed by test id |
   287	| O2 | `decide` property test: 10,000 seeded random scans incl. cap reductions, degraded sources, excludes, window closes | held + admitted ≤ cap on every scan; streak and precedence (D3 table) hold; every `excluded_by` value produced |
   288	| O3 | Offline replay: bars generated in-test → screener snapshots → `scan --replay` with fake stores, fake clock 04:00–20:30 | ≥1 enter, ≥1 leave; no fixture-screen entry before 10:00 and it ranks first after; metric switches at 09:30 and 16:00; no Finviz call in overnight or market_reset; ≥1 sticky retention and ≥1 stickiness leave |
   289	| O4 | Stage crossing: fake clock reaches 20:00:00 between S1 and S2 | zero fake-store writes after S1; next non-paused cycle stamps `failed_stage`; re-applying the same `scan_id` changes nothing; S3 failure → `failed_stage = mirror` and S4 still runs |
   290	| O5 | Parser | both fixtures parse; missing and duplicate pool block → frozen + mirror status; unknown `kind` named; `ft` absent and present; unknown override key named; over-budget pool block refused with numbers |
   291	| O6 | Throttle + transport (mocked) | 429 / 500 / redirect / HTML / header mismatch each stop the stage; `auth=REDACTED`; archiver collector tests unchanged and green |
   292	| O7 | Account mode (fakes) | resolver table: override, standing, neither, invalid; `save` refuses before the INSERT; attest form renders the select; invalid value refused; read-back path leaves the column |
   293	| O8 | `db query` guard | every refused class exits 2 naming the token; keyword inside a literal passes |
   294	| O9 | Migrations as files | 0004 DDL ↔ placement agreement; `--rollback` without `--down-to` refuses before connecting; `--down-to 0003` selects only 0004's reverse file; verdict function CREATED/DROPPED/CHANGED and abort-before-commit with a fake connection |
   295	| O10 | Whole-system, offline | `uv run cobalt validate` exit 0; `uv run cobalt radar check` exit 0; R2 test green; `plutil -lint ops/com.cobalt.radar.plist`; `uv run cobalt jobs restarts main...HEAD` printed |
   296	
   297	**Hub DB gate** — the hub's own environment, `cobalt_dev` + `~/dev-vault-cobalt` (synthetic fixture notes copied into `1 - Trading/`).
   298	
   299	| # | Check | Pass |
   300	|---|---|---|
   301	| H1 | `COBALT_ENV=dev uv run cobalt db migrate`; `--rollback --down-to 0003`; `migrate` | digests identical; 0003 columns survive; radar tables CREATED → DROPPED → CREATED; `aset.account_mode` row present → absent → present |
   302	| H2 | Full suite with DB env | 0 failed; 0 `requires_db` skipped |
   303	| H3 | Corpus: `COBALT_ENV=dev uv run archiver --backfill <T>` for every fixture list ticker (F15) | ≥1 full trading day of i1 + i2 in cobalt_dev; the day named |
   304	| H4 | `cobalt radar replay-build <day>` + `cobalt radar scan --replay <day> --from 04:00 --to 20:30` (RVOL proxy = cumulative volume ÷ mean cumulative volume at the same minute over the prior sessions present; replay-only) | SQL: open admitted ≤ pool-block cap at every `scan_id`; ≥1 enter/leave; all four `excluded_by`; window gate; a retained row with streak > 0; a proxy-RVOL crossing at T entered by T + `scan_interval`; episodes/day and cache bytes/day reported |
   305	| H5 | market_reset | a cycle at 20:30 ET leaves row counts in `radar_pool`, `radar_membership`, `bars`, `trader_settings` unchanged; no `SessionBlocked` in logs; the O4 crossing repeated against real stores writes nothing after 20:00:00 |
   306	| H6 | Degraded | source HTTP 500 → members held + RED; broken screen block → `parse_failed` + RED; pool block deleted → frozen + RED; injected S3 failure → `failed_stage` + RED |
   307	| H7 | Poller | closed bars only; watermark per `(ticker, 'i1')`; aggregate-vs-i2 agreement %; achieved cadence p95 gap ≤ 1.5 × `poll_interval` |
   308	| H8 | Probe | every D11 branch against dev rows |
   309	| H9 | Account mode (`requires_db` web tests, TestClient on cobalt_dev) | standing `live` → card stamped live; attest with `sim` → card stamped sim; standing row deleted, no override → card refused, loud log line, no row |
   310	| H10 | J1 + `db query` | D9 proofs; both sides query cobalt_dev |
   311	| H11 | propose/apply on `~/dev-vault-cobalt` with the fixture prose note | insertions-only diff; sha mismatch refuses; second apply refuses; `restore --write-id` byte-identical |
   312	| H12 | Stage 2 (RUN B) | archiver-diff empty for a Lists note rendered from `watchlists.yaml` at the RUN A sha; `archiver --backfill <T>` works from the note on cobalt_dev |
   313	
   314	Sprint acceptance = O1–O10 and H1–H12 green, plus `uv run pytest tests/cobalt tests/taxonomy` green on the rebased head.
   315	
   316	## §3 Houses, credentials, RESTARTS
   317	
   318	- **Sol** (`gpt-5.6-sol`, high, `-s workspace-write`, network on, cannot commit): **no DB credentials.** The hub launches Sol with no `POSTGRES_*` variables; the worktree has no `.env` (F16) and none is created or copied; Sol never reads `~/cobalt/.env`. Sol's work is non-DB: parser, fixtures, pool and rank logic with fakes, collectors with mocked HTTP, CLIs, migrations as files, plist, offline tests (O1–O10), the throttle probe (network only). Every DB test carries `requires_db` and skips.
   319	- **Hub** (Sonnet): launches, verifies against ground truth, commits per step on the branch; runs H1–H12 with its own environment; runs the live throttle probe if Sol's was NOT RUN; runs D13 at LIVE time.
   320	- **Dejan:** approves the HITL card.
   321	
   322	**RESTARTS rule (E6):** plist in the diff → that job; a changed file in a resident's `reads:` → that resident; a changed `src/` file → every resident whose `imports:` entry modules statically reach it; a resident with no `imports:`, or whose walk meets a dynamic import it cannot resolve → all residents; an unclassified path → ESCALATE, never dropped.
   323	
   324	**Tool:** `cobalt jobs restarts <git-range>` (`src/cobalt/jobs/restarts.py`) prints path · change · rule · restart and a final `RESTARTS:` line; untracked files are included when the range ends at the working tree. The LIVE block and every rollback run it (§6). `imports:` declared: `com.cobalt.aset` `[cobalt.aset.__main__, cobalt.aset.web]` (the app is loaded by string, F19); `com.cobalt.agent` `[cobalt_agent.main]`; `com.cobalt.mainframe`, `com.cobalt.obsidian`, `com.cobalt.herdr` `[]` (no repo Python, plist-proven); `com.cobalt.radar` `[cobalt.cli]`.
   325	
   326	**Derivation for the expected diff** (Sol re-derives from the real diff; the hub re-runs it at L5 and L9):
   327	
   328	| Path | Change | Rule applied | RESTART |
   329	|---|---|---|---|
   330	| `ops/com.cobalt.radar.plist` | A | plist in diff | `com.cobalt.radar` — bootstrap at L10 |
   331	| `configs/cobalt/taxonomy/tunables.yaml` | M | in `com.cobalt.aset` `reads:` (`jobs.yaml:69`) | `com.cobalt.aset` |
   332	| `configs/cobalt/radar.yaml` | A | in `com.cobalt.radar` `reads:` only | covered by the bootstrap |
   333	| `configs/cobalt/jobs.yaml` | M | registry | `cobalt jobs register` (not a restart) |
   334	| `src/cobalt/aset/store.py`, `aset/web.py`, `aset/account_mode.py` | M, M, A | reached from `cobalt.aset.web` (F19) | `com.cobalt.aset` |
   335	| `src/cobalt/daymode/store.py` | M | reached from `cobalt.aset.web` (F19) | `com.cobalt.aset` |
   336	| `src/cobalt/archiver/collector.py`, `archiver/aggregate.py` | M, A | reached only from `cobalt.cli` (radar, not yet loaded) | none |
   337	| `src/cobalt/radar/**`, `db_query.py`, `db_migrations/**`, `heartbeat/**`, `jobs/**`, `cli.py` | A/M | not reached from `cobalt.aset.web`; `cobalt_agent.main` reaches no `cobalt.*`; mainframe/obsidian/herdr `[]` | none (one-shots import fresh each run) |
   338	| `tests/**`, `docs/**`, `ops/README.md` | A/M | no resident reads or imports them | none |
   339	| stage 2: `archiver/config.py`, `watchlists.yaml` (D) | M, D | not reached from `cobalt.aset.web`; `cobalt jobs readers` → none | none |
   340	| anything else | — | unclassified | ESCALATE |
   341	
   342	Derived: **stage 1 → kickstart `com.cobalt.aset`; bootstrap `com.cobalt.radar` (L10). Stage 2 → none.** Rollback of either stage → the same tool on the reverse range, same restarts.
   343	
   344	## §4 Build step 1 — Finviz throttle re-measure (first)
   345	
   346	- `cobalt radar throttle-probe --names 50 --grids 60,30,15,10 --cycles 3`. Names = the first 50 tickers of the synthetic lists fixture. Refuses 09:00–16:00 ET on trading days and inside market_reset.
   347	- Per cycle: sequential `fetch_bars(t, Interval.I1, token, on_metrics=…)` for each name, then one `FinvizScreenerCollector` call with the fixture filter, observed through `on_metrics` (D6). STOP at the first status ≠ 200, any redirect, transport error, non-CSV body or header mismatch.
   348	- Per stage: requests, achieved req/min, status counts, p50/p95 `elapsed_ms`, bytes → `data/radar-throttle-<ts>.json` + a printed table.
   349	- **The number:** `radar.finviz_max_rpm = floor(0.5 × highest clean stage req/min)`, the report's first row; the tunable's `consumers` cites the report. All stages clean → "no throttle observed up to N req/min" (a floor, not a ceiling). Never extrapolated.
   350	- Token resolution fails in Sol's sandbox → NOT RUN with the scrubbed error; the hub runs the same command. READY FOR MERGE requires the number.
   351	
   352	## §5 NOT in P1
   353	
   354	Precondition evaluator (F8), dots / ladder (F10), radar panel, F3 rank display, F12 missed replay, F13 auto-archive. Writing `pool_member_id`. `account_mode NOT NULL`. An editing surface for the standing `aset.account_mode` value. The four-list re-export (E3).
   355	
   356	## §6 LIVE block — named steps, one rollback domain each
   357	
   358	Window: trading day 16:15–19:40 ET, or a weekend daytime. Never 09:00–16:00, 20:00–21:30, 21:25–21:55 (backup), or 23:27–23:47 (generated commit).
   359	
   360	| Step | Action | Proof | Rollback (domain) |
   361	|---|---|---|---|
   362	| L0 PRECONDITIONS | plan FINAL; O1–O10 and H1–H11 green; report READY FOR MERGE; `git tag pre-s2-p1` on main | report + tag | — |
   363	| L1 SNAPSHOT | `uv run cobalt backup run` | restic id + dump printed | belt for DB + vault |
   364	| L2 CODE stage 1 | hub rebases onto current main (the nightly generated commit moves it), then `git -C ~/cobalt merge --ff-only <stage1-sha>`; `git tag s2-p1-stage1` | `git log -1` | `git -C ~/cobalt reset --hard pre-s2-p1`, then L5's rollback (code) |
   365	| L3 DB | `uv run cobalt db migrate --allow-prod` | existing tables OK; radar tables CREATED; `aset.account_mode` seeded | `uv run cobalt db migrate --allow-prod --rollback --down-to 0003` (DB) |
   366	| L4 REGISTRY | `uv run cobalt validate`; `uv run cobalt jobs register` | exit 0; radar row `enabled: false` | re-register at the previous tag |
   367	| L5 RESTARTS stage 1 | `uv run cobalt jobs restarts pre-s2-p1..s2-p1-stage1` (expected: `com.cobalt.aset`, `com.cobalt.radar`); `launchctl kickstart -k gui/$(id -u)/<label>` for each printed resident except `com.cobalt.radar` (L10) | `curl -s :5010/api/health` → `ok:true`; banner shows `ACCOUNT LIVE`; next beat `sheet daymode` OK | after the L2 rollback: `cobalt jobs restarts s2-p1-stage1..pre-s2-p1` and kickstart each printed resident (code) |
   368	| L6 VAULT (HITL) | hub writes the D2 block to `data/radar-pool-block.yaml`; `COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt radar screens propose --pool-block data/radar-pool-block.yaml --ft-compare` and `… radar lists propose` → card → token → `… screens apply --hitl <token> --sha256 <sha>` and `… lists apply --hitl <token> --sha256 <sha>` | 6 write_ids printed; each sha == the card's | `uv run cobalt vault restore --write-id <id>` ×6, or the L1 snapshot (vault) |
   369	| L7 SOURCES | `uv run cobalt radar sources` (production env as L6) | every block `ok`; pool block ok, budget within `finviz_max_rpm`; Day Scan `active_from "10:00"`; list counts == YAML counts | — |
   370	| L8 PROOF | `uv run cobalt radar sources --archiver-diff --yaml-rev HEAD` | empty diff | — |
   371	| L9 CODE stage 2 | `git -C ~/cobalt merge --ff-only sprint-2/radar-pool`; `git tag s2-p1`; `uv run cobalt jobs restarts s2-p1-stage1..s2-p1` (expected: none); `uv run cobalt jobs readers configs/cobalt/watchlists.yaml` | readers: none; RESTARTS: none | `git revert <stage2-sha>` + the tool on the revert range (source switch) |
   372	| L10 LAUNCHD | `cp ops/com.cobalt.radar.plist ~/Library/LaunchAgents/`; `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.radar.plist` | first cycle in `logs/radar.log`; `cobalt db query --prod --side system "select state, degraded, failed_stage, members, last_scan_at from radar_pool"` | `launchctl bootout gui/$(id -u)/com.cobalt.radar` (launchd) |
   373	| L11 ENABLE | `jobs.yaml` `enabled: true` on main; `uv run cobalt jobs register` | registry | flip back + register |
   374	| L12 HEARTBEAT | next beat | GREEN, `radar` line present | — |
   375	| L13 NEXT SESSION | 04:00+ `scanning`, ranked by volume; 09:30 rank switches to RVOL; from 10:00 Day Scan names rank first among screens; 16:00 back to volume; 20:00–21:00 radar row counts constant, probe "paused"; 20:30 archiver exit 0, target count == prior night | `cobalt db query` + logs | per domain above |
   376	
   377	## §7 Risks
   378	
   379	| Risk | Mitigation |
   380	|---|---|
   381	| Finviz lockout on his Elite login (probe or poller) | probe refuses 09:00–16:00; stop at the first error; 0.5 safety factor; one token bucket; pool-block budget check |
   382	| Real screen data reaching the repo | cache under gitignored `data/`; reports name screens by key only; R2 suite test (tracked dirs, grammar) owned by the suite; E5 exact-string check owned by the hub before every commit: `git grep -F -f <patterns>` over tracked + staged files, patterns built at run time from the vault note into a gitignored file under `data/`, never committed |
   383	| Premarket `Volume` export column may not be premarket volume (unverified) | L13 compares the 04:30 export `Volume` with summed i1 volume for 3 members; mismatch → ESCALATE (rank code unchanged) |
   384	| Pool-block budget vs the measured rate (cap 50 alone needs 50 req/min of bars at 60 s) | the budget check freezes the pool loudly at L7 instead of throttling; ESCALATE with the numbers |
   385	| Rank reshuffle at the 09:30 and 16:00 metric switch | stickiness damps it; L13 observes episodes around 09:30 |
   386	| First resident + `self`: zombie path unexercised | watchdog test: stale heartbeat → `zombie`; plist unloaded → RED |
   387	| i1 export ~9.4k rows × members per poll | watermark filter before model build; `last_scan_ms`; H7 achieved cadence |
   388	| Cache growth (~7k CSVs per trading day) | retention in radar.yaml; H4 bytes/day |
   389	| i1→2m disagrees with Finviz's own i2 | H7 agreement %; systematic mismatch → ESCALATE |
   390	| Rebase conflicts | branch already rebased on `16847eb`; rebase again at L2, never after |
   391	
   392	**Round-2 RISKS, one line each:**
   393	
   394	| r2 risk | Verdict |
   395	|---|---|
   396	| 1 Watermark keyed by ticker only; revisions deferred | ADOPT the `(ticker, 'i1')` key (D7). DISSENT on intraday revision: the 20:30 archiver corrects revised bars the same night; a rolling re-pull would multiply poll rows. |
   397	| 2 Proof mislabels intentional drops; raises after commit | ADOPT: direction-aware `CREATED`/`DROPPED`, verdicts before commit, `CHANGED` rolls back (D4). |
   398	| 3 A 60 s setting does not prove two polls per 2m bar | ADOPT: achieved-cadence acceptance, p95 gap ≤ 1.5 × `poll_interval` (D7, H7). |
   399	| 4 Scan freshness is not bar freshness | ADOPT: `poll_failures` on the pool row, RED past `heartbeat.radar_max_age_s` (D11). |
   400	| 5 E5 exact-string check vs grammar test ownership | ADOPT: suite owns the grammar test; the hub owns the exact-string check before every commit (row above). |
   401	
   402	## §8 ESCALATE
   403	
   404	```
   405	ESCALATE:
   406	E9  DAY-OPEN REPORT — ~/cobalt/docs/40 - DevDocs/reports/day-open-2026-09-10.md (uncommitted, main checkout)
   407	    still quotes the screens' real f= values (5 lines). E5 bars its commit until redacted. Outside this
   408	    branch: hub or Dejan, before the day-close commit.
   409	E10 AFTERMARKET RANK = volume (D2) — architect decision. Veto before L6, or it ships in the proposed pool block.
   410	E11 RANK READING (D3) — screens interleave by within-screen position (volume and RVOL are never compared);
   411	    stickiness also covers a member that dropped off every source. Veto either before L6.
   412	```
   413	
   414	## §9 Review record and DISSENT
   415	
   416	- **Round 1** — no verdict: Codex usage limit after 72,175 tokens (`plan-s2-p1-astra-r1.md`).
   417	- **Round 2** — BLOCKED, 8 blockers, 5 risks (`plan-s2-p1-astra-r2.md`). Resolution:
   418	
   419	| r2 blocker | Resolved in |
   420	|---|---|
   421	| 1 Account mode permitted unstamped cards | D8 (refusal, stamp order, sim switch), D4 seed, H9, L5 proof |
   422	| 2 Pool block could not pass the screen parser; committed rank/cap | D1 dispatch, D2 schema, D12 engine-only config, fixtures |
   423	| 3 Ranking incomplete; stickiness vs cap | D3 (rank key, precedence table, invariant, streak rules), D2 scanned sessions |
   424	| 4 Credentials exported to Sol; DB smoke on Sol | §3, D15 gate split |
   425	| 5 Restart rule did not follow E6 | §3 rule + tool + derivation, §6 L5/L9 and rollbacks |
   426	| 6 Single-commit claim across stores | D5 stage order, idempotency, per-stage session check, partial failure |
   427	| 7 `ft` needed a schema change after deploy | D1 optional `ft`, D13 comparison |
   428	| 8 Throttle probe could not observe status/redirects | D6 `finviz_get` + `on_metrics`, §4 |
   429	
   430	- **Round 3** — final (`plan-s2-p1-astra-r3.md`); results and DISSENT below.
   431	
   432	### DISSENT
   433	
   434	- r2 risk 1 (intraday bar revisions): the nightly archiver's full re-pull corrects them; a rolling re-pull would multiply poll rows.

exec
/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md' | sed -n '1,104p'
rg --files --hidden -g AGENTS.md -g '"'!node_modules'"' -g '"'!.git'"' . /Users/cobalt/.codex 2>/dev/null" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
     1	# S2-P1 BUILD BRIEF — for Codex `gpt-5.6-sol`
     2	
     3	You build S2-P1 (radar pool + Finviz bar poller) in this worktree. The plan it implements is
     4	`docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md` (FINAL). Section references (D1…D15, §3, §4)
     5	point there. Where the two disagree, the plan wins; say so in the report.
     6	
     7	## 0. Who does what
     8	
     9	| House | Does | Cannot |
    10	|---|---|---|
    11	| **You (Sol)**, high effort, `-s workspace-write`, network on | code, offline tests, fixtures, migrations as files, plist, DevDocs, the report — inside this worktree | commit, rebase, write outside the worktree, connect to ANY database, touch any vault |
    12	| **Hub (Sonnet)** | launches you, verifies, commits per step on `sprint-2/radar-pool`; runs migrations on cobalt_dev, the DB-backed suite, the dev-vault smoke (plan D15 H1–H12), and the live throttle probe if yours was NOT RUN | build |
    13	| **Dejan** | approves the HITL card | — |
    14	
    15	**Hub, before launching you:** the branch is rebased on main `16847eb` and the plan is FINAL. Launch with NO
    16	database environment: no `POSTGRES_*` variables in your environment, no `.env` in the worktree.
    17	
    18	**Two runs.** RUN A = steps 0–13 (stage 1). Print `DONE`. The hub runs H1–H11 and commits stage 1, then
    19	relaunches you with `RUN B` in the prompt. RUN B = step 14 (stage 2) + report update. Print `DONE`.
    20	Plan D13's real propose/apply and §6 LIVE steps are hub-only; you never run them.
    21	
    22	**Stop rules.** A step you cannot finish → `NOT RUN` or `FAILED` in the report with the exact error line
    23	(scrubbed), then continue with the steps that do not depend on it. Never mark a test passing that did not run.
    24	3 failed attempts at the same thing → stop that step, ESCALATE. `DONE` is the last line of every run.
    25	
    26	## 1. Laws (binding — a violation is a failed step)
    27	
    28	1. **No credentials (E7).** You never connect to a database. Never read, copy or create a `.env`; never read
    29	   `~/cobalt/.env`; never export or set `POSTGRES_*`. Every test that needs a DB carries `requires_db`
    30	   (the existing pattern, `tests/cobalt/test_aset_store.py:30`) and skips in your environment.
    31	2. **Production is sacred (NN#16).** Never open `/Users/cobalt/Vault/Think` or `~/dev-vault-cobalt`; vault
    32	   tests use `tmp_path`. Never `launchctl` anything.
    33	3. **User data never enters the repo (L32, E5).** No real screen, filter string, list or dollar figure in any
    34	   file, report, fixture, test or pasted log line. The repo ships exactly ONE synthetic screen (R2).
    35	4. **Secrets.** Never print, log or paste a token, password, DSN or env value. Every URL and error string
    36	   passes through `cobalt.archiver.collector.scrub`. Never run `env`, `printenv` or `cat .env`.
    37	5. **Fail loud.** Missing data or invalid config = a loud failure naming the file/field. No silent fallback,
    38	   no plausible-empty artifact, no default invented for a missing value.
    39	6. **One path.** Reuse, never copy: `cobalt.db.connect` (the ONLY `psycopg.connect` is in `db.py`),
    40	   `archiver.collector.finviz_get` / `fetch_bars` / `resolve_token` / `scrub`, `BarStore.upsert_bars`,
    41	   `TraderSettingsStore.put`, `VaultWriter.upsert_unit` / `create_if_absent`, `session_clock()`,
    42	   `jobs.wrapper.job_run` / `should_keep_running`, `load_tunables()`, `AsetStore.save`,
    43	   `DayModeStore.attest_sheet`.
    44	7. **ADR-0008 two layers.** Every store declares `SIDE`; `"user"` is ALWAYS quoted (`psycopg.sql.Identifier`);
    45	   cross-side SQL is schema-qualified; every table is on a side in `db_migrations/placement.py`.
    46	8. **Config-as-code.** Pydantic, `extra="forbid"`, a dry-run command. New-core config only under
    47	   `configs/cobalt/`. Committed config carries engine tunables only — never a cap, rank rule, metric choice
    48	   or stickiness (those are the vault pool block's, D2).
    49	9. **Tunables.** EXISTING `TunableUnit` / `TunableStatus` / `TunableSource` values only (09-09 outage). No
    50	   fitting value → ESCALATE.
    51	10. **market_reset (20:00–21:00 ET).** Ask `session_clock()` BEFORE each write stage; never rely on catching
    52	    `SessionBlocked`. Radar writes nothing in that window.
    53	11. **Tools fetch, code computes.** No LLM anywhere in P1.
    54	12. **Tests per step.** The step's tests before moving on; the whole offline suite at step 13.
    55	13. **Names.** One name per concept: `radar_pool`, `radar_membership`, `account_mode`, `aset.account_mode`,
    56	    `pool_member_id`, `excluded_by`, `below_cap_streak`, `scan_id`, `failed_stage`, `poll_failures`, `ticker`.
    57	
    58	## 2. Rulings you implement (09-10, binding)
    59	
    60	- **R1 Screens contract.** Vault note `1 - Trading/Radar Screens.md`: one fenced YAML block per screen —
    61	  `screen, f, sort, columns, active_from, active_to, enabled`, plus optional `ft` (D1). Cobalt only reads the
    62	  note: fenced blocks only, reload on file-hash change, mirror each block + hash into `"user".trader_settings`;
    63	  `radar_membership.source` names source + hash. Parse failure → degraded + `radar` probe RED naming it.
    64	- **R2** Exactly one synthetic screen, as a fixture under `tests/fixtures/radar/`.
    65	- **R3 `cobalt db query`.** Read-only CLI, SELECT-only enforced in code (D10).
    66	- **R4 Static lists** move user-side by the same mechanism: vault note `1 - Trading/Radar Lists.md`.
    67	- **E1 / D1 Account mode.** Card stamp = `day_modes.account_mode` for the day → `trader_settings['aset.account_mode']`
    68	  (standing, `live` seeded by migration 0004) → neither = card REFUSED, loud, logged, no row. The sim switch is
    69	  a select on the attestation form writing `day_modes.account_mode` for that day (D8).
    70	- **E2 / D2 Pool rule** = its own block kind `kind: pool` in the Screens note, own schema, exactly one;
    71	  missing → pool frozen, degraded, probe RED. The cap lives there.
    72	- **D3 Ranking.** premarket = volume, rth = RVOL, aftermarket = volume; overnight and market_reset do not scan.
    73	  Every scan ranks all candidates; stickiness per plan D3's precedence table; the cap is hard; Morning Low Float
    74	  ranks by volume in every session; Day Scan first among screens from 10:00.
    75	- **E3** The three tiers move as they are; `source` names the tier.
    76	- **E4 / D7** `ft` is an optional screen-block key from day one; the LIVE comparison decides whether a proposed
    77	  block carries it.
    78	- **E6 / D5 RESTARTS** by rule, derived by `cobalt jobs restarts`, printed in the report (plan §3).
    79	- **D6** Per-store transactions in the fixed order membership → pool row → mirror → bars, each idempotent,
    80	  partial failure named on the pool row (D5).
    81	- **E8** The vault write is propose (you build + offline tests) → HITL card → apply (hub).
    82	- **D8** The throttle probe observes status, redirects and elapsed through `finviz_get`'s `on_metrics` (D6).
    83	
    84	## 3. Environment
    85	
    86	- Everything from this worktree with `uv run …`. Offline suite: `uv run pytest tests/cobalt tests/taxonomy`.
    87	- DB-backed tests: mark `requires_db` (skip without `POSTGRES_HOST`/`POSTGRES_USER`). Give every store a
    88	  fake or an injected connection so its logic is testable offline; the SQL itself is tested by the hub.
    89	- Finviz token: `resolve_token()`. If it fails in your sandbox, the live throttle run is `NOT RUN`.
    90	- Vault tests: `tmp_path` + `COBALT_VAULT_PATH` monkeypatched to it.
    91	- `data/` and `logs/` are gitignored — confirm with `git check-ignore` before writing there.
    92	- DevDocs: one page per `.py` at `docs/40 - DevDocs/cobalt/<module>/<file>.md`, tests at
    93	  `docs/40 - DevDocs/tests/cobalt/<file>.md`, a line each in `docs/40 - DevDocs/INDEX.md`.
    94	
    95	## 4. Build steps
    96	
    97	Each step lists files, then the tests that must pass before the next step.
    98	
    99	### Step 0 — Base check (no code)
   100	- `test -f src/cobalt/db_migrations/0003_heartbeat_vault_outcome.sql` must succeed (main `16847eb`). Absent →
   101	  STOP, report `FAILED: base is not 16847eb`.
   102	- Record `git rev-parse HEAD`.
   103	
   104	### Step 1 — Finviz transport + throttle probe (FIRST; plan D6, §4)
/Users/cobalt/.codex/.tmp/plugins/plugins/zoom/AGENTS.md
/Users/cobalt/.codex/.tmp/plugins/plugins/product-design/templates/prototype/AGENTS.md
/Users/cobalt/.codex/.tmp/plugins/plugins/product-design/templates/mobile-app/AGENTS.md
/Users/cobalt/.codex/.tmp/plugins/plugins/vercel/skills/react-best-practices/AGENTS.md
/Users/cobalt/.codex/.tmp/plugins/plugins/data-analytics/AGENTS.md
/Users/cobalt/.codex/.tmp/plugins/plugins/build-web-apps/skills/supabase-best-practices/AGENTS.md
/Users/cobalt/.codex/.tmp/plugins/plugins/build-web-apps/skills/react-best-practices/AGENTS.md

codex
The rewrite integrates most of the round-2 fixes. I’m checking several remaining edge cases: whether retained members’ stickiness streaks reset, whether rollback can invoke the new restart tool after removing it, and whether the migration proof allows the new settings seed.
exec
/bin/zsh -lc "nl -ba src/cobalt/db_migrations/cli.py | sed -n '35,215p'
nl -ba src/cobalt/db_migrations/placement.py | sed -n '1,130p'
nl -ba src/cobalt/settings/store.py | sed -n '45,115p'
nl -ba src/cobalt/archiver/store.py | sed -n '45,115p'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
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
     1	"""The placement map: which side every table is on (ADR-0008 D2).
     2	
     3	ONE MAP, THREE READERS. The suite's placement test compares it against
     4	what the database actually holds; the lint test compares every store's
     5	SQL against its own `SIDE`; and a test asserts this map and
     6	`0002_move_tables.sql` name the same tables on the same sides, so the
     7	Python copy and the SQL copy cannot drift apart in silence.
     8	
     9	FUTURE TABLES ARE DECLARED HERE BEFORE THEY EXIST. That is the point of
    10	the map: ADR-0008 D2 names the S2/S3 tables (`trade_defs`, `tunables`,
    11	`trader_settings`, `radar_pool`, `radar_membership`, the legs/fills and
    12	missed rows, the taxonomy anatomy instances) so that when one of them is
    13	created it lands on a side someone already ruled on. A table that exists
    14	in `"user"` or `system` and is NOT in this map fails the placement test;
    15	so does a table on the wrong side.
    16	
    17	`public` IS FROZEN. The 17 old-tree tables are listed and untouched
    18	(strangler rule). A NEW table landing in `public` fails the suite — that
    19	is the whole enforcement behind "every new table is declared on a side".
    20	"""
    21	
    22	from cobalt.db import Side
    23	
    24	#: The 12 tables `0002_move_tables.sql` moves out of `public`.
    25	#: `"user".traders` is not here: 0001 creates it directly on its side.
    26	MOVED_TABLES: dict[str, Side] = {
    27	    # --- user side -----------------------------------------------------
    28	    "aset_sizings": Side.USER,
    29	    "card_transitions": Side.USER,
    30	    "card_stop_edits": Side.USER,
    31	    "day_modes": Side.USER,
    32	    "vault_writes": Side.USER,
    33	    "vault_overrides": Side.USER,
    34	    # --- system side ---------------------------------------------------
    35	    "bars": Side.SYSTEM,
    36	    "cobalt_jobs": Side.SYSTEM,
    37	    "cobalt_kill_switch": Side.SYSTEM,
    38	    "cobalt_redactions": Side.SYSTEM,
    39	    "cobalt_email_sends": Side.SYSTEM,
    40	    "session_blocks": Side.SYSTEM,
    41	}
    42	
    43	#: Created by 0001 on its side, never moved.
    44	SEEDED_TABLES: dict[str, Side] = {
    45	    "traders": Side.USER,
    46	}
    47	
    48	#: Created by a FEATURE MODULE's own migration, directly on its side —
    49	#: `<module>/migrations/*.sql`, executed by that module's store, the way
    50	#: every other table in the new core is created. They were never in
    51	#: `public`, so `0002_move_tables.sql` does not name them and the migrate
    52	#: proof table does not carry them; the placement test does.
    53	MODULE_TABLES: dict[str, Side] = {
    54	    # taxonomy/migrations/0001_trade_defs.sql (ADR-0008 D3)
    55	    "trade_defs": Side.USER,
    56	    "tunables": Side.USER,
    57	    "setup_trade_matrix": Side.USER,   # a VIEW unnested from trade_defs.def
    58	    # settings/migrations/0001_trader_settings.sql (ADR-0008 D3.4)
    59	    "trader_settings": Side.USER,
    60	}
    61	
    62	#: Declared by ADR-0008 D2 before they are built, so the first migration
    63	#: that creates one has a ruled side to create it on. Nothing here exists
    64	#: yet; the placement test only checks tables that DO exist.
    65	DECLARED_TABLES: dict[str, Side] = {
    66	    # S2-P4 / S3 — named now so the placement test knows them on sight.
    67	    "legs": Side.USER,
    68	    "fills": Side.USER,
    69	    "missed": Side.USER,
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

exec
/bin/zsh -lc "nl -ba 'docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md' | sed -n '322,342p'
nl -ba src/cobalt/archiver/collector.py | sed -n '115,200p'
nl -ba src/cobalt/cli.py | sed -n '1,65p'
rg -n 'archiver|watchlist|Interval.I1|tier|imports:|resident' src/cobalt/archiver/runner.py src/cobalt/archiver/config.py src/cobalt/archiver/cli.py configs/cobalt/jobs.yaml
nl -ba 'docs/10 - Decisions/ADR-0008-two-layer-data-model.md' | sed -n '80,160p'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
   322	**RESTARTS rule (E6):** plist in the diff → that job; a changed file in a resident's `reads:` → that resident; a changed `src/` file → every resident whose `imports:` entry modules statically reach it; a resident with no `imports:`, or whose walk meets a dynamic import it cannot resolve → all residents; an unclassified path → ESCALATE, never dropped.
   323	
   324	**Tool:** `cobalt jobs restarts <git-range>` (`src/cobalt/jobs/restarts.py`) prints path · change · rule · restart and a final `RESTARTS:` line; untracked files are included when the range ends at the working tree. The LIVE block and every rollback run it (§6). `imports:` declared: `com.cobalt.aset` `[cobalt.aset.__main__, cobalt.aset.web]` (the app is loaded by string, F19); `com.cobalt.agent` `[cobalt_agent.main]`; `com.cobalt.mainframe`, `com.cobalt.obsidian`, `com.cobalt.herdr` `[]` (no repo Python, plist-proven); `com.cobalt.radar` `[cobalt.cli]`.
   325	
   326	**Derivation for the expected diff** (Sol re-derives from the real diff; the hub re-runs it at L5 and L9):
   327	
   328	| Path | Change | Rule applied | RESTART |
   329	|---|---|---|---|
   330	| `ops/com.cobalt.radar.plist` | A | plist in diff | `com.cobalt.radar` — bootstrap at L10 |
   331	| `configs/cobalt/taxonomy/tunables.yaml` | M | in `com.cobalt.aset` `reads:` (`jobs.yaml:69`) | `com.cobalt.aset` |
   332	| `configs/cobalt/radar.yaml` | A | in `com.cobalt.radar` `reads:` only | covered by the bootstrap |
   333	| `configs/cobalt/jobs.yaml` | M | registry | `cobalt jobs register` (not a restart) |
   334	| `src/cobalt/aset/store.py`, `aset/web.py`, `aset/account_mode.py` | M, M, A | reached from `cobalt.aset.web` (F19) | `com.cobalt.aset` |
   335	| `src/cobalt/daymode/store.py` | M | reached from `cobalt.aset.web` (F19) | `com.cobalt.aset` |
   336	| `src/cobalt/archiver/collector.py`, `archiver/aggregate.py` | M, A | reached only from `cobalt.cli` (radar, not yet loaded) | none |
   337	| `src/cobalt/radar/**`, `db_query.py`, `db_migrations/**`, `heartbeat/**`, `jobs/**`, `cli.py` | A/M | not reached from `cobalt.aset.web`; `cobalt_agent.main` reaches no `cobalt.*`; mainframe/obsidian/herdr `[]` | none (one-shots import fresh each run) |
   338	| `tests/**`, `docs/**`, `ops/README.md` | A/M | no resident reads or imports them | none |
   339	| stage 2: `archiver/config.py`, `watchlists.yaml` (D) | M, D | not reached from `cobalt.aset.web`; `cobalt jobs readers` → none | none |
   340	| anything else | — | unclassified | ESCALATE |
   341	
   342	Derived: **stage 1 → kickstart `com.cobalt.aset`; bootstrap `com.cobalt.radar` (L10). Stage 2 → none.** Rollback of either stage → the same tool on the reverse range, same restarts.
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
     1	"""`cobalt` — the new core's top-level CLI.
     2	
     3	Two command groups:
     4	
     5	    cobalt vault restore --write-id N [--dry-run]
     6	    cobalt vault writes [--limit N]
     7	    cobalt vault overrides --note PATH
     8	
     9	    cobalt session now [--at ISO8601]
    10	    cobalt session backfill [--dry-run]
    11	    cobalt session blocks [--limit N]
    12	
    13	    cobalt cards state/history/move/backfill/expire/edges
    14	
    15	    cobalt daymode show/propose/decide/attest
    16	
    17	    cobalt db migrate [--allow-prod] [--rollback]
    18	    cobalt taxonomy load [--dry-run]
    19	    cobalt settings load --from <dir> | --from-git <commit> --dry-run|--apply
    20	    cobalt settings show
    21	
    22	    cobalt jobs list/register/check/run
    23	    cobalt heartbeat beat/show
    24	    cobalt notify email-auth/email-test/email-status
    25	    cobalt backup run/status/restore
    26	    cobalt stop / cobalt resume        (F17d kill phrase)
    27	
    28	    cobalt validate
    29	
    30	`restore` puts a section back to the before-state recorded in
    31	`vault_writes` id N, and it does so THROUGH THE SAME WRITER — same
    32	markers, same mtime/hash guard, same atomic rename, and its own audit
    33	row. There is no second write path, not even for undo.
    34	
    35	`session` is the F1 clock (Charter §3 F1); `cards` is the F7 state
    36	machine (Charter §3 F7); `daymode` is F6's two-stage mode.
    37	`validate` is the config gate
    38	(F16) — the same `python -m cobalt.taxonomy.validate` the tests run,
    39	given a name an operator can remember.
    40	"""
    41	
    42	import os
    43	
    44	os.environ.setdefault("LOGURU_LEVEL", "INFO")
    45	
    46	import argparse  # noqa: E402
    47	import sys  # noqa: E402
    48	from pathlib import Path  # noqa: E402
    49	
    50	from dotenv import load_dotenv  # noqa: E402
    51	
    52	# The Postgres parts db.connect() composes its DSN from live in the repo
    53	# .env today (TRIAGE 2.7's vault-parts redesign replaces this). The
    54	# prefill/aset entrypoints get them by ACCIDENT — a transitive old-tree
    55	# import calls load_dotenv() somewhere down their chain. This CLI has no
    56	# such chain, so it loads the same file deliberately and visibly.
    57	load_dotenv(Path(__file__).resolve().parents[2] / ".env")
    58	
    59	from cobalt.aset.config import load_config as load_aset_config  # noqa: E402
    60	from cobalt.cards import cli as cards_cli  # noqa: E402
    61	from cobalt.daymode import cli as daymode_cli  # noqa: E402
    62	from cobalt.generated import cli as generated_cli  # noqa: E402
    63	from cobalt.db_migrations import cli as db_cli  # noqa: E402
    64	from cobalt.backup import cli as backup_cli  # noqa: E402
    65	from cobalt.heartbeat import cli as heartbeat_cli  # noqa: E402
rg: src/cobalt/archiver/cli.py: No such file or directory (os error 2)
configs/cobalt/jobs.yaml:13:# kind      : resident (runs continuously) | one-shot (runs and exits).
configs/cobalt/jobs.yaml:38:  # ---------------- residents ----------------
configs/cobalt/jobs.yaml:40:    kind: resident
configs/cobalt/jobs.yaml:73:    kind: resident
configs/cobalt/jobs.yaml:83:    kind: resident
configs/cobalt/jobs.yaml:96:    kind: resident
configs/cobalt/jobs.yaml:128:    kind: resident
configs/cobalt/jobs.yaml:166:  - label: com.cobalt.archiver
configs/cobalt/jobs.yaml:174:    what: "the Bar Archiver nightly full run (uv run archiver)"
configs/cobalt/jobs.yaml:198:    # EVERY day including weekends, and after the archiver's 20:30 (which
configs/cobalt/jobs.yaml:237:    # after the archiver's 20:30 + the backup's 21:40, so the day's
src/cobalt/archiver/runner.py:9:it as a `--db-name` CLI flag, so the archiver kept writing PRODUCTION
src/cobalt/archiver/runner.py:59:    """Nightly job: archive tier_a + tier_b per their configured intervals.
src/cobalt/archiver/runner.py:75:    """On-demand: fetch ALL tier_a intervals for one ticker (a new name
src/cobalt/archiver/runner.py:76:    joining tier_a, or a manual re-fill). Same database rule as
src/cobalt/archiver/runner.py:100:    with as_job("com.cobalt.archiver") as job:
src/cobalt/archiver/runner.py:102:        # THIS is what makes F18's "archiver freshness (last run + rows
src/cobalt/archiver/runner.py:115:                f"{len(summary.failures)} archiver failure(s): "
src/cobalt/archiver/runner.py:130:    parser = argparse.ArgumentParser(prog="archiver", description="Cobalt Bar Archiver")
src/cobalt/archiver/runner.py:134:        help="Fetch all tier_a intervals for one ticker on demand, instead of the full nightly run.",
src/cobalt/archiver/config.py:3:Single source: configs/cobalt/watchlists.yaml. Pydantic-validated on
src/cobalt/archiver/config.py:19:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "watchlists.yaml"
src/cobalt/archiver/config.py:37:    tier_a: Tier
src/cobalt/archiver/config.py:38:    tier_b: Tier
src/cobalt/archiver/config.py:39:    tier_c: Tier
src/cobalt/archiver/config.py:44:        tier_c is deliberately excluded (no archiving) — its presence
src/cobalt/archiver/config.py:48:        for tier in (self.tier_a, self.tier_b):
src/cobalt/archiver/config.py:49:            for ticker in tier.tickers:
src/cobalt/archiver/config.py:50:                for interval in tier.intervals:
src/cobalt/archiver/config.py:55:        """All of tier_a's intervals for one ticker (the on-demand backfill path)."""
src/cobalt/archiver/config.py:56:        return [(ticker, interval) for interval in self.tier_a.intervals]
src/cobalt/archiver/config.py:68:        raise ConfigError(f"{CONFIG_PATH}: invalid watchlists config:\n{e}") from e
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

exec
/bin/zsh -lc "nl -ba src/cobalt/session/guard.py | sed -n '123,185p'
nl -ba src/cobalt/archiver/runner.py | sed -n '18,90p'
nl -ba src/cobalt/aset/store.py | sed -n '72,126p'
rg -n 'volume|Volume|Industry|ETF|Exchange|151' 'docs/30 - Design/DATA-SOURCE-MEMO.md' | head -n 35" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
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
   136	    the clock is read once, here.
   137	    """
   138	    clock = clock or session_clock()
   139	    ts = now or clock_mod.now_utc()
   140	    session = clock.session(ts)
   141	
   142	    if session is not BLOCKED_SESSION:
   143	        return session
   144	
   145	    message = block_message(clock, ts, actor)
   146	    logger.error(message)
   147	    (store or SessionBlockStore()).record(
   148	        session=session.value, actor=actor, target=target, reason=message
   149	    )
   150	    raise SessionBlocked(message, session=session, actor=actor)
    18	
    19	from loguru import logger
    20	
    21	from .collector import CollectorError, fetch_bars, resolve_token
    22	from .config import load_config
    23	from .models import Interval
    24	from .report import RunSummary, append_run_report
    25	from .store import BarStore
    26	
    27	GENTLE_SLEEP_SECONDS = 1.2
    28	
    29	
    30	async def _run_targets(targets: list[tuple[str, Interval]], mode: str) -> RunSummary:
    31	    summary = RunSummary(mode=mode)
    32	    store = BarStore()
    33	    store.ensure_schema()
    34	    token = await resolve_token()
    35	
    36	    total = len(targets)
    37	    for i, (ticker, interval) in enumerate(targets, start=1):
    38	        try:
    39	            bars = await fetch_bars(ticker, interval, token)
    40	            rows = store.upsert_bars(bars)
    41	            summary.record_success(ticker, rows)
    42	            logger.info(f"[{i}/{total}] {ticker}/{interval.value}: {rows} rows")
    43	        except CollectorError as e:
    44	            summary.record_failure(ticker, interval.value, str(e))
    45	            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {e}")
    46	        except Exception as e:
    47	            # Any other unexpected error is still a per-ticker failure,
    48	            # never a reason to abort the whole run or store partial data.
    49	            summary.record_failure(ticker, interval.value, f"{type(e).__name__}: {e}")
    50	            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {type(e).__name__}: {e}")
    51	
    52	        if i < total:
    53	            await asyncio.sleep(GENTLE_SLEEP_SECONDS)
    54	
    55	    return summary
    56	
    57	
    58	async def run_full() -> RunSummary:
    59	    """Nightly job: archive tier_a + tier_b per their configured intervals.
    60	
    61	    Writes to whichever database `COBALT_ENV` names (RULING 9)."""
    62	    cfg = load_config()
    63	    targets = cfg.archive_targets()
    64	    logger.info(f"Bar Archiver full run: {len(targets)} (ticker, interval) targets")
    65	    summary = await _run_targets(targets, mode="full")
    66	    path = append_run_report(summary)
    67	    logger.info(
    68	        f"Run complete: {len(summary.tickers)} tickers, {summary.rows_written} rows, "
    69	        f"{len(summary.failures)} failures, {summary.duration_str()}. Report: {path}"
    70	    )
    71	    return summary
    72	
    73	
    74	async def run_backfill(ticker: str) -> RunSummary:
    75	    """On-demand: fetch ALL tier_a intervals for one ticker (a new name
    76	    joining tier_a, or a manual re-fill). Same database rule as
    77	    `run_full` — `COBALT_ENV`, never an argument."""
    78	    cfg = load_config()
    79	    targets = cfg.backfill_targets(ticker)
    80	    logger.info(f"Bar Archiver backfill for {ticker}: {len(targets)} targets")
    81	    summary = await _run_targets(targets, mode=f"backfill:{ticker}")
    82	    path = append_run_report(summary)
    83	    logger.info(
    84	        f"Backfill complete: {summary.rows_written} rows, "
    85	        f"{len(summary.failures)} failures, {summary.duration_str()}. Report: {path}"
    86	    )
    87	    return summary
    88	
    89	
    90	def _archive_nightly() -> None:
    72	                        if statement:
    73	                            conn.execute(statement)
    74	
    75	    def save(self, result: SizingResult, *, now: Optional[datetime] = None) -> int:
    76	        """Persist a card, stamped with the session it was created in.
    77	
    78	        F1 (Charter §3): "every card, alert and note carries the session."
    79	        The session is resolved HERE, in Python, and not derived in SQL
    80	        from `created_at` — the answer depends on the NYSE calendar, and
    81	        the calendar is config. `now` is the test seam; production passes
    82	        nothing. `created_at` keeps its server-side `now()` default: both
    83	        clocks are on this one host, and the alternative (a client
    84	        timestamp) trades a nonexistent skew for a real one.
    85	        """
    86	        # Local import: cobalt.cards.store imports THIS module (for the
    87	        # migration directory), so a module-level import here would be a
    88	        # cycle. The dependency runs one way at import time and both ways
    89	        # at call time, which is the ordinary shape for two tables that
    90	        # are written together.
    91	        from cobalt.cards.models import Actor, CardState, Origin
    92	        from cobalt.cards.store import CardStore
    93	
    94	        inp = result.input
    95	        ts = now or session_clock_mod.now_utc()
    96	        session = session_clock().session(ts)
    97	
    98	        # ONE TRANSACTION FOR THE CARD AND ITS FIRST STATE (F7).
    99	        # "No card exists without a state" is not a habit the callers
   100	        # keep — it is this `with` block. A crash between the INSERT and
   101	        # the genesis transition rolls both back, so there is no window
   102	        # in which a state-less card is reachable.
   103	        conn = self._connect()
   104	        conn.autocommit = False
   105	        try:
   106	            with conn.cursor() as cur:
   107	                cur.execute(
   108	                    """
   109	                    INSERT INTO aset_sizings (
   110	                        ticker, grade, direction, sheet_mode,
   111	                        risk_budget, entry, stop, per_share_risk, shares,
   112	                        used_risk, last_price, price_source, warnings, session,
   113	                        state, state_at, origin
   114	                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
   115	                    RETURNING id
   116	                    """,
   117	                    (
   118	                        inp.ticker,
   119	                        inp.grade.value,
   120	                        inp.direction.value,
   121	                        inp.sheet_mode.value,
   122	                        result.risk_budget,
   123	                        inp.entry,
   124	                        inp.stop,
   125	                        result.per_share_risk,
   126	                        result.shares,
44:- `MASTER_COLUMNS` (indices `0`–`150`, 151 total) — CONFIRMED: a single
45:  `c=0..150` request returned exactly 151 named columns (full list in
72:  Sector, Industry, Country, Market Cap, P/E, Price, Change, Volume`).
74:- `v=152&c=0..150` (all indices) → 200, **all 151 named columns**,
77:  `No, Ticker, Company, Sector, Industry, Country, Market Cap, P/E,
89:  Average/Relative Volume, Price, Change, Volume, **Earnings Date**,
90:  Target Price, IPO Date, After-Hours Close/Change/Volume, Book/Cash
92:  Shortable, Short Interest, Float %**, OHL, Trades, [ETF-only block:
93:  Asset Type, ETF Type, Region, Category, Tags, AUM, NAV, Net Flows
95:  Exchange, Dividend TTM/Ex-Date, 52-Week Range, **News Time, News URL,
131:  Volume, Open Int., Type, IV, Delta, Gamma, Theta, Vega, Rho`.
183:  → 200, 30 rows, 14 columns (`Ticker, Name, Type, Sector, Industry,
213:  columns already present in the Screener's 151-column export instead
220:**Fixed columns, all intervals:** `Date, Open, High, Low, Close, Volume`
221:(6 columns) — Volume is **present at every granularity tested**,
222:directly resolving §7's "re-verify volume availability" flag. **CONFIRMED.**
334:| **Screener** | Full 151-column field universe; arbitrary filter/column combos; multiple valid `v=` view IDs | `ft=` param meaning unverified | **Pillar 1 backbone** (already validated by existing `FinvizApiClient` usage) |
336:| **Stock** | 6-col OHLCV at 8 real granularities (d/w/m/i1/i5/i15/i30/h); volume present everywhere; depth tiers empirically mapped | **History-depth param name unconfirmed** (highest-priority Phase B item) | **Critical** — setups engine + backtesting both depend on this |
352:1. **§7 "single-stock up-to-the-minute OHLC bars (re-verify volume
353:   availability)" — RESOLVED, not a contradiction.** Volume is present
369:   this.** None of the 151 screener columns nor any of the ten other
377:   boolean are all present in the Screener's 151-column export
440:| `g=sector&v=120` | 11 (one per GICS-style sector) | 15 — valuation/fundamentals view: `No., Name, Market Cap, P/E, Forward P/E, PEG, P/S, P/B, P/C, P/Free Cash Flow, EPS growth past 5Y, EPS growth next 5Y, Sales growth past 5Y, Change, Volume` |
441:| `g=sector&v=140` | 11 | 12 — **different view**, performance-oriented: `No., Name, Performance (Week/Month/Quarter/Half Year/Year/YTD), Average Volume, Relative Volume, Change, Volume` |
544:| **Screener**       | Full 151-column field universe; arbitrary filter/column combos; multiple valid `v=` view IDs; **also the confirmed per-ticker-news path** (cols 135–137)                                          | `ft=` param meaning unverified                                                                           | **Pillar 1 backbone**, plus the working per-ticker-news mechanism                                                                 |
546:| **Stock**          | 6-col OHLCV at **9** real granularities (i1/i2/i5/i15/i30/h/d/w/m); volume present everywhere; depth tiers empirically mapped and re-verified stable across a fresh pull                          | History-depth param name still unconfirmed (Phase B's top item, unchanged)                               | **Critical** — `i2` is Dejan's actual trading timeframe and is now confirmed in the same ~2-week live-detection tier as `i1`/`i5` |

exec
/bin/zsh -lc "nl -ba src/cobalt/archiver/config.py | sed -n '20,62p'
rg -n '"'^tier_|''^  intervals:'"' configs/cobalt/watchlists.yaml
nl -ba src/cobalt/jobs/cli.py | sed -n '1,50p'
nl -ba src/cobalt/jobs/entrypoint.py | sed -n '1,65p'
rg -n 'importlib|__import__|cobalt.archiver|from .*archiver|runner' src/cobalt/jobs src/cobalt/heartbeat src/cobalt/backup src/cobalt/cli.py
nl -ba 'docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md' | sed -n '122,141p;175,217p;234,264p'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
    20	
    21	
    22	class ConfigError(RuntimeError):
    23	    """Config missing or invalid — crash loudly."""
    24	
    25	
    26	class Tier(BaseModel):
    27	    model_config = ConfigDict(extra="forbid")
    28	
    29	    description: str = Field(min_length=1)
    30	    intervals: list[Interval]
    31	    tickers: list[str]
    32	
    33	
    34	class WatchlistsConfig(BaseModel):
    35	    model_config = ConfigDict(extra="forbid")
    36	
    37	    tier_a: Tier
    38	    tier_b: Tier
    39	    tier_c: Tier
    40	
    41	    def archive_targets(self) -> list[tuple[str, Interval]]:
    42	        """Every (ticker, interval) pair this config says to archive.
    43	
    44	        tier_c is deliberately excluded (no archiving) — its presence
    45	        in the config is for future use only.
    46	        """
    47	        targets: list[tuple[str, Interval]] = []
    48	        for tier in (self.tier_a, self.tier_b):
    49	            for ticker in tier.tickers:
    50	                for interval in tier.intervals:
    51	                    targets.append((ticker, interval))
    52	        return targets
    53	
    54	    def backfill_targets(self, ticker: str) -> list[tuple[str, Interval]]:
    55	        """All of tier_a's intervals for one ticker (the on-demand backfill path)."""
    56	        return [(ticker, interval) for interval in self.tier_a.intervals]
    57	
    58	
    59	def load_config() -> WatchlistsConfig:
    60	    if not CONFIG_PATH.exists():
    61	        raise ConfigError(f"Watchlists config not found: {CONFIG_PATH}.")
    62	    raw = yaml.safe_load(CONFIG_PATH.read_text())
55:tier_a:
57:  intervals: [i1, i2, i5, i15, i30]
245:tier_b:
247:  intervals: [i5, i30]
275:tier_c:
277:  intervals: []
     1	"""`cobalt jobs` — F17's command surface, plus `cobalt stop` / `resume`.
     2	
     3	    cobalt jobs list                     the table, as F18 reads it
     4	    cobalt jobs register                 upsert every row from jobs.yaml
     5	    cobalt jobs check                    run the watchdog, print findings
     6	    cobalt jobs run LABEL -- CMD ARGS    wrap any command as that job
     7	    cobalt stop  [--phrase "COBALT STOP"]
     8	    cobalt resume
     9	
    10	`jobs run` is the plist-facing half of the wrapper: a launchd job whose
    11	program is not Python (or is a `uv run` of something else) gets its row,
    12	its heartbeat and its exit code by being launched through this.
    13	"""
    14	
    15	from __future__ import annotations
    16	
    17	import argparse
    18	import subprocess
    19	import sys
    20	
    21	from cobalt import env
    22	
    23	from . import killswitch
    24	from .config import load_job_registry
    25	from .models import RED_STATES
    26	from .store import JobStore
    27	from .watchdog import sweep
    28	from .wrapper import JobStopped, job_run
    29	
    30	
    31	def _store() -> JobStore:
    32	    store = JobStore()
    33	    store.ensure_schema()
    34	    return store
    35	
    36	
    37	def cmd_list(args: argparse.Namespace) -> None:
    38	    store = _store()
    39	    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    40	    print(killswitch.read(store).describe())
    41	    rows = store.all()
    42	    if not rows:
    43	        print("\nno jobs registered — run `cobalt jobs register`")
    44	        return
    45	    red_values = {s.value for s in RED_STATES}
    46	    print(
    47	        f"\n{'LABEL':<28} {'KIND':<9} {'STATE':<9} {'SRC':<8} {'LAST FINISH':<20} "
    48	        f"{'EXIT':<5} CADENCE"
    49	    )
    50	    for r in rows:
     1	"""The decorator half of F17b — one line at each scheduled entry point.
     2	
     3	    from cobalt.jobs.entrypoint import as_job
     4	
     5	    with as_job("com.cobalt.prefill-daily", skip=args.dry_run) as run:
     6	        ...
     7	
     8	WHY A SEPARATE HELPER and not `job_run` directly. Three things every
     9	entry point needs and none of them belongs in the wrapper:
    10	
    11	* `skip=` — a DRY RUN IS NOT A RUN. `prefill daily --dry-run` writes
    12	  nothing and must not satisfy the MISSED probe, or "I checked what it
    13	  would do" would silence the alarm that says it never did it.
    14	* F19's LOG GUARD, installed once, here. Every scheduled job writes to
    15	  `logs/*.log`, those files are read over Tailscale and pasted into
    16	  reports, and a secret reaches a log the same way it reaches a DM.
    17	  Installing it at the entry point means a new job gets it by using this.
    18	* the STOPPED case exits 0 with a printed line rather than a traceback.
    19	
    20	An ad-hoc `uv run prefill daily` goes through this too, and that is
    21	correct: a manual catch-up run IS a run of that job, it belongs in the
    22	row, and it should stop the MISSED probe firing an hour later.
    23	"""
    24	
    25	from __future__ import annotations
    26	
    27	from contextlib import contextmanager
    28	from typing import Optional
    29	
    30	from loguru import logger
    31	
    32	from .wrapper import JobRun, JobStopped, job_run
    33	
    34	
    35	@contextmanager
    36	def as_job(label: str, *, skip: bool = False, store=None):
    37	    """Wrap a scheduled entry point. Yields a `JobRun`, or a bare one
    38	    when `skip` is set."""
    39	    from cobalt.redact import install_log_guard
    40	
    41	    install_log_guard()
    42	
    43	    if skip:
    44	        logger.info(
    45	            "F17: {} is a DRY RUN — no jobs row is touched. A dry run is not a run, "
    46	            "and must not satisfy the MISSED probe.",
    47	            label,
    48	        )
    49	        from .config import load_job_registry
    50	
    51	        yield JobRun(load_job_registry().spec(label))
    52	        return
    53	
    54	    with job_run(label, store=store) as run:
    55	        yield run
    56	
    57	
    58	__all__ = ["JobStopped", "as_job"]
src/cobalt/cli.py:456:    from cobalt.heartbeat.runner import green_summary_at, interval_min
src/cobalt/heartbeat/probes.py:228:    row = store.get("com.cobalt.archiver")
src/cobalt/heartbeat/probes.py:232:    spec = load_job_registry().spec("com.cobalt.archiver")
src/cobalt/heartbeat/probes.py:636:    from cobalt.seatusage.runner import JOB_LABEL
src/cobalt/heartbeat/cli.py:20:from .runner import run_beat, take_beat
src/cobalt/heartbeat/__init__.py:9:`runner.out_of_band()` for what was searched for and what was found —
src/cobalt/heartbeat/__init__.py:15:from .runner import run_beat, take_beat
src/cobalt/jobs/wrapper.py:9:    with job_run("com.cobalt.archiver") as run:
   122	### Step 2 — Migration 0004 as files, bounded rollback, direction-aware proof, placement (plan D4)
   123	- `src/cobalt/db_migrations/0004_radar_pool.sql` + `0004_radar_pool.rollback.sql`: exactly plan D4's DDL,
   124	  grants, ownership, the `aset.account_mode` seed and the rollback (header states its cost).
   125	- `db_migrations/__init__.py`: append to `FORWARD`, prepend to `REVERSE`, docstring.
   126	- `db_migrations/cli.py`: `DIGEST_EXCLUDED_COLUMNS` + `account_mode`, `pool_member_id`; `--rollback` REQUIRES
   127	  `--down-to NNNN` (refuses before connecting, lists targets) and runs only newer reverse files, newest first;
   128	  verdicts `CREATED` / `DROPPED` / `CHANGED` computed BEFORE commit; `CHANGED` rolls back.
   129	- `placement.py`: `radar_pool`, `radar_membership` → new `CREATED_TABLES`, in `PLACEMENT` and the proof set.
   130	- **Offline tests (`test_radar_migration.py`, `test_tenancy.py`):** 0004 DDL ↔ placement agreement (parse the
   131	  SQL text); `--down-to` file selection; refusal without `--down-to` with no connection attempted; verdict
   132	  function table; abort-before-commit ordering with a fake connection.
   133	- **`requires_db` tests (hub):** idempotent migrate; round trip digests; 0003 columns survive; seed row
   134	  present/absent; J1 (plan D9); membership CHECKs and both unique indexes reject bad rows.
   135	
   136	### Step 3 — `cobalt db query` (plan D10)
   137	- `src/cobalt/db_query.py`, registered as `db query`. Guard pure and separately importable.
   138	- **Offline tests (`test_db_query.py`):** every refused class exits 2 naming the token; keyword in a literal
   139	  passes; multi-statement; data-modifying CTE; `set_config('role', …)`; `cobalt_brain` without `--prod` refuses
   140	  before connecting; the `psycopg.connect` lint still passes.
   141	- **`requires_db`:** READ ONLY belt, timeout, `current_user`, user side reads `system.bars` qualified.
   175	### Step 6 — Screener collector, cache, replay (plan D6)
   176	- `src/cobalt/radar/collector.py`: `ScreenerCollector` protocol; `FinvizScreenerCollector` through
   177	  `finviz_get` (screens with optional `&ft=`; lists via `t=` chunks); one process-wide token bucket; cache
   178	  path; header-name parse; `SourceFailure` on missing header / non-CSV / HTTP error / redirect.
   179	- Capture ONE real export header with the fixture filter (network + token) and pin `required_headers`,
   180	  `metric_headers`, `not_equity` from it; cite the capture file (header row only) in the report.
   181	- `src/cobalt/radar/replay.py`: `ReplayCollector` serving snapshots by virtual clock; pure
   182	  `snapshots_from_bars(bars, screen, prior_sessions)` (RVOL proxy per plan D15 H4; only the fixture screen's
   183	  filter codes; any other code fails loud); `cobalt radar replay-build <day>` reads `system.bars` (DB, hub).
   184	- **Offline tests (`test_radar_collector.py`, `test_radar_replay.py`):** recorded-CSV parse; header mismatch;
   185	  HTML body; redirect; `t=` chunking; token bucket (fake clock); cache path gitignored; scrub; snapshot synthesis
   186	  from generated bars.
   187	
   188	### Step 7 — Pool decision + store (plan D3, D5)
   189	- `src/cobalt/radar/pool.py`: pure `decide(candidates, open_members, blocks, sources, now) → transitions`
   190	  implementing plan D3's rank key and precedence table exactly.
   191	- `src/cobalt/radar/store.py`: `RadarStore` (`SIDE = Side.SYSTEM`) — S1 membership transitions and S2 pool row,
   192	  each one transaction, idempotent per plan D5; `assert_writable("radar.<stage>")`.
   193	- **Offline tests (`test_radar_pool.py`):** plan D15 O2; one table test per D3 step; rank key with mixed
   194	  metrics never compares volume to RVOL; first_from before/after 10:00; cap lowered below held; streak
   195	  reset/freeze/leave on the (N+1)-th scan; rollover closes the prior day.
   196	- **`requires_db` (`test_radar_store.py`):** idempotent re-apply of a `scan_id`; unique indexes; store lint.
   197	
   198	### Step 8 — Bar poller + aggregation (plan D7)
   199	- `src/cobalt/radar/poller.py`: admitted members in rank order, `fetch_bars` through the shared bucket;
   200	  watermark per `(ticker, 'i1')`; closed bars only; `BarStore.upsert_bars`; per-ticker failure →
   201	  `poll_failures`.
   202	- `src/cobalt/archiver/aggregate.py`: pure `aggregate(bars, minutes)`, floored from 00:00 ET, explicit OHLCV.
   203	- **Offline tests (`test_radar_poller.py`, `test_archiver_aggregate.py`):** watermark with a fake store; open bar
   204	  excluded; failure recorded; aggregation incl. a DST day and a missing minute.
   205	- **`requires_db`:** upsert idempotent; aggregate vs stored i2 agreement % on the replay day (hub, H7).
   206	
   207	### Step 9 — Resident runner, stages, registry, plist (plan D5)
   208	- `src/cobalt/radar/runner.py` + `cobalt radar run` / `cobalt radar scan --once [--replay <day> --from HH:MM
   209	  --to HH:MM]`: `job_run`; `should_keep_running`; session asked first; S1 → S2 → S3 → S4 with the session asked
   210	  before each commit; partial-failure handling and `failed_stage` stamping per plan D5; `scan_id` monotonic.
   211	- `jobs.yaml`: `com.cobalt.radar` row per plan D5; `reads:` derived by instrumenting one offline
   212	  `scan --once` with fakes (patch `open` / `Path.read_text`, repo-relative paths), each with `# file.py:line`.
   213	- `ops/com.cobalt.radar.plist` per plan D5 (`PATH` as the archiver plist; no double hyphen in XML comments);
   214	  `ops/README.md` radar handover.
   215	- **Offline tests (`test_radar_runner.py`, `test_jobs.py`):** plan D15 O3, O4; idle cycle makes no HTTP call;
   216	  market_reset cycle writes nothing (fakes); kill switch → exit 0; `cobalt validate` exit 0 (registry ↔ plist);
   217	  watchdog: stale heartbeat on this resident → `zombie`.
   234	### Step 12 — Propose / apply (plan D13)
   235	- `src/cobalt/radar/propose.py` + `cobalt radar screens propose --pool-block <file> [--ft-compare]`,
   236	  `cobalt radar lists propose`, `cobalt radar screens apply --hitl <token> --sha256 <sha>`,
   237	  `cobalt radar lists apply --hitl <token> --sha256 <sha>` — derivation, `# from:` and `# PROPOSED` markers,
   238	  pool-block validation, diff + sha256, refusals, write_ids + restore lines.
   239	- **Offline tests (`test_radar_propose.py`, `tmp_path`):** prose → blocks from the screen fixture (no second
   240	  screen definition); `f` mismatch between the export line and the filters line refuses; invalid pool-block file
   241	  refused; diff insertions only; sha stable; `--ft-compare` with mocked HTTP adds `ft: 4` only where sets differ;
   242	  lists proposal round-trips to the same targets as the YAML.
   243	- **`requires_db` (hub, H11):** apply writes, second apply refuses, `restore --write-id` byte-identical.
   244	
   245	### Step 13 — RESTARTS tool, offline gate, report (end of RUN A)
   246	- `src/cobalt/jobs/restarts.py` + `cobalt jobs restarts <git-range>`: plan §3 rule; static ast walk from each
   247	  resident's `imports:`; unresolvable dynamic import or missing `imports:` → all residents; unclassified →
   248	  ESCALATE line; untracked files included when the range ends at the working tree.
   249	  **Tests (`test_jobs_restarts.py`):** each rule; a string-loaded module declared vs undeclared.
   250	- Run plan D15 O1–O10. One row each: PASS / FAIL / NOT RUN + the command and its key output line.
   251	- DevDocs for every new or changed `.py` + INDEX lines.
   252	- RESTARTS: `uv run cobalt jobs restarts main...HEAD` output pasted as the derivation table.
   253	- Write the report (§5). Print `DONE`.
   254	
   255	### Step 14 — RUN B: stage 2 (plan D14)
   256	- `archiver/config.py` reads targets from the Lists note via `cobalt.radar.notes` (read + validate only);
   257	  missing or failed note → loud.
   258	- `cobalt radar sources [--json] [--archiver-diff --yaml-rev <sha>]`.
   259	- Tests re-targeted to the lists fixture; delete `configs/cobalt/watchlists.yaml` from the working tree (the
   260	  hub commits the deletion).
   261	- **Offline tests:** a Lists note rendered by `lists propose` from `watchlists.yaml` at RUN A's sha (the hub
   262	  gives it) into `tmp_path`; archiver-diff between it and the YAML at that sha is empty (the synthetic lists
   263	  fixture is NOT the comparison). **`requires_db` (hub, H12):** `archiver --backfill <T>` from the note.
   264	- Update the report (stage-2 file list, `cobalt jobs restarts <RUN A sha>...HEAD`). Print `DONE`.

codex
Several fixes remain incomplete. The stickiness steps can reset a retained member’s streak every scan; the runner has no hook to check the session immediately before the existing stores commit; and rollback invokes a restart command that the code reset removes. The claimed nightly bar repair also excludes some radar members.
exec
/bin/zsh -lc "python3 -c 'streak = 0
for scan in range(1, 6):
    winners = [\"newcomer\"]
    streak += 1
    if streak <= 3:
        winners = [\"incumbent\"]
    if \"incumbent\" in winners:
        streak = 0
    print(scan, winners, streak)'" in /Users/cobalt/cobalt-wt/s2-p1-radar-pool
 succeeded in 0ms:
1 ['incumbent'] 0
2 ['incumbent'] 0
3 ['incumbent'] 0
4 ['incumbent'] 0
5 ['incumbent'] 0

codex
Round 3: **4 blockers resolved, 4 open; 3 risks resolved, 2 open.** These statuses assess the rewritten instructions, not implementation readiness proven by tests.

References below: **plan** = [plan-s2-p1-2026-09-10.md](</Users/cobalt/cobalt-wt/s2-p1-radar-pool/docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md>); **brief** = [s2-p1-brief.md](</Users/cobalt/cobalt-wt/s2-p1-radar-pool/docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md>).

| Round-2 blocker | Status | Evidence in rewrite |
|---|---|---|
| **1. Account mode** | **RESOLVED** | Standing fallback, refusal, transactional stamp and attestation SIM control agree across `plan:233`, `plan:237`, `plan:309`; `brief:67`, `brief:224`. |
| **2. Pool contract and writer integration** | **OPEN** | Parser dispatch, mirror, fixtures and config separation are fixed (`plan:70`, `plan:78`, `plan:259`; `brief:159`). However, proposal-to-apply input continuity remains unspecified at `plan:265`, `plan:268`; `brief:235`. |
| **3. Ranking and stickiness** | **OPEN** | Mixed metrics and hard-cap precedence are defined, but retention mutates W before step 9 resets its members’ streaks (`plan:129`, `plan:131`, `plan:132`). The brief requires this table exactly while also requiring departure on scan N+1 (`brief:190`, `brief:195`). |
| **4. Sol credentials and DB tests** | **RESOLVED** | Explicit credential prohibition and separate offline/hub gates at `plan:282`, `plan:297`, `plan:318`; `brief:15`, `brief:28`, `brief:87`. |
| **5. Restart deployment and rollback** | **OPEN** | Import analysis is specified (`plan:322`; `brief:246`), but L5’s rollback invokes the new tool **after** L2 removes its implementation (`plan:364`, `plan:367`). |
| **6. Transaction boundaries and market reset** | **OPEN** | Separate transactions replace the whole-cycle atomicity claim (`plan:209`; `brief:79`). But checking immediately before commits inside existing store methods has no specified implementation seam (`plan:211`; `brief:209`). |
| **7. Optional `ft` support** | **RESOLVED** | Validated optional field ships initially and reaches requests: `plan:70`, `plan:219`, `plan:266`; `brief:159`, `brief:177`. |
| **8. Observable throttle transport** | **RESOLVED** | Metrics expose status, redirect history and failures before status raising; followed-redirect tests are explicit: `plan:217`, `plan:347`; `brief:105`, `brief:116`. |

| Round-2 risk | Status | Evidence in rewrite |
|---|---|---|
| **1. Watermark scope and deferred repairs** | **OPEN** | `(ticker, 'i1')` is fixed (`plan:225`; `brief:200`). The blanket nightly-repair claim at `plan:226`, `plan:396` conflicts with archive targets restricted to configured list intervals (`plan:274`; `brief:256`). |
| **2. Migration proof and commit ordering** | **RESOLVED** | Intentional drops are direction-aware; unexpected changes abort before commit; offline and DB checks cover both: `plan:200`, `plan:201`; `brief:126`, `brief:130`. |
| **3. Achieved polling cadence** | **RESOLVED** | A measured acceptance threshold now exists: p95 successful per-member gap ≤1.5×poll interval (`plan:228`, `plan:307`; `brief:205`, via H7). This accepts p95 ≤90 seconds; it does **not** guarantee two polls in every two-minute bar. |
| **4. Scan freshness versus bar freshness** | **OPEN** | Explicit poll failures now reach F18 (`plan:212`, `plan:254`; `brief:200`, `brief:220`). A successful response containing only stale bars still has no freshness failure rule. |
| **5. Grammar/exact-string check ownership** | **RESOLVED** | Suite owns the grammar check; hub owns the exact-string check before every commit (`plan:81`, `plan:382`; `brief:173`, `brief:250`, `brief:281`). |

**BLOCKERS**

1. **B2 — Apply cannot reproduce the specified proposal from its declared inputs.** `screens propose` receives `--pool-block` and optionally obtains comparison-dependent `ft` decisions. `screens apply` receives only a token and hash, yet must “re-derive” everything. Specify a saved proposal artifact containing the approved inputs/results, or explicit reproducible apply inputs. The hash alone cannot supply them. References: `plan:265–268`; `brief:235–241`.

2. **B3 — Sticky retention can last forever.** With cap 1, incumbent A ranked below newcomer B, and stickiness 3: step 7 increments A’s streak; step 8 replaces B with A; step 9 resets A’s streak to zero. Repeating this never reaches departure. Keep provisional ranking winners separate from final retained membership, and reset only on genuine recovery into the provisional winners. References: `plan:129–137`; `brief:190–195`.

3. **B5 — The rollback restart command disappears before invocation.** L2 resets to `pre-s2-p1`; L5 then calls `cobalt jobs restarts`, introduced by this change. Derive and save rollback actions before resetting, or execute the tool from a retained checkout containing it. References: `plan:364`, `plan:367`; `brief:246`.

4. **B6 — Internal commits remain inaccessible to the runner’s checks.** `TraderSettingsStore.put` commits internally (`src/cobalt/settings/store.py:90`); `BarStore.upsert_bars` commits through its connection context (`src/cobalt/archiver/store.py:73`). A runner check before calling either cannot check immediately before its commit. Specify the store hook/transaction API and test boundary crossing inside those methods, including between S4 tickers. Current crossing tests only address the gap between S1 and S2. References: `plan:209–211`, `plan:289`; `brief:199–210`.

5. **Additional deployment blocker — Stage 1 requires a stage-2 CLI.** L7/L8 require `radar sources` and `--archiver-diff` before L9 merges stage 2. The brief introduces those commands only in RUN B, step 14. Build the inspection/equality-proof commands in RUN A; retain the archiver switch and YAML deletion in RUN B. References: `plan:369–371`; `brief:18`, `brief:255–263`.

**RISKS**

- **R1 remains:** nightly i1 repair does not cover screen-only names or lists without i1 archiving. Current tier B archives i5/i30; tier C archives nothing. Narrow the repair claim or specify coverage. Full exports are already fetched, so an overlap repair need not add HTTP requests.
- **R4 remains:** fresh scans plus successful stale exports can remain GREEN indefinitely. Define per-member data freshness, persistent failure onset and recovery, with a stale-200 acceptance case.
- E9’s outside-branch report redaction remains a pre-commit gate (`plan:406`).

**VERDICT: BLOCKED — final review does not clear this plan for build.**

Read-only review; no DB or live-network validation was run.
tokens used
67,970
Round 3: **4 blockers resolved, 4 open; 3 risks resolved, 2 open.** These statuses assess the rewritten instructions, not implementation readiness proven by tests.

References below: **plan** = [plan-s2-p1-2026-09-10.md](</Users/cobalt/cobalt-wt/s2-p1-radar-pool/docs/40 - DevDocs/reports/_inflight/plan-s2-p1-2026-09-10.md>); **brief** = [s2-p1-brief.md](</Users/cobalt/cobalt-wt/s2-p1-radar-pool/docs/40 - DevDocs/reports/_inflight/s2-p1-brief.md>).

| Round-2 blocker | Status | Evidence in rewrite |
|---|---|---|
| **1. Account mode** | **RESOLVED** | Standing fallback, refusal, transactional stamp and attestation SIM control agree across `plan:233`, `plan:237`, `plan:309`; `brief:67`, `brief:224`. |
| **2. Pool contract and writer integration** | **OPEN** | Parser dispatch, mirror, fixtures and config separation are fixed (`plan:70`, `plan:78`, `plan:259`; `brief:159`). However, proposal-to-apply input continuity remains unspecified at `plan:265`, `plan:268`; `brief:235`. |
| **3. Ranking and stickiness** | **OPEN** | Mixed metrics and hard-cap precedence are defined, but retention mutates W before step 9 resets its members’ streaks (`plan:129`, `plan:131`, `plan:132`). The brief requires this table exactly while also requiring departure on scan N+1 (`brief:190`, `brief:195`). |
| **4. Sol credentials and DB tests** | **RESOLVED** | Explicit credential prohibition and separate offline/hub gates at `plan:282`, `plan:297`, `plan:318`; `brief:15`, `brief:28`, `brief:87`. |
| **5. Restart deployment and rollback** | **OPEN** | Import analysis is specified (`plan:322`; `brief:246`), but L5’s rollback invokes the new tool **after** L2 removes its implementation (`plan:364`, `plan:367`). |
| **6. Transaction boundaries and market reset** | **OPEN** | Separate transactions replace the whole-cycle atomicity claim (`plan:209`; `brief:79`). But checking immediately before commits inside existing store methods has no specified implementation seam (`plan:211`; `brief:209`). |
| **7. Optional `ft` support** | **RESOLVED** | Validated optional field ships initially and reaches requests: `plan:70`, `plan:219`, `plan:266`; `brief:159`, `brief:177`. |
| **8. Observable throttle transport** | **RESOLVED** | Metrics expose status, redirect history and failures before status raising; followed-redirect tests are explicit: `plan:217`, `plan:347`; `brief:105`, `brief:116`. |

| Round-2 risk | Status | Evidence in rewrite |
|---|---|---|
| **1. Watermark scope and deferred repairs** | **OPEN** | `(ticker, 'i1')` is fixed (`plan:225`; `brief:200`). The blanket nightly-repair claim at `plan:226`, `plan:396` conflicts with archive targets restricted to configured list intervals (`plan:274`; `brief:256`). |
| **2. Migration proof and commit ordering** | **RESOLVED** | Intentional drops are direction-aware; unexpected changes abort before commit; offline and DB checks cover both: `plan:200`, `plan:201`; `brief:126`, `brief:130`. |
| **3. Achieved polling cadence** | **RESOLVED** | A measured acceptance threshold now exists: p95 successful per-member gap ≤1.5×poll interval (`plan:228`, `plan:307`; `brief:205`, via H7). This accepts p95 ≤90 seconds; it does **not** guarantee two polls in every two-minute bar. |
| **4. Scan freshness versus bar freshness** | **OPEN** | Explicit poll failures now reach F18 (`plan:212`, `plan:254`; `brief:200`, `brief:220`). A successful response containing only stale bars still has no freshness failure rule. |
| **5. Grammar/exact-string check ownership** | **RESOLVED** | Suite owns the grammar check; hub owns the exact-string check before every commit (`plan:81`, `plan:382`; `brief:173`, `brief:250`, `brief:281`). |

**BLOCKERS**

1. **B2 — Apply cannot reproduce the specified proposal from its declared inputs.** `screens propose` receives `--pool-block` and optionally obtains comparison-dependent `ft` decisions. `screens apply` receives only a token and hash, yet must “re-derive” everything. Specify a saved proposal artifact containing the approved inputs/results, or explicit reproducible apply inputs. The hash alone cannot supply them. References: `plan:265–268`; `brief:235–241`.

2. **B3 — Sticky retention can last forever.** With cap 1, incumbent A ranked below newcomer B, and stickiness 3: step 7 increments A’s streak; step 8 replaces B with A; step 9 resets A’s streak to zero. Repeating this never reaches departure. Keep provisional ranking winners separate from final retained membership, and reset only on genuine recovery into the provisional winners. References: `plan:129–137`; `brief:190–195`.

3. **B5 — The rollback restart command disappears before invocation.** L2 resets to `pre-s2-p1`; L5 then calls `cobalt jobs restarts`, introduced by this change. Derive and save rollback actions before resetting, or execute the tool from a retained checkout containing it. References: `plan:364`, `plan:367`; `brief:246`.

4. **B6 — Internal commits remain inaccessible to the runner’s checks.** `TraderSettingsStore.put` commits internally (`src/cobalt/settings/store.py:90`); `BarStore.upsert_bars` commits through its connection context (`src/cobalt/archiver/store.py:73`). A runner check before calling either cannot check immediately before its commit. Specify the store hook/transaction API and test boundary crossing inside those methods, including between S4 tickers. Current crossing tests only address the gap between S1 and S2. References: `plan:209–211`, `plan:289`; `brief:199–210`.

5. **Additional deployment blocker — Stage 1 requires a stage-2 CLI.** L7/L8 require `radar sources` and `--archiver-diff` before L9 merges stage 2. The brief introduces those commands only in RUN B, step 14. Build the inspection/equality-proof commands in RUN A; retain the archiver switch and YAML deletion in RUN B. References: `plan:369–371`; `brief:18`, `brief:255–263`.

**RISKS**

- **R1 remains:** nightly i1 repair does not cover screen-only names or lists without i1 archiving. Current tier B archives i5/i30; tier C archives nothing. Narrow the repair claim or specify coverage. Full exports are already fetched, so an overlap repair need not add HTTP requests.
- **R4 remains:** fresh scans plus successful stale exports can remain GREEN indefinitely. Define per-member data freshness, persistent failure onset and recovery, with a stale-200 acceptance case.
- E9’s outside-branch report redaction remains a pre-commit gate (`plan:406`).

**VERDICT: BLOCKED — final review does not clear this plan for build.**

Read-only review; no DB or live-network validation was run.
