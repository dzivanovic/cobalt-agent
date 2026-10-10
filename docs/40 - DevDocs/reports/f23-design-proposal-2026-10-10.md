# F23 Playbook PPTX renderer · design proposal · 2026-10-10
Proposer: Opus 5.5 drafter `f23-design` (S5 Lane D). Input to the L67 tribunal; no card yet.
Code base: main's code commit `d0a5fbb8` (working tree `src configs tests ops pyproject.toml uv.lock` = `d0a5fbb8`, empty `git diff --stat`).

## 1. Acceptance (Charter:209-211)
- The weekly review opens a deck rendered from the playbook data.
- Test: one deck per setup family, with the latest cards.
- Moment: M11, Sunday 18:00 weekly review (Charter:58). Ladder: "trade-reporter renderer from playbook data; Sunday 18:00 job" (LADDER:936), "no vault write" (LADDER:942).

## 2. Scope
A Sunday one-shot job reads the playbook data, writes one `.pptx` per setup family to a local folder, and exits. No surface, no vault write, no ranking.

### 2.1 The data
- **Setup family** = the taxonomy `Family` enum, five values: `opening_drive`, `continuation`, `range_break`, `reversion`, `time_window` (`taxonomy/trade_def.py:116-121`). A def lists one or more (`trade_def.py:745`, `min_length=1`).
- **Setups** = the validated defs from the vault's strategy notes, read by `load_vault_trade_defs(vault_root)` (`taxonomy/vault_loader.py:472`), folder `1 - Trading/4 - Strategies` (`vault_loader.py:91`). Each `LoadedTradeDef` carries `slug`, `name`, `note_path`, `definition.family` (`vault_loader.py:135-147`). A setup with two families appears in both decks. Drafts (`VaultTradeDefs.drafts`, `:175`) carry no def and no family; they are listed on the run's stdout, never in a deck.
- **Cards** = radar cards: `"user".aset_sizings` rows with `origin = 'radar'`; each carries `trade_def_slug` NOT NULL by constraint (`db_migrations/0007_radar_cards.sql:78`). Card → family by `trade_def_slug` → the loaded def's `family`.
- **Latest** = the newest `N` cards per family by `formed_at` (`0007:39`), every state. `N` = 10 (config).
- A card whose slug has no loaded def (def deleted or drafted since) goes to an `unfiled` deck, counted; never dropped (L1).
- Live vault on 2026-10-10: 22 strategy notes carry `family:`; 13 non-empty. Deck sizes: opening_drive 6 setups, continuation 7, reversion 4, range_break 2, time_window 0.

