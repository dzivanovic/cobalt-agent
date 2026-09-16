# `src/cobalt/taxonomy/predicate.py`

## What it does
Parses the §10.5 IF/Then condition strings (`Predicate.expr`) into a frozen Pydantic AST (S2-P2 ruling R3). It runs at `TradeDef` validation, so a def that loads is a def whose every expression has a tree. The vault notes are never edited to fit the parser.

## Key functions/classes
- `parse_predicate(expr) -> Node` is a tokenizer plus a recursive-descent parser. Precedence runs, lowest first: `OR` < `AND` < `NOT` < qualifiers (`on`/`after`/`against`, `between … and …`) < relations (`== != >= <= > <`, `IN {…}`/`IN cfg(…)`, `touched`/`near`/`close_through`/`inside`) < `+ -` < `* /` < unary `-` < unit postfix (`min bars days sec pct atr cents`).
- The AST nodes form a discriminated union on `kind`: `Number`, `String`, `Null`, `Symbol`, `Cfg`, `Words`, `Quantity`, `Ref` (dotted `Segment`s with optional call `Arg`s, named or positional), `EventAtom`, `SetLiteral`, `Arith`, `Negate`, `Compare`, `InTest`, `Relation`, `Qualified`, `Between`, `Not`, `And`, `Or`.
- `render(node)` produces canonical text; `parse_predicate(render(ast)) == ast` is tested for every inventoried form.
- `required_atoms(node)` returns every outermost reference (a call counts as one atom), every `event(...)` and every relation or qualifier word. `cfg` keys, numbers and symbols are not atoms. `radar.anatomy.registry` subtracts what S2 serves, and the difference is the "missing atoms" list.
- `PredicateSyntaxError` carries `expr`, a 1-based `column` and a `reason`.

## Why the grammar is this wide
Astra R1-4: parsing runs for EVERY loaded def, so a grammar missing one live form fails the whole taxonomy on first run. The inventory covers `IN cfg(...) min`, function calls, named arguments, `/`, `touched`, `on`/`after`/`inside`, nested calls and `!=`.

## Gotchas
- A bare word right of `==`/`!=` or inside `{}` becomes a `Symbol` (an enum value such as `culminating`), never an atom.
- A relation or qualifier word followed by `(` is an ordinary call, so `touched(Leg(pullback), VWAP)` parses.
- `AND`/`OR`/`NOT`/`IN` are accepted all-caps or all-lower, never mixed case.
- `cfg(` is lexed as one token and its key is checked against `CFG_KEY_RE`. Whether the key EXISTS is checked by the loader's `resolve_cfg`, not here.
- `event(name, …)` names are checked against `trade_def.Event`.
- The note path and line number are added by `vault_loader._locate_predicate_errors`, not by this module.
