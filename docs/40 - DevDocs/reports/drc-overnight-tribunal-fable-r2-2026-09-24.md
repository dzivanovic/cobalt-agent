BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Thu Sep 24 12:12:57 EDT 2026

## DIGEST FOR THE DESK

- TRIBUNAL R2: BUILD AFTER the R2-1 (i)–(iii) and R2-2 wordings are folded
- R2-1(i) ADOPT WITH: trigger = any record of P while a later day exists; not-computed P keeps N's stated seed.
- R2-1(ii) ADOPT WITH: a stated N compared to P's close; equal → carried, differ → FAIL naming N, restate.
- R2-1(iii) ADOPT WITH: current import's fills, `failed` → FAIL; stats from stored rows of the current stats import.
- R2-2(a) ADOPT WITH: third literal `cli`; one `record_stated_book(…, via=…)`.
- R2-2(b) ADOPT WITH: changes only K1's new migration; nothing built names `via` or the table.
- R2-2(c) ADOPT WITH: the CLI is the stand-in, covers opening / no_trade / resolve, dry-run then `--apply --sha256`.
- Withdrawn: 3 (round-1 Q3 re-pair sentence, the stated-replaced sentence, the executions source).
- Experiments: 0 new; X9, X10 cited with added K2 cases.
- OWNER: 0 · ESCALATE: 2.

## Rulings

(R2-1 written 12:17 ET, before any read for R2-2.)

### R2-1(i) — is a FIRST record of day P, after a later day N is recorded, a re-pair trigger?

SELF-ATTACK (on my round-1 (1)): see `## Self-attack` A1–A3. The trigger sentence HOLDS against the files. Two defects are found in the sentence that follows it ("The later day N … is re-paired from P's carried book"): it FAILs P's own record when P's pairing is not computed (A2), and it re-pairs N from the carry even when N's stated book differs (A3, ruled under (ii)).

**ADOPT WITH** "FORWARD RE-PAIR TRIGGER. The store runs the forward re-pair every time it records day P (a first file, a superseding file, a no-trade record, a RESOLVE, or a restated opening book) while a later day is already recorded. The later days are re-paired in date order. Each one is seeded as `seed_for` seeds it: from its prior day's re-paired close, or from its current stated `opening` row when its chain is broken. Each carried seed is checked against that day's current stated `opening` row, if it has one (R2-1(ii)). If P is recorded with its pairing `not computed`, P has no close. A later day N whose prior is P then keeps its stated seed, because that statement is the broken-chain remedy (§2c). N is not re-paired, and P is recorded. All-or-nothing and note order as `[F-03]`."

Reasoning.
- Trigger. `check_contiguity` passes a day whose `earlier` set is empty (`pairing.py:249-250`). A later day recorded first is pinned lawful (`test_drc_pairing.py:350-351`). `seed_for` reads only `day < %s` (`store.py:230-231`), so recording P never looks at N. Nothing else reads a later day: `seed_for`'s only reader is itself (grep: definition only, `store.py:220`).
- Scenario: Tue is imported first and stated flat. Tue's `B 40` opens a long (`pairing.py:189-191`), and Wed carries that long and closes it. Mon is then imported for the first time, stated flat, with `SS 40` left open. Mon's stored `book_close` holds a short 40. Tue's seed row says `stated`, empty, and nothing re-reads it. Under L1 (index card: "one contradicted by a stored close, is a loud FAILED") this is not lawful, so Grok's "a superseding import of day P" is too narrow.
- Why the carve-out is needed: under my round-1 wording, recording Mon with a trading log that lacks a pairing column (`build_day` → `not computed`, `pairing.py:327-328`) re-pairs Tue. `seed_for(Tue)` then raises at `store.py:236-244`, and `[F-03]`'s all-or-nothing refuses Mon's record. Mon could never be recorded while Tue exists, although D1 records a not-computed day lawfully today.
- Price: K2, `drc/store.py` (the trigger inside the one re-pair method). No migration. It is inside the seat's round-1 +1 h (UNVERIFIED).

