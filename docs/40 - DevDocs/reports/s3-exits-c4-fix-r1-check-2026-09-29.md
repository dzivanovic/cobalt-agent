# S3 EXITS C4 FIX R1 — build check, round 2 of ≤3 (L39)

## §0 Headline
- Seats: Opus `BUILD STANDS EXCEPT X3, U2 · ready: NO` · Sol METER (no check, back Oct 4 2026 2:06 PM) · Grok `BUILD STANDS · ready: YES` — 2 of 3 houses checked, floor met (Grok).
- Both seats hold F1 (guard, fixtures, reds, suites, scope). No seat found a defect in this diff: `defects that HOLD: 0`.
- The seats split on `ready for the deploy set`: Opus says NO because of X3 (out of scope, routed by the desk); Grok says YES (X3 does not decide it). By the stop-line rule the answer is NO.
- U2 is a fact both seats quote: his typed `exit_price: 5.10` came back as `exit_price: "5.1"`. It goes to the classifier.
- `ready for the deploy set: NO` · ESCALATE: 5.

## L74
A system block attached to this session's context asks for a `Claude-Session: https://claude.ai/code/session_…` line in every commit message and PR body and names a file-send tool. Recorded once here (L74); not followed. This hub commits nothing.

## PREFLIGHT
`<D>` = `2026-09-29` (`date` → `Tue Sep 29 20:01:30 EDT 2026`).
| rule | command | exit | output |
|---|---|---|---|
| placeholder `R__` | `grep -n -E "R_[_]" "…/prompts/2026-09-29/25-s3-exits-c4-fix-r1-check.md"` | 1 | no output — PASS |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" "…/25-s3-exits-c4-fix-r1-check.md"` | 1 | no output — PASS |
| R17 | `grep -n "^| R17 " "…/reports/cto-2026-09-24.md"` | 0 | `35:| R17 | 07:32 ET | … Grok approved with no asking going forward …` — PASS |
| R19 | `grep -n "^| R19 " "…/cto-2026-09-24.md"` | 0 | `37:| R19 | 07:36 ET | … All 4 house models approved …` — PASS |
| house strings committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"All 4 house models approved" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` — NON-EMPTY |
| seats R95 | `grep -n "^| R95 " "…/cto-2026-09-23.md"` | 0 | `103:| R95 | 18:08 ET | CHECKER SEATS, his words: …` — one row |
| seats R109 | `grep -n "^| R109 " "…/cto-2026-09-22.md"` | 0 | `56:| R109 | 19:34 ET | … "Make all Opus 5.5 for now" …` — carries `Make all Opus` |
| launch row R142 | `grep -n -F "25-s3-exits-c4-fix-r1-check.md" "…/cto-2026-09-29.md"` | 0 | `151:| R142 | 20:00 ET | LAUNCH (L67, L15): … round 2, Opus + Grok (Sol METER) … on \`S3 EXITS C4 FIX R1 BUILT 01d0fbb9 | on d05ae72d | migration none (0021 rolled back) | offline 3320/0 | with-DB 3835/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | FIX: 1 | RUNS: 2 | ESCALATE: 1\`; no other house hub is running | LAUNCHED` (+ `109:` R101, `158:` the session row) — carries `<build stop>` and the literal `no other house hub is running` |
| R142 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"25-s3-exits-c4-fix-r1-check.md" -- "docs/40 - DevDocs/reports/cto-2026-09-29.md"` | 0 | `5abc40c38454c8ebcce5416583023ae41ff76ab0` — NON-EMPTY |
| stagger | `grep -n -F "no other house hub is running" "…/cto-2026-09-29.md"` | 0 | the R142 row (`151:`) carries the literal and names `25-s3-exits-c4-fix-r1-check.md` — PASS |
| R35 | `grep -n -F "| R35 |" "…/cto-2026-09-28.md"` | 0 | `43:| R35 | 09:27 ET | **P-HIS — "Approved as recomended"** … O5 / O6 = A: fills only while blank (L28) …` — carries both |
| R37 | `grep -n "^| R37 " "…/cto-2026-09-29.md"` | 0 | `45:| R37 | 08:52 ET | … ready for C4: YES …` |
| R99 | `grep -n "^| R99 " "…/cto-2026-09-29.md"` | 0 | `107:| R99 | 15:51 ET | … defects that HOLD: 1 · ready for the deploy set: NO · ESCALATE: 6 …` |
| R85 | `grep -n -F "| R85 |" "…/cto-2026-09-29.md"` | 0 | `93:| R85 | 14:51 ET | — RULING … R84 → B …` — carries `R84 → B` |
| R88 | `grep -n -F "| R88 |" "…/cto-2026-09-29.md"` | 0 | `96:| R88 | 14:55 ET | — RULING … \`27\`'s four exact \`cp\` strings … \`reports/c4-check-cp-strings-2026-09-29.md\` …` — carries `four exact` and the file name |
| R88 words | `grep -n -A 2 -F "## R88" "…/cto-2026-09-29-words.md"` | 0 | `55:## R88` / `56:14:55 ET, desk chat, …` / `57:> Approved` |
| R88 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R88 |" -- "docs/40 - DevDocs/reports/cto-2026-09-29.md"` | 0 | `3abe67255c256351457554aaf189418170746829` — NON-EMPTY |
| the four `cp` strings | `grep -n -F "Bash(cp " "…/reports/c4-check-cp-strings-2026-09-29.md"` | 0 | four lines (`:11`–`:14`), each the same string as one `cp` rule on my launch line: v3, `LAWS.md`, `s3-exits-c3-build-2026-09-28.md`, `s3-exits-c3-fix-r1-build-2026-09-29.md` → `agy-trial/scratch/tribunal-bars-0920/s3-exits-c4/files/` |
| classification | `grep -n -F "S3 EXITS C4 FIX R1 DRAFTED" "<class>"` | 0 | `69:S3 EXITS C4 FIX R1 DRAFTED · FIX: 2 · NOT REAL: 12 · UNPROVEN: 2 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 7` — one line, the file's last non-blank line (69 lines) |
| `grok --version` | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` |
| built line | `tail -n 3 "<report>"` | 0 | last non-blank line = `<build stop>`, starts `S3 EXITS C4 FIX R1 BUILT ` — PASS |
| commits | `git -C /Users/cobalt/cobalt log --oneline 3e2f557b..01d0fbb9` | 0 | `01d0fbb9 fix(s3-c4): fix r1 — every trade-note test write in a tmp_path vault; a test that resolves one outside fails loud (L28, L75)` · `b493c09c wip(s3-c4-fix-r1): red` |
| stat | `git -C /Users/cobalt/cobalt log --stat --format=%h 3e2f557b..01d0fbb9` | 0 | `01d0fbb9`: `docs/40 - DevDocs/cobalt/prefill/trade_note.md` (+6), `tests/cobalt/test_s3_c3_panel_db.py` (5), `tests/cobalt/test_s3_c4_trade_note_db.py` (4). `b493c09c`: the fix report (62), `tests/cobalt/conftest.py` (+37), `test_s3_c3_panel_db.py` (+10), `test_s3_c4_trade_note_db.py` (+26), `test_s3_c4_trade_note_offline.py` (+35). Path union = 5 `tests/` files + 2 `docs/` files; no `src/`. |
| `.env` | `ls /Users/cobalt/cobalt-wt/s3-exits-c4/.env` | 1 | `No such file or directory` (never read) |
| scratch folder | `ls scratch/tribunal-bars-0920/s3-exits-c4-fix-r1` | 1 | `No such file or directory` = fresh |
| probe OPUS | `claude -p --model claude-opus-5-5 "Reply with exactly the word OK"` | 0 | `OK` — UP (a stderr warning about a `git push*:*` deny rule, no effect) |
| probe SOL | `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` | 1 | `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Oct 4th, 2026 2:06 PM.` — METER, back Oct 4th, 2026 2:06 PM; Sol not launched |
| probe GROK | none defined by the prompt | — | not probed; launched once |
| floor | ≥ 2 answer, ≥ 1 of Sol / Grok | — | MET: Opus and Grok both answered with a `CHECK S3 C4 FIX R1:` line |

## Files copied
`S` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/s3-exits-c4-fix-r1/`; `R1F` = round 1's `…/s3-exits-c4/files/`.
The four `cp` copies, each its own bare call, exactly the launch-line string — `wc -c` copy = original:
| copy | copy bytes | original bytes |
|---|---|---|
| `R1F/S3-EXITS-v3-2026-09-22.md` | 78,960 | 78,960 |
| `R1F/LAWS.md` | 61,011 | 61,011 |
| `R1F/s3-exits-c3-build-2026-09-28.md` | 45,611 | 45,611 |
| `R1F/s3-exits-c3-fix-r1-build-2026-09-29.md` | 47,393 | 47,393 |

