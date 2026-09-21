BLIND: I did not read the round-2 folder or the round-2 hub's report.

# Setups tribunal — Fable seat, round 2 (2026-09-21)

Seat `setups-tribunal-fable-r2-0921` · Fable 5.1 · read-only, one file written (this one). Authorization verified before any reading: R20 row `cto-2026-09-21.md:31` carries both required strings; R20 wording committed at `30ae6c9`; the derive's stop line and v2 committed at `fd33ab5`; all seven allow strings and three deny strings count 1 in `22-draft-setups-tribunal.md`. R20's bound read as covering a round-2 ruling of the same tribunal by the same seat. L32: his notes are cited by `note:line`, assumed values by KEY only; no value, quote or wording of his is in this file.

## DIGEST FOR THE DESK

TRIBUNAL R2: BUILD AFTER the derive folds R2-2's untappable dot into C1 and R2-3's migration into C2

I attacked my own round-1 text first, in the code. 8 of 12 are NEITHER; in every one of the 8 something of mine failed on a file (a broken mechanism, an unrun claim or an omission). Grok's PRINCIPLES mostly held (never lifts; scope equality); its MECHANISMS broke on writers it did not name.

- **R2-2.1 NEITHER** — Grok's principle (suppressed for the card's life) on my carrier (one dot), made UNTAPPABLE in `tap_dot`; existing `suppression()` then holds on all five recompute paths. Grok's stored string dies on the first tap (`store.py:1215-1224`).
- **R2-2.2 NEITHER** — static closure, computed once at formation: `iter_cfg_tokens(def)` + detector `TUNABLE_KEYS` + `ASSUMED_CONVENTIONS`; my "existing pattern" was one module.
- **R2-2.3 NEITHER** — C1 marks `A-01` with that dot from a module constant; no store, column, closure or migration in C1.
- **R2-2.4 FABLE'S** — no: `AtomOutcome` is closed (`seam.py:99-117`); the key rides the dot.
- **R2-2.5 NEITHER** — X8 passes by construction and is re-worded to include a tap; ORDER BY unchanged; every card of the seven is null-scored until its rows are ruled — said plainly, not a L52 (b) breach.
- **R2-1 NEITHER** — no `Direction(unbound)` refusal (dead under F-04, else refuses two of seven); `both_sides` + X7 as a gate of each unlocking chunk.
- **R2-3.1 NEITHER** — note outside the Strategies folder, read INTO `user_tunables`; **needs a migration**: `tunables.slug` is NOT NULL FK (`0001_trade_defs.sql:63`) and the radar merges from the DB — both seats missed it.
- **R2-3.2 NEITHER** — four clauses, row fields only: engine `value is None` · `source ∈ {assumed, ruling}` · scope equal · unit equal.
- **R2-3.3 FABLE'S** — the mark follows `source` only.
- **R2-4.1 NEITHER** — per-card decisions read the card's OWN side (`by_side`); my ranking would expire a short card on the long side's avoid (`evaluate.py:1342`); neither forms → long frame, always.
- **R2-4.2 FABLE'S** — observations once, on the real bars. · **R2-4.3 FABLE'S** — daily series mirrored too (`daily.py:182`).

Own round-1 wording withdrawn: **11** (table below) — all inventions or un-walked consequences. Experiments: 7 (X8 re-worded, X7 re-placed, X12 widened, X18–X21 new). Owner items (after cards): 4. ESCALATE: 2 — C2 ships a migration whatever R2-2 rules; C1 now touches `cards/store.py`.

## Rulings

### R2-2.1 — permanent persisted suppression, or a tappable dot?

**SELF-ATTACK (my O4 paste).** Two failing scenarios, both read in the code, both fatal to my text.
1. *One tap makes the mark a source of conviction.* `conviction()` is the mean of every dot's `trader_grade` (`scoring.py:238-244`); `proposed_key` follows conviction whatever the suppression (`scoring.py:273-286`, `:332`). A rubberband card, curves set, nothing tapped: he taps my `assumed_formation` dot high to clear it. Conviction now rests on that one grade, `card_score` = proximity × 100, the proposed key is the top band — the assumed mark RAISED the score and the size recommendation, and no factor of his own def was graded. "Degrades the score accordingly" (L52 a) is not what the files do with my wording.
2. *It fails X8.* My (d) said the dot "is recomputed each scan like every other dot". `refresh_dots` emits only the factors present in `fresh` (`scoring.py:216-224`): when the row's `source` later reads `ruling`, a closure recomputed from live rows drops the dot, `suppression()` returns None and the OPEN card — whose trigger and stop were formed on the assumed value (`refresh_card` docstring, `evaluate.py:770-773`: formation evidence is never touched) — gains a score. Grok's objection to a mark that can lift HOLDS.

**NEITHER —** "An assumed formation is marked by ONE dot and its score is suppressed for the life of that card through the EXISTING `suppression()`. One helper in `evaluate.py`, `card_dots(ld, ev, settings, at, assumed_keys)`, replaces the bare `compute_dots` call at all four sites (`evaluate.py:774`, `:1077`, `:1383`; `audit_export.py:362`): it returns `compute_dots(...)` and, when `assumed_keys` is non-empty, appends `Dot(factor="assumed_formation", position=len(quality_factors), source="cobalt-degraded", tier="deterministic", role="shadow", na_reason="ASSUMED", engine_inputs={"assumed_keys": [...]}, engine_why="formed on assumed defaults: <keys>")`. `NaReason` (`scoring.py:72`) gains `"ASSUMED"`. `Formation` gains `assumed_keys: tuple[str, ...]`. At creation the keys come from the formation; at refresh they come from the card's OWN stored dot and at replay from the receipt's card entry (one new list beside `taps`, `evaluate.py:1425-1427`) — never from live tunables, so a row ruled later does not lift an open card. `CardStore.tap_dot` refuses the factor `assumed_formation` beside its existing no-such-dot refusal (`store.py:1200-1204`): an assumed default is ruled on the settings surface, never graded on a card. The dot therefore never carries a `trader_grade`, never enters `conviction()`, and `suppression()` (`scoring.py:247-251`), logic unchanged, returns a reason on EVERY path that recomputes it — create, `refresh_card`, `tap_dot`, replay, audit export. Its reason text drops '(tap to grade)' when every blocker is `ASSUMED`. No stored-string special case, no `assumed_keys` column, no view change, no migration, no change to `conviction`, `card_score` or `score_card`. A card formed after the row reads `source: ruling` carries no dot and scores as today."

