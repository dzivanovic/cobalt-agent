"""DRC D5 — THE RECONCILE, offline (card `prompts/2026-10-04/03-drc-d5-card.md`
rows D5-1 … D5-4; v2 `:80` steps 1–6, S-C1 / S-C2, R90).

What runs here without a database:
- the build over a CONSTRUCTED ROW SET: `test_drc_build.py`'s `_Store` /
  `_record` and `test_drc_k3.py`'s `_K3Store` / `_day` / `_carried` (BY
  IMPORT) hold the rows the real `DrcStore._rows` writes over D1's fixtures
  paired by `pairing.build_day` — no row shape is invented;
- the card's legs: `_Legs`, an in-memory stand-in for the build's legs door
  (`BuildDeps.legs`). It answers `position` with `cards.legs`' own
  `Running` / `Position` and `cards.legs.realized_r` over its rows, records
  every write call, and raises `cards.legs.LegRefused` with the writer's own
  words where a test says so. The real writer is proven WITH-DB in
  `test_drc_d5_db.py`.

`DAY1` (`trading_log_carry_day1.csv`): EEE long 15 @ 40.0 09:45:00, out 15 @
40.25 09:50:30 (closed); DDD long 50 @ 30.1 10:00:00, out 20 @ 30.5 10:30:00
(30 held). Constructed 2001 dates, symbols and card ids only (L32 / L45);
every note in a `tmp_path` vault.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, timezone
from decimal import Decimal

import pytest

from cobalt.cards import legs as legs_mod
from cobalt.drc.models import ResolveInput, StatedResolve
from cobalt.session.clock import ET

from test_drc_build import TEN_ET, _card, _deps, _note, _record, _Store, _unit_body, _vault
from test_drc_k3 import _carried, _day, _K3Store
from test_drc_k2_experiments import EEE_ROUND
from test_drc_store import D, D_NEXT, DAY1, weekday_calendar  # noqa: F401 — fixture used by name

#: The card ids (constructed): EEE's card, DDD's card.
EEE_CARD, DDD_CARD = 41, 42
#: The event's trading log id in `_record` / `_day` (`_import_row(1, …)`).
IMPORT_ID = 1
CLOSED_OFF_ZERO = (
    "REFUSED card 42: CLOSED has no way back — this correction would leave 30 shares running. "
    "Nothing written."
)
NOT_BUILT = ["legs: not built", "adjustment pending (legs writer not built)"]


def _at(h, m, s=0, day=D):
    return datetime(day.year, day.month, day.day, h, m, s, tzinfo=ET)


def _leg(id_, card, seq, kind, shares, price, at, *, flag="confirmed", source="sheet", stop="39.90", **over):
    row = dict(
        id=id_, card_id=card, seq=seq, kind=kind, shares=shares, price=Decimal(price), at=at, flag=flag,
        price_source="typed" if source == "sheet" else "last_poll", price_asof=None,
        preset=None if kind == "entry" else "half", running_before=0, stop_in_force=Decimal(stop),
        source=source, source_import_id=None, held_stated=None, corrects=None,
    )
    row.update(over)
    return row


class _Legs:
    """The build's legs door, in memory: `cards.legs`' own read shapes over
    these rows; every write call recorded; a refusal raised where asked."""

    def __init__(self, cards, rows, *, refuse=None):
        self.cards = {c["id"]: dict(c) for c in cards}
        self.rows = [dict(r) for r in rows]
        self.calls: list[tuple] = []
        self.refuse = dict(refuse or {})
        self._ids = iter(range(900, 1000))

    def _current(self, card_id):
        cur = {}
        for r in sorted(self.rows, key=lambda r: r["id"]):
            if r["card_id"] == card_id:
                cur[r["seq"]] = r
        return [cur[s] for s in sorted(cur)]

    def position(self, card_id):
        if card_id not in self.cards:
            from cobalt.cards.store import CardStateError

            raise CardStateError(f"no aset_sizings row with id {card_id}")  # `running_shares`' words
        card = self.cards[card_id]
        cur = self._current(card_id)
        entry = next((r for r in cur if r["kind"] == "entry"), None)
        exits = sum(r["shares"] for r in cur if r["kind"] == "exit")
        if entry is None and card["state"] != "FILLED" and not exits:
            raise legs_mod.LegRefused(
                "no_position", f"card {card_id} is {card['state']} with no entry leg — it holds no position.")
        base = int(entry["shares"]) if entry else int(card["shares"])
        run = legs_mod.Running(
            base - exits, legs_mod.BASIS_LEGS if entry else legs_mod.BASIS_SHARES, base, exits,
            None if entry is None else entry["id"], None if entry is None else Decimal(entry["price"]),
            card["state"],
        )
        return legs_mod.Position(card, cur, run, legs_mod.realized_r(card, cur))

    def history(self, card_id):
        return [dict(r) for r in sorted(self.rows, key=lambda r: r["id"]) if r["card_id"] == card_id]

    def record_correction(self, leg_id, **kw):
        self.calls.append(("correction", leg_id, kw))
        if leg_id in self.refuse:
            raise self.refuse[leg_id]
        old = next(r for r in self.rows if r["id"] == leg_id)
        new = dict(old, id=next(self._ids), corrects=leg_id, source=kw["source"],
                   source_import_id=kw.get("source_import_id"))
        for key in ("shares", "price", "at", "flag", "price_source"):
            if kw.get(key) is not None:
                new[key] = kw[key]
        self.rows.append(new)
        after = self.position(old["card_id"]).running.shares
        return legs_mod.CorrectionResult(new["id"], leg_id, after, False, None)

    def record_exit(self, card_id, **kw):
        self.calls.append(("exit", card_id, kw))
        if ("exit", card_id) in self.refuse:
            raise self.refuse[("exit", card_id)]
        before = self.position(card_id).running.shares
        seq = max((r["seq"] for r in self.rows if r["card_id"] == card_id), default=0) + 1
        new = _leg(next(self._ids), card_id, seq, "exit", kw["shares"], kw["price"], kw["now"], flag=kw["flag"],
                   source=kw["source"], source_import_id=kw.get("source_import_id"), preset=kw["preset"],
                   price_source=kw["price_source"], running_before=before)
        self.rows.append(new)
        return legs_mod.ExitResult(new["id"], kw["shares"], before, before - kw["shares"], False, None)


def _eee_card(**over):
    return {**_card("EEE", "long", created=datetime(2001, 1, 2, 14, 40, tzinfo=timezone.utc), cid=EEE_CARD,
                    stop="39.9"), "shares": 15, **over}


def _ddd_card(**over):
    return {**_card("DDD", "long", created=datetime(2001, 1, 2, 14, 55, tzinfo=timezone.utc), cid=DDD_CARD,
                    stop="29.9"), "shares": 50, **over}


def _eee_tapped():
    """EEE's card: the fill (15 @ 40.00 at the export's time) and his ½ tap
    of 7 @ 40.10 (estimated, last poll)."""
    return [
        _leg(101, EEE_CARD, 0, "entry", 15, "40.0000", _at(9, 45)),
        _leg(102, EEE_CARD, 1, "exit", 7, "40.1000", _at(9, 50, 30), flag="estimated", source="panel",
             running_before=15),
    ]


def _ddd_flat():
    """X11's shape (v2 `:203`): DDD's card CLOSED by his flat tap of 50 while
    the export shows 20 out (30 held)."""
    return [
        _leg(201, DDD_CARD, 0, "entry", 50, "30.1000", _at(10, 0), stop="29.90"),
        _leg(202, DDD_CARD, 1, "exit", 50, "30.5000", _at(10, 30), source="panel", preset="flat",
             running_before=50, stop="29.90"),
    ]


def _deps_with(store, root, legs, cards, **over):
    deps = _deps(store, root, cards=cards, window=30, **over)
    deps.legs = legs  # set after construction: BASE's `BuildDeps` has no such field
    return deps


def _built(tmp_path, store, event, legs, cards):
    from cobalt.drc import build

    root = _vault(tmp_path)
    deps = _deps_with(store, root, legs, cards)
    build.run_drc_build(event, deps=deps)
    return root, deps


def _rows(store, day=D):
    return store.build[day]


def _trade_build(store, symbol, day=D):
    return next(r for r in _rows(store, day) if r["kind"] == "build_trade" and r["ref"].startswith(f"{symbol}-"))


def _day_build(store, day=D):
    return next(r for r in _rows(store, day) if r["kind"] == "build_day")


def _reconcile(root, day=D):
    return _unit_body(_note(root, day), "drc-trades", "reconcile")


def _a31(root, day=D):
    return _unit_body(_note(root, day), "drc-open-items", "open_positions")


def _trade_block(root, store, symbol, day=D):
    return _unit_body(_note(root, day), "drc-trades", f"trade-{_trade_build(store, symbol, day)['ref']}")


# ---------------------------------------------------------------------
# D5-1 — THE DIFF (v2 `:80` steps 1–3), stored once, rendered from the keys
# ---------------------------------------------------------------------


def test_d5_1_the_unit_shows_the_per_seq_diff_of_a_card_with_legs_against_the_export(tmp_path):
    """D5-1: the matched card's current legs against the export, per leg seq
    (shares, price, time), with the held count after each leg on both sides;
    his tap listed as history. A dry plan (`plan_note`, nothing written) —
    the diff is the "before"."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    legs = _Legs([_eee_card()], _eee_tapped())
    plan = build.plan_note(D, deps=_deps_with(store, root, legs, [_eee_card()]), event=_record(
        store, D, trading=DAY1.read_bytes()), check=True)
    body = next(u.body for u in plan.units if (u.section, u.unit) == ("drc-trades", "reconcile")).split("\n")
    assert body != NOT_BUILT, body
    assert "EEE long 09:45:00 · card #41 · running read from legs" in body
    assert ("  seq 0 entry: DAS 15@40.0000 09:45:00 ET · Cobalt 15@40.0000 09:45:00 ET (leg #101, confirmed, "
            "sheet) — match · held after: DAS 15 · Cobalt 15") in body
    assert ("  seq 1 exit: DAS 15@40.2500 09:50:30 ET · Cobalt 7@40.1000 09:50:30 ET (leg #102, estimated, "
            "panel) — shares, price differ · held after: DAS 0 · Cobalt 8") in body
    assert "  history: leg #102 seq 1 exit 7@40.1000 09:50:30 ET panel (estimated)" in body
    assert "  adjustment not written — dry run (plan only)" in body
    assert legs.calls == []


