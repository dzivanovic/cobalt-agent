JOB: kill-hub-row-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R937
BRANCH: ops/kill-hub-row-1010
WORKTREE: kill-hub-row-1010
BASE: 6fe8d690
TIP: b4d82ad6
REPORT: /Users/cobalt/cobalt-wt/kill-hub-row-1010/docs/40 - DevDocs/reports/kill-hub-row-build-2026-10-10.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/kill-hub-row-check-2026-10-10.md
HOUSE B: as needed
DB: none
RULINGS: 2026-10-10 R855

## ROWS

WHY: the `--kill` row (brain R926 A, sequence R927, label fix R929-R930) is a fixed-file change, so it goes by card rows (G5, `ops/desk/bare-guard.py:1084-1089`), never in place (R932). Three edits, docs only, to the text drafted in `reports/standing-list-kill-row-2026-10-10.md`, amended in `reports/kill-sequence-amend-2026-10-10.md` and label-fixed in `reports/kill-label-fix-2026-10-10.md`. The exact OLD and NEW lines are the blocks under TEXT below; each OLD is `git show 6fe8d690:<file>` at the line named, each NEW is the label-fixed text. No row adds a command: every string typed is `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh …` (CLASS (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`, `DEPLOY-HUB.md:11`) or `date` (`Bash(date*)`, same line). No `sleep`, `pgrep` or radar call. No test under `tests/ops/` pins a line these rows move (the drafter's `grep` of `STANDING-LIST|DEPLOY-HUB` over `tests/ops`). Every row's red first ends with `uv run pytest -q tests/ops/test_hub_lines.py` → `0 failed`.

| row | what | red first | files |
|---|---|---|---|
| K1 | FIX ROUND (brain R771, L79, narrowed route; replaces the K1 NEW of the first round). DEPLOY-HUB 4.2, the orphan-clean kill sequence ONCE, AFTER the per-resident bootout loop (not inside it), `com.cobalt.aset` only. Line 137, OLD = TEXT K1 OLD, NEW = TEXT K1 NEW: the one insertion between "still → STEP-5 (nothing merged)." and "If `com.cobalt.agent` is in the set:"; the rest of the line stands byte for byte. The sequence: (1) dry run → `date` → (2) the same dry run, the same pid set, still ppid 1 and `-m cobalt.aset`; (3) ONE `--kill aset`; (4) dry run clean; (5) go on (the agent step, then 4.3). A difference at (2), an orphan at (4), exit 1 or `FAILED: <pid> survived KILL` → no second kill, STEP-5 (nothing merged), FOR DEJAN; the pids go under `## RECORDS` and into `DECISION 0: aset orphan … — FOR DEJAN`, the named line STEP-7 (3) already fills. Backed by `reports/kill-sequence-amend-2026-10-10.md` RECORDS line 1, `reports/kill-label-fix-2026-10-10.md`, `ops/desk/orphan-clean.sh:76-82` (the label table: `aset` only), `:174`, `:250`, `:252` (the printed lines) | `grep -c -F -e "ORPHAN-CLEAN, aset only" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → 1 (`:137`); on `BASE` → 0. `grep -c -F -e "orphan-clean.sh --kill aset"` on the same file → 1 after K1 and K2 (`:137` only; none in `:162`), 0 on `BASE`. `grep -c -F -e "survived KILL"` → 1. `grep -c -F -e "--kill com.cobalt.aset"` → 0 before and after. `uv run pytest -q tests/ops/test_hub_lines.py` → `0 failed` | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| K2 | FIX ROUND (brain R771, L79; replaces the K2 NEW of the first round). DEPLOY-HUB STEP-5 (3) THE RESTORE: NO `--kill`, the dry run ONLY, before aset's bootstrap. Line 162, OLD = TEXT K2 OLD, NEW = TEXT K2 NEW: the dry run is put first, and the old bootstrap sentence follows as "Then `launchctl bootstrap` each resident booted out, …" with its tail unchanged (no hold-down, no new rule-F ending). A verified orphan or exit 1 → no kill, `DECISION 0: aset orphan … — FOR DEJAN`, the run ends under the existing DECISION 0 path, residents per rule F unchanged. Backed by `reports/kill-sequence-amend-2026-10-10.md` RECORDS line 2, `reports/kill-label-fix-2026-10-10.md` | `grep -c -F -e "(dry run ONLY, no kill)" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` → 1 (`:162`); on `BASE` → 0. `grep -c -F -e "orphan-clean.sh aset" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` (the dry run) → 2 (`:137`, `:162`); on `BASE` → 0. `grep -c -F -e "the kill sequence:"` on the same file → 1 (`:137`); on `BASE` → 0. `grep -c -F -e "not held DOWN"` → 0. `wc -l` of the file → 181 before and after (K1 and K2 change lines, add none). `uv run pytest -q tests/ops/test_hub_lines.py` → `0 failed` | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |
| K3 | FIX ROUND (brain R771, L79; replaces the K3 TEXT of the first round: names 4.2 ONLY, nothing else changes). STANDING-LIST, ONE new row in the deploy hub's allow table: the `orphan-clean.sh --kill aset` use of the existing CLASS (a) string, scoped to the deploy hub, 4.2 only, in the R927 sequence only. TEXT K3 is inserted as a new line after line 148 (the `Bash(launchctl print gui/501/*)` row) and before line 149 (the `Bash(/Users/cobalt/cobalt/cobalt.sh status)` row); no other line changes. The row carries no DRAFT or "awaiting his yes" wording (R929). Backed by `reports/standing-list-kill-row-2026-10-10.md`, `reports/kill-sequence-amend-2026-10-10.md` RECORDS line 3, `reports/kill-label-fix-2026-10-10.md`; card `prompts/2026-10-10/229-orphan-clean-card.md` O1 (`aset` → job `com.cobalt.aset`) | `grep -n -F -e "killing the orphaned" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → one hit, `:149`; on `BASE` → no hit, exit 1. `grep -c -F -e "orphan-clean.sh --kill aset"` on the same file → 1; on `BASE` → 0. `wc -l` → 221 after, 220 on `BASE`. `uv run pytest -q tests/ops/test_hub_lines.py tests/ops/test_desk_launch_brain.py` → `0 failed` (the second reads `STANDING-LIST.md` `## 7.`) | `docs/40 - DevDocs/prompts/STANDING-LIST.md` |

TEXT K1 OLD (`DEPLOY-HUB.md:137` at `BASE`, whole line):

```text
4.2 for each of `com.cobalt.aset`, `com.cobalt.radar` in `<restart set>`: `launchctl bootout gui/501/<label>`; `launchctl print gui/501/<label>` → `Could not find service` (exit 113); still loaded → one `date`, print again; still → STEP-5 (nothing merged). If `com.cobalt.agent` is in the set: `/Users/cobalt/cobalt/cobalt.sh stop` → `Cobalt stopped safely.`; `ps -p <agent pid>` → header only.
```

TEXT K1 NEW (FIX ROUND, replaces the K1 NEW of round 1, whole line; `--kill` once, after the loop, `com.cobalt.aset` only):

```text
4.2 for each of `com.cobalt.aset`, `com.cobalt.radar` in `<restart set>`: `launchctl bootout gui/501/<label>`; `launchctl print gui/501/<label>` → `Could not find service` (exit 113); still loaded → one `date`, print again; still → STEP-5 (nothing merged). AFTER the loop, ONCE, if `com.cobalt.aset` is in `<restart set>` (ORPHAN-CLEAN, aset only; radar: no call, the script REFUSES it): the kill sequence: (1) `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` (dry run) → last line `orphan-clean: aset · none found`, or `… dry-run · verified 0 …` = clean, no kill, go on; `… verified <n>` with n ≥ 1 (`WOULD KILL: <pid>`) = a verified orphan holds the voice lock, its pids into `## RECORDS`; (2) `date`, then the SAME dry run → the same pid set, still ppid 1 and `-m cobalt.aset`; (3) `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh --kill aset` once; (4) the dry run again → `none found` or `verified 0`; (5) go on (the agent step below, then 4.3). Any difference at (2), any orphan at (4), or exit 1 (`REFUSED:` / `UNVERIFIED:` / `FAILED: <pid> survived KILL`) → no second kill, STEP-5 (nothing merged), `DECISION 0: aset orphan <pids or the line> — FOR DEJAN`. If `com.cobalt.agent` is in the set: `/Users/cobalt/cobalt/cobalt.sh stop` → `Cobalt stopped safely.`; `ps -p <agent pid>` → header only.
```

TEXT K2 OLD (`DEPLOY-HUB.md:162` at `BASE`, whole line):

```text
- (3) THE RESTORE: `launchctl bootstrap` each resident booted out, with 4.6's single retry and single `kickstart -k`; `launchctl kickstart gui/501/com.cobalt.agent` if stopped.
```

TEXT K2 NEW (FIX ROUND, replaces the K2 NEW of round 1, whole line; no kill here):

```text
- (3) THE RESTORE: aset booted out → `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset` (dry run ONLY, no kill) → `none found` or `verified 0` = go on; `verified <n>` ≥ 1 or exit 1 = `DECISION 0: aset orphan <pids or the line> — FOR DEJAN`, the run ends under that DECISION 0, residents per rule F. Then `launchctl bootstrap` each resident booted out, with 4.6's single retry and single `kickstart -k`; `launchctl kickstart gui/501/com.cobalt.agent` if stopped.
```

TEXT K3 (FIX ROUND, replaces the K3 TEXT of round 1; the new `STANDING-LIST.md:149`, whole line, inserted after `BASE` line 148; names 4.2 only):

```text
| `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` called as `orphan-clean.sh --kill aset` (CLASS (a); brain R926 A; card `prompts/2026-10-10/229-orphan-clean-card.md`) | killing the orphaned `-m cobalt.aset` process that holds the voice lock: ONLY in the deploy hub, at 4.2 once after the per-resident bootout loop, and ONLY in this sequence: (1) dry run → a verified orphan (ppid 1, `-m cobalt.aset`, not launchd's pid); (2) `date`, then the SAME dry run → the same pid set, still ppid 1 and `-m cobalt.aset`; (3) `--kill` once; (4) a dry run → no orphan; (5) go on to 4.3; any difference at (2), any orphan at (4) or exit 1 → no second kill: STEP-5 ending FOR DEJAN; a first dry run that finds nothing → no kill, the run continues | the verified orphan pid(s) of `com.cobalt.aset` | any other seat; any other label (radar is REFUSED by the script; a new label is a new card); never standing outside 4.2 (STEP-5 runs the dry run only); never without a prior dry run that printed a verified orphan |
```

## NOT IN THIS JOB
- THE MERGE. BUILT and CHECK DONE stop at this branch's tip; no deploy card, no merge to `main`, until his yes (R926, R937). The desk asks him after the check.
- Any other line of `DEPLOY-HUB.md` or `STANDING-LIST.md`: `DEPLOY-HUB.md:145` "the SAME pid" (the restart-set check) stays; every other `com.cobalt.aset` names the launchd job and stays (`reports/kill-label-fix-2026-10-10.md` DECISIONS).
- The launch line (`DEPLOY-HUB.md:11`), any allow string, any hub title or INSTALLED line, `BUILD-HUB.md`, `CHECK-HUB.md`, `DEVFIX-HUB.md`.
- `ops/desk/orphan-clean.sh` (deployed `26143007`, card 229) and any file under `ops/`, `tests/` or `.claude/`.
- A radar label, a `pgrep` line, a `sleep` or a 30 s wait (R926: no radar call; `date` plus the dry run twice, no wait).
- A rename of any prompt to pass G7: the check's Grok read runs under the check hub's own G9 (`ops/desk/bare-guard.py:1034-1035`).
- A new command of any kind (R411, R412): a row that needs one is not built; the build stops with `decisions: 1`.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/standing-list-kill-row-2026-10-10.md` (whole); `reports/kill-sequence-amend-2026-10-10.md` (whole); `reports/kill-label-fix-2026-10-10.md` (whole); `reports/kill-row-preflight-2026-10-10.md` `## ISSUES` and `## FOR THE GROK READ`.
- `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` lines 11, 135-137, 145, 158-163; `docs/40 - DevDocs/prompts/STANDING-LIST.md` lines 140-152 (the deploy hub's allow table).
- `ops/desk/orphan-clean.sh` lines 2-7 (usage), 67-83 (arguments and the label table), 174, 250, 252 (the printed lines).
- `docs/40 - DevDocs/prompts/2026-10-10/229-orphan-clean-card.md` row O1.
- Precedent: `prompts/2026-10-05/26-hub-text-card.md` (a docs-only hub-text card).

## CHECK ASKS
- X1 The label literal at K1 (3), K2 (3) and the K3 row: is each exactly what `orphan-clean.sh` accepts (`aset`, `:76-82`), and does every dry-run last line the text names match `:174` and `:252`?
- X2 The stop rules: 4.2 ends in STEP-5 with nothing merged and each pid in `## DECISIONS`; STEP-5 (3) keeps residents down with `DECISION 0 … FOR DEJAN`. Can either path reach a second `--kill`, a loop, or enter STEP-5 twice (`DEPLOY-HUB.md` STEP-5 (5): "STEP-5 is never entered twice")? Trace a 4.2 failure into STEP-5 (3).
- X3 The K3 row's scope against CLASS (a): `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` already allows `--kill` on every hub line, so the row is a rule, not a permission. Is any other line or seat implied to run it?
- X4 Is the diff `<BASE>..<TIP>` exactly the three TEXT blocks (two changed lines, one added line), every other byte equal (`git diff --numstat <BASE> <TIP>` → `2 2` and `1 0`)?
- X5 K2: "each resident booted out and not held DOWN" — does any later step (STEP-5 (4) re-run, (5) the last line's `aset: <UP|DOWN>`) read the held-down aset correctly?

## RECORDS
- `git -C /Users/cobalt/cobalt log --oneline -1` → `6fe8d690 docs(desk): X29 deploy card 285, tip 3c00e204` (the drafter, 2026-10-10, `date` 15:20 EDT). The last commit touching either file: `7bc283fe` (M6, R839). `git -C /Users/cobalt/cobalt diff --stat HEAD -- <both files>` printed nothing: main's working files equal `BASE` (the restore, `reports/restore-hub-text-2026-10-10.md`).
- At `BASE`: `DEPLOY-HUB.md` 181 lines, `STANDING-LIST.md` 220 lines; line 137 begins `4.2 for each of`, line 162 begins `- (3) THE RESTORE:`, line 148 is the `Bash(launchctl print gui/501/*)` row, line 149 the `Bash(/Users/cobalt/cobalt/cobalt.sh status)` row (Read tool on the files equal to `BASE`).
- At `BASE`, `grep -c -F -e` on both files → 0 each for "orphan-clean.sh --kill aset", "the kill sequence:", "orphan-clean.sh aset", "--kill com.cobalt.aset", "killing the orphaned", "each resident booted out and not held DOWN", "ORPHAN-CLEAN, aset only".
- SOURCE OF THE NEW TEXT: the label-fixed copies the Grok re-read staged, `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-row/DEPLOY-HUB.md` (181 lines) and `STANDING-LIST.md` (221 lines). `git -C /Users/cobalt/cobalt diff --no-index` of each against main's file shows exactly the K1, K2 hunks and the K3 line, nothing else. In them: "orphan-clean.sh --kill aset" at `DEPLOY-HUB.md:137`, `:162` and `STANDING-LIST.md:149`; "--kill com.cobalt.aset" 0; the other markers 1 or 2 as the rows state.
- RESTARTS: every path is `docs/**` (DOCS, no resident); `DB: none`. RESTARTS none.
- The check is house A Grok, and that read IS the L67 read of the `--kill` text (R932); the earlier seat's Grok call was refused by G7 (`reports/kill-row-grok-read-2026-10-10.md`), which the check hub's G9 does not meet.
