# DRC D3 re-point draft — 2026-09-29 (drc-d3-repoint-draft-0929)

## §0
- Re-pointed `10` / `11` in place to the D2 fix r2 tip: branch `f52ed883`, code `6ebfe634`.
- The seam is now the fix r2 report's `## SEAM FOR D3` + `## FOR D3` symbols line: 12 of 12 lines carried verbatim (`grep -x -F -f`).
- The D2 gate is re-pointed to `58`'s real line (`defects that HOLD: 4` · `ready for D3: NO`) plus his 09-29 R1 (1) override. `58`'s four HOLDs are now `10`'s rows 0a–0d, and `11` checks them.
- Launch lines are byte-identical to HEAD, with no new strings. The placeholder count is 1 per file, in AUTHORIZATION. ESCALATE: 8.
- Nothing was launched or committed. I wrote the two files and this report.

## FACTS
Authorization (05:32 ET, `date`): `git -C /Users/cobalt/cobalt log --oneline -3 -- "docs/40 - DevDocs/reports/cto-2026-09-29.md"` → `5b726863`, `87809ea7`, `0740eb4c`. `grep -n -F "| R6 |"` → row 14, which names `prompts/2026-09-29/01-draft-drc-d3-repoint.md`. `grep -n -F "| R1 |"` → row 9, which carries `"A,A"` and `D2 counts as checked`. `git log -1 -S"D2 counts as checked"` → `0740eb4c`. Words: `cto-2026-09-29-words.md` `## R1` → `> A,A`.
- Tip: `git -C /Users/cobalt/cobalt log --oneline -3 drc/d1-trading-log` → `f52ed883` (fix r2 report) · `6ebfe634` (fix r2 code) · `963903a3` (with-DB red). This matches the desk's 05:3x read.
- Code: `git -C /Users/cobalt/cobalt log --oneline 6ebfe634..drc/d1-trading-log -- src tests configs` → empty. `log --stat 6ebfe634..drc/d1-trading-log` → one path, the fix r2 build report.
- Main tip: `git -C /Users/cobalt/cobalt log --oneline -1 main` → `e6546cdc`.
- Ahead: `git -C /Users/cobalt/cobalt log --oneline main..drc/d1-trading-log` → 82 lines. Behind: `drc/d1-trading-log..main` → 148 lines.
- Migrations (`git show 6ebfe634:src/cobalt/db_migrations/__init__.py`, `grep -n`): `0019_drc_events` is last, with FORWARD `:133` and REVERSE `:138`. `0018` moved to FORWARD `:132` and REVERSE `:139`. Docstring: `0018` `:62`, `:66`, `:80`; `0019` `:69`, `:74`, `:81`. `placement.py`: `0018` `:98`, `0019` `:101`. D3's `0020` is next, per the seam and R64 (5).
- Counts (fix r2 report on the branch): F6 live-note `146 passed, 1 skipped` (`:109`). F7 offline `3561 passed, 552 skipped, 1 xfailed` (`:112`). F8 with-DB `4096 passed, 6 skipped, 9 deselected, 3 xfailed` (`:117`). F8 (c2) probe `assert 28 == 34`, short by 6 (`:118`). F6–F8 record no `<F0>`–`<F3>` fingerprints, and `10` / `11` carry none (`grep -c -F "<F0>"` → 0 each).
- With-DB deselect set: the eight arguments, which select nine tests (`:115`). Lines by `git show 6ebfe634:<file>` + `grep -n -F "def <name>"`: `test_tenancy.py` `:701`, `:714`, `:263` (class `:692`) · `test_migrate_proof.py` `:306` · `test_voice_store.py` `:216`, `:233`, `:258` (were `:215`, `:232`, `:257`) · `test_voice_confirm.py` `:218` · `test_voice_lifecycle.py` `:137`.
- Anchors at `6ebfe634` (`git show` + `grep -n -F`). Moved: `drc/cli.py` `def add_parser` `:196` → `:216`, plus the `__init__.py` and `placement.py` lines above. Unmoved: `writer.py` `:673` / `:588` · `src/cobalt/cli.py:512` · `prefill/config.py:151` · `vault_loader.py:91` · `runner.py:483` · `line.py:60` · `pyproject.toml:68` · `jobs.yaml` `:199`, `:328` · `s2.yaml` `:545`, `:547` · `0018_drc_stated_books.sql:61`–`:63` · `vault.py:155`. `git diff --stat 7cdc5774 6ebfe634 -- src configs ops pyproject.toml` touches only `drc/{cli,imports,store}.py`, `db_migrations/{__init__,placement}.py`, `0019*.sql` and tests.
- Rows 0a–0d re-read on `6ebfe634`. The guard `if note is None or not str(note):` is at `imports.py:573` / `:722`, with its `raise` at `:574` / `:723`. The F-11 notes are at `:814`–`:820` (line `:818`). The F-10 stubs `lambda event: None` are at `test_drc_d2_fix_r2.py:42` and `test_drc_d2_fix_r2_db.py:59`. RUN-5 is at `test_drc_d2_fix_r1_runs.py:218` / `:224`. F-6's control is at `test_drc_d2_fix_r2_db.py:113`–`:115`. The old `returns` assertions are at `test_drc_d2_fix_r1_db.py:262`–`:263`, and the new ones at `:264`–`:266`. In the `_Drc` double, `record_screenshot` supersedes by trade key (`test_drc_imports.py:99`–`:113`).
- RESTARTS (fix r2 report `:122`): `b86271f9..6ebfe634` → `com.cobalt.aset com.cobalt.radar`. Carried: the branch's own `10163d51..84827649` RESTARTS is widened by the UNCLASSIFIED `.clinerules` row and is OWED to the DRC deploy (R74).

