# Draft: F5 gate pass 4 (prompt 970) — 2026-10-22

## §0 Headline
`## FOURTH PASS (only on the desk's CONTINUE-4)` is in `prompts/2026-10-21/970-f5-gate-run.md` after `## THIRD PASS`: pass 3's lock, note, migrate, rollback and release reused by reference, X6, then X4.
The LAUNCH MODE line now reads `desk, 2026-10-22, the CONTINUE-4 launch`: run only `## FOURTH PASS`. The MODEL line is unchanged. Nothing was committed.

## DECISIONS
- X4 touches no database: `checkpoint_probe.py` on `main` runs it in a `f5-probe-` scratch with "no store (no database)", 20 model calls, no gate check, no Finviz GET. It needs no lock and no migrate. The section runs it in every path, after X6.
- X4 reads its Groups body from disk: the row (b) fixture `groups_sector_v140_real.csv` is not in `tests/cobalt/fixtures/checkpoints/` (only `groups_sector_v140.csv` is), so it needs X6's kept capture. X6 must run first. If X6 does not keep a file, X4 reads `NOT RUN — no real Groups body`.
- No `--allowedTools` string added: every string the new steps need (`checkpoint probe X4`, `probe X6 --keep-groups …`, the `db` and lock strings, `--add-dir` for the dev vault) is already on the MODEL line. The line has `Write` but not `Edit`, so "in place" edits of the report are a Write rewrite, as in passes 2 and 3.
- X2 is not rerun: pass 3 left it `OK`, and the brain direction names X6 and X4 only. Without an X2 run before X6, the one-minute gap of pass 3 step 6b is dropped (X6's gate check is then the first Finviz request of the pass).
- Pass 3's note `2026-10-21.md` is still in the dev vault (`ls` confirms). X6 checks today's note, so pass 4 writes `2026-10-22.md`. Both paths are named as owed to the desk. ASK DESK: remove `2026-10-21.md` before launch? Default: it stays, untouched. [03:26]

## RECORDS
- Read, all of it: `prompts/2026-10-21/970-f5-gate-run.md`; `reports/f5-gate-run-2026-10-21.md`; `reports/draft-f5-gate-pass3-2026-10-21.md`; `F5-FINAL-2026-10-11.md:170-189`; `reports/f5-probe-x4-fix-check-2026-10-21.md`; `git show main:src/cobalt/prefill/checkpoint_probe.py`.
- Not found: `reports/draft-f5-probe-x4-fix-2026-10-21.md` does not exist (read failed). The check report and the code covered what X4 runs.
- Proved against `main` (`d057d99a`): `checkpoint probe` with `X4`, `X6`, `X13` and `--keep-groups PATH` (`checkpoints.py:849`, `:860-863`, `:846`); the keep root and its refusals (`checkpoint_probe.py` `_keep_target`); X4's Groups sources (`X4_GROUPS_FIXTURE`, `X4_GROUPS_KEPT`). `ls` shows `.f5-probe/PLACEHOLDER` only and no `2026-10-22.md` note.
- Pass 3's line numbers and strings were reused by reference, not re-proved against code beyond the above.
- Brain line: `F5 gate pass 4 = X6 + X4 (989 deployed), drafter-written FOURTH PASS + LAUNCH MODE — brain 9b07db5a 2026-10-22`
- Times from `date`: 03:25:57 and 03:26:41 EDT. Nothing run against the DB, Finviz or the vault; no git write, no launch.

DRAFTED · decisions: 5
