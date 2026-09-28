# DRC CHAIN RE-ISSUE — F14 `36` → `37` → `09` → `10` as `2026-09-28/08` → `09` → `10` → `11`

Drafter `drc-reissue-draft-0928` (Sonnet 5), prompt `prompts/2026-09-28/06-draft-drc-reissue.md`. First `date` Mon Sep 28 08:46:06 EDT 2026; last `date` 09:12:08 EDT, read before this report was written.

## §0 Headline
- Four files re-issued whole under `prompts/2026-09-28/`: `08-drc-d2-fix-r1-build.md` (81,773 B), `09-drc-d2-fix-r1-check.md` (56,714 B), `10-drc-d3-build.md` (66,561 B), `11-drc-d3-check.md` (47,589 B); the 09-25 files are untouched.
- Branch tip `10163d51` stands (code tip `6777c463`); merge-base `04b05cd4`; the branch is 590 commits behind `main` and 65 ahead.
- Laws: 45 cited numbers re-checked, 0 meaning changed, 5 wording moved (L28, L35, L62, L63, L67 — each carried on current wording).
- New rule strings 0; each launch line differs from its source by the path and ` --name <job>`.
- ESCALATE 8: the rebase / re-cut call, the desk's `## FOR 09` re-points, three carried identifiers and facts.

