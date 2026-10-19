"""Hub-cos-restart card 2026-10-19/869 (hub-cos-restart-1019), rows R1-R3 (brain L79, R1863).

Read on the real DEPLOY-HUB.md, in the form of tests/ops/test_hub_deferred_1018.py: each test pins
only the lines its row changes, found by their own text (no whole-line pin, no BASE hash).
R1: STEP-R's set check admits `com.cobalt.cos`: the restartable set is agent, aset, cos, radar.
R2: a restart-set label that is not loaded is skipped and acts on nothing.
R3: a loaded cos is booted out, waited on and bootstrapped after radar, as aset is.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md"

GATE = "- GATE: exit 0"
NOT_LOADED = "- NOT LOADED"
SKIPPED = "com.cobalt.cos: not loaded — skipped"
ANYTHING_ELSE = (
    "Anything else (an `UNCLASSIFIED` row, `com.cobalt.herdr` / `com.cobalt.mainframe` / "
    "`com.cobalt.obsidian`, a non-zero exit)"
)
COS_STRINGS = (
    "launchctl bootout gui/501/com.cobalt.cos",
    "launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist",
    "launchctl kickstart -k gui/501/com.cobalt.cos",
)
NAMES = {"agent", "aset", "cos", "radar"}
LABEL = re.compile(r"com\.cobalt\.([a-z0-9-]+)")

AGENT, ASET, COS, RADAR = (f"com.cobalt.{n}" for n in ("agent", "aset", "cos", "radar"))
HERDR, OBSIDIAN = "com.cobalt.herdr", "com.cobalt.obsidian"


def lines() -> list[str]:
    return HUB.read_text(encoding="utf-8").splitlines()


def one(prefix: str) -> str:
    (line,) = [ln for ln in lines() if ln.startswith(prefix)]
    return line


def four() -> set[str]:
    line = one(GATE)
    return set(line.split("within `", 1)[1].split("`", 1)[0].split())


def admits(s: set[str]) -> bool:
    return s <= four()


# ---- R1: the GATE admits cos ------------------------------------------------------------------

def test_r1_the_f16_set_is_admitted():
    assert admits({ASET, COS, RADAR}) is True
    skipped = [ln for ln in lines() if ln.startswith(NOT_LOADED) and SKIPPED in ln]
    assert len(skipped) == 1, skipped


def test_c1_a_label_outside_the_four_is_refused():
    """CONTROL, green on BASE and after."""
    assert admits({ASET, HERDR}) is False
    assert admits({OBSIDIAN}) is False
    assert ANYTHING_ELSE in one(GATE)


# ---- R2: a not-loaded cos is skipped ----------------------------------------------------------

def test_r2_a_not_loaded_cos_is_skipped_and_acts_on_nothing():
    ls = lines()
    at = [i for i, ln in enumerate(ls) if ln.startswith(NOT_LOADED)]
    assert len(at) == 1, "no `- NOT LOADED` line"
    line = ls[at[0]]
    for s in ("launchctl print gui/501/com.cobalt.cos", SKIPPED,
              "/Users/cobalt/cobalt/ops/com.cobalt.cos.plist", "bootstrap-only deploy"):
        assert s in line, s
    for verb in ("launchctl bootout", "launchctl bootstrap", "launchctl kickstart"):
        assert verb not in line, verb
    assert ls[at[0] - 1].startswith(GATE)
    (d1,) = [ln for ln in ls if "<radar pid>" in ln]
    assert "<cos pid>" in d1
    assert "com.cobalt.cos loaded since STEP-R" in d1
    smoke_f = one("- (f) `COBALT_ENV=production uv run cobalt validate`")
    assert "not loaded — skipped" in smoke_f


# ---- R3: a loaded cos is restarted after radar ------------------------------------------------

def test_r3_cos_is_restarted_after_radar():
    assert "`com.cobalt.aset`, `com.cobalt.radar`, `com.cobalt.cos` in `<restart set>`" in one("4.2 ")
    four_six = one("4.6 for each label taken down")
    cos = four_six.index("com.cobalt.cos.plist")
    assert four_six.index("com.cobalt.radar.plist") < cos
    assert cos < four_six.index("kickstart gui/501/com.cobalt.agent")
    launch = one("claude --bg ")
    for s in COS_STRINGS:
        assert launch.count(f'"Bash({s})"') == 1, s
    assert '"Bash(launchctl kickstart -k gui/501/com.cobalt.radar)" <launchd strings>' in launch
    assert "`com.cobalt.cos`" in one("MODEL: ")
    assert "loop stamping" in one("- (e) `COBALT_ENV=production uv run cobalt heartbeat show`")


def test_c2_no_launchctl_call_names_a_label_outside_the_four():
    """CONTROL 2, green on BASE and after."""
    for ln in lines():
        if "launchctl " in ln:
            for name in LABEL.findall(ln):
                assert name in NAMES, (name, ln)
    launch = one("claude --bg ")
    strings = re.findall(r'"Bash\((launchctl [^)]*)\)"', launch)
    assert strings
    for s in strings:
        if s == "launchctl print gui/501/*":
            continue
        names = LABEL.findall(s)
        assert names and set(names) <= NAMES, s
