# deploy-hub-text — check, pass 1 (2026-10-03)

## §0 Headline
- I checked this alone: house A is none, overruled by 2026-10-02 R47. The build is six rows in `DEPLOY-HUB.md`, one commit, `50bd02d8`.
- I wrote 5 findings and 3 held. O1: STEP-T named no command to read a merged `FORWARD` change. O2: STEP-C passed an `ops/desk/` plist even when its label is in the registry. Both are fixed in `59ef8d48`, a 2-line change to the same file. O5: the build's T6 grep was spelled lowercase and could never turn green. The sentence it checks is in the file, so no file changed.
- X1: no migration slips past T1's pattern. X2: T2, T3 and T5 port as copies. T4 also needs the chain's STEP-R re-read changed at the `03d` port, which is out of scope here (O4).
- Suites on `59ef8d48`: offline 3739/0, live-note 146/0, tests/ops 564/0. With-DB not run (DB: none). RESTARTS: none. `.env` absent.
- Nothing is open, so house B is not needed. ready: YES · decisions: 0.

## L74
One block asked for a `Claude-Session:` trailer on commits: a system reminder at the start of this session, after the launch message. I recorded it here once and did not act on it. The commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/02b-deploy-hub-text-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `3887fc68975fca7166045afe56ca0ab8ad71f944` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| standing list | `grep -n "^\| R60 " ".../cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... \| APPROVED \|` |
| standing list commit | `git -C ... log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (and HOUSE A overrule) | `grep -n "^\| R47 " ".../cto-2026-10-02.md"` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait ... \| HIS RULING · APPROVED \|` |
| R47 commit | `git -C ... log -1 --format=%H -S"\| R47 \|" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^\| R154 " ".../cto-2026-10-02.md"` | 0 | `161:\| R154 \| 17:29 ET \| HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock at build + check ... \| HIS RULING · APPROVED \|` |
| R154 commit | `git -C ... log -1 --format=%H -S"\| R154 \|" ...` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^\| R157 " ".../cto-2026-10-02.md"` | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week ... \| HIS RULING · APPROVED \|` |
| R157 commit | `git -C ... log -1 --format=%H -S"\| R157 \|" ...` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gate R17 | `grep -n "^\| R17 " ".../cto-2026-09-24.md"` | 0 | `35:\| R17 \| 07:32 ET \| ... STANDING: Bash(grok *) is a PRE-APPROVED string ...` |
| house gate R19 | `grep -n "^\| R19 " ".../cto-2026-09-24.md"` | 0 | `37:\| R19 \| 07:36 ET \| ... STANDING: the four house strings are pre-approved ...` |
| R19 commit | `git -C ... log -1 --format=%H -S"\| R19 \|" ...` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 19:11:17 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| tip | `git log --oneline -1` | 0 | `696847b1 docs(deploy-hub-text): build report — 50bd02d8` |
| docs-only above tip | `git log --stat --format=%h 50bd02d8..HEAD` | 0 | `696847b1` · `.../reports/deploy-hub-text-build-2026-10-03.md \| 157 +++` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: deploy-hub-text · tip: 50bd02d8 \| on 44b29c63 \| migration: none \| offline 3739/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 6 of 6 \| self-check: 3 of 3 \| decisions: 1 · for Dejan: 0` |
| range | `git log --oneline 44b29c63..50bd02d8` | 0 | `50bd02d8 fix(deploy-hub-text): migration = NNNN_*.sql or FORWARD change; ops/desk plist passes STEP-C; Grok findings 1-5 sentences (T1-T6, L42, L67, L72)` (1 commit) |
| range stat | `git log --stat --format=%h 44b29c63..50bd02d8` | 0 | `50bd02d8` · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md \| 13 +++++++------` · `1 file changed, 7 insertions(+), 6 deletions(-)` |
| DB: none — paths | `git diff --name-only --no-renames 44b29c63..50bd02d8` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (all under docs/) |
| lock | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env: No such file or directory` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house | — | — | house A: none (overruled 2026-10-02 R47) — no house gate run at launch, no probe (CHECK-HUB "NO OUTSIDE HOUSE") |
| mandatory | card `HOUSE B: as needed` | — | not mandatory |

Path union for `## Scope`: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`.

