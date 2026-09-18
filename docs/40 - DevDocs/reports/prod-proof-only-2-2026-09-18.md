# Production `--proof-only`, SECOND run — the FINAL code against production data (read-only)

Hub `prod-proof-0918b` (Opus 5, `claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack` at `20add4f` (stack tip `d72ece4`). Prompt: `docs/40 - DevDocs/prompts/2026-09-18/20-prod-proof-only-2.md`. Authorization: `cto-2026-09-18.md` §4 **R16** (17:26 ET, "Approved.") for a SECOND run of the exact line `COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only`; R12 approved the first; R1 list (1) for every other rule; R8 second opinion done (§24, both houses `SAFE TO RUN --proof-only ON PRODUCTION`).

## §0 Headline

- RUNNING — filled at the close.

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

