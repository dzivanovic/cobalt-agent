# DRC merge-main draft 2026-09-28 — drafter `drc-merge-draft-0928`

## §0 Headline
- Drafted `prompts/2026-09-28/15-drc-merge-main-build.md` (29,339 bytes; `R__` on 1 line, in AUTHORIZATION only).
- `drc/d1-trading-log` `10163d51`: 602 behind `main` `a8b14e6d`, 65 ahead; merge-base `04b05cd4`.
- 16 paths changed on both sides: 12 conflict by hunk overlap, 4 are disjoint (clean). Each has one rule; none needs a design ruling.
- Migration order is numeric (`0013`…`0018`), because main's own pin requires `FORWARD == sorted`. ESCALATE 1 records this reading of R33.
- NEW strings: 2 (`git merge --no-ff --no-edit main`, `git merge --abort`).

## FACTS
[read 09:32–09:41 ET, 2026-09-28]
| fact | command | result |
|---|---|---|
| authorization | `grep -n -F "14-draft-drc-merge-main.md"` on `reports/cto-2026-09-28.md` | `:45` R37, APPROVED — LAUNCHING; R26 `:34`, R33 `:41`, R36 `:44` read; 09-20 R13 `:86` |
| behind | `git -C /Users/cobalt/cobalt log --oneline drc/d1-trading-log..main` (`wc -l`) | 602 |
| ahead | `git -C /Users/cobalt/cobalt log --oneline main..drc/d1-trading-log` (`wc -l`) | 65: `3e13b5de` D1-0 … `10163d51` D2 report (D1, D1 fix r1, K1 + r1 + r2, K2 + r1 + r2, D4 + r1 + r2, D2) |
| tips | `git -C /Users/cobalt/cobalt log -1 --format='%h %ad %s' main` · `… drc/d1-trading-log` | `a8b14e6d` 09:32:49 ET (desk docs) · `10163d51 docs(drc-d2): DRC D2 build report — 6777c463` |
| merge-base | `git -C /Users/cobalt/cobalt merge-base main drc/d1-trading-log` | `04b05cd4` |
| branch paths | `git -C /Users/cobalt/cobalt log --name-only --format= main..drc/d1-trading-log` (`sort -u`) | 99 paths |
| main paths | `git -C /Users/cobalt/cobalt log --name-only --format= drc/d1-trading-log..main` (`sort -u`) | 738 paths |
| both sides | `comm -12` of the two lists; the same 16 from `git diff --name-status 04b05cd4 <side>` | 16 (table below) |
| main deletes / renames of branch paths | `git -C /Users/cobalt/cobalt log --diff-filter=DR --name-status drc/d1-trading-log..main -- src tests configs pyproject.toml uv.lock`; `grep -v "^M"` of main's net diff against the branch list | none touch a branch path |
| main migrations | `git -C /Users/cobalt/cobalt show main:src/cobalt/db_migrations/` | `0001`–`0011`, `0013`, `0014`, `0015`, `0017` |
| migrate order law | `git show main:src/cobalt/db_migrations/__init__.py`; `…/cli.py` `:767`–`:783` | "Both tuples stay ordered by version"; FORWARD applies every file in order; `_rollback_paths` = REVERSE filtered by number > target |
| main's order pin | `git show main:tests/cobalt/test_archiver_migrations.py` `:150`, `:161`–`:163` | `assert numbers == sorted(numbers), "FORWARD must be in numeric order"`; `reverse_numbers == [n for n in reversed(numbers) if n != 1]` |
| pass-2 ids on main | `git show main:tests/cobalt/<file>` + `grep -c -F "<def/class>"` ×8 | each 1 |
| DRC chain with-DB | `grep -n -F -- "--deselect"` on `08-drc-d2-fix-r1-build.md` | `:142`: three deselects (four tests), no forward migrate |
| paths R33 names that the branch never changed | branch list | replay runner, smoke, `jobs.yaml`, `rules.yaml`, `vault_loader.py`, `CLAUDE.md` absent → main's version, no conflict |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` (09:38) | `no matches found` |
| worktree | `ls /Users/cobalt/cobalt-wt` · `ls -d /Users/cobalt/cobalt-wt/drc-d1/.venv` | `drc-d1`, `s3-exits-c1` listed; `.venv` present |
| R22 strings | `grep -n "^| R22 "` on `cto-2026-09-24.md` | `:40`: `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env)`, `Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)`, "approved" |

