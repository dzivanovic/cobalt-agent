## §0 Headline
S3 C3 fix r1 house check, round 2 of ≤3: 2 of 3 seats checked (Opus: BUILD STANDS EXCEPT · Grok: BUILD STANDS EXCEPT; Sol: METER, back 10:46 AM). Both say `ready for C4: YES`; floor met (Grok).
Grok's (iii) DOES NOT HOLD is file-true as a fact: a superseded leg of the same card gets the route's own sentence, not C2's `not_current` text; the built row `03:25` specifies that refusal and the drafter recorded it (draft ESCALATE 1). Filed, not judged.
R1 NaN exit stored (200) and `/correct` `-1` → 500 stand as the builder's ESCALATE R1; lock taken 3×. `defects that HOLD: 0`. `ready for C4: YES`. ESCALATE: 8.

## L74
No L74 line arrived in a tool result. (A `Claude-Session:` attribution note sits in the session's own system prompt, not a tool result; recorded once, not raised.)

## PREFLIGHT
`<D>` = `2026-09-29` (`date` → `Tue Sep 29 08:06:08 EDT 2026`).
| rule | command | result |
|---|---|---|
| placeholder `R_` `_` | `grep -n -E "R_[_]" …/04-s3-exits-c3-fix-r1-check.md` | nothing |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" …/04-…check.md` | nothing (no such line in this file) |
| R17 | `grep -n "^| R17 " …/cto-2026-09-24.md` | line 35, carries `Grok approved with no asking going forward` |
| R19 | `grep -n "^| R19 " …/cto-2026-09-24.md` | line 37, carries `All 4 house models approved` |
| R19 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"All 4 house models approved" -- …cto-2026-09-24.md` | `5055151dbf68899b82de5b11f99733ed2d03048c` |
| R95 | `grep -n "^| R95 " …/cto-2026-09-23.md` | line 103, one row |
| R109 | `grep -n "^| R109 " …/cto-2026-09-22.md` | line 56, carries `Make all Opus 5.5 for now` |
| launch row R31 | `grep -n -F "04-s3-exits-c3-fix-r1-check.md" …/cto-2026-09-29.md` | line 39 `| R31 | 08:05 ET | — LAUNCH ROW …` carries the `<build stop>` and `no other house hub is running`; lines 31 and 45 also name the file |
| R31 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"04-s3-exits-c3-fix-r1-check.md" -- …cto-2026-09-29.md` | `e721e9dbd5d169e1b36d4a423104eab16667b42e` |
| classification | `grep -n -F "S3 EXITS C3 FIX R1 DRAFTED" …/s3-exits-c3-fix-r1-draft-2026-09-29.md` | `80:` = the file's last non-blank line (80 lines) |
| grok | `grok --version` | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| build stop | `tail -n 3 "<report>"` | last non-blank line = `<build stop>`, starts `S3 EXITS C3 FIX R1 BUILT ` |
| commits | `git -C /Users/cobalt/cobalt log --oneline 27d482dc..78e9df82` | `78e9df82 fix(s3-c3): fix r1 — F3's with-DB test and R2 read the sheet's day from the suite clock` · `6114304e fix(s3-c3): fix r1 — terminal refusals shown, /correct binds its card, a closed manual card's estimated leg listed, the structural stop on a failed read (L75)` · `4d3553de wip(s3-c3-fix-r1): red` (3) |
| stat | `git -C /Users/cobalt/cobalt log --stat --format=%h 27d482dc..78e9df82` | `78e9df82`: `tests/cobalt/test_s3_c3_panel_db.py` · `6114304e`: `docs/40 - DevDocs/cobalt/aset/{radar_panel,web}.md`, `src/cobalt/aset/{radar_panel,web}.py` · `4d3553de`: `tests/cobalt/test_s3_c3_panel_{db,offline}.py`. Path union: those 7 paths |
| `.env` | `ls /Users/cobalt/cobalt-wt/s3-exits-c3/.env` | `No such file or directory` |
| scratch | `ls scratch/tribunal-bars-0920/s3-exits-c3-fix-r1` | absent (fresh) |
| stagger | `grep -n -F "no other house hub is running" …/cto-2026-09-29.md` | line 39 also names `04-s3-exits-c3-fix-r1-check.md` |
| probe OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | `OK` — UP (exit 0) |
| probe SOL | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | `OK` — UP at 08:06 (its meter ran out at 08:33 mid-check, see Clock) |
Grok not probed (per file). Floor at launch: Opus, Sol UP, Grok launched.

## Files copied
Every copy: Read → Write, then compared to its original (`cmp` on the whole, or on the head / tail / line range for a part) → identical. Bytes:
| copy under `S/files/` | original | bytes (copy = original) |
|---|---|---|
| `s3-exits-c3-fix-r1-build-2026-09-29.md.part1` + `.part2` | `<report>` | 14,251 + 33,142 = 47,393 |
| `s3-exits-c3-fix-r1-draft-2026-09-29.md` | `<class>` | 13,535 |
| `s3-exits-c3-check-2026-09-29.md` | `<r1>` | 15,965 |
| `s3-exits-c3-build-2026-09-28.md.part1` + `.part2` | `<c3>` | 32,968 + 12,643 = 45,611 |
| `03-s3-exits-c3-fix-r1-build.md` | `03` | 26,984 |
| `24-s3-exits-c3-build.md` | `24` | 28,101 |
| `S3-EXITS-v3-2026-09-22.md.part1`–`.part3` | v3 | 35,192 + 30,038 + 13,730 = 78,960 |
| `LAWS.md.part1` + `.part2` | LAWS.md | 37,784 + 23,227 = 61,011 |
| `wt/src/cobalt/aset/web.py.part1`–`.part3` | `web.py` at `78e9df82` | 28,843 + 26,187 + 28,695 = 83,725 |
| `wt/src/cobalt/aset/radar_panel.py.part1`–`.part3` | `radar_panel.py` at `78e9df82` | 28,698 + 27,969 + 23,203 = 79,870 |
| `wt/tests/cobalt/test_s3_c3_panel_db.py` | same at `78e9df82` | 26,063 |
| `wt/tests/cobalt/test_s3_c3_panel_offline.py` | same at `78e9df82` | 30,098 |
Outside `files/`: `diff.part1.md` 27,945 B (27,845 B of `git log -p` + the header line; `grep -c "^commit "` = 3 = PREFLIGHT's 3); `packet.md` 39,370 B (ceiling 300,000); `rulings.md` 3,699 B (R67, R38, R20); `CHECK-INSTRUCTIONS.md`. Worktree HEAD `6983de75` = report commit over `78e9df82`; `git diff --stat 78e9df82 HEAD -- src tests` → empty.

## CONTINUE
done — every step ran: PREFLIGHT, copies, launch, collate, close.

## Clock
Seats launched 08:30:50 (house gates re-read 08:30:34). SOL: METER at 08:33:15 (`You've hit your usage limit … try again at 10:46 AM`), no answer, `S/sol-check.partial.md`; one attempt, no retry. OPUS: complete, seen 08:34:12. GROK: complete, seen 08:50:50 (its file written 08:50). All inside 45 minutes; no TIMEOUT or HARNESS. Written-nothing proof: `ls -la S` before launch: `CHECK-INSTRUCTIONS.md`, `CHECK-REPORT.md`, `diff.part1.md`, `files/`, `packet.md`, `rulings.md`; after: those plus `opus-check.md`, `sol-check.partial.md` (both written by me) and `grok-check.md` (Grok's own file).

## Per question
Cells are the seat's words, ≤30 words. Sol produced no answer.
| Q | opus | sol | grok |
|---|---|---|---|
| (i) | HOLDS — each red fails for its row's reason (`packet.md:23-27`, `:36-37`); red tree's src is `78549817`; F3's test changed after red (`diff.part1.md:18-43`), still red by reading | METER | HOLDS — quoted reds are the named assertions (`test_s3_c3_panel_offline.py:598-599`, `:609`, `:270-271`, `:637`, `:648`; `test_s3_c3_panel_db.py:424`, `:135`); no other failure |
| (ii) | HOLDS — sink inside `.terminal-legs` (`radar_panel.py:1377-1378`); `PANEL_JS` `status` document-wide lookup (`:1514-1516`); refusal shown (`:1533`); `PANEL_JS` not in diff | METER | HOLDS — terminal block is the only `.card-status` match; JSON reason unchanged through `_refused`/`_card_tap` (`web.py:1325-1327`, `:1529-1530`) |
| (iii) | HOLDS — `read_position` guard before writer, 422 exact text (`web.py:1670-1674`); read rolls back (`legs.py:713-730`); no SQL; caveat: superseded leg gets F2's text (row `03:25`, builder ESCALATE 7) | METER | DOES NOT HOLD — `web.py:1670-1674` refuses any leg absent from current legs, so C2's `not_current` text never reaches the page; bind, current-leg path and read hold |
| (iv) | HOLDS — `_sheet_closed_estimated` via `filled_with_picks`, `render_estimated_legs`, sheet form `source=sheet`; no-live branch appends list (`web.py:753`, `:757`); R2 `carries …/correct: True` | METER | HOLDS — same helper as terminal list (`radar_panel.py:1290-1295`, `:1374`); form `source=sheet` (`:1204-1206`); empty branch keeps list (`web.py:750-753`); tests green |
| (v) | HOLDS — `render_stop_block(…, structural_stop=None, …)` after `_failed` (`web.py:1736-1738`); one renderer; NULL line, no ↺ (`radar_panel.py:1243-1246`) | METER | HOLDS — renamed `_stop_block`, no second body; `Cobalt stop NULL — no Cobalt stop` and no `/stop/reset` (`radar_panel.py:1232`, `:1243-1246`) |
| (vi) | HOLDS EXCEPT the lock count — suites 3297 / 3688+87 / 146, 0 failed; F2 = F0; `.env` gone; lock taken 3×; R1 NaN exit 200 stored, `-1` correction 500; seam lines true; NOTHING WIDENED | METER | HOLDS — same suites, runs, seam lines and NOTHING WIDENED; lock 3× recorded as ESCALATE; R1 names NaN exit 200 and `-1` correction 500 |
| (a) | (1) offline F3 test records `cards.days` but never asserts the day, and never shows a radar/FILLED/duplicate row excluded; (2) per-card failed read and failed `filled_with_picks` untested; (3) F4 test does not assert his stop value | METER | NONE in the new tests for what they claim |
| (b) | NO PATH — reads and renders only; `/correct` reaches C2's unchanged writer | METER | NO PATH — status div, pre-writer check, estimated-legs list, existing stop renderer; no sizer |
Final lines — opus: `CHECK S3 C3 FIX R1: BUILD STANDS EXCEPT (vi) lock taken 3× (ESCALATEd), R1 NaN-exit stored and −1 correction 500 (out of scope, to round-2 classifier) · ready for C4: YES` · sol: METER (no line) · grok: `CHECK S3 C3 FIX R1: BUILD STANDS EXCEPT (iii) C2 not_current replaced by the route sentence · ready for C4: YES`.

## Suites
From `<report>` (`## W THE THREE SUITES`), facts:
- offline on `78e9df82`: `3297 passed, 462 skipped, 1 xfailed, 20 warnings in 551.96s`, exit 0, 0 failed, 0 errors. (First W on `6114304e`: with-DB pass 1 `1 failed, 3687 passed`, superseded by the test-only commit.)
- with-DB: pass 1 at `0013` `3688 passed, 6 skipped, 65 deselected, 1 xfailed, 20 warnings in 649.30s`, exit 0; forward `dev forward: APPLIED 07:52:49`, no `CHANGED`; pass 2 at `0021` `87 passed, 5 warnings in 142.87s`, no FAILED, no SKIPPED; total 3775/0.
- deselected: the fourteen `--deselect` arguments of the C3 report's (c), quoted whole; the six SKIPPED lines are C3's six.
- F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; F1 `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; F2 = F0 (rollback of `0021`, `0017`, `0015`, `0014`).
- live-note: `146 passed, 1 skipped, 15 warnings in 25.05s`; the skip is `COBALT_TEST_LIVE_DRC`, none names `COBALT_LIVE_VAULT_ROOT`.
- `.env`: three takes (07:05:02–07:05:45; 07:17:38–07:31:34; 07:41:09–07:55:48), each removed and proven gone (`ls` → No such file; glob → `no matches found`).
- R1 (at `<code base>`, whole at `packet.md:45-66`): `/exit` `price=NaN` → 200, leg `(2, 'exit', 'NaN', 'confirmed')`, `legs` 1 → 2; `/exit` `price=-1` → 409 stale, counts equal; `/fill` `price=NaN` → 422, nothing written; `/correct` `price=-1` → 500 `Internal Server Error`, counts equal. At `0021` the NaN exit is again 200 (leg `119`) and the `-1` correction again 500.
- R2 (at `0013`, on `<tip>`, whole at `packet.md:116-131`): counts and `day_modes` equal before / after GET `/` and GET `/radar`; GET `/radar` → 200 with `FAILED` (`radar pool 'primary' is missing`); GET `/` carries `/radar/card/12366/correct: True`.
- RESTARTS table: `RESTARTS: com.cobalt.aset com.cobalt.radar`, no `UNCLASSIFIED`.

## Scope
- opus: NOTHING WIDENED · sol: METER · grok: NOTHING WIDENED.
- My path union (PREFLIGHT): `src/cobalt/aset/{radar_panel,web}.py`, `tests/cobalt/test_s3_c3_panel_{db,offline}.py`, `docs/40 - DevDocs/cobalt/aset/{radar_panel,web}.md` — the files of `03`'s rows F1–F4 plus the two C3 test files and the two DevDocs notes.

## Checked against the branch
claim · who · file:line · result · note
| claim | who | file:line | result | note |
|---|---|---|---|---|
| any leg absent from the URL card's current legs gets the route's sentence, so C2's `not_current` text does not reach the page | grok (iii) | `web.py:1670-1674` (worktree `s3-exits-c3` at `78e9df82`) | HOLDS as a fact | walked: guard at `:1670`, `_TapInputRefused` `:1671-1674`, writer only at `:1676`; `03:25` names this refusal text; draft ESCALATE 1 and builder ESCALATE 7 record it |
| F3 offline test records `cards.days` but never asserts the day passed | opus (a) | `test_s3_c3_panel_offline.py:612-627`, `:630-640` | HOLDS | `days` set at `:617`, appended `:626`; no assert reads it (`grep -n -F ".days"` → `:617`, `:626` only) |
| F3 offline test does not show a radar / FILLED / duplicate row is excluded | opus (a) | `test_s3_c3_panel_offline.py:631-632`; `web.py:1763` | HOLDS | the one row fed is CLOSED manual; the filter at `web.py:1763` has no negative case in that test |
| failed `filled_with_picks` and per-card failed read untested | opus (a) | `web.py:1757-1758`, `:1771-1773` | HOLDS | `grep -rn -F "closed manual cards unreadable" tests src` → `web.py:1758` only |
| F4 test does not assert his stop value | opus (a) | `test_s3_c3_panel_offline.py:643-649` | HOLDS | `9.90` appears only as input (`:646`); asserts are `FAILED`, `position unreadable`, the NULL line, no `/stop/reset` |
| lock taken 3×, prompt allows 2 | opus, grok (vi) | report `## W` take 3; `packet.md:109`, `:113` | HOLDS | builder recorded it as ESCALATE 4, cause and test-only fix stated |
| `_tap_price` accepts NaN, a leg with price NaN stored | opus ESCALATE 1 | `web.py:1465-1472`; `packet.md:52-53` | HOLDS | R1 output whole: 200, `legs` 1 → 2 |
| `/correct` `-1` → 500 | opus ESCALATE 2 | `packet.md:58-59` | HOLDS | R1 output whole: `Internal Server Error`, counts equal |
Also stated by me: (i) `git -C /Users/cobalt/cobalt log --oneline 27d482dc..78e9df82 -- src/cobalt/cards src/cobalt/radar src/cobalt/prefill src/cobalt/drc src/cobalt/settings src/cobalt/db_migrations` → EMPTY · (ii) `git log --stat --format=%h 27d482dc..78e9df82 -- src` → `6114304e`: `src/cobalt/aset/radar_panel.py`, `src/cobalt/aset/web.py` only · (iii) `grep -n -F "@app." …/web.py` → `/release` `:1439`, then `/triggered` `:1536`, `/fill` `:1555`, `/pass` `:1581`, `/exit` `:1592`, `/held` `:1639`, `/correct` `:1657`, `/stop` `:1688`, `/stop/reset` `:1701`; the pre-existing list before it unchanged; same routes in the same order as round 1's list (`<r1>`), no new route · (iv) `grep -rn -F "INSERT INTO" …/src/cobalt/aset` → `aset/store.py:129` only · (v) L32: this report holds no ticker beyond constructed ones (`TEST`, `ZZPB`, `X7CT`, `FTFT`), no real date or value of his.

## FOR THE CLASSIFIER
1. "`_sheet_closed_estimated` reads `filled_with_picks(_today_et())`, keeps each CLOSED manual card once and renders it through `render_estimated_legs`; the sheet form posts to `/correct` with `source=sheet`; the list shows when no card is live" · opus, grok · (iv) · `web.py:1745-1776`, `:750-757`; `radar_panel.py:1290-1295` · HOLDS
2. "`_terminal_legs` adds the status sink `card-status` inside `.terminal-legs`; `PANEL_JS` `status` finds it; the refusal is shown" · opus, grok · (ii) · `radar_panel.py:1363-1378`, `:1514-1516`, `:1533` · HOLDS
3. "The sheet's failed read renders the structural-stop line through the one stop renderer, no ↺" · opus, grok · (v) · `web.py:1736-1738`; `radar_panel.py:1232`, `:1243-1246` · HOLDS
4. "`/correct` refuses a leg not among the URL card's current legs before the writer, with nothing written; a current leg still reaches the writer" · opus, grok · (iii) · `web.py:1670-1680` · HOLDS
5. "Every red fails for its row's reason" · opus, grok · (i) · `packet.md:23-27`, `:36-37` · HOLDS
6. "NOTHING WIDENED; no route, store method or migration; `PANEL_JS` and `_tap_price` unchanged" · opus, grok · (vi) · (i), (ii), (iii), (iv) above · HOLDS
7. "NO PATH to a score, rank, grade or size" · opus, grok · (b) · `web.py:1670-1680`, `radar_panel.py:1290-1295` · HOLDS

## ESCALATE
1. **Grok (iii) DOES NOT HOLD — file-true as a fact:** any leg id absent from the URL card's current legs, including a superseded leg of the same card, gets `REFUSED card <id>: leg <leg> is not a current leg of card <id> — reload the card. Nothing written.` and never C2's `not_current` text (`web.py:1670-1674`). `03:25` specifies that refusal; the drafter (draft ESCALATE 1) and the builder (ESCALATE 7) recorded it; Opus files the same as a caveat with HOLDS. Grok's own line still says `ready for C4: YES`. Desk's to read; filed as `defects that HOLD: 0` because no rule of `03` is contradicted (I give no verdict, L37).
2. **R1 (builder ESCALATE 1): `/radar/card/<id>/exit` `price=NaN` → 200, a leg row stored with price `NaN`** (`legs` 1 → 2; the same at `0021`). Not fixed here; for the classifier. (`price=-1` exit hit `stale`, so a negative exit price is unproven.)
3. **R1 (builder ESCALATE 2): `/correct` `price=-1` → 500, nothing written** (`Internal Server Error`); the refusal does not reach the page verbatim (L1). Not fixed here; for the classifier.
4. **Lock taken 3× (prompt allows 2):** cause a test-clock ordering issue (`web.py:40` imports `now_utc` by name); test-only fix `78e9df82`; no take overlapped; F2 = F0. The pre-existing `web.py:40` import is recorded for the classifier.
5. **Sol did not check:** METER at 08:33:15, `try again at 10:46 AM`, no answer, `S/sol-check.partial.md`. ASK DESK: relaunch Sol alone after 10:46 AM? Safe default taken: no retry, round spent on 2 of 3 (L67: no ruling, no round spent for Sol). [08:51]
6. **Weak assertions (Opus (a), all file-checked HOLDS as facts, none a row):** `days` recorded never asserted; no negative case for the CLOSED+manual filter; failed `filled_with_picks` and per-card failed read untested; F4 test omits his stop value. For the classifier.
7. **R2:** GET `/radar` rendered its FAILED page on `cobalt_dev` (`radar pool 'primary' is missing`), so a full radar render with cards is still not counted; the pre-existing `attest_sheet` read-back write (`web.py:496`) did not fire in the run.
8. **Method:** the hub verified its copies with `cmp`, `head`, `sed`, `tail` and `wc` (read-only, not on the launch line's pool; the auto-mode classifier allowed them, which is not an approval, L37), and wrote temporary files only under `$CLAUDE_JOB_DIR/tmp`. Opus's file is its answer minus the harness warning line and exit trailer.
Standing line: **"Round 2 of ≤3 (L39) of S3 C3: Opus 5.5 (R109) · Sol · Grok (L67, K22). A HOLD → fix round 2, classified first (L75); round 3 is the last. `ready for C4: YES` → `26-s3-exits-c4-build.md` is re-issued on `78e9df82` before it runs."**

S3 EXITS C3 FIX R1 CHECK DONE · round: 2 · opus: CHECK S3 C3 FIX R1: BUILD STANDS EXCEPT (vi) lock taken 3× (ESCALATEd), R1 NaN-exit stored and −1 correction 500 (out of scope, to round-2 classifier) · ready for C4: YES · sol: METER · grok: CHECK S3 C3 FIX R1: BUILD STANDS EXCEPT (iii) C2 not_current replaced by the route sentence · ready for C4: YES · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C4: YES · ESCALATE: 8
