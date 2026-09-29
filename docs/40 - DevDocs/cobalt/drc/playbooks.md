# `src/cobalt/drc/playbooks.py`

## What it does
Playbook name → setup, ONE-TO-ONE (DRC D3-2b; R116 / R117; 09-23 R17 (1)). Deterministic, no LLM, no mapping table (L2).

1. `read_strategies(vault_root)` reads the titles of `taxonomy.vault_loader.STRATEGIES_DIR` (`1 - Trading/4 - Strategies`) AT BUILD TIME: top-level `*.md` files, title = the file name without `.md`. Each title's setup id is its frontmatter `trade_def:` (`vaultwrite.frontmatter.split_frontmatter`) validated by `taxonomy.slug.validate_slug`. Never a committed list (L32 / L45).
2. `strip_side(name)` strips ONE trailing ` Long` / ` Short` — case-insensitive, a whole word ending the name. `X Long Long` strips once; `XLong`, `X Longer` never.
3. `resolve(names, strategies)` / `resolve_playbooks(names, vault_root)` — per name, in the stats log's order (R114): the stripped name EQUALS a title (case-sensitive) → `<name> → <slug>`; no equal title → `unmapped: <name>`; the title's slug missing or invalid → `unmapped: <name> — note <title>: <SlugError>`; an unreadable folder → every name `unmapped: <name> — strategies folder not readable`. Nothing here fails the build.

The build stores the names, the title → slug list it read, and the resolutions on each `build_trade` row (L57); the summary counts the unmapped names.