def test_d5_1_the_diff_is_stored_once_on_build_trade_with_the_import_and_the_leg_ids_read(tmp_path):
    """D5-1 (L57): the diff is ONE key of the matched trade's
    `build_trade.derived`; its inputs name the `drc_imports` row and the leg
    ids read; the unit renders those keys only."""
    from cobalt.drc import build, units

    store = _Store()
    legs = _Legs([_eee_card()], _eee_tapped())
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    assert _reconcile(root) != NOT_BUILT, _reconcile(root)
    row = _trade_build(store, "EEE")
    rec = row["derived"]["reconcile"]
    assert rec["card_id"] == EEE_CARD
    assert [(r["seq"], r["state"]) for r in rec["before"]] == [(0, "match"), (1, "mismatch")]
    assert rec["before"][1]["fields"] == ["shares", "price"]
    assert row["inputs"]["reconcile"]["import_id"] == IMPORT_ID
    assert row["inputs"]["reconcile"]["leg_ids"] == [101, 102]
    # rendered from the stored keys alone: the same rows give the same unit
    day_row = _day_build(store)
    builds = [r for r in _rows(store) if r["kind"] == "build_trade"]
    assert units.reconcile(day_row, builds).split("\n") == _reconcile(root)
    assert build.FN_VERSION == row["fn_version"]


