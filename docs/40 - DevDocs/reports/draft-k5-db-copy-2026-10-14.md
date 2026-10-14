# draft-k5-db-copy — 2026-10-14

## §0 Headline
- Card 547 written: `prompts/2026-10-14/547-db-copy-card.md`, K5, `db-copy-1014`, five rows (E1 env script, G1 gate copy mode, L1 launcher, D1 lists header, H1 BUILD-HUB `:83`) plus R5.
- A copy cannot be K5 alone: the verb that creates it and the name seam are `src/` code. The card ships inert machinery; copy mode turns on only when the lists file holds `## COPY CREATE` and `## COPY DROP`.
- No new launch-line string. No overlap with 521, 523 or 537; 546 unread (not yet written).
- Nothing was run (no `uv run`): every red is UNPROVEN until the build.

## DECISIONS
1. ASK DESK: the code card the K5 card waits on: a `cobalt db dev-copy create|drop <name>` verb (bootstrap credential; the app role has no `createdb`; names only `cobalt_dev_[a-z0-9_]{1,50}`, never `cobalt_dev` or `cobalt_brain`) and a dev-only name seam `COBALT_DEV_DB_NAME` in `src/cobalt/env.py`, plus the tests that name `"cobalt_dev"` as a literal. The seam touches the wording of RULING 7 ("not configurable", `env.py:28-30`, `:88-100`): his word or not is the desk's to say. Default: card 547 builds the inert half; the code card adds the two sections to `gate-lists.md` when it deploys. [07:38 ET]
2. ASK DESK: LAWS L76 change (the desk's, not the card's). Today: the lock is released "at the end of that step". Under copy mode it is released after the copy is made; a deploy gate still holds it alone. Default: L76 stands until copy mode is on; the desk amends it then. [07:38 ET]
3. ASK DESK: overlap check with card 546 (deploy freeze), unread. Card 547 edits `desk-launch.sh:1082-1089` (`lock_free`) and `BUILD-HUB.md:83`. Default: 546 touches neither; the desk compares line ranges when 546 is written. No overlap with 521, 523, 537. [07:38 ET]
4. ASK DESK: `CHECK-HUB.md` (lock text at lines 8, 10, 12, 18, 33 and others) is not edited; checks get copy mode through `gate.sh` anyway. Default: a later hub-text card words it. [07:38 ET]
5. ASK DESK: `CREATE DATABASE … TEMPLATE cobalt_dev` fails while any other session is connected to `cobalt_dev` (a devfix, a `db query`, his psql), and each copy costs the database's size in disk. The card makes a failed create fail closed (`copy not created`, exit 1, nothing left). Default: no connection is terminated; the desk reads `pg_database_size` before copy mode is on. [07:38 ET]

## RECORDS
- Read at `main` HEAD `0ffb6949`, 2026-10-14 07:38 ET; `git diff --stat HEAD` over every file the card edits printed nothing.
- Read: `survey-blockers-2026-10-12.md` rows 13, 16; `cto-2026-10-14.md` R1471; `cto-2026-10-14-words.md` `## R1471`; LAWS L76, L81; `gate.sh` whole; `gate-lists.md` whole; `take-devdb-lock.sh`, `release-devdb-lock.sh` whole; `desk-launch.sh` `:1070-1105`; `tests/ops/test_devdb_lock.py:1-336`; `BUILD-HUB.md:76-91`; `src/cobalt/env.py:20-100`; `src/cobalt/devdb.py:1-110`; `restarts.py:215-254`; cards 521, 523, 537 and `CARD.md` whole; prompt 541.
- Not read: card 546 (absent), `CHECK-HUB.md` beyond a count of its lock lines, `desk-launch.sh` outside the cited ranges, `bare-guard.py` G3.
- New command strings on a launch line: none (R411, R412).

DRAFTED · decisions: 5
