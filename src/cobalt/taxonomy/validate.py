"""`python -m cobalt.taxonomy.validate` — read the VAULT, print the table,
exit non-zero on any error.

READS THE VAULT, NOT THE REPO (ADR-0008 D3). Until 2026-09-08 this loaded
`configs/cobalt/taxonomy/trade_defs/*.yaml`; those files are gone and the
strategy notes in `1 - Trading/4 - Strategies/` are the trade_defs' one
home. Which vault it reads is `COBALT_ENV`'s business, not this module's
— `cobalt.vault.resolve_vault_path()` answers it (RULING 7).

Three things print, and the second two are the reason this is worth
running: the validated defs, the DRAFTS it skipped and why, and the
frontmatter WARNINGS where a note's own header disagrees with its def.
A draft is not a failure — a trader mid-way through writing a strategy
must not break the gate — but an unlisted draft is a def someone thinks
is live and is not.

No partial output on a hard failure: a load error prints and exits before
any table is drawn.
"""

from __future__ import annotations

import sys

from .loader import TaxonomyConfigError, iter_tunables, load_tunables
from .trade_def import TradeDef
from .tunables import replay_backlog
from .vault_loader import VaultTradeDefs, load_vault_trade_defs

_HEADERS = [
    "slug", "name", "class", "families",
    "#preconditions", "#text-fallbacks", "#tunables", "#quality",
]


def _row(slug: str, name: str, td: TradeDef) -> list[str]:
    text_fallbacks = sum(
        1 for p in (*td.preconditions, *td.radar_watch, *td.avoid) if not p.computable
    )
    return [
        slug,
        name,
        td.trade_class.value,
        ",".join(f.value for f in td.family),
        str(len(td.preconditions)),
        str(text_fallbacks),
        str(sum(1 for _ in iter_tunables(td))),
        str(len(td.quality_factors)),
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


def print_result(result: VaultTradeDefs) -> None:
    """The three blocks — defs, drafts, warnings. Shared with the CLI."""
    rows = [_row(d.slug, d.name, d.definition) for d in sorted(result.defs, key=lambda d: d.slug)]
    _print_table(rows)
    print(f"\n{len(result.defs)} trade_def(s) validated OK from the vault.")

    if result.drafts:
        print(f"\n{len(result.drafts)} draft(s) skipped — not errors, not yet defs:")
        for draft in sorted(result.drafts, key=lambda d: d.slug):
            print(f"  {draft.slug:<24} {draft.reason}")
    else:
        print("\nNo drafts: every strategy note carries a finished definition.")

    if result.user_tunables:
        print(f"\n{len(result.user_tunables)} per-trade tunable row(s) from the vault:")
        for t in sorted(result.user_tunables, key=lambda t: t.key):
            print(f"  {t.key:<44} {t.row.scope}")

    if result.warnings:
        print(f"\n{len(result.warnings)} frontmatter warning(s) — the human wins:")
        for w in result.warnings:
            print(f"  {w}")


def main() -> int:
    try:
        result = load_vault_trade_defs()
    except TaxonomyConfigError as e:
        print(f"FAILED: {e}", file=sys.stderr)
        return 1

    print_result(result)

    tunables = load_tunables()
    backlog = replay_backlog(tunables)
    print(
        f"\n{len(tunables.tunables)} engine tunable(s) loaded "
        f"({len(backlog)} in replay backlog: dynamic AND status != solidified)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
