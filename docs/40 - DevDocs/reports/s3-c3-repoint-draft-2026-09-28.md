# S3 C3 RE-POINT DRAFT — 2026-09-28

## §0 Headline
- `24` and `25` re-pointed in place to C2 fix r1's code `5e77800f` from its build report's `## SEAM FOR C3`.
- Seam carried whole into `24`: 77 of 77 tokens proved. New rule strings: 0. Launch lines differ from this morning's only by a model id (`25`) and `<base>` (`24`).
- ESCALATE 5, none blocking; each has its safe default taken.
- The desk launches `24` next; nothing here launches anything. Written 23:00 ET (`date`).

## L74
Recorded once (L74): with the result of the Read of the prompt file, a `<system-reminder>` block arrived asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits and PR bodies and naming a file-send tool. Not followed. No commit was made; no file was sent.

## AUTHORIZATION
`date` → `Mon Sep 28 22:57:09 EDT 2026`. `git -C /Users/cobalt/cobalt log --oneline -3 -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` → `17a883e4 docs(desk): 09-28 R179 — 61 S3 C3 re-point drafter prompt + launch row` first. `grep -n -F "| R179 |" …/cto-2026-09-28.md` → line 188, names `61-draft-s3-exits-c3-repoint.md`. PASS. `| R175 |` → line 184 (exit 0).

