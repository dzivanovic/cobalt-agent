"""X12 (v3; the proposal's §7 dry-run + Fable X7 + grok (i)), its offline
half: the `h = 1` pass over EVERY retained day, scan by scan — his pool
block with the handicap ABSENT vs the same block carrying this build's
constructed handicap at factor 1 — through
`handicap_dry_run.identity_mismatches`, the dry-run's own function. "Any
mismatch voids every dry-run figure" (Fable).

One test per retained day (a day's two replays take minutes); the days,
scans and mismatches are summed from the per-day lines in the report.
The stored-membership half is the deploy's read-only step: `cobalt_dev`
holds no production day.
"""

from __future__ import annotations

import pytest
from h1_support import config, constructed_block, his_sources, retained_days

from cobalt.radar.handicap_dry_run import identity_mismatches
from cobalt.radar.models import HandicapBlock


@pytest.mark.parametrize("day_dir", retained_days(), ids=lambda path: path.name)
def test_x12_h1_identity_on_a_retained_day(day_dir):
    cfg = config()
    parsed = his_sources(cfg)
    unit = HandicapBlock(**constructed_block(factor="1"))
    scans, mismatches = identity_mismatches(day_dir, parsed, cfg, unit)
    print(f"X12 day {day_dir.name}: scans {scans} · mismatches {len(mismatches)}")
    for line in mismatches[:20]:
        print(f"X12 mismatch: {line}")
    assert mismatches == []