Every other copy is a Read → Write, and each was checked with `cmp` (identical) as well as `wc -c` (`cmp`, `cat`, `head` and `tail` were used read-only for that byte check):
| file under `S/` | bytes | original |
|---|---|---|
| `diff.part1.md` | 9,736 (part 1 of 1) | `git log -p 3e2f557b..01d0fbb9 -- . ":(exclude)docs"` (2 commits = PREFLIGHT's count) |
| `rulings.md` | 1,679 | the `grep -n` lines of R35, R37, R99 under their commands |
| `packet.md` | 26,402 | `<report>`'s six sections in order (ceiling 300,000 B) |
| `files/s3-exits-c4-fix-r1-build-2026-09-29.md` | 31,744 | `<report>` 31,744 |
| `files/s3-exits-c4-fix-r1-draft-2026-09-29.md` | 12,422 | `<class>` 12,422 |
| `files/s3-exits-c4-check-2026-09-29.md` | 15,310 | `<r1>` 15,310 |
| `files/s3-exits-c4-build-2026-09-29.md.part1` + `.part2` | 34,859 + 14,111 = 48,970 | `<c4>` 48,970 (cut before `## ESCALATE`) |
| `files/24-s3-exits-c4-fix-r1-build.md` | 27,158 | 27,158 |
| `files/26-s3-exits-c4-build.md` | 27,656 | 27,656 |
| `files/wt/tests/cobalt/conftest.py` | 11,681 | worktree at `<tip>` |
| `files/wt/tests/cobalt/test_s3_c3_panel_db.py` | 26,712 | worktree at `<tip>` |
| `files/wt/tests/cobalt/test_s3_c4_trade_note_db.py` | 19,371 | worktree at `<tip>` |
| `files/wt/tests/cobalt/test_s3_c4_trade_note_offline.py` | 14,389 | worktree at `<tip>` |
| `files/wt/docs/40 - DevDocs/cobalt/prefill/trade_note.md` | 6,182 | worktree at `<tip>` |
| `files/wt/src/cobalt/prefill/trade_note.py` | 18,812 | worktree at `<tip>` |
| `files/wt/src/cobalt/prefill/vault_writer.py` | 2,290 | worktree at `<tip>` |
| `files/wt/src/cobalt/aset/web.py.part1` + `.part2` + `.part3` | 37,880 + 35,681 + 14,380 = 87,941 | worktree at `<tip>` (cut at lines 819 / 1599) |
| `CHECK-INSTRUCTIONS.md` | 6,390 | the QUESTIONS verbatim, then the Files paragraph |
Not copied: his vault notes, his template, the dev vault's notes (L32). `trade_note_support.py` is not on the prompt's list and was not copied.
Seat outputs: `S/opus-check.md` (6,377 B, written by me from Opus's stdout; the one stderr line about the deny rule left out) and `S/grok-check.md` (7,120 B, written by Grok itself, not rewritten by me).

## CONTINUE
done — both seats answered; collated below. Sol was not launched (METER).

## Clock
Seats launched 20:19 ET (`date` → `Tue Sep 29 20:19:24 EDT 2026`). Opus done by 20:23. Grok's file last written 20:34; its task was reported complete when I checked at 20:35. Neither is past the 45-minute clock.
Written-nothing proof: `ls -la S` before the launches: `CHECK-INSTRUCTIONS.md`, `diff.part1.md`, `files/`, `packet.md`, `rulings.md`. After: the same plus `opus-check.md` (mine) and `grok-check.md` (Grok's own write). No seat wrote anything else.

## Per question
| Q | opus | sol | grok |
|---|---|---|---|
| (i) red first | HOLDS — reds on `d05ae72d`, tests-only red commit; 14 tests + new test ERROR at teardown (`packet.md:49-67`); `KeyError: 'vault'` (`packet.md:69`); no other reason | METER | HOLDS — same; progress line `.E`×14 + `FE`; guard text names the ZZPB and TEST dev-vault paths (`packet.md:68`) |
| (ii) F1 | HOLDS — one resolver `trade_note.py:256`, `:422`; guard `conftest.py:266-290`, raise `:282-284` before any read/write; web helpers catch `Exception` (`web.py:1551`, `:1570`), teardown `pytest.fail` `:289-290`; no allowlist | METER | HOLDS — same cites; `panel_world` `test_s3_c3_panel_db.py:45-50`, `note_world` `:41-49`; `make_vault` `trade_note_support.py:65-72`; no allowlist, skip or carve-out |
| (iii) runs, suites, scope | HOLDS — U1 200/200, nothing written; U2 `5.10` → `"5.1"` (`packet.md:27-39`); offline 3320, with-DB 3728 + 107, live-note 146; F2 = F0; `.env` gone; NOTHING WIDENED. Dev-vault after-listing: a desk summary only (`cto-2026-09-29.md:129`) | METER | HOLDS — same figures and cites. Dev-vault listings: NOT CHECKABLE FROM READS (only the before listing is in the files). X3 does not decide ready |
| (a) weak assertions | NONE (env note: the offline guard test needs the dev-vault trades folder to exist, `vault_writer.py:32`) | METER | NONE (`test_s3_c3_panel_db.py:512-513`; offline guard test `:304-308`) |
| (b) score/rank/grade/size | NO PATH — tests only | METER | NO PATH — no file under `src/` |
| CHECK line | `CHECK S3 C4 FIX R1: BUILD STANDS EXCEPT X3 (out of scope, routed), U2 (for the classifier) · ready for the deploy set: NO` | METER — usage limit, back Oct 4th, 2026 2:06 PM (probe text, verbatim above) | `CHECK S3 C4 FIX R1: BUILD STANDS · ready for the deploy set: YES` |

## Suites
From `<report>` (facts, not re-run):
- Offline (E2, `01d0fbb9`-era tests): `3320 passed, 480 skipped, 1 xfailed, 20 warnings in 556.66s`; W (a): `3320 passed, 480 skipped, 1 xfailed, 20 warnings in 554.51s (0:09:14)`, exit 0, 0 failed, 0 errors. E0 on the base: `3318 passed`.
- With-DB pass 1 at `0013`: `3728 passed, 7 skipped, 65 deselected, 1 xfailed, 20 warnings in 660.67s`, exit 0 (fourteen `--deselect`, C4's byte for byte; no C4 deselect). Pass 2 at `0021`: `107 passed, 5 warnings in 147.58s`, exit 0. Total 3835, 0 failed. `grep -c "outside tmp_path"` → `0` in both.
- F0 `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; F1 `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; rollback `--down-to 0013` → `content UNCHANGED on every table.`; F2 = F0.
- Live-note: `146 passed, 1 skipped, 15 warnings in 25.54s`; the skip is `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC` not set).
- `.env`: removed, proven gone after take 1 (17:30:10 → 17:31:16) and take 2 (17:41:48 → 17:56:57). Two lock takes.
- RESTARTS: `RESTARTS: none`.
- U1: `/fill` with `NaN` and with `-1` → 200 (the sheet page), counts unchanged, `legs 0 → 0`, card TRIGGERED, `actual_fill=None`, `trade_note_path=None`. No 500, no NaN or negative price stored.
- U2: `exit_price` before `'exit_price: 5.10'`, after `'exit_price: "5.1"'` — the line changed (quotes added, trailing zero dropped). `entry_time` / `exit_time` render quoted.
- The two developer-vault notes, my own `ls -la` at 20:2x ET: `TEST.md` 767 B and `ZZPB.md` 665 B, both `Sep 29 09:35` — equal to the desk's before listing in `<report>` (`767` / `665`, `09:35`). I did not read the notes.

## Scope
Opus (iii): NOTHING WIDENED. Grok (iii): NOTHING WIDENED. Sol: METER.
My PREFLIGHT path union: five `tests/` files (`conftest.py`, `test_s3_c3_panel_db.py`, `test_s3_c4_trade_note_db.py`, `test_s3_c4_trade_note_offline.py`) and two `docs/` files (`cobalt/prefill/trade_note.md`, the fix report); no file under `src/` or `configs/`. Against `24`'s NOT IN THIS FIX: no `src/`, no `vaultwrite/`, no X3 test, no `/fill` parse, no weakened assertion. (The stat lists four distinct `tests/` files.)

## Checked against the branch
| claim | who | file:line | result | note |
|---|---|---|---|---|
| The guard patches the one resolver and nothing else patches it | Opus | `tests/cobalt/conftest.py:277`, `:287` | HOLDS | `grep -rn -F "resolve_target" tests` → only `conftest.py:277`, `:287` and the guard's own test `test_s3_c4_trade_note_offline.py:306`. |
| Both writers look `resolve_target` up in the module at call time | Opus, Grok | `src/cobalt/prefill/trade_note.py:256`, `:422` | HOLDS | Read: `upsert_trade_note` and `write_leg_unit` call the module-level name imported at `:51`; `write_card_note` reaches it through `upsert_trade_note` (`:375`). |
| `set_trade_note_path` runs before the guard trips | Opus | `trade_note.py:373`, `:375` | HOLDS | Read: the path is claimed at `:373`, then `upsert_trade_note` (`:375`); on failure it is set NULL (`:386`). A DB write in the suite's rolled-back transaction, not a vault write. |
| `make_vault` patches `resolve_vault_path` | Opus, Grok | `tests/cobalt/trade_note_support.py:71` | HOLDS | `grep` → `:71: monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: vault_root)`. |
| `note_world` is not a `make_vault` caller | task (iv) | `grep -rn -F "make_vault("` | HOLDS | Callers: `test_s3_c3_panel_db.py:50` (`panel_world`), `test_s3_c4_experiments.py:117,177,207`, `test_s3_c4_trade_note_db.py:367` (the X3 test, own `tmp_path`), `test_s3_c4_trade_note_offline.py:86`; none in `note_world`. |
| U2: his typed `exit_price: 5.10` is re-rendered `"5.1"` | Opus, Grok | `packet.md:27-39`; `trade_note.py:113-118`, `:282-293` | HOLDS as a run result | The quoted output shows the change. The render is `_render_value` (quotes every key but `date` / `symbol` / `trade_def`) on the merged dict; the fix site Opus names (`trade_note.py:113-118`) is where the quoting is. Nothing was fixed in this round (NOT IN THIS FIX). |
| The two developer-vault listings equal before and after | Grok (NOT CHECKABLE) | `/Users/cobalt/dev-vault-cobalt/1 - Trading/2 - Trades/…` | HOLDS | My `ls -la`: `TEST.md` 767 B, `ZZPB.md` 665 B, `Sep 29 09:35` — equal to `<report>`'s desk listing. |
| The offline guard test needs the dev-vault trades folder | Opus (env note) | `src/cobalt/prefill/vault_writer.py:32` | HOLDS | Read: `resolve_target` raises `VaultWriteError` if `path.parent` is not a directory, before the guard runs. It fails loud; it never passes falsely. Not a defect. |
| NOTHING WIDENED; no `src/` | Opus, Grok | `git log --oneline 3e2f557b..01d0fbb9 -- src configs` | HOLDS | EMPTY (my own call). |

Own facts, each its own call:
- (i) `git -C /Users/cobalt/cobalt log --oneline 3e2f557b..01d0fbb9 -- src configs` → EMPTY.
- (ii) `git -C /Users/cobalt/cobalt log --stat --format=%h 3e2f557b..01d0fbb9` → only `tests/` and `docs/` paths (the stat above).
- (iii) `grep -n -F "resolve_target" /Users/cobalt/cobalt-wt/s3-exits-c4/tests/cobalt/conftest.py` → `:277` (`original = trade_note_module.resolve_target`) and `:287` (`monkeypatch.setattr(trade_note_module, "resolve_target", guarded)`).
- (iv) `grep -rn -F "make_vault(" /Users/cobalt/cobalt-wt/s3-exits-c4/tests/cobalt` → the callers listed above; every fixture `<report>` names (`panel_world`; `note_world` reusing it) is accounted for and `note_world` is not a caller.
- (v) the two developer-vault notes: sizes and mtimes equal to `<report>`'s two listings (above).
- (vi) L32: this report names only constructed tickers (`ZZPB`, `TEST`), the frozen-clock date and the desk's byte sizes; no value of his, no note text.

## FOR THE CLASSIFIER
- "The guard wraps the ONE resolver the trade-note writer uses (both `upsert_trade_note` and `write_leg_unit`), raises before any read or write, and fails the test loud at teardown" · opus and grok · (ii) · `trade_note.py:256`, `:422`; `conftest.py:266-290`; `grep -rn -F "resolve_target" tests` → `conftest.py:277,287` only · HOLDS.
- "Every test that posts a fill or a leg tap resolves its note inside `tmp_path` (`panel_world`; `note_world` reusing its vault)" · opus and grok · (ii) · `test_s3_c3_panel_db.py:50`; `test_s3_c4_trade_note_db.py:41-49`; `grep -rn -F "make_vault("` (above) · HOLDS.
- "The two developer-vault listings are equal before and after" · grok said NOT CHECKABLE, opus a summary only · (iii) · my `ls -la`: 767 B / 665 B, `Sep 29 09:35` · HOLDS.
- "NOTHING WIDENED (no file under `src/`)" · opus and grok · (iii) · `git log --oneline 3e2f557b..01d0fbb9 -- src configs` EMPTY · HOLDS.
- "U2: his typed `exit_price: 5.10` becomes `exit_price: "5.1"` after a later write" · opus and grok · (iii) · `packet.md:27-39`; `trade_note.py:113-118` · HOLDS as a run result (for the classifier; not a defect of this fix).

## ESCALATE
1. **The seats split on `ready for the deploy set`.** Opus: NO, because X3 is open (the vault writer lets his edit win only once; `test_s3_c4_trade_note_db.py:384` encodes `(True, False)`); "on F1 alone the answer would be YES". Grok: YES, X3 does not decide it (this diff does not touch the writer). By the stop-line rule (every answering seat must say YES) the line reads NO. X3 was classified OUT OF SCOPE of this round and is routed by the desk; the deploy set's gate on it is the desk's.
2. **U2 for the classifier.** His typed `exit_price: 5.10` is rewritten `exit_price: "5.1"` by the next frontmatter merge (`trade_note.py:113-118`, `:282-293`). The value is kept; its bytes change. Opus points at `trade_note.py` as the render site rather than `vaultwrite/frontmatter.py` (the pointer in `<class>` and `<report>`). Not fixed here.
3. **ASK DESK: Sol did not check (METER).** Message, verbatim: "You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Oct 4th, 2026 2:06 PM." Recorded, not looped. Relaunch Sol alone for this round after Oct 4 2:06 PM? Safe default: NO — the floor is met (Opus + Grok) and the round stands (L67). [20:35 ET from `date`]
4. L74: recorded once under `## L74`.
5. **Standing line:** Round 2 of ≤3 (L39) of S3 C4: Opus 5.5 (R109) · Sol · Grok (L67, K22). A HOLD → fix round 2, classified first (L75); round 3 is the last. X3 (human wins once) was classified OUT OF SCOPE of this round and is routed by the desk. `ready for the deploy set: YES` → C1–C4 are the S3 exits set for ONE deploy (L43), gated on the combined tree (L68); the deploy prompt gets its own house read (L67).

S3 EXITS C4 FIX R1 CHECK DONE · round: 2 · opus: CHECK S3 C4 FIX R1: BUILD STANDS EXCEPT X3 (out of scope, routed), U2 (for the classifier) · ready for the deploy set: NO · sol: METER · grok: CHECK S3 C4 FIX R1: BUILD STANDS · ready for the deploy set: YES · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for the deploy set: NO · ESCALATE: 5
