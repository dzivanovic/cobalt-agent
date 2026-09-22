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

**2026-09-21 — setups one build STEP-2: the dedicated reader.**
`load_assumed_tunables(vault_root, loaded_slugs=)` reads the ONE unit
`tunables:assumed`, inside `<!-- cobalt:section assumed -->`, of
`ASSUMED_NOTE = "1 - Trading/Assumed Defaults.md"`. The note sits
OUTSIDE the Strategies folder, beside the list-config note ([R2F-07]).
**An absent note means no assumed rows, not an error.** Every row must:
- validate through `TunableRegistry`;
- carry scope `global` or `per_trade(<a def loaded in this pass>)`.
  `per_indicator(...)` is REFUSED, as the settled reader words it. That
  is F1, NOT widened, so the three per-indicator holes stay null;
- read `source` `assumed` or `ruling`.

A `global` row's `LoadedTunable.slug` is None; `slug` is now optional.
`load_vault_trade_defs` APPENDS these rows to `user_tunables`, the same
list `_resolve_every_cfg` merges and `TaxonomyStore.sync` writes and
prunes. One key supplied twice is refused with both paths named. The
strategy-note reader `_read_tunables_unit` refuses `source: assumed`, so
the mark has one home.

**2026-09-22 (fix round 3, F2 — R48, F1 WIDENED).** `load_assumed_tunables`
now also accepts a `per_indicator(<ind>)` row, but ONLY for a key whose
committed engine row (`load_tunables()`) carries that same scope and
`value: null` — a hole. Any other `per_indicator` row is refused, naming
why: no engine row, the engine row's scope differs, or the engine row
carries a value. Such a row has no def (`slug` None, like a `global` one);
`merge_tunables` then fills the hole by its existing rule (same scope, same
unit, source assumed or ruling). The three holes this opens are
fashionably-late's two flat thresholds and vwap-continuation's
`dist.k.vwap`; committed config keeps all three null — their values are
proposed in a gitignored file and written into the note by the desk.
