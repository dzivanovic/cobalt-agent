# adoption-hubs — check, pass 1 (2026-10-03)

## §0 Headline
- Check pass 1 of `adoption-hubs`, with no outside house (overruled 2026-10-02 R47). 9 own findings: 2 held, 1 fixed, 1 held unfixed.
- Fixed (O2): `DEPLOY-HUB.md` G (f) named no rollback command, yet THE ONE RESUME types G (f) by hand. Now it names the ROLLBACK command of `gate-lists.md` and `<FP>` (red `b11bbe95`, fix `44c5bd6d`).
- Held, not fixed (O1): `preflight.sh` fails every build or check launched while another worktree holds `.env`. The hubs now stop on that row. The fix is a fenced script → DECISION 1.
- Suites on `44c5bd6d`: offline 3749/0, live-note 146/0, tests/ops 572/0; with-DB not run (DB: none). RESTARTS: none.
- ready: NO (held unfixed 1). 2 decisions, none for Dejan.

## L74
A system notice in this session offered a `Claude-Session:` commit trailer. It is recorded here once and was not acted on.

## AUTHORIZATION
(14:53 EDT)
- INSTALLED · `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` · exit 1 · (no output)
- CARD placeholder · `grep -n -E "«FIL[L]" ".../2026-10-03/02-adoption-hubs-card.md"` · exit 1 · (no output)
- CARD committed · `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02-adoption-hubs-card.md"` · `ec59a9cc7c9377ee12500e6ff7b0eb1e727b124d`; `git -C … diff --stat -- <card>` · (no output)
- STANDING LIST 2026-09-30 R60 · line 46 `| R60 | 15:15 ET | **HIS RULING** … APPROVES STANDING-LIST.md once … | APPROVED |` · `-S"| R60 |"` → `962e9d1705b62a61821f62f4d7bf5d8131656e2a`
- 2026-10-02 R47 · line 54 `… HIS RULING (direction row 10; L73 over L67 house A) … | HIS RULING · APPROVED |` · `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a`
- 2026-10-02 R154 · line 161 `… HIS RULING: a card with no src/, test, config or migration path takes no dev-DB lock … | HIS RULING · APPROVED |` · `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2`
- 2026-10-02 R157 · line 164 `… HIS RULING (B) … | HIS RULING · APPROVED |` · `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2`
- 2026-10-03 R3 · line 9 `… HIS RULING: every Grok seat runs grok-4.7 … | HIS RULING · APPROVED — pending fold |` · `3727a00454268f485f97fdeccb8f9cc428e86113`
- 2026-10-02 R38 · line 45 `… HIS RULING (direction row 1): the bare-command fix … | HIS RULING · APPROVED |` · `4e3fa8d8…`
- 2026-10-02 R39 · line 46 `… HIS RULING (direction row 2): permission by class … | HIS RULING · APPROVED |` · `4e3fa8d8…`
- 2026-10-02 R45 · line 52 `… HIS RULING (direction row 8) … | HIS RULING · APPROVED |` · `4e3fa8d8…`
- 2026-10-02 R46 · line 53 `… HIS RULING (direction row 9) … | HIS RULING · APPROVED |` · `4e3fa8d8…`
- HOUSE A overrule: the card header `HOUSE A: none — overruled 2026-10-02 R47` — R47 proved above. House gates: not run (HOUSE A none: "PREFLIGHT runs no house gate and no probe").

