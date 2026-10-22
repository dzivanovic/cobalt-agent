"""Deploy-cos-restart card 2026-10-21/1008 (deploy-cos-restart), rows F1-F4 (his 2026-10-20 R2240;
brain R2355, L79).

Read on the real DEPLOY-HUB.md and STANDING-LIST.md, in the form of
tests/ops/test_hub_cos_restart_1019.py: each test pins only the lines its row changes, found by
their own text (no whole-line pin, no BASE hash).
F1: the deploy line and the approved list carry the three R60 cos strings, each after its aset twin.
F2: STEP-R admits a loaded, running cos from its repo plist; one the strings cannot restore is
    still refused; the outage and smoke name cos.
F3: THE ONE RESUME (e) reads cos when the report's `## RESTARTS` puts it in `<restart set>`.
F4: the STEP-5 stop line and rule F carry the cos field.
"""

from __future__ import annotations

import shlex
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
HUB = HUBS / "DEPLOY-HUB.md"
LIST = HUBS / "STANDING-LIST.md"

S1 = "Bash(launchctl bootout gui/501/com.cobalt.cos)"
S2 = "Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.cos.plist)"
S3 = "Bash(launchctl kickstart -k gui/501/com.cobalt.cos)"
TWINS = {
    S1: "Bash(launchctl bootout gui/501/com.cobalt.aset)",
    S2: "Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist)",
    S3: "Bash(launchctl kickstart -k gui/501/com.cobalt.aset)",
}
COS = "com.cobalt.cos"
COS_PLIST = "/Users/cobalt/cobalt/ops/com.cobalt.cos.plist"
NOT_LOADED = "- NOT LOADED"
OLD_REFUSAL = "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)"
NEW_REFUSAL = (
    "FAILED: RESTARTS — com.cobalt.cos loaded <state or path>; the bootstrap string would not "
    "restore it · rollback: not used"
)
RESUME = "- THE ONE RESUME"
STOP5 = "- (5) The last line:"
RULE_F = "- F. Residents come up"


def lines(path: Path = HUB) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def one(prefix: str) -> str:
    (line,) = [ln for ln in lines() if ln.startswith(prefix)]
    return line


def tools(line: str, option: str) -> list[str]:
    """The strings after `--allowedTools` or `--disallowedTools`, up to the next option."""
    words = shlex.split(line)
    out, inside = [], False
    for w in words:
        if w.startswith("--"):
            inside = w == option
            continue
        if inside:
            out.append(w)
    return out


def allow() -> list[str]:
    return tools(one("claude --bg "), "--allowedTools")


# ---- F1: the line and the approved list -------------------------------------------------------

def test_f1_the_hub_line_carries_the_three_cos_strings_once():
    a = allow()
    for s, twin in TWINS.items():
        assert a.count(s) == 1, s
        assert a.index(s) == a.index(twin) + 1, (s, a[a.index(twin):a.index(twin) + 2])
    assert len([s for s in a if s.startswith("Bash(launchctl ")]) == 11


def test_f1_the_standing_list_names_the_three_strings():
    text = LIST.read_text(encoding="utf-8")
    s3 = text.split("\n## 3. ", 1)[1].split("\n## 4. ", 1)[0]
    for s, twin in TWINS.items():
        assert s3.count(s) == 1, s
        (row,) = [ln for ln in s3.splitlines() if s in ln]
        assert twin in row, (s, row)
    (never,) = [ln for ln in lines(LIST) if ln.startswith("- `launchctl` on a build or check line")]
    assert f"`{COS}`" in never, never


# ---- F2: the admit ----------------------------------------------------------------------------

def test_f2_a_loaded_running_cos_is_admitted_at_step_r():
    line = one(NOT_LOADED)
    assert OLD_REFUSAL not in line
    assert "keeps it in `<restart set>`" in line
    assert COS_PLIST in line
    # the restore the line promises exists
    assert S2[len("Bash("):-1] in one("4.6 for each label")
    each = one("4.2 for each of ").split("for each of ", 1)[1].split(" in `<restart set>`", 1)[0]
    assert f"`{COS}`" in each.split(", "), each
    a = allow()
    for s in (S1, S2, S3):
        assert s in a, s


def test_f2_a_loaded_cos_the_strings_cannot_restore_is_still_refused():
    assert NEW_REFUSAL in one(NOT_LOADED)


def test_f2_the_outage_and_smoke_name_cos():
    model = one("MODEL: ")
    at = model.index("the labels of `<launchd set>`")
    assert f"`{COS}`" in model[:at], model[:at]
    assert "cos when in `<restart set>`" in one("- (a) `launchctl print` aset")
    (row,) = [ln for ln in lines() if "NO HARMLESS VARIANT, strings with no wildcard" in ln]
    assert "the three `kickstart -k`" in row


# ---- F3: THE ONE RESUME reads cos -------------------------------------------------------------

def test_f3_the_one_resume_reads_cos_when_in_the_set():
    assert ("`…/com.cobalt.cos` → `state = running` when the report's `## RESTARTS` puts "
            "`com.cobalt.cos` in `<restart set>` (a cos outside it is not read)") in one(RESUME)


def test_c_a_cos_outside_the_set_reads_and_prints_as_today():
    """CONTROL, green on BASE and after."""
    assert ("(e) `launchctl print gui/501/com.cobalt.aset` and `…/com.cobalt.radar` → "
            "`state = running`, ") in one(RESUME)
    assert ("— aset: <UP|DOWN|not in the set> — radar: <UP|DOWN|not in the set> — launchd: "
            in one(STOP5))
    assert "the stop line says `aset: DOWN · radar: DOWN`" in one(RULE_F)


# ---- F4: the stop line carries cos ------------------------------------------------------------

def test_f4_the_stop_line_and_rule_f_carry_the_cos_field():
    assert "`com.cobalt.cos` in `<restart set>` adds `— cos: <UP|DOWN>` after the aset field" in one(STOP5)
    assert "and `cos: DOWN` when `com.cobalt.cos` is in `<restart set>`" in one(RULE_F)
