# Production `--proof-only`, SECOND run — the FINAL code against production data (read-only)

Hub `prod-proof-0918b` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack` at `20add4f` (stack tip `d72ece4`). Prompt: `docs/40 - DevDocs/prompts/2026-09-18/20-prod-proof-only-2.md`. Authorization: `cto-2026-09-18.md` §4 **R16** (17:26 ET, "Approved.") for a SECOND run of the exact line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only`; R12 approved the first; R1 list (1) for every other rule; R8 second opinion done (§24, both houses `SAFE TO RUN --proof-only ON PRODUCTION`).

## §0 Headline

- **PROD PROOF DONE (17:29 ET). The FINAL code (F1 folded, `0e1f768`) met production once, read-only: `system.bars` 8,592,116 rows digested in 45.75 s, exit 0, no `ProgramLimitExceeded`, no `-- applying` line, nothing applied and nothing written.**
- **The outage estimate is now measured: total 46.0 s per pass → BEFORE + AFTER ≈ 92 s** (was ≈94 s extrapolated); `bars` is 99.5% of it; the command's wall clock was 50 s.
- 23 tables probed on `cobalt_brain`; `0006`/`0007`'s eight tables absent, as a forward migration expects. Dev first: 23 tables, exit 0, no `-- applying`.
- One production command, run once. `.env` copied by name, removed, proven gone. Worktree clean, report committed after every section.
- ESCALATE: **3** — the ≈92 s grows linearly with `bars`; the archiver is not booted out with the other residents; the 600000 ms Bash timeout is now a property of the harness.

## PREFLIGHT

Run 17:27 ET from `/Users/cobalt/cobalt-wt/s2-p2-cards`. **Zero denials.**

| rule | command | exit | allowed / DENIED |
|---|---|---|---|
| `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-18.md"` | 0 | allowed — top row `392a53f docs(desk): 09-18 R16 — proof rerun + second-attempt stacked deploy approved 17:26 ET …`: **R16 is committed on main** |
| `Bash(grep *)` | `grep -n "R16\|R12\|R8\|R1 " "…/reports/cto-2026-09-18.md"` | 0 | allowed — R16 names *"a SECOND run of the exact read-only production line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` (R12 approved the first), on the final code, per `prompts/2026-09-18/20-prod-proof-only-2.md`"* → **matches this prompt file and this launch line exactly.** No mismatch |
| `Bash(grep *)` | `grep -n "SAFE TO RUN" …/REVIEW.md` | 0 | allowed — Grok and Gemini both `VERDICT: SAFE TO RUN --proof-only ON PRODUCTION`; hub-verified REAL 2, blocks proof-only **0** |
| `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **empty**, worktree clean |
| `Bash(git rev-parse *)` | `git rev-parse --abbrev-ref HEAD` | 0 | allowed — **`sprint-2/stack`** |
| `Bash(git rev-parse *)` | `git rev-parse --short HEAD` | 0 | allowed — **`20add4f`** = the expected tip |
| `Bash(git log*)` | `git log --oneline -4` | 0 | allowed — `20add4f` · `2f69714` (STACK READY) · `237ef25` (PART B) · `d72ece4` (PART A, the stack tip) — the two report-only commits sit above `d72ece4` as the prompt states |
| `Bash(git log*)` | `git log --oneline --grep="review F1" -1` | 0 | allowed — **`0e1f768 fix(db-migrate): count rows inside the streamed fold — one statement, one pass (review F1)`** is on this branch |
| `Bash(date*)` | `date` | 0 | allowed — **`Fri Sep 18 17:27:52 EDT 2026`** — outside the archiver window 20:25–21:15 ET |
| `Bash(grep *)` | `grep -n "proof_only\|READ ONLY\|read_only" src/cobalt/db_migrations/cli.py` | 0 | allowed — the flag and the read-only connection exist in THIS checkout: `cmd_migrate` `if proof_only:` (line 450) → `_connect(…, read_only=True)` (452) → `conn.read_only = True` (423); `--proof-only` refuses `--rollback`/`--down-to` (434); output line 377 `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` |

Read for the index card: `UNATTENDED-LAUNCH.md` §2+§6 · Memory `INDEX.md` → `areas/cobalt.md` `## NOW` → `LAWS.md` in full · `migrate-harness-fix-2026-09-18.md` (§0, BASELINE, §3.1, ESCALATE 1–3) · `src/cobalt/db_migrations/cli.py` (`cmd_migrate`, `_connect`, `_probe`, `_stream_row_texts`, `_digest_rows`) · `…/agy-trial/scratch/review-migrate-fix/REVIEW.md`.

**F1 is no longer a caveat on this code.** The prompt's index card warns that the two-statement probe can print a `rows` value off by concurrent inserts. `_probe` at this tip takes both numbers from ONE statement — `rows, digest = _digest_rows(_stream_row_texts(conn, table, stream))`, the count being the rows the cursor yields (`0e1f768`). On a live `bars` the printed count and digest are therefore the same snapshot, and the 8.4M-row table is read once per probe, not twice.

