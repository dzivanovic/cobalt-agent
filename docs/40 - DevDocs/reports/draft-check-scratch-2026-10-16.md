# Draft: check-scratch-1016 (K5 gap-filler), 2026-10-16

## §0 Headline
- Card written: `prompts/2026-10-16/641-check-scratch-card.md` (K5, `BAND: MID`, `DB: none`, `RESTARTS: none`); `BASE` is a `«FILL»` for the desk, `TIP` empty.
- The cause is narrower than the prompt says: `stage-set.sh` already clears a prior check folder (card 413 T1), but `clearable()` looks for the prior card copy under the CURRENT card's file name (`:108-112`), so a fix round's check card (638, not 633) never matches.
- Fix = option 1, smaller: `clearable()` takes the one `*-card.md` in `$dest/files` and proves it a prompts card on `main`; every other test stays. Rows: CS-1 (RED + edit + five controls), R2 (RUN). Option 2 is the alternative.
- Files: `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`. Nothing run; every RED is UNPROVEN until the builder quotes it.

## DECISIONS
1. ASK DESK: `BAND` of the card. Default: `MID` (a destructive-path script edit, one file and its test, unsure between LOW and MID: the higher of the two). Change the header line if the desk scores it differently. [11:45 ET]
2. ASK DESK: option 1 as the fix, built as "extend the existing clear to any earlier card of the same JOB" (the clear exists; no move-aside as `<name>-pass<n>`). Alternative, not built: option 2, `scratch-clean.sh` admitting `agy-trial/scratch/tribunal-bars-0920/<name>-check` (it overturns the (5)(a) refusal of the whole `agy-trial` tree and still needs a desk call per pass). Default: option 1. [11:45 ET]
3. ASK DESK: `RULINGS: 2026-10-15 R1532` is taken from the prompt's LADDER; no `HIS RULING` row covers this fix. Default: keep as written. [11:45 ET]
4. ASK DESK: until `band-routing-1015` deploys, `BAND` is no field of `CARD.md` on `main`; the `BAND: MID` line is harmless to the launcher meanwhile. Default: keep. [11:45 ET]
5. ASK DESK: the second check of `band-routing-1015` (card 638) stays blocked until this card is deployed, or until the folder is removed by a hand `mv`/`rm` that only he can authorize. Default: wait for the deploy path; no workaround drafted. [11:45 ET]

## RECORDS
- 11:40 ET (the machine's `date`): `git -C /Users/cobalt/cobalt status --short -- ops/desk/stage-set.sh ops/desk/scratch-clean.sh tests/ops/test_stage_set.py` printed nothing; the tree equals `main` for these files.
- `git -C /Users/cobalt/cobalt show main:ops/desk/stage-set.sh`: whole; `clearable()` `:92-122`, prior-copy lines `:108-112`, the refusal raised at `:109`, `rm -rf` lines `:149`, `:156`, the `cleared:` print `:155`; the lines 106-133 were re-read with line numbers.
- `git -C /Users/cobalt/cobalt show main:ops/desk/scratch-clean.sh`: whole; refusal "agy-trial is the check hubs' scratch tree, never cleaned here" under (5)(a); `tests/ops/test_scratch_clean.py:315-318` pins it.
- `tests/ops/test_stage_set.py` `:1-337` whole (fixture `job`, `prior_staging`, `snapshot`, `test_c1_…` to `test_c12_…`).
- `reports/band-routing-check-fr1-2026-10-16.md` last 5 lines (the refusal text); `prompts/2026-10-16/633-…-card.md` and `638-…-card.md` lines 1-16 (same JOB `band-routing-1015`, different file and `CHECK REPORT`).
- `prompts/CARD.md` whole and `prompts/2026-10-15/583-band-routing-card.md` whole (shape).

DRAFTED · decisions: 5
