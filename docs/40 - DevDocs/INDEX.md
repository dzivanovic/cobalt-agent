# DevDocs — Cobalt new core

One short wiki page per `.py` file under `src/cobalt/` (+ its tests),
generated at sprint close per CLAUDE.md's non-negotiable. Structure
mirrors the source tree exactly: `docs/40 - DevDocs/cobalt/...` for
`src/cobalt/...`, `docs/40 - DevDocs/tests/cobalt/...` for `tests/cobalt/...`.

This first generation covers **pre-beta slice 1 — the ASET semi-auto
sizing sheet** (2026-08-23 → 2026-08-28), including the 2026-08-26
vault-path migration (the real Obsidian vault, `cobalt.vault`'s ONE
resolver), the 2026-08-28 iteration-4 sizing-model replacement
(fixed-dollar sheet mode, auto-append, actual-fill recompute), and the
same-day config-completion follow-up (full A+/A/B/C/D grade ladder in
`configs/cobalt/aset.yaml`, `enabled_grades` as the separate UI/compute
gate), plus the **Bar Archiver** (2026-08-28) — a second, sibling
new-core component under `src/cobalt/archiver/`, unrelated to ASET
except for sharing `cobalt.db`. Extended 2026-09-02 to cover
**Taxonomy** (`src/cobalt/taxonomy/`) — the `trade_def` +
variable-registry Pydantic schema and its config-as-code loader,
covering Batch 1 (ADR-0001), Batch 2 / v0.7 schema extensions
(ADR-0002), and the v0.7 fold's schema v0.4 migration — one-stop trail
slot, tunable registry, class definitions (ADR-0003); a third sibling
component, unrelated to ASET/Archiver except for the shared
config-boundary convention (`configs/cobalt/taxonomy/`).

---

## File inventory — everything created/modified for the ASET sheet

### Source (`src/cobalt/`)

