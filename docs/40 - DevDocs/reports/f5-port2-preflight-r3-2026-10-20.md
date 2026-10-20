# F5 port2 preflight round 3 — card 731 as fresh port job `f5-checkpoints-fr2`, amended twice (read-only, 2026-10-20 07:18 EDT)

Card: `prompts/2026-10-18/731-f5-card.md` (134 lines, read whole). main HEAD `4ab0d0f4`; card BASE `b842b08f` trails by desk commits (not a fail). `git diff cbac8938 4ab0d0f4 --stat` on the card: 1 line changed (the PORT row), so every round 2 OK stands unless a check below says otherwise. Nothing run but reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | FAIL 22: `grep -n -o -E "(offline line\|readers line\|DEPLOY PROOF)"` over the card | hits only at :43 (PORT1), :44 (FIX2), :133 (dated RECORDS); PORT (:45), DONE WHEN (inside PORT (3)) and CHECK ASKS (:79-94) hold none. PORT (7) now reads "K12 four with-DB tests …; the deploy gate pass: the `## OFFLINE` line of `ops/desk/gate-lists.md` as written"; `git grep "^## OFFLINE" HEAD -- ops/desk/gate-lists.md` → `:23` | OK |
| 2 | `git diff --stat HEAD -- <card>` | empty: card committed (`4ab0d0f4`) | OK |
| 3 | `grep -c "«FILL"` (read whole) | none | OK |
| 4 | header read | JOB / BRANCH / WORKTREE / REPORT / CHECK REPORT all `f5-checkpoints-fr2`; `BAND: HIGH`; `TIP:` empty | OK |
| 5 | round 1 fix a: smoke lines vs `deploy-smoke.sh` | `## DEPLOY PROOF` :97-102 six `grep -c -F` lines, :103 prose note, no suite line; markers `git grep -c -F` on `3c96ad2e`: `checkpoints:` prefill.yaml 1, `checkpoint.narrative:` modelaccess.yaml 1, four `label: com.cobalt.checkpoint-0…` jobs.yaml (4 hits); on HEAD all print nothing (before 0) | OK |
| 6 | round 1 fix b: RESTARTS | header :13, RECORDS :124, PORT (7) all `com.cobalt.aset com.cobalt.cos com.cobalt.radar` | OK |
| 7 | round 1 fix c: every PORT / DONE WHEN command vs `BUILD-HUB.md:14` | uses `ls`, `git show`, `git diff [-M/--stat/--name-only]`, `git log --merges`, `uv run cobalt jobs restarts`, `uv run pytest`, `COBALT_ENV=dev …`, the Grep tool; all on the allow line. `git mv`/`git grep`/`--no-db` text only in K0 :25, PORT1, FIX2, dated RECORDS, and PORT's own "no git mv" prohibition | OK |
| 8 | `git diff --name-only bd5dd70a 3c96ad2e` vs PORT files cell | 52 names, 2 reports (not ported), 50 ported; the cell lists the same 50 (migration pair as `<NNNN>_market_checkpoints*.sql`) | OK |
| 9 | `git diff --stat bd5dd70a HEAD -- src tests configs ops "docs/40 - DevDocs/cobalt" DEPLOY-HUB.md` | empty: main touched none of the 50 | OK |
| 10 | migration number: `ls src/cobalt/db_migrations`; `git show HEAD:…/__init__.py` | highest `0028_genesis_vectors` (+ rollback); no 0027, no 0029; `FORWARD` last `0028_genesis_vectors.sql`; `REVERSE` first `0028_genesis_vectors.rollback.sql`; next free `0029` = PORT's expected number; PORT (0) makes the builder re-prove and quote | OK |
| 11 | `git grep -c "0027" 3c96ad2e -- src tests configs ops "docs/40 - DevDocs/cobalt"` vs PORT (3) | 27 files (2 sql, `__init__.py` 6, `placement.py` 1, 3 docs, 20 tests); each is named in PORT (3) with class R, M or C; 27 renumber + 23 equal = 50 | OK |
| 12 | migration LAST in `FORWARD`, FIRST in `REVERSE`, `placement.py` | PORT (2): `FORWARD` last after `0028_genesis_vectors.sql`, `REVERSE` first before `0028_genesis_vectors.rollback.sql`, docstring pair after 469's pair, gap note rewritten (HEAD still says 0027 is F5's); `placement.py` HEAD ends `CREATED_TABLES` at `genesis_chunk` (:126), PORT adds `market_checkpoints: Side.SYSTEM` after it | OK |
| 13 | PORT one row; old rows | one row `\| PORT \|` (:45); PORT1, FIX1, FIX2 start `NOT REBUILT` / `NOT REBUILT (…`; K0-K13, R1, B0, D0 declared content | OK |
| 14 | `## LAUNCHD` (:51-55) | four plists, mode `deferred`, ref `…731-f5-card.md:PORT`; no checkpoint plist on HEAD; the four `ops/com.cobalt.checkpoint-*.plist` paths in the files cell | OK |
| 15 | `--no-db` spelling | only the prohibition in FIX2 :44; none in PORT or smoke lines | OK |
| 16 | K10 RESTARTS homes | unchanged from round 2 #6 (prefill.yaml, modelaccess.yaml → aset; cli.py, checkpoints.py, db_migrations → radar; config.py → aset,cos,radar per the fr1 check; sql, plists, docs, tests, gate-lists as classified); no card line changed it | OK |
| 17 | CHECK ASKS :79-94 | fr1-number asks :83-85 SUPERSEDED; :86 scope, :87 THE NUMBER, :88 SHARED FILES present; X1-X6 intact; none cites a dropped line | OK |
| 18 | PORT (6) counts | 23 equal + 27 renumber = 50, matches #8 and #11 | OK |
| 19 | `cli.md` seam | PORT (4) has the builder find the end of the last section by content | OK |
| 20 | K0 / K6 / DECISION 3 wording | "next free at BASE"; DECISION 3 marked SUPERSEDED; PORT does not run K0 as a stop row | OK |
| 21 | `git log --merges bd5dd70a..HEAD` | empty | OK |
| 22 | what blocks the card's own build | nothing found: every command the builder is told to run is on the BUILD line; no instruction points at a missing line | OK |

## ISSUES

- NOTE: K0 (:25) is a `RUN` row quoting two `git grep` commands the BUILD line does not admit; PORT does not run K0. Unchanged from round 2.
- NOTE: `docs/40 - DevDocs/cobalt/prefill/checkpoints.md` at `3c96ad2e` (the laws on the job) still says restarts are `com.cobalt.aset`, `com.cobalt.radar`; ported byte-equal, a doc line only.
- NOTE: CHECK ASKS :82 (Genesis lower number) is stale context, left by decision.
- NOTE: header BASE `b842b08f` trails main `4ab0d0f4` by desk commits; the set diff stays empty.
- NOTE: `jobs restarts` and the pytest lines were not run (read-only seat); the `cos` label rests on the fr1 check's run at `3c96ad2e`.

PREFLIGHT DONE · card: f5-checkpoints-fr2 · checks: 22 · fails: 0 · ready: YES