- Grok's text fails on a writer it does not name. `tap_dot` recomputes `suppressed = suppression(dots)` and writes it with `card_score` (`store.py:1215-1224`). Scenario: rubberband card created with the stored string; he taps `setup_relation`; the string is overwritten, a score is written, the mark is gone; the next `refresh_card` — told not to overwrite — keeps it. That is the L52 (a) hole Grok charges to my text, reached on the first tap.
- Second Grok failure: replay recomputes `score_suppressed` from dots and compares it with the published value (`evaluate.py:1077-1088`, `:1033`); a string no dot explains makes every assumed card a replay mismatch, and `audit_export.py:362-374` shows the other house a candidate score the card does not have (L52 d).
- Grok's PRINCIPLE (never lifts on that card) is right; my CARRIER (a dot) is right because all five recompute sites already go through `suppression(dots)`. `card_dots`: `factor` and `na_reason` are free TEXT, uniqueness is `(card_id, factor)` (`0007_radar_cards.sql:122`, `:132`, `:136`); the panel renders any `na_reason` string (`radar_panel.py:289`, `:894-895`).
- Price: `evaluate.py` (helper, `Formation` field, receipt entry, replay read), `scoring.py:72` + the reason text, `store.py` (two lines), `audit_export.py:362`. About 40 lines + tests. Chunk C1. No migration.

**WITHDRAWN:** "his tap lifts it and his grade enters conviction like any other tap" (O4 paste) — `scoring.py:238-244`, `:273-286`. · "It is recomputed each scan like every other dot" ((d) reasoning) — `scoring.py:216-224`, X8.

### R2-2.2 — a runtime recorder around every read, or a static declared-key closure?

