"""DRC D2 — the one import place, WITH-DB half (`prompts/2026-09-25/
07-drc-d2-build.md` `## E3`): THE `[F-17]` ROUTE as K1 / K2 built it,
the morning line, the R51 line, the no-trade action, the event.

The DRC harness is reused BY IMPORT, never copied (`test_drc_store.py`'s
`migrated` / `weekday_calendar` / `requires_db`, `test_drc_k1_store.py`'s
`_state` / `TEN_ET`, `test_drc_k2_experiments.py`'s constructed days).
Everything runs inside `test_drc_store.py`'s never-committed migration
transaction on `cobalt_dev` (L76): nothing here commits a migration.
Every statement passes the constructed 10:00 ET `now=`. Constructed dates
`2001-01-02` … `2001-01-05` and constructed symbols only (L32 / L45);
every vault write lands in a `tmp_path` vault.
"""

from __future__ import annotations

import sys
from datetime import date

import pytest

from cobalt.drc.models import Kind
from cobalt.drc.store import DrcStore

from test_drc_k1_store import D3, GGG_SHORT, RESET_ET, TEN_ET, _row, _state, blocks  # noqa: F401
from test_drc_k2_experiments import D_FLAT, DDD_COVER, EEE_ROUND, _snapshot, _stated_rows
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)

SATURDAY = date(2001, 1, 6)
UNPAIRED = "not computed — opening book not stated · state your opening book for {d}"


@pytest.fixture
def lane(migrated, weekday_calendar, tmp_path, monkeypatch):
    """A `tmp_path` vault, no D3 build module (the build is not built),
    the cards read patched to none, and a TestClient on the ASET app."""
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module

    root = tmp_path / "vault"
    (root / "1 - Trading" / "5 - Review").mkdir(parents=True)
    monkeypatch.setenv("COBALT_VAULT_PATH", str(root))
    monkeypatch.delitem(sys.modules, "cobalt.drc.build", raising=False)

    class _Cards:
        def for_date(self, day):
            return []

    monkeypatch.setattr(web_module, "AsetStore", lambda: _Cards())
    return TestClient(web_module.app)


def _drop(day: date, trading: bytes | None = None, stats: bytes | None = None):
    from cobalt.drc import imports

    files = []
    if trading is not None:
        files.append((f"t-{day.isoformat()}.md", trading))
    if stats is not None:
        files.append((f"s-{day.isoformat()}.md", stats))
    return imports.place(day, files, now=TEN_ET)


def _counts(conn) -> tuple[int, int, int]:
    return tuple(
        conn.execute(f'SELECT count(*) FROM "user".{t}').fetchone()[0]
        for t in ("drc_imports", "drc_rows", "drc_stated_books")
    )


def _fingerprint(conn) -> dict[str, str]:
    """D2 fix r1 F-3 (`drc-d2-check-2026-09-25.md:144`, `:180`; L35): (a)
    for each `drc_*` table of `store.TABLES`, the md5 of its rows, ordered;
    (b) for EVERY table of EVERY schema, this transaction's `n_tup_ins +
    n_tup_upd + n_tup_del` from `pg_stat_xact_user_tables` — every
    connection of a with-DB test is the one migration transaction, so a
    write by any code in any table moves its counter (no full-table read
    of a large table)."""
    from cobalt.drc import store

    out = {
        f"md5:{t}": conn.execute(
            f"SELECT coalesce(md5(string_agg(t::text, '|' ORDER BY t::text)), '') FROM \"user\".{t} t"
        ).fetchone()[0]
        for t in store.TABLES
    }
    out.update(
        (f"writes:{schema}.{table}", str(n))
        for schema, table, n in conn.execute(
            "SELECT schemaname, relname, n_tup_ins + n_tup_upd + n_tup_del FROM pg_stat_xact_user_tables"
        ).fetchall()
    )
    return out


