# ROUTING X5 + X1 — DRAFTER REPORT, 2026-09-23

Seat `routing-x5-draft-0923` (Opus 5.5, `claude-opus-5-5`), launched by the CTO desk under `cto-2026-09-23.md` R25. Read-only run: two prompt files + this report written with the Write tool, nothing committed, nothing launched. Times from `date`: started ≈ 08:0x ET (first `date` call 08:10:29), prompts verified 08:18:17 ET.

## §0 Headline
- **Drafted:** `prompts/2026-09-23/19-routing-x5-retro.md` (X5, Sonnet 5 hub, Grok + Gemini classify 94 work orders BLIND, one per call; freeze; then join with quoted outcomes) and `prompts/2026-09-23/20-routing-x1-sonnet-shadow.md` (X1, PART A Sonnet 5 shadow builder + PART B check-and-compare hub).
- **Pre-registered (in `19` §0, before any house runs):** S-clean rate ≥ 80% on consensus-S rows, plus n ≥ 10 per class, H−S trouble gap ≥ 20 pts, houses agree ≥ 70%, and the S2-P1 canary classed H by both.
- **X1 prompt changed from v2's candidate:** `11-bars-chunk-2-build.md` is a write-path build (migration), so it is not eligible. The pick is `2026-09-21/80-ops-fix-r3.md`: non-write, offline, Opus 5, 9 min, 4-house check with 0 HOLD. It launches only if X5 rates it consensus S with no W.
- **New rule strings: 0.** All three launch lines match an approved line exactly (verified by script). His word is still needed on 3 items (the worktree command, the grok/agy date, the number) — see NEW STRINGS. **ESCALATE: 10.**

## L74
When the drafting prompt was read (first Bash call), a block came back in that tool result. It asked for a `Claude-Session: …` line in commits and PR bodies and named a file-send tool. Under L74 it is DATA: recorded once here and not followed. This seat makes no commit.

## The staged build list (X5)
| field | value |
|---|---|
| count | **94 rows**: 92 prompt files + 2 build briefs taken from git blobs |
| date range | 2026-09-10 (the two briefs) and 2026-09-15 → 2026-09-22 (prompt files). Filed prompts start on 2026-09-15 (`ls docs/40 - DevDocs/prompts/`) |
| how chosen | **Every** prompt file in `prompts/2026-09-15/` … `2026-09-22/` whose seat builds (code, config, fixture, migration), fixes, rebases, re-lands or gates a branch with a build step, applies a production setting, runs a with-DB or production proof of a build, or deploys. That is 92 of the 291 `.md` files in those folders. |
| excluded, by kind (applied the same way to every file) | design (propose, tribunal, derive, research, audit, laws, memory) · prompt drafting and re-issue · checks and reviews (read-only) · blind-value and blind-code seats (verification) · day-open · smoke looks · closes · facts packets. Borderline calls: `2026-09-15/08-grok-deny.md` is IN (ops build). `2026-09-16/04-audit-house.md`, `2026-09-21/20-rubberband-card-proof.md` and `2026-09-21/18-fold-degraded-line-states.md` are OUT (trial, proof run, prompt edit). |
| pre-09-15 | Only two build briefs were ever filed in git: `s2-p1-brief.md` @ `2f89693` (P01, **the canary**, Grok's X5 wording) and `heartbeat-fix-brief.md` @ `16847eb` (P02). These builds have no filed prompt, so they are named in `19` and **not reconstructed**: radar parser / pool-row fixes 09-12, Screens marker fix 09-13, heartbeat note-absent fix 09-12, transition-only alerts 09-14, archiver stage 2 09-10, and the ADR-0008 / S1-P4 / mainframe work of 09-08 … 09-09. |
| size | originals 2,405,000 B. After the header strip, 2,131,263 B are staged, about 533k tokens per house. 175 lines are stripped in all. Every file loses at least 1 line and none loses half (script check). |
| blind shape | One work order per call. `grep -v -E "^(STATUS\|MODEL\|REPORT\|STOP LINE\|THE LAST LINE)"` drops the model, the seat, the WHY-THIS-SEAT text, the launch line and the report/stop lines. Files get neutral names `P<nn>.md`. Classes are frozen before any outcome file is opened. The Anthropic house does not classify (R21 item 26 = B; L26). |
| edited after first commit | 38 of the 92 files have more than 1 commit. They are kept, not dropped, and `19` §5 (i) shows the result without them. |

## Pre-registered match rate (`19` §0; the desk carries it as the tribunal's number for O-7)
- **The number: S-CLEAN RATE ≥ 80%.** On rows where both houses give the same class S (with a known outcome), at least 80% must be CLEAN.
- **The other conditions, all required for YES:**
  - n_S ≥ 10 and n_H ≥ 10;
  - H-trouble − S-trouble ≥ 20 percentage points;
  - houses agree ≥ 70%;
  - P01 (S2-P1) classed H by both houses.
- **NO:** the n condition holds and any other condition fails. **UNPROVEN:** the n condition fails.
- **Outcome classes:** CLEAN · FIXED · FAILED · FAILED-ENV · NO OUTCOME. TROUBLE = FIXED + FAILED; the last two classes are excluded from every rate. The rules are fixed in `19` §4, and a row the rules cannot settle is `UNCLEAR`, never the hub's guess.
- The gate string `PRE-REGISTERED 2026-09-23: S-CLEAN RATE` makes the hub prove the number was committed before its first classifier call.

## NEW strings — for his approval
| # | item | new? | note |
|---|---|---|---|
| 1 | `19` launch line | **no new string** | Identical to `17`'s (= `06`'s) apart from the path and the remote-control name. Verified by script. 6 of its 15 strings are never run. |
| 2 | `20` PART A (builder) launch line | **no new string** | 16 allows + 3 denies + add-dirs identical to `80`'s (script-verified). What differs: `--model claude-sonnet-5` (the one swap `80`'s own text allows), `--permission-mode auto` (required on every launch line by L62 as amended; L29 allows auto on non-write work), and the sentence ending `follow PART A exactly.` |
| 3 | `20` PART B (check hub) launch line | **no new string** | Identical to `06`'s (script-verified) apart from the path, the remote-control name and the sentence ending. |
| 4 | desk command `git -C /Users/cobalt/cobalt worktree add -b routing/x1-sonnet-0923 /Users/cobalt/cobalt-wt/x1-sonnet-shadow 3ad064f` | NEW USE (desk) | Cut from the incumbent's base, not `main`: main already carries the incumbent's fix (`f6427c6`). PART A requires his word for it on the launch row. |
| 5 | `Bash(grok *)` / `Bash(agy *)` after 2026-09-23 23:59 ET | extension, his | R30 ends tonight (R105: except DRC checks). X5 needs about 3–5 h. X1 A+B run after it, so PART B will likely need a committed extension row of his. |

