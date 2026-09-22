# S3 EXITS TRIBUNAL — ROUND 2 (2026-09-22)

## §0 Headline
Grok: HARNESS at launch (sandbox denied), did not rule — not a used round (L67). Gemini ruled all three: R2-1 ADOPT A (DO NOT BUILD withdrawn), R2-2 ADOPT F, R2-3 ADOPT C — closing `TRIBUNAL R2: BUILD`. Astra: METER — proceed on three (expected, R13).
Converged 2 of 3 (R2-1, R2-3); R2-2 SPLIT — gemini's only ruling, but its (c) citation of grok's own scenario numbers DOES NOT HOLD in file-check.
Fable R1 claims file-checked: 9 of 9 HOLD (C3's DB-acceptance half named UNVERIFIABLE = v2's own X4). Redactions: 0.
Packet staged at 152,651 B, still over 130 KB after all three authorized drops (no further drop authorized).
ESCALATE: 4.

## AUTHORIZATION
Verified, each its own Bash call, before staging:
- `grep -n "^| R13 " cto-2026-09-20.md` → line 86, "Push and approved everything..." — the BARS TRIBUNAL rule list origin.
- `grep -n "^| R23 " cto-2026-09-20.md` → line 206, extends `Bash(grok *)`/`Bash(agy *)` through Monday 09-21 23:59 ET.
- `grep -n "^| R38 " cto-2026-09-20.md` → line 275, carries "B with your addition" (stop-override authority).
- `grep -n "^| R46 " cto-2026-09-21.md` → line 57, carries "For the designs and creations we need the higher level models."
- `grep -n "^| R13 " cto-2026-09-22.md` → line 82, carries "without Astra" — this week's three design tribunals run on Grok · Gemini · Fable.
- `grep -n "^| R62 " cto-2026-09-22.md` → line 36, carries "S3 exits tribunal ROUND 2" and "NEEDS ROUND 2" — this round's authorization, three items only.
- `git log -1 --format=%H -S"| R62 | " -- cto-2026-09-22.md` → `61dd5802b...` (non-empty). Committed.
- `git log -1 --format=%H -S"S3 EXITS DERIVED v2" -- s3-exits-tribunal-derive-2026-09-22.md` → `cda7bf19...` (non-empty). Committed.
- `git log -1 --format=%H -- "docs/30 - Design/S3-EXITS-v2-2026-09-22.md"` → `cda7bf19...` (non-empty). v2 is committed.
- `tail -n 3 s3-exits-tribunal-derive-2026-09-22.md` → last non-blank line `S3 EXITS DERIVED v2 · folds: 42 · verbatim: 26 · needs round 2: 3 · owner items: 20 · ESCALATE: 8`. Matches (stop line, "needs round 2: 3").
- `grep -n "35-s3-exits-tribunal-r2.md" cto-2026-09-22.md cto-2026-09-23.md` → cto-2026-09-23.md does not exist (not fatal); cto-2026-09-22.md line 35, row R63, 14:59 ET, "STAGGER for `35-s3-exits-tribunal-r2.md`: 16 is not running · 28 is not running · `23` ended FAILED PREFLIGHT (its report exists)." — the launch row.
- `git log -1 --format=%H -S"35-s3-exits-tribunal-r2.md" -- cto-2026-09-22.md cto-2026-09-23.md` → `6dbaa36a...` (non-empty). Launch row committed.
- Rule-not-added check: each of the 14 allow strings and 3 deny strings grepped (`grep -c -F`) against `prompts/2026-09-20/08-bars-chunk-e-check.md` → every count ≥1 (grok/agy strings counted 2, matching the recorded precedent). No Sol/Opus checker string in the launch line.
- `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" cto-2026-09-22.md` → line 65, row R30, 13:0x ET, "Approved" (his word, quoted).
- `git log -1 --format=%H -S"Bash(grok *) and Bash(agy *) through 2026-09-23 23:59 ET" -- cto-2026-09-22.md` → `055242df...` (non-empty). Committed.
- DATE + EXTENSION GATE: `date` → Tue Sep 22 14:59:13 EDT 2026 (row 1, first PREFLIGHT); 2026-09-22 is within the R30 window (through 2026-09-23 23:59 ET); not within 19:25–20:45 ET nor at/after 23:20 ET. Second check immediately before launch: Tue Sep 22 15:14:30 EDT 2026 — same day, same clearance, outside both windows.

