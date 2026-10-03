JOB: devfix-verbs
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/devfix-verbs-1003
WORKTREE: devfix-verbs-1003
BASE: «FILL: the 8-hex head of main after cards 11, 12 and 13 are DEPLOYED (dev-rebuild, the devfix kind, the slot guard)»
TIP:
REPORT: /Users/cobalt/cobalt-wt/devfix-verbs-1003/docs/40 - DevDocs/reports/devfix-verbs-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R157, 2026-10-02 R39

## ROWS

WHY: row L6 of card `03` adoption-scripts, moved out because its base facts (`cobalt db dev-rebuild`, the `devfix` kind, `DEVFIX-HUB.md`) are not on `main` until cards `11`, `12` and `13` ship (adoption-scripts build DECISION 1, 10-03). The row is unchanged in substance; its base is `main` after those three are DEPLOYED.

| row | what | red first | files |
|---|---|---|---|
| V1 | DEVFIX VERBS. The `devfix` kind gains a header key `VERB` with the closed list `dev-rebuild` (today's `TABLE` + `PROOF TEST` route, unchanged), `dev-clean`, `dev-level`. `dev-clean`: `COBALT_ENV=dev uv run cobalt db dev-clean --tickers <A,B,…>` (new CLI verb in `src/cobalt/db_migrations/cli.py`, refused for any database but `env.DESTRUCTIVE_DB_ALLOWLIST`; deletes `aset_sizings` rows of exactly those constructed tickers inside one transaction; prints `CLEANED <ticker> <n>` per ticker; `--dry-run` rolls back) with the card key `TICKERS` (`[A-Z0-9,]`, each 1–6 characters). `dev-level`: `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` under the lock, then `LEVEL 0013` (card `03` L1) and `<F>` quoted; no new string. `DEVFIX-HUB.md` gains one STEPS block per verb; `desk-launch.sh devfix` validates the keys per verb; `CARD.md` and `STANDING-LIST.md` §6 gain the keys and the one NEW string `Bash(COBALT_ENV=dev uv run cobalt db dev-clean *)` (inside the dev `db` class, direction row 2 (b), R39) | offline: a unit test of the verb's SQL builder and its allowlist refusal (constructed tickers); with-DB, marked: `dev-clean --dry-run` on rows the test writes inside the suite transaction → `CLEANED` lines, nothing left; `tests/ops/test_desk_launch_devfix.py` gains the three verbs (good cards print filled lines; a `TICKERS` value with a lowercase letter or a space → `REFUSED`; `VERB` outside the list → `REFUSED`). RED on `BASE`: no verb | `src/cobalt/db_migrations/cli.py`, the test files, `ops/desk/desk-launch.sh`, `docs/40 - DevDocs/prompts/DEVFIX-HUB.md`, `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md` |

## NOT IN THIS JOB
- `dev-clean` of anything but `aset_sizings` rows by constructed ticker; any delete on production; a `dev-level` below `0013`.
- Anything of card `03`'s other rows; the hub files of card `02`.

## READ
- `prompts/2026-10-02/12-devfix-route-card.md` (the kind and `DEVFIX-HUB.md` as built), `11-dev-rebuild-card.md`, `13-slot-guard-card.md`; `src/cobalt/db_migrations/cli.py` `cmd_migrate`, `cmd_dev_rebuild`; `src/cobalt/env.py` `DESTRUCTIVE_DB_ALLOWLIST`; `ops/desk/desk-launch.sh` the `devfix` kind.

## CHECK ASKS
- X1 Can `dev-clean` reach any table but `aset_sizings`, any database but `cobalt_dev`, or a ticker not in `TICKERS`? Can a ticker value smuggle SQL?
- X2 Does `dev-level` ever go below `0013` or run outside the lock?

## RECORDS
- Split from card `03` by the judge (adoption-scripts build DECISION 1, 10-03): `03` proceeds on `a09f0862` without L6; this card waits for `11`, `12`, `13` on `main`. With-DB job: takes the lock.
