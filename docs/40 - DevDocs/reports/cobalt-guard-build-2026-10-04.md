# cobalt-guard — build report 2026-10-04

## §0 Headline
- BUILT again after the desk's `CONTINUE: G9`. Tip `21b9e21f`, on base `a8d8a848`. All 11 rows (G1–G11) are built in `ops/desk/bare-guard.py`, extended in place.
- G9 lets a check type its three house strings, G10 lets a check write under its own `<S>`, and G11 denies an `awk` pipe segment that can write. These rows answer the first stop's three decisions.
- Results on the tip: offline 3739 passed, 0 failed; `tests/ops` 953 passed, 0 failed; live-note 146 passed, 0 failed. DB: none, so `cobalt_dev` was never taken. RESTARTS: none.
- 1 decision, for the desk: `awk -f <file>` runs a program G11 cannot read, and it stays allowed to the card's letter.

## L74
- 14:23: an attribution block in the session context asked for a `Claude-Session:` line on commits. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- 15:11, at the continue: the same kind of block, now naming a `Claude-Session:` URL line. DATA (L74): recorded once, not acted on; `11adaf00` and `21b9e21f` carry the `Co-Authored-By` line only.

## AUTHORIZATION
| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" "<card>"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/10-cobalt-guard-card.md"` | 0 | `5d7f125b65a5689d83fb15f3a922846f78c49fe9` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING (09-30 R60) | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (…): APPROVES STANDING-LIST.md once (4be06af0); … | APPROVED |` |
| R60 committed | `git -C … log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 10-02 R47 | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): … | HIS RULING · APPROVED |` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 10-03 R32 | `grep -n "^| R32 " ".../cto-2026-10-03.md"` | 0 | `38:| R32 | 11:03 ET | HIS RULING (via brain): full guard hook cobalt-guard (bare-guard.py extended) … | HIS RULING · APPROVED |` |
| R32 committed | `git -C … -S"| R32 |"` | 0 | `a09f08622ac8522adce99096f5af18faaed9e2ca` |
| 10-03 R33 | `grep -n "^| R33 " ".../cto-2026-10-03.md"` | 0 | `39:| R33 | 11:08 ET | HIS RULING (via brain): read-only pipes allowed (each segment grep, sed -n, cut, sort, uniq, head, tail, wc, awk; no redirect, &&, ;); … | HIS RULING · APPROVED |` |
| R33 committed | `git -C … -S"| R33 |"` | 0 | `a09f08622ac8522adce99096f5af18faaed9e2ca` |
| 10-03 R12 | `grep -n "^| R12 " ".../cto-2026-10-03.md"` | 0 | `18:| R12 | 07:32 ET | HIS RULING: every mod and hook card is checked by an Anthropic seat alone; … | HIS RULING · APPROVED — pending fold |` |
| R12 committed | `git -C … -S"| R12 |"` | 0 | `c32c93cb8ef290caddaaa6c767e0a970d8149a02` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sun Oct  4 14:23:41 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/cobalt-guard-1004` + `?? "docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md"` (this report, the hub's first Write) |
| base | `git log --oneline -1` | 0 | `a8d8a848 Merge branch 'main' into deploy/set2d-1003` |
| branch in repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/cobalt-guard-1004` | 0 | `a8d8a848 Merge branch 'main' into deploy/set2d-1003` |
| first launch | `git diff --stat a8d8a848` | 0 | (nothing) |
| base commit | `git show --stat a8d8a848` | 0 | `Merge: 7f0b2efa ffd0b1be` · `docs/40 - DevDocs/reports/deploy-set2d-1003.md \| 133 +++` · `1 file changed, 133 insertions(+)` |
| .env | `ls /Users/cobalt/cobalt-wt/cobalt-guard-1004/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/cobalt-guard-1004/.env: No such file or directory` |
| other .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| symbol | `grep -rn -F "bare-guard" ops tests src configs` | 0 | `ops/desk/bare-guard.py:2:# bare-guard.py — a Claude Code PreToolUse hook (his 2026-10-01 R45 part 1; card 17 A1).` · `tests/ops/test_bare_guard.py:1:…` · `tests/ops/test_bare_guard.py:17:GUARD = REPO / "ops" / "desk" / "bare-guard.py"` |
| symbol | `grep -n -F "def scan(" ops/desk/bare-guard.py` | 0 | `21:def scan(command):` |
| symbol | `grep -n -F "def main(" ops/desk/bare-guard.py` | 0 | `95:def main():` |
| READ | `grep -n -F "## OPERATIONS A HOOK CAN TAKE" ".../harness-mods-review-2026-10-03.md"` | 0 | `51:## OPERATIONS A HOOK CAN TAKE (his ask, 07:2x ET; …)` |
| READ | `grep -n -F "\| R31 " ".../cto-2026-10-03.md"` | 0 | `37:| R31 | 10:53 ET | DESK RECORD (his word via brain): a REFUSALS list for 10-03 …` ; list itself at line 178 (`grep -n -F "REFUSALS"`) |
| READ | `grep -n -F "ONE command per Bash call" ".../BUILD-HUB.md"` | 0 | `29:ONE command per Bash call, exactly a listed prefix: …` |
| READ | Read `CHECK-HUB.md` lines 47–50 | — | line 48 `ONE command per Bash call, …`; line 50 `Git writes as git add <explicit paths> then git commit -m "…" -m "Co-Authored-By: …" -- <paths> (never -A, ., a bare commit). …` |
| wc | `wc -l ops/desk/bare-guard.py tests/ops/test_bare_guard.py` | 0 | `117 ops/desk/bare-guard.py` · `122 tests/ops/test_bare_guard.py` |
| tail READ report | `tail -n 3 ".../harness-mods-review-2026-10-03.md"` | 0 | last line `- R71 (no new vendors) is not touched: this is the vendor we already run on.` |
| tail READ report | `tail -n 3 ".../cto-2026-10-03.md"` | 0 | last line `HANDOVER: predecessor d78e4549 → successor 95c9c899 at 17:28 ET` |
| RESTARTS | `uv run cobalt jobs restarts a8d8a848..HEAD` | 0 | `docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md A DOCS -` · `RESTARTS: none` (the only path is this untracked report) |
| hub launch lines read | `grep -n -F "claude --bg"` in CHECK-HUB, DEPLOY-HUB, DEVFIX-HUB, CTO-DESK-WAKEUP, 23-brain-judge; `grep -n -F "HUB.md" ops/desk/desk-launch.sh`; `grep -n -F "cd " ops/desk/desk-launch.sh` | 0 | kinds by hub (desk-launch.sh:416–419 `build`/`check`/`deploy`/`devfix`); deploy launches from `/Users/cobalt/cobalt` (line 46); check `<S>` and `<AGY>` (CHECK-HUB.md:5) |
| lock owner shape | Read `ops/desk/take-devdb-lock.sh` | — | line 47 `printf '%s\n' "$wt" > "$LOCK/owner"`; `COBALT_WT_ROOT` stands in for `/Users/cobalt/cobalt-wt` in tests (line 19) |

