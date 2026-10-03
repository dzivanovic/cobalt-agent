# BUILD — deploy-hub-text (card `02b`), 2026-10-03

## §0 Headline
- Six rows built in `DEPLOY-HUB.md` on `main`'s text, in one commit `50bd02d8` on `44b29c63` (one file, +7 / −6).
- T1: P7 and STEP-T now count only `NNNN_*.sql` files (with their rollback twins) and a `FORWARD` registry change as a migration. `cli.py` and other code under the folder pass `MIGRATIONS: none`. T6: a plist added under `ops/desk/` passes STEP-C.
- T2–T5 add Grok's findings 1–5 as sentences at the places the card names, so the `03d` port can copy them.
- Suites: offline 3739 passed / 0 failed. Live-note 146 passed / 0 failed. `tests/ops` 564 passed / 0 failed. DB: none, so no lock was taken. RESTARTS: none.
- One decision, not his: STEP-C still refuses a MODIFIED plist that carries a registry label. The card's wording says "added".

## L74
One block asked for a `Claude-Session:` trailer on commits: a system reminder at the start of this session. Recorded here once and not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Started 18:45:54 EDT (`date`: `Sat Oct  3 18:45:54 EDT 2026`).

| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | nothing |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../2026-10-03/02b-deploy-hub-text-card.md"` | 1 | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `2c1691ba5bd88854f913c449fb4b45a10fa54f69` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | nothing |
| STANDING LIST R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R47 | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, … | HIS RULING · APPROVED |` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING R154 | `grep -n "^| R154 " ".../cto-2026-10-02.md"` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no `src/`, test, config or migration path takes no dev-DB lock at build + check (L68 narrowed there only); … | HIS RULING · APPROVED |` |
| R154 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R154 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| RULING R157 | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, … | HIS RULING · APPROVED |` |
| R157 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R157 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| head = BASE | `git log --oneline -1` | 0 | `44b29c63 Merge branch 'main' into deploy/set2c-1003` |
| branch from main checkout | `git -C /Users/cobalt/cobalt log --oneline -1 ops/deploy-hub-text-1003` | 0 | `44b29c63 Merge branch 'main' into deploy/set2c-1003` |
| first launch | `git diff --stat 44b29c63` | 0 | nothing |
| BASE | `git show --stat 44b29c63` | 0 | `Merge: f99d81f6 bec2a990` · `docs/40 - DevDocs/reports/deploy-set2c-1003.md | 132 +++` · `1 file changed, 132 insertions(+)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env: No such file or directory` |
| .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| symbol: STEP-G red path | `grep -n -F "A red anywhere" DEPLOY-HUB.md` | 0 | `115:- A red anywhere → name each test and assertion, (f) and THE RELEASE if the lock is held; …` |
| symbol: outage rule | `grep -n -F "INSIDE THE OUTAGE" DEPLOY-HUB.md` | 0 | `43:- A DEPLOY NEVER CONTINUES BY MESSAGE … INSIDE THE OUTAGE (4.1 to the end of 4.6) the strict rule stays: ANY refused call → STEP-5 first. Never a retry in another spelling.` |
| symbol: P1 | `grep -n -F "P1 DATE AND WINDOW" DEPLOY-HUB.md` | 0 | `59:- **P1 DATE AND WINDOW**: … Under (i) and (ii) the outage itself must begin before 04:00 ET: D2.6 reads the clock again.` |
| symbol: P7 | `grep -n -F "P7 THE MIGRATIONS" DEPLOY-HUB.md` | 0 | `65:- **P7 THE MIGRATIONS**: for each head, `git -C /Users/cobalt/cobalt diff --stat main <head> -- src/cobalt/db_migrations` → only the files of the card's `MIGRATIONS` (NOTHING when `none`), else …` |
| symbol: STEP-C | `grep -n -F "## STEP-C" DEPLOY-HUB.md` | 0 | `88:## STEP-C — THE CONFIGS AND THE JOBS (read-only; rule C)` |
| symbol: OPS_DESK_PREFIX | `grep -n -F "OPS_DESK_PREFIX" src/cobalt/jobs/restarts.py` | 0 | `38:OPS_DESK_PREFIX = "ops/desk/"` · `230:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` |
| symbol: FORWARD | `grep -n -F "FORWARD" src/cobalt/db_migrations/__init__.py` | 0 | `135:FORWARD = (` · `183:__all__ = ["FORWARD", "MIGRATIONS_DIR", "REVERSE"]` |
| the folder | `ls src/cobalt/db_migrations` | 0 | `__init__.py`, `__pycache__`, `0001_schemas.sql`, `0002_move_tables.rollback.sql` … `0022_prediction_records.sql` (every `.sql` named `NNNN_*.sql` or `NNNN_*.rollback.sql`), `cli.py`, `placement.py` |
| registry labels | `grep -n -F "close-timer" configs/cobalt/jobs.yaml` | 1 | nothing (card `05`'s label is not in the registry) |
| wc of the row file | `wc -l "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | `186 docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| READ tail | `tail -n 3 ".../reports/deploy-set2-1003.md"` | 0 | `FAILED PREFLIGHT: migration — src/cobalt/db_migrations/cli.py (head 9694a679; card MIGRATIONS: none) · rollback: not used · decisions: 1 · for Dejan: 0` |
| READ tail | `tail -n 3 ".../reports/deploy-hub-other-house-read-2026-10-03.md"` | 0 | `READ DONE · findings: 9` |
| READ tail | `tail -n 3 ".../reports/adoption-hubs-decisions-2026-10-03.md"` | 0 | `FOR THE CHECK (card `02` `## RECORDS`): `Build decisions 1–11 answered …; 1, 8, 10, 11 KEEP; 7 is not his.`` |
| T6's cited stop | `tail -n 3 ".../reports/deploy-set2b-1003.md"` | 0 | `FAILED: C — ops/desk/com.cobalt.close-timer.plist: installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used · decisions: 1 · for Dejan: 1` |
| the chain's text | `git show "9694a679:docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | Read whole (54.4 KB). Its P7 (line 63), STEP-T (line 83) and STEP-C (line 87) are `main`'s. Its STEP-G carries the equal-tree clause (line 99) and the exit-5 / exit-6 bullet (line 102). Its P1 carries (v) (line 57), with the STEP-R re-read at line 93. |
| RESTARTS empty | `uv run cobalt jobs restarts 44b29c63..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` (after a first-run `.venv` build) |

Card `## RECORDS`, copied (the desk's facts; neither is re-readable by a listed command beyond the reads above):
- Judge, 10-03 (deploy set 2 FAILED PREFLIGHT; Grok read): this card ships alone, docs-only, before the `03c` chain and the ports; its other-house read (L67) is Grok on this one file, after the check.
- The `03c` chain (`9694a679`) is then PORTED onto this card's `main` by the brain's `03d` card (the chain's files re-applied; `DEPLOY-HUB.md` = this card's text plus the chain's adoption sentences).

DB: none — no lock probe, no with-DB string used by this build.

## E0 BASELINE
- Offline on `44b29c63`, `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`: `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 581.48s (0:09:41)`. Exit 0, 0 failed, 0 errors.
- Live-note, `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`: `146 passed, 1 skipped, 15 warnings in 28.14s`. The one skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which names no `COBALT_LIVE_VAULT_ROOT`. I ran it while the offline run was in flight; it writes no file.

## E2 RED
No row has a test file. Every row's "red first" is a grep on the hub text, run on BASE before any edit:
| row | command | at BASE |
|---|---|---|
| T1 | `grep -n -F "src/cobalt/db_migrations/[0-9][0-9][0-9][0-9]_*.sql" DEPLOY-HUB.md` | no output (0 hits) |
| T2 | `grep -c -F "trap on every exit" DEPLOY-HUB.md` | `0` |
| T3 | `grep -c -F "came from a whole pass 1" DEPLOY-HUB.md` | `0` |
| T4 | `grep -c -F "a non-empty derived set means (v) does not hold" DEPLOY-HUB.md` | `0` |
| T6 | `grep -c -F "a plist added under" DEPLOY-HUB.md` | `0` |
| T5 | `grep -c -F "a blocked call goes to STEP-5, never a resend" DEPLOY-HUB.md` | `0` |
No test file was written, so there was nothing for a `wip(deploy-hub-text): red` commit and none was made.

## E3 THE ROWS
All six rows are in `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, built in the card's order.
- **T1** P7 (line 65): "a MIGRATION is a file matching `src/cobalt/db_migrations/[0-9][0-9][0-9][0-9]_*.sql` (its `.rollback.sql` twin included) or a change of the `FORWARD` registry in `src/cobalt/db_migrations/__init__.py`; any other path under that folder (`cli.py`, `placement.py`, `dev_rebuild.py`, tests, docs) is CODE and passes `MIGRATIONS: none`." When `__init__.py` is in the stat, `git -C /Users/cobalt/cobalt diff main <head> -- src/cobalt/db_migrations/__init__.py` is read; this matches the deploy line's `git -C * diff*`. STEP-T (line 85) names the same pattern and says "the FORWARD check reads only the matching files". Green: `grep -n -F` of the pattern → `65:` and `85:` (two hits).
- **T2** STEP-G red path (line 115) gets: "When STEP-G runs as one `gate.sh` call (its exit-5 / exit-6 ends included): the release is `gate.sh`'s own trap on every exit; verify `<GATE>/.env` gone and the lock dir absent, then the FAILED line; and a leftover lock after a FAILED gate is the trap's to drop; `gate-clean.sh` removes the worktree." Green: `grep -c -F "trap on every exit"` → `1`.
- **T3** New STEP-G bullet (line 116): "THE EQUAL-TREE CLAUSE, the rule for when it lands (this text has no clause yet): it applies only when the check's three suite lines came from a whole pass 1 (no `--db-only`); otherwise the gate runs whole." Green: one hit, `116:`.
- **T4** End of P1 (line 59): "The rule for (v) when it lands (this P1 has (i)–(iv) only): (v) is re-read at STEP-R with `date` then; a non-empty derived set means (v) does not hold, and D2.6's clock rule binds as under (i) or (ii)." Green: one hit, `59:`.
- **T6** STEP-C (line 89): "A plist added under `ops/desk/` is a FILE of the tree, not a resident: nothing loads it but his install by hand, and `restarts.py`'s `OPS_DESK_PREFIX` classes it as an operator script; it passes (deploy set 2b FAILED STEP-C on card `05`'s plist). STEP-C refuses only a plist under `ops/` ADDED or MODIFIED whose label is in `configs/cobalt/jobs.yaml` or whose path is `ops/<label>.plist` (the launchd install path) → `FAILED: C — …`". Green: one hit, `89:`. See DECISION T6.
- **T5** Outage rule (line 43) gets: "Inside the outage (4.1–4.6) a blocked call goes to STEP-5, never a resend." Green: one hit, `43:`.

THE MUTATIONS were made with the Edit tool, all six at once, each grep run alone and each undone with the Edit tool:
| row | mutation | grep under mutation |
|---|---|---|
| T1 | STEP-T's pattern → "the migration files" | `grep -c -F "<pattern>"` → `1` (needs 2) |
| T2 | "own trap on every exit;" → "own;" | `0` |
| T3 | "a whole pass 1" → "a pass 1" | `0` |
| T4 | "a non-empty derived set means (v) does not hold" → "a derived set means (v) holds" | `0` |
| T6 | "A plist added under" → "A plist under" | `0` |
| T5 | "goes to STEP-5, never a resend." → "is resent." | `0` |
After undoing them: T1's grep → `2`. `git diff --stat` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 13 +++++++------` (the fix, unchanged).

DevDocs line: no page for `DEPLOY-HUB.md` exists under `docs/40 - DevDocs/cobalt/` (Glob `docs/40 - DevDocs/cobalt/*{hub,HUB,deploy,prompt}*` → no files). No module changed, so I wrote no line.

Commit `50bd02d8 fix(deploy-hub-text): migration = NNNN_*.sql or FORWARD change; ops/desk plist passes STEP-C; Grok findings 1-5 sentences (T1-T6, L42, L67, L72)`.

## RESTARTS
`uv run cobalt jobs restarts 44b29c63..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md	A	DOCS	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `50bd02d8`.
- (a0) `git diff --name-only --no-renames 44b29c63` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (whole). Every path starts with `docs/`. **`cobalt_dev: not taken (DB: none — 1 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 579.05s (0:09:39)`, exit 0. This build adds no test.
- (e) `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → "No such file". `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.40s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, which names no `COBALT_LIVE_VAULT_ROOT`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `564 passed, 1 xfailed, 15 warnings in 238.86s (0:03:58)`.
- (b)–(d), (f): not run (DB: none).

## PRE-STOP SELF-CHECK
1. Each row's grep is red at BASE (E2) and red under its E3 mutation (T1 `1`, the others `0`), and green at the tip. No test stayed green under its mutation.
2. A row's rule is entered only by the deploy hub reading its own text, so it has no code callers. For T1, every entry path into the migration check is pinned by the two pattern hits (P7 line 65, STEP-T line 85). For T6, the one STEP-C path is line 89.
3. Every line number and quote above was re-read with `grep -n -F` on the working tree at `50bd02d8`, whose `git status` is clean apart from this report. Also re-run: `git show --stat 50bd02d8` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 13 +++++++------`, and `git log --oneline 44b29c63..HEAD` → the one commit.

## FOR THE CHECK
- Range `44b29c63..50bd02d8`, one commit: `fix(deploy-hub-text): migration = NNNN_*.sql or FORWARD change; ops/desk plist passes STEP-C; Grok findings 1-5 sentences (T1-T6, L42, L67, L72)`.
- Reds, mutations and greens per row: the E2 and E3 tables above.
- Caller greps: none apply (a hub-text row).
- RUN rows: none.
- Suites: offline `3739 passed, 745 skipped, 1 xfailed` · with-DB `not run (DB: none)` · live-note `146 passed, 1 skipped` · tests/ops `564 passed, 1 xfailed`. The commands are quoted under W.
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock take and release: not run (DB: none).
- RESTARTS table: under `## RESTARTS`.
- X1, the builder's read for the check to test:
  - A `.sql` without the four digits is CODE by T1's words. It can only run if it is named in `FORWARD`, and a `FORWARD` change is a migration under P7.
  - A change to `REVERSE` alone is not in the card's definition, and the text follows the card.
  - `cli.py`, `placement.py` and other `.py` files pass.
- X2: the chain's text at `9694a679` has the exit-5 / exit-6 bullet (line 102), the equal-tree clause (line 99), (v) (line 57), and no outage blocked-call sentence. The five sentences here are worded so that the port can paste each one at those places as written. The "when it lands" lead-ins are the only words that belong to `main`'s text alone.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS
1. DECISION T6: the card's T6 says STEP-C "refuses only a plist added under `ops/` whose label is in `configs/cobalt/jobs.yaml` or whose path is `ops/<label>.plist`". `main`'s STEP-C refused ADDED or MODIFIED. I kept "ADDED or MODIFIED" for the plists that carry a registry label or the install path. Dropping MODIFIED would have let a changed `ops/com.cobalt.aset.plist` pass STEP-C, and the fence says the fix widens nothing. Safe default: the narrower pass, which is the text as written. The check may cut it to "added" if the desk reads the card that way. Not his.

## RECORDS
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/adoption-scripts-b2-1003 log --oneline -1` — Permission to use Bash has been denied because Claude Code is running in don't ask mode.
- REFUSED, not needed: `git -C /Users/cobalt/cobalt-wt/adoption-scripts-b-1003 log --oneline -1` — Permission to use Bash has been denied because Claude Code is running in don't ask mode.
- L74: one `Claude-Session:` trailer request (system reminder), recorded under `## L74` and not acted on.
- No extra lock take. `.env` was never present in this worktree; last checked 19:09:01 EDT, "No such file".
- `uv run` built `.venv` in this worktree on its first call. It is a gitignored path.
- Card records as re-read at PREFLIGHT: the two judge lines above. Set 2's and 2b's stops were re-read by `tail`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-hub-text · tip: 50bd02d8 | on 44b29c63 | migration: none | offline 3739/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
