# BARS CHUNK 1A CHECK R3 — 2026-09-21 (hub `bars-chunk-1a-check-r3-0921`)

## §0 Headline
Round 3 of 3 (the LAST) on chunk 1a, the same fix `589d40f..1404f23` (nothing built since round 2): **3 of 3 houses checked**, each ended `CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES` (grok, gemini, astra).
X9/X14 one shape: **3 of 3 YES**, and my file-check of the generator (`partitions.py:98`, sibling tip `159f31d`), the pattern (`placement.py:255`, `:278-288`) and the tests HOLDS. FIX rows X1–X14 CLOSED by every house that answered them: **14 of 14**; new defects **0**; nothing reaches a card.
One hunk outside the X14 row HOLDS (`tests/cobalt/test_migrate_proof.py`, a fixture NAME re-pointed, 13 lines) — the fixer disclosed it; grok and astra named it, gemini answered `NONE` (contradiction quoted, nothing smoothed). `requires_db` tests still OWED; the stacked-tree gate is the desk's.
ESCALATE: 5 (`## FOR DEJAN`: 2 OWNER ITEMs, O1 RULED by R45, O2 carried). Nothing else is open after this round.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| DATE GATE (1st) | `date` | 0 | allowed — `Mon Sep 21 06:11:44 EDT 2026` (not 2026-09-22 or later → gate passes) |
| authorization | `git -C /Users/cobalt/cobalt log --oneline -6 -- "docs/40 - DevDocs/reports/cto-2026-09-20.md"` | 0 | allowed — top: `89355f5 docs(desk): 09-21 wake-up b571b1da …` |
| authorization | `grep -n "^| R13 " …cto-2026-09-20.md` | 0 | allowed — line 86, R13 13:33 ET "Push and approved everything…" |
| authorization | `grep -n "^| R23 " …` | 0 | allowed — line 206, R23 17:47 ET "yes" (grok/agy through 2026-09-21 23:59 ET) |
| authorization | `grep -n "^| R25 " …` | 0 | allowed — line 262, R25 17:58 ET "approved" |
| authorization | `grep -n "^| R48 " …` | 0 | allowed — line 463; names `prompts/2026-09-20/25-bars-chunk-1a-fix-1b.md` and "ONE step X14, the child-name seam" |
| authorization | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R25 \|" -- …` | 0 | allowed — `e15d03eac2076366a3009b2d56ac40cba92dd6fc` (non-empty) |
| authorization | `git … log -1 --format=%H -S"1a's ROUND 3 is a CHECK, not a fix" -- …` | 0 | allowed — `e28ba05ed1a50fccae1cdc8e808398de1ae54ca3` (non-empty) |
| authorization | `git … log -1 --format=%H -S"the GENERATOR's Monday-date shape stands" -- …` | 0 | allowed — `407091266786727a04f188baa81feebedf4c305d` (non-empty) |
| METER | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| METER | `agy --version` | 0 | allowed — `1.2.7` |
| worktree | `ls /Users/cobalt/cobalt-wt/bars-chunk-1a` | 0 | allowed — present (src, tests, docs, configs …) |
| fix built | `tail -n 3 "/Users/cobalt/cobalt-wt/bars-chunk-1a/docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md"` | 0 | allowed — LAST NON-BLANK line: `BARS CHUNK 1A FIX BUILT 1404f23 \| on 589d40f \| offline 2295/0 (355 skipped; fix round 1 2291/0) \| fixed: X14 \| not fixed (listed): 13 \| default migrate statement order unchanged: proven \| card/scoring paths untouched: empty diff \| db: OWED — 0 requires_db tests written, never run \| ESCALATE: 6` → `<fix tip>` = `1404f23`, `<round-1 tip>` = `589d40f` |
| branch tip | `git -C /Users/cobalt/cobalt log --oneline -1 bars/chunk-1a-0920` | 0 | allowed — `6961ee0 docs(report): bars chunk 1a fix round 1b — the child-name seam` (matches) |
| boundary | `git … log --stat --oneline 589d40f..1404f23` | 0 | allowed — 13 commits (1404f23, 8dddf2b, 793f452, 81dae9c, beab8c7, 5114af9, c8893c7, e493c95, 4778c31, 19e0228, e292817, a4f9a07, de70755), same seven paths as round 2 |
| X14 paths | `git … log --stat --oneline 1404f23^..1404f23` | 0 | allowed — `placement.md` (31), `placement.py` (52), `test_migrate_proof.py` (13), `test_tenancy.py` (77); 4 files, 118 insertions(+), 55 deletions(-) |
| round-2 folder | `ls scratch/tribunal-bars-0920/chunk-1a-check-r2` | 0 | allowed — holds `grok-check-r2.md`, `astra-check-r2.md`, `QUESTIONS-R2.md`, `classify.md`, `round1-verdicts.md`, `fix-diff.md.part1`…`part5`, `fix-report.md.part1`…`part3`, `fix-prompt.md.part1`/`part2`, `fixed/`, plus round 2's probe leftover `wstest.tmp` (ignore) |
| round-2 fixed | `ls …/chunk-1a-check-r2/fixed` | 0 | allowed — `cli.md`, `cli.py.part1`/`2`, `placement.md`, `placement.py`, `test_migrate_proof.py.part1`…`5`, `test_tenancy.py.part1`/`2` |
| packet sizes | `wc -c` of every round-2 packet file (one call) | 0 | allowed — every size equals round 2's `## Packet` table (fix-diff parts 14,866 / 49,325 / 20,192 / 17,282 / 5,415; classify 10,052; fix-report 36,723 / 35,759 / 3,997; fix-prompt 34,730 / 5,227; QUESTIONS-R2 8,230; fixed/ cli.py 34,609 / 22,723, placement.py 11,711, test_migrate_proof 34,171 / 34,033 / 37,530 / 34,552 / 18,313, test_tenancy 31,800 / 10,173, cli.md 29,832, placement.md 6,139; round1-verdicts 11,320, which round 2 recorded only as "header + 10,098 + 954") |
| recovery | `ls scratch/tribunal-bars-0920/chunk-1a-check-r3` | 1 | allowed — "No such file or directory" → **fresh run** |
| chunk-2 stagger | `ls scratch/tribunal-bars-0920/chunk-2-check-r3` | 1 | allowed — "No such file or directory" → the chunk-2 round-3 check is not running (its tail was therefore not read) |
| CODEX PROBE | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (background) | 0 | allowed — answer `OK`, exit 0, no usage-limit text → **astra: UP** |

