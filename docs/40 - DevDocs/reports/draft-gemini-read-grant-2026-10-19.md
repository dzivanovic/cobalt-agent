# Draft — gemini-read-grant-1019 (prompt 826)

## §0 Headline
- Card written: `docs/40 - DevDocs/prompts/2026-10-19/827-gemini-read-grant-card.md`, BASE `c2ee3cff`, BAND HIGH, rows P0, R1-R4, H1, P1. Uncommitted.
- STEP 1 list: `read_file` only. agy grants by rule family; the one read family is `read_file` (`automation/SKILL.md:229-239`); the logs never name a list, glob or search tool.
- Design: the launcher adds `read_file(<WT>/<wt>/)` beside `write_file(<WT>/<wt>/)` in the same write and removes the two together (trap, orphan step, `grant-sweep`). A hand-added `read_file` rule with no write rule is never touched.
- Risk to the desk before 717's last try: DECISIONS 3.

## DECISIONS
1. ASK DESK: no agy list, glob or search tool and no rule family for one is proved on this machine. The docs name the families `command`, `read_file`, `write_file`, `mcp`, `read_url` and `execute_url`. The logs name only the tools `ViewFile`, `RunCommand` and `ReadUrlContent`. Default taken: grant `read_file` only. Check ask X7 records it. [2026-10-19 08:20 EDT]
2. ASK DESK: the job's own `read_file(<WT>/<wt>/)` present without its `write_file` rule. Default taken: refuse and write nothing, because adopting the rule would let a later sweep delete a hand-added rule. This changes the fixture of `test_k5_gemini_without_its_worktree_grant_is_added` (named in R1). [2026-10-19 08:20 EDT]
3. ASK DESK: the read rule may not make X1 clean. The tool denied in leg 0a is logged as `ViewFile` with no target (`cli-20261019_080830.log:193`), so whether it was the worktree read or a decoy read is UNPROVEN. In both legs headless agy ended the whole run at the first denied tool. X1's steps include decoy reads and a fetch that must be refused, so with the read rule in place the run likely still ends at the decoy read, before `X1 WRITE OK`. That would be the third failure and would stop the arm (R2005). Default taken: draft the card as R2005 directs. Before the one 717 relaunch, the desk decides whether X1 is split into one agy launch per step (option (b) of 717's DECISIONS 1). [2026-10-19 08:20 EDT]

## RECORDS
- 08:14 EDT `date`; read `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `prompts/CARD.md`, `prompts/2026-10-18/800-gemini-grant-card.md`.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `c2ee3cff`.
- `grep -n "gemini-read-grant" reports/cto-2026-10-19.md` → `:16` R2005 DESK RECORD and `:65` OWED.
- `tail -40` of 717's build report (worktree `strike-fallback-env-1018-gemini`): `FAILED: X1 … auto-denied read_file (leg 0a) and read_url (leg 0b)`.
- `agy --help`: no permission keys; the only permission flag is `--dangerously-skip-permissions`.
- Settings file read with `grep -n -v -i -E "key|token|secret|password|auth"`: all 33 lines printed, none held back, and nothing was written. `:5` `"allow": [`, `:6` 717's write rule, `:7-8` hand-added `read_file` rules, no `read_url` or `execute_url` rule.
- `ls -R ~/.gemini`; Grep of `builtin/skills` (`automation/SKILL.md:140-148`, `:229-239`; `antigravity_guide/references/app.md:51-56`; `agy-customizations/docs/hooks.md:115`).
- `grep` of the agy logs: soft-denied names `ViewFile`, `RunCommand` and `ReadUrlContent` only; leg 0a at `cli-20261019_080830.log:193`, leg 0b at `cli.log:226`.
- `git show main:ops/desk/desk-launch.sh` (AGY_PY `:237-382`, `grant-sweep` `:1121-1151`, gemini block `:1947-1991`, dry plan `:2599-2619`, real path and trap `:2665-2695`) and `git show main:…/SHADOW-HUB.md` (`:12`, `:28`). `git diff main` on the four files printed nothing.
- `tests/ops/test_desk_launch_shadow.py` and `tests/ops/test_shadow_hub_file.py` read at their grant blocks.
- A grep of the repo (`ops`, `tests`, `src`, `configs`, hubs) finds `write_file(` only in the launcher, its two test files and `SHADOW-HUB.md`.
- Before counts for DEPLOY PROOF: `without its write rule` 0 and `read_file(` 0 in the launcher; in the hub, `write implies read inside that directory` 1 and `read_file(/Users/cobalt/cobalt-wt/<worktree>/)` 0.
- 08:19:15 EDT card written; 08:20:55 EDT report written. No commit, no launch, no write outside the two files.

DRAFTED · decisions: 3