| File | Purpose |
|---|---|
| `__init__.py` | New-core package marker; states the ground rules (fail-loud, deterministic, config-driven, dev-only). |
| `db.py` | The ONE Postgres connection factory; refuses `cobalt_brain` (prod) unless explicitly overridden. |
| `vault.py` | The ONE vault-path resolver (TRIAGE 2.6); `configs/dev/vault.yaml`, overridable by `COBALT_VAULT_PATH`, fail-loud. New-core only — old tree's ambiguity untouched. |
| `aset/__init__.py` | ASET package marker; states grade/stops are always Dejan's input. |
| `aset/models.py` | Pydantic `Grade`/`Direction`/`SheetMode` enums, `SizingInput`/`SizingResult`/`FillRecompute`. |
| `aset/engine.py` | Deterministic sizing math — pure functions, no I/O: fixed-dollar `compute_sizing` (sheet mode, `enabled_grades` passed in), `compute_fill_recompute` (actual-fill audit). |
| `aset/config.py` | Pydantic config schemas + loaders: `AsetConfig` (`account_size`, `daily_note`, `server` bind) and `SheetModesConfig` (full A+/A/B/C/D ladder × half, plus `enabled_grades`). |
| `aset/store.py` | Persists every sizing to `aset_sizings` in `cobalt_dev`; `ensure_schema()` runs every `migrations/*.sql` file in order. |
| `aset/prefill.py` | Fetches last price from Finviz Elite; fail-loud, scrubs the auth token from every error. |
| `aset/daily_note.py` | Append-only daily-note writer, into the real vault (`cobalt.vault`), gated by an outside-the-repo safety check. `/size` auto-appends a card; `/fill` appends a linked FILL UPDATE block. |
| `aset/net.py` | LAN-IP detection helper for the startup banner. |
| `aset/web.py` | The FastAPI single-page sheet — routes, rendering, ticker/entry state model, FULL/HALF + LONG/SHORT toggles, wiring everything together. |
| `aset/__main__.py` | Launcher (`uv run python -m cobalt.aset`) — resolves bind config, prints reachable URLs, starts uvicorn. |
| `archiver/__init__.py` | Bar Archiver package marker; states the never-daily/weekly/monthly rule and the standalone-scheduling rule. |
| `archiver/models.py` | `Interval` enum (i1/i2/i5/i15/i30 only — the footgun-law validated enum) + `Bar`. |
| `archiver/config.py` | Watchlist tier config loader (`configs/cobalt/watchlists.yaml`) + `archive_targets()`/`backfill_targets()`. |
| `archiver/collector.py` | Finviz `/export/stock` fetch + fail-loud shape validation (columns, and the daily-fallback-shape detector). |
| `archiver/store.py` | Idempotent bar upserts into `bars` in `cobalt_dev` (PK `(ticker, interval, ts)`, `ON CONFLICT DO UPDATE`). |
| `archiver/report.py` | Appends one run-summary row to `docs/30 - Design/archiver-runs.md`; strictly tabular by design. |
| `archiver/runner.py` | Orchestrates a run (gentle rate, fail-loud per ticker); the `archiver` CLI entry point (`--backfill TICKER`). |
| `taxonomy/__init__.py` | Taxonomy package marker. |
| `taxonomy/trade_def.py` | The `trade_def` Pydantic schema (v0.7 §10.1, schema v0.4 — `SCHEMA_VERSION`) — enums as the vocabulary source of truth, `Predicate`/`Tunable`/`StopPlacement`/`Trigger`/`TrailCondition`/`TrailSpec` building blocks, no predicate parser. One-stop trail slot (`TradeDef.trail`); `trail_ma_close`/`trail_bar`/standalone `ma_close` REMOVED (ADR-0003). |
| `taxonomy/variables.py` | The variable-registry stub schema — one file per trade_def, one entry per `quality_factors[]` item; `frontier` flag for tape-class reads (Batch 2). |
| `taxonomy/defaults.py` | `TaxonomyDefaults` schema for `configs/cobalt/taxonomy/defaults.yaml` (`working_timeframe`, `ma.fast`/`ma.slow` — Batch 2; the two NON-dynamic globals `cfg()` falls back to). |
| `taxonomy/tunables.py` | `TunableRow`/`TunableRegistry` schema for `configs/cobalt/taxonomy/tunables.yaml` (v0.7 §13.1) — every `config, dynamic` quantity as a status/replay-tracked row; `replay_backlog()` query (ADR-0003). |
| `taxonomy/loader.py` | Config-as-code loader: parses + cross-validates every trade_def, its variable registry, defaults, tunables, and the Cameron H grid; fail-loud (`TaxonomyConfigError`) — incl. `resolve_cfg`/`iter_cfg_tokens` for `cfg(key)` resolution — except the A.6 stop-buffer check, which warns. |
| `taxonomy/validate.py` | `python -m cobalt.taxonomy.validate` CLI — loads everything, prints a summary table + tunables/backlog counts, exits non-zero on failure. |

### Configs / templates

