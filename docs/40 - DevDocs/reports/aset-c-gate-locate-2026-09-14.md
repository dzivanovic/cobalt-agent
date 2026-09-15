# ASET sizing gate — locate keys A/B allow, C block (2026-09-14)

Read-only recon. No writes, no git actions taken beyond this report file.

## §0 Headline

Allowed-keys set is a `"user".trader_settings` DB row (`aset.enabled_grades`),
not a vault note, not YAML, not hardcoded. Card-time C is a hard **refuse**
(`SizingError`, both server- and UI-side). Minimal change to allow C is a
`cobalt settings load --apply` write to that DB row — takes effect on the
**next card** (config is read fresh per-request, no cache, no restart, no
05:15 prefill involved). That write path is gated only by the market-reset
clock, **not** by a tokenized HITL approval. ESCALATE count: 1.

## 1. Where "keys A, B" comes from

- `src/cobalt/daymode/note.py:93` renders `keys {keys}` from
  `cfg.enabled_grades_for(mode)`.
- `src/cobalt/daymode/config.py:185-192` `enabled_grades_for()`: reduced
  mode narrows to `reduced_enabled_grades`; every other mode uses
  `account_enabled_grades` as-is.
- `src/cobalt/daymode/config.py:296-313` `load_daymode_config()` — docstring
  is explicit: *"one person's rulings, so rows in `"user".trader_settings`
  rather than a committed file... nothing in the runtime reads a file for
  them."* Calls `TraderSettings.from_db().daymode`.
- `src/cobalt/settings/models.py:83-102` `TraderSettings.from_db()` builds
  `account_enabled_grades` from DB key `"aset.enabled_grades"`
  (`SHEET_KEYS` at models.py:29) via `TraderSettingsStore`.

## 2. (a), (b), (c), or (d)?

**(a) — a `"user".trader_settings` DB row.** Confirmed by commit `bd25d47`
("feat(settings)!: aset.yaml and daymode.yaml leave the repo", ADR-0008
D3.4, 2026-09-08): `configs/cobalt/aset.yaml` and `daymode.yaml` were
deleted from the repo entirely; neither file exists in `configs/cobalt/`
today (only `configs/dev/aset.yaml` remains, and that file carries no
`enabled_grades` key — sheet-dollar table only, per its own header comment
pointing at the now-removed `configs/cobalt/aset.yaml`). The DB is the only
source the runtime reads: `load_sheet_modes_config()`
(`src/cobalt/aset/config.py:251`) and `load_daymode_config()`
(`daymode/config.py:296`) both call `TraderSettings.from_db()`, no file
fallback.

Last known value before the file left the repo (`bd25d47^:configs/cobalt/aset.yaml:55`):
`enabled_grades: [A, B]`, with the file's own comment at lines 15-18:
*"A+ activates only once the grading system exists to justify it; **C
returns when the coach program reopens the testing-and-learning tier**."*
— i.e. C's exclusion reads as a deliberate, dated policy choice, not an
oversight. I did not query the live DB row (would require
`COBALT_ENV=production`, a prod touch out of scope for this read-only
recon — see BACKLOG item below if Dejan wants it confirmed live).

The write path that seeds/changes this row is `cobalt settings load
--from <dir>|--from-git <rev> --dry-run|--apply`
(`src/cobalt/settings/cli.py:67-118`) — "the ONE write path for the
trader's own settings."

## 3. What happens at card time when C is chosen today

**Refuse — hard error, not a warning.**

- UI: `src/cobalt/aset/web.py:303-305` — grades outside
  `SheetModesConfig.enabled_grades` render as disabled `<option>`s,
  labeled `"no trade (SAW)"` for C/D, unselectable via the dropdown.
- Server: `src/cobalt/aset/engine.py:50-59` `compute_sizing()` — first
  check is `if inp.grade not in enabled_grades: raise SizingError(...)`,
  explicitly to catch "a stale hidden-field POST" bypassing the disabled
  option (per `web.py:16-22` module docstring). Called from both
  `web.py:919-922` and `web.py:1006-1009` (compute + fill-update paths),
  passing `sheet_modes_cfg.enabled_grades` — the same DB-sourced value
  from §1/§2.

No partial/soft path exists; C never reaches the sizing math.

## 4. Minimal change to allow C

**Mechanism:** write DB key `"aset.enabled_grades"` to include `C`
(`[A, B, C]`) via `cobalt settings load --from <dir> --apply`, pointed at a
directory holding a current `aset.yaml` + `daymode.yaml` pair (these files
no longer live in the repo — a fresh local pair would need to be
constructed off the last known shape at `bd25d47^`, or `daymode.yaml`'s
`reduced_enabled_grades` also touched if C should be permitted on reduced
days too). No source change needed — `Grade.C` already exists in the enum
(`src/cobalt/aset/models.py:33`) and the engine/UI both read the gate from
config, not a hardcoded list.

**Category:** neither a vault-note edit nor a `src/` code change — it's a
DB-row write through the dedicated settings CLI (config-as-code, not
git-tracked). The only gate on that write is `assert_writable("settings.load",
...)` (`src/cobalt/settings/cli.py:111`, `session/guard.py:123-150`) — the
market-reset clock block (20:00-21:00 ET), same as any other write. It is
**not** behind a tokenized HITL approval token.

**When it takes effect:** immediately, on the next card. `load_sheet_modes_config()`
and `load_daymode_config()` carry no cache/`lru_cache` (checked both
`aset/config.py` and `daymode/config.py`) and are called fresh inside each
request handler (`web.py:325`, `495`, `919`, `1006`, `1098`). Not gated to
the 05:15 prefill (a separate subsystem, `prefill/daily.py`) and no
resident restart required.

## ESCALATE

Enabling grade C changes what the sizing engine will compute and persist
for real account risk — by CLAUDE.md's own boundary this reads as a
trading-logic change ("Trading-logic changes... go behind the tokenized
HITL approval pattern"), but the only enforced gate on the
`trader_settings` write path is the market-reset time window, not a HITL
token. Is `cobalt settings load --apply` meant to require a HITL token
before writing `aset.enabled_grades` (or any `SHEET_KEYS`/`DAYMODE_KEYS`
row), or is trader-authored settings.load intentionally exempt because
it's Dejan's own CLI action on his own rulings rather than an
agent-proposed change?
