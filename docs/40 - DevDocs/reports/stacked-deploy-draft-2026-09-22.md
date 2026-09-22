# STACKED DEPLOY DRAFT 2026-09-22 — drafter `stacked-deploy-draft-0922` (Opus 5)

## §0 DIGEST
- **Files written** (Write tool only): `prompts/2026-09-22/05-stacked-deploy.md` (the hub, 57,406 B), `prompts/2026-09-22/06-review-stacked-deploy.md` (the house read, 22,721 B), and this report. Nothing was committed or launched.
- **Hub seat: Sonnet 5, auto mode.** The reason is `53`'s WHY-NOT-OPUS finding, checked again for ops. Neither branch has a migration, a `trader_settings` write, a production DB write or a vault write.
  - `backup.yaml` makes the 21:40 one-shot READ a vault file into restic.
  - `jobs.yaml` adds one `no_resident_reads` row and no job row. The hub proves this at STEP-2.6, so `jobs register` is not run.
  - The one DB write is the with-DB suite on `cobalt_dev` (ESCALATE 2).
- **Predicted:** `RESTARTS: com.cobalt.aset`. This is from the ops build's own `main..HEAD` table (`ops-fix-r3-2026-09-22.md:143-204`):
  - `radar_panel.py` → aset;
  - `backup.yaml` → no resident reads;
  - `jobs.yaml` → `registry; register, no restart`;
  - `.gitignore` → META;
  - tests and docs → `-`.
  The radar stays UP unless the gate table names it.
- **How far main moved** (`main` = `dd6713a` at 06:5x ET):
  - Since the stale cut `5b208a0`: 24 commits, all docs EXCEPT `configs/cobalt/rules.yaml`. That is the machine-written `generated_at` line, committed in the close commit `97ff2cf`.
  - Since the ops cut `f5c5bf0`: 54 commits. Non-docs: `rules.yaml` plus `src/cobalt/aset/radar_panel.py` and `tests/cobalt/test_radar_panel.py`, from the degraded-line deploy `deploy-2026-09-21b`.
  - `main` is NOT docs-only relative to either cut. This is why `05` proves identity on each branch's own paths and runs the gate on the combined tree.
- **Window:** 11:00–19:55 ET on 2026-09-22. The hard clock is 19:55 ET, checked before the bootout; the merge clock is 19:58 ET. No down-window crosses 20:00, 20:30, 21:10 or 21:40.
- **New rule strings (9):**
  - `Bash(git -C /Users/cobalt/cobalt-wt/ops-0921 rebase main)`
  - `Bash(git -C /Users/cobalt/cobalt-wt/ops-0921 rebase --abort)`
  - `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --no-edit s2/stale-marker-0921)`
  - `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --no-edit ops/2026-09-21)`
  - `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --no-edit main)`
  - `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --abort)`
  - `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0922/.env)`
  - `Bash(rm /Users/cobalt/cobalt-wt/stacked-0922/.env)`
  - `Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0922)`
  
  The `revert -m 2` needs no new string: `53`'s `revert --no-edit *` covers it, as `d3` §8 (1) stated. The review prompt adds no new string: it uses 9 of `54`'s strings.
- **ESCALATE: 8.**

