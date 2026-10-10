# Model-by-complexity rule, round 2: the Grok SHADOW trial · proposal for the model tribunal · 2026-10-10

Proposer: Opus 5.5 drafter `complexity-propose-r2` (prompt `prompts/2026-10-10/265-propose-complexity-shadow.md`). L67: one house proposes and the tribunal rules.
Builds on: `reports/complexity-routing-proposal-2026-10-10.md` (round 1). Its §1 data, §2 score, §5.1 shadow log and Q1–Q8 hold unchanged unless this file says otherwise.
Frame (HIS RULING, R919, `cto-2026-10-10.md:12`; words at `brain-direction-2026-10-02.md:186-198`; LAWS L67 `[stated 2026-10-10 · Dejan, R919 via brain L79]`, `LAWS.md:347`):
- His hypothesis: `grok-4.7` builds at Opus 5.5's level or slightly below it, and above Sonnet and Haiku.
- Where a non-Anthropic model builds, Grok is preferred over Sol.
- Astra is RESERVED for tribunals and multi-house reviews.
- Every merged build stays Opus 5.5 until his word on this tribunal's result. Only that word amends L29.
This file tests the hypothesis. It does not argue for or against it.

## §0 Headline
- Round 1's classes stand. Two corrections: (a) three of the 27 checked jobs have card fields that place them LOW, MID and HIGH; (b) Grok has been house B on these checks, so it has its own record as a checker.
- SHADOW TRIAL: Grok 4.7 rebuilds three already-checked cards from their own BASE: `strike-fallback-env` (LOW), `radar-display-fix` (MID) and `s4-p1` (HIGH). Each rebuild goes on a `shadow/` branch that is never merged. Each is judged by the existing CHECK-HUB flow and compared with its Opus original.
- Grok cannot run commands (L67), so a fresh Opus 5.5 GATE SEAT runs Grok's CLI and the three suites. That seat writes no code.
- STOP (R411): the gate seat is a write-path launch, so it needs `dontAsk` mode. `desk-launch.sh prompt` runs only `auto` or `plan` (`desk-launch.sh:454-457`). The seat therefore needs a new fixed file plus a new launcher kind. That is a new command, so this proposal stops there with `decisions: 1`. Everything else uses existing strings.
- n=3 is insufficient data (L8). The trial gives an indication for his word. It cannot prove a tier.

## 1. Complexity classes (round 1 §2, corrected)
The score is unchanged and is read from the card at launch:
- Formula: `R + M + S + X + H + $`. R = 1 per card row over 3. M = migration +3. S = +1 per service restarted. X = +2 per seam. H = new horizon +4. $ = money, sizing or his vault notes +3. W = write path, a gate and not a weight.
- Bands (modelled): LOW 0–2 · MID 3–6 · HIGH ≥7.

Corrections from this round's reads:
1. The 26-build sample does span the three bands, so the bands can be tested once a second model builds:
   - `strike-fallback-env`: 2 rows, RESTARTS aset+radar. R0 + S2 = **2, LOW**.
   - `radar-display-fix`: 6 rows, one `src/` file, RESTARTS aset+radar. R3 + S2 = **5, MID**.
   - `s4-p1`: 8 rows, RESTARTS aset+radar, ONE SEAM (`card_transitions` through `CardStore.transition()`, card `72-s4-p1-card.md:14`), new detector. R5 + S2 + X2 + H4 = **13, HIGH**.
   - Build reports quoted in the check reports: `strike-fallback-env-check-2026-10-10.md:41`, `radar-display-fix-check-2026-10-08.md:42`, `s4-p1-check-2026-10-09.md:45`.
