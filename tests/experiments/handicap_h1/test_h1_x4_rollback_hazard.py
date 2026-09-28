"""X4 (v3; grok X5 / Fable X10; `29` §7): a pool note carrying a
`handicap:` sub-block, parsed by the code AS IT STANDS — does it FREEZE
(`pool_error`, F14) or does an exception escape the reader?

Run on main's code at STEP-1 (EXPECTED: freeze) and again at STEP-2's end
under H1's code (EXPECTED: it parses).

`tests/fixtures/radar/radar-screens.real-shape.md` carries NO fenced block
at all (it is the propose-input fixture), so there is no pool block to
insert into. The experiment therefore runs on the two notes that do carry
one: the committed `radar-screens.example.md`, and a SCRATCH COPY of his
live `Radar Screens.md` — read once, never written; the copy lives in
pytest's `tmp_path`. The inserted block is this build's literals, not his.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from h1_support import VAULT, config

from cobalt.radar.notes import load_sources, parse_note_bytes

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures" / "radar"
BLOCK = (
    b"handicap:\n"
    b"  float_below_m: 20\n"
    b"  market_cap_below_m: 300\n"
    b"  factor: 0.8\n"
    b"  missing: apply\n"
    b"  mode: shadow\n"
    b"  combinator: any\n"
)


def with_handicap(payload: bytes) -> bytes:
    """`BLOCK` appended as the last key of the note's one pool block."""
    start = payload.index(b"kind: pool")
    end = payload.index(b"\n```", start)
    return payload[: end + 1] + BLOCK.rstrip(b"\n") + payload[end:]


def _notes(tmp_path):
    cfg = config()
    return {
        "example fixture": (FIXTURES / "radar-screens.example.md").read_bytes(),
        "his live note (scratch copy)": (VAULT / cfg.notes.screens).read_bytes(),
    }


@pytest.mark.parametrize("which", ["example fixture", "his live note (scratch copy)"])
def test_x4_a_handicap_block_freezes_or_parses_never_crashes(tmp_path, which):
    payload = with_handicap(_notes(tmp_path)[which])
    try:
        note = parse_note_bytes(Path("scratch.md"), "screens", payload)
    except Exception as error:  # the NOT AS EXPECTED case: say it, loudly
        print(f"X4 [{which}]: EXCEPTION escaped parse_note_bytes: {type(error).__name__}")
        raise
    pool = next((item.block for item in note.blocks if item.key == "pool"), None)
    handicap_errors = [e for e in note.errors if "handicap" in e]
    print(
        f"X4 [{which}]: parse errors {len(note.errors)} (naming handicap: {len(handicap_errors)}) · "
        f"pool parsed: {pool is not None} · pool.handicap present: "
        f"{getattr(pool, 'handicap', None) is not None}"
    )
    screens = tmp_path / "screens.md"
    screens.write_bytes(payload)
    try:
        parsed = load_sources(
            screens, FIXTURES / "radar-lists.example.md",
            scan_interval=60, poll_interval=60, finviz_max_rpm=None,
            list_chunk_size=config().list_chunk_size, context_tickers=0,
        )
    except Exception as error:
        print(f"X4 [{which}]: EXCEPTION escaped load_sources: {type(error).__name__}")
        raise
    names_handicap = bool(parsed.pool_error and "handicap" in parsed.pool_error)
    print(
        f"X4 [{which}]: load_sources pool_error set: {parsed.pool_error is not None} "
        f"(names handicap: {names_handicap}) · frozen: {parsed.frozen}"
    )
    if pool is None:
        assert handicap_errors and parsed.frozen and names_handicap   # main: the loud freeze
    else:
        assert not note.errors and pool.handicap is not None           # H1: it parses
