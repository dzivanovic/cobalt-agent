## §0 Headline
- Card `prompts/2026-10-10/284-kill-hub-card.md` written, uncommitted: JOB `kill-hub-row-1010`, branch `ops/kill-hub-row-1010`, worktree `kill-hub-row-1010`, `DB: none`, BASE `6fe8d690`, RESTARTS none (docs only).
- Three rows: K1 `DEPLOY-HUB.md:137` (4.2), K2 `:162` (STEP-5 (3)), K3 one new `STANDING-LIST.md` line after `:148`. Each carries the exact OLD and NEW line; all five blocks match `BASE` and the label-fixed text byte for byte.
- Merge fenced: BUILT and CHECK stop at the branch tip, no merge until his yes. The check's Grok read is the L67 read. No prompt is renamed.

## DECISIONS
- ASK DESK: RULINGS is `2026-10-10 R855` (his ruling for orphan-clean, the same as card 229). R926 and R927 are brain records, not `HIS RULING` rows, so `authorize.sh` could not prove them. [15:20] Default: R855. Replace it if his yes on the row gets its own row before the build.
- ASK DESK: the prompt lists BASE among the desk's values, but the rows must be proven against it, so BASE is `6fe8d690` (main HEAD at drafting). Neither file has changed since `7bc283fe`. [15:20] Default: kept. If the desk recuts BASE, the anchors hold while `git diff --stat <new> 6fe8d690 -- <both files>` prints nothing.

## RECORDS
- `git -C /Users/cobalt/cobalt log --oneline -1` → `6fe8d690 docs(desk): X29 deploy card 285, tip 3c00e204`. `git -C /Users/cobalt/cobalt diff --stat HEAD -- <both files>` printed nothing. `git log -3 -- <both files>` → newest is `7bc283fe` (M6, R839).
- `wc -l` at BASE: `DEPLOY-HUB.md` 181, `STANDING-LIST.md` 220. Staged after-copies: 181 and 221.
- Line reads at BASE (Read tool on files equal to HEAD): `:137` = 4.2, `:162` = STEP-5 (3), `STANDING-LIST.md:148` = the `launchctl print` row, `:149` = the `cobalt.sh status` row.
- The working tree was restored, so the new text was taken from the Grok re-read's staged copies, `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-row/`. Against main, `git -C /Users/cobalt/cobalt diff --no-index` shows exactly the 4.2 hunk, the STEP-5 (3) hunk and the one new row. They carry `--kill aset` and "the same pid set", with no DRAFT wording.
- Byte check: `grep -n -x -F -f <file> <card>` matches card line 26 to BASE `:137`, line 38 to BASE `:162`, line 32 to staged `:137`, line 44 to staged `:162`, and line 50 to staged `STANDING-LIST.md:149`.
- `grep -c -F -e` counts at BASE are 0 for all seven marker strings. After-copies: "orphan-clean.sh --kill aset" 2 in DEPLOY-HUB + 1 in STANDING-LIST; "orphan-clean.sh aset" 2; "the kill sequence:" 2; "ORPHAN-CLEAN, aset only" 1; "each resident booted out and not held DOWN" 1; "killing the orphaned" 1; "--kill com.cobalt.aset" 0.
- `ops/desk/orphan-clean.sh`: the label table is at `:76-82` (`aset` only, else REFUSED). It prints `none found` at `:174`, `WOULD KILL` at `:250` and `dry-run · verified` at `:252`.
- G5 (`ops/desk/bare-guard.py:1084-1089`): a build may write a fixed file only when a row's `files` cell names it. `read_card` (`:722-728`) takes the backticked paths of the last cell of each `|` line in `## ROWS`. K1/K2 name `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` and K3 names `STANDING-LIST.md`. The K3 TEXT line's last cell has no backtick, so it adds no file.
- `grep` of `STANDING-LIST|DEPLOY-HUB` over `tests/ops`: no test pins `:137`, `:162` or the allow table. `test_desk_launch_brain.py:498` reads `## 7.` of STANDING-LIST; K3 adds it to the red-first run.
- Precedent: `prompts/2026-10-05/26-hub-text-card.md` is the newest docs-only hub-text card. M6 was a desk commit (`7bc283fe`), not a card.
- Only the card and this report were written. No commit, no launch.

KILL HUB CARD DRAFTED · decisions: 2
