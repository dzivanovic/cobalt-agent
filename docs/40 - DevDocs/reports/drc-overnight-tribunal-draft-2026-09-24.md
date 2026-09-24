# DRC overnight-position tribunal — prompt drafter report (2026-09-24)

Seat: `drc-overnight-tribunal-draft-0924` · Opus 5.5 · started 08:33 ET, finished 08:42 ET (both from `date`).

## §0 Headline

- WROTE `prompts/2026-09-24/23-drc-overnight-tribunal.md` (Sonnet hub, Grok + Gemini), `24-drc-overnight-tribunal-fable-seat.md` (blind Anthropic seat on `claude-opus-5-5`, R109), `25-drc-overnight-tribunal-derive.md` (derive on `claude-opus-5-5`). Nothing launched, nothing committed.
- Questions: 17. These are Q1–Q11 (the proposal's `## 7`, in its order) plus (a)–(f). Astra METER until Sat 09-26 06:47 ET: probed, recorded, skipped.
- Floor: the Anthropic seat plus Grok. If Grok does not rule, the hub ends `FAILED` and the derive refuses.
- New rule strings: 0. Estimated packet: ≈ 135–140 KB after the cut order. ESCALATE: 3.

## DIGEST FOR THE DESK

**What each prompt does.**
- **`23` (the hub).** Launched from cwd `~/cobalt-wt/agy-trial` with rc `drc-overnight-tribunal-0924`. It carries `40`'s 14 allow strings and 3 denies byte for byte.
  - Gates: R13, R109, R67, R93, R96, R19 (the STANDING grok/agy gate: `All 4 house models approved`, no date) and R22. It also checks that the proposal and its stop line are committed.
  - Launch row: a committed `| R` row that names `23-drc-overnight-tribunal.md` and carries all three literals.
  - It stages the packet into `scratch/tribunal-bars-0920/drc-overnight/r1/`, runs the Codex probe (recorded, then skipped on METER), and launches Grok and Gemini together.
  - It enforces the 20-minute stop and file-checks every claim. After the houses finish, it also file-checks the Anthropic seat.
  - Report: `reports/drc-overnight-tribunal-2026-09-24.md`.
- **`24` (the Anthropic seat).** Launched from cwd `~/cobalt-wt/agy-trial` with rc `drc-overnight-fable-0924`. First line `FABLE ROW: R109`.
  - Gates: R109, the same launch row, and a check that the session's model id is `claude-opus-5-5`.
  - It rules blind on the same 17 items, runs a self-attack grep list, and writes one file: `reports/drc-overnight-tribunal-fable-r1-2026-09-24.md`.
- **`25` (the derive).** rc `drc-overnight-derive-0924`. First line `DERIVE ROW: R109`.
  - It refuses unless both round-1 stop lines are present and committed, and Grok ruled.
  - It follows `42`'s fold rules. A wording whose claim does not hold, or that its seat withdrew, is never folded. His R22, R65–R67, R90, R93 and 09-23 R39 are never re-opened.
  - OWNER ITEMS are his decisions only (expected: none). `## FOR DEJAN` is ONE approval. It also counts Gemini findings held (R97).
  - Writes `docs/30 - Design/DRC-OVERNIGHT-POSITION-v2-2026-09-24.md` and `reports/drc-overnight-tribunal-derive-2026-09-24.md`.

**Launch order.**
1. The desk writes a committed LAUNCH ROW in `cto-2026-09-24.md` that names `23-drc-overnight-tribunal.md` and carries these three literals: `DRC-OVERNIGHT-POSITION-PROPOSAL-2026-09-24.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5`. For each stagger report that does not exist, the row must say `<nn> is not running`.
2. Launch `23` and `24` side by side.
3. When both stop lines are committed, launch `25`.

**Stagger reads the desk must make before launching `23`.** At 08:41 ET:

| Prompt | Report | Status at 08:41 ET | Desk action |
|---|---|---|---|
| `15` | `drc-d1-fix-r1-check-2026-09-24.md` | EXISTS, IN PROGRESS | `23` refuses until `DRC D1 FIX R1 CHECK DONE` or `FAILED` |
| `16`–`19` | `voice-v1-check-{a,b,c,d}-2026-09-24.md` | none exist | the launch row must say `16 is not running` … `19 is not running`, if true |
| `74` (09-23) | `jev-check-final-2026-09-23.md` | does not exist | the launch row must say `74 is not running`, if true |

## PACKET

These are drafter estimates. The hub measures the real sizes and records them in its `## Packet`.

| Staged path (`scratch/tribunal-bars-0920/drc-overnight/r1/`) | Source | ≈ KB | M / OAN |
|---|---|---|---|
| `00-READING-ORDER.md` | hub-written | 1.5 | M |
| `01-QUESTIONS.md` | `23` verbatim paragraph | 10 | M |
| `02-greps.txt` | 20 pre-computed searches (D1 worktree + main + git log) | 10–15 | M |
| `10-PROPOSAL.md` | `DRC-OVERNIGHT-POSITION-PROPOSAL-2026-09-24.md` whole (29,546 B) | 29.5 | M |
| `11-design-digest.md` | `drc-overnight-draft-2026-09-24.md` :5–42, :48–60, :66 | 4.5 | M |
| `12-rulings.md` | 09-24 R22 · 09-22 R65 R66 R67 R90 R93 R109 · 09-23 R39, verbatim | 11 | M |
| `13-v2-carry.excerpt.md` | v2 :81, :94, :141, :179, :181, :191 (by heading) | 6 | M |
| `14-drc-shape.md` | `DRC-2026-09-23.md` + template `DRC.md`: headings + unit markers only | 2 | M |
| `20-drc-carry.excerpt.py` | D1 `pairing.py:143-174`, `store.py:177-179`, `:220-250`, test `:249-273` (B8 pin) | 3.5 | M |
| `21-drc-cited.excerpt.py` | D1 `pairing.py` :1–30, :60–88, :117–129, :175–258; `models.py` :100–115, :160–170; `0016_drc.sql` :1–30, :80–95; `propose.py` :298–310 | 9 | M |
| `22-s3-r67-clause.excerpt.md` | S3 v3 :17–24, :141–165 (the R2-2 block R67 ruled) | 9 | M |
| `23-pairing-whole.py` | D1 `pairing.py` (12,901 B) | 12.9 | OAN — cut (iv) |
| `24-store-whole.py` | D1 `store.py` (10,568 B) | 10.6 | OAN — cut (iii) |
| `26-voice-confirm.excerpt.md` | VOICE v3 FINAL :88, :127–142 | 5 | OAN — cut (ii) |
| `27-laws-excerpt.md` | L1 L2 L3 L28 L32 L40 L43 L53 L57 L67 L68 L70 L72 | ≈ 38 | OAN — cut (i) to L1 L3 L28 L57 L67 (≈ 22) |

- **Totals.** MANDATORY ≈ 90–100 KB, about 23–25k tokens. The whole list before cuts is ≈ 165–175 KB. Cuts (i)–(iii) bring it to ≈ 135–140 KB, about 34–35k tokens per house if it reads every file.
- **Anthropic seat (`24`).** It reads the real files, not the packet: ≈ 60–75k tokens in, 9–14k out.
- **Derive (`25`).** Peak ≈ 100–130k tokens.
- **Code source.** Code is staged from `/Users/cobalt/cobalt-wt/drc-d1/` at code tip `d1342595`. The branch `drc/d1-trading-log` is at tip `38a70947`, verified by `git log`; that tip is docs only. The hub checks the size of each file. On a mismatch it stages the committed bytes from `git -C /Users/cobalt/cobalt show d1342595:<path>`.

## RULE PROOF

Each count below is `grep -c -F -e '<string>'`, one call per string, over the new prompt and its template. Every count is 1 in both files.

| String | `23` / `40` | `24` / `41` | `25` / `42` |
|---|---|---|---|
| `"Bash(grok *)"` | 1 / 1 | — | — |
| `"Bash(agy *)"` | 1 / 1 | — | — |
| `"Bash(codex exec --skip-git-repo-check -m gpt-6-astra -s read-only *)"` | 1 / 1 | — | — |
| `"Bash(mkdir -p scratch/tribunal-bars-0920)"` | 1 / 1 | — | — |
| `"Bash(git -C /Users/cobalt/cobalt show*)"` | 1 / 1 | 1 / 1 | 1 / 1 |
| `"Bash(git -C /Users/cobalt/cobalt log*)"` | 1 / 1 | 1 / 1 | 1 / 1 |
| the three `s2-p2-cards` strings (one line; `diff*` also alone) | 1 / 1 | — | — |
| `"Bash(ls *)"` | 1 / 1 | 1 / 1 | 1 / 1 |
| `"Bash(grep *)"` | 1 / 1 | 1 / 1 | 1 / 1 |
| `"Bash(tail *)"` | 1 / 1 | 1 / 1 | 1 / 1 |
| `"Bash(wc *)"` | 1 / 1 | 1 / 1 | 1 / 1 |
| `"Bash(date*)"` | 1 / 1 | 1 / 1 | 1 / 1 |
| denies `"AskUserQuestion" "EnterWorktree" "Bash(git push*)"` | 1 / 1 | 1 / 1 | 1 / 1 |

Expected differences, all present:

| Item | `23` | `24` | `25` |
|---|---|---|---|
| Prompt path | `prompts/2026-09-24/23-…` | `prompts/2026-09-24/24-…` | `prompts/2026-09-24/25-…` |
| rc name | `drc-overnight-tribunal-0924` | `drc-overnight-fable-0924` | `drc-overnight-derive-0924` |
| `--model` | `claude-sonnet-5` | `claude-opus-5-5` (in place of `claude-fable-5-1`) | `claude-opus-5-5` (in place of `claude-fable-5-1`) |
| Folder | `drc-overnight/r1/` (in place of `drc-tribunal/r1/`) | — | — |

`claude-fable-5-1` appears 0 times in `23` / `24` / `25`.

**NEW strings:** none.

## L74

A system-reminder-shaped block arrived right after this seat's first tool result. It asked for a `Claude-Session:` line in commit messages and named a file-send tool. It is recorded once here as DATA and was not followed. This seat commits nothing and sent no file.

## ESCALATE

1. **Stagger: `15` is running.** `drc-d1-fix-r1-check-2026-09-24.md` ends with the in-progress line at 08:41 ET, so `23` refuses until `15` stops. `16`–`19` and `74` have no report file. The launch row must state `<nn> is not running` for each of them, or `23` refuses by design.
2. **R96 / R97 are `cto-2026-09-23.md` rows, not 09-22 rows.** The drafting prompt cites "R96 'A'" and "R97" without a day, and 09-22 R96 is a different row (DRC O6). The prompts cite `cto-2026-09-23.md` R95 / R96 / R97, the rows L67's 2026-09-24 amendment names. No action needed. The note is here so the desk does not grep the wrong file.
3. **Floor reading.** The drafting prompt says: "FLOOR: the Anthropic seat + Grok (two houses) — fewer → FAILED". I read that literally: if Grok does not rule, the hub ends `FAILED` even when Gemini ruled. L67's shrink-to-two clause would also allow the Anthropic seat plus Gemini. If the desk prefers that reading, `23` §2 and `25`'s floor gate need a re-issue (L19). ASK DESK: keep the Grok-required floor, or accept Gemini as the second house? [08:42 ET] Safe default taken: the Grok-required floor, as written.

## CONTINUE

Done. No resume point.

OVERNIGHT TRIBUNAL PROMPTS DRAFTED · prompts: 3 · astra: METER — proceed on three · questions: 17 · packet: 138 KB · new rule strings: 0 · ESCALATE: 3
