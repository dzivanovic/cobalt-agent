"""DRC K3 — THE SURFACES, offline (card `01-drc-k3-card.md` rows K3-1 … K3-9;
each row's full text is `prompts/2026-09-29/30-drc-k3-build.md`'s row of the
same id).

What runs here without a database:
- the build over a CONSTRUCTED ROW SET: `test_drc_build.py`'s `_Store`
  (BY IMPORT) holds rows the real `DrcStore._rows` writes over D1's
  fixtures paired by `pairing.build_day` — no row shape is invented;
- the page actions (`imports.state_book` / `imports.resolve`) over
  `_Statements`, an in-memory `DrcStore` double whose positions and hash
  come from the store's own `DrcStore._validated` (the canonical rows and
  their `book_sha256`); the effect's store calls are recorded;
- the routes through FastAPI's `TestClient` (D2's page tests' pattern).

Constructed 2001 dates and constructed symbols only (L32 / L45); every
note in a `tmp_path` vault.
"""

from __future__ import annotations

import copy
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

from cobalt.drc.detect import detect_kind
from cobalt.drc.models import (
    Kind,
    ImportResult,
    Outcome,
    PairingError,
    ParsedTradingLog,
    ResolveInput,
    SeedBook,
    StatedBook,
    StatedPosition,
    StatedResolve,
)
from cobalt.drc.pairing import FN_VERSION as PAIRING_FN, book_sha256, build_day, stated_open_positions
from cobalt.drc.stats_log import StatsLogSource
from cobalt.drc.store import DrcStore
from cobalt.drc.trading_log import TradingLogSource

from test_drc_build import (
    SHAPE,
    TEN_ET,
    _deps,
    _import_row,
    _json,
    _note,
    _outside_sections,
    _record,
    _Store,
    _unit_body,
    _vault,
)
from test_drc_k2_experiments import DDD_COVER, EEE_ROUND, _log
from test_drc_store import D, D_NEXT, DAY1, STATS, weekday_calendar  # noqa: F401 — fixture used by name

RESET_ET = datetime(2026, 9, 4, 0, 15, tzinfo=timezone.utc)  # 20:15 ET
D_THIRD = date(2001, 1, 4)
EXIT_NOT_IN_ANY_EXPORT = "not computed — exit not in any export"
NOT_STATED = "not computed — opening book not stated"
#: Two longs left open, `MMM` before `ZZZ` by trade id.
TWO_OPEN = _log(
    "10:10:00,ZZZ,B,7.5,10,ROUTE1,BRK1,ACCT1,Margin,H0000000000502,",
    "10:00:00,MMM,B,9.25,5,ROUTE2,BRK2,ACCT1,Margin,H0000000000501,",
)
GGG = {"symbol": "GGG", "direction": "short", "shares": 40, "avg_cost": None}


# ---------------------------------------------------------------------
# the constructed row set (the shape `test_drc_build._record` builds)
# ---------------------------------------------------------------------


class _K3Store(_Store):
    """`_Store` plus the reads K3's page and stale line make."""

    def __init__(self, *, seed=None, superseded=(), stated_days=None):
        super().__init__()
        self.seed = seed
        self.superseded = set(superseded)
        self.stated_days = dict(stated_days or {})
        self.asked: list[list[int]] = []

    def seed_for(self, day):
        return self.seed

    def stated_difference(self, day):
        return None

    def superseded_stated_ids(self, ids):
        ids = sorted(ids)
        self.asked.append(ids)
        return {i for i in ids if i in self.superseded}

    def stated_day(self, stated_id):
        return self.stated_days[stated_id]


def _put(store, day, pairing, ids, seed, *, no_trade_id=None, extra=None, imports_=()):
    """`pairing` recorded as `DrcStore._rows` writes it; D2's event for it."""
    from cobalt.drc import imports

    krows = [
        dict(kind=k, ref=r, inputs=_json(i), derived=_json(dv), fn_version=PAIRING_FN)
        for k, r, i, dv in DrcStore._rows(pairing, ids, seed, no_trade_id, extra or {})
    ]
    day_row = next(r for r in krows if r["kind"] == "day")
    seed_row = next((r for r in krows if r["kind"] == "seed"), None)
    store.views[day] = dict(
        import_id=None if no_trade_id else 1, event_id=10 + len(store.views),
        source="stated_book" if no_trade_id else "import", state="running", updated_at=None, error=None,
        note_path=None, stated_book_id=no_trade_id, stated_book_sha256="a" * 64 if no_trade_id else None,
        seed=None if seed_row is None else {k: seed_row["inputs"].get(k) for k in (
            "source", "from_day", "from_book_sha256", "stated_book_id", "no_trade_id")},
        imports=list(imports_), day={"inputs": day_row["inputs"], "derived": day_row["derived"]},
        trades=sorted(r["ref"] for r in krows if r["kind"] == "trade"),
        rows={k: sum(1 for r in krows if r["kind"] == k) for k in ("trade", "open_position", "stats_row")},
    )
    store.krows[day] = krows
    return imports._event(day, store.views[day], imports._orphans(store.views[day]))


def _day(store, day, trading: bytes, seed: SeedBook, *, extra=None):
    """A trades day (its trading log + the constructed stats log) paired from
    `seed`, its resolves applied by `build_day` (K2's route)."""
    stats = STATS.read_bytes()
    t = TradingLogSource().parse(trading, day, detect_kind("t.md", trading))
    s = StatsLogSource().parse(stats, detect_kind("s.md", stats))
    pairing = build_day(t, s, seed=seed.positions, resolves=seed.resolves)
    imports_ = [_import_row(1, "trading_log", "t.md", trading, t, fills=len(t.executions)),
                _import_row(2, "stats_log", "s.md", stats, s)]
    return _put(store, day, pairing, {Kind.TRADING_LOG: 1, Kind.STATS_LOG: 2}, seed,
                extra=extra, imports_=imports_)


