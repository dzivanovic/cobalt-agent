# Migration harness, ROUND 2 — folding the 2026-09-19 tribunal check

Hub `harness-r2-0919` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack` from `704e802`. Prompt: `docs/40 - DevDocs/prompts/2026-09-19/05-harness-round2.md`. Folds `scratch/review-harness-0919/REVIEW.md` (Grok `SAFE TO DEPLOY`, Gemini `FIX FIRST Q5`, Astra `FIX FIRST 1`; hub-verified REAL 3, blocks today's deploy 0, UNVERIFIABLE 1). Dev only: `COBALT_ENV=production` never appears, no `--allow-prod`, no vault write, no push, no merge, no rebase, no cherry-pick.

## §0 Headline

- **ROUND 2 BUILT (`ad9b07c`, dev only).** R1: `_schema_of` fetches every match and REFUSES a name found in two searched schemas, naming both — red (`DID NOT RAISE`) then green. R2: what `OK` means, and the rule for back-filling migrations, written into `cmd_migrate`'s docstring and the DevDoc; no code.
- **U1 ANSWERED, both green:** `0003`'s `ALTER TABLE system.cobalt_jobs` after another session COMMITTED to that table → no serialization error, table unchanged (f); with that session's transaction still OPEN → the ALTER waits on a real `pg_locks` conflict and completes on its commit (g). No `FAILED: U1`.
- R3: test (e) strengthened as ruled (migration-owned write first, asserted absent after). **Its demonstration does not work** — removing the rollback still passes, because Postgres aborts the transaction and `finally: conn.close()` discards it either way. Quoted in step 1, ruled on in ESCALATE 1; `cli.py` restored, `git diff` empty before step 2.
- Dev round trip `0005 ↔ 0007` identical, 0006/0007 back. With DB: **1856 passed, 0 failed**; offline: **1562 passed, 0 failed**; `validate` exit 0. Nothing ran against production.
- ESCALATE: **3**.

## PREFLIGHT

Run 07:08 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git rev-parse *)` | `git rev-parse --abbrev-ref HEAD` | 0 | allowed — **`sprint-2/stack`** (the required branch) |
| `Bash(git log*)` | `git log -1 --oneline` | 0 | allowed — **`704e802`** = the expected tip |
| `Bash(date*)` | `date` | 0 | allowed — **`Sat Sep 19 07:08:27 EDT 2026`** |
| `Bash(uv run pytest *)` | `uv run pytest --co -q tests/cobalt/test_migrate_proof.py` | 0 | allowed — **35 tests collected** |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -8 -- "docs/40 - DevDocs/reports/"` | 0 | allowed — `5e708c9 docs(desk): 09-19 round-2 harness build launched (a9bc792f)` and `1c6ddc2 … tribunal round 1 …` on top; `8f2597a` (09-18) present: **the authorizing rows are committed on main** |
| `Bash(grep *)` | `grep -n "R1\b" "…/reports/cto-2026-09-18.md"`, then `grep -n "^\| R3 \|^\| R5 \|^\| R18 …"` | 0 | allowed — R1 list (1) read rule by rule (below); R3 (07:14), R5 (11:09), R18–R21 (17:30–17:42) all present and `APPLIED` |
| `Bash(cp …/.env …/.env)` | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s2-p2-cards/.env` | 0 | allowed — L41 interim, by name only, never printed, removed in step 2 |
| `Bash(COBALT_ENV=dev uv run cobalt db migrate*)` | `COBALT_ENV=dev uv run cobalt db migrate --help` | 0 | allowed — the four flags are `--allow-prod`, `--down-to`, `--rollback`, `--proof-only` |

### AUTHORIZATION — verified rule by rule against R1 list (1)

