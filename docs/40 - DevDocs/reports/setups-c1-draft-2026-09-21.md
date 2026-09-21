# SETUPS C1 — draft of build + check prompts (2026-09-21)

Seat `setups-c1-draft-0921` · Opus 5 · 17:04–17:2x ET · reads only, two prompt files + this report written, nothing launched, nothing committed.

## §0 Headline

- **Drafted:** `56-setups-c1-build.md` (Opus 5 hub, branch `setups/c1-rubberband-0921`, worktree `~/cobalt-wt/setups-c1`, offline + `cobalt_dev`) and `57-setups-c1-check.md` (Sonnet 5 hub, three houses, Astra required, fails closed on METER). R40 = B built as the Fable seat's R2-2.1–2.5 texts; C1 builds closure term (3) only.
- **NEW approvals: 2 strings** (`cp` / `rm` of `.env` for `setups-c1`). Every other string is byte-identical to an approved line (proof below).
- **The main finding: no committed real-shape day exists on which the full Rubberband shape forms** (FTFT's day is covered by its day-1 HTF avoid; BGFI is stale by design). §9 gates 1–3 for the full shape are therefore UNPROVEN in `56` and pinned as a named gap. Closing it needs a fixture cut from the database that no approved string can run. ASK DESK (E1).
- Also found: `replay/formations.py:81` accepts only `"s2p2.1"`. C1's version bump would make the nightly replay refuse every night unless that set is updated, so `56` adds the new version under gate 5 (E3). The receipt card entry has a second writer the FINAL does not cite (E4).
- ESCALATE: 9 (two ASK DESK, safe defaults taken).

## C1's scope (every row is FINAL §10 C1 or R40; nothing added)

| item | FINAL tag | file(s) | test in `56` |
|---|---|---|---|
| direction from anatomy: `relation` never read, trade against the unqualified Extension; the `Setup(relation)` refusal and the order-dependent label deleted | §1, `A-01`, [F-01] | `radar/evaluate.py:34-37`, `:635-647` | T1 (defect RED→GREEN), T4 (reversed `valid_setups` → same formation) |
| `unclassified` token, a module constant outside `SetupRef` | [F-07] | `radar/evaluate.py` | T4 |
| no unbound-direction refusal | [R2F-01] | none | T4 (the def forms; no refusal path exists) |
| geometry guard: point (5), or §2.3 alone if X17 fails | §2.3, §9 (5), [F-16 · X17] | `radar/evaluate.py` formed block | T3 |
| gate 1 / point (1): real-shape formation, all four values asserted | §9 (1), [F-21], [F-16] (1) | `tests/cobalt/test_rubberband_forms.py` (new) | T2; full shape = FULL-SHAPE DAY gap (E1); blind values (E2) |
| gate 2: evaluable ⇒ forms | §9 (2) | same | T2 with the `AWAITING_A_DAY` pin (E1) |
| gate 3: live-note test asserts `formed` | §9 (3), [F-16] (2) | `tests/cobalt/test_radar_evaluate.py:692-714` | re-pointed; SKIPPED in build; run at deploy |
| gate 4: `--expect-formed` exits non-zero on 0 | §9 (4), [F-16] (3) | `radar/evaluate_cli.py`, `radar/cli.py:34-43` | T2 gate 4 |
| gate 5: another evaluator version refused by replay; nightly binding accepts the bump | §9 (5), [F-19 · X9] | `radar/evaluate.py` `replay_receipt`, `:132`; `replay/formations.py:81` | T2 gate 5 |
| point (4): the corpus shape is `evaluable` | [F-16] (4) | test | T2 |
| ONE `assumed_formation` dot, untappable | R40; R2-2.1, R2-2.3 | `cards/scoring.py:72` (+`ASSUMED`, constant), `:247-251` (reason text); `cards/store.py:1200-1204` (refusal); `radar/evaluate.py` `card_dots` at `:774`, `:1077`, `:1383`; `radar/audit_export.py:362` | T5 (a)–(e) |
| key from a module constant (`ASSUMED_CONVENTIONS = ("A-01",)`), closure term (3) only | R2-2.2, R2-2.3 | `radar/evaluate.py` beside the direction line; `Formation.assumed_keys` | T5 (a) |
| key rides the dot and the receipt; `AtomOutcome` closed | R2-2.1, R2-2.4 | receipt card entry `:1425-1429` AND `_receipt_card` `:1474-1480` | T5 (c)(5) |
| X8 reworded to include a tap; ORDER BY unchanged | R2-2.5 | none (`cards/radar.py`, `TIE_POLICY` empty diff) | T5 (c)(1), (d), (e) |
| first card shows NO score for its life | §10 Evenings, R40 | DevDoc `radar/evaluate.md` sentence | D1; 57 Q7 |

## The five recompute paths (main `23fb828`)

| # | path | `file:line` | how B keeps the score null |
|---|---|---|---|
| 1 | tap of any OTHER dot | `cards/store.py:1215-1225` (`_dots_for` → `suppression(dots)` → UPDATE) | the stored dot is never tapped, so `suppression()` still blocks |
| 2 | `refresh_card` | `radar/evaluate.py:774-800` | `card_dots` re-appends from the card's OWN stored dot |
| 3 | `refresh_dots` | `cards/scoring.py:201-235` (called at `evaluate.py:775`) | it drops any factor absent from `fresh` (C3b), so the append must come after it. This is X27 |
| 4 | audit export | `radar/audit_export.py:362-374` | `card_dots` with `ev.formation.assumed_keys` |
| 5 | replay | `radar/evaluate.py:1077-1088` | keys from the receipt card entry, which both writers carry (`:1425-1429`, `:1474-1480`) |
| + | create | `radar/evaluate.py:1383-1396` | the fourth `compute_dots` site |
| + | the column's other writer | `cards/store.py` `refresh_radar_card` (`:1039-1047` per A7) | writes the `CardUpdate` from path 2 (57 check (vi) lists every writer) |

## Which experiments need `cobalt_dev`

| exp | C1's (FINAL) | where in `56` | `cobalt_dev` |
|---|---|---|---|
| X3 | C1 acceptance | **UNPROVEN in build**: `cobalt radar evaluate` is not in the build's strings, and the worktree has no `data/radar-cache` (cwd-relative, `configs/cobalt/radar.yaml:31`; production holds 09-14…09-18, 09-21) → runs at the DEPLOY from `~/cobalt` | deploy |
| X8, tap half | C1 | T5 (b), (c)(1), (d) | **yes** (with-DB `tap_dot`) |
| X9 | C1 | T2 gate 5 | no (offline) |
| X17 | C1 | T3, on main's code first | no |
| X24 | C1 under B | T5 (d): `shadow_agreement_v` + ladder | **yes** |
| X27 | C1 under B | T5 (c)(3): pure `refresh_card` | no (the stage leg with-DB) |
| X28 | only under A | not assigned (R40 = B) | — |
| fixture day | "stored pool days for the definition-written fixture" | E1 | would need a DB cut |

`cobalt_dev` steps in `56`: PREFLIGHT reachability probe, with-DB BASELINE, T5 with-DB legs, A1, CLOSE. Each one is cp → `COBALT_ENV=dev uv run pytest …` → rm → `ls` proof.

## Prompts

| file | size (B) | seat | launch |
|---|---|---|---|
| `prompts/2026-09-21/56-setups-c1-build.md` | 63,833 | Opus 5, hub `setups-c1-build-0921`, NO `--permission-mode` (L29 write path, as `02`) | desk: `git -C /Users/cobalt/cobalt worktree add -b setups/c1-rubberband-0921 /Users/cobalt/cobalt-wt/setups-c1 main` · `cd /Users/cobalt/cobalt-wt/setups-c1` · `claude --bg …` — AFTER `deploy-2026-09-21b` |
| `prompts/2026-09-21/57-setups-c1-check.md` | 36,615 | Sonnet 5, hub `setups-c1-check-0922`, auto mode (read-only seat) | `cd /Users/cobalt/cobalt-wt/agy-trial` · `claude --bg …` — after `SETUPS C1 BUILT`, staggered after `52` / `54` |

## RULE PROOF (per string; `grep -c -F`, run by this seat 17:1x ET)

| prompt | strings | against | count |
|---|---|---|---|
| 56 | `"Bash(uv run pytest *)"` | `2026-09-21/02-bars-chunk-2-fix-r3.md` | 1 |
| 56 | `"Bash(uv run cobalt jobs restarts *)"` | same | 1 |
| 56 | the 14 remaining allow strings + `--disallowedTools` 3 + `--add-dir` triplet, as ONE contiguous substring from `"Bash(git add *)"` to `/Users/cobalt/cobalt-wt` | same | 1 (the build hub proves each one separately at launch) |
| 56 | `"Bash(COBALT_ENV=dev uv run pytest *)"` | `2026-09-19/44-archiver-db-rerun.md` | 1 (his 09-19 R18 row names it as reused, count 2 in `cto-2026-09-19.md`) |
| 56 | `"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)"`, `"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)"` | every file under `prompts/` | **0 — NEW** |
| 57 | `--allowedTools` 14 + `--disallowedTools` 3 + `--add-dir` triplet, as ONE contiguous substring | `2026-09-20/08-bars-chunk-e-check.md` | 1 (the hub proves each one separately) |
| 57 | date gate literal `Bash(grok *) and Bash(agy *) through 2026-09-22` | `cto-2026-09-21.md` | line 50 (R39), committed `3ecbb27` |
| both | R40 literal `ONE EXTRA DOT THAT CANNOT BE TAPPED` | `cto-2026-09-21.md` | committed `23fb828` |

Approvals behind the reused strings: `02` / `11`'s 16+3 → his 09-20 R25 ("approved"; the row says OFFLINE builds). `COBALT_ENV=dev uv run pytest *` → his 09-19 R18 ("approve env"). `57`'s 14+3 → his 09-20 R13 (via `08`), plus grok/agy by R23 (through 09-21) and R39 (through 09-22).

**NEW approvals:**
1. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)`
2. `Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)`

What the desk shows him, verbatim: *"C1 build (`56`): approve two strings, the same pair as 09-19 R18 for the new worktree — `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)` · `Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)`. They copy `.env` by name into the C1 worktree only while a dev-database test runs. It is never printed and is removed at the end. Also reused on this launch: `Bash(COBALT_ENV=dev uv run pytest *)` (09-19 R18) and the 16 offline Opus strings (09-20 R25). No production, no push."* The launch row must quote the two strings and his words. `56` checks that row with `git log -S` on the rm string.

## Other unmerged branches (L68) and shared files

| branch | status | files shared with C1 |
|---|---|---|
| `s2/degraded-line-0921` | lands tonight ≈20:02 (`deploy-2026-09-21b`); C1 branches after it | none |
| `s2/stale-marker-0921` | built tonight after `16`; deploys TUE ≈20:02 (`53`) | none by design. `tests/cobalt/test_radar_panel_cards.py` is shared ONLY if X24 fails or A1 re-points a panel test there; `56` CLOSE reports it |
| `bars/chunk-1a-0920` | unmerged | none (`db_migrations/`, `configs/…/tunables.yaml`, tests) |
| `bars/chunk-2-0920` | unmerged | none. It touches `radar/poller.py`, `radar/runner.py` and `src/cobalt/cli.py`. C1 touches `src/cobalt/radar/cli.py`, a different file |
| `bars/chunk-e-0920` | unmerged | none (`tests/experiments/`) |
| `s2/rubberband-proof-0921` | proof, never merging | none: C1's test file is `test_rubberband_forms.py`, not the proof's filename |
| `ops/agy-trial-0915`, `sprint-2/cards` | old | not checked file by file |

## What C1's DEPLOY will need (facts only; the desk decides)

- **His chat "approve"** (L7 / L61): C1 is a trading-logic change and the first card has no score for its life.
- **RESTARTS**, derived by the tool at build CLOSE. Expected: `com.cobalt.radar` (imports `radar.evaluate`) AND `com.cobalt.aset`. The aset restart comes from `aset/web.py:47`, which imports `cobalt.cards` (`store.py` and `scoring.py` change). That is L42's import rule, not rendering: B changes no panel code. The one-shot `com.cobalt.replay` (21:10 ET) reads `replay/formations.py` and `radar.evaluate` on its next run. L66: both residents go down before the merge, inside 20:00–21:00.
- **No migration.** No `--allow-prod`.
- **Acceptance steps the build cannot run**, each needing strings in the deploy's own list:
  - X3 + gate 4: `cobalt radar evaluate --replay <day> --trade-def rubberband --expect-formed` over the last 10 stored sessions, from `~/cobalt` where `data/radar-cache` lives (the 09-19 deploy ran `--replay` on production, `writes: none`). Zero formations is allowed by X3 but fails `--expect-formed`, so the deploy must say which governs.
  - The live-note test with `COBALT_LIVE_VAULT_ROOT` set; a SKIP is RED ([F-16] (2)).
  - The NN#16 smoke.
- **`EVALUATOR_VERSION` bump:** receipts written before the deploy are refused by replay and audit export afterwards (gate 5). The nightly replay keeps working only through `56` item 6.
- **Stacking with `53` on TUE or WED:**
  - C1 builds tonight after ≈20:02. `57` runs TUE, staggered after `52` and `54` (same seats).
  - The deploy prompt is drafted after `57`, then read by another house, then approved by him.
  - L43 allows one production deploy per evening, so a TUE landing means ONE stacked deploy (C1 + stale-marker) with the L68 integrated gate on the combined tree, which changes `53` into a stacked deploy (a re-issue).
  - Otherwise C1 takes WED.
  - The two branches share no source file.

## READING

`55-draft-setups-c1.md` · `LAWS.md` 1–405 in full · FINAL `SETUPS-AT-DEFAULTS-FINAL-2026-09-21.md` 1–176, 261–496 (§3–§6 not read; not C1's) · `setups-tribunal-derive-r2-2026-09-21.md` (grep + 43–82) · `setups-tribunal-fable-r2-2026-09-21.md` 27–92, 196–238 · `setups-tribunal-r2-2026-09-21.md` (grep, 490–617) · `cto-2026-09-21.md` rows R15, R17, R18, R24, R39, R40 + §12 15:16 bullet · `cto-2026-09-20.md` rows R13, R23, R25 · `cto-2026-09-19.md` R18 (grep) · proof report (whole) + proof test (grep of defs) · gap table (grep E1/E8/E9) · `deploy-2026-09-19.md` (grep) · code on main: `radar/evaluate.py` 20–169, 320–339, 590–829, 905–944, 1000–1099, 1296–1495 · `radar/evaluate_cli.py` whole · `cards/scoring.py` 60–269 · `cards/store.py` 1150–1244 + grep · `radar/audit_export.py` 335–384 · `radar/replay.py` 80–149 · `aset/radar_panel.py` 640–679 + grep · `aset/web.py` 1350–1374 + grep · `radar/config.py`, `configs/cobalt/radar.yaml`, `db_query.py`, `replay/formations.py`, `cards/radar.py`, `cards/shadow_report.py`, `0007_radar_cards.sql` (grep) · `tests/cobalt/test_radar_cards_db.py` 1–96 + grep · `tests/cobalt/test_radar_evaluate.py` 680–719 · `tests/fixtures/radar/_cut_p2_fixtures.py` · prompts `51`, `52` whole; launch lines of `02`, `10`, `11`, `25` (09-20), `37`, `44` (09-19), `08` (09-20) by grep · `git branch --no-merged main` + `diff --stat` of five branches · `ls` of `data/radar-cache`, fixtures, DevDocs.

## ESCALATE

1. **THE FULL-SHAPE DAY (§9 gates 1–3; FINAL §10 C1 cell "stored pool days for the definition-written fixture [F-21]").**
   - No committed real-shape day exists on which the full Rubberband shape (4+1 relations AND the day-1 HTF avoid) forms. FTFT's day is covered by the avoid (proof ESCALATE 2); BGFI is stale by design (proof test A).
   - Cutting one needs a DB read into a committed file. `_cut_p2_fixtures.py` takes raw reads the hub saved; `cobalt db query` has no output file (`db_query.py:209-215`); no approved string runs `python` or a redirect. The worktree also has no daily cache.
   - `56` as drafted proves the RELATION path on the committed day (all four values) and the full shape `avoided` there. It pins the full shape in `AWAITING_A_DAY`. This is a NAMED deviation from gate 2's text ("a def the registry calls evaluable that has no formation fixture fails the suite").
   - `ASK DESK: (A) a separate DB-backed fixture-cut job before 56 (new strings; a stored pool day never chosen because he traded or tagged it, R24; then 56 is re-issued without the pin), or (B) 56 as drafted, with the gap closed by such a job before C1's deploy? [17:2x]` — safe default taken: **B**.
