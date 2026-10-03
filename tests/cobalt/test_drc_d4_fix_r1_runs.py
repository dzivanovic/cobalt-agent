"""DRC D4 fix round 1 — the RUNS (L70): each UNPROVEN claim of the D4
check (drc-d4-check-2026-09-25.md:179, ESCALATE 5) becomes a cheap run
whose output the fix report quotes. A RUN's red is a RESULT, never fixed
in this round (L75).

Every value is constructed here (L32 / L45 / L69); the harness is
`test_drc_settings.py`'s, imported (the `world` / `page` fixtures and the
constructed `FakeStore`).
"""

from __future__ import annotations

import os

import pytest
from test_drc_settings import FakeStore, _form, page, world  # noqa: F401 - fixtures by import

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

RUN1_SOURCE = "test:d4-fix-r1-run1"


# ---------------------------------------------------------------------
# RUN-1 — the with-DB store joins the suite's rollback (dev_db_tx).
# pytest runs a file's tests in definition order: run1_a, then run1_b.
# ---------------------------------------------------------------------


@requires_db
def test_run1_a_a_store_write_lands_inside_its_test():
    """RUN-1 (drc-d4-check-2026-09-25.md:179): a `TraderSettingsStore()`
    write is read back inside the test that made it."""
    from cobalt.settings.store import TraderSettingsStore

    store = TraderSettingsStore()
    store.put({"account.daily_stop_full": "24680"}, source=RUN1_SOURCE)
    rows = [r for r in store.rows() if r["source"] == RUN1_SOURCE]
    assert [r["key"] for r in rows] == ["account.daily_stop_full"]


@requires_db
def test_run1_b_nothing_of_the_previous_test_survives():
    """RUN-1 (drc-d4-check-2026-09-25.md:179): the row the previous test
    wrote is gone — `dev_db_tx` rolled it back (an invariant, not a
    stored value, L69)."""
    from cobalt.settings.store import TraderSettingsStore

    assert [r for r in TraderSettingsStore().rows() if r["source"] == RUN1_SOURCE] == []


# ---------------------------------------------------------------------
# RUN-2 — a refused field puts no typed value in any log line.
# ---------------------------------------------------------------------


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_run2_a_refused_field_puts_no_typed_value_in_any_log_line(page, world):  # noqa: F811
    """RUN-2 (drc-d4-check-2026-09-25.md:179): the WHOLE request path of a
    refused change (review and apply) logs no figure he typed."""
    from loguru import logger

    figure = "86420"
    form = _form(**{"account.daily_stop_full": figure, "aset.sheet_modes.half.A": "x"})
    messages = []
    sink = logger.add(lambda m: messages.append(str(m)), format="{message}")
    try:
        for route in ("/settings/daily", "/settings/daily/apply"):
            r = page.post(route, data=dict(form, sha256="0" * 64))
            assert "FAILED" in r.text, route
    finally:
        logger.remove(sink)
    print(f"RUN-2 captured messages: {len(messages)}")
    assert [m for m in messages if figure in m] == []
    assert world.puts == []