## PREFLIGHT
- `date` · 0 · `Sat Oct  3 14:53:43 EDT 2026`
- branch · `git status --short --branch` · 0 · `## ops/adoption-hubs-1003`
- tip · `git log --oneline -1` · 0 · `70144d6a docs(adoption-hubs): build report — e9aff772`; `git log --stat --format=%h e9aff772..HEAD` · 0 · `70144d6a` → `.../reports/adoption-hubs-build-2026-10-03.md | 52 +++…` (docs only)
- built · `tail -n 3 "<REPORT>"` · 0 · `BUILT · job: adoption-hubs · tip: e9aff772 | on 0a4a7743 | migration: none | offline 3749/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0`
- range · `git log --oneline 0a4a7743..e9aff772` · 0 · `e9aff772 fix(adoption-hubs): STEP-G calls gate.sh --deploy; …` / `f4ef3533 docs(adoption-hubs): build report — 1c349c49` / `1c349c49 feat(adoption-hubs): the fixed files call the step scripts; …` / `2502a3ad wip(adoption-hubs): red` (4 commits)
- range stat · `git log --stat --format=%h 0a4a7743..e9aff772` · 0 · e9aff772: DEPLOY-HUB.md; f4ef3533: build report; 1c349c49: BUILD-HUB.md, CARD.md, CHECK-HUB.md, CTO-DESK-WAKEUP.md, DEPLOY-HUB.md, DEVFIX-HUB.md, STANDING-LIST.md, tests/ops/test_gate.py, tests/ops/test_pass1_db_only.py; 2502a3ad: tests/ops/test_hub_lines.py
- lock (DB: none) · `ls <WT>/.env` · 1 · `ls: /Users/cobalt/cobalt-wt/adoption-hubs-1003/.env: No such file or directory`
- DB: none paths · `git diff --name-only --no-renames 0a4a7743..e9aff772` · 0 · `docs/40 - DevDocs/prompts/BUILD-HUB.md` `docs/40 - DevDocs/prompts/CARD.md` `docs/40 - DevDocs/prompts/CHECK-HUB.md` `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` `docs/40 - DevDocs/prompts/DEVFIX-HUB.md` `docs/40 - DevDocs/prompts/STANDING-LIST.md` `docs/40 - DevDocs/reports/adoption-hubs-build-2026-10-03.md` `tests/ops/test_gate.py` `tests/ops/test_hub_lines.py` `tests/ops/test_pass1_db_only.py` — every path under docs/ or tests/ops/
- scratch · `ls <S>` · 1 · `No such file or directory` (fresh)
- houses: `house A: none (overruled 2026-10-02 R47)` · house B: none available (no house gate, no probe run)

## Files copied
none (no house)

## OWN FINDINGS
Written before any run (house A: none — no house list exists to open).

FINDING O1
ROW: A1, A2 (CHECK ASK X1)
CLAIM: The new PREFLIGHT sentence (`BUILD-HUB.md:49`, `CHECK-HUB.md:63` at `e9aff772`) hands the lock rows to `preflight.sh`, whose `env anywhere` row fails on ANY `.env` under `/Users/cobalt/cobalt-wt/*/` (`ops/desk/preflight.sh:155-167`), and the hub then makes `FAILED PREFLIGHT: env anywhere` the last line. The same sentence says "another session may hold the lock; you wait for it at your with-DB step, L76", and LAUNCH launches a build or check "also while another session holds the `cobalt_dev` lock" (R20). A DB: none check used to run `ls <WT>/.env` only (R154). So a build or check launched while another job holds the lock now stops at PREFLIGHT. The fix is in `ops/desk/preflight.sh` (fenced: NOT IN THIS JOB) or a hub stop rule no row names.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_preflight.py::test_an_env_in_a_sibling_worktree_fails`
EXPECT: `1 passed` — the script ends `FAILED PREFLIGHT: env anywhere` (exit 1) when only a sibling worktree holds `.env`.

FINDING O2
ROW: A3 (CHECK ASK X1)
CLAIM: `DEPLOY-HUB.md` THE ONE RESUME (`:53`) says a resume that finds `<GATE>/.env` must "run G (f) for it (the rollback to `0013` …)", and the first-use table (`:73`) says CLASS (b) is "typed only by THE ONE RESUME's G (f)". But A3's G (f) (`:107`) no longer names a command: "every applied migration reversed, newest first; `<F2>` MUST EQUAL `<F0>`". The file holds no `--rollback` command at all. BUILD-HUB W (f) names "the ROLLBACK command of `ops/desk/gate-lists.md`"; the deploy's G (f) does not. A resume worker would have to guess the command (L1).
RUN: TEST `tests/ops/test_hub_lines.py`
```python
def test_the_deploy_gate_f_names_the_rollback_a_resume_types_by_hand():
    """THE ONE RESUME runs G (f) by hand when it finds <GATE>/.env: G (f) must name what it types."""
    text = (HUBS / "DEPLOY-HUB.md").read_text(encoding="utf-8")
    step_g = text.split("\n## STEP-G ", 1)[1].split("\n## ", 1)[0]
    (f,) = [ln for ln in step_g.splitlines() if ln.startswith("- (f) ")]
    assert "the ROLLBACK command of" in f and "ops/desk/gate-lists.md" in f, f
    assert "`<FP>`" in f, f
