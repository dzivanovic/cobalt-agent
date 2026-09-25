"""X10 (v2 §7, before S1; runs FIRST — it can change the design): on a
fixture receipt, `rebuild_members(...).as_of` equals the receipt's own
`as_of`, never the wall clock. If it were wall-clock, staleness could not be
replayed from the receipt (L57) and the design changes before any bump."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

from cobalt.radar.evaluate import rebuild_members

from stale_support import SCAN, SCAN0


def test_x10_rebuilt_as_of_is_the_receipts_as_of():
    from test_radar_evaluate import World

    world = World()
    world.scan(SCAN0)
    world.scan(SCAN0 + timedelta(seconds=SCAN))
    receipts = list(world.cards.receipts)
    written = [datetime.fromisoformat(m["as_of"]) for m in receipts[-1]["observations"]["members"]]
    before = datetime.now(timezone.utc)
    rebuilt = [m.as_of for m in rebuild_members(receipts)]
    after = datetime.now(timezone.utc)
    equal = rebuilt == written
    wall = any(before <= t <= after for t in rebuilt)
    print(f"X10: receipts={len(receipts)} members={len(rebuilt)} receipt_as_of={[t.isoformat() for t in written]} "
          f"rebuilt_as_of={[t.isoformat() for t in rebuilt]} equal={equal} wall_clock={wall}")
    assert equal and not wall
