## §0 Headline
Card 731 amended in place for the four preflight fails; PORT stays one row.
FIX 1: PORT (1) states both cases (a) main without 469, (b) with 469 (`0027` between `0026` and `0028`); ORDER says (b) is expected.
FIX 2: the `0026_market` grep is scoped. FIX 3: card 877 named in CHECK ASKS. FIX 4: `CHECK REPORT:` and `HOUSE B:` blanked; 469 tip cite is `c56817ec`.
Nothing run, nothing committed.

## DECISIONS
- ASK DESK: case (b) pin widths for the 18 pin files other than the five I traced (`test_archiver_migrations`, `test_f15_p1_records_offline`, `test_seam_drc_s3_registry`, `test_dml_roles_offline`, `test_assumed_store`) are left to the builder's by-content re-find. Default: builder re-finds; the check verifies against the 469 tip. [00:00]
- ASK DESK: `HOUSE B:` is blank on the card, so the desk sets it if the launcher needs it. Default: launcher's build `need` list does not read it (preflight check 7). [00:00]

## RECORDS
- Drafter `draft-f5-port-amend`, Tue Oct 20 00:00 EDT 2026 (`date`). Read: prompt 889; card 731 whole; `reports/f5-checkpoints-fr1-preflight-2026-10-19.md`; `topics/writing-rules.md`. Reads from git: `rev-parse --short=8 main` → `918d175f`; `git grep` on `main` of `db_migrations/__init__.py` (`:111`, `:114`, `:155`, `:180`, `:184`, `:185`) and of four pin files; `git grep` on `c56817ec` of `db_migrations/__init__.py` (`:123-124`, `:167`, `:192`, `:197`, `:199`) and of `tests/cobalt` for `0026`/`0028`/`FORWARD[`/`REVERSE[`. Edits: the card only (header, PORT (1), PORT stop grep, ORDER, CHECK ASKS, one RECORDS line). Nothing run, no git write.
- Not traced: `git show 11eb0d24:` (the card's older 469 cite is kept in PORT (1) as "reads the same", from preflight check 23).

DRAFTED · decisions: 2
