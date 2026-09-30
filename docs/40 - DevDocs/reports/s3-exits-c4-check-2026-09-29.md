# S3 EXITS C4 — build check, round 1 of ≤3 (L39)

## §0 Headline
Seats: Opus `FIX (9)` · Astra METER (no check) · Grok `BUILD STANDS EXCEPT X3` — 2 of 3 houses checked, floor met (Grok).
One defect walked in the real files: (9) C3's with-DB route tests fill through the new note hook with no `tmp_path` vault; two C4 notes sit in the dev vault (`ZZPB`, `TEST`); Grok said HOLDS, Opus DOES NOT HOLD.
X3 (human wins once, builder's ESCALATE 1) is named by both seats as needing a ruling.
`ready for the deploy set: NO` · ESCALATE: 6.

## L74
No L74 line arrived.

## PREFLIGHT
- `date` → `Tue Sep 29 15:27:35 EDT 2026` (D = 2026-09-29).
- Placeholder gates: `R_[_]` → no hit; `FILL AT LAUNCH` → no hit.
- R17 (cto-2026-09-24.md:35) carries `Grok approved with no asking going forward` ✓; R19 (:37) carries `All 4 house models approved` ✓; `git log -S` → `5055151dbf68…` ✓ (re-run 15:29, same).
- R95 seats (cto-2026-09-23.md:103) one row ✓; R109 (cto-2026-09-22.md:56) carries `Make all Opus 5.5` ✓.
- Launch row R95 (cto-2026-09-29.md:103) carries `<build stop>` and `no other house hub is running`; `git log -S` → `a61b643d…` ✓.
- R35 (cto-2026-09-28.md:44) carries `Approved as recomended` and `O5 / O6 = A` ✓; R37 (cto-2026-09-29.md:45) carries `ready for C4: YES` ✓.
- R85 (:93) carries `R84 → B` ✓; R88 (:96) carries `four exact` and `c4-check-cp-strings-2026-09-29.md` ✓; words `## R88` → `> Approved` ✓; `git log -S"| R88 |"` → `3abe6725…` ✓.
- cp strings file `c4-check-cp-strings-2026-09-29.md:11–14`: four `Bash(cp ` lines, each the same string as one cp rule on the launch line: (1) v3 → `files/S3-EXITS-v3-2026-09-22.md`; (2) LAWS.md → `files/LAWS.md`; (3) C3 build report → `files/s3-exits-c3-build-2026-09-28.md`; (4) C3 fix r1 build report → `files/s3-exits-c3-fix-r1-build-2026-09-29.md`.
- `grok --version` → `grok 1.0.25 (f7e67d6988e2) [stable]`, exit 0, allowed.
- `tail -n 3 <report>` → last non-blank line = `<build stop>`, starts `S3 EXITS C4 BUILT ` ✓.
- `git log --oneline 78e9df82..d05ae72d`: `d05ae72d` feat(s3): C4 · `6a980cf0` wip(s3-c4): red · `0d69eeae` wip(s3-c4): E1 experiments.
- Path union: docs/40 DevDocs (cobalt/aset/store.md, aset/web.md, cards/cli.md, prefill/trade_note.md); src/cobalt/aset/store.py, aset/web.py, cards/cli.py, prefill/trade_note.py; tests/cobalt/test_prefill_trade_note.py, test_s3_c4_experiments.py, test_s3_c4_trade_note_db.py, test_s3_c4_trade_note_offline.py, trade_note_support.py; tests/fixtures/trade_note/individual-trade-template.stripped.md.
- `ls …/s3-exits-c4/.env` → No such file ✓ (exit 1, allowed).
- `ls S` → not absent (first launch staged part) → RECOVERY.
- Stagger: cto-2026-09-29.md:103 names `27-s3-exits-c4-check.md` and `no other house hub is running` ✓.
- Probes (background): OPUS → `OK` (UP; a stderr warning about a `git push*:*` deny rule in the checkout's settings, no effect). ASTRA → `OK` (UP).

## Files copied
Recovery verified, kept: `diff.part1..3` — `grep -c "^commit "` 1+1+1 = 3 = PREFLIGHT count; bytes equal a fresh `git log -p` (90,565 B, `cmp` identical). `rulings.md` holds R67, R38, R35, R37 with their commands.
`wc -c` copy = original: `20-…` 31,610 · `24-…` 28,101 · `26-…` 27,656 · report parts 34,859 + 14,111 = 48,970 · `store.py` 24,612 · `web.py` parts 37,880 + 35,681 + 14,380 = 87,941 · `cli.py` 13,293 · `trade_note.py` 18,812 · five test files (4,642 / 11,592 / 18,011 / 12,730 / 2,691) · stripped fixture 345.
The four `cp` copies (bare calls): v3 78,960 = 78,960 · LAWS.md 61,011 = 61,011 · C3 build report 45,611 = 45,611 · C3 fix r1 report 47,393 = 47,393. The whole v3 copy supersedes v3 `.part1`/`.part2` (left on disk, unnamed in `CHECK-INSTRUCTIONS.md`).
`CHECK-INSTRUCTIONS.md` written (questions verbatim, then the Files paragraph).

## CONTINUE
Run complete. Nothing further in this round.

## Clock
Seats launched 15:29 (`date`). Opus done by 15:33. Astra died on METER by 15:36. Grok done by 15:49. None past the 45-minute clock.
Written-nothing proof: `ls -la S` before the launches showed only `CHECK-INSTRUCTIONS.md`, `diff.part*`, `files/`, `rulings.md`; after, the new files are `opus-check.md`, `grok-check.md` (Grok's own write), `astra-check.partial.md` (mine). No seat wrote anything else.

## Per question
| Q | opus | astra | grok |
|---|---|---|---|
| (1) one writer | HOLDS — callers `/size` web.py:1047, fill/close/retry trade_note.py:375, :436; FIELD_ORDER :62-65 unchanged; merge renders present keys only (:127-128) | METER | HOLDS — only writer trade_note.py:221 (:268, :289); FIELD_ORDER context; merge adds only blank-fill and `every_key=False` |
| (2) after commit | HOLDS — commit store.py:326, rollback :327-329; note after return web.py:1182, :1640 | METER | HOLDS — no vault call inside `mark_filled` (store.py:198-332); note at web.py:1182, :1640 |
| (3) path + column | HOLDS — FILLED time ET trade_note.py:338; one setter store.py:419-455; NULL on failure :384-392; banner web.py:1531 | METER | HOLDS — path :338, :84-91; setter store.py:419; banner web.py:1531, :1553-1554; retry cli.py:138-159 |
| (4) his keys | HOLDS — sources :181-198; blank only :284-288; `profit_loss`/`RVOL` excluded :68. Older quirk: `5.10` re-rendered as `"5.1"` (vaultwrite/frontmatter.py:47) | METER | HOLDS — `his_fills` :181-198; `_is_blank` :170-172; tests offline.py:154-224 |
| (5) leg units | HOLDS as scoped — unit id from `seq` :425-430; called after commit web.py:1705, :1731, :1768; second write of same unit replaces his line once (X3, writer.py:724-733) | METER | HOLDS — `leg-<seq>` :201-202, :429-430; override row test db.py:245-260; refusal :419-424 |
| (6) collision | HOLDS — advisory lock + refusal store.py:429-441; create-only trade_note.py:270-274; test db.py:137-149 | METER | HOLDS — `TradeNoteRefused` :270-274; column claim store.py:430-441; test db.py:137-149 |
| (7) X14/X3/X18 | HOLDS — report :62-66; fixture stripped (24 lines); X2 recorded as the S3 smoke's | METER | HOLDS — report :58-66; X3 design-changing yes; fixture no prose |
| (8) S-NOTE / DRC seam | HOLDS — diff touches only store.py, web.py, cli.py, trade_note.py in src; no `+@app` route | METER | HOLDS — no drc.py / daily.py; web diff adds no route |
| (9) L28 | **DOES NOT HOLD** — C3 with-DB route tests (test_s3_c3_panel_db.py:84, :188) fill with no `tmp_path` vault; conftest.py:76 clears the override → dev vault; two notes on disk; not in report | METER | HOLDS — C4 tests use `make_vault` (trade_note_support.py:65-72); C3 tests not looked at |
| (10) suites | HOLDS per report (I cannot run) — 3318; 3724 + 105; F2 = F0; 146/1 | METER | HOLDS per report — same figures |
| (11) scope | NOTHING WIDENED | METER | NOTHING WIDENED (`Dejan` only in pre-existing comment prose) |
| (12) C4-06 | HOLDS — web.py:1487-1488; red report:83; green db.py:289-305 | METER | HOLDS — web.py:1487-1489; hunk `@@ -1467,9 +1479,14 @@` |
| (a) weak assertions | rollback test passed on base (db.py:205); `profit_loss` test checks only key set (offline.py:221-223); X3 tests keep silent overwrite green; no C3 route test checks vault is tmp_path | METER | `profit_loss` test empty map passes (:221-223); exit-price test doesn't assert `exit_time` (:175-179); X16 test checks prefix only (db.py:145) |
| (b) score/rank/grade/size | none | METER | none |
| CHECK line | `CHECK S3 C4: FIX (9) · ready for the deploy set: NO · C3's with-DB route tests write fill notes outside tmp_path vaults` | METER — usage limit, return `5:04 PM` (verbatim: "try again at 5:04 PM") | `CHECK S3 C4: BUILD STANDS EXCEPT X3 human-wins-once · ready for the deploy set: NO` |

## Suites
From `<report>` (facts, not re-run):
- Offline (W, `d05ae72d`): `3318 passed, 478 skipped, 1 xfailed, 20 warnings in 556.98s`, exit 0, 0 failed, 0 errors (`:259`).
- With-DB pass 1 at `0013`: `3724 passed, 7 skipped, 65 deselected, 1 xfailed, 20 warnings in 654.00s` (14 `--deselect`, byte for byte C3 fix r1's, no C4 deselect; `:266-270`). Pass 2 at `0021`: `105 passed, 5 warnings in 145.45s`. Total 3829, 0 failed.
- Rollback `--down-to 0013` → `content UNCHANGED on every table.`; `F0` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; F1 `773 · 38 · 126f2d69…`; F2 = F0 (`:278`, `:186`).
- Live-note: `146 passed, 1 skipped, 15 warnings in 25.82s`; the skip is `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC` not set) (`:280`).
- `.env`: removed, proven gone (W take 3), lock held 12:21:23 → 12:36:02 (`:279`); `ls …/s3-exits-c4/.env` at preflight → No such file.
- The first W attempt stopped FAILED on 3 stray `cobalt_dev` cards (report ESCALATE 0); the desk deleted them (R65); the counts above are the relaunch's.

## Scope
Opus (11): NOTHING WIDENED. Grok (11): NOTHING WIDENED. Astra: METER.
My PREFLIGHT path union: the 11 files listed under PREFLIGHT; no `drc/`, `settings/`, `radar/`, `db_migrations/`, `prefill/drc.py`, `prefill/daily.py`.

## Checked against the branch
| claim | who | file:line | result | note |
|---|---|---|---|---|
| C3 with-DB route tests write C4 fill notes into the dev vault, unpatched | Opus | `tests/cobalt/conftest.py:76`, `configs/dev/vault.yaml:23`, `tests/cobalt/test_s3_c3_panel_db.py:84`, `:188` | HOLDS | `test_s3_c3_panel_db.py` has no `resolve_vault_path` / `tmp_path` patch (grep of the file). Two files exist, mtime `Sep 29 09:35`: `Trade-2026-09-03 10-00-00 -ZZPB.md` and `… -TEST.md` under `~/dev-vault-cobalt/1 - Trading/2 - Trades/`; each has 2 `cobalt-legs` lines. Live vault not touched. |
| Grok's (9) HOLDS | Grok | `trade_note_support.py:65-72` | HOLDS for the C4 files only | Its cites are the C4 tests; it does not address the C3 route tests. |
| Manual `/fill` parser has no finite-and-positive guard | Opus | `src/cobalt/aset/web.py:1110-1113` | HOLDS as a fact; effect NOT CHECKABLE FROM READS | The parse is `Decimal(raw_price)` with only `InvalidOperation` caught; whether NaN reaches a leg would take the NaN red test against `/fill`. |
| X3: after his hand edit the next write of that unit replaces his line, no override row | Opus, Grok | `src/cobalt/vaultwrite/writer.py:724-733`, `:766`; report ESCALATE 1 (`:221`) | HOLDS as the builder's own disclosed finding | Design-changing: yes (report `:14`); measured offline and on the real `vault_writes` store. Pre-existing, escalated by the prompt. Not a code defect of C4. |
| `test_profit_loss_and_rvol_are_never_written` weak | Opus, Grok | `tests/cobalt/test_s3_c4_trade_note_offline.py:221-223` | HOLDS | Asserts only that the `his_fills` keys are a subset; an empty map passes; never reads a note. |
| rollback test passed on base | Opus | `tests/cobalt/test_s3_c4_trade_note_db.py:205`; report `:85` | HOLDS | Report `:85` lists it as PASSED on base ("a guard"). |
| X16 test asserts prefix only | Grok | `test_s3_c4_trade_note_db.py:145` | NOT CHECKABLE FROM READS | I did not open the test line; not counted as a defect (L70). |

Own facts:
- (i) `git log --oneline 78e9df82..d05ae72d -- src/cobalt/cards/legs.py src/cobalt/cards/store.py src/cobalt/radar src/cobalt/prefill/drc.py src/cobalt/prefill/daily.py src/cobalt/drc src/cobalt/settings src/cobalt/db_migrations` → EMPTY.
- (ii) `grep -rn -F "trade_note_path" …/s3-exits-c4/src` → the only write is `UPDATE aset_sizings SET trade_note_path = %s` at `aset/store.py:443` (`set_trade_note_path`, `:419`); every other hit is a read, a docstring, a message, migration DDL (`0021_legs.sql:112`, rollback `:13`), or a local variable in the untouched `prefill/drc.py:123-163`.
- (iii) `grep -rn "def upsert_trade_note" …/src` → ONE (`prefill/trade_note.py:221`).
- (iv) `grep -rn -F "exit_price" …/prefill/trade_note.py` → a key in `FIELD_ORDER` (`:63`), a key in `HIS_FILLED_KEYS` (`:68`), and the single fill `fills["exit_price"] = str(exits[0]["price"])` (`:197`), only when `state == "CLOSED"`, one exit leg, `flag == "confirmed"` (`:193-197`); the write itself goes through the blank test at `:258` and `:287` (I read `:181-198`, `:258`, `:284-288`).
- (iv-b) `grep -n -F "def _tap_price" …/aset/web.py` → TWO lines: `:1477` `def _tap_price(` and `:1502` `def _tap_price_source(` (a substring match). The function `_tap_price` itself is ONE.
- (v) L32: this report names only constructed tickers (`TEST`, `ZZPB`) and no date or value of his; no line of his template is in the diff (`git diff` stat lists only the stripped fixture, 24 lines, as new).

## FOR THE CLASSIFIER
- "(11) SCOPE: `NOTHING WIDENED`" · opus and grok · (11) · `git log` path union above and `diff.part1.md:10`, `:81`, `:256`, `:313` · HOLDS.
- "(8) S-NOTE AND THE DRC SEAM: `prefill/drc.py` and `prefill/daily.py` untouched" · opus and grok · (8) · check (i) above, EMPTY · HOLDS.
- "(1) ONE WRITER: `upsert_trade_note` is the only note writer" · opus and grok · (1) · `grep -rn "def upsert_trade_note"` → `prefill/trade_note.py:221` · HOLDS.
- "(3) `trade_note_path` written through one store method" · opus and grok · (3) · `aset/store.py:443` is the only `UPDATE … trade_note_path` (grep) · HOLDS.

## ESCALATE
1. **FIX (9) — Opus, `DOES NOT HOLD`; my verdict beside it: HOLDS as a defect** (the file walk above). C3's with-DB route tests (`test_s3_c3_panel_db.py:84`, `:188`) trigger the C4 fill-note hook with no `tmp_path` vault; two notes (`ZZPB`, `TEST`) are in the dev vault and the report does not name this. Because the files persist, each later with-DB run meets the X16 refusal for those names. The live vault was not touched. Grok's `HOLDS` covers only the C4 tests. Fix shape Opus names: a patch of `resolve_vault_path` to `tmp_path` for every with-DB route test (`panel_world` or an autouse fixture); the two files need removing by the desk.
2. **X3, human wins once** (builder's ESCALATE 1, both seats; Grok's only exception): design-changing, pre-existing writer behaviour, needs an owner ruling before deploy.
3. Opus: the manual `/fill` price parse has no finite-and-positive guard (`web.py:1110-1113`); effect NOT CHECKABLE FROM READS (would take the NaN red run against `/fill`).
4. Weak assertions listed under (a): `test_profit_loss_and_rvol_are_never_written`, the rollback guard test (passed on base), the X16 prefix-only assertion.
5. **Astra did not check (METER)**, message: "You've hit your usage limit … try again at 5:04 PM." Recorded, not looped. ASK DESK: relaunch Astra alone for this round after 17:04 ET? Safe default: NO — the floor is met (Opus + Grok) and the round stands (L67). [15:49 from `date`]
6. **Standing line:** Round 1 of ≤3 (L39) of S3 C4: Opus 5.5 (Fable seat, R109) · Astra · Grok (L67, R95). A HOLD → a fix round classified first (L75). `ready for the deploy set: YES` → C1–C4 are the S3 exits set for ONE deploy (L43), gated on the combined tree (L68); the deploy prompt gets its own house read (L67).

S3 EXITS C4 CHECK DONE · round: 1 · opus: CHECK S3 C4: FIX (9) · ready for the deploy set: NO · C3's with-DB route tests write fill notes outside tmp_path vaults · astra: METER · grok: CHECK S3 C4: BUILD STANDS EXCEPT X3 human-wins-once · ready for the deploy set: NO · houses that checked: 2 of 3 · defects that HOLD: 1 · ready for the deploy set: NO · ESCALATE: 6
