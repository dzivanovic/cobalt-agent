# DevDocs — Cobalt new core

One short wiki page per `.py` file under `src/cobalt/` (+ its tests),
generated at sprint close per CLAUDE.md's non-negotiable. Structure
mirrors the source tree exactly: `docs/40 - DevDocs/cobalt/...` for
`src/cobalt/...`, `docs/40 - DevDocs/tests/cobalt/...` for `tests/cobalt/...`.

This first generation covers **pre-beta slice 1 — the ASET semi-auto
sizing sheet** (2026-08-23 → 2026-08-26).

---

## File inventory — everything created/modified for the ASET sheet

### Source (`src/cobalt/`)

| File | Purpose |
|---|---|
| `__init__.py` | New-core package marker; states the ground rules (fail-loud, deterministic, config-driven, dev-only). |
| `db.py` | The ONE Postgres connection factory; refuses `cobalt_brain` (prod) unless explicitly overridden. |
| `aset/__init__.py` | ASET package marker; states grade/stops are always Dejan's input. |
| `aset/models.py` | Pydantic `Grade`/`Direction` enums, `GRADE_RISK_PCT` map, `SizingInput`/`SizingResult`. |
| `aset/engine.py` | Deterministic sizing math — pure functions, no I/O: broker cap, daily-stop law (+ its temp override), `compute_sizing`. |
| `aset/config.py` | Pydantic config schema + loader (`account_size`, `broker_hard_stop`, `daily_note`, `server` bind). |
| `aset/store.py` | Persists every sizing to `aset_sizings` in `cobalt_dev`. |
| `aset/prefill.py` | Fetches last price from Finviz Elite; fail-loud, scrubs the auth token from every error. |
| `aset/daily_note.py` | Append-only "Save to Daily Note" writer, gated by a real `git check-ignore` safety check. |
| `aset/net.py` | LAN-IP detection helper for the startup banner. |
| `aset/web.py` | The FastAPI single-page sheet — routes, rendering, wiring everything together. |
| `aset/__main__.py` | Launcher (`uv run python -m cobalt.aset`) — resolves bind config, prints reachable URLs, starts uvicorn. |

### Configs / templates

| File | Purpose |
|---|---|
| `src/cobalt/aset/migrations/0001_aset_sizings.sql` | The one DDL source for `aset_sizings` (one-path rule — `store.py` executes this file, no second copy). |
| `configs/dev/aset.yaml` | Committed example config — placeholder account size, real structure. |
| `configs/dev/aset.local.yaml` | **Gitignored** — Dejan's real account size + LAN bind setting; replaces the example entirely when present. |

### Tests (`tests/cobalt/`)

| File | Purpose |
|---|---|
| `conftest.py` | Neutralizes the repo-root Postgres mock so this directory's tests can hit real `cobalt_dev`. |
| `test_aset_engine.py` | Sizing math unit tests, incl. the reference sizer's worked example. |
| `test_aset_config.py` | Config loader fail-loud tests + `ServerConfig` (loopback/LAN) tests. |
| `test_aset_store.py` | Integration test against real `cobalt_dev`; proves the prod-DB refusal. |
| `test_aset_prefill.py` | Token-scrubbing tests. |
| `test_aset_daily_note.py` | Safety-gate + append-only tests against real git. |
| `test_aset_net.py` | LAN-IP helper tests (faked socket, no real network). |

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
7. **`aset/daily_note.md`** + `tests/cobalt/test_aset_daily_note.md` —
   the vault writer and its safety gate; read the gate test closely,
   it's testing against real git, not a mock.
8. **`aset/net.md`** + `tests/cobalt/test_aset_net.md` — small, quick,
   self-contained.
9. **`aset/web.md`** — where all of the above gets wired into the
   actual page and its three routes. Read this after everything it
   depends on, not before — it won't make sense in isolation.
10. **`aset/__main__.md`** — how it's actually launched.
11. **`tests/cobalt/conftest.md`** — last, as an aside explaining why
    the DB isn't mocked in this directory.
