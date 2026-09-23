"""Setups fix round 4 (prompt `72-setups-fix-r4.md`): the FIX rows of the
round-2 house check (prompt `70`'s report), as classified by the round-4
drafter's report (prompt `71`, L75). Offline; constructed literals of this
file's own only (L32 / L69).
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from test_setups_fix_r3 import _per_trade_accepted

REPO = Path(__file__).resolve().parents[2]
CUT_TEST = REPO / "tests" / "cobalt" / "test_setups_fixture_cut.py"
CUTTER = REPO / "tests" / "fixtures" / "radar" / "_cut_setups_fixtures.py"

# =====================================================================
# F1 — the dials probe asserts WHY a note row was refused
# =====================================================================


def _rubberband_probe(tmp_path):
    shape = shapes.SHAPES["rubberband"]
    return tmp_path, shape.note_slug, shape.mapping(), shape.rows()


def test_f1_a_malformed_probe_note_fails_the_probe_loudly(tmp_path):
    """RED on 8da261a: any refusal printed "not reachable". A tunables row
    that does not parse is a broken probe, not an engine-key refusal."""
    from cobalt.taxonomy.vault_loader import VaultTaxonomyError

    root, slug, mapping, rows = _rubberband_probe(tmp_path)
    malformed = [*rows, {"key": "example_probe.malformed", "value": 1}]  # no unit, scope, …
    unit = sup.engine_tunables()["stop.buffer"].unit.value
    with pytest.raises(VaultTaxonomyError, match="invalid tunables rows"):
        _per_trade_accepted(root, slug, mapping, malformed, "stop.buffer", unit)


def test_f1_the_engine_key_refusal_still_reads_not_reachable(tmp_path):
    """GREEN guard: r3's `## DIALS` row `rubberband | stop.buffer |
    assumed / engine only (global)` stays a refusal (False), not a raise."""
    root, slug, mapping, rows = _rubberband_probe(tmp_path)
    unit = sup.engine_tunables()["stop.buffer"].unit.value
    assert _per_trade_accepted(root, slug, mapping, rows, "stop.buffer", unit) is False


# =====================================================================
# F3 — no real-day literal in the cut's committed test or its cutter
# =====================================================================

#: The only days the cut may name: the synthetic days (L45 — dates stripped).
SYNTHETIC_DAYS = frozenset({"2026-01-06", "2026-01-07", "2026-01-08"})


@pytest.mark.parametrize("path", [CUT_TEST, CUTTER], ids=lambda p: p.name)
def test_f3_every_iso_date_in_the_cut_is_a_synthetic_day(path):
    """RED on 8da261a (the cut test's docstring). The message counts the
    outsiders and never prints them — the real day is never written (L32)."""
    found = set(re.findall(r"\d{4}-\d{2}-\d{2}", path.read_text()))
    outside = len(found - SYNTHETIC_DAYS)
    assert outside == 0, f"{path.name}: {outside} ISO date literal(s) outside the synthetic allowlist"