def _no_trade_day(store, day, seed: SeedBook, *, statement: int = 5):
    """A file-less no-trade day carrying `seed` (K2's no-trade seed rule)."""
    parsed = ParsedTradingLog(
        result=ImportResult(name="no-trade DRC", kind=Kind.TRADING_LOG, outcome=Outcome.PARSED),
        import_date=day, executions=[],
    )
    pairing = build_day(parsed, None, seed=seed.positions)
    return _put(store, day, pairing, {}, DrcStore._no_trade_seed(seed, statement), no_trade_id=statement)


def _carried(store, prior=D, **kw) -> SeedBook:
    """`prior`'s close as the next day's carried book (`seed_for`'s shape)."""
    rows = [r["derived"] for r in store.krows[prior] if r["kind"] == "open_position"]
    from cobalt.drc.models import OpenPosition

    positions = sorted((OpenPosition.model_validate(r) for r in rows), key=lambda p: p.trade_id)
    return SeedBook(source="carried", positions=positions, from_day=prior,
                    from_book_sha256=book_sha256(positions), **kw)


def _ddd(store, day=D) -> str:
    return next(r["ref"] for r in store.krows[day] if r["kind"] == "open_position")


def _built(tmp_path, store, event, **over):
    from cobalt.drc import build

    root = _vault(tmp_path)
    deps = _deps(store, root, **over)
    build.run_drc_build(event, deps=deps)
    return root, deps


def _build_day_row(store, day=D) -> dict:
    return next(r for r in store.build[day] if r["kind"] == "build_day")


def _close_sha(store, day=D) -> str:
    return next(r for r in store.krows[day] if r["kind"] == "book_close")["derived"]["book_sha256"]


# ---------------------------------------------------------------------
# K3-1 — the `drc-trades/open_positions` unit
# ---------------------------------------------------------------------


def test_k3_1_a_flat_day_says_left_open_0(tmp_path, weekday_calendar):
    """K3-1 (v3 §5 `:236`): a flat close → `left open: 0 — tomorrow starts
    flat (stated by this DRC)`, from the stored list (L57)."""
    store = _K3Store()
    root, _ = _built(tmp_path, store, _record(store))
    assert _unit_body(_note(root), "drc-trades", "open_positions") == [
        "left open: 0 — tomorrow starts flat (stated by this DRC)"]
    derived = _build_day_row(store)["derived"]
    assert derived["open_positions"] == [] and derived["open_overnight"] == 0


def test_k3_1_a_position_opened_today_is_new_today_day_1(tmp_path, weekday_calendar):
    """K3-1: the header with the stored `book_close` hash; one line per
    position — `new today`, `day 1`, `carried from —`; every figure a key of
    `build_day.derived["open_positions"]`, its inputs named (L57)."""
    store = _K3Store()
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()))
    tid = _ddd(store)
    assert _unit_body(_note(root), "drc-trades", "open_positions") == [
        f"left open: 1 — tomorrow's import starts from these · book: {_close_sha(store)[:12]}",
        f"DDD · long · 30 · avg cost $30.1 · opened 2001-01-02 · day 1 · new today · carried from — · "
        f"last execution 2001-01-02 · {tid}",
    ]
    row = _build_day_row(store)
    (pos,) = row["derived"]["open_positions"]
    assert pos["trade_id"] == tid and pos["days_held"] == 1 and pos["status"] == "new today"
    assert row["inputs"]["open_positions"]["kinds"] == ["book_close", "open_position", "seed", "trade"]


def test_k3_1_a_carried_position_is_continuing_day_2_carried_from_the_prior_day(tmp_path, weekday_calendar):
    """K3-1: a trade in the day's stored `seed` book → `continuing open
    position`; `day <k>` counts trading days from `opened_on` through the
    day, inclusive; `carried from` is the stored `carried_from` link's day."""
    store = _K3Store()
    _record(store, D, trading=DAY1.read_bytes())
    tid = _ddd(store)
    root, _ = _built(tmp_path, store, _day(store, D_NEXT, EEE_ROUND, _carried(store)))
    body = _unit_body(_note(root, D_NEXT), "drc-trades", "open_positions")
    assert body[1] == (
        f"DDD · long · 30 · avg cost $30.1 · opened 2001-01-02 · day 2 · continuing open position · "
        f"carried from 2001-01-02 · last execution 2001-01-02 · {tid}"
    )


def test_k3_1_a_carried_with_difference_day_still_carries_from_the_close(tmp_path, weekday_calendar):
    """K3-1 × RUN-1 (K2's `## FOR K3`): a carried book beside his stated
    opening (R51: the close wins) renders `carried from <prior day>`."""
    store = _K3Store()
    _record(store, D, trading=DAY1.read_bytes())
    seed = _carried(store, stated_book_id=9, stated_differs=["DDD-long: stated 40, close 30"])
    root, _ = _built(tmp_path, store, _day(store, D_NEXT, EEE_ROUND, seed))
    body = _unit_body(_note(root, D_NEXT), "drc-trades", "open_positions")
    assert "· continuing open position · carried from 2001-01-02 ·" in body[1]


def test_k3_1_a_stated_position_with_no_cost_or_open_day_says_so(tmp_path, weekday_calendar):
    """K3-1 (K2 `## FOR K3`): `opened_on` None → `opened not stated` AND
    `day not stated`; a lot with no price → `avg cost not given`; carried from
    `stated #<id>`; no stored execution → `last execution not stored`."""
    store = _K3Store()
    positions = stated_open_positions(D, [StatedPosition(**GGG)])
    seed = SeedBook(source="stated", positions=positions, stated_book_id=3, from_book_sha256="b" * 64)
    root, _ = _built(tmp_path, store, _day(store, D, EEE_ROUND, seed))
    body = _unit_body(_note(root), "drc-trades", "open_positions")
    assert body[1] == (
        "GGG · short · 40 · avg cost not given · opened not stated · day not stated · continuing open position · "
        "carried from stated #3 · last execution not stored · GGG-short-stated-2001-01-02"
    )


