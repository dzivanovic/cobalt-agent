"""`.gitignore`: a `db apply` file beside its card can be committed (card 2026-10-12 417 K4).

`*.sql` keeps every database dump out of git; one carve-out lets
`docs/40 - DevDocs/prompts/<date>/<nn>-<name>-apply.sql` in. Read with
`git check-ignore --no-index` against this tree's `.gitignore`; the paths are constructed and
never created.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]


def check_ignore(path: str) -> int:
    return subprocess.run(
        ["git", "-C", str(REPO), "check-ignore", "-q", "--no-index", path],
        capture_output=True, text=True, timeout=60,
    ).returncode


def test_g1_an_apply_file_beside_its_card_is_not_ignored():
    """RED on BASE: exit 0 (ignored by `*.sql`)."""
    assert check_ignore("docs/40 - DevDocs/prompts/2026-01-02/1-x-apply.sql") == 1


@pytest.mark.parametrize("path", [
    "docs/40 - DevDocs/prompts/2026-01-02/1-x.sql",
    "docs/40 - DevDocs/prompts/2026-01-02/cobalt_brain.sql",
    "docs/40 - DevDocs/reports/1-x-apply.sql",
    "docs/00 - Project/x-apply.sql",
    "bars-dump-1.sql",
])
def test_g2_every_other_sql_file_stays_ignored(path):
    """Both sides: ignored on BASE and after."""
    assert check_ignore(path) == 0
