# BRAIN — the shared dev database: queue or copies (answer, 2026-10-02)

Seat `brain` (successor of `776c834d`), answering `devdb-parallel-question-2026-10-02.md` (desk R152; the question file's header says R151, corrected by the desk 17:18 ET; this answer is R153). Read-only: nothing launched, nothing changed. Every figure names its source; what is an estimate says so.

## §0 Headline
1. Recommendation: at most TWO dev databases, fixed and named (`cobalt_dev` plus one), never a copy per hub. And not yet: three cheaper steps come first, and the second database is decided on measured numbers after them.
2. The queue (option A) is already built. Card `16` (READY, tip `551f07e0`) replaces the lock that fails with a lock that waits; it ships in tonight's deploy. Today's 14 FAILED + CONTINUE were the old lock's last day.
3. Two steps cost no machine resource and are larger than a copy: (i) six of today's ten cards changed only shell scripts and hub text, yet each held the database for a full gate; (ii) 69% of a gate's hold re-runs tests that already passed without the database.
4. A second database costs little memory. Its real cost is load on the ONE Postgres server that also holds production, in market hours. The desk sized the Mac; the limits that matter are Docker's share and that server.
5. Your bound holds on arithmetic alone: wait falls as 1/N. Of today's 8 queued hours a second database returns 4 h, a third 1 h 20 min more, a fourth 40 min more.

## What holds the database, measured
One gate, check `17` (`desk-tools-a-check-2026-10-02.md` lines 143–149):

| part of the hold | time | changes the schema |
|---|---|---|
| lock taken 13:20:16 → released 13:37:22 | 17 min 06 s | — |
| pass 1 at level `0013`: `4383 passed` | 709.60 s (11 min 49 s) = 69% | no: every test is one transaction, rolled back (`tests/cobalt/conftest.py:133-193`) |
| migrate forward `0014`–`0022`, pass 2 (`171 passed`, 220.14 s), rollback to `0013`, fingerprints | about 5 min | yes: 8 tables created, then dropped |

- The same tree run with no database: `3784 passed, 673 skipped` in 595.72 s. So pass 1 runs those 3,784 tests a second time, under the lock, to reach the roughly 600 that need the database.
- The worker's own turns are about 1 min 30 s of the hold. A scripted gate (`gate.sh`) will not shorten it much.
- Why two hubs cannot share one database even for pass 1: tests with the `migrated` fixture apply migration DDL inside their transaction, which locks tables against everyone else. The `DeadlockDetected` flake (seen 09-30 and 10-02) is that collision with a writer not yet identified.

## What a second database costs
| resource | cost | basis |
|---|---|---|
| memory in Docker | near zero at rest | one server: Postgres's cache is one pool for all its databases; a second database adds a few connections, each a small process. ESTIMATE until measured |
| memory on the Mac | one more test run at a time | today already ran about six hubs at once (desk); a parallel gate adds one `pytest` process |
| disk | one more copy of `cobalt_dev` inside Docker's disk image | size NOT measured; at `0013` it has 35 relations, 664 columns (same report, line 144). The Mac's 446 Gi free is not the limit; the Docker image is |
| CPU and disk I/O | doubles test load on the server | `src/cobalt/db.py:163-165`: "there is one server". Production `cobalt_brain` and `cobalt_dev` share it, and the gates ran 08:30–16:30, market hours |
| safety | a closed name list replaces one constant | `env.py:45,48`: the dev name and the destructive allowlist are the single name `cobalt_dev`; the suite refuses any other (`conftest.py:163`, `:210`) |

A second Postgres SERVER (its own container) is a different thing: it would cost real memory (its own cache), and it is the only option that takes test load off the production server. Not proposed now; measure 1 below says whether it is ever needed.

## The steps, cheapest first
| # | step | what it removes | cost | whose word |
|---|---|---|---|---|
| 1 | The waiting lock (card `16`) | every FAILED + CONTINUE on a held lock | none; deploys tonight | done |
| 2 | A card that touches no `src/`, `tests/cobalt`, `tests/taxonomy`, `configs/` or migration takes no lock: the offline suite and the live-note suite still run; the deploy gate still runs all three suites on the merged tree | the holds of `16`, `17`, `18`, `19`, `12`, `21` today (their `touches` column in the direction; confirm by `git diff --stat`); most of tomorrow's script cards | hub text, one card | YOURS: it narrows L68 |
| 3 | Pass 1 under the lock runs only the tests the offline run skipped | up to 10 of the 17 minutes per hold. ESTIMATE: the with-DB subset's own time is not measured | hub text (the pass-1 command), one card | mine, your veto |
| 4 | Wait budget: the lock waits 90 min, which is four holds ahead; a fifth waiting hub still fails | the remaining FAILED case | one number, or staggered launches | desk |
| 5 | A second fixed database `cobalt_dev_2` | half of what queue is left | below | YOURS, after the measures |

What step 5 takes if you order it: product code (`env.py` resolves the dev name from a closed list of two; the suite guard and the destructive allowlist follow) with a normal outside-house check; the lock script becomes two locks and writes the slot's name into the worktree's `.env` copy, so no worker types a new command string and no permission class is added; `dev-rebuild` and the slot guard take a name; the second database is created once at `0013` by a devfix card. Roles are server-wide and `0001_schemas.sql:55-82` already creates them only if absent. About two cards.

## Why not a copy per hub
- Today's peak was about six hubs: six copies, twice your bound, and no ceiling in the design.
- Workers would need create and drop database rights on the server that holds production: a new destructive permission class.
- A free database name weakens the one check that keeps tests out of `cobalt_brain`.
- After steps 2 and 3 there is little queue left for copies three to six to remove.

## Measure first — all read-only
| # | measure | decides |
|---|---|---|
| 1 | `docker stats --no-stream`, once idle and once during a gate's pass 1 | whether one gate already presses the Postgres container, the LLM or the radar; whether two at once is safe in market hours |
| 2 | Docker's memory, CPU and disk-image limits and use (`docker info`, `docker system df`) | the real headroom |
| 3 | On the server: size of `cobalt_dev`, `shared_buffers`, `max_connections`, version; and `pg_stat_activity` for `cobalt_dev` while no hub holds the lock | disk per copy; connection room; names the unidentified second writer (tomorrow's survey row) |
| 4 | Wall time of the with-DB tests alone | the size of step 3 |
| 5 | Today's holds from the reports: count, minutes, and which jobs' diffs touched `src/` or `tests/` | the size of step 2; the true queue |
| 6 | Whether any with-DB test needs rows in `cobalt_dev` that no migration creates; whether the nightly backup dumps every database | how a second database is created; backup growth |

Measures 1 and 2 are Docker commands, outside every worker's list: yours, or a string you allow. 3 to 6 fit a read-only survey card.

## DECISIONS
1. FOR DEJAN — step 2, the no-lock card class. My recommendation: yes. It narrows L68 for the build and the check only; the deploy gate is unchanged.
2. FOR DEJAN — the bound. My recommendation: two fixed databases as the ceiling for now; a third only if a measured day after steps 1–3 still queues more than an hour.
3. FOR DEJAN — when. My recommendation: steps 2–4 ride tomorrow's adoption card; the measures run tomorrow; step 5 is ordered or dropped on their numbers, not before.
4. Mine, your veto — step 3, if measure 4 shows the with-DB subset is under about five minutes.

## RECORDS
- Corrections to the desk's 17:0x sizing: the database server is not elsewhere, it is the one server `POSTGRES_HOST` names, shared with production (`db.py:163`); "the meter limits us before the machine" was said without the Docker footprints.
- Not measured by me: database size, Docker limits, container load, the with-DB subset's time, the count of today's holds. The 8 h figure is the desk's (08:30–16:30); the 17 min 06 s is one gate.
- Files read: the question file; `BUILD-HUB.md` `## THE LOCK` and `## W`; `CHECK-HUB.md` lock lines; `tests/cobalt/conftest.py` 1–230; `src/cobalt/env.py` and `db.py` name and address lines; `take-devdb-lock.sh` at `551f07e0`; `desk-tools-a-check-2026-10-02.md` lines 143–150; the desk's lock rows R61–R69, R104.

ANSWER WRITTEN — decisions: 4 · for Dejan: 3
