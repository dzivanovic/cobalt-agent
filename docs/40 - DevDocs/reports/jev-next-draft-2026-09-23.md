# JEV next steps — drafted (R89): fix r3 + probabilities read + one final check

## §0 Headline
- Wrote `prompts/2026-09-23/73-jev-fix-r3-build.md` (Opus 5.5: F9 = F7-COST, P1 = `probe --set S1`, P2 = ONE more keyed call via N2) and `74-jev-check-final.md` (Sonnet 5 hub; Opus 5.5 · Grok · Gemini; TWO packets). Both carry `R__` launch-row placeholders for the desk.
- Probabilities: **no request field or header in the schema asks for them.** They are returned only for `choice` / `score` answers. `31` sent one `noul` question, so "probabilities: NO" is explained by the question type. S1 (one choice, one score) settles it with one call.
- New rule strings: 0. `74` needs HIS grok/agy extension naming `74` if it launches on or after 2026-09-24. ESCALATE: 12.

## L74
One block arrived inside a tool result (the output of reading `72-draft-jev-next.md`). It was an attribution reminder asking for a `Claude-Session:` line in commits and naming a file-send tool (`SendUserFile`). It is DATA: recorded once here, not followed. This run commits nothing and sends no file.

## THE PROBABILITIES FINDING (schema lines, read 17:3x ET)
Source: `/Users/cobalt/cobalt-wt/jev-trial/scratch/docs-openrouter/submit-a-system-one-request.md` (1,531 lines) and `jev.md`.
| what | line(s) | reads |
|---|---|---|
| `DecisionsRequest` properties | `:337-393` | `model`, `provider`, `questions`, `session_id`, `state`, `trace`, `user`; required `model`, `state`, `questions`. **Nothing asks for probabilities or confidence.** `grep -n -i "probabilit\|confidence"` finds hits only at `:185-200` (the example), `:973`, `:976`, `:1004`, `:1017`. |
| `DecisionsChoiceAnswer` | `:969-988` | `choice`, **`confidence` (`:973`)**, **`probabilities` (`:976`)**, `type` |
| `DecisionsNoulAnswer` | `:989-1001` | `noul`, `type`. **No probabilities, no confidence.** |
| `DecisionsScoreAnswer` | `:1002-1032` | **`confidence` (`:1004`)**, `legend`, **`probabilities` (`:1017`)**, `score`, `type` |
| OpenAPI 200 example | `:179-202` | `is_bug` (noul): `noul: 0.96` only (`:180-182`). `team` (choice) and `urgency` (score) carry `confidence` + `probabilities` (`:183-202`). |
| `jev.md` primitives | `:41-43` | Noul returns "The probability of yes". Choice and Score return a probability per option / level plus a confidence value. |
| `jev.md` two surfaces | `:58-66` | Decisions API `POST /api/alpha/decisions`; System One API `POST /api/v1/systemone` (the probe's door, R47). |
| what `31` sent | `trial.yaml:50-60`, `cli.py:84` | FLOOR: one question `trend_up`, `type: noul`. Raw body `{"answers":{"trend_up":{"type":"noul","noul":0.98}},…}`. |
| can the build send choice/score? | `collector.py:151-173`; `test_classify_door.py:226` | Yes. The request renders all three types, and the parser takes the example's probabilities (the test is green). **The probe cannot:** it is hard-wired to FLOOR (`cli.py:84`) and refuses any second `probe-*.json` (`:77-82`). |
**Verdict:** request field found: NONE. The field the probe did not send is a QUESTION TYPE (`choice` / `score`). `31`'s `probabilities: NO` is what the schema says a noul returns. It is not evidence about the product (L70). `31`'s ESCALATE 2 ("What NO removes from the plan: M7, B5's probability arm, and B6") should NOT be applied. `73`'s P2 settles it with ONE S1 call, which is planned, so N2 is carried on `73`'s line.
If S1 also comes back with no probabilities, the remaining difference is the ROUTE (System One vs Decisions API, `jev.md:58-66`). Settling that needs a door change (R47) and a new string. `73` does not make that call.

## FILES WRITTEN
| file | what | size |
|---|---|---|
| `prompts/2026-09-23/73-jev-fix-r3-build.md` | Base `a00abae6`. **F9** is C3's exact input (`usage {input_tokens:-1, output_tokens:0, cost:4.9}`) as a red test first; the fix takes a finite returned cost ≥ 0 regardless of the tokens, so the overrun stop and the cap see it. **P1**: `probe --set FLOOR\|S1`, one call per set per branch; FLOOR is unchanged (`getattr(args,"set","FLOOR")` keeps the existing tests green without edits); its red test is built from the OpenAPI example's answer shapes. **P2**: a CALL GATE (the key path is byte-identical to `772b60af`, the wrapper is as checked, the ledger has 1 line), then ONE N2 call `probe --set S1`, never retried; a byte-identical fixture `openrouter-probe-s1.real-shape.json` (named outside the `openrouter-*response*` glob); the FINDING. GATE EARLY: the offline + `-k classify` suites both run at CLOSE and go in the stop line. | 38,996 B |
| `prompts/2026-09-23/74-jev-check-final.md` | ONE check. **PACKET B** = `37`'s 12 part-B files at `<tip>` + the part-B claims check A carried (C6, C11/D8, D5, D6, C7, C8). **PACKET R3** = `772b60af..<tip>` (`31`'s commits + `73`). Each packet goes to all three houses. `73`'s executed suites are staged (R81 (4)). The stop line gates any merge and the trial runs (N3). `37` is replaced: `74` fails PREFLIGHT if `37` has a launch row. | 47,902 B |