| File | Purpose |
|---|---|
| `src/cobalt/aset/migrations/0001_aset_sizings.sql` | The initial DDL for `aset_sizings` (one-path rule — `store.py` executes migration files, no second copy of the schema). |
| `src/cobalt/aset/migrations/0002_aset_sizings_sheet_mode.sql` | Adds `sheet_mode`, drops the retired `daily_stop`/`risk_pct` columns (iteration 4). |
| `configs/dev/aset.yaml` | Committed example config — placeholder account size, real structure. |
| `configs/dev/aset.local.yaml` | **Gitignored** — Dejan's real account size + LAN bind setting; replaces the example entirely when present. |
| `configs/cobalt/aset.yaml` | Committed — the sheet-mode fixed-dollar risk table (full/half × A/B), mirrors Dejan's DAS hotkey files exactly (iteration 4). |
| `configs/dev/vault.yaml` | Committed — the real vault root (not a secret, just a path); `cobalt.vault`'s one config source. |
| `src/cobalt/archiver/migrations/0001_bars.sql` | The one DDL source for `bars`. |
| `configs/cobalt/watchlists.yaml` | Committed — the three watchlist tiers (derived from Dejan's TradingView exports) + intervals per tier. |
| `ops/com.cobalt.archiver.plist` | Standalone launchd template, Mon-Fri 20:30 local — captured here, not auto-installed. |
| `configs/cobalt/taxonomy/defaults.yaml` | Committed — `working_timeframe: 2m`, `ma: {fast: 9, slow: 20}` (Batch 2). |
| `configs/cobalt/taxonomy/tunables.yaml` | Committed — 30 dynamic-tunable rows seeded from v0.7 §13.1's `dyn: yes` rows (ADR-0003). |
| `configs/cobalt/taxonomy/cameron_grid.yaml` | Committed — all 21 Cameron H grid rows (`valid_setups[]`); 13 have a populated `trade_def`. |
| `configs/cobalt/taxonomy/trade_defs/*.yaml` | Committed — 13 populated trade_defs (6 Batch 1 + 7 Batch 2), one file per id; schema v0.4 (trail slot, `cfg()` tokens — ADR-0003). |
| `configs/cobalt/taxonomy/variables/*.yaml` | Committed — the matching variable registry per trade_def; `trail_fit` entry on the 6 trail-carrying trades (ADR-0003). |

### Tests (`tests/cobalt/`)

| File | Purpose |
|---|---|
| `conftest.py` | Neutralizes the repo-root Postgres mock so this directory's tests can hit real `cobalt_dev`. |
| `test_aset_engine.py` | Sizing math unit tests, incl. the reference sizer's worked example. |
| `test_aset_config.py` | Config loader fail-loud tests + `ServerConfig` (loopback/LAN) tests. |
| `test_aset_store.py` | Integration test against real `cobalt_dev`; proves the prod-DB refusal. |
| `test_aset_prefill.py` | Token-scrubbing tests. |
| `test_aset_daily_note.py` | Safety-gate (outside-repo), stub-banner, and append-only tests, via a fake vault. |
| `test_aset_net.py` | LAN-IP helper tests (faked socket, no real network). |
| `test_aset_vault.py` | Vault resolver fail-loud + env-override-precedence tests. |
| `test_archiver_config.py` | Watchlist config fail-loud tests + tier-derivation sanity checks (no cross-tier ticker, VIX excluded). |
| `test_archiver_collector.py` | Datetime-quirk parsing + CSV shape validation, incl. the daily-fallback-shape rejection. |
| `test_archiver_store.py` | Integration test: real upsert idempotency (`DO UPDATE` verified, not just "no duplicate"). |
| `test_archiver_report.py` | Run-report header/append behavior + the table-stays-contiguous regression guard. |

---

## Suggested reading order (first-time inspection)

Ordered by dependency, not by file path — data model first, math next,
config and infra after, integrations last, the app that wires it all
together at the end:

1. **`aset/models.md`** — the vocabulary (Grade, Direction, SheetMode,
   the three Pydantic models). Read this first; everything else is
   built on it.
2. **`aset/engine.md`** + `tests/cobalt/test_aset_engine.md` — the actual
   sizing math (fixed-dollar sheet mode) and the actual-fill recompute.
   This is the heart of the feature.
3. **`aset/config.md`** + `configs/dev/aset.yaml` +
   `configs/cobalt/aset.yaml` + `tests/cobalt/test_aset_config.md` —
   what's configurable (including the sheet-mode dollar table), how
   it's validated, and what "fail-loud" looks like in practice.
4. **`cobalt/db.md`** — the connection factory and its prod-refusal
   guarantee (read this before `store.py` — it's the thing `store.py`
   depends on).
5. **`aset/store.md`** + `aset/migrations/0001_aset_sizings.sql` +
   `aset/migrations/0002_aset_sizings_sheet_mode.sql` +
   `tests/cobalt/test_aset_store.md` — persistence, the multi-file
   migration runner, and the real bug it caught (comment-splitting —
   see `store.md`).
6. **`aset/prefill.md`** + `tests/cobalt/test_aset_prefill.md` — the
   Finviz fetch and why the auth-token scrubbing exists.
7. **`cobalt/vault.md`** + `tests/cobalt/test_aset_vault.md` — the ONE
   vault-path resolver (read this before `daily_note.md`, not after —
   it's what `daily_note.py` depends on now).
8. **`aset/daily_note.md`** + `tests/cobalt/test_aset_daily_note.md` —
   the vault writer: its outside-the-repo safety gate, stub-with-banner
   behavior, and (iteration 4) the auto-append + linked FILL UPDATE
   blocks.
9. **`aset/net.md`** + `tests/cobalt/test_aset_net.md` — small, quick,
   self-contained.
10. **`aset/web.md`** — where all of the above gets wired into the
    actual page and its routes (`/`, `/api/prefill`, `/size`, `/fill`).
    Read this after everything it depends on, not before — it won't
    make sense in isolation.
11. **`aset/__main__.md`** — how it's actually launched.
12. **`tests/cobalt/conftest.md`** — last, as an aside explaining why
    the DB isn't mocked in this directory.

## Bar Archiver reading order

A sibling component to ASET, not built on it — shares only `cobalt.db`.

1. **`archiver/models.md`** — `Interval` and `Bar`; the vocabulary.
2. **`archiver/config.md`** + `configs/cobalt/watchlists.yaml` +
   `tests/cobalt/test_archiver_config.md` — the three tiers, and how
   `archive_targets()`/`backfill_targets()` turn them into work.
3. **`archiver/collector.md`** + `tests/cobalt/test_archiver_collector.md`
   — the fetch + fail-loud shape validation. Read the datetime-quirk
   handling closely; it's the part most likely to bite a future change.
4. **`archiver/store.md`** + `src/cobalt/archiver/migrations/0001_bars.sql`
   + `tests/cobalt/test_archiver_store.md` — idempotent persistence.
5. **`archiver/report.md`** + `tests/cobalt/test_archiver_report.md` —
   the run-report writer; read why it's kept strictly tabular.
6. **`archiver/runner.md`** — where 2–5 get wired into an actual run,
   plus the `archiver` CLI. Read last, same reason as `aset/web.md`.

## Taxonomy reading order

A sibling component to ASET/Archiver, config-as-code only — no engine
code, no predicate parser, no bar logic (ADR-0001, ADR-0002, ADR-0003).

1. **`taxonomy/trade_def.md`** — the vocabulary: enums, `Predicate`,
   `Tunable`, `StopPlacement`, `Trigger`, `TrailCondition`, `TrailSpec`
   (the one-stop trail slot), and the `TradeDef` model itself. Read
   this first.
2. **`taxonomy/variables.md`** — the per-trade variable-registry stub
   schema, incl. the `frontier` tape-class flag (Batch 2) and
   `trail_fit` (ADR-0003).
3. **`taxonomy/defaults.md`** — the two taxonomy-wide knobs
   (`working_timeframe`, `ma.fast`/`ma.slow`) that `loader.md`'s
   `resolve_ma_ref`/`resolve_cfg` resolve against — the NON-dynamic
   `cfg()` fallback.
4. **`taxonomy/tunables.md`** — the dynamic-tunable registry
   (`tunables.yaml`, v0.7 §13.1) that `resolve_cfg` checks FIRST; the
   `replay_backlog()` query that replaced the old hand-maintained
   BACKLOG.md list.
5. **`taxonomy/loader.md`** + `configs/cobalt/taxonomy/cameron_grid.yaml`
   + `configs/cobalt/taxonomy/defaults.yaml` +
   `configs/cobalt/taxonomy/tunables.yaml` +
   `configs/cobalt/taxonomy/trade_defs/*.yaml` +
   `configs/cobalt/taxonomy/variables/*.yaml` +
   `tests/taxonomy/test_trade_defs.py` — where 1–4 get loaded,
   cross-validated, and fail loud (or, for the A.6 stop-buffer check,
   warn). Read this after everything it depends on, not before.
6. **`taxonomy/validate.md`** — the CLI entry point
   (`python -m cobalt.taxonomy.validate`). Read last, same reason as
   `aset/web.md`/`archiver/runner.md`.
7. **ADR-0001** (Batch 1, schema v0.3), **ADR-0002** (Batch 2, v0.3 →
   v0.7 extensions), and **ADR-0003** (v0.7 fold: schema v0.4, one-stop
   trail slot, tunable registry, class definitions — supersedes
   ADR-0002 for trail) — the decision record behind all of the above;
   read alongside `TAXONOMY-DRAFT-v0_7.md` §10/§13.1/§14 and
   `TRADE-DEFS-BATCH1-v0_1.md` / `TRADE-DEFS-BATCH2-v0_1.md` for the
   source sheets.
