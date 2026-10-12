# draft-recut-archive 2026-10-12

## §0 Headline
- Card `prompts/2026-10-12/434-recut-archive-card.md` written (K5, JOB `recut-archive-1012`, BASE left for the desk): row A1 changes the recut arm `ops/desk/desk-launch.sh:1847-1935` only; R2 derives RESTARTS (none expected).
- When `pre-<job>` exists, recut runs seven read-only tests (not DEPLOYED, tag and branch where the report's `<pre-merge>` / `<stack-final>` say, tree registered, nothing landed, no lock, archive names free). Then `job-clean.sh salvage` on the gate, `branch -m` to `archive/<BRANCH>-<stamp>`, a new tag `archive/pre-<job>-<stamp>` and only then `tag -d pre-<job>`. Then the recut proceeds. A miss gives today's refusal text plus `— not archived: <test>`.
- The 256 state passes every test by read (card `## RECORDS`). Tests RA1-RA6 go in `tests/ops/test_desk_launch_recut.py`, each RED on BASE; nothing run.
- Next: the desk fills BASE, commits the card, then preflight / build.

## DECISIONS
1. ASK DESK: the worktree is removed FIRST (`job-clean.sh salvage`), then the branch, then the tag, not in the row's listed order. Salvage refuses before it changes anything (`job-clean.sh:113-124`), so a refusal leaves nothing half-archived. Default: worktree first. [19:25]
2. ASK DESK: "a ref points somewhere other than its report says". The hub records `<pre-merge>` and `<stack-final>` by name (`DEPLOY-HUB.md:5`, `:127`, `:129`) but fixes no line shape. The check: the report's last line holding each literal holds the ref's 8-hex, and `<S>^2` = `<P>` (D2.2's own proof). A report missing either name is refused. Default: this check. [19:25]
3. ASK DESK: `git tag <name> <sha>`, `git tag -d` and `git branch -m` are new inside an `ops/desk/` script. No seat's `--allowedTools` line changes: the desk runs the script under `Bash(sh /Users/cobalt/.claude/ops/*)`. `tag pre-<job>` / `tag -d pre-<job>` stand on DEPLOY-HUB's line (`:11`); `branch -m` stands on none (R411/R412). Default: proceed with no new seat string. [19:25]
4. ASK DESK: `STANDING-LIST.md:122` fences the hub's tag strings off "an earlier deploy's rollback anchor". The archive renames such an anchor (its commit kept under `archive/`). No string of that approved list changes. Default: not his; the desk confirms. [19:25]
5. ASK DESK: when the gate head is on main, the archive refuses even on main's first-parent line (gate-clean's exception, `gate-clean.sh:93-96`, is dropped). With a pre tag present, D2.1 made a merge, so a gate head on main means 4.3 landed. The refusal also means salvage never deletes the archive branch with `branch -d`. Default: refuse. [19:25]

## RECORDS
- Reads 19:10-19:25 EDT, `main` HEAD `0990393f`: `prompts/CARD.md`; `prompts/2026-10-12/413-stage-set-clear-card.md`, `393-needs-his-hand-card.md:1-16`, `411-reapplied-tip-card.md:20-26`, `417-db-apply-prod-card.md:55-64`; `reports/cto-2026-10-12.md` `:7-9`, `:146`, `:149-156`; `ops/desk/desk-launch.sh` `:49-75`, `:110-120`, `:203-211`, `:250`, `:485-510`, `:1007-1013`, `:1579-1600`, `:1840-1945`, grep `:1981-2020`; `ops/desk/gate-clean.sh` whole; `ops/desk/job-clean.sh` whole; `prompts/DEPLOY-HUB.md` `:5`, `:7-12`, `:49-55`, `:112-116`, `:126-135`, `:157-181`; `prompts/STANDING-LIST.md:118-124`; `reports/cto-2026-10-05-words.md:26-30` (R411, R412); `src/cobalt/jobs/restarts.py` `:38`, `:225-233`, `:246`; `tests/ops/test_desk_launch_recut.py` whole; `tests/ops/test_gate_clean.py` test names (grep); `reports/deploy-aset-orphan-1010.md` grep and `:130-248`.
- 256 refs (`git rev-parse`, `git log`): `pre-aset-orphan-1010` → `8199fa13`; `deploy/aset-orphan-1010` → `a617c402`, parents `4aee2f68` `8199fa13`; 5 commits not on main; tag `deploy-2026-10-10-aset-orphan` absent; gate tree clean on `deploy/aset-orphan-1010`; no gate `.env`; no lock directory.
- Symlinks (`ls -la /Users/cobalt/.claude/ops/`): `desk-launch.sh`, `gate-clean.sh` and `job-clean.sh` point at `/Users/cobalt/cobalt/ops/desk/`, so `INSTALL: none`.
- `git show HEAD:.claude/settings.json`: the desk's allow `Bash(sh /Users/cobalt/.claude/ops/*)`, line 29.
- Line counts (`wc -l`): `desk-launch.sh` 2023, `gate-clean.sh` 109, `job-clean.sh` 212, `test_desk_launch_recut.py` 338, `test_gate_clean.py` 745, `DEPLOY-HUB.md` 181, `deploy-aset-orphan-1010.md` 248.
- No git write and no launch from this seat. The card and this report are uncommitted, for the desk.

DRAFTED · decisions: 5
