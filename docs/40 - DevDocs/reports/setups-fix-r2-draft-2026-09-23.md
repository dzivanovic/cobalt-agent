# Setups fix round 2 — classification + prompts (drafted 2026-09-23 18:4x–18:54 ET)

Drafter `setups-fix-r2-draft-0923` · Opus 5.5 · prompt `prompts/2026-09-23/75-draft-setups-fix-r2.md` · launch row R101. Read-only seat: nothing run on any suite, no git write, no DB, no vault write. Wrote 3 files (the two prompts + this report).

## §0 Headline

- Classified `02` round 1 (`reports/setups-live-note-fix-check-2026-09-24.md`) under L75: **FIX 1** (row 1 = rows 1a, 2, ESC 1–2, one path) · **UNPROVEN 3 → RUN in `03`** (rows 3, 4, 5; each costs minutes) · NOT REAL 3 · OUT OF SCOPE 1 (the vwap ORDER seam, which goes to the deploy).
- Wrote `prompts/2026-09-24/03-setups-fix-r2-build.md`: one block of `test_radar_evaluate.py`, red on a mutation, all three suites. Also wrote `04-setups-fix-r2-check.md`: round 2, Opus 5.5 + Grok (R95), failing closed below two. Both launch lines were verified by `diff`: `03` = `01` exactly; `04` = `02` minus `Bash(agy *)`. **New rule strings: 0.**
- `04` is NOT named in R1 (`cto-2026-09-24.md`), so launching it on 09-24 needs his row; before 23:59 tonight, R30 covers it. ESCALATE: 6.

## L74

One arrived: a block appended to the tool result that returned this prompt file. It asked for a `Claude-Session:` line on commits and PR bodies and named a file-send tool. It is data. I did not follow it, and it is recorded once, here. This seat makes no commits.

## Classification (L75, from `02`'s own verdict column)