## Decisions the prompt makes, and why
- **Rebase, then merge into the gate (`d3`'s shape).** `d3` merged its two branches with `merge --no-edit` into a stack cut from `main`, after a separate run had rebased them. `05` does the rebases itself: `53`'s `stale-marker rebase main` string plus the NEW ops pair.
  - Why: under L54 a rebase is required before every merge. `ops` is 54 commits behind. Rebasing brings each conflict up in the branch's own worktree, where its own `--abort` exists.
  - Conflict risk: the drafter compared `ops`'s single BACKLOG hunk (line 519) with `main`'s three hunks (61, 320, 553). They do not overlap.
  - The gate merges are NAMED strings, not `d3`'s `merge --no-edit *` wildcard. That makes them narrower.
- **The `-m 2` merge is GUARANTEED to exist.** In `d3` the run's own report commits moved `main`, so §4.1's `merge --no-edit main` made a real merge. `53` kept its report uncommitted until the end. If `05` did the same, `main` might not move after the gate cut, `merge main` would print `Already up to date.`, and there would be NO merge commit to revert.
  - So `05` makes ONE required report commit at STEP-2.8. `Already up to date.` at 3.1 then fails with nothing down.
  - 3.2 proves `<stack-final>^2` = production's `main` before anything goes down.
- **Identity proofs use each branch's own paths**, not `53`'s tree-wide `':(exclude)docs'`. That form prints `rules.yaml`, which main moved and the branches never touch. See ESCALATE 4.
- **`restarts` runs in the gate worktree.** From `~/cobalt`, main's classifier lacks the `backup.yaml` row, which is ops's own fix. It would flag `backup.yaml` UNCLASSIFIED, as `d3` P7 recorded for its own case.
  - `restarts.py` resolves `REPO_ROOT` from the module file, so `uv run` in the gate uses the gate's code.
  - The range is written with explicit shas, so `restarts.py:80-85`'s working-tree collection (`HEAD` / `WORKTREE` only) cannot add dirt.
  - 4.5 (g) runs it again from `~/cobalt` on the landed classifier.
- **`validate` runs in the gate as well.** `_cmd_validate` (`src/cobalt/cli.py:131-467`) opens no DB connection; the drafter read it. Its success without `.env` is UNPROVEN (ESCALATE 6), and the hub has a written fallback for that case.

## RULE PROOF
The hub's full launch-line allowlist is 43 allow strings and 3 denies. Each was checked with `grep -c -F -e "<string>"` against `2026-09-21/53-stale-marker-deploy.md` (`53`) and `2026-09-19/53-deploy-d3.md` (`d3`); the counts are the drafter's own tool output.

| # | string | source | step that needs it |
|---|---|---|---|
| 1 | `Bash(git -C /Users/cobalt/cobalt add *)` | 53 (and d3) | 2.8, 6 |
| 2 | `Bash(git -C /Users/cobalt/cobalt commit *)` | 53 (and d3) | P3, 2.8, 6 |
| 3 | `Bash(git -C /Users/cobalt/cobalt reset --soft HEAD~1)` | 53 (and d3) | P3 |
| 4 | `Bash(git -C /Users/cobalt/cobalt tag *)` | 53 | P2, 3.4, 6 |
| 5 | `Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0922)` | **NEW** | 4.3 |
| 6 | `Bash(git -C /Users/cobalt/cobalt revert --no-edit *)` | 53 (and d3) | 5 (2), `-m 2` |
| 7 | `Bash(git -C /Users/cobalt/cobalt revert --abort)` | 53 (and d3) | 5 (2) |
| 8 | `Bash(git -C /Users/cobalt/cobalt-wt/stale-marker rebase main)` | 53 (R39: "TUE evening only"; re-approval needed, ESCALATE 6) | 1.1 |
| 9 | `Bash(git -C /Users/cobalt/cobalt-wt/stale-marker rebase --abort)` | 53 (same) | 1.1 |
| 10 | `Bash(git -C /Users/cobalt/cobalt-wt/ops-0921 rebase main)` | **NEW** | 1.2 |
| 11 | `Bash(git -C /Users/cobalt/cobalt-wt/ops-0921 rebase --abort)` | **NEW** | 1.2 |
| 12 | `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --no-edit s2/stale-marker-0921)` | **NEW** (d3's verb, named) | 1.4 |
| 13 | `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --no-edit ops/2026-09-21)` | **NEW** (d3's verb, named) | 1.4 |
| 14 | `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --no-edit main)` | **NEW** (d3 §4.1's verb, named) | 3.1 |
| 15 | `Bash(git -C /Users/cobalt/cobalt-wt/stacked-0922 merge --abort)` | **NEW** (d3's shape, this path) | 1.4, 3.1 |
| 16 | `Bash(git -C * status*)` | 53 (and d3) | P1, P8, P10 |
| 17 | `Bash(git -C * log*)` | 53 (and d3) | P3, AUTH, 1.4, 5 |
| 18 | `Bash(git -C * diff*)` | 53 (and d3) | P9, P10, 1.3, 1.4, 2.6, 2.7, 3.3, 5 |
| 19 | `Bash(git -C * rev-parse*)` | 53 (and d3) | P4, P8, P10, 1.4, 3.2, 4.3 |
| 20 | `Bash(git -C * rev-list*)` | 53 (and d3) | P9, P10, 1.3 |
| 21 | `Bash(git -C * merge-base*)` | d3 | P10, 3.3 |
| 22 | `Bash(git -C * show*)` | 53 (and d3) | 2.8, 6 |
| 23 | `Bash(cd *)` | d3 | 2.1, 2.8 |
| 24 | `Bash(uv run pytest *)` | d3 | 2.2 |
| 25 | `Bash(COBALT_ENV=dev uv run pytest *)` | d3 (09-19 R18) | 2.3 (c) |
| 26 | `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0922/.env)` | **NEW** (d3's R41 shape, this path) | 2.3 (a) |
| 27 | `Bash(rm /Users/cobalt/cobalt-wt/stacked-0922/.env)` | **NEW** (d3's shape, this path) | 2.3 (d) |
| 28 | `Bash(COBALT_ENV=production uv run cobalt validate*)` | d3 | P12, 2.4, 4.5 (f) |
| 29 | `Bash(COBALT_ENV=production uv run cobalt jobs *)` | 53 | 2.5, 4.5 (g) |
| 30 | `Bash(COBALT_ENV=production uv run cobalt heartbeat show*)` | 53 (and d3) | P12, 4.5 (e) |
| 31 | `Bash(launchctl bootout gui/501/com.cobalt.aset)` | 53 (and d3) | 4.2, 5 (1) |
| 32 | `Bash(launchctl bootout gui/501/com.cobalt.radar)` | 53 (and d3) | 4.2 / 5 (1), only if the table names the radar |
| 33 | `Bash(launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.aset.plist)` | 53 (and d3) | 4.4, 5 (3) |
| 34 | `Bash(launchctl bootstrap gui/501 /Users/cobalt/Library/LaunchAgents/com.cobalt.radar.plist)` | 53 (and d3) | same condition |
| 35 | `Bash(launchctl kickstart -k gui/501/com.cobalt.aset)` | 53 (and d3) | 4.4 |
| 36 | `Bash(launchctl kickstart -k gui/501/com.cobalt.radar)` | 53 (and d3) | same condition |
| 37 | `Bash(launchctl print gui/501/*)` | 53 (and d3) | P12, 4.2, 4.4, 4.5, 5 |
| 38 | `Bash(curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/*)` | 53 (and d3) | P12, 4.5 (c) |
| 39 | `Bash(grep *)` | 53 (and d3) | P00, AUTH, P12, 4.5 |
| 40 | `Bash(tail *)` | 53 (and d3) | P5, P6, P7, P12, 4.5 |
| 41 | `Bash(ls *)` | 53 (and d3) | P11, 2.2, 2.3, 2.8 |
| 42 | `Bash(wc *)` | 53 (and d3) | carried (byte-identical to 53's list) |
| 43 | `Bash(date*)` | 53 (and d3) | P0, 4.1, 4.3, 4.4, 5 (0) |
| deny | `AskUserQuestion` · `EnterWorktree` · `Bash(git push*)` | 53 | L63, L55 |

Totals: 29 strings are in `53`, 5 are in `d3` only (#21, 23, 24, 25, 28), and **9 are NEW** (#5, 10–15, 26, 27). No `cobalt` subcommand or flag was invented. `jobs restarts <range>` and `validate` are in `src/cobalt/jobs/cli.py:194-196` and `src/cobalt/cli.py:131`. `heartbeat show` and every `launchctl` and `git` shape appear in `53` or `d3`.

The review prompt `06` uses 9 allow strings plus 3 denies. Each counts 1 in `2026-09-21/54-review-stale-marker-deploy.md` (checked with `grep -c -F`), so it has 0 NEW.

## ESCALATE
1. **L66's text names BOTH residents; the task narrows it.** L66 reads "the deploy stops `com.cobalt.aset` and `com.cobalt.radar` … BEFORE the merge". R3 sets aside only its window ("inside the 20:00–21:00 pause"), and R3's own consequence text says "aset/radar restarted at once".
   - The desk's task (items 4 and 6) says aset only, unless the table names the radar. `05` follows the task: aset only. Its STEP-2.7 empty diff over the radar's paths proves that a KeepAlive respawn would load identical radar code.
   - The trade-off: taking the radar down during RTH would drop a live scanning session's state.
   - `ASK DESK: aset-only window vs L66's both-residents text — confirm with him or record the reading [06:5x]`. Safe default as drafted: aset only.
2. **The with-DB suite writes `cobalt_dev` under a Sonnet seat.** The task's model test looks at the branches' commits, and they carry no write path, so the seat is Sonnet. `d3` ran the same suite on Opus, but for its production migrations. `ASK DESK: keep Sonnet for a dev-lane pytest write, or seat Opus + acceptEdits [06:5x]`. Default: Sonnet, as the task set it.
3. **`jobs.yaml` → `registry; register, no restart`.** `05` does NOT run `cobalt jobs register`, which would be a production DB upsert and so would need the write-path shape. STEP-2.6 proves instead that the diff is only the nine-line `no_resident_reads` row and no job row. `ASK DESK: does he want the register run anyway (then Opus + acceptEdits) [06:5x]`. Default: not run.
4. **`53` AS WRITTEN WOULD HAVE REFUSED TODAY.** Its STEP-1 (b), `git diff --stat <cut> main -- . ':(exclude)docs'`, prints `configs/cobalt/rules.yaml`: the machine-written `generated_at`, committed inside the close commit `97ff2cf` (`docs(close): …`). Machine-written config inside a "docs" commit defeats every `exclude)docs` identity gate.
   - `05` proves identity on each branch's named paths instead (1.3). The prompt that follows `05` should do the same.
   - A fair question for the desk's close: should `rules.yaml` commits stay out of docs commits?
5. **`/Users/cobalt/cobalt-wt/ops-2026-09-17/.env` is present**: `-rw-------`, 2186 B, `Sep 17 05:50`. It is a copy of production's `.env` left in a dead worktree since 09-17 (L4). `05`'s P11 records it as known and it is not a stop. It is the desk's to remove.
6. **Approvals and a proof still to come:**
   - (a) R39 (09-21 16:48) approved the two `stale-marker rebase` strings for the "TUE 2026-09-22 evening deploy only". R3 moves the deploy to daytime, so `05`'s `R__A` row must name them again, beside the 9 NEW strings.
   - (b) Running `COBALT_ENV=production uv run cobalt validate` in a worktree with no `.env` has never been done (L70: UNPROVEN). `05` 2.4 records an environment-only failure as UNPROVEN and relies on 4.5 (f) after the merge.
7. **The rebase rewrites both branch shas.** The build lines (`ead43a0`, `af77d6b`), the check reports and R3's `ca9566f`/`8f3db83` will name pre-rebase commits. The link between them and what ships is `05`'s 1.3 path-identity proof plus P9's docs-only-above-tip proof. The report must carry both the old and new tips.
8. **DAYTIME RESTART OF THE SHEET.** At 11:00+ the radar is scanning RTH and cards are live, so the sheet (aset) is blind for about 60 s. The heartbeat may DM him a RED stamped inside the window (expected, and named in `## Smoke`). The live STALE badge is not readable by curl; the desk confirms it at the next RTH bars-poll failure. ops's include set is first exercised by the 21:40 backup, whose `backup status` the desk reads afterwards.

STACKED DEPLOY PROMPTS DRAFTED · prompts: 2 · new rule strings: 9 · restarts: com.cobalt.aset · window: 11:00–19:55 ET · ESCALATE: 8