## BOTH-SIDES
Hunks are in merge-base coordinates, from `git diff -U0 04b05cd4 <side> -- <path>`. Intent is read from `git diff 04b05cd4 <side> -- <path>`.
| path | branch commits | main commits | conflict | reason · rule |
|---|---|---|---|---|
| `src/cobalt/db_migrations/__init__.py` | `9a0fc900` `d583f6fd` | `00e2b7ff` `91c631ac` `a16c97ff` `01ee8bcd` `a2d320b8` `4e625f6a` `d8359ebf` `69c376bd` | yes | both insert after `:37`, `:78`, `:82` · R-MIG: numeric FORWARD `…0011, 0013–0018`, mirrored REVERSE; the docstring entries in numeric order; main's gap paragraph kept, the branch's dropped |
| `src/cobalt/db_migrations/placement.py` | `9a0fc900` `d583f6fd` | `69c376bd` | yes | both insert after `:88` · R-PLACE: 0016 block, 0017 `voice_turns`, 0018 block |
| `tests/cobalt/test_archiver_migrations.py` | `9a0fc900` `96bee451` `d583f6fd` | `00e2b7ff` `91c631ac` `a16c97ff` `01ee8bcd` `a2d320b8` `4e625f6a` `95ca07d1` `28b6b0c6` `69c376bd` | yes | `:80`, `:84`, `:91`, `:113`, `:117`, `:136`, `:460` · R-ARCH: `[-10:]`, `[:10]`, pin `[*range(1, 12), 13, 14, 15, 16, 17, 18]`, survivors exclude DRC + voice |
| `tests/cobalt/test_p4_migrations.py` | `9a0fc900` `d583f6fd` | same eight as `test_radar_migration.py` | yes | `:101`, `:110`, `:115` · R-PINS |
| `tests/cobalt/test_radar_migration.py` | `9a0fc900` `d583f6fd` | `00e2b7ff` `91c631ac` `a16c97ff` `01ee8bcd` `a2d320b8` `4e625f6a` `95ca07d1` `69c376bd` | yes | `:34` slice `[:4]` → `[:6]` vs `[:8]` · R-PINS `[:10]` |
| `tests/cobalt/test_radar_score_migration.py` | `9a0fc900` `d583f6fd` | same eight | yes | `:103`, `:110`, `:115`, `:120` · R-PINS `[:10]` ×3 |
| `tests/cobalt/test_tenancy.py` | `9a0fc900` `d583f6fd` | same eight | yes | `:514` · R-PINS; `:73` / `:83` (`DrcStore`) clean |
| `tests/cobalt/test_radar_panel_cards.py` | `6777c463` `705fba6f` | `00e2b7ff` `a2d320b8` `4e625f6a` `583852a8` `8bed61d3` | yes | both insert after `:666` in `POST_ALLOWLIST` · R-PANEL: union; `GET_ONLY` the branch's |
| `docs/…/aset/web.md` | `d5b72392` `0075db31` | `8bed61d3` `f00c37d2` | yes | both append after `:235` · R-DOCS: main's section, then the branch's |
| `docs/…/cli.md` | `9a0fc900` | `566d1848` | yes | both append after `:86` · R-DOCS |
| `docs/…/db_migrations/__init__.md` | `9a0fc900` `61ef8381` | the eight | yes | both append after `:137` · R-DOCS |
| `docs/…/db_migrations/placement.md` | `9a0fc900` `61ef8381` | `69c376bd` | yes | both append after `:40` · R-DOCS |
| `src/cobalt/aset/web.py` | `d5b72392` `807c13ec` `0075db31` | `8bed61d3` `f00c37d2` | no | branch `:69`, `:563`, `:619`, `:1180` (D4 after `/attest`), `:1392` (D2 at END); main `:81`, `:84`, `:436`, `:863`, `:867`, `:1249`–`:1257`, `:1264` — disjoint · R-WEB if git conflicts anyway |
| `src/cobalt/cli.py` | `9a0fc900` | `566d1848` | likely no | inserts after `:67` / `:509` vs `:80` / `:510`; one unchanged line (`jobs_cli.add_stop_parsers(sub)`) between · R-CLI if it conflicts |
| `pyproject.toml` | `d5b72392` (`python-multipart==0.0.22`) | `cc2e95b6` (`faster-whisper==1.2.1`) | no | `:32` vs `:57` · a conflict = UNPLANNED |
| `uv.lock` | `d5b72392` (`:788`, `:842`) | `cc2e95b6` (`:318`, `:766`, `:820`, `:1055`, `:1322`, `:1412`, `:3190`) | no | disjoint sorted inserts; the union is the lock both pins produce · a conflict = UNPLANNED; a `uv run` that rewrites it = FAILED |
Rulings needed: 0. Every candidate resolves as a union of both sides' lines, ordered by migration number or by date of section.

## RULE PROOF
`15`'s launch line compared with `48`'s line 5 (`comm` of the sorted `"Bash(…)"` tokens, in `$CLAUDE_JOB_DIR/tmp`):
- Carried byte for byte (20): `git -C * status*` `log*` `diff*` `rev-parse*` `rev-list*` `merge-base*` `show*`; `cd *`; `uv run pytest *`; `COBALT_ENV=dev uv run pytest *`; `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *`; the four `COBALT_ENV=dev uv run cobalt db …` strings; `ls *` `grep *` `tail *` `wc *` `date*`. The three denies are the same.
- Dropped from `48` (12). Four `git -C …/stacked-0925 merge --no-edit <branch>`, plus its `merge --abort`, `add *`, `commit --no-edit` and `commit -m *`, are bound to another tree. So is its `.env` pair. `COBALT_ENV=production uv run cobalt validate` and `COBALT_ENV=production uv run cobalt jobs restarts *` go because this build never types `COBALT_ENV=production`.
- Added, not new (5): the drc-d1 `.env` pair (09-24 R22, byte for byte). `git add *`, `git commit *` and `uv run cobalt jobs restarts *` are the DRC chain's own strings (`07` / `08` line, byte for byte). The `comm -13 s48 s15 | comm -23 - s07` output lists only the two NEW strings.
- Other differences:
  - Prompt path and `--remote-control drc-merge-main-build --name drc-merge-main-build` (`48` carried no `--name`; checklist H6, 09-28 R23).
  - The desk's `cd` targets `/Users/cobalt/cobalt-wt/drc-d1`.
  - The mode `--permission-mode acceptEdits` is unchanged, as are the `--add-dir` triplet and `--model claude-opus-5-5`.