L74 note (recorded once): the harness put an attribution block after the prompt file's read (it asks for a `Claude-Session` line in commits and names a file-send tool). It arrived in a system-reminder outside any tool result and asks for nothing this run does (no commit, no file send); nothing was done with it.

## Packet
Folder `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/chunk-1a-check-r3/` (no `mkdir`; the first Write created it). Every file staged Read → Write. Before copying, every original was checked with `grep -c -E "[[:space:]]$"`: **0 trailing-whitespace lines** in `bars-2-fix-draft-2026-09-20.md`, prompt `25`, `cto-2026-09-20.md`, prompt `20`, `bars-chunk-1a-check-r2-2026-09-20.md`; `grep -n -E "[[:space:]]$"` = no output for the generator's `partitions.py` and 1a's `placement.py` — so every NEW file below matches its source to the byte (nothing was stripped).

**REUSED BY REFERENCE, not re-staged** (round 2's copies; sizes proven in PREFLIGHT to equal round 2's `## Packet` table): `../chunk-1a-check-r2/fix-diff.md.part1`…`part5` (the whole fix `589d40f..1404f23`; X14 is the FIRST commit, in `part1`; the 115 B of stripped whitespace round 2 disclosed is unchanged and was ACCEPTED by the desk, §47) · `fixed/` · `fix-report.md.part1`…`part3` · `fix-prompt.md.part1`/`part2` · `round1-verdicts.md` · `QUESTIONS-R2.md` · `grok-check-r2.md` · `astra-check-r2.md`.

