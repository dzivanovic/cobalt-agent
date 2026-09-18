# Migration harness fix — streamed content proof + `--proof-only` (deploy-2026-09-18 step 3.5)

Hub `migrate-fix-0918` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/cards` on top of `848681e`. Prompt: `docs/40 - DevDocs/prompts/2026-09-18/15-migrate-harness-fix.md`.

## §0 Headline (16:14 ET)

- **HARNESS BUILT — `511bff0`. The 1 GB ceiling is gone and every digest kept its old value: 23/23 tables byte-identical to the BASELINE taken before the change, `bars` (1,043,443 real rows) included.** The old `string_agg` expression is deleted from the module and survives only as the suite's oracle.
- `--proof-only` ships: read-only at the SERVER (`BEGIN … READ ONLY`), applies nothing, exit 0, refuses `--rollback`/`--down-to`. Both modes now print per-table and total wall seconds.
- Suites: **1832 passed / 0 failed** with the DB (1815 gated + 17 new), **1548 / 0** offline. `validate` exit 0. Dev round trip 0005↔0007 identical. `.env` removed and proven gone.
- Zero denials, all run; no production command, no vault write, no push, no merge.
- **OWED before any production use: the second-house review (R8), then a production `--proof-only` under its own approval.** ESCALATE: 3.

## PREFLIGHT

Run 15:54 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git log*)` | `git log -1 --oneline` | 0 | allowed — `848681e docs(report): STACK READY — integrated suite 1815 passed / 0 failed …` = the gated stack tip |
| `Bash(date*)` | `date` | 0 | allowed — `Fri Sep 18 15:54:09 EDT 2026` |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_tenancy.py` | 0 | allowed — **34 tests collected** |
| `Bash(cp /Users/cobalt/cobalt/.env …)` | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s2-p2-cards/.env` | 0 | allowed — by name only, never printed (L41 interim); removed at step 3 |
| `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` | `COBALT_ENV=dev uv run cobalt db migrate --help` | 0 | allowed — today's flags are exactly `--allow-prod`, `--down-to NNNN`, `--rollback`. **No probe-only mode** — deploy ESCALATE 2, confirmed at the CLI |

