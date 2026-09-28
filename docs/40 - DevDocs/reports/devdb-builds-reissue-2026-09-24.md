# DEV-DB BUILDS RE-ISSUE — 2026-09-24 (`41`, seat `devdb-builds-reissue-0924`, Opus 5.5)

## §0 Headline
- I wrote five prompts and launched none: `42` (stale-score build, resumes `46`'s wip after rebasing onto main), `43` (H1 build, re-cut from main), `44` and `45` (their checks: Opus 5.5 + Grok, no Gemini), and `46` (tonight's smoke look, 21:40–23:30 ET).
- Both builds drop `cobalt db migrate` (L76). Each migration is proven only inside the suite's own rollback transaction. Each build runs offline, with-DB and live-note tests before BUILT (L68 GATE EARLY). Each stop line now carries `cobalt_dev: 0013`.
- New rule strings: **2**, both in `42`: the stale-score rebase pair. No approved line carries a stale-score rebase, and the prompt makes the build do its own rebase. Everything else comes from approved lines (proven by `comm`, table below).
- ESCALATE: 7.

## L74
No block arrived inside a tool result. The session's own system prompt does carry a `Claude-Session:` attribution line. I made no commit, so it was never used.

## AUTHORIZATION
| gate | result (16:0x ET) |
|---|---|
| `grep -n "^| R62 " cto-2026-09-24.md` | `73:| R62 | 15:5x ET | … **LAUNCH `prompts/2026-09-24/41-reissue-devdb-builds-r2.md`** …` ✓ |
| `grep -n "^| R58 " cto-2026-09-23.md` | `61:| R58 | 13:2x ET | His words: "yes start both" …` ✓ |