## CHANGES
Line numbers are those of the new files. Bytes: `10` 69846 → 91010 (+21164: 12 carried seam lines, rows 0a–0d, the D2 gate lines). `11` 48890 → 53973 (+5083: rows 0a–0d in the packet, rows list and QUESTIONS). The placeholder is 1 per file, as at HEAD (`10:83`, `11:18`).

| file · line | what | why |
|---|---|---|
| 10 · 1 | header `RE-POINTED 2026-09-29 …`; DESK LINE (2) `57` / `58` stopped; (3) `58`'s `HOLD: 4` · `ready for D3: NO` + R1 (1) grep; (4) home from the seam of record; FILL sentence notes the re-point filled D2's values | items 9, 3, 1 |
| 10 · 3, 5 | title adds the four HOLDs; BASE `f52ed883`, code `6ebfe634` (FILL tokens replaced), 82 ahead / 148 behind `e6546cdc` | items 1, 4 |
| 10 · 15 | `writer.py:673` at `6ebfe634` | item 1 |
| 10 · 27–39 | D2 seam bullet re-pointed to the fix r2 report `:124`–`:136` / `:149`–`:151` (supersedes fix r1 and D2 build); 11 seam lines + the FOR D3 symbols line carried verbatim | item 2 |
| 10 · 40 | THE RETURN GUARD'S TRUE LINES (`:573` / `:722` vs `:574` / `:723`) | item 4; ESCALATE 3 |
| 10 · 41 | X-NT home FILLED from the seam of record (`drc_events` via `no_trade_event`, `:131`) | item 1; ESCALATE 4 |
| 10 · 42 | `cli.py:196` at `7cdc5774` → `cli.py:216` at `6ebfe634` | item 1 |
| 10 · 49–52 | rows 0a–0d before D3-1 | item 4 |
| 10 · 61 | D3-M: `__init__.py` `0018` `:132` / `:139`, `0019` `:133` / `:138`, docstring `:69` / `:74` / `:81`; placement beside `0019`'s `:101` | item 1 |
| 10 · 65 | NOT IN D3: D2 except 0a's two lines; RUN-1 / RUN-2 the desk's | item 4 |
| 10 · 68 | index card L75: rows 0a–0d classified (K2) | item 4 |
| 10 · 71, 74 | card (4): the fix r2 report sections; on main `58` `## FOR DEJAN` + R1; card (6): 0a–0d code / test ranges | items 2, 4 |
| 10 · 82 | AUTHORIZATION: 09-29 R1 bullet (grep + `-S` commit) | item 7 |
| 10 · 83 | placeholder row's file `cto-2026-09-28.md` → `cto-<D>.md`; a re-point row (R6) never counts | item 1 (stale path); placeholder unmoved |
| 10 · 86 | UNATTENDED: the ONE `imports.py` exception (0a) and 0a–0d's named test edits | item 4 |
| 10 · 90 | report `## E4 THE ROWS` lists `0a` … `0d` first | item 4 |
| 10 · 102 | PREFLIGHT base chain: the fix r2 BUILT line and `58`'s stop line verbatim (FILL tokens replaced); gate = R1 override; `6ebfe634..` range | items 1, 3 |
| 10 · 107 | PREFLIGHT greps: the eight seam symbols with lines, 0a's guard, `add_parser` `216`, `0018` `132` / `139` (docstring `:80`), `0019` `133` / `138` | items 1, 2 |
| 10 · 108 | read the fix r2 `## SEAM FOR D3` / `## FOR D3` / `## ESCALATE` and `58`'s `## FOR DEJAN` | item 2 |
| 10 · 113, 115 | E0: offline `3561/0`, with-DB `4096/0` (FILL tokens replaced), live-note `146` | item 1 |
| 10 · 129–131 | E2: 0a–0c offline halves + 0b's control; run + commit files; expected reds | item 4 |
| 10 · 136–138 | E3: 0a / 0b / 0d with-DB halves and controls; run + commit files | item 4 |
| 10 · 142–146 | E4: 0a first; its two-line diff proof + seam re-grep; stat list; `imports.py` out of the EMPTY list | item 4 |
| 10 · 151 | feat commit message names 0a–0d | item 4 |
| 10 · 163 | E7 `<DS>` source → fix r2 F8 `:115`–`:117`; `test_voice_store.py` `:216` / `:233` / `:258` | item 1 |
| 10 · 165 | E7 not-skipped list adds `test_drc_d2_fix_r2_db.py`, `test_drc_d2_fix_r1_db.py` | item 4 |
| 10 · 166 | probe: executed record `28 == 34` (fix r2 F8 `:118`) replaces the derived text | item 1 |
| 10 · 171 | RESTARTS: fix r2's `aset` / `radar`; the `.clinerules` caveat carried | items 1, 6 |
| 10 · 173, 177–178 | FOR K3: D2's = the fix r2 report's `:138`–`:147`; 0a–0d bullet | items 2, 4 |
| 10 · 182 | CLOSE (xi) 0a–0d + RUN-1 / RUN-2; standing line: stacks on `6ebfe634` by R1 (1) | item 4 |
| 11 · 1 | header; LAW STEP: D2 via `58` + R1 (1), base `f52ed883` / code `6ebfe634`; checks 0a–0d | items 9, 3, 5 |
| 11 · 3, 7, 9 | title; the build text; the round's question includes 0a–0d | item 5 |
| 11 · 17 | AUTHORIZATION: 09-29 R1 bullet | item 7 |
| 11 · 18 | placeholder row's file → `cto-<D>.md`; R6 never counts | item 1 |
| 11 · 23 | card (2): rows 0a–0d + `58`'s `## FOR DEJAN` / rows 1–4 | item 5 |
| 11 · 47 | L72: the seam of record is the fix r2 report's | item 2 |
| 11 · 59 | path union: 0a's `imports.py` + 0a–0d's test edits; `imports.py` diff = the two guard lines, recorded | item 5 |
| 11 · 77 | code-at-tip: 0a–0d's code and test slices | item 5 (K4) |
| 11 · 80 | deselect lines `:216` / `:233` / `:258` | item 1 |
| 11 · 82 | seam.md: the fix r2 report path, `## SEAM FOR D3` / `## FOR K3` / `## FOR D3` | item 2 |
| 11 · 83 | rules.md: 09-29 R1 row; `58`'s `## FOR DEJAN` + rows 1–4 verbatim | item 5 (K4) |
| 11 · 90–95 | QUESTIONS: the chunk closes 0a–0d first; FIRST covers 0a–0d with `58`'s four clauses verbatim | item 5 |
| 11 · 114, 127, 130, 137 | SCOPE allows 0a's two lines; `## Per row` lists 0a–0d; (i) boundary without `imports.py` + its record; FOR THE CLASSIFIER rows | item 5 |