def test_k3_1_a_stated_lot_with_a_cost_renders_it(tmp_path, weekday_calendar):
    store = _K3Store()
    positions = stated_open_positions(D, [StatedPosition(**{**GGG, "avg_cost": "12.5"})])
    seed = SeedBook(source="stated", positions=positions, stated_book_id=3, from_book_sha256="b" * 64)
    root, _ = _built(tmp_path, store, _day(store, D, EEE_ROUND, seed))
    assert "· avg cost $12.5 ·" in _unit_body(_note(root), "drc-trades", "open_positions")[1]


def test_k3_1_a_no_trade_day_carries_the_position_unchanged(tmp_path, weekday_calendar):
    """K3-1 (v3 §2b `:97`): a no-trade day's positions are `continuing open
    position` with `last execution` unchanged."""
    store = _K3Store()
    _record(store, D, trading=DAY1.read_bytes())
    tid = _ddd(store)
    root, _ = _built(tmp_path, store, _no_trade_day(store, D_NEXT, _carried(store)))
    body = _unit_body(_note(root, D_NEXT), "drc-trades", "open_positions")
    assert body[1] == (
        f"DDD · long · 30 · avg cost $30.1 · opened 2001-01-02 · day 2 · continuing open position · "
        f"carried from 2001-01-02 · last execution 2001-01-02 · {tid}"
    )


def test_k3_1_a_day_the_calendar_does_not_cover_says_day_not_computed(tmp_path):
    """K3-1 / L1: `day <k>` from THE one calendar; a span it does not cover
    (the shipped NYSE calendar holds no 2001) → `day not computed — <the
    calendar's reason>`, never a weekday guess, and the build goes on (no
    `weekday_calendar` here, on purpose)."""
    store = _K3Store()
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()))
    line = _unit_body(_note(root), "drc-trades", "open_positions")[1]
    assert "· day not computed — no NYSE calendar for 2001 (asked about 2001-01-01)." in line
    assert line.startswith("DDD · long · 30 · ")


def test_k3_1_two_positions_are_sorted_by_trade_id(tmp_path, weekday_calendar):
    store = _K3Store()
    root, _ = _built(tmp_path, store, _record(store, D, trading=TWO_OPEN))
    body = _unit_body(_note(root), "drc-trades", "open_positions")
    assert body[0].startswith("left open: 2 — ")
    assert [line.split(" · ")[0] for line in body[1:]] == ["MMM", "ZZZ"]


def test_k3_1_an_unpaired_day_is_one_loud_line(tmp_path, weekday_calendar):
    """K3-1 / L1: pairing not computed → ONE line naming the stored reason,
    never `left open: 0`."""
    store = _K3Store()
    root, _ = _built(tmp_path, store, _record(store, flat=False))
    assert _unit_body(_note(root), "drc-trades", "open_positions") == [f"open positions: {NOT_STATED}"]


def test_k3_1_a_book_stale_day_is_one_stale_line(tmp_path, weekday_calendar):
    """K3-1 / K3-4 (b): a `derived.book_stale` day → `STALE — <root> has
    pairing not computed — its open positions are unknown`."""
    reason = "2001-01-01 has pairing not computed — its open positions are unknown"
    store = _K3Store()
    event = _record(store, D, trading=DAY1.read_bytes(), extra={"book_stale": {"root": "2001-01-01", "reason": reason}})
    root, _ = _built(tmp_path, store, event)
    assert _unit_body(_note(root), "drc-trades", "open_positions") == [f"STALE — {reason}"]


def test_k3_1_a_computed_day_with_no_book_close_is_loud(tmp_path, weekday_calendar):
    """K3-1 / L1: a computed day with no `book_close` row → `open positions:
    not computed — no book_close row for <day> (L1)`, never `left open: 0`."""
    store = _K3Store()
    event = _record(store)
    store.krows[D] = [r for r in store.krows[D] if r["kind"] != "book_close"]
    root, _ = _built(tmp_path, store, event)
    assert _unit_body(_note(root), "drc-trades", "open_positions") == [
        "open positions: not computed — no book_close row for 2001-01-02 (L1)"]


# ---------------------------------------------------------------------
# K3-2 — `open overnight: <n>` in the summary, from the SAME list
# ---------------------------------------------------------------------


@pytest.mark.parametrize("case, line", [
    ("flat", "open overnight: 0"),
    ("one", "open overnight: 1"),
    ("unpaired", f"open overnight: {NOT_STATED}"),
    ("stale", "open overnight: STALE — 2001-01-01 has pairing not computed — its open positions are unknown"),
    ("no_close", "open overnight: not computed — no book_close row for 2001-01-02 (L1)"),
])
def test_k3_2_the_summary_carries_open_overnight(tmp_path, weekday_calendar, case, line):
    """K3-2 (v3 §5 `:237`, `[F-11]`): ONE summary line from
    `build_day.derived["open_overnight"]` = the length of the SAME list."""
    store = _K3Store()
    stale = {"root": "2001-01-01", "reason": "2001-01-01 has pairing not computed — its open positions are unknown"}
    event = {
        "flat": lambda: _record(store),
        "one": lambda: _record(store, D, trading=DAY1.read_bytes()),
        "unpaired": lambda: _record(store, flat=False),
        "stale": lambda: _record(store, D, trading=DAY1.read_bytes(), extra={"book_stale": stale}),
        "no_close": lambda: _record(store),
    }[case]()
    if case == "no_close":
        store.krows[D] = [r for r in store.krows[D] if r["kind"] != "book_close"]
    root, _ = _built(tmp_path, store, event)
    summary = _unit_body(_note(root), "drc-summary", "summary")
    assert line in summary
    derived = _build_day_row(store)["derived"]
    if derived["open_positions"] is not None:
        assert derived["open_overnight"] == len(derived["open_positions"])


