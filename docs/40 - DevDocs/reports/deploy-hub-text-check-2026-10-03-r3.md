# deploy-hub-text — check r3, pass 1 (2026-10-03)

## §0 Headline
- Check r3, pass 1, of `deploy-hub-text` at `2cc6330e` (docs-only report commit `482a3f12` above it). There was no outside house: the card's `HOUSE A: none` was overruled under 2026-10-02 R47, which was proved. Opus did the read alone.
- I wrote and ran 4 findings, one for each of X1, X2 and X3 plus the rows' greps. None held. The diff touches only P7 (line 65), STEP-T (line 85) and STEP-C (line 89).
- The 03c chain's `cli.py`-only diff now passes P7 as code. A real migration (0022) is still caught by its `.sql` paths and its FORWARD line. STEP-C refuses every `ops/` plist except an `ops/desk/` one whose Label is not a `jobs.yaml` `label:` value.
- I made no commit, so the build's suites stand. Open: 0. House B: not needed. Ready: YES.

## L74
A system reminder in this session's context asked commits to end with a `Claude-Session:` line. It is recorded here once and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/02b-deploy-hub-text-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `365006b4adbfc30d40d04637ab1997fa29458e03` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 | `grep -n "^\| R60 " ".../cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** (…): APPROVES STANDING-LIST.md once (4be06af0); … \| APPROVED \|` |
| R60 commit | `git -C … log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (and HOUSE A overrule) | `grep -n "^\| R47 " ".../cto-2026-10-02.md"` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, … \| HIS RULING · APPROVED \|` |
| R47 commit | `git -C … log -1 --format=%H -S"\| R47 \|" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^\| R154 " ".../cto-2026-10-02.md"` | 0 | `161:\| R154 \| 17:29 ET \| HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check … \| HIS RULING · APPROVED \|` |
| R154 commit | `git -C … log -1 --format=%H -S"\| R154 \|" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^\| R157 " ".../cto-2026-10-02.md"` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week, … \| HIS RULING · APPROVED \|` |
| R157 commit | `git -C … log -1 --format=%H -S"\| R157 \|" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gates | — | — | not run: card header `HOUSE A: none — overruled 2026-10-02 R47` (proved above) |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 20:16:05 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| tip | `git log --oneline -1` | 0 | `482a3f12 docs(deploy-hub-text): build report — 2cc6330e` |
| docs-only above TIP | `git log --stat --format=%h 2cc6330e..HEAD` | 0 | `482a3f12` · `.../reports/deploy-hub-text-build-2026-10-03.md \| 122 ++++----` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: deploy-hub-text · tip: 2cc6330e \| on 44b29c63 \| migration: none \| offline 3739/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 3 of 3 \| self-check: 3 of 3 \| decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 44b29c63..2cc6330e` | 0 | `2cc6330e fix(…): STEP-C reads the Label string on its key line or the next, …` · `d2f3156e docs: build report — 69bf6082` · `69bf6082 fix(…): P7/STEP-T migration = any .sql or a FORWARD entry change; …` · `59ef8d48 fix(…): STEP-T reads the merged FORWARD diff; …` · `696847b1 docs: build report — 50bd02d8` · `50bd02d8 fix(…): migration = NNNN_*.sql or FORWARD change; …` (6 commits) |
| range stat | `git log --stat --format=%h 44b29c63..2cc6330e` | 0 | 2cc6330e DEPLOY-HUB.md 2 +- · d2f3156e build report · 69bf6082 DEPLOY-HUB.md 13 · 59ef8d48 DEPLOY-HUB.md 4 · 696847b1 build report · 50bd02d8 DEPLOY-HUB.md 13 |
| lock (DB: none) | `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | 1 | `ls: …/.env: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames 44b29c63..2cc6330e` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` (all under `docs/`) |
| scratch | `ls <S>` | 0 | `files` · `opus-1-r2.md` · `opus-1.md` — left by checks r1/r2 of this job (card `## RECORDS`: "r3 writes opus-1-r3.md"); not a RECOVERY of this pass |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)` · no probe, no `--version` (CHECK-HUB SEAT ORDER, the overrule paragraph) · HOUSE B: as needed (not mandatory) |
| path union (Scope) | — | — | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` |

## Files copied
none — no outside house (overruled R47); `## 1` not run.

