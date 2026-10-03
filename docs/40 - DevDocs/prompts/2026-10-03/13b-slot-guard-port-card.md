JOB: slot-guard-port
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/slot-guard-port-1003
WORKTREE: slot-guard-port-1003
BASE: «FILL: the 8-hex head of main after set 2 (card 11 dev-rebuild on main) is DEPLOYED»
TIP:
REPORT: /Users/cobalt/cobalt-wt/slot-guard-port-1003/docs/40 - DevDocs/reports/slot-guard-port-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R157

## ROWS

WHY: card `13` slot-guard was built on card `11`'s BUILD tip `1df251b9` and checked (`CHECK DONE`, `ready: YES`, tip `05c8b7fa`), but `11`'s check then moved `11` to `07cc965f` (fix O1–O5), and `13`'s head `834d4c69` does not merge onto it: `git merge-tree --write-tree` conflicts in `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` and `tests/cobalt/test_dev_rebuild_db.py`; `src/cobalt/db_migrations/dev_rebuild.py` auto-merges (desk, 10-03). No worker runs `git merge` or `git rebase`, so this is a PORT in the shape of card `16`: the checked diff is re-applied onto `main` by Edit and Write, every file the conflict did not touch is proven byte-equal to the checked tip, and the two conflict files are settled by hand keeping BOTH sides' content. The rows of `13` are not re-decided; its check stands for what is byte-equal, and this card's check reads only the two settled files and the suites.

| row | what | red first | files |
|---|---|---|---|
| P1 | THE PORT. `git diff --name-only 1df251b9..05c8b7fa` lists `13`'s files. For each file NOT among the two conflict files: write it from `git show 05c8b7fa:<path>` (Write tool, content read by `git show`), then prove `git hash-object <path>` equals `git rev-parse 05c8b7fa:<path>`; record each pair. For `src/cobalt/db_migrations/dev_rebuild.py`: the auto-merge result is NOT trusted blind — write `13`'s version of each hunk onto `main`'s file by Edit so that `11`'s O1–O5 lines and `13`'s guard lines both stand; quote `git diff 07cc965f -- <path>` and `git diff 05c8b7fa -- <path>` whole, each showing only the other card's lines | the ported with-DB tests of `13` (its card's rows S0–S2 name them) red on `BASE` for `13`'s reasons (quote the first line of each) and green at the tip — one lock take at E2 as `BUILD-HUB.md` `## E2` runs a with-DB red | every path of `git diff --name-only 1df251b9..05c8b7fa` except the two conflict files, plus `src/cobalt/db_migrations/dev_rebuild.py` |
| P2 | THE TWO CONFLICT FILES. `tests/cobalt/test_dev_rebuild_db.py`: `11`'s check tests (O1–O5 at `07cc965f`) and `13`'s tests (at `05c8b7fa`) both stand in the file; no assertion of either changes; the file's test count equals the sum of the two sides' counts minus the tests they share by name (list them). `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`: both sides' sections stand, `13`'s guard section after `11`'s fix notes; no sentence of either is dropped | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_db.py` offline → the with-DB tests skip (marked), the offline ones pass; the same file inside the W lock take → every test passes; a `grep -c "^def test_\|^    def test_"` of the file equals the stated sum. RED on `BASE`: `13`'s tests absent | `tests/cobalt/test_dev_rebuild_db.py`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` |

## NOT IN THIS JOB
- Any new behaviour: not one line that is in neither `07cc965f` nor `05c8b7fa`. A line that must be written to make the two sides coexist is named under `## DECISIONS` with both sides quoted.
- `git merge`, `git rebase`, `git cherry-pick`, `git checkout <path>`: not on your line; the port is Edit and Write from `git show`.
- The SELF-HEAL hub text (card `02` A1) and the devfix verbs (`03b`).

## READ
- `prompts/2026-10-02/13-slot-guard-card.md` whole (the rows this card ports; S0–S2); `prompts/2026-10-02/11-dev-rebuild-card.md` `## ROWS`.
- `reports/slot-guard-check-2026-10-02.md` `## §0`, `## RUNS`, last line; `reports/dev-rebuild-check-2026-10-02.md` `## FIXES` (O1–O5: what `07cc965f` changed and why).
- `git show 1df251b9:…`, `git show 05c8b7fa:…`, `git show 07cc965f:…` for the two conflict files: three versions, read whole.
- `prompts/2026-10-02/16-ops-seam-card.md` `## ROWS` (the port shape and its byte-equality proof).

## CHECK ASKS
- X1 Is every non-conflict file byte-equal to `05c8b7fa`'s blob? Re-run the hash pairs.
- X2 In `dev_rebuild.py` and the two conflict files: is any line of `07cc965f` (O1–O5) lost, or any line of `05c8b7fa` (the guard) lost or weakened? Diff each against both parents.
- X3 Is there a line in the tip that is in neither parent, and does `## DECISIONS` name it?
- X4 The slot guard against `11`'s fixed `dev-rebuild`: run `13`'s guard tests against the ported module (not against `1df251b9`'s): do they still assert what the card says?

## RECORDS
- Judge, 10-03 (adoption-scripts set-2 planning): `11` ships alone in set 2; `13` ships in set 3 by this port (desk trial merge: two conflict files, one auto-merge).
- This job is with-DB (`src/`, `tests/cobalt`): it takes the lock as `BUILD-HUB.md` says.
- `13`'s check (`05c8b7fa`, `ready: YES`) stands for the byte-equal files; this card's check reads the settled files and runs the suites.
