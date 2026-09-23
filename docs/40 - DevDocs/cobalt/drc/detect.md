# `src/cobalt/drc/detect.py`

## What it does
This is the ONE header classifier for DRC imports (R114, L3). Every
import path and every test asks `detect_kind(name, data)` what a file
is. It reads only the first line.

It never reads the name or the extension. His two daily files arrive as
`.md` (Obsidian hides `.csv`), and he names them differently every day.
`name` only labels the verdict.

## The header
- The first line is decoded as UTF-8. A BOM is stripped, and a CR before
  the LF is dropped.
- The line is split as ONE CSV record.
- A single trailing empty cell is ignored for classification. E1's
  trading-log header ends with the delimiter.
- A NUL byte or an undecodable first line means `ignored — not text`.
  That covers images and binaries.

## The required sets
- `REQUIRED[Kind.TRADING_LOG]` is `trading_log.REQUIRED`, and
  `REQUIRED[Kind.STATS_LOG]` is `stats_log.REQUIRED`. Both are imported
  from their owners and never copied.
- `SHARED` is computed from the two sets (E1: `Symbol`, `Side`). A shared
  name decides nothing.

## Outcomes
| header carries | verdict |
|---|---|
| every name of one kind | that kind, `parsed` |
| … plus names outside the set | that kind, `parsed`, `degraded: <kind>_shape` naming the extras (L9) |
| every name of both kinds | `failed — header matches both kinds` |
| some names of one kind (by the UNIQUE names) and no kind complete | that kind, `partial`, `missing` in the kind's column order, flag `PARTIAL — missing: <columns>` (R17 (5): the file IS parsed on what it has) |
| unique names of both kinds | `failed — header matches both kinds` |
| only shared names, or no required name | `ignored — header matches neither kind` |
| a required name twice | `failed — duplicate column(s)` |

A reorder alone is not a failure.

**Known consequence on E1 (ASK DESK in the build report).** The real
stats log carries one vendor-named column. L31 keeps that name out of
the required set, so by the literal rule it is an extra. Every real
stats log therefore reads `parsed` with `stats_log_shape` raised.

## Sets
`detect_set(files)` classifies a folder listing or a multi-file drop as
one set:
- exactly one file per kind, complete or `partial` → `pass`
- two files of one kind → `FAILED: <kind> ambiguous — <name 1>, <name 2>`,
  both named and neither picked
- a kind with no file → `incomplete`

The `partial`, `ignored` and `failed` files are always listed.

## The `_imports/drc/` tree
- `import_folder_date(name)` returns a date only for a `YYYY-MM-DD`
  folder name.
- `import_folders(root)` lists only those folders.

`_reference/` and anything else beside the date folders is never an
input. D1 builds no folder READER. The reader is D2's (09-23 R17 (2)),
and it applies this rule.
