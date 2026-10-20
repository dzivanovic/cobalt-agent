"""F5 — `cobalt checkpoint run --slot 0715 --dry-run` on his real notes (card 731 row K13; live-note suite).

Reads `COBALT_LIVE_VAULT_ROOT` (read only). The writer refuses any target
inside the production vault from a dev process (`writer.py`
`assert_write_target`), so each real note's TEXT is copied into a
`tmp_path` vault at the run day's path and the dry run reads it there: the
placement is proven on his real text, and nothing is written anywhere (his
files' bytes are compared before and after). Finviz, the model and the DM
are the offline fakes. Every count of his stays in this process (L32).
"""

from __future__ import annotations

import hashlib
import os
from pathlib import Path

import pytest

from test_checkpoints_offline import at, cp, run  # noqa: F401 — the fixture
from test_prefill_refresh import finviz, plan, vault  # noqa: F401 — F4's fixtures

LIVE = os.getenv("COBALT_LIVE_VAULT_ROOT")
requires_live = pytest.mark.skipif(
    not LIVE, reason="COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run"
)
#: The newest notes only: the `### Market Context:` heading is the template's
#: since F4; an older note is the missing-heading path (X8), not this proof.
NEWEST = 5


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@requires_live
def test_dry_run_finds_the_heading_in_real_notes(cp):  # noqa: F811
    from cobalt.aset.config import load_config

    folder = Path(LIVE) / load_config().daily_note.daily_notes_dir
    notes = sorted(p for p in folder.glob("*.md") if p.stem[:4].isdigit())[-NEWEST:]
    assert notes, "no daily note found under the live vault"
    before = {p: _sha(p) for p in notes}
    # Each check is a bare bool: pytest's assertion rewrite would print the
    # compared text or paths beside the message (L32, card 731 FIX1).
    for i, note in enumerate(notes):  # messages name the index, never his file (L32)
        text = note.read_text(encoding="utf-8")
        has_heading = "### Market Context:" in text.split("\n")
        assert has_heading, f"newest note -{len(notes) - i}: no heading line"
        cp.note.write_text(text, encoding="utf-8")
        copy = _sha(cp.note)
        result = run(cp, "0715", at(7, 15), dry_run=True)
        assert result.action == "dry_run" and result.exit_code == 0
        write = [w for w in result.writes if w.unit == "checkpoint_0715"][0]  # the numbers write (then the final)
        assert not any("anchor not found" in n for n in write.notes), f"newest note -{len(notes) - i}: placement missed the heading"
        added = [x for x in write.diff.split("\n") if x.startswith("+") and not x.startswith("+++")]
        marker_first = added[0] == "+<!-- cobalt:section market_context -->"
        assert marker_first, f"newest note -{len(notes) - i}: the first added line is not the section marker"
        context = [x for x in write.diff.split("\n") if x.startswith(" ")]
        under_heading = "### Market Context:" in [x[1:] for x in context]
        assert under_heading, f"newest note -{len(notes) - i}: the section lands under the heading"
        assert _sha(cp.note) == copy, "a dry run writes nothing"
    untouched = {p: _sha(p) for p in notes} == before
    assert untouched, "his notes are untouched"