```
EXPECT: `AssertionError` on the first assert; the (f) line holds neither phrase.

FINDING O3
ROW: X2
CLAIM: A sentence outside `gate.sh` still tells a worker to type a with-DB `pytest`, a `migrate`, `cp .env` or `rm .env`, beyond what build DECISION 1 records (judge: KEEP): the launch strings, the first-use row, and E2's with-DB red.
RUN: COMMAND `grep -n -F "COBALT_ENV=dev uv run pytest" "docs/40 - DevDocs/prompts/BUILD-HUB.md"` (and the same over `CHECK-HUB.md`, `DEPLOY-HUB.md`; then `grep -n -F "db migrate"` over the three)
EXPECT: if true, a hit outside line 12/61/68 of BUILD-HUB, outside the launch line of CHECK-HUB, or outside the launch line, the first-use row and the resume note of DEPLOY-HUB.

FINDING O4
ROW: X3, A4
CLAIM: A launch line carries a string a class covers, or a class string not byte-equal to `STANDING-LIST.md` `## CLASSES` (a) and (b).
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py`
EXPECT: if true, a red in `test_each_line_carries_the_two_class_strings_once_and_no_string_they_replace`.

FINDING O5
ROW: X5, A4
CLAIM: `desk-launch.sh` does not pass the flag through unchanged (the `$(…)` literal or the quotes) for some kind.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py -k launch`
EXPECT: if true, a red in a dry launch of one of the four kinds or in the real launch.

FINDING O6
ROW: X6, A5
CLAIM: `TREE STATE` is still demanded by `desk-launch.sh` (`ops/desk/desk-launch.sh:507-509`); no hub, `CARD.md` or `preflight.sh` demands it.
RUN: COMMAND `grep -n -F "TREE STATE" ops/desk/desk-launch.sh`
EXPECT: lines 507 and 509 (the refuse). Card RECORDS (R95): card `03c` makes `TREE STATE` optional → OUT OF SCOPE here.

FINDING O7
ROW: X4, A3
CLAIM: The equal-tree clause can be passed by a two-branch set, by a difference outside `docs/` or by a DB: none check line.
RUN: COMMAND `grep -n -F "THE EQUAL-TREE CLAUSE" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: if true, the clause line lacks `ONE branch in TIP`, the `":(exclude)docs"` pathspec, or the with-DB-count condition.

FINDING O8
ROW: A4 (X3)
CLAIM: `STANDING-LIST.md` `## THE LOCK SCRIPTS` (`:48-49`) still says the two `/Users/cobalt/.claude/ops/` lock-script strings stand "on the build, check and deploy lines"; after A4 no line carries them (CLASS (a) replaces them). A4 names only the `## CLASSES` section, §1–§6 and the header counts, so the sentence was left as it stands.
RUN: COMMAND `grep -n -F "on the build, check and deploy lines" "docs/40 - DevDocs/prompts/STANDING-LIST.md"`
EXPECT: one hit at line 48.

