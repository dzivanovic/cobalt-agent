"""ops/desk/card-fill.sh, a job card filled for its check from the build's stop line
(card 17 A3). Every run edits a tmp card under a tmp repo root (COBALT_REPO_ROOT).
"""

from __future__ import annotations

import datetime
import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
FILL = REPO / "ops" / "desk" / "card-fill.sh"
STOP = (
    "BUILT · job: x-job · tip: 1a2b3c4d | on 0f0e0d0c | migration: none | offline 9/0 | "
    "with-DB 3/0 | live-note 2/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | "
    "rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0"
)
# body lines that look like header keys: only the header is ever edited
BODY = "\n## ROWS\n| row | what |\n|---|---|\nTIP:\nCHECK REPORT:\nHOUSE B:\n"


@pytest.fixture
def desk(tmp_path):
    repo = tmp_path / "repo"
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    reports.mkdir(parents=True)
    report = tmp_path / "wt" / "x-job-build.md"
    report.parent.mkdir()
    report.write_text("# build\n\n## RECORDS\n\n" + STOP + "\n\n")
    card = tmp_path / "01-x-job-card.md"
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: 0f0e0d0c\nTIP:\nREPORT: {report}\nCHECK REPORT:\nHOUSE B:\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n" + BODY
    )
    env = dict(os.environ, COBALT_REPO_ROOT=str(repo))
    return card, report, reports, env


def fill(*args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(FILL), *args], env=env, capture_output=True, text=True, timeout=60
    )


def test_the_three_header_lines_are_filled_and_the_body_is_byte_equal(desk):
    card, report, reports, env = desk
    done = fill(str(card), env=env)
    assert done.returncode == 0, done.stderr
    today = datetime.date.today().isoformat()
    check = reports / f"x-job-check-{today}.md"
    lines = card.read_text().split("\n")
    assert "TIP: 1a2b3c4d" in lines
    assert f"CHECK REPORT: {check}" in lines
    assert "HOUSE B: as needed" in lines
    assert card.read_text().endswith("RULINGS: 2026-01-02 R1\n" + BODY)
    assert "TIP: → TIP: 1a2b3c4d" in done.stdout
    assert f"CHECK REPORT: → CHECK REPORT: {check}" in done.stdout
    assert "HOUSE B: → HOUSE B: as needed" in done.stdout
    assert not any(line.startswith("HOUSE A:") for line in lines)


def test_a_filled_house_b_and_check_report_are_kept(desk):
    card, report, reports, env = desk
    text = card.read_text().replace("HOUSE B:\n", "HOUSE B: mandatory — sizing\n")
    text = text.replace("CHECK REPORT:\n", "CHECK REPORT: /x/kept.md\n")
    card.write_text(text)
    done = fill(str(card), env=env)
    assert done.returncode == 0, done.stderr
    lines = card.read_text().split("\n")
    assert "HOUSE B: mandatory — sizing" in lines
    assert "CHECK REPORT: /x/kept.md" in lines
    assert "TIP: 1a2b3c4d" in lines


def test_no_house_adds_one_line_after_check_report(desk):
    card, report, reports, env = desk
    done = fill(str(card), "--no-house", "2026-01-02 R1", env=env)
    assert done.returncode == 0, done.stderr
    lines = card.read_text().split("\n")
    at = next(i for i, line in enumerate(lines) if line.startswith("CHECK REPORT:"))
    assert lines[at + 1] == "HOUSE A: none — overruled 2026-01-02 R1"
    assert sum(line.startswith("HOUSE A:") for line in lines) == 1
    assert card.read_text().endswith("RULINGS: 2026-01-02 R1\n" + BODY)
    # a second run with the flag adds nothing
    before = card.read_bytes()
    done = fill(str(card), "--no-house", "2026-01-02 R1", env=env)
    assert done.returncode == 0, done.stderr
    assert card.read_bytes() == before


def test_a_second_run_changes_nothing(desk):
    card, report, reports, env = desk
    assert fill(str(card), env=env).returncode == 0
    before = card.read_bytes()
    done = fill(str(card), env=env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.strip() == "nothing changed"
    assert card.read_bytes() == before


@pytest.mark.parametrize(
    "last",
    [
        "FAILED: W — x",
        STOP.replace("self-check: 3 of 3", "self-check: 2 of 3"),
        STOP.replace("job: x-job", "job: y-job"),
        STOP.replace("job: x-job", "job: x-jobber"),
        STOP.replace("tip: 1a2b3c4d", "tip: 1a2b3c4"),
        STOP.replace("tip: 1a2b3c4d", "tip: 1A2B3C4D"),
        "(run in progress — next step under ## CONTINUE)",
    ],
)
def test_a_report_not_ending_in_a_full_built_line_of_this_job_is_refused(desk, last):
    card, report, reports, env = desk
    report.write_text("# build\n\n" + STOP + "\n\n" + last + "\n")
    before = card.read_bytes()
    done = fill(str(card), env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert card.read_bytes() == before


def test_a_card_with_no_report_is_refused(desk):
    card, report, reports, env = desk
    card.write_text(card.read_text().replace(f"REPORT: {report}\n", ""))
    before = card.read_bytes()
    done = fill(str(card), env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert card.read_bytes() == before


@pytest.mark.parametrize("value", ["2026-01-02", "R1", "2026-1-2 R1", "2026-01-02 R1 x"])
def test_a_bad_no_house_value_is_refused(desk, value):
    card, report, reports, env = desk
    before = card.read_bytes()
    done = fill(str(card), "--no-house", value, env=env)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert card.read_bytes() == before
