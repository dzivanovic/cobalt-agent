"""DRC D3 — THE BUILD, WITH-DB half (`prompts/2026-09-28/10-drc-d3-build.md`
`## E3`): the real `run_drc_build` behind D2's route — the event, the rows
K1 / K2 recorded, `record_build`'s two kinds, the re-paired days, E8 on the
real rows, E11 on the real build, the no-trade DRC on both day types.

The DRC harness is reused BY IMPORT, never copied: `test_drc_store.py`'s
`migrated` / `weekday_calendar` / `requires_db` / `D` / `D_NEXT`,
`test_drc_k1_store.py`'s `TEN_ET` / `_state`, `test_drc_imports_db.py`'s
`lane` / `_drop` / `_page`, `test_drc_k2_experiments.py`'s constructed
days. Everything runs inside `test_drc_store.py`'s never-committed migration
transaction on `cobalt_dev` (L76): `0016` / `0018` / `0019` / `0020` are
applied only there. Constructed 2001 dates and symbols only (L32 / L45);
every note lands in the lane's `tmp_path` vault, whose template is the
shape fixture. The deps the build reads OUTSIDE the DRC rows (the cards,
the settings, the rules, the replay row) are constructed here; the store
and the audit store are the real ones.
"""

from __future__ import annotations

import functools
import os
import sys
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.drc.store import DrcStore

from test_drc_imports_db import _drop, _page, lane  # noqa: F401 — fixtures are used by name
from test_drc_k1_store import TEN_ET, _state
from test_drc_k2_experiments import EEE_ROUND
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    E1,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)

FIXTURES = Path(__file__).resolve().parent.parent / "fixtures" / "drc"
REVIEW = "1 - Trading/5 - Review"


class _Settings:
    def __init__(self):
        from cobalt.settings.models import DrcGoalSettings, DrcLimitsSettings, DrcWindowsSettings

        self.limits = DrcLimitsSettings(card_match_window_minutes=30)
        self.windows = DrcWindowsSettings()
        self.goal = DrcGoalSettings()


CARD = dict(
    id=41, created_at=datetime(2001, 1, 2, 15, 10, tzinfo=timezone.utc), session="rth", account_mode="live",
    ticker="AAA", grade="A", direction="long", sheet_mode="full", risk_budget=Decimal("60"),
    entry=Decimal("50.2"), stop=Decimal("49.9"), per_share_risk=Decimal("0.3"), shares=200,
    used_risk=Decimal("60"), state="FILLED", state_at=None, status="FILLED", filled_at=None,
    actual_fill=None, recomputed_shares=None, recomputed_used_risk=None, share_delta=None,
    distance_change_pct=None,
)


@pytest.fixture
def built(lane, monkeypatch):
    """The lane with THE REAL BUILD registered (the lane keeps it absent for
    D2's own tests), his template's shape in the lane's vault, and the
    non-DRC reads constructed. The build is imported HERE, never at module
    level, so the file collects before the build exists (E3's red)."""
    import importlib

    monkeypatch.delitem(sys.modules, "cobalt.drc.build")  # the lane's `None`
    real_build = importlib.import_module("cobalt.drc.build")
    cards: list[dict] = []
    root = Path(os.environ["COBALT_VAULT_PATH"])
    (root / "5 - Templates").mkdir(parents=True, exist_ok=True)
    (root / "5 - Templates" / "DRC.md").write_text((FIXTURES / "template_shape.md").read_text())
    (root / "1 - Trading" / "4 - Strategies").mkdir(parents=True, exist_ok=True)
    monkeypatch.setattr(real_build, "default_deps", functools.partial(
        real_build.default_deps,
        cards=lambda day: [c for c in cards if c["created_at"].date() == day],
        card_counts=lambda day: (len(cards), len(cards)),
        drc_settings=lambda: _Settings(),
        daily_stop=lambda: {"full": None, "half": None},
        risk_parameters=lambda day_cards: "no sheet-mode cards today",
        rules_block=lambda: "- [ ] constructed rule one #process",
        daily_note=lambda day: None,
        replay_result=lambda: None,
        now=lambda: TEN_ET,
    ))
    return root, cards, real_build


def _note(root: Path, day: date) -> Path:
    return root / REVIEW / f"DRC-{day.isoformat()}.md"


