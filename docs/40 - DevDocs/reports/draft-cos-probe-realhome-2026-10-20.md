# draft-cos-probe-realhome — 2026-10-20

## §0 Headline
- WROTE card `prompts/2026-10-20/918-cos-probe-realhome-card.md`: job `cos-probe-fr2`, a fresh job on `ops/cos-probe-fr2` from BASE `56abaea2`, BAND HIGH, CLASS K2, RESTARTS `com.cobalt.radar`. No migration.
- Four code rows. H1 runs the probe under the real HOME; the auth check stays first. H2 makes the scratch cwd the only place the probe writes, and moves the plant there. H3 quotes `loggedIn` and `authMethod` only. H4 is a control showing no file under the real HOME is opened, and states the bound on what the CLI writes there. R1 and D0 are as in 877.
- Red-first: H1, H2 and H3 each fail on BASE (`under the scratch HOME`, or the env's HOME is the scratch one). H4 is a control with a mutation. X-item pass rules are unchanged. The DONE test is the gate re-running the six items after deploy (CHECK ASK X6).
- Committed nothing.

## DECISIONS
1. ASK DESK: under the real HOME, a "planted user-config MCP server" (FINAL `:84`, `:91`) would mean writing to his `~/.claude.json`, which is barred. Default (row H2): the plant becomes a project-scope `<scratch>/work/.mcp.json`. X11's rule is unchanged: init tools ⊆ the seven. That rule now also proves his real user config adds no tool, without the probe reading it. [12:34]
2. ASK DESK: "its output quoted" for `claude auth status`. The raw output carries his email and org (`cos-gate-run-2026-10-20.md:72` shows a JSON with more keys). Default (row H3): quote only `loggedIn=<v> authMethod=<v>`, as one stderr line on every run and in the FAIL clause. The stdout shape and the OK lines are unchanged. [12:34]
3. ASK DESK: the CLI's own state under the real HOME (`~/.claude.json` project entries, `~/.claude/projects/<cwd slug>/` transcripts, caches) is stated and bounded but not measured. That is 7 scratch cwds and at most 67 sessions at the gate, and the probe cleans none of it. Check G4 asked for a listing. Default: neither the probe nor the build lists `~/.claude/` (fenced). The desk may add a name-only `ls ~/.claude/projects` before and after to the gate re-run prompt. [12:34]
4. ASK DESK: BASE is main's HEAD at my read, `56abaea2`. The desk resets it at launch, as the prompt says. RULINGS is `2026-10-18 R1863` (as 877), because R2177 is a DESK RECORD, not his ruling. Default: as written. [12:34]

## RECORDS
- `date`: 12:30 start, 12:33 card reads, 12:34 card and report written.
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `56abaea2`. `git status --short -- src tests configs/cobalt/agents ops` → nothing. `git diff --stat HEAD -- src/cobalt/jobs/restarts.py src/cobalt/cos tests/cobalt/test_cos_probe.py configs/cobalt/jobs.yaml` → nothing.
- Read whole: prompt 917; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `prompts/CARD.md`; `prompts/2026-10-19/877-cos-probe-card.md`; `git show HEAD:src/cobalt/cos/probe.py`; `git show HEAD:tests/cobalt/test_cos_probe.py`; `git show HEAD:src/cobalt/cos/session.py`; `reports/cos-gate-run-2026-10-20.md`; `reports/draft-cos-gate-rerun-2026-10-20.md`; `reports/cos-probe-fr1-check-2026-10-20.md`.
- Read in part: `prompts/BUILD-HUB.md:1-20` (`:14` the line, `:16` never typed); `src/cobalt/jobs/restarts.py:178-264`.
- `git grep -n` at HEAD, each card anchor: `probe.py` `:12`, `:130-137`, `:166-176`, `:179-183`, `:246`, `:293-300`, `:317`, `:437-461`, `:454`; `session.py:54`, `:93`, `:105`, `:106`, `:108`, `:118`; `test_cos_probe.py:120`, `:143-149`, `:197-200`, `:288`, `:322`, `:412`, `:416`, `:481`; `jobs.yaml:193`, `:203`, `:206`, `:226`; `cli.py:87`; `F20-FINAL-2026-10-11.md:84`, `:91`; `cos/README.md` headings (`:49` the last one); `cos-gate-run-2026-10-20.md:10-17`, `:72`; `cos-probe-fr1-check-2026-10-20.md:121`, `:123`, `:141`, `:192`; `draft-cos-gate-rerun-2026-10-20.md:12`; `BUILD-HUB.md:14`, `:16`; `cto-2026-10-18.md:90` R1863; `cto-2026-10-20.md:20` R2177, `:21` R2176.
- DEPLOY PROOF before values, each by `grep -c -F` on main's tree at 12:33. `under the scratch HOME` in `probe.py` → `1`. `.claude.json` in `probe.py` → `2`. The H1 test name in `test_cos_probe.py` → `0`. The `cos-probe-fr2` README heading → absent (the `^## ` listing).
- `ls` of the card path and of `/Users/cobalt/cobalt-wt/cos-probe-fr2` → no such file.
- Not run: `uv run` and `claude`, which are off this seat's line. Row R1 is the RESTARTS record.
- Wrote only: the card and this report.

DRAFTED · decisions: 4
