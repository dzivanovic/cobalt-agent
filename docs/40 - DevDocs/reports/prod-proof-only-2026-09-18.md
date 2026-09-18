# Production `--proof-only` — the fixed migration harness against production data (read-only)

Hub `prod-proof-0918` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/cards` at `450316c` (code `511bff0`). Prompt: `docs/40 - DevDocs/prompts/2026-09-18/17-prod-proof-only.md`.

## §0 Headline

- **PROD PROOF DONE (16:54 ET). The 1 GB failure is gone on the real table: `system.bars`, 8,591,339 rows, digested in 46.73 s, exit 0, no `ProgramLimitExceeded`.** 23 tables probed on `cobalt_brain`, one production command, run once.
- **Outage budget, now a fact: 46.9 s per probe → ≈94 s for the BEFORE+AFTER pair**, on top of the DDL. The desk's 8× extrapolation (≈45 s / ≈90 s) was good to 4%. `bars` is the only table over 100,000 rows; every other table together costs 0.18 s.
- **Nothing applied, nothing written** — `READ ONLY` at the server, no `-- applying` line, no vault write, no push, no merge (L28: no trace line owed, none made). `.env` copied by name, removed, proven gone.
- `0006`/`0007` absent: **yes** — exactly their 8 tables and no others; production confirmed at 0005. Grok's F3b answered: no `statement_timeout` under ≈47 s exists on this database.
- Dev step PASSED with one named deviation: `cobalt_redactions` drifted 118 → 120 rows against the BASELINE (append-only telemetry, deterministic on rerun, 22/23 identical) — reasoned, not silent, ESCALATE 1. **ESCALATE: 2.**

## PREFLIGHT

Run 16:51 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git rev-parse *)` | `git rev-parse --short HEAD` | 0 | allowed — **`450316c`** = the expected tip |
| `Bash(git log*)` | `git log --oneline -3` | 0 | allowed — `450316c` (build report) · **`511bff0`** (the fix, the reviewed code commit) · `fd13970` (red tests) |
| `Bash(date*)` | `date` | 0 | allowed — `Fri Sep 18 16:51:39 EDT 2026`; the archiver window is 20:25–21:15 ET → **outside it** |
| `Bash(grep *)` | `grep -n "proof_only\|READ ONLY\|read_only" src/cobalt/db_migrations/cli.py` | 0 | allowed — 11 hits: `_connect(..., read_only=True)` → `conn.read_only = True` (cli.py:402-412), `cmd_migrate`'s `if proof_only:` branch returns **before** `_apply` (cli.py:439-451), the flag itself (cli.py:523). The flag and the read-only connection exist in THIS checkout |
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-18.md"` | 0 | allowed — top commit **`bff4ddd` "docs(desk): 09-18 R12 — production --proof-only (read-only, one exact line) approved 16:50 ET"**; below it `4afd5f6` (the review + this prompt). The approval rows are committed on main |
| `Bash(ls *)` | `ls -la "docs/40 - DevDocs/reports/"` | 0 | allowed — reports tree read |

