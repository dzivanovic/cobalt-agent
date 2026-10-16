# Card 648 `check-scratch-1016` (CHECK, K5) — preflight, 2026-10-16 13:02 EDT (`date`)

Read only. Card `prompts/2026-10-16/648-check-scratch-check-card.md`. BASE `b84cca9a` and TIP `85eade55` are the desk's: named, not failed (`git rev-parse --short=8` of each prints the same 8 hex). Branch head `0605334f`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card header vs `CARD.md` check column | JOB, LADDER (`OFF-LADDER — reports/cto-2026-10-15.md R1532`), BRANCH, WORKTREE, BASE, TIP, REPORT (inside the worktree), CHECK REPORT (under `reports/`), HOUSE B (`as needed`), RULINGS, DB (`none`) all present and valid for a check. Extra keys `CLASS: K5`, `INSTALL: none`, `HOUSE A: grok`, `BAND: MID`, `RESTARTS: none` match card 638's form (`grep -n -E "^(HOUSE A\|HOUSE B\|BAND\|CLASS\|INSTALL\|RESTARTS):"` on 638 → same five) | OK |
| 2 | Read `## ROWS` | CS-1 (RUN, RED on BASE's lines, control `test_cs1_control_no_prior_card_copy_is_refused`: exit 1, no `cleared:`, `snapshot` equal) and R2 (RUN, `uv run cobalt jobs restarts b84cca9a..85eade55`, table and `RESTARTS:` line quoted). R2's red/control cell is `none` (it asserts nothing) | OK (see NOTE 2) |
| 3 | Read row SC1 | asks whether the script removes only `$dest`: dest gate `:50-54`, `:97`, two `rm -rf`, no `git clean`/`-delete`, a second job's folder left equal, what the script cannot prove | OK |
| 4 | `grep -n -E "«FIL[L]\|«INSTAL[L]\|TBD\|TODO\|XXX"` on the card | no output | OK |
| 5 | `grep -n -i -F "opus"` on the card | no output. The card names `HOUSE A: grok` and "Both outside houses run inside this check" but never names the Opus check seat. Card 638 does (`the Opus seat is the check (the brain's condition 1)`, and X7) | FAIL |
| 6 | `grep -n -F -e "deploy-gate" -e "--deploy" ops/desk/gate.sh` | `:2` usage, `:29` `--deploy-gate (offline, all …)`, `:136` option parsed, `:147` `--deploy-gate belongs to offline and all`. Row G1's `gate.sh check-scratch-1016 offline --deploy-gate` is a valid call | OK |
| 7 | `grep -n "^| R1532 " reports/cto-2026-10-15.md` | `102:| R1532 | 07:00 ET | HIS RULING · APPROVED: routing B … | APPLIED: LAWS.md L27, L29 at 07:02 |`. `RULINGS` holds this one row only, with `HIS RULING` and `APPROVED` | OK |
| 8 | `git -C … grep -n -F "def test_cs1_" ops/check-scratch-1016 -- tests/ops/test_stage_set.py` | `:359 :419 :423 :427 :431 :435 :439`, seven, as CS-1 names them | OK |
| 9 | `git -C … grep -n -F "assert done.returncode == 0" ops/check-scratch-1016 -- tests/ops/test_stage_set.py` | `:102 :213 :244 :364`; `:364` is the line CS-1 names | OK |
| 10 | `git -C … grep -n -F "clearable" ops/check-scratch-1016 -- ops/desk/stage-set.sh` | `:90` comment, `:92` definition, `:130` the one call. The card says `:130` (the build report says `:128`; the card names the 2-line shift) | OK |
| 11 | `git -C … grep -n -F "rm -r" ops/check-scratch-1016 -- ops/desk/stage-set.sh` and `grep -c -F "more than one prior card copy"` | `:151 rm -rf "$dest"`, `:158 rm -rf -- "$dest"`; count `1`. Card: `:151`, `:158`, `1` | OK |
| 12 | `git -C … show ops/check-scratch-1016:ops/desk/stage-set.sh` (Read of the worktree copy for numbers) | sampled against the tip, all match the card: `:50-54` dest gate; `:95-107` earlier tests; `:108` `copied=""`; `:109` guarded `find … -name '*-card.md'`; `:110` `no prior card copy`; `:111` `more than one prior card copy`; `:112` hash-object; `:113-114` `find-object … "docs/40 - DevDocs/prompts"`; `:115` JOB test; `:116-122` report tests; `:123` own-report test; `:126-137` caller; `:157` `cleared:` print; `:8` header sentence. 14 `file:line` sampled | OK |
| 13 | `git log -1 --format=%h -- <card>`; `git diff --stat HEAD -- <card>` | `1a093e2d` (equal to `main` HEAD `1a093e2d`); diff against HEAD prints nothing. Card is committed and unchanged (as found) | OK |
| 14 | `git diff --stat 85eade55 0605334f -- . ":(exclude)docs"`; `git diff --name-only --no-renames b84cca9a 85eade55`; `git log --oneline b84cca9a..85eade55` | first prints nothing; second `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`; third `85eade55`, `3f0fd60e` (two commits). Row S0 and H1 expectations hold | OK |
| 15 | `grep -n -E -e "git show" -e "agy-trial" -e "/Users/" tests/ops/test_stage_set.py` (tip) | hits `:3 :4 :55 :85 :129 :138 :141`, all in docstring and `job`/older tests, none in `:344-440`; no `git show` call. Row X4 expectation holds | OK |
| 16 | `ls -la …/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check` | `No such file or directory`: no prior folder, so `desk-launch.sh check` meets nothing to clear | OK |

## ISSUES
- FAIL 5: the card never names the Opus check seat (`grep -i opus` prints nothing). Add to `WHY` or `## CHECK ASKS` X7 the line card 638 carries: "the Opus seat is the check (the brain's condition 1)". Houses: `HOUSE A: grok` named; `HOUSE B: as needed` is card 638's value, and under `CHECK-HUB.md` `## 1` that records house B `none` unless the card says `mandatory`; the card's text "Both outside houses run" and that header disagree, so name Gemini as house B or say "house B only if the hub seats it".
- NOTE 2: R2 has `none` in its red-first cell (it is a RUN that asserts nothing); the prompt's "RED and control" applies to CS-1 only.
- NOTE 3: nothing blocks `desk-launch.sh check "<card>"` that I could read: the card is committed and unchanged (`desk-launch.sh:1058-1060`), no `«FILL`, the scratch folder is absent. Not checked here: worktree tree clean and no other Grok hub running (L15); `band-routing-1015-check` shows mtime Oct 16 11:56, so confirm that check has ended before launch.
- NOTE 4: `CARD.md` on `main` carries no `BAND` row (card RECORDS say so); `BAND: MID` is harmless until band-routing deploys.
- NOTE 5: no test was run and no mutation tried; the greens and reds in the rows stay the builder's, UNPROVEN until the check quotes them (L70).

PREFLIGHT DONE · card: check-scratch-1016-check · checks: 16 · fails: 1 · ready: NO
