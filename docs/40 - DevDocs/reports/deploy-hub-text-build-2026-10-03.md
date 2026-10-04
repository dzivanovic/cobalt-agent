# BUILD — deploy-hub-text (card `02b`, re-issue 2), 2026-10-03

The first build's report is at `696847b1` (first build tip `50bd02d8`, check fix `59ef8d48`). Re-issue 1 was built at `69bf6082`; its report is at `d2f3156e`. This file is re-issue 2's report. Re-issue 2 changes only T6 (JUDGE ASK 17, check r2 O1/O2). It resumed at E3 in a new session on the desk's `CONTINUE: E3` (RECOVERY).

## §0 Headline
- Re-issue 2 rewrites one sentence in `DEPLOY-HUB.md` STEP-C, at commit `2cc6330e` (+1 / −1). T1 and C1 are unchanged from `69bf6082`, and check r2 held them as written.
- T6: STEP-C now reads a plist's Label string on its `<key>Label</key>` line or the line after it. It compares that string against the `label:` values in `jobs.yaml`. A Label the read cannot find is refused.
- `git diff 44b29c63` of the file still touches only P7, STEP-T and STEP-C.
- Suites: offline 3739 passed / 0 failed. Live-note 146 / 0. `tests/ops` 564 / 0. DB: none, so no lock was taken. RESTARTS: none. No decisions.

## L74
A system reminder in this session asked for a `Claude-Session:` trailer on commits. It is recorded here once and was not acted on. The commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Re-run at 20:04 EDT for the re-issued card:
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | no hit | nothing |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../2026-10-03/02b-deploy-hub-text-card.md"` | no hit | nothing |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `48b37d67555f4152509cb73fd29a131f74e1244d` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | nothing |
| R47 | `grep -n "^\| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; …) … \| HIS RULING · APPROVED \|` |
| R154 | `grep -n "^\| R154 " …` | 0 | `161:\| R154 \| 17:29 ET \| HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock … \| HIS RULING · APPROVED \|` |
| R157 | `grep -n "^\| R157 " …` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): … \| HIS RULING · APPROVED \|` |
| R157 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R157 \|" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
R60, plus the commits for R47 and R154: proven in the first build's AUTHORIZATION table (at `696847b1`). The rows are unchanged.

## PREFLIGHT
RECOVERY entry, in order:
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| head | `git log --oneline -3` | 0 | `d2f3156e docs(deploy-hub-text): build report — 69bf6082` · `69bf6082 fix(deploy-hub-text): P7/STEP-T …` · `59ef8d48 fix(deploy-hub-text): …` |
| no .env | `ls -la /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | 1 | `No such file or directory` |
| clock | `date` | 0 | `Sat Oct  3 20:04:02 EDT 2026` |
| the T6 sentence before the edit | Read `DEPLOY-HUB.md` line 89 | — | `… except one under ops/desk/ whose Label (the line after <key>Label</key>, read by grep -A1 -F) is not a key of configs/cobalt/jobs.yaml and whose path is not ops/<label>.plist. A refused plist → …` |
| jobs.yaml shape | `grep -n -F "label:" configs/cobalt/jobs.yaml` | 0 | 15 entries `  - label: com.cobalt.<name>` (lines 39 … 289). The labels are `label:` values, as the T6 sentence reads them. |

