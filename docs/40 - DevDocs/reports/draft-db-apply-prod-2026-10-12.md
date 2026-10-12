# Draft — card 417 `cobalt db apply --prod` (classes K3, K5) — 2026-10-12

## §0 Headline
- Card written: `prompts/2026-10-12/417-db-apply-prod-card.md`, 10 rows (A1-A5 the verb in a new `src/cobalt/db_apply.py`; K1-K4 the launcher, `authorize.sh`, the hub text and `.gitignore`; R1 restarts). BASE is the only placeholder.
- No launch line changes. The seat's one filled `<prod write>` string already carries a `db apply` command (`desk-launch.sh:1804`), and G2 passes it byte for byte (`bare-guard.py:1099-1105`).
- The file's bytes are bound three times: launch (K1), authorize (K2) and the verb's own sha256 check (A2). DDL is detected on the first word after comments, with each statement cut at a `;` outside quotes (A1).
- Expected `RESTARTS: com.cobalt.aset com.cobalt.radar`, because of the new tunable and the CLI import reach. `INSTALL: none`.
- 7 decisions. The one that departs from the prompt is #1: the card has no `DB:` key, because `DB: none` would fail the build at W.

## DECISIONS
1. ASK DESK: the prompt says `DB none`. But rows A1-A5 touch `src/` and `configs/`, and `BUILD-HUB.md:80` fails a `DB: none` build whose diff holds any path outside `ops/`, `tests/ops/` and `docs/`. Default taken: the key is left out. The with-DB tests (A4 T5, T6) run on `cobalt_dev` under the lock, never on production. [14:39 EDT]
2. ASK DESK: the brain's spelling is `cobalt db apply --prod <file.sql>`. The verb adds a required `--side {user,system}`, because `db.connect` refuses a connection with no side (`db.py:253-258`, ADR-0008). It also adds `--sha256` and `--ddl`. Default: all three are required, with no default value (L1). [14:39 EDT]
3. ASK DESK: "quoted byte for byte in the card row". A prodwrite row is 7 cells split on `|` (`desk-launch.sh:1702-1713`), so multi-line SQL cannot sit in a cell. Default: the row's command carries the file's `--sha256`. The card quotes the file whole in one fenced block under `## SQL`. The file is `prompts/<date>/<nn>-<name>-apply.sql`, committed beside the card. Its path has no space, because the seat's command has no quotes (`:1733`). [14:39 EDT]
4. ASK DESK: `DDL: yes` opens a second path for schema changes beside `db migrate` (L3). It also lifts the hub's NEVER line "a production schema change" (`PRODWRITE-HUB.md:16`). Default: built as brain D1 says. A `DDL: yes|no` header line must match the command's `--ddl` (K1, K2). DDL runs only as the side role through `db.connect`, never through the superuser `connect_migration`. The NEVER line is narrowed only for those statements (K3). [14:39 EDT]
5. ASK DESK: how fresh the backup must be. Default: a new tunable `db.apply.backup_max_age_s` = 900 in `tunables.yaml`, the same shape as `db.query.timeout_s`. The cost is an aset restart at deploy, since `tunables.yaml` is in the aset's `reads:` (`jobs.yaml:69`). The 26 h `heartbeat.backup_max_age_min` (`tunables.yaml:611-612`) is too loose for a write. [14:39 EDT]
6. ASK DESK: `.gitignore:83` ignores every `*.sql`, so the approved file cannot be committed today. Default: one narrow carve-out, `!docs/40 - DevDocs/prompts/20*/*-apply.sql` (K4). A test proves every other `.sql` path stays ignored. [14:39 EDT]
7. ASK DESK: `CHECK REPORT` is filled at the build launch, as the prompt gives it. `CARD.md:20` says it is empty for a build. Card 392 carried it too. Default: kept. [14:39 EDT]

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `d3d948f9` (14:00 EDT). Every `file:line` below is read on the main working tree at that HEAD. `.claude/settings.json` is dirty in the tree, so it was read with `git show HEAD:` instead: line 9 is `"Bash(COBALT_ENV=production uv run cobalt db query *)"`.
- `prompts/CARD.md` read whole: the prodwrite section is `:141-147`, and the build header rules are `:11-29`.
- `reports/prodwrite-card-decisions-2026-10-12.md` read whole: D1 is `:13`.
- `cto-2026-10-12.md` rows: R1138 at `:103`, R1205 at `:38`, R1209 at `:34`, R1231 at `:12`, R1233 at `:10` (`c928d4e3` deployed).
- `prompts/PRODWRITE-HUB.md` read whole. The launch line is `:10`. The NEVER line is `:16`. Step (0) is `:25-26`, (1) is `:28-30`, and (2) is `:32-34`.
- LAWS read: L1 `:107`, L4 `:116`, L41 `:249`, L51 `:285`, L62 `:320`, L81 `:403`. The `areas/cobalt.md` sections read were `## What Cobalt is` and `## Build rules` down.
- Existing `db` verbs are wired in `src/cobalt/db_migrations/cli.py:1069-1132`: `migrate`, `dev-rebuild`, and `query` (`add_query_parser`, `:1130-1132`). `src/cobalt/db_query.py:41-95` is `tokenize`, `:98-126` is `guard_select`, and `:163` is `BEGIN READ ONLY`. No production write verb exists.
- The one factory is `src/cobalt/db.py:160-199` `_open`, "THE ONLY `psycopg.connect`", with the DSN composed at `:193-198`. Then `connect` at `:227-266` and `connect_migration` at `:269-300` (superuser, migrations only).
- Backup: `backup/cli.py:58-72` `_status`, with the `database     :` line at `:62`. `backup/restic.py:64-69` is the snapshot line, and `:240-263` is `latest_snapshot_age`. In `DEPLOY-HUB.md`, `:120` and `:131` are the deploy hub's backup reads.
- Launcher prodwrite arm: `ops/desk/desk-launch.sh:1669-1805`. The verb refusals are `:1738-1749`, the character refusal `:1732-1734`, and the fill `:1804` and `:1910`. `authorize.sh` was read whole; its prodwrite rows are `:243-254`. `bare-guard.py:1099-1105` is G2 for the seat.
- `/Users/cobalt/.claude/ops/desk-launch.sh` is a link to the repo's `ops/desk/desk-launch.sh` (`ls -l`, 14:30 EDT).
- RESTARTS evidence: `jobs.yaml:69`, `:75`, `:200` and `:203`; `restarts.py:133` (ast.walk), `:207-220`, `:225-246`, and `:28` (`.gitignore` is META); `cli.py:65`. The precedent is `deploy-2026-10-02-2.md:42`, where `RESTARTS: com.cobalt.radar` came from a src change.
- `.gitignore:21-22` and `:83-92` were read: `*.sql` is ignored after the docs carve-out.
- Test files read for shape: `tests/cobalt/test_db_query.py:33-35`, `tests/cobalt/test_dev_rebuild_db.py:29-50`, `tests/cobalt/test_backup.py:197`. Function names were grepped from `tests/ops/test_prodwrite_hub.py` (`:55`, `:90`, `:133`, `:160`), `tests/ops/test_authorize.py` (`:325`, `:343`, `:386`) and `tests/ops/test_desk_launch_prodwrite.py` (`:134`, `:160`, `:225`).
- Ran nothing but reads: no database, no production command, no git write, no launch.

DRAFTED · decisions: 7
