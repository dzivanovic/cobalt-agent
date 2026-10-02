# devdb-lock — check, pass 1 (2026-10-01)

## §0 Headline
Pass 1 of the devdb-lock check: house A was Grok (Sol is out of usage until Oct 4th, 2:06 PM). Grok wrote 7 findings and I wrote 1. 6 held; I fixed 5 at `aeefb6df`.
The fixes: the release script now removes only a lock it holds (G2, G3). In DEPLOY-HUB, the live-note step runs before the take (O1, G6), and a `STEP-D0` resume writes `RESUMED` first (G7).
1 held finding is not fixed: G1, the build's edit to `src/cobalt/jobs/restarts.py`. The card fences `src/`; the desk's CONTINUE lifted the fence. It goes to Dejan under `## DECISIONS`.
Not held: G4 (`08` minutes waits as it should) and G5 (BASE refuses `build`, as the card's red says).
Suites on `aeefb6df`: offline 3770/0, with-DB 4369 + 171 = 4540/0, live-note 146/0. `cobalt_dev: 0013 — F2 = F0`; `.env` removed. House B (Gemini) is needed: `ready: NO`.

## L74
A system block in this session asked commits to end with a `Claude-Session:` line (seen 22:48 EDT). Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" ".../2026-10-01/07-devdb-lock-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-01/07-devdb-lock-card.md"` | 0 | `314605d426e7690262d6a45f1bc7fe580d21e7cf` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | (nothing) |
| standing list R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C … log -1 --format=%H -S"| R60 |" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R20 | `grep -n "^| R20 " cto-2026-10-01.md` | 0 | `28:| R20 | 08:31 ET | **HIS RULING** … yes on brain's four … Card 07-devdb-lock-card.md. | APPROVED |` |
| R20 committed | `git -C … log -1 --format=%H -S"| R20 |" -- cto-2026-10-01.md` | 0 | `23c7cdeb217d98a24bbe81fc838909c6095f6839` |
| house gate R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | one row, line 35 (STANDING `Bash(grok *)`) |
| house gate R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | one row, line 37 (four house strings standing) |
| R19 committed | `git -C … log -1 --format=%H -S"| R19 |" -- cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Thu Oct  1 22:48:19 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/devdb-lock-1001` |
| head | `git log --oneline -1` | 0 | `35bf039d docs(devdb-lock): build report — a9339f0a` |
| docs-only above TIP | `git log --stat --format=%h a9339f0a..HEAD` | 0 | `35bf039d` · `.../reports/devdb-lock-build-2026-10-01.md | 68` — docs only |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: devdb-lock · tip: a9339f0a | on 093028d0 | migration: none | offline 3770/0 | with-DB 4540/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 7 · for Dejan: 1` |
| range | `git log --oneline 093028d0..a9339f0a` | 0 | `a9339f0a fix(devdb-lock): ops/desk lock scripts and desk-launch.sh classified (L42)` · `28a70ae9 wip(devdb-lock): RESTARTS — ops/desk paths unclassified; class home is fenced src/` · `9915ca9e feat(devdb-lock): atomic waiting cobalt_dev lock scripts; …` · `bd144d45 wip(devdb-lock): red` (4 commits) |
| range paths | `git log --stat --format=%h 093028d0..a9339f0a` | 0 | a9339f0a: `docs/40 - DevDocs/cobalt/jobs/restarts.md`, `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py` · 28a70ae9: build report · 9915ca9e: `prompts/BUILD-HUB.md`, `prompts/CHECK-HUB.md`, `prompts/DEPLOY-HUB.md`, `prompts/STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `ops/desk/release-devdb-lock.sh`, `ops/desk/take-devdb-lock.sh`, `tests/ops/test_devdb_lock.py` · bd144d45: `tests/ops/test_devdb_lock.py` |
| lock: own .env | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock: any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| gemini | `agy --version` | 0 | `1.2.14` |
| Sol probe | `codex exec … "Reply with only the word OK." < /dev/null` | 1 | `ERROR: You've hit your usage limit. … try again at Oct 4th, 2026 2:06 PM.` → METER |

Seats: house A: Grok · house B, if needed: Gemini. Card `HOUSE B: as needed` — not mandatory.

## Files copied
`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/devdb-lock-check`. Every copy by `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh <src> <dest>`, which runs `cmp -s` on the pair and prints `COPIED <bytes> <dest>` only on a byte-identical copy (its own `wc -c` of the copy):
| copy under `<S>/files/` | bytes |
|---|---|
| `07-devdb-lock-card.md` | 5134 |
| `devdb-lock-build-2026-10-01.md` | 38065 |
| `brain-parallel-builds-2026-10-01.md` | 10900 |
| `wt/src/cobalt/jobs/restarts.py` | 11902 |
| `wt/tests/cobalt/test_jobs_restarts.py` | 26845 |
| `wt/tests/ops/test_devdb_lock.py` | 10238 |
| `wt/ops/desk/desk-launch.sh` | 31128 |
| `wt/ops/desk/take-devdb-lock.sh` | 2556 |
| `wt/ops/desk/release-devdb-lock.sh` | 1848 |
| `wt/docs/40 - DevDocs/prompts/BUILD-HUB.md` | 32851 |
| `wt/docs/40 - DevDocs/prompts/CHECK-HUB.md` | 39114 |
| `wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md` | 57080 |
| `wt/docs/40 - DevDocs/prompts/STANDING-LIST.md` | 31736 |
| `wt/docs/40 - DevDocs/cobalt/jobs/restarts.md` | 3629 |
| `main-now/BUILD-HUB.md` · `main-now/DEPLOY-HUB.md` · `main-now/CHECK-HUB.md` · `main-now/STANDING-LIST.md` (main's hubs, the before-side for L3/L4) | 30823 · 55309 · 38685 · 29510 |

`diff.md`: Written from the saved output of `git log -p 093028d0..a9339f0a -- . ":(exclude)docs"`; `grep -c "^commit "` → `3`. PREFLIGHT's range count is 4; `git log --oneline 093028d0..a9339f0a -- . ":(exclude)docs"` → 3 lines (`a9339f0a`, `9915ca9e`, `bd144d45`): the fourth, `28a70ae9`, touches only the build report under `docs/`. See `## DECISIONS` (ASK DESK 1). `rulings.md`: the R20 row under its command. `HOUSE-INSTRUCTIONS.md`: the HOUSE TEXT verbatim, the card's ROWS, NOT IN THIS JOB, CHECK ASKS (none on the card), RECORDS, and the Files paragraph.

## OWN FINDINGS
FINDING O1
ROW: L3
CLAIM: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:112` now keeps "The lock and `<GATE>/.env` … held to your stop line" after G (f), and `:42` says the `ls -la <GATE>/.env` before every pytest "from G (b) to THE RELEASE … PRINTS the file", yet G (e) at `:114` still runs the live-note suite labelled "LIVE-NOTE, no `.env`" after (f) and before THE RELEASE (`:113`, after 4.6). On `main` (`DEPLOY-HUB.md:111`) (f) removed `.env` before (e), so the change to hold the lock left (e) running with the dev `.env` present, against its own precondition.
RUN: COMMAND `grep -n -F "(e) LIVE-NOTE, no" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (then the same with `stay held to your stop line`, to show the order)
EXPECT: `114:- (e) LIVE-NOTE, no \`.env\`: …` and `112:- (f) THE L76 RELEASE … The lock and \`<GATE>/.env\` stay held to your stop line …` — (e) sits after the (f) that keeps `.env`.

Considered, no finding: the build's D7 entry paths (deploy `STEP-D0` over its own lock directory; the take's copy failure). Read at `ops/desk/desk-launch.sh:441-447` and `ops/desk/take-devdb-lock.sh:47-55` (`:54` the refusal line): both do what the row says. A pin that passes is `NOT HELD` under `## 4` and is removed, so the check adds no pin for them; they stay the build's D7.

## Findings
House A Grok, `house-a.md` written by Grok itself (23:11 EDT), closing line `FINDINGS: 7`. Every block has a `RUN:` line followed by a test function or one command line with an allowed beginning: none dropped.
| id | house | row | claim | form |
|---|---|---|---|---|
| G1 | Grok | SCOPE | `src/cobalt/jobs/restarts.py`, its test and its DevDocs line are edited, though `src/` is fenced and no row names them | COMMAND |
| G2 | Grok | L1 | release removes `.env` and prints `lock released` when no lock names the worktree (no lock dir) | TEST |
| G3 | Grok | L1 | release re-reads no owner before `rmdir`: a lock another worktree takes between the check and the removal is deleted | TEST |
| G4 | Grok | L1 | `<minutes>` `08` is accepted but `-lt` treats it as bad octal: no wait, exit 4 at once | TEST |
| G5 | Grok | L2 | the L2 test cannot go red on BASE for the lock reason: the `COBALT_WT_ROOT` override exists only at the tip | COMMAND |
| G6 | Grok | L3 | DEPLOY-HUB STEP-G orders THE RELEASE (`:113`) before live-note (`:114`, `no .env`), against "held to the stop line" (`:102`, `:112`) | COMMAND |
| G7 | Grok | L4 | DEPLOY-HUB `STEP-D0` resume writes `RESUMED` only after checks and G (f)/RELEASE, not as its first act | COMMAND |

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -n -F "(e) LIVE-NOTE, no" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · `grep -n -F "stay held to your stop line" …` | `114:- (e) LIVE-NOTE, no \`.env\`: …` · `112:- (f) THE L76 RELEASE … The lock and \`<GATE>/.env\` stay held to your stop line (L76: the gate holds it alone from its cut to its stop line).` · THE RELEASE at `:113` is "after 4.6" | HELD — (e) runs after (f) keeps `.env`, and before THE RELEASE, yet requires no `.env` |
| G1 | Grok | `git diff 093028d0..a9339f0a -- src/cobalt/jobs/restarts.py tests/cobalt/test_jobs_restarts.py "docs/40 - DevDocs/cobalt/jobs/restarts.md"` | the three hunks as claimed: `OPS_TOOLS` gains `ops/desk/desk-launch.sh`, `ops/desk/release-devdb-lock.sh`, `ops/desk/take-devdb-lock.sh`; `+def test_the_cobalt_dev_lock_scripts_are_operator_scripts_with_no_restart`; `+## 2026-10-01 — devdb-lock` | HELD, NOT FIXED — `src/cobalt/jobs/restarts.py`: an edit inside the card's fence (`## NOT IN THIS JOB`: "`src/`"), made on the desk's `CONTINUE: RESTARTS` (build D6). Undoing it re-opens L42 (`UNCLASSIFIED`, the build's first RESTARTS table) and lies outside the rows' files. `## DECISIONS` |
| G2 | Grok | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_devdb_lock.py::test_release_leaves_the_env_when_no_lock_names_this_worktree` | `1 failed, 15 warnings in 1.14s`; `AssertionError: lock released` / `assert 0 != 0` (`returncode=0, stdout='lock released\n'`) | HELD — the row: the release removes the `.env` "only if the lock names this worktree"; with no lock it removed it |
| G3 | Grok | `uv run pytest … ::test_release_does_not_remove_a_lock_taken_after_it_saw_none` | `1 failed, 15 warnings in 1.00s`; `FileNotFoundError: … wt/.cobalt_dev.lock/owner`. The stub fired: Glob `**/.env` over that tmp `wt` → `…/wt/beta/.env` (planted by the stub during `rm -f` of alpha's `.env`), and the lock directory it made is gone | HELD — the row: "a lock held by another worktree is not touched"; the unguarded second `[ -d "$LOCK" ]` removed beta's lock |
| G5 | Grok | `git show 093028d0:ops/desk/desk-launch.sh` | `94:REPO=/Users/cobalt/cobalt` · `95:WT=/Users/cobalt/cobalt-wt` (no `COBALT_WT_ROOT`) · `lock_free` bare at `457`, `495`, `534` | NOT HELD — the output is as the house says, but the card's red is "RED on `BASE`: `build` is refused", and BASE refuses `build` (build report `:72`, `REFUSED: the card must be …`). The lock reason itself is shown red at E3 by MUTATION 2 (`lock_free` back on build/check → `REFUSED: with-DB launch refused: the cobalt_dev lock is held (…/wt/beta/.env) (L76)`, report `:89`). No row clause is unbuilt and no test stays green with the fix undone |
| G6 | Grok | `grep -n -F "after 4.6" …DEPLOY-HUB.md` · `grep -n -F "HELD TO YOUR STOP LINE" …` · (the `LIVE-NOTE, no` and `stay held` greps of O1). The house's one `grep -n -E "a|b|c|d"` split into four fixed-string greps (form only; `## UNATTENDED RULES` one plain pattern per call) | `75:… THE RELEASE, after 4.6 …` · `113:- THE RELEASE (once, before the stop line of every ending from G (b) on; after 4.6 or STEP-5 (3) …)` · `102:- (b) THE LOCK, taken here and HELD TO YOUR STOP LINE (L76) …` · `112`, `114` as O1 | HELD, as O1 — THE RELEASE bullet itself is placed by its words ("before the stop line … after 4.6"), not by its position; what the order breaks is (e)'s `no .env` with the lock held. One defect with O1, one fix |
| G4 | Grok | `uv run pytest … ::test_leading_zero_minutes_still_waits_out_the_minute` (background) | `1 failed, 15 warnings in 300.91s (0:05:00)`; `subprocess.TimeoutExpired: Command '['sh', '…/ops/desk/take-devdb-lock.sh', 'beta', '08']' timed out after 300 seconds` | NOT HELD — red for another reason: with `08` the take WAITED (past the test's own 300 s limit), so `-lt` read `08` as a number and the loop did not break at once. Test removed again with the Edit tool |
| G7 | Grok | `grep -n "THE STALE LINE" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | `55:` — "Verify, each its own call, (e) FIRST: … otherwise run STEP-5 (3) NOW … THE GATE'S OWN \`.env\` … run G (f) for it … and THE RELEASE … THE STALE LINE: (a) is read before any report write; your FIRST report write of a resume quotes that old last line under \`# RELAUNCH\` and makes the last line \`RESUMED: STEP-D0 <time from date>\`" | HELD — L4: "the first act after any `CONTINUE` is writing `RESUMED`"; here (e), a possible STEP-5 (3) restore and G (f)'s rollback run first while the `FAILED:` line stands |

## FIXES
Red commit first: `12ed3626 wip(devdb-lock): check red — G2, G3` (`tests/ops/test_devdb_lock.py`: `test_release_leaves_the_env_when_no_lock_names_this_worktree`, `test_release_does_not_remove_a_lock_taken_after_it_saw_none`). Fix commit `aeefb6df fix(devdb-lock): release touches only its own lock; deploy live-note before the take; deploy resume writes RESUMED first (check G2, G3, O1, G6, G7)`.
| ids | file | change | after |
|---|---|---|---|
| G2, G3 | `ops/desk/release-devdb-lock.sh` | `mine` set only when the lock directory names this worktree; no lock and this worktree's `.env` present → exit 3, nothing touched; the lock directory is removed only when `mine`; the proof checks the `.env`, and the lock only while it still names this worktree. Header EXITS updated | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_devdb_lock.py` → `22 passed, 15 warnings in 63.03s (0:01:03)` |
| O1, G6 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` G (e), G (b) | (e) LIVE-NOTE runs right after (a), before the take at (b), with its own `ls -la <GATE>/.env` (No such file); (b) says "after (a) and (e)" | `grep -n -F "BEFORE THE TAKE at (b)"` → `114:` (prompt edit; no test) |
| G7 | `DEPLOY-HUB.md:55` THE ONE RESUME | THE STALE LINE is the FIRST ACT, before (e) and any call but `date`: read the old last line, quote it under `# RELAUNCH`, set `RESUMED: STEP-D0 <time>`; (a) and the STEP-5 (2) exception read "that old last line, as quoted"; the later STALE LINE sentence removed | `grep -n -F "STALE LINE"` → one hit, `55:` "THE STALE LINE, YOUR FIRST ACT …" (prompt edit; no test) |
DevDocs line: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` or the prompts (as the build found); none written.

## Suites
On `<tip now>` = `aeefb6df`, by `BUILD-HUB.md` (installed, on `main`) `## RESTARTS` and `## W`:
- RESTARTS: `uv run cobalt jobs restarts 093028d0..HEAD` → exit 0; `ops/desk/*` three rows `operator script; no Cobalt reader -`, `src/cobalt/jobs/restarts.py M static import reach com.cobalt.radar`, tests and docs `-`; last line `RESTARTS: com.cobalt.radar`. No `UNCLASSIFIED`.
- (a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3770 passed, 673 skipped, 1 xfailed, 25 warnings in 564.51s (0:09:24)`. The check's two new tests sit in `tests/ops/test_devdb_lock.py`, outside these paths; that file → `22 passed` (FIXES).
- (b) THE LOCK, 23:29 EDT: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/devdb-lock-1001/.env`; `ls -la …/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  1 23:29 /Users/cobalt/cobalt-wt/devdb-lock-1001/.env` (one line, ours). `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → 36 tables, the eight above `0013` absent (`-`), `NOTHING WAS APPLIED`, `code: aeefb6df (clean)`.
- (c) PASS 1, the hub's command byte for byte (nothing deselected for this build) → `4369 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 701.37s (0:11:41)`. SKIPPED: `test_cards_picks.py:388` (S2-P2 card_score present), `:401` (real S2-P2 0007 applied), `test_radar_evaluate.py:695`, `test_s3_c4_experiments.py:95`, `taxonomy/test_catalyst.py:365`, `taxonomy/test_predicate.py:262` (each `COBALT_LIVE_VAULT_ROOT not set — the hub runs …`), `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC … not set`). `<d1>` = 4369.
- (c2) FORWARD → **dev forward: APPLIED 23:41 EDT** (`date` → `23:41:44`): `0001` … `0011`, `0013` … `0022`; eight tables CREATED; `content UNCHANGED on every table`; no `CHANGED`. `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2 byte for byte → `171 passed, 1 deselected, 5 warnings in 218.18s (0:03:38)`. `<d2>` = 171; `<d>` = 4540.
- (c3r) no with-DB test added by build or check: no ticker written, no `aset_sizings` query owed.
- (f) `--rollback --down-to 0013` → `0022` … `0014` newest first; eight tables DROPPED; `content UNCHANGED on every table`. `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>`: **`cobalt_dev: 0013 — F2 = F0`**. Lock (d): `rm …/devdb-lock-1001/.env`; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `date` → `23:46:11`. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE, `.env` absent → `146 passed, 1 skipped, 15 warnings in 25.09s`; the skip `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`; none names `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.

## Scope
PREFLIGHT's path union (`093028d0..a9339f0a`): `ops/desk/take-devdb-lock.sh`, `ops/desk/release-devdb-lock.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_devdb_lock.py` (rows L1, L2); the four prompts (L3, L4); the build report; and `src/cobalt/jobs/restarts.py`, `tests/cobalt/test_jobs_restarts.py`, `docs/40 - DevDocs/cobalt/jobs/restarts.md` — in no row, `src/` fenced (G1; the build's D6). The check's commits: `tests/ops/test_devdb_lock.py` (L1's test file), `ops/desk/release-devdb-lock.sh` (L1), `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (L3, L4). Nothing of the check's lies outside the rows' files.

## Checked against the branch
- (i) `git log --oneline a9339f0a..HEAD -- . ":(exclude)docs"` → `aeefb6df fix(devdb-lock): … (check G2, G3, O1, G6, G7)` · `12ed3626 wip(devdb-lock): check red — G2, G3`. `<tip now>` = `aeefb6df`.
- (ii) `git log --stat --format=%h a9339f0a..HEAD` → `aeefb6df`: `DEPLOY-HUB.md`, `ops/desk/release-devdb-lock.sh` · `12ed3626`: `tests/ops/test_devdb_lock.py` · `35bf039d`: the build report. Every non-docs path is a row's file. No `WIDENED`.
- (iii) the fence's `src/`: `git log --oneline 093028d0..HEAD -- src` → `a9339f0a fix(devdb-lock): ops/desk lock scripts and desk-launch.sh classified (L42)` — NOT EMPTY (G1, `## DECISIONS`). The other fenced items (the symlink install, LAWS, other allow strings, the lock's meaning) are not paths on this branch; the check added no allow string.
- (iv) `grep -n -F "def test_release_leaves_the_env_when_no_lock_names_this_worktree" tests/ops/test_devdb_lock.py` → `143:` · `grep -n -F "def test_release_does_not_remove_a_lock_taken_after_it_saw_none" …` → `151:`; `12ed3626` (red) sits below `aeefb6df` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `git status --short --branch` → `## ops/devdb-lock-1001`.
- (vi) `git log --stat --format=%h 093028d0..HEAD -- src/cobalt/db_migrations tests/cobalt` → `a9339f0a`: `tests/cobalt/test_jobs_restarts.py | 18 +` (an offline test added to an existing file); no migration, no new with-DB test file: `TREE STATE: unchanged` holds.
- (vii) card record 1: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R20 |" -- "docs/40 - DevDocs/reports/cto-2026-10-01.md"` → `23c7cdeb217d98a24bbe81fc838909c6095f6839`; the row (AUTHORIZATION) carries `HIS RULING` and `APPROVED`. Record 2 (a fixed file's procedure change read by one other house, L9/L67): this check's house A, Grok, read the four hubs' changes (`HOUSE-INSTRUCTIONS.md` Files paragraph, `files/wt/…` against `files/main-now/…`); its G6, G7 are on DEPLOY-HUB.
- (viii) L32: this report holds no ticker, price or date of his; the values quoted are fingerprints, counts, times of this run and constructed test values.

## OPEN
- G1 — HELD, NOT FIXED — `src/cobalt/jobs/restarts.py`. The finding (Grok): the build edits `src/` (`OPS_TOOLS` gains the three `ops/desk/` paths), its test and its DevDocs page, though the card fences `src/` and no row names them. The run: `git diff 093028d0..a9339f0a -- …` shows the three hunks. Why not fixed: undoing it brings back the `UNCLASSIFIED` rows (L42, the build's first RESTARTS table) and the file is outside the rows. What settles it: the desk's (or his) word that the `CONTINUE: RESTARTS` lift of the fence for one line stands (build D6), recorded as a ruling row; or a card row naming `src/cobalt/jobs/restarts.py`.

## CONTINUE
next: none — CLOSE done (pass 1). House B (Gemini) at PASS-2.

## DECISIONS
- **G1 — HELD, NOT FIXED — `src/cobalt/jobs/restarts.py` · FOR DEJAN (scope).** The card's `## NOT IN THIS JOB` fences `src/`; commit `a9339f0a` adds `ops/desk/desk-launch.sh`, `ops/desk/release-devdb-lock.sh`, `ops/desk/take-devdb-lock.sh` to `OPS_TOOLS` (`src/cobalt/jobs/restarts.py:36-43`) with a pin in `tests/cobalt/test_jobs_restarts.py`, on the desk's `CONTINUE: RESTARTS` ("the fence "src/" is lifted for exactly one line", citing K10, L42, R127; build report `:122`). `## 7` (iii) is not empty. The build asked the same (its D6). Safe default taken: the edit is left as built (removing it re-opens L42's UNCLASSIFIED rows and breaks RESTARTS); counted `held unfixed`; `ready: NO` until a ruling row or a card row covers it. The same `OPS_TOOLS` literal is also edited on `ops/desk-size-guard-1001` (`e5d6238b`, build report `:122`): the two meet at the deploy's merge.
- **ASK DESK 1: the diff copy's commit count. [22:50 EDT]** `## 1` (1) says `grep -c "^commit "` over `diff.md` = PREFLIGHT's commit count, else `FAILED: copy`. The count is 3 against PREFLIGHT's 4, because `-- . ":(exclude)docs"` leaves out `28a70ae9`, which touches only the build report (`git log --oneline 093028d0..a9339f0a -- . ":(exclude)docs"` → 3 lines). Safe default taken: the copy is the git output whole, so not `FAILED`; the house was told of the fourth commit in its Files paragraph. Should the rule compare against the code-commit count?
- **ASK DESK 2: a merge seam on the hubs. [23:50 EDT]** `main` carries `01bfe67f ops(desk): stage-copy.sh + CHECK-HUB staging allow (10-01 R37 R39)` after this branch's base: it adds `Bash(sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh *)` to `CHECK-HUB.md`'s launch line and its count (main's THE LIST reads "33 allow"; this branch's reads "34 allow" without that string). Both edit the same launch line and THE LIST sentence, so the deploy's merge of this branch meets a conflict there (and possibly in `STANDING-LIST.md`). Safe default taken: nothing changed (a merge and another allow string are outside the card, its fence "Any other allow string"); the resolved line must hold all 35 strings and `--add-dir /Users/cobalt/.claude/ops`.

## RECORDS
- Sol METER: `try again at Oct 4th, 2026 2:06 PM` (probe 22:48 EDT). House A was Grok (the next in the seat order); house B, if needed: Gemini.
- Grok wrote `house-a.md` itself (stdout: the path only); closing line `FINDINGS: 7`. Launched 22:52 EDT, notice 23:11 EDT.
- Dropped findings: none.
- NOT HELD and removed again: G4 (`test_leading_zero_minutes_still_waits_out_the_minute`). NOT HELD, a command: G5.
- `REFUSED, not needed: ls -la /private/var/folders/…/pytest-1736/test_release_does_not_remove_a0/wt/beta — Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (read instead with the Glob tool, for G3's stub evidence).
- Form repair: G6's one `grep -n -E` with an alternation run as four `grep -n -F` calls; no assertion changed. Grok's tests G2, G3, G4 pasted unchanged.
- Lock takes: one, W (23:29–23:46 EDT), by the installed hub's procedure (`ls`, `cp`, `rm`); `.env: removed, proven gone (W)`. No extra take.
- Main's `CHECK-HUB.md` (installed) is the file this check followed; the branch's lock-script procedure is not installed, so the scripts were run only by the tests, inside `tmp_path`.
- L74: one block, recorded under `## L74`; not acted on.
- files opened: 13 — `prompts/CHECK-HUB.md` (main), the card, `prompts/BUILD-HUB.md` (main; THE LOCK, W, PREFLIGHT rows), the build report (RESTARTS, W, SELF-CHECK, FOR THE CHECK, DECISIONS, RECORDS, E2, E3), `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `ops/desk/desk-launch.sh`, `ops/desk/stage-copy.sh`, `ops/desk/release-devdb-lock.sh`, `tests/ops/test_devdb_lock.py`, `prompts/DEPLOY-HUB.md` (branch; by grep), `house-a.md`, and the saved outputs of the two diffs (`git log -p`, the docs `git diff`). Not opened: the brain report (copied for the house, not read), LAWS.md.
- Check of `devdb-lock`, pass 1: house A `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: devdb-lock · pass: 1 · tip: aeefb6df · house A: Grok FINDINGS: 7 · findings: 8 · dropped: 0 · held: 6 · fixed: 5 · held unfixed: 1 · open: 1 · house B: needed · suites: offline 3770/0 · with-DB 4540/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 1

# PASS 2

## §0 Headline
Pass 2 (house B) produced nothing, so nothing new was found, run or fixed. Gemini's headless run was denied a tool and printed no list (HARNESS), and no house is left: Sol is out of usage until Oct 4th 2:06 PM, and Grok was house A.
The branch is unchanged at `aeefb6df`; pass 1's suites stand there, `cobalt_dev` is at 0013 and `.env` is gone.
One item stays open: G1, the build's one-line `src/cobalt/jobs/restarts.py` edit inside the card's fence. Desk record R57 says the edit stands, but R57 is not a `HIS RULING … APPROVED` row, so G1 is counted `held unfixed`, `ready: NO`, and it goes FOR DEJAN.

## L74
The attribution block in this session again asks commits to end with a `Claude-Session:` line (seen 23:49 EDT). Recorded as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" "<card>"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- <card>` | 0 | `314605d426e7690262d6a45f1bc7fe580d21e7cf` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | 0 | (nothing) |
| standing list R60 | `grep -n "^| R60 " cto-2026-09-30.md` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C … log -1 --format=%H -S"| R60 |" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS R20 | `grep -n "^| R20 " cto-2026-10-01.md` | 0 | `28:| R20 | 08:31 ET | **HIS RULING** … Card 07-devdb-lock-card.md. | APPROVED |` |
| R20 committed | `git -C … log -1 --format=%H -S"| R20 |" -- cto-2026-10-01.md` | 0 | `23c7cdeb217d98a24bbe81fc838909c6095f6839` |
| house gate R17 | `grep -n "^| R17 " cto-2026-09-24.md` | 0 | one row, line 35 (rechecked 23:52 EDT before the launch) |
| house gate R19 | `grep -n "^| R19 " cto-2026-09-24.md` | 0 | one row, line 37 (rechecked 23:52 EDT) |
| R19 committed | `git -C … log -1 --format=%H -S"| R19 |" -- cto-2026-09-24.md` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |
| desk word R57 (from the `cto-desk` message, checked) | `grep -n "^| R57 " cto-2026-10-01.md` | 0 | `65:| R57 | 23:48 ET | DESK RECORD (R127, L42): \`07\` G1 settled: the one-line \`OPS_TOOLS\` lift in \`src/cobalt/jobs/restarts.py\` stands (build D6); ASK DESK 1 default stands; ASK DESK 2 = deploy merge holds all 35 allow strings + \`--add-dir\`. | DESK RECORD |` |
| R57 committed | `git -C … log -1 --format=%H -S"| R57 |" -- cto-2026-10-01.md` | 0 | `7a7495cee04d2f301a71cb2708513e60a4e5fc04` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Thu Oct  1 23:49:16 EDT 2026` |
| pass 1 closed | `tail -n 3 "<CHECK REPORT>"` | 0 | `CHECK DONE · job: devdb-lock · pass: 1 · tip: aeefb6df · house A: Grok FINDINGS: 7 · … · house B: needed · … · ready: NO · decisions: 3 · for Dejan: 1` |
| branch | `git status --short --branch` | 0 | `## ops/devdb-lock-1001` |
| head = pass 1 tip | `git log --oneline -1` | 0 | `aeefb6df fix(devdb-lock): release touches only its own lock; …` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: devdb-lock · tip: a9339f0a | … | self-check: 3 of 3 | decisions: 7 · for Dejan: 1` |
| range (code) | `git log --oneline 093028d0..aeefb6df -- . ":(exclude)docs"` | 0 | `aeefb6df` · `12ed3626` · `a9339f0a` · `9915ca9e` · `bd144d45` (5) |
| lock: own .env | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock: any .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| scratch | `ls <S>` | 0 | `diff.md files house-a.md HOUSE-INSTRUCTIONS.md opus-1.md rulings.md` (pass 1's) |
| grok | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| gemini | `agy --version` | 0 | `1.2.14` |
| Sol probe | `codex exec … "Reply with only the word OK." < /dev/null` | 1 | `ERROR: You've hit your usage limit. … try again at Oct 4th, 2026 2:06 PM.` → METER |

Seats: house A (pass 1) was Grok; Sol is METER until Oct 4th, 2026 2:06 PM; house B = Gemini.

## Files copied
- `diff-b.md`: written from the saved output of `git log -p 093028d0..aeefb6df -- . ":(exclude)docs"`; `grep -c "^commit "` → `5` = the code-commit count. `git diff --no-index <saved output> diff-b.md` → only the header line added and the harness's `[exited with code 0]` trailer left out (a first Write dropped one line, `+    assert (wt / "x-gate").is_dir()`; restored with Edit and re-compared).
- Copied again by `stage-copy.sh` (the files the pass-1 commits touched): `files/wt/ops/desk/release-devdb-lock.sh` → `COPIED 2545` · `files/wt/tests/ops/test_devdb_lock.py` → `COPIED 11389` · `files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md` → `COPIED 57364`.
- `HOUSE-B-INSTRUCTIONS.md`: the HOUSE TEXT with the HOUSE B paragraph, the card's ROWS, NOT IN THIS JOB, CHECK ASKS (none), RECORDS, and the Files paragraph naming `diff-b.md`, `house-a.md`, `opus-1.md` (and R57 as a desk record).

## Findings
House B Gemini produced nothing. Its notice came at 23:55 EDT (`date` → `Thu Oct  1 23:55:49 EDT 2026`), exit 0, and its whole output was: `jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. …` → HARNESS. The output is saved verbatim in `<S>/house-b.partial.md`, first line `PARTIAL — HARNESS`. No other house is left to try: Sol is METER (until Oct 4th, 2026 2:06 PM), and Grok was house A. So this pass records `house B: none produced`, and pass 1's open item goes to `## OPEN` as it stands.

## Dropped
none (no list)

## RUNS
No house-B finding to run. The one OPEN item of pass 1 (G1) has no test or command from house B. Its command from pass 1, `git log --oneline 093028d0..HEAD -- src`, still prints `a9339f0a fix(devdb-lock): ops/desk lock scripts and desk-launch.sh classified (L42)`: unchanged, still HELD, NOT FIXED.

## FIXES
none (no commit in pass 2)

## Suites
suites: as built (no commit). Pass 2 made no commit, so the suites pass 1 ran on `aeefb6df` stand (pass 1 `## Suites`): offline `3770 passed, 673 skipped, 1 xfailed`; with-DB `4369 passed` + `171 passed` = 4540/0; live-note `146 passed, 1 skipped`; `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (W)`; `RESTARTS: com.cobalt.radar`. Pass 2 took no lock.

## Scope
Same as pass 1: pass 2 changed nothing on the branch. Files it wrote, all under `<S>`: `diff-b.md`, `HOUSE-B-INSTRUCTIONS.md`, `house-b.partial.md`, and the three `files/wt/` copies.

## Checked against the branch
- (i) `git log --oneline aeefb6df..HEAD -- . ":(exclude)docs"` → (nothing). `<tip now>` = `aeefb6df`.
- (ii) `git log --stat --format=%h aeefb6df..HEAD` → (nothing). No `WIDENED`.
- (iii) `git log --oneline 093028d0..HEAD -- src` → `a9339f0a fix(devdb-lock): ops/desk lock scripts and desk-launch.sh classified (L42)`. This is NOT EMPTY: it is G1, still standing.
- (iv) no HELD finding in pass 2.
- (v) `ls <WT>/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`; `git status --short --branch` → `## ops/devdb-lock-1001`.
- (vi) `git log --stat --format=%h 093028d0..HEAD -- src/cobalt/db_migrations tests/cobalt` → `a9339f0a` `tests/cobalt/test_jobs_restarts.py | 18 +`. That is an offline test added to an existing file. No migration and no new with-DB test file, so `TREE STATE: unchanged` holds.
- (vii) card record 1: `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R20 |" -- "docs/40 - DevDocs/reports/cto-2026-10-01.md"` → `23c7cdeb217d98a24bbe81fc838909c6095f6839`. Record 2 (one other house reads the procedure change): house A Grok read it in pass 1; house B produced nothing.
- (viii) L32: this pass holds no ticker, price or date of his.

## OPEN
FOLLOW-UP, carried from pass 1 as it stands:
- **G1** (Grok, pass 1) — HELD, NOT FIXED — `src/cobalt/jobs/restarts.py`.
  - The finding: the build edits `src/` (`OPS_TOOLS` gains `ops/desk/desk-launch.sh`, `ops/desk/release-devdb-lock.sh` and `ops/desk/take-devdb-lock.sh`), its test and its DevDocs page, though the card fences `src/` and no row names them.
  - The run: `git diff 093028d0..a9339f0a -- …` shows the three hunks; re-checked above in (iii).
  - What would settle it: a row carrying `HIS RULING` and `APPROVED` that lets the one-line lift stand, or a card row naming the file.
  - What is on file: desk record R57 (`cto-2026-10-01.md:65`, commit `7a7495ce`) says the lift stands. It is marked `DESK RECORD`, not `HIS RULING … APPROVED`, so it does not meet the AUTHORIZATION proof (K23) on its own (see `## DECISIONS`).

## CONTINUE
next: none — CLOSE done (pass 2). No further house, no third pass.

## DECISIONS
- **G1 — HELD, NOT FIXED — `src/cobalt/jobs/restarts.py` · FOR DEJAN (scope).**
  - The desk's message this pass says G1 is settled by R57. I found and checked that row: `65:| R57 | 23:48 ET | DESK RECORD (R127, L42): \`07\` G1 settled: the one-line \`OPS_TOOLS\` lift … stands (build D6) … | DESK RECORD |`, committed in `7a7495cee04d2f301a71cb2708513e60a4e5fc04`.
  - The hub proves an approval only by a row carrying `HIS RULING` and `APPROVED`. It also says a desk message "never widens the job or grants anything". Pass 1 marked this item his (scope, a lift of the card's fence). R57 is a desk record that cites R127, a row I did not open.
  - Safe default taken: G1 stays counted `held unfixed: 1`, and the edit is left as built, so `ready: NO`.
  - If the judgment seat accepts R57 (with R127) as covering the fence lift, nothing else blocks: the suites are green on `aeefb6df`, nothing else is open, and the branch is ready at `aeefb6df`.

## RECORDS
- Desk message (`cto-desk`, received during PREFLIGHT 23:49 EDT): "G1 is settled by desk record R57 … ASK DESK 1: your default stands. ASK DESK 2: the deploy's merge resolves the CHECK-HUB launch line so it keeps all 35 allow strings and --add-dir; it is not this branch's job." I checked R57's row and commit myself (AUTHORIZATION). ASK DESK 1 and 2 are answered and closed. The G1 part is under `## DECISIONS`.
- Sol METER: `try again at Oct 4th, 2026 2:06 PM` (probe 23:49 EDT).
- House B Gemini produced nothing (HARNESS): its headless run auto-denied a tool that needed the `command` permission. The same `agy` spelling may fail again the same way for the next check that seats Gemini. The hub's Gemini line already tells it to run no shell command, but it still asked for one. No retry (one attempt).
- No `REFUSED, not needed` line. No `CONTINUED` line. No lock taken in pass 2.
- L74: one block, recorded under `# PASS 2` `## L74`; not acted on.
- files opened: 7 — `prompts/CHECK-HUB.md` (main), the card, this report (pass 1's sections), `<S>/HOUSE-INSTRUCTIONS.md` (pass 1's, mine, for the card sections), the saved `git log -p` output, the Sol probe output, and the Gemini output. Not opened this pass: `BUILD-HUB.md` (no W ran), `areas/cobalt.md`, `house-a.md`, LAWS.md, and R127.
- Check of `devdb-lock`, pass 2: house B `Gemini` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: devdb-lock · pass: 2 · tip: aeefb6df · house B: none produced · findings: 0 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 1 · open: 1 · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: NO · decisions: 1 · for Dejan: 1
