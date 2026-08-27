# `src/cobalt/archiver/__init__.py`

## What it does
Package marker for the Bar Archiver. States the one hard rule: this
package never archives daily/weekly/monthly (Finviz serves 10y+ of
those on demand) and never touches the old tree's scheduler.

## Key functions/classes
None.

## Data flow in/out
None.

## Config it reads
None directly — see `config.py` for the package's actual config schema.