def test_d5_1_a_trade_with_no_matched_card_is_not_reconciled_and_says_so(tmp_path):
    store = _Store()
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), _Legs([], []), [])
    assert _reconcile(root) == ["no trade matched a card — nothing to reconcile"]


# ---------------------------------------------------------------------
# D5-2 — THE WRITES (v2 `:80` steps 4–6, S-C2), through `cards.legs` only
# ---------------------------------------------------------------------


def test_d5_2_the_event_day_build_writes_one_trading_log_correction_and_running_is_the_exports(tmp_path):
    """D5-2: ½ tapped at 40.10 for 7, the export 15 @ 40.25 → ONE
    `record_correction` of leg #102 with `source = 'trading_log'` and the
    import id, at the build's clock; the unit re-renders `adjusted to DAS: 1
    rows (#900)`; running after = the export's 0."""
    store = _Store()
    legs = _Legs([_eee_card()], _eee_tapped())
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    body = _reconcile(root)
    assert "  adjusted to DAS: 1 rows (#900)" in body, body
    assert "  running after: 0 · DAS position: 0" in body
    assert legs.calls == [("correction", 102, dict(
        shares=15, price=Decimal("40.2500"), price_source="trading_log", flag="confirmed",
        source="trading_log", source_import_id=IMPORT_ID, now=TEN_ET,
    ))]
    rec = _trade_build(store, "EEE")["derived"]["reconcile"]
    assert rec["written"] == [900] and rec["refused"] is None
    assert rec["before"][1]["state"] == "mismatch"  # the "before", kept after the write
    assert _day_build(store)["derived"]["unresolved"] == []


def test_d5_2_an_export_exit_cobalt_never_recorded_is_a_new_exit_leg_then_its_export_time(tmp_path):
    """D5-2 + D5-b: an exit in the export with no Cobalt leg → `record_exit`
    (typed, the export's shares and price, `now` = the build's clock), then ONE
    `record_correction` setting `at` to the export's time — both naming the
    import."""
    store = _Store()
    legs = _Legs([_eee_card()], _eee_tapped()[:1])
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    assert "  adjusted to DAS: 2 rows (#900, #901)" in _reconcile(root), _reconcile(root)
    (exit_call, time_call) = legs.calls
    assert exit_call == ("exit", EEE_CARD, dict(
        preset="typed", shares=15, price=Decimal("40.2500"), price_source="trading_log", price_asof=None,
        flag="confirmed", source="trading_log", running_before=15, now=TEN_ET, source_import_id=IMPORT_ID,
    ))
    assert time_call == ("correction", 900, dict(
        at=_at(9, 50, 30), source="trading_log", source_import_id=IMPORT_ID, now=TEN_ET,
    ))


def test_d5_2_a_card_with_no_legs_gets_no_entry_leg_and_its_exits_on_the_pre_c1_basis(tmp_path):
    """D5-a: a card filled before C1 has no legs; no entry leg is written
    (the entry writer carries no import id); the exit is written on the
    `shares` basis `running_shares` reads."""
    store = _Store()
    legs = _Legs([_eee_card()], [])
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    body = _reconcile(root)
    assert "  entry leg: not written — the entry writer carries no import id" in body, body
    assert "EEE long 09:45:00 · card #41 · running read from shares" in body
    assert [c[0] for c in legs.calls] == ["exit", "correction"]
    assert legs.calls[0][2]["running_before"] == 15


