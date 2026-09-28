# devdb-rollback-0017 — 2026-09-23

## §0
`0017_voice_turns` reversed on `cobalt_dev` from `/Users/cobalt/cobalt-wt/voice-v1` @ `28b6b0c6 (clean)`, 15:08:14–15:08:46 EDT. Only `0017_voice_turns.rollback.sql` was applied, and `voice_turns` was DROPPED. The other 28 tables have the same row count and digest before and after. The `.env` was removed and proven gone. ESCALATE: 0.

## Step 1 — AUTHORIZATION
`grep -n "^| R72 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-23.md"`
```
75:| R72 | 15:0x ET | His word: "approved" — to the desk's A (15:0x): ONE NEW command, `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0011`, run from `/Users/cobalt/cobalt-wt/voice-v1` (which holds the `0017` rollback file), dev DB only → APPROVED for `prompts/2026-09-23/58-devdb-rollback-0017.md` (Opus 5.5, `acceptEdits`, its exact allowlist; the voice `.env` pair of R60). DESK LAUNCH ROW, same row. Lane: no `.env` under `~/cobalt-wt/*` (desk `ls` 15:07). After its stop line: the deploy re-run (`41` → a relaunch with the dev DB to itself; no other with-DB build launched until the deploy stops). | APPROVED — launched |
```
`git -C /Users/cobalt/cobalt log -1 --format=%H -S"--rollback --down-to 0011" -- "docs/40 - DevDocs/reports/cto-2026-09-23.md"`
```
7eddc0628342d51e7dbd695824942125754b80fa
```
The row carries `--rollback --down-to 0011` and "approved", and the commit lookup is non-empty. PASS.

## Step 2 — LANE
`ls -la /Users/cobalt/cobalt-wt/*/.env`
```
(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env
```
`ls src/cobalt/db_migrations/0017_voice_turns.rollback.sql`
```
src/cobalt/db_migrations/0017_voice_turns.rollback.sql
```
No `.env` was found in any worktree, and the rollback file exists. PASS.

## Step 3 — date · .env copy
`date` → `Wed Sep 23 15:08:14 EDT 2026`
`cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/voice-v1/.env` → no output (copied by name only; never read or printed).

## Step 4 — BEFORE (`COBALT_ENV=dev uv run cobalt db migrate --proof-only`)
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)
...
voice_turns          user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
------------------------------------------------------------------------------------------
29 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007. Proof cost: total 5.6 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 28b6b0c6 (clean) · /Users/cobalt/cobalt-wt/voice-v1
```
`voice_turns` is present with 0 rows. 29 tables were probed. The full per-table rows are in the step-6 comparison table below.

## Step 5 — ROLLBACK (`COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0011`)
```
cobalt db migrate — ROLLBACK on cobalt_dev
-- applying 0017_voice_turns.rollback.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  system -> system           0 -> 0          0.01 -> 0.00    d41d8cd9 -> d41d8cd9  OK
archive_progress     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
aset_sizings         user    user -> user               1 -> 1          0.00 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.33 -> 5.28    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           141 -> 141      0.00 -> 0.00    2a14f84b -> 2a14f84b  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
missed               user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
movers_daily         system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
picks                user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               184 -> 184      0.01 -> 0.01    4a965c69 -> 4a965c69  OK
voice_turns          user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
----------------------------------------------------------------------------------------------------------------------
29 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.4 s + AFTER 5.3 s = total 10.7 s; slowest table bars (5.3 s before).
code: 28b6b0c6 (clean) · /Users/cobalt/cobalt-wt/voice-v1
```
Only one rollback was applied: `0017_voice_turns.rollback.sql`. No error. PASS.

## Step 6 — AFTER (`COBALT_ENV=dev uv run cobalt db migrate --proof-only`) — row-by-row vs step 4
AFTER output tail:
```
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
29 table(s) probed on cobalt_dev; ... Proof cost: total 5.5 s ...
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 28b6b0c6 (clean) · /Users/cobalt/cobalt-wt/voice-v1
```
The `voice_turns` row shows `-` for schema, rows, and digest, so the table is absent. The name still appears because this worktree's code, which includes 0017, lists it in the probe.

| table | rows before | rows after | digest before | digest after | equal |
|---|---|---|---|---|---|
| archive_incidents | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| archive_progress | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| aset_sizings | 1 | 1 | 0824685c130da3c7cb7f0e76191a6819 | 0824685c130da3c7cb7f0e76191a6819 | ✓ |
| bars | 1043443 | 1043443 | 2769919a57144c7bf8720110061dbf72 | 2769919a57144c7bf8720110061dbf72 | ✓ |
| card_dot_taps | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| card_dots | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| card_stop_edits | 1 | 1 | 7599f9ab6018697c2299e20bbacace54 | 7599f9ab6018697c2299e20bbacace54 | ✓ |
| card_transitions | 4 | 4 | f181e76b208a51b503339267865c157c | f181e76b208a51b503339267865c157c | ✓ |
| cobalt_email_sends | 2 | 2 | fba8cf9fc07cd6c95b503af272e26639 | fba8cf9fc07cd6c95b503af272e26639 | ✓ |
| cobalt_jobs | 13 | 13 | 8d9b0861615861e343009f33118a4931 | 8d9b0861615861e343009f33118a4931 | ✓ |
| cobalt_kill_switch | 1 | 1 | 2e590e87d4c9576e61d1ee0d5c90bbab | 2e590e87d4c9576e61d1ee0d5c90bbab | ✓ |
| cobalt_redactions | 141 | 141 | 2a14f84bb8f19cd7e7cb1d1a812190fd | 2a14f84bb8f19cd7e7cb1d1a812190fd | ✓ |
| day_modes | 2 | 2 | f2ffb4d41ed0a3bbc3dc2a1c7e6112b9 | f2ffb4d41ed0a3bbc3dc2a1c7e6112b9 | ✓ |
| desk_grade | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| desk_packet | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| desk_regime | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| missed | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| movers_daily | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| picks | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| radar_membership | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| radar_pool | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| radar_score | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| radar_score_receipt | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| radar_score_run | 0 | 0 | d41d8cd98f00b204e9800998ecf8427e | d41d8cd98f00b204e9800998ecf8427e | ✓ |
| session_blocks | 6 | 6 | b650702dd6fd624548e05ca940662f08 | b650702dd6fd624548e05ca940662f08 | ✓ |
| traders | 1 | 1 | a64e01480038484676fad3b14eb2489f | a64e01480038484676fad3b14eb2489f | ✓ |
| vault_overrides | 6 | 6 | 6a8b05207f55b8e25c253ce990c7a65a | 6a8b05207f55b8e25c253ce990c7a65a | ✓ |
| vault_writes | 184 | 184 | 4a965c69340f112d12e6ca21a8a0602c | 4a965c69340f112d12e6ca21a8a0602c | ✓ |
| voice_turns | 0 | — (absent) | d41d8cd98f00b204e9800998ecf8427e | — | DROPPED |

28 of 28 other tables are equal. PASS.

## Step 7 — .env removed, proven gone
`rm /Users/cobalt/cobalt-wt/voice-v1/.env` → no output
`date` → `Wed Sep 23 15:08:46 EDT 2026`
`ls -la /Users/cobalt/cobalt-wt/voice-v1/.env`
```
ls: /Users/cobalt/cobalt-wt/voice-v1/.env: No such file or directory
```

DEVDB 0017 ROLLED BACK · voice_turns: gone · other tables: 28 unchanged · .env: removed, proven gone
