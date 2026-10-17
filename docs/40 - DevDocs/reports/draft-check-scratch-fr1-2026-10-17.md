# draft-check-scratch-fr1 — card 681 drafted · 2026-10-17

## §0 Headline
- Wrote `prompts/2026-10-16/681-check-scratch-fr1-card.md`: a K5 BUILD for the fresh job `check-scratch-fr1` (rows R0, MK-1 marker write, CL-1 `clearable()` reads it, R2).
- RED proofs as the brain set them: (1) the 638+666 shape, no marker, refuses today and clears after; (2) a marker naming another JOB's card refuses; (3) two same-JOB cards clear only by the marker.
- The brain's rule retires two existing controls (two same-JOB cards no longer refuse) and breaks one existing test's setup: 2 decisions below.
- The real `band-routing-1015-check` folder holds one check card (666) plus the 583 build copy, not 638 plus 666.

## DECISIONS
- ASK DESK: `test_cs1_control_two_card_copies_are_refused` and `test_fr1_control_two_same_job_check_cards_are_refused` pin the count refusal; with a marker (or the highest-numbered legacy rule) an extra same-JOB copy clears, so both turn red by the brain's design. Delete both (their two-card cases are now new tests (1) and (3)), or keep them as legacy-shape tests some other way? [09:00 EDT] Default taken: delete both, in the card's ORDER.
- ASK DESK: `test_cs1_rewritten_job_line_is_refused_by_the_job_test_not_the_blob` unlinks the first copy, so the marker names a missing file and the message changes. Add ONE line writing the marker to name the y-job copy (no assertion changed), so the JOB test line still decides it? [09:00 EDT] Default taken: add the one line.

## RECORDS
- Reads (09:00 EDT): `main:ops/desk/stage-set.sh` whole (`clearable()` `:92-145`, count test `:132`, version test `:134-136`, JOB test `:137`, `rm -rf` `:173` `:180`, `cleared:` `:179`, card copy `:219`); `tests/ops/test_stage_set.py` whole (fixture `:51-86`, `prior_staging` `:193`, `test_cs1_…` `:359-440`, `test_fr1_…` `:468-514`, FR-2 test `:518-`); the brain's answer item 3; `CARD.md`; card 641; headers of 638 and 666; `src/cobalt/jobs/restarts.py` `:38`, `:225-232`, `:246`. Working tree equals `main` for the two files (`git status --short` empty). Nothing was run but reads.
- `ls …/band-routing-1015-check/files`: `583-band-routing-card.md`, `666-band-routing-fr2-check-card.md`, no 638. The card builds the 638+666 shape in a tmp repo anyway.
- The marker counts as a staged file (`STAGED <n>` one more); `test_the_whole_set_…` counts by `rglob`, so it needs no edit. `band-routing-check-fr2-2026-10-17.md` is on `main` (`git cat-file -e` exit 0). `grep -rn "stage-set" ops tests`: the script and its test only; no `ASK DESK` file.
- `BASE` is a `«FILL»` for the desk; `TIP` and `CHECK REPORT` empty; `BAND: MID` and `RESTARTS: none` follow card 641.

DRAFTED · decisions: 2