def test_d5_2_negative_control_the_dry_run_writes_no_leg(tmp_path, capsys):
    """D5-2 negative control (v2 `[F-09]`): `cobalt drc build --dry-run`
    calls `plan_note` alone — no write call reaches the legs door."""
    from cobalt.drc import cli

    store = _Store()
    root = _vault(tmp_path)
    legs = _Legs([_eee_card()], _eee_tapped())
    _record(store, D, trading=DAY1.read_bytes())
    cli.cmd_build(argparse.Namespace(date=D, dry_run=True, no_trades=False),
                  deps=_deps_with(store, root, legs, [_eee_card()]))
    assert "DRY RUN: nothing written" in capsys.readouterr().out
    assert legs.calls == []
    assert store.recorded == []


def test_d5_2_a_re_paired_date_stores_and_renders_the_diff_and_writes_nothing(tmp_path):
    """D5-d: `rebuild_notes` (`check=False`) never writes `legs` —
    `adjustment not written — re-paired date`."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    legs = _Legs([_eee_card()], _eee_tapped())
    _record(store, D, trading=DAY1.read_bytes())
    build.rebuild_notes([D], deps=_deps_with(store, root, legs, [_eee_card()]))
    body = _reconcile(root)
    assert "  adjustment not written — re-paired date" in body, body
    assert legs.calls == []
    assert _trade_build(store, "EEE")["derived"]["reconcile"]["before"][1]["state"] == "mismatch"


def test_d5_2_a_carried_trade_stores_and_renders_the_diff_and_writes_nothing(tmp_path, weekday_calendar):
    """D5-d: a trade with `inputs.carried_from` (the next day's DDD) is never
    written — `adjustment not written — carried trade`."""
    store = _K3Store()
    _record(store, D, trading=DAY1.read_bytes())
    rows = _ddd_flat()[:1]  # his fill only: Cobalt holds 50, the export 30
    legs = _Legs([_ddd_card()], rows)
    event = _day(store, D_NEXT, EEE_ROUND, _carried(store))
    root, _ = _built(tmp_path, store, event, legs, [_ddd_card()])
    body = _reconcile(root, D_NEXT)
    assert "  adjustment not written — carried trade" in body, body
    assert legs.calls == []


def test_d5_2_legs_that_match_the_export_write_nothing(tmp_path):
    store = _Store()
    rows = [_eee_tapped()[0], _leg(102, EEE_CARD, 1, "exit", 15, "40.2500", _at(9, 50, 30), running_before=15)]
    legs = _Legs([_eee_card()], rows)
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    assert "  legs match the export — nothing to adjust" in _reconcile(root), _reconcile(root)
    assert legs.calls == []


# ---------------------------------------------------------------------
# D5-3 — THE REFUSAL (R90): stored, rendered twice, carried, never forced
# ---------------------------------------------------------------------


def _x11(tmp_path):
    store = _K3Store(stated_days={7: D_NEXT})
    legs = _Legs([_ddd_card(state="CLOSED")], _ddd_flat(),
                 refuse={202: legs_mod.LegRefused("closed_off_zero", CLOSED_OFF_ZERO)})
    root, deps = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs,
                        [_ddd_card(state="CLOSED")])
    # every D5-3 test starts from the refusal rendered on the event day
    assert f"unresolved: card 42 — {CLOSED_OFF_ZERO}" in _reconcile(root), _reconcile(root)
    return store, legs, root, deps


def test_d5_3_x11_a_refusal_is_stored_rendered_in_both_units_and_the_drc_is_built(tmp_path, weekday_calendar):
    """D5-3 / R90 (X11's shape): his flat tap closed the card on 50, the
    export shows 20 out → the correction is refused (`closed_off_zero`); the
    build does not fail, does not retry, stores the unresolved item (card id,
    leg ids, the export rows, the refusal and its code verbatim) and renders
    `unresolved: card 42 — <refusal>` in the reconcile unit AND in A31."""
    store, legs, root, _ = _x11(tmp_path)
    line = f"unresolved: card 42 — {CLOSED_OFF_ZERO}"
    assert line in _reconcile(root), _reconcile(root)
    assert line in _a31(root), _a31(root)
    assert legs.calls == [("correction", 202, dict(
        shares=20, flag="confirmed", source="trading_log", source_import_id=IMPORT_ID, now=TEN_ET,
    ))]  # tried once, refused, never retried in another shape
    (item,) = _day_build(store)["derived"]["unresolved"]
    assert (item["card_id"], item["code"], item["refusal"]) == (DDD_CARD, "closed_off_zero", CLOSED_OFF_ZERO)
    assert item["trade_id"] == _trade_build(store, "DDD")["ref"] and item["since"] == D.isoformat()
    assert item["leg_ids"] == [201, 202]
    assert [r["seq"] for r in item["export_rows"]] == [0, 1]
    # the DRC book keeps the position OPEN as the export shows it (no CLOSED→open edge)
    assert _unit_body(_note(root), "drc-trades", "open_positions")[1].startswith("DDD · long · 30 · ")


def test_d5_3_the_unresolved_line_is_carried_on_the_next_days_build(tmp_path, weekday_calendar):
    store, legs, root, deps = _x11(tmp_path)
    from cobalt.drc import build

    build.run_drc_build(_day(store, D_NEXT, EEE_ROUND, _carried(store)), deps=deps)
    line = f"unresolved: card 42 — {CLOSED_OFF_ZERO}"
    assert line in _reconcile(root, D_NEXT), _reconcile(root, D_NEXT)
    assert line in _a31(root, D_NEXT)
    (item,) = _day_build(store, D_NEXT)["derived"]["unresolved"]
    assert item["since"] == D.isoformat()
    assert len([c for c in legs.calls if c[0] == "correction"]) == 1  # the carried trade wrote nothing


def test_d5_3_a_current_resolve_row_for_that_trade_clears_the_line(tmp_path, weekday_calendar):
    """D5-3: RESOLVED by a current `drc_stated_books` `resolve` row naming
    the trade (K3-7's RESOLVE): the next day's build no longer carries it."""
    store, legs, root, deps = _x11(tmp_path)
    from cobalt.drc import build

    tid = _trade_build(store, "DDD")["ref"]
    seed = _carried(store, resolves=[ResolveInput(id=7, resolve=StatedResolve(trade_id=tid))])
    build.run_drc_build(_day(store, D_NEXT, EEE_ROUND, seed), deps=deps)
    assert not any(l.startswith("unresolved:") for l in _reconcile(root, D_NEXT)), _reconcile(root, D_NEXT)
    assert not any(l.startswith("unresolved:") for l in _a31(root, D_NEXT))
    assert _day_build(store, D_NEXT)["derived"]["unresolved"] == []


def test_d5_3_a_restated_resolve_does_not_clear_the_line(tmp_path, weekday_calendar):
    """Negative control: resolve #7 superseded (not current) → still carried."""
    store, legs, root, deps = _x11(tmp_path)
    store.superseded = {7}
    from cobalt.drc import build

    tid = _trade_build(store, "DDD")["ref"]
    seed = _carried(store, resolves=[ResolveInput(id=7, resolve=StatedResolve(trade_id=tid))])
    build.run_drc_build(_day(store, D_NEXT, EEE_ROUND, seed), deps=deps)
    assert f"unresolved: card 42 — {CLOSED_OFF_ZERO}" in _reconcile(root, D_NEXT), _reconcile(root, D_NEXT)


def test_d5_3_a_later_successful_reconcile_of_the_card_clears_the_line(tmp_path, weekday_calendar):
    """D5-3: RESOLVED when a later reconcile of that card succeeds — the same
    day re-built by its event once the writer accepts."""
    store, legs, root, deps = _x11(tmp_path)
    from cobalt.drc import build

    legs.refuse.clear()
    build.run_drc_build(build.event_of(D, store), deps=deps)
    assert not any(l.startswith("unresolved:") for l in _reconcile(root)), _reconcile(root)
    assert _day_build(store)["derived"]["unresolved"] == []


def test_d5_3_a_cobalt_leg_with_no_export_execution_is_unresolved_no_writer_removes_a_leg(tmp_path):
    """D5-c: his extra tap (seq 2) has no execution in the export → no write
    is tried; stored and rendered as an unresolved item."""
    store = _Store()
    rows = [
        _leg(201, DDD_CARD, 0, "entry", 50, "30.1000", _at(10, 0), stop="29.90"),
        _leg(202, DDD_CARD, 1, "exit", 20, "30.5000", _at(10, 30), stop="29.90"),
        _leg(203, DDD_CARD, 2, "exit", 10, "30.6000", _at(10, 40), source="panel", flag="estimated",
             stop="29.90"),
    ]
    legs = _Legs([_ddd_card()], rows)
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_ddd_card()])
    line = "unresolved: card 42 — no writer removes a leg — Cobalt leg #203 (seq 2) has no DAS execution"
    assert line in _reconcile(root), _reconcile(root)
    assert legs.calls == []
    (item,) = _day_build(store)["derived"]["unresolved"]
    assert item["code"] == "no_writer"


def test_d5_3_a_matched_card_the_legs_read_cannot_find_is_unresolved_and_the_drc_is_built(tmp_path):
    """D5-3 / L1 (found at E3, `test_drc_build_db.py`'s constructed card): the
    card D3 matched has no `aset_sizings` row for the legs read → no write,
    an unresolved item with the read's words; the build is not failed."""
    store = _Store()
    legs = _Legs([], [])
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    line = "unresolved: card 41 — no aset_sizings row with id 41"
    assert line in _reconcile(root), _reconcile(root)
    assert "  legs: not read — no aset_sizings row with id 41" in _reconcile(root)
    assert legs.calls == []
    (item,) = _day_build(store)["derived"]["unresolved"]
    assert item["code"] == "card_state"


def test_d5_3_the_page_offers_resolve_beside_the_unresolved_line():
    """D5-3: `/drc` lists the unresolved line with K3-7's RESOLVE form for
    that trade (the one resolve path, L3)."""
    from cobalt.aset import drc_page
    from cobalt.drc.imports import DayView

    line = f"unresolved: card 42 — {CLOSED_OFF_ZERO}"
    view = DayView(date=D_NEXT, carried=["DDD-long-x"], status_line="READY",
                   unresolved=[{"line": line, "trade_id": "DDD-long-x", "resolve": True}])
    page = drc_page.render(view)
    assert "UNRESOLVED" in page and "CLOSED has no way back" in page, page[-800:]
    block = page.split("UNRESOLVED", 1)[1]
    assert 'action="/drc/resolve"' in block and 'value="DDD-long-x"' in block


# ---------------------------------------------------------------------
# D5-4 — REALIZED R (`[F-19]`): `legs.realized_r` over the post-reconcile legs
# ---------------------------------------------------------------------


def _r_line(block):
    return next(l for l in block if l.startswith("  - R: "))


def test_d5_4_realized_r_is_computed_over_the_post_reconcile_current_legs(tmp_path):
    """D5-4: after the correction the exit is 15 @ 40.25 (confirmed) against
    the entry 15 @ 40.00 / stop in force 39.90 → (0.25 × 15) / (15 × 0.10) =
    2.5 R; stored with `realized_r.1` and its inputs."""
    store = _Store()
    legs = _Legs([_eee_card()], _eee_tapped())
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    line = _r_line(_trade_block(root, store, "EEE"))
    assert line.endswith("· realized 2.50R (realized_r.1)"), line
    row = _trade_build(store, "EEE")
    r = row["derived"]["realized_r"]
    assert r["function_id"] == "realized_r.1" and Decimal(r["value"]) == Decimal("2.5")
    assert r["provisional"] is False and r["reason"] is None
    assert row["inputs"]["realized_r"]["fn_version"] == "realized_r.1"
    assert [l["id"] for l in row["inputs"]["realized_r"]["legs"]] == [101, 900]


def test_d5_4_an_estimated_leg_left_makes_it_provisional(tmp_path):
    """D5-4: provisional while any current leg is estimated, as `realized_r`
    returns it — a re-paired date writes nothing, so his estimated tap stays."""
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    legs = _Legs([_eee_card()], _eee_tapped())
    _record(store, D, trading=DAY1.read_bytes())
    build.rebuild_notes([D], deps=_deps_with(store, root, legs, [_eee_card()]))
    line = _r_line(_trade_block(root, store, "EEE"))
    assert line.endswith("· realized 0.47R (realized_r.1, provisional)"), line


@pytest.mark.parametrize("case, expected", [
    ("no card", "not computed — no matched card"),
    ("no legs", "not computed — the card has no legs"),
])
def test_d5_4_not_computed_says_why(tmp_path, case, expected):
    from cobalt.drc import build

    store = _Store()
    root = _vault(tmp_path)
    cards = [] if case == "no card" else [_eee_card()]
    _record(store, D, trading=DAY1.read_bytes())
    build.rebuild_notes([D], deps=_deps_with(store, root, _Legs(cards, []), cards))
    line = _r_line(_trade_block(root, store, "EEE"))
    assert line.endswith(f"· realized {expected}"), line


def test_d5_4_a_refused_reconcile_is_not_computed(tmp_path, weekday_calendar):
    store, _, root, _ = _x11(tmp_path)
    line = _r_line(_trade_block(root, store, "DDD"))
    assert line.endswith("· realized not computed — the reconcile was refused (card 42)"), line


# ---------------------------------------------------------------------
# the check (`reports/drc-d5-check-2026-10-04.md`)
# ---------------------------------------------------------------------


def test_check_o1_a_re_paired_date_keeps_its_stored_unresolved_item(tmp_path, weekday_calendar):
    """Check O1 (D5-3 / X3; build DECISION 4; card 39 row O1): K2's re-pair
    deletes every `drc_rows` kind of the day (`store.py:935`), the build rows
    with them; the re-paired build (`check=False`) writes nothing, so it
    cannot re-derive the refusal. The fixed store keeps the day's open items
    on the re-written `day` row (`derived["unresolved"]`); the re-paired
    build reads them as this day's (`same_day`)."""
    from cobalt.drc import build

    store, legs, root, deps = _x11(tmp_path)
    kept = _day_build(store)["derived"]["unresolved"]
    store.build.pop(D)  # K2's re-pair: the day's rows deleted, then re-recorded
    _record(store, D, trading=DAY1.read_bytes(), extra={"unresolved": kept})  # what the fixed store keeps
    build.rebuild_notes([D], deps=deps)
    line = f"unresolved: card 42 — {CLOSED_OFF_ZERO}"
    assert line in _reconcile(root), _reconcile(root)
    assert line in _a31(root), _a31(root)
    assert "  adjustment not written — re-paired date" in _reconcile(root)
    assert _day_build(store)["derived"]["unresolved"] == kept
    assert len([c for c in legs.calls if c[0] == "correction"]) == 1  # the re-paired build wrote nothing


def test_check_o1_the_kept_item_clears_by_a_later_successful_reconcile_of_the_card(tmp_path, weekday_calendar):
    """Row O1 (X2): a kept item clears only as an item of the day does — here
    by the event's build of the card succeeding once the writer accepts."""
    from cobalt.drc import build

    store, legs, root, deps = _x11(tmp_path)
    kept = _day_build(store)["derived"]["unresolved"]
    store.build.pop(D)
    _record(store, D, trading=DAY1.read_bytes(), extra={"unresolved": kept})
    legs.refuse.clear()
    build.run_drc_build(build.event_of(D, store), deps=deps)
    assert not any(l.startswith("unresolved:") for l in _reconcile(root)), _reconcile(root)
    assert _day_build(store)["derived"]["unresolved"] == []


def test_check_o1_a_stored_build_day_is_read_before_the_day_rows_kept_list(tmp_path, weekday_calendar):
    """Row O1, one home: once the day's `build_day` is recorded again, the
    build reads that row, never the `day` row's kept list."""
    from cobalt.drc import build

    store, legs, root, deps = _x11(tmp_path)
    stale = [dict(_day_build(store)["derived"]["unresolved"][0], refusal="constructed stale item")]
    _record(store, D, trading=DAY1.read_bytes(), extra={"unresolved": stale})  # build_day still stored
    build.rebuild_notes([D], deps=deps)
    assert not any("constructed stale item" in l for l in _reconcile(root)), _reconcile(root)
    assert f"unresolved: card 42 — {CLOSED_OFF_ZERO}" in _reconcile(root), _reconcile(root)


def test_check_b2_a_write_then_a_refusal_says_both_on_the_status_line(tmp_path):
    """Row B2 (check B2's second half; `## OPEN` B2 wording): the entry
    correction lands (#900), then leg #102's correction is refused → the
    status reads `adjusted to DAS: 1 rows (#900) — then refused: <text>`.
    Nothing here asserts running = the export (that would be forcing, D5-3)."""
    store = _Store()
    rows = [_leg(101, EEE_CARD, 0, "entry", 15, "40.0500", _at(9, 45)), _eee_tapped()[1]]
    legs = _Legs([_eee_card()], rows,
                 refuse={102: legs_mod.LegRefused("stopped", "REFUSED card 41: exit correction stopped")})
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_eee_card()])
    body = _reconcile(root)
    assert "  adjusted to DAS: 1 rows (#900) — then refused: REFUSED card 41: exit correction stopped" in body, body
    assert [c[1] for c in legs.calls] == [101, 102]


