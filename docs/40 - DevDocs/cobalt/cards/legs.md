# `src/cobalt/cards/legs.py`

## What it does
THE ONE WRITER of `"user".legs` (S3 exits v3 §3; L3, L40). Every leg row — the entry at the fill, the exits, the corrections, his held-count statement, the trading-log reconcile — is written here and nowhere else. S3 C1 built the entry leg only; C2 adds the exits, the running-share function and the correction writer to this module.

## The connection rule
A leg is never a transaction of its own. Every function takes the caller's open connection, runs inside the transaction the caller holds, and never opens, commits, rolls back or closes one. A connection still in autocommit (`db.connect` opens one that way) is refused before anything runs (`RuntimeError`, "…a leg is written only inside the transaction its caller holds…").

## `insert_entry_leg(conn, card_id, *, shares, price, at, flag, price_source, price_asof, source, stop_in_force, session, account_mode, day_mode_id, attested_sheet, sheet_mismatch) -> int`
Inserts the ORIGINAL entry leg (`seq = 0`, `kind = 'entry'`, `running_before = 0`; `preset`, `corrects`, `held_stated`, `source_import_id` NULL). Returns its id. A second original entry is refused by the partial unique index, not checked first. Its only caller is `AsetStore.mark_filled`, inside THE fill's transaction.

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
A correction row of the entry leg: `kind = 'entry'`, `seq = 0`, `corrects` = the current entry row, `held_stated = X`, `shares = X + Σ current exit shares` computed under the card lock, `price` / `price_source` / `price_asof` copied from the row it corrects, `flag = 'confirmed'`. C1 built only the column and its CHECKs; C2 builds the writer (here).
