# `src/cobalt/settings/cli.py`

## What it does
`cobalt settings load --from <dir> | --from-git <commit>
--dry-run|--apply` and `cobalt settings show`.

## Key behaviour
- Exactly one of `--from` / `--from-git`, and exactly one of
  `--dry-run` / `--apply`. No defaults: one of them changes what every
  card is sized on.
- Prints a per-setting diff (db value vs file value) before doing
  anything.
- `--apply` is market_reset gated (`assert_writable`) — re-typing a sheet
  dollar is a trading-logic change. `--dry-run` is not: seeing what WOULD
  change during the window is exactly when you want to.
- After applying it RE-READS the rows and asserts
  `from_db() == the seed` before claiming success.

## `--card <file> [--sha256 <hash>]` (S2-P2, Astra R1-5)
Loads the five radar-card keys (`settings/card.py`) from ONE reviewed
file instead of the two YAMLs. It does not combine with `--from` or
`--from-git`. `--apply` requires `--sha256` of the file's bytes; a
`--sha256` without `--card` is refused. The body is
`card.cmd_load_card`: diff, one `put` with deletes, and a round-trip
proof.

## `--from-git`, and why it exists
`configs/cobalt/aset.yaml` and `daymode.yaml` left the repo in the same
sprint. A LIVE seed therefore reads them at a revision:
`cobalt settings load --from-git <deletion commit>^ --apply`. Same
recovery pattern the taxonomy migration uses for its own deleted inputs.

## Gotchas
`cobalt settings show` prints every row with its `source` and date, then
the RESOLVED objects — a row that parses but does not resolve is worth
seeing as both.

---

## 2026-09-17 — S2-P4: `cobalt settings load --optional <file> --sha256 <hash>` (Astra R1-14)

The real load path for optional keys (today only `radar.benchmark`):

    optional_settings:
      radar.benchmark: {top_n: 20, min_move_pct: 10}

- `load_optional_file(path, sha256=, require_hash=)` hashes the file's
  BYTES before parsing. A mismatch refuses, and `--apply` without
  `--sha256` refuses and names the file's hash. It accepts exactly one root
  `optional_settings` and refuses unknown keys and any required
  `SETTING_KEYS` key by name. Each value is validated by its model.
- `cmd_load_optional` prints a per-key diff; `--dry-run` writes nothing. On
  `--apply` it checks `assert_writable` first (refused inside market_reset),
  then does one `put` of the changed keys (source `optional:<filename>`).
  It proves the round trip by re-reading and re-validating before it claims
  success. Keys the file omits are left untouched.
- `--optional` does not combine with `--from`/`--from-git`. `--sha256`
  without `--optional` refuses.
- Merge note: S2-P2's branch adds a parallel `--card <file> --sha256` path
  in `settings/card.py`. When both land, the two optional-file loaders
  should be unified (one-path rule).

---

## 2026-09-25 — DRC D4: `apply_settings`, the one apply; `show` prints the DRC keys

- `apply_settings(rows, *, source, actor="settings.load", store=None,
  delete=())` is now THE write of `"user".trader_settings` for both
  `cobalt settings load --apply` (the `--from` / `--from-git` path and the
  `--optional` path) and the ASET change line (`aset/web.py`,
  `POST /settings/daily/apply`). In order: `assert_writable` (refused
  inside `market_reset`, raising `SessionBlocked` before anything is
  written); ONE `store.put` (one transaction); a re-read, and a
  `TraderSettingsError` if any written key reads back different (a caller
  may say "saved" only after this returns); one loguru line
  `settings applied: keys … · deleted … · source … · at …` — keys, deleted
  keys, the source KIND (the label up to `@sha256:`) and the time; NEVER a
  value and never a digest of one (2026-09-25, D4 fix r1 F-8: a digest of a
  daily-stop-only payload can be enumerated back to the value, L32). The
  reviewed hash stays in each written row's `source`.
- `payload_sha256(rows)` — sha256 of the payload's canonical JSON
  (`sort_keys`, compact). The change line shows it for review and its
  Apply must carry it back.
- `cmd_load` / `cmd_load_optional` call `apply_settings` and keep their own
  typed round-trip checks after it. `settings/card.py`'s `cmd_load_card`
  calls it too since D4 fix r1 F-1 (2026-09-25; before that it called
  `store.put` itself), keeping its `CardSettings` round trip on top. The
  one other writer of `trader_settings` rows is the radar's vault-note
  mirror (`radar/notes.py` `mirror_sources`, `radar.note.*`) — a machine
  mirror with its own market-reset refusal, not a settings load.
- `cmd_show` (D4-5, the DRC family's dry-run) ends with a
  `DRC keys (optional; absent = not given):` block: every key in
  `DRC_SETTING_KEYS`, its stored JSON, or `not given`.
- `--optional` now also accepts the DRC keys (they are in
  `OPTIONAL_SETTING_KEYS`), e.g. `account.daily_stop_full: <n>`.