def _page(lane, day: date) -> str:
    from cobalt.aset import drc_page

    response = lane.get("/drc", params={"date": day.isoformat()})
    assert response.status_code == 200, response.text
    # F-3: never the route's whole-page failure (`drc_page.failed_page`),
    # always the status block (`drc_page.render`).
    marker = drc_page.failed_page("x").split("\nx", 1)[0].rsplit("\n", 1)[-1]
    assert marker == '<div class="failed">FAILED'
    assert marker not in response.text, response.text
    assert '<div class="status">' in response.text, response.text
    return response.text


# ---------------------------------------------------------------------
# seam (2) — first import, no statement
# ---------------------------------------------------------------------


@requires_db
def test_seam_2_a_first_import_with_no_statement_records_the_day_unpaired(lane, migrated):
    result = _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    day = _row(migrated, D, "day")
    assert day is not None and "pairing" in day[1]["not_computed"]
    assert _row(migrated, D, "seed") is None and _row(migrated, D, "book_close") is None
    assert result.status_line == UNPAIRED.format(d="2001-01-02")
    assert "state your opening book for 2001-01-02" in _page(lane, D)
    event = DrcStore().event_for(D)
    assert (event["state"], event["error"]) == ("failed", "build not built (D3)")


# ---------------------------------------------------------------------
# seam (3) — a stated day, then the carried next day
# ---------------------------------------------------------------------


@requires_db
def test_seam_3_a_stated_day_pairs_and_the_next_day_carries_its_close(lane, migrated):
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    assert _row(migrated, D, "seed")[0]["source"] == "stated"
    held = [r[0] for r in migrated.execute(
        "SELECT ref FROM \"user\".drc_rows WHERE day = %s AND kind = 'open_position'", (D,)
    ).fetchall()]
    assert len(held) == 1
    _drop(D_NEXT, DDD_COVER, STATS.read_bytes())
    assert _row(migrated, D_NEXT, "seed")[0]["source"] == "carried"
    assert migrated.execute(
        "SELECT count(*) FROM \"user\".drc_rows WHERE day = %s AND kind = 'trade' AND ref = %s", (D_NEXT, held[0])
    ).fetchone()[0] == 1


# ---------------------------------------------------------------------
# seam (1) — a seed_for raise is loud, the file stays stored
# ---------------------------------------------------------------------


@requires_db
def test_seam_1_a_skipped_prior_day_fails_the_event_verbatim_and_stores_the_file(lane, migrated):
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    try:
        DrcStore().seed_for(D3)
    except Exception as e:  # the raise text, read from the store itself
        raise_text = str(e)
    result = _drop(D3, EEE_ROUND, STATS.read_bytes())
    assert "2001-01-03" in raise_text
    event = DrcStore().event_for(D3)
    assert (event["state"], event["error"]) == ("failed", raise_text)
    assert result.status_line == f"DRC build FAILED: seed — {raise_text}"
    assert migrated.execute('SELECT count(*) FROM "user".drc_rows WHERE day = %s', (D3,)).fetchone()[0] == 0
    assert len([r for r in event["imports"] if r["current"]]) == 2
    page = _page(lane, D3)
    assert raise_text in page
    assert "No prior DRC for 2001-01-03 — import it, record its no-trade DRC, or state your book" in page


# ---------------------------------------------------------------------
# K2's forward re-pair seen from the page (R51)
# ---------------------------------------------------------------------


@requires_db
def test_the_earlier_close_rebuilds_the_stated_later_day_and_the_page_shows_r51(lane, migrated):
    _state(D_NEXT)
    _drop(D_NEXT, EEE_ROUND, STATS.read_bytes())
    _state(D)
    stated = _stated_rows(migrated)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    assert _stated_rows(migrated) == stated  # L7: his statements untouched by the drop
    ddd = migrated.execute(
        "SELECT ref FROM \"user\".drc_rows WHERE day = %s AND kind = 'open_position'", (D,)
    ).fetchone()[0]
    line = f"stated book for 2001-01-03 differed from 2001-01-02's close: {ddd}"
    assert DrcStore().stated_difference(D_NEXT) == line
    assert line in _page(lane, D_NEXT)


# ---------------------------------------------------------------------
# THE MORNING LINE (v3 §2b step 4, §5)
# ---------------------------------------------------------------------


