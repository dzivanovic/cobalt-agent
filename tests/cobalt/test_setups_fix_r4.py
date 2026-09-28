"""Setups fix round 4 (prompt `72-setups-fix-r4.md`): the FIX rows of the
round-2 house check (prompt `70`'s report), as classified by the round-4
drafter's report (prompt `71`, L75). Offline; constructed literals of this
file's own only (L32 / L69).
"""

from __future__ import annotations

import importlib.util
import re
from datetime import date
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


# =====================================================================
# F4 — the cutter re-dates on the New York wall clock
# =====================================================================

#: Constructed days of this file's own (never a stored day): two EDT days
#: and one EST day.
EDT_DAY, EDT_LATER, EST_DAY = date(2025, 6, 10), date(2025, 7, 15), date(2025, 12, 10)


def _shift():
    spec = importlib.util.spec_from_file_location("_cut_setups_fixtures_r4", CUTTER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module._shift_datetime_str


def _delta(real, synthetic):
    return (synthetic - real).days


@pytest.mark.parametrize("value, expected", [
    ("2025-06-10 13:30:00+00:00", "2025-12-10 14:30:00+00:00"),
    ("2025-06-10T08:01:57.469346+00:00", "2025-12-10T09:01:57.469346+00:00"),
])
def test_f4_an_edt_time_re_dated_onto_an_est_day_keeps_its_new_york_clock(value, expected):
    """RED on 8da261a: the UTC clock was kept, so 09:30 ET read 08:30 ET."""
    assert _shift()(value, _delta(EDT_DAY, EST_DAY)) == expected


def test_f4_between_two_edt_days_the_utc_clock_is_unchanged():
    """GREEN guard: the same offset on both days is today's behaviour."""
    assert _shift()("2025-06-10 13:30:00+00:00", _delta(EDT_DAY, EDT_LATER)) == "2025-07-15 13:30:00+00:00"


def test_f4_a_time_moves_by_its_new_york_local_date():
    """00:00Z on the 11th is 20:00 ET on the 10th: it moves as the 10th."""
    assert _shift()("2025-06-11 00:00:00+00:00", _delta(EDT_DAY, EST_DAY)) == "2025-12-11 01:00:00+00:00"


def test_f4_a_bare_date_moves_by_the_delta():
    assert _shift()("2025-06-10", _delta(EDT_DAY, EST_DAY)) == "2025-12-10"


@pytest.mark.parametrize("value", ["2025-06-10 13:30:00", "2025-06-10 09:30:00-04:00"])
def test_f4_a_time_not_in_utc_fails_the_cutter_loudly(value):
    """L1: a time without `+00:00` is never guessed."""
    with pytest.raises(SystemExit, match="00:00"):
        _shift()(value, _delta(EDT_DAY, EST_DAY))
