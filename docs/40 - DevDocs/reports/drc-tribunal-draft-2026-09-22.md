# drc-tribunal-draft-2026-09-22 — DRC tribunal round-1 prompts (seat `drc-tribunal-draft-0922`, Opus 5.5)

## §0 Headline
- DRAFTED (not launched) `40-drc-tribunal.md` (Sonnet 5 hub, Grok + Gemini, astra probe carried → METER, 21 items), `41-drc-tribunal-fable-seat.md` (Fable 5.1 seat, blind, `FABLE ROW: R73`), `42-drc-tribunal-derive.md` (Fable 5.1 derive, `DERIVE ROW: R73`) under `prompts/2026-09-22/`. Written 16:06–16:21 ET.
- Rule proof: every launch string is byte-identical to its template (`40` vs `73`, `41` vs `74`, `42` vs `75`). Only three things differ: the prompt path, the remote-control name and `--model claude-fable-5-1` on `41` / `42` (R73). **NEW strings: 0.**
- Packet ≈ 135–145 KB after the cut order (MANDATORY core ≈ 125–130 KB); the hub measures it and ESCALATEs if it is still over 140 KB after cut (v). L32: no value, rule sentence, ticker, price or P&L of his in any of the four files (scan = 0).
- ESCALATE: 6. No ASK DESK.

