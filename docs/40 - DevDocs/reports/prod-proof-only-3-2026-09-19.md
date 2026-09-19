# Production `--proof-only`, THIRD run — the FINAL migration harness meets production (2026-09-19)

Seat: proof hub `prod-proof-0919`, Opus 5 (`claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack`, gated code `ad9b07c`.
Prompt: `docs/40 - DevDocs/prompts/2026-09-19/03-prod-proof-only-3.md`. Authorization: `cto-2026-09-19.md` §4 **R7** (07:49 ET, "Approved"), on `cto-2026-09-18.md` §4 R1 list (1), R12, R16, R18–R21.

## §0 Headline

- **PROD PROOF DONE (07:52–07:53 ET). The FINAL code (`ad9b07c` — F1 + the REPEATABLE READ snapshot fix + the tribunal fold) met production once, read-only: 23 tables, `system.bars` 8,834,532 rows digested in 51.99 s, exit 0, no `ProgramLimitExceeded`, no `-- applying` line, nothing applied and nothing written.**
- **The outage budget is now measured on the final code: total 52.2 s per pass → BEFORE + AFTER ≈ 104 s** (09-18 read ≈92 s); `bars` is 99.6% of it; the command's wall clock was 60 s.
- Round 2's new refusal did NOT fire: all 23 probes completed, so production carries no duplicate table name across `public`/`user`/`system`. `0006`/`0007`'s eight tables are absent, as the deploy requires. Dev first: 23 tables, `bars` 1,043,443 in 5.24 s, digests identical to the round-2 baseline except append-only `cobalt_redactions`.
- PREFLIGHT clean (10 rules, 0 denials); review gate `REVIEW DONE … blocks the deploy: 0`; `.env` in by name and removed, `ls` proves it gone; worktree clean.
- ESCALATE: **3** — the ≈104 s grew 4.8× faster than the row count; the archiver is still not booted out; no `lock_timeout` anywhere in the harness.

## PREFLIGHT

Every allowlisted shape this run needs, in the order the steps use it. Rules with no harmless variant inside their own pattern (`cp`/`rm` of the `.env`, the two `db migrate` lines) are probed by their first real use, per `UNATTENDED-LAUNCH.md` §6.

| # | rule | command | exit | verdict |
|---|---|---|---|---|
| 1 | `Bash(git status*)` | `git status --porcelain` | 0 | allowed — **no output: worktree clean** |
| 2 | `Bash(git rev-parse *)` | `git rev-parse --abbrev-ref HEAD` | 0 | allowed — `sprint-2/stack` |
| 3 | `Bash(git log*)` | `git log --oneline -4` | 0 | allowed — tip `c44c760`, then `ad9b07c`, `fb7911b`, `9f03ec1` |
| 4 | `Bash(git diff *)` | `git diff --stat ad9b07c HEAD -- src tests configs ops` | 0 | allowed — **no output: the only commit above the gated code is report-only** |
| 5 | `Bash(git log*)` | `git log --oneline -1 ad9b07c` | 0 | allowed — the tribunal fold is on this branch |
| 6 | `Bash(date*)` | `date` | 0 | allowed — `Sat Sep 19 07:50:29 EDT 2026`, **outside 20:25–21:15 ET** |
| 7 | `Bash(grep *)` | `grep -n "proof_only\|READ ONLY\|read_only\|REPEATABLE READ\|repeatable" src/cobalt/db_migrations/cli.py` | 0 | allowed — 17 hits; see below |
| 8 | `Bash(ls -la /Users/cobalt/cobalt-wt/s2-p2-cards/.env)` | as written | 1 | allowed (the rule matched; exit 1 is the file being absent, which is the expected starting state) |
| 9 | `Bash(git -C /Users/cobalt/cobalt log*)` | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-19.md"` | 0 | allowed — `9917515 docs(desk): 09-19 R7 …` proves the approval row is committed on main |

**No denials. 0 rules failed.**

### The three gate conditions, verified by this hub

| gate | evidence | verdict |
|---|---|---|
| Tip is the gated code with report-only commits above it | `git diff --stat ad9b07c HEAD -- src tests configs ops` prints nothing | PASS |
| Snapshot fix present in THIS checkout | `cli.py:488` `conn.isolation_level = IsolationLevel.REPEATABLE_READ`; `cli.py:487` `conn.read_only = read_only`; `cli.py:543` `_connect(…, read_only=True)` on the `if proof_only:` branch (`cli.py:541`); `cli.py:404` prints `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` | PASS |
| L67 review gate (R18–R21) | `/Users/cobalt/cobalt-wt/agy-trial/scratch/review-harness-0919/REVIEW.md` last line: `REVIEW DONE · grok: 0/0/1 SAFE TO DEPLOY · gemini: 1/0/0 FIX FIRST Q5 · astra: 1/0/1 FIX FIRST 1 · houses that read it: 3 of 3 · hub-verified REAL: 3 (blocks the deploy: 0) · NOT REAL: 0 · UNVERIFIABLE: 1` | PASS — **blocks the deploy: 0** |

Authorization row, quoted from `cto-2026-09-19.md` §4 R7: *"(1) a THIRD run of the exact read-only production line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only` via `prompts/2026-09-19/03-prod-proof-only-3.md` … launch line = 09-18 R12/R16's with the session name `prod-proof-0919`; every other rule = 09-18 R1 list (1) for the `s2-p2-cards` worktree"*. Match: exact. (The row also pins the prompt file by sha256; `shasum` is not in this session's allowlist, so this hub verifies the row's text and the launch line, not the hash — noted, not routed around.)

Also carried into this run from round 2's ESCALATE 2: if production ever acquired one table name in two of `public`/`user`/`system`, `_schema_of` now raises at the FIRST probe. That outcome would be recorded verbatim as `FAILED: production proof-only — duplicate table name`, never retried.

## Dev

`.env` copied in by name (never printed). One command, exit 0:

```
$ COBALT_ENV=dev uv run cobalt db migrate --proof-only
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.01
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.24
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   123          2797ee9763ed61b30c7198dbd7a1d569   0.00
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
23 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 5.3 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

| check | result |
|---|---|
| table quoted, 23 tables | **yes** — 23 rows, each with rows + digest + seconds |
| NO `-- applying` line | **yes** — `_apply` is not reached on the `if proof_only:` branch (`cli.py:541-551`) |
| exit 0 | **yes** |
| dev `bars` | **1,043,443 rows in 5.24 s** (round-2 baseline read 5.42 s at the same row count and the same digest `2769919a`) |
| total | **5.3 s** |

**Drift, expected and by design:** `cobalt_redactions` 122 → 123 (`834d5919` → `2797ee97`) since the round-2 baseline. That table is append-only telemetry; the prompt pins no older BASELINE for exactly this reason. Every other row count and digest is byte-identical to `harness-round2-2026-09-19.md`'s post-round-trip list.

## Production

`date` before: `Sat Sep 19 07:52:08 EDT 2026` · `date` after: `Sat Sep 19 07:53:08 EDT 2026` — **wall clock 60 s**. ONE command, run once, foreground, Bash `timeout` 600000 ms. Whole output, verbatim:

```
$ COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only
cobalt db migrate — PROOF ONLY on cobalt_brain (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
aset_sizings         user    user     146          baac6ac19fd231057ebe2cbe7443c933   0.03
bars                 system  system   8834532      d21fc0b31265b2565c71432a6ebf6979   51.99
card_dot_taps        user    -        -            -                                  0.00
card_dots            user    -        -            -                                  0.00
card_stop_edits      user    user     1            cbae670bbd7acd13749ac41d99f25861   0.00
card_transitions     user    user     293          3986eb3f96571498667bbfbc3d80aa8c   0.01
cobalt_email_sends   system  system   463          c8fc112af72900bb260196353fea82bd   0.00
cobalt_jobs          system  system   15           635701c427c7e7e82581d4291749fd3b   0.00
cobalt_kill_switch   system  system   1            310655940a3a0ce10031f77a390733b6   0.00
cobalt_redactions    system  system   2            cf42d85ee49244ca40d419683eb3ca51   0.00
day_modes            user    user     10           d9139ce7290afb41d88404c32c59736b   0.00
desk_grade           system  -        -            -                                  0.00
desk_packet          system  -        -            -                                  0.00
desk_regime          system  -        -            -                                  0.00
radar_membership     system  system   3334         72b94dfe689084e8e96cd880d031e3f3   0.04
radar_pool           system  system   1            88537229826d4da833be389abd8367be   0.00
radar_score          system  -        -            -                                  0.00
radar_score_receipt  user    -        -            -                                  0.00
radar_score_run      system  -        -            -                                  0.00
session_blocks       system  system   8            ddf2a773f48403300cbff196fe9aa419   0.00
traders              user    user     1            cf9aec4d006d82fb0f12be2d9afa10b9   0.00
vault_overrides      user    user     29           1f529ee789a2e27f1b73010bbae4cdd7   0.00
vault_writes         user    user     1321         8fcd48b94922fee9bd47aa1b8fde8144   0.12
------------------------------------------------------------------------------------------
23 table(s) probed on cobalt_brain; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 52.2 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
```

### PASS conditions, one by one

| condition | result |
|---|---|
| exit 0 | **yes** |
| every table has rows + digest + seconds | **yes** for the 15 tables that EXIST; the 8 that do not exist print `-` / `-` with their seconds, which is the proof table saying what is absent (see 0006/0007 below) |
| `system.bars` ≈ 8.6M completes, no `ProgramLimitExceeded` | **yes — 8,834,532 rows digested in 51.99 s**, one streamed pass, no error |
| NO `-- applying` line | **yes** |
| the run's own last line says nothing was applied | **yes** — `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` |
| duplicate table name (round-2 ESCALATE 2) | **did not fire** — the harness completed all 23 probes, which `_schema_of` would have refused at the first one. Production carries no name in two of `public`/`user`/`system`; this is a second, independent confirmation of the desk's 06:57 ET read-only check |

`.env` removed immediately after the command; `ls -la /Users/cobalt/cobalt-wt/s2-p2-cards/.env` → `No such file or directory` (exit 1). L28: **nothing was written, so no trace line is owed** — the transaction was `READ ONLY` at the server and `--proof-only` never reaches `_apply`.

## Close

### Per-table seconds, every production table over 100,000 rows

There is exactly **one**. The next largest table in the database is `radar_membership` at 3,334 rows — three orders of magnitude below the threshold.

| table | rows | seconds | share of total |
|---|---|---|---|
| `system.bars` | 8,834,532 | **51.99** | **99.6%** |
| *(all 22 others combined)* | 6,624 | 0.21 | 0.4% |
| **TOTAL** | | **52.2** | |

**Implied outage cost of a BEFORE + AFTER pair: ≈ 104 s** (2 × 52.2). The command's own wall clock was 60 s, so ≈8 s of connect + UTF-8 check + interpreter boot sits outside the probe total and is paid once, not twice.

### Against the two earlier production proofs

| | 09-18 16:5x (`511bff0`) | 09-18 17:29 (`0e1f768`) | **09-19 07:52 (`ad9b07c`)** |
|---|---|---|---|
| isolation | READ COMMITTED | READ COMMITTED | **REPEATABLE READ** |
| `bars` rows | 8,591,339 | 8,592,116 | **8,834,532** (+242,416) |
| `bars` seconds | 46.73 | 45.75 | **51.99** |
| total | 46.9 s | 46.0 s | **52.2 s** |
| BEFORE+AFTER | ≈94 s | ≈92 s | **≈104 s** |
| `bars` digest | `a40b1c4e…` | `2ca2840d…` | `d21fc0b3…` |
| wall clock | — | 50 s | **60 s** |

The digest differs from yesterday's for the honest reason that 242,416 rows landed in between (the 09-18 20:53 archiver run, then the overnight replay). Nothing here is a comparison failure — `--proof-only` pins no cross-day baseline.

### `0006`/`0007`'s tables are absent — yes

The proof table lists what exists, and exactly the eight tables those two migrations create print `-`:

| migration | tables it creates | on production |
|---|---|---|
| `0006_radar_score.sql` | `system.radar_score_run`, `system.radar_score`, `system.desk_regime`, `system.desk_packet`, `system.desk_grade` | **all 5 absent** |
| `0007_radar_cards.sql` | `"user".card_dots`, `"user".card_dot_taps`, `"user".radar_score_receipt` | **all 3 absent** |

`"user".aset_sizings` exists with 146 rows but WITHOUT `0007`'s 25 card columns — the footer's `aset_sizings: 25 card column(s) added by 0007` is the digest exclusion list, which is why the same digest is comparable across the migration. This is the expected pre-deploy shape: the stacked deploy is what creates the eight.

Heartbeat-visible impact is the desk's to check, not this hub's.

## ESCALATE

1. **The outage budget is now ≈104 s, and it grew FASTER than the row count.** In the 14.4 hours since the 09-18 17:29 proof, `bars` gained 2.82% more rows (+242,416) but the probe took 13.6% longer (+6.24 s). At yesterday's linear rate today's table should have read 47.0 s; it read 52.0 s — **5 s over linear**. One pair of measurements does not prove superlinearity (Saturday-morning host load is a confound, and the radar is idle rather than scanning), but the deploy must budget from the MEASURED 104 s, not from 09-18's 92 s, and the bounded-proof fix for `bars` (closed periods proven once by a stored digest, only the open period re-read) is now worth more than the ≈11 s per million the 09-18 report estimated. This is exactly the question Sunday's partition/retention tribunal is being asked.
2. **`com.cobalt.archiver` is still not one of the residents the deploy boots out** (unchanged from `prod-proof-only-2-2026-09-18.md` ESCALATE 2, and NOT closed by the snapshot fix). REPEATABLE READ now protects the BEFORE/AFTER pair from a mid-migration commit, so the archiver can no longer make a good migration print `CHANGED`. What it can still do is raise `could not serialize access…` if it commits a change to a row the migration then modifies — the named price in `_connect`'s docstring. Today's registered set touches no row the archiver writes, so the exposure is zero for THIS deploy; the standing fix (disarm the archiver like the other two, or the bounded `bars` proof) is still owed, and until it lands each deploy prompt carries a clock rule instead.
3. **60 s of wall clock for 52.2 s of probe, and the 600000 ms Bash timeout is a property of the harness, not of the code.** The gap is interpreter boot + connect + `SHOW server_encoding`. Nothing in `cli.py` sets a `lock_timeout` or a statement timeout either (REVIEW.md U1), so a deploy whose `0003` ALTER meets a heartbeat write waits indefinitely rather than failing fast. Unproven risk, named: the expected behaviour is a short lock wait, and the deploy takes the residents down first.

PROD PROOF DONE | 23 tables | system.bars 8834532 rows in 51.99 s | total 52.2 s → BEFORE+AFTER ≈ 104 s of outage | nothing applied, nothing written | 0006/0007 absent: yes | ESCALATE: 3
