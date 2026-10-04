# deploy-hub-text — check, pass 1 (re-issue) — 2026-10-03

## §0 Headline
- Check of `deploy-hub-text` at `69bf6082`, pass 1, Opus alone (HOUSE A: none, overruled 2026-10-02 R47). 13 own findings; nothing held, nothing fixed, no commit.
- T1, T6 and C1 are built as the card writes them, and the diff touches only P7, STEP-T and STEP-C (X3).
- X2 is open: STEP-C's judge-dictated sentence lets a resident plist under `ops/desk/` through two ways (O1: jobs.yaml has no label *keys*; O2: a one-line Label defeats `grep -A1`). Both are REJECTED by card T6 and go to the judgment seat.
- Suites stand as built. ready: YES; decisions: 3, for Dejan: 0.

## L74
A system block in this session asked that commits end with a `Claude-Session:` line. Recorded here once and not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 19:59:08 EDT 2026` |
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/02b-deploy-hub-text-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `45181cbaf149e88e09c3f4db9673b882ca7aa279` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (...): APPROVES \`STANDING-LIST.md\` once (\`4be06af0\`); ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 | `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait, ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C ... log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^| R154 " ".../cto-2026-10-02.md"` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no \`src/\`, test, config or migration path takes no dev-DB lock at build + check ... | HIS RULING · APPROVED |` |
| R154 committed | `git -C ... log -1 --format=%H -S"| R154 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, ... | HIS RULING · APPROVED |` |
| R157 committed | `git -C ... log -1 --format=%H -S"| R157 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| HOUSE A overrule | card line 9: `HOUSE A: none — overruled 2026-10-02 R47`; R47 proved above | — | house gates and probe not run (CHECK-HUB `## THE FLOW`, NO OUTSIDE HOUSE) |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| tip | `git log --oneline -1` | 0 | `d2f3156e docs(deploy-hub-text): build report — 69bf6082` |
| docs-only above TIP | `git log --stat --format=%h 69bf6082..HEAD` | 0 | `d2f3156e` · `.../reports/deploy-hub-text-build-2026-10-03.md | 184 +++---` · `1 file changed, 83 insertions(+), 101 deletions(-)` |
| BUILT | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: deploy-hub-text · tip: 69bf6082 | on 44b29c63 | migration: none | offline 3739/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 44b29c63..69bf6082` | 0 | `69bf6082 fix(deploy-hub-text): P7/STEP-T migration = any .sql or a FORWARD entry change; ...` · `59ef8d48 fix(deploy-hub-text): STEP-T reads the merged FORWARD diff; ...` · `696847b1 docs(deploy-hub-text): build report — 50bd02d8` · `50bd02d8 fix(deploy-hub-text): migration = NNNN_*.sql or FORWARD change; ...` (4 commits) |
| range stat | `git log --stat --format=%h 44b29c63..69bf6082` | 0 | 69bf6082: `DEPLOY-HUB.md | 13` · 59ef8d48: `DEPLOY-HUB.md | 4` · 696847b1: `deploy-hub-text-build-2026-10-03.md | 157` · 50bd02d8: `DEPLOY-HUB.md | 13` |
| path union | — | — | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` |
| THE LOCK (DB: none) | `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | 1 | `ls: ...: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames 44b29c63..69bf6082` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` — all under `docs/` |
| `<S>` | `ls <S>` | 0 | `opus-1.md` (19:24, the FIRST build's check; this report is absent, no CONTINUE in the launch: a fresh pass, not RECOVERY; the file is not opened) |
| house | — | — | `house A: none (overruled 2026-10-02 R47)` · house B: as needed |

## Files copied
none (no house).

## OWN FINDINGS
Written before any run below; no house list exists (house A: none, overruled 2026-10-02 R47). `<DH>` = `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` in `<WT>`.

FINDING O1
ROW: T6 / X2
CLAIM: STEP-C (`<DH>:89`) lets an `ops/desk/` plist through when its Label "is not a key of configs/cobalt/jobs.yaml", but `configs/cobalt/jobs.yaml:37-39` holds the labels as list values (`jobs:` → `- label: com.cobalt.aset`), never as keys, so a literal reader finds no label to be a key and a resident's label passes.
RUN: COMMAND `grep -c -F "com.cobalt.aset:" configs/cobalt/jobs.yaml` (the label as a key), beside `grep -c -F "label: com.cobalt.aset" configs/cobalt/jobs.yaml` (the label as a value).
EXPECT: `0` for the key form; `1` for the value form.

FINDING O2
ROW: T6 / X2
CLAIM: STEP-C (`<DH>:89`) reads the Label as "the line after <key>Label</key>, read by grep -A1 -F"; a plist written with key and value on one line (`<key>Label</key><string>…</string>`) gives the NEXT key as the "Label", so a resident label in such a plist is never compared with jobs.yaml.
RUN: COMMAND `grep -A1 -F "<key>Label</key>" <S>/files/oneline-label.plist` on a constructed plist (Label `com.cobalt.aset` on the key's line, `<key>ProgramArguments</key>` on the next).
EXPECT: two lines; the line after the key line is `<key>ProgramArguments</key>`, not the label.

FINDING O3
ROW: T1
CLAIM: the judge's P7 sentence is not in the file at the tip.
RUN: COMMAND `grep -c -F "whatever its name" "<DH>"`
EXPECT (if true): `0`; the row needs `1`.

FINDING O4
ROW: T1
CLAIM: the first build's `[0-9][0-9][0-9][0-9]_*.sql` sentence is still in the file.
RUN: COMMAND `grep -c -F "[0-9][0-9][0-9][0-9]_*.sql" "<DH>"`
EXPECT (if true): above `0`.

FINDING O5
ROW: T1
CLAIM: STEP-T's FORWARD grep still carries the `00` prefix (`<DH>:85`), so an entry numbered 0100 or above is not listed.
RUN: COMMAND `grep -c -F 'MIGRATIONS_DIR / \"00' "<DH>"`
EXPECT (if true): above `0`.

FINDING O6
ROW: T6
CLAIM: the judge's STEP-C sentence is not in the file.
RUN: COMMAND `grep -c -F "anywhere under ops/ is refused" "<DH>"`
EXPECT (if true): `0`.

FINDING O7–O11
ROW: C1
CLAIM: a sentence of the cut T2–T5 is still in the file (one finding per pattern: O7 "trap on every exit", O8 "leftover lock after a FAILED gate", O9 "THE EQUAL-TREE CLAUSE", O10 "The rule for (v) when it lands", O11 "never a resend").
RUN: COMMAND `grep -c -F "<pattern>" "<DH>"`, one call per pattern.
EXPECT (if true): above `0`.

FINDING O12
ROW: C1 / X3
CLAIM: `git diff 44b29c63` of the file touches more than P7, STEP-T and STEP-C.
RUN: COMMAND `git diff 44b29c63 -- "<DH>"`
EXPECT (if true): a hunk whose `-`/`+` lines sit outside the P7 bullet (`<DH>:65`), the STEP-T bullet (`<DH>:85`) and the STEP-C paragraph (`<DH>:89`).

FINDING O13
ROW: T1 / X1
CLAIM: STEP-T's FORWARD grep `grep -n -F 'MIGRATIONS_DIR / "'` (`<DH>:85`) misses an entry of `FORWARD` / `REVERSE` in `src/cobalt/db_migrations/__init__.py:135-180`, or a `.sql` under the folder is not a registered migration (a fixture the new P7 would misread as a migration; card RECORDS, judge finding 2).
RUN: COMMAND `grep -c -F 'MIGRATIONS_DIR / "' src/cobalt/db_migrations/__init__.py`, compared with the count of `.sql` files under `src/cobalt/db_migrations/` (Glob, at the tip).
EXPECT (if true): the two counts differ.

## Findings
none (no house).

## Dropped
none.

## RUNS
All runs in `<WT>` at `d2f3156e` (code tip `69bf6082`), 20:00–20:02 ET.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `grep -c -F "com.cobalt.aset:" configs/cobalt/jobs.yaml` · `grep -c -F "label: com.cobalt.aset" configs/cobalt/jobs.yaml` | `0` · `1` | REJECTED — card T6: the STEP-C sentence ("is not a key of configs/cobalt/jobs.yaml") is the judge's text, verbatim on the row. Red for the stated reason: no label is a key, so read literally the clause never refuses. OPEN |
| O2 | own | `grep -A1 -F "<key>Label</key>" <S>/files/oneline-label.plist` (constructed plist) | `    <key>Label</key><string>com.cobalt.aset</string>` / `    <key>ProgramArguments</key>` | REJECTED — card T6: "the line after <key>Label</key>, read by grep -A1 -F" is the row's verbatim text. Red for the stated reason. Every plist under `ops/` today puts its Label on its own line (`grep -rn -F "<key>Label</key>" ops` → 15 hits, all with the key alone on the line). OPEN |
| O3 | own | `grep -c -F "whatever its name" "<DH>"` | `1` | NOT HELD |
| O4 | own | `grep -c -F "[0-9][0-9][0-9][0-9]_*.sql" "<DH>"` | `0` | NOT HELD |
| O5 | own | `grep -c -F 'MIGRATIONS_DIR / \"00' "<DH>"` | `0` | NOT HELD |
| O6 | own | `grep -c -F "anywhere under ops/ is refused" "<DH>"` | `1` | NOT HELD |
| O7 | own | `grep -c -F "trap on every exit" "<DH>"` | `0` | NOT HELD |
| O8 | own | `grep -c -F "leftover lock after a FAILED gate" "<DH>"` | `0` | NOT HELD |
| O9 | own | `grep -c -F "THE EQUAL-TREE CLAUSE" "<DH>"` | `0` | NOT HELD |
| O10 | own | `grep -c -F "The rule for (v) when it lands" "<DH>"` | `0` | NOT HELD |
| O11 | own | `grep -c -F "never a resend" "<DH>"` | `0` | NOT HELD |
| O12 | own | `git diff 44b29c63..69bf6082 -- "<DH>"` (run during the read in `## 2`; the file is unchanged since, `git log --stat 69bf6082..HEAD` → the build report only) | three hunks: `@@ -62,7 +62,7 @@` changes only the P7 bullet (line 65); `@@ -82,11 +82,11 @@` changes only the STEP-T "After the merges" bullet (line 85) and the STEP-C paragraph (line 89) | NOT HELD |
| O13 | own | `grep -c -F 'MIGRATIONS_DIR / "' src/cobalt/db_migrations/__init__.py` · Glob `src/cobalt/db_migrations/**/*.sql` | `41` · 41 files (`0001_schemas.sql` and 20 forward/rollback pairs, `0002`–`0022`, no `0012`) | NOT HELD: every `.sql` under the folder is a registered entry; no fixture (card RECORDS, judge finding 2, re-read) |

## FIXES
none (nothing held inside the rows; O1, O2 are REJECTED by the row's own text).

## Suites
No commit of mine → `suites: as built (no commit)`. From the build report `## W THE THREE SUITES`: offline `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 573.81s (0:09:33)` · with-DB `not run (DB: none)` · live-note `146 passed, 1 skipped, 15 warnings in 27.65s` (skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`) · tests/ops `564 passed, 1 xfailed, 15 warnings in 239.72s (0:03:59)`. `cobalt_dev: not taken (DB: none — 2 paths)`. RESTARTS (build report): `RESTARTS: none`. `.env`: `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → `No such file or directory` (20:02).

## Scope
Path union `44b29c63..69bf6082`: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (rows T1, T6, C1) and `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` (the build report). No commit of mine. Nothing outside the rows' file.

## Checked against the branch
| item | command | output |
|---|---|---|
| (i) my commits | `git log --oneline 69bf6082..HEAD -- . ":(exclude)docs"` | (nothing) — `<tip now>` = `69bf6082` |
| (ii) non-docs paths | `git log --stat --format=%h 69bf6082..HEAD` (PREFLIGHT) | `d2f3156e` — the build report only |
| (iii) fence | `git log --oneline 44b29c63..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` | (nothing) |
| (iii) fence, any file but DEPLOY-HUB.md | `git log --oneline 44b29c63..HEAD -- . ":(exclude)docs/40 - DevDocs/prompts/DEPLOY-HUB.md" ":(exclude)docs/40 - DevDocs/reports"` | (nothing) |
| (iv) held tests | — | none held |
| (v) `.env` | `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | `No such file or directory` |
| (v) tree | `git status --short --branch` | `## ops/deploy-hub-text-1003` |
| (vi) TREE STATE unchanged | `git log --stat --format=%h 44b29c63..HEAD -- src/cobalt/db_migrations tests/cobalt` | (nothing) |
| (vii) RECORDS | judge finding 2 "no `.sql` test fixture" | re-read by O13: 41 `.sql` = 41 registry entries. The other record lines name no `ls`, `grep` or `git -C` command |
| (viii) L32 | — | this report holds no ticker, price or date of his; `com.cobalt.aset` is a job label |

COUNTING: findings 13 (own 13, house 0) · dropped 0 · held 0 · fixed 0 · held unfixed 0 · open 2 (O1, O2).

## OPEN
- O1 (own, T6 / X2) — REJECTED by card T6. `grep -c -F "com.cobalt.aset:" configs/cobalt/jobs.yaml` → `0`, while `grep -c -F "label: com.cobalt.aset"` → `1`: jobs.yaml holds labels as `label:` values in the `jobs:` list, not as keys. Read literally, STEP-C's "not a key of configs/cobalt/jobs.yaml" is true of every label, so a resident's plist under `ops/desk/` passes. To settle: the judge rewords the clause (for example "is not the `label:` value of an entry in configs/cobalt/jobs.yaml"), or rules that "key" means that.
- O2 (own, T6 / X2) — REJECTED by card T6. `grep -A1 -F "<key>Label</key>"` on a plist with key and value on one line returns the next key as "the line after". To settle: the judge words the read as the Label's `<string>` value, on the key's line or the next, or rules that a one-line Label is refused.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
1. O1 — STEP-C's "not a key of configs/cobalt/jobs.yaml" (card T6, the judge's JUDGE ASK 16 sentence). jobs.yaml holds labels as `label:` values, never keys (`grep -c -F "com.cobalt.aset:"` → 0). Read literally, a resident label in an `ops/desk/` plist passes STEP-C (X2). Safe default taken: nothing changed; the row's text is the judge's and the fix lies in its wording. For the judgment seat: reword T6 (a re-issue row) or rule what "key" means. Not FOR DEJAN.
2. O2 — STEP-C reads the Label as "the line after <key>Label</key>" (grep -A1). A one-line `<key>Label</key><string>…</string>` hands back the next key instead. All 15 plists under `ops/` today use two lines. Safe default taken: nothing changed. For the judgment seat: reword the read, or rule that a one-line Label is refused. Not FOR DEJAN.
3. ASK DESK: `## 8` names `<S>/opus-1.md`, but `<S>` already holds the FIRST check's `opus-1.md` (19:24, never opened by me) [20:02]. Safe default taken: nothing overwritten; my sections are at `<S>/opus-1-r2.md`. House B is `none available` (HOUSE A overruled), so no house reads either file.

## RECORDS
- `house A: none (overruled 2026-10-02 R47)`; no house gate, probe or launch; `## 1` and `## 3` not run; `## Files copied`: none.
- house B: open 2 > 0, card `HOUSE B: as needed`, and HOUSE A is overruled → `none available` (CHECK-HUB `## THE FLOW`, NO OUTSIDE HOUSE). The open items are under `## DECISIONS`.
- `<S>` held `opus-1.md` from the first check at launch; this was not RECOVERY (no `CONTINUE`, and this report did not exist).
- Files written under `<S>`: `files/oneline-label.plist` (constructed, for O2) and `opus-1-r2.md`.
- Reads beyond `## 3` of WHAT YOU READ, done for X2 and named by the T6 sentence: `configs/cobalt/jobs.yaml` (lines 30–44 and one `grep -n -F "com.cobalt."`), and the `<key>Label</key>` line of the `ops/*.plist` files (one `grep -rn -F`). Also `src/cobalt/db_migrations/__init__.py` (one Grep, for X1).
- No dropped finding, no refused command, no CONTINUE message, no lock take.
- L74: one system block asked for a `Claude-Session:` line on commits; recorded under `## L74`, not followed (no commit was made).
- files opened: 25 — CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK` to `## W`); the build report (`## RESTARTS` to `## CONTINUE`, plus its tail); areas/cobalt.md (`## What Cobalt is`, `## Build rules` down); DEPLOY-HUB.md at the tip (lines 1–95); cto-2026-09-30.md (R60 row); cto-2026-10-02.md (R47, R154, R157 rows); configs/cobalt/jobs.yaml; src/cobalt/db_migrations/__init__.py; 15 `ops/*.plist` (the Label line, by one grep).
- Check of `deploy-hub-text`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 69bf6082 · house A: none (overruled 2026-10-02 R47) · findings: 13 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none available · suites: as built (no commit) · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 25 · ready: YES · decisions: 3 · for Dejan: 0