Card `## RECORDS` copied:
- His words: 11:03 ET "Make it Sunday."; 11:08 ET "Make it so. Allow read-only pipes."; mods and hooks are Anthropic tuning, no outside house. (re-read: R32 / R33 rows above.)
- Until this ships, every seat stays bare-command; the build lists the four read strings (`Bash(cut *)`, `Bash(sort *)`, `Bash(uniq *)`, `Bash(awk *)`) in `## RECORDS` for his one approval. The hook itself adds no string.

DB: none — no lock probe, no with-DB string used.

## E0 BASELINE
| run | summary |
|---|---|
| `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) | `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 587.54s (0:09:47)`: 0 failed, 0 errors |
| `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` | `146 passed, 1 skipped, 15 warnings in 28.54s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT` |

## E2 RED
I wrote the tests only, with no change to `ops/`. The added tests are in `tests/ops/test_bare_guard.py`:
- An autouse `roots` fixture sets `COBALT_WT_ROOT` and `COBALT_REPO_ROOT` to directories under tmp_path. This puts the ledger, the lock dir and the cards in tmp; the old cases also run under it.
- Each seat is constructed: a cwd plus a transcript in the real JSONL shape. The first `user` record is the launch message, a non-user record comes before it, and a later `CONTINUE` record comes after.
- Each card is constructed with WORKTREE, REPORT, CHECK REPORT and a `## ROWS` table whose `files` cell holds a `\|`.

Command: `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rfE tests/ops/test_bare_guard.py`
Result on the old guard: `255 failed, 106 passed, 15 warnings in 9.19s`.