def test_check_own_o1_a_later_day_carries_the_item_a_re_paired_unrebuilt_prior_kept(tmp_path, weekday_calendar):
    """Check (drc-d5-o1-b2) O1, row O1 / D5-3: a re-paired D whose rebuild has
    not run holds its item on its `day` row only; the first build of D_NEXT
    still carries it (`_unresolved`'s `carried_in`)."""
    from cobalt.drc import build

    store, legs, root, deps = _x11(tmp_path)
    kept = _day_build(store)["derived"]["unresolved"]
    store.build.pop(D)  # K2's re-pair deleted D's build rows; D's rebuild has not run
    _record(store, D, trading=DAY1.read_bytes(), extra={"unresolved": kept})  # what the fixed store keeps
    build.run_drc_build(_day(store, D_NEXT, EEE_ROUND, _carried(store)), deps=deps)
    line = f"unresolved: card 42 — {CLOSED_OFF_ZERO}"
    assert line in _reconcile(root, D_NEXT), _reconcile(root, D_NEXT)


def test_check_own_o2_the_page_lists_the_item_a_re_paired_unrebuilt_day_kept(tmp_path, weekday_calendar):
    """Check (drc-d5-o1-b2) O2, row O1 / D5-3: while a re-paired D is not
    rebuilt, the `/drc` page lists the item the store kept on D's `day` row."""
    from cobalt.drc import imports

    store, legs, root, deps = _x11(tmp_path)
    kept = _day_build(store)["derived"]["unresolved"]
    store.build.pop(D)
    _record(store, D, trading=DAY1.read_bytes(), extra={"unresolved": kept})
    lines = [u.line for u in imports._unresolved_lines(store, D, None, [])]
    assert lines == [f"unresolved: card 42 — {CLOSED_OFF_ZERO}"], lines