## DIGEST FOR THE DESK
What each prompt does:
- **`40` hub `drc-tribunal-0922`** (Sonnet 5, cwd `~/cobalt-wt/agy-trial`, `73`'s 14 + 3 strings). Gates:
  - AUTHORIZATION: 09-20 R13 / R23, 09-21 R46, and 09-22 R13 (`without Astra`), R60, R66, R72, R73 (all three literals). R73, the proposal, §13 and the proposer's stop line must be committed. It also needs a committed launch row naming `40-drc-tribunal.md`.
  - DATE + EXTENSION GATE (R30): runs on 09-22 or 09-23 only. From 09-24 it FAILS.
  - WINDOWS: refuses 19:25–20:45 ET and from 23:20 ET.
  - STAGGER: waits on `16`, `28` and `32`. None of their reports exists at drafting, so the launch row must say `16 is not running` · `28 is not running` · `32 is not running`, each on a line that also names `40-drc-tribunal.md`.
  - Codex probe carried → `astra: METER — proceed on three`.
- **`40` then** stages the packet into `scratch/tribunal-bars-0920/drc-tribunal/r1/` (Write-created, no mkdir) and launches Grok and Gemini together. It enforces the 20-minute clock with a `date` at every notice, file-checks every house claim, and file-checks the Fable seat's claims at collate. Report: `reports/drc-tribunal-2026-09-22.md`, stop line `DRC TRIBUNAL R1 DONE · grok: … · gemini: … · astra: … · houses that ruled: <n> of 3 · claims that HOLD: <n> · blockers to build: <n> · owner items: <n> · ESCALATE: <n>`.
- **The question set: 21 items.** The proposal's T1–T7, T11, T8–T10 in its own order, then (a)–(j) from `39`, then EXPERIMENTS, OWNER and WRONG FACTS, and a closing `TRIBUNAL R1:` line. R65–R73 are framed as inputs: the houses rule HOW each diff row is built and whether its SOURCE holds, never its ACTION or WRITER. A house text that re-opens a ruling is escalated as `RE-OPENS A RULING`.
- **`41` Fable seat `drc-tribunal-fable-0922`** (`claude-fable-5-1`; the 7 + 3 read-only strings).
  - Gates: `FABLE ROW: R73`; the R73 literals, committed; a seat check (the session model must be `claude-fable-5-1`); the proposal and §13 committed.
  - BLIND to `scratch/…/drc-tribunal/` and to the hub report.
  - It reads the coach spec and his DRC by shape only, exactly what the houses get (L44, L32). It self-attacks by grepping 25 fields.
  - One file: `reports/drc-tribunal-fable-r1-2026-09-22.md`, stop line `DRC TRIBUNAL FABLE R1 DONE · verdict: … · adopt: <n> · adopt with wording: <n> · reject: <n> · experiments named: <n> · ESCALATE: <n>` (counts sum to 21).
  - Date 09-22 or 09-23 only.
- **`42` derive `drc-tribunal-derive-0922`** (`claude-fable-5-1`, R73; `75`'s shape).
  - Refuses unless both round-1 stop lines are present and committed, and at least one of Grok / Gemini ruled.
  - Folds verbatim only. A wording whose claim DOES NOT HOLD, or that its own seat WITHDREW, is never folded. R65–R73 are never re-opened: §13 ACTION and WRITER cells are frozen, only SOURCE cells may be tagged. S3's FINAL (v3 + R67) is not rewritten; seams are stated as seams.
  - Astra → `ASTRA PENDING (R13)`.
  - Writes `docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md` + `reports/drc-tribunal-derive-2026-09-22.md`, stop line `DRC DERIVED v2 · folds: <n> · verbatim: <n> · needs round 2: <n> · owner items: <n> · ESCALATE: <n>`.
  - `## FOR DEJAN` is one A/B per item with no recommendation (the seat holds a side, L37).

Launch order (desk):
1. Commit these four files, plus a `| R` launch row naming `40-drc-tribunal.md` with the three `<nn> is not running` statements (only if they are true).
2. Launch `40` and `41` together, before 19:25 ET today or on 09-23 before 19:25 ET. `41` does not wait on the window.
3. Commit both round-1 reports, then launch `42`.
4. If `42` finds items for round 2: round 2 must run by 09-23 23:59 ET (R30), otherwise it needs his word.

## PACKET
Source → staged path, size (B at drafting; ≈ = drafter's estimate of the excerpt), MANDATORY (M) / OPEN-AS-NEEDED (O):
| Staged | Source | Size | M/O |
|---|---|---|---|
| `00-READING-ORDER.md` | hub-written | ≈ 3,000 | M |
| `01-QUESTIONS.md` | `40` verbatim + file list | ≈ 12,500 | M |
| `02-greps.txt` | 21 commands (`40` §1) | ≈ 12,000–20,000 | M (search) |
| `10-PROPOSAL.md.part1` / `.part2` | `30 - Design/DRC-AUTOMATION-PROPOSAL-2026-09-22.md` :1–191 / :192–298 | 43,581 whole | M |
| `11-design-digest.md` | `reports/drc-design-2026-09-22.md` :3–7, :9–24, :38–44, :53–73 | ≈ 8,500 | M |
| `12-rulings.md` | `cto-2026-09-22.md` header + R60, R65–R73 verbatim | ≈ 11,000 | M |
| `13-spec-shape.md` | `_inflight/DRC-automation-spec-2026-09-22.md` — 15 headings + ≤ 32 key names (no values) | ≈ 1,500 | M |
| `14-drc-shape.md` | `DRC-2026-09-21.md` headings (title / date masked) + prompt lines that match his template outside its example blocks + unit markers | ≈ 3,000–4,000 | M |
| `20-trade-reporter.excerpt.txt` | `trade-reporter/app.py` whole (2,334) + `templates/index.html` :1–86 (of 10,271) | ≈ 6,500 | O |
| `21-drc-writers.excerpt.py` | `prefill/drc.py` :1–67, :321–350, :375–454 · `replay/line.py` :20–70, :143–178 · `replay/runner.py` :436–470 · `daymode/drc.py` :85–141 | ≈ 15,000 | M |
| `22-vaultwrite.excerpt.py` | `vaultwrite/writer.py` :380–420, :559–620, :644–680 | ≈ 7,000 | O |
| `23-aset.excerpt.py` | `aset/web.py` :1–24, :80–84, :940–960 · `aset/store.py` :51–75, :185–190, :197–257, :268–322 | ≈ 8,500 | O |
| `24-migrations.excerpt.py` | `db_migrations/__init__.py` :60–95 · `placement.py` :100–154 | ≈ 4,000 | O |
| `25-s3-legs.excerpt.md` | `S3-EXITS-v3-2026-09-22.md` :17–34, :110–139, :162–170 | ≈ 10,000 | M |
| `26-s3-legs-open.excerpt.md` | same :141–160 (the block R67 answered) | ≈ 8,000 | O, first cut |
| `27-laws-excerpt.md` | LAWS.md L1, L2, L3, L7, L8, L9, L10, L28, L32, L40, L42, L45, L53, L57, L68, L70 | ≈ 12,000 | O |
- Totals (estimate): MANDATORY ≈ 125–130 KB (≈ 31–33k tokens); whole ≈ 165–175 KB before cuts; ≈ 135–145 KB after cut order (i)–(v) (≈ 34–36k tokens). If it is still over 140 KB, the hub stages it and ESCALATEs (`73`'s rule).
- Token estimate per house: Grok ≈ 34–36k read (whole packet); Gemini ≈ 31–36k read; Astra —, not launched (R13); Fable seat (`41`, real files) ≈ 72–87k read, ≈ 12–18k out, peak ≈ 90–105k; derive (`42`) peak ≈ 120–150k; hub (`40`, Sonnet) ≈ 60–90k incl. file-checks.
- L32 at drafting:
  - The three redaction literals occur only in `aset/store.py:192`, `aset/web.py:355` and `aset/web.py:1084`. Every excerpt range skips all three; the hub greps every staged file anyway. The literals are not repeated in `40` (it points at `73` §1, as `35` did).
  - The proposal and its report carry 0 of them.
  - `trade-reporter/` is untracked on the host (`git ls-files` prints nothing). The playbook tab from `index.html:87` carries example placeholder tickers, so it is not staged.

## RULE PROOF
`grep -c -F -e "<string>"` with the quotes included, run separately for each string (40 vs 73: 17 calls each; 41 / 42 / 74 / 75: 10 calls, each over all four files):
| String | 40 | 73 | 41 | 74 | 42 | 75 |
|---|---|---|---|---|---|---|
| `"Bash(grok *)"` | 1 | 1 | — | — | — | — |
| `"Bash(agy *)"` | 1 | 1 | — | — | — | — |
| `"Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)"` | 1 | 1 | — | — | — | — |
| `"Bash(mkdir -p scratch/tribunal-bars-0920)"` | 1 | 1 | — | — | — | — |
| `"Bash(git -C /Users/cobalt/cobalt show*)"` | 1 | 1 | 1 | 1 | 1 | 1 |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 | 1 | 1 | 1 | 1 | 1 |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards show*)"` | 1 | 1 | — | — | — | — |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*)"` | 1 | 1 | — | — | — | — |
| `"Bash(git -C /Users/cobalt/cobalt-wt/s2-p2-cards diff*)"` | 1 | 1 | — | — | — | — |
| `"Bash(ls *)"` | 1 | 1 | 1 | 1 | 1 | 1 |
| `"Bash(grep *)"` | 1 | 1 | 1 | 1 | 1 | 1 |
| `"Bash(tail *)"` | 1 | 1 | 1 | 1 | 1 | 1 |
| `"Bash(wc *)"` | 1 | 1 | 1 | 1 | 1 | 1 |
| `"Bash(date*)"` | 1 | 1 | 1 | 1 | 1 | 1 |
| `"AskUserQuestion"` · `"EnterWorktree"` · `"Bash(git push*)"` | 1 (as one sequence literal) | 1 | 1 · 1 · 1 | 1 · 1 · 1 | 1 · 1 · 1 | 1 · 1 · 1 |
- Whole-sequence literal (from `--allowedTools` through the last `--add-dir`) = 1 in `40` and `73`, in `41` and `74`, and in `42` and `75`. Each list is byte-identical in order.
- The expected differences, and nothing else:
  - prompt path;
  - remote-control name (`drc-tribunal-0922` / `drc-tribunal-fable-0922` / `drc-tribunal-derive-0922`);
  - `--model claude-fable-5-1 --permission-mode auto` = 1 in `41`, `42` and `74`, 0 in `75` (`75` was re-pointed to `claude-opus-5-5` by R36; R73 overrides that for this tribunal);
  - cwd `~/cobalt-wt/agy-trial`, the same as the templates.

**NEW strings:** none (0).

READING:
- `prompts/2026-09-22/39-draft-drc-tribunal.md`; `prompts/2026-09-21/72-…`, `73-…` (whole), `74-…`, `75-…`; `prompts/2026-09-22/35-…`, `36-…`, `37-…`.
- `30 - Design/DRC-AUTOMATION-PROPOSAL-2026-09-22.md` (whole); `reports/drc-design-2026-09-22.md` (whole); `cto-2026-09-22.md` §4 rows R13, R30, R36, R58, R60, R62–R73 (by grep).
- `S3-EXITS-v3-2026-09-22.md` headings + :110–173; LAWS.md :1–66, :154–183, :212–245, :275–304, :343–397 plus the entry-heading list.
- Spec: headings plus a key-shaped line COUNT only (no line read). `DRC-2026-09-21.md` and `5 - Templates/DRC.md`: headings and marker prefixes only.
- `trade-reporter/app.py` (whole), `index.html` (grep of section and drop-zone lines).
- Code (defs and anchors by grep; the Read tool on `prefill/drc.py` :1–30 and :376–455): `prefill/drc.py`, `daymode/drc.py`, `replay/line.py`, `replay/runner.py`, `vaultwrite/writer.py`, `aset/web.py`, `aset/store.py`, `db_migrations/__init__.py`, `placement.py`.
- The 16 / 28 / 32 prompts (their stop prefixes and report names); the reports folder listing.
- `git log` on the proposal, the report and R73 (all committed: `c52133c`, `d1d81e0`, `938f1f5`).

## ESCALATE
1. **Section reference in `39`.** `39` (8') says "S3-exits v3 §2 (legs)". In v3, §2 is the state machine and the legs table is §3 (`S3-EXITS-v3-2026-09-22.md:110`). `40` stages §3 (:110–139, :162–170) plus `## Status after round 2` (:17–34), and says so in the part's guidance. The block R67 answered (:141–160) is OPEN-AS-NEEDED and the first cut.
2. **STAGGER needs the launch row to name three numbers.** `16`, `28` and `32` have no report on disk at 16:1x. Under `73`'s rule the hub refuses unless the desk's launch row states `16 is not running`, `28 is not running` and `32 is not running` on a line that also names `40-drc-tribunal.md`. Write those only if true.
3. **`42` adds one refusal that `75` did not have.** "A HOUSE MUST HAVE RULED": if neither Grok nor Gemini ruled, `42` FAILS. Otherwise the Fable seat would derive from its own ruling alone (L37). It is fewer, never more (safe default), and not a rule string. Strike it by re-issue if unwanted.
4. **Meter.** R73 puts the seat AND the derive on Fable (76 % at 13:45, R36). My estimates: seat peak ≈ 90–105k, derive peak ≈ 120–150k. The desk weighs these before launch (R58's brake).
5. **The packet likely sits at the 140 KB line.** The proposal alone is 43.6 KB with §13, which is MANDATORY. The hub stages and ESCALATEs per `73`'s rule if it is still over after cut (v); that is not a failure.
6. **`14-drc-shape.md`'s filter may stage few prompt lines.** F4: `DRC-2026-09-21.md` was rendered from the repo copy `drc.md.j2`, not his template. Note lines that differ from his template by a byte are DROPPED and counted, never guessed. The houses then see the headings and a smaller prompt set. The proposal's §13 still names every `DRC:n` range.

## CONTINUE
- Done. Next (desk): commit the four files; write the launch row for `40` / `41` (with ESCALATE 2's three statements if true); launch `40` + `41` inside R30's window, outside 19:25–20:45 ET; after both stop lines are committed, launch `42`.

DRC TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: METER — proceed on three · questions: 21 · packet: 140 KB · new rule strings: 0 · ESCALATE: 6
