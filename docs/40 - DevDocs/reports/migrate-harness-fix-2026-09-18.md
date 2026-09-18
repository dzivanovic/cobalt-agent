# Migration harness fix — streamed content proof + `--proof-only` (deploy-2026-09-18 step 3.5)

Hub `migrate-fix-0918` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/cards` on top of `848681e`. Prompt: `docs/40 - DevDocs/prompts/2026-09-18/15-migrate-harness-fix.md`.

## §0 Headline

- RUN OPEN 15:54 ET. PREFLIGHT PASS — six rules probed, **zero denials**.
- Authorization VERIFIED by this hub: every rule in this launch line is inside R1 list (1) (`cto-2026-09-18.md` §4), committed on main.
- Target: `_probe`'s `md5(string_agg(...))` → a client-side streamed md5 over a server-side cursor, byte-identical digests; plus a read-only `--proof-only` with timings.
- ESCALATE: 0 so far.

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

CONTINUE: step 3
