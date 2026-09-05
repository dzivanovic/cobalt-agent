"""S1 smoke, the card half — F1 and F7 together, on cobalt_dev.

Split out of `smoke_s1.sh` because these steps SHARE CARDS: a card
created by one assertion and moved by the next has to be the same row, so
they cannot be five independent shell checks.

REPEATABLE BY CONSTRUCTION. Every row it creates is deleted in a
`finally`, so a failed run leaves the database exactly as it found it —
the S1-P2 lesson about test residue in a live table (15 stray TEST rows
made a DRC report "17 cards" when 2 were real).
"""

import sys
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parents[1] / ".env")

from cobalt.aset.engine import compute_sizing  # noqa: E402
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput  # noqa: E402
from cobalt.aset.store import AsetStore  # noqa: E402
from cobalt.cards.models import Actor, CardState, IllegalTransition, Origin  # noqa: E402
from cobalt.cards.store import CardStore  # noqa: E402
from cobalt.session import SessionBlocked, assert_writable  # noqa: E402

GREEN, RED, OFF = "\033[32m", "\033[31m", "\033[0m"
passed = failed = 0


def ok(message: str) -> None:
    global passed
    passed += 1
    print(f"  {GREEN}PASS{OFF} {message}")


def bad(message: str) -> None:
    global failed
    failed += 1
    print(f"  {RED}FAIL{OFF} {message}")


aset, cards = AsetStore(), CardStore()
aset.ensure_schema()


def make(ticker: str) -> int:
    result = compute_sizing(
        SizingInput(
            ticker=ticker, grade=Grade.B, direction=Direction.LONG,
            sheet_mode=SheetMode.HALF, risk_dollars=Decimal("30"),
            entry=Decimal("10.00"), stop=Decimal("9.50"),
        ),
        [Grade.A, Grade.B],
        Decimal("10"),
    )
    return aset.save(result)


ids: list[int] = []
try:
    # -- the full walk: four transitions after the genesis row --------
    walk = make("SMOKEW")
    ids.append(walk)
    for state in (CardState.ARMED, CardState.TRIGGERED, CardState.FILLED, CardState.CLOSED):
        cards.transition(walk, state, actor=Actor.YOU)
    history = [h["to_state"] for h in cards.history(walk)]
    expected = ["WATCH", "ARMED", "TRIGGERED", "FILLED", "CLOSED"]
    (ok if history == expected else bad)(
        f"manual card walked WATCH->ARMED->TRIGGERED->FILLED->CLOSED — "
        f"{len(history) - 1} transition rows + genesis: {history}"
    )

    # -- one click on a manual card writes the three it is missing ----
    quick = make("SMOKEF")
    ids.append(quick)
    written = cards.fill(quick, actor=Actor.YOU, reason="smoke one-click")
    rows = cards.history(quick)[1:]
    auto = [h for h in rows if (h["evidence"] or {}).get("auto") == "manual_fill"]
    good = (
        len(written) == 3
        and [h["to_state"] for h in rows] == ["ARMED", "TRIGGERED", "FILLED"]
        and len(auto) == 2
        and all(h["actor"] == Actor.COBALT.value for h in auto)
        and rows[0]["at"] == rows[-1]["at"]
    )
    (ok if good else bad)(
        f"one click on a manual WATCH card wrote 3 rows "
        f"{[h['to_state'] for h in rows]}, 2 of them Cobalt's, at one timestamp"
    )

    # -- and the same click on a radar card is refused ---------------
    radar = make("SMOKER")
    ids.append(radar)
    with aset._connect() as conn:
        conn.execute(
            "UPDATE aset_sizings SET origin = %s WHERE id = %s",
            (Origin.RADAR.value, radar),
        )
    try:
        cards.fill(radar, actor=Actor.YOU)
        bad("a RADAR card was filled in one click — the shortcut must not apply")
    except IllegalTransition:
        ok("the same click on a RADAR card is refused by name")

    # -- F1: a card at 20:30 ET is refused ---------------------------
    at_2030 = datetime(2026, 9, 5, 0, 30, tzinfo=timezone.utc)     # 20:30 ET
    try:
        assert_writable("aset.card", target="SMOKE", now=at_2030)
        bad("a card at 20:30 ET was NOT refused")
    except SessionBlocked as e:
        ok(f"a card at 20:30 ET is refused — {str(e).split(chr(8212))[0].strip()}")
finally:
    with aset._connect() as conn:
        conn.execute("DELETE FROM card_stop_edits WHERE card_id = ANY(%s)", (ids,))
        conn.execute("DELETE FROM card_transitions WHERE card_id = ANY(%s)", (ids,))
        conn.execute("DELETE FROM aset_sizings WHERE id = ANY(%s)", (ids,))
    print(f"  (cleaned up {len(ids)} smoke card(s) — this script leaves no residue)")

sys.exit(1 if failed else 0)