| staged NEW file | source | bytes | check |
|---|---|---|---|
| `classify.md` | `../chunk-1a-check-r2/classify.md` WHOLE (10,052) + one header line + `reports/bars-2-fix-draft-2026-09-20.md:36` (the X14 row) | 10,671 | 10,052 + 103 (header, the offsets `grep -b` gives: header starts at 10052, the X14 row at 10155) + 516 (row `:36`: `grep -b` offsets 7069 → 7585 in the original) = **10,671** exactly · `grep -c "X14"` = 2 |
| `fix-1b-prompt.md` | `prompts/2026-09-20/25-bars-chunk-1a-fix-1b.md` WHOLE | 28,509 | original 28,509 (`wc -c`) — exact |
| `seam-call.md` | seven blocks, each headed by its real path and line: `cto-2026-09-20.md:416-423`, `:463`, `:551`; `prompts/2026-09-20/20-bars-chunk-1a-fix.md:72`; `bars-2-fix-draft-2026-09-20.md:12-24` (`## THE SEAM`); generator `child_name` `partitions.py:86-98` (git show `bars/chunk-2-0920`, branch tip when read `159f31d`; the worktree copy `/Users/cobalt/cobalt-wt/bars-chunk-2/…partitions.py:86-98` is identical); pattern `placement.py:224-288` (git show `1404f23`; the file ends at :288, so the prompt's `:290` is past the end of the file) | 11,769 | per source, `grep -n -x -F -f <staged> <source>` lists every non-blank line of each range verbatim: cto `416-422, 463, 551` · draft `12, 13, 15-22, 24` · generator `86-98` (the docstring and return line `:98`) · placement `224-288` (225-248, 250-255, 257-266, 269-288 non-blank) · prompt `20:72` |
| `round2-verdicts.md` | `reports/bars-chunk-1a-check-r2-2026-09-20.md` lines 65-167 (= `## Per FIX row` … `## ESCALATE`, contiguous) under one header line | 18,486 | my first copy had TWO transcription slips (`:122` "per-row table row" for "per-table row", `:164` "hunk, and" for "hunk and"), found by `grep -n -v -x -F -f`, fixed by Edit; after the fix the only staged lines not in the source are the header (line 1) and 12 blank lines, at staged 4, 20, 22, 39, 41, 50, 53, 80, 82, 88, 95, 103 = source 67, 83, 85, 102, 104, 113, 116, 143, 145, 151, 158, 166 (the source's 12 blanks), and the file is 104 lines = 1 + 103 |
| `QUESTIONS-R3.md` | the prompt's QUESTIONS-R3.md text (outer quotes removed) + the appended "Files in this folder:" paragraph (new files, the reused `../chunk-1a-check-r2/…` files, reference-only files, the whitespace note); each `../` path named was checked with `ls` first (`../chunk-1a-check/` holds `build-prompt.md.part1`…`3`, `owner-rulings-r19-r25.md`, `grok-check.md`, `gemini-check.md`, `astra-check.md`; `../chunk-e-check/` holds `spec-final-s3.md`, `spec-final-s8.md`) | 6,975 | — |
| `QUESTIONS-R3-GEMINI.md` | the addendum text, verbatim (outer quotes removed) | 901 | — |

Nothing needed splitting into parts (largest new file 28,509 B < 38,000 B).

Hub slips, recorded plainly (L48): (1) I typed one stray Bash call whose command was `git -C /Users/cobalt/cobalt-wt/s2-p2-cards log*` — the shell (zsh) refused it as an unmatched glob (`no matches found: log*`) and ran nothing; the prompt says never to touch the `s2-p2-cards` strings and I did not mean to. (2) One stray `grep -n -F -f …/QUESTIONS-NONE /dev/null` no-op (the file does not exist; `ugrep: error: option -f: cannot read`). Neither touched any file or worktree.

## CONTINUE
Staging done; the second `date` (DATE GATE, immediately before launch) = `Mon Sep 21 06:19:11 EDT 2026` → passes. astra: UP.
Houses LAUNCHED `Mon Sep 21 06:19–06:20 EDT 2026` (`date` = `06:20:20` after the launch), `run_in_background`, one attempt each, independent: grok (bg `bpaviw3yf`, writes `chunk-1a-check-r3/grok-check-r3.md` itself) · gemini (bg `bzyjalmou`, printed answer → I write `gemini-check-r3.md`) · astra (bg `bn6k62lci`, printed answer → I write `astra-check-r3.md`). The launch spellings are `21-…-r2.md` §2 → `14-…-check.md` §2 → `2026-09-19/01-review-harness.md` §2.1–2.3 (grok `--sandbox cobalt-job --allow "Write(…/scratch/tribunal-bars-0920/**)" -p`; gemini `--model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir … --print=`; astra `codex exec … -s read-only`), plus the prompt's sentences: gemini's names QUESTIONS-R3.md then QUESTIONS-R3-GEMINI.md and says "Read every file with your file viewer only. Run NO shell command…".
Facts checked while waiting (git only, no source read): (i) `git log --oneline 6961ee0..bars/chunk-1a-0920` = EMPTY (nothing built since round 2); `git log --stat 589d40f..bars/chunk-1a-0920` names exactly the seven paths of round 2 (`docs/40 - DevDocs/cobalt/db_migrations/placement.md`, `…/cli.md`, `src/cobalt/db_migrations/placement.py`, `…/cli.py`, `tests/cobalt/test_migrate_proof.py`, `tests/cobalt/test_tenancy.py`, `docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md`), 13 commits; (ii) `git log --oneline 589d40f..1404f23 -- src/cobalt/cards src/cobalt/radar src/cobalt/archiver src/cobalt/bars configs` = EMPTY.
LANDED (06:22 ET): **gemini** answered (bg `bzyjalmou`, exit 0; written byte for byte to `chunk-1a-check-r3/gemini-check-r3.md`, without the harness's trailing `[exited with code 0]`) — last line `CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES`; the file viewer only, no shell denial this time. **astra** answered (bg `bn6k62lci`, exit 0; its final message, printed twice by the CLI, written once to `chunk-1a-check-r3/astra-check-r3.md`) — last line `CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES`. **grok** answered (bg `bpaviw3yf`, exit 0; it wrote `chunk-1a-check-r3/grok-check-r3.md` itself — the run's stdout was only the path) — last line `CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES`. All three answered by 06:25 ET (about 5 minutes; no HARNESS, METER or TIMEOUT); no house was re-asked.
Nothing left to do: the collation below is finished and the last line of this report is the stop line. The desk reads this report; there is NO round 4 — `## FOR DEJAN` goes to him as written, one item per message; the `requires_db` first run on `cobalt_dev`, then chunk 1a's deploy prompt, then the stacked-tree gate with `bars/chunk-2-0920` (L68), are next — nothing merges before them.

## X9/X14 — one shape
The houses' own words (≤30 words per cell; line references in the houses' cells are to the STAGED parts unless they name a source file), then my file-check.

| house | X9/X14 ONE SHAPE | (i) generated at | (ii) admitted by | (iii) old `w<WW>` admitted anywhere | (iv) authority |
|---|---|---|---|---|---|
| grok | YES | sibling `child_name` return, `seam-call.md:50` (`partitions.py:86-98`); its test asserts `bars_p_20261026` (`fix-report.md.part2:227-229`) | `_PARTITION_CHILD` `fixed/placement.py:255` + `strptime` `:281-287`; admits the generator's name (`fixed/test_tenancy.py.part2:54-55`); non-Mondays admitted by named default | No: `w44/w31/w01/w53` are must-raise rows (`part2:69-72`, `:100-104`); the rest are comments and a docstring | Desk call `seam-call.md:7`, R48 `:14`, THE SEAM `:22-35`; X9's "shape NOT changed" (`:20`) is the sentence it replaced |
| gemini | YES | `bars/chunk-2-0920`'s `partitions.py:86-98` (`child_name`) | `placement.py:281-287` (`[0-9]{8}` + `strptime`); "the generator's test asserts `bars_p_20261026` (`tests/cobalt/test_tenancy.py:794`), and the pattern admits it (`test_tenancy.py:801`)" | "not admitted anywhere … (`tests/cobalt/test_tenancy.py:821-824` enforces it raises a KeyError)" | "`seam-call.md:7` and `:14` explicitly covers the change it made" |
| astra | YES | sibling `partitions.py:98`; the sibling's `tests/cobalt/test_bars_partitions.py:240` asserts `bars_p_20261026` | `fixed/placement.py:255`, real date `:282`; admits `bars_p_20261026`, tested at `fixed/test_tenancy.py.part2:54`; non-Mondays admitted deliberately (`fix-1b-prompt.md:43`) | No: `bars_p_2026w44/w31/w01/2027w53` are refusal cases (`part2:69`); the lock fixture is `bars_p_20261026` (`fix-diff.md.part1:130`); other mentions are history | `cto-2026-09-20.md:419` and `:463` via `seam-call.md`; drafter `bars-2-fix-draft:24`; `fix-1b-prompt.md:9` keeps X9's whole-name/ASCII property |

**My file-check (originals, not the staged parts):**
- (i) **HOLDS.** `git show bars/chunk-2-0920:src/cobalt/bars/partitions.py` (branch tip when read `159f31d`; identical in `/Users/cobalt/cobalt-wt/bars-chunk-2/…/partitions.py`): `:98` = `return f"{PARENT_TABLE}_{monday.astimezone(ET).strftime('%Y%m%d')}"`; the generator's own test is `tests/cobalt/test_bars_partitions.py:240` = `assert child_name(MONDAY_2026_10_26) == "bars_p_20261026"`. `child_name` is the only place a child name is generated; `placement.py` generates none.
- (ii) **HOLDS by reading (not executed).** `placement.py:255` = `re.compile(r"^bars_p_(?P<date>[0-9]{8})\Z")` (whole name via `^…\Z`, ASCII via `[0-9]`), `:278-288` = `strptime(match.group("date"), "%Y%m%d")`, `ValueError` → `None` → `side_of`'s existing `KeyError`. `bars_p_20261026` is eight ASCII digits and a real date, and `test_tenancy.py:811` asserts `side_of("bars_p_20261026") is Side.SYSTEM`. `PATTERNED_SYSTEM_TABLES` (`:263-266`) is `bars_digest` / `bars_legacy` only — no second child pattern.
- (iii) **HOLDS — count of every `w<WW>` occurrence on the branch (`grep -n -E "w[0-9]{2}|bars_p_"` on the worktree `/Users/cobalt/cobalt-wt/bars-chunk-1a/`, plus `grep -rn -E "[0-9]{4}w[0-9]{2}|bars_p_<YYYY>w"` over `src`, `configs` and the db_migrations DevDocs): the literal `bars_p_<YYYY>w<WW>` appears 3 times, all HISTORY — `placement.py:226` (comment), `tests/cobalt/test_tenancy.py:783` (comment), `docs/40 - DevDocs/cobalt/db_migrations/placement.md:83` (DevDoc). Concrete week-shaped names appear 5 times: `test_tenancy.py:826-829` (`bars_p_2026w44`, `…w31`, `…w01`, `…w53`) — all four in the REFUSED parametrize `test_the_pattern_admits_only_those_shapes` (`:853-859`, `pytest.raises(KeyError)`), none in an ADMITTED list (the admitted list `:811` holds `bars_p_20261026`, `bars_p_20240101`, `bars_p_20251229`) — and `tests/cobalt/test_migrate_proof.py:3235` (a docstring sentence "It was `bars_p_2026w31` while…", history). ADMITTED: 0. REFUSED near-miss: 4. Comment/doc history: 4.**
- (iv) **HOLDS.** The desk call and row R48 are committed on main (PREFLIGHT: `-S"the GENERATOR's Monday-date shape stands"` → `407091266786727a…`; R48 at `cto-2026-09-20.md:463` names `25-bars-chunk-1a-fix-1b.md`); X14's changes are exactly the ones prompt `25` lists (pattern, `strptime` guard, READING comment, DevDoc, tests re-pointed), plus the one flagged fourth path (see `## Assertions and boundary`).

X9/X14 one shape: **3 of 3 YES** (grok, gemini, astra — no house answered NO, and no NO holds).

## Per FIX row
X9 and X14 are round 3's answers (all three houses). X1–X8 and X10–X13: grok and astra from round 2 (`round2-verdicts.md`, marked `(r2)`), gemini from its `ROUND-2 ROW` answers in this round. No house added a `ROUND-2 CORRECTION` (grok: "No ROUND-2 CORRECTION"). Astra's round-2 X9 `NOT CLOSED` is superseded by its round-3 answer, which says of the staged authority: "This resolves my round-2 naming-contract objection."

| row | what it fixes | grok | gemini | astra | CLOSED: n of 3 |
|---|---|---|---|---|---|
| X1 | restore the joined-row-text assertion | CLOSED (r2) | CLOSED — `test_migrate_proof.py:2404-2417` | CLOSED (r2) | 3 of 3 |
| X2 | `_replaced` count difference alone refused | CLOSED (r2) | CLOSED — `:2551-2574` | CLOSED (r2) | 3 of 3 |
| X3 | per-row proof status asserted | CLOSED (r2) | CLOSED — `:2853-2868` | CLOSED (r2) | 3 of 3 |
| X4 | FROZEN_ARCHIVE refused before connect | CLOSED (r2) | CLOSED — `cli.py:1023`, `test_migrate_proof.py:2747-2795` | CLOSED (r2) | 3 of 3 |
| X5 | AMBER budget read before connect | CLOSED (r2) | CLOSED — `cli.py:1074`, `:3471-3520` | CLOSED (r2) | 3 of 3 |
| X6 | non-finite budget refused | CLOSED (r2) | CLOSED — `cli.py:688`, `:3562` | CLOSED (r2) | 3 of 3 |
| X7 | `status_of` with no probes refused | CLOSED (r2) | CLOSED — `cli.py:317`, `:2803` | CLOSED (r2) | 3 of 3 |
| X8 | round-trip digest parser reads the digest | CLOSED (r2) | CLOSED — `test_tenancy.py:690` | CLOSED (r2) | 3 of 3 |
| X9 | pattern is a complete ASCII match (kept by X14) | CLOSED — X14 supersedes X9's naming sentence, `\Z` / `[0-9]` kept | CLOSED | CLOSED — `\Z` / `[0-9]` survive in `fixed/test_tenancy.py.part2:91` | 3 of 3 |
| X10 | lock-ownership instrument: BEFORE boundary, migrate pid | CLOSED (r2; instrument, NOT RUN) | CLOSED — `:3330-3369` | CLOSED (r2; instrument, execution owed) | 3 of 3 |
| X11 | `--proof-only` observed sending no lock | CLOSED (r2; instrument, NOT RUN) | CLOSED — `:3441-3493` | CLOSED (r2; instrument, execution owed) | 3 of 3 |
| X12 | correction: `_replaced` baseline is the FIRST parameter | CLOSED (r2) | CLOSED — the 1a report | CLOSED (r2) | 3 of 3 |
| X13 | correction: "strictly stronger", "eleven green" | CLOSED (r2) | CLOSED — the 1a report | CLOSED (r2) | 3 of 3 |
| X14 | pattern admits generator's `bars_p_<YYYYMMDD>`, `w<WW>` refused | CLOSED | CLOSED | CLOSED — "X14 … CLOSED"; red `5 failed, 22 passed, 36 deselected`, then `40 passed, 23 skipped` quoted from the fix report | 3 of 3 |

No NOT CLOSED and no NEW DEFECT INTRODUCED from any house. My file-check found that gemini's `cli.py` / test line references for X4, X5 and X6 do not match the worktree (see `## Checked against the branch`); its verdicts agree with the other two houses and with round 2's file-check.

## Per not-fixed row
`row · class · grok (r2) · gemini (r3 addendum) · astra (r2)`. No house DISAGREES on any class.

| row | class | grok (r2) | gemini (r3 addendum) | astra (r2) |
|---|---|---|---|---|
| NR1 | NOT REAL | AGREE | AGREE | AGREE |
| NR2 | NOT REAL | AGREE | AGREE | AGREE |
| NR3 | NOT REAL | AGREE | AGREE | AGREE |
| U1 | UNPROVEN | AGREE | AGREE | AGREE |
| U2 | UNPROVEN | AGREE | AGREE | AGREE |
| U3 | UNPROVEN | AGREE | AGREE | AGREE |
| U4 | UNPROVEN | AGREE | AGREE | AGREE |
| U5 | UNPROVEN | AGREE | AGREE | AGREE |
| U6 | UNPROVEN | AGREE | AGREE | AGREE |
| S1 | OUT OF SCOPE | AGREE | AGREE | AGREE |
| S2 | OUT OF SCOPE | AGREE | AGREE | AGREE |
| O1 | OWNER ITEM | AGREE — "whether an empty default lock list **closes** chunk E ESCALATE 6, or only **arms** it for chunk 4" | AGREE — "What the owner would be ruling: whether an empty default lock list closes chunk E ESCALATE 6, or only arms it for chunk 4." | AGREE — "Resolving the prompt's conflicting closure language belongs to the owner…" |
| O2 | OWNER ITEM | AGREE — "whether one piped `pytest … \| tail -n 5` outside the bare-shape rule is an owner item or acceptable" | AGREE — "What the owner would be ruling: whether one piped `pytest … \| tail -n 5` outside the bare-shape rule is an owner item or acceptable." | AGREE — "Disposition of the bare-command deviation remains the owner's process decision." |

The classify.md X14 row is a FIX row, answered above; no not-fixed row was added.

## Assertions and boundary
Over X14 (commit `1404f23`) for all three houses; gemini also over X1–X13 (round-2 addendum).
- **grok (a) weaker assertions:** "NONE. No `assert` removed without an equal replacement. Admitted list stays three names … Near-miss 15 → 19, all still `pytest.raises(KeyError)` naming `placement.py` … Absence asserts re-pointed `bars_p_2026w31` → `bars_p_20261026` … Lock-phase compare stays an exact ordered list … No test skipped or marked."
- **grok (b):** "one hunk the prompt's three-path list did not name, flagged by the fixer (`fix-report.md.part3:5`)": `fix-diff.md.part1:130` (`tests/cobalt/test_migrate_proof.py`), `test_a_registered_relation_admitted_by_the_pattern_is_accepted`, fixture and expected `LOCK TABLE` `bars_p_2026w31` → `bars_p_20261026`, "Name only; ordered-list assertion unchanged." The asked-for hunks are `part1:13, :52, :60, :112, :159, :205, :256, :265`. **L52:** "NOTHING REACHES A CARD."
- **gemini (a) (b) L52 (round 3):** "ROUND-3 THIRD (a): NONE · (b): NONE · L52: NOTHING REACHES A CARD". Round-2 addendum: "ROUND-2 THIRD (a): NONE · (b): X14 (commit `1404f23`) is outside X1-X13 FIX rows. · L52: NOTHING REACHES A CARD".
- **astra (a):** "NONE. Three acceptance examples remain three; near-miss cases increase from 15 to 19 with their properties preserved. The two map-absence assertions receive equal replacements. The lock assertion remains an exact ordered statement-list comparison. No test gains a skip or other execution mark."
- **astra (b):** "`fix-diff.md.part1:130`, the `test_migrate_proof.py` fixture, expected lock statement and explanatory docstring. This fourth path exceeds the prompt's three named paths, but performs the same X14 name reconciliation without weakening the test. The fixer disclosed it at `fix-report.md.part3:5` … No other extra hunk." **L52:** "NOTHING REACHES A CARD."
- **Contradiction, both quoted, nothing smoothed:** grok and astra name a fourth-path hunk; gemini's round-3 (b) says `NONE`. My file-check: the hunk exists (`git show 1404f23 -- tests/cobalt/test_migrate_proof.py`, `@@ -3228,14 +3228,21 @@`), is outside the three paths `fix-1b-prompt.md` names (its CLOSE says "exactly three paths plus the report… ANY other path → ESCALATE with why"), and the fixer escalated it (1a report ESCALATE 2, `:1464`). grok's and astra's (b) HOLD; gemini's `NONE` does not.
- **No house found a weaker assertion or anything reaching a card.**

## Checked against the branch
Originals: the worktree `/Users/cobalt/cobalt-wt/bars-chunk-1a/` (Read/grep), `git -C /Users/cobalt/cobalt show <sha>:<path>` / `log` / `show 1404f23`, and the sibling worktree `/Users/cobalt/cobalt-wt/bars-chunk-2/` (READ only). Nothing was run — no test, no `python`.

| # | claim | who | file:line | verdict |
|---|---|---|---|---|
| 1 | The one place a child name is generated is `child_name`; its return is `f"{PARENT_TABLE}_{monday.astimezone(ET).strftime('%Y%m%d')}"` | grok, gemini, astra | `bars/chunk-2-0920:src/cobalt/bars/partitions.py:98` (tip `159f31d`); same text in the sibling worktree `:86-98` | HOLDS |
| 2 | The generator's own test asserts `bars_p_20261026` | grok, astra | `/Users/cobalt/cobalt-wt/bars-chunk-2/tests/cobalt/test_bars_partitions.py:240`: `assert child_name(MONDAY_2026_10_26) == "bars_p_20261026"` | HOLDS |
| 3 | Gemini: "the generator's test asserts `bars_p_20261026` (`tests/cobalt/test_tenancy.py:794`), and the pattern admits it (`test_tenancy.py:801`)" | gemini | `test_tenancy.py:794` is a comment line; `:801` is the `def test_a_weekly_partition_child_resolves_system`; the admitting assertion is `:811-812`; the generator's test is `test_bars_partitions.py:240` | DOES NOT HOLD as cited (line and file attribution wrong); the substance — the pattern admits `bars_p_20261026` — HOLDS at `:811` |
| 4 | `_PARTITION_CHILD = re.compile(r"^bars_p_(?P<date>[0-9]{8})\Z")` is the one child pattern; whole name, ASCII digits; real-date guard by `strptime` | grok, gemini, astra | `placement.py:255`, `:278-288` (gemini `:281-287`, astra `:255/:282`, grok `:255/:281-287` — all in range) | HOLDS (by reading; not executed) |
| 5 | The pattern admits `bars_p_20261026` | grok, gemini, astra | eight ASCII digits, a real calendar date; asserted `test_tenancy.py:811-812` (astra/grok's `fixed/test_tenancy.py.part2:54-55` = the same lines) | HOLDS (by reading; a `requires_db`-free offline test, not re-run by me) |
| 6 | The pattern deliberately admits any valid `YYYYMMDD`, not only Mondays (the named default) | grok, astra | `placement.py:243-248` (astra says `:242`, off by one); no `weekday`/`isoweekday` in `placement.py`; `fix-1b-prompt.md:43` | HOLDS |
| 7 | `bars_p_2026w44`, `…w31`, `…w01`, `…2027w53` are refusal cases | grok, gemini, astra | `test_tenancy.py:826-829` inside the `parametrize` of `test_the_pattern_admits_only_those_shapes` (`:853-859`, `pytest.raises(KeyError)` and `"placement.py" in str(...)`); gemini's `:821-824` are the comment lines just above | HOLDS (gemini's line references are off) |
| 8 | The old shape is admitted nowhere; remaining `w<WW>` text is history | grok, astra | see `## X9/X14 — one shape` (iii): 3 literal `bars_p_<YYYY>w<WW>` in comments/DevDoc, 4 concrete names in the REFUSED list, 1 in a docstring, ADMITTED 0 | HOLDS |
| 9 | Near-miss list 15 → 19 rows, admitted list stays three names | grok, astra | `git show 1404f23 -- tests/cobalt/test_tenancy.py`: old parametrize 15 names (`w00, w54, w1, 26w31, w31_old, w31x, x_bars_p_2026w31, bars_p, bars_partition, bars_digest_v2, bars_legacy_backup, user_bars_p_2026w31, \n, fullwidth, Arabic-Indic`), new 19 (`test_tenancy.py:826-850`); admitted list `:811` = 3 names (was 3) | HOLDS |
| 10 | The two map-absence assertions are re-pointed, not dropped | grok, astra | `test_tenancy.py:886` (`"bars_p_20261026" not in placement.PLACEMENT`), `:909` (`… not in system`); the removed lines were the `bars_p_2026w31` versions | HOLDS |
| 11 | The fourth-path hunk: `test_a_registered_relation_admitted_by_the_pattern_is_accepted` fixture and expected `LOCK TABLE` `bars_p_2026w31` → `bars_p_20261026`; the ordered `assert locked == [...]` is unchanged; fixer disclosed it | grok, astra | `git show 1404f23 -- tests/cobalt/test_migrate_proof.py`: `@@ -3228,14 +3228,21 @@`, relation tuple + one expected-statement line + docstring; disclosed in the 1a report ESCALATE 2 (`bars-chunk-1a-2026-09-20.md:1464`, `:1189`, `:1412`) | HOLDS |
| 12 | X14's hunk lines: `fix-diff.md.part1:13, :52, :60, :112, :130, :159, :205, :256, :265` | grok, astra | `grep -n "^@@"` on `fix-diff.md.part1` → 13, 52, 60, 112, 130, 159, 205, 256, 265 | HOLDS |
| 13 | At `beab8c7` (X9) the pattern was `…(?P<year>[0-9]{4})w(?P<week>[0-9]{2})\Z`, then X14 replaced it | grok | `fix-diff.md.part3:224` (old `\d{4}…$`), `:229` (new `[0-9]{4}…\Z`); `1404f23` changes it to `(?P<date>[0-9]{8})` (`git show 1404f23 -- placement.py`) | HOLDS |
| 14 | X14's authority: desk call and R48 | grok, astra, gemini | `cto-2026-09-20.md:419` (desk call, `seam-call.md:7`), `:463` (R48, `seam-call.md:14`); PREFLIGHT proved both committed on main | HOLDS |
| 15 | X14's red-first: `5 failed, 22 passed, 36 deselected`, then `40 passed, 23 skipped` | astra (grok: five failures quoted) | `fix-report.md.part2:244` and `:320` — quoted report text (astra cites `:234`, off by 10) | HOLDS as what the report says (L35: the report is a claim); NOT CHECKABLE FROM READS that the suite ran — run: `uv run pytest -q tests/cobalt/test_tenancy.py` |
| 16 | Gemini's round-2 line references: X4 `cli.py:1023`, X5 `cli.py:1074`, X6 `cli.py:688` | gemini | worktree `cli.py`: `_assert_frozen_archive_inactive()` call `:1064` (and `:288`), `_proof_budget_per_side_s()` call `:1097`, `math.isfinite` `:700` | DOES NOT HOLD as cited (all three off; `:317` X7 matches). The verdicts agree with round 2's file-checked rows 5–8, so I record it as a citation defect, not a claim about the code |
| 17 | NOTHING REACHES A CARD | grok, gemini, astra | `git log --oneline 589d40f..1404f23 -- src/cobalt/cards src/cobalt/radar src/cobalt/archiver src/cobalt/bars configs` → empty | HOLDS |
| 18 | `strptime` alone vs Unicode digits (grok: incidental) | grok | `placement.py:255` uses `[0-9]`, which refuses non-ASCII before `strptime` | NOT CHECKABLE FROM READS — run: `datetime.strptime("２０２６1026", "%Y%m%d")` (incidental to the verdict) |

Count: 18 claims — HOLD 15 · DO NOT HOLD 2 (rows 3, 16; both are line/file citations, both by gemini) · NOT CHECKABLE FROM READS 1 (row 18; row 15 partly).

**The facts the fix promised, stated plainly:**
(i) `git -C /Users/cobalt/cobalt log --oneline 6961ee0..bars/chunk-1a-0920` is **EMPTY** — nothing built since round 2. `git -C /Users/cobalt/cobalt log --stat 589d40f..bars/chunk-1a-0920` names exactly the round-2 seven paths: `docs/40 - DevDocs/cobalt/db_migrations/placement.md`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `src/cobalt/db_migrations/placement.py`, `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_migrate_proof.py`, `tests/cobalt/test_tenancy.py`, `docs/40 - DevDocs/reports/bars-chunk-1a-2026-09-20.md` — 13 commits (`1404f23` … `de70755`) plus the report commit `6961ee0`. **HOLDS.**
(ii) `git -C /Users/cobalt/cobalt log --oneline 589d40f..1404f23 -- src/cobalt/cards src/cobalt/radar src/cobalt/archiver src/cobalt/bars configs` is **EMPTY** (1a never touches the generator; the one place stays on the sibling branch). **HOLDS.**
(iii) Every `assert` removed in X14's test hunks has an equal replacement in the same hunk. `git show 1404f23` on the two test files: the removed `assert` lines are `test_tenancy.py`'s `assert "bars_p_2026w31" not in placement.PLACEMENT, (` and `assert "bars_p_2026w31" not in system`, each replaced by the same assertion at `bars_p_20261026` (`:886`, `:909`) — round 2's two, re-read. In `test_migrate_proof.py` the `assert locked == [...]` line itself is not removed; one list element `'LOCK TABLE "system"."bars_p_2026w31" …'` is replaced by the `bars_p_20261026` element. The other removed lines are comment/docstring text, the `for child in (...)` tuple (the loop's `assert side_of(child) is Side.SYSTEM` is unchanged) and the 15 old parametrize rows, replaced by the 19 above. **HOLDS — no `assert` is removed without an equal replacement.**

