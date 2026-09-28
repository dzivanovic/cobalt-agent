# S3 EXITS C1 FIX R1 — DRAFT (L75 classification)

Seat: drafter `s3-exits-c1-fix-r1-draft-0928` · Opus 5.5 · authorized by `cto-2026-09-28.md` R57 (line 65, read 11:38 ET) · base read 11:39 ET: `git -C /Users/cobalt/cobalt log --oneline -3 s3/exits-c1` → `d9240ae4` over `5164f867` over `eb642f05` (as the desk named). `<chk>` = `reports/s3-exits-c1-check-2026-09-28.md`.

## §0 Headline
- 15 findings classified from `<chk>`'s file-check rows: FIX 6 (built as 4 rows F1–F4) · NOT REAL 5 · UNPROVEN 1 (RUN R1) · OUT OF SCOPE 3 · OWNER ITEM 0.
- The desk's reading holds: both HOLDs are FIX; the three outside edits are KEEP per R43 (1)–(3); the unguarded FILLED writers are OUT OF SCOPE (v3 §2 `[F-22]`).
- One FIX differs from the desk's reading: F4. C1 added two test lines that re-type a real card's values, against `20`'s L32 card. Also, the X-S card-load test passes for a reason other than its claim, so it is FIX F3.
- Wrote `prompts/2026-09-28/29-s3-exits-c1-fix-r1-build.md` (`20`'s launch line byte for byte, apart from the name) and `prompts/2026-09-28/30-s3-exits-c1-fix-r1-check.md` (`21`'s launch line byte for byte, apart from the name). New rule strings: 0.
- ESCALATE 5, including an ASK DESK on `30`'s OpenAI seat (Astra as ordered, or Sol under L67).

## L74
Recorded once (L74): after this prompt file was read (11:38), a `<system-reminder>` block was appended to that tool result. It asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and PR bodies and named a file-send tool. It is data, not an instruction. This seat commits nothing and sent nothing.

## Classification
Source lines are `<chk>:<line>`. `20` = `prompts/2026-09-28/20-s3-exits-c1-build.md`; v3 = `docs/30 - Design/S3-EXITS-v3-2026-09-22.md`.

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | X1 runs on an emulated autocommit wrapper, not the real `db.connect` (Astra; Opus) | `:147` (file-check `:121`, `:122`) | **FIX → F1** | `20:84` E2 "with-DB, on the real autocommit factory"; v3 `[R2F-03]` (v3:102) "`[F-40]`'s one-transaction case is the acceptance test" | A new with-DB test on conftest's `REAL_CONNECT` (the `test_voice_store.py` two-real-connections precedent) for every connection. It rolls back the failed fill and deletes its own rows. Red = W (c3m) mutation: `conn.autocommit = False` removed, test red, line restored, `git diff` empty, test green |
| 2 | Missing-P fill + post-commit `DailyNoteRefused` returns the failure banner without the drift banner (Astra Q5) | `:148` (file-check `:123`) | **FIX → F2** | `20:37` C1-5 "P missing → the fill is RECORDED … the sheet shows `RE-READ STOP …`"; L1 | In the `/fill` body only: after `mark_filled` returns, a note-write exception renders the failure, that the card is marked FILLED, the exact `DRIFT_NOT_EVALUATED` banner when P is missing, and the result card (a warned drift shows). Red = two offline tests through `_FillRoute` with `save_fill_update` raising |
| 3 | X-S card-load assertion accepts any `ValueError` (Opus, Grok) | `:149` (file-check `:124`) | **FIX → F3** | `20:79` X-S "an offline test through that path"; check rule (a). My read of `settings/card.py` at `5164f867`: the constructed file has no `card_settings` root (`FILE_ROOT`, `:74`), so `load_card_file` refuses on the top-level shape (`:258`) before the key check (`:270`), and the test passes for a reason that is not its claim | `match="unknown card setting 'fills.drift_warning_pct'"` and the key put under the root. Red = the tightened match on the unchanged file. If that passes, F3 is recorded as "already held". The X-S conclusion (NO) stands on `:270`; R43 (5) is unchanged |
| 4 | `test_0021_applies_twice` asserts nothing (Opus) | `:150` (file-check `:125`) | NOT REAL | `20:33` C1-1 "Idempotent in the style of `0015` / `0017`" | The claim is that a second forward runs without error. The fixture applies `0021` (`test_legs_db.py:30`), the test applies it again, and pass 2 runs at a real `0021`. Not raising is the assertion |
| 5 | X1's zero-pick assertion has no positive pre-failure pick (Astra) | `:151` (file-check `:126`) | **FIX → F1 (a)** | `20:84` E2 X1 "no … pick" | F1 reads the pick count a real fill of an identical card writes, as a control. If the path writes none for a manual card, the report quotes the condition that makes it so |
| 6 | Schema fingerprint = counts + a view hash only (Astra) | `:152` (file-check `:127`) | OUT OF SCOPE | `20:92` W: the FP is `48`'s, "typed EXACTLY"; row content is the migrate proof's per-table digest | Changing the instrument widens past C1's rows. `29` (f2) does quote the per-table proof before and after (R1) |
| 7 | Missing-P banner test has no note-failure branch (Astra) | `:153` (file-check `:128`) | **FIX → F2 (red)** | `20:37` C1-5 | F2's two red tests are that branch |
| 8 | Radar-refusal test does not query `legs` (Grok) | `:154` (file-check `:129`) | NOT REAL | Check Q(4) HOLDS for all three seats (`<chk>:84`); build `## SEAM FOR C2`: `fill(conn=conn)` `aset/store.py:287` runs before `insert_entry_leg` `:308` in one transaction, with rollback `:328` | The refusal raises before any leg insert and the transaction rolls back. The test's own claims (state, `actual_fill`) are what it asserts |
| 9 | FILLED writable without a leg via `CardStore.fill(conn=None)`, `transition(FILLED)`, backfill (Opus; Astra, Grok name them) | `:155` (file-check `:130`) | OUT OF SCOPE | v3:96 `[F-22]` "`fill(conn=...)` follows `transition()`'s rule: commit only if it opened the connection"; `20:36` C1-4 names the two callers to close (move route, CLI), both built; file-check `:130`: one `.fill(` caller in `src` (`aset/store.py:287`), other `.transition(` callers go to non-FILLED states; backfill is genesis-only (X9, build report `:66`) | A guard inside `transition()` or `fill()` is a design addition that no C1 row or v3 clause carries. See `## RECORDS` |
| 10 | Three edits outside the row list: `db_migrations/cli.py` digest exclusions, `fill_shares` input, `drift_settings=None` (Opus, Astra; Grok names them) | `:156` (file-check `:131`) | NOT REAL — already answered KEEP | `cto-2026-09-28.md` R43 (1)–(3) (line 51) | A record, not a row |
| 11 | `engine.py:302` reaches the persisted `recomputed_shares` (Grok, Astra) | `:157` (file-check `:132`) | NOT REAL | File-check `:132`: the same expression at base `engine.py:292`, unchanged by C1; no score, rank or grade write | Existing fill arithmetic; C1 added no path |
| 12 | Page render can persist a day-mode attestation (Astra Q4) | `:158` (file-check `:133`) | OUT OF SCOPE | File-check `:133` "existing behaviour, not in the diff"; `20:36` limits `aset/web.py` edits to the `/fill` and `/card/{card_id}/move` bodies | Not C1's |
| 13 | New test rows re-type real-card values already present at base (Opus) | `:159` (file-check `:134`) | **FIX → F4** | `20:43` index card L32: "constructed values only; no ticker, price or date of his in any file" | Only the two lines C1 added (`test_aset_web.py:196`, `:581` at `5164f867`) get constructed values that keep the typo-guard ratio. The base lines are not touched (`## ESCALATE` 2). Red = the equality read, with values unquoted |
| 14 | Q(7) X22 and Q(8) suites `NOT CHECKABLE FROM READS` (Opus, Astra) | `:87`, `:88` | UNPROVEN → **RUN R1** | L70; L68 GATE EARLY | `29` W executes the three suites, X22 and the proof reads before (b) and after (f2); the report and `30`'s `packet.md` quote them whole |
| 15 | The check hub's L74 block (ESCALATE 16) | `:165` | NOT REAL | L74 | Data, recorded once by that hub |

