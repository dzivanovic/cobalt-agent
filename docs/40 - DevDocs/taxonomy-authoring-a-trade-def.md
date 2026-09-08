# Authoring a trade_def

**Where a strategy lives, what a note must contain, and what the loader
does with it.** Companion to `src/cobalt/taxonomy/vault_loader.py`;
ruled by [ADR-0008](../10%20-%20Decisions/ADR-0008-two-layer-data-model.md) D3.

The worked example this page walks through is a real, loadable file:
`configs/cobalt/taxonomy/examples/example_trade_def.md`. It is the only
trade_def the repo ships, it is synthetic (anatomy terms only — no trade
name, no cheat-sheet rule), and it is the test suite's fixture. If the
shape of a strategy note ever changes, it changes there first.

---

## 1. The note is the truth

A trade_def lives in **one** place: a note in your vault, under

```
1 - Trading/4 - Strategies/<Your Trade Name>.md
```

There is no copy in the Cobalt repo, and there is no way to author one
there. `"user".trade_defs` in the database is a **loaded copy** — read
from the note, validated, written by `cobalt taxonomy load`, and deleted
again the moment the note stops producing it.

That is the whole of the one-path rule applied to strategies. Before
ADR-0008 the same 13 defs existed as committed YAML *and* inside these
notes, and the first edit to either copy would have made them disagree
with nothing to say which was right.

**Your strategies are yours.** They are user data (L32): never shipped to
another Cobalt user, never committed here.

---

## 2. What a note must contain

Four things. Everything else in the note is yours and Cobalt never
touches it.

### 2.1 Frontmatter: the identity

```yaml
---
trade_def: example-range-break     # THE ID
name: Example Range Break          # THE DISPLAY NAME
class: scalp                       # checked against the def
family: [range_break]              # checked against the def
status: defined                    # checked, never trusted
---
```

- **`trade_def:` is the id.** Lowercase kebab: `[a-z][a-z0-9]*(-[a-z0-9]+)*`.
  No `$`, no leading digit, no underscores, no spaces. A name may be
  spelled however you like; an id may not, because it is matched, joined
  and put in URLs. `9 EMA Scalp` → `nine-ema-scalp`.
- **`name:` is the display name** and it wins over anything the YAML used
  to call the trade. Where an old YAML name differed, it belongs in the
  def's `aliases[]`.
- **`status:` is derived, not obeyed.** The loader sets `defined` if the
  unit validated and `draft` if it did not, then tells you when your
  frontmatter disagrees. **`playbook` is refused outright**: a playbook is
  earned at n ≥ 30 (R3), never typed.
- **`class:` / `family:` are checked, and you win.** A mismatch is a
  listed warning; the loader corrects nothing.

### 2.2 The definition unit

Inside the `definition` section, a unit whose id is `trade_def:<slug>`,
holding one fenced YAML block:

````markdown
## Definition
<!-- cobalt:section definition -->
<!-- cobalt:unit trade_def:example-range-break -->
```yaml
trade_def:
  family: [range_break]
  class: scalp
  valid_setups:
    - {setup_ref: range_break, relation: with_trend}
  ...
```
<!-- /cobalt:unit trade_def:example-range-break -->
<!-- /cobalt:section definition -->
````

**No `id:` and no `name:` in the YAML.** The frontmatter owns both and the
loader injects them; a unit that authors either fails loud. Refusing
rather than preferring one is deliberate — if the two ever disagreed,
every tie-break silently discards something a human wrote.

The unit id must match the frontmatter slug. Prose outside the fence is
yours; the loader reads the fence only.

### 2.3 The tunables unit (optional)

A **second** unit in the same section, for your own per-trade numbers:

````markdown
<!-- cobalt:unit tunables:example-range-break -->
```yaml
tunables:
  - key: example_range_break.range_duration_band
    value: [4, 20]
    unit: min
    scope: per_trade(example_range_break)
    dynamic: true
    status: proposed
    source: ruling
```
<!-- /cobalt:unit tunables:example-range-break -->
````

Two units and not one, on purpose: replay writes a row's `status`, and a
`status` write that had to re-render the definition unit would rewrite
your def and every comment inside it.

- **`scope` must be `per_trade(<trade_key>)`**, where `trade_key` is the
  slug with hyphens turned into underscores. Kebab is illegal in the
  `cfg()` key grammar, and `example-range-break.band` would read as
  subtraction to a predicate parser.
- **A row here may only ADD a key.** Shadowing an engine key from
  `configs/cobalt/taxonomy/tunables.yaml` is a loud collision, not an
  override: the engine row is what every Cobalt install runs on.

### 2.4 The stats unit

```markdown
## Stats
<!-- cobalt:section stats -->
<!-- cobalt:unit stats:example-range-break -->
n: insufficient data (n<30)
<!-- /cobalt:unit stats:example-range-break -->
<!-- /cobalt:section stats -->
```

Cobalt owns this unit. Below n = 30 it says so, because a number without
its sample size is not a number (sample-size law).

---

## 3. Draft, defined, or broken

The loader makes exactly one interesting distinction, and it is the
reason you can leave a strategy half-written:

| the definition unit is | the loader says | you get |
|---|---|---|
| empty | **draft** | listed with a reason, no error |
| a partial mapping (e.g. only `valid_setups`) | **draft** | listed, with the missing fields named |
| complete but invalid | **error** | the note, the field, and what is wrong |
| complete and valid | **defined** | a row in `"user".trade_defs` |

A draft is not a failure. A def you believe is finished and is not, is.

The "complete" test is not a hand-maintained list — it is derived from
the `TradeDef` model's own required fields, so a new required field joins
it automatically.

---

## 4. Loading it

```bash
cobalt taxonomy load --dry-run     # read, report, write nothing
cobalt taxonomy load               # ... then sync
cobalt validate                    # the same report, inside the config gate
```

`--dry-run` first, always. `sync()` is a **replace**: a slug that has left
your vault has its row deleted, and its per-trade tunables with it. That
is the correct semantics — a def you removed from a note is a def gone
from the system — but it is not something to discover from a row count
afterwards. The apply names every slug it deleted.

What lands where:

| object | what it holds |
|---|---|
| `"user".trade_defs` | `slug`, `name`, the validated `def` as JSONB, the unit's `md5`, the `note_path` |
| `"user".tunables` | your per-trade rows, cascade-deleted with their def |
| `"user".setup_trade_matrix` | a **view** unnesting `valid_setups` — it cannot disagree with the def |

---

## 5. Renaming, moving, deleting

- **Renaming the display name** — edit `name:`. Nothing else changes; the
  old name belongs in `aliases[]` if anyone still calls it that.
- **Renaming the slug** — it is the identity, so this is a migration, not
  an edit: trade notes referencing the old slug, the unit ids, the
  `tunables` keys and scopes all move with it. Prefer an alias.
- **Moving a note** — the row's `note_path` updates on the next load.
- **Deleting a def** — delete the unit's contents (it becomes a draft) or
  the note (the row is deleted). Either way, run `taxonomy load`.

---

## 6. Where the rules live

| you want to know | read |
|---|---|
| the slug shape and `trade_key()` | `src/cobalt/taxonomy/slug.py` |
| every field a def may carry | `src/cobalt/taxonomy/trade_def.py` |
| draft/error, status, warnings | `src/cobalt/taxonomy/vault_loader.py` |
| the tables and the view | `src/cobalt/taxonomy/migrations/0001_trade_defs.sql` |
| why any of it is this way | `docs/10 - Decisions/ADR-0008-two-layer-data-model.md` |