def _build_rows(conn, day: date):
    return conn.execute(
        'SELECT id, kind, ref, inputs, derived, fn_version FROM "user".drc_rows '
        "WHERE day = %s AND kind IN ('build_trade', 'build_day') ORDER BY kind, ref",
        (day,),
    ).fetchall()


def _event(conn, day: date):
    return conn.execute(
        'SELECT state, error, note_path FROM "user".drc_events WHERE day = %s ORDER BY id DESC LIMIT 1', (day,)
    ).fetchone()


# ---------------------------------------------------------------------
# the build behind D2's route
# ---------------------------------------------------------------------


@requires_db
def test_a_placed_day_builds_the_note_and_its_build_rows(built, migrated):
    """A day dropped through D2's `place()` (flat stated) → `run_drc_build`
    writes the note in the `tmp_path` vault and `build_trade` /
    `build_day` rows with `inputs` + `fn_version`; the event is `done`
    with the note path — only after the note write."""
    root, cards, _ = built
    cards.append(dict(CARD))
    _state(D)
    result = _drop(D, E1.read_bytes(), STATS.read_bytes())
    note = _note(root, D)
    assert result.status_line == f"READY → DRC built: {note}", result.status_line
    assert _event(migrated, D) == ("done", None, str(note))
    assert note.is_file() and "<!-- cobalt:section drc-summary -->" in note.read_text()
    rows = _build_rows(migrated, D)
    trades = sorted(DrcStore().event_for(D)["trades"])
    assert sorted(r[2] for r in rows if r[1] == "build_trade") == trades
    assert [r[2] for r in rows if r[1] == "build_day"] == ["build"]
    assert {r[5] for r in rows} == {"drc.build/1"}
    aaa = next(r for r in rows if r[2].startswith("AAA-"))
    assert aaa[3]["card"]["id"] == 41 and aaa[4]["card"]["card_id"] == 41


@requires_db
def test_the_card_snapshot_survives_a_later_card_change(built, migrated):
    """`[F-19]`: the stored inputs snapshot the card at build time; a later
    change to the card the build read does not move the stored rows."""
    from cobalt.drc import units

    root, cards, real_build = built
    cards.append(dict(CARD))
    _state(D)
    _drop(D, E1.read_bytes(), STATS.read_bytes())
    before = _build_rows(migrated, D)
    cards[0]["stop"] = Decimal("48.0")
    # D3 fix r2 F-7r2 (c): the change is REAL where the build reads the card
    # — a plan (writes nothing, L10) through the build's own read carries it.
    plan = real_build.plan_note(D, deps=real_build.default_deps(), event=real_build.event_of(D, DrcStore()), check=True)
    aaa_ref = next(r[2] for r in before if r[2].startswith("AAA-"))
    (unit,) = [u for u in plan.units if u.section == "drc-trades" and u.unit == f"trade-{aaa_ref}"]
    (planned,) = [line for line in unit.body.split("\n") if line.startswith("  - card: ")]
    assert f" · stop {units.money(Decimal('48.0'))} · " in planned, planned
    _snapshot_holds(migrated, root, before, Decimal("49.9"))
    aaa = next(r for r in before if r[2].startswith("AAA-"))
    assert aaa[3]["card"]["stop"] == "49.9"


def _snapshot_holds(conn, root: Path, before, stop: Decimal) -> None:
    """D3 fix r1 F-7 (`drc-d3-check-2026-09-25.md:110`, L35): the snapshot
    holds only if BOTH the stored `build_*` rows EQUAL `before` AND the
    note's `card:` line for the AAA trade still carries `stop` — a rebuild
    with the changed card moves both, so this can fail."""
    from cobalt.drc import units
    from cobalt.vaultwrite.markers import find_section

    assert _build_rows(conn, D) == before
    aaa = next(r[2] for r in before if r[2].startswith("AAA-"))
    lines = _note(root, D).read_text().split("\n")
    body = find_section(lines, "drc-trades").units[f"trade-{aaa}"].body(lines)
    (card,) = [line for line in body if line.startswith("  - card: ")]
    assert f" · stop {units.money(stop)} · " in card, card


