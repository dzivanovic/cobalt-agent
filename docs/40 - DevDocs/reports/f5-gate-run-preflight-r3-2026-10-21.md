# F5 gate-run 970 — preflight round 3 (THIRD PASS, read-only)

Prompt `prompts/2026-10-21/970-f5-gate-run.md`, committed at e36b1881. Read-only run; the one file written is this report.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Compared `## THIRD PASS` strings with `prompts/BUILD-HUB.md:14` and 970's MODEL line | Pass 3 uses only `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` (the two lock scripts) and `Bash(COBALT_ENV=dev uv run cobalt db *)` (`db migrate --proof-only`, `db migrate`, `db migrate --rollback --down-to 0013`). Both are on BUILD-HUB:14 byte for byte and both are on 970's MODEL line. The `ls`, `date` and run commands are strings already on the line. No `COBALT_ENV=production`, no `launchctl`, no `-c`. | OK |
| 2 | Read both lock scripts and followed each exit path of pass 3 | The order is lock (2) → note (3) → proof-only (4) → migrate up (5) → X2 then X6 (6) → rollback and proof (7) → release (8) → results (10). Release runs on success, on a failed migrate (5 → 7 → 8), on a level miss (4 → 8), and on an existing note (3 → 8). A failed rollback is the one stated exception: the lock stays held and the last line is `FAILED: pass 3 — …`. The take failing or the lock being already held goes to step 10 with nothing held. | OK |
| 3 | Read steps 4–7 | A failed migrate gives `NOT RUN — migrate failed` and the rollback still runs. A failed rollback or a proof mismatch gives no retry and no other db string, the lock stays held, and the desk decides. X2 and X6 each run once, and there is no loop. | OK |
| 4 | `ls` on the dev note path, and read `configs/dev/vault.yaml` and `configs/dev/aset.yaml:23-24` | The root is `~/dev-vault-cobalt`. The Daily Notes directory exists and `2026-10-21.md` is absent now. Step 3 re-checks with `ls` before it writes, never overwrites, and names the real vault as never written. The note stays and is "owed: the desk removes it" (step 9); no listed string removes a file. | OK |
| 5 | Read steps 1, 9 and 10 | X4 is explicitly not in pass 3. Step 10 leaves X3, X4, X5, X7, X10, X12, X13 and the values card standing, so the HIS HAND items stay NOT RUN. No plist is loaded, and the only commands are `cobalt db`, the lock scripts and the two X-run commands, all dev. | OK |
| 6 | `git diff 12405397 HEAD -- 970` | Two hunks: the MODEL line (adds the two strings and `--add-dir /Users/cobalt/dev-vault-cobalt`) and the new `## THIRD PASS`. Nothing of passes 1 or 2 changed. | OK |
| 7 | Checked every `file:line` the section cites | Present: `BUILD-HUB.md:37`, `__init__.py:198` (the 0029 line of FORWARD) and the 0029 `.sql` and `.rollback.sql`, `gate-lists.md:10-14` and `## LEVEL 0013`, `aset.yaml:23-24`, `daily.md.j2:1-66`, `cli.py` (no `dev-copy`; 0 hits), `/Users/cobalt/cobalt-wt/f5-probe`, `.f5-probe/PLACEHOLDER`. The kept csv is absent, as step 6b needs. `checkpoints.py:779` is a miss, see ISSUES 1. | OK (with NOTE) |
| 8 | Read step 10 | The stop line stays `GATES DONE · ok: <n> · fail: <n> · not run: <n>`. A `FAILED: pass 3 — …` line is stated for the rollback and release failures. | OK |
| 9 | `git diff HEAD --stat -- 970` | Empty. The amend is committed (e36b1881). | OK |

Current state: no `.cobalt_dev.lock` directory, so step 1's `ls -d` would fail as required.

## ISSUES
1. NOTE: step 6a and RULES cite `checkpoints.py:779` for the one local model call. Line 779 is `result.writes.append(write)`; the `narrate` call is at `checkpoints.py:785`. The cite was already in passes 1 and 2 and changes nothing the seat runs.
2. NOTE: the path "BUILD-HUB.md:14" is `docs/40 - DevDocs/prompts/BUILD-HUB.md`, not the repo root. The line numbers are right.
3. NOTE: step 3's "note exists" branch names only X6's result. X2 is also not run on that branch (steps 4–7 are skipped), but its line is unstated; the seat would write `NOT RUN — the note is already there` for both.
4. NOTE: step 3 does not say what happens if the Write of the note fails. The lock is held at that point; the safe reading is to go to step 8 with X2 and X6 `NOT RUN`.

Nothing blocks the launch.

PREFLIGHT DONE · prompt: 970 · checks: 9 · fails: 0 · ready: YES
