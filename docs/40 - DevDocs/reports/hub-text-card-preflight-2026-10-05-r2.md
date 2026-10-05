# hub-text card (26) — preflight round 2, 2026-10-05

CARD: `prompts/2026-10-05/26-hub-text-card.md` (last commit `98d77082`, amended with rows F6–F8). Hubs and `tests/ops/test_hub_lines.py` are unchanged `a09ee1f0..HEAD` (`git diff --stat` empty), so `git grep … a09ee1f0` reads BASE.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor a09ee1f0 main` | exit 0, no output | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/hub-text-1005` | `fatal: Needed a single revision` | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/hub-text-1005` | `No such file or directory` | OK |
| 1d | card header lines 1–12 | `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `DB: none`; `HOUSE A: none — overruled 2026-10-05 R412` | OK |
| 2a | `grep -n "^| R412 " …/cto-2026-10-05.md` | `109:\| R412 \| … HIS RULING: drop pre-merge (d2) from DEPLOY-HUB … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a)` | OK |
| 2b | `git diff --stat -- <card> cto-2026-10-05.md` | empty (committed, clean); card last commit `98d77082` | OK |
| 2c | `grep -n "^| R425 " …/cto-2026-10-05.md` | `133:\| R425 \| … DESK RECORD: brain ruled … (2) card 26 rows for BUILD-HUB:43, CHECK-HUB:58, DEPLOY-HUB:50 … \| RECORD` | OK |
| 3-F1 | `git grep -n -F` of each OLD at BASE | `DEPLOY-HUB.md:26` (L43 / L66 sentence), `:57` (whole P1 bullet), `:93` (STEP-R "P1 (v) RE-READ" bullet, ends "the window D2.6 reads."), `:134` (D2.6 clock clause + `git tag pre-<JOB>`): one hit each, byte for byte | OK ×4 |
| 3-F2 | same: `DEPLOY-HUB.md` "L68 the integrated gate before the merge ·"; `CHECK-HUB.md` "a deploy is gated on the combined tree (L68)." | `DEPLOY-HUB.md:26`; `CHECK-HUB.md:117` | OK ×2 |
| 3-F3 | `CHECK-HUB.md` "NO FURTHER HOUSE AND NO THIRD PASS."; `BUILD-HUB.md` "NEXT STEP, not yours: the desk verifies the artifact (L35) and launches the check." | `CHECK-HUB.md:124`; `BUILD-HUB.md:109` | OK ×2 |
| 3-F4 | `BUILD-HUB.md` end "decisions: <n> · for Dejan: <n>`"; `CHECK-HUB.md` same end; "You write no token figure: the total is the desk's measurement (L70)."; `DEPLOY-HUB.md` end, "then the stop line, LAST non-blank line.", "· L70 unproven is never a defect" | `BUILD-HUB.md:106`; `CHECK-HUB.md:127`, `:129`, `:58`; `DEPLOY-HUB.md:181`, `:178`, `:26` | OK ×7 |
| 3-F5 | `DEPLOY-HUB.md` "(d2) VALIDATE, right before the gate call", the tail "on that tree's own `.env` … `FAILED: G (d2) — <line> · rollback: not used`.", the `--no-db` sentence; "G (d2), STEP-R, D1, D2.4" | `:101` (three fragments, one hit each); `:74` | OK ×2 |
| 3-F6/7/8 | `BUILD-HUB.md` "The stop line carries `decisions: <n> · for Dejan: <n>`."; `CHECK-HUB.md` "The stop line carries `decisions: <n> · for Dejan: <n>`; `decisions: 0` →"; `DEPLOY-HUB.md` "The stop line carries `decisions: <n> · for Dejan: <n>`. For a DEPLOY report" | `BUILD-HUB.md:43`; `CHECK-HUB.md:58`; `DEPLOY-HUB.md:50` — one hit each, byte for byte | OK ×3 |
| 4-new | `git grep -c -F` at BASE of every NEW string: `for Dejan: <n> · tokens: <n>`, `tokens: <n>`, `desk-context.sh <your session id>`, `No restart window binds a deploy`, `no per-night count binds it`, `recorded in the row`, `each feature deploys alone`, `each feature deploying alone`, `(L75, his R376)`, `first runs the gate on the merged hub text` | no output on all three hubs (0 each, so the NEW strings are absent) | OK |
| 4-old | `git grep -c -F` at BASE of `(d2)`, `--no-db`, `jobsG`, `20:00–21:00`, `04:00 ET`, `(v) provisional`, `window closed at` | `DEPLOY-HUB.md:6` matching lines, all present (F5's `(d2)` 2 lines `:74`, `:101`; `--no-db` and `jobsG` `:101` only, per the line reads above) | OK |
| 4-F4 | `git grep -c -F "for Dejan: <n>\`"` at BASE | `BUILD-HUB.md:2`, `CHECK-HUB.md:3`, `DEPLOY-HUB.md:2`: matches the card's "at BASE 2 / 3 / 2". After: BUILD `:106` + `:43` (F6) = 2; CHECK `:127` `:129` + `:58` (F7) = 3; DEPLOY `:181` + `:50` (F8) = 2; the old form → 0/0/0. The F4 sentence for `CHECK-HUB.md:58` and `DEPLOY-HUB.md:178` carries no `for Dejan` text, so it does not change either count. Round 1's FAIL is fixed by F6–F8 | OK |
| 4-F4b | `grep -n -F "for Dejan: <n>\`"` on `CHECK-HUB.md` at BASE | `:58`, `:127`, `:129` — no other line | OK |
| 5 | read `tests/ops/test_hub_lines.py` | pins: the one `claude --bg ` line of each of the four hubs, the `- LAUNCH ` line of `CTO-DESK-WAKEUP.md`, `CHECK-HUB.md`'s `- **GROK:** ` line, `DEPLOY-HUB.md` STEP-G `- (f) ` (needs "the ROLLBACK command of", `ops/desk/gate-lists.md`, `<FP>`). Rows edit `:26 :50 :57 :74 :93 :101 :134 :178 :181` (DEPLOY), `:43 :58 :117 :124 :127 :129` (CHECK), `:43 :106 :109` (BUILD): none is a `claude --bg ` line, the GROK line or `(f)` (`:107`); deleting `:101` leaves `(f)` the one `- (f) ` line in STEP-G | OK |
| 6a | read the rows; `sh …/ops/desk/desk-context.sh 6e237084` | the token sentence types `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh <id>`: an existing script, CLASS (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` on `BUILD-HUB.md:12`; it printed `context 63374 of 400000 — ok`. F5 only removes a command; no `--no-db` allow string | OK |
| 6b | files named by the rows | `DEPLOY-HUB.md`, `CHECK-HUB.md`, `BUILD-HUB.md` under `docs/40 - DevDocs/prompts/`; none under `ops/desk/` | OK |
| 6c | X4 pre-read: `desk-done.sh:22-24`, `desk-watch.sh:39-40`, `wait-stop-line.sh:37,43` | `desk-done.sh` `done_re='^BUILT'` / `'^CHECK DONE'` / `'^DEPLOYED'`; `desk-watch.sh` `re='^(CHECK DONE\|FAILED)'`, `'^(DEPLOYED\|FAILED)'`; `wait-stop-line.sh` `lastline()` takes the last non-blank line and its `awk -F ' · '` reads `desk-list.sh` rows, not the stop line. No field position: an added last field breaks none | OK |
| 7a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 7b | `git diff --stat -- <card>`; `git log -1 --format=%h -- <card>` | empty; `98d77082` | OK |

## ISSUES
none that fail a check. Notes for the check, not FAILs:
- X2: `DEPLOY-HUB.md:141` (4.5) reads "exit 0 (or exactly `<val0>`'s `docs/_inflight/` lines)" and does not name `RETIRE OWED` (`:87`, `:176` record it). With (d2) gone, a `registry <-> plists` line for a retired label would fail 4.5 → STEP-5. A `## DECISIONS` item, not a fix in this job.
- Cosmetic: F4(b) applied after F2 on `DEPLOY-HUB.md:26` leaves "(his R390) ; a set that changes …" with a stray space before the semicolon.

PREFLIGHT DONE · card: hub-text-26 · checks: 27 · fails: 0 · ready: YES
