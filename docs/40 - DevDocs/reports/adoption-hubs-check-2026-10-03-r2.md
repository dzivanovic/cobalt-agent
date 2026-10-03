# adoption-hubs — CHECK, pass 1 (re-check, R108) — 2026-10-03

CARD: `docs/40 - DevDocs/prompts/2026-10-03/02-adoption-hubs-card.md` (on `main` at `a8139661`) · BRANCH `ops/adoption-hubs-1003` · BASE `0a4a7743` · TIP `6251baeb` · HOUSE A: none — overruled 2026-10-02 R47 · DB: none.

## §0 Headline
Rows A1–A10 read at `6251baeb`: A9 (`preflight.sh` lists a sibling's `.env` as information, fails on this worktree's) and A10 (THE LOCK SCRIPTS names class (a)) are built and tested as the card says.
Two findings of mine hold, and neither can be fixed inside this card. O1: `gate.sh` exits 4 at once on a sibling's `.env`, but BUILD-HUB says W's take waits for the lock. That is the A9 defect in the other script. O2: STANDING-LIST §3 still puts the lock scripts under `.claude/ops`.
No fix commit, so the suites stand as built. `ready: NO` (held unfixed 2). Both items are under `## DECISIONS` for the judge seat. Neither is for Dejan.

## L74
One block arrived (a system reminder in this session, not a tool result) asking that commit messages end with a `Claude-Session:` line. Recorded here once, not acted on: this check made no commit, and per L74 its commits would carry only `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## AUTHORIZATION
Started `Sat Oct  3 15:31:07 EDT 2026`.

| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/02-adoption-hubs-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02-adoption-hubs-card.md"` | 0 | `a81396614c6562c507091ef2040fd5dfe11b74f4` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST 09-30 R60 | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C … log -1 --format=%H -S"\| R60 \|" -- cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 10-02 R47 (and HOUSE A overrule) | grep | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house … \| HIS RULING · APPROVED \|` · commit `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 10-02 R154 | grep | 0 | `161:\| R154 \| 17:29 ET \| HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock … \| HIS RULING · APPROVED \|` · commit `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| 10-02 R157 | grep | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|` · commit `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| 10-03 R3 | grep | 0 | `9:\| R3 \| 06:09 ET \| HIS RULING: every Grok seat runs grok-4.7 … \| HIS RULING · APPROVED — pending fold \|` · commit `3727a00454268f485f97fdeccb8f9cc428e86113` |
| 10-02 R38 | grep | 0 | `45:\| R38 \| 07:57 ET \| HIS RULING (direction row 1): the bare-command fix, all three parts … \| HIS RULING · APPROVED \|` · commit `4e3fa8d8…` |
| 10-02 R39 | grep | 0 | `46:\| R39 \| 07:57 ET \| HIS RULING (direction row 2): permission by class — sh …/ops/desk/* everywhere; COBALT_ENV=dev uv run cobalt db * on build/check/devfix/deploy, production denied on the first three; each kind's report glob … \| HIS RULING · APPROVED \|` · commit `4e3fa8d8…` |
| 10-02 R45 | grep | 0 | `52:\| R45 \| 07:57 ET \| HIS RULING (direction row 8): a single-branch deploy whose code equals its checked tip takes the check's suite lines … \| HIS RULING · APPROVED \|` · commit `4e3fa8d8…` |
| 10-02 R46 | grep | 0 | `53:\| R46 \| 07:57 ET \| HIS RULING (direction row 9): a set with an empty restart set and no migration deploys at any hour … \| HIS RULING · APPROVED \|` · commit `4e3fa8d8…` |
| house gate R17 | `grep -n "^\| R17 " cto-2026-09-24.md` | 0 | `35:\| R17 \| 07:32 ET \| … STANDING: Bash(grok *) is a PRE-APPROVED string … \| APPLIED: … \|` |
| house gate R19 | `grep -n "^\| R19 " cto-2026-09-24.md` | 0 | `37:\| R19 \| 07:36 ET \| … STANDING: the four house strings are pre-approved … \| APPLIED: … \|` · commit `5055151dbf68899b82de5b11f99733ed2d03048c` |

AUTHORIZED.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 15:31:07 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/adoption-hubs-1003` |
| tip | `git log --oneline -1` | 0 | `5d3f2817 docs(adoption-hubs): build report — 6251baeb (stop line)` |
| docs-only above tip | `git log --stat --format=%h 6251baeb..HEAD` | 0 | `5d3f2817` / `662901d5`: only `docs/40 - DevDocs/reports/adoption-hubs-build-2026-10-03.md` |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: adoption-hubs · tip: 6251baeb \| on 0a4a7743 \| migration: none \| offline 3749/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 10 of 10 \| self-check: 3 of 3 \| decisions: 4 · for Dejan: 0` |
| range | `git log --oneline 0a4a7743..6251baeb` | 0 | 9 commits: `6251baeb` fix A9 A10 · `641984f5` wip red A9 · `44c5bd6d` fix check O2 · `b11bbe95` wip check red O2 · `70144d6a` docs · `e9aff772` fix A3 amended A7 A8 · `f4ef3533` docs · `1c349c49` feat A1–A6 · `2502a3ad` wip red |
| range stat | `git log --stat --format=%h 0a4a7743..6251baeb` | 0 | path union below |
| lock (DB: none) | `ls <WT>/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/adoption-hubs-1003/.env: No such file or directory` |
| siblings | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| DB: none paths | `git diff --name-only --no-renames 0a4a7743..6251baeb` | 0 | `docs/40 - DevDocs/prompts/BUILD-HUB.md` · `CARD.md` · `CHECK-HUB.md` · `CTO-DESK-WAKEUP.md` · `DEPLOY-HUB.md` · `DEVFIX-HUB.md` · `STANDING-LIST.md` · `docs/40 - DevDocs/reports/adoption-hubs-build-2026-10-03.md` · `ops/desk/preflight.sh` · `tests/ops/test_gate.py` · `tests/ops/test_hub_lines.py` · `tests/ops/test_pass1_db_only.py` · `tests/ops/test_preflight.py` — every path under `docs/`, `ops/` or `tests/ops/` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | house A: none (overruled 2026-10-02 R47): no house gate run in PREFLIGHT, no probe. HOUSE B: as needed. |

## Files copied
none (no house).

## OWN FINDINGS
Written from the read of `## WHAT YOU READ` (2)–(5) before any run (no house list exists: house A none, R47).

FINDING O1
ROW: A1 (and X1, X2)
CLAIM: `BUILD-HUB.md:34` makes THE LOCK "the rule `ops/desk/gate.sh` enforces at `## W`", and LAUNCH (`BUILD-HUB.md:8`) says a build "takes the lock only at its with-DB steps and waits for it there", but `ops/desk/gate.sh` (header, "any .env is a held lock (exit 4, nothing run)", and `take()`) exits 4 at once on a sibling's `.env` and never reaches the waiting take script; so at W a sibling holding the lock ends the build `FAILED: W — cobalt_dev lock not free` instead of waiting (the same class as A9, in the other script).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py::test_a_sibling_env_is_a_held_lock_and_no_uv_runs`
EXPECT: `1 passed` — the pinned behaviour: exit 4 with a sibling `.env`, no call made, no wait.

FINDING O2
ROW: A4 / A10 (STANDING-LIST)
CLAIM: `docs/40 - DevDocs/prompts/STANDING-LIST.md:156` (§3, the deploy list's PATHS sentence) still says the `.claude/ops` root is on the line "for the two lock scripts", while A10's section (`:49`) now says the scripts are called at the repo path and the symlinks are no string's path.
RUN: COMMAND `grep -n -F "for the two lock scripts" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: one line, `156:`, holding `` (`/Users/cobalt/.claude/ops` for the two lock scripts) ``.

## Findings
none (no house).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_gate.py::test_a_sibling_env_is_a_held_lock_and_no_uv_runs` | `1 passed, 15 warnings in 0.83s` (the test asserts `returncode == 4` and `read_calls(calls) == []` with a sibling `.env`, `tests/ops/test_gate.py:368-375`). Beside it: `grep -n -F "any .env is a held lock" ops/desk/gate.sh` → `26:# THE LOCK: \`ls -la $WT/*/.env\` first — any .env is a held lock (exit 4, nothing run). Then`; `grep -n -F "and waits for it there" ".../BUILD-HUB.md"` → `8:After the card is committed on \`main\`, also while another session holds the \`cobalt_dev\` lock: a build takes the lock only at its with-DB steps and waits for it there (THE LOCK; …)` | **HELD, NOT FIXED — `ops/desk/gate.sh`**: a sibling's `.env` makes W exit 4 at once, while THE LOCK (which A1's first sentence says `gate.sh` enforces) waits 90 min. The fix is a script edit, which the card fences: "A script that does not do what a hub sentence needs → `DECISION <row>`, never a script edit here" (only A9's `preflight.sh` is open to edit). |
| O2 | Opus | `grep -n -F "for the two lock scripts" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` | `156:Deny (7; R62): … PATHS: every absolute path above sits under one of the five roots (\`/Users/cobalt/.claude/ops\` for the two lock scripts); …` | **HELD, NOT FIXED — `STANDING-LIST.md:156`**: the sentence contradicts `:49` (scripts at the repo path; the symlinks are no string's path). No row names it, and the card says: "a sentence is changed only when a row names it; a sentence you think wrong goes under `## DECISIONS`". |

No test was added (both findings were settled by a listed command; no test file changed), so nothing was removed and no red commit was made.

## FIXES
none (both held findings lie outside what the rows let this check edit; `## DECISIONS`).

## Suites
No commit of mine → the build's lines stand (`suites: as built (no commit)`), quoted from `<REPORT>` `## W THE THREE SUITES`, RE-ISSUE 2 at `6251baeb`:
- (a0) `cobalt_dev: not taken (DB: none — 13 paths)`.
- offline `3749 passed, 746 skipped, 1 xfailed, 36 warnings in 573.84s (0:09:33)`.
- live-note `146 passed, 1 skipped, 15 warnings in 26.77s` (the skip names `COBALT_TEST_LIVE_DRC`, none names `COBALT_LIVE_VAULT_ROOT`).
- tests/ops `574 passed, 1 xfailed, 15 warnings in 196.92s (0:03:16)`.
- with-DB: not run (DB: none). `.env`: `ls /Users/cobalt/cobalt-wt/adoption-hubs-1003/.env` → `No such file or directory` (mine, PREFLIGHT and `## 7` (v)).
- RESTARTS (build report `## RESTARTS`, re-issue 2): `RESTARTS: none`, no UNCLASSIFIED row.

## Scope
PREFLIGHT's path union (13 paths, every one under `docs/`, `ops/` or `tests/ops/`) against the rows' files: the seven prompt files → A1–A6, A10 (`CTO-DESK-WAKEUP.md` A4); `ops/desk/preflight.sh`, `tests/ops/test_preflight.py` → A9; `tests/ops/test_hub_lines.py` → A4, A6; `tests/ops/test_gate.py`, `tests/ops/test_pass1_db_only.py` → test files (both inside `tests/ops/`, inside the fence's allowance); the build report → docs. My commits: none.

## Checked against the branch
| # | command | output |
|---|---|---|
| (i) | `git log --oneline 6251baeb..HEAD -- . ":(exclude)docs"` | (nothing): no commit of mine; `<tip now>` = `6251baeb` |
| (ii) | `git log --stat --format=%h 6251baeb..HEAD` | `5d3f2817`, `662901d5`: the build report only (PREFLIGHT) |
| (iii) | `git log --oneline 0a4a7743..HEAD -- ops/desk/desk-launch.sh src configs ops/desk/job-run.sh ops/desk/deploy-step0.sh ops/desk/deploy-outage.sh ops/desk/deploy-smoke.sh` | (nothing) |
| (iii) | `git log --oneline 0a4a7743..HEAD -- ".../BRAIN-HUB.md" ".../JUDGE-HUB.md" ".../JUDGE-CARD.md" ".../CLOSE-HUB.md"` | (nothing) |
| (iv) | — | no HELD finding was fixed; no test to find |
| (v) | `ls /Users/cobalt/cobalt-wt/adoption-hubs-1003/.env` · `git status --short --branch` | `No such file or directory` · `## ops/adoption-hubs-1003` |
| (vi) | `git log --stat --format=%h 0a4a7743..HEAD -- src/cobalt/db_migrations tests/cobalt` · `git log --oneline 0a4a7743..HEAD -- ops/desk/gate-lists.md` | (nothing) · (nothing): no migration, no with-DB test; TREE STATE: unchanged holds |
| (vii) | — | no card `## RECORDS` line names an `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command (the one command named, `git diff --name-only <BASE>`, is the build's W (a0), quoted in `## Suites`) |
| (viii) | — | L32: this report holds constructed values and repo facts only; no ticker, price or date of his |

COUNT: findings 2 (O1, O2; no house) · dropped 0 · held 2 · fixed 0 · held unfixed 2 · open 2.

## OPEN
- O1 — HELD, NOT FIXED — `ops/desk/gate.sh`. The run that settles it: a `tests/ops/test_gate.py` test in which a sibling `.env` is removed while `gate.sh <wt> withdb` waits must end green, with exit 0 and its calls made. That needs the take to wait (`take-devdb-lock.sh <wt> 90`, as THE LOCK states it) and not to stop on `ls $WT/*/.env`. The existing `test_a_sibling_env_is_a_held_lock_and_no_uv_runs` would then change. The fix belongs to a scripts card (`03` / `03c`) or a follow-up row, as the card's RECORDS route it.
- O2 — HELD, NOT FIXED — `STANDING-LIST.md:156`. Settled by a row that names the sentence: `(`/Users/cobalt/cobalt` for the scripts)`, then `grep -c -F "for the two lock scripts"` → `0`.

## CONTINUE
next: none (pass 1 closed; house A none, overruled 2026-10-02 R47; house B none available)

## DECISIONS
- DECISION A1 (check O1), HELD, NOT FIXED, outside this card's files. `ops/desk/gate.sh:26` and `take()` treat any `$WT/*/.env` as a held lock and exit 4 at once (pinned by `tests/ops/test_gate.py:368`, run green here). The hubs say otherwise. `BUILD-HUB.md:8` says a build "waits for it there", and `:34` (A1) says THE LOCK, whose take WAITS 90 min, is "the rule `ops/desk/gate.sh` enforces". So at W, a build whose sibling holds the lock stops at once with `FAILED: W — cobalt_dev lock not free` and needs a desk `CONTINUE: W`. It does not wait. This is A9's defect (his 10-01 R20: the take waits), here in `gate.sh`. Safe default taken: nothing edited (the fence bars a script edit here). The build's W text for exit 4 stands and is safe (nothing held). For the judge seat: route it to `03` / `03c` or to a follow-up row.
- DECISION A10 (check O2), HELD, NOT FIXED, a sentence no row names. `STANDING-LIST.md:156` (§3 deploy PATHS) still reads "(`/Users/cobalt/.claude/ops` for the two lock scripts)", which contradicts A10's `:49`. Safe default taken: not edited (THE RULE OF THIS CARD). One word-level row would fix it.
- house B: none available (HOUSE A: none, overruled 2026-10-02 R47; no outside house this card). Both open items are listed here and ship to the follow-up list unless the judge seat routes them.

## RECORDS
- Dropped findings: none (no house list).
- Houses: house A none, overruled 2026-10-02 R47 (row quoted under `## AUTHORIZATION`); no house gate run in PREFLIGHT, no probe, no `<S>` staging. `<S>` is created only for `opus-1.md` (`## 8`).
- REFUSED, not needed: none. CONTINUED: none. Lock takes: none (DB: none).
- The stop line's `cobalt_dev` field reads `not taken`, not `0013`: this card is DB: none, and the check never touched `cobalt_dev`. This is the sentence A2 adds to `CHECK-HUB.md` (lock-relief build DECISION 6). The installed `CHECK-HUB.md` on `main` does not carry it yet.
- Earlier findings of this branch's first check (`reports/adoption-hubs-check-2026-10-03.md`) were not read (CHECK-HUB `## WHAT YOU READ` NOT-list). The card's RECORDS R104/R108 answers bind (D1 → A9, D2 → A10, decisions 14–15 KEEP), and none of them was reopened (L77). The A1/A2 `grep -c -F "COBALT_ENV=dev uv run pytest"` counts (`3` / `1`, the launch strings A4 keeps) are the build's DECISION A1, answered KEEP (R95: 1, 8, 10, 11 KEEP).
- Other reads that held nothing: `authorize.sh:195-207` proves a `HOUSE A` / `HOUSE B` overrule (A2's sentence). `stage-set.sh:168` prints `STAGED <n> files · <total> bytes · commits <k>` (A2). `house-probe.sh:95,107` print `<house>: OUT — …` (A2). `grep -rn ".claude/ops/(take|release)-devdb"` over the prompts finds only a 10-01 card, no hub (X2/X3). `ops/desk/take-devdb-lock.sh` and `release-devdb-lock.sh` are at the repo path (class (a)). TREE STATE is still required only by `ops/desk/desk-launch.sh:507,509` (X6; build DECISION A5, card `03c`). The allow/deny counts were re-counted from the four lines: build 26/4, check 30/4, devfix 19/4, deploy 56 with one head and a migration.
- files opened: 23. Read / `git show` / `git diff`, 11: `CHECK-HUB.md` (main); the card; the saved diff `0a4a7743..6251baeb` (prompts, ops, tests); the build report (`## RESTARTS` → last line); `ops/desk/preflight.sh`; `tests/ops/test_hub_lines.py`; `ops/desk/authorize.sh` (lines 185–209); `tests/ops/test_gate.py` (360–384); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `gate.sh` at BASE; the `test_preflight.py` diff. grep only, 12: `BUILD-HUB.md`, `CHECK-HUB.md` (worktree), `CARD.md`, `DEPLOY-HUB.md`, `STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `stage-set.sh`, `house-probe.sh`, `cto-2026-09-24.md`, `cto-2026-09-30.md`, `cto-2026-10-02.md`, `cto-2026-10-03.md`.
- Check of `adoption-hubs`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: adoption-hubs · pass: 1 · tip: 6251baeb · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 0 · held unfixed: 2 · open: 2 · house B: none available · suites: as built (no commit) · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 23 · ready: NO · decisions: 3 · for Dejan: 0
