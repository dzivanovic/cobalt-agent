# draft-f5-x3-measure — 2026-10-20

## §0 Headline
- Card drafted: `prompts/2026-10-20/945-f5-x3-measure-card.md` (JOB `f5-x3-measure`, CLASS K2, BASE `5347f90e`, LADDER `OFF-LADDER — reports/cto-2026-10-20.md R2217`, RULINGS `2026-10-18 R1863`).
- Three RUN rows: R1 the probe (30 sequential `checkpoint.narrative` calls on one frozen delta list), V1 the values by the brain's rule (or `HELD`), C1 clean-up and RESTARTS `none`. Time gate 20:35–07:00 ET, checked with `date`.
- The committed K2 fixture is only the Groups CSV (synthetic, on main); the delta list is derived from it by a fixed rule (DECISION 4).
- A request can only LOWER the route timeout (`client.py:99-106`), so the 60 s lift is an in-process config copy at 300 s, `modelaccess.yaml` untouched.
- The builder's line has no way to stage or run a script: the desk stages a one-test pytest file outside the worktree (DECISION 1).

## DECISIONS
1. ASK DESK: how the probe script reaches the builder's line? [18:15] Default: the desk stages `/tmp/f5-x3-measure-run/test_x3_calls.py` before the build launches; the builder runs it with `uv run pytest` (the only admitted string that runs code, `BUILD-HUB.md:14`); the file removes itself at its end; C1 proves it with `ls`.
2. ASK DESK: the lifted timeout. [18:15] Default: 300 s.
3. ASK DESK: `max_output_tokens` lifted too? [18:15] Default: no, 512 stays; a `length` finish is flagged and the value is then a floor, facts to the brain.
4. ASK DESK: the frozen delta list. [18:15] Default: 07:45 = `IDX_0745` plus the fixture's sectors, 08:15 = `IDX_0815` plus the same sectors with the 11 Change strings rotated one place; `compute_delta`; one list for all 30 calls.
5. ASK DESK: mainframe not answering. [18:15] Default: `FAILED: X3 — mainframe unreachable … (call 1)`, the desk checks LM Studio.
6. ASK DESK: LADDER. [18:15] Default: `OFF-LADDER — reports/cto-2026-10-20.md R2217` (no `S5-P?` row found for X3).

## RECORDS
- `date` → Tue Oct 20 18:03:40 EDT 2026 (start), 18:05:47 (card write). Reads only; no network, no production command, no git write, nothing committed. BASE `5347f90e` from `git rev-parse --short=8 main`.
- Read: `prompts/2026-10-20/912-f5-x2-card.md`, `reports/draft-f5-x2-probe-2026-10-20.md`, `prompts/BUILD-HUB.md` (`:14`, `:16`, `:72`, greps of RUN), prompt 944.
- Read from main (`git show` / `git grep`): `docs/30 - Design/F5-FINAL-2026-10-11.md` (`:88`, `:138`, `:177`); `configs/cobalt/modelaccess.yaml` (route `:70`, `timeout_s: 60` `:78`, `max_output_tokens: 512` `:80`); `configs/cobalt/prefill.yaml:38-39`; `src/cobalt/prefill/checkpoints.py` (`:91`, `:190-221`, `:283-323`, `:394-439`); `src/cobalt/modelaccess/client.py`, `config.py`, `models.py` whole; `tests/cobalt/test_checkpoints_offline.py` (`:65-68`, `:393-394`, `:470-473`); `tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` (the only file in that directory; line 1 synthetic marker); card 731 `:27`, `:108`; `reports/cto-2026-10-20.md` R2217, R2218.
- Fixture on main, not a branch. No committed delta-list fixture exists.
- Not traced: that the builder's worktree `Edit` rule writes the REPORT (assumed, same as every build report). The desk preflights `BUILD-HUB.md:14`/`:16`; every command in the card is on those lines.

DRAFTED · decisions: 6