def test_o2_an_unbuilt_day_lists_the_item_its_re_paired_unrebuilt_prior_kept(tmp_path, weekday_calendar):
    """Row O2, the prior's fallback: D_NEXT not built, its book starts from D;
    D re-paired and not rebuilt → the page lists D's kept item on D_NEXT,
    RESOLVE offered when the trade is carried in."""
    from cobalt.drc import imports

    store, legs, root, deps = _x11(tmp_path)
    kept = _day_build(store)["derived"]["unresolved"]
    store.build.pop(D)
    _record(store, D, trading=DAY1.read_bytes(), extra={"unresolved": kept})
    got = imports._unresolved_lines(store, D_NEXT, argparse.Namespace(from_day=D), [kept[0]["trade_id"]])
    assert [(u.line, u.resolve) for u in got] == [(f"unresolved: card 42 — {CLOSED_OFF_ZERO}", True)], got


def test_o2_the_page_reads_a_stored_build_day_before_the_day_rows_kept_list(tmp_path, weekday_calendar):
    """Row O2, one home: with D's `build_day` stored, the page never reads a
    list on D's `day` row."""
    from cobalt.drc import imports

    store, legs, root, deps = _x11(tmp_path)
    stale = [dict(_day_build(store)["derived"]["unresolved"][0], refusal="constructed stale item")]
    _record(store, D, trading=DAY1.read_bytes(), extra={"unresolved": stale})  # build_day still stored
    lines = [u.line for u in imports._unresolved_lines(store, D, None, [])]
    assert lines == [f"unresolved: card 42 — {CLOSED_OFF_ZERO}"], lines