All gates PASSED. Proceeding.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| DATE + EXTENSION + WINDOWS (row 1) | `date` | 0 | ALLOWED — Tue Sep 22 14:59:13 EDT 2026, within R30 window, outside both forbidden windows |
| grok version | `grok --version` | 0 | ALLOWED — grok 1.0.25 (f7e67d6988e2) [stable] |
| agy version | `agy --version` | 0 | ALLOWED — 1.2.8 |
| round-1 folder exists | `ls scratch/tribunal-bars-0920/s3-exits-tribunal` | 0 | ALLOWED — lists `r1` |
| round-2 folder (RECOVERY) | `ls scratch/tribunal-bars-0920/s3-exits-tribunal/r2` | 1 | ALLOWED — "No such file or directory" = fresh run |
| STAGGER s1 (`16`) | `tail -n 3 setups-check-r2-2026-09-22.md` | 1 | ALLOWED — file does not exist; launch row R63 (cto-2026-09-22.md:35) names `35-s3-exits-tribunal-r2.md` and states "16 is not running" → 16: no report — not running (launch row), continue |
| STAGGER s2 (`23`) | `tail -n 3 setups-blind-code-2026-09-22.md` | 0 | ALLOWED — last non-blank line `FAILED PREFLIGHT: 15 is editing setups-c1 — the source you would stage is in flight` (starts with FAILED, not running) — not blocking |
| STAGGER s3 (`28`) | `tail -n 3 handicap-h1-check-2026-09-22.md` | 1 | ALLOWED — file does not exist; launch row R63 states "28 is not running" → 28: no report — not running (launch row), continue |
| CODEX PROBE (astra, gate only) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (run_in_background, 3 min) | 1 | RECORDED — usage-limit text: "You've hit your usage limit... try again at Sep 26th, 2026 6:47 AM." → `astra: METER — proceed on three` (EXPECTED, R13). Proceed on Grok + Gemini. |
| DATE + EXTENSION + WINDOWS (second row, before house launch) | `date` | 0 | ALLOWED — Tue Sep 22 15:14:30 EDT 2026, same clearance |

PREFLIGHT PASSED. astra: METER — proceed on three (R13).

## Packet
Staged in `scratch/tribunal-bars-0920/s3-exits-tribunal/r2/` (Write tool created the folder). Byte counts (`wc -c`), after the three authorized drops:

