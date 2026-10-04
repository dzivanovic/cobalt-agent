JOB: adoption-port
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/adoption-port-1003
WORKTREE: adoption-port-1003
BASE: a8d8a848
TIP:
REPORT: /Users/cobalt/cobalt-wt/adoption-port-1003/docs/40 - DevDocs/reports/adoption-port-build-2026-10-03.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B: as needed
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R154, 2026-10-02 R157, 2026-10-03 R3

## ROWS

WHY: the adoption chain (`03` + `02` + `03c`, head `9694a679`, all checked `ready: YES` on the combined tree) could not merge onto `main` beside `11`, `07`, `09`, and `main` has since taken `02b` (`DEPLOY-HUB.md` P7 / STEP-T / STEP-C text, `a8d8a848`). This card PORTS the chain onto `a8d8a848` in the shape of card `16` / `13b`: every file re-applied from `git show 9694a679:<path>` and proven byte-equal by hash where `main` did not change it; the files `main` changed (`DEPLOY-HUB.md` only, by `02b`) settled by hand with both sides. With-DB job (`cli.py`, `conftest.py` are in the chain): it takes the lock.

| row | what | red first | files |
|---|---|---|---|
| P1 | THE PORT. `git diff --name-only a09f0862..9694a679` lists the chain's files. Each file `main` did not touch since `a09f0862` (`git diff --name-only a09f0862..a8d8a848` names what it did): Write from `git show 9694a679:<path>`, prove `git hash-object <path>` = `git rev-parse 9694a679:<path>`; record each pair. A path deleted in the chain is deleted here | the chain's with-DB test `tests/cobalt/test_migrate_level.py` (a chain file at `9694a679`) red on `BASE` (no LEVEL lines), green at the tip — one lock take at E2; `tests/ops` green | every chain file but `DEPLOY-HUB.md` and `CTO-DESK-WAKEUP.md` |
| P3 | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`: touched by the chain (`02` A4's flag) and by `main` since `a09f0862`; settled by Edit with BOTH sides' lines (quote `git diff a8d8a848 -- <path>` showing only the chain's lines, and `git diff 9694a679 -- <path>` showing only `main`'s) | `grep -c -F` of the flag's distinctive words → 1; of `main`'s newest line → 1 | `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` |
| P2 | `DEPLOY-HUB.md` = `main`'s text (`02b`: P7, STEP-T, STEP-C sentences) PLUS the chain's adoption sentences (`02` A3, A4, A7, A8 at `9694a679`), written by Edit so both stand; where a sentence exists in both, `02b`'s words win for P7 / STEP-T / STEP-C and the chain's for STEP-G, P1 (v), LAUNCH, THE RELEASE. Then FOUR SENTENCES, THIS CARD'S TEXT (their origin is the judge's answer to Grok's 02b read; this row is the one source): (5) STEP-G's bullet for exits 5 and 6 (line 102 of the chain's text, two outcomes in one bullet) ends "the release is `gate.sh`'s trap on every exit; verify `<GATE>/.env` gone and the lock dir absent, then the FAILED line"; (6) the equal-tree clause: "ONE branch in `TIP`, `git -C /Users/cobalt/cobalt diff --stat <check code tip> <m1> -- . ":(exclude)docs"` prints nothing, AND the check's stop line carries a with-DB count above 0 → the check's three suite lines are the gate's; otherwise the gate runs whole (`--deploy`)"; (7) P1 (v): "`MIGRATIONS: none` AND an empty derived restart set, provisional at P1; STEP-R re-reads the SET and fails `window (v) does not hold: <labels>` when it is not empty and P1 was outside (i)–(iv)"; (8) the launch line's flag text ends "Inside the outage (4.1–4.6) a blocked call is resent once as single calls; still blocked → STEP-5." | hub text: `grep -n -F` of each distinctive string → one hit; `grep -c -F "MIGRATIONS_DIR / \"00"` → 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |

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
- RESTARTS class homes (L7a): `ops/desk/*` → `OPS_DESK_PREFIX` (operator script, no reader; `restarts.py:38`); `tests/ops/*`, `tests/cobalt/*` → test/documentation (`:239`); `docs/**` → DOCS (`:219`); `src/cobalt/db_migrations/cli.py` → the class `03`'s build report `## RESTARTS` derived for it (quote that line at PREFLIGHT; the build derives again, L42).
- Preflight 10-03 (desk, `03d-card-preflight-2026-10-03.md`): issues 3, 4, 5, 8, 9 answered by the edits above (row P3; P1's red; P2 as the one source; the homes line; HOUSE B).
