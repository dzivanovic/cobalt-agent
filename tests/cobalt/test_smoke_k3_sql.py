"""K3's committed statement, executed on Postgres (`requires_db`).

Every other smoke test runs on fakes: they prove the framework grades a
ROW the way the checklist says. Nothing proved that K3's SQL — the one
committed check with a CTE, a `CROSS JOIN` and its `FILTER` counters —
parses, runs under `cobalt_system`'s grants, and returns the columns its
predicates name (six since S2 smoke fix F3 added `unranked_retained`).
The last test below is OFFLINE: it reads the statement's text, not a
server. That answer only exists on a server, so it
lives here, behind the same `requires_db` guard
`tests/cobalt/test_radar_store.py` uses: SKIPPED offline, run by the hub
on `cobalt_dev`.

NOTHING PERSISTS. The suite's `dev_db_tx` fixture (autouse, see
`tests/cobalt/conftest.py`) hands every `db.connect()` caller a savepoint
proxy over ONE `cobalt_dev` connection whose outer transaction is always
rolled back — the rows constructed below and the `radar_pool` row they
change are gone when the test returns, whether it passes or fails.

WHAT THE SECOND TEST IS FOR. `s2-p4-build2-2026-09-18.md` ESCALATE 6:
K3's second set counts open admitted rows carrying the pool's own
`last_scan_id`, and `radar/store.py`'s HOLD branch stamps `last_scan_id`
too. So a pre-deploy episode that tonight's scan HELD because its only
source was degraded — keeping its pre-deploy NULL `rank_metric` — lands
in `rescanned_metric_missing` and reads exactly like a RETAIN defect. No
column tells the two apart. The test CONSTRUCTS that row and records what
the framework then grades, so the ambiguity is a measured fact in the
report rather than an argument. It builds no fix: the disposition is
Dejan's (accept the loud false positive with the `degraded_sources`
procedure K3's `expect_text` names, add a row-level discriminator, or
revert K3).
"""

from __future__ import annotations

import os
import re
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.smoke import checks
from cobalt.smoke.config import SUITES_DIR, load_suite
from cobalt.smoke.models import SmokeContext, Verdict

ET = ZoneInfo("America/New_York")

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)

#: The P4 deploy instant the checklist is run with, and the run's clock —
#: fixed, so the rendered statement is the same string every run.
CUTOFF = datetime(2026, 9, 18, 20, 5, tzinfo=ET)
NOW = datetime(2026, 9, 22, 21, 50, tzinfo=ET)
DAY = date(2026, 9, 22)

#: The columns K3's predicates and `known_if` name. Exactly these, in one
#: row: `_one_row` makes a second row ERROR, and a missing column is a
#: KeyError the framework reports as ERROR.
K3_COLUMNS = {
    "post_deploy_admitted", "metric_missing", "value_null", "unranked_retained",
    "rescanned_admitted", "rescanned_metric_missing",
}

POOL_KEY = "primary"
TICKER = "K3HOLD"


def _ctx() -> SmokeContext:
    """A real `SmokeContext`, built by hand rather than by
    `build_context`, so the cutoff and the clock are fixed values and the
    test does not depend on the registry's schedule arithmetic."""
    return SmokeContext(
        now=NOW, report_date=DAY, session="overnight", cutoff=CUTOFF,
        last_trading_day=DAY, last_summary_slot="16:30", last_summary_date=DAY,
        prod=False, tunables={},
    )


def _k3():
    return {c.id: c for c in load_suite(SUITES_DIR / "s2.yaml").checks}["K3"]


@requires_db
def test_k3_statement_parses_and_returns_its_six_counters_on_cobalt_dev():
    check = _k3()
    statement = checks.render_sql(check.query, _ctx())
    assert "{" not in statement, statement

    result = checks.default_deps(prod=False).read_rows(statement, check.side)
    assert len(result.rows) == 1, f"K3 must return exactly one row, got {len(result.rows)}"
    assert set(result.columns) == K3_COLUMNS, sorted(result.columns)


