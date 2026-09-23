# Deploy fold — 2026-09-23 (`07` re-issued in place, L19)

## §0 Headline
- `prompts/2026-09-23/07-stacked-deploy.md` re-issued in place: `08`'s folds 2, 3, 4, 5 and 6 applied; fold 1 (P6, already folded by the desk under R26) verified and left unchanged.
- 2 strings narrowed, 0 widened, 0 added. Allow count unchanged at 54 (the file has 55 `"Bash(` = 54 allow + 1 deny `git push*`).
- `R__A` / `R__L` kept: `grep -n -E "R_[_]"` still hits 11 lines (12, 37, 49, 50, 54, 56, 62, 123, 148, 151, 153), the same count `08` recorded.
- Not committed (no git write in this seat). File went from 371 to 372 lines. Diff taken against a copy made before the edit (`$CLAUDE_JOB_DIR/tmp/07-before.md`).
- ESCALATE: 5.

## Folds
| fold | where (line) | before | after | backed by (`08` `## Checked against the files`) |
|---|---|---|---|---|
| 1 P6 (blocker) | 148 | desk's R26 text | **unchanged** — verified, see below | row 1 (HOLDS, blocker) |
| 2 STEP-4.6 `<t up>` | 279, 283 | 279 ended `… com.cobalt.radar.plist`. Then `date` = `<t up>`.` (before the retry and kickstart bullets) | 279 ends at the second bootstrap. New line 283 comes after the kickstart bullet: `Then, once both show `state = running` (every retry and kickstart above resolved), `date` = `<t up>`.` | row 2 (gemini, HOLDS) |
| 3 RELAUNCH RULE (ii) | 256 | `… already recorded (STEP-3.2), so a revert was interrupted. Go to STEP-5 (2) at once, …` | `… already recorded (STEP-3.2). FIRST read the earlier run's stop line (the last non-blank line above `# SECOND RUN`): if it is a `FAILED:` line carrying `rollback: used`, STEP-5 already completed — do NOT re-enter it; end `FAILED: relaunch — STEP-5 already completed; the desk decides · rollback: used`. Otherwise a revert was interrupted. Go to STEP-5 (2) at once, …` | row 9 (opus, HOLDS textual gap). The key is `rollback: used`, not the literal `FAILED: STEP-5` — see ESCALATE 3 |
| 4 STEP-4.4 routing | 277 | `- A non-zero exit, a `CHANGED`, or a `CREATED` → STEP-5, …` | `- A non-zero exit, a `CHANGED`, a `CREATED`, or an incomplete or missing proof table (a tool timeout included) → STEP-5, …` (the existing tail `with migration 0013 applied: <yes\|no from the read-back>` already routes that case through the read-back) | row 10 (opus, HOLDS plausible ambiguity) |
| 5 launch line | 6 | `"Bash(COBALT_ENV=production uv run cobalt jobs *)"` | `"Bash(COBALT_ENV=production uv run cobalt jobs restarts *)"` | row 7 (gemini + opus, HOLDS) |
| 6 launch line | 6 | `"Bash(COBALT_ENV=production uv run cobalt validate*)"` | `"Bash(COBALT_ENV=production uv run cobalt validate)"` | row 8 (gemini + opus, HOLDS) |
| 5+6 rule-string list | 9 | `- 32 are byte for byte in `2026-09-22/05-stacked-deploy.md`'s line as it RAN (43 strings after the desk dropped `wc *`).` | The same sentence, followed by ` — except TWO, NARROWED by `08`'s folds 5–6: …validate* → …validate and …jobs * → …jobs restarts *. Each matches a subset of the commands the carried string matched, so both stay inside his R11 approval; no string was widened or added.` | — |

Fold 1 verification (P6, line 148). The desk's text reads correctly: round 2 if it ran, otherwise round 1. Its three branches are (a) YES from at least 3 houses with HOLD 0, (b) the R26 case, and (c) the METER/HARNESS floor. Branch (b) matches R26's condition word for word: HOLD 0, grok and opus YES, gemini NO, and the R__L row quotes R26 and the stop line. A HOLD above 0 still stops, which is consistent with R26 ("a round-2 HOLD > 0 is NOT covered"). The branches do not contradict each other, and P6 is consistent with P9 (line 153): `blockers: 1` must be named as folded on R__L. R26 is committed: `git log -1 -S"| R26 |" -- cto-2026-09-23.md` = `e16ca16f49717334a212aa646e8715ecd0a14a2d`. There is one scope gap, recorded under ESCALATE 2 and not edited.

