# Card 547 `db-copy-1014` — preflight (2026-10-14, read-only)

Card `prompts/2026-10-14/547-db-copy-card.md`, committed in `73d6ae07` (the HEAD read). Every anchor below was read on that HEAD. The card's own `0ffb6949` is stale, but `git diff --stat 0ffb6949 HEAD` over `ops/desk`, `tests/ops`, `BUILD-HUB.md` and `src/cobalt/env.py` printed nothing, so its lines hold.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <card>`; `git log --oneline -1 -- <card>` | diff empty; last commit `73d6ae07` | OK |
| 2 | header against `CARD.md` | JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS all present. `CLASS: K5`, `INSTALL: none` and `RESTARTS: none` are not in the CARD.md key table, but cards 521, 523, 537 and 546 carry the same set. No `«FILL`; the only empty values are BASE and TIP | OK (NOTE 1) |
| 3 | `gate.sh` anchors on HEAD | `:30-37` THE LOCK, `:37` `# proves .env gone.`, `:194` PASS1_DEPLOY, `:255` held_env, `:267` take, `:288` ours-alone, `:291` release, `:352` cleanup, `:375` proof_clean, `:397` do_offline, `:422` do_withdb, `:182` OFFLINE=, `on cobalt_dev` case in proof_clean. The first reader block ends at `:180` (card: `:181`); `release \|\| exit 1` is at `:494` (card: `:493-ish`) | OK |
| 4 | `desk-launch.sh` anchors | `lock_free` `:1082-1089` with the refuse at `:1087`; `lock_dir_free` `:1091-1098`; `:2119` gate `.env` nogo | OK |
| 5 | `gate-lists.md` anchors | header paragraph `:3-8` ends `byte-equal (tests/ops/test_gate.py).`; `## LEVEL` paragraph `:10`; sections `## OFFLINE`..`## LEVEL 0013` at `:17-47`; no `## COPY` section | OK |
| 6 | `BUILD-HUB.md:83` | the `- (b) THE LOCK` line, text as quoted, `LEVEL 0013` once | OK |
| 7 | lock scripts, test and env anchors | `take-devdb-lock.sh` mkdir/owner/cp at `:47-49`, retry at `:58-60`; `release-devdb-lock.sh` guards `:20-33`, removal `:49-55`; `test_devdb_lock.py` roots `:39`, run `:51`, desk `:201`, hold_the_lock `:267`, launch `:273`, resume test `:290`; `test_hub_lines.py` hub_line `:54`; `env.py` `resolve_db_name` `:78`, `assert_destructive_target` `:88`. Each is within a line or two of the card's range | OK |
| 8 | `LAWS.md` L76 `:384`, L81 `:403-405` (K5 text) | present; K5 = allow strings, guard rules, launcher refusals, hub lines | OK |
| 9 | red reasons, rows E1, G1, L1, D1, H1 | each names its BASE failure: script absent (exit 127), no `dev-copy` call, `lock is held` refusal, header lacks the sections, no `## COPY CREATE` line. Negative controls (3), (10), (13), (15), (17) are named GREEN on BASE | OK |
| 10 | whole-file, whole-line or BASE-literal pins (brain R1472) | every new test reads its own lines by content. No `git show`, no hash, no whole-file compare in tests (1)-(17) | OK (NOTE 2) |
| 11 | `tests/ops/test_build_hub_no_clutter.py:15` `BASE = "5e5fab02"` and `:57` `test_no_other_line_changes_from_base` | this test holds the whole `BUILD-HUB.md` equal to `5e5fab02`, minus the no-clutter pair. Row H1 edits `BUILD-HUB.md:83`, so it goes RED. The card's `files` cells and its `uv run pytest` line do not name this file | FAIL |
| 12 | test (15)'s selector `tests/ops/test_gate.py::test_*lists*` | not a valid pytest id (no globs). The "existing pins of `list_commands()`, `:99-157`" are helpers (`list_commands` `:106`, `hub_commands` `:124`), not tests. Tests that read the lists file are `test_the_hub_holds_no_gate_command_and_points_at_the_lists_file` `:256` and `test_withdb_green_runs_the_lists_commands_byte_for_byte_in_order` `:234` | FAIL |
| 13 | launch-line command strings (R411, R412), LAWS and RULING 7 | no `claude --bg` line, allow string or `.claude/settings.json` touched. The new script runs under the existing `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` (`BUILD-HUB.md:12`). Neither LAWS nor RULING 7 is named in a `files` cell | OK |
| 14 | RESTARTS class home (K10), `src/cobalt/jobs/restarts.py` | `ops/desk/` → "operator script; no Cobalt reader" (`:38`, `:230-234`); `docs/` → `DOCS` (`:225-228`); `tests/` (`:245`). `RESTARTS: none` holds | OK |
| 15 | overlap with 521, 523, 537, 546, 548, 549, 550 (their cards read) | 521: `gate.sh` `:2,:72,:86-112,:156-159,:182,:397-400`, lists after `:18`, `BUILD-HUB.md:80,:82`; 523: `BUILD-HUB.md:105,:112`; 537: `DEPLOY-HUB.md`, `STANDING-LIST.md`, `test_hub_lines.py:102-108`; 546: `DEPLOY-HUB.md`, `pre-commit`, new scripts; 548: `desk-launch.sh:1450-1489`, `BUILD-HUB.md:109`, `test_build_hub_no_clutter.py:57-60`; 549: `CTO-DESK-WAKEUP.md`, `STANDING-LIST.md`; 550: `CARD.md`. None touches `gate.sh` after `:194`, `desk-launch.sh:1082-1089`, `gate-lists.md:8-10` or `BUILD-HUB.md:83`. Nearest: `gate.sh:182` of 521 versus the block after `:194` | OK (NOTE 3) |

