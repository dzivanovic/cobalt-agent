# `src/cobalt/aset/config.py`

## What it does
The ASET package's Pydantic config schema and loader — config-as-code
(TRIAGE cross-cutting law). A missing or invalid config **crashes**
(`ConfigError`) with the file path and validation detail; there is no
silent fallback to defaults for the file itself, though individual
fields may have documented defaults (e.g. `db_name`, `server`).

`configs/dev/aset.local.yaml` (gitignored) **replaces**
`configs/dev/aset.yaml` entirely when present — not merged — so it must
be a complete config. This is how real account numbers (and now real
LAN-bind settings) stay off git while the shape of the config stays
documented in the committed example.

## Key functions/classes
- `DailyNoteConfig` — `vault_path`, `inbox_dir`, `filename_pattern`
  (default `%Y-%m-%d.md`). Consumed by `daily_note.py`.
- `ServerConfig` — `bind: "loopback" | "lan"` (default `"loopback"`),
  `port` (default `5010`, `1–65535`). `.host` property resolves
  `"loopback"` → `127.0.0.1`, `"lan"` → `0.0.0.0`. `"lan"` is documented
  in-line as exposing the sheet **unauthenticated** to the local network
  — acceptable for now, access token is a backlog item.
- `AsetConfig` — the top-level schema: `account_size`, `broker_hard_stop`
  (both `Decimal`, `> 0`), `daily_stop_default` (optional, `> 0` —
  morning-set value; TEMP fallback when absent is account ÷ 100, see
  `engine.temp_prefill_daily_stop`), `db_name` (default `"cobalt_dev"`),
  `daily_note: DailyNoteConfig` (required), `server: ServerConfig`
  (optional, defaults to loopback so an old config without a `server:`
  section never silently exposes the LAN).
- `ConfigError(RuntimeError)` — the one error type this module raises.
- `load_config() -> AsetConfig` — resolves which file to read
  (`LOCAL_CONFIG_PATH` if it exists, else `CONFIG_PATH`), parses YAML,
  validates via Pydantic, raises `ConfigError` on any failure.
- `REPO_ROOT` — computed once (`Path(__file__).resolve().parents[3]`);
  reused by `daily_note.py` to resolve relative vault paths.

## Data flow in/out
**In:** `configs/dev/aset.yaml` (committed, example values) or
`configs/dev/aset.local.yaml` (gitignored, real values — wins if
present) — read as plain YAML via `yaml.safe_load`.
**Out:** a validated `AsetConfig` instance, or a raised `ConfigError`.
Every other ASET module (`web.py`, `store.py`, `daily_note.py`) calls
`load_config()` fresh per request/action — there is no cached singleton,
so editing the YAML takes effect on the next page load with no restart.

## Config it reads
Itself — this **is** the config loader. Schema documented above; example
values live in `configs/dev/aset.yaml`.