FINDING O9
ROW: A7 (X1)
CLAIM: `desk-launch.sh`'s deploy reminder (`ops/desk/desk-launch.sh:966`) still tells the desk "their with-DB steps wait for the lock the gate holds to its stop line", the hold A7 removed. `desk-launch.sh` is fenced.
RUN: COMMAND `grep -n -F "holds to its stop line" ops/desk/desk-launch.sh`
EXPECT: one hit at line 966.

## Findings
none (house A: none)

## Dropped
none

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_preflight.py::test_an_env_in_a_sibling_worktree_fails`; then `grep -n -F "you wait for it at your with-DB step" ".../BUILD-HUB.md"` and `grep -n -F "none under" ".../CHECK-HUB.md"` | `1 passed, 15 warnings in 0.93s` (the script ends `FAILED PREFLIGHT: env anywhere`, exit 1, when only a sibling worktree holds `.env`); the hub sentences at `BUILD-HUB.md:47` ("`ls -la /Users/cobalt/cobalt-wt/*/.env` (another session may hold the lock; you wait for it at your with-DB step, L76). Its last line `PREFLIGHT OK` (exit 0) → go on; else its `FAILED PREFLIGHT: <what>` is your last line") and `CHECK-HUB.md:61` (the same, "none under `/Users/cobalt/cobalt-wt/*/`"). (The finding cited :49 / :63; the greps put them at :47 / :61.) | HELD, NOT FIXED — `ops/desk/preflight.sh` (NOT IN THIS JOB: "no script … A script that does not do what a hub sentence needs → DECISION <row>") |
| O2 | Opus | the test added to `tests/ops/test_hub_lines.py`, alone | `1 failed, 15 warnings in 0.82s` · `E       AssertionError: - (f) THE L76 RELEASE, on green or red, from the moment (c2) returned: every applied migration reversed, newest first; \`<F2>\` MUST EQUAL \`<F0>\` field for field. Record the gate's \`cobalt_dev: 0013 — F2 = F0\`.` at `tests/ops/test_hub_lines.py:117` | HELD |
| O3 | Opus | `grep -n -F "COBALT_ENV=dev uv run pytest"` BUILD-HUB; `grep -c -F` the same over CHECK-HUB, DEPLOY-HUB; `grep -n -F "db migrate"` BUILD-HUB, CHECK-HUB; `grep -c -F "cp /Users/cobalt/cobalt/.env"` BUILD-HUB | BUILD-HUB: lines 12 (launch line), 61 (first-use row), 68 (E2's with-DB red) — build DECISION 1, judge KEEP; CHECK-HUB `1` (launch line); DEPLOY-HUB `1` (launch line); `db migrate`: BUILD-HUB line 68 only (E2's proof-only), CHECK-HUB none; `cp …/.env` BUILD-HUB `1` (launch line). The lock's judgment text stands (`BUILD-HUB.md` THE LOCK, held-lock exits 4 and the stop). | NOT HELD |
| O4 | Opus | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py` (before O2's fix) | `1 failed, 18 passed` — the one red is O2's own test; every class-string, deny, flag and Grok test passed | NOT HELD |
| O5 | Opus | the same run (the whole file, `-k launch` not separated) | `test_a_dry_launch_of_each_kind_prints_a_line_holding_the_flag[build|check|deploy|devfix]` and `test_a_real_launch_hands_the_session_the_flag_byte_for_byte` among the 18 passed | NOT HELD |
| O6 | Opus | `grep -n -F "TREE STATE" ops/desk/desk-launch.sh` | `507:    case "$(field "TREE STATE")" in` · `509:        *) refuse "incomplete card: TREE STATE must be 'unchanged' or 'row <id>'" ;;`; no hit in BUILD/CHECK/DEPLOY/DEVFIX/CARD/STANDING-LIST or `preflight.sh` (Grep tool over `docs/40 - DevDocs/prompts` and `ops/desk`) | OUT OF SCOPE — card RECORDS (R95): "card `03c` … carries … `TREE STATE` optional"; `desk-launch.sh` is fenced |
| O7 | Opus | `grep -n -F "THE EQUAL-TREE CLAUSE" ".../DEPLOY-HUB.md"` | `99:THE EQUAL-TREE CLAUSE (before (a)): ONE branch in TIP, and \`git -C /Users/cobalt/cobalt diff --stat <its check's code tip> <m1> -- . ":(exclude)docs"\` prints nothing → … The clause applies only when the check's stop line carries a with-DB count above 0; a DB: none single branch runs the gate whole.` — all three conditions present | NOT HELD |
| O8 | Opus | `grep -n -F "on the build, check and deploy lines" ".../STANDING-LIST.md"` | `48:## THE LOCK SCRIPTS (L76 as amended: his 2026-10-01 R20 approves these two strings only) — on the build, check and deploy lines` | REJECTED — the card: "THE RULE OF THIS CARD: a sentence is changed only when a row names it"; A4 names `## CLASSES`, §1–§6 and the header counts, not `## THE LOCK SCRIPTS` |
| O9 | Opus | `grep -n -F "holds to its stop line" ops/desk/desk-launch.sh` | `966:    note="reminder: no desk commit on main until the stop line; builds and checks may launch, their with-DB steps wait for the lock the gate holds to its stop line (L76, R20); …"` | OUT OF SCOPE — NOT IN THIS JOB: "`desk-launch.sh` (reads the lines from the hub files; its own checks are card `21`'s)" |

