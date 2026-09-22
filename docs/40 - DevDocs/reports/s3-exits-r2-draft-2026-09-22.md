# S3 exits tribunal R2 — draft report (2026-09-22)

Seat `s3-exits-r2-draft-0922` · Opus 5.5 (`claude-opus-5-5`, R36) · prompt `prompts/2026-09-22/34-draft-s3-exits-r2.md` · 14:49–14:58 ET (`date`) · three prompts written; nothing launched or committed.

## DIGEST
- **R2-1:** does gemini's round-1 DO NOT BUILD still stand against v2's text (the one-transaction fill `[F-22]`, and the share-count fix whose form is left to R2-2)? A = v2 answers it, B = it stands. Every house adds one line: `DO NOT BUILD stands: <defect, file:line>` or `DO NOT BUILD withdrawn`.
- **R2-2:** leg corrections and running shares. G = grok's stored chain, with neighbour checks and no UNIQUE. F = Fable's partial `UNIQUE … WHERE corrects IS NULL`, greatest-id current row, and running derived under the row lock. Houses give one answer for the item, plus one line each for (a)–(g).
- **R2-3:** which runner carries M1. A = grok (`db_migrations`, plus `kind` in `cards/migrations/`). B = gemini (the module sets). C = Fable (one numbered `db_migrations` file with a rollback). This turns on the `ensure_schema()` runners against `cobalt db migrate`.
- **`35` (Sonnet hub, Grok + Gemini):** stages the fold only, about 110–120 KB. It file-checks C1–C9 of the Fable seat's round-1 claims while the houses run. Astra: the probe is carried and records `METER — proceed on three`.
- **`36` (the Fable seat on `claude-opus-5-5`, R36/R62, blind):** attacks its own round-1 text first (grep-first self-attack) and rules the same three items.
- **`37` (derive on `claude-opus-5-5`, DERIVE ROW R36):** writes v3 = `docs/30 - Design/S3-EXITS-v3-2026-09-22.md`. An item that does not converge gets an OPEN FOR DEJAN block, never a vote. A round 3 happens only on a house's DO NOT BUILD.
- **New rule strings: 0.** The one expected difference is `--model claude-opus-5-5` on `36`.
- **Launch order:** `36` beside `35` → both stop lines committed → `37`. `35` gates itself: the date must be 2026-09-22 or 2026-09-23 (R30), the time outside 19:25–20:45 ET and before 23:20 ET, and there must be a launch row, plus the stagger on `16` / `23` / `28`.
- **Stop lines to watch:** `35` `^(S3 EXITS TRIBUNAL R2 DONE|FAILED)` · `36` `^(S3 EXITS TRIBUNAL FABLE R2 DONE|FAILED)` · `37` `^(S3 EXITS DERIVED v3|FAILED)`.

## RULE PROOF
Every string of each new launch line was counted with `grep -c -F -e` in the new file and in its precedent's file. Counts are shown as new|precedent.

| new file | precedent | strings checked | counts |
|---|---|---|---|
| `35-s3-exits-tribunal-r2.md` | `2026-09-21/73-s3-exits-tribunal.md` | 14 allow + 3 deny; `--model claude-sonnet-5`; `--permission-mode auto`; `` `cd /Users/cobalt/cobalt-wt/agy-trial` ``; `claude --bg "Read `; `--allowedTools`; `--disallowedTools`; `--remote-control`; the three `--add-dir`; grok `--sandbox cobalt-job --allow "Write(…/tribunal-bars-0920/**)"`; the agy `--print=` spelling; the codex probe | all 1\|1 |
| `36-s3-exits-tribunal-fable-seat-r2.md` | `2026-09-21/74-s3-exits-tribunal-fable-seat.md` | 7 allow + 3 deny; `--permission-mode auto`; cd; `claude --bg`; the flags; the add-dirs | all 1\|1 |
| `36` `--model` | `74` | `--model claude-opus-5-5` / `--model claude-fable-5-1` | 1\|0 / 0\|1 — **the ONE expected difference** (R36; its MODEL line says so) |
| `37-s3-exits-tribunal-derive-r2.md` | `2026-09-21/75-s3-exits-tribunal-derive.md` | 7 allow + 3 deny; `--model claude-opus-5-5`; `--permission-mode auto`; cd; `claude --bg`; the flags; the add-dirs | all 1\|1 |
| whole span `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` | 73 / 35 · 74 / 36 · 75 / 37 | one span each | 1 in precedent, 1 in approved source |
| approved sources | `2026-09-20/08-bars-chunk-e-check.md` (35's span) · `2026-09-21/22-draft-setups-tribunal.md` (36 and 37's span) | span | 1 · 1 · 1 |