**L28:** nothing is written by this run — no vault write, no DB write, no trace line is owed.

## Dev — the flag does what it says in this checkout

`.env` copied in by name (L41 interim, never printed). `COBALT_ENV=dev uv run cobalt db migrate --proof-only`, 17:29 ET, **exit 0**, verbatim:

```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.01
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.42
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   121          177a0fde30d8c28fa57360b49382abb1   0.00
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
23 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 5.5 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

| check | result |
|---|---|
| tables | **23**, each with rows + digest + seconds |
| `-- applying` line | **none** — nothing was applied |
| exit | **0** |
| dev `bars` | **1,043,443 rows in 5.42 s** (the 09-18 build run read 5.55 s at the same row count — the one-pass fold is no slower) |
| drift, expected | `cobalt_redactions` 118 → 121 rows, digest `2f0b1b28…` → `177a0fde…`: the append-only table drifts by design; no BASELINE comparison is made here (the gate run compared BEFORE with AFTER inside one command) |


## Production — ONE command, once

`date` **`Fri Sep 18 17:28:55 EDT 2026`** → `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` (foreground, Bash `timeout` 600000) → `date` **`Fri Sep 18 17:29:45 EDT 2026`**. **Exit 0. 50 s of wall clock for the whole command.** Whole output, verbatim:

```
cobalt db migrate — PROOF ONLY on cobalt_brain (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     146          baac6ac19fd231057ebe2cbe7443c933   0.03
bars                 system  system   8592116      2ca2840db52f5e0930dd0d31bbbf2b5c   45.75
card_dot_taps        user    -        -            -                                  0.00
card_dots            user    -        -            -                                  0.00
card_stop_edits      user    user     1            cbae670bbd7acd13749ac41d99f25861   0.00
card_transitions     user    user     293          3986eb3f96571498667bbfbc3d80aa8c   0.00
cobalt_email_sends   system  system   463          c8fc112af72900bb260196353fea82bd   0.00
cobalt_jobs          system  system   15           19dc75ee74118d6f1b67d1a0189bedbf   0.00
cobalt_kill_switch   system  system   1            310655940a3a0ce10031f77a390733b6   0.00
cobalt_redactions    system  system   2            cf42d85ee49244ca40d419683eb3ca51   0.00
day_modes            user    user     10           d9139ce7290afb41d88404c32c59736b   0.00
desk_grade           system  -        -            -                                  0.00
desk_packet          system  -        -            -                                  0.00
desk_regime          system  -        -            -                                  0.00
radar_membership     system  system   3330         0d429fe0a347084c02cc224d7daa111d   0.04
radar_pool           system  system   1            960845c0f24ed5c9a91b1d3110108fc9   0.00
radar_score          system  -        -            -                                  0.00
radar_score_receipt  user    -        -            -                                  0.00
radar_score_run      system  -        -            -                                  0.00
session_blocks       system  system   8            ddf2a773f48403300cbff196fe9aa419   0.00
traders              user    user     1            cf9aec4d006d82fb0f12be2d9afa10b9   0.00
vault_overrides      user    user     29           1f529ee789a2e27f1b73010bbae4cdd7   0.00
vault_writes         user    user     1290         000f5ba334d907741af1192dba31e78a   0.12
------------------------------------------------------------------------------------------
23 table(s) probed on cobalt_brain; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 46.0 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

**PASS, every condition:**

| condition | result |
|---|---|
| exit 0 | **yes** |
| every table has rows + digest + seconds | **yes** — 15 present tables carry all three; the 8 absent ones print `-` `-` with their seconds, which is what ABSENT looks like |
| `system.bars` ≈ 8.4M completes | **yes — 8,592,116 rows digested in 45.75 s, no `ProgramLimitExceeded`.** The 1 GB failure of 15:4x is gone on the real table, on the FINAL code |
| no `-- applying` line | **none anywhere in the output** |
| the run's own last line | `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` |
| `.env` | `rm` run, then `ls -la` → `ls: /Users/cobalt/cobalt-wt/s2-p2-cards/.env: No such file or directory` (L41 interim; never printed) |

**Against the FIRST production proof (16:54 ET, code `511bff0`, `prod-proof-only-2026-09-18.md`):**

| | first run (16:54) | this run (17:29) |
|---|---|---|
| `bars` rows | 8,591,339 | **8,592,116** (+777 — the RTH poller, 36 minutes) |
| `bars` seconds | 46.73 | **45.75** |
| total | 46.9 s | **46.0 s** |
| `bars` digest | `a40b1c4e7541c0844b182465a777e537` | `2ca2840db52f5e0930dd0d31bbbf2b5c` |

The digest moved because the table moved: 777 new rows between the runs. That is the expected reading of a live table, not a defect — `--proof-only` renders no verdict, and F1's folded one-statement probe means the printed count and the digest are the SAME snapshot (8,592,116 rows is the count the cursor yielded, not a separate `count(*)`). The one-pass fold is also not slower than the two-pass version it replaced: 45.75 s against 46.73 s at 0.009% more rows.


## Close

**Per-table seconds, every production table over 100,000 rows.** There is exactly one: `bars`. The next largest table in the database is `radar_membership` at 3,330 rows — three orders of magnitude below the threshold.

| table | rows | seconds | share of the proof |
|---|---|---|---|
| `bars` | 8,592,116 | **45.75** | 99.5% |
| `vault_writes` | 1,290 | 0.12 | 0.3% |
| `radar_membership` | 3,330 | 0.04 | 0.1% |
| `aset_sizings` | 146 | 0.03 | 0.1% |
| the other 19 | ≤ 463 | 0.00 each | ~0% |
| **TOTAL (the command's own line)** | | **46.0 s** | |

**Implied outage cost of a BEFORE + AFTER pair: ≈ 92 s** (2 × 46.0 s), measured, not extrapolated — this replaces the ≈94 s estimate the deploy plan has been carrying. It is the probe cost ALONE: the migration's own DDL (0006 + 0007) and the residents' stop/start sit on top of it. The command's wall clock was 50 s, so a deploy step that runs the migration should budget ≈100–110 s of client time for the two probes plus connect overhead.

**`0006`/`0007`'s tables are absent from production — yes, all eight.** The proof table lists what exists, and every table the two pending migrations create prints `-` for schema, rows and digest:

| migration | tables | production |
|---|---|---|
| `0006_radar_score.sql` | `radar_score_run`, `radar_score`, `desk_regime`, `desk_packet`, `desk_grade` | **all 5 absent** |
| `0007_radar_cards.sql` | `card_dots`, `card_dot_taps`, `radar_score_receipt` | **all 3 absent** |

(`card_stop_edits` and `card_transitions` DO exist in production — they are not 0006/0007 tables; they arrived with the settings/migrations tier and are unaffected.) This is the state a forward migration expects: nothing from the reverted 09-17 merge survived, as `cobalt.md` `## NOW` records.

Heartbeat-visible impact during the probe is the desk's to check, not this hub's.

| check | result |
|---|---|
| `git status --porcelain` | empty (verified at the close) |
| production writes | **none possible** — the transaction was `READ ONLY` at the server; the run applied nothing and wrote nothing |
| vault writes | none — L28 owes no trace line for a run that writes nothing |
| commands run against production | **one**, the approved line, once |

## ESCALATE

1. **The outage budget is now a measured fact: ≈92 s of probe inside the deploy, and it grows linearly with `bars`.** `bars` is 99.5% of the proof cost. It gained 777 rows in the 36 minutes between the two proofs (RTH poller) and ~182k rows since the 15:5x count of 8,410,174 (the nightly archiver). At today's ≈5.3 s per million rows, every additional million rows adds ≈11 s to the deploy outage. The streamed fold removed the 1 GB cliff, not the linear cost — the fix is the BOUNDED proof for `bars` (closed periods proven once by a stored digest, only the open period re-read), which is exactly what R15's partition/retention tribunal is being asked to design. Until then every production migration carries ≈92 s and rising.
2. **A live `bars` makes the BEFORE/AFTER pair snapshot-sensitive, and `com.cobalt.archiver` is not one of the residents the deploy boots out.** This run and the 16:54 run printed different `bars` digests for the honest reason that 777 rows landed between them. In a deploy the AFTER probe must see what the BEFORE probe saw except for the DDL: `com.cobalt.aset` and `com.cobalt.radar` are stopped by the deploy, but the archiver (20:30 ET bulk insert into `bars`) and the 21:05 replay are NOT, so a migration overlapping them would read a changed `bars`, print `CHANGED` and roll back — a false failure, fail-safe but expensive. Tonight's prompt `19-deploy-stack-2.md` step 1.1 already avoids this by the clock (start ≤19:00 ET or ≥21:40 ET, re-checked before 3.2/3.6/3.7). The standing fix is to make the exclusion explicit — the archiver disarmed like the other two, or `bars` proven by the bounded method of item 1 — rather than relying on a clock rule in each prompt.
3. **Keep the Bash `timeout` at 600000 on every production migrate call.** The read-only proof alone spent 50 s of client wall time; a real migration pays two probes plus the DDL, i.e. ≈100–110 s+, against a 120 s default that would kill the client mid-transaction (the failure mode the desk named for `19-deploy-stack-2.md` step 3.5). This is a property of the harness now, not of one prompt: any future caller of `db migrate` against production needs the same.

PROD PROOF DONE | 23 tables | system.bars 8592116 rows in 45.75 s | total 46.0 s → BEFORE+AFTER ≈ 92 s of outage | nothing applied, nothing written | 0006/0007 absent: yes | ESCALATE: 3