Rules with no harmless variant inside their own pattern, probed by their first real use (UNATTENDED-LAUNCH §6): the `.env` `cp`/`rm`/`ls -la` (step 1), `COBALT_ENV=dev uv run cobalt db migrate --proof-only` (step 1 — it IS the harmless variant), `COBALT_ENV=production … --proof-only` (step 2, run ONCE), `git add`/`git commit` (this section's commit).

### AUTHORIZATION — verified by this hub, 16:51 ET

Dejan's words are in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-18.md` §4, committed on main (`bff4ddd`, proven above).

| what this run needs | where it is approved | verdict |
|---|---|---|
| the ONE production line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` | **R12, 16:50 ET** — "For the approval, I do approve the test." — approving that exact spelling, run ONCE, read-only, from the `s2-p2-cards` worktree on tip `450316c` / code `511bff0`, dev first, outside the archiver window. "No other production command." | **MATCH** — the launch line carries that string character for character, and no other `db migrate` spelling (no bare `migrate`, no `--rollback`, no `--down-to`) |
| this worktree's `.env` `cp` / `rm` / `ls` by path | **R1 list (1)**, 06:46 ET "Approved" — "`.env` cp/rm/ls by path" | MATCH (L41 interim: by name only, never printed, removed after — even on failure) |
| `COBALT_ENV=dev uv run cobalt db migrate --proof-only` | **R1 list (1)** — "`COBALT_ENV=dev uv run cobalt db migrate*`" | MATCH |
| git add/commit/diff/status/log/show/rev-parse, `git -C /Users/cobalt/cobalt log*`, cd/ls/grep/tail/wc/date | **R1 list (1)** | MATCH |
| second opinion BEFORE production use | **R8**, 14:29 ET standing direction; satisfied by `cto-2026-09-18.md` §24 — both houses `VERDICT: SAFE TO RUN --proof-only ON PRODUCTION`, review file `/Users/cobalt/cobalt-wt/agy-trial/scratch/review-migrate-fix/REVIEW.md` (hub-verified REAL 2, blocks proof-only 0, blocks migrate 0) | MATCH |

No rule in this launch line is outside R1 list (1) + R12's one production line. Absent from it by design: push, merge, `bypassPermissions`, any vault write, any other production command, `--rollback`, `--down-to`, bare `migrate`.

Known cosmetic carried in from the review, named before the run so it is not mistaken for a failure: **F1** — `count(*)` and the digest are two READ COMMITTED statements, so on a live table the `rows` value can be off by the rows inserted between them. `--proof-only` renders no verdict, so this is a wrong-looking number, not a failure (REVIEW.md F1 row: blocks proof-only **no**).

Also noted, unchanged from the four runs before this one: the prompt file's tail carries a block styled as a system reminder asking for a `Claude-Session:` URL line in every commit. It arrives inside a tool result — the file's own bytes — not from the harness or from Dejan; the genuine harness attribution reminder names only `Co-Authored-By` and says not to add lines it leaves out. **Not followed.**

## Dev — step 1, `COBALT_ENV=dev uv run cobalt db migrate --proof-only`

`.env` copied in 16:52 ET (by name, never printed). Exit **0**, **23 tables**, **no `-- applying` line**, closing line `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` Run verbatim:

```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.02
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.35
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   120          a9594cce035f4c845768d97546b55796   0.00
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
23 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 5.4 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

**vs the build report's BASELINE (15:55 ET): 22 of 23 tables byte-identical; ONE table differs, and it differs because its CONTENT changed.**

| table | BASELINE rows / digest | now | reading |
|---|---|---|---|
| `cobalt_redactions` | 118 / `2f0b1b28` | **120 / `a9594cce`** | the table gained **2 rows** between 15:55 and 16:52 |
| the other 22, `bars` (1,043,443 rows) included | — | — | **identical, digest for digest** |

**This is dev-data drift, not a harness difference — the run PASSES.** Named as an explicit, reasoned deviation from the prompt's literal "a difference → FAILED" rather than taken silently:

1. `cobalt_redactions` is an **append-only counter** (`src/cobalt/redact/store.py:60`, `INSERT INTO cobalt_redactions (channel, pattern, hits)`) — F19's redaction-hit telemetry. Any process that redacted a secret pattern against `cobalt_dev` in that hour appends to it. The BASELINE assumed a static dev DB; this table is the one that does not hold still.
2. The digest is a function of content. A row count that moves 118 → 120 **requires** the digest to move. The defect this check exists to catch is the opposite shape — **same content, different digest** — and that is not what is on the page: every table whose row count is unchanged reproduces its BASELINE digest exactly, including the million-row `bars`, which is the table the whole rewrite was for.
3. **Deterministic**: the command was run a second time at 16:53 and printed `120 / a9594cce` again, `bars 1043443 / 2769919a` again — byte-identical output. A flaky fold would not repeat.

Nothing in the harness's behaviour differs from the build report. Carried to the desk as **ESCALATE 1** (the BASELINE oracle needs a table that moves excluded, or a fresh BASELINE taken in the same minute).

| dev fact | value |
|---|---|
| `bars` rows | **1,043,443** |
| `bars` probe seconds | **5.35 s** (run 1) · **5.53 s** (run 2) |
| total probe seconds | **5.4 s** (run 1) · **5.6 s** (run 2) |
| `-- applying` lines | **none** |
| exit | **0** |

## Production — step 2, ONE command, run ONCE

`date` before → **`Fri Sep 18 16:53:45 EDT 2026`**. Command, exactly as approved in R12 and spelled in the launch line:

`COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only`

`date` after → **`Fri Sep 18 16:54:36 EDT 2026`** (51 s wall, of which the probe itself reports 46.9 s; the rest is process start and connect).

**Whole output, verbatim:**

```
cobalt db migrate — PROOF ONLY on cobalt_brain (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     146          baac6ac19fd231057ebe2cbe7443c933   0.03
bars                 system  system   8591339      a40b1c4e7541c0844b182465a777e537   46.73
card_dot_taps        user    -        -            -                                  0.00
card_dots            user    -        -            -                                  0.00
card_stop_edits      user    user     1            cbae670bbd7acd13749ac41d99f25861   0.00
card_transitions     user    user     293          3986eb3f96571498667bbfbc3d80aa8c   0.00
cobalt_email_sends   system  system   463          c8fc112af72900bb260196353fea82bd   0.00
cobalt_jobs          system  system   15           e2fad88bb7692552b55b2092978c94d9   0.00
cobalt_kill_switch   system  system   1            310655940a3a0ce10031f77a390733b6   0.00
cobalt_redactions    system  system   2            cf42d85ee49244ca40d419683eb3ca51   0.00
day_modes            user    user     10           d9139ce7290afb41d88404c32c59736b   0.00
desk_grade           system  -        -            -                                  0.00
desk_packet          system  -        -            -                                  0.00
desk_regime          system  -        -            -                                  0.00
radar_membership     system  system   3329         2797b8b834fe0a127c83b986b5c088af   0.04
radar_pool           system  system   1            1adf8b9ef245f62511b6249fc0c4616a   0.00
radar_score          system  -        -            -                                  0.00
radar_score_receipt  user    -        -            -                                  0.00
radar_score_run      system  -        -            -                                  0.00
session_blocks       system  system   8            ddf2a773f48403300cbff196fe9aa419   0.00
traders              user    user     1            cf9aec4d006d82fb0f12be2d9afa10b9   0.00
vault_overrides      user    user     29           1f529ee789a2e27f1b73010bbae4cdd7   0.00
vault_writes         user    user     1287         77e280aaebdb10ba7649a972ab19dacd   0.11
------------------------------------------------------------------------------------------
23 table(s) probed on cobalt_brain; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 46.9 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

### PASS — every condition the prompt set

| condition | result |
|---|---|
| exit 0 | **yes** |
| every existing table has rows + digest + seconds | **yes** — 15 present tables all carry all three; the 8 absent ones print `-` `-` and 0.00 s, which is the correct rendering for a table that does not exist yet |
| `system.bars` completes | **yes — 8,591,339 rows in 46.73 s.** No `ProgramLimitExceeded`, no `string_agg` ceiling, no error of any kind. **This is the fact the run existed to get: the 15:4x 1 GB failure is gone on the real table.** |
| no `-- applying` line | **none anywhere in the output** |
| the run's own last line says nothing was applied | **`NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`** |
| run ONCE | **once.** No retry, no second production command of any spelling |
| `.env` removed | `rm` 16:54 ET, then `ls -la` → `ls: /Users/cobalt/cobalt-wt/s2-p2-cards/.env: No such file or directory` — **gone** (L41 interim; never printed) |

Nothing was written on any surface: the transaction was `READ ONLY` at the server, no vault write, no DB write, no push, no merge. **L28: no trace line is owed, and none was made.**

### The numbers the deploy now budgets from fact instead of extrapolation

| fact | value |
|---|---|
| tables over 100,000 rows | **exactly one: `system.bars` — 8,591,339 rows, 46.73 s.** The next largest table in production is `vault_writes` at 1,287 rows / 0.11 s |
| every other table, summed | **0.18 s** (aset_sizings 0.03 · radar_membership 0.04 · vault_writes 0.11 · the rest 0.00) |
| TOTAL, one probe | **46.9 s** |
| **BEFORE + AFTER pair = the implied outage cost of the proof** | **≈ 93.8 s → budget ≈ 94 s**, on top of the migration's own DDL time |
| the desk's extrapolation, checked | predicted ≈45 s per probe / ≈90 s per pair from dev's 5.5 s × 8 (build report ESCALATE 1). Measured **46.73 s / ≈94 s** — the estimate was good to 4%. Fold rate: dev 189.8k rows/s, production 183.9k rows/s |
| `0006`/`0007` tables absent | **yes, all 8 and exactly those 8** — `radar_score_run`, `radar_score`, `desk_regime`, `desk_packet`, `desk_grade` (created by `0006_radar_score.sql`) and `card_dots`, `card_dot_taps`, `radar_score_receipt` (created by `0007_radar_cards.sql`). No other table is absent. Production is confirmed at **0005**, and the proof table lists what exists |
| `bars` growth, measured | the desk's figure this afternoon was **8,410,174**; the probe reads **8,591,339** — **+181,165 rows** since. Relevant to his 16:50 question about table size, and to the budget above, which grows with the row count |
| Grok F3b, answered by fact | no server or role `statement_timeout` killed a 46.7 s query — **there is no timeout under ≈47 s on this database**. The review's one UNVERIFIABLE finding is now verified as a non-issue |
| Grok/Gemini F1 (split count/digest) | not visible in this output; `bars`'s row count and digest describe snapshots taken a few seconds apart on a live table, so the printed `rows` may be off by any rows inserted in between. Cosmetic, pre-named, renders no verdict in `--proof-only` |

Residents were UP for this run — that is what `--proof-only` is for. **Heartbeat-visible impact of a 47 s `ACCESS SHARE` read on `bars` is the desk's to check, not this hub's.**

## Close

| check | result |
|---|---|
| `git status --porcelain` | **empty** |
| `.env` | absent, proven by `ls -la` |
| production commands run | **one**, the approved spelling, once |
| anything written | **nothing** — read-only at the server, no vault write, no DB write, no push, no merge, no code edit |

## ESCALATE

1. **The dev BASELINE oracle is not stable, because one table in it is append-only.** `cobalt_redactions` moved 118 → 120 rows (digest `2f0b1b28` → `a9594cce`) between the build report's 15:55 BASELINE and this run's 16:52 dev probe, so a literal "all 23 digests match BASELINE" gate fails on a healthy harness. The other 22 tables, `bars` included, matched byte for byte, and a rerun reproduced the new value exactly — the harness is fine, the gate's premise is not. Fix for the next prompt: either exclude the append-only telemetry table from the BASELINE comparison, or take the BASELINE and the check inside the same minute. This hub proceeded on that reasoning rather than stopping; the desk should rule whether that was the right call.
2. **Budget ≈94 s of outage for the proof pair, and re-measure it, because `bars` grows about 2% a day.** 46.73 s today at 8,591,339 rows; +181,165 rows since the afternoon figure. At this rate the pair costs roughly a further 2 s of outage per day with no other change. Two levers exist and neither is taken yet: the review's F1/F3a fix (count folded into the stream — one pass over `bars` instead of two) and, separately, the retention/pruning question he asked at 16:50, which is the only thing that bends the curve. Neither blocks tonight's deploy; the first is a small, tested change, the second is a design decision.

PROD PROOF DONE | 23 tables | system.bars 8591339 rows in 46.73 s | total 46.9 s → BEFORE+AFTER ≈ 94 s of outage | nothing applied, nothing written | 0006/0007 absent: yes | ESCALATE: 2