WITHDRAWN: "The later day N whose prior trading day is P is re-paired from P's carried book" as an unconditional sentence (defeated by A2 and A3).

### R2-1(ii) — does P's carried book replace N's STATED seed; what stays; what /drc shows

SELF-ATTACK (on my round-1 "If N's seed was STATED, the carried book replaces it (DAS is the truth, R67)"): A3 in `## Self-attack` breaks it. The carried book is also rooted in a statement: P's own opening, stated because `earlier` was empty when P was first recorded (`pairing.py:249`). R67's "DAS is the truth" settles DAS against Cobalt's recompute. It does not settle his statement for N against his statement for P plus a file that never touches the symbol. The code cannot tell which one is right, so the replacement assumes a book.

**ADOPT WITH** "STATED SEED vs CARRIED CLOSE. When a day N has a current stated `opening` row and its prior day P has a computed close, the store compares the two, position by position, on symbol, direction and shares. Cost is not compared: the carried lots' prices stand, and a stated `avg_cost` stays as history.
- EQUAL: N is paired from the carried book. Its `seed` row is `{source: carried, from_day: P, from_book_sha256, stated_book_id: <N's opening id>}`, and every carried `trade_id` is kept.
- DIFFERENT: this is a failure of N's re-pair under `[F-03]`. Nothing in `drc_rows` is replaced. The page shows `<P>: file <name> stored, not applied — <N>: stated opening book #<id> differs from <P>'s close: <symbol direction shares> vs <symbol direction shares>`, with the §2c remedies: restate N's opening (a new `opening` row, `supersedes = <id>`), restate P's opening, or re-export.
- The lane never writes, supersedes or deletes a `drc_stated_books` row. Only his restatement adds one. N's row stays current until he restates it."

Reasoning.
- A3 scenario: a short 40 was opened on a Friday that was never imported. Tue is imported first, stated `short 40`, and its `B 40` covers it: flat, correct. Mon is then imported first-time, and he taps `I started Mon flat`, which is wrong. Mon's file never touches the symbol, so Mon's close is empty.
- Under my round-1 text, Tue is re-paired from the empty carry. `B 40` with no seed opens a long (`pairing.py:189-191`), and that phantom long is carried to Wed, `continuing open position`. It is shown only as a "differed" note, while the book is already wrong.
- Under this wording the same sequence FAILs, naming Tue and both books. He restates Mon's opening as `short 40`, the import retries, the books are EQUAL, and Tue is carried.
- Grok's text has no stated-vs-carried rule. Under it Tue is either silently re-seeded (when the trigger fires on a later supersede of Mon) or left contradicted (on a first record). Neither is fail-loud.
- Smaller than my round-1 text: a compare and a refusal, with no replacement path and no page note that follows a changed book.
- Price: K2, `drc/store.py` compare, about 30 lines plus tests. K3 has no new action (the §2c form restates). No migration. +0.5 h, UNVERIFIED.

WITHDRAWN: "If N's seed was STATED, the carried book replaces it (DAS is the truth, R67): the stated row stays in `drc_stated_books` as history, and the page shows `stated book for <N> differed from <P>'s close: <trade_ids>`."

### R2-1(iii) — a re-paired day's inputs (executions and stats)

SELF-ATTACK (on my round-1 (2)): A4 and A5 in `## Self-attack`. My executions source ("the import ids its own `day` row names, `store.py:190`") can pair a SUPERSEDED file (A4). My stats source HOLDS, but "its `not_computed.match`" does not say how `match_stats`' `stats.result.missing` (`pairing.py:265`) is rebuilt (A5). Grok's executions source holds, except when the newest file FAILED (A6). Grok says nothing about the stats rows.