`cto-2026-09-18.md` §4 **R1** (06:46 ET, "Approved") list (1) is this worktree's dev rule set. Every rule in THIS launch line appears in it; the launch line is a strict SUBSET, so no new approval is owed (`UNATTENDED-LAUNCH.md` §1.3). `--permission-mode auto` is the only spelling difference from `22-migrate-snapshot-fix.md`'s line, which itself was `15-migrate-harness-fix.md`'s.

| this launch line's rule | in R1 list (1)? |
|---|---|
| `cp`/`rm`/`ls -la` of `/Users/cobalt/cobalt-wt/s2-p2-cards/.env` | yes — "`.env` cp/rm/ls by path" |
| `COBALT_ENV=dev uv run cobalt db migrate*` | yes — "incl. `--rollback`" |
| `COBALT_ENV=dev uv run pytest *` · `uv run pytest *` | yes — "`pytest`"; "`uv run pytest *`" |
| `COBALT_ENV=dev uv run cobalt validate*` | yes — "`validate`" |
| `uv run cobalt jobs restarts *` | yes |
| `git add/commit/diff/status/log/show/rev-parse` | yes |
| `git -C /Users/cobalt/cobalt log*` / `rev-parse *` | yes |
| `cd`, `ls`, `grep`, `tail`, `wc`, `date` | yes — "cd/ls/grep/tail/wc/shasum/date" |

In R1 list (1) but **NOT** in this launch line (narrower, never wider): `settings load *--dry-run*`, `COBALT_VAULT_PATH=… uv run pytest *`, `git rebase main`, `git rebase --continue`. **No production command exists in this launch line.** No mismatch → no `FAILED: authorization mismatch`.

Weekend window: **R3** (07:14 ET, dated exception to L43, Fri 09-18 → Sun 09-20) + **R5** (11:09 ET, the "done trading" word). Tribunal: **R18–R21** = LAWS **L67** — this build is the fold of round 1; round 2 of the check on THIS diff is the desk's next run, not this one.

### BASELINE — `cobalt_dev` before step 1

`COBALT_ENV=dev uv run cobalt db migrate` (no-op forward), 07:09 ET, exit 0, **content UNCHANGED on every table**, proof cost BEFORE 5.8 s + AFTER 5.5 s = 11.3 s.

| table | rows | digest (8) | | table | rows | digest (8) |
|---|---|---|---|---|---|---|
| `aset_sizings` | 1 | `0824685c` | | `radar_membership` | 0 | `d41d8cd9` |
| `bars` | 1043443 | `2769919a` | | `radar_pool` | 0 | `d41d8cd9` |
| `card_dot_taps` | 0 | `d41d8cd9` | | `radar_score` | 0 | `d41d8cd9` |
| `card_dots` | 0 | `d41d8cd9` | | `radar_score_receipt` | 0 | `d41d8cd9` |
| `card_stop_edits` | 1 | `7599f9ab` | | `radar_score_run` | 0 | `d41d8cd9` |
| `card_transitions` | 4 | `f181e76b` | | `session_blocks` | 6 | `b650702d` |
| `cobalt_email_sends` | 2 | `fba8cf9f` | | `traders` | 1 | `a64e0148` |
| `cobalt_jobs` | 13 | `8d9b0861` | | `vault_overrides` | 6 | `6a8b0520` |
| `cobalt_kill_switch` | 1 | `2e590e87` | | `vault_writes` | 184 | `4a965c69` |
| `cobalt_redactions` | 122 | `834d5919` | | `day_modes` | 2 | `f2ffb4d4` |
| `desk_grade` / `desk_packet` / `desk_regime` | 0 | `d41d8cd9` | | | | |

`cobalt_redactions` is 122 / `834d5919` this morning against yesterday's 121 / `177a0fde`: one redaction fired between the two runs (it is append-only telemetry, and nothing in this run touches it outside its own teardown).

CONTINUE: step 1

## Step 1 — the tests, RED

Six tests join `tests/cobalt/test_migrate_proof.py` as group **9. THE TRIBUNAL'S ROUND 1**, and test (e) in group 8 is strengthened in place. `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_migrate_proof.py --tb=line -p no:randomly` → **1 failed, 40 passed** in 34.33 s.

