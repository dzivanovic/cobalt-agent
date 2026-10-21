# draft f5-x3-values-port — card 965

## §0 Headline
- Card `prompts/2026-10-20/965-f5-x3-values-port-card.md` drafted: job `f5-x3-values-port`, BAND LOW, BASE `bac9b683`, RESTARTS `com.cobalt.aset`, spec `git diff 20dd871d e9245a8e` (3 files, 43+, 4−).
- Pure re-application: main has not changed any spec file since `20dd871d`.
- Smoke read is the admitted `https://cobalt.taild24291.ts.net/` form; `deploy-smoke.sh` does not map it, and no hub step calls that script.
- Uncommitted; the desk commits the card before launch.

## DECISIONS
1. ASK DESK: the X3 report `reports/f5-x3-measure-2026-10-20.md`, cited by both new `# source:` comments, is off main's tree since revert `7e4f946d`. Default taken: card row D1 ports it byte-equal to `20dd871d` (docs only, no restart), proved by E1 (d). Strike D1 and E1 (d) to keep the port to three files. [01:14 EDT]
2. ASK DESK: `ops/desk/deploy-smoke.sh` maps curl to `http://127.0.0.1:5010/*` only, so a run of it on the deploy card would RED the https line (`curl reads http://127.0.0.1:5010/ only`). The hub runs (s) itself (`DEPLOY-HUB.md:157`) against the launch line's admitted `curl` entry (`:11`); `git grep deploy-smoke HEAD -- ops/` names only `deploy-step0.sh:47`, a comment. Default taken: https line kept as prompt 964 orders; the desk's `deploy-smoke.sh --dry-run` will print `WOULD REFUSE` for it. [01:14 EDT]

## RECORDS
- 01:11–01:16 EDT (`date`). Reads only; no git write; nothing committed; no model call.
- Read: prompt 964; `prompts/CARD.md`; cards 958, 963, 923 whole; `reports/deploy-f5-x3-values.md` whole; `writing-rules.md`.
- `git show HEAD:ops/desk/deploy-smoke.sh` (curl shape `http://127.0.0.1:5010/*` only).
- `git grep` HEAD: `DEPLOY-HUB.md` curl / smoke lines (`:11`, `:152`, `:157`); `deploy-card.sh` / `desk-launch.sh` (`deploy-card.sh:553` ancestor refusal, `:567-576` DEPLOY PROOF parse); `deploy-smoke` across HEAD; `BUILD-HUB.md:14` (`Edit(//Users/cobalt/cobalt-wt/**)`, `git show*`, `git diff *`), `:16` (Edit governs Write; never typed `rm`).
- `git rev-parse --short=8 HEAD` → `bac9b683`; `git log --oneline -6 main` → `bac9b683`, `da546c24`, `e8ee26f7`, `7e4f946d`, `d71bcb4a`, `cfefd31a`.
- `git diff --stat 20dd871d e9245a8e` → 3 files, 43+, 4−; `git diff 20dd871d e9245a8e` read whole.
- `git diff --stat 20dd871d main --` the three paths → nothing; `-- src configs tests ops` → 8 files, none a spec path.
- `git diff --stat main 20dd871d -- "docs/40 - DevDocs/reports/"` → `f5-x3-measure-2026-10-20.md | 182 +++`; `ls` of it on main → No such file.
- `git merge-base --is-ancestor e9245a8e main` → exit 0.
- Markers on HEAD: `source: UNMEASURED` → `2`; X3 source, `(warm model)`, cold-load string → `0`. On `e9245a8e`: UNMEASURED + X3 source → `2` combined.
- Anchors on HEAD: `modelaccess.yaml:18` `local.plan` (`:34` `timeout_s: 15`), `:70`, `:77-80`; `test_checkpoints_offline.py:553`; `jobs.yaml:86`.
- `ls /Users/cobalt/cobalt-wt/` → no `f5-x3-values-port`.

DRAFTED · decisions: 2
