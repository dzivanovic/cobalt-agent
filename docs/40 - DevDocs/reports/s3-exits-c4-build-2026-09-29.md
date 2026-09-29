# S3 EXITS C4 BUILD — 2026-09-29

Prompt: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-28/26-s3-exits-c4-build.md` · seat `s3-exits-c4-build` · Opus 5.5 · started 09:17:47 EDT (`date`).

## §0 Headline
- **FAILED at W: I left 3 stray test cards on `cobalt_dev` (12671, 12672 `X1RF`; 12707 `X7CT`; 9 transitions).** I ran two pass-2-only real-connection tests at `0013`; their cleanup failed. W cannot go green over those rows, and I have no command that deletes. Desk: delete them, then relaunch with `CONTINUE: W` (ESCALATE 0).
- C4 is built at **`d05ae72d`**:
  - the fill writes the card's trade note (his blank keys filled only while blank, R35 (3)) and `leg-0`;
  - `trade_note_path` is set, or NULL with a banner and a retry;
  - every leg / correction / held count writes its `leg-<seq>` unit;
  - `cobalt cards trade-note <id>` is the retry;
  - C4-06 refuses NaN / ≤ 0 tap prices (422).
- Offline **3318/0** and live-note **146/0** on `d05ae72d`. Every C4 with-DB test passed at E3 (take 2). The with-DB W was not run. `cobalt_dev` is at `0013` (F0); `.env` removed. RESTARTS `com.cobalt.aset com.cobalt.radar`.
- X: 4 of 4 run (X2 not run by design). **X3 is design-changing:** the vault writer lets his edit win only once; the next write of that unit replaces it (pre-existing, ESCALATE 1).

## L74
A system block attached to this session's context asks for a `Claude-Session: https://claude.ai/code/session_…` line in every commit message and PR body and names a file-send tool. Recorded once here (L74); not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`<D>` = `2026-09-29` (`date` → `Tue Sep 29 09:17:47 EDT 2026`).
| gate | command | result |
|---|---|---|
| placeholder `R__` | `grep -n -E "R_[_]" "…/prompts/2026-09-28/26-s3-exits-c4-build.md"` | no output (exit 1) — PASS |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" "…/26-s3-exits-c4-build.md"` | one hit, `68:` = this gate's own line — PASS |
| R67 | `grep -n "^| R67 " "…/reports/cto-2026-09-22.md"` | `99:| R67 | 15:48 ET | S3 EXITS R2-2 … This is why the DasTrader Pro import file is very important. …` — PASS |
| R67 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"DasTrader Pro import file is very important" -- "docs/40 - DevDocs/reports/cto-2026-09-22.md"` | `3eeedaa97db9dd8cc7c1ff15aabbaad4b0c9931a` — NON-EMPTY, PASS |
| R35 | `grep -n -F "| R35 |" "…/reports/cto-2026-09-28.md"` | `44:| R35 | 09:27 ET | **P-HIS — "Approved as recomended"** … (3) O5 / O6 = A: Cobalt fills his trade-note keys only while blank, never overwrites (L28) …` — carries `Approved as recomended` and `O5 / O6 = A` — PASS |
| R37 | `grep -n -F "| R37 |" "…/reports/cto-2026-09-29.md"` | `45:| R37 | 08:52 ET | — DESK RECORD: … defects that HOLD: 0 · ready for C4: YES …` — PASS |
| C3 CHECKED | `tail -n 3 "…/reports/s3-exits-c3-fix-r1-check-2026-09-29.md"` | last non-blank line: `S3 EXITS C3 FIX R1 CHECK DONE · round: 2 · … · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C4: YES · ESCALATE: 8` — PASS |
| launch row R49 | `grep -n -F "26-s3-exits-c4-build.md" "…/reports/cto-2026-09-29.md"` | `57:| R49 | 09:17 ET | — LAUNCH ROW (R135, NOW NEXT (a)): \`prompts/2026-09-28/26-s3-exits-c4-build.md\` · Opus 5.5 · acceptEdits · … on \`<base>\` = \`78e9df82\`; \`.env\` no matches, no with-DB run in flight (\`11\` offline); C3 CHECKED …; his approval word for the \`.env\` pair: "Approved as recomended" (09-28 R35 (1), C4's pair) …` (+ `64:` the §5 session row) — names this file, `78e9df82`, the literal `no with-DB run in flight`, his approval word — PASS |
| R49 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"26-s3-exits-c4-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-29.md"` | `22730e8ebb6016d7681d960db2dac102f23efb9e` — NON-EMPTY, PASS |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Tue Sep 29 09:17:47 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## s3/exits-c4` + `?? "docs/40 - DevDocs/reports/s3-exits-c4-build-2026-09-29.md"` (this report, written first per `20`'s REPORT rule) |
| base | `git log --oneline -1` | 0 | `78e9df82 fix(s3-c3): fix r1 — F3's with-DB test and R2 read the sheet's day from the suite clock` = `<base>` |
| no code past C3 tip | `git -C /Users/cobalt/cobalt log --oneline 78e9df82..s3/exits-c4 -- src tests configs` | 0 | empty |
| no `.env` here | `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/s3-exits-c4/.env: No such file or directory` |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| writer | `grep -n "def upsert_trade_note" src/cobalt/prefill/trade_note.py` | 0 | `118:def upsert_trade_note(` |
| unit | `grep -n "def upsert_unit" src/cobalt/vaultwrite/writer.py` | 0 | `644:    def upsert_unit(` |
| create | `grep -n "def create_if_absent" src/cobalt/vaultwrite/writer.py` | 0 | `559:    def create_if_absent(self, path: Path, template: str) -> WriteResult:` |
| pattern | `grep -n "trade_filename_pattern" configs/cobalt/prefill.yaml` | 0 | `14:  trade_filename_pattern: "Trade-%Y-%m-%d %H-%M-%S -{ticker}.md"` |
| column | `grep -n "trade_note_path" src/cobalt/db_migrations/0021_legs.sql` | 0 | `112:    ADD COLUMN IF NOT EXISTS trade_note_path TEXT,` |
| `/size` caller | `grep -n -F "upsert_trade_note(" src/cobalt/aset/web.py` | 0 | `1042:        trade_path, trade_action = upsert_trade_note(result, when, prefill_paths)` |
| templates (READ ONLY) | `ls "/Users/cobalt/Vault/Think/5 - Templates"` | 0 | `Cobalt Tasks.md` · `Daily.md` · `DRC.md` · `Individual Trade Template.md` · `Strategy.md` · `TRADE REPORT CARD.md` |
| strategies (READ ONLY) | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 notes listed (`9 EMA Reclaim.md` … `VWAP Continuation.md`) |
| restarts, empty range | `uv run cobalt jobs restarts 78e9df82..HEAD` | 0 | (venv created first) `path	change	rule	restart` · `docs/40 - DevDocs/reports/s3-exits-c4-build-2026-09-29.md	A	DOCS	-` (this untracked report) · `RESTARTS: none` |

## E0 BASELINE
On `<base>` `78e9df82` src, no `.env`.
- offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, from 09:19) → **`1 failed, 3296 passed, 462 skipped, 1 xfailed, 20 warnings in 566.79s (0:09:26)`**. The one red is NOT the base's. `tests/taxonomy/test_names_rule.py:81` reads the test tree at run time. It found my own E2 test file, written into the worktree while the run was in flight (uncommitted): `AssertionError: L31 / ADR-0008 D5: a trade name is USER data … Found: ['tests/cobalt/test_s3_c4_trade_note_offline.py:206: slug 'his-own-slug' -> …']`. I fixed the test (the slug is now `example-his-own`) and re-ran it: `uv run pytest -q -rf --tb=short -p no:cacheprovider --color=no tests/taxonomy/test_names_rule.py` → `7 passed, 15 warnings in 0.87s`. The base count is 3296 + that 1 = **3297 = EXPECTED**; every other test passed.
- live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 25.11s`** (= EXPECTED). The one skip is `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`; none names `COBALT_LIVE_VAULT_ROOT`.
- Method note (as C3 fix r1's): E1 / E2 test files were written while the offline run was in flight. Pytest imports test modules at collection, so they could not enter that run, except through a test that reads the tree at run time (the names rule above). No `src` file changed before E3.

## E1 EXPERIMENTS
Committed **`0d69eeae`** `wip(s3-c4): E1 experiments` (`tests/cobalt/test_s3_c4_experiments.py`, `tests/cobalt/trade_note_support.py`, `tests/fixtures/trade_note/individual-trade-template.stripped.md`) before any src edit. Every write goes to a `tmp_path` vault through the real `VaultWriter`, with an in-memory audit store standing in for `vault_writes` (`test_replay_line.py`'s pattern). His template was read with the Read tool, READ ONLY. The fixture keeps his frontmatter keys, his headings and his structure lines byte for byte; his values, his slug list, the title expression and his bracketed prose are replaced (L45 / L32).
| X | command | result | design-changing |
|---|---|---|---|
| **X14** | `uv run pytest -q -rA -p no:cacheprovider --color=no -s tests/cobalt/test_s3_c4_experiments.py` (x14 ×2) + `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_experiments.py -k x14` | **EQUAL.** `_render_body(title)`, stripped, equals the fixture's body. The fixture's frontmatter key order equals `FIELD_ORDER`. His live template, stripped, equals the committed fixture: `3 passed, 4 deselected in 0.02s`. Two differences are not in the shape: the title is `[[<% tp.file.title %>]]` (Templater) against the code's rendered title, and his file has no final newline. No divergence to escalate. | no |
| **X3** | same file, `test_x3_create_twice_unit_edit_retry_and_race` + `test_x3_human_wins_once_without_a_race` (`-s`) | `create_if_absent` ×2 → `created`, `skipped_exists`, one body. `upsert_unit leg-0`, his hand edit, retry (same create + same unit) → his line kept, ONE override row (human wins). The retry racing a `leg-1` write through the writer's precommit gap → `ABORT: … changed on disk … (attempt 1/2)`, re-read, retried once (`racer fired 2`). Both units are present once each; no duplicated body; the override row is kept. **But his leg-0 line is REPLACED** by Cobalt's unchanged body: `X3 race: updated · racer fired 2 · override rows 1 · write rows 5 · his leg-0 line kept: False`. Without the race: `X3 no race: retry 1 unchanged kept=True overrides=1 · retry 2 updated kept=False overrides=0`. **Human wins ONCE.** The write that records his override stores HIS text as the unit's baseline (`unit_after` = the merged body, `writer.py:750` / `:766`). The next write of that unit then sees base = on-disk and takes Cobalt's body, with no new override row. This is a silent overwrite, and it is pre-existing in `vaultwrite/` (the race is not the cause; serializing note writes per card would not fix it). C4 builds nothing to fix it → ESCALATE 1. | **yes** |
| **X16** | same file, `test_x16_two_cards_same_ticker_same_second_today` | TODAY: two cards (`TEST`, different entry / stop), `when` = the same second → `X16 today: created Trade-2026-09-03 10-12-30 -TEST.md · updated Trade-2026-09-03 10-12-30 -TEST.md`. The second card's call MERGES into the first card's note and reports `updated`. So C4-2's collision refusal is built as written. | no |
| **X18** | same file, `test_x18_…` | A sizing note at `09-58-10` and a fill note at `10-12-30`, card `created_at` 09:58:09 (naive = host local, as the DRC reads it) → `X18: created_at 2026-09-03 09:58:09 -> Trade-2026-09-03 09-58-10 -TEST.md`. `find_trade_note_for_card` returns the SIZING note (within its 30 s tolerance), never the fill note. The fill note is reachable only through `aset_sizings.trade_note_path` (S-NOTE), for DRC D3. Read only; recorded for the DRC lane. | no |
| **X2** | — | NOT RUN BY DESIGN: it needs Obsidian on his vault. It is the S3 smoke's (ladder S3 smoke). | — |

## E2 RED
Red committed **`6a980cf0`** `wip(s3-c4): red` (`tests/cobalt/test_s3_c4_trade_note_offline.py`, `tests/cobalt/test_s3_c4_trade_note_db.py`) before any src edit.

**Offline** — `uv run pytest -q -rf --tb=line -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_trade_note_offline.py tests/cobalt/test_s3_c4_trade_note_db.py` → **`15 failed, 15 skipped in 0.41s`** (the with-DB file skips without `.env`). Each red, for its row's reason:
- C4-1 (13 tests: the note at the fill, manual blanks, the collision, the leg lines, the close via one / two / an estimated exit leg, his `exit_price` / `trade_def` never overwritten, a Cobalt-filled value never rewritten, an absent key never added, `profit_loss` / `RVOL` never written): `AttributeError: module 'cobalt.prefill.trade_note' has no attribute 'his_fills'` / `… 'render_leg_line'`. `test_the_sizing_note_is_written_by_the_same_writer_from_the_card` → `TypeError: upsert_trade_note() got an unexpected keyword argument 'entry_price'`. `test_size_route_passes_the_card_to_the_one_writer` → `TypeError: 'SizingResult' object is not subscriptable` (`/size` still passes the `SizingResult`).
- `test_market_reset_refuses_the_note_write` → `AttributeError: … 'his_fills'` (the gate is the writer's own; the test needs the new call shape).

**With-DB — LOCK TAKE 1:**
- Lock (a): `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`.
- Lock (b): `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 29 09:29 /Users/cobalt/cobalt-wt/s3-exits-c4/.env`. **L76 lock taken 09:29:37.** Every `COBALT_ENV=dev` call was directly preceded by `ls -la /Users/cobalt/cobalt-wt/s3-exits-c4/.env` (LISTED).
- `<FP>` (C3 fix r1's query, copied under W) → `664	35	272c95bbb12241e3611e4b36326ccf87` → **F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** (= C3 fix r1's F0).
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `legs user - - -` and `voice_turns user - - -` → **`0013`**. Also: `aset_sizings 1 0824685c…`, `card_stop_edits 1`, `card_transitions 4 f181e76b…`, `cobalt_redactions 195 184322f7…` (a system table outside this build), `vault_overrides 6`, `vault_writes 187 2c8181e1…`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `code: 6a980cf0 (DIRTY: 1 path(s))` (this report).
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_s3_c4_trade_note_db.py` (M1 applied inside the suite transaction) → **`13 failed, 2 passed in 2.73s`**. Each red, for its row's reason:
  - C4-2: `test_a_radar_fill_writes_its_note_the_path_and_leg_0` → `assert [] == ['Trade-2026-...-00 -ZZPB.md']` (no note at the fill). `test_a_manual_fill_writes_its_note_with_trade_def_blank` → `assert 'trade note created: 1 - Trading/2 - Trades/Trade-2026-09-03 10-00-00 -TEST.md' in '<!doctype html>…'`. `test_two_cards_one_ticker_one_second_is_refused_never_merged` → `FileNotFoundError: … Trade-2026-09-03 10-00-00 -TEST.md`. `test_a_vault_write_failure_leaves_the_card_filled_and_the_path_null` → `assert 'FILLED — trade note NOT written: constructed vault failure · trade_note_path NULL · retry: cobalt cards trade-note 12605' in '<!doctype html>…'`. `test_a_radar_fill_with_a_failed_note_says_so_and_the_retry_writes_every_leg` → `KeyError: 'trade_note_path'`.
  - C4-3: `test_a_half_writes_leg_1_…`, `test_his_edit_of_a_leg_line_wins_…`, `test_a_close_through_one_confirmed_exit_…`, `test_a_close_through_two_exits_…` → `FileNotFoundError: … Trade-2026-09-03 10-00-00 -ZZPB.md` (no note).
  - C4-06 (the R1 runs as tests): `test_a_nan_exit_price_is_refused_before_the_writer` → `AssertionError: {"status":"ok","card_id":12612,"leg_id":2,"shares":50,"running_before":100,"running_after":50,"closed":false,"transition_id":null,"flag":"confirmed"}` / `assert 200 == 422` (**today 200, and a NaN leg is stored**). `test_a_negative_correction_price_is_refused_verbatim` → `AssertionError: Internal Server Error` / `assert 500 == 422` (**today 500**).
  - C4-4: `test_the_retry_in_market_reset_is_refused_and_writes_nothing` → `FileNotFoundError` (no note to protect). `test_the_retry_refuses_a_card_that_is_not_filled` → `AttributeError: module 'cobalt.cards.cli' has no attribute 'cmd_trade_note'`.
  - PASSED on base, as expected: `test_a_fill_that_rolls_back_writes_no_note` (a guard: base writes no fill note at all) and `test_x3_human_wins_once_on_the_real_store` (X3 on the REAL `vault_writes` store: `X3 real store: retry 1 unchanged kept=True overrides=1 · retry 2 updated kept=False overrides=0 · override rows 1`). This confirms the offline X3 finding on the real store.
