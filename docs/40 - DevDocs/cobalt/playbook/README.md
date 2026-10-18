# `src/cobalt/playbook/`

F23 (card 503, FINAL `docs/30 - Design/F23-FINAL-2026-10-11.md`): the Sunday playbook decks. A one-shot reads the playbook data and writes one `.pptx` per setup family, plus `unfiled`, to a local folder, then exits. No surface, no vault write, no ranking.

## What it does
- `config.py` — `PlaybookConfig`, the Pydantic family of `configs/cobalt/playbook.yaml` (`extra="forbid"`, strict types, no default for any key, L10). `load_playbook_config(path)` raises `ValidationError` on an unknown key, a bad type or a missing key, and `PlaybookConfigError` on a missing file or a non-mapping.
- `data.py` — setups from `load_vault_trade_defs()` (the one loader, L3), family from `definition.family`; cards from ONE SELECT on `"user".aset_sizings WHERE origin = 'radar'` through `db.connect(..., side=Side.USER)` (`fetch_radar_rows`). `group(defs, rows, latest_per_family=…)` is pure and returns a `Playbook`: six `Deck`s (the five `Family` values, then `unfiled`) and the draft slugs.
  - A def with two families puts its cards on both decks; each deck's `also_elsewhere` (K) counts the cards whose def lists another family.
  - A slug that is not a loaded def → `unfiled`, reason `draft` (a draft note's slug) or `no note`. Nothing is dropped.
  - Order: `newest_first`, `formed_at DESC NULLS LAST, id DESC`. Never `card_score`, `conviction` or `proximity` (L52). `latest_per_family: null` = every card; `in_family` is the count before any cap.
- `deck.py` — `build` / `write_deck` / `write_all`: plain python-pptx, blank 16:9, default theme. Title slide (family, `Mon–Fri ET ending this Sunday: <Mon> – <Fri>`, the subtitle `cards are the newest by formed_at, not limited to this week`, `rendered HH:MM ET`, counts, `also in another family: K`); one `setup · <name>` slide per setup; table slides of `rows_per_slide` rows with the twelve §2.2.3 columns, `why` cut to `why_max_chars` + `…`. An empty deck says `no setup in this family`, `no cards yet` (setups, no card) or `no unfiled cards`.
- `cli.py` — `cobalt playbook render [--date YYYY-MM-DD] [--out DIR] [--dry-run]`. `data`, `deck` and python-pptx are imported inside `cmd_render` only, so `import cobalt.cli` leaves `pptx` unloaded (FINAL [F-17]).

## The command
- `render` runs inside `with job_run("com.cobalt.playbook") as run:`; the config loads INSIDE it. Every failure — dead DB, missing strategies folder, a finished note failing validation (`VaultTaxonomyError`), a bad `playbook.yaml`, an unwritable folder, a save error — is a `failed` job row with `exit_code=1`, and `cobalt.cli.main` exits 1 (L1). A draft is not a failure.
- Stdout: each deck's path, slide count and card count; `unfiled cards: <n>`; `drafts: <slugs>`. `run.result`: the date, per family `setups` / `cards` / `in_family` / `slides`, the unfiled count, the draft slugs.
- `--dry-run`: no wrapper; prints the families, counts and the paths a run would write. No deck, no job row.
- `--date` labels the week and names the folder (default: today ET from the session clock). `--out` replaces `out_dir`.

## The output folder and the C11 swap
`out_dir` (`data/playbook`, gitignored) / `<YYYY-MM-DD>/<deck>.pptx`. `publish(out_dir, day, write)`:
1. a leftover `<day>.old` with no `<day>` (a kill between the two renames) is renamed back to `<day>`; one beside a `<day>` is deleted;
2. a leftover `<day>.tmp` is deleted, never written into; a fresh `<day>.tmp` is made and every deck is written there; a missing deck fails the run;
3. `<day>` → `<day>.old`; `<day>.tmp` → `<day>`; a failure of that second rename renames `<day>.old` back; then `<day>.old` is deleted.

`<day>` is never deleted first, so each ending leaves the previous folder or the complete new one. Whether a viewer holding a deck blocks the rename is his E1 check, by day.

## Config it reads
`configs/cobalt/playbook.yaml`: `latest_per_family: null`, `rows_per_slide: 8`, `why_max_chars: 120`, `out_dir: data/playbook`. Read only by the one-shot (`jobs.yaml` `no_resident_reads`). The two layout keys stay UNVERIFIED until his E2 viewer check. No tunables rows (FINAL C7).

## The job
`configs/cobalt/jobs.yaml` `com.cobalt.playbook`: one-shot, `supervisor: self`, `timeout_s: 600`, `{at: "17:30", weekdays: [0]}` (Sunday), `enabled: true`. `ops/com.cobalt.playbook.plist`: absolute `uv run cobalt playbook render`, `COBALT_ENV=production`, `COBALT_VAULT_PATH=/Users/cobalt/Vault/Think`, one `StartCalendarInterval` Weekday 0 Hour 17 Minute 30, `RunAtLoad false`, logs `logs/playbook.{log,err}`. Bootstrap deferred to the deploy (card 496).

## The laws on the job (FINAL [F-16])
- L52: `card_score` is shown as stored; no sort, filter or tie-break on it, `conviction` or `proximity`; no P&L, R or win rate.
- L28: writes `data/playbook/<date>/` and its `jobs` row only. `test_no_vault_write`: the fixture vault's files and mtimes are unchanged after a run AND no `cobalt.playbook` module imports `cobalt.vaultwrite`. (The loader itself imports the read-side parsers `cobalt.vaultwrite.frontmatter` and `.markers`.)
- L1, L10 as above. L53: 17:30 and the card window are neither the Finviz ceiling nor the scan cadence. L32: decks are user data under gitignored `data/`; fixtures are synthetic.

Tests: `tests/cobalt/test_playbook_offline.py` (P1–P5), `tests/cobalt/test_playbook_registry.py` (P6), `tests/cobalt/test_playbook_db.py` (P7, `cobalt_dev`, PASS 2), `tests/cobalt/test_playbook_live.py` (P8, live-note).

## 2026-10-18 — f23-playbook-1013
Package added (card 503 rows P2–P5): `config.py`, `data.py`, `deck.py`, `cli.py`, mounted by `src/cobalt/cli.py`.