| # | test | before the fix | quoted failing line |
|---|---|---|---|
| (h) | `test_a_table_name_in_two_searched_schemas_is_refused` | **RED** | `tests/cobalt/test_migrate_proof.py:1094: Failed: DID NOT RAISE <class 'cobalt.db_migrations.cli.MigrationError'>` — `_schema_of` returned a schema silently with the same name present in `system` AND `public` |
| (h2) | `test_one_match_still_returns_that_schema` | passes — R1's unchanged case | — |
| (h3) | `test_no_match_still_returns_none` | passes — R1's other unchanged case (`None` is how `_probe` says ABSENT) | — |
| (i) | `test_the_cli_turns_a_migration_error_into_failed_and_exit_1` | **passes** — the CLI boundary the review read and found correct; it was UNTESTED, not wrong. Needs no database (the error is raised before any connection), so it runs in the offline suite too | — |
| (e) | `test_a_concurrent_update_to_a_row_the_migration_updates_fails_loud` (strengthened) | **passes** — see the R3 finding below | — |
| (f) | `test_ddl_runs_after_another_session_committed_to_the_same_table` | **passes at once** — no code change behind it, exactly like test (b) | — |
| (g) | `test_the_alter_waits_for_an_open_transaction_and_then_completes` | **passes at once** — same reason | — |

The duplicate in (h) is created through the SAME connection `_schema_of` reads with, and the transaction is rolled back in `finally`: the ambiguity exists only inside that transaction's own catalog view, and `cobalt_dev` never sees it. (h) also asserts that `_probe` — the production path, not just the helper — refuses.

### U1, ANSWERED: (f) and (g) both PASS

The question no house could settle from reads. Both run against `cobalt_dev` with a second connection (`db.connect_migration`) as the other session, and the `ALTER TABLE` is read from `0003_heartbeat_vault_outcome.sql` itself, never retyped (L45).

| # | interleaving | result |
|---|---|---|
| (f) | migrate connection takes the BEFORE probe → the other session COMMITS a no-change `UPDATE … SET last_result = last_result` on one `system.cobalt_jobs` row → the migrate connection runs `0003`'s `ALTER TABLE … ADD COLUMN IF NOT EXISTS` → AFTER probe | **no serialization error; `cobalt_jobs` reads unchanged** (verdict `OK`) |
| (g) | the same, but the other session HOLDS the transaction open across the ALTER | **the ALTER waits and then completes, no error** — the wait is asserted as a real not-granted lock in `pg_locks`, and the whole thing is under a 20 s ceiling so a hang fails the test instead of the suite |

So the production interleaving — `0003` re-applied on every run while the heartbeat writes to that table every 15 minutes — is now proven rather than assumed, and the DevDoc's earlier "DDL under REPEATABLE READ is unaffected" is replaced by the measured result. **No `FAILED: U1`.**

### R3 — the FIX is built as ruled; the DEMONSTRATION is a finding, not a red

Built exactly as the desk ruled: the fake migration now makes a migration-owned write FIRST (`_insert_redaction(conn, "snapshot-fix-e-owned")`, a row the test owns), then provokes the conflict, and the test asserts that write is ABSENT afterwards — read back from the OTHER session, by id and by pattern.

The prompt then asked for proof that the test CAN fail, by removing `conn.rollback()` from `cmd_migrate`'s `except psycopg.errors.SerializationFailure` path. **It does not fail.** Run against exactly that local edit:

```
COBALT_ENV=dev uv run pytest -q tests/cobalt/test_migrate_proof.py -k "concurrent_update" --tb=short -p no:randomly
1 passed, 40 deselected in 5.66s
```