- `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` = F0 (unchanged). Nothing left behind: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN ('TEST', 'ZZPB') GROUP BY ticker"` → `ticker	count` (no rows).
- Lock (d): `rm /Users/cobalt/cobalt-wt/s3-exits-c4/.env`; `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` → `ls: /Users/cobalt/cobalt-wt/s3-exits-c4/.env: No such file or directory`. **`.env: removed, proven gone (E2) — L76 lock released 09:30:01`** (held 09:29:37 → 09:30:01). No migration applied in this take.

## E3 THE ROWS
Feat commit **`d05ae72d`** `feat(s3): C4 — F22 trade note at the fill, leg units, trade_note_path, the retry CLI (v3 §7)` (11 files, 604 insertions, 67 deletions). No migration. Nothing in `prefill/drc.py`, `prefill/daily.py`, `drc/`, `cards/legs.py`, `cards/store.py`, `radar_panel.py`, `db_migrations/`.
| row | built | file:line at `d05ae72d` |
|---|---|---|
| **C4-1** ONE NOTE WRITER | `upsert_trade_note(card, when, prefill_paths, *, entry_price, fills=None, legs_section=False, create_only=False, writer=None, db_name=None, dry_run=False)` takes the card mapping, not `SizingResult`. It creates with his keys pre-filled from `fills`; the merge sets a key of his only where the file's value is blank (`_is_blank`: `key:`, `""`, null). A present value is kept; an absent key is never re-added (`_render_frontmatter(…, every_key=False)`). `his_fills(card, legs)` gives the four sources (O5 / O6). `profit_loss` and `RVOL` are never in it. A new fill note gets the empty `cobalt-legs` section after `_render_body` (unchanged). `render_leg_line`, `leg_unit_id`. `FIELD_ORDER` unchanged. | `prefill/trade_note.py:221` (writer), `:181` (`his_fills`), `:205` (`render_leg_line`), `:121` (`_render_frontmatter`), `:157` (section), `:74` (`LEGS_SECTION`) |
| **C4-2** THE FILL EVENT | `write_card_note(card_id, *, retry=False)`: the session gate (`:367`); then `AsetStore.card_for_note` + `legs.read_position`; the path from the FILLED transition time (ET) + `trade_filename_pattern`, claimed by `AsetStore.set_trade_note_path` (`:373`); `upsert_trade_note(create_only=not retry)`; one `upsert_unit` per current leg. Any failure → `set_trade_note_path(card_id, None)` (`:386`) and re-raise. Web: `_fill_note` (`web.py:1542`) runs after `mark_filled` returned, in `/fill` (`web.py:1182`, after the daily-note block) and in `radar_card_fill` (`web.py:1640`). Failure → `FILLED — trade note NOT written: <reason> · trade_note_path NULL · retry: cobalt cards trade-note <id>` (sheet: a `warn` div; panel: `notice`, first). The panel payload carries `trade_note_path`. Store: `set_trade_note_path` (`store.py:419`) — one transaction, `pg_advisory_xact_lock(hashtext(path))` (`:430`), a path another card holds → `TradeNoteRefused` (X16); `card_for_note` (`store.py:397`, a read). | `prefill/trade_note.py:341`; `aset/web.py:1542`, `:1182`, `:1640`; `aset/store.py:397`, `:419` |
| **C4-3** LEG UNITS | `write_leg_unit(card_id, leg_id, *, closed)` (`trade_note.py:395`): `trade_note_path` NULL / file absent → `TradeNoteRefused`, nothing written; else `upsert_unit(path, 'cobalt-legs', 'leg-<seq>', render_leg_line(current leg))`; `closed` → `upsert_trade_note` (exit keys while blank). Web `_leg_note` (`web.py:1562`) after `record_exit` (`:1705`), `record_held` (`:1731`), `record_correction` (`:1768`). Failure → `leg saved, note unit NOT written: <reason> · retry: cobalt cards trade-note <id>` (panel `notice`, sheet banner). Human wins through the writer's merge (override row); no reverse parse. | `prefill/trade_note.py:395`; `aset/web.py:1562`, `:1705`, `:1731`, `:1768` |
| **C4-4** THE RETRY CLI | `cobalt cards trade-note <card_id>` → `cmd_trade_note` → `write_card_note(card_id, retry=True)`. It prints `card <id>: trade note <action>: <path>`, `  leg-<seq>: <action>` per unit, `trade_note_path: <rel>`. `market_reset` → `REFUSED card <id>: <gate message> Nothing written.`; else `FAILED card <id>: trade note NOT written: <reason> — trade_note_path NULL` (both exit non-zero). | `cards/cli.py:138`, parser `:259` |
| **C4-5** DEVDOCS | `prefill/trade_note.md`, `aset/web.md` (the note calls, C4-06), `aset/store.md` (S-NOTE), `cards/cli.md` (`trade-note`) — each a dated `2026-09-29 — S3 exits C4` section. | `docs/40 - DevDocs/cobalt/**` |
| **C4-06** A TAP PRICE IS POSITIVE | `_tap_price`: after the `Decimal` parse, `not price.is_finite() or price <= 0` → `_TapInputRefused(f"REFUSED: {what} {raw!r} is not a positive price. Nothing written.")` → 422 through `_card_tap`, before any writer. No other change. | `aset/web.py:1488` |

