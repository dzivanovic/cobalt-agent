"""The cache reader's grouping, proved before any cache experiment reads
through it: every retained FILE of every day lands in exactly one scan or
is one of the replay's mover exports; the scan count per day is printed.
"""

from __future__ import annotations

from h1_cache import group_scans, mover_exports
from h1_support import retained_days


def test_every_retained_file_lands_in_exactly_one_scan():
    for day_dir in retained_days():
        files = [p for p in day_dir.iterdir() if p.is_file()]
        folders = [p for p in day_dir.iterdir() if p.is_dir()]
        movers = mover_exports(day_dir)
        scans = group_scans(day_dir)
        placed = [path for scan in scans for path in scan.files.values()]
        assert len(placed) == len(set(placed))
        assert set(placed) | set(movers) == set(files) and not (set(placed) & set(movers))
        print(
            f"GROUPING day {day_dir.name}: files {len(files)} · in scans {len(placed)} · "
            f"mover exports {len(movers)} · folders skipped {len(folders)} · scans {len(scans)}"
        )
