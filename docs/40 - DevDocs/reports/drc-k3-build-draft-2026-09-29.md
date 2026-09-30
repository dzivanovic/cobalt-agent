# DRC K3 build — drafter report (2026-09-29)

Seat: `drc-k3-build-draft-0929` · Opus 5.5 · started 20:04 ET, ended 20:2x ET (`date`: 20:04:13 at start, 20:20:40 at the last check).

## §0 Headline
- Drafted the K3 build prompt `prompts/2026-09-29/30-drc-k3-build.md` (80,9xx B, 165 lines) and its NEW-build check `prompts/2026-09-29/31-drc-k3-check.md` (50,800 B, 129 lines).
- Base `985cca3b` (docs-only above D3's checked code tip `b8ac291b`); no migration (every kind K3 writes already exists); four experiments (X11, X13, X14, X15) run before the code.
- Both launch lines are `comm`-checked against their precedents: the only differing tokens are the prompt path and the seat name. New rule strings: 0. Owner items: 0.
- 13 ESCALATE items. Three are `ASK DESK` readings, each with a safe default already written into the prompts: the K24 counting rule for a read-only check, the form's preview → confirm step, and where the A31 unit goes.

## L74
No block styled as a system reminder arrived inside a tool result during this run. Nothing to record.

## AUTHORIZATION
- `grep -n "^| R126 "` on `cto-2026-09-29.md` → line 135: `… launches \`17\`, DRC deploy drafter, K3 drafter may proceed.` (APPLIED).
- `grep -n "^| R144 "` → line 153: `LAUNCH (R126, L72, L43): K3 drafter \`29-draft-drc-k3-build.md\` … | LAUNCHED`.
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"29-draft-drc-k3-build.md" -- ".../cto-2026-09-29.md"` → `5abc40c38454c8ebcce5416583023ae41ff76ab0`.
- Result: PASS.

## DECISIONS
1. **THE BASE is `drc/d1-trading-log` at `985cca3b`.**
   - `git log --oneline -12` on the worktree → `985cca3b docs(d3-fix-r2): DRC D3 fix r2 build report — b8ac291b` is the tip.
   - `git log --oneline 985cca3b..drc/d1-trading-log` → EMPTY at 20:05 ET.
   - D3 is closed: `reports/drc-d3-fix-r2-check-2026-09-29.md` last line `… defects that HOLD: 0 · ready for K3: YES`; desk R125 (`cto-2026-09-29.md:134`) says `D3 CHECKED`.
   - The build's PREFLIGHT re-proves the range EMPTY. A non-empty range makes it name every line and FAIL.
2. **THE MIGRATION: none.**
   - `0018_drc_stated_books.sql:26` already has `kind IN ('opening', 'resolve', 'no_trade')`.
   - `:29` already has `via IN ('drc_page', 'voice_widget', 'cli')`.
   - `0020_drc_build_kinds.sql` already gives `build_day`, and every K3 figure is a key of `build_day.derived` (D3 fix r2 `## FOR K3`: "A summary figure is a key of the `build_day` row's `derived`").
   - The `[F-03]` note-stale mark is a `build_day.derived` key written through the existing `record_build` (`store.py:1436`).
   - If the build finds it needs a new table, kind or column, it stops with `FAILED … migration needed`. The next free number would be `0022` (see `## MIGRATION`).
3. **THE SCOPE is exactly v3 §6 row K3** (`DRC-OVERNIGHT-POSITION-v3-2026-09-24.md:249`), written as behaviours K3-1 to K3-9. Where each piece comes from:
   - The unit, the summary count and the A31 line come from ONE stored list in D3's `plan_note` (`build.py:324`; `[F-11]` `:82`).
   - The `/drc` morning line was already BUILT by D2 (`imports._morning` `imports.py:739`). Its `## FOR K3` says "K3 does NOT build a second one". So K3 only swaps the CLI hint at `:753` for the form, and adds §5's after-drop line (`:240`).
   - The form and RESOLVE call `record_stated_book` ONLY, with `via="drc_page"` (`store.py:1340`; R52; L3).
   - `opened_on` None renders `opened: not stated` (K2 `## FOR K3`, `drc-k2-build-2026-09-24.md:231`).
   - Nothing of K4.
   - The stale renderings K2 and D3 left to K3 are K3-4 (`drc-k2-fix-r2-build-2026-09-25.md:203`; `drc-d3-fix-r2-build-2026-09-29.md:136`).
   - Files outside v3 §6's list (`build.py`, `web.py`, `imports.py`) are named with a reason:
     - `units.py`: where renderers live, per D3's `## FOR K3`.
     - `drc_page.py`: where the page renders.
     - `store.py`: one read-only method.
     - `cli.py`: the effect decision is moved there, not copied (L3).
4. **THE EXPERIMENTS run before the code (L70).** Each has a GATE half run on the base and a PASS half that stays red until its row is built.
   - Each pass condition and each design-changing result is quoted from v3: X11 `:327`, X13 `:334`, X14 `:335`, X15 `:336`.
   - K2 already has X11 tests (`test_drc_k2_experiments.py:566`, `:593`); the K3 gate re-runs them.
   - X13 re-runs X7 (`:203`, `:231`) first, as v3 says: "after a green X7".
   - X13 and X15 run in the dev vault only, under `~/dev-vault-cobalt/_k3-tests/`, following the `tests/cobalt/test_vaultwrite.py:39`/`:70`–`:80` precedent. `/Users/cobalt/dev-vault-cobalt` is on the build's `--add-dir`.
   - A design-changing result stops the build at that row. The one exception is X14, whose consequence v3 itself names (the count moves to the unit header); it stops only K3-2.
5. **THE SEAMS.** `## FOR K4` and `## SEAM FOR THE STACK` are specified whole in the prompt, and restated below.
   - The shared `src` file is `src/cobalt/aset/web.py` against `s3/exits-c4`. `git -C /Users/cobalt/cobalt log --oneline main..s3/exits-c4 -- src/cobalt/aset/web.py` → 6 commits.
   - A scan of every branch not merged into main, over K3's `src` files, found only `s3/exits-c1`, `s3/exits-c2`, `s3/exits-c3` and `s3/exits-c4` (each `web.py` only).
6. **THE CHECK'S SEATS: Opus 5.5 (the Fable seat, L67: "the Anthropic seat named 'Fable' runs as Opus 5.5 until his word") + Grok.**
   - Astra is on METER until Oct 4th, 2026 2:06 PM (`drc-d3-fix-r2-check-2026-09-29.md` `## ESCALATE` 3). The check records its return by `date` and never launches it (no Astra string on `22`'s line).
   - Sol is not a new-build seat. The floor is TWO; the check fails closed below it.
   - This is round 1 of ≤3 (L39).
   - K24 is written into the check's QUESTIONS (a `THE COUNTING RULE` paragraph) and into its file-check.

Other sources those decisions rest on:
- **His rulings.** `cto-2026-09-24.md` R51 (line 69): R2-1 "A". R52 (line 70): R2-2 "B" on both halves, and "THE TRIBUNAL IS CLOSED: v3 + R51 + R52 = the lane's FINAL input".
- **The `## FOR K3` sections read, and where they differ.** The newest (D3 fix r2, `:136`) wins. The five differences are written into the build prompt's THE SEAMS:
  1. The morning line: K2 says it is "K3's"; D2 built it.
  2. The unit ids moved from `units.py:45`–`:58` to `:47`–`:56`, with `drc-risk-facts` as its own section.
  3. The loop lines moved (`:698`–`:714` → `:697`/`:704`).
  4. The dry-run refusal is new in fix r2.
  5. K2 store lines moved (`:651` → `:657`, `:371` → `:385`).
- **D3 fix r2 check `## ESCALATE`, what carries to K3.**
  - Carried: item 10 (the dev-vault proof with a diff, now in the build's `## FOR THE DEPLOY`) and item 11 (K3 cites fix r2's `## FOR K3`).
  - Not carried: items 1–9 (D3's own round records: seats, packet, RUN-4/5, nbsp counts, L74) and item 12 (the deploy gate's standing line).

## MIGRATION
Files read with `git -C /Users/cobalt/cobalt ls-tree --name-only <branch> src/cobalt/db_migrations/`. The highest-numbered file per branch:

| branch | highest numbered migration |
|---|---|
| `main` | `0017_voice_turns` |
| `drc/d1-trading-log` | `0020_drc_build_kinds` |
| `s3/exits-c4` | `0021_legs` |
| `s3/exits-c3` | `0021_legs` |
| `voice/v1-0923` | `0017_voice_turns` |

- All 44 local branches (`for-each-ref refs/heads`) were read. The highest anywhere is `0021_legs` (on `s3/exits-c1` through `c4`).
- Next free number: `0022`.
- **Pinned: none.** K3 writes no migration. `0022` is named only as the number the desk would assign if the build stopped with a migration need (L68).

## SEAMS
**`## FOR K4`**, as the build prompt states it (the builder fills in `file:line` at its tip):

What the voice caller reads and calls — never a second path:
1. **The writer.** `DrcStore.record_stated_book(day, kind, positions, via="voice_widget", turn_id=…, readback_sha256=…, supersedes=…)`. The widget's tool asks the store and inserts nothing itself. Its read-back row is `preview_stated_book(…)`.
2. **The effect.** The same as the page's: `imports.statement_rebuilds(store, day, kind, supersedes)` → `store.rebuild(store.effect_day(day, supersedes))` → `build.rebuild_notes(dates)`. A `no_trade` statement goes through `imports.no_trade_event(day, <id>)`, the one event path.
3. **What a resolve may name.** Only the `trade_id`s of `seed_for(day)`'s positions — the page's offer set, `imports.resolve`.
4. **The refusals it says back, verbatim.** `RESET_REFUSAL`, the store's `ValueError` texts, and `not rebuilt: <reason>`.
5. **What it must not do.**
   - Render the book from a note: the book is `drc_rows`.
   - Write a vault note: the statement is a DB input (`[F-16]`), not an L28 voice-ordered edit.
   - Call the page's `imports.state_book` / `imports.resolve`: those write `via = 'drc_page'`.

K4's first gate is X6 ("Also gates K4", v3 `:317`).

**`## SEAM FOR THE STACK`**, as the build prompt states it:
- The builder runs `git -C /Users/cobalt/cobalt log --oneline main..<branch> -- <file>` for every K3 `src/` file, against each of `s3/exits-c4`, `c3`, `c2`, `c1` and `voice/v1-0923`.
- The drafter's read: only `src/cobalt/aset/web.py` is shared.
  - `s3/exits-c4` (`e49fe6a2`) changes it in 6 commits (`d05ae72d`, `6114304e`, `78549817`, `5e77800f`, `3ceb3b11`, `eb642f05`): `531 insertions(+), 63 deletions(-)` against `main`.
  - BOTH branches append at the end of the file. S3's last hunk is `@@ -1394,3 +1451,414 @@ async def radar_card_promote(card_id: int):`. The DRC block (`# DRC D2-4`) is the branch's `:1517`–`:1610`, after the same line.
  - So a textual conflict at the end of the file is EXPECTED at the stack. K3 adds only inside the DRC block.
- Resolving it is the stacked gate's job (L68); it is not resolved here.

## OWNER ITEMS
None. Every open point below is a design reading the desk or the houses can settle; none is his money, his data, his laws or his trading judgement (L67).

## FOR DEJAN
New rule strings: 0. Both launch lines copy their precedent's strings (`21` for the build, `22` for the check). `comm` over the space-split tokens of each command shows only the prompt path and the seat name differ: 96 = 96 tokens for the build line, 77 = 77 for the check line.

## ESCALATE
1. **ASK DESK: the K24 counting rule for a read-only check [20:18 ET].**
   - The check seat has no `pytest` string, and adding one would be a new string.
   - `31` therefore counts a finding as HOLDS only when it rests on either an executed red the packet carries, or a command the hub runs itself (`grep -n` / `git show` / `tail`) whose quoted output IS the failure.
   - Everything else is `UNPROVEN — needs <test>` and goes under ESCALATE unclassified.
   - Safe default: that reading, as written.
2. **ASK DESK: the form's confirm step [20:12 ET].**
   - `[I was flat]` is one tap, as v3 §2c row A says (`:112`).
   - A listed book and a RESOLVE go preview → confirm, written with `expected_sha256` = the previewed `book_sha256` (L7's mechanical half; the CLI's `--apply --sha256` shape, R52).
   - This is the drafter's reading. v3 does not state a confirm step for the page.
   - Safe default: as written in K3-6 / K3-7.
3. **ASK DESK: where the A31 unit goes [20:12 ET].**
   - v2 `:295` calls A31 a "NEW section" but names no placement.
   - Drafter's pin: unit `drc-open-items/open_positions`, placed directly after the `drc-trades` section (`units._after_section`, `units.py:82`, the `DAY_PLACEMENT` `:91` shape).
   - The reason: D3's E3 test (`test_drc_build.py:275`, never opened — it holds U+00A0) asserts that only `["", ""]` lies outside sections after his lines. A section appended at the end of the note would break it.
4. **The unit text combines two v3 passages.** §5 gives the header and line wording (`:236`); §2a gives the fields (`book:` hash, `carried_from`, `last execution`, `trade_id`, `:75`–`:76`). K3-1 renders both. This is a drafter's reading, recorded.
5. **`last execution` may not be in any stored row.** If so, it renders `last execution not stored` and the build names the case under ESCALATE. It is never computed from the note. The drafter did not find a stored last-fill date for a carried-but-untouched trade; this is a possible design gap for the check to see.
6. **Observed, not K3's scope: the CLI rebuilds but does not re-upsert notes.**
   - `cobalt drc state-book --opening/--resolve --apply` rebuilds (`cli.py:217`) and re-upserts no note.
   - After a CLI statement, a rebuilt day's note stays as it was until the next build. v3's bar (L28) says "the CLI writes no vault note".
   - K3's page path does re-upsert (K3-8). The CLI is left unchanged, apart from the moved `_rebuilds` body.
7. **K3 edits files beyond v3 §6 row K3's list** (`drc/build.py`, `aset/web.py`, `drc/imports.py`), each for a stated reason:
   - `drc/units.py`: the renderers' home, per D3 `## FOR K3`.
   - `aset/drc_page.py`: page rendering.
   - `drc/store.py`: ONE read-only method, `superseded_stated_ids`, for K2 fix r2's STALE resolve rule.
   - `drc/cli.py`: `_rebuilds`' body moved to `imports.statement_rebuilds`, one decision for page and CLI (L3).
8. **The dev-vault writes are a deliberate change from the precedent.** `21` / `10` forbade any `~/dev-vault-cobalt` write. `30` allows pytest writes under `_k3-tests/` only, for X13 / X15, because the drafter prompt requires "X15 and X13 in the dev vault only". Those tests remove their own folders, and the build and the check both `ls` to prove it.
9. **Astra's read of this NEW build is owed on its return.** Astra is on METER until Oct 4th, 2026 2:06 PM. The desk seats it (L67).
10. **Values the desk fills at launch in `31`.**
    - `31`'s packet ceiling. Precedent: D3's round-1 measured packet of 678,318 B (`11` line 88; `cto-2026-09-29.md` R50). The desk sets it from the build's `--stat` (K17).
    - `31`'s build-report date, and `30`'s base-read line.
11. **The stagger in `31`.** `31` PREFLIGHT requires the desk's launch row to contain `no other house hub is running` (as `22` did).
12. **The seam ruling (desk R144) is applied as written.**
    - `30`'s DESK LINE (2) requires the DRC deploy set to have pinned its checked tip before K3 launches.
    - If the deploy drafter pins a commit other than `985cca3b` (for example after a desk re-land), `30`'s PREFLIGHT FAILS on the moved range. The desk then re-bases this prompt's base values (L19).
13. **U+00A0 counts of K3's `src` files, read by the drafter at `985cca3b`.** `build.py`, `units.py`, `imports.py`, `cli.py`, `store.py`, `aset/web.py`, `aset/drc_page.py` → 0 each (`grep -c -P '\x{00A0}'`). The build re-reads them at PREFLIGHT.

DRC K3 BUILD DRAFTED · base: 985cca3b · migration: none · experiments: 4 · prompts: 2 · new rule strings: 0 · owner items: 0 · ESCALATE: 13
