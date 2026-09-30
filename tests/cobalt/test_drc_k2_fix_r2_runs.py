"""DRC K2 fix r2 — RUNS (L70; the fix prompt
`prompts/2026-09-25/12-drc-k2-fix-r2-build.md` F4).

RUN-2 — the UNPROVEN row of `03` ESCALATE 8 = the fix r1 build report's
ESCALATE 8 (`drc-k2-fix-r1-build-2026-09-25.md:205`): `_repair` RAISES
`PairingError` when stored `stats_row` rows exist but the `day` row names
no stats import (`store.py:520-522`); "No test reaches it". The state is
constructed through the ONE writer (`record_day`), never a direct insert:
a day paired WITH a stats input, recorded with its import ids OMITTING the
stats import. A RUN's red is a result, recorded, never fixed here.

Runs inside `test_drc_store.py`'s never-committed migration transaction
on `cobalt_dev` (L76). Constructed symbols and dates only (L32 / L45).
"""

from __future__ import annotations

import pytest

from cobalt.drc.models import Kind, PairingError
from cobalt.drc.pairing import build_day
from cobalt.drc.stats_log import StatsLogSource
from cobalt.drc.detect import detect_kind
from cobalt.drc.store import DrcStore

from test_drc_k1_store import _day1_carrying_ddd, _row
from test_drc_k2_experiments import _import, _one_row_stats, _snapshot
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D_NEXT,
    SEED,
    migrated,
    requires_db,
    weekday_calendar,
)


@requires_db
def test_run_2_stats_rows_stored_with_no_stats_import_named_refuse_the_re_pair(migrated, weekday_calendar):
    """RUN-2 (`drc-k2-fix-r1-build-2026-09-25.md:205`, ESCALATE 8; `03`
    ESCALATE 8): the shape of `test_drc_k2_experiments.py`'s
    `_record_with_stats`, but `record_day` is called with the trading
    import id only. (1) the writer stores it; (2) the day's `stats_row`
    rows exist and its `day` row's `import_ids` names no `stats_log`;
    (3) `rebuild` of that day raises `PairingError` naming it, and the
    day's `drc_rows` are byte-identical after the refusal."""
    _day1_carrying_ddd()
    parsed, ids = _import(SEED.read_bytes(), D_NEXT)
    stats_bytes = _one_row_stats("FFF", "short", D_NEXT, "10:05:00 EST")
    stats = StatsLogSource().parse(stats_bytes, detect_kind("s.md", stats_bytes))
    DrcStore().record_import(D_NEXT, stats.result, stats_bytes)
    book = DrcStore().seed_for(D_NEXT)
    pairing = build_day(parsed, stats, seed=book.positions, resolves=book.resolves)

    # (1) the state is storable through the one writer.
    DrcStore().record_day(pairing, {Kind.TRADING_LOG: ids[Kind.TRADING_LOG]}, book)

    # (2) stats rows stored, no stats import named on the day row.
    assert migrated.execute(
        """SELECT count(*) FROM "user".drc_rows WHERE day = %s AND kind = 'stats_row'""", (D_NEXT,)
    ).fetchone()[0] >= 1
    day_inputs, _ = _row(migrated, D_NEXT, "day")
    assert sorted(day_inputs["import_ids"]) == [Kind.TRADING_LOG.value]

    # (3) the re-pair refuses, with exactly this message; nothing written.
    before = _snapshot(migrated, D_NEXT)
    with pytest.raises(PairingError) as e:
        DrcStore().rebuild(D_NEXT)
    assert str(e.value) == "2001-01-03: stats rows are stored with no stats import named — nothing assumed"
    assert _snapshot(migrated, D_NEXT) == before
