BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Sat Oct 10 16:55:52 EDT 2026

## DIGEST FOR THE DESK
TRIBUNAL R1: ADOPT AFTER fixing the gate, scoring and Grok-scope seams named in S2, S5, S11
- S1 ADOPT · STAKE
- S2 ADOPT WITH — run BUILD-HUB E0 on each BASE first; a base-red card is swapped for the next same-band no-migration card
- S3 ADOPT
- S4 ADOPT · STAKE
- S5 ADOPT WITH — bar on Opus-own held only; "distinct defects" leaves the bar (the original's includes Sol); tolerances labelled modelled · STAKE
- S6 ADOPT WITH — fixed quote rule for failing lines; the rows' own tests run before the full gate; re-pass cap unchanged · STAKE
- S7 ADOPT WITH — SHADOW-INSTRUCTIONS says every run, commit and quote step of E2/E3 is the gate seat's, not Grok's
- S8 ADOPT
- S9 ADOPT · STAKE
- Q1 ADOPT · Q3 ADOPT · Q4 ADOPT · Q7 ADOPT · Q8 ADOPT
- Q2 ADOPT WITH — S comes from the card's expected RESTARTS text, X only from a shared seam document, H only from a launch row
- Q5 ADOPT WITH — drop the "within 5 points" cut (below the noise at n=30); report the gap with its interval; the margin comes from a measurement; zero missed planted mismatches stays
- Q6 ADOPT WITH — no Fable naming for a HIGH build until his word on this tribunal (R919, LAWS.md:347)
- S11 ADOPT WITH — the SHADOW-HUB card also carries the Grok repo-write scope (STANDING-LIST.md:98 forbids it today) and five named seams
- Counts: adopt 10 · adopt with wording 8 · reject 0 (18)
- Experiments: X1 Grok's sandbox read/write reach from a worktree cwd · X2 cost per Grok pass · X3 E0 on each BASE today · X4 an ignored path for SHADOW-INSTRUCTIONS.md · X5 a fresh Opus check's run-to-run spread · X6 can headless Grok edit a large file without rewriting it whole
- Owner items: none
- WRONG FACTS: 5 (s4-p1 was not green at the first gate; "only existing strings"; S read from the build, not the card; a citation range; `tokens:` is context size, not meter use)
- WITHDRAWN: 2
- STAKE items: S1, S4, S5, S6, S9, (b)
- ESCALATE: 0

## Rulings

### S1 — three cards, an indication only, "insufficient data (n=3)"
ADOPT · SELF: no · STAKE: yes — the baseline is my own model, so a reading that favours or disfavours Grok is a reading about my tier.
The proposal says it plainly: §0 :17 "n=3 is insufficient data (L8). The trial gives an indication for his word. It cannot prove a tier", and S1 :171. L8 (LAWS.md:130) is a render rule. Reporting the result as "insufficient data (n=3)" and passing it to his word follows it. Each card is also n=1 against ONE Opus check whose run-to-run spread nobody has measured (X5). That belongs in the result line, and §2.4's last bullets already keep the set result an indication. No mechanism change.

### S2 — card choice, no migration cards
ADOPT WITH, replacing §2.1 "Why these three" bullet 3 (`complexity-routing-proposal-r2-2026-10-10.md:68`) with:
"- None of the three has a migration (a shadow migration would move `cobalt_dev` off `0013` for a branch that never lands; `s4-p2` (0024) and `price-floor` (0023) are excluded). Before pass T, the gate seat runs BUILD-HUB `## E0` as it stands on the untouched `<BASE>` (offline, then live-note). A red E0 ends that shadow with `FAILED: E0 — base red — <tests>` and scores nothing. The desk then takes the next checked card of the same band that has no migration and no MANDATORY HOUSE B (round 1 §1.2 table), and records the swap in the results table."
SELF: no. Why: §2.2 copies E2 and E3 (:79) but skips `## E0` (BUILD-HUB.md:64-65), the step every Opus original ran. The BASEs are old: `e4586978` is from 2026-10-09 18:25, `50b0cd87` from 10-08, and `git -C … log` shows main's tip is `a92661df` today. The live-note suite reads his notes as they are now (BUILD-HUB.md:65, :89). Failing scenario: s4-p1 shadow, pass S done, gate (e) live-note red on a test that is red on BASE too. That counts as "suites at first run: red" and costs Grok a re-pass (§2.2 step 6) for a red Grok never caused. E0 sorts this out before Grok's first pass. Cost: one offline run plus one live-note run per card, about 13 min going by the strike gate log (strike check :181, 621 s offline + 25 s live-note). One SHADOW-HUB line. Whether a BASE is red today is X3.

### S3 — Grok as house A on its own build; its held findings tallied apart
ADOPT · SELF: no
R921 (LAWS.md:349) seats a check as Opus plus house A = Grok. All three cards say `HOUSE B: as needed` (215:9, 118:9, 72:9), so Gemini does not sit. CHECK-HUB unchanged gives exactly that. The L67 floor holds because the Opus check session is a house other than the author. Every Grok finding is a test or command the Opus session runs (CHECK-HUB.md:20-21), so a self-finding is never taken on Grok's word. Tallying Grok's own held findings apart stops self-review from raising or lowering Grok's score. The one place it leaks is the "distinct defects" bar row, fixed under S5.

### S4 — primary figure = the Opus check session's own held findings
ADOPT · SELF: yes — it keeps the judging role in my house (the fresh Opus check). EVIDENCE: UNMEASURED (L67's check flow puts it there; that is a law, not a measurement) · STAKE: yes — my model is both the baseline and the judge.
This is the only source present on both sides. On the originals, house A was Sol (strike :223, radar :246, s4-p1 :279). On the shadow, under R920/R921, house A is Grok, so Sol-sourced and Grok-sourced counts cannot be compared. Opus-own is written before either list is opened (strike :98-99 "Written before either house's list was opened"; radar :139; s4-p1 :130). I re-derived the counts: strike O1 HELD (:137) = 1; radar O1, O2 HELD, O3 REJECTED (:158-160) = 2; s4-p1 O1, O3 HELD (:155, :157) = 2. Total 1 / 2 / 2.

### S5 — pass bar AT LEVEL / CLOSE BELOW / BELOW
ADOPT WITH, replacing §2.4's first two bullets (`complexity-routing-proposal-r2-2026-10-10.md:116-122`) with:
"- **AT LEVEL** on a card, when all of these hold: `ready: YES` with no fix round; Opus-own held ≤ the original's + 1; suites green at first run, or after 1 Grok re-pass; 0 scope breaks.
- **CLOSE BELOW** on a card: `ready: YES` after at most 1 fix round, Opus-own held ≤ the original's + 3, and at most 2 Grok re-passes.
- The tolerances +1 and +3 are MODELLED: no measurement of a fresh Opus check's run-to-run spread on one tip exists (X5). All-source held and distinct defects are reported in §2.3 beside each card and enter no bar."
SELF: no · STAKE: yes — loosening or tightening this bar moves Grok against my tier.
Why: "distinct defects" (§2.3 :103) counts every held row. On the originals, Sol's rows are in it: radar A3 is Sol's (`radar-display-fix-check-2026-10-08.md:163` HELD), and s4-p1's A3 and A2 were merged as the same defects as O1 and O3 (:156, :158). The shadow has no Sol (R920, LAWS.md:348). Failing scenario: radar shadow, Grok's tree has a WHERE-clause slip like A3. Only Sol would have caught it, so the shadow's distinct count drops to 2 against the original's 3. The bar then reads Grok as better than Opus for a defect nobody looked for, which tips toward Grok. In the other direction, a real defect Grok finds in its own build (S3: "not counted") would still enter "distinct defects" and count against it. Opus-own is the one comparable row (S4). The proposal gives no measurement behind the +1 and +3 numbers, so they are labelled modelled rather than changed.

### S6 — re-pass cap 2; the gate seat never repairs code; a third red is BELOW
ADOPT WITH, replacing §2.2 step 6 (`complexity-routing-proposal-r2-2026-10-10.md:86-88`) with:
"6. **Gate.** After pass S, the gate seat first runs the rows' own test files (`uv run pytest -q -rs -p no:cacheprovider --color=no <the rows' test files>`, as E3 runs them after each row, BUILD-HUB.md:71). Then it runs BUILD-HUB `## RESTARTS` and `## W` as they stand. A red at either step sends Grok ONE re-pass (pass S2) quoting, verbatim and nothing else, the run's summary line and, for each failing test, its node id and its first `E ` line (from the gate log: `grep -n -F` lines). The gate seat adds no hint, diagnosis or file:line of its own. The cap is 2 re-passes per card, both kinds counted together. After that the build stops `SHADOW BUILT … suites: red` and is scored, not repaired."
SELF: no · STAKE: yes — the feedback Grok gets decides how close its third try lands to my model's in-session loop.
Why: (1) an unspecified "failing lines quoted" leaves the gate seat free to quote more or less. That is the step where my house could tip the result (see (b)), and a fixed rule closes it. (2) An Opus builder runs its row tests after every row (E3, BUILD-HUB.md:71) before the full gate. Without the targeted run, every Grok red costs a full gate, about 38 min going by strike :181 (621 + 782 + 230 + 25 s), and the lock (L76). The cap and "never repairs" stay. They are what makes this a measure of Grok and not of the gate seat.

### S7 — two Grok passes (tests, then rows) for RED FIRST
ADOPT WITH, adding to §2.2 step 3 (`complexity-routing-proposal-r2-2026-10-10.md:79`) after "the fence: `src/` and `tests/` only, the rows' files only.":
" Above the copied E2 and E3 text, SHADOW-INSTRUCTIONS.md carries one line: `Every step in E2 and E3 that runs, quotes, mutates or commits is the gate seat's, not yours: you write files only.`"
SELF: no. Why: E2 and E3 tell the builder to run tests, quote output, make and undo mutations and commit (BUILD-HUB.md:68, :71). The Grok line says "Run no command" (§2.6 :146). Pasting E2 and E3 verbatim hands Grok two instructions that contradict each other, and how it resolves them changes what it writes. One line removes the conflict. Two passes keep the red commit before any `src/` edit (BUILD-HUB.md:67), the same order the originals have (strike `985f06fa` red then `b3d59b5f`; radar `37e496a1` then `8f42bf2e`; s4-p1 `e6f880e8` then `cfcef0a7`, from `git -C … log`).

### S8 — Grok's reasoning effort at the CLI default, recorded
ADOPT · SELF: no
CHECK-HUB's Grok seat line pins no effort (CHECK-HUB.md:91), and that is the profile Grok's checker record was made on. Pinning one would be a new flag on a new line. Recording the effort per pass is enough at n=3. Whether `medium` is what a headless pass really uses is read from each pass's own session summary (X2), not argued here.

### S9 — "above Sonnet and Haiku" left untested
ADOPT · SELF: no · STAKE: yes — Sonnet and Haiku are my house's lower tiers; leaving them out spares my house a comparison.
L29 (LAWS.md:204): "Sonnet/Haiku and their equivalents: non-write mechanical work only". The proposal also states the gap where the bar is set (§2.4 :126). The second half of his hypothesis stays an untested statement, not a result. Adding a Sonnet arm would cost Anthropic meter, and its L29 standing behind a gate seat would be a new question. Neither is needed to test the first half of the hypothesis.

### Q1 — a shadow log at launch before any routing changes
ADOPT · SELF: no
One launch-row field, no seat change (round 1 §4 rule 1, :98). It is the only way to reach n≥30 per band (L8) without moving a model.

### Q2 — inputs R, M, S, X, H, $
ADOPT WITH, replacing round 1 §2's table rows S, X and H (`complexity-routing-proposal-2026-10-10.md:76-78`) and r2 §1 :21 accordingly:
"| S: services restarted | the card's own expected RESTARTS text (the residents it names); a card that names none logs `S: not on card` and scores 0. Never the build's derived `RESTARTS:` line, which is an outcome | +1 each |
| X: seams | a seam document that both this card and another open card cite (L72, LAWS.md:367). A card's own 'ONE SEAM' into an existing module is not X | +2 each |
| H: new horizon | the drafter's launch row only; no row → `H: none recorded`, scored 0 | +4 |"
SELF: no. Why: round 1 §2 :69 says "none reads an outcome". Yet r2 §1 :26 scores strike `S2` from "RESTARTS aset+radar", which is the build's derived line. The strike card expects `com.cobalt.aset` only (`215-strike-fallback-env-card.md:46`), and the radar reach was "the builder's DECISION" (`strike-fallback-env-check-2026-10-10.md:159`). From the card, strike scores R0 + S1 = **1**. s4-p1's X2 counts the card's "ONE SEAM" (`72-s4-p1-card.md:14`), a seam to `CardStore.transition()` and not to another open card. H4 cites "new detector", not a launch row. From the card alone, s4-p1 is R5 + S2 = **7**, with X and H UNVERIFIED — the drafter's launch row for card 72 was not read. All three bands are unchanged (LOW 1, MID 5, HIGH ≥7). Radar = R3 (6 rows: card table count 6) + S2 (card :52 expects both) = **5** HOLDS.

### Q3 — non-write builds into the Sonnet trial
ADOPT (NO) · SELF: no
L29 says "mechanical work only". Every build runs the full gate (L68 GATE EARLY, LAWS.md:355), and the with-DB suite writes `cobalt_dev`.

### Q4 — band cut points 0–2 / 3–6 / ≥7
ADOPT · SELF: no
They are marked modelled (round 1 §2 :81) and reset from the shadow log at n≥30 per band. No measurement exists to set them now.

### Q5 — the Sonnet drafter trial's PASS bar
ADOPT WITH, replacing round 1 §5.2's PASS line (`complexity-routing-proposal-2026-10-10.md:115`):
"- PASS for Sonnet: n≥30 per arm; zero missed planted mismatches; and the first-run ready rates of both arms reported with n and the 95% interval of their difference. Sonnet passes when that interval's lower bound is above minus the key `sonnet_trial.margin_points`. That key has no value until the Opus arm's own first-run spread is measured over its first 30 launches; no number is written before that measurement."
SELF: no. Why: "within 5 points" sits below the noise at n=30. Steps: at p≈0.8, one arm's standard error is √(0.8×0.2/30) = √0.00533 ≈ 0.073. The difference of two arms has SE ≈ √2 × 0.073 ≈ 0.103, so a 95% interval is about ±20 points. Two equal arms land more than 5 points apart well over half the time (P(|Z| > 0.05/0.103 ≈ 0.49) ≈ 0.62). A point cut there passes or fails by chance. Zero missed planted mismatches is the known-answer gate, and it stays.

### Q6 — HIGH → Fable named per job via the brain
ADOPT WITH, replacing round 1 §4 rule 3 (`complexity-routing-proposal-2026-10-10.md:100`):
"3. HIGH builds and HIGH design proposals: AFTER his word on the model tribunal's result (R919; LAWS.md:347), the desk names Fable 5.1 to the brain per job and the brain asks him. Until that word every merged build stays Opus 5.5 and nothing is named. No automatic Fable."
SELF: yes — it keeps HIGH work within my house's tier ladder. EVIDENCE: UNMEASURED.
Why: R919 (LAWS.md:347) says "Every merged build stays Opus 5.5 (L29) until his word on the model tribunal's result". Naming Fable for a HIGH merged build now would be a model change before that word. The wording only orders the steps. It reopens nothing (L77).

### Q7 — the JEV picker compared blind against the score
ADOPT · SELF: no
A blind router compared against the score keeps the score as a baseline and not as a feature it can learn from. R8's 80% agreement gate stays where his ruling put it.

### Q8 — retire the score if band does not beat row count at n≥30
ADOPT · SELF: no
It follows from the data: in round 1's sample, 1–2-row cards held 11 findings (`guard-g2`, `radar-ladder-refresh`, round 1 §1.2 :30, :32). The score has to earn its keep.

### S11 — launch only after the SHADOW-HUB card is built, checked and approved
ADOPT WITH, replacing §3's "R411 STOP" bullet list (`complexity-routing-proposal-2026-10-10.md:160-163`) with:
"- **R411 STOP:** this seat needs `dontAsk` on a write path, so it must be a FIXED file launched by a launcher kind (L29; `desk-launch.sh:454-456` passes only `auto` and `plan` on a prompt). Neither exists, and the Grok builder line is outside the standing `Bash(grok *)` scope: `STANDING-LIST.md:98` lets Grok's sandbox write 'only under `agy-trial/scratch/tribunal-bars-0920/`' and never 'the repo'. The SHADOW-HUB card therefore carries, for his ONE approval of the list:
  - `SHADOW-HUB.md` (the gate seat's procedure) and `desk-launch.sh shadow <card>` (BUILD-HUB's LAUNCH (0)–(2) with SHADOW-HUB and the line above);
  - the Grok builder line of §2.6 as a NEW scope of `Bash(grok *)`: writes under `/Users/cobalt/cobalt-wt/<job>-grok/**` only;
  - before every Grok pass: `ls <WT>/.env` → `No such file` (L41; `ops/grok-sandbox.toml` denies `/Users/cobalt/cobalt/.env` but not a worktree's copy);
  - SHADOW-INSTRUCTIONS.md at a worktree path that `git check-ignore -v` proves ignored (X4), so `git status --short --branch` stays `## shadow/<job>-grok` for the check's PREFLIGHT (`ops/desk/preflight.sh:8-11` fails on any other line);
  - the shadow BUILT line carries `self-check: <k> of 3` honestly (`preflight.sh:230` accepts 0–3). `card-fill.sh` refuses anything below 3 (`card-fill.sh:5`, `:71`), so the desk fills the shadow card's `TIP` and `CHECK REPORT` header lines by hand, which `desk-launch.sh check` needs (`desk-launch.sh:917`), and records them.
  - Until that card is approved, the tribunal can still rule on §1, §2.1–§2.5 and §4."
SELF: yes — the gate seat it keeps is an Opus seat. EVIDENCE: UNMEASURED (L29's floor puts it there; no measurement).
Why: the stop is in the right place. The prompt kind refuses the mode (desk-launch.sh:454-456) and the write strings too (desk-launch.sh:105-108: `git add`, `git commit`, `uv run`). But §0 :16 says "Everything else uses existing strings", and the standing Grok scope forbids repo writes, so that one approval must name the scope explicitly. The other four bullets are seams the real readers enforce. Without them, the first shadow check FAILS at PREFLIGHT on the untracked instructions file, or at launch on an empty TIP. Price: no new file beyond the proposal's two, five lines in the SHADOW-HUB card, and no new string beyond the Grok scope (the `ls` is already on BUILD-HUB's list).

### (a) THE FACT BASE
| claim (proposal) | file:line | verdict |
|---|---|---|
| strike card committed `bc051c44` | strike check :16 | HOLDS |
| strike build tokens 165,478 | strike check :41 | HOLDS |
| strike Grok FINDINGS 0 | strike check :129 | HOLDS ("House B (Grok): no finding.") |
| strike O1 held | strike check :137 | HOLDS |
| strike held 1, ready YES, check tokens 138,173 | strike check :223 | HOLDS |
| strike red `245f3fd6` | strike check :139 | HOLDS |
| radar card committed `0deb06fc` | radar check :16 | HOLDS |
| radar build tokens 179,901 | radar check :42 | HOLDS |
| radar O1, O2 held | radar check :158-159 | HOLDS |
| radar A3 held (Sol) | radar check :163 | HOLDS |
| radar held 3, Grok FINDINGS 0, tokens 176,294 | radar check :246 | HOLDS |
| s4-p1 card committed `d35d6841` | s4-p1 check :18 | HOLDS |
| s4-p1 build tokens 415,769 | s4-p1 check :45 | HOLDS |
| s4-p1 O1, O3 held; A3, A2 same defects | s4-p1 check :155-158 | HOLDS |
| s4-p1 held 4, open 7, tokens 259,254 | s4-p1 check :279 | HOLDS |
| s4-p1 Grok: 3 REJECTED + B2 UNSETTLED, at :163-165 | s4-p1 check :160, :163-165 | HOLDS in substance; B1's REJECT is at :160, outside the cited range |
| s4-p1 red `720cc29f` | s4-p1 check :167 | HOLDS |
| Grok held 2 of 2 on stop-guard-g7 | stop-guard-g7 check :166-167 | HOLDS (B1 is "same cause as A1", :166) |
| BASEs 8f4bbe28 / 50b0cd87 / e4586978 | cards :5 | HOLDS |
| `HOUSE B: as needed` on all three | cards :9 | HOLDS |
| s4-p1 ONE SEAM | `72-s4-p1-card.md:14` | the text HOLDS; scoring it as X does not fit round 1's X definition (Q2) |
| BUILD-HUB LAUNCH (0) | BUILD-HUB.md:9 | HOLDS |
| BUILD-HUB 26 allow, 4 deny | BUILD-HUB.md:12-14 | HOLDS (:14 "26 allow … 4 deny") |
| CHECK-HUB copies files for houses | CHECK-HUB.md:91 | HOLDS |
| `--sandbox cobalt-job` denies `.env`, `~/.cobalt`, agent homes | ops/grok-sandbox.toml | HOLDS (the repo `.env` path only, not a worktree's) |
| prompt kind passes only auto/plan | desk-launch.sh:454-457 | HOLDS (:454-456) |
| `Bash(grok *)` standing | LAWS.md:321 | HOLDS; its approved scope is STANDING-LIST.md:98 (scratch only) |
| R919/R920/R921/R908 | LAWS.md:347/348/349/346 | HOLDS |
| R919 at `cto-2026-10-10.md:12` | cto-2026-10-10.md:31 today | line drift (the desk file adds rows above); content HOLDS; the line at the proposal's commit is UNVERIFIED (would need `git show 17ef6b09:…`) |
| "all three originals BUILT on the first gate" | `git -C … log e4586978..2433078f` | DOES NOT HOLD (WRONG FACTS 1) |
- The three scores from card fields: strike **1** (not 2), radar **5**, s4-p1 **≥7**, with X2 and H4 UNVERIFIED from the card (Q2). Bands LOW/MID/HIGH HOLD.
- Held counts 1 / 3 / 4 HOLD (the stop lines above). Opus-own 1 / 2 / 2 HOLD (S4).
- §1.3 states Grok's record as a reviewer, "not evidence about Grok as a builder" (:36). HOLDS.
- n=3 is stated plainly as insufficient (§0 :17, S1). HOLDS.
- Not settled by reads: Grok's tokens per call (no token field, per the proposal; I did not open `~/.grok`); whether `tokens:` in the BUILD stop lines comes from `desk-context.sh` as the check's does (strike :220) — UNVERIFIED.

### (b) THE TRIAL'S FAIRNESS — §2.2 walked for `radar-display-fix`
STAKE: yes — my house writes the instructions, runs the gate, quotes the failures, checks the result, and is the baseline.
1. Shadow card: rows byte for byte. The card has had no row change since its check: its last commit is `0deb06fc` "TIP … and check report filled", a header-only fill (`card-fill.sh:6`). No leak from the original's check through the card.
2. Worktree at `50b0cd87`: neutral. The tree is two days old. E0 (S2) separates base reds from Grok's.
3. SHADOW-INSTRUCTIONS: the gate seat's widest lever. Verbatim rows plus E2/E3 plus the fence leaves it nothing to add, provided "verbatim" is the rule and the S7 line removes the run/commit conflict. Risk named: the gate seat (Opus, `--add-dir /Users/cobalt/cobalt`) can read main, where the original fix `8f42bf2e` and the check fix `eb14f860` live. The rule is that nothing after BASE enters the file. Whether Grok itself can read `/Users/cobalt/cobalt` from a worktree cwd is X1.
4. Pass T and its commit: the gate seat commits what Grok wrote. Timing cannot tip the result because each pass is one commit.
5. Pass S: the same. A path outside the rows is recorded as SCOPE and not reverted, which is neutral.
6. Gate and re-passes: the quote rule (S6) removes the seat's discretion. Remaining asymmetry, against Grok and not fixable without giving Grok a shell: the Opus builder ran its tests and the E3 MUTATIONS in session (BUILD-HUB.md:71). Grok gets at most 3 blind tries, and no mutation step runs on its tests. The original radar's O1 and O2 were exactly "test stays green under a mutation" (radar check :143-144, :158-159). Grok's tests face that class with no mutation loop. The trial therefore measures "Grok through this harness", and the result line must say so.
7. Build report: the gate seat's prose. Its BUILT line names `builder: grok-4.7`.
8. Check: a fresh Opus that has never seen the original, which is good. But it knows the builder is Grok (JOB `-grok`, BRANCH `shadow/…-grok`, the BUILT line). That bias is unmitigated and named here. Its reach is limited: a held finding must run red (CHECK-HUB.md:20-21), so bias can work only through effort (looking harder or less hard), never by inventing a defect. House A = Grok on its own build, and there is no Sol: the original had Sol (A3 held, :163). That makes "distinct defects" non-comparable (S5).
9. Never merged: neutral.
§2.3 row by row: Opus-own held is comparable. All-source held and distinct defects are not (no Sol on the shadow). Fix rounds are comparable. "Suites at first green" is NOT comparable as written: the originals' column says "green" for all three, but s4-p1's build had a W red (WRONG FACTS 1), and an Opus builder's "first run" is after in-session iteration. Scope breaks are comparable (same CHECK-HUB `## 7` (ii) rule). Tokens: the Opus columns are context sizes, not meter use (WRONG FACTS 5), and Grok's are UNKNOWN. Not comparable as cost.

### (c) THE LAWS
- A write path with a model below Opus without the gate seat: none. Grok writes files only. Every command, commit and with-DB run is the gate seat's (Opus 5.5, `dontAsk`, a fixed file). L29's second condition, "a permission gate proven in a scratch test to stop file AND command writes" (LAWS.md:204), is what X1 proves for Grok's builder line. Running it is a precondition of the SHADOW-HUB card, not of this ruling.
- Production database: no. The with-DB suite runs on `cobalt_dev` under L76's lock, with `COBALT_ENV=production*` denied (BUILD-HUB.md:12). His notes: read-only, through the live-note suite (L68 allows it). His trading platform: nothing reads, writes or infers from it.
- Credentials (L41): the one gap is a worktree `.env` present while Grok runs. Closed by S11's `ls` bullet.
- Is `dontAsk` a real L29 need: yes. The gate seat runs the with-DB suite and commits on a branch. L29: "never auto mode on a write path". L62 (LAWS.md:323): a write-path launch never runs as a bare background launch. The prompt kind refuses both the mode and the write strings (desk-launch.sh:105-108, :454-456).
- Is the R411 stop at the right place: yes, plus the Grok scope (S11).
- Does the proposal change any model by itself: no. Builds stay Opus (R919), shadow branches are never merged (§2.2 step 9), and L29 changes only by his word.

## Self-attack
Writers and readers found (grep -rn / -rl over `prompts`, `reports`, `ops`, plus `desk-launch.sh`):
- `SHADOW-INSTRUCTIONS`: only `270`, `271` and the r2 proposal. No committed mechanism writes or reads it. NEW.
- `SHADOW-HUB`: `270`, `271`, `272`, the r2 proposal and its report. No file exists. NEW.
- `shadow/`: the r2 proposal and its report, `270`/`271`, and older unrelated uses (archiver runner "shadow" packets 2026-09-19, routing x1 Sonnet shadow prompt 2026-09-23/20, day-open reports). No script reads a `shadow/` branch. `desk-launch.sh:736` admits `/` in BRANCH.
- `desk-launch.sh` modes: `:105-108` (prompt kind refuses dontAsk and the write strings), `:454-456` (auto|plan only); check kind `:917-951` (needs TIP, CHECK REPORT, HOUSE B; BUILT `job · tip`); `:722` needs JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS; `:733` JOB `[a-z0-9-]`.
- `--permission-mode` / `dontAsk`: BUILD-HUB.md:3, :12; STANDING-LIST.md:54, :85, :109, :174, :192 (every fixed file dontAsk; BRAIN-HUB auto :209); desk-launch.sh:106, :456.
- `Bash(grok *)`: CHECK-HUB.md:10 (on its line); STANDING-LIST.md:98 (scope: scratch writes only, never the repo); LAWS.md:321 (standing).
- `--sandbox cobalt-job`: CHECK-HUB.md:91 and about 110 one-off prompts (all reviewer lines writing under scratch); `ops/desk/house-probe.sh`.
- `always-approve`: CHECK-HUB.md:91 ("never"); STANDING-LIST.md:98 ("never").
- `HOUSE B`: card headers :9; desk-launch.sh:768, :917-922; card-fill.sh:9; CHECK-HUB.md:22.
- `held:`: CHECK DONE lines (CHECK-HUB); read by `desk-launch.sh` only among ops.
- `ready:`: CHECK DONE lines; read by `ops/desk/deploy-step0.sh`, `deploy-card.sh`.
- `tokens:`: in stop lines (L71); no ops/desk script writes it; the check's value comes from `desk-context.sh`, which measures CURRENT context (desk-context.sh:3-5).
- `BASE`: card header; desk-launch.sh:726, :899-928 (hex8, exists, ancestor of TIP); BUILD-HUB E0/LAUNCH (0).
- `CHECK DONE`: written by CHECK-HUB; read by desk-watch.sh, desk-launch.sh, preflight.sh, stop-guard.py, bare-guard.py, desk-done.sh.
- `BUILT`: written by BUILD-HUB; read by card-fill.sh:67-71 (needs `self-check: 3 of 3`), preflight.sh:230 (`self-check: [0-3] of 3`), desk-launch.sh:866, :951, deploy-step0.sh:394, deploy-card.sh:187, desk-watch.sh:38, desk-done.sh:22, stop-guard.py:72, bare-guard.py:112.
Walk of my text against this list: S11's TIP/CHECK REPORT bullet rests on desk-launch.sh:917 and card-fill.sh:71 (both read). The status bullet rests on preflight.sh:8-11 (read). The Grok scope rests on STANDING-LIST.md:98 (read). The BUILT field rests on preflight.sh:230 (read). No shadow BUILT line reaches deploy-card.sh or deploy-step0.sh, because no deploy card names `shadow/` (§2.2 step 9).
WITHDRAWN: "an untracked SHADOW-INSTRUCTIONS.md makes `gate.sh` refuse the worktree" — `ops/desk/gate.sh:51` (its exits are lock, level and fingerprint; a grep of gate.sh for `status --short`/`untracked`/`dirty` finds nothing). The refusal is the check's PREFLIGHT, `preflight.sh:8-11`.
WITHDRAWN: "the shadow check could seat Gemini as house B to stand in for Sol" — LAWS.md:349 (R921: Gemini only on a mandatory-B build or a Grok failure) with all three cards `HOUSE B: as needed` (:9). That would reopen his ruling (L77).

## SELF-ASSIGNMENTS
- S4 ADOPT · SELF: yes (keeps the judging role on the Opus check) · EVIDENCE: UNMEASURED
- Q6 ADOPT WITH · SELF: yes (HIGH work stays within the Anthropic tier ladder) · EVIDENCE: UNMEASURED
- S11 ADOPT WITH · SELF: yes (the gate seat is Opus) · EVIDENCE: UNMEASURED

## Experiments (L70)
- X1 (missing from the proposal; this ruling adds it): in a scratch worktree at `8f4bbe28` (strike card), run the §2.6 Grok line from that cwd with a probe prompt asking it to (a) read `/Users/cobalt/cobalt/src/cobalt/aset/strike.py`, (b) write `<WT>/x1.txt`, (c) write `/Users/cobalt/cobalt-wt/agy-trial/scratch/x1.txt`, (d) read `<WT>/.env` after copying one in. Design change if (a) succeeds: SHADOW-INSTRUCTIONS forbids paths outside the worktree, and the shadow check greps Grok's diff for the original fix's lines. If (c) succeeds: the glob is not a fence, and L29's "permission gate proven" fails, so no shadow build launches. If (d) succeeds: S11's `ls` bullet is load-bearing.
- X2 (the proposal names it, §2.5): the messages and wall time of one Grok pass T and one pass S on the strike card, from its session summary, plus the `reasoning_effort` recorded there. Design change: if one pass approaches the 45-min limit CHECK-HUB gives a house (CHECK-HUB.md:89), SHADOW-HUB needs its own timeout.
- X3 (added): `sh /Users/cobalt/cobalt/ops/desk/gate.sh <scratch WT> all --deploy` on untouched worktrees at `8f4bbe28`, `50b0cd87` and `e4586978`, plus BUILD-HUB E0's live-note command. Design change: a red BASE swaps that card (S2).
- X4 (added): `git check-ignore -v <path>` in a worktree at each BASE for a candidate instructions path (for example under `tmp/` or a gitignored `docs/` folder). Design change: if no ignored path exists inside the workspace, SHADOW-HUB adds one `rm <WT>/SHADOW-INSTRUCTIONS.md` string (BUILD-HUB's `.env` rm pattern) before the BUILT line.
- X5 (added; sets S5's tolerances): run CHECK-HUB's OWN FINDINGS step twice, in two fresh Opus sessions, on one original tip (for example `b3d59b5f`), each read-only up to `## OWN FINDINGS`, and compare the held counts. Design change: if the two differ by 2 or more, "+1" is below the checker's own noise and AT LEVEL widens.
- X6 (added): a pass S on the radar card (`src/cobalt/aset/radar_panel.py`, a large `PANEL_JS` file), with `git diff --stat` after it. Design change: if Grok rewrites the whole file (thousands of lines changed for a 3-row fix) or truncates it, the trial is biased by tooling. SHADOW-HUB then records `whole-file rewrite` as a column and keeps that card's result apart.

## OWNER (after the tribunal)
none — every item is a design, figure or bar a house settles. The L29 amendment is his word on the result (R919) and is not one of the eighteen items.

## WRONG FACTS
1. r2 §2.3 :105 "green at build / green / green (all three originals BUILT on the first gate)" — `git -C /Users/cobalt/cobalt log --oneline e4586978..2433078f` shows `f6e72c94 wip(s4-p1-1009): W — skip outside the allowed set (card M1 (f)); build report`, followed by `2433078f fix(…): … (W-1, S-1; L35, L79)`. A W red, a fix and another gate (the BUILD-HUB.md:91 path). s4-p1 was not green at its first gate.
2. r2 §0 :16 "Everything else uses existing strings" and §2.6 :140 "only existing strings" — `STANDING-LIST.md:98`: the standing `Bash(grok *)` "can touch: its sandbox writes only under `agy-trial/scratch/tribunal-bars-0920/`"; "never touches: the repo, a vault". The builder line's `Write(/Users/cobalt/cobalt-wt/<job>-grok/**)` is a new scope.
3. r2 §1 :21, :26 S from "RESTARTS aset+radar" for strike — `215-strike-fallback-env-card.md:46` expects `com.cobalt.aset` only; `strike-fallback-env-check-2026-10-10.md:159` "the extra `com.cobalt.radar` is the build's DECISION". The card-field score is 1 (LOW either way). This also contradicts round 1 §2 :69 "none reads an outcome".
4. r2 §1.3 :34 cites `s4-p1-check-2026-10-09.md:163-165` for "Three were REJECTED and B2 was UNSETTLED" — B1's REJECT is at `:160`; :163-165 hold B4, B3, B2.
5. r2 §2.5 :129-132 sums the stop lines' `tokens:` as Anthropic meter use ("Total: about 0.9–1.0 M tokens. That compares with 1.33 M") — `ops/desk/desk-context.sh:3-5`: "the desk's CURRENT context size in tokens … input + cache_read + cache_creation" of the last recorded usage; the check's figure comes from it (`strike-fallback-env-check-2026-10-10.md:220` "context 138173 of 400000"). It measures context at the end of the run, not consumption. Round 1 §6 :120 ("≈10.4 M tokens over 53 runs") carries the same unit error. Whether the builds' `tokens:` use the same script is UNVERIFIED.

## READING
- `271-model-tribunal-opus-seat.md` whole (the launch prompt).
- `LAWS.md` :1-12, :93-132, :186-265, :265-399 (Preamble, Reading, L1-L9, L25-L80), plus the heading grep.
- `complexity-routing-proposal-r2-2026-10-10.md` whole; `complexity-propose-r2-2026-10-10.md` whole; `complexity-routing-proposal-2026-10-10.md` whole; `complexity-propose-2026-10-10.md` whole.
- `brain-direction-2026-10-02.md` heading grep, :186-199.
- `cto-2026-10-10.md` grep rows R908, R919, R920, R921, R942 and the `270-model-tribunal.md` grep; `cto-2026-09-22.md` grep R109.
- `270-model-tribunal.md`: a grep for `01-QUESTIONS.md (verbatim)`, `HOW TO RULE`, `THE ITEMS`, `TRIBUNAL R1:`. The grep output also showed lines :40, :44, :47, :50, :59 (hub procedure text: Astra's sentence, floor rules, table layout, the Opus-seat file-check, its stop line). That is prompt text, not any house's ruling. Read only through the grep, not opened further.
- `259-f4-tribunal-r2-opus-seat.md`: ten `grep -c` checks.
- `strike-fallback-env-check-2026-10-10.md` :1-50, :95-224 and its heading grep; `radar-display-fix-check-2026-10-08.md` a grep for key lines (:16, :42, :139-171, :238-246); `s4-p1-check-2026-10-09.md` a grep for key lines (:7-45, :130-173, :264, :279) and a `720cc29f` grep (:167, :217-231); `stop-guard-g7-check-2026-10-09.md` :140-168.
- Cards: `215-…:1-12`, `118-…:1-16`, `72-…:1-16`; a RESTARTS grep in all three (215:46, 118:23, :52; 72:14, :27, :29, :59); a row-line count (2, 6, 8).
- `BUILD-HUB.md` :1-16, :64-105 and its heading grep; `CHECK-HUB.md` :20-24, :89-92; `STANDING-LIST.md` heading and table grep (:16-214); `ops/grok-sandbox.toml` whole.
- `~/.claude/ops/desk-launch.sh` mode grep, :100-111, :440-459, :720-767, :912-953, a tree_state grep (:745-751) and a field grep.
- `ops/desk/card-fill.sh` :1-30; `ops/desk/desk-context.sh` :1-12 and a grep; `ops/desk/preflight.sh` status grep (:8, :11, :100, :105, :128-129); `ops/desk/gate.sh` status grep (:51, :352-427).
- `git -C /Users/cobalt/cobalt log`: the authorization gates (`75b2aa57`, `3fa4a0f9`, `17ef6b09` ×2); the ranges `50b0cd87..8f42bf2e` and `e4586978..2433078f`; the dates of `8f4bbe28`, `e4586978` and main `a92661df`; messages of `f6e72c94` and `2433078f`; the history of the three card files.
- Self-attack greps: `SHADOW-INSTRUCTIONS`, `shadow/`, `SHADOW-HUB`, `Bash(grok *)` (output persisted to a tool-results file and read only from its preview), `--sandbox cobalt-job`, `always-approve`, `BUILT` (ops/desk), `CHECK DONE`, `held:`, `ready:`, `tokens:` (ops), and desk-launch.sh field names.
- Not opened: the houses' folder, the hub's report, any vault note, `Rules.md`, `~/.grok`. Tokens for this seat: UNMEASURED (no measure command on this line).

## L74
This session received two system-channel notices, not inside a tool result. One asked for a `Claude-Session:` line in commit messages and PR bodies and named a file-send tool. The other loaded a docs connector's instructions. This seat makes no commit, sends no file and uses no connector. Recorded once here; not acted on.

## ESCALATE
none

## CONTINUE
next: none — ruling written 17:02 EDT (date).

MODEL TRIBUNAL OPUS R1 DONE · verdict: ADOPT AFTER fixing the gate, scoring and Grok-scope seams named in S2, S5, S11 · adopt: 10 · adopt with wording: 8 · reject: 0 · ESCALATE: 0