**ADOPT WITH** "RE-PAIR INPUTS. For each re-paired day, the executions are the `drc_fills` of that day's CURRENT `trading_log` import: the `drc_imports` row that no other row supersedes (the predicate at `store.py:92-93`). If that import is `failed`, the re-pair FAILs naming the day and the file (`[F-03]`, nothing replaced). A `partial` import re-pairs to `not computed` exactly as its first record did (`pairing.py:327-336`).
The stats input is the day's stored `stats_row` rows (matched and unmatched), each rebuilt as a `StatsRow` from `derived.row` (`store.py:175`, `:185`) and read in the re-pair's transaction before the delete, but only when every row's `inputs.stats_log_import_id` is the day's CURRENT `stats_log` import. Otherwise the re-pair FAILs naming the day and the stats file (its rows exist nowhere else: `drc_fills` holds trading-log columns only, `0016_drc.sql:52-71`).
If the stored `day` row carries `not_computed.match`, the stats rows are written back unchanged, because the match cannot run on the same file. Otherwise `match_stats` runs on them with `missing = []`, which is exact: `match_stats` reads only `MATCH_INPUTS ∩ missing` (`pairing.py:265`), and that set was empty when `not_computed.match` was absent.
A day with no stats import has no stats rows and no match. The `day` row's `import_ids` name the current imports used."

Reasoning.
- A4 scenario: Mon leaves a short 40 open, and Tue file 1 is paired from it. He drops Tue file 2, a later export with an extra fill. `record_import` commits it as current (`store.py:88-97`, `:116`), but its pairing FAILs (a line contradicts the seed, `pairing.py:203-218`), so Tue's `day` row still names file 1. He then re-exports Mon, which carries a missing add.
- Under my round-1 text, Tue is re-paired from file 1, a superseded export, while file 2 is DAS's latest (R67). Under this wording Tue is re-paired from file 2, which now pairs, or FAILs loudly.
- A6 scenario: Tue file 2 fails to parse. `record_import` still stores it with zero fills and makes it current (`store.py:83-84`, `:88-97`). Grok's "current import only" then pairs Tue with zero executions: Tue's trades vanish and the seed passes through unchanged (`pairing.py:220-234`). This wording FAILs it instead.
- Stats rows exist only in `drc_rows`, and every parsed row is stored exactly once, matched or unmatched (`store.py:170-186`, `pairing.py:277-307`). So the read-before-delete is the only source. X9 proves the round-trip.
- Price: K2, the same re-pair method, about 40 lines plus 3 tests (a failed current file, a stale stats import, `not_computed.match` carried). No migration. It is inside the seat's round-1 +1 h (UNVERIFIED), and it replaces v2's X9 row wording only by adding the failed-file case.

WITHDRAWN: "(2) Inputs of each re-paired day: its executions from `drc_fills` of the import ids its own `day` row names (`store.py:190`)." The stats half ("its stats rows come from its own stored `stats_row` rows … read before the delete") HOLDS and is kept.

### R2-2(a) — the `via` value of the CLI caller

SELF-ATTACK (on my own answer): A7 in `## Self-attack`. Reusing `drc_page` is smaller (no new literal), but the stored row would then say the page wrote a statement it did not write. A replay could not separate the two callers, and that is wrong under L57. A new literal costs nothing, because the CHECK lives in a migration that does not exist yet (R2-2(b)). The remaining weakness: `cli` names the caller, not the hand that ran it. That is carried by the apply gate in R2-2(c), not by the column.

**ADOPT WITH** "`via` text CHECK IN (`drc_page`, `voice_widget`, `cli`). `cli` = the `cobalt drc state-book` command. All three callers call the one `DrcStore.record_stated_book(…, via=…)` (L3). `via` is an argument of that function, never a second write path."