# ---------------------------------------------------------------------
# K3-3 — the A31 line `drc-open-items/open_positions`
# ---------------------------------------------------------------------


@pytest.mark.parametrize("case", ["flat", "one", "two", "unpaired"])
def test_k3_3_the_a31_unit_renders_the_same_list(tmp_path, weekday_calendar, case):
    """K3-3 (v3 §5 `:238`, `[F-11]`): `open items carried forward — open
    positions: <n>` then one line per position, from the SAME list; `none`
    at 0; the K3-1 state verbatim."""
    store = _K3Store()
    trading = {"flat": None, "one": DAY1.read_bytes(), "two": TWO_OPEN, "unpaired": None}[case]
    event = _record(store, flat=case != "unpaired", **({} if trading is None else {"trading": trading}))
    root, _ = _built(tmp_path, store, event)
    body = _unit_body(_note(root), "drc-open-items", "open_positions")
    if case == "flat":
        assert body == ["open items carried forward — open positions: none"]
    elif case == "unpaired":
        assert body == [f"open items carried forward — open positions: {NOT_STATED}"]
    else:
        listed = _build_day_row(store)["derived"]["open_positions"]
        assert body == [f"open items carried forward — open positions: {len(listed)}"] + [
            f"{p['symbol']} {p['direction']} {p['held_shares']} · {p['trade_id']} · day {p['days_held']}"
            for p in listed
        ]
        assert [p["trade_id"] for p in listed] == sorted(p["trade_id"] for p in listed)


def test_k3_3_the_a31_section_sits_after_drc_trades_and_his_lines_stay_byte_identical(tmp_path, weekday_calendar):
    """K3-3: the section directly after `drc-trades`, nothing outside a
    section but his lines and the writer's two blank lines (D3's E3
    comparison, its helper by import); built twice, identical."""
    from cobalt.drc import build

    store = _K3Store()
    event = _record(store, D, trading=DAY1.read_bytes())
    root, deps = _built(tmp_path, store, event)
    text = _note(root).read_text()
    lines = text.split("\n")
    assert lines.index("<!-- cobalt:section drc-open-items -->") == lines.index(
        "<!-- /cobalt:section drc-trades -->") + 1
    expected = SHAPE.read_text().replace("{{date:YYYY-MM-DD}}", D.isoformat()).split("\n")
    outside = _outside_sections(text)
    assert outside[: len(expected)] == expected and outside[len(expected):] == ["", ""]
    build.run_drc_build(event, deps=deps)
    assert _note(root).read_text() == text


# ---------------------------------------------------------------------
# K3-4 — the stale renderings
# ---------------------------------------------------------------------


def _resolved_day(superseded=()):
    """D leaves DDD open; D_NEXT's file never touches it; resolve #7 for it
    dated D_NEXT is applied by `build_day` (K2)."""
    store = _K3Store(superseded=superseded, stated_days={7: D_NEXT})
    _record(store, D, trading=DAY1.read_bytes())
    tid = _ddd(store)
    seed = _carried(store, resolves=[ResolveInput(id=7, resolve=StatedResolve(trade_id=tid))])
    return store, tid, _day(store, D_NEXT, EEE_ROUND, seed)


def test_k3_4_a_a_superseded_resolve_named_by_a_stored_row_renders_stale(tmp_path, weekday_calendar):
    """K3-4 (a) (K2 fix r2 `## FOR K3`): a stored row naming a resolve id
    that is no longer current → `STALE — resolve #<id> was restated; rebuild
    <effect day> once <effect day>'s input is recorded` — never a current
    close; the current set read by `DrcStore.superseded_stated_ids`."""
    store, _, event = _resolved_day(superseded={7})
    root, _ = _built(tmp_path, store, event)
    body = _unit_body(_note(root, D_NEXT), "drc-trades", "open_positions")
    assert body[0] == "STALE — resolve #7 was restated; rebuild 2001-01-03 once 2001-01-03's input is recorded"
    assert store.asked == [[7]]


def test_k3_4_a_a_current_resolve_renders_no_stale_line(tmp_path, weekday_calendar):
    store, _, event = _resolved_day()
    root, _ = _built(tmp_path, store, event)
    body = _unit_body(_note(root, D_NEXT), "drc-trades", "open_positions")
    assert not any(line.startswith("STALE") for line in body)
    assert body == ["left open: 0 — tomorrow starts flat (stated by this DRC)"]


def test_k3_4_c_a_note_failure_marks_the_build_day_and_a_clean_build_clears_it(tmp_path, weekday_calendar):
    """K3-4 (c) (v3 `[F-03]` note half): `write_note` raising AFTER
    `record_build` → the date's `build_day` re-recorded through the SAME
    `record_build` with `derived["note_stale"] = {note, error}`, then the
    error raised; the next clean build writes `build_day` without the key."""
    from cobalt.drc import build

    store = _K3Store()
    root = _vault(tmp_path)
    event = _record(store)
    deps = _deps(store, root)
    blocker = _note(root)
    blocker.mkdir()
    with pytest.raises(IsADirectoryError):
        build.run_drc_build(event, deps=deps)
    stale = _build_day_row(store)["derived"]["note_stale"]
    assert stale["note"] == str(blocker) and stale["error"].startswith("IsADirectoryError: ")
    assert store.recorded == [D, D]
    blocker.rmdir()
    build.run_drc_build(event, deps=deps)
    assert "note_stale" not in _build_day_row(store)["derived"]


def test_k3_4_c_day_view_shows_the_note_stale_line_from_the_stored_key(tmp_path, weekday_calendar, monkeypatch):
    from cobalt.drc import imports

    store = _K3Store()
    _record(store)
    store.build[D] = [dict(kind="build_day", ref="build", inputs={}, fn_version="drc.build/1",
                           derived={"note_stale": {"note": "/v/DRC-2001-01-02.md", "error": "OSError: disk"}})]
    monkeypatch.setattr(imports, "DrcStore", lambda: store)
    view = imports.day_view(D, vault_root=tmp_path)
    assert "note stale: /v/DRC-2001-01-02.md — OSError: disk · the book above is the database's" in view.notes