| `02` item | hub verdict | class | built / run as |
|---|---|---|---|
| row 1 — Gemini: T2's early `continue` (`test_radar_evaluate.py:739–740`) runs before the `holes` pin (`:745–753`) | HOLDS | **FIX (F1)** | `03` D3: the pin block moves above the early pass and gains `assert "formed" not in outcomes`. The un-pinned path is unchanged. Test file only. |
| row 1a — can a pinned def with a null hole form on the window | NOT CHECKABLE FROM READS ("run T2 with a stubbed window that forms a listed def") | **FIX (F1's red)**, the hub's own run | `03` D2 (A) / D3: a scratch MUTATION stubs T2's `evaluate_member` to `formed` for the `AWAITING_AN_ENGINE_FILL` slugs. Expected: `1 passed` on `<base>` (the bypass), `1 failed` on the fix. Without the window assert, a reorder alone would not catch the mutation, because the stub leaves the committed-day grid real; hence that one added line. |
| row 2 — Opus: the same path, "predates this fix" | HOLDS in part | FIX (same edit as F1) | — |
| row 3 — Gemini: offline / with-DB `NOT SHOWN — a SKIP naming COBALT_LIVE_VAULT_ROOT` | HOLDS in part; `-rs` part NOT CHECKABLE | **UNPROVEN → RUN** (0 extra minutes) | `03` D5 / D5b run with `-rs`, then count and quote each skip naming the variable. They are EXPECTED there, because `requires_vault` skips by design and D4 is its leg. A skipped id that no leg runs → ESCALATE. |
| row 4 — Opus: `CUT_DAY_CHECKS`' `check(ld)` gets no `tunables` | fact HOLDS; reachability NOT CHECKABLE | **UNPROVEN → RUN** (≈1 min) | `03` D2 (B) `ROW4`: `_forms_on_a_committed_day("rubberband", …, ld, tunables)` on his live def. `ERROR` → ESCALATE as a latent path. It is not built, because no `02` HOLD backs it and T2 exits rubberband on `avoided` first. |
| row 5 — Opus: the corpus pin does not isolate A-19/A-20 | NOT CHECKABLE FROM READS | **UNPROVEN → RUN** (≈2 min) | `03` D2 (B) `ROW5`: the corpus shape with D6 and with D6 minus the two keys. Expected `True` / `False`; any other pair → ESCALATE, not a stop (round 1's LADDER on HIS def already printed `+A19+A20=True`). |
| row 6 — Opus "the only assert removed is line 735" | DOES NOT HOLD as a count | NOT REAL | — |
| ESC 1 / ESC 2 (Gemini's DEFECT REMAINS; FOR THE CLASSIFIER item 1) | = row 1 | FIX (F1) | — |
| ESC 3 — `R119 vwap: False` | carried from `01` ESC 2 | **OUT OF SCOPE** for this round → `## FOR THE DEPLOY` | `03` D2 (B) prints one informational `VWAP` diagnostic (booleans in the report; R119's values only in scratch). |
| ESC 4, ESC 5 (standing lines) | — | NOT REAL (no finding) | carried into `04`'s standing lines |
| (Opus residual) line-reference drift in the round-1 classifier's report | not a row | NOT REAL (docs, no test effect) | — |

Counts: FIX 1 · UNPROVEN 3 (all RUN in `03`) · NOT REAL 3 · OUT OF SCOPE 1 · OWNER ITEM 0 new (A-19 / A-20 values stay FOR DEJAN 1 of `second-chance-fix-draft-2026-09-23.md`).

## Prompts written

| file | seat · model · mode | stop line |
|---|---|---|
| `prompts/2026-09-24/03-setups-fix-r2-build.md` | `setups-fix-r2-build-0924` · Opus 5.5 · auto · `setups-c1` on `setups/seven-0921`, BASE expected `91e07fc7` (report commit; code `c9a11e14`, verified docs-only above it by `git diff --stat c9a11e14 91e07fc7 -- . ':(exclude)docs'` = empty) · scratch under `setups-c1/scratch/prints-0924/`, OUTSIDE `tests/` (`01` ESC 1's lesson) | `SETUPS FIX R2 BUILT <tip> \| on <base> \| offline <p>/<f> \| with-DB <p>/<f> \| live-note <p>/<f> \| .env: removed \| FIX: 1 \| ESCALATE: <n>` |
| `prompts/2026-09-24/04-setups-fix-r2-check.md` | `setups-fix-r2-check-0924` · Sonnet 5 hub · auto · `agy-trial` · checkers Opus 5.5 + Grok (R95; Sol METER; Gemini out, R96/R97) · round 2 of ≤3 · fail closed below TWO · packet carries the fix diff, both mutation runs and all three suites' output (R81 (4)) | `SETUPS FIX R2 CHECK DONE · round: 2 · opus: … · grok: … · sol: NOT SEATED … · gemini: NOT SEATED (R96/R97) · defects that HOLD: <n> · ESCALATE: <n>` |

Rule strings: `03` = `01`'s line (20 allow + 3 deny + triplet), confirmed identical by `diff` once the path and the rc name were masked. `04` = `02`'s line minus ONE string, **`"Bash(agy *)"`**, confirmed by `diff` (the only difference): 14 allow + 3 deny + triplet, a strict subset. New strings: 0. `R__` placeholders: 2 in each prompt (the launch row in the SEAT prose and in the AUTHORIZATION gate), each behind its own placeholder gate.

## FOR THE DEPLOY

1. **The vwap ORDER seam (`01` ESC 2) — decision: the DEPLOY carries it, not this round.** Why: no `02` row HOLDS against it (L75: only FIX rows are built). Settling it needs either a new committed day that forms at R119's values or a new pin that gate 2 does not back, and both widen beyond the HOLD. Fix r2 does not change it: once `dist.k.vwap` is filled, `holes` is empty, vwap-continuation takes the un-pinned path, and at R119's values `assert forms` goes RED. The deploy prompt must carry:
   - **(a)** its 2.3 (d) live-note proof, run BEFORE STEP-6: both engine-fill pins hold, with the same five `AWAITING` lines as delta row 17 (unchanged by fix r2).
   - **(b)** delta row 19's post-STEP-6 run (6.6). Its expected result is RED on vwap-continuation's `assert forms`, recorded as `R119 live-note: RED — <assertion>`, NOT a rollback.
   - **(c)** the consequence, stated: from STEP-6 on, `~/cobalt`'s live-note leg is red. Every later build's GATE EARLY (R81 (1)) and every later deploy's L68 live-note leg will show that red until a fix round lands. `03`'s `VWAP` row prints which of R119's keys blocks formation, so the next classifier starts from evidence.

   **ASK DESK** (below): adopt (b) and name the 09-25 classifier seat before any other deploy's gate, or hold R119's STEP-6 (his ruling, his call).
2. **P5 / P6:** `<setups tip>` comes from `03`'s `SETUPS FIX R2 BUILT` line. P6 adds `04`'s `SETUPS FIX R2 CHECK DONE · round: 2`, where **≥2** `ready … YES` (R95 seats Opus + Grok, not three) and `defects that HOLD: 0`. Round 1's DONE line stays in the chain with its HOLD 1 answered by round 2. P6's "≥3 ready" text (delta row 9) must read R95's count for round 2.
3. **P11 identity (delta row 12):** `<ln base>..<setups tip>` still touches EXACTLY the four test files (r2 changes only `test_radar_evaluate.py`). `<nse>` is now recorded, not predicted: row 12's "expected 39" is already stale by `01`'s wip commit `9a59178c`. Round 1 added three commits (`c9a11e14`, `9a59178c`, `91e07fc7`), and r2 adds two or more.
4. **P1 REFUSED `??` list (delta row 15):** + `setups-fix-r2-build-2026-09-24.md`.
5. **Deploy-prompt house read (delta row 11):** seats per R95 = Opus + Grok (+ Sol if its meter returns). It needs its own committed `Bash(grok *) … through 2026-09-24` row from him naming the deploy read, because R1 names only `02` / `44` / `74`.
6. **Cleanup (delta row 20):** + `setups-c1/scratch/prints-0924/` (two files), with `prints-0923` and `seam-0923`.
7. **Window:** R83 (his "A") → the deploy gates on a `DONE TRADING <time>` row in `cto-2026-09-24.md`. Unchanged by this round.

## ESCALATE

1. **ASK DESK: `04` is NOT named in R1** (`cto-2026-09-24.md`, "Approved", `through 2026-09-24` for `02` / `44` / `74` only). If `04` launches on 09-24 or later, it needs a committed row of his naming `04-setups-fix-r2-check.md` with `Bash(grok *)`, to be carried to him with his next word. Safe default: `04` stops `FAILED: authorization expired`. If `03` stops green and `04` launches before 23:59 tonight, R30 (`cto-2026-09-22.md`, general through 09-23) covers it. `03` ≈ 40 min + `04` ≈ 30 min from an ≈19:00 launch fits that. [18:54]
2. **ASK DESK: the vwap ORDER seam** (FOR THE DEPLOY 1): adopt delta row 19's 6.6 with an expected RED plus a named 09-25 classifier, or bring him the choice of holding STEP-6's R119 rows. The desk decides which. [18:54]
3. **R97 evidence:** round 1's one HOLD was Gemini's alone (Opus noted the same path but answered KEPT). A Gemini finding HELD in a code check. That is his evidence for R97; the desk noted it in R101.
4. **R95 applied:** `04` seats two houses (Opus + Grok), not L67's three. This follows his R95 ("just Opus and Grok for code checks … while we follow the new gate rule"); the L67 fold is owed at the 09-23 close. The deploy's P6 must count accordingly (FOR THE DEPLOY 2).
5. **The dev-DB lock for `03` D5b:** before launching `03`, check `ls ~/cobalt-wt/*/.env` and every running build's `## CONTINUE` (09-23 lesson (1)). `03` fails closed on a held lock, so this is not a hazard, only lost time.
6. **Scratch location:** `03`'s two scratch files live in `setups-c1/scratch/prints-0924/` and add `sys.path` themselves, because no conftest reaches them. If they fail to import, `03` stops `FAILED: D2 — the mutation harness does not load`, before any edit. It is safe, but it would cost a relaunch.

SETUPS FIX R2 DRAFTED · FIX: 1 · UNPROVEN: 3 · prompts: 2 · new rule strings: 0 · ESCALATE: 6