## Narrowing proof
Every command `07` runs with `validate` or `jobs` (`grep -n -F "cobalt validate"` gives lines 6, 176, 220, 278, 298; `grep -n -F "cobalt jobs"` gives lines 6, 26, 72, 222, 298):

| line | command in `07` | narrowed string | matches? |
|---|---|---|---|
| 176 (P14) | `COBALT_ENV=production uv run cobalt validate` | `…cobalt validate` (exact) | YES, exact |
| 220 (2.3 d2) | `COBALT_ENV=production uv run cobalt validate` | same | YES, exact |
| 278 (4.5) | `COBALT_ENV=production uv run cobalt validate` | same | YES, exact |
| 298 (4.7 f) | `COBALT_ENV=production uv run cobalt validate` ("as 4.5") | same | YES, exact |
| 222 (2.5) | `COBALT_ENV=production uv run cobalt jobs restarts <main-at-gate>..<stack>` | `…cobalt jobs restarts *` | YES, prefix + one argument |
| 298 (4.7 f) | `COBALT_ENV=production uv run cobalt jobs restarts <pre-merge>..<stack-final>` | same | YES |
| 26, 72 | prose only (`cobalt jobs restarts` named, not run) | — | n/a |
| 1, 238 | `jobs register`: FORBIDDEN, never run | now also outside the allowlist | n/a |

Every `validate` call is bare, and every `jobs` call is `jobs restarts <range>`, so both strings were narrowed. After the edit: `grep -c -F 'cobalt validate*)'` = 0, `grep -c -F 'cobalt jobs *)'` = 0, and each narrowed string appears exactly once. Subset: `validate` matches only the bare command, which `validate*` also matched. `jobs restarts *` matches only commands that `jobs *` also matched. So nothing outside his R11 list, which covers the 05-carried strings as written, becomes runnable.

## ESCALATE
1. `ASK DESK: R11's condition reads "`08` changes no string; a change → back to him". Folds 5–6 change two strings, although only by narrowing them. I followed this prompt's ruling that a narrowing is a subset of R11. Does he still need to see a narrowing under that condition's wording? Safe default: narrowed. A subset cannot let the hub run anything R11 did not already approve. [08:15 ET]`
2. `ASK DESK: P6's R26 branch (line 148) does not require the `round: 2` field, but R26 covers only the round-2 case. The round-2 report `s2-smoke-fix-check-r2-2026-09-23.md` is ABSENT (`tail`: No such file, 08:1x). Round 1's actual line has exactly the R26 shape: grok YES, gemini NO, opus YES, HOLD 0. So if R__L quoted round 1, P6 would accept it outside R26's scope. I left it unchanged because P6 does not contradict itself. Safe default: R__L quotes only a `round: 2` line for branch (b), or the desk adds `round: 2` to that branch. [08:15 ET]`
3. Fold 3 differs from the proposed wording. The proposal keyed on "an already-written `FAILED: STEP-5` stop". However, STEP-5's stop line (lines 317 and 371) is `FAILED: <step> — <reason> · rollback: used — …`, where `<step>` is the failing step (4.4, 4.7, …), not the literal `STEP-5`. A literal check would miss almost every completed STEP-5. `rollback: used` appears on every STEP-5 ending and on no other ending, so it is the key used.
4. Line 8 still points to `reports/stacked-deploy-draft-2026-09-23.md` `## RULE PROOF`, which lists the two strings in their WIDE form. That report is not this seat's file and was not edited. Line 9 of `07` now records the two narrowings.
5. R26 is used by P6 (via R__L) but has no check of its own in `## AUTHORIZATION`. R5, R4 and R119 each get a `grep` and `git log -S`. I proved it committed here (`e16ca16`), but the hub will not re-prove it at run time. Reading only; not folded (not one of `08`'s folds).

Reading, not an escalation: fold 2 moves `<t up>` a few seconds later, so 4.7(b)'s "radar cycle line stamped AFTER `<t up>`" may need one more of its three permitted tails.

DEPLOY PROMPT FOLDED · folds applied: 5 · strings narrowed: 2 · strings widened or added: 0 · ESCALATE: 5