No test's form was repaired.

## FIXES
| id | commit | file | change | proof |
|---|---|---|---|---|
| O2 | red `b11bbe95` `wip(adoption-hubs): check red — O2` · fix `44c5bd6d` `fix(adoption-hubs): DEPLOY-HUB G (f) names the rollback and fingerprint a resume types by hand (check O2)` | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (A3's file; STEP-G (f)) | one sentence appended to G (f): by hand, only THE ONE RESUME's G (f) with `<GATE>/.env` present — the ROLLBACK command of the merged tree's `ops/desk/gate-lists.md` (FOREGROUND, timeout 600000, read with the Read tool, typed byte for byte), then `<FP>` → `<F2>` equal to the log's `F0:` line; unequal → `DECISION 0` | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_hub_lines.py tests/ops/test_gate.py tests/ops/test_pass1_db_only.py` → `61 passed, 15 warnings in 17.68s` |

No DevDocs module page: the change is a fixed prompt file, which has no page under `docs/40 - DevDocs/cobalt/` (the build added none either).

## Suites
On `44c5bd6d` (DB: none; W (a0), (a), (e) and tests/ops as `main`'s BUILD-HUB W (a0) gives them):
- RESTARTS · `uv run cobalt jobs restarts 0a4a7743..HEAD` · 0 · the eleven rows, each `DOCS` or `test/documentation; no resident`, restart `-`; `RESTARTS: none`.
- (a0) · `git diff --name-only --no-renames 0a4a7743` · 0 · the 11 paths of PREFLIGHT, every one under `docs/` or `tests/ops/` → `cobalt_dev: not taken (DB: none — 11 paths)`.
- (a) offline · `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) · 0 · `3749 passed, 746 skipped, 1 xfailed, 36 warnings in 597.05s (0:09:57)`; `grep -c -E "^(FAILED|ERROR) "` on the output → `0`.
- (e) live-note · `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · 0 · `146 passed, 1 skipped, 15 warnings in 28.49s`; the one skip `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (none names `COBALT_LIVE_VAULT_ROOT`).
- tests/ops · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) · 0 · `572 passed, 1 xfailed, 15 warnings in 204.78s (0:03:24)` (the build's 571 plus O2's test).
- with-DB: not run (DB: none); no lock taken. `.env`: `ls /Users/cobalt/cobalt-wt/adoption-hubs-1003/.env` → `No such file or directory` (15:09 EDT); `git status --short --branch` → `## ops/adoption-hubs-1003`.
- O2's test was shown red first (`## RUNS` O2) and passes after the fix.