2. Held findings do not track the band in these three: LOW 1, MID 3, HIGH 4. In round 1's full sample, 1–2-row cards held 11 (`guard-g2`, `radar-ladder-refresh`). Round 1's warning stands: the band predicts cost (tokens rise with rows: 165k / 180k / 416k) better than it predicts defects.
3. Grok as a checker, house B on all three originals:
   - `strike-fallback-env`: FINDINGS 0 (`strike-fallback-env-check-2026-10-10.md:129`).
   - `radar-display-fix`: FINDINGS 0 (`radar-display-fix-check-2026-10-08.md:246`).
   - `s4-p1`: 4 findings, 0 held. Three were REJECTED and B2 was UNSETTLED (`s4-p1-check-2026-10-09.md:163-165`).
   - Elsewhere, Grok held 2 of 2 on `stop-guard-g7` (`stop-guard-g7-check-2026-10-09.md:166-167`).
   - This is Grok's record as a reviewer. It is not evidence about Grok as a builder.
4. The Opus check session's OWN held findings are the only source that sat on every original:
   - `strike-fallback-env`: 1 (O1, `strike-fallback-env-check-2026-10-10.md:137`).
   - `radar-display-fix`: 2 (O1, O2, `radar-display-fix-check-2026-10-08.md:158-159`).
   - `s4-p1`: 2 distinct defects (O1, O3, `s4-p1-check-2026-10-09.md:155,157`; Sol's A3 and A2 are the same two defects).
   - The trial uses this as its primary comparable figure (§2.3).

## 2. The SHADOW trial

### 2.1 The three cards (each checked, each built by Opus 5.5)

**strike-fallback-env · LOW (2)**
- Card: `prompts/2026-10-09/215-strike-fallback-env-card.md`, BASE `8f4bbe28` (`:5`).
- Proof it was checked: CARD COMMITTED `bc051c44` (`strike-fallback-env-check-2026-10-10.md:16`). Stop line `CHECK DONE … held: 1 … ready: YES` (`:223`).
- Opus build tokens: 165,478 (`:41`). Check tokens: 138,173 (`:223`).
- Held: 1, O1 (`step()` raises on an unprintable exception, `:137`).

**radar-display-fix · MID (5)**
- Card: `prompts/2026-10-08/118-radar-display-fix-card.md`, BASE `50b0cd87` (`:5`).
- Proof it was checked: CARD COMMITTED `0deb06fc` (`radar-display-fix-check-2026-10-08.md:16`). Stop line `held: 3 … ready: YES` (`:246`).
- Opus build tokens: 179,901 (`:42`). Check tokens: 176,294 (`:246`).
- Held: 3, O1, O2 and A3 (`:158-159,163`).

**s4-p1 · HIGH (13)**
- Card: `prompts/2026-10-06/72-s4-p1-card.md`, BASE `e4586978` (`:5`).
- Proof it was checked: CARD COMMITTED `d35d6841` (`s4-p1-check-2026-10-09.md:18`). Stop line `held: 4 … open: 7 … ready: YES` (`:279`).
- Opus build tokens: 415,769 (`:45`). Check tokens: 259,254 (`:279`).
- Held: 4 findings, 2 distinct defects: O1=A3 and O3=A2 (`:155-158`).

Why these three:
- Each is in a different band.
- All three were checked in the next flow (house A and house B at once).
- None of the three has a migration. A shadow migration would move `cobalt_dev` off `0013` for a branch that never lands. `s4-p2` (migration 0024) and `price-floor` (0023) are excluded for that reason.
- None of the three is a MANDATORY-HOUSE-B card (all three are `HOUSE B: as needed`, `:9` of each card).
- `s4-p1` writes `card_transitions` through the existing store. That is a DB write path under L29. It runs only in tests under the L76 lock, on a branch that is never merged.

### 2.2 How one shadow build runs
1. **Shadow card.** The desk commits a copy of the original card:
   - The ROWS stay byte for byte.
   - Changed header fields: `JOB: <job>-grok`, `BRANCH: shadow/<job>-grok`, `WORKTREE: <job>-grok`, the same `BASE`, and `RULINGS: 2026-10-10 R919`.
   - No `TIP` or `CHECK REPORT` of the original.
   - New header line: `SHADOW OF: <original card path>`.
2. **Worktree.** `git -C /Users/cobalt/cobalt worktree add -b shadow/<job>-grok /Users/cobalt/cobalt-wt/<job>-grok <BASE>`. This is BUILD-HUB LAUNCH (0) as it stands (`BUILD-HUB.md:9`), run by the launcher.
3. **Gate seat, start.** The gate seat (§3) writes `<WT>/SHADOW-INSTRUCTIONS.md` and never commits it. It holds the shadow card's ROWS verbatim, BUILD-HUB `## E2` and `## E3` verbatim, and the fence: `src/` and `tests/` only, the rows' files only. Grok's sandbox reads only its workspace, so the card is copied in. CHECK-HUB copies files for its houses the same way (`CHECK-HUB.md:91`).
4. **Grok pass T (tests only).** The gate seat runs the Grok builder line (§2.6). Grok writes the rows' tests under `tests/`. The gate seat then:
   - runs `git diff --stat` and quotes it;
   - commits with `git add tests/…` and `git commit -m "wip(<job>-grok): red"`;
   - runs the new tests to show them red.
   - If a test is green before the fix, that is recorded. The gate does not repair it.
5. **Grok pass S (the rows).** The same line, now asking for the `src/` rows. The gate seat quotes `git diff --stat` and commits `feat(<job>-grok): rows`. A path outside the rows' files is recorded as `SCOPE` and is not reverted.
6. **Gate.** BUILD-HUB `## RESTARTS` and `## W` as they stand: offline, with-DB under THE LOCK, and live-note.
   - If a suite is red, the gate seat sends Grok ONE re-pass (pass S2) with the failing lines quoted verbatim, then reruns the suites.
   - The cap is 2 re-passes. After that the build stops `SHADOW BUILT … suites: red`, and the build is scored, not repaired.
7. **Build report.** The gate seat writes `<WT>/docs/40 - DevDocs/reports/<job>-grok-build-<date>.md` in BUILD-HUB's REPORT shape. Its stop line is BUILD-HUB's BUILT line with these extra fields: `builder: grok-4.7 · gate: <seat> · grok passes: <n> · suites at first run: <green|red>`.
8. **Check.** `desk-launch.sh check <shadow card>`: the existing CHECK-HUB, unchanged (fresh Opus plus house A by R921). Grok sits as house A on its own build. Its findings are run like any other and tallied apart (§2.3, T3). The check fixes what holds, as CHECK-HUB says. Those fixes are Opus's and are never counted for Grok.
9. **Never merged.**
   - No deploy card ever names a `shadow/` branch.
   - The worktree stays until the tribunal's result is recorded, then it goes by the desk's usual worktree salvage.
   - The original check's report and fix commits are on `main`. The shadow check prompt (CHECK-HUB) reads the shadow card, which does not name them.

### 2.3 Metric (per card, recorded beside the Opus original)

| metric | how measured | Opus original (LOW / MID / HIGH) |
|---|---|---|
| held findings, all sources | the shadow CHECK DONE line `held:` | 1 / 3 / 4 |
| held, Opus check's own (primary) | `O<n>` rows with verdict HELD | 1 / 2 / 2 |
| held, Grok-sourced (on its own build) | house-A rows HELD; tallied apart and not counted | n/a |
| distinct defects | held rows merged where the check says "same defect as" | 1 / 3 / 2 |
| fix rounds | `ready: NO` → the card's FIX ROUND count to `ready: YES` | 0 / 0 / 0 |
| suites at first green | `suites at first run` plus `grok passes` on the BUILT line | green at build / green / green (all three originals BUILT on the first gate) |
| scope breaks | a path outside the rows' files (CHECK-HUB `## 7` (ii)) | 0 / 0 / 0 (A2, A5 and B4 rejected as docs/precedent) |
| tokens | Opus: gate seat plus check `tokens:`. Grok: UNKNOWN (§2.5) | build 165,478 / 179,901 / 415,769 · check 138,173 / 176,294 / 259,254 |

Known-answer side run (T5): after the shadow check, the gate seat's report lists the original check's red tests:
- `strike-fallback-env`: `245f3fd6`.
- `s4-p1`: `720cc29f`.
- `radar-display-fix`: its red commit, read at launch.
For each test it says whether that test applies to Grok's tree: same function name, or not applicable. It is recorded only and does not count toward the bar.

### 2.4 Pass bar (proposed; each card, then the set)
- **AT LEVEL** on a card, when all of these hold:
  - `ready: YES` with no fix round;
  - Opus-own held ≤ the original's + 1;
  - distinct defects ≤ the original's + 1;
  - suites green at first run, or after 1 Grok re-pass;
  - 0 scope breaks.
- **CLOSE BELOW** on a card: `ready: YES` after at most 1 fix round, distinct defects ≤ the original's + 3, and at most 2 Grok re-passes.
- **BELOW** on a card: anything else, or a build that stops with `suites: red`.
- SET result: AT LEVEL when all three cards are AT LEVEL. CLOSE BELOW when none is BELOW. Otherwise BELOW.
- The tribunal reads the set result against his hypothesis. Only his word turns it into a seat rule (R919).
- The trial cannot show "above Sonnet and Haiku", because neither is in the trial. That half of the hypothesis stays untested (Q5).

### 2.5 Cost
- **Anthropic meter.**
  - Shadow checks: about 575k by analogy with the three original checks (138k + 176k + 259k).
  - Gate seats: about 300–450k MODELLED (three seats). Each one reads BUILD-HUB and the card, runs the suites, and authors no code. No measured row exists for such a seat.
  - Total: about 0.9–1.0 M tokens. That compares with 1.33 M for the originals' builds plus checks.
- **Grok meter.** 3 cards × at least 2 passes (T and S), plus up to 2 re-passes each, so 6–12 calls.
  - Tokens: UNKNOWN (L70). Grok's session `summary.json` records `num_messages`, `created_at` and `updated_at`, but no token field (read of `~/.grok/sessions/…agy-trial/01a126f9…/summary.json`).
  - The gate seat records messages and wall time per pass instead.
  - Grok's own check seat: 3 more calls.
- **Dollars:** $0 (L27; minimum tiers, no top-up).
- **OpenAI:** none. Sol does not sit (R920). Astra's meter is kept for this tribunal.

### 2.6 Grok builder launch line (run by the gate seat; only existing strings)
- `Bash(grok *)` is a STANDING house string (`LAWS.md:321`).
- The flags are CHECK-HUB's Grok seat (`CHECK-HUB.md:91`): `-m grok-4.7` (his 10-03 R3), `--sandbox cobalt-job` (`ops/grok-sandbox.toml`: the workspace profile; `.env`, `~/.cobalt` and the agent homes are denied) and one `--allow "Write(…)"` glob.
- `--always-approve` is never passed, so Grok runs no shell command. That keeps L67's "a house cannot run a command".
- cwd: `/Users/cobalt/cobalt-wt/<job>-grok`. The line:

`grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/<job>-grok/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass <T|S|S2>: <tests only under tests/ | the src/ rows | fix the failing lines quoted under PASS S2>. Write only the rows' files. Run no command. Reply with the list of files you wrote."`

## 3. THE GATE SEAT
- **Seat:** a fresh Opus 5.5 session, `<job>-grok-gate`, launched by the desk.
  - It is never the builder, which is Grok.
  - It is never the shadow check session, which is a separate fresh Opus under CHECK-HUB.
  - L29: a session on a DB write path (the with-DB suite) runs on Opus or higher and never in auto mode.
- **Its line:** BUILD-HUB's 26 allow strings and 4 deny strings unchanged (`BUILD-HUB.md:12-14`), in `--permission-mode dontAsk`, plus the standing `Bash(grok *)`.
  - The fixed file tells it to Edit only `SHADOW-INSTRUCTIONS.md` and its report, never `src/` or `tests/`.
  - Its report quotes `git diff --stat` before each commit, so the check can match every commit to a Grok pass.
- **How its result is recorded:**
  1. The BUILT stop line in its build report (§2.2 step 7) is the record. CHECK-HUB reads it like any build report.
  2. The desk adds one row per card to a new table `reports/complexity-shadow-results-2026-10-<dd>.md`: §2.3's columns with the shadow value beside the original.
  3. The model tribunal's hub reads that table.
- **R411 STOP:** this seat needs `dontAsk` on a write path, so it must be a FIXED file launched by a launcher kind (L29; `desk-launch.sh:445-457` refuses every mode but `auto` and `plan` on a prompt). Neither exists:
  - `SHADOW-HUB.md` (the gate seat's procedure);
  - `desk-launch.sh shadow <card>`: BUILD-HUB's LAUNCH (0)–(2) with SHADOW-HUB and the line above.
  - That is a new command. The shadow trial cannot launch until a card builds it and he approves its line (the BUILD-HUB pattern: one approval of the list).
  - Precedent for "a fixed file plus a launcher kind, not a prompt": `ops-hand-draft-2026-10-10.md:17`.
  - Until that card exists, the tribunal can still rule on §1, §2.1–§2.5 and §4.

## 4. Questions for the model tribunal (each with a default)
SEATS: Astra (OpenAI; his reserved meter is spent here, R919/R920; one OpenAI seat at a time, F4 holds it first, `LAWS.md:346`), Gemini, and the blind Anthropic seat (Opus 5.5, `LAWS.md:344` desk reading). Grok also sits. Its ruling on any item about Grok's own tier (S1, S5, S6, S9) is RECORDED APART and not counted (R919 "self-interest", `LAWS.md:349`).
No item below is an owner item. A tier assignment is not his money, data or law. The L29 amendment is his word on the result, as R919 already says, so it is not a question here (`LAWS.md:345`).

- **S1. Are three cards (LOW, MID, HIGH) enough to read his hypothesis, given L8's n≥30?** Default: YES, as an indication only. The result is reported as "insufficient data (n=3)", and his word decides. *(Grok: recorded apart.)*
- **S2. Card choice: `strike-fallback-env`, `radar-display-fix`, `s4-p1`, no migration cards.** Default: keep. A migration card would move `cobalt_dev` for a branch that never lands.
- **S3. Grok sits as house A on the check of its own build (R921 seat order, CHECK-HUB unchanged).** Default: YES. Its findings are run by Opus like any other, and held ones are tallied apart and not counted toward the bar. No hub change is needed.
- **S4. Primary figure = the Opus check session's OWN held findings, because it is the only source on every original and every shadow.** Default: YES. All-source held and distinct defects are reported beside it.
- **S5. Pass bar AT LEVEL / CLOSE BELOW / BELOW (§2.4).** Default: keep as written. *(Grok: recorded apart.)*
- **S6. Grok re-pass cap: 2 per card, and the gate seat never repairs code.** Default: keep. A third red stops the build and scores it BELOW. *(Grok: recorded apart.)*
- **S7. Two Grok passes (tests, then rows) to keep BUILD-HUB's RED FIRST.** Default: YES.
- **S8. Grok's reasoning effort.** CLI headless runs show `"reasoning_effort": "medium"` (`summary.json` above). Default: leave the CLI default and record it. A pinned effort would be a new flag on the line (R411).
- **S9. "Above Sonnet and Haiku" is untested by this trial.** Default: leave it untested. His R919 states it, and a Sonnet arm on a write path is barred (L29). *(Grok: recorded apart.)*
- **S10. Round 1's Q1–Q8 (shadow log, inputs, bands, non-write Sonnet trial, HIGH → Fable, JEV, retire rule).** Default: carried as round 1's defaults. This tribunal rules them in the same sitting.
- **S11. Order: the shadow trial launches only after the `SHADOW-HUB` card is built, checked and approved (§3).** Default: YES. The tribunal rules the design now and reads the results in a second sitting, within L67's three rounds.
