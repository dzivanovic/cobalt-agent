# `src/cobalt/taxonomy/vault_loader.py`

## What it does
Reads every strategy note in `1 - Trading/4 - Strategies/` and returns
the validated defs, the drafts, the trader's per-trade tunable rows, and
a list of frontmatter warnings. ONE PATH: vault unit → this loader →
`"user".trade_defs`.

## Key functions/classes
- `load_vault_trade_defs(vault_root=None) -> VaultTradeDefs`.
- `LoadedTradeDef` — slug, name, vault-relative `note_path`, `md5` of the
  unit's YAML text, and the `TradeDef`.
- `REQUIRED_UNIT_FIELDS` — derived from the model, not hand-listed, so a
  new required field joins it automatically.

## Draft vs error — the distinction this module exists to make
An EMPTY unit, or one holding only a partial mapping, is a DRAFT: listed
with its reason, never an error, because a trader mid-way through writing
a strategy must not break the loader. A unit with the FULL shape that
then fails validation IS an error, named by note and field: that is a def
someone believes is finished and it is not.

## Checked, never trusted
`status` is DERIVED (`defined` iff it validated) and the frontmatter is
compared to it; `playbook` is REFUSED — earned at n ≥ 30 (R3), never
typed. `class`/`family` drift is a warning and THE HUMAN WINS: this is a
read path and it corrects nothing.

## Gotchas
A predicate that does not parse (S2-P2 R3) fails the def like any other
validation error. `_locate_predicate_errors` puts one line per bad
expression IN FRONT of the error: `<note>:<line> (trade_def:<slug>):
predicate syntax error at column N …`. The line is found by searching
for the expression text inside the unit's own line range. If YAML
escaping hides the exact text, the unit's opening marker line is named
instead, and the error is still reported.

Two units per note, on purpose: replay writes a tunable row's `status`,
and a status write that re-rendered the definition unit would rewrite the
def and every comment in it. A per-trade row must carry scope
`per_trade(trade_key(slug))`; a row shadowing an engine key is a loud
collision, not an override.
