# DevDocs — Cobalt new core

One short wiki page per `.py` file under `src/cobalt/` (+ its tests),
generated at sprint close per CLAUDE.md's non-negotiable. Structure
mirrors the source tree exactly: `docs/40 - DevDocs/cobalt/...` for
`src/cobalt/...`, `docs/40 - DevDocs/tests/cobalt/...` for `tests/cobalt/...`.

This first generation covers **pre-beta slice 1 — the ASET semi-auto
sizing sheet** (2026-08-23 → 2026-08-26), including the 2026-08-26
vault-path migration (the real Obsidian vault, `cobalt.vault`'s ONE
resolver), plus the **Bar Archiver** (2026-08-28) — a second, sibling
new-core component under `src/cobalt/archiver/`, unrelated to ASET
except for sharing `cobalt.db`.

---

## File inventory — everything created/modified for the ASET sheet

### Source (`src/cobalt/`)

| File | Purpose |
|---|---|
| `__init__.py` | New-core package marker; states the ground rules (fail-loud, deterministic, config-driven, dev-only). |
| `db.py` | The ONE Postgres connection factory; refuses `cobalt_brain` (prod) unless explicitly overridden. |
| `vault.py` | The ONE vault-path resolver (TRIAGE 2.6); `configs/dev/vault.yaml`, overridable by `COBALT_VAULT_PATH`, fail-loud. New-core only — old tree's ambiguity untouched. |
| `aset/__init__.py` | ASET package marker; states grade/stops are always Dejan's input. |
| `aset/models.py` | Pydantic `Grade`/`Direction` enums, `GRADE_RISK_PCT` map, `SizingInput`/`SizingResult`. |
| `aset/engine.py` | Deterministic sizing math — pure functions, no I/O: broker cap, daily-stop law (+ its temp override), `compute_sizing`. |
| `aset/config.py` | Pydantic config schema + loader (`account_size`, `broker_hard_stop`, `daily_note`, `server` bind). |
| `aset/store.py` | Persists every sizing to `aset_sizings` in `cobalt_dev`. |
| `aset/prefill.py` | Fetches last price from Finviz Elite; fail-loud, scrubs the auth token from every error. |
| `aset/daily_note.py` | Append-only "Save to Daily Note" writer, into the real vault (`cobalt.vault`), gated by an outside-the-repo safety check. |
| `aset/net.py` | LAN-IP detection helper for the startup banner. |
| `aset/web.py` | The FastAPI single-page sheet — routes, rendering, wiring everything together. |
| `aset/__main__.py` | Launcher (`uv run python -m cobalt.aset`) — resolves bind config, prints reachable URLs, starts uvicorn. |
| `archiver/__init__.py` | Bar Archiver package marker; states the never-daily/weekly/monthly rule and the standalone-scheduling rule. |
| `archiver/models.py` | `Interval` enum (i1/i2/i5/i15/i30 only — the footgun-law validated enum) + `Bar`. |
| `archiver/config.py` | Watchlist tier config loader (`configs/cobalt/watchlists.yaml`) + `archive_targets()`/`backfill_targets()`. |
| `archiver/collector.py` | Finviz `/export/stock` fetch + fail-loud shape validation (columns, and the daily-fallback-shape detector). |
| `archiver/store.py` | Idempotent bar upserts into `bars` in `cobalt_dev` (PK `(ticker, interval, ts)`, `ON CONFLICT DO UPDATE`). |
| `archiver/report.py` | Appends one run-summary row to `docs/30 - Design/archiver-runs.md`; strictly tabular by design. |
| `archiver/runner.py` | Orchestrates a run (gentle rate, fail-loud per ticker); the `archiver` CLI entry point (`--backfill TICKER`). |

### Configs / templates

| File | Purpose |
|---|---|
| `src/cobalt/aset/migrations/0001_aset_sizings.sql` | The one DDL source for `aset_sizings` (one-path rule — `store.py` executes this file, no second copy). |
| `configs/dev/aset.yaml` | Committed example config — placeholder account size, real structure. |
| `configs/dev/aset.local.yaml` | **Gitignored** — Dejan's real account size + LAN bind setting; replaces the example entirely when present. |
| `configs/dev/vault.yaml` | Committed — the real vault root (not a secret, just a path); `cobalt.vault`'s one config source. |
| `src/cobalt/archiver/migrations/0001_bars.sql` | The one DDL source for `bars`. |
| `configs/cobalt/watchlists.yaml` | Committed — the three watchlist tiers (derived from Dejan's TradingView exports) + intervals per tier. |
| `ops/com.cobalt.archiver.plist` | Standalone launchd template, Mon-Fri 20:30 local — captured here, not auto-installed. |

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

1. **`aset/models.md`** — the vocabulary (Grade, Direction, the two
   Pydantic models). Read this first; everything else is built on it.
2. **`aset/engine.md`** + `tests/cobalt/test_aset_engine.md` — the actual
   sizing math, and the reference worked example proving it's right.
   This is the heart of the feature.
3. **`aset/config.md`** + `configs/dev/aset.yaml` +
   `tests/cobalt/test_aset_config.md` — what's configurable, how it's
   validated, and what "fail-loud" looks like in practice.
4. **`cobalt/db.md`** — the connection factory and its prod-refusal
   guarantee (read this before `store.py` — it's the thing `store.py`
   depends on).
5. **`aset/store.md`** + `aset/migrations/0001_aset_sizings.sql` +
   `tests/cobalt/test_aset_store.md` — persistence and its one real
   integration test.
6. **`aset/prefill.md`** + `tests/cobalt/test_aset_prefill.md` — the
   Finviz fetch and why the auth-token scrubbing exists.
7. **`cobalt/vault.md`** + `tests/cobalt/test_aset_vault.md` — the ONE
   vault-path resolver (read this before `daily_note.md`, not after —
   it's what `daily_note.py` depends on now).
8. **`aset/daily_note.md`** + `tests/cobalt/test_aset_daily_note.md` —
   the vault writer, its outside-the-repo safety gate, and the stub-
   with-banner behavior.
9. **`aset/net.md`** + `tests/cobalt/test_aset_net.md` — small, quick,
   self-contained.
10. **`aset/web.md`** — where all of the above gets wired into the
    actual page and its three routes. Read this after everything it
    depends on, not before — it won't make sense in isolation.
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
