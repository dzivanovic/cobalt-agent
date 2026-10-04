JOB: cobalt-guard
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/cobalt-guard-1004
WORKTREE: cobalt-guard-1004
BASE: a8d8a848
TIP:
REPORT: /Users/cobalt/cobalt-wt/cobalt-guard-1004/docs/40 - DevDocs/reports/cobalt-guard-build-2026-10-04.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
DB: none
RULINGS: 2026-10-02 R47, 2026-10-03 R32, 2026-10-03 R33, 2026-10-03 R12

## ROWS

WHY: his words 10-03 (11:03, 11:08 ET): the full guard hook builds Sunday after 13:00; read-only pipes are allowed. `bare-guard.py` (PreToolUse, his install) is EXTENDED IN PLACE so the existing hook entry covers it; it reads the hook JSON on stdin and exits 2 with ONE stderr sentence to deny, naming the route (`harness-mods-review-2026-10-03.md` ops 3–6, 8, 10, 12, 24; the REFUSALS list `cto-2026-10-03.md` R31 as test cases). The seat's kind is read from `cwd` (a worktree under `/Users/cobalt/cobalt-wt/` = worker; `/Users/cobalt/cobalt` = desk or brain) and from the first user message's `CARD:` / prompt path (`build`, `check`, `deploy`, `devfix` by the hub file it names). Tests in `tests/ops/` with constructed JSON; the hook never runs a command.

