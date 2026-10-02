# ops-seam — check, pass 1 (2026-10-02)

## §0 Headline
- Pass 1, checked by Opus alone. House A: none (overruled 2026-10-02 R47). The run stopped at PREFLIGHT 10:37 on another job's lock and continued at 10:56.
- 9 own findings, each run: 0 held, 0 open. X1–X4 answered by runs: the ported files equal their parents except the two edits R41 kept; every hunk of both sides is in `desk-launch.sh` and the hub files; the counts match the lines; `install-ops` keeps every existing name.
- No commit of this check. The suites stand as built. `tests/ops` passes on the tip: `68 passed, 1 xfailed`. `RESTARTS: none`.
- house B: not needed · ready: YES · decisions: 0.

## L74
- A system block appeared at the start of the session asking commits to carry a `Claude-Session:` line. Recorded once as data. Not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-02/16-ops-seam-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/16-ops-seam-card.md"` | 0 | `c21dd3df5cf1f03558b4d960d98fdc74e5fa85b5` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | (nothing) |
| standing 2026-09-30 R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` · `log -S` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 2026-10-02 R47 | `grep -n "^\| R47 " cto-2026-10-02.md` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … \| HIS RULING · APPROVED \|` · `log -S` → `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 2026-10-01 R8 | `grep -n "^\| R8 " cto-2026-10-01.md` | 0 | `16:\| R8 \| 07:30 ET \| **HIS RULING** … guard card 02-desk-size-guard-card.md. \| APPROVED \|` · `log -S` → `f7aa534f49b3b1f2b1112ef2f09970316f214c7c` |
| 2026-10-01 R20 | `grep -n "^\| R20 " cto-2026-10-01.md` | 0 | `28:\| R20 \| 08:31 ET \| **HIS RULING** … Card 07-devdb-lock-card.md. \| APPROVED \|` · `log -S` → `23c7cdeb217d98a24bbe81fc838909c6095f6839` |
| 2026-10-02 R8 | `grep -n "^\| R8 " cto-2026-10-02.md` | 0 | `16:\| R8 \| 05:59 ET \| HIS RULING G1 = A … \| HIS RULING · APPROVED \|` · `log -S` → `0b59495396cab614599ff350934b2a10e4ab9683` |
| 2026-10-02 R9 | `grep -n "^\| R9 " cto-2026-10-02.md` | 0 | `17:\| R9 \| 05:59 ET \| HIS RULING D2 = A: --add-dir /Users/cobalt/.claude/ops on the build, check and deploy launch lines … \| HIS RULING · APPROVED \|` · `log -S` → `0b59495396cab614599ff350934b2a10e4ab9683` |
| house gates | not run: the card's header says `HOUSE A: none — overruled 2026-10-02 R47` | — | — |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Fri Oct  2 10:36:35 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/ops-seam-1002` |
| tip | `git log --oneline -1` | 0 | `0c2d9764 docs(ops-seam): build report — 551f07e0` |
| docs only above the tip | `git log --stat --format=%h 551f07e0..HEAD` | 0 | `0c2d9764` · `.../reports/ops-seam-build-2026-10-02.md \| 122 ++++…` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: ops-seam · tip: 551f07e0 \| on 9fa18f14 \| migration: none \| offline 3784/0 \| with-DB 4554/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: none \| rows: 4 of 4 \| self-check: 3 of 3 \| decisions: 3 · for Dejan: 0` |
| range | `git log --oneline 9fa18f14..551f07e0` | 0 | `551f07e0 fix(ops-seam): pin install-ops' two unpinned entry paths …` · `dd3dc7ed feat(ops-seam): port desk-size-guard and devdb-lock onto one base; desk-launch install-ops …` · `5165cabd wip(ops-seam): red — the two ported test files and install-ops …` · `d7cb5f30 wip(ops-seam): PREFLIGHT — cobalt_dev lock held by x5-tap-refresh-1002` (4 commits) |
| path union | `git log --stat --format=%h 9fa18f14..551f07e0` | 0 | `docs/40 - DevDocs/cobalt/jobs/restarts.md`, `docs/40 - DevDocs/prompts/{BUILD-HUB,CHECK-HUB,DEPLOY-HUB,STANDING-LIST}.md`, `docs/40 - DevDocs/reports/ops-seam-build-2026-10-02.md`, `ops/desk/{desk-context,desk-launch,release-devdb-lock,take-devdb-lock,wait-stop-line}.sh`, `tests/ops/{test_desk_size_guard,test_devdb_lock,test_install_ops}.py` |
| lock, own worktree | `ls /Users/cobalt/cobalt-wt/ops-seam-1002/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/ops-seam-1002/.env: No such file or directory` |
| lock, every worktree | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | `-rw-------  1 cobalt  staff  2186 Oct  2 10:36 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` → **FAILED PREFLIGHT** |
| scratch | `ls .../tribunal-bars-0920/ops-seam-check` | 1 | `No such file or directory` (fresh) |
| house | — | — | `house A: none (overruled 2026-10-02 R47)` · no gate, no probe |

