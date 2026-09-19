# Production `--proof-only`, THIRD run — the FINAL migration harness meets production (2026-09-19)

Seat: proof hub `prod-proof-0919`, Opus 5 (`claude-opus-5`), worktree `/Users/cobalt/cobalt-wt/s2-p2-cards`, branch `sprint-2/stack`, gated code `ad9b07c`.
Prompt: `docs/40 - DevDocs/prompts/2026-09-19/03-prod-proof-only-3.md`. Authorization: `cto-2026-09-19.md` §4 **R7** (07:49 ET, "Approved"), on `cto-2026-09-18.md` §4 R1 list (1), R12, R16, R18–R21.

## §0 Headline

- RUN IN PROGRESS — this section is rewritten at the close.

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
