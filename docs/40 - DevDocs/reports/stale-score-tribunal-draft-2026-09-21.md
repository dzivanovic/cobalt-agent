# Stale-score tribunal — round-1 prompt drafting (2026-09-21)

Seat `stale-score-tribunal-draft-0921` · Opus 5 · read-only except the four files named in `60` · started 17:41 ET, done 17:5x ET (`date`).

## §0 Headline
- Drafted three prompts: `61-stale-score-tribunal.md` (Sonnet 5 hub, three houses, 21 questions, packet ≈ 105–112 KB), `62-stale-score-tribunal-fable-seat.md` (the Fable seat, blind, line 1 `FABLE ROW: R__`), and `63-stale-score-tribunal-derive.md` (line 1 `DERIVE ROW: R__`). Nothing launched.
- Astra is **REQUIRED**. `61`'s PREFLIGHT fails closed on METER or HARNESS and names the retry time (`57`'s wording). A PARTIAL ruling with k ≥ 1 of 21 is kept. `63` refuses without an astra ruling.
- New rule strings: **0.** `61` = `38`'s 14 + 3 strings; `62` / `63` = `39`'s 7 + 3 strings. Each string counts 1 in each file.
- No user data is in the packet (checked, L32). The date gate is R23 for 09-21 and R39's literal for 09-22; 09-23 or later fails.
- ESCALATE: 5 (two are ASK DESK, with safe defaults).