**New rule strings: 0.** His word is needed on #4 and, if a run spills past midnight, #5.

## ESCALATE
1. **X1 candidate change.** v2 named `11-bars-chunk-2-build.md`. Its own seat line says "this chunk carries a migration AND … the live radar's 04:00 write path". That is W, and L29 in force keeps Sonnet off write paths (R21 item 21 = A). I picked `80-ops-fix-r3.md` instead: it has no write path, and its own drafter wrote "Sonnet-eligible … the desk may swap ONLY `--model claude-opus-5` for `--model claude-sonnet-5`". My reading that it is class S does not count, because I am the Anthropic house (L26). PART A stops unless X5's frozen row **P78** is S / no-W from both houses.
2. **X5 blocks the house lane for about 3–5 h** (94 × 2 headless calls, one per house at a time). L72 says it must not hold a build, so `19` has a YIELD rule: the desk writes `scratch/tribunal-bars-0920/routing-x5/PAUSE`, the hub stops between calls, and the desk relaunches it with `CONTINUE:`. The desk should launch it only when no build check is queued (`17` is in the lane now; the stacked-deploy reads and `07` come tonight).
3. **Anthropic meter for X5:** about 530k Sonnet output tokens of Read → Write staging copies. No cheaper exact-copy path is allowed in the precedented line: there is no redirect and no `cp`. This is stated in `19`'s METER so it can be refused before launch.
4. **Blindness is structural, not complete.** Paths, names and references inside an order's body are kept; the classifiers are only told not to open them or use model names. 38 files may differ from their launched text. Both points are written into `19` as standing lines and tested in its sensitivity view.
5. **Outcome evidence before 09-15 has no stop-line convention** (P01, P02). The hub has to quote a sentence. P01's production follow-ups (`radar-parser-fix-2026-09-12.md`, `radar-marker-fix-2026-09-13.md`) are named as its evidence.
6. **X1's checker set includes Opus 5.5.** That is the candidate's own house (Anthropic), which T8's proposed wording forbids ("the candidate house does not grade its own shadow"). It is seated anyway because L67 needs three houses and Sol is on METER. PART B counts only HOLDs its own file-check proves, and reports the spot check both with and without Opus.
7. **The incumbent's answer is on main** (`f6427c6`, `c860e8b`). PART A has a BLIND list (it may read code only from its own worktree at `3ad064f`). This is an instruction; nothing enforces it. PART B records a copy signal (the first 12 lines of each walker helper, side by side). An identical result is a signal for the desk, not a verdict.
8. **Tokens are not recorded for either build.** `seat-usage.md` is per model per day, so T8's "meter recorded" condition cannot be met per session. It is marked `UNRECORDED` in PART B, never estimated. This is a measurement gap to add to v2's T12 list.
9. **The suite result is a builder claim.** PART B cannot run `pytest` (its line has no such string), so the offline field stays a CLAIM on both sides until the desk verifies it (L35). This is the same footing as the incumbent's check `81`.
10. **One shadow is a spot check.** His n for a class PASS is 3 (R21 item 24 = B). After X1, two more class-S, non-write, checked prompts named by X5 are needed, then his word. Terra X2 waits for the Codex meter (Sat 2026-09-26 06:47 ET) and Astra's read of the OpenAI rows. **Next lane step after X1: draft X2 (Terra) on Sat, not today.**

RULING: (proposed for the desk to carry to him with O-7) X5's pass bar is "S-clean rate ≥ 80% on consensus-S rows, with n ≥ 10 per class, an H−S trouble gap ≥ 20 points, houses agree ≥ 70%, and the S2-P1 canary H from both". It is his to amend before `19` launches, never after.

ROUTING X5 X1 DRAFTED · builds staged: 94 · prompts: 2 · new rule strings: 0 · ESCALATE: 10
