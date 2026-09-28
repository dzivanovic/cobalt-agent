# `src/cobalt/voice/tools.py`

## What it does
The voice tools and the rules around them (FINAL §2.4, §3).

## Read tools — data from the stores, words from code templates
- `cards.open` / `cards.numbers`: `read_open_cards()` — the sheet's own
  `CardStore.open_cards()` — rendered by `render_open_cards` /
  `render_numbers` (stored fields only: entry, stop, shares or "unsized",
  grade, state).
- `radar.pool`: `read_pool()` calls the `/api/radar/pool` route function
  itself (never a second query path); a 503 from it is `ToolReadFailed`
  with the route's own error text. `render_pool` names at most ten.
Nothing here calls `/size` or the sizer, or computes a score, rank, grade
or size (tested on the module's code).

## The figures check [F-05]
`figures_ok(say, result)`: every numeric token in the model's `say` must be
a numeric token of the rendered result (so `4.4` ≠ `4.40`, and `440` never
passes on the digits of `4.40`). `compose_reply` speaks the template, with
`say` in front only when it passes.

## Hard refusals, whatever the Plan says
`code_refusal`: an order / platform request (buy, sell, cover, flatten,
"at market", order words; since fix r1 also the platform names — DAS,
Lightspeed, TradeStation, CenterPoint, "platform" — and order PHRASES such
as "go long", "short 100", "exit my … position", "take profits", "scale
out"; since fix r2 also a bare exit / close / close out / get out of, or
a share-count-free short, OF A TICKER — an upper-case 1–5 letter token,
matched case-sensitively, and not after "the" / "my" / "a" for short;
never a bare long / short / close / exit on their own, so card sides such
as "my short XYZ card" and price fields such as "close at" stay readable)
→ `refuse` with ONE fixed sentence; a settings /
rules / strategy / risk request, or a registry tool marked
`trading_logic: true` → `unsupported` naming
`cobalt settings load --card <file> --sha256 <hash> --apply` ([R3F-11]);
a Plan of kind refuse / unsupported → the fixed sentences.

## The act: dry run, then the one card-stop function
`stop_dry_run` computes the exact change (card, from → to, state, the
read-back, `diff_sha256`, `target_sha256`, expiry) and writes nothing. It
CLARIFIES when the new stop equals the current one, or is ≥ 10× / ≤ 0.1×
it — X-X5 found the engine writes a spoken "four fifty" as `450`.
`execute_stop` (after HIS confirmation only) re-reads the card, recomputes
the dry run, requires both hashes to match (else `TargetChanged` carrying
the fresh read-back — refused, re-confirm, [F-09]) and then calls
`cobalt.aset.card_stop.set_card_stop` — the same function the sheet's stop
route calls; `CardStore.record_stop_edit` is the expert (L40). Since fix r2
it passes `expect_from_stop=pending.from_stop`, so a stop that moved
between its own read and `set_card_stop`'s is refused as well: `StopMoved`
becomes `TargetChanged` with a fresh dry run of the moved card, read aloud
for re-confirmation, and no edit is recorded.