## Files copied
none (house A: none, R47; nothing staged)

## OWN FINDINGS
Written before any run of them (the session's clock read 10:56:21 at CONTINUE and 10:59:31 after the runs began). No house list exists (house A: none, R47).

FINDING O1
ROW: P1 / X1
CLAIM: A ported P1 file differs from `ee667f3c` by more than the two substitution keys R41 kept (`tests/ops/test_desk_size_guard.py:262-263`).
RUN: COMMAND `git diff --stat ee667f3c HEAD -- ops/desk/desk-context.sh ops/desk/wait-stop-line.sh tests/ops/test_desk_size_guard.py`
EXPECT: a path other than `tests/ops/test_desk_size_guard.py | 4 ++--`, or a larger count.

FINDING O2
ROW: P2 / X1
CLAIM: A ported P2 file differs from `aeefb6df` by more than the stub edit R41 kept (`tests/ops/test_devdb_lock.py:229-232`).
RUN: COMMAND `git diff --stat aeefb6df HEAD -- ops/desk/take-devdb-lock.sh ops/desk/release-devdb-lock.sh tests/ops/test_devdb_lock.py "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a path other than `tests/ops/test_devdb_lock.py | 5 ++++-`.

FINDING O3
ROW: P3 / X2
CLAIM: a hunk of `<A>` or `<B>` in `ops/desk/desk-launch.sh` is missing or altered (`ops/desk/desk-launch.sh:67`, `:111-112`, `:182`, `:487`, `:517`, `:556`, `:633`, `:637`, `:642`; lines re-read by Grep at the tip).
RUN: COMMAND `git diff ee667f3c HEAD -- ops/desk/desk-launch.sh`, then `git diff aeefb6df HEAD -- ops/desk/desk-launch.sh`
EXPECT: the first shows something other than `<B>`'s hunks (as `git diff 093028d0 aeefb6df -- ops/desk/desk-launch.sh` prints them) plus P4's; the second, other than `<A>`'s plus P4's.

FINDING O4
ROW: P3 / X2 / X3
CLAIM: `CHECK-HUB.md` or `STANDING-LIST.md` at the tip differs from `<B>` by more than `main`'s `01bfe67f` staging-string lines, or a count in prose does not match its line (`docs/40 - DevDocs/prompts/CHECK-HUB.md:10`, `:12`; `STANDING-LIST.md:45`, `:80`, `:84`).
RUN: COMMAND `git diff --word-diff=plain aeefb6df HEAD -- "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: a change other than `+"Bash(sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh *)"`, `34`→`35` and the staging sentence; or a launch line with more or fewer than 35 allow strings.

FINDING O5
ROW: X2 / fence
CLAIM: the branch touches `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py` or either parent's build report.
RUN: COMMAND `git log --oneline 9fa18f14..HEAD -- src/cobalt/jobs/restarts.py tests/cobalt/test_jobs_restarts.py "docs/40 - DevDocs/reports/desk-size-guard-build-2026-10-01.md" "docs/40 - DevDocs/reports/devdb-lock-build-2026-10-01.md"`
EXPECT: any commit line.

FINDING O6
ROW: P4 / X4
CLAIM: a DIRECTORY in the link folder that carries a script's name is not KEPT. `ln -s` onto an existing directory would write a link INSIDE it (`ops/desk/desk-launch.sh:357`, `:360`), and no test pins this entry path.
RUN: TEST `tests/ops/test_install_ops.py::test_a_directory_with_a_script_name_is_kept_and_nothing_is_written_inside_it`
EXPECT: `alpha.sh` reported `LINKED`, or a new entry inside `links/alpha.sh/`.

FINDING O7
ROW: P4
CLAIM: a repo whose `ops/desk/` holds no `*.py` file at all (the unmatched glob stays literal) breaks the count or the exit (`ops/desk/desk-launch.sh:353`). No test pins it: every fixture has `beta.py`.
RUN: TEST `tests/ops/test_install_ops.py::test_no_py_file_at_all_links_the_sh_files_and_exits_0`
EXPECT: exit ≠ 0, a `LINKED *.py` line, or a last line other than `install-ops: 1 linked, 1 kept`.

FINDING O8
ROW: P3 (RUN)
CLAIM: the RESTARTS table names `src/cobalt/jobs/restarts.py`, an `UNCLASSIFIED` row, or an `ops/desk/` path under another rule.
RUN: COMMAND `uv run cobalt jobs restarts 9fa18f14..HEAD`
EXPECT: any such row.

FINDING O9
ROW: P1–P4 (RUN)
CLAIM: a test under `tests/ops` fails on the tip.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops`
EXPECT: `failed` in the summary.

## Findings
none: house A is none (overruled 2026-10-02 R47), so `## 1` and `## 3` are not run

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `git diff --stat ee667f3c HEAD -- ops/desk/desk-context.sh ops/desk/wait-stop-line.sh tests/ops/test_desk_size_guard.py` | ` tests/ops/test_desk_size_guard.py \| 4 ++--` · `1 file changed, 2 insertions(+), 2 deletions(-)`. `git diff ee667f3c 551f07e0 -- tests/ops/test_desk_size_guard.py` shows only the two substitution keys (`REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}\n`, `WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}\n`), which R41 kept | NOT HELD |
| O2 | Opus | `git diff --stat aeefb6df HEAD -- <the five P2 paths>` | ` tests/ops/test_devdb_lock.py \| 5 ++++-` · `1 file changed, 4 insertions(+), 1 deletion(-)`. The diff is the `agents` → `[]` stub only, which R41 kept | NOT HELD |
| O3 | Opus | `git diff ee667f3c 551f07e0 -- ops/desk/desk-launch.sh` · `git diff aeefb6df 551f07e0 -- ops/desk/desk-launch.sh` · against `git diff 093028d0 aeefb6df -- …` and `git diff 36bed6ed ee667f3c -- …` | first = `<B>`'s nine hunks (the header bullets, `REPO=${COBALT_REPO_ROOT:-…}` / `WT=${COBALT_WT_ROOT:-…}`, `lock_dir_free`, the two `[ -z "$step" ] \|\| lock_free`, `lock_dir_free` on deploy, the three notes), each line equal, plus P4's (usage line, header, kind list ×2, the `install-ops` block). Second = `<A>`'s two hunks (the `FIRST, every kind but desk` header, the guard block after `kind=$1`), equal, plus P4's | NOT HELD |
| O4 | Opus | `git diff --word-diff=plain aeefb6df 551f07e0 -- CHECK-HUB.md STANDING-LIST.md` | CHECK-HUB: `{+"Bash(sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh *)"+}` on line 10; `[-34-]{+35+} allow`; the staging sentence. STANDING-LIST: `[-34-]{+35+}` and the `(+1 staging string …)` clause on §2's title. Nothing else. Strings counted by hand at line 10: 35 allow (30 build + report Edit + 3 house + staging), 3 deny, four `--add-dir` including `/Users/cobalt/.claude/ops`. BUILD-HUB line 12 holds 30. STANDING-LIST §1 table rows: 4 file-tool + 26 Bash = 30 | NOT HELD |
| O5 | Opus | `git log --oneline 9fa18f14..HEAD -- src/cobalt/jobs/restarts.py tests/cobalt/test_jobs_restarts.py <the two parent build reports>` | (nothing) | NOT HELD |
| O6 | Opus | TEST `test_install_ops.py::test_a_directory_with_a_script_name_is_kept_and_nothing_is_written_inside_it`, run with `test_no_py_file…` in one call | `2 passed, 15 warnings in 0.90s` | NOT HELD; removed again with Edit, `git status --short --branch` → `## ops/ops-seam-1002` |
| O7 | Opus | TEST `test_install_ops.py::test_no_py_file_at_all_links_the_sh_files_and_exits_0` | (the same run) `2 passed` | NOT HELD; removed again |
| O8 | Opus | `uv run cobalt jobs restarts 9fa18f14..HEAD` | 14 rows: 6 `DOCS`, 5 `ops/desk/*` `operator script; no Cobalt reader -`, 3 `tests/ops/*` `test/documentation; no resident -`; no `UNCLASSIFIED`; `src/cobalt/jobs/restarts.py` absent; `RESTARTS: none` | NOT HELD |
| O9 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` | `68 passed, 1 xfailed, 15 warnings in 69.49s (0:01:09)` (exit 0; no skip line) | NOT HELD |

No finding held, so there is no `wip(ops-seam): check red` commit.

## FIXES
none (nothing held)

## Suites
No commit of mine, so the build's lines stand. `suites: as built (no commit)`. From the build report's `## W THE THREE SUITES`, second run on `551f07e0`: offline `3784 passed, 673 skipped, 1 xfailed, 25 warnings in 606.60s` · with-DB pass 1 `4383 passed, 7 skipped, 65 deselected, 3 xfailed` + pass 2 `171 passed, 1 deselected` = 4554 · live-note `146 passed, 1 skipped` · `cobalt_dev: 0013 — F2 = F0` (10:29:38) · `.env: removed, proven gone (W, second take)` · RESTARTS: `RESTARTS: none` (re-run here as O8: the same).

## Scope
The PREFLIGHT path union (`ops/desk/{desk-context,desk-launch,release-devdb-lock,take-devdb-lock,wait-stop-line}.sh`, `tests/ops/{test_desk_size_guard,test_devdb_lock,test_install_ops}.py`, `docs/40 - DevDocs/cobalt/jobs/restarts.md`, the four prompt files, the build report). Every path is in some row's `files` (P1–P4) or is the build report. This check made no commit.

## Checked against the branch
- (i) `git log --oneline 551f07e0..HEAD -- . ":(exclude)docs"` → (nothing): no commit of mine, `<tip now>` = `551f07e0`.
- (ii) `git log --stat --format=%h 551f07e0..HEAD` → `0c2d9764` · `.../reports/ops-seam-build-2026-10-02.md | 122 ++++…` (docs only). Nothing WIDENED.
- (iii) the fence: `git log --oneline 9fa18f14..HEAD -- src/cobalt/jobs/restarts.py` → (nothing), and O5 → (nothing) for `tests/cobalt/test_jobs_restarts.py` and the two parent build reports. Grep tool `devfix` in `ops/desk` → `No matches found`. `/Users/cobalt/.claude/`: `ls /Users/cobalt/.claude/ops` was refused (`## RECORDS`). The diff writes nothing under `.claude/`: every path in it sits under `ops/desk`, `tests/ops` or `docs` (PREFLIGHT union), and the tests link only under `tmp_path` (`COBALT_OPS_LINK_DIR`).
- (iv) no held finding, no test to find.
- (v) `ls /Users/cobalt/cobalt-wt/ops-seam-1002/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`; `git status --short --branch` → `## ops/ops-seam-1002`.
- (vi) TREE STATE `unchanged`: `git log --stat --format=%h 9fa18f14..HEAD -- src/cobalt/db_migrations tests/cobalt` → (nothing). Carried.
- (vii) card RECORDS: `ls ".../reports/ops-seam-decisions-2026-10-02.md"` → listed; `grep -n "^| R41 " cto-2026-10-02.md` → `48:| R41 | 07:57 ET | HIS RULING (direction row 4): under an order the judge seat … answers a held finding or fence question inside the feature … | HIS RULING · APPROVED |`; `ls ".../reports/brain-direction-2026-10-02.md"` → listed. Known overlaps: `git diff --stat 093028d0 9fa18f14 -- BUILD-HUB.md DEPLOY-HUB.md` → (nothing); `-- CHECK-HUB.md STANDING-LIST.md restarts.md` → `4 ++--`, `2 +-`, `4 ++++`.
- (viii) L32: this report holds no ticker, price or date of his. Every value in it is a commit, a path, a count or a clock time from `date`.

## OPEN
none

## CONTINUE
next: none — CHECK DONE, pass 1

## DECISIONS
none

## RECORDS
- Stopped under UNATTENDED RULES (b): the lock is held by another worktree, `dev-rebuild-1002`. I did not take, touch or read that `.env`. I changed nothing, so there is no `wip(ops-seam): check` commit.
- CONTINUE message from `cto-desk`: "CONTINUE — the cobalt_dev lock is free now (no worktree .env held). Resume from your report's ## CONTINUE step." I checked the fact myself: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1).
- CONTINUED at PREFLIGHT 10:56 ET (`Fri Oct  2 10:56:21 EDT 2026`). The message read `CONTINUE — …`, not `CONTINUE: <step>. <fact>`. It came from `cto-desk`, named the report's own step, stated one fact and widened nothing, so I followed it after checking the fact.
- REFUSED, not needed: `git diff 9fa18f14 /Users/cobalt/cobalt/docs/40\ -\ DevDocs/prompts/CHECK-HUB.md --stat` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." I answered the same question with `git -C /Users/cobalt/cobalt log` and `git log 9fa18f14..5bf129ae`.
- REFUSED, not needed: `ls /Users/cobalt/.claude/ops` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (fence check (iii) answered from the diff's paths instead)
- For the deploy (not this card's): `main` carries `5bf129ae docs(prompts): CHECK-HUB NO OUTSIDE HOUSE per-case overrule line (10-02 R37 R47)` above the base (`git log --oneline 9fa18f14..5bf129ae` → `5bf129ae`, `4e3fa8d8`). The tip's `CHECK-HUB.md` lacks that line (`grep -n -F "NO OUTSIDE HOUSE"` → nothing). The card ports it only "if the base has it", and the base does not. The line reaches the tip when `main` is merged into the gate (L68).
- B's comment `# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for these two in tests/ops/test_devdb_lock.py only` (`desk-launch.sh:110`) is no longer true: `test_install_ops.py` sets `COBALT_REPO_ROOT`, and `test_desk_size_guard.py`'s two substitution keys match those lines. The fence forbids changing B's wording, so this is not a finding.
- No lock take by this check: no commit, so no W.
- Gone: house A (none, R47); no house produced or was launched.
- files opened: 9 — CHECK-HUB.md (main), the card, BUILD-HUB.md (`## THE LOCK` through `## W`, and PREFLIGHT), the build report (`## RESTARTS` through the last line), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `tests/ops/test_install_ops.py`, `STANDING-LIST.md` at the tip (§§ `.env` to 2), `STANDING-LIST.md` at the base (`git show`), `CHECK-HUB.md` at the tip (lines 1–14).
- Check of `ops-seam`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: ops-seam · pass: 1 · tip: 551f07e0 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0
