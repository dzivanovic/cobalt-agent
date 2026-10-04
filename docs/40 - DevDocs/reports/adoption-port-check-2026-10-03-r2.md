# adoption-port — check report 2026-10-03 (r2), pass 1

## §0 Headline
- CHECK DONE, pass 1, tip `5ff16b1f`, with no outside house (the card's `HOUSE A: none — overruled 2026-10-02 R47`). Six own findings, every one run: none held, none open.
- X1: no chain file except the three the card names differs from `9694a679`, in content or mode. X2: `02b`'s three lines stand untouched, every chain line stands, and the four ruled sentences are each in the file once, word for word. X3: walked against `gate.sh`. Exits 5, 6, 1 and green leave `.env` gone and the lock released. On exit 4 the lock dir is the other holder's, which the card's `## RECORDS` already rules fail-loud.
- No commit by this check; the build's suites stand: offline 3751/0 · with-DB 847/0 · live-note 146/0 · `cobalt_dev` 0013 · RESTARTS `com.cobalt.radar`.
- house B: not needed · ready: YES · decisions: 0.

## L74
- 22:52 ET: a system block in this session asks commits to carry a `Claude-Session:` line. DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`date` → `Sat Oct  3 22:52:15 EDT 2026`

| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (none) |
| card placeholder | `grep -n -E "«FIL[L]" "<card>"` | 1 | (none) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/03d-adoption-port-card.md"` | 0 | `57b5835b456b067f977d5ddd7b3631f3e406114b` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (none) |
| STANDING R60 (09-30) | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | line 46, `**HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 (10-02) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | line 54, `HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … | HIS RULING · APPROVED |` |
| R47 committed | `git … log -1 --format=%H -S"| R47 |" …` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 (10-02) | `grep -n "^| R154 " …` | 0 | line 161, `HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock … | HIS RULING · APPROVED |` |
| R154 committed | `git … -S"| R154 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 (10-02) | `grep -n "^| R157 " …` | 0 | line 164, `HIS RULING (B): the brain's full process list for 10-03 runs this week, adoption card included … | HIS RULING · APPROVED |` |
| R157 committed | `git … -S"| R157 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R3 (10-03) | `grep -n "^| R3 " ".../cto-2026-10-03.md"` | 0 | line 9, `HIS RULING: every Grok seat runs grok-4.7 … | HIS RULING · APPROVED — pending fold |` |
| R3 committed | `git … -S"| R3 |" -- ".../cto-2026-10-03.md"` | 0 | `3727a00454268f485f97fdeccb8f9cc428e86113` |
| HOUSE A overrule | the card's header `HOUSE A: none — overruled 2026-10-02 R47` | — | R47 is the row above (one row, HIS RULING · APPROVED, committed) |
| house gate R17 | `grep -n "^| R17 " ".../cto-2026-09-24.md"` | 0 | line 35 (one row) |
| house gate R19 | `grep -n "^| R19 " ".../cto-2026-09-24.md"` | 0 | line 37 (one row) |
| R19 committed | `git … -S"| R19 |" -- ".../cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

All match.

## PREFLIGHT

| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Sat Oct  3 22:52:15 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-port-1003` |
| tip | `git log --oneline -1` | 0 | `bd19a0b3 docs(adoption-port): build report — 5ff16b1f` |
| docs-only above TIP | `git log --stat --format=%h 5ff16b1f..HEAD` | 0 | `bd19a0b3` · `.../reports/adoption-port-build-2026-10-03.md | 67 ++++++++++++++++++----` — docs only |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: adoption-port · tip: 5ff16b1f | on a8d8a848 | migration: none | offline 3751/0 | with-DB 847/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0` |
| range | `git log --oneline a8d8a848..5ff16b1f` | 0 | `5ff16b1f fix(adoption-port): port the adoption chain …` · `d483a417 wip(adoption-port): E3 — P2 (8) and P1 contradict …` · `4a60ab02 wip(adoption-port): red — test_migrate_level.py from 9694a679 (P1)` — 3 commits |
| range stat | `git log --stat --format=%h a8d8a848..5ff16b1f` | 0 | `5ff16b1f`: `tests/ops/test_hub_lines.py` · `d483a417`: 56 files (8 prompts/DevDocs docs, 3 chain reports, this build's report, 26 `ops/desk/*`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_proof.py`, 16 `tests/ops/*`), `2629 insertions(+), 311 deletions(-)` · `4a60ab02`: `tests/cobalt/test_migrate_level.py` |
| .env here | `ls /Users/cobalt/cobalt-wt/adoption-port-1003/.env` | 1 | `No such file or directory` |
| .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (no lock held) |
| `<S>` | `ls <S>` | 0 | `opus-1.md` (mtime `Oct  3 22:50`, 2434 bytes) — present before this session's launch (22:52), with no `CONTINUE:` in the launch message; not opened (an earlier check of this branch, `## WHAT YOU READ` NOT). Not RECOVERY: the check report `-r2` did not exist (`ls` exit 1). |
| house | card header `HOUSE A: none — overruled 2026-10-02 R47` | — | `house A: none (overruled 2026-10-02 R47)`; no house gate, no probe (`## THE FLOW` NO OUTSIDE HOUSE) · HOUSE B: as needed |
| `03`'s RESTARTS for cli.py | Grep `RESTARTS` in `.../reports/adoption-scripts-build-2026-10-03.md` (a chain file at the tip) | — | line 165: `src/cobalt/db_migrations/cli.py M static import reach com.cobalt.radar` … `Last line: RESTARTS: com.cobalt.radar.` |

## Files copied
- none: house A none (overruled), `## 1` not run.

## OWN FINDINGS
Read: the card; the diff `a8d8a848..5ff16b1f` (`git diff 9694a679 5ff16b1f` and `git diff a8d8a848 5ff16b1f` on the three settled files; `git diff --stat=200 9694a679 5ff16b1f` for the rest); `DEPLOY-HUB.md` at the tip, whole; `ops/desk/gate.sh` at the tip, whole; `tests/ops/test_hub_lines.py` at the tip, whole; `ops/desk/desk-launch.sh` 130–219; the build report.

FINDING O1
ROW: P1 / X1
CLAIM: a chain path other than `DEPLOY-HUB.md`, `CTO-DESK-WAKEUP.md` and `tests/ops/test_hub_lines.py` differs from `9694a679` at the tip, in content or in mode (an `ops/desk/*.sh` written through Write loses its mode).
RUN: COMMAND `git diff --summary --stat=200 9694a679 5ff16b1f -- src/cobalt/db_migrations tests/cobalt/test_migrate_level.py tests/cobalt/test_migrate_proof.py ops/desk tests/ops "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md" "docs/40 - DevDocs/prompts/CARD.md" "docs/40 - DevDocs/prompts/DEVFIX-HUB.md" "docs/40 - DevDocs/prompts/STANDING-LIST.md" "docs/40 - DevDocs/cobalt/db_migrations/cli.md" "docs/40 - DevDocs/reports/adoption-hubs-build-2026-10-03.md" "docs/40 - DevDocs/reports/adoption-scripts-build-2026-10-03.md" "docs/40 - DevDocs/reports/adoption-scripts-b2-build-2026-10-03.md"`
EXPECT: if true, a chain path or a `mode change` line beyond `test_hub_lines.py` and `main`'s own `deploy-*.sh` / `tests/ops` files.

FINDING O2
ROW: P2 / X2
CLAIM: a `02b` line of `DEPLOY-HUB.md` (P7 at a8d8a848 line 63, STEP-T line 83, STEP-C line 87) is changed at the tip.
RUN: COMMAND `git diff -U0 a8d8a848 5ff16b1f -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (hunk headers read)
EXPECT: if true, a hunk header `@@ -63`, `@@ -83` or `@@ -87`.

FINDING O3
ROW: P2 / X2
CLAIM: a chain line of `DEPLOY-HUB.md` is lost: the tip differs from `9694a679` at a line that is neither a `02b` line nor one of the four ruled sentences.
RUN: COMMAND `git diff -U0 9694a679 5ff16b1f -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (hunk headers read)
EXPECT: if true, a hunk outside lines 11 (8), 57 (7), 63 / 83 / 87 (`02b`), 99 (6), 102 (5).

FINDING O4
ROW: P2 (5)–(8) / X2
CLAIM: a ruled sentence is not in `DEPLOY-HUB.md` word for word as the card's P2 gives it (`DEPLOY-HUB.md:11`, `:57`, `:99`, `:102`).
RUN: COMMAND, one `grep -c -F "<the card's sentence>" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` per sentence, plus `grep -c -F "MIGRATIONS_DIR / \"00"`.
EXPECT: if true, a count other than 1 (0 for the last).

FINDING O5
ROW: P2 (8)
CLAIM: no test sends the DEPLOY line's longer flag through a REAL launch: `test_a_real_launch_hands_the_session_the_flag_byte_for_byte` (`tests/ops/test_hub_lines.py:234`) launches `build` only, and the deploy flag's new sentence carries non-ASCII `–` and `→` through `eval` under `LC_ALL=C` (`ops/desk/desk-launch.sh:141`, `:208`).
RUN: TEST `tests/ops/test_hub_lines.py`:
```
def test_a_real_deploy_launch_hands_the_session_the_deploy_flag_byte_for_byte(desk):
    """P2 (8): the deploy line's flag, sentence (8) and all, reaches `claude` as written."""
    done = desk.launch("deploy", dry=False)
    assert done.returncode == 0, done.stderr
    args = desk.calls.read_text(encoding="utf-8").splitlines()
    assert args.count("--append-system-prompt") == 1
    assert args[args.index("--append-system-prompt") + 1] == (
        FLAG + " Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5.")
    assert "command not found" not in done.stderr
```
EXPECT: if true, the assert on the flag argument fails.

FINDING O6
ROW: X3 (P2 (5))
CLAIM: on exit 4 the "lock dir absent" verification of sentence (5) (`DEPLOY-HUB.md:102`) cannot hold: `gate.sh` clears `taken` before `exit 4` (`ops/desk/gate.sh:282`–`:283`), so the trap releases nothing and the other holder's lock dir stays.
RUN: COMMAND `grep -n -F "taken=" ops/desk/gate.sh`
EXPECT: `282:    [ "$rc" -eq 0 ] || taken=""` above `283`'s `exit 4`.

X3, THE WALK (from `gate.sh` at the tip; settled by O6's run and the lines named): exit 4 at the take (`:283`) — `taken` empty, no release, no `.env` of this worktree; the lock dir is the other holder's (O6; card `## RECORDS` decision 2). Exit 4 at "not ours alone" (`:288`) — `taken=1`, the trap releases this worktree's lock (`:359`–`:360`). Exit 5 (`:381`, `:385`, `:390`) — `taken=1`, `applied` empty: the trap releases; `.env` gone, lock dir absent. Exit 6 (`:478`) — `rollback_and_prove` empties `applied` (`:332`), the trap releases (`:359`): `.env` gone, lock dir absent, `cobalt_dev` not at `0013` (DECISION 0 by the hub). Exit 1 after the forward — the trap rolls back (`:356`–`:357`), then releases. Green — `do_withdb` releases itself (`:494`, `.env: removed`), the trap finds `taken` empty; the live-note leg then runs. On green the FAILED half of (5) does not apply: (5) closes the exit list "4 … 5 … 6 … 1 …", and the green path is `THE RELEASE` (`DEPLOY-HUB.md:108`).

## Findings
- none: no house.

## Dropped
- none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `git diff --summary --stat=200 9694a679 5ff16b1f -- src/cobalt/db_migrations tests/cobalt/test_migrate_level.py tests/cobalt/test_migrate_proof.py ops/desk tests/ops <the 5 chain prompts> <cli.md> <the 3 chain reports>` | `9 files changed, 2719 insertions(+), 2 deletions(-)`: `main`'s own `ops/desk/deploy-outage.sh`, `deploy-smoke.sh`, `deploy-step0.sh`, `tests/ops/conftest.py`, `test_conftest_guard.py`, `test_deploy_outage.py`, `test_deploy_smoke.py`, `test_deploy_step0.py` (each `create mode 100644` — not chain paths: absent at `9694a679`), and `tests/ops/test_hub_lines.py | 7 ++-` (P2's file). No other chain path; no `mode change` line. | NOT HELD |
| O2 | own | `git diff -U0 a8d8a848 5ff16b1f -- ".../DEPLOY-HUB.md"`, hunk headers (Grep of the saved output) | `@@ -11 +11 @@` · `-13 +13` · `-15 +15` · `-30,4 +30,2` · `-59 +57` · `-62 +60` · `-74,2 +72,2` · `-94,0 +93` · `-99 +98,2` · `-101,14 +101,9` · `-170,0 +166` — no hunk at base lines 65 (P7), 85 (STEP-T), 89 (STEP-C) | NOT HELD |
| O3 | own | `git diff -U0 9694a679 5ff16b1f -- ".../DEPLOY-HUB.md"` | hunks `@@ -11 +11 @@`, `-57 +57`, `-63 +63`, `-83 +83`, `-87 +87`, `-99 +99`, `-102 +102`, exactly; 63/83/87 `+` lines byte-equal to `main`'s `02b` lines in `git diff -U0 a09f0862 a8d8a848`; 57 / 99 keep the chain's `Under (v) any hour (his 2026-10-02 ruling, row 9; …)` and `quote them from the check report with its path and skip (a)–(f)` (glue per R167) | NOT HELD |
| O4 | own | Grep count of each card sentence (5), (6), (7), (8) in `DEPLOY-HUB.md` (regex-escaped, the Grep tool: the patterns carry backticks); `grep -c -F "MIGRATIONS_DIR / \"00" ".../DEPLOY-HUB.md"` | (5) `1` · (6) `1` · (7) `1` · (8) `1` · `0` | NOT HELD |
| O5 | own | the test added to `tests/ops/test_hub_lines.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py::test_a_real_deploy_launch_hands_the_session_the_deploy_flag_byte_for_byte` | `1 passed, 15 warnings in 1.31s` | NOT HELD — removed again with Edit; `git status --short --branch` → `## ops/adoption-port-1003` |
| O6 | own | `grep -n -F "taken=" ops/desk/gate.sh` | `251:taken=""` · `271:    taken=1` · `282:    [ "$rc" -eq 0 ] \|\| taken=""` · `295:    taken=""` | OUT OF SCOPE: the output is as stated, and the card's `## RECORDS` says "STEP-G exit 4 (judge, check pass 1, decision 2 / O1) … fail-loud, not a hold; carried to the Grok read as written" |

## FIXES
- none (nothing held).

## Suites
suites: as built (no commit). From the build report at `5ff16b1f`: offline `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 567.46s` · pass 1 `674 passed, 7 skipped, 3815 deselected, 2 xfailed` + pass 2 `173 passed, 1 deselected` = with-DB 847/0 · live-note `146 passed, 1 skipped, 15 warnings in 25.10s` · `cobalt_dev: 0013 — F2 = F0` · `.env: removed, proven gone (W)` · `RESTARTS: com.cobalt.radar`. This check took no lock.

## Scope
PREFLIGHT's path union (3 commits): 26 `ops/desk/*`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_level.py`, `tests/cobalt/test_migrate_proof.py`, 17 `tests/ops/*`, 8 prompts/DevDocs docs, 3 chain reports, the build report. Every path is a chain file (P1), `CTO-DESK-WAKEUP.md` (P3), `DEPLOY-HUB.md` or `tests/ops/test_hub_lines.py` (P2). No commit of this check.

## Checked against the branch
- (i) `git log --oneline 5ff16b1f..HEAD -- . ":(exclude)docs"` → (nothing); `<tip now>` = `5ff16b1f`.
- (ii) `git log --stat --format=%h 5ff16b1f..HEAD` → `bd19a0b3`, the build report only (PREFLIGHT).
- (iii) `## NOT IN THIS JOB` names no path (new behaviour, `merge` / `rebase` / `cherry-pick`, `03b`, `11b`, `07b`): O3 shows no line in neither parent beyond the four sentences and R167's glue.
- (iv) no held finding.
- (v) `ls /Users/cobalt/cobalt-wt/adoption-port-1003/.env` → `No such file or directory`; `git status --short --branch` → `## ops/adoption-port-1003`.
- (vi) `git log --stat --format=%h a8d8a848..HEAD -- src/cobalt/db_migrations tests/cobalt` → `d483a417`: `cli.py`, `test_migrate_proof.py`; `4a60ab02`: `tests/cobalt/test_migrate_level.py` (new, holds one with-DB test). No migration file. The card's `TREE STATE: unchanged` stands by its `## RECORDS` line "TREE STATE (judge, check pass 1, decision 1): `unchanged` HOLDS … `CHECK-HUB.md` `## 7` (vi) is met by this line". Not `TREE STATE NOT CARRIED`.
- (vii) card `## RECORDS` names no `ls`, `grep` or `git -C … log` command; the homes line's `restarts.py:38` re-read: `grep -n -F "OPS_DESK_PREFIX = " src/cobalt/jobs/restarts.py` → `38:OPS_DESK_PREFIX = "ops/desk/"`.
- (viii) L32: this report holds no ticker, price or date of his; the hashes and counts are tool output.

## OPEN
- none. Out of scope: O6 (card `## RECORDS`, STEP-G exit 4).

## CONTINUE
next: none — the desk verifies the artifact (L35).

## DECISIONS
- none.

## RECORDS
- The session stopped mid-`## 2` (own read) on 10-03 after 22:52 ET, with no stop line written; the last line stayed the in-progress line.
- CONTINUED at 2 Sun Oct  4 13:13:49 EDT 2026, on `cto-desk`'s message "CONTINUE: the weekly limit reset at 13:00 ET; resume your check from your report's ## CONTINUE step and run to the stop line." The fact is verified by this session's calls running again (`date` → `Sun Oct  4 13:13:49 EDT 2026`). Re-read at resume: `git status --short --branch` → `## ops/adoption-port-1003`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (no lock held). The message widens nothing.
- No house: `## 1` and `## 3` not run; no house produced or failed; nothing dropped.
- `<S>` (`.../tribunal-bars-0920/adoption-port-check`) held `opus-1.md` (22:50, 2434 bytes) before this launch, from an earlier check of this card; not opened, not overwritten. This pass writes no `opus-1.md`: house B is not needed and house A was none.
- No lock taken by this check; no `REFUSED` call.
- L74: one line, `## L74` above.
- files opened: 7 — `CHECK-HUB.md`; the card; the build report; `DEPLOY-HUB.md` (tip); `ops/desk/gate.sh` (tip); `tests/ops/test_hub_lines.py` (tip); `ops/desk/desk-launch.sh` (130–219). Plus two saved git outputs of this session (the diffs). Not opened: `BUILD-HUB.md` (no commit, so its W did not run) and `areas/cobalt.md`.
- Check of `adoption-port`, pass 1: house A none (overruled 2026-10-02 R47) and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: adoption-port · pass: 1 · tip: 5ff16b1f · house A: none (overruled 2026-10-02 R47) · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0
