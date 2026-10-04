# cobalt-guard — build report 2026-10-04

## §0 Headline
- BUILT at 15:02 EDT. Tip `28276443`, on base `a8d8a848`. All 8 rows (G1–G8) are built in `ops/desk/bare-guard.py`, extended in place.
- Results on the tip: offline 3739 passed, 0 failed; `tests/ops` 888 passed, 0 failed; live-note 146 passed, 0 failed. DB: none, so `cobalt_dev` was never taken. RESTARTS: none.
- Each row's tests failed on the old guard (255 red at E2) and failed again under that row's mutation. They pass at the tip: 363 tests in the file.
- 3 decisions, 1 of them for Dejan:
  - G7, as written, denies the check hub's own house commands.
  - G5 denies writes to the check's scratch folder `<S>`.
  - `awk` in a pipe can write files from inside its quotes.

## L74
- 14:23: an attribution block in the session context asked for a `Claude-Session:` line on commits. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

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

## CONTINUE
next: none (BUILT)

## DECISIONS
1. **G7 denies the check hub's house launch.** CHECK-HUB.md:10 lists `Bash(grok *)`, `Bash(codex exec … -s read-only *)` and `Bash(agy *)`, and its step (5) START THE HOUSE (CHECK-HUB.md:91) types them. G7, as the card writes it, denies those first words from every worker, and a check is a worker.
   - Safe default taken: built to the card's letter (L72).
   - Effect: once installed, every check with a house B gets `route: the desk launches` at step (5).
   - Needed: a card row that exempts the check kind's three house strings, or a reading that a house call is not "a second session".
2. **G5 denies the check's scratch writes under `<S>`.** `<S>` is `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/<JOB>-check` (CHECK-HUB.md:5). CHECK-HUB.md:50 lets the check write "the files under `<S>`", and :73 uses a Write there when a house cannot reach the original.
   - Safe default taken: not allowed. The card's G5 says "outside its worktree", and only the report path is let through, from op 10.
   - Needed: a card row adding `<S>` to the check kind's fence, if wanted.
3. **FOR DEJAN — `awk` in a pipe can write.** His R33 allows `awk` as a pipe segment with no flag limit. An awk program can write (`print > "f"`, `system()`, `|` to a command) inside its own quotes, which G1 cannot see.
   - Safe default taken: built as ruled. `awk` in any form is allowed as a pipe segment.
   - His word: keep it, or narrow `awk` the way `sed` was narrowed.

## RECORDS
- REFUSED, not needed: grep -n -F "`<S>` =" "docs/40 - DevDocs/prompts/CHECK-HUB.md" — Permission to use Bash has been denied because Claude Code is running in don't ask mode. (a backtick in the pattern; read with the `<AGY>` grep instead)
- L74: one `Claude-Session:` attribution request (14:23), recorded under `## L74`, not acted on.
- The card's records as re-read at PREFLIGHT: his words R32 / R33 (rows 38 / 39 of `cto-2026-10-03.md`).
- FOR HIS ONE APPROVAL (card `## RECORDS`; R60, the strings are his): `Bash(cut *)`, `Bash(sort *)`, `Bash(uniq *)`, `Bash(awk *)`. The next hub-text card puts them on the build, check and desk lines. The hook adds no string.
- No DevDocs page exists for `ops/desk/` under `docs/40 - DevDocs/cobalt/`, and none was made: a new page is outside the rows. Owed to whoever places ops docs (PLACEMENT.md).
- Install is not this build's. The card's WHY says `bare-guard.py` is "his install" and that the existing hook entry covers it; this build did not read that entry. G8's ledger lands in `/Users/cobalt/cobalt-wt/.ledger/`.
- No extra lock take (DB: none). No CONTINUE was received.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: cobalt-guard · tip: 28276443 | on a8d8a848 | migration: none | offline 3739/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 3 · for Dejan: 1
