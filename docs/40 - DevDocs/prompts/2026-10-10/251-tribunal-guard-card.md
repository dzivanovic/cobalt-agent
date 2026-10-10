JOB: tribunal-guard-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R877
BRANCH: ops/tribunal-guard-1010
WORKTREE: tribunal-guard-1010
BASE: fccbb258
TIP: 2e680273
REPORT: /Users/cobalt/cobalt-wt/tribunal-guard-1010/docs/40 - DevDocs/reports/tribunal-guard-build-2026-10-10.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/tribunal-guard-check-2026-10-10.md
HOUSE B: as needed
DB: none
RULINGS: 2026-10-08 R685

## ROWS

| row | what | red first | files |
|---|---|---|---|
| T | THE TRIBUNAL HUB'S HOUSE CALLS. G9 extends from the check to a tribunal hub (brain direction under L79, R877). Today `LAUNCHERS = ("claude", "codex", "grok", "agy")` (`ops/desk/bare-guard.py:88`); G7 (`:1036-1037`) denies any launcher for a seat whose kind is in `WORKERS` (`:83`); the one house exemption is G9 (`:1034-1035`): `kind == "check"`, the launcher the first and only segment, and the whole command matching `HOUSE` (`:125`); `seat()` (`:731-753`) gives a tribunal hub no kind of its own, so launched from a worktree (`cd /Users/cobalt/cobalt-wt/agy-trial`) it is `worker` (`:748-749`). Change: `seat()` also returns `"tribunal"`, true when the launch prompt (`prompt`, `:736`) matches a design-tribunal hub name under `prompts/20*/`: `(^|/)prompts/20[^/]*/[0-9]+-(?!draft)[a-z0-9-]*-tribunal(-r[0-9]+)?\.md$` (matches `237-f4-tribunal.md`, `2026-09-29/12-f15-tribunal.md`, `17-f15-tribunal-r2.md`, `2026-09-22/63-routing-tribunal.md`; not `236-draft-f4-tribunal.md`, `238-f4-tribunal-opus-seat.md`, `239-f4-tribunal-derive.md`, `249-f4-tribunal-preflight.md`, `13-f15-tribunal-anthropic-seat.md`); the rule at `:1034` reads `kind == "check" or s["tribunal"]` (`s` is in scope, `:1015`, `:1021`). The tribunal hub may run a whole command that opens with a `HOUSE` string and is one segment: `codex exec --skip-git-repo-check -m <m> -s read-only "<probe>"` (237 line 9 types it without a redirect; line 43 with ` < /dev/null`), `grok --version`, `agy --version`, and the launch shapes of 237 `## 2` (`grok -m … --sandbox … -p "…"`, `agy --model … --print="…"`). Every other launcher (`claude` above all, and a house string behind a pipe, a prefix, a wrapper or an absolute path) stays G7-denied; G1-G6 apply unchanged. No new permission class (L67 seats the houses on every design tribunal; the strings are `CHECK-HUB.md` line 10's, `HOUSE` unchanged). Backed by DESK RECORD R877. | In `tests/ops/test_bare_guard.py`, next to the G9 block (`:1221-1273`), a helper `tribunal_seat(roots, name="237-f4-tribunal.md")` = `make_seat(roots, None, cwd=roots.wt / "agy-trial", first=f"Read '{prompts(roots) / '2026-01-01' / name}' and follow it exactly.")`. (1) `test_g9_a_tribunal_hub_types_each_house_string`, parametrized over `HOUSE_CALLS` (`:1223`) plus `grok -m grok-4.7 --sandbox cobalt-job -p "x"`, `agy --model m --mode accept-edits --sandbox --print-timeout 20m --print="x"` and `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` (no redirect): `assert_allowed(run(command, tribunal_seat(roots)))`. RED on `BASE`: exit 2 with `route: the desk launches` (the call is G7, kind `worker`). (2) `test_g9_a_tribunal_hub_stays_denied_every_other_launch`, parametrized over `CHECK_LAUNCHES_DENIED` (`:1240`; it holds `claude --bg "Read x"`, `claude -p x`, the prefixed, absolute-path and piped shapes): `assert_denied(…, G7_ROUTE)`; GREEN on `BASE`, pins the fence. (3) `test_g9_a_build_seat_is_still_denied_the_tribunal_shapes`: `build`, `devfix`, `deploy`, each denied `grok --version`, `agy --version`, the astra probe, `claude --bg "Read x"` with `G7_ROUTE`; GREEN on `BASE` (the existing `:1265-1273` already pins three kinds; this adds the two shapes). (4) `test_g9_a_non_hub_tribunal_prompt_is_denied`, parametrized over the names `236-draft-f4-tribunal.md`, `238-f4-tribunal-opus-seat.md`, `239-f4-tribunal-derive.md`, `249-f4-tribunal-preflight.md`, `242-x29-card.md`, all with `grok --version`: `G7_ROUTE`; GREEN on `BASE`. (5) `test_g9_a_tribunal_hub_is_denied_what_g1_to_g6_deny`: from `tribunal_seat`, `grok --version && ls` is denied with G1's resend line (assert the block text G1 gives for `&&`, as `:88-96` does) and `git push` is denied `G4_ROUTE`; the `&&` case is RED on `BASE` (a `worker` seat meets G7 at `:1036` before G1 at `:1038`, so the denial is `route: the desk launches`, G7 hides G1) and green after; `git push` is GREEN on both. Only (1) and the `&&` case of (5) are red on `BASE`; the whole file runs green after the change. | `ops/desk/bare-guard.py` (`seat()` the one field, `:1034` the one condition, the header comment `:22-23` the G9 clause), `tests/ops/test_bare_guard.py` |

