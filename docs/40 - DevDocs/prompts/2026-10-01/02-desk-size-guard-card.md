JOB: desk-size-guard
LADDER: OFF-LADDER — cto-2026-10-01.md 2026-10-01 R8
BRANCH: ops/desk-size-guard-1001
WORKTREE: desk-size-guard-1001
BASE: 36bed6ed
TIP:
REPORT: /Users/cobalt/cobalt-wt/desk-size-guard-1001/docs/40 - DevDocs/reports/desk-size-guard-build-2026-10-01.md
CHECK REPORT:
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-01 R8

## ROWS

| row | what | red first | files |
|---|---|---|---|
| G1 | `desk-context.sh` gains a `--guard` mode: `desk-context.sh --guard` finds the desk, measures it exactly as today (input + cache_read + cache_creation), prints nothing and exits 0 below 300,000, and at 300,000 or more prints `REFUSED: desk at <n> tokens — REFRESH first` and exits 3. The desk is the caller's own id when `basename $CLAUDE_JOB_DIR` is a live `cto-desk` row of `desk-list.sh`; otherwise the `cto-desk` row with the smallest measure (the successor during a handover). A measure that fails or no `cto-desk` row: print `WARNING: desk size unread — guard skipped` to stderr and exit 0 (the guard never blocks on its own failure; DECISION G-A). The plain `desk-context.sh <id> [threshold]` call is unchanged | test: a fixture transcript at 299,999 → exit 0, silent; at 300,000 → exit 3 with the exact REFUSED text and `<n>` = 300000; the plain call's output on the same fixture equals today's (`context 300000 of 250000 — REFRESH`). RED on `BASE`: `--guard` is read as a session id and prints `no transcript for --guard` | `ops/desk/desk-context.sh`, `tests/ops/test_desk_size_guard.py` |
| G2 | `desk-launch.sh` runs `desk-context.sh --guard` before it builds any launch, for every kind except `desk` (`build`, `check`, `deploy`, `prompt`, `close`, every resume form), and exits with the guard's status and text unchanged when it refuses. `desk-launch.sh desk` never calls it | test: guard stubbed to refuse → each of the five kinds exits non-zero with the REFUSED line and starts nothing (the stub `claude` is never called); `desk` with the same stub reaches the launch. RED on `BASE`: all five kinds reach the stub `claude` | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_size_guard.py` |
| G3 | `wait-stop-line.sh` runs `desk-context.sh --guard` first; on a refusal it prints the REFUSED line, exits 3 and never enters its loop. `wait-desk-idle.sh` and `desk-context.sh` itself are NOT guarded | test: refusing stub → exit 3, the watched file never read; passing stub → today's behaviour (match and timeout paths). RED on `BASE`: the refusing stub still reaches the loop and exits 2 on timeout | `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_size_guard.py` |
| G4 | RUN — asserts nothing. Prove the closeout always completes: with the guard refusing, quote the output of `desk-launch.sh desk`, `wait-desk-idle.sh` and `desk-context.sh <id>` (all unguarded), and `grep -n` that no hook, settings entry or script in `ops/desk/` or `.claude/` routes `git add`, `git commit`, Edit or Write through `desk-context.sh --guard` | — (tool output quoted in the report) | none (read only) |

## NOT IN THIS JOB
- Any file outside `ops/desk/` and `tests/ops/`; the symlinks under `/Users/cobalt/.claude/ops/` already point at `ops/desk/` and are not touched.
- A guard on `desk-launch.sh desk`, `wait-desk-idle.sh`, `desk-list.sh`, `git`, Edit or Write.
- The thresholds' meaning: 300,000 is his R8; the 220,000 floor and the 250,000 quiet-moment rule are the wake-up's and are not coded.
- Any change to the desk's wake-up, checklist or contract (his R8 already applied them).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-01-words.md` `## R8`.
- `ops/desk/desk-context.sh`, `ops/desk/wait-stop-line.sh`, `ops/desk/desk-launch.sh` from the top to the `desk` kind (about line 228) and each kind's launch branch.
- `/Users/cobalt/.claude/ops/desk-list.sh` (the `cto-desk` row shape).

## DECISIONS ASKED
- DECISION G-A: fail-open when the desk's size cannot be read (a warning, launch goes ahead) or fail-closed? The card ships fail-open so the closeout can never be locked out; the builder reports any path where that lets an oversized desk through.
- DECISION G-B: `close` (the nightly close) is guarded like every other kind, as written in R8; the builder reports whether that can strand a night's close when a desk sits at 300,000 or more.