| file | bytes | note |
|---|---|---|
| NEEDS-ROUND-2.md | 6,534 | |
| v2-sections.excerpt.md | 25,691 | two ranges dropped (below) |
| hub-checks.md | 2,066 | |
| fable-r1.excerpt.md | 11,388 | |
| grok-r1-own.excerpt.md | 10,506 | [RAW RULING — Grok's own]; one range dropped (below) |
| gemini-r1-own.excerpt.md | 3,264 | [RAW RULING — Gemini's own] |
| fill-path.excerpt.py | 19,023 | |
| models.excerpt.py | 2,113 | |
| schema.excerpt.sql | 12,127 | |
| runners.excerpt.py | 11,386 | |
| greps.txt | 37,099 | |
| QUESTIONS-R2.md | 11,454 | |
| **TOTAL** | **152,651** | |

Pre-drop total was 162,868 B. Drops applied, in the file's required order:
1. `v2-sections.excerpt.md`'s range `:324-338` ("## L52 and the bar") — dropped, saved 3,388 B.
2. `v2-sections.excerpt.md`'s range `:222-237` ("## 10. CHUNKS") — dropped, saved 4,024 B.
3. `grok-r1-own.excerpt.md`'s `## (n)` range (experiments) — dropped, saved 3,829 B.

Total saved: 11,241 B. Post-drop total (152,651 B) is still over the 130 KB threshold. The file names only these three drops, in this order, with no further authorization to cut more — so no further drop was taken. Named under `## ESCALATE`.

REDACTION (L32): `grep -c -E` for the three literals run on every staged file → every file printed `0`. No ticker, price, share count or P&L of his appears in any staged file (the source documents already carried `[TICKER]` / `[PRICE]` redactions from round 1's own staging). 0 redactions needed this round.

`[RAW RULING]` files: `grok-r1-own.excerpt.md` (Grok's own, for Grok only), `gemini-r1-own.excerpt.md` (Gemini's own, for Gemini only).

The round-1 packet was not restaged; it stays at `../r1/`.

## Clock
| time | trigger | running houses (min since launch) | action |
|---|---|---|---|
| 15:14:30 ET | second DATE gate, before launch | none yet | cleared, launching |
| 15:14:3x ET | GROK launch attempt | — | HARNESS: `Error: Operation not permitted (os error 1)`, exit 1, immediate — recorded, not retried |
| 15:15:53 ET | GEMINI launched | gemini: 0 min | `--print-timeout 20m`, deadline 15:35:53 ET |
| 15:17:26 ET | collate step (Fable claims file-check, done while houses run) | gemini: ~1.5 min | continuing |

## Fable round-1 claims, file-checked
(Done while Gemini ran, per the file's own instruction not to be idle.)

| id | claim (report line, found with grep -n) | file:line | verdict | note |
|---|---|---|---|---|
| C1 | `transition()` takes the card row lock `SELECT … FOR UPDATE` (fable-r1 `:54`) | `cards/store.py:275-278` | **HOLDS** | read directly: `"SELECT state, grade, risk_budget, shares, used_risk FROM aset_sizings WHERE id = %s FOR UPDATE"` at :276-277 |
| C2 | `refuse_row_update()` refuses every UPDATE of a row of a table it is attached to; attached at :190, :199 (fable-r1 `:56`) | `0007_radar_cards.sql:105-111`, `:188-199` | **HOLDS** | the function unconditionally `RAISE EXCEPTION`s on any BEFORE UPDATE call; attached to `radar_score_receipt` (:188-190) and `card_dot_taps` (:196-199) — NOT to `card_stop_edits` or `aset_sizings` today |
| C3 | a partial `UNIQUE (card_id, seq) WHERE corrects IS NULL` needs no UPDATE of an old row (fable-r1 `:54`, `:221` X5) | logic only; DB acceptance = v2 X4 | **HOLDS (readable part) / UNVERIFIABLE FROM READS (DB-acceptance part, named)** | correct as pure logic — a correction always INSERTs a new row with `corrects` set, so no original row's `corrects` column is ever UPDATEd; whether Postgres accepts this index alongside the `refuse_row_update()` trigger and what `legs_current_v` then returns is not settled by a read — v2 names this X4 |
| C4 | `record_stop_edit` passes `in_trade_shares=shares` from the planned column; `mark_filled`'s UPDATE writes `recomputed_shares`, never `shares` (fable-r1 `:271`, ESCALATE 3 = round-1 FC2) | `cards/store.py:679-720`, `aset/store.py:233-240` | **HOLDS** | :679 SELECTs `shares` (the planned column) under the row lock; :720 passes it as `in_trade_shares` when FILLED; the UPDATE at aset/store.py:233-239 lists `filled_at, actual_fill, recomputed_shares, recomputed_used_risk, share_delta, distance_change_pct` — `shares` is never in that list |
| C5 | CLOSED has no outgoing edge (fable-r1 `:122`) | `cards/models.py:106` | **HOLDS** | `CardState.CLOSED: frozenset(),` — confirmed, matches `models.excerpt.py` |
| C6 | `direction` and `entry` have no UPDATE writer (fable-r1 `:129`) | `greps.txt`'s `UPDATE aset_sizings SET` grep, 14 hits | **HOLDS** | every `UPDATE aset_sizings SET` hit (cards/store.py:339,622,708,730,1032,1040,1169,1222,1246,1250,1252; aset/store.py:233; one migration) assigns state, stop/per_share_risk/shares, proximity/last_price, grade fields, conviction/score, or promoted_at — none assigns `direction` or `entry` |
| C7 | `0007_radar_cards.sql:27-40` ALTERs `"user".aset_sizings`; `0002_move_tables.sql` moved both tables to `"user"` (Fable cites `:48`; the derive `:64`) (fable-r1 `:126`) | `0007_radar_cards.sql:27-45`, `0002_move_tables.sql:46-64` | **HOLDS** | :27 `ALTER TABLE "user".aset_sizings` through a run of `ADD COLUMN IF NOT EXISTS` past :40; `0002_move_tables.sql:48` lists `('user', 'card_stop_edits')`, :46 lists `('user', 'aset_sizings')`, :64 is the `EXECUTE format('ALTER TABLE public.%I SET SCHEMA %I', ...)` line |
| C8 | `fill()` has no `before_commit` hook and commits at `:519`; `transition()` has `before_commit` (`:250`, `:360-361`) (fable-r1 `:118`, `:210`, `:253`) | `cards/store.py:429-438` (signature), `:519`, `:250`, `:360-363` | **HOLDS** | `fill()`'s signature (:429-438) carries no `before_commit` param; its only commit is `conn.commit()` at :519; `transition()`'s signature carries `before_commit=None` at :250 and calls it at :360-361 (`if before_commit is not None: before_commit()`) before its own commit at :363 |
| C9 | in `mark_filled`, an UPDATE matching 0 rows raises `RuntimeError` (`aset/store.py:252`) AFTER `fill()` has committed (fable-r1 `:62`) | `aset/store.py:217`, `:230-256` | **HOLDS** | `fill()` is called and commits internally at :217 (`CardStore(...).fill(...)`, which commits on its own connection per C8); `mark_filled` then opens a SEPARATE connection at :230 for its own UPDATE, and `if cur.rowcount != 1: raise RuntimeError(...)` at :251-256 — strictly after the `fill()` call already returned/committed |

Fable R1 claims checked: 9 HOLD of 9 checked (C3 HOLDS on its readable half; its DB-acceptance half is UNVERIFIABLE FROM READS and is the same gap v2 already names as X4 — not counted as a non-HOLD).

GEMINI completed at 15:17:52 ET (notice received), well inside its 20-minute deadline (15:35:53 ET). Its printed answer was written byte for byte (minus the harness's trailing `[exited with code 0]`) to `gemini-ruling-r2.md`.

## Rulings table
| item | grok | gemini | agreement across houses that ruled | NEITHER/OWNER gist |
|---|---|---|---|---|
| R2-1 | HARNESS — did not rule | ADOPT A | 1 of 2 ruled (gemini only) | — |
| R2-2 | HARNESS — did not rule | ADOPT F | 1 of 2 ruled (gemini only) | — |
| R2-3 | HARNESS — did not rule | ADOPT C | 1 of 2 ruled (gemini only) | — |

R2-1 `DO NOT BUILD stands/withdrawn` line, verbatim: **grok** — none (did not rule). **gemini** — `DO NOT BUILD withdrawn`.

R2-2 sub-table (a)–(g):
| sub-point | grok | gemini |
|---|---|---|
| (a) index | — (HARNESS) | F |
| (b) current row | — (HARNESS) | F |
| (c) running shares | — (HARNESS) | F |
| (d) FILLED stop-edit share read | — (HARNESS) | F |
| (e) cache after correction | — (HARNESS) | F |
| (f) where `direction` is read | — (HARNESS) | F |
| (g) two concurrent ½ taps | — (HARNESS) | F |

Closing `TRIBUNAL R2:` line, verbatim: **grok** — none (HARNESS, no ruling produced). **gemini** — `TRIBUNAL R2: BUILD`.

Per-item summary (CONVERGED requires every house that ruled it to agree AND no house's supporting claim for that answer to fail file-check; else SPLIT):
- **R2-1: CONVERGED.** Only gemini ruled; its two supporting claims (the `fill()`/UPDATE seam location, and that v2 §5 acknowledges the `record_stop_edit` share-count defect) both HOLD in file-check (below). No contradicting house.
- **R2-2: SPLIT.** Only gemini ruled, but its (c) supporting claim — the restated numbers for grok's own scenario 1 — DOES NOT HOLD against the packet's verbatim text (below): gemini gives exit shares 50 / stale `running_after=50`; grok's own scenario (staged verbatim in this packet) gives exit shares 40 / stale `running_after=60`. A file-check failure on a supporting claim means the item does not clear the CONVERGED bar, even with only one ruling house.
- **R2-3: CONVERGED.** Only gemini ruled; its two failing-scenario citations (`greps.txt:318`'s "no `.rollback.sql`" fact, and `aset/web.py:508`'s `ensure_schema()` call site) both HOLD in file-check.

The Fable seat is not counted here (its round-2 report is not read this round); the second derive counts it.

## Wording offered, verbatim
**Gemini, R2-1 (ADOPT A, `DO NOT BUILD withdrawn`):**
> The single-transaction orchestrator correctly closes the seam between `fill()` (`cards/store.py:429`) and the fill-column UPDATE (`aset/store.py:233`), and v2 acknowledges the defect of `record_stop_edit` reading the stale `shares` column (`cards/store.py:720`).

**Gemini, R2-2 (ADOPT F):**
> (a) index: F — `WHERE corrects IS NULL` enforces one original without an `is_current` flip, respecting `schema.excerpt.sql:105`.
> (b) current row: F — `MAX(id)` per `(card_id, seq)` is cleanly queryable without backwards-link traversal.
> (c) running shares: F — computed running avoids Option G's failure in scenario 1 (entry 100 corrected to 80 leaves an exit of 50 with stale `running_before=100` and `running_after=50`).
> (d) FILLED stop-edit share read: F — `legs_current_v` gives the live position, replacing the stale `aset_sizings.shares` read at `cards/store.py:720`.
> (e) cache after entry-leg correction: F — rewriting the cache in the correction's transaction keeps it synchronized.
> (f) where `direction` is read: F — `aset_sizings.direction` is never updated (`greps.txt:101`), so duplicating it on `legs` is redundant.
> (g) two concurrent ½ taps: F — serialized under the card row lock (`cards/store.py:277`); tap 1 reads running 100 and writes 50, tap 2 reads running 50 and writes 25 (X7).

**Gemini, R2-3 (ADOPT C):**
> Failing scenario for A (grok): On a Tuesday evening rollback (`cobalt db migrate --rollback`), `db_migrations` reverses but `card_stop_edits.kind` remains stranded because `cards/migrations/` has no `.rollback.sql` (`greps.txt:318`).
> Failing scenario for B (gemini): The same Tuesday evening rollback fails to revert any column changes, and `AsetStore.ensure_schema()` re-executes `ALTER TABLE` on every web request (`aset/web.py:508`).
> OWNER: O16 (striking `fills` from DECLARED_TABLES) is his decision; the build keeps it declared if he says nothing.
> EXPERIMENTS: X4 — create `"user".legs` with the trigger; UPDATE a row; INSERT two rows with the same `(card_id, seq)` and no corrects; check view and GUC default. X7 — two concurrent ½ taps on a FILLED 100-share card under the card row lock.

No `NEITHER` or `OWNER`-as-precondition wording was offered by either house this round (grok did not rule; gemini's one `OWNER` line is explicitly not a precondition).

## Checked against the files
| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| `fill()` is at `cards/store.py:429`; the fill-column UPDATE is at `aset/store.py:233` | gemini, R2-1 | `cards/store.py:429`, `aset/store.py:233` | **HOLDS** | confirmed by direct read: `def fill(` at :429; `UPDATE aset_sizings SET` at :233 = FILL-PATH.EXCERPT.PY |
| v2 acknowledges the `record_stop_edit` stale-`shares` defect | gemini, R2-1 | `docs/30 - Design/S3-EXITS-v2-2026-09-22.md` §5 (`[F-29]`) | **HOLDS** | v2 §5, staged verbatim in `v2-sections.excerpt.md`, explicitly states "Something IS needed... `cards/store.py:720` passes the planned `shares` column" |
| `WHERE corrects IS NULL` respects `0007_radar_cards.sql:105` | gemini, R2-2(a) | `0007_radar_cards.sql:105` | **HOLDS** | `:105` is `CREATE OR REPLACE FUNCTION "user".refuse_row_update()` — the trigger function a `legs` table would attach, confirmed by direct read |
| Option G scenario 1: "entry 100 corrected to 80 leaves an exit of 50 with stale `running_before=100` and `running_after=50`" | gemini, R2-2(c) | `NEEDS-ROUND-2.md` / `grok-r1-own.excerpt.md`, grok's (c) scenario 1 | **DOES NOT HOLD** | grok's own verbatim scenario 1 (staged in this packet) reads: "Entry head `running_after = 80`, exit head still `running_before = 100`, `running_after = 60`. The tail says 60 open. `80 − 40 = 40`." — exit shares are 40, not 50, and the stale figure is `running_after = 60`, not 50. Gemini's restated numbers do not match the source it is citing. Does not change ADOPT F's conclusion (F has no `running_after` column to go stale at all), but the specific citation is a misquote |
| `legs_current_v` would replace the stale `aset_sizings.shares` read at `cards/store.py:720` | gemini, R2-2(d) | `cards/store.py:720` | **HOLDS (location)** | :720 is exactly `in_trade_shares=shares if state is CardState.FILLED else None,` reading the planned `shares` column, per C4 above |
| `aset_sizings.direction` is never updated | gemini, R2-2(f) | `greps.txt:101` cited; supported by `greps.txt`'s full `direction` grep block | **HOLDS (substance); citation imprecise** | `greps.txt:101` itself is one SELECT hit among many, not the summary conclusion line (`greps.txt:102`, "no line ever assigns `direction`") — the underlying claim holds, the specific line pointed to is not the strongest one |
| serialized under the card row lock at `cards/store.py:277` | gemini, R2-2(g) | `cards/store.py:277` | **HOLDS (as a pattern citation)** | `:277` is `transition()`'s `FOR UPDATE` line — the same row-lock pattern v2 §3 Option F itself cites (`cards/store.py:275-278`) for a proposed `legs` writer; no `legs` writer exists yet to lock literally, but the pattern citation is accurate |
| `cards/migrations/` and `aset/migrations/` carry no `.rollback.sql` | gemini, R2-3 (failing scenario A) | `greps.txt:318` | **HOLDS** | `greps.txt:318` is exactly the summary line: "`aset/migrations` and `cards/migrations` carry NO `.rollback.sql` files at all — only `db_migrations` does" |
| `AsetStore.ensure_schema()` re-executes `ALTER TABLE` on every web request | gemini, R2-3 (failing scenario B) | `aset/web.py:508` | **HOLDS** | `:508` is one of seven `store.ensure_schema()` call sites inside `aset/web.py` request handlers (`greps.txt`'s `ensure_schema(` grep), confirmed |
| `cobalt db migrate --rollback` is a real command | gemini, R2-3 | `db_migrations/__init__.py` (staged in `runners.excerpt.py`) | **HOLDS** | the module docstring states exactly: "Run them with `cobalt db migrate` (... `--rollback` to reverse 0003 then 0002)" |

Duplicates of the earlier `## Fable round-1 claims, file-checked` rows: none of gemini's claims restate a C<n> row verbatim (gemini did not cite the Fable seat's text this round).

## Experiments named (L70)
| experiment | named by | = v2 X<n> or NEW | gates which chunk | result that would change the design |
|---|---|---|---|---|
| create `"user".legs` with the trigger; UPDATE a row; INSERT two rows same `(card_id, seq)` with no `corrects`; check view + GUC default | gemini | = v2 X4 | C1 (and round 2 on `[R2-2]`) | UPDATE allowed → append-only claim false; view returning two rows per seq → the chosen `[R2-2]` option's wording changes |
| two concurrent ½ taps on a FILLED 100-share card under the card row lock | gemini | = v2 X7 | C2 | two 50-share legs → lock claim insufficient; decides "one refused" vs "second writes 25" |

Both experiments gemini named are the same experiments v2 already names (X4, X7) — no NEW experiment this round.

## OWNER answers
| answer | who | precondition to build? |
|---|---|---|
| O16 (striking `fills` from `DECLARED_TABLES`) is his to decide; the build keeps it declared if he says nothing | gemini, R2-3 | **no** (explicit in the text itself) |

## Independence
`grep -c -F -e "-ruling" gemini-ruling-r2.md` → `0`. `grep -c -F -e "grok-r1-own" gemini-ruling-r2.md` → `0`. No breach. Grok produced no ruling file to check (HARNESS at launch, before any read).

## ESCALATE
- `ASK DESK: grok did not rule round 2 (HARNESS — "Error: Operation not permitted (os error 1)", exit 1, immediate at launch, before any file was read) — relaunch this same file for it alone inside the grok/agy window (through 2026-09-23 23:59 ET, R30), or take the second derive with gemini alone? [15:17 ET]` — safe default taken: no retry by me. Note for the second derive/desk: per L67, a house that produced no ruling has not used a round — this HARNESS attempt does not consume one of grok's ≤3 rounds.
- Packet staged at 152,651 B, still over the 130 KB threshold after all three authorized drops (pre-drop 162,868 B; drops saved 11,241 B). The file names only these three drops and authorizes no further cut, so none was taken. `## Packet` above has the full breakdown.
- R2-2(c): gemini's supporting citation of grok's scenario 1 numbers DOES NOT HOLD against the packet's verbatim text (exit shares 50 vs grok's 40; stale `running_after` 50 vs grok's 60) — see `## Checked against the files`. This is why R2-2 is marked SPLIT rather than CONVERGED despite being the only house to rule it.
- Redactions: 0. `grep -c -E` for the three L32 literals printed `0` on every staged file; no ticker, price, share count or P&L of his was found needing replacement.
- No `DO NOT BUILD` line survives (gemini withdrew its own round-1 line; grok produced none). No independence breach. No number proposed for one of his keys. No owner item written as a precondition. astra's probe row is exactly `METER — proceed on three` (expected, not escalated per rule).

## Clock (continued)
| time | trigger | running houses (min since launch) | action |
|---|---|---|---|
| 15:17:52 ET | GEMINI completion notice | gemini: ~2 min (well inside 20 min) | ruling written verbatim to `gemini-ruling-r2.md`; began collate |
| 15:19:57 ET | close step | none running | finalizing report |

## CONTINUE
next: none — round complete. Report ready to close.

S3 EXITS TRIBUNAL R2 DONE · grok: HARNESS · gemini: TRIBUNAL R2: BUILD · astra: METER — proceed on three · houses that ruled: 1 of 3 · converged: 2 of 3 · ESCALATE: 4