## NOT IN THIS JOB
- A new permission class, a change to `HOUSE` (`:125`) or `LAUNCHERS` (`:88`), a second house string, a wider `codex` shape; the 14 allow strings of 237's launch line stand.
- Any rule but G9's condition (G1-G8, G10, G11 as they are); any other file under `ops/` or `.claude/`; `ops/desk/stop-guard.py`.
- FOLLOW-UP ROW, not built: `seat()` classifies ANY prompt seat launched in the repo with a `prompts/20*/` prompt as `brain` (`:746-747`, `elif in_repo and re.search(r"(^|/)prompts/20[^/]*/[^/]+\.md$", prompt)`), and the brain kind is outside `WORKERS` (`:83`), so G7 does not apply to it; that wider gap is a row for the next guard card.
- The relaunch of `237-f4-tribunal.md`: the desk's, after the deploy.

## READ
- `ops/desk/bare-guard.py` at `BASE`: `:83` `WORKERS`, `:88` `LAUNCHERS`, `:124-125` the G9 comment and `HOUSE`, `:731-753` `seat()`, `:1015-1041` `bash_rules` (G7 at `:1033-1037`).
- `tests/ops/test_bare_guard.py`: fixtures `roots` `:28`, `make_seat` `:223`, `call`/`run` `:250-264`, the G7 block `:1187-1218`, the G9 block `:1221-1273`.
- `docs/40 - DevDocs/prompts/2026-10-10/237-f4-tribunal.md`: line 1 (launch line and its cwd), line 9 (the probe shapes), `## 2` lines 39-43 (the house launch shapes).
- `docs/40 - DevDocs/prompts/CHECK-HUB.md` line 10 (the three house strings).
- `docs/40 - DevDocs/reports/cto-2026-10-10.md` R877; `docs/40 - DevDocs/reports/f4-tribunal-2026-10-10.md` (the denial).

## CHECK ASKS
- X1 tribunal-guard brain 10-10 — F4 hub denied by bare-guard G7 because seat() gives a tribunal hub kind worker and G9 exempts only the check; fix = G9 extends to design-tribunal prompts for HOUSE strings and the listed probe shapes, claude still denied; no new permission class (L67, CHECK-HUB line 10 strings); seat() 'brain' for any prompts/20* seat is a follow-up row; relaunch 237 as-is after the deploy.
- X2 Does the tribunal name pattern match every real hub name under `prompts/20*/` and none of a drafter, an Opus seat, a derive or a preflight prompt (list the directory and run the pattern over it)?
- X3 Does any command a tribunal hub is denied today and may now run reach beyond the `HOUSE` prefixes with the launcher the first and only segment (a pipe, a wrapper, `FOO=1`, an absolute path, a second launcher)?
- X4 Test (3) repeats existing `:1265-1268` for `grok --version` and `agy --version`; confirm the new coverage is the astra shape and `claude --bg "Read x"` for build, devfix and deploy.
- X5 The name pattern misses older hub names (`2026-09-19/08-tribunal-archiver*.md`, `2026-09-21/27-setups-tribunal-r1b.md`, `41-reissue-handicap-tribunal-q17.md`); confirm no live hub is among them (F4 and later follow the `-rN` shape).
- X6 A tribunal hub may type any option after `grok `, `agy ` or the `codex exec … -s read-only ` prefix, as the check may; confirm the fence is the launch line's `--allowedTools` and the sandbox, not this guard.

## RECORDS
- Each read below is `git -C /Users/cobalt/cobalt show d0a5fbb8:ops/desk/bare-guard.py`, 2026-10-10: `:83` `WORKERS`; `:88` `LAUNCHERS`; `:124-125` G9 comment and `HOUSE`; `:731-753` `seat()` (the row's `:731-751` ends two lines short; `return` is `:753`); `:746-747` the `brain` branch; `:748-749` the `worker` branch; `:1015-1041` `bash_rules`; `:1033` `launches`; `:1034-1035` G9; `:1036-1037` G7. Every number matched the direction except `seat()`'s end.
- `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- ops/desk/bare-guard.py tests/ops/test_bare_guard.py` printed nothing: the working files equal `d0a5fbb8`'s.
- 237 records the probe and launch strings as the row does; the astra probe (line 9) has no ` < /dev/null`, the astra launch (line 43) has it; `HOUSE` matches both and G1 passes a lone command.
- RESTARTS: `uv run cobalt jobs restarts <BASE>..HEAD`, expected none; UNPROVEN at drafting (no `uv` in the drafter's allow list), the build hub runs it.