## DECISIONS
| # | decision | source |
|---|---|---|
| 1 | **`46`'s RESUME.** `42`'s STEP-R commits its PREFLIGHT report first, then runs `git -C …/stale-score rebase main`. The wip commits `1a5c6928` and `57925f3b` come along. A conflict means `rebase --abort` and `FAILED: rebase — <files>`, never a blind resolve. The ancestry proof is `git log HEAD..<main tip>` empty plus `<main tip>..HEAD` = 3 lines; `git merge-base` is not on the list, so `git log` stands in for it. After the rebase it re-runs X10, X18/X19 and X20/X22, and re-locates every `v2 cite → rebased line`. BASELINE runs all three suites. It names **15 expected REDs**, all in `tests/cobalt/test_stale_score.py`: `46`'s STEP-2 red table (17 tests: 15 RED, 2 GREEN). Any other failing test counts as a real red. Then STEP-2 C continues. `46`'s `## CONTINUE` "`cobalt db migrate`" step is void. | `git cherry -v main cards/stale-score-0922` = 2 `+` lines (setups and seam pin `51afdad0` are patch-equal on main as `583852a8`); `git log 51afdad0..HEAD -- src configs` = 0 lines (no conflict surface in `evaluate.py`); `stale-score-build-2026-09-23.md:173-193, :231-238`; L54, L60 |
| 1b | **`46`'s ASK DESK (its ESC 1: `0015` or `0016`?) is answered: `0015`.** The branches settle it. `drc/d1-trading-log` carries `0016_drc.sql`, `voice/v1-0923` carries `0017_voice_turns.sql`, and the K1 drafter pins `0018`. The 09-23 desk rows R62/R63/R66 were overtaken by what got built. | `git ls-tree … db_migrations/`; `38-draft-drc-k1-build.md:11`; `devdb-builds-reissue-2026-09-23.md` `## MIGRATION SEAM` |
| 2 | **`47`'s BASE.** The desk re-cut line is `git -C /Users/cobalt/cobalt-wt/handicap-h1 checkout -B radar/handicap-h1-0922 main`, placed in `43`'s header. Nothing was ever built on the branch. `be4c79b5` is a 09-22 main commit (`log -3` shows three desk docs commits), `merge-base --is-ancestor radar/handicap-h1-0922 main` exits 0, and the worktree is clean. `0014` goes directly on `0013`. PREFLIGHT proves `a2d320b8` is below the base. | desk `git log` / `merge-base` (16:0x); `ls src/cobalt/db_migrations` on main = `…0011, 0013` |
| 3 | **MIGRATIONS UNDER L76.** Every `cobalt db migrate` step and string is gone from both builds (a negative gate greps each file for a count of 0). `0014`/`0015` are written, registered in `FORWARD`/`REVERSE` and proven only through `_apply(conn, FORWARD)` on `db.connect_migration` with rollback. The existing tests that already apply every registered migration inside a rollback: `test_archiver_migrations.py:407` (`test_forward_creates_both_tables_on_the_system_side`), `:424` (`…idempotent…`), `:441` (`test_rollback_down_to_0009…`), and `test_p4_migrations.py:403` (`test_0008_0009_apply_twice_reverse_and_reapply_on_populated_membership`), `:456`, `:518`. `test_tenancy.py::TestMigrationRoundTrip` (`:686`) commits through a subprocess, so both builds **deselect** it (`14` D7 precedent) and the deploy gate runs it. `placement.py`: `shadow_agreement_v` is already `Side.USER` (`placement.py:100`), and `0014` adds columns only, so neither build needs a change there. The absence probes are XL76 modules reading `pg_catalog`: `pg_get_viewdef` for `0015`, and `pg_attribute` count = 0 for `0014`. They run alongside the table-set probe `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`. Re-points under A1 are named: `test_assumed_store.py:244-245` and `test_archiver_migrations.py:80-105` pin `0013` as last. | L76; `14-drc-d1-fix-r1-build.md:106-111`; test files read 16:0x |
| 3b | **H1's L76 seam, settled by a first-gate experiment and never by judgement.** Once `apply_membership`/`members_for_day`/`open_members` name the three new columns, any existing with-DB test that reaches `system.radar_membership` on a `cobalt_dev` at `0013` would fail. Nine test files call those functions. `43` adds **XL76**: list the callers, prove the `migrated` harness shape (`drc/d1-trading-log:tests/cobalt/test_drc_store.py:217-235`), and time one `_apply`. Outcome (A): one fixture `migrated_radar` goes in a new support module, `conftest.py` stays untouched, and the moved callers are listed with assertions unchanged. Outcome (B): `FAILED` with a design question for the desk. Stale-score has no such seam, because `0015` is a view only. | `grep -rln "apply_membership\|members_for_day\|open_members" tests/cobalt` = 9 files |
| 4 | **GATE EARLY.** Both builds carry the live-note step and string: `03` D4's command byte for byte, READ-ONLY, `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think`. The stop lines carry `offline <p>/<f> \| with-DB <p>/<f> \| live-note <p>/<f>`. The expected state comes from R56 of 09-24: `131 passed, 0 failed`, exactly four AWAITING lines (backside and fashionably-late awaiting a ruling, hitchhiker awaiting a day, vwap-continuation awaiting its engine fill, `dist.k.vwap null`), and the second-chance pin lifted. A different result at BASELINE is an ESCALATE, never "expected red". CLOSE must match BASELINE. | `cto-2026-09-24.md` R9, R56; `assumed-rows-write-2026-09-24.md:222` |
| 5 | **CHECK SEATS.** `44` and `45` use Opus 5.5 + Grok. Sol is on METER until `Sep 26th, 2026 6:47 AM` (recorded) and is probed only after that. `"Bash(agy *)"` is removed, a strict subset. The line is `15`'s byte for byte. The grok gate is R17 (+R19). The packet gains `52-suites.md` (the three suites' executed output) and a question on the suites. Fail closed below TWO. The stop line follows `15`'s shape. | L67 (09-24 amend), 09-23 R95/R97, 09-24 R17/R19; `15-drc-d1-fix-r1-check.md:1` |
| 6 | **THE SMOKE LOOK.** `46-s2-smoke-look.md` = `09` re-issued for 09-24: remote-control `s2-smoke-look-0924`, report `reports/s2-smoke-look-2026-09-24.md`, date gate 2026-09-24, window 21:40–23:30 unchanged, strings byte for byte. The verdict rule no longer decides S2 (R113). It reports the replay, K9.4, K17's absence (R114), every colour, and `smoke green: yes\|no` with the first failing clause. `R113` places nothing tonight. The K9.4 proof quotes `07`'s build ESC 1 verbatim: K9.4 PASS with `not_archived` printed, `not_archived` = `archive_partial_by_side` on both sides (K9.9/K9.12 PASS), and K9.8/K9.11 reading a present key. | `mover-bars-fix-build-2026-09-24.md:169`, `§0`; `configs/cobalt/smoke/s2.yaml:356-490` (main: K9.7–K9.12 present, no K17) |

