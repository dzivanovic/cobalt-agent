# BUILD — deploy-hub-text (card `02b`, re-issue 3), 2026-10-03

The first build's report is at `696847b1` (first build tip `50bd02d8`, check fix `59ef8d48`). Re-issue 1 was built at `69bf6082` (report `d2f3156e`). Re-issue 2 was built at `2cc6330e` (report `482a3f12`). This file is re-issue 3's report. Re-issue 3 changes only T1's sentence (JUDGE ASK 18, Grok re-read F2: REVERSE edits are migrations). It resumed at E3 in a new session on the desk's `CONTINUE: E3` (RECOVERY).

## §0 Headline
- Re-issue 3 rewrites T1's sentences in `DEPLOY-HUB.md` P7 (line 65) and STEP-T (line 85), at commit `3395ef68` (+2 / −2). T6 and C1 are unchanged from `2cc6330e`.
- T1: a migration is now any `.sql` under `src/cobalt/db_migrations/`, or a changed line inside `FORWARD = (…)` **or `REVERSE = (…)`** that adds, removes or reorders an entry. Every other change under that folder is CODE, including any other line of `__init__.py`.
- `git diff 44b29c63` of the file still touches only P7, STEP-T and STEP-C.
- Suites: offline 3739 passed / 0 failed. Live-note 146 / 0. `tests/ops` 564 / 0. DB: none, so no lock was taken. RESTARTS: none. One decision (ASK DESK 1, not for Dejan).

## L74
A system reminder in this session asked for a `Claude-Session:` trailer on commits. It is recorded here once and was not acted on. The commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Re-run at 20:45 EDT for the re-issued card:
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | no hit | nothing |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../2026-10-03/02b-deploy-hub-text-card.md"` | no hit | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `38824130c61bd54ebcc22d3a3b34046de23be6e7` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | nothing |
| R47 | `grep -n "^\| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, … \| HIS RULING · APPROVED \|` |
| R154 | `grep -n "^\| R154 " …` | 0 | `161:\| R154 \| 17:29 ET \| HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check … \| HIS RULING · APPROVED \|` |
| R157 | `grep -n "^\| R157 " …` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week, … \| HIS RULING · APPROVED \|` |
R60, and the commits for R47, R154 and R157: proven in the earlier AUTHORIZATION tables (reports `696847b1`, `482a3f12`). The rows are unchanged.

## PREFLIGHT
RECOVERY entry, in order:
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| head | `git log --oneline -3` | 0 | `482a3f12 docs(deploy-hub-text): build report — 2cc6330e` · `2cc6330e fix(deploy-hub-text): STEP-C reads the Label string …` · `d2f3156e docs(deploy-hub-text): build report — 69bf6082` |
| no .env | `ls -la /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | 1 | `No such file or directory` |
| clock | `date` | 0 | `Sat Oct  3 20:44:56 EDT 2026` |
| the T1 sentences before the edit | `grep -n -F "FORWARD" ".../DEPLOY-HUB.md"` | 0 | `65:- **P7 THE MIGRATIONS**: … or a changed line inside FORWARD = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every .py under that folder (cli.py, placement.py, dev_rebuild.py), tests and docs are CODE and pass MIGRATIONS: none. …` · `85:- After the merges, … (P7: every file ending .sql under that folder, and __init__.py only when a changed line inside its FORWARD = (…) adds, removes or reorders an entry) … every .py, test and doc under that folder is CODE and passes; … a changed line inside FORWARD = (…) that adds, removes or reorders an entry is a migration …` |
| the finding | Read `reports/deploy-hub-02b-grok-reread-2026-10-03.md` | — | finding 2: a REVERSE add / remove / reorder is not inside `FORWARD = (…)`, and `__init__.py` is a `.py`, so the r3 sentence calls it CODE. |
| the judge's row | `grep -n -F "ASK 18" ".../reports/cto-2026-10-03.md"` | 0 | `161:\| R155 \| 20:44 ET \| LAUNCHED: Grok re-read 2 findings → brain JUDGE ASK 18: F2 HOLD (REVERSE edits are migrations; its P7 text), F1 DROP (fail-loud); no third read. 02b re-issued (T1 only, CHECK REPORT -r4); build resumed at E3. … \| LAUNCHED \|` |