def test_check_o2_two_unresolved_items_of_one_card_are_both_carried(tmp_path, weekday_calendar):
    """Check O2 (D5-3 / X3): two Cobalt legs with no DAS execution on one card
    are two unresolved items (D5-c); the next day's build carries both."""
    from cobalt.drc import build

    store = _K3Store(stated_days={7: D_NEXT})
    rows = [
        _leg(201, DDD_CARD, 0, "entry", 50, "30.1000", _at(10, 0), stop="29.90"),
        _leg(202, DDD_CARD, 1, "exit", 20, "30.5000", _at(10, 30), stop="29.90"),
        _leg(203, DDD_CARD, 2, "exit", 5, "30.6000", _at(10, 40), source="panel", flag="estimated", stop="29.90"),
        _leg(204, DDD_CARD, 3, "exit", 5, "30.7000", _at(10, 50), source="panel", flag="estimated", stop="29.90"),
    ]
    legs = _Legs([_ddd_card()], rows)
    root, deps = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_ddd_card()])
    lines = [l for l in _reconcile(root) if l.startswith("unresolved:")]
    assert len(lines) == 2, lines
    build.run_drc_build(_day(store, D_NEXT, EEE_ROUND, _carried(store)), deps=deps)
    carried = [l for l in _reconcile(root, D_NEXT) if l.startswith("unresolved:")]
    assert carried == lines, carried


