JOB: rules-cut-dayopen-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-dayopen-1013
WORKTREE: rules-cut-dayopen-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-dayopen-1013/docs/40 - DevDocs/reports/rules-cut-dayopen-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-dayopen-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` R1341, R1344; direction file `## RULED 2026-10-13 — the rules cut list, all of it`). Map C10 (row 393): `DAY-OPEN-QWEN.md:5` tells the local seat to write its report with its file-write tool; L49 (FROZEN) wins: the local seat writes only through a Cobalt command. Map S21 (rows 392, 393): the S1-S7 fallback and "(after 2026-09-15 it is)" are stale since `cobalt day-open` shipped (the S0 path). `Q` = `docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md` at HEAD. Every quoted text is byte for byte.

| row | what | red first | files |
|---|---|---|---|
| Q1 | C10: `Q:5` `Report path: \`docs/40 - DevDocs/reports/day-open-DATE.md\` — write it with your file-write tool, print the VERDICT table last, stop.` becomes `Report path: \`docs/40 - DevDocs/reports/day-open-DATE.md\` — the S0 command writes it; you write no file (L49); print the VERDICT table last, stop.` | NEW `tests/ops/test_rules_cut_dayopen.py` on the real file: `file-write tool` occurs zero times; the new `:5` text once. RED on BASE: `file-write tool` once | `docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md`, `tests/ops/test_rules_cut_dayopen.py` (NEW) |
| Q2 | S21: `Q:7` `## S0 — is the day-open command available? (after 2026-09-15 it is)` becomes `## S0 — the day-open command`; `Q:9` ` STOP — skip S1–S7.` at its end becomes ` STOP.`; `Q:10` `If it fails: continue with S1–S7 below.` becomes `If it fails: print \`FAILED: S0 — <the exit code and the first error line>\` and stop; the desk reads the missing report (L1, L49).`; `Q:12`-`Q:25` (`## S1 radar resident` through the `## S7 archiver` command line) and the blank line `Q:26` after them are deleted | same test: `S1–S7`, `## S1 `, `## S7 `, `launchctl print` and `after 2026-09-15` occur zero times; `Q:8` (`\`COBALT_ENV=production uv run cobalt day-open --help\``) and `Q:9`'s two commands equal BASE's. RED on BASE: each occurs. `tests/ops/test_needs_his_hand.py` `test_nothing_else_changed` pins the file at 30 lines (`:25`): `LINE_COUNT`'s `"DAY-OPEN-QWEN.md": 30` becomes `15` (RED on BASE once changed); `test_the_section_sits_where_the_text_puts_it` (the shape line right after `Table: check \| verdict`, the last line `/no_think`) stays green unchanged | same files, `tests/ops/test_needs_his_hand.py` |
| Q3 | `Q:28` `Last line: \`NEXT: the desk reads this report and states the plate.\` Write the report, print the table, stop.` becomes `Last line: \`NEXT: the desk reads this report and states the plate.\` Print the table, stop.` | same test: `Write the report` occurs zero times. RED on BASE: once | same files |
| Q4 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line (expected none) | — (output quoted) | none |

## NOT IN THIS JOB
- `Q:29` (`## NEEDS HIS HAND`, "append it to the file the command wrote"): it is also a direct file write (L49), but it carries his 2026-10-12/13 hand-by-day ruling and no Cobalt command writes that section; it stays, and the conflict is the desk's item (DECISIONS 8 of the draft report: a `cobalt day-open` change is `src/`, outside K5).
- `Q:1` (the MODEL line), `Q:3`, `Q:30`; the `~/.qwen/settings.json` allowlist (his).
- `src/cobalt/` (`cobalt day-open`); any file under `/Users/cobalt/Vault`; any `ops/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md` whole (30 lines).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` C10, S21; rows 392-394.

## CHECK ASKS
- X1 Does any line still have the local seat write a file itself, but `Q:29`?
- X2 Is the S0 path (`Q:8`, `Q:9`'s commands) byte for byte BASE's, and does the file still tell the seat what to do when S0 fails?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "file-write tool" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md"` · before `1` · after `0`
- `grep -c -F "## S1 radar resident" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md"` · before `1` · after `0`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:20-07:45 ET, at `main` HEAD `7516154c`; the prompts folder clean but one untracked dated prompt.
- `git show HEAD:"docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md"` whole (30 lines): `:1` MODEL, `:3` title, `:5` INDEX CARD with `write it with your file-write tool`, `:7` `## S0 — is the day-open command available? (after 2026-09-15 it is)`, `:8` the `--help` probe, `:9` `If exit 0: … STOP — skip S1–S7.`, `:10` `If it fails: continue with S1–S7 below.`, `:12`-`:25` S1-S7, `:27` `## VERDICT`, `:28` `… Write the report, print the table, stop.`, `:29` NEEDS HIS HAND, `:30` `/no_think`.
- `grep -rn -F "DAY-OPEN-QWEN"` of `tests` and `src/cobalt/cli.py`: one test reads the file, `tests/ops/test_needs_his_hand.py` (`:19`, `:25` `LINE_COUNT … "DAY-OPEN-QWEN.md": 30`, `:76-79`, `:94`); no code reads it.