@requires_db
def test_record_build_replaces_only_the_two_build_kinds(built, migrated):
    """`record_build` replaces `build_trade` / `build_day` for the day in
    one transaction and touches no K kind."""
    root, _, _ = built
    _state(D)
    _drop(D, E1.read_bytes(), STATS.read_bytes())
    k_rows = migrated.execute(
        "SELECT id, kind, ref FROM \"user\".drc_rows WHERE day = %s AND kind NOT IN ('build_trade', 'build_day') "
        "ORDER BY id", (D,)).fetchall()
    first = [r[0] for r in _build_rows(migrated, D)]
    DrcStore().record_build(D, [dict(kind="build_day", ref="build", inputs={}, derived={}, fn_version="drc.build/1")])
    assert [r[1:3] for r in _build_rows(migrated, D)] == [("build_day", "build")]
    assert not set(first) & {r[0] for r in _build_rows(migrated, D)}
    assert migrated.execute(
        "SELECT id, kind, ref FROM \"user\".drc_rows WHERE day = %s AND kind NOT IN ('build_trade', 'build_day') "
        "ORDER BY id", (D,)).fetchall() == k_rows
    with pytest.raises(ValueError, match="build_trade"):
        DrcStore().record_build(D, [dict(kind="trade", ref="x", inputs={}, derived={}, fn_version="drc.build/1")])


@requires_db
def test_a_re_pair_rebuilds_the_later_days_build_rows_and_note(built, migrated):
    """v3 `[F-03]` note half: the later day built first; then the earlier
    day's first file → K2 re-pairs the later day (deleting every kind of
    its rows, `build_*` included) and D3-2r re-builds its `build_*` rows
    and its note."""
    root, _, _ = built
    _state(D_NEXT)
    _drop(D_NEXT, EEE_ROUND, STATS.read_bytes())
    later_before = {r[0] for r in _build_rows(migrated, D_NEXT)}
    assert later_before
    before_text = _summary_text(root, D_NEXT)
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    ((derived,),) = migrated.execute(
        "SELECT derived FROM \"user\".drc_rows WHERE day = %s AND kind = 'day'", (D,)).fetchall()
    assert derived["repaired"] == [D_NEXT.isoformat()]
    later_after = {r[0] for r in _build_rows(migrated, D_NEXT)}
    assert later_after and not later_before & later_after
    assert _event(migrated, D)[0] == "done"
    (day_row,) = [r for r in _build_rows(migrated, D_NEXT) if r[1] == "build_day"]
    assert day_row[3]["seed"]["source"] == "carried" and day_row[3]["seed"]["from_day"] == D.isoformat()
    assert _note(root, D_NEXT).is_file()
    _note_rebuilt(root, D_NEXT, before_text, day_row)


def _summary_text(root: Path, day: date) -> str:
    from cobalt.vaultwrite.markers import find_section

    lines = _note(root, day).read_text().split("\n")
    return "\n".join(find_section(lines, "drc-summary").units["summary"].body(lines))


def _note_rebuilt(root: Path, day: date, before_text: str, day_row) -> None:
    """D3 fix r1 F-8 (`drc-d3-check-2026-09-25.md:111`, L35): the later
    day's note was REWRITTEN — its `drc-summary/summary` text differs from
    the text before the re-pair AND equals `units.summary(<the re-paired
    build_day row>)` as the note holds it (`is_file()` alone cannot fail)."""
    from cobalt.drc import units

    after = _summary_text(root, day)
    assert after != before_text
    assert after == units.summary({"inputs": day_row[3], "derived": day_row[4]})


# ---------------------------------------------------------------------
# E11 — the real build killed after `pending`
# ---------------------------------------------------------------------


@requires_db
def test_e11_an_exception_inside_the_real_build_is_failed_and_never_built(built, migrated, lane, monkeypatch):
    """E11 (v2 `:201`): "Kill the ASET request after `pending` and before
    `done`. Pass: the row is `failed` and the page is not `DRC built`." —
    on the REAL build (the note write raises)."""
    root, _, real_build = built

    def kill(*args, **kwargs):
        raise RuntimeError("constructed kill after pending")

    monkeypatch.setattr(real_build, "write_note", kill)
    _state(D)
    result = _drop(D, E1.read_bytes(), STATS.read_bytes())
    assert _event(migrated, D) == ("failed", "RuntimeError: constructed kill after pending", None)
    assert result.status_line == "DRC build FAILED: build — RuntimeError: constructed kill after pending"
    assert "DRC built" not in _page(lane, D)


# ---------------------------------------------------------------------
# the no-trade DRC — both day types (R93)
# ---------------------------------------------------------------------


