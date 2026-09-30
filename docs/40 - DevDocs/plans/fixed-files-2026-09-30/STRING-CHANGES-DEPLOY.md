# STRING-CHANGES-DEPLOY — the deploy line's string changes from the other-house read (DRAFT 2026-09-30 · PROPOSED · NOT APPLIED)

His R60 condition: a command string changed by the close test or the other-house read of `DEPLOY-HUB.md` returns to him alone. Source: Grok's read `reports/deploy-hub-other-house-read-2026-09-30.md`; the brain's verdicts `reports/brain-desk-review-2026-09-30.md` `## READ OF THE DEPLOY-HUB READ`. The close test changed NO string. The text-only fixes (findings 1–4, 9, 10) are already in `DEPLOY-HUB.md`. Each change below only REMOVES power; none adds a command the hub did not have. On his yes the desk applies them to `DEPLOY-HUB.md` and `STANDING-LIST.md` §3, then runs the named sandbox test before install.

| # | finding | deploy line today | deploy line after | test before install (sandbox, `dontAsk`) |
|---|---|---|---|---|
| 1 | 5 | (no deny) | ADD DENY `Bash(git -C * commit*--no-verify*)` and `Bash(git -C * commit* -n*)` (the guard is skipped by `--no-verify`) | `commit --no-verify` refused |
| 2 | 6 | `Bash(git -C /Users/cobalt/cobalt revert --no-edit *)` | `Bash(git -C /Users/cobalt/cobalt revert --no-edit -m 2 *)` (`-m 1` would keep the new tree) | `revert --no-edit -m 1 x` refused |
| 3 | 7 | `Bash(git -C /Users/cobalt/cobalt tag *)` | five exact strings filled from the card: `tag scratch-allow-probe-<job>`, `tag -d scratch-allow-probe-<job>`, `tag pre-<job>`, `tag -d pre-<job>`, `tag <TAG>` (`tag -d deploy-2026-09-30-2` no longer matches) | `tag -d <other tag>` refused; the five run |
| 4 | 8 | `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)` | `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-*)` (the hub no longer edits `cto-<date>.md`) | Write `reports/deploy-x.md` ok, `reports/cto-x.md` refused |
| 5 | UNPROVEN | (no deny) | ADD DENY `Bash(COBALT_ENV=production uv run cobalt db migrate*--rollback*)` and `Bash(COBALT_ENV=production uv run cobalt db migrate*--down-to*)` (a deny beats an allow, whatever the prefix result) | allow `Bash(echo hi)`; `echo hi there` refused or allowed, recorded |

Count: 4 denies added, 1 allow narrowed, 1 allow replaced by 5, 1 allow narrowed = the deploy line's allow 54 → 58, deny 3 → 7 (to re-count at the apply).
