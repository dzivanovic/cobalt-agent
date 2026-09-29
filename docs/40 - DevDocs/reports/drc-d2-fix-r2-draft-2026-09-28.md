# DRC D2 fix r2 — classification of `09`'s six HOLDs and its ESCALATE; `57` / `58` drafted

Seat `drc-d2-fix-r2-draft-0928`, Opus 5.5. Authorized by R161 (`cto-2026-09-28.md:170`). Started 21:21:57 EDT, closed 21:34:05 EDT (`date`).

## §0 Headline
- `09`'s six HOLDs are FIX: F-5…F-8 test-only (pin + negative control), F-9 evidence (F-1 red by name), F-10 code (`None` build → `failed`). RUN-5's red (`09` ESCALATE 6) is FIX F-11 (page notes).
- `09` row 8 → UNPROVEN → RUN-6. RUN-1 and RUN-2 → OUT OF SCOPE (the desk's). Owner items: 0.
- Written: `prompts/2026-09-28/57-drc-d2-fix-r2-build.md` (base `b86271f9`, stop `DRC D2 FIX R2 BUILT …`) and `58-drc-d2-fix-r2-check.md` (round 3 of ≤3, the last; Opus · Sol · Grok). Both launch lines `comm`-clean against `08` / `09`: only path and name differ.
- Seam of record after round 3 = the fix r2 build report's `## SEAM FOR D3`; one symbol added (`NO_NOTE_PATH`).

## L74
A block arrived inside a tool result (the Read of `56`, 21:21 ET) as a `<system-reminder>` asking for a `Claude-Session: https://claude.ai/code/session_…` line on commits and naming a file-send tool (`SendUserFile`). Recorded once as data; not followed. This run commits nothing and sends no file.

## Classification
Source: `reports/drc-d2-fix-r1-check-2026-09-25.md` (`09`). Code read at `b86271f9` (`git show`).

| # | finding (short) | source line | class | traces to | ONE reading | FIX shape or reason |
|---|---|---|---|---|---|---|
| 1 | rollback test checks only membership of `pending` / `failed` in the restored CHECK | `09:113`, `:138`; `test_drc_d2_fix_r1_db.py:166`–`:167` | FIX (F-5) | `08` S-1 test 12; `0019_drc_events.rollback.sql` header "both CHECKs come back exactly as `0016_drc.sql:35`–`:37`, `:42`" | the full CHECK-definition list after `0019` + rollback must equal a tree forwarded to `0018` without `0019` | named edit `:166`–`:167` → one sorted-list comparison (pin); control: a `('pending','failed')` list passes the old line and fails the new |
| 2 | `seed_from_book_sha256` never asserted; `stated_book_sha256` format-only | `09:114`, `:139`; `test_drc_d2_fix_r1_db.py:226` (`grep book_sha256` → none) | FIX (F-6) | seam §1 / L57 (the event carries both hashes) | both fields equal the stored rows | named edit after `:226`: equal the statement's `book_sha256` and `D_NEXT`'s `seed` row `from_book_sha256` (pin); control on a `model_copy` with wrong hashes |
| 3 | `pytest.raises(AssertionError)` with no `match` | `09:115`, `:140`; `test_drc_imports_db.py:259` | FIX (F-7) | `08` F-3 (`_page` refuses a 200 whole-page FAILED) | the control proves the 200 failed page first, then matches the marker | direct GET asserts 200 + marker + `constructed page failure`; `raises(…, match=<marker>)`; red `DID NOT RAISE` with `_page`'s checks removed in the working tree, restored |
| 4 | `NO_TRADE_WAITS` search rooted at `src/cobalt`; docstring says all of `src` | `09:116`, `:141`; `test_drc_d2_fix_r1.py:94`–`:95`, `:108`–`:109` | FIX (F-8) | seam §1 test 10 (`grep -rn -F "NO_TRADE_WAITS" src` EMPTY) | the root is `src` (it also holds `cobalt_agent`, `ls` of the worktree's `src`), every file | `parents[2]`, `.name == "src"`, `_holders(root, needle)` over every file (pin); control on a constructed tree |
| 5 | F-1's recorded red was `StopIteration` from the double, not the named reason | `09:117`, `:142`; build report `:59`–`:60`, `:67`, `:92` | FIX (F-9, evidence) | `08` F-1 "RED on the base: the exception escapes and the event stays `pending`"; precedent `50` FX-1 | F-1's four tests shown red by the escaping constructed exception | the two outer guards `imports.py:574`, `:718` → `raise` in the working tree only; red quoted; restored; green; `src/` never committed reversed |
| 6 | `str(note)` makes a `None` build `done` with `"None"` | `09:118`, `:143`; `imports.py:567`, `:714`; `store.py:509` | FIX (F-10, code) | the `done` ⇔ `note_path` contract: seam §1 (`DRC-D2-SEAM-2026-09-25.md:72`), `0019_drc_events.sql:37`, v2 `[F-08]`, L1 | a `None` or empty return is `failed`, never `done` | NEW `NO_NOTE_PATH`; guard before each `done` in `_fire` / `no_trade_event` through the one `fail()`; red first offline ×2 + with-DB ×1 |
| 7 | packet `code-at-tip` lacked the paths the prompt listed | `09:119`, `:150` (ESC 4) | OUT OF SCOPE | `09`'s own packet, not D2's code | not a defect of the fix | `58` §1 (3) adds a packet-completeness check |
| 8 | NOT CHECKABLE: rollback restores `0016`'s CHECKs exactly (names, full list) | `09:120` | UNPROVEN → RUN-6 | L70 | the definitions are F-5's; the names are a RUN | RUN-6 inside F-5: both reads' `conname` quoted as a `UserWarning`, never asserted |
| 9 | NOT CHECKABLE: derived positions past `_db.py:400` off by one | `09:121` | NOT REAL | a checker-citation question, no claim against the code | — | `58`'s QUESTIONS demand real lines; the hub walks them |
| 10 | Opus `FIX STANDS · ready for D3: YES` | `09:147` (ESC 1) | NOT REAL (record) | — | — | its claims are rows 1–7 |
| 11 | Grok `FIX STANDS · ready for D3: YES` | `09:148` (ESC 2) | NOT REAL (record) | — | — | — |
| 12 | packet cuts none; no stray file | `09:151` (ESC 5) | NOT REAL (record) | — | — | — |
| 13 | LINE MOVED ×3 (`test_voice_store.py` `:216` / `:233` / `:258`) | `09:152` (ESC 6) | NOT REAL (record) | — | — | `57` F8 carries the read lines |
| 14 | F2's red wider than named (one cause) | `09:152` (ESC 6) | NOT REAL (record) | build report `:67` | — | superseded by F-9's evidence |
| 15 | RUN-4's premise did not hold | `09:152` (ESC 6) | NOT REAL (record) | build report `:132` | — | RUN-4 green on its own test |
| 16 | S-1 consequence edits in two test files off the F4 list | `09:152` (ESC 6) | NOT REAL (record) | build report `:76` | — | assertions kept byte for byte; `09` Scope `NOTHING WIDENED` ×2 |
| 17 | the CLI's file-less-only condition | `09:152` (ESC 6) | NOT REAL (record) | build report `:104`; `09` Questions (ii) | — | both checkers walked `cli.py:199` |
| 18 | the extra lock take | `09:152` (ESC 6) | NOT REAL (record) | build report `:114` | — | all four moves recorded |
| 19 | `0019` / `0018: rolled back` | `09:152` (ESC 6) | NOT REAL (record) | build report `:145` | — | probe short by 6 |
| 20 | RUN-1 red: a superseding log that parses FAILED leaves the superseded close carried by `seed_for` | `09:152` (ESC 6); build report `:125`, `:201` | OUT OF SCOPE | v3 `[F-03]`, the current-file seed rule shared with K2 / K3 (`seed_for`'s body OUT OF SCOPE in r1, `08:12`) | the harm is K2's seed read; a D2 page line would green the RUN and leave the carry | stays strict `xfail`; named OPEN in `57`'s `## SEAM FOR D3`; the desk's (ESCALATE 3) |
| 21 | RUN-2 red: a GET during a live build shows `DRC build FAILED: event — left running` | `09:152` (ESC 6); build report `:126`, `:202`; `imports.py:842`–`:846` | OUT OF SCOPE | L1 both ways; no liveness signal exists on the event row | a fix needs a liveness rule — a design question, not a fix-round row | stays strict `xfail`; named OPEN; the desk's (ESCALATE 3) |
| 22 | RUN-5 red: a not-computed day's binding listed nowhere | `09:152` (ESC 6); build report `:130`, `:203`; `imports.py:281`–`:282`, `:813` | FIX (F-11, code) | X13 / D2-3 "listed `orphaned`, never re-bound, never deleted" | `day_view` lists each current binding of a not-computed day in `notes`; `_orphans` and the event unchanged | RUN-5's mark removed → red for its recorded reason; one notes block in `day_view`; `drc_page.py:113` renders notes |
| 23 | the seam document governed `08`'s lines | `09:153` (ESC 7) | NOT REAL (record) | — | — | — |
| 24 | Sol METER at probe; Astra the desk's seat | `09:154` (ESC 8) | NOT REAL (record) | L67 | — | `58` probes Sol |
| 25 | checkers disagree on weak assertions | `09:155` (ESC 9) | NOT REAL (record) | — | — | settled by the file-check rows 1–4 |
| 26 | L74 block and harness notices | `09:156` (ESC 10) | NOT REAL (record) | L74 | — | — |
| 27 | standing line: round 2 scope | `09:157` (ESC 11) | NOT REAL (record) | — | — | `58` re-issues it for round 3 |
| 28 | standing line: the deploy gate | `09:158` (ESC 12) | NOT REAL (record) | — | — | carried in `58` |

`09` ESCALATE 3 restates items 1–6 and is not counted again.

## RECORDS
- Branch read 21:27 ET: `git -C /Users/cobalt/cobalt log --oneline -3 drc/d1-trading-log` → `96ad059a` · `b86271f9` · `8e8762ca`; last code commit `b86271f9`. The base matches.
- Lock read 21:2x ET: `ls /Users/cobalt/cobalt-wt/*/.env` → `no matches found`.
- `57` = `08`'s shape: seat, launch line (`comm -3` shows only the path and the name `drc-d2-fix-r2-build-0928`), `acceptEdits`, the `.env` pair, THE LOCK, F0–F8, RESTARTS, the stop form. The lock is taken twice (F3, F8); RUN-6 runs inside F3.
- `58` = `09`'s shape: launch line (`comm -3`: only the path and the name `drc-d2-fix-r2-check-0928`), the grok gate, the probes, the three seat spellings, the stagger literal, REAL-line staging, the 45-minute clock. `## FOR THE CLASSIFIER` becomes `## FOR DEJAN` (round 3 is the last).
- Sizes: `57` 50,377 B, `58` 45,397 B (`wc -c`, before this report).

## FOR 10
What `10-drc-d3-build.md` re-points after fix r2 is BUILT and `58` checks it:
- The seam of record moves to the fix r2 build report `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-d2-fix-r2-build-2026-09-28.md` `## SEAM FOR D3` (it supersedes the fix r1 report's and the D2 build report's).
- `10:27` and `10:84` name `drc-d2-build-2026-09-25.md` → the fix r2 build report. `10:84` names `drc-d2-check-2026-09-25.md` → `drc-d2-fix-r2-check-2026-09-28.md`.
- `10:15`, `:29`, `:44` name the base `7cdc5774` → the fix r2 tip.
- The fix r1 report's `## FOR D3` list (`:1`, `:27`, `:28`, `:37`, `:44`, `:88`, `:101`, `:129`, `:144`, `:159`, `:162`) stands for the desk's re-point.
- Symbol added: `imports.NO_NOTE_PATH` (the build's return contract: a non-empty note path; `None` → `failed`). No other seam symbol moves. The `imports.py` line numbers of every seam symbol move by F-10 / F-11's lines; `10`'s PREFLIGHT greps them at the fix r2 tip.
- RUN-1 and RUN-2 stay strict `xfail`, named OPEN in the seam; D3 writes no event state, so neither blocks D3's build.

## OWNER ITEMS
None.

## FOR DEJAN
New strings: none. Both launch lines copy `08` / `09` with only the path and the name changed.

## ESCALATE
1. L74: one block arrived inside a tool result; recorded under `## L74`, not followed.
2. The desk's reading said items 1–4 go "red first on `b86271f9`". Built as `08`'s ASSERTION shape instead: a pin expected green on `b86271f9`, and a negative control shown red for the row's named reason. If a pin is red on `b86271f9`, that is a RESULT: `57` stops the row there, and it goes to Dejan after round 3 (L39).
3. ASK DESK: RUN-1 (the K2 current-file seed rule) and RUN-2 (no liveness rule for `running`) are proven L1 reds classified OUT OF SCOPE. Which lane takes them, and do they block the DRC deploy? [21:34 ET] Safe default: both stay strict `xfail`, named OPEN in the seam of record; D3 is not blocked; the desk routes the design (houses settle it, L67; not an owner item).
4. ASK DESK: "keep `08`'s suffix convention" was read as the `-MMDD` suffix of the drafting day. Names used: `drc-d2-fix-r2-build-0928` / `drc-d2-fix-r2-check-0928`; reports `drc-d2-fix-r2-build-2026-09-28.md` / `drc-d2-fix-r2-check-2026-09-28.md`. [21:34 ET] Safe default: as written. `-0925` is a one-token change in each line.
5. `58`'s FLOOR is "Opus AND one of Sol / Grok". That joins `56`'s "at least two answer and one is Sol or Grok" with L67's "every code check has an Anthropic seat".
6. F-9 is counted in `FIX: 7` as evidence. No `src/` commit is ever made with the reversal in it; `57`'s RECOVERY restores it first.
7. `58`'s ceiling is a `FILL AT LAUNCH` token for the desk (K17). `09`'s 400,000 B is quoted as the last measured shape.

## CONTINUE
Done. The three files are the desk's to commit: `prompts/2026-09-28/57-drc-d2-fix-r2-build.md`, `prompts/2026-09-28/58-drc-d2-fix-r2-check.md`, this report. Before launch the desk fills `57`'s `R__` and its one FILL token, and `58`'s `R__` and its FILL tokens.

DRC D2 FIX R2 DRAFTED · FIX: 7 · NOT REAL: 17 · UNPROVEN: 1 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 7
