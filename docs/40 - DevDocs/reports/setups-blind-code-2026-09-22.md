# Setups Blind Code Seat — 2026-09-22

## §0 Headline
Stopped at PREFLIGHT: the fix round (`15`, `setups-fix-r2-2026-09-22.md`) is still `(run in progress)` against `/Users/cobalt/cobalt-wt/setups-c1` — the exact source this seat would stage. AUTHORIZATION passed in full (Grok, LINE-G, R25/R23 all verified, committed on main). No packet staged, no house launched. ESCALATE: 0 (a preflight gate, not a finding).

## AUTHORIZATION
- Launch row: `cto-2026-09-22.md:33` `R25` filled (DESK LAUNCH ROW, "APPLIED: launch row (this)"). Committed: `git log -S"23-setups-blind-code-seat.md"` → `d86b973`.
- Context rows: `R12` (:30, the check), `R15` (:43, hand seat `17`), `09-21 R39` (:50, "All approved" — `Bash(grok *)` / `Bash(agy *)` through 2026-09-22 23:59 ET), `09-21 R49` (:60, "Approved" — Sol READ-ONLY string; does NOT cover `-s workspace-write`, recorded as context only).
- Seven read strings (`Bash(git … show*)`, `Bash(git … log*)`, `Bash(ls *)`, `Bash(grep *)`, `Bash(tail *)`, `Bash(wc *)`, `Bash(date*)`), three deny strings (`AskUserQuestion`, `EnterWorktree`, `Bash(git push*)`), `--add-dir` triplet (Vault, cobalt, cobalt-wt) — each `grep -c -F` against `66-setups-one-check.md` ≥1.
- `Bash(grok *)` ≥1 in `66`. `Write(/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/**)` ≥1 in `66`.
- Grok run-form precedent: `Bash(python3 …/scratch/toy-check-grok/*)` ≥1 in `audit-house-2026-09-16.md`.
- NEW STRING (Grok, the house in use — date 2026-09-22 < 2026-09-26, so LINE-S/Sol's string not required): `Bash(python3 /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/setups-blind-code/*)` found at `cto-2026-09-22.md:35` `R23` — carries "approved" in his words. Committed: `git log -S<string>` → `d86b973`.
- Result: **all gates pass.** No FAILED.

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| date gate | `date` | 0 | `Tue Sep 22 12:41:33 EDT 2026` → `<D>` = 2026-09-22, before 23:59 ET → HOUSE = Grok (LINE-G) |
| house probe | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — no METER/HARNESS line |
| STAGGER (house lane) | `tail -n 1 float-handicap-tribunal-r2-2026-09-22.md` | 0 | `FLOAT HANDICAP TRIBUNAL R2 DONE · …` — starts DONE, gate clear |
| fix round not editing worktree | `ls setups-fix-r2-2026-09-22.md` | 0 | present |
| fix round last line | `tail -n 1 setups-fix-r2-2026-09-22.md` | 0 | `(run in progress — row 0 of 6, next under ## CONTINUE)` — does NOT start `SETUPS FIX R2 BUILT` or `FAILED` |

**GATE FAILS HERE.** Per this file's own rule: "present → `tail -n 1` of it must START `SETUPS FIX R2 BUILT` or `FAILED`, else `FAILED PREFLIGHT: 15 is editing setups-c1 — the source you would stage is in flight`." The fix round (`15`) is actively running against `/Users/cobalt/cobalt-wt/setups-c1` — the exact source (tests, fixtures, `src/cobalt/radar`, etc.) this seat would stage byte-identical. Staging now risks a mid-edit read: a file half-written, a fixture mid-cut, or a value that changes under the house's feet during its 60-minute run. No further preflight rows run; no packet staged; no house launched.

## Packet
Not reached — PREFLIGHT gate failed before staging.

## House
Not reached — no house launched.

## Program
Not reached.

## ORDER
Not reached.

## Comparison
Not reached — 0 of 17 fields answered.

## ESCALATE
None — the stop is a PREFLIGHT gate (the fix round in flight), not a defect or a judgement call.

## CONTINUE
next: relaunch this seat once `setups-fix-r2-2026-09-22.md`'s last line starts `SETUPS FIX R2 BUILT` (or `FAILED`, in which case the desk decides whether the pinned files moved). RECOVERY (L60): a relaunch re-runs this PREFLIGHT row first — the packet folder was never created, so nothing needs re-staging.

FAILED PREFLIGHT: 15 is editing setups-c1 — the source you would stage is in flight
