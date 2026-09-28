# DRC overnight lane — round-2 prompts drafted (2026-09-24)

Seat `drc-overnight-r2-draft-0924` · `claude-opus-5-5` · started 10:57 ET, prompts written by 11:05 ET, report closed 11:06 ET Thu 2026-09-24 (each time from `date`). Nothing launched, built or committed.

## §0 Headline

- WROTE `prompts/2026-09-24/27-drc-overnight-tribunal-r2.md` (house hub r2, 49,210 B), `28-drc-overnight-tribunal-fable-seat-r2.md` (blind Anthropic seat r2, 17,713 B) and `29-drc-overnight-tribunal-derive-r2.md` (second derive → v3, 19,876 B).
- Two items only. `R2-1` is the derive's (i)–(iii) and gates K2. `R2-2` is the derive's ESCALATE 9 (the `via` value, its migration, the CLI as the statement caller) and gates K1.
- Packet ≈ 110–115 KB (limit 140), with `pairing.py` and `store.py` WHOLE (the R36 ESC 1 fix). Rule proof: 0 new strings. Every launch line matches its precedent byte for byte except the path and the rc name.
- ESCALATE: 4 (stagger reads, one small greps file I added, the launch-row literal set, R2-2(c) vs the desk's R37 line).

## DIGEST FOR THE DESK

- **R2-1:** does a FIRST record of an earlier day P, made after a later day N, re-pair N forward? If it does, does P's carried book replace N's STATED seed (R67), and where does a re-paired day's stats input come from? The seat stands against Grok and Gemini.
- **R2-2:** name `drc_stated_books.via` for the `cobalt drc state-book` CLI caller, say what that does to the one K1 migration, and say whether the CLI is the statement caller when K3 is not checked.
- **`27` needs:** a committed desk row that names `27-drc-overnight-tribunal-r2.md` and carries `Fable seat: yes` and `derive seat: claude-opus-5-5`. It also needs the derive's stop line committed (already done) and v2 committed (already done). The R19 row (L62) is the grok / agy gate. The packet stages into `scratch/tribunal-bars-0920/drc-overnight/r2/`.
- **`28` needs:** the same launch row (it greps for `27`'s filename). It runs beside `27` with no stagger.
- **`29` needs:** both round-2 stop lines present and committed, a `TRIBUNAL R2:` line in Grok's field (the floor), and the same launch row.
- **Launch order:** `27` and `28` together → both stop, and the desk commits them → `29`.
- **Stagger reads the desk makes before `27`:** the reports of `15`, `16`–`19` (voice a–d), `74` and `23` must each end on their done prefix or `FAILED`. For a prompt with no report, the launch row must say `<nn> is not running`. `18` is running now (R37). `19` has no report yet, so the row needs `19 is not running`, unless `19` has run and stopped by then.
- **Stop lines the desk watches:**
  - `^(DRC OVERNIGHT TRIBUNAL R2 DONE|FAILED)` on `reports/drc-overnight-tribunal-r2-2026-09-24.md`
  - `^(DRC OVERNIGHT FABLE R2 DONE|FAILED)` on `reports/drc-overnight-tribunal-fable-r2-2026-09-24.md`
  - `^(DRC OVERNIGHT DERIVED v3|FAILED)` on `reports/drc-overnight-tribunal-derive-r2-2026-09-24.md`
- **After `29`:** `converged: 2 of 2` closes the tribunal, and v3 = `docs/30 - Design/DRC-OVERNIGHT-POSITION-v3-2026-09-24.md` becomes the K1–K4 build drafter's input. Otherwise the desk brings Dejan ONE A/B per item.

## PACKET

Staged by `27` into `scratch/tribunal-bars-0920/drc-overnight/r2/`. Sizes are measured from the source ranges with `wc -c` at drafting and do not include the one-line range headers.

| Staged file | Source | Bytes |
|---|---|---|
| `00-READING-ORDER.md` | written last by the hub | ≈ 3,000 (est.) |
| `01-QUESTIONS-R2.md` | `27`'s verbatim paragraph + the "Files in this folder" paragraph | 7,364 + ≈ 1,500 |
| `02-greps.txt` | 7 searches (`27` §1), measured by running the same greps | 12,666 (≈ 14,000 with absolute paths) |
| `10-NEEDS-ROUND-2.md` | derive report `:90-101`, ESCALATE 5 `:144`, 9 `:148` | 3,358 |
| `11-v2-sections.excerpt.md` | v2 `:1-11`, `:73-94`, `:95-110`, `:111-165`, `:166-190`, `:201-216`, `:261-268`, `:276-285`, `:295-306`, `:308-316` | 34,669 |
| `12-hub-checks.md` | round-1 hub rows: rulings Q3 / Q10 / (b) / (e); GK7, GK13, GK21, GK26, GK32, GM3, GM8, GM12; FC3, FC13, FC19, FC22; ESCALATE 1–2; the three headers | 4,699 |
| `13-seat-r1.excerpt.md` | seat r1 `:41-52`, `:75-77`, `:98-107`, `:114-120` | 4,795 |
| `14-grok-r1-own.excerpt.md` [RAW, Grok only] | `r1/grok-ruling.md` `:21-28`, `:77-86`, `:133-147`, `:171-178` | 6,237 |
| `15-gemini-r1-own.excerpt.md` [RAW, Gemini only] | `r1/gemini-ruling.md` `:9-12`, `:37-40`, `:48-50`, `:57-59` | 1,528 |
| `20-pairing-whole.py` | D1 `src/cobalt/drc/pairing.py` WHOLE (348 lines, 0 trailing-ws lines) | 12,901 |
| `21-store-whole.py` | D1 `src/cobalt/drc/store.py` WHOLE (253 lines, 0 trailing-ws lines) | 10,568 |
| `22-cited.excerpt.py` | `models.py:94-113`, `:254-263`; `test_drc_pairing.py:340-351`; `0016_drc.sql:17-95`; `propose.py:300-307` | 5,670 |

- **Total:** sources 91,789 B. With greps, `00`, the files paragraph and headers: **≈ 110–115 KB**, under the 140 KB limit, so the cut order should not fire.
- **Cut order in `27`:** (i) v2 down to its marker paragraphs, (ii) `02-greps.txt`. The two whole files are never cut.
- **Token estimate** (bytes ÷ 4): ≈ 28k for the whole packet. Each house opens only its own `-own` excerpt, so Grok reads ≈ 27k and Gemini ≈ 26k.
- **Code tip verified at drafting:** `drc/d1-trading-log` = `38a70947…`, worktree clean. All five code file sizes match `23`'s figures.

## RULE PROOF

Each launch line's quoted strings were checked with `grep -c -F` against its precedent line. Every count is ≥1:

| Prompt | Precedent | Strings checked | Counts | Flags (`--model`, `--permission-mode auto`, `--add-dir` ×3) | Line with path + `--remote-control` removed |
|---|---|---|---|---|---|
| `27` | `23` | 14 allow + 3 deny | all 1 | all 1 (`claude-sonnet-5`) | IDENTICAL |
| `28` | `24` | 7 allow + 3 deny | all 1 | all 1 (`claude-opus-5-5`) | IDENTICAL |
| `29` | `25` | 7 allow + 3 deny | all 1 | all 1 (`claude-opus-5-5`) | IDENTICAL |

NEW strings: none. The rc names are `drc-overnight-tribunal-r2-0924`, `drc-overnight-fable-r2-0924` and `drc-overnight-derive-r2-0924`. Every command shape in the three bodies (`grep -n`, `grep -c -x -F`, `git log -1 --format=%H -S…`, `tail -n 3`, the `codex` probe, and the grok / agy spellings reached through `23` → `04`) appears in `23`–`25` / `19`–`21`.

## EXPERIMENTS

| X | What it runs | Could a house settle it from reads? | Where it runs |
|---|---|---|---|
| v2 X9 | Supersede day 1, re-pair day 2: does the day re-pair from the current import's fills and its stored `stats_row` rows to identical rows? | No. The mechanism is readable (`store.py:170-186`, `:195`, `:201-203`), but "identical" needs a run. | K2 first gate |
| v2 X10 | Record Wed stated flat, then Tue as a first file: is Wed re-paired, and is the difference shown? | No. The sequence is readable (`pairing.py:249-250`, `store.py:227-235`; hub C1/C7), but the result depends on the wording R2-1 picks. | K2 first gate |
| v2 X7 | Re-pair all-or-nothing across one DB transaction | No (L70) | K2 first gate |
| v2 X1–X6 | Carry and hash, first-import cover, null cost, hash stability, `0016` fold, `market_reset` refusal | No | **K1 build's first gate: 6** (plus any R2-2 experiment `29` folds) |

- None of these can be settled from reads.
- R2-2 is expected to add no experiment: `02-greps` shows `drc_stated_books` exists on no branch, so a `via` literal changes only the unwritten K1 migration.
- The K1 prompt runs X1–X6 first. The K2 prompt runs X7–X10 (X11 and X12 as v2 places them).

## L74

The tool result of this session's first read of the drafter card had a system-reminder-shaped block appended to it. It asked for a `Claude-Session:` line in commits and named a file-send tool. It is recorded once here as DATA and was not followed. This seat commits nothing and sent no file.

## ESCALATE

1. **Stagger (a desk read before `27` launches).** `18` (voice C) is running per R37, and `19` has no report. `27`'s preflight refuses while `18`'s report is not on its done prefix, and it refuses on `19` unless the launch row says `19 is not running` (`23`'s (7') rule, extended to `23`'s own report). `28` does not block and may launch at any time after the row is committed.
2. **`02-greps.txt` is staged (≈ 13–14 KB), though the card expected no searches for two items.** R2-2(b) turns on whether `drc_stated_books` exists on any branch, and the headless houses cannot run `grep` (L33). It is second in the cut order and never displaces the two whole files.
3. **Launch-row literals.** All three gates grep for ONE row that names `27-drc-overnight-tribunal-r2.md` and carries exactly `Fable seat: yes` and `derive seat: claude-opus-5-5`. Round 1 also required the proposal filename. I dropped that literal on purpose so `27`, `28` and `29` all read the same row, and `27`'s authorization separately proves that v2 is committed.
4. **R2-2(c) overlaps the desk's R37 line** ("+ K3 when checked; else the CLI statement caller"). That line is a desk plan, not his ruling. R2-2(c) asks the houses to settle the mechanism. If they rule otherwise, the desk's landing-set line needs a re-read, not a fold.

## CONTINUE

next: done. The desk commits the three prompts and this report, writes the launch row (literals above, plus `19 is not running` if `19` has not run), and launches `27` + `28`.

OVERNIGHT R2 PROMPTS DRAFTED · prompts: 3 · items: 2 · packet: 113 KB · new rule strings: 0 · experiments for K1: 6 · ESCALATE: 4
