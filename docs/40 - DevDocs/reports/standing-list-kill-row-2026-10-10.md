## §0 Headline
- ONE row drafted in `STANDING-LIST.md:149` (§3, after the `launchctl print` row): `orphan-clean.sh --kill com.cobalt.aset`, deploy hub only, at 4.2 after the bootout and at STEP-5 (3) before the bootstrap, only after a dry run printed a verified orphan.
- `DEPLOY-HUB.md:137` (4.2) and `:162` (STEP-5 (3)): "dry run only" replaced by "dry run, then `--kill` only when the dry run printed a verified orphan". Other two defaults kept (no radar call; `date` plus dry run twice).
- Not committed; the row is marked DRAFT, awaiting his yes (R926 A).

## DECISIONS
- ASK DESK: the hub text still says "verified <n> ≥ 1 → `date`, same call again, then STEP-5 FOR DEJAN" (`DEPLOY-HUB.md:137`, `:162`), which I left, as ordered (change nothing else). It now sits beside the `--kill` wording without saying when the kill runs or what follows it. [15:00] Default: left as is; the desk should settle, before the commit, whether the kill comes right after the first verified dry run or after the two repeats, and what the hub does when the kill's own output is not clean.
- ASK DESK: the row's string column cites the class (a) allow `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`; the row adds no new command. [15:00] Default: no new string, per R411/R412.

## RECORDS
- `git -C /Users/cobalt/cobalt diff --stat` on the two files: `DEPLOY-HUB.md | 4 ++--` and `STANDING-LIST.md | 1 +`, 2 files, 3 insertions, 2 deletions. I touched no other file except this report.
- `--kill` count: `DEPLOY-HUB.md` 2 (`:137`, `:162`); `STANDING-LIST.md` 1 (`:149`).
- Row wording, `STANDING-LIST.md:149`, carries: deploy hub only; 4.2 after the bootout; STEP-5 (3) before the bootstrap; only after a dry run printed a verified orphan (ppid 1, `-m cobalt.aset`, not launchd's pid); no other seat; no other label (radar REFUSED, a new label is a new card); never standing outside those two steps.
- Basis: card `prompts/2026-10-10/229-orphan-clean-card.md` `## RECORDS`; the prior drafter's report `reports/deploy-hub-orphan-row-2026-10-10.md`.

KILL ROW DRAFTED · files: 2 · decisions: 2
