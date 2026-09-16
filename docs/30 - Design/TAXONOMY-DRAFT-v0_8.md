# Trading Taxonomy — Draft v0.8
S2-P2 fold 2026-09-16. Amendment layer over v0.7: **every v0.7 section not restated here carries forward unchanged** (and, through it, v0.4–v0.6 as v0.7 describes). Schema **v0.5** in code (`trade_def.SCHEMA_VERSION = "0.5"`); the loader enforces **0.4** until STEP-D4 (`trade_def.LOADER_SCHEMA_GATE`). Status: rulings R1–R11 of 2026-09-15 (plan `docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md`) are **RULED**; items marked DwV are decided with veto in that plan.
Legend as v0.7.

---

## Change log v0.7 → v0.8

| # | Change | Source | Status |
|---|---|---|---|
| 1 | `catalyst` joins the standard quality factors (`setup_relation`, `market_alignment`, `sector_alignment`, `catalyst`) at schema 0.5 | 2026-09-15 R10; 09-14 group-2 ruling | RULED |
| 2 | Schema 0.5 ships behind a loader gate that stays 0.4 until every defined note carries `- catalyst` (batch apply re-read), flipped in code at STEP-D4 | R10; plan §6 STEP-D4 | RULED |
| 3 | The notes migrate through ONE review file + ONE batch apply bound to the file's sha256 and each Definition unit's sha256; a `catalyst_*` factor is removed only where marked `drop` | R10; Astra R1-17 | RULED |
| 4 | §10.5 `expr` strings are parsed at load into a typed AST; a note that does not parse fails loud with note path + line + slug; the notes are never edited to fit the parser | R3; Astra R1-4 | RULED |
| 5 | `required_atoms(ast)` names what a detector must supply; a def whose atoms are not all served renders "not evaluable: missing atoms […]", never a card | R2 | RULED |
| 6 | Dot roles `shadow` · `live` · `human`; every computed dot is `shadow` through S2 and rendered hollow; conviction counts taps only | R6 | RULED |
| 7 | Extension path B is not evaluable in S2 (catalyst unknown); only path A forms | R4 | RULED |
| 8 | A card formed before its def gained a factor gains that dot once, untapped, recording the definition md5 and run that added it; formation evidence is never rewritten | Astra R2-4 | DwV |

## 10. Trade layer — schema v0.5 (amends v0.7 §10)

### 10.1 `trade_def` registry — amended line
```
  quality_factors[]: → card dots; always includes setup_relation, market_alignment, sector_alignment
                     and, from schema 0.5, catalyst;
                     tape-class factors carry source: human (frontier) [v0.7 A.12];
                     each item a bare name (source: human, tier: judgment) or a mapping
                     {name, source: cobalt | cobalt-degraded | human, tier: deterministic | judgment,
                      why_template, status, frontier}   (ADR-0008 D3 b.2)
```
`catalyst` as authored is a bare `- catalyst`. Its dot is desk-graded: shadow, `source: cobalt-degraded`, N/A `DESK_NA` until the desk supplies a grade (S3). Existing `catalyst_grade` / `catalyst_polarity` / `catalyst_class` factors are the trader's and stay unless his review row says `drop`.

**The migration (R10).** `cobalt taxonomy catalyst-review` drafts one row per defined note — note · proposed `- catalyst` line · existing `catalyst_*` factors · `keep` — and records each Definition unit's sha256. He marks each row `keep`, `drop` or `drop: <factor>, …`. `cobalt taxonomy catalyst-apply --review <file> --sha256 <hash>` refuses on a changed file, preflights every unit before writing any (a drifted unit refuses the batch), writes each through the L28 vault writer, and re-reads every unit at schema 0.5 before it reports the gate ready. An interrupted batch resumes: applied units are recognised, not rewritten.

### 10.5 IF/Then condition grammar — PARSED (amends v0.7 §10.5)
The grammar is unchanged in meaning; it is now a parser (`src/cobalt/taxonomy/predicate.py`), inventoried against every `expr` position of every defined note before it was written (Astra R1-4):

```
expr      := or
or        := and (OR and)*
and       := not (AND not)*
not       := NOT not | qualified
qualified := relation ( (on|after|against) additive | between additive and additive )*
relation  := additive [ cmp additive | IN (set | additive) | (touched|near|close_through|inside) additive ]
additive  := term (('+'|'-') term)*
term      := unary (('*'|'/') unary)*
unary     := '-' unary | postfix
postfix   := primary [unit]                    unit: min bars days sec pct atr cents
primary   := number | string | null | cfg(key) | event(name, args…) | '{' additive, … '}' | '(' expr ')' | [that] ref
ref       := segment ('.' segment)*
segment   := ident [ '(' [arg (',' arg)*] ')' ]
arg       := [ident ':'] (words | expr)
cmp       := == != >= <= > <
```

The AST is frozen and typed; it is derived from `expr`, so it never enters the stored def or its md5. **Atoms** are the outermost references, every `event(…)` and every relation/qualifier word; `cfg()` keys, numbers and enum symbols are not atoms. Evaluation is three-valued: an atom the detectors could not measure is UNKNOWN, never false.

### 10.7 Dot rendering on the card (new)
| role | computed by | counts in conviction | face |
|---|---|---|---|
| `shadow` | engine (computed factors, desk factors) | no — until a curve tribunal + an L7 promotion | hollow, engine grade shown as `shadow n`, tappable 1–10 |
| `live` | engine, promoted | yes | filled with the engine grade |
| `human` | the trader | yes, once tapped | hollow until tapped, never a neutral 5 |

A tapped dot fills with his grade; the engine grade at tap time is stored beside the tap (`"user".card_dot_taps.engine_grade_at_tap`) and is the pair the shadow report scores (§12.2 below). Every field on the card carries its owner badge (`COBALT` · `YOU` · `LEDGER`).

## 12. Population plan — addendum
### 12.2 Shadow promotion evidence (new)
`cobalt cards shadow-report [--since]` reports, per factor, trading sessions with pairs, pairs, median |tap − engine| over all pairs and the share within 2, against the trader setting `card.shadow_promotion_bar` (09-14 group-2 ruling: 10 sessions, 30 pairs, median ≤ 1, within-2 ≥ 0.90). It prints GATE MET / NOT MET and flips nothing: promotion is a trading-logic change (L7).
