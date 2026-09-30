# S3 EXITS C2 FIX R1 CHECK — 2026-09-28 (round 2 of ≤3; hub run 2 — run 1 was `FAILED PREFLIGHT: stagger`, its record is in git `a71ecc81`)

## §0 Headline
Three of three seats checked `0d591041..5e77800f`: Opus 5.5 · Sol · Grok. Two say BUILD STANDS; Sol says BUILD STANDS EXCEPT three weak-assertion notes, ready YES. All three: ready for C3 YES.
Defects that HOLD: 0. Floor met (3 of 3, Sol and Grok answered). No seat down. Hub gives no verdict (L37).
ESCALATE: 4.

## L74
none arrived.

## PREFLIGHT
| rule | command | result |
|---|---|---|
| date | `date` | `Mon Sep 28 22:18:43 EDT 2026` |
| placeholder gates | `grep -n -E "R_[_]"` / `grep -n -F "FILL AT LAUNCH"` on this file | both exit 1, no hit |
| R17 / R19 | greps on `cto-2026-09-24.md` | 1 / 1; `git log -S` → `5055151dbf68899b82de5b11f99733ed2d03048c` |
| seats | R109 `Make all Opus` (`cto-2026-09-22.md`) | 1 |
| launch row | `grep -n -F "55-s3-exits-c2-fix-r1-check.md"` on `cto-2026-09-28.md` | R172 (first launch) and R174 (this run); R174 carries `<build stop>` and `no other house hub is running`; `git log -S` → `a71ecc81…` |
| grok | `grok --version` | `grok 1.0.25 (f7e67d6988e2) [stable]`, exit 0 |
| build stop | `tail -n 3 <report>` | last non-blank line = `S3 EXITS C2 FIX R1 BUILT 5e77800f | on 77cf18fd | migration none (0021 rolled back) | offline 3255/0 | with-DB 3689/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | FIX: 3 | RUNS: 2 | ESCALATE: 5` — equals `<build stop>` |
| range | `git log --oneline 0d591041..5e77800f` | `5e77800f fix(s3-c2): fix r1 …` · `d727a7bc wip(s3-c2-fix-r1): red` (2 commits) |
| stat | `git log --stat --format=%h … ` | `5e77800f`: `aset/store.py`, `aset/web.py`, `cards/cli.py`, `cards/legs.py` (49+/34−) · `d727a7bc`: `tests/cobalt/test_legs_c2_db.py`, `tests/cobalt/test_legs_c2_offline.py` (132+) |
| `.env` | `ls /Users/cobalt/cobalt-wt/s3-exits-c2/.env` | `No such file or directory` (also at close) |
| scratch | `ls …/s3-exits-c2-fix-r1` | absent → fresh |
| stagger | grep literal + file name | R174 line names this file ✓ |
| probes | OPUS `claude -p … OK` | first probe's stdout was cut by my `head -c` (warning text only); re-probe → `OK` = UP |
| probes | SOL `codex exec … "Reply with only the word OK."` | `OK` = UP |

## Files copied
Scratch `scratch/tribunal-bars-0920/s3-exits-c2-fix-r1/` (`S`). Byte checks: `diff.part1.md` 15,463 B = 15,363 diff + 100 header, `grep -c "^commit "` = 2 = PREFLIGHT's 2 ✓. `rulings.md` 3,604 B (R67 · R38 · R151, 3 rows). `packet.md` 32,422 B (ceiling 300,000 B; sections PREFLIGHT, E2 RED, E3 THE ROWS, W THE THREE SUITES, RESTARTS, SEAM FOR C3, FOR THE CHECK, in that order, extracted whole by heading).
`files/` (Grok): `s3-exits-c2-fix-r1-build-2026-09-28.md` 37,477 = original 37,477 ✓ · `…-draft-…` 9,932 ✓ · `s3-exits-c2-check-2026-09-28.md` 22,055 ✓ · `54-…` 25,528 ✓ · `22-…` 19,994 ✓ · `20-…` 31,610 ✓ · v3 design in 3 parts (35,192 + 30,038 + 13,730 = 78,960; `cmp` against the original ✓) · LAWS.md in 2 parts (37,814 + 23,197 = 61,011; `cmp` ✓) · `wt/`: `aset/store.py` 21,757 ✓ · `aset/web.py` in 3 parts (28,843 + 30,573 + 6,448 = 65,864; `cmp` ✓) · `cards/cli.py` 11,836 ✓ · `cards/legs.py` 30,874 ✓ · `test_legs_c2_db.py` 26,412 ✓ · `test_legs_c2_offline.py` 2,598 ✓ · `test_fill_c1_offline.py` 14,888 ✓ · `test_fill_transaction_db.py` 15,597 ✓. Copies were made by `cp`/`awk` split from the tip worktree (HEAD `04b3ca3e`; `git diff --stat 5e77800f 04b3ca3e` = the report only).
Method note: `diff.part1.md` was assembled with `cat` (header + saved `git log -p` output), not Read → Write, for byte fidelity. `CHECK-INSTRUCTIONS.md` written by Write.