def test_d5_3_second_refusal_does_not_clear_prior_unresolved():
    from datetime import date

    from cobalt.drc import reconcile

    first = {
        "card_id": 41,
        "trade_id": "T-1",
        "since": "2001-01-02",
        "code": "first",
        "refusal": "first refusal",
        "leg_ids": [101],
        "export_rows": [],
    }
    second = {
        "card_id": 41,
        "trade_id": "T-1",
        "since": "2001-01-03",
        "code": "second",
        "refusal": "second refusal",
        "leg_ids": [101],
        "export_rows": [],
    }
    applied = {
        "T-1": {
            "card_id": 41,
            "trade_id": "T-1",
            "written": [],
            "refused": {"code": "second", "text": "second refusal"},
            "items": [second],
        }
    }

    got = reconcile.unresolved(
        date(2001, 1, 3),
        carried_in=[first],
        same_day=[],
        applied=applied,
        resolved_trades=set(),
    )

    assert [(item["code"], item["since"]) for item in got] == [
        ("second", "2001-01-03"),
        ("first", "2001-01-02"),
    ]


def test_d5_3_current_resolve_clears_current_build_refusal():
    from datetime import date

    from cobalt.drc import reconcile

    item = {
        "card_id": 41,
        "trade_id": "T-1",
        "since": "2001-01-03",
        "code": "refused",
        "refusal": "writer refused",
        "leg_ids": [101],
        "export_rows": [],
    }
    applied = {
        "T-1": {
            "card_id": 41,
            "trade_id": "T-1",
            "written": [],
            "refused": {"code": "refused", "text": "writer refused"},
            "items": [item],
        }
    }

    got = reconcile.unresolved(
        date(2001, 1, 3),
        carried_in=[],
        same_day=[],
        applied=applied,
        resolved_trades={"T-1"},
    )

    assert got == []


def test_d5_4_a_no_export_leg_is_realized_over_the_current_legs_not_called_refused(tmp_path):
    """D5-4: D5-c stores an unresolved item and does not set `refused`.
    R is `realized_r` over the post-reconcile legs (provisional while the
    extra leg is estimated), not `the reconcile was refused`."""
    store = _Store()
    rows = [
        _leg(201, DDD_CARD, 0, "entry", 50, "30.1000", _at(10, 0), stop="29.90"),
        _leg(202, DDD_CARD, 1, "exit", 20, "30.5000", _at(10, 30), stop="29.90"),
        _leg(203, DDD_CARD, 2, "exit", 10, "30.6000", _at(10, 40), source="panel", flag="estimated",
             stop="29.90"),
    ]
    legs = _Legs([_ddd_card()], rows)
    root, _ = _built(tmp_path, store, _record(store, D, trading=DAY1.read_bytes()), legs, [_ddd_card()])
    line = _r_line(_trade_block(root, store, "DDD"))
    assert line.endswith("· realized 1.30R (realized_r.1, provisional)"), line
