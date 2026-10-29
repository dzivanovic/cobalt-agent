# Draft: open every day mode, sheet check warns
Seat `draft-daymode-open` (Opus 5.5), prompt `prompts/2026-10-29/1080-draft-daymode-open.md`. Reads only; nothing committed; no existing file edited. Times ET from `date`.

## §0 Headline
- Card 1081 (K3 prodwrite): `cobalt settings load --from /Users/cobalt/cobalt/data/backups/daymode-open-2026-10-29/forward --apply`; only `daymode.enabled_modes` moves to `[reduced, half, full]`. The count read proves only one row took the new source.
- Route proven from the code: `--from <dir>` writes all seven keys, but skips a key equal to the database (`store.py:90-92`). `--from-git` has no usable source: `bd25d471d^` lacks `trade_count_over_band`, so `config.py:265-271` refuses it.
- 1081 cannot launch until the desk fills four things: the two YAML dirs built from a production read, their sha256s, and two production dry runs (forward shows exactly one `~`; rollback shows `no differences`).
- Card 1082 (build, MID): `assert_sheet_matches` becomes `sheet_warning`, which returns a string and never raises. `/size` (`web.py:1033`) and the radar key tap (`web.py:1771`) write the card and show the warning. `attested_sheet` is never written; `assert_grade_allowed` is unchanged.

## DECISIONS
- ASK DESK: 1081's WRITE RULING is R2563 (HIS RULING · APPROVED, K3 "a ruling of his"), but L7 asks him to approve the exact file by sha256. Default: R2563 stands; the four sha256s and both dry runs are pinned in the card's `## RECORDS`. [17:43]
- ASK DESK: PRODWRITE-HUB has no dry-run step and its seat can create no file. Default: the desk builds the `forward/` and `rollback/` dirs under `data/backups/daymode-open-2026-10-29/` from one production read, then runs GATE 1 and GATE 2. The card's `«FILL»` lines hold the launch until that is done. [17:43]
- ASK DESK: the prompt names one refusing caller, but grep finds two card paths (`web.py:1033` `/size`, `web.py:1771` radar key) plus the banner (`web.py:609`). Default: 1082 makes all three warn. [17:43]
- ASK DESK: a note/selector attestation conflict (`NoteAttestationConflict`, `web.py:560-564`) still refuses every card through `dm["error"]` (`web.py:1011-1015`). Default: left unchanged, because it is not the sheet-vs-mode check. [17:43]
- ASK DESK: his A/B letter is not yet given; 1082 is drafted on the desk's reading A. Default: A; a B from him voids 1082. [17:43]

## RECORDS
- 17:36 `date`; main `1fd977ab` (`git rev-parse --short=8 main`).
- Read: `prompts/CARD.md` whole; `areas/cobalt.md` `## What Cobalt is`, `## Build rules` down; `topics/writing-rules.md`; `LAWS.md` L7, L42, L81; `prompts/PRODWRITE-HUB.md`; precedent cards `2026-10-23/1030-restore-radar-benchmark-card.md`, `2026-10-26/1068-radar-mirror-scope-port4-card.md`.
- `git show main:` (via `git grep -n -e "" main --`): `src/cobalt/daymode/match.py` (`:71-77` `SheetMismatch`, `:80-117` `assert_sheet_matches`, `:99-107` none attested, `:110-116` mismatch, `:120-143` `assert_grade_allowed`, `:146` `__all__`); `daymode/propose.py:58-61` (the clamp); `daymode/config.py` (`:156-158`, `:178-185`, `:189-239`, `:265-271`, `:284-289`, `:309-326`); `settings/models.py:33-48`, `:349-386`; `settings/cli.py` whole (`:88-100`, `:249-330`, `:283`, `:309`, `:313`, `:320`); `settings/store.py:60-117`; `settings/drc.py:143-161`.
- `git show bd25d471d --stat`: `configs/cobalt/aset.yaml` and `daymode.yaml` deleted; `git show bd25d471d^:configs/cobalt/daymode.yaml`: `enabled_modes: [reduced]`, six step-down rows.
- `ls` `data/backups/`: `pre-stack-0919/daymode-settings-rollback/{aset,daymode}.yaml` (09-19, the shape); the forward dir `cobalt-wt/ops-2026-09-18/scratch/daymode-settings-0918` is gone (exit 1). `git check-ignore -v` → `.gitignore:6:data/`.
- `git grep -n` `SheetMismatch|assert_sheet_matches` main `src`: `aset/web.py:55,57,536,609,612,968,1012,1033,1035,1241,1247,1258,1745,1771,1783,1825`; `daymode/__init__.py:27,60,62`. `git grep -c -F "assert_sheet_matches("` → `web.py` 3, `match.py` 1.
- `git grep -n` main `tests`: `test_daymode.py:31,33,191,400-428,518-525`; `test_aset_web.py:432-448`; `test_radar_card_routes.py:113-119`; `test_sheet_daymode_probe.py:128`; read `web.py:525-640`, `:955-1101`, `:1225-1265`, `:1700-1834`.
- `git grep -l cobalt.daymode` main `src`: aset (`radar_panel`, `store`, `web`), `cli`, `drc/imports`, `drc/store`, `heartbeat/runner`, `prefill/checkpoint_probe`, `prefill/checkpoints`, `prefill/daily`, `radar/evaluate`, `radar/runner`, `settings`.
- `git grep cache` main `src/cobalt/settings src/cobalt/daymode src/cobalt/aset/config.py` → only `settings/card.py:231` ("no cache").
- `cto-2026-10-29.md:10` R2563, `:13` R2560 (grep); `survey-settings-writer-2026-10-23.md` (writers: `cli.py:317`, `web.py:1365`); `cto-2026-09-18.md` R4/R10 and `deploy-2026-09-19.md:145` (the `--from` precedent, approved by sha256).
- Wrote `prompts/2026-10-29/1081-daymode-enabled-modes-card.md`, `prompts/2026-10-29/1082-sheet-check-warns-card.md`, this report. 17:43 `date`.

DRAFTED · decisions: 5