## DELTA
**Rule-string arithmetic (desk `comm`, 16:1x, launch lines extracted from each file):**
| file | vs | removed | added |
|---|---|---|---|
| `42` | `46` | `"Bash(COBALT_ENV=dev uv run cobalt db migrate)"` | `"Bash(COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *)"` (09-23 R52) · `"Bash(git -C /Users/cobalt/cobalt-wt/stale-score rebase main)"` **NEW** · `"Bash(git -C /Users/cobalt/cobalt-wt/stale-score rebase --abort)"` **NEW** |
| `43` | `47` | `"Bash(COBALT_ENV=dev uv run cobalt db migrate)"` | `"Bash(COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *)"` (09-23 R52) |
| `44` | `50` / `15` | `"Bash(agy *)"` / — | — / — (= `15` byte for byte) |
| `45` | `51` / `15` | `"Bash(agy *)"` / — | — / — (= `15` byte for byte) |
| `46` | `09` | — | — |

### 46 → 42
| where | old → new |
|---|---|
| line 1 | re-issue of `31` for 09-23 → re-issue of `46` for 09-24 that RESUMES the wip (why `46` stopped: 09-23 R73; what changed: setups on main, L76, GATE EARLY) |
| line 1 MODE | quoted verbatim from `46`, plus one sentence: under L76 no dev migrate at all, which narrows the rule and never widens it |
| line 1 strings | `31`'s line byte for byte → `46`'s −1 +1 +2 (the table above); the `.env` pair stays on R64 |
| line 1 DESK | "fills the BASE; `worktree add` at `51afdad0`" → a DESK LINE: L76 lock, queue order `36` / `39` before, `43` after; the desk runs no rebase; launch row `R__` |
| seat / report | `stale-score-0923` / `…-2026-09-23.md` → `stale-score-r2-0924` / `…-2026-09-24.md` (the 09-23 report stays as history, cited) |
| title | "cut from `51afdad0`, stacks on setups" → "rebased by you onto `main` at STEP-R"; LADDER `S2-P2 · F10` → `S2 · F10 carry-over` |
| WHAT IS RULED | R42 "byte-identical to `51afdad0`" → "…to `<main tip>`"; migration seam extended to `0016` D1 / `0017` voice / `0018` K1, and it answers `46`'s ASK; new **L76** bullet (rollback-transaction pattern, `file:line`; the deselect) |
| INDEX CARD | adds L46/L54 (rebase), L68 GATE EARLY, L76; item 2 = `46`'s own report (history); item 6 = `03` D4 / `14` D3/D7 |
| STOP LINE | `… on <base> \| experiments … \| offline \| with-DB \| migration: <0015\|none> \| version: … \| .env: removed, proven gone …` → the ordered shape: `on <main tip> \| rebased: yes \| red <hash> \| offline \| with-DB \| live-note \| migration: <0015\|none> rolled back \| cobalt_dev: 0013 \| .env: removed \| experiments …`; `version:` dropped (the ordered shape omits it) |
| AUTHORIZATION | adds a placeholder gate, R9/R10/L76, R52 (live-vault string), the rebase pair gated on a committed row of his, and a NEGATIVE gate (migrate string count 0); R66 → `R__`; greps `46`, not `31` |
| UNATTENDED | allows the two rebase strings; forbids `cobalt db` and `git merge-base` by name |
| LANE GATE → THE LOCK | adds (c) exactly one `.env` after `cp` and (d) rm + proof after every with-DB call (`14`) |
| PREFLIGHT | seam-pin/base checks → the wip is `57925f3b`/`1a5c6928`, `--cherry-pick --right-only` shows exactly those 2, the wip touches no `src`, the live strategies folder exists |
| new STEP-R | the rebase, conflict rule, ancestry proof, re-runs, rebased cite table |
| BASELINE | two suites + `cobalt db migrate` → three suites, no migrate, the deselect, the 15 named REDs, R56 known state, table-set probe |
| STEP-1 | full experiment list → CARRIED (17/17 from `46`, four re-run at STEP-R) |
| STEP-2 | T to be written → `46`'s T already written and RED, re-quoted; the rest unchanged |
| STEP-3 | `.env` pair → THE LOCK; rollback via `dev_db_tx` named; `0015` "SETTLED" wording |
| STEP-4 (iv) | "then `COBALT_ENV=dev … db migrate`" → proven only inside the test's rollback (`test_p4_migrations.py:403`, `test_archiver_migrations.py:407-436`); A1 names the two registry pins; `placement.py` stays unchanged |
| CLOSE | two suites → three suites with gates, plus XL76 `0015` absence probe and table-set probe; `cobalt_dev: 0013` or UNPROVEN |
| CLOSE L68 | drops `setups/seven-0921` (merged); adds `drc/d1-trading-log`, `voice/v1-0923`, `replay/mover-partial-0924`, `test_replay_runner.py` |
| FOR THE DEPLOY / `FOR 50` → `FOR 44` / ESCALATE | the stack is now "rebased onto main"; the gate runs the deselected class; ESC adds (ix) the deselect and (x) the live-note difference |
| NEXT STEP | `50` (Grok · Gemini · Opus) → `44` (Opus 5.5 + Grok) |

