# `src/cobalt/seatusage/__init__.py`

## What it does
Package marker for the seat-usage report. No exports — every consumer
imports the module it wants (`config`, `ccusage`, `report`, `runner`,
`cli`), so nothing depends on an import-time side effect.

## The shape of the package
| Module | Job |
|---|---|
| `config.py` | `configs/cobalt/seat_usage.yaml` → typed. The tool pin, the role hints, the free-model list. |
| `ccusage.py` | Runs the pinned external tool, read-only and offline, and types what comes back. |
| `report.py` | Renders one day's marked unit, and the human cells that sit beside it. |
| `runner.py` | One run: collect, write in place, seed the cells once. |
| `cli.py` | `cobalt seat-usage run / show / gate`. |

The split is the standing law, not a preference: **tools fetch, agents
reason.** `ccusage.py` fetches and validates, `report.py` formats, and
no model appears anywhere in the path.