## FACTS
| fact | command | result |
|---|---|---|
| authorization | `git -C /Users/cobalt/cobalt log --oneline -3 -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` · `grep -n -F "\| R27 \|"` on that file | `e77b08a1` · `e6b26fd3` · `22044363`; `:35` R27 names `06-draft-drc-reissue.md`, APPROVED; `:34` R26 |
| branch tip | `git -C /Users/cobalt/cobalt log --oneline -3 drc/d1-trading-log` | `10163d51` docs D2 report · `6777c463` D2-4 · `d5b72392` D2 |
| tip stands | `git -C /Users/cobalt/cobalt log --oneline 10163d51..drc/d1-trading-log -- tests src configs` · `… 6777c463..drc/d1-trading-log -- tests src configs` | empty · empty |
| branch dates | `git -C /Users/cobalt/cobalt log -1 --format=%h%x20%ad drc/d1-trading-log --date=iso` · `… --skip=64 --first-parent main..drc/d1-trading-log …` | tip `10163d51` 2026-09-25 09:56 ET; first commit `3e13b5de` 2026-09-23 13:52 ET |
| merge-base | `git -C /Users/cobalt/cobalt log --oneline -2 078734aa` · `… -2 3e13b5de` | both have parent `04b05cd4` (oldest main-only, oldest branch-only) |
| main-only commits | `git -C /Users/cobalt/cobalt log --oneline drc/d1-trading-log..main`; `--skip=589`; `--skip=590` | 590 lines; `078734aa` alone; empty |
| branch-only commits | `git -C /Users/cobalt/cobalt log --oneline main..drc/d1-trading-log`; `--skip=64`; `--skip=65` | 65 lines; `3e13b5de` alone; empty |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -3 main` | `1ba082e9` · `e77b08a1` · `e6b26fd3` |
| stacked deploy | `git -C /Users/cobalt/cobalt log -1 --format=%h%x20%ad%x20%s deploy-2026-09-27 --date=iso` | `3349466f` 2026-09-27 18:42 ET, merge of `main` into `deploy/stacked-0925` |
| migrations, main | `git -C /Users/cobalt/cobalt show main:src/cobalt/db_migrations/` | `0001`–`0011`, `0013`, `0014`, `0015`, `0017` (+ `__init__.py`, `cli.py`, `placement.py`) |
| migrations, branch | `git -C /Users/cobalt/cobalt show 10163d51:src/cobalt/db_migrations/` | `0001`–`0011`, `0016`, `0018` (+ `__init__.py`, `cli.py`, `placement.py`); `0012` on neither |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` · `ls /Users/cobalt/cobalt-wt` | `no matches found`; `drc-d1` listed |
| D2 stop line | `tail -n 2` of `drc-d2-build-2026-09-25.md` (worktree) | `DRC D2 BUILT 6777c463 \| on 8ba81131 \| … offline 2588/0 \| with-DB 3071/0 \| live-note 142/0 \| … ESCALATE: 15` |
| D2 check stop | `tail -n 2` of `drc-d2-check-2026-09-25.md` | `DRC D2 CHECK DONE · round: 1 · … defects that HOLD: 11 · ready for D3: NO · ESCALATE: 12` |
| ladder | `grep -n -F "F14 DRC prefill" docs/00 - Project/SPRINT-LADDER-v0_1.md` | `:691`: tip `10163d51`; `0016` / `0018` (+ `0019` D2 fix, `0020` D3 owed); `36` / `37` / `09` / `10` HELD |
| seam reports | `grep -n "^## FOR"` on the D4 and K2 reports (worktree) | D4: build `:201`, fix r1 `:212`, fix r2 `:168`; K2: build `:231`, fix r1 `:186`, fix r2 `:203` |
| seam document | `grep -n "^## " DRC-D2-SEAM-2026-09-25.md` | `## FOR 09` `:272`, `## FOR THE D2 FIX ROUND` `:289`, `## FOR K3` `:302` |
| code lines at `10163d51` | `grep -n` in `/Users/cobalt/cobalt-wt/drc-d1` | `drc/cli.py` `def add_parser` `:196` (was `:190`); `src/cobalt/cli.py` `drc_cli.add_parser` `:511`; `resolve_vault_path` `:155` (was `:145`); `writer.py` `create_if_absent` `:588` (was `:559`), `upsert_unit` `:673` (was `:644`); `pyproject.toml` prefill entry `:67` (was `:64`); `load_prefill_paths` `:151`; `STRATEGIES_DIR` `:91`; `line_step` `:443`; `MIN_N_FOR_AVERAGE = 30` `:59`; `jobs.yaml` `:181`, `:310`; `s2.yaml` `:436`–`:438`, DRC rows `:383`–`:395`; `0018` sql `:61`–`:62`; `__init__.py` `:100`, `:105`; `placement.py` `:95`, `:97`; `daily_risk_values` `:114`; `load_drc_settings` `:82`; `BUILD_NOT_BUILT` `:88`; the four deselect ids `:697`, `:710`, `:263`, `:306` |
| v2 cites | `grep -n` in `DRC-AUTOMATION-v2-2026-09-22.md` | D3 row `:177` (was `:91`); E3 `:193`, E6 `:196`, E8 `:198`, E11 `:201` (were `:107`, `:110`, `:112`, `:115`); X12 `:204` (was `:118`); "two `{{` lines" `:129` (was `:43`) |
| v3 cites | `grep -n "^## \|^### "` on v3 | `:10` Astra METER; §2a `:67`; §5 `:234`; §6 `:243` — unchanged |
| prompts | `ls prompts/2026-09-25` · `ls prompts/2026-09-28` | `07`, `08`, `21`, `22`, `35`, `36`, `37`, `39` … present; `08`–`11` were free |

