# ADR-0008 — Two-layer data model: user data vs system data

Date: 2026-09-08
Status: Accepted (architect spike, Fable 5.1; rulings 0, a–g decided-with-veto by
Dejan 09-08, one per message; implemented by an Opus 5 lead-developer session on
`sprint-2/data-model`)
Implements: **L32** (user-data / system-data law, 09-05; tenancy R2 09-06) and
**L31** (names rule, 09-06). Relates to: ADR-0001 (trade_defs as data — superseded
in part: the repo no longer carries populated defs), ADR-0004 (L28, the one vault
write path — reused unchanged, frontmatter site included), ADR-0005/0006 (RULING 7
environment law and the one connection factory — extended, not replaced).
Gates: SPRINT-LADDER S2-P1 line 0.

## Context

Cobalt-the-system is only the schema and engine that make any trader's strategies
pluggable: taxonomy anatomy (regime, range, gap, extension, leg, session clock), the
card engine, the radar, alerts, the rules-engine schema. Everything named after a
trade, everything SMB- or cheat-sheet-derived, every setting that is one trader's
choice, and every note in `1 - Trading` is user data — never shipped to or visible
to another Cobalt user (L32).

On 2026-09-08 the code did not know the difference:

- Every new-core table sat in `public` of `cobalt_brain` beside 17 old-tree tables
  (`memory_logs`, `graph_nodes`, `graph_edges`, `hitl_proposals`,
  `browser_fast_path`, `instruments`, `market_snapshots`, `daily_in_play`,
  `key_levels`, `news_events`, `news_mentions`, `order_fills`, `strategy_signals`,
  `system_alerts`, `themes`, `trades`, `trading_accounts`). One login role,
  `cobalt`, the docker superuser, owned all of it. `search_path` was
  `"$user", public`.
