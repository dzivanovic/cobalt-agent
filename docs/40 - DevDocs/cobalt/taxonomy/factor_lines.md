# `src/cobalt/taxonomy/factor_lines.py`

## What it does
Reads and edits the `quality_factors:` block of a strategy note's Definition unit **by line**, so a change to one factor leaves every other byte of the note — comments, spacing, order — exactly as the trader wrote it. Shared by the two S2-P2 note changes: the catalyst batch (`taxonomy/catalyst.py`, R10) and the trail_fit draft (`cards/trail_fit_draft.py`, R5).

## Key functions/classes
- `factor_block(lines) -> FactorBlock` finds the unit's fenced YAML, its single `quality_factors:` key and every item under it. The item indent is whatever the note uses (`    - x` as the shipped example writes, `  - x` as a YAML dumper writes). An item is its `- ` line plus every deeper-indented line after it (a block mapping); blank and comment lines belong to no item. Each item is parsed on its own with `yaml.safe_load` to read its name (bare string, flow mapping or block mapping).
- `FactorBlock.names`, `FactorBlock.item(name)`; `FactorItem` carries name, start/end line, the lines and the parsed value.
- `append_factor(lines, text)` inserts one item after the last, at the block's item indent.
- `remove_factors(lines, names)` deletes the named items' lines; nothing else moves.
- `replace_factor(lines, name, text)` swaps one item for a single line.

## Refusals (`FactorLinesError`)
No closed fence; zero or two `quality_factors:` keys; a flow-style list on the key line (editing it would mean rewriting his line); no items; an item that does not parse or has no name; any line inside the block it cannot classify.

## Config it reads
None.
