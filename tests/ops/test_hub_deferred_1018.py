"""Hub-deferred card 2026-10-18/787 (hub-deferred-1018), rows D1-D2 (brain L79, R1863).

Read on the real DEPLOY-HUB.md, in the form of tests/ops/test_hub_text_1013.py: each test pins
only the lines its row changes, found by their own text (no whole-line pin, no BASE hash).
D1: STEP-R's set check reads the restart set minus every label the card ships `deferred`.
D2: the deferred set is named where it is made and read, and no `launchctl` call names it.
"""

from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md"

GATE = "- GATE: exit 0"
THREE = "com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar"
MINUS = "minus every label of `<deferred set>`"
ANYTHING_ELSE = (
    "Anything else (an `UNCLASSIFIED` row, `com.cobalt.herdr` / `com.cobalt.mainframe` / "
    "`com.cobalt.obsidian`, a non-zero exit)"
)
DEFERRED = "<deferred set>"
CALLS = ("launchctl bootout", "launchctl bootstrap", "launchctl kickstart", "launchctl print")
RESIDENT_STRINGS = (
    "launchctl bootout gui/501/com.cobalt.aset",
    "launchctl bootout gui/501/com.cobalt.radar",
    "launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist",
    "launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist",
    "launchctl kickstart -k gui/501/com.cobalt.aset",
    "launchctl kickstart -k gui/501/com.cobalt.radar",
)

AGENT, ASET, COS, RADAR = (f"com.cobalt.{n}" for n in ("agent", "aset", "cos", "radar"))
HERDR = "com.cobalt.herdr"


def lines() -> list[str]:
    return HUB.read_text(encoding="utf-8").splitlines()


def one(prefix: str) -> str:
    (line,) = [ln for ln in lines() if ln.startswith(prefix)]
    return line


def section(head: str) -> list[str]:
    ls = lines()
    i = next(i for i, ln in enumerate(ls) if ln.startswith(f"## {head}"))
    j = next(j for j in range(i + 1, len(ls)) if ls[j].startswith("## "))
    return ls[i + 1:j]


def rule() -> tuple[set[str], bool]:
    line = one(GATE)
    three = line.split("within `", 1)[1].split("`", 1)[0]
    assert three == THREE, three
    return set(three.split()), MINUS in line


def admits(s: set[str], d: set[str]) -> bool:
    three, minus = rule()
    return (s - d if minus else s) <= three


# ---- D1: STEP-R reads the restart set minus the deferred set ---------------------------------

def test_d1_card_730s_set_is_admitted():
    assert admits({AGENT, ASET, COS, RADAR}, {COS}) is True


def test_d1_a_label_outside_the_three_not_deferred_is_refused():
    """CONTROL, green on BASE and after."""
    assert admits({AGENT, ASET, HERDR}, set()) is False
    assert admits({ASET, HERDR}, {COS}) is False
    assert ANYTHING_ELSE in one(GATE)


# ---- D2: the deferred set is never a launchctl label ------------------------------------------

def test_d2_the_deferred_set_is_named_where_it_is_made_and_read():
    assert one("This file is the same for every deploy").count(DEFERRED) == 1
    assert [ln for ln in section("STEP-C ") if "is `<deferred set>`" in ln]
    drives = one("- THE SET DRIVES THE REST")
    assert "A label of `<deferred set>` is never in `<restart set>` or `<launchd set>`" in drives
    for source in ("from `<restart set>`", "from `<launchd set>`"):
        assert source in drives, source
    smoke_f = one("- (f) `COBALT_ENV=production uv run cobalt validate`")
    assert "`RESTARTS:` minus `<deferred set>`" in smoke_f


def test_d2_no_launchctl_call_names_the_deferred_set():
    for ln in lines():
        if any(call in ln for call in CALLS):
            assert DEFERRED not in ln, ln
    assert len([ln for ln in lines() if DEFERRED in ln]) == 5


def test_d2_the_three_residents_strings_stand():
    """CONTROL 2, green on BASE and after."""
    launch = one("claude --bg ")
    assert launch.count("<launchd strings>") == 1
    for s in RESIDENT_STRINGS:
        assert launch.count(s) == 1, s
    assert COS not in launch
    model = one("MODEL: ")
    assert "the labels of `<launchd set>`" in model
    assert DEFERRED not in model
