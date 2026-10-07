# devfix-sizings-draft 2026-10-07

## §0 Headline
- No card written. The task says to stop with `decisions: 1` if no `BRANCH` / `WORKTREE` convention for a devfix is stated; none is.
- `CARD.md:15-16` says only "the branch of its worktree" and "the tree its dev commands run from". No devfix has ever run, so no precedent names one.
- Main HEAD is `e479fff9`, not `6286f526` as the prompt says. `BASE` would be `e479fff9`.
- Proof test found: `tests/cobalt/test_dev_rebuild_db.py::test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings`.

## CARD
Not written: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/99-devfix-aset-sizings-card.md` is absent (`ls` exit 1). The rest of the header is ready:

| key | value |
|---|---|
| JOB | `devfix-aset-sizings-1007` |
| LADDER | `OFF-LADDER — reports/deploy-radar-direction-color-1007.md 2026-10-07 R638` |
| BRANCH | held, see DECISIONS |
| WORKTREE | held, see DECISIONS |
| BASE | `e479fff9` |
| REPORT | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/devfix-aset-sizings-2026-10-07.md` (absent, `ls` exit 1) |
| RULINGS | `2026-10-07 R625` |
| TABLE | `user.aset_sizings` |
| PROOF TEST | `tests/cobalt/test_dev_rebuild_db.py::test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings` |

PROOF TEST proof that it runs against `user.aset_sizings`: `tests/cobalt/test_dev_rebuild_db.py:237` defines it, its name says so, and its SQL at `:232` reads `"user".aset_sizings`. `reports/slot-guard-build-2026-10-02.md:140` names it as the slot-guard's with-DB test, and `reports/slot-guard-check-2026-10-02.md:166` records it ran in pass 1. The launcher accepts the form (`ops/desk/desk-launch.sh:1015-1030`: `tests/cobalt/<file>.py::<name>`). Caveat: it asserts `slot_report` equals the slot read; it does not assert a lower `max_attnum`. The rebuild itself proves the drop (`REBUILT … max_attnum <b> → <a>`).

## DECISIONS
- ASK DESK: `BRANCH` and `WORKTREE` for this devfix are not stated anywhere (`CARD.md:15-16`, `DEVFIX-HUB.md:9`, `desk-launch.sh:1044-1047` give the shape only). The two devfix-named cards are build cards: `ops/devfix-route-1002` and `ops/devfix-verbs-1003`. Default if you do not answer: `BRANCH: ops/devfix-aset-sizings-1007`, `WORKTREE: devfix-aset-sizings-1007`. Neither is in `cobalt-wt` (`ls` listing). [13:00 ET]
- ASK DESK: `BASE`. The prompt says main HEAD is `6286f526`. `git rev-parse --short=8 HEAD` gives `e479fff9`, the prompt-98 commit. Default: `e479fff9`, per "main HEAD at the time you write". [13:00 ET]

## RECORDS
- Reads: `prompts/2026-10-07/98-draft-devfix-sizings.md`; `Memory/areas/cobalt.md` (whole); `prompts/DEVFIX-HUB.md` (whole); `prompts/CARD.md:136-139` and `:11-28` rows by grep; `ops/desk/desk-launch.sh:1000-1051`; `reports/deploy-radar-direction-color-1007.md` (whole; slot counts at `:5`, `:86`, `:93-95`, `:124`).
- Slot counts: `user.aset_sizings` 1538 of 1600 at the guard. 1534 after pass 1, before the forward migrate (`:93`). Forward migrate of 0014–0022 took `max_attnum` 1534 → 1538 (`:94`, `:124`). `cobalt_dev` back at 0013, F2 = F0 (`:96`).
- `git rev-parse --short=8 HEAD` → `e479fff9`. `git status` at session start named `6286f526` as HEAD's parent in the log, not HEAD.
- Precedent search: `grep dev-rebuild` over `docs/40 - DevDocs` → 61 files. `ls reports/devfix-*.md` → two build/check reports only, no devfix run.
- `ls /Users/cobalt/cobalt-wt` → no `devfix-aset-sizings-*` entry.
- `date` → Wed Oct 7 12:58:31 EDT 2026.

FAILED: BRANCH/WORKTREE convention for a devfix not stated, no card written · decisions: 1
