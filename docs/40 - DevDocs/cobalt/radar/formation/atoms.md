# `cobalt.radar.formation.atoms` — ATOMS, RELATIONS and the one shape walk

Added 2026-09-21 in STEP-2 of the setups one build (FINAL §2.5, §4, §7 R2-2.2 B).

- **`AtomValue`** is the value of one atom as the Frame measured it. It moved here from `evaluate.py`, which still re-exports it.
- **`ATOMS`** holds one `AtomResolver` per served atom. A resolver declares:
  - the value kind;
  - for a symbol, its **producible domain** (`Extension.state` is `{culminating, none}` today);
  - `price`: its number is a price, negated back before publication (X12);
  - `tunable_keys`: its detector's `TUNABLE_KEYS` (term (2) of the closure);
  - `conventions`: the conventions it implements (term (3)).
- **`RELATIONS`** has no entries yet. A word it does not serve is named missing.
- **`predicate_gaps(node)`** is the one walk of a predicate's shape. The registry uses it, and it mirrors what `evaluate_node` can evaluate, so the two agree (E9, proved over the corpus). It names:
  - an unserved atom, verbatim;
  - an unserved relation word;
  - `Unsupported(<kind>)` for a shape the interpreter cannot evaluate, such as Arith, a Quantity, or `IN` against something that is not a set;
  - `<atom>∌<value>` for a symbol compared to a value outside its atom's domain (E8).

The atom values themselves are computed by `anatomy/frame.py`. This table only says what is served.