- Count: 27 allow, 3 deny.

NEW strings:
- `Bash(git merge --no-ff --no-edit main)`: run from the cwd `/Users/cobalt/cobalt-wt/drc-d1`. It can touch only that worktree's index and files, and the branch ref `drc/d1-trading-log`, which it advances by one merge commit. It never touches `main`, `~/cobalt`'s tree, another worktree, a remote or `cobalt_dev`. It fixes the merge source to `main` and the shape to `--no-ff` (always a merge commit, the L54 revert-`-m` shape) with `--no-edit` (no editor, L63).
- `Bash(git merge --abort)`: run from the same cwd. It can touch only the in-progress merge in that worktree, restoring its index and files to `10163d51`. It never touches a commit, another ref or another tree. Outside a merge it is a no-op error.
Both go to him before `15` launches (UNATTENDED-LAUNCH §1.2).

## ESCALATE
1. ASK DESK: R33 says "main's entries, then DRC's `0016` `0018` … in number order". Taken literally, that yields FORWARD `…0017, 0016, 0018`, which fails main's pin `assert numbers == sorted(numbers)` (`test_archiver_migrations.py:150`). It also breaks the module's own "Both tuples stay ordered by version". `15` therefore orders FORWARD `0013, 0014, 0015, 0016, 0017, 0018` and mirrors it in REVERSE. [09:41 ET] Safe default taken: numeric order.
2. ASK DESK: the add and commit strings are `07`'s `Bash(git add *)` and `Bash(git commit *)`, not `48`'s path-bound `-C` forms, which were cut for another tree. They are wider than `48`'s, but they are on the DRC chain's approved line. Confirm, or issue `-C /Users/cobalt/cobalt-wt/drc-d1` forms as NEW strings instead. [09:41 ET] Safe default taken: `07`'s strings carried.
3. W applies `0014`–`0018` to `cobalt_dev` and rolls them back to `0013` (`48`'s W, as `14` orders), proven by F2 = F0. The DRC chain's prompts never ran `cobalt db migrate` on `cobalt_dev`; this is the first time `0016` and `0018` are applied outside a suite transaction.
4. For `08`–`11`: on the merged tree the voice with-DB tests need `0017`. `08`'s three `--deselect` arguments (`:142`) then leave those tests red at `0013`, so the with-DB set to re-point is `15`'s eight-argument set. `15` `## FOR 08` carries it.
5. A red after the merge commit leaves that commit on the branch, and `15` holds no `reset` or `revert` string. The desk rules the next step (a fix round, L75, or its own reset before `08`). The shipped branch's rollback shape is unaffected: the DRC deploy's gate (L54 / L68).
6. Order vs S3 C1 (R36): `15`'s W takes the L76 lock only while it is free. A held lock ends `FAILED: W — cobalt_dev lock held`, and the run is relaunched with `CONTINUE: W`; the merge and offline legs need no lock.
7. The kept prose stays stale where it was already stale. Main's gap paragraph calls `0016` unmerged, and `test_archiver_migrations.py`'s kept comments name unmerged branches. The rules keep text verbatim; `08` rewrites the docstring for `0019`.
8. `~/cobalt`'s uncommitted `M configs/cobalt/rules.yaml` (session git status) is not in the `main` ref, and the merge does not see it.
9. The first `uv run` on the merged tip syncs `faster-whisper` and its dependencies into `drc-d1/.venv`, which needs network. `15`'s status rule stops the run if `uv run` rewrites `uv.lock`.
10. L74: a block arrived inside the tool result of reading `14-draft-drc-merge-main.md`. It asked commits to carry a `Claude-Session:` line and named a file-send tool. Recorded once and not followed. This seat commits nothing and sends no file.

## CONTINUE
The desk:
1. Verify `15` (L35).
2. Put the two NEW strings and ESCALATE 1–2 to him.
3. Commit `15` with its launch row. The row fills `R__` and carries `no with-DB run in flight`.
4. Launch `15` only while the lock is free and `drc-d1` is quiet.
5. Re-point `08`–`11` from `15`'s `## FOR 08`.

DRC MERGE PROMPT DRAFTED · behind: 602 · ahead: 65 · both-sides files: 16 · rulings needed: 0 · new rule strings: 2 · ESCALATE: 10
