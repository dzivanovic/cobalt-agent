"""The desk refresh rules in prompts/CTO-DESK-WAKEUP.md (card 2026-10-13 458 W1; his 2026-10-13 R1323).

Reads the real wake-up: the four new texts once each, the two replaced texts gone, the STATE line
directly after the OWED paragraph, the 3a line directly after STEP 0 item 3, and the `- LAUNCH`
line byte for byte the BASE line (`git show <BASE>:`). Nothing is written.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WAKEUP = REPO / "docs" / "40 - DevDocs" / "prompts" / "CTO-DESK-WAKEUP.md"
BASE = "f7d71571"

SIZE = (
    "the Stop hook (ops/desk/stop-guard.py, card 458) prints DESK SIZE <n> / 300,000 after every "
    "turn; MEASURE by hand only at READ 7."
)
ORDER = (
    "at 300,000 or more the hook prints REFRESH NOW: run it the same turn, nothing first; one turn "
    "or 10 minutes later the hook sends WRITE HANDOVER NOW and the refresh runs without you."
)
STATE = (
    "STATE (card 458): §5 CURRENT carries the line STATE AT <hh:mm> (ET) directly under the OWED "
    "block, rewritten with §5 every turn; on UPDATE §5 CURRENT NOW, update §5 and the stamp before "
    "anything else."
)
FORCED = (
    "3a. Last line HANDOVER: FORCED — no line from <p>; successor reconciles → you are <p>'s "
    "successor; the refresh ended <p> (still in LIST → claude stop <p> and claude rm <p>, each "
    "alone); the pane id is §5 CURRENT's; READ 8 RECONCILE (card 458) before the plate."
)
RECONCILE = (
    " RECONCILE (card 458): LIST and herdr pane list against §5 CURRENT's table and OWED block; a "
    "live session or pane the table lacks, a row whose session is gone, a watch no pgrep -fl "
    "\"wait-stop-line.sh|desk-watch.sh\" line carries → re-arm the watch from the row's watch cell; "
    "one §4 row per difference."
)


def lines() -> list[str]:
    return WAKEUP.read_text(encoding="utf-8").splitlines()


def test_w1_each_new_text_occurs_once():
    text = WAKEUP.read_text(encoding="utf-8")
    for part in (SIZE, ORDER, STATE, FORCED, RECONCILE):
        assert text.count(part) == 1, part


def test_w1_the_replaced_texts_are_gone():
    text = WAKEUP.read_text(encoding="utf-8")
    assert text.count("starts with MEASURE.") == 0
    assert text.count("at the next turn boundary, always.") == 0


def test_w1_the_state_line_follows_the_owed_paragraph():
    ls = lines()
    (i,) = [n for n, x in enumerate(ls) if x.startswith("OWED (his 10-06 R590")]
    assert ls[i + 1] == STATE


def test_w1_the_3a_line_follows_step_0_item_3():
    ls = lines()
    (i,) = [n for n, x in enumerate(ls) if x.startswith("3. No HANDOVER")]
    assert ls[i + 1] == FORCED


def test_w1_reconcile_ends_read_item_8():
    (line,) = [x for x in lines() if x.startswith("8. ACT")]
    assert line.endswith(RECONCILE)


def test_w1_the_launch_line_is_unchanged():
    (now,) = [x for x in lines() if x.startswith("- LAUNCH ")]
    base = subprocess.run(
        ["git", "-C", str(REPO), "show", f"{BASE}:docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"],
        capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    (then,) = [x for x in base if x.startswith("- LAUNCH ")]
    assert now == then