## LAW MAP
`LAWS.md` read top to `## Reading`, `## Reading`, then each entry below (`b0e5b903`). Lines are the 09-25 source lines (`36` = `08`, `37` = `09`, `09` = `10`, `10` = `11`); a new file's line is the same up to its AUTHORIZATION block and one later after it. Index-card one-liners: `36:39`, `37:29`–`:51`, `09:51`, `10:23`–`:48`.
| L | citing lines | verdict | note |
|---|---|---|---|
| L1 | 36:13,39 · 37:29 · 09:51 · 10:23 | holds | fail-loud; a dead request `failed` is its form (with L18) |
| L2 | 09:21,51 | holds | binds watchers; the no-LLM rule of D3-2b rests on R116 / R117 and L57 |
| L3 | 36:39 · 37:30 · 09:51 · 10:24 | holds | |
| L4 | 36:63 | holds | with L41: `.env` by name, never printed |
| L7 | 09:51 · 10:25 | holds | R101 is the ruling; L7 the shadow-run law |
| L8 | 09:51 · 10:26 | holds | n<30 `insufficient data` |
| L11 | 09:51 · 10:27 | holds | narrow: the entry renders his human-only variable as his; create-once of voice units is R99 — gloss extended with the entry's words |
| L18 | 36:13,32,39 · 37:31 | holds | |
| L19 | 36:39 · 09:51 | holds | |
| L28 | 09:51 · 10:28 | wording moved | entry: create-if-absent, marker-bounded units by stable id, human wins, every write versioned, dev vault first, live vault never a test target; "voice units created once" (R99) and "refused in `market_reset`" (the writer's guard) are not entry text — gloss rewritten to the entry, the two kept as step facts with their source |
| L29 | 36:1,39 · 09:1,7,51 | holds | Opus 5 floor; never auto mode on a write path |
| L31 | 36:39 | holds | |
| L32 | 36:39 · 37:32 · 09:51 · 10:29 | holds | |
| L35 | 36:24,34,39 · 37:33 · 09:51 · 10:30 | wording moved | label "P-e" no longer resolves; the unscoped-read sentence carries — "L35 P-e" → "L35" (`08` §S-1 test 7, F-3) |
| L36 | 36:1 | holds | |
| L37 | 37:1,34 · 10:1,31 | holds | narrow: bars self-approval and model approvals in his place; the hubs tabulate, they approve nothing |
| L39 | 37:35 · 10:32 | holds | |
| L40 | 36:13,39 · 37:36 · 09:51 · 10:33 | holds | |
| L41 | 36:39,63 · 09:51 | holds | |
| L42 | 36:39,147 · 09:51 · 10:34 | holds | |
| L43 | 36:7 · 37:1 · 09:9,159 · 10:1 | holds | |
| L44 | 37:37 · 10:35 | holds | |
| L45 | 36:39 · 09:51 | holds | |
| L46 | 36:39 · 09:51 | holds | the MAX AGE clause is a `## SEAM` fact |
| L47 | 37:38 · 10:36 | holds | |
| L48 | 36:59 · 37:67 · 09:70 · 10:66 | holds | |
| L52 | 37:39 · 10:37 | holds | used as the scope boundary |
| L54 | 09:51 | holds | see `## SEAM` |
| L57 | 36:39 · 37:40 · 09:51 · 10:38 | holds | |
| L58 | 36:1 · 09:1 · 10:1 | holds | |
| L60 | 36:39,57 · 09:51 | holds | |
| L62 | 36:1,39 · 37:1,41 · 09:1,51 · 10:1,39 | wording moved | "as amended R19 / R80" quotes → the entry's STANDING STRINGS paragraph (a seat is left out only while its meter is out; the desk seats it from the return time) and its permission-mode paragraph; read-only auto mode stated on the line |
| L63 | 36:1 · 37:41 · 09:1 · 10:39 | wording moved | the entry is "no dialogs"; the "state note" (`acceptEdits` + full allowlist = INTERIM PRACTICE) is a status note in LAWS-HISTORY.md under L63, not law text — quote re-pointed to L62's last paragraph + that note |
| L65 | 09:99 | holds | |
| L66 | 09:148 | holds | |
| L67 | 36:39 · 37:1,42,85,109,133 · 10:1,40,116 | wording moved | label "P-c" no longer resolves → "a turn that ends without a ruling spends no round"; "while Sol is METER" → "when the OpenAI meter is short"; seats = the entry's CHECKER SEATS BY KIND OF WORK |
| L68 | 36:1,39 · 37:43 · 09:1,51 · 10:41 | holds | "as amended 2026-09-24" is the GATE EARLY clause, kept as provenance |
| L69 | 36:13,39 · 37:44 | holds | |
| L70 | 36:39,121 · 37:45 · 09:51 · 10:42 | holds | |
| L71 | 36:39 · 37:46 · 09:51 · 10:43 | holds | |
| L72 | 36:39,157 · 37:47 · 09:51 · 10:44 | holds | |
| L73 | 37:48 · 10:45 | holds | |
| L74 | 36:39 · 37:49 · 09:51 · 10:46 | holds | |
| L75 | 36:1,39 · 37:50 · 09:51 · 10:47 | holds | |
| L76 | 36:1,39,61 · 37:51 · 09:51 · 10:48 | holds | |
Every card that said "read LAWS.md in full" (`36:39`, `09:51`) and both check cards' (4) header now read: top to `## Reading`, `## Reading`, the entries the prompt cites (L59).

## SEAM
Facts only; the decision is the desk's.
- **Numbering:** main holds `0013` `0014` `0015` `0017`; the branch `0016` `0018`; the union `0013`–`0018` is contiguous (`0012` on neither); next free `0019` = `08`'s `drc_events`, then `0020` = D3's (R64 (5)). No number collides. `FORWARD` / `REVERSE` in `db_migrations/__init__.py` and `placement.py` are edited on both sides, so any merge conflicts textually there.
- **`10-drc-d3-build.md` carries `0019_drc_build_kinds`** at its lines 1, 37, 44, 51, 101, 126, 129, 144, 154, 159, 162. The seam document's `## FOR 09` (`:272`) has the desk re-point those and the settled-home / seam-symbol / absence-probe lines at launch: source `:1 :27 :28 :37 :44 :87 :100 :128 :143 :158 :161` = new `:1 :27 :28 :37 :44 :88 :101 :129 :144 :159 :162`. Carried unchanged.
- **Paths the four prompts touch that changed on main since `04b05cd4`** (`git -C /Users/cobalt/cobalt log --oneline --name-only 04b05cd4..main -- <paths>`):
| path | main commits | prompt row |
|---|---|---|
| `src/cobalt/db_migrations/__init__.py`, `placement.py` | `a16c97ff` `01ee8bcd` `d8359ebf` `a2d320b8` `4e625f6a` `69c376bd` | `08` S-1 · `10` D3-M |
| `tests/cobalt/test_p4_migrations.py`, `test_radar_migration.py`, `test_tenancy.py`, `test_archiver_migrations.py`, `test_radar_score_migration.py` | `a16c97ff` `01ee8bcd` `a2d320b8` `4e625f6a` `95ca07d1` `69c376bd` | `08` F3 registry pins |
| `src/cobalt/aset/web.py` | `f00c37d2` `8bed61d3` (voice routes) | D2's `/drc` block; `08` F-2 `_d2_is_last` (after `radar_card_release`) |
| `tests/cobalt/test_radar_panel_cards.py` | `583852a8` `a2d320b8` `4e625f6a` `8bed61d3` | D2's allowlist guard `:668` / `:670` |
| `src/cobalt/cli.py` | `566d1848` | `10` D3-4 (`drc_cli.add_parser` `:511`) |
| `src/cobalt/replay/runner.py`, `line.py`; `tests/cobalt/test_replay_line.py`, `test_radar_evaluate.py` | `12fac3cd` `38e54342` `a2d320b8` `4e625f6a` `915b7b6e` | `10` D3-3 |
| `src/cobalt/smoke/checks.py`; `configs/cobalt/smoke/s2.yaml` | `83ed34a3`; `a2d320b8` `4e625f6a` `38e54342` `97ed027e` `83ed34a3` `4903138f` | `10` D3-6 |
| `configs/cobalt/jobs.yaml`; `configs/cobalt/rules.yaml` | `a7296b44` `41c9c962` `d2963110`; `0f593f0d` `ddb41fbd` `de88c302` (and `~/cobalt` holds an uncommitted `M configs/cobalt/rules.yaml`) | `10` D3-5 |
| `pyproject.toml`, `uv.lock` | `cc2e95b6` | `10` D3-4 (F39 entry `:67`) |
| `src/cobalt/taxonomy/vault_loader.py` | `d8359ebf` `4d940411` `a2d320b8` `4e625f6a` | `10` D3-2b (`STRATEGIES_DIR` `:91`) |
  Empty log on main: `src/cobalt/drc/**`, `aset/drc_page.py` (branch-only files), `prefill/`, `vault.py`, `vaultwrite/`, `settings/drc.py`, `daymode/drc.py`, `taxonomy/slug.py`, `ops/README.md`, `ops/com.cobalt.prefill-drc.plist`, `configs/cobalt/templates/drc.md.j2`, `tests/cobalt/conftest.py`, `test_migrate_proof.py`.
- **L54 / L68 on a branch behind main:** L54 — every Code prompt works in `~/cobalt-wt/<branch>` off main; a gate branch combining siblings gets `main` merged into it, then is fast-forwarded; its rollback is one `git revert -m 2`. L68 — no merge while a second unmerged branch of the deploy exists unless the stacked gate is green; siblings off one `main`: `main` merged into the gate branch first and the result proven docs-only; GATE EARLY on each build's own tree. The 590 main-only commits carry code (voice V1, H1, stale-score, setups, replay, smoke, jobs), so a `main` → branch merge is not docs-only. The prompts' counts (offline 2588, with-DB 3071, live-note 142) are counts on this base.
- **L46 MAX AGE:** first commit `3e13b5de` 2026-09-23 13:52 ET, tip `10163d51` 2026-09-25 09:56 ET; `areas/cobalt.md` `## NOW` names `36 → 37 → 09` as NEXT.
- **Branch `CLAUDE.md`:** `/Users/cobalt/cobalt-wt/drc-d1/CLAUDE.md` is the pre-redesign file (it says LAWS.md is read in full); a builder launched in `drc-d1` loads it. `main`'s `CLAUDE.md` is the stub since `b0e5b903`.
- **ASK DESK:** rebase or re-cut `drc/d1-trading-log` on `main` before `09-28/08` launches, or carry the base? [09:12 ET] Safe default taken: the prompts carry the base unchanged.

## CHANGES
Line = the 09-25 source line. Items refer to the prompt's `WHAT CHANGES` 1–6.
| file | line | what | why |
|---|---|---|---|
| `08` | 1 | RE-ISSUED + NAMING sentence; `09` → `09-28/10`, `37` → `09-28/09` | L19; a bare `09` / `37` would collide with the 09-25 numbers (cross-reference) |
| `08` | 1 | mode quote: "L63's state note" → L62's last paragraph + the LAWS-HISTORY status note | LAW MAP L63 (item 1) |
| `08` | 1 | DESK LINE: the stacked-deploy lane (`39`, `32`'s gate) → the 09-27 deploy has landed (`3349466f`); "At drafting (2026-09-25 11:1x ET)" → the 09-28 reading of base and lock | item 5 |
| `08` | 1 | SEAT: "launch row **R82** of `cto-2026-09-25.md`" → "launch row" | placeholder only in AUTHORIZATION (K18) |
| `08` | 1 | launch line: path `2026-09-28/08-…`; ` --name drc-d2-fix-r1-build-0925` after `--remote-control`; RULE STRINGS names the third differing token | item 6 |
| `08` | 5, 7 | BASE: 09-25 / 13:25 ET readings → the 09-28 reading (`10163d51`, code tip stands, 65 / 590); LADDER "tonight" → the 09-27 deploy is on main without the DRC set | items 2, 5 |
| `08` | 24, 34 | "L35 P-e: unscoped" → "L35: unscoped" | item 1 |
| `08` | 39 | card (1): LAWS.md top to `## Reading` + `## Reading` + cited entries; L67 seat wording | items 1, 4 |
| `08` | 46–52 | heading adds the re-issue; gate path → new file; NEW R26 bullet; launch bullet → `R__` + `\| R27 \|` exclusion, held R82 named | item 5 |
| `08` | 154, 176, 180, 183 | `09` / `37` names → `09-28/10`, `09-28/09`; `09-28/10` line list → `:1 :27 :28 :37 :44 :88 :101 :129 :144 :159 :162` | cross-reference |
| `09` | 1 | RE-ISSUED + NAMING; "TWO today, THREE once Sol's meter returns" and "Sol / Astra METER until Sep 26th" → probe-seated Sol, METER past; L62 "as amended R19 / R80" → current L62; `--name`; prose "Launch row: **R__**" removed; `36` / `09` names | items 1, 4, 5, 6, K18 |
| `09` | 17–21 | heading; gate paths; NEW R26 bullet; launch bullet → `R__` + `\| R27 \|` exclusion (`\| R69 \|` exclusion dropped: it names the 09-25 file) | item 5 |
| `09` | 26, 56, 57, 59, 115, 122, 123, 133 | `36` / `09` → `09-28/08`, `09-28/10` | cross-reference |
| `09` | 28, 42, 85, 109, 133 | card header; L67 wording; "L67 P-c" → "a turn without a ruling spends no round" | item 1 |
| `10` | 1 | as `08` line 1 (RE-ISSUED, NAMING, mode quote, prose `R__` removed, SEAT, `--name`, RULE STRINGS) | items 1, 5, 6 |
| `10` | 9 | LADDER "tonight" → the 09-27 deploy | item 5 |
| `10` | 15, 51, 57 | `writer.py:644` → `:673`; `create_if_absent :559` → `:588`; `resolve_vault_path :145` → `:155` | item 2 |
| `10` | 29 | `cli.py:190` at `4626a1f2` → `cli.py:196` at `10163d51` | item 2 |
| `10` | 41, 57 | `pyproject.toml:64` → `:67` | item 2 |
| `10` | 30, 54, 88, 150, 155 | D4 `## FOR D3` → `drc-d4-fix-r2-build-2026-09-25.md:168` (supersedes fix r1 `:212`, build `:201`); K2 `## FOR K3` → `drc-k2-fix-r2-build-2026-09-25.md:203` (re-cites fix r1 `:186`, build `:231`) | item 2, L72 |
| `10` | 51 | card (1) LAWS reading; L28 and L11 glosses; L67 `10-…` → `09-28/11` | item 1 |
| `10` | 52, 99, 101, 158 | v2 cites `:91` → `:177`, `:43` → `:129`, `:107 :110 :112 :115` → `:193 :196 :198 :201`, `:118` → `:204` | item 2 |
| `10` | 59–63 | heading; gate paths; NEW R26 bullet; launch bullet → `R__` + `\| R27 \|` exclusion (`\| R9 \|` dropped) | item 5 |
| `10` | 87 | `resolve_vault_path` `(145)` → `(155)` | item 2 |
| `10` | 159, 162 | `10-drc-d3-check.md` → `09-28/11`; standing line: Astra METER past | items 4, 5 |
| `11` | 1 | RE-ISSUED + NAMING; Astra "METER until" → METER past, desk seats it; L62 quote → current; `--name`; prose `R__` removed; `09` → `09-28/10` | items 1, 4, 5, 6 |
| `11` | 11–15 | heading; gate paths; NEW R26 bullet; launch bullet → `R__` + `\| R27 \|` exclusion (`\| R9 \|` dropped) | item 5 |
| `11` | 20, 21, 79–81 | `09` → `09-28/10`; v2 `:91` → `:177`; seam reports → D4 fix r2, K2 fix r2 | items 2, cross-reference |
| `11` | 28, 40, 44, 135 | L28 gloss; L67 wording; L72 K2 fix r2; standing line: Astra METER past | items 1, 4 |
Written sizes and placeholder counts: `wc -c` `08` 81,773 · `09` 56,714 · `10` 66,561 · `11` 47,589; `grep -c -F "R__"` 1 · 1 · 1 · 1, each on the `THIS launch` bullet inside AUTHORIZATION. `grep -n -F "@@"` on the four: empty.

## RULE PROOF
Each new launch line vs its source, `grep -c -F -e '<string>'` over source and new file; only the prompt path and ` --name <job>` differ. The `cd` line is untouched.
| new | source | `--model … --remote-control <job> ` (source / new) | full `--allowedTools … --add-dir` tail (source / new) | ` --name <job>` after the rc name (source / new) |
|---|---|---|---|---|
| `08` | `36` | 1 / 1 | 1 / 1 | 0 / 1 |
| `09` | `37` | 1 / 1 | 1 / 1 | 0 / 1 |
| `10` | `09` | 1 / 1 | 1 / 1 (both carry the two `git rm` strings) | 0 / 1 |
| `11` | `10` | 1 / 1 | 1 / 1 | 0 / 1 |
Path string `claude --bg "Read '<new path>' and follow it exactly." --model <model>`: 1 in each new file.

## NEW strings
NEW strings: none.

## ESCALATE
1. ASK DESK: rebase or re-cut `drc/d1-trading-log` before `09-28/08` launches, or carry the base? Facts under `## SEAM`. [09:12 ET] Safe default taken: the base is carried.
2. ASK DESK: the seam document's `## FOR 09` re-points (`0019` → `0020`, the SETTLED token, the seam symbols, the absence probe) are not made in `10-drc-d3-build.md`, and the D2 build report stays the named D2 seam in `10` (`:27`) and `11`'s `seam.md` (fix r1's report does not exist yet). New line numbers are under `## SEAM`. [09:12 ET] Safe default taken: carried; the desk re-points at launch.
3. ASK DESK: the identifiers keep their `0925` names — jobs `drc-d2-fix-r1-build-0925`, `drc-d2-fix-r1-check-0925`, `drc-d3-build-0925`, `drc-d3-check-0925`, the `…-2026-09-25.md` report paths, the scratch folders `d2-fix-r1`, `d3-0925` — because item 6 changes the path and `--name` only. Rename to `0928`? [09:12 ET] Safe default taken: carried.
4. ASK DESK: `/Users/cobalt/cobalt-wt/drc-d1/CLAUDE.md` still says LAWS.md is read in full and a builder in `drc-d1` loads it; the cards here state the L59 reading. Update it on the branch? [09:12 ET] Safe default taken: nothing edited.
5. L46 MAX AGE fact for the plate: `drc/d1-trading-log` unmerged since 2026-09-23 13:52 ET; `## NOW` names `36 → 37 → 09` as NEXT.
6. Date-keyed branches carried as written: `09`'s Sol probe (`before 2026-09-26 06:47 ET`) and `11`'s Astra row resolve on the run's own `date`; the `astra: METER …` stop-line field is kept.
7. References carried as written, not re-read: checklist K3 / H6 / K18, the R100 / R101 lessons, the 09-24 evening lesson, every `R<n>` row other than R26 / R27 (their verification greps are unchanged).
8. L74: a block arrived inside a tool result (a system reminder appended to the Read result of `areas/cobalt.md`) asking commits to carry a `Claude-Session:` line and naming a file-send tool. Recorded once; not followed. This seat commits nothing and sends no file.

## CONTINUE
The desk: verify the four files (L35), fill `08`'s launch row into its `R__` (L7), launch `08` first — `cd /Users/cobalt/cobalt-wt/drc-d1`, then its `claude --bg` line — and answer ESCALATE 1–4 before it.

DRC CHAIN REISSUED · files: 4 · tip: 10163d51 · merge-base behind main: 590 commits · laws meaning changed: 0 · new rule strings: 0 · ESCALATE: 8