| row | what | red first | files |
|---|---|---|---|
| G1 | READ-ONLY PIPES (R45 part 1 amended): a Bash command is allowed when it is ONE command, or a `\|` chain whose EVERY segment's first word is one of `grep sed cut sort uniq head tail wc awk` with `sed` only as `sed -n` and no `-i`, `w`, `e` flags, and the whole holds no `&&`, `;`, `\|\|`, `>`, `<`, `>>`, newline or `$(`/backtick outside quotes. Anything else compound → deny with today's resend sentence | tests: today's denied `grep … \| cut ; grep … \| grep -o` → deny (the `;`); `grep -n X f \| cut -f2` → allow; `grep X f \| rm -rf /` → deny naming `rm`; `sed -i` in a chain → deny; `ls && ls` → deny | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |
| G2 | PRODUCTION FROM A NON-DEPLOY SEAT: `COBALT_ENV=production`, `--prod`, `cobalt_brain` in a Bash call whose seat is not a deploy hub → deny: `route: production is the deploy hub's; a dev read uses COBALT_ENV=dev` | per seat kind: deploy allowed, build/check/devfix/brain/desk denied | the same |
| G3 | `.env` NEVER READ: `cat`, `grep`, `sed`, `head`, `tail`, `less`, `Read` of a path ending `/.env` → deny; `ls -la <path>/.env`, `cp`, `rm` of it allowed (the lock steps) | tests per verb | the same |
| G4 | GIT SHAPE from a worker: `git add -A`, `add .`, a `commit` without `--`, `push`, `merge`, `rebase`, `reset`, `checkout`, `stash`, `cherry-pick`, `--output=` on any git call → deny: `route: git add <paths> then commit -m … -- <paths>; a merge is the deploy hub's` | tests per verb; the desk's `git -C /Users/cobalt/cobalt commit` with `--` allowed | the same |
| G5 | THE WRITE FENCE: a Write/Edit from a worker outside its worktree or under `/Users/cobalt/Vault`; from the brain outside `reports/` and `prompts/20*/`; from any seat onto a fixed file at `prompts/` root or `LAWS.md` unless the seat is a build whose card's `files` name it (the hook reads the card) → deny: `route: a fixed file changes by a card row` | tests per case | the same |
| G6 | STOP LINE WHILE DIRTY: a Write/Edit whose content's last non-blank line starts `BUILT ·`/`CHECK DONE ·`/`DEPLOYED` while `<cwd>/.env` exists or `/Users/cobalt/cobalt-wt/.cobalt_dev.lock/owner` names this worktree → deny: `route: release the lock (W (f)), then the stop line` | tests with tmp lock dir | the same |
| G7 | NO SECOND SESSION FROM A WORKER: `claude`, `codex`, `grok`, `agy` as a command's first word from a worker → deny: `route: the desk launches` ; the desk and brain allowed (`claude --bg` through `desk-launch.sh`) | tests | the same |
| G8 | THE LEDGER: every deny appends one JSON line to `/Users/cobalt/cobalt-wt/.ledger/<session_id>.jsonl` (time, cwd, rule, the command's first 200 bytes); never blocks on a ledger write error | tests: the line's fields; an unwritable dir → deny still exits 2 | the same |
| G9 | CHECK HOUSE CALLS (desk record, build DECISION 1, 10-04): G7 allows, for the `check` kind only, a command whose prefix is one of the three house strings `CHECK-HUB.md` line 10 lists (`grok `, `codex exec --skip-git-repo-check -m <slug> -s read-only `, `agy `); every other kind, and any other `claude`/`codex`/`grok`/`agy` call from a check, stays denied | tests: check kind → each of the three allowed; `codex exec` without `-s read-only` from a check → deny; build kind → `grok` denied | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |
| G10 | CHECK SCRATCH FENCE (desk record, build DECISION 2, 10-04): G5's fence for the `check` kind adds `<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/<JOB>-check` (`CHECK-HUB.md` line 5, writes per lines 50 and 73), `<JOB>` read from the card; a build or the brain writing there stays denied | tests: check Write under its own `<S>` allowed; under another job's `<S>` denied; build kind under `<S>` denied | the same |
| G11 | AWK READ-ONLY (desk record under his 2026-10-03 R33, brain reading 10-04): an `awk` pipe segment whose program text holds `system(`, `>` or `\|` is not read-only → deny, as `sed -i` is; any other `awk` segment stays allowed | tests: `awk '{print > "f"}'` → deny; `awk '{system("x")}'` → deny; `awk '{print \| "sh"}'` → deny; `grep X f \| awk '{print $2}'` → allow | `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` |

## NOT IN THIS JOB
- Any hub text, launch line or allow string (the hub lines' "ONE command per Bash call" sentence changes to "one command or a read-only pipe" on the next hub-text card); the Stop and Notification hooks (`09`); any mod.
- A rule that needs judgment (whether a finding holds, whether a diff is docs-only in meaning).

## READ
- `ops/desk/bare-guard.py` at `BASE` whole; `tests/ops/test_bare_guard.py`; `reports/harness-mods-review-2026-10-03.md` `## OPERATIONS A HOOK CAN TAKE`; `reports/cto-2026-10-03.md` the REFUSALS list (R31 and after); `BUILD-HUB.md` line 29 and `CHECK-HUB.md` line 48 (the one-command sentence G1 makes deterministic), `CHECK-HUB.md` line 50 (the git-write shape G4 enforces).

## CHECK ASKS
- X1 For each rule: a call that should pass and is denied (a false deny costs a resend), and a call that should be denied and passes. Write both per rule.
- X2 Can the kind detection be fooled (a worker whose cwd is the repo, a desk in a worktree)? What does the hook do when the kind is unknown — it must deny only G1, G3, G6 (kind-free rules) and allow the rest.
- X3 Does any hub step as written today type a command G2–G7 would deny? Walk the four hub files.

## RECORDS
- His words: 11:03 ET "Make it Sunday."; 11:08 ET "Make it so. Allow read-only pipes."; mods and hooks are Anthropic tuning, no outside house.
- Until this ships, every seat stays bare-command: the classifier judges each pipe segment, and `cut`, `sort`, `uniq`, `awk` are not on any line. Strings are his (R60): the build lists the four read strings (`Bash(cut *)`, `Bash(sort *)`, `Bash(uniq *)`, `Bash(awk *)`) in its report's `## RECORDS` approved by his 2026-10-03 R33 (desk record 10-04, not R60); the next hub-text card puts them on the build, check and desk lines. The hook itself adds no string.
