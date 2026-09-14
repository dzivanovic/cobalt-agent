# `src/cobalt/dayopen/runner.py`

`run(report_date=None, now=None)` — the one place the six checks run in
this fixed order (C1..C6), fed `dayopen.config.load_dayopen_config()`'s
ruled numbers, and assembled into a `DayOpenReport` via
`models.overall_verdict`. `report_date` defaults to today's ET date;
`now` defaults to `cobalt.session.clock.now_utc()`. CLI, tests and any
future scheduler all call this — never the individual `checks.py`
functions directly (L3: one definition of "a day-open run").