Carried, not stale: `10:1` and `11:1` keep the 09-28 headers, NAMING, and `42`'s `0019` / `0020` history. `10:61` keeps `42`'s rollback contract and `32`'s proof shape (the migration's source of record, unchanged by fix r2). `11`'s D3-output FILL tokens (`:56`, `:58`, `:59`) stay the desk's. Seats and models are unchanged (`10` `claude-opus-5-5`; `11` hub `claude-sonnet-5-5`, Opus 5.5 + Grok).

## SEAM PROOF
Source: `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-d2-fix-r2-build-2026-09-28.md` lines 126–136 (`## SEAM FOR D3`, every bullet) and 151 (`## FOR D3`'s symbols line). Line 125 is the section's own supersession sentence. It is re-stated in `10:27`, and line 150 is the desk's re-point instruction, applied here.
- `grep -c -x -F -f <(sed -n '126,136p;151p' <source>) 10-drc-d3-build.md` → `12`.
- `grep -n -x -F -f …` → `10:28`–`:39`, one hit per line, in source order. A per-line `grep -q -x -F` loop printed 12 × `HIT`.
- It was re-run after the last edit → `12`.

Seam lines carried: 12 of 12.

## FIRST ROWS
As written at `10:49`–`:52`. Each row gives its class, the clause verbatim, ONE reading, `file:line` on `6ebfe634`, red first, done-when and its E-step.
- **0a** (defect; E2 + E3 red, E4 fix first). `58` `## FOR DEJAN` 1: "a build returning `Path("")` stores `"."` and lands `done`, because `str(Path(""))` is `"."`. A whitespace-only string also lands `done`."
  - Fix: the guard at `imports.py:573` / `:722` becomes `if note is None or not str(note).strip() or str(note) == ".":`, edited in place.
  - Red first: new tests over `Path("")` / `"   "` on both day types offline, plus one with-DB. On the base they give `('done', None, '.')`.
  - Done when: `failed` with `NO_NOTE_PATH`, and the `imports.py` diff is exactly those two lines.
- **0b** (weak assertion; E2 + E3 pin and control). `58` 2: "F-10's empty-string branch (`not str(note)`, `imports.py:573`, `:722`) is exercised by no test; every stub returns `None`."
  - Change: `""` joins 0a's parametrize.
  - Control: remove ` or not str(note)` → red for a named reason → restore → `git diff --stat HEAD -- src` EMPTY.
- **0c** (weak assertion; E2 pin and control). `58` 3: "F-11's only assertion is `"shot.png" in page` … No test asserts the notes line's text, its trade key, or the `current` filter".
  - Change: assert the exact `:818` line in `day_view(D).notes` and on the page. A second `record_screenshot` with the same key supersedes `shot.png`, and only `shot2.png` is listed.
  - Control: the old assertion passes where the new one fails.
- **0d** (weak assertion; E3 pin and control). `58` 4: "F-6's control … only compares constants against the stored hashes. It never shows the forged copy passing the old assertions."
  - Change: the old (`:262`–`:263`) and new (`:264`–`:266`) assertions become two helpers. The control runs both on `forged`: the old pass, and the new fail per field.
  - Red once: a `forged` copy with the stored hashes → `DID NOT RAISE`.

## RULE PROOF
Method: the launch line is the text from `claude --bg` to the closing `--add-dir /Users/cobalt/cobalt-wt` of line 1, taken from the file and from `git -C /Users/cobalt/cobalt show HEAD:<path>` and compared as strings.

| file | result |
|---|---|
| 10 | identical (1064 B, 94 tokens); `--model claude-opus-5-5` |
| 11 | identical (908 B, 77 tokens); `--model claude-sonnet-5-5` (already R118's id; no change) |

NEW strings: none.

## ESCALATE
1. ASK DESK: row 0a edits D2's source, `imports.py:573` / `:722`, in place. `10` otherwise forbids `imports.py`, and `11` checks it EMPTY; both now carve out exactly those two lines.
   - Reading A (written): this does not move a D2 seam. It makes the code meet the seam of record's own return contract ("`None` or an empty path lands the event `failed`"), and no symbol, signature or line moves. `10`'s E4 re-greps the eight symbols and fails the run on a moved line.
   - Reading B: K3's safe default, a test-only row that pins `Path("")` → `done` as a known red.
   - Default: A, as the prompt's 0a states ("then the fix"). [05:44 ET]
2. Seam lines whose meaning fix r2 changed from fix r1, as opposed to only a line number. Default: the fix r2 report, as carried verbatim in `10:28`–`:39`.
   - (a) THE ONE entry: fix r1 read "its return value is the note path". Fix r2 reads "returns a NON-EMPTY note path; `None` or an empty path lands … `failed`" (F-10).
   - (b) THE SCREENSHOT BINDINGS: fix r1 read "RUN-5, red: … listed nowhere". Fix r2 reads "a not-computed day lists each current binding in the page's notes (F-11, `:818`)".
   - (c) RUN-1 / RUN-2: fix r1 put them under `## FOR D3` as "also for D3". Fix r2 makes them a seam line, "OPEN … the desk's items, not D3's to fix". `10:65` names them out of D3.
3. Line cites the sources and `git` disagree on. Default: git's lines in the new text, with the sources' text carried verbatim.
   - The seam of record gives the guard as `:574` / `:723` (the `raise` lines). `58` and `git` give the condition at `:573` / `:722`. Both are stated at `10:40`.
   - `58` gives the `None` stubs at `test_drc_d2_fix_r2.py:44` / `test_drc_d2_fix_r2_db.py:60`; `git` gives `:42` / `:59`.
4. ASK DESK: `10`'s seven D2-side `«FILL AT LAUNCH»` tokens were filled from the built facts. They were the base / code tip, the X-NT home, the D2 BUILT and CHECK lines, and the offline and with-DB counts. The line-1 definition and the gate line remain.
   - Reading A (written): they are built facts from the source of record, and the gate must name `58`'s real line (item 3 of the prompt).
   - Reading B: leave them for the desk at launch.
   - The desk re-reads them at launch; PREFLIGHT's `git log -1` fails a moved tip. [05:44 ET]
5. `<F0>`–`<F3>`: the fix r2 report's F6–F8 record no migration fingerprints (F8 records the absence probe), and `10` / `11` carry no `<F>` token. Nothing was re-pointed; the last recorded values are `42`'s, at `0018`.
6. Carried, never resolved: the branch RESTARTS is widened by the UNCLASSIFIED `.clinerules` row and is OWED to the DRC deploy (R74). See `10:171`.
7. L74: a harness `system-reminder`, attached to the first tool result, asked for a `Claude-Session:` trailer and named `SendUserFile`. It is recorded once here and was not followed. I made no commit and sent no file.
8. Tools: I used read-only `sed -n`, `awk`, `cut`, `tr`, `for` / `while` loops and process substitution over the files and `git show`, beyond the seven precedented strings. There was no repo write except the Edit / Write tools on the two files and this report, and no tmp file.

## CONTINUE
None. The desk verifies the two files (L35), then launches `10` after `24` frees the `cobalt_dev` lock (L76).

DRC D3 REPOINTED · files: 2 · tip: f52ed883 · code: 6ebfe634 · seam lines carried: 12 of 12 · first rows: 4 · new rule strings: 0 · ESCALATE: 8