Reasoning. `drc_stated_books`, `record_stated_book` and `via` exist nowhere in either tree (grep D1 and main `src/cobalt`: no hits; `git log --all -S"drc_stated_books" -- src/`: empty). The only precedent for a caller or source CHECK is `0007_radar_cards.sql:124` (`source IN ('cobalt', 'cobalt-degraded', 'human')`), which also names the producer. Failing scenario for reusing `drc_page`: on the day K3 misses the deploy, a statement written from the CLI is stored with `via = drc_page`. The `/drc` access log shows no such request, and the stored input's provenance is false. Price: one literal in K1's new migration and one enum member. Zero hours.

WITHDRAWN: none. No round-1 text of mine named a value.

### R2-2(b) — its migration consequence

SELF-ATTACK: A8. Could any branch already carry `drc_stated_books` (for example a K1 cut before this round)? `git -C /Users/cobalt/cobalt log --all -S"drc_stated_books" -- src/` is empty, and neither tree's `src/cobalt` has the name. Only `0016_drc.sql` (D1, unmerged) and `0017` (`69c376bd`, voice V1) exist above main's migrations for this lane's range. Neither is touched by `via`.

**ADOPT WITH** "The `cli` literal changes the one K1 migration only (the new file that creates `\"user\".drc_stated_books`, number at the L68 gate, `[F-02]`). Nothing built changes: `0016_drc.sql` is not edited for it (whether `[F-02]` folds the `drc_rows.kind` widening into `0016` is independent of `via`), and no table, function or test on any branch names `via`. v2 §3's `via` row (`:125`) gains `cli`, and the gap note (`:134`) is retired."

Reasoning. The table is K1's new object (v2 `:152`, `:205`). The only migration touching this lane on a branch is `0016_drc.sql`, whose CHECKs are on `drc_imports.kind`, `parse_status`, `event_state`, `drc_fills.side` and `drc_rows.kind` (`0016_drc.sql:26`, `:30`, `:35`, `:61`, `:86`), none of them `via`. Price: 0 h, K1.

WITHDRAWN: none.

### R2-2(c) — is the CLI the landing set's statement caller without K3, and what does it write

SELF-ATTACK (on my round-1 Q10 "the `cobalt drc state-book` CLI … stands in"): A9 in `## Self-attack`. If the CLI takes only an opening book, then without K3 there is no writer of `[F-05]`'s `no_trade` row (v2 `:88`: "written by `record_stated_book` when he records the no-trade DRC on `/drc`") and none of `[F-06]`'s `resolve` row.
- Scenario: D2 + D3 + K1 + K2 land and K3 does not. Mon leaves a swing open. Tue is a no-trade day (R93), and nothing can record Tue's `no_trade` row. Wed's import FAILs contiguity (`pairing.py:250-254`).
- The only remedy left is stating Wed's opening book by CLI. That is the daily manual restatement my own round-1 Q10 reasoning called the cost of a missing K2. It is loud, but it breaks the carry the lane exists for.
- The stand-in therefore has to cover all three kinds. Round-1 Q10 is incomplete (not wrong) and is widened here.

