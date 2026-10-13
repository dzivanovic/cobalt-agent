"""THE RULE's sweep over the real reports (card 446 C1, R1311 (c)).

THE RULE (`ops/desk/deploy-card.sh`, one text in the three scripts) is sourced alone and its
seams are called on the committed reports of this tree, dated 2026-10-02 to 2026-10-12:

- every check report (`*-check*-2026-10-*.md`) whose last non-blank line carries
  `held unfixed: <n>`, n >= 1 (the one condition under which a gate runs THE RULE): a MISMATCH
  is `held_union` reading a number of ids other than n, or one id twice;
- every build report (`*-build-2026-10-*.md`): each CLAIM line (a line starting, after an
  optional bullet and bold, with FIXED, CARRIED or SETTLED) that `fix_lines` does not read for
  its id is a MISMATCH.

`SWEEP_EXEMPT` names the reports no reader can resolve, each with the shape that makes it so.
No report is edited to pass (R1157); nothing here writes outside `tmp_path`.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
REPORTS = REPO / "docs" / "40 - DevDocs" / "reports"
SCRIPT = REPO / "ops" / "desk" / "deploy-card.sh"
RULE_START = "# ---- THE RULE (card 317"
RULE_END = "# ---- end of THE RULE"
FIRST, LAST = "2026-10-02", "2026-10-12"

DATE = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
HELD_N = re.compile(r"(?:^| )held unfixed: ([0-9]+)(?: |$)")
CLAIM = re.compile(r"^(?:[-*]\s+)?\**(FIXED|CARRIED|SETTLED)\b")
CLAIM_ID = re.compile(r"^(?:[-*]\s+)?\**(?:FIXED|CARRIED|SETTLED):?\**\s+`?([A-Za-z0-9._-]+)")

# <report file name> → why no mark of it can be read (card 446 C1, drafter ASK DESK 1, 2, 4)
SWEEP_EXEMPT: dict[str, str] = {
    "brain-hub-check-2026-10-03.md":
        "shape: a `**HELD**` table row of a finding not left unfixed (O2, `**HELD** as a fact … OUT OF "
        "SCOPE`) beside the one `HELD, NOT FIXED` row O1; card 361's `**HELD**` read counts both (n 1, "
        "read 2); ASK DESK 1",
    "drc-d5-check-2026-10-04.md":
        "shape: one defect held under two ids in two passes, two `## RUNS` (O1, B3, both `HELD, NOT "
        "FIXED`), each pass's stop line n 1: read 2, a count no mark resolves; ASK DESK 2",
    "kill-hub-row-check-2026-10-10.md":
        "shape: twelve `## RUNS` table rows with a bare `HELD` verdict and `## FIXES` prose: no NOT FIXED "
        "mark (n 12, read 0); ASK DESK 1",
    "radar-display-fix-1008-terra-check-2026-10-11.md":
        "shape: six `## RUNS` bullets with a bare `HELD` or `HELD (shadow …)` verdict, `## FIXES` a prose "
        "line: no NOT FIXED mark (n 6, read 0); ASK DESK 1",
    "s4-p1-1009-terra-check-2026-10-11.md":
        "shape: twenty-five `## RUNS` bullets ending `· HELD`, `## FIXES` prose: no NOT FIXED mark "
        "(n 25, read 0); ASK DESK 1",
    "f4-refresh-build-2026-10-10.md":
        "shape: `:262` a bulleted bold CARRIED line with a backticked id and a trailing sentence; read, it "
        "would count 304's O1 twice beside row CR's plain line (`has 2 FIXED or CARRIED lines`); ASK DESK 4",
    "dev-rebuild-port-build-2026-10-03.md":
        "shape: `:101`, `:104` bullets `- SETTLED <path> by Edit` record a merge resolution, no claim (no "
        "colon, no id); the claim regex takes the word; DECISION C1-1",
}

# the reports the first run swept: a report added later is not swept, a report removed fails
CHECKS_SWEPT: int | None = 18
BUILDS_SWEPT: int | None = 85


def in_window(name: str) -> bool:
    m = DATE.search(name)
    return bool(m) and FIRST <= m.group(0) <= LAST


def last_line(path: Path) -> str:
    lines = [ln for ln in path.read_text(errors="replace").splitlines() if ln.strip()]
    return lines[-1] if lines else ""


def held_n(line: str) -> int:
    """THE RULE's `held_n`: the first `held unfixed: <n>` of the line when n >= 1, else 0."""
    m = HELD_N.search(line)
    return int(m.group(1)) if m and re.fullmatch(r"[1-9][0-9]*", m.group(1)) else 0


