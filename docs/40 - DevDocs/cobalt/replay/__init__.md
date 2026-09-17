# `src/cobalt/replay/__init__.py`

The package for `com.cobalt.replay`, the nightly one-shot at 21:05 ET on
weekdays (S2-P4 ruling R3). The file holds only the package docstring, which
maps the modules:

| Module | Owns |
|---|---|
| `cli.py` | `cobalt replay nightly [--date] [--dry-run]`, wrapped by `as_job` |
| `runner.py` | the ordered run: archiver precondition, deadline, per-side phases |
| `movers.py` | F13: unfiltered top movers, their i1 archive, the benchmark diff |
| `cards.py` | F12: unfilled cards over i1 bars, counterfactual R, the gates, the versioned `"user".missed` store |
| `line.py` | the one DRC miss line, unit `drc-misses/miss_line` |
| `models.py` | every structured value the modules above pass around |

It exports nothing and has no side effects on import.