## Scope
PREFLIGHT's path union (11 paths, all under `docs/` or `tests/ops/`) plus my two commits: `tests/ops/test_hub_lines.py` (row A4/A6's test file) and `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (rows A3, A7, A8). Outside every row's `files` and inside `tests/ops/`: `tests/ops/test_gate.py`, `tests/ops/test_pass1_db_only.py` (the build's ASK DESK 1, decision 10, judge KEEP). Nothing under the fence.

## Checked against the branch
- (i) `git log --oneline e9aff772..HEAD -- . ":(exclude)docs"` → `b11bbe95 wip(adoption-hubs): check red — O2`. My fix `44c5bd6d` touches only `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, which this pathspec excludes. On this branch the hub files are the code: the card's own `TIP: e9aff772` is a DEPLOY-HUB-only commit. So `<tip now>` = `44c5bd6d` (see RECORDS).
- (ii) `git log --stat --format=%h e9aff772..HEAD` → `44c5bd6d` DEPLOY-HUB.md `1 insertion(+), 1 deletion(-)`; `b11bbe95` tests/ops/test_hub_lines.py `9 insertions(+)`; `70144d6a` the build report. Every path is in a row's `files` (A3, A4) or is a report.
- (iii) `git log --oneline 0a4a7743..HEAD -- ops/desk/desk-launch.sh ops/desk src configs ".../BRAIN-HUB.md" ".../JUDGE-HUB.md" ".../JUDGE-CARD.md" ".../CLOSE-HUB.md"` → (no output).
- (iv) `grep -n -F "def test_the_deploy_gate_f_names_the_rollback_a_resume_types_by_hand" tests/ops/test_hub_lines.py` → `112:def test_the_deploy_gate_f_names_the_rollback_a_resume_types_by_hand():`; `b11bbe95` (red) sits below `44c5bd6d` (fix) in `git log --oneline 0a4a7743..HEAD`.
- (v) see `## Suites`.
- (vi) `git log --stat --format=%h 0a4a7743..HEAD -- src/cobalt/db_migrations tests/cobalt` → (no output): no migration and no with-DB test, so there is nothing for the gate lists to carry.
- (vii) The card's `## RECORDS` name no `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command: nothing to run.
- (viii) L32: this report holds no ticker, price or date of his; the test uses no value.