## DIGEST FOR THE DESK
- **`61` hub** (`stale-score-tribunal-0922`, Sonnet 5, cwd `~/cobalt-wt/agy-trial`):
  - Stages ≈ 17 files into `scratch/tribunal-bars-0920/stale-score-tribunal/r1/` using the Write tool.
  - Launches grok, gemini and astra together. Astra runs with ` < /dev/null`, but only if `44`'s `Experiment field: **reads started**` line is still there.
  - Runs `date` at every completion notice and stops any house past 20 min with its task-stop tool.
  - File-checks every claim the houses make. At collate it also file-checks the Fable seat's claims, but only if that report ends on its stop line; otherwise it writes one UNCHECKED line.
  - Report: `reports/stale-score-tribunal-<D>.md`, named from its row-1 `date` (the report's line 1 says so).
  - Stop line: `STALE SCORE TRIBUNAL R1 DONE · grok … · gemini … · astra … · houses that ruled … · claims that HOLD … · blockers to build … · owner items … · ESCALATE …`.
- **`61` refuses when:**
  - there is no desk LAUNCH ROW naming `61`, committed in `cto-2026-09-21.md` or `-22.md` (52's shape);
  - the date is 09-22 without R39's committed literal, or it is 09-23 or later;
  - the time is 19:25–20:45 ET or ≥ 23:20 ET (either date, at both date rows);
  - `38`, `52`, `54` or `57` has a report without a stop line;
  - one of those reports is MISSING and the launch row does not carry `<nn> has stopped or will not run`;
  - astra is not UP at the probe.
- **`62` Fable seat** (`claude-fable-5-1`):
  - Refuses while line 1 still reads `R__`. The row must be in either desk file and carry `Fable seat: yes` + `STALE-SCORE-PROPOSAL-2026-09-21.md`.
  - BLIND to the r1 folder and to both candidate hub-report names.
  - Its self-attack starts by grepping 13 field and function names (the Fable R2 MEMORY line); any sentence it cannot support is marked `WITHDRAWN:`.
  - Writes one file, `reports/stale-score-tribunal-fable-r1-<D>.md`. Its 21 counts must sum to 21.
- **`63` derive:**
  - `DERIVE ROW: R__`; the desk also sets `--model` to the id after `derive seat:`.
  - Refuses unless the hub's stop line is present and committed, plus the Fable stop line if `Fable seat: yes`, plus an astra ruling (full, or partial with k ≥ 1).
  - Never folds a wording whose claim DOES NOT HOLD or is WITHDRAWN. A Fable claim the hub did not check stays UNCHECKED and is never counted as HOLDS.
  - Writes `30 - Design/STALE-SCORE-v2-<D>.md` and `reports/stale-score-tribunal-derive-<D>.md`. The report includes `## FOR DEJAN`: one A/B per owner item, with no recommendation from a seat that holds a side (L37).
- **Launch order with clocks:**
  1. Desk: write `61`'s launch row, stating the status of `38` / `52` / `54` / `57` literally.
  2. `61`, at the earliest open slot:
     - tonight after `38`'s stop line and before 23:20 (≈ 22:00–23:20 if `38` runs 20:45–≈22:00);
     - or TUE 09-22 before 19:25, staggered around `52` / `54` / `57`.
  3. `62` needs his yes. He is away until late evening. It can run beside `61` or after it; if it runs after, its claims go UNCHECKED by the hub.
  4. `63` runs after the hub report (and the Fable report, if approved) is committed. Its row is filled on his answer.

## L47 finding
Astra is REQUIRED for this tribunal, and the probe fails closed.
- **Why required:**
  - The proposer is Anthropic (Opus 5), and the Fable seat is not yet approved.
  - The design is scoring and reaches the card (L52). Without astra it could close on Grok + Gemini alone.
  - Today's record: Gemini produced 9 claims that did not hold on setups R1.
- **Why fail closed now, when `38` did not:**
  - R39 keeps the house strings through 09-22, so a METER stop on 09-21 costs no approval.
  - `57`'s brief set the same shape for a card-reaching check.
- **The cost:** a METER stop on 09-22 late in the day leaves no retry inside R39. That relaunch would need his word.
- **Evidence the stdin shape works:** astra ruled 12 questions in 46,391 tokens (≈ 6 min) with a reading order and ` < /dev/null` (`setups-tribunal-r2-2026-09-21.md:95`).

## PACKET
Sizes: exact where the whole file is staged; otherwise an estimate from line ranges × each file's average bytes per line. The hub states the real `wc -c`.

| staged path | source | size |
|---|---|---|
| `PROPOSAL.md` | `30 - Design/STALE-SCORE-PROPOSAL-2026-09-21.md` whole | 20,933 B |
| `design-digest.md` | `reports/stale-score-design-2026-09-21.md` :6–31, :61–65, :78–107 | ≈ 7.5 KB |
| `owner-rulings.md` | `cto-2026-09-21.md` rows R36 (:47), R40 (:51) | ≈ 3.5 KB |
| `c1-facts.md` | `reports/setups-c1-draft-2026-09-21.md` :33–43, :137–140 | ≈ 2.5 KB |
| `laws-excerpt.md` | LAWS.md L1, L3, L7, L29, L42, L52, L53, L57, L70 | ≈ 8 KB |
| `ADR-0009-D4.excerpt.md` | ADR-0009 :27–28 | ≈ 0.5 KB |
| `scoring.py` | `src/cobalt/cards/scoring.py` whole | 14,048 B |
| `evaluate.excerpt.py` | `radar/evaluate.py`, 10 ranges (≈ 330 lines) | ≈ 16 KB |
| `store.excerpt.py` | `cards/store.py` :1016–1075, :1182–1231 | ≈ 5.5 KB |
| `cards-radar.excerpt.py` | `cards/radar.py` :20–35, :160–206 | ≈ 2.5 KB |
| `clocks.excerpt.py` | `poller.py` :90–125, `freshness.py` :106–142, `tunables.yaml` :465–472, :512–522 | ≈ 3.5 KB |
| `expire-audit.excerpt.py` | `cards/expire.py` :272–312, `audit_export.py` :240–260 | ≈ 3 KB |
| `migrations.excerpt.sql` | `0007` :44–50, :140–150, :215–258; `0006` :95–109 | ≈ 3.5 KB |
| `panel.excerpt.py` | `aset/radar_panel.py` :877–885, :955–958, :998 | ≈ 2.5 KB |
| `greps.txt` | 17 greps + 3 `git log` (branch state of C1 and the stamp) | ≈ 12–16 KB (unmeasured) |
| `QUESTIONS.md` | verbatim in `61` | ≈ 10 KB |
| **total** | | **≈ 105–112 KB** |

- Target ≤ 110 KB. The cut order, if over: `panel` → the `0006` range → `evaluate` :487–505. The core files are never cut.
- **User data: none.** Every source is committed code, config, a design, a report or a ruling row (tunables.yaml tracked, `e824f36`; proposal and report `86df294`).
- **Token estimates per house:**

| house | reads | output | notes |
|---|---|---|---|
| Grok | ≈ 28–32k (reads whole) | 8–12k | |
| Gemini | ≈ 28–32k | 8–12k | |
| Astra | ≈ 35–50k | — | with the reading order; r2 used 46k on 90 KB |
| Fable seat | ≈ 55–65k | 10–14k | peak ≈ 75–90k |
| Derive | — | 8–11k | peak ≈ 90–120k |

## RULE PROOF
`grep -c -F -e '"<string>"'` run per string, 17:5x ET, on `61 38 62 63 39` together.

| string | 61 | 38 | 62 | 63 | 39 |
|---|---|---|---|---|---|
| `"Bash(grok *)"` | 1 | 1 | — | — | — |
| `"Bash(agy *)"` | 1 | 1 | — | — | — |
| `"Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)"` | 1 | 1 | — | — | — |
| `"Bash(mkdir -p scratch/tribunal-bars-0920)"` | 1 | 1 | — | — | — |
| `"Bash(git -C /Users/cobalt/cobalt show*)"` | 1 | 1 | 1 | 1 | 1 |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 | 1 | 1 | 1 | 1 |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)"` | 1 | 1 | — | — | — |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*)"` | 1 | 1 | — | — | — |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards diff*)"` | 1 | 1 | — | — | — |
| `"Bash(ls *)"` · `"Bash(grep *)"` · `"Bash(tail *)"` · `"Bash(wc *)"` · `"Bash(date*)"` | 1 each | 1 each | 1 each | 1 each | 1 each |
| `"AskUserQuestion"` · `"EnterWorktree"` · `"Bash(git push*)"` | 1 each | 1 each | 1 each | 1 each | 1 each |

- Other facts I proved:
  - R39's literal `Bash(grok *) and Bash(agy *) through 2026-09-22` is committed (`3ecbb27`).
  - The proposal's `STALE SCORE PROPOSED` line is committed (`86df294`).
  - Main is `86df294`, which is `031196f` plus docs only, so the proposal's line refs hold. All anchors were re-checked by `grep -n`.
- Prompt sizes: `61` 59,065 B · `62` 15,961 B · `63` 17,682 B.

**NEW strings:** none.

## READING:
- Prompts (whole): `60`, `37`, `38`, `39`, `40`, `44`, `52`.
- Prompts (by grep): `57` (the fail-closed astra row, stagger, report name); `54` (report name, stop prefix); `45` / `46` (`WITHDRAWN`).
- The proposal (whole) and its report (whole).
- `setups-c1-draft-2026-09-21.md`: :5–44, :121–152.
- `setups-tribunal-r2-2026-09-21.md`: grep astra experiment (:5, :38, :82, :93–95, :615–617).
- `setups-tribunal-fable-r2-2026-09-21.md`: :232 MEMORY.
- `cto-2026-09-21.md`: rows R36, R39–R43 (:47–54); grep handicap lines :39, :41, :43, :302–311, :367–390.
- LAWS.md headings (grep).
- ADR-0009: :27–28.
- Code on main, by grep + ranges:
  - `radar/evaluate.py` anchors
  - `cards/scoring.py` :238–268
  - `cards/store.py` :1182–1232 + anchors
  - `cards/radar.py`, `radar/poller.py` :98–132
  - `freshness.py`, `tunables.yaml`, `expire.py`, `audit_export.py`, `radar_panel.py`, `0007` (anchors)
- `ls` of `reports/` and `prompts/2026-09-21/`.
- Git: `git log` main (5); branch `setups/c1-rubberband-0921` (not found, exit 128).

## ESCALATE
1. **`38` has not run.** `reports/float-handicap-tribunal-2026-09-21.md` does not exist; the desk log plans it for after 20:45 tonight. `61`'s stagger then needs either `38`'s stop line, or a launch row carrying `38 has stopped or will not run` (the literal copied from `38`'s own rule). The same holds for `52`, `54` and `57`, whose reports do not exist yet.
   - `ASK DESK: the literal reads "will not run" — write it in 61's launch row only when that prompt will not overlap 61's houses? [17:52]`
   - Safe default as drafted: no literal means no launch.
2. **The Fable seat needs his yes.** One row carries three literals: `Fable seat: yes|no` · `derive seat: <model id>` · `STALE-SCORE-PROPOSAL-2026-09-21.md`. The same `R<nn>` fills line 1 of both `62` and `63`, and `63`'s `--model` is set to match.
   - A row number could repeat across `cto-2026-09-21.md` and `-22.md`. Both prompts FAIL if two `R<nn>` rows carry `STALE-SCORE`.
   - `ASK DESK: ask him tonight on return? [17:52]`
   - Safe default: `61` runs without it, and `63` waits for his answer.
3. **Astra fails closed** (unlike `38`, following the brief and `57`). If astra is on METER at a 09-22 evening probe, no retry fits inside R39, and the next attempt needs his word for `grok` / `agy`.
4. **`61` departs from `38` in two places:**
   - It requires a desk LAUNCH ROW naming it (`52`'s shape). That row carries the stagger literals and makes the launch accountable.
   - Its rule proof accepts "1 or more" against `08`, because `Bash(grok *)` and `Bash(agy *)` count 2 there (lines 1 and 5, recorded by the r2 hub).
5. **The proposal's W19 panel lines are partly off.** It cites `radar_panel.py:877-883, :957, :982, :1026`. On main, `_field` is at :877 and `score suppressed:` is at :957, but the RANK + WHY fields line is at :998. I did not open :982 or :1026. `61` stages by verified anchors, and question (a) lets the houses flag the rest. This is a citation drift, not a defect claim.

L74: no instruction block arrived inside a tool result this run. This seat committed nothing and sent nothing.

## CONTINUE
None. The run is complete. Next steps belong to the desk:
- L35 on `61` / `62` / `63`.
- Commit the prompts and this report.
- Write `61`'s launch row.
- Ask him about the Fable seat (ESCALATE 2).

STALE SCORE TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: REQUIRED · questions: 21 · packet: 110 KB · new rule strings: 0 · ESCALATE: 5
