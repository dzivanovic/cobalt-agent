# `src/cobalt/cards/legs.py`

## What it does
THE ONE WRITER of `"user".legs` (S3 exits v3 §3; L3, L40). Every leg row — the entry at the fill, the exits, the corrections, his held-count statement, the trading-log reconcile — is written here and nowhere else. S3 C1 built the entry leg; S3 C2 (R67 = the Fable seat's N) added THE running read, the exit, correction and held-count writers, and the one realized-R function.

## The connection rule — two shapes
- `insert_entry_leg` and `running_shares` run on the CALLER's open transaction and never open, commit, roll back or close one (the entry leg lands with THE fill, `AsetStore.mark_filled`).
- `record_exit`, `record_correction`, `record_held` are top-level writes: each runs the session gate first (`assert_writable`, refused in `market_reset` before anything is read), opens ONE connection (`db.connect(env.resolve_db_name(), side=USER)`), sets `autocommit = False`, takes the card row lock `SELECT * FROM aset_sizings WHERE id = %s FOR UPDATE` (the lock `transition()` takes), writes its leg and — when running reaches 0 — FILLED → CLOSED through `CardStore.transition(…, conn=conn)`, evidence `{"leg_id": <the leg>}`; ONE commit; any exception rolls everything back and re-raises.

A connection still in autocommit is refused before anything runs (`RuntimeError`, "…a leg is written only inside the transaction its caller holds…").

## Refusals — `LegRefused(CardStateError)`
Every refusal is raised by name, nothing written; the message is shown verbatim; `code` is stable: `stale` (`REFUSED: screen said <posted>, now <computed> — tap again`), `not_filled`, `zero_preset` (`REFUSED card <id>: ½ of 1 is 0 — use flat or type`), `over_running`, `typed_shares`, `preset`, `import_id`, `not_current` (names the current id), `over_entry`, `closed_off_zero`, `closed_held` (`CLOSED has no way back — correct the exit instead`), `no_entry_leg`, `held_zero_no_exit`, `held`, `no_change`, `price_source`, `shares`, `no_leg`, `no_position`.

## `insert_entry_leg(conn, card_id, *, shares, price, at, flag, price_source, price_asof, source, stop_in_force, session, account_mode, day_mode_id, attested_sheet, sheet_mismatch) -> int`
Inserts the ORIGINAL entry leg (`seq = 0`, `kind = 'entry'`, `running_before = 0`; `preset`, `corrects`, `held_stated`, `source_import_id` NULL). Returns its id. A second original entry is refused by the partial unique index, not checked first. Its only caller is `AsetStore.mark_filled`, inside THE fill's transaction. It and every C2 writer insert through one private `_insert_leg`.

## `running_shares(conn, card_id) -> Running` (C2-1)
THE ONLY running read (L3): current entry-leg shares − Σ current exit-leg shares from `legs_current_v`. Takes the card lock itself (`FOR UPDATE`, re-entrant for a caller already holding it). `Running(shares, basis, base_shares, exit_shares, entry_leg_id, entry_price, state)`. `basis`: `legs` (the current entry leg); for a FILLED card filled before C1 (no entry leg, O21 A) `recomputed_shares` when that cache is set, else `shares`. No entry leg in any other state → `LegRefused('no_position')`. Its callers: the three writers, `CardStore.record_stop_edit` (FILLED), `read_position`.

## `record_exit(card_id, *, preset, shares=None, price, price_source, price_asof, flag, source, running_before, now, source_import_id=None) -> ExitResult` (C2-2)
Card must be FILLED. The posted `running_before` must equal the running computed under the lock (a stale or duplicate tap is refused, never re-applied — X7). Presets (O14 A, O1 A): `half` ⌊running/2⌋, `third` ⌊running/3⌋, `flat` running, `typed` = `shares` (0 < shares ≤ running); a result of 0 is refused. The row: `kind = 'exit'`, `seq` = greatest current seq + 1, `running_before` = computed, `stop_in_force` = the card's stop under the lock, `session` = the gate's session, `account_mode` = the card's. `ExitResult(leg_id, shares, running_before, running_after, closed, transition_id)`.

## `record_correction(leg_id, *, price=None, at=None, flag=None, price_source=None, shares=None, source, now, source_import_id=None) -> CorrectionResult` (C2-3)
A NEW row with `corrects = leg_id`, which must be the CURRENT row of its seq. Copied: `seq`, `kind`, `preset`, `running_before`, `stop_in_force`, `session`, `account_mode`, `day_mode_id`, `attested_sheet`; `at` unless given; `price_asof` only while price and source are unchanged. A changed price must name its `price_source` (L57) and is `confirmed` unless `flag` is given. A shares change is refused when Σ current exits would exceed the entry, or when it moves a CLOSED card's running off 0; one that brings a FILLED card to 0 closes it in the same transaction (O22 A). An ENTRY-price correction rewrites the fill cache (`actual_fill`, `recomputed_shares`, `recomputed_used_risk`, `share_delta`, `distance_change_pct`, `drift_warned`) on the same transaction: `compute_fill_recompute` on `SizingResult.from_card` of the card rebuilt with the stop in force AT THE FILL (the entry leg's `stop_in_force`) and the P stored at the fill; `filled_at` and `drift_warning_pct` are untouched and the fill transition's evidence keeps the fill-time figures. `CorrectionResult(leg_id, corrects, running_after, closed, transition_id)`.