# ---------------------------------------------------------------------
# K3-5 — the `/drc` hand-off and the after-drop line
# ---------------------------------------------------------------------


class _Seed:
    def __init__(self, book=None, error=None):
        self.book, self.error = book, error

    def seed_for(self, day):
        if self.error:
            raise PairingError(self.error)
        return self.book


def test_k3_5_a_the_book_is_none_line_names_the_form(weekday_calendar):
    """K3-5 (a): ONLY `_morning`'s `book is None` line changes."""
    from cobalt.drc import imports

    assert imports._morning(_Seed(), D) == [
        "state your opening book for 2001-01-02 — the form below (or cobalt drc state-book --opening 2001-01-02 …)"]


def test_k3_5_a_every_other_morning_line_is_byte_for_byte(weekday_calendar):
    from cobalt.drc import imports

    error = "2001-01-03: the prior trading day 2001-01-02 has no import and no no-trade record, while 2001-01-01 does"
    assert imports._morning(_Seed(error=error), D_NEXT) == [
        error, "No prior DRC for 2001-01-02 — import it, record its no-trade DRC, or state your book"]
    positions = stated_open_positions(D, [StatedPosition(**GGG)])
    stated = SeedBook(source="stated", positions=positions, stated_book_id=3, from_book_sha256="b" * 64)
    assert imports._morning(_Seed(stated), D) == [
        "Starting book stated for 2001-01-02 (statement #3): 1 open (GGG)", "GGG short 40 · opened: not stated"]
    carried = SeedBook(source="carried", positions=[], from_day=D, from_book_sha256=book_sha256([]))
    assert imports._morning(_Seed(carried), D_NEXT) == ["Starting book from DRC 2001-01-02: 0 open (flat)"]


@pytest.mark.parametrize("trading, line", [
    (DDD_COVER, "1 carried closed · 0 still open → tonight's DRC"),
    (EEE_ROUND, "0 carried closed · 1 still open → tonight's DRC"),
])
def test_k3_5_b_the_after_drop_line_from_the_stored_rows(tmp_path, weekday_calendar, monkeypatch, trading, line):
    """K3-5 (b) (v3 §5 `:240`): `<k> carried closed · <m> still open →
    tonight's DRC` from the day's stored `seed` book and `open_position`
    rows; shown on a paired day only."""
    from cobalt.drc import imports

    store = _K3Store()
    _record(store, D, trading=DAY1.read_bytes())
    _day(store, D_NEXT, trading, _carried(store))
    monkeypatch.setattr(imports, "DrcStore", lambda: store)
    assert imports.day_view(D_NEXT, vault_root=tmp_path).after_drop == line


def test_k3_5_b_no_after_drop_line_on_an_unpaired_day(tmp_path, weekday_calendar, monkeypatch):
    from cobalt.drc import imports

    store = _K3Store()
    _record(store, flat=False)
    monkeypatch.setattr(imports, "DrcStore", lambda: store)
    assert imports.day_view(D, vault_root=tmp_path).after_drop is None


def test_k3_5_c_the_page_shows_the_form_and_resolve_beside_starting_book():
    """K3-5 (c): the form (K3-6) and RESOLVE (K3-7, one per carried trade)
    beside STARTING BOOK — a form, not a second morning line."""
    from cobalt.aset import drc_page
    from cobalt.drc.imports import DayView

    view = DayView(date=D_NEXT, morning=["Starting book from DRC 2001-01-02: 1 open (DDD)"],
                   carried=["DDD-long-x"], after_drop="0 carried closed · 1 still open → tonight's DRC",
                   status_line="READY")
    page = drc_page.render(view)
    assert 'action="/drc/state-book"' in page and "I was flat" in page and "List positions" in page
    assert 'action="/drc/resolve"' in page and 'value="DDD-long-x"' in page
    assert "0 carried closed · 1 still open → tonight&#x27;s DRC" in page or \
        "0 carried closed · 1 still open → tonight's DRC" in page
    assert page.count("Starting book from DRC") == 1


# ---------------------------------------------------------------------
# K3-6 — the state-your-book form; K3-7 — RESOLVE (the store double)
# ---------------------------------------------------------------------


class _Statements:
    """`DrcStore`'s statement API, in memory. Positions and hash are the
    store's own (`DrcStore._validated`); the refusals are its words."""

    def __init__(self, *, imports=(), chain=(), later=(), seed=None, rebuild_error=None):
        self.rows: list[StatedBook] = []
        self.imports, self.chain, self.later = set(imports), set(chain), list(later)
        self.seed, self.rebuild_error = seed, rebuild_error
        self.calls: list[str] = []

    def preview_stated_book(self, day, kind, positions, *, via, supersedes=None, **kw):
        rows, sha = DrcStore._validated(kind, positions, via, None, None)
        self.calls.append("preview")
        return StatedBook(day=day, kind=kind, positions=rows, book_sha256=sha, via=via,
                          reason="first import", supersedes=supersedes)

    def record_stated_book(self, day, kind, positions, *, via, supersedes=None, expected_sha256=None, now=None,
                           **kw):
        from cobalt.session import assert_writable

        assert_writable("drc.record_stated_book", target=day.isoformat(), now=now)
        rows, sha = DrcStore._validated(kind, positions, via, None, None)
        if expected_sha256 is not None and expected_sha256 != sha:
            raise ValueError(f"book_sha256 {sha} is not the reviewed {expected_sha256} — nothing written")
        superseded = {r.supersedes for r in self.rows}
        current = [r.id for r in self.rows if r.day == day and r.kind == kind and r.id not in superseded]
        if supersedes is None and current:
            raise ValueError(f"{day} {kind}: drc_stated_books #{current[0]} ({day}) is current — a restatement "
                             "names it with supersedes; nothing written")
        row = StatedBook(id=len(self.rows) + 1, day=day, kind=kind, positions=rows, book_sha256=sha, via=via,
                         reason="first import", supersedes=supersedes)
        self.rows.append(row)
        self.calls.append("record")
        return row

    def stated_day(self, stated_id):
        return next(r.day for r in self.rows if r.id == stated_id)

    def effect_day(self, day, supersedes):
        return day if supersedes is None else min(day, self.stated_day(supersedes))

    def has_current_import(self, day, kind):
        return day in self.imports

    def has_chain_through(self, day):
        return any(d <= day for d in self.chain)

    def rebuild(self, day):
        self.calls.append(f"rebuild {day}")
        if self.rebuild_error:
            raise PairingError(self.rebuild_error)
        return [day, *self.later]

    def seed_for(self, day):
        return self.seed