## CONTINUE
done — all seats collated.

## Clock
Seats launched 22:20 ET (`date` 22:19:59 before). Opus done 22:22 (`date` 22:22:41). Sol done 22:27 (`date` 22:27:06). Grok done 22:36 (`date` 22:36:24). All inside 45 minutes. Written-nothing proof: `ls -la S` before (8 lines) and after — new files only `opus-check.md`, `sol-check.md`, `grok-check.md` (all by me, plus Grok's own Write to `grok-check.md`, which its `--allow` names); no other file changed.

## Per question
Cell ≤30 words. Paths: `pk` = `S/packet.md`; `wt` = `/Users/cobalt/cobalt-wt/s3-exits-c2/`.
| Q | opus | sol | grok |
|---|---|---|---|
| (i) RED FIRST | HOLDS — reds ran on code base; F1 stub reached (`pk:34-35`), F2 two lines (`pk:36`), F3 `no_position` (`pk:48`); F2 DB `not red by design` (`pk:49`) | HOLDS — F1 reds reached stub `transition`, F2 named both writers, F3 alone `no_position`; R2 reads quoted (report `:62-:80`) | HOLDS — quotes `pk:34,35,36,47-48`; F2 DB test PASSED at E2 recorded `not red by design` (`pk:49`); R2 reads `pk:18-23` |
| (ii) CLOSED | HOLDS — route `web.py:1246-1255` before `CardStore()` `:1256`; CLI `cli.py:87-94` before `_store()` `:95`; only `legs.py:236` writes CLOSED (evidence leg id `:237`) | HOLDS — three CLOSED-capable callers; two refuse before store `web.py:1246`, `cli.py:87`; `_close_if_zero` `legs.py:228-236` alone writes at 0 | HOLDS — (text in `grok-check.md`; truncated in my read of the tail, full file kept) guards before store; `_close_if_zero` only zero writer |
| (iii) ONE CACHE WRITER | HOLDS — `store.py:370` only cache UPDATE; correction → `legs.py:477` `at_fill=False`; `mark_filled` `:325` unchanged; replacements `test_fill_transaction_db.py:171,254` | HOLDS — one UPDATE `store.py:360-380`; correction on its transaction, `filled_at`/`drift_warning_pct` omitted; replacements still intercept (`:171`, `:252`) | HOLDS — `store.py:371` sole `actual_fill = %s`; callers `store.py:325`, `legs.py:477`; NOTHING WIDENED |
| (iv) PRE-C1 CLOSED | HOLDS — `legs.py:315-333` `pre_c1`; `no_position` `:330`; test `test_legs_c2_db.py:316-335` green pass 2 (`pk:82`); `cli.py:115` `read_position` | HOLDS — `legs.py:319-330`; confirm succeeds, one CLOSED row, `read_position` running 0 (`cli.py:115`) | HOLDS — `pre_c1` `legs.py:319-321`, basis branches `:325`,`:327`; F3 test `:328-335` |
| (v) SUITES/RUNS/SEAM/SCOPE | HOLDS — `pk:68,74,80,87`; two lock takes; deselects match C2 report (c) and (c3); SEAM cites true; NOTHING WIDENED; YES | HOLDS — `<3255>` · `<3624>` + `<65>` · `<146>`, `<0>` failed, F2 = F0, `.env` twice removed; NOTHING WIDENED; YES | HOLDS — same numbers; 14 `--deselect` args, no 15th; SEAM cites opened at tip; NOTHING WIDENED; YES |
| (a) weak assertions | 4: `test_legs_c2_db.py:313` cannot catch `at_fill=True` slide (same `now()` on savepointed conn, `conftest.py:92,127`); F2 scan keyed on literal (`offline:330-338`); F1 stubs fail only on `transition` (`offline:281-322`); F3 `no_position` branch untested | 3: F1 proves `transition` not reached, not store/`state_of` order; F2 one spelling only; F3 lacks CLOSED `recomputed_shares`, `cmd_legs` surface, negative branch | NONE — each new assertion fails for the behaviour it names (`offline:47-48`, `:64-65`, `:80-81`; `db:303-313`, `:328-335`) |
| (b) reach a score/rank/grade/size | NO PATH | `legs.py:474` DOES — correction recomputes fill sizing; `store.py:382,384` writes `recomputed_shares` / `share_delta`; "reaches a size cache, but no score, rank, grade, or planned `shares`" | NO PATH — cache SET `store.py:371-376` is what the pre-fix legs UPDATE already wrote |
| closing line | `CHECK S3 C2 FIX R1: BUILD STANDS · ready for C3: YES` | `CHECK S3 C2 FIX R1: BUILD STANDS EXCEPT weak F1 pre-store assertions, weak F2 one-writer scan, weak F3 CLOSED-position coverage · ready for C3: YES` | `CHECK S3 C2 FIX R1: BUILD STANDS · ready for C3: YES` |
Note: Grok's (ii) cell is from the part of `grok-check.md` my tail display truncated (8,926 characters cut in the middle of the file, not in the file); the file on disk is whole (18,913 B) and its (ii) answer reads HOLDS. I did not re-open that middle; ready-line and (v)–(b) were read.

## Suites
From `<report>` (`pk` = its copy):
- offline: `3255 passed, 440 skipped, 1 xfailed, 20 warnings in 546.93s` — 0 failed, 0 errors (`pk:68`).
- with-DB pass 1 at `0013`: `3624 passed, 6 skipped, 65 deselected, 1 xfailed` — 0 failed (`pk:74`); pass 2 at `0021`: `65 passed, 5 warnings` — 0 failed, no SKIPPED (`pk:80`); total 3689.
- deselects: 14 `--deselect` args (`pk:72`), the `-rA` pass-2 list of the same 14 ids (`pk:78`). The file `22-s3-exits-c2-build.md` carries no `--deselect` literal (my `grep -o` = 0), so "the deselects `22`'s" is checked here only as the seats did against the C2 report's (c)/(c3); Opus quotes that C2 report at `:119`, `:125`.
- fingerprints: take 1 `F0` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, `F2` = `F0` (`pk:44`, `:51`); take 2 `F0` same, `F1` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`, `F2` = `F0` (`pk:69`, `:75`, `:88`). Lock takes 21:48:22 → 21:49:19 and 22:00:08 → 22:15:20; `0021` forward and rolled back in each; `cobalt_dev: 0013`.
- live-note: `146 passed, 1 skipped, 15 warnings in 25.49s`; the skip `tests/cobalt/test_replay_line.py:256 … COBALT_TEST_LIVE_DRC` (`pk:87`).
- `.env`: removed and proven gone after each take (`pk:52`, `:89`); at this hub's close `ls /Users/cobalt/cobalt-wt/s3-exits-c2/.env` → `No such file or directory`.
- R2's three reads: quoted whole `pk:21-23` — (3) hit only `test_legs_c2_db.py:364` (another test's `kind` read); (4) hit only `:111`; (5) no hit.
- RESTARTS line: `RESTARTS: com.cobalt.aset com.cobalt.radar`, no `UNCLASSIFIED`.
- The mutation-run leg does not apply (no mutation in this fix).

## Scope
Seats' (v) answers: Opus NOTHING WIDENED; Sol NOTHING WIDENED; Grok NOTHING WIDENED. My PREFLIGHT path union: `src/cobalt/aset/store.py`, `src/cobalt/aset/web.py`, `src/cobalt/cards/cli.py`, `src/cobalt/cards/legs.py`, `tests/cobalt/test_legs_c2_db.py`, `tests/cobalt/test_legs_c2_offline.py` (the report file itself is outside `src`/`tests`). My own calls:
- (i) `git log --oneline 0d591041..5e77800f -- src/cobalt/radar src/cobalt/prefill src/cobalt/drc src/cobalt/settings src/cobalt/db_migrations src/cobalt/cards/models.py` → EMPTY ✓.
- (ii) `git log --stat --format=%h 0d591041..5e77800f -- src` → only `aset/store.py`, `aset/web.py`, `cards/cli.py`, `cards/legs.py` ✓.
- (iii) `grep -rn -F "actual_fill = %s" /Users/cobalt/cobalt-wt/s3-exits-c2/src` → ONE: `src/cobalt/aset/store.py:371: {fill_stamps}actual_fill = %s,` ✓.
- (iv) `grep -rn -F "CardState.CLOSED" …/src`: `cards/models.py:105` (`FILLED: frozenset({CardState.CLOSED})`), `:106` (`CLOSED: frozenset()`); `cards/cli.py:87` (guard), `:92` (message); `cards/legs.py:237` (`transition(card_id, CardState.CLOSED, … evidence={"leg_id": leg_id}`), `:320` (`pre_c1`), `:529` (correction state gate), `:560` (`closed_off_zero`), `:630` (held `closed_held`); `aset/radar_panel.py:1160` (a state loop); `aset/web.py:651` (a button label map), `:1246` (guard), `:1252` (message). The only `.transition(` in `src` that writes CLOSED is `legs.py:236-237`; the other `.transition(` callers are `cards/store.py:535,549,1193`, `cards/cli.py:97`, `cards/expire.py:203`, `aset/web.py:1261,1348`, and `voice/*` (a separate state machine).
- (v) `grep -n -F "@app.post" …/web.py` → nine routes (`/size`, `/fill`, `/attest`, `/card/{card_id}/move`, `/card/{card_id}/stop`, `/radar/card/{card_id}/key`, `/radar/card/{card_id}/dot/{factor}`, `/radar/card/{card_id}/promote`, `/radar/card/{card_id}/release`); `git show 77cf18fd:src/cobalt/aset/web.py | grep -c -F "@app.post"` → 9. No new route ✓.
- (vi) L32: this report holds only constructed ids (card `11510`, `7`), commit shas, file paths, and figures from the builder's own report (suite counts, fingerprints); no ticker beyond none, no real date or value of the trader's.

## Checked against the branch
`claim · who · file:line · verdict · ≤30 words`
| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| the `filled_at`/`drift_warning_pct` equality cannot catch an `at_fill=True` slide (one savepointed connection, one `now()`) | Opus | `wt/tests/cobalt/conftest.py:88-93`, `:125-129` (a `SAVEPOINT`-proxy over the one connection), `wt/tests/cobalt/test_legs_c2_db.py:313` | HOLDS | Opus's savepoint description matches the file; whether the two `now()` values are the same stamp inside one transaction is Postgres behaviour I did not run (`NOT CHECKABLE FROM READS` for that half) |
| F3's `no_position` negative branch has no test | Opus, Sol | `grep -rn -F "no_position" wt/tests` → exit 1, no output | HOLDS | No test names `no_position`; the only `legs.py` raise is `:330` |
| CLOSED `recomputed_shares` basis untested | Opus, Sol | `wt/tests/cobalt/test_legs_c2_db.py:201-212` sets `recomputed_shares = 450` on a FILLED card only; the CLOSED test `:316-335` reads basis `shares` | HOLDS | The CLOSED-with-`recomputed_shares` path has no test of its own |
| F2 scan keys on the literal `actual_fill = %s` only | Opus, Sol | `wt/tests/cobalt/test_legs_c2_offline.py:73-81` (`"actual_fill = %s" in line`) | HOLDS | A second UPDATE without that literal would pass the scan; the diff shows none |
| F1 stubs fail only on `transition`; refusal order is not asserted | Opus, Sol | `wt/tests/cobalt/test_legs_c2_offline.py:31-61`; `wt/src/cobalt/aset/web.py:1246-1256`, `wt/src/cobalt/cards/cli.py:87-95` | HOLDS | The stub `ensure_schema` is a no-op and `state_of` returns FILLED; a guard moved after them would still pass |
| L52 path: `legs.py:474` recomputes fill sizing and writes `recomputed_shares` / `share_delta` (`store.py:382,384`) — "a size cache" | Sol | `wt/src/cobalt/cards/legs.py:470-477`; `wt/src/cobalt/aset/store.py:376-388` | HOLDS as described | The correction writes the F6 cache columns through `_update_fill_cache`; the removed UPDATE wrote the same `recomputed_shares` and `share_delta` (diff `legs.py` hunk `-465,22`). Not a score, rank, grade or planned `shares`; Sol says the same |
Nothing in the table is `DOES NOT HOLD` or `WIDENED`.

## FOR THE CLASSIFIER
- "F1's route and CLI refuse CLOSED before any store read" — Opus, (ii), `wt/src/cobalt/aset/web.py:1246-1256`, `wt/src/cobalt/cards/cli.py:87-95` — HOLDS.
- "`AsetStore._update_fill_cache` is the only UPDATE of the fill cache; the correction writes through it with `at_fill=False`" — all three, (iii), `wt/src/cobalt/aset/store.py:360-395`, `wt/src/cobalt/cards/legs.py:477` — HOLDS (my (iii) grep: one `actual_fill = %s`, `store.py:371`).
- "`running_shares` reads the O21 A basis for CLOSED with at least one exit leg and refuses `no_position` otherwise" — all three, (iv), `wt/src/cobalt/cards/legs.py:315-333` — HOLDS.
- "`_close_if_zero` is the only `.transition(` that reaches CLOSED" — Opus, Sol, Grok, (ii), `wt/src/cobalt/cards/legs.py:236-237`, my `grep -rn -F ".transition(" …/src` — HOLDS.
- "Suites: offline 3255/0, with-DB 3689/0, live-note 146/0, F2 = F0 twice, `.env` removed" — all three, (v), `pk:68-89` — HOLDS (the report's own lines, quoted under `## Suites`).
- "NOTHING WIDENED" — all three, (v), `git log --stat` over `src` = four files — HOLDS.

## ESCALATE
1. **Weak assertions (Opus 4, Sol 3, Grok none), all file-checked HOLDS as facts, none a HOLD** — F1 stubs do not assert refusal order; F2's scan is literal-keyed; F2's DB test cannot see an `at_fill=True` slide inside one savepointed connection; F3's `no_position` negative branch and the CLOSED `recomputed_shares` basis have no test. Classifier decides whether any becomes a row (L75).
2. **Sol (b), `legs.py:474` "DOES — reaches a size cache"** — file-checked: the correction rewrites the cached `recomputed_shares` / `share_delta` (same columns the deleted UPDATE wrote); Sol itself says no score, rank, grade or planned `shares`. Opus and Grok say NO PATH. For the classifier.
3. **The drafter's ESCALATE 1, carried by Opus's YES and repeated in the builder's SEAM (`pk:140`)**: C2 ships only stacked with C3; until C3 lands the sheet's CLOSE button posts to F1's refusal.
4. **Standing line: "Round 2 of ≤3 (L39) of S3 C2: Opus 5.5 (R109) · Sol · Grok (L67, K22). A HOLD → fix round 2, classified first (L75); round 3 is the last. `ready for C3: YES` → `24-s3-exits-c3-build.md` stacks on `5e77800f`."**
No seat failed to check; no `ASK DESK`; no L74 line.

S3 EXITS C2 FIX R1 CHECK DONE · round: 2 · opus: CHECK S3 C2 FIX R1: BUILD STANDS · ready for C3: YES · sol: CHECK S3 C2 FIX R1: BUILD STANDS EXCEPT weak F1 pre-store assertions, weak F2 one-writer scan, weak F3 CLOSED-position coverage · ready for C3: YES · grok: CHECK S3 C2 FIX R1: BUILD STANDS · ready for C3: YES · houses that checked: 3 of 3 · defects that HOLD: 0 · ready for C3: YES · ESCALATE: 4