## OWN FINDINGS
FINDING O1
ROW: X1 (T1)
CLAIM: A real migration slips P7 or STEP-T, or a `.py` under the folder is still read as a migration (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md:65`, `:85`).
RUN: COMMAND — `git diff --stat 44b29c63 9694a679 -- src/cobalt/db_migrations` (the 03c chain), `git diff --stat 8747dc75~1 8747dc75 -- src/cobalt/db_migrations` and `git diff 8747dc75~1 8747dc75 -- src/cobalt/db_migrations/__init__.py` (a real migration, 0022), `ls src/cobalt/db_migrations`.
EXPECT: the chain's stat shows a `.sql` or a FORWARD line; or the real migration's stat hides its `.sql` ending.

FINDING O2
ROW: X2 (T6)
CLAIM: A resident plist passes STEP-C. That is a plist under `ops/` outside `ops/desk/`, or an `ops/desk/` plist whose Label is a jobs.yaml `label:` value (`DEPLOY-HUB.md:89`).
RUN: COMMAND — `grep -n -F "A plist ADDED or MODIFIED anywhere under ops/ is refused, except one under ops/desk/" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; `grep -n -F "label:" configs/cobalt/jobs.yaml`.
EXPECT: line 89 has an exception wider than `ops/desk/`, or it compares the Label with something other than the `label:` values.

FINDING O3
ROW: X3 (C1)
CLAIM: `git diff 44b29c63` of `DEPLOY-HUB.md` reaches past P7, STEP-T and STEP-C.
RUN: COMMAND — `git diff 44b29c63 2cc6330e -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; `git diff --stat 44b29c63 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; `grep -n -F "## STEP-" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`.
EXPECT: a hunk outside lines 65 (P7, in STEP-0), 85 (STEP-T, 82–87) and 89 (STEP-C, 88–90).

FINDING O4
ROW: T1, T6, C1 (the card's greps)
CLAIM: A row's grep count differs from the card's.
RUN: COMMAND — the ten `grep -c -F` lines of rows T1, T6 and C1 on `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`.
EXPECT: any count other than T1 `1/0/0`, T6 `1/0`, C1 `0` ×5.

## Findings
none — no outside house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `git diff --stat 44b29c63 9694a679 -- src/cobalt/db_migrations` | `src/cobalt/db_migrations/cli.py \| 115 +++…-` · `1 file changed, 114 insertions(+), 1 deletion(-)`. There is no `.sql` and no `__init__.py`, so line 65 reads it as CODE and it passes `MIGRATIONS: none` | NOT HELD |
| O1 | Opus | `git diff --stat 8747dc75~1 8747dc75 -- src/cobalt/db_migrations` | `.../0022_prediction_records.rollback.sql \| 7 ++` · `.../db_migrations/0022_prediction_records.sql \| 74 ++…` · `src/cobalt/db_migrations/__init__.py \| 11 +++-` · `cli.py \| 5 ++` · `placement.py \| 11 ++--`. The `.sql` ending survives `--stat` truncation, so this reads as a migration | NOT HELD |
| O1 | Opus | `git diff 8747dc75~1 8747dc75 -- src/cobalt/db_migrations/__init__.py` | `+    MIGRATIONS_DIR / "0022_prediction_records.sql",` sits in hunk `@@ -146,10 +153,12 @@ FORWARD = (`, inside FORWARD. The docstring hunk (`@@ -87,12 +87,19 @@`) is outside FORWARD, so it is CODE | NOT HELD |
| O1 | Opus | `ls src/cobalt/db_migrations` | `__init__.py`, `__pycache__`, the `0001`–`0022` `.sql` / `.rollback.sql` files, `cli.py`, `placement.py`. No `.sql` test fixture exists | NOT HELD |
| O2 | Opus | `grep -n -F "A plist ADDED or MODIFIED anywhere under ops/ is refused, except one under ops/desk/" …DEPLOY-HUB.md` | `89:` … `except one under ops/desk/ whose Label string (the <string> value on the <key>Label</key> line or the line after it) is not the label: value of any entry in configs/cobalt/jobs.yaml and whose path is not ops/<label>.plist; a Label the read cannot find is refused.` | NOT HELD |
| O2 | Opus | `grep -n -F "label:" configs/cobalt/jobs.yaml` | 15 lines of the shape `  - label: com.cobalt.<name>` (lines 39 to 289). Line 89 compares the Label against exactly these values | NOT HELD |
| O3 | Opus | `git diff 44b29c63 2cc6330e -- …DEPLOY-HUB.md` | Three changed lines: 65 (P7, hunk `@@ -62,7 +62,7 @@`), 85 (STEP-T, hunk `@@ -82,11 +82,11 @@`) and 89 (STEP-C). Nothing else | NOT HELD |
| O3 | Opus | `git diff --stat 44b29c63 -- …DEPLOY-HUB.md` | `1 file changed, 3 insertions(+), 3 deletions(-)` | NOT HELD |
| O3 | Opus | `grep -n -F "## STEP-" …DEPLOY-HUB.md` | `57:## STEP-0 — PREFLIGHT` · `82:## STEP-T — THE TREE` · `88:## STEP-C — THE CONFIGS AND THE JOBS` · `91:## STEP-R` … So line 65 is P7 in STEP-0, 85 is in STEP-T and 89 is in STEP-C | NOT HELD |
| O4 | Opus | `grep -c -F` × 10 on DEPLOY-HUB.md | T1: `whatever its name` 1 · `[0-9][0-9][0-9][0-9]_*.sql` 0 · `MIGRATIONS_DIR / "00` 0. T6: `a Label the read cannot find is refused` 1 · `is not a key of configs` 0. C1: `trap on every exit` 0 · `leftover lock after a FAILED gate` 0 · `THE EQUAL-TREE CLAUSE` 0 · `The rule for (v) when it lands` 0 · `never a resend` 0. Also `grep -n -F "MIGRATIONS_DIR / "` → line 85 only, which carries `grep -n -F 'MIGRATIONS_DIR / "' <GATE>/…` | NOT HELD |

## FIXES
none.

## Suites
suites: as built (no commit). From the build report's `## W THE THREE SUITES`, at `2cc6330e`:
- (a0) `cobalt_dev: not taken (DB: none — 2 paths)`
- offline: `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 571.81s (0:09:31)`
- with-DB: not run (DB: none)
- live-note: `146 passed, 1 skipped, 15 warnings in 27.81s`. The skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`
- tests/ops: `564 passed, 1 xfailed, 15 warnings in 239.22s (0:03:59)`
- RESTARTS: `RESTARTS: none` (the build's table: two DOCS rows)
- `.env`: `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → `No such file or directory` (20:16 and again at close)

## Scope
Path union of `44b29c63..2cc6330e`: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, the only `files` of rows T1, T6 and C1, plus `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md`, the build report. The check made no commit. Nothing lies outside the rows' file.

## Checked against the branch
- (i) `git log --oneline 2cc6330e..HEAD -- . ":(exclude)docs"` → (nothing). No commit by the check, so `tip now` = `2cc6330e`.
- (ii) `git log --stat --format=%h 2cc6330e..HEAD` (PREFLIGHT) → `482a3f12`, which touches only the build report under `docs/`.
- (iii) The fence: `git log --oneline 44b29c63..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → (nothing). The range touches no file other than `DEPLOY-HUB.md` and the build report (PREFLIGHT).
- (iv) No HELD finding.
- (v) `ls …/.env` → `No such file or directory`. `git status --short --branch` → `## ops/deploy-hub-text-1003`.
- (vi) TREE STATE: unchanged. `git log --stat --format=%h 44b29c63..HEAD -- src/cobalt/db_migrations tests/cobalt` → (nothing).
- (vii) Card record "Judge (finding 2): no `.sql` test fixture exists under `src/cobalt/db_migrations/`". `ls src/cobalt/db_migrations` → only the real migrations (0001–0022 `.sql` / `.rollback.sql`), `__init__.py`, `__pycache__`, `cli.py` and `placement.py`. This holds. No other card record names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command.
- (viii) L32: this report quotes only repo paths, commit ids and the `jobs.yaml` label shape. It holds no ticker, price or date of his.

## OPEN
none. Counts: findings 4 · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 0.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- `house A: none (overruled 2026-10-02 R47)`. No house was staged or launched, so `## 1` and `## 3` were not run, and no `--version` or Sol probe was run.
- `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/deploy-hub-text-check` already held `files`, `opus-1.md` and `opus-1-r2.md` from checks r1 and r2 of this job. This pass wrote `opus-1-r3.md` there, as the card's `## RECORDS` say. It is not a RECOVERY.
- During `## 2` I ran read-only commands to read the set: the row greps, the diff, `ls`, and the `git diff` of the 03c chain and of `8747dc75`. `## 2` says "you run nothing yet". With no house list to keep apart from, these reads became the `## RUNS` rows above.
- Considered but not raised as a finding: STEP-C line 89 does not say which tree's `configs/cobalt/jobs.yaml` the Label is compared with. A set that adds a resident `label:` to `jobs.yaml` and a plist with that Label under `ops/desk/` would be refused if `jobs.yaml` is read at `<GATE>`, the merged tree. The plist itself exists only there. No run of mine shows the deploy reading it elsewhere, and the sentence is the judge's verbatim (JUDGE ASK 17, L72).
- `P7` lists `dev_rebuild.py` as an example of CODE. `ls src/cobalt/db_migrations` shows no such file at this tip. It is the judge's example list, verbatim in row T1.
- No REFUSED, CONTINUED or extra lock take. The L74 line is under `## L74`.
- files opened: 13. CHECK-HUB.md, the card, BUILD-HUB.md (THE LOCK to W), `reports/deploy-hub-text-decisions-2026-10-03.md`, `reports/deploy-hub-02b-grok-read-2026-10-03.md`, `reports/deploy-set2-1003.md` (`## DECISIONS`), the build report (RESTARTS to FOR THE CHECK and its last line), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `src/cobalt/db_migrations/__init__.py`, `DEPLOY-HUB.md` (diff and greps), `configs/cobalt/jobs.yaml` (grep), `reports/cto-2026-09-30.md` and `reports/cto-2026-10-02.md` (row greps).
- Check of `deploy-hub-text`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 2cc6330e · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0