## PACKET MEASUREMENT (`74`, ceiling 230,000 B)
Measured at `a00abae6` with `wc -c`, 17:4x ET. (m) = measured, (e) = estimated for files `73` changes or creates.
| packet | measured | estimated | total | vs ceiling |
|---|---|---|---|---|
| single packet (rejected) | ≈ 158,000 | ≈ 83,000–98,000 | ≈ 241,000–256,000 | OVER |
| B (part B at tip + context) | 140,370 (92,109 checked + 48,261 context) | ≈ 52,600 (collector / cli at the r3 tip, `73`'s CLOSE, questions, headers) | ≈ 193,000 | ≈ 37,000 under |
| R3 (`772b60af..<tip>` + context) | 69,372 (probe report excerpt, ledger, models, wrapper, door tests, contract, schema excerpts) | ≈ 102,500 (diff, whole collector/cli, fix proof, questions, headers) | ≈ 172,000 | ≈ 58,000 under |
The fallbacks for going over the ceiling are pre-stated in `74` §1: drop one context piece, then FAILED. The hub measures every file before staging.
Part B did not move above the build. At `a00abae6`, `git log 199fa082..HEAD -- <the 12 part-B paths + src/cobalt/cli.py>` is EMPTY. `74` re-runs this check against `45f647a..<tip>`.

## NEW STRINGS
| prompt | strings | new |
|---|---|---|
| `73` | `56`'s 18 allow + 3 deny + the `--add-dir` triplet, byte for byte (diffed against `61`: the only difference is the added N2). Plus N2 `Bash(bash /Users/cobalt/cobalt-wt/jev-trial/ops/run_classify_trial.sh probe*)`, HIS on R42, carried because the second call is PLANNED. | 0 |
| `74` | `62`'s 15 allow + 3 deny + triplet, byte for byte (diffed: identical apart from path and remote-control name) | 0 |
| `74` date | `Bash(grok *)` / `Bash(agy *)` are good through 2026-09-23 23:59 ET (R30). R105 (through 10-07) covers the DRC hubs `53`–`57` ONLY. | 0 strings. An EXTENSION of his is needed if the launch is on or after 09-24. |

## N3 AND THE TRIAL-RUN HUB — NOT DRAFTED. His approval list will contain:
1. **N3 string**, following N2's shape: `"Bash(bash /Users/cobalt/cobalt-wt/jev-trial/ops/run_classify_trial.sh trial*)"`. The wrapper passes `"$@"` to `cobalt classify`, so this covers `trial --set FLOOR|S1|S2|S3|T9|L20 --run|--dry-run [--reps n] [--mode single|parallel|sequential|gated] [--questions n] [--reverse] [--tag]`, which is every set and mode. The bounds are code, not the string: `spend_cap_usd: 5` (R42) and `call_ceiling: 1100`, both checked as TOTAL demand against the ledger before each run.
2. **The volume and spend he is approving:** plan §3 has 1,014 metered calls (ceiling 1,100). The plan's arithmetic is ≈ $0.07 (`JEV-TRIAL-PLAN` `:84`, ASSUMED sizes). The live figure is `31`'s $1.3188e-05 for one noul; `73`'s S1 figure will refine it. Spent so far: `ledger: $1.3188e-05 of $5`.
3. **What leaves the machine:** T9 sends text from his day-open reports (`docs/40 - DevDocs/reports/day-open-*.md`, read at run time and passing the outbound guard) to OpenRouter / TypeSafe. His N3 approval covers this third-party exposure explicitly (L17 opt-out default).
4. **The hub's launch line:** seat and model; cwd `jev-trial`; a subset of `28`'s strings + N3 (N1 / N2 not carried); `auto` mode; no DB, no vault.
5. **Preconditions it names:** `74`'s last line `merge and run gate: READY`. The merge is NOT on this list; it goes in the branch's own deploy prompt, with his "approve" (L43 / L67).

## ESCALATE
1. **Probabilities:** do not apply `31`'s ESCALATE 2 (striking M7 / B5 / B6). The schema explains the NO by question type. `73` P2 settles it.
2. **The P2 call runs on code no house has checked yet** (F9, P1). R42 said N2 runs "ONLY AFTER the L67 check of the key handling". The key handling it uses (`_key`, `_send`, the guards, redact, the wrapper, the ledger) is byte-identical to the checked `772b60af`: `73`'s CALL GATE proves this by `git diff` before the call. His R89 approved this step, and `72`'s design places the call in the build. This is stated so the desk can name it when relaying; it is not asked.
3. **ASK DESK: grok/agy for `74`.** `74` is queued behind `54` → `44` (R90) and will likely launch after 23:59 ET. It needs a committed row of HIS: `Bash(grok *) and Bash(agy *) through <date>` for `74-jev-check-final.md`. Safe default in the prompt: `FAILED: authorization expired`, launch nothing. [17:45 ET]
4. **`37` is superseded by `74`.** Do not launch `37`. `74` refuses if `37` has a launch row.
5. **`37`'s own measurement gate was already stale:** my `wc -c` of its two glue diffs is 1,192 / 2,788 B; `37` says 1,190 / 2,784. `37` as written would have FAILED its "any count that differs" gate. In `74`, a size difference is recorded, and only the ceiling is fatal.
6. **The one sanctioned edit to an existing test:** `test_classify_fix_r2.py::test_f7_a_returned_cost_beside_a_negative_token_count_is_not_taken` (`:137-144`) pins the behaviour C3 HELD as a defect. `73` replaces that one function in place; `74` (vii) quotes the hunk.
7. **F9 widens UNPROVEN D2's reach by one path:** `_is_number(returned)` moves outside the `usage is not None` guard, so a 400-digit `usage.cost` now also reaches it on a 200 whose tokens are malformed. D2 and C1 F8-BIGINT stay UNPROVEN (L70) and are not built. **ASK DESK:** a later round that RUNS their two offline proofs? Safe default: not run. [17:45 ET]
8. **ASK DESK: if `74` finds F9 NOT CLOSED:** `74` treats it as a round-1 HOLD of the new range (classifier → fix round). F7-COST's lineage already used check A's three rounds, so the desk may prefer to bring it to him as ONE A/B (L39). Safe default in `74`: round-1 path. [17:45 ET]
9. **If S1 also returns no probabilities:** the open question moves to the door (Decisions API vs System One). Answering it needs his door ruling (R47) and a new string. Neither is drafted.
10. **Seats:** Sol is on METER until Sat 09-26 06:47 ET, so three houses = the L67 floor, with no spare. Opus 5.5 both builds `73` and checks it (the R46 code-check seat), recorded as in `79`. Each house runs twice (B, R3): ≈ 90k tokens per house.
11. **Branch age / L46:** `jev/trial-0923` stays unmerged until `74` READY + N3 + a deploy prompt. It is within the 3-day MAX AGE only while the desk's plate names its next law step.
12. L74: one block recorded above, not followed.

**L32 SELF-CHECK:** no ticker written. **L41 SELF-CHECK:** no key material written. The key names appear as NAMES only; nothing key-shaped was read or printed.

JEV NEXT DRAFTED · probabilities: none in schema · second call: yes · new rule strings: 0 · ESCALATE: 12