@pytest.fixture
def statements(monkeypatch):
    """`imports.DrcStore` → a `_Statements`; `build.rebuild_notes` → a spy
    (K3-8's function, its own tests below); the session block store quiet."""
    from cobalt.drc import build, imports
    from cobalt.session.store import SessionBlockStore

    monkeypatch.setattr(SessionBlockStore, "record", lambda self, **kw: None)
    holder: dict = {"store": _Statements(), "notes": []}
    monkeypatch.setattr(imports, "DrcStore", lambda: holder["store"])

    def _notes(dates, *, deps=None):
        holder["notes"].append(list(dates))
        if holder.get("notes_error"):
            raise build.BuildError(holder["notes_error"])
        return [Path(f"/v/DRC-{d}.md") for d in dates]

    # `raising=False`: on a tree without K3-8 the test fails in its body,
    # naming the missing K3 action — never at setup.
    monkeypatch.setattr(build, "rebuild_notes", _notes, raising=False)
    return holder


def test_k3_6_i_was_flat_is_one_tap(statements):
    """K3-6 (v3 §2c row A): `[I was flat]` → ONE `record_stated_book(day,
    "opening", [], via="drc_page")`, no preview; no import yet → `stated;
    <effect day> has no import yet`."""
    from cobalt.drc import imports

    result = imports.state_book(D, [], now=TEN_ET)
    store = statements["store"]
    assert [(r.kind, r.positions, r.via) for r in store.rows] == [("opening", [], "drc_page")]
    assert "preview" not in store.calls
    assert result.status_line == "stated; 2001-01-02 has no import yet" and statements["notes"] == []


def test_k3_6_a_listed_book_is_previewed_then_confirmed_with_its_sha(statements):
    """K3-6 (L7's mechanical half): a listed book → a preview (nothing
    written) carrying the row and its `book_sha256`; `Confirm` with that sha
    → written, `via = drc_page`."""
    from cobalt.drc import imports

    store = statements["store"]
    preview = imports.state_book(D, [GGG], now=TEN_ET)
    assert store.rows == [] and preview.preview is not None
    rows, sha = DrcStore._validated("opening", [GGG], "drc_page", None, None)
    assert preview.preview.sha256 == sha and preview.preview.positions == rows
    done = imports.state_book(D, preview.preview.positions, expected_sha256=sha, now=TEN_ET)
    assert [(r.positions, r.via, r.book_sha256) for r in store.rows] == [(rows, "drc_page", sha)]
    assert done.refused is None


def test_k3_6_a_wrong_sha_is_the_stores_refusal_and_no_row(statements):
    from cobalt.drc import imports

    _, sha = DrcStore._validated("opening", [GGG], "drc_page", None, None)
    result = imports.state_book(D, [GGG], expected_sha256="0" * 64, now=TEN_ET)
    assert result.refused == f"book_sha256 {sha} is not the reviewed {'0' * 64} — nothing written"
    assert statements["store"].rows == []


def test_k3_6_a_second_current_opening_is_refused_and_a_restatement_supersedes(statements):
    from cobalt.drc import imports

    imports.state_book(D, [], now=TEN_ET)
    again = imports.state_book(D, [], now=TEN_ET)
    assert again.refused == ("2001-01-02 opening: drc_stated_books #1 (2001-01-02) is current — a restatement "
                             "names it with supersedes; nothing written")
    imports.state_book(D, [], supersedes=1, now=TEN_ET)
    assert [r.supersedes for r in statements["store"].rows] == [None, 1]


def test_k3_6_inside_market_reset_is_refused_and_nothing_written(statements):
    from cobalt.drc import imports

    result = imports.state_book(D, [], now=RESET_ET)
    assert result.refused == imports.RESET_REFUSAL and statements["store"].rows == []
    assert imports.resolve(D, "DDD-long-x", now=RESET_ET).refused == imports.RESET_REFUSAL


def test_k3_6_a_day_with_its_import_rebuilds_from_the_effect_day_and_rewrites_every_note(statements):
    """K3-6 + K3-8: `statement_rebuilds` true → `rebuild(effect_day(day,
    supersedes))` → the notes of EVERY date it returned."""
    from cobalt.drc import imports

    statements["store"] = _Statements(imports={D}, later=[D_NEXT])
    result = imports.state_book(D, [], now=TEN_ET)
    assert statements["store"].calls == ["record", f"rebuild {D}"]
    assert statements["notes"] == [[D, D_NEXT]]
    assert result.status_line == "rebuilt: 2001-01-02, 2001-01-03"


def test_k3_6_a_refused_rebuild_is_loud_and_the_statement_kept(statements):
    from cobalt.drc import imports

    statements["store"] = _Statements(imports={D}, rebuild_error="2001-01-02: constructed refusal")
    result = imports.state_book(D, [], now=TEN_ET)
    assert result.status_line == "not rebuilt: 2001-01-02: constructed refusal"
    assert len(statements["store"].rows) == 1 and statements["notes"] == []