**NEW strings: none.** In each launch line, the only differences from the precedent are the prompt path, the `--remote-control` name (`s3-exits-tribunal-r2-0922` · `s3-exits-tribunal-fable-r2-0922` · `s3-exits-tribunal-derive-r2-0922`) and, on `36`, `--model`. `37` drops `75`'s "THE DESK replaces `--model`" clause because R36 has already fixed the value (`21`'s precedent). `35` carries no Astra launch spelling, only the probe. L32: `grep -c -E` for the three literals from `73` §1 found 0 in all three prompts. None of the files names those literals: `35` points the hub to `73` §1's command.

## EXPERIMENTS
These are the derive's X4, X6 and X7, from v2 `## First-gate experiments (L70)`.

| X | runs | a house can run it from reads? | what it gates | who runs it first |
|---|---|---|---|---|
| X4 | `cobalt_dev`: create `"user".legs` with the trigger; UPDATE (must fail); duplicate `(card_id, seq)`; a correction; a correction of a correction; the view; the GUC default | **no** (a database) | R2-2 (a)/(b); C1's DDL | **C1 build prompt, first.** Whichever option v3 keeps, its index and view wording are proven or changed here. |
| X6 | `cobalt_dev`: `structural_stop` on a manual `aset_sizings` row | **no** (a database) | C1 / C3 (v2 §5 manual-card case; not a round-2 item) | **C1 build prompt** (before the ↺ / gap code in C3) |
| X7 | `cobalt_dev`: two concurrent ½ taps on one FILLED 100-share card under the row lock | **no** (a concurrent run) | R2-2 (g); C2 | **C2 build prompt, first.** Its expected outcome ("one refused" or "writes 25") is set by v3. |

As expected, none can be run from reads. `35` and `36` tell every seat to cite X4 and X7, not restate them, and `37` merges any round-2 repeat into those rows. I launched none of them.

## ESCALATE
1. **The launch row carries two new gates (from `73`, not `19`).** `35` requires a committed desk `| R` row naming `35-s3-exits-tribunal-r2.md`. For any stagger hub whose report does not exist yet (`16` `setups-check-r2`, `28` `handicap-h1-check` at drafting), that row must also contain the literal `<nn> is not running`, otherwise `35` fails at preflight. `23`'s report exists and ended `FAILED PREFLIGHT …`, so it passes. Desk: write the launch row with those literals, or re-issue `35` (L19).
2. **Window.** R30 covers `grok` / `agy` through 2026-09-23 23:59 ET only. `35` must launch outside 19:25–20:45 ET and before 23:20 ET on 09-22 or 09-23. Any later run needs a new row of his and a re-issue.
3. **The Fable seat changes model between rounds.** Round 1 ran on `claude-fable-5-1`; round 2 runs on `claude-opus-5-5` (R36, R62). `36` treats it as the same SEAT (R57 plus R62) with the same self-attack duty, and fails closed if it reads R57 / R62 otherwise. The derive `37` is another Opus 5.5 session. It is stated as holding no side.
4. **R2-2 is one item with seven sub-points.** Following the task's "per item", seats give ONE answer (G / F / NEITHER / OWNER), and the (a)–(g) lines are support only. A mixed view has to be written as NEITHER with wording, so R2-2 is the item most likely to end OPEN FOR DEJAN.
5. **R2-3's B (gemini) is incomplete.** It places only the `card_stop_edits` and `aset_sizings` changes. Where `legs`, `legs_current_v` and M2 go under B is unstated in round 1, so a house may answer NEITHER.
6. **`'user'` notation.** Inside `35`'s quoted QUESTIONS-R2 paragraph the Postgres schema is written `'user'` (single quotes), to keep the paragraph's double quotes intact. The excerpts show the real `"user"`.
7. **L74, recorded once:** a system reminder asked for a `Claude-Session` commit line and named a file-send tool. This seat commits nothing and sent nothing.

S3 EXITS R2 PROMPTS DRAFTED · prompts: 3 · new rule strings: 0 · ESCALATE: 7