**SELF-ATTACK (my (d) paste).** "Every atom resolver, detector, trigger resolver, stop resolver and relation resolver declares `tunable_keys` — the existing pattern at `extension.py:40-44`" is not what the files show. `TUNABLE_KEYS` is ONE module constant of the Extension detector (`extension.py:40-44`, read at `:56`); a search of `src/cobalt` finds no other resolver, trigger or stop that declares keys (the only like-shaped constant is the health thresholds' `HEALTH_KEYS`, `cards/health.py:65`, not a resolver). And today's trigger and stop do not own a key at all: the key is named by the DEFINITION (`trigger_def.params["bars_cleared"]`, `placement.buffer.cents.value` through `_cfg_value`, `evaluate.py:653`, `:656`), and the function that already lists those statically is `iter_cfg_tokens` (`loader.py:139-153`) — I invented a declaration where a scanner exists. What held: `TunableUnit.LABEL` exists and `TunableRow.value` is `Any` (`tunables.py:40`, `:89`), so a convention CAN be a label row; `TunableSource` has no `assumed` today (`tunables.py:63-66`).

**NEITHER —** "`assumed_keys` is computed ONCE, at formation, as a static closure of the definition, and stored on the card's dot (R2-2.1); nothing records reads at run time. The closure is the union of three sets: (1) `iter_cfg_tokens(definition)` (`loader.py:139-153`) — every `cfg(<key>)` the def itself names, trigger params and stop buffer included; (2) the `TUNABLE_KEYS` module constant of every detector that serves an atom the def's preconditions or avoids name (`extension.py:40-44` is the one instance today and becomes the rule: a detector's `from_tunables` reads only keys in its own `TUNABLE_KEYS`, proved by a test that builds it from a mapping holding those keys alone); (3) `ASSUMED_CONVENTIONS`, a module constant beside each resolver or branch that implements a convention (`A-01` beside the direction branch, `A-13` beside the catalyst resolver, …). `assumed_keys` = the closure's keys whose resolved row reads `source: assumed`. From C2 every convention is ALSO a row (unit `label`, value = the name of the rule the code implements); the code refuses a label it does not implement (`not_evaluable`, named) and a declared convention with no row is a loud load error. Until a convention has a row (C1) it counts as assumed unconditionally."

- Grok's recorder cannot attribute a detector's read to a def. Detector params are built before any atom is consulted (`ExtensionParams.from_tunables`, `evaluate.py:528`, ahead of `consulted` at `:604`), and `consulted` tracks atoms, not keys. Scenario, from C3b on: a Range detector built the same way reads `A-03` / `A-04` for every member; a rubberband card (it names no Range, carries `A-01` alone) lists them; after he rules `A-01` its cards stay suppressed for keys they never rested on. Scoping the recorder to consulted atoms needs the atom → detector → keys map — the static declaration.
- The conventions are not reads, so Grok's text already needs a static flag for them ("assumed resolver"): two mechanisms where one does all 23.
- Wrapping the mapping instead of the functions fails on the code as written: `resolve_cfg(key, dict(tunables), …)` copies every row (`evaluate.py:421`, `:602`).
- A static closure over-reports a short-circuited branch of the def's OWN predicates only — the safe direction, and the same set `--assumed` needs for its consumers column.
- Price: `evaluate.py` (closure function, ~25 lines), one constant per detector / convention site, one test per detector. Chunk C2 (C1 uses set (3) alone). No migration.

**WITHDRAWN:** "— the existing pattern at `extension.py:40-44`" and, with it, "trigger resolver, stop resolver … declares `tunable_keys`" ((d) paste) — grep of `src/cobalt`; `evaluate.py:653`, `:656`; `loader.py:139-153`.

### R2-2.3 — which chunk marks `A-01` on the Rubberband card, and with what?

**SELF-ATTACK.** Under my round-1 text C1 CANNOT mark `A-01`: my mark needed the closure, and my closure needed `A-01` to be a label row in a store that only exists from C2. I ruled "C1 needs nothing from C2" ((h)) and left C1's own card unmarked — the L52 (a) hole both hubs escalated sits in my text too.

**NEITHER —** "C1 marks `A-01` with the R2-2.1 dot. `ASSUMED_CONVENTIONS = ("A-01",)` is a module constant beside the direction branch (`evaluate.py:635-647`); every C1 formation carries `assumed_keys = ("A-01",)`; the card is created with the `assumed_formation` dot, its score suppressed, the key readable on the dot's `engine_inputs` and in its `engine_why`. C1 ships `NaReason` + `ASSUMED`, the `card_dots` helper at the four sites, the `tap_dot` refusal and the receipt entry. C1 has no store, no closure, no column, no migration and no panel change. C2 replaces the unconditional constant with the closure of R2-2.2."

- Grok's C1 sentence ("rubberband still sets `score_suppressed = assumed_formation`") fails by the R2-2.1 scenario (`store.py:1215-1224`), and in C1 it puts no KEY on the card: the face says a formation is assumed and cannot say of what until C2's chip.
- The dot needs nothing C1 lacks: `0007_radar_cards.sql:118-137` takes it as is; `radar_panel.py:894-895` prints `n/a ASSUMED`.
- Price: inside R2-2.1's ~40 lines; C1 stays S logic + M gates. `EVALUATOR_VERSION` is bumped by C1 already (v2 §1 Files).

**WITHDRAWN:** none beyond R2-2.1 / R2-2.2 (an omission, not a false sentence).

### R2-2.4 — can `A-13` be marked on the atom at all?

**SELF-ATTACK (my O8 paste, WF5).** Walked: `_Closed` sets `extra="forbid", frozen=True` (`seam.py:99-100`); `AtomOutcome(_Closed)` (`:111-117`) declares `atom`, `value_kind`, `boolean`, `number`, `symbol`, `unavailable` and nothing else; `_one_value` (`:124-138`) demands exactly the slot `value_kind` names. Path B: `extension.py:140-144` emits `catalyst_ref_unknown`, `evaluate.py:620-622` turns it into `not_evaluable` / `B_only` — both as I cited. `catalyst_ref` appears in `src/cobalt/radar` ONLY as that Extension reason (grep: `seam.py:49`, `evaluate.py:620`, `extension.py:10`, `:12`, `:84`, `:143`), so a def-level `catalyst_ref` precondition atom is new code and the scoping sentence describes something separable. None found against the paste; its two cross-references now read "`ASSUMED_CONVENTIONS`" (R2-2.2) and "the R2-2.1 dot".

**FABLE'S**
- No: `AtomOutcome(…, assumed="A-13")` is an extra field on a forbid model, constructed inside `detail()` (`evaluate.py:588-592`). Scenario: nine-ema-scalp's first evaluation after C5 raises in `detail()`, not a refusal — unless the seam model changes, which v2's L52 (c) row and ADR-0009's audit bundle would then have to version.
- Grok's "Mark A-13 on the atom" buys nothing the dot does not already carry: the key reaches the card in `engine_inputs.assumed_keys`, and the atom's stored outcome stays an honest `boolean`.
- Smaller: zero seam change. X9 (round 1) stays the permanent test of the closed model.

**WITHDRAWN:** none.

### R2-2.5 — does the winner pass X8, and does WATCH stay ordered by `card_score`?

**SELF-ATTACK (my O4 scenario and my (c)(b) paste).** I wrote that a suppression that never lifts "contradicts ADR-0009 D4" and that (b) "holds only with the O4 dot". The files do not bear that out. `ADR-0009:28` names `card_score` the only number that orders WATCH, and the committed `TIE_POLICY` (`evaluate.py:134-138`) already orders null-score WATCH cards by `pool_position` — the state EVERY card is in today until he taps (`conviction` None → `card_score` None, `scoring.py:264-266`). A longer-lived null adds no second authority to the code; it extends a state the ratified policy already handles. My two-card scenario is real, but it is the PRICE of L52 (a), not a breach of L52 (b).

**NEITHER —** "X8 passes by construction under R2-2.1: the open card's dot is carried from its own stored row, so changing the row's `source` to `ruling` cannot lift it; X8's assertion is re-worded to the mechanism — 'the open card still carries the `assumed_formation` dot, `card_score` is null and `score_suppressed` names `assumed_formation`, after a refresh AND after a tap on another dot' (the tap is the path that breaks a stored string). WATCH's ORDER BY is unchanged: `card_score desc nulls last, pool_position nulls last, ticker, card_id`. Stated plainly on the design's face: until he rules a row, every card of a def whose closure holds it has a null score and is ordered by the tie policy; conviction, the proposed key, proximity and shares are still computed and shown (`scoring.py:329-336`). The first card he can make score is rubberband's, by ruling `A-01` alone."

- My own tappable dot FAILS X8 (R2-2.1 self-attack 2). Grok's stored string passes X8 as literally worded (refresh only) and fails the tap path X8 does not exercise — hence the re-wording.
- Neither seat's text says the plain consequence; v2 leaves it "OPEN inside R2-2" (L52 table row (b)).
- Price: a test and two sentences. Chunk C1 (the tap half) and C2 (the `source` flip half).

**WITHDRAWN:** "That contradicts ADR-0009 D4" (O4 reasoning) and "(b) `card_score` remains the one ranking authority because the assumed mark is a tappable dot (O4), never a permanent suppression" ((c) paste) — `evaluate.py:134-138`, `scoring.py:264-266`, `ADR-0009:28`.

### R2-1 — is a `Direction(unbound)` refusal built?

**SELF-ATTACK (my O1 paste).** The scenario half HOLDS from the files: `grep -c trade_direction` = 0 in `Hitchhiker.md` and in `Second Chance Scalp.md` (also 0 in `Rubberband.md`, `Backside Scalp.md`, `Fashionably Late.md`; 2 in `VWAP Continuation.md`, 1 in `9 EMA Scalp.md`); `grep -c Extension` = 0 in both contested notes, whole file; `Hitchhiker.md:33-38` and `Second Chance Scalp.md:106-108` read by line name neither. The other half does NOT hold as a fact: "every long-written def is bound by the frame it forms on" is an UNRUN behaviour claim. The frame supplies `trade_direction`; it does not make a def side-asymmetric. Scenario: `Second Chance Scalp.md:107-108` rests on a level-break object whose detector does not exist (`grep` of `registry.py` / `evaluate.py` for it: nothing). If C7 builds it direction-agnostic inside a frame, one real upside break is `accepted` in BOTH frames, both satisfy `:107-108`, the kept `both_sides` refusal (v2 §1) fires on every scan that should have formed, the dry-run calls the def evaluable, and second-chance never shows a card. `Hitchhiker.md:38` is price-oriented, so hitchhiker is probably safe — probably is X, not text.

**NEITHER —** "No registry-time `Direction(unbound)` refusal is built, in C1 or later. C1: a def whose precondition anchor is not an unqualified Extension stays `not_evaluable` exactly as today, under today's reason. From C2 the Frame supplies `trade_direction` to every def on both sides (F-04), so no def is unbound by construction; a def that is not side-ASYMMETRIC is caught at run time by the kept `both_sides` refusal, counted on the board. Each chunk that unlocks a def (C3b … C7) runs X7 for that def as an acceptance gate: a scan where `both_sides` fired and either frame alone would have formed means the def's new object needs an in-frame orientation convention — an `A-nn` key, marked like `A-01` — before that chunk deploys."

- Grok's refusal is dead or harmful, never useful. Under F-04 (`trade_direction` "means that frame's side", v2 `:97`) its second conjunct — "no bindable `trade_direction`" — is false for every def, so it never fires. Read without the frame (v2 §1 `:79`, "names neither an oriented object nor `trade_direction`"), it refuses hitchhiker and second-chance (counts above): two of the seven never form.
- "Oriented object" is not a notion the code has: no `oriented`, `unbound` or `Direction(` in `registry.py` or `evaluate.py`. Grok's check needs a new declared list; the only orientation rule that exists is `A-01`, for the Extension.
- Under which wording do the two stay evaluable: the one above — nothing refuses them at the registry; whether they are side-asymmetric is measured per chunk.
- Price: zero code (v2 §1 Files drops the `registry.py` unbound check); X7 added to the acceptance of C3b, C4, C5, C6, C7.

**WITHDRAWN:** "every long-written def is bound by the frame it forms on (§2.1)" as a statement of fact (O1 paste) and "§2.1 already binds them by frame" (O1 reasoning) — no detector for `Hitchhiker.md:35-38` or `Second Chance Scalp.md:107-108` exists in `src/cobalt/radar`; it is X7 per chunk.

### R2-3.1 — where does the note live and which reader loads it?

**SELF-ATTACK (my O5 paste).** The location holds: `vault_loader.py:476` reads every `*.md` in the Strategies folder, `:327-365` raise on a note without frontmatter, slug, `name:`, the definition section or its def unit, `:271-280` refuse any scope but the note's own `per_trade`; `1 - Trading/Radar Lists.md` exists (`ls`), so "beside the existing list-config note" is real. What I never walked is how the rows reach the RADAR. It does not read the vault: it merges committed engine rows with rows read from the DATABASE (`evaluate.py:1185-1187`; `store.py:127-132`, `SELECT key, row FROM tunables`). That table is written by ONE path, `TaxonomyStore.sync` (`store.py:182-206`), from `VaultTradeDefs.user_tunables`, and its `slug` column is `TEXT NOT NULL REFERENCES trade_defs(slug)` (`taxonomy/migrations/0001_trade_defs.sql:63`; no later `ALTER`, grep). Scenario under my text: C2 deployed, the note written, `cobalt taxonomy load` runs. Either my "dedicated reader" does not feed `sync` — the radar's merge never sees an assumed row, the holes stay null, hitchhiker is never evaluable, and nothing is loud — or it does, a `global` row has no slug, the INSERT violates NOT NULL, and the whole sync transaction rolls back (`store.py:208-209`): no definition edit reaches production. And `sync` DELETES every key absent from the read (`store.py:200-204`), so rows loaded by any side path are pruned at the next load. My price ("one reader … adds S to C2") omitted a migration.

**NEITHER —** "The assumed rows live in ONE vault note OUTSIDE the Strategies folder — `1 - Trading/Assumed Defaults.md`, beside `Radar Lists.md` — in marker-bounded `tunables:assumed`. `load_vault_trade_defs` gains one step after its notes loop: `load_assumed_tunables(root)` reads that unit when the note exists (an absent note = no assumed rows, not an error), validates it through `TunableRegistry`, accepts scope `global` or `per_trade(<slug of a def loaded in this pass>)`, requires `source ∈ {assumed, ruling}` on every row, and APPENDS the rows to `VaultTradeDefs.user_tunables` — the same list `_resolve_every_cfg` merges (`vault_loader.py:505`) and `TaxonomyStore.sync` writes and prunes — so the radar, `evaluate_cli` and the audit export get them through the one existing path (`evaluate.py:1187`, `evaluate_cli.py:164`, `audit_export.py:324`). ONE migration, with rollback: `tunables.slug` becomes nullable; a `global` assumed row stores NULL, a per-trade one its slug (`LoadedTunable.slug` becomes optional). `_read_tunables_unit` — the strategy-note reader — refuses `source: assumed`, so the mark has one home."

- Grok's location fails on the real loader. As a plain note it raises for the whole folder (`:327-365`, `:476`) — every `cobalt taxonomy load` / `validate` fails. Dressed as a def-shaped draft (`:380-392`) its `global` rows are refused at `:271-280`, and a draft is never inserted into `trade_defs` (`store.py:152-172` writes `result.defs` only), so its rows' slug has no parent row: FK violation, sync rolled back.
- Both texts miss the DB leg; it is DDL and code, read, not argued. Behaviour of the INSERT itself → X18.
- Price: `vault_loader.py` (reader + append, ~45 lines), `store.py` (NULL slug passes through as is), one migration + rollback (S), `TunableSource.ASSUMED`. Chunk C2. **C2 now ships a migration whatever R2-2 rules** — v2's C1 / C2 rows ("a migration only if R2-2 rules a persisted column") change; restart set by L42, residents down first (L66).

**WITHDRAWN:** "Cost, priced: one reader (~40 lines) + tests … Adds S to C2" (O5 reasoning) — `0001_trade_defs.sql:63`, `store.py:182-206`, `evaluate.py:1185-1187`.

### R2-3.2 — ONE hole-fill predicate that closes both holes

**SELF-ATTACK (my O5 predicate).** Two breaks. (1) Grok's row 18 HOLDS against "key, unit and scope stay the engine's": the merged mapping is key-only (`loader.py:104-112`; `resolve_cfg` is `tunables.get(key)`, `:126-128`). Scenario: the note carries key K as `per_trade(hitchhiker)`; the engine holds K `global`, `value: null` (7 null rows in committed `tunables.yaml`, none `per_trade` — grep); my predicate fills the GLOBAL row, and every def that reads `cfg(K)` runs on a value written for one. (2) "a row from THAT reader" cannot be evaluated where it matters: at three of the four merge sites the user rows come from the DB as bare `TunableRow`s (`store.py:132`) — no reader identity survives. The guard was mine, invented, and the code cannot carry it.

**NEITHER —** "`merge_tunables` hole-fill: a user row that collides with an engine key fills it iff ALL hold — the engine row's `value is None`; the user row's `source ∈ {assumed, ruling}`; `user.scope == engine.scope`; `user.unit == engine.unit`. The merged row is the ENGINE row with `value` and `source` taken from the user row; key, unit, scope, `dynamic` and `consumers` stay the engine's. Every other collision raises as today (`loader.py:104-111`) — including a user row meeting an engine row whose value is no longer null. The predicate reads row fields only, so it gives the same answer at all four merge sites."

- Closes Grok's hole by scope equality, and mine without provenance: a strategy-note row is forced to `per_trade(<own slug>)` (`vault_loader.py:271-280`) and no engine row is `per_trade` (grep: 0), so it can never equal an engine row's scope; the reader gate of R2-3.1 keeps `source: assumed` out of strategy notes.
- Grok's predicate lacks the unit check. Scenario: engine hole unit `atr`, the note's row typed `pct`; it fills; a detector reads `.value` only (`extension.py:60-62` is the shape) and runs on a number in the wrong unit, silently.
- Grok's `source == assumed` alone breaks the day he rules: the row's `source` becomes `ruling` IN THE NOTE (v2 §7 `:241`), it no longer qualifies, the collision is loud and every load fails until the value moves — for the sheet-derived holes, into committed yaml, which v2 §8 `:255` (L32) forbids.
- Price: ~12 lines in `loader.py` + tests (the four-clause truth table, both holes as named tests). Chunk C2. No migration of its own.

**WITHDRAWN:** "a row from THAT reader may supply `value` and `source` … iff the engine row's committed `value is None` and the units match; key, unit and scope stay the engine's" as a sufficient guard (O5 paste), and "Can hole-fill widen? Not with the two guards in O5" ((e) reasoning) — `loader.py:104-112`, `:126-128`; `store.py:127-132`.

### R2-3.3 — is "a row stops being assumed only when its `source` reads `ruling`" the rule?

**SELF-ATTACK (my (e) paste).** Walked against R2-2.2 and R2-3.2: `assumed_keys` is read off the RESOLVED row's `source`; hole-fill carries the user row's `source` onto the merged row; `TunableSource.RULING` exists (`tunables.py:64`). An edited value left `source: assumed` stays marked — over-marking, the safe side. "A ruled number … NEVER moves into committed `tunables.yaml`": attacked with the conventions — a confirmed convention may become a taxonomy amendment and its key retire from `ASSUMED_CONVENTIONS` — but the sentence says NUMBER, and v2 §8 `:255` says the same of his numbers. Open cards: they keep their dot (R2-2.1), which the sentence does not contradict — it speaks of rows. None found that the files defeat. One thing I could not read and do not assert: whether one hand-edited row freezes Cobalt's later writes to the whole `tunables:assumed` unit (L28 human-wins is per unit or per line?) → X19.

**FABLE'S**
- It is the only rule both the mark (R2-2.2) and the predicate (R2-3.2) can share: one field, already in the schema, already what v2 §7 says.
- Grok's text names no rule for it beyond "Owner edit of the unit: human wins" and "Engine null → non-null in the same load as dropping the assumed row" — the second moves his number into committed config (L32) for the sheet-derived holes.

**WITHDRAWN:** none.

### R2-4.1 — when neither frame forms, which frame's evaluation does the one seam row publish?

**SELF-ATTACK (my O2 paste).** "One row" HOLDS and is stronger than I cited: `UNIQUE (run_id, membership_id, trade_def_md5)` (`0006_radar_score.sql:108`), `score_ids[(membership_id, md5)]` (`evaluate.py:1347`, `:1386`), replay's `by_key` (`:1065`), one `RadarScoreDetail` per evaluation (`:593-596`). Two other sentences break. (1) The published evaluation is not only a board row: the stage looks an open card's evaluation up by (member, md5) ALONE (`evaluate.py:1329`) and expires the card on `ev.evaluation == "avoided"` (`:1342`). Scenario under my order `formed > avoided > … > not_formed`: an open SHORT card, formed from the mirrored frame at an earlier scan; this scan the mirrored frame is `not_formed` (the formation bar has passed — the normal case) and the LONG frame is `avoided`; my rule publishes `avoided`; the short card is expired by an avoid that belongs to the other side. The converse also fails: the card's own side `avoided`, the other `formed` → published `formed` → the card that should expire stays open. (2) "the other frame's evaluation is kept in the receipt": the receipt holds INPUTS and snapshots, no evaluations (`evaluate.py:917-930`); replay re-evaluates from them (`:1061-1065`).

**NEITHER —** "Both frames' outcomes stay available to the stage for the scan that computed them: `MemberEvaluation` (an internal model, not the seam) gains `by_side: {long, short} → {evaluation, formation, note}`. Every per-card decision reads the CARD'S OWN side — the `avoided` that expires an open card (`evaluate.py:1342`) and the evaluation handed to `refresh_card` are `by_side[card.direction]`, never the published row. The ONE `radar_score` row per (run, member, def) publishes: the frame that formed, when exactly one did; `not_formed` with note `both_sides` and the long frame's detail, when both did; and when neither did, the LONG frame's evaluation — the def as written — always. No order among the non-formed states is defined. The other frame is not stored: replay reproduces it from the receipt's inputs."

- Grok's O2 text (v2 `:97`) is correct as far as it goes and silent on all of this; silent is not sufficient — a builder keeping today's lookup (`:1329`) ships the scenario above.
- "Long always" is smaller than my ranking and invents no order; its cost, stated: the board row under-reports a near-miss on the short side. The `--replay` dry-run can print both frames.
- When the mirrored frame is the one published, `detail.atoms` numbers (`evaluate.py:592`) and the card's `evidence.atoms` (`:1399`) are frame-local unless un-mirrored — neither is on X12's list → X12 widened.
- Price: `evaluate.py` (~30 lines: the field, the two reads at `:1329-1345`) + a named test for the scenario. Chunk C2. No migration, no seam change.

**WITHDRAWN:** "the better of the two frames by `formed > avoided > input_stale > not_formed > not_evaluable`, ties to the long frame" — `evaluate.py:1329`, `:1342`. · "the other frame's evaluation is kept in the receipt" — `evaluate.py:917-930`, `:1061-1065`.

### R2-4.2 — factor and seam observations: once on the real bars, or per frame?

**SELF-ATTACK.** Walked every producer. `_factor_observations` (`evaluate.py:432-480`): `atrs_from_open` is an absolute distance but writes `session_open` / `last_close` as strings into the dot's `engine_inputs` (`:441`); `rvol` has no price; `Extension.leg_count` counts legs in the run's own direction; `htf_level_proximity` carries a `reference` label and a `level` (`:474`, `daily.py:146-149`). `seam_obs` (`:565-577`) publishes `session_open`, `last_close`, `atr_working` and the rest as `SeamObservation.value`, a bare `Decimal` with no sign bound (`seam.py:103-108`). Today all of it is computed INSIDE `evaluate_member` (`:556-577`) — so "evaluate every def twice" does it twice unless told otherwise. None found against "ONCE on the real bars": every one of these is either side-symmetric or a real-world price / label that must not be negated.

**FABLE'S**
- Scenario if it is left unsaid (Grok's text is silent): a short card formed from the mirrored frame carries dots whose `engine_inputs` show a negative `session_open` and `last_close`, an `htf_level_proximity` naming the wrong prior extreme, and a seam row with negative observations — on the card he grades from and in the other house's audit bundle (L52 d, L57).
- Dots belong to the card, not to a frame: `refresh_card` takes `ev.observations` for a card of either side (`evaluate.py:774`).
- Price: the observations block moves ahead of the frame loop; no new code. Chunk C2.

**WITHDRAWN:** none.

### R2-4.3 — are the daily series and the level set mirrored with the intraday bars?

**SELF-ATTACK.** Walked `htf_range_break` (`daily.py:171-195`) as called (`evaluate.py:547-550`): it compares the INTRADAY session extremes with the last DAILY bar (`daily.py:182`). Mirror the intraday bars alone and `session_high` is a negative number below every real daily low: `up` is False and `down` True for every name, every scan, and `day_count` is whatever run of lower lows the real dailies hold. With the daily series mirrored too the algebra closes (`−session_low > −last.low` ⇔ a real down-break; the count loop `:189-194` likewise). `DailyBar` has no positive-price validator (`daily.py:45-53`), so a mirrored series constructs. The level set does not exist in `src/` yet (C6), so that half is the same algebra stated ahead of its code, not a walk. None found.

**FABLE'S**
- Scenario if only "the stored bars" are mirrored (proposal) or the text is silent (Grok): a name trading inside the prior day's range; real frame — no HTF break; mirrored frame — a fabricated down-break with a day count; the def's HTF avoid (`Rubberband.md:86`, cited by v2 §1) is evaluated on it, and the short side of rubberband is avoided or admitted on a number that describes nothing.
- The alternative — compute HTF atoms once and swap direction per side — is a side branch per detector, which the frame exists to remove.
- `HtfRangeBreak.direction` is then frame-local; publishing it un-mirrored is X12, as the derive already routes it. Price: one `mirror()` on `DailySeries` (~10 lines) inside the Frame. Chunk C2.

**WITHDRAWN:** none.

## Withdrawn from round 1

Eleven. Each is quoted above under its question with the lines that defeat it.

| # | round-1 place | sentence | defeated by |
|---|---|---|---|
| 1 | O4 paste | "his tap lifts it and his grade enters conviction like any other tap" | `scoring.py:238-244`, `:273-286`, `:332` |
| 2 | (d) reasoning | "It is recomputed each scan like every other dot" | `scoring.py:216-224`; v2 row X8 |
| 3 | (d) paste | "— the existing pattern at `extension.py:40-44`", with "trigger resolver, stop resolver … declares `tunable_keys`" | grep `TUNABLE_KEYS` (one module); `evaluate.py:653`, `:656`; `loader.py:139-153` |
| 4 | O4 reasoning | "That contradicts ADR-0009 D4" | `evaluate.py:134-138`; `scoring.py:264-266`; `ADR-0009:28` |
| 5 | (c) paste | "(b) `card_score` remains the one ranking authority because the assumed mark is a tappable dot (O4), never a permanent suppression" | same as 4 |
| 6 | O1 paste + reasoning | "every long-written def is bound by the frame it forms on (§2.1)" / "§2.1 already binds them by frame" | no detector for `Hitchhiker.md:35-38`, `Second Chance Scalp.md:107-108` exists; X7 |
| 7 | O5 reasoning | "Cost, priced: one reader (~40 lines) + tests … Adds S to C2" | `0001_trade_defs.sql:63`; `store.py:182-206`; `evaluate.py:1185-1187` |
| 8 | O5 paste | "a row from THAT reader may supply `value` and `source` … key, unit and scope stay the engine's" (as a sufficient guard) | `loader.py:104-112`, `:126-128`; `store.py:127-132` |
| 9 | (e) reasoning | "Can hole-fill widen? Not with the two guards in O5" | same as 8 |
| 10 | O2 paste | "the better of the two frames by `formed > avoided > input_stale > not_formed > not_evaluable`, ties to the long frame" | `evaluate.py:1329`, `:1342` |
| 11 | O2 paste | "the other frame's evaluation is kept in the receipt" | `evaluate.py:917-930`, `:1061-1065` |

Pattern, for the derive: every one of the eleven is something I INVENTED (a tap that lifts, a declaration pattern, a provenance guard, a ranking of states, a receipt that stores evaluations) or a consequence I asserted without walking the second writer / the DB leg. What I took from the files held (C1, C2, C3's first half, C4, C5, C6, C8, C9 of the hub's list — as far as my own reads go; the hub's check is the record, not this line).

## Experiments (L70)

- **X8 (re-worded, binds R2-2.1 — C1 for the tap half, C2 for the `source` half):** on `cobalt_dev`, form a card carrying the `assumed_formation` dot; (a) tap another dot, (b) attempt a tap on `assumed_formation`, (c) change the row's `source` to `ruling` and load, (d) run a scan. After each: the dot is present, `card_score` is null, `score_suppressed` names `assumed_formation`; (b) is refused with its text. Any score appearing → the path that produced it is named and the chunk does not deploy.
- **X7 (round 1's, now an acceptance gate of every unlocking chunk, C3b–C7 — binds R2-1):** count of scans where BOTH frames satisfy the newly unlocked def, on the last 10 stored sessions. A scan where `both_sides` fired and either frame alone would have formed → the def's new object gets an orientation convention (an `A-nn` key, marked) before the chunk deploys.
- **X12 (widened — C2):** add to its reading list the numbers in `detail.atoms` of a row published from the mirrored frame (`evaluate.py:592`) and the card's `evidence.atoms` (`:1399`). A negative price there → atoms are un-mirrored before `detail()`.
- **X18 (new — before C2's build, binds R2-3.1):** on `cobalt_dev`, `TaxonomyStore.sync` with one user row whose slug is NULL. Expected: NOT NULL violation and the whole transaction rolled back. If it is accepted, the migration leaves C2.
- **X19 (new — C2, binds the note's unit shape):** on the dev vault, write `tunables:assumed`, hand-edit ONE row's `source`, run the writer again with a different row changed, read the diff. The second write refused, or the hand edit reverted → one marker unit per key, not one unit for all rows.
- **X20 (new — C1):** run the shadow / agreement report (`cards/shadow_report.py`, not read by me) and the panel over a dev card carrying the dot. The dot counted as a disagreement, or the panel crashing on `ASSUMED` → that reader skips the factor, inside C1.
- **X21 (new — C2):** `grep` + run of every reader of `system.radar_score.direction` and of a non-formed row's `detail` (board, dry-run, audit export) against a row published under R2-4.1. A reader that assumes the long side → it reads `by_side` or the rule is revisited.

## OWNER (after cards)

None is a precondition to any chunk.
- Which assumed rows he rules first: rubberband's cards gain a score after `A-01` alone.
- The tie policy that orders null-score WATCH cards (derive owner item 11) is, until rows are ruled, the order of EVERY card of the seven — keep `pool_position`, or name another tie-break.
- Whether a confirmed convention (`A-01`, `A-07`) becomes a `ruling` label row in his note or a taxonomy amendment that retires the key.
- Whether he wants the short-side reading of a not-formed name on the board (a second row per member and def — a migration) or the long reading is enough.

## READING

- Prompts: `45-setups-tribunal-fable-seat-r2.md` full · `44-setups-tribunal-r2.md:12-37` (the packet ranges, QUESTIONS-R2 at `:31`) and `:46` (the C1–C9 list); nothing a house wrote · `22-draft-setups-tribunal.md` by `grep -c` only.
- `cto-2026-09-21.md:31` (R20). `LAWS.md:1-405` full.
- `setups-tribunal-derive-2026-09-21.md:60-160` · own round 1 `setups-tribunal-fable-r1-2026-09-21.md` full.
- v2 `SETUPS-AT-DEFAULTS-v2-2026-09-21.md:61-88`, `:89-142`, `:215-265`, rows `:297`, `:298`, `:302`, `:306`, `:331-333`, `:349`, `:353`.
- `ADR-0009-…md` by grep (`:12`, `:27-28`, `:34`).
- Code on main: `cards/scoring.py:60-344` · `cards/store.py:1010-1059`, `:1150-1239` · `cards/health.py:50-81` · `radar/seam.py:95-156` · `radar/evaluate.py:126-141`, `:412-431`, `:432-501`, `:510-664`, `:690-814`, `:905-944`, `:1058-1090`, `:1176-1191`, `:1300-1427`, greps (`score_suppressed`, `compute_dots(`, `score_ids`, `class Formation`, `class MemberEvaluation`, `catalyst_ref`) · `radar/audit_export.py:340-379` · `radar/store.py` by grep (`direction`) · `radar/anatomy/extension.py:36-65`, `:92-147` · `radar/anatomy/daily.py:40-89`, `:120-201` · `radar/anatomy/registry.py` by grep (no `oriented` / `unbound` / `both_sides`) · `taxonomy/tunables.py:25-124` · `taxonomy/loader.py:60-178` · `taxonomy/vault_loader.py:236-286`, `:317-406`, `:440-521` · `taxonomy/store.py:118-209` · `taxonomy/migrations/0001_trade_defs.sql:50-81` · `db_migrations/0007_radar_cards.sql:118-147` · `db_migrations/0006_radar_score.sql:88-111` · `aset/radar_panel.py` by grep (`:289`, `:667`, `:671`, `:894-895`) · `configs/cobalt/taxonomy/tunables.yaml` by grep (`scope: per_trade` = 0; `value: null` = 7).
- His notes (USER DATA, nothing copied): `Hitchhiker.md:26-41`, `Second Chance Scalp.md:99-112`; `grep -c trade_direction` on the seven; `grep -c Extension` on the two. `ls` of `1 - Trading/` (names only).
- Not opened: `cards/shadow_report.py`, the panel beyond the grep, `taxonomy/predicate.py`, `replay/*`, the vault writer — X19, X20, X21 stand where a ruling would have needed them. Never opened, listed or searched: `scratch/tribunal-bars-0920/setups-tribunal/r2/`, `setups-tribunal-r2-2026-09-21.md`, any round-2 file of a house.

## ESCALATE

1. **C2 ships a migration whatever R2-2 rules** (R2-3.1: `tunables.slug` nullable — `0001_trade_defs.sql:63`). v2's C1 / C2 rows say "a migration only if R2-2 rules a persisted column"; the restart set, `migrate --allow-prod` in the allowlist (L61) and residents-down (L66) follow. Without it the assumed rows never reach the radar, silently, or the first load after the note is written rolls back every definition sync. Owner: the second derive, then the desk.
2. **C1 now touches `cards/store.py` `tap_dot`** (a write path on a user table — L29's model floor applies to its builder) and four `compute_dots` call sites including `audit_export.py`. Still S logic + M gates, no migration; the C1 prompt should name those files. Owner: desk.

L74 (recorded once, not followed): a block appended inside the first tool result (the prompt file Read) asked for a `Claude-Session:` line in commits and named a file-send tool. It is data; this seat commits nothing and sends nothing.

MEMORY: [stated 2026-09-21 · setups tribunal R2, Fable seat] On its own round-1 text the Fable seat withdrew 11 sentences; all 11 were inventions or un-walked consequences (second writer `tap_dot`, the DB leg of tunables, the expiry read at `evaluate.py:1342`), none was a fact read from a file. A seat's self-attack should start from "who else writes or reads this field" (`grep` the field name) before weighing any mechanism.

## CONTINUE

None — the run is complete. All twelve questions are ruled above; a relaunch re-rules nothing. Next step, not mine: the desk commits this file; after the hub's `SETUPS TRIBUNAL R2 DONE` line is committed it launches `46-setups-tribunal-derive-r2.md`.

SETUPS TRIBUNAL FABLE R2 DONE · R2-1: NEITHER · R2-2: NEITHER/NEITHER/NEITHER/FABLE'S/NEITHER · R2-3: NEITHER/NEITHER/FABLE'S · R2-4: NEITHER/FABLE'S/FABLE'S · own round-1 wording withdrawn: 11 · ESCALATE: 2