Where two houses contradict each other: (b) above (grok, astra vs gemini) — both quoted in `## Assertions and boundary`.

## Ready for a deploy prompt
| house | ready | reason verbatim |
|---|---|---|
| grok | YES | `CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES` |
| gemini | YES | `CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES` |
| astra | YES | `CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES` |

## FOR DEJAN — open after the last round
This is where the matter ends; no fourth round is drafted (L67, L39). No recommendation added.
- FIX rows NOT CLOSED by some house with a claim that HOLDS: **NONE.**
- `X9/X14 ONE SHAPE: NO` that HOLDS: **NONE.**
- NEW DEFECT that HOLDS: **NONE.**
- DISAGREE on a class: **NONE.**
- OWNER ITEMs of `classify.md`, each quoted, not summarised:

1. **O1 — RULED (his R45, 20:06 ET 09-20: "A" — armed by 1a, closed by chunk 4).** `cto-2026-09-20.md:371`: chunk 1a ships the lock-before-snapshot phase with an EMPTY default lock list; chunk E's ESCALATE 6 is NOT closed by 1a and is not a 1a defect; the CLOSURE is chunk 4's; the wording "is what step 4 closes" / `cli.md:480` "The phase closes that" is to be corrected to "arms" in the next 1a docs touch (a desk item, not a build blocker). The `classify.md` row: `| O1 | Does step 4 CLOSE chunk E's ESCALATE 6, or is it "armed, not closed"? This also covers report ESCALATE 8's "is what step 4 closes" and `cli.md:480` "The phase closes that". | grok, astra (not closed) vs gemini (closes) | row 17 HOLDS (the shipped default does not close it) · row 18 DOES NOT HOLD | `cli.py:763`, `:1020-1021`, `:1068`. Prompt 10 told the builder both "No caller supplies a non-empty list today — the swap deploy (chunk 4) is the first" (step 4) and "is what step 4 closes, and the ≥3 checkers should confirm it is closed" (ESCALATE (iv)). | **OWNER ITEM** |`
2. **O2 — carried, no ruling.** The `classify.md` row: `| O2 | ESCALATE 7: one piped `pytest … \| tail -n 5` outside the bare-shape rule. It was not denied and nothing counts on it. | astra (OWNER ITEM) vs grok, gemini (ACCEPTABLE) | N4 NOT CHECKABLE (the provenance only) | report `:645-650` | **OWNER ITEM** |`. All three houses AGREE with the class (round 2 and this round); what he would be ruling, in grok's words: "whether one piped `pytest … | tail -n 5` outside the bare-shape rule is an owner item or acceptable. Nothing in this fix counts on it."

