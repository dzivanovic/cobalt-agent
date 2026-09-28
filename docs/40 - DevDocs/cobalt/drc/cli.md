# `src/cobalt/drc/cli.py`

## What it does
This is the `cobalt drc` command group (DRC K1). It is the ONE `drc`
group, and D3's `cobalt drc build` joins it later (L3). It mounts
`state-book`. Until K3's `/drc` form is checked, this command is the
landing set's statement caller (R52 (c); v3 `[F-10]`).

```
cobalt drc state-book --opening DAY (--flat | --position SYMBOL DIRECTION SHARES [AVG_COST] ...)
cobalt drc state-book --no-trade DAY
cobalt drc state-book --resolve DAY TRADE_ID [--exit-price P] [--exit-time T]
    [--supersedes ID] [--apply --sha256 HASH]
```

## Dry run by default
- **Without `--apply`** it calls `DrcStore().preview_stated_book(…,
  via="cli")`.
  - It prints the row: day, kind, positions as canonical JSON, reason,
    `via: cli` and supersedes.
  - It then prints `book_sha256: <hex>` and `DRY RUN — nothing written`,
    and exits 0.
  - The dry run is not gated: it still prints inside `market_reset`.
- **`--apply` without `--sha256`** is refused with exit 2.
- **`--apply --sha256 H`** calls `record_stated_book(…, via="cli",
  expected_sha256=H)`.
  - On success it prints `written: drc_stated_books #<id> (book_sha256
    <hex>)`.
  - A refusal prints `REFUSED: <reason>` and exits 1. A refusal is a hash
    mismatch, a `market_reset` block, a current row not superseded, or
    invalid positions.
- This is L7's interim clause. His chat word and the printed hash
  approve the write, and what is written is what was reviewed.

## Parser rules (`request_from_args`, exit 2 on misuse)
- It takes exactly one kind: `--opening` / `--no-trade` / `--resolve`.
- `--opening` takes exactly one of `--flat` or `--position` (repeatable,
  3 or 4 values).
- `--exit-price` and `--exit-time` belong to `--resolve` only.
  `--exit-time` is ISO-8601 with an offset; a naive time is refused.
- `--supersedes ID` works on every kind.

## What it never does
It runs no SQL and touches no `DrcStore` internals, so it inserts
nothing itself (L3, L40). It prints the table name from
`DrcStore.STATED_TABLE`. It writes no vault note (L28). `turn_id` and
`readback_sha256` stay NULL, because they belong to the voice caller
only.

## 2026-09-25 — DRC K2: the statement's effect
After `--apply`, the CLI calls `DrcStore.rebuild(day)` in two cases:
- the day has a current trading-log import (any kind of statement);
- the statement is a `no_trade` or a `resolve` for a day that joins a
  recorded chain (a `day` row on or before it).

In those cases:
- The dry run prints one more line after the row: `on --apply: rebuild
  <day> and every later recorded day`.
- The apply prints `rebuilt: <dates>`.
- A refused rebuild prints `not rebuilt: <reason>` and exits 1. The
  statement stays written, because it is his input.

Otherwise the apply prints `stated; <day> has no import yet`.

The narrowing for `no_trade` / `resolve` is a builder reading of the K2
contract's C7, carried to the check. It keeps a statement for a day that
has no recorded chain from being refused for having nothing to re-pair.
The CLI still inserts nothing itself (L3).

## 2026-09-25 — DRC K2 fix r1
The day the CLI tests, prints and rebuilds is
`DrcStore.effect_day(day, supersedes)`: a restatement's rebuild starts at
the earlier of its day and the superseded row's day (F-1, AMENDED C7).

## 2026-09-25 — DRC K2 fix r2
For a restatement, the recorded-chain test now reads the SUPERSEDED row's
day (`DrcStore.stated_day`), not the new day. So a resolve restated to an
earlier day with no import, while the superseded row's day is recorded,
now rebuilds from `effect_day`. That rebuild is refused loud (`not
rebuilt: … nothing to re-pair ([F-05])`, exit 1, the statement kept),
never the silent exit 0 it was before (F-1r2, AMENDED C7 (r2)). The
`stated; <day> has no import yet` line now names the effect day, which is
the day actually tested for an import.

## 2026-09-28 — DRC D2 fix r1
`--no-trade DAY --apply` on a day with no trading log, once the statement
is written and the day joins a recorded chain, no longer runs its own
rebuild: it calls `imports.no_trade_event(DAY, <the statement's id>)`,
the page's ONE path (L3; `DRC-D2-SEAM-2026-09-25.md` §1), which runs the
rebuild AND fires the day's file-less event. It prints the function's
lines (`rebuilt: <dates>` or `not rebuilt: …`, then the status line) and
exits 1 unless the event is `done` — with no D3 build that is `DRC build
FAILED: build — build not built (D3)`. `via` stays `cli`. The `opening` /
`resolve` branches, the dry run, `_rebuilds`, a zero-execution day and
the `stated; <day> has no import yet` path are unchanged.