### 47 → 43
| where | old → new |
|---|---|
| line 1 | re-issue of `27` for 09-23 → re-issue of `47` for 09-24 (never launched; the deploy gate is met; L76; GATE EARLY) |
| line 1 MODE | quoted verbatim from `47`, plus the L76 narrowing sentence |
| line 1 strings | `27` byte for byte (with `53-deploy-d3` for migrate) → `47`'s −1 +1; the `.env` pair stays on R30 |
| line 1 LAUNCH GATE | "`41` DONE + `46` stopped; `merge --ff-only main`" → a DESK LINE (L76 lock; `36`/`39`/`42` ahead) + the desk re-cut `checkout -B radar/handicap-h1-0922 main`, with ancestry evidence |
| seat / report | `handicap-h1-0923` / `…-2026-09-23.md` → `handicap-h1-r2-0924` / `…-2026-09-24.md`; LADDER → `S2 · F10 carry-over` (still off-ladder R28/R29) |
| WHAT IS RULED | migration seam gains `0016`/`0017`/`0018` with branch evidence; new **L76** bullet naming the membership-store seam |
| INDEX CARD | adds L68 GATE EARLY, L76; the cite list adds `test_archiver_migrations`, `test_assumed_store`, `conftest.py` `dev_db_tx`, `cli.py` `_apply`; item 5 = `03` / `14` |
| STOP LINE | `… with-DB \| migration: 0014 \| h=1 identity \| .env: removed, proven gone …` → `… with-DB \| live-note \| migration: 0014 rolled back \| cobalt_dev: 0013 \| h=1 identity: proven \| .env: removed …` |
| AUTHORIZATION | adds a placeholder gate, R9/R10/L76, a `deploy-2026-09-24` = `a2d320b8` check, R52 and a NEGATIVE gate; the `tail` of `deploy-2026-09-23-r2.md` and of `46`'s report are removed (the gate is met; the lane is now the lock); greps `47` |
| UNATTENDED / LOCK / PREFLIGHT | `cobalt db` forbidden; LANE GATE → THE LOCK (c)(d); PREFLIGHT "still `be4c79b5`" → "not re-cut"; adds the `a2d320b8` ancestry and strategies-folder checks; a lock FAIL at PREFLIGHT no longer stops (offline work runs on) |
| BASELINE | two suites + migrate → three suites, no migrate, the deselect, R56 known state |
| STEP-1 | adds **XL76** (the harness, with a decision table) and its STOP |
| STEP-5 | "THEN THE MIGRATION ON `cobalt_dev` … `db migrate`" → rollback-transaction tests only; seeding precedent `test_p4_migrations.py:387`; A1 names the registry pins and the moved callers; `placement.py` unchanged |
| STEP-6 (iv) | adds "inside the `migrated_radar` rollback" |
| CLOSE | three suites with gates; XL76 `0014` absence probe (`pg_attribute`); empty diffs add `conftest.py` and `placement.py`; L68 list adds `drc/d1-trading-log`, `voice/v1-0923` and the two pin tests, and drops the merged setups/smoke-fix branches |
| FOR THE DEPLOY / `FOR 51` → `FOR 45` / ESCALATE | production is at `0013` from `deploy-2026-09-24`; the gate runs the deselected class; ESC adds (xi) the deselect and harness and (xii) the live-note difference |