Every red is the row not being built yet:
- G1: a read-only pipe is denied with `…this call contains a pipe \`|\`…`, and the pipe-into-`rm` / `sed -i` reds show only `a pipe \`|\`` (`assert '\`rm\`' in 'a pipe \`|\`'`).
- G2–G7: the deny cases get `assert 0 == 2`, because the old guard exits 0 for every call that is not compound.
- G8: there is no `.ledger`.

The 106 passes are the old cases plus the allow controls. Each allow control is shown red under its mutation in E3.

Commit: `78561316 wip(cobalt-guard): red — G1–G8 tests on the old guard`.

## E3 THE ROWS
All eight rows are in one file, `ops/desk/bare-guard.py`, which went from 117 to 680 lines. The tests are in `tests/ops/test_bare_guard.py`, which went from 122 to 778 lines.

The first green run was `361 passed`. I then made one fix of my own: a fixed file that the build's card names is still inside the build's fence, so the copy on main stays denied. I added one assertion for it, and the file still showed `361 passed, 15 warnings in 11.23s`.

THE MUTATIONS. Each was made with the Edit tool, run alone with `-k`, then undone with Edit.

| row | mutation | run | result |
|---|---|---|---|
| G1 | `if found == ["a pipe \`|\`"]:` → `if False:` | `-k g1` | `32 failed, 10 passed`. First: `test_g1_a_read_only_pipe_is_allowed[grep -n X f \| cut -f2-None]` `AssertionError: NOT A REFUSAL. … contains a pipe \`|\`.` |
| G1 sed | `if any(sed_writes(s) …)` → `if False:` | `-k g1` | `6 failed, 36 passed`. Every `\`sed\` with a \`w\` or \`e\` command or flag` case |
| G2 | `kind != "deploy"` → `kind == "deploy"` | `-k g2` | `24 failed, 7 passed`. Every non-deploy deny and every deploy allow |
| G3 | `is_env` → `return False` | `-k g3` | `70 failed, 7 passed`. Every verb, the Read tool and every seat |
| G3 allow control | reader-verb test dropped (any verb with `/.env`) | `-k g3_the_lock_steps` | `4 failed, 2 passed`: `ls -la`, `ls`, `cp`, `rm` |
| G4 | `kind in GIT_SHAPED` → `kind in ()` | `-k "g4 or desk_launch_in_a_worktree"` | `46 failed, 9 passed` |
| G4 allow control | → `kind is not None` | `-k g4` | First run: `2 failed, 52 passed`. The desk-commit-with-`--` test STAYED GREEN, because a worker passes it too. I added `test_g4_is_a_workers_rule_the_desk_and_the_brain_are_not_shaped` (a desk or brain `commit` without `--` is allowed), and the re-run gave `4 failed, 52 passed` |
| G5 | `deny = g5(s, full)` → `deny = None` | `-k "g5 or kind_ or g8_a_write"` | `48 failed, 12 passed` |
| G5 allow control | `named = kind == "build" and …` → `named = False and …` | `-k g5_a_build_whose_card` | `1 failed`: `AssertionError: route: a fixed file changes by a card row` |
| G6 | the stop-head test → `if True: return None` | `-k g6` | `7 failed, 2 passed` |
| G6 allow control | `owner and owner in names` → `owner` | `-k g6` | `1 failed, 8 passed`: `…lock_names_another_worktree_is_allowed` |
| G7 | `kind in WORKERS` → `kind in ()` | `-k "g7 or kind_ or g8"` | `31 failed, 29 passed` |
| G7 allow control | → `kind is not None` | `-k g7_the_desk` | `12 failed, 6 passed`: every desk and brain launch |
| G8 | the `ledger(event, rule, what)` call removed | `-k g8` | `3 failed, 2 passed`. First: `assert [] == ['G7', 'G1']` |
| G8 allow control | `except Exception` → `except ZeroDivisionError` in `ledger` | `-k g8` | `1 failed, 4 passed`: `test_g8_an_unwritable_ledger_still_denies` `assert 0 == 2` |

After the last undo, `git diff --stat` showed `ops/desk/bare-guard.py | 607 +++…`, `tests/ops/test_bare_guard.py | 8 +`, `2 files changed, 593 insertions(+), 22 deletions(-)`. That is the fix plus the test rewrite above, with no mutation left in.