@requires_db
def test_the_morning_line_names_the_prior_close_before_any_drop(lane, migrated):
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    before = _fingerprint(migrated)
    page = _page(lane, D_NEXT)
    assert "Starting book from DRC 2001-01-02: 1 open (DDD)" in page
    assert _fingerprint(migrated) == before


@requires_db
def test_the_morning_line_shows_a_stated_position_opened_not_stated(lane, migrated):
    _state(D, positions=[GGG_SHORT])
    before = _fingerprint(migrated)
    page = _page(lane, D)
    assert "1 open (GGG)" in page and "opened: not stated" in page
    assert _fingerprint(migrated) == before


@requires_db
def test_get_drc_writes_nothing(lane, migrated):
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    before = _fingerprint(migrated)
    for day in (D, D_NEXT, D3, SATURDAY):
        _page(lane, day)
    assert _fingerprint(migrated) == before


@requires_db
def test_the_fingerprint_and_the_page_check_can_fail(lane, migrated, monkeypatch):
    """F-3's NEGATIVE CONTROL (inside the rollback): a constructed UPDATE of
    one `drc_rows` value between two fingerprints moves BOTH halves (the
    table's md5 and its `pg_stat_xact_user_tables` counter); a `day_view`
    that raises makes the route's whole-page failure, which `_page`
    refuses."""
    from cobalt.drc import imports

    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    before = _fingerprint(migrated)
    with DrcStore()._connect() as conn:
        conn.execute("UPDATE drc_rows SET fn_version = 'constructed' WHERE day = %s AND kind = 'day'", (D,))
    after = _fingerprint(migrated)
    moved = {k for k in before.keys() | after.keys() if before.get(k) != after.get(k)}
    assert moved == {"md5:drc_rows", "writes:user.drc_rows"}, moved

    def _raise(*args, **kwargs):
        raise RuntimeError("constructed page failure")

    monkeypatch.setattr(imports, "day_view", _raise)
    with pytest.raises(AssertionError):
        _page(lane, D)


# ---------------------------------------------------------------------
# the current-file rule
# ---------------------------------------------------------------------


@requires_db
def test_a_second_trading_log_supersedes_the_first_and_the_day_is_the_new_files(lane, migrated):
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    first = DrcStore().event_for(D)["import_id"]
    _drop(D, D_FLAT)
    event = DrcStore().event_for(D)
    rows = {r["id"]: r for r in event["imports"]}
    assert rows[event["import_id"]]["supersedes"] == first and not rows[first]["current"]
    assert DrcStore().has_current_import(D, Kind.TRADING_LOG)
    trades = [r[0] for r in migrated.execute(
        "SELECT ref FROM \"user\".drc_rows WHERE day = %s AND kind = 'trade'", (D,)
    ).fetchall()]
    assert len(trades) == 1 and trades[0].startswith("DDD-long-2001-01-02T10:00:00")
    assert _row(migrated, D, "open_position") is None


# ---------------------------------------------------------------------
# D2-3c — "No trades today"
# ---------------------------------------------------------------------


@requires_db
def test_no_trade_after_a_recorded_day_states_it_and_records_the_carried_book(lane, migrated):
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    response = lane.post("/drc/no-trade", data={"date": D_NEXT.isoformat()})
    stated = migrated.execute(
        'SELECT kind, via FROM "user".drc_stated_books WHERE day = %s', (D_NEXT,)
    ).fetchall()
    assert stated == [("no_trade", "drc_page")]
    assert _row(migrated, D_NEXT, "seed")[0]["source"] == "no_trade_carry"
    # D2 fix r1 S-1 NAMED REVERSAL (NO_TRADE_WAITS removed): the file-less
    # event fires; with no D3 build it lands failed, never done (L1).
    assert "DRC build FAILED: build — build not built (D3)" in response.text


@requires_db
def test_no_trade_with_no_prior_record_is_stated_only(lane, migrated):
    from cobalt.drc import imports

    result = imports.no_trade(D, now=TEN_ET)
    assert result.message == "stated; 2001-01-02 has no import yet"
    assert migrated.execute('SELECT count(*) FROM "user".drc_rows').fetchone()[0] == 0


