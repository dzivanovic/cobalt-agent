# BUILD — deploy-hub-text (card `02b`, re-issue), 2026-10-03

The first build's report is at `696847b1` (first build tip `50bd02d8`, check fix `59ef8d48`). This file is the re-issue's report. It resumed at E3 on the desk's `CONTINUE: E3` in a new session (RECOVERY).

## §0 Headline
- Three rows built in `DEPLOY-HUB.md`, one commit `69bf6082` on top of `59ef8d48` (one file, +6 / −7).
- T1: P7 now counts any `.sql` under `src/cobalt/db_migrations/`, whatever its name, as a migration. A `FORWARD` change counts only when it adds, removes or reorders an entry. Every `.py`, test and doc under that folder is CODE. STEP-T's FORWARD check greps `'MIGRATIONS_DIR / "'`, with the `00` dropped.
- T6: STEP-C refuses an added or modified plist anywhere under `ops/`. The only exception is an `ops/desk/` plist whose Label is not a `jobs.yaml` key and whose path is not `ops/<label>.plist`.
- C1: the T2–T5 sentences are removed. `git diff 44b29c63` of the file touches only P7, STEP-T and STEP-C.
- Suites: offline 3739 passed / 0 failed. Live-note 146 / 0. `tests/ops` 564 / 0. DB: none, so no lock was taken. RESTARTS: none. No decisions.

## L74
One block asked for a `Claude-Session:` trailer on commits: a system reminder in this session. It is recorded here once and was not acted on. The commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
The first build's AUTHORIZATION table (at `696847b1`) proved R60, R47, R154 and R157. The re-issued card names the same three RULINGS. Re-run at 19:45 EDT for the re-issued card:
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | no hit | nothing |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../2026-10-03/02b-deploy-hub-text-card.md"` | no hit | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `bcdcaae0f8bc6465664a788542a48884a6017ecc` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | nothing |

## PREFLIGHT
RECOVERY entry, in order:
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| head | `git log --oneline -3` | 0 | `59ef8d48 fix(deploy-hub-text): STEP-T reads the merged FORWARD diff; …` · `696847b1 docs(deploy-hub-text): build report — 50bd02d8` · `50bd02d8 fix(deploy-hub-text): …` |
| no .env | `ls -la /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | 1 | `No such file or directory` |
| clock | `date` | 0 | `Sat Oct  3 19:45:40 EDT 2026` |
| main's text = BASE's | `git -C /Users/cobalt/cobalt diff --stat 44b29c63 main -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | nothing |
| the folder (judge finding 2) | `ls src/cobalt/db_migrations` | 0 | `__init__.py`, `__pycache__`, `0001_schemas.sql` … `0022_prediction_records.sql` (all migrations with their `.rollback.sql` twins), `cli.py`, `placement.py`. No `.sql` test fixture. |
| FORWARD entries | `grep -n -F "MIGRATIONS_DIR / " src/cobalt/db_migrations/__init__.py` | 0 | lines 136–156 (`FORWARD`, `0001` … `0022`), lines 161–180 (`REVERSE`) |

READ: the judge's `deploy-hub-text-decisions-2026-10-03.md` whole (all 8 HOLD; the fix text for findings 1, 3 and 4; T2–T5 CUT). Grok's read, findings 1–8. The branch diff at `59ef8d48` against `44b29c63`.