## Files copied
none — house A: none (overruled 2026-10-02 R47); `## 1` not run.

## OWN FINDINGS
Read: the card; R47, R154, R157 (above); the diff `44b29c63..50bd02d8`; `DEPLOY-HUB.md` at the tip; `src/cobalt/db_migrations/__init__.py` (lines 120–184) and the folder listing; the build report; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the chain's text by `git diff 50bd02d8 9694a679 -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (saved tool output, read by Grep / Read).

FINDING O1
ROW: T1
CLAIM: STEP-T (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md:85`) counts `__init__.py` as a migration path "only when its `FORWARD` registry changed", but names no command that reads the merged tree's `__init__.py` diff; P7 (`:65`) names one for each head. With `__init__.py` in the STEP-T stat, the deploy has no listed step that proves the registry is unchanged (L35, L1).
RUN: COMMAND `grep -c -F "diff <m0> <BRANCH> -- src/cobalt/db_migrations/__init__.py" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `0`

FINDING O2
ROW: T6
CLAIM: STEP-C (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md:89`) says a plist added under `ops/desk/` "passes" with no condition, then says STEP-C refuses a plist under `ops/` whose label is in `configs/cobalt/jobs.yaml`. A plist added at `ops/desk/` that carries a registry label matches both sentences. The card's T6 governs by "refuses only … whose label is in `configs/cobalt/jobs.yaml`", so the pass sentence needs that exception.
RUN: COMMAND `grep -c -F "it passes unless its label is in" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `0` (the pass sentence carries no registry-label exception)

FINDING O3
ROW: X1
CLAIM: a real migration can slip past T1's pattern: a `.sql` in `src/cobalt/db_migrations/` not named `NNNN_*.sql`, or a registry outside `__init__.py`.
RUN: COMMAND `ls src/cobalt/db_migrations` and `grep -n -F "from . import FORWARD, REVERSE" src/cobalt/db_migrations/cli.py`
EXPECT: a `.sql` not matching `[0-9][0-9][0-9][0-9]_*.sql`, or a second registry source.

FINDING O4
ROW: X2
CLAIM: T4's sentence (`docs/40 - DevDocs/prompts/DEPLOY-HUB.md:59`, "(v) is re-read at STEP-R with `date` then") differs from the chain's STEP-R re-read at `9694a679`, which judges a non-empty set "at P1's `date`" and fails.
RUN: COMMAND `grep -n -F "P1 (v) RE-READ" <the saved git diff 50bd02d8 9694a679 output>`
EXPECT: the chain's line, with "at P1's `date`" and `FAILED: STEP-R — window (v) does not hold`.

FINDING O5
ROW: T6 (a report claim, `## W` item (3) of the HOUSE TEXT)
CLAIM: the build report's T6 red-first command, `grep -c -F "a plist added under"` (`docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md:76`), still prints `0` at the tip: the sentence starts with a capital `A`. The report's "Green: one hit, `89:`" (`:86`) is not the output of that command.
RUN: COMMAND `grep -c -F "a plist added under" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `0` at the tip.

## Findings
none — no house.

## Dropped
none

## RUNS
All runs on `50bd02d8` (the tree clean at `696847b1`, a docs-only report commit above it), cwd `<WT>`.
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -c -F "diff <m0> <BRANCH> -- src/cobalt/db_migrations/__init__.py" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `0` | HELD — STEP-T names no command for the merged `__init__.py` diff |
| O2 | Opus | `grep -c -F "it passes unless its label is in" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; context `grep -n -F "it passes (deploy set 2b" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `0`; `89:… classes it as an operator script; it passes (deploy set 2b FAILED STEP-C on card \`05\`'s plist). STEP-C refuses only a plist under \`ops/\` ADDED or MODIFIED whose label is in \`configs/cobalt/jobs.yaml\` or whose path is \`ops/<label>.plist\` …` | HELD — the pass sentence is unconditional, the refusal sentence covers the same plist |
| O3 | Opus | `ls src/cobalt/db_migrations`; `grep -n -F "from . import FORWARD, REVERSE" src/cobalt/db_migrations/cli.py`; `grep -rn -F "import FORWARD" src/cobalt` | every `.sql` is `NNNN_*.sql` or `NNNN_*.rollback.sql` (0001–0022, no 0012), plus `__init__.py`, `__pycache__`, `cli.py`, `placement.py`; `82:from . import FORWARD, REVERSE`; only `src/cobalt/db_migrations/cli.py:82:from . import FORWARD, REVERSE` | NOT HELD — the migrate CLI runs only what `FORWARD` / `REVERSE` in `__init__.py` name, so a non-`NNNN` `.sql` runs only through a `FORWARD` change, which P7 counts. A `REVERSE`-only change passes as CODE by the card's T1 definition (the build's X1 note) |
| O4 | Opus | `grep -n -F "P1 (v) RE-READ" <saved output of git diff 50bd02d8 9694a679 -- DEPLOY-HUB.md>` | `86:+- P1 (v) RE-READ: when P1 named \`(v) provisional\`, the derived \`<restart set>\` is read against it now: a non-empty set outside (i)–(iv) at P1's \`date\` → … \`FAILED: STEP-R — window (v) does not hold: <labels> · rollback: not used\`; an empty set → record \`window: (v) holds\`.` | REJECTED — card T4 gives the sentence word for word, and card `## RECORDS` puts the chain's text in the `03d` port: OUT OF SCOPE |
| O5 | Opus | `grep -c -F "a plist added under" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; `grep -c -F "A plist added under" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `0`; `1` | HELD — the build's T6 grep never turns green; the row's sentence is there under its own spelling. At BASE the phrase appears only on a `+` line of `git diff 44b29c63..50bd02d8` (red), at the tip `1` (green) |

No test file was written (every held finding is a COMMAND on the hub text), so there is no `wip(deploy-hub-text): check red` commit.

## FIXES
| id | change | proof after | commit |
|---|---|---|---|
| O1 | STEP-T (`DEPLOY-HUB.md:85`) gains, after "any other path under that folder is CODE and passes;": "when `__init__.py` is in that stat, `git -C /Users/cobalt/cobalt diff <m0> <BRANCH> -- src/cobalt/db_migrations/__init__.py` → a changed line inside `FORWARD = (…)` is a migration and names only the card's files;" (P7's own words, for the merged tree; `git -C * diff*` is on the deploy line) | O1 grep → `1`; T1's pattern grep → `2` (unchanged) | `59ef8d48` |
| O2 | STEP-C (`DEPLOY-HUB.md:89`): "it passes (deploy set 2b …" → "it passes unless its label is in `configs/cobalt/jobs.yaml` (deploy set 2b …" | O2 grep → `1`; `grep -c -F "A plist added under"` → `1` | `59ef8d48` |
| O5 | no file change: the row's text is right; the proof is re-run here with the sentence's spelling (red at BASE, `1` at the tip) | as in `## RUNS` | none |

`git diff --stat` before the commit: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 4 ++--`. Commit: `[ops/deploy-hub-text-1003 59ef8d48] fix(deploy-hub-text): STEP-T reads the merged FORWARD diff; an ops/desk plist with a registry label is refused (check O1, O2)` · `1 file changed, 2 insertions(+), 2 deletions(-)`. DevDocs line: no page for `DEPLOY-HUB.md` exists under `docs/40 - DevDocs/cobalt/` (the build report's Glob); no module changed, so none written.

## Suites
On `59ef8d48`. This is a DB: none card, so W runs as `BUILD-HUB.md` gives it: (a0), (a), (e) and tests/ops.
- RESTARTS: `uv run cobalt jobs restarts 44b29c63..HEAD` → `path	change	rule	restart` · `docs/40 - DevDocs/prompts/DEPLOY-HUB.md	M	DOCS	-` · `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md	A	DOCS	-` · `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames 44b29c63` → `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` (all under `docs/`). **`cobalt_dev: not taken (DB: none — 2 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 572.18s (0:09:32)`, exit 0.
- (e) `ls <WT>/.env` → "No such file" · `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.56s`. The one skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `564 passed, 1 xfailed, 15 warnings in 237.73s (0:03:57)`, exit 0.
- (b)–(d), (f): not run (DB: none, R154). `.env`: `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → `No such file or directory` (19:24:40 EDT).

## Scope
The paths changed across PREFLIGHT's range and my commit: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (`50bd02d8`, `59ef8d48`). Every row names that file, and nothing else in the change is outside it. The build report `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` (`696847b1`) is the build's report.

## Checked against the branch
- (i) `git log --oneline 50bd02d8..HEAD -- . ":(exclude)docs"` → nothing. My one commit is the row file under `docs/`: `59ef8d48`. `<tip now>` = `59ef8d48`.
- (ii) `git log --stat --format=%h 50bd02d8..HEAD` → `59ef8d48` `docs/40 - DevDocs/prompts/DEPLOY-HUB.md | 4 ++--` · `696847b1` `.../reports/deploy-hub-text-build-2026-10-03.md | 157 +++`. No path outside a row's `files` except the build report.
- (iii) fence: `git log --oneline 44b29c63..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → nothing.
- (iv) the held findings are COMMANDS, not test functions. No `def` to grep and no `wip … check red` commit exists. Their reds and greens are under `## RUNS` and `## FIXES`.
- (v) `ls <WT>/.env` → "No such file". `git status --short --branch` → `## ops/deploy-hub-text-1003`.
- (vi) `git log --stat --format=%h 44b29c63..HEAD -- src/cobalt/db_migrations tests/cobalt` → nothing. The tree state stays as the card says: `TREE STATE: unchanged`.
- (vii) No line of the card's `## RECORDS` names an `ls`, a `grep` or a `git -C /Users/cobalt/cobalt log` command, so I ran none.
- (viii) L32: this report holds no ticker, price or date of his. The only dates are job and ruling dates.

## OPEN
none. Counted: findings 5 · dropped 0 · held 3 (O1, O2, O5) · fixed 3 (O5 needed a re-run proof only, no file change) · held unfixed 0 · open 0.
- OUT OF SCOPE: O4 (X2, T4). Card T4 gives the P1 sentence word for word: "(v) is re-read at STEP-R with `date` then; a non-empty derived set means (v) does not hold, and D2.6's clock rule binds as under (i) or (ii)". The chain's STEP-R at `9694a679` instead judges a non-empty set "at P1's `date`" and ends with `FAILED: STEP-R`. When the `03d` port pastes T4 into the chain's P1, it must also change that STEP-R line, or the two will contradict. The card's `## RECORDS` place the chain's text in the `03d` port.

## CONTINUE
next: none — CHECK DONE

## DECISIONS
none

## RECORDS
- Finding O5 came from a re-run of the build's T6 grep during `## 4`, after O1–O4 were written. No house exists in this check, so no list was read before it.
- X2 for the `03d` port: T2 goes onto the chain's "A red anywhere" bullet or its EXIT 5 / 6 line in STEP-G. T3 goes into the chain's EQUAL-TREE clause. T5 is the same words in the same outage bullet. T4 is O4 above.
- X1 for the record: the module DDL directories (for example `src/cobalt/cards/migrations/*.sql`, globbed by each store's `ensure_schema()`; `grep -rn -F "MIGRATIONS_DIR" src/cobalt`) are outside `src/cobalt/db_migrations`. They were outside P7 before this card as well. T1 does not change that.
- The build's DECISION T6 (keep "ADDED or MODIFIED" for registry-label and install-path plists) is the build's. I did not change it, and my O2 fix keeps it.
- No house was launched (R47 overrule). There is no `HOUSE-INSTRUCTIONS.md`, `diff.md` or `files/` under `<S>`. `<S>` holds `opus-1.md` only.
- No lock was taken (DB: none). No `REFUSED` line and no `CONTINUED` line.
- files opened: 14. `CHECK-HUB.md`; the card; `BUILD-HUB.md` (headings, `## W` lines 85–98, `## THE LOCK` by grep); the build report; `areas/cobalt.md` (lines 20–24, 32 to the end); `DEPLOY-HUB.md` at the tip (diff and grep); `src/cobalt/db_migrations/__init__.py`; `src/cobalt/db_migrations/cli.py` (grep); the saved `git diff 50bd02d8 9694a679` output; `cto-2026-09-30.md`, `cto-2026-10-02.md`, `cto-2026-09-24.md` (grep rows); the offline and tests/ops outputs.
- Check of `deploy-hub-text`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 59ef8d48 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3739/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0