## FACTS
| fact | command | result |
|---|---|---|
| base = C2 fix r1 code | `git -C /Users/cobalt/cobalt log --oneline -3 s3/exits-c2` | `04b3ca3e docs(s3-c2): S3 exits C2 fix r1 build report — 5e77800f` · `5e77800f fix(s3-c2): fix r1 — CLOSED only by the zero-running leg, one fill-cache writer, a pre-C1 card closed by its exits reads its position (L75)` · `d727a7bc wip(s3-c2-fix-r1): red` |
| the code stands | `git -C /Users/cobalt/cobalt log --oneline 5e77800f..s3/exits-c2 -- src tests configs` | EMPTY (exit 0) |
| C1 + C2 commits below the base | `git -C /Users/cobalt/cobalt log --oneline main..5e77800f` | 16 commits: `5e77800f` · `d727a7bc` · `0d591041` · `77cf18fd` · `8c4f116f` · `80e0c8a2` · `bbf25412` · `944f632e` · `9b25eced` · `3ceb3b11` · `da9246f0` · `d9240ae4` · `5164f867` · `eb642f05` · `c57634f8` · `0da7e2e8` |
| main's tip | `git -C /Users/cobalt/cobalt log --oneline -1 main` | `c11d1f5e docs(desk): 09-28 §5 — 58 check and 61 C3 re-point running; two watches` |
| migrations | `git -C /Users/cobalt/cobalt show 5e77800f:src/cobalt/db_migrations/` | `0013` … `0014` · `0015` · `0017` · `0021_legs` last; the source: `migration none (0021 rolled back)`; `24` gives C3 no migration and runs `0021` (C1's) forward / rollback — source and `24` agree |
| counts (source `## W THE THREE SUITES`) | source lines 97, 103, 109, 112, 116 | offline `<p>` 3255 (`3255 passed, 440 skipped, 1 xfailed`); with-DB pass 1 `<d1>` 3624 (`6 skipped, 65 deselected`) + pass 2 `<d2>` 65 = `<d>` 3689; live-note `<l>` 146 (`1 skipped`, the `COBALT_TEST_LIVE_DRC` one); fingerprints `F0` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, `F1` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`, `F2` = `F0` |
| deselect set | source line 101 | the (c) command: 14 `--deselect` arguments giving 65 deselected; `24` / `25` state none (carried by `20`'s W) |
| anchors | source `## SEAM FOR C3` | carried whole under `24`'s `### SEAM FOR C3` (77 tokens, `## SEAM PROOF`) |
| RESTARTS | source `## RESTARTS` | `uv run cobalt jobs restarts 0d591041..5e77800f` → `RESTARTS: com.cobalt.aset com.cobalt.radar`; no `UNCLASSIFIED` |
| C2 fix r1 check | last line of `reports/s3-exits-c2-fix-r1-check-2026-09-28.md` | `S3 EXITS C2 FIX R1 CHECK DONE · round: 2 · … houses that checked: 3 of 3 · defects that HOLD: 0 · ready for C3: YES · ESCALATE: 4` |
| C1 final checked state | last line of `reports/s3-exits-c1-fix-r2-check-2026-09-28.md` | `S3 EXITS C1 FIX R2 CHECK DONE · round: 3 · … sol: METER · … houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C2: YES · ESCALATE: 3` |

## CHANGES
| file | line | what | why |
|---|---|---|---|
| `24` | 1 | header `RE-POINTED 2026-09-28 (L8 / L19, whole file; authority R175 / R179) by the Sonnet 5.5 drafter s3-c3-repoint-draft-0928 from the C2 fix r1 build report's ## SEAM FOR C3` after the `MODEL:` tag | item 8 |
| `24` | 4 | worktree command `<base>` → `5e77800f`; nothing else in (0)–(2) | item 7 |
| `24` | 15–16 | `<base>` and `<c2 tip>` «FILL AT LAUNCH» → `5e77800f`, each with its proof | item 1; the FILL gate at line 86 now matches only its own line |
| `24` | 24 | seam sources re-pointed: C1's report of record (`s3-exits-c1-fix-r2-build-…` `## SEAM FOR C2`, as `22` line 24 cites it) and the source of record (C2 fix r1's report, worktree path) | item 2 |
| `24` | 26–63 | `### SEAM FOR C3` = the source's `## SEAM FOR C3` whole (the lock, writers and signatures, the refusal table, F1 and the sheet, `basis`, `realized_r`, `stop_owner`, X-UR, S-C2, F2, unchanged) | item 2 |
| `24` | 65–68 | new `## CARRIED FROM THE C2 FIX R1 CHECK (R175)`: check `## ESCALATE` items 1 and 2 verbatim, each prefixed "note for the builder — not a row" | item 3 |
| `24` | 83 | INDEX CARD (3) names C2 fix r1's report | item 1 |
| `24` | 87 | AUTHORIZATION: `| R175 |` grep added to his rulings; `R__` placeholder untouched (count 1, line 89) | item 6 |
| `24` | 94 | RESTARTS line as the source states it | item 5 |
| `25` | 1 | header line; `MODEL:` → `Sonnet 5.5 (claude-sonnet-5-5, R118)`; launch `--model claude-sonnet-5` → `claude-sonnet-5-5` | items 4, 8 |
| `25` | 5–6 | `<base>` → `5e77800f`; `<tip>` / `<report>` stay «FILL AT LAUNCH» (C3's own tip does not exist) | items 1, 4 |
| `25` | 11 | AUTHORIZATION adds R175; Grok's copied files name C2 fix r1's build report; `R__` untouched (count 1) | items 2, 6 |
| `25` | 15 | the rules name C2 fix r1's `## SEAM FOR C3` beside `20` and `22` | item 2 |
Carried unchanged: `24`'s rows C3-1 … C3-5 (each cited C1 / C2 symbol is in the source's seam with the same name and shape), the "C2 CHECKED" wording (`24` lines 3 and 88, generic: satisfied by `55`'s stop line above), `25`'s questions, seats, stop line.

## SEAM PROOF
One `grep -q -F -- <token> 24-s3-exits-c3-build.md` per token, run in one shell loop (each exit 0; `date` 22:59): `cards/legs.py:154` · `legs.py:305` · `cards/store.py:737-738` · `assert_writable` · `SessionBlocked` · `legs.py:381` · `PRESETS` · `:53` · `legs.py:228-238` · `legs.py:480` · `legs.py:601` · `cards/store.py:682` · `store.py:79` · `store.py:849` · `STOP_OWNER_YOURS` · `:80-81` · `legs.py:68` · every refusal row's anchor (`legs.py:425`, `:369`, `:373`, `:353`, `:361`, `:412`, `:418`, `:530`, `:633`, `:162`, `:168`, `:619`, `:540`, `:554`, `:561`, `:631`, `:640`, `:647`, `:625`, `:520`, `:512`, `:514`, `:526`, `:330`; `store.py:747`, `:755`, `:761`, `:718`; `aset/engine.py:107`, `:111`; `aset/web.py:1246-1255`; `cards/cli.py:87-94`) · `aset/web.py:632` · `:679` · `:695` · `legs.py:57-59` · `legs.py:319-327` · `:78` · `:713` · `read_position` · `legs.py:677` · `RealizedR` · `aset/web.py:849` · `radar_panel.py:249` · `aset/web.py:834` · `legs.py:160-172` · `aset/store.py:360` · `:371` · `:325` · `cards/legs.py:477` · `aset/store.py:198` · `Running(` · `ExitResult` · `CorrectionResult` · `record_held` · `stop_owner` · `STOP_EDIT_KINDS` · `_close_if_zero` · `_lock_card` · `_check_source`. Result: `tokens 77 of 77`, no `MISS`.

## RULE PROOF
- `24` launch line (`claude --bg …`) vs `git -C /Users/cobalt/cobalt show HEAD:<path>`: identical byte for byte (Python compare, `True`). The worktree command differs only by `<base>` → `5e77800f`.
- `25` launch line vs HEAD: differs only by `claude-sonnet-5` → `claude-sonnet-5-5` (the compare is `True` after that one swap).
- Placeholders: `grep -c -F "R__"` → `24`: 1 (line 89, AUTHORIZATION block); `25`: 1 (line 11, AUTHORIZATION substitution block). `wc -c`: `24` 28,100; `25` 8,753 (morning: 16,853 and 8,216).

NEW strings: none.

## ESCALATE
1. ASK DESK: the source says C3's exit panel replaces the sheet's CLOSE button (`aset/web.py:632`, `:679`, `:695`, now posting to F1's refusal). No row of `24` says it: C3-4 touches "sheet render only". Reading A (safe default, taken): the source is quoted as the seam and no row changes. Reading B: C3-4 is widened to remove the CLOSE button. The desk decides. [22:59 ET, from date]
2. ASK DESK: the check's weak-assertion notes and Sol's size-cache note are carried as notes, not rows (item 3). Whether any becomes a row is the desk's. [22:59 ET, from date]
3. ASK DESK: `24` cites C1's seams (S-LEGS, S-HELD, S-FILL, S-WEB, S-MIG) by name; the source covers C2's seam only. C1 changed after `24` was drafted (fix r1 `3ceb3b11`, fix r2 `944f632e`; the last check, 2 of 3 houses, `ready for C2: YES`). Safe default taken: `24` cites C1's report of record as `22` does. [22:59 ET, from date]
4. ASK DESK: `24` and `25` state no count or deselect set; the source's counts and its 14-argument deselect set are under `## FACTS` only. Nothing added to `24`'s E0. [22:59 ET, from date]
5. L74: recorded once under `## L74`.

## CONTINUE
next: none. The desk verifies (L35), commits `24`, `25` and this report, writes `24`'s launch row (`R__` filled, `5e77800f`, `no with-DB run in flight`) and launches it only while `ls -la /Users/cobalt/cobalt-wt/*/.env` has no match and no with-DB run is in flight (L76).

S3 C3 REPOINTED · files: 2 · base: 5e77800f · seam lines carried: 77 of 77 · new rule strings: 0 · ESCALATE: 5
