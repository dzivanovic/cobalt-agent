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