def test_k3_6_a_notes_failure_is_loud_the_database_committed(statements):
    from cobalt.drc import imports

    statements["store"] = _Statements(imports={D})
    statements["notes_error"] = "re-paired 2001-01-02: note /v failed — OSError: x · not rebuilt: none"
    result = imports.state_book(D, [], now=TEN_ET)
    assert result.status_line == (
        "rebuilt: 2001-01-02 · notes FAILED: re-paired 2001-01-02: note /v failed — OSError: x · not rebuilt: none")
    assert len(statements["store"].rows) == 1


def _old_rebuilds(store, day, kind, supersedes) -> bool:
    """`cli._rebuilds`' body at BASE `979ec797` (`git show
    979ec797:src/cobalt/drc/cli.py`, `:157`–`:161`), the request's fields
    named — the reference the moved body must equal."""
    effect = store.effect_day(day, supersedes)
    if store.has_current_import(effect, Kind.TRADING_LOG):
        return True
    tested = day if supersedes is None else store.stated_day(supersedes)
    return kind in ("no_trade", "resolve") and store.has_chain_through(tested)


@pytest.mark.parametrize("kind", ["opening", "no_trade", "resolve"])
@pytest.mark.parametrize("restated", [False, True])
@pytest.mark.parametrize("has_import", [False, True])
@pytest.mark.parametrize("chain", [False, True])
def test_k3_6_statement_rebuilds_equals_the_old_cli_decision(kind, restated, has_import, chain):
    """K3-6: `cli._rebuilds`' body MOVED to `imports.statement_rebuilds` —
    over kind × supersedes × a current import × a recorded chain it returns
    what the old body returned; `cli._rebuilds` calls it (L3)."""
    from cobalt.drc import cli, imports

    # The superseded row is dated D, the statement D_NEXT, the chain starts
    # at D_NEXT: the day a restatement tests (`stated_day`) differs from the
    # statement's own day, so a body that tests the wrong day returns another
    # answer (K2 fix r2 F-1r2).
    store = _Statements(imports={D} if has_import else (), chain={D_NEXT} if chain else ())
    store.rows.append(StatedBook(id=1, day=D, kind=kind, positions=[], book_sha256="c" * 64, via="cli",
                                 reason="x"))
    supersedes = 1 if restated else None
    day = D_NEXT
    expected = _old_rebuilds(store, day, kind, supersedes)
    assert imports.statement_rebuilds(store, day, kind, supersedes) is expected
    req = cli.StateBookRequest(day=day, kind=kind, supersedes=supersedes)
    assert cli._rebuilds(store, req) is expected


def test_k3_6_cli_rebuilds_delegates_to_the_one_decision(monkeypatch):
    from cobalt.drc import cli, imports

    seen = []
    monkeypatch.setattr(imports, "statement_rebuilds", lambda *a: seen.append(a) or True)
    req = cli.StateBookRequest(day=D, kind="opening")
    assert cli._rebuilds("store", req) is True and seen == [("store", D, "opening", None)]


def test_k3_7_resolve_a_carried_trade_preview_then_confirm(statements):
    """K3-7 (v3 §2b `:103`, `[F-06]`): offered only for a trade of
    `seed_for(day)`; preview → `Confirm` with its sha → one `resolve` row,
    `via = drc_page`, no exit price stored as none."""
    from cobalt.drc import imports

    positions = stated_open_positions(D, [StatedPosition(**GGG)])
    tid = positions[0].trade_id
    statements["store"] = _Statements(seed=SeedBook(source="stated", positions=positions, stated_book_id=3,
                                                    from_book_sha256="b" * 64))
    preview = imports.resolve(D_NEXT, tid, now=TEN_ET)
    assert statements["store"].rows == [] and preview.preview is not None
    rows, sha = DrcStore._validated("resolve", [{"trade_id": tid}], "drc_page", None, None)
    assert preview.preview.sha256 == sha
    imports.resolve(D_NEXT, tid, expected_sha256=sha, now=TEN_ET)
    (row,) = statements["store"].rows
    assert (row.kind, row.via, row.positions) == ("resolve", "drc_page", rows)
    assert row.positions[0]["exit_price"] is None


def test_k3_7_an_exit_price_is_in_the_reviewed_row(statements):
    from cobalt.drc import imports

    positions = stated_open_positions(D, [StatedPosition(**GGG)])
    tid = positions[0].trade_id
    statements["store"] = _Statements(seed=SeedBook(source="stated", positions=positions, stated_book_id=3,
                                                    from_book_sha256="b" * 64))
    preview = imports.resolve(D_NEXT, tid, exit_price="11.75", exit_time="2001-01-03T15:59:00-05:00", now=TEN_ET)
    assert preview.preview.positions[0]["exit_price"] == "11.75"


def test_k3_7_a_trade_not_carried_into_the_day_is_refused_and_nothing_written(statements):
    from cobalt.drc import imports

    statements["store"] = _Statements(seed=None)
    result = imports.resolve(D_NEXT, "QQQ-long-x", now=TEN_ET)
    assert result.refused == "refused: QQQ-long-x is not carried into 2001-01-03"
    assert statements["store"].rows == [] and statements["store"].calls == []


def test_k3_7_a_naive_exit_time_is_refused(statements):
    from cobalt.drc import imports

    positions = stated_open_positions(D, [StatedPosition(**GGG)])
    statements["store"] = _Statements(seed=SeedBook(source="stated", positions=positions, stated_book_id=3,
                                                    from_book_sha256="b" * 64))
    result = imports.resolve(D_NEXT, positions[0].trade_id, exit_time="2001-01-03T15:59:00", now=TEN_ET)
    assert result.refused == "refused: exit time '2001-01-03T15:59:00' has no UTC offset — a naive time is refused"
    assert statements["store"].rows == []