Card `## RECORDS`, copied (the desk's facts):
- Judge, 10-03 20:04 (JUDGE ASK 17, check r2 O1/O2 HOLD): T6 as checked in r2 O1/O2. Labels are `label:` values in jobs.yaml. The Label string is read on its key line or the next. An unreadable Label is refused.
- Check r2 at `69bf6082`: T1 and C1 as written, the diff limited to P7, STEP-T and STEP-C. Only T6 changes in this re-issue. Re-read below: the diff hunks are still those three.
- Judge, 10-03 ~19:50 (JUDGE ASK 16): Grok's 8 findings were answered. T2–T5 are carried to 03d.
- Judge (finding 2): no `.sql` test fixture exists under `src/cobalt/db_migrations/`. Re-read by the previous session's `ls`.
- Judge, 10-03 19:12 (JUDGE ASK 15): ADDED or MODIFIED is kept. The wording is superseded.
- The first build `50bd02d8` was checked ready YES at `59ef8d48`.
- The card ships alone and docs-only. Its other-house read is Grok after the check.
- The `03c` chain (`9694a679`) is ported later by `03d`.

## E0 BASELINE
Not re-run: the re-issue resumes at E3. The first build's E0 on `44b29c63`: offline `3739 passed, 745 skipped, 1 xfailed`, live-note `146 passed, 1 skipped` (report at `696847b1`).

## E2 RED
Not re-run: the re-issue resumes at E3. T6's red is a grep on the hub text. At `d2f3156e` (before the edit), `a Label the read cannot find is refused` was absent and `is not a key of configs` was present. The mutation below shows both going red again.

## E3 THE ROWS
- **T6** STEP-C (line 89): the r2 clause was replaced with the card's sentence, verbatim: "… except one under ops/desk/ whose Label string (the <string> value on the <key>Label</key> line or the line after it) is not the label: value of any entry in configs/cobalt/jobs.yaml and whose path is not ops/<label>.plist; a Label the read cannot find is refused." The rest of STEP-C reads as at `69bf6082`.
- **T1**, **C1**: no edit in this re-issue. Their greens were re-run at the tip (table).

Greens at `2cc6330e` (each its own `grep -c -F` on the file):
| row | pattern | count | want |
|---|---|---|---|
| T6 | `a Label the read cannot find is refused` | 1 | 1 |
| T6 | `is not a key of configs` | 0 | 0 |
| T1 | `whatever its name` | 1 | 1 |
| T1 | `[0-9][0-9][0-9][0-9]_*.sql` | 0 | 0 |
| T1 | `MIGRATIONS_DIR / \"00` | 0 | 0 |
| C1 | `trap on every exit` | 0 | 0 |
| C1 | `leftover lock after a FAILED gate` | 0 | 0 |
| C1 | `THE EQUAL-TREE CLAUSE` | 0 | 0 |
| C1 | `The rule for (v) when it lands` | 0 | 0 |
| C1 | `never a resend` | 0 | 0 |

THE MUTATION (Edit tool): the r2 clause was put back in place of the fix.
| row | mutation | grep under mutation |
|---|---|---|
| T6 | the r2 clause "whose Label (the line after <key>Label</key>, read by grep -A1 -F) is not a key of configs/cobalt/jobs.yaml … .plist." restored | `a Label the read cannot find is refused` → `0` (needs 1); `is not a key of configs` → `1` (needs 0) |

The mutation was undone with the Edit tool. Afterwards: `a Label the read cannot find is refused` → 1, `is not a key of configs` → 0. `git diff --stat` showed only the T6 line (+1/−1) and the report's last line.

X3: `git diff 44b29c63 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` has three hunks: P7 (line 65), STEP-T (line 85) and STEP-C (line 89). `git diff --stat 44b29c63 -- <file>` → `6 +++---`, `1 file changed, 3 insertions(+), 3 deletions(-)`.

DevDocs line: no page for `DEPLOY-HUB.md` exists under `docs/40 - DevDocs/cobalt/`, and no module changed, so no line was written.

Commit `2cc6330e fix(deploy-hub-text): STEP-C reads the Label string on its key line or the next, against jobs.yaml label: values; an unreadable Label is refused (T6, L67, L72)`.

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
`<tip>` = `2cc6330e`.
- (a0) `git diff --name-only --no-renames 44b29c63` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` (the whole output). Every path starts with `docs/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 571.81s (0:09:31)`, exit 0. This build adds no test.
- (e) `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → "No such file". `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 27.81s`. Skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `564 passed, 1 xfailed, 15 warnings in 239.22s (0:03:59)`, exit 0.
- (b)–(d), (f): not run (DB: none).

## PRE-STOP SELF-CHECK
1. T6's two greps were red under the E3 mutation (`0` and `1`) and are green at the tip. T1's and C1's greps were shown red under their mutations at `69bf6082` (report `d2f3156e`) and are green at the tip (table).
2. A hub-text row has no code callers. STEP-C (line 89) is the only plist check, and it carries the new sentence. Its three parts are: (i) a path outside `ops/desk/` is refused; (ii) an `ops/desk/` Label equal to a `jobs.yaml` `label:` value, or a path `ops/<label>.plist`, is refused; (iii) a Label the read cannot find is refused. The `jobs.yaml` `label:` shape was re-read at PREFLIGHT.
3. Line numbers and quotes were re-read at `2cc6330e`: `grep -n -F "a Label the read cannot find is refused"` → `89:`; `grep -n -F "P7 THE MIGRATIONS"` → `65:`; `git show --stat 2cc6330e` → `DEPLOY-HUB.md | 2 +-`; `git log --oneline 44b29c63..HEAD` → six commits, `2cc6330e` on top.

## FOR THE CHECK
- Range `44b29c63..2cc6330e`. Commits: `50bd02d8 fix(deploy-hub-text): migration = NNNN_*.sql or FORWARD change; ops/desk plist passes STEP-C; Grok findings 1-5 sentences (T1-T6, L42, L67, L72)` · `696847b1 docs(deploy-hub-text): build report — 50bd02d8` · `59ef8d48 fix(deploy-hub-text): STEP-T reads the merged FORWARD diff; an ops/desk plist with a registry label is refused (check O1, O2)` · `69bf6082 fix(deploy-hub-text): P7/STEP-T migration = any .sql or a FORWARD entry change; STEP-C refuses every ops/ plist but a non-resident ops/desk/ one; T2-T5 sentences cut (T1, T6, C1, L42, L67, L72)` · `d2f3156e docs(deploy-hub-text): build report — 69bf6082` · `2cc6330e fix(deploy-hub-text): STEP-C reads the Label string on its key line or the next, against jobs.yaml label: values; an unreadable Label is refused (T6, L67, L72)`. Re-issue 2's own range is `d2f3156e..2cc6330e`.
- Reds, mutations and greens: the E3 tables above.
- Caller greps: none apply (a hub-text row).
- RUN rows: none.
- Suites: offline `3739 passed, 745 skipped, 1 xfailed` · with-DB `not run (DB: none)` · live-note `146 passed, 1 skipped` · tests/ops `564 passed, 1 xfailed`. The commands are quoted under W.
- `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock take and release: not run (DB: none).
- RESTARTS table: under `## RESTARTS`.
- X2: a plist added or modified anywhere under `ops/` outside `ops/desk/` is refused. An `ops/desk/` plist is refused when any of these holds:
  - its Label string (on the `<key>Label</key>` line or the next) equals any `jobs.yaml` `label:` value;
  - its path is `ops/<label>.plist`;
  - the read cannot find its Label.
- X1, X3: unchanged from check r2. The diff still has three hunks (E3).
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — BUILT

## DECISIONS
none

## RECORDS
- CONTINUED at E3 20:04:02 EDT. This was a new session on the desk's `CONTINUE: E3` for re-issue 2 (JUDGE ASK 17). The RECOVERY entry ran first: no `.env`, no wip commit. The report's previous last line (re-issue 1's `BUILT` line) was replaced with `RESUMED: E3 20:04:02 EDT` before any other report write.
- L74: one `Claude-Session:` trailer request (system reminder), recorded under `## L74` and not acted on.
- No lock take. `.env` was never present in this worktree; last checked 20:14:36 EDT, "No such file".
- The offline and `tests/ops` suites ran at the same time in the background. Both exited 0.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: deploy-hub-text · tip: 2cc6330e | on 44b29c63 | migration: none | offline 3739/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