Test edits at E3 (named, not hidden):
- `test_prefill_trade_note.py`: its 4 calls moved to the card signature through a local `upsert(result, when, paths)` helper that passes what `/size` now passes. Assertions unchanged.
- `test_s3_c4_experiments.py::test_x16_…`: E1's run was quoted above. At the tip it keeps the measured merge (without `create_only`) and adds the fill event's refusal.
- `test_s3_c4_trade_note_db.py` (after red):
  - the manual note's `entry_price` expectation `"10.10"` → `"10.1000"` (the entry leg's stored `numeric(14,4)` price — the fill price the row holds, L57);
  - the manual failure test uses `monkeypatch.context()` (a bare `undo()` would also undo the suite's DB and clock patches);
  - the market-reset regex `market_reset` → `MARKET RESET` (the gate's own text).

E3 runs (no `.env` unless named):
- `uv run pytest -q -rf --tb=short -p no:cacheprovider --color=no tests/cobalt/test_s3_c4_trade_note_offline.py tests/cobalt/test_s3_c4_experiments.py tests/cobalt/test_prefill_trade_note.py` → **`21 passed, 4 skipped in 0.80s`**. The first E3 run had 1 red: `test_a_key_absent_from_the_file_is_never_added` — the merge re-added his deleted `exit_time:` blank. I fixed it in `_render_frontmatter(every_key=False)`.
- Neighbours (C3's list + `test_voice_fix_r1_runs.py`): `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/cobalt/test_s3_c3_panel_offline.py tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_card_routes.py tests/cobalt/test_aset_web.py tests/cobalt/test_voice_card_stop.py tests/cobalt/test_radar_handicap_panel.py tests/cobalt/test_fill_c1_offline.py tests/cobalt/test_legs_c2_offline.py tests/cobalt/test_sheet_daymode_probe.py tests/cobalt/test_voice_web.py tests/cobalt/test_voice_fix_r1_runs.py` → **`321 passed, 1 skipped in 7.68s`**.
- **LOCK TAKE 2 (with-DB green check on the E3 tree, before the feat commit):**
  - Lock (a) `no matches found` → (b) `cp …/.env …/s3-exits-c4/.env`, exactly `-rw-------  1 cobalt  staff  2186 Sep 29 09:35 /Users/cobalt/cobalt-wt/s3-exits-c4/.env` → **lock taken 09:35:11**. Every `COBALT_ENV=dev` call was preceded by the listed `ls -la …/s3-exits-c4/.env`.
  - `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=short tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py` → `1 failed, 17 passed in 4.00s`. The one red is my test's regex: `Regex pattern did not match. Expected regex: 'market_reset' Actual message: "REFUSED card 12629: REFUSED (prefill.trade_note): it is 20:30:00 ET on 2026-09-02 — inside MARKET RESET, … Nothing written."` (the refusal itself is right). Every C4 row test PASSED, among them:
    - X16's captured `REFUSED card 12619: trade note 1 - Trading/2 - Trades/Trade-2026-09-03 10-00-00 -TEST.md is card 12618's (same ticker, same second, X16). Nothing merged, nothing written.`;
    - C4-06's `REFUSED: the exit price 'NaN' is not a positive price. Nothing written.` / `REFUSED: the corrected price '-1' is not a positive price. Nothing written.` (both 422);
    - the NULL-path leg's `card 12621 has no trade note (trade_note_path NULL)`.
  - Regex fixed, then `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py` → **`2 failed, 74 passed in 10.84s`**. Every C4 test and every C3 panel test PASSED.
  - The 2 reds are `test_fill_transaction_db.py::test_x1_real_factory_…` and `test_legs_c2_db.py::test_x7_two_concurrent_half_taps_…` → `psycopg.errors.UndefinedTable: relation "legs" does not exist`. These are REAL-connection tests that need `0021` truly applied: pass 1 deselects them, pass 2 runs them. **I ran them at `0013` by mistake (my command, not the code).** Their `finally` cleanup deletes `legs` first; that failed, so **the cards they wrote were NOT deleted** → ESCALATE 0.
  - `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` = F0 (schema untouched; nothing applied).
  - Stray rows, read: `SELECT s.id, s.ticker, s.state, … FROM aset_sizings s WHERE s.ticker IN ('X1RF', 'X7CT')` → `12671 X1RF TRIGGERED 2026-09-29 13:35:32.200368+00:00 3 transitions 0 picks 0 stop_edits`, `12672 X1RF TRIGGERED 2026-09-29 13:35:32.224958+00:00 3 0 0`, `12707 X7CT TRIGGERED 2026-09-29 13:35:33.663178+00:00 3 0 0`. Their transitions: `25830 25831 25832` (card 12671), `25833 25834 25835` (12672), `25974 25975 25976` (12707).
  - Totals: `aset_sizings 4 · card_transitions 13 · picks 0 · stop_edits 1 · day_modes 2 · vault_writes 187 · vault_overrides 6` (E2 proof: 1 · 4 · 0 · 1 · 2 · 187 · 6 → exactly +3 cards, +9 transitions). System: `session_blocks 6 · cobalt_jobs 13` (unchanged).
  - `cobalt db query` is READ ONLY (`src/cobalt/db_query.py:1`, `BEGIN READ ONLY` `:163`), and no listed command deletes rows, so I did not remove them.
  - Lock (d): `rm …/s3-exits-c4/.env`; `ls …/s3-exits-c4/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` → **`.env: removed, proven gone (E3 take 2) — L76 lock released 09:36:28`** (held 09:35:11 → 09:36:28). No migration applied.

## W THE THREE SUITES
**NOT RUN WITH-DB — stopped before W (b).** The three stray cards (ESCALATE 0) would make pass 1 red:
- C3's W already went red once on one stray `X7CT` card, through `test_cards.py::TestExpiry::test_expires_at_1305_on_the_2026_11_27_early_close` (C3 build report 09-28);
- `test_x1_real_factory_…` asserts `count(*) FROM aset_sizings WHERE ticker = 'X1RF' == 0` in pass 2.
So W cannot go green until the desk deletes them.
- **(a) offline** on `<tip>` `d05ae72d` (no `.env`, no lock): `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, from 09:37) → **`3318 passed, 478 skipped, 1 xfailed, 20 warnings in 553.60s (0:09:13)`**, exit 0, 0 failed. That is 3297 plus 21 new offline tests (15 trade-note + 6 experiments). Skipped = 462 + the 15 new with-DB tests + the 1 live X14 test.
- **(e) live-note** on `d05ae72d` (read only, lawful without the lock): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 25.95s`**. The one skip is `test_replay_line.py:256 … COBALT_TEST_LIVE_DRC … not set`.
- `<FP>` = C3 fix r1 report's query, copied whole (typed by me at every take above):
```
COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"
```
- W for the relaunch, planned (L60 / L19 `CONTINUE: W`):
  - **(c) PASS 1** = C3 fix r1's (c) command with its FOURTEEN `--deselect` BYTE FOR BYTE. There is NO extra C4 `--deselect`: `test_s3_c4_trade_note_db.py` applies `0021` inside the suite transaction (`legs_db_support.apply_0021`), as `test_s3_c3_panel_db.py` does, so it runs at `0013` (E3 take 2 proved it: all C4 tests PASSED at `0013`).
  - **(c3) PASS 2** = its (c3) ids BYTE FOR BYTE plus `tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py`.
  - (c2) EXPECT `legs` and `voice_turns` CREATED, no `CHANGED`; (f) rollback to `0013`, F2 = F0; (e) live-note.

## RESTARTS
`uv run cobalt jobs restarts 78e9df82..d05ae72d` (explicit shas; this report is outside the range), exit 0 — the table WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cards/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/trade_note.md	M	DOCS	-
src/cobalt/aset/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cards/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/prefill/trade_note.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_prefill_trade_note.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c4_experiments.py	A	test/documentation; no resident	-
tests/cobalt/test_s3_c4_trade_note_db.py	A	test/documentation; no resident	-
tests/cobalt/test_s3_c4_trade_note_offline.py	A	test/documentation; no resident	-
tests/cobalt/trade_note_support.py	A	test/documentation; no resident	-
tests/fixtures/trade_note/individual-trade-template.stripped.md	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row. The same pair as C3's.

## SEAM FOR THE DRC LANE
S-NOTE as built (every `file:line` at `d05ae72d`):
- **The column:** `aset_sizings.trade_note_path TEXT NULL` (C1's `0021_legs.sql:112`). It holds the fill note's path RELATIVE TO THE VAULT ROOT, e.g. `1 - Trading/2 - Trades/Trade-2026-09-03 10-00-00 -ZZPB.md` = `trades_dir` + `/` + `trade_filename_pattern` at the FILLED transition's time in ET (`prefill/trade_note.py:88` `trade_note_relative_path`).
- **The one writer:** `AsetStore.set_trade_note_path(card_id, path_or_none)` (`aset/store.py:419`).
  - It is called in the fill's request, AFTER `mark_filled` committed: first with the path (the intent, `trade_note.py:373`); then, on ANY failure of the note, the unit or the claim, with NULL (`:386`).
  - A path another card holds is refused under `pg_advisory_xact_lock(hashtext(path))` (`store.py:430`).
  - **A FILLED / CLOSED card with NULL = its note is missing** (the page said so; `cobalt cards trade-note <id>` is the retry).
  - A card filled before C4 has NULL too: it had no fill note. A /size sizing note is never pointed at (O4 A).
- **The read the note is written from:** `AsetStore.card_for_note(card_id)` (`store.py:397`) — the row + `filled_transition_at` / `closed_transition_at`.
- **X18 for DRC D3:** `prefill/drc.py:101` `find_trade_note_for_card` (nearest filename timestamp to `created_at`, ±30 s) returns a manual card's SIZING note, never its fill note. The pointer is the column. C4 did not edit `prefill/drc.py` or `prefill/daily.py`.
- **The fill note's shape** (what D3 reads):
  - his template's frontmatter (`FIELD_ORDER`) and body;
  - `entry_price` = the entry leg's price;
  - `entry_time` / `exit_time` / `exit_price` / `trade_def` filled while blank (O5 / O6);
  - one section `<!-- cobalt:section cobalt-legs -->` with one unit `<!-- cobalt:unit leg-<seq> -->` per current leg seq.

## FOR THE CHECK
- Range **`78e9df82..d05ae72d`**:
  - `0d69eeae` `wip(s3-c4): E1 experiments`
  - `6a980cf0` `wip(s3-c4): red`
  - `d05ae72d` `feat(s3): C4 — F22 trade note at the fill, leg units, trade_note_path, the retry CLI (v3 §7)`
  - then this report's commit.
- Red → green per row (red at `6a980cf0` on `<base>` src; green on the E3 tree = `d05ae72d`, E3 take 2): every C4-1 / C4-2 / C4-3 / C4-4 / C4-06 test quoted red under `## E2 RED` PASSED under `## E3 THE ROWS` (offline `21 passed`; with-DB the C4 file 14 of 15, the 15th my regex, fixed and PASSED in the 76-test run).
- Suites: E0 offline 3297 (1 red from my in-flight file, explained) · live-note `146 passed, 1 skipped`. W: offline on `d05ae72d` under `## CONTINUE`. With-DB W NOT RUN (ESCALATE 0).
- F0 per take: take 1 (E2) F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, end = F0; take 2 (E3) end = F0. No forward in either. Lock: take 1 09:29:37 → 09:30:01 · take 2 09:35:11 → 09:36:28.
- Worth a checker's eye:
  - The fill note is created at the FILLED time in ET. Its units: `leg-<seq>`, one per current leg.
  - `his_fills` sources: `exit_price` only for ONE current exit leg that is `confirmed`.
  - `set_trade_note_path` claims under an advisory lock.
  - `create_only` refuses an existing file even when no card claims it.
  - The note helpers swallow every failure into a notice (the DB write has committed). Offline (no DB), the C3 panel tests' fill / tap routes now carry a `FILLED — trade note NOT written: …` or `leg saved, note unit NOT written: …` notice; no test asserts its absence (`321 passed`).
  - `_render_frontmatter(every_key=False)` changes the merge: an absent key of his is no longer re-added blank.
- Stop line: the last line of this file.

## CONTINUE
next: W — after the desk deletes the 3 stray cards (ESCALATE 0).
- Done: AUTHORIZATION, PREFLIGHT, E0, E1 `0d69eeae`, E2 `6a980cf0`, E3 `d05ae72d`, W (a) offline 3318 and (e) live-note 146 on `d05ae72d`, RESTARTS.
- A relaunch with `CONTINUE: W` runs W whole on `d05ae72d` (or its successor):
  - (a) again;
  - the lock;
  - pass 1 = C3 fix r1's fourteen `--deselect`, byte for byte;
  - forward;
  - pass 2 = its ids + `tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py`;
  - (f);
  - (e);
  - then CLOSE.
- `cobalt_dev` is at `0013` (F0); no `.env` in any worktree.

## ESCALATE
0. **ESCALATE 0 — THE STOP: I left 3 stray cards on `cobalt_dev`.** At E3 take 2 I ran `test_fill_transaction_db.py` and `test_legs_c2_db.py` whole, at `0013`. Their two REAL-connection tests need `0021` truly applied, which is why W pass 1 deselects them. They failed on `relation "legs" does not exist`, and their `finally` could not delete what they wrote.
   - Rows: `aset_sizings` ids **12671, 12672** (`X1RF`) and **12707** (`X7CT`), all TRIGGERED, and their **9** `card_transitions` (**25830–25835, 25974–25976**). No picks, legs, stop edits, vault or system rows (totals quoted under E3).
   - Schema untouched (F0), nothing applied, `.env` removed.
   - W cannot go green over them: C3's W went red on one such `X7CT` card (`test_cards.py::TestExpiry`), and `test_x1_real_factory_…` asserts zero `X1RF` rows.
   - `cobalt db query` is READ ONLY and no listed command deletes, so I stopped.
   - **ASK DESK: delete those 3 cards and their 9 transitions (as for card 11822 on 09-28), then relaunch this prompt with `CONTINUE: W` on `d05ae72d` [09:37].** Safe default taken: stop, nothing forced. `design-changing: no`.
1. **X3 — `design-changing: yes`: human wins ONCE.** Measured offline and on the real `vault_writes` store (`X3 real store: retry 1 unchanged kept=True overrides=1 · retry 2 updated kept=False overrides=0 · override rows 1`).
   - The write that records his override stores HIS text as the unit's baseline (`vaultwrite/writer.py:750` / `:766`, `unit_after` = the merged body). So the next write of the same unit takes Cobalt's body and silently replaces his line, with no override row. That next write can be a retry, a correction, or a held count that rewrites the `leg-<seq>` unit.
   - The race (retry vs a leg write) is handled: one abort, a re-read, one retry, no duplicate, no lost override row. Serializing note writes per card would not fix this.
   - Pre-existing in `vaultwrite/`; C4 built nothing to fix it (as the prompt orders).
   - `test_vaultwrite.py:274` checks only the override COUNT after a second write, not the text.
   - For the desk: an owner of `VaultWriter._merge_base` / the baseline rule.
2. **Owner defaults taken (unruled):**
   - **O4 A** — `/size` still writes its sizing note at sizing time, through the same writer. `trade_note_path` points at the FILL note, so a manual card may have two files (X18: the DRC's nearest-timestamp match finds the sizing note).
   - **O11 A** — a radar fill writes the trade note only, no daily-note FILL UPDATE block (the radar route writes none).
   - **O12** — his daily table's `strategy` column is his template: untouched.
3. **R35 (3)'s narrower writes, as built:**
   - `entry_time` ← the latest FILLED transition `at`;
   - `exit_time` ← the latest CLOSED transition `at` (both ET, `%Y-%m-%d %H:%M`);
   - `exit_price` ← only when the card is CLOSED with exactly ONE current exit leg AND it is `confirmed` (an estimated single exit → blank; two or more exits → blank);
   - `trade_def` ← `trade_def_slug` when the card has one (radar only).
   - `profit_loss` and `RVOL` are never written.
   - The two times are rendered QUOTED (`entry_time: "2026-09-03 10:00"` — the renderer quotes every key but `date` / `symbol` / `trade_def`); `date` stays unquoted. Whether his dataview reads the quoted time as a date is X2's question — the S3 smoke's.
4. **"An absent key is never added" changed the merge render.** Before C4, the frontmatter merge re-rendered every `FIELD_ORDER` key, so a key he deleted came back blank (on the first merge after creation, which has no region baseline). Now the merge renders only the keys present (`_render_frontmatter(…, every_key=False)`); a NEW note still gets every key.
5. **The leg line, as read:**
   - An entry leg has no preset, so it renders `entry · 100 sh @ 5.4800 · 10:00 · estimated` (the spec's `<exit|entry> <preset>` with the preset omitted).
   - A held-count row renders `holding <X> (stated) · <HH:MM>` in the SAME unit `leg-0` (it is a correction of seq 0), replacing the entry line.
   - Its HH:MM is the row's `at`, which `record_held` copies from the entry leg: no statement time is stored (S-LEGS has none), so the held line shows the ENTRY's time. That is a record, never a guess.
6. **`/size`'s card:** the web passes the card's values from the sizing (`ticker`, `direction`, `stop`, the planned entry), not a re-read of the `numeric(14,4)` row, so the sizing note stays byte for byte as before (`stop_price: "225.00"`). The fill note's `entry_price` is the entry leg's stored price (`"10.1000"` for a typed `10.10`), because the stored input is the one written (L57).
7. **X16 residual:** the fill event refuses when a file already sits at the path, even if no card claims it (for example a /size sizing note of the same ticker in the same second). A later RETRY would then update that file if no card holds its path. Rare; recorded.
8. **A failed retry NULLs `trade_note_path`**, even when an earlier note was good (the prompt: on failure NULL). The file stays on disk.
9. **Lock takes:** 2 in this run (E2 reds; an E3 green check). W needs a third on the relaunch.
10. **E0's red** was my own in-flight test file (a slug the names rule refuses, `his-own-slug`); fixed to `example-his-own`. The base itself is 3297.
11. **X14:** no divergence; his template, stripped, equals the committed fixture (the live leg ran READ ONLY). Nothing for his template.
12. **L74:** recorded once under `## L74`.

**"C4 is checked by `27-s3-exits-c4-check.md` (Opus 5.5 · Astra · Grok, L67). With C4 checked, C1–C4 are the S3 exits set for ONE deploy (L43), stacked with whatever else is ready and gated on the combined tree (L68); the S3 smoke (X2 included) runs after that deploy. The builder decided nothing."**

FAILED: W — cobalt_dev carries 3 stray cards I left at E3 (aset_sizings 12671, 12672 X1RF; 12707 X7CT; card_transitions 25830–25835, 25974–25976); no listed command deletes rows — the desk deletes them, then relaunches with CONTINUE: W on d05ae72d | offline 3318/0 | live-note 146/0 | with-DB not run | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | ESCALATE: 13
