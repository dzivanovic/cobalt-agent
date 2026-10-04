"""DRC K3 — the first-gate experiments X11, X13, X14, X15 (v3 `## First-gate
experiments (L70)`, `docs/30 - Design/DRC-OVERNIGHT-POSITION-v3-2026-09-24.md`
`:327`, `:334`–`:336`), run BEFORE any K3 `src/` edit (card `01-drc-k3-card.md`
row X).

A RUN row: every test here ASSERTS NOTHING. Each prints what it observed
(`-rP` shows it) and the report quotes it; a design-changing result is a
`DECISION X<n>` in the report, never fixed here. Run once on the BASE and
once after the rows are built (the PASS halves then show the built
behaviour).

X13 and X15 run in `tmp_path` vaults (the card's `## RECORDS`: the dev
vault is read only; its proof is the desk's step after the check). The
with-DB halves of X7 / X11 are K2's own tests, re-run by node id
(`test_drc_k2_experiments.py`), not copied. Constructed 2001 dates and
symbols only (L32 / L45); `template_shape.md` is copied in Python, never
opened for write.
"""

from __future__ import annotations

import re
from pathlib import Path

from test_drc_build import SHAPE, TEN_ET, _deps, _note, _outside_sections, _record, _Store, _vault
from test_drc_store import D, D_NEXT, DAY1, weekday_calendar  # noqa: F401 — fixture used by name
from test_replay_line import MemoryWriteStore

SRC = Path(__file__).resolve().parents[2] / "src" / "cobalt" / "drc"


def _say(x: str, **facts) -> None:
    for key, value in facts.items():
        print(f"{x} · {key}: {value}")


def _copy(tmp_path: Path, day=D) -> Path:
    """A `tmp_path` note: his template's SHAPE with the date token replaced
    (the build's own renderer), copied in Python."""
    from cobalt.drc import template

    path = tmp_path / "vault" / "1 - Trading" / "5 - Review" / f"DRC-{day.isoformat()}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(template.render_template(SHAPE.read_text(), day))
    return path


def _writer(store):
    from cobalt.vaultwrite import VaultWriter

    return VaultWriter("drc.build", store=store, now=lambda: TEN_ET)


# ---------------------------------------------------------------------
# X11 — v3 `:327`
# ---------------------------------------------------------------------


def test_x11_run_a_resolve_with_no_exit_price_and_the_page_action(weekday_calendar):
    """X11 (v3 `:327`): "A resolve with no exit price on a carried trade:
    CLOSED, `legs = []`, realized `not computed — exit not in any export`, no
    `IndexError` at `pairing.py:97`. Also gates K3." Design-changing: "an
    exception → the resolved trade is not built through `_trade`".
    GATE: K2's offline X11 test, called as it is. PASS half: the page's
    `imports.resolve` exists (K3-7)."""
    import test_drc_k2_experiments as k2
    from cobalt.drc import imports

    try:
        k2.test_x11_pass_a_resolve_with_no_exit_price_closes_the_carried_trade_offline()
        gate = "K2's offline X11 test green (CLOSED, legs [], the literal, no exception)"
    except Exception as e:  # noqa: BLE001 — a RUN reports, it asserts nothing
        gate = f"K2's offline X11 test raised {type(e).__name__}: {e}"
    _say("X11", gate=gate, page_action=f"imports.resolve present: {hasattr(imports, 'resolve')}")


# ---------------------------------------------------------------------
# X13 — v3 `:334`
# ---------------------------------------------------------------------


def test_x13_run_an_older_unit_after_put_back_is_a_sync_revert(tmp_path, weekday_calendar):
    """X13 (v3 `:334`): "After a green X7, put an older `unit_after` of
    `drc-trades/open_positions` back on disk (the Sync-revert shape, L28);
    run the next build: the seed hash still matches the database rows,
    `sync_revert_of` recorded, the unit rewritten from the rows unless he
    changed a line." Design-changing: "any reader using the unit text as the
    next day's book → that reverse parse is removed; the hash design
    changes". (X7 is K2's with-DB test, re-run by node id.)"""
    from cobalt.drc import build
    from cobalt.vaultwrite.markers import find_section

    # GATE: the writer alone — v1, v2, v1 put back, v3.
    store = MemoryWriteStore()
    path = _copy(tmp_path / "gate")
    w = _writer(store)
    w.upsert_unit(path, "drc-trades", "tickers", "trades: 1")
    w.upsert_unit(path, "drc-trades", "open_positions", "left open: 1 — v1")
    v1 = path.read_text()
    w.upsert_unit(path, "drc-trades", "open_positions", "left open: 1 — v2")
    path.write_text(v1)
    third = w.upsert_unit(path, "drc-trades", "open_positions", "left open: 1 — v3")
    lines = path.read_text().split("\n")
    body = find_section(lines, "drc-trades").units["open_positions"].body(lines)
    v1_id = next(r["id"] for r in store.rows if r["unit_after"] == "left open: 1 — v1")
    _say("X13 gate", v1_write_id=v1_id, last_row_sync_revert_of=store.rows[-1].get("sync_revert_of"),
         action=third.action, body_on_disk=body, overrides=len(store.overrides))

    # The reader proof: no DRC reader of the book reads a note.
    for name in ("store.py", "pairing.py"):
        hits = [f"{name}:{i}: {l.strip()}" for i, l in enumerate((SRC / name).read_text().split("\n"), 1)
                if "open_positions" in l and re.search(r"read_text|note|vault", l)]
        _say("X13 reader", file=name, note_reading_hits=hits or "none")

    # PASS half: the build's own unit. Build 1 leaves DDD open; the day is
    # re-recorded flat and built (build 2); build 1's note is put back on
    # disk (a sync bringing old bytes back); build 3 runs.
    from test_drc_k2_experiments import D_FLAT

    s = _Store()
    root = _vault(tmp_path / "pass")
    deps = _deps(s, root)
    build.run_drc_build(_record(s, D, trading=DAY1.read_bytes()), deps=deps)
    note = _note(root)
    lines = note.read_text().split("\n")
    sec = find_section(lines, "drc-trades")
    if "open_positions" not in sec.units:
        _say("X13 pass", unit="drc-trades/open_positions not built")
        return
    old = note.read_text()
    event = _record(s, D, trading=D_FLAT)
    build.run_drc_build(event, deps=deps)
    second = note.read_text()
    note.write_text(old)
    build.run_drc_build(event, deps=deps)
    rows = [r for r in deps.write_store.rows if r["unit"] == "open_positions" and r["section"] == "drc-trades"]
    lines = note.read_text().split("\n")
    _say("X13 pass", writes=len(rows), sync_revert_of=rows[-1].get("sync_revert_of"),
         first_write_id=rows[0]["id"], unit_rewritten_from_rows=note.read_text() == second,
         body=find_section(lines, "drc-trades").units["open_positions"].body(lines),
         overrides=len(deps.write_store.overrides))


