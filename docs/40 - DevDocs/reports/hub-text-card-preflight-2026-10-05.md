# hub-text card (26) — preflight, 2026-10-05

CARD: `prompts/2026-10-05/26-hub-text-card.md` (committed `f0045dfc`). The DRAFT REPORT file was not read: every check ran against the card, git and the hubs. The three hubs are unchanged `a09ee1f0..HEAD`, so a read of the tree is a read at BASE.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a09ee1f0 main` | exit 0, no output | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/hub-text-1005` | `fatal: Needed a single revision` (branch is new) | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/hub-text-1005` | `No such file or directory` | OK |
| 1d | card header read | `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `DB: none`; `HOUSE A: none — overruled 2026-10-05 R412` | OK |
| 2 | `grep -n "^| R412 " …cto-2026-10-05.md` | line 109: `HIS RULING: drop pre-merge (d2) from DEPLOY-HUB …` · `APPROVED (…)` | OK |
| 2b | `git log -1 --format=%h -S"\| R412 \|" -- …cto-2026-10-05.md` | `b3583b28` (committed) | OK |
| 3-F1 | `grep -n -F` of each OLD at BASE: `DEPLOY-HUB.md:26` (L43 / L66 sentence), `:57` (whole P1 bullet), `:93` (whole STEP-R "P1 (v) RE-READ" bullet, ends "the window D2.6 reads."), `:134` (D2.6 clock clause + `git tag pre-<JOB>`) | one hit each, at the named line, byte for byte | OK ×4 |
| 3-F2 | `DEPLOY-HUB.md:26` "L68 the integrated gate before the merge ·"; `CHECK-HUB.md:117` "a deploy is gated on the combined tree (L68)." | one hit each (`:26`, `:117`) | OK ×2 |
| 3-F3 | `CHECK-HUB.md:124` "NO FURTHER HOUSE AND NO THIRD PASS."; `BUILD-HUB.md:109` "NEXT STEP, not yours: the desk verifies the artifact (L35) and launches the check." | one hit each | OK ×2 |
| 3-F4 | `BUILD-HUB.md:106` end "decisions: <n> · for Dejan: <n>`"; `CHECK-HUB.md:127`, `:129` same end; `CHECK-HUB.md:58` "You write no token figure: the total is the desk's measurement (L70)."; `DEPLOY-HUB.md:181` end; `:178` "then the stop line, LAST non-blank line."; `:26` "· L70 unproven is never a defect" | each at the named line | OK ×7 |
| 3-F5 | `DEPLOY-HUB.md:101` the whole (d2) bullet (three-fragment `grep -c -F` → 1, line 101); `:74` "G (d2), STEP-R, D1, D2.4" | present at `:101`, `:74` | OK ×2 |
| 4-F1 | `grep -c -F -e` the seven new strings (all F1–F5) over the three hubs | `0`, `0`, `0` (all NEW strings absent at BASE) | OK |
| 4-F1b | old strings at BASE: `20:00` → `:26`, `:57`; `04:00` → `:26`, `:57`, `:134`; `(v) provisional` → `:57`, `:93`; `window closed at` → `:134`; `grep -n -i window` → `:26`, `:57`, `:93`, `:134` | all present; the four edits remove every one, so the "only the two new sentences" claim holds | OK |
| 4-F4 | `grep -c -F "for Dejan: <n>\`"` at BASE | `BUILD-HUB.md:2`, `CHECK-HUB.md:3`, `DEPLOY-HUB.md:2`. The card expects 0 after. The rows edit only the stop-line shapes (`BUILD:106`, `CHECK:127,129`, `DEPLOY:181`). Three prose lines that quote the shape stay: `BUILD-HUB.md:43`, `CHECK-HUB.md:58`, `DEPLOY-HUB.md:50` ("The stop line carries `decisions: <n> · for Dejan: <n>`") | **FAIL** |
| 4-F5 | `grep -n -F -e "(d2)" -e "--no-db" -e "jobsG"` at BASE | `(d2)` lines 74, 101 → 2; `--no-db` line 101 → 1; `jobsG` line 101 → 1 | OK |
| 5 | read `tests/ops/test_hub_lines.py` | pins: the one `claude --bg ` line of each of the four hubs (allow/deny strings, the flag), the `- LAUNCH ` line of `CTO-DESK-WAKEUP.md`, `CHECK-HUB.md`'s `- **GROK:** ` line, and `DEPLOY-HUB.md` STEP-G `- (f) `. No row touches any of them: F5 deletes `(d2)` and edits line 74 only, and `:11`, `(f)` `:151` and the GROK line stand | OK |
| 6 | read the rows; `ls /Users/cobalt/cobalt/ops/desk/desk-context.sh`; `grep -n -F "uv run cobalt validate"` | the token sentence types `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh <id>`, an existing script under CLASS (a); F5 only removes a command; `:11` allow string, 4.5 (`:141`), smoke (f) (`:151`) stand; every named file is a `prompts/` hub, none under `ops/desk/` | OK |
| 6b | X4 pre-read: `desk-done.sh:22-25`, `desk-watch.sh:38-41` | match only the line start `^BUILT`, `^(CHECK DONE\|FAILED)`, `^DEPLOYED`; no field position, so a last field `tokens: <n>` breaks nothing (`wait-stop-line.sh` not opened) | OK (note) |
| 7a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 7b | `git diff --stat -- <card>`; `git log -1 --format=%h -- <card>` | empty; `f0045dfc` | OK |

checks: 24 · fails: 1

## ISSUES
- 4-F4: the red-first `grep -c -F "for Dejan: <n>\`"` → 0 on each hub cannot hold after the rows. `BUILD-HUB.md:43`, `CHECK-HUB.md:58` and `DEPLOY-HUB.md:50` describe the stop line in prose and keep that string. After the build the counts are BUILD 1, CHECK 1, DEPLOY 1. Fix the card either way: expect those counts, or add rows that also bring the three prose lines to `· tokens: <n>`. Otherwise the prose names a shape the stop line no longer has.
- Note, not a FAIL (X2 for the check): `DEPLOY-HUB.md:141` (4.5) accepts "exit 0 (or exactly `<val0>`'s `docs/_inflight/` lines)" and does not name `RETIRE OWED`. With (d2) gone, a `registry <-> plists` line for a retired label would fail 4.5 → STEP-5. That is a `## DECISIONS` item.
- Note: F4(b) is applied after F2 on line 26. F2's NEW text ends "(his R390) ·" and F4's OLD begins "· L70", so the result reads "(his R390) ; a set that…" with a stray space before the semicolon. Cosmetic.

PREFLIGHT DONE · card: hub-text-26 · checks: 24 · fails: 1 · ready: NO