Card `## RECORDS`, copied (the desk's facts):
- Judge, 10-03 ~19:50 (JUDGE ASK 16): Grok's 8 findings were answered. Findings 1–4 are fixed in the P7, STEP-T and STEP-C sentences. T2–T5 are cut from this card and carried to 03d. The card is the P7/T/C fix only.
- Judge (finding 2): no `.sql` test fixture exists under `src/cobalt/db_migrations/`. Re-read above by `ls`: none.
- Judge, 10-03 19:12 (JUDGE ASK 15, build decision T6): ADDED or MODIFIED was kept. The wording is superseded by JUDGE ASK 16's T6 sentence.
- The first build `50bd02d8` was checked ready YES at `59ef8d48`. This re-issue resumes at E3 on that branch. Re-read: HEAD was `59ef8d48`.
- This card ships alone, docs-only, before the `03c` chain and the ports. Its other-house read (L67) is Grok on this one file, after the check.
- The `03c` chain (`9694a679`) is then PORTED onto this card's `main` by `03d`.

## E0 BASELINE
Not re-run: the re-issue resumes at E3. The first build's E0 on `44b29c63` was offline `3739 passed, 745 skipped, 1 xfailed` and live-note `146 passed, 1 skipped` (report at `696847b1`).

## E2 RED
Not re-run: the re-issue resumes at E3. No row has a test file. Each row's red is a grep on the hub text. Each grep is red at `59ef8d48`, the text the rows replace: T1's old pattern was present there, and so were the cut sentences. The mutation table below shows each grep going red again.

## E3 THE ROWS
All in `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, built in the card's order, then committed together.
- **T1** P7 (line 65) now begins with the judge's sentence verbatim: "a MIGRATION is any file ending .sql under src/cobalt/db_migrations/ (whatever its name), or a changed line inside FORWARD = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every .py under that folder (cli.py, placement.py, dev_rebuild.py), tests and docs are CODE and pass MIGRATIONS: none". The `__init__.py` diff clause now reads "a changed line inside `FORWARD = (…)` that adds, removes or reorders an entry is a migration". Without that change it would still call a comment or a rewrap a migration (finding 2).
  STEP-T (line 85) names the same definition and uses the FORWARD check `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/src/cobalt/db_migrations/__init__.py`.
- **T6** STEP-C (line 89) now reads: "A plist ADDED or MODIFIED anywhere under ops/ is refused, except one under ops/desk/ whose Label (the line after <key>Label</key>, read by grep -A1 -F) is not a key of configs/cobalt/jobs.yaml and whose path is not ops/<label>.plist. A refused plist → `FAILED: C — …`". The rest of STEP-C reads as at BASE.
- **C1** Removed the old T5 sentence (outage, line 43), the old T4 sentence (end of P1, line 59), and the old T2 sentence and T3 bullet (STEP-G red path, lines 115–116). Those places read as at BASE.

Greens at the fix (each its own `grep -c -F` on the file):
| row | pattern | count | want |
|---|---|---|---|
| T1 | `whatever its name` | 1 | 1 |
| T1 | `[0-9][0-9][0-9][0-9]_*.sql` | 0 | 0 |
| T1 | `MIGRATIONS_DIR / \"00` (the card's literal) | 0 | 0 |
| T1 | `MIGRATIONS_DIR / "00` (unescaped, also run) | 0 | 0 |
| T6 | `anywhere under ops/ is refused` | 1 | 1 |
| C1 | `trap on every exit` | 0 | 0 |
| C1 | `leftover lock after a FAILED gate` | 0 | 0 |
| C1 | `THE EQUAL-TREE CLAUSE` | 0 | 0 |
| C1 | `The rule for (v) when it lands` | 0 | 0 |
| C1 | `never a resend` | 0 | 0 |

X3: `git diff 44b29c63 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` has three hunks: P7 (line 65), STEP-T (line 85) and STEP-C (line 89). `git diff --stat 44b29c63 -- <file>` → `6 +++---`, `1 file changed, 3 insertions(+), 3 deletions(-)`.

THE MUTATIONS were made with the Edit tool, all at once. Each grep was run alone, then each mutation was undone with the Edit tool:
| row | mutation | grep under mutation |
|---|---|---|
| T1 | "(whatever its name)" → "(named NNNN_*.sql)" | `whatever its name` → `0` (needs 1) |
| T1 | STEP-T `'MIGRATIONS_DIR / "'` → `'MIGRATIONS_DIR / "00'` | `MIGRATIONS_DIR / "00` → `1` (needs 0) |
| T6 | "ADDED or MODIFIED anywhere under ops/" → "ADDED under ops/" | `anywhere under ops/ is refused` → `0` (needs 1) |
| C1 | the outage sentence "… a blocked call goes to STEP-5, never a resend." re-added | `never a resend` → `1` (needs 0) |
After the undo: `whatever its name` → 1, `anywhere under ops/ is refused` → 1, `MIGRATIONS_DIR / "00` → 0, `never a resend` → 0. `git diff --stat 44b29c63 -- <file>` → 3 insertions, 3 deletions: the fix, unchanged.

DevDocs line: no page for `DEPLOY-HUB.md` exists under `docs/40 - DevDocs/cobalt/`, as the first build found. No module changed, so I wrote no line.

Commit `69bf6082 fix(deploy-hub-text): P7/STEP-T migration = any .sql or a FORWARD entry change; STEP-C refuses every ops/ plist but a non-resident ops/desk/ one; T2-T5 sentences cut (T1, T6, C1, L42, L67, L72)`.

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
`<tip>` = `69bf6082`.
- (a0) `git diff --name-only --no-renames 44b29c63` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` (whole). Every path starts with `docs/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 573.81s (0:09:33)`, exit 0. This build adds no test.
- (e) `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → "No such file". `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.65s`. The skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which names no `COBALT_LIVE_VAULT_ROOT`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `564 passed, 1 xfailed, 15 warnings in 239.72s (0:03:59)`, exit 0.
- (b)–(d), (f): not run (DB: none).

## PRE-STOP SELF-CHECK
1. Each row's grep was red under its E3 mutation (T1 `0` and `1`, T6 `0`, C1 `1`) and is green at the tip. No grep stayed green under its mutation.
2. A row's rule is entered only by the deploy hub reading its own text, so it has no code callers. T1: P7 (line 65) and STEP-T (line 85) are the two migration checks, and both carry the new definition. T6: STEP-C (line 89) is the only plist check. C1: all five patterns count 0.
3. Every line number and quote above was re-read at `69bf6082`: `grep -n -F "P7 THE MIGRATIONS"` → `65:`, `grep -n -F "MIGRATIONS_DIR / "` → `85:`, `grep -n -F "anywhere under ops/ is refused"` → `89:`. `git show --stat 69bf6082` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 13 ++++++-------`. `git log --oneline 44b29c63..HEAD` → four commits, `69bf6082` on top.

## FOR THE CHECK
- Range `44b29c63..69bf6082`. Commits: `50bd02d8 fix(deploy-hub-text): migration = NNNN_*.sql or FORWARD change; ops/desk plist passes STEP-C; Grok findings 1-5 sentences (T1-T6, L42, L67, L72)` · `696847b1 docs(deploy-hub-text): build report — 50bd02d8` · `59ef8d48 fix(deploy-hub-text): STEP-T reads the merged FORWARD diff; an ops/desk plist with a registry label is refused (check O1, O2)` · `69bf6082 fix(deploy-hub-text): P7/STEP-T migration = any .sql or a FORWARD entry change; STEP-C refuses every ops/ plist but a non-resident ops/desk/ one; T2-T5 sentences cut (T1, T6, C1, L42, L67, L72)`. The re-issue's own range is `59ef8d48..69bf6082`.
- Reds, mutations and greens per row: the E3 tables above.
- Caller greps: none apply (a hub-text row).
- RUN rows: none.
- Suites: offline `3739 passed, 745 skipped, 1 xfailed` · with-DB `not run (DB: none)` · live-note `146 passed, 1 skipped` · tests/ops `564 passed, 1 xfailed`. The commands are quoted under W.
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock take and release: not run (DB: none).
- RESTARTS table: under `## RESTARTS`.
- X1: any `.sql` under the folder is a migration by name-free suffix. A FORWARD entry added, removed or reordered is a migration. A `.py`, test or doc under the folder is CODE. STEP-T's FORWARD grep matches every entry regardless of its leading digits. A `REVERSE`-only edit is not in the judge's definition, and the text follows it.
- X2: any added or modified plist under `ops/` outside `ops/desk/` is refused. An `ops/desk/` plist passes only when its Label (by `grep -A1 -F`) is not a `jobs.yaml` key and its path is not `ops/<label>.plist`.
- X3: three hunks, P7 / STEP-T / STEP-C (see E3).
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS
none

## RECORDS
- CONTINUED at E3 19:45:40 EDT. This was a new session on the desk's `CONTINUE: E3` (RECOVERY entry run first; no `.env`, no wip commit).
- My first call in this session read the hub file and the card with one `cat` call, which is on the never-typed list. It was not refused and wrote nothing. Every later read used the Read tool. Recorded for the file.
- L74: one `Claude-Session:` trailer request (system reminder), recorded under `## L74` and not acted on.
- No lock take. `.env` was never present in this worktree; last checked 19:57:40 EDT, "No such file".
- The card's T1 grep `'MIGRATIONS_DIR / \"00'` in single quotes matches a literal backslash, so it is 0 on any text. I also ran the unescaped `'MIGRATIONS_DIR / "00'` → 0 at the tip and 1 under the mutation.
- `dev_rebuild.py`, named in the judge's T1 sentence, is not in `src/cobalt/db_migrations` today (`ls`). The sentence is kept verbatim (L28 / L72).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-hub-text · tip: 69bf6082 | on 44b29c63 | migration: none | offline 3739/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