@pytest.fixture(scope="module")
def rule(tmp_path_factory) -> Path:
    text = SCRIPT.read_text()
    start = text.index(RULE_START)
    path = tmp_path_factory.mktemp("rule") / "the-rule.sh"
    path.write_text(text[start:text.index(RULE_END, start)])
    return path


def seam(rule: Path, *args: str, stdin: str | None = None) -> str:
    done = subprocess.run(["sh", "-c", '. "$0"; "$@"', str(rule), *args], input=stdin,
                          capture_output=True, text=True, timeout=60)
    assert done.returncode == 0, done.stderr
    return done.stdout


@pytest.fixture(scope="module")
def sweep(rule: Path) -> tuple[list[Path], list[Path], dict[str, list[str]]]:
    checks = sorted(p for p in REPORTS.glob("*-check*-2026-10-*.md")
                    if in_window(p.name) and held_n(last_line(p)))
    builds = sorted(p for p in REPORTS.glob("*-build-2026-10-*.md") if in_window(p.name))
    found: dict[str, list[str]] = {}
    for path in checks:
        n = held_n(last_line(path))
        ids = seam(rule, "held_union", str(path)).split()
        if len(ids) != n or len(set(ids)) != len(ids):
            found.setdefault(path.name, []).append(
                f"{path.name} · n {n} · read {len(ids)} ({' '.join(ids) or 'none'}) · shape: check")
    for path in builds:
        for i, line in enumerate(path.read_text(errors="replace").splitlines(), start=1):
            if not CLAIM.match(line):
                continue
            m = CLAIM_ID.match(line)
            cid = m.group(1) if m else "-"
            read = seam(rule, "fix_lines", stdin=line + "\n").splitlines()
            if not any(r.split()[1:2] == [cid] for r in read):
                found.setdefault(path.name, []).append(
                    f"{path.name}:{i} · claim {cid} · read {len(read)} · shape: {line.strip()[:160]}")
    return checks, builds, found


def test_the_sweep_has_no_mismatch(sweep):
    found = sweep[2]
    left = [ln for name, lines in sorted(found.items()) if name not in SWEEP_EXEMPT for ln in lines]
    assert not left, "\n" + "\n".join(left)


def test_every_exempt_entry_still_mismatches(sweep):
    assert SWEEP_EXEMPT, "no exemption is named"
    stale = [name for name in SWEEP_EXEMPT if name not in sweep[2]]
    assert not stale, stale


def test_the_exempt_reasons_name_their_shape():
    assert SWEEP_EXEMPT, "no exemption is named"
    for name, reason in SWEEP_EXEMPT.items():
        assert (REPORTS / name).is_file(), name
        assert len(reason.strip()) >= 20, name


def test_the_304_check_reads_o1_and_a3(rule):
    """Card 446 A1: card 304's check gives its two `HELD, NOT FIXED` table rows and nothing else
    (0 ids before the card)."""
    ids = seam(rule, "held_union", str(REPORTS / "f4-refresh-check-2026-10-10.md")).split()
    assert ids == ["O1", "A3"]


def test_the_sweep_swept_what_it_pins(sweep):
    checks, builds, _ = sweep
    assert (len(checks), len(builds)) == (CHECKS_SWEPT, BUILDS_SWEPT), [p.name for p in checks]