### 2.2 The deck (one per family, plus `unfiled`)
1. Title slide: family name, the week (Mon–Fri ET dates ending the run's Sunday), "rendered HH:MM ET", counts (setups, cards shown, cards in family overall).
2. One slide per setup in the family: name, `note_path`, class, the def's family list, count of its cards in the deck.
3. Card table slides, 8 rows per slide, newest first: date (ET of `formed_at`), ticker, setup name, direction, state, grade (`sized_grade` else `tapped_grade`), trigger price, structural stop, entry, stop, `card_score`, `why` (cut to 120 chars, cut marked `…`).
4. An empty family renders a deck whose one content slide says "no setup in this family" or "no cards yet" — loud, never a missing file.
- Plain `python-pptx` layout built in code (blank 16:9 presentation, default theme), no template file.

### 2.3 The job
- CLI: `uv run cobalt playbook render [--date YYYY-MM-DD] [--out DIR]`. Default date = today ET; default out from config.
- Runs inside `with job_run("com.cobalt.playbook") as run:` (`jobs/wrapper.py:125`), the pattern of `generated/cli.py:56` and `seatusage/runner.py:239`, so F18 sees it.
- Output: `data/playbook/<YYYY-MM-DD>/<family>.pptx` (`data/` is gitignored, `.gitignore:6`); a same-day rerun overwrites that day's folder whole (write to `<date>.tmp/`, then rename). Stdout lists each path, its slide count, card count, the unfiled count and the draft slugs.
- Reads: production DB, read-only, one SELECT on `"user".aset_sizings` (USER side, `db.connect(..., side=Side.USER)`, `db.py:227`); the vault strategies folder, read-only. Writes: only the output folder and the job's own `jobs` heartbeat row via `job_run`.
- Schedule: Sunday 17:30 ET (`weekdays: [0]`, `jobs/config.py:27` 0 = Sun), so the deck exists when the 18:00 review opens.

## 3. Files touched
| File | Change | Shared? |
|---|---|---|
| `src/cobalt/playbook/__init__.py` | new package | no |
| `src/cobalt/playbook/data.py` | read defs + cards, group by family → plain dataclasses | no |
| `src/cobalt/playbook/deck.py` | dataclasses → `.pptx` bytes; no I/O but the save | no |
| `src/cobalt/playbook/cli.py` | `add_parser(sub)`, `render` under `job_run` | no |
| `src/cobalt/playbook/config.py` | pydantic loader for `playbook.yaml` | no |
| `src/cobalt/cli.py` | one import + one `playbook_cli.add_parser(sub)` line in the list at `cli.py:520-543` | one-line seam |
| `configs/cobalt/playbook.yaml` | new: `latest_per_family: 10`, `rows_per_slide: 8`, `why_max_chars: 120`, `out_dir: data/playbook` | no |
| `configs/cobalt/jobs.yaml` | one row `com.cobalt.playbook` in one-shots after `com.cobalt.generated` (`jobs.yaml:298`); one `no_resident_reads` entry for `configs/cobalt/playbook.yaml`, reader `com.cobalt.playbook` (`jobs.yaml:327`) | the named seam (R746) |
| `ops/com.cobalt.playbook.plist` | new; shape of `ops/com.cobalt.cards-expire.plist` (absolute `uv`, `COBALT_ENV=production`, `COBALT_VAULT_PATH`, one `StartCalendarInterval` Weekday 0 Hour 17 Minute 30, `RunAtLoad false`, logs `logs/playbook.{log,err}`) | no |
| `pyproject.toml` | one dependency line `python-pptx==<locked version>` next to `python-multipart` (`pyproject.toml:35`) | seam (see R2) |
| `uv.lock` | regenerated by `uv lock`; adds `python-pptx` (and `XlsxWriter`, its own dependency); `lxml` (`uv.lock:2681`) and `pillow` (`:3652`) already locked | seam (see R2) |
| `tests/cobalt/test_playbook_*.py` | §5 | no |
| `docs/40 - DevDocs/cobalt/playbook/README.md` | module doc, as `docs/40 - DevDocs/cobalt/aset/web.md` | no |

## 4. Config row (jobs.yaml)
```yaml
  - label: com.cobalt.playbook
    kind: one-shot
    supervisor: self
    timeout_s: 600
    schedule: {at: "17:30", weekdays: [0]}
    what: "the Sunday playbook decks, one .pptx per setup family (uv run cobalt playbook render)"
```

## 5. Tests
Offline (no DB):
1. Fixture vault (tmp) with 3 strategy notes, families `[opening_drive]`, `[opening_drive, continuation]`, `[]` draft → `data.py` puts setup 2 in two decks, lists the draft, renders 5 family decks + `unfiled`.
2. Deck read back with `python-pptx`: title text, one slide per setup, table rows in `formed_at` desc order, 8 rows per slide (17 cards → 3 table slides at N ≥ 17).
3. `N` cap: 12 cards, `latest_per_family: 10` → 10 rows, newest 10.
4. Empty family (`time_window`) → its deck exists with the "no setup in this family" slide.
5. Card slug absent from the defs → in `unfiled.pptx`, counted on stdout.
6. `why` of 300 chars → 120 + `…`.
7. Rerun same date → the folder holds only the new run's files.
8. No vault write: the fixture vault's file list and every mtime are unchanged after a run; `vaultwrite` is never imported by `cobalt.playbook` (import check).
9. Registry: `cobalt validate` passes with the new row and plist (plist ↔ `jobs.yaml` schedule match); `cobalt jobs readers configs/cobalt/playbook.yaml` exits 0 naming `com.cobalt.playbook`.
With-DB (`cobalt_dev`, under L76's lock):
10. Seed radar cards with `create_radar_card` (`cards/store.py:1121`) through the existing helper `tests/cobalt/radar_p2_support.py`, two slugs, mixed states → `render` reads them, grouped right; manual-origin cards absent.
11. `job_run` stamps a `done` row for `com.cobalt.playbook`.
Live-note suite: run `render` against his real strategies folder (`COBALT_LIVE_VAULT_ROOT`, read-only) and `cobalt_dev` → 5 decks + `unfiled`, deck setup counts 6/7/4/2/0 as of 10-10 (or the counts the notes hold on the build day, printed).
Each new test shown red first (L67 check flow).

## 6. Risks
- **R1 New package.** `python-pptx` is not in `pyproject.toml` or `uv.lock` at `d0a5fbb8`; it brings `XlsxWriter`. `lxml` and `pillow` are already locked. Pin exact, as `python-multipart` (`pyproject.toml:33-35`).
- **R2 Lock seam.** `pyproject.toml` and `uv.lock` are shared with any lane that adds a package; F20's Agent SDK is the likely one. A trial-merge conflict in `uv.lock` is resolved by re-running `uv lock` on the combined `pyproject.toml`, never by hand-merging the lock (R746).
- **R3 `cli.py` seam.** One line in the parser list; a conflict is an adjacent-line merge.
- **R4 Production read on Sunday.** One SELECT at 17:30; nothing else runs then (archiver/replay weekdays only, backup 21:40, `jobs.yaml:268`). Read-only.
- **R5 Vault edits mid-read.** He may edit a strategy note at 17:30; the read is one pass, and a note failing validation shows as a draft/error on stdout, never a crash.
- **R6 Thin data.** Radar cards started in S2; some families show few or no cards. The empty deck is the honest output.
- **R7 Fonts.** Default theme fonts only; no font file shipped.

## 7. Not in F23
- The licensed SMB 17-slide template and trade-reporter's per-trade fill (`playbook_builder.py`, local-only reference, untracked; template `docs/90 - References/assets/`, gitignored `.gitignore:31`).
- Charts, screenshots or images of any kind.
- P&L, R, win rate or any statistic computed over cards.
- Any ranking or scoring: cards are ordered by time; `card_score` is shown as stored (L52 not triggered).
- Manual (non-radar) cards.
- A vault write, a link in the weekly note, a Mattermost DM.
- A web page or upload flow; retention or pruning of old deck folders.
- Vital Dawn (LADDER:942 SHOULD).

## 8. Open choices (each with its default)
| # | Choice | Default | Reason |
|---|---|---|---|
| C1 | What is a "setup family" | The taxonomy `Family` enum (5) | It is the code's and the notes' own field (`trade_def.py:116`, notes' `family:`); the Charter's word matches it. |
| C2 | Which cards | Radar cards only (`origin='radar'`) | Only they carry a `trade_def_slug`, the one deterministic link to a family (`0007:78`); a manual card would need a guess (L1). |
| C3 | "Latest" | Newest 10 per family by `formed_at`, every state | The Charter names no window or state; a missed or expired card is review material too. `N` is config. |
| C4 | Template | Plain `python-pptx` deck built in code | The SMB template is one trade per deck, licensed and untracked, so the gate and a fresh checkout cannot use it. |
| C5 | Library | `python-pptx`, pinned exact | The reference renderer's library (trade-reporter `requirements.txt`); its heavy deps are already locked. |
| C6 | Output place | `data/playbook/<date>/`, outside vault and git | LADDER:942 says no vault write; `data/` is gitignored. |
| C7 | Run time | Sunday 17:30 ET | The deck must exist when the 18:00 review opens (Charter:58); the ladder's "18:00 job" is read as the review moment. |
| C8 | Telling him it is ready | No DM; the path is fixed and stdout lists it; F18 reports a failed run | Keeps F23 off the notify path; a DM is a small later card if he wants one. |
| C9 | Empty family | A deck is rendered with an explicit empty slide | "One deck per setup family" holds for all five; an absent file reads as a failure. |
| C10 | Card with no loaded def | An `unfiled` deck, counted | Never dropped silently (L1). |
| C11 | Rerun same day | Overwrite that day's folder whole (tmp + rename) | A half-written folder is never left. |
| C12 | Build model | Opus 5.5 | BUILD-HUB:3 and L29 overtake LADDER:942's Sonnet. |
| C13 | Check house B | Not mandatory | F23 writes no vault note and changes no sizing (L67 MANDATORY HOUSE B). |