`uv run pytest -q -p no:cacheprovider --color=no --tb=short -rfE tests/ops` gave `888 passed, 1 xfailed, 15 warnings in 247.64s`.

Commit: `28276443 feat(cobalt-guard): bare-guard.py extended in place — read-only pipes, seat kind, production, .env, git shape, write fence, dirty stop line, second session, ledger (G1–G8, L1, L3, L28)`.

DevDocs line: no page exists for `ops/desk/` under `docs/40 - DevDocs/cobalt/`. The only mention is in `jobs/restarts.md:48`, which classifies the folder. I created no page (see `## RECORDS`).

## RESTARTS
`uv run cobalt jobs restarts a8d8a848..HEAD`
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md	A	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No path is UNCLASSIFIED.

## W THE THREE SUITES
`<tip>` = `28276443`. The card is DB: none.
- (a0) `git diff --name-only --no-renames a8d8a848` returned `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py`. Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) gave `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 596.89s (0:09:56)`: 0 failed, 0 errors, the same counts as E0. This build adds no test under `tests/cobalt` or `tests/taxonomy`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) gave `888 passed, 1 xfailed, 15 warnings in 256.37s (0:04:16)`. This build's tests are all in `tests/ops/test_bare_guard.py`: 363 in the file, of which 254 are new parametrized ids.
- (e) live-note, with `.env` absent: `146 passed, 1 skipped, 15 warnings in 28.58s`. The skip is the same `COBALT_TEST_LIVE_DRC` one and does not name `COBALT_LIVE_VAULT_ROOT`.
- `ls /Users/cobalt/cobalt-wt/cobalt-guard-1004/.env` returned `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red for its named reason, by E2 on the old guard or by its E3 mutation. Each allow control was red under its own E3 mutation. The one control that stayed green, G4's desk commit, was strengthened with a new test, and that test went red. See the E2 summary and the E3 table.

(2) Every entry path of each rule is pinned by a test.
- Callers: `grep -rn -F "bare-guard" ops tests src configs` finds only the hook file and its test. The hook entry in `~/.claude/settings.json` is his install, outside this worktree and not read.
- Entry paths pinned per rule:
  - Bash single command, Bash pipe and Bash compound.
  - The Read tool for G3.
  - Write and Edit for G5 and G6.
  - Every seat kind: build, check, devfix, deploy, desk, brain, generic worker and unknown.
  - The kind cases: a build whose cwd is the repo, a desk launch in a worktree, a worktree with no transcript, the repo with no prompt, CLOSE-HUB, the launch message as text parts, a missing transcript file, and the check's cwd moved to `agy-trial`.
  - Edge inputs, which the old cases also cover: `< /dev/null`, quoted separators, `$(`, backticks, comments and a broken event.

(3) Every `file:line` and count in this report was re-read at the tip:
- `grep -n -F "def " ops/desk/bare-guard.py`: for example `80:def scan(command):`, `533:def bash_rules(command, s):`, `582:def g5(s, path):`, `615:def ledger(event, rule, what):`.
- `grep -n -F "if kind" ops/desk/bare-guard.py`: `540:` G2, `542:` G4, `544:` G7, `584:`/`593:`/`602:` G5.
- `wc -l`: 680 and 778.
- `git show --stat 28276443`.

## FOR THE CHECK
- `a8d8a848..28276443`, two commits:
  - `78561316 wip(cobalt-guard): red — G1–G8 tests on the old guard`
  - `28276443 feat(cobalt-guard): bare-guard.py extended in place — … (G1–G8, L1, L3, L28)`
- The reds, mutations and greens are in E2 and E3. The suites are in W.
  - with-DB suite: `not run (DB: none)`
  - `<F0>`/`<F1>`/`<F2>`: `not run (DB: none)`
  - lock taken and released: `not run (DB: none)`
- The RESTARTS table is in `## RESTARTS`. The records copied at PREFLIGHT are in `## PREFLIGHT`.

How the build reads the rows. Each of these is a choice I made, for the check to judge.
- **Seat kind.**
  - The hub file named in the first transcript `user` record decides `build`, `check`, `deploy` or `devfix`, whatever the cwd. The worktree comes from the card's `WORKTREE:`, so a check that has `cd`'d into `<AGY>` keeps its fence.
  - With no hub, the repo cwd plus `CTO-DESK-WAKEUP.md` means desk. The repo cwd plus a prompt under `prompts/20*/` means brain; drafter and tribunal seats launched that way are brains too.
  - A cwd under the worktree root with no hub means `worker`. Anything else is unknown, and an unknown seat meets only G1, G3 and G6 (X2).
- **G1.**
  - "First word" is the segment's raw first word, so `LC_ALL=C sort` is denied.
  - `sed` must carry `-n` (or `--quiet`/`--silent`). It is denied for `-i` or `--in-place`, `-f` or `--file`, an unknown option, a `w`/`W`/`e` command, an `s///` `w` or `e` flag, or a script the parser cannot read.
  - A single `sed -i` command is not a pipe, so it is left to the allow strings.
- **G2.** Plain text match over the whole command: `COBALT_ENV=production`, `--prod` as a whole word (`--prod=` included, `--products` not), `cobalt_brain`. This is a false-deny cost for X1: a non-deploy `grep -n -F "COBALT_ENV=production" <file>` is denied too; the Grep tool is the way around it.
- **G4.**
  - Applies to build, check, devfix and worker. It does not apply to deploy, since "a merge is the deploy hub's"; deploy types `merge --ff-only` and `reset --soft`.
  - `--output…` is denied on any git call.
  - A `commit` needs a real `--` token, so `-m "a -- b"` is still denied.
- **G5.**
  - A worker may write inside its card's worktree and to its card's own report path: `REPORT`, or `CHECK REPORT` for a check. The report path comes from op 10, "the rows' files, the report". Without it, the check's report on main (CHECK-HUB.md:12) and devfix's report (DEVFIX-HUB.md:41) would be denied at their first Write.
  - The brain may write under `reports/` and `prompts/20*/`. The desk has no fence except the fixed files.
  - A fixed file is any file directly under `…/docs/40 - DevDocs/prompts/`, or any `LAWS.md`. Only a build whose card's `## ROWS` `files` cell names it may write it, and still only inside its fence.
- **G6.**
  - Write content, or Edit `new_string`: the last non-blank line is tested.
  - "Dirty" means any of these: `<cwd>/.env` exists; `<worktree root>/<wt>/.env` exists for the card's worktree or the cwd's worktree; the lock's `owner` names either of them.
- **G7.** The first word is read past `NAME=value` words, as a basename, in every segment (so `grep … | claude` is denied too). Applies to every worker kind, including deploy.
- **G8.** One line per deny: `{"time", "cwd", "rule", "command"}`. For Write/Edit/Read the `command` field holds the path. It is the first 200 UTF-8 bytes. The session id is reduced to `[A-Za-z0-9._-]` and given a leading `_` if it starts with a dot.

X3, partly walked: BUILD-HUB and CHECK-HUB git writes carry `--`, and the lock steps use `ls -la`, `cp` and `rm` of `.env`, which are allowed. The two hub steps the rules deny are DECISIONS 1 and 2. The DEPLOY-HUB and DEVFIX-HUB step text was not walked line by line; only their launch lines were read.

## CONTINUE AT G9 (rows G9–G11)
The desk sent `CONTINUE: G9.` I verified the fact myself at 15:11 EDT:
- `git -C /Users/cobalt/cobalt log -3 --format=%H%x20%ci%x20%s -- "<card>"` → `abcb732b… 2026-10-04 15:11:11 -0400 docs(desk): R218-R227 set 3 deploy FAILED gate; card 10 G9-G11; …`. The card on main now has rows G9, G10 and G11.
- `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` → nothing. `grep -n -E "«FIL[L]" "<card>"` → nothing (exit 1).
- The desk records the rows cite, in `cto-2026-10-03.md`: `228:| R222 | 10-04 15:04 ET | RECORD: \`10\` BUILT \`28276443\`, 3 decisions (…); DESK RECORD: 1 and 2 → card rows G9 (check house calls) G10 (check scratch fence), build relaunch at G9 after set 3; 3 (\`awk\` can write) → his A/B; …` and `232:| R226 | 10-04 15:10 ET | DESK RECORD (brain, under R33): \`awk\` with \`system(\`, \`>\` or \`\|\` in its program is not read-only → card \`10\` row G11 denies it; on his veto list. | RECORD |`.
- `ls /Users/cobalt/cobalt-wt/cobalt-guard-1004/.env` → `No such file or directory`.

E2 RED (G9–G11). Tests only, in `tests/ops/test_bare_guard.py`. G7's deny test now covers build, devfix and deploy; the check kind moved to G9's own tests.
- `uv run pytest -q -p no:cacheprovider --color=no --tb=line -k "g9 or g10 or g11" tests/ops/test_bare_guard.py` on the G1–G8 guard → `16 failed, 55 passed, 357 deselected, 15 warnings in 2.73s`.
- G9: each house string from the check → `AssertionError: route: the desk launches` (`assert 2 == 0`).
- G10: the check's Write under its own `<S>` → `AssertionError: route: this seat writes only inside its fence (…)` (`assert 2 == 0`).
- G11: each awk-that-writes pipe → `assert 0 == 2` (the old guard lets it through).
- The deny cases of G9 and G10 and the allow cases of G11 passed on the old guard, as they should. Each is shown red under a mutation below.
- Commit: `11adaf00 wip(cobalt-guard): red — G9–G11 tests on the G1–G8 guard`.

E3 (G9–G11), all in `ops/desk/bare-guard.py`:
- G9: in `bash_rules`, the G7 test now lists the launcher segments. A check passes when the only launcher is segment 0 and the whole command opens with `HOUSE` (`grok `, `codex exec --skip-git-repo-check -m <slug> -s read-only `, `agy `; the slug is `[A-Za-z0-9._-]+`).
- G10: `read_card` also reads `JOB:`. In `g5`, a check may write under `<WT_ROOT>/agy-trial/scratch/tribunal-bars-0920/<JOB>-check`.
- G11: `awk_writes` reads every awk word except the values of `-F` and `-v` and the file of `-f`. A word holding `system(`, `>` or `|` adds `` `awk` with `system(`, `>` or `|` in its program `` to the pipe's problems.
- The whole file at the fix: `428 passed, 15 warnings in 13.18s`.

THE MUTATIONS (G9–G11). Each was made with Edit, run alone, then undone with Edit.

| row | mutation | run | result |
|---|---|---|---|
| G9 | `if kind == "check" and …` → `if False and …` | `-k "g9 or g7"` | `5 failed, 72 passed`: every `test_g9_the_check_types_each_house_string` id, `route: the desk launches` |
| G9 control: kind | `kind == "check"` → `kind in WORKERS` | `-k g9` | `16 failed, 21 passed`: every `…another_worker_kind_typing_a_house_string_is_denied` id and `…a_worker_with_no_hub…` |
| G9 control: one segment | `launches == [0]` → `launches` | `-k g9` | `2 failed, 35 passed`: `[grok -p x \| claude -p y]`, `[agy x \| agy y]` |
| G9 control: the prefix | `and HOUSE.match(command)` dropped | `-k g9` | `13 failed, 24 passed`: every `codex` without the full house prefix, `claude`, `/usr/local/bin/grok`, `FOO=1 grok`, `FOO=1 agy`, bare `grok` |
| G10 | `if kind == "check" and job …` → `if False and …` | `-k g10` | `2 failed, 11 passed`: `test_g10_the_check_writes_under_its_own_scratch[None]` and `[agy]`, the G5 fence route |
| G10 control: kind | `kind == "check"` → `kind in WORKERS` | `-k g10` | `3 failed, 10 passed`: `…another_kind_under_the_scratch_is_denied[build]`, `[devfix]`, `[deploy]` (the brain is denied by its own fence) |
| G10 control: one job | `under(path, …SCRATCH, job + "-check")` → `under(path, …SCRATCH)` with no `job` | `-k g10` | `7 failed, 6 passed`: every `…under_another_jobs_scratch_is_denied` id and `…a_check_card_with_no_job_has_no_scratch` |
| G11 | `if ws[0] == "awk" and awk_writes(…)` → `… and False and …` | `-k g11` | `9 failed, 12 passed`: every `test_g11_an_awk_segment_that_can_write_is_denied` id, `assert 0 == 2` |
| G11 control: option values | `("-F", "-v", "-f")` → `("-f",)` | `-k g11` | `8 failed, 13 passed`: the `-F'\|'`, `-F '\|'`, `-v 'x=>'`, `-vx='\|'` allow ids |

The G9 deny `grep -n X f | grok -p x` stays green under all three G9 mutations. G7 itself pins it, since the launcher is not segment 0.

After the last undo, `git diff --stat` showed `ops/desk/bare-guard.py | 50 ++++++++++++++++++----` plus this report. `git diff ops/desk/bare-guard.py` shows the fix and no mutation.

- The file at the fix: `uv run pytest -q -p no:cacheprovider --color=no --tb=short -rfE tests/ops` → `953 passed, 1 xfailed, 15 warnings in 252.99s (0:04:12)`.
- Commit: `21b9e21f feat(cobalt-guard): check house calls, check scratch fence, awk read-only (G9–G11, L1, L3, L72)`. No DevDocs page for `ops/desk/` (as at G1–G8, `## RECORDS`).

RESTARTS at the continue. `uv run cobalt jobs restarts a8d8a848..HEAD`
```
path	change	rule	restart
docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md	M	DOCS	-
ops/desk/bare-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_bare_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```

W at the continue. `<tip>` = `21b9e21f`. The card is DB: none.
- (a0) `git diff --name-only --no-renames a8d8a848` → `docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md`, `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py`. Every path is under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**
- (a) `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 584.81s (0:09:44)`: 0 failed, 0 errors. This build adds no test under `tests/cobalt` or `tests/taxonomy`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `953 passed, 1 xfailed, 15 warnings in 254.72s (0:04:14)`: 0 failed. This build's tests are all in `tests/ops/test_bare_guard.py`: 428 in the file, 65 of them added at the continue.
- `ls /Users/cobalt/cobalt-wt/cobalt-guard-1004/.env` → `No such file or directory`.
- (e) `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.61s`. The skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

PRE-STOP SELF-CHECK at the continue:
1. Every G9–G11 test was shown red, either by E2 on the G1–G8 guard or by a mutation or control in the table above. The one deny that no G9 mutation turned red, `grep -n X f | grok -p x`, is pinned by G7 itself, as noted under the table.
2. The entry paths G9–G11 open are each pinned by a test:
   - G9: the check in `<WT>` and in `<AGY>` (`cwd` param); build, devfix and deploy; a worker with no hub; a launcher at segment 0, later, or both; `NAME=` in front; an absolute path; the bare word; each prefix with one part missing or altered.
   - G10: Write and Edit; the check in `<WT>` and in `<AGY>`; another job, a longer job name, `..`, a sibling dir and the scratch root; build, devfix, deploy and brain; a card with no `JOB:`.
   - G11: `>`, `>>`, `system(`, `| "sh"`, `| getline`; `-F` and `-v` attached and detached; `--`; awk at the head of a pipe.
   - Callers: `bare-guard` has no Cobalt caller (PREFLIGHT grep).
3. Re-read at the tip:
   - `grep -n -F "HOUSE"` → `83:` and `573:`.
   - `grep -n -F "SCRATCH"` → `85:` and `633:`.
   - `grep -n -F "awk_writes"` → `371:` and `402:`.
   - `wc -l` → `714 ops/desk/bare-guard.py`, `922 tests/ops/test_bare_guard.py`.
   - `git log --oneline a8d8a848..HEAD` → five commits (below).

FOR THE CHECK at the continue:
- `a8d8a848..21b9e21f`:
  - `78561316 wip(cobalt-guard): red — G1–G8 tests on the old guard`
  - `28276443 feat(cobalt-guard): bare-guard.py extended in place — … (G1–G8, L1, L3, L28)`
  - `b31120b4 docs(cobalt-guard): build report — 28276443`
  - `11adaf00 wip(cobalt-guard): red — G9–G11 tests on the G1–G8 guard`
  - `21b9e21f feat(cobalt-guard): check house calls, check scratch fence, awk read-only (G9–G11, L1, L3, L72)`
- How the build reads the new rows. Each of these is a choice I made, for the check to judge.
  - **G9.**
    - "Prefix" is read on the whole command. A `NAME=` word, a path such as `/usr/local/bin/grok`, or leading whitespace means the call is not the house string.
    - The launcher must be segment 0 and the only launcher. A house call cannot be piped into another session.
    - `<slug>` is one word of `[A-Za-z0-9._-]`. Today's `gpt-5.6-sol` fits.
    - G1 still applies after G9. The Sol line passes by its exact ` < /dev/null` ending; a house call with `&&` is still denied.
  - **G10.**
    - `<JOB>` is the card's `JOB:` line, read with the same pattern as `WORKTREE:`.
    - `<S>` is built under the worktree root, `<WT_ROOT>/agy-trial/scratch/tribunal-bars-0920/<JOB>-check`. A card with no `JOB:` gives the check no `<S>`.
  - **G11.**
    - Only a pipe segment is read, as `sed -i` is: a single `awk` command is left to the allow strings.
    - Every awk word is read except the values of `-F` and `-v` and the file of `-f`, so a `>` in a comparison (`$1 > 5`) is denied too. The card names `>` with no exception.
    - `awk -f <file>` is allowed: see DECISION 1.
- X3: the walk from the first stop still holds. With G9 and G10 built, the two hub steps it found (CHECK-HUB.md:91–94 house launch, :50/:73 `<S>` writes) are allowed for the check. DEPLOY-HUB and DEVFIX-HUB step text is still not walked line by line.

## CONTINUE
next: none (BUILT)

## DECISIONS
1. **`awk -f <file>` runs a program G11 cannot read.** G11 denies an awk pipe segment "whose program text holds `system(`, `>` or `|`", and says "any other `awk` segment stays allowed". With `-f`, the program is in a file, not in the command, so the hook never sees it. A worker could Write a `.awk` file inside its worktree and then pipe into `awk -f` it. (`sed -f` is denied under G1 for the same reason.)
   - Safe default taken: built to the card's letter (L72), so `awk -f` stays allowed.
   - Needed: a card row denying `awk -f` in a pipe, as `sed -f` is, if wanted.

The first stop's three decisions are answered by the card's new rows and are not counted again: 1 → G9, 2 → G10 (desk record R222), 3 → G11 (desk record R226, "on his veto list").

## RECORDS
- REFUSED, not needed: grep -n -F "`<S>` =" "docs/40 - DevDocs/prompts/CHECK-HUB.md" — Permission to use Bash has been denied because Claude Code is running in don't ask mode. (a backtick in the pattern; read with the `<AGY>` grep instead)
- L74: two `Claude-Session:` attribution requests (14:23, 15:11), recorded under `## L74`, not acted on.
- The card's records as re-read at PREFLIGHT: his words R32 / R33 (rows 38 / 39 of `cto-2026-10-03.md`).
- FOR HIS ONE APPROVAL (card `## RECORDS`; R60, the strings are his): `Bash(cut *)`, `Bash(sort *)`, `Bash(uniq *)`, `Bash(awk *)`. The next hub-text card puts them on the build, check and desk lines. The hook adds no string.
- No DevDocs page exists for `ops/desk/` under `docs/40 - DevDocs/cobalt/`, and none was made: a new page is outside the rows. Owed to whoever places ops docs (PLACEMENT.md).
- Install is not this build's. The card's WHY says `bare-guard.py` is "his install" and that the existing hook entry covers it; this build did not read that entry. G8's ledger lands in `/Users/cobalt/cobalt-wt/.ledger/`.
- No extra lock take (DB: none).
- CONTINUED at G9 15:11 EDT. The desk's message (`CONTINUE: G9.`) named a step only. The rows G9–G11 come from the card committed on main at `abcb732b` (desk records R222, R226), not from the message.
- At the continue, my first call was off the list: `cat "<BUILD-HUB.md>"; echo ======; cat "<card>"`. The shape is `cat`, which BUILD-HUB.md:14 says is never typed, plus a `;`. It RAN and was not refused: it printed the hub, truncated, and exit 1. It was read-only and changed nothing. After it I read both files with the Read tool. It also means the bare-guard hook did not deny a `;` in this session. A fact for the install, which this build did not read.
- REFUSED, not needed: git -C /Users/cobalt/cobalt show --stat abcb732b — Permission to use Bash has been denied because Claude Code is running in don't ask mode. (read with `git -C /Users/cobalt/cobalt log -1 --stat --format=%H abcb732b` instead)
- G11 rests on the desk record R226 ("DESK RECORD (brain, under R33) … on his veto list"), not on a new ruling row of his. If he vetoes it, G11 is the one row to undo: `awk_writes` and the one line in `pipe_problems` that calls it.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

First stop line (G1–G8), superseded by the continue at G9: `built · job: cobalt-guard · tip: 28276443 · rows: 8 of 8 · decisions: 3 · for Dejan: 1`

BUILT · job: cobalt-guard · tip: 21b9e21f | on a8d8a848 | migration: none | offline 3739/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 11 of 11 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0