## OPEN
COUNTING: findings 9 (O1–O9; no house) · dropped 0 · held 2 (O1, O2) · fixed 1 (O2) · held unfixed 1 (O1) · open 2 (O1, O8) · out of scope 2 (O6, O9).
- O1 — HELD, NOT FIXED — `ops/desk/preflight.sh`. A build or check launched while another worktree holds `.env` stops `FAILED PREFLIGHT: env anywhere`, against LAUNCH ("also while another session holds the `cobalt_dev` lock") and against the sentence's own "you wait for it at your with-DB step". A DB: none check (R154) stops the same way. It would be settled by a script row of the shape `03c` M1 has: `env anywhere` printed as information, not a failing rule (or failing only for a `## W`-bound probe), plus a `tests/ops/test_preflight.py` case: a sibling `.env` → `PREFLIGHT OK`. Or by a hub sentence that names that row as not a stop, which no row of this card names.
- O8 — REJECTED (the card's rule). `STANDING-LIST.md:48` `## THE LOCK SCRIPTS` still says the two `/Users/cobalt/.claude/ops/` strings stand "on the build, check and deploy lines"; no line carries them after A4. It would be settled by a row naming that section (one heading line, and its first sentence to say CLASS (a) carries the scripts at the repo path).
- OUT OF SCOPE: O6 (`desk-launch.sh:507-509` demands `TREE STATE`; card `03c`, R95), O9 (`desk-launch.sh:966` deploy reminder still says the gate holds the lock to its stop line; the launcher is fenced, card `21`'s).

## CONTINUE
next: none (pass 1 closed 15:09 EDT; the judgment seat reads ## DECISIONS)

## DECISIONS
1. HELD, NOT FIXED — O1 (rows A1, A2) — `ops/desk/preflight.sh` fails every build or check launched while another worktree holds `.env`. The hubs now call `preflight.sh build|check` for their mechanical PREFLIGHT rows. Its `env anywhere` row (`ops/desk/preflight.sh:155-167`) fails on any `/Users/cobalt/cobalt-wt/*/.env`. The hub then makes `FAILED PREFLIGHT: env anywhere` the last line (`BUILD-HUB.md:47`, `CHECK-HUB.md:61` at `44c5bd6d`). Before this branch, both hubs quoted `ls -la /Users/cobalt/cobalt-wt/*/.env` and went on ("another session may hold the lock; you wait for it at your with-DB step, L76"). LAUNCH still launches them "also while another session holds the `cobalt_dev` lock" (R20). A DB: none check used to run `ls <WT>/.env` only (R154 lock relief). Proof: `## RUNS` O1 (`tests/ops/test_preflight.py::test_an_env_in_a_sibling_worktree_fails` → `1 passed`). Card `03c` M1 fixes the `status` row only; nothing on file routes this one. Safe default: not fixed (the script is fenced; the hub sentence is A1's/A2's words as ordered). It needs a script row, routed by the judge like build decision 2 (to `03c` or a follow-up). Until then, the desk launches builds and checks on this hub only while no `.env` stands, or expects `FAILED PREFLIGHT: env anywhere` and sends `CONTINUE` once the lock is free.
2. OPEN — O8 (row A4) — `STANDING-LIST.md:48` heading `## THE LOCK SCRIPTS … — on the build, check and deploy lines` names the two `/Users/cobalt/.claude/ops/` strings that A4 took off every line. The card's rule kept the sentence; the approval file now says something no line does. Safe default: left as written. It needs one row (the heading and the first sentence of that section) on a later card.
House B: none available (HOUSE A: none — overruled 2026-10-02 R47; no outside house sits for this card). The two open items above ship to the follow-up list unless the judgment seat orders otherwise.

## RECORDS
- Check of `adoption-hubs`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).
- started 14:53:43 EDT (`date`).
- No house ran: `## 1` and `## 3` not run; no file under `<S>`, so no `opus-1.md` (there is no house B to read it).
- `<tip now>` = `44c5bd6d`. `## 7` (i)'s pathspec `":(exclude)docs"` shows only `b11bbe95`, because this card's code is the fixed files under `docs/40 - DevDocs/prompts/`. The card's own `TIP` (`e9aff772`, DEPLOY-HUB.md only) follows the same reading. So the newest commit that changes a row's file is the tip.
- L74: a system notice in this session offered a second commit trailer line (`Claude-Session: …`). Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- Dropped: none. REFUSED: none. CONTINUED: none. Lock takes: none (DB: none).
- The suites ran from the main `CHECK-HUB.md`'s `## 6` for a DB: none card: W (a0), (a), (e) and `tests/ops`, typed, as `main`'s BUILD-HUB W (a0) gives them. This session's line carries no `ops/desk/*` string, so `gate.sh` was not called.
- files opened: 15 — `prompts/CHECK-HUB.md` (main), the card, the diff `0a4a7743..e9aff772` (saved tool output), the build report, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `prompts/BUILD-HUB.md` (main: THE LOCK, E2, RESTARTS, W), `ops/desk/preflight.sh`, `tests/ops/test_preflight.py`, `ops/desk/gate.sh` (header), `ops/desk/authorize.sh` (header), `ops/desk/house-probe.sh` (header), `ops/desk/stage-set.sh` (header), `prompts/STANDING-LIST.md` (tip, lines 1–55), `ops/desk/desk-launch.sh` (190–219, 900–989), `prompts/DEPLOY-HUB.md` (tip, line 107).

CHECK DONE · job: adoption-hubs · pass: 1 · tip: 44c5bd6d · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 2 · fixed: 1 · held unfixed: 1 · open: 2 · house B: none available · suites: offline 3749/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: NO · decisions: 2 · for Dejan: 0
