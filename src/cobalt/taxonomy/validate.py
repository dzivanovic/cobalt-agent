"""`python -m cobalt.taxonomy.validate` — loads every trade_def, prints a
summary table, exits non-zero on any failure. No partial output: a load
failure prints the error and exits before any table is drawn.
"""

from __future__ import annotations

import sys

from .loader import TaxonomyConfigError, iter_tunables, load_trade_defs, load_tunables
from .trade_def import TradeDef
from .tunables import replay_backlog

_HEADERS = ["id", "class", "families", "#preconditions", "#text-fallbacks", "#tunables"]


def _row(td: TradeDef) -> list[str]:
    text_fallbacks = sum(
        1 for p in (*td.preconditions, *td.radar_watch, *td.avoid) if not p.computable
    )
    n_tunables = sum(1 for _ in iter_tunables(td))
    return [
        td.id,
        td.trade_class.value,
        ",".join(f.value for f in td.family),
        str(len(td.preconditions)),
        str(text_fallbacks),
        str(n_tunables),
    ]


def _print_table(rows: list[list[str]]) -> None:
    widths = [
        max(len(h), *(len(r[i]) for r in rows)) if rows else len(h)
        for i, h in enumerate(_HEADERS)
    ]

    def fmt(cols: list[str]) -> str:
        return " | ".join(c.ljust(w) for c, w in zip(cols, widths))

    print(fmt(_HEADERS))
    print("-+-".join("-" * w for w in widths))
    for r in rows:
        print(fmt(r))


def main() -> int:
    try:
        trade_defs = load_trade_defs()
    except TaxonomyConfigError as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1

    rows = [_row(td) for td in sorted(trade_defs.values(), key=lambda t: t.id)]
    _print_table(rows)
    print(f"\n{len(trade_defs)} trade_def(s) validated OK.")

    tunables = load_tunables()
    backlog = replay_backlog(tunables)
    print(
        f"{len(tunables.tunables)} tunable(s) loaded "
        f"({len(backlog)} in replay backlog: dynamic AND status != solidified)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
