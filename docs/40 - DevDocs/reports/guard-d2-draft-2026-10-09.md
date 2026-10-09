# Guard D2 card — draft report · 2026-10-09

## §0 Headline
- Card `prompts/2026-10-09/158-guard-d2-card.md` written: rows T1-T4 red tests (any verb, interpreters, brace/continuation, typed cp/rm of `.env`), C1 control, F1 fix (G3-P in `g3_bash`), K1 eight K25 mutations. One seam: `ops/desk/bare-guard.py` + `tests/ops/test_bare_guard.py`.
- LAUNCH BLOCKER (D7): `RULINGS: 2026-10-08 R707` is a `RECORD` row; `desk-launch.sh:146-148` and `authorize.sh:98` need `HIS RULING` … `APPROVED`. The desk fixes the row or the field before launch.
- REPORT is the worktree path (D6): `desk-launch.sh:901-904` refuses the main-repo path the prompt named.
- Brief line numbers all hold at main `0e84db6f`.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/158-guard-d2-card.md` (uncommitted; the desk commits it).
- Header: `JOB: guard-d2-1009` · `BRANCH: ops/guard-d2-1009` · `WORKTREE: guard-d2-1009` · `BASE: 0e84db6f` · `DB: none` · `RULINGS: 2026-10-08 R707`.

## DECISIONS
- D1 ASK DESK: which tests need the live harness hook rather than a unit test? [11:35 EDT] DEFAULT TAKEN: none. Every test runs `bare-guard.py` as a subprocess with the PreToolUse JSON (`tests/ops/test_bare_guard.py:41-50`, `:250-264`), the same entry the harness calls. The live proof is one deploy-card smoke line on a path that does not exist, so a guard miss prints nothing: `xxd /Users/cobalt/cobalt-wt/.none/.cobalt_key` → refused with the `G3 secret` route.
- D2 ASK DESK: the brief says "whatever its verb", but every hub types `ls`/`ls -la <…>/.env` and both G3 route sentences tell the seat to (`bare-guard.py:58-64`). [11:35 EDT] DEFAULT TAKEN: a segment whose verb is bare `ls` is exempt; `env ls …` is not. Pinned by C1 and mutation K1 (5).
- D3 ASK DESK: `cp /x/repo/.env /x/wt/job/.env` and `rm /x/wt/job/.env` are allowed controls today (`test_bare_guard.py:625-626`), and the hubs list them as allow strings. [11:35 EDT] DEFAULT TAKEN: refused after D2 (row T4); the lock copies and removes `.env` only through its two scripts (`BUILD-HUB.md` 14, 35). The hub allow strings stay unused; no hub edit.
- D4 ASK DESK: any word naming a dotted secret is refused, including a commit message, an `echo`, a grep pattern. [11:35 EDT] DEFAULT TAKEN: accepted, no exemption beyond `ls`; recorded in the card's `## RECORDS`.
- D5 ASK DESK: `ENV_READERS` no longer gates G3; the brief keeps it. [11:35 EDT] DEFAULT TAKEN: the constant stays, with a comment that no rule reads it; the route is picked by `is_env` or a part (b) `env` match.
- D6 ASK DESK: the prompt names REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d2-build-2026-10-09.md`; `desk-launch.sh:901-904` refuses a build REPORT outside `$WT/$wt/docs/40 - DevDocs/reports/`, and `BUILD-HUB.md:103` commits it on the branch. [11:35 EDT] DEFAULT TAKEN: `/Users/cobalt/cobalt-wt/guard-d2-1009/docs/40 - DevDocs/reports/guard-d2-build-2026-10-09.md`, as card 120 did. Neither path exists.
- D7 ASK DESK: `RULINGS: 2026-10-08 R707` as ordered, but `cto-2026-10-08.md:75` R707 ends `| RECORD |` with no `HIS RULING`/`APPROVED`. `desk-launch.sh:146-148` refuses it at launch and `authorize.sh:98` fails it. [11:35 EDT] DEFAULT TAKEN: the card carries R707 as ordered. Before launch, the desk adds an approved row or names one; `cto-2026-10-08.md:39` R686 is `APPROVED · HIS RULING` and covers "secrets stay refused".

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse main` → `0e84db6fdfcd17c32fa888a1e16680e82e6d2a41` (11:32 EDT); `git -C /Users/cobalt/cobalt diff main -- ops/desk/bare-guard.py` → nothing.
- Read whole: `reports/guard-d1-d2-answer-2026-10-09.md`; `ops/desk/bare-guard.py` (1129 lines); `prompts/CARD.md`; `prompts/2026-10-08/119-draft-guard-g2-open-reads.md`; `prompts/2026-10-08/120-guard-g2-open-reads-card.md`; `Memory/topics/writing-rules.md`; `areas/cobalt.md` 19-23, 32-end.
- Read in part: `tests/ops/test_bare_guard.py` 1-70, 215-284, 593-777, 1412-1501 (1575 lines, `wc -l`); the test index by `grep -n "^def \|^[A-Z_0-9]* = \|^@pytest"`; `grep -n -E "\.(env|cobalt_key|cobalt_vault)"` over it: only `:625-626` flip.
- Brief lines proved: `g3_bash` 842-854, `ENV_READERS` 86, unwrapped segs 938, `is_secret` 802, G2 943, segs 935-938, `prod_read` 895-930.
- Hubs type `.env` only with `ls` (`grep -n -o` over the four hubs and `CTO-DESK-WAKEUP.md`; line list in the card's `## RECORDS`); `BUILD-HUB.md:14` lock only through its scripts; `CHECK-HUB.md:77` house text goes into a file, not the typed call.
- `ls` → `ops/run_backup.sh` and `ops/desk/close-timer.sh` exist; worktree `guard-d2-1009`, the card, the build report and this report did not exist (11:32 EDT).
- `grep -n "bare-guard" /Users/cobalt/.claude/settings.json` → `:22` the hook entry, main's file.
- `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` → nothing (11:32 EDT): `bare-guard.py` is an operator script; the test is test; reports DOCS. Expected `RESTARTS: none`.
- `grep -n "R707" reports/cto-2026-10-08.md` → `:75` `| RECORD |`; `:39` R686 `APPROVED · HIS RULING`. `authorize.sh:18-21`, `:98`; `desk-launch.sh:146-148`, `:901-904`.

GUARD D2 CARD DRAFTED · decisions: 7
