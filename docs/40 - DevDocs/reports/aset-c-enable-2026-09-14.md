# ASET grade C enable — dry-run + apply command (2026-09-14)

Read-only recon + one dry-run. No `--apply` run. Writes so far: two YAML
files under `~/tmp/aset-c/` (not committed, not in the repo) and this
report. Dejan runs the apply himself. ESCALATE count: 0.

## §0 Headline

Current DB row is `aset.enabled_grades = ["A", "B"]` (unchanged since
`bd25d47^`, 2026-09-08). `cobalt settings load` requires BOTH full YAML
files (no partial/single-key file) and only ever UPSERTs the 7
`SETTING_KEYS` rows that differ — it never deletes rows and never touches
keys outside that set. Dry-run against a seed built from the live DB
values (only `aset.enabled_grades` changed to add `C`) shows exactly one
key changing, nothing else. Apply command is ready; verify query included.

## 1. Current row

```
key                  value        updated_at
aset.enabled_grades  ['A', 'B']   2026-09-08 21:49:54.937068+00:00
```

Query run: `COBALT_ENV=production uv run cobalt db query --side user --prod
"SELECT key, value, updated_at FROM \"user\".trader_settings WHERE key =
'aset.enabled_grades'"` — ran as given, no schema adaptation needed.

## 2. `cobalt settings load` — scope and behavior

- `--help`: `--from FROM_DIR` (directory holding both YAMLs) or
  `--from-git COMMIT` (reads both at a revision), plus exactly one of
  `--dry-run` / `--apply` (no default — `cli.py:42-48` refuses if both or
  neither are given).
- **File layout**: `--from <dir>` requires BOTH `aset.yaml` and
  `daymode.yaml` in that directory (`models.py:144-150`, hard error if
  either is missing). Each file needs its own full top-level key
  (`sheet_modes:` / `daymode:`), and `TraderSettings.from_yaml()` validates
  all 7 `SETTING_KEYS` are present and Pydantic-valid before `cmd_load`
  will even print a diff for `--apply` — **no partial/single-key file is
  possible**. To touch only `aset.enabled_grades`, every other field must
  be reproduced verbatim from the current DB so its diff line reads `=`
  (unchanged).
- **UPSERT, not replace** (`store.py:60-104`, confirmed by reading, not
  inferring): `TraderSettingsStore.put()` loops the 7 `rows` the YAML
  pair produced, skips any key whose value already matches the DB
  (`outcome[key] = "unchanged"`, no SQL executed for it), and for the
  rest does `INSERT ... ON CONFLICT (user_id, key) DO UPDATE`. It never
  deletes a row and never touches a key outside `SETTING_KEYS` (e.g. the
  `radar.*` and `aset.account_mode` rows are untouched by any
  `settings load` run). One transaction — commit or full rollback.
- **Without `--apply`** (`--dry-run`): prints `cobalt settings load — DRY
  RUN from <source>`, then one line per `SETTING_KEYS` entry — `=` for
  unchanged, `~`/`+` with `db:`/`file:` values for anything that would
  change — then either `no differences...` or `DRY RUN — N setting(s)
  would change. Nothing written.` Confirmed live below.

## 3. Seed files

`~/tmp/aset-c/aset.yaml` and `~/tmp/aset-c/daymode.yaml` — both files, full
shape required by §2. Every field copied byte-for-byte from
`cobalt settings show`'s live values (all sourced `git:bd25d47^`, matching
the pre-removal `configs/cobalt/{aset,daymode}.yaml` from the locate
report). The only changed value in either file:
`aset.yaml: sheet_modes.enabled_grades: [A, B] → [A, B, C]`.
`daymode.reduced_enabled_grades` stays `[A, B]` — Dejan's 09-14 ruling
was about the account-wide gate, not the reduced rung's size restriction.

## 4. Dry-run output

```
$ COBALT_ENV=production uv run cobalt settings load --from ~/tmp/aset-c --dry-run
cobalt settings load — DRY RUN from yaml:/Users/cobalt/tmp/aset-c

  = aset.sheet_modes
  ~ aset.enabled_grades
      db  : ["A", "B"]
      file: ["A", "B", "C"]
  = daymode.reduced_sheet
  = daymode.reduced_enabled_grades
  = daymode.enabled_modes
  = daymode.hotkey_file_template
  = daymode.stepdowns

DRY RUN — 1 setting(s) would change. Nothing written.
```

## 5. Stop condition check

Only `aset.enabled_grades` changes; all 6 other `SETTING_KEYS` show `=`
(unchanged); no row deletion is possible via this write path (§2). Stop
condition NOT triggered — proceeding to give Dejan the apply command.

## 6. Apply command (Dejan runs this, from Local Terminal)

```
COBALT_ENV=production uv run cobalt settings load --from ~/tmp/aset-c --apply
```

Verify after:

```
COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT key, value, updated_at FROM \"user\".trader_settings WHERE key = 'aset.enabled_grades'"
```

Expect `value = ['A', 'B', 'C']` with a fresh `updated_at`. `cmd_load`
itself also self-checks the round trip (`from_db() == from_yaml()`) and
will raise `FAILED` on the spot if it doesn't match, so a clean `applied:
{...}` + `from_db() == from_yaml() — field-by-field diff EMPTY.` print is
sufficient; the verify query is a second, independent confirmation.

## ESCALATE

None. Locate report's open HITL-scope question (whether `settings load
--apply` should require a token) stands unresolved but is a policy
question for Dejan, not a blocker for this recon — repeating it here
only if he wants it re-flagged.