@requires_db
def test_a_zero_execution_trading_log_builds_the_no_trade_drc(built, migrated):
    root, _, _ = built
    header = DAY1.read_bytes().splitlines(keepends=True)[0]
    _state(D)
    result = _drop(D, header)
    note = _note(root, D)
    assert result.status_line == f"no-trade day recorded → DRC built: {note}"
    text = note.read_text()
    assert "<!-- cobalt:unit no_trade -->" in text and "<!-- cobalt:unit voice-no-trades -->" in text
    assert "<!-- cobalt:unit trade-" not in text


@requires_db
def test_a_file_less_no_trade_day_builds_the_no_trade_drc_on_its_statement_event(built, migrated):
    """The file-less no-trade event home (SETTLED: `drc_events` via
    `imports.no_trade_event`) → the no-trade DRC from his statement."""
    from cobalt.drc import imports

    root, _, _ = built
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    result = imports.no_trade(D_NEXT, now=TEN_ET)
    note = _note(root, D_NEXT)
    assert result.status_line == f"no-trade day recorded → DRC built: {note}"
    assert _event(migrated, D_NEXT) == ("done", None, str(note))
    assert "### Why no trades today:" in note.read_text()


# ---------------------------------------------------------------------
# E8 — on the real rows
# ---------------------------------------------------------------------


@requires_db
def test_e8_on_the_real_rows_a_vanished_trade_keeps_its_voice_unit_orphaned(built, migrated):
    """E8 (v2 `:198`) through D2's route: a superseding trading log without
    CCC → CCC's derived block gone, his voice text kept, one `orphaned`
    line above it."""
    root, _, _ = built
    _state(D)
    _drop(D, E1.read_bytes(), STATS.read_bytes())
    note = _note(root, D)
    ccc = next(t for t in DrcStore().event_for(D)["trades"] if t.startswith("CCC-"))
    marker = f"<!-- cobalt:unit voice-{ccc} -->"
    note.write_text(note.read_text().replace(marker, marker + "\nmy CCC answer"))
    without = b"\n".join(l for l in E1.read_bytes().split(b"\n") if b",CCC," not in l)
    stats = b"\n".join(l for l in STATS.read_bytes().split(b"\n") if b",CCC," not in l)
    _drop(D, without, stats)
    lines = note.read_text().split("\n")
    at = lines.index(marker)
    assert lines[at + 1] == "my CCC answer"
    assert lines[at - 2] == f"orphaned — trade {ccc} is not in the current trading log"
    assert _event(migrated, D)[0] == "done"


# ---------------------------------------------------------------------
# D3-9 (09-29 R32 / R33) — the K10 guards resolve `user.drc_events`
# ---------------------------------------------------------------------


@requires_db
@pytest.mark.parametrize("check_id", ["K10.1", "K10.2"])
def test_the_k10_guards_find_drc_events_in_the_migrated_transaction(migrated, tmp_path, check_id):
    """The committed row through `checks.default_deps(prod=False)`'s read
    path inside the migration transaction: the `to_regclass('user.drc_events')`
    statement is read and answers `present = True`, so the verdict is NOT
    the guard's FAIL — EXPECTED `KNOWN` pending (no event on the
    constructed day)."""
    import dataclasses

    from cobalt.smoke import checks
    from cobalt.smoke.config import SUITES_DIR, load_suite
    from cobalt.smoke.models import Verdict

    from test_smoke import ctx

    check = {c.id: c for c in load_suite(SUITES_DIR / "s2.yaml").checks}[check_id]
    live = checks.default_deps(prod=False)
    seen = []

    def spy(statement, side):
        result = live.read_rows(statement, side)
        seen.append((statement, side, result))
        return result

    note = tmp_path / "DRC.md"
    note.write_text("")
    deps = dataclasses.replace(live, read_rows=spy, drc_note_path=lambda day: note)
    out = checks.evaluate(check, ctx(prod=False, last_trading_day=D), deps)
    guard = [s for s in seen if "to_regclass('user.drc_events')" in s[0]]
    assert len(guard) == 1, [s[0] for s in seen]
    assert guard[0][1] == "user" and guard[0][2].rows == [(True,)]
    assert not (out.verdict is Verdict.FAIL and "user.drc_events" in out.detail), out.detail
    assert out.verdict is Verdict.KNOWN, out.detail