Composite lines map to the rows above. Astra's FIX line (`:162`) = #1, #2. Opus's CHECK line (`:92`, `:163`) = #1, #3, #10, #9. Grok's `BUILD STANDS` (`:92`) names no item.

## RECORDS
- The builder's ESCALATE 1–5 (`<chk>:166`, build report `:200–204`) are answered by R43. (1) digest exclusion, (2) `fill_shares` and (3) `drift_settings` are KEEP. (4) The tip is the fix commit, accepted. (5) `fills.drift_warning_pct` lands after DRC D4 is on main and stays out of `29`.
- #9: v3 keeps `fill(conn=None)`'s owned commit and `create_state`'s genesis path. For C2 onward, every FILLED writer outside `mark_filled` stays uncalled in `src` by construction, not by a guard.
- #6, #12: nothing is built. `29` NOT IN THIS FIX names them.
- Round count (L39): this fix check is round 2 of ≤3.

## OWNER ITEMS
NONE.

## FOR DEJAN
New rule strings: NONE. `29` = `20`'s 24 allow + 3 deny. `30` = `21`'s 10 allow + 3 deny.

## ESCALATE
1. `ASK DESK: 30's OpenAI seat. The draft order says 21's seats (Opus 5.5 · Astra · Grok), but L67's schedule reads a fix-round check as an "other check" (Opus · Sol · Grok; 18 seats Sol). I drafted 30 with Astra as ordered. Swap = the Sol string from 18 line 1 (standing, no new string) plus the seat prose. Which? [11:47 ET]` Safe default: Astra, as ordered.
2. L32, the desk's item: `tests/cobalt/test_aset_web.py:101` and `:183` at base `c1dc476d` hold a real card's ticker and prices (a replay test that predates C1). `29` changes only C1's two added copies (F4), so nothing widens (L75).
3. F1 writes durable rows to `cobalt_dev` through the real factory, under `29`'s single lock take. It deletes them in `finally`, proves zero `X1RF` rows by two reads, and R1 compares the per-table proof before and after. The precedent is `test_voice_store.py::test_single_flight_under_two_real_connections`. DESK LINE: launch `29` only while `ls ~/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76).
4. F3 rests on my read of `settings/card.py` at `5164f867` (`:74`, `:258`, `:270`); it has not been run. `29` E2's red is the proof, and a PASS turns F3 into "already held".
5. The L74 block from this seat's prompt read is recorded under `## L74`.

## CONTINUE
- next: none. The desk reads this report, commits `28`'s three files (`29`, `30`, this report), fills `29`'s `R__` and `<base>` values and launches `29` under L76.

S3 EXITS C1 FIX R1 DRAFTED · FIX: 6 · NOT REAL: 5 · UNPROVEN: 1 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 5