## `record_held(card_id, held, *, source, now) -> CorrectionResult` (C2-4, S-HELD)
FILLED only (CLOSED → `CLOSED has no way back — correct the exit instead`). A correction row of the current entry leg: `held_stated = held`, `shares = held + Σ current exit shares`, `price` / `price_source` / `price_asof` / `at` copied, `flag = 'confirmed'`. `held = 0` closes the card in the same transaction. Refused: a card with no entry leg (filled before C1); "holding 0" with no exit (a leg holds > 0 shares); `source = 'trading_log'` (the trading log reconciles through `record_correction`).

## `realized_r(card_row, current_legs) -> RealizedR` (C2-5, `realized_r.1`)
Pure, never stored (v3 §3). `R_unit = |entry.price − entry.stop_in_force|`; `sign` from the card's `direction`; Σ over the current exits `sign × (exit.price − entry.price) × exit.shares ÷ (entry.shares × R_unit)`; `provisional` while any current leg is `estimated`; `R_unit = 0` → `value None`, `reason 'not computed — zero risk unit'`; no entry leg → `'not computed — no entry leg'`. Actual unit only (O15 A). `RealizedR(function_id, value, provisional, r_unit, reason)`.

## `read_position(card_id) -> Position` (C2-7's read)
The card (`id, ticker, direction, state, stop, structural_stop`), its `legs_current_v` rows by seq, `running_shares`, `realized_r` — on one transaction that writes nothing and is rolled back (the running read takes the lock, so it cannot be READ ONLY). `cobalt cards legs <id>` prints it with `CardStore.stop_owner`.

## S-C2 — the trading-log seam (the DRC lane's D5; C2 builds no caller)
`record_exit` and `record_correction` accept `source = 'trading_log'` only with a `source_import_id` (and refuse an import id on any other source) — `LegRefused('import_id')`. Such a row is appended like any other: it never deletes or updates his rows. The CLOSED check runs only when running reaches 0, so a trading-log correction may leave running above 0 across days (R67 (4)). A refusal (e.g. moving a CLOSED card off 0) is raised by name for the caller to show; nothing is forced.

## S-LEGS — `"user".legs` as built (`db_migrations/0021_legs.sql`)
| column | type | rule |
|---|---|---|
| `id` | bigint identity PK | |
| `user_id` | int NOT NULL | `DEFAULT (current_setting('cobalt.trader_id')::int)`, FK `"user".traders(id)` (the 0007 shape) |
| `card_id` | bigint NOT NULL | FK `"user".aset_sizings(id)` |
| `seq` | smallint NOT NULL | 0 = entry, 1..n = exits |
| `kind` | text NOT NULL | `entry` / `exit` |
| `shares` | int NOT NULL | `> 0`, his broker's count |
| `price` | numeric(14,4) NOT NULL | `> 0` |
| `at` | timestamptz NOT NULL | when he tapped / sent |
| `flag` | text NOT NULL | `estimated` / `confirmed` |
| `price_source` | text NOT NULL | `last_poll` / `typed` / `dm` / `trading_log` |
| `price_asof` | timestamptz NULL | the bar ts when `last_poll` |
| `preset` | text NULL | `half` / `third` / `flat` / `typed` |
| `running_before` | int NOT NULL | `>= 0`; the count a tap was computed from (entry: 0) |
| `stop_in_force` | numeric(14,4) NOT NULL | the stop in force at that leg (R38) |
| `source` | text NOT NULL | `panel` / `sheet` / `dm` / `trading_log` |
| `source_import_id` | bigint NULL | NO FK (the import table is the DRC lane's); `(source = 'trading_log') = (source_import_id IS NOT NULL)` |
| `held_stated` | int NULL | `>= 0`; only on an entry CORRECTION: `held_stated IS NULL OR (kind = 'entry' AND corrects IS NOT NULL)` |
| `corrects` | bigint NULL | FK `"user".legs(id)`; a correction names the current row of its seq |
| `session`, `account_mode` | text NOT NULL | the fill's session; the card's account-mode stamp |
| `day_mode_id` | date NULL | FK `"user".day_modes(trade_date)` (the day_modes key is the date) |
| `attested_sheet` | text NULL | the `.htk` he had attested that day |
| `sheet_mismatch` | boolean NULL | set on the original entry and nowhere else: `(kind = 'entry' AND corrects IS NULL) = (sheet_mismatch IS NOT NULL)` |

Indexes: `legs_one_original_per_seq` UNIQUE `(card_id, seq) WHERE corrects IS NULL`; `legs_one_original_entry` UNIQUE `(card_id) WHERE kind = 'entry' AND corrects IS NULL`. Trigger `legs_append_only` BEFORE UPDATE → `"user".refuse_row_update()` (0007). View `"user".legs_current_v` = per `(card_id, seq)` the row with the greatest `id` (`DISTINCT ON … ORDER BY id DESC`). No `running_after`, no `direction`, no `cobalt_stop` (R67: running is derived by ONE store function, C2's; `direction` / `entry` are the card row's; Cobalt's stop is `structural_stop`, the gap computed at render). `fills` stays declared and unbuilt (O16 default).

## S-HELD — his "holding X" (R67 (1))
A correction row of the entry leg: `kind = 'entry'`, `seq = 0`, `corrects` = the current entry row, `held_stated = X`, `shares = X + Σ current exit shares` computed under the card lock, `price` / `price_source` / `price_asof` copied from the row it corrects, `flag = 'confirmed'`. C1 built the column and its CHECKs; C2 built the writer, `record_held` (above).