Card `## RECORDS`, copied (the desk's facts):
- Judge, 10-03 20:26 (JUDGE ASK 18, Grok re-read): Grok r2 F2 fixed: REVERSE edits are migrations. F1 dropped as fail-loud by design. No third Grok read. Check r3 ready YES at `2cc6330e`. Only T1's sentence changes in this re-issue. r4 writes `opus-1-r4.md`.
- Judge, 10-03 20:04 (JUDGE ASK 17): T6 as checked in r2 O1/O2. Re-read below: T6's greps are unchanged.
- Check r2 at `69bf6082`: T1 and C1 as written, the diff limited to P7, STEP-T and STEP-C.
- Judge, 10-03 ~19:50 (JUDGE ASK 16): Grok's 8 findings were answered. T2–T5 are carried to 03d.
- Judge (finding 2): no `.sql` test fixture exists under `src/cobalt/db_migrations/`.
- Judge, 10-03 19:12 (JUDGE ASK 15): ADDED or MODIFIED is kept. The wording is superseded.
- The first build `50bd02d8` was checked ready YES at `59ef8d48`.
- The card ships alone and docs-only. Its other-house read is Grok after the check.
- The `03c` chain (`9694a679`) is ported later by `03d`.

## E0 BASELINE
Not re-run: the re-issue resumes at E3. The first build's E0 on `44b29c63`: offline `3739 passed, 745 skipped, 1 xfailed`, live-note `146 passed, 1 skipped` (report at `696847b1`).

## E2 RED
Not re-run: the re-issue resumes at E3. T1's red is a grep on the hub text. Before the edit, the new P7 phrase was absent and `every .py under that folder` was present (PREFLIGHT line 65). The mutation below shows both going red again.

## E3 THE ROWS
- **T1** P7 (line 65): the r3 clause was replaced with the card's sentence, verbatim: "a MIGRATION is any file ending .sql under src/cobalt/db_migrations/ (whatever its name), or a changed line inside FORWARD = (…) or REVERSE = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every other change under that folder (cli.py, placement.py, dev_rebuild.py, tests, docs, and any other line of __init__.py) is CODE and passes MIGRATIONS: none." P7's own command clause now reads "a changed line inside `FORWARD = (…)` or `REVERSE = (…)` that adds, …".
- **T1** STEP-T (line 85): both "a changed line inside `FORWARD = (…)`" phrases now read "inside `FORWARD = (…)` or `REVERSE = (…)`", as the card says. The phrase "every `.py`, test and doc under that folder is CODE and passes" now reads "every other change under that folder is CODE and passes", to match P7 (ASK DESK 1). The FORWARD check grep (`'MIGRATIONS_DIR / "'`) is unchanged.
- **T6**, **C1**: no edit in this re-issue. Their greens were re-run at the tip (table).

Greens at `3395ef68` (each its own `grep -c -F` on the file, except the one marked Grep tool):
| row | pattern | count | want |
|---|---|---|---|
| T1 | `whatever its name` | 1 | 1 |
| T1 | `[0-9][0-9][0-9][0-9]_*.sql` | 0 | 0 |
| T1 | `MIGRATIONS_DIR / "00` | 0 | 0 |
| T1 | `inside FORWARD = (…) or REVERSE = (…) of src/cobalt/db_migrations/__init__.py` | 1 | 1 |
| T1 | `every .py under that folder` | 0 | 0 |
| T1 | `every other change under that folder` | 2 | 2 (P7, STEP-T) |
| T1 | `` `REVERSE = (…)` `` (Grep tool, regex `REVERSE = \(…\)`) | 2 lines | P7 command clause and STEP-T (the P7 sentence's unbackticked `REVERSE = (…)` shares line 65) |
| T6 | `a Label the read cannot find is refused` | 1 | 1 |
| T6 | `is not a key of configs` | 0 | 0 |
| C1 | `trap on every exit` | 0 | 0 |
| C1 | `leftover lock after a FAILED gate` | 0 | 0 |
| C1 | `THE EQUAL-TREE CLAUSE` | 0 | 0 |
| C1 | `The rule for (v) when it lands` | 0 | 0 |
| C1 | `never a resend` | 0 | 0 |

THE MUTATION (Edit tool): the r3 P7 clause was put back in place of the fix.
| row | mutation | grep under mutation |
|---|---|---|
| T1 | "or a changed line inside FORWARD = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every .py under that folder (cli.py, placement.py, dev_rebuild.py), tests and docs are CODE and pass MIGRATIONS: none." restored | `inside FORWARD = (…) or REVERSE = (…) of src/cobalt/db_migrations/__init__.py` → `0` (needs 1); `every .py under that folder` → `1` (needs 0) |

The mutation was undone with the Edit tool. Afterwards the new phrase → 1. `git diff --stat` showed `DEPLOY-HUB.md | 4 ++--` and the report's last line only.

X3: `git diff -U0 44b29c63 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` has three hunks: `@@ -65 +65 @@` (P7), `@@ -85 +85 @@` (STEP-T), `@@ -89 +89 @@` (STEP-C). `git diff --stat 44b29c63 -- <file>` → `6 +++---`, `1 file changed, 3 insertions(+), 3 deletions(-)`.

DevDocs line: no page for `DEPLOY-HUB.md` exists under `docs/40 - DevDocs/cobalt/`, and no module changed, so no line was written.

Commit `3395ef68 fix(deploy-hub-text): P7/STEP-T read a FORWARD or REVERSE entry change as a migration; every other change under db_migrations is CODE (T1, L42, L67, L72)`.

## RESTARTS
`uv run cobalt jobs restarts 44b29c63..HEAD`:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-
docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md	M	DOCS	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `3395ef68`.
- (a0) `git diff --name-only --no-renames 44b29c63` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` (the whole output). Every path starts with `docs/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 575.20s (0:09:35)`, exit 0. This build adds no test.
- (e) `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → "No such file". `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.45s`. Skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `564 passed, 1 xfailed, 15 warnings in 238.32s (0:03:58)`, exit 0.
- (b)–(d), (f): not run (DB: none).

## PRE-STOP SELF-CHECK
1. T1's two greps were red under the E3 mutation (`0` and `1`) and are green at the tip. T6's greps were shown red under their mutation at `2cc6330e` (report `482a3f12`), and C1's at `69bf6082` (report `d2f3156e`); both are green at the tip (table).
2. A hub-text row has no code callers. The two places that classify a migration are P7 (line 65) and STEP-T (line 85); both carry FORWARD-or-REVERSE and "every other change under that folder is CODE". The third mention of FORWARD (line 108, W (c2)) is the dev forward run, not a classifier, and is untouched.
3. Line numbers and quotes were re-read at `3395ef68`: `git diff -U0 44b29c63 -- <file>` → hunks at 65, 85, 89; the green table's greps ran on the committed text (the tree equals `3395ef68` for that file); `git log --oneline -1` → `3395ef68`.

## FOR THE CHECK
- Range `44b29c63..3395ef68`. Commits: `50bd02d8 fix(deploy-hub-text): migration = NNNN_*.sql or FORWARD change; ops/desk plist passes STEP-C; Grok findings 1-5 sentences (T1-T6, L42, L67, L72)` · `696847b1 docs(deploy-hub-text): build report — 50bd02d8` · `59ef8d48 fix(deploy-hub-text): STEP-T reads the merged FORWARD diff; an ops/desk plist with a registry label is refused (check O1, O2)` · `69bf6082 fix(deploy-hub-text): P7/STEP-T migration = any .sql or a FORWARD entry change; STEP-C refuses every ops/ plist but a non-resident ops/desk/ one; T2-T5 sentences cut (T1, T6, C1, L42, L67, L72)` · `d2f3156e docs(deploy-hub-text): build report — 69bf6082` · `2cc6330e fix(deploy-hub-text): STEP-C reads the Label string on its key line or the next, against jobs.yaml label: values; an unreadable Label is refused (T6, L67, L72)` · `482a3f12 docs(deploy-hub-text): build report — 2cc6330e` · `3395ef68 fix(deploy-hub-text): P7/STEP-T read a FORWARD or REVERSE entry change as a migration; every other change under db_migrations is CODE (T1, L42, L67, L72)`. Re-issue 3's own range is `482a3f12..3395ef68`.
- Reds, mutations and greens: the E3 tables above.
- Caller greps: none apply (a hub-text row).
- RUN rows: none.
- Suites: offline `3739 passed, 745 skipped, 1 xfailed` · with-DB `not run (DB: none)` · live-note `146 passed, 1 skipped` · tests/ops `564 passed, 1 xfailed`. The commands are quoted under W.
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock take and release: not run (DB: none).
- RESTARTS table: under `## RESTARTS`.
- X1: a `.sql` file under the folder, by any name, is a migration. A FORWARD or REVERSE entry added, removed or reordered is a migration, in P7 and in STEP-T. Every other change under the folder (`cli.py`, `placement.py`, `dev_rebuild.py`, tests, docs, any other line of `__init__.py`) is CODE.
- X2, X3: X2 unchanged from check r3 (STEP-C line 89 untouched). The diff still has three hunks (E3).
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS
- ASK DESK 1: the card names STEP-T's "a changed line inside `FORWARD = (…)`" for the REVERSE addition. STEP-T also said "every `.py`, test and doc under that folder is CODE and passes", which still read `__init__.py` (a `.py`) as CODE, the r3 wording Grok's finding 2 held against. Safe default taken: that phrase now reads "every other change under that folder is CODE and passes", matching T1's P7 sentence. The edit stays inside STEP-T. If the desk wants the literal card text only, revert that one phrase. [20:47 EDT]

## RECORDS
- CONTINUED at E3 20:44:56 EDT. This was a new session on the desk's `CONTINUE: E3` for re-issue 3 (JUDGE ASK 18). The RECOVERY entry ran first: no `.env`, no wip commit. The report's previous last line (re-issue 2's `BUILT` line) was replaced with `RESUMED: E3 20:44:56 EDT` before any other report write.
- Off-list command: this session's first call read BUILD-HUB.md and the card with `cat … ; echo … ; cat …` before reading the rule that forbids it. It was not refused; it only read the two files. Every later call used listed prefixes.
- REFUSED, not needed: `grep -n -F` with a backticked pattern — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." The count was taken with the Grep tool instead.
- L74: one `Claude-Session:` trailer request (system reminder), recorded under `## L74` and not acted on.
- No lock take. `.env` was never present in this worktree; last checked 20:56:30 EDT, "No such file".
- The offline and `tests/ops` suites ran at the same time in the background. Both exited 0.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-hub-text · tip: 3395ef68 | on 44b29c63 | migration: none | offline 3739/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