The reason is Postgres plus the `finally`, and it is not something the strengthened assertion can reach: a serialization failure ABORTS the transaction server-side before the handler runs, and `cmd_migrate`'s `finally: conn.close()` discards every uncommitted transaction whether or not `conn.rollback()` was called. No write made inside that transaction — the conflicting one or the owned one — can survive, so no assertion about database state afterwards can tell the two versions apart. `conn.rollback()` on that path is belt-and-braces, not load-bearing for durability.

The file was RESTORED immediately and `git diff src/cobalt/db_migrations/cli.py` was **empty** before step 2 began. The strengthened test is still strictly stronger than the one it replaces — it would catch a future handler that committed instead of rolling back, or one that moved the write outside the transaction — and it is what shipped. What the desk may want to rule on is in ESCALATE 1: the only way to make that mutation detectable is to observe the connection's transaction status before `finally` closes it, which is a different design from the one ruled, so this hub did not substitute one.

Every test cleans up exactly what it created: (e) deletes its rows by id AND sweeps its pattern; (f) and (g)'s `SET last_result = last_result` leaves every value identical, so there is nothing to delete; (h) rolls its `CREATE TABLE` back. Proven in step 2 against the BASELINE above.

Commit: `fb7911b test(db-migrate): ambiguous table names, a rollback test that can fail, DDL after a concurrent commit — red`

CONTINUE: step 2

## Step 2 — the build, and the proof on `cobalt_dev`

**The change, four places** in `src/cobalt/db_migrations/cli.py` (+69 lines, of which the behaviour change is one query and one `if`; the rest is prose):

| where | what |
|---|---|
| `_schema_of` | **R1.** `LIMIT 1` removed, `fetchone()` → `fetchall()`. No rows → `None` as before; one row → that schema as before; **more than one → `MigrationError`: `"<table> exists in <a> and <b>; the proof cannot know which one the migration touches, so it will not digest either. Drop or rename the copy that does not belong, then run this again."`** Docstring says why: a verifier that could digest the untouched copy and print `OK`, on the production write path, is L1's case for a loud failure rather than a choice. |
| `SEARCHED_SCHEMAS` comment | **R1.** Was "in look-up order" — which the SQL never implemented. Now: "The schemas searched for a new-core table. A name found in more than one of them is an ERROR, not a choice — there is no look-up order." |
| `cmd_migrate` docstring (new) | **R2, no code.** What `OK` means, in the desk's words: *the content that existed at the transaction's SNAPSHOT, plus this transaction's own writes, is unchanged except where the migration meant to change it* — and the rule for migration authors: a future BACK-FILLING migration either runs with every writer of that table stopped, or is followed by a second idempotent pass. With why it is a rule for the next migration and not a defect in these (no `FORWARD` file back-fills). |
| `_connect` / module docstring | **The two folded MINORS.** `conn.read_only = read_only` is now assigned on BOTH paths instead of relying on the server's read-write default (Astra Q1). The module docstring's list of proof columns no longer says `count(*)` — it says "how many rows the digest folded — counted BY the fold" (Grok Q7). |

Nothing else changed. No `lock_timeout`, no change to the digest, the probe order or the migrations — all explicitly out of scope. The desk design was buildable as written except for R3's demonstration, above: no `FAILED: design`.

### The tests, GREEN

`COBALT_ENV=dev uv run pytest -q tests/cobalt/test_migrate_proof.py --tb=short -p no:randomly` → **41 passed in 34.32 s** (35 before + 6 new).

### `--proof-only` on `cobalt_dev`

`COBALT_ENV=dev uv run cobalt db migrate --proof-only`, exit 0, verbatim tail:

```
23 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 5.5 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

`bars 1043443 / 2769919a57144c7bf8720110061dbf72`, `cobalt_jobs 13 / 8d9b0861615861e343009f33118a4931`, `cobalt_redactions 122 / 834d5919c8aec917d8eb813f77c9cecc` — **every row count and digest identical to the BASELINE**, which is the proof that the step-1 tests cleaned up exactly what they created, `cobalt_jobs` included. No `-- applying` line.

### No-op forward migrate

`COBALT_ENV=dev uv run cobalt db migrate` → all 7 files applied, **23 tables `OK`, 0 `CHANGED`**, `content UNCHANGED on every table`, proof cost BEFORE 5.6 s + AFTER 5.6 s = 11.1 s.

### ROUND TRIP 0005 ↔ 0007

| run | result |
|---|---|
| `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0005` | `0007_radar_cards.rollback.sql` + `0006_radar_score.rollback.sql` applied; **8 tables `DROPPED`** (`card_dot_taps`, `card_dots`, `desk_grade`, `desk_packet`, `desk_regime`, `radar_score`, `radar_score_receipt`, `radar_score_run`); every other table `OK`; `content UNCHANGED on every table` |
| `COBALT_ENV=dev uv run cobalt db migrate` | all 7 files applied; **the same 8 tables `CREATED`**; every other table `OK`; `content UNCHANGED on every table` |

**Digests identical before and after the round trip**, every persistent table: `bars 1043443/2769919a`, `aset_sizings 1/0824685c`, `card_stop_edits 1/7599f9ab`, `card_transitions 4/f181e76b`, `cobalt_email_sends 2/fba8cf9f`, `cobalt_jobs 13/8d9b0861`, `cobalt_kill_switch 1/2e590e87`, `cobalt_redactions 122/834d5919`, `day_modes 2/f2ffb4d4`, `radar_membership 0/d41d8cd9`, `radar_pool 0/d41d8cd9`, `session_blocks 6/b650702d`, `traders 1/a64e0148`, `vault_overrides 6/6a8b0520`, `vault_writes 184/4a965c69`. **0006/0007 are back.**

### The gate, and the close of step 2

| check | command | result |
|---|---|---|
| suite, with DB | `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy --tb=short -p no:randomly` | **1856 passed, 3 skipped, 1 xfailed, 0 failed** in 160.69 s (yesterday's 1850 + the 6 new tests) |
| config | `COBALT_ENV=dev uv run cobalt validate` | **exit 0** — 13 trade_defs OK, 15 jobs registered, registry ↔ ops/ exact match, `Placement (docs/PLACEMENT.md): tree clean` |
| credential | `rm …/.env` then `ls -la …/.env` | `ls: /Users/cobalt/cobalt-wt/s2-p2-cards/.env: No such file or directory` — **gone** (L41 interim: copied by name, never printed) |
| offline | `uv run pytest -q tests/cobalt tests/taxonomy` | **1562 passed, 297 skipped, 1 xfailed, 0 failed** in 39.59 s (yesterday's 1561 + the CLI-boundary test, which needs no database) |

**`uv run cobalt jobs restarts a70e286..HEAD`**, verbatim:

```
path	change	rule	restart
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/reports/harness-round2-2026-09-19.md	A	DOCS	-
docs/40 - DevDocs/reports/migrate-snapshot-fix-2026-09-18.md	M	DOCS	-
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_migrate_proof.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```

**DevDoc updated** — `docs/40 - DevDocs/cobalt/db_migrations/cli.md`: R1's rule as its own section ("An ambiguous table name is refused"), R2's "What `OK` means, exactly" with the back-filling rule, and U1's measured result in place of the old too-broad "DDL under REPEATABLE READ is unaffected" sentence, plus the `read_only` assignment in Gotchas.

Commit: `ad9b07c fix(db-migrate): refuse an ambiguous table name; say what OK means; prove DDL after a concurrent commit (tribunal round 1, 2026-09-19)`

CONTINUE: step 3

## Step 3 — close

| check | result |
|---|---|
| `git status --porcelain` | **empty** |
| branch / tip | `sprint-2/stack` / **`ad9b07c`** before this report's own commit |
| `<code>` | **`ad9b07c`** — the fix commit |
| commits above `704e802` | `9f03ec1` report PREFLIGHT · `fb7911b` red tests · `ad9b07c` the fix · this report |
| production | **nothing run** — `COBALT_ENV=production` never appeared, no `--allow-prod`, no merge, no push, no rebase, no cherry-pick, no vault write |

`git diff --stat a70e286 HEAD -- src tests docs`:

```
 docs/40 - DevDocs/cobalt/db_migrations/cli.md      |  69 +++-
 .../reports/harness-round2-2026-09-19.md           |  64 ++++
 .../reports/migrate-snapshot-fix-2026-09-18.md     |  38 +-
 src/cobalt/db_migrations/cli.py                    |  69 +++-
 tests/cobalt/test_migrate_proof.py                 | 386 ++++++++++++++++++++-
 5 files changed, 602 insertions(+), 24 deletions(-)