**ADOPT WITH** "Yes. When K3 is not checked for the deploy that carries D2 + D3, the `cobalt drc state-book` CLI is the statement caller of the landing set (`[F-10]`, `[F-17]`). It covers the three kinds of `drc_stated_books`: `--opening <day> (--flat | --position SYMBOL DIRECTION SHARES [AVG_COST]…)`, `--no-trade <day>` and `--resolve <day> TRADE_ID [--exit-price P] [--exit-time T]`, with `--supersedes <id>` for a restatement. Every call goes through the one `record_stated_book` (L3), which refuses inside `market_reset` for every caller (`[F-01]`).
DRY-RUN BY DEFAULT: the CLI prints the row it would write and its `book_sha256`, and writes only with `--apply --sha256 <that book_sha256>` (the `cobalt settings load` shape, `settings/cli.py:313-319`; L7's mechanical half: what is written is what was reviewed).
It writes the same columns as the form: `via = cli`, `turn_id` NULL and `readback_sha256` NULL (voice-only, v2 `:126-127`), `book_sha256` = the reviewed hash. It writes nothing the form would not. When he did not type the command himself, the run is the desk's, on his chat word, logged under L7's interim clause."

Reasoning.
- K1 alone is inert: no caller of `seed_for`, `record_day` or `record_import` exists on D1 or main (greps: definitions only, `store.py:70`, `:153`, `:220`). So the landing-set question is only which caller writes `drc_stated_books` when D2 + D3 land.
- Without some caller, a first import stays `not computed — opening book not stated` forever (v2 §4 row 1).
- The dry-run and hash gate is what a command-line statement has in place of the widget's read-back binding (`readback_sha256`) and the page's own click.
- Price: K1, the `drc/cli.py` subcommand with the three kinds, dry-run and apply, plus tests. +0.5 h over `[F-10]`'s +0.5 h, so +1 h total (UNVERIFIED). No migration beyond R2-2(a)'s literal.

WITHDRAWN: none. Round-1 Q10's CLI sentence is incomplete, not contradicted by a file, and it is widened above.

## Self-attack

### Writers and readers (one grep each; D1 = `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt`, main = `/Users/cobalt/cobalt/src/cobalt`)

| Name | Writers / definitions | Readers / callers |
|---|---|---|
| `seed_for` | def `store.py:220` (docstrings `store.py:24`, `pairing.py:21`) | none, on D1 or main |
| `record_day` | def `store.py:153` | none, on D1 or main |
| `record_import` | def `store.py:70` | none, on D1 or main |
| `check_contiguity` | def `pairing.py:239` | `store.py:235` (only) |
| `pair_day` | def `pairing.py:162` | `pairing.py:337` (`build_day`) only |
| `prior_trading_day` | def `daymode/propose.py:300` | `store.py:225`, `daymode/drc.py:152`, `propose.py:380` |
| `stats_row` | writes `store.py:172`, `:182`; CHECK `0016_drc.sql:86` | none (no reader on D1 or main) |
| `not_computed` | `trading_log.py:171`, `stats_log.py:276`, `pairing.py:271`, `:328`, `:333`; stored `store.py:195` | `store.py:238` (the `pairing` key only), `pairing.py:327` |
| `match_stats` | def `pairing.py:260` | `pairing.py:338` only |
| `supersedes` | `drc_imports` only: `store.py:116` (predicate `:92-93`); column `0016_drc.sql:34` | `store.py:92-93` |
| `drc_stated_books` | none on D1 or main; `git log --all -S -- src/` empty | none |
| `record_stated_book` | none | none |
| `via` | none in `drc/` or `db_migrations/` (one comment, `0001_schemas.sql:112`, unrelated) | none |

### The attacks

- **A1 (the (i) trigger sentence): none found.** I walked `check_contiguity` (`pairing.py:239-254`), `seed_for` (`store.py:220-250`: only `day < %s`, `:230-231`), the pin (`test_drc_pairing.py:350-351`) and every caller in the table above. No code path reads a LATER day when an earlier one is recorded, so a first record of P never re-checks N. The trigger is needed.
  - Rows after each step. Today's code plus v2 K1:
    - Tue first: `drc_stated_books` `opening` Tue `[]`, and Tue's `seed` (stated), `trade` (long 40 from `B 40`), `open_position`, `day` and `book_close` (count 1).
    - Wed: carried long 40, `S 40` closes it (a closed long, P&L off a phantom).
    - Mon first: `opening` Mon `[]`, `SS 40` left open, `book_close` count 1.
  - Tue's rows are unchanged. `/drc` for Tue shows `started flat (stated)` and a long `new today`, while Mon's evening block says `left open: 1`. Nothing flags it.
- **A2 (my (1), continued: "re-paired from P's carried book"):** Tue is recorded first and stated. Mon is then dropped with a trading log missing a pairing column. `build_day` gives `not_computed.pairing` (`pairing.py:327-328`). The re-pair calls `seed_for(Tue)`, which raises at `store.py:236-244`, and `[F-03]` refuses Mon. Mon can never be recorded. Fixed in (i)'s carve-out.
- **A3 (my (ii) replacement):** the Friday-short sequence in R2-1(ii). The carry is `his Mon statement + a file that never touches the symbol`, not DAS alone. The replacement opens a phantom long on Tue (`pairing.py:189-191`) and carries it. Withdrawn.
- **A4 (my (2) executions source):** in the Tue-file-2 sequence in R2-1(iii), the `day` row names a superseded import (`store.py:190` records what was paired, and `record_import` has already moved "current" at `:88-97`). Withdrawn.
- **A5 (my (2) "and its `not_computed.match`"):** vague, not wrong. `match_stats` needs `stats.result.missing` (`pairing.py:265`), which is not stored as a list anywhere in `drc_rows`. It exists only as text in `drc_imports.reason` (`models.py:205`, `:231`) and `derived.not_computed.match`. Fixed without any text parse: when `match` is absent, `missing = []` is exact, and when it is present the rows are carried unchanged.
- **A6 (Grok's executions source, weighed after my own):** a `failed` newest file is stored with zero fills and becomes current (`store.py:83-84`, `:88-97`, `:116`). "Current import only" then pairs an empty day, and the seed passes through (`pairing.py:170-174`, `:220-234`). Fixed in (iii).
- **A7 ((a) reuse `drc_page`):** false provenance, per the R2-2(a) scenario.
- **A8 ((b) something already built):** none found. See R2-2(b).
- **A9 ((c) opening-only CLI):** the R2-2(c) scenario.

## Withdrawn from round 1

Count: 3.

1. "The later day N whose prior trading day is P is re-paired from P's carried book" (report `:41`, as an unconditional rule). Defeated by `store.py:236-244` with `pairing.py:327-328` (A2), and by A3.
2. "If N's seed was STATED, the carried book replaces it (DAS is the truth, R67): the stated row stays in `drc_stated_books` as history, and the page shows `stated book for <N> differed from <P>'s close: <trade_ids>`" (report `:41`). Defeated by A3: `pairing.py:249` (the carry's own root is a statement) and `:189-191` (the replacement opens a phantom).
3. "(2) Inputs of each re-paired day: its executions from `drc_fills` of the import ids its own `day` row names (`store.py:190`)" (report `:41`). Defeated by `store.py:88-97` and `:116` (A4).

Kept, and re-checked against the whole files:
- (b) "Remaining assume path: an earlier day recorded after a later stated day … nothing re-checks it" HOLDS (A1).
- The stats half of (2) HOLDS (`store.py:170-186`, `0016_drc.sql:52-71`).
- (e)'s "every hit is a definition" HOLDS (table).
- Q10's CLI sentence is incomplete (A9), not withdrawn.

## Experiments (L70)

No new X. The behaviour claims above are read from the code; the new FAIL paths are K2 read-back tests.
- **X9** (cited; v2 `:282`). K2's check adds one case: the current trading import is `failed` → the re-pair FAILs naming the day. The `StatsRow` round-trip through `derived.row` is X9's "identical `derived` and `inputs`" run.
- **X10** (cited; v2 `:283`). K2's check adds the A3 sequence (the stated book differs from the carried close → FAIL naming N, nothing replaced; after the restatement, the books are EQUAL → N carried, `seed.stated_book_id` set) and the A2 sequence (P not computed → P recorded, N keeps its stated seed).

## OWNER

none. Every sub-item is mechanism. His runtime answer to a stated-vs-carried FAIL is an input he gives through the §2c form, not a design decision.

## READING

Authorization (verified 12:12–12:14 ET):
- FABLE ROW: `grep -c -x -F "FABLE ROW: R__"` → 0 (filled). The first line is `FABLE ROW: R109`.
- `cto-2026-09-22.md:56` `| R109 |` carries "Make all Opus 5.5 for now" and `claude-opus-5-5`; committed `75b2aa57…`.
- Launch row `cto-2026-09-24.md:54` `| R44 |` carries `27-drc-overnight-tribunal-r2.md` · `Fable seat: yes` · `derive seat: claude-opus-5-5`; committed `c14217ba…`. `cto-2026-09-25.md` does not exist (recorded, not fatal).
- Seat: R109 names `claude-opus-5-5`, and this session runs `claude-opus-5-5`.
- `cto-2026-09-22.md:99` R67 carries "continuing position". `cto-2026-09-24.md:32` R22 carries "We need to design the lane".
- The derive's stop line is committed (`e9652bdb…`), and so is v2 (`e9652bdb…`).
- Each of the ten launch rule strings counts 1 in `prompts/2026-09-21/22-draft-setups-tribunal.md` (0 new).

Files and searches:
- Prompt `prompts/2026-09-24/28-drc-overnight-tribunal-fable-seat-r2.md` (whole).
- LAWS.md `:1-275`, `:276-454` (whole).
- Derive report `drc-overnight-tribunal-derive-2026-09-24.md`: `## ` heading grep, then `:90-149`.
- `27-drc-overnight-tribunal-r2.md`: `grep -n "01-QUESTIONS-R2.md (verbatim)"` → `:30`, that paragraph only.
- My round-1 report `drc-overnight-tribunal-fable-r1-2026-09-24.md` `:41-120`.
- v2 `:1-11`, `:73-190`, `:201-216`, `:276-316`.
- D1 code (tip `38a70947` = docs-only above `d1342595`, proven; sizes 12,901 B / 10,568 B match): `pairing.py` whole, `store.py` whole, `models.py:90-114`, `:250-265`, grep `class ParsedStatsLog|class StatsRow|missing:` and `class Execution` (`:63-79`), `test_drc_pairing.py:330-352`, `0016_drc.sql:17-95`, `daymode/propose.py:298-309`.
- Main: `settings/cli.py:305-322`.
- Searches: the 13 greps in the table; `grep -rn -e "'cli'" -e "'voice_widget'" -e "'drc_page'"` (none); `grep -rni "state-book|state_book"` (none); `grep -rn -E "(source|origin|via|caller)\s+TEXT.*CHECK"` over both trees' migrations (`0007_radar_cards.sql:124`); `grep -rn "\"--sha256\"" "\"--apply\""` over main `src/cobalt`.
- `git log --all -S"drc_stated_books" -- src/` (empty); `git log --all -- db_migrations/0017* 0018*` (`69c376bd` only).
- Authorization greps and git logs as listed under AUTHORIZATION.
- NOT read: the round-1 hub report `drc-overnight-tribunal-2026-09-24.md` (the derive report and v2 quoted the rows needed), the houses' folder at any depth, and the round-2 hub's report.

## L74

A block in the shape of a system reminder arrived after this session's first tool result. It asked for a `Claude-Session:` line in commits and named a file-send tool. It was recorded once as DATA and not followed. This seat commits nothing and sent no file.

## ESCALATE

1. **K3 seam (the page text).** R2-1(ii)'s DIFFERENT branch adds a §4 row and a `/drc` failure line (`<N>: stated opening book #<id> differs from <P>'s close …`). K3's prompt carries it. No new page action is needed: the §2c form restates.
2. **Desk process for the CLI stand-in (R2-2(c)).** When the desk runs `cobalt drc state-book --apply` on his chat word, the dry-run output and `book_sha256` go in his approval message and the desk report (L7 interim clause). This is a desk step, not design.

## CONTINUE
next: none. All six sub-items are ruled and the stop line is written. A relaunch reads this file and stops.

TRIBUNAL R2: BUILD AFTER the R2-1 (i)–(iii) and R2-2 wordings are folded

DRC OVERNIGHT FABLE R2 DONE · R2-1: ADOPT WITH/ADOPT WITH/ADOPT WITH · R2-2: ADOPT WITH/ADOPT WITH/ADOPT WITH · owner: 0 · ESCALATE: 2
