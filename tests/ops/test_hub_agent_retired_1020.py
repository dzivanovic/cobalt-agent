"""Cos-cutover-tooling card 2026-10-20/931, row T1c (brain L79, R1863).

Read on the real DEPLOY-HUB.md, in the form of tests/ops/test_hub_cos_restart_1019.py: each test
pins only the lines its row changes, found by their own text (no whole-line pin, no BASE hash).
T1c: every read the hub makes of the agent names the retired case, `com.cobalt.agent recorded
retired`, read from the one record the two scripts read (`ops/desk/retired-labels`) with a
`grep` string already on the launch line; no allow string changes.
"""

from __future__ import annotations

from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md"
DESK = REPO / "ops" / "desk"

RETIRED = "com.cobalt.agent recorded retired"
READ = 'grep -c -x -F "com.cobalt.agent" /Users/cobalt/cobalt/ops/desk/retired-labels'
FOUR = "com.cobalt.agent com.cobalt.aset com.cobalt.cos com.cobalt.radar"

# each place by its own start (the D1 line by its `<radar pid>`)
PLACES = {
    "P8": "- **P8 THE OUTAGE",
    "GATE": "- GATE: exit 0",
    "smoke (a)": "- (a) `launchctl print`",
    "STEP-5 (3)": "- (3) THE RESTORE",
    "THE ONE RESUME": "- THE ONE RESUME",
    "smoke (f)": "- (f) `COBALT_ENV=production uv run cobalt validate`",
    "RED": "RED = a resident",
}


def lines() -> list[str]:
    return HUB.read_text(encoding="utf-8").splitlines()


def one(prefix: str) -> str:
    (line,) = [ln for ln in lines() if ln.startswith(prefix)]
    return line


def d1() -> str:
    (line,) = [ln for ln in lines() if "<radar pid>" in ln]
    return line


@pytest.mark.parametrize("place", sorted(PLACES))
def test_t1c_each_place_names_the_retired_agent(place):
    """RED on BASE: the place does not hold the literal."""
    assert RETIRED in one(PLACES[place]), place


def test_t1c_d1_names_the_retired_agent():
    """RED on BASE: D1 does not hold the literal."""
    line = d1()
    assert RETIRED in line
    assert "no `ps -p`" in line


def test_t1c_the_file_holds_the_literal_eight_times():
    """RED on BASE: count 0. LINES holding the literal, not occurrences."""
    assert len([ln for ln in lines() if RETIRED in ln]) == 8


def test_t1c_p8_reads_the_record_and_fails_a_retired_agent_online():
    """RED on BASE: P8 holds neither the read nor the FAILED text."""
    p8 = one(PLACES["P8"])
    assert READ in p8
    assert f"FAILED PREFLIGHT: {RETIRED} but ONLINE" in p8
    assert "Bash(grep *)" in one("claude --bg ")


def test_t1c_the_gate_takes_the_retired_agent_out_of_the_restart_set():
    """RED on BASE: the GATE line has no minus for the agent."""
    gate = one(PLACES["GATE"])
    assert "also minus `com.cobalt.agent`" in gate
    assert "com.cobalt.agent: recorded retired — not restarted" in gate
    smoke_f = one(PLACES["smoke (f)"])
    assert "minus `com.cobalt.agent`" in smoke_f


def test_t1c_step5_never_kickstarts_a_retired_agent():
    """RED on BASE: STEP-5 (3) kickstarts the agent whenever it is stopped."""
    assert f"never typed when `{RETIRED}`" in one(PLACES["STEP-5 (3)"])


def test_t1c_the_two_scripts_read_the_same_record():
    """RED on BASE: neither script names the record."""
    for script in ("deploy-step0.sh", "deploy-outage.sh"):
        text = (DESK / script).read_text(encoding="utf-8")
        assert '"$REPO/ops/desk/retired-labels"' in text, script


# ---- CONTROLS, green on BASE and after ---------------------------------------------------------

def test_c_the_gate_within_span_is_the_four_labels():
    gate = one(PLACES["GATE"])
    assert gate.split("within `", 1)[1].split("`", 1)[0] == FOUR


def test_c_d1_still_reads_cos():
    line = d1()
    assert "<cos pid>" in line
    assert "com.cobalt.cos loaded since STEP-R" in line


def test_c_no_allow_string_changed():
    launch = [ln for ln in lines() if ln.startswith("claude --bg ")]
    assert len(launch) == 1
    for s in ("Bash(launchctl kickstart gui/501/com.cobalt.agent)",
              "Bash(/Users/cobalt/cobalt/cobalt.sh status)",
              "Bash(/Users/cobalt/cobalt/cobalt.sh stop)"):
        assert launch[0].count(s) == 1, s
    assert "retired" not in launch[0]
