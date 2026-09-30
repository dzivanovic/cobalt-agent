# S2 smoke look re-point — drafter report 2026-09-28

## §0
- Wrote `prompts/2026-09-28/60-s2-smoke-look.md` (14,850 B) from `34`; authorization verified 21:38 ET (09-27 R32, 09-28 R167).
- Deploy `3349466f` (`deploy-2026-09-27`); both step-2 literals still on the tree.
- Placeholder `R__` present once, in AUTHORIZATION only; the desk fills it before launch.
- New rule strings: 0. ESCALATE: 1.

## FACTS
- Authorization: `grep -n -F "| R32 |" cto-2026-09-27.md` → line 40 ("yes A"); `grep -n -F "| R167 |" cto-2026-09-28.md` → line 176, names `59-draft-s2-smoke-look-repoint.md`.
- Deploy prompt: `grep -n -F "50-stacked-deploy-r3.md" cto-2026-09-27.md` → R7 (also R11); cited in `60`.
- Tag: `git log --oneline -1 deploy-2026-09-27` → `3349466f Merge branch 'main' into deploy/stacked-0925`.
- `git show deploy-2026-09-27:src/cobalt/radar/evaluate.py | grep -n -F "def prepare_member"` → `950`; same for `EVALUATOR_VERSION = "s2p2.3"` → `163`; `grep -n -F` on the file at main → `950` / `163`. Both literals carried.
- Deploy report last non-blank line: `STACKED DEPLOY DONE 3349466f · tag deploy-2026-09-27 · branches: 4 · migrations: 0014 0015 0017 · residents down 220 s · /radar 200 · rollback: not used · ESCALATE: 14`.
- Cutoff: `git log -1 --format=%cI deploy-2026-09-19b` → `2026-09-19T15:11:42-04:00` (carried).
- Plist: Weekday 1–5 at 21:10 (`grep -n -E "Weekday|Hour|Minute"`).
- Step 8 literals in `deploy-2026-09-27.md`: `stored membership` — 0 hits; `proximity IS NULL` — lines 276, 380, 486; `voice/status` — lines 303, 473; `V1 STT: model not fetched` — line 500. The report carries `H1 dry-run UNPROVEN` at line 304 (§0 relaunch).
- `wc -c 60-s2-smoke-look.md` → 14850; `grep -c -F "R__"` → 1.

## CHANGES
- L1 · MODEL tag `claude-sonnet-5` → `claude-sonnet-5-5`; header `RE-POINTED 2026-09-28 …` added after the tag · item 7, 9.
- L1 · seat, remote-control and name → `s2-smoke-look-0928` (+ `--name`); prompt path → `60` · item 7.
- L1 · parenthetical now names `34` as the source (itself the re-issue of `46`) · item 1.
- L3 · heading, night, deploy prompt / report → 09-27; added "no replay fired after the deploy before tonight (R31)" · items 1–3.
- L5 · AUTHORIZATION: R43 checks and placeholder gate carried on `60`'s path; ADDED 09-27 R32 grep; launch row → `cto-2026-09-28.md` (grep + `git log -S`) · item 8.
- L7 (5) · plist card adds the Weekday 1–5 / 21:10 fact · item 3.
- L7 (6) · 09-24 stays "the last look that ran"; 09-25 replay FAILED line added as the last replay before tonight · item 4.
- L7 (7) · verbatim `## FOR THE DEPLOY` quote untouched; desk's bracket names 09-28 · item 3.
- L7 (8) · DRC note → `DRC-2026-09-28.md` · item 1.
- Steps 1–5, 7, report path, stop-line shape: dates 09-25 → 09-28; step 2 tag `deploy-2026-09-27`, expected sha `3349466f`; step 7 column "last look (09-24)" · items 1, 2.
- Step 8: greps → `deploy-2026-09-27.md`; wording unchanged · item 6.
- Remaining `09-25` mentions (7) are the R47 citation, the R31 line, the verbatim quote and its bracket, and the `34` path.

## RULE PROOF
- `sed -n 1p` of each, quoted tokens sorted, `diff`: one difference — the prompt path (`34` → `60`). The eight rule strings and the `--add-dir` tokens are byte-identical.
- Unquoted differences: model id `claude-sonnet-5` → `claude-sonnet-5-5`; `--remote-control s2-smoke-look-0925` → `s2-smoke-look-0928`; `--name s2-smoke-look-0928` added.

NEW strings: 0.

## ESCALATE
1. ASK DESK: step 8 (a) greps `stored membership`, which `deploy-2026-09-27.md` does not carry, so `60` reads `NOT RECORDED BY THE DEPLOY`. The report does carry `H1 dry-run UNPROVEN (no 2026-09-27 cache, Sunday)` at :304, and `34` says "or its `UNPROVEN` line". Reading A: literal absent → `NOT RECORDED BY THE DEPLOY`. Reading B: quote line 304 as the UNPROVEN line. Safe default taken: A (source `34`, the grep unchanged). The hub may still find :304 by reading the report's §0; the desk can add a second grep on `H1 dry-run UNPROVEN` at launch. [asked 21:40 ET]

Items with `NOT RECORDED BY THE DEPLOY` per step 6: (a) only; (b) and (c) are recorded.

## CONTINUE
- Desk: replace the `R__` token in `60`'s AUTHORIZATION with the launch row number in `cto-2026-09-28.md`, commit that file, then run the two bare commands in `60` line 1 (`cd /Users/cobalt/cobalt`, then `claude --bg …`). Window 21:40–23:30 ET.
- Commit `60` and this report (pathspec).

S2 SMOKE LOOK REPOINTED · file: 60-s2-smoke-look.md · deploy: 3349466f · new rule strings: 0 · ESCALATE: 1