### 50 → 44 (and 51 → 45, the same deltas on H1's text)
| where | old → new |
|---|---|
| line 1 seats | Grok · Gemini · Sol · Opus, floor THREE (R46) → Opus 5.5 · Sol · Grok per R95/R96/R97, Opus + Grok until Sol returns `Sep 26th, 2026 6:47 AM`, floor TWO |
| line 1 strings | `32`/`28`'s 15 (= `06`) → `15`'s 14 byte for byte (= `50`/`51` − `"Bash(agy *)"`); R17/R19 standing; no dated extension |
| AUTHORIZATION | R13/R46/R49/R30/R32 greps + the DATE + EXTENSION GATE → a placeholder gate, THE GROK GATE (R17/R19), R95/R97, and a check that the line is `15`'s; an `agy` string on the line → FAILED |
| PREFLIGHT | BUILT line fields add `live-note`, `cobalt_dev: 0013`, `rebased: yes` (`44`); base check → `main` ancestry (`<tip>..<main tip>` empty, `a2d320b8` under the base); probes → `15`'s (Sol keyed on `date`); `agy --version` removed |
| packet | adds `52-suites.md` (BASELINE + CLOSE executed output); `10-rulings.md` adds R95/R97/R9/R10 |
| questions | adds (15)/(14) THE SUITES; (7) adds "proven only inside rollback" (and for `45`, the XL76 harness); a no-ticker / no-value line |
| §2 launch | `66` §2 with Gemini → `04` §2 GROK/OPUS, `54` §2 Sol |
| §3 | new `## Suites` table; file-check (xi) L76; stop line `15`'s shape with `gemini: NOT SEATED (R96/R97)` |
| report | `…-check-2026-09-23.md` → `…-check-2026-09-24.md`; remote-control `…-check-r2-0924` |

### 09 → 46
| where | old → new |
|---|---|
| line 1 | path `09` / remote `s2-smoke-look-0923` → `46` / `s2-smoke-look-0924`; strings unchanged |
| title | "the CLOSING LOOK … S2 CLOSES on …" → S2 CLOSED (R113), K17 out (R114); this look decides nothing about S2; first post-deploy replay night for the mover-bars fix |
| AUTHORIZATION | row `R111` of 09-23 → placeholder gate + `R__` of 09-24 + a committed-row check; adds R113/R114 greps |
| INDEX CARD | adds L73; s2.yaml note (K9.7–K9.12 present, K17 absent); (6) `deploy-2026-09-23.md` → `deploy-2026-09-24-reland.md` + the 09-23 look; new (7) the K9.4 proof, `07` ESC 1 quoted verbatim |
| steps 1–3 | date 09-23 → 09-24; deploy tail/tag → the reland report + `deploy-2026-09-24`; `unranked_rows` grep → `archive_partial_by_side` grep + K17 absence; replay line adds `· partial <n>` |
| step 5 | the K17 files row → a K9 rows block (K9.1/4/7–12); a printed K17 row counts as a real red |
| step 6 | "S2 CLOSE VERDICT" → "SMOKE GREEN" (same three clauses; `fix not live` and `UNPLACED` are real; R113 places nothing tonight) + K9.4's stop-line field |
| report / stop line | `…-2026-09-23.md` → `…-2026-09-24.md`; stop line → `S2 SMOKE LOOK DONE · deploy: deploy-2026-09-24 · replay ran · checks · K9.4: <value> (<PASS\|FAIL>) · real reds · smoke green · ESCALATE` |

