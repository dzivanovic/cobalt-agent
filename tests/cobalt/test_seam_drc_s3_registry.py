"""The DRC D3 × S3 exits seam (2026-09-30): the registry's union tail.

Offline. Prints both tuples in order (`-s`) and pins the seam's rule S-1
(`reports/deploy-reissue-2026-09-30.md` `## THE SEAM`): `FORWARD` ends
0015 … 0021, `REVERSE` begins 0021 … 0015, and the placement map carries
both lanes' tables.
"""

from cobalt.db import Side
from cobalt.db_migrations import FORWARD, REVERSE
from cobalt.db_migrations.placement import CREATED_TABLES, CREATED_VIEWS, DECLARED_TABLES


def test_the_union_tail_is_0015_to_0021_and_reverse_mirrors_it():
    forward = [p.name for p in FORWARD]
    reverse = [p.name for p in REVERSE]
    print("FORWARD:", *forward, sep="\n  ")
    print("REVERSE:", *reverse, sep="\n  ")
    assert [name[:4] for name in forward[-7:]] == ["0015", "0016", "0017", "0018", "0019", "0020", "0021"]
    assert [name[:4] for name in reverse[:7]] == ["0021", "0020", "0019", "0018", "0017", "0016", "0015"]
    assert all(p.exists() for p in (*FORWARD, *REVERSE))


def test_placement_carries_both_lanes_and_declares_neither_built_table():
    names = list(CREATED_TABLES)
    drc = ["drc_imports", "drc_fills", "drc_rows", "drc_stated_books", "drc_events"]
    assert all(CREATED_TABLES[name] is Side.USER for name in (*drc, "legs"))
    assert names[-1] == "legs" and max(names.index(name) for name in drc) < names.index("legs")
    assert CREATED_VIEWS["legs_current_v"] is Side.USER
    assert "legs" not in DECLARED_TABLES and "drc_rows" not in DECLARED_TABLES