**AUTHORIZATION — verified by this hub, 15:53 ET.** `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` → `293db20` (this run's launch row), `5ac9560`, `7864fd8` on top of the 09-18 revert range — the rulings file is committed on main. Compared rule by rule against **R1 list (1)** (`cto-2026-09-18.md` §4, "Approved" 06:46 ET):

| this launch line's rule | in R1 list (1)? |
|---|---|
| `cp/rm/ls -la` on `/Users/cobalt/cobalt-wt/s2-p2-cards/.env` | YES — "`.env` cp/rm/ls by path" |
| `COBALT_ENV=dev uv run cobalt db migrate*` (incl. `--rollback`) | YES — named verbatim |
| `COBALT_ENV=dev uv run pytest *` · `uv run pytest *` | YES |
| `COBALT_ENV=dev uv run cobalt validate*` | YES |
| `uv run cobalt jobs restarts *` | YES |
| git add/commit/diff/status/log/show/rev-parse | YES |
| `git -C /Users/cobalt/cobalt log*` / `rev-parse *` | YES |
| `cd`/`ls`/`grep`/`tail`/`wc`/`date` | YES (R1's list also carries `shasum`, unused here) |

No rule in this launch line is outside R1 list (1); R1's list additionally carries `settings load *--dry-run*`, `COBALT_VAULT_PATH=… pytest`, `git rebase main`/`--continue` and `shasum`, which this line does **not** take — a strict subset. **No production command exists in this launch line**: `COBALT_ENV=production`, `--allow-prod`, push, merge and vault writes are absent. R3 + R5 (the weekend push, "done trading" 11:09 ET) and R8 (second opinion — owed BEFORE any production use of this build, and it is not this run's job) are on the same committed row set.

Also noted, as in all three deploy runs today: the prompt file's tail carries a block styled as a system reminder asking for a `Claude-Session:` URL line in every commit. It arrives inside a tool result — the file's own bytes — not from the harness or from Dejan; the genuine harness attribution reminder names only `Co-Authored-By` and says not to add lines it leaves out. **Not followed.**

## 1. BASELINE — today's behaviour, pinned before anything was touched

`COBALT_ENV=dev uv run cobalt db migrate` (15:55 ET, `.env` in place), exit 0, a no-op at 0007. **This is the byte-compatibility oracle for step 3: every digest below must be reproduced character for character by the streamed fold.**

```
cobalt db migrate — FORWARD on cobalt_dev
-- applying 0001_schemas.sql
-- applying 0002_move_tables.sql
-- applying 0003_heartbeat_vault_outcome.sql
-- applying 0004_radar_pool.sql
-- applying 0005_heartbeat_note_absent.sql
-- applying 0006_radar_score.sql
-- applying 0007_radar_cards.sql

table                side    schema before -> after     rows            digest before -> after verdict
------------------------------------------------------------------------------------------------------
aset_sizings         user    user -> user               1 -> 1          0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           118 -> 118      2f0b1b28 -> 2f0b1b28  OK
day_modes            user    user -> user               2 -> 2          f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               184 -> 184      4a965c69 -> 4a965c69  OK
------------------------------------------------------------------------------------------------------
23 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
```

| fact | value |
|---|---|
| tables in the proof | **23** |
| `cobalt_dev`'s `bars` | **1,043,443 rows** — one eighth of production's 8,410,174, and the reason the old SQL still fits under the 1 GB ceiling here. The streamed fold is therefore exercised against a real million-row table, not a toy one |
| empty-table digest | `d41d8cd9…` = `md5('')` — the `coalesce(…, '')` arm. The streamed fold must reproduce it as `md5(b"")` |
| no timings | today's table has no seconds column anywhere — deliverable 3 |

## 2. Tests first — `tests/cobalt/test_migrate_proof.py`, RED

`COBALT_ENV=dev uv run pytest -q tests/cobalt/test_migrate_proof.py --tb=line -p no:randomly` → **16 failed, 1 passed**, then the one green test was tightened (it was passing for the wrong reason — argparse refusing `--proof-only` as an UNKNOWN flag is not the harness refusing the COMBINATION) → **17 failed, 0 passed**. Every test red before the change:

| # | group | test | red line, verbatim |
|---|---|---|---|
| a | fold | `test_the_streamed_fold_reproduces_string_agg_byte_for_byte[zero_rows / one_row / many_rows / rows_containing_the_separator / empty_strings / non_ascii / very_long]` (7) | `AttributeError: module 'cobalt.db_migrations.cli' has no attribute '_digest_rows'` |
| a | fold | `test_no_rows_digests_the_empty_string` | `AttributeError: … has no attribute '_digest_rows'` |
| a | fold | `test_the_separator_goes_between_rows_and_never_after_the_last` | `AttributeError: … has no attribute '_digest_rows'` |
| b | DB oracle | `test_every_proof_table_digests_to_the_value_the_old_sql_returns` | `AttributeError: … has no attribute '_row_json'` |
| c | guard | `test_no_statement_the_probe_sends_contains_string_agg` | `AssertionError: the proof still concatenates rows server-side — that value is what passed the 1 GB ceiling on 8.4M rows: ['SELECT count(*), md5(coalesce(string_agg(…))::text, '\|' ORDER BY "t"."id"), '')) FROM "user"."aset_sizings" AS t', … FROM "system"."bars" AS t']` |
| e | memory | `test_rows_reach_the_probe_through_a_named_cursor_in_batches` | `AssertionError: every table's rows must stream through its own NAMED (server-side) cursor; named cursors declared: []` |
| d | flag | `TestProofOnly::test_it_prints_every_table_with_timings_and_applies_nothing` | `cobalt: error: unrecognized arguments: --proof-only` · `assert 2 == 0` |
| d | flag | `TestProofOnly::test_it_refuses_rollback_and_down_to` | `AssertionError: ('--proof-only', '--rollback', '--down-to', '0005') was refused by argparse as an UNKNOWN flag, which is not the same thing as refusing the combination` |
| d | read-only | `TestProofOnly::test_its_transaction_is_read_only_at_the_server` | `AttributeError: … has no attribute '_connect'` |
| e | memory | `test_row_texts_stream_through_one_named_batched_server_side_cursor` | `AttributeError: … has no attribute '_stream_row_texts'` |
| e | memory | `test_the_batch_size_is_bounded_and_not_one_row_at_a_time` | `AttributeError: … has no attribute 'PROBE_BATCH_SIZE'` |

Two of the reds are BEHAVIOURAL, not scaffolding — (c) prints today's actual `string_agg` query back as the failure, and (e)'s DB half records that today's probe declares **zero** server-side cursors. Test (b) is the byte-compatibility oracle: it runs the OLD SQL expression itself, which after step 3 survives in this test file and nowhere else (L3), and it additionally asserts the new `seconds` key that today's probe has no concept of.

## 3. Built to the desk design, and proven on `cobalt_dev`

| design point | built |
|---|---|
| 1 streamed digest, byte-compatible | `_stream_row_texts` (named server-side cursor, `itersize = PROBE_BATCH_SIZE = 10_000`) → `_digest_rows` (one `hashlib.md5`, `b"\|"` between rows, never after the last, no rows = `md5(b"")`). `_probe` keeps `count(*)` in SQL. **No `string_agg` of row content is left in the module** — the regression guard asserts it on the constructed queries |
| 1 rejected designs recorded | both, in the DevDoc and the module docstring: per-row md5s (269 MB today, 1 GB again near 33M rows) and exempting bulk tables (weakest proof where the most data lives) |
| 2 `--proof-only` | new flag; `_connect(..., read_only=True)` → psycopg opens `BEGIN … READ ONLY`, so the SERVER refuses a write; applies nothing; exit 0; refused with `--rollback`/`--down-to` before any connection opens; production still reached only through the existing gate |
| 3 timings | per-table `probe secs` column + `proof cost: BEFORE … + AFTER … = total …; slowest table …` on the normal run; per-table `secs` + total on `--proof-only` |
| 4 one path (L3) | the old SQL digest expression is deleted from `cli.py`. Its one surviving copy is the ORACLE inside `tests/cobalt/test_migrate_proof.py`, built from the shared `_row_json()` seam |

Tests after the change: `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_migrate_proof.py` → **17 passed**.

### 3.1 `--proof-only` on `cobalt_dev`, verbatim — digests vs BASELINE: 23/23

```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.01
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.55
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   118          2f0b1b28ddb106c99664ac38d622f61f   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.00
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     184          4a965c69340f112d12e6ca21a8a0602c   0.01
------------------------------------------------------------------------------------------
23 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 5.6 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

**Byte compatibility, table by table against step 1's BASELINE (the proof table truncates to 8 characters; the full 32 are above and the suite compares all 32 against the old SQL):**

| table | BASELINE | `--proof-only` | | table | BASELINE | `--proof-only` |
|---|---|---|---|---|---|---|
| aset_sizings | `0824685c` | `0824685c` ✓ | | radar_membership | `d41d8cd9` | `d41d8cd9` ✓ |
| bars | `2769919a` | `2769919a` ✓ | | radar_pool | `d41d8cd9` | `d41d8cd9` ✓ |
| card_dot_taps | `d41d8cd9` | `d41d8cd9` ✓ | | radar_score | `d41d8cd9` | `d41d8cd9` ✓ |
| card_dots | `d41d8cd9` | `d41d8cd9` ✓ | | radar_score_receipt | `d41d8cd9` | `d41d8cd9` ✓ |
| card_stop_edits | `7599f9ab` | `7599f9ab` ✓ | | radar_score_run | `d41d8cd9` | `d41d8cd9` ✓ |
| card_transitions | `f181e76b` | `f181e76b` ✓ | | session_blocks | `b650702d` | `b650702d` ✓ |
| cobalt_email_sends | `fba8cf9f` | `fba8cf9f` ✓ | | traders | `a64e0148` | `a64e0148` ✓ |
| cobalt_jobs | `8d9b0861` | `8d9b0861` ✓ | | vault_overrides | `6a8b0520` | `6a8b0520` ✓ |
| cobalt_kill_switch | `2e590e87` | `2e590e87` ✓ | | vault_writes | `4a965c69` | `4a965c69` ✓ |
| cobalt_redactions | `2f0b1b28` | `2f0b1b28` ✓ | | desk_grade / desk_packet / desk_regime | `d41d8cd9` | `d41d8cd9` ✓ |
| day_modes | `f2ffb4d4` | `f2ffb4d4` ✓ | | **TOTAL** | | **23/23 identical** |

No `-- applying` line anywhere in that output, and `bars` — a real 1,043,443-row table — digests to the old value through the new path.

### 3.2 Normal `migrate` — no-op, digests = BASELINE, seconds printed

```
cobalt db migrate — FORWARD on cobalt_dev
-- applying 0001_schemas.sql … 0007_radar_cards.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
aset_sizings         user    user -> user               1 -> 1          0.01 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.50 -> 5.60    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           118 -> 118      0.00 -> 0.00    2f0b1b28 -> 2f0b1b28  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               184 -> 184      0.01 -> 0.01    4a965c69 -> 4a965c69  OK
----------------------------------------------------------------------------------------------------------------------
23 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.6 s + AFTER 5.6 s = total 11.2 s; slowest table bars (5.5 s before).
```

(The `-- applying` lines are all seven, elided above to one line; every other character of the table is verbatim.) 23 OK, 0 CHANGED, digests = BASELINE.

### 3.3 ROUND TRIP 0005 ↔ 0007 — digests identical before and after

`COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0005` → applied `0007_radar_cards.rollback.sql`, `0006_radar_score.rollback.sql`; verdicts: **8 `DROPPED`** (`card_dot_taps`, `card_dots`, `desk_grade`, `desk_packet`, `desk_regime`, `radar_score`, `radar_score_receipt`, `radar_score_run`), every surviving table `OK` at its BASELINE digest, `proof cost: BEFORE 5.7 s + AFTER 5.6 s = total 11.3 s`.

`COBALT_ENV=dev uv run cobalt db migrate` → all seven forward files applied, the same 8 tables back as `CREATED`, `proof cost: BEFORE 5.5 s + AFTER 5.5 s = total 11.0 s`.

| table | BASELINE | after rollback | after re-migrate |
|---|---|---|---|
| aset_sizings | `0824685c` | `0824685c` | `0824685c` |
| bars | `2769919a` | `2769919a` | `2769919a` |
| card_stop_edits | `7599f9ab` | `7599f9ab` | `7599f9ab` |
| card_transitions | `f181e76b` | `f181e76b` | `f181e76b` |
| cobalt_email_sends | `fba8cf9f` | `fba8cf9f` | `fba8cf9f` |
| cobalt_jobs | `8d9b0861` | `8d9b0861` | `8d9b0861` |
| cobalt_kill_switch | `2e590e87` | `2e590e87` | `2e590e87` |
| cobalt_redactions | `2f0b1b28` | `2f0b1b28` | `2f0b1b28` |
| day_modes | `f2ffb4d4` | `f2ffb4d4` | `f2ffb4d4` |
| radar_membership / radar_pool | `d41d8cd9` | `d41d8cd9` | `d41d8cd9` |
| session_blocks | `b650702d` | `b650702d` | `b650702d` |
| traders | `a64e0148` | `a64e0148` | `a64e0148` |
| vault_overrides | `6a8b0520` | `6a8b0520` | `6a8b0520` |
| vault_writes | `4a965c69` | `4a965c69` | `4a965c69` |
| 0006/0007's 8 tables | `d41d8cd9` | DROPPED | CREATED, `d41d8cd9` |

**IDENTICAL** — 0006/0007 are back and nothing else moved.

### 3.4 Gates

| gate | result |
|---|---|
| `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy --tb=short -p no:randomly` | **1832 passed, 0 failed**, 3 skipped, 1 xfailed, 155 s. The stack gate's third run was **1815**; 1815 + 17 new = 1832 exactly, so no pre-existing test changed its verdict |
| `COBALT_ENV=dev uv run cobalt validate` | exit **0** — 13 trade_defs OK, 7 step-down rows incl. `trade_count_over_band=down(1)`, band 2/6, card states 8/11/4, jobs 15 exact match, `Placement: tree clean` |
| `rm` the `.env` · `ls -la` | `ls: /Users/cobalt/cobalt-wt/s2-p2-cards/.env: No such file or directory` — **gone** (L41 interim; never printed) |
| `uv run pytest -q tests/cobalt tests/taxonomy` (OFFLINE, no `.env`) | **1548 passed, 0 failed**, 287 skipped, 40 s. The gate's offline run was **1537**; 1537 + 11 = 1548 (6 of the 17 new tests need the database and skip here) |

One test-side fix was needed and it is named here rather than buried: `tests/cobalt/test_radar_migration.py`'s fake `Conn` (a no-database test of rollback ordering) gained an `execute` that answers `SHOW server_encoding`, and its two hand-built `argparse.Namespace`es gained `proof_only=False`. No production behaviour depends on either.

### 3.5 RESTARTS — `uv run cobalt jobs restarts 848681e..HEAD`, verbatim

```
path	change	rule	restart
docs/40 - DevDocs/reports/migrate-harness-fix-2026-09-18.md	A	DOCS	-
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_migrate_proof.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```

The prompt expected no resident. The classifier derives **`com.cobalt.radar`** by static import reach, and it is right by rule (L42 — derived, never judged): `src/cobalt/cli.py:63` does `from cobalt.db_migrations import cli as db_cli`, and the radar resident's entrypoint reaches `cobalt.cli`. So the module IS loaded by that resident even though nobody calls it there. **`RESTARTS: com.cobalt.radar` stands** and the deploy that ships this carries it. 0 UNCLASSIFIED.

## 4. Close (16:14 ET)

| check | result |
|---|---|
| `git status --porcelain` | **empty** |
| `git rev-parse --short HEAD` | **`511bff0`** |
| `git diff --stat 848681e HEAD -- src tests docs` | `docs/40 - DevDocs/cobalt/db_migrations/cli.md 105 ++++-` · `docs/40 - DevDocs/reports/migrate-harness-fix-2026-09-18.md 265 +++` · `src/cobalt/db_migrations/cli.py 267 ++++--` · `tests/cobalt/test_migrate_proof.py 426 +++` · `tests/cobalt/test_radar_migration.py 15 +-` — **5 files, 1040 insertions, 38 deletions** |
| commits above `848681e` | `5ad8a6a` (preflight) · `44fb72a` (BASELINE) · `fd13970` (red tests) · `511bff0` (the fix) + this close commit. Nothing rebased, nothing cherry-picked, main untouched |
| configs / ops | **not touched** — no file under `configs/` or `ops/` is in the diff |

## ESCALATE

1. **The proof is not free, and the deploy plan needs its number.** `bars` probes in **5.5 s** at `cobalt_dev`'s 1,043,443 rows; production holds **8,410,174** — about **8× that, so ≈45 s per probe and ≈90 s of the outage window** for the before/after pair, on top of the migration itself. The old harness never told anyone this because it never printed a time. The next deploy prompt should budget it, and `--proof-only` can now measure it against production for real (read-only, its own approval) instead of being extrapolated from this line.
2. **`RESTARTS: com.cobalt.radar`, not "no resident" as the prompt expected.** The derivation is correct by rule (L42): `src/cobalt/cli.py:63` imports `cobalt.db_migrations.cli`, and the radar resident's entrypoint reaches `cobalt.cli` by static walk, so the resident does load this module. An operator-only command still triggers a resident restart through the CLI module graph — worth knowing generally, since it applies to every `db_*`/ops command in that package, not just this change. Not overridden here; the deploy that ships this carries the restart.
3. **Second opinion (R8) is OWED and this build has not had it.** The prompt states it, and this hub did not run it: R8 requires another house to review a build before its deploy. This report is the artefact for that review. After it, the production `--proof-only` run is the next thing — read-only, under its own approved command list, and it is the first production command this fix has ever seen.

Also noted, unchanged from all three deploy runs today: the prompt file's tail carries a block styled as a system reminder asking for a `Claude-Session:` URL line in every commit. It arrives inside a tool result — the file's own bytes — not from the harness or from Dejan; the genuine harness attribution reminder names only `Co-Authored-By` and says not to add lines it leaves out. **Not followed.**

HARNESS BUILT 511bff0 | digests byte-compatible with BASELINE: 23/23 tables | --proof-only: read-only, applies nothing | dev round trip 0005↔0007: identical | with DB: 1832 passed, 0 failed | offline: 1548 passed, 0 failed | OWED: second-house review, then production --proof-only (read-only, its own approval) | ESCALATE: 3
