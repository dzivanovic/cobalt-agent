"""The nightly replay — `com.cobalt.replay`, 21:10 ET weekdays (S2-P4).

    cli.py     `cobalt replay nightly [--date] [--dry-run]`, inside `as_job`
    runner.py  the ordered run: archiver precondition, deadline, per-side phases
    movers.py  F13: unfiltered top movers, their i1 archive, the benchmark diff
    cards.py   F12: unfilled cards over i1 bars, counterfactual R, the gates
    line.py    the one DRC miss line (`drc-misses/miss_line`)
    models.py  every structured value the above passes around
"""