@requires_db
def test_no_trade_is_refused_on_a_day_with_executions_naming_the_count(lane, migrated):
    from cobalt.drc import imports

    _drop(D, DAY1.read_bytes())
    before = _counts(migrated)
    result = imports.no_trade(D, now=TEN_ET)
    assert result.refused == "refused: 2001-01-02 has a trading log with 4 executions — not a no-trade day"
    assert _counts(migrated) == before


@requires_db
def test_no_trade_is_refused_on_a_non_trading_date(lane, migrated):
    from cobalt.drc import imports

    result = imports.no_trade(SATURDAY, now=TEN_ET)
    assert result.refused == "refused: 2001-01-06 is not a market trading day"
    assert _counts(migrated) == (0, 0, 0)


@requires_db
def test_no_trade_is_refused_inside_market_reset(lane, migrated, blocks):
    from cobalt.drc import imports

    result = imports.no_trade(D, now=RESET_ET)
    assert result.refused == "refused: market reset 20:00–21:00 — drop again after 21:00"
    assert _counts(migrated) == (0, 0, 0)


@requires_db
def test_a_second_no_trade_shows_the_stores_refusal_verbatim(lane, migrated):
    from cobalt.drc import imports

    first = imports.no_trade(D, now=TEN_ET)
    again = imports.no_trade(D, now=TEN_ET)
    assert first.refused is None
    assert again.refused is not None and again.refused.startswith("2001-01-02 no_trade: drc_stated_books #")
    assert again.refused.endswith("is current — a restatement names it with supersedes; nothing written")


# ---------------------------------------------------------------------
# the event (L18: pending → running → done | failed)
# ---------------------------------------------------------------------


@requires_db
def test_the_event_moves_pending_running_then_failed_while_the_build_is_not_built(lane, migrated, monkeypatch):
    # D2 fix r1 S-1 §1 test 4: `pending` is `fire_event`'s, the rest
    # `mark_event`'s, keyed by the `drc_events` row.
    moves: list[str] = []
    real_fire, real = DrcStore.fire_event, DrcStore.mark_event

    def fire(self, day, **kw):
        moves.append("pending")
        return real_fire(self, day, **kw)

    def spy(self, event_id, state, error=None, **kw):
        moves.append(state)
        return real(self, event_id, state, error, **kw)

    monkeypatch.setattr(DrcStore, "fire_event", fire)
    monkeypatch.setattr(DrcStore, "mark_event", spy)
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    assert moves == ["pending", "running", "failed"]
    event = DrcStore().event_for(D)
    assert (event["state"], event["error"]) == ("failed", "build not built (D3)")
    assert event["updated_at"] is not None


@requires_db
def test_an_exception_in_the_build_is_failed_with_the_reason_never_done(lane, migrated, monkeypatch):
    import types

    module = types.ModuleType("cobalt.drc.build")

    def run_drc_build(event):
        raise KeyError("constructed")

    module.run_drc_build = run_drc_build
    monkeypatch.setitem(sys.modules, "cobalt.drc.build", module)
    _state(D)
    result = _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    event = DrcStore().event_for(D)
    assert event["state"] == "failed" and event["error"] == "KeyError: 'constructed'"
    assert result.status_line == "DRC build FAILED: build — KeyError: 'constructed'"


@requires_db
def test_the_event_payload_is_built_from_the_stored_rows(lane, migrated):
    _state(D)
    result = _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    rows = {r["kind"]: r for r in DrcStore().event_for(D)["imports"]}
    ev = result.event
    assert ev.import_id == rows["trading_log"]["id"] and ev.stats_import_id == rows["stats_log"]["id"]
    assert ev.sha256s == {str(r["id"]): r["sha256"] for r in rows.values()}
    assert ev.kind == "trades" and ev.partial == {}


@requires_db
def test_a_zero_execution_trading_log_is_the_no_trade_day_with_no_stats_log(lane, migrated):
    header = DAY1.read_bytes().splitlines(keepends=True)[0]
    _state(D)
    result = _drop(D, header)
    assert result.event is not None and result.event.kind == "no_trade"
    assert result.event.stats_import_id is None
    assert _row(migrated, D, "seed")[0]["source"] == "stated"
