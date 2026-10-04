JOB: adoption-port
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/adoption-port-1003
WORKTREE: adoption-port-1003
BASE: a8d8a848
TIP:
REPORT: /Users/cobalt/cobalt-wt/adoption-port-1003/docs/40 - DevDocs/reports/adoption-port-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R154, 2026-10-02 R157, 2026-10-03 R3

## ROWS

WHY: the adoption chain (`03` + `02` + `03c`, head `9694a679`, all checked `ready: YES` on the combined tree) could not merge onto `main` beside `11`, `07`, `09`, and `main` has since taken `02b` (`DEPLOY-HUB.md` P7 / STEP-T / STEP-C text, `a8d8a848`). This card PORTS the chain onto `a8d8a848` in the shape of card `16` / `13b`: every file re-applied from `git show 9694a679:<path>` and proven byte-equal by hash where `main` did not change it; the files `main` changed (`DEPLOY-HUB.md` only, by `02b`) settled by hand with both sides. With-DB job (`cli.py`, `conftest.py` are in the chain): it takes the lock.

| row | what | red first | files |
|---|---|---|---|
| P1 | THE PORT. `git diff --name-only a09f0862..9694a679` lists the chain's files. Each file `main` did not touch since `a09f0862` (`git diff --name-only a09f0862..a8d8a848` names what it did): Write from `git show 9694a679:<path>`, prove `git hash-object <path>` = `git rev-parse 9694a679:<path>`; record each pair. A path deleted in the chain is deleted here | the chain's with-DB tests (`test_migrate_level.py`, `test_db_only_selection.py` as they stand at `9694a679`) red on `BASE` for their reasons, green at the tip — one lock take at E2 | every chain file but `DEPLOY-HUB.md` |
| P2 | `DEPLOY-HUB.md` = `main`'s text (`02b`: P7, STEP-T, STEP-C sentences) PLUS the chain's adoption sentences (`02` A3, A4, A7, A8 at `9694a679`), written by Edit so both stand; where a sentence exists in both, `02b`'s words win for P7 / STEP-T / STEP-C and the chain's for STEP-G, P1 (v), LAUNCH, THE RELEASE. Then the four rulings of `reports/deploy-hub-text-decisions-2026-10-03.md` items 5–8 written against the chain's own clauses: (5) STEP-G's exit-5/6 bullet ends "the release is `gate.sh`'s trap on every exit; verify `<GATE>/.env` gone and the lock dir absent, then the FAILED line"; (6) the equal-tree clause: "ONE branch in `TIP`, `git -C /Users/cobalt/cobalt diff --stat <check code tip> <m1> -- . ":(exclude)docs"` prints nothing, AND the check's stop line carries a with-DB count above 0 → the check's three suite lines are the gate's; otherwise the gate runs whole (`--deploy`)"; (7) P1 (v): "`MIGRATIONS: none` AND an empty derived restart set, provisional at P1; STEP-R re-reads the SET and fails `window (v) does not hold: <labels>` when it is not empty and P1 was outside (i)–(iv)"; (8) the launch line's flag text ends "Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5." | hub text: `grep -n -F` of each distinctive string → one hit; `grep -c -F "MIGRATIONS_DIR / \"00"` → 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |

## NOT IN THIS JOB
- Any new behaviour: not one line in neither `9694a679` nor `a8d8a848` except P2's four ruled sentences. `git merge` / `rebase` / `cherry-pick`: not on your line.
- The devfix verbs (`03b`), the dev-rebuild port (`11b`), the desk-tools port (`07b`).

## READ
- `prompts/2026-10-03/13b-slot-guard-port-card.md` (the port shape); `reports/adoption-hubs-decisions-2026-10-03.md`; `reports/deploy-hub-text-decisions-2026-10-03.md`; `reports/adoption-scripts-b-check-2026-10-03.md` `## §0`.
- `git show 9694a679:docs/40 - DevDocs/prompts/DEPLOY-HUB.md` and `main`'s, whole, side by side.

## CHECK ASKS
- X1 Every non-`DEPLOY-HUB.md` file byte-equal to `9694a679`? Re-run the hash pairs.
- X2 In `DEPLOY-HUB.md`: is any `02b` sentence lost, any chain sentence lost, and do the four ruled sentences match the decisions file word for word?
- X3 Walk STEP-G as a worker: on exit 4, 5, 6 and green, is the lock state and the FAILED/GREEN line unambiguous?

## RECORDS
- Judge, 10-03 21:39 ET: set 3 = `03d`, `11b`, `07b`, `05` (`47a689a1`, checked), `10`; Sunday after 13:00. The `DEPLOY-HUB.md` part gets one Grok read after the check (L67), F1-style fail-loud findings are not holds.
- The three checks of the chain stand for the byte-equal files; this card's check reads `DEPLOY-HUB.md` whole and the suites.
