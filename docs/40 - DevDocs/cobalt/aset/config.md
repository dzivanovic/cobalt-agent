# `src/cobalt/aset/config.py`

## What it does
The ASET package's Pydantic config schemas and loaders — config-as-code
(TRIAGE cross-cutting law). A missing or invalid config **crashes**
(`ConfigError`) with the file path and validation detail; there is no
silent fallback to defaults for the file itself, though individual
fields may have documented defaults (e.g. `db_name`, `server`).

`configs/dev/aset.local.yaml` (gitignored) **replaces**
`configs/dev/aset.yaml` entirely when present — not merged — so it must
be a complete config. This is how real account numbers (and real
LAN-bind settings) stay off git while the shape of the config stays
documented in the committed example.

**Iteration 4 (2026-08-28, ruled by Dejan):** `AsetConfig` lost
`broker_hard_stop` and `daily_stop_default` — the percentage model they
served is retired. `account_size` is kept, but currently unused by the
fixed-dollar sheet-mode sizer; it's reserved for the future
1%-of-account computed mode. A second, sibling config —
`SheetModesConfig` / `load_sheet_modes_config()` — was added to load
`configs/cobalt/aset.yaml` (the actual per-grade dollar table), which
lives under `configs/cobalt/` rather than `configs/dev/` because it's
not per-developer settings, it's Dejan's actual trading rule (same
boundary class as the Bar Archiver's `watchlists.yaml`).

## Key functions/classes
- `DailyNoteConfig` — `daily_notes_dir` (relative to the vault root
  resolved by `cobalt.vault.resolve_vault_path()` — the vault ROOT
  itself is deliberately not configurable here, that's the one
  resolver's job), `filename_pattern` (default `%Y-%m-%d.md`). Consumed
  by `daily_note.py`.
- `ServerConfig` — `bind: "loopback" | "lan"` (default `"loopback"`),
  `port` (default `5010`, `1–65535`). `.host` property resolves
  `"loopback"` → `127.0.0.1`, `"lan"` → `0.0.0.0`. `"lan"` is documented
  in-line as exposing the sheet **unauthenticated** to the local network
  — acceptable for now, access token is a backlog item.
- `AsetConfig` — the top-level schema: `account_size` (`Decimal > 0`,
  reserved for the future computed mode, unused today), `db_name`
  (default `"cobalt_dev"`), `daily_note: DailyNoteConfig` (required),
  `server: ServerConfig` (optional, defaults to loopback so an old
  config without a `server:` section never silently exposes the LAN).
- `ConfigError(RuntimeError)` — the one error type this module raises.
- `load_config() -> AsetConfig` — resolves which file to read
  (`LOCAL_CONFIG_PATH` if it exists, else `CONFIG_PATH`), parses YAML,
  validates via Pydantic, raises `ConfigError` on any failure.
- `SheetModeGrades` — `A`, `B` (both `Decimal > 0`); one column (full or
  half) of the dollar table.
- `SheetModesConfig` — `full: SheetModeGrades`, `half: SheetModeGrades`.
  `.dollars_for(mode, grade) -> Decimal` — the one lookup helper; raises
  `ConfigError` for any grade other than A/B (i.e. a non-tradeable
  grade), so callers never get a silent `None`/zero. Accepts either
  enum members or raw strings (imports `Grade`/`SheetMode` from
  `models.py` locally, inside the method, to avoid a module-level
  reverse dependency).
- `load_sheet_modes_config() -> SheetModesConfig` — reads
  `SHEET_MODES_CONFIG_PATH` (`configs/cobalt/aset.yaml`, under the
  `sheet_modes:` key), same fail-loud pattern as `load_config()`. No
  local-override file for this one — it's shared new-core data, not a
  per-developer secret.
- `REPO_ROOT` — computed once (`Path(__file__).resolve().parents[3]`);
  reused by `daily_note.py`'s outside-the-repo safety check (not for
  vault resolution — that's `cobalt.vault`).

## Data flow in/out
**In:** `configs/dev/aset.yaml` (committed, example values) or
`configs/dev/aset.local.yaml` (gitignored, real values — wins if
present); `configs/cobalt/aset.yaml` (committed, shared) for
`load_sheet_modes_config()` — all read as plain YAML via
`yaml.safe_load`.
**Out:** a validated `AsetConfig` / `SheetModesConfig` instance, or a
raised `ConfigError`. Every other ASET module calls `load_config()` (and
`web.py` also `load_sheet_modes_config()`) fresh per request/action —
there is no cached singleton, so editing either YAML takes effect on the
next page load with no restart.

## Config it reads
Itself — this **is** the config loader for both files. Schema documented
above; example values live in `configs/dev/aset.yaml` and
`configs/cobalt/aset.yaml`.
