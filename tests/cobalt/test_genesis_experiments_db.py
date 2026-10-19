"""F21 chunk 1, RUN row G6 (card 2026-10-13 468; X7 (b)): asserts nothing.

On cobalt_dev under the lock, inside the suite's rolled-back transaction
(RULING 7.1d, L76): the committed `docs/00 - Project/PROJECT-LEDGER.md` goes
through `GenesisStore`, and the acceptance question goes through `search` with
both tsquery forms. The question carries no figure: his figure is never written
in a file (L32). Printed: the chunk count, and per form the rank of the first
hit whose body holds "stop buffer" and its `line_start`; never a body. Needs
0026, so the gate runs it in PASS 2 (`ops/desk/gate-lists.md`).
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]

LEDGER = Path(__file__).resolve().parents[2] / "docs" / "00 - Project" / "PROJECT-LEDGER.md"
QUESTION = "why is the stop buffer"


def test_x7b_the_committed_ledger_through_search_both_forms():
    from cobalt.genesis.search import search
    from cobalt.genesis.store import GenesisStore, import_paths

    [source] = import_paths([str(LEDGER)], store=GenesisStore("cobalt_dev"))
    print(f"G6 chunks: {len(source.chunks)}")
    for form in ("websearch", "plain"):
        hits = search(QUESTION, limit=50, form=form)
        first = next(((i, h) for i, h in enumerate(hits, 1) if "stop buffer" in h.body.lower()), None)
        if first is None:
            print(f"G6 {form}: {len(hits)} hits; none holds 'stop buffer' in the first 50")
        else:
            print(f"G6 {form}: {len(hits)} hits; first 'stop buffer' hit rank {first[0]}, "
                  f"line_start {first[1].line_start}")
