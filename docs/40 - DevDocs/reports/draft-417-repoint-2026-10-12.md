# Draft — card 417 re-pointed to the brain's directions — 2026-10-12

## §0 Headline
- `prompts/2026-10-12/417-db-apply-prod-card.md` edited in place: ask 4 (no DDL through `apply`, no `--ddl`, NEVER line unchanged) and ask 5 (constant `BACKUP_MAX_AGE_S = 900`, no tunable).
- Rows changed: A1, A3, A5, K1, K2, K3, R1, plus NOT IN THIS JOB, READ, CHECK ASK X1, RECORDS. A2, A4, K4 untouched. BASE is the only placeholder.
- RESTARTS now `com.cobalt.radar` only: the aset reads `tunables.yaml` but the card no longer changes it, and the aset's imports do not reach the changed `src/` modules.
- 3 decisions.

## DECISIONS
1. A `ddl` statement and an `other` statement are refused with two texts, both naming the statement number and first word. The brain's "any statement that does not parse as DML" is the `other` kind (test case `FROBNICATE t`). Kept: the existing named DDL words `REINDEX`, `CLUSTER`, `REFRESH`, `SECURITY` stay `ddl` for the message only; both kinds are refused.
2. Row K1 loses its `DDL:` check; its checks are renumbered (a)–(d), and K2's rows are four (`SQL FILE committed`, `SQL FILE unchanged`, `SQL SHA256`, `SQL CARD BLOCK`). Added test S3 is green on `BASE` (the NEVER line is unchanged); S1, S2, S4 stay red on `BASE`.
3. RESTARTS: no aset restart, proved by reading (see `## RECORDS`). `latest_snapshot_age` returns a timedelta (`backup/cli.py:70-71`), so the verb compares `age.total_seconds()` with the constant. [14:43 EDT]

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `bcaa97e6`; `git diff --stat d3d948f9 HEAD -- src ops configs tests .gitignore` printed nothing (14:43 EDT): the card's `file:line` refs read at `d3d948f9` hold at `bcaa97e6`.
- Read whole: the card, `reports/db-apply-prod-decisions-2026-10-12.md`, `reports/draft-db-apply-prod-2026-10-12.md`, `topics/writing-rules.md`.
- Re-read at HEAD: `src/cobalt/db_query.py:20-126`; `ops/desk/desk-launch.sh:1728-1751`, `:1800-1805`, `:1908-1911`; `ops/desk/authorize.sh:75-87`, `:240-255`; `prompts/PRODWRITE-HUB.md:1-45` (NEVER `:16`, step 0 `:26`, step 1 `:29`, step 4 `:42-43`); `prompts/CARD.md:138-148`; `src/cobalt/backup/cli.py:56-73`; `configs/cobalt/jobs.yaml:55-100`, `:190-210`; `src/cobalt/jobs/restarts.py:120-264`.
- Greps of `src/`: `cobalt.db_migrations.cli` is imported only at `src/cobalt/cli.py:65`; `cobalt.cli` is imported by no module (docstrings only: `session/cli.py:166`, `cards/cli.py:280`, `archiver/store.py:46`); `tunables.yaml` holds no `db_apply` or `backup_max_age_s` row (`:611` is `heartbeat.backup_max_age_min`).
- Ran nothing but reads and edits of the card and this report: no database, no production command, no git write, no launch.

DRAFTED · decisions: 3