2. **[F-16] (1)'s BLIND step is not in `57`.**
   - `56`'s four expected values come from main's engine on the `COUNTERTREND_ONLY` control. They are the definition on the stored bars, and C1 does not touch the trigger and stop code, but a checker house did not write them blind.
   - A blind step does not fit `57`: the ≤120 KB cap, one attempt per house, and a "read this first" instruction inside the same launch is not blind. It also needs the anatomy rules to recompute the culmination.
   - `ASK DESK: run a small blind seat (bars excerpt + neutral def + anatomy excerpts only; each house writes side / formed bar / trigger / stop) before C1's deploy? [17:2x]` — safe default: `57` asks (Q2) whether the constants are the definition evaluated on the bars, and the deploy prompt carries the blind step as owed.
3. **`replay/formations.py:81` `SUPPORTED_EVALUATORS = {"s2p2.1"}`.**
   - C1's `EVALUATOR_VERSION` bump (FINAL §1 Files) without this change makes `com.cobalt.replay` refuse every night after deploy, which breaks production (NN#16).
   - The FINAL notes it only as the X9 hub note ("a C1 bump … meets that check"); the file is not in C1's list.
   - `56` adds the version under gate 5 with a read-first rule (STOP if the binding's consumed fields change). The desk confirms this is inside C1.
4. **Two writers of the receipt card entry.** The Fable text cites `evaluate.py:1425-1427` only; `_receipt_card` `:1474-1480` (the refresh path) also writes one. Without the key there, a refreshed card replays without its dot, which is X28's failure mode under B. `56` requires both writers.
5. **B makes every C1 formation score-null**, not only Rubberband's: the suites' single-relation synthetic defs go through the same direction line. Consequences, all by design and all listed in `56` A1:
   - existing tests that pin `with_trend → long`, `setup_ref == "overextension"`, dot lists or non-null scores are re-pointed;
   - the `--candidate` harness (the L52 (d) audit tool, `evaluate_cli.py:20-29`) yields null `card_score`s from now on;
   - a taps file naming `assumed_formation` fails loudly.
6. **RESTARTS: aset expected by import, not by rendering.** The brief said "+ aset only if the files say the dot's rendering needs it". Rendering needs nothing (`radar_panel.py:894-895` already prints `n/a ASSUMED`; a refused tap reaches the card's status line through `post()` `:1092` from `web.py:1368-1369`'s 409). But `aset/web.py:47` imports `cobalt.cards`, so L42's rule derives `com.cobalt.aset`. The build quotes the tool.
7. **X3 and gate 4 move to the deploy** (no replay string in the build; no daily cache in the worktree). The deploy needs `cobalt radar evaluate --replay … --expect-formed` strings (new unless copied from a prior deploy line), and must say whether X3's "zero is allowed" or gate 4's "non-zero on zero" governs acceptance.
8. **Stop-line shape, widened by one word:** `56`'s `experiments:` field is `<n> PASS / <n> FAIL / <n> UNPROVEN` (the brief's line had PASS / UNPROVEN, while its result-line format already lists FAIL). A with-DB baseline is added beside the offline one.
9. **`57` differs from `52` in three places, each from the brief:**
   - Astra is REQUIRED and PREFLIGHT fails closed on METER / HARNESS, naming the retry time.
   - The build prompt is NOT staged (the brief's packet list); houses judge against the FINAL + R40.
   - A 120 KB cap has a stated cut order.

L74: no instruction block was observed inside a tool result this run. This seat committed nothing and sent nothing.

MEMORY: [stated 2026-09-21 · setups-c1 drafter] A version constant has consumers outside its module. Before any prompt bumps one, run `grep -rn <CONSTANT>\|<value>` over `src/`. `EVALUATOR_VERSION`'s bump would have silently broken the nightly replay through `replay/formations.py:81`.

## CONTINUE

None. The run is complete. Next steps are not mine:
- The desk answers E1 and E2, shows him the NEW approvals line, and fills `56`'s launch row (quoting both `.env` strings with his words) and `57`'s row.
- The desk launches `56` after `DEGRADED LINE DEPLOY DONE … deploy-2026-09-21b`, and `57` after `SETUPS C1 BUILT` and after `52` / `54` finish.

## DIGEST FOR THE DESK

- Two prompts drafted, nothing launched:
  - `56-setups-c1-build.md`: Opus 5, no auto mode (L29), `setups/c1-rubberband-0921` in `~/cobalt-wt/setups-c1`, cut after `deploy-2026-09-21b`.
  - `57-setups-c1-check.md`: Sonnet 5, three houses, Astra required and fails closed on METER, staggered after `52` / `54`, date gate R23 / R39.
- **NEW approvals (2):** `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env)` · `Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)`. Reused: 16 + 3 (09-20 R25), `COBALT_ENV=dev uv run pytest *` (09-19 R18); `57`'s 14 + 3 (09-20 R13). The launch row must quote both new strings with his words.
- R40 = B, as built: ONE `assumed_formation` dot, refused in `tap_dot` before any write, `ASSUMED_CONVENTIONS = ("A-01",)` (closure term (3) only), `card_dots` at `evaluate.py:774/:1077/:1383` + `audit_export.py:362`, keys on the receipt entry, `NaReason` + `ASSUMED`. No store, column, migration or panel change.
- Five paths pinned with `file:line`: `store.py:1215-1225`, `evaluate.py:774-800`, `scoring.py:201-235`, `audit_export.py:362-374`, `evaluate.py:1077-1088` (+ create `:1383`).
- `cobalt_dev`: yes, for X8's tap half and X24 (and the with-DB suite); X9, X17 and X27 run offline; X3 moves to the deploy.
- **ASK DESK E1 (needs you):** no committed day on which the FULL Rubberband shape forms (its day-1 avoid covers FTFT). `56` pins it as `AWAITING_A_DAY` (default B). Option A is a DB fixture-cut job first (new strings), then `56` re-issued.
- **ASK DESK E2:** [F-16] (1)'s blind expected values need their own small seat; `57` cannot be blind. Default: owed before deploy.
- E3: the nightly replay would break on the version bump (`replay/formations.py:81`); `56` adds the version under gate 5. Confirm it is inside C1.
- E4: the second receipt writer `_receipt_card` `:1474-1480` must carry the key too; `56` requires it.
- E5: every formation (not only Rubberband's) carries `A-01`, so test re-points and null `--candidate` scores are expected.
- DEPLOY facts:
  - his "approve" (L7 / L61); no migration; RESTARTS expected radar + aset (import rule), the tool decides.
  - X3 / `--expect-formed` / the live-note test run at the deploy from `~/cobalt`, with new strings.
  - TUE only as ONE stacked deploy with `53` (L43, L68), otherwise WED. No shared source file.
- Stop line of `56`: `SETUPS C1 BUILT … | rubberband forms …: proven on the relation path; full shape UNPROVEN — …` is the expected honest value under default B.

SETUPS C1 PROMPTS DRAFTED · prompts: 2 · builder seat: Opus 5 · needs cobalt_dev: yes · new rule strings: 2 · READING: 38 · ESCALATE: 9