- The 13 populated trade_defs were committed YAML under
  `configs/cobalt/taxonomy/trade_defs/`, cross-checked against
  `cameron_grid.yaml` (a person's name in a config key, L31) and
  `variables/<id>.yaml`. The same 13 defs existed a second time, verbatim, inside
  the 22 strategy notes written on 09-06 (`1 - Trading/4 - Strategies/<note>.md`,
  `cobalt:section definition` units) — a one-path violation waiting for the first
  edit to either copy.
- The vault key (`trade_def:` frontmatter, kebab: `big-dog`, `nine-ema-scalp`) and
  the YAML key (`id:`, snake: `big_dog`, `ema9_scalp`) were not inter-derivable
  for 3 of 13, and nothing in the repo owned the map.
- 69 trade notes in `1 - Trading/2 - Trades/` carried `strategy:` as free text
  (33 blank; aliases like `Big Dawg`, `Offside Scalp`, `Fashionable Late Scalp`;
  leading spaces and doubled quotes from Templater) and none carried `trade_def:`,
  so every `## Instances` dataview rendered empty.
- The trader's own dollar sheet, enabled grades, reduced mode, `.htk` template and
  step-downs lived in committed config (`configs/cobalt/aset.yaml`,
  `daymode.yaml`).
- The 09-06 strategy-note batch was hand-work with no L28 record; its ledger line
  cited a restic snapshot ("09-05 21:40") that does not exist.

Facts verified read-only during the spike, and binding on the design:

- `user` is a **reserved word** in PostgreSQL 16 (`pg_get_keywords` catcode R);
  `system` is unreserved.
- `cobalt` is `rolsuper = true`; superusers bypass every grant regardless of
  `INHERIT`.
- `pg_read_all_data` exists (PG14+).
- `VaultWriter.upsert_region` (ADR-0004) already is the marker-less frontmatter
  write site: 3-way merge, write_id, restore. A first write on a unit with no
  baseline takes Cobalt's body wholesale (base := human) — exactly right for
  migrating Cobalt-seeded units.
- The `cfg()` key grammar (§13.1) and `per_trade(<id>)` scope accept `[a-z0-9_]`
  only: a kebab slug cannot appear verbatim in a tunable key, and would read as
  subtraction to a future predicate parser.
- The SSD restic repo holds three snapshots: `24f3f36b` 2026-09-06 08:30:23,
  `472ade44` 09-06 21:40:08, `0d55d7b5` 09-07 21:40:03. The 09-06 batch began
  09:21 → its pre-state is `24f3f36b`.

## Decision

### D1 — Tenancy A: one database, two schemas, per-store sides (RULED L32 R2; item 0)

- One database `cobalt_brain` (dev twin `cobalt_dev`). Two schemas: **`system`**
  and **`"user"`**. The user-side schema keeps the name `user` (ruled 09-08:
  "user will have more roles and more user settings outside of being trader
  only") and is therefore **always quoted** — in every migration, grant,
  `search_path`, hand query and Python (`psycopg.sql.Identifier`). A suite lint
  test fails on any unquoted `user.` reference under `src/cobalt`. The word
  "trader" survives only inside table/field names (`trader_settings`, `traders`,
  `trader_id`, `trade_key`).
- Two `NOLOGIN` roles: **`cobalt_user`** (ALL on `"user"`, SELECT on `system`) and
  **`cobalt_system`** (ALL on `system`, **nothing** on `"user"` — system never reads
  user data). Each schema and every new-core table is **owned** by its side role
  (`ALTER … OWNER TO`): ownership is not a grant and would otherwise leak every
  privilege back to the login role. A third `NOLOGIN` role **`cobalt_backup`** is
  a member of `pg_read_all_data` for `pg_dump --role=cobalt_backup`.
- **The side is chosen per store, never per process.** Every store declares
  `SIDE = Side.USER | Side.SYSTEM` and opens its connections through the one
  factory, `cobalt.db.connect(dbname, side=…)`, which does
  `SET ROLE <side role>; SET search_path = <own schema only>` (no `public`). A job
  that touches both sides holds one connection per side; there is no "both" role.
  Cross-side references are written **schema-qualified** (`system.bars`), never
  resolved through `search_path`. A wrong-side statement fails loud twice over:
  relation-not-found (search_path) or permission denied (grants).
- **`user_id`.** `"user".traders(id, handle, created_at)`, seeded `id = 1,
  handle = 'primary'` (no name). Every user-side table carries
  `user_id INTEGER NOT NULL REFERENCES "user".traders(id)` with
  `DEFAULT current_setting('cobalt.trader_id')::int`. The factory sets the GUC
  from `configs/cobalt/tenant.yaml` (`trader_id: 1` — which local trader this
  install serves; committed; a product install ships it as 1). A connection that
  did not pass through the factory has no GUC and every INSERT fails loud; no
  literal default anywhere. Existing rows are backfilled to 1 in the same
  migration.
- **`public` is untouched** for the 17 old-tree tables (strangler rule). The
  placement test carries that list frozen: a NEW table landing in `public`, or any
  table not on exactly one side of the placement map, fails the suite.
- **Superuser login — weighed, split (Revision 2).** `NOINHERIT` on `cobalt` buys
  nothing while it is the superuser; after the factory's `SET ROLE` the session's
  current role is a non-superuser and the grants bite, so per-store enforcement is
  real. The only closure for "a connection that skips the factory" is a
  non-superuser app login. Target state, ruled here; implementation split:
  - this sprint: ownership to side roles, `cobalt_backup`, and a suite test that no
    `psycopg.connect` exists under `src/cobalt` outside `db.py`;
  - next ops prompt (owed): `cobalt_app` LOGIN NOINHERIT with its own credential in
    VaultManager/.env, member of `cobalt_user`, `cobalt_system`, `cobalt_backup`;
    factory and `pgdump.py` connect as it; superuser `cobalt` reserved for
    `db migrate --allow-prod` and docker; every production plist restarted in the
    same action (L28 restart-on-deploy). No credential change rides inside a
    data-model migration — two rollback domains would become three.

### D2 — Placement (RULED item 2; `cobalt_email_sends` revised under g)

| table | side | note |
|---|---|---|
| `aset_sizings` (cards), `card_transitions`, `card_stop_edits` | user | + `user_id`; S2 adds `account_mode`, `pool_member_id → system.radar_membership(id)` |
| `day_modes` | user | + `user_id` |
| `vault_writes`, `vault_overrides` | user | + `user_id` (note text is user data) |
| `trade_defs`, `tunables` (per-trade rows), `trader_settings`, `traders` — NEW | user | loaded copies of vault units / seeded settings |
| `setup_trade_matrix` | user | a VIEW `(trade_def, setup_ref, relation)` unnested from `trade_defs` |
| legs/fills, missed, DRC rows, prediction records | user | S2-P4 / S3 — declared now so the placement test names them |
| `bars` | system | 4.84M rows; `SET SCHEMA` is catalog-only |
| `radar_pool`, `radar_membership` (S2-P1) | system | |
| `cobalt_jobs`, `cobalt_kill_switch`, `cobalt_redactions`, `session_blocks` | system | |
| `cobalt_email_sends` | **system** | revised 09-08: channel log (`ts, ok, caller, message_id, detail`), no personal data — same class as `cobalt_redactions` |
| taxonomy anatomy instances (S2-P2) | system | |
| 17 old-tree tables | public | frozen allowlist, untouched |

Per launchd job, which side each of its stores connects as:

| job | stores → side |
|---|---|
| `com.cobalt.aset` | AsetStore, CardStore, DayModeStore, VaultWriteStore → user; SessionBlockStore → system |
| `prefill-daily` / `prefill-drc` | AsetStore, DayModeStore, VaultWriteStore → user; SessionBlockStore, JobStore → system |
| `cards-expire` · `daymode-propose` | CardStore / DayModeStore (+ VaultWriteStore) → user; JobStore → system |
| `archiver` | BarStore, JobStore → system only |
| `heartbeat` | JobStore, kill switch, SessionBlockStore, RedactionStore, EmailSendStore → system; VaultWriteStore (daily-note red/green block) → user |
| `cobalt notify email-test` | EmailSendStore, RedactionStore → system |
| `backup` | `pg_dump` as the login role (`--role=cobalt_backup` once D1's ops prompt lands), both schemas, no store |
| `agent` (old tree) | `public` only, untouched · `mainframe`, `obsidian`: no DB |

Tunables split: engine rows stay in `configs/cobalt/taxonomy/tunables.yaml`
(system); trader rows (every `per_trade(...)` row) become user data (D3.3);
trader-level settings become `"user".trader_settings` (D3.4).

### D3 — The vault note is the trade_def's truth (RULED item 3; a, b, d, e)

- **Source of truth** = the `cobalt:unit trade_def:<slug>` inside
  `<!-- cobalt:section definition -->` of `1 - Trading/4 - Strategies/<note>.md`,
  read through `cobalt.vault.resolve_vault_path()`. The DB row
  (`"user".trade_defs`: `slug` PK, `def` jsonb, `md5`, `note_path`, `loaded_at`,
  `user_id`) is a loaded, validated copy. One path: vault unit → loader →
  `"user".trade_defs`.
- **Key (a).** The frontmatter `trade_def:` slug — lowercase kebab, no `$`, no
  leading digit — **is the id**. `id:` is removed from the YAML unit; the loader
  injects `id = slug`; a unit that still carries `id:` fails loud ("id comes from
  frontmatter `trade_def:`"). Grammar-safe spelling for `cfg()` keys and
  `per_trade()` scope is ONE helper, `trade_key(slug) = slug.replace('-', '_')`.
  Consequence: `ema9_scalp.*` tunable rows re-key to `nine_ema_scalp.*`; every
  other key already equals `trade_key(slug)`. Schema: "v0.4 minus authored `id`
  and `name`, plus structured `quality_factors[]`" — recorded here, folded into the
  taxonomy at S2-P2's v0.8 bump.
- **Display name (e).** `TradeDef.name` = frontmatter `name:` (loader-injected
  like `id`); `name:` is removed from the unit; where the YAML's former name
  differed it joins `aliases[]` (Back$ide Scalp, Rubber Band Scalp, Big Dog
  Consolidation, Gap, Give and Go, Hitchhiker Scalp, Fashionably Late Scalp,
  Back-Through Open).
- **Loader.** Parses frontmatter with the existing `_FRONTMATTER_RE` pattern
  (no new dependency), finds the `definition` section and its units with
  `vaultwrite.markers`, loads the fenced YAML, injects id/name, validates
  `TradeDef`, fails loud on any populated unit that does not validate. A unit
  whose body is empty or holds only a partial mapping (see the matrix below) is a
  **draft**: skipped with a listed warning, never an error. Frontmatter `status:`
  is checked, not trusted: `defined` iff the unit validated, `draft` otherwise;
  `playbook` is never typed (earned at n ≥ 30, R3). Frontmatter `class:` /
  `family:` (d) are checked against the unit and any drift is listed; the human
  wins; `cobalt taxonomy sync-frontmatter` re-aligns with a diff.
  `python -m cobalt.taxonomy.validate` reads the vault.
- **The three former cross-checks (b).**
  1. `cameron_grid.yaml` → dies. The def's own `valid_setups[]` is the truth. The
     9 grid-only rows (drafts) move into their draft notes' Definition unit as a
     partial `trade_def: {valid_setups: [...]}`. The check becomes schema-level
     (refs ∈ `SetupRef`, unique pairs, non-empty). `"user".setup_trade_matrix` is
     a VIEW so S2's radar keeps the artifact by name.
  2. `variables/<id>.yaml` → folded INTO `quality_factors[]`: each item is a bare
     string (defaults: `source: human`, `tier: judgment`, `frontier: false`) or a
     mapping `{name, source, tier, frontier, why_template, status}`. The
     set-equality check vanishes by construction.
  3. `cfg()` → per-trade tunable rows move into the strategy note as a second
     Cobalt unit, `<!-- cobalt:unit tunables:<slug> -->`, inside the Definition
     section (separate from the def so replay's `status` writes never re-render
     the def and its comments). `resolve_cfg` = user rows ∪ engine rows; an
     unknown key fails loud; a user row shadowing an engine key fails loud.
     Loaded copy → `"user".tunables`.
  4. Trader-level settings — all of `aset.yaml` (sheet dollars per mode,
     `enabled_grades`) and all of `daymode.yaml` (reduced sheet/grades, enabled
     modes, `.htk` template, step-downs) — → `"user".trader_settings(user_id, key,
     value jsonb, source, updated_at)`. The Pydantic `TraderSettings` shape stays
     in code; both YAML files leave the repo; dev/prod are seeded from a
     gitignored `configs/dev/trader_settings.local.yaml` via `cobalt settings load
     --dry-run | --apply` (diff shown, market_reset-gated). **Proof before the
     YAMLs are deleted (Revision 3):** `TraderSettings.from_db() ==
     TraderSettings.from_yaml(...)` field-by-field (test + printed empty diff), and
     the ASET sheet renders identically on `cobalt_dev` + the dev vault (`GET /`
     and every JSON endpoint diffed before/after, empty modulo timestamps). The
     deletion is its own commit; its revert plus `settings load --apply --from`
     is that piece's rollback.
- **`category:` (d)** → replaced by `class:` and `family:` in the 22 notes' frontmatter
  and in `5 - Templates/Strategy.md`, filled from the def on the 13 (7 scalp /
  6 move2move), empty on the 9 drafts, via the frontmatter site. Deleting the
  Cobalt-seeded `category:` is allowed only because it was verified blank on all
  22; any non-blank value → refuse and report.
- **The repo ships one synthetic example def** in anatomy terms only — no SMB name,
  no cheat-sheet rule — so the product installs empty. The 13 YAMLs,
  `variables/`, `cameron_grid.yaml`, `aset.yaml` and `daymode.yaml` leave the repo
  only after the md5 proof (each vault unit's `trade_def` mapping, minus
  `id`/`name`, equals its YAML's) is in the report.

### D4 — Trade notes carry `trade_def:` (RULED item c)

`strategy:` free text → `trade_def:` slug on all 69 notes through
`VaultWriter.upsert_region` (the ADR-0004 frontmatter site): ONE inserted line
`trade_def: <slug>` after `strategy:`, every other byte preserved, `strategy:` left
verbatim (a human line). Match = trimmed, quotes stripped, casefolded. Blanks and
non-def values get an empty `trade_def:` so a later fill is a clause-2a cell. One
write_id per note, unified diff per note in the report, restore proven on the
dev-vault copy first.

**Corrected 2026-09-08 from the dry-run**: the pre-ADR tally had been taken over
all of `1 - Trading/` and so swept in the four legacy `strategy:` keys of the
STRATEGY notes themselves (Backside Scalp, Back Through Open, Second Chance Scalp,
Second Day Play) — which is why four rows read one high and `Backside Scalp`
appeared at all. The table below is the actual `1 - Trading/2 - Trades/` corpus:
69 notes, 36 with a non-blank `strategy:`, of which **31 match a slug**.

| `strategy:` value | n | `trade_def:` |
|---|---|---|
| Second Chance Scalp | 5 | second-chance |
| VWAP Continuation | 4 | vwap-continuation |
| Offside Scalp | 3 | off-sides |
| Hitchhiker Scalp | 3 | hitchhiker |
| Fashionable Late Scalp | 3 | fashionably-late |
| Opening Range Break | 2 | opening-range-break |
| 9 EMA Reclaim | 2 | nine-ema-reclaim |
| Second Day Play | 2 | second-day-play |
| Gap Give and Go · First VWAP Pullback · Bouncy Ball · Bella Fade · 9 EMA Scalp · Back Through Open | 1 each | gap-give-and-go · first-vwap-pullback · bouncy-ball · bella-fade · nine-ema-scalp · back-through-open |
| Big Dawg | 1 | big-dog |
| Puppy Dog Consolidation | 1 | blank — RULED: a separate def later (`puppy-dog` queued) |
| Bad Trade Outside of Playbook · Breaking News | 3 + 1 | blank, reported (not trade_defs) |
| (blank) | 33 | blank, reported |
| **totals** | **69** | **31 matched · 38 blank** |

`Backside Scalp` names no trade note: the value exists only as the Backside Scalp
STRATEGY note's own legacy `strategy:` key. Two values in the table were not yet
anywhere in the vault and were added as aliases first (`cobalt taxonomy add-alias`):
`Offside Scalp` on the `off-sides` draft and `Fashionable Late Scalp` on the
`fashionably-late` def.

`5 - Templates/Individual Trade Template.md` gains a `trade_def:` dropdown of the
22 slugs and loses the `strategy:` dropdown for NEW notes. Templates are human-tree
files: applied as hand-work with the diff in the report (09-06 R4 precedent).

### D5 — Names rule dispositions (RULED item 4, L31)

| identifier | where | disposition |
|---|---|---|
| `cameron_grid.yaml`, `load_cameron_grid`, `CAMERON_GRID_PATH`, `cameron_grid_path`, "Cameron H grid" docstrings | `taxonomy/loader.py`, `trade_def.py`, `tests/taxonomy` | → `setup_trade_matrix` (view + loader term); the file leaves the repo (user data, D3) |
| `bella_fade`, `spencer_scalp` ids; `bella_fade.*` tunable keys; `bella_fade` in tests and a `trade_def.py` docstring | `configs/cobalt/taxonomy/*`, tests | user data → leave with the YAMLs / move to note units; tests re-target the synthetic def; docstring reworded |
| `SMB` in `defaults.yaml` comment, `rubberband.yaml` reference_stats | configs | rubberband leaves; comment reworded ("sheet value 21") |
| `smbtraining.com` in `redact/secrets.py` docstring + `redact.yaml` pattern values | `src/cobalt/redact` | credential-host redaction VALUES, not identifiers; user data inside system config → ESCALATE (belongs with the trader, but F19 must not depend on the DB) |
| `dm_username: dejan_z`, `email.to` | `configs/cobalt/notify.yaml` | config VALUES; same DB-independence constraint (F18 out-of-band) → ESCALATE, not moved |
| finviz / mattermost / obsidian / gmail / google / oura / restic / tailscale in module and config names | adapters, collectors | EXEMPT: an adapter named after the API it adapts cites the artifact (source-substitution law). This is the L31 reading for integration targets. |
| `ya29.a0AfH6SMB…` test fixtures | tests | a token shape, not a name — no action |

### D6 — Local-tier adapter contract (RULED item 5; spec, implemented by the first new-core LLM consumer)

The 27B (`mainframe`) always thinks and inlines it; `reasoning_effort`,
`enable_thinking`, `/no_think` and a no-think system prompt are all ignored on this
server; the template-level disable (`{%- set enable_thinking = false %}` in
`chat_template.jinja`) takes effect only on the next model load (Prompt 5). The
adapter therefore:

1. strips `<think>…</think>` handling BOTH shapes — the endpoint's open+close pair
   and the Python SDK's shape (opening tag already stripped, closing kept);
2. asserts `max_tokens ≥ cfg(local.min_useful_tokens)` before the call (a tunables
   row, engine side);
3. counts post-strip tokens after the call and **raises `LocalTierEmptyOutput`
   on zero** — seats-followup STEP 6d: 3/3 runs at `max_tokens=1600` delivered
   1599 tokens of untagged scratch work and 0 useful tokens;
4. reports useful tok/s (post-strip) in the job's `last_result`, never raw tok/s
   alone.

### D7 — Hygiene rider (RULED item 6, F16)

`MattermostConfig.timeout_s` → tunables row `notify.mattermost.timeout_s` (10 s,
engine side), removed from `MattermostConfig` and `notify.yaml`; one consumer
(`notify/mattermost.py`), one test.

### D8 — Record (RULED item 8; item f)

The 09-06 strategy-note batch is pre-L28 hand-work; its `/tmp` backup is gone.
Rollback for that batch = restic snapshot **`24f3f36b`** (2026-09-06 08:30:23, tag
`cobalt-nightly`, vault + staging dump). The ledger's R4 line ("09-05 21:40") names
a snapshot that does not exist and is corrected in this ADR's appendix block.

## Migration and rollback — two domains (Revision 4)

- **Database** (`cobalt db migrate`; `--allow-prod` from `~/cobalt` only):
  `src/cobalt/db_migrations/0001_schemas.sql` (schemas, roles, grants, ownership,
  `traders`, tenant GUC) and `0002_move_tables.sql` (`ALTER TABLE public.<t> SET
  SCHEMA …` per new-core table — catalog-only, keeps data, indexes, FKs and
  sequences; then `user_id` columns + backfill). Proof per table: row count and
  `md5(string_agg(t::text, '|' ORDER BY <pk>))` before and after. Rollback:
  `cobalt db migrate --rollback` (reverse `SET SCHEMA public`, catalog-only) or
  the `pg_dump` taken first. Every store's `ensure_schema()` and the CLI assert the
  schemas exist before touching a table.
- **Vault** (91 note writes + 2 template hand-edits): `cobalt backup run`
  immediately before (fresh snapshot id printed = this domain's rollback); every
  write through `VaultWriter` with a write_id and a unified diff in the report;
  rollback = `cobalt vault restore --write-id` per note, or the snapshot.
- LIVE order: database first, heartbeat green at the next beat, then the vault
  domain. Each is reversible without touching the other. Window: outside
  20:00–21:30 and outside 09:00–12:00 ET; merge and migration are one action.

## Consequences

- One identity per trade (the slug), one home per fact (the note), one factory,
  one side per store. The repo installs empty: no trade name, no sheet dollar,
  no cheat-sheet rule is committed.
- Every new table must be declared on a side in the placement map or the suite
  fails; every cross-side reference is schema-qualified or the lint fails.
- S2-P1 line 0 is unblocked: pool/membership/bars are `system` writes; the
  account-mode tag is a `"user".aset_sizings` column; the first cross-side joins
  are named for S2-P2/P4: J1 `"user".aset_sizings.pool_member_id →
  system.radar_membership(id)`; J2 detector reads `system.bars` +
  `"user".trade_defs` in Python, SQL touches `system.bars` only; J3
  `"user".missed.pool_member_id → system.radar_membership(id)`, counterfactual R
  from `system.bars`; J4 F13 movers vs in-play, both system-side.
- Owed after this ADR: the `cobalt_app` non-superuser login (D1, ops prompt);
  `working_timeframe: 2m` frontmatter duplicate and `status:` derivation; the
  stats unit's free-text body (`n: insufficient data (n<30)`) wants a typed row;
  user values inside system config (`redact.yaml` hosts, `notify.yaml` recipient)
  under the F18/F19 DB-independence constraint; the `puppy-dog` strategy note; the
  old tree's pre-existing `tests/test_finviz_extractor.py` collection error.
