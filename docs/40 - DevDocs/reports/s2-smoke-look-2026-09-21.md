# S2 Smoke Look — night of 2026-09-21 (first look)

## §0 Headline
- STEP 1 window check failed: `date` = `Tue Sep 22 06:32:51 EDT 2026`, past the 23:30 ET cutoff for the 09-21 run window (21:20–23:30 ET).
- Authorization was verified first (per the prompt's order) and is clean: R43 row in `cto-2026-09-21.md` quotes "App approved" against the smoke string, and `git log -S"cobalt smoke s2 --prod" -- "docs/40 - DevDocs/reports/cto-2026-09-21.md"` returns `f5c5bf0`.
- No replay-log read, no smoke run, no K-check table: the run stops at STEP 1, before those steps execute.
- Report file did not exist before this write.

## Authorization check
| check | result |
|---|---|
| `grep -c -F` R43 smoke string in `cto-2026-09-21.md` | 1 (R43 row, 17:31 ET, "App approved") |
| `git log -1 -S"cobalt smoke s2 --prod"` on that file | `f5c5bf0f35ff2786b8fea70983bd250b35bf0918` (non-empty) |

## ESCALATE
None — this is a window failure, not a defect (L70: unrun checks are UNPROVEN, never a defect).

## DIGEST FOR THE DESK
Hub started well outside the 21:20–23:30 ET window for the 09-21 night (`date` = 06:32 ET Tue 09-22), so STEP 1 stopped the run before any log read or smoke call. Authorization itself was sound (R43 quote + matching commit). Nothing was read from the replay logs and the smoke command was never invoked — no findings, expected or otherwise, were produced. This run does not close S2 in any case; the run that counts is TUE 09-22 / WED 09-23 evening per BACKLOG. If a first look at the 09-21 night's replay is still wanted, it needs a fresh timer inside window, or an explicit desk waiver of the window gate for this one run.

FAILED: window — too late
