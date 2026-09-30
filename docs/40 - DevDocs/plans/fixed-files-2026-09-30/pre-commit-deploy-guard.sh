# DRAFT — NOT INSTALLED — TESTED IN PART: the third-pass copy ran in the 09-30 scratch test (item 2:
# refuses and lets through as written; fails open); the D3 fix below (fourth pass) is NOT TESTED.
#
# pre-commit-deploy-guard.sh — the addition to /Users/cobalt/cobalt/.git/hooks/pre-commit that refuses
# a desk commit on main while a deploy hub is live (cto-2026-09-30.md R34; the brain's RULED PROCESS
# item 5; checklist C2 and K19; DEPLOY-HUB.md rule B).
#
# WHERE IT GOES. INSERTED between line 1 (`#!/bin/sh`) and line 2 of the existing hook — ABOVE the
# desk row gate, never appended below it. The row gate is a pipeline whose exit status is the hook's
# only because it is the hook's LAST command; a block appended after it would swallow a row-gate
# refusal. This block ends by falling through, so the row gate still runs and still decides.
# .git/hooks is not tracked: the install is a hand edit of that one file, and his to order.
#
# WHAT IT REFUSES. A commit that is ALL of: made in the main tree /Users/cobalt/cobalt (a worktree's
# commit is a builder's or a gate's, never a desk commit on main); on branch main; staging at least
# one path that is not a deploy report; while a deploy hub is live.
#
# WHAT IT LETS THROUGH ON PURPOSE. The deploy hub's own commits on main: they stage exactly one
# `docs/40 - DevDocs/reports/deploy-<name>.md` (DEPLOY-HUB.md D2.0, STEP-7, a FAILED ending;
# desk-launch.sh refuses a deploy card whose REPORT is not of that shape), and its allowlist probe
# (`commit --allow-empty`, nothing staged).
#
# HOW IT DECIDES "LIVE". By LIST state, the way /Users/cobalt/.claude/ops/desk-list.sh tells a live
# session from a finished one: a row of `claude agents --json` that still has a `pid`. A deploy hub
# is a live row whose name starts `deploy-hub-` — the name DEPLOY-HUB.md's launch line gives
# (`--name deploy-hub-<job>`). NOT a lock file: a lock file needs a writer and a remover; desk-launch.sh
# runs the launch (loop 2) but removes nothing after the stop line, the hub has no listed string that
# creates or removes one, and a stale lock would refuse every desk commit until someone noticed.
#
# FALSE POSITIVES (a lawful desk commit refused):
#   1. The hub wrote its stop line but is still listed (its row keeps a pid until `claude stop` +
#      `claude rm`). Cure: verify, stop and remove the hub first (checklist W8), then commit.
#   2. A hub that ended FAILED before touching anything and sits idle: the same cure.
#   3. Any session someone named `deploy-hub-…` that is not a deploy.
#   4. The hub's own commit, if its report path is not `reports/deploy-<name>.md` or it stages a
#      second file: the hub then ends FAILED on a refused commit. desk-launch.sh closes the first
#      case; DEPLOY-HUB.md commits by explicit path, which closes the second.
#
# FALSE NEGATIVES (a desk commit let through while a deploy runs):
#   1. A desk commit that stages ONLY `reports/deploy-<name>.md` files (moving an attempt's report
#      aside). It still moves main by one commit and makes 4.3's fast-forward refuse.
#   2. A deploy hub launched without `--name deploy-hub-…` (a hand launch, or an old prompt's line).
#   3. `claude agents --json` unreadable from the hook (the CLI not on the hook's PATH, a changed
#      output shape) or `python3` missing or failing: the guard WARNS on stderr and lets the commit
#      through — it fails open, loud. The Python prints `NONE` when no row matches and the pipeline
#      ends `|| echo UNREADABLE`, so an empty answer never means "no hub" (scratch test D3).
#   4. The seconds between the launch and the hub's row appearing in the list.
#   5. `git commit --no-verify`; and `git merge`, `git revert`, `git cherry-pick`, `git rebase`,
#      which do not run pre-commit.
#   6. A change made by Edit / Write and left uncommitted is not a commit: the guard does not see
#      it (DEPLOY-HUB.md D0 refuses a dirty `src/`, `tests/`, `ops/`, `configs/` path itself).
#
# PROVEN (scratch item 5): a git hook run from a Claude session finds the real `claude` and `python3`
# on its PATH. NOT TESTED: the real `claude agents --json` row shape (read from desk-list.sh: `pid`,
# `id`, `name`; the scratch runs used a stub list).

# ---- deploy guard (begin) ---------------------------------------------------------------------
if [ "$(git rev-parse --show-toplevel 2>/dev/null)" = "/Users/cobalt/cobalt" ] \
   && [ "$(git symbolic-ref --short -q HEAD)" = "main" ]; then
    guard_other=$(git -c core.quotePath=false diff --cached --name-only \
        | grep -v '^docs/40 - DevDocs/reports/deploy-[^/]*\.md$')
    if [ -n "$guard_other" ]; then
        guard_live=$(claude agents --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.load(sys.stdin)
except Exception:
    print("UNREADABLE")
    sys.exit(0)
hit = 0
for a in rows:
    if a.get("pid") and str(a.get("name", "")).startswith("deploy-hub-"):
        print("%s %s" % (a.get("id", "?"), a.get("name")))
        hit = 1
if not hit:
    print("NONE")
' 2>/dev/null || echo UNREADABLE)
        case "$guard_live" in
            NONE)
                ;;
            ""|UNREADABLE*)
                echo "pre-commit: deploy guard could not read the session list (claude agents --json); NOT enforced for this commit." >&2
                ;;
            *)
                echo "pre-commit: a deploy hub is live — no desk commit on main until its stop line:" >&2
                echo "$guard_live" >&2
                echo "Write by Edit / Write only; commit after DEPLOYED or FAILED, once the hub is stopped and removed." >&2
                exit 1
                ;;
        esac
    fi
fi
# ---- deploy guard (end) — the desk row gate below stays the hook's last command ----------------