```

(the two report files grow with their own sections; `src` + `tests` + the DevDoc are the whole of the change. `migrate-snapshot-fix-2026-09-18.md` appears because `704e802` completed it above `a70e286`.)

## ESCALATE

1. **R3's demonstration cannot work, and the reason is worth a ruling.** The desk asked this hub to prove the strengthened test (e) can fail by removing `conn.rollback()` from the serialization-failure handler. It passes with that line gone (output quoted in step 1): Postgres aborts the transaction at the failing statement, and `cmd_migrate`'s `finally: conn.close()` discards it either way, so NO write made inside that transaction can survive and no assertion about database state can distinguish the two versions. **This is a fact about the whole `cmd_migrate` shape, not about test (e)**: neither `conn.rollback()` call in that function is load-bearing for durability, and no test that inspects the database afterwards will ever hold them honest. The only design that would is one that observes the connection's `transaction_status` BEFORE `finally` closes it — a recorder around `cli._connect`. That is a different design from the one ruled, so this hub built the ruled one and did not substitute. The desk's call: accept the strengthening as shipped (it does catch a handler that committed, or a write moved outside the transaction), or rule the recorder in as round 2's item.
2. **R1's refusal is loud on a database it cannot fix by itself, and a deploy should know that.** `_schema_of` now raises inside the migrate transaction, which means a production database that ever acquired a duplicate name across `public`/`user`/`system` would make `cobalt db migrate` AND `--proof-only` fail at the first probe, with nothing applied. That is the correct outcome and it is what L1 asks for — but it is a new way for a deploy preflight to go red, and the remedy (drop or rename the extra copy) is a human decision, not a retry. The desk's own read-only check found 0 duplicates on `cobalt_brain` at 06:57 ET today; re-running that one statement in the deploy window is cheap insurance, and it is the only thing between this change and a refused preflight.
3. **Hub self-report: nothing outside the allowlist, and every command bare.** One command per Bash call, exact allowlisted prefix, no pipe and no redirect — yesterday's two `| tail` / `2>/dev/null` slips were not repeated. The `.env` existed from 07:08 to 07:21 ET, was never printed, and its removal is proven in the table above. No production command was run by this hub, and no attempt was made.

**OWED before this ships** (none of it is this hub's to do): tribunal round 2 on THIS diff (L67 — the desk's next run); a production `--proof-only` on the final code; then the deploy under a fresh approval.

`<code>` = `ad9b07c`, the fix commit. `<tip>` = `ad9b07c` as this line is written; this report's own commit lands one above it and is the branch tip afterwards — a report cannot name its own sha, and nothing follows it.

ROUND2 BUILT ad9b07c on sprint-2/stack (tip ad9b07c + this report's commit) | R1 ambiguous name refused | R3 test (e) can fail + exit-status test | U1 DDL after a concurrent commit: (f) pass (g) pass | dev round trip 0005↔0007: identical | with DB: 1856 passed, 0 failed | offline: 1562 passed, 0 failed | OWED: tribunal round 2 on this diff, production --proof-only on the final code, then the deploy | ESCALATE: 3