## OWNER ITEMS
NONE.

## FOR DEJAN
Two new strings, both for `42` (stale-score build). L54 says the build rebases its own branch onto main first, and no approved line carries a rebase for this worktree. They follow the shape of your 09-23 R52 `setups-c1` pair:
1. `Bash(git -C /Users/cobalt/cobalt-wt/stale-score rebase main)`
2. `Bash(git -C /Users/cobalt/cobalt-wt/stale-score rebase --abort)` (used only on a conflict, which then ends the run `FAILED`)

`42`'s AUTHORIZATION refuses to run until a committed row of yours carries both strings. Every other string, in all five prompts, is already on an approved line (table above).

## ESCALATE
1. **The two rebase strings (FOR DEJAN) gate `42`.** If he declines, the desk can run the rebase itself instead (desk commands are not hub strings). `42` would then be re-issued without the pair (L19), and STEP-R would find the ancestry already true. ASK DESK: take his approval, or the desk rebases? [16:19]
2. **`44`/`45` seat reading.** The prompt ruled these checks "other checks": Opus · Sol · Grok. The desk's own L67 reading (close-2026-09-23 (c)) calls the first check of a new feature's build a "new build", which seats Fable · Astra · Grok. Today both readings produce the same seats: Opus 5.5 (R109 pins Fable as Opus 5.5) + Grok, with Astra and Sol both on the Codex METER. They differ only from Sat 06:47, when it becomes Sol vs Astra, and only Sol's string is on `15`'s line. ASK DESK: which OpenAI seat after Sat? [16:19]
3. **XL76 (H1) is a real design fork the old prompts never faced.** Under L76, the existing with-DB callers of the membership store break unless they see `0014` inside their own transaction. `43` settles this with an experiment and a decision table. Outcome (B) stops the build with a design question for the houses, not for him. The deploy's stacked gate inherits the same `migrated_radar` fixture.
4. **The desk rows R62/R63/R66 of 09-23 give conflicting migration numbers** (`0015` to D1, `0016` to stale-score). The branches as built settle it: D1 = `0016`, voice = `0017`. `42` says `0015` and answers `46`'s ASK.
5. **Registry-pin re-points.** `test_assumed_store.py:244-245` pins `0013` as `FORWARD[-1]`/`REVERSE[0]`, and `test_archiver_migrations.py:80-105` pins the last five. Each branch adding a migration re-points them (A1 in `42` (A) and `43`). Those are the L68 seam at the stacked gate, the same class `14` classed OUT OF SCOPE (row 13) for D1.
6. **`46` (smoke look) cutoff:** the prompt keeps `2026-09-19T15:11:42-04:00` (from `deploy-2026-09-19b`), which the 09-22 and 09-23 looks also used. It is re-derived by command at run time.
7. **Reports for the desk to clean up** (not mine, untouched): `46`'s 09-23 report stays in the stale-score tree as history. The re-issue writes a new `…-2026-09-24.md` beside it, and a relaunch never edits the old one.

DEVDB BUILDS REISSUED · 42: ready (rebase first) · 43: ready (re-cut first) · 44: ready · 45: ready · 46: ready (window 21:40) · new rule strings: 2 · ESCALATE: 7
