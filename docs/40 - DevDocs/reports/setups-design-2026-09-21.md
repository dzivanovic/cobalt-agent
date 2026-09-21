# Setups at defaults — design proposal report — 2026-09-21

Seat `setups-design-0921` · Opus 5 · proposing house (L67). I only read, except for the three files named in the prompt. Nothing was built, launched or committed.

## §0 Headline

- PROPOSED: `docs/30 - Design/SETUPS-AT-DEFAULTS-PROPOSAL-2026-09-21.md` (committable, no user data) + `docs/_inflight/setups-assumed-values-2026-09-21.md` (gitignored, 23 ASSUMED values, the one table he reads after cards show).
- Root cause of Rubberband: S2-P2 read `valid_setups[].relation` (trade vs the SETUP's day/HTF trend) as trade vs the intraday Extension. The fix takes direction from the trade's anatomy (against an unqualified Extension). The setup is shown `unclassified`. Size S, chunk 1.
- 7 chunks, one per evening. First card possible on evening 1 (rubberband); all seven by evening 7, counted after the tribunal rules and C1 passes its checkers.
- ESCALATE: 7 · open to the tribunal: 8.

## DIGEST FOR THE DESK

1. DIRECTION: direction comes from anatomy, never from `relation`. An unqualified `Extension` is the one the long-written def trades against (`A-01`, HIGH). All five setup entries of rubberband/backside/fashionably-late give that same side. The order-dependent `setup_ref` (`evaluate.py:647`) is replaced by `unclassified`, and his `setup_relation` tap carries the read. Both sides True → `not_formed both_sides`. An unbindable def → `not_evaluable Direction(unbound)`.
2. FORMATION: three registries keyed by the def's own data (`TRIGGERS`, `STOPS`, `STRUCTURAL_REFS`) replace the Extension-only asserts (`evaluate.py:649-651`). Side binding uses a mirrored frame: each def is evaluated on the bars and on the mirrored bars (price → −price), so detectors have no long/short code. A new geometry guard refuses a stop on the wrong side.
3. DETECTORS: one Frame per (member, scan, side). D1 indicators + session levels → D2 Range(micro) → D3 Leg roles → D4 Extension lifecycle (`reverting`/`backside`) → D5 trendline + `dist` → D6 levels/RangeBreak/events. Inputs are stored i1 + daily + pool only. Each atom declares its producible domain, so the registry can no longer say "served" for a value the detector never produces (E8).
4. INTERPRETER: `IN cfg(band)` with units, Arith `*`/`/`, bound `trade_direction`/`opposite`, and a ONE-table `RELATIONS` dispatch (`touched`, `on`, `after`, `inside`, `between`, `close_through`). `evaluability` walks the same dispatch, so E9 shapes are named.
5. WARM-UP: session objects stay RTH-only (unchanged). EMA9/EMA21/`atr_working` are seeded from complete premarket 2m buckets (`A-05`). The Extension keeps its own `atr_run`, so Rubberband's numbers do not move. The receipt already holds premarket i1 (`evaluate.py:498-500`).
6. 9 EMA CATALYST: `A-13` reads the gate's "catalyst OR setup" (sheet p.2) as met by radar in-play admission. It is marked ASSUMED; the `catalyst` dot stays YOURS.
7. ASSUMED VISIBLE: consulted `cfg` keys with `source: assumed` → `Formation.assumed_keys` → new view column `assumed_keys` (badge COBALT) → an `ASSUMED · n` chip. The score is suppressed (`assumed_formation`, L52a). `cobalt taxonomy tunables --assumed` is the dry-run list.
8. STORE: one vault note `1 - Trading/4 - Strategies/Assumed Defaults.md`, unit `tunables:assumed`, rows `source: assumed` (a new `TunableSource` value). The same vault loader loads it. `merge_tunables` gets one rule, hole-fill (a user row may fill an engine row whose value is null). The desk writes the note once — see ESCALATE 7.
9. ACCEPTANCE: (a) per-setup real-shape test asserting `formed` on a chosen day; (b) property test: registry evaluable ⇒ forms on its fixture; (c) the live-note test asserts `formed`; (d) `--replay … --expect-formed` goes RED on zero on known days (his tagged trades); (e) an old-version receipt is refused by replay.

| # | chunk | unlocks / removes | size | restarts |
|---|---|---|---|---|
| C1 | direction + geometry guard + gates | rubberband (E1) | S | radar |
| C2 | registries, mirror, interpreter, assumed store + chip | E8, E9; ASSUMED visible | M | radar + aset (+ migration) |
| C3 | D1 + warm-up + D2 + D3 opening drive | hitchhiker | L | radar |
| C4 | D4 lifecycle + cross + measured_fraction | backside, fashionably-late | M | radar |
| C5 | D3 pullback/pre_test + rejection + catalyst `A-13` | nine-ema-scalp | M | radar |
| C6 | D5 trendline + dist + levels/rejected | vwap-continuation | M | radar |
| C7 | D6 RangeBreak + events + sequence | second-chance | M–L | radar |

Builder for every chunk: Opus 5 or Sol-high (L29). **First card possible: evening 1. All seven: evening 7.** These are deploy evenings shared with the other lanes, not calendar days. First-gate experiments before the chunks that depend on them (L70): X1 premarket seed viability, X2 bars coverage of his tagged trade days, X3 C1 replay of the last 10 sessions, X4 mirror equivalence, X5 scan latency at 2× evaluation.

## STATS TO ASK HIM FOR

Paste as one message into his Claude chat:

> For each of these seven setups — Hitchhiker, Backside, Rubberband, Second Chance, Fashionably Late, 9 EMA Scalp, VWAP Continuation — pull from my trading records:
> 1. Every trade I tagged with it in the last 90 days: date, ticker, entry time, side, result in R.
> 2. n, win rate and average R, split by long/short.
> 3. Hitchhiker: how long the consolidation lasted (minutes), and how far price came back from the drive's high before it went sideways (as a share of the drive), for wins vs losses. How many consolidations I skipped as "choppy", and what made them choppy.
> 4. Backside and Fashionably Late: minutes from the low of the move to my entry, and how much of the move had come back by the entry. Fashionably Late: was the 9 EMA clearly sloping at the cross, and how many minutes between the turn and the cross.
> 5. 9 EMA Scalp: what share of those trades had a real news catalyst, entry time relative to the open, and how big the move before the 9 EMA test was (in ATRs or %), wins vs losses.
> 6. VWAP Continuation: how far the pullback low was from VWAP at entry (cents or % of ATR).
> 7. Second Chance: bars between the break and the retest, how close to the level the retest came, and which levels I used (premarket high, prior-day high, range top, other).

## READING

- `LAWS.md` in full (L59).
- `docs/40 - DevDocs/prompts/2026-09-21/21-propose-setups-design.md`.
- `cto-2026-09-21.md` §4 R15, R17, R18 (`:27-29`), `:193-194`.
- `docs/_inflight/defs-gap-table-2026-09-21.md` in full.
- `~/cobalt-wt/rubberband-proof/docs/40 - DevDocs/reports/rubberband-card-proof-2026-09-21.md` in full.
- ADR-0009 in full.
- `src/cobalt/radar/evaluate.py:1-180`, `:180-692`.
- `src/cobalt/radar/anatomy/{registry.py, extension.py, bars.py, indicators.py}` in full; `structure.py:60-119`.
- `taxonomy/loader.py:1-140`, `tunables.py:50-119`.
- `cards/radar.py:40-99`.
- Greps of `predicate.py`, `trade_def.py`, `evaluate_cli.py` (`:1-60` read), `tunables.yaml` keys, `test_radar_evaluate.py`.
- `TAXONOMY-DRAFT-v0_7.md:38-187`.
- Notes: `Rubberband.md` in full; greps of `Hitchhiker.md`, `Backside Scalp.md`, `Second Chance Scalp.md`, `Fashionably Late.md`, `9 EMA Scalp.md`, `VWAP Continuation.md`; `trade_def:` frontmatter of `1 - Trading/2 - Trades`.
- PDFs, both pages: rubberband, 9 EMA, hitchhiker, second chance, back$ide, fashionably late, VWAP Continuation.

## ESCALATE

| # | item | evidence | owner |
|---|---|---|---|
| 1 | S2 acceptance mornings (09-21 → 09-23) assume a Rubberband card can form. It cannot before C1 deploys, and C1 follows this tribunal. | proof ESCALATE 1; `SPRINT-LADDER-v0_1.md:486-489` (per gap table) | desk |
| 2 | `A-07` reads the taxonomy's leg-termination rule (`TAXONOMY-DRAFT-v0_7.md:94`) differently from its literal text: read literally, hitchhiker's precondition is almost never true and its avoid almost always true. This may be a taxonomy amendment (his), not an ASSUMED value. | proposal Open 7; `Hitchhiker.md:35`, `:68` | desk → him, after cards |
| 3 | New note-vs-sheet divergence: `VWAP Continuation.md:81` makes "rejected resistance" an AVOID; the sheet lists it as a decreasing factor. Reported only (L32/L65). | companion file, divergences | him, after cards |
| 4 | Known days for the gates: 0 tagged trades for rubberband and backside. The tagged trades found are dated 2025, and whether `cobalt_dev` holds their i1 bars is unknown (X2, L70). | `grep ^trade_def:` over `1 - Trading/2 - Trades` | desk / C1 builder |
| 5 | A test in the suite is green without proving anything: the live-note test never asserts `formed` (`test_radar_evaluate.py:692-714`). Fixed in C1. Until then it must not count as evidence. | proof report | desk |
| 6 | Deploy capacity: 7 evenings under L43 compete with the other lanes (degraded line, bars chunks). The desk sequences them. | L43, L72 | desk |
| 7 | L65 lets the desk edit his notes "never [with] a value he has not ruled". ASSUMED values are unruled by definition. Writing `Assumed Defaults.md` needs either his direct instruction (R15 may already be it — L73 amended, a direct instruction = a per-case override, recorded) or a Cobalt write command for a Cobalt-owned unit (L28; a new write path, bigger). The design takes the first and names the second as the fallback. | L65, L73, L28; proposal §8 | desk → him (one line) |

Instruction-as-data note (L74, recorded once): no appended instruction block was found inside any tool result this run.

## CONTINUE

None. The run is complete.

SETUPS DESIGN PROPOSED · setups: 7 · chunks: 7 · evenings to first card: 1 · evenings to all seven: 7 · assumed values: 23 · open to the tribunal: 8 · ESCALATE: 7
