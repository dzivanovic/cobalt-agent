JOB: devfix-route
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R18
BRANCH: ops/devfix-route-1002
WORKTREE: devfix-route-1002
BASE: 551f07e0
TIP:
REPORT: /Users/cobalt/cobalt-wt/devfix-route-1002/docs/40 - DevDocs/reports/devfix-route-build-2026-10-02.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R14, 2026-10-02 R18, 2026-10-02 R47

## ROWS

| row | what | red first | files |
|---|---|---|---|
| F1 | A fifth fixed file, `docs/40 - DevDocs/prompts/DEVFIX-HUB.md` (title token `«INSTALL`, as the others before his approval): one dev-maintenance job on `cobalt_dev` from a card, no git write. Steps: AUTHORIZATION as `BUILD-HUB.md` (installed, card committed and unchanged, every `RULINGS` row); PREFLIGHT (`git status`, the lock free, the worktree at `BASE`); THE LOCK exactly as `BUILD-HUB.md` states it at this build's `BASE`, taken once; `<FP>` → `<F0>`; `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `0013`, else the release and `FAILED`; `COBALT_ENV=dev uv run cobalt db dev-rebuild <TABLE> --dry-run` → `DRY RUN — ROLLED BACK`, every field equal; the same without `--dry-run` → `REBUILT`; `<FP>` → `<F1>` = `<F0>`; `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line <PROOF TEST>` → passes; `migrate --proof-only` → `0013`; the release, ALWAYS, at every ending. Report `<REPORT>` (`## §0 Headline` → `## STEPS` → `## DECISIONS` → `## RECORDS`), last line while running `(run in progress)`. Stop line, one of: `REBUILT · <TABLE> max_attnum <b> → <a> · rows <n> = <n> · FP F1 = F0 · proof test: PASSED · cobalt_dev: 0013 · .env: removed · decisions: <n> · for Dejan: <n>` or `FAILED: <step> — <reason> · cobalt_dev: <level, FP state> · .env: removed`. ONE launch line: the one in this card's `## RECORDS`, byte for byte | RUN — asserts nothing (a prompt file has no test): `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/DEVFIX-HUB.md"` → `1`; the F2 dry run prints that line with its tokens filled | `docs/40 - DevDocs/prompts/DEVFIX-HUB.md` |
| F2 | `desk-launch.sh devfix "<card>"`, a kind beside `build` (`ops/desk/desk-launch.sh`, the kind `case` ~388 and the per-kind `case` ~450). Header keys it needs: `JOB`, `LADDER`, `BRANCH`, `WORKTREE`, `BASE` (8 hex, a commit on `main`), `REPORT`, `RULINGS`, `TABLE`, `PROOF TEST`; body `## RECORDS` optional, `## ROWS` none. Refuses: `TABLE` not `system.<name>` or `user.<name>` with `<name>` in `[a-z0-9_]`; `PROOF TEST` not `tests/cobalt/<file>.py` with an optional `::<name>` in `[A-Za-z0-9_:.]`; `REPORT` not `$REPORTS/devfix-*.md`, or already present on a first launch; the lock held (`lock_free`, or 07's lock test as `BASE` carries it); a card or fixed file uncommitted or changed; a worktree on another branch. Runs `git -C /Users/cobalt/cobalt worktree add -b <BRANCH> /Users/cobalt/cobalt-wt/<WORKTREE> <BASE>` when absent, `cd` there, then the fixed file's line with `<card>`, `<job>`, `<worktree>`, `<table>`, `<proof test>` filled. A resume step as `build` | a new `tests/ops/test_desk_launch_devfix.py`, run with `DESK_LAUNCH_DRY=1`, a tmp copy of the tree and a stub `claude` (the shape of `tests/ops/test_devdb_lock.py` at `BASE`): a good card prints the worktree add, the `cd` and the filled line; each refusal above exits 1 with its `REFUSED:` text; `prompt` and `build` lines print as at `BASE`. RED on `BASE`: `REFUSED: kind 'devfix' is none of …` | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_devfix.py` |
| F3 | The format and the one approval list. `prompts/CARD.md`: the header table gains a `devfix` column and the keys `TABLE`, `PROOF TEST`; one short "A DEVFIX CARD, IN SHORT". `prompts/STANDING-LIST.md`: a `## 6. DEVFIX-HUB.md` table in the shape of §1 — every string of the F1 line with for / can touch / never touches, the standing ones marked by their section, the NEW ones flagged **NEW**; and the NEVER block's last line names `devfix` as the dev-maintenance route. `desk-launch.sh`'s header comment lists the kind | RUN — asserts nothing: `grep -n -F "dev-rebuild" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → the one NEW allow row; quote the §6 table whole | `docs/40 - DevDocs/prompts/CARD.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md` |
| F4 | RUN — asserts nothing. The desk's watch: `ops/desk/wait-stop-line.sh` accepts the pattern `^(REBUILT\|FAILED)` on a `reports/devfix-*.md` path. Quote its usage line and one `DESK_LAUNCH_DRY`-style dry run, if it has one; otherwise its argument check | — (tool output quoted) | none (read only) |

## NOT IN THIS JOB
- `cobalt db dev-rebuild` itself (card `11-dev-rebuild-card.md`); the slot guard (card `13-slot-guard-card.md`).
- Any change to the `build`, `check`, `deploy`, `desk`, `prompt` or `close` kinds; the `prompt` kind's write-path refusal stands.
- The install under `/Users/cobalt/.claude/ops/` and the `«INSTALL` token: the desk's, after his approval row.
- Any allow string beyond the F1 line; any production string; any git write string on the F1 line.
- A devfix that changes schema level, applies or reverses a migration, or deletes rows.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-02.md` R11, R12, R15, R16, R18.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-02/01-devdb-rebuild.md`: the one-off this route replaces (its allow list, its steps, its stop line).
- `ops/desk/desk-launch.sh` at `BASE`: the header, `committed`, `check_paths`, `run_launch`, the `prompt` kind's refusals, the `build` kind's worktree add, `lock_free`.
- `docs/40 - DevDocs/prompts/BUILD-HUB.md` `## THE LOCK`, `## UNATTENDED RULES`, the launch line; `docs/40 - DevDocs/prompts/STANDING-LIST.md` §1 and the `.env` pattern.

## RECORDS
- THE LINE F1 WRITES INTO `DEVFIX-HUB.md` — the job's product, not this card's launch (this card launches on `BUILD-HUB.md`). The lock pair is the `cp` / `rm` pattern on main at 06:27 ET; if `BASE` carries 07's `take-devdb-lock.sh` / `release-devdb-lock.sh` strings and `--add-dir /Users/cobalt/.claude/ops` (2026-10-01 R20, 2026-10-02 R9), F1 carries those instead, byte for byte as `BUILD-HUB.md` at `BASE`:
  `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEVFIX-HUB.md' and follow it exactly. CARD: '<card>'" --model claude-opus-5-5 --permission-mode dontAsk --remote-control <job>-devfix --name <job>-devfix --allowedTools "Read" "Grep" "Glob" "Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-*)" "Bash(cd *)" "Bash(ls *)" "Bash(grep *)" "Bash(tail *)" "Bash(wc *)" "Bash(date*)" "Bash(git status*)" "Bash(git log*)" "Bash(git show*)" "Bash(git diff *)" "Bash(git -C /Users/cobalt/cobalt log*)" "Bash(git -C * diff*)" "Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/<worktree>/.env)" "Bash(rm /Users/cobalt/cobalt-wt/<worktree>/.env)" "Bash(COBALT_ENV=dev uv run cobalt db query *)" "Bash(COBALT_ENV=dev uv run cobalt db migrate --proof-only)" "Bash(COBALT_ENV=dev uv run cobalt db dev-rebuild *)" "Bash(COBALT_ENV=dev uv run pytest *)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" "Bash(COBALT_ENV=production*)" --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt`
- NEW strings on that line, for his ONE approval: allow `Bash(COBALT_ENV=dev uv run cobalt db dev-rebuild *)`; allow `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-*)`; deny `Bash(COBALT_ENV=production*)` — APPROVED, his `cto-2026-10-02.md` R26. Every other string stands on `BUILD-HUB.md`'s or `CHECK-HUB.md`'s line (STANDING-LIST §1–§2); `wc *`, `git show*`, `git diff *` added by the desk at R26 as the basic read set every hub carries.
- RESTARTS class homes: `ops/desk/desk-launch.sh` → `OPS_TOOLS` in `src/cobalt/jobs/restarts.py` (`:36`) as 02 / 07 lift it ("operator script; no Cobalt reader"); if `BASE` does not carry that lift, the row's `files` gains `src/cobalt/jobs/restarts.py` for the one-line lift (2026-10-02 R8's shape). `tests/ops/*` → "test/documentation" (`:239`). `docs/…` → DOCS (`:219`). (the drafter, 06:27 ET)
- At 06:27 ET `tests/ops/` is not on `main`: it lands with 02 / 07.