@requires_db
def test_k3_hold_row_reads_red_documented_ambiguity():
    """A frozen HOLD on a pre-deploy episode grades K3 FAIL.

    The constructed row is what `radar/store.py`'s HOLD branch leaves
    behind: an open, admitted episode first seen BEFORE the cutoff,
    carrying the pool's latest post-cutoff `last_scan_id` and a NULL
    `rank_metric` it has held since before the deploy.
    """
    conn = db.connect(env.DEV_DB_NAME, side=Side.SYSTEM)
    scan_id = conn.execute(
        "SELECT COALESCE(max(last_scan_id), 0) + 1 FROM system.radar_pool"
    ).fetchone()[0]

    # The pool row the CTE reads. If dev already has a `primary` row it is
    # CHANGED here, never duplicated — the transaction rolls it back.
    conn.execute(
        "INSERT INTO system.radar_pool (pool_key, state, session, members, "
        "last_scan_id, last_scan_at) VALUES (%s, 'idle', 'overnight', 0, %s, %s) "
        "ON CONFLICT (pool_key) DO UPDATE SET last_scan_id = EXCLUDED.last_scan_id, "
        "last_scan_at = EXCLUDED.last_scan_at",
        (POOL_KEY, scan_id, CUTOFF + timedelta(hours=1)),
    )
    # The held episode: born before the deploy, stamped by tonight's scan,
    # still carrying the NULL pair the deploy never backfilled (0008).
    first_seen = CUTOFF - timedelta(days=1)
    conn.execute(
        "INSERT INTO system.radar_membership (pool_key, ticker, trade_date, first_seen_at, "
        "entered_at, left_at, source, sources, last_rank, below_cap_streak, session, "
        "opened_scan_id, last_scan_id, rank_metric, rank_value) "
        "VALUES (%s, %s, %s, %s, %s, NULL, 'test', '[]'::jsonb, 1, 0, 'rth', %s, %s, NULL, NULL)",
        (POOL_KEY, TICKER, first_seen.astimezone(ET).date(), first_seen, first_seen,
         scan_id, scan_id),
    )

    context = _ctx()
    check = _k3()
    result = checks.default_deps(prod=False).read_rows(
        checks.render_sql(check.query, context), check.side
    )
    row = dict(zip(result.columns, result.rows[0]))
    assert row["rescanned_admitted"] >= 1, row
    assert row["rescanned_metric_missing"] >= 1, row

    # The framework's own grader, on the row the server returned.
    outcome = checks.evaluate(check, context, checks.default_deps(prod=False))
    assert outcome.verdict is Verdict.FAIL, (outcome.verdict.value, outcome.detail)
    assert "rescanned_metric_missing" in outcome.detail, outcome.detail


# ---------------------------------------------------------------------
# S2 smoke fix F3 — OFFLINE: what K3's statement grades (no server)
# ---------------------------------------------------------------------


def _filter_of(query: str, column: str) -> str:
    """The `FILTER (WHERE …)` condition of the counter named `column`."""
    match = re.search(r"FILTER \(WHERE ([^)]*)\) AS " + column + r"\b", query)
    assert match, f"no FILTER counter named {column}"
    return match.group(1)


def _op(predicate) -> str:
    return str(getattr(predicate.op, "value", predicate.op))


def test_k3_grades_only_a_ranked_row_that_stored_no_metric():
    """A sticky RETAIN of a member the scan no longer ranks writes
    `last_rank`, `rank_metric`, `rank_value` = NULL, NULL, NULL by design
    (`radar/pool.py` Transition: "None where no ranking happened"), so a
    NULL metric alone is not the write-path defect K3 exists for — a NULL
    metric on a row the scan RANKED (`last_rank IS NOT NULL`) is."""
    check = _k3()
    query = " ".join(check.query.split())
    assert "m.last_rank" in query
    for column in ("metric_missing", "rescanned_metric_missing"):
        condition = _filter_of(query, column)
        assert "rank_metric IS NULL" in condition and "last_rank IS NOT NULL" in condition, column
    # the designed class is printed as evidence, never graded
    unranked = _filter_of(query, "unranked_retained")
    assert "inserted_after" in unranked
    assert "rank_metric IS NULL" in unranked and "last_rank IS NULL" in unranked
    assert "last_rank IS NOT NULL" not in unranked
    assert "unranked_retained" not in {p.column for p in check.expect}
    assert "value_null" not in {p.column for p in check.expect}
    assert [(p.column, _op(p), p.value) for p in check.known_if] == [
        ("post_deploy_admitted", "eq", 0), ("rescanned_admitted", "eq", 0)]
    assert check.query.count("{cutoff}") == 2
