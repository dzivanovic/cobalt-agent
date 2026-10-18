"""F23 card 503 row P7: the render on `cobalt_dev` (`requires_db`, hub-run; FINAL §5 tests 10, 11).

Radar cards are seeded through the real-shape `world` of
`test_radar_cards_db.py` (the real `CardStore.create_radar_card`, F-14) and
one manual card through the sheet's own `AsetStore.save`, all inside the
suite's rolled-back transaction. `world` applies `0022` inside that
transaction, so this file runs in PASS 2 (`ops/desk/gate-lists.md`). Tickers
are constructed (L32). The vault is a synthetic `tmp_path` folder whose two
notes carry the seeded cards' slugs.

`cobalt_dev` may hold other radar rows; the assertions name only the cards
seeded here.
"""

from __future__ import annotations

import os
import sys
from datetime import timedelta
from decimal import Decimal

import pytest

from test_playbook_offline import RUN_DATE, _slide_text, _slides, _table_slides, make_vault, note_text
from test_radar_cards_db import ENABLED, SCAN0, TICKER, world  # noqa: F401 — the with-DB fixture

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]

OTHER_SLUG = "example-playbook-other"
MANUAL_TICKER = "ZZPM"


def _seed(world) -> dict[str, int]:
    """Two slugs, mixed states, plus one manual card."""
    from cobalt.aset.engine import compute_sizing
    from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
    from cobalt.aset.store import AsetStore
    from cobalt.cards import Actor, CardState
    from cobalt.cards.radar import RadarCardSpec

    first = world["scan"](SCAN0)
    watch_id = first.created[0]
    cards = world["cards"]
    with cards._connect() as conn:
        row = conn.execute(
            "SELECT pool_member_id, direction, trade_def_md5, radar_score_id FROM aset_sizings WHERE id = %s",
            (watch_id,),
        ).fetchone()
    other = RadarCardSpec(
        ticker=TICKER, direction=row[1], session="RTH", pool_member_id=row[0], trade_def_slug=OTHER_SLUG,
        trade_def_md5=row[2], setup_ref="overextension", trigger_type="bar_break", trigger_price=Decimal("5.50"),
        stop_ref="snapback_candle", structural_stop=Decimal("5.81"), formed_at=SCAN0 - timedelta(minutes=5),
        expires_at=SCAN0 + timedelta(hours=1), why="synthetic other", radar_score_id=row[3], scan_id=1,
        formula_sha256="a" * 64, tunables_sha256="b" * 64, settings_sha256="c" * 64, proximity=Decimal("0.5"),
        dots=[], evidence={"run_id": first.run_id},
    )
    passed_id = cards.create_radar_card(other, proposed_key_reason=None, now=SCAN0)
    assert passed_id is not None
    cards.transition(passed_id, CardState.PASSED, actor=Actor.YOU)
    manual = compute_sizing(
        SizingInput(ticker=MANUAL_TICKER, grade=Grade.B, direction=Direction.LONG, sheet_mode=SheetMode.FULL,
                    risk_dollars=Decimal("60"), entry=Decimal("10.0000"), stop=Decimal("9.9000")),
        (Grade.A, Grade.B), Decimal("10"),
    )
    manual_id = AsetStore("cobalt_dev").save(manual)
    with cards._connect() as conn:
        slug = conn.execute("SELECT trade_def_slug FROM aset_sizings WHERE id = %s", (watch_id,)).fetchone()[0]
    return {"watch": watch_id, "passed": passed_id, "manual": manual_id, "watch_slug": slug}


def _render(monkeypatch, tmp_path, seeded) -> tuple[int, object]:
    import cobalt.cli
    import cobalt.playbook.cli  # noqa: F401 — the package the render runs

    vault = make_vault(tmp_path / "vault", {
        "Seeded": note_text(seeded["watch_slug"], "Seeded Setup", ["range_break"]),
        "Other": note_text(OTHER_SLUG, "Other Setup", ["opening_drive"]),
    })
    monkeypatch.setenv("COBALT_VAULT_PATH", str(vault))
    out = tmp_path / "out"
    monkeypatch.setattr(sys, "argv", ["cobalt", "playbook", "render", "--date", RUN_DATE, "--out", str(out)])
    try:
        cobalt.cli.main()
    except SystemExit as e:
        return e.code, out
    return 0, out


def test_render_reads_radar_cards_grouped_and_skips_manual(world, monkeypatch, tmp_path):
    seeded = _seed(world)
    code, out = _render(monkeypatch, tmp_path, seeded)
    assert code == 0
    folder = out / RUN_DATE
    tickers = {}
    for deck in sorted(folder.glob("*.pptx")):
        tickers[deck.stem] = [(r[1], r[2], r[4]) for t in _table_slides(deck) for r in t]
    assert ("ZZPB", "Seeded Setup", "WATCH") in tickers["range_break"]
    assert ("ZZPB", "Other Setup", "PASSED") in tickers["opening_drive"]
    assert all(row[1] == "Seeded Setup" for row in tickers["range_break"])
    assert all(row[1] == "Other Setup" for row in tickers["opening_drive"])
    for name, rows in tickers.items():
        assert MANUAL_TICKER not in [r[0] for r in rows], f"a manual card reached {name}.pptx"
    assert "range_break" in _slide_text(_slides(folder / "range_break.pptx")[0])


def test_job_run_stamps_a_done_row(world, monkeypatch, tmp_path):
    from cobalt.jobs.store import JobStore

    code, _out = _render(monkeypatch, tmp_path, _seed(world))
    assert code == 0
    row = JobStore().get("com.cobalt.playbook")
    assert row is not None
    assert (row["state"], row["exit_code"]) == ("done", 0)
    assert row["last_result"]["families"]["range_break"]["cards"] >= 1
