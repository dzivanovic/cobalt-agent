"""THE one recall entry (F21 FINAL F-01, F-07, F-15, L3; card 468 G4).

`search(question, limit=…)` turns the question into a tsquery with
`websearch_to_tsquery('english', …)` (or `plainto_tsquery`, `form="plain"`,
kept for the X7 comparison), matches it against `genesis_chunk.tsv` and
ranks by `ts_rank_cd`. F20, the dream job and O3 call this and nothing
else; no second index, no model call.
"""

from __future__ import annotations

from typing import NamedTuple, Optional

from .store import GenesisStore

#: The two tsquery builders X7 compares; nothing else reaches the SQL.
_FORMS = {"websearch": "websearch_to_tsquery", "plain": "plainto_tsquery"}


class Hit(NamedTuple):
    source: str
    line_start: int
    line_end: int
    rank: float
    body: str


def search(question: str, *, limit: int, form: str = "websearch",
           store: Optional[GenesisStore] = None) -> list[Hit]:
    """The trader's chunks matching `question`, best `ts_rank_cd` first, at most `limit`."""
    if form not in _FORMS:
        raise ValueError(f"unknown tsquery form {form!r}; one of {sorted(_FORMS)}")
    if not question.strip():
        raise ValueError("an empty question matches nothing")
    if limit < 1:
        raise ValueError(f"limit must be at least 1, got {limit}")
    fn = _FORMS[form]
    store = store or GenesisStore()
    with store._connect() as conn:
        rows = conn.execute(
            f"SELECT source, line_start, line_end, ts_rank_cd(tsv, q) AS rank, body "
            f"FROM genesis_chunk, {fn}('english', %s) AS q "
            "WHERE user_id = current_setting('cobalt.trader_id')::int AND tsv @@ q "
            "ORDER BY rank DESC, source, seq LIMIT %s",
            (question, limit),
        ).fetchall()
    return [Hit(source=r[0], line_start=r[1], line_end=r[2], rank=float(r[3]), body=r[4]) for r in rows]


__all__ = ["Hit", "search"]
