# ROUTING TRIBUNAL — PROMPT DRAFT REPORT (2026-09-22)

Seat `routing-tribunal-draft-0922` · `claude-opus-5-5` · prompt `prompts/2026-09-22/62-draft-routing-tribunal.md` · started 19:36 ET, prompts written 19:41–19:47, report 19:48 (times from `date`, L48).

## §0 Headline

- Drafted, not launched: `63-routing-tribunal.md` (Sonnet hub; Grok + Gemini; Astra METER), `64-routing-tribunal-fable-seat.md` (Opus 5.5 in the Anthropic seat by R109; blind) and `65-routing-tribunal-derive.md` (derive on Opus 5.5 by R109; drafted FILLED, no placeholders).
- Shapes are copied from `59` / `60` / `61`. The launch-line rule strings are byte-identical to theirs (proof below). NEW strings: 0.
- 20 questions: T1–T12 plus (a)–(h), each carrying a `SELF` / `EVIDENCE` line (L26). Packet ≈ 142 KB before the cuts, ≈ 118 KB after. The mandatory part is ≈ 93 KB.
- ESCALATE: 6. The big three: Astra has not ruled on its own seats; grok/agy approval ends 2026-09-23 23:59 ET; one Grok/Gemini hub at a time, so `59` and `63` cannot overlap.

## DIGEST FOR THE DESK

- **`63`**: Sonnet 5 hub `routing-tribunal-0922`, cwd `~/cobalt-wt/agy-trial`. Launch line matches `59` except the path and the remote-control name.
  - **Authorization:** 09-20 R13 and R23; 09-21 R46; 09-22 R4 (`Laws are all mine`), R13, R30, R36, R76, R81 (`ROUTING TRIBUNAL RUNS THIS WEEK`) and R109 (all four literals). Also checks that the proposal and its stop line are committed, and that a committed launch row names `63`.
  - **Date gate (from `59`):** 09-22 / 09-23 only, on R30. On 09-24 or later → `FAILED: authorization expired …`. R105 covers only `53`–`57`.
  - **Windows (from `59`):** refuses 19:25–20:45 ET and at or after 23:20 ET.
  - **Stagger (checks `53`–`57`, `28`, `32` and `59`):** refuses if the voice hub `59`'s report exists without a stop line.
  - **Run:** Codex probe (METER expected → proceed on three). Stages `scratch/tribunal-bars-0920/routing-tribunal/r1/`. Runs Grok and Gemini on a 20-minute clock.
  - **Collate:** file-checks both houses and then the Anthropic seat's claims. Adds a `## Self-assignments (L26)` table: every `SELF: yes` row, its evidence checked, UNMEASURED counted, and any self-assignment a house did not mark counted as `UNMARKED SELF`.
  - **ESCALATE always carries the ASTRA line.** Report `reports/routing-tribunal-2026-09-22.md`. Stop line `ROUTING TRIBUNAL R1 DONE · … · self-assignments unmeasured: <n> · …`.
- **`64`**: `claude-opus-5-5` in the Anthropic seat by R109, `routing-tribunal-fable-0922`.
  - First line `FABLE ROW: R109`. Its gate greps R109 for `ROUTING-PROPOSAL-2026-09-22.md` · `Fable seat: yes` · `seat model: claude-opus-5-5` · `derive seat: claude-opus-5-5`, and checks the session's model against the row.
  - Blind to the houses' folder and to `63`'s report.
  - A CONFLICT OF INTEREST block binds it: the proposal is its own house's work, and a ruling of his counts as `RULED`, never as a measurement. Its self-attack greps are clause names and model ids.
  - Writes ONE file, `reports/routing-tribunal-fable-r1-2026-09-22.md`. Its verdict counts sum to 20. Date gate 09-22 / 09-23.