# ---------------------------------------------------------------------
# X14 — v3 `:335`
# ---------------------------------------------------------------------


def test_x14_run_both_units_on_his_note_shape(tmp_path, weekday_calendar):
    """X14 (v3 `:335`): "On a copy of his note shape (no `drc-summary`, no
    `open_positions` section), upsert unit `drc-trades/open_positions` and
    unit `drc-summary/summary`." Design-changing: "the summary upsert
    refuses an absent section → the evening count is the `open_positions`
    header only, and `drc-summary/summary` leaves this lane"."""
    from cobalt.drc import build, units
    from cobalt.vaultwrite.markers import find_section

    path = _copy(tmp_path / "gate")
    w = _writer(MemoryWriteStore())
    out = {}
    for section, unit, body, placement in (
        ("drc-summary", "summary", "open overnight: 1", units.date_line_placement(D.isoformat())),
        ("drc-trades", "open_positions", "left open: 1", build.TRADES_PLACEMENT),
    ):
        try:
            r = w.upsert_unit(path, section, unit, body, placement=placement)
            out[f"{section}/{unit}"] = f"{r.action} {r.notes or ''}".strip()
        except Exception as e:  # noqa: BLE001
            out[f"{section}/{unit}"] = f"REFUSED {type(e).__name__}: {e}"
    lines = path.read_text().split("\n")
    summary_at = lines.index("<!-- cobalt:section drc-summary -->")
    trades_at = lines.index("<!-- cobalt:section drc-trades -->")
    _say("X14 gate", **out, summary_under=lines[summary_at - 1], trades_under=lines[trades_at - 1])

    s = _Store()
    root = _vault(tmp_path / "pass")
    build.run_drc_build(_record(s, D, trading=DAY1.read_bytes()), deps=_deps(s, root))
    lines = _note(root).read_text().split("\n")
    summary = find_section(lines, "drc-summary").units["summary"].body(lines)
    trades = find_section(lines, "drc-trades")
    _say("X14 pass", summary_open_overnight=[l for l in summary if l.startswith("open overnight")] or "absent",
         open_positions_unit="open_positions" in trades.units,
         trades_under=lines[trades.open_line - 1])


# ---------------------------------------------------------------------
# X15 — v3 `:336`
# ---------------------------------------------------------------------


def test_x15_run_the_two_new_units_and_his_text_byte_identical(tmp_path, weekday_calendar):
    """X15 (v3 `:336`): "Dev vault: unit bytes under their heading, his text
    byte-identical (v2 E3 shape)." Design-changing: "his text changed → K3's
    unit write is wrong". In a `tmp_path` vault (the card's `## RECORDS`)."""
    from cobalt.drc import build, units
    from cobalt.vaultwrite import Placement

    path = _copy(tmp_path / "gate")
    his = path.read_text()
    w = _writer(MemoryWriteStore())
    w.upsert_unit(path, "drc-trades", "open_positions", "left open: 1", placement=build.TRADES_PLACEMENT)
    w.upsert_unit(path, "drc-open-items", "open_positions", "open items carried forward — open positions: 1",
                  placement=Placement("after the drc-trades section", units._after_section("drc-trades")))
    after = path.read_text()
    expected = his.split("\n")
    outside = _outside_sections(after)
    lines = after.split("\n")
    _say("X15 gate", his_lines_identical=outside[: len(expected)] == expected, tail=outside[len(expected):],
         open_items_after_trades=lines.index("<!-- cobalt:section drc-open-items -->")
         == lines.index("<!-- /cobalt:section drc-trades -->") + 1)

    s = _Store()
    root = _vault(tmp_path / "pass")
    event = _record(s, D, trading=DAY1.read_bytes())
    deps = _deps(s, root)
    build.run_drc_build(event, deps=deps)
    first = _note(root).read_text()
    rows = len(deps.write_store.rows)
    build.run_drc_build(event, deps=deps)
    second = _note(root).read_text()
    expected = SHAPE.read_text().replace("{{date:YYYY-MM-DD}}", D.isoformat()).split("\n")
    outside = _outside_sections(second)
    _say("X15 pass", open_items_section="<!-- cobalt:section drc-open-items -->" in second,
         his_lines_identical=outside[: len(expected)] == expected, tail=outside[len(expected):],
         second_build_identical=second == first, rows_written_by_second=len(deps.write_store.rows) - rows)