def test_k3_7_the_page_shows_the_resolved_trade_closed_and_every_outcome(tmp_path, weekday_calendar, monkeypatch):
    """K3-7: the resolved trade as the stored rows hold it — CLOSED, realized
    `not computed — exit not in any export`; the day row's `derived.resolves`
    (applied AND superseded) each with its reason; a superseded id STALE."""
    from cobalt.drc import imports

    store, tid, _ = _resolved_day()
    monkeypatch.setattr(imports, "DrcStore", lambda: store)
    view = imports.day_view(D_NEXT, vault_root=tmp_path)
    assert f"resolve #7 {tid}: applied — closed outside the export (resolve #7)" in view.resolves
    assert f"{tid}: CLOSED · realized {EXIT_NOT_IN_ANY_EXPORT} (resolve #7)" in view.resolves
    store.superseded = {7}
    stale = imports.day_view(D_NEXT, vault_root=tmp_path).resolves
    assert ("STALE — resolve #7 was restated; rebuild 2001-01-03 once 2001-01-03's input is recorded") in stale
    assert not any("CLOSED" in line for line in stale)


# ---------------------------------------------------------------------
# K3-8 — `build.rebuild_notes(dates)`, two callers
# ---------------------------------------------------------------------


def test_k3_8_rebuild_notes_builds_each_date_in_order(tmp_path, weekday_calendar):
    from cobalt.drc import build

    store = _K3Store()
    root = _vault(tmp_path)
    _record(store, D_NEXT, trading=DAY1.read_bytes(), no_stats=True)
    _record(store, D_THIRD, trading=DAY1.read_bytes(), no_stats=True)
    paths = build.rebuild_notes([D_NEXT, D_THIRD], deps=_deps(store, root))
    assert store.recorded == [D_NEXT, D_THIRD] and paths == [_note(root, D_NEXT), _note(root, D_THIRD)]


def test_k3_8_a_failure_names_the_note_the_date_and_the_later_dates(tmp_path, weekday_calendar):
    from cobalt.drc import build

    store = _K3Store()
    root = _vault(tmp_path)
    _record(store, D_NEXT, trading=DAY1.read_bytes(), no_stats=True)
    _record(store, D_THIRD, trading=DAY1.read_bytes(), no_stats=True)
    _note(root, D_NEXT).mkdir()
    with pytest.raises(build.BuildError) as failed:
        build.rebuild_notes([D_NEXT, D_THIRD], deps=_deps(store, root))
    assert str(failed.value).startswith(f"re-paired {D_NEXT}: note {_note(root, D_NEXT)} failed — IsADirectoryError")
    assert str(failed.value).endswith(f"· not rebuilt: {D_THIRD}")


def test_k3_8_run_drc_build_goes_through_rebuild_notes(tmp_path, weekday_calendar, monkeypatch):
    from cobalt.drc import build

    store = _K3Store()
    root = _vault(tmp_path)
    _record(store, D_NEXT, trading=DAY1.read_bytes(), no_stats=True)
    event = _record(store, D, extra={"repaired": [D_NEXT.isoformat()]})
    seen = []
    monkeypatch.setattr(build, "rebuild_notes", lambda dates, *, deps=None: seen.append(list(dates)) or [])
    build.run_drc_build(event, deps=_deps(store, root))
    assert seen == [[D_NEXT]]


# ---------------------------------------------------------------------
# K3-9 — the routes
# ---------------------------------------------------------------------


@pytest.fixture
def page(monkeypatch):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from cobalt.drc import imports
    from cobalt.drc.imports import DayView, PlaceResult

    class _Cards:
        def for_date(self, day):
            return []

    calls: list = []
    monkeypatch.setattr(web_module, "AsetStore", lambda: _Cards())
    monkeypatch.setattr(imports, "day_view", lambda day, cards=None: DayView(date=day, status_line="READY"))

    def _spy(name):
        def action(*args, **kw):
            calls.append((name, args, kw))
            if kw.get("supersedes") == 99:
                raise RuntimeError("constructed")
            return PlaceResult(date=args[0], message=f"{name} done")
        return action

    monkeypatch.setattr(imports, "state_book", _spy("state_book"), raising=False)
    monkeypatch.setattr(imports, "resolve", _spy("resolve"), raising=False)
    return TestClient(web_module.app), calls


def test_k3_9_post_state_book_flat_calls_the_one_action_once(page):
    client, calls = page
    response = client.post("/drc/state-book", data={"date": D.isoformat(), "flat": "1"})
    assert response.status_code == 200 and "state_book done" in response.text
    assert calls == [("state_book", (D, []), {"supersedes": None, "expected_sha256": None})]


def test_k3_9_post_state_book_listed_parses_the_rows(page):
    client, calls = page
    client.post("/drc/state-book", data={
        "date": D.isoformat(), "symbol": ["GGG", ""], "direction": ["short", "long"], "shares": ["40", ""],
        "avg_cost": ["", ""], "sha256": "d" * 64, "supersedes": "2"})
    assert calls == [("state_book", (D, [{"symbol": "GGG", "direction": "short", "shares": "40", "avg_cost": None}]),
                      {"supersedes": 2, "expected_sha256": "d" * 64})]


def test_k3_9_post_state_book_with_no_row_and_no_flat_is_refused(page):
    client, calls = page
    response = client.post("/drc/state-book", data={"date": D.isoformat(), "symbol": [""]})
    assert "refused: no position listed — [I was flat] states a flat book" in response.text and calls == []


def test_k3_9_post_resolve_calls_the_one_action_once(page):
    client, calls = page
    response = client.post("/drc/resolve", data={"date": D_NEXT.isoformat(), "trade_id": "DDD-long-x",
                                                 "exit_price": "", "exit_time": ""})
    assert response.status_code == 200 and "resolve done" in response.text
    assert calls == [("resolve", (D_NEXT, "DDD-long-x"),
                      {"exit_price": None, "exit_time": None, "supersedes": None, "expected_sha256": None})]


def test_k3_9_an_exception_is_the_failed_page(page):
    client, _ = page
    response = client.post("/drc/resolve", data={"date": D_NEXT.isoformat(), "trade_id": "x", "supersedes": "99"})
    assert '<div class="failed">FAILED' in response.text and "RuntimeError: constructed" in response.text