- **`65`**: the derive, `DERIVE ROW: R109`, `--model claude-opus-5-5`, no placeholder (the placeholder grep returns 0).
  - **Gates:** a new "his later word wins" gate, because R109 says "for now". Refuses unless both round-1 stop lines are committed.
  - **Filters:** a wording that DOES NOT HOLD or was WITHDRAWN is never folded. An UNMEASURED self-assignment is never folded; it becomes a `## Re-test rows` entry (proposal §5).
  - **Splits and rulings:** a split on law text goes to `## FOR DEJAN` as an A/B, never a count (L39). His rulings (R81, R4, R13, R46/R49, the per-case seats, L27's ceiling) and D1–D3 are never re-opened.
  - **Writes:**
    - `30 - Design/ROUTING-v2-2026-09-22.md`: each frozen entry's current text beside the proposed text, the seat table, a clause trace and OPEN items.
    - `reports/routing-tribunal-derive-2026-09-22.md`: fold table, NEEDS ROUND 2, OWNER ITEMS, FOR DEJAN and `## ASTRA READ OWED`.
  - Stop line `ROUTING DERIVED v2 · …`.
- **LAUNCH ORDER:**
  1. Commit the three prompts and this report. R109 is already committed (`75b2aa5`).
  2. Write and commit two launch rows. The row for `63` must name `63-routing-tribunal.md` and say `<nn> is not running` for each of 53–57, 28, 32 and 59 that has no report. The second row is for `64`.
  3. Launch `63` and `64` side by side. `59` must have its stop line first, or its launch row must say `59 is not running`.
  4. When both stop lines are committed, launch `65`. No fill is needed.
  5. v2 → Astra's read on Sat 09-26 → his ruling, entry by entry (R4) → the desk folds LAWS.md (L58).
- **EARLIEST WINDOW:** tonight at 20:45 ET, but only once `59` (voice) has its stop line or has not started. `59` also queues at 20:45, and only one Grok/Gemini hub runs at a time. Realistic slots:
  - tonight after `59` finishes, if `63` starts before 23:20 ET;
  - 2026-09-23 before 19:25 ET, or between 20:45 and 23:20 ET.
- `64` does not depend on the grok/agy window, but its date gate is 09-22 / 09-23.

## PACKET

Sources staged by `63` §1. Whole files are measured; excerpts were measured with `awk` over the ranges; headers are estimated.

| Part | Source | Status | Size |
|---|---|---|---|
| 00-READING-ORDER.md | written by the hub | MANDATORY | ≈ 3 KB (est.) |
| 01-QUESTIONS.md | `63`'s verbatim paragraph + file list | MANDATORY | ≈ 14 KB (est.) |
| 02-greps.txt | 18 pre-computed commands (`63` §1) | MANDATORY (search) | ≈ 10–14 KB (est.; the model-call grep is 8 lines, the `--model` grep ≈ 15 lines at drafting) |
| 10-PROPOSAL.md | `30 - Design/ROUTING-PROPOSAL-2026-09-22.md` whole | MANDATORY | 24,950 B, 245 lines, 0 trailing-ws |
| 11-propose-report.md | `reports/routing-propose-2026-09-22.md` whole | MANDATORY | 3,802 B, 40 lines, 0 trailing-ws |
| 12-rulings.md | `cto-2026-09-22.md` header + R4, R13, R36, R76, R81, R109; `cto-2026-09-21.md` R46 | MANDATORY | ≈ 7.5 KB (rows 6,642 B) |
| 13-rulings-cited.md | R30, R32, R73, R74; 09-21 R49 | OPEN (cut iv) | ≈ 5.2 KB (rows 4,741 B) |
| 14-laws-routing-cluster.md | LAWS.md :17, :47–49, :124–154, :168–174, :278–281 | MANDATORY | ≈ 9 KB (8,620 B) |
| 15-laws-history.excerpt.md | LAWS-HISTORY :27–32, :48–72 | MANDATORY | ≈ 4.3 KB (4,112 B) |
| 16-seats.excerpt.md | MODELS.md whole + `cobalt-houses.md` :19, :23, :51–52, :55, :59–60, :65–68 | MANDATORY | ≈ 9.5 KB (1,812 + 7,297 B) |
| 17-ledger-core.excerpt.md | LEDGER :1323–1326, :900–912, :1142–1143 | MANDATORY | ≈ 6.3 KB (4,003 + 1,103 + 923 B) |
| 18-ledger-cited.excerpt.md | LEDGER :21–30, :615–632, :873–880, :1120, :1175–1177, :1185 | OPEN (cut iii) | ≈ 9.8 KB |
| 20-evidence.excerpt.md | `11-panel-order-deploy.md` :1 · `seat_usage.yaml` :44–83 · `seat-usage.md` :22–49 · TRIAGE :43, :54, :66, :124–125 · laws-audit :264–284, :380–399, :477–491 | OPEN (cut ii) | ≈ 18.5 KB (3,069 + ≈2,200 + 2,337 + ≈800 + 4,580 + 3,683 + 1,653 B) |
| 27-laws-excerpt.md | L1, L3, L10, L17, L31, L39, L47, L62, L63, L67, L70, L72 | OPEN (cut i) | ≈ 16 KB |

- **Total:** ≈ 142 KB before the cuts. Cuts (i)–(iv) remove ≈ 24 KB, leaving ≈ 118 KB. `63` stages it anyway if it lands over 120 KB, and names it under ESCALATE.
- **MANDATORY:** ≈ 93 KB.
- **Tokens per house (÷4):** mandatory ≈ 23–24k; whole packet after the cuts ≈ 29–30k.
- **Anthropic seat `64` read set:** ≈ 60–75k tokens, peak ≈ 80–95k.
- **Derive `65`:** peak ≈ 120–150k.
- **Not staged:** his notes, `Rules.md`, meter screenshots, secrets, the rest of the memory folder, desk reports whole, the ledger whole, ADR-0008 whole, and any production row.
- **Staging facts the hub must honour:**
  - `seat-usage.md` was dirty in `~/cobalt` at drafting; `63` has the hub record its last commit.
  - `day-open-2026-09-22.md` is untracked; `63` has the hub run `git log` on it and record the result.
  - The ledger's repo copy and its vault copy are both 291,377 B.

## RULE PROOF

Method: one `grep -c -F -e` on the WHOLE contiguous launch segment. A count of 1 in both files proves every string in the segment is present byte-identical.

**Segment A.** This is `--allowedTools "Bash(grok *)" … "Bash(date*)" --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir …×3`: the 14 allow strings, the 3 denies and the add-dir triplet, in order.

| File | Segment A |
|---|---|
| `59-voice-tribunal.md` | 1 |
| `63-routing-tribunal.md` | 1 |
| `2026-09-20/08-bars-chunk-e-check.md` (the approved line) | 1 |

**Segment B.** This is the 7 read-only allows, the 3 denies and the add-dir triplet.

| File | Segment B |
|---|---|
| `60-voice-tribunal-fable-seat.md` | 1 |
| `64-routing-tribunal-fable-seat.md` | 1 |
| `61-voice-tribunal-derive.md` | 1 |
| `65-routing-tribunal-derive.md` | 1 |
| `2026-09-21/22-draft-setups-tribunal.md` (the approved line) | 1 |
| `62-draft-routing-tribunal.md` (this seat's own line) | 1 |

Expected differences only, read with `grep -o` on the launch lines:

| Prompt | Prompt path | `--remote-control` | `--model` |
|---|---|---|---|
| `63` | `63-routing-tribunal.md` | `routing-tribunal-0922` | `claude-sonnet-5` (= `59`) |
| `64` | `64-routing-tribunal-fable-seat.md` | `routing-tribunal-fable-0922` | `claude-opus-5-5` (R109; = `60`) |
| `65` | `65-routing-tribunal-derive.md` | `routing-tribunal-derive-0922` | `claude-opus-5-5` (R109; = `61` after its R108 fill) |

- `--permission-mode auto` and the cwd `~/cobalt-wt/agy-trial` match `59` / `60` / `61`.
- In `65`, `grep -c -E "__DERIVE_(ROW|MODEL)__"` = 0.
- The `--model claude-opus-5` / `gemini-3.1-pro-high` / `acceptEdits` hits in `63` lines 5, 7 and 17 are prose (the R46 refusal clause, the gemini spelling reference, and the `02-greps` search patterns). None is a launch string, as in `59`.

**NEW strings:** none (0).

## READING

- **Prompts:**
  - The prompt `62`.
  - Templates `58`, `59` (whole), `60`, `61` (as filled by R108).
  - The voice draft report `voice-tribunal-draft-2026-09-22.md`.
- **Laws and design:**
  - `LAWS.md` in full (442 lines, 82,174 B). `LAWS-HISTORY.md` headings, with :27–72 measured.
  - The proposal (whole) and its report (whole).
- **Desk reports:**
  - `cto-2026-09-22.md` rows R4, R13, R30, R32, R36, R73, R74, R76, R81, R105, R106, R108 and R109, plus header lines :1–12.
  - `cto-2026-09-21.md` rows R46 and R49.
  - Confirmed committed: R109 (`75b2aa5`), the proposal and its stop line (`1bcc1a8`).
- **Seats and launch:**
  - `areas/cobalt-houses.md` (grep).
  - `docs/50 - Roles/MODELS.md`.
  - `prompts/UNATTENDED-LAUNCH.md` (first 6,000 B, §1–§3). The path `62` gives, `docs/40 - DevDocs/UNATTENDED-LAUNCH.md`, does not exist. The standard lives under `prompts/`.
- **Ledger:** grep and `awk` over the cited lines; :1318–1334 previewed.
- **Evidence files:**
  - `seat-usage.md` headings and Terra / Haiku rows.
  - `seat_usage.yaml` role hints.
  - Day-open `SEAT VERDICT` lines.
  - TRIAGE :43, :54, :66, :124–125.
  - `laws-audit-2026-09-20.md` headings.
  - The `--model` values on 11 prompts.
  - The `WHY NOT OPUS` prompt list.
- **Code and config searches:**
  - The `src/cobalt` model-call grep: 8 hits, no model call.
  - `configs/` routing grep.
  - The decisions-folder bake-off grep: no output.
  - The reports listing (for the stagger).
- **Facts seen while drafting, left to the tribunal (not ruled here):**
  - `seat_usage.yaml` :78–83 names `claude-opus-5` and `grok-4.6-build`. Proposal §2 names `claude-opus-5-5` and `grok-4.7-build`. This is question (a)'s to settle.
  - The ledger line L49 cites as "reaffirmed LEDGER:1313" reads as an archiver fact at :1313. Not cited by the proposal; not staged.
- **Drafting choices beyond `62`'s letter:**
  - (i) The closing line is `TRIBUNAL R1: ADOPT / ADOPT AFTER / DO NOT ADOPT` instead of BUILD, because the output is law text forwarded to him.
  - (ii) `63` adds a `## Self-assignments (L26)` section and an `UNMARKED SELF` count for self-assignments a house did not mark.
  - (iii) `65` adds a gate that fails if a later row of his changes the derive seat, because R109 says "for now".
  - (iv) `65` derives law text as "current beside proposed" per frozen entry, plus a clause trace, and writes nothing to LAWS.md (L58).
  - (v) Ledger excerpts are cut to the lines the proposal cites in its text; the wider §8 "sources read" ranges were not staged, to hold the 120 KB target.
  - (vi) R49 of 09-21 is staged OPEN-AS-NEEDED, for question (g).

## ESCALATE

1. **ASTRA HAS NOT RULED on a routing design that assigns its own seats.** Seat-map rows 9–12 are Astra, Sol and Terra. R13 puts the Codex meter out until Sat 09-26 06:47 ET. The desk should bring Astra's read of the derived v2 to him BEFORE his ruling of the law text. `63`'s ESCALATE carries this line always; `65` writes `## ASTRA READ OWED`.
2. **grok/agy approval for this tribunal ends 2026-09-23 23:59 ET (R30).** R105's extension to 10-07 is scoped to `53`–`57`. If `63`, or a round 2, slips to 09-24 or later, it FAILs at row 1. The desk needs his extension row naming this tribunal before 09-24, then a re-issue of `63` (L19).
3. **One Grok/Gemini hub at a time:**
   - `63` refuses while `59` (voice) runs without a stop line. Both want the 20:45–23:20 ET slot.
   - The launch row must name `63-routing-tribunal.md` and say `<nn> is not running` for each of 53–57, 28, 32 and 59 that has no report. At drafting, none of `59`, `28`, `32` or the `drc-d<k>-check-*` reports existed.
   - Missing literal → `FAILED PREFLIGHT`.
4. **Packet at the target:** ≈ 118 KB after all four cuts (estimated). It may land over 120 KB; `63` stages it anyway and names it in its ESCALATE.
5. **R109 is "for now":**
   - `64`'s date gate is 09-22 / 09-23; later needs a re-issue.
   - `65` fails if a later row of his changes the derive seat for this proposal.
   - If he ends R109 before `64` launches, `64` and `65` are re-issued (L19).
6. **The `62` prompt names a path that does not exist.** It gives `docs/40 - DevDocs/UNATTENDED-LAUNCH.md`; the standard is at `docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md`. Read there; nothing in `63`–`65` cites the wrong path.

## CONTINUE

- next: none. All four files are written. The desk commits them and follows LAUNCH ORDER above.
- L74: the session's context carried an attribution block and a file-send tool mention after a tool result. Not followed; this seat commits nothing and sends nothing.

ROUTING TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: METER — proceed on three · questions: 20 · packet: 118 KB · new rule strings: 0 · ESCALATE: 6