## ESCALATE
No recommendation added.
1. **FOR DEJAN items 1–2** above (O1 RULED by R45 — carried for the record; O2 carried, unruled).
2. **A hunk outside the X14 row, HELD by my file-check:** `tests/cobalt/test_migrate_proof.py` (`@@ -3228,14 +3228,21 @@`, 13 lines: fixture name `bars_p_2026w31` → `bars_p_20261026`, the expected `LOCK TABLE` element, one docstring), a fourth path beyond `fix-1b-prompt.md`'s three; the fixer disclosed and escalated it (1a report ESCALATE 2, "round 2 should read the hunk"); named by grok and astra; gemini's round-3 (b) `NONE` does not hold. No assertion is weakened (check row 11, fact (iii)).
3. **ASK DESK, carried from the fixer's ESCALATE 1 (verbatim):** "the placement pattern admits any valid YYYYMMDD, not only Mondays — the weekday rule stays in the generator (L3). Tighten it here as well? [20:43 ET]" — safe default taken by the fixer: as built, not tightened. Grok and astra both accept it as the prompt's named default; no house raised it as a defect.
4. **The `requires_db` tests are still unrun and OWED** — the first run on `cobalt_dev` before deploy (round 1's four plus the three pre-existing; this fix wrote or changed 0 of them). Two houses record it as NOT CHECKABLE FROM READS, not a defect (L70).
5. **The stacked-tree gate (L68) with `bars/chunk-2-0920` is the desk's and is NOT done:** the seam is closed in the repo (each side read from the other's file), not on the tree that lands; `bars/chunk-2-0920` sat at `159f31d` when I read it, and `placement.py` is a file both branches touch. Not asked of the houses.

Not escalated, recorded: no `NOT CLOSED`, `NEW DEFECT`, `FIX AGAIN` or class DISAGREE from any house; no L52 finding; no weaker assertion my file-check HOLDS; no packet mismatch; every house checked (3 of 3); no `ASK DESK` of mine; the two stray no-op calls I made are disclosed in `## Packet`.

BARS CHUNK 1A CHECK R3 DONE · grok: CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES · gemini: CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES · astra: CHECK R3: FIX STANDS · X9/X14 one shape: YES · ready for its deploy prompt: YES · houses that checked: 3 of 3 · FIX rows CLOSED: 14 of 14 · new defects: 0 · ready for a deploy prompt: 3 of 3 · X9/X14 one shape: 3 of 3 YES · ESCALATE: 5