## ISSUES

- FAIL (check 11): row H1 turns `tests/ops/test_build_hub_no_clutter.py::test_no_other_line_changes_from_base` RED, because the test holds the whole `BUILD-HUB.md` equal to `5e5fab02`. The card repairs nothing and its final run omits the file. Cards 523 (H3 (3)) and 548 (RF2) both own the same repair. Amend one of two ways: (a) add that test (the `:57-60` body) to H1's `files` with the by-content ordered-subsequence repair and add the file to the final `uv run pytest` line, or (b) order 547 after 523 or 548 on the same test and say so.
- FAIL (check 12): test (15) names `tests/ops/test_gate.py::test_*lists*`, which is not runnable, and the `:99-157` pins are helpers. Name the real tests, or run `tests/ops/test_gate.py` whole with `0 failed`.
- NOTE 1: a build card should hold `CHECK REPORT` and `HOUSE B` empty per `CARD.md`, and the desk fills them. The card pre-fills both, as 521, 537 and 546 do. Harmless, same precedent.
- NOTE 2: negative control (10) says "the verdict lines equal the stub run's today". Spell the expected lines (`offline`, `with-DB <n>/0`, `cobalt_dev: <level> — F2 = F0`, `.env: removed`, `log:`) instead of "today", so the test cannot become a BASE compare.
- NOTE 3: card 521 changes the lists file and `test_gate.py`; both of this card's `test_gate.py` reads are by content, so they hold on either order.
- NOTE 4: the deploy is blocked by one-deploy-at-a-time, with 537 first (and 521/523 if not yet merged). Its set changes `gate.sh`, so L-GATE EARLY (`LAWS.md:358`) runs the gate on the merged hub text first.
- NOTE 5: G1 (e) cites `release || exit 1` as `:493-ish`; it is `:494`. The builder re-reads (E3). Drift of one line, no effect.
- NOTE 6: X1 holds only if the real lists file stays free of `## COPY`, which row D1 keeps. The card's own `grep -c` proofs (`## COPY CREATE` count 1 in the lists file) therefore count the header paragraph, as `## DEPLOY PROOF` says.

PREFLIGHT DONE · card: db-copy-1014 · checks: 15 · fails: 2 · ready: NO
